# WATER + Spin in the Homelab — Design & Placement

*A design note (docs + diagrams). Code blocks are illustrative but use the real
`refraction-networking/water` **v0.6.4** API and Fermyon Spin APIs so they can be
lifted into a real build later. Nothing here is deployed yet.*

---

## 0. The one thing to get right first

**Spin is not a WATER runtime, and a WATM is not a Spin component.**
Both are WebAssembly, but they are different *host ABIs*:

| | Fermyon **Spin** | **WATER** |
|---|---|---|
| Guest shape | request/response **component** | long-lived **transport module (WATM)** |
| Trigger | HTTP / Redis / cron | n/a — it's a byte-stream transform |
| Guest ABI | `wasi:http`, `wasi:sockets`, Component Model (WASI 0.2) | custom: exports `init/dial/accept/worker`, imports `host_dial/host_accept/pull_config` (WASI **Preview 1**) |
| Host runtime | `spin` / SpinKube shim | `wazero` (Go) or `wasmtime` (Rust) embedded in *your* app |

➡️ You **cannot** load `plain.wasm` into Spin and have it obfuscate traffic —
Spin never provides the `host_dial` import a WATM needs. So we use each runtime
for what it is actually good at, at **two different layers**:

- **Data plane = WATER** — a tiny Go service that embeds the WATER runtime, loads
  a WATM, and obfuscates egress. *This is the part that actually evades DPI.*
