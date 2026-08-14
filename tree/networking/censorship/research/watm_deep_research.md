---
name: WATM
title: "WATER / WATM vs Tor and other circumvention transports"
description: >-
  Deep-research comparison of WATER (WebAssembly Transport Executables Runtime)
  and its hot-swappable WATMs against Tor, Tor Pluggable Transports, Proteus,
  Marionette, Shadowsocks, and VPNs — plus how it is actually used today.
summary: research note
category: research
agent: privacy-expert
skill: deep-research
tags:
  - censorship
  - circumvention
  - pluggable-transports
  - webassembly
  - tor
  - water
  - watm
created: '2026-08-09'
last_updated: '2026-08-09'
---

# WATER / WATM vs Tor and other circumvention transports

> Synthesis of two verified research passes (a 104-agent deep-research run with
> 3-vote adversarial verification, and a focused primary-source usage brief),
> grounded in the FOCI 2024 paper *"Just add WATER"* (`foci-2024-0003.pdf` in
> this directory). Every claim below traces to a primary source in
> [Sources](#sources). Confidence is high on the technical description and
> benchmarks; adoption/maturity is deliberately hedged (see [Caveats](#caveats)).

## TL;DR

**WATER is a delivery mechanism for pluggable transports, not an alternative to
Tor.** It is a runtime library that loads a hot-swappable WebAssembly Transport
Module (**WATM**, a `.wasm` binary) which wraps a network connection in an
application-layer transport (TLS-mimic, Shadowsocks, etc.). Its one real
advantage over prior approaches is **portability + over-the-network updates**:
ship a new transport as a single `.wasm` + config, reusable across tools written
in different languages, with no app rebuild or app-store review. You pay for that
with **throughput** (WASM has no hardware crypto acceleration) and it provides
**no anonymity and no relays** — that is Tor's job, not WATER's.

- **WATER** = *WebAssembly Transport Executables Runtime* — the host library
  (Go on `wazero`, Rust on `wasmtime`).
- **WATM** = *WebAssembly Transport Module* — the hot-swappable `.wasm` transport.
- Maintained by **Refraction Networking** (UMich + CU Boulder); **research-grade,
  no confirmed production adoption** as of this research.

## What WATER/WATM actually is

From the paper's abstract, WATER "enables applications to use a WebAssembly-based
application-layer (e.g., TLS) to wrap network connections and provide network
transports," and "deploying a new circumvention technique with WATER only
requires distributing the WATM binary and any transport-specific configuration,
allowing dynamic transport updates without any change to the application itself."

Two components:

1. **Runtime library** — embedded by a circumvention tool. Exposes a `net`-style
   API (Dialer / Listener / Relay). The developer loads a `.wasm`, gets back a
   normal connection, and the WATM transparently obfuscates the byte stream.
2. **WATM (`.wasm`)** — the transport logic, compiled from Rust / Go(TinyGo) /
   (prospectively) Python(CPython), C, Zig. Implements a fixed host/guest ABI
   over **WASI Preview 1**.

## The core comparison

| Approach | Portability | Update path | Anonymity | Notes |
|---|---|---|---|---|
| **WATER / WATM** | Any WASI runtime; WATM compiled from many languages | **Ship a `.wasm` over the network — no app update** | ❌ none | Transport-obfuscation delivery layer |
| **Tor Pluggable Transports** (obfs4, meek, Snowflake, WebTunnel) | Language-specific, **mutually incompatible APIs (Go/Java/Swift)** | Recompile + redeploy client (app-store review) | ✅ via Tor network | The framework WATER most directly competes with |
| **Proteus** | Rust-based **DSL**, self-contained; hard to embed in non-Rust tools | Compile PSF spec | ❌ none | Programmable protocols, but bespoke DSL |
| **Marionette** | Non-Turing-complete **FTE DSL**; plugins need recompilation | Redeploy | ❌ none | Format-transforming encryption templates |
| **Shadowsocks / fully-encrypted proxies** | Native per-platform builds | Recompile + redistribute | ❌ none | Fast; but fingerprintable (GFW blocks fully-encrypted traffic) |
| **VPNs (OpenVPN / WireGuard)** | Native clients | Reconfigure | ❌ none (obscures, doesn't anonymize) | **Tunnels are fingerprintable** (Xue et al., USENIX Sec '22) |
| **Tor (the network)** | Cross-platform bundle | App update | ✅ **onion routing / relays** | A different layer entirely — anonymity, not just unblocking |

**Key distinction:** WATER competes with the *pluggable-transport layer* (obfs4,
Proteus, Marionette) — a peer to "the pipe." Tor-the-network is the anonymity
layer above it. To get Tor-like unlinkability you would run a WATM *underneath*
something that actually provides relays.

## "I know how to use Tor…" — the usage asymmetry

The sharpest way to understand WATER is by contrast with the Tor end-user
experience. There is **no consumer front-end** for WATER — no browser, no
"Connect" button. It is a developer SDK.

| A Tor user does… | WATER analog | Status |
|---|---|---|
| Install Tor Browser | *No equivalent* — a developer adds the `water` Go module / Rust crate to their app | absent |
| Click "Connect" / bootstrap | *No bootstrap* — the app `DialContext`s a single pre-configured server; no directory/consensus/discovery | absent |
| Choose a bridge / PT (obfs4, Snowflake) | **Select a WATM** (`plain.wasm`, `shadowsocks.wasm`, custom) — this is the real analog | present |
| Get anonymity via relays | **None** — one obfuscated hop, no relays | absent |

So "using WATER" is always one of two developer jobs:

- **Integrate the runtime** — embed WATER, load someone's WATM:
  ```go
  import _ "github.com/refraction-networking/water/transport/v0" // register a version or it panics
  wasm, _ := os.ReadFile("shadowsocks.wasm")
  cfg := &water.Config{TransportModuleBin: wasm, NetworkDialerFunc: net.Dial}
  dialer, _ := water.NewDialerWithContext(ctx, cfg)
  conn, _ := dialer.DialContext(ctx, "tcp", remoteAddr) // ordinary net.Conn
  ```
  Server side is `cfg.ListenContext(...)` → `Accept()`; relay is
  `water.NewRelayWithContext(...)` → `ListenAndRelayTo(...)`.
- **Author a WATM** — write the obfuscation in Rust/TinyGo, compile to
  `wasm32-wasi`, implement the ABI (`init`/`dial`/`accept`/`worker`, importing
  `host_dial`/`host_accept`/`pull_config`). Prebuilt examples ship in-repo:
  `plain` (identity), `reverse` (byte-flip), `shadowsocks` (real, Rust). The
  official Go compiler is **not** supported — TinyGo only.

> WATM spec versions: **v0 is deprecated**; **v1** ("first production-ready" spec:
> `watm_dial_v1` / `watm_accept_v1` / `watm_start_v1`) supersedes it. Both are
> WASI Preview 1.

## Performance — the portability tax

Real-world iperf3, Michigan→San Francisco, M1 Max (paper Table 6):

| Transport | Throughput | vs native |
|---|---|---|
| shadowsocks-rust (native) | **~415–418 Mbps** | baseline |
| Proteus-SS | 68–96.6 Mbps | ~17–23% |
| **WATER-SS** | **~56 Mbps** | **~13.6% (~7× slower)** |

Root cause: WebAssembly has **no hardware crypto acceleration** (no AESNI/SIMD).
AES-256-GCM on 256 B ran **230 µs native vs 5300 µs in WASM (~23×)**. General WASM
overhead is smaller (~45–55% slower on SPEC CPU, Jangda et al. ATC '19) — the
crypto gap dominates. The authors argue ~50 Mbps "is very unlikely to be the
bottleneck in a real-world circumvention scenario," and note AOT compilation and
`wasi-crypto` could narrow the gap. **Verdict: fine for browsing/research; a real
tax on bulk transfer.**

## Architecture: obfuscation vs anonymity

- **Tor** is "a distributed overlay network designed to anonymize low-latency
  TCP-based applications" — onion routing across relays. Its PTs (obfs4, meek,
  Snowflake, WebTunnel) only disguise the *entry* traffic.
- **WATER** wraps a single connection's bytes. It has **no relays, no directory,
  no anonymity**. The "not anonymity" point is an accurate inference from the
  paper's scope, not an explicit disclaimer the authors wrote.

Correct mental model: **WATER ≈ a portable, hot-swappable runtime for
obfs4/Snowflake-style transports**, competing with Tor's PT framework and with
Proteus — not with Tor itself.

## WATER vs XTLS / VLESS (Xray)

> Note: REALITY/XTLS specifics below come from the Xray/Project X docs and
> community source analysis, not the peer-reviewed record — treat as
> well-documented engineering, not academic measurement.

**They are different layers, not competitors.** VLESS+XTLS is a concrete,
production transport you deploy; WATER is a runtime for *delivering* transports.

- **VLESS** — a stateless, lightweight proxy protocol from Xray/Project X
  (successor to VMess). It carries **no built-in encryption** — just a UUID +
  routing envelope — and delegates confidentiality to the TLS/XTLS layer beneath,
  minimizing overhead and fingerprint surface.
- **XTLS** — the TLS camouflage/optimization family under VLESS:
  - **XTLS-Vision** removes the **TLS-in-TLS** fingerprint/overhead by splicing
    the inner stream, so proxied TLS doesn't look like TLS-wrapped-in-TLS to DPI.
  - **REALITY** — the headline anti-GFW technique: the server acts as a MITM for a
    real high-reputation site (e.g. Apple/Bing). It fetches a **genuine ServerHello
    from that target** and relays it; the client authenticates via a private key
    hidden in modified handshake fields invisible to a prober. An unauthenticated
    probe just gets proxied to the real site and fails cleanly. Result: **no fake
    cert to catch, SNI hidden, active probing defeated — and no domain/cert of your
    own required.**

**How it differs from WATER:**

| | **VLESS + XTLS/REALITY** | **WATER / WATM** |
|---|---|---|
| Category | Proxy protocol + TLS camouflage technique | Runtime that loads swappable transports |
| Anti-DPI technique | **Built-in, state-of-the-art** (REALITY, Vision) | **None of its own** — lives in the WATM you load |
| Engine | Xray-core, **Go, native** (hardware crypto) | wazero/wasmtime running **WASM** |
| Performance | **Near-native** | **~7× slower** throughput; ~23× slower AES |
| Update model | Update native binary + JSON config | **Hot-swap a signed `.wasm`**, cross-language reuse |
| Adoption | **Dominant real-world anti-GFW stack** | Research prototype |
| Anonymity | ❌ single-hop | ❌ single-hop |
| Own domain/cert? | REALITY: **not needed** (borrows a real one) | N/A |

**They compose rather than compete.** A REALITY/uTLS-style technique is exactly
the *kind of thing you would author as a WATM*; WATER is the meta-layer that
distributes it. Practical posture: run **VLESS+REALITY** natively (e.g. via an
Xray operator) for fast, proven egress *today*; reach for **WATER** when you want
hot-swap transport agility over raw throughput. Shared thread: both ecosystems
rely on **uTLS** (browser TLS-fingerprint mimicry) — maintained by Refraction
Networking, the same group behind WATER.

## How it's used today (2024–2026)

- **Maintainer:** Refraction Networking. Repos: `refraction-networking/water`
  (Go, formerly `gaukas/water`), `refraction-networking/water-rs` (Rust),
  `refraction-networking/watm` (module tooling).
- **Maturity:** Go runtime stable at **v0.6.4** (Mar 2024) with a
  **v0.7.1-alpha** prerelease (Jun 2025); Rust runtime stuck at **v0.1.0**; WATM
  tooling last active mid-2024. Low stars/forks.
- **Production adoption:** **None confirmed.** No evidence WATER is embedded in
  Tor, Psiphon, Lantern, Outline/Jigsaw, or any VPN. The paper's own Future Work
  still lists real-world deployment as aspirational. **Treat as a research
  prototype / early SDK.**
- **WASI limits:** WASI Preview 1 only (no Preview 2 / Component Model);
  `wasm32-wasip1` implies a 32-bit target (adequate for AEAD framing, a
  constraint for authoring).

## Arms-race context

WATER is a direct response to the accelerating censor/circumventor cycle: SSL
fingerprinting → obfsproxy → active probing → probe-resistant proxies → entropy
detection of fully-encrypted traffic → prefix fixes. The GFW's **Nov 2021
fully-encrypted-traffic blocking** (Wu et al., USENIX Sec '23) is the canonical
recent example. WATER's pitch is *cycle-time*: when a technique is blocked, push a
new signed `.wasm` instead of shipping an app update. The paper demonstrates this
by porting the exact upstream `shadowsocks-rust` GFW-evasion patch into a WATM
**unchanged**. Whether hot-swappability yields a *measured* operational edge over
statically-deployed obfs4/Snowflake remains unproven (see open questions).

## Caveats

All 25 surviving claims were verified against primary sources (FOCI paper via
arXiv/PETS/ar5iv + official repos), so the technical description, portability
thesis, and benchmarks are high-confidence. Limits of the evidence:

1. Benchmarks are the **authors' own single setup** (one M1 Max, one MI→SF path),
   not independently reproduced; the 45–55% general-WASM figure is a 2019 study on
   since-improved engines.
2. **Adoption/arms-race angles are weakly supported** — evidence confirms
   ownership and runtime existence, not production deployment, downstream
   integrators, or measurement linkage.
3. Portability / generic-reuse / real-time-delivery are stated **design goals**,
   not benchmarked evidence of cross-tool reuse in the wild.
4. "No anonymity / no relays" is an inference from scope, not an authors' claim.
5. **Security:** WASM sandboxes *execution*, not *intent* — a malicious WATM can
   still open arbitrary sockets and exfiltrate. The paper prescribes **code-signing
   + verification** of WATMs (as Tor signs its PTs); runtime-enforced signature
   verification does **not** appear to exist — it is the integrator's job.

## Open questions

- What is WATER's actual production adoption — any real tool/VPN/Outline, or still
  a prototype?
- How do WASI P1 vs P2 limits constrain WATMs (sockets, threading, async I/O), and
  has newer WASM SIMD/crypto narrowed the ~23× crypto gap?
- Does hot-swappability give a *measurable* arms-race advantage over static
  obfs4/Snowflake/Shadowsocks against the GFW?
- Is WATER a replacement, a delivery layer, or complementary to existing
  Refraction/Tor deployments (Conjure, obfs4)?

## Applied companion

For a homelab deployment design (WATER as an egress-obfuscation layer + Spin as a
WATM distribution control plane, placed against UDM Pro VLANs / Talos-Cilium),
see [examples/water-spin-homelab](../examples/water-spin-homelab/README.md).

## Sources

Primary:

- FOCI 2024 — *Just add WATER: WebAssembly-based Circumvention Transports*:
  [PETS PDF](https://www.petsymposium.org/foci/2024/foci-2024-0003.pdf) ·
  [page](https://www.petsymposium.org/foci/2024/foci-2024-0003.php) ·
  [arXiv 2312.00163](https://arxiv.org/abs/2312.00163) ·
  [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2312.00163)
- Repos: [refraction-networking/water](https://github.com/refraction-networking/water) ·
  [water-rs](https://github.com/refraction-networking/water-rs) ·
  [watm](https://github.com/refraction-networking/watm) ·
  [pkg.go.dev/water](https://pkg.go.dev/github.com/refraction-networking/water)
- Docs: [water.refraction.network](https://water.refraction.network/) ·
  [architecture](https://water.refraction.network/architecture.html) ·
  [Go quick-start](https://water.refraction.network/runtime/go/quick-start.html) ·
  [WATM spec v0](https://water.refraction.network/transport-module/spec/v0.html) ·
  [WATM spec v1](https://water.refraction.network/transport-module/spec/v1.html)
- Author page: [jack.wampler.co/projects/water](https://jack.wampler.co/projects/water/)
- Tor: [PT overview](https://support.torproject.org/tor-browser/circumvention/unblocking-tor/) ·
  [Tor spec](https://spec.torproject.org/intro/index.html)
- Alternatives / measurement:
  [Proteus (FOCI 2023)](https://www.robgjansen.com/publications/proteus-foci2023.pdf) ·
  [Marionette (USENIX Sec 2015)](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-dyer.pdf) ·
  [GFW fully-encrypted-traffic blocking (USENIX Sec 2023)](https://gfw.report/publications/usenixsecurity23/en/) ·
  [Geneva / fully-encrypted](https://geneva.cs.umd.edu/posts/fully-encrypted-traffic/en/) ·
  [PTPerf (arXiv 2309.14856)](https://arxiv.org/abs/2309.14856) ·
  [WASM perf — Jangda et al. ATC'19 (arXiv 1901.09056)](https://arxiv.org/pdf/1901.09056)

XTLS / VLESS / REALITY:

- [Xray-examples — REALITY (ENG spec)](https://github.com/XTLS/Xray-examples/blob/main/VLESS-TCP-XTLS-Vision-REALITY/REALITY.ENG.md) ·
  [Project X docs — SNI fallback/camouflage](https://xtls.github.io/en/document/level-1/fallbacks-with-sni.html) ·
  [REALITY source-code analysis (ObjShadow)](https://objshadow.pages.dev/en/posts/how-reality-works/)

Secondary: [Lantern censorship corpus — pluggable transports](https://corpus.lantern.io/defenses/pluggable-transport/) ·
[fully-encrypted detection](https://corpus.lantern.io/techniques/fully-encrypted-detect/)
