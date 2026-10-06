---
title: Regenerative Software - EARLY RELEASE - Developing Scalable, Maintainable Systems
  with AI (Chad Fowler)
source: books/pdf/Regenerative Software - EARLY RELEASE - Developing Scalable, Maintainable
  Systems with AI (Chad Fowler) (z-library.sk, 1lib.sk, z-lib.sk).pdf
source_type: book
source_hash: 86718bdbb95aad92d2feca1caf6860a5c82daa676d2a833e522b05e6bb6cd431
tags:
- ai
- book
extracted: '2026-10-04'
---

# **Regenerative Software**

## Developing Scalable, Maintainable Systems with AI

## **Chad Fowler**

**Regenerative Software**

by Chad Fowler

Copyright © 2027 Chad Fowler. All rights reserved.

Published by O’Reilly Media, Inc., 141 Stony Circle, Suite 195, Santa
Rosa, CA 95401.

O’Reilly books may be purchased for educational, business, or sales
promotional use. Online editions are also available for most titles
[(https://oreilly.com). For more information, contact our](https://oreilly.com/)
corporate/institutional sales department: 800-998-9938 or
_corporate@oreilly.com_ .

Acquisitions Editor: Louise Corrigan

Development Editor: Rita Fernando

Production Editor: Katherine Tozer

Interior Designer: David Futato

Interior Illustrator: Kate Dullea

April 2027: First Edition

**Revision History for the Early Release**

2026-07-31: First Release

[See https://oreilly.com/catalog/errata.csp?isbn=9798295900433 for release](https://oreilly.com/catalog/errata.csp?isbn=9798295900433)
details.

The O’Reilly logo is a registered trademark of O’Reilly Media, Inc.
_Regenerative Software_, the cover image, and related trade dress are
trademarks of O’Reilly Media, Inc.

The views expressed in this work are those of the author and do not
represent the publisher’s views. While the publisher and the author have

used good faith efforts to ensure that the information and instructions
contained in this work are accurate, the publisher and the author disclaim all
responsibility for errors or omissions, including without limitation
responsibility for damages resulting from the use of or reliance on this
work. Use of the information and instructions contained in this work is at
your own risk. If any code samples or other technology this work contains
or describes is subject to open source licenses or the intellectual property
rights of others, it is your responsibility to ensure that your use thereof
complies with such licenses and/or rights.

979-8-295-90039-6

# **Brief Table of Contents ( Not Yet** **Final )**

Part I: Foundation

Chapter 1: The End of Code as the Asset (available)

Chapter 2: Replaceability as the Defining Property (available)

Chapter 3: The Seven Primitives: How the System Survives the
Implementation (available)

Part II: Implementation

Chapter 4: The Regeneration Pipeline (available)

_Chapter 5: Designing Evaluations_ (unavailable)

_Chapter 6: Provenance as the New Version Control_ (unavailable)

Part III: Architecture

_Chapter 7: Pace Layers and Stability Boundaries_ (unavailable)

_Chapter 8: Deletion Safety and Hidden Dependencies_ (unavailable)

_Chapter 9: Compaction and System Integrity_ (unavailable)

Part IV: Context and Constraint

_Chapter 10: What Regenerative Software Is Not_ (unavailable)

_Chapter 11: Failure Modes and Constraints_ (unavailable)

_Chapter 12: Operating a Regenerative Software System_ (unavailable)

Part V: Implications

_Chapter 13: The Economic Inversion_ (unavailable)

_Chapter 14: Architecture for Software That Can Burn and Return_
(unavailable)

# **Chapter 1. The End of Code as** **the Asset**

The software industry has historically protected code as its most precious
asset—the “crown jewels” of an organization. This behavior was not
irrational; it was the logical response to code functioning as a system’s only
reliable memory. A product manager can explain the visible requirements,
and an architect can describe the intended shape, but only the code knows
the exceptions. The code knows what happens when an exchange pauses
trading, which third-party API returns malformed data on the first business
day of the month, and how to handle illiquid instruments. This knowledge
often exists nowhere else.

This creates the strange paradox of “legacy” software. In most fields, a
legacy is a durable value—a living body of work worth studying. In
software, we use the term as an insult. We fear touching legacy systems not
because they are old, but because of _how_ they have aged. A system that
survives ten years encodes real business truth, absorbing production
incidents, regulatory changes, and performance hacks. The problem is that
we have failed to extract this knowledge from the implementation, making

the specific lines of code precious simply because they are the only record
of that accumulated truth.

This failure to separate knowledge from implementation is why big rewrites
are so dangerous. We treat them as implementation projects, but they are
actually archaeology projects. A rewrite team usually reproduces the
“happy path” and the visible features but loses the “scar tissue”—the
accumulated production behavior that is the only reason the system actually
works. A rewrite fails when it loses the truth buried in conditionals and
workarounds.

To move forward, we must stop treating code as a precious artifact and start
building software capable of growing old well, where the system’s essential
behavior and identity can survive independent of any specific
implementation. In this chapter, I’ll dismantle the assumption that code is
the asset. First, you’ll examine the historical economies that forced us to
protect our code. Next, we’ll explore the inversion: how generative AI
collapses implementation costs and shifts engineering value toward
defining system truth. Then, we’ll redefine how a system maintains its
identity and introduce the assets that must survive code changes. Finally,
we’ll end on the ultimate measure of an architecture’s readiness for this new
era.

## **Code Was Expensive, So We Protected It**

Treating code as precious always made sense. For most of software history,
it was the only sensible response to the economics of the field.

Producing working software was brutally expensive. Experienced
developers on complex systems might produce only a small amount of
finished, tested, production-quality code each day. Not because they were
lazy, but because it is hard to make code correct. You write a few lines, then
spend hours figuring out why it breaks under load, why it fails at boundary
conditions, or why it explodes when a downstream service gets cranky.

Organizations planned projects in developer-months because writing
working software was the bottleneck. When something costs that much to
create, you protect it.

So we built an entire professional culture around preserving source code.
Version control systems protected it from accidental loss. Code review
protected it from careless change. Style guides made it uniform. Every tool
—from the IDE to the release pipeline—assumed source files were the
atomic unit of truth.

That made sense when source code was the expensive artifact. A hard drive
crash without backups could erase months of work. A rewrite could
consume years and still fail.

This is why we developed the instinct to protect our code with our lives. It
was a rational response to an era where implementation was our scarcest
resource. But the economics are shifting. As we move away from this era of
expensive authorship, we have to recognize that the asset was never the
code itself; it was the system knowledge we trapped inside. The “inversion”
is coming, and our relationship with the implementation is about to be
fundamentally upended.

## **Historical Lessons in Disposability**

The industry has long flirted with the idea of disposable parts, though we
didn’t always call it that. Efforts like the microservices movement and the
push for “tiny” components were tactical attempts to solve the crushing
weight of coupling. We sought independently deployable units to escape the
monolith’s gravity, but often merely moved the coupling onto the network.
The true breakthrough in disposability came not from application
architecture, but from immutable infrastructure.

With the rise of cloud and containers, we transformed servers from “pets” to
“cattle.” A machine was no longer a precious asset to be nursed; it was an
artifact to be destroyed and recreated from a known recipe. This shift was
freeing, moving the durable value from the running instance to the structure

and process that defined it. However, we stopped short. While we
successfully learned to stop loving the server, we failed to apply that same
mindset to the implementation itself. We still protect source code as if it
were the crown jewels, failing to realize that the fundamental shift required
for Regenerative Software is treating the implementation as a temporary
expression of system truth—just as disposable as the servers that host it.

## **The Inversion: Implementation Got Cheap**

The old rule was simple: maintaining existing code is almost always
cheaper than replacing it.

So we tolerated extraordinary maintenance burdens: accumulated patches,
undocumented workarounds, implicit dependencies, fragile deployment
processes, modules everyone feared but nobody could justify rewriting. The
fear was rational under the old economics. Replacement was expensive.
Humans had to rediscover the behavior, rewrite the implementation, rebuild
confidence, and endure the long tail of regressions. Even when the old code
was ugly, it was usually safer to keep patching it. For fifty years,
implementation consumed most of the budget, and everything evolved
around that fact — review, refactoring, style guides, defensive architecture,
change-control processes. All of it assumed that changing code was the
expensive part.

Generative AI attacks that cost directly.

A component that once took a team months to rewrite may now be
generated, reviewed, corrected, and tested in days. We already knew
replaceability mattered. We knew it from legacy systems, from failed
rewrites, and from every painful migration where the old code turned out to
know more than the people replacing it. What has changed is the cost of
producing a plausible implementation.

Plausible is the load-bearing word. Cheap implementation doesn’t make
replacement safe; it makes unsafe replacement easier to attempt. Cheap
implementation without strong boundaries is just faster chaos. The problem

we already had, amplified under the illusion of progress. Without a way to
evaluate the implementation, generation is a more efficient way to produce
plausible wrong answers. Confidence theater. AI is really good at
hallucinating something that looks so right it’s hard to tell the difference.

The value does not move from humans to machines. It moves from typing
implementations to defining and defending system truth.

In the old world of expensive implementation, teams asked: how do we
preserve this implementation? When code becomes cheap, teams have to
ask: how do we know whether this implementation is correct? That’s a
different question, and arguably one that would have served us better all
along. It cannot be answered by looking only at the generated source. The
code may be readable. It may follow the right patterns. It may pass
superficial tests. It may look exactly like the code a competent human
would have written. That’s not enough. The question is whether it preserves
the behavior that matters. Does it respect the boundary? Does it satisfy the
contract? What about the ugly edge cases? What happens under real load,
when the downstream service times out, duplicates messages, changes
schema, or returns a value nobody expected?

In other words: can you evaluate it?

This is why “AI writes code now” is the least interesting interpretation of
this point in software history. The interesting interpretation is that code is
becoming abundant, and when something scarce becomes abundant, value
flows to whatever remains scarce. Code production gets cheaper, so value
moves to the things generation cannot produce: system understanding,
judgment, good boundaries, executable knowledge of correct behavior,
operational evidence, and the ability to say “this replacement is safe.”

That is the inversion. Not everywhere, not automatically, and not for
systems whose knowledge is trapped entirely in the implementation. But for
components with clear boundaries, captured behavior, meaningful
evaluations, and operational evidence, replacement becomes a real option,
and the implementation becomes less precious as the system around it
becomes more explicit.

Code doesn’t become worthless. That’s too simple. Running code still
matters; production still matters; a system isn’t a pile of specifications, and
at some point something has to execute. But a specific implementation
stops being sacred. It becomes one expression of the system rather than the
system itself. This is the shift from code as asset to code as commodity
input. A commodity input can still be important — steel is important to a
bridge, lumber to a house, electricity to a data center — but the durable
value lives in the structure, design, and constraints around those inputs.

The source code matters because it realizes the system today. The asset is
what lets us realize the system again tomorrow. The rest of this book (and
the second half of this chapter) is about what that asset actually consists of.

## **System Identity**

If implementations can change constantly, what makes the system the
system? Something has to persist across the replacements, or “the same
system” is an empty phrase. And whatever persists, it isn’t the source files,
the framework, the language, or the deployment topology. The system
persists through recognizable behavior, stable boundaries, and preserved
promises.

System identity isn’t mystical. It’s the combination of things other systems,
users, and operators depend on: what inputs the system accepts and what
outputs it produces, what invariants it preserves and what failures it
tolerates, what performance it promises and what data it owns, what
contracts it exposes and what operational behavior people have come to rely
on. A system retains its identity when these things persist, even if every line
of implementation changes.

The Ship of Theseus for software: identity lives in the structure, not the
planks.

We already accept this in many places. A database can radically change its
storage engine and still be the same database to its users, as long as the wire
protocol, query semantics, transactional guarantees, and operational

behavior remain intact. A web service can move from one framework to
another and stay the same service as long as the API contract and behavior
remain stable. The machines underneath a deployment platform can be
replaced without changing the system you experience, and a compiler can
rewrite its internals for decades while preserving the language contract
developers depend on. In each case, implementation continuity matters less
than behavioral continuity.

This isn’t permission to be careless. Some implementation details carry
weight the system has come to depend on. Performance characteristics,
failure modes, timing behavior, and operational quirks can all become part
of the contract once other systems have learned to depend on them.

That’s why evidence matters. You don’t get to decide system identity only
from the architecture diagram. Production gets a vote. The system is what it
_does_, including the parts you forgot to specify.

## **The Durable Assets**

Behavior, boundaries, promises: identity has ingredients, and they can be
named. The durable assets are the things we wished we had during every
painful rewrite — not prettier code, not more comments explaining local
implementation details, not another wiki page that goes stale before the next
release. The durable assets are the pieces of system knowledge that survive
a change in implementation, and they are what the rest of this chapter takes
apart one at a time.

### **Behavior**

Behavior is what the system actually promises.

Not just the happy path, not just the user stories, not just the public API
examples. Behavior includes the nasty stuff we can’t or don’t want to think
about when we’re creating something from scratch: edge cases, failure
modes, timing expectations, ordering rules, operational constraints, and all
the strange little facts learned in production.

A payment system’s behavior includes what happens when authorization
succeeds but capture fails. A messaging system’s includes what happens
when a message arrives twice, late, or out of order. A trading system’s
includes what happens during market halts, partial data outages, and
inconsistent exchange responses. A billing system’s includes what happens
to customers migrated through three pricing models over ten years. If that
behavior isn’t captured outside the implementation, then the
implementation remains precious.

### **Boundaries**

Boundaries define what can change independently.

A boundary isn’t a line on a diagram, a repository, a process boundary, or a
REST endpoint. A boundary is a _promise_ : this side may change without
requiring that side to change, this implementation may be replaced as long
as it satisfies the contract, and this component owns its data, its behavior,
and its failure modes. Everything else is topology.

Good boundaries make replacement local. Bad boundaries turn local change
into global negotiation and constant anxiety.

### **Evaluations**

Evaluations are executable promises.

They are how a system asks, in a form that can actually be run:

_If we replace this part, do the promises that matter still hold?_

Tests are one kind of evaluation, but they are not the whole idea. A test
usually asks whether a known piece of code behaves the way we expected
in a known situation. That is useful, but it is still tied to the shape of the
current implementation.

Evaluations have a different job. They describe the obligations a
replacement must satisfy.

A unit test might check that a function returns the right value. A contract
test might check that a component still speaks the expected protocol. A
property test might explore a wider space of valid inputs. A performance
evaluation might ask whether the replacement remains fast enough under
load. A production canary might ask whether real traffic reveals differences
that the pre-production checks missed.

Those all matter, but the category is not the point.

The point is that evaluations move correctness out of the code being
replaced and into the boundary around it. They make the system’s
expectations explicit enough that another implementation can be judged
against them.

Without evaluations, replacement is mostly trust. A human looks at the new
thing and decides it seems right. Maybe it passes the old test suite. Maybe
the author is careful. Maybe the diff looks reasonable.

That is not enough for regenerative software.

If a system is going to replace its own parts, the definition of “still works”
has to live somewhere other than the part being replaced. Evaluations are
that somewhere. They are the executable memory of what the system
promised to users, callers, operators, and neighboring components.

With evaluations, replacement becomes an operation.

Not a rewrite. Not a migration. Not a heroic act of judgment.

An operation: propose a replacement, run the evaluations, compare the
evidence, decide whether the promise still holds.

### **Evidence**

Evidence is what the system tells us about itself: logs, metrics, traces, error
rates, latency distributions, user behavior, incident reports, production data,
failed requests, retry storms, dead letters, support tickets, operational
dashboards, and the weird chart that only one engineer knows how to read.

Evidence matters because specifications are always incomplete, tests are
always partial, and human understanding is always behind production
reality. A system that can’t observe itself can’t safely replace itself. We
know about this already, because good systems engineers employ
observability tools and service level objects and KPIs. But now they serve
as _input_ into the development process--not just a way to monitor and
manually repair systems in production.

If evaluations define what we _expect_, evidence tells us what is actually
happening. The two need each other.

### **Provenance**

Provenance tells us where an artifact came from, why it exists, and what
supports trusting it. This becomes more important as generated code
becomes ordinary.

Who or what generated this implementation? What prompt, specification,
model, template, or prior version influenced it? What evaluations did it
pass? What production evidence supports it? What human decisions shaped
it? What changed since the last version?

Without provenance, generated systems become amnesiac. They can
produce artifacts, but they can’t explain their lineage. They can’t tell you
why a choice was made, what evidence justified it, or whether the same
assumption still holds.

Provenance isn’t bureaucracy. It’s memory. And memory is what keeps
replaceable systems from becoming disposable in the bad sense.

## **The Craft Moves**

None of this means engineering craft stops mattering. It means the craft
moves.

When implementation was scarce, much of the craft centered on producing
code: choosing abstractions, naming things well, controlling dependencies,

writing maintainable functions, structuring modules, and making the current
implementation understandable. That work still matters. Clean code is
easier to read, debug, operate, and replace while it exists. But it’s no longer
enough.

In an abundant-code world, the deeper craft is the ability to define the
system outside any particular implementation. Can you write a boundary
clear enough for another team, another language, or another model to
implement? Can you distinguish essential behavior from historical
accident? The day-to-day skills follow from there: capturing behavior
without overfitting to the current code, designing evaluations that detect
meaningful regressions instead of accidental details, and using production
evidence to discover what the system really does. And finally, can you
replace a component without making the whole organization hold its
breath?

These are engineering skills, and they’re not softer than programming. They
aren’t management. They aren’t documentation chores. They’re the
technical work required when code can be produced more cheaply than
system understanding.

The craft moves from authorship to judgment.

Authorship still exists. Someone still needs to understand code. Someone
still needs to review generated implementations. Someone still needs to
debug the ugly failure at 2:00 a.m. when all the evaluations passed and
production still found a new way to be production. But the highest-leverage
work shifts. The engineer who can hand-write a component in three weeks
is valuable. The engineer who can define the boundary, capture the
behavior, build the evaluations, use production evidence, and safely replace
that component in two days is more valuable, because preserving system
truth is harder than producing code.

And when the craft moves, the daily practices built around the old craft
move with it. Once you stop treating code as the asset, the familiar rituals of
engineering work start pointing at different targets:

_You review different things._ A code review still matters, but it’s not
enough to ask whether the implementation is locally clean. You
also ask whether the boundary is explicit, whether the behavior is
captured, whether the evaluations are meaningful, and whether the
new code has trapped system knowledge that should live
somewhere else.

_You document different things._ Instead of documenting every
implementation detail, you document contracts, invariants, failure
modes, operational expectations, and design rationale. The things a
future replacement will need to preserve.

_You test different things._ You still test functions, but you care more
about externally visible behavior: contract tests, property tests,
regression suites built from production incidents, and evaluations
that can run against multiple implementations.

_You version different things._ Source code remains versioned, but so
do prompts, specifications, schemas, contracts, evaluation suites,
model outputs, deployment recipes, and evidence trails. If an
artifact influences the system, it belongs in the lineage.

_You value different abstractions._ An internal abstraction that makes
the current code elegant is useful. An external boundary that makes
future replacement safe is strategic.

_And you become willing to delete._ This is perhaps the hardest
change, because it is the most personal. Developers take deletion
personally. We remember the work, the cleverness, the late nights,
the bug that took three days to find, the effort that went into getting
it right. But the system doesn’t owe the implementation
immortality. If the behavior is captured, the boundary is real, the
evaluations are strong, and the evidence supports the replacement,
deleting code isn’t vandalism. It’s maintenance.

This isn’t reckless rewriting. Quite the opposite. Most rewrites fail because
they’re reckless about system knowledge. They replace implementation

without preserving behavior. They draw new boxes without creating real
boundaries. They trust subjective human confidence instead of evidence.
Safe replacement is disciplined. It requires more rigor, not less.

That covers the human half of the shift: what engineers know, what they
practice, and what they let go of. The other half isn’t human at all. If the
people and processes reorient around replacement, the systems themselves
have to be shaped for it. That is an architectural demand, and it’s where the
consequences get structural.

## **The Architectural Consequence**

If components will be replaced — not _might_ be, but _will_ be — then
architecture has to change.

Interfaces between components have to become precise, explicit, and stable.
Fuzzy boundaries are the primary obstacle to safe replacement. Implicit
dependencies, shared mutable state, undocumented assumptions, hidden
ordering requirements, and database coupling all make replacement
dangerous. When one side of a boundary can be regenerated while the other
side continues running in production, every ambiguity becomes a potential
incident.

This doesn’t mean every system needs hundreds of tiny services, or that
every function needs a formal specification, or that architecture becomes a
bureaucratic exercise in drawing boxes and writing documents nobody
reads. It means we have to take replaceability seriously as a design
constraint. Can this component be replaced? And if so, what would a
replacement need to know, how would we tell whether it behaved correctly,
what evidence would we trust, what assumptions would break neighboring
components, and what knowledge is currently trapped in the
implementation? These questions reveal the real architecture of a system:
the architecture we have, not the architecture we intended.

You can’t always retrofit clean boundaries onto existing systems. Legacy
systems often evolved with implicit coupling that resists separation. Some

components are tangled so deeply into data models, workflows, and
operational practices that replacing them requires fundamental
restructuring. That’s the sometimes unfortunate reality.

The point isn’t that every old system can suddenly become replaceable
because generative AI exists. Many can’t, at least not cheaply. What
changes is that the gap between well-architected and poorly architected
systems will widen. Systems with explicit boundaries and strong
evaluations will compound the benefits of cheap implementation. Systems
without them will compound the confusion.

The same generative tools that make a well-bounded component easier to
replace will make a poorly bounded system easier to damage. You’ll be able
to produce more code, faster, with less understanding. You’ll be able to
create plausible implementations that pass shallow tests and fail under the
weight of real production behavior. That’s accelerated entropy, not progress.

Architecture is what prevents abundance from becoming noise.

## **Conclusion: The Deletion Test**

Pick an important module in your system. If you deleted the
implementation tomorrow, could you rebuild the system correctly?

Could you reproduce the edge cases, the failure behavior, the timing
assumptions, the integration contracts, the operational constraints, the weird
exception added after the outage everyone remembers but nobody
documented? Could you tell which parts of the current implementation are
essential and which are accidental, evaluate a replacement without relying
on the old code as the oracle, and prove, with evidence, that the new
implementation keeps the promises the system is supposed to keep?

For most systems, the honest answer is no, and this chapter has explained
why that was, for a long time, forgivable. Writing working code was
brutally expensive, so we protected it, and the protection worked well
enough that the knowledge trapped inside never had to live anywhere else.
The code was the memory because nothing else could afford to be. We even

rehearsed the alternative once, with infrastructure, when servers stopped
being pets. Then we stopped short of applying the lesson to the
implementation itself.

Generative AI ends the excuse. When implementation becomes cheap,
trapping system knowledge inside source code stops being a necessity and
becomes a choice. And increasingly, it’s the wrong one. The value moves to
what generation cannot produce: the identity of the system, its behavior,
boundaries, evaluations, evidence, and provenance, held somewhere
durable, outside any particular expression in code.

That’s the end of code as the asset. Code itself goes on, as does craft, as
does engineering judgment. What ends is the assumption that preserving a
particular body of source code is the same thing as preserving the system.
The system is the asset. Code is one expression of it. And from here on, we
design for the day that expression gives way to the next one.

Which raises the practical question this chapter has only gestured at: if the
defining property of a healthy system is that its parts can be replaced safely,
what does “safely” actually mean? It is not the same as modularity, and it is
not what microservices promised. The next chapter takes replaceability
seriously as a property in its own right: what it requires, what it rules out,
and how to test whether a system has it.

# **Chapter 2. Replaceability as the** **Defining Property**

We set out to replace what looked like the simplest important thing in
Wunderlist.

I’ll call it _group memberships_ . That isn’t quite what it was, and the real
name doesn’t matter. What matters is that it was two things at once: central
to how the product worked, and small enough that replacing it felt like a
chore rather than a project. A few of us could read the whole thing in an
afternoon. We had read it. We gave the replacement an afternoon.

The trouble was never in group memberships. It was in how the rest of the
system found things. We had built our own unique-ID system, the kind of
decision that makes sense at 3 a.m. in year one and then follows you for the
life of the company. Every entity in Wunderlist drew its ID from it, and
every part of the system that needed to point at another part’s data resolved
those IDs through machinery that, by the time we went to touch group
memberships, almost nobody fully understood. It had accumulated
assumptions about uniqueness, ordering, and how references resolved

across services, and those assumptions were opaque even to the people who
owned them.

Group memberships sat on top of that machinery, and when we replaced it,
the machinery began to lie. Records stopped matching in ways we couldn’t
explain. Data appeared to vanish for real users, lists and shared items
simply gone, and we couldn’t reliably say why or get it back. That is a
particular kind of terror: watching people’s data disappear and not
understanding your own system well enough to promise it will stop.

The afternoon lasted until Sunday morning. One of those nights I left the
office so tired I wrecked my bike on the way home and limped for weeks.

The component was small. It was not replaceable. And the thing that made
it unreplaceable was not inside it. It was in a system we had stopped being
able to see.

None of this was unique to us; it’s the shape of a recurring mistake. The
microservices movement taught a generation of engineers that small
components yield loose coupling, and many teams discovered they had only
traded a monolith for a _distributed_ one: small pieces wired together by
dependencies nobody wrote down, behaving as a single unit with network
calls where function calls used to be. Whether the pieces are services,
modules, or a homegrown ID system, the lesson is the same. Small is not
the same as replaceable.

The previous chapter argued that the durable asset is the system, not the
code: the behavior, boundaries, evaluations, and provenance that survive
any particular implementation. This chapter names the architectural
property that makes that survival possible: _safe replaceability_ . Can you
remove a component and put a regenerated substitute in its place without
the system losing its identity, which here means nothing mystical, just the
contracts it keeps and the behavior its evaluations pin down? Everything in
the rest of the book exists to make the answer _yes_ . So this chapter does
three things: it shows why our best modern architectures still fail at
replaceability, defines what safe replaceability actually requires, and gives
you an operational test for whether any given component has it.

## **The Failure of Modern Architectures**

When architects say “keep things small,” they’re reaching for something
real: components that are easy to understand, change, and replace. Size
correlates loosely with those properties. The correlation breaks down
precisely at the boundaries where components interact.

Look again at what actually trapped us. Group memberships was small and
clean inside its own boundaries. The danger lived outside it, in the IDresolution machinery it silently depended on, whose assumptions had never
been written down and had drifted beyond anyone’s full understanding. On
a diagram the component’s boundaries looked crisp. In the running system
they were porous in exactly the places that mattered, and none of that
showed up in its line count.

Tight coupling persists across small components through several familiar
channels: shared databases where multiple services read from the same
tables, undocumented message contracts that become implicit APIs,
temporal dependencies where services assume response times or ordering
guarantees, and shared domain concepts that leak across boundaries without
explicit contracts. None of these show up in line counts. All of them show
up when you try to remove something.

### **The Microservices Lesson, Revisited**

The microservices era taught this expensively: the unit of decomposition
should be the unit of independent _action_, not the unit of minimum size.

You can get the independent deployments, the Kubernetes clusters, the
service mesh, and still lose the ability to change direction quickly, because
each service is handcrafted, understood only by its original author, and
wrapped in integration tests so brittle that replacing any single one takes
weeks of coordination. The monolith got decomposed; the fragility didn’t.
The problem was never monolith-versus-microservices; it was that no part
of the system was designed to be safely replaced.

### **The Immutable Infrastructure Precedent**

We have solved a version of this problem before, one layer down. A few
years into the cloud era, production ran on hand-configured servers, each
the product of months of SSH sessions, hotfixes, and undocumented
package upgrades. Every manual patch pushed a running machine further
from any described state, and it drifted in one direction only: no one ever
accidentally simplified a production server. The industry called these
“snowflake servers,” individually maintained machines that became unique
artifacts, impossible to reproduce.

The “pets versus cattle” reframing broke the pattern. Stop treating servers
as irreplaceable individuals you nurse back to health; treat them as
identical, disposable units produced from a single specification. If one goes
down, don’t repair it, replace it. Build a complete, tested artifact, deploy it
whole, and never modify it after deployment. If something needed to
change, you built a new image from an updated specification and swapped
the instance. You didn’t SSH in and apply a fix.

This eliminated drift by construction and moved the source of truth
upstream, from the running machine to the specification that produced it.
The lasting lesson: when you eliminate in-place mutation, you eliminate the
slow, invisible accumulation of unknown state. The cost is investing in
specifications precise enough to reproduce what you need and pipelines
reliable enough to do it on demand. The industry largely paid that cost for
infrastructure over the 2010s, and cloud-native shops rarely revisit the
decision.

Immutable infrastructure is precedent, not thesis. It made _machines_
replaceable by making them disposable expressions of a specification. I
made a version of this argument back in 2013, in an essay called “Trash
Your Servers and Burn Your Code,” when burning the servers was
becoming ordinary and burning the code was still mostly aspiration.
Regenerative software asks the same question of the layer above: what
would it take to make the _implementation itself_ as replaceable as a server
instance?

### **Replaceability as the Real Metric**

Once you shift to replaceability as the measure of architectural health, the
picture inverts. A 200-line module with tentacles into six other modules is
harder to replace than a 2,000-line module behind a clean interface with
strong evaluation coverage. The question stops being “how big is this?” and
becomes “what happens if I remove it?”

None of this means size is irrelevant. Smaller components are, all else being
equal, easier to understand and faster to regenerate. But all else is rarely
equal. Size is a fine heuristic for initial decomposition and a poor measure
of architectural health over time.

## **Defining Safe Replaceability**

A component is replaceable when you can delete it, regenerate a substitute
that honors the same contracts, and deploy it without coordinating changes
in other components. “Honors the same contracts” distinguishes between
interfaces you designed and dependencies that accreted. “Without
coordinating changes” means the blast radius stays inside territory your
evaluations already cover. Miss either clause and you have something that
looks replaceable on a diagram and isn’t.

The instinct to chase this through smallness is strong, and it’s wrong. A
team rebuilding a billing platform once decided to make each function
independently regenerable: every parser, every validator, every formatter
got its own boundary, its own evaluation suite, its own contract. Within
weeks they had 140 regenerable units. The diagrams looked clean. Then
someone changed the shape of an invoice. The new field touched a dozen
components, each with its own contract tests, and a failure in any single
boundary cascaded into hours of debugging interface mismatches. They had
achieved maximum replaceability of individual pieces and near-zero
replaceability of anything that mattered.

That reasoning confuses the cost of _generating_ a component with the cost
of _replacing_ one. When you shrink components below a natural seam, you

don’t eliminate complexity; you push it into the gaps, where every
boundary needs a contract, every contract needs an evaluation, and
coordination overhead grows with the number of boundaries rather than the
complexity inside them. The team eventually restructured around twelve
modules organized by business capability, and the observable complexity
dropped sharply, because now they could reason about twelve things and
their relationships instead of 140. Generation is local; replacement is
systemic.

### **The Boundary Is the Decision That Holds**

If size isn’t the property that matters, boundaries are. System boundaries
(API contracts, data ownership lines, integration seams) are the
architectural decisions that persist across rewrites, and they are what you’re
actually protecting.

A widely-cited illustration is Amazon’s service-interface mandate, dated in
secondhand accounts to around 2002 and best known from Steve Yegge’s
later public retelling: all teams expose functionality through service
interfaces, no shared memory, no direct database access. Two decades on,
that boundary discipline is generally reported to still govern the
architecture, through many rounds of implementation change. The
boundaries held.

PostgreSQL tells a similar story from the inside. Today’s codebase shares
little with the 1997 release: the query planner has been reworked repeatedly,
storage internals extended and optimized far beyond the original, and
replication capabilities added and redesigned over two decades. <sup>1</sup> Yet no one
treats it as a different system, because the SQL dialect and the ACID
guarantees held firm, and the wire protocol maintained a stable, versioned
contract model even as it evolved. Both systems earned those boundaries
the hard way, through human discipline and without a regenerator in sight.
What changes now is not the definition of replaceability but its price. Cheap
regeneration lowers the cost of actually exercising a clean boundary, which
is what makes boundaries worth more than they used to be, not less.

This points to a distinction worth internalizing. When you redraw a
boundary, splitting a service, merging two data stores, changing which
system owns a concept, you are making an expensive architectural change
with cascading consequences. When you replace the code _behind_ a stable
boundary, you are doing maintenance. The boundary is what holds the
system together; the implementation behind it is architecturally
interchangeable. Teams that conflate the two treat every code change as an
architectural event, which is how you end up in organizations where
replacing a dependency takes six months of committee review.

So the real question is never how you deploy. A monolith with clean
internal boundaries supports independent replacement of its parts. A
microservices architecture with implicit behavioral coupling between
services does not. The question is where clean contracts exist.

### **A Boundary Not Covered by Evaluations**

A boundary is only as real as your ability to verify it. A clean-looking API
means nothing if the contract that holds the system together lives in
undocumented timing, shared state, or format assumptions nobody wrote
down.

Consider a user-authentication module. From the outside it has a clean API:
validate credentials, issue tokens, check permissions. But internally it
shares session state through a database that other components also read and
write. The login service writes session records, the authorization
middleware reads them directly, the audit service watches the same table for
changes. Replace the module with a version that uses a different session
schema and two other components break silently. Compare that to a
stateless design where token validation is a pure function of a token and a
signing key: no shared state, no side channels, every call independently
evaluable. The boundary is real because you can write evaluations that fully
characterize it, and those evaluations will catch any regeneration that
changes the contract.

Shared mutable state is a dependency that API diagrams don’t show. This is
why evaluations, which we develop fully in Chapter 5, are a structural part
of the architecture: they define the contract that survives regeneration. If
your evaluations can’t cover a boundary, the boundary doesn’t hold, and the
component behind it isn’t safely replaceable no matter how small it is.

### **What Safe Replaceability Is Not**

Safe replaceability shares instincts with several familiar ideas and diverges
from each in ways that matter. _Microservices_ share the instinct toward
independent deployability, but replaceability is agnostic about service size.
A regenerative system might have large components or a monolithic
deployment; what matters is whether each component can be replaced while
the system keeps its identity. _Clean Architecture_ (Robert Martin’s
formulation) shares the emphasis on boundaries, but it is largely agnostic
about whether the code behind those boundaries is long-lived or disposable.
Replaceability makes an explicit commitment the others don’t: the code
behind a boundary is _expected_ to be replaced, and the boundary is what
endures. That commitment moves your design energy toward the interfaces
and evaluations that survive regeneration, and away from the internal
elegance of code that won’t.

## **The Operational Replacement Test**

Definitions are cheap. The question is how you tell, for a real component in
a real system, whether it actually has this property. The test is deliberately
concrete. In an architectural review, instead of asking “is this service small
enough?” ask: _could we delete this and regenerate it by Friday? If not,_
_what’s in the way?_

The obstacles that surface are specific and actionable. The obstacle might
be a shared database, which is a boundary problem. Or an undocumented
event contract, which is an evaluation gap. Or a web of implicit
dependencies nobody has mapped, coupling hiding behind clean service

boundaries. Each obstacle is a specific piece of architectural debt, and
unlike a line-count threshold, it tells you what to fix.

### **Run It, Don’t Reason About It**

The test works best when you treat it as something you actually do, not
something you argue about at a whiteboard. The attempt itself is the
instrument. You don’t have to follow through on every deletion, but you do
have to try, because the gap between “looks safe” and “is safe to delete” is
exactly where architectural debt hides.

The group-memberships disaster was one shape of this problem; here is
another. A team inherits a mid-sized order-processing system and decides to
modernize it one component at a time. They pick the smallest, simplestlooking service first: a notification formatter that turns order events into
customer-facing messages. When they remove it in staging and slot in a
regenerated replacement, three other services fail in ways nobody predicted.
The formatter had quietly become the de facto schema authority for a data
structure shared across the pipeline. Other services didn’t just consume its
output; they imported its internal types directly. The afternoon task became
a two-week archaeology project. That team would learn more about their
system’s hidden dependencies from one failed deletion than from six
months of routine operation.

Start with leaf nodes or recently-changed components. Leaf nodes have the
most contained blast radius, so the diagnostic is cheapest to run. Recentlychanged components are where coupling patterns are freshest. In both cases
you’re probing the architecture at its most accessible points first, building
confidence and vocabulary before you attempt anything the business
depends on.

The test has a political cost as well as a technical one, and it’s worth naming
out loud. Someone has to sign off on spending a staging run, and
occasionally a day of a sprint, on an experiment whose whole value is in
what it breaks. The case for your manager is straightforward: a deletion that
eats an afternoon now is buying down a six-week replacement you can’t

schedule later, and the obstacles it surfaces are the same ones that would
otherwise surface in an incident, at a worse hour and without a rollback
plan.

### **What One Deletion Exposes**

A single deletion attempt exposes four properties at once, properties that
would otherwise require separate audits to find.

First, it reveals _boundary clarity_ : every undeclared dependency the
interface definition doesn’t capture surfaces the moment something
unexpected breaks. When you remove a component and something you
didn’t predict breaks, you’ve found a boundary that exists in the running
system but not in your diagrams. It also measures _evaluation coverage_ .
Delete the component, and if no evaluation notices, either the component
was dead weight or your evaluations have gaps, and you need to know
which. _Coupling depth_ shows up as the number of components that change
behavior when one disappears, and how far away they sit; a service three
hops away producing bad data is coupling no static analysis would have
revealed. Last is _architectural coherence_ : the difference between the
dependency graph you think you have and the one you have.

These four properties tend to degrade together, and deletion is the only
single operation that tests them simultaneously. Resist the urge to turn them
into a dashboard of scores; the value is diagnostic, not quantitative. What
you want is the list of specific obstacles, because that list _is_ your
architectural to-do.

### **Blast Radius, and Why the Test Must Be Ongoing**

Underlying all four properties is a single quantity worth naming, the blast
radius: the set of components, behaviors, data flows, and user-visible
outcomes that degrade when a component is deleted without replacement. It
includes direct dependents, indirect dependents that consume side effects or
parse logs, and environmental dependents that rely on caches it warms or
schemas it maintains. Blast radius, not size, is the true cost of replacing

something. The goal isn’t zero blast radius (a component nothing depends
on does nothing worth keeping) but _known, bounded_ blast radius: small
enough to plan for, visible enough to detect, recoverable enough that
replacement doesn’t require a war room. For any component, ask two
questions: _what breaks if this disappears, and how would we know?_ If the
honest answer to both is “we’d find out in production,” that’s an
architectural gap.

And it is never settled. A feature-flag service that starts as a clean key-value
lookup can, over eighteen months and without a single interface change,
become unreplaceable: one team starts using its cache-warming as a
readiness signal, another tails its audit log as an event stream, a third
depends on the specific error codes it returns under load. Each was a
reasonable local decision. Together they transformed a deletion-safe
component into one that would fail across three unrelated domains if
replaced. The interface never changed. The deletion safety collapsed
anyway. This is why the test is a habit, not a one-time audit, and why the
components most worth re-testing are your most stable ones, the slowchanging layers we’ll return to as pace layers in Chapter 7. (The mechanics
of discovering hidden dependencies and staging a safe removal are the
subject of Chapter 8; here the test is a diagnostic for the property, not yet a
procedure.)

Something shifts when teams run this test regularly. “Can we delete this?”
becomes a routine question in reviews, and teams stop debating coupling in
the abstract and start asking what breaks, how far the damage spreads, and
what would make the replacement safe. The test stops being a way to grade
the architecture and becomes a way to design it.

### **When Replaceability Is the Wrong Goal**

Everything in this chapter assumes you can afford the one artifact the whole
property depends on: evaluations rich enough to characterize a boundary.
Most teams can’t, at least not everywhere. Comprehensive behavioral
evaluations are common in avionics and payment rails and almost nowhere
else, because they are expensive to write and expensive to keep honest. So

safe replaceability, as defined here, isn’t a property you can declare. It’s one
you buy, boundary by boundary, and the bill comes due before the benefit
does. A team with clean APIs and no evaluations doesn’t have replaceable
components; it has components that look replaceable, which is worse,
because the diagram lies with confidence.

That cost sets the scope. The deletion test earns its keep where change is
frequent and the blast radius of a mistake is high. On a slow-moving
internal tool, standing up evaluation coverage and re-running deletions
every quarter is effort spent defending against a change that isn’t coming.
Run the test where the system is going to move, and let the stable, lowstakes corners stay boring.

There is a subtler failure too, the mirror image of the over-decomposition
trap. A team that internalizes replaceability as the goal can spend a quarter
carving seams, writing contracts, and building evaluation suites while the
roadmap sits untouched. Replaceability is a means to cheap change, not an
end. If you are making things replaceable faster than you are shipping the
changes replaceability was supposed to enable, you have inverted the point.

Finally, not all coupling is debt. Some seams should be expensive to cross,
because they guard an invariant: a ledger that must stay consistent, a pricing
core whose parts only make sense together. The deletion test will flag these
as high blast radius, and it should. The real question it asks is whether that
cost is known and intended or discovered in production. A boundary you
chose to make rigid is architecture. A boundary that turned rigid while you
weren’t looking is debt. The test doesn’t tell you which. You do.

## **Conclusion: From Property to Primitives**

Replaceability is the property that separates architectures that can absorb
cheap regeneration from architectures that cheap regeneration will break
faster. Replaceability isn’t smallness, modularity, or the shape of your
deployment. It’s whether a component can be deleted and regenerated
within a known blast radius, verified against contracts that live outside it.

The operational replacement test is how you find out which of your
components have it and which have only been pretending.

A component is only replaceable if the knowledge that made it correct lives
somewhere other than the code you’re about to delete. What those durable
things are, and how to build a system that holds them by design, is the
subject of Chapter 3.

1 Native streaming replication didn’t arrive until 2010.

# **Chapter 3. The Seven** **Primitives: How the System** **Survives the Implementation**

In Chapter 1, I argued that code isn’t the asset. The system is. That sounds
fine until you try to delete something. Then the question gets
uncomfortable: if the system isn’t the code, where does the system live?

I’ve spent a lot of years watching system replacements fail, and the failures
have a pattern.

A team rewrites a payment service. The new implementation passes the
tests and deploys cleanly. Six months later, a compliance auditor asks why a
particular rounding rule exists. The code is right there. It still rounds
correctly. But the reason is gone. The regulatory requirement that created
the rule is gone. The rejected alternatives are gone. The payment processor
constraint that made the ugly version necessary is gone.

Another team replaces a rate limiter. The new version rejects the same
requests as the old one, but takes 200 milliseconds to do it. That sounds fine
until three upstream services start timing out. The old implementation had

rejected requests in under 50 milliseconds, not because anybody loved
premature optimization, but because a previous incident had taught the
system that slow rejection was worse than no rejection and caused
cascading failures across many services.

Years ago my company inherited a large Rails application from another
consulting firm. The client wanted a major version upgrade. The syntax
changes were annoying, but they weren’t the real problem. The real
problem was that years of architectural decisions had fused themselves to
framework behavior: callbacks, middleware ordering, transaction
semantics, background job timing, cache invalidation, plugin assumptions,
deployment scripts, and tests that accidentally defined production behavior.
The team thought it was upgrading Rails, but it was really trying to recover
the architecture from the code.

These aren’t code failures in the usual sense. They’re _memory_ failures. The
knowledge that made the system work was trapped in the implementation,
and replacement destroyed the container.

Regenerative software starts from a simple discipline: before you make
implementation disposable, move system knowledge somewhere durable.

This chapter is about the primitives that let a system survive the loss of its
current code. They aren’t documents in the old enterprise sense. They might
appear as markdown, schemas, tests, traces, dashboards, generated
specifications, architectural decision records, prompts, policies, or
executable checks. The medium matters less than the role: each primitive
must be durable, reviewable, and connected to the system’s behavior.

A primitive only counts when the system actually uses it. A stale wiki page,
a distrusted diagram, a test suite coupled to deleted internals, a changelog
with no rationale — each is the _shape_ of a primitive without the substance.
The primitive has to participate in the life of the system.

Together, these seven answer the question Chapter 1 leaves open: if the
implementation of a system is replaced, exactly _what_ lets the system
continue to be itself?

## **The Seven Primitives**

As I’ve said previously, when implementations are expensive and rare, it’s
tempting to let knowledge live inside the code. The code becomes the place
where intent, architecture, behavior, history, operational constraints, and
edge cases accumulate. That’s how most software has worked for decades.
But once implementations can be regenerated, that arrangement breaks
down. The current implementation can no longer be the only place the
system knows what it is.

The following seven primitives represent the types of system knowledge
that have to survive implementation replacement.

_Intent_ captures what the system must do and why.

_Compilation_ is the architecture that generated code compiles into:
boundaries, ownership, communication primitives, runtime
choices, framework constraints, and operational constraints,
specified mostly by humans so generated code doesn’t have to
figure them out.

_Evaluations_ define executable ways to determine whether behavior
survived replacement (or even initial generation).

_Provenance_ preserves the lineage of decisions, constraints,
incidents, rejected alternatives, and generated artifacts.

_Pace_ matches replacement velocity to architectural position.

_Deletion_ makes it safe to remove or replace components without
breaking hidden dependencies.

_Compaction_ keeps regeneration from accumulating complexity.

Each primitive exists because replacement destroys something unless that
thing has been preserved somewhere else. Intent preserves purpose;
compilation, architectural shape; evaluations, behavioral truth; provenance,
reasoning; pace, stability; deletion, safety; compaction, comprehensibility.
They form a loop.

Intent defines what must be preserved. Compilation gives the system an
architecture, mostly chosen by humans, that the next generated code
compiles into. Evaluations test whether the generated implementation
actually preserves it. Provenance records why the shape and
implementation were chosen. Pace determines how cautiously the change
should move. Deletion removes the old implementation when the new one
is safe. Compaction reduces the accumulated complexity left behind by
many such cycles.

Each primitive prevents a particular kind of decay. Without intent,
regeneration produces code with no anchor for what “correct” means, and
without compilation the new code defaults to whatever shape the old
implementation happened to imply. Evaluations are how you tell that
behavior survived. Provenance is how you explain why the system works
this way. Pace keeps foundational layers from changing as casually as
experiments, deletion stops old components from haunting the system, and
compaction prevents each generation from leaving sediment.

The goal is to move the essential knowledge out of the implementation so
the implementation can change.

## **Intent: What the System Is For**

Intent is the knowledge you wish the old implementation had explained
before you deleted it.

It includes business rules, constraints, regulatory requirements, timing
assumptions, security properties, operational expectations, and the reasons
behind them. Intent isn’t a description of how the current code happens to
work. It’s a description of what any future implementation must preserve.
The difference matters.

A requirement like this is implementation documentation:

OrderService.validatePayment() must check inventory before calling
PaymentGateway.authorize().

That may be useful today, but it’s tied to a specific structure. It assumes an
OrderService, a PaymentGateway, a call sequence, and probably a
particular programming model.

A requirement like this is intent:

_Payment authorization requires inventory confirmation. Customers must_
_not be charged for unavailable items. Partial fulfillment may authorize_
_only the available portion of the order._

That statement survives a rewrite, a language change, a move from a
monolith to services, a move from services back into a module. It describes
the promise, not the current mechanism.

Intent isn’t a user story either. A user story says what someone wants to _do_ .
Intent says what must remain _true_ for the implementation to be considered
valid, both initially and as it is continuously regenerated. That distinction
matters because most replacement failures don’t violate the obvious story.
They violate the hidden constraint.

Consider the rate-limiting service example I mentioned earlier.

The old implementation rejected requests in under 50 milliseconds. The
new implementation rejected the same requests, but took 200 milliseconds.
From a narrow functional perspective, the behavior matched. Both
implementations answered the same question: should this request be
allowed?

But the timing constraint was part of the system’s real intent. The rate
limiter didn’t merely need to reject excess traffic. It needed to reject excess
traffic _quickly_ enough to prevent upstream services from exhausting their
own request budgets and triggering cascade failures.

A proper intent statement would have said:

_Rate-limit decisions must be returned within 50 milliseconds at p99 so_
_upstream callers can fail fast and avoid service-mesh timeout cascades._
_This constraint comes from the March 2024 incident in which 200ms_
_rejection latency caused dependent services to fail closed._

That statement does several things at once: it names the behavior, gives the
constraint, explains why the constraint exists, and links the constraint to
evidence. And critically, it survives the implementation.

Good intent usually has three parts:

Scope: where the requirement applies

Invariant: what must remain true

Reason: why the invariant matters

Let’s look at the payment service example again. An intent statement with
proper scope would be:

_For all subscription proration calculations, the prorated charge must_
_never exceed the monthly subscription amount, including leap years,_
_daylight-saving transitions, partial-month billing cycles, currency_
_conversion, and plan changes._

The scope is proration. The invariant is that the prorated charge never
exceeds the monthly subscription amount. The reason might be regulatory,
contractual, or reputational. That reason should be recorded too.

The most valuable intent often appears as negative space. It defines what
the system must never do: double-charge a customer, expose private data
without authorization, let inventory go negative, accept an expired reset
token, emit an event before the transaction commits, or treat a failed fraud
check as an approval because the fraud service timed out. Negative
constraints are powerful because they rule out whole classes of
implementations while still leaving room for different technical strategies.

This is the right kind of rigidity. _A regenerative system should be flexible_
_about implementation and stubborn about intent._

## **Compilation: The Architecture Code** **Compiles into**

Intent is necessary, but it is not enough to fully specify a working,
repeatable system. We know what the user wants, but we still need some
control over how this intent is expressed technologically and architecturally.

“Users must be able to reset passwords securely” is intent. It tells us what
must remain true. It does not tell us where the boundary belongs, which
component owns reset tokens, how audit events are emitted, how long
tokens live, or what guarantees the mobile app can rely on.

Intent needs an architecture to compile to.

A regenerative system has its own architecture in the same way a CPU has
an instruction set: a defined target with boundaries, ownership rules,
communication primitives, runtime choices, framework constraints, and
operational expectations. Generated code compiles to that target. It does not
get to invent its own.

That is the primitive’s job. Compilation absorbs structural decisions so
generated code does not have to rediscover them every time it runs. A
generator that has to infer the architecture from the old implementation is
likely to reproduce the old system’s accidents. A generator that invents the
architecture fresh each time is likely to produce a different system each
time.

The compiled architecture defines things like:

Where the boundaries are

Which component owns which data

Which interfaces are stable

Which communication primitives are allowed

Which runtime and framework versions are acceptable

Which framework idioms are permitted or forbidden

Which side effects must be explicit

Which failure modes must be handled locally

Which operational constraints apply

Which implementation choices are intentionally left open

Specifying this architecture is mostly a human job. People look at the
intent, the business constraints, the operational realities of the team, and the
long-term cost of different shapes, then decide what the structural target
should be. That decision is high-leverage. It is where engineering judgment
shows up most directly.

The architecture is not frozen. Some changes force it to reform. Moving
from Rails 6 to Rails 8, from Django to another runtime, from a monolith to
services, or from services back into a modular monolith may change the
communication vocabulary enough that boundaries, calling conventions,
batching rules, ownership, and failure behavior need to be reconsidered. In
those cases, the architecture itself is recompiled, and that recompilation
should be deliberate, reviewable, and recorded.

Day to day, though, generation runs against an architecture that is mostly
stable. The architecture absorbs structural change so individual
implementations can change cheaply. The more work the architecture does
explicitly, the less each generated implementation has to rediscover.

The rest of this section works through what that means in practice. A
compiled architecture has to do more than make generation possible. It has
to make later replacement possible. That requires resisting the places where
frameworks quietly become architecture, making communication paths
explicit enough to survive regeneration, treating architectural change as a
deliberate recompilation, and keeping the architectural target separate from
the code produced against it.

### **Buildable Is Not Replaceable**

Most frameworks optimize for buildability. They help a developer get from
idea to working feature quickly. They provide conventions for routing,
persistence, validation, templates, background jobs, middleware,

configuration, and deployment. They reduce boilerplate. They make the
easy path productive.

That is good engineering. But buildable is not the same as replaceable.

A system can be easy to build and hard to regenerate. It can have beautiful
framework conventions and terrible system boundaries. It can reuse code
everywhere and, by doing so, make independent replacement impossible.
This is the trap a regenerative architecture has to avoid.

Frameworks have gravity. Rails pulls toward models, controllers, callbacks,
migrations, jobs, and concerns. Django pulls toward apps, models, views,
middleware, signals, and admin conventions. React frameworks pull toward
components, hooks, routes, server/client boundaries, and build-time
assumptions. Every productive framework does this in its own way.

That gravity is useful when it aligns with the system. It is dangerous when it
silently becomes the architecture.

A framework wants to help you build. A regenerative architecture wants to
help you replace. Those are different design pressures.

This does not mean abandoning frameworks. It means reversing the
dependency. The compiled architecture defines boundaries, ownership
rules, communication primitives, side-effect constraints, and evaluation
points. The framework is then used inside those constraints.

Use Active Record, but do not let database associations decide domain
ownership. Use Django signals internally, but do not let them become
invisible cross-boundary contracts. Use middleware for security and audit,
but only if that behavior is explicit enough to survive a runtime change. Use
a background job system, but never as the only place where workflow
correctness lives.

The framework can make implementation pleasant. It just cannot be
allowed to decide what the system is.

### **Communication Model**

The architecture also defines the communication vocabulary the system is
allowed to use.

Most accidental architecture happens through shortcuts. One component
reaches into another component’s table. A model callback sends an email. A
signal updates a search index. A shared library performs a network call. A
background job mutates state owned by another subsystem. A plugin adds
behavior nobody can see from the boundary.

Each shortcut may be reasonable in isolation. Together they destroy
replaceability.

A regenerative architecture needs a small, explicit vocabulary for
communication: commands, queries, events, streams, workflows, and
owned state. Components should not be free to communicate through
whatever mechanism the framework happens to make convenient. If a
component needs something from another component, that dependency
should appear in the compiled architecture. If a component emits behavior
another component relies on, that relationship should be visible, evaluable,
and traceable.

Side effects aren’t necessarily bad, but hidden side effects are.

A payment service has to charge cards. A notification service has to send
messages. An inventory service has to reserve stock. Useful software
changes the world. The question is whether the side effect is part of the
component’s explicit contract or an implementation accident.

If a regenerated component sends fewer emails, emits events in a different
order, writes audit records differently, or changes retry timing, evaluations
should catch it, provenance should explain it, and evidence should confirm
it in production. That cannot happen when side effects are hidden in
callbacks, observers, signals, middleware, or shared libraries whose
behavior is not represented in the architecture.

### **Recompilation as Optimization**

Compilation is not only for major rewrites or framework upgrades. It is also
how a system adapts when constraints change.

Once intent, evaluations, evidence, and provenance are separated from the
implementation, a subsystem can be recompiled against a new architectural
target: faster, cheaper, simpler, safer, or better matched to current needs.

A reporting service originally compiled for correctness may need to be
recompiled for cost when usage grows. A batch process may need to
become a streaming architecture when freshness matters more than
throughput. A service split out for independent deployability may need to
return to a modular monolith when the operational overhead stops paying
for itself. A Python component may need to be regenerated in Go or Rust
when latency or resource use becomes the limiting constraint.

In each case, the intent may remain stable while the architectural target
changes. The behavior may remain stable while the runtime changes. The
evaluations may remain stable while the implementation strategy changes.

That is the leverage. Architecture stops being a one-time decision that
slowly decays. It becomes something the system can deliberately reform
under changing constraints.

The change still has to be justified. A regenerative system should not churn
architecture because it can. It should recompile architecture because the old
target no longer fits the evidence. Cost, latency, reliability, team capacity,
external dependency risk, regulatory pressure, and platform changes can all
be reasons. The reason should be recorded as provenance so the next
regeneration knows why the architecture changed.

### **What the Architecture Can’t Do Alone**

The architecture defines the shape of a candidate. It cannot prove the
candidate is correct. An architecture can be elegant and still wrong. It can
use the right patterns and still violate intent. It can satisfy every structural
constraint and still fail in production. Architecture narrows the solution
space; evaluations, the next primitive, test what comes out of it.

The architecture also needs its own memory. If a billing requirement
compiles to event sourcing, we should know why. Was it auditability?
Reversibility? Regulatory retention? Customer-service replay? Historical
accident? Familiarity? Without provenance, the architecture becomes
another source of mystery: the shape is explicit, but the reasons behind it
are missing. An architecture without provenance is just a better-looking
legacy system waiting to happen.

So the architecture ends where verification begins. It can constrain a
candidate into the right shape, and provenance can explain why the shape
was chosen, but neither can say whether the thing that came out actually
behaves. For that, the system needs claims about behavior that are
executable, and that outlive any single implementation. That is the job of
evaluations.

## **Evaluations: Tests That Outlive the Code**

A test suite can make a team brave, or it can make a team delusional. The
difference is whether the tests describe the system’s _promises_ or the current
implementation’s _habits_ .

Traditional tests often grow around code. They know method names,
internal seams, private data structures, call order, and implementationspecific decomposition. That’s useful while the code lives. But when the
implementation dies, those tests die with it.

Evaluations are different. An evaluation is an executable claim about
system behavior that should remain meaningful across implementations.
Tests often verify an implementation. Evaluations define correctness
_outside_ the implementation.

Consider an order validation service. A team regenerates it three times in
two months. Each iteration has cleaner code, better performance, and a
passing test suite. The fourth regeneration goes live, and customers start
complaining about being charged for out-of-stock items.

The implementation looked correct. It handled the obvious edge cases. It
passed the unit tests. But there was a race condition between inventory
checking and concurrent order processing that the test suite never covered.
Behavior changed silently. Customers found the bug before the team did.

A useful evaluation would have said:

_Concurrent orders for the last available item must result in exactly one_
_successful order and appropriate failure responses for all others, verified_
_under realistic concurrency and retry conditions._

That evaluation doesn’t care whether the implementation uses locks,
transactions, optimistic concurrency, a queue, an event stream, or a singlethreaded actor. It cares about the promise.

This is the key distinction.

An implementation-specific test says:

_OrderValidator calls InventoryService.reserve before_
_PaymentGateway.authorize._

A behavioral evaluation says:

No customer may be charged for inventory that was unavailable at
authorization time.

The first test may be useful while the current implementation exists. The
second evaluation should survive every implementation.

Evaluations bind to system boundaries: API responses, state changes visible
to consumers, published events, persisted data that other components
depend on, audit records, latency expectations, and failure behavior.

A serious replacement system needs several kinds of evaluations:

_Contract evaluations_ verify that interfaces behave as promised.

_Property evaluations_ verify invariants across wide ranges of input.

_Regression evaluations_ preserve lessons from incidents and
production bugs.

_Performance evaluations_ verify latency, throughput, resource use,
and cost.

_Failure-mode evaluations_ verify behavior under timeouts, retries,
partial failures, restarts, and bad data.

_Security evaluations_ verify authorization, authentication, isolation,
and data exposure properties.

_Production canaries_ compare real behavior under controlled
exposure.

The categories matter less than the discipline. Correctness must be external
to the implementation.

This is harder than it sounds because test suites tend to accrete around the
shape of code. Developers write tests where the seams are. If the current
implementation exposes a convenient internal method, tests use it. If the
current framework makes one kind of test easy, teams overuse that kind of
test. If fixtures are easy and production data is hard, tests begin to describe
the fixture world instead of the real world. That’s how a test suite becomes
a museum of the old implementation.

Evaluations have to resist that pull. The best question is simple: Would this
assertion still be meaningful if we replaced the implementation tomorrow?

If no, it may still be a useful test. But it isn’t an evaluation.

Evaluations evolve more slowly than implementations but faster than intent.
Production experience reveals new edge cases. Incidents expose missing
constraints. Performance regressions reveal unstated expectations. Security
reviews add new invariants. Customer behavior teaches the system
something the designers didn’t know. Those discoveries should become
evaluations.

A regenerative system should become harder to break over time because
every replacement cycle teaches the evaluation suite what matters.

## **Provenance: Why It Works This Way**

Version control tells us _what_ changed. Provenance tells us _why_ the system
became this way. That difference matters more once implementations are
regenerated.

Consider a recommendation engine that filters out items with less than
seven days of availability. Six months later, someone asks why. The code
does it. The tests expect it. The generated implementation preserved it. But
nobody knows whether the threshold came from inventory analysis, user
research, performance constraints, a business rule, or a model hallucination
that accidentally got committed.

Then the team discovers that the threshold is hiding profitable slow-moving
items and costing revenue. Now what?

If the threshold was a deliberate product decision based on user behavior,
changing it might be dangerous. If it was a temporary workaround for an
inventory problem that no longer exists, preserving it is waste. If it came
from generated code with no human or evidentiary basis, it should probably
be treated with suspicion. Without provenance, you can’t tell the difference.

Provenance records the derivational history of a component: what intent
produced it, which architecture it compiled into, what evaluations validated
it, what evidence influenced it, and what decisions changed it.

For the recommendation example, useful provenance might include:

Original product requirement: increase engagement through
personalization

Architectural decision: recommendation filtering happens at the
API boundary to reduce client complexity

Threshold constraint: availability greater than seven days based on
inventory analysis

Evaluation evidence: A/B test showing engagement improvement

Rejected alternative: client-side filtering caused inconsistent
behavior across platforms

Human decision: product team approved after revenue impact
analysis

This isn’t the same as a commit history.

A commit history says:

_Changed recommendation filter threshold._

Provenance says:

_Changed recommendation filter threshold from 3 days to 7 days because_
_Q2 inventory analysis showed items below 7 days availability produced_
_high cancellation rates and lower trust scores. Rejected dynamic_
_thresholding because the model was unstable for low-volume categories._
_Approved by product and operations. Evaluation suite updated with_
_cancellation-rate regression checks._

That’s the memory future replacements need.

Generated systems make provenance _way more_ important. When a human
writes code, we can at least pretend the reasoning lives in the author’s head.
That was never a great plan, but it sometimes worked. When code is
generated, regenerated, transformed, compacted, and partially rewritten by
tools, the reasoning can’t live in anyone’s head. It has to live in the system’s
lineage.

Provenance operates at several levels. At the system level, it explains why
services are decomposed this way, which integration patterns were chosen,
which external dependencies were accepted, and which architectural
alternatives were rejected. At the component level, it explains why an
algorithm was chosen, what performance constraints apply, which business
rules are encoded, and which incidents shaped behavior. At the
configuration level, it explains why timeouts have these values, what retry
policies are active, which feature flags control behavior, and what
operational evidence supports them. At the generation level, it explains

what prompts, models, specifications, templates, prior versions, evaluations,
and human decisions produced a given artifact.

The meaningful unit of history shifts from the textual diff to the derivation.
Traditional version control shows that a file changed. Provenance shows
what caused the change to exist.

This becomes especially important when you regenerate a component
multiple times. Imagine a billing calculation regenerated three times in one
quarter. Traditional history shows three commits with large diffs.
Provenance shows:

First generation: compliance requirements v2.1, passed financial
accuracy evaluations, deployed to 10% of traffic

Second generation: added tax calculation for new jurisdictions,
passed expanded international evaluation suite

Third generation: production incident required sub-100ms
response, compilation updated with caching constraint, passed
performance and accuracy evaluations

That history is useful because it connects change to reason. Without
provenance, each generation erases context. With it, each generation adds
memory.

## **Pace: Not Everything Should Change at the** **Same Speed**

Regeneration creates a temptation: if replacement is possible, replace
aggressively. That’s a mistake.

A recommendation model and an authentication boundary don’t occupy the
same kind of architectural space. One can change weekly and merely affect
engagement. The other changes rarely because every user-facing path,
mobile client, partner integration, audit process, and security assumption
leans on it.

The question isn’t only _can we regenerate this?_ The question is _what is the_
_appropriate rate of change for this layer?_ Fast change at the wrong layer
isn’t agility. It’s instability.

I learned this the hard way, and the lesson is sharper than the authentication
example makes it sound, because the truly dangerous slow layers are the
ones that never announce themselves the way authentication does.

One Thanksgiving, a friend and I came into the office over the holiday to
get ahead of Black Friday, hunting for optimizations before the traffic
arrived. One looked free. We were running Redis, and there was a drop-in
replacement client with much better performance. Redis speaks a stable,
well-documented protocol, so swapping one client for another read as the
safest possible change: a pure speed win with no behavior attached. We
made the swap, and the monitoring system filled with exceptions.

The protocol was never the problem. The session store was. Our user
sessions lived in Redis, and the old client had serialized them in a particular
way, with some cleverness we never fully reconstructed, even afterward,
that the new client did not reproduce. Every existing session now
deserialized wrong. We rolled back and drove home in the dark, the holiday
ruined, having learned that “just swap the library” had never been a small
change at all.

Both clients were well-built. The difference was architectural position. A
Redis client looks like a leaf, a dependency at the edge of the system you
can upgrade on a whim, and for most systems it is. But ours had a slow
layer hiding beneath it: a session store that every logged-in user depended
on, coupled to an exact serialization format nobody had written down. The
blast radius of the change was not “the Redis client.” It was “every active
session,” which is to say the entire system. We had treated a slow-layer
change as a fast-layer one, and it is the layer, not the size of the diff, that
decides what happens next.

Authentication sits in a slow layer. Its interfaces are consumed by nearly
every user-facing component. It’s integrated with mobile apps, partner

systems, compliance expectations, audit trails, and security assumptions.
Even small behavioral changes can ripple widely.

Recommendations sit in a faster layer. They matter, but their blast radius is
usually more contained. A poor recommendation can hurt engagement or
conversion. It usually doesn’t prevent users from logging in or break
contractual integration with partners.

This isn’t an argument against changing slow layers. Slow layers need
change. They may need security upgrades, framework migrations,
regulatory updates, performance improvements, or complete redesigns. But
the process has to match the layer.

Pace is the discipline of matching replacement velocity to architectural
position. A fast layer can regenerate frequently with lightweight review,
automated evaluations, and narrow blast-radius controls. A slow layer needs
deeper provenance, stronger compatibility guarantees, broader evaluations,
staged rollout, extended observation, and more careful deletion.

Different layers need different friction. Too much friction in a fast layer
kills learning. Too little friction in a slow layer creates systemic risk.

Pace also affects compilation. A fast-layer component may compile toward
experimentation: pluggable models, flexible configuration, A/B testing
hooks, frequent deployment, rollback-friendly behavior. A slow-layer
component may compile toward stability: versioned contracts, backward
compatibility, conservative communication primitives, explicit migration
paths, and slower interface evolution.

The mistake is treating all components as if they occupy the same
architectural time. They don’t.

A healthy regenerative system has rhythm. Some things move quickly.
Some things move slowly. Some things should barely move at all unless the
evidence is overwhelming. The architecture should know the difference.

## **Deletion: Removing Without Breaking the** **World**

Replacement isn’t complete when the new implementation works.
Replacement is complete when the old implementation can safely
disappear. That’s often the harder part.

A team regenerates a notification service. The new implementation is
cleaner, handles edge cases better, and uses fewer resources. They deploy it,
retire the old one, and immediately discover that order confirmations have
stopped working.

The problem isn’t in the obvious API. The old notification service returned
delivery receipts through a deprecated webhook. Nobody documented it.
The new implementation uses event-based delivery receipts. That’s better
architecture. But the order system still relies on the old webhook to mark
transactions complete. Removing the old implementation broke a hidden
dependency.

Deletion exists because systems are full of hidden dependencies. Static
imports are only the obvious kind. Real dependencies appear in runtime
traffic, shared tables, event consumers, timing assumptions, log formats,
dashboards, support workflows, batch jobs, data exports, customer scripts,
partner integrations, and habits nobody thinks of as architecture.

A component can be depended on in several ways:

_Interface dependencies_

Another system expects specific response formats, error
codes, timing behavior, or deprecated endpoints.

_Behavioral dependencies_

Another system relies on side effects, ordering guarantees,
retries, or failure modes.

_Data dependencies_

Another system reads or writes data the component
implicitly owns.

_Operational dependencies_

Monitoring, logging, alerting, deployment, or support
processes assume the component behaves in a particular
way.

_Human dependencies_

Operators, support staff, customers, or partners have built
workflows around current behavior.

Deletion safety requires discovering these dependencies before the old
implementation disappears. That discovery can’t rely only on code search.
Code search won’t find a partner integration. It won’t find a dashboard
query. It won’t find a support macro. It won’t find a customer who depends
on an undocumented response field because someone copied an example
from a Slack thread four years ago.

Deletion requires runtime evidence. Trace traffic and consumers. Inspect
event subscriptions and database access. Read logs, dashboards, and the
support backlog. And ask the question the tooling can’t: which humans will
notice if this disappears?

The safe replacement pattern is usually:

1. Introduce compatibility

2. Migrate dependencies

3. Verify isolation

4. Remove old implementation

5. Observe

6. Compact

Compatibility preserves old interfaces while routing behavior to the new
implementation. Migration moves consumers to the new contract. Isolation
verifies that nothing still depends on the old behavior. Removal deletes the
old path. Observation watches for missed dependencies. Compaction cleans
up the sediment.

The timeline reflects dependency complexity, not implementation
complexity. A simple service with many hidden dependencies may take
months to retire. A complex service with clean boundaries may be replaced
in days.

This is why deletion is a primitive. The hard part of regenerative software
isn’t only building the new thing. It’s safely making the old thing _gone_ .

## **Compaction: Keeping the System from** **Growing Forever**

Most teams are better at adding the new thing than removing the old one.
That’s how systems become haunted. The old endpoint stays because one
partner still uses it. The old token format stays because the mobile app
might still need it. The old queue stays because no one is sure whether the
nightly job consumes it. The old webhook stays because removing it once
broke order confirmation, the old configuration flag stays because no one
knows what happens when it is false, and the old model stays because a
report might query it. Every one of these decisions is locally rational.
Together they create a system nobody can understand.

Compaction is the discipline that prevents regeneration from becoming
accumulation.

This matters because regeneration can make accumulation worse. If
generating a new implementation is cheap, teams may preserve old
behavior too casually. They add compatibility layers. They support old
APIs. They carry forward old configuration. They preserve old data shapes.
They keep deprecated flows alive because doing so is easier than migrating
the last consumer.

Each cycle leaves sediment. After six cycles, the code may be clean, but the
system is conceptually obese. An authentication service supports four token
formats, three login flows, two session models, and five compatibility
paths. Every piece has a reason. Nobody can explain the whole. That’s
archaeology with better tooling, not regeneration.

Compaction asks a different set of questions. What can be removed? What
can be merged? What can be simplified? Which compatibility layer has
served its purpose? Which deprecated interface still has consumers, and
why? Which old behavior is essential? Which old behavior is just fear?

The goal is comprehensibility, not minimalism for its own sake. A system
that can’t be understood can’t be safely regenerated.

Compaction operates at several levels:

_Interface compaction_ removes redundant APIs, deprecated
endpoints, unused fields, and overlapping contracts.

_Configuration compaction_ removes unused settings, obsolete flags,
and option hierarchies that no longer reflect real choices.

_Dependency compaction_ removes unused integrations, shared
libraries, dead consumers, and accidental coupling.

_Evaluation compaction_ removes redundant or implementationspecific tests while preserving behavioral verification.

_Conceptual compaction_ simplifies the mental model required to
understand the system.

That last one is the most important. Software complexity isn’t only
measured in lines of code, number of services, or size of dependency graph.
It’s measured in how much someone has to know to make a safe change.
Regeneration without compaction increases that burden. Regeneration with
compaction should reduce it.

This is the healthiest form of replacement: the new system isn’t only
equivalent, faster, or cheaper. It’s easier to understand. That should be one

of the promises of regenerative software. Not just that the system can
return, but that it can return _smaller_ .

## **How the Primitives Work Together**

The primitives are easiest to understand separately, but they only work as a
system.

Imagine a billing subsystem that needs to be regenerated for a new platform
version and lower operating cost.

The intent says:

_Billing must calculate charges accurately across plan changes,_
_prorations, discounts, taxes, refunds, and historical contract terms._
_Customers must never be charged more than the amount contractually_
_allowed. All charge decisions must be auditable._

Compilation supplies the architecture, mostly human-specified, that the
regenerated implementation has to compile into:

Owned billing ledger

Explicit charge calculation boundary

Event log for auditable decisions

No hidden ORM callbacks for financial side effects

Versioned tax calculation interface

Background jobs constrained to idempotent command processing

Framework version upgraded

Runtime cost target reduced

Performance target defined for invoice generation

Evaluations define correctness:

Property tests for proration

Contract tests for billing API

Regression tests from historical billing incidents

Performance evaluations for invoice generation

Audit reconstruction checks

Canary comparison between old and new implementations

Provenance records why the architecture looks this way:

Regulatory audit findings

Rejected alternatives

Historical double-charge incident

Tax jurisdiction requirements

Cost analysis that justified platform change

Human approval of financial invariants

Pace classifies billing as a slow layer:

Extended validation

Staged rollout

Compatibility period

Higher review burden

Longer observation window

Deletion maps old dependencies:

Reports reading old tables

Support tools using deprecated fields

Partner exports depending on legacy invoice formats

Dashboards querying historical charge records

Compaction removes sediment:

Retired discount formats

Obsolete feature flags

Deprecated invoice endpoints

Duplicate tax calculation paths

Old compatibility code after consumers migrate

No single primitive makes the replacement safe. Intent without evaluations
is aspiration, and evaluations without intent are a pile of checks with no
theory. Compilation without provenance becomes unexplained architecture.
Provenance without deletion becomes a museum, deletion without
compaction leaves ghosts, and compaction without pace can remove things
too aggressively. Pace without evidence becomes bureaucracy. The
primitives need each other because each one protects against a different
failure mode.

Together, they move system knowledge out of the implementation and into
the structure around it. That’s what lets the implementation change.

## **Conclusion: The Primitive Test**

If you deleted an implementation tomorrow, what would you need in order
to rebuild the system correctly?

You’d need intent to know what still has to be true, and compilation to
define the architectural shape the next implementation should take.
Evaluations would tell you whether behavior survived. Provenance would
explain why the system has this shape. And you’d need pace to govern how
carefully the change should move, deletion to find what still depends on the
old thing, and compaction to decide what shouldn’t be carried forward.

That’s the minimum structure a system needs before implementation can
become disposable. Without these primitives, regeneration is just rewriting
with better tools. With them, replacement becomes part of the system’s
design.

But structure is not motion. This chapter has answered a static question
(what knowledge has to exist outside the implementation) and left the
dynamic one open: how does that knowledge actually become running
software? Knowing that intent must survive doesn’t tell you how intent gets
validated, compiled against an architectural target, synthesized into an
implementation, evaluated, and deployed, over and over, as a repeatable
process rather than a heroic one-off.

That process is the subject of the next part of this book. Chapter 4
assembles the primitives into a regeneration pipeline: the machinery that
takes intent in one end and produces deployed, observable implementations
out the other. The primitives you’ve just met stop being a taxonomy and
become stations on a line. Intent processed and validated, architecture
generated against it, implementations synthesized within its constraints,
behavior evaluated and observed in production. Everything so far has
described what the system must remember. What follows describes how the
system runs.

The code can burn. The system knows how to return.

# **Chapter 4. The Regeneration** **Pipeline**

You already trust a machine to write most of your code, and you have for
decades. You write in a high-level language, and a compiler turns it into
machine instructions you will never read, never review, and never handedit. When a bug appears, you fix the source and recompile. Nobody
patches the binary. We have forgotten how radical this arrangement is,
because it works so well that it disappeared into the background: we let an
automated pipeline produce the artifact that actually runs, and we trust that
artifact. Not because we inspect it, but because we trust the process that
produced it and the checks that constrain it.

That arrangement is the ancestor of everything in this chapter. The
regeneration pipeline asks a question the field has answered before, in a
new key: what if the high-level language is a behavioral specification, and
the compiled artifact is the whole application, database and API and
validation and interface? And it answers the way compilers, build systems,
and immutable infrastructure all answered their versions of the question.
Not with a cleverer generator, but with a pipeline of small, checkable

stages, each one turning the next from an act of judgment into a mechanical
transformation.

Chapter 3 named the primitives a regenerative system cannot delete. This
chapter is about how they compose. On their own the primitives are a
checklist; assembled, they are a compiler for intent, and the interesting
properties, the ones that make regeneration safe rather than reckless, only
appear once the stages are wired together.

A note before we start: this is an architecture, not a product you can install
this afternoon. What follows is the shape the field is converging toward,
drawn from the parts of it that already work in production, and honest about
the parts that don’t yet.

## **Pipeline Architecture**

The pipeline has four movements: intent becomes a structured set of
requirements, requirements become an architecture and a plan, the plan
becomes verified code, and the code reaches production and stays honest
there. A record of provenance runs underneath all four, connecting every
output back to the input that caused it. A reader fresh from the seven
primitives should know one thing before we begin: two of them, deletion
and compaction, are not stages in this pipeline at all. That is deliberate, not
an oversight, and the end of the chapter explains why.

The shape is borrowed on purpose. A compiler is not one transformation
but a sequence of them, front end to back end, each with a narrow job and a
checkable output: lexing, parsing, type checking, an intermediate
representation, optimization, code generation. The power is in the seams.
Because each stage hands the next a validated artifact, no stage has to
reason about the whole problem, and a failure stops at a gate instead of
propagating into the output. The regeneration pipeline keeps that structure
and changes only what flows through it. By the time generation runs, the
scope is fixed, the boundaries are declared, and the success criteria already
exist. Generation stops being creative and becomes what it should be, the
most mechanical step in the process.

Two properties make the pipeline worth the trouble, and both come from
prior art rather than from anything novel.

The first is that every intermediate artifact is addressable and replayable.
This is the lesson of content-addressed build systems and version control:
when the same input reliably produces the same identity, you can see what
actually changed, cache what didn’t, and replay any step in isolation. A
pipeline whose intermediate state you can inspect is debuggable; one that
goes from prompt to application in a single opaque leap is not, no matter
how good the leap.

The second is selective invalidation, and it is the property that separates this
from “an AI rewrites the app.” Incremental build systems solved this
decades ago with a dependency graph: change one source file and the build
reconstructs only what depends on it, not the world. The regeneration
pipeline builds the same graph out of semantic dependencies rather than file
imports. Change one line of intent and only the subtree that line justifies
goes stale. A wording fix that changes no meaning invalidates nothing. This
is the difference between a system that regenerates _a component_ and a
system that regenerates _everything and hopes_, and it is the reason the
pipeline can be trusted with a large system instead of a toy.

One more inheritance worth naming: the generator in the middle is
probabilistic, and the gates around it are not. A compiler’s optimizer uses
heuristics, but its type checker does not negotiate. The same division holds
here. A language model may produce the code, but types, contracts, and
evaluations judge it, and they judge it deterministically. Probabilistic in the
middle, deterministic at the edges. Everything that makes this pipeline safe
lives at the edges.

## **Intent Processing and Validation**

A compiler’s front end does not guess. Hand it an ill-formed program and it
does not produce its best approximation of what you might have meant; it
stops and points at the ambiguity. That refusal is a feature. It moves the cost

of a mistake to the cheapest possible moment, before anything downstream
has been built on top of it.

The first stage of the regeneration pipeline is a front end for intent, and it
does the same job. It takes requirements written in ordinary language and
turns them into a structured, typed representation: statements classified as
requirements, constraints, invariants, definitions, or context, connected by
explicit relationships. The taxonomy is not the point. The point is that
structure makes ambiguity visible. Prose can hold a contradiction
indefinitely and read perfectly well; two requirements that cannot both be
true sit in adjacent paragraphs and no one notices. Rendered as a graph with
typed edges, the same contradiction is a detectable conflict, something the
pipeline can surface and refuse to resolve silently on your behalf.

The field has been circling this idea for forty years. Design by Contract
made preconditions, postconditions, and invariants first-class parts of a
program instead of comments. Formal specification languages went further,
insisting that what a system must do could be stated precisely enough to
check. Those methods proved the value of making intent explicit, and they
also taught the cautionary lesson this stage has to respect: full formality is
so expensive that almost no one pays for it. The goal here is not a proof. It
is tractability. Enough structure to detect conflict and incompleteness, not
so much that writing the specification becomes its own doctoral program.

Validation, then, asks three questions of the intent: is it complete, is it
unambiguous, is it testable. Completeness checking looks for what the
intent did not say but must, the edge cases and failure modes that prose
omits because the author never hit them. It does this the way a careful
reviewer does: running the requirements against known failure-mode
taxonomies and the architecture’s catalog of edge cases, and making an
adversarial pass that asks what input or ordering the specification forgot to
rule out. It will not catch everything; nothing does. Its job is to turn the gaps
it can reach into explicit questions for the author instead of silent
assumptions buried in the generated code. Conflict detection looks for
requirements that cannot coexist. Both turn a silent guess into an explicit
decision. This is where my earlier claim that specifying is harder than

coding stops being rhetoric and becomes operational. The requirementsengineering literature has shown for decades that the most expensive
defects are the ones born in requirements, not in code, because they are the
ones discovered last. The pipeline moves the hard thinking to the stage
where fixing it is cheapest, and it does not pretend that stage is easy.

There is a subtler requirement on this front end, and it is easy to miss: it has
to be stable. If re-processing an unchanged specification reshuffles the
graph, every downstream identity churns and selective invalidation
becomes meaningless, because the pipeline can no longer tell what actually
changed. This is the content-addressing discipline again, applied to
meaning. The same intent must resolve to the same structure, so that a real
change stands out against a stable background. A probabilistic generator at
the end of the pipeline is fine. A probabilistic front end that can’t agree with
itself is corrosive. We return to this fault line at the end of the chapter,
because it is the place the whole architecture is most exposed.

## **Architectural Generation and Synthesis**

Between the front end and the code generator, a good compiler puts an
intermediate representation, and that single design decision is one of the
most productive in the history of the field. The intermediate representation
is language-independent and target-independent: many source languages
compile down to it, and it compiles out to many machines. LLVM turned
that seam into an industry. It is why a new language can reach every
processor by targeting one representation, and why a new processor can run
every language by consuming it.

The regeneration pipeline puts the same seam in the same place.
Requirements do not compile straight to code; they compile to an
architecture. The specification says what the system must do; the
architecture says how a system of that kind is built, its runtime, its patterns,
its conventions, its boundaries. Code becomes a build artifact produced to
satisfy the architecture, the way machine instructions are produced to
satisfy an instruction set. Many implementations can target one architecture

the way many languages target one processor. This is the compilation
primitive from Chapter 3 doing its work, and it is what keeps the pipeline
from being welded to a single framework’s momentary fashions.

The other job of this stage is to decide the unit of regeneration, which is to
say the grain. Requirements are grouped into implementation units, and the
grouping is not arbitrary. It follows the oldest good advice in software
architecture, Parnas on modularity: decompose a system around the
decisions that change independently, and hide each decision behind an
interface. A well-drawn unit owns the mutations of its own data, exposes a
versioned contract, and can be verified at its boundary without booting half
the system. Chapter 3 gave the tests for this; the pipeline applies them
mechanically, and the seam it looks for is data ownership, because who is
allowed to change a piece of state defines an architectural boundary far
more reliably than any file layout.

With units drawn, the pipeline assigns each one a risk tier and a boundary
policy, and connects them into a dependency graph. That graph is the thing
selective invalidation walks. It is also what lets the pipeline state a change’s
blast radius before generating anything, the set of components a change will
touch and the boundaries it must leave intact. Minimal but complete:
everything the intent requires, and nothing it does not.

And the boundaries themselves are the part that must not move. Chapter 2
argued that replacing code behind a stable boundary is maintenance while
changing the boundary is an architectural event; this stage encodes that
directly. An implementation unit’s interior is disposable, but its contract is a
promise to everything that depends on it, and regenerating the interior must
never quietly change that promise. When a contract does need to change,
the pipeline treats it as what it is, a coordination event, and refuses to let it
happen by accident. The industry learned this the hard way through years of
broken APIs and the discipline that grew up to prevent them; the pipeline
inherits the discipline rather than relearning it.

## **Implementation Synthesis**

Now the code. This is the stage everyone imagines when they picture AI
writing software, and it is the stage that matters least to whether the result
can be trusted, for the same reason a compiler’s back end is not where you
look to know if your program is correct. The back end generates
instructions guided by the intermediate representation and the target’s
constraints, and we accept its output because the constraints are tight and
the checks are real, not because we read it.

Synthesis in the regeneration pipeline works the same way. The generator
receives a unit’s requirements, constraints, and invariants, the architecture’s
conventions, worked examples of the patterns to follow, and the contracts of
the neighbors it must connect to. Generation is guided, not freeform. Then
the deterministic edge does its work: if the generated code does not
typecheck, the pipeline retries with the error in hand, and if that fails, it falls
back to a valid, mountable stub. A stub is not a fix. It typechecks and
satisfies the shape of the contract while doing nothing real, so it ships
disabled, behind a feature flag or as an explicit degraded mode, and the
status surface marks the gap loudly. The point of the fallback is to fail in the
open, where an operator can see the hole, rather than to pass broken
behavior off as working code. We already trust this arrangement in
production, everywhere. Parser generators, protocol buffer and OpenAPI
code generators, database migration tools, and object-relational mappers all
emit machine-written code from a specification, and we trust it because it is
generated from a declared contract and constrained by a checkable one. The
pipeline extends a trust model the field has relied on for decades to a
broader class of code.

What makes that extension safe is the oracle. Regeneration is conservative
when you have a way to evaluate the result and reckless when you do not,
and the difference is the whole game. Durable evaluations derived from the
requirements give a regenerated unit something external to be judged
against, something that survives the code it tests. The next chapter is about
what those evaluations are and how you write them, so I will save that
discussion for later, except to say the obvious thing the verification tradition
has always known: a test does not care whether a human or a machine

wrote the code under it. Property-based testing, contract testing, and
behavioral checks judge outcomes, and outcomes are indifferent to
authorship.

Verification is graded, not uniform, and here too the pipeline copies a
practice the field already trusts. Safety-critical software has always spent
more rigor where the blast radius is larger; avionics and payment systems
do not verify a logging helper and a flight-control loop to the same
standard. The pipeline makes that gradient explicit. A low-risk unit may
need only to typecheck. A higher-risk one earns property tests and a threat
review. A critical one does not ship without a human signing off. This is the
same principle the primitives chapter builds into pace, more rigor where the
blast radius is larger, turned into a policy the pipeline enforces rather than
one it hopes engineers will remember.

Finally, synthesis is selective. Only the units the last change invalidated
regenerate; everything whose justification still holds is left exactly as it
was. Incremental compilation and build caching have made this normal for
machine code for decades. The pipeline claims the same efficiency for
application logic, which is what makes regenerating a real system an
operation you can run on a Tuesday rather than an event you schedule for a
quarter.

## **Deployment and Observability**

A regenerated component still has to reach production without breaking the
system around it, and here the pipeline leans entirely on operational practice
the industry already trusts. A new implementation is deployed the way
immutable infrastructure taught us to deploy a new image: built whole,
rolled out behind a stable contract, never patched in place, and rolled back
by swapping the old version back in. Blue-green and canary deployment
gave us decades of experience replacing a running component safely; a
regenerated unit is just another artifact moving through that same
machinery. Because its contract held, its neighbors never learn that its
interior changed.

The harder half of this stage is staying honest after deployment, and the
danger it guards against is the one this whole book keeps returning to: quiet
failure, a system that works without anyone able to say why, until the day it
doesn’t. The observability movement was the field’s answer to exactly this,
the recognition that you cannot operate what you cannot see. A regenerative
system needs the same instrumentation pointed at a slightly different target:
not just whether the system is up, but whether it still matches its intent. Its
status surface has to be explainable, conservative, and actionable, and it has
to be honest about uncertainty. A monitor that cannot yet tell healthy from
unknown, and says “healthy” anyway, is worse than no monitor. Better to
say plainly that the system is still warming up than to emit confidence it has
not earned.

Two mechanisms keep the deployed system tied to its intent, and both have
direct ancestors. The first is drift detection. An edit made in place to
generated code is a drift event, the same category of mistake as logging into
a server to change a config file by hand.

Infrastructure-as-code tools already reconcile declared state against actual
state and flag the gap; terraform plan does nothing but show you
where reality has wandered from the specification. The pipeline applies the
same reconciliation to application code, and adds a discipline the
infrastructure world often skips: an unplanned edit is not rejected, it is
labeled. A fix to be harvested back into the requirements, a signed waiver
where a named owner puts their name to the divergence and its reason so
the pipeline stops flagging it while keeping who-signed-and-why on the
record, or a patch that expires on a known date and forces the question back
open when it does.

That labeling is not bookkeeping. It is the mechanism that keeps
regeneration from committing the one unforgivable sin, which is forgetting.
Mature code is full of scar tissue, the retries and timeouts and strange
conditionals that encode an incident nobody wrote down, and naive
regeneration destroys it. The label path is how a hand-fix made at 3 a.m.
during an outage becomes a requirement instead of a casualty of the next
regeneration cycle. The implementation remembers things the specification

has not yet learned, and the deployment stage is where those things get
carried back upstream rather than lost.

This loss of institutional knowledge is measurable. An exploratory study
compared ten machine-generated C and C++ projects against comparable
hand-built tools. The findings were stark: the machine-generated software
had shed almost all the design variability that traditional systems naturally
accumulate. Across those ten projects, there were only 45 total commandline options (a median of zero), and no conditional structure reflected a
deliberate design choice.

In contrast, established tools carry significant history. A single long-lived
tool like x264 exposes 184 options across more than 2,000 conditional
paths; even GNU’s simple 800-line wc utility exposes 8 options. While the
generated programs functioned correctly, they were “born” without the
hard-won, accumulated decisions that legacy implementations carry. This
demonstrates why a regenerative system requires a deliberate path for
design: if we don’t capture these decisions, we lose them during every
regeneration cycle.

The second mechanism closes the loop back to the beginning of the
pipeline. Production is not the end of the process; it is an input to it. A
component is correct only as long as the evidence still supports the claim
that it satisfies its requirements, and the world changes even when the code
does not. A regulation shifts, a dependency’s behavior drifts, a load pattern
nobody anticipated arrives. The reframed question is not “did the code
change” but “which claims about the system are no longer true.” Telemetry
that can answer that question localizes the drift to a specific part of the
intent graph, which invalidates exactly the subtree whose justification
expired, which hands the pipeline a concrete regeneration job. This is a
feedback loop of the ordinary control-theory kind, and it is what turns the
pipeline from a one-way build into a system that keeps a living application
aligned with a living intent. Provenance is what makes it auditable, and that
is the subject of Chapter 6; here it is enough that the loop closes.

That loop, though, only ever adds, and a reader who has been counting will
have noticed something missing. Chapter 3 named seven primitives; this
pipeline has quietly used five. Deletion and compaction never appear in the
machinery, and their absence is a real seam, not an accident of exposition.

The pipeline as drawn regenerates the invalidated subtree and stops, which
is precisely where I warned in Chapter 3 that sediment collects. Generation
with no paired removal step produces the conceptually overloaded system
that I cautioned against, and it produces it faster than any human could.

So the removal disciplines are not a stage inside the generation pipeline;
they run alongside it, driven by the same invalidation graph. When a change
orphans a requirement, deletion asks whether the component that
requirement justified can be removed rather than regenerated, and
compaction is the periodic pass that asks whether the surviving set of
concepts still earns its keep.

Chapter 8 takes deletion as its own subject and Chapter 9 does the same for
compaction. Here it is enough to mark the seam plainly: this pipeline
generates, and generation without a disciplined counterweight of removal is
just accumulation with better tooling. All seven stations are on the line; two
of them are about taking things away.

## **Where the Pipeline Breaks Down**

This chapter’s introduction promised honesty about the parts of this that
don’t work yet, and it is time to pay that. The pipeline is not uniformly real.
Some of its movements are ordinary engineering today, some exist only in
pieces, and one of them contains an unsolved problem the rest of the
architecture is standing on.

The back half is the solid part. Guided generation with a typecheck-andretry loop, verification graded by risk, selective regeneration, immutable
deployment, and drift detection are all either standard practice or a short
reach from it, and the coding tools of the mid-2020s already assemble crude

versions of the whole back end. If the pipeline were only its second half,
this would be a report on established practice dressed in new vocabulary.

The front end is where the drawing outruns the built thing, and it is where
the compiler analogy I have leaned on all chapter finally breaks. I am
breaking it on purpose, because you should see exactly where it stops
holding. A compiler’s front end checks a program against a formal grammar
and a language specification; “ill-formed” has a definition a machine
applies without judgment. The intent front end has no such standard. Its
input is human language, its notion of a contradiction is semantic, and there
is no specification that says what a well-formed set of requirements even is.
When a compiler rejects a program it is enforcing a rule. When the intent
processor flags a conflict it is exercising judgment, and judgment from a
probabilistic model is precisely the thing the rest of the pipeline works so
hard to fence out at its edges.

That gap concentrates into the fault line I flagged at the end of the intent
stage, and it is the crux of the whole design: stability. Selective invalidation,
the property that makes any of this safe at scale, depends on the same intent
resolving to the same structure every time. A deterministic front end gives
you that for free. A front end that reads meaning from language, using a
model that can answer the same question two ways on two days, does not.
If re-reading an unchanged specification reshuffles the graph, every
downstream identity churns, the pipeline can no longer tell what actually
changed, and it collapses back into the “regenerate everything and hope” it
was supposed to replace. This is the hardest unsolved problem in the
architecture. Everything downstream of it is engineering; this part is still
research, and an honest reader should weigh the whole chapter against it.

So the wager underneath the whole design is really a claim about this one
seam: that a probabilistic front end can be made stable and self-consistent
enough for a deterministic back end to stand on. The field’s decades of prior
art do not settle that question, because no prior compiler ever had a
stochastic front end. It is the genuinely new thing here, and it is unproven.
The rest of the pipeline is the field’s most trustworthy ideas reassembled;
this is the part that has to be earned.

## **Conclusion: The Oracle Comes Next**

Read back over this chapter and one word is carrying more than any other.
Every stage leaned on evaluation. Generation is safe because the result can
be judged against durable evaluations; verification grades itself against
them; deployment stays honest because production evidence tells us which
of a component’s claims have expired; the whole pipeline is conservative
rather than reckless only because an oracle exists to say whether a
regenerated component is still correct.

Chapter 3 already told you what a durable evaluation is. What I have yet to
show you is the harder thing: how to write one you can actually trust to gate
a regeneration, how to know when a suite is complete enough to rely on,
and why that work is genuinely harder than writing the code it judges. That
is the debt this chapter and the last one ran up together, and it is the whole
subject of the next. The pipeline is exactly as trustworthy as its oracle. Time
to build the oracle.

**About the Author**

**Chad Fowler** is a general partner and CTO at BlueYard Capital, where he
invests in AI infrastructure, decentralized systems, and developer platforms.

Fowler has been one of the most influential voices in modern software
development for over two decades. He co-created RubyGems and helped
shape the dependency management patterns (later carried forward by
Bundler and adopted by npm and Cargo) that developers now take for
granted. He co-founded Ruby Central, RubyConf, and RailsConf, and his
book The Passionate Programmer became a touchstone for a generation of
developers.

As CTO of Wunderlist, he led engineering through hypergrowth and
acquisition by Microsoft, where he subsequently ran Microsoft’s global
startup advocacy programs. During the 2014 Heartbleed crisis, he rebuilt
Wunderlist’s entire production infrastructure in a single day, proving the
immutable infrastructure principles he had championed in his 2013 essay
“Trash Your Servers and Burn Your Code,” which anticipated by a decade
the architectural shifts that AI-generated code now demands.
