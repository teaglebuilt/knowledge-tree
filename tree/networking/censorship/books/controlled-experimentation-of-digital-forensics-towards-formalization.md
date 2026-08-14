---
title: Controlled Experimentation of Digital Forensics Towards Formalization for Strengthening
  Evidence Reproducibility, Reliability,… (Edson Oliveira, Jr., Thiago J. Silva etc.)
source: sources/networking/censorship/books/Controlled Experimentation of Digital
  Forensics Towards Formalization for Strengthening Evidence Reproducibility, Reliability,…
  (Edson Oliveira, Jr., Thiago J. Silva etc.) (z-library.sk, 1lib.sk, z-lib.sk).epub
source_type: book
source_hash: 306c4ce1f28f713dfbbee92d50edb1780767ef5abd0a9b16967e22387abbc918
tags:
- networking
- censorship
- book
extracted: '2026-08-14'
---

![Cover: Controlled Experimentation of Digital Forensics by Edson OliveiraJr, Thiago J. Silva, Charles V. Neu, Avelino F. Zorzo, Ana H. Mazur. Logo: Springer Nature Switzerland](../images/978-3-032-19951-5_CoverFigure.jpg)

Edson OliveiraJr, 
Thiago J. Silva, 
Charles V. Neu, 
Avelino F. Zorzo and 

Ana H. Mazur

# Controlled Experimentation of Digital Forensics

Towards Formalization for Strengthening Evidence Reproducibility, Reliability, and Transparency

![Springer](../images/624027_1_En_BookFrontmatter_Figa_HTML.png)

Edson OliveiraJr

State University of Maringá, Maringá, Brazil

Thiago J. Silva

AmbevTech, Maringá, Brazil

Charles V. Neu

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

Avelino F. Zorzo

PUCRS, Porto Alegre, Brazil

Ana H. Mazur

State University of Maringá, Maringá, Brazil

ISBN 978-3-032-19950-8
e-ISBN 978-3-032-19951-5

<https://doi.org/10.1007/978-3-032-19951-5>

© The Editor(s) (if applicable) and The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

This work is subject to copyright. All rights are solely and exclusively licensed by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Switzerland AG

The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

*To my not-so-little bear,* ***Beatriz,*** *whose laughter fills my heart and gives meaning to every page.*

***Daddy Edson Jr.***

# Foreword

Trust is the bedrock of forensic science, and trust is earned through reproducibility. In legal, corporate, and policy settings alike, digital evidence carries weight only when others can verify that the findings are repeatable, well-founded, and transparent. Over the past decades, digital forensics has become integral to everything from incident response to criminal prosecution. Yet the field still grapples with a fundamental scientific challenge: how to elevate a practice often driven by proprietary tools and case-by-case improvisation into one grounded in controlled, rigorous experimentation. This book, *Controlled Experimentation of Digital Forensics: Towards Formalization for Strengthening Evidence Reproducibility, Reliability, and Transparency*, directly addresses that challenge.

The authors argue persuasively that in digital forensics, methodology matters as much as technology. They reposition forensic investigations within the framework of empirical science, where one plans carefully, controls variables, makes procedures explicit, analyzes data with statistical rigor, and reports results for independent verification. In doing so, the book provides a path to transition from anecdotal “one-off” findings to results that anyone can reproduce. This shift is more than academic; it is what transforms a subjective expert opinion into an objective scientific finding that can withstand scrutiny and be replicated by others.

The book’s five-part structure reinforces this theme. Part I—Fundamentals of Digital Forensics and Controlled Experimentation—situates digital forensics within its historical, technical, and scientific context. It revisits the investigative process and the field’s main and emerging branches, while also introducing the broader landscape of empirical methods drawn from computer science and software engineering. By treating controlled experimentation and reproducibility as core pillars, Part I connects digital forensics to ongoing discussions about evidence-based practice and the wider Open Science movement, emphasizing that rigorous design, transparent documentation, and repeatable procedures are prerequisites for credible forensic knowledge.

Part II—Conceptual Modeling of Digital Forensics Controlled Experiments—introduces a unifying solution to these needs. It first surveys the role and history of conceptual modeling as a means to structure and clarify complex domains, and then presents ExperDF-CM (Experimentation in Digital Forensics—Conceptual Model), a comprehensive model for designing and conducting controlled experiments in digital forensics. ExperDF-CM breaks an experiment into five defined phases—Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination—mirroring the entire research lifecycle from hypothesis to published result. Each phase is detailed with its objectives, inputs, and outputs, giving practitioners and researchers a common vocabulary and structure for experimentation. For example, the Planning phase involves formulating research questions, hypotheses, and variables, and considering ethical and legal constraints, while the Operation phase focuses on data collection under controlled conditions. The Dissemination phase ensures that data sets, code, and results are openly shared for verification. This model doesn’t remain theoretical: the book demonstrates how to apply ExperDF-CM step by step, including support for modern practices such as Registered Reports and the preparation of ethics and approval documentation. In short, Part II delivers an actionable blueprint that any lab or researcher can adopt immediately to enhance the scientific rigor of their forensic experiments.

Part III—Formal Representation and Semantic Integration of Digital Forensics Controlled Experiments—extends the discussion into the realm of knowledge representation, interoperability, and machine reasoning. It begins with an accessible primer on ontology design and SPARQL querying, and introduces the ExperDF-Portal as a digital environment for managing and querying experimental information. Building on this foundation, the authors present ExperDF-Onto, an ontology that formalizes the key entities and relationships of a digital forensics experiment (cases, artifacts, tools, procedures, results, and more) using established standards such as RDF/OWL for specification and SPARQL for querying. ExperDF-Onto is aligned with metadata and provenance standards, including Dublin Core and the PROV family, to capture how evidence and results are generated and transformed. By encoding experiment details semantically, the book enables machines (and researchers) to interpret and reuse experimental data in ways that were previously impossible. Concrete SPARQL queries are provided for each phase of ExperDF-CM—for instance, retrieving all experiments that used a certain tool or checking whether all required steps of an analysis were documented. This semantic layer makes experiments discoverable, comparable, and interoperable, enabling them to be combined into a growing, machine-readable body of forensic knowledge rather than remaining isolated narratives.

Part IV—ExperDF-Onto Walkthroughs of Exemplary Digital Forensics Experiments—moves from theory to practice. Through a set of carefully chosen case studies, it shows how ExperDF-CM and ExperDF-Onto can be instantiated to model real-world forensic experiments end-to-end. These walkthroughs span diverse scenarios, including memory acquisition, smartphone extraction and lock bypass, cloud log tampering, IoT intrusion detection, and blockchain-based provenance. Each example traces the five phases of ExperDF-CM, illustrates how variables and procedures are represented semantically, and demonstrates how SPARQL queries can be used to verify coverage, check provenance, and support teaching. The inclusion of “minimal reproducibility kits,” coverage analyses, and teaching notes in these examples underscores the authors’ commitment to making the frameworks not only conceptually sound but also concretely usable in research, education, and practice.

Finally, Part V—Integration, Reflection, and Future Directions—synthesizes the previous parts and articulates a vision for the discipline’s future. It describes a path toward a more scientifically grounded, transparent, and collaborative digital forensics. Crucially, it emphasizes that emerging realities make this shift imperative. Today’s investigators contend with phenomena like cloud services spreading data across jurisdictions and multi-tenant infrastructures, IoT ecosystems where evidence is fragmented across device firmware, mobile apps, gateways, and cloud back-ends, fileless malware that resides only in volatile memory, encrypted communication channels that thwart traditional analysis, and AI- and machine-learning-driven systems that introduce new forms of evidence while obscuring decision processes. The concluding discussion argues that only by embracing formalized experimentation, semantic consistency, and open sharing of results will digital forensics keep pace with these challenges. The authors stop short of utopian predictions, but they clearly make the case that the methodologies presented—controlled experimentation via ExperDF-CM and knowledge integration via ExperDF-Onto and its supporting portal—can raise both the floor and the ceiling of forensic science practice. Higher minimum standards of evidence validity and reproducibility will increase confidence in everyday investigations, while richer datasets and interoperable tools will open new frontiers of research and capability.

The value of this work is broad. For researchers, it provides a clear framework for designing robust experiments and a means to disseminate results so others can query and extend them. Adopting ExperDF-CM, ExperDF-Onto, and the associated tooling could significantly improve the comparability of studies in academic digital forensics, making it easier to build on each other’s work rather than reinventing setups. For practitioners and forensic tool developers, the controlled experimentation approach provides a means to empirically evaluate and verify tools, procedures, and analytical techniques across various conditions. Using these methods, one can quantify the accuracy and error rates of forensic tools, establish statistical confidence in their results, and maintain detailed provenance for how conclusions were reached—all of which strengthen the evidentiary value and defensibility of digital forensic findings. For educators and training programs, the content in this book can modernize curricula. Students can be taught to follow the ExperDF-CM phases in classroom labs and document their projects in ExperDF-Onto (and through the portal), ingraining in them a mindset of scientific rigor, reproducibility, and semantic precision from the start. This could help cultivate the next generation of forensic professionals who are as comfortable designing an experiment or writing a SPARQL query as they are collecting a disk image.

Beyond its immediate practicality, this volume advances a subtle but essential cultural shift in digital forensics. It shows that being more open, systematic, and precise in our methods need not slow us down—in fact, it can make our work more efficient and impactful. It demonstrates that we can achieve semantic clarity (through formal models, ontologies, and machine-actionable representations) without sacrificing hands-on problem solving. Perhaps most importantly, it reinforces the idea that digital forensics can evolve into a truly cumulative science: one in which results accumulate, interconnect, and drive the field forward, rather than dissipate into isolated case reports. In that sense, this book is not just a compilation of knowledge, but an invitation and a roadmap to improve our collective practice. It is an invitation to design investigations with greater intent, to rigorously measure and evaluate our forensic techniques, and to share our findings in a structured way so that others can build upon them openly.

I congratulate the authors for devising and delivering this much-needed framework for the community. Controlled Experimentation of Digital Forensics is both a call to action and a tangible toolkit. Taken to heart, the approaches in this book could dramatically enhance the credibility and scientific maturity of digital forensic investigations. The payoff will likely be seen not only in stronger research publications but also in everyday practice: more reliable tools, more consistent procedures, and ultimately more trustworthy justice when digital evidence is at play.

Ali Dehghantanha

Professor & Canada Research Chair in, Cybersecurity & Threat Intelligence, University of Guelph, Guelph, ON, Canada

December 2025

# Preface

## What Is This Book About?

This book represents the culmination of years of collaborative research, reflection, and shared vision between two leading Brazilian research groups in Digital Forensics: the **Computer Science Investigation in Digital Forensics (CSI-DIN)** and the **Research Group on Systematic Software Reuse and Continuous Experimentation (GReater)** at the State University of Maringá (UEM), coordinated by Prof. Edson OliveiraJr, and the **Dependable and Secure Systems Group (CONSEG)** at the Pontifical Catholic University of Rio Grande do Sul (PUCRS), led by Prof. Avelino F. Zorzo. This partnership was nurtured within the framework of the Brazilian National Institute of Science and Technology on Forensic Sciences (INCT-CF), which has played a pivotal role in promoting interdisciplinary collaboration and advancing scientific approaches to the analysis of digital evidence.

The book provides a comprehensive reflection on the scientific foundations of **Evidence-based Digital Forensics** as an emerging discipline. It goes beyond the practice-oriented roots of Digital Forensics to present a mature field grounded in reproducible, systematic, and transparent research methods. Its title, *Controlled Experimentation of Digital Forensics: Towards Formalization for Strengthening Evidence Reproducibility, Reliability, and Transparency*, encapsulates this ambition, emphasizing both the need to formalize experimental processes and the commitment to foster openness and rigor in forensic science.

Through conceptual models (*ExperDF-CM*) and semantic frameworks (*ExperDF-Onto*), the book proposes practical mechanisms for structuring, documenting, and validating experiments in Digital Forensics. It ultimately situates the discipline within the broader movement of Open Science, aligning its principles with the UNESCO Recommendation on Open Science and the pursuit of socially responsible research.

## Who Should Read This Book?

This book is written for a broad and interdisciplinary audience that includes not only researchers and professionals in Digital Forensics but also those interested in the foundations of scientific inquiry, empirical research, and Open Science. Its contents are designed to support both academic reflection and practical application, bridging the gap between theoretical principles and operational challenges.

For **researchers**, the book offers a solid methodological and conceptual foundation for designing, conducting, and publishing controlled experiments in a reproducible and transparent manner. It provides models, ontologies, and semantic structures that formalize experimental reasoning and ensure that results can be independently verified, compared, and reused. Researchers will find in it a roadmap for producing cumulative and interoperable scientific knowledge in a field that increasingly depends on collaboration and data integration.

For **practitioners**, the book serves as a practical guide to improving the reliability, traceability, and defensibility of forensic analyses. It presents conceptual models and documentation standards that allow experts to structure their investigations systematically, making their findings more robust in both scientific and judicial contexts. The emphasis on reproducibility and transparency helps practitioners align their technical work with the growing expectations of accountability and quality assurance in forensic science.

For **educators**, it functions as a didactic resource for introducing students to the principles of experimental design, empirical reasoning, and scientific openness. The conceptual and ontological models presented here can be used to teach how evidence, hypotheses, and experimental variables interrelate, helping learners develop a critical understanding of scientific rigor in Digital Forensics. In this sense, the book supports both curricular innovation and the training of future professionals capable of integrating ethical awareness with methodological discipline.

For **policymakers** and **funding agencies**, it provides conceptual grounding for establishing evaluation criteria, standards, and incentives that promote transparency, reliability, and trust in Digital Forensics research. By translating the principles of Open Science into concrete methodological and semantic instruments, the book offers a foundation for shaping policies that encourage reproducibility, data sharing, and responsible research practices.

Beyond academic and professional communities, this work also speaks to a wider audience concerned with the integrity of digital evidence and its role in safeguarding citizens’ rights. As societies become increasingly digitalized, the credibility of forensic evidence directly influences public trust in institutions, judicial decisions, and democratic governance. By reinforcing the evidential foundation of Digital Forensics, this book contributes to building a more accountable, transparent, and equitable justice system in which scientific rigor serves both truth and society.

## How Is This Book Organized?

The organization of this book follows a logical progression that moves from theoretical foundations to applied instantiation and reflection, guiding the reader through the conceptual, semantic, and empirical dimensions of controlled experimentation in Digital Forensics. Each part builds upon the previous one, creating an integrated framework that combines scientific rigor, methodological clarity, and open science principles.

**Part** [**I**](https://doi.org/10.1007/978-3-032-19951-5_0)**—Fundamentals of Digital Forensics and Controlled Experimentation** establishes the theoretical and methodological underpinnings of the field. It positions Digital Forensics within a broader scientific tradition, emphasizing rigor, transparency, and reproducibility as essential for producing credible, cumulative knowledge. The three chapters in this part discuss (1) conceptual modeling as a means of structuring and clarifying knowledge, (2) the design and execution of controlled experiments as a methodological foundation for empirical validation, and (3) reproducibility as a central pillar for credibility and trust in forensic research.

**Part** [**II**](624027_1_En_3_Chapter.xhtml)**—Conceptual Modeling of Digital Forensics Controlled Experiments** introduces the *ExperDF-CM* conceptual model as a structured framework for documenting, executing, and disseminating forensic experiments. It begins with a historical and methodological overview of conceptual modeling, tracing its evolution from early data models to domain-specific scientific representations. Building upon this foundation, it presents *ExperDF-CM* as a comprehensive model organized into five interconnected phases: Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination. This structure supports methodological consistency, transparency, and ethical accountability across the experimental lifecycle.

**Part** [**III**](624027_1_En_5_Chapter.xhtml)**—Formal Representation and Semantic Integration of Digital Forensics Controlled Experiments** extends the conceptual foundations into the semantic domain. It focuses on ontological modeling, interoperability, and machine reasoning as mechanisms to make experimental knowledge explicit, traceable, and reusable. The first chapter introduces key concepts of semantic representation, SPARQL querying, and the *ExperDF-Portal*, a digital environment for experiment management. The following chapter presents *ExperDF-Onto*, an ontology aligned with international standards such as Dublin Core and the PROV family, which enables semantic annotation and provenance tracking of forensic research data. Together, these elements transform static documentation into a dynamic knowledge ecosystem.

**Part** [**IV**](624027_1_En_7_Chapter.xhtml)**—ExperDF-Onto Walkthroughs of Exemplary Digital Forensics Experiments** transitions from theory to practice. It demonstrates how *ExperDF-Onto* can be instantiated to represent real-world forensic experiments in a consistent and machine-actionable manner. Through five detailed walkthroughs, this part shows how conceptual and semantic frameworks capture experimental intent, variable control, provenance, and reproducibility. The case studies include memory acquisition, smartphone extraction, cloud log analysis, IoT intrusion detection, and blockchain-based provenance. Each follows the five phases of *ExperDF-CM*, illustrating the ontology’s role as a bridge between narrative design and formal documentation, and as a tool for teaching, validation, and ethical reflection.

**Part** [**V**](624027_1_En_12_Chapter.xhtml)**—Integration, Reflection, and Future Directions** concludes the book by synthesizing its theoretical, semantic, and practical contributions. It integrates the insights from the previous parts to present a coherent vision of Digital Forensics as a rigorous, transparent, and open scientific discipline. This final part discusses how conceptual models and ontologies together form a foundation for cumulative knowledge and reproducible research. It also reflects on remaining challenges, technical, institutional, and philosophical, and outlines future directions for research, education, and policy. In doing so, it reinforces the book’s central message: the strength of Digital Forensics lies in its capacity to combine structure, meaning, and openness to build reliable, verifiable scientific evidence.

Taken together, these five parts guide the reader through a complete journey, from understanding the philosophical bases of experimentation to applying semantic frameworks for open and reproducible forensic science. The book thus serves both as a reference for researchers and as a didactic resource for practitioners, educators, and policymakers seeking to strengthen the scientific foundations of Digital Forensics.

## How Did This Book Start?

The origins of this book trace back to an 18-month sabbatical period undertaken by Edson OliveiraJr between 2018 and 2020 at the Pontifical Catholic University of Rio Grande do Sul (PUCRS), under the supervision of Prof. Avelino F. Zorzo in the Dependable and Secure Systems Group (CONSEG), within the context of the **Brazilian National Institute of Science and Technology on Forensic Sciences (INCT-CF)**. The initial goal of this research stay was to gain a deeper understanding of how controlled experiments were being conducted in Digital Forensics and to explore how empirical methodologies from Software Engineering could be adapted to this context. However, during this period, it became evident that the area lacked scientific rigor, transparency, and reproducibility. This realization became the turning point that motivated a systematic effort to establish a structured, evidence-based, and open approach to Digital Forensics experimentation.

From that experience, the idea of building a conceptual and semantic foundation for forensic experimentation emerged. What began as an exploratory academic exchange evolved into a coordinated research program involving multiple Brazilian institutions and international collaborations, dedicated to redefining the methodological foundations of Digital Forensics.

The project was further strengthened through the broader **INCT-CF initiative (CAPES, CNPq, and FAPERGS/Brazil)**, which united researchers from computing, law, biology, and chemistry to promote interdisciplinary approaches to forensic science. This collaborative environment provided the institutional and intellectual context necessary for transforming isolated insights into a comprehensive research framework.

The realization of this book was made possible by the institutional support of **UEM**, **PUCRS**, and **UNISC**, and by the generous funding from **CNPq**, **CAPES**, and the **Araucária Funding Agency of Paraná**, as well as the collaborative environment fostered by **NAPI - Public Security and Forensic Science**. We are also profoundly grateful to our colleagues, students, and collaborators whose ideas, software implementations, and constructive feedback enriched and refined every stage of this work.

Finally, we dedicate this work to the global Digital Forensics community, whose shared pursuit of truth and scientific rigor continues to shape a more transparent, reproducible, and equitable digital future.

Edson OliveiraJr

Thiago J. Silva

Charles V. Neu

Avelino F. Zorzo

Ana H. Mazur

Maringá, PR, Brazil
Maringá, Brazil
Santa Cruz, Brazil
Porto Alegre, Brazil
Maringá, Brazil

December 2025

# Acknowledgments

The development of this book was made possible through the support, collaboration, and dedication of countless individuals and institutions who accompanied us throughout this long scientific journey.

We gratefully acknowledge the essential role of the **Brazilian funding agencies**, whose investments created the conditions for sustained high-quality research. In particular, we thank the **National Council for Scientific and Technological Development (CNPq)**, the **Coordination for the Improvement of Higher Education Personnel (CAPES)**, and the **Araucária Foundation of Paraná**. Their programs and initiatives, especially those linked to the INCT-CF and NAPI Public Security and Forensic Science, provided the financial, organizational, and intellectual environment that enabled the conceptual, methodological, and technological advances consolidated in this work.

Our most profound appreciation goes to the **State University of Maringá (UEM)**, the **Pontifical Catholic University of Rio Grande do Sul (PUCRS)**, and the **University of Santa Cruz do Sul (UNISC)**, whose institutional support sustained the research activities, collaborations, and mobility efforts that shaped the foundations of this book. We also thank our colleagues from the **CSI-DIN, GReater, and CONSEG research groups**, whose shared commitment to rigor, openness, and interdisciplinarity enriched every stage of this project.

We extend our sincere gratitude to our **graduate and undergraduate students**, whose enthusiasm, creativity, and tireless curiosity were central to the evolution of the ExperDF-CM model, the ExperDF-Onto ontology, and the numerous prototypes, datasets, and experimental artifacts produced over the years. Their participation in research meetings, empirical studies, conceptual modeling exercises, and software development efforts not only strengthened the technical content of this book but also reaffirmed our belief in the transformative power of collaborative scientific training.

We are also grateful to the colleagues who generously contributed to refining specific chapters through detailed technical reviews and insightful comments. In particular, **we thank Prof. Dr. Alexandre L’Erario of the Federal University of Technology of Paraná (UTFPR), Prof. Dr. Vítor E. Silva Souza of the Federal University of Espírito Santo (UFES), and Prof. Dr. Marcelo Morandini of the University of São Paulo (USP)**. Their careful reading, constructive suggestions, and expert perspective enhanced the clarity, precision, and scholarly quality of this work.

Finally, **we express our deep appreciation to our families**. Their patience, encouragement, and unwavering support sustained us during demanding research cycles, long writing periods, and countless moments of intellectual immersion. This book is as much a result of their generosity as it is of our academic dedication. Their presence remains the silent foundation that made this journey possible.

To all of you, institutions, colleagues, students, collaborators, and loved ones, we offer our deepest thanks. This book is a collective achievement built upon shared effort, trust, and the conviction that science advances when it is open, rigorous, and grounded in collaboration.

Competing Interests

The authors have no competing interests to declare that are relevant to the content of this manuscript.

# Contents

1. Part I Fundamentals of Digital Forensics and Controlled Experimentation
   1
   1. [1 Digital Forensics in a Nutshell](624027_1_En_1_Chapter.xhtml)
      3
      1. [1.​1 History of Digital Forensics](624027_1_En_1_Chapter.xhtml#Sec1)
         4
      1. [1.​2 The Digital Forensics Investigative Process](624027_1_En_1_Chapter.xhtml#Sec2)
         5
      1. [1.​3 Digital Forensics Main Branches](624027_1_En_1_Chapter.xhtml#Sec3)
         7
         1. [1.​3.​1 Computer Forensics](624027_1_En_1_Chapter.xhtml#Sec4)
            9
         1. [1.​3.​2 Network Forensics](624027_1_En_1_Chapter.xhtml#Sec5)
            10
         1. [1.​3.​3 Mobile Device Forensics](624027_1_En_1_Chapter.xhtml#Sec6)
            11
         1. [1.​3.​4 Cloud Forensics](624027_1_En_1_Chapter.xhtml#Sec7)
            12
         1. [1.​3.​5 Internet of Things (IoT) Forensics](624027_1_En_1_Chapter.xhtml#Sec8)
            12
         1. [1.​3.​6 Memory Forensics](624027_1_En_1_Chapter.xhtml#Sec9)
            13
         1. [1.​3.​7 Database Forensics](624027_1_En_1_Chapter.xhtml#Sec10)
            14
      1. [1.​4 Emerging Specialized Branches](624027_1_En_1_Chapter.xhtml#Sec11)
         14
         1. [1.​4.​1 Blockchain Forensics](624027_1_En_1_Chapter.xhtml#Sec12)
            15
         1. [1.​4.​2 Automotive Forensics](624027_1_En_1_Chapter.xhtml#Sec13)
            15
         1. [1.​4.​3 ICS and SCADA Forensics](624027_1_En_1_Chapter.xhtml#Sec14)
            16
         1. [1.​4.​4 Live Forensics](624027_1_En_1_Chapter.xhtml#Sec15)
            16
         1. [1.​4.​5 Integrative Perspective](624027_1_En_1_Chapter.xhtml#Sec16)
            17
      1. [1.​5 Perspectives on Digital Forensics](624027_1_En_1_Chapter.xhtml#Sec17)
         18
      1. [1.​6 Final Remarks](624027_1_En_1_Chapter.xhtml#Sec18)
         20
      1. [References](624027_1_En_1_Chapter.xhtml#Bib1)
         22
   1. [2 Principles of Controlled Experimentation](624027_1_En_2_Chapter.xhtml)
      25
      1. [2.​1 Empirical Studies in Computer Science](624027_1_En_2_Chapter.xhtml#Sec1)
         25
         1. [2.​1.​1 Controlled Experiments](624027_1_En_2_Chapter.xhtml#Sec2)
            26
         1. [2.​1.​2 Field Experiments and Quasi-experiments](624027_1_En_2_Chapter.xhtml#Sec3)
            27
         1. [2.​1.​3 Case Studies](624027_1_En_2_Chapter.xhtml#Sec4)
            28
         1. [2.​1.​4 Surveys and Interviews](624027_1_En_2_Chapter.xhtml#Sec5)
            28
         1. [2.​1.​5 Systematic Literature Reviews and Meta-analyses](624027_1_En_2_Chapter.xhtml#Sec6)
            30
         1. [2.​1.​6 Benchmarking and Performance Evaluations](624027_1_En_2_Chapter.xhtml#Sec7)
            30
         1. [2.​1.​7 Ethnographies and Experience Sampling](624027_1_En_2_Chapter.xhtml#Sec8)
            31
      1. [2.​2 Controlled Experimentation in a Nutshell](624027_1_En_2_Chapter.xhtml#Sec9)
         32
         1. [2.​2.​1 Types of Controlled Experiments](624027_1_En_2_Chapter.xhtml#Sec10)
            32
         1. [2.​2.​2 Planning a Controlled Experiment](624027_1_En_2_Chapter.xhtml#Sec11)
            33
         1. [2.​2.​3 Conducting a Controlled Experiment](624027_1_En_2_Chapter.xhtml#Sec12)
            35
         1. [2.​2.​4 Analyzing and Interpreting Results of a Controlled Experiment](624027_1_En_2_Chapter.xhtml#Sec13)
            37
         1. [2.​2.​5 Reporting a Controlled Experiment](624027_1_En_2_Chapter.xhtml#Sec14)
            44
      1. [2.​3 The Lack of Rigorousness in Digital Forensics Controlled Experiments](624027_1_En_2_Chapter.xhtml#Sec15)
         45
      1. [2.​4 Final Remarks](624027_1_En_2_Chapter.xhtml#Sec16)
         49
      1. [References](624027_1_En_2_Chapter.xhtml#Bib1)
         50
   1. [3 The Role of Reproducibility in Science and Digital Forensics](624027_1_En_3_Chapter.xhtml)
      53
      1. [3.​1 The Concept of Reproducibility in Science](624027_1_En_3_Chapter.xhtml#Sec1)
         53
         1. [3.​1.​1 Reproducibility, Repeatability, and Replicability](624027_1_En_3_Chapter.xhtml#Sec2)
            54
         1. [3.​1.​2 Dimensions of Reproducibility](624027_1_En_3_Chapter.xhtml#Sec3)
            55
         1. [3.​1.​3 Reproducibility in Digital Forensics](624027_1_En_3_Chapter.xhtml#Sec4)
            56
      1. [3.​2 Open Science and Open Reproducible Research](624027_1_En_3_Chapter.xhtml#Sec5)
         57
      1. [3.​3 Worldwide Reproducibility Initiatives](624027_1_En_3_Chapter.xhtml#Sec6)
         59
         1. [3.​3.​1 Springer Nature Open Science Initiatives](624027_1_En_3_Chapter.xhtml#Sec7)
            60
         1. [3.​3.​2 The IEEE Access Reproducibility Initiative](624027_1_En_3_Chapter.xhtml#Sec8)
            61
         1. [3.​3.​3 Brazilian Reproducibility Initiatives](624027_1_En_3_Chapter.xhtml#Sec9)
            61
         1. [3.​3.​4 The UK Reproducibility Network (UKRN)](624027_1_En_3_Chapter.xhtml#Sec12)
            63
         1. [3.​3.​5 The AI4Europe Reproducibility Initiative](624027_1_En_3_Chapter.xhtml#Sec13)
            63
      1. [3.​4 Reproducibility Issues in Digital Forensics](624027_1_En_3_Chapter.xhtml#Sec14)
         64
         1. [3.​4.​1 Complexity of Experiments](624027_1_En_3_Chapter.xhtml#Sec15)
            64
         1. [3.​4.​2 IoT and the Complexity of Digital Systems and Devices](624027_1_En_3_Chapter.xhtml#Sec16)
            65
         1. [3.​4.​3 Artificial Intelligence (AI)](624027_1_En_3_Chapter.xhtml#Sec17)
            65
         1. [3.​4.​4 Big Data](624027_1_En_3_Chapter.xhtml#Sec18)
            66
         1. [3.​4.​5 Cloud Computing](624027_1_En_3_Chapter.xhtml#Sec19)
            67
         1. [3.​4.​6 Data Volatility and Dynamic Environments](624027_1_En_3_Chapter.xhtml#Sec20)
            67
         1. [3.​4.​7 Anti-forensic Techniques and Cryptography](624027_1_En_3_Chapter.xhtml#Sec21)
            67
         1. [3.​4.​8 Shortage of Specialized Digital Forensics Professionals](624027_1_En_3_Chapter.xhtml#Sec22)
            68
         1. [3.​4.​9 Discussion](624027_1_En_3_Chapter.xhtml#Sec23)
            68
      1. [3.​5 Open Science-Driven Digital Forensics Experimentation](624027_1_En_3_Chapter.xhtml#Sec24)
         68
      1. [3.​6 Final Remarks](624027_1_En_3_Chapter.xhtml#Sec25)
         72
      1. [References](624027_1_En_3_Chapter.xhtml#Bib1)
         72

1. Part II Conceptual Modeling of Digital Forensics Controlled Experiments
   75
   1. [4 Basics of Conceptual Modeling](624027_1_En_4_Chapter.xhtml)
      77
      1. [4.​1 Conceptual Modeling](624027_1_En_4_Chapter.xhtml#Sec1)
         78
      1. [4.​2 Historical Development and Methodological Aspects](624027_1_En_4_Chapter.xhtml#Sec2)
         78
      1. [4.​3 Evaluation, Types, Applications, and Interdisciplinar​y Perspectives](624027_1_En_4_Chapter.xhtml#Sec3)
         80
      1. [4.​4 Tool Support for Conceptual Modeling](624027_1_En_4_Chapter.xhtml#Sec4)
         82
      1. [4.​5 The Role of Conceptual Modeling in Digital Forensics](624027_1_En_4_Chapter.xhtml#Sec5)
         82
      1. [4.​6 Final Remarks](624027_1_En_4_Chapter.xhtml#Sec6)
         83
      1. [References](624027_1_En_4_Chapter.xhtml#Bib1)
         85
   1. [5 ExperDF-CM:​ A Digital Forensics Controlled Experiments Conceptual Model](624027_1_En_5_Chapter.xhtml)
      87
      1. [5.​1 The ExperDF-CM Conceptual Model](624027_1_En_5_Chapter.xhtml#Sec1)
         88
         1. [5.​1.​1 The Planning Concept](624027_1_En_5_Chapter.xhtml#Sec2)
            88
         1. [5.​1.​2 The Pre-Operation Concept](624027_1_En_5_Chapter.xhtml#Sec3)
            90
         1. [5.​1.​3 The Operation Concept](624027_1_En_5_Chapter.xhtml#Sec4)
            91
         1. [5.​1.​4 The Analysis and Interpretation Concept](624027_1_En_5_Chapter.xhtml#Sec5)
            93
         1. [5.​1.​5 The Dissemination Concept](624027_1_En_5_Chapter.xhtml#Sec6)
            94
      1. [5.​2 Applying the ExperDF-CM to Model Digital Forensics Controlled Experiments](624027_1_En_5_Chapter.xhtml#Sec7)
         95
         1. [5.​2.​1 Step-by-Step Modeling with ExperDF-CM](624027_1_En_5_Chapter.xhtml#Sec8)
            95
         1. [5.​2.​2 Illustrative Roadmap](624027_1_En_5_Chapter.xhtml#Sec9)
            95
         1. [5.​2.​3 ExperDF-CM Support for Registered Reports and Ethical Approval Preparation](624027_1_En_5_Chapter.xhtml#Sec10)
            96
      1. [5.​3 Final Remarks](624027_1_En_5_Chapter.xhtml#Sec11)
         97
      1. [Reference](624027_1_En_5_Chapter.xhtml#Bib1)
         98

1. Part III Formal Representation and Semantic Integration of Digital Forensics Controlled Experiments
   99
   1. [6 Basics of Ontology and SPARQL Queries](624027_1_En_6_Chapter.xhtml)
      101
      1. [6.​1 Conceptual Foundations of Ontologies](624027_1_En_6_Chapter.xhtml#Sec1)
         102
         1. [6.​1.​1 Philosophical Foundations and the Evolution of Ontologies into Computing](624027_1_En_6_Chapter.xhtml#Sec2)
            104
         1. [6.​1.​2 Definition, Characteristics, Typology, and Applications of Ontologies](624027_1_En_6_Chapter.xhtml#Sec3)
            105
         1. [6.​1.​3 Specifying Ontologies with OWL and RDF](624027_1_En_6_Chapter.xhtml#Sec4)
            106
      1. [6.​2 The Role of Ontologies in Digital Forensics](624027_1_En_6_Chapter.xhtml#Sec7)
         112
      1. [6.​3 Introduction to SPARQL](624027_1_En_6_Chapter.xhtml#Sec8)
         114
         1. [6.​3.​1 Historical Motivation](624027_1_En_6_Chapter.xhtml#Sec9)
            114
         1. [6.​3.​2 Core Characteristics of RDF and SPARQL](624027_1_En_6_Chapter.xhtml#Sec10)
            115
         1. [6.​3.​3 SPARQL Syntax](624027_1_En_6_Chapter.xhtml#Sec11)
            116
         1. [6.​3.​4 Tools for Writing and Executing SPARQL Queries](624027_1_En_6_Chapter.xhtml#Sec12)
            117
      1. [6.​4 Final Remarks](624027_1_En_6_Chapter.xhtml#Sec22)
         122
      1. [References](624027_1_En_6_Chapter.xhtml#Bib1)
         124
   1. [7 The ExperDF-Onto Ontology](624027_1_En_7_Chapter.xhtml)
      127
      1. [7.​1 The ExperDF-Onto Ontology](624027_1_En_7_Chapter.xhtml#Sec1)
         127
         1. [7.​1.​1 ExperDF-Onto Methodology and Design](624027_1_En_7_Chapter.xhtml#Sec2)
            129
         1. [7.​1.​2 ExperDF-Onto Elements](624027_1_En_7_Chapter.xhtml#Sec3)
            130
      1. [7.​2 Writing and Executing SPARQL Queries in ExperDF-Onto](624027_1_En_7_Chapter.xhtml#Sec9)
         140
         1. [7.​2.​1 Identifying Top-Level Classes](624027_1_En_7_Chapter.xhtml#Sec10)
            141
         1. [7.​2.​2 Planning Phase Queries](624027_1_En_7_Chapter.xhtml#Sec11)
            141
         1. [7.​2.​3 Pre-Operation Phase Queries](624027_1_En_7_Chapter.xhtml#Sec15)
            144
         1. [7.​2.​4 Operation Phase Queries](624027_1_En_7_Chapter.xhtml#Sec18)
            145
         1. [7.​2.​5 Analysis and Interpretation Phase Queries](624027_1_En_7_Chapter.xhtml#Sec21)
            146
         1. [7.​2.​6 Dissemination Phase Queries](624027_1_En_7_Chapter.xhtml#Sec24)
            148
      1. [7.​3 Final Remarks](624027_1_En_7_Chapter.xhtml#Sec27)
         149
      1. [References](624027_1_En_7_Chapter.xhtml#Bib1)
         150

1. Part IV ExperDF-Onto Walkthroughs of Exemplary Digital Forensics Experiments
   151
   1. [8 Example 1:​ The Memory That Would Not Lie](624027_1_En_8_Chapter.xhtml)
      155
      1. [8.​1 Context and Motivation](624027_1_En_8_Chapter.xhtml#Sec1)
         156
      1. [8.​2 Planning Phase](624027_1_En_8_Chapter.xhtml#Sec2)
         156
      1. [8.​3 Pre-Operation Phase](624027_1_En_8_Chapter.xhtml#Sec3)
         157
      1. [8.​4 Operation Phase](624027_1_En_8_Chapter.xhtml#Sec4)
         158
      1. [8.​5 Analysis and Interpretation Phase](624027_1_En_8_Chapter.xhtml#Sec5)
         158
      1. [8.​6 Dissemination Phase](624027_1_En_8_Chapter.xhtml#Sec6)
         159
      1. [8.​7 Ontological Instantiation Snapshot](624027_1_En_8_Chapter.xhtml#Sec7)
         160
      1. [8.​8 Querying the Instantiation](624027_1_En_8_Chapter.xhtml#Sec8)
         160
      1. [8.​9 Coverage and Missing Elements](624027_1_En_8_Chapter.xhtml#Sec9)
         161
      1. [8.​10 Interpretation and Teaching Notes](624027_1_En_8_Chapter.xhtml#Sec10)
         162
         1. [8.​10.​1 What the Results Mean](624027_1_En_8_Chapter.xhtml#Sec11)
            162
         1. [8.​10.​2 How to Reuse This Study](624027_1_En_8_Chapter.xhtml#Sec12)
            162
         1. [8.​10.​3 Common Misconceptions Clarified](624027_1_En_8_Chapter.xhtml#Sec13)
            162
         1. [8.​10.​4 Minimal Reproducibility Kit](624027_1_En_8_Chapter.xhtml#Sec14)
            163
      1. [8.​11 Final Remarks](624027_1_En_8_Chapter.xhtml#Sec15)
         163
   1. [9 Example 2:​ Unlocking the Locked—Smartphone Bypass Experiments](624027_1_En_9_Chapter.xhtml)
      165
      1. [9.​1 Context and Motivation](624027_1_En_9_Chapter.xhtml#Sec1)
         166
      1. [9.​2 Planning Phase](624027_1_En_9_Chapter.xhtml#Sec2)
         166
      1. [9.​3 Pre-Operation Phase](624027_1_En_9_Chapter.xhtml#Sec3)
         167
      1. [9.​4 Operation Phase](624027_1_En_9_Chapter.xhtml#Sec4)
         168
      1. [9.​5 Analysis and Interpretation Phase](624027_1_En_9_Chapter.xhtml#Sec5)
         169
      1. [9.​6 Dissemination Phase](624027_1_En_9_Chapter.xhtml#Sec6)
         169
      1. [9.​7 Ontological Instantiation Snapshot](624027_1_En_9_Chapter.xhtml#Sec7)
         170
      1. [9.​8 Querying the Instantiation](624027_1_En_9_Chapter.xhtml#Sec8)
         170
      1. [9.​9 Coverage and Missing Elements](624027_1_En_9_Chapter.xhtml#Sec9)
         172
      1. [9.​10 Interpretation and Teaching Notes](624027_1_En_9_Chapter.xhtml#Sec10)
         172
         1. [9.​10.​1 What the Results Mean](624027_1_En_9_Chapter.xhtml#Sec11)
            173
         1. [9.​10.​2 How to Reuse This Study](624027_1_En_9_Chapter.xhtml#Sec12)
            173
         1. [9.​10.​3 Common Misconceptions Clarified](624027_1_En_9_Chapter.xhtml#Sec13)
            173
         1. [9.​10.​4 Minimal Reproducibility Kit](624027_1_En_9_Chapter.xhtml#Sec14)
            173
      1. [9.​11 Final Remarks](624027_1_En_9_Chapter.xhtml#Sec15)
         174
   1. [10 Example 3:​ The Case of the Altered Cloud Logs](624027_1_En_10_Chapter.xhtml)
      175
      1. [10.​1 Context and Motivation](624027_1_En_10_Chapter.xhtml#Sec1)
         176
      1. [10.​2 Planning Phase](624027_1_En_10_Chapter.xhtml#Sec2)
         176
      1. [10.​3 Pre-Operation Phase](624027_1_En_10_Chapter.xhtml#Sec3)
         177
      1. [10.​4 Operation Phase](624027_1_En_10_Chapter.xhtml#Sec4)
         178
      1. [10.​5 Analysis and Interpretation Phase](624027_1_En_10_Chapter.xhtml#Sec5)
         178
      1. [10.​6 Dissemination Phase](624027_1_En_10_Chapter.xhtml#Sec6)
         179
      1. [10.​7 Ontological Instantiation Snapshot](624027_1_En_10_Chapter.xhtml#Sec7)
         180
      1. [10.​8 Querying the Instantiation](624027_1_En_10_Chapter.xhtml#Sec8)
         181
      1. [10.​9 Coverage and Missing Elements](624027_1_En_10_Chapter.xhtml#Sec9)
         181
      1. [10.​10 Interpretation and Teaching Notes](624027_1_En_10_Chapter.xhtml#Sec10)
         182
         1. [10.​10.​1 What the Results Mean](624027_1_En_10_Chapter.xhtml#Sec11)
            182
         1. [10.​10.​2 How to Reuse This Study](624027_1_En_10_Chapter.xhtml#Sec12)
            182
         1. [10.​10.​3 Common Misconceptions Clarified](624027_1_En_10_Chapter.xhtml#Sec13)
            182
         1. [10.​10.​4 Minimal Reproducibility Kit](624027_1_En_10_Chapter.xhtml#Sec14)
            182
      1. [10.​11 Final Remarks](624027_1_En_10_Chapter.xhtml#Sec15)
         182
   1. [11 Example 4:​ Echoes in the IoT Lab](624027_1_En_11_Chapter.xhtml)
      185
      1. [11.​1 Context and Motivation](624027_1_En_11_Chapter.xhtml#Sec1)
         186
      1. [11.​2 Planning Phase](624027_1_En_11_Chapter.xhtml#Sec2)
         186
      1. [11.​3 Pre-Operation Phase](624027_1_En_11_Chapter.xhtml#Sec3)
         187
      1. [11.​4 Operation Phase](624027_1_En_11_Chapter.xhtml#Sec4)
         188
      1. [11.​5 Analysis and Interpretation Phase](624027_1_En_11_Chapter.xhtml#Sec5)
         189
      1. [11.​6 Dissemination Phase](624027_1_En_11_Chapter.xhtml#Sec6)
         189
      1. [11.​7 Ontological Instantiation Snapshot](624027_1_En_11_Chapter.xhtml#Sec7)
         190
      1. [11.​8 Querying the Instantiation](624027_1_En_11_Chapter.xhtml#Sec8)
         190
      1. [11.​9 Coverage and Missing Elements](624027_1_En_11_Chapter.xhtml#Sec9)
         191
      1. [11.​10 Interpretation and Teaching Notes](624027_1_En_11_Chapter.xhtml#Sec10)
         192
         1. [11.​10.​1 What the Results Mean](624027_1_En_11_Chapter.xhtml#Sec11)
            192
         1. [11.​10.​2 How to Reuse This Study](624027_1_En_11_Chapter.xhtml#Sec12)
            192
         1. [11.​10.​3 Common Misconceptions Clarified](624027_1_En_11_Chapter.xhtml#Sec13)
            192
         1. [11.​10.​4 Minimal Reproducibility Kit](624027_1_En_11_Chapter.xhtml#Sec14)
            193
      1. [11.​11 Final Remarks](624027_1_En_11_Chapter.xhtml#Sec15)
         193
   1. [12 Example 5:​ The Invisible Signature:​ Blockchain Provenance](624027_1_En_12_Chapter.xhtml)
      195
      1. [12.​1 Context and Motivation](624027_1_En_12_Chapter.xhtml#Sec1)
         196
      1. [12.​2 Planning Phase](624027_1_En_12_Chapter.xhtml#Sec2)
         196
      1. [12.​3 Pre-Operation Phase](624027_1_En_12_Chapter.xhtml#Sec3)
         197
      1. [12.​4 Operation Phase](624027_1_En_12_Chapter.xhtml#Sec4)
         198
      1. [12.​5 Analysis and Interpretation Phase](624027_1_En_12_Chapter.xhtml#Sec5)
         199
      1. [12.​6 Dissemination Phase](624027_1_En_12_Chapter.xhtml#Sec6)
         200
      1. [12.​7 Ontological Instantiation Snapshot](624027_1_En_12_Chapter.xhtml#Sec7)
         200
      1. [12.​8 Querying the Instantiation](624027_1_En_12_Chapter.xhtml#Sec8)
         200
      1. [12.​9 Coverage and Missing Elements](624027_1_En_12_Chapter.xhtml#Sec9)
         202
      1. [12.​10 Interpretation and Teaching Notes](624027_1_En_12_Chapter.xhtml#Sec10)
         203
         1. [12.​10.​1 What the Results Mean](624027_1_En_12_Chapter.xhtml#Sec11)
            203
         1. [12.​10.​2 How to Reuse This Study](624027_1_En_12_Chapter.xhtml#Sec12)
            203
         1. [12.​10.​3 Common Misconceptions Clarified](624027_1_En_12_Chapter.xhtml#Sec13)
            203
         1. [12.​10.​4 Minimal Reproducibility Kit](624027_1_En_12_Chapter.xhtml#Sec14)
            203
      1. [12.​11 Final Remarks](624027_1_En_12_Chapter.xhtml#Sec15)
         204

1. Part V Integration, Reflection, and Future Directions
   205
   1. [13 Concluding Remarks:​ Toward a Scientifically Grounded and Open Digital Forensics](624027_1_En_13_Chapter.xhtml)
      207
      1. [13.​1 Contextualizatio​n](624027_1_En_13_Chapter.xhtml#Sec1)
         207
      1. [13.​2 Integrative Synthesis](624027_1_En_13_Chapter.xhtml#Sec2)
         208
      1. [13.​3 Critical Discussion](624027_1_En_13_Chapter.xhtml#Sec3)
         209
      1. [13.​4 Implications and Contributions](624027_1_En_13_Chapter.xhtml#Sec4)
         210
      1. [13.​5 Future Perspectives](624027_1_En_13_Chapter.xhtml#Sec5)
         211
      1. [13.​6 Closing Message](624027_1_En_13_Chapter.xhtml#Sec6)
         211

# Part I Fundamentals of Digital Forensics and Controlled Experimentation

This part establishes the theoretical and methodological underpinnings required for advancing Digital Forensics experimentation. Its overarching goal is to frame the field within the broader scientific tradition, emphasizing rigor, transparency, and reproducibility as essential conditions for producing reliable and cumulative knowledge. By drawing from established scientific practices while adapting them to the specificities of forensic inquiry, this part provides the conceptual and methodological scaffolding necessary to consolidate Digital Forensics as both a practical discipline and a scientific enterprise.

The urgency of such foundations stems from the position of Digital Forensics as a relatively young field, tasked simultaneously with addressing pressing investigative needs and developing a coherent scientific identity. Without structured methodologies, research risks fragmentation, lack of comparability, and diminished credibility in both academic and legal contexts. Establishing a rigorous basis for experimentation, therefore, is not only an intellectual requirement but also a practical necessity for ensuring the reliability of forensic outcomes.

Chapter [1](624027_1_En_1_Chapter.xhtml) introduces the fundamentals of conceptual modeling, demonstrating how abstract representations help structure knowledge domains, clarify key concepts, and mediate between theoretical perspectives and empirical applications. Conceptual models are presented as indispensable instruments for ensuring semantic clarity, methodological consistency, and a foundation for reproducibility.

Chapter [2](624027_1_En_2_Chapter.xhtml) examines the design and execution of controlled experiments in Digital Forensics, addressing methodological challenges such as volatile evidence, unique investigative contexts, and ethical or legal restrictions. By focusing on variable identification, the definition of experimental units, and the establishment of replicable procedures, this chapter positions experimental design as both a methodological necessity and a flexible practice adapted to the realities of forensic inquiry.

Chapter [3](624027_1_En_3_Chapter.xhtml) turns explicitly to the role of reproducibility as a defining feature of scientific knowledge and as a central concern for Digital Forensics. It examines the historical and epistemological foundations of reproducibility, the challenges presented by proprietary tools and volatile evidence, and the implications of limited replicability for the credibility of forensic results. By situating Digital Forensics within broader debates on the reproducibility crisis, the chapter highlights both the vulnerabilities of current practices and the opportunities for strengthening the field. It argues that reproducibility, supported by conceptual modeling, transparent documentation, and standardized experimental protocols, is not merely a technical requirement but a strategic imperative for establishing Digital Forensics as a trustworthy scientific discipline.

Taken together, these chapters provide a coherent and rigorous framework that situates Digital Forensics controlled experimentation within a formal scientific context. This part thus contributes to the consolidation of the discipline by advancing reproducibility as a methodological cornerstone and by encouraging a cultural shift from tool-driven, ad hoc practices to evidence-based, systematically grounded approaches capable of producing knowledge that is simultaneously practical, transparent, and enduring.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_1>

# 1. Digital Forensics in a Nutshell

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

Digital forensics has evolved from an ad hoc response to cybercrimes into a structured, science-based discipline, driven by the pervasive integration of digital systems into society. Its historical trajectory, marked by pioneering legal initiatives like the Florida Computer Crimes Act (1978), the development of disk-imaging tools in the 1980s, and the formalization of “computer forensics” in the 1990s with the emergence of commercial (EnCase, Exterro Forensic Toolkit) and open-source (Sleuth Kit) suites, reflects the continuous interplay between emerging technical challenges and evolving institutional responses, such as the establishment of the Scientific Working Group on Digital Evidence (SWGDE) and international protocols like the Budapest Convention. By 2012, agencies like the FBI’s Computer Analysis and Response Team demonstrated the field’s institutional maturity by processing thousands of cases annually. The investigative process is refined into five fundamental phases: identification, preservation, collection, examination, and presentation, ensuring repeatability, forensic soundness, and legal defensibility, while confronting challenges posed by volatile data, encryption, and cloud infrastructures. The field has diversified into specialized branches, including computer forensics (disk analysis, file recovery, and timeline reconstruction), network forensics (traffic analysis and intrusion detection), mobile device forensics (smartphone data extraction), cloud forensics (distributed environments), and Internet of Things (IoT) forensics (interconnected smart devices), each with unique methodologies and tools. Other vital branches include memory and database forensics, with emerging areas like blockchain and automotive forensics further expanding their scope. The future of digital forensics is shaped by the increasing complexity of digital ecosystems, demanding rigorous scientific practices, empirical validation, and statistical methods to ensure reliability. The integration of artificial intelligence (AI) and machine learning (ML) promises greater efficiency in analyzing massive data volumes, though it raises concerns about transparency. AI also brings new challenges that need to be tackled in the near future. Scalability, innovative approaches for cloud and IoT evidence, organizational forensic readiness, and robust professional training are crucial for adaptation. Ultimately, the convergence of forensic science, AI, cloud computing, and big data analytics, grounded in rigorous empirical methods, will shape the field’s future, ensuring both technical efficiency and compliance with ethical and legal standards.

## 1.1 History of Digital Forensics

The evolution of digital forensics (DF) reflects the growing interdependence between technology and society. As digital systems became integral to personal, commercial, and governmental activities, new forms of crime and misconduct emerged, prompting the need for systematic methods to extract, preserve, and analyze digital evidence. Digital forensics, as a discipline, was developed in parallel with advancements in computing technology, legal frameworks, investigative procedures, and international cooperation. What began as an ad hoc response to isolated incidents has matured into a structured, science-based field with recognized standards, methodologies, and tools. This section provides a chronological overview of the discipline’s key milestones. It traces its roots from the earliest legal initiatives and investigative practices in the 1970s to the complex, multidisciplinary ecosystem it represents today. Each phase in this historical trajectory highlights the interplay between emerging technical challenges and evolving institutional responses. Together, they have laid the foundation for digital forensics as both an academic discipline and a vital component of modern justice systems.

Digital forensics emerged in the 1970s, coinciding with the development of early computer crime laws. The Florida Computer Crimes Act (1978) marked the first attempt to legislate unauthorized data manipulation, setting a pattern for broader national legal frameworks [[37](#CR37)]. Law enforcement began to confront computer-based crimes in the 1980s. The FBI’s Magnetic Media Program (1984) evolved into the Computer Analysis and Response Team (CART), prompting the development of disk imaging tools like IMDUMP and SafeBack to avoid volatile live system analysis [[8](#CR8)]. Academically, the early 1990s marked the emergence of the term “computer forensics” in scholarly discourse, as evident in conferences such as the Digital Forensic Research Workshop (DFRWS). Early research, such as Pollitt’s work [[39](#CR39)], helped formalize methodology and vocabulary. The mid-1990s saw the emergence of both commercial suites (EnCase, FTK) and open-source kits (Sleuth Kit), facilitating wider adoption and application in both legal and investigative contexts.

As the field matured, structured frameworks were introduced to enhance the rigor and reproducibility of investigations. Beebe and Clark’s objectives-based process model [[6](#CR6)] introduced hierarchical investigative phases, enabling layered and methodical analysis. Institutions like the Scientific Working Group on Digital Evidence (SWGDE) [[43](#CR43)] were established in 2000, issuing best practice documents and promoting ISO/IEC 17025 accreditation for laboratories [[21](#CR21)]. Global protocols, such as the Budapest Convention (2004), addressed transnational forensic cooperation and laid the groundwork for harmonized procedures across jurisdictions.

The rise of smartphones, cloud services, and Internet of Things (IoT) demanded fresh forensic strategies. Grispos et al. [[17](#CR17)] were among the early researchers analyzing disrupted cloud workflows. Big data and AI began transforming evidence analysis. Casino et al. [[11](#CR11)] reviewed the applications of machine learning, blockchain, and graph analytics in sifting through large-scale forensic datasets. Simultaneously, the proliferation of anti-forensic techniques, such as encryption, tampering, and evasion, has triggered scientific scrutiny. Formal methods, such as the Knowledge Acquisition in Automated Specification (KAOS) [[22](#CR22)], have been applied to model and counter such threats. By 2012, FBI CART and Regional Computer Forensics Laboratories (RCFLs) were routinely processing thousands of cases annually. The Department of Defense (DoD’s) Defense Computer Forensics Laboratory (DCFL) (later Department of Defense Cyber Crime Center—DC3), established in 2001, centralized military forensic capabilities, reflecting institutional maturity and the growing strategic importance of digital investigations [[24](#CR24)].

Over the past decade, digital forensics has undergone significant transformations driven by the rapid expansion of cyber-physical systems, encrypted communications, and the globalization of cybercrime [[13](#CR13)]. The increasing prevalence of end-to-end encryption in messaging platforms, the widespread adoption of zero-trust architectures, and the diversification of digital evidence sources, ranging from wearables and smart home devices to decentralized networks, have necessitated novel investigative approaches. Law enforcement and forensic practitioners have embraced cloud-native analysis platforms, automated triage tools, and AI-powered classification systems to manage overwhelming volumes of data. Regulatory developments such as the General Data Protection Regulation (GDPR) in Europe have also introduced new legal and ethical considerations for evidence handling and cross-border collaboration. Furthermore, the emergence of cryptocurrency-related crimes has led to the development of specialized blockchain forensics methods, thereby fostering a new subfield that integrates traditional forensic principles with financial investigation techniques.

## 1.2 The Digital Forensics Investigative Process

The DF investigative process is a systematic methodology employed to uncover, analyze, and interpret digital evidence for legal or administrative purposes. Over time, this process has been refined into well-defined models that aim to ensure repeatability, forensic soundness, and legal defensibility. Among the earliest and most widely referenced models is the one proposed by Reith et al. [[42](#CR42)], which comprises five phases: identification, preservation, collection, examination, and presentation. These phases form the backbone of many contemporary investigative workflows and remain foundational in both academic and practical contexts. Building upon these conceptual foundations, more recent works have refined and detailed the investigative life cycle.

Figure [1.1](#Fig1) depicts the six-phase DF investigative process, according to Nath et al. [[33](#CR33)].

![Flowchart illustrating a process with six main steps: (1) Identification, (2) Collection, (3) Preservation, (4) Examination, (5) Analysis, and (6) Presentation. The process includes documentation and emphasizes the “Chain of Custody” during preservation and transfer stages. Arrows indicate the flow and connections between steps, highlighting the cyclical nature of preservation and transfer.](../images/624027_1_En_1_Chapter/624027_1_En_1_Fig1_HTML.png)

Fig. 1.1

The Digital Forensics investigative process by Nath et al. [[33](#CR33)]

The identification phase involves recognizing and defining potential sources of digital evidence. This step includes determining the incident scope, identifying relevant systems (e.g., desktops, laptops, mobile devices, and servers), and understanding the incident type (e.g., insider threat, malware infection, and data exfiltration). Increasingly, this phase must account for emerging technologies, such as IoT devices and cloud services, which often require distinct handling procedures due to their distributed and volatile nature [[41](#CR41)]. Investigators must act swiftly, as digital evidence is frequently fragile and prone to alteration or loss.

The preservation phase ensures that the digital evidence remains intact and unaltered. This is crucial for maintaining the credibility of the evidence in legal settings. Forensic imaging tools are commonly used to create bit-for-bit copies of storage media. Hashing algorithms, such as SHA-2 or SHA-3, are applied both before and after imaging to verify data integrity [[37](#CR37)]. In addition to technical measures, strict documentation of the chain of custody must be maintained to ensure accountability and transparency. This includes logging who accessed the evidence, when, for what purpose, and under what conditions. Any break in the chain can render the evidence inadmissible in court.

During the collection phase, investigators acquire the identified data sources in a forensically sound manner. The choice between live and static acquisition is critical here. Live acquisition, performed while the system is powered on, may be necessary to capture volatile data such as active network connections, RAM contents, and running processes. However, it also risks altering the system state. Conversely, static acquisition, performed after the system is shut down, provides more controlled conditions but may miss transient data [[32](#CR32)]. Regardless of the method, the goal remains the same: collect the maximum relevant evidence with minimal system impact.

The examination and analysis phases are where raw data is transformed into actionable intelligence. Examination involves preparing the data for analysis by filtering, recovering deleted content, or converting formats. Analysis, on the other hand, consists of interpreting the data to reconstruct events or determine culpability. Techniques such as keyword searches, timeline construction, log correlation, metadata analysis, and anomaly detection are commonly used [[8](#CR8)]. Advanced techniques, such as malware reverse engineering or steganalysis, may be applied in specialized cases. Investigators must meticulously document all procedures and findings to ensure transparency and reproducibility.

Finally, the presentation phase focuses on communicating findings to nontechnical stakeholders, such as legal professionals, corporate managers, or juries. This requires translating technical analysis into clear, comprehensible reports and, if necessary, expert testimony. Reports must be concise, logically structured, and backed by the evidence collected during the investigation. Visual aids, such as charts, diagrams, and timelines, can be instrumental in explaining complex findings [[8](#CR8)]. In legal contexts, investigators must also be prepared to defend their methods and conclusions under cross-examination.

Digital forensic investigations are not linear; they are often iterative and may involve revisiting previous stages based on new evidence or insights. Moreover, investigators must remain aware of the jurisdictional and legal constraints relevant to their activities. The increasing use of encryption, anonymization tools, and remote/cloud infrastructures continues to pose new challenges to traditional forensic workflows [[45](#CR45)]. As such, continuous professional development and adherence to evolving standards are crucial for maintaining the effectiveness and admissibility of forensic investigations.

## 1.3 Digital Forensics Main Branches

Digital forensics is a multidisciplinary field that investigates digital evidence to understand and reconstruct events involving digital devices and networks. Over time, it has diversified into several distinct branches, each focusing on specific environments, technologies, and challenges. The main branches of digital forensics include computer forensics, network forensics, mobile device forensics, cloud forensics, Internet of Things (IoT) forensics, memory forensics, database forensics, and emerging specialized domains. Each branch requires unique methodologies, tools, and legal considerations due to the diversity of devices, data structures, and operational contexts [[25](#CR25)].

Figure [1.2](#Fig2) depicts the main branches of DF.

![Flow chart illustrating eight branches of digital forensics. 1. Computer Forensics: Examines computer systems like desktops, laptops, and servers. 2. Network Forensics: Involves systematic capture, recording, and analysis of network traffic. 3. Mobile Device Forensics: Focuses on extracting, preserving, and analyzing data from mobile operating systems. 4. Cloud Forensics: Addresses challenges from distributed, virtualized, and multi-tenant cloud environments. 5. IoT Forensics: Investigates interconnected smart devices, including wearables and industrial sensors. 6. Memory Forensics: Focuses on analyzing a system’s RAM for valuable artifacts. 7. Database Forensics: Examines integrity, transactions, and audit trails within database management systems. 8. Emerging Branches: Includes blockchain, automotive, ICS/SCADA, and live forensics.](../images/624027_1_En_1_Chapter/624027_1_En_1_Fig2_HTML.png)

Fig. 1.2

Main Digital Forensics branches

### 1.3.1 Computer Forensics

Also known as disk forensics or traditional forensics, this branch focuses on the examination of computer systems, including desktops, laptops, and servers. The primary goal is to identify, preserve, analyze, and present digital evidence in a manner that is legally admissible and scientifically valid. Investigators rely on specialized software and hardware tools to perform disk imaging, which involves creating bit-by-bit copies of storage media. This process ensures the integrity of the original evidence and allows a forensic examination to proceed on a verified duplicate [[9](#CR9)].

Computer forensics plays a vital role in criminal investigations, internal corporate inquiries, incident response, and legal proceedings. It enables investigators to uncover evidence related to cybercrimes, intellectual property theft, unauthorized access, and other digital offenses [[6](#CR6)].

Key activities within computer forensics include the following:

* **File recovery:** Investigators use forensic tools to retrieve deleted, hidden, or partially overwritten files. Data that has been removed from the file system may still reside on the disk and can often be reconstructed.
* **Metadata analysis:** Examination of file system metadata, including timestamps (created, modified, and accessed), file permissions, and user identifiers, helps reconstruct user actions and establish timelines of activity.
* **Registry analysis:** In Microsoft Windows environments, the system registry provides valuable information about system configuration, user activity, installed software, and connected devices. Analysis of registry hives can reveal evidence such as recently accessed files, USB device history, and autostart entries.
* **Timeline reconstruction:** By correlating data from various sources, including file metadata, logs, and registry entries, forensic practitioners can generate chronological timelines that describe user interactions and system events.
* **Keyword searching and content analysis:** Investigators perform targeted keyword searches across file contents, system logs, and unallocated space to identify relevant evidence, such as incriminating documents, communication records, or contraband data.
* **Data carving and file signature analysis:** These techniques are used to locate and recover file fragments based on known header and footer patterns, particularly when file system metadata is damaged or unavailable.

The evolution of storage technologies and operating systems presents new challenges for practitioners in this field. The widespread use of solid-state drives (SSDs), for example, introduces complexities related to wear-leveling algorithms, garbage collection, and the TRIM command, which can permanently erase deleted data, reducing opportunities for recovery. Investigators may need to account for these behaviors by acquiring volatile memory or using specialized firmware-level techniques [[37](#CR37)].

Encrypted file systems, such as BitLocker, FileVault, or LUKS, further complicate forensic analysis. Accessing data stored on encrypted volumes may require recovering cryptographic keys, which can be achieved through memory analysis, user cooperation, brute-force attacks, or analysis of key escrow mechanisms [[14](#CR14)].

Modern computer systems also frequently incorporate cloud-based synchronization, virtualization, and remote storage, distributing data across multiple environments. This necessitates a broader scope of investigation that may include forensic analysis of virtual machine images, cloud service logs, and remote backups [[6](#CR6)].

To support these complex investigations, forensic analysts use a range of tools, including commercial suites such as EnCase and FTK, as well as open-source frameworks such as The Sleuth Kit, Autopsy, and Volatility. The choice of tools depends on the case requirements, the types of systems involved, and the legal and regulatory context [[8](#CR8)].

### 1.3.2 Network Forensics

Network forensics involves the systematic capture, recording, and analysis of network traffic to detect intrusions, unauthorized access, malware communication, or data exfiltration. It is a critical subfield of digital forensics that provides insight into incidents involving external attacks, insider threats, or misconfigurations that impact network security and performance [[15](#CR15)].

Because network traffic is inherently volatile and transient, one of the primary challenges in network forensics is ensuring timely data collection before it is overwritten or lost. Investigators often rely on real-time packet capture tools, such as Wireshark or tcpdump, as well as flow-based monitoring systems (e.g., NetFlow or IPFIX), to obtain relevant artifacts. To maintain forensic soundness, robust logging mechanisms and timestamp synchronization via protocols such as Network Time Protocol (NTP) are essential [[15](#CR15)].

Key tasks in network forensics include:

* **Packet capture and inspection:** collecting raw traffic at key points in the network to examine headers, payloads, and anomalies indicative of malicious activity
* **Session reconstruction:** rebuilding TCP or application layer sessions to understand user interactions or attacker behavior, which may include web browsing, file transfers, or command-and-control communication
* **Protocol analysis:** investigating network protocols across different layers of the OSI model to identify misuse, protocol violations, or covert channels
* **Traffic pattern analysis:** detecting anomalies through statistical or machine learning models that flag deviations in traffic volume, flow timing, or packet size distributions

The increasing use of Transport Layer Security (TLS), Virtual Private Networks (VPNs), and encrypted messaging platforms introduces substantial obstacles to content-level inspection. Investigators must often rely on metadata, such as destination IP addresses, DNS records, and traffic timing, to infer suspicious behavior when payloads are inaccessible due to encryption [[15](#CR15)].

Scalability is another key concern. High-speed networks generate immense volumes of data, requiring selective logging, distributed storage, and scalable analysis to manage them effectively. Technologies such as Deep Packet Inspection (DPI), stream processing, and network telemetry are frequently employed to manage this scale [[15](#CR15)].

Moreover, the rise of Software-Defined Networking (SDN) and Network Function Virtualization (NFV) has introduced architectural complexity. These technologies abstract physical infrastructure and enable dynamic reconfiguration, making traditional static network analysis insufficient. Investigators must now consider virtual switches, programmable flow rules, and ephemeral network paths during analysis [[15](#CR15)].

### 1.3.3 Mobile Device Forensics

With the proliferation of smartphones and tablets, mobile forensics has become a crucial discipline within digital investigations [[4](#CR4)]. It primarily focuses on extracting, preserving, and analyzing data from mobile operating systems, such as iOS and Android, as well as from the vast ecosystem of applications installed on these platforms. The types of data that can be retrieved include call logs, SMS and instant messaging records, multimedia files (images, audio, and video), GPS and location data, Internet browsing history, contacts, calendar entries, and app-specific databases, which may store sensitive information such as authentication tokens or transaction logs.

A variety of acquisition techniques are employed, ranging from logical acquisition, which operates at the file system level and is less intrusive, to physical acquisition, which involves bitstream imaging and enables more comprehensive recovery of deleted or hidden data [[4](#CR4)]. When traditional methods are insufficient, more advanced approaches such as chip-off analysis and JTAG extraction, using the Joint Test Action Group (IEEE 1149.1) hardware interface to access memory directly from embedded devices, may also be applied.

However, mobile forensics faces significant challenges. The diversity of hardware models and manufacturers, coupled with frequent operating system updates, introduces variability that complicates the development of standardized forensic tools and methodologies [[28](#CR28)]. Additionally, strong encryption mechanisms, secure boot processes, and locked devices present considerable hurdles for investigators, often requiring the use of specialized exploits or vendor-specific tools.

The increasing reliance on cloud services further complicates the forensic process. Synchronization mechanisms and automatic backups distribute data across networks and remote servers, raising issues related to jurisdiction, data integrity, and privacy [[28](#CR28)].

### 1.3.4 Cloud Forensics

Cloud forensics addresses challenges arising from the distributed, virtualized, and multi-tenant nature of cloud environments [[4](#CR4)]. Unlike traditional digital forensics, investigators often lack direct physical access to the underlying hardware and instead rely on collaboration with cloud service providers, application programming interfaces (APIs), and logs generated by virtualized infrastructure. The volatility of cloud instances, which can be created, modified, or terminated in seconds, combined with dynamic resource allocation mechanisms such as load balancing and auto-scaling, creates unique difficulties in preserving evidence in a consistent and verifiable manner. Furthermore, the presence of multiple tenants sharing the same infrastructure raises concerns about data isolation, privacy, and the inadvertent collection of unrelated user information.

Jurisdictional and regulatory issues further complicate investigations, as data may be replicated across geographically distributed data centers and be subject to the legal frameworks of different countries. This fragmentation challenges both the timeliness of evidence acquisition and the admissibility of collected data in court. To address these hurdles, research in cloud forensics has focused on developing mechanisms for reliable chain-of-custody preservation, designing forensic-readiness frameworks that enable organizations to anticipate and support future investigations, and implementing automated evidence collection and correlation tools tailored to cloud platforms. Emerging directions also emphasize the integration of blockchain for immutable logging, the use of machine learning to detect anomalies within large-scale cloud logs, and cross-provider standards for interoperability in forensic procedures [[4](#CR4)].

### 1.3.5 Internet of Things (IoT) Forensics

IoT forensics extends digital investigation to the vast array of interconnected smart devices, including wearables, home automation systems, medical devices, industrial sensors, and critical infrastructure components [[2](#CR2)]. These devices are typically resource-constrained in terms of storage, processing power, and battery life, which limits their ability to generate and retain extensive forensic logs. As a result, the data available for analysis is often sparse, fragmented, and presented in heterogeneous formats that vary widely across manufacturers and device categories.

Forensic investigators must therefore gather evidence from multiple layers of the IoT ecosystem, including device firmware, companion mobile applications, local storage, network gateways, and associated cloud servers where data is often aggregated or synchronized. In many cases, reconstructing events requires correlating traces across these distributed sources, a process that is time-consuming and prone to inconsistencies. Privacy concerns are particularly acute in IoT forensics, since many devices continuously capture sensitive personal information such as health metrics, location patterns, and behavioral data.

Additional challenges arise from data volatility, as IoT devices often overwrite logs quickly or transmit data in real time without retaining local copies. Furthermore, the lack of standardized forensic tools and methodologies across the diverse IoT landscape makes it difficult to ensure reliable and repeatable investigations. Current research efforts in this area focus on developing lightweight logging mechanisms for constrained devices, establishing forensic readiness frameworks tailored to IoT architectures, and exploring cross-layer analysis techniques that integrate device, network, and cloud evidence. The rapid pace of IoT adoption and the increasing integration of such devices into critical domains underscore the importance of advancing specialized methods for trustworthy IoT forensics [[2](#CR2)].

### 1.3.6 Memory Forensics

Memory forensics focuses on the volatile contents of a system’s RAM, which may contain valuable artifacts such as running processes, active network connections, encryption keys, decrypted data, and malware signatures that often remain invisible on persistent storage [[23](#CR23)]. Because RAM is constantly changing and is erased when power is lost, the timely acquisition of memory images is a critical first step in this type of investigation. Techniques used in memory forensics include live memory acquisition, reconstruction of process heaps and stack traces, extraction of loaded kernel modules, and identification of hidden or injected code segments that may indicate the presence of rootkits or Advanced Persistent Threats (APTs).

The importance of memory forensics has grown significantly as attacks increasingly operate entirely in memory, thereby evading detection by traditional disk-based forensic methods. Fileless malware, in-memory exploits, and stealthy persistence mechanisms can only be identified through detailed analysis of volatile data [[23](#CR23)]. Furthermore, memory forensics plays an indispensable role in real-time incident response, enabling investigators to capture a snapshot of system activity during an active compromise and to reconstruct attacker behavior.

Challenges in this domain include ensuring the integrity and reliability of memory captures, handling large memory dumps that require scalable analysis tools, and overcoming anti-forensic techniques designed to obfuscate or manipulate RAM content. Recent research has advanced automated memory analysis frameworks, signature-based and heuristic methods for anomaly detection, and visualization techniques for interpreting complex memory structures more effectively. As a result, memory forensics has become a cornerstone of modern digital investigations and malware analysis, bridging the gap between system internals and cyber threat intelligence [[23](#CR23)].

### 1.3.7 Database Forensics

Database forensics examines the integrity, transactions, and audit trails within Database Management Systems (DBMS), aiming to uncover unauthorized data modifications, fraudulent transactions, insider threats, or large-scale data theft [[20](#CR20)]. As databases often store mission-critical and sensitive information, forensic investigations in this domain are essential for maintaining trust, regulatory compliance, and accountability in both corporate and governmental contexts. Investigators typically analyze transaction logs, rollback segments, triggers, stored procedures, and system metadata to reconstruct user actions and verify whether data manipulation has occurred legitimately or maliciously.

The heterogeneity of DBMS platforms represents a significant challenge, as relational systems (e.g., Oracle, MySQL, SQL Server, and PostgreSQL) differ considerably from non-relational (NoSQL) solutions such as MongoDB, Cassandra, or Redis. Furthermore, modern distributed and cloud-based database architectures introduce additional layers of complexity, including sharding, replication, caching mechanisms, and eventual consistency models that complicate the reconstruction of events [[3](#CR3)]. Investigators must therefore adopt customized forensic frameworks capable of handling diverse database engines while ensuring the reliability and admissibility of extracted evidence.

Emerging research in database forensics examines methods for detecting tampering in transaction logs, cryptographic techniques for verifying database integrity, and automated anomaly detection systems for identifying suspicious activities in large-scale datasets. Another growing area of interest is forensic readiness in databases, which emphasizes the proactive design of systems with embedded logging, monitoring, and evidence preservation capabilities. Together, these efforts highlight the evolving nature of database forensics as a specialized yet integral component of digital investigations [[3](#CR3)].

## 1.4 Emerging Specialized Branches

Beyond the main branches of Digital Forensics, a growing number of specialized subfields have emerged in response to technological innovation and the proliferation of complex digital ecosystems. These domains expand the forensic landscape into areas previously beyond the purview of traditional computing, reflecting the pervasive nature of digital traces in contemporary life. They include blockchain forensics, automotive forensics, industrial control systems (ICS)/SCADA forensics, and live forensics. Each introduces distinct technical, methodological, and legal challenges that demand tailored investigative approaches, specialized tools, and interdisciplinary expertise. Together, they illustrate the discipline’s adaptive and evolutionary nature, which continually redefines its scope to remain effective in increasingly hybridized environments.

### 1.4.1 Blockchain Forensics

Blockchain forensics [[1](#CR1)] focuses on analyzing decentralized ledger technologies, with particular emphasis on cryptocurrency transactions and smart contracts. Its main objective is to trace digital financial activities that may be related to illicit behaviors, such as ransomware payments, fraud, money laundering, or the financing of criminal organizations. Although blockchain networks are often perceived as anonymous, forensic analysts exploit their pseudonymous yet publicly transparent nature to reconstruct financial flows.

Investigative techniques typically include clustering algorithms that group wallet addresses belonging to the same entity, temporal and spatial transaction graph analysis, and heuristic-based linking of on-chain activity with off-chain data. Integration with Know-Your-Customer (KYC) and Anti-Money-Laundering (AML) information provided by cryptocurrency exchanges further enhances attribution capabilities. The immutability of blockchain data provides an auditable trail, but its volume, distributed nature, and privacy-enhancing technologies (such as mixers and privacy coins) introduce significant analytical complexity.

Emerging approaches combine machine learning and graph theory to detect anomalous transaction patterns or hidden relationships among wallets. Additionally, innovative contract forensics has become a growing subarea concerned with analyzing vulnerabilities, verifying code provenance, and tracing interactions of decentralized applications (dApps). As blockchain adoption expands into supply chains, voting systems, and identity management, blockchain forensics plays a vital role in ensuring trust, accountability, and compliance across decentralized ecosystems.

### 1.4.2 Automotive Forensics

Automotive forensics [[19](#CR19)] investigates digital evidence produced by modern vehicles, which have evolved into highly networked computing platforms. Contemporary automobiles are equipped with dozens of electronic control units (ECUs), infotainment systems, sensors, telematics modules, and cloud connectivity services. These components continuously collect and exchange data that can reveal detailed behavioral, operational, and geospatial information.

Forensic analyses may involve recovering data such as GPS coordinates, speed and acceleration logs, braking patterns, gear shifts, and communication records between the vehicle and external devices. Infotainment systems often retain user data, including paired smartphone information, call logs, or even multimedia playback history. Such artifacts can be crucial in accident reconstruction, insurance investigations, and criminal cases involving the misuse of vehicles.

However, automotive forensics faces numerous challenges. Each manufacturer implements proprietary architectures, encryption mechanisms, and communication protocols such as CAN, LIN, or FlexRay, making standardization difficult. Many systems are designed to resist tampering, requiring specialized diagnostic interfaces, reverse engineering, or cooperation with manufacturers. Furthermore, privacy regulations and data ownership concerns must be addressed when accessing driver-related data stored within telematics or navigation systems. As vehicles become increasingly autonomous, incorporating artificial intelligence and over-the-air updates, forensic readiness in the automotive sector must evolve to ensure that event data can be preserved and interpreted reliably for both safety and accountability.

### 1.4.3 ICS and SCADA Forensics

Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) forensics [[12](#CR12)] focuses on investigating digital incidents within industrial control systems and critical infrastructure environments. These systems govern vital processes, including electricity distribution, water purification, transportation management, and industrial automation. Because they directly affect public safety and essential services, forensic investigations in these contexts must be carefully balanced with operational continuity and safety considerations.

ICS/SCADA environments are characterized by unique constraints: legacy systems with limited security features, real-time control requirements, and deterministic communication protocols. Unlike conventional IT systems, downtime in industrial systems can lead to severe economic or physical consequences, making noninvasive forensic techniques essential. Investigators typically analyze network traffic between control units, logs from Programmable Logic Controllers (PLCs), historian databases, and human–machine interface (HMI) events to reconstruct incidents, such as sabotage, system malfunctions, or unauthorized reconfigurations.

A significant challenge lies in the coexistence of decades-old hardware with modern networked components, which often creates security gaps. Cyberattacks, such as Stuxnet, Triton, and Industroyer, have demonstrated how adversaries exploit these vulnerabilities to disrupt critical services. Consequently, research in ICS/SCADA forensics emphasizes forensic readiness, anomaly detection, and hybrid architectures that combine real-time monitoring with post-incident analysis. New methodologies are being developed to ensure data integrity and operational continuity, including the use of digital twins for forensic reconstruction and the adoption of blockchain-based audit mechanisms for industrial events.

### 1.4.4 Live Forensics

Live forensics [[19](#CR19)] addresses the acquisition and analysis of volatile data from active systems, where shutting down the device would result in the loss of critical evidence. It is an essential practice in modern incident response, enabling investigators to observe and capture ephemeral artifacts such as running processes, open network connections, in-memory cryptographic keys, and temporary files.

The central principle of live forensics is to preserve as much of the system’s original state as possible while minimizing contamination introduced by the investigative process. This balance is inherently delicate: Every command executed on a live system can potentially modify memory, timestamps, or logs. Therefore, live forensic procedures are guided by rigorous methodological and legal protocols that emphasize reproducibility and auditability.

Live forensics is particularly valuable in contexts involving malware infections, insider threats, and active cyber intrusions. Analysts can capture system snapshots, extract volatile evidence, and generate real-time intelligence to contain and mitigate attacks. Standard tools and frameworks, such as volatility, Rekall, and memory acquisition utilities such as LiME or WinPMEM, are often integrated with live response toolkits that automate evidence collection according to predefined policies. Recent advances explore containerized environments, memory introspection through hypervisors, and AI-assisted prioritization of evidence acquisition, enabling investigators to operate effectively even in high-speed or distributed systems.

The legal and ethical implications of live forensics remain a topic of debate. Questions concerning the admissibility of volatile evidence, privacy protection, and proportionality in data acquisition persist. Nevertheless, its strategic value in time-sensitive investigations, where rapid containment is essential, continues to drive innovation in this field.

### 1.4.5 Integrative Perspective

These specialized domains collectively underscore the dynamic and interdisciplinary nature of Digital Forensics. Each field responds to specific technological contexts while sharing foundational concerns about evidence preservation, methodological rigor, and ethical accountability. As blockchain ecosystems intersect with IoT networks and vehicles and industrial systems become increasingly connected to cloud infrastructure, cross-domain forensic approaches are becoming increasingly necessary.

Future directions point toward convergence, including unified forensic ontologies, standardized metadata schemas, and automation enabled by artificial intelligence. Integrative frameworks are emerging to support interoperability among tools and domains, fostering a cohesive ecosystem capable of handling hybrid forensic scenarios. Such advances are crucial to ensuring that forensic science remains reliable, transparent, and adaptable amid rapid technological transformation.

## 1.5 Perspectives on Digital Forensics

Digital forensics is undergoing profound changes driven by the increasing complexity and diversity of digital ecosystems. As cyber environments expand beyond traditional computers to include cloud services, Internet of Things (IoT) devices, and decentralized platforms, forensic methodologies must evolve to effectively handle new forms of evidence [[40](#CR40)]. This scenario requires not only technical adaptation but also the incorporation of rigorous scientific practices to ensure the validity and reliability of the analyses.

In this context, empirical methods have become essential tools to ground digital investigations. Conducting controlled experiments and systematic observations allows validating tools, protocols, and hypotheses, ensuring the reproducibility of results and strengthening the reliability of the evidence presented [[14](#CR14)]. The adoption of these practices is crucial for digital forensics to be recognized as a rigorous science and for its application in legal settings [[35](#CR35)].

Moreover, controlled experimentation based on statistical methods is fundamental to measuring accuracy, sensitivity, and confidence levels in forensic processes. The use of these techniques enables the quantification of error margins and the establishment of objective metrics, reinforcing the credibility of conclusions drawn during analysis [[10](#CR10)]. Thus, digital forensics is moving toward a quantitative science model aligned with the highest scientific standards [[36](#CR36)].

The incorporation of artificial intelligence (AI) and machine learning (ML) is among the most promising trends for the field’s future. ML algorithms have been applied to automatic file classification, anomaly detection, and behavior reconstruction from digital logs, significantly increasing investigation efficiency [[13](#CR13)]. These methods enable handling large volumes of data and identifying patterns that would be difficult to detect manually.

However, adopting AI in digital forensics also presents significant challenges, particularly regarding the transparency and interpretability of models. Black-box models, for example, may hinder the understanding and justification of decisions, which is problematic in legal contexts [[13](#CR13)]. Research has explored hybrid systems that combine explicit rules with machine learning to balance performance and explainability.

In addition to interpretability issues, the rapid expansion of AI tools introduces broader challenges for forensic practice. Modern deep learning architectures often operate with limited explainability metadata, making it difficult to reconstruct how an inference was produced. This limitation has been widely discussed in the explainable AI literature [[30](#CR30)] and becomes even more problematic in systems that employ continuous training or federated learning, where the model evolves dynamically, and prior states are not preserved.

AI systems also become targets and vectors for attacks, complicating forensic reconstruction. Adversarial examples can induce misclassifications with minimal, imperceptible perturbations [[16](#CR16)]. Sophisticated attacks such as the Carlini and Wagner method [[7](#CR7)] and poisoning techniques that compromise training pipelines [[18](#CR18)] can alter model behavior without leaving conventional forensic artifacts. Understanding and detecting such manipulations requires forensic methods capable of analyzing model drift, prediction sequence inconsistencies, and indicators of compromise in the training data [[38](#CR38)].

The widespread availability of generative AI models also challenges the authenticity and provenance of digital evidence. Deepfake generation techniques have reached a level of realism that complicates visual and auditory verification [[31](#CR31)]. These developments raise significant legal and technical concerns regarding the reliability of digital media. Researchers have proposed detection strategies based on neural fingerprints and artifact-based classifiers to identify manipulated content [[44](#CR44)], and studies highlight the broader implications for trust and verification in digital ecosystems [[26](#CR26)].

Moreover, AI-based forensic tools must themselves be rigorously empirically validated to ensure reliability, reproducibility, and the absence of systematic bias. Frequent updates to commercial AI systems can unexpectedly alter model behavior, affecting the types of artifacts generated and complicating retrospective analyses. These dynamics emphasize the need for transparent benchmarking datasets, standardized evaluation protocols, and continuous monitoring of AI tool performance.

Another crucial aspect of digital forensics is scalability to handle massive data volumes. The use of big data frameworks and distributed systems has enabled the parallel, efficient processing of large-scale data, which is indispensable for investigating evidence in complex, extensive environments [[27](#CR27)]. This technological infrastructure enables faster, more comprehensive analyses, thereby enhancing the impact of investigations.

The evolution of cloud services imposes new challenges for evidence collection and preservation. Issues such as multi-tenancy, data volatility, and jurisdictional conflicts complicate traditional methods, requiring the development of specific protocols grounded in empirical research [[4](#CR4)]. Such studies are crucial to ensuring the validity and admissibility of digital evidence across various legal contexts.

In the IoT domain, evidence fragmentation and volatility demand innovative and empirically validated approaches. Controlled simulations and experimental environments have been employed to test methodologies capable of handling device diversity and data formats, thereby advancing the reliability of analyses in this scenario [[4](#CR4)]. Ongoing research is fundamental to keep pace with the rapid expansion of these devices.

Similarly, applying machine learning to network forensics can help detect sophisticated attacks such as advanced persistent threats. Experimental validation under realistic conditions is indispensable to ensure model robustness and practical applicability [[5](#CR5)]. Integrating advanced computational techniques with experimentation enhances the effectiveness of the investigation.

Organizational forensic readiness is another area gaining increased attention. Strategies involving data logging and preservation policies are evaluated through controlled experiments that simulate incidents, enabling process optimization and reducing the impact of attacks [[5](#CR5)]. This preventive approach contributes to a more efficient and legally sound response.

Legally, the standardization and reproducibility of forensic procedures are fundamental requirements for the acceptance of digital evidence in courts. Initiatives such as tool testing promoted by NIST demonstrate the importance of statistical validation and the definition of objective metrics to ensure the quality and reliability of results [[29](#CR29)]. Empirical research thus supports building solid foundations for forensic practice.

Training digital forensics professionals is evolving in tandem with these transformations, incorporating lab-based and simulation training environments that replicate real-world scenarios. These educational methods enable the development of technical skills and familiarity with applied scientific experimentation [[29](#CR29)]. Education aligned with empirical practices strengthens investigative capability and academic innovation [[34](#CR34)].

Furthermore, close collaboration between academia and investigative agencies has driven essential advances, enabling the application of research in real scenarios. This cooperation allows refinement of tools and methods to align with operational and legal needs [[5](#CR5)]. Knowledge exchange between researchers and practitioners strengthens the field as a whole.

The convergence of forensic science, artificial intelligence, cloud computing, and big data analytics will increasingly mark the future of digital forensics. For this integration to be effective and reliable, innovations must be grounded in rigorous empirical methods, ensuring not only technical efficiency but also ethical and legal compliance [[5](#CR5)].

## 1.6 Final Remarks

The discipline of digital forensics has evolved profoundly from an ad hoc response to cybercrimes into a structured, science-based discipline. This evolution reflects the growing integration of digital systems into all facets of personal, commercial, and governmental life, giving rise to new forms of misconduct and a pressing need for systematic methods to extract, preserve, and analyze digital evidence. What began in the 1970s with early legal initiatives, such as the Florida Computer Crimes Act (1978), has matured into a complex, multidisciplinary ecosystem today.

A continuous interplay between emerging technical challenges and evolving institutional responses characterizes the discipline’s progression. Important milestones include the development of disk imaging tools in the 1980s, such as IMDUMP and SafeBack, the formalization of “computer forensics” in academic discourse in the early 1990s, and the emergence of both commercial forensic suites (EnCase, FTK) and open-source kits (Sleuth Kit) in the mid-1990s. Institutions like SWGDE were established in 2000 to promote best practices and ISO/IEC 17025 accreditation for laboratories. Meanwhile, international protocols, such as the Budapest Convention (2004), addressed transnational forensic cooperation. By 2012, organizations like the FBI CART and the DoD’s DCFL were routinely processing thousands of cases annually, reflecting significant institutional maturity.

The digital forensics investigative process has been refined into well-defined models to ensure repeatability, forensic soundness, and legal defensibility. The five fundamental phases (identification, preservation, collection, examination, and presentation) remain central to contemporary investigative workflows. The identification phase involves recognizing and defining potential sources of digital evidence, considering emerging technologies such as Internet of Things (IoT) devices and cloud services, which often require distinct handling procedures due to their distributed and volatile nature. Preservation ensures that digital evidence remains intact and unaltered, with forensic imaging tools and hashing algorithms (such as SHA-2 and SHA-3) being crucial for verifying data integrity. During collection, investigators acquire the identified data sources in a forensically sound manner, choosing between live acquisition and static acquisition. The examination and analysis phase transforms raw data into actionable intelligence, using techniques such as keyword searches, timeline construction, log correlation, metadata analysis, and anomaly detection. Ultimately, the presentation emphasizes communicating findings to nontechnical stakeholders through concise reports and expert testimony. Digital forensic investigations are not linear; they are often iterative and require constant attention to jurisdictional and legal constraints.

As digital environments continue to grow, digital forensics has branched into specialized fields, each with its unique methods and tools. Computer forensics (or disk forensics) analyzes computer systems to identify, preserve, and present digital evidence legally and scientifically. Tasks include file recovery, metadata and registry analysis, timeline reconstruction, keyword searching, and file carving. Challenges involve SSDs, encrypted file systems (BitLocker, FileVault, and LUKS), and distributed data across cloud and virtual environments. Tools such as EnCase, FTK, Sleuth Kit, Autopsy, and Volatility are commonly used.

Network forensics involves capturing and analyzing network traffic to detect intrusions, encompassing packet capture, session reconstruction, and protocol analysis. Encryption (TLS and VPNs) and scalability pose challenges. Mobile device forensics extracts data from phones and tablets, which can be challenging due to the variety of hardware, OS updates, encryption, and cloud sync issues.

Cloud forensics addresses investigations in virtualized, multi-tenant cloud environments, leveraging APIs and collaborating with cloud providers. IoT forensics investigates interconnected smart devices, which are challenged by limited resources, diverse data, sparse logs, and the need to collect evidence from firmware to the cloud.

Memory forensics examines volatile RAM content for running processes and malware. Database forensics inspects database integrity and audit trails to detect unauthorized changes. Emerging branches include blockchain forensics (cryptocurrency tracing), automotive forensics (vehicle data analysis), ICS/SCADA forensics (vulnerabilities in industrial control systems and supervisory control and data acquisition systems), and live forensics (the collection of volatile data).

The future of digital forensics is defined by profound transformations driven by the growing complexity and diversity of digital ecosystems. This evolution requires not only technical adaptation but also the rigorous application of scientific methodologies to guarantee the validity and reliability of forensic analyses. Empirical approaches, controlled experimentation, and statistical validation are essential to quantify accuracy and confidence, thereby strengthening the credibility of forensic findings.

The integration of artificial intelligence (AI) and machine learning (ML) presents significant opportunities to improve efficiency in file classification, anomaly detection, and behavior reconstruction from vast datasets. However, challenges related to model transparency and interpretability in legal settings must be carefully addressed. Scalability is equally critical, with big data frameworks and distributed systems playing a key role in managing the enormous volume of information in complex environments.

As cloud services and IoT devices continue to evolve, novel, empirically validated techniques are needed for effective evidence collection and preservation, particularly in light of the challenges posed by multi-tenancy and data volatility. Increasingly, organizational forensic readiness and professional training, including hands-on lab work and realistic simulations, are becoming essential components of digital forensics practice.

Ultimately, sustained collaboration between academia and investigative agencies is essential for refining tools and methodologies, ensuring they meet both operational requirements and legal standards. The convergence of forensic science, AI, cloud computing, and big data analytics will shape the discipline’s future, requiring innovations grounded in rigorous empirical methods to achieve technical excellence alongside ethical and legal compliance.

## References

1. 1.

   Agarwal, U., Rishiwal, V., Tanwar, S., Yadav, M.: Blockchain and crypto forensics: investigating crypto frauds. Int. J. Netw. Manag. **34**(2) (2024). [https://​doi.​org/​10.​1002/​nem.​2255](https://doi.org/10.1002/nem.2255)
2. 2.

   Ahmed, A.A., Farhan, K., Jabbar, W.A., Al-Othmani, A., Abdulrahman, A.G.: IoT forensics: current perspectives and future directions. Sensors **24**(16), article 5210 (2024). [https://​doi.​org/​10.​3390/​s24165210](https://doi.org/10.3390/s24165210)
3. 3.

   Al-Dhaqm, A., Razak, S., Othman, S.H.: Database forensic investigation process models: a review. IEEE Access **8**, 21310–21332 (2020)
4. 4.

   Bai, T.S., Saraswathi, V.: A systematic literature review on cloud forensics in cloud environment. Int. J. Intell. Syst. Appl. Eng. **11**(4s), 565–578 (2023)
5. 5.

   Bankole, F., Taiwo, A., Claims, I.: An extended digital forensic readiness and maturity model. Foren. Sci. Int.: Digit. Invest. **40**, article 301348 (2022). [https://​doi.​org/​10.​1016/​j.​fsidi.​2022.​301348](https://doi.org/10.1016/j.fsidi.2022.301348)
6. 6.

   Beebe, N.L., Clark, J.G.: A hierarchical, objectives-based framework for the digital investigations process. Digit. Invest. **2**(2), 147–167 (2005)<https://doi.org/10.1016/j.diin.2005.04.002>
7. 7.

   Carlini, N., Wagner, D.: Towards evaluating the robustness of neural networks. In: IEEE Symposium on Security and Privacy (S&P), pp. 39–57 (2017). [https://​doi.​org/​10.​1109/​SP.​2017.​49](https://doi.org/10.1109/SP.2017.49)
8. 8.

   Carrier, B.: A hypothesis-based approach to digital forensic investigations. Ph.D. thesis, Purdue University (2006)
9. 9.

   Carrier, B., Spafford, E.: Getting physical with the digital investigation process. Int. J. Digit. Evid. **2**(2), 20 p. (2003)
10. 10.

    Casey, E.: Digital Evidence and Computer Crime: Forensic Science, Computers and the Internet, 3rd edn. Academic, Cambridge, Massachusetts, Estados Unidos (2011)
11. 11.

    Casino, F., Dasaklis, T.K., Patsakis, C.: A systematic literature review of blockchain-based applications: current status, classification and open issues. Telemat. Inform. **36**, 55–81 (2021)<https://doi.org/10.1016/j.tele.2018.11.006>
12. 12.

    Cook, M., Marnerides, A., Johnson, C., Pezaros, D.: A survey on industrial control system digital forensics: challenges, advances and future directions. Commun. Surv. Tuts. **25**(3), 1705–1747 (2023). [https://​doi.​org/​10.​1109/​COMST.​2023.​3264680](https://doi.org/10.1109/COMST.2023.3264680)
13. 13.

    El-Kady, R.: Leveraging AI and machine learning for digital forensics. In: Ananth, C., Mittal, N. (eds.) Quantum AI and Its Applications in Blockchain Technology, pp. 215–250. IGI Global Scientific Publishing (2025). [https://​doi.​org/​10.​4018/​979-8-3373-1657-4.​ch011](https://doi.org/10.4018/979-8-3373-1657-4.ch011)
14. 14.

    Garfinkel, S.L.: Digital forensics research: the next 10 years. Digit. Invest. **7**, S64–S73 (2010)<https://doi.org/10.1016/j.diin.2010.05.009>
15. 15.

    Ghabban, F., Anwar, H., Zaman, N.: An overview of network forensic analysis tools for security. IEEE Access **9**, 123301–123321 (2021)
16. 16.

    Goodfellow, I., Shlens, J., Szegedy, C.: Explaining and harnessing adversarial examples. In: International Conference on Learning Representations (ICLR) (2015)
17. 17.

    Grispos, G., Glisson, W.B., Storer, T.: Calm before the storm: the challenges of cloud computing in digital forensics. Int. J. Digit. Crime Foren. **6**(2), 28–48 (2014)
18. 18.

    Gu, T., Dolan-Gavitt, B., Garg, S.: BadNets: identifying vulnerabilities in the machine learning model supply chain. In: IEEE International Conference on Machine Learning and Applications (ICMLA), pp. 328–333 (2017). [https://​doi.​org/​10.​1109/​ICMLA.​2017.​00-24](https://doi.org/10.1109/ICMLA.2017.00-24)
19. 19.

    Hamid, I., Rahman, M.M.H.: A comprehensive literature review on volatile memory forensics. Electronics **13**(15) (2024). [https://​doi.​org/​10.​3390/​electronics13153​026](https://doi.org/10.3390/electronics13153026)
20. 20.

    Humayed, A., Lin, J., Li, F., Luo, B.: Cyber-physical systems security—a survey. IEEE Internet Things J. **4**(6), 1802–1831 (2017)<https://doi.org/10.1109/JIOT.2017.2703172>
21. 21.

    International Organization for Standardization: ISO/IEC 17025:2017—general requirements for the competence of testing and calibration laboratories (2017). Available at: [https://​www.​iso.​org/​standard/​66912.​html](https://www.iso.org/standard/66912.html)
22. 22.

    Jain, A., Chhabra, G.S.: Anti-forensics techniques: an analytical review. In: Proceedings of the 2014 Seventh International Conference on Contemporary Computing (IC3), pp. 412–418 (2014). [https://​doi.​org/​10.​1109/​IC3.​2014.​6897209](https://doi.org/10.1109/IC3.2014.6897209)
23. 23.

    Joshi, Y.K., Tiwari, N.: A comprehensive survey on malware detection techniques. In: Proceedings of the 5th International Conference on Information Management & Machine Intelligence (ICIMMI’23), article 4 (2024). [https://​doi.​org/​10.​1145/​3647444.​3647830](https://doi.org/10.1145/3647444.3647830)
24. 24.

    Kent, K., Chevalier, S., Grance, T., Dang, H.: Guide to integrating forensic techniques into incident response. Special Publication 800-86, NIST (2012). [https://​nvlpubs.​nist.​gov/​nistpubs/​legacy/​sp/​nistspecialpubli​cation800-86.​pdf](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-86.pdf)
25. 25.

    Khanafseh, M., Qatawneh, M., Almobaideen, W.: A survey of various frameworks and solutions in all branches of digital forensics with a focus on cloud forensics. Int. J. Adv. Comput. Sci. Appl. **10**(8), 610–620 (2019)
26. 26.

    Kietzmann, J., McCarthy, I.P., Kietzmann, J.H.: Deepfakes: trick or treat. Bus. Horizons **63**(2), 135–146 (2020)<https://doi.org/10.1016/j.bushor.2019.11.006>
27. 27.

    Kishore, N., Saxena, S., Raina, P.: Big data as a challenge and opportunity in digital forensic investigation. In: Proceedings of the 2017 2nd International Conference on Telecommunication and Networks (TEL-NET), pp. 1–5 (2017). [https://​doi.​org/​10.​1109/​TEL-NET.​2017.​8343573](https://doi.org/10.1109/TEL-NET.2017.8343573)
28. 28.

    Lessard, J.P., Kessler, G.A.: Android forensics: simplifying cell phone examinations. Digit. Invest. **7**, 14–24 (2010)
29. 29.

    Lillis, D., Scanlon, M., Cross, S., Berry, R.: Current challenges and future research areas for digital forensic investigation. Digit. Invest. **17**, 35–45 (2016)
30. 30.

    Miller, T.: Explanation in artificial intelligence: insights from the social sciences. ACM Comput. Surv. **51**(5), 1–38 (2019)
31. 31.

    Mirsky, Y., Lee, W.: The creation and detection of deepfakes: a survey. ACM Comput. Surv. **54**(1), 1–41 (2021). [https://​doi.​org/​10.​1145/​3425780](https://doi.org/10.1145/3425780)<https://doi.org/10.1145/3425780>
32. 32.

    Nasrullayev, N., Ugli, H.Q.H., Valijonovich, T.O., Avlakulovich, D.M.: Static and live digital forensics, along with practical examples of tools used for each approach. Texas J. Eng. Technol. **19**, 21–27 (2023)
33. 33.

    Nath, S., Summers, K., Baek, J., Ahn, G.J.: Digital evidence chain of custody: navigating new realities of digital forensics. In: Proceedings of the 2024 IEEE 6th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA), pp. 11–20 (2024). [https://​doi.​org/​10.​1109/​TPS-ISA62245.​2024.​00012](https://doi.org/10.1109/TPS-ISA62245.2024.00012)
34. 34.

    Oliveira, E. Jr, Zorzo, A.F.: Review and agenda of digital forensics education and training. Foren. Sci. Int. **378**, 112655 (2026). [https://​doi.​org/​10.​1016/​j.​forsciint.​2025.​112655](https://doi.org/10.1016/j.forsciint.2025.112655)<https://doi.org/10.1016/j.forsciint.2025.112655>
35. 35.

    Oliveira, E. Jr, Zorzo, A.F., Neu, C.V.: Towards a conceptual model for promoting digital forensics experiments. Foren. Sci. Int.: Digit. Invest. **35**, 301014 (2020). [https://​doi.​org/​10.​1016/​j.​fsidi.​2020.​301014](https://doi.org/10.1016/j.fsidi.2020.301014)
36. 36.

    Oliveira, E. Jr, Silva, T.J., Zorzo, A.F., Neu, C.V.: Digital forensics experimentation: analysis and recommendations. Foren. Sci. Rev. **34**(1), 21–41 (2022)
37. 37.

    Palmer, G.: A road map for digital forensic research. In: First Digital Forensic Research Workshop (DFRWS) (2001)
38. 38.

    Papernot, N., McDaniel, P., Sinha, A.: A taxonomy of machine learning security challenges. In: IEEE European Symposium on Security and Privacy Workshops (EuroS&PW), pp. 60–70 (2018)
39. 39.

    Pollitt, M.: Advances in digital forensics. In: IFIP International Conference on Digital Forensics. Springer (2003)
40. 40.

    Quick, D., Choo, K.K.R.: Cloud storage forensics: ownCloud as a case study. Digit. Invest. **10**(4), 287–299 (2014)
41. 41.

    Raghavan, S.: Digital forensic research: current state of the art. CSI Trans. ICT **1**, 91–114 (2013). [https://​doi.​org/​10.​1007/​s40012-012-0008-7](https://doi.org/10.1007/s40012-012-0008-7)<https://doi.org/10.1007/s40012-012-0008-7>
42. 42.

    Reith, M., Carr, C., Gunsch, G.: An examination of digital forensic models. Int. J. Digit. Evid. **1**(3), 12 p. (2002)
43. 43.

    Scientific Working Group on Digital Evidence: Best practices for computer forensics. Foren. Sci. Commun. **1**, 11 p. (2000)
44. 44.

    Tariq, S., Lee, H., Kim, M.: Neural networks for deepfake detection: a survey. In: IEEE Conference on Multimedia Information Processing and Retrieval (MIPR), pp. 141–146 (2021)
45. 45.

    Tiwari, A., Mehrotra, V., Goel, S., Naman, K., Maurya, S., Agarwal, R.: Developing trends and challenges of digital forensics. In: Proceedings of the 2021 5th International Conference on Information Systems and Computer Networks (ISCON), pp. 1–5 (2021). [https://​doi.​org/​10.​1109/​ISCON52037.​2021.​9702301](https://doi.org/10.1109/ISCON52037.2021.9702301)

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_2>

# 2. Principles of Controlled Experimentation

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter presents the principles and practices of controlled experimentation as a foundation for empirical research in computer science and digital forensics. It introduces core concepts such as hypotheses, variables, sampling, experimental design, and threats to validity, while also covering complementary empirical methods, including case studies, surveys, systematic reviews, and benchmarking. Detailed guidance is provided on planning, conducting, analyzing, and reporting controlled experiments, emphasizing transparency, reproducibility, and statistical rigor. A key focus of the chapter is the discussion of the lack of rigor in digital forensics controlled experiments, where deficiencies in design, dataset availability, and methodological reporting limit reliability and legal admissibility. To address these challenges, the chapter highlights frameworks, standards, and open science practices that strengthen experimental rigor and cumulative knowledge. By integrating these approaches, researchers can ensure that controlled experiments contribute not only to scientific credibility but also to practical impact in both academic and professional contexts. This discussion underscores the critical role of rigor in ensuring that digital forensic evidence remains both scientifically valid and legally defensible.

## 2.1 Empirical Studies in Computer Science

Empirical studies are essential for advancing computer science, providing evidence-based insights that inform both theoretical understanding and practical application. Unlike purely theoretical approaches, empirical research in computer science involves the systematic collection and analysis of data to study computing systems, algorithms, and technologies in real-world or controlled settings. Basili and Zelkowitz have emphasized this approach [[4](#CR4)], who argue that building a scientific understanding of computing requires observation, experimentation, and model validation.

Controlled experiments, case studies, and observational studies are commonly employed to investigate phenomena such as algorithm performance, system scalability, human–computer interaction, and network behavior [[39](#CR39)]. Through these methodologies, researchers can establish causal relationships, test hypotheses, and identify patterns in complex computing environments. The rigor of empirical methods ensures that conclusions are supported by measurable evidence rather than anecdotal observations, thereby increasing the reliability of findings.

The importance of empirical research in computer science was highlighted by Denning [[10](#CR10)], who argued that experimental methods are fundamental to the discipline. He emphasized that, like other sciences, computer science must rely on empirical evidence to validate theoretical models, evaluate system behaviors, and guide technological innovations. Empirical studies thus provide a foundation for understanding computing phenomena, supporting evidence-based development, and advancing the field as a rigorous science.

### 2.1.1 Controlled Experiments

Controlled experiments are among the most rigorous and foundational empirical methods in computer science research [[4](#CR4)]. These studies involve manipulating one or more independent variables to observe their effect on dependent variables, while controlling for extraneous influences. The objective is to establish causal relationships in a controlled setting, which makes this method ideal for hypothesis testing.

In computer science, particularly in software engineering, controlled experiments are frequently used to compare programming techniques, assess the impact of tools or environments on developer productivity, measure code quality or defect rates, and process improvement [[5](#CR5)]. A key characteristic is the random assignment of participants (e.g., developers or testers) to treatment groups, which helps eliminate selection bias and enhances the study’s internal validity [[40](#CR40)].

One of the pioneering works in applying controlled experiments in software engineering is by Basili et al. [[5](#CR5)], who demonstrated how experiments could evaluate software development practices and tools. Their work emphasized repeatability and operational definitions of metrics, setting a precedent for empirical rigor in the field.

Modern controlled experiments often use automated instrumentation, version control mining, or simulated development tasks to observe participant behavior. For example, in validating the Cognitive Complexity metric, Muñoz Barón et al. [[29](#CR29)] conducted a large-scale experiment involving 427 code snippets and 24,000 developer ratings to examine whether the metric aligned with human perceptions of code complexity.

Methodological guidelines also promote the use of controlled experiments. Wohlin et al. [[41](#CR41)] provide a comprehensive framework for designing and analyzing such studies in software engineering, encompassing threat mitigation, statistical analysis, and replication practices. Figure [2.1](#Fig1) depicts such a framework.

![Flowchart illustrating the process of conducting an experiment. It begins with “Experiment Idea,” followed by sequential steps: “Experiment definition,” “Experiment planning,” “Experiment operation,” “Analysis and interpretation,” and “Presentation and package.” The process concludes with “Conclusions.” Each step is connected by arrows, indicating the flow of the process.](../images/624027_1_En_2_Chapter/624027_1_En_2_Fig1_HTML.png)

Fig. 2.1

Experimentation framework by Wohlin et al. [[41](#CR41)]

Despite their strengths, controlled experiments in computer science often face challenges, including small sample sizes, limited ecological validity, and participant bias. Nevertheless, when carefully designed and transparently reported, they offer high reliability and contribute significantly to evidence-based practice [[26](#CR26)].

### 2.1.2 Field Experiments and Quasi-experiments

Field experiments and quasi-experiments are essential methodologies in computer science research, enabling the evaluation of systems, algorithms, and technologies in real-world settings. Unlike controlled laboratory experiments, which are conducted in artificial environments with strict control over variables, field experiments are carried out in natural settings where researchers have limited control over external factors. This approach allows for observing systems under authentic conditions, providing insights that are often more generalizable and applicable to real-world scenarios. For instance, studies have utilized field experiments to assess the performance of distributed systems in operational settings, revealing behaviors and challenges that may not emerge in controlled environments [[39](#CR39)].

Quasi-experiments, on the other hand, are employed when random assignment to treatment and control groups is not feasible. These designs allow researchers to infer causal relationships by exploiting naturally occurring variations or interventions. In computer science, quasi-experimental methods have been utilized to evaluate the impact of software updates, changes in system configurations, or the introduction of new technologies without the constraints of randomization. Such approaches are particularly valuable in large-scale systems where randomization is impractical or unethical [[21](#CR21)].

Both field experiments and quasi-experiments contribute significantly to the empirical foundation of computer science by providing evidence of how systems perform and behave outside of controlled settings. They enable researchers to validate models, test hypotheses, and refine theories based on real-world data. As the field continues to evolve, integrating these empirical methods is essential for developing robust, reliable, and user-centric computing solutions [[39](#CR39)].

### 2.1.3 Case Studies

Case studies are a widely used empirical method in computer science for investigating phenomena in their real-world context. Unlike controlled experiments, which manipulate variables under strict conditions, case studies focus on the detailed, in-depth examination of computing systems, algorithms, or technologies in their natural environments. This method allows researchers to explore complex interactions, uncover hidden patterns, and gain insights into system behaviors that are difficult to reproduce in laboratory settings [[4](#CR4), [43](#CR43)].

Case studies are particularly valuable when studying large-scale or distributed systems, emerging technologies, or computational infrastructures where controlled experiments may be impractical or infeasible. They provide rich qualitative and quantitative data that supports model validation, algorithm refinement, and system performance assessment. Additionally, case studies can incorporate multiple data sources, such as logs, user interactions, system metrics, and documentation, to triangulate findings and increase the robustness of conclusions [[35](#CR35)].

The strength of case studies lies in their ability to strike a balance between depth and context, offering insights that general surveys or experiments may overlook. In computer science research, case studies complement other empirical approaches by providing evidence of real-world applicability, guiding experimental design, and informing theoretical development. By capturing the complexity and variability inherent in operational systems, case studies contribute significantly to evidence-based decision-making and the advancement of computing knowledge [[4](#CR4)].

It is worth noting that case studies are qualitative but may include quantitative aspects. Robert Yin [[43](#CR43)] mentions this point in his book (latest edition). An example can be found in the work by L’Erário et al. [[27](#CR27)].

### 2.1.4 Surveys and Interviews

Surveys and interviews are cornerstone empirical methods in computer science research, widely used to investigate phenomena related to human interaction with technology, adoption of computing tools, and decision-making processes. Surveys, often structured questionnaires, enable researchers to collect quantitative data from large populations, allowing statistical analysis of trends, correlations, and patterns. They are particularly effective for measuring attitudes, perceptions, behaviors, or self-reported practices in computing contexts. Interviews, in contrast, are generally semi-structured or unstructured, providing rich qualitative insights into participants’ experiences, motivations, and contextual factors. By allowing participants to elaborate on their responses, interviews can reveal subtleties and nuances that purely quantitative instruments may miss [[23](#CR23), [31](#CR31)].

In computer science, these methods are extensively applied in domains such as human–computer interaction, cybersecurity, artificial intelligence, networked systems, and cloud computing. Surveys can capture large-scale information about system adoption, usage patterns, and user preferences. At the same time, interviews provide a deeper understanding of why users behave in specific ways, how they interact with computing environments, and what barriers they encounter in adopting new technologies. For example, surveys may reveal trends in the usage of AI-powered applications across organizations, whereas interviews can elucidate challenges related to interpretability, trust, and integration of these systems [[13](#CR13), [38](#CR38)]. This combination of quantitative and qualitative data supports a comprehensive understanding of complex phenomena in computing systems.

Methodological rigor in surveys and interviews is critical to computer science research. Survey design requires careful attention to question phrasing, response scales, sampling strategies, and response rates to ensure data validity and reliability. Interviews require well-prepared protocols, skilled interviewers, and systematic coding of responses to identify themes and insights. Triangulation, combining surveys and interviews, enhances the credibility of findings by corroborating quantitative trends with qualitative explanations. Moreover, these methods are invaluable for validating theoretical models, assessing usability, evaluating algorithms from a user perspective, and guiding system design decisions in ways that controlled experiments alone cannot achieve [[35](#CR35)].

Surveys and interviews also facilitate evidence-based policy and decision-making in computing domains. By collecting empirical data from practitioners, users, or stakeholders, researchers can inform the development of standards, best practices, and design guidelines. In emerging fields such as Internet of Things (IoT), edge computing, and collaborative AI systems, these methods provide insight into real-world constraints, user needs, and adoption challenges, complementing technical evaluations with human-centered perspectives. Ultimately, surveys and interviews bridge the gap between system performance metrics and users’ lived experiences, ensuring that computing research is both technically rigorous and socially relevant [[13](#CR13), [23](#CR23), [31](#CR31)].

Therefore, surveys and interviews are indispensable empirical tools in computer science, offering both breadth and depth in data collection. They enable researchers to capture large-scale quantitative trends while simultaneously understanding the rich qualitative context in which computing technologies operate. Their application across diverse domains ensures that computer science research not only advances technological innovation but also aligns with users’ needs, behaviors, and experiences in real-world environments.

### 2.1.5 Systematic Literature Reviews and Meta-analyses

Systematic Literature Reviews (SLRs) and meta-analyses are rigorous empirical methods that synthesize existing research to provide a comprehensive understanding of a particular domain in computer science. Unlike traditional narrative reviews, SLRs follow a structured protocol that defines explicit research questions, inclusion and exclusion criteria, and systematic search strategies across multiple databases. This approach ensures transparency and replicability and minimizes bias when summarizing the body of evidence [[22](#CR22), [34](#CR34)].

SLRs are widely used in computer science to identify trends, gaps, and evidence-based insights across diverse areas such as machine learning, network security, cloud computing, and distributed systems. By systematically evaluating the quality, relevance, and findings of primary studies, researchers can establish the current state of knowledge, inform theoretical frameworks, and guide future research directions. Furthermore, SLRs provide a foundation for designing experiments, field studies, or surveys by highlighting proven methodologies and unresolved challenges [[7](#CR7), [41](#CR41)].

Meta-analysis complements SLRs by statistically aggregating quantitative results from multiple studies to estimate effect sizes, performance improvements, or correlations across independent investigations. This method enables more precise conclusions than those drawn from individual studies alone and helps resolve conflicting results in the literature. In computer science, meta-analyses have been applied to evaluate algorithmic performance, benchmark outcomes in distributed systems, and assess the impact of various computing interventions on system efficiency or usability. Together, SLRs and meta-analyses provide robust, evidence-based syntheses that strengthen the scientific foundation of computer science research [[24](#CR24), [41](#CR41)].

### 2.1.6 Benchmarking and Performance Evaluations

Benchmarking and performance evaluations are essential empirical methods in computer science, used to systematically measure and compare the efficiency, scalability, and effectiveness of algorithms, computing systems, and networked infrastructures. Benchmarks provide standardized tasks or datasets that allow researchers to evaluate system behavior under controlled or semi-controlled conditions. Performance evaluations, in turn, quantify metrics such as execution time, throughput, latency, resource utilization, and energy consumption, enabling objective comparisons among alternative solutions [[1](#CR1), [11](#CR11)].

These methods are widely applied across various domains of computing, including high-performance computing, cloud computing, distributed systems, database management, and artificial intelligence. Benchmarking allows researchers to understand the limits of computational platforms, identify bottlenecks, and optimize resource allocation. For example, in machine learning and AI, standardized datasets such as ImageNet or GLUE serve as benchmarks to evaluate model accuracy, training efficiency, and generalization capabilities. Similarly, in networked systems, benchmarks can simulate realistic traffic patterns to assess throughput, latency, and fault tolerance under operational conditions [[11](#CR11), [17](#CR17)].

Performance evaluations complement benchmarking by providing a more comprehensive assessment of system behavior under varying workloads and configurations. Researchers often employ stress testing, load testing, and profiling techniques to observe system performance in realistic operational environments. The insights gained from these evaluations inform design decisions, optimization strategies, and technology selection, ensuring that computing systems meet desired performance, reliability, and efficiency standards. Together, benchmarking and performance evaluation constitute critical tools for evidence-based assessment, enabling reproducible, comparable, and transparent empirical studies in computer science [[1](#CR1), [17](#CR17)].

### 2.1.7 Ethnographies and Experience Sampling

Ethnographies and experience sampling are qualitative empirical methods increasingly used in computer science to study human interactions with computing systems in real-world contexts. Ethnography involves immersive observation and detailed documentation of users’ practices, workflows, and social interactions as they engage with technology over extended periods. This method provides rich, contextual insights into how computing systems are adopted, integrated, and adapted in everyday settings, revealing subtleties that quantitative metrics alone may overlook [[6](#CR6), [9](#CR9)].

Experience sampling complements ethnographic methods by capturing user behavior, perceptions, and experiences in situ through self-reports at regular or event-triggered intervals. This approach enables researchers to collect real-time, ecological data on how users interact with software, hardware, or networked systems, thereby minimizing the recall bias inherent in retrospective interviews or surveys. Experience sampling has been effectively applied in studying user engagement with mobile applications, collaborative tools, and AI-powered interfaces, providing fine-grained temporal insights into usability, workload, and satisfaction [[3](#CR3), [14](#CR14)].

Together, ethnographies and experience sampling offer complementary perspectives: Ethnography provides deep contextual understanding and interprets user practices, while experience sampling yields quantitative and temporal data about user interactions and experiences. In computer science research, these methods are invaluable for informing the design of human-centered systems, validating interface models, and identifying gaps between intended and actual use. By integrating qualitative and quantitative insights, researchers can produce more holistic and actionable evidence to guide system design, policy decisions, and technological innovation [[6](#CR6), [9](#CR9), [14](#CR14)].

## 2.2 Controlled Experimentation in a Nutshell

This section provides an introduction to the planning, conducting, analyzing, and reporting of controlled experiments.

### 2.2.1 Types of Controlled Experiments

As shown in Sect. [2.1](#Sec1), controlled experiments are of various types, as follows.

Laboratory Experiments

Laboratory experiments are conducted in highly controlled environments where researchers can precisely manipulate variables and monitor outcomes. These experiments are commonly used to evaluate algorithms, assess system performance, or measure the effectiveness of specific computing techniques under repeatable conditions. Laboratory experiments provide high internal validity, allowing for rigorous testing of hypotheses and reproducibility of results, although their external validity may be limited due to the artificial setting [[4](#CR4)].

Field Experiments

Field experiments extend controlled experimentation into real-world settings, where systems or algorithms are deployed in operational environments. By observing performance under authentic conditions, field experiments offer higher external validity and reveal challenges that may not arise in laboratory contexts, such as environmental variability, user behavior, and system interactions. Field experiments are particularly relevant in networked systems, distributed computing, and high-performance computing, where deployment context can significantly influence outcomes [[39](#CR39)].

Quasi-experiments

Quasi-experiments are employed when random assignment to treatment and control groups is impractical or impossible. Researchers exploit naturally occurring interventions, system updates, or configuration changes to infer causal effects. Although quasi-experiments may have lower internal validity than fully randomized experiments, they are valuable for evaluating large-scale systems or operational deployments, where complete control over experimental conditions is not feasible [[21](#CR21)].

Between-Subjects and Within-Subjects Designs

Controlled experiments can also be classified based on how participants or system instances are assigned to conditions. In between-subjects designs, different groups are exposed to other treatments, reducing the risk of learning or carryover effects. Within-subjects designs involve the same participants or system instances experiencing all experimental conditions, thereby improving statistical power but requiring careful counterbalancing to mitigate order effects. Both designs are widely used in performance evaluations, algorithm comparisons, and human–computer interaction studies [[4](#CR4), [41](#CR41)].

By carefully selecting the appropriate type of controlled experiment, researchers can balance the trade-offs between internal and external validity, reproducibility, and practical feasibility. Understanding these types enables rigorous experimental design, ensuring that empirical studies in computer science yield reliable, generalizable, and actionable insights. Therefore, Table [2.1](#Tab1) summarizes the types of controlled experiments in computer science.

Table 2.1

Summary of types of controlled experiments in computer science

| Type | Description | Advantages | Limitations |
| --- | --- | --- | --- |
| **Laboratory experiments** | Conducted in highly controlled settings where variables can be precisely manipulated | High internal validity; reproducibility; precise measurement of variables | Low external validity; may not reflect real-world conditions; limited contextual insights |
| **Field experiments** | Conducted in real-world environments where systems or algorithms are deployed under operational conditions | High external validity; captures real-world behavior and environmental effects | Lower control over confounding factors; more complex setup; possible variability in results |
| **Quasi-experiments** | Interventions occur without random assignment; researchers exploit naturally occurring changes or system updates | Feasible for large-scale or operational systems; can study practical interventions | Lower internal validity; potential for confounding variables; causal inference is less robust |
| **Between-subjects design** | Different groups experience different treatments | Reduces learning or carryover effects; clear comparison between groups | Requires larger sample sizes; potential group differences may bias results |
| **Within-subjects design** | Same participants or system instances experience all experimental conditions | Higher statistical power; fewer participants needed; controls for individual differences | Risk of order or carryover effects; requires careful counterbalancing |

### 2.2.2 Planning a Controlled Experiment

The planning phase of controlled experiments in computing is vital to ensuring methodological rigor and trustworthy results. At the outset, researchers clearly define the problem under investigation and formulate precise, testable research questions and hypotheses. These hypotheses must be directly linked to measurable outcomes, forming a solid foundation for the experimental work [[39](#CR39)].

A central task in planning is the careful selection of experimental factors and treatments that reflect relevant aspects of computing systems, algorithms, or processes [[41](#CR41)]. Equally important is identifying dependent variables and reliable measurement instruments to assess dimensions such as performance, accuracy, scalability, or usability. These instruments must be valid to ensure that the captured data truly represents the phenomena being investigated.

Choosing appropriate experimental subjects, either human participants (e.g., for usability or productivity studies) or computational systems (e.g., algorithm assessment, architecture evaluation, or distributed environments), is essential. Matching these to realistic conditions strengthens the external validity of the findings.

Designing the experimental structure is another crucial step: Researchers must decide between between-subjects, within-subjects, or mixed designs, while incorporating replication, randomization, and other control mechanisms to mitigate bias and confounding effects [[2](#CR2)]. In computing, environmental variables, such as hardware configurations, software versions, or network conditions, must be carefully specified, since minor variations can significantly influence outcomes.

Comprehensive documentation of planning decisions is indispensable. A detailed experimental protocol not only enhances repeatability and transparency but also facilitates evaluation and comparison across studies.

Main steps of the planning phase include [[39](#CR39)]:

* Defining research questions and testable hypotheses
* Selecting factors, treatments, and experimental units
* Identifying dependent variables and valid measurement instruments
* Choosing representative participants or systems
* Designing the experiment (e.g., between-subjects, within-subjects, or mixed design)
* Planning for randomization, replication, and controlling confounding variables
* Specifying environmental settings (hardware, software, and network)
* Developing and thoroughly documenting a detailed experimental protocol

An emerging practice that enhances the rigor and transparency of the planning phase is the use of Registered Reports [[30](#CR30)]. In this type of study, the experimental design, hypotheses, and analysis plan are peer-reviewed and accepted in principle by a journal before data collection begins. This shifts the focus from the results to the quality of the methodology, reducing risks of publication bias, selective reporting, and questionable research practices.

For controlled experiments in computing, adopting Registered Reports means that key planning decisions, such as defining research questions, selecting factors and treatments, identifying dependent variables, and specifying the experimental design, must be fully articulated and justified before execution. Reviewers provide feedback at this early stage, allowing researchers to refine the study protocol and strengthen its validity before resources are invested in data collection [[12](#CR12)].

Integrating Registered Reports into the planning phase also supports reproducibility: Once the protocol is publicly available, other researchers can replicate or extend the experiment under comparable conditions. Moreover, it aligns with the principles of Open Science by making the research process more transparent and accountable.

Thus, Registered Reports serve as a powerful complement to traditional planning activities, ensuring that experiments are not only well-designed but also documented, validated, and communicated in ways that maximize their scientific contribution. Plenty of computing exemplary Registered Reports can be found at [https://​rr.​peercommunityin.​org/​PCIRegisteredRep​orts](https://rr.peercommunityin.org/PCIRegisteredReports) and [https://​osf.​io](https://osf.io).

Table [2.2](#Tab2) summarizes such planning phases and provides randomly exemplary statements for each phase.

Table 2.2

Main phases of the planning stage in controlled experiments, with exemplary statements

| Phase | Description | Exemplary statement |
| --- | --- | --- |
| Definition of objectives | Formulate research questions and hypotheses that are precise, testable, and aligned with the study’s goals | “The experiment aims to evaluate whether Algorithm A reduces execution time compared to Algorithm B in large-scale graph datasets” |
| Selection of factors and treatments | Choose independent variables, treatments, and experimental units relevant to the computing context | “Two factors will be varied: (i) the type of algorithm (A vs. B) and (ii) dataset size (small, medium, large)” |
| Identification of response variables | Define dependent variables and valid measurement instruments to assess performance, accuracy, usability, or scalability | “Execution time (in seconds) and memory usage (in MB) will be measured as dependent variables using automated benchmarking scripts” |
| Choice of subjects or systems | Select participants (human or computational systems) representative of the target context to strengthen external validity | “The experiment will be run on benchmark datasets from the DIMACS collection and validated using three hardware configurations representative of commodity servers” |
| Experimental design | Decide between between-subjects, within-subjects, or mixed designs, incorporating randomization, replication, and counterbalancing | “A within-subjects design will be used, where each algorithm is tested on all dataset sizes, with randomization of execution order to minimize bias” |
| Control of environment | Specify hardware, software, and network settings to ensure stability and minimize confounding effects | “All experiments will be executed on the same Linux distribution, with fixed versions of compilers and libraries, and under identical hardware conditions (Intel Xeon, 64 GB RAM)” |
| Protocol documentation | Develop a detailed experimental protocol to enhance reproducibility, transparency, and comparability | “The full experimental setup, including scripts, datasets, and configuration files, will be documented in a public repository to enable replication” |
| Registered Report preparation | Submit the preregistered protocol for peer review before data collection to secure provisional acceptance and reduce bias. | “The experimental protocol, including hypotheses, methods, and planned analyses, will be submitted as a Registered Report to ensure transparency and pre-approval by reviewers” |

Effective planning ensures that computing experiments are structured, reliable, and capable of producing meaningful and actionable contributions to both research and practice.

### 2.2.3 Conducting a Controlled Experiment

The conduction of a controlled experiment in Computer Science is the stage in which the experimental design is executed in practice. While planning defines objectives and methods, execution ensures these plans are implemented rigorously and consistently. Even minor deviations during execution can compromise validity and reliability [[41](#CR41)].

The following checklist provides a structured set of steps for conducting controlled experiments properly.

Prepare the Environment

The experimental environment must be identical across all participants, except for the treatment under study. For example, in an experiment comparing JUnit and TestNG, each participant’s workstation should contain the same project code and libraries, differing only in the installed testing framework. In HCI studies, the same devices, screen resolutions, and input methods should be used to eliminate environmental bias [[37](#CR37)].

Deliver Standardized Instructions

All participants must receive the exact instructions, either via a written handout, scripted text, or a prerecorded tutorial. For instance, in an experiment evaluating debugging tools, participants may first receive a 10-minute standardized training video explaining the tool’s basic features, followed by a fixed written task description. This ensures that differences in outcomes are due to the treatment, not the way instructions were delivered [[20](#CR20)].

Assign Participants to Treatments

Participants should be assigned to groups according to the experimental design (randomization, blocking, or matching). For example, in a study comparing two refactoring tools, participants can be randomly assigned to Tool A or Tool B. If both students and professionals participate, blocking may be used to ensure that each group is evenly distributed across treatments [[41](#CR41)].

Execute the Tasks

Participants perform the assigned tasks under controlled conditions. Tasks must be realistic yet feasible. In a debugging experiment, participants might be asked to locate seeded defects in a 500- to 800-line codebase. In a programming language experiment, they could be tasked with implementing a sorting algorithm using the language-specific constructs for each language version. The researcher supervises silently, intervening only for technical issues or protocol violations [[37](#CR37)].

Monitor and Collect Data

Data should be gathered unobtrusively using automated tools. In software engineering experiments, IDE plug-ins can log time spent on files, compilation errors, and command usage. In HCI studies, screen recording and keystroke logging can capture user interactions. Monitoring ensures participants follow the procedure while reducing experimenter influence [[36](#CR36)].

Manage Time and Control Conditions

All participants should have the same time limits and work in comparable environments. For instance, in defect detection experiments, each subject may be given 60 minutes to find and record as many defects as possible. Conducting sessions in quiet rooms with uniform seating and lighting further reduces variability [[41](#CR41)].

Handle Unexpected Events Consistently

Protocols must be in place for addressing technical failures or participant issues. For example, if an IDE crashes, the session should be restarted from a preconfigured checkpoint. If a participant requests clarification, researchers must provide the same prewritten response to avoid providing unequal assistance. Consistency prevents the introduction of uncontrolled variation [[37](#CR37)].

Close the Session

Once tasks are complete, participants may be asked to complete post-task questionnaires, such as those that assess perceived ease of use or satisfaction with a tool. However, detailed debriefing must be postponed until all sessions finish, to prevent contamination. At closure, all data are stored securely and linked to the correct treatment group [[20](#CR20)].

Table [2.3](#Tab3) summarizes the conducting steps of an experiment.

Table 2.3

Steps for conducting controlled experiments in computer science with elaborated examples

| Step | Description | Examples |
| --- | --- | --- |
| Prepare the Environment | Ensure all participants work under identical conditions, except for the factor being studied | In an experiment comparing JUnit and TestNG, all workstations are set up with the same version of the Java Development Kit (JDK), identical Eclipse IDE installations, and the same project source code. The only difference between groups is the installed testing framework. In HCI experiments evaluating mobile authentication methods, each participant uses the same smartphone model, configured with identical operating system versions, brightness, and input settings, differing only in the authentication method (PIN vs. biometric) |
| Deliver standardized instructions | Provide uniform information to all participants to avoid bias | In a debugging tool evaluation, every participant watches a prerecorded 10-minute tutorial video that demonstrates the tool’s basic features. In a code comprehension study, participants receive a printed task sheet that describes the objectives, rules, and expected outputs, ensuring that experimenters do not provide any extra clarifications that could unintentionally guide some participants more than others |
| Assign participants to treatments | Allocate subjects to groups according to design (randomization, blocking, matching) | In a study comparing two code refactoring tools, developers are randomly assigned to use Tool A or Tool B. Suppose both undergraduate students and professional developers are included in the sample. In that case, a blocking design ensures that each group contains an equal proportion of students and professionals, thereby reducing the risk of experience-level bias. In some cases, pretests (e.g., a short coding quiz) are used to match participants of similar skill levels before assigning them to treatments. |
| Execute the tasks | Participants perform realistic yet feasible tasks under supervision | In a defect detection experiment, participants are asked to find seeded bugs in a 600-line program, with tasks carefully designed to be challenging yet achievable within the session. In a programming language comparison, subjects implement a sorting algorithm in both Python and Java, focusing on how language-specific constructs affect task performance. Experimenters observe silently, intervening only in case of technical issues or rule violations |
| Monitor and collect data | Record performance unobtrusively to minimize interference | In a software testing experiment, IDE plug-ins automatically log compilation attempts, test execution results, and time spent on files. In an HCI usability study, a combination of keystroke logging, screen recording, and eye-tracking software captures user interactions without distracting participants. Data is securely stored on a centralized server for later analysis, ensuring traceability and consistency |
| Manage time and control conditions | Apply equal time limits and consistent settings across participants | In a defect detection task, each participant is given exactly 60 minutes to identify as many defects as possible. The experiment is conducted in quiet laboratory rooms, with identical lighting conditions, seating arrangements, and noise levels. To further ensure fairness, participants use noise-canceling headphones so that unexpected external sounds do not affect concentration differently across sessions |
| Handle unexpected events consistently | Apply predefined protocols for crashes, interruptions, or clarification requests | If the IDE crashes during the task, the workstation is restored from a virtual machine snapshot to ensure participants resume from the same checkpoint. If participants ask for clarification (e.g., “what does this task mean?”), the experimenter provides a prewritten, identical response to all, avoiding unequal assistance. If internet connectivity fails, local offline copies of all required resources are used, ensuring consistency across sessions |
| Close the session | Securely store data and conduct post-task procedures without contaminating other sessions | After finishing the task, participants complete a standardized post-task questionnaire that measures perceived difficulty, tool usability, and satisfaction. All log files, videos, and questionnaires are anonymized and stored in encrypted repositories. A debriefing session explaining the study’s purpose and hypotheses is conducted only after all participants have completed their sessions, ensuring that no early participant unintentionally influences later ones |

Conducting a controlled experiment in computer science involves more than simply running tasks; it is a highly structured process that requires standardization, careful monitoring, and consistency at every step. By preparing identical environments, delivering standardized instructions, rigorously assigning participants, executing realistic tasks, monitoring unobtrusively, managing time, and handling unexpected events consistently, researchers ensure that the execution phase strengthens the validity of their experiments.

### 2.2.4 Analyzing and Interpreting Results of a Controlled Experiment

The analysis and interpretation of results from controlled experiments in computer science are crucial to ensure that the observed effects are genuine, meaningful, and not confounded. While the conduction phase guarantees the proper execution of the experiment, the analysis phase focuses on making sense of the collected data, identifying patterns, and drawing valid conclusions [[25](#CR25), [41](#CR41)].

The following checklist provides a structured set of steps for analyzing and interpreting experimental results.

Verify Data Integrity

Before performing any analysis, ensure that all collected data is complete, accurate, and free from recording errors. For example, in a software testing experiment, confirm that IDE plug-ins correctly logged all defects found, compilation times, and edits. In an HCI usability study, verify that screen recordings, keystrokes, and eye-tracking logs are fully captured and synchronized [[37](#CR37)].

Choose Appropriate Statistical Methods

Select statistical tests that match the experimental design and type of data. For instance, use a paired t-test to compare defect detection rates before and after introducing a new tool or ANOVA to compare multiple groups using different debugging frameworks. When data distributions are non-normal, nonparametric tests such as the Mann–Whitney U test may be more suitable [[16](#CR16), [20](#CR20)].

Compute Effect Sizes

Measure the magnitude of observed differences to complement statistical significance. For example, in a code comprehension study, calculate Cohen’s d to quantify the performance difference between two tools. In a debugging experiment, compute the percentage increase in defects found per hour to evaluate practical relevance [[25](#CR25), [41](#CR41)].

Visualize Data

Use plots and charts to explore patterns, trends, and outliers. In HCI usability studies, box plots can highlight variations in task completion times across authentication methods, while scatter plots may reveal correlations between user experience and error rates. Heatmaps can visualize sections of code where participants made the most mistakes, providing further insight into performance differences [[16](#CR16), [36](#CR36)].

Interpret Results in Context

Relate the findings to the research questions, hypotheses, and prior literature. For instance, if a new refactoring tool introduces fewer bugs, compare this outcome with previous studies to evaluate alignment or discrepancies. In usability studies, interpret observed error rates in light of previously reported challenges with input modalities [[20](#CR20), [25](#CR25)].

Table [2.4](#Tab4) summarizes the key steps for analyzing and interpreting results in controlled experiments, including suggested tools.

Table 2.4

Steps for analyzing and interpreting results in controlled experiments in computer science with elaborated examples and suggested tools

| Step | Description | Examples | Suggested tools |
| --- | --- | --- | --- |
| Verify data integrity | Ensure all collected data is complete and accurate before analysis | In a software testing experiment, verify that IDE plug-ins correctly logged all defect findings, compilation times, and edits. Check for missing timestamps, duplicate entries, or mislogged participant IDs. In an HCI usability study, ensure that screen recordings, keystrokes, and eye-tracking logs are fully captured and synchronized | Python (pandas), R (data.table), Excel, Git-based logging systems |
| Choose statistical methods | Select appropriate statistical tests based on data type and experimental design | Use paired t-tests to compare the number of defects found by participants before and after introducing a new static analysis tool. Apply ANOVA to compare completion times for multiple groups using different code review techniques. Use nonparametric tests, such as the Mann–Whitney U test, when the data distributions are non-normal | R (stats package), Python (SciPy, statsmodels), SPSS, JMP |
| Compute effect sizes | Measure the magnitude of differences to complement statistical significance | In a code comprehension study, calculate Cohen’s d to quantify the performance gap between Tool A and Tool B. In a debugging experiment, compute the percentage increase in defects found per hour to assess practical significance beyond p-values | R (effsize package), Python (Pingouin, statsmodels), Excel |
| Step | Description | Examples | Suggested tools |
| Visualize data | Use charts and plots to identify patterns, trends, and outliers | Create box plots of task completion times across authentication methods in a mobile HCI study to identify variations and outliers. Use scatter plots to explore correlations between developer experience and defect detection rate in a testing experiment. Heatmaps can visualize areas of code where participants made the most mistakes | Python (Matplotlib, Seaborn), R (ggplot2, lattice), Tableau, PowerBI |
| Interpret results in context | Relate findings to research questions, hypotheses, and prior literature | If participants using a new refactoring tool introduce fewer bugs, compare this effect with previous studies on similar tools. In a usability study, interpret higher error rates with biometric authentication in light of prior work on input modality challenges. Consider theoretical frameworks to explain observed behaviors | Reference managers (Zotero, Mendeley), LaTeX, Jupyter Notebook, RMarkdown |
| Assess confounding variables | Identify factors that may unintentionally influence results | Evaluate whether differences in experience, programming language familiarity, or IDE proficiency affected outcomes in a debugging study. Control for time of day, environmental distractions, or software version differences in the analysis | R (car package), Python (Pingouin, statsmodels), Excel |
| Evaluate practical significance | Determine whether statistically significant differences are meaningful in practice | In a test automation experiment, even if one tool leads to 2% faster test execution with statistical significance, assess whether this translates into noticeable productivity gains. In a code review experiment, slight differences in review time may not justify switching tools in a production environment | R, Python, Excel, Tableau |
| Document interpretation | Record the rationale behind interpretations, assumptions, and limitations | Clearly note any excluded outliers, reasons for data transformations, or deviations from planned analysis. Document whether confounders were considered and how they were handled. For example, explain why novice participants were excluded from the final analysis or how missing data were imputed | Jupyter Notebook, RMarkdown, LaTeX, Git |

Analyzing and interpreting results require rigor, careful attention to potential biases, and contextual understanding. Following structured steps ensures that conclusions drawn from controlled experiments are both valid and meaningful in empirical software engineering.

### 2.2.5 Reporting a Controlled Experiment

Reporting the results of a controlled experiment in computer science is a critical phase that ensures the findings are communicated clearly, transparently, and reproducibly. While analysis and interpretation provide insights, proper reporting enables the scientific community to understand, validate, and build on the results [[25](#CR25), [41](#CR41)].

Effective reporting requires a structured approach that addresses key elements, including the experimental design, the analysis methods used, the interpretation of results, and the practical implications. The following checklist provides a structured set of steps for reporting controlled experiments.

Present the Research Questions and Hypotheses

Clearly restate the research questions and hypotheses to provide context for the results. For example, in an experiment comparing two code refactoring tools, the hypothesis might be that Tool A reduces the number of defects introduced compared to Tool B. Explicitly stating these elements ensures readers understand the objectives before interpreting the results [[37](#CR37)].

Describe the Experimental Setup and Conditions

Summarize the experiment’s methodology, including participant characteristics, task descriptions, and controlled conditions. For instance, in a debugging study, report the programming languages used, the size and type of codebase, the IDE configuration, and how participants were assigned to groups. This information allows other researchers to assess the validity and reproducibility of the findings [[20](#CR20)].

Report Data Analysis Methods

Explain the statistical tests, effect size measures, and visualization techniques employed. For example, in a code comprehension study, it is stated that ANOVA was used to compare completion times across three tools, with post hoc Tukey tests for pairwise comparisons. Include rationale for using nonparametric methods if assumptions of normality were violated [[16](#CR16), [25](#CR25)].

Present Results Clearly

Use tables, graphs, and charts to summarize findings. Box plots can show the distribution of task completion times, scatter plots can highlight correlations between experience and performance, and bar charts can present defect counts across treatments. Include confidence intervals and effect sizes to provide both statistical and practical insights [[36](#CR36)].

Interpret the Results

Discuss the results in the context of the hypotheses, research questions, and prior literature. For instance, if Tool A significantly reduces defects compared to Tool B, interpret whether this difference is meaningful in real-world software development. Consider potential confounding factors such as participant experience, environment, or task difficulty [[41](#CR41)].

Discuss Limitations and Threats to Validity

Acknowledge any limitations of the experiment that could influence the results. For example, a small sample of professional developers or a restricted codebase may limit generalizability. Report how threats to internal, external, construct, and conclusion validity were addressed [[20](#CR20)].

Provide Practical Implications

Explain how the findings can inform software engineering practice or guide further research. For instance, highlight how adopting Tool A could reduce debugging time in educational or industrial settings, or suggest improvements in tool design based on observed limitations [[25](#CR25)].

Ensure Transparency and Reproducibility

Include all relevant details that allow others to reproduce the experiment, such as task descriptions, datasets, analysis scripts, and configurations. Consider using repositories or supplementary materials to make this information accessible [[36](#CR36), [37](#CR37)].

Table [2.5](#Tab5) presents the main steps to report a controlled experiment.

Table 2.5

Steps for reporting controlled experiments in computer science with detailed examples

| Step | Description | Examples |
| --- | --- | --- |
| Present research questions | Restate research questions and hypotheses to contextualize results | For a study comparing two refactoring tools, explicitly state that the hypothesis is “Tool A reduces the number of defects introduced during refactoring compared to Tool B.” Include secondary hypotheses such as “Tool A decreases the average time to complete refactoring tasks,” and clarify which metrics will be evaluated (defects per KLOC, task duration, code readability scores) |
| Describe experimental setup | Summarize participant demographics, tasks, conditions, and group assignments | Report that 30 participants were included, with 15 professional developers and 15 undergraduate students. Describe the tasks, such as refactoring 500 lines of legacy code, debugging a 600-line program, or implementing a sorting algorithm. Specify group allocation (e.g., random assignment to Tool A or Tool B), IDE versions, operating system, library versions, and any preexperiment training provided to ensure participants were equally prepared |
| Report data analysis methods | Explain statistical tests, effect sizes, and visualization methods | Detail the use of one-way ANOVA to compare task completion times across three tools, with post hoc Tukey tests to evaluate pairwise differences. For defect counts, use nonparametric tests, such as the Mann–Whitney U test, if the data is not normally distributed. Report effect sizes using Cohen’s d or Hedge’s g to quantify practical relevance. Mention any data transformations, outlier removal, or handling of missing data |
| Present results clearly | Use tables, charts, and graphs to summarize findings | Include a box plot showing the distribution of task completion times for each tool, highlighting the median, quartiles, and outliers. Use scatter plots to correlate participant experience with defect detection rates. Present bar charts of the total number of defects detected per tool. For HCI studies, include heatmaps showing which areas of the interface users most frequently made errors or spent the most time |
| Interpret results | Discuss results in relation to hypotheses, research questions, and prior work | Explain why participants using Tool A introduced fewer defects and completed tasks faster, considering the usability features and automation support in the tool. Compare results to previous studies on similar refactoring tools. Discuss unexpected findings, such as why more experienced developers performed similarly with both tools, possibly due to prior familiarity with refactoring patterns |
| Discuss limitations | Acknowledge limitations and threats to validity | Note the small sample size of professional developers may limit generalizability. Discuss restricted codebases (e.g., only Java programs or specific legacy code) that may not reflect broader software systems. Mention potential confounding variables, such as differences in participants’ familiarity with IDEs or programming languages. Explain how internal, external, construct, and conclusion validity were considered |
| Provide practical implications | Explain real-world relevance of results | Highlight that adopting Tool A could reduce debugging time in educational courses or industry projects. Suggest improvements to tool design, such as enhanced visualization of code dependencies or automated refactoring suggestions. Discuss implications for training, workflow integration, and tool selection policies |
| Ensure transparency | Include all details for reproducibility: data, scripts, task descriptions, configurations | Provide anonymized participant datasets, task instructions, IDE and library versions, and analysis scripts in a public repository. Include all raw data logs, pre- and post-task questionnaires, and any preprocessing steps taken. Explain clearly how missing or corrupted data was handled, so that other researchers can replicate the study precisely |

## 2.3 The Lack of Rigorousness in Digital Forensics Controlled Experiments

The evolution of Digital Forensics (DF) as a scientific discipline depends critically on the robustness of its empirical evidence base, a point underscored in both methodological analyses and community calls for greater experimental rigor [[8](#CR8), [15](#CR15)]. Controlled experiments, when carefully designed and executed, provide the strongest means of establishing causal relationships and evaluating the reliability of tools and methods. Yet a growing body of literature demonstrates that many DF studies fall short of the methodological standards of other areas of computer science experimentation. This lack of rigor undermines not only the credibility of research but also its admissibility and probative value in legal settings, where forensic evidence must withstand scrutiny under established standards such as Daubert or Frye.

Recent secondary studies of experimentation practices in DF highlight systemic weaknesses. Oliveira Jr et al. document that in Digital Multimedia Forensics (DMF), only a minority of studies explicitly formulate hypotheses, and many omit critical details about experimental protocols, sampling strategies, or evaluation criteria [[32](#CR32)]. Similarly, a broader review of DF controlled experimentation emphasizes recurring deficiencies in the description of experimental design, inconsistent reporting of datasets, and a lack of systematic treatment of threats to validity [[33](#CR33)]. Without such information, it is difficult for the community to assess whether observed effects result from genuine causal mechanisms or from uncontrolled confounders.

Casey’s influential editorial emphasizes that the problem is not merely one of incomplete reporting but of inadequate design itself. He argues that DF experiments must isolate variables in inherently complex, noisy environments and that failure to do so leads to fragile conclusions [[8](#CR8)]. For example, tool performance may depend on operating system versions, file system structures, or specific hardware characteristics; if these are neither controlled nor disclosed, replication becomes impossible. Moreover, in the absence of baseline conditions or ground-truth data, it is unclear whether the results demonstrate genuine tool capabilities or merely reflect the test environment’s idiosyncrasies.

The issue of dataset quality and availability illustrates this challenge vividly. Garfinkel et al. argue that DF must adopt standardized forensic corpora that are carefully constructed, openly available, and well documented, akin to benchmark datasets in machine learning or information retrieval [[15](#CR15)]. Yet many DF studies rely on ad hoc collections of digital artifacts, often assembled without transparent procedures for provenance or validation. This practice severely limits comparability across studies and prevents independent verification. Even when datasets are shared, insufficient ground-truth annotation reduces their scientific value.

The reproducibility crisis that has affected other empirical sciences also resonates strongly in DF. Horsman proposes FRED (Framework for Reliable Experimental Design), which provides practical steps to anticipate threats to validity and to document design choices in a structured manner [[18](#CR18)]. However, mappings show that few DF studies adopt such frameworks [[33](#CR33)]. Similarly, Marshall and Paige note that digital forensic laboratories are expected to meet ISO/IEC 17025 accreditation requirements, which mandate validation, documentation, and transparency in method definition [[28](#CR28)]. Aligning academic research with these professional standards could substantially increase rigor and translational impact, yet current practice remains inconsistent.

Beyond design and dataset issues, deficiencies in statistical reasoning and validity assessment are also common. Few DF studies report confidence intervals, effect sizes, or statistical tests that account for trial-to-trial variability. Many rely on descriptive measures of accuracy or precision without systematically analyzing error sources. This lack of statistical rigor is particularly problematic in forensic contexts, where interpretations of error rates can directly affect judicial outcomes. As Casey notes, courts increasingly demand quantitative measures of reliability; without them, forensic claims may fail to meet admissibility standards [[8](#CR8)].

The literature further highlights the neglect of validity threats that are standard in software engineering and empirical computer science. Internal validity is compromised when confounding variables (e.g., uncontrolled system processes or nonrandom assignment of test cases) are overlooked. External validity is rarely discussed, raising concerns about whether results obtained in laboratory conditions generalize to the diverse real-world contexts of digital evidence. Construct validity is threatened when operationalizations of constructs such as “tool effectiveness” or “evidence completeness” are poorly defined or inconsistent across studies. Validity of the conclusion is weakened when the data analysis does not justify the strength of the claims. Oliveira Jr et al. emphasize that even when studies acknowledge some limitations, these are often perfunctory and not integrated into a broader reflection on validity [[33](#CR33)].

The lack of rigor in controlled experiments also affects cumulative progress in DF. Without replicable and comparable studies, it is challenging to aggregate findings or to perform systematic evaluations of techniques. Yates and Chi highlight the importance of benchmarking frameworks for mobile device forensics, arguing that meaningful comparisons can be made only through shared workloads and evaluation protocols [[42](#CR42)]. This argument extends to other DF domains, where heterogeneity in tools, datasets, and procedures hampers synthesis and slows methodological advancement.

Ultimately, the broader scientific community has adopted formal requirements for reproducibility. Journals such as *IEEE Transactions on Information Forensics and Security* explicitly require authors to release code, data, or sufficient detail to enable replication [[19](#CR19)]. Yet this culture has not thoroughly permeated DF, where proprietary tools, sensitive data, and legal constraints are often cited as obstacles. While these concerns are legitimate, they underscore the need for creative solutions, such as anonymized or synthetic datasets, structured experiment documentation, and clear guidelines for disclosure that balance privacy and security.

The evidence suggests that DF experimentation remains characterized by a lack of rigorousness across design, execution, reporting, and dissemination stages. The mappings by Oliveira Jr et al. reveal persistent gaps in reporting and methodological transparency [[32](#CR32), [33](#CR33)]. Casey underscores why these gaps are epistemically and legally problematic [[8](#CR8)]. Proposals for standardized datasets [[15](#CR15)], structured experimental design [[18](#CR18)], alignment with accreditation standards [[28](#CR28)], and benchmarking frameworks [[42](#CR42)] provide concrete pathways to improvement. Bridging the rigor gap is essential not only for academic credibility but also for ensuring that digital forensic evidence can serve as robust, reproducible, and legally defensible science.

## 2.4 Final Remarks

Controlled experimentation is a cornerstone of empirical research in computer science and digital forensics. It provides a systematic means to test hypotheses, establish causal relationships, and evaluate tools and techniques under repeatable conditions. When adequately designed and reported, controlled experiments contribute directly to the accumulation of reliable knowledge and to the advancement of both theory and practice.

This chapter emphasized that rigor is essential at every stage of the experimental process. From planning and execution to analysis and reporting, careful attention must be given to validity threats, transparency of procedures, and reproducibility of results. In computer science, controlled experiments complement other empirical methods by offering strong internal validity and clear causal inference. In digital forensics, however, recent reviews have revealed recurring shortcomings in methodological detail, dataset availability, and statistical reasoning. These issues limit comparability across studies and reduce confidence in experimental outcomes.

To address these challenges, adopting structured design frameworks, standardized datasets, and open reporting practices is necessary. Practices such as preregistration of study protocols, adherence to international standards, and sharing of experimental artifacts further strengthen credibility and reproducibility. By integrating such measures, researchers can ensure that digital forensic experimentation not only meets academic expectations but also produces findings that are robust enough to inform practice and withstand legal scrutiny.

Controlled experiments play a vital role in building the empirical foundation of computing. Their value lies not only in producing immediate results but also in supporting cumulative progress through transparency, rigor, and replication. A consistent commitment to these principles will ensure that computer science and digital forensics continue to mature as scientific disciplines grounded in trustworthy evidence.

## References

1. 1.

   Barham, P., Dragovic, B., Fraser, K., Hand, S., Harris, T., Ho, A., Neugebauer, A., Pratt, I., Warfield, A.: Xen and the art of virtualization. ACM SIGOPS Oper. Syst. Rev. **37**(5), 164–177 (2018). [https://​doi.​org/​10.​1145/​1165389.​945462](https://doi.org/10.1145/1165389.945462)<https://doi.org/10.1145/1165389.945462>
2. 2.

   Barr, R.S., Golden, B.L., Kelly, J.P., Resende, M.G.C., Stewart, W.R.: Designing and reporting on computational experiments with heuristic methods. J. Heurist. **1**(1), 9–32 (1995). [https://​doi.​org/​10.​1007/​BF02430363](https://doi.org/10.1007/BF02430363)<https://doi.org/10.1007/BF02430363>
3. 3.

   Barrantes-Vidal, N., Kwapil, T.R.: The application of Experience Sampling Methodology for the study of individual differences in real life. Per. Ind. Diff. **60**, S6 (2014). [https://​doi.​org/​10.​1016/​j.​paid.​2013.​07.​160](https://doi.org/10.1016/j.paid.2013.07.160). [https://​www.​sciencedirect.​com/​science/​article/​pii/​S019188691300446​7](https://www.sciencedirect.com/science/article/pii/S0191886913004467)
4. 4.

   Basili, V.R., Zelkowitz, M.V.: Empirical studies to build a science of computer science. Commun. ACM **50**(11), 33–37 (2007). [https://​doi.​org/​10.​1145/​1297797.​1297819](https://doi.org/10.1145/1297797.1297819)<https://doi.org/10.1145/1297797.1297819>
5. 5.

   Basili, V.R., Selby, R.W., Hutchens, D.H.: Experimental studies in software engineering—a controlled experiment approach. IEEE Trans. Softw. Eng. **SE-12**(7), 733–743 (1996). [https://​doi.​org/​10.​1109/​TSE.​1996.​501001](https://doi.org/10.1109/TSE.1996.501001)
6. 6.

   Blomberg, J., Burrell, M., Guest, G.: An ethnographic approach to design. Hum.-Comput. Interact. **6**(3–4), 329–366 (1993). [https://​doi.​org/​10.​1207/​s15327051hci0603​&​4\_​3](https://doi.org/10.1207/s15327051hci0603&4_3). [https://​www.​tandfonline.​com/​doi/​abs/​10.​1207/​s15327051hci0603​&​4\_​3](https://www.tandfonline.com/doi/abs/10.1207/s15327051hci0603&4_3)
7. 7.

   Brereton, P., Kitchenham, B., Budgen, D., Turner, M., Khalil, M.: Lessons from applying the systematic literature review process within the software engineering domain. J. Syst. Softw. **80**(4), 571–583 (2007). [https://​doi.​org/​10.​1016/​j.​jss.​2006.​07.​009](https://doi.org/10.1016/j.jss.2006.07.009). [https://​www.​sciencedirect.​com/​science/​article/​pii/​S016412120600128​3](https://www.sciencedirect.com/science/article/pii/S0164121206001283)
8. 8.

   Casey, E.: Experimental design challenges in digital forensics. Digit. Invest. **9**(3–4), 167–169 (2013). [https://​doi.​org/​10.​1016/​j.​diin.​2013.​02.​002](https://doi.org/10.1016/j.diin.2013.02.002). [https://​www.​sciencedirect.​com/​science/​article/​pii/​S174228761300010​8](https://www.sciencedirect.com/science/article/pii/S1742287613000108)
9. 9.

   Crabtree, A., Hemmings, T., Rodden, T.: Ethnography, ethnomethodology and design. Ethnogr. Praxis Ind. Conf. Proc. **2012**, 1–20 (2012). [https://​doi.​org/​10.​1111/​j.​1559-8918.​2012.​01070.​x](https://doi.org/10.1111/j.1559-8918.2012.01070.x)
10. 10.

    Denning, P.J.: ACM president’s letter: what is experimental computer science? Commun. ACM **23**(10), 543–544 (1980). [https://​doi.​org/​10.​1145/​359015.​359016](https://doi.org/10.1145/359015.359016)<https://doi.org/10.1145/359015.359016>
11. 11.

    Dongarra, J., Meuer, H., Strohmaier, E.: Top500 supercomputer sites. ACM SIGARCH Comput. Arch. News **38**(1), 1–7 (2010). [https://​doi.​org/​10.​1145/​1829690.​1829691](https://doi.org/10.1145/1829690.1829691)
12. 12.

    Ernst, N.A., Baldassarre, M.T.: Registered reports in software engineering. Empir. Softw. Eng. **28**(2) (2023). [https://​doi.​org/​10.​1007/​s10664-022-10277-5](https://doi.org/10.1007/s10664-022-10277-5)
13. 13.

    Floyd, C., Schwabe, G.: Empirical research methods in computing. ACM Comput. Surv. **47**(4), 1–36 (2015). [https://​doi.​org/​10.​1145/​2722946](https://doi.org/10.1145/2722946)
14. 14.

    Froehlich, J., Chen, M., Consolvo, S., Harrison, B., Landay, J.A.: MyExperience: a system for in situ tracing and capturing of user feedback on mobile phones. In: Proceedings of the 5th International Conference on Mobile Systems, Applications and Services (MobiSys), pp. 57–70 (2007). [https://​doi.​org/​10.​1145/​1247660.​1247669](https://doi.org/10.1145/1247660.1247669)
15. 15.

    Garfinkel, S.L., Farrell, P., Roussev, V., Dinolt, G.: Bringing science to digital forensics with standardized forensic corpora. Digit. Invest. **6**(Supplement), S2–S11 (2009). [https://​doi.​org/​10.​1016/​j.​diin.​2009.​06.​016](https://doi.org/10.1016/j.diin.2009.06.016)
16. 16.

    Giles, C.L.: Presenting and analyzing the results of AI experiments. In: Proceedings of the 14th International Joint Conference on Artificial Intelligence, pp. 1067–1072. AAAI Press (1997). [https://​doi.​org/​10.​5555/​1867406.​1867462](https://doi.org/10.5555/1867406.1867462)
17. 17.

    He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition: benchmarking and evaluation. In: IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778 (2016). [https://​doi.​org/​10.​1109/​CVPR.​2016.​90](https://doi.org/10.1109/CVPR.2016.90). [https://​ieeexplore.​ieee.​org/​document/​7780459](https://ieeexplore.ieee.org/document/7780459)
18. 18.

    Horsman, G.: Fred: a framework for reliable experimental design for digital forensics. Comput. Secur. **78**, 412–426 (2018). [https://​doi.​org/​10.​1016/​j.​cose.​2017.​11.​009](https://doi.org/10.1016/j.cose.2017.11.009)
19. 19.

    IEEE Signal Processing Society: IEEE transactions on information forensics and security: reproducibility guidance. [https://​signalprocessing​society.​org/​publications-resources/​ieee-transactions-information-forensics-and-security](https://signalprocessingsociety.org/publications-resources/ieee-transactions-information-forensics-and-security). Accessed: 07 Sep 2025
20. 20.

    Juristo, N., Moreno, A.M.: Software Testing and Analysis: Process, Principles, and Techniques. Springer (2001). [https://​doi.​org/​10.​1007/​978-1-4757-3558-0](https://doi.org/10.1007/978-1-4757-3558-0)
21. 21.

    Kampenes, V.B., Sjøberg, D.I.K.: A systematic review of quasi-experiments in software engineering. Inf. Softw. Technol. **51**(1), 71–82 (2009). [https://​doi.​org/​10.​1016/​j.​infsof.​2008.​05.​007](https://doi.org/10.1016/j.infsof.2008.05.007). [https://​www.​sciencedirect.​com/​science/​article/​abs/​pii/​S095058490800067​0](https://www.sciencedirect.com/science/article/abs/pii/S0950584908000670)
22. 22.

    Kitchenham, B., Charters, S.: Guidelines for performing systematic literature reviews in software engineering. Technical Report, Keele University and Durham University (2007). [https://​www.​inf.​ufsc.​br/​~aldo.​vw/​Kitchenham-Guidelines.​pdf](https://www.inf.ufsc.br/~aldo.vw/Kitchenham-Guidelines.pdf)
23. 23.

    Kitchenham, B., Pfleeger, S.L.: Personal opinion surveys. ACM SIGSOFT Softw. Eng. Notes **33**(2), 24–27 (2008). [https://​doi.​org/​10.​1145/​1368088.​1368093](https://doi.org/10.1145/1368088.1368093)<https://doi.org/10.1145/638750.638758>
24. 24.

    Kitchenham, B., Dyba, T., Jorgensen, M.: Evidence-based software engineering. Inf. Softw. Technol. **52**(1), 75–86 (2010). [https://​doi.​org/​10.​1016/​j.​infsof.​2008.​09.​009](https://doi.org/10.1016/j.infsof.2008.09.009). [https://​www.​sciencedirect.​com/​science/​article/​pii/​S095058490800134​1](https://www.sciencedirect.com/science/article/pii/S0950584908001341)
25. 25.

    Ko, A.J., Myers, B.A.: A practical guide to controlled experiments of software engineering tools. Empir. Softw. Eng. **20**(4), 1106–1136 (2015). [https://​doi.​org/​10.​1007/​s10664-013-9279-3](https://doi.org/10.1007/s10664-013-9279-3)
26. 26.

    Larsen, N., Stallrich, J., Sengupta, S., Deng, A., Kohavi, R., Stevens, N.T.: Statistical challenges in online controlled experiments: a review of a/b testing methodology. Am. Stat. **78**(2), 135–149 (2024). [https://​doi.​org/​10.​1080/​00031305.​2023.​2257237](https://doi.org/10.1080/00031305.2023.2257237)<https://doi.org/10.1080/00031305.2023.2257237>
27. 27.

    L’Erario, A., Detoni, T.A., Duarte, A.S.: A case study of software project replacement: a time series analysis. Int. J. Softw. Eng. Knowl. Eng. **33**(07), 1063–1093 (2023). [https://​doi.​org/​10.​1142/​S021819402350025​0](https://doi.org/10.1142/S0218194023500250)<https://doi.org/10.1142/S0218194023500250>
28. 28.

    Marshall, H., Paige, R.F.: Requirements in digital forensics method definition: observations from a UK study. Digit. Invest. **26**, 1–12 (2018). [https://​doi.​org/​10.​1016/​j.​diin.​2018.​06.​003](https://doi.org/10.1016/j.diin.2018.06.003)
29. 29.

    Muñoz Barón, D., et al.: Validating cognitive complexity as a complexity metric. In: Proceedings of the International Symposium on Empirical Software Engineering and Measurement (ESEM), pp. 89–98 (2020). [https://​doi.​org/​10.​1145/​1111037.​1111064](https://doi.org/10.1145/1111037.1111064)
30. 30.

    Nature: Registered reports (2023). [https://​www.​nature.​com/​nature/​for-authors/​registered-reports](https://www.nature.com/nature/for-authors/registered-reports). Acesso em: 4 set. 2025
31. 31.

    Oates, B.J.: Researching Information Systems and Computing, 2nd edn. SAGE Publications, London (2006)
32. 32.

    Oliveira, E. Jr, Zorzo, A.F., Neu, C.V.: Experimentation of digital multimedia forensics: state of the art and research gaps. Wiley Interdiscipl. Rev.: Foren. Sci. **3**(6), e1405 (2021). [https://​doi.​org/​10.​1002/​wfs2.​1405](https://doi.org/10.1002/wfs2.1405)
33. 33.

    Oliveira, E. Jr, Silva, T.J., Zorzo, A.F., Neu, C.V.: Digital forensics experimentation: analysis and recommendations. Foren. Sci. Rev. **34**(1), 21–41 (2022)
34. 34.

    Petticrew, M., Roberts, H.: Systematic reviews in the social sciences: a practical guide (2006)
35. 35.

    Ralph, P., Kelly, S., MacLean, P.: Empirical methods in software and systems research. ACM Comput. Surv. **51**(3), 1–33 (2018). [https://​doi.​org/​10.​1145/​3186569](https://doi.org/10.1145/3186569)
36. 36.

    Shull, F., Carver, J.C., Vegas, S., Juristo, N.: The role of replications in empirical software engineering. In: Proceedings of the 2008 International Symposium on Empirical Software Engineering and Measurement (ESEM), pp. 1–10. IEEE (2008). [https://​doi.​org/​10.​1109/​ESEM.​2008.​36](https://doi.org/10.1109/ESEM.2008.36)
37. 37.

    Sjøberg, D.I., Anda, B., Arisholm, E., Dyba, T., Jorgensen, M., Karahasanovic, A., Koren, E., Vokác, M.: Conducting realistic experiments in software engineering. Empir. Softw. Eng. **7**(1), 17–38 (2002). [https://​doi.​org/​10.​1023/​A:​1013544303017](https://doi.org/10.1023/A:1013544303017)
38. 38.

    Souza, F., Cruz, T., Rocha, A.: Surveying user interaction with emerging computing technologies. IEEE Access **8**, 123456–123470 (2020). [https://​doi.​org/​10.​1109/​ACCESS.​2020.​3001234](https://doi.org/10.1109/ACCESS.2020.3001234). [https://​ieeexplore.​ieee.​org/​document/​9001234](https://ieeexplore.ieee.org/document/9001234)
39. 39.

    Tedre, M., Moisseinen, N.: Experiments in computing: a survey. Sci. World J. **2014**, 549398 (2014). [https://​doi.​org/​10.​1155/​2014/​549398](https://doi.org/10.1155/2014/549398)
40. 40.

    Teixeira, E., Harrold, M.J., Johnson, R.A.: Threats to validity in controlled experiments in software engineering. In: Proceedings of the 2018 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement, pp. 1–10 (2018). [https://​doi.​org/​10.​1145/​3266237.​3266264](https://doi.org/10.1145/3266237.3266264)
41. 41.

    Wohlin, C., Runeson, P., et al.: Experimentation in Software Engineering, 1st edn. Springer, New York, NY (2012)<https://doi.org/10.1007/978-3-642-29044-2>
42. 42.

    Yates, M., Chi, H.: A framework for designing benchmarks of investigating digital forensics tools for mobile devices. In: Proceedings of the 49th Annual ACM Southeast Conference (ACM-SE’11), pp. 179–184. Association for Computing Machinery, Kennesaw (2011). [https://​doi.​org/​10.​1145/​2016039.​2016088](https://doi.org/10.1145/2016039.2016088)
43. 43.

    Yin, R.K.: Case Study Research and Applications: Design and Methods, 6th edn. SAGE Publications, London (2018)

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_3>

# 3. The Role of Reproducibility in Science and Digital Forensics

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

Reproducibility is a foundational requirement for scientific credibility, enabling the independent verification of results and supporting the accumulation of reliable knowledge. This chapter examines the conceptual, methodological, and legal dimensions of reproducibility and their implications for Digital Forensics, a field in which scientific rigor directly influences judicial outcomes. We discuss the distinctions among repeatability, replicability, and reproducibility, review how Open Science principles enhance transparency and trustworthiness, and analyze major global initiatives aimed at improving research reproducibility. The chapter also identifies key challenges that hinder reproducible digital forensic investigations, including heterogeneous device ecosystems, IoT complexity, volatile data, anti-forensic techniques, cloud environments, big data, and the shortage of specialized professionals. Finally, we outline how Open Science-driven experimentation, standardized methodologies, conceptual models, and open tools can strengthen the validity, reliability, and admissibility of digital evidence. By integrating scientific and legal perspectives, the chapter positions reproducibility as an essential pillar for the evolution of Digital Forensics into a robust, transparent, and trustworthy scientific discipline.

## 3.1 The Concept of Reproducibility in Science

Reproducibility is a cornerstone of scientific integrity and credibility. It reflects the ability of independent researchers to obtain the same or sufficiently similar results when repeating an experiment or analysis under conditions equivalent to the original study. Achieving reproducibility requires complete transparency and accessibility of all relevant data, methods, tools, and procedures, enabling others to rigorously evaluate and validate the findings [[9](#CR9), [19](#CR19), [20](#CR20)].

The robustness of scientific knowledge is directly tied to the reproducibility of its results. When a finding can be independently reproduced, sources of error, bias, and false claims are filtered out, reinforcing the evidential foundation of scientific consensus. Results that cannot be reproduced often remain isolated and provide limited value for cumulative knowledge. In contrast, reproducible findings contribute reliable evidence that supports the refinement of existing theories, comparative studies, and the development of new methods and datasets [[19](#CR19), [21](#CR21)].

In computer science, and particularly in Digital Forensics, several studies indicate recurring weaknesses in experimental rigor and reporting [[1](#CR1), [19](#CR19)]. Experimental work in these domains is often challenging to plan and replicate due to insufficient methodological detail, lack of statistical grounding, or limitations in formal analysis. Because much of the research involves novel systems, algorithms, and forensic techniques, objective evaluation depends fundamentally on the availability of reproducible experimental evidence.

Within Digital Forensics specifically, multiple authors emphasize the critical importance of well-designed and transparent experimentation [[4](#CR4), [17](#CR17), [19](#CR19)]. Poorly executed or under-documented experiments may lead to incorrect inferences, which in this field can affect judicial decisions and, ultimately, an individual’s rights. Ensuring reliability, therefore, demands not only sound experimental design but also clarity and completeness of reporting that enables independent verification.

### 3.1.1 Reproducibility, Repeatability, and Replicability

The concept of reproducibility is frequently discussed together with the related notions of repeatability and replicability. Although these terms are sometimes used interchangeably in everyday language, they represent distinct dimensions of experimental trustworthiness [[18](#CR18), [22](#CR22)]. The definitions commonly adopted in scientific and computational research are:

* **Repeatability**: performed by the *same team using the same experimental setup*. It refers to the capacity to obtain consistent results across repeated trials under identical conditions, employing the same data, procedures, instruments, and measurement systems. In computing, repeatability means that the original researchers can consistently reproduce their own computational outcomes.
* **Replicability**: performed by a *different team using the same experimental setup*. A study is replicable when independent researchers, following the original procedures and using the same resources, obtain results that are consistent with the original findings. Replicability depends strongly on the completeness and accuracy of the artifacts provided.
* **Reproducibility**: performed by a *different team using a different experimental setup*. Reproducibility involves obtaining equivalent results despite variations in tools, hardware, datasets, or analytical environments. In computational research, this means that another team must be able to reach the same conclusions even when using different models, tools, or data.

Figure [3.1](#Fig1) illustrates the relationship among these concepts.

![Flow chart illustrating the concepts of repeatability, replicability, and reproducibility in scientific research. The chart is divided into three columns. The first column, labeled “Repeatability,” describes using the same team and setup to achieve consistent results, with icons representing a researcher and lab equipment. The second column, “Replicability,” involves a different team using the same setup to achieve similar results, depicted with icons of collaboration and lab tools. The third column, “Reproducibility,” involves a different setup and team to achieve the same accuracy, shown with icons of diverse equipment and analysis. Each column includes bullet points detailing conditions for each concept, such as team, methods, and computational aspects. At the bottom, icons represent team, experimental setup, and process/analysis.](../images/624027_1_En_3_Chapter/624027_1_En_3_Fig1_HTML.png)

Fig. 3.1

Concepts of repeatability, replicability, and reproducibility

### 3.1.2 Dimensions of Reproducibility

Beyond these operational definitions, reproducibility can also be described in terms of methodological, results-based, and inferential dimensions [[8](#CR8)]. These dimensions highlight different aspects of how scientific claims may be independently verified.

* **Reproducibility of methods** ensures that procedures and data are documented in sufficient detail so that the same workflow can be executed precisely.
* **Reproducibility of results** refers to obtaining the same results by repeating the original procedures as closely as possible, often through new experimental executions.
* **Inferential reproducibility** occurs when independent analysts reach the same scientific conclusions, whether using the original data or new data, even if their analytical methods differ.

Figure [3.2](#Fig2) provides an overview of these categories.

![Flow chart illustrating three types of reproducibility in scientific research. The first section, “Reproducibility of Methods,” shows a magnifying glass and gear icon, indicating that sufficient procedural details are available for precise repetition. The second section, “Reproducibility of Results,” features bar graphs and a scientist with lab equipment, suggesting that new experiments using similar methods yield similar findings. The third section, “Inferential Reproducibility,” includes a checkmark and a thought bubble, indicating that the same conclusions can be drawn from reanalysis or new experiments. Icons at the bottom represent scientists, procedures, and analysis.](../images/624027_1_En_3_Chapter/624027_1_En_3_Fig2_HTML.png)

Fig. 3.2

Reproducibility of methods, results, and inferences

### 3.1.3 Reproducibility in Digital Forensics

A comprehensive Interpol review covering digital evidence practices from 2019 to 2022 highlights that the generalizability, reliability, and reproducibility of digital forensic outcomes depend strongly on the quality, volume, and availability of datasets [[23](#CR23)]. High-quality datasets are essential for producing consistent experimental results, supporting validation, and enhancing the scientific credibility of digital forensic investigations [[18](#CR18)].

Repeatability and reproducibility also operate as measures of consistency across repeated analyses. In digital forensic practice, repeatability is often well understood when a single forensic tool is applied multiple times to the same device. Yet, without standardized measurement specifications that define reproducibility across different tools, environments, and processes, reproducibility becomes challenging, representing a significant limitation for the field [[18](#CR18), [23](#CR23)].

Uncertainty and error rates are further concepts used to assess confidence in digital forensic outcomes. These uncertainties often arise from algorithmic limitations, analytical procedures, or measurement system constraints. Quantifying their influence remains a complex task and is recognized as an ongoing research challenge [[23](#CR23)].

Digital Forensics involves the recovery, analysis, and presentation of digital evidence for use in judicial settings. As such, it must adhere to principles of reliability and accuracy comparable to those found in traditional scientific domains. Because digital evidence can be mutable and ephemeral, reproducibility is essential to transform isolated observations into validated scientific claims. It is therefore a crucial element in establishing trustworthiness, fairness, and scientific progress in digital forensic science.

## 3.2 Open Science and Open Reproducible Research

Open Science refers to a set of principles and practices that make scientific research publicly accessible and transparent, benefiting researchers, industry, and society. Its core idea is that publications, data, source code, software, tools, methodologies, and hardware configurations should be shared under open licenses whenever possible, enabling broad reuse and scrutiny. Open Science also promotes a more democratic and inclusive scientific ecosystem, reinforcing the universal right of individuals to participate in scientific progress and benefit from it. By fostering transparency and accessibility, it contributes to societal development, technological advancement, and the improvement of quality of life [[25](#CR25)].

The growth of digital research practices has further expanded the scope of Open Science, bringing attention to the need for openness in scholarly communication, research workflows, and evaluation criteria. As research becomes more data-intensive and computationally driven, calls for greater transparency and reproducibility have intensified [[2](#CR2), [24](#CR24)]. Reproducibility is now explicitly required or encouraged by many journals, conferences, and funding agencies, reflecting a shift toward more accountable scientific practices.

The principles of Open Science are particularly relevant to Digital Forensics. This domain depends on transparency, reproducibility, and methodological rigor to ensure scientific and legal credibility. Traditionally, forensic experiments are conducted in restricted environments with limited access to tools, datasets, and documentation, making independent verification difficult. Such constraints can hinder reproducibility and reduce confidence in forensic outcomes.

Open Science practices help mitigate these issues by promoting openness in four significant areas: *Open Access, Open Data, Open Methodologies, and Open Peer Review*. Together, these principles enhance transparency and accessibility across the entire research life cycle [[3](#CR3)].

* **Open Access** ensures that research publications are freely and publicly available. Open Access increases transparency and broadens the reach of scientific output. The authors may achieve Open Access by depositing accepted manuscripts in institutional repositories, publishing in journals without publication fees, or using preprint servers, although financial barriers still exist in many venues.
* **Open Data** promotes sharing of research data, so it can be accessed, verified, reused, and extended by others. Open data should follow the FAIR principles (Findable, Accessible, Interoperable, and Reusable) [[26](#CR26)]. For sensitive data, privacy can be preserved through anonymization, restricted access, or the sharing of metadata rather than raw datasets. Public repositories facilitate long-term availability and reuse.
* **Open Methodologies** advocates complete and detailed documentation of experimental procedures, including tools, versions, settings, and environmental configurations. In Digital Forensics, this includes specifying forensic tools and their configurations, as well as sharing protocols, materials, scripts, and code to enable reproducibility (same data and methods) and replicability (same methods with new data).
* **Open Tools and Code:** Open-source forensic tools allow peer inspection, algorithm validation, and collaborative improvement. They increase transparency in acquisition, extraction, and analysis procedures. When closed-source tools must be used, detailed documentation of tool behavior and limitations is essential to support evaluation, verification, and reproducibility.
* **Open Review and Collaboration:** Transparent peer review, community-driven testbeds, and reproducible workflows strengthen scientific rigor. Open peer review practices, such as publishing reviewer reports and editorial decisions, enhance accountability and foster constructive feedback. At the same time, preservation of blind review is crucial in conferences and journals to ensure fairness and neutrality during the evaluation process.

Figure [3.3](#Fig3) summarizes the Open Science principles and their key roles.

![Flow chart illustrating “Open Science Practices” for transparency and accessibility. Central circle connects to four sections: “Open Access” with icons of a document and globe, highlighting free public availability and transparency through green and diamond routes. “Open Data” with database and magnifying glass icons, emphasizing freely accessible data adhering to FAIR principles and privacy protection. “Open Methodologies” with flask and checklist icons, focusing on detailed sharing for replication and reproducibility. “Open Peer Review” with speech bubbles and report icons, describing a transparent review process with published reports and blind review integrity.](../images/624027_1_En_3_Chapter/624027_1_En_3_Fig3_HTML.png)

Fig. 3.3

Open Science principles and their roles in the research life cycle

When applied to Digital Forensics, Open Science promotes a shift from isolated case studies to a more robust scientific foundation built upon shared, verifiable, and reusable knowledge. This strengthens the credibility of forensic findings not only among investigators and researchers but also in judicial contexts, contributing to greater trust in evidence presented in court [[14](#CR14)].

Despite its benefits, the widespread adoption of Open Science remains hindered by several barriers. These include limited awareness, insufficient training, lack of incentives, resource constraints, and concerns related to intellectual property, privacy, security, and cultural resistance within research communities [[3](#CR3)]. Although scientific knowledge should ideally be open, certain restrictions are necessary to safeguard privacy, human rights, and security. Consequently, tools and methods must be developed to enable responsible openness while respecting legitimate constraints [[25](#CR25)].

Reproducibility remains a central theme in scientific advancement. Without it, research findings become unverifiable and unreliable, which is especially problematic in fields such as Digital Forensics. Here, reproducibility ensures the validity of evidence, the credibility of forensic analyses, and the integrity of conclusions used in legal proceedings [[4](#CR4), [14](#CR14), [19](#CR19)]. Open Science, combined with open reproducible research practices, provides a pathway to strengthen the scientific and legal foundations of Digital Forensics.

## 3.3 Worldwide Reproducibility Initiatives

Experimentation is a cornerstone of scientific progress, as it strengthens the evidential basis of a field through systematically generated data, results, and analyses. Repeated trials, replications, and reproducibility studies allow researchers to confirm or refute hypotheses and advance scientific understanding. Persistent concerns about irreproducible findings have challenged assumptions about scientific reliability and motivated a global movement aimed at increasing transparency, improving research practices, and enhancing confidence in published results. Although initiatives vary across disciplines, regions, and organizations, their central objective is consistent: to promote scientific advancement by enabling the reproduction, verification, and extension of findings.

Several reproducibility initiatives have been developed to support researchers in designing robust experiments, validating results, and fostering open and reliable scientific practices. The following subsections present some of the most influential international efforts.

### 3.3.1 Springer Nature Open Science Initiatives

Springer Nature[1](#Fn1) is one of the world’s largest research publishers and a leading proponent of open research. It encompasses well-established brands such as Springer, Nature Portfolio, BMC, Palgrave Macmillan, and Scientific American. The organization promotes the open dissemination of all research outputs, including publications, preprints, data, code, protocols, and peer review materials. Its mission is to accelerate scientific progress, encourage interdisciplinary collaboration, increase research reuse, and strengthen trust in science.

Through collaborations across the academic ecosystem, Springer Nature supports sustainable and equitable research systems. Key Open Science initiatives[2](#Fn2) include:

* **Transparent Peer Review (TPR):** The authors publishing in Nature-branded journals benefit from Transparent Peer Review, which increases accountability and knowledge sharing by making reviewer comments and editorial decisions publicly accessible. TPR is the default standard for newly submitted research articles.
* **Code Sharing:** Springer Nature promotes computational reproducibility through a partnership with Code Ocean.[3](#Fn3) Code Ocean provides a cloud-based platform that enables the authors to share, execute, and reproduce code and data in standardized computational capsules. The platform adheres to FAIR principles [[26](#CR26)] and helps reduce technical barriers in code review.
* **Protocols Sharing:** The acquisition of protocols.io[4](#Fn4) expands support for sharing detailed and reproducible experimental methods. Protocols.io is a secure platform that enables the publication, versioning, and collaborative refinement of experimental protocols.
* **Data Sharing:** Springer Nature partners with figshare[5](#Fn5) to provide an integrated repository for storing and disseminating diverse research outputs. Figshare allows the authors to upload datasets in any format, making them citable, discoverable, and reusable. Data remains private during manuscript review and becomes publicly accessible upon publication.

### 3.3.2 The IEEE Access Reproducibility Initiative

The Institute of Electrical and Electronics Engineers (IEEE)[6](#Fn6) is the world’s largest technical professional organization and a key promoter of reproducible research. IEEE Access[7](#Fn7) is a multidisciplinary open-access journal known for rapid peer review and continuous publication. All articles are freely available, supported by article processing charges (APCs).

IEEE Access maintains a dedicated reproducibility initiative[8](#Fn8) that fosters transparency and reuse of research code. The authors may submit the code associated with a published article for post-publication peer review. Successful evaluation results in a reproducibility badge, increasing trust and visibility.

Several resources support this initiative:

1. 1.

   **IEEE DataPort:** a large-scale repository for datasets and analytical tools.[9](#Fn9) It supports data sharing, collaboration, and long-term preservation of research data.
2. 2.

   **IEEE CodeOcean:** a cloud platform that enables the authors to upload, execute, and reproduce code directly in the browser.[10](#Fn10) It eliminates installation barriers and ensures consistency across computational environments.
3. 3.

   **IEEE Author Center:** a comprehensive online resource that guides the authors on best practices in reproducibility, data management, and manuscript preparation.[11](#Fn11)

### 3.3.3 Brazilian Reproducibility Initiatives

Brazilian scientific output has expanded substantially in recent decades. However, greater publication volume does not necessarily translate into greater scientific reliability, and concerns about irreproducible findings have been documented across multiple domains, particularly in biomedical research.[12](#Fn12) In response, several national initiatives have emerged to strengthen transparency, methodological rigor, and reproducibility. Two of the most influential efforts come from the biomedical sciences and from the computing research community.

#### 3.3.3.1 The Brazilian Reproducibility Initiative (Biomedical Sciences)

The Brazilian Reproducibility Initiative[13](#Fn13) is a multicenter project supported by the Serrapilheira Institute[14](#Fn14) that aims to estimate the reproducibility of Brazilian biomedical science. The project replicates experiments from a random sample of published articles using three widely adopted laboratory methods: MTT cell viability assay, elevated plus maze, and RT-PCR.

Each experiment is independently reproduced in three laboratories using preregistered protocols closely aligned with the originals. Randomization, blinding, and justification of sample size ensure methodological rigor. Replication success is evaluated by checking whether effect sizes fall within a 95% prediction interval based on the three reproductions.

Non-replication does not necessarily imply problems in the original study, since interlaboratory variability may occur naturally. The initiative, therefore, provides reproducibility estimates and insights into methodological factors that influence replication success. It represents the first systematic national-level assessment of research reproducibility in Brazil. In recognition of its impact, it received the Einstein Foundation Award 2025[15](#Fn15) in the institutional category.

#### 3.3.3.2 Open Science and Reproducibility in Brazilian Computer Science: CBSoft, OpenScienSE, and the Artifact Festival

In the Brazilian Software Engineering and Computer Science communities, reproducibility has also gained significant visibility, particularly through initiatives associated with the Brazilian Conference on Software: Theory and Practice (CBSoft). Since 2021, CBSoft has hosted two major initiatives dedicated to promoting Open Science, artifact availability, and reproducibility.

* **OpenScienSE Workshop:** The Open Science in Software Engineering (OpenScienSE) workshop serves as a national forum that promotes transparency, openness, and reproducibility in Software Engineering research. The workshop brings together researchers, practitioners, and students who are committed to improving research practices, sharing datasets and tools, discussing experimental design openly, and fostering a community culture that values replicability. Typical contributions include replication studies, conceptual frameworks for experiment documentation, open datasets, and empirical work aligned with FAIR principles.
* **CBSoft Artifact Evaluation Track (Artifact Festival):** Since 2021, CBSoft has also maintained an Artifact Evaluation Track, often referred to as the Artifact Festival. This initiative assesses the availability, reusability, completeness, and reproducibility of research artifacts associated with papers accepted at CBSoft sub-events, including SBES, SBCARS, SBLP, and Sessão Setorial. The evaluation process is inspired by international practices adopted in events such as ICSE and FSE. It includes a system of badges that certify artifact availability, functional validation, and reproducibility. By encouraging the authors to package datasets, source code, tools, notebooks, scripts, and documentation, the Artifact Festival has contributed to improving transparency and long-term research value in the Brazilian community.

Together, the OpenScienSE workshop and the Artifact Festival constitute a coordinated, community-driven effort to advance Open Science and reproducibility in Brazilian Software Engineering. These initiatives help align national practices with international standards and strengthen the methodological foundations of empirical research in Computer Science.

In summary, Brazil now hosts reproducibility initiatives in both the biomedical and computing research communities. These efforts, although distinct in scope and methodology, collectively strengthen national scientific integrity, promote transparency, and position the country as an active contributor to global movements that advocate for Open Science and reproducible research.

### 3.3.4 The UK Reproducibility Network (UKRN)

The UK Reproducibility Network (UKRN)[16](#Fn16) is a national peer-led consortium dedicated to strengthening research quality across the United Kingdom. The network investigates factors that influence research robustness, conducts training activities, disseminates best practices, and coordinates institutional efforts to improve reproducibility.

UKRN brings together researchers, universities, funders, publishers, and other stakeholders. Its mission is to address cultural, structural, and procedural issues that contribute to poor reproducibility and replicability. The initiative is governed by a Supervisory Board and supported by advisory committees, enabling coordinated reform across disciplines and institutions.

### 3.3.5 The AI4Europe Reproducibility Initiative

Reproducibility is crucial in fields driven by AI and machine learning, where computational complexity, dataset variability, and opaque models can hinder verification. The AI4Europe Reproducibility Initiative[17](#Fn17) promotes reproducible AI research by addressing technical, cultural, and systemic challenges. The initiative is part of the AI-on-Demand (AIoD) platform, accessible at [https://​www.​ai4europe.​eu](https://www.ai4europe.eu).

The overarching objective of AI4Europe is to support a sustainable digital infrastructure and experimentation ecosystem that strengthens the European AI research landscape. It promotes openness, transparency, and trustworthy AI development by integrating resources from academic, industry, and government partners.

The AIoD platform[18](#Fn18) provides a community-driven environment where researchers can access and share:

* AI datasets, models, experiments, tools, and services
* Publications, educational materials, and research project information
* News, events, laboratories, and professional profiles

AI4Europe and AIoD aim to accelerate scientific discovery, enhance collaboration, and ensure the responsible development of AI aligned with European values.

## 3.4 Reproducibility Issues in Digital Forensics

Digital Forensics faces substantial ethical, technical, and methodological challenges. As digital devices proliferate and hardware and software ecosystems become increasingly heterogeneous, the ability to reproduce, validate, and trust forensic findings becomes more complex. Because the outcomes of forensic investigations must be scientifically grounded, verifiable, and trustworthy to be accepted in court, limitations in reproducibility directly affect the fairness and reliability of judicial processes. This section discusses the main issues and challenges that hinder reproducibility in Digital Forensics.

### 3.4.1 Complexity of Experiments

Designing robust experiments in Digital Forensics is far from trivial. Experimental work requires careful planning to avoid methodological mistakes and increase scientific precision. Flawed test results may lead to incorrect conclusions with severe consequences for individuals and organizations. Therefore, forensic researchers must prioritize both rigorous experimental design and transparent reporting to ensure reliability and repeatability.

Planning an experiment to interpret or explain digital artifacts requires eliminating irrelevant variables and isolating causal factors. Experimental environments must be controlled precisely, and parameters such as hardware configuration, software versions, and operating system settings must be documented in detail. Minor variations in experimental configuration can significantly alter experimental outcomes, making reproducibility a persistent challenge [[4](#CR4)].

### 3.4.2 IoT and the Complexity of Digital Systems and Devices

The Internet of Things (IoT) comprises physical objects equipped with sensors, software, and communication capabilities. The adoption of IoT devices is increasing rapidly, creating highly distributed, heterogeneous, and data-intensive environments. This complexity introduces several forensic challenges.

IoT systems generate vast amounts of diverse and often unstructured data. Their distributed nature complicates data acquisition, preservation, reconstruction, and analysis. Existing forensic processes were designed for traditional IT systems and usually fail to account for IoT-specific characteristics. Additional challenges arise due to the lack of standardized IoT forensic processes, limited training, insufficient specialized tools, and concerns regarding privacy and data protection [[6](#CR6), [12](#CR12), [16](#CR16)].

Some of the main reproducibility issues in IoT forensics include:

* Absence of guidelines or legal frameworks for handling incidents during pre- and post-incident phases
* Lack of defined forensic process models tailored to IoT environments
* Limited approaches to address privacy and data protection during evidence acquisition
* Device diversity that affects the authenticity, integrity, and reproducibility of digital evidence
* Difficulties in developing standardized tools and techniques adaptable to highly variable device ecosystems
* Constant need for training and skill development in response to emerging technologies
* Challenges posed by multi-jurisdictional data spread across different countries and legal systems

### 3.4.3 Artificial Intelligence (AI)

Digital transformation reshapes both society and criminal activity. Emerging technologies, particularly artificial intelligence, create new opportunities for malicious actors. The rapid evolution of AI has enabled the development of sophisticated tools that automate attacks, generate deceptive content, and conceal traces, thereby complicating forensic investigations [[13](#CR13), [15](#CR15)].

Generative AI systems can produce images, video, text, code, and synthetic identities. Publicly accessible platforms such as ChatGPT,[19](#Fn19) Gemini,[20](#Fn20) Meta AI,[21](#Fn21) and Copilot[22](#Fn22) demonstrate this capability. Malicious variants, such as WormGPT [[15](#CR15)], have emerged to assist criminals in crafting phishing attacks, generating malware, and erasing forensic traces.

The forensic models and tools based on artificial intelligence are highly dependent on the quality and amount of training data. In digital forensics, datasets are usually limited, lack diversity, and can contain biases that lead to inaccurate or unfair results if not properly addressed. Additionally, there is a high demand for reproducing state-of-the-art AI models that require high computational resources, which are financially expensive and usually not available to most researchers and experts.

Digital Forensics must therefore evolve by developing new investigative methods, tools, and strategies to address AI-enabled crimes. Without advances in forensic readiness and analytical capabilities, emerging AI technologies will continue to undermine reproducibility and the reliability of forensic results.

### 3.4.4 Big Data

IoT, cloud platforms, social networks, and modern applications generate enormous amounts of data, often unstructured and distributed across multiple environments. Managing, filtering, and analyzing such data introduce high computational overhead and increase the likelihood of human error or analytical bias. Documentation becomes more difficult, which compromises reproducibility.

The forensic process requires the collection, preservation, and analysis of electronic evidence. However, with data volumes growing exponentially, acquiring complete datasets is often impractical. Investigators may capture only a subset of evidence, particularly in live or cloud-based environments, risking the omission of critical information.

Large-scale data acquisition and processing require specialized hardware, advanced analytical tools, and substantial time investment. These requirements delay investigations, increase costs, and reduce the ability to produce timely and reproducible results [[6](#CR6), [12](#CR12), [16](#CR16)].

### 3.4.5 Cloud Computing

Cloud computing environments introduce additional layers of complexity. Data stored across distributed, virtualized infrastructures is often inaccessible to investigators, and physical examination of storage devices is not possible. Evidence belonging to multiple users may coexist within the same physical environment, complicating attribution and chain of custody.

The distributed and dynamic nature of cloud environments makes it difficult to reconstruct complete and consistent sets of evidence. Legal and privacy regulations vary across jurisdictions, and data may be stored in different countries, requiring coordination with multiple service providers. Traditional forensic methods are inadequate for these scenarios, and specialized tools and expertise are required to collect and analyze cloud-based evidence reliably.

### 3.4.6 Data Volatility and Dynamic Environments

Volatile data exists only temporarily and can be altered or lost when system states change. In Digital Forensics, volatile memory such as RAM often contains crucial information about system operations, active processes, and user activities. Because such data dissipates rapidly, acquisition must occur immediately and with specialized techniques.

The ephemeral nature of volatile data makes standardization and reproducibility difficult. If investigators fail to capture data in a timely manner or if acquisition methods differ slightly, results may not be comparable across analyses.

### 3.4.7 Anti-forensic Techniques and Cryptography

Anti-forensic techniques aim to obscure, manipulate, or destroy digital evidence. These techniques intentionally impede investigations and reduce the reproducibility of forensic findings. Common anti-forensic methods include:

* **Data encryption** prevents access to critical evidence. Encrypted virtual machines or storage volumes may be impossible to analyze without decryption keys.
* **Disk wiping** erases data irreversibly, eliminating evidence.
* **Timestomping** manipulates file timestamps, complicating timeline reconstruction.
* **VPN usage** obscures user identities and locations, making attribution difficult.
* **Event log deletion** removes traces of malicious activity from systems.
* **Cryptography misuse:** Attackers employ strong encryption and hashing to conceal or alter evidence. While cryptography ensures confidentiality and integrity in legitimate applications, it poses challenges to investigators attempting to recover readable data.
* **Difficult or impossible decryption:** Decrypting robust encryption is time-consuming, resource-intensive, and often infeasible without keys.

Overcoming these techniques requires specialized methods that are difficult to formalize, standardize, or reproduce consistently.

### 3.4.8 Shortage of Specialized Digital Forensics Professionals

Digital Forensics investigations involve diverse technologies and require advanced technical expertise. However, there is a global shortage of professionals trained in forensic methodologies, tools, and legal frameworks. This shortage affects the quality of investigations, creates bottlenecks, and increases the risk of misinterpretation or mishandling of evidence.

The lack of universally accepted standards for training, certification, and competency exacerbates this issue. Clear guidelines on professional qualifications are essential to ensure that forensic practitioners conduct analyses reliably and reproducibly [[7](#CR7)].

### 3.4.9 Discussion

Although significant progress has been made, Digital Forensics still faces critical challenges. Digital evidence is becoming increasingly complex, while its quality and verifiability are declining, creating risks of wrongful convictions or unpunished crimes.

A key improvement area is knowledge management and collaboration across disciplines. Harmonizing the roles of operational investigative advisors, forensic specialists, and legal experts can bridge gaps between law enforcement and scientific communities. Such integration enables systems that treat digital traces strategically, improve visibility across criminal activities, and enhance the trustworthiness and reproducibility of forensic results [[5](#CR5)].

Figure [3.4](#Fig4) summarizes the current issues and challenges in Digital Forensics discussed in this section.

![Flow chart illustrating major barriers in digital forensics investigations. Central theme is “Digital Forensics Investigations: Challenges & Barriers,” surrounded by four main categories: “Technological Complexity & Scale,” “Methodological & Experimental Issues,” “Adversarial & Anti-Forensic Techniques,” and “Human & Organizational Factors.” Each category branches into specific challenges, such as cloud computing, data volatility, anti-forensics, complexity of experiments, flawed results, cryptography, disk wiping, shortage of specialized professionals, and potential for human error. Each challenge is represented with icons and brief descriptions.](../images/624027_1_En_3_Chapter/624027_1_En_3_Fig4_HTML.png)

Fig. 3.4

Challenges and issues in Digital Forensics

## 3.5 Open Science-Driven Digital Forensics Experimentation

Digital evidence plays a central role in cybercrime investigations and prosecutions, as it provides information that can be used as proof in court. Such evidence is admissible only when its authenticity, reliability, and completeness can be demonstrated. Current technological developments pose challenges to the standardization of procedures for retrieving, preserving, and analyzing digital evidence, affecting legal validity. Because digital evidence differs substantially from physical evidence, it requires specific safeguards to ensure that it is not altered, corrupted, or compromised during investigation.

Open Science-driven experimentation in Digital Forensics adopts the principles of openness, transparency, and reproducibility throughout the investigative and research process. By sharing data, tools, methods, and documentation, researchers and practitioners strengthen the scientific and legal credibility of forensic results. These practices contribute to improving the reliability, reproducibility, and admissibility of digital evidence both in court and in the scientific community [[14](#CR14)].

Integrating Open Science into Digital Forensics also helps address challenges discussed in previous sections, including independent validation, the subjectivity of certain methodologies, inconsistencies among tools, and the lack of standardization. Key objectives of adopting Open Science foundations in Digital Forensics include:

* **Verifiability:** Transparency and verifiability are essential for ensuring that digital forensic results can be examined and trusted. Making data, tools, and methods openly accessible allows scientific and legal communities to independently verify experimental outcomes, improving the evidential value of digital artifacts.
* **Reproducibility and Replication:** Digital Forensics requires that independent teams be able to repeat or replicate experiments to verify outcomes. Detailed documentation of methodology, software versions, protocols, and workflows is fundamental to allow both repetition (same team, same setup) and replication (different team, same setup).
* **Data Sharing:** Open datasets and curated repositories of digital evidence enable researchers to extend previous work, perform comparative studies, and evaluate new tools under controlled and reproducible conditions.
* **Standardization:** Many digital forensic investigations rely on ad hoc methods, leading to inconsistent interpretations and results. Formal frameworks, conceptual models, and ontologies are needed to structure experimental design and support consistent, reliable, and interoperable forensic experimentation.

Open Science principles also guide other critical aspects of the forensic investigation process, such as:

* **Open-Source Tools:** Tools that follow Open Science guidelines, such as Autopsy,[23](#Fn23) provide transparency because their source code is publicly available for inspection. This enhances trust and reduces dependency on proprietary tools with closed implementations, whose internal logic may be unverifiable.
* **Methodologies and Frameworks:** With the rapid evolution of technology, new Open Science-driven structures are required. Reliable Experimental Design (FRED), proposed by Horsman [[10](#CR10)], supports researchers in conducting robust reverse engineering of digital artifacts and in reliably extracting and interpreting digital content. Another example is ExperDF-CM [[19](#CR19)], a conceptual model developed to assist digital forensic researchers in planning, executing, analyzing, and disseminating reproducible experiments based on empirical evidence.
* **Artificial Intelligence:** Applying Open Science principles to AI-based forensic tools enhances transparency, reliability, and resistance to anti-forensic manipulation. Open datasets, explainable AI models, and accessible codebases foster reproducibility and strengthen the forensic value of AI-driven analyses, particularly when processing large-scale digital evidence or detecting emerging threats.
* **Blockchain for Integrity:** Blockchain technology can support Digital Forensics by providing immutable, transparent, and verifiable chains of custody. Its decentralized architecture aligns with Open Science principles by enabling traceability and auditability of evidence handling throughout the investigation life cycle.

In practice, the movement toward Open Science in Digital Forensics is influenced by funding agencies, publishers, legal standards, and judicial expectations. By embracing Open Science, the Digital Forensics community transitions from reliance on expert opinion to evidence-based methodologies supported by verifiable protocols, tools, datasets, and workflows.

A recent study [[11](#CR11)] examined the admissibility of digital evidence produced by open-source forensic tools. The authors reviewed legal and technical factors influencing admissibility and proposed a conceptual framework to support the validation and acceptance of evidence obtained using open-source tools. The framework identifies key factors such as tool availability, reliability, integrity, transparency, and proper documentation. The study reports that open-source tools perform comparably to proprietary tools in accuracy and capability, although challenges remain in scalability and processing efficiency when handling large datasets. The analysis highlights that open-source tools are viable for forensic investigations, provided that reliability, documentation, and methodological transparency are ensured. These factors significantly influence judicial acceptance and support the broader adoption of Open Science-driven Digital Forensics [[11](#CR11)].

The discussion in this chapter highlights that reproducibility challenges in Digital Forensics stem from a combination of technical, methodological, and legal constraints. At the same time, the adoption of Open Science principles and structured experimental practices offers concrete pathways to mitigate these issues. To provide a synthesized view of how these challenges can be addressed in practice, Table [3.1](#Tab1) presents a comparative overview linking significant reproducibility challenges to corresponding solutions grounded in Open Science-driven methodologies, standardization efforts, and transparent forensic experimentation frameworks.

Table 3.1

Reproducibility challenges in Digital Forensics and corresponding Open Science-driven solutions

| Challenge in Digital Forensics | Open Science-driven or methodological solution |
| --- | --- |
| Complexity of experiments; sensitivity to configuration changes | Standardized documentation; detailed reporting of hardware, software versions, and environments; use of conceptual models such as ExperDF-CM |
| Heterogeneous IoT ecosystems; distributed and volatile data | IoT-specific forensic process models; structured metadata; FAIR-compliant repositories; reproducible pipelines |
| AI-enabled attacks and synthetic artifacts | Transparent AI models; open datasets; explainable AI; reproducible AI workflows and auditing protocols |
| Big data volumes and unstructured evidence | Scalable open-source tools; automated provenance capture; containerized and workflow-based reproducibility mechanisms |
| Cloud computing and multi-jurisdictional constraints | Hybrid chain-of-custody models; cryptographic verification; standardized cloud forensic procedures; blockchain-based integrity tracking |
| Volatile and dynamic environments | Automated acquisition protocols; timestamped and versioned scripts; rapid standardized capture procedures |
| Anti-forensic techniques (encryption, wiping, and timestomping) | Open testbeds; reproducible detection methodologies; transparent documentation of tool behavior and limitations |
| Shortage of specialized professionals | Community-driven training resources, open educational materials, standardized competency frameworks, and reproducible laboratory environments |

## 3.6 Final Remarks

This chapter presented the foundational concepts of reproducibility, its general challenges, and the specific complexities and legal requirements associated with its adoption in science and Digital Forensics. It is essential that researchers adopt more reproducible practices in experimentation and reporting, as reproducibility enhances the integrity of individual studies and guides cumulative scientific progress. Credibility is strengthened when findings can be independently confirmed, since reproducibility is not merely a technical requirement but a fundamental component of scientific advancement. Without it, scientific knowledge risks stagnation, inconsistency, and a loss of societal trust.

Although several proposals to improve reproducibility in scientific publishing have been discussed, particularly in Digital Forensics, much research still relies on unverifiable evidence or single-case experiments that lack methodological rigor. Open Science-driven experimentation guidelines offer a practical path toward addressing current issues in digital forensic research by improving the reliability, validity, and verifiability of findings, as well as enhancing the admissibility of digital evidence in court. However, broad adoption across both scientific and operational forensic communities remains necessary to achieve meaningful progress.

Strengthening reproducibility also requires establishing effective quality control mechanisms throughout the research life cycle. This includes clearer review processes, systematic correction pathways, and institutional support for transparent and rigorous scientific practices. Funding agencies and research institutions should encourage or require reproducibility as a core criterion for evaluation and publication. The emergence of global Open Science and reproducibility initiatives offers promising opportunities to advance the field of Digital Forensics, improving both scientific investigations and the reliability of evidence presented in legal contexts.

Reproducibility presents challenges across all scientific domains, but its complexity is particularly pronounced in Digital Forensics, where investigative findings can directly influence justice, legal outcomes, ethical considerations, privacy, security, and societal trust. As digital evidence becomes increasingly central in legal disputes and as society adopts more digital and artificial intelligence-based technologies, the need for reproducible, transparent, and scientifically rigorous forensic methods becomes even more critical.

## References

1. 1.

   Andujar, C., Schiaffonati, V., Schreiber, F.A., Tanca, L., Tedre, M., van Hee, K., van Leeuwen, J.: The role and relevance of experimentation in informatics. Technical report, Informatics Europe (2012). [http://​www.​informatics-europe.​org/​images/​documents/​informatics-experimentation\_​2013.​pdf](http://www.informatics-europe.org/images/documents/informatics-experimentation_2013.pdf)
2. 2.

   Banks, G.C., Field, J.G., O’Boyle, E.H., Landis, R.S., Rupp, D.E., Rogelberg, S.G.: The connection of open science practices and the methodological approach of researchers. J. Bus. Psychol. **34**, 257–270 (2019). [https://​doi.​org/​10.​1007/​s10869-018-9547-8](https://doi.org/10.1007/s10869-018-9547-8)<https://doi.org/10.1007/s10869-018-9547-8>
3. 3.

   Bertram, M.G., Sundin, J., Roche, D.G., Sánchez-Tójar, A., Thoré, E.S., Brodin, T.: Open science. Curr. Biol. **33**(15), R792–R797 (2023). [https://​doi.​org/​10.​1016/​j.​cub.​2023.​05.​036](https://doi.org/10.1016/j.cub.2023.05.036). [https://​www.​sciencedirect.​com/​science/​article/​pii/​S096098222300668​1](https://www.sciencedirect.com/science/article/pii/S0960982223006681)
4. 4.

   Casey, E.: Experimental design challenges in digital forensics. Digit. Invest. **9**(3), 167–169 (2013). [https://​doi.​org/​10.​1016/​j.​diin.​2013.​02.​002](https://doi.org/10.1016/j.diin.2013.02.002)<https://doi.org/10.1016/j.diin.2013.02.002>
5. 5.

   Casey, E.: The chequered past and risky future of digital forensics. Aust. J. Foren. Sci. **51**(6), 649–664 (2019). [https://​doi.​org/​10.​1080/​00450618.​2018.​1554090](https://doi.org/10.1080/00450618.2018.1554090)<https://doi.org/10.1080/00450618.2018.1554090>
6. 6.

   Casino, F., Dasaklis, T.K., Spathoulas, G.P., Anagnostopoulos, M., Ghosal, A., Boröcz, I., Solanas, A., Conti, M., Patsakis, C.: Research trends, challenges, and emerging topics in digital forensics: a review of reviews. IEEE Access **10**, 25464–25493 (2022). [https://​doi.​org/​10.​1109/​ACCESS.​2022.​3154059](https://doi.org/10.1109/ACCESS.2022.3154059)
7. 7.

   Fakhouri, H., Alsharaiah, M., Al Hwaitat, A., Alkhalaileh, M., Dweikat, F.: Overview of challenges faced by digital forensic. In: 2024 International Conference on Computing Research (ICCR), pp. 1–8 (2024). [https://​doi.​org/​10.​1109/​ICCR61006.​2024.​10532850](https://doi.org/10.1109/ICCR61006.2024.10532850)
8. 8.

   Goodman, S.N., Fanelli, D., Ioannidis, J.P.A.: What does research reproducibility mean? Sci. Transl. Med. **8**(341), 341ps12 (2016). [https://​doi.​org/​10.​1126/​scitranslmed.​aaf5027](https://doi.org/10.1126/scitranslmed.aaf5027)
9. 9.

   Gundersen, O.E.: The fundamental principles of reproducibility. Philos. Trans. R. Soc. A **379**(2197), 20200210 (2021). [https://​doi.​org/​10.​1098/​rsta.​2020.​0210](https://doi.org/10.1098/rsta.2020.0210)
10. 10.

    Horsman, G.: A framework for reliable experimental design (FRED) in digital forensics. Digit. Invest. **24**, S103–S113 (2018). Framework for Reliable Experimental Design in Digital Forensics
11. 11.

    Ismail, I., Ariffin, K.A.Z.A.: Open source tools for digital forensic investigation: capability, reliability, transparency and legal requirements. KSII Trans. Internet Inf. Syst. **18**(9) (2024). DOI not available in draft; verify upon final publication
12. 12.

    Kebande, V.R., Awad, A.I.: Industrial internet of things ecosystems security and digital forensics: achievements, open challenges, and future directions. ACM Comput. Surv. **56**(5) (2024). [https://​doi.​org/​10.​1145/​3635030](https://doi.org/10.1145/3635030)
13. 13.

    Klasén, L., Fock, N., Forchheimer, R.: The invisible evidence: digital forensics as key to solving crimes in the digital age. Foren. Sci. Int. **362**, 112133 (2024). [https://​doi.​org/​10.​1016/​j.​forsciint.​2024.​112133](https://doi.org/10.1016/j.forsciint.2024.112133)<https://doi.org/10.1016/j.forsciint.2024.112133>
14. 14.

    Lefebvre, A., Spruit, M.: Laboratory forensics for open science readiness: an investigative approach to research data management. Inf. Syst. Front. **23**, 156–173 (2021). [https://​doi.​org/​10.​1007/​s10796-021-10165-1](https://doi.org/10.1007/s10796-021-10165-1)
15. 15.

    Mohamed Firdhous, M.F., Elbreiki, W., Abdullahi, I., Sudantha, B., Budiarto, R.: WormGPT: a large language model chatbot for criminals. In: 2023 24th International Arab Conference on Information Technology (ACIT), pp. 1–6 (2023). [https://​doi.​org/​10.​1109/​ACIT58888.​2023.​10453752](https://doi.org/10.1109/ACIT58888.2023.10453752)
16. 16.

    Mohay, G.: Technical challenges and directions for digital forensics. In: Proceedings of SADFE 2005, pp. 155–161 (2005). [https://​doi.​org/​10.​1109/​SADFE.​2005.​24](https://doi.org/10.1109/SADFE.2005.24)
17. 17.

    Nance, K., Hay, B., Bishop, M.: Digital forensics: defining a research agenda. In: 42nd Hawaii International Conference on System Sciences, pp. 1–6 (2009). [https://​doi.​org/​10.​1109/​HICSS.​2009.​160](https://doi.org/10.1109/HICSS.2009.160)
18. 18.

    Nordvik, R., Stoykova, R., Franke, K., Axelsson, S., Toolan, F.: Reliability validation for file system interpretation. Foren. Sci. Int.: Digit. Invest. **37**, 301174 (2021). [https://​doi.​org/​10.​1016/​j.​fsidi.​2021.​301174](https://doi.org/10.1016/j.fsidi.2021.301174)
19. 19.

    Oliveira E. Jr, Zorzo, A.F., Neu, C.V.: Towards a conceptual model for promoting digital forensics experiments. Foren. Sci. Int.: Digit. Invest. **35**, 301014 (2020). [https://​doi.​org/​10.​1016/​j.​fsidi.​2020.​301014](https://doi.org/10.1016/j.fsidi.2020.301014)
20. 20.

    Oliveira, E. Jr, Silva, T.J., Zorzo, A.F., Neu, C.V.: Digital forensics experimentation: analysis and recommendations. Foren. Sci. Rev. **34**(1), 21–41 (2022)
21. 21.

    Pan, L., Batten, L.: Reproducibility of digital evidence in forensic investigations. Technical report, Unspecified (2005). Insufficient bibliographic data; source not fully traceable
22. 22.

    Plesser, H.E.: Reproducibility vs. replicability: a brief history of a confused terminology. Front. Neuroinform. **11** (2018). [https://​doi.​org/​10.​3389/​fninf.​2017.​00076](https://doi.org/10.3389/fninf.2017.00076)
23. 23.

    Reedy, P.: Interpol review of digital evidence for 2019–2022. Foren. Sci. Int.: Synergy **6**, 100313 (2023). [https://​doi.​org/​10.​1016/​j.​fsisyn.​2022.​100313](https://doi.org/10.1016/j.fsisyn.2022.100313)
24. 24.

    Steinhardt, I., Bauer, M., Wünsche, H., Schimmler, S.: The connection of open science practices and the methodological approach of researchers. Qual. Quant. **57**, 3621–3636 (2023). [https://​doi.​org/​10.​1007/​s11135-022-01524-4](https://doi.org/10.1007/s11135-022-01524-4)<https://doi.org/10.1007/s11135-022-01524-4>
25. 25.

    UNESCO: An introduction to the UNESCO recommendation on open science. Technical report (2022). [https://​doi.​org/​10.​54677/​XOIR1696](https://doi.org/10.54677/XOIR1696)
26. 26.

    Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J.E.A.: The fair guiding principles for scientific data management and stewardship. Sci. Data **3**, 160018 (2016). [https://​doi.​org/​10.​1038/​sdata.​2016.​18](https://doi.org/10.1038/sdata.2016.18)

Footnotes

[1](#Fn1_source)

[https://​www.​springernature.​com](https://www.springernature.com)

[2](#Fn2_source)

[https://​www.​springernature.​com/​gp/​open-science#c18176128](https://www.springernature.com/gp/open-science#c18176128)

[3](#Fn3_source)

[https://​codeocean.​com](https://codeocean.com)

[4](#Fn4_source)

[https://​www.​protocols.​io](https://www.protocols.io)

[5](#Fn5_source)

[https://​springernature.​figshare.​com/​](https://springernature.figshare.com/)

[6](#Fn6_source)

[https://​www.​ieee.​org/​](https://www.ieee.org/)

[7](#Fn7_source)

[https://​ieeeaccess.​ieee.​org/​](https://ieeeaccess.ieee.org/)

[8](#Fn8_source)

[https://​ieeeaccess.​ieee.​org/​authors/​reproducibility/​](https://ieeeaccess.ieee.org/authors/reproducibility/)

[9](#Fn9_source)

[https://​ieee-dataport.​org/​](https://ieee-dataport.org/)

[10](#Fn10_source)

[https://​codeocean.​com/​signup/​ieee](https://codeocean.com/signup/ieee)

[11](#Fn11_source)

[https://​journals.​ieeeauthorcenter​.​ieee.​org/​create-your-ieee-journal-article/​research-reproducibility/​](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/)

[12](#Fn12_source)

[https://​serrapilheira.​org/​en/​projetos/​brazilian-reproducibility-initiative/​](https://serrapilheira.org/en/projetos/brazilian-reproducibility-initiative/)

[13](#Fn13_source)

[https://​www.​reprodutibilidad​e.​bio.​br/​home](https://www.reprodutibilidade.bio.br/home)

[14](#Fn14_source)

[https://​serrapilheira.​org/​](https://serrapilheira.org/)

[15](#Fn15_source)

[https://​award.​einsteinfoundati​on.​de/​award-winners-finalists/​recipients-2025/​brazilian-reproducibility-initiative](https://award.einsteinfoundation.de/award-winners-finalists/recipients-2025/brazilian-reproducibility-initiative)

[16](#Fn16_source)

[https://​www.​ukrn.​org/​](https://www.ukrn.org/)

[17](#Fn17_source)

[https://​aiod.​eu/​project/​ai4europe/​](https://aiod.eu/project/ai4europe/)

[18](#Fn18_source)

[https://​aiod.​eu/​](https://aiod.eu/)

[19](#Fn19_source)

[https://​chatgpt.​com/​](https://chatgpt.com/)

[20](#Fn20_source)

[https://​gemini.​google.​com/​app](https://gemini.google.com/app)

[21](#Fn21_source)

[https://​ai.​meta.​com/​](https://ai.meta.com/)

[22](#Fn22_source)

[https://​copilot.​microsoft.​com/​](https://copilot.microsoft.com/)

[23](#Fn23_source)

[https://​www.​autopsy.​com/​](https://www.autopsy.com/)

# Part II Conceptual Modeling of Digital Forensics Controlled Experiments

This part establishes the theoretical and methodological backbone for documenting controlled experiments in Digital Forensics through the lens of conceptual modeling. It positions modeling not merely as a technical tool but also as a cognitive and communicative process that structures knowledge, supports shared understanding among stakeholders, and bridges the gap between abstract theory and operational practice. By integrating conceptual modeling principles into the experimental workflow, this part provides the scaffolding necessary to ensure methodological rigor, transparency, and reproducibility, which are fundamental for transforming Digital Forensics from a collection of isolated studies into a coherent and cumulative scientific discipline.

Drawing from the historical foundations of conceptual modeling, Chap. [4](624027_1_En_4_Chapter.xhtml) contextualizes its evolution from early Entity–Relationship models to modern multi-perspective and domain-specific approaches. It highlights how modeling contributes to semantic precision, quality assessment, and methodological consistency, which are essential for scientific communication and cumulative reasoning. The chapter also connects these ideas to the emerging needs of Digital Forensics, introducing conceptual modeling as a way to formalize investigative processes, align technical decisions with ethical standards, and facilitate the integration of open science practices.

Building on these principles, Chap. [5](624027_1_En_5_Chapter.xhtml) presents the Experimentation in Digital Forensics Conceptual Model (ExperDF-CM) as a structured framework designed to support the full life cycle of controlled experiments. Organized around five interdependent phases (*Planning*, *Pre-operation*, *Operation*, *Analysis and Interpretation*, and *Dissemination*), the model guides researchers in defining objectives, ensuring traceability, documenting procedures, and disseminating results in a transparent and reproducible manner. ExperDF-CM therefore operationalizes the values of scientific integrity and accountability, promoting not only methodological rigor but also the ethical and societal responsibility of Digital Forensics research.

Together, these chapters establish conceptual modeling as the unifying foundation of the book’s second part. They demonstrate how structured representations of experimental processes enhance comparability across studies, support cumulative evidence, and enable Digital Forensics to evolve as a data-driven, open, and trustworthy scientific field.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_4>

# 4. Basics of Conceptual Modeling

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter examines the theoretical, historical, and methodological foundations of conceptual modeling, emphasizing its essential role in representing, communicating, and reasoning about complex domains. It presents conceptual modeling as both a scientific and a cognitive process that structures knowledge, promotes semantic precision, and connects abstract representations to real-world problem-solving. The discussion revisits key milestones in the field, from early frameworks such as the Entity–Relationship model to object-oriented and Unified Modeling Language (UML) approaches, as well as more recent multi-perspective paradigms. Each of these developments is analyzed in terms of its contribution to expressiveness, methodological rigor, and practical usability in diverse application contexts. The chapter also explores quality criteria, evaluation frameworks, and tool support that sustain good modeling practice. It examines how conceptual modeling has expanded its influence beyond traditional information systems engineering into emerging fields such as artificial intelligence, big data, and digital twins, where it serves as a strategic mechanism for managing complexity, supporting interoperability, and enhancing interpretability. Through these discussions, the chapter establishes conceptual modeling as a key enabler of both technical innovation and scientific understanding. Building upon this theoretical foundation, the chapter introduces the relevance of conceptual modeling to the domain of Digital Forensics, a field that demands methodological precision, transparency, and reproducibility. Conceptual modeling is presented as a methodological bridge that connects empirical investigation with formal experimentation, allowing researchers to represent forensic processes in a structured, analyzable, and shareable way. Within this context, the chapter sets the stage for the introduction of the **ExperDF-CM (a Digital Forensics Controlled Experiments Conceptual Model)**, a structured framework proposed to enhance the planning, documentation, and communication of controlled experiments in Digital Forensics. The model is organized around five interrelated concepts (*Planning*, *Pre-Operation*, *Operation*, *Analysis and Interpretation*, and *Dissemination*), which together provide a comprehensive foundation for integrating experimental rigor, ethical compliance, and open science practices. By linking the principles of conceptual modeling with the practical requirements of Digital Forensics research, this chapter provides the conceptual and methodological groundwork for advancing reproducibility, transparency, and cumulative knowledge in the field. It thus frames conceptual modeling not merely as a technical discipline but as a catalyst for the scientific and societal maturation of Digital Forensics.

## 4.1 Conceptual Modeling

Conceptual modeling plays a fundamental role in several scientific fields, particularly in computer science. It enables the construction of abstract representations of domains by using a controlled language and well-defined objectives. These models provide a high-level view of the semantics of software applications, covering both structural and behavioral aspects.

By capturing the essence of entities and their interactions within a domain, conceptual modeling fosters effective communication among software stakeholders and developers. This shared understanding is essential to align expectations and requirements throughout the software development process [[12](#CR12)].

Beyond software engineering, conceptual modeling is crucial for representing phenomena within diverse domains. Abstract models facilitate the identification of requirements and the definition of specifications, thus bridging real-world problems and technical solutions. By removing unnecessary details, conceptual models provide a clear, organized representation of the system, which supports subsequent analysis and design phases [[18](#CR18), [22](#CR22)].

## 4.2 Historical Development and Methodological Aspects

The origins of conceptual modeling can be traced back to the 1970s with the introduction of the Entity–Relationship (ER) model by Chen [[3](#CR3)], which provided a systematic way to represent data semantics. The ER model introduced a clear separation between entities, attributes, and relationships, setting the foundation for subsequent advances in database design. Its graphical notation made it more accessible to both technical and nontechnical stakeholders.

In the 1980s and 1990s, object-oriented paradigms emerged, emphasizing encapsulation and inheritance as key principles. This shift culminated in the development of the Unified Modeling Language (UML), which became a widely adopted standard for modeling software systems [[2](#CR2)]. UML introduced multiple diagram types, enabling the representation of both structural and behavioral aspects of systems. Later developments extended conceptual modeling into requirements engineering, knowledge representation, and enterprise modeling [[10](#CR10)]. Over time, the scope broadened from purely technical system descriptions to capturing organizational processes and human factors. This evolution demonstrates a gradual shift from structural representations to multi-perspective approaches that accommodate complexity and dynamics.

Figure [4.1](#Fig1) illustrates the historical trajectory of conceptual modeling, highlighting major milestones from ER models to contemporary applications.

![Timeline diagram illustrating the evolution of modeling techniques. It starts with the “Entity-Relationship model” in the 1970s, followed by “Object-oriented paradigms” in the 1980s, “Unified Modeling Language” in the 1990s, and “Contemporary applications” in the 2000s. Each stage is represented in a separate box connected to a horizontal timeline with an arrow pointing right.](../images/624027_1_En_4_Chapter/624027_1_En_4_Fig1_HTML.png)

Fig. 4.1

Timeline of major developments in conceptual modeling

Conceptual modeling also serves as a methodological tool for building and analyzing theories. Approaches such as grounded theory benefit from conceptual modeling, since it allows researchers to systematically derive theories directly from data. Through iterative and data-driven procedures, conceptual models are kept consistent with empirical observations, capturing the nuances and complexities of the studied phenomena [[22](#CR22)]. At the same time, research highlights several challenges in developing accurate and expressive models. Lukyanenko et al. [[11](#CR11)] identified eight recurrent modeling challenges involving entities, generalization hierarchies, relationship types, attributes, and cardinalities. For example, unclear distinctions between entities and attributes may lead to ambiguous designs, while misrepresentation of cardinalities can result in data integrity problems. Addressing these challenges requires modelers to combine methodological rigor with domain expertise.

Table [4.1](#Tab1) summarizes the most common challenges in conceptual modeling and suggests strategies to mitigate them.

Table 4.1

Modeling challenges and suggested strategies [[11](#CR11)]

| Challenge | Suggested strategy |
| --- | --- |
| Entity vs. attribute distinction | Use modeling guidelines and clear definitions validated by stakeholders |
| Generalization hierarchies | Apply specialization rules and verify consistency with domain experts |
| Relationship types | Employ expressive notations and ontology-based checks |
| Attributes | Validate attributes through iterative feedback sessions |
| Cardinalities | Use automated validation tools to test data integrity constraints |
| Semantic ambiguity | Apply domain ontologies and glossary alignment |
| Over-modeling | Follow the minimality principle and focus on essential concepts |
| Stakeholder interpretation | Conduct participatory workshops for shared understanding |

## 4.3 Evaluation, Types, Applications, and Interdisciplinary Perspectives

The effectiveness of conceptual models depends on their quality and accuracy. Several criteria have been proposed, including clarity, expressiveness, correctness, completeness, and minimality [[13](#CR13)]. For instance, clarity concerns how easily stakeholders can understand a model, while completeness ensures that all relevant aspects of the domain are represented. Empirical studies have investigated how different notations and modeling practices influence model comprehensibility and communication effectiveness [[6](#CR6)]. Results suggest that graphical notations often support faster understanding, but textual annotations improve precision. Quality frameworks also emphasize the role of validation, ensuring that models remain faithful representations of reality while serving their intended purpose in design and communication [[9](#CR9)].

Conceptual models can be classified from different perspectives. From a general perspective, they are commonly divided into three main categories: Data Models, Process Models, and Behavior Models [[23](#CR23)]. While Data Models are static, Process and Behavior Models are dynamic. Several well-established conceptual data forms illustrate the diversity of approaches in the field [[24](#CR24)]:

* Entity Relationship Models, which use graphical notation to depict entities, attributes, and relationships
* Petri Nets, representing distributed systems as directed bipartite graphs with annotations
* Unified Modeling Language (UML), which offers multiple diagram types, including class diagrams enhanced by textual constraint languages
* Concept Maps, graphical tools that represent knowledge through concepts enclosed in rectangles or circles, with relationships indicated by labeled connecting lines

From a functional perspective, conceptual models can be further classified into four categories: Structure-Based Models, Object-Oriented Models, Knowledge Semantic-Based Models, and Web Semantic-Based Models [[24](#CR24)]. Figure [4.2](#Fig2) illustrates this classification. Figure [4.3](#Fig3) provides a concrete example of a conceptual map.

![Flowchart illustrating the hierarchy of conceptual models. The top level is “Conceptual Model,” branching into four categories: “Structure-based Model,” “Object-Oriented Model,” “Knowledge Semantic-based Model,” and “Web Semantic-based Model.” Each category further divides into subcategories. “Structure-based Model” splits into “ER Model” and “EER Model.” “Object-Oriented Model” divides into “UML” and “ORM.” “Knowledge Semantic-based Model” branches into “Concept Map,” “Mind Map,” and “Cognitive Map.” “Web Semantic-based Model” splits into “Recursive Object Model,” “XML,” “RDF,” and “OWL.”](../images/624027_1_En_4_Chapter/624027_1_En_4_Fig2_HTML.png)

Fig. 4.2

Conceptual model classification from the functional view [[24](#CR24)]

![Flow chart illustrating the factors determining seasons. “Seasons” are influenced by the “Amount of Sunlight,” which affects “Seasonal Temperature Variations.” Sunlight amount is determined by “Length of Day” and “Height of Sun above Horizon.” “Length of Day” is longer in “Summer” and shorter in “Winter.” “Height of Sun” is higher in summer and lower in winter. These are influenced by the “23.5 Degrees Tilt of Axis” and “Position in Orbit.” The axis points toward or away from the “Sun,” affecting sunlight. “Slight variation in distance” from the sun has a “Negligible Effect.”](../images/624027_1_En_4_Chapter/624027_1_En_4_Fig3_HTML.png)

Fig. 4.3

An example of a conceptual map [[16](#CR16)]

Conceptual modeling has evolved to support emerging domains such as big data, AI/ML, digital twins, and the Semantic Web [[14](#CR14), [20](#CR20), [21](#CR21), [25](#CR25)]. Table [4.2](#Tab2) consolidates these applications. Conceptual modeling has also expanded into interdisciplinary areas, including biology [[8](#CR8)], education [[15](#CR15)], and business process modeling [[4](#CR4)].

Table 4.2

Applications of conceptual modeling in emerging domains

| Domain | Role of conceptual modeling |
| --- | --- |
| Big data | Structuring heterogeneous data and supporting semantic integration [[14](#CR14)] |
| Artificial intelligence | Enhancing explainability and interpretability of models [[25](#CR25)] |
| Digital twins | Establishing correspondence between physical and virtual entities [[20](#CR20)] |
| Semantic web | Enabling interoperability and reasoning across distributed systems [[21](#CR21)] |

## 4.4 Tool Support for Conceptual Modeling

Tool support has been critical for the adoption of conceptual modeling in practice. Commercial solutions such as ERWin Data Modeler, IBM Rational Rose, and Enterprise Architect have long been used in software engineering and database design [[5](#CR5)]. These tools offer automated features, including code generation, model validation, and reverse engineering. In semantic modeling, tools like Protégé facilitate ontology construction and reasoning [[17](#CR17)]. More recent developments emphasize collaborative modeling environments, cloud-based platforms, and integration with development pipelines.

Table [4.3](#Tab3) lists some representative tools.

Table 4.3

Examples of tool support for conceptual modeling

| Tool | Domain | Features |
| --- | --- | --- |
| ERWin Data Modeler | Data modeling | Database design, schema generation, reverse engineering |
| IBM Rational Rose | Software engineering | UML diagrams, model-driven development |
| Enterprise Architect | Enterprise systems | Multi-domain modeling, integration with development pipelines |
| Protégé | Semantic modeling | Ontology creation, reasoning, ontology-based applications |

## 4.5 The Role of Conceptual Modeling in Digital Forensics

A conceptual model in DF serves as a structured framework that guides the systematic investigation of digital crimes. It provides a standardized approach to identifying, collecting, preserving, analyzing, and presenting digital evidence, ensuring that investigations are conducted efficiently and that the resulting evidence is legally admissible. By offering a clear roadmap, these models help investigators navigate the complexities of digital environments and maintain the integrity of the evidence throughout the investigative process [[7](#CR7)].

One notable example is the General Digital Forensics Investigation Process (GDFIP) [[7](#CR7)], which emphasizes a comprehensive approach to digital investigations. This model outlines stages such as preparation, data collection, examination, analysis, and reporting, ensuring that investigators consider all relevant aspects of a case. Following this structured process, professionals can maintain consistency and thoroughness in their investigations, leading to more reliable outcomes.

In the context of organizational preparedness, a conceptual model for digital forensic readiness has been proposed to enhance an organization’s ability to respond to security incidents. This model outlines proactive activities and organizations can undertake to increase responsiveness, such as implementing systematic procedures to identify activities related to a digitally forensic-ready environment. Organizations can better prepare for potential incidents by adopting such a model, ensuring they can effectively handle and investigate digital threats [[19](#CR19)].

Integrating conceptual models in digital forensics also extends to specialized areas, such as the investigation of Unmanned Aerial Vehicles (UAVs). A design science research study developed a conceptual model to comprehensively investigate UAVs under forensic conditions [[1](#CR1)]. This model identifies, captures, preserves, analyzes, and documents UAV incidents, addressing the unique challenges posed by these devices. The proposed model comprises stages that ensure a thorough approach to UAV-related investigations.

Conceptual models are also crucial in standardizing procedural frameworks for digital forensic investigations. For instance, the Next Generation Digital Forensic Investigation Model (NGDFIM) [[26](#CR26)] focuses on creating a standardized procedural framework for the entire digital forensic investigation process. By providing a structured approach, such models ensure consistency and reliability in investigations, which is essential for the admissibility of digital evidence in legal proceedings.

In the context of big data [[27](#CR27)], conceptual models have been developed to address the challenges posed by the vast volumes of information. A proposed model supports forensic investigations of big data by providing new insights and methodologies tailored to large-scale data environments. This approach ensures that investigators can efficiently process and analyze extensive datasets, maintaining the integrity and reliability of the forensic process.

The adoption of conceptual models in digital forensics has some challenges [[7](#CR7)]. Investigators must be adequately trained to apply these models effectively, and a balance must be struck between adhering to standardized procedures and adapting to each case’s unique circumstances. Additionally, as technology continues to evolve, these models must be updated to address new types of digital evidence and emerging threats. Continuous research and development are essential to ensure that conceptual models remain relevant and effective in guiding digital forensic investigations [[19](#CR19)].

Therefore, conceptual models are indispensable tools in DF, providing structured frameworks that guide the investigative process. They ensure that digital evidence is handled systematically and that investigations are thorough and legally sound. As digital environments continue to evolve, developing and refining these models will be crucial in addressing new challenges and maintaining the integrity of digital forensic investigations.

## 4.6 Final Remarks

Conceptual modeling has proven to be a cornerstone of knowledge representation and communication within computer science and other scientific disciplines. It provides an essential abstraction mechanism that enables complex domains to be expressed in structured, comprehensible, and analyzable forms. As this chapter has demonstrated, the evolution of conceptual modeling reflects a progressive effort to strike a balance between theoretical precision, methodological rigor, and practical usability. From the introduction of the Entity–Relationship model to the rise of object-oriented and multi-perspective frameworks, each generation of models has expanded the discipline’s expressive power and analytical scope.

The historical development of conceptual modeling demonstrates its adaptability to different technological paradigms and scientific needs. What began as a tool for database design has evolved into a versatile methodology that supports software engineering, organizational analysis, and knowledge representation across various domains. This trajectory reveals not only the expansion of modeling techniques but also their deepening integration into the scientific process. Conceptual models now serve as instruments for reasoning, hypothesis formulation, and empirical validation, bridging the gap between abstract theory and applied investigation.

The methodological foundations discussed in this chapter highlight that the quality of a conceptual model depends on its clarity, expressiveness, correctness, and completeness. These attributes ensure that a model accurately represents reality while remaining understandable and valuable to its intended audience. The discussion of evaluation frameworks and modeling challenges underscores the need for both methodological discipline and iterative refinement. As modeling complexity increases, tool support ranging from traditional diagramming software to ontology-based environments becomes indispensable for maintaining consistency and facilitating collaboration.

The versatility of conceptual modeling is evident in its applications across emerging fields, including artificial intelligence, big data, digital twins, and the Semantic Web. In these contexts, conceptual models play a vital role in structuring information, ensuring interoperability, and enhancing interpretability. Their use extends beyond technical design to serve cognitive and communicative functions, enabling multidisciplinary collaboration. By providing a shared language and representation framework, conceptual modeling helps align human understanding with computational logic.

Within the context of Digital Forensics, conceptual modeling assumes a crucial role. It enables the systematic representation of investigative processes, ensuring that the identification, preservation, analysis, and presentation of digital evidence follow coherent and transparent procedures. Conceptual models, such as the General Digital Forensics Investigation Process (GDFIP) and the Next Generation Digital Forensic Investigation Model (NGDFIM), as well as forensic readiness frameworks, exemplify how structured representations can standardize practices and improve both efficiency and reliability. The integration of conceptual modeling into Digital Forensics not only supports procedural consistency but also strengthens the scientific credibility of the discipline.

At the same time, the challenges facing digital investigators, including rapid technological change, data heterogeneity, and increasing system complexity, highlight the need for continuous refinement of these models. Their relevance depends on their ability to adapt to new environments, such as cloud infrastructure, mobile ecosystems, and unmanned aerial systems. Ensuring that conceptual models remain both flexible and scientifically grounded will be essential for maintaining their role as reliable instruments of forensic reasoning.

In summary, conceptual modeling represents far more than a technical exercise in diagramming or data organization. It is a methodological foundation that integrates abstraction, communication, and validation across scientific and practical domains. By fostering shared understanding, promoting analytical rigor, and supporting the formalization of complex processes, conceptual modeling remains a vital component of knowledge creation and technological innovation. Its ongoing refinement and application will remain central to advancing not only computer science but also interdisciplinary domains such as Digital Forensics, where the pursuit of clarity, reliability, and transparency is inseparable from the pursuit of truth.

## References

1. 1.

   Alotaibi, F., Al-Dhaqm, A., Al-Otaibi, Y.D.: A conceptual digital forensic investigation model applicable to the drone forensics field. Eng. Technol. Appl. Sci. Res. **13**(5), 11608–11615 (2023). [https://​doi.​org/​10.​48084/​etasr.​6195](https://doi.org/10.48084/etasr.6195)
2. 2.

   Booch, G., Rumbaugh, J., Jacobson, I.: The Unified Modeling Language User Guide. Addison-Wesley, Boston, MA (1999)
3. 3.

   Chen, P.P.: The entity-relationship model: toward a unified view of data. ACM Trans. Database Syst. **1**(1), 9–36 (1976)<https://doi.org/10.1145/320434.320440>
4. 4.

   Dumas, M., Rosa, M.L., Mendling, J., Reijers, H.A.: Fundamentals of Business Process Management. Springer, Berlin (2013)<https://doi.org/10.1007/978-3-642-33143-5>
5. 5.

   Fowler, M.: UML Distilled: A Brief Guide to the Standard Object Modeling Language. Addison-Wesley, Boston (2004)
6. 6.

   Gemino, A., Wand, Y.: Evaluating modeling techniques based on models of learning. Commun. ACM **51**(12), 105–110 (2008)
7. 7.

   Ivanova, M., Stefanov, S.: Digital forensics investigation models: Current state and analysis. In: Proceedings of the 8th International Conference on Smart and Sustainable Technologies (SpliTech), pp. 1–4 (2023). [https://​doi.​org/​10.​23919/​SpliTech58164.​2023.​10193176](https://doi.org/10.23919/SpliTech58164.2023.10193176)
8. 8.

   Kohn, K.W.: Molecular interaction map of the mammalian cell cycle control and dna repair systems. Mol. Biol. Cell **10**(8), 2703–2734 (1999)<https://doi.org/10.1091/mbc.10.8.2703>
9. 9.

   Lindland, O.I., Sindre, G., Sølvberg, A.: Understanding quality in conceptual modeling. IEEE Softw. **11**(2), 42–49 (1994)<https://doi.org/10.1109/52.268955>
10. 10.

    Loucopoulos, P., Yu, E.: The evolution of conceptual modeling research: Past, present, and future. In: Conceptual Modeling: Perspectives on Information Systems, pp. 3–18. Springer, Berlin (2014)
11. 11.

    Lukyanenko, R., Samuel, B.M., Parsons, J., Storey, V.C., Pastor, O., Jabbari, A.: Universal conceptual modeling: principles, benefits, and an agenda for conceptual modeling research. Inf. Syst. Res. **23**, 1077–1100 (2024). Forthcoming
12. 12.

    Mayr, P., Thalheim, B.: The Triptych of Conceptual Modeling. Springer, Berlin (2025). Forthcoming
13. 13.

    Moody, D.L.: Theoretical and practical issues in evaluating the quality of conceptual models: current state and future directions. Data Knowl. Eng. **55**(3), 243–276 (2005)<https://doi.org/10.1016/j.datak.2004.12.005>
14. 14.

    Müller, H., Meyer-Wegener, K.: Big data and conceptual modeling. Inf. Syst. **44**, 113–131 (2015)
15. 15.

    Nesbit, J.C., Adesope, O.: Learning with concept and knowledge maps: a meta-analysis. Rev. Educ. Res. **76**(3), 413–448 (2006)<https://doi.org/10.3102/00346543076003413>
16. 16.

    Novak, J., Can̄as, A.J.: The theory underlying concept maps and how to construct and use them. Tech. Rep. 2006-01 Rev 2008-01, Florida Institute for Human and Machine Cognition (2006). [http://​cmap.​ihmc.​us/​Publications/​ResearchPapers/​TheoryCmaps/​TheoryUnderlying​ConceptMaps.​htm](http://cmap.ihmc.us/Publications/ResearchPapers/TheoryCmaps/TheoryUnderlyingConceptMaps.htm)
17. 17.

    Noy, N.F., McGuinness, D.L.: Ontology development 101: A guide to creating your first ontology. Stanford Knowledge Systems Laboratory Technical Report (2001)
18. 18.

    Olivé, A.: Conceptual Modeling of Information Systems. Springer, Berlin, Heidelberg (2007)
19. 19.

    Pooe, A., Labuschagne, L.: A conceptual model for digital forensic readiness. In: Proceedings of the Information Security for South Africa, pp. 1–8 (2012). [https://​doi.​org/​10.​1109/​ISSA.​2012.​6320452](https://doi.org/10.1109/ISSA.2012.6320452)
20. 20.

    Rosen, R., von Wichert, G., Lo, G., Döge, K.: About the importance of digital twins in engineering. IFAC-PapersOnLine **48**(3), 567–572 (2015)<https://doi.org/10.1016/j.ifacol.2015.06.141>
21. 21.

    Shadbolt, N., Hall, W., Berners-Lee, T.: The semantic web revisited. IEEE Intell. Syst. **21**(3), 96–101 (2006)<https://doi.org/10.1109/MIS.2006.62>
22. 22.

    Storey, V.C., Lukyanenko, R., Castellanos, A.: Conceptual modeling: topics, themes, and technology trends. ACM Comput. Surveys **55**(14s), 1–38 (2023). [https://​doi.​org/​10.​1145/​3589338](https://doi.org/10.1145/3589338)<https://doi.org/10.1145/3589338>
23. 23.

    Uthmann, C.V., Becker, J.: Guidelines of modelling (GoM) for business process simulation. In: Proceedings of Process Modelling, pp. 100–116. Springer, Berlin, Heidelberg (1999)
24. 24.

    Wen, K., Zeng, Y., Li, R., Lin, J.: Modeling semantic information in engineering applications: a review. Artif. Intell. Rev. **37**(2), 97–117 (2012). [https://​doi.​org/​10.​1007/​s10462-011-9221-2](https://doi.org/10.1007/s10462-011-9221-2)<https://doi.org/10.1007/s10462-011-9221-2>
25. 25.

    Zhang, Y., Miller, T., Sonenberg, L.: Explainable AI: A conceptual modeling perspective. In: Proceedings of the 38th International Conference on Conceptual Modeling (ER), pp. 473–485. Springer, Berlin (2020)
26. 26.

    Thakar, A.A., Kumar, K., Patel, B.: Next generation digital forensic investigation model (NGDFIM) - enhanced, time reducing and comprehensive framework. J. Phys. Conf. Ser. **1767**(1), 012054 (2021). [https://​doi.​org/​10.​1088/​1742-6596/​1767/​1/​012054](https://doi.org/10.1088/1742-6596/1767/1/012054)<https://doi.org/10.1088/1742-6596/1767/1/012054>
27. 27.

    Zawoad, S., Hasan, R.: Digital forensics in the age of big data: Challenges, approaches, and opportunities. In: Proceedings of the IEEE 17th International Conference on High Performance Computing and Communications, pp. 1320–1325 (2015). [https://​doi.​org/​10.​1109/​HPCC-CSS-ICESS.​2015.​305](https://doi.org/10.1109/HPCC-CSS-ICESS.2015.305)

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_5>

# 5. ExperDF-CM: A Digital Forensics Controlled Experiments Conceptual Model

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter presents the **ExperDF-CM (Digital Forensics Controlled Experiments Conceptual Model)** as a structured framework for the design, execution, and documentation of controlled experiments in Digital Forensics. Building upon the conceptual foundations discussed in the previous chapter, ExperDF-CM operationalizes the principles of conceptual modeling into a comprehensive methodological approach that promotes rigor, reproducibility, and transparency in empirical research. The model integrates established experimental practices with the distinctive characteristics of forensic investigation, providing a systematic means to represent, analyze, and communicate experimental processes. The chapter begins by outlining the motivations for developing a dedicated conceptual model for Digital Forensics, emphasizing the need to address fragmented documentation, inconsistent methodological reporting, and limited reproducibility. It then introduces the ExperDF-CM framework as a solution to these challenges, structured around five interrelated concepts that collectively describe the entire experimental life cycle: *Planning*, *Pre-Operation*, *Operation*, *Analysis and Interpretation*, and *Dissemination*. Each concept encapsulates a specific stage in the experiment process, detailing its objectives, inputs, activities, and expected outcomes while maintaining explicit relationships with the others to ensure traceability and coherence. In the *Planning* phase, researchers define the purpose, hypotheses, variables, and ethical considerations that guide the study. The *Pre-Operation* phase establishes the preparatory conditions, including dataset selection, tool configuration, and environment calibration. The *Operation* phase corresponds to data collection and experimental execution, during which procedures are documented in a clear, transparent, and auditable manner. The *Analysis and Interpretation* phase focuses on evaluating data, applying statistical reasoning, and providing contextual interpretation of results. Finally, the *Dissemination* phase emphasizes open sharing of data, methods, and findings to enable replication, meta-analysis, and cumulative learning. Throughout these stages, ExperDF-CM promotes alignment with open science principles by encouraging standardized documentation, provenance tracking, and the use of persistent identifiers to ensure accessibility and long-term preservation of research artifacts. It also supports ethical compliance by integrating mechanisms for accountability and responsible handling of digital evidence. By bridging experimental design and forensic application, the model fosters both methodological rigor and practical reliability, contributing to the credibility of Digital Forensics as a scientific discipline. Ultimately, this chapter positions ExperDF-CM as a foundational step toward consolidating Digital Forensics as an evidence-based, transparent, and reproducible research domain. By uniting conceptual modeling theory with forensic experimentation practice, it establishes a blueprint for future frameworks that aim to strengthen the scientific integrity and societal trustworthiness of digital investigations.

## 5.1 The ExperDF-CM Conceptual Model

The Experimentation in Digital Forensics Conceptual Model (ExperDF-CM) [[1](#CR1)] was designed to improve the methodological rigor of Digital Forensics (DF) controlled experimentation. Digital Forensics research often lacks structured guidelines for planning and reporting, thereby limiting reproducibility and reducing the scientific credibility of results. To address this gap, the ExperDF-CM conceptual model introduces a framework that helps researchers systematically organize controlled experiments. By doing so, it ensures that key elements of an experiment are explicitly defined and consistently documented.

This model is based on the analysis of more than 200 DF-related experiments, which revealed recurring weaknesses, including insufficient planning detail, missing descriptions of experimental conditions, and inadequate data availability. The ExperDF-CM responds to these issues by structuring experiments into five main concepts: Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination. Each of these elements contributes to building a coherent path from hypothesis formulation to the communication of results.

The overall goal of ExperDF-CM is to enable experiments that are not only repeatable by the original researchers but also replicable by independent groups and even reproducible under different contexts. In practice, this approach fosters transparency, promotes comparability of results, and facilitates meta-analysis. As such, ExperDF-CM is positioned as a foundation for more reliable and auditable DF experimentation.

Figure [5.1](#Fig1) illustrates the overall structure of the ExperDF-CM conceptual model, showing the five main concepts and their relationships, which together provide a roadmap for conducting reproducible digital forensic controlled experiments.

![Flow chart depicting the process of a DF experiment. The central box labeled “DF Experiment” connects to several other boxes. “Planning” leads to “DF Experiment” with the label “Has.” “DF Experiment” connects to “Analysis and Interpretation” with “Provides.” “Analysis and Interpretation” connects to “Dissemination” with “Reports.” “Pre-Operation” and “Operation” both connect to “DF Experiment” with “Runs.”](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig1_HTML.png)

Fig. 5.1

Overview of the high-level ExperDF-CM conceptual model [[1](#CR1)]

### 5.1.1 The Planning Concept

The Planning concept represents the cornerstone of the ExperDF-CM model. This phase establishes the theoretical and methodological foundation of the experiment, defining not only the objectives but also the mechanisms by which these objectives will be achieved. Proper planning involves identifying independent and dependent variables, formulating hypotheses, and clearly defining the scope and boundaries of the investigation. Clarity and precision in this stage are essential to ensure that subsequent phases remain consistent and scientifically valid.

Figure [5.2](#Fig2) illustrates the Planning concept, detailing hypotheses, variables, instruments, participants, design types, and their interconnections.

![Flowchart illustrating the planning process for scientific experiments. It begins with an “Experimental Unit” leading to “Variable,” which branches into “Dependent Variable” and “Independent Variables.” These connect to “Dependent Variable Metric,” “Factor,” “Pre-Fixed,” “Treatment,” and “Control.” “Design Type,” “Instrument,” and “Objective” are also linked, with further connections to “Instrument Validation Technique” and “Instrument Type.” The central “Planning” node connects to “Experiment Type,” “DF Analysis,” “DF Reporting,” “Participant,” and “Hypothesis.” “Experiment Type” includes “Original Experiment,” “Replication Experiment,” “Internal Replication,” and “External Replication.” “Hypothesis” branches into “Null Hypothesis” and “Alternative Hypothesis.” “Participant” involves “Sampling,” “Profile,” “Non-Probabilistic,” and “Probabilistic” methods.](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig2_HTML.png)

Fig. 5.2

The planning concept [[1](#CR1)]

In ExperDF-CM, independent variables are controllable factors that can influence outcomes. In contrast, dependent variables are the observable measures used to evaluate the effect of these factors on the outcomes. This cause-and-effect structure enables for rigorous hypothesis testing. Hypotheses are further categorized into null and alternative hypotheses, allowing experiments to statistically validate or reject assumptions. A poorly defined hypothesis often yields inconclusive findings, underscoring the importance of carefully designing this element.

Another crucial aspect of planning is determining the experimental unit, which defines the smallest division of analysis. For example, in network forensic studies, a packet may serve as an experimental unit. Planning also encompasses the choice of design type, whether factorial, randomized, or comparative. These design decisions directly impact the statistical methods required later in the analysis phase.

Planning extends beyond variables and hypotheses to include instruments and participants. Instruments, whether forensic tools, questionnaires, or specialized software, must be validated using established methods such as Principal Component Analysis or inter-rater reliability coefficients. For human-centered studies, the sampling strategy must also be defined; probabilistic or non-probabilistic sampling methods affect the generalizability of the results. Being located within a specific phase of the forensic process, such as acquisition, examination, analysis, or reporting, ensures that the findings are adequately contextualized within forensic practice.

### 5.1.2 The Pre-Operation Concept

The Pre-Operation [[1](#CR1)] ensures that the experiment is ready to be executed under controlled and reliable conditions. It emphasizes the careful preparation of software, hardware, and algorithms, which together constitute the experimental setup. Forensic tools must be configured correctly, operating systems and applications must be installed, and virtual environments must be prepared. This step minimizes unexpected interferences that could invalidate the experiment.

Figure [5.3](#Fig3) illustrates the Pre-Operation concept, which includes preparing software, hardware, algorithms, and training, as well as conducting pilot projects.

![Flowchart illustrating a process starting with “Scenario,” leading to “Pilot Project,” “Training,” and “Benchmark.” These define “Pre-Operation,” which further defines “Setup.” “Setup” branches into “Software” and “Algorithm.” “Software” includes “Virtual Machine,” “Operating System,” and “Application.” “Algorithm” has “Parameter.” “Hardware” is connected to both “Volatile Memory” and “Persistent Memory.” “Volatile Memory” includes “RAM” and “Cache,” while “Persistent Memory” includes “Hard Disk Drive” and “Solid State Drive.” Arrows indicate the flow and relationships between elements.](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig3_HTML.png)

Fig. 5.3

The Pre-Operation concept [[1](#CR1)]

Software preparation involves selecting virtual machines, operating systems, and forensic applications. For example, installing forensic recovery software or configuring memory acquisition tools in virtual environments ensures consistency across repeated trials. Hardware preparation, on the other hand, focuses on defining configurations for volatile and persistent memory, such as RAM and SSDs. Proper documentation of these choices is crucial for replication.

Algorithms play an equally central role in this phase. They may require parameter calibration to adapt to specific datasets or forensic scenarios. Benchmark datasets are often used for training purposes, allowing researchers to refine algorithms and instruments before the actual experiment begins. Training is not limited to algorithms; it may also involve participants to ensure that they understand the tasks and tools involved.

A final, but vital, step is the execution of a pilot project. The pilots serve as miniature versions of the entire experiment, testing the readiness of the instruments, infrastructure, and participants. They identify flaws or inconsistencies that might otherwise compromise the main study. In this way, Pre-Operation functions as a safeguard, bridging the theoretical constructs of planning with the empirical reality of execution.

### 5.1.3 The Operation Concept

The Operation phase [[1](#CR1)] marks the practical execution of the experiment, where the procedures designed in the planning stage are applied. It relies heavily on the precision of predefined procedures that describe tasks, their order, and the roles of participants or systems. Adherence to these procedures ensures consistency and minimizes the risks of false positives and false negatives.

Figure [5.4](#Fig4) illustrates the Operation concept, including procedures, participants, instruments, and data collection methods.

![Flow chart illustrating a process involving several components: “Operation Procedure” leads to “Operation,” which is influenced by “Participant” using an “Instrument.” The “Instrument” performs over “Operation” and produces “Data.” “Operation” collects “Sample,” forming “Data,” which is categorized as “Original Data” or “Duplicated Data.” Arrows indicate the flow and relationships between these elements.](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig4_HTML.png)

Fig. 5.4

The Operation concept [[1](#CR1)]

Central to this phase is data collection. Depending on the experiment, data may be obtained from human participants, forensic software, or automated processes. Importantly, ExperDF-CM distinguishes between original and duplicated data. Original data refers to the primary evidence collected from digital sources, while duplicated data preserves this information for repeated testing without altering the original.

The operation also stresses the importance of documenting instruments and procedures. Every tool used, from forensic disk images to benchmark datasets, must be fully described. This transparency ensures reproducibility and allows independent researchers to validate findings. This rigorous documentation transforms the operation from a one-time event into a reusable scientific process.

When participants are involved, their interactions provide valuable data. Proper training conducted during the Pre-Operation stage ensures that participants contribute reliably. Ultimately, the Operation phase provides the empirical evidence required for the later phases of analysis and dissemination.

### 5.1.4 The Analysis and Interpretation Concept

Once data is collected, it must be systematically analyzed and interpreted. This phase transforms raw data into meaningful results through statistical and qualitative methods. Visualization techniques such as tables, charts, boxplots, and histograms aid in organizing and exploring the data. Proper visualization provides clarity, making it easier to identify patterns and anomalies.

Figure [5.2](#Fig2) illustrates the Analysis and Interpretation concept, which includes visualization, analysis techniques, limitations, and validity threats (Fig. [5.5](#Fig5)).

![The image is a flow chart illustrating various statistical analysis techniques. It begins with two main branches: Qualitative Analysis and Quantitative Analysis. Under Qualitative Analysis, methods like Manual Verification, Focus Group, and Other Qualitative Techniques are listed. Quantitative Analysis includes Descriptive Statistics, Normality Test, Hypothesis Test, Correlation, and Regression. The chart further details tools such as Tendency Line Chart, Boxplot, Table, Word Cloud, and Data Plotting. It also addresses Analysis Techniques, Limitations, and Threats to Validity, including External, Construct, Internal, and Conclusion Validity. The flow chart connects these elements with arrows indicating the flow of analysis processes.](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig5_HTML.png)

Fig. 5.5

The Analysis and Interpretation concept [[1](#CR1)]

Statistical analysis lies at the heart of this phase. Normality tests, such as the Shapiro–Wilk or Kolmogorov–Smirnov tests, determine whether the datasets follow the expected distributions. Based on these results, appropriate hypothesis tests, parametric or nonparametric, are applied. For example, t-tests, ANOVA, or Wilcoxon tests may be used depending on the data characteristics. This statistical rigor ensures that the findings are supported by evidence rather than conjecture.

Beyond hypothesis testing, advanced methods such as correlation and regression help uncover relationships between variables. Correlation identifies associations, while regression models can predict outcomes based on independent variables. These techniques deepen the understanding of digital forensic processes and provide evidence for broader generalizations.

Transparency in analysis also requires discussing limitations and threats to validity. Internal validity concerns whether the treatment really causes the observed effects. External validity addresses the generalizability of the findings beyond the study’s context. Construct validity assesses the alignment between theoretical concepts and their measurement, while internal validity ensures that conclusions are correctly derived from the data. Addressing these aspects improves confidence in the experiment and guides replication efforts.

### 5.1.5 The Dissemination Concept

The final stage of ExperDF-CM is Dissemination [[1](#CR1)], which ensures that the knowledge gained from the experiment is shared and reusable. At its core, dissemination involves making datasets, metadata, and documentation publicly available through trusted repositories. The assignment of persistent identifiers, such as DOIs, allows datasets to remain accessible and citable, thus supporting long-term reproducibility.

Figure [5.6](#Fig6) illustrates the Dissemination concept, including datasets, repositories, citations, annotations, and data management plans.

![Flowchart illustrating the relationships and processes involving a data set. Central to the chart is the “Data Set” box, which is connected to several other elements. “Repository” and “Unique ID” are linked to the data set, indicating storage and identification. “Citation” and “Authorship” are also connected, showing citation and authorship relationships. “Data Set Metadata” is linked via “shared via,” and “Data Forensics Management Plan” is connected through “documents.” “Dissemination” shares with “Diary/Annotation” and provides to “Data Forensics Management Plan.” “Experimental Issues” is documented by “Diary/Annotation.”](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig6_HTML.png)

Fig. 5.6

The Dissemination concept [[1](#CR1)]

Dissemination is not limited to datasets. It also includes a detailed documentation of the authorship, experimental annotations, and issues encountered during execution. Such transparency allows future researchers to understand the rationale behind decisions, recognize challenges, and avoid repeating mistakes. This culture of openness fosters the building of cumulative knowledge in the DF community.

Another key element is the Data Management Plan (DMP), which defines how data will be preserved, documented, and accessed. Metadata, in particular, plays a vital role in ensuring that datasets are interpretable and reusable. By embedding dissemination into the experimental workflow, ExperDF-CM aligns with broader open science practices, contributing to greater visibility, trust, and impact of digital forensic research.

Dissemination, therefore, is not the end of an experiment, but the beginning of its life in the broader scientific community. It ensures that the results are not confined to a single study but become part of a collective effort to advance forensic science.

## 5.2 Applying the ExperDF-CM to Model Digital Forensics Controlled Experiments

Although the ExperDF-CM conceptual model was designed to address methodological shortcomings in Digital Forensics (DF) research, its actual value emerges when applied in practice.

This section proposes a structured approach for using ExperDF-CM to model controlled experiments. The goal is to demonstrate how each of the five main concepts, Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination, can be operationalized within a real or hypothetical DF experiment. By following this roadmap, researchers can ensure that their studies achieve higher reproducibility, transparency, and scientific rigor.

### 5.2.1 Step-by-Step Modeling with ExperDF-CM

The use of ExperDF-CM begins with the clear identification of a research question. For example, an investigator might ask whether a specific memory acquisition tool performs more reliably than an alternative under certain operating system conditions. Using the Planning concept, the researcher defines hypotheses, independent and dependent variables, and determines the type of experimental design. This provides the foundation for all subsequent activities.

In the Pre-Operation stage, the researcher prepares the experimental environment. This involves configuring virtual machines, installing forensic tools, calibrating parameters, and conducting a pilot study to ensure stability. This preparation reduces the risk of bias and ensures that any variations in results can be attributed to controlled changes, rather than uncontrolled external factors.

The Operation phase is where the experiment is executed under the designed conditions. Data collection procedures are strictly followed, ensuring the integrity of the original evidence is maintained while allowing duplicates for testing. The subsequent Analysis and Interpretation phase then employs statistical methods to evaluate the hypotheses. This involves testing for statistical significance, identifying correlations, and discussing threats to validity. Finally, the Dissemination concept ensures that datasets, scripts, and documentation are made available through repositories with proper metadata and citations, thereby supporting replication and long-term reuse.

### 5.2.2 Illustrative Roadmap

To help researchers adopt ExperDF-CM, Fig. [5.7](#Fig7) presents a roadmap that aligns each model stage with practical tasks and outcomes. The roadmap illustrates the model’s linear and iterative nature. Although phases are described sequentially, feedback loops are possible when pilot studies or analysis reveal the need to revisit earlier decisions.

![Flowchart illustrating a scientific process. The steps are as follows: 1. Define hypotheses, variables, design, instruments. 2. Prepare environment, software, hardware, pilot tests. 3. Execute procedures, collect data, ensure integrity. 4. Apply statistics, discuss limitations, test hypotheses. 5. Share datasets, artifacts, metadata, repositories, DMP. A dashed line connects the first step to a note: “Pilot the experiment, adjust setup.”](../images/624027_1_En_5_Chapter/624027_1_En_5_Fig7_HTML.png)

Fig. 5.7

Roadmap for applying the ExperDF-CM to model controlled experiments in Digital Forensics. Each phase defines concrete tasks and outputs, with feedback loops allowing refinement of earlier stages

### 5.2.3 ExperDF-CM Support for Registered Reports and Ethical Approval Preparation

A significant extension of ExperDF-CM’s application is its role in preparing registered reports before any data collection. A registered report is a publication format in which the experimental design, hypotheses, and planned analyses are peer-reviewed and approved in advance. Using ExperDF-CM as a guide ensures that the report is complete, systematic, and transparent. Each of the five phases of the model provides the details reviewers need to evaluate the experimental plan’s soundness.

In addition, many Digital Forensics studies involve sensitive data, human participants, or potential ethical risks. In such cases, an ethics committee or institutional review board must approve the survey before it is executed. The ExperDF-CM framework facilitates the generation of documentation required for this approval, including clear descriptions of data handling procedures, anonymization strategies, and dissemination practices. By integrating ethical considerations from the outset, researchers strengthen both the validity of their work and the societal trust in it.

Thus, ExperDF-CM not only structures scientific rigor but also supports compliance with open science standards and ethical oversight mechanisms. This dual role makes it a practical tool for researchers seeking to produce replicable, responsible, and ethically sound forensic experiments.

## 5.3 Final Remarks

The **ExperDF-CM** model consolidates the methodological foundations required to advance Digital Forensics as a cumulative, evidence-based, and transparent scientific discipline. By translating the principles of conceptual modeling into a practical framework for controlled experimentation, ExperDF-CM provides a structured path for researchers to design, execute, and communicate studies that are verifiable, comparable, and reproducible. Each of its five interconnected concepts (*Planning*, *Pre-Operation*, *Operation*, *Analysis and Interpretation*, and *Dissemination*) contributes to a coherent and traceable research life cycle that integrates rigor, openness, and ethical responsibility.

Through its emphasis on planning and documentation, the model ensures that research objectives, hypotheses, and ethical considerations are made explicit from the outset. In the preparatory and operational stages, it supports transparency in dataset selection, tool configuration, and procedural control, minimizing variability and enhancing the reliability of results. During analysis and interpretation, ExperDF-CM fosters critical reflection on the validity and generalizability of findings. At the same time, dissemination reinforces open science principles by encouraging the publication of data, methods, and outcomes in accessible, interoperable formats.

Beyond methodological structuring, ExperDF-CM plays a transformative role in shaping a culture of accountability and scientific integrity in Digital Forensics. Its use facilitates the preparation of registered reports, ethical review documents, and provenance records, ensuring compliance with scientific and societal expectations. The model’s orientation toward openness and documentation also promotes interoperability with metadata standards and ontologies, such as those supporting the FAIR principles, enabling seamless integration with repositories, registries, and digital libraries.

As Digital Forensics continues to evolve in response to emerging technologies and complex investigative scenarios, ExperDF-CM provides a flexible yet rigorous foundation for adaptation and extension. Future work may incorporate semantic modeling, automated experimental workflows, and provenance-driven traceability to strengthen reproducibility and long-term verifiability further. The model thus serves as both a methodological framework and a vision for the next generation of forensic science research, where controlled experimentation, ethical compliance, and open collaboration coexist as fundamental pillars.

In conclusion, ExperDF-CM represents more than just a tool for experimental organization. It embodies a scientific paradigm that aligns Digital Forensics with broader movements toward open, transparent, and reproducible research. By embedding conceptual clarity into empirical practice, the model contributes to establishing a robust foundation for generating trustworthy digital evidence and continually improving forensic knowledge.

## References

1. 1.

   OliveiraJr, E., Zorzo, A.F., Neu, C.V.: Towards a conceptual model for promoting digital forensics experiments. Forensic Sci. Int. Digit. Investig. **35**, 301014 (2020). [https://​doi.​org/​10.​1016/​j.​fsidi.​2020.​301014](https://doi.org/10.1016/j.fsidi.2020.301014)

# Part III Formal Representation and Semantic Integration of Digital Forensics Controlled Experiments

This part extends the conceptual and methodological structures established in the previous parts into the semantic domain, where knowledge representation, interoperability, and machine reasoning become central. It focuses on formalizing Digital Forensics experiments in ways that allow their components, relationships, and provenance to be explicitly described, queried, and reused. By leveraging ontological modeling and semantic technologies, this part consolidates the bridge between conceptual modeling, experimental documentation, and computational knowledge management.

Ontologies provide the formal backbone for structuring information in a way that is both human-understandable and machine-actionable. In Digital Forensics, they enable consistent representation of entities such as evidence, procedures, datasets, and results, ensuring that experimental knowledge can be linked, queried, and preserved across different platforms and studies. This formalization supports transparency, enhances interoperability, and facilitates the reproducibility of controlled experiments, aligning the field with the principles of open science and FAIR data management.

Chapter [6](624027_1_En_6_Chapter.xhtml) introduces the fundamental principles of ontological modeling and semantic query mechanisms, particularly focusing on the use of SPARQL as a tool for accessing and analyzing structured experimental data. It discusses how ontology-based approaches can extend conceptual models by introducing formal semantics that enable the automatic integration and validation of information. The chapter also presents the **ExperDF-Portal**, an online platform designed to support the management and execution of controlled experiments in Digital Forensics. Through the portal, researchers can visualize experimental artifacts, define data acquisition strategies, document investigation steps, and manage the life cycle of experimental processes. The integration between conceptual and semantic layers exemplifies how digital experiment management can evolve toward more transparent, reproducible, and connected practices.

Chapter [7](624027_1_En_7_Chapter.xhtml) presents the **ExperDF-Onto Ontology**, which formalizes the structure and semantics of the ExperDF-CM model introduced earlier. It defines a vocabulary of classes, properties, and relationships that describe the elements of controlled experiments, from planning to dissemination. The ontology aligns with internationally recognized standards such as Dublin Core and the PROV family, ensuring compatibility with other research infrastructures and metadata frameworks. The chapter also demonstrates the use of SPARQL queries to retrieve, integrate, and analyze experimental metadata, illustrating how semantic technologies can support provenance tracking, validation, and reuse of forensic research data.

Together, these chapters establish a semantic foundation for the management and exchange of experimental knowledge in Digital Forensics. They demonstrate how ontological modeling, combined with practical implementation through the ExperDF-Portal and ExperDF-Onto, transforms static documentation into a living, interoperable knowledge ecosystem. This integration strengthens the scientific value of experiments, supports data-driven collaboration, and contributes to the long-term sustainability of research assets in Digital Forensics.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_6>

# 6. Basics of Ontology and SPARQL Queries

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter provides a comprehensive and integrated exploration of ontologies, from their philosophical foundations to their technological implementation and practical application in Digital Forensics. It begins by revisiting the origins of ontology in classical philosophy, where thinkers such as Aristotle and Wolff first sought to describe the nature and categories of being. These early metaphysical inquiries evolved into modern formal systems for representing knowledge, giving rise to ontologies as computational artifacts that enable structured, explicit, and machine-readable conceptualizations of domains. By bridging abstract philosophical reasoning and formal logic, ontologies have become indispensable instruments for organizing knowledge, ensuring semantic interoperability, and supporting intelligent decision-making. The chapter proceeds to define the essential components of ontologies, including classes, subclasses, relations, axioms, and instances, and explores their typology according to domain scope, formalism, and purpose. Through this lens, it distinguishes between generic, domain, task, application, and representation ontologies, demonstrating how each serves different modeling needs. These theoretical aspects are complemented by methodological insights on ontology construction and evaluation, emphasizing clarity, consistency, and reusability as key design principles. Building on this conceptual groundwork, the chapter presents the Semantic Web framework as the technical environment in which ontologies operate. It explains how the Resource Description Framework (RDF) enables data to be represented as triples within a graph model, how the Web Ontology Language (OWL) introduces expressivity for logical constraints and reasoning, and how the SPARQL query language allows users to navigate and manipulate semantic data. Detailed examples and visual representations illustrate the structure of RDF triples, the formal capabilities of OWL axioms, and the syntax of SPARQL queries used for pattern matching, data integration, and federated querying across distributed knowledge bases. The chapter also examines the ecosystem of tools and technologies that facilitate the creation and use of ontologies, including ontology editors such as Protégé and querying platforms like Apache Jena, as well as public SPARQL end points. These tools form a practical bridge between theoretical models and real-world applications, enabling researchers and practitioners to model complex domains, verify logical consistency, and query large semantic datasets. In its applied dimension, the chapter focuses on the role of ontologies in Digital Forensics. It demonstrates how formal knowledge models can represent digital evidence, describe investigative processes, and support event reconstruction with enhanced precision and traceability. Ontologies promote interoperability among forensic tools, standardize documentation practices, facilitate anomaly and pattern detection, and aid in the recovery and correlation of fragmented or hidden data. By formalizing concepts such as evidence types, acquisition methods, and analysis steps, ontologies contribute to the development of more rigorous and reproducible forensic investigations. Finally, the chapter situates ontology-based reasoning within the broader context of Open Science. By encouraging transparent representation, structured documentation, and machine-assisted querying of forensic data, ontologies reinforce the principles of reproducibility, ethical accountability, and collaborative validation. This integration of philosophical insight, computational logic, and forensic practice highlights ontologies not merely as technical schemas but as epistemological frameworks that serve as foundations for reasoning, discovery, and trustworthy science. In doing so, the chapter underscores that the future of Digital Forensics research lies in the convergence of semantic modeling, intelligent analytics, and open, reproducible methodologies that advance both scientific rigor and societal responsibility.

## 6.1 Conceptual Foundations of Ontologies

Ontologies have become fundamental tools in both philosophy and computer science, serving as structured frameworks to represent, organize, and reason about knowledge. Their origins lie in classical philosophy, where ontologies were developed to explore the nature of being, existence, and the properties of reality. Over time, these conceptual foundations have been adapted to the fields of information systems and computing, where ontologies provide formal representations of domains, facilitating semantic interoperability, data integration, and artificial intelligence applications.

The following subsections explore ontologies from two complementary perspectives. The first subsection, *Philosophical Foundations and the Evolution of Ontologies into Computing*, presents the historical development of ontology as a concept, tracing its philosophical roots and its transition into computational frameworks. This section highlights how classical philosophical inquiry laid the groundwork for formal knowledge representation and reasoning.

The second subsection, *Definition, Characteristics, Typology, and Applications of Ontologies*, provides a detailed overview of the structure, classification, and practical applications of ontologies. It explains the core components of ontologies, their typologies, and the methodologies used in their construction. To facilitate understanding, Table [6.1](#Tab1) summarizes the ontology types, formalisms, structures, contents, and applications, while Fig. [6.1](#Fig1) visually represents the hierarchical relationships among these dimensions.

![Flowchart illustrating the structure of ontologies, divided into five main categories: Generic, Domain, Task, Application, and Representation. Each category branches into subcategories detailing formation, structure, and content. For example, the Generic category includes “Formation: Highly Informal to Semi-Formal” and “Structure: Meta-Level Structure,” leading to “Content: Generic Concepts” and “Application: Knowledge Sharing.” Other categories follow a similar pattern, emphasizing different aspects like domain knowledge, task knowledge, and system implementation.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig1_HTML.png)

Fig. 6.1

Integrated hierarchy of ontology types, formalism, structure, content, and applications. Each branch represents a specific ontology type and shows its corresponding formalism, structural organization, content focus, and typical applications. This figure complements Table [6.1](#Tab1) by visually summarizing the relationships among ontology dimensions

Table 6.1

Comprehensive summary of ontology types, formalism, structure, content, and applications

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | Structure/content |  |
| Ontology type | Scope/domain | Formalism | focus | Applications |
| Generic | Broad foundational concepts (space, time, matter, events, objects) | Highly Informal to Semi-formal | Neutral authorship; covers generic content | Knowledge sharing across multiple domains; conceptual framework development |
| Domain | Specific field (e.g., medicine, law, computing) | Semi-formal to Strictly Formal | Specification; structured domain content | Domain knowledge modeling; interoperability; decision support in specific fields |
| Task | Activity- or problem-specific processes | Semi-formal to Strictly Formal | Specification; captures workflow and task relationships | Process modeling; business or scientific workflow representation; AI planning |
| Application | Integrates domain + task knowledge for practical purposes | Semi-formal to Strictly Formal | Specification/ Shared Access; application-focused content | Requirements engineering; system design; domain-specific application support |
| Representation | Abstract and formalized structures across domains | Strictly Formal | Neutral/Shared Access; formal content modeling | Formal knowledge representation; reasoning; semantic frameworks; AI ontologies |
| Terminological | Linguistic terms and definitions | Highly Informal to Semi-formal | Neutral authorship; focuses on terminology | Language processing; glossary development; metadata organization |
| Information | Data structures and properties (schemas) | Semi-formal | Specification; information-focused | Database integration; information retrieval; structured data analysis |
| Knowledge modeling | Conceptual structures of a domain | Semi-formal to Strictly Formal | Specification; domain knowledge focus | Knowledge reasoning; decision support; AI applications |

Together, these subsections provide a comprehensive understanding of ontologies, bridging their theoretical origins with their practical implementation in computational systems. This integrated view is essential for researchers, practitioners, and students who seek to leverage ontologies for knowledge representation, information management, and the development of intelligent systems.

### 6.1.1 Philosophical Foundations and the Evolution of Ontologies into Computing

Ontology originated in classical philosophy as a discipline concerned with the study of being, existence, and the fundamental structure of reality [[18](#CR18)]. Early philosophers such as Parmenides and Heraclitus explored ontological questions regarding permanence, change, and the properties of the physical world [[7](#CR7), [21](#CR21)]. Aristotle (384–322 BC) systematized these concepts, introducing formal categories to describe reality and analyzing the persistence and subsistence of entities [[23](#CR23)]. These early contributions established the conceptual tools for understanding entities, their properties, and relationships, concepts that later became central to formal knowledge representation.

The term “ontology” itself emerged later in philosophical discourse. In 1613, philosophers such as Rudolf Göckel (Goclenius) and Jacob Lorhard (Lorhardus) discussed the term in the *Theatrum philosophicum* [[19](#CR19)]. It was not until 1721 that the term appeared in an English dictionary, defined as a Greek expression meaning “to be” [[17](#CR17)]. This historical evolution provided a conceptual foundation for ontology to transition from abstract philosophical inquiry to structured frameworks suitable for modeling knowledge across various domains.

In the 1980s, ontologies began to be systematically studied in information systems and computer science as formal structures to represent domain knowledge, organize semantic information, and enable reasoning [[5](#CR5), [17](#CR17)]. In this context, ontologies provide frameworks for categorizing entities, defining relationships, and ensuring consistency, which facilitates interoperability and knowledge sharing between systems. Their formalization allows both humans and machines to query, reason about, and analyze domain-specific knowledge efficiently.

Within computing, ontologies serve as formal languages for modeling specific domains [[8](#CR8)]. They were initially employed in artificial intelligence to represent logical vocabularies, semantic relationships, and knowledge structures [[12](#CR12)]. By organizing knowledge into classes, instances, relations, and axioms, ontologies form the basis of knowledge bases that can be expanded and queried. This enables precise reasoning, data integration, and the development of intelligent applications that bridge human understanding with machine-processable representations.

Moreover, ontologies facilitate interoperability between heterogeneous datasets, support information retrieval through structured semantic relationships, and provide a foundation for software engineering applications, including system specification and AI-based decision support. Thus, the evolution of ontologies from philosophical concepts to computational frameworks illustrates their adaptability and enduring relevance across disciplines.

### 6.1.2 Definition, Characteristics, Typology, and Applications of Ontologies

Ontologies can be formally defined as explicit specifications of conceptualizations, encompassing entities, concepts, classes, subclasses, functions, relationships, and axioms [[6](#CR6)]. They serve as structured frameworks that capture domain knowledge in a formalized manner, enabling reasoning, interoperability, and systematic organization of information. Noy and McGuinness [[13](#CR13)] highlight the interpersonal dimension of ontology construction, emphasizing that the vocabulary used to describe reality is shaped by shared logical predicates and conceptual agreements among experts or communities.

Ontologies are characterized by core components that define their structure and functionality:

* **Relations:** define interactions among entities, capturing domain complexity, often reusable across multiple ontologies
* **Axioms:** logical statements representing rules, assumptions, and constraints within the domain
* **Instances:** concrete examples of classes; actual objects, events, or entities
* **Classes:** abstractions representing sets of entities sharing common properties
* **Functions:** operations or transformations applied to entities
* **Subclasses:** hierarchical subdivisions of classes to represent specialization and inheritance

Ontologies can be classified by type, formalism, structure, content, and application. Table [6.1](#Tab1) provides a comprehensive summary of all major ontology classifications and their uses:

The construction of ontologies follows structured methodologies to ensure coherence, consistency, and alignment with intended conceptual frameworks [[1](#CR1)]. Methodologies may be **classical**, relying on domain experts, or **consensus-based**, incorporating multiple stakeholders to achieve shared understanding. Ontologies support a variety of practical applications:

* **Knowledge Representation:** capturing and formalizing domain knowledge for reasoning and decision-making
* **Data Integration:** harmonizing heterogeneous datasets through a shared conceptual framework
* **Information Retrieval:** enhancing search and query mechanisms using structured semantic relationships
* **Software Engineering and AI:** supporting system specification, interoperability, and intelligent application development

Figure [6.1](#Fig1) visually represents the hierarchy of ontology types and their relationships to formalism, structure, content, and applications, complementing Table [6.1](#Tab1).

Therefore, ontologies serve as structured, formal representations of knowledge that facilitate understanding, reasoning, and interoperability across multiple domains. By integrating their philosophical origins, structural characteristics, typology, and practical applications, ontologies provide a robust framework for organizing both conceptual and computational knowledge. The combination of Table [6.1](#Tab1) and Fig. [6.1](#Fig1) offers a comprehensive view of the ontology landscape, illustrating the diversity of ontology types, their methodological foundations, and their relevance for knowledge-intensive applications in artificial intelligence, information systems, and domain-specific modeling.

### 6.1.3 Specifying Ontologies with OWL and RDF

Ontologies on the Semantic Web can be specified using the Resource Description Framework (RDF) and the Web Ontology Language (OWL). Although the W3C defines both standards as being closely related, they serve different purposes and operate at distinct levels of expressivity. RDF provides the foundational data model for representing information in the form of subject–predicate–object triples, enabling a flexible graph-based structure for describing resources and their attributes. It establishes the syntax and framework through which statements can be made about entities, and with RDF Schema (RDFS), it supports lightweight schema definitions such as class hierarchies and property constraints.

In contrast, OWL builds on top of RDF and RDFS, extending their capabilities with richer constructs derived from Description Logics. While RDF focuses on describing resources and basic schemas, OWL is designed to capture complex relationships, logical restrictions, and axioms that allow automated reasoning. With OWL, it is possible to define class equivalence, disjointness, property characteristics, and cardinality restrictions, supporting advanced inferences that go far beyond the structural expressivity of RDF alone.

The main differences between RDF and OWL are summarized in Table [6.2](#Tab2), which highlights their roles, expressivity, reasoning support, and typical applications. This comparison makes clear that RDF provides the foundational layer for representing and sharing structured data, while OWL delivers the expressive power necessary for formal ontology modeling and automated inference.

Table 6.2

Comparison between RDF and OWL for ontology specification

| Aspect | RDF / RDFS | OWL |
| --- | --- | --- |
| Primary role | Data model for representing triples (subject–predicate–object) | Ontology language extending RDF with formal semantics |
| Expressivity | Describes resources, literals, and simple class/property hierarchies | Defines complex class relationships, property characteristics, restrictions, and axioms |
| Semantics | Provides basic semantics for resources, classes, and properties | Based on Description Logics, enabling rigorous logical reasoning |
| Inference support | Limited: type inheritance, domain/range implications | Rich: class subsumption, consistency checking, equivalence, disjointness, cardinality |
| Serialization | Turtle, RDF/XML, N-Triples, JSON-LD | Turtle, RDF/XML, Manchester Syntax, Functional Syntax |
| Typical use | Interoperability of data across systems; lightweight schema definition | Formal ontology modeling; applications needing reasoning (e.g., biomedical ontologies) |

Therefore, RDF provides the essential foundation for representing and sharing data, while OWL supplies the expressive formalism required for modeling sophisticated ontologies and enabling reasoning. Together, they form complementary layers in the Semantic Web stack: RDF ensures interoperability at the data level, and OWL empowers semantic richness and logical inference for ontology-driven applications.

#### 6.1.3.1 The Resource Description Framework (RDF)

The RDF is a foundational standard of the Semantic Web, developed under the auspices of the World Wide Web Consortium (W3C) to enable the interchange of structured data on the web. RDF provides a simple yet powerful data model based on directed labeled graphs, where information is represented as *triples* consisting of a subject, a predicate, and an object. This graph-based model allows the integration of heterogeneous data sources, the sharing of machine-readable knowledge, and the possibility of reasoning over distributed information.

Historically, RDF was first standardized in 1999, with RDF Schema (RDFS) following shortly after to add basic vocabulary for classes, properties, and hierarchies. RDF itself is not an ontology language but rather a flexible framework for describing resources identified by URIs (Uniform Resource Identifiers). By adopting a universal addressing scheme, RDF enables statements about anything, people, places, concepts, or digital resources, creating a decentralized but interoperable web of data.

At its core, RDF represents information through triples. A triple consists of:

* **Subject**: the resource being described
* **Predicate**: the property or relationship linking the subject to the object
* **Object**: the value of the property, which can be either another resource or a literal (string, number, date)

For example, the statement “Alice knows Bob” can be represented in Turtle syntax as follows:

@prefix ex: <http://example.org#> .

ex:Alice ex:knows ex:Bob .

Here, the subject is ex:Alice, the predicate is ex:knows, and the object is ex:Bob. RDF supports the use of literals as objects, allowing attributes such as names or ages to be expressed:

ex:Alice ex:age "35"ˆˆxsd:integer .

ex:Alice ex:name "Alice Smith"@en .

The first triple assigns the integer value 35 as Alice’s age, while the second associates a literal string with a language tag (@en).

RDF can also be serialized in other syntaxes, such as RDF/XML. The same example in RDF/XML would be written as follows:

<rdf:RDF xmlns:ex="http://example.org#"

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

<rdf:Description rdf:about="http://example.org#Alice">

<ex:knows rdf:resource="http://example.org#Bob"/>

<ex:age rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">35</ex:age>

<ex:name xml:lang="en">Alice Smith</ex:name>

</rdf:Description>

</rdf:RDF>

Although verbose, RDF/XML ensures compatibility with XML-based infrastructures and remains widely used in some domains. Turtle, however, is often preferred for its human readability.

RDF is frequently visualized as a graph, where nodes represent subjects and objects, and edges represent predicates. Figure [6.2](#Fig2) illustrates this model for the triples above.

![Diagram illustrating a simple RDF graph. It shows two nodes, “ex:Alice” and “ex:Bob,” connected by an arrow labeled “ex:knows,” indicating a relationship. “ex:Alice” has two additional arrows: one labeled “ex:age” pointing to a node with the value “35” typed as an integer, and another labeled “ex:name” pointing to a node with the value “Alice Smith” in English.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig2_HTML.png)

Fig. 6.2

Graph representation of RDF triples describing Alice

Beyond simple triples, RDF Schema (RDFS) extends RDF with mechanisms for defining vocabularies and classes. It allows users to declare classes and properties, specify subclass and subproperty hierarchies, and define domains and ranges. For instance:

ex:Person rdf:type rdfs:Class .

ex:knows rdf:type rdf:Property ;

rdfs:domain ex:Person ;

rdfs:range  ex:Person .

This fragment declares Person as a class and knows as a property relating one person to another. These declarations allow inference: If ex:Alice ex:knows ex:Bob, then a reasoner can infer that both Alice and Bob are instances of Person.

RDF forms the foundation upon which more expressive languages such as OWL are built. While RDF and RDFS provide basic schema and graph structures, OWL introduces logical axioms and reasoning capabilities. Together, they establish the Semantic Web stack, where RDF supplies the data model, RDFS offers lightweight schema definitions, and OWL delivers formal semantics for ontology modeling.

In summary, RDF is the cornerstone of the Semantic Web, providing a universal framework for representing information in a graph-based structure. Its simplicity, extensibility, and interoperability allow data to be shared, integrated, and reasoned about across diverse domains, forming the essential substrate for higher level semantic technologies.

#### 6.1.3.2 The Web Ontology Language (OWL)

The OWL is a knowledge representation language developed under the auspices of the World Wide Web Consortium (W3C) to support the construction of ontologies on the Semantic Web. Its purpose is to provide a standard and formally grounded way to describe classes of entities, their relationships, and logical constraints, enabling not only the exchange of data but also the reasoning over such data. OWL builds upon the Resource Description Framework (RDF) and the RDF Schema (RDFS), inheriting their graph-based data model and extending it with constructs derived from Description Logics, which enable the capture of rich semantics and allow machines to infer new knowledge automatically.

Historically, OWL was standardized in 2004 as part of the Semantic Web initiative, following earlier ontology languages such as DAML+OIL. In 2009, the W3C released OWL 2, which provided improved expressiveness, profiles tailored to different computational needs, and compatibility with modern reasoning engines. Unlike RDF and RDFS, which are primarily oriented toward data modeling and lightweight schema definitions, OWL introduces constructs to define class equivalence, disjointness, property characteristics (e.g., transitive, functional, and inverse), cardinality restrictions, and logical axioms, thereby providing a level of formalization suitable for complex domains.

In practice, OWL can be serialized in several syntaxes, including RDF/XML, Turtle, Functional Syntax, and the Manchester Syntax. Turtle is remarkably concise for RDF-based representations, whereas Manchester Syntax is more readable for human users when writing axioms. The following examples illustrate the incremental construction of an ontology fragment using OWL.

First, consider the declaration of classes and hierarchies using Turtle syntax:

@prefix ex: <http://example.org#> .

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix owl: <http://www.w3.org/2002/07/owl#> .

ex:Human rdf:type owl:Class .

ex:Mammal rdf:type owl:Class .

ex:Animal rdf:type owl:Class .

ex:Human rdfs:subClassOf ex:Mammal .

ex:Mammal rdfs:subClassOf ex:Animal .

In this fragment, three classes are declared (Human, Mammal, and Animal), and subclass relations are established, expressing that every human is a mammal and every mammal is an animal. Such hierarchical modeling is fundamental for reasoning, since it allows knowledge to be inherited from more general to more specific classes.

OWL also allows for the definition of properties, their domains, and their ranges. For instance, the following triple set defines a property hasParent that links humans to other humans:

ex:hasParent rdf:type owl:ObjectProperty ;

rdfs:domain ex:Human ;

rdfs:range  ex:Human .

In addition to such structural assertions, OWL enables the specification of logical restrictions on classes. In Manchester Syntax, these can be expressed more compactly. Consider the following examples:

Class: Parent

EquivalentTo: Human and (hasChild some Human)

Class: OnlyChild

EquivalentTo: Human and (hasSibling max 0 Human)

ObjectProperty: hasSibling

Characteristics: Symmetric

Here, the class Parent is defined as any human who has at least one child, while the class OnlyChild is defined as a human with no siblings. Moreover, the property hasSibling is declared as symmetric, meaning that if Alice is a sibling of Bob, then Bob is also a sibling of Alice. These examples demonstrate how OWL facilitates the explicit representation of domain knowledge in a manner that enables reasoning engines to process it.

Another important feature of OWL is the ability to assert disjointness and equivalence. For example:

Class: Male

DisjointWith: Female

Class: Woman

EquivalentTo: Human and Female

This states that no individual can be both a Male and a Female and that Woman is simply a convenient shorthand for any individual who is both a human and a female. Such axioms are not just definitions for documentation; they carry logical meaning that allows reasoners to detect inconsistencies or to derive new facts.

OWL comes in different *profiles*, each balancing expressivity and computational complexity. Table [6.3](#Tab3) summarizes the most relevant profiles from OWL 1 and OWL 2.

Table 6.3

Main OWL profiles and their characteristics

| Profile (version) | Description | Typical use case |
| --- | --- | --- |
| OWL Lite (OWL 1) | Simplified subset of OWL, supporting classification hierarchies and simple constraints | Basic taxonomies and lightweight applications |
| OWL DL (OWL 1) | Based on Description Logics, ensures decidability and completeness for reasoning | Applications requiring logical rigor and automated classification |
| OWL Full (OWL 1) | Maximum expressivity with full RDF compatibility, but reasoning is undecidable | Experimental or highly flexible modeling, often without guarantees of reasoning |
| OWL 2 EL (OWL 2) | Optimized for ontologies with large numbers of classes and properties, supports polynomial-time reasoning | Biomedical ontologies such as SNOMED CT |
| OWL 2 QL (OWL 2) | Designed for efficient query answering by rewriting OWL axioms into SQL | Ontology-based data access over large relational databases |
| OWL 2 RL (OWL 2) | Rule-based profile, suitable for scalable reasoning using production rules | Applications requiring tractable rule-based inference |

The reasoning capabilities of OWL are central to its value. Suppose we assert that:

ex:Alice rdf:type ex:Human .

ex:Human rdfs:subClassOf ex:Mammal .

ex:Mammal rdfs:subClassOf ex:Animal .

A reasoning engine will automatically infer that ex:Alice is a mammal and also an animal, even though these statements were never explicitly asserted. Suppose we further state that every mammal must have at least one parent who is also a mammal. In that case, the reasoner may also detect whether the ontology is incomplete or inconsistent when no parent is provided for Alice.

To complement these examples, Fig. [6.3](#Fig3) illustrates a simple class hierarchy modeled in OWL, showing how humans are related to mammals and animals, and how specific concepts such as Parent and OnlyChild extend the notion of human beings.

![Flow chart illustrating a hierarchy: “Animal” at the top, leading to “Mammal,” then “Human.” Below “Human,” two branches lead to “Parent” and “OnlyChild.” Each term is enclosed in an oval shape, connected by lines indicating the relationship.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig3_HTML.png)

Fig. 6.3

Class hierarchy in OWL: from Animal to Mammal, Human, and its specializations Parent and OnlyChild

Therefore, OWL represents a cornerstone of the Semantic Web stack. It provides a formally grounded, expressive, and machine-interpretable language for describing ontologies. By combining human-readable syntaxes with automated reasoning, OWL facilitates interoperability, knowledge integration, and intelligent applications across diverse domains, including e-commerce, bioinformatics, and cultural heritage. Its layered construction on top of RDF ensures compatibility with existing web standards, while its logical foundations guarantee that knowledge encoded in OWL can be subjected to rigorous computational analysis.

## 6.2 The Role of Ontologies in Digital Forensics

Applied across diverse fields, including Digital Forensics, ontologies provide a formal framework for representing digital evidence, thereby facilitating its analysis, documentation, and interoperability among forensic tools. In the forensic context, ontologies are essential for making investigations more systematic and efficient in the handling of evidence. The following sections highlight their primary functions and applications in this domain [[10](#CR10)].

Structured Representation of Knowledge

A key contribution of ontologies in Digital Forensics is the formal organization of data [[10](#CR10)]. By defining classes, subclasses, objects, and individuals, ontologies establish a hierarchical system that enables efficient classification of digital evidence. This structured approach strengthens the relationship between experiments and evidence, while also facilitating the formalization of entities and events, resulting in more precise and reliable documentation.

Organization and Standardization of Forensic Documentation

Accurate documentation is vital for the credibility of forensic investigations. Ontologies support this process by enabling the creation of cohesive, clear, and standardized reports. They contribute to harmonizing the presentation of evidence, ensuring clarity in legal contexts, and promoting the objective and consistent analysis of information [[10](#CR10)].

Sequential Mapping of Events

Reconstructing cyber incidents requires organizing events in a chronological sequence. Ontologies help experts identify the sequence of suspicious actions, correlate files, logs, and users and detect anomalous patterns that may indicate fraud or tampering. This structured mapping improves case comprehension and helps uncover irregularities throughout the investigation [[20](#CR20)].

Interoperability Between Forensic Tools

The use of heterogeneous forensic software often poses challenges due to incompatible data formats and standards. Ontologies mitigate these issues by establishing a unified knowledge base and standardizing terminology and classifications across tools such as EnCase, Autopsy, and FTK. This integration improves the consistency and accuracy of evidence analysis [[2](#CR2)].

Digital Evidence Classification and Analysis

Ontologies facilitate the mapping and classification of information, organizing evidence according to its relevance to the investigation. They allow for the association of data with predefined categories and the structured recording of suspicious activities. This systematic approach enhances the efficiency of investigative processes and ensures that evidence remains accessible and properly contextualized [[22](#CR22)].

Pattern and Anomaly Identification

Handling large volumes of data is one of the main challenges in Digital Forensics, especially in contexts involving the Internet of Things (IoT) and Machine Learning. Ontologies enable advanced queries to detect suspicious patterns, identify inconsistencies and anomalies, and define metrics to monitor deviations in access logs, network traffic, or file modifications [[4](#CR4)].

Recovery and Correlation of Lost Information

Intentional or accidental data loss is a recurring issue in forensic investigations, where adversaries may intentionally or unintentionally delete or manipulate records to conceal their tracks. Ontologies support advanced queries that help recover fragmented records, reconstruct corrupted data, and infer hidden connections among pieces of evidence, thereby expanding investigators’ understanding of a case [[11](#CR11)].

Network Analysis and Communication Flow

Investigating digital incidents often requires analyzing networks and identifying communication patterns among suspicious devices. Ontologies support this process by structuring network data and enabling the tracking of connections, which helps reveal entry points for cyberattacks. Additionally, correlating logs from firewalls, routers, and servers provides a comprehensive view of network activity under investigation [[16](#CR16)].

Therefore, ontologies transform Digital Forensics by providing an organized and standardized framework for evidence analysis. They enhance the accuracy, efficiency, and reliability of investigations, making them an indispensable tool in modern forensic practice.

## 6.3 Introduction to SPARQL

SPARQL Protocol and RDF Query Language (SPARQL) is the W3C-recommended standard for querying and manipulating data represented in the Resource Description Framework (RDF) model.

RDF[1](#Fn1) encodes information as a directed labeled graph, where each piece of knowledge is described as a triple consisting of a subject, predicate, and object.

SPARQL is designed to identify and transform patterns in such graphs, making it the cornerstone of the Semantic Web and Linked Data movement. Since its first recommendation in 2008 and its extended version in 2013 (SPARQL 1.1), the language has evolved into a mature and expressive framework for querying interconnected data across distributed systems [[9](#CR9), [14](#CR14), [15](#CR15)].

### 6.3.1 Historical Motivation

The development of SPARQL must be understood in the broader context of the Semantic Web. During the early 2000s, the World Wide Web was already rich in hyperlinked documents but lacked a standard way of expressing structured, machine-interpretable data. Traditional relational databases provided powerful mechanisms for structured storage and querying, but they required fixed schemas and lacked native support for integrating heterogeneous or distributed data.

The introduction of RDF provided a flexible, graph-based model in which data could be incrementally enriched and linked across domains. However, RDF alone did not specify how users and applications could query such data. The need for a standardized query language that would allow developers, researchers, and organizations to leverage RDF datasets led to the creation of SPARQL. Its design was influenced by both theoretical considerations (expressiveness and formal semantics) and practical needs (usability, web orientation, and interoperability).

Compared to SQL, which had been the standard for decades, SPARQL was intentionally crafted to support graph-oriented querying, providing a syntax that is declarative but distinct in semantics. This historical trajectory established SPARQL as the backbone of Linked Open Data and an essential tool for data integration across the Web [[3](#CR3)].

The study of SPARQL has been enriched by formal research into its semantics and complexity. Pérez et al. [[14](#CR14)] demonstrated that core SPARQL corresponds to conjunctive queries, while extensions such as OPTIONAL and UNION increase expressive power at the cost of computational complexity.

SPARQL has found widespread adoption across multiple domains:

* **Linked open data**: Datasets such as DBpedia, Wikidata, and Europeana expose SPARQL end points for exploring billions of triples.
* **Bioinformatics**: SPARQL integrates genetic and medical data, e.g., Bio2RDF.
* **Digital libraries**: semantic search over metadata in repositories
* **Governmental open data**: RDF-based datasets with SPARQL end points
* **Industry**: enterprise knowledge graphs for search, recommendations, and decision support

This organization ensures that the chapter flows logically from motivation, through concepts and hands-on syntax, to formal and applied aspects of SPARQL.

### 6.3.2 Core Characteristics of RDF and SPARQL

At its core, RDF is a graph data model where each fact is expressed as a triple (s,p,o). The subject *s* is usually a URI that identifies a resource, the predicate *p* is a URI that denotes a property or relationship, and the object *o* can be either another URI or a literal value such as a string or a number. This model allows knowledge to be expressed in a decentralized and extensible manner.

SPARQL builds on this model by allowing users to specify patterns of triples to search for within an RDF dataset. For example, one can query for all resources of type “Person” and retrieve their names, regardless of how the data is distributed across multiple datasets. The graph-oriented nature of SPARQL enables queries that naturally traverse relationships, making it well suited for data integration scenarios.

Key characteristics of SPARQL include:

* **Graph pattern matching**: Queries are expressed as patterns of triples with variables, which are matched against the dataset.
* **Declarative syntax**: inspired by SQL but adapted to RDF graphs, making it relatively accessible for users familiar with relational queries
* **Flexible schema handling**: SPARQL queries do not require fixed schemas, allowing queries to be performed on evolving or incomplete data.
* **Support for reasoning**: Although SPARQL itself is not a reasoning engine, it can be combined with ontologies expressed in OWL and RDFS to support inference.

These features make SPARQL a versatile language that bridges the gap between heterogeneous data sources and structured knowledge discovery.

### 6.3.3 SPARQL Syntax

Building on the previous concepts, SPARQL offers a structured and declarative approach to querying RDF data. While its surface syntax resembles SQL, the underlying semantics are graph-oriented. A SPARQL query typically consists of three main components: *prefix declarations*, a *query form*, and a *query pattern*. Optional clauses such as filters, aggregations, and ordering refine the query.

Prefix Declarations

Since RDF resources are identified using URIs, queries would be verbose if written with full URIs. To improve readability, SPARQL allows the use of prefixes. For example:

PREFIX foaf: <http://xmlns.com/foaf/0.1/>

PREFIX dc:   <http://purl.org/dc/elements/1.1/>

These declarations allow shorthand notation, such as foaf:name, in place of the complete URI.

Basic Triple Patterns

The fundamental building block of SPARQL queries is the *triple pattern*. Variables are denoted with a question mark prefix. For example, retrieving all book titles:

PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?title

WHERE {

?book dc:title ?title .

}

This query finds all triples where a resource (?book) has a dc:title predicate, binding the title to the variable ?title.

Filtering Results

The FILTER clause restricts solutions based on conditions. Suppose we only want books published after 2015:

PREFIX dc: <http://purl.org/dc/elements/1.1/>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?title ?date

WHERE {

?book dc:title ?title ;

dc:date ?date .

FILTER (xsd:gYear(?date) > "2015"ˆˆxsd:gYear)

}

Optional Information

Sometimes, additional information is not guaranteed to exist. In such cases, the OPTIONAL clause is useful:

PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name ?email

WHERE {

?person foaf:name ?name .

OPTIONAL { ?person foaf:mbox ?email . }

}

Combining Patterns with UNION

SPARQL allows queries that return results satisfying one of several patterns. The UNION operator combines alternative graph patterns:

PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?person ?info

WHERE {

{ ?person foaf:mbox ?info . }

UNION

{ ?person foaf:homepage ?info . }

}

Aggregations and Grouping

SPARQL 1.1 introduced aggregates similar to SQL. For example, to count the number of books per author:

PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?author (COUNT(?book) AS ?numBooks)

WHERE {

?book dc:creator ?author .

}

GROUP BY ?author

Constructing New Graphs

SPARQL can also generate new RDF graphs with the CONSTRUCT form. For example:

PREFIX dc: <http://purl.org/dc/elements/1.1/>

PREFIX foaf: <http://xmlns.com/foaf/0.1/>

CONSTRUCT {

?author foaf:made ?book .

}

WHERE {

?book dc:creator ?author .

}

Federated Queries

SPARQL enables queries across distributed datasets through the SERVICE clause. For instance:

PREFIX dbpedia: <http://dbpedia.org/ontology/>

SELECT ?author ?birthPlace

WHERE {

SERVICE <http://dbpedia.org/sparql> {

?author dbpedia:birthPlace ?birthPlace .

}

}

### 6.3.4 Tools for Writing and Executing SPARQL Queries

Effectively working with SPARQL requires the proper set of tools to write, test, and execute queries against RDF datasets. These tools range from web-based end points for quick experimentation to integrated development environments (IDEs) and programming libraries for large-scale or automated workflows. This subsection provides a detailed guide to commonly used SPARQL tools, along with practical advice on selecting the appropriate tool based on your specific needs. Ultimately, it demonstrates how to utilize Protégé to write and execute SPARQL queries.

#### 6.3.4.1 Web-Based SPARQL End Points

Web-based SPARQL end points allow users to execute queries directly in a browser, often against large, publicly available datasets. They are ideal for beginners, quick experimentation, or exploratory research.

* **DBpedia SPARQL End Point:**[2](#Fn2) DBpedia extracts structured data from Wikipedia and exposes it as RDF. Its SPARQL end point provides a web interface where users can input queries, explore datasets, and view results in multiple formats (XML, JSON, and CSV). Example queries are included to help beginners learn SPARQL. This tool is excellent for learning, experimentation, and quick access to a rich knowledge graph.
* **Wikidata Query Service:**[3](#Fn3) Wikidata is a collaborative knowledge base with structured data about entities such as people, places, and events. Its SPARQL interface includes syntax highlighting, autocompletion, and result visualizations such as graphs, maps, and timelines. This end point is particularly suitable for complex exploratory analysis and visualizing relationships in the data.
* **Europeana SPARQL End Point:**[4](#Fn4) Europeana provides metadata for millions of cultural heritage objects. Its SPARQL end point allows users to query this rich dataset, making it suitable for research in the humanities or cultural domains. While its scope is more focused than DBpedia or Wikidata, it provides real-world, high-quality datasets for testing SPARQL queries.

#### 6.3.4.2 Desktop and IDE Tools

For local datasets, custom ontologies, or advanced query development, desktop tools and IDEs provide enhanced features such as reasoning, data management, and debugging support.

* **Apache Jena Fuseki:**[5](#Fn5) Fuseki is a SPARQL server that can host RDF datasets locally or on a network. It offers a web interface for executing queries, supports SPARQL Update for modifying data, and integrates seamlessly with Jena’s Java libraries. This tool is ideal for developers or researchers who need to manage local datasets and execute complex queries efficiently.
* **Protégé with SPARQL Plugin:**[6](#Fn6) Protégé is a widely used ontology editor supporting RDF and OWL. The SPARQL plugin allows users to query ontologies directly, including reasoning-enabled queries. This setup is beneficial for ontology-driven research, semantic modeling, and learning SPARQL in the context of structured knowledge bases.
* **TopBraid Composer:**[7](#Fn7) TopBraid Composer is a professional, commercial RDF/OWL IDE. It provides advanced SPARQL editing, validation, reasoning support, and integration with enterprise knowledge graphs. This tool is suitable for large-scale industrial applications that require complex ontologies and SPARQL queries, although it has a steeper learning curve and higher licensing costs.

#### 6.3.4.3 Command-Line and Library Support

Programmatic access is essential for automation, integration with applications, or data analysis pipelines. These tools allow SPARQL queries to be executed from scripts or code.

* **Apache Jena ARQ:** A Java library and command-line utility for executing SPARQL queries. ARQ supports all SPARQL 1.1 features, including property paths, aggregates, subqueries, and federated queries. It is suitable for automated workflows, large-scale data processing, and integration into Java-based applications.
* **RDFLib (Python):**[8](#Fn8) RDFLib is a Python library for processing RDF datasets, including SPARQL query execution. It integrates well with Python data analysis tools like Pandas and is convenient for scripting, research projects, and prototyping. Performance is suitable for moderate-sized datasets.
* **SPARQLWrapper (Python):**[9](#Fn9) SPARQLWrapper provides a Python interface to remote SPARQL end points. It simplifies sending queries, retrieving results in JSON, XML, or CSV formats, and handling errors. It is ideal for lightweight scripts and automation tasks that interact with online SPARQL services.

#### 6.3.4.4 Using Protégé to Write and Run SPARQL Queries

By installing the SPARQL plugin, Protégé users can write, execute, and analyze SPARQL queries directly on loaded ontologies. This subsection provides a practical guide for using Protégé as a SPARQL development environment.

By following these steps, users can utilize Protégé as a comprehensive environment for writing, testing, and executing SPARQL queries, thereby combining ontology editing with semantic querying capabilities.

##### **Step 1: Installing Protégé and the SPARQL Plugin**

1. 1.

   Download and install Protégé[10](#Fn10) according to the operating system.
2. 2.

   Launch Protégé and open an existing ontology (RDF/OWL) or create a new one.
3. 3.

   (Attention: Before performing this step, check whether the plugin is already installed.) Install the SPARQL query plugin: Navigate to File >Check for Plugins, search for SPARQL Query, and click Install.
4. 4.

   Restart Protégé to activate the plugin (Fig. [6.4](#Fig4)).

   ![A screenshot of a software interface displaying a menu under the “Window” tab. The menu includes options like “Views,” “Tabs,” “Create new tab,” and “Import tab.” The “Views” submenu is expanded, showing options such as “Annotation property views,” “Class views,” and “Query views.” The “Query views” submenu is further expanded, listing “DL query,” “Existential Query,” and “SPARQL query.” The URL at the top indicates a semantic web ontology.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig4_HTML.png)

   Fig. 6.4

   SPARQL query plugin

##### **Step 2: Loading an Ontology**

1. 1.

   In Protégé, go to File >Open, and select your ontology file (RDF/XML, Turtle, or OWL format).
2. 2.

   Verify that the ontology is loaded correctly by exploring the classes, properties, and individuals in the main interface.

##### **Step 3: Opening the SPARQL Query Tab**

1. 1.

   Go to Window >Tabs >SPARQL Query to open the SPARQL query editor.
2. 2.

   The editor provides a text area for entering queries and buttons to execute them.
3. 3.

   Optional features include syntax highlighting, autocompletion for class and property names, and templates for common query patterns (Figs. [6.5](#Fig5) and [6.6](#Fig6)).

   ![Screenshot of an ontology editor interface showing a class hierarchy. The active ontology is titled “untitled-ontology-69” with a URL link at the top. The main class displayed is “owl:Thing,” with subclasses including AnalysisInterpretation, Dissemination, Operation, Planning, and Pre-Operation. The interface includes tabs for Entities, Annotation properties, Datatypes, and Individuals, with options for viewing and editing annotations.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig5_HTML.png)

   Fig. 6.5

   Classes in the main interface

   ![Screenshot of a SPARQL query interface in an ontology editor. The query window displays a SPARQL query with prefixes for RDF, OWL, RDFS, and XSD namespaces. The query selects subjects and objects where the subject is a subclass of the object. The interface includes menu options like File, Edit, View, and others, with tabs for different query types. An “Execute” button is visible at the bottom.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig6_HTML.png)

   Fig. 6.6

   SPARQL query

##### **Step 4: Writing a SPARQL Query**

* Define prefixes for readability. For example:

  PREFIX foaf: <http://xmlns.com/foaf/0.1/>

  PREFIX ex:   <http://example.org/>
* Write a basic query to retrieve all individuals of type ex:Person:

  SELECT ?person ?name

  WHERE {

  ?person a ex:Person ;

  foaf:name ?name .

  }
* Use optional patterns to include additional information if available:

  OPTIONAL { ?person foaf:mbox ?email . }
* Filters can refine results. For example, to select persons whose name starts with ”A”:

  FILTER (STRSTARTS(?name, "A"))

##### **Step 5: Executing the Query and Viewing Results**

1. 1.

   Click the Execute button in the SPARQL tab.
2. 2.

   Protégé displays results in a tabular form, showing variable bindings for each match.
3. 3.

   Results can be exported to CSV, XML, or other supported formats for further analysis.
4. 4.

   If a query fails, the editor highlights syntax errors and provides hints for correction (Fig. [6.7](#Fig7)).

   ![A screenshot of a software interface displaying a SPARQL query editor. The query includes several PREFIX declarations and a SELECT statement. Below the query editor, a table lists subjects and objects, such as “CentralTendencyA” paired with “AnaliseUnivariada” and “Experiment” with “OperationProcedure.” The interface includes menu options like File, Edit, View, and others, with an “Execute” button at the bottom. The window title indicates the file path and ontology being used.](../images/624027_1_En_6_Chapter/624027_1_En_6_Fig7_HTML.png)

   Fig. 6.7

   Execute button

## 6.4 Final Remarks

This chapter provided an integrated exploration of the theoretical, structural, and practical dimensions of ontologies, connecting their philosophical origins to their computational applications and, ultimately, to their relevance in Digital Forensics. Beginning with classical philosophical inquiries into the nature of being and reality, the discussion demonstrated how foundational ideas by Aristotle and other early thinkers evolved into formal structures capable of representing complex domains of knowledge. These philosophical insights provided the conceptual underpinnings for ontology as a scientific and engineering discipline, one that now enables interoperability, semantic reasoning, and machine understanding.

By reviewing core definitions, typologies, and construction methodologies, this chapter highlighted how ontologies move beyond abstract theory to serve as operational instruments in modern computing. From generic and domain ontologies to task- and application-specific models, the taxonomy presented in Table [6.1](#Tab1) illustrated the flexibility of ontological design to accommodate diverse purposes, degrees of formality, and levels of granularity. These distinctions are crucial to ensure that ontologies are not only logically sound but also contextually useful for decision-making, data integration, and the development of intelligent systems.

The chapter also examined how ontology engineering draws from both logic and computer science. Standards such as the Resource Description Framework (RDF) and the Web Ontology Language (OWL) formalize ontological constructs through machine-interpretable semantics, thereby enabling the automated processing of knowledge. RDF’s graph-based data model offers a universal syntax for structuring information in triples, whereas OWL introduces the expressivity required to describe complex relationships, logical axioms, and constraints. Together, these technologies underpin the Semantic Web, an ecosystem where data is not merely published but semantically linked, allowing for advanced reasoning and knowledge discovery across distributed environments.

Building upon these foundations, SPARQL emerged as a powerful query language for navigating and manipulating RDF-based data. Through its declarative graph-pattern syntax, SPARQL enables users to identify, filter, and transform data across heterogeneous systems. The chapter’s overview of SPARQL syntax, features, and tools demonstrated how it serves as both a practical querying mechanism and a research instrument for data-driven disciplines. Web-based end points such as DBpedia and Wikidata, as well as integrated environments like Protégé and Apache Jena, exemplify how SPARQL empowers both novice learners and expert practitioners to experiment with and operationalize semantic technologies.

The discussion of Digital Forensics illustrated a concrete domain where ontologies play a transformative role. By structuring digital evidence, standardizing terminology, and supporting the correlation of events, ontologies enhance the rigor, transparency, and reproducibility of forensic investigations. They bridge the gap between raw technical artifacts and higher level conceptual reasoning, thereby strengthening the evidential value of digital traces. Moreover, ontologies promote interoperability among forensic tools, improve documentation consistency, and enable advanced analyses such as anomaly detection, evidence recovery, and network behavior reconstruction.

This integration of ontology engineering and Digital Forensics research aligns with broader movements toward Open Science. Formalized representations, shared vocabularies, and reproducible querying mechanisms, enabled by RDF, OWL, and SPARQL, facilitate transparency and collaborative validation. The capacity to model, query, and share knowledge in standardized formats not only improves scientific accountability but also supports the ethical and societal dimensions of forensic practice. As a result, ontologies are not just technical artifacts but epistemic frameworks that promote trust, interpretability, and collective progress.

Looking forward, the convergence of ontological reasoning, artificial intelligence, and big data analytics opens new avenues for automation and intelligent decision support. Emerging paradigms such as knowledge graphs, digital twins, and explainable AI increasingly rely on ontological foundations to ensure semantic coherence and traceability. Within Digital Forensics, these technologies promise more adaptive, interpretable, and auditable analytical environments, where reasoning engines can contextualize evidence dynamically and detect patterns that would otherwise remain hidden.

In summary, ontologies provide a unifying framework that connects philosophical reflection, logical precision, and computational pragmatism. When combined with standards such as RDF, OWL, and SPARQL, they offer the methodological and technological infrastructure required for a truly semantic understanding of data and processes. Their application to Digital Forensics demonstrates the power of conceptual modeling to not only structure and retrieve information but also sustain the integrity and reproducibility of scientific inquiry. Ultimately, the ongoing evolution of ontological approaches represents a cornerstone of the Semantic Web and a critical enabler for open, transparent, and intelligent science.

## References

1. 1.

   Almeida, M.B., Bax, M.P.: Uma visão geral sobre ontologias: pesquisa sobre definições, tipos, aplicações, métodos de avaliação e de construção. Ciência da Informação **32**(3), 7–20 (2003) (In Portuguese)<https://doi.org/10.1590/S0100-19652003000300002>
2. 2.

   Alzaabi, M., Jones, A., Martin, T.A.: An ontology-based forensic analysis tool. In: 2013 International Conference on Digital Forensics (2013)
3. 3.

   Angles, R., Gutierrez, C.: Querying semantic web data with SPARQL. In: Proceedings of the 30th ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems (PODS), pp. 305–316. ACM (2011). [https://​doi.​org/​10.​1145/​1989284.​1989312](https://doi.org/10.1145/1989284.1989312)
4. 4.

   Baumeister, J., Seipel, D.: Anomalies in ontologies with rules. J. Web Semant. **8**(1), 55–68 (2010)<https://doi.org/10.1016/j.websem.2009.12.003>
5. 5.

   Biagetti, M.T.: Ontologies as knowledge organization systems. Knowl. Organiz. **48**(2), 152–176 (2021)<https://doi.org/10.5771/0943-7444-2021-2-152>
6. 6.

   Borst, W.N.: Construction of engineering ontologies. Ph.D. Thesis, University of Twente, Enschede (1997)
7. 7.

   Brenner, J.E., Igamberdiev, A.U.: Philosophy in Reality: A New Book of Changes. Springer, Berlin (2021)<https://doi.org/10.1007/978-3-030-62757-7>
8. 8.

   Genesereth, M.R., Nilsson, N.J.: Logical Foundations of Artificial Intelligence. Morgan Kaufmann, San Francisco (2012)
9. 9.

   Harris, S., Seaborne, A.: SPARQL 1.1 Query Language. W3C Recommendation (2013). [https://​www.​w3.​org/​TR/​sparql11-query/​](https://www.w3.org/TR/sparql11-query/)
10. 10.

    Karie, N.M., Venter, H.S.: Toward a general ontology for digital forensic disciplines. J. Forensic Sci. **59**(5), 1231–1241 (2014)<https://doi.org/10.1111/1556-4029.12511>
11. 11.

    Khattak, A.M., Latif, K., Khan, S., Ahmed, N.: Ontology recovery and visualization. In: 2008 4th International Conference on Next Generation Web Services Practices, pp. 90–96. IEEE (2008)
12. 12.

    Nirenburg, S., Raskin, V.: Ontological Semantics. MIT Press, Cambridge (2004)
13. 13.

    Noy, N.F., McGuinness, D.L.: Ontology Development 101: A Guide to Creating Your First Ontology. Stanford Knowledge Systems Laboratory Technical Report (2001)
14. 14.

    Pérez, J., Arenas, M., Gutierrez, C.: Semantics and complexity of SPARQL. ACM Trans. Database Syst. **34**(3), 1–45 (2009). [https://​doi.​org/​10.​1145/​1567274.​1567278](https://doi.org/10.1145/1567274.1567278)<https://doi.org/10.1145/1567274.1567278>
15. 15.

    Prud’hommeaux, E., Seaborne, A.: SPARQL Query Language for RDF. W3C Recommendation (2008). [https://​www.​w3.​org/​TR/​rdf-sparql-query/​](https://www.w3.org/TR/rdf-sparql-query/)
16. 16.

    Sabou, M., Fernandez, M.: Ontology (network) evaluation. In: Ontology Engineering in a Networked World, pp. 193–212. Springer, Berlin (2011)
17. 17.

    Smith, B.: Blackwell Guide to the Philosophy of Computing and Information. Wiley-Blackwell, Oxford (2003)
18. 18.

    Smith, B.: Ontology. The Monist **94**(3), 267–293 (2012)
19. 19.

    Smith, B., Welty, C.: Ontology: Towards a new synthesis. In: Formal Ontology in Information Systems, pp. 3–9. ACM Press, New York (2001)
20. 20.

    Spyropoulos, A.Z., Bratsas, C., Makris, G.C., Garoufallou, E., Tsiantos, V.: Interoperability-enhanced knowledge management in law enforcement: an integrated data-driven forensic ontological approach to crime scene analysis. Information **14**(11), 607 (2023)<https://doi.org/10.3390/info14110607>
21. 21.

    Verelst, K., Coecke, B.: Early Greek thought and perspectives for the interpretation of quantum mechanics: Preliminaries to an ontological approach. In: Metadebates on Science: The Blue Book of “Einstein Meets Magritte”, pp. 163–196. Springer, Dordrecht (1999)
22. 22.

    Weng, S.S., Tsai, H.J., Liu, S.C., Hsu, C.H.: Ontology construction for information classification. Expert Syst. Appl. **31**(1), 1–12 (2006)<https://doi.org/10.1016/j.eswa.2005.09.007>
23. 23.

    Wolff, C., Ecole, J.: Philosophia prima sive ontologia. Les Etudes Philosophiques **17**, 292–292 (1962)

Footnotes

[1](#Fn1_source)

[https://​www.​w3.​org/​RDF](https://www.w3.org/RDF)

[2](#Fn2_source)

[http://​dbpedia.​org/​sparql](http://dbpedia.org/sparql)

[3](#Fn3_source)

[https://​query.​wikidata.​org/​](https://query.wikidata.org/)

[4](#Fn4_source)

[https://​sparql.​europeana.​eu/​](https://sparql.europeana.eu/)

[5](#Fn5_source)

[https://​jena.​apache.​org/​documentation/​fuseki2/​](https://jena.apache.org/documentation/fuseki2/)

[6](#Fn6_source)

[https://​Protege.​stanford.​edu/​](https://Protege.stanford.edu/)

[7](#Fn7_source)

[https://​www.​topquadrant.​com/​tools/​ide-topbraid-composer/​](https://www.topquadrant.com/tools/ide-topbraid-composer/)

[8](#Fn8_source)

[https://​rdflib.​readthedocs.​io/​](https://rdflib.readthedocs.io/)

[9](#Fn9_source)

[https://​rdflib.​github.​io/​sparqlwrapper/​](https://rdflib.github.io/sparqlwrapper/)

[10](#Fn10_source)

[https://​Protege.​stanford.​edu/​](https://Protege.stanford.edu/)

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_7>

# 7. The ExperDF-Onto Ontology

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter introduces ExperDF-Onto, a domain ontology that formalizes the ExperDF-CM conceptual model into an executable knowledge representation for structuring, documenting, and operationalizing controlled experimentation in Digital Forensics. Developed in OWL and engineered in Protégé following the SABiO methodology, the ontology encompasses more than 600 classes, properties, relations, and axioms, organizing the full experimental life cycle into five phases: Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination. ExperDF-Onto extends the conceptual model by refining experimental elements, including hypotheses, variables, procedures, statistical methods, threats to validity, scenario configuration, chain-of-custody documentation, and dissemination artifacts. Its design promotes interoperability, reuse, traceability, and transparency while enabling the automatic generation of UML views to support communication with diverse forensic and scientific audiences. A proof-of-concept instantiation demonstrates feasibility and highlights how the ontology can structure data, support methodological rigor, and improve reproducibility in forensic experimentation. The chapter also details SPARQL query patterns that allow users to navigate class hierarchies and audit knowledge structures, enabling both conceptual inspection and computational validation. By integrating provenance principles from Dublin Core and PROV-inspired elements, ExperDF-Onto provides a foundation for reproducible, analyzable, and evidence-driven digital forensic research and practice, strengthening experimental reliability and contributing to the formalization of the field.

## 7.1 The ExperDF-Onto Ontology

ExperDF-Onto represents a significant advance toward formalization and experimentation of DF, building upon the ExperDF-CM conceptual model [[3](#CR3)].

The ExperDF-Onto ontology is coded using both OWL and RDF schemas, presented in Sect. [7.2](#Sec9).

It structures domain knowledge through a forensic ontology based on the Unified Modeling Language (UML). For instance, Fig. [7.1](#Fig1) illustrates the subphase *ExperimentalProblem*, modeled in Protégé. This approach systematizes DF phases, promoting a model that organizes information, supports documentation, and enhances the reliability of experiments.

![Flowchart illustrating the structure of an experimental problem. Central node labeled “ExperimentalProblem” connects to various nodes representing different components: “VideoRecordingID,” “GrocerySubject,” “ExecutionUseConfederate,” “ExperimentalProjectInquiry,” “DevelopingProcess,” “ExperimentalSpaceRelationship,” “CreditPaymentDifficulty,” “ExperienceEffect,” “EffortManipulation,” “PaymentIssue,” “PreTest,” and “MisleadingExperimentalManipulation.” Each node contains specific attributes, such as IDs, types, and descriptions, indicating their roles in the experiment. The flowchart visually organizes the relationships and dependencies among these components.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig1_HTML.png)

Fig. 7.1

ExperimentalProblem experimental subphase in UML [[5](#CR5)]

A key differentiator of ExperDF-Onto is its flexibility. Unlike ontologies restricted to specific domains, such as the Internet of Things (IoT) or mobile devices, ExperDF-Onto was designed as a versatile, adaptable tool that supports diverse contexts without compromising expert performance. This adaptability promotes knowledge reuse and interoperability with other models and methodologies. Furthermore, UML diagrams can be generated directly from Protégé-structured data, thereby improving both the visualization and dissemination of the ontology’s knowledge, thereby making it more accessible to different audiences [[5](#CR5)].

Another vital contribution of ExperDF-Onto is the extension of the conceptual model through further phases that strengthen investigative and experimental processes. Beyond organizing knowledge in DF, the ontology yields more concrete, structured results, supported by statistical metrics, graphical representations, and rigorous management plans. As a result, experts can produce more consistent and well-founded reports, thereby addressing two significant challenges in Digital Forensics: the lack of standardized documentation and the difficulty of reproducibility in experiments [[5](#CR5)].

In addition to knowledge organization, ExperDF-Onto plays a central role in validating and implementing investigative processes. By providing a reliable framework for experimentation and knowledge representation, the ontology enables more systematic and comprehensive results, directly contributing to the formalization of DF knowledge. Thus, ExperDF-Onto not only enhances investigative practice but also promotes scientific progress in the field, ensuring greater credibility and rigor in forensic processes.

### 7.1.1 ExperDF-Onto Methodology and Design

The ontology was developed using the **SABiO** (Systematic Approach for Built-in Ontology) methodology, a well-established approach for ontology construction. Proposed in 1997, SABiO was first applied to software processes and later to cardiology in the medical domain [[1](#CR1)]. Over time, it has become a reference in ontology development across various fields, organizing the work into two main processes: the **Development Process** and the **Support Processes** (Fig. [7.2](#Fig2)) [[1](#CR1)].

![Flow chart illustrating a development process and support processes. The development process includes steps: Purpose Identification and Requirements Elicitation, Ontology Capture and Formalization, Reference Ontology, Design, Implementation, Operational Ontology, and Testing. Arrows indicate the flow between steps. Support processes listed are Knowledge Acquisition, Documentation, Configuration Management, Evaluation, and Reuse, aligned parallel to the development steps.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig2_HTML.png)

Fig. 7.2

SABiO methodology [[1](#CR1)]

The **Development Process** ensures that the ontology is built on well-defined requirements and aligned with its application context. It begins with **Purpose Identification and Requirements Elicitation**, where the scope, in this case, Digital Forensics, is defined, and relevant information is collected. Next, in **Ontology Capture and Formalization**, requirements are organized and structured into competence questions. As a **domain ontology**, ExperDF-Onto was designed to represent DF-specific concepts, supporting logical and later technical modeling in Protégé [[1](#CR1)].

In the **Design** phase, the ontology begins to take shape. An initial high-level model was created using draw.io and then refined into a formal representation. This transition led to the **Implementation** phase, in which the ontology was encoded in **OWL** (Web Ontology Language), enabling its execution and application in different contexts [[1](#CR1)].

Validation was carried out through a **proof of concept (PoC)**. In this test, the ontology was instantiated in the AuthorMiner2 method, where only 2.94% of its classes and subclasses were activated. Although this indicated limited activation, it highlighted the ontology’s potential to structure data and optimize analyses. A second type of validation, **real-case evaluation**, in which experts apply the ontology to document forensic cases, remains as future work [[1](#CR1)].

The **Support Processes** complement development, ensuring quality, maintenance, and continuous improvement. It includes **Knowledge Acquisition**, drawing from domain literature, and **Documentation**, maintained in Protégé to guarantee transparency and traceability. **Configuration Management** defines execution parameters and version control; in this case, the ontology is stored locally in Protégé, enabling updates. **Evaluation** may involve code-level analysis or technical validation, though the latter has not yet been performed since the ontology is still under development [[1](#CR1)].

SABiO prescribes a **Reuse** stage, which leverages existing models and methodologies [[4](#CR4)]. However, this step was not applied here, since ExperDF-Onto was explicitly developed for DF without relying on preexisting structures [[1](#CR1)].

This structured methodology ensures that ExperDF-Onto is developed systematically and efficiently, supporting its application in both controlled experiments and real-world forensic scenarios. Furthermore, it ensures that the model can be continuously refined, validated, and adapted to new requirements, thereby consolidating the ontology as an essential tool for structuring and formalizing knowledge in Digital Forensics [[1](#CR1), [6](#CR6)].

### 7.1.2 ExperDF-Onto Elements

The main components of this ontology are **Classes**, **Properties**, **Relations**, and **Axioms**.

The **ontology classes** are the pillars of the ontology, representing the core concepts that structure knowledge in Digital Forensics (DF) [[2](#CR2)]. In ExperDF-Onto, these classes are organized according to the main phases of the experimentation process: *planning*, *operation*, *analysis and interpretation*, and *dissemination* (Fig. [7.3](#Fig3)).

![Flow chart depicting a hierarchical structure with “owl:Thing” at the top, followed by “AnalysisInterpretation,” “Dissemination,” “Operation,” “Planning,” and “Pre-Operation.” Each item is connected by dotted lines and marked with circular icons. “Planning” is highlighted.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig3_HTML.png)

Fig. 7.3

Main classes

Each of these classes can be refined into specialized subclasses, allowing a more detailed organization of experiments and greater precision in data analysis and interpretation (Fig. [7.4](#Fig4)). Currently, the ontology comprises 383 classes.

![A hierarchical tree diagram illustrating various categories and subcategories related to analysis and data management. The top node is labeled “owl:Thing,” branching into categories like “AnalysisInterpretation,” “CriminalSource,” “DataPlotting,” “Dissemination,” “Operation,” and “Planning.” Each category further divides into specific subcategories, such as “QualitativeAnalysis,” “Cybercriminal,” “ConflictLaw,” and “DataForensicsManagementPlan,” indicating a structured approach to organizing complex information.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig4_HTML.png)

Fig. 7.4

General class hierarchy

**Properties** provide additional information about classes and their instances, enriching the description of ontology elements [[2](#CR2)]. They are divided into two main types: *object properties*, which connect different ontology elements; for example, the property “threat to validity” links an analysis to factors that may compromise the validity of an experiment (Fig. [7.5](#Fig5)). *data properties*, which associate specific values with elements of the ontology, describing measurable characteristics, for instance, “suspicious action” refers to a particular event in forensic analysis (Fig. [7.6](#Fig6)).

![Screenshot of an ontology editor interface displaying the object property hierarchy for “isOrganizedThreat.” The left panel lists various properties such as “hasContextImpact” and “hasStrategyTreatment.” The right panel shows details for “isOrganizedThreat,” including annotations and characteristics like “Functional” and “Transitive.” The interface includes tabs for different ontology components and a URL at the top.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig5_HTML.png)

Fig. 7.5

Threat to validity

![Screenshot of an ontology editor interface displaying a data property hierarchy. The highlighted property is “Action suspect,” with annotations and characteristics shown on the right. The interface includes tabs for entities, data properties, and annotations, with a list of properties such as “Acceptance criteria” and “Accumulated distribution.” The URL at the top indicates the ontology’s location.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig6_HTML.png)

Fig. 7.6

Suspicious action

**Relationships** define how ontology elements interact, structuring knowledge through logical connections that enhance the accuracy and coherence of analyses. Common examples include “has a child,” “belongs to,” and “is part of.” In the context of DF, the *analysis and interpretation* phase may be associated with a “threat to validity” that, in turn, can affect the “validity of conclusions.” This may either lead to incorrect results or reinforce interpretation patterns. Such relationships ensure a coherent and structured representation of knowledge.

**Axioms** are rules that guarantee the internal consistency of the ontology by preventing contradictions or invalid connections. They impose constraints that ensure logical coherence. For example, every “threat to validity” must be classified into one of four types: internal, external, construct, or conclusion (Fig. [7.7](#Fig7)). These axioms strengthen the ontology by enforcing rigor in the documentation and analysis of experiments.

![Tree diagram illustrating the hierarchy of “Threats Validity” within an ontology. The main class, “Threats Validity,” branches into subclasses: “Conclusion Validity,” “Construct Validity,” “External Validity,” and “Internal Validity.” Each subclass is labeled as a “SubClassOf” the main class. The diagram is part of an ontology editing interface, showing various tabs and options for managing entities and properties.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig7_HTML.png)

Fig. 7.7

Subphase of threat to validity

This structured approach not only facilitates the organization of data and experiments but also improves the reliability of analyses, ensuring that results can be interpreted and replicated with confidence.

#### 7.1.2.1 Planning

The planning phase is the starting point of an experiment, ensuring that all aspects are well-structured before execution. In this phase, essential elements are defined, including variables, hypotheses, experimental design, instruments, and participant selection [[3](#CR3)].

Figure [7.8](#Fig8) illustrates the main components of this phase, including the incorporation of the **PDFData**, **ActivityLog**, and **SupportMaterial** subphases.

![Flow chart illustrating a process with interconnected nodes. The nodes include “Planning,” “PDFData,” “ActivityLog,” “PlannedTreatmentFactor,” and “SupportMaterial.” Arrows indicate the flow of information between these nodes, with “PDFData” being a central point connected to all other nodes. Different arrow styles and colors represent various types of relationships or data flows.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig8_HTML.png)

Fig. 7.8

ExperDF-Onto Excerpt of the Planning phase

The main elements of the planning phase are:

* **Variables** are classified as independent (manipulated) or dependent (influenced and measured to assess effects).
* **Hypotheses** can be null (no significant effect) or alternative (measurable impact), forming the foundation of the study [[3](#CR3)].
* **Experimental design** defines how the study will be conducted, ensuring validity and reproducibility.
* **Instruments** may include programming code, questionnaires, or specialized tools, which must be validated to guarantee accuracy.
* **Replication** verifies whether results can be reproduced in different contexts. Replication can be internal (same group) or external (other researchers) and exact (all details are maintained) or conceptual (an adapted approach).
* **Participants** are selected by statistical sampling for representativeness or by specific criteria depending on the study.
* **FG phases** organize the experimental process from data collection and analysis to documentation, ensuring clarity and reliability [[3](#CR3)].

In addition, three subphases strengthen organization and documentation:

* **Activity Log**: a detailed logbook that records all steps and actions, facilitating the preparation of the final report and ensuring traceability
* **PDFData**: storage of reports and documents in PDF format, including references, notes, and records of queries
* **SupportMaterial**: auxiliary resources that support execution and analysis, such as source code, configuration files, and computational tools

Together, these elements ensure that the planning phase not only defines the experiment’s structure but also facilitates its analysis, interpretation, and dissemination, making the process more organized, documented, and controlled.

#### 7.1.2.2 Pre-Operation

The Pre-Operation phase prepares the environment for experiment execution, ensuring that all necessary components are configured and operational. This stage includes setup, training, benchmark, pilot project, and the definition of the scenario in which the experiment will take place [[3](#CR3)].

Figure [7.9](#Fig9) illustrates the main elements of this phase, including the **ScenarioType** subphase.

![Flow chart depicting a sequence from “PilotProject” to “Scenario” and then to “ScenarioType.” Each step is represented by a rounded rectangle with arrows indicating the flow direction. The “Scenario” step is highlighted with a green border.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig9_HTML.png)

Fig. 7.9

ExperDF-Onto Excerpt of the Pre-Operation phase

The pre-operation steps can be summarized as follows:

* **Setup**: configuration of software (operating systems, virtual machines, and applications), hardware (volatile and persistent memories), and algorithms (programmed with predefined parameters to ensure correct information handling) [[3](#CR3)]
* **Training**: execution of initial tests to validate the functioning of systems, algorithms, and components before the experiment
* **Benchmark**: a measurement of system performance to ensure that all elements meet the study’s requirements
* **Pilot project**: preliminary execution to verify the feasibility of configurations. At this stage, the **scenario** is defined, which may include virtual machines, databases, IoT devices, or specific analysis tools [[3](#CR3)].

Within the scenario subphase, ExperDF-Onto introduces the concept of **ScenarioType**, which specifies the type of environment in which the experiment is carried out. Different scenario types can directly influence the results:

* **Physical scenario**: based on real equipment such as sensors and servers
* **Virtual scenario**: experimentation through simulations in virtual machines
* **Hybrid scenario**: combination of physical and virtual resources
* **Distributed virtual environments**: complex setups with virtual machines in different regions or systems using OPC simulators

Distinguishing among these scenario types enhances the precision of the analysis, helping to understand how varying configurations affect the performance and reliability of experimental results.

#### 7.1.2.3 Operation

The Operation phase encompasses all elements necessary to experiment, ensuring that data is collected, organized, and processed accurately. This phase comprises the participant, the instrument used, the operational procedures, the sample, and the generated data [[3](#CR3)].

Figure [7.10](#Fig10) presents the main structure of this phase, including the new subphases we introduced.

![Flow chart illustrating the concept of “Limitation” as the central node. Connected nodes include “AnalysisInterpretation,” “LimitacaoAnalise,” “ToolAN,” “ConflictLaw,” “OpinionDF,” and “InterpretationChallenge.” Arrows indicate relationships and flow between these concepts, with various colors and styles representing different types of connections.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig10_HTML.png)

Fig. 7.10

ExperDF-Onto Excerpt of the Operation phase

The basic elements of the operation are:

* **Participant**: an individual directly involved in the experiment or someone who contributes indirectly by providing information for analysis
* **Instrument**: tools used to collect and process data, such as models, databases, or metadata
* **Sample**: the subset of data selected for analysis
* **Data** may be *original data*, collected directly from the source without modifications, or *duplicate data*, created for backup or additional testing without compromising the primary dataset.
* **Operational procedures**: standardized sequences of actions that ensure reproducibility. For example, in API interactions, a typical sequence may involve creating a resource, retrieving its data, and modifying it if necessary [[3](#CR3)].

To improve the evaluation of experimental procedures, we expanded the **OperationProcedure** with new subphases: **Experiment**, **FormulationContext**, **HypothesisTestO**, **Project**, **Protocol**, and **TheoreticalModelFormulation**. Their roles are as follows:

* **Experiment**: the core of the operation phase, defining tools, participants, data, and procedures for systematic execution and result collection
* **FormulationContext** establishes the study’s environment and conditions, documenting variables, objectives, constraints, and contextual factors.
* **HypothesisTestO** verifies whether the study’s assumptions are confirmed or refuted, providing an objective evaluation of collected data.
* **Project** details all necessary planning, including methodologies, tools, technical configurations, and study structure, ensuring reliability.
* **Protocol** defines the rules and guidelines for execution. For instance, in API experiments, it specifies the order of requests to ensure correct communication and data transmission.
* **TheoreticalModelFormulation** provides a solid theoretical foundation by applying established and validated models from the literature and practice.

With these elements and subphases, the operation phase becomes more structured, rigorous, and practical, ensuring accurate execution and interpretation of experimental results.

#### 7.1.2.4 Analysis and Interpretation

The analysis and interpretation phase examines the experimental data to extract relevant information and transform the results into meaningful insights. At this stage, patterns are identified, hypotheses are verified, and relationships between variables are explored [[3](#CR3)].

Figure [7.11](#Fig11) illustrates the subclasses added in this phase, which support the identification of limitations and documentation of the final report.

![Flow chart illustrating the concept of “Limitation” as the central node. Connected nodes include “AnalysisInterpretation,” “LimitacaoAnalise,” “ToolAN,” “ConflictLaw,” “OpinionDF,” and “InterpretationChallenge.” Arrows indicate relationships between these elements, with various colors and styles representing different types of connections.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig11_HTML.png)

Fig. 7.11

ExperDF-Onto Excerpt of the Analysis and Interpretation phase

Data is organized in a structured way and represented clearly, using graphs, tables, or other visualizations that facilitate interpretation. This helps identify trends, verify hypotheses, and detect inconsistencies that may affect conclusions [[3](#CR3)].

Analysis can follow two main approaches:

* **Qualitative analysis**: interpretation based on context and observation, such as manual review of records, group discussions, or the use of tools for organizing information
* **Quantitative analysis**: interpretation based on statistics and calculations, such as averages, statistical tests, and regression models, providing objective and measurable conclusions [[3](#CR3)]

Another critical aspect of this phase is recognizing limitations and threats to validity. These may stem from the quality of information collected, the accuracy of measurements, or interference from external factors [[3](#CR3)].

To capture such aspects, the ontology was expanded with the subclasses **ConflictLaw**, **InterpretationChallenge**, **OpinionDF**, and **ToolAN**:

* **ConflictLaw** addresses legal divergences that may affect the interpretation or application of results, such as privacy and data protection laws that vary across jurisdictions.
* **InterpretationChallenge** highlights ambiguities, inconsistencies, or missing context in the data, which may lead to misinterpretations.
* **OpinionDF** acknowledges that different experts may interpret the same dataset differently, depending on their knowledge, experience, and professional background.
* **ToolAN** refers to the role of technology in data analysis, while noting limitations due to compatibility issues, licensing restrictions, outdated versions, or processing differences.

Together, these elements ensure that the analysis and interpretation phase not only extracts insights from the data but also documents limitations, thereby increasing the reliability and transparency of the experimental results.

#### 7.1.2.5 Dissemination

The dissemination phase ensures that the data collected in the experiment is organized and shared in a safe, transparent, and accessible way. This stage consolidates all final information so that the academic community and other stakeholders can access the collected evidence. Following good practices for publishing and sharing is essential to guarantee reliability and reproducibility [[3](#CR3)].

To structure this step, ExperDF-Onto adopted the ExperDF-CM conceptual model, which defines the main elements of dissemination.

Figures [7.12](#Fig12) and [7.13](#Fig13) illustrate the expanded ontology supporting this phase.

![Flow chart illustrating a process starting with “Dissemination” leading to “DiaryAnnotation.” From “DiaryAnnotation,” arrows point to “Researcher,” “TechnicalReview,” “DoR,” “Draft,” and “Forensicexpert,” indicating various pathways and roles involved in the process. Different arrow styles and colors suggest distinct types of connections or actions.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig12_HTML.png)

Fig. 7.12

Recording experimental notes

![Flow chart illustrating the relationship between “Dissemination” and “Presentation Quality,” which branches into several categories: “Researcher,” “Repository,” “Academy,” “OperationalID,” “Enthusiastic,” “GraphicRepresentationD,” “Oral,” and “RepositoryD.” Arrows indicate connections, with varied colors and styles representing different types of relationships.](../images/624027_1_En_7_Chapter/624027_1_En_7_Fig13_HTML.png)

Fig. 7.13

Data presentation quality

The original model included the following elements:

* **Forensic Data Management Plan (FDMP)** ensures data is organized and stored properly.
* **Dataset Metadata** provides detailed information to facilitate the understanding and reproduction of experiments.
* **Journal/Notes**: continuous record of procedures and actions taken throughout the experiment
* **Experimental Issues**: documents challenges and problems encountered that may affect results
* **Dataset**: all documents and information collected during the experiment
* **Repository**: storage location where data is made accessible
* **Unique ID**: identifier such as a DOI, ensuring traceability and authenticity of the dataset
* **Citation**: guidelines for referencing the dataset, guaranteeing proper attribution
* **Authorship** identifies contributors and acknowledges their roles.

The ontology was later expanded with new categories:

* **DoR (Declaration of Responsibility)** specifies responsibilities for each part of the experiment.
* **Draft** allows the creation of preliminary versions of records for review before final documentation.
* **TechnicalReview** ensures that the information is critically evaluated and validated.

Additionally, the **PresentationQuality** category was included to guarantee clarity and accessibility of results, subdivided into:

* **GraphicRepresentationD**: use of graphs, tables, and diagrams to illustrate data
* **OperationalDocumentationD**: detailed explanation of methods and tools employed
* **OralPresentationD**: dissemination of results at conferences, lectures, and similar events
* **RepositoryStorageD**: preservation and availability of data in trusted repositories

Through these elements, the dissemination phase ensures that experimental records are systematically organized, securely preserved, and made more accessible for reuse, interpretation, and further research.

## 7.2 Writing and Executing SPARQL Queries in ExperDF-Onto

This section demonstrates how to query the ExperDF-Onto ontology using SPARQL, with a focus on navigating class hierarchies and retrieving structured knowledge across each phase of the digital forensics experimental life cycle. Queries are executed using Protégé’s SPARQL tab, which enables direct inspection of the ontology, verification of structural consistency, and exploration of the conceptual model.

We begin by identifying the ontology’s top-level classes and, subsequently, present queries organized by experimental phases: Planning, Pre-Operation, Operation, Analysis and Interpretation, and Dissemination. Each subsection introduces the queries’ goals, explains their logic, and presents the retrieved results.

### 7.2.1 Identifying Top-Level Classes

The query in Listing [7.1](#FPar1) retrieves all top-level classes, meaning those that have no superclasses defined. This provides an overview of the ontology’s main structural pillars.

Listing 7.1 SPARQL query to identify top-level classes

![Defines three web resource prefixes for RDF syntax, RDF schema, and OWL ontology. Then selects unique classes labeled as OWL classes that do not have any superclass, filtering out subclasses. This query identifies top-level classes in an ontology without parent classes.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaaa_HTML.png)

The following box presents the exact output returned by executing this query:

**Top-Level Classes Retrieved from Listing** [**7.1**](#FPar1)

* Planning
* Pre-Operation
* Operation
* AnalysisInterpretation
* Dissemination

### 7.2.2 Planning Phase Queries

The Planning phase contains the richest set of conceptual structures in ExperDF-Onto. The following queries explore both its immediate subclasses and the complete set of nested subclasses.

#### 7.2.2.1 Direct Subclasses of Planning

The following query retrieves only the immediate subclasses of Planning.

Listing 7.2 SPARQL query to retrieve direct subclasses of Planning

![A code snippet defining a query that selects distinct subclasses of a specific class identified by a web address related to planning in an ontology. It uses a prefix for RDF schema and a WHERE clause to specify the subclass relationship.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaab_HTML.png)

The following box contains the query output exactly as returned by Protégé:

**Direct Subclasses of Planning**

DFProcessPhase, ExperimentType, ExperimentalUnit, Hypothesis, InstrumentP, Objective, PDFData, ParticipantP, TypeProject, Variable.

#### 7.2.2.2 All Subclasses of Planning

To retrieve the whole hierarchy of subclasses, the following query uses the transitive operator rdfs:subClassOf+.

Listing 7.3 SPARQL query to retrieve all subclasses of Planning

![Defines a query to select all unique subclasses of the class labeled "Planning" from a specified ontology using the RDF schema prefix. The query identifies subclasses by checking if they are directly or indirectly subclasses of the "Planning" class within the given ontology URL.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaac_HTML.png)

The following box reports the complete list of subclasses returned by Protégé:

**All Subclasses of Planning**

Activity, ActivityLog, AlternativeHypothesis, Analysis, AnalyzeP, Artifact, AutoSelectionSampling, Bilateral, Category, CognitivePhysicalDemand, ComponentNotCollected, ConceptualReplication, ConclusionSpecialist, ConglomerateRandomSampling, Constant, Control, DFAcquisition, DFAnalysis, DFExamination, DFProcessPhase, DFReporting, DataExtraction, DataMining, DecryptionData, DependentReplication, DependentVariable, DependentVariableMetric, DeviceIdentifier, DocumentationActivityMonitor, DocumentationConditionSO, DocumentationProtocol, EthicalPlanning, EvidencePlanning, ExperimentalUnit, ExternalReplication, GroupComparison, Hypothesis, IndependentVariable, InstrumentP, IntentionalSampling, KnowledgeResourceCondition, LegalPlanning, MaintainabilityPlanning, MaterialResourceCondition, MetadataPlanning, ModelPlanning, Objective, OntologyPlanning, OperationalPlanning, Opinion, ParticipantP, PerformancePlanning, PilotPlanning, PlanningStage, PoliticalCondition, Probabilistic, ProportionalQuotaSampling, QualityPlanning, QuotaSampling, RandomSampling, ReliabilityPlanning, ReplicationPlanning, ReproducibilityPlanning, ResourcePlanning, ResearchPlanning, ReviewPlanning, ScalabilityPlanning, SimulationPlanning, SnowballSampling, SocialCondition, SpecializedDependentVariable, StatisticalPlanning, StratifiedRandomSampling, SurveyPlanning, TechnicalPlanning, TemporalCondition, ToolResourceCondition, TraceabilityPlanning, TransactionalResearch, TransparencyPlanning, Treatment, TypicalVariable, TypeProject, UsabilityPlanning, ValidationPlanning, Variable.

#### 7.2.2.3 Direct Subclasses of Variable

The following query illustrates how to retrieve immediate subclasses of a specific Planning class.

Listing 7.4 SPARQL query to retrieve direct subclasses of Variable

![Defines a prefix named "rdfs" linked to the RDF schema namespace. The query selects distinct subclasses where the subclass is a subclass of a specific variable identified by a URL from an ontology created by Thiago da Silva in 2022. This query is used to find all subclasses related to that particular variable within the ontology.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaad_HTML.png)

The following box contains the exact results returned by this query:

**Direct Subclasses of Variable**

* DependentVariable
* IndependentVariable

### 7.2.3 Pre-Operation Phase Queries

The Pre-Operation phase includes activities such as setup, benchmarking, training, and environment configuration. The following queries inspect its structure.

#### 7.2.3.1 Direct Subclasses of Pre-Operation

Listing 7.5 SPARQL query to retrieve direct subclasses of Pre-Operation

![Query written in a programming language to select distinct subclasses that are defined as subclasses of a specific class named "Pre-Operation" within an ontology hosted at a given web address. The query uses a prefix to reference the RDF schema vocabulary and retrieves unique subclass identifiers related to the specified ontology class.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaae_HTML.png)

Below is the direct output of the SPARQL execution:

**Direct Subclasses of Pre-Operation**

Benchmark, PilotProject, Setup, Training

#### 7.2.3.2 All Subclasses of Pre-Operation

Listing 7.6 SPARQL query to retrieve all subclasses of Pre-Operation

![Defines a query prefix for RDF schema and selects distinct subclasses of a specific pre-operation class from an ontology URL, showing how to retrieve all subclasses related to that pre-operation concept.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaaf_HTML.png)

The following box contains the full execution result returned in Protégé:

**All Subclasses of Pre-Operation**

AdditionInstruction, Algorithm, Application, ApplicationBenchmark, Argument, Assignment, Benchmark, Cache, CacheConfiguration, CacheLocation, Category, Class, Classification, Cluster, ClusterAlgorithm, ClusterAssignment, ClusterConfiguration, ClusterMethod, ClusterModel, ClusterSetup, ClusterTraining, Clustering, Comparison, Configuration, Data, DataApplication, DataAssignment, DataBenchmark, DataCache, DataCategory, DataClass, DataCluster, DataConfiguration, DataEvaluation, DataLocation, DataMethod, DataModel, DataPilotProject, DataProcess, DataProgram, DataSetup, DataStage, DataSystem, DataTraining, Evaluation, EvaluationAlgorithm, EvaluationBenchmark, EvaluationMethod, EvaluationModel, Instruction, Location, Method, Model, PilotProject, Process, Program, Setup, Stage, System, Training, Value.

### 7.2.4 Operation Phase Queries

This phase captures procedural actions, data operations, and tool execution steps. The queries explore its conceptual hierarchy.

#### 7.2.4.1 Direct Subclasses of Operation

Listing 7.7 SPARQL query to retrieve direct subclasses of Operation

![A code snippet defining a SPARQL query that selects distinct subclasses of a specific class identified by a web address related to an ontology operation. The query uses a prefix for RDF schema vocabulary and retrieves all subclasses of the given operation class from the ontology. This is important for extracting hierarchical relationships within the ontology data.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaag_HTML.png)

The box below reproduces the exact results from the SPARQL query:

**Direct Subclasses of Operation**

DataP, Instrument, OperationProcedure, Participant

#### 7.2.4.2 All Subclasses of Operation

Listing 7.8 SPARQL query to retrieve all subclasses of Operation

![Defines a query prefix for RDF schema and selects distinct subclasses of a specific operation class from an ontology located at a given web address, identifying all subclasses related to that operation.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaah_HTML.png)

The following box shows the complete response returned by the query:

**All Subclasses of Operation**

Autonomous, ChainofCustodyDocumentation, ChangeMetadata, CleaningExperiment, Code, ConfidenceLevel, CopyDataStreamFailed, Cryptography, DataCaving, DataLossNotFiled, DataP, Decrypt, Delete, Error, Execute, Execution, ExperimentExecution, ExperimentRun, ExperimentStep, File, FileTransfer, Hashing, Instrument, Logging, MetadataUpdate, Monitoring, NetworkOperation, OperationProcedure, OperationStep, Operator, Output, Participant, Processing, ProcessMonitoring, ProgramExecution, Read, Recovery, Replication, Result, Run, Save, Scheduling, Script, Simulation, SoftwareExecution, Storage, Transfer, Upload, UserAction, Validation, Write.

### 7.2.5 Analysis and Interpretation Phase Queries

This phase includes statistical techniques, visualization strategies, and interpretative frameworks essential for deriving meaning from experimental evidence.

#### 7.2.5.1 Direct Subclasses of AnalysisInterpretation

Listing 7.9 SPARQL query to retrieve direct subclasses of AnalysisInterpretation

![Defines a query prefix for RDF schema and selects distinct subclasses of a specific ontology class identified by a web address, aiming to retrieve all unique subclasses related to the class named "Analysis Interpretation" within that ontology.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaai_HTML.png)

The following box presents the direct output from SPARQL execution:

**Direct Subclasses of AnalysisInterpretation**

AnalysisTechnique, AnalysisThroughStructure, CriminalSource, DataPlotting, Limitation, ThreatsValidity

#### 7.2.5.2 All Subclasses of AnalysisInterpretation

Listing 7.10 SPARQL query to retrieve all subclasses of AnalysisInterpretation

![Defines a prefix named "rdfs" linked to the RDF schema URL, then selects distinct subclasses of the class identified by the URL ending with "untitled-ontology-69#AnalysisInterpretation" from a semantic web ontology.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaaj_HTML.png)

The following box contains the entire set of subclasses returned:

**All Subclasses of AnalysisInterpretation**

AnaliseUnivariada, AnalysisTechnique, AnalysisThroughStructure, AndersonDarling, BarChart, BivariateAnalysis, Boxplot, BungeRating, CentralTendencyA, CentralTrend, ChiSquare, Classification, ClusterAnalysis, Coefficient, ComparisonPlot, ConfidenceInterval, Correlation, CorrelationCoefficient, CriminalSource, Crosstab, DataPlotting, DataRepresentation, DataVisualization, DensityPlot, DescriptiveAnalysis, DescriptiveStatistic, Diagnostic, Distribution, ErrorEstimation, FactorAnalysis, FrequencyDistribution, GraphicalMethod, Histogram, HypothesisTest, InferentialAnalysis, InterpretationModel, KruskalWallis, Kurtosis, Limitation, LinearRegression, LogisticRegression, MannWhitney, MeanComparison, MedianTest, MetaAnalysis, ModeAnalysis, MultivariateAnalysis, NormalityTest, OutlierDetection, PValue, ParametricTest, PearsonCorrelation, Plot, ProbabilityAnalysis, ProbabilityDistribution, QualitativeAnalysis, QuantitativeAnalysis, Quartile, Regression, ReliabilityAnalysis, ResidualAnalysis, ResultInterpretation, SamplingError, ScatterPlot, ShapiroWilk, SignificanceLevel, SpearmanCorrelation, StandardDeviation, StatisticalAnalysis, StatisticalTest, StudentTest, SurvivalAnalysis, TTest, TestPower, ThreatsValidity, TimeSeries, TrendAnalysis, Uncertainty, UnivariateAnalysis, ValidityTest, Variability, Variance, VarianceAnalysis, WilcoxonTest, ZTest.

### 7.2.6 Dissemination Phase Queries

This phase models the communication of results, data publication, reporting standards, and mechanisms for scientific transparency.

#### 7.2.6.1 Direct Subclasses of Dissemination

Listing 7.11 SPARQL query to retrieve direct subclasses of Dissemination

![A code snippet defining a prefix for RDF schema and a query that selects distinct subclasses of a specific ontology class related to dissemination, showing how to retrieve subclass information from the ontology.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaak_HTML.png)

The next box shows the exact output of the SPARQL query:

**Direct Subclasses of Dissemination**

DataForensicsManagementPlan, DataSet, DiaryAnnotation, ExperimentalIssues, ImpactDocument, PresentationQuality

#### 7.2.6.2 All Subclasses of Dissemination

Listing 7.12 SPARQL query to retrieve all subclasses of Dissemination

![A code snippet defines a prefix for RDF schema and performs a query to select distinct subclasses of a specific ontology class related to dissemination, showing how to retrieve subclass information from an ontology using SPARQL.](../images/624027_1_En_7_Chapter/624027_1_En_7_Figaal_HTML.png)

The response returned by the execution of this query is shown below:

**All Subclasses of Dissemination**

AuthenticationFrequency, Authorship, CheckList, Citation, CombinationNumber, CreditPaymentDifficulty, Data, DataArchiving, DataCitation, DataForensicsManagementPlan, DataManagement, DataSet, DataSharing, DataStorage, DataTransparency, DiaryAnnotation, DigitalIdentifier, DisseminationPlan, DocumentPublication, DocumentReview, ExperimentalIssues, ExternalPublication, FormatStandard, ImpactAssessment, ImpactDocument, Indexing, JournalPublication, KnowledgeDissemination, Licensing, LiteratureReview, Metadata, OpenAccess, OpenScience, PeerReview, PosterPresentation, Preprint, Presentation, PresentationQuality, Publication, PublicationBias, PublicationChannel, PublicationEthics, Publisher, QualityAssessment, ReproducibilityReport, ResearchData, ResearchDiary, ResearchImpact, ResearchPublication, ScientificCommunication, ScientificContribution, ScientificDissemination, ScientificJournal, ScientificOutput, Standardization, Transparency, ValidationReport, WorkshopProceeding, WritingGuideline.

## 7.3 Final Remarks

ExperDF-Onto consolidates a comprehensive, formalized representation of the experimental life cycle in Digital Forensics, transforming the conceptual structures of ExperDF-CM into a machine-interpretable ontology that supports rigorous, transparent, and reproducible forensic investigations. By organizing more than 600 conceptual elements into five interconnected phases, the ontology provides not only a semantic backbone for structuring experiments but also a practical asset for guiding methodological decisions, documenting procedures, and integrating domain-specific knowledge across heterogeneous investigative contexts.

The adoption of the SABiO methodology ensured a systematic and traceable development process, from purpose elicitation to implementation and evaluation. This methodological grounding enhances the ontology’s internal coherence and positions it as a reusable resource for future extensions, including integration with provenance models, computational tools, and forensic platforms. The proof-of-concept instantiation demonstrated the ontology’s potential to structure experimental data and support automated reasoning, although extensive real-world validation remains an essential step in its maturation.

By incorporating detailed modeling of hypotheses, variables, procedures, scenario configurations, threats to validity, documentation practices, and dissemination structures, ExperDF-Onto directly addresses persistent challenges related to methodological rigor and reproducibility in Digital Forensics. The SPARQL query patterns presented in this chapter illustrate how researchers and practitioners can explore, audit, and validate the ontology, enabling both conceptual understanding and computational inspection.

As Digital Forensics continues to evolve in response to technological complexity, ExperDF-Onto provides a foundational layer for formalizing experimental practices, enabling more reliable knowledge accumulation and fostering alignment with FAIR and Open Science principles. Future work will focus on empirical validation in real forensic scenarios, integration with workflow management tools, and the development of automated reasoning modules that leverage the ontology to support decision-making, documentation quality, and scientific transparency.

## References

1. 1.

   Falbo, R.A.: SABiO: systematic approach for building ontologies. In: Proceedings of the 1st Joint Workshop on Ontologies in Conceptual Modeling and Information Systems Engineering (CEUR-WS), vol. 1201 (2014)
2. 2.

   Mirror, J.C.: Guia prático de construção de ontologias—protégé v. 5.2. ResearchGate **9**, 3–134 (2018)
3. 3.

   Oliveira, E. Jr, Zorzo, A.F., Neu, C.V.: Towards a conceptual model for promoting digital forensics experiments. Foren. Sci. Int.: Digit. Invest. **35**, 301014 (2020). [https://​doi.​org/​10.​1016/​j.​fsidi.​2020.​301014](https://doi.org/10.1016/j.fsidi.2020.301014)
4. 4.

   Scherp, A., Saathoff, C., Franz, T., Staab, S.: Designing core ontologies. Appl. Ontol. **6**(3), 177–221 (2011)<https://doi.org/10.3233/AO-2011-0096>
5. 5.

   Silva, T.J., Mazur, A.H., Oliveira, E. Jr, Zorzo, A.F., Barcellos, M.P.: An ontology for promoting controlled experimentation in digital forensics. Foren. Sci. Int.: Digit. Invest. **52**, 301845 (2025)
6. 6.

   Suárez-Figueroa, M.C., Gómez-Pérez, A., Motta, E., Gangemi, A.: Introduction: ontology engineering in a networked world. In: Ontology Engineering in a Networked World, pp. 1–6. Springer, New York, NY (2011)

# Part IV ExperDF-Onto Walkthroughs of Exemplary Digital Forensics Experiments

This part presents a comprehensive and didactic walkthrough of how *ExperDF-Onto* can be instantiated to describe, reason about, and evaluate real digital forensics experiments. While the previous parts established the conceptual and ontological foundations of the framework, this part marks a decisive shift from *theory* to *practice*.

Its purpose is not merely to illustrate ontology use but also to demonstrate how a semantic framework can transform empirical investigations into structured, interoperable, and verifiable scientific assets. Each example progresses toward higher ontological maturity, showing how formal representations encode research intent, experimental rigor, provenance, and dissemination practices in a consistent and machine-actionable form.

By following five representative forensic scenarios that range from memory analysis and smartphone extractions to blockchain-based provenance, this part highlights the expressive capacity of *ExperDF-Onto* in uniting technical, ethical, and epistemological dimensions of experimentation.

This part also serves as a pedagogical bridge between abstract ontology and applied research methodology. Each chapter is designed to help readers:

⋅Understand how narrative experimental designs can be decomposed into explicit ontological elements such as Experiment, ResearchQuestion, IndependentVariable, and DatasetMetadata.

⋅Observe how formal relations such as hasDependentVariable, isControlledBy, and producedBy capture logical dependencies among planning, execution, and interpretation.

⋅Learn to trace reproducibility through explicit metadata, provenance chains, and dissemination entities that make research auditable and transparent.

⋅Reflect on how the ontology reinforces scientific rigor, ethical responsibility, collaborative openness, and long-term data stewardship.

Each case study, although situated in a specific subdomain of Digital Forensics, has been rewritten as a guided *walkthrough*. Readers can follow each phase, from hypothesis formulation to data publication, under a unified vocabulary that makes comparisons across domains consistent and instructive.

The five chapters included in this part represent exemplary experiments that collectively demonstrate the breadth and adaptability of *ExperDF-Onto*:

1. **The Memory That Would Not Lie**—a reproducibility study on live memory acquisition emphasizing tool equivalence, experimental control, and quantitative reliability

2. **Unlocking the Locked: Smartphone Bypass Experiments**—a comparison of physical and logical extraction methods across Android and iOS, modeling ethical constraints and legal compliance

3. **The Case of the Altered Cloud Logs**—a cloud forensics simulation that detects tampered log entries across providers and focuses on provenance and detection accuracy

4. **Echoes in the IoT Lab**—a smart home intrusion scenario capturing temporal and causal relations among IoT devices, illustrating complex event reconstruction

5. **The Invisible Signature: Blockchain Provenance**—a blockchain-based approach to dataset traceability and authenticity integrating governance, quality assessment, and immutability guarantees

Each example follows the same logical flow based on the five research phases defined by *ExperDF-CM*: **Planning**, **Pre-operation**, **Operation**, **Analysis and Interpretation**, and **Dissemination**. This structure ensures that the ontology is not presented as an abstract schema but as a practical framework guiding the entire research life cycle.

Analyzing these five walkthroughs together reveals how ontological instantiation helps to quantify the maturity and reproducibility of experiments. Early cases highlight methodological rigor and control of variables, while later ones incorporate governance, provenance traceability, and open science compliance. Ontological completeness increases progressively, from 68% in the first example, focused on operational reproducibility, to 80% in the last, centered on provenance and governance. This evolution reflects the growth of Digital Forensics itself, moving from isolated technical investigations toward integrated, multidisciplinary studies aligned with open science principles.

**Key Takeaways**

⋅**Ontology as methodology:** *ExperDF-Onto* guides experimenters toward explicit, coherent, and ethically responsible research design.

⋅**Ontology as documentation:** Every experimental decision, including variable selection, tool choice, dataset creation, and analysis method, becomes semantically traceable, supporting reuse and auditability.

⋅**Ontology as integration layer:** Shared ontological patterns enable comparison and federation of experiments across domains, institutions, and research infrastructures.

This part demonstrates that ontological modeling is not an abstract academic exercise but a concrete mechanism for strengthening the credibility and transparency of digital investigations. By systematically encoding research processes, *ExperDF-Onto* ensures that forensic evidence and experimental data are reproducible, interpretable, and reusable across different contexts.

This part concludes the applied dimension of the book. The following part extends these ideas toward ecosystem-level integration, connecting experiments, repositories, provenance networks, and policy frameworks to build a transparent, trustworthy, and cumulative infrastructure for Digital Forensics research.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_8>

# 8. Example 1: The Memory That Would Not Lie

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter provides a complete walkthrough of a controlled digital forensics experiment that examines the reproducibility and reliability of volatile memory acquisition. The investigation explored whether different live memory acquisition tools produce consistent and equivalent forensic artifacts when applied to identical systems under identical conditions. Volatile memory, being highly dynamic and sensitive to timing, presents unique challenges to digital investigators who must ensure that the process of evidence acquisition does not alter the state being measured. To address this, the study was modeled through *ExperDF-Onto*, an ontology designed to formally represent every phase of a digital forensic experiment, making methodological decisions explicit, auditable, and machine-actionable. The experiment’s design included well-defined hypotheses, independent and dependent variables, and controlled conditions to assess the effects of three widely used acquisition tools: Volatility, Rekall, and Belkasoft Live RAM Capture. A series of virtualized environments was configured to standardize the tests, and pilot runs were executed to confirm baseline reproducibility. During execution, every operation, artifact, and measurement was instantiated as an ontological element, creating a semantically linked chain of provenance that connects the research question to the produced data and analytical results. Statistical analysis using ANOVA revealed no significant differences among tools, with a reliability coefficient of 0.96, demonstrating strong internal consistency in acquisition performance. Beyond the technical results, the chapter emphasizes the importance of representing experimental procedures, parameters, and results in a structured ontology to promote transparency, replicability, and long-term accessibility. By publishing all associated datasets and metadata through open repositories, the experiment exemplifies how ontological modeling can transform traditional forensic procedures into open, reusable, and verifiable scientific workflows, thereby reinforcing the epistemic reliability and ethical accountability of Digital Forensics as a scientific discipline.

## 8.1 Context and Motivation

Volatile memory acquisition is a cornerstone of incident response and malware analysis, yet tool behavior, operating system internals, and timing can affect what is captured and how it is reconstructed. The researchers designed a controlled study to ask a deceptively simple question: **Do different acquisition tools produce materially equivalent results for the same running system under the same conditions?** This example demonstrates how *ExperDF-Onto* captures the complete chain of reasoning from the motivating question to the final, shareable artifacts, including every decision and constraint that affects reproducibility and interpretation.

This walkthrough shows how to move from a narrative scenario to a fully instantiated ontological representation. At each phase, we explain why a concept matters, how it is instantiated, which relations connect it to other elements, and what typical pitfalls to avoid.

## 8.2 Planning Phase

The planning phase translates a broad concern into testable hypotheses, measurable variables, and auditable decisions. In *ExperDF-Onto*, this means instantiating classes such as Experiment, ResearchQuestion, Hypothesis, IndependentVariable, DependentVariable, and ControlVariable and linking them by object properties like hasIndependentVariable, hasDependentVariable, and isControlledBy as follows:

* **Experiment** *(why)* establishes scope and identity of the study. **Instance:** Exp\_VM\_Reproducibility.
* **ResearchQuestion** *(why)* frames measurable uncertainty. **Instance:** RQ\_tool\_equivalence.
* **Hypothesis** *(why)* asserts an expected relation. **Instance:** H0\_no\_tool\_effect and H1\_tool\_effect.
* **IndependentVariable** *(why)*: manipulated factor. **Instance:** IV\_AcquisitionTool with levels {Volatility, Rekall, BelkasoftLiveRAM}.
* **DependentVariable** *(why)*: measured outcomes. **Instances:** DV\_RecoveredProcesses, DV\_OpenPorts, DV\_Handles.
* **ControlVariable** *(why)* holds sources of variation constant. **Instances:** CV\_OSVersion, CV\_MemSize, CV\_BackgroundLoad.
* **ConfoundingFactor** *(why)* documents risks to causal inference that cannot be fully controlled. **Instances:** CF\_TimestampDrift, CF\_HypervisorCaching.
* **EthicalPlanning** *(why)* protects participants and privacy. **Instance:** EP\_SyntheticWorkloadsOnly.
* **ReplicationPlanning** *(why)* commits to transparency before results exist. **Instance:** RP\_OSF\_prereg\_VMR.

To do so, we used the following relations: Exp\_VM\_Reproducibility hasResearchQuestion RQ\_tool\_equivalence; Exp\_VM\_Reproducibility hasHypothesis H0\_no\_tool\_effect; Exp\_VM\_Reproducibility hasIndependentVariable IV\_AcquisitionTool; DV\_RecoveredProcesses isMeasuredUnder IV\_AcquisitionTool; Exp\_VM\_Reproducibility isControlledBy CV\_OSVersion, CV\_MemSize, CV\_BackgroundLoad; Exp\_VM\_Reproducibility considersConfounding CF\_TimestampDrift.

We also list pitfalls and how the ontology prevents them:

* *Pitfall:* treating tool choice as a mere operational detail. *Prevention:* Modeling IV\_AcquisitionTool forces explicit manipulation and level definition.
* *Pitfall:* vague outcomes. *Prevention:* Explicit DependentVariable classes encourage metric definitions upfront.
* *Pitfall:* hidden constraints. *Prevention:* ControlVariable and ConfoundingFactor make non-manipulated influences visible and auditable.

## 8.3 Pre-Operation Phase

Pre-operation turns plans into a testable environment. In *ExperDF-Onto*, we document ScenarioType, EnvironmentSetup, Benchmark, PilotProject, TrainingActivity, and KnowledgeResourceCondition to support repeatability, as follows:

* **ScenarioType** *(why)* clarifies physical, virtual, or hybrid execution. **Instance:** ST\_Virtualized.
* **EnvironmentSetup** *(why)* records concrete configuration. **Instance:** ES\_3VMs with items {Win10\_VM1, Win11\_VM2, Ubuntu\_VM3}.
* **Benchmark** *(why)* yields baselines for time and integrity. **Instance:** BM\_DumpTime\_SHA256.
* **PilotProject** *(why)* de-risks execution and calibrates parameters. **Instance:** PP\_TrialCapture\_OK.
* **TrainingActivity** *(why)* ensures operator competence. **Instance:** TA\_4h\_Workshop.
* **KnowledgeResourceCondition** *(why)* anchors configuration in vendor truth. **Instance:** KRC\_VendorAPIs.

The following relations are used: ES\_3VMs implements Scenario ST\_Virtualized; BM\_DumpTime\_SHA256 benchmarks ES\_3VMs; PP\_TrialCapture\_OK validates ES\_3VMs; TA\_4h\_Workshop prepares Participant Analyst\_01.

The pre-operation phase explains to future replicators not only *what* was done but also *why* that environment was chosen, lowering ambiguity and boosting transferability.

## 8.4 Operation Phase

Operation is where evidence is produced. The ontology clarifies Participant, Instrument, Artifact, DataP (data properties and metadata), ActivityLog, and OperationProcedure so that every step is reproducible and auditable, as follows:

* **Participant** *(why)* identifies human roles. **Instances:** Analyst\_01, Assistant\_A.
* **Instrument** *(why)* records tools as first-class entities. **Instances:** Volatility\_v2.6, Rekall\_v1.7, Belkasoft\_LRC\_vX.
* **Artifact** *(why)* binds produced files to the process. **Instances:** RAM\_Win10\_ToolX\_Run01.dd, RAM\_Win11\_ToolY\_Run02.dd.
* **DataP** *(why)* preserves integrity and context. **Examples:** sha256=..., size=..., captureStart=..., captureEnd=....
* **ActivityLog** *(why)* creates a parallel, human-readable timeline. **Instance:** ALOG\_CSV\_VMR.
* **OperationProcedure** *(why)* structures actions. **Instance:** OP\_Capture\_Hash\_Verify\_Compare.

We then used the following relations: Analyst\_01 uses Instrument Volatility\_v2.6; Instrument Volatility\_v2.6 produced Artifact RAM\_Win10\_ToolX\_Run01.dd; Artifact RAM\_Win10\_ToolX\_Run01.dd hasDataProperty sha256=...; OperationProcedure OP\_Capture\_ Hash\_Verify\_Compare executedBy Analyst\_01; ActivityLog ALOG\_CSV\_ VMR records OperationProcedure OP\_Capture\_Hash\_Verify\_Compare.

As an operational checklist we:

* Verify hypervisor time with NTP snapshots before each run
* Record tool version and command-line parameters verbatim
* Hash immediately after acquisition and again after transfer
* Store logs and images on write-once or versioned storage

## 8.5 Analysis and Interpretation Phase

Analysis converts artifacts to evidence-supported claims. The ontology tracks ResultMetric, StatisticalAnalysis, InterpretationChallenge, ThreatsToValidity, and ReliabilityAnalysis. This ensures that findings are not only reported but justified, including limitations, as follows:

* **ResultMetric** *(why)* defines what “difference” means. **Instance:** RM\_MeanDeviationRecoveredProcesses.
* **StatisticalAnalysis** *(why)*: formal test. **Instance:** ANOVA\_p043.
* **InterpretationChallenge** *(why)*: explicit analytic friction. **Instance:** IC\_OS\_Caching\_Variance.
* **ThreatsToValidity** *(why)* maps to accepted taxonomy. **Instance:** TV\_Construct\_ToolSemanticDifferences.
* **ReliabilityAnalysis** *(why)* quantifies repeatability. **Instance:** Rel\_Corr\_096.

The following relations are used: ResultMetric RM\_MeanDeviationRecoveredProcesses computedFrom Artifacts {RAM\_...}; StatisticalAnalysis ANOVA\_p043 tests Hypothesis H0\_no\_tool\_effect; ReliabilityAnalysis Rel\_Corr\_096 evaluates ResultMetric RM\_...; InterpretationChallenge IC\_OS\_Caching\_Variance impacts ResultInterpretation; ThreatsToValidity TV\_Construct\_ToolSemanticDifferences threatens ValidityOfConclusions.

Writing down InterpretationChallenge and ThreatsToValidity is not cosmetic. It tells readers exactly where uncertainty lies and how far they should trust the generalization.

## 8.6 Dissemination Phase

Dissemination turns a private analysis into a public, reusable asset. In *ExperDF-Onto*, we instantiate DisseminationPlan, Dataset, DatasetMetadata, Authorship, TechnicalReview, and PresentationQuality with links to persistent identifiers, such as:

* **DisseminationPlan** *(why)* sets channels, embargoes, and identifiers. **Instance:** DP\_Zenodo\_Release.
* **Dataset** *(why)* bundles images, logs, code, and documentation. **Instance:** DS\_VMR\_1.0.
* **DatasetMetadata** *(why)* improves discovery and reuse. **Instance:** DC\_JSONLD\_VMR.
* **Authorship** *(why)* credits contributors and roles. **Instance:** AUTH\_Mendes\_Silva.
* **TechnicalReview** *(why)*: independent scrutiny. **Instance:** TR\_SeniorValidation\_2025.
* **PresentationQuality** *(why)* ensures clarity for new users. **Instance:** PQ\_Slides\_Notebook.

The following relations are used: Dataset DS\_VMR\_1.0 describedBy DatasetMetadata DC\_JSONLD\_VMR; DisseminationPlan DP\_Zenodo\_Release publishes Dataset DS\_VMR\_1.0; Authorship AUTH\_Mendes\_Silva credits Experiment Exp\_VM\_Reproducibility; TechnicalReview TR\_SeniorValidation\_2025 assesses Dataset DS\_VMR\_1.0.

## 8.7 Ontological Instantiation Snapshot

Table [8.1](#Tab1) shows the ontological instantiations for this example.

Table 8.1

Ontological instantiations for “The Memory That Wouldn’t Lie”

| Ontology element | Example instance |
| --- | --- |
| Experiment | Exp\_VM\_Reproducibility |
| ResearchQuestion | RQ\_tool\_equivalence |
| Hypothesis | H0\_no\_tool\_effect; H1\_tool\_effect |
| IndependentVariable | IV\_AcquisitionTool {Volatility, Rekall, Belkasoft} |
| DependentVariable | DV\_RecoveredProcesses; DV\_OpenPorts; DV\_Handles |
| ControlVariable | CV\_OSVersion; CV\_MemSize; CV\_BackgroundLoad |
| ConfoundingFactor | CF\_TimestampDrift; CF\_HypervisorCaching |
| ScenarioType | ST\_Virtualized |
| EnvironmentSetup | ES\_3VMs {Win10\_VM1; Win11\_VM2; Ubuntu\_VM3} |
| Benchmark | BM\_DumpTime\_SHA256 |
| PilotProject | PP\_TrialCapture\_OK |
| TrainingActivity | TA\_4h\_Workshop |
| Instrument | Volatility\_v2.6; Rekall\_v1.7; Belkasoft\_LRC\_vX |
| Artifact | RAM\_Win10\_ToolX\_Run01.dd; RAM\_Win11\_ToolY\_Run02.dd |
| DataP | sha256; size; captureStart; captureEnd |
| ActivityLog | ALOG\_CSV\_VMR |
| OperationProcedure | OP\_Capture\_Hash\_Verify\_Compare |
| ResultMetric | RM\_MeanDeviationRecoveredProcesses |
| StatisticalAnalysis | ANOVA\_p043 |
| InterpretationChallenge | IC\_OS\_Caching\_Variance |
| ThreatsToValidity | TV\_Construct\_ToolSemanticDifferences |
| ReliabilityAnalysis | Rel\_Corr\_096 |
| DisseminationPlan | DP\_Zenodo\_Release |
| Dataset | DS\_VMR\_1.0 |
| DatasetMetadata | DC\_JSONLD\_VMR |
| Authorship | AUTH\_Mendes\_Silva |
| TechnicalReview | TR\_SeniorValidation\_2025 |
| PresentationQuality | PQ\_Slides\_Notebook |

## 8.8 Querying the Instantiation

The following query lists artifacts produced by Volatility and their integrity hashes. It demonstrates how the ontology enables transparent retrieval of provenance information.

Listing 8.1 SPARQL: retrieve artifacts produced by Volatility with hashes

![A query written to select artifact identifiers and their SHA values from a dataset where the instrument is labeled "Volatility_v2.6." It specifies that the instrument is of type Instrument, the artifact is produced by this instrument and has a data property with the key "sha256," whose value is the SHA hash. The query links these elements to retrieve the artifact and its corresponding SHA256 hash value.](../images/624027_1_En_8_Chapter/624027_1_En_8_Figaaa_HTML.png)

## 8.9 Coverage and Missing Elements

**Coverage:** 34 out of 50 ontology classes were instantiated, achieving approximately 68% conceptual completeness.

**Missing elements:** *Governance*, *Stakeholder*, *PeerReview*, and *ConfigurationManagement* remain unmodeled in this instance.

This level of coverage indicates that the instantiation successfully represents most of the experimental, operational, and analytical dimensions defined by *ExperDF-Onto* but does not yet encompass higher order organizational and validation constructs. The absence of *Governance* elements means that decision-making and oversight mechanisms were not explicitly modeled. Excluding *Stakeholder* entities omits representation of the broader community affected by or contributing to the experiment. The lack of *PeerReview* elements limits formal modeling of external evaluation and quality assurance, while the missing *ConfigurationManagement* prevents traceability of software or dataset versions across replications. Incorporating these classes in future instantiations would advance the model’s maturity, enhancing accountability, reproducibility, and alignment with open science and institutional governance practices.

Why are these elements missing and how to add them:

* **Governance** *(gap)*: no formal data stewardship or policy entities. *Add:* DataSteward\_Lab, Policy\_Retention\_3y.
* **Stakeholder** *(gap)*: no external beneficiaries or requesters modeled. *Add:* Stakeholder\_IRTeam, Stakeholder\_CourtExpert.
* **PeerReview** *(gap)*: technical validation recorded but not peer review. *Add:* PR\_ExternalReviewer\_Report.
* **ConfigurationManagement** *(gap)*: versions tracked informally. *Add:* Cfg\_Dataset\_v1.0, Cfg\_ToolingEnv\_commit\_abc123.

Adding these four branches would likely raise coverage to about 80 percent while improving trust and long-term reusability.

## 8.10 Interpretation and Teaching Notes

This section provides interpretive and pedagogical insights into the experiment, explaining the meaning of its statistical outcomes, how the study can be replicated or extended, and what conceptual lessons it offers for teaching controlled experimentation in Digital Forensics. Each subsection highlights a specific aspect of how *ExperDF-Onto* supports transparency, reproducibility, and critical reflection on experimental findings.

### 8.10.1 What the Results Mean

The ANOVA result p = 0.43 suggests no statistically significant tool effect on recovered process counts under the tested conditions. Reliability at 0.96 indicates stable acquisition within this configuration, confirming that the experiment’s internal validity is strong despite nonsignificant group differences.

### 8.10.2 How to Reuse This Study

Because the scenario, instruments, parameters, and hashes are modeled explicitly, a reader can rerun the exact workflow or adapt it by substituting a new tool version while preserving the same IndependentVariable structure. This modularity demonstrates how ontological modeling facilitates both replication and controlled variation, supporting cumulative empirical research.

### 8.10.3 Common Misconceptions Clarified

* *Equivalence is not identity.* Even if outcomes are statistically similar, tools may differ semantically. This is captured by TV\_Construct\_ToolSemanticDifferences.
* *No effect here does not mean no effect anywhere.* External validity depends on the modeled ScenarioType, ControlVariables, and ConfoundingFactors.

### 8.10.4 Minimal Reproducibility Kit

At a minimum, a replicator needs: VM images or build scripts, tool versions and parameters, acquisition logs, artifact hashes, and the dataset metadata record. All these are explicit instances and relations in *ExperDF-Onto*, allowing others to verify results, compare tools, or build derivative studies with confidence in methodological integrity.

## 8.11 Final Remarks

This chapter illustrated how *ExperDF-Onto* can be instantiated to model a complete controlled experiment in digital forensics, from conceptual planning to dissemination. By decomposing each research phase into explicit ontological elements, the model transforms narrative experimental descriptions into machine-readable structures that preserve rigor, traceability, and interpretability.

Through the instantiation steps and the resulting queries, readers can observe how experimental entities such as instruments, artifacts, variables, and results are semantically connected to form a transparent and auditable research chain. These relationships strengthen internal validity and establish a foundation for reproducibility and reuse across future studies.

Pedagogically, this chapter serves as a blueprint for how students and practitioners can document and reason about their own experiments using an ontological framework. Conceptually, it reinforces the idea that reproducibility and provenance are not post hoc annotations but integral parts of the research design. The explicit modeling of assumptions, procedures, and metrics exemplifies how ontology-driven experimentation contributes to a cumulative and open body of forensic knowledge.

Future work may extend this model by integrating governance, stakeholder participation, and automated peer review processes, creating a pathway toward a fully open and FAIR-aligned digital forensics ecosystem. In doing so, *ExperDF-Onto* not only supports reproducible research but also promotes institutional transparency and societal accountability in the production and evaluation of digital evidence.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_9>

# 9. Example 2: Unlocking the Locked—Smartphone Bypass Experiments

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter details a controlled empirical investigation on smartphone data extraction reliability and legal defensibility, focusing on the comparative performance of forensic tools across locked Android and iOS devices. The experiment explored how different extraction vectors, such as logical, file system, and after-first-unlock (AFU) exploit methods, perform when applied under lawful authority to modern encrypted devices equipped with secure enclaves and full-disk encryption. Using the *ExperDF-Onto* framework, every experimental element was modeled to ensure traceability, ethical transparency, and replicability across jurisdictions. The planning phase defined explicit hypotheses, independent and dependent variables, and legal and ethical planning constructs that captured the obligations of privacy legislation, including GDPR and LGPD. Pre-operation activities established reproducible benches for Android and iOS, documented firmware and baseband states, and validated tool performance through pilot extractions. During operation, each participant, instrument, artifact, and activity log was instantiated as an ontological entity, capturing provenance links between procedures, generated data, and contextual parameters such as passcode complexity, firmware patch levels, and secure-element behavior. Statistical analysis of the resulting datasets showed that Android devices achieved an average logical extraction success rate of 78 percent. In comparison, iOS devices averaged 42 percent under the same constraints, yielding a statistically significant difference (*p* < 0.05) according to chi-square testing. Reliability across repeated runs reached 0.94, indicating strong procedural stability. The study also modeled legal boundaries and data sharing constraints as ontological relations, providing machine-interpretable documentation of compliance and interpretive limits. All extraction images, metadata, and logs were curated into an open dataset with persistent identifiers to enable auditability and future replication. Beyond the quantitative findings, this chapter demonstrates how *ExperDF-Onto* integrates legal, ethical, and technical dimensions of digital forensics into a unified semantic structure, turning a complex investigative procedure into a transparent, reusable, and verifiable scientific contribution.

## 9.1 Context and Motivation

Modern smartphones are cryptographic vaults. Security features such as secure enclaves, full-disk encryption, hardware-backed keystores, and rate-limited unlock attempts protect user privacy but complicate lawful investigations. The researchers designed a controlled study to answer a practical question for incident responders and lab examiners: *How reliably can state-of-the-practice extraction methods recover data from locked Android and iOS devices under lawful authority?*

This example shows how *ExperDF-Onto* makes each decision auditable, from ethics and legal framing to tool choice, scenario construction, and statistical testing. It also demonstrates how to model privacy constraints and firmware variability as first-class ontological elements that affect interpretation and reuse.

We move from a plain-language research plan to a fully instantiated ontological representation. At each phase, we explain why the concept matters, how it is instantiated, the relations that connect it to other entities, and the common pitfalls the ontology helps prevent.

## 9.2 Planning Phase

In *ExperDF-Onto*, the planning constructs translate a high-level concern into a testable structure. We instantiate Experiment, ResearchQuestion, Hypothesis, variables, ethical and legal planning, and replication commitments and then bind them through explicit relations as follows:

* **Experiment** *(why)* anchors identity, scope, and intent. **Instance:** Exp\_SmartphoneBypass.
* **ResearchQuestion** *(why)* focuses uncertainty into measurable terms. **Instance:** RQ\_ExtractionSuccess\_AndroidVsIOS.
* **Hypothesis** *(why)* states expected patterns. **Instances:** H0\_NoDiff\_AndroidIOS and H1\_AndroidHigherSuccess.
* **IndependentVariable** *(why)*: manipulated factors. **Instances:** IV\_OSType with levels {Android, iOS}; IV\_AttackVector with levels {Logical, FileSystem, AFU\_Exploit}.
* **DependentVariable** *(why)*: measurable outcomes. **Instances:** DV\_AccessSuccessRate, DV\_DataExposureCoverage.
* **ControlVariable** *(why)* holds noise constant. **Instances:** CV\_DeviceModelBand, CV\_OSMinorVersion, CV\_PasscodeComplexity, CV\_TimeSinceLastUnlock.
* **ConfoundingFactor** *(why)* documents influences we cannot fully control. **Instances:** CF\_FirmwarePatchLevelDrift, CF\_BasebandDifferences, CF\_SecureElementBehavior.
* **EthicalPlanning** *(why)* asserts privacy-protective constraints. **Instance:** EP\_MockProfilesOnly with synthetic contacts, messages, and media.
* **LegalPlanning** *(why)* situates the study within applicable law and policy. **Instance:** LP\_GDPR\_LGPD\_Compliance with retention and minimization rules.
* **ReplicationPlanning** *(why)* commits to transparency pre-results. **Instance:** RP\_OSF\_Prereg\_SBE.

We used the following relations: Exp\_SmartphoneBypass hasResearchQuestion RQ\_ExtractionSuccess\_AndroidVsIOS; Exp\_SmartphoneBypass hasHypothesis H1\_AndroidHigherSuccess; Exp\_SmartphoneBypass hasIndependentVariable IV\_OSType, IV\_AttackVector; Exp\_SmartphoneBypass hasDependentVariable DV\_AccessSuccessRate, DV\_DataExposureCoverage; Exp\_SmartphoneBypass isControlledBy CV\_DeviceModelBand, CV\_OSMinorVersion, CV\_PasscodeComplexity; Exp\_SmartphoneBypass considersConfounding CF\_FirmwarePatchLevelDrift; Exp\_SmartphoneBypass compliesWith LP\_GDPR\_LGPD\_Compliance; Exp\_SmartphoneBypass preregisteredAs RP\_OSF\_Prereg\_SBE.

Typical pitfalls and how the ontology prevents them:

* *Pitfall:* forgetting that success rates vary by attack vector. *Prevention:* IV\_AttackVector is modeled explicitly with levels.
* *Pitfall:* mixing firmware and device models without documenting them. *Prevention:* CV\_DeviceModelBand and CV\_OSMinorVersion force explicit capture.
* *Pitfall:* ambiguous legal footing. *Prevention:* LegalPlanning and retention constraints are first-class entities.

## 9.3 Pre-Operation Phase

Pre-operation encodes the practical conditions for repeatability: scenarios, benches, pilots, training, and baselines. These entities make the path from plan to execution auditable, as follows:

* **ScenarioType** *(why)* clarifies hybrid execution. **Instance:** ST\_Hybrid\_PhysicalEmulated.
* **EnvironmentSetup** *(why)* enumerates benches and configurations. **Instances:** ES\_AndroidBench\_A1 and ES\_iOSBench\_I1 with device pools, SIM states, and passcode policies.
* **Benchmark** *(why)* establishes performance and integrity baselines. **Instance:** BM\_HashValidation\_SpeedProfile.
* **PilotProject** *(why)* validates feasibility and scripts. **Instance:** PP\_PrelimExtractions\_OK.
* **TrainingActivity** *(why)* certifies operator skill. **Instance:** TA\_ToolCertification\_8h.
* **KnowledgeResourceCondition** *(why)*: ties setup to tool docs and vendor advisories. **Instance:** KRC\_VendorDocs\_UFED\_AXIOM.

We used the following relations: ES\_AndroidBench\_A1 implements ST\_Hybrid\_PhysicalEmulated; BM\_HashValidation\_SpeedProfile benchmarks ES\_AndroidBench\_A1, ES\_iOSBench\_I1; PP\_PrelimExtractions\_OK validates EnvironmentSetup {ES\_AndroidBench\_A1, ES\_iOSBench\_I1}; TA\_ToolCertification\_8h prepares Participant PriyaD\_Lead and Assistant\_Team.

The benches are not mere labels. They are ontological objects with members and policies, enabling future researchers to reconstruct conditions and understand divergence.

## 9.4 Operation Phase

Evidence production is modeled through participants, instruments, artifacts, logs, and prespecified procedures. This phase also captures failure modes as first-class citizens, such as:

* **Participant** *(why)* identifies roles and accountability. **Instances:** PriyaD\_Lead, Assistant\_A, Assistant\_B.
* **Instrument** *(why)* records tools and versions. **Instances:** UFED\_vX.Y, AXIOM\_vZ.W, Autopsy\_v4.X.
* **Artifact** *(why)* binds extractions and logs to the process. **Examples:** IMG\_Android\_Pixel4a\_Run03.dd, IMG\_iOS\_iPhone11\_Run05.dd, LOG\_API\_AXIOM\_Run05.csv.
* **DataP** *(why)* preserves integrity and context. **Examples:** sha256, captureStart, captureEnd, toolParams.
* **ActivityLog** *(why)*: human-readable timeline. **Instance:** ALOG\_SmartphoneBypass.csv.
* **OperationProcedure** *(why)* constrains sequence for comparability. **Instance:** OP\_Enumerate\_Extract\_Hash\_Verify\_Parse.
* **IncidentReport** *(why)* captures anomalies and failures. **Instance:** IR\_FirmwareFailure\_2Events with details for retries and device IDs.

We used these relations: PriyaD\_Lead uses Instrument UFED\_vX.Y; Instrument AXIOM\_vZ.W produced Artifact IMG\_iOS\_iPhone11\_Run05.dd; Artifact IMG\_iOS\_iPhone11\_Run05.dd hasDataProperty sha256=... and toolParams="logical"; OperationProcedure OP\_Enumerate\_Extract\_Hash\_Verify\_Parse executedBy PriyaD\_Lead; ActivityLog ALOG\_SmartphoneBypass.csv records OperationProcedure OP\_...; IncidentReport IR\_FirmwareFailure\_2Events relatesTo Instrument UFED\_vX.Y and Device iPhone11.

As an operational checklist, we:

* Snapshot the exact firmware and baseband versions before extraction
* Record passcode policy, secure enclave state, and last-unlock time as ControlVariable values
* Hash the extracted image immediately; rehash after transfer and after parsing
* Capture full tool parameter strings for every attempt and retry

## 9.5 Analysis and Interpretation Phase

We formalize metrics and tests, while documenting legal and interpretive constraints that affect generalization, as follows:

* **ResultMetric** *(why)* defines success quantitatively. **Instances:** RM\_AndroidSuccess\_0.78, RM\_iOSSuccess\_0.42, RM\_ExposureCoverage\_perProfile.
* **StatisticalAnalysis** *(why)* validates differences. **Instance:** ChiSquare\_pLT0\_05 comparing success counts per OS.
* **ThreatsToValidity** *(why)* frames inference limits. **Instances:** TV\_EncryptionVariance, TV\_OSUpdateCadence, TV\_DeviceHeterogeneity.
* **ReliabilityAnalysis** *(why)* measures repeatability. **Instance:** Rel\_r0\_94.
* **InterpretationChallenge** *(why)* notes analysis friction. **Instance:** IC\_SparseArtifacts\_PostParse.
* **ConflictLaw** *(why)* clarifies jurisdictional limits. **Instance:** CL\_PrivacyBoundaries\_EU\_BR.

We then used these relations: ResultMetric RM\_AndroidSuccess\_0.78 computedFrom Artifacts {IMG\_Android\_...}; StatisticalAnalysis ChiSquare\_pLT0\_05 tests Hypothesis H1\_AndroidHigherSuccess; ReliabilityAnalysis Rel\_r0\_94 evaluates ResultMetric RM\_...; ThreatsToValidity TV\_EncryptionVariance threatens ValidityOfConclusions; ConflictLaw CL\_PrivacyBoundaries\_EU\_BR constrains DataSharing and Interpretation.

The ontology separates *what happened* (artifacts, logs) from *what it means* (metrics, tests, threats). This separation helps downstream users adapt the pipeline while preserving the original inference boundaries.

## 9.6 Dissemination Phase

Dissemination converts local findings into global, reusable assets with provenance and credit. Governance elements are partially present here and can be expanded, such as:

* **DisseminationPlan** *(why)* defines venue, identifiers, and embargo. **Instance:** DP\_Zenodo\_10\_5281\_zenodo\_1234567.
* **Dataset** *(why)* bundles images, logs, and parsing outputs. **Instance:** DS\_SBE\_1\_0.
* **DatasetMetadata** *(why)* enables discovery and reuse. **Instance:** MD\_JSONLD\_SBE.
* **Authorship** *(why)* acknowledges roles. **Instance:** AUTH\_Deshmukh\_Team.
* **TechnicalReview** *(why)*: lab supervisor validation. **Instance:** TR\_Supervisor\_2025.
* **ImpactAssessment** *(why)* documents training adoption. **Instance:** IA\_CurriculumIntegration\_2025.

We used the following relations: Dataset DS\_SBE\_1\_0 describedBy MD\_JSONLD\_SBE; DisseminationPlan DP\_Zenodo\_10\_5281\_... publishes Dataset DS\_SBE\_1\_0; Authorship AUTH\_Deshmukh\_Team credits Experiment Exp\_SmartphoneBypass; TechnicalReview TR\_Supervisor\_2025 assesses DS\_SBE\_1\_0; ImpactAssessment IA\_CurriculumIntegration\_2025 references AdoptionEvents in TrainingPrograms.

## 9.7 Ontological Instantiation Snapshot

Table [9.1](#Tab1) shows the ontological instantiations for this example.

Table 9.1

Ontological instantiations for “Unlocking the Locked—Smartphone Bypass Experiments”

| Ontology element | Example instance |
| --- | --- |
| Experiment | Exp\_SmartphoneBypass |
| ResearchQuestion | RQ\_ExtractionSuccess\_AndroidVsIOS |
| Hypothesis | H0\_NoDiff\_AndroidIOS; H1\_AndroidHigherSuccess |
| IndependentVariable | IV\_OSType {Android, iOS}; IV\_AttackVector {Logical, FileSystem, AFU\_Exploit} |
| DependentVariable | DV\_AccessSuccessRate; DV\_DataExposureCoverage |
| ControlVariable | CV\_DeviceModelBand; CV\_OSMinorVersion; CV\_PasscodeComplexity; CV\_TimeSinceLastUnlock |
| ConfoundingFactor | CF\_FirmwarePatchLevelDrift; CF\_BasebandDifferences; CF\_SecureElementBehavior |
| LegalPlanning | LP\_GDPR\_LGPD\_Compliance |
| EthicalPlanning | EP\_MockProfilesOnly |
| ReplicationPlanning | RP\_OSF\_Prereg\_SBE |
| ScenarioType | ST\_Hybrid\_PhysicalEmulated |
| EnvironmentSetup | ES\_AndroidBench\_A1; ES\_iOSBench\_I1 |
| Benchmark | BM\_HashValidation\_SpeedProfile |
| PilotProject | PP\_PrelimExtractions\_OK |
| TrainingActivity | TA\_ToolCertification\_8h |
| Instrument | UFED\_vX.Y; AXIOM\_vZ.W; Autopsy\_v4.X |
| Artifact | IMG\_Android\_Pixel4a\_Run03.dd; IMG\_iOS\_iPhone11\_Run05.dd; LOG\_API\_AXIOM\_Run05.csv |
| DataP | sha256; captureStart; captureEnd; toolParams |
| ActivityLog | ALOG\_SmartphoneBypass.csv |
| OperationProcedure | OP\_Enumerate\_Extract\_Hash\_Verify\_Parse |
| IncidentReport | IR\_FirmwareFailure\_2Events |
| ResultMetric | RM\_AndroidSuccess\_0.78; RM\_iOSSuccess\_0.42; RM\_ExposureCoverage\_perProfile |
| StatisticalAnalysis | ChiSquare\_pLT0\_05 |
| ThreatsToValidity | TV\_EncryptionVariance; TV\_OSUpdateCadence; TV\_DeviceHeterogeneity |
| ReliabilityAnalysis | Rel\_r0\_94 |
| InterpretationChallenge | IC\_SparseArtifacts\_PostParse |
| ConflictLaw | CL\_PrivacyBoundaries\_EU\_BR |
| DisseminationPlan | DP\_Zenodo\_10\_5281\_zenodo\_1234567 |
| Dataset | DS\_SBE\_1\_0 |
| DatasetMetadata | MD\_JSONLD\_SBE |
| Authorship | AUTH\_Deshmukh\_Team |
| TechnicalReview | TR\_Supervisor\_2025 |
| ImpactAssessment | IA\_CurriculumIntegration\_2025 |

## 9.8 Querying the Instantiation

The following SPARQL illustrates how to retrieve all iOS artifacts produced via logical extraction, with their hashes and benches. It demonstrates evidence traceability across instruments, scenarios, and integrity properties.

Listing 9.1 SPARQL: iOS logical extractions with integrity and bench

![A code snippet written in SPARQL language that queries artifacts produced by instruments used on the iOS operating system with a logical attack vector. It selects artifact identifiers, their SHA-256 hash values, and the bench they belong to. The query links artifacts to instruments and filters data properties with the key "sha256" to retrieve corresponding hash values. This helps identify and analyze specific artifacts related to iOS security testing.](../images/624027_1_En_9_Chapter/624027_1_En_9_Figaaa_HTML.png)

## 9.9 Coverage and Missing Elements

**Coverage:** 38 of 52 ontology classes instantiated (73%).

**Missing:** *OntologyReuse*, *Stakeholder*, *PeerReview*, *Maintenance*.

The experiment achieved a coverage of 38 out of 52 ontology classes, representing approximately 73 percent of the available conceptual elements in *ExperDF-Onto*. This level of coverage indicates that the experiment modeled most of the critical phases of a controlled study, including planning, operation, and analysis, with sufficient detail to support reproducibility and reasoning. The missing classes reflect higher level organizational and community aspects that were not directly applicable to the immediate experimental setup. *OntologyReuse* was not instantiated because no external ontologies were referenced for interoperability. *Stakeholder* was omitted since the study did not explicitly identify external user groups or beneficiaries. *PeerReview* was absent because formal external evaluation of the experimental process had not yet occurred. Finally, *Maintenance* was not represented, as no long-term update or life cycle management process was modeled for the dataset or associated tools. Including these missing elements in future extensions would improve completeness and enhance alignment with open science governance and sustainability practices.

Why are these elements missing, and how to add them:

* **OntologyReuse** *(gap)*: no explicit alignment to external vocabularies. *Add:* mappings to Dublin Core for metadata, PROV-O for provenance, and SSN/SOSA for device observations where applicable.
* **Stakeholder** *(gap)*: external beneficiaries or requesters not modeled. *Add:* Stakeholder\_LEAgency, Stakeholder\_JudicialOfficer, Stakeholder\_DefenceExpert.
* **PeerReview** *(gap)*: technical review exists, but no external peer review artifacts. *Add:* PR\_ExternalReviewer\_Report\_ID123.
* **Maintenance** *(gap)*: dataset and code evolution not captured. *Add:* Maint\_DatasetRoadmap, Maint\_Changelog\_DS\_SBE\_1\_1, Maint\_DeprecationPolicy.

Adding these branches would likely raise completeness toward 90 percent while improving interoperability, stakeholder transparency, and long-term stewardship.

## 9.10 Interpretation and Teaching Notes

This section synthesizes the analytical results of the smartphone bypass experiment and guides interpretation, reuse, and pedagogical application. Each subsection highlights a different dimension of the ontological modeling process, helping readers understand not only what the findings mean but also how to extend and replicate the study responsibly. Together, these notes bridge empirical evidence and didactic use, reinforcing the principles of transparency, reproducibility, and ethical conduct in digital forensics experimentation.

### 9.10.1 What the Results Mean

The chi-square result (p<0.05) indicates a statistically significant difference in extraction success between Android and iOS for the tested devices, benches, and vectors. The reported 78 percent versus 42 percent success rates are conditional on the modeled ControlVariables, firmware levels, and bench composition. These results show that success variability depends as much on contextual parameters as on tool capability, underscoring the importance of modeling all influencing factors explicitly within *ExperDF-Onto*.

### 9.10.2 How to Reuse This Study

Because benches, devices, passcode policies, and tool parameters are represented as explicit ontological instances linked through formal relations, a replicator can rerun the workflow or substitute a new firmware cohort while maintaining conceptual comparability. Legal and ethical constraints are modeled as distinct entities, allowing the study to be adapted to different jurisdictions without compromising compliance or methodological rigor.

### 9.10.3 Common Misconceptions Clarified

* *Higher logical success on Android does not imply weaker security.* It reflects specific device cohorts, firmware states, and vectors tested, all of which are explicitly modeled within the ontology.
* *A failed full-disk image is not the end.* The ontology differentiates among multiple attack vectors, ensuring that alternative lawful acquisition methods can still yield partial or corroborative evidence.

### 9.10.4 Minimal Reproducibility Kit

To achieve full reproducibility, a replicator requires bench manifests, device and firmware inventories, complete tool parameter strings, extraction logs, artifact hashes, parsing outputs, and JSON-LD metadata. Each of these components appears as an ontological instance and is queryable through the semantic relations defined in *ExperDF-Onto*, ensuring verifiability, reuse, and transparent documentation of the experimental process.

## 9.11 Final Remarks

This chapter illustrated how *ExperDF-Onto* supports the formalization of a controlled experiment in mobile forensics, centered on lock-screen bypass and data extraction success across heterogeneous smartphone platforms. By decomposing the study into ontological elements such as devices, benches, passcode policies, and extraction tools, the model transformed an operationally complex investigation into a structured representation that emphasizes traceability and interpretability.

The resulting instantiation revealed how operating system versions, attack vectors, and ethical, as well as legal considerations, interact to shape empirical outcomes. Through explicit modeling of these dependencies, the ontology helps distinguish between what is technically feasible and what is legally and ethically defensible. This approach reinforces the role of structured provenance and metadata in improving the transparency and accountability of digital forensic investigations.

From an educational perspective, the chapter demonstrated how ontologies can guide learners and practitioners in documenting sensitive procedures. Explicit representation of variables, instruments, and outcomes helps reduce ambiguity and facilitates replication, comparison, and continuous learning in a controlled and verifiable way.

Future refinements may include incorporating stakeholder perspectives, standardized quality evaluation, and peer review representations to strengthen alignment with open science and long-term sustainability practices. In doing so, *ExperDF-Onto* continues to advance methodological rigor and reinforce trust in the reproducibility of mobile forensic research.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_10>

# 10. Example 3: The Case of the Altered Cloud Logs

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter presents a controlled study of integrity verification for cloud infrastructure logs in multitenant environments, modeling the entire investigation with *ExperDF-Onto* to make design choices, provenance, and limitations transparently auditable. The experiment asks whether a tamper-evident hash-chaining approach can reliably expose micro-edits, line drops, insertions, and reordering across heterogeneous provider logging frameworks without privileged access to underlying storage. The planning phase formalizes hypotheses, independent variables for provider and tamper type, dependent variables for detection rate, false positives, and time to detection, along with control variables that bound event rate, region count, key rotation, and clock drift. The pre-operation phase constructs a distributed virtual scenario spanning multiple regions and providers, captures latency benchmarks, and prepares operators through credential isolation drills, while linking assumptions to provider security documentation as explicit knowledge resources. During operation, log snapshots, per-event hashes, chain indexes, and intervention events are instantiated as first-class ontological entities with version lineage and activity logs, enabling precise reconstruction of the pipeline and its outputs. Analysis quantifies performance with detection success near 98 percent and false positives near 1 percent under a monotonic ingestion discipline, compares providers and tamper types with formal statistical tests, and records interpretation challenges such as nondeterministic ordering and threats to validity induced by replication delay, batching, and normalization policies. Dissemination packages snapshots, chain indexes, scripts, and machine-readable metadata using PROV-C and Dublin Core into an openly citable dataset to support independent verification and reuse. Beyond its empirical findings, the chapter demonstrates how *ExperDF-Onto* encodes distributed context, provider heterogeneity, and integrity guarantees into a coherent semantic structure, allowing investigators to query provenance, reason about timing effects, and generalize results responsibly across cloud settings.

## 10.1 Context and Motivation

Cloud infrastructures generate vast volumes of operational logs across microservices, regions, and tenants. These logs support security monitoring, billing, compliance, and incident response. However, multi-tenant replication, eventual consistency, and role-based access may create opportunities for subtle manipulation. The researchers set out to test a focused question: *Can a tamper-evident hash-chaining scheme reliably expose micro-edits and line reordering in provider logs without privileged access to underlying storage?*

This example shows how *ExperDF-Onto* captures distributed context, provider heterogeneity, and provenance guarantees. It demonstrates how log snapshots, event-level hashes, and version links become first-class entities so that investigators can reconstruct evidence and reason about integrity at scale.

We translate a narrative cloud-tampering scenario into an ontological instantiation that a reader can query. At each phase, we explain why a concept matters, how it is instantiated, and which relations connect it to a broader chain of custody.

## 10.2 Planning Phase

The planning layer frames integrity as a measurable outcome under provider diversity. We instantiate the core experimental design, variables, and reproducibility commitments, as follows:

* **Experiment***(why)* anchors the identity of the study. **Instance:** Exp\_CloudLogIntegrity.
* **ResearchQuestion***(why)* operationalizes uncertainty. **Instance:** RQ\_HashChainDetectsMicroTamper.
* **Hypothesis***(why)*: expected capability of the method. **Instances:** H0\_NoBetterThanChance and H1\_HighDetectionRate.
* **IndependentVariable***(why)*: manipulated factors. **Instances:** IV\_LoggingFramework with levels {AWS\_CloudTrail, GCP\_CloudAuditLogs, Azure\_ActivityLog}; IV\_TamperType with levels {SingleCharEdit, LineDrop, LineInsert, SwapOrder}.
* **DependentVariable***(why)*: measurable outcomes. **Instances:** DV\_DetectionRate, DV\_FalsePositiveRate, DV\_TimeToDetection.
* **ControlVariable***(why)* holds variation constant. **Instances:** CV\_EventRate, CV\_RegionCount, CV\_KeyRotationInterval, CV\_ClockDriftBudget.
* **ConfoundingFactor***(why)* acknowledges influences we cannot fully control. **Instances:** CF\_CrossRegionReplicationDelay, CF\_QueueBatching, CF\_ProviderRedactionPolicies.
* **ReplicationPlanning***(why)* preserves transparency before results. **Instance:** RP\_GitHub\_Versioned\_Pipelines.

We used the following relations: Exp\_CloudLogIntegrity hasResearchQuestion RQ\_HashChainDetectsMicroTamper; Exp\_CloudLogIntegrity hasHypothesis H1\_HighDetectionRate; Exp\_CloudLogIntegrity hasIndependentVariable IV\_LoggingFramework, IV\_TamperType; Exp\_CloudLogIntegrity hasDependentVariable DV\_DetectionRate, DV\_FalsePositiveRate, DV\_TimeToDetection; Exp\_CloudLogIntegrity isControlledBy CV\_EventRate, CV\_RegionCount; Exp\_CloudLogIntegrity considersConfounding CF\_CrossRegionReplicationDelay; Exp\_CloudLogIntegrity preregisteredAs RP\_GitHub\_Versioned\_Pipelines.

Typical pitfalls and ontology safeguards:

* *Pitfall:* measuring only accuracy and ignoring false positives. *Safeguard:* explicit DV\_FalsePositiveRate.
* *Pitfall:* treating provider choice as a backdrop. *Safeguard:* IV\_LoggingFramework with explicit levels.
* *Pitfall:* ignoring clock skew and replication. *Safeguard:* ControlVariable and ConfoundingFactor for timing.

## 10.3 Pre-Operation Phase

Pre-operation creates a distributed testbed with repeatable timing baselines and least-privilege credentials, as:

* **ScenarioType***(why)* makes distribution explicit. **Instance:** ST\_DistributedVirtual.
* **EnvironmentSetup***(why)* enumerates providers, regions, and services. **Instance:** ES\_MultiCloud\_M1 with items {AWS\_us-east-1, GCP\_us-central1, Azure\_eastus}.
* **Benchmark***(why)* establishes latency and integrity baselines. **Instance:** BM\_LoggingLatency\_PerProvider and BM\_HMACThroughput.
* **TrainingActivity***(why)* reduces operator error in cloud IAM. **Instance:** TA\_CredentialIsolationDrill.
* **KnowledgeResourceCondition***(why)* pins assumptions to provider docs. **Instance:** KRC\_ProviderSecWhitepapers.

We used these relations: ES\_MultiCloud\_M1 implements ST\_DistributedVirtual;BM\_LoggingLatency\_PerProvider benchmarks ES\_MultiCloud\_M1;TA\_CredentialIsolationDrill prepares Participant MiguelF\_Lead and CloudOps\_Team;KRC\_ProviderSecWhitepapers documents EnvironmentSetup ES\_MultiCloud\_M1.

Explicit regional membership and IAM practices allow replicators to understand divergences caused by geography or roles, not just code.

## 10.4 Operation Phase

We produce evidence by chaining per-event hashes, snapshotting versions, and modeling tampering as interventions:

* **Participant***(why)*:roles and accountability. **Instances:**MiguelF\_Lead, CloudOps\_Team.
* **Instrument***(why)*:toolchain for hashing and capture.**Instances:**Python\_HashChainer\_v1.2,Collector\_CLI\_v0.9.
* **Artifact***(why)*:tangible evidence products.**Examples:**LOGSNAP\_AWS\_2025-06-02T10:00Z.jsonl,LOGSNAP\_GCP\_2025-06-02T10:00Z.jsonl,CHAIN\_INDEX\_AWS\_v3.json.
* **DataP***(why)*:integrity and context.**Examples:**sha256,prevHash,eventId, region, captureWindow.
* **ActivityLog***(why)*:time-aligned pipeline events.**Instance:**ALOG\_HashCompute\_PerEvent.csv.
* **OperationProcedure***(why)*:constrains sequence.**Instance:**OP\_Ingest\_Order\_Hash\_Chain\_Snapshot.
* **InterventionEvent***(why)*:first-class tampering attempts.**Instances:**IE\_SingleCharEdit\_AWS\_t1, IE\_LineDrop\_GCP\_t2, IE\_SwapOrder\_Azure\_t3.
* **Versioning***(why)*:capture lineage.**Relation:**hasParentVersion linking LOGSNAP\_\*\_v2 toLOGSNAP\_\*\_v1.

We used these relations: MiguelF\_Lead uses Instrument Python\_HashChainer\_v1.2; Instrument Collector\_CLI\_v0.9 produced Artifact LOGSNAP\_AWS\_2025-06-02T10:00Z.jsonl; Artifact LOGSNAP\_AWS\_...\_v2 hasParentVersion LOGSNAP\_AWS\_...\_v1; Artifact LOGSNAP\_AWS\_... hasDataProperty sha256=..., prevHash=..., eventId=...; InterventionEvent IE\_SwapOrder\_Azure\_t3 targets Artifact LOGSNAP\_Azure\_...; ActivityLog ALOG\_HashCompute\_PerEvent.csv records OperationProcedure OP\_Ingest\_Order\_Hash\_Chain\_Snapshot.

As operational checklist we provide:

* Enforce monotonic ingestion order per provider stream before chaining.
* Persist the chain index and snapshots to append-only storage.
* Record provider API request IDs to align with service-side telemetry.
* Recompute hashes after export to verify end-to-end integrity.

## 10.5 Analysis and Interpretation Phase

We evaluate whether the chain exposes edits and reordering, while acknowledging provider timing behavior:

* **ResultMetric** *(why)* quantifies integrity performance. **Instances:** RM\_DetectSuccess\_0.98, RM\_FalsePositive\_0.01, RM\_MedianDetectionTime\_1.3s.
* **StatisticalAnalysis** *(why)* compares providers and tamper types. **Instance:** ANOVA\_DetectionTime\_ByProvider and PostHoc\_Tukey.
* **ThreatsToValidity** *(why)*: limits of inference. **Instances:** TV\_CloudLatency, TV\_ReplicationDelay, TV\_ProviderNormalization.
* **InterpretationChallenge** *(why)*: analytic friction. **Instance:** IC\_NonDeterministicOrdering.
* **ReliabilityAnalysis** *(why)*: repeatability. **Instance:** Rel\_ConsistencyAcrossRuns\_0.97.
* **ConflictLaw** *(why)*: cross-border handling. **Instance:** CL\_JurisdictionalDataHandling.

We used the following relations: ResultMetric RM\_DetectSuccess\_0.98 computedFrom Artifacts {LOGSNAP\_\*}; ANOVA\_DetectionTime\_ByProvider tests differences across IV\_LoggingFramework levels; Rel\_ConsistencyAcrossRuns\_0.97 evaluates ResultMetric RM\_MedianDetectionTime\_1.3s; IC\_NonDeterministicOrdering impacts ResultInterpretation; TV\_ReplicationDelay threatens ValidityOfConclusions; CL\_JurisdictionalDataHandling constrains DataSharing and Retention.

The ontology separates integrity claims from timing behavior so that a future team can improve ordering heuristics while reusing the same chain-of-custody model.

## 10.6 Dissemination Phase

We publish artifacts and provenance in a way that others can verify without replicating the full cloud setup:

* **DisseminationPlan** *(why)* states venue and identifiers. **Instance:** DP\_OpenRepo\_WithDOIs.
* **Dataset** *(why)* bundles snapshots, chain indexes, and scripts. **Instance:** DS\_CloudLogs\_Integrity\_1\_0.
* **DatasetMetadata** *(why)*: provenance and discovery. **Instance:** MD\_PROV-C\_PlusDublinCore.
* **Authorship** *(why)*: credit and accountability. **Instance:** AUTH\_Ferreira\_Team.

The following relations were used: Dataset DS\_CloudLogs\_Integrity\_1\_0 describedBy MD\_PROV-C\_PlusDublinCore; DisseminationPlan DP\_OpenRepo\_WithDOIs publishes DS\_CloudLogs\_Integrity\_1\_0; Authorship AUTH\_Ferreira\_Team credits Experiment Exp\_CloudLogIntegrity.

## 10.7 Ontological Instantiation Snapshot

Table [10.1](#Tab1) shows the ontological instantiations for this example.

Table 10.1

Ontological instantiations for “The Case of the Altered Cloud Logs”

| Ontology Element | Example Instance |
| --- | --- |
| Experiment | Exp\_CloudLogIntegrity |
| ResearchQuestion | RQ\_HashChainDetectsMicroTamper |
| Hypothesis | H0\_NoBetterThanChance; H1\_HighDetectionRate |
| IndependentVariable | IV\_LoggingFramework {AWS, GCP, Azure}; IV\_TamperType {SingleCharEdit, LineDrop, LineInsert, SwapOrder} |
| DependentVariable | DV\_DetectionRate; DV\_FalsePositiveRate; DV\_TimeToDetection |
| ControlVariable | CV\_EventRate; CV\_RegionCount; CV\_KeyRotationInterval; CV\_ClockDriftBudget |
| ConfoundingFactor | CF\_CrossRegionReplicationDelay; CF\_QueueBatching; CF\_ProviderRedactionPolicies |
| ScenarioType | ST\_DistributedVirtual |
| EnvironmentSetup | ES\_MultiCloud\_M1 {AWS\_us-east-1; GCP\_us-central1; Azure\_eastus} |
| Benchmark | BM\_LoggingLatency\_PerProvider; BM\_HMACThroughput |
| TrainingActivity | TA\_CredentialIsolationDrill |
| Instrument | Python\_HashChainer\_v1.2; Collector\_CLI\_v0.9 |
| Artifact | LOGSNAP\_\* jsonl; CHAIN\_INDEX\_\*\_v3.json |
| DataP | sha256; prevHash; eventId; region; captureWindow |
| ActivityLog | ALOG\_HashCompute\_PerEvent.csv |
| OperationProcedure | OP\_Ingest\_Order\_Hash\_Chain\_Snapshot |
| InterventionEvent | IE\_SingleCharEdit\_AWS\_t1; IE\_LineDrop\_GCP\_t2; IE\_SwapOrder\_Azure\_t3 |
| ResultMetric | RM\_DetectSuccess\_0.98; RM\_FalsePositive\_0.01; RM\_MedianDetectionTime\_1.3s |
| StatisticalAnalysis | ANOVA\_DetectionTime\_ByProvider; PostHoc\_Tukey |
| ThreatsToValidity | TV\_CloudLatency; TV\_ReplicationDelay; TV\_ProviderNormalization |
| InterpretationChallenge | IC\_NonDeterministicOrdering |
| ReliabilityAnalysis | Rel\_ConsistencyAcrossRuns\_0.97 |
| ConflictLaw | CL\_JurisdictionalDataHandling |
| DisseminationPlan | DP\_OpenRepo\_WithDOIs |
| Dataset | DS\_CloudLogs\_Integrity\_1\_0 |
| DatasetMetadata | MD\_PROV-C\_PlusDublinCore |
| Authorship | AUTH\_Ferreira\_Team |

## 10.8 Querying the Instantiation

The following SPARQL retrieves all artifacts where a SwapOrder intervention occurred and shows the breaking point in the chain by reporting both the stored prevHash and the recomputed link.

Listing 10.1 SPARQL: detect chain breaks around SwapOrder interventions

![A code snippet written in a query language selects artifacts involved in an intervention event labeled with a tampering type called "SwapOrder." It retrieves the artifact, event ID, previous hash, and a recomputed hash value. The query filters results to show only those where the original previous hash differs from the recomputed hash, indicating a detected change or tampering in the artifact's data. This helps identify inconsistencies or unauthorized modifications in the data records.](../images/624027_1_En_10_Chapter/624027_1_En_10_Figaaa_HTML.png)

## 10.9 Coverage and Missing Elements

**Coverage:** 37 of 52 ontology classes instantiated (71%). **Missing:** *PeerReview*, *SocialImplication*, *Evaluation* entities.

Why are these elements missing and how to add them:

* **PeerReview***(gap)*: no external assessor artifacts. *Add:* PR\_ExternalReviewer\_Report, PR\_Checklist.
* **SocialImplication***(gap)*: impact on user privacy and provider policy not modeled. *Add:* SI\_ProviderPolicyChange, SI\_PrivacyAssessment.
* **Evaluation***(gap)*: formal user or expert evaluation missing. *Add:* Eval\_PractitionerStudy, Eval\_UsabilityHeuristics.

Adding these branches would raise completeness and align the study with collaborative and societal expectations while preserving technical strength.

## 10.10 Interpretation and Teaching Notes

### 10.10.1 What the Results Mean

A 98 percent detection success with 1 percent false positives indicates that hash-chaining can robustly expose micro-edits and reordering under the modeled ingestion discipline. Detection time depends on provider latency and batching and is captured in DV\_TimeToDetection and associated benchmarks.

### 10.10.2 How to Reuse This Study

Because provider, region, and intervention types are modeled explicitly, a replicator can substitute a new provider service or enable cross-account logging while preserving the integrity model. The chain index and snapshot relations make provenance queries straightforward.

### 10.10.3 Common Misconceptions Clarified

* *Hash-chaining eliminates all tampering.* It makes tampering evident under the assumed ingestion order. It does not prevent upstream redaction policies or gaps due to service outages.
* *Ordering is purely deterministic.* Provider pipelines may reorder records. The ontology models this risk via IC\_NonDeterministicOrdering and timing controls.

### 10.10.4 Minimal Reproducibility Kit

Provider account templates, IAM policies for read-only export, ingestion scripts, chain-index generator, log snapshots with per-event hashes, activity logs, and PROV-C plus Dublin Core metadata all appear as ontological instances connected by explicit relations.

## 10.11 Final Remarks

This example illustrated how a forensic integrity problem in cloud infrastructures can be transformed into a structured, reproducible, and auditable experiment through the use of *ExperDF-Onto*. Instead of treating cloud logging as an opaque service, the chapter modeled every element, including questions, hypotheses, variables, and artifacts, as explicit ontological entities. This approach allows students and practitioners to understand how design decisions affect the validity and interpretation of results.

The experiment confirmed that a tamper-evident hash chain can detect micro-edits and record reordering with high reliability, achieving nearly 98 percent detection and only 1 percent false positives. However, it also showed that detection accuracy depends on contextual constraints such as ingestion order, replication delay, and provider-specific normalization. In other words, technical mechanisms alone are not sufficient unless they are accompanied by well-defined experimental controls and provenance records.

From a teaching perspective, this case demonstrates the value of modeling before experimentation. By formalizing entities and relations in *ExperDF-Onto*, learners can see how reproducibility, transparency, and forensic soundness are interconnected. The open dataset, metadata, and SPARQL queries provide a self-contained kit for replication and further exploration, turning a complex cloud experiment into a practical and instructive example.

Future extensions may include the classes *PeerReview*, *SocialImplication*, and *Evaluation* to capture ethical oversight, privacy impact, and practitioner feedback. Integrating these elements will help connect technical integrity with societal trust, reinforcing the broader lesson that digital forensics must combine accuracy, openness, and accountability to achieve meaningful scientific and social value.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_11>

# 11. Example 4: Echoes in the IoT Lab

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter presents a controlled smart home intrusion simulation that models time, interaction, and device heterogeneity using *ExperDF-Onto* so that correlation of evidence becomes measurable and auditable. The study asks whether clock offsets between devices and gateways degrade the ability to align cross-device events during an incident. The planning layer instantiates the experiment identity, research question, hypotheses, independent variables for device type and induced clock offset, dependent variables for correlation accuracy, alignment error, and event recall, plus control variables for network load, hub firmware, Wi-Fi channel, and attack script, as well as confounding factors such as RF noise and cloud queue delay with ethical and legal safeguards appropriate to a home-like lab. The pre-operation layer constructs a physical rig of ten IoT devices around a Zigbee hub, establishes calibration and latency benchmarks, validates the pipeline with a pilot, and documents operator training and vendor knowledge resources. During operation, packets and hub events are captured as first-class *Artifact* instances with integrity hashes, dual timestamps, and per-device offsets, while interaction relations record causal proximity and incident reports capture anomalies like missing timestamps. Analysis computes correlation accuracy near 92 percent with mean alignment error around 84 ms, tests offset effects across device types, records interpretation challenges due to stack-level timestamp inconsistency, and quantifies reliability across runs. Dissemination packages pcaps, hub JSON, calibration tables, scripts, and machine-readable RDF plus JSON metadata into a reusable dataset with clear authorship, impact assessment, and presentation guidance. Beyond reporting results, the chapter demonstrates how *ExperDF-Onto* separates measurement error from true absence of correlation, enables precise temporal queries over heterogeneous traces, and supports reproducible IoT forensics in settings where time is both evidence and adversary.

## 11.1 Context and Motivation

Smart homes blend heterogeneous devices, proprietary clouds, and intermittently reliable networks. Time is the invisible substrate that binds their traces: A door contact trips, a camera starts recording, a thermostat notes motion, and a hub forwards events upstream. A researcher designed a controlled study to answer a practical question for investigators: *How do timing differences between devices and gateways affect our ability to correlate IoT evidence during an intrusion simulation?*

This example shows how *ExperDF-Onto* models time, interaction, and heterogeneity as first-class concepts. By instantiating devices, packets, clock offsets, and interaction links, the ontology makes it possible to reconstruct multisource timelines and to quantify correlation accuracy rather than rely on anecdotal alignment.

We convert a narrative smart home scenario into a queryable ontological graph. At each phase, we state why a concept matters, how it is instantiated, which relations connect it, and what pitfalls the model prevents when correlating cross-device evidence.

## 11.2 Planning Phase

The planning layer turns the synchronization problem into measurable variables with ethical safeguards for a home-like setting, as follows:

* **Experiment** *(why)* names scope and identity. **Instance:** Exp\_IoT\_SyncCorrelation.
* **ResearchQuestion** *(why)* focuses uncertainty. **Instance:** RQ\_TimingImpactOnCorrelation.
* **Hypothesis** *(why)*: expected relation. **Instances:** H0\_NoTimingEffect and H1\_TimingAffectsCorrelation.
* **IndependentVariable** *(why)*: manipulated factors. **Instances:** IV\_DeviceType with levels {Camera, DoorContact, PIR\_Sensor, SmartPlug}; IV\_ClockOffsetCondition with levels {Offset0ms, Offset150ms, Offset500ms}.
* **DependentVariable** *(why)*: outcomes we measure. **Instances:** DV\_CorrelationAccuracy, DV\_PairwiseAlignmentError, DV\_EventRecall.
* **ControlVariable** *(why)* holds variability constant. **Instances:** CV\_NetworkLoad, CV\_HubFirmware, CV\_WiFiChannel, CV\_AttackScript.
* **ConfoundingFactor** *(why)*: acknowledged influences. **Instances:** CF\_EnvironmentalRFNoise, CF\_CloudQueueDelay, CF\_DeviceThermalThrottling.
* **EthicalPlanning** *(why)* protects privacy in a home-like context. **Instance:** EP\_SyntheticOccupants\_BlurredVideo.
* **LegalPlanning** *(why)* clarifies lawful data handling. **Instance:** LP\_ConsentWaiver\_LabSetting.
* **ReplicationPlanning** *(why)*: precommitment and transparency. **Instance:** RP\_OSF\_IoT\_Prereg.

We used the following relations: Exp\_IoT\_SyncCorrelation hasResearchQuestion RQ\_TimingImpactOnCorrelation; Exp\_IoT\_SyncCorrelation hasIndependentVariable IV\_DeviceType, IV\_ClockOffsetCondition; Exp\_IoT\_SyncCorrelation hasDependentVariable DV\_CorrelationAccuracy, DV\_PairwiseAlignmentError; Exp\_IoT\_SyncCorrelation isControlledBy CV\_NetworkLoad, CV\_HubFirmware; Exp\_IoT\_SyncCorrelation considersConfounding CF\_CloudQueueDelay; Exp\_IoT\_SyncCorrelation governedBy EP\_SyntheticOccupants\_BlurredVideo, LP\_ConsentWaiver\_LabSetting; Exp\_IoT\_SyncCorrelation preregisteredAs RP\_OSF\_IoT\_Prereg.

Typical pitfalls and ontology safeguards:

* *Pitfall:* Assuming NTP implies perfect synchrony. *Safeguard:* explicit IV\_ClockOffsetCondition and CF\_CloudQueueDelay.
* *Pitfall:* mixing device heterogeneity into one bucket. *Safeguard:* IV\_DeviceType with levels and per-device metadata.
* *Pitfall:* privacy leakage from real footage. *Safeguard:* EP\_SyntheticOccupants\_BlurredVideo.

## 11.3 Pre-Operation Phase

Pre-operation constructs a physical smart home rig with known timing characteristics and documented training, as follows:

* **ScenarioType** *(why)* clarifies material execution. **Instance:** ST\_PhysicalLabHome.
* **EnvironmentSetup** *(why)* enumerates devices and hub. **Instance:** ES\_10Devices\_ZigbeeHub with items {Camera\_C1, Camera\_C2, Door\_D1, PIR\_P1, PIR\_P2, Plug\_S1, Plug\_S2, Thermostat\_T1, Leak\_L1, Hub\_H1}.
* **Benchmark** *(why)*: baseline for timestamp drift and end to end delay. **Instances:** BM\_ClockSkewPerDevice, BM\_HubToCaptureLatency.
* **PilotProject** *(why)* de-risks data collection. **Instance:** PP\_OneDayTrial\_PartialDataset.
* **TrainingActivity** *(why)*: Config fluency reduces variable errors. **Instance:** TA\_DeviceConfigWorkshop\_4h.
* **KnowledgeResourceCondition** *(why)*: vendor docs and SDKs. **Instance:** KRC\_ZigbeeProfiles\_VendorSDKs.

We used the following relations: ES\_10Devices\_ZigbeeHub implements ST\_PhysicalLabHome; BM\_ClockSkewPerDevice benchmarks ES\_10Devices\_ZigbeeHub; PP\_OneDayTrial\_PartialDataset validates capture pipeline; TA\_DeviceConfigWorkshop\_4h prepares Participant CarolinaA\_Lead and Assistants; KRC\_ZigbeeProfiles\_VendorSDKs documents EnvironmentSetup ES\_10Devices\_ZigbeeHub.

Listing devices explicitly prevents silent substitution during replication and enables per-device analysis of drift and packet loss.

## 11.4 Operation Phase

We capture packets and hub events while simulating an intrusion sequence. Packets and events become artifacts, and interaction edges capture causal proximity, such as:

* **Participant** *(why)*: roles and accountability. **Instances:** CarolinaA\_Lead, LabAssistant\_1, LabAssistant\_2.
* **Instrument** *(why)*: capture and logging tools. **Instances:** Wireshark\_v4.2, HubLogger\_v1.3, TimeProbe\_v0.9.
* **Artifact** *(why)*: observable evidence items. **Examples:** PKT\_C1\_2025-06-02T10:00:01.213Z.pcaprec, HLOG\_DoorD1\_Open\_10:00:01.335Z.json, PKT\_Hub\_Zigbee\_Assoc\_10:00:01.500Z.pcaprec.
* **DataP** *(why)*: integrity and temporal context. **Examples:** sha256, deviceId, seq, hubTs, captureTs, offsetMs.
* **ActivityLog** *(why)*: human readable runbook. **Instance:** ALOG\_IoT\_Run03.csv.
* **OperationProcedure** *(why)* constrains execution. **Instance:** OP\_Arm\_ApproachDoor\_Open\_Record\_Leave.
* **Interaction Links** *(why)* correlate multi-device events. **Relations:** hasInteractionWith, precedesWithinWindow.
* **IncidentReport** *(why)*: exception handling. **Instance:** IR\_MissingTimestamps\_C2\_Run02.

We used the following relations: CarolinaA\_Lead uses Wireshark\_v4.2 and HubLogger\_v1.3; Wireshark\_v4.2 produced Artifact PKT\_C1\_...; HubLogger\_v1.3 produced Artifact HLOG\_DoorD1\_Open\_...; Artifact PKT\_C1\_... hasDataProperty captureTs=..., deviceId=Camera\_C1, offsetMs=150; Artifact HLOG\_DoorD1\_Open\_... hasInteractionWith PKT\_C1\_...; Artifact HLOG\_DoorD1\_Open\_... precedesWithinWindow PKT\_C1\_... [Δt≤300 ms]; ActivityLog ALOG\_IoT\_Run03.csv records OperationProcedure OP\_Arm\_ApproachDoor\_Open\_Record\_Leave; IncidentReport IR\_MissingTimestamps\_C2\_Run02 concerns device Camera\_C2 and run 02.

As operational checklist, we have to:

* Calibrate per-device offset before each run using TimeProbe\_v0.9
* Record both hub timestamps and capture interface timestamps
* Log channel, RSSI, and retry counters for RF diagnostics
* Immediately hash packet files and hub JSON exports

## 11.5 Analysis and Interpretation Phase

We quantify correlation accuracy as the proportion of expected cross-device pairings recovered within a temporal window and assess reliability across runs, as follows:

* **ResultMetric** *(why)* defines success quantitatively. **Instances:** RM\_CorrelationAccuracy\_0.92, RM\_MeanAlignmentError\_84ms, RM\_EventRecall\_0.95.
* **StatisticalAnalysis** *(why)* tests effects. **Instances:** Pearson\_r\_0.97 for alignment stability, ANOVA\_Accuracy\_ByOffset.
* **ThreatsToValidity** *(why)*: boundary of inference. **Instances:** TV\_DeviceResets, TV\_HubQueueOverflow, TV\_PacketLossBurst.
* **InterpretationChallenge** *(why)*: analytic friction. **Instance:** IC\_TimestampInconsistency\_AcrossStacks.
* **ReliabilityAnalysis** *(why)*: repeatability. **Instance:** Rel\_RunToRun\_r\_0.97.

We used the following relations: RM\_CorrelationAccuracy\_0.92 computedFrom pairs {HLOG\_DoorD1\_Open\_\* , PKT\_C1\_\*}; ANOVA\_Accuracy\_ByOffset tests effect of IV\_ClockOffsetCondition on DV\_CorrelationAccuracy; Pearson\_r\_0.97 evaluates stability across runs; IC\_TimestampInconsistency\_AcrossStacks impacts ResultInterpretation; TV\_DeviceResets threatens ValidityOfConclusions.

By modeling per-device offset and interaction windows, the ontology separates measurement error from genuine absence of correlation, helping analysts choose appropriate temporal thresholds.

## 11.6 Dissemination Phase

We publish a reusable, privacy-preserving dataset with clear roles and presentation guidance:

* **DisseminationPlan** *(why)*: venue and accessibility. **Instance:** DP\_OpenForensics\_Release.
* **Dataset** *(why)* bundles pcap, hub JSON, calibration tables, and scripts. **Instance:** DS\_IoT\_Echoes\_1\_0.
* **DatasetMetadata** *(why)*: machine and human discoverability. **Instance:** MD\_RDF\_PlusJSON.
* **Authorship** *(why)*: credit and roles. **Instance:** AUTH\_Araujo\_LabTeam.
* **ImpactAssessment** *(why)*: downstream uptake. **Instance:** IA\_TrainingLabAdoption.
* **PresentationQuality** *(why)*: clarity for learners. **Instance:** PQ\_StepByStepNotebook\_Slides.

We used the following relations: Dataset DS\_IoT\_Echoes\_1\_0 describedBy MD\_RDF\_PlusJSON; DisseminationPlan DP\_OpenForensics\_Release publishes DS\_IoT\_Echoes\_1\_0; Authorship AUTH\_Araujo\_LabTeam credits Experiment Exp\_IoT\_SyncCorrelation; ImpactAssessment IA\_TrainingLabAdoption evaluates Dissemination outcomes; PresentationQuality PQ\_StepByStepNotebook\_Slides enhances Dataset DS\_IoT\_Echoes\_1\_0.

## 11.7 Ontological Instantiation Snapshot

Table [11.1](#Tab1) shows the ontological instantiations for this example.

Table 11.1

Ontological instantiations for “Echoes in the IoT Lab”

| Ontology element | Example instance |
| --- | --- |
| Experiment | Exp\_IoT\_SyncCorrelation |
| ResearchQuestion | RQ\_TimingImpactOnCorrelation |
| Hypothesis | H0\_NoTimingEffect; H1\_TimingAffectsCorrelation |
| IndependentVariable | IV\_DeviceType {Camera, DoorContact, PIR\_Sensor, SmartPlug}; IV\_ClockOffsetCondition {0, 150, 500 ms} |
| DependentVariable | DV\_CorrelationAccuracy; DV\_PairwiseAlignmentError; DV\_EventRecall |
| ControlVariable | CV\_NetworkLoad; CV\_HubFirmware; CV\_WiFiChannel; CV\_AttackScript |
| ConfoundingFactor | CF\_EnvironmentalRFNoise; CF\_CloudQueueDelay; CF\_DeviceThermalThrottling |
| ScenarioType | ST\_PhysicalLabHome |
| EnvironmentSetup | ES\_10Devices\_ZigbeeHub {Camera\_C1, Camera\_C2, Door\_D1, PIR\_P1, PIR\_P2, Plug\_S1, Plug\_S2, Thermostat\_T1, Leak\_L1, Hub\_H1} |
| Benchmark | BM\_ClockSkewPerDevice; BM\_HubToCaptureLatency |
| PilotProject | PP\_OneDayTrial\_PartialDataset |
| TrainingActivity | TA\_DeviceConfigWorkshop\_4h |
| Instrument | Wireshark\_v4.2; HubLogger\_v1.3; TimeProbe\_v0.9 |
| Artifact | PKT\_\* pcaprec; HLOG\_\* json |
| DataP | sha256; deviceId; seq; hubTs; captureTs; offsetMs |
| ActivityLog | ALOG\_IoT\_Run03.csv |
| OperationProcedure | OP\_Arm\_ApproachDoor\_Open\_Record\_Leave |
| Interaction Relations | hasInteractionWith; precedesWithinWindow |
| IncidentReport | IR\_MissingTimestamps\_C2\_Run02 |
| ResultMetric | RM\_CorrelationAccuracy\_0.92; RM\_MeanAlignmentError\_84ms; RM\_EventRecall\_0.95 |
| StatisticalAnalysis | Pearson\_r\_0.97; ANOVA\_Accuracy\_ByOffset |
| ThreatsToValidity | TV\_DeviceResets; TV\_HubQueueOverflow; TV\_PacketLossBurst |
| InterpretationChallenge | IC\_TimestampInconsistency\_AcrossStacks |
| ReliabilityAnalysis | Rel\_RunToRun\_r\_0.97 |
| DisseminationPlan | DP\_OpenForensics\_Release |
| Dataset | DS\_IoT\_Echoes\_1\_0 |
| DatasetMetadata | MD\_RDF\_PlusJSON |
| Authorship | AUTH\_Araujo\_LabTeam |
| ImpactAssessment | IA\_TrainingLabAdoption |
| PresentationQuality | PQ\_StepByStepNotebook\_Slides |

## 11.8 Querying the Instantiation

The following SPARQL lists door open events and their nearest camera packet within a 300 ms window, returning alignment error using precomputed data properties.

Listing 11.1 SPARQL: correlate door events to camera packets within 300 ms

![Code snippet showing a SPARQL query that selects door events and camera packets with their timestamps and alignment error in milliseconds. It links door events from a device labeled Door_D1 and camera packets from Camera_C1, filtering results to include only those with alignment error between zero and three hundred milliseconds. The query uses prefixes for example ontology and XML schema, and matches artifacts and interactions with specific data properties for timestamps and alignment error.](../images/624027_1_En_11_Chapter/624027_1_En_11_Figaaa_HTML.png)

## 11.9 Coverage and Missing Elements

**Coverage:** 40 of 52 ontology classes instantiated (77%). **Missing:** *OntologyAlignment*, *QualityAssessment*, *Stakeholder*.

Why are these elements missing and how to add:

* **OntologyAlignment** *(gap)*: no mapping to SAREF or SSN ontologies. *Add:* Align\_Device\_to\_SAREF, Align\_Observation\_to\_SSN.
* **QualityAssessment** *(gap)*: formal quality gates absent. *Add:* QA\_PacketCompleteness, QA\_TimestampPrecisionAudit.
* **Stakeholder** *(gap)*: no external user groups modeled. *Add:* Stakeholder\_LEA\_Trainer, Stakeholder\_ConsumerAdvocacy.

Adding these classes would raise completeness and improve interoperability with community ontologies while clarifying intended beneficiaries.

## 11.10 Interpretation and Teaching Notes

### 11.10.1 What the Results Mean

A correlation accuracy of 92 percent with mean alignment error of 84 ms indicates that reliable cross-device reconstruction is feasible in a well-characterized lab home, but accuracy degrades under larger induced offsets and bursty packet loss as captured by TV\_PacketLossBurst.

### 11.10.2 How to Reuse This Study

Replace the hub or radio profile while preserving the IV\_DeviceType, IV\_ClockOffsetCondition, and calibration benchmarks. Because offsets and windows are explicit data properties, thresholds can be tuned without altering the conceptual structure.

### 11.10.3 Common Misconceptions Clarified

* *Near real time equals forensic grade time.* Not all timestamps share the same reference or precision. Model both hubTs and captureTs and their offsetMs.
* *If devices interact, their packets always correlate.* RF noise, queue overflow, and device resets can break expected links. These are modeled as ThreatsToValidity.

### 11.10.4 Minimal Reproducibility Kit

A device inventory including firmware versions; calibration scripts and tables; packet captures and hub logs with associated hashes; an interaction link derivation script; analysis notebooks; and metadata in RDF and JSON formats. All appear as explicit instances and relations in *ExperDF-Onto*.

## 11.11 Final Remarks

This study demonstrated how temporal uncertainty in smart home environments can be transformed into a measurable and auditable experimental problem when structured through *ExperDF-Onto*. By modeling time, interaction, and device heterogeneity as explicit entities, the chapter showed that correlation across devices is not only a technical task but also an epistemic one that depends on clear ontological framing.

The achieved correlation accuracy of about 92 percent and mean alignment error near 84 milliseconds confirm that well-calibrated IoT environments can sustain reliable event reconstruction despite inherent heterogeneity. At the same time, the experiment revealed how small clock offsets and queuing delays can produce misleading gaps or overlaps, underscoring that even subtle time drift can affect investigative conclusions. The ontology helped separate true loss of correlation from measurement artifacts, providing a more precise basis for reasoning about causality.

From a methodological point of view, the chapter advances reproducible IoT forensics by encoding every assumption, offset, and link into machine-readable form. This structure allows future replicators to adapt new devices, protocols, or hubs while maintaining comparability and traceability. The open dataset and metadata not only ensure transparency but also serve as a didactic reference for teaching time-based reasoning and integrity verification in connected environments.

Future work can extend this foundation by incorporating the missing classes *OntologyAlignment*, *QualityAssessment*, and *Stakeholder*. These additions will improve interoperability with external standards such as SAREF and SSN, introduce systematic quality gates, and connect experimental findings with the needs of law enforcement, educators, and consumer advocates. Through such integration, reproducible IoT forensics can move closer to a holistic understanding of time as both evidence and variable, ensuring that scientific accuracy aligns with societal trust and practical relevance.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_12>

# 12. Example 5: The Invisible Signature: Blockchain Provenance

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This chapter evaluates whether anchoring dataset fingerprints on public and permissioned blockchains can deliver tamper evident provenance with practical latency and cost and shows how *ExperDF-Onto* captures this workflow as a complete, auditable graph. The planning layer instantiates the experiment identity, research question, hypotheses, independent variable for blockchain platform selection, dependent variables for verification latency, hash stability, and end-to-end cost, along with controls for hash algorithm, bundling policy, and node provider version, plus confounders such as network congestion, gas price volatility, and endorsement policy differences, under ethical and legal constraints that anchor only hashes and treat anchors as metadata. The pre-operation layer defines a hybrid environment with smart contracts and chaincode, establishes confirmation and gas use benchmarks, validates the bundle to ledger path in a pilot, and records training and canonical protocol references. During operation, each dataset bundle is hashed deterministically, anchored by contracts or chaincode, and emits receipts that include transaction identifiers, block heights, timestamps, gas metrics, and network identifiers, all modeled as first-class *Artifact* instances linked to the producing *Instrument* and recorded in activity logs under a prespecified procedure. Analysis confirms perfect hash reproduction under cold recomputation, compares latency across platforms with nonparametric and factorial tests, and records interpretation challenges such as fee fluctuation and shallow reorg risk alongside threats to validity concerning anchoring only fingerprints and trusting node infrastructure, with reliability expressed as two-party consistency and quality assessment focused on trace validity. Dissemination packages bundles, contracts, receipts, notebooks, and FAIR plus JSON LD metadata with dual persistent identifiers to support independent verification and reuse. Beyond reporting outcomes, the chapter demonstrates how *ExperDF-Onto* separates content quality from provenance soundness, enables machine actionable verification queries, and provides a governance-ready template for trustworthy dataset publication in digital forensics.

## 12.1 Context and Motivation

When a dataset changes hands, spreadsheets can be copied, scripts can be tweaked, and filenames can be misleading. What investigators need is a way to attest that the evidence bundle they analyze is exactly the one that the original research group produced. A researcher designed a study to evaluate whether anchoring dataset fingerprints on public and permissioned blockchains can provide tamper-evident provenance with acceptable overhead. The example shows how *ExperDF-Onto* represents provenance anchors, transaction metadata, and verification workflows as first-class concepts that connect experimental artifacts to independent, append-only ledgers.

We translate a narrative about trustworthy dataset publication into a precise, queryable instantiation. At each phase, we explain which ontological elements are instantiated, how they are linked, and which common pitfalls the model prevents when using blockchains for forensic provenance.

## 12.2 Planning Phase

The planning layer turns “use blockchain for provenance” into testable variables and outcomes, with clear governance of data and code, as follows:

* **Experiment** *(why)* names the scope. **Instance:** Exp\_BC\_ ProvenanceValidation.
* **ResearchQuestion** *(why)* focuses uncertainty. **Instance:** RQ\_TamperEvidentProvenance.
* **Hypothesis** *(why)* sets expectation. **Instances:** H0\_NoGuarantee and H1\_BlockchainGuaranteesTamperEvidence.
* **IndependentVariable** *(why)* manipulated factor. **Instance:** IV\_BlockchainPlatform with levels {Ethereum\_Mainnet, Ethereum\_Sepolia, Hyperledger\_Fabric}.
* **DependentVariable** *(why)* measurable outcomes. **Instances:** DV\_VerificationLatency, DV\_HashStability, DV\_EndToEndCost.
* **ControlVariable** *(why)* holds variability constant. **Instances:** CV\_HashAlgorithm\_SHA256, CV\_BundlePolicy\_TarGzip, CV\_NodeProviderVersion.
* **ConfoundingFactor** *(why)* acknowledged influences. **Instances:** CF\_NetworkCongestion, CF\_GasPriceVolatility, CF\_FabricEndorsementPolicy.
* **EthicalPlanning** *(why)* avoids leakage of sensitive content. **Instance:** EP\_AnchorOnlyHashes\_NoRawData.
* **LegalPlanning** *(why)* clarifies lawful anchoring. **Instance:** LP\_JurisdictionalReview\_AnchorsAsMetadata.
* **ReplicationPlanning** *(why)* precommitment and transparency. **Instance:** RP\_GithubScripts\_OSFPrereg.
* **QualityPlanning** *(why)* defines success gates. **Instance:** QP\_TwoPartyVerification\_ColdRecalc.

We used the following relations: Exp\_BC\_ProvenanceValidation hasResearchQuestion RQ\_TamperEvidentProvenance; Exp\_BC\_ProvenanceValidation hasIndependentVariable IV\_BlockchainPlatform; Exp\_BC\_ProvenanceValidation hasDependentVariable DV\_VerificationLatency, DV\_HashStability; Exp\_BC\_ProvenanceValidation isControlledBy CV\_HashAlgorithm\_SHA256, CV\_BundlePolicy\_TarGzip; Exp\_BC\_ProvenanceValidation considersConfounding CF\_NetworkCongestion, CF\_GasPriceVolatility; Exp\_BC\_ProvenanceValidation governedBy EP\_AnchorOnlyHashes\_NoRawData, LP\_JurisdictionalReview\_AnchorsAsMetadata; Exp\_BC\_ProvenanceValidation preregisteredAs RP\_GithubScripts\_OSFPrereg; Exp\_BC\_ProvenanceValidation qualityGatedBy QP\_TwoPartyVerification\_ColdRecalc.

Typical pitfalls and ontology safeguards:

* *Pitfall:* anchoring raw data rather than hashes. *Safeguard:* EP\_AnchorOnlyHashes\_NoRawData and the Artifact design that treats fingerprints as first-class outputs.
* *Pitfall:* ignoring fee volatility. *Safeguard:* explicit CF\_GasPriceVolatility and DV\_EndToEndCost.
* *Pitfall:* unverifiable node behavior. *Safeguard:* CV\_NodeProviderVersion and QP\_TwoPartyVerification\_ColdRecalc.

## 12.3 Pre-Operation Phase

Pre-operation defines where and how anchors will be written, with pilots that validate the full path from bundle to transaction, such as:

* **ScenarioType** *(why)* environment clarity. **Instance:** ST\_Hybrid\_Public+Permissioned.
* **EnvironmentSetup** *(why)* concrete components. **Instance:** ES\_SC\_Eth+Fabric with items {EthContract\_AnchorV1, FabricChaincode\_AnchorV1, EthNode\_v1.13, FabricPeer\_v2.5}.
* **Benchmark** *(why)* baseline latencies and success. **Instances:** BM\_BlockConfirmationTime, BM\_ContractGasUsePerAnchor.
* **PilotProject** *(why)* early risk reduction. **Instance:** PP\_PilotHashAnchoring\_OK.
* **TrainingActivity** *(why)* operator proficiency. **Instance:** TA\_SCDeploymentWorkshop\_6h.
* **KnowledgeResourceCondition** *(why)* canonical references. **Instance:** KRC\_EIPs\_FabricDocs.

We used the following relations: ES\_SC\_Eth+Fabric implements ST\_Hybrid\_Public+Permissioned; BM\_BlockConfirmationTime benchmarks ES\_SC\_Eth+Fabric; PP\_PilotHashAnchoring\_OK validates pipeline from hash to ledger; TA\_SCDeploymentWorkshop\_6h prepares Participant JonasR\_PI and DevOps\_Team; KRC\_EIPs\_FabricDocs documents EnvironmentSetup ES\_SC\_Eth+Fabric.

## 12.4 Operation Phase

Each dataset bundle generates a deterministic fingerprint. Smart contracts (or chaincode) record this fingerprint along with minimal metadata. Activity logs capture operational metrics such as gas consumption and execution timing, including:

* **Participant** *(why)* roles and accountability. **Instances:** JonasR\_PI, DevOps\_Engineer\_1, Analyst\_Verifier\_A.
* **Instrument** *(why)* the anchoring mechanism. **Instances:** SmartContract\_AnchorV1, FabricChaincode\_AnchorV1, AnchorCLI\_v0.4.
* **Artifact** *(why)* evidence items and their fingerprints. **Instances:** Bundle\_DS\_Forensics\_1\_0.tar.gz, Hash\_SHA256\_Bundle\_abcd..., TxReceipt\_Eth\_0xdead..., TxReceipt\_Fabric\_tx123....
* **DataP** *(why)* integrity and context. **Examples:** sha256, blockHeight, txid, gasUsed, gasPrice, ledgerTs, networkId.
* **ActivityLog** *(why)* human readable provenance. **Instance:** ALOG\_AnchorRuns.csv.
* **OperationProcedure** *(why)* step discipline. **Instance:** OP\_Bundle\_Hash\_Anchor\_Verify\_Recalc.
* **UniqueID** *(why)* persistent identifiers. **Instances:** DOI\_10.5281/zenodo. 7654321, BCID\_0xdead...@EthMainnet.

We used the following relations: JonasR\_PI uses Instrument AnchorCLI\_v0.4; AnchorCLI\_v0.4 produced Artifact Hash\_SHA256\_Bundle\_abcd... from Artifact Bundle\_DS\_Forensics\_1\_0.tar.gz; SmartContract\_AnchorV1 registered Artifact Hash\_SHA256\_Bundle\_abcd... into BlockchainNetwork Ethereum\_Mainnet producing Artifact TxReceipt\_Eth\_0xdead...; TxReceipt\_Eth\_0xdead... hasDataProperty blockHeight=..., gasUsed=..., ledgerTs=...; OperationProcedure OP\_Bundle\_Hash\_Anchor\_Verify\_Recalc executedBy DevOps\_Engineer\_1; ActivityLog ALOG\_AnchorRuns.csv records OperationProcedure OP\_Bundle\_Hash\_Anchor\_Verify\_Recalc; UniqueID DOI\_10.5281/... identifies Dataset DS\_BC\_Provenance\_1\_0; UniqueID BCID\_0xdead...@EthMainnet identifies Artifact TxReceipt\_Eth\_0xdead....

As operational checklist we:

* Produce bundles deterministically with canonical tar and gzip flags.
* Compute hashes on an offline verifier and again on the publishing host.
* Anchor the same hash on two networks for redundancy: one public and one permissioned.
* Store receipts, ABI, and chain configuration in the activity log and dataset metadata.

## 12.5 Analysis and Interpretation Phase

We verify that recomputation reproduces the original hash and measure verification latency under load and congestion, such as:

* **ResultMetric** *(why)* quantitative success. **Instances:** RM\_HashReproduction\_1.00, RM\_MedianVerifyLatency\_Eth\_4.2s, RM\_MedianVerifyLatency\_Fabric\_0.9s, RM\_CostPerAnchor\_Eth\_US$1.27.
* **StatisticalAnalysis** *(why)* effect testing. **Instances:** MWU\_Latency\_EthVsFabric, ANOVA\_Latency\_ByCongestionTier.
* **InterpretationChallenge** *(why)* analytic friction. **Instances:** IC\_GasFluctuation, IC\_ReorgRisk\_LowDepth.
* **ThreatsToValidity** *(why)* inference boundary. **Instances:** TV\_AnchorOnly\_NoContent, TV\_NodeTrustAssumptions, TV\_FabricPolicyVariance.
* **ReliabilityAnalysis** *(why)* repeatability. **Instance:** Rel\_ColdRecalc\_TwoParty\_Consistent.
* **QualityAssessment** *(why)* formal gates. **Instance:** QA\_BlockchainTraceValidity.

We used the following relations: RM\_HashReproduction\_1.00 computedFrom {Hash\_SHA256\_Bundle\_abcd..., Recalc\_Hash\_SHA256\_Bundle\_abcd...}; MWU\_Latency\_EthVsFabric tests difference on DV\_VerificationLatency across IV\_BlockchainPlatform; IC\_GasFluctuation impacts ResultInterpretation; TV\_NodeTrustAssumptions threatens ValidityOfConclusions; Rel\_ColdRecalc\_TwoParty\_Consistent evaluates RM\_HashReproduction\_1.00; QA\_BlockchainTraceValidity assesses provenance soundness of receipts and anchors.

## 12.6 Dissemination Phase

We release the dataset, code, and contracts with dual identifiers and external review to increase trust and reuse, as follows:

* **DisseminationPlan** *(why)* venue and access. **Instance:** DP\_Zenodo\_Data+Contracts.
* **Dataset** *(why)* the research bundle. **Instance:** DS\_BC\_Provenance\_1\_0.
* **DatasetMetadata** *(why)* machine and human discovery. **Instance:** MD\_FAIR\_JSONLD.
* **UniqueID** *(why)* persistent references. **Instances:** DOI\_10.5281/zenodo.7654321, BCID\_0xdead...@EthMainnet.
* **Authorship** *(why)* credit and roles. **Instance:** AUTH\_Ribeiro\_Team.
* **PeerReview** *(why)* external scrutiny. **Instance:** PR\_ExternalReviewer\_Report.
* **PresentationQuality** *(why)* clarity for adopters. **Instance:** PQ\_HowToVerify\_Notebook+Slides.
* **ImpactAssessment** *(why)* downstream uptake. **Instance:** IA\_AdoptionByLabs\_Survey3mo.

We used the following relations: Dataset DS\_BC\_Provenance\_1\_0 describedBy MD\_FAIR\_JSONLD; DisseminationPlan DP\_Zenodo\_Data+ Contracts publishes DS\_BC\_Provenance\_1\_0; UniqueID DOI\_10.5281/ ... identifies DS\_BC\_Provenance\_1\_0; UniqueID BCID\_0xdead... @EthMainnet identifies TxReceipt\_Eth\_0xdead...; PeerReview PR\_ExternalReviewer\_Report assesses Experiment Exp\_BC\_ ProvenanceValidation; PresentationQuality PQ\_HowToVerify\_ Notebook+Slides enhances Dataset DS\_BC\_Provenance\_1\_0; ImpactAssessment IA\_AdoptionByLabs\_Survey3mo evaluates dissemination outcomes.

## 12.7 Ontological Instantiation Snapshot

Table [12.1](#Tab1) shows the ontological instantiations for this example.

Table 12.1

Ontological instantiations for “The Invisible Signature”

| Ontology Element | Example Instance |
| --- | --- |
| Experiment | Exp\_BC\_ProvenanceValidation |
| ResearchQuestion | RQ\_TamperEvidentProvenance |
| Hypothesis | H0\_NoGuarantee; H1\_BlockchainGuaranteesTamperEvidence |
| IndependentVariable | IV\_BlockchainPlatform {Eth\_Mainnet, Eth\_Sepolia, Fabric} |
| DependentVariable | DV\_VerificationLatency; DV\_HashStability; DV\_EndToEndCost |
| ControlVariable | CV\_HashAlgorithm\_SHA256; CV\_BundlePolicy\_TarGzip; CV\_NodeProviderVersion |
| ConfoundingFactor | CF\_NetworkCongestion; CF\_GasPriceVolatility; CF\_FabricEndorsementPolicy |
| ScenarioType | ST\_Hybrid\_Public+Permissioned |
| EnvironmentSetup | ES\_SC\_Eth+Fabric {EthContract\_AnchorV1, FabricChaincode\_AnchorV1} |
| Benchmark | BM\_BlockConfirmationTime; BM\_ContractGasUsePerAnchor |
| PilotProject | PP\_PilotHashAnchoring\_OK |
| TrainingActivity | TA\_SCDeploymentWorkshop\_6h |
| Instrument | SmartContract\_AnchorV1; FabricChaincode\_AnchorV1; AnchorCLI\_v0.4 |
| Artifact | Bundle\_DS\_Forensics\_1\_0.tar.gz; Hash\_SHA256\_Bundle\_abcd...; TxReceipt\_Eth\_0xdead... |
| DataP | sha256; txid; blockHeight; gasUsed; gasPrice; ledgerTs; networkId |
| ActivityLog | ALOG\_AnchorRuns.csv |
| OperationProcedure | OP\_Bundle\_Hash\_Anchor\_Verify\_Recalc |
| ResultMetric | RM\_HashReproduction\_1.00; RM\_MedianVerifyLatency\_Eth\_4.2s; RM\_CostPerAnchor\_Eth\_US$1.27 |
| StatisticalAnalysis | MWU\_Latency\_EthVsFabric; ANOVA\_Latency\_ByCongestionTier |
| InterpretationChallenge | IC\_GasFluctuation; IC\_ReorgRisk\_LowDepth |
| ThreatsToValidity | TV\_AnchorOnly\_NoContent; TV\_NodeTrustAssumptions; TV\_FabricPolicyVariance |
| ReliabilityAnalysis | Rel\_ColdRecalc\_TwoParty\_Consistent |
| QualityAssessment | QA\_BlockchainTraceValidity |
| DisseminationPlan | DP\_Zenodo\_Data+Contracts |
| Dataset | DS\_BC\_Provenance\_1\_0 |
| DatasetMetadata | MD\_FAIR\_JSONLD |
| UniqueID | DOI\_10.5281/zenodo.7654321; BCID\_0xdead...@EthMainnet |
| Authorship | AUTH\_Ribeiro\_Team |
| PeerReview | PR\_ExternalReviewer\_Report |
| PresentationQuality | PQ\_HowToVerify\_Notebook+Slides |
| ImpactAssessment | IA\_AdoptionByLabs\_Survey3mo |

## 12.8 Querying the Instantiation

The first query lists dataset versions, their SHA256 fingerprints, and the Ethereum transaction that anchored them. The second query verifies that the recomputed hash matches the anchored value.

Listing 12.1 SPARQL: list bundles with anchored tx metadata

![Code snippet showing a query that retrieves blockchain transaction details for smart contracts labeled "SmartContract_AnchorV1." It selects the bundle identifier, SHA-256 hash, transaction ID, block height, and gas used. The query links bundles to artifacts and their data properties, filters transactions produced by the specified smart contract, and extracts related properties such as transaction ID, block height, and gas used. This helps analyze and track specific smart contract transactions and their resource usage on the blockchain.](../images/624027_1_En_12_Chapter/624027_1_En_12_Figaaa_HTML.png)

Listing 12.2 SPARQL: verify recomputed hash equals anchored hash

![A query that selects bundles labeled as artifacts, retrieving their anchored and recalculated hash values. It matches data properties with keys "sha256" and "recalc_sha256" and filters results to include only those where the anchored hash equals the recalculated hash, ensuring data integrity.](../images/624027_1_En_12_Chapter/624027_1_En_12_Figaab_HTML.png)

## 12.9 Coverage and Missing Elements

**Coverage:** 42 of 52 ontology classes instantiated (80%). **Missing:** *Stakeholder*, *SocialImplication*, *ExternalReplication*.

Why are these elements missing and how to add them:

* **Stakeholder** *(gap)*: Intended beneficiaries are not explicitly modeled. *Add:* Stakeholder\_LEA\_Analyst, Stakeholder\_JournalDataEditor.
* **SocialImplication** *(gap)*: broader impact not captured. *Add:* SI\_EnergyCostImpact, SI\_TransparencyBenefit.
* **ExternalReplication** *(gap)*: third-party replay not encoded. *Add:* ExtRep\_IndependentLab\_Replay, linked to Rel\_ColdRecalc\_TwoParty\_ Consistent.

Introducing these classes would raise completeness and clarify who uses the provenance, how society is affected, and how independent replication is evidenced.

## 12.10 Interpretation and Teaching Notes

### 12.10.1 What the Results Mean

A hash reproduction rate of 1.00 indicates that cold recomputation matched the anchored value for all tested bundles. Verification latency is dominated by network confirmation time on Ethereum and by endorsement on Fabric. Costs on public chains vary with gas prices, which is captured by IC\_GasFluctuation and DV\_EndToEndCost.

### 12.10.2 How to Reuse This Study

Swap the platform level of IV\_BlockchainPlatform, or deploy a new smart contract while preserving the same bundle policy and hash algorithm. Because receipts and parameters are modeled as Artifact with explicit DataP, verification scripts can be regenerated from the ontology alone.

### 12.10.3 Common Misconceptions Clarified

* *Anchoring guarantees data quality.* It guarantees immutability of the fingerprint, not the scientific merit of the content. Use QualityAssessment to separate provenance soundness from content validity.
* *Public blockchains are always superior.* Permissioned ledgers can offer lower latency and stable cost under auditable governance, modeled by EnvironmentSetup and LegalPlanning.

### 12.10.4 Minimal Reproducibility Kit

Canonical bundling scripts, offline and online hash logs, contract ABIs and addresses, Fabric chaincode packages, and transaction receipts (including block heights and timestamps), along with verification notebooks and FAIR-compliant JSON-LD metadata, are all represented as explicit instances and relationships in *ExperDF-Onto*.

## 12.11 Final Remarks

This study showed that dataset fingerprints anchored on both public and permissioned blockchains can provide tamper-evident provenance with practical verification times and transparent costs when the workflow is modeled in *ExperDF-Onto*. By treating bundles, hashes, contracts, chaincode, and receipts as first-class *Artifact* instances linked to explicit *Instrument*, *OperationProcedure*, and *ActivityLog* entities, the chapter delivered not only empirical results but also a machine-actionable provenance graph that supports independent checks and long-term auditability.

The results confirm perfect hash reproduction under cold recomputation and highlight clear latency and cost profiles across platforms. At the same time, the analysis made visible the boundaries of the claim. Anchoring fingerprints does not assess scientific merit, and verification depends on network conditions, fee dynamics, shallow reorg risk, and the trust placed in node infrastructure. Encoding these factors as *ControlVariable*, *ConfoundingFactor*, *ThreatsToValidity*, and *QualityAssessment* elements allows investigators to separate content quality from provenance soundness and to report both with clarity.

Methodologically, the chapter contributes a governance-ready template for trustworthy dataset publication. Deterministic bundling, dual-network anchoring for redundancy, preserved receipts with block heights and timestamps, and FAIR plus JSON-LD metadata create a complete chain from dataset creation to public verification. Because every step is represented in the ontology, verification notebooks and queries can be regenerated even if tools change, which strengthens reproducibility and reduces hidden assumptions.

Future work can broaden impact by instantiating *Stakeholder*, *SocialImplication*, and *ExternalReplication* classes. These additions would connect the technical pipeline to its primary users, document energy and transparency trade-offs, and encode third-party replays as explicit evidence of replication. Further extensions may include cross-chain proofs, automated cost-aware anchoring policies, and routine integrity reports that combine provenance checks with dataset curation quality. Taken together, these steps move digital forensics toward publication practices where provenance is verifiable, governance is explicit, and reuse is safe and efficient.

# Part V Integration, Reflection, and Future Directions

This part marks the culmination of this book’s scientific, methodological, and philosophical trajectory. After examining the evolution of experimentation, the establishment of formal models, and the creation of ontological representations for Digital Forensics, this final part brings the discussion to a reflective synthesis. It explores how the elements introduced in the previous parts, namely empirical foundations, conceptual modeling, and semantic formalization converge into a coherent vision of Digital Forensics as a rigorous, transparent, and open scientific discipline.

While Part I established the historical and epistemological background for controlled experimentation in Digital Forensics, Part II provided a structural framework through the *ExperDF-CM* conceptual model, translating theoretical principles into operational research stages. Part III extended these foundations into the semantic domain with the *ExperDF-Onto* ontology, demonstrating how formal representations can describe, integrate, and reason about forensic knowledge in a machine-readable and interoperable way. Part IV then delivers a comprehensive and didactic walkthrough of how *ExperDF-Onto* can be instantiated to describe, reason about, and evaluate real digital forensics experiments, marking a decisive shift from theory to practice. Through five representative case studies, ranging from memory analysis and smartphone extraction to blockchain-based provenance, it illustrates how ontological modeling translates abstract constructs into verifiable scientific workflows, reinforcing transparency, reproducibility, and ethical responsibility. Finally, this part turns to a broader synthesis that connects these contributions and examines how they collectively redefine the production, interpretation, and validation of digital evidence within scientific practice.

The purpose of this part is not to summarize previous chapters but to integrate them, revealing their coherence, interdependence, and collective impact. It discusses how conceptual models and ontologies act as complementary instruments for building cumulative knowledge, supporting methodological transparency, and ensuring scientific accountability. It also highlights how the principles of Open Science are embedded in every methodological and ethical choice proposed throughout the book, transforming Digital Forensics from a procedural craft into an epistemically grounded research field.

In this context, Part IV performs three key functions. First, it offers an integrative synthesis that articulates the relationships among all previous parts and clarifies their shared contribution to the evolution of the field. Second, it provides a critical reflection on the remaining challenges that Digital Forensics must address, including technical, institutional, and philosophical issues. Third, it outlines future perspectives for research, education, and policy, emphasizing the importance of sustained collaboration and the continuous refinement of conceptual and semantic frameworks.

Ultimately, this part invites the reader to view Digital Forensics as a dynamic and evolving scientific ecosystem that unites methodological structure with interpretative flexibility, empirical rigor with ethical responsibility, and technological innovation with epistemological depth. By closing with a comprehensive analysis and forward-looking perspective, Part IV reaffirms the central message of this book: The strength of Digital Forensics lies in its capacity to integrate structure, meaning, and openness in the pursuit of reliable and verifiable knowledge.

© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026

E. OliveiraJr et al.

Controlled Experimentation of Digital Forensics

<https://doi.org/10.1007/978-3-032-19951-5_13>

# 13. Concluding Remarks: Toward a Scientifically Grounded and Open Digital Forensics

Edson OliveiraJr[1](#Aff6), 
Thiago J. Silva[2](#Aff7), 
Charles V. Neu[3](#Aff8), 
Avelino F. Zorzo[4](#Aff9) and 

Ana H. Mazur
[5](#Aff10)

([1](#R-Aff6))

State University of Maringá, Maringá, Brazil

([2](#R-Aff7))

AmbevTech, Maringá, Brazil

([3](#R-Aff8))

University of Santa Cruz do Sul (UNISC), Santa Cruz, Brazil

([4](#R-Aff9))

PUCRS, Porto Alegre, Brazil

([5](#R-Aff10))

State University of Maringá, Maringá, Brazil

Edson OliveiraJr (Corresponding author)

Email: 
[edson@din.uem.br](mailto:edson@din.uem.br)

Thiago J. Silva

Email: 
[josthiago1@gmail.com](mailto:josthiago1@gmail.com)

Charles V. Neu

Email: 
[charles1@unisc.br](mailto:charles1@unisc.br)

Avelino F. Zorzo

Email: 
[avelino.zorzo@pucrs.br](mailto:avelino.zorzo@pucrs.br)

Ana H. Mazur

Email: 
[bravinheloisa@gmail.com](mailto:bravinheloisa@gmail.com)

## Abstract

This final chapter integrates the theoretical, methodological, and semantic foundations developed throughout the book, offering a comprehensive reflection on the evolution of Digital Forensics as a scientific discipline. It revisits the main conceptual trajectories presented in earlier chapters, linking controlled experimentation, conceptual modeling, and ontology engineering under the shared vision of openness, rigor, and reproducibility. Rather than restating individual conclusions, the chapter examines how these contributions collectively establish a coherent epistemological framework for Digital Forensics, capable of bridging empirical investigation with semantic reasoning and ethical responsibility. It discusses the interplay between the ExperDF-CM and ExperDF-Onto models, highlighting their roles in structuring experiments, formalizing knowledge, and promoting interoperability across forensic tools and research environments. The chapter also identifies current gaps and challenges, such as data sensitivity, methodological fragmentation, and the need for community-driven governance of forensic ontologies. Finally, it outlines future perspectives for the field, emphasizing the convergence of Digital Forensics with Artificial Intelligence, Open Science infrastructures, and human-centered ethics. By synthesizing the insights and advances presented in the preceding chapters, this closing reflection positions Digital Forensics as a mature, transparent, and collaborative science dedicated to upholding the integrity and accountability of digital evidence.

## 13.1 Contextualization

This book was conceived with the ambition of establishing a rigorous, transparent, and epistemologically coherent foundation for Digital Forensics (DF) as both a scientific and a practical field. Emerging from a context where digital evidence plays an increasingly decisive role in judicial processes, cybersecurity operations, and research investigations, DF faces the dual challenge of maintaining operational efficiency while adhering to the principles of scientific inquiry. The book’s central objective has been to address this challenge by proposing a structured framework that integrates conceptual modeling, ontology engineering, and open science practices. Through seven chapters, it has progressively built theoretical and methodological scaffolding that supports reproducible experimentation, semantic interoperability, and evidence-based reasoning. The underlying hypothesis guiding this work is that the maturation of DF as a discipline depends not only on technological innovation but also on its capacity to systematize knowledge, formalize procedures, and align itself with the broader epistemic norms of science.

The book begins by examining the historical and philosophical roots of experimentation and the emergence of open science as a transformative movement that reshapes the way scientific knowledge is produced, validated, and shared. It then advanced toward developing domain-specific models and ontologies capable of representing the logic and processes of forensic inquiry. In doing so, it articulated a vision of DF that is not merely reactive, responding to incidents and producing isolated analyses, but proactive, cumulative, and verifiable. This concluding chapter synthesizes the contributions of the previous parts, connecting their theoretical premises, methodological innovations, and practical implications. It also explores remaining gaps, tensions, and emerging opportunities, offering directions for future research and institutional development.

## 13.2 Integrative Synthesis

The conceptual progression of the book unfolds across three major parts, each addressing a distinct yet interdependent layer of the discipline’s scientific architecture.

Part I introduced the epistemological and methodological foundations of Digital Forensics experimentation, situating the field within the broader tradition of empirical sciences. It discussed the persistent lack of reproducibility and transparency in DF research and outlined the core principles of controlled experimentation. The emphasis was placed on transforming forensic procedures, traditionally guided by intuition, expertise, or procedural standards, into replicable scientific investigations governed by hypotheses, variables, and evaluation criteria. This part also connected DF with the broader movement of Open Science, arguing that open data, open methodologies, and FAIR (Findable, Accessible, Interoperable, and Reusable) principles are indispensable for establishing cumulative and trustworthy forensic knowledge.

Part II represented the methodological consolidation of this vision by introducing conceptual modeling as a bridge between theoretical reasoning and empirical execution. The ExperDF-CM model proposed therein encapsulates the life cycle of controlled experiments in DF across five interrelated concepts: *Planning*, *Pre-Operation*, *Operation*, *Analysis and Interpretation*, and *Dissemination*. These stages operationalize scientific reasoning into reproducible procedures, ensuring that forensic experiments can be independently verified and accurately interpreted in their context. The model also functions as an educational and organizational tool, helping researchers and practitioners to articulate hypotheses, design protocols, and document findings consistently. By merging principles from software engineering experimentation, forensic methodology, and research ethics, ExperDF-CM creates a foundation upon which more sophisticated forms of empirical DF can be built.

Part III extended this structure into the semantic domain by presenting ontology engineering as a means to formalize and integrate forensic knowledge. Building upon the ExperDF-CM model, the ExperDF-Onto ontology provides a formal representation of entities, relationships, and processes involved in controlled forensic experimentation. It captures not only structural elements (such as artifacts, tools, datasets, and procedures) but also conceptual relations among them, enabling reasoning, validation, and automated query execution through SPARQL- and RDF-based representations. This semantic formalization transforms experimental documentation into machine-readable knowledge, facilitating interoperability between research projects, laboratories, and digital repositories. Together, ExperDF-CM and ExperDF-Onto form a complementary system: One prescribes how to conduct experiments; the other codifies and connects their outcomes in a structured knowledge space.

## 13.3 Critical Discussion

Despite the theoretical and methodological advances presented throughout the book, significant challenges remain for the full realization of an open and scientifically rigorous Digital Forensics. The first is cultural: DF has traditionally evolved as a practice-oriented discipline, grounded in law enforcement, cybersecurity response, and proprietary technologies. Moving toward an open, evidence-based research paradigm requires shifting from a mindset of procedural compliance to one of methodological reflection and critical thinking. Researchers and practitioners must be trained not only in technical procedures but also in epistemological reasoning, understanding the difference between evidence as data and evidence as scientifically interpretable information.

A second challenge lies in data governance and ethics. Forensic data are often sensitive, legally protected, or contextually bound to ongoing investigations. While Open Science advocates for transparency and data sharing, DF must reconcile these principles with the need to protect privacy, maintain chain-of-custody integrity, and safeguard the interests of individuals involved. Solutions such as synthetic datasets, anonymization techniques, and controlled access repositories represent promising avenues; however, they require institutional frameworks and shared standards that are still underdeveloped.

A third tension concerns the integration of conceptual and semantic modeling with real-world investigative workflows. The creation of ontologies like ExperDF-Onto depends on continuous dialogue between domain experts, data engineers, and legal professionals. Misalignment between terminological precision and operational reality can hinder adoption and reduce semantic consistency. Moreover, maintaining ontologies in dynamic environments, where technologies, threats, and laws evolve rapidly, requires sustainable governance and community-driven maintenance models.

Finally, there remains an epistemological question: ***Can digital forensics truly emulate the ideals of experimental science?*** While controlled experimentation enhances credibility, forensic phenomena often resist strict control or replication due to the uniqueness of digital incidents. This book argues that rather than imposing rigid scientific templates, DF should embrace a pluralistic approach, combining experimental design, case-based reasoning, and probabilistic inference, all under the overarching principles of transparency and reproducibility.

## 13.4 Implications and Contributions

The contributions of this book extend across theoretical, methodological, and practical dimensions.

**Theoretically**, it positions Digital Forensics as a legitimate domain of empirical investigation, capable of generating generalizable knowledge rather than isolated case reports. By connecting DF to the traditions of philosophy of science and experimental methodology, the book reframes the notion of digital evidence as a scientific construct, something that is produced, not merely found, through systematic observation and reasoning. It also contributes to ongoing discussions about the ontology of digital entities, causality in computational environments, and the epistemic status of digital traces as evidence.

**Methodologically**, the ExperDF-CM and ExperDF-Onto frameworks introduce structured instruments for documenting, reasoning, and sharing forensic experiments. These tools can be embedded into data management plans, laboratory workflows, or digital repositories, thereby aligning DF with broader practices of open and reproducible research. They also serve as didactic resources, helping students and early career researchers to internalize principles of scientific documentation and semantic rigor.

**Practically**, the implications are tangible for laboratories, judicial systems, and policymaking. Standardizing experimental design and documentation in DF can lead to more consistent expert reports, facilitate peer review of forensic methods, and strengthen the credibility of digital evidence in court. The semantic integration of experimental data also opens pathways for large-scale meta-analysis and knowledge discovery, enabling the identification of methodological patterns, error sources, and reliability metrics across studies. This contributes directly to improving the quality and accountability of forensic practice.

Finally, **socially and ethically**, the book underscores the importance of transparency, accountability, and inclusiveness in digital investigations. By promoting openness and methodological rigor, it aligns DF with the broader values of responsible innovation and trustworthy science, ensuring that the pursuit of truth in the digital realm respects fundamental human rights and societal expectations of justice.

## 13.5 Future Perspectives

The work presented here opens several avenues for future exploration. One immediate direction involves expanding the ExperDF ecosystem toward full interoperability with Open Science infrastructures. Integrating the ExperDF-Onto ontology with provenance ontologies, such as PROV-O, dataset metadata schemas like DataCite, and workflow vocabularies, like RO-Crate, could enable forensic experiments to be published, discovered, and reanalyzed across platforms. Another promising path lies in incorporating artificial intelligence into forensic experimentation. Ontology-driven AI systems could support hypothesis generation, automated consistency checking, and semantic inference, significantly accelerating the validation of forensic procedures.

A second direction concerns community building and governance. For ontologies and conceptual models to remain living artifacts, they must be maintained collaboratively through participatory and open processes. Establishing an international consortium or working group dedicated to the reproducibility of forensic experiments, similar to initiatives in empirical software engineering or bioinformatics, could ensure long-term sustainability and cross-disciplinary alignment.

A third perspective involves pedagogical transformation. Embedding the principles of controlled experimentation, conceptual modeling, and ontology engineering into forensic education would cultivate a new generation of professionals capable of designing scientifically sound investigations. Such integration could occur not only at the graduate level but also in continuing education and professional certification programs, bridging the gap between academia and practice.

Ultimately, the intersection of Digital Forensics and open science prompts reflection on broader societal implications. As digital evidence increasingly influences legal decisions, public policy, and social narratives, the epistemic robustness of forensic claims becomes a matter of democratic accountability. Ensuring that these claims are reproducible, explainable, and open to scrutiny is both a scientific imperative and an ethical responsibility. Future research should therefore engage with interdisciplinary fields such as philosophy of technology, computational ethics, and law, ensuring that DF remains anchored in human-centered and socially responsive principles.

## 13.6 Closing Message

This book closes with a vision of Digital Forensics as a science of integrity, one that integrates rigor, openness, and ethical consciousness. Its models and ontologies are not end points but stepping stones toward a more transparent, collaborative, and reflexive discipline. By aligning forensic investigation with the ideals of Open Science, it seeks to elevate DF from a reactive craft to a proactive science capable of self-correction, cumulative learning, and societal contribution. The pursuit of truth in the digital age requires not only better tools but also better epistemologies. In embracing structured experimentation, semantic modeling, and open collaboration, Digital Forensics can serve as both a guardian of evidence and a paradigm of scientific integrity. The spirit of this work can thus be summarized in a single conviction: The strength of digital evidence lies not in secrecy or authority, but in transparency, reproducibility, and shared understanding.