- **Control plane = Spin** — a Spin HTTP app on SpinKube that **serves + signs +
  rotates** the WATMs out-of-band (the paper's "ship a new `.wasm` without an
  app-store/CDN update" story).

### Why bother at all — what WATER buys you over your current Gluetun tunnel
Your VLAN 40 egress is WireGuard via Gluetun. WireGuard/OpenVPN tunnels are
**fingerprintable** (Xue et al., *"OpenVPN is Open to VPN Fingerprinting"*,
USENIX Sec '22 — cited by the WATER paper). A censor's DPI can classify the
tunnel even without decrypting it. WATER wraps a stream in a **hot-swappable**
transport (e.g. a TLS-mimic WATM) so egress looks like benign traffic, and when a
technique gets blocked you push a new `.wasm` instead of redeploying anything.

> ⚠️ WATER gives you **transport obfuscation, not anonymity**. No relays, no
> onion routing. It is "the pluggable-transport pipe," not "Tor the network."

---

## 1. Data-plane topology (how the bytes actually move)

WATER needs **both ends** running the *same* WATM: a **Dialer** (inside your
network) and a **Listener** (an egress **bridge** you control on a VPS outside the
censored/monitored path). The WATM is a transparent byte transform, so we tunnel
a normal SOCKS5 session *through* it and let a plain SOCKS5 daemon on the bridge
do the real internet egress:

```
   your workload                         water-proxy                    (public VPS bridge)
 ┌───────────────┐   SOCKS5   ┌────────────────────────────┐        ┌────────────────────────────┐
 │ browser / pod │──────────▶ │  TCP :1080                 │        │  WATER Listener :443        │
 │ curl --socks5 │  (raw      │  WATER **Dialer** (WATM)   │──obfs──▶│  (same WATM) decodes bytes  │
 └───────────────┘   SOCKS5   │  loads current .wasm       │  looks  │            │                │
                     bytes)   └────────────────────────────┘  like   │            ▼                │
                                          ▲                    TLS    │  microsocks :1055 ──▶ WAN   │
                                          │ WATM pulled/rotated       └────────────────────────────┘
                                          │ from Spin control plane
                              ┌────────────────────────────┐
                              │ Spin app (SpinKube, Lab)   │
                              │  GET /watm/current  (.wasm) │
                              │  GET /watm/manifest.json    │
                              │  ed25519-signed, versioned  │
                              └────────────────────────────┘
```

- `water-proxy` does **not** parse SOCKS5 — it just forwards the raw client bytes
  through the WATER Dialer. The SOCKS5 handshake happens **end-to-end** between
  your workload and `microsocks` on the bridge, fully obfuscated in transit.
- Swap `plain.go.wasm` (demo, identity transform) for a real TLS-mimic /
  Shadowsocks WATM in production. Same code, different `.wasm`.

### Data-plane code — the client side (`water-proxy`)
Verified against `refraction-networking/water` v0.6.4:

```go
import (
    "context"
    "io"
    "net"
    "os"

    "github.com/refraction-networking/water"
    _ "github.com/refraction-networking/water/transport/v0" // MUST register a version or it panics
)

func main() {
    wasm, _ := os.ReadFile(os.Getenv("WATM_PATH"))     // pulled from the Spin control plane
    bridge := os.Getenv("BRIDGE_ADDR")                 // e.g. bridge.example.com:443

    cfg := &water.Config{
        TransportModuleBin: wasm,
        NetworkDialerFunc:  net.Dial,                  // how the WATM reaches the network
    }
    cfg.ModuleConfig().InheritStdout()
    cfg.ModuleConfig().InheritStderr()

    ln, _ := net.Listen("tcp", ":1080")                // local SOCKS5 entrypoint for workloads
    for {
        client, _ := ln.Accept()
        go func() {
            defer client.Close()
            dialer, err := water.NewDialerWithContext(context.Background(), cfg)
            if err != nil { return }
            // obfuscated hop to the bridge; whatever we relay is WATM-transformed on the wire
            up, err := dialer.DialContext(context.Background(), "tcp", bridge)
            if err != nil { return }
            defer up.Close()
            go io.Copy(up, client)
            io.Copy(client, up)
        }()
    }
}
```

### Data-plane code — the bridge side (`water-bridge`, on a VPS)
```go
import (
    "context"
    "io"
    "net"
    "os"

    "github.com/refraction-networking/water"
    _ "github.com/refraction-networking/water/transport/v0"
)

func main() {
    wasm, _ := os.ReadFile(os.Getenv("WATM_PATH"))     // SAME watm as the proxy
    upstream := os.Getenv("UPSTREAM_SOCKS")            // 127.0.0.1:1055 (microsocks)

    cfg := &water.Config{TransportModuleBin: wasm, NetworkDialerFunc: net.Dial}
    cfg.ModuleConfig().InheritStdout()
    cfg.ModuleConfig().InheritStderr()

    ln, _ := cfg.ListenContext(context.Background(), "tcp", ":443") // WATER Listener
    for {
        conn, _ := ln.Accept()                          // bytes arrive de-obfuscated
        go func() {
            defer conn.Close()
            up, err := net.Dial("tcp", upstream)        // hand the SOCKS5 stream to a real SOCKS server
            if err != nil { return }
            defer up.Close()
            go io.Copy(up, conn)
            io.Copy(conn, up)
        }()
    }
}
```

That's the whole data plane: ~40 lines each side + a stock `microsocks` container
for real egress. The intelligence lives in the `.wasm`, which is exactly the point.

---

## 2. Control-plane code — the Spin WATM server

A Spin HTTP component that serves the current signed WATM + a manifest. Runs on
**SpinKube** in your Lab cluster (containerd `spin` shim), so it's just another
K8s workload behind your Gateway. Illustrative Rust component:

```rust
// src/lib.rs  (spin_sdk http component)
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;

#[http_component]
fn handle(req: Request) -> anyhow::Result<impl IntoResponse> {
    match req.path() {
        "/watm/manifest.json" => Ok(Response::builder()
            .status(200)
            .header("content-type", "application/json")
            .body(include_str!("../watmd/manifest.json"))  // {version, sha256, ed25519_sig, params}
            .build()),
        "/watm/current" => Ok(Response::builder()
            .status(200)
            .header("content-type", "application/wasm")
            .header("x-watm-version", "2024.08-tls-mimic")
            .header("x-watm-sig", include_str!("../watmd/current.sig"))
            .body(include_bytes!("../watmd/current.wasm").to_vec())
            .build()),
        _ => Ok(Response::new(404, "not found")),
    }
}
```

```toml
# spin.toml
spin_manifest_version = 2
[application]
name = "watm-server"
version = "0.1.0"

[[trigger.http]]
route = "/watm/..."
component = "watm-server"

[component.watm-server]
source = "target/wasm32-wasi/release/watm_server.wasm"
```

**WATM lifecycle the control plane enforces:**
1. Build the WATM (`refraction-networking/watm`, Rust or TinyGo → `wasm32-wasi`).
2. `sha256` + **ed25519 sign** it (offline key; the paper stresses signing —
   a malicious WATM can still open arbitrary sockets, WASM sandboxes *execution*
   not *intent*).
3. Publish via the Spin app (`/watm/current` + `/watm/manifest.json`).
4. `water-proxy` / `water-bridge` fetch on boot (and on a rotation signal),
   **verify the signature**, then hot-swap — no container rebuild, no app-store.

---

## 3. Where it sits in *your* stack (both placements)

Your current egress reality (from `homelab/docs`):
- **VLAN 40 (Downloads)** — Gluetun (WireGuard) + qBittorrent, firewalled off all
  LAN (rules 12/`Block-Downloads-to-LAN`), WAN via VPN only.
- **VLAN 70 (Lab)** — Talos K8s, Cilium CNI + **Egress Gateway**, Gateway API /
  Kgateway, ClusterMesh across `admin`/`application`/`mlops`.
- **External Gateway** — Cloudflare tunnel for inbound.

### Variant A — WATER as a Lab egress pod (VLAN 70) — *data-plane, K8s-native*

```
                            ┌────────────────────────────────────────────┐
   Lab VLAN 70 (Talos)      │  Cilium Egress Gateway ──▶ UDM Pro ──▶ WAN  │
                            └───────────────▲────────────────────────────┘
                                            │ obfuscated (WATM)
  ┌──────────────┐  SOCKS5   ┌──────────────┴───────────────┐    fetch/rotate   ┌──────────────────┐
  │ research pod │─────────▶ │ water-proxy  (Deployment)     │◀─── /watm/... ────│ watm-server      │
  │ (browse/AI/  │           │  :1080  WATER Dialer + WATM   │                   │ (SpinKube SpinApp)│
  │  scrape)     │           │  ClusterIP svc `water-egress` │                   │  Lab VLAN 70      │
  └──────────────┘           └───────────────────────────────┘                   └──────────────────┘
        set HTTP(S)_PROXY / SOCKS to water-egress:1080                     Spin exposed via Gateway API
                                            │
                                            ▼  (WATM-obfuscated TCP :443)
                                   public VPS  →  water-bridge + microsocks  →  Internet
```

- **Consumers:** your **research / browsing / scraping** workloads
  (`platform/research.md`, `platform/ai.md` outbound) point `SOCKS5`/`HTTPS_PROXY`
  at the `water-egress` ClusterIP service.
- **K8s shape:** `Deployment` (water-proxy) + `Service` (ClusterIP `:1080`);
  `SpinApp` CRD for the control plane; an `HTTPRoute` if you expose `/watm/...`
  in-cluster or via Cloudflare.
- **NetworkPolicy (Cilium):** only the research namespace may reach
  `water-egress:1080`; `water-egress` may egress only to the bridge IP:443.

### Variant B — WATER chained *inside* Gluetun (VLAN 40) — *defense-in-depth / DPI fallback*

```
  VLAN 40 (Downloads, isolated from all LAN)
  ┌────────────┐      ┌────────────────────────┐      ┌──────────────────┐      ┌──────────────┐
  │ qBittorrent│────▶ │ water-proxy sidecar     │────▶ │ Gluetun (WG tun) │────▶ │  WAN / VPN   │
  │            │ SOCKS│  WATER Dialer + WATM     │ obfs │  network_mode    │  WG  │  provider    │
  └────────────┘      └────────────────────────┘      └──────────────────┘      └──────────────┘
        obfuscated stream is what rides the WireGuard tunnel  →  even the VPN provider / on-path
        DPI sees a benign-looking inner transport, and if the WG tunnel itself is fingerprinted &
        throttled, you can flip the WATM to a domain-fronting / TLS-mimic transport without touching
        the compose stack.
```

Docker-compose sketch (fits your existing Gluetun pattern):

```yaml
services:
  gluetun:            # unchanged — your existing WireGuard egress
    image: qmcgaw/gluetun
    cap_add: [NET_ADMIN]
    devices: ["/dev/net/tun:/dev/net/tun"]

  water-proxy:        # NEW: obfuscation sidecar, egresses through gluetun
    image: homelab/water-proxy:latest
    network_mode: "service:gluetun"      # its traffic rides the VPN tunnel
    environment:
      WATM_URL: "http://watm-server.lab.svc/watm/current"   # pull from Spin
      BRIDGE_ADDR: "bridge.example.com:443"

  qbittorrent:
    image: qbittorrentofficial/qbittorrent-nox
    network_mode: "service:gluetun"
    environment:
      # point qBit's proxy at the local water-proxy SOCKS entrypoint
      QBT_PROXY: "socks5://127.0.0.1:1080"
```

> Note: WATER-in-tunnel costs throughput (see §5). For bulk torrent traffic,
> Variant B is more of a *"break glass when the VPN is being fingerprinted"*
> switch than an always-on layer. Variant A (targeted research egress) is the
> everyday use.

---

## 4. Firewall / VLAN deltas you'd add

| # | Src | Dst | Port | Action | Why |
|---|-----|-----|------|--------|-----|
| A1 | Lab (70) research ns | `water-egress` svc | 1080 | ALLOW | workloads → proxy |
| A2 | `water-egress` pod | bridge VPS IP | 443 | ALLOW | obfuscated egress only |
| A3 | `water-egress` pod | ANY other | ANY | DENY | no side-channel leaks |
| B1 | VLAN 40 | bridge VPS IP | 443 | ALLOW (via Gluetun) | chained variant egress |
| C1 | Lab (70) | `watm-server` (Spin) | 443 | ALLOW | fetch/rotate WATMs |

The bridge (`water-bridge` + `microsocks`) lives **off-net on a VPS** — it is the
"unblocked side," so it must not be inside VLAN 40/70.

---

## 5. Honest limitations (don't skip these)

- **Throughput.** WATER's WASM path is slow: the paper measures WATER-Shadowsocks
  at **~56 Mbps vs ~415 Mbps native**, and WASM AES ~**20× slower** than native.
  Fine for browsing/research; a real tax on bulk downloads.
- **WASI Preview 1, 32-bit only** — `usize` is 32-bit; adequate for AEAD framing,
  but a constraint when authoring WATMs.
- **You must run + trust a bridge.** WATER is two-ended; no bridge = nothing to
  obfuscate *to*. Budget a small VPS.
- **Sign your WATMs.** WASM isolates execution, not intent — an unsigned WATM can
  still open arbitrary sockets and exfiltrate.
- **Not anonymity.** Pair with Tor/relays if unlinkability (not just
  unblockability) is the goal.
- **Maturity.** WATER is research-grade, from **Refraction Networking** (UMich +
  CU Boulder). Latest *stable* Go release is **v0.6.4** (Mar 2024) with a
  **v0.7.1-alpha** prerelease (Jun 2025); the Rust runtime is stuck at v0.1.0.
  **No shipping consumer tool is known to embed WATER yet** (verified: not Tor,
  Psiphon, Outline/Jigsaw, or any VPN as of this research) — the paper's own
  "Future Work" still lists real-world deployment as aspirational. Treat this as a
  lab/experimental transport, not a hardened production dependency.
- **WATM spec versions.** The snippets here pin `transport/v0` (what the repo's
  `examples/v0/` ship). A newer **v1 spec** exists (v0 is deprecated; v1 exports
  `watm_dial_v1`/`watm_accept_v1`/`watm_start_v1`) — still WASI Preview 1. Use v1
  for anything beyond a demo.

---

## 6. If you later promote this to real infra
- `water-proxy` / `water-bridge` → one small Go module, two `cmd/` binaries,
  distroless images.
- Control plane → `SpinApp` CRD + `HTTPRoute`; WATM artifacts in R2/KV, ed25519
  key in your existing secrets flow (SOPS).
- Wire rotation to a `CronJob` or a Spin `/watm/rotate` webhook.
- Add a Cilium `CiliumNetworkPolicy` implementing the §4 table.

*Filed under research: `knowledge/tree/networking/censorship` — this is the
applied companion to the WATER-vs-Tor comparison.*
