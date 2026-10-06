---
title: AI Security Engineering (Dan Borges, David Campbell)
source: books/pdf/AI Security Engineering (Dan Borges, David Campbell) (z-library.sk,
  1lib.sk, z-lib.sk).pdf
source_type: book
source_hash: a09d1331f149d3b1d5874b3695a80782fe779374274535c3798172e08e433bdd
tags:
- security
- book
extracted: '2026-10-05'
---

# **AI Security Engineering**

## Securing Agentic Systems in Production

## **Dan Borges and David Campbell**

**AI Security Engineering**

by Dan Borges and David Campbell

Copyright © 2026 O’Reilly Media, Inc. All rights reserved.

Published by O’Reilly Media, Inc., 141 Stony Circle, Suite 195, Santa
Rosa, CA 95401.

O’Reilly books may be purchased for educational, business, or sales
promotional use. Online editions are also available for most titles
[(https://oreilly.com). For more information, contact our](https://oreilly.com/)
corporate/institutional sales department: 800-998-9938 or
_corporate@oreilly.com_ .

Acquisitions Editor: Nicole Butterfield

Development Editor: Gary O’Brien

Production Editor: Destiny Baitinger

Cover Designer: Susan Brown

Cover Illustrator: Monica Kamsvaag

Interior Designer: David Futato

Interior Illustrator: Kate Dullea

October 2027: First Edition

**Revision History for the Early Release**

2026-06-22: First Release

[See https://oreilly.com/catalog/errata.csp?isbn=0642572359133 for release](https://oreilly.com/catalog/errata.csp?isbn=0642572359133)
details.

The O’Reilly logo is a registered trademark of O’Reilly Media, Inc. _AI_
_Security Engineering_, the cover image, and related trade dress are
trademarks of O’Reilly Media, Inc.

The views expressed in this work are those of the author(s) and do not
represent the publisher’s views. While the publisher and the author(s) have
used good faith efforts to ensure that the information and instructions
contained in this work are accurate, the publisher and the author(s) disclaim
all responsibility for errors or omissions, including without limitation
responsibility for damages resulting from the use of or reliance on this
work. Use of the information and instructions contained in this work is at
your own risk. If any code samples or other technology this work contains
or describes is subject to open source licenses or the intellectual property
rights of others, it is your responsibility to ensure that your use thereof
complies with such licenses and/or rights.

979-8-341-67484-4

# **Preface**

## **Conventions Used in This Book**

The following typographical conventions are used in this book:

_Italic_

Indicates new terms, URLs, email addresses, filenames, and
file extensions

Constant width

Used for program listings, as well as within paragraphs to
refer to program elements such as variable or function
names, databases, data types, environment variables,
statements, and keywords

```
Constant width bold
```

Shows commands or other text that should be typed literally
by the user

```
Constant width italic
```

Shows text that should be replaced with user-supplied
values or by values determined by context

**TIP**

This element signifies a tip or suggestion.

**NOTE**

This element signifies a general note.

**WARNING**

This element indicates a warning or caution.

## **Using Code Examples**

Supplemental material (code examples, exercises, etc.) is available for
download at _[https://github.com/oreillymedia/title_title](https://github.com/oreillymedia/title_title)_ .

If you have a technical question or a problem using the code examples,
please send email to _[support@oreilly.com](mailto:support@oreilly.com)_ .

This book is here to help you get your job done. In general, if example code
is offered with this book, you may use it in your programs and
documentation. You do not need to contact us for permission unless you’re
reproducing a significant portion of the code. For example, writing a
program that uses several chunks of code from this book does not require
permission. Selling or distributing examples from O’Reilly books does
require permission. Answering a question by citing this book and quoting
example code does not require permission. Incorporating a significant
amount of example code from this book into your product’s documentation
does require permission.

We appreciate, but generally do not require, attribution. An attribution
usually includes the title, author, publisher, and ISBN. For example: “ _Book_
_Title_ by Some Author (O’Reilly). Copyright 2012 Some Copyright Holder,
978-0-596-xxxx-x.”

If you feel your use of code examples falls outside fair use or the
permission given above, feel free to contact us at _[permissions@oreilly.com](mailto:permissions@oreilly.com)_ .

## **O’Reilly Online Learning**

**NOTE**

[For more than 40 years, O’Reilly Media has provided technology and business training,](https://oreilly.com/)
knowledge, and insight to help companies succeed.

Our unique network of experts and innovators share their knowledge and
expertise through books, articles, and our online learning platform.
O’Reilly’s online learning platform gives you on-demand access to live
training courses, in-depth learning paths, interactive coding environments,
and a vast collection of text and video from O’Reilly and 200+ other
publishers. For more information, visit _[https://oreilly.com](https://oreilly.com/)_ .

## **How to Contact Us**

Please address comments and questions concerning this book to the
publisher:

O’Reilly Media, Inc.

141 Stony Circle, Suite 195

Santa Rosa, CA 95401

800-889-8969 (in the United States or Canada)

707-827-7019 (international or local)

707-829-0104 (fax)

_[support@oreilly.com](mailto:support@oreilly.com)_

_[https://oreilly.com/about/contact.html](https://oreilly.com/about/contact.html)_

We have a web page for this book, where we list errata and any additional
information. You can access this page at
_[https://www.oreilly.com/catalog/<catalog page>](https://www.oreilly.com/catalog/catalog_page)_ .

For news and information about our books and courses, visit
_[https://oreilly.com](https://oreilly.com/)_ .

Find us on LinkedIn: _[https://linkedin.com/company/oreilly](https://linkedin.com/company/oreilly)_ .

Watch us on YouTube: _[https://youtube.com/oreillymedia](https://youtube.com/oreillymedia)_ .

## **Acknowledgments**

# **Chapter 1. The AI and Security** **Problem Spaces**

In computer science, and especially in security, we rarely solve entirely new
problems. Instead, we build on well established math, programming
paradigms, and mental models to understand emerging technologies.
Security in particular is a discipline shaped by history and accumulated
lessons. Thedore Roosevelt famously said, “The more you know about the
past, the better prepared you are for the future.” Classes of vulnerabilities
have emerged and been mitigated over time, from memory corruption to
injection attacks, depending on the technologies and implementations. The
development of such attacks and solutions has led to some longstanding
security principles that can be applied when looking at new systems.
Concepts such as least privilege, input validation, and defense in depth were
not created for any single technology; they are security abstractions that
apply across generations of systems. By reusing these mental models, we
can more effectively reason about new architectures, including modern AI
systems, and anticipate where they may fail. Sometimes a simple
implementation trick is all it takes to solve a decade long vulnerability.

Throughout this book we will see that many modern security problems can
be reframed as traditional security challenges with well-understood
solutions.

This perspective is especially important as new paradigms emerge. AI
systems have brought about entirely new classes of vulnerabilities, and the
nature of their nondeterminism also resurfaces dozens of traditional
vulnerabilities. While the implementation details may change with the
technologies, the underlying security challenges often remain consistent. If
you are building large scale AI systems, you may be introducing
vulnerabilities at the architecture level without even knowing it. The ability
to map a new problem space to known categories is one of the most
powerful tools in building secure systems. Technologies and capabilities
may evolve, but the consequences or impact of a successful exploitation
remains a consistent way to assess the security risk of a system. However,
those technologies do play a critical role when it comes to implementing the
appropriate fixes and controls in that system. In this chapter we are going to
lay out some core security principles that will help the reader in any infosec
situation. From there we will move to some fundamental principles of AI
systems, as they will be helpful in how we understand common problems
with these systems. Finally we will look at a unique mix of security and AI
issues.

## **Traditional Security Theory**

Security is a very deep and old field full of traditional lessons we can draw
from in this new environment. A lot of the following sections are a
selection of traditional security and information security best practices.
These security principles can often be leveraged to think about problems
abstractly and reason about new design patterns and threats. Specifically
these paradigms are often helpful with red teaming or threat modeling and
trying to think about ways to attack an application. This isn’t a full review
or understanding of information security, for example we won’t cover many
basics such as the CIA triad (that’s confidentiality, integrity, and availability

for our non-security-wonks) or fault tolerance. But we will cover core
strategic principles that are particularly relevant to AI systems. These are
problems and mental models the reader can use to help articulate and solve
vulnerabilities as they surface in AI systems. Rick Howard boils down what
a principle is in his book “Security First Principles”.

There he has a lot of good, guiding philosophy on how we can navigate
understanding principles. “must not be derived from one another nor from
anything else, while everything has to be derived from them.” and as he
[takes from the general practice of “First Principle Reasoning”: you boil a](https://en.wikipedia.org/wiki/First_principle)
problem down to the fundamental truths that you know must be true in any
situation.

He arrives at one fundamental principle in his book, which is “Reduce the
probability of a material impact due to a cyber event over the next three
years.”. That is great, but it doesn’t give us any mental models or tools to
actually reduce negative cyber events. Therefore I think we can boil down a
bunch more Infosec phenomenon down into principles. These fundamental
rules can help us reason about infosec systems beyond “we need to reduce
risk”, and give us tools to effectuate that. These fundamentals will start to
give operators controls and logical frameworks to leverage that can be
combined into an effective strategy to reduce risk.

### **Untrusted Input**

_Untrusted input_ is a fundamental issue in computer and web security. At its
most basic, if we have users, they can submit maliciously crafted input to
attack the system, and we will otherwise refer to this category of problems
as _untrusted input_ . Even if you completely trust your user base, user
accounts can be hijacked (through techniques such as credential phishing),
and operated in a malicious manner. We can see this as a core principle and
[best practice on sites like securecoding.org, underscoring the importance of](https://www.securecoding.org/secure-coding-principles-best-practices/)
input validation in regards to untrusted input. This principle states that if we
are going to have user input, we should treat it as untrusted, or simply
“never trust user input”. Thus we should be able to produce a principle on

untrusted input. That principle can be as simple as: _“Treat all external input_
_as potentially malicious until validated within the intended context.”_

Several historical attack categories, like SQL injection, cross-site scripting
(XSS), and command injection all stem from untrusted user input. If we go
back even further, we can see this entire category emerging from a quality
control problem space known as “unexpected input”. Quality control
programmers often write unit tests to test the bounds of a system by
providing input intended to crash it to make sure the system handles
unexpected input elegantly. This type of programmatic testing has a rich
background and, in our opinion, has evolved into modern security scanning
and even model evaluations.

We can see a number of controls arise out of the same attack categories,
controls that can still be used and have relevancy in other _untrusted input_
scenarios. Controls such as input sanitization, removing special characters,
strongly typed objects, parameterized queries, and output sanitization
(which we will explore throughout the book) are all still as relevant to
writing applications that leverage LLMs or generative models today.

This is particularly relevant to AI systems as systems can take user prompts
and this changes the output of the system. This can result in prompt
injection or unexpected outcomes of a system where a user can directly
influence the input of an LLM system. It’s a fundamental property of LLMs
to take that text input, and if that’s taken directly from “untrusted users”
then it may open up the system to a wide category of attacks.

The essence of this problem is that we can’t always trust users (or agents).
Anywhere a user could send the system input is a place an attacker could
try to maliciously harm the system. Thus, you need to treat every user as
potentially malicious, even internal users based on the threat model and
security requirements of the system.

Believe it or not, this is an aspect of the Behaviour of a system, especially
when this input is passed to a model. In that regard we should actively test
for these failure scenarios, but also build controls that generally constraint
these failure cases.

### **Access controls and Security Boundaries**

This is a fundamental tenet of security, which is commonly gated by
_authentication_ and _authorization_ . Authentication is essentially your ability
to prove “who” you are, established through what you know (passwords),
what you own (keys), or even biometrics. Whereas Authorization is what
you have permissions to access with that identity. As a shorthand, and a
good mnemonic for remembering them, people often call Authentication,
AuthN, and they call Autherization, AuthZ. Both of these features together
make up what we have come to call _Identity_ within the context of
Behaviour, Identity, and Control (BIC). At the core of BIC we need to
establish what is the intended behaviour and what is the system’s core
identity, then we can design access controls for systems such that we can
limit permissions to the intended permissions.Thus, we can produce another
principle of information security, rooted in zero trust architecture: “Access
decisions should require verified identity and explicit authorization before
actions are permitted.”

It was the number two issue when the OWASP Top 10 debuted in 2003. The
security issue has persisted through dozens of different technologies in that
time. Access control is now the number one issue on the 2025 OWASP Top
10, showing that even decades later we still struggle to get core properties
of information security right.

[Granted there is an OWASP top 10 specifically for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
that doesn’t include this, but in my experience leading security engineering
at a major AI development company, this is a timeless issue (h).

A trust boundary or security boundary is a location where assumptions
about identity, behavior, permissions, or security guarantees change
between systems, users, devices, processes, or environments. Good security
design incorporates identifying trust boundaries and defining what
capabilities, permissions, and assumptions change across them. Mapping
trust boundaries is a prerequisite to designing effective security controls.

One of the reasons I like identifying security boundaries is because it
creates an easy delineation marker for security practitioners where they can

measure and control how a system gains new privileges, or moves across a
security boundary. It’s important to identify any of these security
boundaries and ensure we have proper access controls at each of those
points. Whenever the application fetches sensitive data, or accesses a user’s
profile information, there should be an explicit authority check (who is this
user, do they have access to this data). This is most commonly then
implemented in middleware. But having those clear boundaries highlighted
in a plan or scoping document, then applying those controls ubiquitously
through a common middleware is a great way to write a single set of
functions and ensure you are securely accessing data or features.

### **Control Decay**

One thing we need to talk about is the idea of ‘bit rot’ or that technologies
become less effective over time. When we consider the speed at which
innovation occurs now, it is fairly easy to exploit or bypass a given set of
controls. At the time of writing this in the summer of 2026 the infosec
community witnessed an explosion in exploit development due to AI
assisted technologies. The idea is similar to ‘bit rot’ in the sense that
technology becomes less effective over time as the technologies around it
evolve; In information security we tend to call this security control decay.
Our friend Chris Nickerson regularly preaches about the dangers of security
control decay, or the idea that that security technology tends to lose its
effectiveness over time unless it is actively updated. In this sense, controls
will eventually fail over time, as engineers we want to reduce this risk of
failed controls by staggering layered controls.

Consider the following example, a cloud environment where a VPC firewall
rule was originally designed to allow outbound communication only from a
single microservice to a specific external API. At the time, the rule was
highly restrictive and effectively enforced the principle of least privilege.
Over the next several years, however, the environment evolved. New
microservices were deployed, third-party integrations were added, and
development teams requested additional network access to support new
business requirements. Rather than redesigning the architecture,

administrators gradually modified the existing firewall rule by adding more
approved destinations, broader IP ranges, and additional exceptions.
Individually, each change was justified. Collectively, however, they
transformed a narrowly scoped control into a much more permissive one.
The firewall rule still existed, and on paper the control remained in place.
Yet its security value had diminished significantly. This is an example of
control decay. The control became less effective over time because the
surrounding technology, business requirements, and operational practices
evolved faster than the control itself.

As we transition this to information security, we can apply this as a
principle of control decay: “Security controls lose effectiveness over time
unless continuously tested, updated, and challenged.” In applying that to the
above example, the right move would have been to deconstruct the everexpanding network firewall rule, into specific service or host roles, making
each one tight and explicit to the service it is controlling. One of the reasons
we lay this principle out is a lot of automation work tends to be set-andforget, but time has shown that all things decay, even technology. This
principle tends to serve as a good basis for the next principle, which is
layering controls to counter when an individual control may fail.

### **Defense in Depth**

As we’ve previously seen, control decay is real and controls can and will
fail spontaneously over time. Sometimes even security controls themselves
can have vulnerabilities or bypasses in the underlying technologies. This
persistent issue of control failure means we should be prepared for control
failure, and one solution for such a scenario is to have overlapping controls.
Thus we can produce an infosec principle on this phenomenon such as:
“Security improves when independent controls overlap such that failure of
one does not produce a total failure of the control set.” And that is really the
crux of Defense in Depth.

The idea of _defense in depth_ comes from the military planning sphere of
security. In the military definition defense in depth refers to the ability for a
commander to lose space strategically while still responding and winning

the war. We can see the same concept adopted in information security; by
moving our most critical or important aspects behind several layers of
abstraction and security controls, we can engineer acceptable losses into the
scenario. Thus if we are hacked in one location, we should be able to
respond appropriately before the crown jewels or the most critical systems
are affected.

We can see the navy write about it in the following context:

“The key is creating multiple independent and redundant layers of defense
to compensate for potential human and mechanical failures so that no single
layer, no matter how robust, is exclusively relied upon to prevent an
accident.” <sup>1</sup> One of their key arguments is that while this may seem like
overhead or overengineering, it’s actually a safeguard against the
inevitability of error. It’s essentially a systems engineering approach to
layered error handling.

Bruce Schneier, security elder and thinkist, wrote about this back in 2000,
[in his "The Process of Security.” It’s a fantastic process that largely holds](https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html)
up today, which prioritizes defense in depth among other controls we
discuss in this chapter. Schneier puts it simply, “Don’t rely on single
solutions. Use multiple complementary security products, so that a failure
in one does not mean total insecurity. This might mean a firewall, an
intrusion detection system and strong authentication on important servers.”

[And to quote Bruce Schneier one more time, this time echoing age old](https://risk-engineering.org/concept/defence-in-depth)
wisdom, “There’s no such thing as perfect security. Interestingly enough,
that’s not necessarily a problem.” We will discuss in

Having multiple security controls either at different layers of the kill chain
enables us to catch and respond to attackers throughout their attack
lifecycle, not just at a static point in the attack. In Dan’s other book,
_Adversarial Tradecraft in Cybersecurity: Offense vs Defense in Real Time_
he goes into the game theory and reaction correspondence of an attacker
penetrating through layered security technologies and how either party can
[react in regards to those killchains. This is where defense in depth is](https://github.com/ahhh/Cybersecurity-Tradecraft/tree/main/Chapter4)
arguably most helpful. There is a saying in infosec that goes “attackers only

have to be right once, defenders have to be right every time” however the
corollary to that, especially with well engineered systems, is that “attackers
only have to make one mistake that defenders catch”. In _Adverserail_
_Tradecraft_ Dan shows several techniques where defenders can the attackers
pivoting through their environment by utilizing _defense in depth_ .

### **Principle of Least Privilege**

This is another core principle we will leverage when designing systems.
This is our infosec principle and fundamental idea of least privilege access
when designing a system. Specifically, I’m thinking of the _Principle of_
_Least Privilege_ **_(_** _POLP_ **_)_** [which can aid us here. As defined via CrowdStrike:](https://www.crowdstrike.com/en-us/cybersecurity-101/identity-protection/principle-of-least-privilege-polp)

_The principle of least privilege is a computer security concept and_
_practice that gives users limited access rights based on the tasks_
_necessary to their job. POLP ensures only authorized users whose_
_identity has been verified have the necessary permissions to execute jobs_
_within certain systems, applications, data and other assets._

Essentially, the Principle of Least Privilege tells us that each part of the
system should have the minimum permissions necessary to perform its task,
and no more permissions than that.

This is a lesson that has been learned time and time again throughout
computing. More recently, we can see it clearly in the world of
microservices. There, when PoLP is not applied, it actively contributes to
an increased attack surface, a wider spectrum of errors, and enables
privilege escalation throughout the system.

[A blog article by Shahzad Bhatti details many common vulnerabilities and](https://shahbhat.medium.com/security-challenges-in-microservice-architecture-a6065dbedce9)
recent 0-days that could have easily caused incidents in microservice
systems. Right up front, he talks about frameworks, methodologies, and
best practices one can apply to reduce the impact of these vulnerabilities.
And unsurprisingly, many of those practices overlap with principles we
cover in this chapter, from defense in depth to failing securely, and most
relevant to our conversation, the Principle of Least Privilege is right near
the top.

What this shows is that over time, new and unknown vulnerabilities will
appear and affect our systems. That said, we can still reduce the impact and
blast radius of those incidents through well-engineered systems.

This applies even more to LLM tool use than to microservice architecture.
Why? Many of the properties we’ve already explored:

LLMs are probabilistic in nature

They are far less predictable, even in normal execution (including
hallucinations)

They are susceptible to contextual manipulation and unique classes of
injection attacks

The industry has already felt the impact of this. Researchers have had
[agents delete all their emails due to over-permissioned systems. Agents](https://techcrunch.com/2026/02/23/a-meta-ai-security-researcher-said-an-openclaw-agent-ran-amok-on-her-inbox/)
[have even taken down production environments. These are clear examples](https://medium.com/@adarshpriydarshi5646/when-ai-deleted-production-a-case-study-of-the-aws-kiro-outage-f6b1484a1355)
of permissions that agents shouldn’t have. or at the very least should be
rate-limited and tightly controlled.

In response, the industry has noticed this ratcheting increase in tool and
agent permissions and has begun building frameworks to limit them.
[Research like MiniScope, along with frameworks such as AgentScope and](https://arxiv.org/pdf/2512.11147)
[NanoClaw, are all steps in this direction.](https://github.com/qwibitai/nanoclaw)

**Supply Chain Attacks**

In 2026 we’ve begun seeing attacks in increasing volume targeting
dependency installations or the software supply chain. Many of the largest
attacks in this area were targeted attacks against specific developers that
maintained large software repositories. But something else novel emerged
on the edge of AI generated code and supply chain attacks.

[There has been such a rise in hallucinated dependency names by model](https://snyk.io/articles/package-hallucinations/)
[systems. that attackers have begun typo squating such packages, and](https://snyk.io/articles/package-hallucinations/)
essentially typosquating software that was AI hallucinated. Traditional
cybersquating or typosquatting relied on developers mistyping trusted
[package names. This new type of attack, coined as Slopsquatting instead](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/slopsquatting-when-ai-agents-hallucinate-malicious-packages)

weaponizes hallucinated dependencies. This is obviously a funny play on
[the term slopcode, which is what many people had come to call purely AI](https://www.greptile.com/blog/ai-slopware-future)
generated code.

All this is to say that reviewing your software bill of materials, from the
dependencies used to the API calls programs make is still a critical step.
More now than ever we need to use automated scanners to update our
packages, monitor for new vulnerabilities, and check our code bases for
known weaknesses. As AI coding assistants become more deeply embedded
in software development workflows, their errors become part of the attack
surface. The software supply chain is a core component of application
security and should be explicitly addressed for major projects. Now more
than ever with AI generated supply chain artifacts.

### **Monitor What We Can’t Control**

I like to think of computer systems like wandering a series of dark rooms,
or even a series of connected buildings. In these buildings there are tons of
boxes of information, but you need access to the rooms and a light to look
through all of the boxes. For whatever reason, I tend to think of network
scanning and searching file systems like that, albeit at scale and using lots
of automation. Likewise if we are defending these systems we will want to
wire them up such that we know what is going on inside of them. We want
to know if there is someone sneaking around, or if one of the buildings has
caught fire. This is only possible if we are able to observe them remotely,
and thus we reach the crux of this principle: observation. Our principle of
observation will state: “You cannot secure behaviors you cannot observe.
Systems require sufficient telemetry to distinguish intended behavior from
anomalous behavior.”

One of the best ways to organize computer telemetry in my opinion is
through a concept known as _centralized logging_ [. Splunk defines it as the](https://www.splunk.com/en_us/blog/learn/centralized-logging.html)
following, “Centralized logging consolidates logs from multiple sources
into a single system, simplifying monitoring, troubleshooting, and analysis
across complex environments.” They enhance this definition further adding,
“By providing visibility, log data can help you to enhance reliability,

improve performance, and fortify the security of your system’s
infrastructure.”

Another amazing benefit we tend to get from centralized logging is data
normalization. Data normalization is the act of transforming all incoming
data into a common schema to make it easy to reference and join across
complex queries. Logging, and its direct corollary detection engineering, is
a core pillar of security engineering. Centralized logging can allow the
security teams of an organization to better understand incidents, collect
evidence, investigate compromise, and respond to active threats. Think of
this as the body’s ability to respond to sickness. If you get a fever, there are
several alarms that help you identify and fight infection or disease.

In many of these situations, we desire to prevent the bad activity from
happening in the first place. Unfortunately, that isn’t always possible, or we
don’t know about the bad activity until it’s already after the fact and we are
investigating the incident post-mortem. We want prevention, but we need to
assume that some failure is inevitable and should be ready to respond
accordingly. In many ways this is an extension of defense in depth. One of
our layered controls should be the ability to monitor the health of the
system, or the health of our controls. This will let us know if we are under
attack and give us options to respond to the attack.

To take this even further, oftentimes in security you can’t always outright
prevent something. Such as if you have a vulnerability with no issued
patches in critical customer facing software. Sometimes you don’t have the
luxury of taking a thing offline or patching it (if such a patch even exists at
the time). In such situations you can’t always apply a control to a certain
thing. In those situations, the next best thing is to set up verbose monitoring
and logging of its operations to see if you can detect it acting abnormally or
strangely.

Logging is a fundamental part of incident response (detection), and
something we will build into any systems we are engineering. We can also
see this as a core part of several common control sets, such as CIS and
NIST 800-53.

**CIS (Critical Security Controls): Control 8: Audit Log Management**

Key practices:

Collect logs from all critical systems

Ensure logs are protected and immutable

Regularly review and analyze logs

**NIST SP 800-53 (AU – Audit and Accountability family)**

Defines logging as a mandatory control family. Emphasizes:

Event logging

Log retention

Log analysis and correlation

As such our AI systems should be well instrumented to not only log errors
(for their own debugging), but log critical user interactions and security
functions (for example, when it needs to make calls across security
boundaries).

### **Fail Securely (Fail Closed)**

When a system fails, how does it fail? It should fail in a way that does not
allow for more permissions or result in unexpected behaviour. In security
we call this _failing closed_ or _failing securely_ . This is another classic control
that we can blatantly steal from Bruce Schnier’s “The Process of Security”.
This idea of failing securely is more important than ever in agentic or LLM
systems, as these systems can easily chew through funds (tokens or energy)
when they enter a looping failure state. If you’ve worked with agents in any
capacity you’ve probably seen them rabbit hole on a problem, and spin their
wheels endlessly trying to solve an impossible task.

All systems fail, and infosec is often the exploration of very specific failure
cases. Thus we can define this principle as: _Failure in computer systems is_

_inevitable; secure system design considers this and constrains the_
_consequences of failure._

Generally speaking, failures should reduce capability, not expand it. But
this is also where smart engineering comes into play, and people need to
consider these controls. We can have the example of a door that stops
working. In a high-safety / life critical situation, perhaps that door should
_fail open_ such that people can escape and life can be saved. In a security
system or a vault like system, maybe the system should fail closed such that
if it fails for any number of reasons (losing power, act of god, etc..) then it
doesn’t result in the system being breached.

Now imagine a secure facility with a door that controls access to a restricted
area that is critical to the business operations. If a catastrophic bug causes
the door controller to malfunction, permanently locking it could be just as
disruptive as leaving it open. Rather than choosing between fail open and
fail closed, we might design a more sophisticated system. If the primary
access control system fails, a secondary system takes over, perhaps
requiring additional verification, human approval, a limited smaller door, or
alternate credentials. In this case, resilience comes not from the door simply
failing open or closed, but from having a deliberate sub-system for when
failure occurs. This is another control that we can see echoed across other
common control sets, such as NIST 800-53 again.

**NIST SP 800-53 control framework**

Controls emphasize:

Secure failure states

Least privilege enforcement even during failure

**NIST SP 800-160 (Systems Security Engineering) control framework**

Explicitly calls for:

Systems to “fail in a known secure state”

Again these are security mental models we will apply throughout the book
in various ways. We will call back to this theory when we do.

### **Planning is a Security Control**

As defined by National Institute of Standards and Technology in NIST SP
800-53, Planning is itself an entire security control family. That decision
isn’t made lightly, I can’t tell you how many bad decisions or vulnerabilities
my teams have removed in the planning stage. Planning before diving into
any kind of prompting or agent tasks, will almost always yield greater
results and a more high quality product. By planning we mean setting up a
formal project structure, outline, and goals, at development milestones.

Planning in security can’t be understated. In large corporate environments,
engineering and security teams often push for design documents, or a
formal way to discuss the plans and implementation of a project in a
technically rigorous way. This is similar to the way several engineering
teams will meet to discuss the master blueprint on large building projects.
Depending on the situation plans and controls may be subject to various
regulatory frameworks, so why not factor those into the planning stage
early. Large projects may also involve multiple teams, so having a plan that
people can make decisions on and use as a north star while building is very
important.

We will also see how effective this can be for both project development and
agentic development. Later in this chapter we will clearly see how planning
adds benefits with the ALARA framework and their testing results. If we
lay out the plan well, the effects are felt downstream in multiple ways, from
simply a better organizational layout to mitigating entire vulnerability
classes through making good core technology decisions.

I won’t belabor this point or bombard you with ancient planning quotes, but
this is a strategic step that is as old as time. You would be remiss to not
explicitly include this step when setting up a new project.

## **AI and Security Theory**

Artificial intelligence systems are fundamentally probabilistic systems that
produce outputs based on patterns rather than fixed logic. This distinction
fundamentally changes how we reason about their behavior, correctness,
and risk when performing certain activities. While these systems can appear
coherent and intentional, their operation is governed by statistical inference
and more susceptible to emergent behaviors when compared to traditional
systems. When artificial intelligence systems are placed into real-world
environments, traditional security assumptions intersect with probabilistic,
non-deterministic systems in ways that create entirely new classes of risk.
Systems that appear capable may not be reliable over time. Systems that
follow instructions in tests may misinterpret intent in the field. And systems
that operate correctly in isolation may exhibit emergent behavior when
composed with other tools or agentic systems. The protection of AI systems
represents an evolution beyond traditional security practices, requiring
careful adaptation of established principles to systems characterized by nondeterminism and adversarial manipulation. As security engineers, we
should assume the system will deviate from intended behavior some of the
time, and constrain its activities such that it does not present catastrophic
risk. The following sections outline the core conceptual properties of AI
systems that are most relevant to security engineers when designing,
evaluating, or securing systems that leverage models in their core
functionality.

### **Non-Determinism & Probabilistic Behavior**

One of the core principles of LLMs or AI systems in general, is that they
have probabilistic outcomes; they are non-deterministic systems. This
means that given the same exact input, LLMs will often produce two
slightly different outputs, and this is a desirable feature of this technology.
At their core, large language models (LLMs) don’t always return the same
answer, and there are numerous mathematical reasons for this (see
["Defeating Nondeterminism in LLM Inference“). From sampling the](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
tokens, to floating point math, and concurrent associations, there are

multiple places where non-determinism is consciously implemented in the
design of the system.

Granted, these models can be tuned or configured differently. You can
change the temperature, which is a setting on the model to reduce the nondeterminism or chaotic nature of the model. That said, there has been
research that shows that even when these settings are tuned, with the
temperature set to 0, the model will still assert non-deterministic behaviour
[(see "Non-Determinism of ‘Deterministic’ LLM Settings). We can see this](https://arxiv.org/html/2408.04667v5)
is because LLMs, and most other models, at their core are token prediction
engines. Further, many of these models are fine-tuned in a post-training
stage, where they are optimized for generally meeting the possible most
answers and their output formatting (want to learn more about the different
[types of model training and how they are used? IBM has an entire free wiki](https://www.ibm.com/think/topics/llm-training)
on machine learning with tons of detailed subjects. They are statistically
trying to predict which elements or tokens come next, to please the largest
group of people, rather than logically understand and answer a question (see
"Deterministic vs Probabilistic AI: Why Modern Models Lack
Predictability“).

Therefore our programs can very likely have unintended or non-predictable
behaviour if we use these models in a part of the program that makes core
decisions or uses some kind of evaluation logic. In many ways, you aren’t
calling a single function with a deterministic output; you are querying a
field that can have a wide range in its response. What makes it hard for us
as engineers is that the field is largely a black-box or unknown to us, that
we can only interpret through the oracle of the LLM.

So as programmers and security engineers, we need to build the
determinism around the models and AI systems. This means adding
controls to make sure the system can’t act outside of its expected behaviour
or output. Occasionally we will discuss guardrails within the model context,
but the focus of this book and our engineering efforts should be on the
controls of the actual systems or programs that refine and act on the output
of the models.

### **The Importance of Saving our Prompts**

Prompts to LLMs function in a similar way that source code does to an
executable program. It allows us to view the intents, intended constraints,
and control flow in an easily interpretable way rather than trying to
understand it through the output alone. Similar to infrastructure-as-code,
storing and refining prompts provides us a semi-reproducible and
inspectable way into system behavior, enabling refinement and the ability to
save highly effective parts of our prompts over time. It’s hard to understate
the ability to version, trace, and iterate on prompts is critical for debugging
as we evolve our program over time. It will enable us to be more scientific
with these systems over time and they also tend to function better when the
prompts are full detailed instructions as opposed to one-line prompts.

Claude does this natively under the current user context, you can see a
fairly extensive log of your model prompts and their associated projects,
session IDs, and time stamps under .claude/history.jsonl. If we want to start
[to capture this output in Github, we can see an example of how that is used](https://github.com/ahhh/Mork_Items/commit/a2bf8d64a75dc07d8746648a654c20812a64c358)
below.

**_Prompt_** _: Any output you give me here, you will also add as a “git commit_
_-m” comment when you we go to “finalize” our work and “git add” our_
_additions to the project. I also want you to save my exact prompts with_
_that corresponding output and this commit based on the current_
_sessionID ~/.claude/history.jsonl._

However, “sharing prompts” also introduces a new attack surface,
especially the more connected to external systems our LLMs are. Because
prompts are interpreted and may lead to code execution, they are just as
vulnerable to injection, manipulation, and those various threat models. This
is why programs like _Claude Code_ will warn us when opening new
repositories, because depending on the context of the system running
untrusted prompts can be just as dangerous as running untrusted code.

Thus as re-usable prompt libraries evolve over time into reusable and
sharable “skills”, they must be treated with scrutiny like any other part of
our software supply chain. Ideally we would introduce static scanners to

these repos to look for keys, backdoors, vulnerabilities, and general
misconfigurations. These security scanners could also look at prompts for
common prompt injection keywords to make sure our supply chain isn’t
compromised over time. Some tools to help scan for this type of activity
[already exist, such as skill-scanner and razin, although I imagine we will](https://github.com/cisco-ai-defense/skill-scanner)
see this functionality incorporated into more flagship infosec products over
time as well.

The prompt is really just a guiding mechanism for the program execution, it
shouldn’t be the security boundary or enforce permissions. I’ll repeat that
for emphasis: _the prompt is not a security boundary and should not be_
_treated as a decider for access controls_ . While prompts and plans can
describe the intended constraints and outcomes, they can’t guarantee
adherence as we’ve already seen. In this sense, “security through prompt
conditions” is analogous to “security through obscurity”, in that it provides
a false sense of control without real enforcement. Another way to remember
this slogan is “security through text, fails under stress” The prompts
certainly guide the behaviour, but ultimately the system must be engineered
to enforce and support the permissions of the program. Therefore the true
security controls will be implemented outside the prompts, such as
programmatic checks, filesystem permissions, network controls, and scoped
API access, which will ultimately determine what the program is capable of
doing beyond its intended prompt instructions.

### **Context Windows & Memory Architecture**

Context windows define the working memory of LLM systems, but their
effectiveness is determined less by sheer size than by structure and
relevance. Modern models may support extremely large context windows,
yet increasing context size does not automatically increase the quality of the
output. Most daily use of frontier models doesn’t even come close to using
the full context window anyway. In practice, very large contexts often
become noisy and inefficient unless the information being fed to them is
carefully organized. Research on long-context performance has repeatedly
shown that models do not use every part of a large prompt equally well;

relevant information can become harder to retrieve or apply when it is
buried in the middle of long inputs or when it is surrounded by less relevant
tokens. <sup>2</sup>

The key distinction is that more context is not the same thing as better
context. A large window is only useful when the model can reliably find,
prioritize, and reuse what matters. Without structure, large prompts become
a messy dumping ground of notes, instructions, examples, and partial
outputs. The result is often a weaker signal-to-noise ratio when compared to
well reasoned responses. That is why context engineering matters more
about structure than context length alone.

One of the modern techniques for adding structure to the context is using
files to externalize intent and execution. A simple _plan.md_ does several jobs
at once: it compresses intent, structures other information, filters noise, adds
phases for human-in-the-loop interaction, and acts as a stable anchor in
context. Instead of forcing the model to infer the goal again and again from
a long conversational trail, you give it a durable artifact that states what the
task is, what has already been done, and what remains. As the working
context fills up, the model can return to that file to refresh its orientation
instead of drifting away from the original objective. This is often far more
reliable than hoping the entire conversational history remains equally
salient. The same principle applies to extra functionality, summaries,
rewritten plans, and execution logs. Compartmentalization, recall, and
summarization are often treated as a token-saving tricks but they are more
fundamental than that. Summarization is one of the main ways LLM
systems simulate continuity within an inherently stateless architecture.
Summary objects are so powerful because they both shorten context (cost
savings) and notating the parts that matter by constantly updating some type
of memory structure. Summarizing hits many bullet points for us, it’s
logging, it’s optimization, and it’s improved memory management. That
said, if the summarization is rewriting the same file, consider saving a copy
or backup for a historical reference.

Frequent summarization on small edits becomes even more powerful in
large or long running workflows. Rewriting plans, updating progress notes,

and tracking execution in a log file or memory object allows the model to
carry forward known verified good ideas from one stage to the next. Each
summary can work as a handoff between agents, as well as a step for
verifiers to act on the data. The verifiers can be human or automated, but
really shouldn’t be LLMs checking other LLMs work, and if they are they
shouldn’t be the same model. How you structure either the memory, output,
or log files is very likely application dependent, but at some level you
should employ summarization if you are planning a multishot project. If
you are at a lack of what to summarize simply go with what was attempted,
what worked, what failed, what are the current assumptions in play, what
planned steps have been accomplished, and what are the planned next steps.
That in even its most basic form, will reduce token use and improve
coherence, reference quality, and task continuity. This will also help you
from restarting from ground zero if your session were to end. Solutions like
Claude Code will also attempt to manage memory naively for the user, but
I’ve always had way more success doing it myself (such as in the git
comments if I want to avoid project bloat, but track per-commit changes).
In practice such artifact-driven workflows often outperform both naive chat
systems and full autonomous agent systems. In these workflows, the user
and the AI jointly maintain context and memory through files or memory
objects such as plan.md, prompt files, while the user also reviews logs,
summaries, and outputs that are later reused as inputs.

Many people argue that agents are the natural answer here, and in some
settings they are. But in practice, agentic systems still often get caught in
loops, overcommit to faulty assumptions, or fail to work past their own
blind spots. Artifact-driven workflows offer a more controllable alternative.
They let practitioners preserve continuity without surrendering oversight.
Further we are going to attempt to replace agentic oversight with more strict
controls, and in many ways this will look like more traditional
programming to support agentic systems. I’ve personally seen many cases
of agentic swarms totally losing the plot and just burning resources in a
loop. I’ve also seen projects go so long on platforms like the early days of
Manus that the chat window loses context of many of the things it has
previously done.

This approach also aligns well with what research has shown about
intermediate computation. Models often perform better when they can
externalize reasoning into scratchpads, intermediate outputs, or reusable
scaffolds instead of trying to solve everything in a single pass. By
combining curated context, iterative summarization, and reusable scaffolds,
practitioners can move beyond ad-hoc prompting toward workflows that are
more reliable, more stateful in practice, and better aligned with how these
systems are designed to operate. This becomes especially important in
large, multi-step processes that cannot be solved well in a single shot. This
also becomes important when people talk about engineering reliable agentic
systems. Our goal here with optimizing the context window is to ultimately
make the application more usable, stable, and accurate over time as we
develop on it. <sup>3</sup>

### **Verify Before Trust (Code Reviews / Human in the Loop)**

There’s an old quote that Ronald Regan once used that goes “Trust but
verify”. While this was important at the time for diplomatic reasons,
logically the phrase should be “Verify then Trust”. This is the core
philosophy that ‘zero-trust’ espouses. Originally put forward by John
Kindervag, the concept flips traditional network security on its head.
Instead of assuming everything inside an organization’s network is safe,
Zero Trust mandates continuous, explicit verification of every user, device,
and connection, regardless of whether they are inside or outside the network
perimeter. <sup>4</sup> This principle of _always verify at permission boundaries_, is
going to be at the core of our engineering principles as we move forward
throughout this book, although you will see we are going to apply it to far
more locations than just network and API controls.

When working with AI-assisted development, the principle of _verify before_
_trust_ becomes essential. AI systems can accelerate coding dramatically, but
they can also introduce subtle bugs, insecure patterns, or outright
hallucinations in the generated code. In practice, this means that every piece
of AI-generated code should be treated as untrusted until reviewed by a
human developer. I’ve taken to making a very explicit distinction between

AI generated code (unreviewed code), and _AI assisted code_ (AI generated
code that a human has reviewed and/or edited), when discussing the two.
Code reviews should remain a mandatory step in the development process,
just as they are in traditional software engineering. Further, pushing unreviewed, AI-generated code on peers or into a pull request, should be
considered an anti-pattern or faux pas. That is to say, humans and especially
engineers should be producing AI assisted code whenever possible, and
should actively advise colleagues against purely AI generated code. I find
that AI generated code, if left unchecked, becomes increasingly hard for
humans to contribute to over time. Engineers should take great care in
setting up any initial structure, harnesses, and test suites for code that will
be heavily AI assisted. In this way, engineers can add structure and
guardrails (in the form of linting, unit, smoke, integration, and systems
tests), to help ensure AI assisted code confirms to the standards of the
project.

It is also important to treat AI tools as part of the software supply chain.
The models, associated infrastructure, prompts, generated code, and
external libraries used by AI systems can all introduce new risks.
Maintaining auditability, logging AI-assisted changes, and enforcing secure
coding standards helps ensure that convenience does not come at the cost of
security. Ultimately, AI should function as an assistant to developers, not as
an autonomous authority pushing production code. AI can generate so much
code that it can quickly dwarf the ability for developers to review if they
aren’t careful, and they will lose the deep understanding of their software
functions. It becomes increasingly hard to engineer a competent and secure
system if you don’t understand the architected technology, actions, control
flow, or permission boundaries. Because of these challenges, I strongly
recommend using _Plan files_, a git-like versioning architecture, and a staged
approach whenever approaching an AI-generated code project. Plan files
are simple markdown files that humans can review, and give the model
something to anchor on when developing. It can come back to its static plan
file to reference a human approved architecture before each change.
Further, the changes should be small enough that each stage of the plan file

only introduces single features at a time, and those changes can be reviewed
in a separate branch before any of the changes land.

The risk is real, AI-generated code may include the wrong libraries,
improper input validation, weak authentication logic, or patterns that violate
internal corporate security policies. Developers should review the code not
only for correctness but also for security posture, architectural alignment,
and long-term maintainability. The goal is to leverage AI for speed while
ensuring human oversight maintains the integrity of the system and the
engineer’s design patterns.

One important control in AI-assisted software development is maintaining
clear logging and traceability for changes that were generated or materially
influenced by AI. In traditional engineering, reviewers can usually infer
intent from commit history, comments, tickets, and design discussions. With
AI-generated code, however, that intent can be harder to reconstruct unless
teams deliberately preserve the context in which the code was produced.
For that reason, organizations should consider treating AI assistance as part
of the development record. The purpose is not only accountability, but also
incident response and maintainability. If a defect or vulnerability is later
discovered, the organization should be able to trace whether it originated in
the prompt, the generated output, or the human modifications that followed.
They should be reviewed to ensure they do not contain secrets, sensitive
internal context, or instructions that encourage insecure behavior. A useful
practice is to note in the commit message, pull request, or accompanying
documentation that AI was used, include any prompts used, and capture any
important constraints or assumptions. Another idea is to have the AI
explicitly mark with comments in the code any functions it touched or
wrote. One of the best developer traits I’ve seen is leaving small comments
about functions about the providence of the code, such as if the developer
took an implementation from StackOverflow, they will often include the
link to the question in the code. This is a similar technique for tracking AI’s
influence on a body of code. This traceability can help establish
provenance, support incident response, and make it easier to audit the code

later. Another way large organizations can audit or monitor LLM usage is
through a proxy gateway, but we will cover more on these techniques later.

You should continue using traditional security tools wherever possible,
especially when reviewing AI-generated code. Static analysis tools,
dependency scanning, and security linters can provide automated checks
that help identify vulnerabilities introduced during generation. Monitoring
for insecure patterns, such as unsafe deserialization, injection
vulnerabilities, or improper credential handling, should be part of the
standard review workflow. You should also be running secrets detection
code on the code bases, to make sure you aren’t committing secrets directly
to repos. Setting these systems up will catch vulnerabilities introduced by
AI assisted code. Models are inherently slower than the state-of-the-art,
they need to take time to train on data and be released, so they will
regularly suggest older, out-dated, potentially vulnerable versions of
libraries. Depending on the data and credentials provided, they will also
happily hardcode credentials to re-use them later. This is why not only
setting up a good architecture is critical (like setting them up with properly
secured creds in a credential store), but we need to double check their work
(with automated scanners) for these mistakes regardless.

One effective strategy when working with AI-assisted code is applying the
principles of Test-Driven Development (TDD). By defining tests and
constraints before code is written, or before the AI generates code, you
establish clear expectations that the implementation must satisfy. This can
act as a powerful guardrail, forcing the generated code to conform to
predefined behaviors, security requirements, and functional constraints.
TDD can also help reduce the risk of reward hacking by making the tests
independent of the generated implementation. If the tests are out-of-band of
the scope that the model has access to, the AI must produce code that
satisfies them rather than generating both the implementation and the
validation logic in a way that conveniently passes. When used correctly, this
approach turns tests into security and reliability constraints that guide the
AI toward safer outputs. If you struggle at writing tests you can have a
different model or system to help write automated tests. The trick is to keep

the tests independent from the code actively being worked on. Tests can be
implemented as a series of github actions or an external CI/CD machine, in
this way they can be removed from the development environment and direct
model access. This can help greatly with reviewing automatically generated
code, but you also have to review the tests and results to make sure the
agent isn’t rewarded for hacking the outcomes.

In agentic AI systems, the principle of “verify before trust” often takes the
form of human-in-the-loop (HITL) controls. Agents like Claude Code often
operate in a more real time manner, querying systems, modifying data,
executing workflows, or interacting with external services. Because these
actions can have immediate and real-world consequences, it is important to
introduce checkpoints where a human reviews or approves the agent’s
actions before critical operations occur. Human oversight acts as a
safeguard against hallucinations, misinterpretations of instructions, or
manipulation through adversarial inputs. Claude Code’s harness natively
introduces these HITL controls as part of their default tool suite, but it gives
the user the option to turn them on, with auto-editing and auto-execution
(simply called ‘auto’) modes. I don’t think auto-editing is the worst thing in
my opinion, so long as repo is properly scoped and using a git-like SVN, as
you should have backups and diffs of anything being worked on. I do think
auto-execution mode is dangerous for several reasons. While Claude Code
has an invisible prompt review layer here, so much crazy stuff can still get
through that model filter. I’ve seen agents ‘rm -rf’ large parts of the
filesystem, create https disasters, loop endlessly for hours (eating funds),
and take services offline unnecessarily, to name a few examples. God forbid
you are doing something like reverse-engineering, and the agent decides to
execute the malware on your localhost. All this is to say that ‘auto’ mode
can be very dangerous, especially if you are trying to implement it yourself
rather than using something like Claude Code (which already has a great
framework and hidden guardrails built in and still makes mistakes).

Human-in-the-loop controls are particularly valuable when agents interact
with sensitive systems or high-impact operations. For example, an agent
that drafts an email may not require approval, but an agent that modifies a

production database, deploys code, accesses confidential records, exploits a
live system, or sends external communications should typically require
human validation before executing those actions. By defining clear
thresholds for when human review is required, in policy, a markdown
document, or tiered agent controls, applications can balance the efficiency
benefits of automation with the safety provided by human judgment. This
can be made even more effective by writing your own tools that gate the
actions or call the model on behalf of the user, moving away from generic
agent harness towards specific tools.

Another effective pattern is tiered autonomy, where agents are allowed to
operate independently for low-risk tasks but must escalate higher-risk
decisions to a human reviewer. This model treats human oversight as a
governance layer rather than a constant bottleneck. The agent can still
accelerate low-risk workflows, but the system ensures that potentially
dangerous or irreversible actions are examined by a person who can
recognize context, intent, and broader consequences that automated systems
might miss. Human-in-the-loop processes can also serve as a learning
mechanism. When humans review agent actions, approving, rejecting, or
modifying them, the organization gains valuable insight into where the
agent performs well and where it struggles. Over time, these human
feedback loops can inform improvements to prompts, guardrails, policies,
and system design. In this sense, human oversight is not just a safety
measure; it is also a practical way to continuously refine the reliability and
security of agentic systems.

We will revisit these various human-in-the-loops designs later in the book.

### **Tool Use & Agency**

One of the most common patterns I see when it comes to builders, from
non-developers to the most hardcore computer scientists, is they just want
to give the agents or models full access and let it do its thing. This is
honestly the most common security pitfall I observe day-to-day when
people are using AI systems. I think the dopamine rush of AI-assisted
development short circuits some of our decision making or overtakes deep

work patterns. It reminds me of the book Deep Work, by Karl Newport.
Often, when we are using AI systems, we are caught in high-level, shallow
work. We throw quick prompts into a chat interface and are rewarded with
tons of output to sift through, some of it containing gold. But to engineer
systems that have hard permissions, or counter real threats, we must work
outside of the AI systems we are building, to put the right walls in place.
Sometimes we can use AI to assist us in this, but often this is the deep work
our brain wants to shortcut, or worse, we put false controls in place at the
prompt and model layers.

**Separation of Duties**

When we begin to design agentic systems, it’s best practice in my opinion
to keep the ‘agentic’ part as small, and focused as possible. This means we
should make the agentic portion or tool as focused on a single thing as
possible. Kind of like the linux philosophy KISS, or keep it super simple.
The more focused on a single activity our model or tool is, the more
performant it will be, and the easier it will be to apply a single identity, and
the principle of least privilege on top of that.

Even if our model is supposed to do multiple things, which are seemingly
inter-related, such as:

Stock a stores shelves with items people want

Run a profitable business (balance business reality with customer
demand)

It may run into issues when trying to interpret user intent. Let’s look at the
example of Anthropic’s Claudius. After several iterations of being taken
advantage of, Anthropic decided to add an abstraction layer over Claudius
to manage its business decisions (SeeMoreCash).

In this way they were able to use agents to watchdog each other and create a
system of accountability and more narrowly focused agents / tasks.
Personally I would have automated even more of the agent tasks, such
allowing them to only use an API with pre-authenticated items. Or having

the self checkout systems use hardcoded limits such that a model couldn’t
alter a price beyond a reasonable limit (say the purchase price), without a
human override.

There are also many lessons we can borrow directly from the microservice
world. Alongside the Principle of Least Privilege, we have a guiding sister
principle: Separation of Duties. This aligns well with the Linux philosophy
of small, purpose-built tools. If a tool needs to perform another major duty,
it may be better to separate those tools and explicitly manage permissions
between them. This enforces compartmentalization and keeps the scope of
failures or vulnerabilities smaller.

**An easier approach for researchers**

Start locked down then pivot. This leads to a practical approach: start
locked down, then open up the controls you want individually.

Often, it’s difficult to engineer a secure system from the ground up. If a
project is small enough, it can be better to start from a secure baseline and
gradually open only the permissions that are needed. This helps prevent
accidental misconfiguration or over-privileged actions. That said, this
approach has tradeoffs—permissions can accumulate over time and become
harder to track.

Still, adding permissions gradually helps us understand:

What each permission allows and how it expands functionality

Where the boundary between tools exists

Whether each control matches its purpose and isn’t exposed by
default

That each action is individually evaluated

This approach naturally aligns with several core principles. It defaults to
fail-closed, allows iterative design, and forces us to consciously apply
controls to each action. As we add permissions, we should continuously
review the system and ensure each function is intentionally designed.

Default-deny > incremental enablement > continuous auditing

Instead of starting from the locked down position, let’s look at some
frameworks for building a secure system from the ground up.

[One example is from the "ALARA for Agents" paper. ALARA stands for](https://gist.science/paper/2603.20380)
As Low as Reasonably Achievable. The idea emphasizes that projects
should define their tool scope, context, and permissions explicitly within a
structured project definition. The key difference from current agent
approaches (like SKILLS from Anthropic, which uses mostly free-form
markdown) is that ALARA enforces structure for agents.

In line with the other research we’ve already seen, by tightly implementing
systems like this, we not only gain security benefits but also noticeable
performance improvements. The authors implement ALARA in a system
called npcsh and evaluate it across 22 local language models (ranging from
0.6B to 35B parameters) on 115 tasks involving file operations, web search,
[scripting, and multi-agent coordination.](https://github.com/NPC-Worldwide/npcsh)

Their results show that structuring agent systems through strict tool scoping
and modular organization improves performance, especially for smaller
models. Adding structured overhead also reduces failure modes like context
overload and coordination breakdowns by giving agents stable anchors
(files and structure) to return to as context grows. The study further shows
that limiting tool access improves both accuracy and safety by decomposing
agents into specialized roles with minimal context. This structured approach
actually improves scalability and collaboration between agents, as opposed
to trying to make megalithic agents. The ALARA structure is pretty based
in terms of concepts and models for laying out an AI project, if not
practically at least conceptually. Let’s look at an overview of the structure
below:

my-agent-project/
│
├── context/
│ ├── main.yaml <1>
│ ├── research_team.yaml <2>

│ └── writing_team.yaml
│
├── agents/ <1>
│ ├── researcher.yaml
│ ├── writer.yaml
│ ├── reviewer.yaml
│ └── orchestrator.yaml
│
├── tools/ <4>
│ ├── base/
│ │ ├── python.yaml
│ │ ├── chat.yaml
│ │ ├── shell.yaml
│ │ └── web_search.yaml
│ │
│ ├── composite/
│ │ ├── react.yaml <5>
│ │ ├── delegate.yaml <6>
│ │ └── computer_use.yaml <7>
│ │
│ └── custom/
│ ├── summarize.yaml
│ └── write_report.yaml
│
├── workflows/
│ ├── report_pipeline.yaml
│ └── research_flow.yaml
│
├── data/
│ ├── inputs/
│ └── outputs/
│
├── config/
│ ├── models.yaml <8>
│ └── settings.yaml
│
└── run.py / cli.sh <9>

<1> Top-level team definition (orchestrator, teams)

<2> Sub-team context (optional)

<3> NPC files in the paper

<4> Jinxes in the paper

<5> chat + python

<6> chat + shell

<7> chat + screenshot + shell

<8> model configs per agent

<9> entry point (npcsh equivalent)

Looking at the ALARA structure we can see a clear separation of duties.
Our goal should be our best to separate the AI model calls from the
workflows and the actual execution of the tasks. We want to avoid having a
model shell directly out, and instead call known, deterministic tools.

The tools and frameworks already exist to pull a lot of this apart and apply
traditional automation, or layers where applicable. We also have strong
guiding principles. The real challenge is avoiding the trap of the easy path
and instead engineer systems that are resilient to model manipulation
through out-of-band controls.

### **Threat Modeling and Red Teaming**

One of the most effective ways to improve the resilience of AI systems is to
red team your own solutions. Instead of waiting for real attackers to
discover weaknesses, proactively attempt to uncover failure cases before
they occur. The goal here is to understand the various ways the application
could fail or be abused though different attacks or use cases. By exploring
these scenarios early, teams can design controls, guardrails, and monitoring
strategies that reduce the likelihood of those events becoming real incidents.

This attacker mindset closely aligns with the long-standing security practice
of threat modeling. At its core, threat modeling is an exercise in playing
devil’s advocate with your own work. Rather than assuming a system will
behave as intended, you deliberately ask how it could go wrong. What
assumptions could fail? What unintended behaviors might emerge? By
challenging your own design decisions in this way, you begin to surface the
weaknesses that an adversary might eventually discover. It can also help to
bring an outsider in for this type of analysis, we often have unconscious
biases with our own work that others will not have.

A simple way to start threat modeling, especially for smaller teams or
researchers, is through structured brainstorming. Ask questions such as:

How could my application be intentionally attacked?

How could it be unintentionally misused or harmed?

Who are the individuals or groups that might target it?

What motivations might they have?

What techniques might they use?

How could my system fail or break?

What would happen if the system was inaccessible?

What impact could attackers have if they hacked the system and
got root control?

You should also consider failure modes that have nothing to do with
attackers at all, systems can fail through design flaws, operational mistakes,
or unexpected interactions with other components. While malicious
attackers open up a plethora of new outcomes, your most common
scenarios will likely be through regular use.

Once potential threats are identified, the next step is to evaluate them in
terms of likelihood and impact. This process is often called risk analysis
and comes from the field of actuarial sciences. Their formula for calculating
risk is [Risk = Impact x Liklihood]. Some scenarios may be highly unlikely
but catastrophic if they occur, while others may be frequent but relatively
minor. By considering both the probability of an event and the severity of
its consequences, you can begin to estimate the risk each scenario presents.
This process allows teams to prioritize their efforts, focusing first on the
risks that pose the greatest danger to the system or the organization. If this
seems completely foreign, there is a fantastic book on this subject called
_How to Measure Anything in Cybersecurity Risk_ by Douglas Hubbard that
shows exactly how to quantify these metrics.

For anyone interested in exploring this discipline further, Adam Shostack’s
book _Threat Modeling: Designing for Security_ is an excellent resource. In
it, Shostack outlines several structured methodologies for identifying
threats, including the well-known STRIDE model. STRIDE categorizes
threats into types such as spoofing, tampering, repudiation, information
disclosure, denial of service, and elevation of privilege, giving practitioners
a systematic way to analyze how an application might be attacked. I
personally still prefer the brainstorming approach, and if you were still
looking for a more systematic way to go about that, I recommend my friend
[Benedek Szabó’s Bsides presentation Pocket Threat Modeling.](https://www.youtube.com/watch?v=Le5pvynaaB)

Organizations can also implement threat modeling through tabletop
exercises. In these exercises, teams walk through hypothetical failure or
attack scenarios together, such as an AI model being manipulated by
malicious prompts or sensitive data being exposed through an automated
workflow. By simulating incidents and discussing how the organization
would respond, teams can test both their assumptions and their response
plans. Tabletop exercises often reveal gaps in processes, communication, or
tooling that might otherwise remain hidden until a real incident occurs. This
is a great way to apply threat modeling to a specific threat scenario.

Using techniques such as red teaming, threat modeling, and scenario
exercises, can help you proactively think about security risks and new
controls. Using these techniques can shift the security issues left by
identifying risks and mitigating them before they become real-world
incidents.

### **Lethal Trifecta**

As a shortcut to normal red teaming, some people have started calling a
certain mix of properties and access the _Lethal Trifecta_ or a recipe for a
security incident in the making. The Lethal Trifecta was first coined by
[Simon Willson, where he proposes tools or agents with the following](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
characteristics can be easily manipulated by external threats to access your
private data. While not every system that exhibits these traits will inevitably
lead to compromise, the framework provides a useful mental model for

evaluating risk in agentic systems. The trifecta describes a situation in
which an AI system simultaneously has access to private or sensitive data,
is exposed to untrusted or attacker-controlled content, and possesses the
ability to communicate externally in ways that could transmit that data
outside the system. When these three conditions coexist, an attacker may be
able to manipulate the model through crafted inputs and ultimately extract
sensitive information.

Let’s break down those properties a little more. The three components of
the Lethal Trifecta are:

_Access to private data_

Many AI agents are granted the ability to retrieve internal
documents, query databases, or interact with personal and
organizational information in order to function effectively.
When assessing this capability, it is important to consider
what kinds of data the system can access, such as secrets, PII,
proprietary information, or other sensitive records, and who
could ultimately be exposed to it. A crucial part of threat
modeling this system would be naively asking whether
every user interacting with the system should be able to see
the data it can retrieve. This is exactly where you should
double check your access controls and always explicitly
verify.

_Exposure to untrusted input_

This refers to any pathway through which attackercontrolled input, whether text, images, files, or web content,
can reach the model. If malicious instructions can be
embedded in that content, the model may be influenced in
unintended ways. This is yet another anchor on the principle
of untrusted input.

_The ability to communicate externally_

If the system can send messages, call external APIs, write
files, or otherwise transmit information outside its
environment, a successful manipulation could cause it to
leak sensitive data. In security terminology this is often
referred to as data exfiltration, though the core risk is simply
that private information could be transmitted beyond the
intended trust boundary of the system. This could be as
simple as a chat interface that the model responds to.

## **Summary**

If you’ve been in security long enough, you’ve watched the same fights
play out in different arenas. The names change throughout technologies, for
example SQL injection looks a lot like prompt injection under the current
context. But the underlying dynamics stay remarkably consistent; untrusted
input being used to subvert backend systems and control logic. Chapter 1 is
about building up those older mental models in your brain, as we are going
to rely on them in future sections.

We started by revisiting the fundamentals as both a history lesson and to
prepare the reader with a mental toolkit. Traditional information security
issues such as untrusted input, access controls, defense in depth, logging,
and secure failure design are still effective concepts we can apply to modern
agentic systems. The reason problem-sets like broken access controls have
sat at or near the top of OWASP’s vulnerability list for over two decades is
because these are ubiquitous security problems across new technologies.
Granted, there are a lot of genuinely new and interesting problems in this
new technology space. The probabilistic nature of these systems isn’t a bug
to be patched, it’s intentionally designed in, and it breaks a lot of
assumptions that traditional software engineering is built on.

Querying LLMs isn’t the same thing as making a traditional function call.
You’re not invoking logic, you’re querying a statistical and dynamic
distribution. Not only that, but that distribution can be manipulated at
multiple parts in its supply chain. From there we took a look at prompt

management as a logging and summarization effort. This was insightful in
terms of how context windows behave under pressure, and where the real
security failures happen when agents start touching the world. We talk
about saving your prompts like source code, because they are, they’re your
original intent and the most immediate interpretation of that by the LLM.
Treating them as throwaway chat history is a mistake that’ll haunt you later
in debugging and incident response. We dug into context windows and
memory architecture, where the lesson is also clear: more context isn’t
always better context. Structure beats size every time.

And we cover tool use and agency, where the biggest security failure I see
across the industry isn’t a novel attack vector, it’s developers handing
agents the keys to the kingdom because the demo was impressive. Least
privilege principles feel obvious until you watch someone hand an agent
unrestricted filesystem access because sandboxing feels like friction. In
their current state, these frontier agentic systems are just a little too
unhinged to let run for long periods of time with too much access.
Eventually their finite context window catches up to them, they lose the
plot, and do something wildly stupid.

The final section is where traditional security theory and AI behavior
collide. Planning is an entire NIST control family for a reason, it catches
vulnerabilities before they’re code. Separation of duties and the principle of
least privilege, lessons we learned the hard way in multiple industries, apply
even more when your executor is a probabilistic (potentially hallucinatory)
model. Code reviews become even more important. Engineers should be
producing AI assisted code not AI generated code (read slop). Threat
modeling and red teaming your own AI systems before an attacker does is
the shift-left play that planning often presents in a formal manner.

Finally, we covered a few shortcut models. From the locked down user
approach to the Lethal Trifecta. The locked down user approach lets
researchers quickly prototype a solution in a secure way, without having to
go through all of the rigor of building a secure solution from the ground up.
And the Lethal Trifecta, coined by Simon Willison, gives us a shortcut in
terms of threat modeling: if your agent can access private data, is exposed

to untrusted input, and can communicate externally, you’ve got the
preconditions for a serious incident. Not every system with those properties
will blow up, but you’d better be threat modeling like one will. The bottom
line is this: the hard part of AI security isn’t identifying new attack classes.
It’s having the discipline to apply what we already know to systems that
feel new enough to justify skipping the fundamentals.

1 Naval Safety Command. “What is Defense-in-Depth?” May 2023.
_https://navalsafetycommand.navy.mil/Portals/100/Documents/Defense-in-_
_Depth%20Info%20Paper.pdf_

2 Liu et al., “Lost in the Middle: How Language Models Use Long Contexts” (2023).
_[https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)_

3 Show Your Work: Scratchpads for Intermediate Computation with Language Models (2021) _[https://arxiv.org/abs/2112.00114](https://arxiv.org/abs/2112.00114)_

4 John Kindervang, et al. No More Chewy Centers: The Zero Trust Model Of Information
Security _https://www.forrester.com/report/No-More-Chewy-Centers-The-Zero-Trust-Model-Of-_
_Information-Security/RES56682_

**About the Authors**

Dan Borges is a seasoned security leader and former Head of Security
Engineering at Scale AI, where he helped design and implement secure,
scalable solutions across the organization. With a career spanning security
consulting, enterprise engineering, and community leadership, Dan has built
a reputation for advancing practical security at scale. Before joining Scale
AI, Dan held key roles at premier incident response and threat intelligence
firms including Mandiant and CrowdStrike, where he worked on highprofile investigations and defensive strategy. He also contributed to security
engineering and incident response efforts at Bay Area technology leaders
such as Uber, helping mature security practices inside fast-moving, highgrowth environments. Dan is the author of Adversarial Cybersecurity, a
work that pushes the industry toward more realistic, offense-informed
defense strategies. Today, he focuses on building security programs that
balance technical depth with business reality. He partners with engineering
and executive leadership to translate adversarial risk into clear, actionable
strategy, ensuring that security is not a blocker to innovation, but a force
multiplier for resilient growth.

David Campbell is Head of AI Security at Scale AI, where he architects and
leads some of the most advanced AI red teaming and resilience programs in
the world. A two-decade veteran of Silicon Valley, David built his career at
the intersection of infrastructure, security, and developer experience before
becoming one of the industries most trusted voices on AI risk. He pioneered
Discovery, one of the first and largest large-scale AI Red Teaming
platforms deployed across governments and Fortune 100 companies. Before
Scale AI, David shaped platform security and engineering culture at Uber,
DoorDash, and Nest Labs, where he built systems and practices that scaled
to thousands of engineers. Across his career, he has been recognized for
turning fragmented engineering environments into resilient, high-trust,
high-standards organizations. David’s expertise is sought globally. He has
briefed the U.S. Congress, the White House, U.K. Parliament, NATO,
Korea AISI, UK AISI, Qatar NCSA, and senior public-sector leaders on AI
risk, misuse, and national resilience. He is a founding member of OWASP

AIVSS and a core member of AIUC-1, the industry consortium defining
how enterprises evaluate, insure, and underwrite AI systems. He also
contributes to collaborative defense efforts such as CISA’s JCDC.AI series
on AI-driven cyber threats. David helps companies bridge the gap between
rapid AI innovation and enterprise-grade safety. His mission is simple: align
technology with the future of the business, and ensure that AI systems are
deployed responsibly, securely, and with confidence.
