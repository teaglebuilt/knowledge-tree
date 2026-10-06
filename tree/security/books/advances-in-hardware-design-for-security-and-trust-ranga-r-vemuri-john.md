---
title: Advances in Hardware Design for Security and Trust (Ranga R. Vemuri John M.
  Emmert)
source: books/pdf/Advances in Hardware Design for Security and Trust (Ranga R. Vemuri  John
  M. Emmert) (z-library.sk, 1lib.sk, z-lib.sk).pdf
source_type: book
source_hash: 87ff927b0fd93d62615b42a8b68d42eacbaf2d015e32e8005ecfcd05b1de62e1
tags:
- security
- book
extracted: '2026-10-05'
---

## Advances in Hardware Design for Security and Trust

This book addresses various electronics supply-chain vulnerabilities, attack methods
that exploit these vulnerabilities, and design techniques to mitigate the vulnerabilities while defending against the attacks. This book covers the entire spectrum of
electronic hardware design including integrated circuits, embedded systems, and design automation tools.

Advances in Hardware Design for Security and Trust offers self-contained tutorials
within each chapter, as well as a presentation of recent advances. The relevance of
each method in the context of the overall design and fabrication process is clearly
articulated. Both qualitative analysis and quantitative experimental results to evaluate the significance of methods are presented. Both side-channel methods as well as
front-channel techniques are covered. The authors emphasize methods that are ready
for technology transition and commercialization.

This book is intended for both researchers and industry practitioners. They will benefit from the tutorial style exposition of the topics along with advanced research
results and emerging directions.

Computer Hardware Security and Correctness

Advances in Hardware Design for Security and Trust
Edited by Ranga R. Vemuri and John M. Emmert

[For more information about this series, please visit: www.routledge.com/Computer-](https://www.routledge.com/Computer-Hardware-Security-and-Correctness/book-series/CHSC)
[Hardware-Security-and-Correctness/book-series/CHSC](https://www.routledge.com/Computer-Hardware-Security-and-Correctness/book-series/CHSC)

## Advances in Hardware Design for Security and Trust

##### Edited by Ranga R. Vemuri and John M. Emmert

Designed cover image: © Getty Images

First published 2026
by CRC Press
2385 NW Executive Center Drive, Suite 320, Boca Raton FL 33431

and by CRC Press
4 Park Square, Milton Park, Abingdon, Oxon, OX14 4RN

CRC Press is an imprint of Taylor & Francis Group, LLC

© 2026 selection and editorial matter, Ranga R. Vemuri and John M. Emmert; individual chapters, the
contributors

Reasonable efforts have been made to publish reliable data and information, but the author and publisher
cannot assume responsibility for the validity of all materials or the consequences of their use. The authors
and publishers have attempted to trace the copyright holders of all material reproduced in this publication
and apologize to copyright holders if permission to publish in this form has not been obtained. If any
copyright material has not been acknowledged please write and let us know so we may rectify in any
future reprint.

Except as permitted under U.S. Copyright Law, no part of this book may be reprinted, reproduced, transmitted, or utilized in any form by any electronic, mechanical, or other means, now known or hereafter
invented, including photocopying, microfilming, and recording, or in any information storage or retrieval
system, without written permission from the publishers.

For permission to photocopy or use material electronically from this work, access [www.copyright.com](https://www.copyright.com)
or contact the Copyright Clearance Center, Inc. (CCC), 222 Rosewood Drive, Danvers, MA 01923, 978[750-8400. For works that are not available on CCC please contact mpkbookspermissions@tandf.co.uk](mailto:mpkbookspermissions@tandf.co.uk)

Trademark notice: Product or corporate names may be trademarks or registered trademarks and are used
only for identification and explanation without intent to infringe.

ISBN: 978-1-032-84042-0 (hbk)
ISBN: 978-1-032-84044-4 (pbk)
ISBN: 978-1-003-51094-9 (ebk)

[DOI: 10.1201/9781003510949](https://doi.org/10.1201/9781003510949)

Typeset in Nimbus font

by KnowledgeWorks Global Ltd.

#### _Dedication_

###### To the memory of Dr. S.L.N.S. Sarath Kumar, for his affection, compassion, and curiosity. – Ranga Vemuri and To my wife, Jorie, and my children, for their unconditional love and support. – Marty Emmert

### Contents

Preface......................................................................................................................xi

About the editors...................................................................................................xiii

Contributors ...........................................................................................................xv

Chapter 1 Introduction .....................................................................................1

Ranga R. Vemuri and John M. Emmert

Chapter 2 Hardware Security In The Consumer Technology Industry............7

Paul M. Simon

Chapter 3 A Commercial EDA Perspective on Hardware Security, Safety,
and Trust........................................................................................22

P. Len Orlando III, Lang Lin, and Norman Chang

Chapter 4 Machine Learning Techniques for Detecting Hardware Trojans in
ASIC Designs................................................................................50

Kevin Immanuel Gubbi, Banafsheh Saber Latibari, Setareh
Rafatirad, Avesta Sasan, Soheil Salehi, and Houman Homayoun

Chapter 5 Next-Generation Semiconductor Reverse Engineering: Laser
Delayering, Correlative Imaging, and Cloud-Enabled Image
Analysis Techniques......................................................................74

Hongbin Choi, Matthew Maniscalco, Adrian Phoulady, Alexander Blagojevic, Toni Moore, Mohammad Taghi Mohammadi
Anaei, Todor Bliznakov, Marcus Emanuel, Parisa Mahyari,
Nichoals May, Sina Shahbazmohamadi, and Pouya Tavousi

**vii**

**viii** Contents

Chapter 6 Synthesis of Polymorphic Circuits for Hardware Security .........110

Haimanti Chakraborty and Ranga Vemuri

Chapter 7 Design Obfuscation and Performance-Locking Solutions for
Mixed-Signal, Analog and RF ICs ..............................................134

Priyanshu Mishra, Andrew Marshall, and
Yiorgos Makris

Chapter 8 On-Chip Integrity, Reliability, and Aging Assurance Techniques
for ICs..........................................................................................170

Manoj Yasaswi Vutukuru and Rashmi Jha

Chapter 9 Deep Learning Side-Channel Attacks: Challenges and
Opportunities...............................................................................193

Logan Reichling, Mabon Ninan, Boyang Wang, and John M. Emmert

Chapter 10 Side-Channel Attack Avoidance and Mitigation Through
Asynchronous Digital Design......................................................217

John M. Emmert and Anvesh Perumalla

Chapter 11 Is ARM’s TrustZone Trustable for Confidentiality Protection?..240

Tianhong Xu and Yunsi Fei

Chapter 12 Security Verification for Next-Generation SoCs .........................267

Samit Shahnawaz Miftah, Amisha Srivastava, Yiorgos Makris,
and Kanad Basu

Chapter 13 Cloud FPGA Accelerator Fingerprinting Using Communication
Side Channels..............................................................................302

Chongzhou Fang, Ning Miao, Han Wang, Jiacheng Zhou, Tyler
Sheaves, John M. Emmert, Avesta Sasan, and Houman Homayoun

Contents **ix**

Chapter 14 Enterprise Risk Management of Electronics and Computing
Device Supply Chains .................................................................330

Zachary A. Collier and James H. Lambert

Index......................................................................................................................349

### Preface

This is a time of rapidly changing technology. Along with major improvements to
the existing technology, there is a rapidly growing increase in cyber vulnerabilities
and attacks. A less leveraged but perhaps even more vulnerable weakness is the integrated circuit hardware and processors that run all of the software. Software viruses
can bring down infrastructures for hours, and even days. Compared to hardware, it
is relatively simple to update the code and firmware to eliminate software viruses.
Much more time consuming and difficult is the process of addressing a hardware attack like a Trojan circuit embedded in an integrated circuit by a malicious individual
or entity during circuit fabrication. While hardware attacks are rarer than software
attacks, they can be much more expensive and catastrophic. They can bring down
infrastructures for weeks or even months. The fixes are not nearly as simple and
may even result in entire chip set replacement. Hardware attacks in the supply chain
(whether the hardware is being shipped or controlling the shipping process) hold the
potential to ruin entire economies.

We are even more vulnerable to hardware attacks given the majority of integrated
circuits are fabricated outside of the United States. In addition, hardware designs are
often composed using modules (cores) which are in turn designed outside the country. The recent approach to addressing hardware vulnerabilities is to bring major
integrated circuit manufacturing back “on shore.” The result: The Chips and Science
Act. However, this is arguably a temporary, unsustainable approach. Given the cost
of bringing up a new integrated circuit fabrication node, it is not a viable approach
for the government to subsidize the industry, long term. Ideally, we should be able to
fabricate chips anywhere, and be assured that the systems produced are secure and
trustworthy. The methods presented in this book support this goal. These are solutions to some of the problems arising in improving hardware and embedded systems
security, assurance, and trust.

The majority of techniques presented in this volume were developed through the
National Science Foundation (NSF) Center for Hardware and Embedded Systems
Security and Trust (CHEST) Industry/University Collaborative Research Center (IUCRC). The mission of this center is to address the research challenges that industry
faces in the design, protection, and resilience of hardware, develop solutions to mitigate the security vulnerabilities associated with electronic hardware and embedded
systems, and train the much-needed workforce for government and industry. Since its
inception in 2019, the NSF CHEST IUCRC has supported over 120 research projects
involving over 200 faculty and graduate students at the University of Cincinnati,
the University of Texas at Dallas, the University of California, Davis, Northeastern
University, the University of Virginia, and the University of Connecticut. There is
currently no single solution to protect remotely fabricated hardware and assure the
trustworthiness of the hardware supply chain, but hopefully the reader can apply the
techniques presented here to provide a greater degree of assurance.

**xi**

### About the editors

Ranga Vemuri is a Professor in Electrical and Computer Engineering and directs
the Digital Design Environments Lab at the University of Cincinnati where served
since 1989. His interests are in Hardware Trust, Correctness and Security, VLSI Design and Design Automation, and Reconfigurable Computing. His research has been
funded by AFRL, DAGSI, DARPA, NSF, State of Ohio and various industries. He
and his students have published over 300 papers and have received several Best Paper Awards and nominations. Prof. Vemuri co-authored two books and graduated 42
PhD and over 90 MS students. He served on the program committees of numerous
international conferences and served as an Associate Editor of the IEEE Transactions
on VLSI and as a Guest Editor of the IEEE Computer.

John Emmert has been an Electrical Engineering Professor since 1999. His research
has been funded by AFRL, DARPA, NSF, the US Congress, the State of Ohio and
various industrial companies, and he currently has eight full and three provisional
US patents, all related to integrated circuit design. He is the Director of the NSF
Center for Hardware and Embedded Systems Security and Trust (CHEST) I/UCRC.
He also served in the United States Air Force from 1989-2015. In the Air Force he
held positions from UAV pilot to reserve wing commander, and after 26 years of
service, he retired as a Colonel. He has been awarded the Air Force Legion of Merit
and five Meritorious Service Medals.

**xiii**

### Contributors

Mohammad Taghi Mohammadi Anaei

University of Connecticut, Mansfield,

CT, USA

Kanad Basu
University of Texas, Dallas, TX, USA

Alexander Blagojevic

University of Connecticut, Mansfield,

CT, USA

Haimanti Chakraborty

University of Cincinnati, Cincinnati,

OH, USA

Norman Chang
Ansys, San Jose, CA, USA

Hongbin Choi

University of Connecticut, Mansfield,

CT, USA

Zachary A. Collier
Radford University, Radford, VA, USA

John Emmert
University of Cincinnati, Cincinnati,

OH, USA

Chongzhou Fang

University of California, Davis, Davis,

CA, USA

Yunsi Fei
Northeastern University, Chicago, IL,

USA

Kevin Immanuel Gubbi
University of California, Davis, CA,

USA

Houman Homayoun
University of California, Davis, Davis,

CA, USA

Rashmi Jha
University of Cincinnati, Cincinnati,

OH, USA

James H. Lambert
University of Virginia and

Commonwealth Center for Advanced
Logistics Systems, Charlottesville,
VA, USA

Banafsheh Saber Latibari
University of California, Davis, CA,

USA

Lang Lin
Ansys, San Jose, CA, USA

Parisa Mahyari
University of Connecticut, Mansfield,

CT, USA

Yiorgos Makris
University of Texas, Dallas, TX, USA

Matthew Maniscalco
University of Connecticut, Mansfield,

CT, USA

Andrew Marshall
University of Texas, Dallas, TX, USA

**xv**

**xvi** Contributors

Nichoals May
University of Connecticut, Mansfield,

CT, USA

Ning Miao
University of California, Davis, Davis,

CA, USA

Samit Shahnawaz Miftah
University of Texas, Dallas, TX, USA

Priyanshu Mishra
University of Texas, Dallas, TX, USA

Toni Moore
University of Connecticut, Mansfield,

CT, USA

Mabon Ninan
University of Cincinnati, Cincinnati,

OH, USA

P. Len Orlando III
Ansys, San Jose, CA, USA

Anvesh Perumalla
University of Cincinnati, Cincinnati,

OH, USA

Adrian Phoulady
University of Connecticut, Mansfield,

CT, USA

Setareh Rafatirad
University of California, Davis, Davis,

CA, USA

Logan Reichling
University of Cincinnati, Cincinnati,

OH, USA

Soheil Salehi
University of Arizona, Tucson, AZ,

USA

Avesta Sasan
University of California, Davis, Davis,

CA, USA

Sina Shahbazmohamadi
University of Connecticut, Mansfield,

CT, USA

Tyler Sheaves
University of California, Davis, Davis,

CA, USA

Paul Simon
Amazon, Oakwood, OH, USA

Amisha Srivastava
University of Texas, Dallas, TX, USA

Pouya Tavousi
University of Connecticut, Mansfield,

CT, USA

Ranga Vemuri
University of Cincinnati, Cincinnati,

OH, USA

Manoj Yasaswi Vutukuru
University of Cincinnati, Cincinnati,

OH, USA

Boyang Wang
University of Cincinnati, Cincinnati,

OH, USA

Han Wang
Temple University, Philadelphia, PA,

USA

Tianhong Xu
Northeastern University, Chicago, IL,

USA

Jiacheng Zhou
University of California, Davis, Davis,

CA, USA

# 1 Introduction

Ranga R. Vemuri and John M. Emmert

**1.1** **ELECTRONICS LIFE CYCLE**

Life of an electronic system can be broadly divided into four stages: design, implementation, operation, and disposal. Figure 1.1 shows the typical life cycle of an
integrated circuit (IC). A design house commences the design process with a high
level specification. A model is written in a hardware description language such as
Verilog. A suitable EDA (electronic design automation) tool flow is used to generate mask layouts. Typical EDA flows include logic and layout synthesis, timing and
power analysis, and testability enhancement tools. Pre-designed modules obtained
from outside sources are integrated with the design to reduce design time. These
cores, often referred to as 3PIP (third-party intellectual property) cores, can be in
soft, firm, or hard forms. The design process ends with a mask layout, usually in the
GDSII format, which is sent to a foundry where the design is implemented in silicon.

The manufactured wafers are cut into dies, tested, and packaged. Packaged ICs
are used to build electronic systems, often in the form of one or more printed circuit boards assembled into a suitable chassis. These end products, usually supported
by multiple layers of software, are sold to target consumers, deployed, used, and
eventually discarded as electronic waste.

Discarded electronic parts could be recycled by unscrupulous scavengers and put
back into the supply chains. These counterfeit parts not only cause loss of revenue to
the legitimate producers of those parts but also pose a significant product longevity,
safety, and security risk to the consumers.

**Figure 1.1** Typical integrated circuit life cycle.

[DOI: 10.1201/9781003510949-1](https://doi.org/10.1201/9781003510949-1) **1**

**2** Advances in Hardware Design for Security and Trust

**1.2** **HARDWARE ATTACKS**

Multiple actors are involved in the life cycle of an electronics product. These actors
are often owned by multiple agents, dispersed across the world, and are influenced by
disparate; possibly competing; or even adversarial, political, geographical, and economical influences. In this context, a variety of threats that undermine the interests
of the legitimate producers or consumers of the electronic products have emerged.
Some of these threats are briefly summarized below:

1. Hardware Trojans: The term hardware trojan is used to refer to any change
made to the design at any stage with a malicious intent to cause harm to its
correct operation. Examples of such changes include nick of a wire in the
layout made at an untrusted foundry, addition of a small amount of logic
which when triggered leads to incorrect outputs, and insertion of a stealthy
module which leaks privileged data during operation via a primary output
port or a side channel.
2. Reverse Engineering: Attackers can attempt recover the specification from
the design at any level of abstraction. This includes attempts to reconstruct
the mask layout of an IC through a series of delayering, imaging, and image stitching steps, to obtain a gate-level design from a mask layout, and to
derive a register-transfer level (RTL) specification from a gate-level netlist.
Reverse-engineering attacks aim to steal the intellectual property (IP) with
the intent to reimplement the design or to understand its function. A legitimate purpose of reverse engineering is to repair or reimplement legacy
electronic systems whose design specifications may have been lost.
3. Counterfeiting: Counterfeiting refers to the sale of partly functional or
under-performing parts obtained from a foundry or of aged parts scavenged
from recycled electronics. Procurement and use of counterfeit parts is attractive due to their low pricing but poses serious threats to the functionality, longevity, and safety of the products built using those parts.
4. Overproduction and Overuse: An unscrupulous foundry may overproduce
a design and engage in unauthorized sales thereby causing loss of income
to the design house. A design house may overuse an IP core beyond the
purpose and number of copies for which it is licensed for.
5. Design Theft: A design, at any level of abstraction, may be stolen and the
thief may claim ownership rights to the design. For example, soft or hard
IP cores may be stolen by a design house and mask layouts may be stolen
by hacking into the servers of a design house.
6. Unauthorized Access and Use: A product may be stolen from a customer
and the thief may claim to be the rightful owner of the product. An attacker
may gain access to a hardware resource by exploiting a side-channel vulnerability.
7. Data Theft: Protected sensitive data such as a key may be stolen by an
attacker by breaking into the privilege mode or by mounting a side-channel
attack.

Introduction **3**

**1.3** **DESIGN FOR SECURITY AND TRUST**

Over the past two decades, a number of design methods have been developed to
defend against various attacks and improve the trustworthiness of electronic systems.
Some of these methods are summarized below:

1. Design Obfuscation: Incorporating features into the design which hide its
function from an attacker is referred to as design obfuscation. Logic encryption or logic locking is an obfuscation method which inserts a number of key
gates that are controlled by key inputs. The key inputs together constitute
the key port. Only when the correct key vector, known only to an authorized user, is applied, the function is unlocked; otherwise, the output vectors
are corrupted. This defeats attacks such as reverse engineering, unauthorized use, overproduction, etc. In layout camouflaging, dummy contacts are
added to the layout in such a way that the delayering process cannot distinguish between them and the legitimate contact. There are also parametric
locking methods which degrade the chip’s performance or power when an
incorrect key is applied.
2. Watermarking and Fingerprinting: Watermarking refers to the incorporation in the design of a secret feature known only to the producer to help
establish the producer’s ownership of the design. All instances (e.g., chips)
of the design would have the same watermark. A fingerprint is a similar secret feature which helps establish a consumer’s ownership of a copy of the
design. Hence, each instance (e.g., chip) of a design would have a unique
fingerprint. Watermarks and fingerprints help discourage IP piracy.
3. Side-Channel Defense: Side-channel attacks are based on measuring some
physical parameter while an electronic product is operating and correlating that measurement to the data being processed. For example, power attacks are based on exploiting data-dependent variations in the instantaneous
power draw. Preventing side-channel information leakage requires diminishing or eliminating the correlation between data and power by either incorporating features to randomize the power consumption, to draw constant
power, or mask the data being processed. Similar techniques could be used
to defend other side channels such as the electromagnetic emissions or heat
maps.
4. Metering, Monitoring, and Tracking: Metering refers to instrumentation
modules incorporated on-chip to measure some physical parameter. Monitoring refers to the addition of logic to determine if a functional or parametric condition is satisfied during run time. For example, aging meters can be
incorporated to determine how long a chip has been in use and thwart recycling and aging attacks. Functional monitoring for critical security aspects
can be used to detect trojan activity and, if necessary, force the system into
a safe state. Device tracking methods attempt to record the device usage
and location trajectory to thwart counterfeiting and aging attacks.

**4** Advances in Hardware Design for Security and Trust

5. Device Identification and Authentication: Devices can be uniquely identified using device-specific characteristics induced by the fabrication process. Authentication protocols used to verify access privileges often require
unique passwords. These in turn require true random number generators
(TRNGs). A variety of TRNGs and challenge-response pairs of passwords
unique to a device can be constructed using physical unclonable functions
(PUFs) which are unique to each individual device. Device identification
and authentication methods should be implemented to defend against unauthorized access.

**1.4** **OVERVIEW OF CHAPTERS**

This volume contains 13 chapters on selected topics and emerging directions in hardware security and trust. The next two chapters discuss various drivers for security and
trust and analyze related issues in developing and deploying hardware products and
design tools. The remaining chapters are focused on the design of hardware to defend against specific types of attacks and to mitigate risks in using hardware systems
and their supply chains.

Chapter 2 by Simon discusses hardware security issues important to the consumer

technology industry and challenges in adopting emerging assurance methods. It
identifies several areas of research that have high potential for transitioning to consumer electronics products.
Chapter 3 by Orlando et al. analyzes hardware security, safety, and trust issues from

the commercial EDA industry perspective. It discusses multiple market drivers and
the interplay between research and commercial challenges. The authors emphasize
the need for safety and security assessment early in the design process.
Chapter 4 by Gubbi et al. discusses recent advances in hardware trojan (HT) detec
tion using machine learning (ML) techniques. In addition, Gubbi et al. propose a
new ML-based method that does not require a trojan-free golden IC for reference.
They present an EDA tool flow for HT detection and a neural net–based timing
profiling method to improve the sensitivity of HT detection such that even small
changes in the timing paths can be detected.
Chapter 5 by Choi et al. reviews the state of the art in reverse engineering of in
tegrated circuits and printed circuit boards and summarizes its limitations and
challenges. It then proposes a new reverse-engineering method which overcomes
these challenges by bringing together femtosecond laser delayering techniques,
correlative multimodality imaging, and cloud-based analysis platforms. Choi et al.
also provide roadmaps to adapt the proposed methodology for various reverseengineering applications.
Chapter 6 by Chakraborty and Vemuri discusses the utility of emerging polymor
phic devices to construct polymorphic functional units and switch boxes. It then
describes three methods to improve hardware security using these functional units
and switch boxes: 1) An RTL obfuscation method using bi-functional polymorphic

Introduction **5**

operators, 2) an RTL interconnect obfuscation method using polymorphic switch
boxes, 3) a logic obfuscation method suitable for split manufacturing with 3D integration.
Chapter 7 by Mishra et al. examines reverse engineering of analog and RF ICs and

reviews various obfuscation and performance locking methods to prevent reverse
engineering. Existing approaches introduce limited key space and are vulnerable
to key removal attacks. Accordingly, Mishra et al. explore purely analog locking
methods to increase the key space and defend against the removal attacks.
Chapter 8 by Vutukuru and Jha considers integrity, reliability, and aging of ICs in the

context of heterogeneous packaging. Following a review of the key issues in modeling, prediction, and monitoring of these parameters, Vutukuru and Jha survey the
existing monitoring methods, with a specific focus on electromagnetic radiation–
based techniques. Monitoring methods using several emerging novel devices are
discussed in detail.
Chapter 9 by Reichling et al. examines emerging research in side-channel attacks

to recover cryptographic keys by collecting and analyzing power or EM traces.
In particular, it summarizes recent research in applying deep learning methods to
increase the attack effectiveness. Reichling et al. present a detailed workflow for
deep learning side-channel attacks and discuss the challenges and opportunities for
further research.
Chapter 10 by Emmert and Perumalla considers the use of asynchronous logic to

avoid side-channel information leakage. It introduces the use of clock-less null
convention logic (NCL) and describes NCL-based cell development and a logic
design methodology using these cells. Finally, it discusses the limitations of NCL
design and explains how the proposed methodology overcomes those limitations.
Chapter 11 by Fei and Xu investigates the security of ARM TrustZone TEE (trusted

execution environment) which is widely used in mobile and embedded systems to
execute secure applications in an isolated environment with dedicated resources.
A number of side-channel attacks which exploit certain vulnerabilities associated
with on-chip resources shared between the trusted and untrusted resources have
been demonstrated. Fei and Xu analyze the side-channel vulnerabilities and propose effective countermeasures.
Chapter 12 by Miftah et al. provides a survey of the state-of-the-art and emerging

directions for security verification for complex systems-on-chip (SoCs). Due to the
number, variety, and complexity of the 3PIP cores comprising the SoCs, verifying
their security properties becomes a challenging task. Miftah et al. examine these
challenges and reviews various methods proposed for security verification before
fabrication and continuous monitoring after fabrication.
Chapter 13 by Fang et al. discusses vulnerabilities in cloud-based shared FPGA ac
celerators. Multi-tenant FPGAs use some communication link to transfer application bitstreams and data between the FPGA and a host processor. Fang et al.
develop a method to attack the PCIe communication channel between the host
and the FPGA to identify the types of accelerators co-located on the FPGA. This
fingerprinting attack in turn would allow an attacker to use the knowledge of the

**6** Advances in Hardware Design for Security and Trust

accelerators so gathered to mount side-channel attacks to recover, for example,
information from the co-located applications.
Chapter 14 by Collier and Lambert addresses risk management in device supply

chains. Various sources of risk, such as counterfeit devices, compromise the availability of functional and certifiably secure devices in the required quantities. This
chapter explains, and demonstrates through an example, how principles of systems
engineering and operations research can be applied to systematically model risk
sources and vulnerabilities and evaluate their impact on the device supply chains.

# 2 Hardware Security In The
### Consumer Technology Industry

Paul M. Simon

**2.1** **INTRODUCTION**

The military, academic, and research and development (R&D) worlds readily experiment with hardware and embedded system security mechanisms. These organizations are better suited to enhancing the state-of-the-art and state-of-the-possible.
These organizations are structured and geared toward conceptualizing new approaches, combinations, and uses for advanced security technologies. The cost of
research is viewed as an investment in the future, not as a tax. They are not striving to maximize profits because they are generally not profit centers. Some security
mechanisms end up being successful, for example the use of encryption like advanced encryption standard (AES) or the various trusted architectures or secure-boot
options. Other technologies are viewed as too unwieldy, difficult to implement, or are
not cost-effective to deploy or commercialize. Those ideas are eventually abandoned.

In contrast, the consumer technology industry is generally not driven by the need
for security within its devices; it is driven by convenience, usability, or profitability
of devices. Moreover, consumer electronics manufacturing is driven by minimizing
cost and increasing speed-to-market. Because of this, the consumer technology industry tends to lag behind military, academic, and R&D organizations when adopting
new hardware or embedded system security techniques. Only when security mechanisms become comparatively inexpensive to deploy or easy to implement at a large
scale do these technologies become part of consumer electronics. There are still numerous challenges that stand in the way of universal adoption of embedded security
mechanisms and few solutions.

**2.2** **CHALLENGES FOR CONSUMER ELECTRONICS**

The consumer electronics industry faces numerous challenges not typically addressed by military, academic, and R&D organizations. Each of these challenges
individually are a significant headwind to incorporating hardware and embedded

[DOI: 10.1201/9781003510949-2](https://doi.org/10.1201/9781003510949-2) **7**

**8** Advances in Hardware Design for Security and Trust

security mechanisms into devices. Worse yet, all these challenges are interrelated
and came about as solutions to other challenges, like outsourcing of manufacturing [1]. Taken all together, it becomes abundantly clear why robust hardware and
embedded systems security in consumer electronics continues to be elusive.

**2.2.1** **SCALE**

A major challenge facing the consumer electronics industry is designing and manufacturing devices at massive scale. One of the most notable examples is the Apple
iPhone. Apple has sold at least 180 million iPhones per year from 2015 through
2023 [2], with no end in sight. By comparison, in March 2024, the U.S. Department of Defense (DoD) approved the F-35, the most technologically advanced fighter
aircraft, to enter full-rate production. The manufacturer of the F-35, Lockheed, recently forecast that “the F-35 program will have a stable production rate goal of
about 156 aircraft per year for at least the next five years” [3]. That is a difference in roughly six orders of magnitude between the two production rates. Manufacturing millions of electronic devices per year with minimal defects is challenging enough without ensuring robust hardware security is properly deployed in those
devices.

**2.2.2** **SUPPLY CHAIN**

To achieve manufacturing and production at scale, consumer electronics companies
typically outsource the manufacturing, assembly, and packaging of their devices,
possibly to multiple companies [1]. Doing so allows each company to focus their energy and resources on core strengths, for example device design and physical layout,
printed circuit board (PCB) fabrication and assembly, or final assembly and packaging. This process injects numerous other third-party companies into the supply
chain, with many of those third parties being overseas. Even when secure hardware
technologies are developed, the vast international supply chain introduces new threat
vectors and vulnerabilities. For example, once devices are manufactured, the provisioning of encryption keys and media access control (MAC) addresses or the loading
of digitally signed software or firmware may also be performed by a third party. If
these third parties have access to encryption keys and digitally signed software or
firmware, then the end products may not be as secure as expected. Provisioning and
loading security keys and digitally signed software onto the hardware must follow a
particular order to maintain the security of the keys and software. Even one improperly provisioned device could cause a vulnerability or security issue. Opportunities
arise for steps to be skipped, the same key being loaded onto multiple devices, exfiltration of the digitally signed software for analysis, or other security breaches.
If other security steps are skipped, embedded e-fuses may not be properly set. Because these third parties are outside of the corporate landscape, relationships are
controlled by legal contract. If physical security controls that safeguard the handling
of devices throughout the supply chain are not explicitly enumerated in the contract,
most likely those security controls are not implemented. This leaves secure hardware

Hardware Security In The Consumer Technology Industry **9**

**Figure** **2.1** A notional version of a consumer electronics supply chain demonstrating the extensive attack surface, where any node or any transition may be an attack
vector.

technologies at risk of being actively bypassed, mitigated by other means, or possibly
subject to nation-state level exploitation.

Consider all the possible steps within the supply chain for consumer electronics. For example, Figure 2.1 shows a notional version of a consumer electronics

**10** Advances in Hardware Design for Security and Trust

supply chain. The broadest take-away is that each node and each transition represent a possible attack vector to infiltrate a supply chain, as highlighted by MITRE’s
Supply Chain Attack Framework [4]. It is not uncommon for a company to only
touch the endpoints in the life of a device: the initial design and the final sale to
the consumer. All steps in the middle may be outsourced to contract manufacturers (CMs) or service providers. Even the handling of returns and refurbishment may
be handled by third-party contracted organizations. The layout of the PCBs, programming of the firmware or software, the fabrication of the PCBs, acquisition of
the components, population of the PCBs, final assembly, and packaging may all
be performed by contracted service providers and all of those could be performed
by different companies in different geographic locations. All these services must
be performed as inexpensively as possible to maintain the general affordability of
these consumer electronics. Furthermore, these devices number in the hundreds of
thousands to possible tens of millions. Any additional assembly process, components, or service, like security features or special processors, adds to the cost of the
device.

Manufacturing at the scale of consumer electronics requires components to be
ready and available. If the average electronic device contains 500 components,
then to manufacture 10 million devices would require managing an array of 5 billion components. If one company cannot provide an adequate number of passive
components, like resistors or capacitors, or more critical components like Wi-Fi
transceivers, microprocessors, crystal oscillators, or complex systems on chip (SoC),
other sources need to be engaged to maintain the manufacturing throughput. In the
scramble to maintain expected manufacturing throughput, the qualification and authorization processes my not be followed for secondary sources. Secondary sources,
especially when considering critical components, introduce an entry vector for injection of counterfeit, substandard, recycled, or gray-market components. This is
what occurred during the peak of COVID-19 and the ensuing supply chain constrictions [5]. Additionally, with the fast-paced turnover of inventory, other logistics
and management issues arise, including transport of the components from the manufacturer or reseller to the assembly facilities, management and storage of components on-site, and loading the reels of components into the pick-and-place machines.
In each of these additional steps, opportunities exist for unnoticed infiltration or
substitution.

The scale of manufacturing also has a direct impact on the cost of devices. The
scale can be a benefit by dividing the non-recurring engineering (NRE) costs across
many devices. Conversely, it is common for consumer electronics companies to sell
hardware at a loss, relying on a software subscription or recurring cost model to
turn a profit. The difference between using a $0.10 component and a $0.15 component across 180 million devices translates into a Cost of Goods Sold (COGS)
savings of $9 million. The COGS directly impacts profit margin and gross profit [6].
As contract manufacturing companies try to meet a particular price-point, there is
downward pressure on the COGS to maximize profits. If contract manufacturers are
engaged to assemble the devices, they are typically paid a flat rate for a batch or

Hardware Security In The Consumer Technology Industry **11**

set quantity of devices. Because the profit margin of contract manufacturers hover
around 3% [7], there is clear motivation to use substandard, recycled, gray-market,
or otherwise cheaper components in the assembly process to inflate those margins.
Manufacturing steps, such as cleaning off excess solder flux and residue, may be
skipped. Any reduction in cost or time spent in assembly saves money for the contract manufacturer.

Another aspect of contract manufacturing that must be considered includes the
inevitable defective units that are produced that do not make it out of the factory.
Rework slows the manufacturing process and may potentially reduce profits. On the
other hand, scrapping the defects, while saving time in labor and handling, reduces
profits as wasted materials. Worse yet, scrap may not be tracked or may be improperly destroyed, leading to intellectual property (IP) leaks allowing a malicious agent
to develop hardware modification attacks. The balancing act between reworking as
many devices as possible quickly without waste creates an environment where reduced acceptance criteria occurs or defective units may be exported to low-cost resellers.

An unexpected way the supply chain may affect embedded systems security is
at the front and back doors of the various companies who handle devices. A lack
of physical security or security controls at the design, manufacturing, or assembly
facilities opens the door (pun intended) for tampering or substitutions during development on the assembly line. Physical intervention may be used to defeat any embedded hardware and software security mechanisms. The unsecured, unmonitored,
or untracked transport or shipping of components and devices from one facility to
another is another opportunity for malicious behavior. Packages that disappear from
one site and reappear at another site without adequate controls creates opportunities
for malicious substitutions or modifications. Therefore, embedded security is unexpectedly coupled to all the physical aspects of manufacturer facility security and
supply chain security controls.

**2.2.3** **CONSUMER PERCEPTIONS**

An additional complication to deploying hardware security mechanisms is that consumers are increasingly cost-conscious. They may refuse to spend more for devices
if additional security features are not directly observed or perceived. For the average person, mechanisms should not interfere with or degrade regular device functionality. Similarly, consumers who want additional embedded security features are
less willing to pay a premium price-point. Because of that, security mechanisms
typically only find their way into hardware when the technology is mature enough
to support and demonstrate security and trust without negatively impacting performance and functionality. For example, the ARM TrustZone [8] has been deployed as
a method of securing hardware in mid- and high-end electronics. However, the TrustZone requires digitally signed firmware or software to enforce the hardware security
features. In this regard, the firmware and software are foundational to the security
because software development is far cheaper and faster than hardware development.
Unfortunately, signed firmware leads to longer boot times which may be unaccept

**12** Advances in Hardware Design for Security and Trust

able to consumers who prefer faster performance over security. The ARM processors and similar devices are still commercial off the shelf (COTS) components that
are manufactured in large numbers. The hardware is arguably still vulnerable [9–11].
Consumer perceptions can change if a massive exploit occurs, causing a reevaluation
of nascent hardware, new legislation is created, or if security functions are presented
as a premium value-add.

**2.2.4** **DEPLOYMENT**

The methods of deployment or updates of hardware security in consumer electronics
directly impacts the technology proliferation. In the automotive industry, manufacturers frequently use the same engine, transmission, controls, or accessories across
multiple models to reduce development costs. This also includes the software. Doing so reduces software development, testing, debugging, and long-term sustainment costs. The same is true for the consumer electronics industry, where similar
hardware and software are used across multiple devices or device families. In some
cases, there may even be a corporate policy to use identical critical components, like
Wi-Fi and Bluetooth transceivers, memory modules, processors, or encryption cores,
across multiple devices. This allows software and firmware development costs to be
shared across multiple platforms. Therefore, security mechanisms become somewhat
modular, despite a coupling of the hardware to the firmware or software. In these
cases, software or firmware updates may be deployed to address bugs or vulnerabilities as they appear, and the impact of the update covers multiple device types.
For the automotive industry, over-the-air (OTA) software updates have solved many
bug fixes, patches, and systems updates, and they can be deployed rapidly. However these still need to be compatible with the hardware, forcing the hardware to be
flexible while also secure. Despite these methods, software updates cannot solve all
problems. Hardware and embedded systems security mechanisms are still needed to
protect the data and privacy of end users.

**2.3** **REQUIREMENT FOR ADOPTION**

As a cost-saving measure, it is common for consumer electronics manufacturers to
assess hardware only at the end of the assembly process, and only by verifying device
functionality. Verifying functionality does not verify security, and penetration testing
does not verify the security of the supply chain. In general, the consumer electronics
industry will not see widespread adoption of embedded hardware security mechanisms until certain design or implementation requirements are met. These broad
requirements include being robust yet simple to implement, being considered from
product inception yet not interfering with or degrading device functionality, being
technologically advanced yet inexpensive, and proceeding through a supply chain
that is secure and transparent yet free of constraints. These requirements address the
myriad complex and interrelated challenges inherent in the manufacturing of consumer electronics. In each case, they appear as trade-offs, but ideally improvements
are needed on both sides of the comparison.

Hardware Security In The Consumer Technology Industry **13**

**2.3.1** **ROBUST VS. SIMPLE TO DEPLOY**

One of the primary requirements for embedded hardware security mechanisms to
reach consumer electronics is that the security and trust features need to be robust
yet simple to implement in manufacturing. As detailed previously, deployment of
security mechanisms on 100 units differs greatly from deployment on 100 million
units. Because of that, embedded security mechanisms must be easy to deploy and
should have enough cryptographic entropy to protect hundreds of millions of individual units. For example, digitally signed firmware that dovetails with hardware
security environments, like ARM TrustZone [8], are a popular means for protecting
many devices. Common digital signatures use a 256-bit key, yielding 2 <sup>256</sup> possible
key combination. If the software is digitally signed properly, the hardware enforces
the security mechanisms and environments. Automatic software updates and antirollback features are also common with these security environments. The devices
regularly verify the version of software and firmware, making sure that they are up
to date and providing extra peace of mind to consumers. This level of robust security
spanning both hardware and software mitigates some of the risks inherent in using
CMs, requiring the software and hardware to verify each other. Marketing and advertising advanced security mechanisms to consumers are challenges because there are
few metrics that average consumers understand compared to speed, power draw, or
amount of data storage. However, robust mechanisms may also spur public interest
in those devices, especially if they are significantly more secure than offerings from
competitors. With the right solution, the requirements of robustness and deployment
simplicity can serve to motivate and reinforce the other.

**2.3.2** **BAKED-IN VS. FUNCTIONAL**

A challenging set of requirements for embedded hardware security mechanisms is
that mechanisms need to be considered from product inception and thoroughly integrated into system operations, yet should not interfere with or degrade device functionality. The analogy here is that security is like an ingredient in a loaf of bread, such
that it should be “baked in and throughout, and not just basted on top at the end.” In
other words, embedded security mechanisms must be designed and incorporated into
devices from the beginning of the design process. To meet this requirement, systems
engineers, security engineers, and hardware and software developers must clearly
define what is needed to meet the design requirements at the beginning and through
product design and development processes. Considering possible attack vectors at
the same time as the hardware, software, and systems design processes ultimately
drives down development costs because security features can be built around or incorporated in desired functions. Design teams are then free to refine the user experience, instead of struggling to layer on security mechanisms to address unanticipated
vulnerabilities. Continuing the bread analogy, if security makes the device unusable,
then the ingredient made the loaf of bread inedible. Consumers expect value for their
money, and when device functionality is impeded by security processes or the embedded security mechanisms are too difficult to turn on or use reliably, then that

**14** Advances in Hardware Design for Security and Trust

diminishes the value of the product. The best security features would be easy to use
by the general population and would not interfere with the expected performance
of the device. Degradation of capabilities to support security by slowing processing is not an option. Better still if the hardware security features are designed to be
future-proof, anticipating potential future threats and threat-actors. End users would
perceive the long-term functionality as significantly valuable.

**2.3.3** **ADVANCED VS. INEXPENSIVE**

For large-scale deployment of hardware or embedded security mechanisms, they
need to be technologically advanced enough to protect the device from attacks and
exploits, yet inexpensive enough to not dramatically increase the retail price, profitability, or manufacturing costs of the device. The most advanced mechanisms are
the ones that are flexible enough to be secure today and well into the future. However, because the hardware cannot be modified once it is in the hands of the end user,
this requires a balanced approach between hardware and software. This approach can
directly support both cutting-edge mechanisms and lower unit costs. Across 10,000
or 100 million devices, if the security mechanisms provide a significant benefit to
the end user, then the added cost of deployment can be countered by an increased
retail price-point. However, if those added security mechanisms do not prove obvious and beneficial to the end user, then the consumer may be turned off by an
increased retail price, at which point the security mechanisms begin to slice into the
profit margin of the device. If incorporated into enough devices, the development
costs for advanced hardware security mechanisms can be divided across many more
units, minimizing the impact to the price-point while also supporting the large-scale
security deployment. If the security mechanisms are used across a broad enough
selection of products, that would further bring the per-unit cost of implementation
down while potentially educating or contractually requiring the CMs how to implement them properly. Incremental refinements and evolutionary changes can also push
advancements without excessive financial investments.

**2.3.4** **SECURE VS. FREE-FLOWING SUPPLY CHAIN**

One of the hardest requirements for implementing hardware security in the consumer electronics industry is to secure the supply chain. Every entity, from designers
to CMs, retailers, and end users, would benefit from a secure and transparent supply chain. The benefits would be as appreciable as they are for grocery stores and
restaurants. The food supply has many more steps and processes for verification and
tracking through that supply chain compared to the electronics supply chain. There is
also a similar downward pressure on prices and varying levels of quality. Tainted food
causes illness or death, whereas tainted devices only allow ephemeral exploitation,
exfiltration of personal data, or loss of privacy. As described, the supply chain for
consumer electronics touches so many parties and goes through so many transitions
that adequate tracking or traceability is nearly impossible with today’s technology.
In many cases, supply chain relationships are managed only by legal contract. In

Hardware Security In The Consumer Technology Industry **15**

the best cases, those contracts detail every step in handling, and then performance is
audited to verify compliance. In other cases, the contracts are written very broadly
and compliance is rarely verified. Simple functional verification and validation at the
endpoints does not provide adequate granularity or visibility into the supply chain.
This lack of visibility and accountability erodes trust that devices will perform as
expected. More insight into the entire supply chain would offer assurances that what
is in a device is exactly what was designed to be, and that the expected security
mechanisms expected are operating correctly. This may even offer support that longterm life and usage of a device will continue to perform exactly as expected. Intermediate testing steps, though, would slow the manufacturing and transport of devices.
To support the massive number of devices produced on a daily basis and to provide
the best experience for retailers and end users, there should be as few constraints as
possible. As noted previously, any turbulence or constriction in the supply chain has
the potential to reduce supplies, increase intermediate handling, and ultimately raise
prices.

**2.4** **AREAS OF PROMISING RESEARCH**

Despite the numerous challenges that exist to deploying robust hardware and embedded systems security into consumer electronics, some technologies are making their
way into devices. Some examples include hardware-enforced digitally signed software and firmware, hardware-enforced anti-rollback of firmware, on-chip security
fuses, and on-chip encryption capabilities. The proliferation of SoCs has mitigated
many external attack vectors, but has also shed a light on the design and fabrication
these complex devices. There is also active research into other promising technologies that, while not specifically directed at hardware or embedded systems security,
will ultimately aid in protecting the hardware in consumer electronics.

**2.4.1** **DEVICE TRACKING**

Because securing the supply chain is foundational to deploying embedded security
mechanisms into consumer electrics, methods for tracking devices through fabrication, assembly, and sale are of significant interest. For example, one possible solution
to device tracking is developing a highly detailed ledger known as device-identifying
information (DII) for every Internet of Thing (IoT) device. Similar to personally
identifiable information (PII) for people, the concept of DII is a step toward identifying each individual component in a device and tracking them through the supply
chain. At each transfer point or assembly process, additional entries are made in the
ledger, recording the date, time, location, process performed, an obfuscated identifier for the person performing the process, and so on. All this information taken
together provides a complete mapping of a device in association with its serial number. This is a massive amount of data and information about manufacturing lots,
sources, and transport details for every component and assembly. The information
may allow statistical observations or correlation of components to specific device serial numbers, lots, or manufacturers if issues arise. The challenges that exist are how

**16** Advances in Hardware Design for Security and Trust

to accurately collect and store this information in a manner where it cannot be tampered with while also maintaining an unbroken connection to the device itself. This
device-specific and device-unique identification opens opportunities for a solution to
full supply chain provenance.

An incremental example of device tracking information is the U.S. Federal Communication Commission (FCC) creating a voluntary cybersecurity labeling program for wireless consumer IoT products. The FCC’s cybersecurity
labeling program, at this time, only reflects “details about the security of the product,
such as the support period for the product and whether software patches and security
updates are automatic.” The intent is to “help consumers make informed purchasing
decisions, differentiate trustworthy products in the marketplace, and create incentives
for manufacturers to meet higher cybersecurity standards” [12]. This is a voluntary
program where manufacturers may offer security-related information about their devices, and in return, are provided an FCC-approved label reflecting participation in
the program.

A possible solution to the storage of data could be a blockchain-styled digital
ledger [13]. This technique could record the serial number, make, model, batch number, date and time of manufacture, assembly line, manufacturing lots for each component, and all assorted information about the device and everyone who touched it
throughout the supply chain until it gets to the end user. This digital ledger can also
store and report the version of firmware and software loaded on the device, ensuring that the latest updates are incorporated, and would only be updated by the end
user. This could also be included as part of the FCC’s cyber trust mark, or could help
feed the cyber trust mark repository. Additionally, if the digital ledger were inscribed
in or on the physical device, then the device provenance would travel with the device itself. This concept leads to a hybridized application of physically uncloneable
functions (PUFs), making them more broadly useful [14]. PUFs have demonstrated
themselves in various applications where maximum security is the goal [15–17]. In
the context of deployment into consumer electronics, PUFs have many challenges
that still need to be addressed. The relatively exotic nature of them, manufacturing
costs, amount of variability due to temperature and aging effects, and the arguably
small amount of cryptographic entropy all require improvements to make PUFs fully
usable in consumer electronics. However, even if using PUFs to identify all the Wi-Fi
transceivers or other critical chips that are manufactured for use in all types of devices
is intractable, perhaps using PUFs embedded in the plastic casing or a combination
of other DIIs to uniquely identify the final end product is within reach. Overlapping
a blockchain-styled ledger and PUFs may provide a robust, scalable, secure solution
to secure consumer electronics supply chains.

**2.4.2** **COUNTERFEIT AND SUBSTITUTION DETECTION**

Another aspect of securing the supply chain is protecting against counterfeit, substandard, or recycled components proliferating legitimate suppliers and manufacturers. In certain situations, lower standard and recycled components are useful and
may be a cost-effective method for prototyping, rapid development, or for use in

Hardware Security In The Consumer Technology Industry **17**

devices that do not require new components. However, consumers generally expect
that the electronics that they purchase are new, untouched, and function properly out
of the box. Additionally, counterfeit and substituted components may not support
current or future embedded security mechanisms, and they may have a drastically
diminished useful life. Therefore, the consumer electronics industry invests significant time and effort in verifying that counterfeits and substitutions have not infiltrated their devices. This has an added effect of protecting the reputation of their
devices and their company. Numerous methods for counterfeit and substitution detection are being explored [19, 81]. One method of counterfeit detection is adding a
watermark to the outside casing of an integrated circuit (IC). The watermarks added
to ICs are similar to watermarks in printed papers and currency such that they allow
for easy recognition of a genuine item. Watermarking of critical components is one
such area of research that may assist in both tracking of devices and components
through the supply chain, as described previously, while also mitigating counterfeit
proliferation [20,21]. PCBs are also subject to potential tampering and substitutions.
Watermarks applied to PCBs [22] involve another area of similar research that would
aid in securing the consumer electronics supply chain. These hardware watermarks
are not embedded in the IC or PCB material as PUFs are; they are merely a manner
of marking the IC or PCB. These markings allow identification and rapid validation
of larger components to indicate they are legitimate, and also change their character
if they have been tampered with. One challenge is that watermarking is only intended for the critical components in a circuit; passive components and connectors
are typically not considered when applying these protections. The motivation for this
approach is that passive components and connectors may not have a direct impact on
functionality if they were counterfeit or substandard. Another motivating factor is
that watermarking is still an additive cost to components, and when applied to hundreds of thousands or millions of components or assemblies, critical or not, that cost
becomes difficult to justify. As the technology is improved and refined through additional R&D, the cost-at-scale will decrease.

**2.4.3** **FULL DEVICE AND SYSTEM SIMULATION**

An area of research that could be used to address the myriad complexities of consumer electronics manufacturing while aiding in the design and deployment of embedded hardware security mechanisms is full-scale software simulation of hardware
devices. A full-scale simulation supports awareness of the hardware, firmware, software, and their interactions from the very beginning of the design. Using this approach in the design and development of consumer electronic devices, teams can
experiment with hardware-based security mechanisms without having to fabricate
custom hardware. As the hardware is simulated, the various processors, memories,
and interfaces are monitored, allowing the designers to observe every bit of data
during processing. Making changes to the hardware design at this stage is trivial
compared to fabricating and testing prototypes, a process that may take months.
Overlaying the firmware, software, and other security mechanisms, designers have
the ability to detonate bugs or find potential coding errors while also monitoring

**18** Advances in Hardware Design for Security and Trust

every interface and transaction. Security features can be enhanced and verified at the
design phase or upon subsequent design updates. Even long-term software updates
can be deployed into the simulation for rapid testing and subsequent deployment
to users in the case of newly discovered vulnerabilities. Taking a broader scope, a
full-scale device simulation creates an opportunity to fingerprint the behavior of devices which can then be used to verify and validate that every device, as it comes
out of the manufacturing facility is behaving exactly as expected, without any additional emergent behaviors. The simulation can even be extended to fingerprint the
behavior and performance of multiple devices in a network and their interactions.
With a full-scale performative-based fingerprint, the consumer electronics industry
will have the ability to validate functionality and design consistency of devices more
thoroughly. Device testing can be performed faster and more accurately using the
performative fingerprint and automated tools. The validation can be performed at the
bit level, comparing the designed fingerprint to exact parameters during operation.
When the devices finally end up in consumer hands and while the devices perform
initial checks for software or firmware updates, the device can also perform a validation that the performative fingerprint is still correct and matches expected values. Using artificial intelligence/machine learning (AI/ML) to generate real-world
input, various negative tests may be performed, further enhancing the robustness of
the tests. These AI-generated negative tests, while time consuming, can be scoped
to find potential zero-day vulnerabilities; unexpected race conditions; or mismatches
between hardware, firmware, and software components. This type of full-scale simulation hearkens back to the automotive industry of the 1980s when Renault, Porsche,
Chrysler, and others embarked upon using computer-aided design/computer-aided
manufacturing (CAD/CAM) tools to completely design automobiles. These revolutionized the processes and trimmed unnecessary manufacturing and assembly steps.

A full-scale simulation of hardware should not be confused with a digital twin.
Whereas a digital twin is a virtual model created to reflect the performance of a
device, a simulation represents the design or theoretical device itself. The simulation
can be used to generate data for a digital twin. A digital twin is used to create a virtual
environment to study several simulations and may be supported by real-world sensor
data. In this case, a digital twin replicates what is happening to an actual device in
the real world; a simulation represents the art of the possible for a design.

The two primary challenges with creating a full-scale software simulation of devices are navigating the levels of abstraction and managing the amount of data and
processing needed to capture the performative fingerprint. The levels of abstraction
are from physical hardware (the PCBs, resistors, capacitors, oscillators, etc.) through
complex assemblies and processors to the bare-metal programs, operating system,
or applications, as shown in Figure 2.2. Transitioning from one level of abstraction
to another may be technically difficult; however, each lower level may be instantiated as submodules in the next higher level of abstraction. As the level of abstraction
increases, more assumptions must be made about the functions below. To maintain
visibility and granularity, the complexity of the simulation increases, as does the
number of data points collected or recorded. It is possible that the fidelity of the

Hardware Security In The Consumer Technology Industry **19**

**Figure** **2.2** Levels of abstraction that would be needed to simulate a notional consumer electronics device.

simulation may decrease because of various assumptions or inherent complexities
make it necessary to aggregate data or processes. The amount of time to test functionality will also increase when moving up the levels of abstraction due to the increasing number of data points, simulated components, and complexity. Suffice to
say, if data regarding every individual component within a device is collected at every clock transition and how the software or apps behave in response, the amount of
collected data and required processing will be massive. Cloud computing and storage options make this challenge somewhat easier to solve without having to resort to
self-hosting. The prevalence of high-performance computing clusters for hire coupled with cloud storage may also help to address the speed of processing.

**2.5** **CONCLUSION**

Major challenges exist to deploying reliable, robust, and cost-effective hardware and
embedded systems security mechanisms into consumer electronics. Unlike military,
academic, and R&D organizations, the consumer electronics industry does not typically lead the development of security mechanisms. Some embedded security solutions are mature and readily available, and those get rolled into consumer electronics
devices. Unfortunately, the consumer electronics industry is more focused on the
profitability of devices and not directly focused on security. If secure devices are
what the average consumer wants, and they can be delivered at scale with robust and
easily deployed and used embedded security mechanisms, then an opportunity arises
to leverage security for more profits.

**20** Advances in Hardware Design for Security and Trust

**REFERENCES**

1. Scott J Mason, Michael H Cole, Brian T Ulrey, and Li Yan. Improving electronics manufacturing supply chain agility through outsourcing. International Journal of Physical
Distribution & Logistics Management, 32(7):610–620, 2002.
2. Statista Search Department (February 24, 2024). Unit sales of the Apple
iPhone worldwide from 2007 to 2023. [https://www.statista.com/](https://www.statista.com/statistics/276306/global-apple-iphone-sales-since-fiscal-year-2007)
[statistics/276306/global-apple-iphone-sales-since-fiscal-](https://www.statista.com/statistics/276306/global-apple-iphone-sales-since-fiscal-year-2007)
[year-2007/, February 2024.](https://www.statista.com/statistics/276306/global-apple-iphone-sales-since-fiscal-year-2007) [Accessed 07-20-2024].
3. John A. Tirpak. At last: After 23 years, F-35 enters full-rate production. Air & Space
Forces Magazine, March 2024.
4. John F Miller. Supply chain attack framework and attack patterns. The MITRE Corporation, MacLean, VA, 2013.
5. Keith Bradsher. China’s covid lockdowns set to further disrupt global supply chains.
The New York Times, 2022.
6. Andrew Bunnie Huang. The hardware hacker: Adventures in making and breaking
hardware. No Starch Press, 2019.
7. Aswath Damodaran. Margins by Sector. [https://pages.stern.nyu.edu/](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html)
˜ <sup>[adamodar/New_Home_Page/datafile/margin.html, January](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html)</sup> <sup>2024.</sup> <sup>[Ac-</sup>
cessed 07-29-2024].
8. ARM Limited. Trustzone for Cortex-A. [https://www.arm.com/](https://www.arm.com/technologies/trustzone-for-cortex-a)
[technologies/trustzone-for-cortex-a, 2024.](https://www.arm.com/technologies/trustzone-for-cortex-a) [Accessed 07-25-2025].
9. Lilian Bossuet and Carlos Andres Lara-Nino. Advanced covert-channels in modern
socs. In 2023 IEEE International Symposium on Hardware Oriented Security and Trust
(HOST), pages 80–88. IEEE, 2023.
10. Mathieu Gross, Nisha Jacob, Andreas Zankl, and Georg Sigl. Breaking trustzone memory isolation and secure boot through malicious hardware on a modern FPGA-SoC.
Journal of Cryptographic Engineering, 12(2):181–196, 2022.
11. Mohammad Mannan and N Asokan. Confronting the limitations of hardware-assisted
security. IEEE Security & Privacy, 18(5):6–7, 2020.
12. Federal Communications Commission et al. Cybersecurity labeling for internet of
things. Federal Communications Commission, Tech. Rep, 7, 2023.
13. Fahim Rahman and Mark Tehranipoor. Blockchain-enabled electronics supply chain assurance. In Emerging Topics in Hardware Security, pages 1–26. Springer International
Publishing, Cham, 2021.
14. Saraju P Mohanty, Venkata P Yanambaka, Elias Kougianos, and Deepak Puthal.
PUFchain: A hardware-assisted blockchain for sustainable simultaneous device and data
security in the internet of everything (IoE). IEEE Consumer Electronics Magazine,
9(2):8–16, 2020.
15. Nikolaos Athanasios Anagnostopoulos, Yufan Fan, Muhammad Umair Saleem, Nico
Mexis, Emiliia Gel´oczi, Felix Klement, Florian Frank, Andr´e Schaller, Tolga Arul, and
Stefan Katzenbeisser. Testing physical unclonable functions implemented on commercial off-the-shelf nand flash memories using programming disturbances. In 2022
IEEE 12th International Conference on Consumer Electronics (ICCE-Berlin), pages 1–
9. IEEE, 2022.
16. Himanshu Thapliyal and Saraju P Mohanty. Physical unclonable function (PUF)-based
sustainable cybersecurity. IEEE Consumer Electronics Magazine, 10(4):79–80, 2021.
17. Amit Degada and Himanshu Thapliyal. An integrated TRNG-PUF architecture based
on photovoltaic solar cells. IEEE Consumer Electronics Magazine, 10(4):99–105, 2020.

Hardware Security In The Consumer Technology Industry **21**

18. Ujjwal Guin, Ke Huang, Daniel DiMase, John M Carulli, Mohammad Tehranipoor, and
Yiorgos Makris. Counterfeit integrated circuits: A rising threat in the global semiconductor supply chain. Proceedings of the IEEE, 102(8):1207–1228, 2014.
19. Adam Hook. New solutions to combat counterfeits. In 2024 Pan Pacific Strategic
Electronics Symposium (Pan Pacific), pages 1–19. IEEE, 2024.
20. Ujjwal Guin, Xuehui Zhang, Domenic Forte, and Mohammad Tehranipoor. Low-cost
on-chip structures for combating die and IC recycling. In Proceedings of the 51st Annual Design Automation Conference, pages 1–6. Association for Computing Machinery,
2014.
21. Mark Tehranipoor, Kimia Zamiri Azar, Navid Asadizanjani, Fahim Rahman, Hadi Mardani Kamali, and Farimah Farahmandi. Rethinking hardware watermark. In Hardware
Security: A Look into the Future, pages 143–182. Springer, 2024.
22. Dhwani Mehta, Hangwei Lu, Olivia P Paradis, Mukhil Azhagan MS, M Tanjidur Rahman, Yousef Iskander, Praveen Chawla, Damon L Woodard, Mark Tehranipoor, and
Navid Asadizanjani. The big hack explained: Detection and prevention of PCB supply
chain implants. ACM Journal on Emerging Technologies in Computing Systems (JETC),
16(4):1–25, 2020.

# 3 A Commercial EDA
### Perspective on Hardware Security, Safety, and Trust

P. Len Orlando III, Lang Lin, and Norman
Chang

**3.1** **INTRODUCTION**

**3.1.1** **IMPORTANCE OF HARDWARE SECURITY**

The Semiconductor Industry Association projects that the commercial electronics industry revenue will exceed a trillion dollars by 2030, and it has the second-highest
reinvestment into research and development behind pharmaceuticals and biotechnology [1]. This continued rapid electronics growth can be attributed to the societal
demand for ubiquitous electronics that are integrated into our everyday lives and
aligns with societal transformations associated a knowledge-based economy as described by the fourth Industrial Revolution [2]. Pervasive and often invisible, electronics fuel our cell phones, cars, laptops, gaming devices, smart devices, and health
monitors; often put into end use sectors of PCs and computers (30% of the market), communications (26%), automotive (14%), consumer (14%), industrial (14%),
and government (2%) [1]. Society has become accustom to being highly connected,
rapidly accessible information, and processing at our fingertips with the proliferation
of electronics seeding the transformational technologies of the future. This societal
shift towards ubiquitous electronics has not come without a cost as they are often
a nexus of personal, private, and confidential data serving as the gateway into our
health and financial systems. This makes electronics a rich target for exploitation.

The rise of cybercrime over the last two decades has increased societal awareness of the risks involved with a highly connected world. As described in the U.S.
Senate’s March 2014 Target Data Breach report of the November 2013 Target cyberattack, attackers gained access to Target’s computer network and stole financial and
personal data of 110 million Target customers [3] and resulted in a $18.5 million
settlement [4]. The Center for Strategic and International Studies (CSIS) maintains a timeline which records significant cyber incidents that have occurred against
government agencies, defense, and high-tech companies with losses greater than a

[DOI: 10.1201/9781003510949-3](https://doi.org/10.1201/9781003510949-3) **22**

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **23**

**Figure** **3.1** Attacker: Individuals and rogue actors, organized crime, to nation state
actors.

**Figure 3.2** Illustrative electronic industry attacks.

million dollars [5]. Some noteworthy observations, first the progression of cyberattacks started as researcher and individuals and has now matured to include organized crime syndicates and well organized and orchestrated nation state actors. Second, adversarial advantage is in favor of the attacker because they have access to the
full system, often crossing designed in or architectural boundaries, to find the weakest entry point. Finally, all software runs on electronic hardware, and as software
cyber defenses improve, they are driving the attacker towards hardware-based attacks. Figures 3.1 and 3.2 show the temporal progression of hardware-based attacks,
and Figure 3.3 shows some of the efforts targeted toward countering these attacks.
Similar attack progressions are observable within the electronics industry and across
the life cycle of electronics. The illustrative examples highlight the security market drivers within the electronics industry having components of technology loss,

**24** Advances in Hardware Design for Security and Trust

**Figure 3.3** Example efforts to counter hardware attacks.

financial loss, and corporate liability:

1. Modchips, first observed mid-1990s, are additive hardware that circumvented intellectual property and copyright protections on gaming systems
thus enabling systems them to play imported or copied games. Commercial companies employed a two-prong counter measure, a technical solution to remove intrusion access points and deployment of sophisticated
anti-modchip measures and a legal solution leveraging many countries antipiracy laws, such as the Digital Millennium Copyright Act [6].
2. Row Hammer, circa 2014, effected dynamic random-access memory
(DRAM) hardware. Here, one could induce a memory hardware error, a
bit flip, via the execution of unprivileged software commands to induce a
repeatable compromise that allows software programs to access memory
locations not assigned to them thus circumventing the memory protections.
This attack was achievable because of the capacitor-based DRAM architecture and technology scaling which led to increased inter-bit signal coupling

[7, 8, 9, 10].
3. Spectre and Meltdown, circa 2017, take advantage of modern processor architectures where pipelining and out of order processing are used
to accelerate processor computation. To achieve faster processing, these
architectures predict what the next instruction will be and execute these

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **25**

instructions speculatively and make these speculative outputs available if
the prediction is correct. Spectre and Meltdown leverage this speculative
process, specifically the execution of speculations that were not correct,
or misspeculation, instructions that leave residual information or hints on
timing and encrypted keys. These exploits effected all Intel based x86 microprocessors, IBM Power processors, and some ARM holdings PLC with
reduced instruction set computer (RISC)-based processors with subsequent
variations effecting advanced micro devices (AMD) processors [11, 12].
4. BroadPWN, circa 2017, targeted the Broadcom BCM34xx family Wi-Fi
chipsets. This fully remote exploit allowed a payload to be delivered via
the BCM34xx to execute code on the main application processor. As the
BCM34xx chipset is a prolific third-party IP, this exploit affected many
major cell phone manufacturers (e.g. Apple, Samsung, and Android devices

[13, 14, 15]).
5. Heartbleed, circa 2014, is a vulnerability in OpenSSL cryptographic software library and allows an unauthorized individual to capture portions of
the system memory that contains encryption keys or passwords. At the time
of discover, approximately half a million servers were believed to be vulnerable to the attack, requiring administrators to patch those systems and
users to update and change their passwords [16, 17, 18, 19, 20].
6. A2, circa 2016, is an example of an in-circuit design modification where
a minute circuit modification payload can siphon charge, via coupling, to
target a victim flip-flop and force it a desired state. When orchestrated correctly, the authors were able to remotely control privilege escalation within
a processor manipulating a single privilege escalation bit. Detecting this
type of modification is challenging due to its physically small size, allowing
stealthy placement, orchestrated triggering coupling effect, and reachability
when performing post-manufacturing tests [21, 22].
7. Side Channel Emissions, utilize unintended information emitted from an
electronics system that, when correlated, can lead to the compromise of the
embedded security features, specifically encryption keys. All microelectronics produce emissions via side channels in the timing, power, thermal,
optical, and electromagnetic domains [23, 24].
8. “The Big Hack” and “The Long Hack” Bloomberg articles, circa 2018/
2021, are Bloomberg reports that indicated a nation state actor used a tiny
chip to infiltrate over 30 U.S. companies with compromised vulnerable systems through supply chain manipulation. Although unconfirmed, these articles highlight the susceptibility of the electronics supply chain to the worldwide manufacturing of electronics components and access available to foreign nations for manipulation. Later, this was further exacerbated by supply
chain issues stemming from the COVID-19 pandemic [25, 26, 27].
9. Proliferation of counterfeits and clones within the supply chain. “In 2017,
Defense Advanced Research Projects Agency (DARPA) pegged the cost
at $170 billion in lost electronics revenue. That same year, the Semi

**26** Advances in Hardware Design for Security and Trust

conductor Industry Association estimated that counterfeiting cost the chip
industry $7.5 billion per year” [28]. These supply chain attacks can be classified into five categories of counterfeit chips: recycled, cloned, re-marked,
over-produced, and forged. Initially, counterfeits tended towards low-cost
of entry approaches where desired parts were reclaimed from discarded
components and then cleaned for re-entry into the supply chain (i.e., recycled) or the substantiating documentation for the part was forged, allowing
for a similar package configuration to be substituted having a different function or without the internal electronic component. As detection mechanisms
improved, malicious suppliers countered, through a technique of blacktopping and re-marking of packaged electronic components. Often, these remarked components present as “new” and pristine when visually inspected
and compared to an equivalently aged part. The newer and more nefarious
techniques of function mapping to an embedded device to produce a replicate function and complete reverse engineering and remanufacturing (i.e.,
clones) allow for unsuspecting payloads to be inserted in the extra functionality or inserted during manufacturing [28, 29, 30, 31, 32].
10. Reverse Engineering for Inspection, Intellectual Property Protection and
Patent Infringement. Reverse engineering of a microelectronics system
or component is permitted under the Semiconductor Chip Protection Act
(SCPA) of 1984 and similar, in principle, to copyright’s fair use for research
and educational purposes and intended to protect an author’s original mask
work [33]. The SCPA is often paired with applicable patent and copyright
laws to provide full protection of the artwork and function of the original
author [34]. Reverse engineering can be classified into two domains composed of non-destructive and destructive techniques. Non-destructive techniques can employee electrical tests, optical inspection, and x-ray technologies to reconstruct printed circuit board, package, and chip-level features.
Destructive techniques are typically costly and intrusive, but they are able
to reconstruct a full chip in its entirety extracting both the physical topology
and logic function.

**3.1.2** **STANDARDS, POLICIES,** **AND** **GUIDELINES THAT IMPACT COMMER-**
**CIAL INDUSTRY**

The electronics industry utilizes several mechanisms to document known microelectronics hardware vulnerabilities, inhibit their creation, and manage supply chains.
The U.S. Department of Commerce (DoC) National Institute of Standards and Technologies (NIST) created and maintains the National Vulnerability Database (NVD).
The NVD was formed in 2005 as a standards-based vulnerability management data
repository structured to enable automation of vulnerability management, security
measurement, and compliance. Complimentary to the NVD is the MITRE corporations Common Vulnerabilities and Exposures (CVE) program which is a dictionary
or glossary of identified vulnerabilities which are referred to by a unique identifier

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **27**

(CVE ID). The CVE ID is assigned after the vetting process is completed which
includes reporting of the discover, type of vulnerability, affected code base, expected
impact, attack vectors, and remediation. The NVD is responsible for enriching the
CVE post-vetting and publishment to the CVE list. This process includes reviewing
the CVE Record, assigning a common weakness enumeration (CWE) identifier, metrics for exploitability and impact, development of the common product enumerator
(CPE) Applicability Statement, and peer review. In particular, the CWE, maintained
by MITRE, is a community developed list of weaknesses organized into a taxonomy framework that can become vulnerabilities. Since inception of this framework,
cyber-security hardware researchers have worked closely with NIST and MITRE to
ensure enhancements to this process were made to be inclusive of microelectronics
hardware vulnerabilities [35, 36, 37]. Additionally, several standards bodies (International Organization for Standards, Society of Automotive Engineers, Radio Technical Commission for Aeronautics, International Society of Automation) have included
and amended language to mitigate cybersecurity threats for software and hardware
within the automotive, airborne, communications, industrial automation, and controls sectors. Often sectors having existing functional safety requirements are early
adopters due to the additional safety risks associated with a cyber vulnerability. The
standards below are intended to establish a risk-based methodology across the complete life cycle of the components from design to retirement:

1. ISO26262 is a set of functional safety risk-based standards used to assess
hazardous operational situations [38].
2. ISO/SAE 21434 is a comprehensive cybersecurity risk management framework that requires compliance with relevant cybersecurity standards [39].
3. DO-254 is a requirement that necessitates independence of the design process from the verification process [40].
4. ISA/IEC 62443 are risk management practices for design, production, and
maintenance of their components [41].

Accellera Systems Initiative IP-XACT, IEEE 1685, is a vendor neutral XML format for re-useable electronic circuit designs, referred to as intellectual property (IP)
or 3rd Party Intellectual Property (3PIP), has two working groups to address security
and assurance:

1. Security Annotation for Electronic Design Integration (SA-EDI): Intended
to standardize an approach to provide information about IP security for integration and use and implementation related to mitigations and risk. Inherent
features build upon the existing MITRE CWEs and other security weakness
knowledge to form the Security Weakness Knowledge Base.
2. IP Security Assurance Standard (IPSA) specifies an approach to form a
Common IP Security Concerns Enumeration (CIPSCE) knowledge base for
the IP “black box” integrator to address during IP ingestion and use [42–44].

The Government-Industry Data Exchange Program (GIDEP) and DoD Instruction 5200.49 are applicable to the aerospace, defense, and government sectors where

**28** Advances in Hardware Design for Security and Trust

counterfeit electronics can compromise a U.S. National Security system. Army Lt.
Gen. Patrick J. O’Reilly of the Missile Defense Agency (MDA) mentioned, “We do
not want to be in a position where the reliability of a $12 million THAAD interceptor
is destroyed by a $2 part” [45] and similarly, in a Senate Armed Services Committee investigation, found that the 1,800 suspect counterfeit part cases exceeded over 1
million counterfeit parts affecting military aircraft and missiles [46, 47]. The purpose
of this instruction is to establish policy and oversight in the collecting and exchange
of counterfeit information for suspect and confirmed counterfeit items and major and
critical nonconforming items [47]. The GIDEP is the collection vehicle, database, for
these identified counterfeit electronics and provides the defense industry access via
membership. GIDEP reports are classified as Alert (report of nonconforming item),
Safe Alert (report a problem, failure, or nonconformance), Suspect Counterfeit (report of suspect or confirmed counterfeit), Problem Advisory (general reporting where
the probability of failure is low), and Agency Action Notice (distribution of actions
to mitigate a counterfeit threat) [47–49]. Other governmental policies influencing the
defense industry is the National Security Agency’s publication of the Hardware Assurance Technical Reports that are used to guide determination of levels of hardware
assurance different types of microelectronics components as related to their criticality to the top-level system and national impact caused by failure or subversion [50].

**3.2** **MARKET DRIVERS**

**3.2.1** **DEFENSE-IN-DEPTH**

Defense-in-depth is defined as the application of multiple countermeasures in a layered or stepwise manner to achieve security objectives [51]. The methodology involves layering heterogeneous security technologies in the common attack vectors to
ensure that attacks missed by one technology are caught by another [51].

To successfully achieve defense-in-depth, one must consider the spectrum of
threats that it realistically faces and the available solutions to create layers of defense.
Additionally, the standards and policies outlined above lack the operational details
necessary to be prescriptive, leaving the implementor with a large set of implementation decisions that may or may not result in success. In Hughes and Cybenko, they
explore a security approach based on confidentiality, integrity, and availability and
the quantification and assessment of cybersecurity defense investments [52]. Here,
they define confidentiality as the protection of information from access by unauthorized user, integrity as the protection of information from unauthorized modification,
and availability as the end users to derive benefit from the system.

As shown in Figure 3.4, for a successful attack to occur, Hughes and Cybenko
identified three elements as necessary and sufficient [52]:

1. The existence of system susceptibilities: This forms the basis for any attack as the ability for any system to simultaneously achieve confidentiality,
integrity, and availability is extremely difficult and thus has inherent weaknesses introduced through design trade-offs.

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **29**

**Figure 3.4** Three elements necessary and sufficient for successful attacks [52].

2. The ability of the threat to access the susceptibility: A threat will explore,
analyze, and discover susceptibilities that are accessible with the intent to
exploit the system. Taking advantage of access given for legitimate use and
manipulating it in unintended and undocumented ways.
3. The threats capability to exploit: Describes the attacker’s methodical approach to reverse engineering and use of guideposts, observational behaviours, to aid in the exploitation.

Utilizing this successful attack model one can implement a system security engineering approach based on criticality, integrity, and availability. This system security
engineering approach minimizes the number of potential susceptibilities and paths
for successful attacks through focusing on critical elements of essential functionality. Conscious separation of user access and attacker access and through system
availability keep key assets inaccessible to the attacker, either logically or physically. System security is not static and is instead a dynamic environment where the

**30** Advances in Hardware Design for Security and Trust

**Figure 3.5** Technology stack.

system is detecting, reacting, and adapting to the attacker’s exploitation attempts,
also known as the “moving target defense.”

**3.2.2** **SECURE ELECTRONICS FEATURES**

Electronics systems are a composition of software applications that operate on the
operating system which interfaces to the hardware through the firmware. A notional
representation of this technology stack is illustrated in Figure 3.5. For this context,
firmware is a low-level software or microcode which controls a device’s basic functions and serves as the breakpoint between the hardware and software domains. In
this model, secure operation is a shared responsibility of all the layers between the
secure software application layer and the secure hardware features. Any misconfiguration is an opportunity for an attacker to subvert the secure operations of the system.
Examples of common hardware security features are:

1. Unique identifiers take advantage of semiconductor process variation to create statistical and probabilistic uniqueness for identification or authentication.
a. A physical unclonable function (PUF) can be any physical object that,

for a given input and condition (challenge), provides a physically
defined “digital fingerprint” output (response) that serves as a unique

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **31**

identifier, most often for a semiconductor device such as a microprocessor [53].
b. Process specific functions (PSFs) which utilize a combination of the

process variation and quantization theory within the analog domain to
produce a statistically bounded uniqueness model [54].
2. One-time programmable features:
a. An eFUSE is a small, one-time programmable, non-volatile memory

element [55].
b. Read-only memory is a non-volatile memory element where the con
tents of the memory is programmed during the manufacturing process.
3. Privilege access features:
a. Privilege bits for elevated granular control of instructions within a siloed

execution environment.
4. Cryptographic encryption engines:
a. Hardware-based cryptographic engines provide accelerated encryption

and decryption functionality for in hardware execution.
5. Joint Test Action Group (JTAG) Protections:
a. Secure boot controlled enablement of the JTAG.
b. Dynamically obfuscated scan (DOS) reads control vectors from non
volatile memory in secure zones and provides limited scan access based
on keys [56].
6. Anti-tamper features:
a. A set of technologies that prevent the extraction of information from the

hardware via countermeasures.
b. For instance, circuit camouflage is used to obfuscate the hardware

netlist from reverse engineering attacks [57].
7. Embedded Field Programmable Gate Arrays (eFPGAs).
a. Advancements in FPGA technology have enabled coarse- and fine
grained on-chip embedded FPGAs.
b. This reprogrammable fabric provides a new security dimension where

the fabric can be statically reprogrammed or can context switch as desired.

These features are combined into a secure boot operation, which at power up,
is intended to ensure no unauthorized code will be executed before the boot process reaches the device owner’s code. The secure boot operation utilizes a form of
multifactor authentication using combinations of the available hardware to produce
something you know (read-only memory or eFUSE) and something you are (PUF
or Unique IDs) to establish the foundations of security. Once established, secure
operations then can utilize the cryptographic encryption engines to securely transfer information into or out of the hardware and elevate secure functions with privilege controls. JTAG protections and anti-tamper features are employed to ensure the
established secure state is not compromised. Ultimately, layering of these features
provides defense-in-depth, providing multiple layers of defense for the adversary to
circumvent prior to gaining access the internal resources of the system.

**32** Advances in Hardware Design for Security and Trust

**Figure 3.6** Microelectronics proactive design methodology.

**3.3** **THE COMMERCIAL APPROACH**

As shown in Figure 3.6, the commercial microelectronics design industry employees a proactive design methodology where tasks typically performed at the end of
the design process are integrated into early stages. Thus, enabling the identification
and resolution of bugs earlier in the development cycle leading to improved maturity
systems. In industry, this is widely referred to as the “shift left” methodology, first
introduced in 2001, as a solution to complex software development [58]. Here, the
intended application was to break the traditionally sequential steps of software design and test by introducing them earlier in the development cycle and then through
automation re-application. Today, this is often paired with “shift up” to indicate that
it extends beyond implementation and test into architecture and design. Additionally,
this compliments today’s hardware design processes that are becoming increasingly
analogous with agile design methodologies found in software development. The industries’ adoption of these practices is due to the enormity and complexity of modern
microelectronic systems that are driven by time to market and cost to develop. Today’s designers desire to have early visibility into functional flaws, security issues,
and effectiveness of countermeasures prior to widespread consumer release.

A deeper investigation into integrated circuit (IC) design and implementation,
specifically for digital systems, is necessary to gain additional insight into the various
layers of abstraction used in design and the associated transformations. A Y-diagram,
Figure 3.7 and developed by Daniel Gajski and Robert Kuhn in 1983, is a common
method to describe this design process and referenced in most VLSI courses [59–61].
Here, the Y-diagram separates the Function Behavioral Domain from the Form Structural Domain and the Geometric Physical Domain. Designs progress in a clockwise
fashion and iteratively repeat transitioning between each domain, and adding fidelity
down each axis until reaching the center:

1. Design starts at the abstract behavioral model describing the intended software and system functionality to be produced within the design. This forms
the basis of the system architecture and drives the subsequent domains
via transformation. In a 2018 paper, Khailany describes NVIDIA’s process
of using of higher-level languages (e.g., C++) to perform quick architectural trade space analysis in a “loosely timed” style while leveraging other

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **33**

**Figure 3.7** Y-diagram depicting the IC design process [59–61].

emerging technologies that raise the level of design abstraction beyond the
current state of practice [62, 63].
2. Additional model fidelity occurs within the structural domain where notional function mapping occurs to identify major block elements, such as
CPUs, memory, and I/O. Here, system target selection becomes important.
For instance, mapping to a FPGA, graphics processing unit, or custom integrated circuit are design decisions that may occur at this stage. Additional
considerations for von Neumann architectures and non-von Neumann architectures would occur here.
3. In the physical domain, those major elements are segmented into physical
partitions or across multiple chips. Here, selection of the technology node
to support the implementation would be performed.

Additions to the Y-diagram, highlighted in blue, are the security aspects of the
design process in relationship to the traditional design operations. With the secure
software driving parallel requirements to the user software for the architectural and
functional structural domain elements necessary for secure operation. The Geometrical Physical domain may now drive decisions related to anti-tamper, controlled
sources of manufacturing, and in-circuit camouflage. These design and architectural
choices are balanced against the system susceptibility, threat capability, and threat
access models.

This description shares common features with another common pictorial representation within the systems engineering community called the system V-diagram
(VEE-Diagram) or V-Model (Figure 3.8). Within this context the designs enter on
the leftmost leg, which describes requirement mapping and system decomposition

**34** Advances in Hardware Design for Security and Trust

**Figure 3.8** V-diagram for systems engineering.

while progressing towards a detailed design followed by system composition and
validation post-manufacturing. Both models offer a glimpse into the systems engineering processes necessary to produce complex systems.

Current industry trends better align with the system V-diagram, above, where the
system and operational endpoint drive the composition of the hardware and software. Classically, semiconductor companies would focus on purely the silicon hardware irrespective of the end application and producing generalized functional blocks
dictated by the semiconductor market. High-performance and advanced computing
leveraged general purpose processors to perform complex mathematical calculations.
New advanced computing implementations are driving the codesign of the software,
silicon, and composed system hardware to achieve new levels of performance. Traditionally, this type of optimization was reserved for specialized silicon hardware
where the performance gains outweighed the cost to develop a unique implementation. Examples of this level of optimization are graphics processing units wherein silicon hardware algorithm acceleration is necessary to achieve high data rate graphics
and FPGAs, where the fabric re-programmability, signal processing functions, and
associated FPGA programming stack are market differentiators. With today’s electronic design automation (EDA) tools and customizable processor IP (e.g., RISC-V),
designers are easily able to tailor and specialize their implementation for their marketplace. This opens up adjacent markets where systems and applications are the
market differentiator for system companies (Figure 3.9). System companies in the
high-tech, automotive, and defense verticals pursue the design and implementation
of capabilities in which electronics coexist with mechanical and electric systems and
desire to derive silicon specifications from this system and model the silicon within
the complete system. Some examples of systems influencing silicon are within the

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **35**

**Figure 3.9** Systems spectrum.

area of artificial intelligence where the algorithm and hardware must be codesigned
and vehicle electrification and autonomous driving require additional analysis and
redesign.

In this evolved system, design construct hardware security has evolved into separate domains of functional security, physical security, and cybersecurity. Each plays a
critical role in the system’s ability to achieve secure functionality and effective countermeasures. Illustrated in Figure 3.10, the functional, physical, and cyber-domains
address different aspects of secure operation. The functional security domain ensures
correct operation and addresses protections necessary for data at rest and in motion
in hardware. For instance, exposure of the systems private key in plain text on an
openly accessible port of the chip would be captured within this domain. The physical security domain addresses unintended information leakage through side-channel
analysis and physical probing to extract information. This ensures that the functional
security premises are not compromised through physical manifestation. Additionally, within this domain are notions of reliability and mechanical stability where an
adversary may seek to compromise the system via the systems integrity by inducing
failure modes that would cause complete system failure, early wear out, or sporadic
operation. In the cybersecurity domain, a set of established procedures is followed
to establish a secure foundation and achieve a secure state and subsequent operation
and dynamic responsive resilient operation to adversarial threats.

**3.3.1** **FUNCTIONAL DOMAIN: LEVERAGING EXISTING VERIFICATION**

Modern IC designs utilize multiple commercially available verification methods
to ensure system operation and achieve functional completeness. Today, no singular verification technique can cover the complete design state space. Industry has
adopted a total coverage score which is a summation of metrics from direct test,

**36** Advances in Hardware Design for Security and Trust

**Figure 3.10** Functional, physical, and cyber-domains.

random test, formal methods, emulation, and rapid prototyping. Each method partially contributes to covering the complete functional legal state space of the device
under test. Designer and verification team independence is crucial to successfully
identifying and remediating bugs, via bug burndown charts. Both teams operate from
the same initial specification, with the verification team creating comprehensive verification plans, testbench development, and running simulations to achieve verification coverage.

Security verification teams often draw from existing functional safety critical applications standards and EDA supplied verification IP to establish a baseline. These
standards-based compliance approaches allow for multiple vendor solutions to be
readily available for implementation. The verification teams have the responsibility to enhance the verification IP to match their total system, institute multiple tool
vendor and metric-driven verification processes, and produce thorough documentation while being receptive to evolving safety requirements and updates to safety
standards via a change management process or engineering change order (ECO).
Security-specific software utilize information flow control to track safety critical and
security information by tagging and tainting of secret data to ensure it is not leaked
to a harmful location. This gate-level information flow tracking technique (GLIFT)
tracks flow through gates by associating each data bit with a one-bit label, called

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **37**

taint, and tracking this label through the electronics hardware in simulation with additional tracking logic [64]. Outputs from this methodology can then be integrated
into the metric-driven verification flow. Other tools explore the application of game
theory to establish adversary and defensive outcomes to identify critical system elements where Trojans may exist. These games may be inclusive of on-chip, package,
or board vulnerabilities and countermeasures as well those that may be employed
across the entire life cycle. The benefit of this approach is “what-if” scenarios that
can be explained both mathematically and graphically [65]. Finally, advanced tailored security formal methods can formally prove the absence of entire classes of
security vulnerabilities. Through formal proofs one can identify multiple classes of
triggers, either sets of events and state activation, reliability issues, or deadlock conditions that could lead to denial-of-service (DoS) attacks [66].

A 2022 Wilson Research Group and Siemens EDA study indicates that the top
errors driving remanufacturing of integrated circuit hardware are logic and functionality, followed by analog function and power [67]. Of the survey responders, less than
10 percent identified safety or security as a driver for remanufacturing. In the same
report, the root cause of functional flaws was due to (1) design error, (2) incorrect or
incomplete specification, (3) changes in specification, and (4) flaws in IP (Internal
IP and External IP). Although security was not a primary root cause of failure, these
indicate that there are challenges with scaling verification to cover the entire system
leaving open misconfiguration in the design or specifications for an adversary to exploit. Also, these systems are assembled using 3PIP blocks, which are difficult to
ascertain the full gambit of functionality that resident.

Large-scale semiconductor and microelectronics manufacturers have dedicated
security teams to which advocate, design, and verify security of their microelectronics, working with customers on their implementation, and securing the supply
chain. For instance, Intel has a security-first approach intended to discover vulnerabilities prior to product delivery, employ an offensive research team to ensure a
robust security development life cycle, and actively perform company-wide vulnerability management within the product security incidence response team [68]. Cisco
has an Advanced Security Research, Security and Trust Organization which pursues
research in emerging threats and disruptive technologies through cyber-manipulation
with a focus on cryptography,privacy and analytics, systems integrity, and threat mitigation [69]. In comparison, Google promotes an open-source methodology with the
OpenTitan: open-source silicon root of trust (RoT) intended for data center servers,
storage, and peripherals [70].

**3.3.2** **PHYSICAL SECURITY: EARLY PREDICTIVE SIDE-CHANNEL ANALYSIS**

As the commercial industry continues to follow the shift-left shift-up objective, there
is a need to perform early predictive analysis of analog, digital power, thermal, and
electromagnetic side-channels and laser fault injection, illustrated in Figure 3.11, to
identify and mitigate vulnerabilities while employing effective countermeasures and
performing side-channel signoff. For instance, power side-channel leakage analysis can occur as early as the logic design level using register transfer level (RTL)

**38** Advances in Hardware Design for Security and Trust

**Figure 3.11** Side-channel predictive analysis.

**Figure 3.12** Design cycle completion through side-channel analysis sign-off.

information to represent the power and switching activity. Subsequent stages of circuit and physical design add additional fidelity to the power side-channel analysis
with gate-level information and physical placement. Additionally, as the design progresses towards the final implementation, other side-channel analysis become available to the designer; the results of various side-channel analyses are represented in
Figure 3.12. Culminating into a complete side-channel and design cycle analysis
sign-off methodology. Similar techniques can be applied to the chip, package, and
board to assess side-channel vulnerabilities at the system level. These side-channel
models are composed into a chip side-channel model for composable system security
analysis.

The side-channel analysis workflow, in Figure 3.13, utilizes a unified multiphysics
kernel to simultaneously calculate power current, magnetic field, and side-channel
leakage analysis (SCLA). The benefits of these methods are so it is not a struggle to
scale across small and complete systems on a chip analysis and minimize errors introduced by using a single domain concatenated flow. This flow is optimized for
collecting traces which are analyzed in the subsequent SCLA flow by using a
security-sensitive register extraction engine, an intelligent probe generation flow, and

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **39**

a fast simulation methodology called the direct vector control (DVC). In the subsequent SCLA stage, the side-channel leakage heatmap is produced to guide a designer
to find vulnerable spots, and also to expedite the adoption of countermeasures. SCLA
measures side-channel leakage metrics including T-score, side-channel leakage score
(SLS), and the number of measurement traces to disclosure (MTD), leveraged by a
secure system-on-chip (SoC) design flow toward side-channel attack resiliency and
side-channel leakage signoff.

1. Power SCLA features the tracking of security-sensitive registers within
cryptographic logic paths and the automatic assignments of probe points
on associated physical power nets.
2. Power supply current traces are efficiently simulated for the large set of
input payloads, with direct vector-based and vector-less random switching
controls.
3. EM SCLA evaluates magnetic fields created by every piece of metal wiring
in metal stacks where power supply current of cryptographic processing
flows.

Various attacks can then be explored:

1. Simple power analysis (SPA) and differential power analysis (DPA)
straightforwardly relate bit-wise operation with power supply current consumption of associated digital integrated circuits (ICs).
2. Correlation power analysis (CPA), an evolved DPA, assumes a side-channel
leakage model that is tailored for the given cryptography algorithm and
related to power supply current consumption of an IC chip.

This methodology enables a top-down cross-domain simulation approach that targets the system on a chip, featuring the logic-level tracking of security-sensitive parts
as well as the system-level location dependent power and EM side-channel analyses.

A comparison of the simulation and measurement heatmap of a backside electromagnetic side-channel analysis is illustrated in Figure 3.14. In simulation, there
are 1024 virtual probes that are evenly placed in simulation grids while in measurement nine probe points were used to in a 3×3 array configuration. Two-dimensional
B field heatmaps in the area of a BGA packaging interposer is shown in the figure.
The frequency components at the clock frequency of 30 MHz given to the AES core
are compared for the simulated B field and the measured voltage. In simulation, the
CPS model, including CPM of AES core and IO cells, produces the near-field EM
emission. In measurements, an EM probe is scanned over the packaging area and
measuring magnetic fields during AES operation. Qualitative heatmap observation
indicates good correlation between measurement and simulation. Subsequent trace
analysis shows the number of traces and mean time to disclose of the encryption keys
associated with the AES core [71, 72, 73, 74].

Alternatively, an optical side-channel leakage analysis workflow, in Figure 3.15,
is provided to illustrate the ability to capture device-level photon emissions for security verification and sign-off using the physical geometry and device channel current.

**40** Advances in Hardware Design for Security and Trust

**Figure 3.13** Side-channel analysis workflow.

Here, the intent is to model the optical side-channel attacks that capitalize on the
inadvertent emission of light during the operation of integrated circuits (e.g., cryptographic operations). During the attack procedure, adversaries measure the emitted
photons produced by the execution of cryptographic tasks, aiming to extract sensitive
data like secret encryption keys. Optical SCA is classified based on different methodologies: simple photonic emission analysis (SPEA), differential photonic emission
analysis (DPEA), and correlation-based photon emission analysis (CPEA). Similar
metrics of key disclosure, simulated MTD, and sensitivity scores are used to assess
and determine the effectiveness of countermeasures. A comparison of the simulation
and measured photo emission is in Figure 3.16. Here, an AES-128 bit encryption IP
block is simulated with 3000 photon emission images from 3000 plain texts and then
partitioned into pixel elements to represent the physical sensor, PHEMOS-1000, and
tile-based traces [75].

**3.4** **RESEARCH CHALLENGES**

The 2005Defense Science Board (DSB) Task Force report on high-performance microchip supply identified concerns with the U.S. national technology leadership due
to consolidation of commercial microelectronics suppliers and economic forces driving manufacturing relocation worldwide. The task force concluded that the DoD
requires trusted and assured supplies of IC components that are able to contain mission critical information without compromise, they are reliable, and do not contain
elements susceptible to exploitation to adversary agents. “Trust cannot be added to
integrated circuits after fabrication; electrical testing and reverse engineering cannot
be relied upon to detect undesired alterations in military integrated circuits” [76].
The DSB concerns were subsequently reinforced in the Institute of Electrical and

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **41**

**Figure 3.14** Comparison of EM simulation and measurement heatmaps.

Electronics Engineers (IEEE) 2008 article “the hunt for the kill switch” which postulated that the success of a 2007 Israeli airstrike was due to a hidden back door inside one of the Syrian radars which temporarily blocked critical detection functions

[77]. This was further exacerbated by the 2012 Senate Armed Services Report on
counterfeited electronics within the defense supply [46]. As a result, several research

**42** Advances in Hardware Design for Security and Trust

**Figure 3.15** Optical side-channel leakage analysis workflow.

initiatives were launched by the DARPA, Intelligence Advanced Research Projects
Activity (IARPA), and National Science Foundation (NSF) (Figure 3.17).

**3.4.1** **DARPA AND IARPA**

The DARPA and IARPA launched several programs to address confidentiality, integrity, and assurance of microelectronics (Figures 3.18 and 3.19).

These research endeavors aligned themselves to a taxonomy framework to address
loss of information,fraudulent products, loss of access, malicious insertion, and quality and reliability covering the spectrum of use models from bounded by high government intervention technologies to high commercial sponsorship. Research protections would pursue fine disaggregation and transience functional disaggregation,
obscuration and marking, verification and validation, and secure implementations
to achieve an asymmetric offset. These technologies would provide the government

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **43**

**Figure** **3.16** Simulated photon emission versus measure emission data captured by
PHEMOS-1000 [75].

**Figure 3.17** Summary of major research and emerging technology efforts related to
hardware security.

with a set of security options that could be selectively applied based on need.

1. Verification and Validation: Trusted Integrated Circuits (TRUST) and subsequent Integrity and Reliability of Integrated Circuits (IRIS) programs developed techniques for validating the design and process integrity before
distribution. The objective of the TRUST program was to use measurable
techniques and testing technologies to ensure U.S. weapons systems do not
contain malicious circuitry. While the IRIS program sought to develop nondestructive technologies to derive the functionality of digital, analog, and
mixed-signal integrated circuits within a operational envelope and extend
knowledge of the circuits integrity and reliability given a limited number of
samples, the Circuit Analysis Tools (CAT) program desired to advance the
state of the art for deep inspection of microelectronics devices through developing tools and techniques to improve analytical capability and metrology analysis. Rapid analysis of various emerging nanoelectronics developed technologies to accelerate the inspection processes, both destructive
and non-destructive, to assess manufacturing quality.

**44** Advances in Hardware Design for Security and Trust

**Figure 3.18** Global semiconductor industry.

**Figure 3.19** DARPA hardware security programs.

2. Obscuration and Marking: Supply Chain Hardware Integrity for Electronics Defense (SHIELD) program’s goal was to eliminate counterfeit electronics from the supply chain by dramatically increasing the cost to counterfeit through the use of an embedded dielet. The dielet, 100 um × 100

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **45**

um, would contain a passively powered highly integrated computer chip
that provide both a root of trust and root of authentication anywhere along
the supply chain. The Circuit Realization at Faster Timescales (CRAFT)
program targeted the acceleration of the design process and specialization of hardware to enable small teams to affordably produce custom integrated chips, providing a fast cost-effective way to establish supply chain
independence.
3. Functional Disaggregation (in processing or manufacturing): Secure Processing Architecture by Design (SPADE), and lead in-program Obfuscated
Manufacturing for GPS (OMG), was architected to help prevent and respond to threats such as malicious insertion of hardware trojans and reliability failures through the integration and use of high-performance commercial and trusted controlled semiconductor supplies utilizing a security dies as an interposer. Continuous-Correctness On Opaque Processors
(COOP) was intended to shift the paradigm from anti-threat to anti-error
using stable physics, via side channels, to guarantee computational correctness. Diverse Accessible Heterogeneous Integration (DAHI) demonstrated
processes that enabled transistor-scale heterogeneous integration to combine advanced compound semiconductor devices with high-density silicon
in a monolithic manufacturing environment. Whereas the Common Heterogeneous Integration and IP Reuse Strategies (CHIPS) program developed
methodologies for function block-level integration and the associated design tools and integration standards necessary to demonstrate modular integration.
4. Fine Grain Disaggregation and Transience: Trusted Integrated Chips (TICs)
evaluated protection techniques to split manufacture the front-end-of-line
(FEOL) at a state-of-the-art manufacturing node from the back-end-of-line
(BEOL) metallization performed in a controlled secure facility. The Vanishing Programmable Resources (VAPR) program sought to revolutionize the state of the art for transient and dissolvable electronics and perform with the functionality and ruggedness of conventional electronics until
triggered.
5. Secure Implementations: Automatic Implementation of Secure Silicon
(AISS) developed a novel automated chip design flow that allows security mechanisms to be evaluated using metric-driven quantification and then
scale across complex microelectronics systems. OMG developed technologies to lock, obfuscate, or redact critical IP during manufacturing, enabling
manufacturing of mission-sensitive chips within commercial state-of-theart foundries. Faithful Integration and Reverse-engineering and Emulation
(FIRE) developed tools to hypothesis and rationalize security for medium
complexity cyber-physical systems by identifying, exploiting, and patching vulnerabilities within the composed hardware, software, and physical
components.

**46** Advances in Hardware Design for Security and Trust

**3.4.2** **ACADEMIA AND NSF**

Other opportunities to participate in security research exist within the DoD’s Microelectronics Commons national innovation hub network addressing technical innovation challenges the inhibit transition from lab and fab. Specifically, the Secure
Edge and IoT computing technical area is pursuing the demonstration of mature
secure prototypes. Additionally, the National Science Foundations (NSF) IndustryUniversity Cooperative Research Centers Program (IUCRC) Center for Hardware
and Embedded System Security and Trust (CHEST) provides a pre-competitive environment to pursue research in identification, detection, monitoring, mitigating, and
elimination of vulnerabilities that affect hardware and embedded systems. Both utilize a public-private partnership to establish a long-term relationship between industry and government to pursue mutually beneficial innovations.

IEEE International Symposium on Hardware Oriented Security and Trust (HOST)
was formed in 2008 to provide a forum for systems security research to address
emerging vulnerabilities and defense mechanisms targeting hardware. Since inception, the HOST conference has continued to grow and expand the conference scope
to include all areas of overlap between hardware and security, and cybersecurity
bridging the gap between computer security, microelectronics, and electronic design
automation (EDA) communities. Similarly, the BlackHat conference traditionally focused on software cybersecurity attacks, mitigations, and vulnerability identification
has extended down to include hardware covering topics like Spectre, MeltDown, and
BroadPWN.

The emerging area of 3-dimensional integrated circuits (3DICs) are the next evolution of current 2.5-dimension (2.5D) systems. Driven by the industries’ desire to
continue pacing with Moore’s law, beyond transistor scaling, by achieving unparallel performance within a processing volume. Commercial industries will pursue
3D, homogeneous volumes for high-performance markets to manage cost, yield, and
process complexity through mapping of their IP-based architectures to tiers. Blocklevel placement allows existing architectures to be mapped to 3D volumes without
requiring redesign and optimization due to new technology manufacturing enablers.
However, this new paradigm offers new security opportunities and threats ripe for
investigation.

**3.5** **CONCLUSION**

The commercial industry operates within the existing standards to achieve market
compliance and industry differentiation and is motivated to change normal business practices when their brand name is jeopardized or market presence is impacted
by a security event. Unfortunately, standards often lag behind the current threat
and are not prescriptive. In general, the commercial industry is moving towards a
metric-driven risk-based quantification for security and encouraging the use of
security-specific software to assess early design vulnerabilities and evaluate mitigations. Ultimately, it is more challenging and costly to modify, fix, and patch

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **47**

hardware post-manufacturing due to the intricate physical nature of hardware, unless a software workaround can be issued.

**REFERENCES**

1. [https://www.semiconductors.org/2023-state-of-the-u-s-semiconductor-industry/](https://www.semiconductors.org/2023-state-of-the-u-s-semiconductor-industry)
2. [https://en.wikipedia.org/wiki/Fourth](https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution) Industrial Revolution
3. [https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-](https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883)
[a3a67f183883](https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883)
4. [https://www.nbcnews.com/business/business-news/target-settles-2013-hacked-](https://www.nbcnews.com/business/business-news/target-settles-2013-hacked-customer-data-breach-18-5-million-n764031)
[customer-data-breach-18-5-million-n764031](https://www.nbcnews.com/business/business-news/target-settles-2013-hacked-customer-data-breach-18-5-million-n764031)
5. [https://www.csis.org/programs/strategic-technologies-program/significant-cyber-](https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents)
[incidents](https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents)
6. [https://en.wikipedia.org/wiki/Modchip](https://en.wikipedia.org/wiki/Modchip)
7. [https://en.wikipedia.org/wiki/Row](https://en.wikipedia.org/wiki/Row_hammer) hammer
8. Y. Kim, R. Daly, J. Kim, C. Fallin, J. H. Lee, D. Lee, C. Wilkerson, K. Lai, and O.
Mutlu, “Flipping Bits in Memory Without Accessing Them: An Experimental Study
of DRAM Disturbance Errors,” ACM/IEEE 41st International Symposium on Computer
Architecture (ISCA), June, 2014.
9. [https://www.blackhat.com/docs/us-15/materials/us-15-Seaborn-Exploiting-The-](https://www.blackhat.com/docs/us-15/materials/us-15-Seaborn-Exploiting-The-DRAM-Rowhammer-Bug-To-Gain-Kernel-Privileges.pdf)
[DRAM-Rowhammer-Bug-To-Gain-Kernel-Privileges.pdf](https://www.blackhat.com/docs/us-15/materials/us-15-Seaborn-Exploiting-The-DRAM-Rowhammer-Bug-To-Gain-Kernel-Privileges.pdf)
10. [https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html)
[gain.html](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html)
11. [https://spectrum.ieee.org/how-the-spectre-and-meltdown-hacks-really-worked](https://spectrum.ieee.org/how-the-spectre-and-meltdown-hacks-really-worked)
12. [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
13. [https://blog.exodusintel.com/2017/07/26/broadpwn/](https://blog.exodusintel.com/2017/07/26/broadpwn)
14. [https://www.blackhat.com/docs/us-17/thursday/us-17-Artenstein-Broadpwn-Remotely-](https://www.blackhat.com/docs/us-17/thursday/us-17-Artenstein-Broadpwn-Remotely-Compromising-Android-And-iOS-Via-A-Bug-In-Broadcoms-Wifi-Chipsets-wp.pdf)
[Compromising-Android-And-iOS-Via-A-Bug-In-Broadcoms-Wifi-Chipsets-wp.pdf](https://www.blackhat.com/docs/us-17/thursday/us-17-Artenstein-Broadpwn-Remotely-Compromising-Android-And-iOS-Via-A-Bug-In-Broadcoms-Wifi-Chipsets-wp.pdf)
15. [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9417)
16. [https://heartbleed.com/](https://heartbleed.com)
17. [https://en.wikipedia.org/wiki/Heartbleed](https://en.wikipedia.org/wiki/Heartbleed)
18. [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160)
19. [https://www.pcmag.com/news/heartbleed-how-it-works](https://www.pcmag.com/news/heartbleed-how-it-works)
20. [https://www.datacenterdynamics.com/en/opinions/cybersecurity-a-heartbleed-deep-](https://www.datacenterdynamics.com/en/opinions/cybersecurity-a-heartbleed-deepdive)
[dive/](https://www.datacenterdynamics.com/en/opinions/cybersecurity-a-heartbleed-deepdive)
21. [https://www.wired.com/2016/06/demonically-clever-backdoor-hides-inside-computer-](https://www.wired.com/2016/06/demonically-clever-backdoor-hides-inside-computer-chip)
[chip/](https://www.wired.com/2016/06/demonically-clever-backdoor-hides-inside-computer-chip)
22. K. Yang, M. Hicks, Q. Dong, T. Austin, and D. Sylvester, “A2: Analog Malicious Hardware,” 2016 IEEE Symposium on Security and Privacy (SP), pp. 18–37, 2016.
23. [https://en.wikipedia.org/wiki/Electromagnetic](https://en.wikipedia.org/wiki/Electromagnetic_attack) attack
24. [https://www.cs.jhu.edu/∼astubble/600.412/s-c-papers/em.pdf](https://www.cs.jhu.edu/~astubble/600.412/s-c-papers/em.pdf)
25. [https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies)
[a-tiny-chip-to-infiltrate-america-s-top-companies](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies)
26. [https://www.bloomberg.com/features/2021-supermicro/](https://www.bloomberg.com/features/2021-supermicro)
27. [https://rais.education/wp-content/uploads/2023/12/0319.pdf](https://rais.education/wp-content/uploads/2023/12/0319.pdf)
28. [https://semiengineering.com/the-threat-of-supply-chain-insecurity/](https://semiengineering.com/the-threat-of-supply-chain-insecurity)
29. [https://www.dhs.gov/sites/default/files/2023-09/23](https://www.dhs.gov/sites/default/files/2023-09/23_0915_oia_CCM_White_Paper_508_final.pdf) 0915 oia CCM White Paper 508 final.pdf

**48** Advances in Hardware Design for Security and Trust

30. [https://spectrum.ieee.org/invasion-of-the-hardware-snatchers-cloned-electronics-](https://spectrum.ieee.org/invasion-of-the-hardware-snatchers-cloned-electronics-pollute-the-market)
[pollute-the-market](https://spectrum.ieee.org/invasion-of-the-hardware-snatchers-cloned-electronics-pollute-the-market)
31. [https://smtcorp.com/wp-content/uploads/2023/05/Growing-Threat-of-Counterfeit-](https://smtcorp.com/wp-content/uploads/2023/05/Growing-Threat-of-Counterfeit-Electronic-Parts-in-the-Critical-Infrastructure-Supply-Chain-Releasable-1.pdf)
[Electronic-Parts-in-the-Critical-Infrastructure-Supply-Chain-Releasable-1.pdf](https://smtcorp.com/wp-content/uploads/2023/05/Growing-Threat-of-Counterfeit-Electronic-Parts-in-the-Critical-Infrastructure-Supply-Chain-Releasable-1.pdf)
32. https://nepp.nasa.gov/docs/etw/2010/08 [Hughitt](https://nepp.nasa.gov/docs/etw/2010/08_Hughitt_Counterfeit%20Electronics%20-%20All%20the%20World%27s%20a%20Fake.pdf) Counterfeit%20Electronics%20[%20All%20the%20World%27s%20a%20Fake.pdf](https://nepp.nasa.gov/docs/etw/2010/08_Hughitt_Counterfeit%20Electronics%20-%20All%20the%20World%27s%20a%20Fake.pdf)
33. [https://btlj.org/data/articles2015/vol7/7](https://btlj.org/data/articles2015/vol7/7_1/7-berkeley-tech-l-j-0071-0106.pdf) 1/7-berkeley-tech-l-j-0071-0106.pdf
34. [https://en.wikipedia.org/wiki/Semiconductor](https://en.wikipedia.org/wiki/Semiconductor_Chip_Protection_Act_of_1984#:¡«:text=The%20Semiconductor%20Chip%20Protection%20Act,illegal%20to%20copy%20without%20permission) Chip Protection Act of 1984#:∼:text=
[The%20Semiconductor%20Chip%20Protection%20Act,illegal%20to%20copy](https://en.wikipedia.org/wiki/Semiconductor_Chip_Protection_Act_of_1984#:¡«:text=The%20Semiconductor%20Chip%20Protection%20Act,illegal%20to%20copy%20without%20permission)
[%20without%20permission.](https://en.wikipedia.org/wiki/Semiconductor_Chip_Protection_Act_of_1984#:¡«:text=The%20Semiconductor%20Chip%20Protection%20Act,illegal%20to%20copy%20without%20permission)
35. [https://nvd.nist.gov/](https://nvd.nist.gov)
36. [https://nvd.nist.gov/general/brief-history](https://nvd.nist.gov/general/brief-history)
37. [https://nvd.nist.gov/general/cve-process](https://nvd.nist.gov/general/cve-process)
38. [https://en.wikipedia.org/wiki/ISO](https://en.wikipedia.org/wiki/ISO_26262) 26262
39. [https://en.wikipedia.org/wiki/Information](https://en.wikipedia.org/wiki/Information_security_standards) security standards
40. [https://en.wikipedia.org/wiki/DO-254](https://en.wikipedia.org/wiki/DO-254)
41. [https://en.wikipedia.org/wiki/IEC](https://en.wikipedia.org/wiki/IEC_62443) 62443
42. [https://en.wikipedia.org/wiki/IP-XACT](https://en.wikipedia.org/wiki/IP-XACT)
43. [https://www.accellera.org/downloads/standards/ip-security-assurance](https://www.accellera.org/downloads/standards/ip-security-assurance)
44. [https://www.accellera.org/resources/videos/saedi-workshop-2021](https://www.accellera.org/resources/videos/saedi-workshop-2021)
45. T. Kaiser, “SAS committee: Counterfeit electronics from China could be harmful
to military,” 736792344Online736792344CECE7367923441205121821Author: Please
add URL., DailyTech, November, 2011.
46. [https://www.armed-services.senate.gov/imo/media/doc/SASC-Counterfeit-Electronics-](https://www.armed-services.senate.gov/imo/media/doc/SASC-Counterfeit-Electronics-Report-05-21-12.pdf)
[Report-05-21-12.pdf](https://www.armed-services.senate.gov/imo/media/doc/SASC-Counterfeit-Electronics-Report-05-21-12.pdf)
47. [https://www.dau.edu/acquipedia-article/counterfeit-parts](https://www.dau.edu/acquipedia-article/counterfeit-parts)
48. [https://www.dsp.dla.mil/Programs/GIDEP/](https://www.dsp.dla.mil/Programs/GIDEP)
49. [https://www.gidep.org/home](https://www.gidep.org/home)
50. [https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/520049p.PDF?ver=](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/520049p.PDF?ver=zl8 zpWdSNJCvTJqVJakXA%3d%3d)
zl8 [zpWdSNJCvTJqVJakXA%3d%3d](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/520049p.PDF?ver=zl8 zpWdSNJCvTJqVJakXA%3d%3d)
51. [https://nvlpubs.nist.gov/nistpubs/ir/2017/NIST.IR.8183.pdf](https://nvlpubs.nist.gov/nistpubs/ir/2017/NIST.IR.8183.pdf)
52. J. Hughes and G. Cybenko, “Quantitative Metrics and Risk Assessment: The Three
Tenets Model of Cybersecurity,” Technology Innovation Management Review, August,
2013.
53. [https://www.synopsys.com/glossary/what-is-a-physical-unclonable-function.html](https://www.synopsys.com/glossary/what-is-a-physical-unclonable-function.html)
54. M. Casto, B. Dupaix, P. L. Orlando, and W. Khalil, “Process Specific Functions for
Assurance of Analog/Mixed-Signal Integrated Circuits,” 2019 IEEE 62nd International
Midwest Symposium on Circuits and Systems (MWSCAS), pp. 456–459, 2019.
55. [https://docs.amd.com/r/en-US/ug1085-zynq-ultrascale-trm/PS-eFUSEs](https://docs.amd.com/r/en-US/ug1085-zynq-ultrascale-trm/PS-eFUSEs)
56. X. Wang, D. Zhang, M. He, D. Su, and M. Tehranipoor, “Secure Scan and Test Using
Obfuscation Throughout Supply Chain,” IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems, vol. 37, no. 9, pp. 1867–1880, September, 2018.
57. R. P. Cocchi, J. P. Baukus, L. W. Chow, and B. J. Wang, “Circuit camouflage integration
for hardware IP protection,” 2014 51st ACM/EDAC/IEEE Design Automation Conference (DAC), San Francisco, CA, pp. 1–5, 2014.
58. L. Smith, “Shift left Testing,” Dr. Dobb’s, September, 2001.
59. [https://en.wikipedia.org/wiki/Gajski%E2%80%93Kuhn](https://en.wikipedia.org/wiki/Gajski%E2%80%93Kuhn_chart) chart
60. G¨oran Herrman, Entwurf und Technologie von Mikroprozessoren. In Thomas Beier

A Commercial EDA Perspective on Hardware Security, Safety, and Trust **49**

lein and Olaf Hagenbruch, editors, Taschenbuch Mikroprozessortechnik, pp. 357–359,
M¨unchen/Wien, 1999.
61. Neil Weste and David Harres, CMOS VLSI Design: A Circuits and Systems Perspective,
4th edition, Pearson, 2010.
62. B. Khailany, et al., “INVITED: A Modular Digital VLSI Flow for High-Productivity
SoC Design,” 2018 55th ACM/ESDA/IEEE Design Automation Conference (DAC), San
Francisco, CA, USA, pp. 1–6, 2018.
63. [https://eri-summit.darpa.mil/docs/Khailany](https://eri-summit.darpa.mil/docs/Khailany_Brucek_CRAFT_Final.pdf) Brucek CRAFT Final.pdf
64. [https://cseweb.ucsd.edu/∼jkoberg/pubs/oberg](https://cseweb.ucsd.edu/%E2%88%BCjkoberg/pubs/oberg_tcad_14.pdf) tcad 14.pdf
65. J. Graf, W. Batchelor, S. Harper, et al., “A practical application of game theory to optimize selection of hardware Trojan detection strategies,” Journal of Hardware Systems
Security, vol. 4, pp. 98–119, 2020.
66. [https://semiengineering.com/trust-is-not-a-good-feeling/](https://semiengineering.com/trust-is-not-a-good-feeling)
67. [https://blogs.sw.siemens.com/verificationhorizons/2023/01/09/part-12-the-2020-](https://blogs.sw.siemens.com/verificationhorizons/2023/01/09/part-12-the-2020-wilson-research-group-functional-verification-study-2)
[wilson-research-group-functional-verification-study-2/](https://blogs.sw.siemens.com/verificationhorizons/2023/01/09/part-12-the-2020-wilson-research-group-functional-verification-study-2)
68. [https://www.intel.com/content/www/us/en/security/intel-2023-product-security-](https://www.intel.com/content/www/us/en/security/intel-2023-product-security-report.html)
[report.html](https://www.intel.com/content/www/us/en/security/intel-2023-product-security-report.html)
69. https://www.cisco.com/c/dam/en [us/solutions/industries/docs/education/ub-](https://www.cisco.com/c/dam/en_us/solutions/industries/docs/education/ub-cybersecurity-research.pdf)
[cybersecurity-research.pdf](https://www.cisco.com/c/dam/en_us/solutions/industries/docs/education/ub-cybersecurity-research.pdf)
70. [https://opensource.googleblog.com/2019/11/opentitan-open-sourcing-transparent.html](https://opensource.googleblog.com/2019/11/opentitan-open-sourcing-transparent.html)
71. K. Monta, L. Lin, J. Wen, H. Shrivastav, C. Chow, H. Chen, J. Geada, S. Chowdhury, N.
Pundir, N. Chang, and M. Nagata. “Silicon-correlated Simulation Methodology of EM
Side-channel Leakage Analysis,” ACM Journal of Emerging Technologies in Computing
Systems, vol. 19, pp. 1–23, January, 2023.
72. L. Lin, et al., “Layout-level Vulnerability Ranking from Electromagnetic Fault Injection,” 2022 IEEE International Symposium on Hardware Oriented Security and Trust
(HOST), McLean, VA, USA, pp. 17–20, 2022.
73. N. Chang, et al., “ML-augmented Methodology for Fast Thermal Side-channel Emission Analysis,” 2021 26th Asia and South Pacific Design Automation Conference (ASPDAC), Tokyo, Japan, pp. 463–468, 2021.
74. L. Lin, et al., “Multiphysics Simulation of EM Side-Channels from Silicon Backside
with ML-based,” 2021 IEEE International Symposium on Hardware Oriented Security
and Trust (HOST), Tysons Corner, VA, USA, pp. 270–280, 2021.
75. H. Li, et al., “Photon Emission Modeling and Machine-Learning Assisted Pre-Silicon
Optical Side-Channel Simulation,” 2024 IEEE International Symposium on Hardware
Oriented Security and Trust (HOST), Tysons Corner, VA, USA, pp. 107–111, 2024.
76. [https://dsb.cto.mil/wp-content/uploads/dsb/site/wwwroot/reports/2000s/ADA435563.pdf](https://dsb.cto.mil/wp-content/uploads/dsb/site/wwwroot/reports/2000s/ADA435563.pdf)
77. S. Adee, “The hunt for the kill switch,” Institute of Electrical and Electronic Engineers
(IEEE) Spectrum, May, 2008.

# 4 Machine Learning
### Techniques for Detecting Hardware Trojans in ASIC Designs

Kevin Immanuel Gubbi, Banafsheh Saber Latibari, Setareh Rafatirad, Avesta Sasan, Soheil
Salehi, and Houman Homayoun

As integrated circuit (IC) design and development become increasingly globalized,
the number of design houses and designers continues to grow. Establishing a fabrication facility is a capital-intensive endeavor, often exceeding $20 billion, with costs
for advanced nodes even higher. Consequently, many IC design houses, lacking inhouse manufacturing capabilities, are compelled to rely on external foundries, which
are frequently located in other countries. Trusting these external foundries poses significant challenges, especially when they are considered untrusted. This reliance on
untrusted foundries within the global semiconductor supply chain has sparked serious concerns regarding the security of ICs, particularly those destined for sensitive
applications.

One of the primary security risks is the insertion of hardware Trojans (HTs) into
fabricated ICs. An HT refers to a malicious alteration of a circuit designed to control, modify, disable, or monitor its logic. Traditional very large scale integration
(VLSI) manufacturing tests and verification methods often fail to detect HTs due
to the unconventional and unmodeled nature of these modifications. The complexities in secure embedded system design were highlighted in the 2004 publication [1],
where several challenges, including processing gap, battery gap, flexibility, tamper
resistance, assurance gap, and cost, were discussed.

Current advanced HT detection techniques employ statistical analysis of various
side-channel information extracted from ICs, such as power analysis [2], transient
power supply analysis [3], regional supply current analysis [4], temperature monitoring [5], wireless transmission power analysis [6], and delay analysis [7–12].
Typically, these methods necessitate a Trojan-free reference, or “golden,” IC. Signatures derived from these golden ICs are used to identify those tainted with HTs.

[DOI: 10.1201/9781003510949-4](https://doi.org/10.1201/9781003510949-4) **50**

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **51**

However, obtaining a golden IC is not always practical. In many cases, especially
with advanced technology nodes, there are only a limited number of foundries available, none of which can be considered fully trustworthy. Even if a reliable foundry
were available, the cost of fabricating a small batch of ICs to identify a golden IC is
typically prohibitive [13]. Furthermore, a golden IC produced in one foundry cannot
be used to evaluate ICs fabricated in another, due to significant differences in each
foundry’s manufacturing processes.

Given these challenges, there is a pressing need for HT detection mechanisms that
do not rely on a golden IC. Machine learning (ML) has emerged as a powerful tool
to address this challenge, offering solutions that eliminate the dependency on golden
ICs. Recent studies have demonstrated the promise of ML in HT detection, making
significant strides toward this goal. The unique and unmodeled characteristics of HTs
render traditional VLSI test and verification processes ineffective in their detection.
This challenge has driven researchers to explore alternative methods for HT detection
through the statistical analysis of side-channel data collected from ICs.

This work introduces a novel approach that eliminates the need for a golden IC
or model by developing and training a learning-assisted timing-adjustment model
integrated with static timing analysis (STA). This model acts as a surrogate for the
traditional golden model, enabling effective HT detection without relying on a reference IC. Our methodology draws inspiration from prior research, including the sidechannel power analysis in [13] and the side-channel delay analysis in [12]. However,
it significantly advances these techniques by overcoming the limitations associated
with previous methods that required larger HTs or the use of process control monitors (PCMs). Unlike the side-channel delay analysis method in [12], which depends
on the clock frequency sweeping test (CFST) and necessitates a golden IC for delay comparison, our approach generates label data points for each feature set using
CFST, thereby allowing for the detection of even a single added logic gate within a
timing path without the need for a golden IC. This book chapter explains and contributes the following:

1. An ML-based HT detection method that does not require a golden IC, addressing a significant limitation of traditional detection techniques.
2. An electronic design automation (EDA) tool flow that automates the process of ML-assisted HT detection, streamlining the implementation for
practical use in secure IC design, security verification, and testing.
3. A neural network-based timing profiling method that improves the sensitivity of HT detection, capable of identifying even minimal modifications,
such as the addition of a single logic gate within a timing path.

**4.1** **HT BENCHMARKS AND TAXONOMY**

In the last decade, research into HTs has seen a significant increase. However,
it was not until the work presented in [14, 15] that a standardized set of benchmarks for evaluating HTs and their detection methods was developed. The authors

**52** Advances in Hardware Design for Security and Trust

**Figure** **4.1** Hardware Trojans can be classified into different categories based on
their characteristics, insertion phase, abstraction level, activation mechanism, effect,
and location.

created a comprehensive resource suite containing known HTs and “trust benchmarks”—benchmark circuits with HTs embedded—that researchers can use to evaluate various HT detection techniques. Their work provides a detailed vulnerability
analysis flow to generate these trust benchmarks at different levels of abstraction in
digital design, as illustrated in Figure 4.2. Additionally, they offer an in-depth analysis of their benchmarks, focusing on metrics such as HT detectability and considering
various attack strategies. These HT benchmark suites are available on the Trust-Hub
website [14].

Some of the key challenges that motivated the creation of this HT benchmarking
effort, as highlighted in [15], include:

 - Ad-Hoc Trojans: Prior to the availability of a standardized benchmark
suite, researchers often relied on custom-designed HTs to demonstrate the
effectiveness and accuracy of their proposed detection methods. While
these HTs might be tailored to a specific detection technique, their performance could vary significantly when tested with other detection methods. Consequently, there was no consistent baseline for comparing different detection techniques, and it was unclear whether these custom HTs met
the essential criteria of being undetectable by conventional manufacturing
tests, including functional, structural, and fault-based checks.

 - Varying Assumptions: The environment for simulation and implementation, as well as factors such as process variation tolerance, HT triggering
difficulty, HT switching activity, and design size (number of gates, HT size,
etc.), differed significantly across different detection methods. This variation made it challenging to compare the effectiveness of different HT detection techniques.

 - Ad-Hoc Metrics: Researchers have employed various ad-hoc metrics to
evaluate detection techniques. Some focus on false positive/false negative
rates, others on test coverage, and still others on arbitrary detection percentages. Even when using the same HT attack model, comparing different
methods with these disparate metrics proved difficult.

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **53**

**Figure 4.2** Taxonomy of a hardware Trojan (HT) – HT triggers are used to activate
the trigger circuit, and the HT payload is deployed on the victim net/node when the
HT is activated.

**4.1.1** **HT THREAT MODEL**

This section provides a brief overview of the IC supply chain and discusses the HT
threat model. The traditional IC supply chain model along with the associated HT
threats is illustrated in [16]. Once the design specifications are finalized by the chip
architects, the design process is handed over to the appropriate design teams. Most
design houses incorporate third-party IPs (3PIP), third-party EDA tools or vendors
(3P-EDA), and external design expertise throughout the IC design and implementation phases. Multiple HT security vulnerabilities exist throughout the IC supply
chain. The most common insertion point is at the untrusted fabrication facility, where
an adversary could modify the lithography masks to maliciously alter the IC. Other
potential threats include HT insertion by 3PIPs, 3P-EDA vendors, and rogue designers. This threat model assumes that the untrusted foundry is the adversary with access
to the GDSII files, and HTs could potentially be inserted into every IC produced.

The adversary’s goal is to embed an HT that is triggered by a combination or
sequence of unusual events. Figure 4.1 shows the components of an HT: 1) Trojan
trigger inputs (TT); 2) Trojan triggering circuit (TTC), which can be either sequential
or combinational; and 3) Trojan payload (TP). Upon activation, the TP alters the
circuit’s operation. Another assumption is that the design house has access to a secure
testing facility for HT detection, without relying on a golden IC.

**4.1.2** **CURRENT STATE OF THE ART IN HT DETECTION**

Researchers have explored various methods for detecting HTs by analyzing statistical
side-channel information collected from ICs. Some of these side channels include:

 - Side-Channel Power Analysis

 - Power Supply Transient Signal Analysis

 - Regional Supply Current Analysis

 - Temperature Analysis

 - Wireless Transmission Power Analysis

 - Side-Channel Delay Analysis

**54** Advances in Hardware Design for Security and Trust

Many of these detection methods depend on a “golden” model or golden ICs,
which are fabricated in a trusted facility and are free of HTs. A signature from these
golden ICs is extracted and used to identify ICs compromised with HTs. While using
golden ICs as a reference has proven effective in enhancing the HT detection process,
fabricating these golden ICs is challenging. The design house must either have an inhouse foundry or access to a trusted foundry, both of which are difficult to achieve.

**4.2** **CHALLENGES IN HARDWARE TROJAN DETECTION**

This section outlines some of the key challenges associated with detecting HTs. Although the TP in the studied Trojans introduces at least one gate delay to the victim’s
timing path, the TT adds an additional capacitive load to the driving cell, resulting in
slower rise and fall times. It is important to note that the added delay could exceed
a single gate, especially in cases where a large and complex TC impacts the timing
path containing the TP. This can occur if the combined worst-case delay of the trigger sub-path and TC exceeds the delay of the sub-path leading to the TP. However,
for a more challenging scenario, this work assumes a small TC, limiting the delay
increase in the timing path hosting the TP to a single gate delay.

Our ML-based hardware trojan detection scheme, (which will be discussed in
detail in subsequent sections), is based on side-channel delay analysis. It identifies
HTs by tracking and analyzing changes in the delay of tested timing paths. Unlike
other methods, our scheme does not require a golden IC; instead, it utilizes the timing model generated through STA during the design phase. However, the delay data
from STA can significantly differ from the actual delay measured during testing. This
discrepancy arises due to the conservative margins applied when generating GDSII
files, which account for various sources of variability, including process variation
and process drift. The following subsections will explore these sources of variation
and how they can be exploited by adversaries to insert stealthy HTs. Later, we will
discuss how modeling these variations can enhance the likelihood of detecting HTs
by mitigating or accounting for their impact.

**4.2.1** **PROCESS VARIATION**

Random process variation refers to the inconsistencies in the physical and electrical
properties of transistors due to the inherent limitations of the fabrication process.
This variation affects the delay and drive strength of the fabricated transistors, complicating HT detection as test engineers must distinguish between delays caused by
random process variation and those induced by an HT.

**4.2.2** **PROCESS DRIFT**

Standard cell libraries used by physical design teams are characterized using SPICE
models based on the manufacturing process at a new technology node, typically
made available once the process reaches a certain level of stability. To ensure high
yield, these SPICE models and standard cell libraries are padded with conservative

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **55**

margins. Over time, foundries update the process by introducing new and improved
stepping devices to increase yield and reduce costs. This leads to a divergence between the actual manufacturing process and the published SPICE model over time.
As a result, an IC manufactured using an outdated SPICE model may have significant
unused timing slack due to process improvements. This situation presents a security
risk, as an attacker in an untrusted foundry could exploit this hidden slack to insert
stealthy HTs.

**4.2.3** **VOLTAGE NOISE**

The power delivery network (PDN), an RLC network on an ASIC chip, responds
to changes in the current demands of transistors by causing voltage (IR) drops and
voltage variations across the transistors [17]. When modeling IR drops and voltage
noise during STA, two steps are typically taken: (1) setting a rail voltage value lower
than the supplied voltage to account for IR drops, and (2) applying uncertainty at the
register endpoints to prevent clock network issues caused by voltage variations. Pessimistic values for rail voltage and uncertainty are used to prevent setup/hold failures
under worst-case scenarios. Voltage noise and IR drops are usually less problematic
for timing paths. However, this introduces a security risk because test engineers and
physical designers may be unaware of the significant timing slack that exists in most
timing paths due to these conservative margins. A malicious actor in an untrusted
foundry could exploit this slack to insert an HT and conceal its delay impact.

**4.3** **ML-BASED HT DETECTION**

This section explores the rationale for using ML in HT detection and provides an
overview of previous works that leverage various ML algorithms for this purpose.

**4.3.1** **WHY IS ML ESSENTIAL FOR HT DETECTION?**

Detecting HTs using traditional testing methods presents several challenges:

1. ICs today are not only highly complex but also incredibly large, making
manual inspection or traditional detection methods inadequate.
2. HTs are often designed to be small and stealthy, complicating detection
efforts.
3. Identifying HTs during the design phase is crucial to avoid costly and potentially catastrophic consequences later in the IC life cycle.
4. There is a pressing need to reduce the overall cost associated with HT detection, particularly as the scale and complexity of ICs continue to grow.

To address these challenges, ML approaches such as regression, deep neural networks, graph neural networks, and reinforcement learning can be employed to automate the detection process. HTs exhibit specific features that can be used as inputs
to ML models for detection. ML-based HT detection typically involves two main

**56** Advances in Hardware Design for Security and Trust

phases: the learning phase and the detection phase [18]. Before delving into a pathdelay-based Trojan detection method, we provide an overview of the current state of
the art in ML.

**4.3.2** **OVERVIEW OF ML METHODS AND ALGORITHMS**

ML is a process of learning from experience, requiring a substantial amount of data
as input to build a learning model. The ML process generally consists of two primary
steps: model training and prediction. Figure 4.3 illustrates the current state-of-theart ML approaches, which can be broadly categorized into four groups: supervised,
semi-supervised, unsupervised, and reinforcement learning.

 - Supervised Learning: This approach uses labeled input-output pairs to train
a model that maps inputs to desired outputs, aiming to produce outputs that
match the class labels.

 - Semi-Supervised Learning: This technique combines both labeled and unlabeled data sets for model training, leveraging the available labeled data
while utilizing the unlabeled data to improve learning accuracy.

 - Unsupervised Learning: Unsupervised ML works with untagged data to
identify underlying patterns or models that predict input data without predefined labels.

 - Reinforcement Learning: In RL, an agent interacts with a problem space
by performing actions and receiving feedback from the environment, with
the goal of maximizing cumulative rewards.

Notable ML models include K-means and generative adversarial networks
(GANs) from supervised learning; Bayesian networks and genetic algorithms from
the semi-supervised group; random forest, regression, and deep learning methods from the unsupervised group; and Q-learning, state-action-reward-state-action
(SARSA), and Actor-Critic as prominent RL-based algorithms.

**4.3.3** **REVIEW OF PREVIOUS ML-BASED HT DETECTION METHODS**

Figure 4.3 provides an overview of ML model used in HT detection methods, which
can be categorized into the following groups:

**4.3.3.1** **Netlist-Based Classification Approaches**

These methods classify design nets as either Trojan or non-Trojan. In [18], the authors proposed a gate-level HT classification method using support vector machines
(SVMs) and neural networks (NNs) to detect HT nets. They extracted five features
and represented them as a five-dimensional vector. In [19], they introduced 51 HT
features and used a random forest to identify the 11 most important features, improving their ML-based HT classifier.

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **57**

**Figure 4.3** Overview of ML algorithms classified under four categories – supervised,
unsupervised, semi-supervised, and reinforcement learning.

**4.3.3.2** **Reverse Engineering–Based Approaches**

Reverse engineering for HT detection involves five steps: 1) decapsulation, 2) delayering, and 3) imaging for layout identification, followed by two final stages that

**58** Advances in Hardware Design for Security and Trust

extract the netlist. In [20], a one-class SVM was used for HT detection based on reverse engineering, where features were extracted directly from IC images, bypassing
the need for netlist extraction. In [21], the authors automated layout identification
using a histogram of oriented gradients to extract circuit layout features, which were
then fed into a decision tree classifier enhanced by AdaBoost, leading to the creation
of the automatic HT detection and description tool (AHTDT). In [22], HT detection
was framed as a clustering problem using K-means clustering. This approach divided
the layout image into grids, extracted features from each grid, and grouped them into
clusters using K-means.

**4.3.3.3** **Golden Model–Free Approaches**

Golden models are costly, so methods in this category aim to eliminate the need for
them in Trojan detection. In [23], the authors proposed COTD, which uses controllability and observability metrics, coupled with K-means clustering, to classify signals
into Trojan-inserted and Trojan-free groups. In [24], HT detection was formulated
as a two-class classification problem using the transient power of simulated ICs for
model training, avoiding the need for real-time HT behavior. This work explored
different regression algorithms and adaptive iterative optimization to handle process
variations and improve detection accuracy.

**4.3.3.4** **LASCA**

The authors in [25] introduced learning assisted side channel delay analysis
(LASCA), which employs a neural network as a process-tracking watchdog. LASCA
correlates static timing data from the design phase with delay data extracted during
clock frequency sweeping in testing to detect HTs. The method addresses the impact
of voltage noise, process variation (PV), and process drift to enhance the correlation
between the timing model and IC behavior. They modeled process drift using a NN
watchdog that predicts differences between slack reported by STA at design time
and the slack extracted from the IC at test time. To mitigate PV, they categorized
it into two classes: random (independent intra-die variation) and persistent (interdie and correlated intra-die variation), employing speed binning and averaging delay
data across ICs to reduce randomness. Voltage noise was modeled using the IR-ATA
methodology. AVATAR [26], an extension of LASCA, will also be discussed where
relevant in this tutorial.

**4.3.3.5** **Deep Learning–Based Approaches**

In HERO [27], the authors proposed a comprehensive HT detection solution using a deep neural network (DNN) model that leverages features generated at various stages of manufacturing, from design to post-silicon verification, across different benchmarks. HERO’s pipeline integrates and standardizes these diverse data
sources into a uniform format (single-channel images) for DNN application, allowing the use of pre-trained deep convolutional networks. Data augmentation was
employed to address data set imbalance. HERO incorporates several HT detection

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **59**

techniques, including gate-level netlist analysis, placement and routing (PNR), and
SCA. In [28, 29], the authors used a graph data structure to represent hardware designs and generated data flow graphs (DFGs) for both RTL codes and gate-level
netlists. They then applied graph neural networks (GNNs) for Trojan detection, involving three main steps: 1) DFG extraction, 2) graph learning and feature extraction with GNN, and 3) classification using a multi-layer perceptron (MLP). In [30],
the authors combined generative adversarial networks (GANs) with stacked autoencoders (SAEs) for HT detection, using GANs for data pre-processing to generate
balanced fake samples, followed by SAE for classification.

**4.3.3.6** **Reinforcement Learning (RL) for HT Detection**

In [31], the authors presented AdaTest, an adaptive test pattern generation framework for HT detection that is scalable and resistant to noise and variation. AdaTest
utilizes RL to generate test inputs and adaptive sampling to prioritize the most informative test samples for HT detection. The AdaTest framework consists of two main
phases: 1) circuit profiling, where each design node is characterized based on transition probability and Sandia controllability/observability analysis program (SCOAP)
testability, and 2) adaptive test pattern generation, which uses a reward function to
prioritize nodes based on their rarity and testability, as well as the graph-level distance within the circuit. AdaTest also incorporates hardware acceleration through
pipelined computation and circuit emulation to speed up reward evaluation.

**4.4** **ML-BASED HT DETECTION IMPLEMENTATION**

In our detection model, we assume that the adversary is an untrusted foundry with
access to the graphic database system (GDSII) format of the design. The adversary’s
goal is to insert a HT that is triggered by a specific combination or sequence of rare
events. We assume the HT has several triggers and at least one payload, although our
detection solution is also applicable to HTs with no payload (designed for monitoring
purposes). Additionally, we assume the same HT is inserted in all fabricated dies and
that the foundry can manipulate the process (e.g., making transistors faster) to create
timing slack for HT insertion without increasing the overall delay beyond what is
reported or expected by static timing analysis (STA) during the design phase. HT detection in our approach is conducted at a trusted facility. The overarching scheme of
most ML schemes including training and inference/classification is shown in Figure
4.4.

**4.4.1** **CLOCK FREQUENCY SWEEPING TEST (CFST)**

Frequency sweep tests, a well-known technique in analog electronics, are used to
analyze how various circuit components affect a monochromatic input signal. The
input signal’s frequency is swept across a desired range, and the output voltage or
current is measured at each frequency. Phase shifts introduced by reactive components are also recorded along with the output. In [32], researchers first demonstrated

**60** Advances in Hardware Design for Security and Trust

**Figure 4.4** Overview of ML-based HT detection flow. The training stage has feature
extraction and ML training, and the classification stage has feature extraction and
classification.

path delay analysis for uniquely identifying ICs, and in [12], CFSTs were used for
HT detection.

**4.4.2** **HT DETECTION FLOW**

Figure 4.5 illustrates the overall flow of the ML-based hardware detection process.
The design stage is supplemented with statistical modeling for IR drop and voltage
noise using the IR-ATA flow as described in [33]. This approach allows STA to report
the timing slack of each path based on its estimation of voltage drop and noise, rather
than relying on a global pessimistic margin. This adjustment enhances the correlation
between the timing slack observed during CFST and the timing slack predicted by
the timing engine, as demonstrated in the results section. Once the final GDSII is
prepared, it is sent to the untrusted foundry for fabrication. The foundry may test the
functionality of the manufactured ICs before they are sent to a trusted facility for
Trojan detection.

To detect a Trojan, we must locate the slack shift induced by the TT or TP. As
shown in Figure 4.1, a TT increases the capacitive load on the driving cell of the
observed net, while a TP adds an extra gate delay to each timing line passing through
the victim net. Since we do not know which nets are affected, we must include all
nets in our delay analysis to identify any net that has been victimized or monitored
(by a TT or TP). A pin-to-pin wire (P2P wire) connects the output pin of a driver cell
(or primary input) to the input pin of one of its fanout cells (or primary output). A
gate with a fanout of four has four P2P wires. Each P2P wire is tested for both rise
and fall transitions.

This process can be repeated for N different timing paths passing through each net
to increase the detection rate and account for process variation (PV). The second criterion for selecting timing paths is the maximum frequency of the tester equipment;

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **61**

**Figure** **4.5** ML-based HT detection methodology. The figure describes the flow of
the HT detection scheme through the design, fabrication, and post-silicon stages.

the selected paths’ delay should be greater than the limit imposed by the tester’s maximum frequency. If a P2P wire in any timing path is not long enough for CFST, it
cannot be tested using side-channel delay analysis. However, these timing paths can
still be candidates for HT detection using power-based detection techniques. These
techniques are well suited for timing paths with a small number of gates, as they offer high controllability. For the other timing-path candidates, path delay fault (PDF)
test vectors are generated using an automatic test pattern generation (ATPG) tool. If
ATPG fails to generate a test pattern for a specific path, an alternative path is chosen.
Any path that ATPG cannot generate a test vector for is eliminated.

**4.4.3** **HT DETECTION METHODOLOGY**

**4.4.3.1** **Modeling and Tracking Process Drift**

Different timing paths experience varying delays due to process drift. We train a NN
that acts as a process tracking watchdog (NN-watchdog) to model the timing impact
of process drift. This NN-watchdog predicts the gap between the delay reported by
STA during design and the delay measured from the manufactured IC during testing.
The NN-watchdog is trained using a labeled data set, where each data point consists
of 48 input features and a corresponding label (output) value. The input features to
the ML model are setup time, path delay reported in STA, and sum of fanout over
cells over data part of the timing path extracted for each timing path. The other 15
features are from the sub-paths (capture path, launch path, and the data path), namely
the number of cells with various drive strengths and total length of metal layers for
each path. The input features, detailed in [16], are extracted from EDA tools for
timing engines and physical design.

**62** Advances in Hardware Design for Security and Trust

**Table 4.1**
**Description of Models Used and Model Hyperparameters**

Model Hyper parameters
MLP in layer=48, hidden layer=23, out layer=1,
activation=’tanh’, optimizer=’Adam’, learning rate=’adaptive’, start lr=’0.1’
Random Forest n estimators=’1024’, bootstrap=’true’, min leaf=’1’, min split=’2’
XgB n estimators=’1024’, learning rate=’0.05’,
Lasso alpha=’1’, max iter=’5000’
Ridge alpha=’1’, max iter=’500’
ElasticNet alpha=’0.001’, max iter=’1000’

To evaluate the effectiveness of the NN-watchdog, we modeled process drift (and
systematic process variation) by extracting the shift in delay values from SPICE simulations conducted using a skewed SPICE model. This model simulates a systematic
process drift by skewing the NMOS (N-channel MOSFET) and PMOS (P-channel
MOSFET) transistors to be X% faster and derating the metal capacitance for metal
layers 1 to 7 by Y%. Depending on the chosen values for X and Y, the process model
can be consistently faster or slower. For instance, in our simulations, using (X, Y) =
(5,5), (0,0), (5,5) results in fast, typical, and slow process models, respectively.

In this chapter, we evaluated three different models for predicting the processinduced change in timing path delays. The details of each model are discussed in the
relevant section:

1. Linear Regression (Ridge Regression) Model (Baseline): Ridge regression

[34] is a regularized linear regression model useful for modeling and tracking multicollinearity phenomena.
2. Multi-Layer Perceptron (MLP) Regression: MLP is a non-linear NN composed of an input layer, one or more hidden layers, and an output layer. The
setup of the MLP regressor used in this paper is summarized in Table 4.1.
3. Stacking Regression Model: Stacking regression [34] is an ensemble learning technique where different estimators are arranged into two layers to
form a regressor with lower variance compared to individual regressors.
In our model, we used eXtreme Gradient Boosting (XGB) [35, 36], Enet

[37–39], Lasso [40, 41], Ridge [42], MLP [34, 43], and random forest

[44, 45] for the first layer regression. The predictions of these regressors
are stacked together and fed to the second layer, which in our case, consists
of a single Lasso regressor.

**4.4.4** **FEATURE SELECTION, EXTRACTION, AND DATASET GENERATION**

To detect an HT, we need to identify the change in slack in timing paths affected by
the presence of TT or TP. As shown in Figure 4.1, the TT adds capacitive load to
the driving cell of an observed net, while the TP inserts one or more additional gates

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **63**

in the victim net. Without a golden IC, we do not know which nets are affected,
so we must analyze the delay of timing paths by examining each net within the
suspicious timing paths, i.e., those whose slack appears larger than expected during
the frequency sweeping test. A P2P wire connects the output pin of a driver cell
(or primary input) to the input pin of one of its fanout cells (or primary output).
A gate with a fanout of four has four P2P wires, each of which is tested for rise
and fall transitions. To improve detection accuracy and account for random process
variation, this process can be repeated for N different timing paths passing through
each net (similar to N-detect testing).

The second criterion for selecting timing paths is the maximum frequency of the
tester equipment; the selected paths’ delay should exceed the limit imposed by the
maximum frequency of the tester. If no timing path for a P2P wire is long enough for
CFST, it cannot undergo side-channel delay testing. However, such timing paths can
still be used as candidates for HT detection through power-based detection schemes.
These schemes are well suited for timing paths with a small number of gates, as
they offer high controllability. For the remaining timing-path candidates, PDF test
vectors are generated using an ATPG tool. If ATPG fails to generate a test pattern for
a specific path, a different path is selected. Any path for which ATPG cannot generate
a test vector is eliminated. This is illustrated by the flow described in Figures 4.6 and
4.7.

**4.5** **REGRESSION MODELS FOR HARDWARE TROJAN DETECTION**

**4.5.1** **MULTI-LAYER PERCEPTRON REGRESSOR**

The MLP is a fundamental type of neural network that comprises three main components: the input layer, hidden layers, and the output layer. In this architecture,
the input data is fed into the network through the input layer, where each neuron is
connected to others via weighted connections. These weights represent the strength
of interaction between the neurons. The hidden layers apply activation functions to
determine whether the input data carries significant information that should be propagated forward to the next layer, ultimately contributing to the model’s final prediction.

The MLP learns iteratively through a process known as backpropagation. During
backpropagation, the overall error, defined as the difference between the predicted
value and the ground truth, is calculated and minimized by an optimization algorithm. This process allows the model to refine its performance on the training set.
After training for a set number of epochs, the model’s accuracy is evaluated by testing it with unseen data, enabling it to produce the desired output.

The loss function for MLP regression is defined as:

yi −

p
###### ∑

j=0

Loss (MLP Regression) = <sup>1</sup>

M

M
###### ∑

i=1

w j × xij

�2

where M represents the number of instances, p is the number of features, yi is the
actual output, and xij and w j denote the input features and weights, respectively.

**64** Advances in Hardware Design for Security and Trust

**4.5.2** **RIDGE REGRESSION**

Ridge regression is a technique that enhances the stability and accuracy of regression
models by introducing regularization, particularly useful when dealing with multicollinear data sets. It minimizes the least-squares error of the regression model while
adding a penalty term proportional to the magnitude of the coefficients. This regularization term helps prevent overfitting by shrinking the coefficients of less important
features toward zero, thereby improving the model’s generalization.

The loss function for ridge regression is given by:

+ λ1
�2

M
###### ∑

i=1

p
###### ∑

j=0

Loss (Ridge Regression) = <sup>1</sup>

M

Loss (Ridge Regression) = <sup>1</sup>

1�

yi −

w j × xij

p
###### ∑

j=0

w <sup>2</sup> j

w <sup>2</sup> j

where λ1 is the regularization parameter that controls the degree of shrinkage applied
to the coefficients.

**4.5.3** **LASSO REGRESSION**

Lasso regression, like ridge regression, is a regularization technique used to reduce
the complexity of regression models. However, it employs L1 regularization, which
adds a penalty equal to the absolute value of the coefficient magnitudes. This method
is particularly effective for feature selection, as the L1 penalty forces some coefficients to become exactly zero, effectively eliminating low-contributing features and
preventing overfitting.

The loss function for lasso regression is defined as:

+ λ2
�2

p
###### ∑

j=0

Loss (Lasso Regression) = <sup>1</sup>

M

Loss (Lasso Regression) = <sup>1</sup>

M
###### ∑

i=1

yi −

p
###### ∑ |

j=0

|w j|

w j × xij

where λ2 is the regularization parameter associated with the L1 penalty.

**4.5.4** **ELASTICNET REGRESSION**

ElasticNet regression is a hybrid approach that combines the strengths of both ridge
and lasso regression models. It incorporates both L1 and L2 regularization terms in
its loss function, making it particularly effective for handling data sets with multicollinear features while performing feature selection. The ElasticNet model is controlled by the hyperparameter α, which balances the contributions of the L1 and L2
penalties, as described in the equation below:

Loss (ElasticNet Regression)

= <sup>1</sup>

M

M
###### ∑

i=1

p
###### ∑

j=0

w <sup>2</sup> j <sup>+ 0.5α ∗</sup> <sup>(1 −</sup> <sup>Lratio)</sup>

p
###### ∑

j=0

(yi −

p
###### ∑

j=0

w j ∗ xij) <sup>2</sup> + α ∗ Lratio

|w j| (4.1)

a
whereα = a + b and Lratio = a + b <sup>,</sup>

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **65**

with a and b being constants that control the trade-off between L1 and L2 regularization.

**4.5.5** **RANDOM FOREST REGRESSOR**

Random forest is an ensemble learning model that aggregates the predictions of multiple decision trees to enhance accuracy and mitigate overfitting. Each decision tree
in the forest starts at a root node and splits based on variable outcomes until a leaf
node is reached, which delivers the result. Random forest assumes that each decision
tree learns from different features and is relatively independent of the others.

As the data set size increases, random forest models can become prone to overfitting. To counter this, a technique called bootstrapping is used, which involves random sampling of subsets of the data set across multiple iterations. The bootstrapped
results are then averaged to produce a more robust and generalized prediction.

**4.5.6** **GRADIENT BOOSTING REGRESSOR**

Gradient boosting is an ensemble learning technique that combines multiple weak
models to achieve strong overall performance. It is particularly powerful in identifying nonlinear relationships between features and the target variable, and it is highly
resilient to missing values, outliers, and categorical features with high cardinality.

The primary objective of gradient boosting is to minimize the mean squared error
by iteratively improving the model. In each iteration, a residual function is calculated,
which is then added as an estimator to the current output. The subsequent model aims
to correct the errors of the previous one by using the gradient of the loss function to
fit a weak learner model.

**4.5.7** **STACKING CROSS-VALIDATION REGRESSOR (STACKINGCV)**

Stacking is an advanced ensemble learning technique that combines the predictions
of multiple regression models through a meta-regressor. In StackingCV, the data set
is split into k folds, and in each round, k − 1 folds are used to train the first-level regressors, while the remaining fold is used to generate out-of-fold predictions. These
predictions are then stacked to form the input for the second-level regressors. This
technique helps prevent overfitting by ensuring that the meta-regressor is trained on
predictions from data not used in the training of the first-level models.

**4.5.8** **MODEL TRAINING AND HYPERPARAMETERS**

This section details the training setup, including the parameters and hyperparameters for each regression model. We utilized the Scikit-learn library [34] in Python to
implement the regression models for detecting inserted HTs. The MLP model with
23 hidden layers, an Adam optimizer [48], and an adaptive learning rate was found
to produce good results. The model was trained for 10,000 epochs due to the large
training set, using a Tanh activation function and an 80:20 train-test split. The model
achieved high accuracy on the test set.

**66** Advances in Hardware Design for Security and Trust

For the ridge regression model, the α hyperparameter was set to 1.0, which was
found to be optimal for our data set. We trained the models with 45 interdependent
features, making ridge regression particularly useful for reducing prediction variance.

To implement the lasso regression model, the α hyperparameter was set at 0.001,
and the model was trained for 5,000 epochs, yielding the best results. The random
forest regression model used a maximum of 1,024 trees. The gradient boost regressor model was trained with a learning rate of 0.01 and a maximum of 1,024 trees.
For the StackingCV regressor, implemented using the MLXtend library [47], lasso
regression was employed as the meta-regressor model. The ElasticNet regression
model was implemented with an α term set to 0.001 and trained for 1,000 epochs.

**4.5.9** **IMPLEMENTATION RESULTS AND DISCUSSION**

This section describes our experimental setup and presents the results of our simulations.

Experimental Setup: We evaluated the effectiveness of our ML-based HT detection scheme on three major IWLS benchmarks [48] (Ethernet, S38417, and
AES128). For each benchmark, we inserted 90 HTs, consisting of simple combinational HTs with a single 2-input XOR gate to transfer the TP to a target net, a single
AND-tree to generate the HT activation signal, and four input triggers attached to
specific nets (TNs). Nets were carefully selected from non-critical timing patterns
with sufficient slack to accommodate the TT and TP. The positioning of the HT circuit (and the first gate of the AND-tree) relative to the triggering net determines the
capacitive delay impact of the TT. The HT circuit (first gate) is placed within a 20
µm radius of the TT nets to minimize the trigger impact (ensuring a small delay impact). The AND-tree for the HT circuit is also designed using the smallest AND gate
available in the standard cell library to minimize the influence of the driver gate’s
capacitance on the Trojan triggering net’s delay.

To demonstrate the sensitivity of our approach, we created 90 placed-and-routed
netlists for each benchmark, each containing a single HT circuit. Each benchmark
was physically designed and timing-closed at 1.4GHz in 32nm technology.

During NN-watchdog training, we do not know if a timing path chosen for training contains an HT. Therefore, we also assessed the effect of including Trojanaffected timing paths in the training set. We trained five NN-watchdogs with the
inclusion of 0, 1, 5, 10, and 15 TPs in their training set. Our objective was to determine whether Trojan-affected timing paths, such as trigger nets or payload nets,
could contaminate the model to the point where HT evasion occurs during the MLbased HT detection.

To simulate the silicon CFST test, we modeled the CFST step size and adjusted
the slack recorded for each timing path to the nearest higher clock sweeping frequency step using SPICE simulation. Modern testing equipment allows for step sizes
as small as 10–15ps, so we selected 15ps as the tester’s step size. We also considered
the effect of random process variation. Each SPICE simulation was subjected to 200
Monte Carlo simulations (modeling CFST on 200 different dies in the same speed

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **67**

**Figure 4.6** Generating a training set for the NN-watchdog

**Figure 4.7** ML-based HT classification algorithm

bin) to model the variation in path delays from chip to chip. The threshold voltage
(Vth), oxide thickness (Tox), and channel length (L) were varied, with random process variation limited to 5% as in [12].

In our simulations, we evaluated the effectiveness of HT detection using two
methods for building our reference (golden) timing model:

**68** Advances in Hardware Design for Security and Trust

**Figure 4.8** Hardware TP detection results

**4.5.9.1** **Shifted STA (SSTA)**

In this approach, the STA results are used as our reference timing model for HT
detection. However, direct use of STA results is ineffective due to process drift. To
account for process drift in SSTA, we calculated a static shift value by averaging
the observed shift from several sampled timing paths and applied this value to adjust
all reported slacks by STA. The detection threshold for this method was set at 45ps,
corresponding to the latency of a two-input NAND gate in our standard cell library.

**4.5.9.2** **Neural Shifted Golden Timing Model (NGTM)**

In this approach, the process drift and systematic process variation are modeled using
the proposed NN-watchdog. The anticipated shift by NN-watchdog, which generates
path-specific changes in slack based on path topology/features, is added to the STA
results. We also evaluated the use of MLP and stacked regression as NN-watchdogs
to demonstrate the effectiveness of the layered learning model. Since the timing paths
affected by the HT may be included in the data set used to train the NN-watchdog,
we investigated the performance of NGTM when the training set included 0, 1, 5,
10, and 15 HT-affected timing paths. In this method, the HT detection threshold was
adjusted to 4σ of the regressor standard deviation. Selecting σ helps reduce the falsepositive rate. Comparing the standard deviation of the two models (MLP vs. stacked
regression) can provide critical insights into why the NN-watchdog created using the
stacked regression model is expected to be more sensitive and accurate.

Figure 4.8 shows the results of TP detection in the Fast (X, Y) = (5, 5) speed bin.
The top row compares the accuracy of SSTA and NGTM in detecting TPs, while
the bottom row shows the false positive detection rate for each model across several
benchmarks. The performance of the stacked regression and MLP regression models
for HT detection is compared in this figure. Five different iterations of the NGTM
model (NGTM-X) are provided, each trained with X HTs included in its training set,
where X∈[0,1,5,10,15]. As reported, the inclusion of a small number of HT samples
in our data set minimally impacts the detection rate of our HT detection scheme
(using NGTM) on the test set, as the detection rate and false-positive rate of our HT
detection scheme for NGTM-0 is similar to NGTM-X for X∈[0,1,5,10,15].

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **69**

**Figure 4.9** Hardware TT detection results

Since the detection rate and false-positive rate of our ML-based HT detection
scheme for NGTM-0 and NGTM-X are comparable, the inclusion of a few HT samples in our data set had a negligible effect on the rate of the HT detection on the test
set (using NGTM). The similarity in detection and false-positive rates is because the
number of HTs (e.g., 15 HT data versus 20K HT-free data points) is not statistically
significant enough to influence the training process.

Figure 4.9 shows the results of TT detection in the Fast speed bin with (X, Y) =
(5, 5). Similar to the TP scenario, it compares the effectiveness of SSTA and various
types of NGTM (Trojan-tainted model) in identifying TTs. The figure shows that
reducing the NN-watchdog’s standard deviation (over 40% in some cases) greatly
improves TT detection. As demonstrated, NGTM is less effective in detecting TTs
than TPs, as TTs have a smaller impact on the delay of affected nets than TPs (which
cause at least one gate delay). Similar to the TP scenario, the training set’s contamination by a small number of HT data points does not affect the NN-watchdog’s accuracy. As shown, HT detection accuracy is highly dependent on the learning model
used (MLP vs. stacked regression). The stacking regression model’s lower detection
threshold (based on 4x(sigma NN) of regression model error) increases the detection
rate by 10% to 15%, yielding an HT detection rate above 95%. This occurs while
maintaining a false-positive rate that is lower or equal to the MLP-based equivalent. Although using the Youden threshold for detection significantly increases TT
detection, it also produces more false positives and may not be the best method for
determining the detection threshold.

The TTs can be designed to have a minimal delay impact on the affected timing
paths, making them more difficult to detect. A small delay change can be achieved by
connecting TTs to gates with high drive strength and low threshold voltage, and by
minimizing the TT nets’ capacitive delay. However, by limiting the size of standard
cells used in the design, increasing utilization in protected areas, and enforcing high
routing density in those areas, the system can be made more sensitive to TTs. This
would force the adversary to connect the TT to cells with lower drive strength and
use longer nets to connect the TT to the Trojan logic (with the TT placed further
away). An experimental SPICE framework was set up to evaluate how a TT affects
delay at various distances from its driving cell. We used a distributed RC model for

**70** Advances in Hardware Design for Security and Trust

Metal 3 in a 32nm technology process. The effect of increasing the TT distance (and
associated capacitive delay) on the delay of a timing path built using five NAND
gates was modeled. Assuming a detection threshold of 25ps, the timing-path delay
will increase by 25ps when the TT introduces an extra capacitance equivalent to a
net driving the TT logic placed 40 µm away from the affected net. Thus, sensitization
can be an effective strategy for increasing HT detection rates.

In this chapter, we provided a comprehensive overview of ML-based HT detection methods, with a focus on our proposed detection scheme. Unlike traditional
methods that require a golden IC, our approach, building on the LASCA framework [49], operates without one by leveraging two key elements: enhancing the timing model during the design phase to account for voltage noise and training a NN to
act as a process-tracking watchdog during testing, effectively modeling process drift
while considering process variations. We detailed the entire detection flow and the
ML framework, including an overview of the individual ML models used. Detection
results and evaluation metrics were also provided. Finally, we discussed emerging
trends, future challenges, and the potential of ML techniques in HT detection.

**REFERENCES**

1. Srivaths Ravi, Anand Raghunathan, Paul Kocher, and Sunil Hattangady. Security in
embedded systems: Design challenges. ACM Transactions on Embedded Computing
Systems (TECS), 3(3):461–491, 2004.
2. Seetharam Narasimhan, Dongdong Du, Rajat Subhra Chakraborty, Somnath Paul, Francis G Wolff, Christos A Papachristou, Kaushik Roy, and Swarup Bhunia. Hardware
trojan detection by multiple-parameter side-channel analysis. IEEE Transactions on
Computers, 62(11):2183–2195, 2012.
3. Reza Rad, Jim Plusquellic, and Mohammad Tehranipoor. Sensitivity analysis to hardware trojans using power supply transient signals. In 2008 IEEE International Workshop
on Hardware-Oriented Security and Trust, pages 3–7. IEEE, 2008.
4. Dongdong Du, Seetharam Narasimhan, Rajat Subhra Chakraborty, and Swarup Bhunia. Self-referencing: A scalable side-channel approach for hardware trojan detection.
In International Workshop on Cryptographic Hardware and Embedded Systems, pages
173–187. Springer, 2010.
5. Domenic Forte, Chongxi Bao, and Ankur Srivastava. Temperature tracking: An innovative run-time approach for hardware trojan detection. In 2013 IEEE/ACM International
Conference on Computer-Aided Design (ICCAD), pages 532–539, 2013.
6. Yu Liu, Yier Jin, and Yiorgos Makris. Hardware trojans in wireless cryptographic ics:
Silicon demonstration & detection method evaluation. In 2013 IEEE/ACM International
Conference on Computer-Aided Design (ICCAD), pages 399–404, 2013.
7. Xiaotong Cui, Elnaz Koopahi, Kaijie Wu, and Ramesh Karri. Hardware trojan detection
using the order of path delay. ACM Journal on Emerging Technologies in Computing
Systems (JETC), 14(3):1–23, 2018.
8. Ingrid Exurville, Loie Zussa, Jean-Baptiste Rigaud, and Bruno Robisson. Resilient hardware trojans detection based on path delay measurements. In 2015 IEEE International
Symposium on Hardware Oriented Security and Trust (HOST), pages 151–156. IEEE,
2015.

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **71**

9. Dylan Ismari, Jim Plusquellic, Charles Lamech, Swarup Bhunia, and Fareena Saqib. On
detecting delay anomalies introduced by hardware trojans. In 2016 IEEE/ACM International Conference on Computer-Aided Design (ICCAD), pages 1–7. ACM, 2016.
10. Yier Jin and Yiorgos Makris. Hardware trojan detection using path delay fingerprint.
In 2008 IEEE International Workshop on Hardware-Oriented Security and Trust, pages
51–57. IEEE, 2008.
11. Jie Li and John Lach. At-speed delay characterization for IC authentication and trojan
horse detection. In 2008 IEEE International Workshop on Hardware-Oriented Security
and Trust, pages 8–14. IEEE, 2008.
12. Kan Xiao, Xuehui Zhang, and Mohammad Tehranipoor. A clock sweeping technique for
detecting hardware trojans impacting circuits delay. IEEE Design & Test, 30(2):26–34,
2013.
13. Yu Liu, Ke Huang, and Yiorgos Makris. Hardware trojan detection through golden chipfree statistical side-channel fingerprinting. In Proceedings of the 51st Annual Design
Automation Conference, pages 1–6, 2014.
14. Hassan Salmani, Mohammad Tehranipoor, and Ramesh Karri. On design vulnerability
analysis and trust benchmarks development. In 2013 IEEE 31st International Conference on Computer Design (ICCD), pages 471–474. IEEE, 2013.
15. Bicky Shakya, Tony He, Hassan Salmani, Domenic Forte, Swarup Bhunia, and Mark
Tehranipoor. Benchmarking of hardware trojans and maliciously affected circuits. Journal of Hardware and Systems Security, 1(1):85–102, 2017.
16. Kevin Immanuel Gubbi, Banafsheh Saber Latibari, Anirudh Srikanth, Tyler Sheaves,
Sayed Arash Beheshti-Shirazi, Sai Manoj PD, Satareh Rafatirad, Avesta Sasan, Houman
Homayoun, and Soheil Salehi. Hardware trojan detection using machine learning: A
tutorial. ACM Transactions on Embedded Computing Systems, 22(3):1–26, 2023.
17. Karim Arabi, Resve Saleh, and Xiongfei Meng. Power supply noise in SoCs: Metrics,
management, and measurement. IEEE Design & Test of Computers, 24(3):236–244,
2007.
18. Kento Hasegawa, Masao Yanagisawa, and Nozomu Togawa. A hardware-trojan classification method using machine learning at gate-level netlists based on trojan features.
IEICE Transactions on Fundamentals of Electronics, Communications and Computer
Sciences, 100(7):1427–1438, 2017.
19. Kento Hasegawa, Masao Yanagisawa, and Nozomu Togawa. Trojan-feature extraction at
gate-level netlists and its application to hardware-trojan detection using random forest
classifier. In 2017 IEEE International Symposium on Circuits and Systems (ISCAS),
pages 1–4. IEEE, 2017.
20. Chongxi Bao, Domenic Forte, and Ankur Srivastava. On application of one-class svm
to reverse engineering-based hardware trojan detection. In Fifteenth International Symposium on Quality Electronic Design, pages 47–54, 2014.
21. Abdurrahman A Nasr and Mohamed Z Abdulmageed. An efficient reverse engineering
hardware trojan detector using histogram of oriented gradients. Journal of Electronic
Testing, 33(1):93–105, 2017.
22. Chongxi Bao, Domenic Forte, and Ankur Srivastava. On reverse engineering-based
hardware trojan detection. IEEE Transactions on Computer-Aided Design of Integrated
Circuits and Systems, 35(1):49–57, 2016.
23. Hassan Salmani. Cotd: Reference-free hardware trojan detection and recovery based on
controllability and observability in gate-level netlist. IEEE Transactions on Information
Forensics and Security, 12(2):338–350, 2017.

**72** Advances in Hardware Design for Security and Trust

24. Mingfu Xue, Jian Wang, and Aiqun Hu. An enhanced classification-based golden chipsfree hardware trojan detection technique. In 2016 IEEE Asian Hardware-Oriented Security and Trust (AsianHOST), pages 1–6, 2016.
25. Ashkan Vakil, Farnaz Behnia, Ali Mirzaeian, Houman Homayoun, Naghmeh Karimi,
and Avesta Sasan. Lasca: Learning assisted side channel delay analysis for hardware
trojan detection. In 2020 21st International Symposium on Quality Electronic Design
(ISQED), pages 40–45, 2020.
26. Ashkan Vakil, Ali Mirzaeian, Houman Homayoun, Naghmeh Karimi, and Avesta Sasan.
Avatar: NN-assisted variation aware timing analysis and reporting for hardware trojan
detection. IEEE Access, 9:92881–92900, 2021.
27. S Moustakidis, K Liakos, G Georgakilas, Nikolaos Sketopoulos, Stavros Seimoglou,
Patrik Karlsson, and Fotios Plessas. A novel holistic approach for hardware trojan detection powered by deep learning (HERO). In Proceedings of ATTRACT’20, 2020.
28. Rozhin Yasaei, Luke Chen, Shih-Yuan Yu, and Mohammad Abdullah Al Faruque. Hardware trojan detection using graph neural networks. arXiv preprint arXiv:2204.11431,
2022.
29. Rozhin Yasaei, Shih-Yuan Yu, and Mohammad Abdullah Al Faruque. Gnn4tj: Graph
neural networks for hardware trojan detection at register transfer level. In 2021 Design, Automation & Test in Europe Conference & Exhibition (DATE), pages 1504–1509.
IEEE, 2021.
30. Fredin Jose, M Priyatharishini, and M Nirmala Devi. Hardware trojan detection using
deep learning-generative adversarial network and stacked auto encoder neural networks.
In ICT Analysis and Applications, pages 203–210. Springer, 2022.
31. Huili Chen, Xinqiao Zhang, Ke Huang, and Farinaz Koushanfar. AdaTest: Reinforcement learning and adaptive sampling for on-chip hardware trojan detection. arXiv
preprint arXiv:2204.06117, 2022.
32. Nicholas Tuzzio, Kan Xiao, Xuehui Zhang, and Mohammad Tehranipoor. A zerooverhead IC identification technique using clock sweeping and path delay analysis. In
Proceedings of the Great Lakes Symposium on VLSI, pages 95–98, ACM, 2012.
33. Ashkan Vakil, Houman Homayoun, and Avesta Sasan. IR-ATA: IR annotated timing
analysis, a flow for closing the loop between PDN design, IR analysis & timing closure.
In Proceedings of the 24th Asia and South Pacific Design Automation Conference, pages
152–159, ACM, 2019.
34. F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau,
M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python.
Journal of Machine Learning Research, 12:2825–2830, 2011.
35. Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, pages 785–794, 2016.
36. Tianqi Chen, Tong He, Michael Benesty, Vadim Khotilovich, Yuan Tang, Hyunsu Cho,
Kailong Chen, et al. Xgboost: extreme gradient boosting. R Package Version 0.4-2,
1(4):1–4, 2015.
37. Zheng Zhang, Zhihui Lai, Yong Xu, Ling Shao, Jian Wu, and Guo-Sen Xie. Discriminative elastic-net regularized linear regression. IEEE Transactions on Image Processing,
26(3):1466–1481, 2017.
38. Hui Zou and Trevor Hastie. Regularization and variable selection via the elastic net.
Journal of the royal statistical society: Series B (statistical methodology), 67(2):301–
320, 2005.

Machine Learning Techniques for Detecting Hardware Trojans in ASIC Designs **73**

39. Hui Zou and Hao Helen Zhang. On the adaptive elastic-net with a diverging number of
parameters. Annals of Statistics, 37(4):1733, 2009.
40. Lukas Meier, Sara Van De Geer, and Peter B¨uhlmann. The group lasso for logistic
regression. Journal of the Royal Statistical Society: Series B (Statistical Methodology),
70(1):53–71, 2008.
41. J Ranstam and JA Cook. Lasso regression. Journal of British Surgery, 105(10):1348–
1348, 2018.
42. Gary C McDonald. Ridge regression. Wiley Interdisciplinary Reviews: Computational
Statistics, 1(1):93–100, 2009.
43. Leonardo Noriega. Multilayer perceptron tutorial. School of Computing. Staffordshire
University, 2005.
44. Mariana Belgiu and Lucian Dr˘agut¸. Random forest in remote sensing: A review of applications and future directions. ISPRS Journal of Photogrammetry and Remote Sensing,
114:24–31, 2016.
45. G´erard Biau and Erwan Scornet. A random forest guided tour. Test, 25(2):197–227,
2016.
46. Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv
preprint arXiv:1412.6980, 2014.
47. Sebastian Raschka. Mlxtend: Providing machine learning and data science utilities and
extensions to python’s scientific computing stack. The Journal of Open Source Software,
3(24), April 2018.
48. Christoph Albrecht. IWLS 2005 benchmarks. In International Workshop for Logic
[Synthesis (IWLS): http://www. iwls. org, 2005.](http://www.iwls.org)
49. Ashkan Vakil, Farnaz Behnia, Ali Mirzaeian, Houman Homayoun, Naghmeh Karimi,
and Avesta Sasan. Lasca: Learning assisted side channel delay analysis for hardware
trojan detection. In 2020 21st International Symposium on Quality Electronic Design
(ISQED), pages 40–45. IEEE, 2020.

# 5 Next-Generation
### Semiconductor Reverse Engineering: Laser Delayering, Correlative Imaging, and Cloud-Enabled Image Analysis Techniques

Hongbin Choi, Matthew Maniscalco, Adrian
Phoulady, Alexander Blagojevic, Toni Moore,
Mohammad Taghi Mohammadi Anaei, Todor
Bliznakov, Marcus Emanuel, Parisa Mahyari,
Nichoals May, Sina Shahbazmohamadi, and
Pouya Tavousi

**5.1** **INTRODUCTION**

Reverse engineering of electronics and microelectronics is a critical process used to
understand the structure and function of components, including integrated circuits
(ICs) and printed circuit boards (PCBs). This process is essential for failure analysis,
intellectual property (IP) verification, and competitive analysis. As electronic devices
become increasingly complex, the need for more advanced reverse engineering techniques has grown. Traditional delayering methods, such as mechanical polishing and
focused ion beam (FIB) milling, face significant trade-offs between throughput and
precision. Mechanical and chemical delayering methods are faster but lack precision,
while FIB delayering, though precise, is slow and impedes timely failure analysis and
verification processes.

[DOI: 10.1201/9781003510949-5](https://doi.org/10.1201/9781003510949-5) **74**

Next-Generation Semiconductor Reverse Engineering **75**

**5.1.1** **CHALLENGES**

Several challenges complicate the reverse engineering of microelectronics, particularly during the delayering and imaging processes:

 - Trade-Off Between Resolution and Speed: Achieving high resolution is
essential for capturing the fine details of the component’s structure, but
it often necessitates slower delayering speeds. Conversely, increasing the
speed of delayering can compromise resolution, potentially missing critical
details necessary for accurate reverse engineering.

 - Non-Flat Layer Exposure: The layers exposed during delayering are
rarely perfectly flat, leading to challenges in accurately stacking images
for 3D reconstruction. This can result in errors in analysis and misinterpretation of the component’s architecture due to overlapping information from
different layers.

 - Accessibility of Computational Resources: The extensive computational
resources required for processing and analyzing high-resolution images
during delayering are another hurdle. This includes the need for powerful hardware and specialized software, which may not be accessible to all
researchers or institutions. The cost and availability of these resources can
limit the ability to fully leverage the advanced techniques discussed in this
chapter, especially for smaller or less well-funded research groups.

These challenges underscore the complexities involved in modern reverse engineering of microelectronics and highlight the need for ongoing innovation to address
these issues effectively.

**5.1.2** **INNOVATION**

To tackle these challenges, this chapter introduces a novel approach that combines
femtosecond laser delayering, correlative multimodality imaging, and cloud-based
image analysis. Femtosecond lasers offer a significant advantage over traditional
mechanical/chemical and FIB techniques by enabling rapid material removal with
minimal collateral impact. The integration of correlative imaging allows for capturing complementary data from different modalities, enhancing the overall resolution
and accuracy of the reverse engineering process.

**5.1.3** **CLOUD INTEGRATION**

The integration of cloud-based platforms further enhances this approach by providing the computational power necessary to process and analyze the extensive data sets
generated. Machine learning algorithms can be employed on these platforms to automate defect detection, netlist extraction, and other analytical processes, making the
analysis more efficient and accurate. This integration is particularly important for
streamlining the reverse engineering process and making high-resolution imaging
more accessible.

**76** Advances in Hardware Design for Security and Trust

**5.1.4** **OBJECTIVES**

This chapter aims to provide a comprehensive overview of this next-generation
approach to reverse engineering in microelectronics. It will cover the foundational
techniques, present a tutorial on different delayering approaches—including femtosecond laser delayering—and survey the current state of the art in the field.
Additionally, we will discuss the potential impact of these innovations on the electronics industry and provide a technical road map for their implementation.

**5.2** **TUTORIAL** **AND** **STATE-OF-THE-ART** **SURVEY:** **DELAYERING,**
**IMAGING,** **AND** **ANALYSIS** **TECHNIQUES** **IN** **SEMICONDUCTOR**
**REVERSE ENGINEERING**

Delayering and imaging are critical processes in semiconductor reverse engineering, allowing researchers to expose and analyze individual layers of an IC or other
electronic components. This section provides a detailed tutorial on the main delayering techniques—mechanical/chemical delayering, FIB delayering, and femtosecond
laser delayering—along with the associated imaging and analysis methods. Additionally, it surveys the state-of-the-art advancements pushing the boundaries of these
techniques.

**5.2.1** **MECHANICAL/CHEMICAL DELAYERING AND IMAGING**

**5.2.1.1** **Tutorial**

 - Delayering Overview: Mechanical and chemical delayering are traditional
methods for removing layers from an IC or PCB. Mechanical delayering
involves physical abrasion, while chemical delayering uses specific acids
or solvents to dissolve layers.

 - Imaging Considerations:

   - Imaging Setup: Periodic imaging is crucial during mechanical or
chemical delayering. Optical microscopy is commonly used, though it
may lack the resolution required for finer details.

   - Image Documentation: Regular imaging ensures that each layer is
documented before moving on. These images are essential for reconstructing the structure of the component.

   - Surface Flatness: Uneven surfaces can cause image distortion, complicating the stacking process necessary for accurate 3D reconstruction.

 - Steps Involved:

   - Mechanical Delayering: Utilize precision grinding or polishing to remove layers. Periodically capture images using an optical microscope
to monitor progress.

   - Chemical Delayering: Apply chemical etchants to selectively dissolve
layers. Use optical or SEM imaging to document the exposed layers.

Next-Generation Semiconductor Reverse Engineering **77**

**5.2.1.2** **State-Of-The-Art Survey**

Recent advancements in mechanical and chemical delayering include improved control mechanisms for more uniform layer removal and the integration of automated
systems to reduce manual errors. However, these methods are increasingly being
supplemented by more advanced techniques, particularly in applications requiring
higher precision and resolution.

**5.2.2** **FOCUSED ION BEAM DELAYERING AND IMAGING**

**5.2.2.1** **Tutorial**

 - Delayering Overview: FIB delayering uses a focused ion beam, typically
gallium, to sputter away material from the component surface. This method
is known for its precision, making it ideal for removing very thin layers.

 - Imaging Considerations:

   - Integrated Imaging: FIB systems often include SEM, allowing realtime imaging of the delayering process to ensure accurate layer removal.

   - High-Resolution Imaging: The SEM provides detailed images that
capture the fine structures within each layer, critical for 3D reconstruction.

   - Image Stacking: FIB’s precision minimizes layer overlap, making it
easier to stack images accurately for 3D modeling.

 - Steps Involved:

   - Setup and Calibration: Calibrate the FIB system, adjusting ion beam
parameters for optimal precision.

   - Delayering Process: Sputter away material layer by layer, capturing
high-resolution SEM images after each step.

   - Imaging and Documentation: Document each exposed layer thoroughly before proceeding to the next.

**5.2.2.2** **State-Of-The-Art Survey**

FIB technology has seen improvements in ion beam control and automation, allowing for more precise and faster material removal. Innovations such as dual-beam
systems, which combine FIB with electron beam imaging, have enhanced real-time
monitoring capabilities. These advancements have made FIB an indispensable tool
in reverse engineering, particularly for analyzing advanced ICs.

**5.2.3** **FEMTOSECOND LASER DELAYERING AND IMAGING**

**5.2.3.1** **Tutorial**

 - Delayering Overview: Femtosecond laser delayering uses ultrafast laser
pulses to ablate material from the component surface. This method enables
rapid, non-contact material removal, minimizing thermal damage and making it suitable for high-throughput applications.

**78** Advances in Hardware Design for Security and Trust

 - Imaging Considerations:

   - Real-Time Monitoring: Femtosecond laser delayering can be paired
with confocal microscopy for monitoring, ensuring even material removal.

   - High-Precision Volumetric Imaging: Post-ablation, high-resolution
images can be captured using confocal microscopy to enable accurate
3D reconstructions.

   - Hybrid Imaging Approach: For improved flatness and precision, femtosecond laser delayering can be combined with FIB polishing, creating
an ideal surface for imaging.

 - Steps Involved:

   - Setup and Calibration: Configure the femtosecond laser system, adjusting parameters for optimal ablation.

   - Delayering Process: Use the laser to ablate material, with imaging to
monitor progress.
Imaging and Documentation: Capture high-resolution images after
each delayering step to obtain a volumetric image of the sample.

**5.2.3.2** **State-Of-The-Art Survey**

Femtosecond laser technology represents the cutting edge in material removal, particularly in terms of speed and precision. Recent advancements include better control
over pulse duration, shape and energy, allowing for more precise ablation. Additionally, the integration of femtosecond lasers with advanced imaging systems, such as
confocal microscopy and 3D SEM, can significantly improve the ability to capture
detailed 3D models of components. The development of hybrid techniques combining laser ablation with FIB polishing can significantly enhance the accuracy and
reliability of the imaging process.

**5.2.4** **INNOVATIONS IN IMAGING AND ANALYSIS TECHNOLOGIES**

**5.2.4.1** **Correlative Imaging**

Combining different imaging modalities, such as SEM and confocal microscopy, is
becoming a trending innovation in reverse engineering microelectronic components.
This approach leverages the strengths of each modality, providing comprehensive
data sets that are essential for accurate reverse engineering. Correlative imaging allows for a multi-faceted analysis, where different aspects of the component are captured and integrated into a unified data set, offering deeper insights into the structure
and functionality.

**5.2.4.2** **Cloud-Based Imaging and Analysis**

The shift toward cloud-based platforms for processing and analyzing imaging data is
another key innovation. These platforms provide the computational resources needed
to handle large data sets and offer advanced tools, such as machine learning (ML)
algorithms, for automating analysis, defect detection, and improving accuracy. This

Next-Generation Semiconductor Reverse Engineering **79**

trend is particularly important for making high-resolution imaging more accessible to
researchers and institutions with limited resources. By leveraging cloud computing,
users can perform complex analyses without the need for expensive on-premises
infrastructure.

**5.2.4.3** **Machine Learning for Automated Analysis**

ML is increasingly being integrated into imaging systems to automate tasks such as
image recognition, defect detection, and netlist extraction. These technologies are
enhancing the speed and accuracy of reverse engineering by reducing the need for
manual analysis and enabling more sophisticated data interpretation. ML models
trained on large data sets can identify patterns and anomalies that might be missed
by human inspectors, significantly improving the reliability of reverse engineering
processes.

**5.3** **SHOWCASING** **TECHNIQUES** **AND** **CAPABILITIES** **IN** **RAPID** **MI-**
**CROELECTRONICS REVERSE ENGINEERING**

This section showcases various aspects of our proposed method for rapid microelectronics reverse engineering by presenting multiple techniques and capabilities that
we have developed, including femtosecond laser delayering, multimodal microscopy,
and cloud-based platforms for data visualization and analysis.

**5.3.1** **REVERSE** **ENGINEERING** **TECHNIQUE** **1:** **HIGH-RESOLUTION** **3D** **RE-**
**CONSTRUCTION** **OF** **MICROELECTRONICS** **USING** **FEMTOSECOND**
**LASER DELAYERING AND DIGITAL MICROSCOPY**

**5.3.1.1** **Motivation**

The reverse engineering of microelectronics, including PCBs and integrated circuits,
is essential for quality assurance, failure analysis, and competitive intelligence. Traditional reverse engineering methods, like X-ray computed tomography (CT) and
FIB delayering, often face limitations in terms of resolution, material differentiation, and throughput. While X-ray CT provides non-destructive insights, it lacks the
resolution needed for detailed analysis, especially in complex, multi-material components. FIB delayering offers higher resolution but is slow and unsuitable for analyzing large areas. Mechanical and chemical delayering techniques, while faster,
often lack precision and repeatability.

To overcome these challenges, we propose a novel workflow that combines ultrashort pulsed femtosecond laser delayering with digital microscopy. This approach
aims to provide a fully automated and repeatable method for microelectronics reverse
engineering, offering high resolution and rapid processing.

**5.3.1.2** **Method Overview**

The proposed workflow integrates a femtosecond laser machining system with a fivemegapixel digital microscope and a gas processing component. The entire process
is automated, including the movement of the XYZ stage system, the triggering of

**80** Advances in Hardware Design for Security and Trust

the laser and gas injection systems, and the imaging process. The key steps in the
workflow are as follows:

1. Initial Imaging: The PCB is placed on a vacuum stage and imaged using
a digital microscope. The operator selects the region of interest (ROI) and
creates a computer-aided design (CAD) model for the laser ablation.
2. Height Measurement: The PCB is then moved to a confocal height sensor,
which takes height measurements across the exposed surface. The highest
point is brought into focus for the laser.
3. Laser Ablation: The PCB is transferred to the laser scanner field, where the
femtosecond laser begins the delayering process. The process is monitored
to ensure minimal height variation within each slice.
4. Gas Processing and Imaging: After each laser cycle, the area is cleaned
using a gas processing system to remove debris and minimize heat-affected
zones (HAZs). The PCB is then imaged using the digital microscope.
5. Repetition: Steps 2 through 4 are repeated until the desired depth is
reached.

**5.3.1.3** **Delayering/Imaging System**

The delayering and imaging system consists of six major components: a laser scanner, confocal height sensor, digital microscope, gas processing system, XYZ stage
system, and vacuum chuck. The laser scanner, equipped with a 70 mm f-theta lens,
is capable of scanning a 7.5 µm laser beam with high precision. The confocal height
sensor ensures accurate laser focusing, while the digital microscope captures highresolution images post-laser ablation. The gas processing system plays a crucial role
in maintaining clean cuts with minimal collateral damage.

**5.3.1.4** **Demonstration**

The proposed workflow was tested on a 1.5 cm × 1.5 cm area of a PCB, requiring 380
cycles of laser ablation and imaging, resulting in a total of 1520 images. Each cycle
took approximately 2 minutes, with additional time for imaging and stage movement,
resulting in a total process time of about 19 hours. The resulting images were stacked
to create a 3D reconstruction of the PCB.

 - Comparison with X-ray CT: The 3D reconstruction generated by the proposed method was compared with X-ray CT images of the same ROI. The
femtosecond laser delayering method provided higher resolution and more
detailed information, particularly in differentiating materials. While X-ray
CT images are limited to grayscale, the proposed method captures color
information, enabling better material distinction.

 - Application Beyond PCBs: Although the focus of the study was on PCBs,
the method’s applicability extends to other microelectronic devices. The
workflow was also tested on a 12 LP die, where it demonstrated superior
resolution and material differentiation compared to X-ray CT.

Next-Generation Semiconductor Reverse Engineering **81**

**5.3.1.5** **Summary**

The presented technique is a novel workflow combining ultrashort pulsed femtosecond laser delayering and digital microscopy for the reverse engineering of PCBs.
This method offers significant advantages over existing techniques, including higher
resolution, faster processing, and better material differentiation. The workflow is
fully automated, reducing the need for multiple PCB replicates and minimizing operator dependence. The method has potential applications beyond PCBs, making it
a versatile solution for the rapid reverse engineering of various microelectronic devices. Future improvements could focus on enhancing throughput and expanding the
scope of application to provide a universal solution for microelectronics reverse engineering. A detailed description of this technique has been provided in [1] (Figures
5.1–5.7).

**Figure** **5.1** Consecutive laser delayering and digital imaging, followed by stacking
the images to reconstruct the 3D structure of the PCB.

**Figure 5.2** Overview of the lasering/imaging system.

**82** Advances in Hardware Design for Security and Trust

**Figure** **5.3** Digital microscope images of various slices obtained from the delayering process and schematic depiction of the stacking of slices for three-dimensional
reconstruction.

**Figure 5.4** (a) Side-by-side of reconstructed volume and X-ray CT of PCB; (b) crosssectional view of the reconstructed volume.

**5.3.2** **REVERSE** **ENGINEERING** **TECHNIQUE** **2:** **PRECISION** **VOLUMETRIC**
**IMAGING OF ELECTRONICS VIA FEMTOSECOND LASER DELAYERING**
**AND CONFOCAL MICROSCOPY**

**5.3.2.1** **Motivation**

Achieving high-resolution, three-dimensional (3D) imaging of microelectronic components is crucial for applications such as inspection, failure analysis, and reverse

Next-Generation Semiconductor Reverse Engineering **83**

**Figure 5.5** Six slices among 91 slices that were resulted from applying the proposed
technique on a 12 LP die.

**84** Advances in Hardware Design for Security and Trust

**Figure** **5.6** Multiple slices from the same region of interest as Figure 5.5, obtained
from the X-ray CT image.

**Figure** **5.7** Comparison of the quality of the cut using the proposed laser system,
with and without the gas injection system running.

Next-Generation Semiconductor Reverse Engineering **85**

engineering. Traditional methods, such as X-ray CT and FIB delayering, either lack
the necessary resolution or are too slow for large-scale applications. Furthermore,
differences in laser ablation rates across materials can result in non-flat layers, complicating 3D reconstructions when using conventional techniques.

This section explores a method that combines femtosecond laser ablation with
confocal microscopy to create high-resolution volumetric images, addressing the
limitations of both traditional non-destructive and destructive techniques.

**5.3.2.2** **Creating a 3D Image from Non-Flat 2D Images**

One of the challenges in volumetric imaging is the assumption that each exposed
layer of the sample is flat, which is rarely the case. Differences in the laser ablation
rate across various materials often result in uneven layers, distorting the final 3D
reconstruction when stacking 2D images. To overcome this, the proposed method
uses confocal microscopy to obtain a height map of each exposed layer in addition
to the optical image. This combined data is used to reconstruct an accurate 3D image.

**5.3.2.3** **Workflow Overview**

The workflow involves repeated cycles of optical and confocal imaging followed by
laser delayering:

1. Region of Interest (ROI) Identification: The sample’s ROI is identified,
and an initial X-ray CT image may be obtained for preliminary analysis.
2. Fiducial Mark Creation: Fiducial marks are laser-etched around the ROI
for precise alignment during subsequent imaging and delayering steps.
3. Optical and Confocal Imaging: A confocal microscope captures optical
and height images of the ROI, which are processed to generate a virtual
mask for the next delayering step.
4. Laser Delayering: Based on the virtual mask, the laser selectively ablates
material from the sample, ensuring minimal height variation across the ROI.
5. Repetition: The process is repeated until the entire volume of interest is
captured.

**5.3.2.4** **Delayering using Femtosecond Laser**

Femtosecond lasers offer significant advantages over traditional delayering methods,
including minimal thermal damage and high throughput. However, challenges such
as redeposition of ablated material and the trade-off between ablation rate and surface
quality must be managed. The study optimizes laser parameters, including energy per
pulse and repetition rate, to achieve a balance between speed and precision.

**5.3.2.5** **Imaging**

A laser confocal microscope is used for imaging, providing both optical and height
information. The microscope’s settings, such as the numerical aperture and field of

**86** Advances in Hardware Design for Security and Trust

view, are optimized to capture high-resolution images efficiently. The confocal images are essential for creating accurate 3D reconstructions by ensuring that each
layer’s height variations are accounted for during the stacking process.

**5.3.2.6** **Gas Cleaning/Cooling**

To address the issue of redeposition during laser ablation, the workflow includes
a gas cleaning system that uses dry ice particles to remove debris from the surface.
This process not only prevents redeposited material from interfering with subsequent
laser cycles but also helps mitigate heat-affected zones (HAZs), ensuring cleaner and
more precise cuts.

**5.3.2.7** **Image Registration and Virtual Masking**

Accurate image registration is crucial for aligning the data obtained during the delayering process. Fiducial marks are used to correct for any translation, rotation, or tilt
that occurs between imaging cycles. Additionally, a virtual masking process is employed to manage height variations across the ROI, ensuring that only the necessary
regions are lasered in each cycle.

**5.3.2.8** **3D Reconstruction**

The final 3D reconstruction is generated by combining the registered optical and
height images. The resolution of the 3D image is determined by the laser delayering
resolution and the vertical resolution of the confocal height map. The study demonstrates that this method produces high-resolution 3D images with significantly more
detail than traditional X-ray CT images.

**5.3.2.9** **Demonstration**

The proposed method was applied to a typical PCB sample, successfully creating
a 3D image with a total height range of approximately 700 µm. The entire process
took about 20 to 30 hours to complete, which is significantly faster than traditional
methods like FIB. The resulting 3D images were compared with X-ray CT images,
showing that the proposed method provided richer information, including color data
that helped distinguish different material compositions. The confocal microscopy’s
high-resolution optical data also revealed fine details in materials like glass fiber,
which were not visible in the X-ray CT images.

**5.3.2.10** **Summary**

The presented technique is a novel method for high-resolution volumetric imaging
that combines femtosecond laser delayering with confocal microscopy. The proposed
approach addresses several challenges associated with traditional methods, including
the non-flatness of layers and the redeposition of ablated material. By leveraging
confocal microscopy to obtain accurate height maps and using targeted gas cleaning
to maintain surface quality, this method offers a significant improvement in both the

Next-Generation Semiconductor Reverse Engineering **87**

**Figure** **5.8** The challenge of stacking 2D images for obtaining a 3D image: due to
nonplanarity of the 2D layers, the resulting 3D image will be distorted.

speed and resolution of 3D imaging. The results demonstrate that this method not
only outperforms X-ray CT in terms of resolution and information content but also
offers a practical alternative to slower, more expensive techniques like FIB. Future
work will focus on further optimizing the process and expanding its application to a
wider range of microelectronic devices. A detailed description of this technique has
been provided in [2] (Figures 5.8–5.23).

**5.4** **IMAGING ANALYSIS**

**5.4.1** **IMAGE ANALYSIS CAPABILITY 1: CLOUD-ENABLED AUTOMATED DE-**
**FECT DETECTION VIA SYNTHETIC DATA AUGMENTATION**

**5.4.1.1** **Motivation**

The detection and analysis of defects in microelectronics are vital for ensuring the
reliability and safety of electronic devices. As the semiconductor industry continues
to grow, the need for accurate and efficient defect detection becomes increasingly
important. Traditional methods, such as manual inspection and ML-based automated
detection, are hampered by the scarcity of defective parts, limiting the availability of
ground truth data necessary for training effective defect detection models.

To address these challenges, this study introduces a novel synthetic data augmentation workflow designed to overcome the limitations of traditional defect detection
approaches. By generating virtual defective parts and simulating their X-ray images,
the proposed method enables the creation of large, labeled data sets at a low cost,
significantly enhancing the training of both manual inspectors and ML algorithms.

**5.4.1.2** **Overview of the Synthetic Data Augmentation Workflow**

The proposed workflow involves generating synthetic data sets by introducing defects into flawless 3D CAD models of microelectronic components. This process
involves several key steps:

**88** Advances in Hardware Design for Security and Trust

**Figure 5.9** (a) Proposed approach for sampling the volume of interest addresses the
distortion issue of the resulting 3D image; (b) laser cutting pattern is determined
based on the height profile to maintain the height variation within a certain limit.

 - 3D Model Construction: The workflow begins with the construction of
a 3D model of the microelectronic part. This model is generated through
imaging-enabled reverse engineering, where 3D images of the part are reconstructed to extract the CAD model.

 - Generation of Defective Models: Once the CAD model is available, multiple instances of the part are created, and known defects with specific characteristics are introduced into these models. This step produces a population of defective parts in silico.

 - X-ray Image Simulation: Using state-of-the-art X-ray CT simulation software, X-ray images of the defective parts are simulated. These images,
along with detailed information about the defects, form the basis of the
training data set.

Next-Generation Semiconductor Reverse Engineering **89**

**Figure** **5.10** The different regions, marks, and areas on the sample for the whole
process.

**Figure** **5.11** Digital image of the PCB board after: (a) 0 cycles of lasering; (b) few
cycles of lasering; and (c) tens of cycles of lasering. (d) Schematic illustration of
PCB cross section.

**90** Advances in Hardware Design for Security and Trust

**Figure 5.12** 3D CAD design of the laser system.

 - Labeling and Data Set Compilation: Each simulated image is inherently
labeled with defect information, creating a comprehensive data set suitable
for training ML algorithms and manual inspectors.

**5.4.1.3** **Validation of Synthetic X-Ray Images**

The synthetic X-ray images generated through this workflow were validated by comparing them with real X-ray images of the same microelectronic parts. The comparison focused on the similarity between the simulated and real images, using metrics
such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Normalized
Mean Absolute Error (NMAE). The results indicated a high degree of similarity between the synthetic and real images, with relatively low error values, confirming the
realism and applicability of the synthetic data sets.

**5.4.1.4** **Case Study: Detecting Defects in Integrated Circuits**

To demonstrate the effectiveness of the proposed workflow, a case study was conducted on an IC sample. The IC was subjected to an X-ray CT scan, and the resulting 3D image was used to generate STL files for the electronic parts and packaging.
These STL files, along with the assigned materials, were used in the image simulation algorithm to generate synthetic 2D X-ray projections of the sample.

The study also explored the introduction of specific defects, such as missing bond
wires and dented packaging, into the CAD models. The resulting synthetic images

Next-Generation Semiconductor Reverse Engineering **91**

**Figure 5.13** 2D optical image with 6 × 5 imaging grid illustrated; (b) surface height
information of the same imaged area in (a), represented as a heatmap; and (c) and
3D surface image obtained from fusing optical and confocal images.

**Figure 5.14** Laser optimization experimentation. Single-pulse experiments on plastic, for fluence and EPP investigations (left). Laser trenches on a copper substrate for
repetition rate and overlap investigations (right).

**92** Advances in Hardware Design for Security and Trust

**Figure** **5.15** Different recipes ablating an ABS plastic sample. The left sample is
lasered with an improper and the right one is lasered with a proper lasering recipe.

**Figure** **5.16** The trade-off between throughput and cleanliness is shown. Left: Use
of high power to create a trench. Right: Use of low power and a higher number of
cycles to obtain a trench with the same depth.

successfully represented these defects, providing realistic training data for defect
detection models. The case study highlighted the potential of the proposed workflow
to enhance defect detection capabilities in microelectronics by generating diverse
and realistic training data sets.

**5.4.1.5** **Summary of Analysis Capability 1**

The comprehensive workflow presented in this section offers a solution for generating synthetic data to augment traditional defect detection methods in microelectronics. By leveraging 3D CAD models and X-ray simulation software, the proposed

Next-Generation Semiconductor Reverse Engineering **93**

**Figure** **5.17** Laser lines drawn on silicon with no dwelling compensation depicting
“burn-in” and causing uneven milling at the edges (left), and an example of lasering
with dwelling compensation (right).

**Figure** **5.18** An example of dwelling caused by scanner mirror acceleration (left).
Dwelling compensation utilizing a developed intelligent scanning system (right).

method creates large, labeled data sets that significantly enhance the training of both
manual inspectors and machine learning algorithms. The ability to introduce realistic noise profiles and a wide range of defect types into the synthetic images further
improves the effectiveness of the training data. The results of this study demonstrate
that synthetic data sets generated through this workflow closely resemble real-world
X-ray images, providing a valuable tool for improving defect detection accuracy and
reliability. A detailed description of this capability has been provided in [3] (Figures
5.24–5.29).

**94** Advances in Hardware Design for Security and Trust

**Figure 5.19** Comparison of laser processing of copper without gas processing (left)
and with gas processing (right).

**Figure 5.20** Generation of mask to be utilized during laser processing.

**5.4.2** **IMAGE ANALYSIS CAPABILITY 2: DEEP LEARNING-DRIVEN PCB**
**REVERSE ENGINEERING WITH SYNTHETIC X-RAY DATA SETS**

**5.4.2.1** **Motivation**

Part obsolescence in microelectronics is a critical issue that can lead to expensive
redesigns and delays in product development. Remanufacturing, which relies on reverse engineering, offers a solution by enabling the production of obsolete parts.
For PCBs, reverse engineering can employ nondestructive methods like X-ray CT
to capture their internal structures. However, a significant challenge lies in the segmentation of X-ray CT images to extract the design of PCBs, a task traditionally
done manually. Manual segmentation is time-consuming, labor-intensive, and prone
to human error, necessitating automated solutions.

Deep learning has emerged as a powerful tool for automating image segmentation
tasks, including PCB reverse engineering. However, the effectiveness of deep learning models depends on the availability of large, annotated data sets, which are often
scarce due to the high costs and effort associated with image acquisition and labeling. This study proposes a novel approach to overcome this limitation by generating
synthetic X-ray images that serve as ground truth data for training deep learning algorithms. The method shows promise in automating PCB reverse engineering and can
be extended to other applications, including automated verification and validation
(V&V) of fabricated chips, defect detection, and brain network mapping (connectomics).

Next-Generation Semiconductor Reverse Engineering **95**

**Figure** **5.21** Some xy-plane sections of the resulting PCB 3D image using the proposed method and the corresponding X-ray CT images.

**96** Advances in Hardware Design for Security and Trust

**Figure** **5.22** Cross-sectional view of the volumetric image data as collected by the
confocal microscope at different layers throughout the consecutive delayering/imaging procedure. The aspect ratio is 1:1.

**Figure** **5.23** Automated image segmentation using the ablation rate information.
Left: A heatmap of the ablation rate (red is low and yellow is high). Right: The
optical image of the same region.

**5.4.2.2** **Overview of the Synthetic Data Generation Process**

The proposed method for automated segmentation of PCB images is built on three
key pillars:

 - Creation of Realistic Synthetic Geometries: The method begins with
generating sufficiently realistic 3D CAD models of the PCBs using OpenSCAD software, which is a script-based open-source 3D compiler.

 - Synthesis of Corresponding X-ray Images: These 3D models are then
used to generate synthetic X-ray images through two approaches—
simplified ray tracing and direct geometry-based image generation with
added noise.

 - Training Deep Learning Networks: The generated synthetic images,
along with their inherent labels, are used to train deep learning networks
designed to segment the PCB X-ray images automatically.

Next-Generation Semiconductor Reverse Engineering **97**

**Figure 5.24** Workflow for synthesizing training data for workforce training and training of machine learning algorithms.

**98** Advances in Hardware Design for Security and Trust

**Figure 5.25** (a, b) Two different X-ray images of air and (c) the normalized resulted
noise profile.

Next-Generation Semiconductor Reverse Engineering **99**

**Figure 5.26** CADs of (a) the electronic parts and (b) packaging.

**5.4.2.3** **Performance on Simple Geometries**

To validate the approach, the workflow was first tested on simpler geometries, such
as cubical blocks with spherical cavities. A synthetic data set of X-ray images was
generated for these models, which included realistic noise addition. The deep learning network was trained on this synthetic data set and tested on real X-ray images of
3D-printed cubes with spherical cavities. The results demonstrated that the network
could accurately segment the cavities, despite distortions introduced by 3D-printing
errors.

**100** Advances in Hardware Design for Security and Trust

**Figure 5.27** The X-ray simulation from the CADs using gVirtualXRay.

**Figure 5.28** (a) A real X-ray image and (b) synthetic image.

Next-Generation Semiconductor Reverse Engineering **101**

**Figure** **5.29** CADs of (a) missing bond wire and (b) dented packaging, (c) the synthetic image with these defects, and (d) the zoomed-in version of the defects.

**102** Advances in Hardware Design for Security and Trust

**5.4.2.4** **Application To Pcb X-Ray Images**

After successfully validating the approach on simple geometries, the method was
applied to segment X-ray images of PCBs. Synthetic data sets were generated by
creating basic geometries that resembled PCB layouts, with features such as hollow
circles representing junctions and lines representing traces. Real noise profiles were
added to these synthetic images to create a training data set.

The trained networks were then tested on real PCB X-ray images. The results
showed that both networks could accurately segment the PCB content, including
junctions and traces. However, the networks struggled with features not present in the
training data set, highlighting the need for diverse training data to cover all possible
variations in real-world images.

**5.4.2.5** **Scalability and Limitations**

The proposed method offers significant scalability, as generating larger and more diverse data sets only requires additional computational resources. However, the quality of the training data depends on the level of detail captured by the synthetic models. If the models are too simplistic, the training data may not cover the full range of
variations present in real-world images. Additionally, the method still relies on a few
real images to calculate noise profiles, which may limit its applicability in scenarios
where such images are unavailable.

**5.4.2.6** **Summary**

This study presents a novel approach to address the shortage of labeled data for training automated image segmentation methods in PCB reverse engineering. By generating synthetic X-ray images with inherent labels, the proposed method eliminates the
need for costly image acquisition and manual labeling. The method has demonstrated
its effectiveness in training deep learning networks to segment PCB X-ray images,
with potential applications in other imaging modalities, such as scanning electron
microscopy. The scalability and flexibility of the approach make it a powerful tool
for automating reverse engineering and defect detection tasks in microelectronics.
Future work will focus on refining the method to generate more realistic and diverse
synthetic data sets, further enhancing the performance of deep learning algorithms in
real-world applications. A detailed description of this technique has been provided
in [4] (Figures 5.30–5.37).

**5.5** **TECHNICAL ROAD MAP**

Implementing the next-generation reverse engineering techniques and capabilities
discussed in this chapter requires a strategic approach that integrates advanced
technologies with current industry practices. The following technical road map outlines the key steps and milestones for adopting and scaling these innovations across
different applications in electronics and microelectronics reverse engineering.

Next-Generation Semiconductor Reverse Engineering **103**

**Figure** **5.30** The air X-ray images (left and middle), and the noise profile extracted
(right).

**Figure** **5.31** Left: a real 2D X-ray projection of a 3D-printed object, a cubic with a
spherical cavity; middle: segmentation result produced by the ML algorithm that has
been trained only with synthetic data; right: overlay of the X-ray 2D projection and
the segmentation.

**Figure 5.32** Four instances of synthetic images prior to noise addition.

**5.5.1** **INITIAL ASSESSMENT AND INFRASTRUCTURE DEVELOPMENT**

 - Evaluate Current Capabilities: Assess the existing reverse engineering
tools and techniques used within your organization or research environment. Identify the gaps in precision, speed, and data analysis capabilities
that can be addressed by integrating femtosecond laser delayering, correlative imaging, and cloud-based analysis.

**104** Advances in Hardware Design for Security and Trust

**Figure 5.33** The synthetic images after contrast variation and addition of real noise.

**Figure** **5.34** The corresponding board content, junction, and connection masks for
the synthetic images.

 - Invest in Equipment: Procure or upgrade essential equipment such as
femtosecond lasers, advanced microscopy systems (including confocal and
SEM), and high-performance computing resources. Ensure that the infrastructure supports real-time data processing and integration with cloud platforms.

 - Build a Cloud-Enabled Environment: Set up a secure, scalable cloud
environment to host data storage, processing, and ML algorithms. Ensure
that the platform is compatible with existing systems and supports seamless
data transfer from imaging devices.

Next-Generation Semiconductor Reverse Engineering **105**

**Figure 5.35** Top: the synthetic images; middle: segmentation of all the board content
(i.e., union of junctions and traces); bottom: segmentation of junctions.

**5.5.2** **INTEGRATION OF ADVANCED IMAGING TECHNIQUES**

 - Adopt Femtosecond Laser Delayering: Begin by integrating femtosecond laser delayering into existing workflows. Train personnel on the operation of the femtosecond laser system and develop protocols for its use in
different reverse engineering applications, from PCBs to advanced semiconductor devices.

 - Implement Correlative Imaging: Incorporate correlative multimodality imaging techniques, combining the strengths of SEM, confocal microscopy, and other relevant imaging modalities. Develop protocols for
capturing and integrating data from these multiple sources to create comprehensive data sets.

 - Standardize Image Analysis Workflows: Establish standardized workflows for image capture, data processing, and 3D reconstruction. Ensure
that these workflows are reproducible and scalable, allowing for consistent
results across different projects.

**106** Advances in Hardware Design for Security and Trust

**Figure** **5.36** Top: real PCB images; middle: segmentation of all the board content
(i.e., union of traces and junctions); bottom: segmentation of junctions.

Next-Generation Semiconductor Reverse Engineering **107**

**Figure** **5.37** Left: real PCB images; middle: processed and overlaid segmentation
outputs from the two networks; right: fused images of the X-ray and segmentation.

**5.5.3** **DEVELOPMENT AND DEPLOYMENT OF MACHINE LEARNING**
**MODELS**

 - Create Synthetic Data Sets: Generate synthetic data sets to train ML models for automated defect detection, netlist extraction, and PCB reverse engineering. Leverage the cloud environment to create, store, and manage these
data sets efficiently.

 - Train and Validate Machine Learning Models: Develop ML algorithms
tailored to your specific reverse engineering needs. Validate these models
using real-world data to ensure accuracy and reliability. Continuously update the models with new data to improve performance.

 - Deploy Automated Analysis Tools: Integrate ML models into the cloud
platform to automate the analysis of imaging data. Develop user-friendly
interfaces for researchers and engineers to access and interpret the results
quickly.

**5.5.4** **CONTINUOUS IMPROVEMENT AND SCALING**

 - Monitor and Optimize Performance: Regularly review the performance
of the integrated reverse engineering system. Identify bottlenecks in the
process and areas for improvement, such as increasing the speed of data
processing or enhancing the resolution of imaging techniques.

**108** Advances in Hardware Design for Security and Trust

 - Expand Applications: As the system matures, explore its application to
new areas within microelectronics reverse engineering, such as the analysis
of more complex semiconductor devices or new material types. Adjust the
workflows and models as needed to accommodate these new challenges.

 - Collaborate and Share Best Practices: Collaborate with industry partners, academic institutions, and research organizations to share insights,
data, and best practices. Participate in industry forums and workshops to
stay updated on the latest advancements and contribute to the collective
knowledge base.

**5.5.5** **FUTURE INNOVATIONS AND RESEARCH**

 - Explore Hybrid Techniques: Continue researching hybrid techniques that
combine laser delayering with other advanced methodologies, such as FIB
polishing, to further enhance the accuracy and speed of reverse engineering.

 - Leverage Emerging Technologies: Keep an eye on emerging technologies, such as quantum computing or AI advancements, that could be integrated into the reverse engineering process. Evaluate their potential to
disrupt or improve current methods.

 - Plan for Scalability: As demand for reverse engineering grows, plan for
the scalability of your infrastructure, including cloud resources, imaging
equipment, and data processing capabilities. Ensure that the system can
handle increasing volumes of data and more complex analysis tasks.

**5.5.6** **IMPLEMENTATION OF SECURITY AND COMPLIANCE MEASURES**

 - Ensure Data Security: Implement robust security protocols to protect sensitive data during storage, processing, and transmission, particularly when
using cloud platforms. Compliance with industry standards and regulations
should be a priority.

 - Compliance with IP and Legal Requirements: Ensure that the reverse
engineering process adheres to intellectual property laws and regulations.
Establish clear guidelines for the use of reverse engineering results, particularly when dealing with 3PIP or proprietary technologies.

**5.6** **CONCLUSION**

In this chapter, we have presented a comprehensive approach to the reverse engineering of electronics and microelectronics, emphasizing innovative techniques such
as femtosecond laser delayering, correlative multimodality imaging, and cloud-based
data analysis. These advancements address the critical challenges faced in traditional
reverse engineering methods, such as the trade-off between resolution and speed,
non-flat layer exposure, and the accessibility of computational resources.

Next-Generation Semiconductor Reverse Engineering **109**

By integrating femtosecond laser technology with advanced imaging techniques
and leveraging cloud platforms, we have demonstrated significant improvements in
the precision, speed, and reliability of reverse engineering processes. The proposed
methodologies allow for detailed 3D reconstructions, accurate extraction of circuit
information, and automated defect detection, making them valuable tools for failure analysis, intellectual property verification, and competitive analysis within the
semiconductor industry.

Our discussion included various techniques, such as high-resolution 3D reconstruction using femtosecond laser delayering and digital microscopy, and precision
volumetric imaging via femtosecond laser and confocal microscopy. Each of these
techniques showcases the potential to enhance reverse engineering processes by providing high-resolution data and reducing analysis time.

Additionally, the cloud-enabled capabilities for automated defect detection and
deep learning-driven PCB reverse engineering highlight the importance of synthetic
data augmentation and machine learning in modern reverse engineering. These tools
not only improve the accuracy and efficiency of defect detection but also democratize
access to advanced analysis techniques by utilizing cloud resources.

In conclusion, the innovations discussed in this chapter represent significant
strides in the field of reverse engineering. As the semiconductor industry continues
to evolve, the need for rapid, accurate, and accessible reverse engineering techniques
will only grow. The methods and tools we have developed provide a robust foundation for meeting these demands and offer a road map for future advancements in the
field. Continued research and development in these areas will be crucial for keeping
pace with the increasing complexity of electronic devices and ensuring the integrity
and security of microelectronic systems.

**REFERENCES**

1. Choi, H., May, N., Phoulady, A., Suleiman, Y., DiMase, D., Shahbazmohamadi, S., &
Tavousi, P. (2022). Rapid three-dimensional reconstruction of printed circuit board using
femtosecond laser delayering and digital microscopy. Microelectronics Reliability, 138,
114659.
2. Phoulady, A., May, N., Choi, H., Suleiman, Y., Shahbazmohamadi, S., & Tavousi, P.
(2022). Rapid high-resolution volumetric imaging via laser ablation delayering and confocal imaging. Scientific Reports, 12(1), 12277.
3. Phoulady, A., Suleiman, Y., Choi, H., Moore, T., May, N., Shahbazmohamadi, S., &
Tavousi, P. (2023). Synthetic data augmentation to enhance manual and automated defect detection in microelectronics. Microelectronics Reliability, 150, 115220.
4. Phoulady, A., Choi, H., Suleiman, Y., May, N., Shahbazmohamadi, S., & Tavousi, P.
(2024). Synthetic data for semantic segmentation: A path to reverse engineering in
printed circuit boards. Electronics, 13(12), 2353.

# 6 Synthesis of Polymorphic
### Circuits for Hardware Security

Haimanti Chakraborty and Ranga Vemuri

**6.1** **INTRODUCTION**

Designing and fabricating a traditional integrated circuit (IC) in the recent times
has become expensive and complex. To reduce cost, many design houses are going fabless and outsourcing their designs to third-party, pureplay foundries that may
potentially be located overseas. An adversarial entity located at an untrusted fabrication facility may reverse engineer the design functionality without the design
house’s knowledge and illegally overproduce for personal benefit, resulting in loss
of revenue to the design house. They may also make malicious modifications to the
design, resulting in denial-of-service (DoS), leak confidential data, or produce counterfeit ICs [1–4]. “Business Action to Stop Counterfeiting and Piracy (BASCAP)”
had in its study found the global value of counterfeit and pirated goods estimated to
be $600 to $650 billion [5] before 2015. Therefore, incorporating security in modern
hardware designs has become crucial and is the need of the hour.

Split manufacturing (SM) [1, 6] and logic obfuscation (LO) [1, 6] are two powerful design-for-trust solutions that researchers have proposed over the past decade to
counter against the aforementioned security vulnerabilities. Both of these techniques
work by hiding the design functionality to safeguard IC designs before sending them
to potentially untrusted foundries for manufacturing. In SM, a design is typically
split into two parts: front end of line (FEOL) comprising the lower metal layers and
the transistors in the device layers, and back end of line (BEOL) comprising the rest
of the higher metal layers. The FEOL portion can be manufactured at an untrusted
foundry, whereas the BEOL at a trusted facility, and then the two parts can be integrated together at a trusted facility. The untrusted facility no longer having access to
the full IC provides some design protection. In LO (also known as logic encryption
or logic locking), some extra key gates are added to the design to lock the IC. It
can be operational only when the correct key bits (stored in a tamper-proof secure
memory and unknown to the untrusted foundry) are identified.

[DOI: 10.1201/9781003510949-6](https://doi.org/10.1201/9781003510949-6) **110**

Synthesis of Polymorphic Circuits for Hardware Security **111**

Nevertheless, a number of attack methodologies have been proposed that are able
to thwart SM and LO designs. One such potent attack is the Boolean satisfiability
attack (also known as the SAT attack) proposed by Subramanyan et al. [7]. At the
same time, SM- and LO-based designs incur PPA (performance, power, area) costs
from the addition of extra hardware components to obfuscate, and the fabrication
costs of the FEOL and the BEOL layers. Hence, it is imperative to design effective
and robust defense methodologies that maintain a balanced cost-security trade-off.

In the recent years, many researchers have been utilizing the advantages offered
by emerging technologies to secure hardware designs. As the conventional CMOS
(complementary metal oxide semiconductor) transistor scaling is approaching its
limits, numerous CMOS-compatible and beyond-CMOS devices are being proposed
and evaluated for use in future ICs. Some of these devices have area, power, and
performance benefits, while others offer security benefits due to their stochastic or
polymorphicbehavior. Polymorphic devices belong to the category of emerging technologies and novel devices. Researchers have used them to propose defense methods (such as using polymorphic transistor-based devices, or designing logic circuits
containing some polymorphic components besides the CMOS-based ones to logic
obfuscate a design) that have been shown to be resilient against the Boolean SAT Attack. More details pertaining to polymorphic electronics will be discussed in Section
6.2.
In this chapter, we will show how polymorphic transistor-based logic circuits can
be used to design RTL Bi-functional Units or Switch Boxes to generate secure hardware that is resilient against well-renowned attacks such as the Boolean satisfiability
attack [7] or the Network Flow Attack [8]. The novelty of such implementations is
that these methodologies have been implemented at a high level, requiring less hardware and do not require expensive resynthesis cycles or redesign of standard cells.
First, we will introduce polymorphicelectronics (ambipolarity) and discuss a number
of state-of-the-art methodologies.

**6.2** **POLYMORPHIC ELECTRONICS AND AMBIPOLARITY**

Polymorphism was demonstrated by A. Stoica’s group [9] at the NASA Jet Propulsion Laboratory as a novel class of electronic devices for a new approach to reconfiguration [10]. Some polymorphic devices exhibit the characteristics of ambipolarity,
which is defined as the placement of both positive and negative charge carriers under
bias constraints that enables a designer to change the polarity of the same device [11],
i.e., from an NMOS to PMOS and vice versa [2–4, 6, 11]. Such devices contain two
gate terminals, namely, the Control Gate (CG) and the Polarity Gate (PG), where
the former is responsible for turning the device on and off (similar to a conventional
CMOS-based transistor), and the latter changes the device polarity from p-type to
n-type or the reverse [2–4, 6, 11]. Silicon Nanowire Field Effect Transistor (or SiNW
FET) is an example of an ambipolar polymorphic device, proposed by De Marchi
et al. [12]. When the voltage at CG is 0 (1) and 1 (0), the NMOS (PMOS) device
is turned off and on respectively [2-4, 13]. In addition to this, if PG is low (high),
the device behaves as a PMOS (NMOS) transistor respectively [2–4,6,11]. Although

**112** Advances in Hardware Design for Security and Trust

other emerging devices such as Carbon Nanotube (CNT) FETs, Graphene SymFET
and Nanoelectromechanical (NEM) relays have polarity control characteristics as
well, SiNW FETs are compatible with the modern CMOS technology [2–4, 6, 11].

Due to the phenomenon of ambipolarity, polymorphic devices can readily support
logic encryption and camouflaging [1] if the voltage values supplied to the CG and
the PG are hidden from the untrusted foundry as key bits [2–4, 6]. If an incorrect
key-bit combination is supplied by an adversary at the third-party foundry, the device functionality would change completely, corrupting the final output. Polymorphic
circuits can be synthesized using a mix of polymorphic and standard CMOS-based
logic gates to construct Functional Units (FUs) at the Register-Transfer Level (RTL)
design. For example, if a single polymorphic circuit can behave as an adder or a
subtractor FU, it not only requires an attacker to identify the key bits correctly to
recognize if the actual functionality in use at a given instance of time would be an
adder or a subtractor, but it also helps save hardware resources, and a single circuit
can now be used as both an adder as well as a subtractor. This benefit is not available
when using components such as XOR or XNOR gates to perform logic obfuscation.
Details pertaining to this implementation will be discussed in Section 6.5.1.1. Another advantage that polymorphic circuits offer is that, when they are configured as
a switch box structure, they provide more key-bit combinations (thereby increasing
the attack complexity) for an adversary to decipher the correct functionality as compared to a standard CMOS-based switch box. More details pertaining to this can be
found in Sections 6.5.2 and 6.5.3.

**6.3** **HARDWARE** **SECURITY** **WITH** **POLYMORPHIC** **ELECTRONICS:**
**STATE-OF-THE-ART DEFENSE METHODOLOGIES**

A number of methodologies in the recent past have been proposed by researchers that
make use of polymorphic devices as the means to secure a hardware design. Alasad et
al. [11] proposed a logic locking technique using hybrid CMOS and emerging SiNW
FET transistors. The authors designed configurations wherein a single polymorphic
circuit could be used to perform the NAND/NOR functionality (as an example) using
SiNW FETs depending on the voltage values supplied to the CG/PG of that configuration, and this was implemented to replace the conventional XOR-based logic cone
for LO. The authors then evaluated the proposed technique based on performance
overhead and security metric [11].

Patnaik et al. [14] presented a hardware security technique using polymorphic and
stochastic spin-hall effect devices by employing the Giant Spin-Hall Effect (GSHE)
Switch to simultaneously enable camouflaging and locking within a single instance.
Using the GSHE switch, the authors proposed a powerful primitive that enabled
hiding all the 16 Boolean functions possible for two inputs [14]. The authors then
conducted a comprehensive study using the Boolean SAT attack [7] to demonstrate
superior resilience of the proposed technique in comparison to several others in the
literature [14].

Rangarajan et al. [15] proposed a dynamic camouflaging method using polymorphic devices by exploiting the multi-functionality, post-fabrication reconfigurability,

Synthesis of Polymorphic Circuits for Hardware Security **113**

and run-time polymorphism of the magneto-electric spin-orbit (MESO) spin device
to defend against the SAT attack [7].

Saxena et al. [16] proposed the ISPLock technique that utilizes a hybrid internal
state locking method using polymorphic gates to protect a design against the SAT
attack. The method first selects certain internal nodes from the circuit and then determines an internal state of the selected nodes using a simulator. It replaces all selected
gates with polymorphic gates and based on the simulator output, it camouflages the
internal states using polymorphic gates. The camouflaged internal state will be used
to corrupt the functionality of the primary outputs.

Parveen et al. [17] presented a Hybrid Polymorphic Logic Gate with 5-Terminal
Magnetic Domain Wall Motion Device that shows 74.23% power reduction and
7.14% transistor count reduction compared to its traditional CMOS counterpart. Edwards et al. [18] proposed a Physically Secure Logic Locking With Nanomagnet
Logic: a logic locking scheme utilizing the non-volatile properties of nanomagnet
logic (NML) to provide comprehensive protection against SAT-based and structural
threats. Angizi et al. [13] presented a hybrid spin-CMOS polymorphic logic gate
(HPLG) using a novel five-terminal magnetic domain wall motion device. The proposed HPLG is able to perform a full set of one- and two-input Boolean logic functions (i.e., NOT, AND/NAND, OR/NOR, and XOR/XNOR) by configuring the applied keys. Hassan et al. [19] proposed a logic locking scheme that leverages the
non-volatility of the NML family to achieve both physical and algorithmic security.
Polymorphic NML minority gates protect the obfuscation key against algorithmic attacks, while a strain-inducing shield surrounding the nanomagnets provides physical
security via a self-destruction mechanism.

**6.4** **LIMITATIONS OF HARDWARE SECURITY AT LOWER**
**ABSTRACTION LEVELS**

Although a number of polymorphic electronics–based defense methods have been
proposed by researchers in the recent past, most of them have been implemented at
lower abstraction levels, such as the gate and the layout levels, that may require expensive resynthesis cycles and/or redesign of standard cells [1, 3, 4, 6]. At the same
time, there is a greater hardware count at lower abstraction levels that make logic encryption or inclusion of other forms of hardware security methodologies more complex. With increased complexity of an IC design, designers are migrating to higher
abstraction levels for design automation [25] that has relatively fewer design components [2–4, 6]. Section 6.5 discusses three polymorphic electronics–based defense
methods, recently proposed at the high level.

**6.5** **HARDWARE SECURITY METHODOLOGIES USING**
**POLYMORPHIC ELECTRONICS AT HIGH LEVEL**

This section discusses three recently proposed defense methodologies using polymorphic circuits and switch boxes at high level (i.e., during High Level Synthesis [HLS] and Register-Transfer Level [RTL]) design stages. The first two

**114** Advances in Hardware Design for Security and Trust

methods based on logic obfuscation can defend against the SMT (Satisfiability Modulo Theories)–based RTL Logic Attack [21], which is primarily the Boolean SAT
attack at the RTL, and the third method based on combined logic encryption and
split manufacturing defends against the Network Flow Attack [8]. Sections 6.5.1 6.5.3 present the details of each of the three techniques.

**6.5.1** **ROBUST: RTL OBFUSCATION USING BI-FUNCTIONAL**
**POLYMORPHIC OPERATORS**

Chakraborty et al. [3] proposed a defense methodology based on how hybrid (polymorphic and standard CMOS combined) logic gate-based bi-functional circuits can
be utilized to construct RTL bi-functional polymorphic operators/functional units
(FUs) for RTL Obfuscation. The authors propose high-level synthesis algorithms for
scheduling and allocation of two operators at a time to the same bi-functional polymorphic FU, and further include a multiplier block element to one polymorphic FU
per benchmark circuit to test the robustness of the design against the SMT-based RTL
Logic Attack [21] since a multiplier was found to be a difficult problem for SAT and
SMT-based solvers [7].

**6.5.1.1** **Bi Functional Polymorphic Operators**

Figure 6.1 showcases an example representation of a 1-bit adder/subtractor bifunctional circuit, adapted from [22]. Utilizing this, the method [3] shows how a
polymorphic FU can be constructed for obfuscation. Polymorphic gates and the standard CMOS technology are used together to form the circuit, and the 1-bit structure
can be extended to multi-bit.

It is known that the Boolean expressions for Sum (S) and Carry (Cout) of a Full

Full Subtractor, the expressions corresponding to the symbols used in Figure 6.1
Adder are, respectively: S = A <sup>�</sup> B <sup>�</sup> Cin and Cout = AB + BCin + ACin. For a
Cout are in this case, Difference and Borrow, respectively. Since the expressions for
are,the sum/differencerespectively: S for= Aboth <sup>�</sup> theB <sup>�</sup> adderCin andand Ctheout subtractor= AB + ACarein the+ BCsame,in, whereit wouldS andbe
more important to camouflage the Cout expressions (for carry-out and borrow) to

**Figure 6.1** 1-bit full adder/subtractor bi-functional circuit representation at the gate
level. (Adapted from [3, 22].)

Synthesis of Polymorphic Circuits for Hardware Security **115**

**Figure** **6.2** Representation of the eight-transistor structure that can perform
AB/NAND and NOR/A + B functionalities by changing the 14 key bit values. The 14
key-bit configuration shown here generates the AB functionality. (Adapted from [3].)

distinguish between an adder or a subtractor. Figure 6.1 shows three conventional
CMOS-based gates being used, namely, two XNOR gates and one NOR gate. For
the purpose of obfuscation, the remaining two rectangular boxes can be replaced with
two bi-functional polymorphic gates. If the first box on top is configured to perform
the AB functionality and the box on the right be configured as a NOR gate, the entire
circuit would behave as a full adder. Likewise, if the first box is configured as a
NAND functionality and the second box as (A + B), the circuit would perform the
subtraction operation. The structures of the rectangular boxes for AB/NAND and
NOR/A + B can be designed as shown in Figure 6.2. By integrating two 2-transistor
polymorphic inverter/buffer structures from [12] and the 4-transistor polymorphic
NAND/NOR functionality from [11], four functionalities (AB/NAND and NOR/A
+ B) can be generated using the same circuit. The area overhead is low despite the
design requiring eight transistors for NAND or NOR, since two operator types can
be implemented in one.

Figure 6.2 shows the 8-transistor polymorphic circuit with the two 2-transistor
Inverter/Buffer in the first stage (the first inverter/buffer to get either input A or
A, and the second inverter/buffer to get either input B or B) that drives the 4transistor AB/NAND or the NOR/A + B structure. For a NAND functionality,
the correct key-bit configuration K1K2K3K4K5K6K7K8K9K10K11K12K13K14=
11001100100110. Similarly, the correct bits for the AB functionality in the same order would be 11001010011001. For the second polymorphic block in Figure 6.1,
the NOR and the (A + B) functions can be obtained in Figure 6.2 by key bits
11001100011001 and 10101100100110, respectively.

**116** Advances in Hardware Design for Security and Trust

Thus, in Figure 6.2, it can be observed how the same circuit structure can be used
to build four functionalities, resulting in design camouflaging when the values of the
PGs and supplies (power and ground) are hidden as key bits while sending the design
to an untrusted facility. It can be seen that the adder/subtractor bi-functional circuit in
Figure 6.1 requires two polymorphic blocks for the AB/NAND and NOR/A + B functionalities, and that one polymorphic block in Figure 6.2 requires 14 key-bits. Thus,
using two such blocks in Figure 6.1 would require 28 key bits per adder/subtractor
bi-functional FU. Therefore, the total number of possible keys for a single adder/subtractor FU would be 2 <sup>28</sup> . With more FUs (same as discussed above or different
bi-functional operations) used by a design, the key bits could thereby be increased
for more security. Another way to increase key-bit size is to replace one or more
conventional CMOS logic gates with bi-functional polymorphic gates.

Following this technique, one can also construct other bi-functional polymorphic
FUs depending on the operators needed by the benchmark circuits used. Sekanina
et al. [23] discusses an evolutionary design of an adder/multiplier bifunctional polymorphic circuit. Beyond arithmetic operators, if logical operators are required, some
configurations, such as AND/OR, NAND/NOR, and XOR/XNOR designs, are discussed in [11]. Because this RTL obfuscation method is based on constructing bifunctional polymorphic FUs using polymorphic gates, not only can one FU serve the
purpose of obfuscation, requiring recognition between the two types of operations
taking place at a given time, but it also saves area of having two FU functionalities
in one. Two different operators can be allocated in high-level synthesis to the same
polymorphic FU, and the more the connections of two different operation types entering the same bi-functional FU, the more would be the effort needed by the attacker
to identify if each of such connections would belong to the first operator type or the
second (that is, having to identify each of the bits of the 28 key bits correctly per connection per FU, to determine if the FU is an adder or a subtractor, as an example).

**6.5.1.2** **High-Level Synthesis (HLS) and Security-Aware HLS Algorithms**

The first algorithm for the Security-Aware Scheduling in [3] begins by calculating
the security-weight w and the scheduling mobility µ of each node of a design represented as a Data Flow Graph (DFG) in high level. w is the arithmetic sum of two
metrics, namely, PO and FO, where PO is the number of primary outputs a particular node has paths ending in, and FO is the fanout count or the number of output
dependencies/edges of that node to the next node(s). The more the numerical values
of PO and/or FO, the more the number of register values would be corrupted upon
incorrect identification of the functionality of the bi-functional FU for the respective
interconnections at the RTL stage.

µ represents the scheduling range of a node, subject to meeting design timing constraints, and is calculated using the formula: As-Late-As-Possible (ALAP) schedule
time of the node – As-Soon-As-Possible (ASAP) schedule time of the node + 1] [24].
The next step is to schedule all the nodes belonging to the critical path (CP) (µ = 1;
hence, these nodes have a fixed time step for scheduling) to meet design timing. The
remainder of the algorithm deals with scheduling all remaining nodes with µ - 1.

Synthesis of Polymorphic Circuits for Hardware Security **117**

Selecting two operator types from this list that corresponds to the two operators of a
bi-functional FU, if there are nodes with w > 2 (i.e., either one of PO, FO, or both
are > 1; and hence will corrupt multiple RTL registers upon incorrect FU operation
identification), they would be given higher priority. Next, if CP nodes with w > 2 are
available as well, then the CP node with the maximum w value is selected. And then
the high-priority node is scheduled to the time step different from this CP node where
resource cost remains minimal (as discussed in [24]). Being in different time steps,
both these weighted nodes (affecting multiple RTL registers) could be assigned the
same bi-functional FU for greater corruptibility. If there are nodes with w = 2, that is,
both PO and FO are 1 each, they would be scheduled in the time step corresponding
to the least resource cost [24]. Once scheduled, the successor node(s) (if any) of the
most recently scheduled nodes are scheduled by placing them in the time step with
minimal resource cost. Once the first pair of operators are scheduled, the algorithm
moves to the next pair of resource types and the process repeats until all nodes are
scheduled. In case of odd number of operators, they would be be scheduled in time
steps with minimal resource cost.

The second algorithm allocates all high-priority weighted nodes w ≥ 2 (two different operations at a time), scheduled in different time steps to the same bi-functional
FU [3]. Other nodes of the same resource-type pair (ri,j) belonging to overlapping
time steps would be assigned a different bi-functional FU. This repeats until all resources are assigned pairwise to the bi-functional FUs. If the number of operator
types is odd, it is allocated to a bi-functional FU (bi-FU) performing the second
functionality as a random one. The two aforementioned algorithms are represented
figuratively as two flowcharts in Figures 6.3 and 6.4, respectively.

**6.5.1.3** **Enhanced Robustness with Multiplier Block Element**

It has been previously observed that SAT attack [7] and SMT-based attack solvers

[21] take a long time in a design containing multiplier blocks [3]. As a result, a
multiplier block was included in only one of the polymorphic FUs (preferably to the
one with the maximum RTL interconnections allocated) per benchmark circuit to
check the resilience against the SMT-based attack [3, 21]. The proposed structure is
shown in Figure 6.5.

The proposed technique is to connect the multiplier inputs to logic value 0, which
would output logic 0. Using this as one input to an XOR gate, and another of the XOR
input connected to the FU output, the final output would be the actual FU output.
Thus, the final output functionality of the FU does not change and the multiplier
essentially acts as a dummy element. Because, only multiplier with an XOR gate is
used for one bi-FU per design, the overhead is not significantly high.

**6.5.1.4** **Experimental Results**

The method was evaluated using 12 different benchmarks from [20] on the a system
with AMD Ryzen 7 2700X Eight-Core Processor and 15GB memory [3].

**118** Advances in Hardware Design for Security and Trust

**Figure 6.3** Security-aware scheduling flowchart. (Adapted from [3].)

Once the security-aware scheduling and allocation are performed pairwise, the
RTL datapaths (containing the bi-functional polymorphic-basedfunctional units) and
controllers are obtained for each benchmark circuit (baseline design, i.e., the design
without the multiplier) [3]. Then, a multiplier block (as shown in Figure 6.5) to one
FU was included and the SMT-based RTL Logic Attack [21] was mounted.

The area for different benchmarks for the baseline polymorphic FU design (without multiplier) and the one with the multiplier block included were measured, and
compared with the area overheads of the TAO (Techniques of Algorithmic Obfuscation) method [25]. The results are shown in Table 6.1. The resilience of the designs
containing the multiplier block were tested against the SMT-based attack [21] and it
was found that for each of the 12 benchmarks, it timed out after 10 hours without
deciphering the key.

Synthesis of Polymorphic Circuits for Hardware Security **119**

**Figure 6.4** Security-aware allocation flowchart. (Adapted from [3].)

**Figure** **6.5** Multiplier block included within a bi-functional polymorphic FU.
(Adapted from [3].)

**6.5.2** **RTL** **INTERCONNECT** **OBFUSCATION** **BY** **POLYMORPHIC** **SWITCH**
**BOXES**

In this section, another defense methodology proposed by Chakraborty et al. [4]
is discussed. The method is about designing a simple switch box (SB) using

**120** Advances in Hardware Design for Security and Trust

**Table 6.1**
**Comparison** **of** **Area** **Overhead** **(in** **%)** **Between** **the** **TAO** **Method** **(DFG** **Vari-**
**ants)** **[20],** **ROBUST** **Method** **Without** **Multiplier** **and** **ROBUST** **Method** **With**
**Multiplier**

Benchmark TAO ROBUST ROBUST
Name Method [20] Method (W/O *) Method (With *)
BM1 12% 0.5% 8%
BM2 18% 1% 9%
BM3 25% 1.5% 10%
BM4 31% 2% 12%
BM5 13% 0.7% 8%
BM6 11% 0.3% 7.5%
BM7 12% 0.4% 8%
BM8 23% 1% 9%
BM9 25% 1.4% 10%
BM10 24% 1.3% 9.5%
BM11 25% 1.5% 10%
BM12 26% 1.6% 11%
Adapted from [3]

polymorphic transistors for RTL Interconnect Obfuscation. Similar to Section 6.5.1,
this method also includes modified high-level synthesis algorithms for scheduling
and allocation of data flow graph nodes and edges to assign them to RTL functional
units that would impact multiple outputs such that when the polymorphic SBs are
included at those specific locations, they would corrupt all of those outputs when an
attacker incorrectly identifies the polymorphic SB key-bits to unlock them. Finally,
the obfuscated design is tested against the SMT-based RTL Logic Attack [21] to
evaluate the robustness of the obfuscation method.

**6.5.2.1** **Polymorphic Switch Boxes**

A switch box using standard CMOS transistors for obfuscation has been proposed in

[26]. Figure 6.6(a) shows a CMOS-based switch box (SB) composed of four NMOS
pass transistors (and SRAMs to store the programming bits) and Figure 6.6(b) shows
the two modes (crisscross and parallel) in which it can be configured to obfuscate a
gate-level design as implemented in [4, 26].

If in Figure 6.6(a), P1P2P3P4 key vector = 0110, it would be a crisscross SB connection and if P1P2P3P4 key vector = 1001, we would get a parallel SB connection.
Out of the two modes, only one would be correct and any other bit combinations
would shuffle the correct interconnect connectivity. Since this configuration has four
key-bits to identify a connectivity, the total number of possible key-bit combinations

Synthesis of Polymorphic Circuits for Hardware Security **121**

**Figure 6.6** (a) Standard CMOS switch box using 4 NMOS pass transistors; (b) Parallel and crisscross connection modes using a switch box at gate level. (Adapted
from [4, 26].)

for an attacker to identify the correct bits is 2 <sup>4</sup> = 16, out of which one key vector is
responsible for the parallel connection and another for the crisscross connection.

Now, if all four standard CMOS transistors are replaced with four polymorphic
transistors, each transistor would now have a Polarity Gate (PG) key-bit value and a
Control Gate (CG) key-bit value, thus doubling the number of key-bits per transistor,
resulting in more effort required by an attacker to guess the correct key-bits per

**122** Advances in Hardware Design for Security and Trust

**Figure 6.7** Representation of a 4-transistor polymorphic switch box. (Adapted from

[4].)

polymorphic SB. Figure 6.7 showcases a polymorphic SB configuration containing
four polymorphic transistors.

If both CG and PG are 0, the polymorphic transistor behaves as a PMOS transistor
in ON state. When both are 1, it behaves as an NMOS ON transistor. When CG is
0 and PG is 1, it behaves as an NMOS OFF transistor, and when CG is 1 and PG is
0, it behaves as a PMOS OFF transistor. If these values are considered as key-bits
for obfuscation, then in Figure 6.7, if C1P1C2P2= 0010 or 1101 or 0001 or 1110, X
would be connected to Z, and if C3P3C4P4= 1000 or 0111 or 1011 or 0100, Y would
be connected to W, resulting in a parallel connection. Then, if C1P1C2P2= 1000 or
0111 or 1011 or 0100, X would be connected to W, and when C3P3C4P4= 0010 or
1101 or 0001 or 1110, Y would be connected to Z, making it a crisscross connection.
Although this implies that one can have more than one key vector to make a parallel
or a crisscross connection, the total number of key bit combinations per polymorphic
SB has now increased from 16 (CMOS SB) to 2 <sup>8</sup> = 256 possible combinations. Any
other key-bit combinations would shuffle the correct connectivity. If more than one
polymorphic SB is inserted (say, x) subject to allowable area constraints, the attack
complexity (interconnect wire combinations) would increase exponentially to 2 <sup>x</sup> [23]
with each polymorphic SB having 256 possible key-bit combinations.

Section 6.5.2.3 shows that some SBs can be configured as parallel and some SBs
as crisscross, and can be placed in strategic locations to confuse an attacker. One
way to include SBs strategically would be between two interconnects which enter an
RTL functional unit that fan out their output results to more than one register. This
is shown in Figure 6.8. In doing so, upon incorrect identification of the polymorphic
SB key-bits, all the output register values would be corrupted. This can be attained
by assigning specific nodes and edges of the design at the Data Flow Graph stage
(to RTL functional units) via security-aware scheduling and allocation (High Level
Synthesis or HLS) to generate the RTL.

Synthesis of Polymorphic Circuits for Hardware Security **123**

**Figure 6.8** Strategic location for polymorphic switch box insertion for RTL obfuscation type 1: Parallel and crisscross connections impacting multiple output registers.
(Adapted from [4].)

**6.5.2.2** **Security-Aware HLS Algorithms**

The modified security-aware scheduling and allocation algorithms proposed in this
methodology are similar to those in Section 6.5.1.2 with the difference being, in Section 6.5.1.2, two operators were selected at a time for the bi-functional FU, however,
in this method, one operator is selected at a time.

**6.5.2.3** **Polymorphic Switch Box Insertion**

Implementing the algorithms in Section 6.5.2.2 helps increase high-priority weighted
nodes to be assigned the same FU, provided they could be scheduled in different time
steps and subject to design latency bound constraints. The security weights were calculated based on nodes having paths ending in more than one primary output and/or
if they had fanout of more than one. From prior knowledge, it is known that if DFG
edges cross at least one common time step boundary (that is, if they have an overlapping time step boundary), they need to be assigned different registers. Subject
to design timing constraints, if more high-priority weighted nodes are allocated to
the same RTL FU, the total security weight combined from all such nodes would
increase. This implies that if an obfuscator (polymorphic SB, in this case) is placed
between two interconnects that enter such an FU (and then incorrectly unlocked with
the wrong keys by an adversary), more output register values would get corrupted.
Such a location is considered as one of the strategic ones for the polymorphic SB
insertion. A second type of strategic location is when a polymorphic FU is included
between two interconnects entering two FUs of different resource types (say, one

**124** Advances in Hardware Design for Security and Trust

**Figure 6.9** Strategic location for polymorphic switch box insertion for RTL obfuscation type 2: Parallel and crisscross connections entering two different resource types.
(Adapted from [4].)

being a multiplier FU and another one being an adder FU, etc.). In doing so, if the
polymorphic SBs are again incorrectly unlocked with the wrong keys, the functionality of the intended design would change. Based on the allowed area constraints, as
more polymorphic SBs are included, the output corruptibility would increase. The
authors propose using a mix of a few parallel-type polymorphic SBs and a few of
the crisscross variants to increase confusion for an attacker. These are illustrated in
Figures 6.8 and 6.9.

**6.5.2.4** **Experimentation and Results**

The method [4] was evaluated using 10 benchmarks from [20] on a system with
AMD Ryzen 7 2700X Eight-Core Processor and 15GB memory. After executing
the security-aware scheduling and allocation algorithms for all the operators based
on security-aware weights, RTL data paths and controllers were obtained for each
benchmark circuit. Then, depending on the allowed area constraints, polymorphic
SBs of the parallel and crisscross variants were inserted at strategic locations, as
discussed in Section 6.5.2.3. The SMT-based RTL Logic Attack [21] was then run
on the RTL interconnect obfuscated designs. For different benchmarks, the output
error rate versus the percentage of area overhead (due to addition of the polymorphic
SBs) were measured, where Output Error Rate (OER) is defined as the percentage
of erroneous outputs obtained. The results are shown in Table 6.2. It can be seen
that the error rate is increasing with the increase in the number of polymorphic SBs
(represented as the percentage of area overhead increase).

The robustness of the RTL interconnect obfuscation method was tested against
the RTL Logic Attack [21] and it was found that for each of the 10 benchmarks

Synthesis of Polymorphic Circuits for Hardware Security **125**

**Table 6.2**
**Increase in Output Error Rate (OER) (in %) with Increase in the Polymorphic**
**Switch Box Count (Represented as % of Area Overhead)**

Area Overhead Due to
Benchmark Name Polymorphic SB Insertion (in %) Error Rate (in %)
5% 14%
BM1 10% 31%
15% 52%
20% 65%
5% 12%
BM2 10% 35%
15% 56%
20% 68%
5% 13%
BM3 10% 37%
15% 58%
20% 70%
5% 15%
BM4 10% 38%
15% 60%
20% 71%
5% 17%
BM5 10% 39%
15% 62%
20% 73%
5% 18%
BM6 10% 40%
15% 60%
20% 74%
5% 20%
BM7 10% 42%
15% 64%
20% 75%
5% 22%
BM8 10% 44%
15% 65%
20% 76%
5% 23%
BM9 10% 46%
15% 67%
20% 78%
5% 24%
BM10 10% 40%
15% 68%
20% 80%

Adapted from [4].

**126** Advances in Hardware Design for Security and Trust

obfuscated with the 20% area overhead and using a mix of the four encryption configurations as shown in Figures 6.8 and 6.9, it timed out after 10 hours without deciphering the key.

**6.5.3** **COMBINED SPLIT MANUFACTURING (SM) AND LOGIC**
**OBFUSCATION (LO) FOR SECURE 3D IC DESIGN**

This section discusses yet another defense technique proposed by Chakraborty et
al. [6]. This is a combined methodology incorporating Split Manufacturing (SM)
and Logic Obfuscation (LO) for enhanced security for 3D IC designs at a high level
(DFG stage). The two defense methods discussed in Sections 6.5.1 and 6.5.2 were
based on 2D Integration. 3D Integration offers several advantages over 2D: difficult
reverse engineering, lower power consumption, higher bandwidth between vertical
device layers. 3D Integration allows heterogeneous process nodes to be used for the
circuit layers, and is expected to continue to provide “Moore” equivalent integration
benefits over the next decade [1, 6].

The authors [6] present a BEOL signal selection method by assigning securityaware weights to edges of the design represented as a DFG, such that high-priority
weighted edges are marked at this stage for actual BEOL signal lifting to take place
later at the post-route layout design stage. This technique also helps identify suitable
locations to include obfuscation elements to the design to perform LO. The obfuscation elements used are SBs designed using emerging technologies (polymorphic or
ambipolar transistors).

Another technique employed in this methodology was to have multiple FEOL
chiplets by partitioning the FEOL design and allowing the manufacture of each
chiplet at different untrusted facilities. In doing so, not only does each untrusted
foundry have any access to the BEOL signals, but also no knowledge of all the devices used in the complete design, enhancing security. The authors leverage this to
their advantage and bi-partition the design to have two FEOL chiplets as the top and
the bottom stacks of the 3D IC, bonded using the face-to-face (F2F) method. The
selected BEOL signals and the polymorphic SBs (PSBs) are located in the Redistribution Layer (RDL), which is sandwiched between the two FEOL chiplets to form
the 3D IC structure. The secure 3D IC structure is shown in Figure 6.10.

**Figure 6.10** The secure face-to-face 3D IC structure. (Adapted from [6].)

Synthesis of Polymorphic Circuits for Hardware Security **127**

**Figure 6.11** Combined split manufacturing and logic obfuscation method flowchart.
(Adapted from [6].)

**6.5.3.1** **Methodology**

The algorithm for this method begins by calculating the security weight wi of each
DFG edge ei. wi is the arithmetic sum of two metrics, PO and FO, where PO is the
number of primary outputs each edge ei has paths ending in, and FO is the fanout
count or the number of output dependencies/edges of the node (to which ei is an
incoming edge) to the next node(s). The higher the values of PO and/or FO, the
higher is the number of output values that would be corrupted if ei is delegated
to the BEOL and reconstructed incorrectly by an attacker. Following this, an initial DFG bi-partitioning into two FEOL chiplets FC1 and FC2 is performed using
the Fiduccia-Mattheyses (FM) method [27] supporting multi-terminal nets to obtain
a near-minimal cutsize (edge connections between the two partitions) among the
two balanced (similar component count in each) partitions. It is known that a nearminimal cutsize does not ensure maximal security (since cutsets are assigned to the
BEOL, and fewer signals in BEOL would make reverse engineering the functionality
easier for an attacker) but is a good starting point to gradually add security, subject
to PPA (power, performance, area) constraints. Once bi-partitioned, the cells (nodes)
are unlocked. Then two edges ei,max and e j,max are selected with the maximum w
values, and are marked as the select signals to be lifted to the BEOL at the post-route
layout design stage, as long as the cutsize percent increase is within the allowed
limit. The next steps assign predecessor and successor nodes of ei,max and e j,max to
FEOL partitions FC1 and FC2, subject to the Area Imbalance (AI) factor being met

**128** Advances in Hardware Design for Security and Trust

**Figure** **6.12** (a) Normal bi-partitioning; (b) Secure bi-partitioning. (Adapted from

[1, 6, 28].)

(to ensure similar area in each FEOL partition), as discussed in [28]. Shuffling and
swapping of these nodes are done for some to be in FC1 and some in FC2, to include
randomization. Their pins would be swapped at the layout synthesis stage [29] to increase confusion for the attacker to recover the correct signal(s), and have some PSB
configurations set as parallel and some as the crisscross type. The next steps identify locations for the PSBs between ei,max and e j,max if the area overhead is within a
certain allowed limit. The algorithm is represented as a flowchart in Figure 6.11.

To ensure secure partitioning, at least one path between every connected PI/PO
(Primary Input/Primary Output) pair must be cut [1, 6, 28], as illustrated in Figure
6.12. In Figure 6.12(a), the functionality of the primary output of node ‘a’ is exposed
since its input cone is entirely within one FEOL partition. Similarly, the inputs of
node ‘e’ and the output of node ‘f’ are in one FEOL partition, and node ‘e’ inputs
are unable to influence a cut signal. These are modified in Figure 6.12(b) to increase
output corruptibility by cutting PI/PO pair(s), and this can be performed if it is within
the range of the cutsize cost limit.

The entire process in the aforementioned algorithm is repeated for the next set
of maximum w valued edges and continued until the permitted limits to cutsizeincrease, area-increase, and the area-imbalance factor are reached.

Following these steps, the FEOL partitions independently go through the design
flow from high-level synthesis to layout to fabrication, and later integrated together.
Figure 6.13 shows the design process for the secure 3D IC generation.

Synthesis of Polymorphic Circuits for Hardware Security **129**

**Figure 6.13** Proposed secure 3D IC design process. (Adapted from [6].)

**6.5.3.2** **Experimentation and Results**

The authors [6] evaluate the method using benchmarks from UCSB’s ExPRESS
Benchmark Set [20] on a system with AMD Ryzen 7 2700X Eight-Core Processor
and 15GB memory.

Once the FEOL partitions are generated, the BEOL signals marked and the PSB
locations identified, the design goes through HLS, RTL design, gate-level design
(using Synopsys Design Compiler), and layout synthesis (using Cadence Innovus
and Nangate 45nm Open Cell Library). Then, pin swapping is performed [29] on the
FEOL partitions, followed by lifting off the selected BEOL signals and including the
PSBs to the RDL.

Attack Correctness (AC): Attack Correctness (AC) is defined as the percentage of
BEOL signals correctly recovered by an attack [1]. The Network Flow Attack [8]
for each benchmark was run after the post-route stage of layout synthesis, once on
the normal version, then followed by lifting different percentages of the DFG edges
(cutsizes) to BEOL (RDL) and PSBs included (represented as percentage of area
overhead in Table 6.3). For each case, the recovered nets were compared with the
actual connections to obtain the Attack Correctness (AC) values. The results in Table
6.3 show the AC values for each benchmark with different percentages of edges
lifted and the area overhead due to PSBs inclusion when the Network Flow Attack

**130** Advances in Hardware Design for Security and Trust

**Table 6.3**
**Attack Correctness** **(AC) Values** **(in %)** **for** **the** **Benchmarks** **with Increases** **in**
**the Percentage of Edges Lifted to the BEOL and the Polymorphic Switch Box**
**Insertion (Represented as % of Area Overhead)**

Edges Lifted (in %) and Area Overhead
Benchmark (in %) due to PSB Insertion AC (in %)
(0%, 0%) 90%
(15%, 5%) 71%
BM1 (30%, 10%) 62%
(45%, 15%) 57%
(60%, 20%) 41%
(0%, 0%) 97%
(15%, 5%) 80%
BM2 (30%, 10%) 60%
(45%, 15%) 51%
(60%, 20%) 40%
(0%, 0%) 93%
(15%, 5%) 77%
BM3 (30%, 10%) 59%
(45%, 15%) 48%
(60%, 20%) 39%
(0%, 0%) 97%
(15%, 5%) 76%
BM4 (30%, 10%) 57%
(45%, 15%) 42%
(60%, 20%) 33%
(0%, 0%) 96%
(15%, 5%) 70%
BM5 (30%, 10%) 52%
(45%, 15%) 40%
(60%, 20%) 29%
(0%, 0%) 100%
(15%, 5%) 82%
BM6 (30%, 10%) 80%
(45%, 15%) 77%
(60%, 20%) 62%
(0%, 0%) 96%
(15%, 5%) 90%
BM7 (30%, 10%) 77%
(45%, 15%) 75%
(60%, 20%) 69%
(0%, 0%) 97%
(15%, 5%) 90%
BM8 (30%, 10%) 72%
(45%, 15%) 70%
(60%, 20%) 56%
(0%, 0%) 96%
(15%, 5%) 76%
BM9 (30%, 10%) 74%
(45%, 15%) 55%
(60%, 20%) 37%
(0%, 0%) 90%
(15%, 5%) 71%
BM10 (30%, 10%) 62%
(45%, 15%) 56%
(60%, 20%) 41%

Adapted from [6].

Synthesis of Polymorphic Circuits for Hardware Security **131**

**Figure** **6.14** Routed wirelengths for the design with unlifted and different percentages of lifted edges [6].

was run [8]. As can be noted, even with a small percentage of edges lifted and area
overhead, the Network Flow Attack fails with a significant drop in AC.

Security Versus Cost: The authors have computed for each benchmark the routing
wirelengths for the normal and the other variants with the different percentages of
edges lifted. These are shown in Figure 6.14. It can be observed that the routed
wirelength has increased minimally with the increase in the percentage of edges
lifted.

**6.6** **CONCLUSION**

This chapter presents an overview of how polymorphic-based devices and circuits
can be used to secure hardware designs. As the conventional CMOS transistor scaling approaches its limits, numerous CMOS-compatible and beyond-CMOS devices
are being proposed and evaluated that have performance, area, power, state-of- and
security benefits due to their polymorphic behavior, and at the same time resilient
to potent attacks such as the Boolean satisfiability (SAT) attack. Some of these proposed methods have been discussed in Sections 6.3 and 6.5, the former discussing
the state of the art defense methods, and the latter elaborating details pertaining to
more recently published methods at the high level. Polymorphic electronics continues to be promising in the design and security of future integrated circuits and opens
directions for great potential in future research.

**132** Advances in Hardware Design for Security and Trust

**REFERENCES**

1. R. Vemuri and S. Chen, “Split manufacturing of integrated circuits for hardware security
and trust: methods, attacks and defenses,” Springer, 2021.
2. H. Chakraborty and R. Vemuri, “Split manufacturing based secure hardware design by
beol signal selection in high level synthesis,” in 2023 IEEE 66th International Midwest
Symposium on Circuits and Systems (MWSCAS), pp. 1083–1087, IEEE, 2023.
3. H. Chakraborty and R. Vemuri, “Robust: RTL obfuscation using bi-functional polymorphic operators,” in 2024 37th International Conference on VLSI Design and 2024 23rd
International Conference on Embedded Systems (VLSID), pp. 499–504, IEEE, 2024.
4. H. Chakraborty and R. Vemuri, “RTL interconnect obfuscation by polymorphic switch
boxes for secure hardware generation,” in 2024 25th International Symposium on Quality Electronic Design (ISQED), pp. 1–8, IEEE, 2024.
5. S. Verma, R. Kumar, and P. Philip, “Economic and societal impact of global counterfeiting and piracy,” Pacific Business Review International, vol. 6, no. 12, 2014.
6. H. Chakraborty and R. Vemuri, “Combined split manufacturing and logic obfuscation
based on emerging technologies at high level for secure 3D IC design,” in 2024 IEEE
67th International Midwest Symposium on Circuits and Systems (MWSCAS), pp. 1403–
1407, IEEE, 2024.
7. P. Subramanyan, S. Ray, and S. Malik, “Evaluating the security of logic encryption
algorithms,” in 2015 IEEE International Symposium on Hardware Oriented Security
and Trust (HOST), pp. 137–143, IEEE, 2015.
8. Y. Wang, P. Chen, J. Hu, and J. Rajendran, “The cat and mouse in split manufacturing,”
in Proceedings of the 53rd Annual Design Automation Conference, pp. 1–6. Association
for Computing Machinery, 2016.
9. A. Stoica, R. Zebulum, and D. Keymeulen, “Polymorphic electronics,” in International
Conference on Evolvable Systems, pp. 291–302, Springer, 2001.
10. Z. Gajda and L. Sekanina, “On evolutionary synthesis of compact polymorphic combinational circuits.,” Journal of Multiple-Valued Logic and Soft Computing, vol. 17, no. 56, pp. 607–631, 2011.
11. Q. Alasad, J.-S. Yuan, and Y. Bi, “Logic locking using hybrid CMOS and emerging
SiNW FETs,” Electronics, vol. 6, no. 3, p. 69, 2017.
12. M. De Marchi, D. Sacchetto, S. Frache, J. Zhang, P.-E. Gaillardon, Y. Leblebici, and
G. De Micheli, “Polarity control in double-gate, gate-all-around vertically stacked silicon nanowire FETs,” in 2012 International Electron Devices Meeting, pp. 8–4, IEEE,
2012.
13. S. Angizi, Z. He, A. Chen, and D. Fan, “Hybrid spin-cmos polymorphic logic gate with
application in in-memory computing,” IEEE Transactions on Magnetics, vol. 56, no. 2,
pp. 1–15, 2020.
14. S. Patnaik, N. Rangarajan, J. Knechtel, O. Sinanoglu, and S. Rakheja, “Advancing hardware security using polymorphic and stochastic spin-hall effect devices,” in 2018 Design, Automation & Test in Europe Conference & Exhibition (DATE), pp. 97–102, IEEE,
2018.
15. N. Rangarajan, S. Patnaik, J. Knechtel, R. Karri, O. Sinanoglu, and S. Rakheja, “Opening the doors to dynamic camouflaging: Harnessing the power of polymorphic devices,”
IEEE Transactions on Emerging Topics in Computing, vol. 10, no. 1, pp. 137–156, 2020.
16. N. Saxena and R. Vemuri, “ISPLock: A hybrid internal state locking method using polymorphic gates,” in 2022 IEEE Computer Society Annual Symposium on VLSI (ISVLSI),
pp. 140–145, IEEE, 2022.

Synthesis of Polymorphic Circuits for Hardware Security **133**

17. F. Parveen, Z. He, S. Angizi, and D. Fan, “Hybrid polymorphic logic gate with 5terminal magnetic domain wall motion device,” in 2017 IEEE Computer Society Annual
Symposium on VLSI (ISVLSI), pp. 152–157, IEEE, 2017.
18. A. J. Edwards, N. Hassan, J. Arzate, A. N. Chin, D. Bhattacharya, M. M. Shihab,
P. Zhou, X. Hu, J. Atulasimha, Y. Makris, et al., “Physically secure logic locking with
nanomagnet logic,” IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 44, no. 1, pp. 105–118, 2024.
19. N. Hassan, A. J. Edwards, D. Bhattacharya, M. M. Shihab, V. Venkat, P. Zhou, X. Hu,
S. Kundu, A. P. Kuruvila, K. Basu, et al., “Secure logic locking with strain-protected
nanomagnet logic,” in 2021 58th ACM/IEEE Design Automation Conference (DAC),
pp. 127–132, IEEE, 2021.
20. [UCSB, “ExPRESS Benchmarks, https://web.ece.ucsb.edu/express/benchmark/.”](https://web.ece.ucsb.edu/express/benchmark)
21. C. Karfa, R. Chouksey, C. Pilato, S. Garg, and R. Karri, “Is register transfer level locking secure?,” in 2020 Design, Automation & Test in Europe Conference & Exhibition
(DATE), pp. 550–555, IEEE, 2020.
22. J. Nevoral and R. Rˇziˇcka, “Efficient implementation of bi-functional RTL componentscase study,” in 2018 New Generation of CAS (NGCAS), pp. 25–28, IEEE, 2018.
23. L. Sekanina, “Evolutionary design of gate-level polymorphic digital circuits,” in Workshops on Applications of Evolutionary Computation, pp. 185–194, Springer, 2005.
24. P. G. Paulin and J. P. Knight, “Force-directed scheduling for the behavioral synthesis of
asics,” IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 8, no. 6, pp. 661–679, 1989.
25. C. Pilato, F. Regazzoni, R. Karri, and S. Garg, “TAO: Techniques for algorithm-level
obfuscation during high-level synthesis,” in Proceedings of the 55th Annual Design Automation Conference, pp. 1–6, Association for Computing Machinery, 2018.
26. T. F. Wu, K. Ganesan, Y. A. Hu, H.-S. P. Wong, S. Wong, and S. Mitra, “TPAD: Hardware trojan prevention and detection for trusted integrated circuits,” IEEE Transactions
on Computer-Aided Design of Integrated Circuits and Systems, vol. 35, no. 4, pp. 521–
534, IEEE, 2015.
27. C. M. Fiduccia and R. M. Mattheyses, “A linear-time heuristic for improving network
partitions,” in Papers on Twenty-five years of electronic design automation, pp. 241–247,
Association for Computing Machinery, 1988.
28. Y. Xie, C. Bao, and A. Srivastava, “Security-aware design flow for 2.5D IC technology,”
in Proceedings of the 5th International Workshop on Trustworthy Embedded Devices,
pp. 31–38, Association for Computing Machinery, 2015.
29. J. Rajendran, O. Sinanoglu, and R. Karri, “Is split manufacturing secure?,” in 2013 Design, Automation & Test in Europe Conference & Exhibition (DATE), pp. 1259–1264,
IEEE, 2013.

# 7 Design Obfuscation and
### Performance-Locking Solutions for Mixed-Signal, Analog and RF ICs

Priyanshu Mishra, Andrew Marshall, and
Yiorgos Makris

Analog/RF integrated circuits (ICs) are particularly prone to reverse engineering
(RE) as they consist of a limited number of design topologies and possess low transistor counts in their design blocks. Despite their simple structure, however, they require
significant time and resources, due to their custom design nature and their sensitivity to minute parameter variation. In this chapter, we review the various design-level
and layout-level solutions which have been proposed toward protecting analog/RF
hardware intellectual property (IP) from RE and unauthorized use. A popular approach uses a key-based mechanism to unlock the biases of analog/RF ICs to obtain
specification-compliant performance. Combinational locking and parameter biasing
obfuscation utilize a digital key to configure an array of transistors in a current mirror
block or the physical dimensions of the transistors, respectively, to hide the biasing
conditions of the analog/RF IC. Similarly, tuning elements such as memristors or
analog floating gate transistors (AFGTs) can be used in trimmable analog/RF ICs to
lock the performances of the circuit. Along a different direction, modification of existing parameterized cells (P-cells) using either process variation or layout structures
to create polymorphic devices and camouflage them with process P-cells can also
improve security of analog/RF ICs through the use of fake contacts. Similarly, polymorphic devices can also be created by leveraging process variations effects such
as Well-Proximity Effect (WPE) or Length of Diffusion (LOD). Most existing approaches to locking analog/RF ICs suffer from a limited key space and are prone to
removal attacks due to the digital nature of the key. Therefore, implementation of
analog solutions which are embedded in the analog/RF IC will not only increase the
key space but will also improve resilience against removal attacks. Accordingly, this
chapter will conclude with guidelines for effective implementation of such purely
analog locking solutions.

[DOI: 10.1201/9781003510949-7](https://doi.org/10.1201/9781003510949-7) **134**

Design Obfuscation and Performance-Locking Solutions **135**

**7.1** **INTRODUCTION**

The globalization of the semiconductor supply chain along with the technological
developments in RE have led to growing concerns for hardware security and trust
in ICs in recent times. One of the growing challenges is IP/IC piracy [1, 2] which
involves RE and different types of counterfeiting, such as cloning, overbuilding, remarking and recycling at the foundry level and at the end-user level. The IP/IC piracy
creates different challenges for different entities. The use of counterfeits in critical
infrastructure and in defense raises national security concerns for the government.
Similarly, it results in financial losses and loss of customers’ trust for the industry. It
also increases the risk of failure for the consumers, leading to safety issues in critical
products such as cars, healthcare products, etc.

Reverse engineering [3–5] refers to the procedure of obtaining the IP/IC proprietary information such as the design architecture, netlist and the layout of the designed chip. It is used in cloning [6] to market them as original by malicious system
on chip (SOC) integrator or foundry. Overbuilding refers to extra ICs that are fabricated by the malicious foundry in addition to the quantity measured in the contract
to be sold. Remarked ICs [6] are poor-quality ICs which have been approved by a
malicious test facility to be sold with forged documentation. Recycled ICs [6] refer
to the extraction of old ICs to be remarked and sold as new. Analog/RF ICs are more
prone to RE than their digital counterparts [3] due to their limited design topologies and lower transistor counts in the design blocks [7, 8]. Despite their simplicity,
analog and RF circuits require significant resources and time [9] due to their custom design nature and their sensitivity to minute parametric variations. Despite the
scale of the problem, most of the existing protection schemes are targeted at digital
ICs [10–12,14–18]. These schemes aim to lock the functionality of digital ICs which
can be de-embedded with a correct key. Unlike digital ICs, locking of functionality is
not an effective measure for analog/RF ICs as it leads to a low impact on degradation
of system performance.

This chapter discusses possible security approaches, as shown in Figure 7.1, to
ensure security for analog/RF and mixed-signal chips via transistor-level and layoutlevel techniques. Due to their sensitive nature, analog/RF designers devote a considerable effort on optimizing the design parameters to control the design performance.
The optimization of design parameters for in-spec performance stemmed from a popular approach of performance locking as a security primitive for analog/RF chips. At
the transistor level, it discusses approaches like using a digital key to lock the parameter performance [13] or the current mirrors [19] of the analog and mixed-signal circuits. Similarly, it discusses another popular approach which involves locking of the
calibration tools such as memristors [20], analog floating gate transistors [22], etc.,
to control the performance of the analog and mixed-signal circuits. It also discusses
the approaches at the layout level, such as security primitives utilizing layout effects

[38], or utilizing multi-threshold voltage [22] transistors in layouts to lock analog ICs
or utilization of fake contacts to camouflage analog and mixed-signal layouts using a
P-cell library consisting of obfuscated and normal P-cells [23]. Another popular area
of mixed-signal security research is the locking of the digital section, via traditional
logic locking techniques to control system performance [24–26]. This chapter also

**136** Advances in Hardware Design for Security and Trust

**Figure 7.1** Approaches to analog/RF and mixed signal IC security.

compares the effectiveness of the various discussed approaches as well as their ease
of implementation in terms of time and cost to provide a better understanding of the
available security solutions and allow the selection of the best solutions for particular
applications.

**7.2** **DIGITAL** **KEY-BASED** **LOCKING** **MECHANISM** **FOR** **ANALOG,** **RF**
**AND AMS CIRCUITS**

One of the popular approaches to secure analog/RF and mixed-signal ICs is to use
digital keys to control the current mirror or the bias voltages of the circuit to affect the
small-signal parameters of the analog and the mixed-signal circuits. The following
section discusses these approaches and concludes with a discussion of the approach
in which the digital key intertwines locking between the digital and analog circuits
in a mixed-signal circuit.

**7.2.1** **PERFORMANCE LOCKING VIA CONFIGURABLE CURRENT MIRROR**

Current mirrors are basic analog circuit blocks which are used to provide correct
current biases to obtain desired circuit performance. They are used in analog circuits

Design Obfuscation and Performance-Locking Solutions **137**

**Figure** **7.2** System-level diagram of configurable current mirror. (Adapted from

[19].)

to provide biasing currents, which determines the circuit performance. The approach
aims to make these current mirrors configurable through the use of a digital key [19].
The digital key configures the current mirror with a specific configuration to ensure
optimal performance. The digital key is a combination of the chip identification,
which is generally stored as a PUF [27], and an individualized chip key to create
a common key which unlocks the specific chip. Figure 7.2 illustrates the systemlevel diagram of the configurable current mirror (CCM) approach. The CCM locking
approach offers protection against RE and recycle-based counterfeiting.

The CCM approach has a large area overhead in terms of the area of the CCM,
exclusive OR (XOR) circuit, chip identification circuit and additional I/Os. Despite
its large area overhead, it allows the locking technique to be effectively used in large
analog and mixed-signal designs. The transistors in the current mirror block are in
saturation mode and hence the current through each branch can be approximated as:

ID1 = IREF = <sup>K0W</sup> <sup>(VGS −</sup> <sup>VTH</sup> <sup>)2</sup>

2L

Similarly, the ratio of the current between two branches can be written as:

ID2 =

12 <sup>K1(β W</sup> L <sup>)</sup>

12 <sup>K0(</sup> <sup>W</sup> L <sup>)</sup> <sup>ID1 = βID1</sup>

where beta(β) would be size ratio between two MOSFETs (M2 and M1).

The transconductance (gm) of the MOSFET transistor depends on the drain current (ID) which in turn determines the amplifier’s performance parameters, such as
DC gain, gain-bandwidth product (GBW) and thermal noise current density. As amplifiers are the building blocks of complex analog designs such as filters, oscillators,
voltage converters, ADCs, low-dropout (LDO) regulators, etc., the transconductance

**138** Advances in Hardware Design for Security and Trust

**Figure** **7.3** Schematic of configurable current mirror architecture. (Adapted from

[28].)

determines system-level performance parameters such as filter transfer function, oscillator’s output frequency, LDO’s stability, etc. The criticality of the bias current
to affect the performance of the analog system makes it a good locking choice for
secure analog chips. The locking architecture for the current mirror consists of an
array of MxN control transistors having K key lines [19]. Figure 7.3 illustrates the
schematic of CCM architecture. The bias current is given by:

M
###### ∏

i=1

φ(xij).IREF

IOUT =

N
###### ∑

j=1

β j

Here, xij is the control signal at transistor of row i and column j [19].

The locking approach needs to ensure in-spec performance for a single key and
significant performance deviation for all of the possible keys. To ensure that both
criteria are met for a specific CCM architecture with specific M, N and K, a satisfiability modulo theory (SMT) solver can be used to solve for the branch size vector
and the control matrix X(MxN) for a unique key K* [19]. The current mirror should
consist of NMOS and PMOS current branches to ensure that the input-output correlation is not monotonic in nature [28]. It offers better resilience against RE attacks.
Despite the undoubted advantages of this approach, it suffers from the limitation of
being applicable to circuits having current mirrors in their original design. Moreover,
the locking of the current mirror makes the circuit susceptible to removal attacks by
the attacker. The next section discusses a more generic bias locking technique to
control the performance of analog circuits which can be implemented in all types of
analog/RF circuits.

Design Obfuscation and Performance-Locking Solutions **139**

**Figure 7.4** Circuit schematic of vector-based obfuscation. (Adapted from [18].)

**7.2.2** **ANALOG AND RF PERFORMANCE LOCKING VIA BIAS LOCKING**

The so-called parameter obfuscation technique is based on the obfuscation of the
biasing transistors to control the performance of the analog circuits [29, 30]. As
analog and RF circuits depend on the biasing transistors for performance, the selection of the transistors together with accounting for the process, voltage and temperature variations are critical in implementing the parameter obfuscation technique.
It can be implemented in two configuration: vector-based and mesh-based parameter obfuscation. Vector-based parameter obfuscation replaces the selected transistors
with a set of parallel transistors whose gates are controlled by a single digital keybit [29]. Figure 7.4 shows vector-based parameter obfuscation. The current flowing through the source node of the parallel transistors is the sum of the individual
current flowing through each parallel transistor [18]. It can be summed, as, where
Ii is the drain current in the i <sup>th</sup> branch and the Si is the digital key-bit for the i <sup>th</sup>

branch [18].

Ivector =

n
###### ∑

i=1

IiSi

Replacement of a single transistor with a set of parallel transistors is done to hide
the target width of the biasing transistors. The drain current equation can be used to
model the variance of the widths, assuming the ideality in the mobility and threshold
voltage. The cumulative effective width can be calculated as: [18]

Tvector =

n
###### ∑

i=1

TiSi

where Ti is the width of the i <sup>th</sup> branch and the Si is the digital key bit for the i <sup>th</sup>

branch.

The replacement of the selected transistor with a mesh structure which consists
of series and parallel transistors is called mesh-based parameter obfuscation [31].

**140** Advances in Hardware Design for Security and Trust

**Figure 7.5** Circuit schematic of mesh-based obfuscation. (Adapted from [18].)

Figure 7.5 shows the mesh-based parameter obfuscation. While the addition of
transistors in parallel increases the width, the addition of transistors in series increases the length. Hence, the mesh-based parameter obfuscation allows us to control
the width and the length of the composite transistor in comparison to the width of the
composite transistor in vector-based parameter obfuscation [18]. Due to the ability
to mask the complete structure, mesh-based parameter obfuscation allows the designer to mask the threshold voltage and small-signal parameter in addition to device
dimensions. The W/L ratio of the selected transistor can be calculated as: [18]

1
Tmesh

=

r
###### ∑

i=1

1
∑ <sup>n</sup> j=1 <sup>TijSij</sup>

However, this technique suffers from a major limitation: the number of rows in
the mesh structure is limited due to stacking of the threshold voltage due to the
constituents [18]. It can be calculated as:

VGS − rVth ≥ 0

Here, r denotes the number of rows [18]. Despite the topology for implementation of
the parameter obfuscation, the determination of the target transistors, the elimination
of multiple correct keys as well as the possibility of incorrect keys giving desirable
circuit performance are the major challenges with this approach. The selection of
the target transistors is done through the selection algorithm, while the satisfiability modulo theory (SMT) algorithm is utilized to determine the sizes of the target
transistors as well as the obfuscation transistors [18].

Design Obfuscation and Performance-Locking Solutions **141**

Algorithm 1: Pseudocode for Target Transistor Selection [Adapted from

[18]]

Input: Tsel, ST, k,WR
Output: Torder
1 for j = 1 to Tsel do

2 S( j) = ParaSweep(Tsel( j),WR);

3 Shigh = ST + ST × k;

4 Slow = ST − ST × k;

5 WjEZ = Tj sizes producing per formance in range(Shigh, Slow);

6 Wjobfus = WR − WjEZ ;

7 Response = VertCat(Tsel( j),Wjobfus );

8 Rorder = DecreasingOrder(Response,Wob fus);

9 Torder = Rorder(Column1);

10 return Torder

The selection algorithm is based on the selection of target performance parameters and running sweeps on the transistor widths to obtain the range of the transistor widths (WEZ) which performs within the specifications of the target performance parameters [18]. The in-spec range (WEZ) is subtracted from the total range
(Wpermissible) to obtain the obfuscated range of transistor width (Wob fus). The selection algorithm determines the Wob fus for all the transistors and sorts them in descending order to select the transistors with the largest Wob fus based on the key size [18].
The algorithm can account for other design factors, such as signal integrity, etc., to
improve the selection of the obfuscation transistors.

Similarly, the SMT-based algorithm is used to determine the size of the target
and the obfuscation transistors which allows the production of a single unique key
and a large performance degradation for other keys [18]. Depending on the key size,
obfuscation topology and transistor sizes, the algorithm determines the unique key
for unlocking circuit performance. It allows to account for the parasitic and PVT
variations, thereby limiting information about the transistor sizing to the attacker

[18].

Large analog circuits generally require peripheral biasing and calibration circuits
which are accessible only during testing. The approach can be applied to these calibration circuits allowing us to better minimize PVT and mismatch variations in the
analog circuits [18]. Determination of the bias along with the unique key increases
the complexity of the circuit for attacking and thereby improving the resilience of
the circuit.

The method offers protection against RE attacks and analog IP theft. It offers
widespread protection in comparison to the CCM approach as current mirrors are
not present in all analog circuits. Although the approach offers better resilience with
increased key size, it increases the overall area of the circuit and also makes it susceptible to SMT and removal attacks.

**142** Advances in Hardware Design for Security and Trust

**Figure** **7.6** AMS circuit with shared locking between the analog and digital block.
(Adapted from [32].)

**7.2.3** **LOCKING OF AMS CIRCUITS VIA SHARED KEY**

Most of the existing locking approaches for AMS circuits lock the digital portions
of the circuit or use separate locking mechanisms for the analog and digital blocks
of the AMS circuits. A separate locking mechanism for both parts of the circuit
makes the mixed-signal circuit susceptible to partial decomposition attacks [32]. The
addition of correlated key dependencies within the circuit increases the adversarial
key search space, leading to better security. The increased key space offers better
protection against SAT attacks as well as partial key attacks [32].

The approach was demonstrated through a peak detector and counting circuit
which consisted of an analog front end, a 7-bit Flash ADC and a digital counter circuit [32]. Figure 7.6 shows the AMS circuit with locking interdependencies between
the analog and the digital block. The black lines show the interconnects between the
analog obfuscation and digital obfuscation keys. The interdependencies were created
using XOR gate connections between random key-bits of the analog and the digital
key. The analog and the digital sections were locked using parameter obfuscation and
a combination of XOR-based logic locking and stripped-functionality logic locking
(SFLL)-HD0, respectively. For the digital locking, the XOR-based logic locking was
used in the digital counter block and SFLL was applied to the logic cone of the peak
detector circuit, respectively [32]. Similarly, the resistive divider Flash ADC was
locked with parameter obfuscation [32]. As discussed, the parameter obfuscation
technique uses transistor sizing to control the biasing performance which affects the
vital analog performance of the circuit. While the analog key for locking the Flash
ADC consisted of 10 bits, the digital key consisted of 6 bits and hence the complete
peak detector and counter circuit was locked with a 16-bit key space [32].

The correlation between the digital and analog locking creates a dependency on
the key and input for obtaining output instead of a simple input-output relation. This

Design Obfuscation and Performance-Locking Solutions **143**

dependency of the keys and the input to the output improves the resilience against saturating 0 and 1 input attacks which allows the attacker to isolate the digital keys from
analog keys [32]. The shared dependency also creates three times more distinguishing input patterns (DIP) patterns, which leads to increased key space. In addition to
this, the inaccessibility of scan chain and internal testing points to adversaries offers
better protection of the digital portions in AMS circuits [32]. In conclusion, locking
techniques aiming for system-level locking of analog and mixed-signal systems offer
better security than individual locking of components of such blocks.

**7.3** **CALIBRATION LOCKING FOR ANALOG/RF AND AMS CIRCUITS**

Analog/RF circuits are more sensitive to process variations and device-level effects
than digital circuits and hence require calibration to ensure matched performance
with the datasheet specifications. In this section, we are going to discuss the calibration locking of these circuits using memristors, analog floating gate transistors
(AFGT) and analog neural networks as well as the locking of programmable analog
ICs.

**7.3.1** **BIAS LOCKING THROUGH MEMRISTORS**

An early approach to calibration locking was to build a circuit security primitive
which provided protection against unauthorized access through the utilization of
memristors and the adaptive body bias (ABB) property of transistors [20]. This was
demonstrated through the differential sense amplifier which is typically used in static
random-access memory (SRAM) amplifiers. Memresistance depends on the integral
of the current and the voltage of the device through the device. It relates the charge
q and flux φ via the following equation: [20]

M(q) = <sup>dφ(q)</sup>

dq

Memristors can be fabricated as metal-insulator-metal (MIM) with an insulating
layer consisting of materials like chalcogenides, metal oxides, perovskites and organic films [20]. Memristors have two resistance states, a high resistance state (HRS)
and a low resistance state (LRS) [20]. The transition from the HRS to the LRS and
vice versa are called the SET and the RESET operations, respectively. To perform
the SET operation, memristors require a voltage bias with fixed polarity and magnitude called VSET . Similarly, the RESET operation is performed using the voltage
bias of VRESET [20]. The memristance of the memristor depends on the device size
and the dopant concentration and therefore is prone to process variation–induced
changes.

One of the approaches to counter the parametric variations is via ABB. ABB
utilizes a bias voltage (Vbs) between the source and the substrate terminal of the
MOSFET to tune the threshold voltage and thereby reduce the effect of parametric

**144** Advances in Hardware Design for Security and Trust

**Figure 7.7** Amplifier schematic with memristor-controlled input pair threshold bias
voltage. (Adapted from [20].)

**Figure 7.8** Memristor crossbar programming circuit. (Adapted from [20].)

variations on the threshold voltage [20]. Applying a positive bias or forward body
bias (FBB) can reduce the threshold voltage but increases the leakage current [20].

(|2φf |− Vbs −

|2φf |)

Vth = Vth0 + γ(

The approach demonstrated the locking of the SRAM sense amplifier through utilization of the memristor programming and ABB. The sense amplifier detects a small
differential voltage in the complementary bit lines of the SRAM array and amplifies it
to perform the SRAM read-out operation [20]. Figure 7.7 shows the amplifier whose
input pair threshold bias voltage is controlled via a memristor programming circuit.
Such an approach can be used to provide protection against the evil-maid attack

Design Obfuscation and Performance-Locking Solutions **145**

**Figure 7.9** Block diagram of waypoints approach. (Adapted from [21].)

where the attacker tries to retrieve and write to the memory [20]. The programming
circuit consists of control logic and memristor array circuitry which properly sets the
bias voltage to allow the differential amplifier to function as per the specifications.
Figure 7.8 illustrates the memristor crossbar-based programming circuit.

The upper and lower crossbar array consists of 1T1M crossbar architecture where
each memristor is selected by FET [20]. The upper and lower array consists of PMOS
and NMOS devices, respectively. The amplifier provides a gain to the Vout from the
memristor crossbar to Vprog, which sets the proper bias through the bias voltage generator circuit to reduce the threshold voltage offset. Memristors have low parasitic
capacitance and allow precise tuning of resistance values which allows for precise accounting for the threshold voltage mismatch and thereby does not degrade the circuit
performance with additional circuitry [20]. However, such a method suffers from
fabrication challenges as memristors are generally incompatible with the standard
CMOS process.

**7.3.2** **BIAS LOCKING THROUGH ANALOG FLOATING GATE TRANSISTORS**

Programmability of AFGTs allows them to be used in the calibration of analog
ICs. An approach termed waypoint security locks the calibration of analog circuits
using AFGTs [21]. It is an analog locking mechanism which facilitates simultaneous
unlocking and calibration of analog circuits using AFGTs [21]. It offers protection
against illegitimately acquired analog ICs by locking its calibration. The waypoints
mechanism limits the initial programming range of the AFGTs using the AFGT Inhibit circuit which keeps the performance of the analog IC away from the desired
results [21]. To unlock the complete programming range, the waypoints require an
analog key which comprises of a particular sequence of specific values in the AFGTs.
Figure 7.9 illustrates the block diagram of the proposed method. The waypoint mechanism consists of a range controller, key checker and analog circuit [21].

The key checker controls the Inhibit signal, which upon correct sequential programming of the AFGT, allows full-range AFGT programming through the range
controller [21]. Figure 7.10 shows the unlocking and calibration of the operational
transconductance amplifier (OTA) via waypoints using two AFGTs.

**146** Advances in Hardware Design for Security and Trust

**Figure** **7.10** Simultaneous unlocking and calibration of OTA via waypoints using
two AFGTs. (Adapted from [21].)

**Figure** **7.11** Schematic of analog floating gate transistors(AFGT) along with its
charging via Fowler Nordheim tunneling. (Adapted from [21].)

The AFGT consists of a standard MOS transistor whose gate node is a floating gate node formed using a control gate capacitor (Ccg) and a tunneling capacitor
(Ctun). As the gate node is surrounded by an electrically insulating layer, the charge
trapped at the floating gate is permanently stored. The floating gate transistors can be
programmed through Fowler Nordheim (FN) tunneling via applying voltage pulse at
the Tun terminal of the Ctun capacitor [21]. Figure 7.11 shows the schematic of the
AFGT and its charging through FN tunneling.

The programming range of the AFGTs is controlled by the AFGT Inhibit circuit
which consists of a zener diode, a resistor and a NMOS switch. When the Inhibit
signal is low, the NMOS switch is off and hence the amplitude of the pulses at the
Tun terminal would be equal to the amplitude of pulses at the program terminal [21].

Design Obfuscation and Performance-Locking Solutions **147**

**Figure 7.12** Working principle of Inhibit signal. (Adapted from [21].)

Figure 7.12 shows the AFGT Inhibit circuit which controls the Inhibit signal. Similarly, when the Inhibit signal is high, the zener diode limits the amplitude of the
pulses. As the key checker controls the Inhibit signal, it is initially set to high to
limit AFGT programming. The key checker circuit consists of a window comparator, a finite state machine (FSM) and two multiplexers, which are controlled by the
FSM. The FSM compares the monitored voltage with the internally generated voltage via the window comparator and upon matching, moves to the next value of voltage matching for the next waypoint [21]. Upon considering all the waypoints, if the
AFGTs match the individual waypoints, the FSM generates a low Inhibit signal allowing programming of the AFGT in their entire range. If a certain waypoint is not
matched, the matching process would still continue but the FSM would not generate
a low Inhibit signal at the end of the process. The IC would need to be power-cycled
for another attempt at calibration [21].

AFGTs are used in analog and mixed-signal circuits to counteract process variations and improve mismatch errors. The proposed approach utilizing AFGTs to
simultaneously unlock and calibrate the ICs offers protection against IC theft at the
foundry as well as the user level. However, like other calibration-locking techniques,
it is susceptible to removal attacks.

**7.3.3** **PERFORMANCE LOCKING VIA NEURAL NETWORK–BASED BIASING**

Another calibration-locking technique involves locking the performance of analog
ICs using an analog neural network. The trained neural network provides the desired
biasing voltage to the ICs for it to operate within specifications [33]. The programming of the analog neural network is done through the AFGTs, which offers permanent storage for the synapse weights and also allows for a large key size [33]. Figure
7.13 shows the general architecture for neural network-based biasing.
It also enables individualized keys per chip thereby offering better resilience
against key-sharing attacks [33]. The approach offers protection against unauthorized users aiming to obtain the in-spec performance from an illegitimately obtained

**148** Advances in Hardware Design for Security and Trust

**Figure** **7.13** General architecture of neural network-based biasing. (Adapted from

[33].)

IC [33]. The analog nature of the key offers a large key size which provides protection against brute force and model approximation attacks.

The on-chip analog neural network consisting of floating gate transistors is provided to the end user along with the analog key to unlock the circuit performance

[33]. The utilization of floating gate transistors allows the solution to be in the analog domain. Large key size, combined with the time-consuming process of evaluating individual keys, offers protection against brute force attacks. Similarly, the
deviation of results from the incorrect keys and the lack of correlation among them
offers protection against model approximation attacks. The designed neural network
was a two-layer multilayer perceptron (MLP) neural network [33]. MLP neural networks are feed-forward neural networks wherein each neuron receives connection
only from inputs or previous layers. The first layer known as the hidden layer receives the analog key values as the input. The second layer, called the output layer,
receives the output from the first layer and bias values to generate the output bias values for the main circuit. Each connection’s contribution to the output depends on the
synaptic product of the local weight value and the corresponding neuron input. The
training of the MLP neural network can be performed via the chip-in-the-loop training strategy and the hardware-customized version of the resilient back propagation
algorithm [33]. The approach was applied to determine the biases of the low noise
amplifier (LNA) to obtain in-spec performance of the S11, S12, S21, S22 and the
operating frequency of the LNA. Figure 7.14 illustrates the LNA circuit schematic,
along with its characteristic specifications. The LNA is a cascode LNA with an inductive source degeneration type which consists of three biases.

Table 7.1 illustrates the three bias sets (P1, P2 and P3) obtained using the twoinput hardware analog neural network and shows its performance on the cascode
LNA. From Table 7.1, it can be understood that the neural network generates correct
bias values for P3 to allow in-spec performance of the LNA. Points like Point 2 arise
from the non-idealities in training and hence should be treated as successful keys to
offer better protection against model approximation attacks [33]. As neural networks

Design Obfuscation and Performance-Locking Solutions **149**

**Figure** **7.14** LNA circuit schematic along with its specifications. (Adapted from

[33]).

**Table 7.1**
**Performance** **of** **the** **Obtained** **Bias** **Sets** **for** **the** **Cascode** **LNA** **Using** **2-Input**
**Hardware Analog Neural Network.**

Points Status Biases (V) Performance

P1 Locked 0.8, 0.8, 0.8

P2 In-between 1.05, 1.5, 1.35

P3 Unlocked 1.35, 2.55, 2.25

Adapted from [33].

S11: –6.5 dB
S12: –34.9 dB
S21: 0.3 dB
S22: –4.8 dB

S11: –6.9 dB
S12: –33.9 dBS
S21: 8.1 dB
S22: –5.6 dB

S11: –8 dB
S12: –31.4 dB
S21: 11.2 dB
S22: –7.5 dB

are programmed after the fabrication of the neural chip, it allows the key to be individualized per circuit and offers better security in comparison to a common key [33].
Due to the measurement complexity and large experiment runtime of analog circuits,
a small number of key inputs for the neural network–based biasing approach would
offer quality protection against brute force and other attacks [33].

**150** Advances in Hardware Design for Security and Trust

**Figure 7.15** Block diagram for locking of programmable analog IC. (Adapted from

[6].)

**7.3.4** **PERFORMANCE LOCKING FOR PROGRAMMABLE ANALOG ICS**

In this technique, analog and mixed-signal ICs are made programmable to ensure
compensation for process variations and other non-idealities and for reconfiguration
of ICs for application specific demands [34–36]. In addition to this, programmable
ICs improve fault tolerance and provide better performance. Programmability of ICs
is performed via tuning knobs which determine the circuit performance. The tuning
knobs are programmable bias sources which fix either the voltage or the current in a
node. Although these tuning knobs should have orthogonality in circuit performance,
in reality, a tuning knob has an impact on multiple circuit performance which creates
an entangled programming nature. The programming of the chip is performed using
a calibration algorithm which uses the performance indicators to traverse the space of
tuning knob settings to obtain the target circuit performance. It can be implemented
on-chip or off-chip using an automated test equipment (ATE). Although on-chip implementation provides faster calibration and better calibration, it increases the design
complexity as well as the area overhead.

The entangled programming nature of the method can be harnessed to create a
security primitive for analog and mixed-signal ICs to provide protection against RE
by the foundry and the end user [6,37]. While the calibration algorithm would be the
designer’s secret, the configuration settings from the calibration algorithm would act
as keys to the locked programmable analog and mixed-signal chips [6]. Figure 7.15
illustrates the block diagram for locking of the programmable analog ICs. In addition
to the circuit netlist, the attacker needs to determine the calibration algorithm to
derive in-spec performance from the chip. The proposed locking approach can also
provide protection against overbuilding by a malicious foundry and remarking by
the malicious test facility as the chip activation is performed by the design house [6].

Design Obfuscation and Performance-Locking Solutions **151**

**Figure 7.16** TPM-based key scheme. (Adapted from [6].)

**Figure 7.17** PUF-based key scheme. (Adapted from [6].)

Due to the calibration algorithm’s off-chip nature, the locked IC does not require a
significant redesign in terms of additional circuitry. The additional area and power
overheads arise from the implementation of the key management block. It can be
implemented via storing the lookup table (LUT) of the configuration setting into
a tamper-proof memory (TPM) or via the physical unclonable function (PUF) [6].
Figure 7.16 and 7.17 illustrate the TPM-based key scheme and the PUF-based key
scheme, respectively.

The PUF-based scheme selects a corresponding challenge from the selection of
the challenges in the TPM and generates a secret identification key. The secret identification key is XORed with the user key to generate the target configuration settings [6]. In order to ensure the secrecy of the calibration algorithm along with
the configuration settings as well as to ensure resilience against remarking, the offchip calibration should be performed in a trusted environment. The untrusted-test

**152** Advances in Hardware Design for Security and Trust

facility could perform structural defect-oriented tests which do not involve calibration and would return the chips to the design house or the trusted test facility for
further testing [6]. In case the testing needs to be performed in the untrusted test
facility, the calibration can be performed using secured remote calibration via asymmetric cryptography [10]. The proposed approach offers resilience against removal
attacks and bias-locking attacks due to its lock-less nature and the de-obfuscation
of the main circuit. Combining the large key space along with simulation time for
each iteration makes the proposed locking technique effective against brute force and
multi-objective optimization attacks. Due to the inability of the behavioral model to
model the transistor-level effects for the analog and mixed-signal circuits, transistorlevel simulations are used to test circuit performance [6]. Transistor-level simulations
are complex and time consuming as compared to register transfer-level simulations.
Hence, a small key for analog and mixed-signal circuits creates a large key space in
comparison to digital counterparts [6]. Most of the analog and mixed-signal chips
have internal feedback loops between the sub-blocks which disallow the attacker to
divide the main circuit into sub-blocks to perform the hierarchical decomposition
attack to determine the key. Due to the interdie variations, the configuration settings
from the calibration algorithm would be different for each individual circuit, which
would require additional effort for the attacker to optimize the common key for each
case [6].

**7.4** **PROTECTION** **OF** **ANALOG/RF** **AND** **MIXED-SIGNAL** **CIRCUITS**
**VIA LAYOUT CAMOUFLAGING**

Recently, an active research area to protect analog/RF IP is to camouflage IC layouts
using different layout techniques. At the layout level, one of the first approaches to
ensure the security of analog circuits was to utilize the threshold voltage variations
in the PMOS and the NMOS cells, respectively.

**7.4.1** **ANALOG/RF IP PROTECTION VIA MULTI-THRESHOLD LAYOUT**
**CAMOUFLAGING**

Analog circuit performance depends on the correct voltage and current biasing and
operating regions. The correct voltage and the current bias can be obtained using
normal Vth transistors with nominal sizing or using a combination of high Vth (HVT)
and low Vth (LVT) transistors [22]. The use of multi-threshold voltage transistors
allows us to create a secure analog design offering protection against RE attacks [22].

Multi-threshold voltage transistors are used in analog design to balance leakage
and performance. LVT transistors are generally used in low-power circuits to improve circuit performance as well as to answer the headroom challenges [22]. HVT
transistors are used generally used to reduce the leakage at the cost of depreciating
circuit performance [22].

The following diagram 7.18 illustrates the flowchart of designing analog circuits
with high/low VT transistors. One of the critical aspects to ensure more secure analog

Design Obfuscation and Performance-Locking Solutions **153**

**Figure** **7.18** Flowchart for the secure design flow using multi-threshold transistors.
(Adapted from [22].)

**Figure** **7.19** 3 possible configurations of multi-threshold voltage transistors.
(Adapted from [28].)

designs is to use novel topologies with uncommon sizing and use of high/low VT
transistors in a symmetrical manner to increase the RE efforts. Figure 7.19 shows the
three possible configurations of multi-threshold voltage transistors.

The IP protection technique provides protection against brute force attacks due
to the large size of combinations (3N combinations) for a circuit with N number
of transistors [22]. A large number of layout combinations along with long simulation times for each individual analog circuit combination increases the brute force
time rendering it ineffective. It offers protection from RE attacks using tools such
as optical imaging and X-ray imaging equipment [22]. The value of the Vt can be
determined using dopant profiling tools such as spreading resistance profiling, secondary ion mass spectrometry and scanning capacitance microscopy. However, the
cost of using tools exponentially increases the RE costs thereby making the RE attacks on such circuits a costly proposition [22]. One of the major drawbacks of this
approach was its applicability to large circuits as the key space of 3N combinations
offers effective protection against SAT/SMT attacks when N is large.

**154** Advances in Hardware Design for Security and Trust

**Figure** **7.20** Baseline (BL), side-poly (SP) and short-oxide diffusion (SOD) layout
configurations. Here, A and B denotes the distance between the gate and the OD and
D denotes the distance between the gate and well edge. (Adapted from [38].)

**7.4.2** **LOCKING OF ANALOG/RF ICs UTILIZING LAYOUT-BASED EFFECTS**

Another popular technique to camouflage ICs is to utilize the layout-based effects
to lock the performance of analog circuits [38]. The layout-based concept utilizes a
key-based approach which provides protection against counterfeiting and RE attacks.
For example, the layout approach uses the effects of length of oxide diffusion (LOD)
and well proximity effect (WPE) on transistors for tuning device parameters such
as transconductance (gm) and threshold voltage (Vth) [38]. The utilization of these
effects is incorporated into regular transistors without modifying the IC fabrication
process or the structure of manufacturing. WPE refers to the variance of device performance based on the device’s proximity to the well edge [38]. A transistor close to
the well edge presents a different performance to a device located far from the well
edge due to ion implant scattering of the resist side well [38]. Similarly, LOD refers
to the mechanical stress induced by different oxide diffusion length options. Based
on these two differentiating factors, the three arrangements for the transistor can be
classified as baseline (BL), side-poly (SP) and short-OD (SOD) to illustrate the layout effects on gm and Vt [38]. Figure 7.20 illustrates the three possible arrangements
of the transistor called the BL, SP and SOD structure. The layout effects can create variations of up to ∼10% in threshold voltage and transconductance [38]. It was
observed while NMOS had profound voltage threshold variations, PMOS had significant transconductance variations [38]. Table 7.2 illustrates the variations of voltage
threshold and transconductance with respect to the BL.

The key-based locking leveraging layout-effects has a keyspace of 2*3 <sup>N</sup> keys
for N devices, assuming binary signals for keys [38]. The technique was demonstrated using an operational transconductance amplifier (OTA) which had 36

Design Obfuscation and Performance-Locking Solutions **155**

**Table 7.2**
**Variations on Threshold Voltage** vt **and Transconductance** gm **Based on Layout**
**Effects.**

Parameter Ai Device Variation

Vth

gm

SP

SOD

SP

SOD

HVT: 2.85%
PMOS SVT: 3.7%
LVT: 4.59%
HVT: 4.05%
NMOS SVT: 4.38%

LVT: 5%

HVT: 6.08%
PMOS SVT: 7.9%
LVT: 9.79%
HVT: 8.53%
NMOS SVT: 9.28%
LVT: 10.61%

HVT: 4.76%
PMOS SVT: 4.72%
LVT: 4.68%
HVT: 1.72%
NMOS SVT: 2.54%
LVT: 2.42%

HVT: 10.4%
PMOS SVT: 10.19%
LVT: 10.16%

HVT: 3.7%
NMOS SVT: 5.41%
LVT: 5.09%
(Adapted from [38]).

transistors [38]. It has an input differential pair, summing circuit and floating classAB control, bias circuit and class-AB output circuit. Of the 36 transistors, 13 critical
transistors were selected to obfuscate, thereby creating a key space of 2*(3 <sup>N</sup> ) [38].
The 13 critical transistors were selected based on the analysis of depreciation caused
by a single transistor on the system performance between the obfuscated and the
unlocked OTA.

The layout-based effect provides protection against an untrusted end user and
untrusted foundry. The untrusted end user can use optical imagers as well as circuit
simulators to RE the chip; however, it will not be able to identify the layout effects as
most of the RE tools do not possess layout dependent effects (LDE)-level visibility

[38]. Thus, the adversary will see similar transistors with identical sizes. Even if the
adversary possesses an unlocked chip (oracle), they will have difficulty in obtaining

**156** Advances in Hardware Design for Security and Trust

distinguishing input patterns which would offer protection against SAT attacks [38].
Although the untrusted foundry has more information about the circuit compared to
the end user, it would still have difficulty determining the keys due to the arbitrary
arrangement of transistors in the layout. The resource and time required to brute
force the key, it is argued by the authors, would make it an unfeasible approach for
key determination [38]. As mentioned above, the SAT solvers cannot account for
layout effects and hence circuit simulators along with SAT solvers would be needed
to determine the keys [38]. The added complexity of using circuit simulators in key
determination makes the process difficult. It also offers protection against removal
attacks as the camouflaging is done on multiple blocks instead of a single block such
as the bias block [38].

**7.4.3** **LOCKING OF ANALOG/RF ICs UTILIZING COMPONENT SIZING**
**CAMOUFLAGING**

Besides utilizing layout effects, another popular technique called analog IC camouflaging can be used to protect analog and RF circuits from RE attacks [23, 39].
It refers to hiding the correct size of the components to create a deceptive sizing
from an extracted netlist of reverse-engineered circuits and thereby offers protection against RE attacks by malicious end users. It is different from gate camouflaging where a large percentage of gates are camouflaged to make RE difficult [23].
Gate camouflaging tends to lead to large areas, delays and power overheads [40].
The proposed camouflaging has a lower area and delay overhead as well as increased complexity for attackers due to its potential to obfuscate all the available
components [23].

It aims to hide the active geometry of the layout components using fake contacts. In custom analog circuits, some of the conventional techniques to improve
component matching and reduce process variations are the use of gate fingers for
large transistors, serpentine serial connections for resistors and capacitor banks for
capacitors. The fake contacts are used in these unit blocks of transistors, resistors
and capacitors to create seemingly connected but electrically disabled components
thereby camouflaging the active layout geometry of components [23].

A set of camouflaged P-cells of transistors, resistors and capacitors is created for
each technology node. Figure 7.21 shows an obfuscated layout for a transistor. The
camouflaged P-cells consist of standard P-cell components with electrically disabled
components [23]. The designer uses the camouflaged P-cells and sets the parameters
in terms of active sizing, number of extra inactive instances and its location. The
approach is versatile and can be implemented in existing designs as well as new
designs [23]. Figure 7.22 depicts the flow-chart for camouflaging an existing design
as well as a new design from the defender’s perspective. As we know that the addition
of the extra components would lead to an increase in parasitics which would hamper
the performance of the circuits, hence the defender needs to aim for the following
objectives [23]:

Design Obfuscation and Performance-Locking Solutions **157**

**Figure 7.21** Obfuscated layout for transistor. (Adapted from [28].)

**Figure 7.22** Flowchart involving steps for camouflaging an a) existing design and b)
new design. (Adapted from [23].)

1. Minimize the performance degradation due to induced parasitic from camouflaged components and from additional changes in floor planning and
routing in the layout.
2. Maximize performance deviation of all-true contact design with the obfuscated design to maximize protection against RE attacks.
3. Minimize the area overhead occurring to design obfuscation and the design
effort to ensure secure designs with lower cost and turnaround times.

**158** Advances in Hardware Design for Security and Trust

The approach offers protection against SAT attacks and brute force attacks due to
the large space size and its analog nature. The search space size is:

S =

M
###### ∏

i=1

Ni

Here, M and Ni denote the number of the components and the number of instances
of the ith component in the circuit, respectively [23].

It also offers protection against the hierarchical decomposition attack as subblocks would function correctly without any performance degradation. However, the
system suffers from performance degradation at the top level which makes all the
sub-blocks candidates for obfuscation [23]. The attacker cannot distinguish between
the obfuscated and normal blocks and hence cannot reduce the attack effort [23].

Recently, attackers have chosen to use CAD sizing tools to attack analog circuits
using automatic analog circuit sizing tools [41–45]. The tool is generally provided
with a given topology and a performance objective and returns a sized schematic. It
is used by the attacker to resize the extracted topology obtained from RE. However,
currently, such an attack is difficult to carry out on large analog circuits using layout
camouflaging approaches, as these CAD tools have difficulty in running multiple
simulations on large analog circuits [23]. It would require the creation of hierarchical
behavioral sub-models which would be difficult as the attacker would have to guess
the performanceof each sub-block to reach the system-level performance. In addition
to this, the derived netlist would be different from the netlist extracted from the RE
of the layout and hence would require a significant redesign in the layout in terms of
floor planning and routing [23].

The approach offers significant protection against physical attacks such as optical imaging, scanning electron microscopy (SEM), heat maps and EM side-channel
analysis as it is difficult to obtain gate-level component sizing from such approaches

[23]. Although the attacker can extract the component sizing for all the components
from the focused ion beam (FIB)-assisted probing, it would be expensive for large
analog circuits due to the destruction of the chips caused in the process [23].

**7.5** **DIGITAL-LOCKING MECHANISM OF AMS CIRCUITS**

In recent times, locking of the digital circuitry to lock the performance of the mixedsignal chips has gained popularity due to the growth of digital-centric mixed-signal
chips as well as the ease of implementation of digital-locking techniques.

**7.5.1** **LOCKING OF AMS CIRCUITS VIA AMSLOCK AND MixLock**

One of the first approaches utilizing the idea was the AMSlock technique [24]. It
was based on the logic locking of the optimizer which controls the tuning knobs
for the passive components in the analog and mixed-signal circuits to counteract the
process variations [24]. Upon applying the correct key, the optimizer tuned the tuning

Design Obfuscation and Performance-Locking Solutions **159**

**Figure 7.23** Locking of analog circuit via AMSlock. (Adapted from [24].)

knobs to the correct values to ensure desired performance of the analog circuit. The
optimization was performed using stripped-functionality logic locking (SFLL) [46]
technique. SFLL works on the principle of stripping a part of the original circuit
to replace it with a functionality stripped circuit (FSC). In SFLL, at a particular
hamming distance (HD), say h, away from the correct secret key, the output of the
circuit is flipped for all the input patterns. The input patterns for which the FSC’s
output is corrupted are called protected input patterns (PIPs). The restore unit only
nullifies the flipping of the output for the valid secret key to recover the correct
output. The number of key-bits, k, and the hamming distance, h, play an important
role in determining the security offered by the SFLL against various attacks [24].
AMSlock uses the SFLL-flex technique, allowing the defender to select the desired
number of input patterns to protect, thereby offering greater protection [24]. Figure
7.23 illustrates the AMS locking of an analog circuit.
One of major implementation challenges of this approach was to determine the
granularity of the tuning knobs to ensure performance compensations for the mismatch and process variations as well as lead to significant performance degradation
for the incorrect keys [24]. Overcoming these shortcoming was another popular digitally assisted performance locking techniques called MixLock [25, 26, 47]. Figure
7.24 illustrates the general architecture of MixLock. It can be implemented using
various locking techniques, such as the use of SFLL in MixLock 1.0 [26, 47] or
the dishonest oracle (DisORC) with truly random logic locking (TRLL) in MixLock
2.0 [25]. The DisORC with the TRLL in MixLock 2.0 ensures maximum digital security as well as enhanced degradation of analog parameters for incorrect keys [25].
It reduces the dependency of circuit performance on the input data and allows us to
determine the hamming distance from the valid secret key. The hamming distance
determines the upper bound of the number of user keys which, apart from the secret
key, allows in-spec circuit performance [25].

The MixLock approach enjoys certain advantages over other mixed-signal approaches which makes it a good candidate for mixed-signal IC protection. It locks

**160** Advances in Hardware Design for Security and Trust

**Figure 7.24** Block diagram of MixLock architecture. (Adapted from [25].)

the digital portion of the mixed-signal chips without modifying the analog sections
of the chip. Modification of analog cores requires significant rework due to its custom design and layout nature. In addition to this, the locking of digital portions can
be fully automated as logic locking can be performed after logic synthesis [25]. Most
of the area overhead and the power consumption in mixed-signal ICs are dominated
by the analog section. As it only involves locking of the digital section, the additional
area and power overhead in terms of a complete mixed-signal chip would be justifiable. Additionally, the logic locking algorithms can be programmed to insert locks in
the non-timing critical path to ensure that the timing violations are avoided and only
a non-critical delay penalty for the entire chip is added [25]. Due to its digital-locking
nature, it can have large keys offering a large key space which acts as a detriment to
logic attacks. Mixed-signal locking in general can be evaluated in terms of digital
security level and analog security level. While the digital security level involves the
amount of time and effort required by the locking attacker to obtain the secret key,
analog security level involves parameters such as the presence of a unique key in the
key space and a large percentage of keys in the key space, which leads to significant
performance degradation [25].

The MixLock 1.0 was based on logic locking of the digital section of the mixedsignal chip using the SFLL technique. Figure 7.25 illustrates the SFLL architecture
used in MixLock 1.0. The main drawback of MixLock 1.0 using the SFLL technique
was its ability to only provide protection against oracle-based attacks. In comparison to this, MixLock 2.0 provides a strong analog security level due to its ability

Design Obfuscation and Performance-Locking Solutions **161**

**Figure 7.25** SFLL architecture used in MixLock 1.0. (Adapted from [26].)

to drastically corrupt functionality for the incorrect keys as well as a strong digital security level due to its ability to stop most of the logic locking attacks. The
DisORC with TRLL [48] used in MixLock 2.0 creates two orthogonal solutions providing protection against oracle-based attacks as well as oracle-less attacks. While
the DisORC provides protection against scan chain oracle–based attacks, TRLL provides protection against oracle-less attacks such as machine learning–based structure
analysis attacks. The DisORC principle works on the withdrawal of the secret locking key upon scan detection to provide protection against scan-chain oracle-based
attacks while maintaining complete testability [25]. Figure 7.26 illustrates the DisORC defense architecture. The corrupt signal whose input is the scan-enable signal
determines the selection of the correct key and the incorrect key in the functional
mode and the test mode, respectively. The use of incorrect keys in test mode allows structural test and fault coverage while protecting the correct key. Similarly, the
TRLL works on the principle of inserting or replacing existing gates with key gates
at random locations in the netlist. The randomized nature of the key gates makes it
difficult for the attacker to determine the key values from these gates [25].

Although the DisORC component of MixLock can be easily identified for removal attacks, the TRLL gates are embedded into the design and offer protection
against such attacks [25]. Also, the complete removal and replacement of the digital
block is not feasible in mixed-signal ICs due to the intertwined nature of the digital
block with the analog block. It offers protection against brute force and optimization
attacks due to its large key space and long simulation runtimes for transistor-level
simulations for analog and mixed-signal circuits [25]. It also leads to high functionality corruption for the incorrect keys which leads to difficulty in convergence for
optimization algorithms [25]. It also provides protection against the SMT-based and
genetic algorithm (GA)-based bias locking attacks which are typically used for attacking analog and mixed-signal circuits.

**162** Advances in Hardware Design for Security and Trust

**Figure 7.26** DisORC architecture. (Adapted from [25].)

**7.6** **EXISTING ATTACK CLASSES ON ANALOG/RF AND**
**MIXED-SIGNAL ICs**

The following section presents a brief overview of the probable attack mechanisms
on the analog/RF which can be caused by an untrusted foundry or an end user. One
of the earliest attack approaches is the brute force method in which the attacker in
the form of the untrusted foundry or end user uses an unlocked chip and datasheet
specifications to determine the desired circuit performance and perform circuit simulations for all the keys to match the desired circuit performance for the determination
of the correct key. Increasing the key size is seen as one of the effective approaches
to counter the brute force method due to the inability of the attacker to transverse a
large key space with the existing computational capabilities.

Another common attack mechanism is RE [3–5]. It is used by attackers to determine the proprietary information, such as circuit netlist and layout. It generally consists of five steps: depackaging, delayering, imaging, annotation and extraction [49].
While the delayering of an IC involves the removal and scanning of each metal layer
up to the substrate level with different types of delayering methodology depending upon the complexity of each metal layer [49], the imaging of different layers
of the delayered IC is performed using an SEM [49]. Based on the imaging, RE
software tools are used to annotate and visualize the interconnects for all the IC layers [50]. RE of ICs is a costly proposition due to the need for advanced imaging
tools [49].

Most of the analog/RF ICs require correct biasing of the circuit to obtain
the desired circuit performance. Due to its importance, one of the popular defense mechanisms is to lock the biasing circuits to control the performance of the
analog/RF circuits. Removal attacks refer to the identification of the locked portion
and replacing it with an unlocked part to ensure proper performance of the circuit

[51, 52]. However, it involves certain challenges in terms of the determination of the

Design Obfuscation and Performance-Locking Solutions **163**

**Figure** **7.27** Flowchart involving steps to perform SMT attacks on analog/RF ICs.
(Adapted from [56].)

obfuscated components and the redesign of such components with similar components at the schematic and layout level to obtain the desired specifications.

SAT attacks [46, 53] are generally used on combinational logic-locked circuits as
they use Boolean satisfiability to determine the correct keys. It is generally effective
against AMS circuits which solely rely on locking of the digital component. The
SMT attack [54] is a stronger superset of the SAT which can handle non-Boolean
parameters and delayed logic locking [55] and hence, better suited to analog/RF circuits. SMT attacks require the attacker to identify the obfuscated components and
the input-output relationship of the circuits to formulate the equations for the SMT
solver [56, 57]. The attacker can obtain this information from the circuit netlist, process design kit (PDK) information and the circuit specifications from the datasheet.
Obtaining the circuit netlist often requires the attacker to reverse engineer the oracle
or obtain the netlist from the untrusted foundry. The SMT solver can return a unique
key or a set of multiple keys, which requires the attacker to use the oracle chip to
further determine the correct key [56]. Figure 7.27 illustrates the flowchart for performing SMT attacks on analog/RF ICs. While SMT attacks require prior circuit
expertise for constraint formulations, optimization algorithms such as the genetic
algorithm (GA) [58] only require the circuit net-list and the oracle for the key exploration. The GA [58] is an advanced form of an SMT attack which uses optimization
techniques to search for the correct key in the search space. Unlike the SMT attacks,
it is able to perform multi-objective optimization and return a unique key [28, 58].

Calibration

Locking

Physical Design

Obfuscation

Digital Locking of

AMScircuits

Moderate Medium Low Yes No No No Yes Yes No(N.D.)
Dependencies

Memristors Moderate High Low Yes No No Yes No Yes No(N.D.)

AFGTs Moderate Medium Low Yes No No Yes No(N.D.) Yes No(N.D.)

Neural Network

Moderate Medium Low Yes No No Yes No Yes No(N.D.)
Biasing

Programmmable

Easy Low Low Yes Yes Yes Yes Yes Yes Yes
AnalogICs

HighVt
Moderate High Medium Yes Yes Yes Yes Yes Yes Yes
/LowVt

Sizing
Easy High Medium Yes Yes Yes Yes Yes Yes Yes
Camouflaging

AMSlock Moderate Medium Medium Yes No No No Yes Yes Yes
MixLock 2.0 Moderate Medium Medium Yes No No Yes Yes Yes Yes

Layout
Dependent
Effects(LDE)

Moderate Low Medium Yes Yes Yes Yes Yes Yes Yes

Here N.D stands for Not Demonstrated.
Adapted from [28].

Design Obfuscation and Performance-Locking Solutions **165**

**7.7** **CONCLUSION**

The digital key–based performance locking, calibration locking, physical design obfuscation and digital locking of AMS circuits approaches in terms of ease of implementation, additional incurred costs in terms of die area and power consumption as
well as resilience against different types of attacks are tabulated in Table 7.3. The
various attacks discussed are the SAT [46, 53], SMT [56], removal attacks [51, 52]
and GA [58] attacks, respectively. The projected rising demands of ICs in health
care, agriculture and other commercial sectors due to the growth of technologies like
Internet of Things (IoT), 5G, etc., will lead to more sophisticated RE attacks on ICs
in the future. This increased vulnerability creates an enhanced demand for protecting
the product’s functionality as well as their design IPs in the future. The chapter provides an overview of the existing approaches to secure analog/RF and mixed-signal
ICs to enable the reader to understand and select the suitable approach for their individual implementations. Silicon demonstration of the approaches would increase
their robustness to chip-level variations and increase consumer confidence for users
in industries and governments, enabling more widespread implementations.

**7.8** **ACKNOWLEDGEMENT**

This work was partially supported by the I/UCR Center For Hardware and Embedded
System Security and Trust (CHEST P08_20, P14_21 & P15_22).

**REFERENCES**

1. M. Rostami, F. Koushanfar, and R. Karri. A Primer on Hardware Security: Models,
Methods, and Metrics. Proceedings of the IEEE, 102(8):1283–1295, 2014.
2. M. M. Tehranipoor, U. Guin, and D. Forte. Counterfeit Integrated Circuits. Springer
International Publishing, 2015.
3. R. Torrance and D. James. The State-of-the-Art in Semiconductor Reverse Engineering.
In Design Automation Conference, pages 333–338. IEEE, 2011.
4. Bernhard Lippmann, Michael Werner, Niklas Unverricht, Aayush Singla, Peter Egger,
Anja D¨ubotzky, Horst Gieser, Martin Rasche, Oliver Kellermann, and Helmut Graeb.
Integrated Flow for Reverse Engineering of Nanoscale Technologies. In Asia South
Pacific Design Automation Conference, pages 82–89. IEEE, 2019.
5. U. Guin, K. Huang, D. DiMase, J. M. Carulli, M. Tehranipoor, and Y. Makris. Counterfeit Integrated Circuits: A Rising Threat in the Global Semiconductor Supply Chain.
Proceedings of the IEEE, 102(8):1207–1228, 2014.
6. M. Elshamy, A. Sayed, M.-M. Lou¨erat, H. Aboushady, and H.-G. Stratigopoulos. Locking by Untuning: A Lock-Less Approach for Analog and Mixed-Signal IC Security.
IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 29(12):2130–2142,
2021.
7. A. Antonopoulos, C. Kapatsori, and Y. Makris. Security and Trust in the Analog/MixedSignal/RF Domain: A Survey and a Perspective. In IEEE European Test Symposium.
IEEE, 2017.

**166** Advances in Hardware Design for Security and Trust

8. M. M. Alam, S. Chowdhury, B. Park, D. Munzer, N. Maghari, M. Tehranipoor, et al.
Challenges and Opportunities in Analog and Mixed Signal (AMS) Integrated Circuit
(IC) Security. Journal of Hardware and Systems Security, 2:15–32, 2018.
9. R. A. Rutenbar. Design Automation for Analog: The Next Generation of Tool Challenges. In IEEE/ACM International Conference on Computer-Aided Design, pages 458–
460. IEEE, 2006.
10. J. A. Roy, F. Koushanfar, and I. L. Markov. Epic: Ending Piracy of Integrated Circuits.
In Design, Automation and Test in Europe, pages 1069–1074. IEEE, 2008.
11. R. S. Chakraborty and S. Bhunia. Hardware Protection and Authentication Through
Netlist Level Obfuscation. In IEEE/ACM International Conference on Computer-Aided
Design, pages 674–677. IEEE, 2008.
12. A. Baumgarten, A. Tyagi, and J. Zambreno. Preventing IC Piracy using Reconfigurable
Logic Barriers. IEEE Design and Test of Computers, 27(1):66–75, 2010.
13. J. Rajendran, Y. Pino, O. Sinanoglu, and R. Karri. Security Analysis of Logic Obfuscation. In Design Automation Conference, pages 83–89. IEEE, 2012.
14. Y. Xie and A. Srivastava. Mitigating SAT Attack on Logic Locking. In Cryptographic
Hardware and Embedded Systems, pages 127–146. Springer, 2016.
15. X. Xu, B. Shakya, M. M. Tehranipoor, and D. Forte. Novel Bypass Attack and BDDbased Tradeoff Analysis against all known Logic Locking Attacks. In Cryptographic
Hardware and Embedded Systems, pages 189–210. Springer, 2017.
16. A. Vijayakumar, V. C. Patil, D. E. Holcomb, C. Paar, and S. Kundu. Physical Design
Obfuscation of Hardware: A Comprehensive Investigation of Device and Logic-Level
Techniques. IEEE Transactions on Information Forensics and Security, 12(1):64–77,
2017.
17. A. Chakraborty, N. G. Jayasankaran, Y. Liu, J. Rajendran, O. Sinanoglu, A. Srivastava, Y. Xie, M. Yasin, and M. Zuzak. Keynote: A Disquisition on Logic Locking.
IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems,
39(10):1952–1972, 2020.
18. V. Venugopal Rao and I. Savidis. Performance and Security Analysis of ParameterObfuscated Analog Circuits. IEEE Transactions on Very Large Scale Integration Systems, 29(12):2013–2026, 2021.
19. J. Wang, C. Shi, A. Sanabria-Borbon, E. S´anchez-Sinencio, and J. Hu. Thwarting Analog IC Piracy via Combinational Locking. In IEEE International Test Conference, pages
1–10. IEEE, 2017.
20. H. K. Hoe, J. Rajendran, and R. Karri. Towards Secure Analog Designs: A Secure Sense
Amplifier Using Memristors. In IEEE Computer Society Annual Symposium on VLSI,
pages 516–521. IEEE, 2014.
21. S. Govinda Rao Nimmalapudi, G. Volanis, Y. Lu, A. Antonopoulos, A. Marshall, and
Y. Makris. Range-Controlled Floating-Gate Transistors: A Unified Solution for Unlocking and Calibrating Analog ICs. In Design Automation and Test in Europe Conference
and Exhibition, pages 286–289. IEEE, 2020.
22. A. Ash-Saki and S. Ghosh. How Multi-Threshold Designs Can Protect Analog IPs. In
IEEE International Conference on Computer Design, pages 464–471. IEEE, 2018.
23. J. Leonhard, A. Sayed, M.-M. Lou¨erat, H. Aboushady, and H. Stratigopoulos. Analog
and Mixed-Signal IC Security via Sizing Camouflaging. IEEE Transactions on Computer Aided Design of Integrated Circuits and Systems, 40(5):822–835, 2021.
24. N. G. Jayasankaran, A. S. Borbon, E. Sanchez-Sinencio, J. Hu, and J. Rajendran. Towards Provably-Secure Analog and Mixed-Signal Locking Against Overproduction.
IEEE Transactions on Emerging Topics in Computing, 10(1):386–403, 2020.

Design Obfuscation and Performance-Locking Solutions **167**

25. J. Leonhard, N. Limaye, S. Turk, A. Sayed, A. Rizo, H. Aboushady, O. Sinanoglu, and
H.-G. Stratigopoulos. Digitally Assisted Mixed-Signal Circuit Security. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 41(8):2449–2462,
2022.
26. J. Leonhard, M. Yasinand, S. Turk, M. Nabeel, M. Lou¨erat, C. Roselyne, H. Aboushady,
O. Sinanoglu, and H.-G. Stratigopoulos. Mixlock: Securing Mixed-Signal Circuits via
Logic Locking. In Design Automation Test in Europe Conference and Exhibition, pages
84–89. IEEE, 2019.
27. C. Herder, M.-D. Yu, F. Koushanfar, and S. Devadas. Physical Unclonable Functions
and Applications: A Tutorial. Proceedings of the IEEE, 102(8):1126–1141, 2014.
28. Sanabria-Borb´on, N. G. Jayasankaran, J. Hu, J. Rajendran, and E. S´anchez-Sinencio.
Analog/RF IP Protection: Attack Models, Defense Techniques, and Challenges. IEEE
Transactions on Circuits and Systems II: Express Briefs, 68(1):36–41, 2021.
29. V. V. Rao and I. Savidis. Protecting Analog Circuits with Parameter Biasing Obfuscation. In IEEE Latin American Test Symposium, pages 1–6. IEEE, 2017.
30. V. V. Rao and I. Savidis. Transistor Sizing for Parameter Obfuscation of Analog Circuits
Using Satisfiability Modulo Theory. In IEEE Asia Pacific Conference on Circuits and
Systems, pages 102–106. IEEE, 2018.
31. V. V. Rao and I. Savidis. Mesh Based Obfuscation of Analog Circuit Properties. In IEEE
International Symposium on Circuits and Systems (ISCAS), pages 1–5. IEEE, 2019.
32. K. Juretus, V. V. Rao, and I. Savidis. Securing Analog Mixed-Signal Integrated Circuits
Through Shared Dependencies. In ACM Great Lakes Symposium on VLSI, pages 483–
488. Association for Computing Machinery, 2019.
33. G. Volanis, Y. Lu, S. G. Rao Nimmalapudi, A. Antonopoulos, A. Marshall, and
Y. Makris. Analog Performance Locking through Neural Network-Based Biasing. In
IEEE VLSI Test Symposium, pages 1–6. IEEE, 2019.
34. V. Natarajan, S. Sen, A. Banerjee, A. Chatterjee, G. Srinivasan, and F. Taenzler. Analog Signature-Driven Postmanufacture Multidimensional Tuning of RF Systems. IEEE
Design and Test of Computers, 27(6):6–17, 2010.
35. Y. Lu, K. S. Subramani, H. Huang, N. Kupp, K. Huang, and Y. Makris. A Comparative Study of One-Shot Statistical Calibration Methods for Analog/RF ICs. In IEEE
International Test Conference, pages 1–10. IEEE, 2015.
36. J. W. Jeong, A. Nassery, J. N. Kitchen, and S. Ozev. Built-In Self-Test and Digital Calibration of Zero-IF RF Transceivers. IEEE Transactions on Very Large Scale Integration
Systems, 24(6):2286–2298, 2016.
37. M. Elshamy, A. Sayed, M.-M. Lou¨erat, A. Rhouni, H. Aboushady, and H.-G.
Stratigopoulos. Securing Programmable Analog ICs Against Piracy. In Design, Automation and Test in Europe Conference and Exhibition, pages 61–66. IEEE, 2020.
38. M. J. Aljafar, F. Aza¨ıs, M. Flottes, and S. Pagliarini. Leveraging Layout-based Effects
for Locking Analog ICs. In ACM Workshop on Attacks and Solutions in Hardware
Security, pages 5–13. Association for Computing Machinery, 2022.
39. J. Rajendran, M. Sam, O. Sinanoglu, and R. Karri. Security Analysis of Integrated
Circuit Camouflaging. In ACM SIGSAC Conference on Computer and Communications
Security, pages 709–720. Association for Computing Machinery, 2013.
40. S. Patnaik, M. Ashraf, J. Knechtel, and O. Sinanoglu. Obfuscating the Interconnects: Low-Cost and Resilient Full-Chip Layout Camouflaging. IEEE Transactions
on Computer-Aided Design of Integrated Circuits and Systems, 39(12):4466–4481,
2020.

**168** Advances in Hardware Design for Security and Trust

41. D. M. Binkley, C. E. Hopper, S. D. Tucker, B. C. Moss, J. M. Rochelle, and D. P. Foty. A
CAD Methodology for Optimizing Transistor Current and Sizing in Analog CMOS Design. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems,
22(2):225–237, 2003.
42. W. Daems, G. Gielen, and W. Sansen. Simulation-based Generation of Posynomial
Performance Models for the Sizing of Analog Integrated Circuits. IEEE Transactions
on Computer-Aided Design of Integrated Circuits and Systems, 22(5):517–534, 2003.
43. T. Y. Zhou, H. Liu, D. Zhou, and T. Tarim. A Fast Analog Circuit Analysis Algorithm for
Design Modification and Verification. IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems, 30(2):308–313, 2011.
44. A. Malak, Y. Li, R. Iskander, F. Durbin, F. Javid, J.-M. Guebhard, M.-M. Lou¨erat, and
A. Tissot. Fast Multidimensional Optimization of Analog Circuits Initiated by Monodimensional Global Peano Explorations. Integration, the VLSI Journal, 48(2):198–212,
2015.
45. Y. Li, Y. Wang, Y. Li, R. Zhou, and Z. Lin. An Artificial Neural Network Assisted
Optimization System for Analog Design Space Exploration. IEEE Transactions on
Computer-Aided Design of Integrated Circuits and Systems, 39(10):2640–2653, 2020.
46. M. Yasin, A. Sengupta, M. Nabeel, M. Ashraf, J. Rajendran, and O. Sinanoglu.
Provably-Secure Logic Locking: From Theory To Practice. In ACM SIGSAC Conference on Computer and Communications Security, pages 1601–1618. Association for
Computing Machinery, 2017.
47. J. Leonhard, M.-M. Lou¨erat, H. Aboushady, O. Sinanoglu, and H.-G. Stratigopoulos.
Mixed-Signal Hardware Security Using Mixlock: Demonstration in an Audio Application. In International Conference on Synthesis, Modeling, Analysis and Simulation
Methods and Applications to Circuit Design, pages 185–188. IEEE, 2019.
48. N. Limaye, E. Kalligeros, N. Karousos, I. G. Karybali, and O. Sinanoglu. Thwarting All Logic Locking Attacks: Dishonest Oracle with Truly Random Logic Locking. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems,
40(9):1740–1753, 2021.
49. V. Venugopal Rao, K. Juretus, and I. Savidis. Hidden Costs of Analog Deobfuscation
Attacks. IEEE Transactions on Very Large Scale Integration Systems, 31(11):1802–
1815, 2023.
50. K. Shamsi, M. Li, K. Plaks, S. Fazzari, D. Z. Pan, and Y. Jin. IP Protection and Supply
Chain Security through Logic Obfuscation: A Systematic Overview. ACM Transactions
on Design Automation of Electronic Systems, 24(6):65.1–65.36, 2019.
51. M. Yasin, B. Mazumdar, O. Sinanoglu, and J. Rajendran. Removal Attacks on Logic
Locking and Camouflaging Techniques. IEEE Transactions on Emerging Topics in
Computing, 8(2):517–532, 2020.
52. J. Leonhard, M. Elshamy, M.-M. Lou¨erat, and H.-G. Stratigopoulos. Breaking Analog Biasing Locking Techniques via Re-Synthesis. In Asia and South Pacific Design
Automation Conference, pages 555–560. IEEE, 2021.
53. P. Subramanyan, S. Ray, and S. Malik. Evaluating the Security of Logic Encryption
Algorithms. In IEEE International Symposium on Hardware Oriented Security and
Trust, pages 137–143. IEEE, 2015.
54. K. Z. Azar, H. M. Kamali, H. Homayoun, and A. Sasan. SMT Attack: Next Generation Attack on Obfuscated Circuits with Capabilities and Performance Beyond the
SAT Attacks. IACR Transactions on Cryptographic Hardware and Embedded Systems,
2019(1):97–122, 2018.

Design Obfuscation and Performance-Locking Solutions **169**

55. Y. Xie and A. Srivastava. Delay Locking: Security Enhancement of Logic Locking
Against IC Counterfeiting and Overproduction. In Design Automation Conference,
pages 1–6. IEEE, 2017.
56. N. G. Jayasankaran, A. S. Borb´on, A. Abuellil, E. S´anchez-Sinencio, J. Hu, and J. Rajendran. Breaking Analog Locking Techniques. IEEE Transactions on Very Large Scale
Integration Systems, 28(10):2157–2170, 2020.
57. V. V. Rao, K. Juretus, and I. Savidis. Practical Performance of Analog Attack Techniques. In IEEE International Symposium on Hardware Oriented Security and Trust,
pages 153–156. IEEE, 2022.
58. R. Y. Acharya, S. Chowdhury, F. Ganji, and D. Forte. Attack of the Genes: Finding Keys
and Parameters of Locked Analog ICs using Genetic Algorithm. In IEEE International
Symposium on Hardware Oriented Security and Trust. IEEE, 2020.

# 8 On-Chip Integrity,
### Reliability, and Aging Assurance Techniques for ICs

Manoj Yasaswi Vutukuru and Rashmi Jha

**8.1** **INTRODUCTION**

The globalization of the integrated circuit (IC) supply chain has transformed the
semiconductor industry, enabling rapid advancements in technology and driving innovation on a global scale. However, this globalization has also introduced a variety
of challenges in ensuring the integrity and reliability of ICs throughout their life cycle [1]. As ICs become increasingly integral to mission-critical applications, including consumer electronics, military, aerospace, and medical devices, it is necessary to
ensure the integrity and reliability of ICs.

One of the most significant challenges due to the globalization of the IC supply
chain is the increased risk of security vulnerabilities. The complex, multi-step process of IC design, fabrication, testing, and assembly involves multiple entities across
various geographic locations. This dispersion increases the probability of malicious
tampering, such as hardware Trojan (HT) insertions, counterfeit components, and
other forms of attack that can compromise the functionality and reliability of ICs.

Beyond security concerns, the reliability of ICs is also significantly influenced
by inherent degradation mechanisms that occur over time, such as Bias Temperature Instability (BTI), Hot Carrier Injection (HCI), and Time-Dependent Dielectric
Breakdown (TDDB). These mechanisms can lead to aging, resulting in performance
degradation and device failure. The advent of advanced packaging technologies, such
as heterogeneous integration in 2.5D and 3D ICs, adds an additional layer of complexity to these issues. The thermal management challenges associated with these
packaging methods can accelerate aging effects, particularly through electromigration, where the movement of metal atoms within ICs can lead to short- or open-circuit
failures. Given these challenges, ensuring the integrity and reliability of ICs throughout their life cycle is essential.

[DOI: 10.1201/9781003510949-8](https://doi.org/10.1201/9781003510949-8) **170**

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **171**

**Figure** **8.1** Bathtub curve illustrating the progression of component failure rates
throughout their operational lifetime.

Reliability (R) over time (t) is defined as the probability that an IC will operate
within its specified parameters from the beginning to the end of its lifetime. This can
be expressed mathematically as: R (t) = e <sup>−</sup> �tt0 <sup>λ(t)</sup> <sup>dt</sup>, where R (t) is the reliability at

time t, λ (t) is the failure rate at time t, and t0 is the start time of operation. It is
well known that IC components experience aging over time as they operate, which
leads to an increase in the failure rate. This behavior is commonly represented by the
bathtub curve seen in Figure 8.1. The curve describes the failure rate of a device as
a function of time, divided into three distinct phases: the early failure period (infant
mortality), the normal life period (constant failure rate), and the wear-out period
(increasing failure rate). In the early failure period, ICs may have a higher failure
rate due to defects or issues from manufacturing. This is shown by a quick drop in
the failure rate. During the normal life period, the failure rate becomes steady as the
defects are worked out and the ICs function reliably. Finally, in the wear-out period,
the failure rate starts to rise again as the ICs age and degrade, making failures more
likely.

This chapter deals with various reliability and integrity issues that affect ICs, with
a particular focus on the complexities introduced by heterogeneous packaging. It explores various monitoring techniques designed to monitor the reliability, aging, and
integrity of ICs over time. Furthermore, the chapter also addresses the specific challenges associated with advanced 2.5D/3D packaged ICs, highlighting the importance
of continuous monitoring in maintaining the long-term reliability of these advanced
emerging technologies.

**172** Advances in Hardware Design for Security and Trust

**8.2** **FUNDAMENTALS OF IC RELIABILITY AND AGING**

IC reliability refers to the ability of a circuit to perform its intended function consistently over its expected lifetime, even under varying operating conditions. However,
several factors can impact this reliability, leading to degradation and eventual failure
of the ICs.

**8.2.1** **KEY RELIABILITY CHALLENGES**

One of the primary challenges in maintaining IC reliability is the inherent degradation that occurs over time due to various physical and electrical stresses. Several key
mechanisms contribute to this degradation, including BTI, HCI, and TDDB.

 - Bias Temperature Instability (BTI): BTI is a phenomenon where the
threshold voltage of a transistor shifts due to prolonged exposure to high
temperature and electric fields. This shift can lead to slower transistor
switching times and degraded circuit performance, ultimately impacting
the overall reliability of the IC.

 - Hot Carrier Injection (HCI): HCI occurs when high-energy carriers, such
as electrons or holes, gain enough energy to break the bonds in the silicon
lattice of the transistor. This process can lead to the accumulation of charge
in the transistor’s gate oxide, causing shifts in the threshold voltage and
degrading the transistor’s performance over time.

 - Time-Dependent Dielectric Breakdown (TDDB): TDDB is a gradual
process where the insulating properties of the dielectric material in a transistor degrade due to the continuous application of voltage. Over time, this
can lead to the formation of conductive paths through the dielectric, eventually causing catastrophic failure of the transistor.

These degradation mechanisms not only reduce the performance of ICs but also
increase the probability of failures, which can be fatal in mission-critical applications
where reliability is important.

**8.2.2** **AGING AND ITS IMPACT ON ICs**

Aging in ICs refers to the gradual deterioration of the electrical and physical properties of the circuit over time. This process is influenced by various factors, including
thermal and electrical stress, manufacturing process variations, and environmental
conditions. Aging can occur in several ways, such as increased delay in critical signal paths, higher power consumption, and reduced noise margins. These effects can
lead to timing violations and, ultimately, device failure. Electromigration is another
significant aging mechanism that specifically affects the metal interconnects in ICs.
Electromigration occurs when the momentum transfer between conducting electrons
and metal atoms causes the metal atoms to migrate. This migration can lead to the
formation of voids or hillocks in the metal lines, which can cause open circuits or
short circuits, leading to device failure as shown in Figure 8.2. Electromigration is

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **173**

**Figure** **8.2** Electromigration in metal interconnects. (a) Short-circuit failure. (b)
Open-circuit failure.

particularly problematic in modern ICs, where the shrinking dimensions of the interconnects and the increasing current densities increase the problem.

The mean-time-to-failure (MTTF) of an interconnect can be estimated using
Black’s equation [2],

(8.1)

MTTF = A×J <sup>−n</sup> × exp

k×T

- Ea

where A is a cross-sectional area dependent constant, J is the current density, n is
a scaling factor, Ea is the activation energy, k is the Boltzmann constant, and T is
temperature in Kelvin.

The impact of aging is further observed in advanced IC designs, such as those
using 2.5D and 3D packaging. These packaging methods involve stacking multiple
dies on top of each other, creating long interconnects and complex thermal management challenges. The increased heat and mechanical stress in these advanced designs
can accelerate aging, leading to earlier failures if not properly managed.

**8.2.3** **THE ROLE OF MONITORING AND PREDICTION**

To mitigate the effects of aging and ensure the reliability of ICs, it is essential to
implement effective monitoring and prediction techniques. By continuously monitoring the IC activity during their operation, it is possible to detect early signs of
degradation and take corrective actions before a failure occurs.

Monitoring the IC activity involves tracking various parameters that reflect the circuit’s operational status. Recent approaches to IC monitoring have included methods
such as critical path delay measurement and the use of process control monitors.

One of the emerging approaches for monitoring IC reliability involves the use
of electromagnetic (EM) radiation–based techniques. These methods leverage the
unintentional EM emissions generated by the IC during its operation to monitor the

**174** Advances in Hardware Design for Security and Trust

**Figure 8.3** Reliability challenges in 2.5D/3D IC packaging.

circuit activity. By analyzing the patterns and intensity of these EM emissions, it is
possible to detect anomalies that may indicate aging or other reliability issues. EMbased monitoring offers the advantage of being non-invasive,allowing for continuous
monitoring without interfering with the normal operation of the IC.

In addition to monitoring, predictive modeling plays a crucial role in assessing
IC reliability. By simulating the expected aging behavior of the circuit under various operating conditions, it is possible to estimate the remaining useful life of
the IC and identify potential failures. These predictive models typically consist of
real-time data, physics-based models, and machine learning (ML) techniques, providing a comprehensive understanding of the aging process and its impact on
reliability.

**8.3** **CHALLENGES IN HETEROGENEOUS PACKAGING**

**8.3.1** **INTRODUCTION TO HETEROGENEOUS PACKAGING**

Heterogeneous packaging refers to the integration of multiple types of components,
such as processors, memory, and sensors, onto a single package, often using different
technologies and materials. This approach enables the creation of highly compact,
efficient, and high-performance systems by combining various ICs with different
functionalities into a single package. Examples of heterogeneous packaging include
2.5D and 3D ICs, where multiple dies are stacked or placed side by side on a single substrate (Figure 8.3). These dies or chiplets are interconnected using advanced
technologies like through-silicon vias (TSVs) or microbumps.

While heterogeneous packaging offers significant advantages in terms of performance, power efficiency, and area, it also introduces a variety of challenges, particularly related to the reliability of the packaged ICs. Ensuring the long-term reliability
of these systems requires careful consideration of several factors which can impact
the overall performance and lifetime of the device.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **175**

**8.3.2** **RELIABILITY CHALLENGES IN HETEROGENEOUS PACKAGING**

**8.3.2.1** **Thermal Management**

One of the primary challenges in heterogeneous packaging is managing the heat generated by the densely packed components. The integration of multiple dies within a
single package leads to increased power density, which can result in higher operating
temperatures. Efficient thermal management is crucial to prevent overheating, which
can accelerate aging mechanisms like electromigration, ultimately leading to device
failure.

Non-uniform heat dissipation can cause hot spots within the package, leading to
uneven temperature distribution. These thermal gradients can accelerate reliability
issues, particularly in the interconnects and other components.

**8.3.2.2** **Interconnect Reliability**

The reliability of interconnects is another significant concern in heterogeneous packaging. The use of TSVs, microbumps, and other advanced interconnect technologies
in 2.5D and 3D ICs are more prone to electromigration. TSVs can suffer from issues like void formation and electromigration, which can compromise the electrical
integrity of the connections between dies. Additionally, the mechanical stresses induced during the manufacturing process, as well as thermal cycling during operation,
can lead to the delamination or cracking of interconnects. These mechanical failures
can result in complete circuit failures, making it essential to carefully design, test
and monitor interconnects for long-term reliability.

**8.3.2.3** **Aging and Degradation**

As with all ICs, the components within a heterogeneous package undergo aging and
degradation over time. However, the closely packed nature of these packages can
accelerate aging effects due to the higher operating temperatures and mechanical
stresses involved. For example, electromigration can be accelerated in the densely
packed interconnects of 3D ICs, leading to premature failure. Additionally, the integration of different types of ICs with varying aging characteristics can complicate
the prediction of overall system reliability. Each component may degrade at a different rate, making it challenging to ensure consistent performance across the entire
package.

**8.4** **TECHNIQUES** **FOR** **RELIABILITY** **AND** **INTEGRITY** **MONITORING**
**IN ICs**

This section provides a survey of traditional IC testing methods and explores the
advantages and advancements in EM-based methods for reliability or circuit activity
monitoring.

**176** Advances in Hardware Design for Security and Trust

**8.4.1** **TRADITIONAL IC RELIABILITY TESTING METHODS**

Traditional IC testing and reliability monitoring methods have evolved over decades,
providing a strong foundation for detecting faults and ensuring the integrity of
ICs. These methods are typically employed during the manufacturing process and
throughout the operational life of the ICs.

**8.4.1.1** **Built-In Self-Test (BIST)**

Built-In Self-Test (BIST) is a technique where additional circuitry is embedded
within the IC to enable the device to test its own functionality. BIST is commonly
used during the manufacturing process to detect defects and can also be used for
periodic testing during the IC’s operational life. It is generally useful for automating
the testing process by reducing the need for external testing equipment. However,
the complexity and cost of IC design increases due to the additional area and power
consumption required for the self-test circuitry.

**8.4.1.2** **Burn-In and Accelerated Life Testing**

Burn-In testing and accelerated life testing are widely used methods to identify earlylife failures, often referred to as “infant mortality” in ICs. In these tests, ICs are
subjected to elevated temperatures and voltages for long durations. This process accelerates the failure of weak devices that might not survive under normal operating
conditions thereby ensuring that only the most reliable ICs proceed to the next stage
of manufacturing. The goal is to accelerate the aging process and induce failures
quickly, allowing manufacturers to predict the IC’s life span under normal operating
conditions. However, these tests are time-consuming, energy-intensive, and may not
be effective in identifying defects that occur only under specific operational conditions such as HTs.

**8.4.2** **RECENT METHODS FOR IC RELIABILITY MONITORING**

As IC designs become more complex and the demand for higher reliability increases,
traditional testing methods face limitations in detecting and predicting all potential
failure modes. Emerging techniques, such as critical path delay measurements, novel
devices like Resistive Random Access Memory (RRAM) and Ferroelectric FieldEffect Transistors (FeFETs), and EM signal-based methods, offer innovative solutions for detecting and mitigating reliability issues. This section provides a survey of
these emerging methods, discussing their principles, advantages, and limitations.

**8.4.2.1** **Critical Path Delay Measurements**

Critical path delay measurements are a vital tool for detecting aging and reliability
issues in ICs. The critical paths in an IC are those that determine its maximum operational frequency. As ICs age due to various degradation mechanisms such as BTI and
HCI, the delays along these paths increase, potentially leading to timing violations
and sometimes device failure.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **177**

Ring Oscillator-Based Techniques: Ring oscillators (ROs) are commonly used
to monitor delay variations in ICs. An RO consists of an odd number of inverters
connected back-to-back, generating a signal that oscillates at a frequency dependent
on the delay of the inverters. As the IC ages, the delay increases, causing the RO’s
frequency to decrease. By monitoring these frequency changes, it is possible to detect
aging effects. RO-based sensors are easy to implement and provide valuable insights
into the overall performance of the IC. However, they may not accurately represent
the delays on the actual critical paths, leading to less precise aging detection. Despite
this limitation, they are widely used due to their simplicity and effectiveness [3, 4,
5].
Shadow Register-Based Techniques: To directly monitor the delays on critical
paths, Shadow Register techniques are used. A shadow register is placed alongside a
regular register on a critical path, with the clock delayed slightly [6, 7]. If the signal
takes too long to propagate due to aging, the shadow register will capture a different
value, indicating a potential timing violation. This method provides direct and accurate monitoring of critical path delays, making it an effective method for detecting
aging effects. However, careful design is necessary to ensure that the shadow registers are correctly synchronized with the critical paths they monitor. It increases the
design complexity and power consumption of the IC.

**8.4.2.2** **Reliability Monitoring Using Novel Devices**

The integration of novel devices such as Resistive Random Access Memory (RRAM)
and Ferroelectric Field-Effect Transistors (FeFETs) into ICs has opened new avenues
for reliability monitoring. These devices offer unique properties that can be leveraged
to detect aging and other reliability issues in real time.

RRAM-Based Monitoring: RRAM devices, known for their non-volatile memory properties, can also be used for reliability monitoring. RRAM operates by
switching between a high-resistance state (HRS) and a low-resistance state (LRS)
based on the applied voltage. The resistance state of RRAM changes over time due
to aging, which can be monitored to assess IC reliability [8].

FeFET-Based Monitoring: FeFETs are another promising novel device for aging detection. FeFETs incorporate a ferroelectric material in the gate stack, allowing
for a configurable threshold voltage. This property enables the creation of delay lines
with variable delays, which can be used to monitor critical path delays in real-time.
FeFET-based monitors offer several advantages over traditional methods, including
reduced area and power consumption, as well as improved accuracy in delay measurement. By using FeFETs, designers can create highly sensitive aging sensors that
can detect even minor changes in critical path delays, providing early warning of
potential reliability issues [9].

**8.4.2.3** **A Survey of EM-Based Reliability Monitoring Methods**

EM-based monitoring techniques involve capturing and analyzing the EM radiation
emitted by ICs as they operate. These emissions occur due to the switching activity

**178** Advances in Hardware Design for Security and Trust

**Figure 8.4** Overview of EM side-channel-based reliability monitoring.

of transistors and the flow of current through metal interconnects. They contain valuable information about the internal state of the IC. The primary advantage of EMbased monitoring is its non-invasive nature. Unlike traditional methods, which often
require direct contact with the IC, EM-based techniques can monitor the IC without
interfering with its operation. This makes EM-based methods well suited for realtime monitoring of ICs, where access to the device may be limited.

Overview of EM Monitoring Techniques: A typical EM side-channel monitoring process begins with capturing EM emissions from the IC as shown in Figure 8.4. This can be done using either external near-field probes or on-chip sensors. Near-field probes are positioned close to the IC at locations where the emissions are strongest. The captured signals are then analyzed and compared with the
golden reference to detect anomalies that may indicate aging, HTs, or other reliability issues. On-chip EM sensors offer a more localized and sensitive method of
capturing EM emissions. These sensors are integrated directly into the IC, allowing for real-time monitoring of the IC’s activity. The proximity of the sensors to the
emission sources results in high signal quality and reduces the impact of external
noise.

On-chip sensors also provide higher spatial and temporal resolution than external
probes, enabling more accurate detection of reliability issues. These sensors can be
effective in detecting changes in the EM spectrum associated with phenomena such
as HTs and aging or electromigration.

As discussed in [10], the EM radiation (E (t)) emitted by an IC can be divided into
various components including normal circuit operation (Eori (t)), process variations
(Epv (t)), and measurement noise (En (t)). If an HT is present in the circuit, it adds
another component ET (t), which alters the EM radiation, as described by (8.2).

E (t) = Eori (t)+ Epv (t)+ En (t)+ ET (t) (8.2)

The intensity of accumulated EM emissions over the surface of the chip was modeled
using (8.3) in [11], where E represents the accumulated EM emission, I and Z are the

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **179**

current and impedance at position (x, y), and r is the distance from the observation
point to the source.

x

(I (x, y)) <sup>2</sup> Z (x, y)

dx dy (8.3)
4π(r (x, y)) <sup>2</sup>

E ∝

y

x

S
4πr <sup>2</sup> <sup>dx dy =</sup> y

      

When an IC undergoes aging due to mechanisms like electromigration, HCI, or BTI,
the EM emissions change over time and the emissions due to the aging of IC can be
described using (8.4),

Eaging (t) ∝

y

x

V (x,y)
Raging(x,y)

- 4π(

dxdy (8.4)
4π(r (x, y)) <sup>2</sup>

Zaging (x, y)

r�(2x, y)) <sup>2</sup>

where Eaging (t) represents the change in EM emissions due to aging, V (x, y) is the
voltage at location (x, y), Raging (x, y) is the increased resistance caused by aging
mechanisms (such as electromigration), Zaging (x, y) is the changed impedance due to
aging, and r (x, y) is the distance from the point of observation. This equation models how aging impacts the IC’s EM emissions. As aging progresses, the resistance
in the interconnects increases, reducing the current and thereby modifying the EM
emissions from the IC.

Near-Field Probe Methods: Numerous studies have explored the application of
EM-based methods for reliability monitoring, focusing on different aspects of IC
reliability. HTs represent a significant security threat in ICs, as they can lead to malfunction, data leakage, or early failure. Detecting these Trojans is challenging as
they remain dormant until triggered by specific conditions. EM-based methods have
emerged as an effective solution for identifying these hidden Trojans. EM emissions
are unintentional signals resulting from the switching activity within the IC. Analyzing the captured data can reveal the presence of a Trojan in the device under test
(DUT). Near-field probes are often used to capture these emissions in a laboratory
environment. Researchers such as S¨oll et al. [12] have shown that by comparing the
EM signatures of a suspected IC against a golden reference, it is possible to identify
differences indicative of Trojan activity. This EM side-channel analysis process relies on detecting minute variations in the EM emissions caused by the additional or
altered circuitry introduced by the Trojan.

Another approach to Trojan detection is EM fingerprinting, which involves creating a unique EM signature for each IC based on its normal operating behavior.

Generally, even when a dormant Trojan is present, its presence alters the IC’s
EM fingerprint. Balasch et al. [13] have successfully applied this method to detect extremely small Trojans by focusing on these subtle changes in EM emissions.
This technique is valuable for identifying Trojans that are designed to be minimally invasive, which would normally evade detection through conventional methods. Backscattering techniques have also been introduced as an innovative method
for Trojan detection. In this approach, a carrier signal is introduced into the IC, and
the backscattered EM waves are analyzed. Adibelli et al. [14] demonstrated that by
examining these backscattered signals, it is possible to detect the presence of Trojans

**180** Advances in Hardware Design for Security and Trust

embedded within the IC. This method leverages the unique interactions between the
injected signal and the altered circuitry within the IC, providing a new technique of
Trojan detection using EM signals.

Counterfeit ICs pose a serious threat to both the reliability and security of electronic systems. These counterfeit components, which can range from recycled and
remarked chips to unauthorized clones, generally fail to meet the quality standards
required for critical applications. Detecting counterfeit ICs is therefore essential to
prevent system failures and maintain the integrity of supply chains. EM radiationbased methods have proven to be highly effective in counterfeit detection. One innovative approach in this field is the use of device fingerprinting through EM emissions.
Each IC, due to its unique physical structure and manufacturing process, generates a
distinct EM signature. Huang et al. [15] developed a method that uses these unintentional EM emissions to authenticate ICs. By comparing the EM emission profiles of
a given IC against those of known authentic devices (golden reference), it is possible
to identify counterfeit components with a high accuracy.

Recent advancements in counterfeit detection have incorporated deep learning
techniques to enhance the analysis of EM data. Zhang et al. [16] employed deep
residual neural networks to process EM emissions, which improved the classification
accuracy of counterfeit detection. The use of deep learning allows for the processing of vast amounts of EM data and the extraction of complex patterns that might
indicate a counterfeit device. This method not only improves detection accuracy but
also reduces the need for extensive preprocessing of the EM data. In another work,
Ahmed et al. [4] applied this technique to field-programmable gate arrays (FPGAs),
using a cosine similarity metric to compare the EM fingerprints of different devices.
This approach is useful in environments where ICs need to be authenticated quickly
and with minimal disruption to their operation.

Reliability monitoring also involves continuously assessing the behavior of an IC
to detect issues such as aging, electromigration, and other forms of degradation that
can lead to failure. EM radiation-based methods offer an effective means of conducting this monitoring in a non-invasive and real-time manner. By capturing and
analyzing the EM emissions of an IC during its operation, it is possible to continuously monitor the reliability and predict potential failures before they occur.

Challenges: The methods discussed above have successfully used near-field
probes to capture EM emissions for detecting HTs, and counterfeit components to
ensure the reliability of ICs. However, there are some challenges associated with
their application. The sensitivity of EM probes is crucial for accurately detecting the
signals indicative of issues like Trojans, counterfeit components, or aging. Environmental noise and variations in EM emissions due to process variations or operational
conditions can also complicate the data collection process and subsequent analysis.
Additionally, while near-field probes are effective in capturing EM emissions, they
are limited to experimental setups and do not support continuous, real-time monitoring of ICs in operational environments. To address these limitations, on-chip antenna
structures have been developed, enabling continuous monitoring of ICs, which offers
a more practical and integrated solution for real-time reliability assessment and threat
detection.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **181**

On-Chip EM Sensor Applications: He et al. [17] introduced a novel approach
using on-chip EM sensors for real-time Trojan detection. The sensor, designed to
mimic the structure of a LANGER RF probe, was integrated into the IC to monitor
its EM emissions continuously. They demonstrated that this on-chip sensor could detect the presence of various HTs with high accuracy. The sensor’s ability to operate
effectively in real time makes it suitable for continuous monitoring of IC reliability
during operation. Chen et al. [18] introduced a novel approach to reliability monitoring and hardware Trojan detection using Magnetic Tunnel Junction (MTJ)–based
sensors. Typically used in spintronic devices due to their ability to detect changes in
magnetic fields, MTJs are used in this study for monitoring the EM emissions of ICs.
The authors leveraged the high sensitivity of MTJs to detect abnormal current patterns that may indicate the presence of HTs or other reliability concerns. Vutukuru
et al. [19] highlighted the advantages of using on-chip antennas for continuous EM
monitoring. This allows for more accurate detection of changes in the IC’s EM profile that may indicate aging, electromigration, or other reliability issues.

On-chip antennas, while providing enhanced monitoring capabilities, can introduce design complexity and may be sensitive to layout variations. Despite these
challenges, the potential of EM-based methods to provide real-time, non-invasive
monitoring makes them a valuable tool to ensure the reliability and security of ICs.

**8.5** **EMERGING TECHNIQUES FOR IC RELIABILITY MONITORING**

In this section, we discuss a few emerging techniques that enable reliability and
security monitoring of ICs in detail. These methods use novel devices like RRAM
and FeFETs, as well as ML approaches, to provide more accurate, scalable, and
integrated solutions for IC monitoring. We also discuss recent approaches in on-chip
EM sensor-based methods for reliability monitoring and explore the challenges and
future research directions.

**8.5.1** **RRAM-BASED AGING AND INTEGRITY MONITORING**

The RRAM-based aging and integrity monitoring method by Dewey et al. [20] introduces a novel approach using RRAM devices to monitor the aging and integrity of
ICs. RRAM is a type of non-volatile memory that can switch between high-resistance
and low-resistance states, depending on the applied voltage. This characteristic is
leveraged in a monitoring system where changes in the resistance of RRAM devices
over time correlate with the aging of the circuit under test (CUT).

**8.5.1.1** **Threat Model**

The security concerns associated with untrusted foundries in IC manufacturing are
a focus of this work. These foundries might introduce malicious modifications, such
as HTs, that can alter the function or shorten the life span of ICs. The RRAM-based

**182** Advances in Hardware Design for Security and Trust

**Figure** **8.5** (a) Schematic of aging circuit; (b) percent high output of the aging circuitry with various current inputs to the data AHC [20].

monitoring system is designed to track the aging process of the ICs, as tampering
typically accelerates aging due to changes in thermal and operational conditions.

**8.5.1.2** **Experimental Setup**

This monitoring system uses RRAM devices, which can switch between two states: a
high-HRS and LRS. The authors designed a compact setup with an RRAM crossbar
array made up of two columns, each with five RRAM devices. One column is set
to the HRS, where the resistance naturally drifts and weakens over time, while the
other column is kept in the LRS as a stable reference. This design helps the monitoring system detect changes in resistance that indicate the aging of the CUT. Figure
8.5(a) illustrates the configuration of the RRAM crossbar array used in this method.
The HRS column is prone to resistance degradation over time, while the LRS column provides a stable reference, enabling the system to detect and measure aging
effects in the CUT. The authors tested the RRAM devices under different conditions
to simulate aging. They applied varying voltage levels and monitored the changes
in resistance over time. The results showed that the resistance in the HRS column
degrades faster when exposed to higher temperatures or voltages, providing a clear
signal that the circuit is aging. The monitoring system captures these changes in
real-time.

**8.5.1.3** **Aging Prediction Process**

The RRAM-based monitoring system processes the output from the RRAM array using Axon-Hillock Circuits (AHCs), which convert the changes in current into spiking
voltage signals. These signals are then processed by a D Flip Flop (DFF) to produce
a digital output that reflects the aging state of the circuit. As the resistance in the
HRS devices degrades over time, the output from the monitoring system changes,
giving a measurable indication of how much the circuit has aged.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **183**

Figure 8.5(b) shows the output signal from the RRAM-based monitoring system
as the HRS resistance degrades. The figure shows how the AHCs and DFF work together to convert the gradual changes in resistance into a digital signal that indicates
the aging process. As the HRS resistance increases due to aging, the output signal
reflects this degradation, providing a clear and quantifiable measure of the circuit’s
aging state. This output can be compared to the expected aging profiles of circuits
made in trusted versus untrusted foundries. If a circuit shows signs of aging faster
than expected, it could suggest tampering or the presence of HTs in the IC.

**8.5.2** **LOW-OVERHEAD IN-SITU AGING MONITORING USING**
**RECONFIGURABLE FeFET**

In this section, we discuss a novel approach to in-situ aging monitoring in ICs using
a FeFET buffer with a programmable delay [9]. This method addresses the challenges associated with IC aging like the increase in signal delay over time, which
can lead to timing violations and potential circuit failures. By utilizing FeFETs, this
approach provides a flexible and low-overhead solution for detecting aging effects
and improving the long-term reliability and security of ICs.

**8.5.2.1** **Threat Model and Motivation**

Aging in ICs is influenced by various factors such as operating conditions, process
variations, and potential malicious tampering at untrusted foundries that can accelerate degradation. Traditional aging sensors often introduce significant area and timing overhead, limiting their effectiveness. To overcome these limitations, the authors
propose an aging sensor that leverages FeFET buffers with configurable delay. This
design reduces overhead and enhances the accuracy of aging detection, to provide
security for ICs fabricated in untrusted foundries.

**8.5.2.2** **Experimental Setup**

The FeFET-based aging sensor replaces traditional multiplexer-based sensors, which
typically require multiple delay paths and introduce additional loading capacitance.
In contrast, the FeFET buffer provides a single, reconfigurable delay path, minimizing both circuit area and timing overhead. This design allows for more precise slack
estimation in critical paths, improving the accuracy of aging detection. Figure 8.6
illustrates the slack detection mechanism implemented with the FeFET-based aging
sensor. Here, the FeFET buffer provides a configurable delay that can be adjusted to
match the specific aging characteristics of the IC. This flexibility allows the sensor
to closely estimate the actual slack in the critical path, reducing the margin for error
compared to traditional multiplexer-based approaches.

Experiments were conducted using the C17 ISCAS85 benchmark circuit, simulating the effects of aging over time. They tested the FeFET buffers under various
conditions by adjusting the threshold voltages to simulate different levels of aging.
The results reveal that the FeFET-based sensor introduces significantly less delay to
the critical path compared to traditional methods, with an average delay increase of

**184** Advances in Hardware Design for Security and Trust

**Figure 8.6** Slack detection with FeFET-based aging sensor [9].

only 7% compared to 18% for the multiplexer-based sensor. This reduction in delay
is directly attributed to the elimination of additional capacitance and the more precise
control over delay provided by the FeFET buffer.

**8.5.2.3** **Aging Prediction Process**

The FeFET-based aging monitor operates by adjusting the threshold voltage of the
FeFET buffer to vary the delay in the critical path. As the IC ages, the system reprograms the threshold voltage to reflect changes in the circuit’s characteristics, enabling continuous monitoring and adaptation. This capability ensures that the sensor
provides accurate slack estimates throughout the IC’s life span, even as the circuit
undergoes stress and degradation.

The experimental results demonstrate that compared to traditional multiplexerbased approaches, the FeFET sensor shows improved aging detection accuracy and
reduced overhead. Its ability to dynamically adjust delay while minimizing the impact on the critical path makes it a promising solution for applications where reliability and security are critical.

**8.5.3** **AGING** **PREDICTION** **USING** **RING** **OSCILLATORS** **AND** **MACHINE**
**LEARNING**

In this section, we explore a novel method for predicting the aging of ICs by utilizing ROs combined with ML techniques [21]. This approach plays an important
role in modern IC reliability by providing a method to detect HTs and other forms
of tampering that can accelerate aging. Identifying these issues early is crucial for
maintaining the long-term functionality of ICs.

**8.5.3.1** **Threat Model**

The threat model in this research suggests that a compromised IC will age faster,
shortening its expected life span. For example, an IC designed to last five years might
fail in four if it has been tampered with, such as by inserting a Trojan or using poor

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **185**

**Figure 8.7** (a) RO setup in FPGA with HTs, counter and CUT. (b) Full circuit with
subcircuits spread across the FPGA [21].

manufacturing processes. To address this issue, the research uses data-driven methods, focusing on ROs as simple, low-overhead sensors. ROs monitor the IC’s aging
by monitoring how their oscillation frequency decreases over time. Normally, this
decrease is gradual, but if the IC is compromised, the frequency drops faster, signaling potential tampering.

**8.5.3.2** **Experimental Setup**

The experimental setup for this research was implemented using a Basys3 board
which consists of a Xilinx Artix-7 FPGA. FPGAs are more suitable for such
experiments as they allow precise control over the placement and activation of logic
blocks, making it easier to simulate and observe the effects of accelerated aging.

The ROs used in the experiment were designed with 15 stages, each consisting
of one lookup table (LUT). This design ensured that each RO could fit within a
single configurable logic block (CLB) on the FPGA, maintaining a balance between
accuracy and space efficiency. The frequency of each RO was measured using 32-bit
digital counters, which were positioned directly beside the ROs to ensure accurate
and consistent data collection. Figure 8.7(a) provides a schematic representation of
the experimental setup, showing the placement of the RO, the HT, the counter, and
the CUT on the FPGA. ROs are positioned close to the HT and the CUT to closely
monitor the effects of HT activation on the RO’s frequency. The proximity of these
components is crucial for detecting the changes in frequency that indicate accelerated
aging. Figure 8.7(b) shows the complete circuit setup on the FPGA, including the
distribution of seven RO-HT-counter subcircuits across the FPGA.

To simulate the presence of HTs, four flip-flops oscillating at 100 MHz were
placed near the ROs. This setup was designed to accelerate aging in the vicinity of
the ROs, thereby making the impact of HTs more noticeable and easier to detect. The

**186** Advances in Hardware Design for Security and Trust

**Figure 8.8** (a) LSTM training and validation loss on all Trojan-free data for seventh
RO; (b) LSTM prediction for Trojan data for seventh RO [21].

data collected from the FPGA was processed using a Linux-based system, with an
ATMEGA2560 microcontroller enabling the transfer of raw data to the computer.

**8.5.3.3** **Aging Prediction Process**

The aging prediction process in this research involves the use of a long short-term
memory (LSTM) neural network, a type of ML model well suited for analyzing
time-series data. The LSTM network was trained to predict the expected frequency
degradation of the ROs over time, which represents the normal aging process of the
IC. When HTs were activated, the RO frequencies decreased more rapidly than predicted by the model, indicating accelerated aging and, by extension, the presence of
a Trojan or other degradation mechanisms. The LSTM model consisted of a bidirectional LSTM layer with 128 units, followed by a single output neuron. Training and
validation of the model were conducted on different segments of the RO frequency
data, collected both in the presence and absence of HTs.

Figure 8.8(a) illustrates the training and validation loss curves for the LSTM neural network, trained on Trojan-free data from the seventh RO. The figure shows how
the model’s prediction error decreases over successive epochs, stabilizing as it learns
the normal aging behavior of the RO. Figure 8.8(b) compares the LSTM model’s
predictions with actual frequency data from the seventh RO during Trojan-active
conditions. Initially, the model’s predictions closely match the observed data when
no Trojans are present. However, as HTs are activated, the frequency data deviates
from the model’s predictions indicating accelerated aging. This shift in RO frequency
indicates the model’s ability to detect HTs by identifying unexpected changes in aging patterns. Similar results were observed for all the other ROs spread across the
FPGA die.

The experimental results demonstrated that the LSTM model could effectively
predict normal aging trends and detect deviations caused by HTs. When applied to
a new FPGA, the model’s predictions closely matched the observed data during normal operation. However, the model’s prediction errors increased significantly when
HTs were activated, signaling the accelerated aging of the IC. Similar results were
obtained when the experiment was conducted on an aged FPGA, which shows its
potential for real-time applications.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **187**

**Figure** **8.9** (a) On-chip EM sensor arrays for continuous reliability monitoring. (b)
On-chip antenna structure [19].

**8.5.4** **ON-CHIP ANTENNA APPROACHES FOR IC RELIABILITYMONITORING**

The development of on-chip antenna structures is a recent advancement in the continuous monitoring of ICs for monitoring reliability over time. On-chip antennas which
are integrated directly onto the IC, offer a promising solution for enabling real-time,
non-invasive monitoring of critical parameters such as aging, electromigration, and
overall circuit integrity. The antennas are designed to be embedded within the IC’s
back-end-of-line (BEOL) layers, allowing them to closely monitor the signals emanating from the underlying circuitry.

In this section, we discuss an on-chip antenna array framework for continuous
reliability monitoring of ICs [19]. The structure of the proposed EM sensor is illustrated in Figure 8.9(a). It consists of an array of antennas designed to measure the
EM radiation emitted by the CUT. By positioning the EM sensor directly above the
CUT, it is possible to capture EM traces across different frequencies during the circuit’s operation. As the underlying circuits or interconnects experience accelerated
aging or electromigration, noticeable changes in the EM frequency spectrum trends
can be observed. This characteristic can be utilized to detect and estimate the aging
and electromigration effects on the chip.

On-Chip Antenna Design: Figure 8.9(b) shows the antenna design used in the
framework. The proposed antenna design includes a loop antenna optimized for coupling with adjacent metal traces within the IC. The loop antenna was modified to
operate at 1.5 GHz to target the clock frequency of the ICs, which is critical for
detecting any anomalies in the signal integrity caused by aging mechanisms such as
electromigration. A meander structure was added to the loop antenna design to lower
its resonant frequency and to improve its sensitivity to changes in the IC.

**8.5.4.1** **Electromigration Detection Using On-Chip Antennas:**

As electromigration occurs, it leads to the formation of voids in the interconnects
which can significantly impact the circuit’s performance. Electromigration can be
modeled as the formation of a semi-circular void in a copper conductor, where
the void’s diameter increases as the severity of electromigration increases [22]. As
the void grows, there is a proportional increase in resistance, which can affect the

**188** Advances in Hardware Design for Security and Trust

**Figure 8.10** On-chip EM sensor array fabrication process flow.

performance of the interconnect. An increase in resistance results in a decrease in
the current flowing through the interconnect. This reduction in current affects the
differential mode coupling between the on-chip antenna and the interconnect. A reduction in coupling signals abnormal activity within the IC, allowing the detection
of electromigration using on-chip antennas or EM sensors. This method provides a
novel way to monitor and detect electromigration as it progresses, helping to prevent
potential interconnect failure [23].

**8.5.4.2** **On-Chip Antenna Fabrication and BEOL Reliability Analysis:**

Fabrication Process of On-Chip Antenna Arrays

The on-chip antennas used for electromigration detection are fabricated through
a CMOS-compatible process to ensure they can be integrated into the BEOL layers
of the IC [24].

The fabrication process, as seen in Figure 8.10, starts with thermally oxidized p-Si
wafers as the base substrate. On these wafers, copper metal is deposited using physical vapor deposition (PVD) sputtering process. Once the copper layer is deposited,
the next step involves patterning the antenna arrays. Lithography processes, such as
photoresist coating, exposure, and development, are used to create the desired antenna patterns on the copper surface. Finally, the antennas are formed by etching
away the unnecessary copper metal, using wet-chemical etching and removing the
photoresist from the wafer.

**8.5.4.3** **On-Chip Antenna Testing and Characterization**

Once the on-chip antennas are fabricated, wafer-level characterization is performed
to evaluate their performance and reliability. This is typically done through Sparameter analysis, which helps in assessing performance metrics such as return
loss (-S11) and coupling efficiency (S12). Figure 8.11 shows the fabricated antenna
arrays and the wafer-level characterization setup. In this process, the antennas are
considered a two-port network, and ground-signal-ground (GSG) probes along with

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **189**

**Figure 8.11** (a) Processed antenna wafer. (b) VNA setup.

a vector network analyzer (VNA) are used to send power into the ports and measure
the transmitted or reflected power. Return loss measures how much power is reflected
back to the source, indicating how well the antenna matches the system. Based on
the results of the S-parameter analysis, adjustments to fabrication parameters, such
as metal thickness and the properties of the interlayer dielectric, can be made to meet
the necessary performance specifications.

**8.6** **USING ON-CHIP ANTENNAS FOR RELIABILITY MONITORING IN**
**2.5D/3D ICS**

Integrating on-chip antennas or EM sensors into 2.5D and 3D ICs involves embedding these sensors into various layers of the stacked dies, as shown in Figure 8.12.
These antennas can be strategically placed in the interconnect layers between the
dies to monitor the EM signals emitted by the circuits. Since 3D ICs involve longer

**Figure 8.12** Integrating on-chip EM sensors in advanced emerging 2.5D/3D ICs.

**190** Advances in Hardware Design for Security and Trust

and more complex interconnects, the antennas can be designed to be placed within
the BEOL layers to monitor signal integrity, aging, and electromigration in real time.

These antennas can potentially be used to detect changes in the EM spectrum as
circuits age or experience electromigration, allowing continuous monitoring of the
IC and improve reliability.

**8.6.1** **READ-OUT CIRCUITRY FOR PROCESSING RELIABILITY DATA**

Once the on-chip antennas capture the EM signals related to aging and electromigration, the next step is to process this data on-chip. The signals picked up by the
antennas need to be decoded, amplified, filtered, and analyzed to extract meaningful reliability information. To enable this, circuits to read the EM signals from the
antenna need to be developed.

The read-out circuitry typically consists of components from an RF receiver frontend. Row and column decoders are used to select specific antennas for analysis. They
can be used as selectors to focus on areas that may require closer inspection in 3D
ICs. Amplifiers are then used to amplify the signals received from the antennas. Mixers are used to extract specific frequency components and filters are used to remove
unwanted noise or interference from the amplified and mixed signals.

The integration of on-chip antennas in 2.5D and 3D ICs can be an effective
method for real-time monitoring reliability. By embedding antennas within the interconnect layers, reliability data across multiple levels of the IC stack can be collected.
The read-out circuitry consisting of decoders, amplifiers, mixers, and filters can be
designed to process the data for improved reliability monitoring of ICs.

**8.7** **CONCLUSION**

As IC technology advances with the development of 2.5D and 3D advanced packaging, ensuring the reliability and integrity of these complex circuits has become more
challenging. In this chapter, we explored how ICs are affected by factors like aging,
electromigration, and hardware Trojans. The chapter introduced various new reliability monitoring techniques, including the use of emerging devices, on-chip sensors
and electromagnetic monitoring methods. These approaches enable effective monitoring of IC’s reliability, providing valuable information about its performance and
early signs of failure. On-chip antennas, integrated directly into the IC, can be potentially used for detecting issues like aging and electromigration without disrupting
the IC’s operation.

In the future, these techniques will become increasingly important as IC designs
continue to grow more complex. Future research could focus on designing efficient,
low-power read-out circuitry to process data directly on the chip, minimizing power
consumption and improving integration. Additionally, novel tunable on-chip antennas could be developed to target a wider range of operating frequencies, enhancing
the detection of aging and reliability issues across different IC designs. These advancements would improve the ability to monitor the performance and reliability of
ICs in real time, ensuring longer operational lifetime and higher reliability.

On-Chip Integrity, Reliability, and Aging Assurance Techniques for ICs **191**

**REFERENCES**

1. W. Hu, C.-H. Chang, A. Sengupta, S. Bhunia, R. Kastner, and H. Li, “An Overview
of Hardware Security and Trust: Threats, Countermeasures, and Design Tools,” IEEE
Trans. Comput. Des. Integr. Circuits Syst., vol. 40, no. 6, pp. 1010–1038, 2021, doi:
[10.1109/TCAD.2020.3047976.](https://doi.org/10.1109/TCAD.2020.3047976)
2. J. R. Black, “Electromigration—A brief survey and some recent results,” IEEE Trans.
[Electron Devices, vol. 16, no. 4, pp. 338–347, 1969, doi: 10.1109/T-ED.1969.16754.](https://doi.org/10.1109/T-ED.1969.16754)
3. A. Amouri, F. Bruguier, S. Kiamehr, P. Benoit, L. Torres, and M. Tahoori, “Aging effects in FPGAs: An experimental analysis,” in Conference Digest    - 24th International
Conference on Field Programmable Logic and Applications, FPL 2014, 2014, doi:
[10.1109/FPL.2014.6927390.](https://doi.org/10.1109/FPL.2014.6927390)
4. M. M. Ahmed et al., “Towards a robust and efficient em based authentication of FPGA
against counterfeiting and recycling,” 2017 19th Int. Symp. Comput. Archit. Digit. Syst.
[CADS 2017, vol. 2018, pp. 1–6, 2017, doi: 10.1109/CADS.2017.8310673.](https://doi.org/10.1109/CADS.2017.8310673)
5. F. Bruguier, P. Benoit, P. Maurine, and L. Torres, “A New Process Characterization
Method for FPGAs Based on Electromagnetic Analysis,” in 2011 21st International
Conference on Field Programmable Logic and Applications, 2011, pp. 20–23, doi:
[10.1109/FPL.2011.15.](https://doi.org/10.1109/FPL.2011.15)
6. M. Vald´es et al., “Programmable sensor for on-line checking of signal integrity in
FPGA-based systems subject to aging effects,” in 2011 12th Latin American Test Work[shop (LATW), 2011, pp. 1–7, doi: 10.1109/LATW.2011.5985926.](https://doi.org/10.1109/LATW.2011.5985926)
7. M. D. Valdes-Pe˜na et al., “Design and Validation of Configurable Online Aging Sensors in Nanometer-Scale FPGAs,” IEEE Trans. Nanotechnol., vol. 12, no. 4, 2013, doi:
[10.1109/TNANO.2013.2253795.](https://doi.org/10.1109/TNANO.2013.2253795)
8. T. Schultz, R. Jha, B. Dupaix, and M. Casto, “ARIA: Additive ReRAM-based Integrity and Aging Monitoring for ICs,” IEEE Access, p. 1, 2019, doi: [10.1109/AC-](https://doi.org/10.1109/ACCESS.2019.2951661)
[CESS.2019.2951661.](https://doi.org/10.1109/ACCESS.2019.2951661)
9. G. Muha, J. Mayersky, and R. Jha, “Low-Overhead In-Situ Aging Monitors Using a
Reconfigurable FeFET for Trusted Hardware,” Proc. IEEE Natl. Aerosp. Electron. Conf.
[NAECON, vol. 2021, pp. 239–242, 2021, doi: 10.1109/NAECON49338.2021.9696415.](https://doi.org/10.1109/NAECON49338.2021.9696415)
10. J. He, H. Ma, Y. Liu, and Y. Zhao, “Golden Chip-Free Trojan Detection Leveraging
Trojan Trigger s Side-Channel Fingerprinting,” ACM Trans. Embed. Comput. Syst., vol.
[20, no. 1, pp. 1–18, 2021, doi: 10.1145/3419105.](https://doi.org/10.1145/3419105)
11. A. Stern, U. Botero, B. Shakya, H. Shen, D. Forte, and M. Tehranipoor, “EMFORCED:
EM-based Fingerprinting Framework for Counterfeit Detection with Demonstration on
Remarked and Cloned ICs,” in 2018 IEEE International Test Conference (ITC), 2018,
[vol. 2018, pp. 1–9, doi: 10.1109/TEST.2018.8624679.](https://doi.org/10.1109/TEST.2018.8624679)
12. O. S¨oll, T. Korak, M. Muehlberghuber, and M. Hutter, “EM-based detection of hardware
trojans on FPGAs,” Proc. 2014 IEEE Int. Symp. Hardware-Oriented Secur. Trust. HOST
[2014, pp. 84–87, 2014, doi: 10.1109/HST.2014.6855574.](https://doi.org/10.1109/HST.2014.6855574)
13. J. Balasch, B. Gierlichs, and I. Verbauwhede, “Electromagnetic circuit fingerprints for
Hardware Trojan detection,” IEEE Int. Symp. Electromagn. Compat., vol. 2015-Septm,
[pp. 246–251, 2015, doi: 10.1109/ISEMC.2015.7256167.](https://doi.org/10.1109/ISEMC.2015.7256167)
14. S. Adibelli, P. Juyal, L. N. Nguyen, M. Prvulovic, and A. Zajic, “Near-Field
Backscattering-Based Sensing for Hardware Trojan Detection,” IEEE Trans. Antennas
[Propag., vol. 68, no. 12, pp. 8082–8090, 2020, doi: 10.1109/TAP.2020.3000562.](https://doi.org/10.1109/TAP.2020.3000562)
15. H. Huang, A. Boyer, and S. Ben Dhia, “The detection of counterfeit integrated circuit
by the use of electromagnetic fingerprint,” IEEE Int. Symp. Electromagn. Compat., pp.
[1118–1122, 2014, doi: 10.1109/EMCEurope.2014.6931070.](https://doi.org/10.1109/EMCEurope.2014.6931070)

**192** Advances in Hardware Design for Security and Trust

16. H. xin Zhang, J. Liu, J. Xu, F. Zhang, X. tong Cui, and S. fei Sun, “Electromagnetic
radiation-based IC device identification and verification using deep learning,” Eurasip
[J. Wirel. Commun. Netw., vol. 2020, no. 1, 2020, doi: 10.1186/s13638-020-01808-z.](https://doi.org/10.1186/s13638-020-01808-z)
17. J. He, X. Guo, H. Ma, Y. Liu, Y. Zhao, and Y. Jin, “Runtime trust evaluation and hardware trojan detection using on-chip em sensors,” Proc. - Des. Autom. Conf., vol. 2020[July, pp. 0–5, 2020, doi: 10.1109/DAC18072.2020.9218514.](https://doi.org/10.1109/DAC18072.2020.9218514)
18. E. Chen, J. Kan, B.-Y. Yang, J. Zhu, and V. Chen, “Intelligent electromagnetic
sensors for non-invasive trojan detection,” Sensors, vol. 21, p. 8288, 2021, doi:
[https://doi.org/10.3390/s21248288.](https://doi.org/10.3390/s21248288)
19. M. Y. Vutukuru, A. Muha, and R. Jha, “On-Chip EM Sensor Arrays for Reliability Monitoring of Integrated Circuits,” Proc. IEEE Natl. Aerosp. Electron. Conf. NAECON, pp.
[157–162, 2023, doi: 10.1109/NAECON58068.2023.10366049.](https://doi.org/10.1109/NAECON58068.2023.10366049)
20. R. Dewey and R. Jha, “RRAM Devices for Hardware Integrity and Age Monitoring,” Proc. IEEE Natl. Aerosp. Electron. Conf. NAECON, pp. 163–167, 2023, doi:
[10.1109/NAECON58068.2023.10365728.](https://doi.org/10.1109/NAECON58068.2023.10365728)
21. K. Arvin and R. Jha, “Aging Prediction of Integrated Circuits Using Ring Oscillators
and Machine Learning,” Proc. 2021 IEEE Int. Conf. Phys. Assur. Insp. Electron. PAINE
[2021, 2021, doi: 10.1109/PAINE54418.2021.9707703.](https://doi.org/10.1109/PAINE54418.2021.9707703)
22. H. Ceric, S. Selberherr, H. Zahedmanesh, R. L. de Orio, and K. Croes,
“Review—Modeling Methods for Analysis of Electromigration Degradation in NanoInterconnects,” ECS J. Solid State Sci. Technol., vol. 10, no. 3, p. 035003, 2021, doi:
[10.1149/2162-8777/abe7a9.](https://doi.org/10.1149/2162-8777/abe7a9)
23. A. Muha, M. Y. Vutukuru, V. K. Gogi, and R. Jha, “On-Chip Antennas for IC Reliability and Aging Monitoring,” in 2024 IEEE 67th International Midwest Symposium on Circuits and Systems (MWSCAS), 2024, pp. 1276–1280, doi: [10.1109/MWS-](https://doi.org/10.1109/MWSCAS60917.2024.10658847)
[CAS60917.2024.10658847.](https://doi.org/10.1109/MWSCAS60917.2024.10658847)
24. M. Y. Vutukuru, A. Muha, R. Srinivasan, and R. Jha, “Impact of CMOS BEOL
and Heterogenous Packaging Process Conditions on the Performance of On-Chip
Antenna Arrays for EM Radiation Monitoring,” in NAECON 2024   - IEEE National Aerospace and Electronics Conference, 2024, pp. 297–300, doi: [10.1109/NAE-](https://doi.org/10.1109/NAECON61878.2024.10670674)
[CON61878.2024.10670674.](https://doi.org/10.1109/NAECON61878.2024.10670674)

# 9 Deep Learning
### Side-Channel Attacks: Challenges and Opportunities

Logan Reichling, Mabon Ninan, Boyang Wang,
and John M. Emmert

**9.1** **INTRODUCTION**

Side-channel attacks (SCAs) [1–3] can reveal encryption keys on a target device,
e.g., a microcontroller or Field Programmable Gate Array, despite the fact that an
encryption algorithm is mathematically secure. The attacks examine correlations between power consumption and intermediate outputs of an encryption algorithm, such
as advanced encryption standard (AES), over a large amount of traces captured from
a device. After intermediate outputs are revealed, the encryption key can be further
inferred by known plaintexts/ciphertexts and the encryption algorithm. Once an encryption key is compromised, the communication and data associated with a device
are no longer secure. It is one of the most fundamental threats to the security and
trust of hardware and embedded systems.

Since the seminal work by Kocher et al. in 1999, traditional side-channel attacks,
including Simple Power Analysis (SPA) [4], Differential Power Analysis (DPA) [5],
Correlation Power Analysis (CPA) [3], and Template Attacks [2], have been extensively investigated. To mitigate side-channel leakage and enhance the security of
encryption algorithms, two types of countermeasures, masking and blinding, can be
applied. Masking introduces masks, i.e., random values, in the implementation of encryption to hide correlations between power consumption and intermediate results,
which mitigates side-channel leakage without affecting the correctness of an encryption algorithm. For instance, a mask can be applied with two exclusive-or operations, one before and one after a leakage function, respectively, to hide side leakage
but maintain the correctness of the encryption. Blinding randomly shuffles the order
of operations or randomly delays operations in the implementation of encryption to
desynchronize the samples of the same operations across traces.

[DOI: 10.1201/9781003510949-9](https://doi.org/10.1201/9781003510949-9) **193**

**194** Advances in Hardware Design for Security and Trust

Recently, the research community has shown that deep learning side-channel attacks can offer advantages, such as defeating countermeasures and requiring less preprocessing, over traditional side-channel attacks. Maghrebi et al. [6] published the
first work evaluating deep neural networks for side-channel attacks against protected
and unprotected implementations of AES in 2016. Specifically, the authors investigated multiple neural networks, including Multi-Layer Perceptrons, Convolutional
Neural Networks, Autoencoders, Recurrent Neural Networks, and Long Short-Term
Memory, and compare their attack performance with template attacks. As reported in
a survey paper by Picek et al. [6], over 180 papers focusing on deep learning–based
side-channel attacks had been published as of 2023.

Despite the substantial progress in deep learning side-channel attacks, there are
still many challenges and opportunities. In this chapter, we introduce the typical
workflow of deep learning side-channel attacks with concrete examples to help researchers, especially the ones who are new to side-channel attacks, to enhance their
understanding and knowledge in this research area. Moreover, we highlight several
emerging aspects in deep learning side-channel attacks, including (1) new data sets,
(2) new architectures, (3) architecture optimization, (4) portability, (5) explainability, (6) non-profiling attacks, and (7) pre-silicon side-channel analyses, and discuss
open research opportunities associated with these aspects.

The rest of this chapter is organized as follows. In Section 9.2, we introduce the
system model and basic notations of side-channel attacks. In Section 9.3, we illustrate the workflow of deep learning side-channel attacks, from establishing a trace
acquisition setup to obtaining attack results, with examples over power traces collected from ARM STM32F3 (a 32-bit microcontroller) running AES-128. In Section
9.4, we discuss existing works and highlight open research opportunities. Finally, we
conclude this chapter in Section 9.5.

**9.2** **BACKGROUND ON SIDE-CHANNEL ATTACKS**

Depending the assumptions on an attacker, side-channel attacks consists of two categories, including profiling attacks and non-profiling attacks. We primarily discuss
profiling side-channel attacks in this chapter.

System Model. The system model of a profiling side-channel attack involves two
devices: the profiling device and the target device. We assume that an attacker has
complete control over the profiling device, e.g., a microcontroller or FPGA. Specifically, the attacker controls the plaintexts and associated key on the profiling device
and can capture an unlimited number of power or electromagnetic (EM) traces to
train a profile (i.e., a classifier). This attacker can passively capture the power consumption or EM radiation and plaintexts on the test device. By leveraging the profile,
the attacker aims to reveal an unknown but fixed key on the test device.

A profiling side-channel attack includes two phases, the training phase (or profiling phase) and the test phase (or attack phase). In the profiling phase, the attacker
trains a profile with labeled traces from the training device. Labels of traces are
intermediate results of encryption (or the Hamming weights of these intermediate
results), which are derived based on the known key and plaintexts. In the attack

Deep Learning Side-Channel Attacks: Challenges and Opportunities **195**

phase, the attacker captures traces and plaintexts from the test device and aims to
reveal the unknown key on the test device by leveraging the profile. In deep learning
side-channel attacks, a profile is a trained neural network.

For a non-profiling attack, an attacker does not have access to a profiling device to
build a profile in advance. Instead, it only has unlabeled traces from the test device
to perform the attack. As a result, it only consists of one phase, i.e., the attack phase,
which aims to distinguish the correct key from incorrect candidates. For instance, a
deep learning non-profiling attack can train 256 neural networks over the same set of
traces to identify the correct key.

Notations. A power trace t is one-dimensional time series data represented as
a vector t = (t[1],...,t[l]), where t[i] is the measurement of power consumption at
timestamp i and l is the total number of measured samples. We use M and K to
denote the plaintext space and the key space, respectively. Samples within a trace t
are recorded as a device runs encryption with plaintext m and key k, where m ∈ M
and k ∈ K . Intermediate values of encryption are denoted as z = ϕ(m, k), where the
function ϕ(·) is a leakage step of the encryption algorithm.

AES-128. The description of side-channel attacks in this chapter focuses on AES128 encryption, where an encryption key has 128 bits (i.e., 16 bytes). The sidechannel attacks over AES are performed in a divide-and-conquer approach, where
one key byte is revealed each time. Following problem descriptions in the literature [7, 8], we can assume key k, plaintext m, or intermediate value z has one byte.
We use k1 <sup>∗,</sup> <sup>k</sup> 2 <sup>∗,....,</sup> <sup>k</sup> 256 <sup>∗</sup> <sup>to denote all the possible 256 key candidates.</sup>

Leakage Model. A leakage model will need to be selected to formulate sidechannel leakage and calculate the labels of traces in side-channel attacks. Two popular leakage models, including the Hamming Weight (HW) model and the Identity
(ID) model. The HW model assumes that there are correlations between the power
consumption of an intermediate value and the Hamming weight of this intermediate
value. The label of a trace t is HW(z) - the Hamming weight of the intermediate
value z = ϕ(m, k) given plaintext m and key k. There are nine possible Hamming
weights (or nine possible labels) over one byte. The ID model assumes that there are
correlations between the power consumption and the intermediate value itself. The
label of a trace is the intermediate value z, and there are 256 possible labels.

Evaluation Metrics. Given a trained profile and a trace, the test phase derives a
score for every possible label. Next, each score is assigned to corresponding key candidate(s) based on the label, an associated plaintext, and AES encryption algorithm.
Every key candidate’s scores across all the test traces are aggregated. Since there are
256 key candidates given one byte, 256 aggregated scores are derived and sorted in
a descending order.

Specifically, let us assume that an attacker can capture N <sup>′</sup> test traces T <sup>′</sup> =
(t1 <sup>′</sup> <sup>,...,t</sup> N <sup>′</sup> <sup>′</sup> <sup>) and their N′</sup> <sup>plaintexts M′</sup> <sup>= (m</sup> 1 <sup>′</sup> <sup>,...,</sup> <sup>m′</sup> N <sup>′</sup> <sup>) from a test device running un-</sup>

1 <sup>′</sup> <sup>,...,t</sup> N <sup>′</sup> <sup>′</sup> <sup>) and their N′</sup> <sup>plaintexts M′</sup> <sup>= (m</sup> 1 <sup>′</sup>

(t1 <sup>′</sup> <sup>,...,t</sup> N <sup>′</sup> <sup>′</sup> <sup>) and their N′</sup> <sup>plaintexts M′</sup> <sup>= (m</sup> 1 <sup>′</sup> <sup>,...,</sup> <sup>m′</sup> N <sup>′</sup> <sup>) from a test device running un-</sup>

known key k <sup>′</sup>, where m <sup>′</sup> i <sup>is</sup> <sup>associated</sup> <sup>with t</sup> i <sup>′.</sup> <sup>Assume</sup> <sup>the</sup> <sup>ID</sup> <sup>model</sup> <sup>is</sup> <sup>used</sup> <sup>as</sup> <sup>the</sup>

leakage model. Given a trace ti <sup>′, the trained neural network outputs a ID score vector</sup>

(si[0],..., si[255]), where si[ j] is the score for label byte value j (in decimal). Next,

<sup>′</sup> i <sup>is</sup> <sup>associated</sup> <sup>with t</sup> i <sup>′</sup>

**196** Advances in Hardware Design for Security and Trust

an attacker obtains a key score vector (ri[k1 <sup>∗],...,</sup> <sup>ri[k</sup> 256 <sup>∗</sup> <sup>]) by calculating</sup>

g <sup>∗] = si[</sup> <sup>j],</sup> if ϕ(m <sup>′</sup> i

ri[kg <sup>∗</sup>

<sup>′</sup> i <sup>,</sup> <sup>k</sup> g <sup>∗</sup>

g <sup>∗) ==</sup> <sup>j</sup> (9.1)

for 1 ≤ g ≤ 256, where ri[kg <sup>∗</sup>

g <sup>∗] is the score of possible key k</sup> g <sup>∗</sup>

g <sup>∗</sup> <sup>according to trace t</sup> i <sup>′</sup>

for 1 ≤ g ≤ 256, where ri[kg <sup>∗] is the score of possible key k</sup> g <sup>∗</sup> <sup>according to trace t</sup> i <sup>′</sup> <sup>and</sup>

plaintext m <sup>′</sup> . The aggregated key score vector (r[k1 <sup>∗],...,</sup> <sup>r[k</sup> 256 <sup>∗</sup> <sup>]) over N′ power traces</sup>

plaintext m <sup>′</sup> . The aggregated key score vector (r[k1 <sup>∗],...,</sup> <sup>r[k</sup> 256 <sup>∗</sup> <sup>]) over N′ power traces</sup>

are computed as

r[k <sup>∗</sup> j <sup>] =</sup>

N <sup>′</sup>
###### ∑

i=1

ri[k <sup>∗</sup> j <sup>],</sup> <sup>for 1 ≤</sup> <sup>j ≤</sup> <sup>256</sup> (9.2)

The aggregated key scores (r[k1 <sup>∗],...,</sup> <sup>r[k</sup> 256 <sup>∗</sup> <sup>])</sup> <sup>are</sup> <sup>further sorted</sup> <sup>in</sup> <sup>descending order</sup>

based on the scores.

We utilize key rank (or guessing entropy) and measurements to disclosure (MTD)
to measure the effectiveness of side-channel attacks [9, 10]. Key rank r, where r ∈

[1, 256], is the rank of the aggregated score of the correct key among all the 256 key
candidates given a certain number of test traces. For instance, a key rank of 1 given
200 test traces indicates that the correct key has the highest score and the attacker
can distinguish the key correctly within 200 test traces. MTD indicates the minimal
number of test traces that is needed for the key rank to converge to one, i.e., when it
is distinguishable from others. A lower MTD indicates the attack is more effective.

**9.3** **EXAMPLES OF DEEP LEARNING SIDE-CHANNEL ATTACKS**

The complete workflow of deep learning side-channel attacks includes the following
steps: (1) establishing a trace acquisition setup, (2) identifying points of interest, (3)
large-scale trace collection, (4) statistical analysis, (5) deep learning model training,
and (6) reporting attack results.

In the following section, we present the workflow of deep learning side-channel
attacks over power traces from the ARM STM32F3 microcontroller running unmasked AES-128 as an example. ARM STM32F3 is a 32-bit microcontroller, which
is widely used on embedded devices. We utilize TinyAES, a C implementation of
unmasked AES-128 that is customized for embedded systems with low memory
usage. The power traces are collected using ChipWhisperer [11]. In addition, we
demonstrate the advantages of deep learning side-channel attacks over traditional
side-channel attacks given countermeasures (e.g., random delays). Understanding
these examples will help readers enhance their capabilities on performing and troubleshooting the evaluations of deep learning side-channel attacks over various targets
and data sets in practice. Examples of source code that can be used for statistical analysis, deep learning model training, and reporting attack results can be found [12,13].

**9.3.1** **TRACE ACQUISITION SETUP**

The first step of side-channel attacks is to establish a trace acquisition setup, which
can collect traces from a target running an encryption algorithm. There are no differences between traditional side-channel attacks and deep learning side-channel

Deep Learning Side-Channel Attacks: Challenges and Opportunities **197**

attacks in terms of a trace acquisition setup. We briefly describe a typical trace acquisition setup for power and EM traces in this section for completeness.

Power Trace Acquisition. A common power trace acquisition setup requires
components including (1) a target, e.g., microcontroller or FPGA; (2) an implementation of an encryption algorithm, e.g., a C implementation of AES-128; (3) an oscilloscope (with a high sampling rate); and (4) a computer (with large memory). During
data collection, the implementation of an encryption algorithm is first compiled on
the computer. Next, the compiled program, e.g., a binary, is loaded to the target with
the help of the computer. To collect a trace, the computer passes a plaintext and a
key to the target such that the target will perform one execution of the encryption.
During this process, the oscilloscope captures a trace and passes it to the computer.
The computer saves this trace and its associated plaintext and key.

Ideally, the entire trace, i.e., the samples from one entire execution of the encryption algorithm, is kept. However, due to storage limitation for the later large-scale
data collection, one can opt to save a small portion of the samples from the entire
execution. This requires identifying the leakage step to ensure the samples from the
leakage step are included. We will discuss more details regarding this aspect in the
next subsection. The sampling rate typically should be at least three or four times
higher than the clock rate of the target in order to capture samples associated with
the executions of the leakage step. Typically, an additional trigger signal is provided
to automatically record the start of each encryption execution, which can align traces
across multiple executions easily.

Establishing a trace acquisition setup is one of the key challenges for side-channel
attacks as it often requires comprehensive engineering experience and extensive
hand-on skills. This could be a major barrier, especially for new researchers to this
area. Fortunately, thanks to the efforts of the research and industry community in
the past decade, there are tools available that can ease the process. For instance,
ChipWhisperer is an open-source, affordable, and easy-to-use toolset that can collect
traces from microcontrollers and FPGAs for side-channel attacks. It is very popular
among the research and industry community. More information regarding ChipWhisperer hardware, its API, and tutorials can be found at [11].

EM Trace Acquisition. Built upon a power trace acquisition setup, a typical EM
trace acquisition setup requires additional components, including (5) an EM probe,
(6) an amplifier, (7) a probe holder, and (8) circuit board clamps. Specifically, an EM
probe is positioned over the top of a target to collect EM signals while the target
runs the encryption algorithm. Ideally, the probe should be very close to the target,
e.g., 2 mm, but does not physically touch it. The EM signals are then passed to
the amplifier to reduce noise. Next, the amplifier passes the filtered signals to the
computer. The probe holder and circuit board clamps help fix the position of the
probe and the target to minimize noise during EM trace acquisition. Once connected,
the steps for collecting a trace are almost identical to the ones from power trace
acquisition. Examples of a power trace acquisition and an EM trace acquisition using
ChipWhisperer are illustrated in Figure 9.1.

Even given the tiny surface of a target, e.g., 8 mm × 8 mm. The location of the
probe can be critical for high-quality EM traces, i.e., traces with high signal-to-noise

**198** Advances in Hardware Design for Security and Trust

**Figure 9.1** A power trace acquisition setup (left) and an EM trace acquisition setup
(right) using ChipWhisperer.

ratio. In general, a probe location that is closer to the data bus and ALU (Arithmetic
Logic Unit) can result in EM traces with higher signal-to-noise ratio. Multiple probe
locations can be scanned and compared to decide which probe location is the best
option before conducting a large-scale trace collection.

**9.3.2** **IDENTIFYING POINTS OF INTEREST**

Before collecting traces on a large scale, it is critical to identify points of interest,
the samples associated with the leakage step (as well as the ones associated with
countermeasures; e.g., masking) given a target, an encryption algorithm, and its software/hardware implementation. Identifying points of interest before large-scale trace
collection will allow us to keep a small portion of the samples from the entire execution, which can significantly save the storage for traces and downstream analyses.
This is particularly important for microcontrollers due to the large number of samples from one execution of AES. For instance, one execution of TinyAES running
on ARM STM32F3 can lead to around 50,000 samples given a sampling rate of 28
MHz (about four times of the clock rate of the microcontroller) using ChipWhisperer. Keeping all the 50,000 samples per trace requires large storage overheads and
it is not necessary. For masked AES implementation on microcontrollers, the number of samples per AES execution is much greater and a higher sampling rate is
also preferred, and therefore, identifying points of interest is certainly needed before
large-scale trace collections. Even when the storage overhead is not an issue and an
entire trace from a microcontroller can be kept, identifying points of interest in advance will allow us to provide a reasonable size of samples as an input to a neural
network, rather than passing an entire trace in the later training step.

On the other hand, for FPGAs, keeping all the samples from one execution of
AES does not lead to significant storage overheads and it is fine to collect a large
number of traces without specifically identifying points of interest in advance. In
other words, all the samples from one AES execution are considered as points of
interest. For instance, there are less than 150 samples for one execution of unmasked

Deep Learning Side-Channel Attacks: Challenges and Opportunities **199**

**Figure** **9.2** A comparison of two power traces from ARM STM32F3 running
TinyAES with ChipWhisperer. The left one is a power trace collected from the original C code and the right one is a power trace collected from the modified C code
(25 NOP operations added before and after SubBytes function, respectively). The C
code was compiled with gcc 9.2.1 and O0 optimization.

AES when collecting a power trace from a FPGA target using ChipWhisperer given
a sampling rate of 96 MHz.

For AES-128, most of the existing studies consider the first round of SubBytes as
the leakage step. There are two main reasons: (1) the side-channel leakage is high as
SubBytes is a non-linear function; (2) it is easier to derive the encryption key in the
analyses as the round key used in the first round of AES-128 is exactly the same as
the encryption key.

One effective approach for identifying points of interest is to add a certain number
of consecutive no operations (NOPs) instructions, e.g., 20∼30 NOPs, before and
after the leakage function in the source code (C or assembly), and then compare
the power trace of this modified code with the power trace of the original code. An
example of the comparison of power traces is presented in Figure 9.2. As we select
the first round of SubBytes as the leakage step, the inserted NOPs cause noticeable
gaps before and after the first round of SubBytes. These gaps offer indications of the
start and end timestamps of SubBytes in the power trace of the original code. In this
particular example shown in Figure 9.2, points of interest are set as (1,200, 2,200),
which covers all the samples associated with the first round of SubBytes.

Note that the selections of the start and end of points of interest are relatively loose
in this example, and can be further optimized if one prefers. In addition, we highly
recommend to keep the version of the compiler and optimization level consistent
between the original code and modified code as different software settings can lead
to different sets of machine instructions, and therefore, unexpected shifts in terms of
points of interest, as shown in a recent study [14].

**9.3.3** **LARGE-SCALE TRACE COLLECTION**

Once the first two steps are completed, the next step is to collect a large number of
traces. Specifically, by leveraging the trace acquisition setup, the computer passes
a number of N plaintexts and a key to the target such that the target will execute
the encryption N times. The oscilloscope captures N traces, one for each plaintext,

**200** Advances in Hardware Design for Security and Trust

and passes these traces to the computer. In addition, the computer also saves the N
plaintexts and the key. Finally, a data set consisting of N traces, N plaintexts, and a
key is assembled. In other words, the data set can be presented as a set of N tuples,
in which each tuple is in the form of (trace, plaintext, key). This concludes
the large-scale trace collection.

In this example, we collect a data set of N = 50, 000 power traces, plaintexts,
and a key by running STM32F3 using ChipWhisperer. We denote this data set as
S1 K1 50k. In addition, we also generate a data set by randomly delaying samples
in each trace with a number of d samples, where d is uniformly selected from (0,
50). This is a common approach to simulate traces with random delays. We denote
this data set as S1 K1 50k RD50.

Note that a data set can contain traces from multiple keys as long as a trace, a
plaintext, and a key are stored accordingly. One can also keep ciphertexts instead
of plaintexts (or even keep both ciphertexts and plaintexts) in a data set. There are
no specific advantages between keeping plaintexts and ciphertexts as long as it is
sufficient to generate a label, i.e., an intermediate result of an encryption, given a key
and a plaintext (or ciphertext).

Ideally, we should collect traces from two targets, e.g., two ARM STM32F3 microcontrollers with two different keys, where one target serves as the training device
and the other serves as the target device. This is critical, especially when we would
like to consider the domain shifts between training and test traces. For ease of presentation, we assume that both training and test traces are from the same device in
this example.

**9.3.4** **STATISTICAL ANALYSES**

Given a data set, we highly recommend performing statistical analyses before training a neural network. Specifically, the results of statistical analyses can validate at
which timestamps side-channel leakage happen and to what degree leakage may
present. Examining the results of statistical analyses enhances the explainability of
the entire process and minimizes the cases of blindly training a neural network as
a black-box process without understanding the root cause of side-channel leakage.
Common statistical analyses include signal-to-noise ratio [9], TVLA (test vector
leakage assessment, also referred to as t-test) [15], and NICV (normalized inner-class
variance) [16]. The details of each method are different but share similar concepts,
i.e., indicating where and to what degree there is side-channel leakage, but does not
recover a key directly. Typically, performing one is sufficient. Same as side-channel
attacks, statistical analyses over AES are based on each key byte.

In Figure 9.3, we provide the results of TVLA and NICV given data set
S1 K1 50k, where we select the third key byte and all the 50,000 traces for analysis. As we can observe from Figure 9.3, TVLA shows that significant side-channel
leakage associated with the third key byte (in essence, the third byte of the output of
the first round of SubBytes) can be observed around timestamp 1,675. In TVLA, a
value higher than 4.5 indicates that a key byte can likely be recovered. Similarly, we
also observe high NICV values at the same timestamp around 1,675 given the results

Deep Learning Side-Channel Attacks: Challenges and Opportunities **201**

**Figure** **9.3** Results of statistical analysis (left: TVLA, right: NICV) over data set
S1 K1 50k based on the third key byte, where distinguishable high values suggest
high side-channel leakage.

**Figure** **9.4** Results of statistical analysis (left: TVLA, right: NICV) over data set
S1 K1 50k RD50 based on the third key byte, where distinguishable high values
are no longer available due to random delays.

from the same byte. We can also further expand the analyses on all the 16 key bytes.
For instance, we aggregate the results of NICV over S1 K1 50k across all 16 bytes
in Figure 9.5. This also offers another opportunity to validate the selection of points
of interest covering all the samples associated with the first round of SubBytes.

Another example of statistical analyses over data set S1 K1 50k RD50 is presented in Figure 9.4. We still choose all the 50,000 power traces and the third key
byte for analysis. Due to random delays, samples from the third byte of the output of
the first round SubBytes do not happen at the same timestamps across all the traces,
which significantly minimizes the side-channel leakage. The TVLA values are lower
than 4.5 and the NICV values are almost zero. In other words, the values around
1,675, i.e., the values associated with the third key byte of the output of the first
round SubBytes, are not sufficiently distinguishable from the values of other timestamps. These results indicate that traditional side-channel attacks, such as correlation
power analyses or template attacks, will fail to recover keys over this data set.

**202** Advances in Hardware Design for Security and Trust

**Figure** **9.5** Results of NICV over data set S1 K1 50k across all the 16 key bytes,
where distinguishable high values suggest high side-channel leakage from every
byte.

**9.3.5** **TRAINING A NEURAL NETWORK**

With the steps described above, we are now ready to move on to the training of a
neural network for side-channel attacks. Given data set S1 K1 50k, we use 40,000
traces for training, 5,000 traces for validation, and 5,000 traces for testing. Based
on our experience for power traces from microcontrollers running unmasked AES,
typically it is sufficient to train a neural network with 10k∼50k training traces
such that the neural network can recover keys later in the attack phase. For more
challenging data sets, such as EM traces, FPGAs, or masked AES, a much greater
number of training traces (e.g., greater than 100k training traces) is suggested.

When performing the training, we pass each training trace (samples from points
of interest, only as shown in Figure 9.6) and its label to a neural network. The label
of each trace is calculated as the output of first round of SubBytes given a chosen
byte, where this output can be generated by the plaintext, key, and the encryption
algorithm. For instance, when we choose the third key byte as the byte we would
like to attack, then the label of a trace can be assigned as the third byte of the output
of the first round of SubBytes computed from the third key byte, the third plaintext
byte, and AES encryption algorithm.

Convolutional neural networks (CNNs) are commonly used for side-channel attacks and often derive promising results. We leverage a CNN used over the ASCAD
data set as an example. This CNN contains five convolutional blocks, two dense
layers, and one output layer. Each convolutional block consists of a convolutional
layer and an average pooling layer. Hyperparameters of this CNN can be found
in [17].

Deep Learning Side-Channel Attacks: Challenges and Opportunities **203**

**Figure** **9.6** 3D Representation of power trace fed to a CNN. Only samples from
points of interest are passed to the input layer. Layer legend: Yellow: Input, Pink:
Convolutional, Green: Average Pooling, Blue: Flatten, Purple: Dense.

To perform training, we need to choose several important parameters, including
points of interest, the number of training traces, leakage model, target byte, and the
number of training epochs. In this example, we choose (1,200, 2,200) as points of
interest, 40,000 as the number of training traces, identity (ID) model as the leakage
model, third key byte as the target byte, and 150 epochs. Through the training process, the neural network calculates the loss and update weights accordingly through
back-propagation to minimize the loss over training data. In other words, the training
process aims to train a neural network such that it can predict encryption intermediate
results, e.g., the output of first round SubBytes. An example of the loss changes during the training process is presented in Figure 9.7. The training in this example can
be completed with about 40∼60 minutes given a machine equipped with NVIDIA
GeForce RTX 4080 GPU.

Compared to machine learning in other domains, it is critical to keep in mind
that a well-trained neural network for side-channel attacks typically does not derive extremely high accuracy as the ones in other domains (e.g., over 95% accuracy
in image recognition). For instance, the training accuracy of a CNN trained from
data set S1 K1 50k only achieves an accuracy of around 4% given the ID model.
On the other hand, this accuracy is already way above the random guess of the ID
model (1/256 = 0.39%) and is sufficient to recover keys successfully. This difference,
in essence, is due to successfully recovering keys relying on the aggregated scores
across a certain number of traces rather than examining scores from each trace independently. It is worth mentioning that if a different leakage model is utilized, then
the expectation of the accuracy after training should be adjusted accordingly. For

**204** Advances in Hardware Design for Security and Trust

**Figure 9.7** Loss changes (left) and accuracy (right) during the training process of the
CNN given training traces from data set S1 K1 50k (ID model, third key byte, 150
epochs).

instance, if the HW model is used as the leakage model, then the accuracy of a neural network after the training should be sufficiently higher than the random guess of
the HW model (1/9 = 11.11%) in order to (potentially) recover keys correctly later
in the test phase. Our experience over various data sets shows that, typically, choosing the ID model would derive better results when training a profile with a neural
network, especially given challenging data sets, such as EM traces and traces from
FPGAs.

**9.3.6** **REPORTING ATTACK RESULTS**

Once the training is completed, we can perform the attack/test phase. Given a trained
neural network, we pass each test trace to the neural network, obtain a score for
each label among all the 256 possible labels, and assign each score to a candidate
key byte based on each label and the plaintext of this trace. This step is repeated
across all the test traces. The scores on each candidate key byte from all the test
traces are aggregated, and the aggregated scores of all the 256 candidate key bytes
are compared and ranked. It is also critical to keep in mind that two scores of a
label, e.g., 0×01, obtained from two test traces do not necessarily assign to the same
key candidate as the plaintexts of these two traces can be different. Assigning and
aggregating scores of labels to key candidates correctly is a unique but significant
step for side-channel attacks, which other machine learning applications typically
do not perform.

As mentioned, once obtaining the aggregated scores on all the candidate key
bytes, the results of side-channel attacks are reported with key rank and MTD in
the test phase. Specifically, given a number of N <sup>′</sup> test traces and a trained neural network, typically, the testing should perform multiple rounds, e.g., 20 rounds, where
the number of N <sup>′</sup> test traces are passed to the trained neural network in each round,
but the order of the test traces per each round is randomly shuffled. This is because
the order of test traces can affect the results of key rank and MTD, e.g., one specific
trace carries extremely high leakage and passing this trace to the trained neural network before others can lead to much lower MTD. This could be extremely important

Deep Learning Side-Channel Attacks: Challenges and Opportunities **205**

**Figure 9.8** Average key rank and MTD results from side-channel attacks on third key
byte (left, MTD = 4, deep learning; right, MTD=75, template attacks) given 5,000
test traces from data set S1 K1 50k with 20 rounds of testing.

for the evaluation of EM traces, where the variance of samples is higher across traces.
Calculating the average results of MTDs from multiple rounds is more accurate to
reflect the side-channel leakage. Running multiple rounds of testing is also a unique
step for side-channel attacks compared to machine learning in other domains.

An example of key rank and MTD from the third key byte is presented in Figure 9.8, where the neural network is trained and tested based on data set S1 K1 50k.
We can observe that the key rank decreases when the number of test traces increases
and it converges to one when the number of test traces is four. This suggests that an
attacker can reveal the third key byte correctly with four test traces given the welltrained CNN. To obtain results for other bytes, we can simply retrain a CNN with
each specific key byte and repeat the test phase accordingly. For comparison purpose,
we also provide the attack results over data set S1 K1 50k by using a template attack, where we use the same training traces and test traces. It is easy to see that
template attacks can also recover keys over this data set, but with a greater MTD. In
other words, both methods can recover keys, but deep learning side-channel attacks
offer better attack results in this case.

In addition to the attack results from data set S1 K1 50k, we also demonstrate
the attack results from dataset S1 K1 50k RD50 in Figure 9.9. We still use the
same number of training traces, test traces, and CNN architecture. We observe that
deep learning side-channel attacks can still effectively recover keys. On the other
hand, template attacks fail to recover keys due to random delays across all the traces.
This is a classic example where deep learning side-channel attacks can offer obvious
advantages over traditional attacks.

**9.4** **STATE OF THE ART, CHALLENGES, AND OPPORTUNITIES**

Deep learning side-channel attacks have been extensively studied in the past 10 years.
Comprehensive surveys can be found in [7, 8]. Rather than illustrating the details of
every existing study, we primarily discuss recent work related to several emerging

**206** Advances in Hardware Design for Security and Trust

**Figure** **9.9** Average key rank and MTD results from side-channel attacks on third
key byte (left, MTD=6, deep learning; right, attack is unsuccessful, template attacks)
given 5,000 test traces from data set S1 K1 50k RD50 with 20 rounds of testing.

aspects, including (1) new data sets, (2) new architectures, (3) architecture optimizations, (4) portability, (5) explainability, (6) non-profiling deep learning side-channel
attacks, and (7) pre-silicon side-channel analyses. We believe that these aspects bring
unique challenges and new opportunities for the research community.

**9.4.1** **NEW DATA SETS**

New data sets, especially data sets acquired from implementations with countermeasures, are critical for expanding research findings in deep learning side-channel attacks. The ASCAD data set released in [17] has been prominently used for benchmarking and comparison in the majority of recent studies. This data set consists
of two versions, referred to as ASCADv1 and ASCADv2, respectively. ASCADv1
consists of 100,000 power traces collected from an ATMEGA8515 (a 8-bit microcontroller) running a first-order Boolean masked AES-128 implementation. The microcontroller was running at 4 MHz. The traces were collected with a sampling
rate of 2 GHz and each trace contains 100,000 samples, where points of interest,
e.g., samples from the first round of SubBytes, are also suggested. ASCADv1 offers
traces from fixed keys and variable keys. Traces with random delays (simulated) are
also provided. The masked assembly implementation was also made publicly available for the research community [18]. The authors perform comprehensive analyses over this data set using multiple CNNs and MLPs, and demonstrate the advantages of deep learning side-channel attacks over this data set. The CNNs and MLPs
are also utilized in many subsequent studies in side-channel attacks over other data
sets.

Compared to ASCADv1, ASCADv2 is relatively new. It contains 800,000 power
traces collected from an ARM STM32F3 microcontroller running a third-order
masked AES-128 implementation using ChipWhisperer. This masked implementation offers two countermeasures, including affine masking and shuffling. The microcontroller was under-clocked to 4 MHz. The traces were collected with a sampling rate of 50 MHz and each trace contains 1 million samples. Like ASCADv1,

Deep Learning Side-Channel Attacks: Challenges and Opportunities **207**

suggested points of interest are provided, e.g., mask calculations and first-round
SubBytes; 800,000 random keys and plaintexts were utilized. The masked implementation was also made publicly available.

Other data sets, including AES RD [19], DPAcontestV4 [20], and CHES2020
CTF [21], have also been examined under deep learning side-channel attacks, but
are less popular than the ASCAD data set. Two recent studies release unique data
sets, referred to as SoftPower [14] and CrossEM [22], respectively, for the evaluation of portability of deep learning side-channel attacks. Both data sets were acquired using ChipWhisperer. SoftPower contains 3.2 million power traces from AVG
XMEGA and ARM STM32F3 microcontrollers running AES, where the binaries are
not always the same due to discrepancies in software settings, such as compiler optimization, instruction rewriting, and code obfuscation. CrossEM consists of 3 million
EM traces from AVG XMEGA and ARM STM32F3 microcontrollers running AES,
where EM traces were collected from multiple EM probe locations over the surface
of a microcontroller. Unfortunately, the traces from these two data sets are from unmasked AES only.

Opportunities. Continuing to release large-scale data sets of power traces, EM
traces, and even simulated traces at the Register Transfer Level (RTL) level, from
software and hardware implementation of encryption algorithms with countermeasures, will offer enormous opportunities for the research community to further understand the capabilities of deep learning side-channel attacks. In addition, detailed
documents and public repositories associated with new data sets will help improving
reproducibility of research and facilitating comparisons between existing and new
methods.

**9.4.2** **NEW ARCHITECTURES**

While the majority of existing studies focus on relatively common neural network architectures, such as CNNs, MLPs, and LSTM, several recent studies introduce more
comprehensive architectures, including Residual Networks (ResNets), Transformer
Networks, Generative Adversarial Networks (GANs), and Large Language Models
(LLMs), which demonstrate the strength of modern techniques in deep learning sidechannel attacks.

Masure et al. [23] introduced a new ResNet architecture, referred to as
ResNetSCA, which is customized for side-channel attacks. It contains 27 layers and
incorporates multi-task learning to perform side-channel attacks successfully over
the ASCADv2 data set. Multi-task learning is a deep learning technique which trains
a neural network to perform multiple associated tasks simultaneously to benefit the
learning of all the tasks. Specifically, the authors show that the ResNetSCA with
multi-task learning can predict all the 16 key bytes, 16 shuffling indices, and 2 masking bytes at the same time with an average of 60 test traces, where the POI of each
trace includes 15,000 samples. On the other hand, the authors demonstrate that CNNs
and MLPs fail to recover keys over this data set. A work in parallel by Wu et al. [24]
also utilized multi-task learning to predict the full AES-128 key simultaneously over
the ASCADv1 data set. The paper also demonstrates that better performance can be

**208** Advances in Hardware Design for Security and Trust

achieved by predicting each bit individually instead of using one-hot encoding over
the byte space.

Hajra et al. [25] designed EstraNet, a transformer-style architecture, for sidechannel attacks. It implements a customized modification of the self-attention architecture, which notably includes a linear-time complexity attention head kernel,
allowing for a much greater number of utilized points of interest. The study reports successful attacks with a point-of-interest length of 60,000, which is four times
greater compared to the one used in ResNetSCA. Furthermore, its custom attention
layer includes relative positional encoding parameters that are learned during training. This allows EstraNet to associate specific points in time during the encryption
operations with others, which is significant for tackling masking, e.g., calculations of
mask shares with intermediate values after SubBytes. The relative positional encoding scheme also allows the architecture to automatically overcome random delays.
The study presents low MTDs across several public data sets, including ASCADv1
and CHES2020, and outperform CNNs and LSTMs over traces with the point-ofinterest length ranging from 10,000 to 60,000.

Kulkarni et al. [26] demonstrated the potential of formulating side-channel attacks
as Natural Language Processing problems and addressed it with LLMs. Specifically,
the authors form an n-cryptogram consisting of a trace, a key byte, a SubBytes output, a plaintext, a ciphertext, and a mask value. They train a LLM to recognize and
later predict the difference between ordered and chaotic n-cryptograms. An ordered
n-cryptogram has the correct key byte guess for the associated trace, plaintext, ciphertext, and mask value. On the other hand, a chaotic n-cryptogram has the incorrect key byte guess. By leveraging a sigmoid classification, the proposed Order vs.
Chaos classifier predicts the probability that a n-cryptogram is ordered. Their evaluation shows that the proposed neural network can recover key bytes correctly within
one test trace over the ASCADv1 data set (fixed key) and 43 test traces over the ASCADv2 data set, respectively, which are better results than previous architectures.
Wang et al. [27] leveraged conditional Generative Adversarial Networks (cGANs)
to produce synthetic traces for training when there is a small number of traces
available.

Opportunities. One emerging question to answer related to this aspect is, given
a new data set (or target), when do we know a more comprehensive architecture is
needed rather than using a baseline architecture, e.g., a CNN. In addition, rather than
experimentally enumerating different comprehensive architectures, is there a way
for researchers to measure (or at least estimate) in advance which architecture will
likely succeed in recovering keys given a new data set?

**9.4.3** **ARCHITECTURE OPTIMIZATION**

Architecture optimization aims to find best hyperparameters and/or reduce the number of parameters in a neural network for side-channel attacks. Rijsdijk et al. [28]
leveraged reinforcement learning to perform neural network optimization using a
reward-based system. Their evaluations show that it is feasible to obtain a compressed CNN with only 1,282 trainable parameters but still reveal a key byte

Deep Learning Side-Channel Attacks: Challenges and Opportunities **209**

correctly with 242 traces given the ASCADv1 data set (fixed key). This is significantly compressed since the baseline CNN examined over the ASCADv1 data set
consists of over 53 million parameters. The main downside of this method is the long
search time due to the large architecture search space. Specifically, given one data
set, the study reports that it takes over 100 hours to search over 2,500 combinations
of hyperparameters to derive the smallest neural network. An adjacent work [29]
on hyperparameter selection for side-channel attacks utilizes multi-fidelity Bayesian
optimization and hyperband (BOHB) search. It bounds the maximum search space
with a budget parameter, where a greater budget size, i.e., a greater search space,
leads to more performant neural networks given a data set. Their experimental results indicate that the proposed approach is effective over multiple public data sets,
including ASCADv1, AES HD, and CHES2018. It also requires a long search time,
e.g., 2 days and 6 hours.

In addition to hyperparameter search, a couple of recent studies investigate neural
network compression using pruning. Pruning reduces the size of a neural network by
removing less important parameters, e.g., filters and weights. Perin et al. [30] were
the first to explore pruning for side-channel attacks, where they utilized unstructured
pruning, i.e., less important weights are set as zeros but not removed. Specifically,
the authors make use of the Lottery Ticket Hypothesis, which states that random initialization of weights often contain ideal sub-networks for classification. The experimental results show that it is feasible to reduce over 90% of parameters of a neural
network trained on the ASCADv1 data set. A more recent work in [31] investigate
structured pruning to reduce the size of neural networks for side-channel attacks. The
authors develop an automatic pruning algorithm, named MiniDrop, which can automatically decide the best pruning rate and remove less important filters at each layer.
The experimental results show that the proposed pruning is highly effective over
multiple data sets, including the ASCADv1 data sets, EM traces from STM32F3,
and power traces from Artix-7 FPGAs, and can achieve up to a 98% reduction rate.
In addition, the authors demonstrate their pruned neural networks can be operated on
a Raspberry Pi.

Opportunities. Being able to optimize neural networks for side-channel attacks
and having the capabilities to deploy the networks on embedded devices may facilitate the vision of continuous, local, and real-time analyses of side-channel leakage
and ensure embedded devices are monitored and secure through their lifetime.

**9.4.4** **PORTABILITY**

In deep learning side-channel attacks, a trained neural network is considered portable
when this network can still effectively recover keys given discrepancies (or domain
shifts) between training traces and test traces. Many existing studies [14,32–42] have
investigated the portability of side-channel attacks when there are domain shifts
between training and test data. Many factors, such as distinct keys, differences in
software settings, hardware manufacturing variances, inconsistent acquisition setups, and EM probe positions can lead to domain shifts between training and test
data in the context of side-channel attacks. Three common existing approaches to

**210** Advances in Hardware Design for Security and Trust

address domain shifts for side-channel attacks are (1) multi-domain training, (2) preprocessing, and (3) domain adaptation.

Bhasin et al. [38] investigate the portability of deep learning side-channel attacks
given discrepancies caused by keys and devices. The authors propose to train a neural
network with traces from multiple devices (in essence, multiple domain training)
to tackle domain shifts. Danial et al. [36] evaluated the portability of MLPs over
EM traces from distinct devices and different EM probe locations. Their findings
suggest that significant cross-device variations and inherent low SNR of EM traces
bring challenges to portability. The study also shows that pre-processing methods,
including Discrete Fourier Transform (DFT), Principle Component Analysis (PCA),
and Linear Discriminant Analysis (LDA), can overcome domain shifts.

Yu et al. [40] proposed to utilize meta-transfer learning to address domain shifts
caused by chip model variations. Similarly, Genevey-Metat et al. [41] leveraged finetuning to address domain shifts over EM traces and power traces from STM32 microcontrollers. However, both of the two methods require labeled traces from the test
device, which is impractical for real-world attackers. Knowing labels of test traces
before attacks indicates that an attacker knows the key byte already.

A recent study [14] examines domain shifts caused by software settings, which
have not been widely investigated in the literature. Specifically, the authors show that
multiple software factors, including compiler optimization levels, instruction rewriting, and code obfuscation, can lead to distinct binaries given the same AES implementation. Different binaries, in essence, different sets of machine instructions, lead
to domain shifts between training traces and test traces. While the study demonstrates
multi-domain training, training a neural network with traces from multiple software
settings can improve portability. The authors also mention that multi-domain training
is not scalable for a real-world attacker in this scenario as the number of potential
software settings is extremely large and difficult to enumerate in practice.

Opportunities. Despite the extensive discussions on portability, the domain shifts
are complicated and can be easily triggered by multiple factors in side-channel attacks. A recent study [22] indicates that none of the existing approaches can consistently outperform others given domain shifts caused by EM probe locations. It is
critical for the research community to further explore new methods that can better
address domain shifts in the context of side-channel attacks, especially when traces
are collected from implementations with countermeasures.

**9.4.5** **EXPLAINABILITY**

Since neural networks are often considered black-box approaches, the explainability
of deep learning side-channel attacks is fundamental to understanding the root cause
of the leakage. Hettwer et al. [43] explored multiple attribution-based methods for
enhancing the explainability of a CNN in the context of side-channel attacks. Specifically, each sample of a trace is sequentially set to zero to measure its effect on a
given output to determine which sample points matter the most. For instance, the
study reports the results of attribution analyses over the ASCADv1 data set by using
two methods: Saliency and Layer-wise Relevance Propagation. The results indicate

Deep Learning Side-Channel Attacks: Challenges and Opportunities **211**

that samples associated with the processing of mask values and the masked SubByte
operations are most critical to the output of a CNN.

Perin et al. [44] developed a new method, referred to as ExDL-SCA, based on information flow through multiple layers of a neural network, such as MLPs or CNNs,
in side-channel attacks. Specifically, internal hidden layer representations of a neural network are fed through a small, specialized MLP at each epoch to estimate the
perceived information index. In other words, this specialized MLP estimates to what
degree the labels (and masks) can be predicted using internal data. The inner-neural
outputs are training data. The original labels are outputs of this specialized MLP.
This method relies on the Information Bottleneck Theory; deeper layers carry more
compressed representations of correct output labels. Evaluations over the ASCADv1
and DPAcontest4.2 data set show that intermediate layers learn to separate less important features from features related to SubBytes output and masking values. In
addition, the study concludes that random delay is typically tackled in earlier layers
while masking is addressed in deeper layers.

Opportunities. Despite the findings on the explainability of MLPs and CNNs,
there are opportunities for the research community to investigate and enhance the
explainability of recent comprehensive architectures, such as ResNets [23] and transformers [25], in the context of side-channel attacks.

**9.4.6** **NON-PROFILING DEEP LEARNING SIDE-CHANNEL ATTACKS**

A recent work in [45] shows that it is feasible to perform non-profiling attacks with
deep neural networks. To recover one key byte of AES, the proposed method assigns
traces with guessed labels based on each possible key byte among the 256 candidates
and then trains 256 neural networks, where each neural network is trained based
on traces and guessed labels calculated from each possible key byte candidate. In
essence, it produces 256 partitions of traces based on all the 256 possible key byte
values. The distinguisher, either training accuracy or loss, is utilized to select the
correct key byte candidate from incorrect ones. In other words, training 256 neural
networks is the attack phase of this attack. The intuition is that the correct key byte
results in correct labels, and therefore, leads to better training results while incorrect
ones only lead to an accuracy similar to random guess. It is worth mentioning that
the Identity model cannot be used as the leakage model in this approach as the 256
partitions would be the same, and there would be no statistical difference across these
partitions, i.e., the distinguisher would fail to distinguish the correct key from others,
regardless how the distinguisher is selected.

Following the study in [45], several works [46–49] further examine non-profiling
deep learning side-channel attacks. Specifically, Kwon et al. [46] successfully attacked AES implementations with random delay and masking with a single unsupervised autoencoder, but utilized more training traces. Wu et al. [47] successfully
recovered a key byte by training a model to predict the differences in a trace given
plaintext collisions. Wu et al. [48] also proposed another method of determining
intermediary encryption information given the plaintext, ciphertext, and trace in a
non-profiling scenario. Savu et al. [49] leveraged multi-output regression models for

**212** Advances in Hardware Design for Security and Trust

side-channel attacks. It offers modest improvements on attack results, but is more
computationally efficient than previous methods.

Opportunities. One major challenge for deep learning non-profiling side-channel
attacks is the extremely long time needed to train 256 neural networks per key byte.
Fully recovering all the 16 key bytes of AES-128 requires training 256×16 neural
networks, which is even more time consuming. New methods are needed to optimize
the overall training time for non-profiling side-channel attacks. In addition, how to
perform non-profiling side-channel attacks with the recent complex neural network
architectures, such as such as ResNets [23] and transformers [25], remains unknown.

**9.4.7** **PRE-SILICON SIDE-CHANNEL ANALYSES**

There is an emerging trend to apply side-channel analyses at the pre-silicon phase,
e.g., the design stage at the Register Transfer Level (RTL). Pre-silicon side-channel
analyses can help identify the root cause of side leakage early during the design
stage and updating the design to mitigate leakage. This can save significant costs in
chip design. Typically, simulated power or EM traces of a hardware design of an
encryption, e.g., AES, can be generated at the RTL level or netlist level, then these
simulated traces can be leveraged to perform side-channel analyses.

The survey paper by Buhan et al. in [50] identified a range of current offerings for
pre-silicon side-channel analyses, including targeted devices/implementations, tools,
and capabilities. One major challenge is that a very limited number of existing tools
for pre-silicon side-channel analyses are hardware independent or open source. This
is mainly because the hardware design toolchains are complicated and vary across
different vendors and designers. For instance, an open-sourcetool, named TOFU, can
produce simulated power traces for pre-silicon side-channel analyses, where these
traces are produced based on Value-Change Dump (VCD) files generated by RTL
designs. Electromagnetic simulation for pre-silicon side-channel leakage detection
proves to be a challenging task. Sehatbakhsh et al. developed an EM emulator named
EMSIM [51], which utilizes the hardware design to generate an EM signal and an accompanying physical RISC-V processor as a reference point for signal comparison.
The emulator then replicates the analog EM signal by assigning scaling factors to the
different categories of potential instructions (ALU, memory storage, etc.) based on
recorded amplitudes from the companion RISC-V core. The study further reinforces
their simulation by showing similar TVLA results from a real EM trace compared
to the synthetic one. A later simulator created by Lin et al. in [52] aims to provide
locality-based simulation of EM leakage in addition to analog trace synthesis. A recent study [10] investigates transfer learning for enhancing post-silicon side-channel
attacks with simulated traces from the pre-silicon stage. Specifically, a neural network is initially trained with a large number of simulated traces and then fine-tuned
with a small number of traces from the post-silicon stage for side-channel attacks.

Opportunities. It remains largely unknown what advantages as well as disadvantages that deep learning can offer in the context of pre-silicon side-channel analyses
compared to traditional side-channel analyses, such as TVLA and CPA. It would
be interesting for the research community to investigate this aspect to enhance the

Deep Learning Side-Channel Attacks: Challenges and Opportunities **213**

implementation of countermeasures for encryption algorithms, such as AES and
post-quantum encryption algorithms, at the design stage.

**9.5** **CONCLUSION**

In this chapter, we illustrate the typical workflow of deep learning side-channel attacks and highlight the unique differences of deep learning between side-channel
attacks and other applications. In addition, we extensively discuss several emerging
aspects of deep learning side-channel attacks and underline multiple open research
opportunities. We hope that the content of this chapter provides a solid anchor point
for researchers, especially newer ones, to further investigate open problems in this
area and contribute new data sets, methods, tools, and insights to the research community.

**REFERENCES**

1. P. Kocher, J. Jaffe, and B. Jun. Differential Power Analysis. In Proceedings of
CRYPTO’99, 1999.
2. S. Chari, J. R. Rao, and P. Rohatgi. Template Attacks. In Proceedings of Cryptographic
Hardware and Embeeded Systems (CHES 2002), 2002.
3. E. Brier, C. Clavier, and F. Olivier. Correlation Power Analysis with a Leakage Model.
In Proceedings of CHES’04, 2004.
4. S. Chari, C. Jutla, J. Rao, and P. Rohatgi. Towards sound approaches to counteract
power-analysis attacks. In M. Wiener, editor, Advances in Cryptology — CRYPTO’ 99,
pages 398–412, Berlin, Heidelberg, 1999. Springer Berlin Heidelberg.
5. P. Kocher, J. Jaffe, B. Jun, and P. Rohatgi. Introduction to differential power analysis.
Journal of Cryptographic Engineering, 1(1):5–27, Apr 2011.
6. H. Maghrebi, T. Portigliatti, and E. Proff. Breaking cryptographic implementations using deep learning techniques. In Proceedings of International Conference on Security,
Privacy and Applied Cryptography Engineering (SPACE’16), 2016.
7. S. Picek, G. Perin, L. Mariot, L. Wu, and L. Batina. SoK: Deep Learning-based Physical
Side-channel Analysis. ACM Computing Surveys, 55(11):1–35, 2023.
8. M. Panoff, H. Yu, H. Shan, and Y. Jin. A Review and Comparison of AI-enhanced Side
Channel Analysis. ACM Journal on Emerging Technologies in Computing Systems,
18(3):1–20, 2022.
9. K. Papagiannopoulos, O. Glamocanin, M. Azouaoui, D. Ros, F. Regazzoni, and M. Stojilovic. The Side-channel Metrics Cheat Sheet. ACM Computing Surveys, 55(10):1–35,
2023.
10. D. Shanmugam and P. Schaumont. Improving Side-Channel Leakage Assessment Using
Pre-Silicon Leakage. In International Workshop on Constructive Side-Channel Analysis
and Secure Design (COSADE), 2023.
11. NewAE. Chipwhisperer. [https://www.newae.com/chipwhisperer.](https://www.newae.com/chipwhisperer)
12. H. Li, M. Ninan, B. Wang, and J. Emmert. Tinypower github repository, 2023. [https:](https://github.com/UCdasec/TinyPower)
[//github.com/UCdasec/TinyPower.](https://github.com/UCdasec/TinyPower)
13. C. Wang, M. Ninan, S. Reilly, J. Ward, W. Hawkins, B. Wang, and J. M. Emmert. Softpower github repository, 2023. [https://github.com/UCdasec/SoftPower.](https://github.com/UCdasec/SoftPower)

**214** Advances in Hardware Design for Security and Trust

14. C. Wang, M. Ninan, S. Reilly, J. Ward, W. Hawkins, B. Wang, and J. M. Emmert. Portability of Deep-Learning Side-Channel Attacks against Software Discrepancies. In Proceedings ACM WiSec’23, 2023.
15. G. Becker, J. Cooper, E. DeMulder, G. Goodwill, J. Jaffe, G. Kenworthy, T. Kouzminov, A. Leiserson, M. Marson, P. Rohatgi, and S. Saab. Test vector leakage assessment
(TVLA) methodology in practice. In 2013 International Cryptographic Module Conference, 2013.
16. S. Bhasin, J. Danger, S. Guilley, and Z. Najm. NICV: Normalized inter-class variance for
detection of side-channel leakage. In 2014 International Symposium on Electromagnetic
Compatibility, 2014.
17. R. Benadjila, E. Prouff, R. Strullu, E. Cagli, and C. Dumas. Deep learning for sidechannel analysis and introduction to ASCAD database. Journal of Cryptographic Engineering, 10(2), 2020.
18. R. Benadjila, V. Lomne, E. Prouff, and T. Roche. Secure AES128 for ATMega8515.
GitHub repository, 2018.
19. J. Coron and I. Kizhvatov. Analysis and Improvement of the Random Delay CounterMeasure of CHES 2009. In S. Mangard and F. Standaert, editors, “Cryptographic Hardware and Embedded Systems, CHES 2010”, pages 95–109, Berlin, Heidelberg, “2010”.
Springer Berlin Heidelberg.
20. S. Bhasin, N. Bruneau, J. Danger, S. Guilley, and Z. Najm. Analysis and improvements
of the DPA contest v4 implementation. In S. Chakraborty, V. Matyas, and P. Schaumont, editors, Security, Privacy, and Applied Cryptography Engineering, pages 201–
218, Cham, 2014. Springer International Publishing.
21. D. Bellizia, O. Bronchain, G. Cassiers, C. Momin, F. Standaert, and B. Udvarhelyi.
Spook SCA CTF. [https://doi.org/10.14428/DVN/W2SV5G, 2021.](https://doi.org/10.14428/DVN/W2SV5G)
22. M. Ninan, E. Nimmo, S. Reilly, C. Smith, W. Sun, B. Wang, and J. Emmert. A second
look at the portability of deep learning side-channel attacks over em traces. In 2024
International Symposium on Research in Attacks, Intrusions and Defenses (RAID), 2024.
23. L. Masure and R. Strullu. Side channel analysis against the ANSSI’s protected AES
implementation on ARM. Cryptology ePrint Archive, Paper 2021/592, 2021. [https:](https://eprint.iacr.org/2021/592)
[//eprint.iacr.org/2021/592.](https://eprint.iacr.org/2021/592)
24. L. Wu, A. Ali-Pour, A. Rezaeezade, G. Perin, and S. Picek. Breaking Free: Leakage Model-free Deep Learning-based Side-channel Analysis.
[https://eprint.iacr.org/2023/1110.pdf.](https://eprint.iacr.org/2023/1110.pdf)
25. S. Hajra, S. Chowdhury, and D. Mukhopadhyay. EstraNet: An Efficient Shift-Invariant
Transformer Network for Side-Channel Analysis. TCHES, 2024.
26. P. Kulkarni, V. Verneuil, S. Picek, and L. Batina. Order vs. Chaos: A Language Model
[Approach for Side-channel Attacks. https://eprint.iacr.org/2023/1615.](https://eprint.iacr.org/2023/1615.pdf)
[pdf.](https://eprint.iacr.org/2023/1615.pdf)
27. P. Wang, P. Chen, Z. Luo, G. Dong, M. Zheng, N. Yu, and H. Hu. Enhancing the
Performance of Practical Profiling Side-Chanel Attacks Using Conditional Generative
Adversarial Networks. [https://arxiv.org/abs/2007.05285.](https://arxiv.org/abs/2007.05285)
28. J. Rijsdijk, L. Wu, G. Perin, and S. Picek. Reinforcement learning for hyperparameter
tuning in deep learning-based side-channel analysis. IACR Transactions on Cryptographic Hardware and Embedded Systems, 2021(3):677–707, 2021.
29. L. Wu, G. Perin, and S. Picek. I Choose You: Automated Hyperparameter Tuning for
Deep Learning-based Side-Channel Analysis. IEEE Transactions on Emerging Topics
in Computing, 2022.

Deep Learning Side-Channel Attacks: Challenges and Opportunities **215**

30. G. Perin, L. Wu, and S. Picek. Gambling for success: The lottery ticket hypothesis in
deep learning-based SCA. Cryptology ePrint Archive, Paper 2021/197, 2021. [https:](https://eprint.iacr.org/2021/197)
[//eprint.iacr.org/2021/197.](https://eprint.iacr.org/2021/197)
31. H. Li, M. Ninan, B. Wang, and J. M. Emmert. TinyPower: Side-Channel Attacks with
Tiny Neural Networks. In Proceedings of IEEE HOST’24, 2024.
32. M. Elaabid and S. Guilley. Portability of templates. Journal of Cryptographic Engineering, 2:63–74, 2012.
33. D. Das, A. Golder, J. Danial, S. Ghosh, A. Raychowdhury, and S. Sen. X-DeepSCA:
Cross-Device Deep Learning Side Channel Attack. In Proceedings of 56th ACM/IEEE
Design Automation Conference (DAC’19), 2019.
34. A. Golder, D. Das, J. Danial, S. Ghosh, S. Sen, and A. Raychowdhury. Practical
Approaches Towards Deep-Learning Based Cross-Device Power Side Channel Attack.
IEEE Transactions on Very Large-Scale Integration (VLSI) Systems, 27(12), 2019.
35. H. Wang, M. Brisfors, S. Forsmark, and E. Dubrova. How Diversity Affects DeepLearning Side-Channel Attacks. In 2019 IEEE Nordic Circuits and Systems Conference
(NORCAS): NORCHIP and International Symposium of System-on-Chip (SoC), 2019.
36. J. Danial, D. Das, A. Golder, S. Ghosh, A. Raychowdhury, and S. Sen. EM-X-DL:
Efficient Cross-device Deep Learning Side-channel Attack with Noisy EM Signatures.
ACM Journal on Emerging Technologies in Computing Systems, 18(1):1–17, 2022.
37. F. Zhang, B. Shao, G. Xu, B. Yang, Z. Yang, Z. Qin, and K. Ren. From Homogeneous
to Heterogeneous: Leveraging Deep Learning based Power Anlysis across Devices. In
Proceedings of 57th ACM/IEEE Design Automation Conference (DAC’20), 2020.
38. S. Bhasin, A. Chattopadhyay, A. Heuser, D. Jap, S. Picek, and R. R. Shrivastwa. Mind
the Portability: A Warriors Guide through Realistic Profiled Side-channel Analysis. In
Proceedings of NDSS’20, 2020.
39. U. Rioja, L. Batina, and I. Armendariz. When Similarities Among Devices are Taken for
Granted: Another Look at Portability. In Proceedings of AFRICACRYPT 2020, pages
337–357, 2020.
40. H. Yu, H. Shan, M. Panoff, and Y. Jin. Cross-Device Profiled Side-Channel Attacks using Meta-Transfer Learning. In Proceedings of the 58th ACM/IEEE Design Automation
Conference (DAC’21), 2021.
41. C. Genevey-Metat, A. Heuser, and B. Gerard. Train or Adapt a Deeply Learned Profile?
In Proceedings of International Conference on Cryptology and Information Security in
Latin America (Latin Crypt’21), 2021.
42. H. Yu, S. Wang, H. Shan, M. Panoff, M. Lee, K. Yang, and Y. Jin. Dual-Leak: Deep Unsupervised Active Learning for Cross-Device Profiled Side-Channel Leakage Analysis.
In Proceedings of IEEE HOST’23, 2023.
43. B. Hettwer, S. Gehrer, and T. Guneysu. Deep neural network attribution methods
for leakage analysis and symmetric key recovery. Cryptology ePrint Archive, Paper
2019/143, 2019. [https://eprint.iacr.org/2019/143.](https://eprint.iacr.org/2019/143)
44. G. Perin, L. Wu, and S. Picek. I know what your layers did: Layer-wise explainability
of deep learning side-channel analysis. Cryptology ePrint Archive, Paper 2022/1087,
2022. [https://eprint.iacr.org/2022/1087.](https://eprint.iacr.org/2022/1087)
45. B. Timon. Non-Profiled Deep Learning-based Side-Channel Attacks with Sensitivity
Analysis. IACR Transactions on Cryptographic Hardware and Embedded Systems,
2019(2):107–131, 2019.
46. D. Kwon, H. Kim, and S. Hong. Non-Profiled Deep Learning-based Side-Channel Preprocessing with Autoencoders. IEEE Access, vol. 9, pp. 57692–57703, 2021.

**216** Advances in Hardware Design for Security and Trust

47. L. Wu, S. Tiran, G. Perin, and S. Picek. An End-to-end Plaintext-based Side-channel
Collision Attack without Trace Segmentation. [https://eprint.iacr.org/](https://eprint.iacr.org/2023/1109.pdf)
[2023/1109.pdf.](https://eprint.iacr.org/2023/1109.pdf)
48. L. Wu, G. Perin, and S. Picek. Hiding in Plain Sight: Non-profiling Deep Learning-based
Side-channel Analysis with Plantext/Ciphertext. [https://eprint.iacr.org/2023/209.pdf.](https://eprint.iacr.org/2023/209.pdf)
49. I. Savu, M. Krcek, G. Perin, L. Wu, and S. Picek. The Need for MORE: Unsupervised Side-channel Analysis with Single Network Training and Multi-output Regression. [https://eprint.iacr.org/2023/1681.pdf.](https://eprint.iacr.org/2023/1681.pdf)
50. I. Buhan, L. Batina, Y. Yarom, and P. Schaumont. SoK: Design Tools for Side-ChannelAware Implementations. In Proceedings of the 2022 ACM on Asia Conference on Computer and Communications Security, 2021.
51. N. Sehatbakhsh, B. Yilmaz, A. Zajic, and M. Prvulovic. Emsim: A microarchitecturelevel simulation tool for modeling electromagnetic side-channel signals. In 2020 IEEE
International Symposium on High Performance Computer Architecture (HPCA), pages
71–85, 2020.
52. L. Lin, D. Zhu, J. Wen, H. Chen, Y. Lu, N. Cheng, C. Chow, H. Shrivastav, C. W. Chen,
K. Monta, and M. Nagata. Multiphysics Simulation of EM Side-Channels from Silicon
Backside with ML-based Auto-POI Identification. In IEEE HOST’21, 2021.

# 10 Side-Channel Attack
### Avoidance and Mitigation Through Asynchronous Digital Design

John M. Emmert and Anvesh Perumalla

**10.1** **INTRODUCTION**

Due to cost considerations, integrated circuits (ICs) may be fabricated at cheaper,
untrusted facilities. The loss of process control results in digital ICs and systems
that are susceptible to side-channel attacks (SCAs). By leveraging and inserting Trojan circuits and monitoring side channels, malicious untrusted entities or agents can
steal sensitive or personal information like credit card numbers or cryptographic
keys [1, 2]. A simple way to describe a Trojan circuit is an extra circuit that is added
during the IC fabrication process by the manufacturer without the designer’s prior
knowledge. Extra circuitry is often legitimately added by the manufacturer to provide feedback data on the fabrication process. However, malicious Trojan circuits
can also be added to subversively leak secret or private information during standard
operation of the IC. Several different types of Trojan circuits have been developed
that require minimal area overhead and are very difficult for designers to detect either
during normal testing or (low probability) IC reverse engineering [1,3,4]. The SCAs
themselves make use of indirect measurements to exploit either already-existing or
secretly added Trojan circuitry and obtain secret or private information [5, 6]. Many
types of SCAs can leverage indirect measurements like temperature variations, electromagnetic radiation, power usage, or other measurable characteristics during regular or normal IC operation. Covertly inserted Trojan circuits and the exploitation of
indirect, synchronized readings are primary enablers of many Trojan attacks.

One approach to mitigate and combat SCAs is to use asynchronous or clockless
digital design [7]. There are several different types of asynchronous design methods that range from locally clocked to completely clockless (handshaking), and each
type has its own advantages and disadvantages [8]. One popular form of clockless
logic circuit is based on Null Convention Logic (NCL) [9, 10]. The NCL technique

[DOI: 10.1201/9781003510949-10](https://doi.org/10.1201/9781003510949-10) **217**

**218** Advances in Hardware Design for Security and Trust

works well for data flow designs because the data flows through the processing networks in waves. In NCL, a data wave is only processed when all incoming signal
values are available, making it self-timed. Since input signals are only processed
when available, no timing assumptions are required. This characteristic guarantees
data sequencing and correct data arrival at the receiver under varying gate, process,
and wire delays [9]. In this chapter, we provide additional material on the problem,
SCAs, and Trojan circuits; a brief tutorial on a solution, asynchronous NCL digital
design; recent work related to NCL design; limitations associated with asynchronous
NCL design (mainly circuit size); and some recent solutions and methodologies to
overcome some of the limitations.

**10.1.1** **SIDE-CHANNEL ATTACKS**

SCAs leverage indirect signal measurements (like power consumption, temperature
variations, electromagnetic emanations, etc.) and existing or added (Trojan) circuitry
to steal secret, sensitive, or private information.

With algorithmic or other system implementation details, SCAs allow an untrusted agent or entity to indirectly extract private data during normal IC operation.
Figure 10.1 shows an example of data for a power-based SCA to detect a two-bit
secret key value. Figure 10.1 (A) illustrates the expected ideal patterns for each of
four possible two-bit key values, k ∈{00, 01, 10, 11}. Figure 10.1 (B) shows noisy
power data that is cross-correlated with each of the expected key patterns. After
cross-correlation, the raw data in Figure 10.1 has the highest correlation with key 01.

**10.1.2** **TROJAN CIRCUITS**

Extra circuitry is often added by the IC manufacturer during the fabrication process.
Non-malicious extra circuitry can include test structures, bypass circuitry, isolation
circuitry, etc. These circuits are useful and serve a purpose like testability, fault tolerance, improved performance, and improved process yield. However, extra circuitry
can be added for malicious intent. Another, similar way to describe Trojan circuits
is extra-malicious circuity added by the manufacturer or an untrusted agent during
the IC fabrication process. Trojan circuits can be leveraged to leak private or secret
information during normal IC operation. Malicious actors take advantage of obfuscation techniques to make the detection of Trojan circuits and data leakage very
difficult. Several types of Trojans have been developed that require minimal area
overhead and are very difficult to detect either during regular IC testing or IC reverse
engineering [4, 11–13].

One Trojan circuit that demonstrates the concepts of malicious Trojans is the malicious off-chip leakage enabled side-channels (MOLES) circuit [1]. The data in
Figure 10.1 was taken from an application with an added MOLES structure. The
MOLES circuit is relatively small; uses very little power; can be built using simple,
digital circuitry; and allows side-channel data leakage that can be post-processed to
detect things like secret keys. Figure 10.2 illustrates a basic MOLES circuit used to

Side-Channel Attack Avoidance and Mitigation **219**

**Figure 10.1** Illustration of synchronized power substrate propagation.

detect a l-bit key. It is composed of a Pseudo Random Number Generator (PRNG),
some extra Exclusive-Or (XOR) gates, and some extra capacitance. A PRNG circuit
is already available in many IC designs. If one already exists within the IC, it can
be tapped to produce the required pseudo random number (PRN). If a PRNG is not
readily available, one can be created with low area overhead by adding a simple Linear Feedback Shift Register (LFSR). The LFSR only requires a few D flip flops and
XOR gates. Either way, leveraging an existing or added PRNG, the malicious agent
will use the known pattern of the PRNG during the processing of side-channel data.

The extra XOR gates each have two inputs: secret key bit and PRNG bit. The secret key bits are a function of the data that is being leaked. For most applications, the
secret key bits are stored in non-volatile memory that is loaded post-IC fabrication, so
the key is unknown at the time of IC fabrication. The other inputs, PRNG bits, come
from the known, PRNG pattern. By collecting millions of samples of side-channel

**220** Advances in Hardware Design for Security and Trust

**Figure 10.2** Example Trojan circuitry: MOLES circuit [1].

data and cross-correlating it with the known pattern XORed with different combinations of expected key bits, the secret key can be determined with a high degree of
probability.

The last pieces of the MOLES circuit are the capacitors that are driven by the output of the added XOR gates. These are usually not directly accessible to the outside
world, and in fact, they are obfuscated to avoid detection. They do use miniscule
(but predictable) amounts of power. For complementary metal oxide semiconductors
(CMOS), these are usually formed from the gates of carefully sized CMOS p-type
and n-type field effect transistors (FETs). The sizing of these capacitors is critical to
the MOLES circuit. If they are too large, the extra power used to drive them from
logic ‘1’ to ‘0’ and ‘0’ to ‘1’ will be detected during normal IC testing. If they are too
small, the probability of secret key cross-correlation goes down. Usually, extensive
simulation is required to set them to an acceptable size.

Once properly sized and inserted, the synchronous nature of the MOLES data and
circuit can be used by a malicious entity to steal secret keys. The MOLES circuit
itself is one example of a class of Trojan circuits that can be inserted during remote
fabrication. A key aspect of almost all Trojan circuits is the synchronous, clocked
nature of their data processing.

**10.2** **ASYNCHRONOUS DESIGN**

Clocked or synchronous IC systems are especially susceptible to SCAs if they are
fabricated at untrusted foundries where malicious Trojan circuits can be inserted.
As described in the last subsection, a malicious entity can leverage Trojan circuits
to steal sensitive information like secret keys by monitoring power consumption,
electromagnetic emanations, temperature, or other indirectly measurable IC characteristics [2].

One way that has been shown to mitigate MOLES-type SCAs is to leverage asynchronous circuit design to desynchronize or distribute (relative to time) power consumption, electromagnetic emanations, etc. [7, 14]. Using clockless, asynchronous
digital processing makes it more difficult for the attacker to decipher the SCA
data. Furthermore, researchers have demonstrated asynchronous logic offers greater

Side-Channel Attack Avoidance and Mitigation **221**

**Figure 10.3** Threshold gate, THmn, with threshold m and n inputs [9].

tamper-resistance to counteract SCAs [14]. Thus, an asynchronous circuit can be
used to mitigate SCAs. Instead of processing data changes all at once (on a clock
edge), asynchronous logic distributes (in-time) data processing and makes it very
difficult to cross-correlate secret keys with measured side-channel data. It should be
mentioned that asynchronous logic processing is also applicable to mixed-signal design. When sensitive analog and radio frequency (RF) components are fabricated on
the same substrate as clocked digital circuits, the synchronized power consumption
of the digital CMOS gates causes “ringing” in the form of digital noise that propagates through the substrate of the IC. This so-called ringing presents itself as noise
to the analog and RF circuits. One metric used to determine the effectiveness of
analog and RF components is signal-to-noise (S/N) ratio. The synchronous, digital
noise raises the noise floor (N), thereby lowering the S/N ratio. Isolation and moats
are examples of techniques used to improve mixed-signal S/N for analog and RF
circuits; however, they have been met with limited success [15]. By distributing the
digital noise, N, in time, asynchronous logic is another approach to improve common
substrate, mixed-signal design.

Here, we present a brief tutorial of basic NCL. More detailed explanations are
available in [8, 9, 16–18].

**10.2.1** **THRESHOLD GATES**

The key component of NCL logic gates is the THmn threshold gate. Figure 10.3
illustrates a basic THmn threshold gate. For the general or basic THmn gate, m defines the threshold value of the gate and n defines the number of inputs. Instead of
Boolean logic levels, THmn gates operate on two signal values: data and null. In abstract terms, a data value, D, on a wire indicates data is present. It does not mean the
wire is a logic ‘1’ or ‘0,’ it only implies data is present. Similarly, a null value, N, on
a wire indicates the lack of data on a wire (in other words, no data is present). Just
to be clear, it is worth reiterating that the input and output wires can only have the
abstract values data, D, or null, N, on them.

The basic operation of the THmn gate is similar to a Boolean latch in that it has
hysteresis or memory characteristics. All n inputs of the THmn gate start with null,
N, values on them. With all n input values set to N, the output of the THmn gate is
forced to N. As the inputs of the THmn gate start to change to data, D, the output
remains at an N value until m of the n inputs become D. Once the threshold, m, is
reached, the output becomes D. As the inputs start to change back to N, the output

**222** Advances in Hardware Design for Security and Trust

**Figure 10.4** Basic library of THmn threshold gates [7].

**Figure 10.5** Example weighted threshold gate, TH35w322.

holds the D value (hysteresis effect) until all of the n inputs change back to N. Once
all the inputs are back to N, the output changes back to N, and the process repeats.

To build useful logic circuits, a library of THmn gates is available. Figure 10.4
shows a basic library [9]. In Figure 10.4, it is worth noting that the diagonal THmn
gates, where m = n, are called the Muller C-Elements [19, 20]. These asynchronous
gates predate NCL logic, and they are often found in many types of asynchronous
circuits, not just NCL.

In addition to basic THmn gates, there is a class of weighted, threshold gates [7].
They are too numerous to mention all of them, but an example will illustrate the operation of the others. Figure 10.5 shows a TH35w322 threshold gate. The TH35w322
gate has a threshold of m = 3 with n = 5 inputs. However, the weight of the first input
is 3, the second input is 2, the third input is 2, and the remaining inputs are 1. To
set the output of the weighted TH35w322 threshold gate to D, any combination of

Side-Channel Attack Avoidance and Mitigation **223**

**Figure 10.6** Standard K-map to NCL logic function.

the following can occur: the first input (alone) can be set to D, the second and third
inputs can be set to D, the second and fourth or fifth inputs can be set to D, or the
third and fourth or fifth inputs can be set to D. Weighted threshold gates are used to
reduce the total number of threshold gates required to implement NCL logic gates.

Once we have a library of threshold gates that operate on a set of abstract signal
values, D and N, we can combine them to form a set of asynchronous, Boolean logic
functions. The first step is to make the logic less abstract. This is accomplished by
creating dual wire (rail) signals with one wire to represent logic ‘1’ and one wire to
represent logic ‘0.’ As an example, signal X will have one wire, X1, that represents
logic ‘1,’ and one wire, X0, that represents logic ‘0.’ The cost of this resolution is two
wires for every digital logic signal, but typically, there are more than enough routing
layers available in most contemporary IC fabrication nodes. So, the extra wires are
not typically a problem; however, the number of FETs in threshold gate logic circuits
is up to three to four times that of their equivalent Boolean circuits.

**10.2.2** **NCL LOGIC GATES**

Here, we will illustrate the process to implement basic Boolean output complete
logic functions using threshold gates. A basic approach to generate output complete NCL logic gates is to use the standard digital Karnaugh-map (K-map) of the

**224** Advances in Hardware Design for Security and Trust

**Table 10.1**
**Table of Common Semi-Static TH** **_mn_** **Gates with Equations and Transistors [7]**

Gate Boolean Function Trans Count
TH12 A + B 6
TH22 AB 8
TH13 A + B + C 8
TH23 AB + AC + BC 12
TH33 ABC 10
TH23w2 A + BC 10
TH33w2 AB + AC 10
TH14 A + B + C + D 10
TH24 AB + AC + AD + BD + BD + CD 16
TH34 ABC + ABD + ACD + BCD 16
TH44 ABCD 12
TH24w2 A + BC + BD + CD 14
TH34w2 AB + AC + AD + BCD 15
TH44w2 ABC + ABD + ACD 15
TH34w3 A + BCD 12
TH44w3 AB + AC + AD 12

Boolean equation along with threshold gate equations. Figure 10.6 shows the symbol,
K-map, and function of a standard Boolean combinational Not-Or (NOR) gate. The
Prime Implicants (PIs) in the K-map capture the product terms that form the sum of
products (SOP) expression for the NOR equation. To implement an NCL version of
the NOR function, we relabel the rows and columns of the K-map by replacing the
Boolean logic values with the NCL wires that represent those values. Then we find
PI product terms for both the logic ‘0’ output wire (G0 = X1 + Y1) and the logic
‘1’ output wire (G1= X0 · Y0). Next, we find the form of the logic function for each
output wire in the NCL functional table, Table 10.1. For this example, the form of
the expression for G0 is A + B, so a TH12 threshold gate is used to implement the G0
function. The form of the expression for G1 is A · B, so a TH22 threshold gate is used
to implement the G1 function. In general, most standard Boolean logic gates can be
built directly using a basic threshold gate library. So, if you can design a combinational Boolean circuit, you should be able to build an NCL version of that circuit. (It
should be noted that if the function is not available in the target library, it must be
built from smaller threshold gates.)

It should also be noted that we only discussed output-complete NCL logic.
Output-complete NCL logic changes as soon the minimum required input wires have
D on them. Input-complete NCL logic has more transistors, but the outputs will not
change until all input signals have logic values on them.

Side-Channel Attack Avoidance and Mitigation **225**

**Figure 10.7** CMOS design of semi-static TH12 and TH22 threshold gates.

**10.2.3** **TRANSISTOR-LEVEL THRESHOLD GATES**

Once we determine which threshold gates are required to implement asynchronous
digital logic circuits, we need to know how to implement the threshold gates with
CMOS transistors. To illustrate this, we describe examples of how to implement
the semi-static CMOS versions of TH12 and TH22 threshold gates. Other gates are
similar in design. The semi-static CMOS transistor design can be broken into four
parts, as shown in Figure 10.7. The transistor design of the Reset network consists of
series connected p-type transistors, one for each of the inputs. A series p-type FET
source to drain connections (one p-type FET for each input) will work for the Reset
network of all the threshold gates in the library. For semi-static threshold gates, the
Hold Null and the Hold Data networks consist of a set of cross-coupled inverters.
These two Hold networks perform the hysteresis function, they hold null or hold
data as the inputs toggle between all null values (Reset) and m data values (Set).
They are the same for all semi-static transistor implementations of THmn threshold
gates with the exception of the m = 1 TH1n gates. Since TH1n gates only have a
threshold m = 1, they do not need the HOLD networks. The set to data networks
need a little more explanation. To create the set to data network, series and parallel
connections of n-type CMOS transistors are combined to form the AND and OR
functions (respectively) described in the threshold gate in Table 10.1. The TH12 gate
in Figure 10.7 has a parallel OR connection to form the Set TH12, A + B function.
The TH22 gate in Figure 10.7 has a series AND connection to form the Set TH22,
A - B function. All the functions in Table 10.1 can be similarly designed. It should be
noted that when making series AND connections, fabrication node limitations on the
number of allowable series transistors must be adhered to.

In this section, we covered threshold gates, logic function design with threshold
gates, and transistor-level design of threshold gate circuits. Much more detail can be
found in resources dedicated to the subject of NCL design [7, 16].

**226** Advances in Hardware Design for Security and Trust

**10.3** **CURRENT STATE OF THE ART OF ASYNCHRONOUS NCL**
**DESIGN**

Researchers have been working with asynchronous circuit design since the 1950s

[19, 20]. More recently, in the 1990s, NCL logic was formalized [7]. As a result, some technology companies, such as Intel and IBM, have increased research
and design related to asynchronous circuits, and globally asynchronous locally synchronous (GALS) circuits and networks-on-chip (NoC) architectures have been introduced [21]. From GALS methods to completely asynchronous logic systems, several issues need to be addressed for the more general digital design community to
be more accepting of the asynchronous approach. Branover, Kol, and Ginosar found
that area growth for an asynchronous circuit can be over 200 percent, with more
area growth occurring for smaller asynchronous equivalent designs [22]. They also
used Synopsys to synthesize synchronous circuits, and then converted them to asynchronous circuits. This is suboptimal because those tools are not designed for asynchronous circuit generation or optimization.

Current topics of interest include, but are not limited to:

1. Methods to reduce and minimize asynchronous circuit area.
2. Improved methods to interface standard clocked circuits to asynchronous
circuits.
3. Improved field programmable asynchronous gate arrays.
4. Computer aided design (CAD) tools that optimize asynchronous circuits.
5. CAD tools to optimally convert synchronous circuits to asynchronous circuits.
6. Improved event-driven simulators.

The techniques described below address the first, arguably main concern, asynchronous circuit area.

**10.4** **LIMITATIONS OF ASYNCHRONOUS NCL DESIGN**

There are several limitations that hinder digital asynchronous circuit design from
becoming more accepted by the digital design community. The biggest drawback is
arguably related to asynchronous circuit area. The number of transistors in a fully
asynchronous digital circuit can be more than three times the size of the equivalent
Boolean logic circuit. Even with the tremendous improvements in fabrication process nodes, these large area requirements remain unacceptable with the exception
of highly specialized circuits. Additionally, asynchronous CAD tools are in short
supply. Finally, even though the world is asynchronous, most of our data processing is synchronized or clocked. It is difficult to interface existing clocked systems
to asynchronous ones. The discussion below focuses on recent advances to significantly reduce asynchronous circuit area, and to a limited extent, make as much use
as possible of existing digital CAD tools and design flows.

Side-Channel Attack Avoidance and Mitigation **227**

**10.5** **RECENT** **SOLUTIONS** **AND** **METHODS** **FOR** **ASYNCHRONOUS**
**NCL DESIGN**

In order to improve acceptance, recent work has focused on reducing the size of
asynchronous, and especially, NCL logic circuits [23–30]. A difficult hurdle to many
approaches is to reduce the circuit area while still maintaining the main advantages
of asynchronous over standard Boolean circuits for SCA and mixed-signal design
applications. We present the details of a path-based approach that makes use of special hybrid cells to minimize the amount of asynchronous circuitry, thereby bringing
the area increase to approximately 6 percent of a standard Boolean digital circuit.
The second technique describes a method to reduce the number of transistors in an
asynchronous n-input, Muller C-Element to approximately half the number in the
standard NCL Muller C-Element implementation.

**10.5.1** **PATH-BASED ASYNCHRONOUS DESIGN USING HYBRID CELLS**

Most fabricated designs are synchronous, meaning they require one or more global
clock signals that simultaneously push combinational data through the circuit. This
results in a large, synchronized power draw that propagates through the IC substrate
causing digital noise and exposes confidential data [1, 3]. This abets methods such
as Simple Power Analysis (SPA) and Differential Power Analysis (DPA), and it allows reverse engineering of circuit functionality. In addition, global clock signals add
unwanted power leading to large inefficiencies for clocked circuits.

One approach to implement asynchronous circuits is through the use of NCL
gates, which, according to [9], is a symbolically complete logic which expresses a
process completely in terms of the logic itself and inherently and conveniently expresses asynchronous digital circuits. Designs that use NCL gates have increased
design security and assurance due to the dual rail design; however, there is a cost:
relatively large numbers of transistors.

**10.5.1.1** **NCL Data-Path Design Methodology**

Figure 10.8 shows an example critical timing path for a combinational Boolean logic
circuit. The idea behind the path-based approach to asynchronous design is to determine the critical timing path of a standard combinational Boolean circuit and
replace the Boolean logic gates in the critical timing path with their hybrid, asynchronous equivalent gates. The hybrid, asynchronous gates have one critical path
asynchronous NCL input; one or more standard, non-critical path Boolean inputs;
and one NCL critical path output. The approach assumes that all non-critical path,
Boolean signals arrive at their non-critical path inputs before the asynchronous NCL
input. This approach alters the design of basic NCL gates so that they can process
one or more standard Boolean inputs as well as one dual rail asynchronous input,
and at the same time, output a dual-rail asynchronous signal. The methodology
maintains the return-to-zero (RTZ) characteristic that is found in asynchronous circuits, and it allows these hybrid gates to maintain the same security benefits as fully

**228** Advances in Hardware Design for Security and Trust

**Figure 10.8** Example of critical timing path Boolean logic gates.

asynchronous circuits. The RTZ design keeps the circuit from executing until the
asynchronous inputs have been set. These so-called hybrid, data-path cells can be
inserted directly into a combinational digital design using standard CAD tools and
flows, eliminating the need for special-purpose asynchronousCAD tools. Logic gates
not in the critical path remain standard, Boolean gates. In most cases, the majority
of Boolean gates are not in the critical path, so only a minority of Boolean gates
are replaced with their larger, hybrid equivalents. The overall result: asynchronous
circuit area is greatly reduced.

In the past, attempts have been made to implement similar approaches, but success
was limited [22,31–34]. To minimize the overall circuit area, it was desirable to only
use asynchronous cells in the critical timing paths and maintain Boolean logic structures for the rest of the circuit. There were two primary difficulties with actual implementation. First, only one input of a gate in the critical timing path was actually in the
critical timing path, but the other, non-critical path, gate inputs also had to be driven
by asynchronous NCL gates. This resulted in a large number of other, non-critical
path asynchronous NCL gates. The result was an insignificant overall area reduction. Second, to address the drawback, attempts were made to maintain the Boolean
structure of the gates driving the non-critical path gate inputs by adding signal conditioning circuits to them. The signal conditioning circuits converted non-critical path
Boolean inputs to dual-rail asynchronous NCL inputs, but it also added input signal
delay to the non-critical path Boolean inputs. Ultimately, this changed the critical
timing paths, and compromised the integrity of the resultant asynchronous circuit.
To overcome these difficulties, the key was to develop methods that maintained the
integrity of the critical path, and did not add additional delay to non-critical path
combinational inputs. The approach described below addresses these issues, and it
does so without requiring any extra external circuitry for signal conditioning. The result: No added delay to Boolean inputs and only cells in the critical timing path need
to be replaced by hybrid cells [24, 25, 30]. All other cells remain standard Boolean.

To successfully implement the hybrid, data-path approach for asynchronous circuit generation, it is critical to correctly identify the longest timing paths through all
combinational subcircuit blocks. To accomplish this, one approach is to use static
timing analysis available in most commercial off-the-shelf synthesis tools, or it can
be accomplished using an O(N - log(N)) breadth first search. To be compatible
with most commercially available design flows and tools, a tool needs to 1) parse a

Side-Channel Attack Avoidance and Mitigation **229**

**Figure 10.9** Example of critical timing path asynchronous NCL logic gate substitution.

structural Verilog netlist, 2) convert it to a hyper-graph, 3) find the critical timing
delay path, 4) substitute hybrid cells for the standard Boolean gates in the critical
timing path, and 5) write the result to a modified, structural Verilog netlist. Figure
10.9 illustrates the ideal result of such a tool. In Figure 10.8, the critical timing path
gates have been replaced with their hybrid equivalents, and no external signal conditioning has been added to the non-critical path Boolean inputs, thereby maintaining
the integrity of the critical path. The only area increase for the resulting asynchronous
NCL circuits is the additional area required to implement the hybrid gates. Below,
Table 10.2 illustrates the area reduction for several benchmark circuits [24]. Overall, Table 10.2 shows the hybrid data-path approach achieved asynchronous circuits
with only an average of 6 percent more transistors than the functionally equivalent
Boolean circuits. This is in contrast to the fully asynchronous circuits that had on
average 2.47 times more transistors [24].

To significantly reduce the area of an equivalent asynchronous NCL circuit, only
the gates in the critical timing path should be replaced by their hybrid counterparts.

**Table 10.2**
**Transistor Counts for Standard, Fully Asynchronous, and Hybrid Circuits [24]**

BM Circuit Boolean # FETs Semi-static # FETs Hybrid # FETs
C432 826 1894 1008
C499 1796 3564 1904
C880 1802 4324 2037
C1355 2276 6892 2556
C1908 3330 7402 3628
C2670 5008 10382 5169
C3540 7194 14980 7518
C5315 11332 22676 11700
C6288 10112 33376 11031
C7552 15624 32108 15939
WTM4 468 1120 609
WTM12 876 2040 1309
RISC V 10048 33868 10826

**230** Advances in Hardware Design for Security and Trust

Given a static timing analysis tool that determines the list of Boolean gates in the
critical timing path, the following assertion must be adhered to:

 - Replacing standard Boolean gates in the critical timing path with their hybrid equivalents must not change the critical timing path.

Two implications:

 - All non-critical timing path or standard Boolean signal values must arrive
at the non-asynchronoushybrid gate inputs before critical timing path asynchronous NCL inputs.

 - Signal conditioning of hybrid gate Boolean inputs must not result in additional input delay.

Hybrid gates have two types of inputs: a dual-rail asynchronous NCL input and
one or more standard Boolean inputs. By contrast, hybrid gates only have one type of
output: a single dual-rail NCL output. To make sure the second set of assertions are
adhered to, hybrid gates must be designed with no external signal conditioning on
their inputs and it must guarantee signal propagation delay through the hybrid gate is
≥ the delay through the Boolean gate it replaces. Usually this is not an issue because
hybrid gates have at least two levels of transistor delay and additional delay can be
added by sizing the transistors. All assertions should be verified.

**10.5.1.2** **Critical Timing Path Hybrid Cell Design**

In the past, it has been difficult to design data-path cells without adding Boolean
input delay that results from signal conditioning circuitry [22, 31, 34]. To directly
address this, we use a technique for signal conditioning that is included within the
hybrid cell itself, so no Boolean input delay is added. The hybrid gate can be directly
inserted into a critical timing path without violating any assertions. For each hybrid
gate, the dual-rail NCL input interfaces directly to the NCL output of the previous
hybrid gate in the critical timing path (the first gate in the path is either driven by an
NCL primary input or an NCL register cell). All other (non-NCL) Boolean inputs are
driven by non-critical path Boolean logic gates. Each NCL hybrid gate output drives
the next NCL input in the critical timing path [24, 25].

In Figures 10.8 and 10.9, we see the critical timing path Boolean NOR gate replaced with a hybrid NOR gate. To understand hybrid gate design, we first compare
a standard Boolean NOR gate implementation to a fully asynchronous NCL gate implementation (Figure 10.6). In Figure 10.6, the standard two-input NOR gate uses
two p-type and two n-type CMOS transistors, for a total four transistors. By contrast,
the asynchronous NCL gate in Figure 10.6 uses one TH12 and one TH22 threshold
gates, and from Table 10.1, we see this requires 14 transistors. There are 3.5 times as
many transistors in the asynchronous NCL gate.

The Boolean NOR2 gate in Figure 10.6 has two Boolean input signals, X and Y,
and a single Boolean output signal, G. Each signal in Figure 10.6 can have a Boolean
logic value of ‘1’ or ‘0.’ The asynchronous NCL NOR2 gate in Figure 10.6 has two

Side-Channel Attack Avoidance and Mitigation **231**

dual-rail input signals, X (X1 and X0 wires) and Y (Y 1 and Y 0 wires), and one dualrail output signal, G (G1 and G0 wires). Each dual-rail signal has two wires, a logic
‘1’ wire and logic ‘0’ wire, which must each be driven by a separate sub-circuit.
The biggest difference for the asynchronous NCL NOR2 in Figure 10.6 is that a data
(Vdd) value applied to either wire (logic ‘1’ wire or ‘0’ wire) asserts its logic value.
In other words, a Vdd applied to the logic ‘1’ wire implicates the NCL signal has a
logic ‘1’ on it, and a Vdd applied to the logic ‘0’ wire implicates a logic ‘0’ value
on the NCL signal. A hybrid gate must support both single-rail Boolean inputs and
asynchronous dual-rail NCL input and output. The general design flow for hybrid
gate Boolean inputs is shown in Algorithm 2 [24].

Algorithm 2: Hybrid gate design flow [24]

if Boolean value to pull Zb downto Vss = 1 then

use strong n-type FETs for Boolean inputs in set Data/Vdd subcircuit
else

use weak p-type FETs for Boolean inputs in set Data/Vdd subcircuit
add additional weak n-type FET to Hold Null/Vss subcircuit
end if

The tricky part of designing the equivalent hybrid gate is the Boolean logic ‘0’
input. Since hybrid gates output dual-rail, asynchronous NCL signals, a logic ‘0’
value is represented by a Vdd on the logic ‘0’ wire. The hybrid gates need to process
Boolean logic ‘0’ inputs at the Vss voltage level, but generate a Vdd voltage level
on asynchronous NCL logic ‘0’ output wires. Traditional CMOS gate design is difficult because CMOS is an inverting logic. Traditional CMOS would require extra
inversion circuitry, and the extra inversion (input signal conditioning) can change the
circuit critical path. To handle this, we leverage an unconventional, weak transistor
design. Figure 10.10 shows an example NOR2 hybrid gate design using the procedure in Algorithm 2. Other hybrid gates can also be designed using the approach [24].

For the NOR2 hybrid gate in Figure 10.10, there are three critical cases to analyze:
X = ‘1’ =⇒ G = ‘0,’ Y = ‘1’ =⇒ G = ‘0,’ and X = Y = ‘0’ =⇒ G = ‘1.’ It is
assumed that the X input is the dual-rail, asynchronous NCL input; Y is a Boolean
combinational input; and G is the dual-rail, asynchronous NCL output. For the X =
‘1’ case, output G should become a logic ‘0’ regardless of the value on the Boolean
input, Y . In asynchronous NCL, this corresponds to a data (Vdd) on the logic ‘0’
wire, G0, and a null (Vss) on the logic ‘1’ wire, G1. Since the NCL input signal X is
in the critical path, the dual-rail NCL wire X1 will become Vdd after the arrival of
the value on Boolean input Y (which is a do not care for this case). Since X1 becomes
Vdd, according to NCL convention, X0 will remain Vss. In Figure 10.10, with X1 =
Vdd, G0 will be set to Vdd (hybrid TH12), and with X0 = Vss, G1 will stay at Vss
(hybrid TH22). Further, G0 will remain Vdd (hysteresis) until X1 is reset to Vss (X0
is already Vss).

For the Y = ‘1’ case, output G should go to a logic ‘0’ regardless of the value that
the NCL input signal X eventually becomes (note Y arrives first). In the data-path

**232** Advances in Hardware Design for Security and Trust

**Figure 10.10** Example of hybrid asynchronous gate transistor implementation.

hybrid approach, Y becomes ‘1,’ and then either X1 or X0 will become data (Vdd),
while the other remains null (Vss). In the circuit in Figure 10.10, if X1 = Vdd (X0 =
Vss), the logic ‘0’ output wire, G0, will become Vdd (hybrid TH12), and the logic
‘1’ output wire, G1, will be Vss. Else, if X0 = Vdd (X1 = Vss), the logic ‘0’ output
wire, G0, will become Vdd (hybrid TH12), and the logic ‘1’ output wire, G1, will
remain Vss (hybrid TH22). So, the logic ‘0’ output wire, G0, is set regardless of the
value signal X changes to. Further, G0 will remain Vdd until X is reset (X0 = X1 =
Vss).

It should be noted that for both previous cases, the Boolean input is either a logic
‘1’ or a do not care. For the final case, where the Boolean signal has a controlling
value of ‘0,’ the pFET design flow in Algorithm 2 comes into play.

For the X = Y = ‘0’ case of the NOR2 example in Figure 10.10, the output should
eventually become a logic ‘1.’ For NCL, both X1 and X0 are initialized to null (Vss).
In the example NOR2 circuit (Figure 10.10), these null values force G1 = G0 =
Vss regardless of the value on Boolean input Y . Based on the data-path assertions,
Boolean Y becomes ‘0’ before X is asserted. With Y = ‘0,’ when X0 is asserted =
Vdd (X1 still = Vss), G0 will remain Vss; however, Zb in the G1 subcircuit (hybrid
TH22) will be pulled down through the weak Y pFET, and G1 will become Vdd. So,
the logic ‘1’ output wire, G1, is set. Further, G1 will remain set to Vdd until X is
reset (X1 = X0 = Vss).

Side-Channel Attack Avoidance and Mitigation **233**

To satisfy the assertions describe above, the delay of a replacement hybrid gate
must be ≥ the delay of the replaced critical timing path Boolean gate. Given the
assertions are true, it can be assumed that all combinational Boolean signals arrive
before the asynchronous NCL dual-rail signal values. To guarantee the assertions,
designers carefully control hybrid gate transistor sizes. One approach is to begin with
standard, proportional transistor widths for CMOS transistors in the hybrid gates and
perform low, transistor-level simulations to verify delays between standard Boolean
gates and hybrid replacements. To increase the delay through hybrid gates, transistor
widths can be narrowed or lengths can be increased to an acceptable margin of error
for the envelop of a particular target fabrication node.

**10.5.2** **AREA-EFFICIENT MULLER C-ELEMENT**

Even though asynchronous circuits are not clocked, they can still take advantage of
registers to shift large sets of data from one processing unit to the next. The main
difference between standard, clocked Boolean registers and asynchronous registers
is that asynchronous registers pass data through hand-shaking protocols instead of
on clock edges. The advantage of the asynchronous registers is that while they can
pass large amounts of data, they all operate independently of each other. For asynchronous registers, the timing of data transition is distributed versus all at once for
synchronous, clocked registers. The distributed nature is what helps prevent SCAs.
It should be noted that registering large sets of asynchronous data does increase the
instantaneous power consumption, thereby negatively impacting the digital noise in
mixed-signal circuits, but since the registers are operating independent of each other,
it is still significantly less than for synchronously clocked systems.

Figure 10.11 illustrates standard synchronous and asynchronous NCL registers for
an n = 3-bit data wave. For the standard clocked registers in Figure 10.11, all data is
passed to the combinational processing blocks at the same time, on the same clock
edge. The sudden increase in combinational switching causes large, synchronized
power spikes. On the other hand, the asynchronous NCL registers operate independently from each other. The feedback (FB) to previous and FB from next signals
control when data is passed between the combinational processing blocks. Within
the asynchronous NCL register is a FB circuit component composed of an inverted
THmn threshold gate where the threshold, m, is the same as the number of inputs, n.
We call the special case threshold gate where n = m a THmm gate. As shown in the

**Figure 10.11** Standard synchronous and asynchronous NCL registered circuits.

**234** Advances in Hardware Design for Security and Trust

**Figure 10.12** TH33 gate and staged TH44 =⇒ THmm, m = 16 implementation.

diagonal of Figure 10.4, this special class of threshold gate is called the set of Muller
C-Elements [19, 20, 26, 29, 35–37].

The THmm Muller C-Elements in NCL registers have m inputs, where m is the bitwidth of the register. The FB subcircuit itself is composed of a THmm gate followed
by an inverter on its output. It should be noted that the data in an NCL circuit is
processed in waves. Successive waves of null values followed by data values keep
the process rolling. The input to the FB THmm gate starts out with all null values
on its inputs, thereby initializing the output of the THmm gate to null. The inverter
actually reverses that null value and feeds back a data value to the previous stage,
telling it that it is ready to receive new data values. Once all the input data values
arrive at the inputs to the m-bit NCL register and once the FB from the next NCL
register has data on it, all the m inputs to the m-bit Muller C-Element will have
data on them. The threshold, m, is met, and the output of the FB Muller C-Element
becomes data. This triggers an inverted data, or null value, to be fed back to the
previous stage, telling it that it is busy processing, do not send new data values yet,
send a null wave to clear out the register.

The main component of any asynchronous NCL hand-shaking register is the feedback circuit or the inverted THmm gate. In Figure 10.12, there is a symbolic TH33
gate and its corresponding transistor diagram. An inverter can be added to the output
Z, or for low fanouts, the Zb output can be directly fed back to the previous asynchronous register. For Muller C-Elements with m ≥ 5 input bits, the feedback THmm
gate is usually implemented by staging up smaller TH44 gates. The 5-bit input limit
is a function of the target fabrication technology node, and the number of allowable
series transistors should not be exceeded. It should also be noted that the size and
delay of the feedback circuit is a function of the number of THmm feedback circuit
inputs, N, and ideally, a single THmm gate would be used where m = N.

Due to the fabrication node limits on the number of series transistors, Muller CElements, or THmm threshold gates, with high numbers of inputs (m ≥ 5), are usually

Side-Channel Attack Avoidance and Mitigation **235**

implemented by staging up smaller, THmm with m ≤ 5, threshold gates. An example
is shown in Figure 10.12 where an m = 16 Muller C-Element is created using five
TH44 gates. This TH1616 threshold gate could be used in a register with N = 16
inputs.

The five staged-up m = 4 bit-width TH44 gates each require 12 transistors (see
Table 10.1), for total of 5 × 12 = 60 transistors, and since each TH44 gate requires
two levels of transistors, the m = 16 input Muller C-Element requires a total of four
transistor delays between the time an input changes and the output is valid. In more
generic terms, the number of transistor levels in a staged-up THmm gate is ⌈log4(m)⌉,
where m is the number of inputs [26]. An example application, a 64-point complex
FFT circuit, has a data-path with 64 complex inputs. Even if each complex input is
only 2 × 8-bits, then the data-path has m = 1024 bits and the number of staged-up
levels of TH44 gates in the staged-up THmm, m = 1024, gates is five. With two
transistor delays in each level, the total number of transistor delays from an input
change until the output is valid is 10. In reality, this is a very modest example. In
receiver-processing applications, N = 1024-point fast Fourier transform (FFT) circuits are not unusual. If driven by 12-bit analog-to-digital converters, a 1024-point
FFT would require m on the order of 28k-bits. To make NCL acceptable, it is necessary to reduce the feedback circuit area and delay. Some previous work has met with
limited success [8,9,16,31,33,38]; however, the design presented here requires only
two levels of transistor delays and uses half the transistors of the standard, staged-up
register feedback circuits [26, 29].

In general, NCL circuits (to include Muller C-Elements) would be more acceptable and utilitarian to the digital design community if threshold gate delays and sizes
could be further minimized to match conventional Boolean logic elements more
closely. For Muller C-Elements, or THmm gates, delay and area increase with m,
and due to limitations on the number of series transistors, even gates with small m
values can grow quite large. To address acceptability, a modified, more efficient implementation for the Muller C-Element is illustrated in Figure 10.13. The delay of
the circuit in Figure 10.13 is two transistor levels, no matter the value of the input
width, m. Since the modified design methodology is primarily composed of parallel
OR connections, it is not limited by the number of series transistors. As a result, it is
significantly smaller (close to half the size) than those formed by staging up smaller
THmm gates. In Figure 10.13, only the version with the semi-static output is shown;
however, it should be noted that there is also a cross-coupled sense-amplifier version
with one additional transistor.

**10.5.2.1** **Improved Muller C-Element Operation**

The main component of the asynchronousNCL register feedback circuit is the Muller
C-Element, or in NCL notation, the THmm gate. To initialize the THmm gate in
Figure 10.13, all m inputs should be reset to null, Vss, which resets or initializes the
output Z to a null start state. With Z reset to null, Zb will be initialized to data, which
is desired for the register feedback circuit. As the inputs start changing to data, the
semi-static output network holds the Z value at null until all inputs are set to data.

**236** Advances in Hardware Design for Security and Trust

**Figure 10.13** Area-efficient THmm Muller C-Element for large values of m [26].

Once they are all set to data, the output is set to data, and the output will hold the
data value until all m inputs are again reset to null. Then, the process repeats.

**10.5.2.2** **Improved Muller C-Element Implementation and Analysis**

The Muller C-Element shown in Figure 10.13 is a form of transistor-resistor logic.
When all I j inputs are reset to null, all of the m p-type CMOS transistors in the reset
to null subcircuit are “ON,” but more important, all m n-type transistors in the set
to data subcircuit are “OFF.” In addition to all m n-type transistors being “OFF,” at
least one of the two Zb transistors in the reset to null or set to data subcircuits will
be “ON.” (This is because Zb must be Vdd or Vss, so either the p-type or the n-type
transistor will be “ON.”) With one of the Zb transistors “ON,” X will be pulled up
to Vdd since there is no path to Vss. With X pulled up to a strong Vdd, the n-type
transistor in the write network will be “ON,” and Z will be pulled down to Vss. A
null value will be written to Z and stored in the cross-coupled inverters that make up
the semi-static output network.

While in the null output state, as the I j inputs transition to data, some of the m
p-type transistors in the reset to null subcircuit and some of the m n-type transistors
in the set to data subcircuit will be “ON.” With some of both subcircuit’s transistors
“ON,” X will be pulled up to a strong Vdd and Y will be pulled down to a strong
Vss. In this case (output Z reset to null or Vss), Zb will be at a data or Vdd value.

Side-Channel Attack Avoidance and Mitigation **237**

This causes the Zb transistor in the reset to null subcircuit to be “ON,” and creates
a resistive path between Vdd and Vss. It is important to minimize the power draw
during this transition by making the channel resistance in Zb as large as is acceptable.
The trade-off is that larger resistance slows down the transition of X from Vdd to Vss
during the output, Z, transition from null to data.

However, when all I j inputs are set to data, all of the m n-type CMOS transistors in
the set to data subcircuit are “ON,” but more important, all m p-type transistors in the
reset to null subcircuit are “OFF.” In addition to all m p-type transistors being “OFF,”
at least one of the two Zb transistors in the reset to null or set to data subcircuits will
be “ON.” With one of the Zb transistors “ON,” Y will be pulled down to Vss since
there is no path to Vdd. With Y pulled down to a strong Vss, the p-type transistor in
the write network will be “ON,” and Z will be pulled up to Vdd. A data value will
be written to Z and stored in the cross-coupled inverters that make up the semi-static
output network.

It should be noted that during the quiescent state (all I j inputs are either null or
data), there is no path between Vdd and Vss, so power draw is minimized. When the
I j inputs change back to all null values, the output Z will switch back to null, and the
process will repeat.

The big advantage of the Muller C-Element described here is that it requires just
a few more than half the transistors of the staged Muller C-Elements. In addition,
due to the parallel-OR connections, it works for large numbers of inputs with only
a two transistor-level delay, so it switches very quickly. While in a quiescent state
with all data or all null values on its inputs, its power draw is minimal, but as the
inputs switch from data to null and vice versa, there is static power draw. This can be
limited by sizing for allowable channel resistance in the Zp transistors of the reset to
null and set to data subcircuits.

**10.6** **CONCLUSION**

In this chapter, we addressed one approach to mitigate SCAs: asynchronous design
using NCL logic. The basic techniques demonstrated here are by no means comprehensive. The material is suitable for a one-week topic in a survey course. After a
condensed overview, we described contemporary limitations to the approach, and we
detailed some of the techniques developed through our research. By leveraging nonconventional transistors in CMOS design, the data path, hybrid cell approach has
shown significant reduction in the area required to implement asynchronous circuits.
Additionally, the Muller C-Element shows both improved throughput as well as a
significant reduction in area, especially for Muller C-Elements with large numbers
of input bits.

**REFERENCES**

1. L. Lin, W. Burleson, and C. Parr. Moles: Malicious off-chip leakage enabled by sidechannels. In IEEE/ACM International Conference on CAD (ICCAD), pages 117–122.
IEEEACM, November 2009.

**238** Advances in Hardware Design for Security and Trust

2. P. Kocher, J. Jaffe, and B. Jun. Differential power analysis. In Annual International
Cryptology Conference, pages 388–397. Springer, 1999.
3. S Yang, P. Chakraborty, and S. Bhunia. Side-channel analysis for hardware Trojan detection using machine learning. In IEEE International Test Conference India (ITC India),
pages 1–6. IEEE, July 2021.
4. M. Tehranipoor and F. Koushanfar. A survey of HW Trojan taxonomy and detection. In
IEEE Design & Test of Computers, pages 10–25. IEEE, 2010.
5. T. Hu, L. Wu, X. Zhang, and Z. Liao. Hardware Trojan detection combines with machine learning: An isolation forest-based detection method. In IEEE 14th International
Conference on Big Data Science and Engineering (BigDataSE), pages 96–103. IEEE,
2020.
6. C. He, B. Hou, L. Wang, Y. En, and S. Xie. A novel hardware Trojan detection method
based on side-channel analysis and PCA algorithm. In International Conference on
Reliability Maintainability and Safety (ICRMS), pages 1043–1046. IEEE, 2014.
7. S. Moore, R. Anderson, P. Cunningham, R. Mullins, and G. Taylor. Improving smart
card security using self-time circuits. In Proceedings of the Eighth International Symposium on Asynchronous Circuits and Systems, pages 211–218. IEEE, 2002.
8. R. Sridhar. Asynchronous design techniques. In Proceedings of the Fifth Annual IEEE
International ASIC Conference, pages 296–300. IEEE, September 1992.
9. K. Fant and S. Brandt. Null convention logic: A complete and consistent logic for
asynchronous digital circuit synthesis. In Proceedings of the International Conference
on Application Specific Systems, Architectures and Processors, pages 261–273. IEEE,
August 1996.
10. S. C. Smith. Completion-completeness for null convention digital circuits utilizing the
bit-wise completion strategy. In 2003 International Conference on VLSI, pages 143–
149. IEEE, June 2003.
11. B. Shakya, T. He, H. Salmani, D. Forte, S. Bhunia, and M. Tehranipoor. Benchmarking
of hardware Trojans and maliciously affected circuits. Journal of Hardware and Systems
Security, 1(1):85–102, 2017.
12. S. Bhunia, M. S. Hsiao, M. Banga, and S. Narasimhan. Hardware Trojan attacks: Threat
analysis and countermeasures. In Proceedings of the IEEE, pages 1229–1247. IEEE,
August 2014.
13. K. Xiao, X. Zhang, and M. Tehranipoor. A clock sweeping technique for detecting
hardware Trojans impacting circuits delay. IEEE Design & Test, 30(2):26–34, 2013.
14. J. J. Fournier, S. Moore, H. Li, R. Mullins, and G. Taylor. Security evaluation of asynchronous circuits. In Cryptographic Hardware and Embedded Systems, pages 137–151.
Springer, 2003.
15. M. Forsberg, T. Johansson, W. Liu, and M. Vellaikal. A shallow and deep trench isolation
process module for rf bicmos. Journal of The Electrochemical Society, 151(12):G839–
G846, 2004.
16. J. Wu. Dissertation: Null convention logic applications of asynchronous design in nanotechnology and cryptographic security. Missouri S&T, 2012.
17. K. Bandapati and S. C. Smith. Design and characterization of null convention arithmetic
logic units. In Mircoelectronic Engineering, pages 280–287. Elsevier, February 2007.
18. S. C. Smith. Speedup of self-timed digital systems using early completion. In The IEEE
Computer Society Annual Symposium on VLSI, pages 107–113. IEEE, April 2002.
19. D. E. Muller and W. S. Bartky. A theory of asynchronous circuits. In Proceedings of
the International Symposium on Theory of Switching, Part 1, pages 204–243. Harvard
University Press, 1959.

Side-Channel Attack Avoidance and Mitigation **239**

20. D. E. Muller. Theory of asynchronous circuits. In Rep. no. 66, Digital Computer Lab.
University of Illinois at Urbana-Champaign, 1955.
21. S. M. Nowick and M. Singh. Asynchronous design part 1: Overview and recent advances. In IEEE Design & Test, pages 5–18. IEEE, June 2015.
22. A. Branover, R. Kok, and R. Ginosar. Asynchronous design by conversion: Converting
synchronous circuits into asynchronous ones. In Proceedings Design, Automation and
Test in Europe Conference and Exhibition, pages 870–875. IEEE, March 2004.
23. J. M. Emmert, A. Perumalla, T. Hudson, and L. Concha. Thx2 programmable logic
block architecture for clockless asynchronous fpgas. In IEEE Transactions on Circuits
and Systems I (TCAS-I), pages 2906–2915. IEEE, 2022.
24. D. Phillips, P. Chen, and J. M. Emmert. Area efficient asynchronous circuits for side
channel attack mitigation. In IEEE International Conference on Computer Design
(ICCD-22), pages 565–571. IEEE, October 2022.
25. D. Phillips, P. Chen, and J. M. Emmert. Datapath cells for null convention logic asynchronous circuit area reduction. In IEEE National Aerospace & Electronics Conference
(NAECON)-21, pages 400–404. IEEE, August 2021.
26. J. M. Emmert and S. VanDewerker. EMC: Efficient Muller C-element implementation
for high bit-width asynchronous applications. In IEEE Mid-West Symposium on Circuits
and Systems (MWSCAS), pages 816–819. IEEE, August 2021.
27. J. M. Emmert, A. Perumalla, and L. Concha. An asynchronous FPGA THx2 programmable cell for mitigating side-channel attacks. In IEEE Mid-West Symposium on
Circuits and Systems (MWSCAS), pages 840–843. IEEE, August 2020.
28. John M. Emmert. US patent 11886622: Systems and methods for asynchronous programmable gate array devices. In USPTO, 2024.
29. John M. Emmert. US patent application 18265593: Efficient Muller C-element implementation for high bit-width asynchronous applications. In USPTO, 2024.
30. J. M. Emmert and A. Perumalla. Us provisional patent 63346711: Area efficient asynchronous circuit generator. In USPTO, 2022.
31. S. Semba and H. Saito. Comparison of RTL conversion and GL conversion from synchronous circuits to asynchronous circuits. In IEEE International Symposium on Circuits and Systems (ISCAS), pages 1–4. IEEE, 2019.
32. H. Park and T. Kim. Synthesizing asynchronous circuits toward practical use. In Proceedings - IEEE Computer Society Annual Symposium on VLSI (ISVLSI), pages 47–52.
IEEE, July 2016.
33. Z. Xia, S. Ishihara, M. Hariyama, and M. Kameyama. Dual-railsingle-rail hybrid logic
design for high-performance asynchronous circuit. In IEEE International Symposium
on Circuits and Systems (ISCAS), pages 3017–3020. IEEE, 2012.
34. C. F. Brej. An automatic synchronous to asynchronous circuit convertor. In Proceedings
11th UK Asynchronous Forum, 2001.
35. Y. A. Stepchenkov. RU patent 2371842: H flip-flop. In Rospatent FSIP, 2009.
36. S. Fairbanks. WO patent 0122591 A1, two-stage Muller C-element, march. In WIPO,
2001.
37. S. L. Lu. Improved design of CMOS multiple-input Muller C-elements. In Electronics
Letters, pages 1680–1682. IEE, 1993.
38. S. Hauck. Asynchronous design methodologies: An overview. In Proceedings of the
IEEE, pages 69–93. IEEE, 1995.

# 11 Is ARM’s TrustZone
### Trustable for Confidentiality Protection?

Tianhong Xu and Yunsi Fei

Advanced RISC Machine (ARM)’s TrustZone is a hardware-based trusted execution environment (TEE), prevalent in mobile devices, IoT edge systems, and autonomous systems. Within TrustZone, security sensitive applications reside in a
hardware-isolated secure world protected from the normal-world’s applications, OS,
debugger, peripherals, and memory. However, microarchitectural side-channel vulnerabilities have been discovered on shared on-chip resources, such as caches and
branch prediction unit (BPU), mostly on X86 processors. As each TEE has specific
implementations and resource management mechanisms, side-channel vulnerabilities of TrustZone that result in confidentiality breach are largely under-explored. We
investigate a performance-optimizing microarchitectural unit, pattern history table,
and evaluate its vulnerability. We develop important primitives for cross-world sidechannel attacks that can leak the complete control flow of any application in the
secure world. We also propose several countermeasures against such microarchitectural side-channel attacks targeting TrustZone.

**11.1** **INTRODUCTION**

With ever-increasing requirements for security and trust of running applications,
many modern CPUs are companioned with a trusted execution environment (TEE).
By executing security-sensitive applications in an isolated environment, such as secure enclave or secure world, TEEs dedicate separate resources to the secure applications and disallow access by untrusted applications or even OS from the rest of
the system (usually called host or normal world) [1]. TEEs can protect the confidentiality of valuable code and data as well as integrity of the system. Intel’s Software
Guard Extensions (SGXs) and ARM’s TrustZone are two common TEEs that are
widely used in modern computing systems, while Intel has discontinued the support
for SGX on client machines from its 12th-generation cores. ARM’s TrustZone remains the most popular TEE found in billions of mobile systems, edge, and internetof-things (IoT) devices. In TrustZone, the secure world and normal world are two

[DOI: 10.1201/9781003510949-11](https://doi.org/10.1201/9781003510949-11) **240**

Is ARM’s TrustZone Trustable for Confidentiality Protection? **241**

software worlds with separate hardware components and access mechanisms, including debugger, peripherals, and memory.

However, recent research demonstrated that TEEs are vulnerable to microarchitectural side-channel attacks [2–6], as many on-chip microarchitectural units are
shared across the worlds, including caches and branch prediction units (BPUs).
Through shared resources, an adversary in the normal world can glean details of
a critical application in the secure world, breaking the confidentiality protection provided by the TEE.

In this chapter, we provide a comprehensive framework for side-channel attacks
targeting TEEs. We start with introducing essential background on TEEs, including their features and implementations. We then present a general framework for
side-channel attacks against TEEs, outlining the key components and strategies that
can be employed to exploit shared microarchitectural resources. To demonstrate the
practical application of this framework, we introduce TrustZoneTunnel [7], a novel
microarchitectural side-channel attack targeting the branch prediction unit of ARM
systems with TrustZone. TrustZoneTunnel exemplifies how the general attack principles can be adapted and implemented to exploit vulnerabilities with a specific microarchitecture under ARM’s TrustZone. The general attack process includes identifying vulnerable microarchitectural components, developing attack primitives, and
constructing a complete attack that can leak sensitive information from the secure
world to the normal world. By presenting both the general framework and a specific implementation, we aim to provide readers with a deep understanding of the
potential vulnerabilities in TEEs and the methodologies used to exploit them. This
approach not only highlights the current security challenges facing TEEs but also
offers insights into potential countermeasures and future research directions for TEE
security.

**11.2** **BACKGROUND ON TRUSTED EXECUTION ENVIRONMENTS**

**11.2.1** **GENERAL TEE CONCEPTS**

TEEs represent a significant advancement in computer security architecture, designed to provide a secure and isolated execution space within a larger computing
system on many modern CPUs. The fundamental concept of a TEE is to partition resources of a hardware platform for a ’normal world’ and a ’secure world’, and create
isolated execution environments on such resources. By running security-sensitive applications in a secure enclave or secure world, isolated from the normal world (host),
TEEs dedicate separate resources to the secure applications and disallow access by
untrusted applications or even OS from the rest of the system. TEEs can protect the
confidentiality of valuable code and data as well as integrity of the system.

Key features of TEEs include:
Isolation: TEEs provide hardware-backed isolation of execution environments,
ensuring that processes running in the secure world are protected from potential
threats in the normal world.

Secure Storage: TEEs often include mechanisms for securely storing sensitive
data, protecting it from unauthorized access even if the main system is compromised.

**242** Advances in Hardware Design for Security and Trust

Secure Boot: Many TEE implementations ensure the integrity of the secure world
through a secure boot process, verifying each component of the boot chain.

Attestation: TEEs typically provide mechanisms to prove their authenticity and
integrity to remote parties, enabling trust in distributed systems.

Secure I/O: Some TEE implementations offer secure paths for input and output,
protecting sensitive data from interception during user interaction.

The intended protections of TEEs aim to safeguard the confidentiality and integrity of code and data in the secure world, even in the presence of a compromised
operating system or malicious software in the normal world.

**11.2.2** **TEE IMPLEMENTATIONS**

Several implementations of TEEs exist in modern computing systems, each with its
unique characteristics and target platforms.

Intel’s Software Guard Extensions (SGXs): Intel’s SGX consists of a set of
security-related instructions built into some Intel CPUs. Introduced in 2015, SGX
allows user-level code to allocate private regions of memory, called enclaves, which
are protected from processes running at higher privilege levels, including the operating system and hypervisor. SGX is designed primarily for cloud computing scenarios, allowing sensitive computations to be performed on untrusted remote platforms.
It provides a ‘reverse sandbox’, protecting applications from a potentially malicious
host system.

Key features of SGX include:

1. Memory encryption: SGX uses a hardware-based memory encryption engine to protect enclave data.
2. Attestation: SGX provides mechanisms for remote attestation, allowing a
remote party to verify the integrity of an enclave.
3. Sealing: SGX enables secure data storage outside the enclave through a
process called sealing.
4. Dynamic memory management: Later versions of SGX allow for dynamic
increase of enclave memory.

SGX has been widely adopted in various applications, including secure multiparty computation, protected audio/video playback, and secure key storage. However, Intel has discontinued SGX support for client systems from its 12th-generation
processors onwards, focusing its application more on server and cloud environments.

ARM’s TrustZone: ARM’s TrustZone is a security technology integrated into
ARM processors, widely used in mobile devices, IoT systems, and embedded applications. TrustZone creates two separate worlds – the Normal World and the Secure
World - with hardware-enforced isolation between them. It provides a full-system
approach to security, extending its protection to memory, software, bus transactions,
interrupts, and peripherals.

Since its introduction in 2004 with the ARMv6 architecture, ARM’s TrustZone
technology has been a key security feature in the ARM processor family. As the
most popular TEE, TrustZone has been adopted in billions of lightweight devices to
protect both confidentiality and integrity of sensitive code and data. With TrustZone,

Is ARM’s TrustZone Trustable for Confidentiality Protection? **243**

on the same processor the secure world has its dedicated hardware resources and
peripherals, ensuring sensitive data and applications to operate in a trusted environment, isolated from the regular operation modes in the normal world.

Starting from the Cortex-A8 architecture, the TrustZone technology has seen significant advancement. The Cortex-A53 processor, which has been the most widely
adopted processor model in smartphones since 2014 until 2017, and is still commonly used in game consoles and embedded devices at present, embodies TrustZone
features including robust isolation for secure data handling, integrated cryptographic
support for enhanced data protection, and secure boot functionality for verified software execution.

Other TEE Implementations: Besides Intel’s SGX and ARM’s TrustZone, there
are other TEE implementations tailored for specific platforms or use cases.

AMD Secure Encrypted Virtualization (SEV) [8]: Designed for virtualized environments, SEV provides encryption of virtual machine memory to protect against hypervisor attacks. It includes features like Secure Encrypted Virtualization-Encrypted
State (SEV-ES) and Secure Nested Paging (SEV-SNP) for enhanced protection.

RISC-V MultiZone Security [9]: An open-source TEE for RISC-V processors
offers a lightweight and customizable security solution for embedded systems. It
provides isolated execution environments without the need for a separate security
co-processor.

Google’s Titan M [10]: A custom-built security chip used in Google Pixel phones
and Chromebooks. It handles sensitive data and operations, such as Verified Boot,
on-device encryption, and secure transactions.

Microsoft’s Pluton [11]: A security processor design that Microsoft has developed
in collaboration with AMD, Intel, and Qualcomm. It aims to bring Xbox-like security
to Windows PCs, integrating directly into the CPU to protect against physical attacks
and firmware vulnerabilities.

These diverse implementations highlight the growing importance of hardwarebacked security solutions across various computing platforms, from mobile devices
to IoT systems and cloud servers. Each implementation offers unique features and
trade-offs, catering to different use cases and security requirements in the evolving
landscape of cybersecurity.

**11.3** **MICROARCHITECTURAL SIDE-CHANNEL ATTACKS ON TEEs**

**11.3.1** **CONCEPT AND THREAT TO TEEs**

TEEs are designed to provide a secure and isolated execution space for sensitive
applications. However, despite the logical isolation and security guarantees offered
by TEEs, certain microarchitectural components remain shared between the secure
and normal worlds for performance and efficiency reasons. This sharing of hardware
resources creates potential vulnerabilities that can be exploited through microarchitectural side-channel attacks.

Common shared microarchitectural components focus on performance optimization, and lack security considerations.

Caches: As the cache hierarchy has multiple levels, including L1, L2, and often L3 (last-level) caches, some levels may still be shared in TEEs. In ARM’s

**244** Advances in Hardware Design for Security and Trust

TrustZone, while the L1 cache can be partitioned between the secure and normal
worlds, the L2 cache and beyond are usually shared. This sharing allows for higher
utilization of cache resources but also opens up possibilities for cache-based sidechannel attacks, where an attacker can infer secure-world data activities through
observing cache/memory access patterns.

Branch Prediction Unit (BPU): The branch predictor is often shared across
worlds to maintain high performance in both secure and normal operations. This
unit includes components like the branch target buffer (BTB) and pattern history table (PHT). Sharing the BPU allows for efficient branch prediction across worlds but
can lead to information leakage on the program control-flow of the secure world, as
the buffer or table states for branch prediction can persist across world transitions.

Translation Lookaside Buffer (TLB): TLBs are frequently shared resources between the secure and normal worlds for efficiency. Shared TLBs can speed up address translation after world switches but may leak information about memory access
patterns in the secure world through timing differences in TLB hits and misses.

Microarchitectural side-channel attacks exploit these shared resources to leak sensitive information from the secure world to the normal world. An attacker operating
in the normal world can manipulate these shared hardware resources and observe
their state changes to infer secret information about processes running in the secure
world, e.g., extract cryptographic keys, infer the control flow of secure applications,
or reconstruct sensitive data processed within the secure world. Microarchitectural
side-channel attacks undermine the confidentiality guarantees that TEEs are designed
to provide. Understanding and mitigating these microarchitectural side-channel attacks is crucial for maintaining the integrity and confidentiality promises of TEEs.
As TEEs become more prevalent in various computing environments, from mobile
devices to cloud servers, the importance of addressing these vulnerabilities grows
correspondingly.

**11.3.2** **EXISTING ATTACKS ON TEEs**

Microarchitectural side-channel attacks on TEEs have been extensively studied, revealing numerous vulnerabilities in both Intel’s SGX and ARM’s TrustZone platforms. On both systems, microarchitectural side-channel attacks start with exploiting
caches, and then extend to other components, such as BPU and page table.

Cache-based attacks have been a primary focus of microarchitectural attacks.
G¨otzfried et al. [12] demonstrated prime+probe techniques to extract sensitive information from SGX enclaves through cache timing analysis. Lapid et al. [13] then
showed cache attacks on ARM’s TrustZone.

The BPU has been another major target. On Intel systems, BTB-based attacks
were first introduced by Acıc¸mez et al. [14, 65], exploiting the shared BTB to infer a victim application’s control flow and confidential data. More recently, attacks
targeting the PHT have emerged, such as BranchScope by Evtyushkin et al. [16]
and BlueThunder by Huo et al. [3]. On ARM systems, the hardware-backed Heist
attack by Ryan [6] implemented a BTB-based attack on TrustZone. Other attack
vectors have also been explored. Chen et al. [17] introduced SGXPectre, combining

Is ARM’s TrustZone Trustable for Confidentiality Protection? **245**

speculative execution with page table side channels to extract secrets from SGX enclaves. Wang et al. [18] demonstrated how carefully crafted interface calls could be
used to leak information from SGX enclaves. In these cross-world/enclave attacks,
the OS is not trusted and the attacker can have kernel-privilege but still cannot access the secure hardware protected by the TEE. With the shared microarchitecture
for which applications in both worlds can set the state and also monitor the change,
the attacker in the normal world can bypass the protection of the secure world and
retrieve critical information about the victim application.

In response to these attacks, both hardware and software countermeasures have
been proposed. For cache-based attacks, hardware-level solutions include cache partitioning techniques like Intel’s Cache Allocation Technology (CAT) [19], which
isolates cache resources between different security domains. On the software side,
constant-time programming techniques [20] aim to eliminate timing variations in
cryptographic operations, while dynamic software diversity approaches [21] randomize memory layouts to thwart attackers. For BPU-based attacks, the countermeasures include a hardware-level mechanism to partition BTB entries among processes [22] and a compiler-assisted protection in Half&Half [23], both adopting the
principle of isolation.

It is worth noting that majority of the prior attacks and countermeasures target
Intel systems, with comparatively fewer addressing ARM architectures. This oversight is significant given the substantial differences between ARM’s and Intel’s BPU
and TEE designs. The only notable BPU-based attack on ARM’s platforms was the
hardware-backed Heist [6] that implemented a BTB-based attack, while PHT-based
attacks on ARM’s TrustZone were unexplored prior to recent work. Our work, TrustZoneTunnel, contributes to this body of research by introducing the first PHT-based
side-channel attack specifically targeting ARM’s TrustZone. This attack demonstrates that the PHT can be exploited to leak sensitive information from the secure
world to the normal world in ARM’s TrustZone environments, further highlighting
the ongoing challenges in securing TEEs against microarchitectural side-channel attacks.

**11.3.3** **GENERAL FRAMEWORK FOR MICROARCHITECTURAL**
**SIDE-CHANNEL ATTACKS ON TEEs**

We summarize the process of developing a microarchitectural side-channel attack on
TEEs, with three main steps described in the following.

**11.3.3.1** **Identifying and Analyzing the Target Microarchitecture**

The first step in launching a successful microarchitectural side-channel attack involves identifying the specific microarchitectural component that can be exploited,
and thoroughly understanding its structure, parameters, and working mechanisms.

Literature Review and Documentation Study: Conducting a thorough review
of the literature and available technical documentation is the first step in analyzing the microarchitecture. The attacker must gather and study all relevant resources
related to the target processor’s architecture, including technical manuals, research

**246** Advances in Hardware Design for Security and Trust

papers, and online resources. This step is crucial for forming a foundational understanding of the expected behavior of the target component, identifying potential
vulnerabilities, and learning about existing countermeasures.

The review is not limited to official documentation provided by the processor’s
manufacturer but also includes academic research and open-source contributions
from the community. These resources offer insights into the design principles of
the target architecture, the operational modes of key components, and any known
security and privacy concerns. However, existing public materials often lack detailed
descriptions of certain critical mechanisms, particularly those related to performance
optimizations and microarchitecture implementation details. While literature review
provides a solid starting point, further investigation is often required to fill in the gaps
left by these documents.

Reverse Engineering: When critical details are not publicly available, reverse
engineering becomes an essential tool. The purpose of reverse engineering is to infer with the internal working mechanisms of the hardware through experimentation
and analysis, which is particularly important for microarchitectural attacks. In the
absence of complete documentation, the attacker must first explore and understand
the hardware’s behavior by constructing and running microbenchmarks.

Microbenchmarks are carefully designed small programs that stress specific parts
of the microarchitecture. By using microbenchmarks, the attacker can precisely control inputs such as the branch history or memory access patterns and observe how
the microarchitectural component responds through side channels such as timing or
power consumption. This approach allows the attacker to deduce the internal state
changes and operational mechanisms of the component. For example, when analyzing a complex PHT, microbenchmarks can help determine which bits are used
for indexing PHT and the role of the Global History Register (GHR) in branch
prediction.

Reverse engineering is not only about hypothesizing the behavior of a component
but also about validating these hypotheses. In practice, this often means iteratively
adjusting microbenchmarks and conducting extensive experiments to ensure the accuracy of the understanding. Through this iterative process, the attacker can progressively uncover the microarchitecture’s working mechanisms, ultimately providing
the critical technical foundation needed for attack design.

In our research, we successfully revealed the PHT indexing mechanism in the
ARM Cortex-A53 processor through carefully designed microbenchmarks. This process not only enhanced our understanding of the target architecture but also provided
the crucial technical support needed to implement the TrustZoneTunnel attack.

**11.3.3.2** **Designing the Attack Mechanism**

Once the target microarchitecture is understood, the next step is to design the attack
mechanism. This process focuses on developing the appropriate techniques to exploit
the microarchitecture.

Microarchitectural Side-Channel Techniques: A microarchitectural sidechannel attack is typically composed by three key phases: the attacker first sets the

Is ARM’s TrustZone Trustable for Confidentiality Protection? **247**

microarchitectural state; then allows the victim to execute with the activities affecting the state; and finally, the attacker checks the microarchitectural state change to
infer the victim’s activities. These common phases are fundamental to various microarchitectural side-channel attacks.

In cache-based attacks, two commonly used methods are Flush+Reload and
Evict+Time. Flush+Reload involves the attacker flushing a shared memory line from
the cache and then monitoring how long it takes to reload it. If the victim accesses
the memory line in between, it will be reloaded into the cache, and the attacker can
detect the “hot” status of the cache line during the Reload stage by measuring the
access time. This method is highly effective in environments where the attacker and
victim share memory, such as shared libraries. On the other hand, Evict+Time relies
on the attacker evicting a certain data/cache line with other memory loads that index into the same cache set, and then measuring how long it takes for the victim to
access the data. By analyzing the timing differences, the attacker can infer whether
the victim has used this cache line or not. Although this method is less precise than
Flush+Reload, it is applicable to broader scenarios where the two parties do not share
memory.

Beyond cache attacks, a more generalized technique known as Prime+Probe is
widely employed. In this approach, the attacker first ‘primes’ the entire microarchitectural component by filling it with their own data. The victim then executes, potentially altering the state of the microarchitecture. Finally, the attacker ‘probes’ the
component to check whether the victim’s actions have affected the attacker’s data,
typically by measuring access times. This approach is applicable to a broader range
of microarchitectural components beyond caches, such as branch predictors.

World Switching Mechanism: In attacks targeting TEEs such as ARM’s TrustZone and Intel’s SGX, precise control over the world switching is critical, as normally the victim code is placed inside the enclave or the secure world for protection.
The attacker needs to alternately execute their own code (often in the normal world
or host) and the victim’s code in a controlled sequence to extract secret information. For instance, in Intel’s SGX, the SGX-Step [24] technique allows the attacker
to interrupt enclave execution with fine granularity, enabling precise monitoring of
the victim’s influence on shared microarchitectural components. The timing resolution is also important, and hardware features like CPU performance counters can be
leveraged to achieve the necessary measurement precision.

In the context of ARM’s TrustZone, the Load-Step [4] mechanism is used for
high-resolution switching between the attacker’s normal world and the victim’s
secure-world execution. This method is implemented as a Linux kernel driver, which
customizes interrupt handler functions to embed the attacker’s code within the
context-switching process. The Load-Step mechanism allows switching at the granularity of individual instructions, enabling the attacker to monitor the exact impact
of the secure-world operations on shared microarchitectural components.

Figure 11.1 shows the procedure of the Load-Step world-switching mechanism. It
involves using an auxiliary control core to manage the timing of interrupts. This core
sets a timer, and when the timer expires, it signals the generic interrupt controller
(GIC) to generate a cross-core interrupt. This interrupt forces the victim core to save

**248** Advances in Hardware Design for Security and Trust

**Figure 11.1** Process of Load-Step

its secure-world context and switch to the normal world, where the attacker’s code
executes during the interrupt handling. After this, control returns to the auxiliary
core, which resets the timer for the next round of attacks. This fine-grained control
is crucial for aligning the attacker’s observations with the victim’s execution phases,
enabling the attacker to extract information with high precision.

In summary, designing the attack mechanism involves carefully selecting and
implementing microarchitectural side-channel techniques, such as Flush+Reload,
Evict+Time, and Prime+Probe, alongside precise world-switching mechanisms like
SGX-Step and Load-Step. These components work together to create a robust framework for extracting sensitive information from TEEs, demonstrating the vulnerabilities that exist even in ostensibly secure environments.

**11.3.3.3** **Selecting the Target Application**

The final step in designing a microarchitectural side-channel attack is to identify a
suitable target application running in the secure world. The choice of target often
hinges on the specific microarchitectural component being exploited and the type of
information the attacker aims to extract. Common security-sensitive target applications include:

Cryptographic Algorithms: Cryptographic implementations, such as RSA and
AES, are frequent targets in microarchitectural side-channel attacks due to their
widespread use in secure communications and the critical nature of the secrets they
process. Attacks on RSA often focus on extracting the private key-bits by targeting the operations involved in modular exponentiation. For instance, side-channel
attacks can monitor the execution time or cache access patterns during the modular
exponentiation process, revealing the bits of the private key.

Similarly, AES implementations, particularly those using T-tables (lookup tables
for precomputed values), are vulnerable to side-channel attacks that exploit cache
access patterns. In a typical cache attack, the attacker can observe which cache lines
are accessed during encryption and derive the T-table usage, allowing them to reconstruct the secret key. The Flush+Reload technique is particularly effective against
AES, where the attacker flushes specific cache lines and monitors when the victim
reloads these lines during encryption, revealing the key-dependent accesses directly.

Machine Learning Models: As machine learning (ML) applications are increasingly deployed in secure enclaves to protect sensitive data and intellectual property,

Is ARM’s TrustZone Trustable for Confidentiality Protection? **249**

they have become attractive targets for microarchitectural side-channel attacks. One
prominent example is the model extraction attack, where the attacker aims to steal a
functionally equivalent copy of a deployed deep neural network (DNN) model.

Such attacks typically target the layers of the model that involve conditional operations, such as ReLU activations or branches in decision trees. By carefully monitoring the execution of these operations, attackers can infer the weights and biases of the
model. For instance, by using techniques like Prime+Probe, an attacker can monitor
cache usage patterns during the forward pass of a neural network, allowing them to
reconstruct the model’s parameters. In more sophisticated attacks, the attacker might
also exploit the timing of specific operations, like matrix multiplications, to gather
information about the model’s structure and parameters.

Attacks on machine learning models are particularly concerning because they can
lead to the complete theft of proprietary models, undermining the security and privacy guarantees of the enclave. These attacks are not limited to simple models; they
can extend to complex DNNs used in applications like image recognition or natural
language processing. The TrustZoneTunnel attack, for example, demonstrates how
side-channel techniques can be applied to extract sensitive model parameters in a
TrustZone environment, highlighting the vulnerability of ML models in TEEs.

The choice of target application depends on several factors, including the microarchitectural component being exploited, the attacker’s access level, and the nature of
the information to be extracted. Cryptographic algorithms and ML models represent
high-value targets due to their critical roles in modern computing and the sensitive
nature of the data they handle.

By following this general framework, researchers and security professionals can
systematically develop and analyze new microarchitectural side-channel attacks on
TEEs. This contributes to a deeper understanding of these vulnerabilities and the
development of more robust security measures to protect against such attacks. In
the following sections of this chapter, we will present our TrustZoneTunnel attack,
a novel microarchitectural attack that breaks confidentiality protection of ARM’s
TrustZone.

**11.4** **TRUSTZONETUNNEL:** **PATTERN** **HISTORY** **TABLE-BASED** **MI-**
**CROARCHITECTURAL SIDE-CHANNEL ATTACK**

Based on the framework for developing microarchitectural side-channel attacks on
TEEs outlined before, in this section, we delve into our TrustZoneTunnel attack,
demonstrating how the PHT in the BPU can be exploited for a cross-world sidechannel attack on ARM’s TrustZone.

This section is organized as follows. First, we reverse-engineer ARM’s BPU,
focusing on understanding the BPU’s inner workings, particularly the PHT’s indexing mechanisms. Second, we present the attack Implementation in detail,
including construction of PHT collisions and building precise world-switching
mechanisms. Finally, we explore several real-world victim applications for attacks,
where we demonstrate how TrustZoneTunnel can extract sensitive information from

**250** Advances in Hardware Design for Security and Trust

secure-world applications, including cryptographic algorithms and machine learning
models.

**11.4.1** **REVERSE-ENGINEERING ARM BPU**

To build the microarchitectural side-channel attack, we conduct thorough reverse engineering of the conditional branch predictor (CBP) of a 64-bit Cortex-A53 processor. These reverse-engineering results are crucial for constructing attack components
like collisions on specific PHT entries and manipulating PHT states.

**11.4.1.1** **Branch Prediction Unit (BPU)**

Modern processors use BPUs to speed up control flow in instruction streams. When
the instruction fetch unit (IFU) fetches a branch instruction, the BPU predicts the
direction and/or target address before the branch is resolved, filling the pipeline with
the predicted instruction for speculative execution. The BPU comprises several components, including the BTB, which predicts branch destinations, and the CBP, which
determines branch direction.

The CBP typically relies on a PHT, a multi-entry table where each entry contains a
saturation counter for direction prediction. The PHT’s index function is based on the
current branch address and the processor’s execution context, provided by a GHR.
The GHR records the history of previously executed branches, influencing the PHT
index. In modern processors, CBPs often use a TAGE (TAgged GEometric history
length) structure, which includes multiple PHTs, each associated with a different
history length, to optimize prediction accuracy across varying execution patterns.

**11.4.1.2** **An Overview of Cortex-A53’s CBP**

We experimented using a Raspberry Pi 3B+ board with a quad-core ARM CortexA53 processor and 1 GB RAM, running OPTEE. The Cortex-A53 CBP is documented to use a DHR and a 3072-entry PHT, but details like PHT indexing, DHR
size, and effective branch address bits are not documented. Our experiments revealed
that the CBP employs a TAGE structure with three PHT tables: a base table indexed
by branch addresses and two tagged tables indexed with different GHR sizes.

In a TAGE predictor, all tables are queried during prediction, but only one is
selected. We reverse-engineered the predictor selection mechanism: by default, the
predictor with the shorter GHR (T1) is chosen, but when T2 shows significantly higher
accuracy, it is selected instead.

Next, in Section 11.4.1.3, we design microbenchmarks to determine the size of
GHR for each tagged predictor. In Section 11.4.1.4, we reverse-engineer the effective
bits in a branch address for PHT indexing.

**11.4.1.3** **Measuring the Size of GHR**

Given that the PHT in Cortex-A53 has 3072 entries, we hypothesize that the GHR is
no more than 16 bits. We design a function (Listing 11.1) to access the PHT with a
target branch using a pre-set GHR.

Is ARM’s TrustZone Trustable for Confidentiality Protection? **251**

✞ ☎

1 Access_PHT(h, d){

2 **if** ((h>>15)&1) {...}

3 **if** ((h>>14)&1) {...}

4 ...

5 **if** ((h>>0)&1) {...}

6 m0=misprediction_counter();

7 **if** (d) {...} // Target branch

8 m1=misprediction_counter();

9 **return** (m1-m0);

10 }
✝ ✆
Listing 11.1: Function for accessing a PHT entry

This function has two inputs: h, a 16-bit unsigned value setting the GHR for a
target branch, and d, a one-bit direction for the target branch (1 for Taken, 0 for
Untaken). Line 8 represents the target branch, with the previous lines setting the
GHR (Lines 2–6). Each branch updates a respective PHT entry, but they likely index
different entries than the target branch due to varying addresses and global history.
The function returns the difference in misprediction counts before and after the target
branch executes, indicating whether the target branch experienced a misprediction.

Using this function, we designed a microbenchmark (Listing 11.2) to measure the
size of GHR, specifically how many bits in h contribute to the PHT lookup for the
target branch, while also gathering insights into predictor selection preferences.
✞ ☎

1 h1=value;

2 h2=h1ˆ(1<<x); // Set the x-bit different

3 m=0;

4 **for** (i=0

5 ) // Training loop

6 {

7 Access_PHT(h1, 1);

8 Access_PHT(h1, 1);

9 Access_PHT(h1, 1);

10 Access_PHT(h2, 0);

11 Access_PHT(h2, 0);

12 Access_PHT(h2, 0);

13 }

14 m += Access_PHT(h1, 1); // Testing period

15 m += Access_PHT(h1, 1);

16 m += Access_PHT(h1, 1);

17 print(m);
✝ ✆
Listing 11.2: Microbenchmark 1

In this microbenchmark, two h values, h1 and h2, differ by one bit at the x <sup>th</sup> position. If the x <sup>th</sup> bit contributes to indexing, h1 and h2 will index different entries. If
not, the target branch will index the same entry. The training loop (Lines 4–12) sets
an entry for the target branch as Taken (Lines 6–8) or Untaken (Lines 9–11). In the
testing period (Lines 13–15), we check the state of the entry indexed by h1. If indexed
into different entries, m returns 0; if the same, m returns 2 due to mispredictions.

We experimented with Microbenchmark 1, observing m as x varied from 0 to 15
with different iterations (n) in the training loop. Figure 11.2 shows changes in the
proportion of h1 and h2 indexing different entries. The results suggest three phases:

**252** Advances in Hardware Design for Security and Trust

**Figure 11.2** Percentage of different PHT entries when changing x and n

0 ≤ x ≤ 4 indicates a 5-bit GHR (s1), x ≥ 8 suggests an 8-bit GHR (s2), and 5 ≤ x ≤ 7
reflects an unstable predictor choice.

The phase between 5 ≤ x ≤ 7 highlights the selection mechanism between T1 and
T2. Initially, T1 is preferred, but as n increases, T2 becomes favored due to its higher
accuracy when T1 performs poorly. Experiments show that retraining T1 back to the
default state is faster than training T2 to take precedence, indicating the stability of
T1’s default choice. In subsequent sections, we will always train the target branch to
use T1 for prediction.

In summary, the ARM Cortex-A53 CBP comprises a base predictor table indexed
only by the branch address, a tagged table using a 5-bit GHR for indexing, and another tagged table using an 8-bit GHR.

**11.4.1.4** **Effective Bits in the Branch Address**

When determining the PHT index for a target branch, not all bits in the branch address are used; only some are effective. To identify these, we designed an advanced
PHT-accessing function that not only sets the GHR but also selects different branch
instructions to access the PHT (Listing 11.3).
✞ ☎

1 Access_PHT_Adv(h, x, d){

2 **if** ((h>>7)&1) {...}

3 ...

4 **if** ((h>>0)&1) {...}

5 **return** branchx;

6 }

7 branch[0]{

8 m0=misprediction_counter();

9 **if** (d) {...} // Target branch

10 m1=misprediction_counter();

11 **return** (m1-m0);

12 }

13 branch[1]{...}

14 ...

15 branch[4095]{...}
✝ ✆
Listing 11.3: Advanced function for specifying a branch instruction and accessing a
PHT entry

Is ARM’s TrustZone Trustable for Confidentiality Protection? **253**

**Figure 11.3** Average difference between two colliding addresses on each bit

This function adds a third parameter, x, to an 8-bit h vector and branch direction d.
We built an array, branch[4096], to generate different target branch addresses. Each
function executes a conditional branch with the same global branch history (h) and
checks for mispredictions. The experiment given in Listing 11.4 checks whether two
different target branches with the same global branch history index the same PHT
entry.
✞ ☎

1 h=value;

2 m=0;

3 **for** (i=0:100)

4 {

5 m += Access_PHT_Adv(h, x1, 1);

6 m += Access_PHT_Adv(h, x1, 1);

7 m += Access_PHT_Adv(h, x1, 1);

8 m += Access_PHT_Adv(h, x2, 0);

9 m += Access_PHT_Adv(h, x2, 0);

10 m += Access_PHT_Adv(h, x2, 0);

11 }
✝ ✆
Listing 11.4: Identifying the effective bits of a branch address

In a TAGE predictor, although each table uses a different GHR size, all tables
share the same effective branch address bits. If two target branches (x1 and x2) share
the same effective bits, they will use the same table entry, causing a PHT collision.
This microbenchmark detects such collisions by measuring m. Given the 3072-entry
PHT, collisions are inevitable among 4096 branches due to the birthday problem.

We varied x1 and x2 to select different target branches, saving addresses when a
PHT collision was detected. Figure 11.3 shows the average difference between x1
and x2 across all bits for collisions, with the x-axis representing bit positions. The
results indicate that the lower 4th to 13th bits of branch addresses are the effective
bits, with the last two bits consistently zero due to 4-byte word alignment.

**11.4.2** **ATTACK IMPLEMENTATION**

In this section, we present the detailed implementation of TrustZoneTunnel, a PHTbased side-channel attack. Building on the reverse-engineering insights from the
previous section, we demonstrate how an attacker operating in the normal world

**254** Advances in Hardware Design for Security and Trust

can exploit the PHT to infer the direction of a target branch executing in the secure
world.

**11.4.2.1** **Threat Model**

We assume the common threat model for TrustZone, where the victim is a trusted
application in the secure world and the normal world applications can only invoke it
as service. The attacker has full control of the normal world, including the operating
system. It can install external kernel modules to modify the interrupt handlers, has
the privilege to access the PMU, and is able to assign specific cores to run the adversary program. We also assume that the attacker figures out the virtual address of
a target branch, through knowledge to the source code and the binary of the victim
application.

**11.4.2.2** **Attack Overview**

TrustZoneTunnel aims to extract secrets from a victim application running in the
secure world, if the conditional branches are dependent on the secrets. Our reverseengineering results indicate that with the TAGE predictor architecture, there are three
prediction tables each of which uses a different length GHR in indexing. To avoid
unexpected switching between the three predictors, we first train the target branch
to use the tagged predictor that uses a 5-bit GHR for indexing, which is the most
reliable predictor.

TrustZoneTunnel consists of three salient parts: the PHT Preset & Check function,
world-switching, and PHT collision construction.

PHT Preset & Check mechanism: We propose a PHT Preset & Check mechanism, where we first preset the state of a PHT entry by executing a collision branch,
and then checks the state update of the entry by the victim target branch. Both the
collision branch in the normal world and the target branch in the secure world index
to the same PHT entry during execution, i.e., a collision on the PHT occurs.

World-switching: to achieve a fine-grained control on the switching between the
victim and the adversary, we implement our attack with the Load-Step framework.
As shown in Figure 11.1, the victim application is set to run on a victim core (in the
secure world), and the adversary program keeps sending interrupts to the victim core
from an auxiliary core. The interrupt handler is customized to embed the Preset &
Reset functions to operate on a common PHT entry which the victim target branch
collides with the collision branch on.

PHT collision construction: when constructing a PHT collision between the two
worlds, the target branch in the victim application is already fixed, we then set the
collision branch in the normal world to have the same values for the effective bits as
the target branch, and also set the common branch global history for them.

**11.4.2.3** **PHT Preset & Check**

We first construct a PHT_Preset() function to set the state of the 2-bit counter in
a PHT entry to a specific value. After the target branch execution, we then monitor

Is ARM’s TrustZone Trustable for Confidentiality Protection? **255**

the state update via the PHT_Check() function, and speculate the direction of the
target branch. The pseudo-code for the two functions is given in Listing 11.5. We
use an Activate_T1() function to train the CPU to use the tagged predictor table
that is indexed with the 5-bit GHR (T1). Note that to ensure the CPU consistently
utilizes T1, h needs to be 8 bits instead of 5 bits; otherwise, the other table (T2) might
still be selected occasionally.
✞ ☎

1 PHT_Preset(){

2 Activate_T1(h, x);

3 Access_PHT_Adv(h, x, 1);

4 Access_PHT_Adv(h, x, 1);

5 Access_PHT_Adv(h, x, 1);

6 Access_PHT_Adv(h, x, 0);

7 }

8 PHT_Check(){

9 m=0;

10 m+=Access_PHT_Adv(h, x, 0);

11 m+=Access_PHT_Adv(h, x, 0);

12 **return** m;

13 }
✝ ✆
Listing 11.5: PHT Preset & Check Functions

The adversary collision branch instruction is in the branch function branch[x]
(shown in Listing 11.3). In the PHT_Preset() function, we use the collision
branch to access a PHT entry with three taken and one non-taken, so as to train
the 2-bit counter in the entry to be a weak T (10). In the PHT_Check() function,
we execute the same collision branch twice with direction of non-taken, and count
how many mispredictions have occurred. We deliberately control the victim to run
the target branch between the Preset & Check functions, the m value returned by
the PHT_Check() function will leak the execution direction of the target branch,
assuming no other branches have a PHT collision with the target branch or the collision branch, i.e., no noise, and the target branch executes at most once in this piece of
code. If m=0, no misprediction occurs when executing the two non-taken, meaning
that the state of the 2-bit counter at the beginning of the PHT_Check() is either
Strong non-taken (00) or Weak non-taken (01), so the target branch must have executed as non-taken. If m=1, we can speculate that the state of the 2-bit counter start
as Weak-taken (10), implying that no target branch is executed between the Preset &
Check. If m=2, the state of the 2-bit counter should be Strong taken (11), indicating
that the target branch has been executed taken. With this method, we can build a
PHT-based side channel, and extract the direction of the target branch.

**11.4.2.4** **Implementing TrustZoneTunnel with Load-Step**

TrustZoneTunnel is implemented with the Load-Step framework, as shown in
Figure 11.1, where the world-crossing interrupt handler is prefixed with a
PHT_Check() function, to detect the impact of the prior execution of the victim
application (possibly one target branch) in the secure world, followed by Interrupt
Handler and Context Recovery, before a PHT_Preset() function, to set the target

**256** Advances in Hardware Design for Security and Trust

entry in the PHT to a known state before the victim core resumes the secure-world
application. The Load-Step framework is installed in the Linux OS as an external
kernel module. For the adversary program on the auxiliary core, it starts a timer
once the TEE OS is activated. When the timer is up (after a fixed time interval), an
interrupt signal is sent to the victim’s core, forcing the secure-world application to
pause and switching to the normal world for handling the interrupt. When the routine is over, the adversarial execution returns to the auxiliary core while the victim
core is released to resume the victim application, to start the next epoch. Note the
PHT_Check() function will store its output in a trace file.

**11.4.2.5** **PHT collision construction**

To build a collision branch, we need to first obtain the address of the target branch,
and then select a branch in the normal world whose lowest fourth to thirteenth address bits are the same as the target branch. Then we need to set the context for the
target branch and the collision branch the same, i.e., setting a common branch GHR
for both branches’ execution.

For the collision branch in the Preset & Check functions, the branch global history
is easy to set to any specific value with the method shown in Listing 11.1. So the
important thing is to figure out the branch history for the target branch and then
align the collision branch with it. We assume that the attacker can always interrupt
the victim right before the target branch execution, so that the recent branch global
history of the target branch is provided by the world switching (WS) function, as
shown in Figure 11.1. We assume these operations have a fixed branch profile and
design an experiment to recover it.

We first write a simple trusted application shown in Listing 11.6, where the directions of the target branch are decided by the value of the 64-bit secret. We put
the trusted application in our Load-Step framework for experiments and adjust the
interrupt timer to make sure that the 64 iterations (each with one target branch execution shown on Line 4) can all be monitored by interrupts (with PHT Preset+Check
functions) preceding them.
✞ ☎

1 uint64_t k = secret; // secret

2 **for** (i=0;i<64;i++)

3 {

4 **if** ((k>>i)&1) //target branch

5 { ... }

6 }
✝ ✆
Listing 11.6: A simplified victim

As the number of branches in the world switching function may be less than five,
we need to complement it with more branch executions to contribute to a full controllable GHR for the target branch, and the PHT_Preset() function is therefore
extended, as shown below.

Is ARM’s TrustZone Trustable for Confidentiality Protection? **257**

**Figure 11.4** Detected PHT collisions when varying h1 in the range of 0 and 31

✞ ☎

1 PHT_Preset(){

2 ... //same with Listing 5

3 h2=0;

4 **if** ((h2>>7)&1) {...}

5 **if** ((h2>>6)&1) {...}

6 ... //Setting target GHR

7 **if** ((h2>>0)&1) {...}

8 }
✝ ✆
Listing 11.7: Extended PHT Preset Function

With this extended function, the value h1 sets the GHR for the collision branch,
while the lower part of the value h2 combined with the branch pattern of the WS
routine sets the GHR for the target branch. Both h1 and h2 have 8 bits to activate
the prediction table with the shorter GHR (5-bit), while only the least significant 5
bits contribute to PHT indexing. We first set h2 as zero and vary the other vector h1
value from 0b00000000 to 0b00011111 to find one h1 value, where PHT collisions
between the target branch and the collision branch can be detected. The results are
shown in Figure 11.4, where we calculate how many PHT collisions we can detect
on this simplified victim among different h1 values. The result shows that a PHT
collision only happens when h1=0b00000001, and a common GHR has resulted for
the collision branch and the target branch.

We design another experiment, now with h1 fixed at a value of 0b00000001 but
varying h2, to figure out the composition of the target branch GHR, i.e., how many
lower bits of GHR are contributed by the branch profile of the world switching routine, and how many upper GHR bits are contributed by part of h2. The result is given
in Figure 11.5, showing that as long as h2 is an even value, PHT collisions can be
detected. This indicates that only the last bit of h2 affects collisions, and therefore the
number of branches in the WS routine must be four, with their directions as 0b0001.
Meanwhile, from Figure 11.5 we can also observe that only when h2=0b00000 or
0b10000 can we detect all 64 PHT collisions, while when the second to fourth bits
dismatch the corresponding bits in h1, we will always miss several collisions because

**258** Advances in Hardware Design for Security and Trust

**Figure 11.5** Detected PHT collisions when varying h2 in the range of 0 and 31

the selection of the predictor T1 is unstable. In our following experiments, we still
need to consider 8 bits for the GHR, to train towards selecting the right predictor
table, while only the last 5 bits are used for PHT indexing.

With this reverse-engineering result, in attacks, the PHTPreset function only
needs to append four conditional branches, together with the WS routine, to set the
context GHR for the target branch.

**11.4.3** **MODEL EXTRACTION ATTACK OF NEURAL NETWORKS**

We next evaluate TrustZoneTunnel on real-world trusted applications.

With TrustZoneTunnel, we further propose a model extraction attack on DNNs,
where the adversary aims at stealing a function-equivalent copy of a deployed ML
model. Previous works [25, 26] apply software methods to recover the model, where
they need both the model outputs and the detailed logits when being queried in order
to perform the attack. In contrast, our attack can recover a high-fidelity model with
only the controlled inputs and the execution information leaked through our PHTbased side channel.

**11.4.3.1** **Attack Overview**

We start with a target application of a simple multi-layer perceptron (MLP), which
is composed of fully connected layers and ReLU activations, with an argmax function in the last layer. We target the branch in the ReLU activation function and the
argmax function and observe their directions through our PHT-based side channel.
We iteratively change the input and observe the direction of a chosen ReLU, until the
ReLU activation reaches a critical condition, i.e., its input is so small to be approximated as zero. We call such input a witness to the ReLU’s critical condition. The
attack is conducted in two steps:

1. Weights recovery: for the layers except for the last layer, we search for the
critical conditions for each neuron, i.e., the input to the ReLU function of
the neuron is zero. We recover the input weights of each neuron based on
many witnesses to its critical condition through linear regression.

Is ARM’s TrustZone Trustable for Confidentiality Protection? **259**

**Figure 11.6** A simple victim MLP model

2. Last-layer weight recovery: the last layer uses the argmax function instead
of the ReLU function. We search for another type of critical condition under
which two output logits are equal, and subseuqently recover the weights in
the last fully connected layer.

Next, we illustrate the attack with a sample 2 ∗ 2 ∗ 3 MLP model, which consists
of two input features, one fully connected layer with two neurons each followed
by a ReLU function, and a final layer with three neurons and an argmax function, as shown in Figure 11.6. The model is implemented with Trusted-DNN [27], a
TrustZone-based adaptive isolation strategy for DNN models.

**11.4.3.2** **Weight Recovery**

Weight recovery relies on searching for witnesses of the critical condition for each
neuron of the hidden layers. Previous work [25, 26] exploits the gradients on the
model output logits to search for witnesses, while in our attack we only use the proposed side channel without using logits, i.e., treating the model inference execution
as a black box, a more realistic attack scenario.

The implementation of the ReLU activation function is presented below, where
Line 6 is our target branch, whose direction is determined by the sign of the function’s input, essentially the output from the preceding fully connected layer. Specifically, the branch direction hinges on whether this input value exceeds zero.
✞ ☎

1 **void** relu_op_forward(nonlinear_op *op)

2 {

3 **for** ( **int** i=0; i<(op->out_units); i++)

4 {

5 op->output[i] =

6 op->input[i]>0 ? op->input[i]: 0;

7 //Target branch

8 }

9 }
✝ ✆
Listing 11.8: ReLU activation function

**260** Advances in Hardware Design for Security and Trust

For the hidden fully connected layer of the example DNN model shown in
Figure 11.6, there are two neurons, n1 and n2, with their output calculated by
Oi = Wi ∗ X + Bi, where X is the input vector {x1, x2}, Wi is the associated weight
vector {W1i,W2i}, and Bi the bias for this neuron. The neuron output will go through
the ReLU function to rectify it, where the ReLU function contains a conditional
branch, as shown in Listing 11.8. By monitoring this branch instruction using our
PHT-based side channel, the sign of the input to ReLU, Oi, is detected.

We first set the model input at zero, x1 = x2 = 0, to reveal the sign of the biases
Bi. Previous work has shown that such a model extraction attack only retrieves a
function-equipment network, with the weights and biases determined relatively, i.e.,
with a scalar multiplier [26]. We normalize the weights and biases according to the
biases, assuming Bi = 1 if it is positive; and Bi = −1 if negative.

We next search for the witness to the critical condition for each neuron. That is,
taking neuron n1 as an example, search for X that makes O1 = W11 ∗ x1 + W21 ∗ x2 +
B1 = 0. We randomly generate inputs until we find two points, X1, X2, such that their
corresponding outputs O1 have opposite signs. Then we use binary search iteratively
until we find an input X that makes O1 a small positive value, below the preset ε.
We need to find multiple witnesses to the critical condition of neuron n1, so that we
can have sufficient linear equations over the weights {W11,W21} in order to solve
them (note B1 is already known to be 1 or −1). We apply this method one by one
to other neurons in the first layer. We then apply this weight recovery process layer
by layer. For deeper layers, because the weights and biases in previous layers are
all recovered, we can set the input to the current layer to specific values for binary
searching to find the critical conditions and witnesses in a similar fashion as the first
layer.

**11.4.3.3** **Last-Layer Parameter Recovery**

The last layer of a DNN model normally utilizes argmax instead of the ReLU function to pick the highest logit. For example, for the MLP model we target, shown in
Figure 11.6, the three logits computed by the three neurons in the last layer are:

y1 = W11 <sup>2</sup>

y1 = W11 <sup>2</sup> <sup>∗</sup> <sup>FO1 +W</sup> 12 <sup>2</sup> <sup>∗</sup> <sup>FO2 +</sup> <sup>B</sup> 1 <sup>2</sup>

y2 = W21 <sup>2</sup> <sup>∗</sup> <sup>FO1 +W</sup> 22 <sup>2</sup> <sup>∗</sup> <sup>FO2 +</sup> <sup>B</sup> 2 <sup>2</sup>




y2 = W21 <sup>2</sup> <sup>∗</sup> <sup>FO1 +W</sup> 22 <sup>2</sup> <sup>∗</sup> <sup>FO2 +</sup> <sup>B</sup> 2 <sup>2</sup>

y3 = W31 <sup>2</sup> <sup>∗</sup> <sup>FO1 +W</sup> 32 <sup>2</sup> <sup>∗</sup> <sup>FO2 +</sup> <sup>B</sup> 3 <sup>2</sup>



31 <sup>2</sup> <sup>∗</sup> <sup>FO1 +W</sup> 32 <sup>2</sup> <sup>∗</sup> <sup>FO2 +</sup> <sup>B</sup> 3 <sup>2</sup>

where the FOi are the feature map outputs from the first layer, and the superscript
2 indicates it is the second layer (we will drop it in the following description for
simplicity). Since the classifier outputs the class corresponding to the highest value
among y1, y2, and y3, its classification only depends on the relative comparisons
among the three yi. Therefore, the network is functionally equivalent when the last
layer is re-parameterized as:

y <sup>∗</sup> 1




y <sup>∗</sup> 1 <sup>= 0</sup>

y <sup>∗</sup> 2 <sup>=</sup>

y <sup>∗</sup> 2 <sup>=</sup> <sup>W¯</sup> <sup>21 ∗</sup> <sup>FO1 +W¯</sup> <sup>22 ∗</sup> <sup>FO2 +</sup> <sup>B¯2</sup>

y <sup>∗</sup> 3 <sup>=</sup> <sup>W¯</sup> <sup>31 ∗</sup> <sup>FO1 +W¯</sup> <sup>32 ∗</sup> <sup>FO2 +</sup> <sup>B¯3</sup>



<sup>∗</sup> 3 <sup>=</sup> <sup>W¯</sup> <sup>31 ∗</sup> <sup>FO1 +W¯</sup> <sup>32 ∗</sup> <sup>FO2 +</sup> <sup>B¯3</sup>

Is ARM’s TrustZone Trustable for Confidentiality Protection? **261**

where W <sup>¯</sup> i1 = Wi1 −W11, W <sup>¯</sup> i2 = Wi2 −W12 and B <sup>¯</sup> i = Bi - B1 for i = 2, 3. This conversion
reduces the number of variables from nine to six. Similar to the weight recovery
process shown in Section 11.4.3.2, we just need to recover the relative parameters
while assuming B <sup>¯</sup> i as 1 or −1.

We look into the argmax function and track the conditional branches used. The
source code of argmax function is shown below.
✞ ☎

1 **void** argmax( **float** *arr, **int** n, TEE_Param  - temp)

2 {

3 ...

4 **for** ( **int** p = 0; p<n; p++)

5 {

6 **if** (arr[p]  - max) //Target branch

7 {

8 idx = p;

9 max = arr[p];

10 }

11 }

12 ...

13 }
✝ ✆
Listing 11.9: The last-layer argmax function

The source code shows that with n neurons (logits) in the last layer, there are n
comparisons, implemented as conditional branches (Line 6), to bubble sort the highest logit. The first execution of the target branch is always taken, while the second
execution compares y2 and y1, and the third execution compares either y3 and y1 or
y3 and y2, depending on the result of the second execution. Assuming the attacker
has already recovered all the previous layers and is able to set a value for FO1 and
FO2, with the critical condition setting method described in Section 11.4.3.2, we
can find witness to the critical condition of y1=y2 and y1=y3 (or y2=y3), which can be
represented by:

W¯ 21 ∗ FO1 +W¯ 22 ∗ FO2 + B¯2 = 0
W¯ 31 ∗ FO1 +W¯ 32 ∗ FO2 + B¯3 = 0
OR
(W <sup>¯</sup> 21 −W <sup>¯</sup> 31) ∗ FO1 +(W <sup>¯</sup> 22 −W <sup>¯</sup> 32) ∗ FO2 +(B <sup>¯</sup> 2 − B <sup>¯</sup> 3) = 0






With witnesses for these critical conditions found, i.e., a set of {FO1, FO2} values, the four parameters, W <sup>¯</sup> 21,W <sup>¯</sup> 31,W <sup>¯</sup> 22,W <sup>¯</sup> 32, will be solved. Note in our computation,
we do not rely on knowing the values of logits (yi), as the previous work did [26] (in
a white- or gray-box fashion), but just exploit the PHT-based side channel for weight
recovery, a complete black-box attack model for the victim application.

**11.4.3.4** **Evaluation**

We evaluate the performance of our model extraction attack on different MLP model
sizes and architectures, and also extend our attack to a CNN model: LeNet-5. We
compare the number of queries needed to recover weights of the whole network by

**262** Advances in Hardware Design for Security and Trust

our attack with the prior cryptanalytic/software model extraction work [25, 26]. We
also give the execution time of our attack, compared to the original model execution
time. The results are shown in Table 11.1.

**Table 11.1**
**Performance of the Model Extraction Attack**

Our
Queries

Model

Time

Our Attack

Time

Prior
Queries

Architecture

#of
Parameters

784-32-1 25,120 2 <sup>18.2</sup> 2 <sup>19</sup> 0.5 s 3.9 s
784-128-1 100,480 2 <sup>20.2</sup> 2 <sup>21</sup> 1.8 s 13.6 s
10-10-10-1 210 2 <sup>16</sup> 2 <sup>13</sup> 79 ms 238 ms
10-20-20-1 420 2 <sup>17.1</sup> 2 <sup>14</sup> 86 ms 517 ms
40-20-10-10-1 1,110 2 <sup>17.8</sup> 2 <sup>15</sup> 95 ms 836 ms
80-40-20-1 4,020 2 <sup>18.5</sup> 2 <sup>17</sup> 145 ms 1.7 s
Lenet-5 44,426 −−−− 2 <sup>20</sup> 265 ms 11.6 s

Note that in our attack the number of queries is linearly dependent on the number
of neurons, and not related to the number of layers. So for deeper networks, our
attack requires less queries than cryptanalytic methods. Also, the prior work does
not apply to CNN models like LeNet-5 due to high complexity, while our attack
successfully applies.

The result also shows that our attack increases the total execution time by about
tenfold for all these models, which is acceptable for performing a feasible model
extraction attack. As shown in Figure 11.1, this time overhead is due to frequent interruptions of the attack, including the customized interrupt handler and WS, where
each interruption in the attack of DNN execution causes a delay of about 15 µs.
As different victim applications use different amounts of registers and memory resources, the context saving and restoring time may vary and such interruption delays
may also vary, we set the timer interval as 2130 CPU cycles in the attack of the
sample MLP model. For DNN inference, as the execution of ReLU activations only
takes a small fraction of the time, we do not need to attack the entire network execution. We can profile the network execution and only start interruptions near the first
ReLU layer, to reduce unnecessary interruptions and therefore reduce the execution
overhead. On average, 10 interrupts are needed for one ReLU iteration.

**11.4.4** **ATTACK MITIGATIONS**

With the effectiveness of TrustZoneTunnel in extracting sensitive information from
the secure world demonstrated, it is crucial to develop corresponding mitigations
to maintain the integrity and confidentiality promises of TEEs. In this section, we

Is ARM’s TrustZone Trustable for Confidentiality Protection? **263**

discuss several mitigation strategies, ranging from general approaches to specific
techniques tailored to our attack.

One general approach to mitigating BPU-based side-channel attacks is to prevent
PHT collisions across different security domains. Half & Half [23] introduced such
a mitigation for Intel systems by partitioning conditional branch addresses between
domains with different privileges. This method effectively makes the effective bits of
branch addresses different across domains, preventing PHT collisions. However, in a
TEE setting where attackers may have OS-level privileges, such compiler-level solutions might be circumvented. An alternative strategy focuses on detecting the attack
based on its unique characteristics. Prior works [28, 29] have proposed monitoring
for frequent interrupts in a victim enclave, treating this as an anomaly indicative of
an attack. While effective, this approach may lead to performance degradation due to
the overhead of constant monitoring. Software-based mitigations have also been explored, with some approaches aiming to eliminate conditional branches in securitycritical applications [30,31]. While this can be effective, its algorithm-specific nature
limits its broad applicability across different types of applications and systems. Other
potential mitigations include flushing all counters in the PHT entries during WSs or
using separate BPUs for different worlds. These hardware-level approaches can be
effective but come with non-negligible implementation and execution overheads.

Specific to our TrustZoneTunnel attack, we propose a more targeted and efficient
mitigation strategy. As described in Section 11.4.2.5, our attack relies on aligning
the GHR seen by the collision branch with that seen by the target branch. To counter
this, we introduce dummy branch executions with random directions in the WS routine. This approach prevents the adversary from accurately profiling the GHR and
aligning it for the collision branch. We implemented this mitigation on our experimental platform by modifying OPTEE’s secure-world unbanked registers restore
function. This function is called during the switch from the normal world to the
secure world. We use the CPU cycle counter to generate a pseudo-random number, which determines the directions of the dummy branches. On our Cortex-A53
platform, we insert eight dummy branches, ensuring that the entire GHR for the target branch is randomized. This mitigation strategy is particularly effective against
TrustZoneTunnel, while remaining lightweight and efficient. The minimal resource
and time consumption of executing these dummy branches make it a practical solution for real-world implementation.

When designing mitigation strategies, it is important to consider both general and
attack-specific approaches. General mitigations, such as preventing resource sharing
across security domains or implementing constant-time algorithms, provide broad
protection against a range of potential attacks. Meanwhile, attack-specific mitigations, like our proposed method for TrustZoneTunnel, address particular vulnerabilities with targeted solutions. The most robust defense strategies often combine both
approaches, providing layered protections that address known threats while also raising the bar for potential adversaries. As the field of TEE security continues to evolve,
staying informed about the latest attack techniques and continuously updating mitigation strategies remains essential for maintaining the trustworthiness of secure execution environments.

**264** Advances in Hardware Design for Security and Trust

**11.5** **CONCLUSION**

The primary goal of this chapter is to propose a framework for microarchitectural
attacks on TEEs. To demonstrate the practical application of this framework, we introduced a novel TrustZoneTunnel attack, specifically targeting the branch prediction
unit with ARM’s TrustZone.

We demonstrate the effectiveness of TrustZoneTunnel in extracting sensitive information, such as neural network parameters, from the secure world. This case study
clearly showcases that even in strongly isolated TEE environments, shared microarchitectural components can lead to information leakage. We proposed several countermeasures against the TrustZoneTunnel attack, including randomizing the GHR,
flushing PHT entries during world switches, and implementing software-based protections. These mitigations aim to disrupt the attacker’s ability to reliably construct
and exploit PHT collisions. In conclusion, the proposed framework of microarchitectural attacks on TEEs challenges the promise of confidentiality provided by TEEs and
underscores the importance of addressing microarchitectural vulnerabilities within
our increasingly complex digital landscape. By systematically approaching the development, analysis, and mitigation of microarchitectural side-channel attacks, researchers and security professionals can contribute to truly secure implementations
of TEEs.

**REFERENCES**

1. Mohamed Sabt, Mohammed Achemlal, and Abdelmadjid Bouabdallah. Trusted execution environment: What it is, and what it is not. In 2015 IEEE Trustcom/BigDataSE/ISPA, volume 1, pages 57–64. IEEE, 2015.
2. Haehyun Cho, Penghui Zhang, Donguk Kim, Jinbum Park, Choong-Hoon Lee, Ziming Zhao, Adam Doup´e, and Gail-Joon Ahn. Prime+ count: Novel cross-world covert
channels on arm trustzone. In Proceedings of the 34th Annual Computer Security Applications Conference, pages 441–452, 2018.
3. Tianlin Huo, Xiaoni Meng, Wenhao Wang, Chunliang Hao, Pei Zhao, Jian Zhai, and
Mingshu Li. Bluethunder: A 2-level directional predictor based side-channel attack
against sgx. IACR Transactions on Cryptographic Hardware and Embedded Systems,
pages 321–347, 2020.
4. Zili Kou, Wenjian He, Sharad Sinha, and Wei Zhang. Load-step: A precise trustzone
execution control framework for exploring new side-channel attacks like flush+ evict.
In 2021 58th ACM/IEEE Design Automation Conference (DAC), pages 979–984. IEEE,
2021.
5. Xinyao Li and Akhilesh Tyagi. Cross-world covert channel on ARM TrustZone through
PMU. Sensors, 22(19):7354, 2022.
6. Keegan Ryan. Hardware-backed heist: Extracting ECDSA keys from qualcomm’s TrustZone. In Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security, pages 181–194, 2019.
7. Tianhong Xu, Aidong Adam Ding, and Yunsi Fei. TrustZoneTunnel: A cross-world
pattern history table-based microarchitectural side-channel attack. In 2024 IEEE International Symposium on Hardware Oriented Security and Trust (HOST), pages 01–11.
IEEE, 2024.

Is ARM’s TrustZone Trustable for Confidentiality Protection? **265**

8. AMD. AMD secure encrypted virtualization (SEV). [https://www.amd.com/en/](https://www.amd.com/en/developer/sev.html)
[developer/sev.html.](https://www.amd.com/en/developer/sev.html)
9. Cesare Garlati and Sandro Pinto. Secure IoT firmware for RISC-V processors. Embbedded World, 2021, 2021.
10. Xiaowen Xin. Titan M makes Pixel 3 our most secure phone yet, 2018.
11. Microsoft. Microsoft pluton security processor. [https://learn.microsoft.](https://learn.microsoft.com/en-us/windows/security/hardware-security/pluton/microsoft-pluton-security-processor)
[com/en-us/windows/security/hardware-security/pluton/](https://learn.microsoft.com/en-us/windows/security/hardware-security/pluton/microsoft-pluton-security-processor)
[microsoft-pluton-security-processor.](https://learn.microsoft.com/en-us/windows/security/hardware-security/pluton/microsoft-pluton-security-processor)
12. Johannes G¨otzfried, Moritz Eckert, Sebastian Schinzel, and Tilo M¨uller. Cache attacks
on intel SGX. In Proceedings of the 10th European Workshop on Systems Security,
pages 1–6, 2017.
13. Ben Lapid and Avishai Wool. Cache-attacks on the ARM TrustZone implementations
of AES-256 and AES-256-GCM via GPU-based analysis. In International Conference
on Selected Areas in Cryptography, pages 235–256. Springer, 2018.
14. Onur Acıic¸mez, Shay Gueron, and Jean-Pierre Seifert. New branch prediction vulnerabilities in openssl and necessary software countermeasures. In Cryptography and Coding: 11th IMA International Conference, Cirencester, UK, December 18–20, 2007, pages
185–203. Springer, 2007.
15. Onur Acıic¸mez, C¸ etin Kaya Koc¸, and Jean-Pierre Seifert. Predicting secret keys via
branch prediction. In Topics in Cryptology–CT-RSA 2007: The Cryptographers’ Track
at the RSA Conference 2007, San Francisco, CA, USA, February 5–9, 2007, pages 225–
242. Springer, 2006.
16. Dmitry Evtyushkin, Ryan Riley, Nael CSE Abu-Ghazaleh, ECE, and Dmitry Ponomarev. Branchscope: A new side-channel attack on directional branch predictor. ACM
SIGPLAN Notices, 53(2):693–707, 2018.
17. Guoxing Chen, Sanchuan Chen, Yuan Xiao, Yinqian Zhang, Zhiqiang Lin, and Ten H
Lai. SgxPectre attacks: Stealing intel secrets from SGX enclaves via speculative execution. arXiv preprint arXiv:1802.09085, 2018.
18. Jinwen Wang, Yueqiang Cheng, Qi Li, and Yong Jiang. Interface-based side channel
attack against intel SGX. arXiv preprint arXiv:1811.05378, 2018.
19. Intel Corporation. Intel <sup>®</sup> 64 and IA-32 Architectures Software Developer’s Manual Volume 3 (3A, 3B, 3C & 3D): System Programming Guide, 2019. Order Number: 325384070US.
20. Jos´e Bacelar Almeida, Manuel Barbosa, Gilles Barthe, Franc¸ois Dupressoir, and
Michael Emmi. Verifying {Constant-Time} implementations. In 25th USENIX Security
Symposium (USENIX Security 16), pages 53–70, 2016.
21. Per Larsen, Andrei Homescu, Stefan Brunthaler, and Michael Franz. SoK: Automated
software diversity. In 2014 IEEE Symposium on Security and Privacy, pages 276–291.
IEEE, 2014.
22. Lutan Zhao, Peinan Li, Rui Hou, Michael C Huang, Jiazhen Li, Lixin Zhang, Xuehai
Qian, and Dan Meng. A lightweight isolation mechanism for secure branch predictors. In 2021 58th ACM/IEEE Design Automation Conference (DAC), pages 1267–1272.
IEEE, 2021.
23. Hosein Yavarzadeh, Mohammadkazem Taram, Shravan Narayan, Deian Stefan, and
Dean Tullsen. Half&half: Demystifying Intel’s directional branch predictors for fast,
secure partitioned execution. In 2023 IEEE Symposium on Security and Privacy (SP),
pages 1220–1237. IEEE Computer Society, 2023.
24. Jo Van Bulck, Frank Piessens, and Raoul Strackx. SGX-step: A practical attack framework for precise enclave execution control. In Proceedings of the 2nd Workshop on
System Software for Trusted Execution, pages 1–6, 2017.

**266** Advances in Hardware Design for Security and Trust

25. Nicholas Carlini, Matthew Jagielski, and Ilya Mironov. Cryptanalytic extraction of neural network models. In Advances in Cryptology–CRYPTO 2020: 40th Annual International Cryptology Conference, CRYPTO 2020, Santa Barbara, CA, USA, August 17–21,
2020, Proceedings, Part III, pages 189–218. Springer, 2020.
26. Matthew Jagielski, Nicholas Carlini, David Berthelot, Alex Kurakin, and Nicolas Papernot. High accuracy and high fidelity extraction of neural networks. In Proceedings of
the 29th USENIX Conference on Security Symposium, pages 1345–1362, 2020.
27. Zhuang Liu, Ye Lu, Xueshuo Xie, Yaozheng Fang, Zhaolong Jian, and Tao Li. TrustedDNN: A trustzone-based adaptive isolation strategy for deep neural networks. In ACM
Turing Award Celebration Conference-China (ACM TURC 2021), pages 67–71, 2021.
28. Sanchuan Chen, Xiaokuan Zhang, Michael K Reiter, and Yinqian Zhang. Detecting
privileged side-channel attacks in shielded execution with d´ej´a vu. In Proceedings of
the 2017 ACM on Asia Conference on Computer and Communications Security, pages
7–18, 2017.
29. Ming-Wei Shih, Sangho Lee, Taesoo Kim, and Marcus Peinado. T-SGX: Eradicating
controlled-channel attacks against enclave programs. In NDSS Symposium 2017, 2017.
30. Giovanni Agosta, Luca Breveglieri, Gerardo Pelosi, and Israel Koren. Countermeasures
against branch target buffer attacks. In Workshop on Fault Diagnosis and Tolerance in
Cryptography (FDTC 2007), pages 75–79. IEEE, 2007.
31. Youngsoo Choi, Allan Knies, Luke Gerke, and Tin-Fook Ngai. The impact of ifconversion and branch prediction on program execution on the Intel Itanium processor. In Proceedings. 34th ACM/IEEE International Symposium on Microarchitecture.
MICRO-34, pages 182–182. IEEE Computer Society, 2001.

# 12 Security Verification for
### Next-Generation SoCs

Samit Shahnawaz Miftah, Amisha Srivastava,
Yiorgos Makris, and Kanad Basu

**12.1** **INTRODUCTION**

The advent of the next-generation system-on-chips (SoCs) marks a significant evolution in technological capabilities, aiming to meet the rising demands for more
intelligent and efficient devices across various industries. These SoCs incorporate
sophisticated AI and machine learning accelerators for real-time data processing,
significantly enhancing the functionality of edge devices [1,2]. As SoCs evolve, they
integrate cutting-edge semiconductor technologies like smaller node sizes and 3D
stacking, which not only improve power efficiency and performance but also allow
for the inclusion of more complex functionalities within increasingly compact footprints [3–5]. The complexity of SoC designs is further compounded by the integration of heterogeneous components such as CPUs, GPUs, and specialized accelerators
into a single chip [1, 6]. For example, a very simple SoC architecture, representative
of an automotive SoC, is shown in Figure 12.1, which includes a myriad of IPs like
memory, crypto, communication, etc. [7,8]. This integration challenges existing verification methodologies, as traditional techniques struggle to adequately address the
concurrency and non-deterministic behaviors exhibited by these complex systems.
The sheer volume of potential interactions and corner cases in such intricate designs
makes exhaustive verification impractical, often leading to prolonged development
cycles, elevated costs, and a heightened risk of critical design errors reaching production [9, 10]. Consequently, there is a pressing need for the industry to explore
and adopt advanced verification methodologies, such as semi-formal verification and
machine learning-assisted techniques, which are better suited to ensure the reliability
and functionality of these sophisticated hardware systems.

Advanced techniques are essential to address the growing complexity of SoCs and
the limitations of traditional verification methods [11–13]. As designs integrate more
components and functionalities, the number of possible interactions and scenarios
that need to be verified increases exponentially [12]. Traditional simulation-based
approaches, which rely on verifying a subset of possible states and conditions, struggle to provide adequate coverage for these complex systems, often leaving critical
corner cases unverified [13–16]. On the other hand, formal verification techniques

[DOI: 10.1201/9781003510949-12](https://doi.org/10.1201/9781003510949-12) **267**

**268** Advances in Hardware Design for Security and Trust

**Figure** **12.1** A simple SoC architecture (AutoSoC [7]), incorporating memory,
crypto, DSP, communication IPs.

ensure full coverage by mathematically proving system correctness. As hardware
designs grow in complexity, the number of possible states increases exponentially,
leading to a state space explosion that requires extensive computational resources and
memory. This makes formal verification impractical for large-scale systems such as
the next-generation SoCs since current hardware and algorithms are unable to handle the computational demands efficiently [13, 14, 17, 18]. Despite these challenges,
formal verification remains essential for smaller, well-defined systems, and ongoing
research seeks to enhance its scalability and efficiency [19].

Functional verification primarily focuses on verifying that a system behaves correctly under normal operational scenarios. However, security verification extends
this by considering potential threats and malicious attacks that could exploit unforeseen weaknesses [20]. These vulnerabilities may include side-channel attacks,
buffer overflows, and unauthorized access points [9]. Unlike functional verification,
which often overlooks corner cases—rare or unusual states—security verification
actively seeks to identify and mitigate these vulnerabilities before they can be exploited [9, 17, 21].

The importance of robust security verification is underscored by the increasing
sophistication of cyber threats and the critical role that electronic devices play in
sectors such as healthcare, finance, and national security. As technology becomes
more integrated into these vital areas, ensuring data integrity and system resilience is
paramount. Hardware vulnerabilities, once deployed, are difficult to patch or update,
making early identification and resolution crucial [9].

Security Verification for Next-Generation SoCs **269**

**Figure** **12.2** Different categories of common hardware and software vulnerability
exposure in an electronic system [9].

To effectively safeguard against potential threats, security verification employs a
myriad of techniques, including formal verification [22–25], information flow tracking (IFT) [26–30], fuzzing [13, 16, 31–33], and penetration testing [34, 35]. Formal
methods provide mathematical proofs to ensure certain vulnerabilities are absent,
while fuzz testing involves exposing the system to random or malformed inputs to
uncover unexpected behaviors. Penetration testing simulates real-world attack scenarios to identify and address vulnerabilities proactively.

In summary, security verification is critical for next-generation SoC designs. It
must be seamlessly integrated into every stage of the design process to anticipate
and counter emerging threats. This proactive approach not only protects individual
devices but also fortifies the broader security infrastructure, contributing to a more
secure digital environment.

**12.2** **THREAT MODELS**

In this section, we discuss the various vulnerabilities commonly found in SoCs,
which can be exploited either by software alone or through the combined efforts
of hardware and software. As depicted in Figure 12.2, approximately 43% of these
vulnerabilities result from such collusion and can be divided into seven categories:
access privileges, buffer errors, resource management, information leakage, numeric
errors, cryptographic errors, and code injection [9]. Detecting these vulnerabilities
is challenging because adversaries often exploit corner cases that are typically overlooked during functional verification. Therefore, implementing a thorough security
verification process is crucial. A well-defined threat model is essential to address
these issues, which we classify into five main categories: hardware Trojans, architectural flaws, access violations, fault injection attacks, and side-channel leakage. We
will discuss these threat models in detail in the following subsections.

**270** Advances in Hardware Design for Security and Trust

**Figure 12.3** Hardware Trojan attacks occurring at different stages of the IC life cycle
by involving various parties [36].

**12.2.1** **HARDWARE TROJANS**

Hardware Trojans are stealthy alterations made to integrated circuits with the intent
to undermine security measures [36, 37]. These modifications can cause functional
disruptions, leading to denial-of-service attacks, data breaches, or unauthorized access by adversaries [38]. Typically inactive during regular operations, these Trojans
activate under rare, specific conditions [39]. Trojan insertion can occur at various
stages of the IC design life cycle, often through vulnerabilities in third-party intellectual property, compromised electronic design automation (EDA) tools, or actions
by malicious insiders, as depicted in Figure 12.3 [36]. Structurally, Trojans may be
classified as either combinational or sequential circuits and usually consist of a trigger and a payload [40]. The trigger detects particular activation conditions, while
the payload executes the Trojan’s intended disruption upon activation. Activation
can occur via changes in digital functionality or variations in physical parameters
like temperature [40,41]. Advanced attackers design these Trojans to avoid detection
during standard testing and validation, ensuring they remain concealed until activated
during extended field use [9].

A representative hardware Trojan is depicted in Figure 12.4, demonstrating a
design that leverages frequent switching to charge a capacitor, CPayload, eventually

Security Verification for Next-Generation SoCs **271**

**Figure 12.4** A simple analog bug to flip bits within a circuit using frequent switching.

accumulating enough charge to flip a bit, as seen in Figure 12.4(a) [42]. This concept
is used to create a simple trigger circuit with transistors, as shown in Figure 12.4(b).
In this configuration, the transistor Cunit functions as a capacitor, storing charge when
the “Trigger Input” signal is HIGH. When the signal switches to LOW, the charge
transfers to transistor Cmain, which has sufficient driving strength to flip a bit, while
transistor M2 facilitates charge leakage. To activate this Trojan, the trigger signal
must switch at a high frequency to sufficiently charge Cmain. This keeps the Trojan
concealed, as knowledge of the specific trigger condition is required for exploitation.
Figure 12.4(c) illustrates two versions of a potential Trojan implementation, which
are used to reset a flip-flop.

Trojans are inherently covert and often tailored to specific architectures, making it
challenging to establish a standard attack surface [39, 40]. They remain undetectable
due to trigger conditions that are difficult for unaware users to activate [36]. Consequently, traditional verification techniques fall short in detecting these Trojans.
Furthermore, because Trojans are embedded in hardware, implementing effective
software-level defenses to bypass them is particularly challenging [39, 43].

Trojans can be inserted into hardware design using various ways, as listed below.

**12.2.1.1** **Rare Nodes and Branches**

Rare nodes and internal circuit nodes activated only under infrequent conditions are
prime targets for adversaries to insert hardware Trojans [39]. For instance, the ‘A2’
Trojan depicted in Figure 12.4 remains dormant until the trigger node operates at a
frequency exceeding a certain threshold. This threshold is typically set high enough
to prevent accidental activation by a benign user. However, an adversary can deliberately increase the trigger’s switching frequency beyond this threshold, thereby
activating the Trojan.

Furthermore, an adversary, such as a rogue designer or an untrusted IP vendor [36], can strategically embed Trojans within the register transfer level (RTL)
design by obscuring them in rarely executed branches or within continuous and concurrent assignments. These Trojans are specifically designed to avoid detection by
traditional simulation methods, which commonly employ random or constrainedrandom test patterns [39]. By exploiting these seldom-triggered design paths, the

**272** Advances in Hardware Design for Security and Trust

adversary ensures that the malicious modifications remain hidden during standard
verification processes, effectively bypassing detection and compromising the security and integrity of the design.

**12.2.1.2** **Gate Misplacement**

Strict adherence to design specifications is essential, as deviations can significantly
compromise functionality, trustworthiness, and security. Specifically, gate replacement errors in the gate-level netlist may introduce subtle anomalies that undermine
the design’s intended operation [44–46]. These errors not only disrupt functionality but also pose serious security risks by mimicking bit-flips, potentially leading to
unauthorized state transitions, incorrect outcomes, or denial of service [47,48]. Such
anomalies are particularly insidious because they often evade detection during design
reviews due to their minimal impact on physical characteristics like area, power, and
energy, and they are difficult to trigger using conventional validation techniques. For
instance, as illustrated in Figure 12.4 [42], a bit-flip attack can be executed by introducing just two new transistors, which can severely impact the security of an IP
where operations rely on single-bit flags, such as in interrupt controllers or memory
controllers.

**12.2.2** **ARCHITECTURAL FLAWS**

Architectural flaws can lead to significant security vulnerabilities, particularly when
a design incorporates all necessary functionalities but lacks robust security measures [49–51]. For instance, storing or transmitting sensitive data in plaintext within
memory makes it susceptible to unauthorized access. Another example involves the
design of a SoC mailbox, which is tasked with collecting data from the main infrastructure, verifying its integrity, and forwarding intact data to the SoC. If the data
is corrupted, the mailbox should discard it and request a resend. However, without an adequate feedback mechanism, the mailbox might continue operating without
generating error diagnostics, complicating debugging and the identification of error
sources.

Moreover, vulnerabilities may arise from the use of single-bit flags in critical
operations [52, 53]. For instance, in an interrupt controller that manages various interrupts based on ongoing processes, multiple flags (e.g., those for validity checks,
error checks, parity checks, etc.) are essential for indicating potential data loss, corruption, or manipulation. An adversary could exploit this by executing a bit-flip attack [54–56], altering the flag bits to falsely validate incorrect instructions. Replacing
the single-bit flag with a bit array to represent these flags can significantly enhance
hardware resilience against such attacks. This array would encode distinct patterns
for each error type, with specific patterns or sets of patterns indicating valid instructions, thereby providing a more robust defense against tampering.

**12.2.3** **PRIVILEGE ESCALATION ATTACKS**

Privilege escalation is a critical security vulnerability in modern computing, where
attackers exploit system flaws to gain unauthorized higher privileges, enabling them

Security Verification for Next-Generation SoCs **273**

to access and manipulate sensitive data. This threat significantly compromises system integrity and confidentiality. Diverse techniques are employed for privilege escalation, such as, exploiting circuit behaviors like Row-Hammer [57], and side-channel
attacks like Spectre and Meltdown [51, 58], targetting memory and processor vulnerabilities. Securing critical data and states is essential, as unauthorized access can
lead to illegal operations, including reading, writing, or altering sensitive information. Memory areas like caches, registers, RAM, and hard drives must be protected
against unauthorized changes.

Moreover, a concerning risk arises from the misuse of design for test (DFT) and
design for debug (DFD) infrastructures, which can expose sensitive information during functional mode. Furthermore, vulnerabilities such as buffer and integer overflows pose risks by allowing unauthorized memory overwrites, potentially violating
system integrity. Recent research highlights that speculative hardware components,
like exception handlers and branch predictors, can be manipulated to leak sensitive
data [50, 51, 58]. To mitigate these risks, security validation must thoroughly assess
and secure all access paths to critical information and memory locations. Blocking
unauthorized access is crucial to maintaining system integrity and confidentiality.
Privilege escalation remains one of the most severe security threats to computing
systems. It is imperative for designers and security professionals to implement robust defenses to protect sensitive data and ensure system integrity.

**12.2.4** **SIDE-CHANNEL ATTACKS**

Side-channel attacks exploit indirect information that is unintentionally leaked during the normal operation of a system rather than relying on direct access to the system’s internal states or data [59]. These attacks focus on observing and analyzing various physical phenomena, such as power consumption, electromagnetic emissions,
timing variations, and even acoustic signals. By analyzing these phenomena, attackers can infer sensitive information about the operations being performed within a
SoC or cryptographic device, as shown in Figure 12.5. In the context of cryptography, a side-channel is any observable characteristic of a system that can be measured
during its operation, aside from the actual data output. For instance, when a cryptographic algorithm is executed, the power consumption of the device running the
algorithm may vary depending on the data being processed. Although this power
consumption is not part of the algorithm’s intended output, it can still provide clues
about the data or the operations performed. Listed below are some types of popular
side-channel attacks.

**12.2.4.1** **Microarchitectural Side-Channel Attacks**

_12.2.4.1.1_ _Timing Attacks_

Timing attacks exploit variations in the time it takes to execute certain operations, particularly in cryptographic algorithms. These timing variations can arise
from different execution paths or optimizations that depend on secret data, such as

**274** Advances in Hardware Design for Security and Trust

**Figure** **12.5** Example scenario for a side-channel attack: Embedded devices, such
as public kiosks and sensors, are often physically accessible, heightening the risk of
these attacks.

cryptographic keys. By carefully measuring the execution time of specific operations, an attacker can infer the secret parameters involved in the computation. For
example, in a chosen ciphertext attack, an adversary may measure the time taken
to decrypt different ciphertexts and use statistical methods to deduce the secret key.
These attacks are particularly effective when the algorithm’s execution time varies
based on the data being processed.

_12.2.4.1.2_ _Cache-Based Attacks_

Cache-based attacks exploit the behavior of the CPU cache, a small, fast memory
used to store frequently accessed data. Since the cache is shared among different processes, an attacker can infer information about another process by observing changes
in the cache state. Common types of cache-based attacks include:

_Flush+Reload:_ In a Flush+Reload attack, the attacker begins by flushing (removing)
a specific cache line, forcing any data in that line to be fetched from the main memory
the next time it is accessed. The attacker then waits and reloads the same cache line,
measuring the time it takes to access the data [60]. If the access is fast, it indicates
that another process has loaded the data back into the cache, suggesting that the data
was recently used. This allows the attacker to determine whether a specific memory
location was accessed by the victim process, potentially revealing information about
the victim’s activities, such as cryptographic key usage in algorithms like AES or
RSA.

Security Verification for Next-Generation SoCs **275**

_Prime+Probe:_ In this attack, the attacker takes advantage of the cache’s shared nature in modern CPUs [61]. The attack involves two key phases. The “prime” phase,
where the attacker fills the cache with their own data by accessing specific memory
addresses that map to certain cache lines, ensuring these lines are fully occupied.
Following this, during the “probe” phase, the attacker re-accesses the same memory
addresses after allowing the victim process to run and measures the access times.
If the access time is slower, it indicates that the victim process accessed those cache
lines, causing the attacker’s data to be evicted and replaced with the victim’s data. By
analyzing which cache lines were evicted, the attacker can infer the victim’s memory
access patterns, which can be linked to sensitive information, such as cryptographic
keys or plaintext. This attack is particularly concerning in shared environments, like
cloud servers, where multiple processes or virtual machines run on the same hardware, making it easier for an attacker to glean critical data without needing direct
access to the victim’s memory.

_12.2.4.1.3_ _Speculative Execution Attacks_

Speculative execution attacks exploit advanced performance optimizations in modern CPUs, where instructions are executed speculatively, i.e., ahead of time—based
on predicted outcomes of operations like conditional branches [62]. This technique
is used to keep the CPU pipeline full and efficient, allowing the processor to operate
at high speeds by guessing the results of operations and executing instructions before
the final outcome is known. However, this speculative execution can lead to security
vulnerabilities when it interacts with sensitive data. If the speculative execution process is influenced by secret data, it can leave traces of this data in the system, such as
in the CPU cache, even if the execution is eventually rolled back. These traces can
then be exploited by attackers to extract sensitive information.

_Meltdown:_ Meltdown is a speculative execution attack that specifically targets a
vulnerability in out-of-order execution, a process where the CPU executes instructions in a non-sequential order to optimize performance [63]. Meltdown exploits this
mechanism to bypass standard security boundaries, allowing an attacker to read privileged memory, including kernel memory, from a user-space application. By leveraging the fact that speculative execution temporarily grants access to sensitive data,
Meltdown can extract this data even though the CPU eventually blocks the unauthorized access. The attacker measures side effects, such as cache changes, to infer the
contents of the protected memory, making Meltdown a highly dangerous attack that
undermines core security protections.

_Spectre:_ Spectre is a highly sophisticated branch prediction attack that takes advantage of speculative execution, a performance optimization technique where the
CPU guesses the outcome of a branch and executes instructions ahead of time [58].
Branch prediction attacks exploit the CPU’s branch predictor, a critical component designed to enhance performance by guessing the direction of conditional

**276** Advances in Hardware Design for Security and Trust

**Figure** **12.6** Power side-channel attack flow. Attacker observes and analyzes dynamic power consumption profile of security-critical hardware devices to reconstruct
secrets, such as encryption keys.

branches (such as if-else statements) before they are fully resolved [64]. This prediction helps maintain a smooth and efficient execution pipeline. However, when the
branch predictor’s behavior is influenced by secret data, it can be manipulated by
an attacker to infer that data by carefully crafting inputs that cause the predictor to
make specific guesses, and then analyzing the resulting performance changes or side
effects [65].

In Spectre, the attacker manipulates the branch predictor to mislead the CPU into
speculatively executing instructions that access sensitive data, such as passwords or
encryption keys. Although these speculative instructions are not supposed to produce observable effects if the branch prediction is wrong, they can leave subtle
traces in the system, particularly in the CPU cache. The attacker then measures
these side effects, such as changes in cache state, to infer the sensitive information. Spectre’s power lies in its ability to exploit speculative execution across different software layers, making it a formidable attack that can breach even wellprotected systems by leaking data that should be inaccessible under normal execution
conditions.

**12.2.4.2** **Power Side-Channel Attacks**

Power analysis attacks involve monitoring the power consumption of a cryptographic
device during its operation, as shown in Figure 12.6. These attacks are particularly
effective against hardware implementations such as smart cards or other embedded
systems [66]. Power analysis attacks are divided into three main categories.

Security Verification for Next-Generation SoCs **277**

_12.2.4.2.1_ _Simple Power Analysis (SPA)_

SPA involves directly observing power traces to identify which specific instructions
are being executed and what values are being processed [67]. This attack requires
detailed knowledge of the implementation. The power traces can reveal distinct patterns corresponding to different operations, enabling the attacker to infer sensitive
information, such as the sequence of instructions and even specific data values.

_12.2.4.2.2_ _Differential Power Analysis (DPA)_

DPA is more sophisticated and does not require detailed knowledge of the implementation [68]. Instead, it uses statistical methods to find correlations between power
consumption and secret data, allowing an attacker to recover secret keys with relatively few resources. DPA has been demonstrated to be highly effective against various cryptographic algorithms, including those implemented in elliptic curve cryptosystems (ECC). By analyzing the differences in power consumption across multiple encryption or decryption operations, DPA can effectively isolate the contributions
of the secret key and reveal it.

_12.2.4.2.3_ _Correlation Power Analysis (CPA)_

CPA is an advanced form of DPA that involves correlating the power consumption
of a cryptographic device with hypothetical power consumption models [69]. The
attacker creates a hypothesis about the value of the secret key and calculates the expected power consumption based on this hypothesis. By comparing the actual power
traces with the expected power consumption, the attacker can identify the correct key
when the correlation is highest. CPA is particularly effective because it can exploit
even small differences in power consumption, making it a powerful tool for extracting secret keys from cryptographic devices. CPA is often used in conjunction with
other statistical methods to enhance the accuracy and efficiency of the attack.

**12.2.4.3** **Electromagnetic (EM) Attacks**

Electromagnetic attacks exploit the electromagnetic radiation emitted by a device
during its operation. Like power analysis attacks, EM attacks can reveal information
about the underlying computation and data. These attacks are divided into: (1) simple
electromagnetic analysis (SEMA): SEMA focuses on direct observation of electromagnetic emissions to deduce specific instructions or data being processed; (2) differential electromagnetic analysis (DEMA): DEMA, similar to DPA, uses statistical
techniques to analyze EM emissions and extract secret information. EM attacks are
particularly dangerous because they can be performed even when power analysis attacks are mitigated. EM emanations can thus break power analysis countermeasures
and compromise cryptographic devices [70].

**278** Advances in Hardware Design for Security and Trust

**Figure 12.7** System-on-Chip (SoC) Design Flow [71].

**12.3** **CHALLENGES OF SECURITY VERIFICATION**

Security verification and validation are particularly challenging due to several factors. Firstly, security is a broad concept, making it difficult to define a secure design
or establish a clear verification plan. As mentioned in Section 12.2, various security
vulnerabilities—such as information leakage, side-channel attacks, privilege escalation, and malicious functionality—must be addressed, requiring extensive knowledge of security attacks. Designers often prioritize performance, budget constraints,
and testability, sometimes overlooking the security implications of their decisions.
Moreover, mitigating one vulnerability can expose the design to others, as threat
models often overlap. For instance, preventing information leakage might introduce
side-channel leakage, which attackers can exploit.

In the following subsections, we will elaborate on the challenges typically faced
during security verification in the security development cycle.

**12.3.1** **DIVERSITY OF ASSETS**

Modern SoCs integrate numerous IP cores throughout the design flow, as shown
in Figure 12.7 [71]. These components pose significant security challenges, requiring robust protection, especially for assets like secret keys used in cryptographic
operations. Interrupt controllers and reset handlers are susceptible to unauthorized
exploits, potentially leading to security breaches [72]. Additionally, memory units
are vulnerable to attacks such as Row-hammer, which can result in data leakage or
corruption [57, 73].

Moreover, developer keys and configuration bits, which control critical operations
within the SoC, represent another layer of vulnerability. If the integrity of these elements is compromised, an attacker could bypass system security [74]. For instance,
encryption algorithms typically rely on a random number, known as a nonce, generated by the true random number generator (TRNG). If an attacker were to alter the
TRNG’s configuration—perhaps forcing it to produce a predictable number—the security of the entire encryption unit could be undermined [75, 76].

Furthermore, SoCs contain manufacturing codes, such as original equipment
manufacturer (OEM) and original component manufacturer (OCM) keys, which are
crucial for preventing counterfeiting [77,78]. Compromising these keys could lead to
unauthorized replication of the chip, with severe implications for both security and
economic loss. Sensitive user data, including credentials stored on the device, must
also be rigorously protected to maintain user privacy [77, 79–81].

Security Verification for Next-Generation SoCs **279**

The dynamic nature of assets in SoCs further exacerbates security challenges.
Unlike static values, assets in an SoC propagate across various components and influence other variables during runtime [82, 83]. This complexity makes it difficult to
identify and protect all assets effectively. Furthermore, each asset requires a specific
threat model and a set of security rules to ensure its secure transmission through
different communication channels.

The intricate and interconnected nature of SoC assets, combined with their dynamic behavior, necessitates a comprehensive approach to security validation [84–
87]. This includes not only identifying all critical assets but also understanding how
they interact and propagate throughout the system. Without such an approach, the diverse and evolving threats in modern SoCs could result in significant vulnerabilities,
undermining the security of the entire chip.

**12.3.2** **LACK OF SECURITY METRICS**

The verification of next-generation SoCs faces a significant challenge due to the absence of comprehensive security metrics. Unlike functional verification, which uses
metrics like branch and statement coverage to guide efforts, security lacks similar
quantitative measures, making it difficult to systematically validate designs for vulnerabilities.

For instance, in the context of side-channel vulnerabilities, metrics are essential
to measure unbalanced execution paths that may create exploitable timing and power
signatures in hardware designs [88]. Similarly, metrics should assess the impact of
different encryption keys on power consumption to identify and prevent leaky implementations [89]. Without these metrics, detecting and mitigating such vulnerabilities
becomes a challenging task.

The challenge is further compounded by Hardware Trojans, malicious functions,
and unintentional architectural flaws [90, 91]. The variety of Trojans, each with
unique objectives, triggers, and impacts, complicates the creation of a unified fault
model for detection. Adversaries often design Trojans with stealthy characteristics,
embedding them in hard-to-detect areas and evading standard validation. Assets can
be leaked through multiple channels, complicating the development of a comprehensive information leakage model. Additionally, designers may inadvertently introduce
security vulnerabilities during SoC design and IP core integration, with no existing
metric to assess the security of the entire SoC at each step.

Thus, a critical need exists for a set of security metrics that can measure the vulnerability of designs against different threat models and attack surfaces. Such metrics
would enable the automatic identification of security weaknesses and guide the security verification process, ultimately enhancing the robustness of design security.

**12.3.3** **UNINTENTIONAL VULNERABILITIES**

Unintentionally introduced vulnerabilities pose significant challenges to the security of modern systems. These vulnerabilities often arise not from malicious intent
but from design errors, limitations in EDA tools, or compromises made for DFT

**280** Advances in Hardware Design for Security and Trust

and DFD purposes. For example, speculative execution units in modern processors,
which are designed to enhance performance, can inadvertently create security risks.
When these units execute instructions speculatively, they may leave traces in the
cache that can be exploited by attackers through cache timing attacks, leading to
unauthorized access to sensitive data.

EDA tools, especially synthesis tools, can also unintentionally introduce security
vulnerabilities. These tools may optimize finite state machines (FSMs) by generating
additional “don’t care” states, which, if improperly connected to secure states, could
be exploited by attackers using fault injection techniques [92–94]. Such vulnerabilities allow attackers to bypass security mechanisms and alter a system’s control flow,
compromising its integrity.

The complexity of modern SoCs further complicates security, as DFD and DFT
infrastructures increase observability for debugging and validation but also create
new attack vectors. While these infrastructures are essential for post-silicon debugging, their enhanced observability can be exploited in attacks such as trace
buffer [95, 96] and scan-based side-channel attacks [97], jeopardizing the system’s
confidentiality and integrity. These vulnerabilities underscore the need for current
design and verification processes to evolve and incorporate security measures to prevent unintended security risks.

**12.3.4** **GLOBALLY DISTRIBUTED SUPPLY CHAIN**

Globally distributed supply chains present significant challenges in ensuring the security of SoC designs [36, 98]. The complexity of these supply chains arises from
the involvement of multiple countries and companies in various stages of the design, fabrication, and testing processes [98–100]. SoC designers often integrate IP
cores from third-party vendors to reduce costs and meet time-to-market demands.
However, these 3P IPs can introduce malicious functionalities, which may alter the
correct behavior of the design, cause denial of service, or lead to information leakage. These threats are often concealed well enough to evade traditional validation
methods.

Furthermore, SoC designs are frequently sent to external vendors for specialized
tasks such as power optimization, clock-tree insertion, and DFT and DFD implementation. These vendors gain full access to the gate level or layout of the design, which
poses risks such as reverse engineering or intellectual property theft. Additionally,
these vendors could introduce malicious functionality that is difficult to detect. The
potential threats extend to untrusted foundries during the fabrication stage, where
similar risks can be introduced.

The globally distributed nature of SoC supply chains creates unique vulnerabilities that necessitate thorough security validation and verification techniques. It is
crucial to detect and address these security issues during the design and verification
phases. If vulnerabilities persist into the post-silicon stage, the ability to modify or
rectify them becomes extremely limited. Moreover, the cost associated with fixing
these issues escalates significantly as the design progresses through the development
stages, adhering to the “rule of ten” [101]. If vulnerabilities are not addressed before

Security Verification for Next-Generation SoCs **281**

the manufacturing stage, they can lead to substantial revenue losses. Therefore, the
development of efficient security validation and verification methods is essential to
ensure the security and trustworthiness of SoC designs.

**12.3.5** **SIDE-CHANNEL VULNERABILITY DETECTION**

Detecting side-channel vulnerabilities presents significant challenges due to the subtle and often indirect nature of these attacks. Side-channel attacks do not rely on
traditional software vulnerabilities, such as code flaws or misconfigurations, but instead exploit the unintended leakage of information through physical phenomena,
making them difficult to identify and mitigate.

One of the key challenges in detecting microarchitectural side-channel attacks,
such as timing attacks, cache-based attacks, and speculative execution attacks, lies
in their reliance on micro-level variations in system behavior [102, 103]. Timing
attacks, for instance, exploit minor variations in the time it takes to execute cryptographic operations, which are influenced by factors such as execution paths and
hardware optimizations. These variations can be so small that they are easily overlooked during standard security assessments. Moreover, the execution time may vary
based on different input data, making it challenging to create consistent detection
mechanisms.

Power side-channel attacks further illustrate the challenges of side-channel vulnerability detection. These attacks analyze the power consumption of a device during
cryptographic operations to extract sensitive information, such as encryption keys.
Detecting these vulnerabilities is challenging because the power variations exploited
by attackers are often minute and can be obscured by noise or other factors in the
environment [104]. Furthermore, these attacks do not require direct access to the
data being processed, making them difficult to detect with conventional monitoring
tools. For instance, SPA relies on directly observing power traces, which may reveal
distinct patterns corresponding to specific instructions or data values. However, detecting such patterns requires detailed knowledge of the device’s operation and often
specialized equipment. DPA and CPA, being more advanced, use statistical methods to find correlations between power consumption and secret data, making them
particularly challenging to detect because they do not require precise knowledge of
the device’s implementation. Instead, these attacks can succeed with relatively few
resources, further complicating detection efforts.

Detecting vulnerabilities to EM attacks is particularly challenging because the
emitted radiation can vary widely depending on the device’s design and operational
conditions [105]. Moreover, EM attacks can be conducted from a distance, without
direct contact with the target device, making traditional security monitoring and detection approaches less effective. Identifying and mitigating EM vulnerabilities often
requires specialized equipment to analyze the radiation patterns and assess potential
information leakage. Overall, detecting side-channel vulnerabilities is a complex and
multifaceted challenge. These attacks exploit subtle, often unintended behaviors of
hardware, making them difficult to detect with conventional security tools.

**282** Advances in Hardware Design for Security and Trust

**Figure 12.8** Different types of information flow in hardware.

**12.4** **SECURITY** **VERIFICATION** **AND** **VULNERABILITY** **DETECTION**
**STRATEGIES**

To tackle the challenges highlighted in Section 12.3 and manage the increasing complexity of next-generation SoCs, various security verification techniques have been
developed in recent years. These methods span from RT-level verification to postsilicon verification, including information flow tracking (IFT), runtime detection,
concrete testing, and fuzzing. Each technique targets specific types of vulnerabilities
while ensuring scalability to accommodate the growing size and complexity of future
SoCs.

In the subsequent subsections, we elaborate on these security verification and
vulnerability detection techniques.

**12.4.1** **INFORMATION FLOW TRACKING**

IFT is a security technique that monitors how information moves through a system
during computation. It assigns tags to data objects to indicate their security classifications, which vary based on the specific security properties being analyzed. As data
is processed, IFT updates these tags and checks the information flow by examining
the tag states [106]. The first IFT method was developed by Denning et al. [107,108]
to enforce security across various system components, including operating systems
(OSs) [109–111], programming languages [112], distributed systems [113,114], and
cloud computing [115]. IFT can identify and prevent numerous software security issues, such as buffer overflows, memory corruption, SQL injection, formatted string
attacks, cross-site scripting, and malware [116–121].

Hardware IFT assigns tags to data bits or groups to indicate their sensitivity or origin. As data moves through hardware components like registers, caches, and buses,
the IFT system monitors these tags to ensure sensitive information is managed according to security policies. Information flow can be categorized into two types:
explicit and implicit. Explicit flow, also known as data flow, involves direct data
movement (Figure 12.8(a)), whereas implicit flow occurs due to context-dependent
execution, such as conditional operations (Figure 12.8(b)).

Security Verification for Next-Generation SoCs **283**

1. Fine-grained tracking: IFT can monitor data at the bit level, providing
highly detailed control.
2. Low overhead: Hardware implementation minimizes performance impact
compared to software-based solutions.
3. Tamper-resistance: Being built into the hardware makes IFT more difficult
for attackers to bypass or disable.

The significance of hardware IFT has grown with the increasing sophistication of
cyber threats. As attackers develop more advanced techniques to exploit hardware
vulnerabilities, traditional software-based security measures are often insufficient.
Hardware IFT provides a crucial layer of defense by:

1. Detecting data leaks: Identifying when sensitive information is being accessed or transmitted improperly.
2. Preventing unauthorized modifications: Ensuring critical data and system
configurations remain intact.
3. Enhancing isolation: Maintaining strict boundaries between different security domains within a system.
4. Supporting compliance: Helping organizations meet stringent data protection regulations.

Hardware-based information flow tracking presents a powerful solution for enhancing the security of next-generation SoCs. By offering fine-grained control over
data movement and enabling real-time threat detection, IFT addresses critical vulnerabilities at the hardware level. Despite challenges in implementation, ongoing
research promises to refine this technology, potentially revolutionizing cybersecurity
in complex digital systems. As the digital landscape evolves, IFT’s ability to provide
proactive protection against sophisticated cyber threats positions it as a cornerstone
of future SoC security strategies.

**12.4.2** **RUN-TIME DETECTION**

Run-time detection is a security mechanism designed to identify and mitigate processor bugs that occur during the execution of a program. Unlike pre-deployment verification methods, run-time detection operates in real time, monitoring the processor’s
behavior to catch any deviations from the expected execution patterns [122].

The primary strength of run-time detection lies in its ability to catch vulnerabilities that may have been missed during the initial verification phase, especially those
related to security-critical bugs [122–124]. These bugs can compromise system security by allowing unauthorized access to privileged processor states. Run-time detection ensures that even if a bug is present in the hardware, its impact can be minimized
or entirely prevented during operation. This method is particularly valuable because
it can dynamically adapt to new threats without the need for complete system redesigns.

Run-time detection is implemented by enforcing a set of invariants on the processor’s state, which are derived from the instruction set architecture (ISA). These

**284** Advances in Hardware Design for Security and Trust

invariants define the expected behavior of the processor during execution. If a processor state violates one of these invariants, the detection system triggers an exception
that halts the compromised state and invokes recovery mechanisms to ensure system
stability. This approach effectively isolates and neutralizes potential threats without
significantly impacting performance.

As SoC designs become more complex, incorporating run-time detection mechanisms will be crucial for ensuring their security. By integrating lightweight, real-time
monitoring systems into the SoC, manufacturers can protect against emerging threats
and maintain the integrity and reliability of these advanced processors in increasingly
hostile environments.

**12.4.3** **PROOF-CARRYING HARDWARE VERIFICATION**

Proof-carrying hardware (PCH) intellectual property is a framework designed to ensure the security and trustworthiness of third-party hardware IP modules [121, 125].
It draws on principles from proof-carrying code (PCC), adapting them for hardware.
The process starts with the consumer and vendor establishing certain security-related
properties that the IP module must comply with, i.e., defining the security protocols.
These properties are formally defined in a logical language, such as Coq [126], which
serves as the basis for constructing a proof of compliance.

The vendor is responsible for creating this formal proof, demonstrating that the IP
module conforms to the agreed-upon security properties. This proof, crafted in the
Coq language, is delivered alongside the IP module. Upon receipt, the consumer can
automatically validate the proof using the same formal language, ensuring that the
IP operates within the defined security boundaries. This process allows the consumer
to verify the trustworthiness of the hardware without needing to rely on the inherent
trustworthiness of the vendor.

The PCH framework offers significant security advantages by protecting against
the insertion of malicious circuitry, such as Hardware Trojans, which can compromise the integrity of a system. By embedding security assurances into the design and
acquisition process, PCH enables consumers to confidently integrate 3P IP modules
into their systems, knowing they meet the predefined security criteria. This approach
not only enhances security but also empowers consumers to actively verify the safety
of the IP cores they use.

**12.4.4** **CONCOLIC TESTING**

Concolic testing, an advanced hybrid technique that combines concrete and symbolic
execution, has gained prominence as a powerful tool in hardware verification [17,
127, 128]. This approach leverages the practicality of simulation-based testing while
incorporating the rigor of formal verification, thereby bridging the gap between these
two traditional methodologies.

One of the key strengths of concolic testing lies in its ability to systematically
explore execution paths, which enables the detection of corner cases that might otherwise go unnoticed with conventional testing methods. Employing both concrete

Security Verification for Next-Generation SoCs **285**

**Figure 12.9** Concolic testing workflow [128].

and symbolic execution not only enhances test coverage but also uncovers subtle
bugs that arise from specific input combinations or rare conditions. Moreover, concolic testing intelligently guides the test generation process, significantly reducing
the time required for verification while ensuring a thorough examination of the hardware design. This makes it an indispensable technique in scenarios where reliability
and correctness are paramount.

Concolic testing is a systematic verification method that combines concrete execution with symbolic analysis to ensure the reliability of hardware designs. Figure 12.9 illustrates the working process of concolic testing. The procedure begins
by defining the design under test (DUT), identifying input variables, and setting up
the testing environment. The DUT is then executed with specific input vectors while
symbolic representations of these inputs are maintained. At each decision point during execution, symbolic constraints are generated, which are then used to identify
new input vectors that explore different execution paths. This process is iteratively
repeated until sufficient coverage is achieved or a predefined limit is reached. Finally,
the results are analyzed to identify any failures and assess the thoroughness of the
verification process.

Concolic testing is crucial for securing next-generation SoCs by offering comprehensive coverage and detecting hard-to-find bugs that traditional methods may overlook. Its hybrid approach, blending practical simulation with formal rigor, makes it a
scalable and reliable solution for verifying complex hardware designs where security
and reliability are essential.

**12.4.5** **FUZZING**

Fuzz testing, commonly referred to as fuzzing, is a dynamic software testing technique designed to identify vulnerabilities and security flaws by providing invalid,
unexpected, or random data as inputs to a computer program. Unlike boundary value
analysis (BVA) [129], which primarily focuses on refining exception handling for
predefined edge cases, fuzzing goes a step further by exploring inputs that fall outside the expected range. This approach not only tests the program’s handling of valid
and invalid inputs but also probes the boundaries to trigger undefined or insecure
behaviors, potentially uncovering vulnerabilities that would otherwise remain hidden [130].

**286** Advances in Hardware Design for Security and Trust

Fuzzing methods are broadly categorized into mutation-based, where existing
data is altered to create new test cases, and generation-based, which involves creating new tests from scratch based on specific protocols or formats. These techniques
have proven highly effective across various software categories, including binary
targets and operating systems. Major tech companies like Google leverage fuzzing
extensively through platforms like OSS-Fuzz and ClusterFuzz, which automate the
fuzzing process for large codebases, leading to the discovery of numerous security flaws [13, 131–139]. Fuzzing can be divided into two primary approaches: (1)
Coverage-guided, which aims to maximize execution coverage by exploring diverse
program paths [140–143], and (2) directed fuzzing, which focuses on generating test
cases that target specific points in the program’s execution [144].

The adoption of fuzzing for hardware security verification has marked a significant advancement in developing scalable and robust security processes. Laeufer et al.
introduced this approach with Rfuzz [14], demonstrating its potential in uncovering
hardware vulnerabilities through random or semi-random input testing. Subsequent
research has focused on enhancing fuzzing techniques in two primary areas:

1. Improved Coverage: Developing more sophisticated algorithms for input
generation and mutation to expand the range of tested scenarios.
2. Directed Test Cases: Creating more targeted fuzzing approaches to focus
on areas likely to contain vulnerabilities.

Notable contributions include DifuzzRTL [15], HypFuzz [16], HyperFuzzing [31],
and GenFuzz [32]. These studies have significantly advanced the field, improving
both the efficiency and effectiveness of hardware security testing.

As shown in Figure 12.10, fuzzing starts by taking the RTL design of the design
under verification (DUV), the security properties to be verified, reset logic, and circuit initialization assumptions as inputs. The fuzzer generates input vectors via the
seed generator, which are applied to both the DUV and its golden reference model.
The outputs are then compared; mismatches are reported as errors, while matches
lead to coverage measurement in the DUV simulation. Based on coverage and input vectors, the mutation engine constrains the seed generator, enabling the fuzzer to
simulate the DUV and reach uncovered states.

Fuzzing is a powerful tool for hardware security that helps identify vulnerabilities in complex SoC designs by generating unexpected inputs and exploring edge
cases. This dynamic approach complements traditional verification methods and is
evolving to incorporate new technologies, such as machine learning, for improved
input pattern generation. By rigorously stress-testing SoCs beyond conventional parameters, fuzzing plays a crucial role in creating more resilient and secure hardware systems, essential for the next generation of connected devices and advanced
microprocessors.

**12.4.6** **SIDE-CHANNEL ATTACK DETECTION TECHNIQUES**

In the realm of hardware security, side-channel attack detection techniques are crucial for safeguarding sensitive information. These techniques vary based on the

Security Verification for Next-Generation SoCs **287**

**Figure 12.10** Fuzzing mechanism for hardware.

nature of the attack but generally involve the analysis of unintended information
leakage from physical implementations of cryptographic systems. Cache-based sidechannel attacks leverage patterns in cache access to infer protected data. These
detection strategies primarily focus on the monitoring of cache-related metrics. Techniques such as performance counter monitoring utilize hardware performance counters to identify irregular cache activities that might suggest an attack [145, 146].
Additionally, machine learning approaches are applied to classify and predict abnormal access patterns, enhancing detection capabilities [147]. Similarly, detection
methods for timing side-channel attacks include the use of machine learning to identify timing discrepancies that may indicate malicious activities [148]. Implementing
cryptographic algorithms that maintain constant execution times regardless of input
conditions is another effective countermeasure, ensuring that timing variations do not
reveal sensitive information [149]. Detection of power side-channel attacks focuses
on analyzing the power consumption patterns of devices during cryptographic processes. This is crucial in both pre-silicon and post-silicon stages to ensure the security
integrity of cryptographic hardware. Techniques such as layout-based analysis and
gate-level leakage localization are employed in the early stages of design to identify
and mitigate potential vulnerabilities [150, 151]. For devices in operation, real-time
monitoring using on-chip sensors helps in detecting ongoing attacks, allowing for
immediate response measures [152]. The application of methodologies such as test
pattern generation and graph neural networks at the RTL level further enhances the
detection capabilities by detecting potential attack scenarios [153, 154].

**288** Advances in Hardware Design for Security and Trust

**12.5** **FUTURE RESEARCH PROSPECTS**

Emerging methodologies such as automatic property extraction from documentation [155,156], automatic bug localization [8], and automated repair leveraging large
language models (LLMs) hold significant promise for advancing the security of nextgeneration SoCs. These techniques facilitate the rigorous and efficient identification
and rectification of vulnerabilities by automating complex processes that traditionally require extensive manual effort. By utilizing LLMs, the process of ensuring adherence to security specifications and detecting potential weaknesses can be greatly
expedited, leading to enhanced robustness and resilience of SoCs against evolving
security threats. Consequently, these advancements offer substantial benefits in fortifying the security infrastructure of contemporary and future SoCs.

**12.5.1** **SECURITY PROPERTY EXTRACTION**

Traditional methods for generating security properties in SoCs are both timeconsuming and dependent on the developer’s experience. As a result, there is a
pressing need for techniques that systematically generate security properties from
available documentation. Major hardware organizations like RISC-V, MSP, and Arduino provide detailed documentation on processor functionalities and operational
behaviors [155]. Leveraging this documentation to generate security properties can
significantly reduce manual effort and improve the robustness of the verification process.

Documentation from hardware providers contains rich information about system
operations that can be transformed into security constraints at the RTL. By employing LLMs, particularly those based on language models like GPT, it is possible
to extract relevant security-related sentences from these documents. This approach
builds upon successful applications of language models in other domains, such as
the biomedical field, where models like BioBERT have demonstrated effective extraction of domain-specific information.

The use of LLMs to generate hardware security assertions is a promising new
area of research. By processing natural language comments from designers and verification engineers, LLMs can automatically create security assertions, potentially
speeding up the definition of security policies. The generated security properties can
then be used with the RTL design verification methods discussed in Section 12.4 to
identify potential vulnerabilities. Incorporating this approach into the security development life cycle for SoCs can enhance security and further decrease the time
required.

Automatic extraction of security properties from hardware documentation offers a
promising approach to reducing the time and effort required for security verification.
By leveraging advanced language models, the process of generating and verifying
security assertions can be streamlined, leading to enhanced security and efficiency in
hardware design, as demonstrated by recent studies [155–158].

Security Verification for Next-Generation SoCs **289**

**12.5.2** **AUTOMATIC BUG LOCALIZATION**

Automatic bug localization is a critical advancement in the field of software debugging, particularly for improving the efficiency of security verification in RTL
designs. Software bug localizing methods, such as code slicing and spectrum analysis, are often insufficient for dealing with the unique challenges posed by RTL
codes. These techniques, which rely on analyzing executed versus non-executed code
lines [159–161], struggle with the concurrent nature of RTL execution, making it difficult to trace and isolate bugs effectively.

Bugs can significantly impact the security and functionality of an SoC in RTL
designs. The concurrent execution of RTL code adds complexity to the debugging
process, making manual methods time-consuming and prone to errors. Automatic
bug localization addresses these issues by providing a systematic approach to pinpointing faulty lines of code with precision. This capability is crucial for enhancing
the speed and accuracy of security verification processes.

Consider the example in Listing 12.1, which illustrates a password-checkingfunction with a security flaw. Existing RTL security verification methods, as mentioned
in Section 12.4, may identify such vulnerabilities but lack the capability to pinpoint
the specific lines of code causing the issue. Consequently, developers may need to
manually inspect extensive RTL code, potentially spanning thousands of lines, to
identify the problem. This manual process not only incurs substantial delays but also
extends the time-to-market for the SoC.
✞ ☎

1 ‘STATE_run_test_idle: **begin**

2 **if** (tms_pad_i && (passchk))

3 next_TAP_state=‘STATE_select_dr_scan;

4 **else** **begin**

5 next_TAP_state = ‘STATE_run_test_idle;

6 **if** (correct >= 32’h0001_FFFF)

7 passchk = 1;

8 **else** **if** (tdi_o == pass[bitindex]) **begin**

9 correct++;

10 bitindex++; **end** **end** **end**
✝ ✆
Listing 12.1: Password checking bug.

The adoption of automatic bug localization techniques can substantially reduce
the time and effort required to debug RTL designs. By enabling precise identification
of security vulnerabilities within the code, these techniques streamline the debugging process and help developers to address issues more efficiently. Consequently,
this leads to a more effective verification process, ensuring that vulnerabilities are
identified and resolved promptly.

RTL-Spec is a novel framework created to accurately identify security vulnerabilities within SoC designs at the RTL level for the first time [8]. It operates by
first applying slicing techniques to focus on relevant paths in the design, reducing
the complexity of the verification process. Subsequently, it employs spectrum-based
localization, assigning suspiciousness scores to RTL statements based on their likelihood of causing security violations. The framework further refines its analysis using
a z-score method to distinguish between incorrect and missing logic.

**290** Advances in Hardware Design for Security and Trust

Automatic bug localization represents a significant advancement in the realm of
RTL security verification. It overcomes the limitations of manual debugging methods, offering a more efficient and accurate approach to identifying and addressing
security issues. As a result, it accelerates the development life cycle and enhances
the overall security of SoC designs.

**12.5.3** **AUTOMATIC DESIGN REPAIR**

The rapid evolution of modern software systems often introduces bugs due to deprecated features, new functionalities, and architectural changes. These bugs can be
costly and destructive, with global financial impacts estimated to be billions annually. The increasing complexity of software systems exacerbates the issue, making
manual bug fixes a time-consuming and error-prone process. Notably, debugging accounts for over 50% of the software development cost [162].

To address these challenges, automatic program repair (APR) has emerged as a
crucial tool in both academia and industry. APR aims to autonomously fix software
bugs, significantly reducing the need for manual intervention. Recent advancements
in APR have shown promising results, with a substantial increase in the number
of bugs correctly fixed. This progress is largely attributed to the development of
learning-based APR techniques, which utilize deep learning (DL) to automatically
derive bug-fixing patterns from extensive code corpora.

Learning-based APR techniques offer several advantages over traditional methods. Unlike pattern-based APR, which relies on manually crafted repair templates,
learning-based approaches leverage deep learning models to learn repair patterns
from vast datasets. These techniques, such as those employing neural machine translation (NMT) models, can handle a broader range of bugs and programming languages. For instance, models like CIRCLE can generate patches across multiple languages by translating buggy code into correct code, demonstrating the versatility and
effectiveness of learning-based APR [163].

This method can be applied to SoC development to minimize unintended security vulnerabilities, as discussed in Section 12.3. Automating design repairs not only
simplifies debugging but also significantly improves SoC design security. Reducing
the manual effort needed for bug fixing can also make sure the design is free of human errors. This shift can result in more robust and secure SoC designs, reducing
vulnerabilities and enhancing overall security.

Automatic design repair (ADR) represents a significant advancement in software
engineering. It offers substantial benefits in reducing the time and effort required
for bug fixes and security verification. The ongoing development and refinement
of learning-based ADR techniques hold promise for further improving SoC design
quality and security, making ADR indispensable for the next-generation SoC development process.

**12.6** **CONCLUSION**

The rapid advancement of next-generation SoCs has introduced unprecedented levels
of complexity and functionality in modern electronic devices. As these SoCs evolve,

Security Verification for Next-Generation SoCs **291**

integrating diverse and sophisticated components into compact designs, the challenges associated with their verification become increasingly intricate. Traditional
verification techniques, while foundational, are proving inadequate in addressing the
security of these advanced systems due to several challenges such as Trojans, architectural flaws, privilege escalation attacks, etc.

In this chapter, we have highlighted the necessity of adapting and enhancing verification methodologies to meet the evolving demands of SoC security. The limitations of conventional simulation-based methods and the scalability issues of formal
verification underscore the need for innovative approaches. As we move towards
integrating AI and machine learning into SoCs, it becomes imperative to leverage
advanced verification techniques, including semi-formal methods, fuzz testing, and
penetration testing, to ensure comprehensive coverage and robust security.

The critical role of security verification cannot be overstated. In an era where
electronic devices underpin crucial sectors such as healthcare, finance, and national
security, safeguarding against vulnerabilities is of utmost importance. Security verification must be woven into every phase of SoC design, from initial concept through
to deployment, to proactively identify and mitigate potential threats. This proactive stance not only enhances the security of individual devices but also fortifies
the broader digital ecosystem against emerging threats.

Looking forward, it is clear that the ongoing development of advanced verification
strategies and tools will be essential for maintaining the integrity and resilience of
next-generation SoCs. As research and technology continue to evolve, so too must
our approaches to verification, ensuring that our systems remain secure and reliable
in an increasingly complex digital landscape.

**ACKNOWLEDGMENT**

This chapter is partially funded by NSF CHEST I/UCRC CNS-1916722.

**REFERENCES**

1. Donghyeon Han and Hoi-Jun Yoo. On-Chip Training NPU-Algorithm, Architecture
and SoC Design. Springer, 2023.
2. Kangyi Qiu, Yaojun Zhang, Bonan Yan, and Ru Huang. Heterogeneous memory architecture accommodating processing-in-memory on SoC for AIoT applications. In
2022 27th Asia and South Pacific Design Automation Conference (ASP-DAC), pages
383–388. IEEE, 2022.
3. Bokyung Kim and Hai Li. Monolithic 3D stacking for neural network acceleration.
Nature Electronics, 6(12):937–938, 2023.
4. Yuan Ren, Yidong Zou, Yang Liu, Xinran Zhou, Junhao Ma, Dongyuan Zhao,
Guangfeng Wei, Yuejie Ai, Shibo Xi, and Yonghui Deng. Synthesis of orthogonally
assembled 3D cross-stacked metal oxide semiconducting nanowires. Nature materials,
19(2):203–211, 2020.
5. Mohammed Nabeel, Mohammed Ashraf, Satwik Patnaik, Vassos Soteriou, Ozgur
Sinanoglu, and Johann Knechtel. 2.5D root of trust: Secure system-level integration of
untrusted chiplets. IEEE Transactions on Computers, 69(11):1611–1625, 2020.

**292** Advances in Hardware Design for Security and Trust

6. Jun-Woo Jang, Sehwan Lee, Dongyoung Kim, Hyunsun Park, Ali Shafiee Ardestani,
Yeongjae Choi, Channoh Kim, Yoojin Kim, Hyeongseok Yu, Hamzah Abdel-Aziz,
et al. Sparsity-aware and re-configurable NPU architecture for samsung flagship mobile SoC. In 2021 ACM/IEEE 48th Annual International Symposium on Computer
Architecture (ISCA), pages 15–28. IEEE, 2021.
7. Felipe Augusto da Silva, Ahmet Cagri Bagbaba, Annachiara Ruospo, Riccardo Mariani, Ghani Kanawati, Ernesto Sanchez, Matteo Sonza Reorda, Maksim Jenihhin, Said
Hamdioui, and Christian Sauer. Special session: AutoSoC    - A suite of open-source
automotive SoC benchmarks. In 2020 IEEE 38th VLSI Test Symposium (VTS), pages
1–9, 2020.
8. Samit S Miftah, Shamik Kundu, Austin Mordahl, Shiyi Wei, and Kanad Basu. RTLSpec: RTL spectrum analysis for security bug localization. In 2024 IEEE International
Symposium on Hardware Oriented Security and Trust (HOST), pages 171–181. IEEE,
2024.
9. Farimah Farahmandi, Yuanwen Huang, Prabhat Mishra, Farimah Farahmandi, Yuanwen Huang, and Prabhat Mishra. System-on-chip security vulnerabilities. System-onChip Security: Validation and Verification, pages 1–13, 2020.
10. Wen Chen, Sandip Ray, Jayanta Bhadra, Magdy Abadir, and Li-C Wang. Challenges
and trends in modern SoC design verification. IEEE Design & Test, 34(5):7–22,
2017.
11. Nusrat Farzana, Avinash Ayalasomayajula, Fahim Rahman, Farimah Farahmandi, and
Mark Tehranipoor. SAIF: Automated asset identification for security verification at
the register transfer level. In 2021 IEEE 39th VLSI Test Symposium (VTS), pages 1–7.
IEEE, 2021.
12. Kimia Zamiri Azar, Muhammad Monir Hossain, Arash Vafaei, Hasan Al Shaikh, Nurun N Mondol, Fahim Rahman, Mark Tehranipoor, and Farimah Farahmandi. Fuzz,
penetration, and ai testing for soc security verification: Challenges and solutions. Cryptology ePrint Archive, 2022.
13. Rahul Kande, Addison Crump, Garrett Persyn, Patrick Jauernig, Ahmad-Reza Sadeghi,
Aakash Tyagi, and Jeyavijayan Rajendran. TheHuzz: Instruction fuzzing of processors
using Golden-Reference models for finding Software-Exploitable vulnerabilities. In
31st USENIX Security Symposium (USENIX Security 22), pages 3219–3236, 2022.
14. Kevin Laeufer, Jack Koenig, Donggyu Kim, Jonathan Bachrach, and Koushik Sen.
RFUZZ: Coverage-directed fuzz testing of RTL on fpgas. In 2018 IEEE/ACM International Conference on Computer-Aided Design (ICCAD), pages 1–8. IEEE, 2018.
15. Jaewon Hur, Suhwan Song, Dongup Kwon, Eunjin Baek, Jangwoo Kim, and Byoungyoung Lee. DifuzzRTL: Differential fuzz testing to find CPU bugs. In 2021 IEEE
Symposium on Security and Privacy (SP), pages 1286–1303. IEEE, 2021.
16. Chen Chen, Rahul Kande, Nathan Nguyen, Flemming Andersen, Aakash Tyagi,
Ahmad-Reza Sadeghi, and Jeyavijayan Rajendran. HyPFuzz: Formal-assisted processor fuzzing. In 32nd USENIX Security Symposium (USENIX Security 23), pages
1361–1378, 2023.
17. Xingyu Meng, Shamik Kundu, Arun K Kanuparthi, and Kanad Basu. RTL-contest:
Concolic testing on RTL for detecting security vulnerabilities. IEEE Transactions on
Computer-Aided Design of Integrated Circuits and Systems, 41(3):466–477, 2021.
18. Edmund M Clarke, William Klieber, Miloˇs Nov´aˇcek, and Paolo Zuliani. Model checking and the state explosion problem. In LASER Summer School on Software Engineering, pages 1–30. Springer, 2011.

Security Verification for Next-Generation SoCs **293**

19. Wilayat Khan, Muhammad Kamran, Syed Rameez Naqvi, Farrukh Aslam Khan,
Ahmed S Alghamdi, and Eesa Alsolami. Formal verification of hardware components in critical systems. Wireless Communications and Mobile Computing,
2020(1):7346763, 2020.
20. cwe - common weakness enumeration. Accessed: 06/28/2024.
21. Michael Howard and Steve Lipner. The security development lifecycle, volume 8. Microsoft Press Redmond, 2006.
22. Robert Brayton and Alan Mishchenko. ABC: An academic industrial-strength verification tool. In Computer Aided Verification: 22nd International Conference, CAV 2010,
Edinburgh, UK, July 15-19, 2010. Proceedings 22, pages 24–40. Springer, 2010.
23. Clifford Wolf. Formal verification with symbiyosys and Yosys-SMTBMC. URL
[http://www. clifford. at/papers/2017/smtbmc-sby/slides. pdf, 2017.](http://www.clifford.at/papers/2017/smtbmc-sby/slides.pdf)
24. Robert Beers. Pre-RTL formal verification: An intel experience. In Proceedings of the
45th annual design automation conference, pages 806–811. Association for Computing
Machinery, 2008.
25. Alfred Koelbl, Yuan Lu, and Anmol Mathur. Embedded tutorial: Formal equivalence checking between system-level models and RTL. In ICCAD-2005. IEEE/ACM
International Conference on Computer-Aided Design, 2005, pages 965–971. IEEE,
2005.
26. Mohit Tiwari, Jason K Oberg, Xun Li, Jonathan Valamehr, Timothy Levin, Ben Hardekopf, Ryan Kastner, Frederic T Chong, and Timothy Sherwood. Crafting a usable
microkernel, processor, and I/O system with strict and provable information flow security. ACM SIGARCH Computer Architecture News, 39(3):189–200, 2011.
27. Armaiti Ardeshiricham, Wei Hu, and Ryan Kastner. Clepsydra: Modeling timing flows
in hardware designs. In 2017 IEEE/ACM International Conference on Computer-Aided
Design (ICCAD), pages 147–154. IEEE, 2017.
28. Xun Li, Mohit Tiwari, Jason K Oberg, Vineeth Kashyap, Frederic T Chong, Timothy
Sherwood, and Ben Hardekopf. Caisson: A hardware description language for secure
information flow. ACM Sigplan Notices, 46(6):109–120, 2011.
29. Xun Li, Vineeth Kashyap, Jason K Oberg, Mohit Tiwari, Vasanth Ram Rajarathinam,
Ryan Kastner, Timothy Sherwood, Ben Hardekopf, and Frederic T Chong. Sapper:
A language for hardware-level security policy enforcement. In Proceedings of the
19th international conference on Architectural support for programming languages
and operating systems, pages 97–112, 2014.
30. Danfeng Zhang, Yao Wang, G Edward Suh, and Andrew C Myers. A hardware design language for timing-sensitive information-flow security. ACM Sigplan Notices,
50(4):503–516, 2015.
31. Sujit Kumar Muduli, Gourav Takhar, and Pramod Subramanyan. Hyperfuzzing for SoC
security validation. In Proceedings of the 39th International Conference on ComputerAided Design, pages 1–9, 2020.
32. Dian-Lun Lin, Yanqing Zhang, Haoxing Ren, Brucek Khailany, Shih-Hsin Wang, and
Tsung-Wei Huang. GenFUZZ: GPU-accelerated hardware fuzzing using genetic algorithm with multiple inputs. In 2023 60th ACM/IEEE Design Automation Conference
(DAC), pages 1–6. IEEE, 2023.
33. Chen Chen, Vasudev Gohil, Rahul Kande, Ahmad-Reza Sadeghi, and Jeyavijayan Rajendran. PSOFuzz: Fuzzing processors with particle swarm optimization. In 2023
IEEE/ACM International Conference on Computer Aided Design (ICCAD), pages 1–9.
IEEE, 2023.

**294** Advances in Hardware Design for Security and Trust

34. Matt Bishop. About penetration testing. IEEE Security & Privacy, 5(6):84–87, 2007.
35. Sugandh Shah and Babu M Mehtre. An overview of vulnerability assessment and
penetration testing techniques. Journal of Computer Virology and Hacking Techniques,
11:27–49, 2015.
36. Swarup Bhunia, Michael S Hsiao, Mainak Banga, and Seetharam Narasimhan. Hardware Trojan attacks: Threat analysis and countermeasures. Proceedings of the IEEE,
102(8):1229–1247, 2014.
37. Rajat Subhra Chakraborty, Seetharam Narasimhan, and Swarup Bhunia. Hardware
Trojan: Threats and emerging solutions. In 2009 IEEE International High Level Design
Validation and Test Workshop, pages 166–171. IEEE, 2009.
38. Mohammad Tehranipoor and Farinaz Koushanfar. A survey of hardware Trojan taxonomy and detection. IEEE Design & Test of Computers, 27(1):10–25, 2010.
39. Rajat Subhra Chakraborty, Francis Wolff, Somnath Paul, Christos Papachristou, and
Swarup Bhunia. MERO: A statistical approach for hardware Trojan detection. In
International Workshop on Cryptographic Hardware and Embedded Systems, pages
396–410. Springer, 2009.
40. Yier Jin, Nathan Kupp, and Yiorgos Makris. Experiences in hardware Trojan design
and implementation. In 2009 IEEE International Workshop on Hardware-Oriented
Security and Trust, pages 50–57. IEEE, 2009.
41. He Li, Qiang Liu, and Jiliang Zhang. A survey of hardware Trojan threat and defense.
Integration, 55:426–437, 2016.
42. Kaiyuan Yang, Matthew Hicks, Qing Dong, Todd Austin, and Dennis Sylvester. A2:
Analog malicious hardware. In 2016 IEEE symposium on security and privacy (SP),
pages 18–37. IEEE, 2016.
43. Alex Baumgarten, Michael Steffen, Matthew Clausman, and Joseph Zambreno. A
case study in hardware trojan design and implementation. International Journal of
Information Security, 10:1–14, 2011.
44. Richard L Rudell. Logic synthesis for VLSI design. University of California, Berkeley,
1989.
45. Srinivas Devadas, Abhijit Ghosh, and Kurt William Keutzer. Logic synthesis. McGrawHill, 1994.
46. Pran Kurup and Taher Abbasi. Logic synthesis using Synopsys®. Springer Science &
Business Media, 1997.
47. Kris Tiri and Ingrid Verbauwhede. Secure logic synthesis. In International Conference
on Field Programmable Logic and Applications, pages 1052–1056. Springer, 2004.
48. Eleonora Testa, Mathias Soeken, Heinz Riener, Luca Amaru, and Giovanni De Micheli.
A logic synthesis toolbox for reducing the multiplicative complexity in logic networks.
In 2020 Design, Automation & Test in Europe Conference & Exhibition (DATE), pages
568–573. IEEE, 2020.
49. Michael Vai, Ben Nahill, Josh Kramer, Michael Geis, Dan Utin, David Whelihan, and
Roger Khazan. Secure architecture for embedded systems. In 2015 IEEE High Performance Extreme Computing Conference (HPEC), pages 1–5. IEEE, 2015.
50. Congmiao Li and Jean-Luc Gaudiot. Online detection of spectre attacks using microarchitectural traces from performance counters. In 2018 30th International Symposium
on Computer Architecture and High Performance Computing (SBAC-PAD), pages 25–
28. IEEE, 2018.
51. Moritz Lipp, Michael Schwarz, Daniel Gruss, Thomas Prescher, Werner Haas, Anders
Fogh, Jann Horn, Stefan Mangard, Paul Kocher, Daniel Genkin, Yuval Yarom, and

Security Verification for Next-Generation SoCs **295**

Mike Hamburg. Meltdown: Reading kernel memory from user space. In 27th USENIX
Security Symposium (USENIX Security 18), pages 973–990, Baltimore, MD, August
2018. USENIX Association.
52. Niek Timmers and Cristofaro Mune. Escalating privileges in Linux using voltage
fault injection. In 2017 Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC), pages 1–8. IEEE, 2017.
53. Fehmi Jaafar, Gabriela Nicolescu, and Christian Richard. A systematic approach for
privilege escalation prevention. In 2016 IEEE International Conference on Software
Quality, Reliability and Security Companion (QRS-C), pages 101–108. IEEE, 2016.
54. Sanjay Das, Shamik Kundu, and Kanad Basu. Explainability to the rescue: A patternbased approach for detecting adversarial attacks. In 2024 IEEE International Symposium on Hardware Oriented Security and Trust (HOST), pages 160–170. IEEE, 2024.
55. Shamik Kundu, Sanjay Das, Sayar Karmakar, Arnab Raha, Souvik Kundu, Yiorgos
Makris, and Kanad Basu. Bit-by-bit: Investigating the vulnerabilities of binary neural
networks to adversarial bit flipping. Transactions on Machine Learning Research.
56. Sanjay Das, Shamik Kundu, and Kanad Basu. Bottlenecks in secure adoption of deep
neural networks in safety-critical applications. In 2023 IEEE 66th International Midwest Symposium on Circuits and Systems (MWSCAS), pages 801–805. IEEE, 2023.
57. Mark Seaborn and Thomas Dullien. Exploiting the dram rowhammer bug to gain kernel
privileges. Black Hat, 15(71):2, 2015.
58. Paul Kocher, Jann Horn, Anders Fogh, Daniel Genkin, Daniel Gruss, Werner Haas,
Mike Hamburg, Moritz Lipp, Stefan Mangard, Thomas Prescher, et al. Spectre attacks: Exploiting speculative execution. Communications of the ACM, 63(7):93–101,
2020.
59. YongBin Zhou and DengGuo Feng. Side-channel attacks: Ten years after its publication and the impacts on cryptographic module security testing. Cryptology ePrint
Archive, 2005.
60. Yuval Yarom and Katrina Falkner. FLUSH+ RELOAD: A high resolution, low noise,
l3 cache Side-Channel attack. In 23rd USENIX Security Symposium (USENIX Security
14), pages 719–732, 2014.
61. Fangfei Liu, Yuval Yarom, Qian Ge, Gernot Heiser, and Ruby B Lee. Last-level cache
side-channel attacks are practical. In 2015 IEEE symposium on security and privacy,
pages 605–622. IEEE, 2015.
62. Ross Mcilroy, Jaroslav Sevcik, Tobias Tebbi, Ben L Titzer, and Toon Verwaest. Spectre
is here to stay: An analysis of side-channels and speculative execution. arXiv preprint
arXiv:1902.05178, 2019.
63. Moritz Lipp, Michael Schwarz, Daniel Gruss, Thomas Prescher, Werner Haas, Stefan
Mangard, Paul Kocher, Daniel Genkin, Yuval Yarom, and Mike Hamburg. Meltdown.
arXiv preprint arXiv:1801.01207, 2018.
64. Dmitry Evtyushkin, Ryan Riley, Nael CSE Abu-Ghazaleh, ECE, and Dmitry Ponomarev. Branchscope: A new side-channel attack on directional branch predictor. ACM
SIGPLAN Notices, 53(2):693–707, 2018.
65. Onur Acıic¸mez, C¸ etin Kaya Koc¸, and Jean-Pierre Seifert. Predicting secret keys via
branch prediction. In Topics in Cryptology–CT-RSA 2007: The Cryptographers’ Track
at the RSA Conference 2007, San Francisco, CA, USA, February 5-9, 2007, pages 225–
242. Springer, 2006.
66. Hasindu Gamaarachchi and Harsha Ganegoda. Power analysis based side channel attack. arXiv preprint arXiv:1801.00932, 2018.

**296** Advances in Hardware Design for Security and Trust

67. Stefan Mangard. A simple power-analysis (SPA) attack on implementations of the
AES key expansion. In Information Security and Cryptology—ICISC 2002: 5th International Conference Seoul, Korea, November 28–29, 2002 Revised Papers 5, pages
343–358. Springer, 2003.
68. Paul Kocher, Joshua Jaffe, and Benjamin Jun. Differential power analysis. In Advances in Cryptology—CRYPTO’99: 19th Annual International Cryptology Conference Santa Barbara, California, USA, August 15–19, 1999. Proceedings 19, pages
388–397. Springer, 1999.
69. Eric Brier, Christophe Clavier, and Francis Olivier. Correlation power analysis with
a leakage model. In Cryptographic Hardware and Embedded Systems-CHES 2004:
6th International Workshop Cambridge, MA, USA, August 11-13, 2004. Proceedings
6, pages 16–29. Springer, 2004.
70. Pankaj Rohatgi. Electromagnetic attacks and countermeasures. Cryptographic Engineering, pages 407–430, 2009.
71. Adib Nahiyan and Mark Tehranipoor. Code coverage analysis for IP trust verification.
Hardware IP security and trust, pages 53–72, 2017.
72. Samit S Miftah, Kshitij Raj, Xingyu Meng, Sandip Ray, and Kanad Basu. Systemon-chip information flow validation under asynchronous resets. IEEE Transactions on
Computer-Aided Design of Integrated Circuits and Systems, 2024.
73. Onur Mutlu and Jeremie S Kim. Rowhammer: A retrospective. IEEE Transactions on
Computer-Aided Design of Integrated Circuits and Systems, 39(8):1555–1571, 2019.
74. Tom St Denis. Cryptography for developers. Elsevier, 2006.
75. Yevgeniy Dodis, David Pointcheval, Sylvain Ruhault, Damien Vergniaud, and Daniel
Wichs. Security analysis of pseudo-random number generators with input: /dev/random is not robust. In Proceedings of the 2013 ACM SIGSAC conference on Computer
& communications security, pages 647–658, 2013.
76. Werner Schindler. Random number generators for cryptographic applications. Cryptographic Engineering, pages 5–23, 2009.
77. Donghang Lu, Pedro Moreno-Sanchez, Amanuel Zeryihun, Shivam Bajpayi, Sihao
Yin, Ken Feldman, Jason Kosofsky, Pramita Mitra, and Aniket Kate. Reducing automotive counterfeiting using blockchain: Benefits and challenges. In 2019 IEEE International Conference on Decentralized Applications and Infrastructures (DAPPCON),
pages 39–48. IEEE, 2019.
78. Douglas A Bodner. Enterprise modeling framework for counterfeit parts in defense
systems. Procedia Computer Science, 36:425–431, 2014.
79. Miron Abramovici and Paul Bradley. Integrated circuit security: New threats and solutions. In Proceedings of the 5th Annual Workshop on Cyber Security and Information
Intelligence Research: Cyber Security and Information Intelligence Challenges and
Strategies, pages 1–3, 2009.
80. Daniel DiMase, Zachary A Collier, Jinae Carlson, Robin B Gray Jr, and Igor Linkov.
Traceability and risk analysis strategies for addressing counterfeit electronics in supply
chains for complex systems. Risk Analysis, 36(10):1834–1843, 2016.
81. Ujjwal Guin, Ke Huang, Daniel DiMase, John M Carulli, Mohammad Tehranipoor,
and Yiorgos Makris. Counterfeit integrated circuits: A rising threat in the global semiconductor supply chain. Proceedings of the IEEE, 102(8):1207–1228, 2014.
82. Sandip Ray, Eric Peeters, Mark M Tehranipoor, and Swarup Bhunia. System-on-chip
platform security assurance: Architecture and validation. Proceedings of the IEEE,
106(1):21–37, 2017.

Security Verification for Next-Generation SoCs **297**

83. Atul Prasad Deb Nath, Sandip Ray, Abhishek Basak, and Swarup Bhunia. System-onchip security architecture and cad framework for hardware patch. In 2018 23rd Asia
and South Pacific Design Automation Conference (ASP-DAC), pages 733–738. IEEE,
2018.
84. Abhishek Basak, Swarup Bhunia, Thomas Tkacik, and Sandip Ray. Security assurance for system-on-chip designs with untrusted ips. IEEE Transactions on Information
Forensics and Security, 12(7):1515–1528, 2017.
85. Xingyu Meng, Kshitij Raj, Sandip Ray, and Kanad Basu. SeVNoC: Security validation
of system-on-chip designs with NoC fabrics. IEEE Transactions on Computer-Aided
Design of Integrated Circuits and Systems, 42(2):672–682, 2022.
86. Xingyu Meng, Kshitij Raj, Atul Prasad Deb Nath, Kanad Basu, and Sandip Ray. Soccar: Detecting system-on-chip security violations under asynchronous resets. In 2021
58th ACM/IEEE Design Automation Conference (DAC), pages 625–630. IEEE, 2021.
87. Paolo Prinetto, Gianluca Roascio, et al. Hardware security, vulnerabilities, and attacks:
A comprehensive taxonomy. In ITASEC, pages 177–189, 2020.
88. Weizhe Hua, Zhiru Zhang, and G Edward Suh. Reverse engineering convolutional
neural networks through side-channel information leaks. In Proceedings of the 55th
Annual Design Automation Conference, pages 1–6, 2018.
89. Jungmin Park, Adib Nahiyan, Apostol Vassilev, Yier Jin, Mark Tehranipoor, et al.
RTL-PSC: Automated power side-channel leakage assessment at register-transfer level.
arXiv e-prints, pages arXiv–1901, 2019.
90. Anand Menon, Amisha Srivastava, Shamik Kundu, and Kanad Basu. Application profiling using register-instruction hardware performance counters. In 2023 IEEE Computer Society Annual Symposium on VLSI (ISVLSI), pages 1–6, 2023.
91. Amisha Srivastava, Sneha Thakur, Abraham Peedikayil Kuruvila, Poras T. Balsara,
and Kanad Basu. Hardware-based detection of malicious firmware modification in
microgrids. In 2024 37th International Conference on VLSI Design and 2024 23rd
International Conference on Embedded Systems (VLSID), pages 186–191, 2024.
92. Adib Nahiyan, Kan Xiao, Kun Yang, Yeir Jin, Domenic Forte, and Mark Tehranipoor.
AVFSM: A framework for identifying and mitigating vulnerabilities in FSMs. In Proceedings of the 53rd Annual Design Automation Conference, pages 1–6, 2016.
93. Adib Nahiyan, Farimah Farahmandi, Prabhat Mishra, Domenic Forte, and Mark Tehranipoor. Security-aware fsm design flow for identifying and mitigating vulnerabilities
to fault attacks. IEEE Transactions on Computer-aided design of integrated circuits
and systems, 38(6):1003–1016, 2018.
94. Kanad Basu, Samah Mohamed Saeed, Christian Pilato, Mohammed Ashraf, Mohammed Thari Nabeel, Krishnendu Chakrabarty, and Ramesh Karri. Cad-base: An
attack vector into the electronics supply chain. ACM Transactions on Design Automation of Electronic Systems (TODAES), 24(4):1–30, 2019.
95. Yuanwen Huang, Anupam Chattopadhyay, and Prabhat Mishra. Trace buffer attack:
Security versus observability study in post-silicon debug. In 2015 IFIP/IEEE International Conference on Very Large Scale Integration (VLSI-SoC), pages 355–360. IEEE,
2015.
96. Yuanwen Huang and Prabhat Mishra. Trace buffer attack on the AES cipher. Journal
of Hardware and Systems Security, 1:68–84, 2017.
97. Jeremy Lee, M Tebranipoor, and Jim Plusquellic. A low-cost solution for protecting
ips against scan-based side-channel attacks. In 24th IEEE VLSI Test Symposium, pages
6–pp. IEEE, 2006.

**298** Advances in Hardware Design for Security and Trust

98. Basel Halak. CIST: A threat modelling approach for hardware supply chain security.
Hardware Supply Chain Security: Threat Modelling, Emerging Attacks and Countermeasures, pages 3–65, 2021.
99. Frank E McFadden and Richard D Arnold. Supply chain risk mitigation for it electronics. In 2010 IEEE International Conference on Technologies for Homeland Security
(HST), pages 49–55. IEEE, 2010.
100. Yier Jin, Dzmitry Maliuk, and Yiorgos Makris. Post-deployment trust evaluation in
wireless cryptographic ICs. In 2012 Design, Automation & Test in Europe Conference
& Exhibition (DATE), pages 965–970. IEEE, 2012.
101. Prabhat Mishra, Swarup Bhunia, and Mark Tehranipoor. Hardware IP security and
trust. Springer, 2017.
102. Xiaoxuan Lou, Tianwei Zhang, Jun Jiang, and Yinqian Zhang. A survey of microarchitectural side-channel vulnerabilities, attacks, and defenses in cryptography. ACM
Computing Surveys (CSUR), 54(6):1–37, 2021.
103. Chao Su and Qingkai Zeng. Survey of CPU cache-based side-channel attacks: Systematic analysis, security models, and countermeasures. Security and Communication
Networks, 2021(1):5559552, 2021.
104. Mark Randolph and William Diehl. Power side-channel attack analysis: A review of
20 years of study for the layman. Cryptography, 4(2):15, 2020.
105. Asanka Sayakkara, Nhien-An Le-Khac, and Mark Scanlon. A survey of electromagnetic side-channel attacks and discussion on their case-progressing potential for digital
forensics. Digital Investigation, 29:43–54, 2019.
106. Wei Hu, Armaiti Ardeshiricham, and Ryan Kastner. Hardware information flow tracking. ACM Computing Surveys (CSUR), 54(4):1–39, 2021.
107. Dorothy Elizabeth Robling Denning. Secure information flow in computer systems.
Purdue University, 1975.
108. Dorothy E Denning. A lattice model of secure information flow. Communications of
the ACM, 19(5):236–243, 1976.
109. Petros Efstathopoulos, Maxwell Krohn, Steve VanDeBogart, Cliff Frey, David Ziegler,
Eddie Kohler, David Mazieres, Frans Kaashoek, and Robert Morris. Labels and event
processes in the asbestos operating system. ACM SIGOPS Operating Systems Review,
39(5):17–30, 2005.
110. Maxwell Krohn, Alexander Yip, Micah Brodsky, Natan Cliffer, M Frans Kaashoek, Eddie Kohler, and Robert Morris. Information flow control for standard OS abstractions.
ACM SIGOPS Operating Systems Review, 41(6):321–334, 2007.
111. Nickolai Zeldovich, Silas Boyd-Wickizer, Eddie Kohler, and David Mazieres. Making
information flow explicit in histar. Communications of the ACM, 54(11):93–101, 2011.
112. Andrei Sabelfeld and Andrew C Myers. Language-based information-flow security.
IEEE Journal on selected areas in communications, 21(1):5–19, 2003.
113. Andrew C Myers and Barbara Liskov. A decentralized model for information flow
control. ACM SIGOPS Operating Systems Review, 31(5):129–142, 1997.
114. Nickolai Zeldovich, Silas Boyd-Wickizer, and David Mazieres. Securing distributed
systems with information flow control. In NSDI, volume 8, pages 293–308, 2008.
115. Jean Bacon, David Eyers, Thomas FJ-M Pasquier, Jatinder Singh, Ioannis Papagiannis, and Peter Pietzuch. Information flow control for secure cloud computing. IEEE
Transactions on network and Service Management, 11(1):76–89, 2014.
116. Shan Ao and Guo Shuangzhou. A enhancement technology about system security
based on dynamic information flow tracking. In 2011 2nd International Conference

Security Verification for Next-Generation SoCs **299**

on Artificial Intelligence, Management Science and Electronic Commerce (AIMSEC),
pages 6108–6111. IEEE, 2011.
117. Manuel Egele, Christopher Kruegel, Engin Kirda, Heng Yin, and Dawn Song. Dynamic
spyware analysis. In 2007 USENIX Annual Technical Conference on Proceedings of
the USENIX Annual Technical Conference, pages 1–14, 2007.
118. Andreas Moser, Christopher Kruegel, and Engin Kirda. Exploring multiple execution
paths for malware analysis. In 2007 IEEE Symposium on Security and Privacy (SP’07),
pages 231–245. IEEE, 2007.
119. James Newsome and Dawn Xiaodong Song. Dynamic taint analysis for automatic
detection, analysis, and signature generation of exploits on commodity software. In
NDSS, volume 5, pages 3–4. Citeseer, 2005.
120. G Edward Suh, Jae W Lee, David Zhang, and Srinivas Devadas. Secure program
execution via dynamic information flow tracking. ACM Sigplan Notices, 39(11):85–
96, 2004.
121. Yier Jin and Yiorgos Makris. Proof carrying-based information flow tracking for data
secrecy protection and hardware trust. In 2012 IEEE 30th VLSI Test Symposium (VTS),
pages 252–257. IEEE, 2012.
122. Matthew Hicks, Cynthia Sturton, Samuel T King, and Jonathan M Smith. SPECS:
A lightweight runtime mechanism for protecting software from security-critical processor bugs. In Proceedings of the Twentieth International Conference on Architectural Support for Programming Languages and Operating Systems, pages 517–529,
2015.
123. Smruti R Sarangi, Abhishek Tiwari, and Josep Torrellas. Phoenix: Detecting and recovering from permanent processor design bugs with programmable hardware. In 2006
39th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO’06),
pages 26–37. IEEE, 2006.
124. Ilya Wagner and Valeria Bertacco. Engineering trust with semantic guardians. In
2007 Design, Automation & Test in Europe Conference & Exhibition, pages 1–6. IEEE,
2007.
125. Eric Love, Yier Jin, and Yiorgos Makris. Proof-carrying hardware intellectual property:
A pathway to trusted module acquisition. IEEE Transactions on Information Forensics
and Security, 7(1):25–40, 2011.
126. Bruno Barras. Coq en coq. PhD thesis, INRIA, 1996.
127. Rui Zhang, Calvin Deutschbein, Peng Huang, and Cynthia Sturton. End-to-end automated exploit generation for validating the security of processor designs. In 2018 51st
Annual IEEE/ACM International Symposium on Microarchitecture (MICRO), pages
815–827. IEEE, 2018.
128. Yangdi Lyu and Prabhat Mishra. Scalable concolic testing of RTL models. IEEE
Transactions on Computers, 70(7):979–991, 2020.
129. R.D. Craig and S.P. Jaskiel. Systematic Software Testing. Artech House ITS library.
Artech House, 2002.
130. Michael Sutton, Adam Greene, and Pedram Amini. Fuzzing: Brute force vulnerability
discovery. Pearson Education, 2007.
131. Xiaogang Zhu, Sheng Wen, Seyit Camtepe, and Yang Xiang. Fuzzing: A survey for
roadmap. ACM Computing Surveys, 54(11s):1–36, 2022.
132. Ari Takanen, Jared D Demott, Charles Miller, and Atte Kettunen. Fuzzing for software
security testing and quality assurance. Artech House, 2018.

**300** Advances in Hardware Design for Security and Trust

133. Kostya Serebryany. OSS-Fuzz - Google’s continuous fuzzing service for open source
software. In Proceedings of the 26th USENIX Security Symposium, Vancouver, BC,
August 2017. USENIX Association.
134. Valentin JM Man`es, HyungSeok Han, Choongwoo Han, Sang Kil Cha, Manuel Egele,
Edward J Schwartz, and Maverick Woo. The art, science, and engineering of fuzzing:
A survey. IEEE Transactions on Software Engineering, 47(11):2312–2331, 2019.
135. Samuel Groß. FuzzIL: Coverage guided fuzzing for javascript engines. Department of
Informatics, Karlsruhe Institute of Technology, 2018.
136. LaShanda Dukes, Xiaohong Yuan, and Francis Akowuah. A case study on web application security testing with tools and manual testing. In 2013 Proceedings of IEEE
Southeastcon, pages 1–6. IEEE, 2013.
137. [https://github.com/google/syzkaller.](https://github.com/google/syzkaller) Accessed: 04/03/2024.
138. Wen Xu, Soyeon Park, and Taesoo Kim. Freedom: Engineering a state-of-the-art dom
fuzzer. In Proceedings of the 2020 ACM SIGSAC Conference on Computer and Communications Security, pages 971–986, 2020.
139. [https://google.github.io/clusterfuzz/.](https://google.github.io/clusterfuzz) Accessed: 04/03/2024.
140. Zalewski Michal. [https://lcamtuf.coredump.cx/afl/.](https://lcamtuf.coredump.cx/afl) Accessed: 04/03/2024.
141. Marcel B¨ohme, Van-Thuan Pham, and Abhik Roychoudhury. Coverage-based greybox
fuzzing as Markov chain. In Proceedings of the 2016 ACM SIGSAC Conference on
Computer and Communications Security, pages 1032–1043, 2016.
142. Maximilian Beckmann and Jan Steffan. Coverage-guided fuzzing of embedded systems leveraging hardware tracing. In Computer Security. ESORICS 2022 International
Workshops, pages 362–378, Cham, 2023. Springer International Publishing.
143. Andrea Fioraldi, Dominik Maier, Heiko Eißfeldt, and Marc Heuse. AFL++ : Combining incremental steps of fuzzing research. In 14th USENIX Workshop on Offensive
Technologies (WOOT 20). USENIX Association, August 2020.
144. Marcel B¨ohme, Van-Thuan Pham, Manh-Dung Nguyen, and Abhik Roychoudhury.
Directed greybox fuzzing. In Proceedings of the 2017 ACM SIGSAC Conference on
Computer and Communications Security, pages 2329–2344, 2017.
145. Jonghyeon Cho, Taehun Kim, Soojin Kim, Miok Im, Taehyun Kim, and Youngjoo
Shin. Real-time detection for cache side channel attack using performance counter
monitor. Applied Sciences, 10(3):984, 2020.
146. Md Shohidul Islam, Abraham Peedikayil Kuruvila, Kanad Basu, and Khaled N Khasawneh. ND-HMDs: Non-differentiable hardware malware detectors against evasive
transient execution attacks. In 2020 IEEE 38th International Conference on Computer
Design (ICCD), pages 537–544. IEEE, 2020.
147. Manaar Alam, Sarani Bhattacharya, Debdeep Mukhopadhyay, and Sourangshu Bhattacharya. Performance counters to rescue: A machine learning based safeguard against
micro-architectural side-channel-attacks. Cryptology ePrint Archive, 2017.
148. Faizan Shoaib, Yang-Wai Chow, Elena Vlahu-Gjorgievska, and Chau Nguyen. Mitigating timing side-channel attacks in software-defined networks: Detection and response.
In Telecom, volume 4, pages 877–900. MDPI, 2023.
149. Gilles Barthe, Benjamin Gr´egoire, and Vincent Laporte. Secure compilation of
side-channel countermeasures: The case of cryptographic “constant-time”. In 2018
IEEE 31st Computer Security Foundations Symposium (CSF), pages 328–343. IEEE,
2018.
150. Lang Lin et al. Fast and comprehensive simulation methodology for layout-based
power-noise side-channel leakage analysis. In 2020 IEEE iSES, 2020.

Security Verification for Next-Generation SoCs **301**

151. Haocheng others Ma. Pathfinder: Side channel protection through automatic leaky
paths identification and obfuscation. In DAC, 2022.
152. Navyata Gattu et al. Power side channel attack analysis and detection. In Proceedings
of the 39th International Conference on Computer-Aided Design, 2020.
153. Tao Zhang et al. PSC-TG: RTL power side-channel leakage assessment with test pattern generation. In 58th ACM/IEEE DAC, 2021.
154. Amisha Srivastava, Sanjay Das, Navnil Choudhury, Rafail Psiakis, Pedro Henrique
Silva, Debjit Pal, and Kanad Basu. SCAR: Power side-channel analysis at RTL level.
IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 32(6):1110–1123,
2024.
155. Xingyu Meng, Amisha Srivastava, Ayush Arunachalam, Avik Ray, Pedro Henrique
Silva, Rafail Psiakis, Yiorgos Makris, and Kanad Basu. Unlocking hardware security
assurance: The potential of LLMs. arXiv preprint arXiv:2308.11042, 2023.
156. Samit Shahnawaz Miftah, Amisha Srivastava, Hyunmin Kim, and Kanad Basu. AssertO: Context-based assertion optimization using LLMs. In Proceedings of the Great
Lakes Symposium on VLSI 2024, pages 233–239, 2024.
157. Rahul Kande, Hammond Pearce, Benjamin Tan, Brendan Dolan-Gavitt, Shailja
Thakur, Ramesh Karri, and Jeyavijayan Rajendran. (Security) assertions by large language models. IEEE Transactions on Information Forensics and Security, 2024.
158. Sudipta Paria, Aritra Dasgupta, and Swarup Bhunia. DIVAS: An LLM-based end-toend framework for SoC security analysis and policy-based protection. arXiv preprint
arXiv:2308.06932, 2023.
159. W Eric Wong, Ruizhi Gao, Yihao Li, Rui Abreu, and Franz Wotawa. A survey on
software fault localization. IEEE Transactions on Software Engineering, 42(8):707–
740, 2016.
160. Mark Weiser. Program slicing. IEEE Transactions on Software Engineering, SE10(4):352–357, 1984.
161. James A. Jones and Mary Jean Harrold. Empirical evaluation of the tarantula automatic
fault-localization technique. In Proceedings of the 20th IEEE/ACM International Conference on Automated Software Engineering, ASE ’05, page 273–282, New York, NY,
USA, 2005. Association for Computing Machinery.
162. Tom Britton, Lisa Jeng, Graham Carver, Paul Cheak, and Tomer Katzenellenbogen.
Reversible debugging software. Judge Bus. School, Univ. Cambridge, Cambridge, UK,
Tech. Rep, 229, 2013.
163. Wei Yuan, Quanjun Zhang, Tieke He, Chunrong Fang, Nguyen Quoc Viet Hung, Xiaodong Hao, and Hongzhi Yin. Circle: Continual repair across programming languages. In Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis, pages 678–690, 2022.

# 13 Cloud FPGA Accelerator
### Fingerprinting Using Communication Side Channels

Chongzhou Fang, Ning Miao, Han Wang, Jiacheng Zhou, Tyler Sheaves, John M. Emmert,
Avesta Sasan, and Houman Homayoun

In recent years, cloud computing has revolutionized the way computational power
and storage resources are accessed, offering scalable infrastructure that meets growing demand through a flexible, pay-as-you-go model. <sup>1</sup> Public cloud services have
enabled users to forgo the burden of establishing and maintaining their own physical infrastructure, significantly reducing costs and enhancing operational efficiency.
Infrastructure-as-a-Service (IaaS) platforms have opened doors for new applications
requiring intensive computation, such as large-scale simulations [1] and deep learning [2]. The rising demand for such applications has driven the adoption of specialized hardware accelerators, including GPUs [3], Fileld programmable gate arrays
(FPGAs) [4], and application-specific integrated circuits (ASICs) [5]. Among these,
FPGA-based CPU architectures are particularly attractive for cloud environments
due to their high performance, adaptability, and energy efficiency.

Leading cloud providers, including AWS [6] and Microsoft Azure [7], have embraced FPGA technology by introducing FPGA-enabled services. Recently, both the
academia and the industry have begun exploring multi-tenant FPGA infrastructure,
which enables multiple users to share a single FPGA, maximizing hardware utilization. Although this multi-tenancy model has the potential to improve resource
efficiency, it also introduces significant security challenges, as multiple user circuits
are co-located on shared hardware, increasing the risk of malicious attacks. This has
sparked research into various security threats. Previous studies have identified vulnerabilities in FPGAs that could be exploited through methods such as bitstream
fault injection [8], hardware Trojans [9], and rowhammer attacks [10]. Remote
attacks on cloud FPGAs have further escalated these concerns, with a growing body

1This chapter was originally published as a regular paper at ACM CCS 2023 [15].

[DOI: 10.1201/9781003510949-13](https://doi.org/10.1201/9781003510949-13) **302**

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **303**

of work examining threats specific to multi-tenant environments, where attackers can
exploit side channels to retrieve information on co-located circuits [11, 12]. Power
side channel and fault attacks on FPGA clouds have been demonstrated [13], exposing the need for improved defenses against such threats.

A notable limitation of existing attacks, however, is their dependency on prior
knowledge of the specific FPGA circuit under attack. For example, the remote fault
injection attack detailed in [14] requires that the target FPGA is running an AES encryption circuit, while Moini et al. [11] rely on power side channel traces to recover
MNIST inputs [16] based on a known binarized neural network (BNN) accelerator.
This reliance on circuit-specific knowledge constrains the scope and applicability of
these attacks, leaving unexplored security gaps that could further jeopardize FPGA
cloud infrastructures.

This chapter investigates a new approach to FPGA cloud vulnerabilities, focusing on the feasibility of circuit fingerprinting via side channel information from
shared communication links, such as the Peripheral Component Interconnect Express (PCIe) [17]. PCIe is widely used to connect FPGAs to host machines in cloud
infrastructures, providing an open communication channel that attackers can target.
By stressing the shared PCIe link, it is possible to capture distinctive I/O patterns,
enabling attackers to infer the types of circuits co-located within the same FPGA
board and consequently facilitating previously proposed attacks [14].

To explore this vulnerability, we develop a custom measurement accelerator (referred to as an “accelerator” hereafter) that stresses PCIe through repeated read and
write operations to host memory in the cloud environment (Intel DevCloud [18] in
this work). We measure the PCIe bandwidth as the accelerator coexists with different
victim accelerators on the same FPGA, allowing us to gather side channel traces. By
analyzing these traces using machine learning, we classify the victim accelerators
based on their unique communication patterns. Additionally, we assess how varying
levels of PCIe contention impact fingerprinting success rates, implementing a prototype attack to detect the presence of specific victim circuits in cloud settings, thereby
laying groundwork for future research.

In summary, the main contributions of this work include:

1. A novel attack model targeting multi-tenant FPGA clouds, allowing attackers to gather information on co-located applications, thus enhancing subsequent attack capabilities.
2. A proof-of-concept implementation of an attack accelerator and host program that captures unique communication fingerprints from co-located accelerators.
3. A thorough evaluation of our method, with four classification algorithms
tested in both closed-world and open-world settings, achieving up to 90%
and 80% success rates, respectively.
4. Identification of a previously unaddressed security vulnerability in FPGA
communication links, highlighting areas for potential improvement in the
design of hardware and software defenses for heterogeneous computing
environments.

**304** Advances in Hardware Design for Security and Trust

**13.1** **BACKGROUND**

**13.1.1** **CLOUD FPGA**

FPGAs are integrated circuits designed for post-manufacturing programmability. Today, FPGAs are widely used to implement custom hardware solutions, such as accelerators for machine learning tasks. Recently, cloud providers have started offering
FPGA resources as part of their services. The advent of multi-tenant FPGA clouds
further introduces the option for multiple users to share a single FPGA simultaneously [19]. Cloud FPGAs provide customers with remote access to powerful FPGA
resources. Different providers supply varied FPGA models: Intel’s DevCloud grants
access to Arria 10 and Stratix 10 FPGAs [20]; AWS offers Xilinx Virtex UltraScale+
FPGAs in their F1 instances [21]; and Alibaba Cloud supplies Xilinx Kintex UltraScale and Arria 10 FPGAs [22], among others.

**13.1.2** **SECURITY PROBLEMS OF CLOUD FPGA**

In multi-tenant FPGA clouds, it has been proposed that circuits from multiple users
can be placed on the same FPGA, which makes FPGA resource utilization on the
cloud more efficient. However, recent research works have shown that cloud FPGAs
are vulnerable to various types of side channel attacks in a multi-tenant setting. Once
the security of these FPGA accelerators is compromised, sensitive data or secret keys
they are processing can be revealed, which may lead to unwanted data leakage and
potentially harm the profits of cloud providers. The following types of attacks are
studied most extensively in literature.

**13.1.2.1** **Long-Wire Side Channel Attack**

Long wires, one type of FPGA routing resources that are used to connect configurable logic blocks (CLBs), have been proved to be a source of side channel information leakage. In [23], the authors find that when a long wire on FPGA is transmitting
a logical 1, the delay of the nearby long wires is shorter than when it is transmitting
a logical 0. Based on this phenomenon, the authors propose to measure the delay of
long wires by connecting ring oscillators (ROs) to them. When the target long wire
is transmitting a logical 1, the delay of the nearby long wires will decrease, which
causes the frequency of the ROs to increase. By monitoring the frequency change
of the ROs in a fixed time interval, the authors successfully recovered 99% of the
bits that are being transmitted in the target long wire. Similarly, in [24] the authors
recovered the secret key of an AES implementation using the long-wire side channel
attack.

**13.1.2.2** **Power Side Channel Attack**

In certain FPGA circuits (e.g., cryptographic circuits), power consumption may be
influenced by data being processed in the circuits; hence, this information may be
monitored and used to recover secrets (e.g., cryptographic keys). Normally, deploying power side channel attacks requires physical access to the FPGA boards in order

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **305**

to assess the system’s power usage. Although direct access to cloud FPGAs is not
achievable, Zhao et al. [25] propose a power side channel attack using FPGA as a
power monitor. The authors created an RO-based on-chip power monitor and prove
that the RO-based FPGA power monitor may be utilized for a power analysis attack
on an RSA crypto module on the same FPGA. Furthermore, in [26], the authors proposed a new design for the RO-based power sensor, which can measure the internal
voltage in nanosecond scale. They are able to successfully retrieve the secret key of
an AES encryption circuit using the power side channel.

A power side channel can also be used for accelerator fingerprinting, as shown
in [27]. However, in this chapter, we will show that communication side channel can
be a better option, which has less stringent requirements for attackers.

**13.1.2.3** **PCIe Side Channel Attack**

PCIe contention side channel has been utilized before to retrieve secret information
from CPU-GPU systems [28]. In [29], the authors used PCIe contention to perform
an attack on the AWS server. The authors observed that the difference in locations of
PCIe slots in the PCIe topology can result in disparate latency and bandwidth. Based
on this, they were able to detect the bandwidth change when different FPGAs in the
same sever attempted simultaneous memory accesses to generate PCIe contention
and successfully reverse-engineer the locality of different FPGAs in the same AWS
server. However, unlike our work, [29] focused on revealing infrastructure information instead of revealing information about applications on the same FPGA.

The existing attacks targeting the FPGA cloud presume the knowledge of the colocated victim circuit is provided. In fact, this information is nearly impossible to
be obtained directly. In response, our work focuses on inferring co-located FPGAaccelerated workloads using PCIe contention side channel information. Previously
proposed attacks will benefit from our attack method.

**13.2** **THREAT MODEL**

This work operates under assumptions consistent with prior studies [12, 13], particularly that circuits from multiple users can be co-located on the same FPGA device,
which is connected to a shared host. This setup mirrors co-location attacks commonly
seen in cloud environments [30–32]. While no direct connections or communication
channels exist between user circuits, all circuits share the FPGA-to-host communication link (e.g., via PCIe), as well as its associated protocols. Our objective is to
highlight the security risks posed by this shared communication infrastructure.

Both attacker and victim users are assumed to possess equal privileges within the
cloud environment, with attackers having no additional features or access beyond
what is available to victims. The attackers’ primary aim in our setup is to infer information about co-located user applications—an aspect largely unaddressed in existing research on cloud FPGA side channel attacks. We explore two scenarios: (1)
a closed-world model, where attackers have a limited set of potential co-located accelerators to consider; and (2) an open-world model, where attackers are unaware of

**306** Advances in Hardware Design for Security and Trust

the types of accelerators co-located with them. In both cases, the attacker has access
to an FPGA-hosted server configured similarly to a cloud-based FPGA setup.

We assume that cloud service providers act as neutral entities and do not alter
user-uploaded designs. Applications and their host programs are assumed to run as
deployed, and our attack accelerator, which performs only seemingly benign operations, may require specialized detection measures for mitigation. We further assume
that service providers will not intervene to terminate our accelerators or host programs. Since the methods proposed in this chapter only involve standard I/O operations without sensitive inter-user access, this assumption holds reasonably well.

We assume benign users are unaware of any malicious entities on the platform
and thus do not shut down their accelerators following the launch of attack accelerators. Victim accelerators are assumed to operate continuously, processing a steady
stream of input data—a convenient assumption, as our approach does not rely on
precise timing information of victim execution. These victim accelerators may process either encrypted or plaintext data, but they all communicate with the host via
I/O operations. The goal of our attack is to detect differences in I/O access patterns,
which can reveal characteristics of the victim’s operations.

**13.3** **METHOD AND IMPLEMENTATION**

In this section, we introduce the design of the proposed fingerprinting attack in FPGA
cloud, which consists of attack preparation and online fingerprinting as shown in
Figure 13.1. The key idea of this work is to capture the execution fingerprints of
FPGA circuits by launching a measurement accelerator to measure the bandwidth of
communication links and deducing the running victim circuits with machine learning
techniques. The whole workflow of our fingerprinting attack consists of several steps:

**Figure** **13.1** Diagram of our FPGA fingerprinting attack. Our four-stage attack
method includes: (1) an offline data collection phase; (2) an offline training phase;
(3) an online attack launch phase; and (4) an online classification phase.

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **307**

1. Run victim accelerators locally with our proposed measurement circuit to
collect data;
2. Pre-process the collected I/O measurement of possible victim accelerators
and train a machine learning-based classifier with the offline collected data
set;
3. Launch the previously used benchmark to the cloud as accelerators and
collect I/O measurements;
4. Pass online I/O traces to the trained classifier to obtain fingerprinting results.

**13.3.1** **MEASURING COMMUNICATION PERFORMANCE**

In this section, we will introduce the implementation details of the benchmark used
to stress the shared communication link and monitor I/O bandwidth. The observation
of the benchmark reflects the I/O patterns of co-located victim circuits, which can be
further leveraged to reveal the type of victim and used for our proof-of-concept(PoC)
fingerprinting attack in the FPGA cloud. We will implement our PoC benchmark
accelerator as well as the master host program under OpenCL [33] framework. The
benchmark consists of two parts: the master host program located in CPU which
orchestrates the execution of accelerators, and accelerator circuits in FPGA which
stress PCIe communication link.

**13.3.1.1** **Host Program Design**

In our PoC benchmark, the host program is responsible for:

1. Assigning appropriate resources for the operation of accelerator kernels;
2. Invoking and orchestrating accelerator kernels;
3. Measuring kernel performance using low-level function calls.

There are three design parameters in our host program: BUFFER NUM, BUFFER SIZE
and REPEAT NUM. The workflow of our host program is defined as follows. First,
the host program will allocate BUFFER NUM memory trunks of size BUFFER SIZE.
Then, these BUFFER NUM memory trunks will be accessed by the FPGA accelerator
in a pre-defined order. Each of the BUFFER NUM memory trunks will be read and
written by the accelerator, with traffic passing through the communication link. During the operation to a memory trunk, the time it takes to execute the kernel will be
recorded using profiling APIs provided by OpenCL. This information will be further
used for calculating the bandwidth of the communication link when all operations
to a memory trunk are finished. The operations to a single memory trunk may be
repeated for REPEAT NUM times and averaged to cancel the effect of noise. Finally,
the BUFFER NUM measurement of bandwidth will be combined together to form a
trace with length BUFFER NUM. The pseudo-code for the host program is shown in
Figure 13.2.

**308** Advances in Hardware Design for Security and Trust

**Figure 13.2** The pseudo-code of our host program.

**Figure 13.3** The OpenCL code of our benchmark kernel.

**13.3.1.2** **Measurement Accelerator Design**

The measurement accelerator we use in this chapter focuses on measuring the I/O
bandwidth performance. Similar to previous works that target measuring PCIe performance [17] or stressing the PCIe connection [29], our measurement accelerator
implementation follows a similar method and stresses the PCIe communication link
via massive read and write communication. There is one design parameter called
ACCESS NUM that controls how much data is written to the host. The code of our
benchmark accelerator implemented as an OpenCL kernel is shown in Figure 13.3.

First, our benchmark accelerator takes in an address pointer (dst). dst is defined as a pointer pointing to pre-allocated host memory. By doing so, we guarantee
that our FPGA accelerator will be able to access legally allocated host memory and
the generated traffic will pass the FPGA-host communication link. Our kernel then
obtains an arbitrarily assigned index to access the host memory space. The exact
index is not important in our implementation, and we only use the OpenCL API
get global id() for convenience.

Second, our accelerator enters an execution loop where host memory is accessed
multiple times via an array update operation. The same location (dst[id]) in host
memory will be updated ACCESS NUM times, where ACCESS NUM is a design parameter of our benchmark accelerator. The operation listed in Figure 13.3 ensures
that a certain amount of data is transferred and the compiler will not optimize out the
operation since every time there will be a new value written to the host memory.

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **309**

**Figure** **13.4** The diagram of our data processing flow. Each entry in the trace is a
measurement result of a buffer, and the trace is provided to ML models for further
processing.

**13.3.2** **DATA PROCESSING**

In the offline data collection phase (Step 1 of Figure 13.1), the attacker will create
a co-location environment and run benchmarks together with potential victim accelerators to collect a performance trace data set. The collected data traces will be
normalized and organized in the same data set. Each trace will be labeled according
to the types of corresponding victim accelerators.

The diagram of our data processing flow is shown in Figure 13.4. We can see
that each data point within a trace corresponds to the measurement result of kernel
execution on an assigned buffer. All the data points will be combined as a feature
vector and be fed to machine learning (ML) models for further processing.

The resulting data set will consist of all the collected traces, where each row
represents one trace. There will be BUFFER NUM +1 columns in each row, with
BUFFER NUM entries for collected bandwidth data and one entry for label. The data
set will be fed to the ML models for training.

**13.3.3** **CLASSIFIERS**

The collected traces are 1-D vectors with a fixed dimension, since the number of
data points are automatically defined by BUFFER NUM in the implementation of

**310** Advances in Hardware Design for Security and Trust

benchmark circuit. We explore multiple types of ML models to assess the potential leakage of the side channel incurred by the shared communication link. Since
we are performing classification tasks and we aim to reduce the costs of attackers
by collecting as little data as possible, we select small models that tend to perform
well under these scenarios (e.g., Random Forest [34]), which has been used in fingerprinting tasks [35] and also compare the performance of more complex models (e.g.,
convolutional neural networks). The models we examine in this chapter include:

1. 1D-Convolution [36]: 1 convolution layer, followed by a batch normalization layer, a ReLU layer, 3 layers of fully connected perceptrons [37], and
a Softmax layer [38].
2. Multi-layer Perceptron (MLP): 3 layers of fully connected perceptrons [37].
3. Support Vector Machine (SVM) [39]: classic model that is implemented in
popular ML libraries [40, 41].
4. Random Forest [34]: classic model that is implemented in popular ML libraries [40, 41].

For more practical usage in the real world (i.e., the open world scenario), we find
that Random Forest can still achieve relatively high accuracy rates even with the existence of unseen accelerator traces. We will demonstrate this in our later evaluation.

**13.3.4** **IMPLEMENTATION OF PoC**

The PoC system is built on Devcloud [20], using Intel FPGA SDK for OpenCL [18].
DevCloud is a cloud platform managed by Intel [20] to support research and education about FPGAs, GPUs, AI acceleration, etc. We selected DevCloud for its access
to high-end commercial FPGA devices, such as the Arria 10 and Stratix 10 FPGAs.
This platform allows us to leverage multiple off-the-shelf toolchains, including HighLevel Synthesis (HLS) [42], OpenCL [43], and OneAPI [44]. We choose OpenCL
because: (1) compared to traditional Verilog RTL design flow, C/C++-based development is faster and sufficient since we do not need to optimize for performance; (2)
according to Intel’s documentation [43], as long as different kernels are executed in
different OpenCL command queues, they can be executed concurrently which conveniently creates an application co-locating environment that satisfies our need. Besides, we chose to perform our experiments on DevCloud because commercial cloud
providers have yet to deploy multi-tenancy FPGAs, despite the possibility of their
availability in the future. Nonetheless, our research demonstrates the serious danger
posed by the PCIe side channel when multi-tenancy FPGAs become accessible to
users.

In our PoC implementation, victim kernels and accelerator kernels will be defined
as two unrelated OpenCL kernels running concurrently on the same FPGA. Victim
kernels are configured to run continuously to model victim accelerators that process
data streams. They operate on host memory spaces different from those allocated for
our benchmark accelerator.

Since the execution environment for offline data collection and online attack is the
same, in our PoC implementation the collected data set will be divided into a training

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **311**

set and test set, where the training set will be used to train the classifier models and
the classification results on the test set can emulate the classification accuracy of an
online attack.

**13.4** **EVALUATION**

**13.4.1** **EXPERIMENT SETTINGS**

**13.4.1.1** **Hardware Environment**

All our FPGA-related experiments are conducted on Intel DevCloud [20]. DevCloud
allows free Secure Shell (SSH) access to their servers and FPGA resources from
academic users. In our experiments, we select to use nodes with Xeon CPUs and Intel
Arria 10 series FPGAs. The environment version is development stack release 1.2.1.
To compile our OpenCL kernels, we utilize the tool-chain provided by Intel, which
is available on these nodes. Results are all obtained from node named s005-n007.

**13.4.1.2** **I/O Measurement Collection**

The experiment process is controlled by our host program. After the initial setup of
OpenCL environments (getting platform information, setting up context, command
queues, etc.), we launch a victim kernel which will run continuously during the experiment. Meanwhile we also launch the proposed benchmark to perform multiple
measurements on the PCIe communication link and gather data. In each measurement, we initialize a new memory buffer item in host memory and execute benchmark kernel for BUFFER NUM times, aggregate acquired data and calculate the average bandwidth as the result of this measurement. For each accelerator, we collect
50 traces, with BUFFER NUM points in each trace (default value 100). Since victim
FPGA circuits and our benchmark circuits (both are synthesized from OpenCL kernel implementation) run concurrently and there is no synchronization step between
the two kernels, our experimental setting resembles a multi-tenant FPGA cloud setting.

**13.4.1.3** **Victim Accelerators**

In our experiments, we select eight different FPGA-accelerated workloads provided
by Xilinx Vitis Accelerator Example repository [46] and FPGA-synthesized GPU
workloads from Rodinia benchmark [45]. We make necessary modifications to deploy them on DevCloud. Detailed description and abbreviation codes are listed in
Table 13.1. These accelerators cover different critical areas for FPGA accelerators,
including image processing, signal processing, numerical simulation, and neural network acceleration, thus can serve as representative workloads.

**13.4.1.4** **Classifier Settings**

The collected data will be further analyzed by our learning models. In our experiment, we build several different models based on Python ML libraries like Pytorch [47] and Scikit-learn [41]. The configurations of these models are listed as
follows:

**312** Advances in Hardware Design for Security and Trust

**Table 13.1**
**Descriptions of Our Victim Accelerators**

Name Code Function
adder A Adder implemented using FPGA. It reads inputs
from input buffer, computes results and writes
back to an output buffer.
apply watermark AW Image processing circuit. It reads an image from
input buffer, adds a watermark, and writes back
to an output buffer.
fir F Signal processing circuit. It reads input and coefficient data
from input buffer and performs finite impulse response (FIR) filtering, then writes output back to
output buffer.
matmul M Matrix multiplication circuit. It reads two matrices A and B from input buffer,
calculates AB and writes back to output buffer.
convolute C Convolution accelerator. It reads an image and
filter weights from input buffer,
performs convolution, and writes the results
back to output buffer.
vector addition V This accelerator reads two arrays from input
buffer, performs parallel vector addition
on the two buffers, and writes the results back to
output buffer.
noisegen NG An accelerator that generates random traffic between host and FPGA.
hotspot HS An accelerator employed from Rodinia benchmark [45]
that performs thermal simulation by iteratively
solving differential equations.

1. Random-forest: RandomForestClassifier() from Scikit-learn library [41] is used.
2. SVM: SVC() classifier from Scikit-learn library [41] is used.
3. MLP: built in Pytorch [47], using learning rate 0.001, cross-entropy loss
and stochastic gradient descent (SGD) optimizer, being trained for 1500
epochs.
4. 1D-Convolution: built in Pytorch [47], using learning rate 0.001, crossentropy loss and Adam optimizer [48], being trained for 1500 epochs.

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **313**

**13.4.1.5** **Attacking Scenarios**

In this chapter, we consider two attacking scenarios (i.e., closed-world and openworld scenario). For closed-world testing, we assume all accelerators are known to
the attacker, and we consider the fingerprinting problem as an n-way classification
problem, with n being the number of accelerators in this closed world. For the more
realistic open-world scenario, we consider it as a binary classification problem (since
most attackers will have only one specific target for side channel attacks) and each
classifier will be trained to recognize a single accelerator.

Under both attacking scenarios, we split all collected traces into 7:3 for training
and testing respectively to obtain accuracy data. Additionally, for open-world scenario, we manually remove traces from certain classes in the training set, making
these accelerators agnostic to the classifier. The test set will still include traces from
these classes to simulate the real-world scenario, where traces from unknown accelerators are collected.

In our experiments, we aim to answer two research questions (RQs):

1. RQ1: Does our measurement circuit capture the communication patterns,
and what is the accuracy of fingerprinting?
2. RQ2: How do the parameter settings of benchmark impact the attacking
results?

**13.4.2** **RESULTS**

**13.4.2.1** **RQ** 1

To answer RQ 1, we first present the visualization of measured PCIe side channel
traces and fingerprinting accuracy in Figure 13.5 and Table 13.2, respectively. All
data are obtained from the eight FPGA-accelerated workloads mentioned above.

**Figure** **13.5** Plain data visualization and t-SNE visualization of performance traces
collected by our benchmark.

**314** Advances in Hardware Design for Security and Trust

**Table 13.2**
**Accuracy Results**

Model Test Acc.
Random Forest 88%
SVM 69%
MLP 55%
1D-Convolution 26%

We first present the collected traces with using t-Distributed stochastic neighbor embedding (t-SNE) [49], which is a widely used data visualization method. It
projects high-dimensional data to a 2-D plane and can show how the data points can
be clustered. In Figure 13.5, we collect and visualize the bandwidth traces of our
benchmark accelerator when it is running concurrently with one of the eight victim circuits. In Figure 13.5 (a), bandwidth data are normalized with minimum and
maximum bandwidth values in the data set and range between 0 and 1. We can see
that traces belonging to different accelerators are separable, which indicates that our
benchmark circuit is able to capture the unique communication patterns existing in
the execution of the victim accelerators and generate fingerprints for each of them.
The bandwidth difference exposes a vulnerability of inferring the co-located victim
circuit. T-SNE results in Figure 13.5 (b) also prove that the data traces are separable.

Based on findings in Figure 13.5, which indicates that these traces contain information that can help differentiate different accelerators, we further consider two
fingerprinting attacking scenarios (i.e., closed-world and open-world scenarios).
Closed-world fingerprinting aims to classify the types of accelerators within a known
accelerator set, while open-world fingerprinting only interests in one sensitive accelerator and classify others as “unrelated.”

Closed-world. Table 13.2 shows the closed-world classification accuracy performance of our selected models. Among our models, Random Forest achieves the highest classification accuracy, reaching 88% accuracy in this task. The 10-fold crossvalidation results of our Random Forest model is provided in Figure 13.6. From the
distribution of model metrics like accuracy, precision, recall, and F1-score, we can
see that the model, we can see that the model performance is relatively stable. There
are similar but different FPGA workload fingerprinting works [27,50], where the authors utilize power side channel to perform classification of different cryptographic
cores. Compared to their works, we focus on fingerprinting general computing circuits and utilize a different side channel. Also, our implementation stays at HLS
level.

We select the two models with the best accuracy performance (i.e., SVM and
Random Forest), and provide further details to show how well our model performs
in this specific task. Confusion matrices are provided in Figure 13.7. It shows how
accurate the selected models are able to classify each of the victim accelerators. Values in each cell of the confusion matrix represent the number of samples of each

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **315**

**Figure 13.6** Cross-validation results of Random Forest model.

**Figure 13.7** Confusion matrices of the two classifiers.

(Predicted Label, True Label) pair. We can see from the figure that both models have
acceptable accuracy performance (69.2% and 88.3%) and are able to differentiate the
eight accelerator classes, although Random Forest works better with fewer misclassified samples and outperforms with a great margin. This could be due to the intrinsic
features of the data traces, which are potentially more suitable for the algorithm of
Random Forest and decision trees [38].

Open-world. Then we also consider open-world fingerprinting scenario, where
the attacker only has one specific target to recognize, and there are traces belonging
to unseen accelerators during the training process. During the experiments, we randomly select labels to remove and repeat the experiments multiple times to obtain

**316** Advances in Hardware Design for Security and Trust

**Figure 13.8** Open-world accuracy results.

the average accuracy performance data regarding classifiers corresponding to each
class of victim accelerators. The accuracy results are shown in Figure 13.8. We increment the number of unseen accelerators during the training process and collect
accuracy results for classifiers targeting different accelerators. We can see that the
accuracy drops as the number of unknown accelerators increases. However, as long
as the attacker has partial knowledge about accelerators in the system, when half of
the traces are from unseen accelerators the fingerprinting accuracy can still maintain
at around 80% or higher. From Figure 13.8, we can also see that (1) some accelerators are more vulnerable than others (e.g., our model on fir consistently achieves
high fingerprinting success rate), highlighting the importance of providing protection
when victim is fir; (2) when there are less types of accelerators, the fingerprinting
success rate is higher and it is more important to provide defense.

In the experiments above, we only use standard min-max scaling pre-processing
and standard models. With further customization (filtering data, modifying predictive
models), the accuracy can be potentially higher, resulting in a higher success rate and
lower costs for continuing side channel attacks.

Summary. Our benchmark accelerator is able to capture communication patterns
of co-located accelerators on FPGA and use these generated fingerprints to classify
at a higher accuracy. This accuracy performance is sufficient for use in a real-world

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **317**

scenario. From the classifier side, we find that Random Forest model achieves the
highest classification accuracy and can reach 88% classification accuracy. Surprisingly, the most complicated model, 1D-Convolution,achieves the worst classification
accuracy performance. In our experiments, simpler models like Random Forest and
SVM achieve significantly better accuracy performance. This could be potentially
attributed to the limited number of traces in our data set.

**13.4.2.2** **RQ** 2

As mentioned in Section 13.3, our benchmark has four different design parameters:

1. ACCESS NUM, which corresponds to how much traffic is generated by the
benchmark accelerator.
2. REPEAT NUM, which is the number of times the kernel is executed and it
relates to our measuring granularity and data stability.
3. BUFFER SIZE, which determines how large each buffer is.
4. BUFFER NUM, which relates to how many data points are collected within
one performance trace.

The following parameter settings:

1. ACCESS NUM= 1000,
2. REPEAT NUM= 10,
3. BUFFER SIZE= 4 Bytes,
4. BUFFER NUM= 100.

will be later referred to as our default setting.

In this experiment, we screen all parameters and provide t-SNE visualization and
compare their classification accuracy with the one under the default setting. To make
visualization results clearer, we drop the simplest accelerator (noisegen) and the
most complex accelerator (hotspot) and only perform attacks on the remaining six
accelerators. To explore the effects of each of the four parameters, we fix the other
three parameters to the default settings and vary the value of the target parameter,
and then collect data on the six victim accelerators. The t-SNE visualization of the
collected data traces as well as classification accuracy traces of our four models regarding the four parameters shown in Figures 13.9–13.12. Corresponding accuracy
performance of the four models are provided in Figure 13.13. Figures corresponding
to configurations that are identical with default settings are omitted to avoid repetition, and the results are the same as in Figure 13.5(b). In these figures, we obtain
t-SNE results from normalized communication bandwidth data. Overall, the use of
different parameter values results in varying trace patterns and can hence affect the
accuracy of different models. The analysis of the results we obtain in this experiment
is shown as follows.

**ACCESS** **NUM** . In Figure 13.9, the influence of the parameter ACCESS NUM is
shown. From Figure 13.9(a–d), we can observe a change in the visualization results (i.e., the traces collected from different victim accelerators show different separability). This indicates that the ability of our accelerator benchmark to capture

**318** Advances in Hardware Design for Security and Trust

**Figure 13.9** T-SNE visualization results of traces under different ACCESS NUM settings.

the differentiable patterns in I/O operations existing in our victim accelerators can
vary according to ACCESS NUM. We can see that after ACCESS NUM ≥ 2000, data
points from several accelerator classes tend to be mixed together. By looking at Figure 13.13(a), we can see that the Random Forest model achieves the highest accuracy
result, reaching an accuracy over 90% at ACCESS NUM= 1000. SVM achieves over
85% accuracy and MLP achieves over 70% classification accuracy, both at the same
point. However, the 1D-Convolution model is only able to achieve 60% accuracy
at its highest. We can also see that as ACCESS NUM increases, except for the 1DConvolution model, the accuracy generally increases first (though the accuracy of
our Random Forest model stays over 90% with relative stability). After reaching the
highest accuracy at ACCESS NUM= 1000, the accuracy starts to drop.

We speculate that the reason behind the fingerprinting accuracy difference is due
to the measurement granularity differences when ACCESS NUM ranges from 250 to
4000. Initially, the growth of ACCESS NUM introduces more data to be read and

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **319**

**Figure** **13.10** T-SNE visualization results of traces under different REPEAT NUM
settings.

written; hence, the effects of noise can be better canceled and communication patterns can be better captured until ACCESS NUM reaches 1000. However, since the
execution time of our benchmark accelerator also increases as ACCESS NUM grows,
the measurement will become more coarse-grained since the change in I/O performance variance of victim accelerators within this execution time period will be amortized. After a certain point (in our experiment, between 1000 and 2000), the extended
execution time of a benchmark accelerator causes the benchmark circuit to lose the
ability to accurately capture victim communication patterns, thereby inducing a drop
in classification accuracy.

**REPEAT** **NUM.** For parameter REPEAT NUM, the t-SNE visualization results
are shown in Figure 13.10. As in Figure 13.9, data points belonging to different
accelerator classes in Figure 13.10(a–d) are separable, where the clearest clustering results appear at REPEAT NUM= 5 and REPEAT NUM= 10 (see Figure 13.5).
The classification results for the ML models in Figure 13.13(b) also match this

**320** Advances in Hardware Design for Security and Trust

observation, with the highest classification results achieved at REPEAT NUM= 5 and
REPEAT NUM= 10, where the accuracy of random forest is again over 90% and
the highest accuracy results of SVM and MLP are around 85% and 70%, respectively. In Figure 13.13(b), we can observe a similar trend as in Figure 13.13(a), where
the accuracy first increases to an optimal point and starts to drop as REPEAT NUM
grows.

The explanation for the accuracy trend is similar. As REPEAT NUM determines
how many times our benchmark is executed when operating on a memory buffer, increasing REPEAT NUM will: (1) cancel the effects of noise and obtain a more precise
measurement of the performance; (2) extend the time it takes to operate on a single
buffer (i.e., the time it takes to generate a data point in the performance trace). As the
execution time of the accelerator kernel task is relatively short, when REPEAT NUM
is low, the measurement will be finished within a short period of time and the dynamic communication patterns cannot be captured by our benchmark accelerator.
This, combining the influence of noise, is the reason why all models achieve poor
classification accuracy results at REPEAT NUM= 1. When REPEAT NUM increases,
the communication patterns start to be captured. However, if REPEAT NUM is too
large, same as the situation in ACCESS NUM, the whole measurement process becomes too coarse-grained. Changes in the I/O communication traffic may be amortized; thus, classification models cannot extract detailed information from the collected traces.

**BUFFER** **SIZE** . The experimental results of trace visualization and classification results under different BUFFER SIZE settings are shown in Figure 13.11. We
can see that all the BUFFER SIZE settings we use are able to preserve the layering information in the victim accelerators. From Figure 13.13(c), we also observe
that the influence of parameter BUFFER SIZE is not as much as ACCESS NUM and
REPEAT NUM. However, there is an optimal point for the Random Forest and SVM
to work on (BUFFER SIZE= 4 Bytes). We will keep using this empirical value since
it is the best work point for our most accurate model. However, as BUFFER SIZE
increases beyond the optimal point, there is a slight drop in classification accuracy.
This can be due to certain details of the implementation of low-level runtime drivers.

**BUFFER** **NUM** . Results of varying the parameter BUFFER NUM are shown in Figure 13.12. By increasing BUFFER NUM, a longer period of execution of the victim
accelerators will be probed and the trace can include more information. However,
surprisingly, from Figure 13.13(d), the classification accuracy does not change much.
With BUFFER NUM= 50, our Random Forest classifier is able to reach over 90%.
Other models have a similar trend of accuracy.

Summary. In our experimental results, we show that for a relatively wide range of
parameter choices, the Random Forest model is able to achieve satisfying classification accuracy. This helps loosen the constraints on attackers’ benchmark accelerator
implementation. Under ACCESS NUM= 1000, REPEAT NUM= 5, BUFFER NUM=
100, and BUFFER SIZE= 4 Bytes, our model is able to achieve the highest accuracy. However, in the real world, under some other hardware or software settings
(different FPGA models, communication link hardware, or a different heterogeneous

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **321**

**Figure** **13.11** T-SNE visualization results of traces under different BUFFER SIZE
settings.

computing software stack), these values may vary. To maximize attack performance,
attackers are recommended to conduct some offline screening prior to launching the
attack to obtain near-optimal parameters. This parameter search does not need to
be accurate, since our most powerful model can achieve over 92% accuracy performance under a relatively wide range of attack accelerator parameter choices in the
selected accelerator set, which is sufficient for fingerprinting tasks. From the benchmark accelerator side, we conclude that:

1. Our benchmark accelerator is able to capture the I/O patterns of each of the
victim accelerators.
2. Both ACCESS NUM and REPEAT NUM affect the granularity of measurement and can significantly influence the performance of classification models. There are optimal values for these two values, as shown in Figure 13.13(a) and Figure 13.13(b).

**322** Advances in Hardware Design for Security and Trust

**Figure** **13.12** T-SNE visualization results of traces under different BUFFER NUM
settings.

3. Buffer-related parameters BUFFER SIZE and BUFFER NUM have less influence on classification accuracy. However, the optimal parameter values
still exist.

**13.5** **DISCUSSION**

**13.5.1** **MITIGATION**

The intrinsic cause of the security vulnerability revealed in this chapter is the different communication or I/O patterns of accelerators. The different access patterns of
accelerators can serve as unique fingerprints of these accelerators. What our benchmark accelerator and host program do is to stress the communication link (i.e., PCIe)
and obtain performance measurement trace results that contain information about

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **323**

**Figure 13.13** Accuracy results when varying different parameters.

these fingerprints. This information is further extracted by ML models and helps
achieve high classification accuracy.

The mitigation to our proposed fingerprint attack can be done by enhancing the FPGA-host interface (e.g., FPGA interface manager [FIM] in Intel cloud
FPGAs [20]). Instead of transmitting raw data, messages traveling through the communication link should pass another security layer for obfuscation. In this obfuscation layer, the communication pattern will be distorted, where random latency/burst
will be inserted to make communication patterns unrecognizable. Policies targeting
introducing such distortions with minimum performance overhead will be our future
work.

From the host side, we can also modify the underlying platforms (OPAE [51],
OpenCL [43], etc.). By changing how the driver handles data movement between the
host server and FPGA, communication pattern obfuscation can also be achieved.

**13.5.2** **ATTACK AND DEFENCE SUGGESTIONS**

**13.5.2.1** **For Attackers**

In our proposed attack, one prerequisite for attackers is to obtain servers and FPGAs
that are identical to the servers and FPGAs used in FPGA clouds. In reality, instead

**324** Advances in Hardware Design for Security and Trust

of purchasing hardware and building up the system locally, it’s better for attackers
to use the cloud itself for data collection. By running data collection steps in the
cloud multiple times and recording the underlying hardware and software platform,
the attackers can eventually have a set of models that are able to cover heterogeneous
hardware and software platforms in the cloud. Doing this step on the victim cloud is
more realistic and economical, considering the high cost to set up required hardware
and software environments locally.

**13.5.2.2** **For Regular FPGA Cloud Users**

The fingerprinting attack we propose relies on the intrinsic features of victim accelerators, and we make an assumption that attackers are aware of the target accelerator and can limit the range of accelerators running on the cloud. Therefore, to
defend against the proposed fingerprinting attack, FPGA cloud users should be careful about using existing public intellectual property cores (IPs) since these IPs are
possibly already in the attackers’ database. To achieve this, these users can modify
their accelerators and insert noisy I/O or computation operations (additional writes
to an unimportant memory location, inserting additional computation between two
I/O operations, etc.) to distort the performance traces the attacker may obtain.

In the meantime, it is worth noting that exploiting this security vulnerability also
relies on physically residing on the same FPGA where the victim accelerator is running. The simplest way for users to avoid being attacked is to obtain ownership of
the whole FPGA board as well as the hosting server. This may result in higher costs
in deploying FPGA accelerators (since it requires users to pay more to cloud service
providers), but it completely eliminates the threat of side channel-related attacks induced by sharing FPGA resources with unknown users.

**13.5.2.3** **For Cloud Service Providers**

We suggest cloud service providers enhance their infrastructure interface as mentioned in Section 13.5.1. Though this may add additional performance overhead, it
can efficiently prevent the proposed attack.

Also, FPGA cloud service providers can consider improving their scheduling policy to scatter users’ FPGA accelerators on the cloud. It can dramatically reduce the
chance of victims’ malicious accelerators co-locating with victims’ accelerators and
hence mitigating side channel attacks or fingerprinting attacks that require attackers
and victims to be placed together.

**13.5.3** **FUTURE WORK**

Future work will be dedicated to developing mitigation technologies against this
side channel. We will come up with both hardware and software-based mitigation
strategies. For hardware defense, we will consider deploying low-overhead noise injection circuits. For software defense, we will modify the underlying heterogeneous

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **325**

computing frameworks like OpenCL [33] or OPAE [51] to obfuscate the communication patterns of computation accelerators on board. Besides, cloud scheduler-level
defense can be employed to securely schedule/migrate instances.

**13.6** **RELATED WORK**

FPGA side channel attacks. Several kinds of remote attacks targeting cloud FPGAs
have been proposed recently. One major type is a long-wire attack, where attackers
utilize leakage in long wires to probe information transmitted inside the circuit. [23]
uses the delay difference of nearby wires to probe the signal being transmitted on the
long wire, since logical 1 and logical 0 on long wires can lead to different delays of
nearby wires. The authors use ROs to capture this difference and use collected information to recover the bits being transmitted on the target long wire. [24] performs
a similar attack and recovers the secret key of an AES crypt circuit. [52] provides
detailed tests of several RO designs and validate the efficiency of these variants of
long-wire attacks. Defense mechanisms are proposed as well to mitigate long-wire
attacks. Remote power side channel attack is another type of FPGA side channel attack. In [25], it is performed by programming an on-chip RO-based power monitor
to reveal the secret key of a RSA crypto module. This paper also shows that by using
the RO-based power monitor, it is possible to perform an FPGA-to-CPU attack on
the same SoC. Power side channel attacks have also been proven to be feasible in a
production environment [53], where researchers retrieved AES key information from
an AWS EC2 F1 FPGA instance.

Our attack is based on PCIe communication side channels. There has been an
attack in a FPGA cloud using PCIe contention. In [29], the authors utilize the generation of PCIe contention to perform infrastructure cartography. They use PCIe stressors to generate PCIe contention and reveal information regarding cloud servers in
AWS Cloud. However, their attack targets multiple FPGAs and aims at revealing infrastructure information instead of revealing information about applications on the
same FPGA. In [54, 55], the authors build a covert communication channel based
on PCIe contention and consider information leakage in the PCIe contention side
channel. Similar to our work, PCIe traffic is monitored, and information like execution timing traces of victim applications can be obtained. The difference is that
we consider multi-tenancy FPGAs (accelerators from multiple users residing on the
same FPGA hardware), whereas they consider the scenario where accelerators from
different users are distributed to multiple FPGA boards connected to the same server.

The most similar works we find in literature are [27,50]. To the best of our knowledge, they are also the only works about multi-tenancy FPGA accelerator fingerprinting. In these papers, to achieve a similar goal, the authors propose using a power
side channel for fingerprinting co-located FPGA circuits. Their measurement targets
lower-level side channel leakage and they focus on classifying cryptographic cores,
whereas our method is more coarse-grained and we focus on identifying general accelerator workloads.

Our proposed method is more closely related and will be beneficial to side channel attacks in a FPGA cloud, which relies on co-locating with target victims and

**326** Advances in Hardware Design for Security and Trust

information about co-located victim circuits. These attacks include attacks targeting cross-talk information leakage [56], power analysis attacks [11, 12] that collect
power side channel information using co-located malicious circuits and reveal secret information from collected data, fault attacks [13] that actively induce faults like
voltage drops to victim circuits, etc.

**13.7** **CONCLUSION**

In this chapter, we propose a novel attack targeting multi-tenancy FPGA clouds,
where attackers can obtain knowledge about co-located accelerators. By implementing a PoC attack accelerator as well as its corresponding host program, we test accelerators from several application scenarios like signal processing, numerical simulation acceleration, etc. Our results show that communication links like PCIe can
serve as a new source of side channel and can be exploited by fingerprinting attacks
targeting co-located FPGA accelerators. Our proposed attack method will be beneficial for cloud FPGA side channel attacks, since successfully recognizing target
co-located victims is a prerequisite and can significantly reduce the costs of attacks.
As far as we know, this is the first work targeting fingerprinting co-located FPGA
accelerators using communication side channels. Future work will be dedicated to
security-enhanced FPGA interface development and another version of this research
under an open-world setting.

**REFERENCES**

1. Sagar Karandikar, Howard Mao, Donggyu Kim, David Biancolin, Alon Amid, Dayeol
Lee, Nathan Pemberton, Emmanuel Amaro, Colin Schmidt, Aditya Chopra, et al.
FireSim: FPGA-accelerated cycle-exact scale-out system simulation in the public cloud.
In 2018 ACM/IEEE 45th Annual International Symposium on Computer Architecture
(ISCA), pages 29–42. IEEE, 2018.
2. Tiago Carneiro, Raul Victor Medeiros Da N´obrega, Thiago Nepomuceno, Gui-Bin Bian,
Victor Hugo C De Albuquerque, and Pedro Pedrosa Reboucas Filho. Performance analysis of google colaboratory as a tool for accelerating deep learning applications. IEEE
Access, 6:61677–61685, 2018.
3. Nikko Strom. Scalable distributed dnn training using commodity GPU cloud computing. In Sixteenth Annual Conference of the International Speech Communication Association, 2015.
4. Oliver Knodel, Paul R Genssler, Fredo Erxleben, and Rainer G Spallek. FPGAs and the
cloud–an endless tale of virtualization, elasticity and efficiency. International Journal
on Advances in Systems and Measurements, 11(3-4):230–249, 2018.
5. Yu-Hsin Chen, Tushar Krishna, Joel S Emer, and Vivienne Sze. Eyeriss: An energyefficient reconfigurable accelerator for deep convolutional neural networks. IEEE Journal of Solid-State Circuits, 52(1):127–138, 2016.
6. Amazon. Amazon EC2 instance types, 2022. [https://aws.amazon.com/ec2/instance-](https://aws.amazon.com/ec2/instancetypes)
[types/ [Online; accessed 10 March 2022].](https://aws.amazon.com/ec2/instancetypes)
7. Microsoft Research. Microsoft unveils project brainwave for real-time AI, 2017.
[https://www.microsoft.com/en-us/research/blog/microsoft-unveils-project-brainwave/](https://www.microsoft.com/en-us/research/blog/microsoft-unveils-project-brainwave)

[Online; accessed 17 July 2022].

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **327**

8. Pawel Swierczynski, Georg T Becker, Amir Moradi, and Christof Paar. Bitstream fault
injections (BiFI)–automated fault attacks against sram-based FPGAs. IEEE Transactions on Computers, 67(3):348–360, 2017.
9. Christian Krieg, Clifford Wolf, and Axel Jantsch. Malicious LUT: A stealthy FPGA
Trojan injected and triggered by the design flow. In 2016 IEEE/ACM International
Conference on Computer-Aided Design (ICCAD), pages 1–8. IEEE, 2016.
10. Zane Weissman, Thore Tiemann, Daniel Moghimi, Evan Custodio, Thomas Eisenbarth,
and Berk Sunar. Jackhammer: Efficient rowhammer on heterogeneous FPGA-CPU platforms. arXiv preprint arXiv:1912.11523, 2019.
11. Shayan Moini, Shanquan Tian, Daniel Holcomb, Jakub Szefer, and Russell Tessier. Remote power side-channel attacks on BNN accelerators in FPGAs. In 2021 Design, Automation & Test in Europe Conference & Exhibition (DATE), pages 1639–1644. IEEE,
2021.
12. George Provelengios, Daniel Holcomb, and Russell Tessier. Characterizing power distribution attacks in multi-user FPGA environments. In 2019 29th International Conference
on Field Programmable Logic and Applications (FPL), pages 194–201. IEEE, 2019.
13. Md Mahbub Alam, Shahin Tajik, Fatemeh Ganji, Mark Tehranipoor, and Domenic Forte.
RAM-Jam: Remote temperature and voltage fault attack on FPGAs using memory collisions. In 2019 Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC),
pages 48–55. IEEE, 2019.
14. Jonas Krautter, Dennis RE Gnad, and Mehdi B Tahoori. Remote fault attacks in multitenant cloud FPGAs. IEEE Design & Test, 2022.
15. Chongzhou Fang, Ning Miao, Han Wang, Jiacheng Zhou, Tyler Sheaves, John M Emmert, Avesta Sasan, and Houman Homayoun. Gotcha! I know what you are doing on the
FPGA cloud: Fingerprinting co-located cloud FPGA accelerators via measuring communication links. In Proceedings of the 2023 ACM SIGSAC Conference on Computer
and Communications Security, pages 2024–2037, 2023.
16. Yann LeCun. The mnist database of handwritten digits. [http://yann.lecun.com/exdb/](http://yann.lecun.com/exdb/mnist)
[mnist/, 1998.](http://yann.lecun.com/exdb/mnist)
17. Rolf Neugebauer, Gianni Antichi, Jos´e Fernando Zazo, Yury Audzevich, Sergio L´opezBuedo, and Andrew W Moore. Understanding PCIe performance for end host networking. In Proceedings of the 2018 Conference of the ACM Special Interest Group on Data
Communication, pages 327–341, 2018.
18. Intel. Intel FPGA SDK for OpenCL pro edition: Programming guide, 2022.
[https://www.intel.com/content/www/us/en/docs/programmable/683846/22-4/eol.html](https://www.intel.com/content/www/us/en/docs/programmable/683846/22-4/eol.html)

[Online; accessed 10 March 2022].
19. Ghada Dessouky, Ahmad-Reza Sadeghi, and Shaza Zeitouni. SoK: Secure FPGA multitenancy in the cloud: Challenges and opportunities. In 2021 IEEE European Symposium
on Security and Privacy (EuroS&P), pages 487–506. IEEE, 2021.
20. Intel Devcloud, 2021. [https://www.intel.com/content/www/us/en/developer/tools/](https://www.intel.com/content/www/us/en/developer/tools/devcloud/overview.html)
[devcloud/overview.html [Online; accessed 10 March 2022].](https://www.intel.com/content/www/us/en/developer/tools/devcloud/overview.html)
21. Amazon Web Service. Developer preview - EC2 instances (F1) with programmable
hardware, 2016. [https://aws.amazon.com/blogs/aws/developer-preview-ec2-instances-](https://aws.amazon.com/blogs/aws/developer-preview-ec2-instances-f1-with-programmable-hardware)
[f1-with-programmable-hardware/ [Online; accessed 17 July 2022].](https://aws.amazon.com/blogs/aws/developer-preview-ec2-instances-f1-with-programmable-hardware)
22. Alibaba Cloud. Elastic compute service: Instance family, 2022. [https://www.](https://www.alibabacloud.com/help/en/ecs/user-guide/instance-families)
[alibabacloud.com/help/en/ecs/user-guide/instance-families/](https://www.alibabacloud.com/help/en/ecs/user-guide/instance-families) [Online; accessed 17 July
2022].

**328** Advances in Hardware Design for Security and Trust

23. Ilias Giechaskiel, Kasper B. Rasmussen, and Ken Eguro. Leaky wires: Information
leakage and covert communication between FPGA long wires. In Proceedings of the
2018 on Asia Conference on Computer and Communications Security, ASIACCS ’18,
page 15–27. Association for Computing Machinery, 2018.
24. Chethan Ramesh, Shivukumar B. Patil, Siva Nishok Dhanuskodi, George Provelengios,
Sebastien Pillement, Daniel Holcomb, and Russell Tessier. FPGA side channel attacks
without physical access. In 2018 IEEE 26th Annual International Symposium on FieldProgrammable Custom Computing Machines (FCCM), pages 45–52, 2018.
25. Mark Zhao and G. Edward Suh. FPGA-based remote power side-channel attacks. In
2018 IEEE Symposium on Security and Privacy (SP), pages 229–244, 2018.
26. Joseph Gravellier, Jean-Max Dutertre, Yannick Teglia, and Philippe Loubet-Moundi.
High-speed ring oscillator based sensors for remote side-channel attacks on FPGAs. In
2019 International Conference on ReConFigurable Computing and FPGAs (ReConFig),
pages 1–8, 2019.
27. Mustafa Gobulukoglu, Colin Drewes, William Hunter, Ryan Kastner, and Dustin Richmond. Classifying computations on multi-tenant FPGAs. In 2021 58th ACM/IEEE
Design Automation Conference (DAC), pages 1261–1266. IEEE, 2021.
28. Mingtian Tan, Junpeng Wan, Zhe Zhou, and Zhou Li. Invisible probe: Timing attacks
with PCIe congestion side-channel. In 2021 IEEE Symposium on Security and Privacy
(SP), pages 322–338. IEEE, 2021.
29. Shanquan Tian, Ilias Giechaskiel, Wenjie Xiong, and Jakub Szefer. Cloud FPGA cartography using PCIe contention. In 2021 IEEE 29th Annual International Symposium
on Field-Programmable Custom Computing Machines (FCCM), pages 224–232. IEEE,
2021.
30. Najmeh Nazari, Hosein Mohammadi Makrani, Chongzhou Fang, Behnam Omidi,
Setareh Rafatirad, Hossein Sayadi, Khaled N Khasawneh, and Houman Homayoun. Adversarial attacks against machine learning-based resource provisioning systems. IEEE
Micro, 2023.
31. Chongzhou Fang, Han Wang, Najmeh Nazari, Behnam Omidi, Avesta Sasan, Khaled N
Khasawneh, Setareh Rafatirad, and Houman Homayoun. Repttack: Exploiting cloud
schedulers to guide co-location attacks. In Proceedings of the Network and Distributed
Systems Security (NDSS) Symposium, 2022.
32. Chongzhou Fang, Najmeh Nazari, Behnam Omidi, Han Wang, Aditya Puri, Manish
Arora, Setareh Rafatirad, Houman Homayoun, and Khaled N Khasawneh. Heteroscore:
Evaluating and mitigating cloud security threats brought by heterogeneity. 2023.
33. Aaftab Munshi. The OpenCL specification. In 2009 IEEE Hot Chips 21 Symposium
(HCS), pages 1–314. IEEE, 2009.
34. Tin Kam Ho. Random decision forests. In Proceedings of 3rd international conference
on document analysis and recognition, volume 1, pages 278–282. IEEE, 1995.
35. Kartik Patwari, Syed Mahbub Hafiz, Han Wang, Houman Homayoun, Zubair Shafiq,
and Chen-Nee Chuah. Dnn model architecture fingerprinting attack on CPU-GPU edge
devices. In 2022 IEEE 7th European Symposium on Security and Privacy (EuroS&P),
pages 337–355. IEEE, 2022.
36. Serkan Kiranyaz, Onur Avci, Osama Abdeljaber, Turker Ince, Moncef Gabbouj, and
Daniel J Inman. 1D convolutional neural networks and applications: A survey. Mechanical Systems and Signal Processing, 151:107398, 2021.
37. Stephen I Gallant et al. Perceptron-based learning algorithms. IEEE Transactions on
neural networks, 1(2):179–191, 1990.
38. Ian Goodfellow, Yoshua Bengio, and Aaron Courville. Deep learning. MIT press, 2016.

Cloud FPGA Accelerator Fingerprinting Using Communication Side Channels **329**

39. Corinna Cortes and Vladimir Vapnik. Support-vector networks. Machine Learning,
20(3):273–297, 1995.
40. Mart´ın Abadi. Tensorflow: Learning functions at scale. In Proceedings of the 21st ACM
SIGPLAN International Conference on Functional Programming, pages 1–1, 2016.
41. Fabian Pedregosa, Ga¨el Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand
Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent
Dubourg, et al. Scikit-learn: Machine learning in python. The Journal of Machine
Learning Research, 12:2825–2830, 2011.
42. Philippe Coussy and Adam Morawiec. High-level synthesis, volume 1. Springer, 2010.
43. [Intel/FPGA-Devcloud, 2022. https://github.com/intel/FPGA-Devcloud/tree/master [On-](https://github.com/intel/FPGA-Devcloud/tree/master)
line; accessed 10 March 2022].
44. Intel. oneAPI Programming Model, 2022. [https://www.intel.com/content/www/us/en/](https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2024-1/oneapi-programming-model.html)
[docs/oneapi/programming-guide/2024-1/oneapi-programming-model.html](https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2024-1/oneapi-programming-model.html) [Online; accessed 10 March 2022].
45. Shuai Che, Michael Boyer, Jiayuan Meng, David Tarjan, Jeremy W Sheaffer, Sang-Ha
Lee, and Kevin Skadron. Rodinia: A benchmark suite for heterogeneous computing.
In 2009 IEEE international symposium on workload characterization (IISWC), pages
44–54. IEEE, 2009.
46. Xilinx. Vitis Accel Examples’ Repository, 2020. [https://github.com/Xilinx/Vitis](https://github.com/Xilinx/Vitis_Accel_Examples/tree/main)
Accel [Examples/tree/main [Online; accessed 10 March 2022].](https://github.com/Xilinx/Vitis_Accel_Examples/tree/main)
47. Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory
Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch:
An imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems, 32, 2019.
48. Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv
preprint arXiv:1412.6980, 2014.
49. Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-SNE. Journal
of machine learning research, 9(11), 2008.
50. Colin Drewes, Olivia Weng, Keegan Ryan, Bill Hunter, Christopher McCarty, Ryan
Kastner, and Dustin Richmond. Turn on, tune in, listen up: Maximizing side-channel
recovery in time-to-digital converters. In Proceedings of the 2023 ACM/SIGDA International Symposium on Field Programmable Gate Arrays, pages 111–122, 2023.
51. Intel. Open Programmable Acceleration Engine, 2017. [https://opae.github.io/](https://opae.github.io/latest/index.html)
[latest/index.html [Online; accessed 10 March 2022].](https://opae.github.io/latest/index.html)
52. Ilias Giechaskiel, Kasper Bonne Rasmussen, and Jakub Szefer. Measuring long wire
leakage with ring oscillators in cloud FPGAs. In 2019 29th International Conference on
Field Programmable Logic and Applications (FPL), pages 45–50. IEEE, 2019.
53. Ognjen Glamoˇcanin, Louis Coulon, Francesco Regazzoni, and Mirjana Stojilovi´c. Are
cloud FPGAs really vulnerable to power analysis attacks? In 2020 Design, Automation
& Test in Europe Conference & Exhibition (DATE), pages 1007–1010. IEEE, 2020.
54. Ilias Giechaskiel, Shanquan Tian, and Jakub Szefer. Cross-vm information leaks in
FPGA-accelerated cloud environments. In 2021 IEEE International Symposium on
Hardware Oriented Security and Trust (HOST), pages 91–101. IEEE, 2021.
55. Ilias Giechaskiel, Shanquan Tian, and Jakub Szefer. Cross-vm covert-and side-channel
attacks in cloud FPGAs. ACM Transactions on Reconfigurable Technology and Systems,
16(1):1–29, 2022.
56. Ilias Giechaskiel and Jakub Szefer. Information leakage from FPGA routing and logic
elements. In Proceedings of the 39th International Conference on Computer-Aided Design, pages 1–9, 2020.

# 14 Enterprise Risk
### Management of Electronics and Computing Device Supply Chains

Zachary A. Collier and James H. Lambert

**14.1** **INTRODUCTION**

The life cycle of a semiconductor is complex, with sophisticated procedures and
numerous constituent inputs to produce a single chip. For example, it is estimated
to take over 700 steps to produce a semiconductor (Whalen, 2021). In terms of resources, a 2-gram chip requires approximately 1.6 kg of fossil fuels, 72 g of chemicals, and 32 kg of water to produce. Around 630 times the mass of input materials
go into making a chip as compared to the mass of the final output (Graham, 2002).
Managing the associated supply chain is similarly complex, with subsystem experts/operators/owners specializing in different value-adding processes, from design, fabrication, assembly, packaging, testing, and integration into products (Varas et al.,
2021). The market for semiconductors after their production involves several interests and partners, such as networks of distributors and brokers (DiMase et al., 2016).
Managing the complexities inherent in the industry thus necessitates a perspective of
the system of systems across multiple time horizons.

The discipline of systems engineering offers principles and set of tools by which
to manage large and complex product development efforts. According to INCOSE
(2006),

“Systems Engineering is an interdisciplinary approach and means to enable
the realization of successful systems. It focuses on defining customer needs
and required functionality early in the development cycle, documenting requirements, and then proceeding with design synthesis and system validation
while considering the complete problem. Systems Engineering considers both
the business and the technical needs of all customers with the goal of providing
a quality product that meets the user needs.”

[DOI: 10.1201/9781003510949-14](https://doi.org/10.1201/9781003510949-14) **330**

Enterprise Risk Management of Electronics and Computing Device Supply Chains **331**

Developing successful systems or products involves creating technical solutions
that align with the business case and funding constraints throughout the system’s
or product’s life cycle (INCOSE, 2006). Typical system life cycles include conceptualization, development, production, utilization, support, and retirement phases
(INCOSE, 2006). The life cycle can be divided into various processes, such as in
the ISO/IEC/IEEE 15288 standard, which defines, for example, 14 technical processes, starting with business and mission analysis and concluding with disposal
(ISO/IEC/IEEE, 2023). Systems engineering principles provide essential guidance
on the security of cyber-physical systems across their life cycles, including secure
hardware, software, and firmware (DiMase et al., 2020, 2019, 2015).

Within the scope of technical management of systems is risk management. In the
context of systems engineering, most systems involve managing elements of technical risk (whether the functional performance is in alignment with requirements), operational risk (whether the system achieves the desired business value), and programmatic risk (whetheer the project meets cost and scheduling constraints) (Horowitz &
Lambert, 2006).

Risk itself is a term that is associated with a number of complementary definitions and concepts. The Society for Risk Analysis (2018) publishes a glossary with
13 definitions of risk, ranging from qualitative to quantitative. Kaplan and Garrick
(1981) defined a risk as the set of triplets {(si, pi, xi)}, where si is a scenario, pi
is the probability of that scenario occurring, and xi is the consequence or damage
associated with the scenario. Lowrance (1976) differentiated risk (a measure of the
probability and severity of harm) from safety (a judgment about the acceptability of
risk). Kaplan and Garrick (1981), following the triplet formulation of risk, defined
three guiding questions for risk analysis:

 - What can happen?

 - How likely is it that it will happen?

 - If it does happen, what are the consequences?

Once risks have been identified and analyzed, they must be treated. Risk treatments typically fall into four categories: Avoidance, mitigation, transfer, and acceptance (Hillson, 1999). Risk treatment involves making decisions about balancing
costs of risk treatment and the benefits of risk reduction (Kleindorfer & Saad, 2005).
Haimes (2012) developed three guiding questions for decisions about how to treat
risks:

 - What can be done, and what options are available?

 - What are the trade-offs among all relevant costs, benefits, and risks?

 - What are the impacts of current decisions on future options?

Teng, Thekdi, and Lambert (2013, 2012) describe a risk, safety, or security program, with the three guiding questions:

 - What sources of risk are to be addressed by the program?

 - What are the allocations of resources of the program across risks, organizational units, time horizons, facilities etc.?

 - How is the program to be evaluated and adapted to changing circumstances?

**332** Advances in Hardware Design for Security and Trust

Integrated systems that benefit from application of the above principles are described by Beteto et al. (2024), Moghadasi et al. (2022a, 2022b), Andrews et al.
(2023), Collier et al. (2022), Johnson et al. (2022), Forkin et al. (2023), Moghadasi
and Lambert (2023), Loose et al. (2023), Baker et al. (2023), Moghadasi et al. (2024),
Johnson et al. (2023), and Bazemore et al. (2024).

The following sections of this chapter describe advances in systems engineering and risk analysis, and describe four case studies that illustrate applications of
methodologies for embedded hardware and enterprise systems.

**14.2** **STATE OF THE ART**

**14.2.1** **RISK IDENTIFICATION THROUGH BUSINESS PROCESS MAPPING**

As identified above, one of the first stages in risk analysis is to identify what can
happen (i.e., what can go wrong and cause harm to the system of interest; Kaplan &
Garrick, 1981). This step is commonly referred to as risk (or hazard) identification.

When considering the identification of risks in complex business processes, such
as the life cycle of a semiconductor, methods from the practice of business process reengineering, particularly business process mapping, can be helpful. Business
process reengineering is a process of examining the processes of a business, understanding which ones no longer adequately serve the organization, and creating
new processes that improve competitiveness, effectiveness, and efficiency (Grover &
Malhotra, 1997; Hammer, 1990). Business process modeling is used in reengineering efforts to visually document existing business processes and create and evaluate
the performance of new processes, comparing “as-is” and “to-be” cases (Bevilacqua
et al., 2015; Lin et al., 2002). Business processes are composed of activities that
add value for customers, are operated by resources within the organization (e.g., employees, equipment), and involve organizational units within an enterprise (Lin et al.,
2002). An effective business process model will serve as the basis for improving how
the business operates (Eriksson & Penker, 2000).

An innovation in business process mapping is that they can be utilized to identify
risks that may negatively impact various activities within a process. The IDEF0 modeling language consists of blocks, which are activities within a process, connected
by arrows. An activity can be thought of as a function that takes in various inputs,
transforms them using mechanisms, subject to a set of controls, and results in outputs (Menzel & Mayer, 1998). Lambert et al. (2006) modified the IDEF0 business
process modeling language (Menzel & Mayer, 1998) to include sources of risk for
a highway construction project (Figure 14.1). Teng et al. (2013, 2012) incorporated
sources of risk when developing business process models for risk management and
safety program administration.

**14.2.2** **MONITORING AND TRACKING OF RISKS USING RISK REGISTERS**

As sources of risk are identified, it is helpful to record them in a central document
for tracking and monitoring purposes. A risk register is a tool that organizations

Enterprise Risk Management of Electronics and Computing Device Supply Chains **333**

**Figure 14.1** IDEF0 block diagram with sources of risk.

utilize to monitor risks across the enterprise, and aids in the prioritization of risks
that require more of the resources of the organization (Leva et al., 2017). The use of
risk registers assures that risk assessment and risk management are ongoing for audit
purposes (Filippin & Dreher, 2004).

Risk registers are typically presented in a tabular format, with each row representing a unique hazard (Whipple & Pitblado, 2010). While the columns in the table
may vary, the core components of a risk register include the following: a unique risk
identification number, a description of each risk, a ranking of the risk based on a
quantification of its severity and likelihood, a risk owner responsible for managing
the risk, actions taken for each risk, and relevant dates when actions were taken or
target date when actions are scheduled to be completed (Leva et al., 2017). Other
elements may include existing risk controls in place, effectiveness of risk controls,
risk status, type or category of risk, and a target risk level (Leva et al., 2017).

The assessments of severity and likelihood can be depicted in a risk matrix (Filippin & Dreher, 2004). The risk register can also be used to generate relevant reports
and graphical summaries to assist with risk management (Filippin & Dreher, 2004).
Importantly, risk registers are not meant to be static documents, but should be continuously updated as new information becomes available, and facilitates all steps of
the risk management process, from risk identification through risk monitoring and
control (Lavanya & Malarvizhi, 2008).

While risk registers should be continuously updated, they often do not capture
information about the abundant uncertainty associated with the project or process
under evaluation. Karvetski and Lambert (2012) described how, in contrast to some
situations in which risks can be clearly quantified, there are certain situations (typically when fundamental knowledge is lacking) when uncertainty is best described
through scenarios. Scenarios reflect deep epistemic uncertainty and are narrative,
qualitative, and non-probabilistic (Karvetski & Lambert, 2012). Scenario analysis is
different from forecasting in that scenario analysis does not utilize probabilities to
characterize future conditions (Karvetski et al., 2010). A scenario can be defined as

**334** Advances in Hardware Design for Security and Trust

a non-empty and feasible set of emergent conditions, where emergent conditions are
assumptions about possible future conditions relevant for decision making (Karvetski et al., 2009).

The addition of scenario analysis techniques to risk registers allows for the prioritization of initiatives across different future scenarios, as well as the identification
of the most and least disruptive scenarios to the priorities of stakeholders. Example
domains in which scenario-based analyses have been demonstrated include supply
chains for electric vehicle to grid (V2G) systems (Moghadasi et al., 2022a), obsolescence management (Collier & Lambert, 2020), and systems integration project
management (Collier & Lambert, 2019).

**14.2.3** **RISK** **MANAGEMENT** **INVESTMENT** **DECISIONS** **USING** **SECURITY**
**ECONOMICS**

Among the guiding risk management questions (Haimes, 2012) is “What are the
trade-offs among all relevant costs, benefits, and risks?” Central to this insight is that
risk management actions involve the allocation of resources, which is true of hardware security as well (Hastings & Sethumadhaven, 2020). More generally, decisions
about what types of security measures to implement often are rooted in economic
criteria. For example, organizations need to balance considerations such as the cost
of lack of security and the cost and efficacy of security solutions (Sonnenreich et al.,
2006). Authors have described security failures as instances of more common economic problems, such as “the market for lemons” and “the tragedy of the commons”
(Hastings & Sethumadhaven, 2020; B¨ohme, 2006).

The field of security economics (Anderson & Moore, 2006) aims to guide security
investment decisions through the use of economic modeling approaches. One of the
prominent models in security economics is the Gordon-Loeb model, which identifies
the optimal level of security investment, based on the expected benefit of information
security (Gordon & Loeb, 2012). The model is based on assessing the difference in
a system’s vulnerability in an unprotected state and in a state conditional on a level
of investment in security (Gordon & Loeb, 2012).

Another approach to security investment decision making is to calculate the return on security investment (ROSI), which assesses how much potential loss can be
avoided (i.e., risk reduction) by investment in security measures (ENISA, 2012). It
is a calculation of a return on investment (ROI) that compares the loss reduction to
the cost of the solution (ENISA, 2012).

**14.2.4** **ASSESSMENT** **OF** **SUPPLY** **CHAIN** **RESILIENCE** **THROUGH** **STRESS**
**TESTING**

While risk analysis is a valuable tool within the process of systems engineering, only
the risks that are identified and controlled can be effectively managed. Linkov et al.
(2022) contrasted the process of risk analysis with resilience analysis, where the latter implies an acceptance that some disruptions may not be anticipated ahead of time,

Enterprise Risk Management of Electronics and Computing Device Supply Chains **335**

and therefore assesses how systems can be designed and managed such that disruptions have a minimal impact. Focusing on risk involves preparing for and absorbing
shocks, while focusing on resilience involves analyzing how system performance
degrades after a disruption and how it can adapt and recover to pre-disruption levels (Linkov et al., 2022). For supply chains, post-pandemic resilience requires continuous preparation for disruptions amidst a constantly changing environment (i.e.,
“crisis as normal”; Ivanov & Dolgui, 2021).

Given the importance of supply chains for certain goods, such as semiconductors,
some authors have called for stress testing the supply chain (Ivanov & Dolgui, 2021;
Simchi-Levi & Simchi-Levi, 2020). Stress testing refers to approaches that are used
to assess the vulnerability of a system when subjected to stressors outside of normal
operating conditions ( Cih´ak, <sup>ˇ</sup> 2007; Blaschke et al., 2001). Plausible scenarios are
created to uncover potential points of failure (Pescaroli & Needham-Bennett, 2021;
Flood & Korenko, 2015). The system’s performance under a stressor scenario is
compared to its performance under a baseline scenario to facilitate comparison (Thun
et al., 2013; Buncic & Melecky, 2012).

Stress testing has been traditionally applied within financial contexts, such as for
financial portfolios or institutions like banks, but the modeling principles have been
extended to supply chains (e.g., Jain & Leong, 2005; Ivanov & Dolgui, 2021). Necessary for a stress test is an appropriate set of key performance indicators (KPIs) to
measure performance, such as time to recover (TTR) (Simchi-Levi et al., 2015).

**14.3** **SAMPLE APPLICATIONS**

The following sub-sections provide an overview of applications of the methodologies
described above.

**14.3.1** **IDENTIFICATION** **OF** **RISKS** **ACROSS** **THE** **SEMICONDUCTOR** **LIFE**
**CYCLE USING IDEF0**

There are many stages that comprise a life cycle of semiconductors. Areno (2020)
identified sources of risk associated with six broad life cycle stages: conceptual/design, integration, manufacturing, testing, provisioning/configuration, and deployment. Within each of these stages, the process can be decomposed into multiple
sub-steps. The hierarchical nature of the IDEF0 modeling language is well suited to
processes of this kind, allowing users to view process steps at the desired level of
granularity (Lambert et al., 2006; Menzel & Mayer, 1998). For example, in Figure
14.2, the top-level diagram (designated A-0) contains a single block containing the
entire life cycle, and it can be decomposed into several constituent activities. Each
step can then be further decomposed into more granular sub-activities.

Lambert et al. (2006) defined three preliminary stages of building any business
process model. First, the purpose of the model must be identified. Second, the viewpoint of the model should be identified. Third, the appropriate depth and scope of the
model should be defined (Lambert et al., 2006). From there, data should be collected
on the process and the constituent activities and sub-activities, including the inputs,

**336** Advances in Hardware Design for Security and Trust

**Figure** **14.2** Hierarchical decomposition of a process applicable to enterprise risk
management of semiconductors and associated device supply chains.

outputs, controls, and mechanisms. Inputs describe what an activity consumes or
transforms, while the outputs describe the results of the activity. Controls describe
anything that guides, determines, or constrains an activity. Mechanisms describe how
an activity is completed, but unlike an input, is not something that is consumed. For
example, a mechanism may be a machine, employee, or other resource that accomplishes an activity (Lambert et al., 2006; Menzel & Mayer, 1998). In addition to
collecting information about all of the process activities, the sources of risk that impact each activity should be identified. These sources of risk are represented by arrows going into the lower left-hand diagonal side of the activity block (Collier et al.,
2023a; Lambert et al., 2006). Such information collection should be done with the
appropriate stakeholders and subject matter experts to capture the needed knowledge
about a business process.

Once the data are collected, the IDEF0 model can be constructed according to the
defined syntax of boxes and arrows. A complete overview of the modeling syntax is
beyond the scope of the chapter but some general guidelines are provided here. First,
each activity box requires at least one output and control, while input and mechanism
arrows are not strictly required. Second, arrows may join or fork, designating the
bundling or decomposition of various aspects of the process flow (e.g., the same
mechanism may be shared across several activities). Finally, a general convention is
that two to nine activity boxes should be included within each diagram (Menzel &
Mayer, 1998).

As an illustration of the methodology, Collier et al. (2023a) developed IDEF0
diagrams, modified to include sources of risk, for a generic semiconductor’s life
cycle. At a high level, six main activities were identified: design, integration,

Enterprise Risk Management of Electronics and Computing Device Supply Chains **337**

fabrication, testing, provisioning, and deployment. Demonstrating the hierarchical
decomposition feature of IDEF0, the fabrication stage was decomposed into the following sub-activities: mask manufacturing, wafer manufacturing, photolithography,
etching, electrode formation, and inspection. For each of these two levels of system
decomposition, sources of risk were taken from Areno (2020). For example, within
the manufacturing stage, nine sources of risk were identified, such as insertion of
Trojan circuitry, reverse engineering, and overproduction of parts (Areno, 2020). Finally, the sub-activity of wafer manufacturing was further sub-divided into activities
such as ingot pulling, ingot slicing, wafer polishing, and oxidation (Collier et al.,
2023a).

**14.3.2** **PRIORITIZATION OF DISRUPTION SCENARIOS TO ELECTRIC VEHI-**
**CLE TO GRID SYSTEMS**

The methodological risk register framework is based on a scenario-based decision
model with the following elements (Moghadasi et al., 2022a; Collier et al., 2018).
Let Sc = {c1,...,cm} be the set of m performance criteria, Sx = {x1,...,xn} be the
set of n initiatives (e.g., projects, technologies, processes), Sec = {ec1,...,ecp} be the
set of p emergent conditions, and Ss = {s1,...,sq} be the set of q scenarios (where a
scenario is a non-empty set of emergent conditions). Let w jk be the weight placed on
criterion c j in scenario sk. Using a linear-additive value function, a scenario-specific
score can be assigned to initiative xi as follows:

Vk (xi) =

m
###### ∑

j=1

w jk ∗ v j(xi)

where v j(xi) is the partial value function of the i-th initiative assessed against the j-th
criterion (Belton & Stewart, 2002).

The process is summarized as follows. First, information is collected about the
set of n initiatives relevant for a system. As mentioned above, an initiative may be a
project, technology, investment, activity, or other item that requires an allocation of
resources. The next step is to identify and weight the performance criteria. The criteria are based on system objectives, and represent the values of the key stakeholders.
There are a number of weighting techniques, for example rank-sum weighting methods, or more linguistic approaches can be used. For each criterion, a stakeholder
can select the emphasis relative to the criteria set using responses such as “low”,
“medium”, and “high”, and these responses can then be converted into numerical
weight values. The resultant set of weights represents the baseline scenario. Next, a
criteria-initiative assessment is conducted, in which stakeholders are asked the degree to which an initiative xi addresses criterion c j, again using linguistic terms such
as “strongly agree”, “agree”, “somewhat agree”, or “neutral”. These responses are
again converted into numerical scores, and represent the partial value function v j(xi)
under the baseline scenario. From here, the baseline ranking of initiatives can be performed. The result is a 1 through n ranking of initiatives (Moghadasi et al., 2022a;
Collier et al., 2018).

**338** Advances in Hardware Design for Security and Trust

Scenarios are generated by combining emergent conditions one or more at a time
(Karvetski & Lambert, 2012). It has been recommended that four to six scenarios
be identified (Stewart et al., 2013). Once a set of scenarios is identified, the criteria
weights are reweighted to explore the impact of the scenario on the priorities of the
stakeholders. Asking the question, “Under scenario sk, is criterion c j more or less
important than in under the baseline scenario?” to which a respondent can answer
“increases”, “increases somewhat”, “no change”, “decreases somewhat”, and “decreases” (Karvetski & Lambert, 2012). Based on the method described by Karvetski
et al. (2009), the weights are rescaled and renormalized to sum to 1. The result is
a unique set of scenario-specific criteria weights for each scenario. These can be
used to create new scenario-specific rankings of initiatives, resulting in a unique set
initiative rankings across each scenario.

Finally, the level of disruption of each scenario is calculated based on comparing
the rank ordering of a future scenario to the baseline ordering. A number of rank
correlation coefficients can be used (e.g., Spearman rho, Kendall tau) to compare
the level of disruption from a baseline ranking, where lower degrees of correlation
indicate a larger disruption (Moghadasi et al., 2022a; Collier et al., 2018).

Moghadasi et al. (2022a) demonstrated the above methodology on the development and deployment of bidirectional electric vehicle chargers. First, 10 performance
criteria were identified: lower economic cost, increase economic revenue, keep up
with market standards, reduce carbon emissions, reduce cyber attack vulnerability,
availability, reduced energy consumption, affordability, durability, and increase selfsufficiency. This set represents stakeholder goals for the system of chargers. The criteria were weighted based on the linguistic procedure described above. Next a set of
20 initiatives was generated, including such activities as develop charge controllers,
identify at-risk components, and analysis of long-term use of batteries. Given a set
of n initiatives and m criteria, an m ∗ n matrix was created to perform the criteriainitiative assessment. Symbolic responses can be used in place of linguistic ones,
for example, •,, ◦,- can be used to represent the responses{strongly agree, agree,
somewhat agree, neutral}. These responses are then converted into numerical scores.
By taking the weighted sum of the scores and weights, a ranked list of initiatives can
be created that represents the baseline condition (Moghadasi et al., 2022a).

From there, scenarios were identified by combining one or more emergent conditions. In total, 37 emergent conditions were identified and combined to form nine
scenarios: private support, public support, electricity market, green movement, technology innovation, funding decreases, change of vendor, obsolete technology, and
change in government policy. Given q scenarios and m criteria, an m*q matrix can
be constructed that facilitates the criteria-scenario relevance assessment, in which
each criterion may increase, increase somewhat, not change, decrease somewhat,
or decrease in relevance relative to the baseline scenario. Again, these responses
were converted into numerical scores that adjust the respective weights upward or
downward. The resulting weight sets are then used to generate q new initiative rankings. Finally, the most disruptive scenarios to stakeholder priorities can be identified
using a rank correlation metric. In this case, the scenarios of “electricity market”

Enterprise Risk Management of Electronics and Computing Device Supply Chains **339**

**Figure 14.3** Risk register methodology applicable to the accounting of most disruptive scenarios in across the lifecycle of semiconductors and their supply chains.

(consisting of emergent conditions related to the cost and demand for electricity)
and “funding decreases” (consisting of emergent conditions related to project budgets and schedules) were the two most disruptive (Moghasasi et al., 2022a). Figure
14.3 provides a summary of the methodology.

**14.3.3** **TECHNO-ECONOMIC ANALYSIS OF HARDWARE SECURITY INVEST-**
**MENT PORTFOLIOS**

Organizationally, justifying investment in security measures can be difficult, as such
investments are typically not revenue producing. Rather, the benefits accrued to the
enterprise are in the form of reduced risk. To quantify such benefits, economic metrics have been proposed that aim to capture the benefits, and in some cases, the costs.

One such metric is ROSI (ENISA, 2012). ROSI is calculated by first determining
the Annual Loss Expectancy (ALE), the loss incurred by an organization in the case
of a single cyber attack. It is the product of the Single Loss Expectancy (SLE) and the
Annual Rate of Occurrence (ARO), a frequency of annual attacks. SLE is determined
by multiplying the Asset Value (AV) by the Exposure Factor (EF). The AV represents
the total magnitude of a loss, and the EF represents a fraction of the AV that would
be lost (ENISA, 2012). ALE, therefore is calculated by:

ALE = SLE ∗ ARO = AV ∗ EF ∗ ARO

ROSI is determined by estimating the cost savings (i.e., risk reduction) associated

**340** Advances in Hardware Design for Security and Trust

with a countermeasure less the cost of its implementation, divided by the cost:

ROSI = <sup>ALE −</sup> <sup>mALE −</sup> <sup>Annual Cost</sup>

Annual Cost

In the equation above, mALE is the modified ALE with the countermeasure purchased and implemented, and is based on a Mitigation Ration (MR) for the countermeasure that measures the percentage of attacks successfully prevented. The mALE
is defined as:

mALE = ALE ∗ (1 − MR)

Other metrics can similarly be defined based on the Gordon-Loeb model introduced
above (Gordon & Loeb, 2012). Let z be the amount of money invested in the countermeasure, v be the vulnerability of an asset (in the absence of the countermeasure)
measured as the probability of a successful attack, t be the threat measured as a
probability of an attack, and λ be the loss associated with a successful attack. Further, assume S(z,v) is the new vulnerability given an investment of z and a starting
vulnerability of v (Gordon & Loeb, 2012). Therefore, the Expected Net Benefit of
Information Security (ENBIS) is equal to:

ENBIS (z) = [v          - S (z, v)]tλ−z

Collier et al. (2023b) investigated the utility of such metrics. Specifically, four metrics were analyzed: ENBIS, EBIS (expected benefit of information security, which is
equal to ENBIS but without subtracting the cost), ROSI, and benefit/cost (B/C) ratio
(which is equal to ROSI without subtracting cost in the numerator). For the demonstration, a notional smart warehouse was considered, with various sensors, connected
devices, and cloud capabilities. The AV was assumed to be $2,250,000, and the EF
was assumed to be 100%, therefore the SLE was equal to the entire AV. ARO was set
to 10. For the case study, 10 mitigations were proposed: firewall protection, wired
sensors, two factor authentication for firmware updates, sensor polling procedures,
premium/trusted sensors, buddy system for handling protocol improvements, security protocols for improved staff hygiene, intermittent attack protection/monitoring,
and power grid protection/monitoring. For each of the mitigations, the MR, years
of use, and cost were estimated. From there, the four metrics (ENBIS, EBIS, ROSI,
B/C ratio) were calculated. By varying the total budget for countermeasures in increments of $5,000 from $5,000 to $225,000, portfolios of countermeasures were
created based on each metric. For each countermeasure, the surplus, defined as the
budget minus the amount invested in countermeasures, was calculated (Collier et al.,
2023b).
The analysis showed that, in the demonstration case, EBIS and ENBIS provided
the same recommendations for what countermeasures to select at each budget level.
Similarly, ROSI and B/C ratio provided the same recommendations, but the two sets
of recommendations differed. One difference was that the EBIS and ENBIS metrics
did not select any mitigations until a budget level of $40,000 was reached, while
ROSI and B/C ratio recommended two mitigations with the lowest budget of $5,000.
This is because ROSI and B/C ratio are both ratio-based measures, with cost in the

Enterprise Risk Management of Electronics and Computing Device Supply Chains **341**

**Figure 14.4** Overview of techno-economic methodology applicable to risk management of semiconductors and their supply chains.

denominator, and therefore they tend to favor more inexpensive mitigations. These
inexpensive measures may not necessarily be strongly correlated with benefit (i.e.,
risk reduction). Therefore, care must be taken when selecting metrics to use for investment purposes (Collier et al., 2023b). Figure 14.4 provides an overview of the
methodology.

**14.3.4** **DISCRETE** **EVENT** **SIMULATION-BASED** **STRESS** **TEST** **FOR** **SUPPLY**
**CHAIN RESILIENCE**

An organization, situated within a global supply chain ecosystem, may experience
delays and shocks from a number of external stressors – from climate change and extreme weather to more operational factors like delayed shipments from an upstream
supplier. In all cases, it is beneficial to understand how the KPIs of an organization
are impacted by various stressors.

The methodology was described by Collier et al. (2023c) and is based on a discrete
event simulation model. Discrete event simulations are based on discrete time steps,
where the model outputs at a time step influence the parameters in future steps. The
supply chain is first created with nodes and arrows connecting them to represent the
flow of materials. Nodes may have their own individual behaviors and parameters,
or be grouped into classes (e.g., the set of all manufacturing nodes). Parameters such
as maximum inventory capacity, initial inventory level, production rates, delivery
times, and various inventory costs are defined, as well as policies and rules for when
to place new orders (Collier et al., 2023c).

From this initial parameterization, a simulation can be performed to generate time
series of relevant node parameters (e.g., costs at each node, inventory held at each

**342** Advances in Hardware Design for Security and Trust

**Figure 14.5** Resilience curves showing the resilience enhancement under a scenario
with mitigations in place (the mitigated performance) relative to without mitigations
in place (the disrupted performance).

node), representing a normal or baseline case. Next, the model can be run in a “disrupted” state by changing one or more model parameters to represent the impact of a
supply chain disruption, such as a delay or cost increase. Finally, the simulation can
be run in the disrupted state but with the implementation of some risk management
countermeasure or strategy. A number of supply chain risk management approaches
and inventory management strategies could be leveraged (Chopra & Sodi, 2004).
Plotting the three performance curves together allows for a comparison of the effectiveness of the risk management actions, and can be used to explore the system’s
resilience, or ability to “bounce back” to pre-disruption performance levels (Collier
et al., 2023c).

Collier et al. (2023c) described a simplified supply chain comprising a single
foundry, an outsourced semiconductor assembly and test (OSAT) company, and a
system integrator. The foundry purchases raw materials from a supplier outside of
the simulation boundary. The foundry converts the raw materials into a wafer, the
OSAT converts the wafer into packaged chips, and the system integrator uses them
to produce a final product that is then sold to a customer. Parameters relating to costs
and processing times can be set for each supply chain actor. Penalties for stockouts
are included, as well as holding costs, in order to simulate the tension between holding too little and too much inventory (Collier et al., 2023c).

The simulation serves as a testbed for understanding the impacts of supply chain
risks and how performance may, or may not, bounce back to pre-disruption levels.
For example, Figure 14.5 displays the output of resilience curves. The blue line is the

Enterprise Risk Management of Electronics and Computing Device Supply Chains **343**

baseline performance (in this case, measured as cost), for a system integrator. The
red line shows the cost relative to the baseline due to a disruption of an upstream
OSAT. The performance degrades (i.e., cost rapidly spikes) due to unavailability of
materials, and slowly recovers as material shipments begin to resume. However, the
green resilience curve shows the mitigated performance of a disruption, for example,
by buying additional safety stock early in the simulation. The cost increases over the
baseline somewhat, but the extra inventory is able to offset the disruption later in the
simulation. Therefore, we can compare the two curves and conclude that the system
integrator has increased their resilience by investing in mitigations.

**14.4** **CONCLUSION**

Effective and comprehensive hardware security involves not just technological advancements in the design of electronic components, but extends to systems engineering practices that support risk assessment and risk management. This involves
mitigating risks across the supply chain and is multidisciplinary in nature.

In this chapter, several methodologies of systems engineering were demonstrated
to aid in the understanding and management of enterprise-wide risks of the supply
chains of semiconductors. First, a methodology for identifying risks was described
that utilizes business process mapping techniques. Next, a risk register-based approach was demonstrated that allows users to understand the impact of risk scenarios
on system-level priorities. Third, recognizing that risk management countermeasures
require investment of organizational resources, a set of benefit and benefit/cost metrics was introduced. Finally, a stress-testing methodology for these supply chains
was described to use discrete-event simulation, enabling managers to visualize the
impacts of disruptions to relevant KPIs, and their ability to restore system functions
as timely as possible.

**REFERENCES**

1. Anderson, R., Moore, T. (2006). The economics of information security. Science, 314,
610–613.
2. Andrews, D., Eddy, T., Hollenback, K., Sreekumar, S., Loose, D., Pennetti, C., Polmateer, T., Haug, J., Oliver-Clark, L., Williams, J., & others (2023). Enterprise risk management for automation in correctional facilities with pandemic and other stressors. Risk
Analysis, 43(4), 820–837.
3. Areno, M. (2020). Supply chain threats against integrated circuits. Intel White
Paper. [https://www.intel.com/content/dam/www/public/us/en/documents/white-](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/supply-chain-threats-v1.pdf)
[papers/supply-chain-threats-v1.pdf](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/supply-chain-threats-v1.pdf)
4. Baker, R., Polmateer, T., Marcellin, M., Chen, T., Riggs, R., Iqbal, T., Hendrickson, D.,
Slutzky, D., & Lambert, J. (2023). Mixed-Integer Programming with Enterprise Risk
Analysis for Vehicle Electrification at Maritime Container Ports. In 2023 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1759–1766).
5. Bazemore, B., Cha, M., Goss, Z., Haywood, H., Dye, B., Gunn, M., Loose, D., Polmateer, T., Hendrickson, D., & Lambert, J. (2024). Electrification of Utility Tractors at

**344** Advances in Hardware Design for Security and Trust

Maritime Container Ports. In 2024 Systems and Information Engineering Design Symposium (SIEDS) (pp. 221–226).
6. Belton, V., Stewart, T.J. (2002). Multiple Criteria Decision Analysis: An Integrated Approach. Boston: Kluwer Academic Publishers.
7. Beteto, A., Melo, V., Lin, J., Alsultan, M., Dias, E., Korte, E., Johnson, D., Moghadasi,
N., Polmateer, T., & Lambert, J. (2022). Anomaly and cyber fraud detection in
pipelines and supply chains for liquid fuels. Environment Systems and Decisions, 42(2),
306–324.
8. Bevilacqua, M., Mazzuto, G., Paciarotti, C. (2015). A combined IDEF0 and FMEA approach to healthcare management reengineering. International Journal of Procurement
Management, 8(1/2), 25–43.
9. Blaschke, W., Jones, M.T., Majnoni, G., Peria, S.M. (2001). Stress testing of financial
systems: An overview of issues, methodologies, and FSAP experiences. IMF Working
Paper WP/01/88, International Monetary Fund.
10. B¨ohme R. (2006). A comparison of market approaches to software vulnerability disclosure. Proceedings of ETRICS.
11. Buncic, D., Melecky, M. (2012). Macroprudential stress testing of credit risk: A practical
approach for policy makers. Policy Research Working Paper 5936, The World Bank.
12. Chopra, S., Sodhi, M.S. (2004). Managing risk to avoid supply chain breakdown. (2004).
MIT Sloan Management Review, 46(1), 53–61.
13. Cih´ak, M., (2007). Introduction to applied stress testing. IMF Working Paper WP/07/59, <sup>ˇ</sup>
International Monetary Fund.
14. Collier, Z., Gaskins, A., & Lambert, J. (2022). Business process modeling for semiconductor production risk analysis using IDEF0. IEEE Engineering Management Review, 51(1), 183–188.
15. Collier, Z.A., Briglia, B., Finkelston, T., Manasco, M.C., Slutzky, D.L., Lambert, J.H.
(2023b). On metrics and prioritization of investments in hardware security. Systems Engineering, 26(4), 425–437.
16. Collier, Z.A., Gaskins, A., Lambert, J.H. (2023a). Business process modeling for semiconductor production risk analysis using IDEF0. IEEE Engineering Management Review, 51(1), 183–188.
17. Collier, Z.A., Hendrickson, D., Polmateer, T.L., Lambert, J.H. (2018). Scenario analysis and PERT/CPM applied to strategic investment at an automated container port.
ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part A: Civil
Engineering, 4(3), 04018026.
18. Collier, Z.A., Lambert, J.H. (2019). Evaluating management actions to mitigate disruptive scenario impacts in an e-commerce systems integration project. IEEE Systems
Journal, 13(1), 593–602.
19. Collier, Z.A., Lambert, J.H. (2020). Managing obsolescence of embedded hardware and
software in secure and trusted systems. Frontiers in Engineering Management, 7(2),
172–181.
20. Collier, Z.A., Loose, D.C., Sellers, E., Polmateer, T.L., Behl, M., Linkov, I., Lambert,
J.H. (2023c). Stress testing for resilience of semiconductor supply chains. IEEE 14th Annual Ubiquitous Computing, Electronics & Mobile Communication Conference (UEMCON), 12–14 October, 2023, New York, NY.
21. DiMase, D., Collier, Z.A., Carlson, J., Gray, Jr., R.B., Linkov, I. (2016). Traceability
and risk analysis strategies for addressing counterfeit electronics in supply chains for
complex systems. Risk Analysis, 36(10), 1834–1843.

Enterprise Risk Management of Electronics and Computing Device Supply Chains **345**

22. DiMase, D., Collier, Z.A., Chandy, J., Cohen, B.S., D’Anna, G., Dunlap, H., Hallman,
J., Mandelbaum, J., Ritchie, J., Vessels, L. (2020). “A holistic approach to cyber physical
systems security and resilience.” Proceedings of IEEE/NDIA/INCOSE Systems Security
Symposium 2020, 01 July–01 August, Virtual.
23. DiMase, D., Collier, Z.A., Heffner, K., Linkov, I. (2015). “Systems engineering framework for cyber physical security and resilience.” Environment Systems & Decisions,
35(2), 291–300.
24. DiMase, D., Collier, Z.A., Pav, B., Chandy, J.A., Heffner, K., Walters, S. (2019). “Engineering for vehicle cyber security.” In: D’Anna, G. (ed.), Cybersecurity for Commercial
Vehicles, (pp. 67–98). SAE International: Warrendale, PA.
25. ENISA (2012). Introduction to Return on Security Investment. European Network and
Information Security Agency (ENISA).
26. Eriksson, H.E., Penker, M. (2000). Business Modeling With UML – Business Patterns at
Work. New York, NY, USA: Wiley.
27. Filippin, K., Dreher, L. (2004). Major hazard risk assessment for existing and new facilities. Process Safety Progress, 23(4), 237–243.
28. Flood, M.D., Korenko, G.G. (2015). Systemic scenario selection: Stress testing and the
nature of uncertainty. Quantitative Finance, 15(1), 43–59.
29. Forkin, E., Paulen, C., Swierczewski, M., Roy, T., Costello, T., Loose, D., Williams, J.,
Slutzky, D., Polmateer, T., Jackson, K., & others (2023). Capacity Planning and Investment for Electrification of Maritime Container Ports. In 2023 Systems and Information
Engineering Design Symposium (SIEDS) (pp. 143–148).
30. Gordon, L.A., Loeb, M.P. (2012). The economics of information security investment.
ACM Transactions on Information and System Security, 5(4), 438–457.
31. Graham, S. (2002). Making microchips takes mountains of materials. Scientific Ameri[can, https://www.scientificamerican.com/article/making-microchips-takes-m/](https://www.scientificamerican.com/article/making-microchips-takes-m)
32. Grover, V., Malhotra, M.K. (1997). Business process reengineering: A tutorial on the
concept, evolution, method, technology and application. Journal of Operations Management, 15, 193–213.
33. Haimes, Y.Y. (2012). Systems-based guiding principles for risk modeling,
planning, assessment, management, and communication. Risk Analysis, 32(9),
1451–1467.
34. Hammer, M. (1990). Reengineering work: Don’t automate, obliterate. Harvard Business
[Review, https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate](https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate)
35. Hastings, A., Sethumadhavan, S. (2020). WaC: a new doctrine for hardware security. In
4th Workshop on Attacks and Solutions in Hardware Security (ASHES’20), November
13, 2020, Virtual Event, USA. ACM, New York, NY, USA.
36. Hillson, D. (1999). Developing effective risk responses. Proceedings of the 30th Annual
Project Management Institute 1999 Seminars & Symposium, Philadelphia, Pennsylvania, USA
37. Horowitz, B.M., Lambert, J.H. (2006). Assembling off-the-shelf components: “learn as
you go” systems engineering. IEEE Transactions on Systems, Man, and CyberneticsPart A: Systems and Humans, 36(2), 286–297.
38. ISO/IEC/IEEE (2023). ISO/IEC/IEEE 15288:2023 Systems and software engineering

[— System life cycle processes. https://www.iso.org/standard/81702.html](https://www.iso.org/standard/81702.html)
39. INCOSE (2006). INCOSE Systems Engineering Handbook.
40. Ivanov, D., Dolgui, A. (2021). Stress testing supply chains and creating viable ecosystems. Operations Management Research, 15(1–2), 475–486.

**346** Advances in Hardware Design for Security and Trust

41. Jain, S., Leong, S. (2005). Stress testing a supply chain using simulation. Proceedings
of the Winter Simulation Conference.
42. Johnson, D., Melo, V., & Lambert, J. (2022). Risk identification with entity attributes
diagrams in business process modeling. In 2022 IEEE International Symposium on Systems Engineering (ISSE) (pp. 1–8).
43. Johnson, D., Wheeler, R., Marcellin, M., Moghadasi, N., Altman, R., Polmateer, T., &
Lambert, J. (2023). Integration of Risk Sources and Risk Controls to SysML Requirements Diagrams With Application to Sustainable Aviation Fuels. In 2023 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM) (pp.
443–449).
44. Kaplan, S., Garrick, B.J. (1981). On the quantitative definition of risk. Risk Analysis,
1(1), 11–27.
45. Karvetski, C.W., Lambert, J.H. (2012). Evaluating deep uncertainties in strategic
priority-setting with an application to facility energy systems. Systems Engineering,
15(4), 483–493.
46. Karvetski, C.W., Lambert, J.H., Linkov, I. (2009). Emergent conditions and multiple criteria analysis in infrastructure prioritization for developing countries. Journal of MultiCriteria Decision Analysis, 16, 125–137.
47. Karvetski, C.W., Lambert, J.H., Linkov, I. (2010). Scenario and multiple criteria decision
analysis for energy and environmental security of military and industrial installations.
Integrated Environmental Assessment and Management, 7(2), 228–236.
48. Kleindorfer, P.R., Saad, G.H. (2005). Managing disruption risks in supply chains. Production and Operations Research, 14(1), 53–68.
49. Lambert, J.H., Jennings, R.K., Joshi, N.N. (2006). Integration of risk identification with
business process models. Systems Engineering, 9(3), 187–198.
50. Lavanya, N. & Malarvizhi, T. (2008). Risk analysis and management: a vital key to effective project management. Paper presented at PMI® Global Congress 2008, Newtown
Square, PA: Project Management Institute.
51. Leva, M.C., Balfe, N., McAleer, B., Rocke, M. (2017). Risk registers: Structuring data
collection to develop risk intelligence. Safety Science, 100, 143–156.
52. Lin, F.R., Yang, M.C., Pai, Y.H. (2002). A generic structure for business process modeling. Business Process Management Journal, 8(1), 19–41.
53. Linkov, I., Trump, B.D., Trump, J., Pescaroli, G., Hynes, W., Mavrodieva, A., Panda,
A. (2022). Resilience stress testing for critical infrastructure. International Journal of
Disaster Risk Reduction, 82, 103323.
54. Loose, D., Eddy, T., Polmateer, T., Hendrickson, D., Moghadasi, N., & Lambert, J.
(2023). Reinforcement learning and automatic control for resilience of maritime container ports. In 2023 9th International Conference on Control, Decision and Information
Technologies (CoDIT) (pp. 1–6).
55. Lowrance, W.W. (1976). Of Acceptable Risk: Science and the Determination of Safety.
William Kaufman, Inc., Los Altos, CA, USA.
56. Menzel, C., Mayer, R.J. (1998). The IDEF family of languages, in Handbook on Architectures of Information Systems, Bernus, P., Mertens, K., Schmidt, G. Eds. Berlin,
Heidelberg: Springer, 209–241.
57. Moghadasi, N., Valdez, R., Piran, M., Moghaddasi, N., Linkov, I., Polmateer, T., Loose,
D., & Lambert, J. (2024). Risk Analysis of Artificial Intelligence in Medicine with a
Multilayer Concept of System Order. Systems, 12(2), 47.
58. Moghadasi, N., & Lambert, J. (2023). On Evaluating System Resilience by the Degree
of Order Disruption. In INCOSE International Symposium (pp. 739–751).

Enterprise Risk Management of Electronics and Computing Device Supply Chains **347**

59. Moghadasi, N., Collier, Z., Koch, A., Slutzky, D., Polmateer, T., Manasco, M., & Lambert, J. (2022a). Trust and Security of Electric Vehicle-to-Grid Systems and Hardware
Supply Chains. Reliability Engineering & System Safety, 108565.
60. Moghadasi, N., Luu, M., Adekunle, R., Polmateer, T., Manasco, M., Emmert, J., & Lambert, J. (2022b). Research and development priorities for security of embedded hardware
devices. IEEE Transactions on Engineering Management, 71, 2800–2811.
61. Pescaroli, G., Needham-Bennett, C. (2021). Operational resilience and stress testing: Hit
or myth? Capco Institute Journal of Financial Transformation, 53, 32–43.
62. Simchi-Levi, D., Schmidt, W., Wei, Y., Zhang, P.Y., Combs, K., Ge, Y., Gusikhin, O.,
Sander, M., Zhang, D. (2015). “Identifying risks and mitigating disruptions in the automotive supply chain,” INFORMS Interfaces, 45(5), 375–390.
63. Simchi-Levi, D., Simchi-Levi, E. (2020). We need a stress test for critical sup[ply chains. Harvard Business Review, https://hbr.org/2020/04/we-need-a-stress-test-for-](https://hbr.org/2020/04/we-need-a-stress-test-for-critical-supply-chains)
[critical-supply-chains](https://hbr.org/2020/04/we-need-a-stress-test-for-critical-supply-chains)
64. Society for Risk Analysis (2018). Risk Analysis Glossary. [https://www.sra.org/risk-](https://www.sra.org/riskanalysis-introduction/risk-analysis-glossary)
[analysis-introduction/risk-analysis-glossary/](https://www.sra.org/riskanalysis-introduction/risk-analysis-glossary)
65. Sonnenreich, W., Albanese, J., Stout, B. (2006). Return on security investment (ROSI)

   - a practical quantitative model. Journal of Research and Practice in Information Technology, 38(1), 45–56.
66. Stewart, T. J., S. French, and J. Rios. 2013. Integrating multicriteria decision analysis
and scenario planning—Review and extension. Omega, 41(4), 679–688.
67. Teng, K.Y., Thekdi, S.A., Lambert, J.H. (2012). Identification and evaluation of priorities in the business process of a risk or safety organization. Reliability Engineering &
System Safety, 99, 74–86.
68. Teng, K.Y., Thekdi, S.A., Lambert, J.H. (2013). Risk and safety program performance
evaluation and business process modeling. IEEE Transactions on Systems, Man, and
Cybernetics—Part A: Systems and Humans, 42(6), 1504–1513.
69. Thun, C., Prioux, S., Canamero, M.C. (2013). Stress testing best practices: A
seven steps model. Moody’s Analytics. [https://www.moodysanalytics.com/risk-](https://www.moodysanalytics.com/risk-perspectives-magazine/stresstesting-europe/approaches-to-implementation/stres-stesting-bestpractices-a-seven-steps-model)
[perspectives-magazine/stresstesting-europe/approaches-to-implementation/stress-](https://www.moodysanalytics.com/risk-perspectives-magazine/stresstesting-europe/approaches-to-implementation/stres-stesting-bestpractices-a-seven-steps-model)
[testing-bestpractices-a-seven-steps-model](https://www.moodysanalytics.com/risk-perspectives-magazine/stresstesting-europe/approaches-to-implementation/stres-stesting-bestpractices-a-seven-steps-model)
70. Varas, A., Varadarajan, R., Goodrich, J., Yinug, F. (2021). Strengthening the Global
Supply Chain in an Uncertain Era. Boston, MA, USA: Boston Consulting Group and
Semiconductor Industry Association.
71. Whalen, J. (2021). Three months, 700 steps: Why it takes so long to produce a com[puter chip. The Seattle Times. https://www.seattletimes.com/business/technology/three-](https://www.seattletimes.com/business/technology/three-months-700-steps-why-it-takesso-long-to-produce-a-computer-chip)
[months-700-steps-why-it-takesso-long-to-produce-a-computer-chip](https://www.seattletimes.com/business/technology/three-months-700-steps-why-it-takesso-long-to-produce-a-computer-chip)
72. Whipple, T., Pitblado, R. (2010). Applied risk-based process safety: A consolidated risk
register and focus on risk communication. Process Safety Progress, 29(1), 39–46.

### Index

3D integration, 5, 126
3D reconstruction, 75–77, 79–80,
85–86, 105, 109

A
AES, 7, 39–40, 193–200, 202,

206–207, 209–214, 248,
265, 274, 296–297,
303–305, 325
Analog floating gate transistors,

134–135, 143, 145–146
Analog neural network, 147–149
Architectural flaws, 269, 272, 279,

291
Asynchronous design, 217, 220, 227,

237–239
Automatic bug localization, 288–290
Automatic design repair, 290

B
Benefit-cost ratio, 340–341
BEOL, 45, 110–111, 126–131,

187–188, 190, 192
Bi-functional units, 111
Branch prediction unit, 240–241,

244, 250, 264
Business process mapping, 332, 343

C
Cache-based attacks, 244–245, 247,

274, 281
Center for Strategic and International

Studies (CSIS), 22
Challenges in heterogenous

packaging, 174–175
Closed world, 313
Cloud-based analysis, 4, 103
Commercial Microelectronics

Security, 35–36

Commercial Microelectronics

Verification, 35–36
Concolic testing, 284–285, 292, 299
Confocal microscopy, 78, 82, 85–86,

105, 109
Contract manufacturers, 10–11
Convolutional neural networks, 194,

202, 297, 310, 326, 328
Correlative imaging, vii, 74–75, 78,

103, 105
Critical components, 10, 12, 17
Cyber trust mark, 16

D
Deep learning, viii, 5, 56, 58, 72, 94,

96, 99, 102, 109, 180,
192–197, 199, 201, 203,
205–207, 209–216, 290,
302, 326, 328–329
Defect detection, 75, 78–79, 87,

92–94, 102, 107, 109
Defects, 8, 11, 87–88, 90, 92, 101,

171, 176
Defense Advanced Research Project

Agency (DARPA), 24–25,
42, 44–45
Digital ledger, 16
Digital twin, 18
Digitally signed software, 8, 15
DO-254, 27, 48

E
Electromagnetic attacks, 277, 296
Embedded Field Programmable Gate

Arrays (eFPGAs), 31
Embedded fuse (eFUSE), 31
Emerging reliability monitoring

approaches, 181–184

349

**350** Index

F
Feature extraction, 59–60, 71
Femtosecond laser delayering, 4,

75–82, 86, 103, 105,
108–109
FEOL, 45, 110–111, 126–128
Fingerprint, 3, 18, 30, 71, 179, 191,

323
Fingerprinting, viii, 3, 5, 71,

179–180, 191, 302–303,
305–307, 309–311,
313–319, 321, 323–329
Firmware, xi, 8, 10–13, 15–18, 30,

243, 265, 297, 331, 340
FPGA attacks, 304–305, 325–326
Fuzzing, 269, 282, 285–287,

292–293, 299–300

H
Hardware Trojan detection, 49, 54,

63, 70–73, 181, 191–192,
238, 294
Hardware Trojans, vii, 2, 45, 50–53,

55, 57, 59, 61, 63, 65, 67,
69–71, 73, 190–191, 238,
269–271, 279, 284, 302
High performance computing (HPC)

cluster, 19
Hybrid cells, 227–229
Hyperparameter optimization,

208–209
Hyperparameters, 62, 65, 202,

208–209

I
IC reliability monitoring, 176, 181,

187
IDEF0, 332–333, 335–337, 344
Information flow tracking, 36, 269,

282–283, 298–299
Intelligence Advanced Research

Projects Activity (IARPA),
42
IP-XACT IEEE 1685, 27

ISA/IEC, 27
ISO26262, 27
ISO/SAE 21434, 27

L
Large language models, 207, 288,

301
Legislation, 12
Length of oxide diffusion, 154
Linear regression, 62, 72, 258
Logic obfuscation, 5, 110, 112,

126–127, 132, 166, 168

M
Machine learning, vii, 4, 18, 50–51,

53, 55, 57, 59, 61, 63, 65,
67, 69, 71–73, 75, 78–79,
93, 97, 107, 109, 161, 174,
184, 192, 203–205, 238,
248–250, 267, 286–287,
291, 295, 300, 303–304,
306–307, 309, 328–329
Memristors, 134–135, 143, 145, 164,

166
Microarchitectures, 243–244
Model extraction attack, 249, 258,

260–262
Monte Carlo simulations, 66
Muller C-Element, 227, 233–237,

239
Multi-layer perceptron, 59, 62–63,

258, 310
Multi-threshold voltage transistors,

152–153

N
National Vulnerability Database

(NVD), 26
NCL logic gates, 221, 223
Negative testing, 18
Network flow attack, 111, 114, 130
Neural network, 51, 58, 63, 147–149,

164, 167–168, 186, 195,
198, 200, 202–205,

Index **351**

207–212, 215, 249, 264,
266, 291, 303, 311
Null Convention Logic, 5, 217,

238–239

O
On-chip antenna-based approaches,

187–190
Open world, 310
Outsourcing, 8, 20, 110

P
Perceptions, of security, 11–12
Physical side-channels, 37–38, 40
Physically unclonable function

(PUF), 16–17, 30
Polymorphic electronics, 111–113,

131–132
Polymorphic switch boxes, 5,

119–120, 132
Power side-channel attacks, 276,

281, 287, 327–328
Printed circuit boards, 1, 4, 8, 74, 109
Privilege escalation attacks, 272, 291
Process drift, 54, 58, 61–62, 68, 70
Process Specific Functions (PSFs),

31
Process variations, 58, 70, 134, 143,

147, 150, 156, 158–159,
172, 178, 180, 183
Profit, 7, 10–11, 14
Proof-carrying hardware verification,

284
Provenance, 16

R
Reliability challenges, 172, 174–175
Requirements, 12–14, 27, 33, 36,

108, 226, 240, 243, 305,
330–331, 346
Resilience, xi, 112, 117–118, 134,

138, 141, 143, 147,
151–152, 164–165, 268,
272, 288, 291, 334–335,
341–347

Return on security investment

(ROSI), 334, 347
Reverse engineering, vii, 2–5, 26, 29,

31, 40, 57–58, 71, 74–79,
81–83, 85, 87–89, 91,
93–95, 97, 99, 101–103,
105, 107–109, 126–127,
134–135, 165, 217–218,
227, 246, 250, 280, 297,
337
Risk identification, 332–333, 346
Risk management, ix, 6, 27,

330–337, 339, 341–343,
345, 347
Risk register, 332–333, 337, 339,

343, 347
Row hammer, 24, 47
RTL logic attack, 114, 118, 120, 124
Run-time detection, 283–284

S
Scale, 7–8, 10, 14, 17–19, 37–38, 45,

50, 55, 85, 135, 165–170,
191, 196–200, 207, 215,
268, 297, 301–302, 305,
326, 329
Security controls, 8, 11
Security economics, 334
Semiconductor Industry Association

(SIA), 22
Side channel attacks, 193–213,

304–305, 313, 316,
324–326, 328
Side channel attacks on TEEs,

244–249
Side-channel vulnerability detection

techniques, 286
Simulation, 17–19, 37, 39–41, 49,

52, 66, 88, 90, 92, 100,
152–153, 161, 168, 212,
216, 220, 267, 271,
284–286, 291, 300,
311–312, 326, 341–343,
346

**352** Index

Speculative execution attacks, 275,

281
Split manufacturing, 5, 110, 114,

126–127, 131–133
Static timing analysis, 51, 59, 228,

230
Stress testing, 334–335, 344–347
Substitutions, 11, 17
Sustainment, 12
Synthetic data, 87, 90, 92–93, 96, 99,

102–103, 107, 109
Systems engineering, 6, 33–34,

330–332, 334, 343–346

T
Threshold gates, 221–225, 230,

234–235

Timing attacks, 273, 280–281, 328
Trace acquisition, 194, 196–199
Transformer architectures, 207–208
Trusted execution environments

(TEEs), 241–243
TrustZoneTunnel attack, 246, 249,

263–264

V
V-diagram, 33–34

W
Watermarking, 3, 17
Well proximity effect, 154

Y
Y-diagram, 32–33
