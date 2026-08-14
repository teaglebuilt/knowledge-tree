---
title: llm-training
source: sources/ai/pdf/llm-training.pdf
source_type: paper
source_hash: 716484a814cf981c59e0ff2a14062fe680d8270f74a22a0fde61804376fbb88d
tags:
- ai
- paper
extracted: '2026-08-14'
---

# Click to edit Master title style

### **Generative AI Foundations, Fine-** **Tuning, RAG, and LLM** **Application Development**

**Rob Barton and Jerome Henry**

Cisco Confidential

#### Course Overview
# Click to edit Master title style

###### • Section 1: An Introduction to Large Language Models • Section 2: Prompt Engineering • Section 3: Retrieval Augmented Generation (RAG) • Section 4: Working with Open Source LLMs • Section 5: Fine-Tuning LLMs • Section 6: Developing LLM Applications

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Large Language Models**

Objectives:

    - How did Large Language Models Develop?

    - Tokenization and Word Embedding

    - The Transformer Architecture

    - The Self-Attention Mechanism

    - Positional Encoding

    - The Decoder Architecture

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - An Introduction to Generative AI

Cisco Confidential

#### A Short History of LLMs
# Click to edit Master title style

**Sept 2023**
**AWS Invests**

**GPT-3**
**Launch**

**Public**

**Feb 2023**

**Meta**
**launches**

Cisco Confidential

**Jan 2023**
**Chat GPT**
**100M Users**

#### The Many Uses of GenAI
# Click to edit Master title style

Cisco Confidential

#### Great for Generating Images

(drawn using OpenAI’s DALL-E)

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - Language Modeling

Cisco Confidential

#### What is Language Modeling?
# Click to edit Master title style
###### • Generative AI is a technique that uses neural networks to generate next words in a sequence

The conditional probability equation:

_next in sequence_ _history_

###### • Large Language models generate probabilities by learning from one or more text corpus (e.g. Wikipedia).

Cisco Confidential

#### The Early Days of Language Modelling
# Click to edit Master title style

Eliza – developed between 1964-67

- Language modeling was
[developed by Joseph](https://en.wikipedia.org/wiki/Joseph_Weizenbaum)
<u>[Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum)</u>

- Relied on scripted
responses based on
keywords and simple
syntactic transformations

Cisco Confidential

#### Classic Next-Word Prediction with NLP
# Click to edit Master title style

_Complete this famous movie line . . ._
###### • An n-gram is a contiguous sequence of words (tokens) from a given text sample. • The model uses a fixed-size window of previous words to calculate the probability of the next word:

n-gram with N=2
_Probability Distribution_

###### _I’ll make him an offer he can’t . . ._

Most words would receive a
probability of 0 since they are never
observed, and would make no sense

_resist_ _0.12_
_believe_ _0.14_
**_refuse_** **_0.54_**
_reject_ _0.15_
_accept_ _0.05_

Cisco Confidential

#### We use it all the time!
# Click to edit Master title style

Cisco Confidential

#### What’s Really Going On?
# Click to edit Master title style

Language Model

_I’ll make him an_
_refuse_
_offer he cant _____

99.5%

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - Tokenization and Word Embedding

Cisco Confidential

#### Preparing Words for the LLM
# Click to edit Master title style

Cisco Confidential

#### ChatGPT Tokenizer
# Click to edit Master title style DEMO

https://platform.openai.com/tokenizer

Cisco Confidential

#### Language Modeling and Neural Networks
# Click to edit Master title style

 - LLMs are based on Neural Networks at massive scale,

 - NNs understand numbers, not words!

 - Converting words into a single number doesn’t get you very far – words have
meaning, tone, feeling, context, et.

 - Words are converted to a vector with many dimensions.

  - The dimensions capture details of meaning, context, tone, voice, etc.

Cisco Confidential

#### Word Embedding:
# Click to edit Master title style

Building a model for a whole language

  - There are more than 100,000 words in the English language!

  - The average sentence in English has between 15-20 words.

  - There are almost an infinite number of combinations of words to form sentences

    - how can AI learn (AI relies on learning from a training set) this to predict words,
and then even generate new sentences?

1
2
3
4

99326
99327
99328
99329

A
A-1
A-bomb
A-frame
…
…
Zwitterion
Zwitterionic
Zwingli
zyzzogeton

How do you do
prediction / generation

with so many words?

Cisco Confidential

#### Word2Vec
# Click to edit Master title style

- Word2vec is a popular technique for Word Embedding
published in 2013.

- The word2vec algorithm uses a neural network model to learn
word associations from a text corpus.

- Word2vec uses ~300 dimensions to find context of a word

- Once trained, such a model can detect synonymous words or
suggest additional words for a partial sentence.

- GPT3 uses 12,288 dimensions per word (12,288 dimensions in
the tensor space represent a single word).

   - Think of all those extra dimensions as a “scratch space” that GPT-3
can use to write notes to itself about the context of each word.

Cisco Confidential

#### Word Embedding Semantic Relationships
# Click to edit Master title style

- By scanning multiple texts (a corpus) word Embedding represents
words in a multi-dimensional embedding vector space

- Words with similar semantic meanings (or used in similar contexts) are
close together in the embedding space.

Numbers

Cisco Confidential

#### Word2Vec
# Click to edit Master title style DEMO

https://projector.tensorflow.org/

Cisco Confidential

#### Neural Networks Refresher
# Click to edit Master title style

**Values are passed from the input to**

**multiple hidden layers, where a**

**Input Layer:**
**each “circle” represents**
**a dimension of the data**

**represented as a vector**

**A result comes out**

**here**

Input
Layer

Cisco Confidential

#### E.g. Word Embedding Vectors are Fed
# Click to edit Master title style
#### to the NN Input layer

 - The number of dimensions in the vector equate to the neurons in the NN
input layer (i.e. 12K embedding dimensions = 12K input neurons

Cisco Confidential

#### Values are then Passed to the Hidden
# Click to edit Master title style
#### Layer Neurons

 - Each hidden layer neuron has a different weight for the input links – the
weights are learned through training data (back prop)

```
Houston

```

```
 [34]

[419]

 [0]

```

Cisco Confidential

#### What’s Happening In the Neurons?
# Click to edit Master title style

 - The Weights are multiplied by the incoming values, then summed up
and passed to an activation function (ReLU)

Cisco Confidential

#### LLMs do More than Next-Word Word Prediction
# Click to edit Master title style

###### • We want to do more than just predict next words – we want to generate words! • LLMs are designed to generate text word-by-word by looking at what they have already generated until they reach End of Sequence (EOS)

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - The Transformer Architecture

Cisco Confidential

#### From Word Embeddings and Classic
# Click to edit Master title style
#### Language Modeling to Modern LLMs

In 2017 a revolutionary
paper introduced a new
architecture that gave
birth to the commercial
use of Generative AI

Cisco Confidential

#### The Transformer

              - GenAI and LLMs are based on the
# Click to edit Master title style

- GenAI and LLMs are based on the
Transformer Architecture, which uses
neural network foundations

Input

Output

Cisco Confidential

#### A Little More Detail

**The Encoder:**

tokens (words, etc.)

- The self-attention mechanism

them to surrounding words

Source: <u>[https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)</u>

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - The Self-Attention Mechanism

Cisco Confidential

#### The Self-Attention Mechanism
# Click to edit Master title style

- In self-attention the model tries to associate relevance of each individual
word to all other words (and itself) in the input sequence

- This happens one word at a time. Self-attention associates each word with
other words of similar context (looks for which words are similar to other
words in the input)

- Once similarities are calculated, they are used to determine how the
transformer encodes each word

Cisco Confidential

#### Self-Attention Mechanism at work

Cisco Confidential

#### Self-Attention Mechanism at work

Cisco Confidential

#### Self-Attention Example
# Click to edit Master title style

  - The goal of the attention mechanism is to add contextual information to
an input sequence

  - Self-attention looks at how each word appears in context and then makes
changes to the word embeddings

###### who  is  snow  white?

noun

noun adjective

Cisco Confidential

#### Before Self-Attention:
# Click to edit Master title style

- At first, the embeddings for “is” “snow” and “white” are all the same

- We don’t know the context

Cisco Confidential

#### After Self-Attention
# Click to edit Master title style

Who   is  Snow White? Why   is  Snow White?

1.3
3.2
5.2
7.2
3.5
0.6
1.4
. .
. .
. .
6,8

7.3
5.6
2.6
5.2
7.6
5.8
8.8
. .
. .
. .
7.7

3.7
8.3
3.2
6.6
8.4
7.2
0.5
. .
. .
. .
2.2

9.5
0.6
6.9
8.3
2.5
4.8
8.1
. .
. .
. .
1.9

9.2
6.3
0.3
6.3
7.3
9.6
7.2
. .
. .
. .
8.5

9.9
6.2
2.4
3.1
3.8
7.8
8.2
. .
. .
. .
6.9

2.2
7.7
2.7
6.3
5.3
8.0
1.1
. .
. .
. .
2.1

1.6
0.5
3.5
7.3
3.8
8.2
6.2
. .
. .
. .
5.2

- The goal of the Transformer is to update the embeddings with richer information,
changing their place in the vector space, giving the words meaning

- Now the word embeddings all look different – contextual meaning has been added,
changing their place in the vector space

Cisco Confidential

#### What Self-Attention Does
# Click to edit Master title style

Who    is  Snow  White? Why    is  Snow  White?

Initial _E1   E2  E3    E4_ _E1   E2  E3    E4_
Vectors:

_E1’   E2’   E3’   E4’_

New Vectors that
capture meaning:

_E1’’  E2’’  E3’’   E4’’_

Cisco Confidential

#### The Attention Mechanism

Three inputs to the attention mechanism:

- **(q) Query Vector:** **q** is a set of ”questions”
that each token asks about each other token

- **(k) Key Vector:** the **k** vector helps determine
the importance of each part of the input relative
to the query.

- **(v) Value Vector:** The **v** (value) vector
represents the actual data or information to be
attended to, and it is what ultimately gets passed
through and transformed into the final output (a
simple transformation of the original word
embedding)

Cisco Confidential

#### Step 1: Input Sequence embeddings are split
# Click to edit Master title style
#### into 3, then transformed into Q, K, V Vectors

The attention head generates the Q, K, and V
matrices:

- Q: a set of questions to ask about each token
in the sequence

- K: the "index" or "key" is a way to answer the
queries

- V: carries the actual meaning or embedding
of the word (derived from the original word
embedding).

Word
embedding

layer

Attention

Head

```
 who
 is
snow
white

```

Note: “n x d” indicates the matrix dimensions. The matrix
has “n” rows, indicating the number of tokens in the input
sequence, and “d” dimensions of each token from the
word embedding

Cisco Confidential

#### Step 2: The Q * K dot productClick to edit Master title style(dot product

matrix function)

Key
Matrix

Resulting

Matrix

- Q * K is a dot product matrix function

  - matches how well each query
aligns to each key

- e.g. “who” has a high association
score with “snow white” not just
with “snow”

Cisco Confidential

Query
Matrix

Word
embedding

layer

```
   who
   is
   snow
  white

```

x

=

|Attention Head|Col2|
|---|---|
|`Q `<br>`Matrix`<br>`(n x d)`<br>`K `<br>`Matrix`<br>`(n x d)`<br>`V `<br>`Matrix`<br>`(n x d)`<br>`Qw NN`<br>`Kw NN`<br>`Vw NN`||
|`Q `<br>`Matrix`<br>`(n x d)`<br>`K `<br>`Matrix`<br>`(n x d)`<br>`V `<br>`Matrix`<br>`(n x d)`<br>`Qw NN`<br>`Kw NN`<br>`Vw NN`||
|`Q `<br>`Matrix`<br>`(n x d)`<br>`K `<br>`Matrix`<br>`(n x d)`<br>`V `<br>`Matrix`<br>`(n x d)`<br>`Qw NN`<br>`Kw NN`<br>`Vw NN`||

#### What Does Dot Product do?

a large number

a small number

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|why|is|snow|snow|snow|white|

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|why|is|snow|white|white|white|

Attention for “why” Attention for “is” Attention for “snow” Attention for “white”

Cisco Confidential

#### Step 3: Calculate Softmax probabilities
# Click to edit Master title style

Soft max creates a
probability distribution

where the values sum

up to 1

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|why|is|snow|white|white|white|

Attention scores for

“white”

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|why|is|is|snow|white|

Normalized
Attention for “white”

- Softmax is a way to scale the input values between 0 and 1, the total
sum of all values = 1

- The result is the “attention matrix” - a set of attention scores indicating
how much attention to pay to each token when processing ”who”, etc.

Cisco Confidential

#### Softmax and Temperature

standard Softmax function.

- When T is low (i.e., _T → 0_ ), the output
probabilities become more deterministic,
concentrating most of the probability mass on the
largest logits.

- When T is high (i.e., _T → ∞_ ) the output
probabilities approach a uniform distribution.

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|why|is|is|snow|white|

Temp is small

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|why|is|is|snow|white|

Temp is large

Cisco Confidential

#### Step 4: Combine with the v Vector
# Click to edit Master title style

# Click to edit Master title style

Word
embedding

layer

```
   who
   is
   snow
  white

```

```
Attention
 Result
 (n x d)

```

|n meaning to the wo Attention Head|ord)|
|---|---|
|`Q `<br>`Matrix`<br>`K `<br>`Matrix`<br>`V `<br>`Matrix`<br>`Qw NN`<br>`Kw NN`<br>`Vw NN`|Dot product<br>function|
|`Q `<br>`Matrix`<br>`K `<br>`Matrix`<br>`V `<br>`Matrix`<br>`Qw NN`<br>`Kw NN`<br>`Vw NN`||

The attention vector is attached to the V vector, through
a matrix multiplication (matmul)

The output is what the model uses to represent “who”
after the self-attention mechanism.

Cisco Confidential

#### Multi-Head Attention
# Click to edit Master title style

 - Each self-attention process is called a "head” – there are
typically multiple attention heads

 - In theory, each head would learn something different

 - Each head produces an output vector that gets concatenated
(combined) into a single vector before going through the final
linear layer, and presented to the decoder

Cisco Confidential

#### Multi-Head Attention

d

d

n

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - Positional Encoding

Cisco Confidential

#### Transformers Process Tokens in Parallel
# Click to edit Master title style

```
      Who
[0.25,0.62,0.42,0.92]

```

```
      is
[0.43,0.22,0.12,0.87]

```

```
      Snow
[0.87,0.33,0.55,0.38]

```

```
     White
[0.11,0.24,0.97,0.31]

```

Cisco Confidential

#### Positional EncodingClick to edit Master title style

0.52 0.25 0.14 0.75

+

0.01 0.03 0.04 0.03

White

White + a tiny
adjustment

0.83 0.24 0.93 0.31

+

0.02 0.03 0.06 0.01

Cisco Confidential

#### Positional Encoding
# Click to edit Master title style

0.83 0.24 0.93 0.31

+

0.02 0.03 0.06 0.01

0.02 0.04 0.02 0.06 0.01 0.02 0.05 0.01

0.52 0.25 0.14 0.75

+

0.01 0.03 0.04 0.03

Offset Position 1 Offset Position 2 Offset Position 3 Offset Position 4

- Positional offsets are added to each dimension of the token’s embedding
vector, one by one

- The offsets for each position are always the same, so the model knows
what’s going on

- The offsets must be really small, to ensure the semantic representation
of the token doesn’t change

Cisco Confidential

#### Positional Encoding

Offset Encoding

Cisco Confidential

#### Positional Encoding
# Click to edit Master title style

Sine and Cosine are used in pairs, _d_ follows the
embedding dimensions

Cisco Confidential

# Section 1: Click to edit Master title style

**An Introduction to Generative AI**

    - The Decoder Architecture

Cisco Confidential

#### The Decoder

[Source: https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

**The Decoder:**

- The model generates tokens one at a
time, based on the previously generated
tokens.

- The decoder uses a similar self-attention
as tokens are generated so the output
stays coherent (i.e. predicts future
values based on past values).

Cisco Confidential

Output Probabilities

Exactly the
same as the
encoding
component

Cisco Confidential

- The decoder is _<u>auto-regressive</u>_,
meaning it takes in a list of previous
tokens as inputs, along with the
encoder output

#### Token Generation

- The output probabilities produced by softmax

- The new token is fed back into the decoder so
a new word in the sequence can be generated

- Positional encoding is used to track where the
word should be in the sentence

- The cycle continues until the decoder finally
generates an end of sequence token as an
output <EOS>.

Output (shifted right)

Cisco Confidential

#### Token Generation

- The output probabilities produced by softmax

- The new token is fed back into the decoder so
a new word in the sequence can be generated

- Positional encoding is used to track where the
word should be in the sentence

- The cycle continues until the decoder finally
generates an end of sequence token as an
output <EOS>.

Output (shifted right)

Cisco Confidential

#### Stacking Transformer Layers
# Click to edit

(Decoder-only architecture)

- Transformers are stacked in layers to
produce better results

- The lower layers are focused more on
word association and syntax.

- The higher layers encore more complex
relationships that focus on semantics.

- Chat GPT has 96 transformer layers!

Cisco Confidential

# Click to edit Master title style

### **Section 2 – Prompt Engineering**

**Rob Barton and Jerome Henry**

Cisco Confidential

**Section 2 Prompt Engineering**

Objectives

                 - Prompt Structure and ICL

                 - Zero or more shots

                 - Chains-of-Thought Prompting

                 - Self ask techniques

                 - Automated Prompt Engineering (APE)

                 - Advice for prompt engineering

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Prompt Structure and ICL

Cisco Confidential

## Starting Point
# Click to edit Master title style

You have a trained LLM:

    - It has a n-dimensional matrix for
each word embedding

    - (for each word-segment in the
training set, it can find relationships
with other word-segments, up to
”m” distance away in the text)

    - You want to interact with the LLM 
    - have it produce the text that best
continues your prompt

Cisco Confidential

## Prompt Structure
# Click to edit Master title style

All the text

that the
LLM

(your)
prompt

**LLM**

**Inference**

Cisco Confidential

#### In-Context Learning (ICL)
# Click to edit Master title style

Training dataset (+ fine tuning)

- Humans often have context in their mind (+personality, + tastes) when asking for LLM tasks

- LLMs ‘only’ have the relationships from the training set (+ optimally fine tuning)

     - You must convey your context to the LLM

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Zero or more shots

                      - Zero shot

                      - Few shots

                      - Role prompting

Cisco Confidential

#### Zero-shot (or Direct) Prompting
# Click to edit Master title style

 - The model is given a direct (context-less) instruction,
produces a response from its training

    - Recommended for simple tasks that only require general
knowledge

    - Often inefficient for complex or specific tasks

Cisco Confidential

#### Zero-shot Prompting – Specialized Task
# Click to edit Master title style

 - Without context, the model does not know what you
have in mind

    - E.g. what sound does a duck make again?

    - Of course, you could ask a more complete question, but can the
system learn what you have in your mind?

Cisco Confidential

#### Few-shot Prompting
# Click to edit Master title style

 - You provide the model with a few examples

    - When done well, this is sufficient to prime the answer to the
structure you are looking for

     - Variants: one example (“one-shot”), multiple examples (“multi-shot”)

Note: do not confuse few-shot prompting (here)
and few-shot learning (you fine-train your model
with many such examples, so that type of
answer becomes ‘natural’ to the model)

Cisco Confidential

#### Role Prompting
# Click to edit Master title style

 - “Context” needs not be examples – can be… context of
what type of answer you are looking for

    - A common approach is to describe the type of person
providing the answer (role)

Cisco Confidential

#### “Context Matters” Example
# Click to edit Master title style

 - Context provides tokens and their relationship.

    - The model is trained to continue expressing tokens and their
relationship

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Chains of thoughts variants

                      - Chain of Thought (CoT) Prompting

                      - Contrasted CoT

                      - Thread of thoughts

Cisco Confidential

#### Chain-of-Thought (CoT) Prompting
# Click to edit Master title style

 - “Context” is provided as a structure for building the answer

    - In addition to (or instead of) examples, you show the model
how to workout the answer

Cisco Confidential

#### Chain-of-Thought (CoT) Prompting
# Click to edit Master title style

 - “Context” is provided as a structure for building the answer

    - In addition to (or instead of) examples, you show the model
how to workout the answer

Cisco Confidential

#### Chain-of-Thought (CoT) Prompting
# Click to edit Master title style

 - “CoT” can sometimes be shortened as an instruction

    - This is zero-shot CoT

Cisco Confidential

#### Contrastive Chain-of-Thought (CoT) Prompting
# Click to edit Master title style

 - You provide both positive and negative examples

    - Works well in larger LLMs

    - Supposes that the LLM can perform each individual task required

Cisco Confidential

#### Thread-of-Thought (ToT) Prompting

CoT: the system is told to proceed
linearly from one thought to the next

# Click to edit Master title style

- Also called tree-of-thoughts

- Goal is to avoid trap where one thought is wrong
(-> all the rest is wrong)

- ToT provides “elements” or “bricks”
and lets the system build a path

dead ends

#### CoT, ToT Prompt Engineering Advice
# Click to edit Master title style

 - Build the context step-by-step if the task is difficult

    - This is called self-ask prompting

     - ###User: Tom has 23 apples. He removes two apples, how many does he have left?

     - ###Response: 21 apples.

     - ###User: now Tom uses 5 apples for a pie, how many apples are left?

     - ###Response: 16 apples.

     - Etc.

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Self ask techniques

                 - Self ask

                 - Self ask and Least to most

Cisco Confidential

#### Self-Ask Prompting
# Click to edit Master title style

 - If the task is complex (many bricks or steps, and you know
these steps), guide the model through the steps

Cisco Confidential

#### Self-Ask vs Least-to-Most Prompting
# Click to edit Master title style

 - With self-ask, you ask for individual tasks until there is enough context to operate the
complex task

 - With Least-to-most, you express the task into simple components

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Automated Prompt Engineering (APE)

Cisco Confidential

#### Prompt Engineering Automation
# Click to edit Master title style

New trend in prompt engineering (Automated Prompt Engineering, APE)
1. You use a (very) large LLM to generate _n_ questions variations aimed at
getting a better answer

    - _Generate a variation of the following instruction while keeping the semantic_
_meaning. Input: [INSTRUCTION]_

    - _“Present the answer logically”, “present the proof, then the conclusion”,_
_“explain each phase leading to the conclusion”,…_
2. A script sends the questions one by one to your (smaller) LLM and
collects each answer
3. The script (e.g. using rouge/bleu scores) or an operator measures which
answer is best
4. The output is a set of best keywords to add for better responses

Source: https://arxiv.org/abs/2211.01910

Cisco Confidential

**Section 2 Prompt Engineering**

                 - Advice for prompt engineering

Cisco Confidential

#### Prompt Engineering Limits
# Click to edit Master title style

 - Your model cannot provide structures it was not trained on.

    - Even in the CoT training, we showed addition examples, not
additions + subtractions

Cisco Confidential

#### Prompt Engineering Advice
# Click to edit Master title style

 - Stress important points by repeating them, for example
in different forms

     - <Blah blah>. _Proceed step-by-step_ . <more text>. _After each step, verify your reasoning_ .

 - Give specific instructions

     - _Summarize this text in two sentences._

     - _Summarize this text in 3 to 5 key bullets_
###### • Use positive patterns, not negative patterns

     - _Summarize in 3 sentences or less_

     - _Summarize. Do not use more than 3 sentences_

Cisco Confidential

#### Prompt Engineering Advice
# Click to edit Master title style

 - Learn “how many examples are enough, how many
examples are too many”

     - Not enough examples -> the system does no understand your context

     - Too many examples -> the model overfits (continues using the same structure for other,
unrelated tasks)

 - Your context should be larger than the completion

     - Accurate completion depends on the context richness

     - If your context is short, you assume the model default training is the context
###### • Don’t overthink the context, juts try

     - There is no perfect prompt, because the model is designed to produce varied answers

Cisco Confidential

#### Prompt Engineering Advice
# Click to edit Master title style

 - Plan-and-Solve prompting can trigger the model to work
step-by-step by itself

     - <Blah blah>. _First make sure to understand and rephrase the problem. Then devise a plan_
_to solve the problem. Then carry out the plan_ .

 - Use Self-Criticism prompting to improve the answer

     - User: tell me about climate change. LLM: <blah>

     - User: critique your answer. Find where it is lacking. LLM: the responses misses <blah>

     - User: from this critique, build a better response (if the LLM does not do it itself)

Cisco Confidential

#### A Warning on Hallucination
# Click to edit Master title style

 - The LLM continues the sentences based on its trained
dataset

    - It has no knowledge of the implied reality boundaries in the
meaning of the text

Cisco Confidential

# Click to edit Master title style

### **Section 3 – Retrieval-Augmented** **Generation (RAG)**

**Rob Barton and Jerome Henry**

Cisco Confidential

**Section 3: RAG**

Objectives

                 - RAG Principles

                 - RAG Data Process

                 - Retrieval within a chat context

Cisco Confidential

**Section 3: RAG**

                 - RAG Principles

Cisco Confidential

## Starting Point
# Click to edit Master title style

Your trained LLM does not provide the right text output

   - LLMs usually ‘try’ to provide the information you asked

   - They can hallucinate if they do not have the required data

- This issue happens often:

    - Because it was not trained on the relevant text

         - You ask about physics and the LLM was trained on Shakespeare

    - Because the relevant information was not accessible to the LLM at training time

         - The LLM was trained in 2023 and the information appeared in 2024

         - You have private, specific content

Cisco Confidential

## Two Directions: Fine Tuning or RAG
# Click to edit Master title style

Fine Tuning RAG

##### • You want to modify (adjust) the LLM internal parameters

- Private or more recent data

- Pointing to the source is a
Plus

##### • You want the LLM to access new information

- Make it better (more
knowledgeable) in a
particular field

- Make it provide more
naturally some type of
answer (e.g., good/bad
ratings)

Cisco Confidential

## Fine Tuning vs RAG
# Click to edit Master title style

|Fine Tuning|RAG|
|---|---|
|Task Specialization:<br>aims at making the model better for specific<br>fields/tasks|New information Integration:<br>aims at adding new knowledge to the model|
|Static:<br>model gets enhanced with new training, then<br>stays as (newly) trained)|Dynamic:<br>integrates new data as you point to it, but<br>model stays the same|
|Resource-intensive at fine-tuning<br>time|Resource-intensive at inference time|

Cisco Confidential

#### How RAG Works

# Click to edit Master title style

Standard LLM LLM with RAG

**Knowledge (Vector) DB**

**Relevant**
**chunks**

**Query**
**embedding**

**LLM**

**LLM**

#### The Knowledge Base
# Click to edit Master title style
###### • A Vector Database where you upload the documents of interest • 4 Phases:

Lorem ipsum
dolor sit
amet,
consectetur
adipiscing
elit

Upload
documents,
and convert
them to text
format

Chop Each Text
in Chunks

Convert each
chunk to
embedding

Add to DB

Cisco Confidential

**Section 3: RAG**

                 - RAG Data Process

Cisco Confidential

#### The Knowledge Base
# Click to edit Master title style
###### • A Vector Database where you upload the documents of interest • 4 Phases:

Chop Each Text
in Chunks

Convert each
chunk to
embedding

Add to DB

Cisco Confidential

#### Loading Documents
# Click to edit Master title style
###### • The loader needs to understand the document format you are loading (and convert it to text)

   - E.g. pdf (easy format)

Cisco Confidential

#### Loading Documents
# Click to edit Master title style
###### • The loader needs to understand the document format you are loading (and convert it to text)

   - E.g. youtube: mp4-> m4a (or mp3) -> voice to txt

Cisco Confidential

#### Loading Documents
# Click to edit Master title style
###### • The loader needs to understand the document format you are loading (and convert it to text)

   - E.g. youtube: mp4-> m4a (or mp3) -> voice to txt

Cisco Confidential

#### The Knowledge Base
# Click to edit Master title style
###### • A Vector Database where you upload the documents of interest • 4 Phases:

Lorem ipsum
dolor sit
amet,
consectetur
adipiscing
elit

Upload
documents,
and convert
them to text
format

Convert each
chunk to
embedding

Add to DB

Cisco Confidential

#### Splitting Documents
# Click to edit Master title style
###### • Cutting in 500/1000 characters (or tokens) is common

   - Overlap helps build continuity between chunks

Cisco Confidential

#### The Knowledge Base
# Click to edit Master title style
###### • A Vector Database where you upload the documents of interest • 4 Phases:

Lorem ipsum
dolor sit
amet,
consectetur
adipiscing
elit

Upload
documents,
and convert
them to text
format

Chop Each Text
in Chunks

Add to DB

Cisco Confidential

#### Vector Embedding
# Click to edit Master title style
###### • A Vector that encode the meaning of a chunk of text

“Lorem ipsum
dolor sit amet…”

My cat is hungry

My cat is happy

My cat is in the house

My house has a door

A plane in the sky

A cloud high above

The door is closed

Cisco Confidential

#### Creating Embeddings
# Click to edit Master title style
###### • Each split becomes a vector

Cisco Confidential

#### The Knowledge Base
# Click to edit Master title style
###### • A Vector Database where you upload the documents of interest • 4 Phases:

Lorem ipsum
dolor sit
amet,
consectetur
adipiscing
elit

Upload
documents,
and convert
them to text
format

Chop Each Text
in Chunks

Convert each
chunk to
embedding

Cisco Confidential

#### Storing in a Vector DB
# Click to edit Master title style
###### • This phase is trivial in principle, but an efficient vector database allows for fast search, duplicate detection etc.

Cisco Confidential

**Section 3: RAG**

                 - Retrieval within a chat context

Cisco Confidential

#### Retrieving Data

# Click to edit Master title style

LLM with RAG

###### • A query is passed to the vector Db through a retriever function • The DB returns the k vectors closest to the query text

**LLM**

#### Retrieving Vector dB data
# Click to edit Master title style
###### • The retriever does not process the text – it merely returns the ‘k’ closest matches

Cisco Confidential

#### RAG Process

# Click to edit Master title style

LLM with RAG

- The vector DB is created beforehand
(update each time a new source is
added)

1. In the chatbot, the user query is first
passed to the vector db
2. The retriever brings back the k most
relevant chunks
3. The chunks and the query are
passed to the LLM
4. The LLM uses the chunks to optimize
its answer

**Query**
**embedding**

**Knowledge (Vector) DB**

**Relevant**
**chunks**

**LLM**

# Click to edit Master title style

### **Section 4 Working with Open-** **Source LLMs**

**Rob Barton and Jerome Henry**

Cisco Confidential

# Section 4: Click to edit Master title style

**Working with Open Source LLMs**

Objectives:

    - Comparing Mode Types

    - Open-Source vs. Closed-Source LLMs

    - The Hugging Face Transformers Library

Cisco Confidential

# Section 4: Click to edit Master title style

**Working with Open Source LLMs**

    - Comparing Model Types

Cisco Confidential

# Click to edit Master title style
#### Types of Transformers / Language Models

There are generally two types of language models used today:

**1.** **Auto Encoding** (often known as “BERT”-style models. Excel at
reading text very quickly)

2. **Auto Regressive** (most of the GPT-style models. Very good at
generating new text)

Cisco Confidential

#### BERT (Bi-Directional Encoder Representation from Transformer)Click to edit Master title style

- Developed by Google in 2018 – an early
Language Model based on the Transformer
encoder.

- Powerful model for language understanding
and sentiment analysis (but not so good at
generating words)

- ~2,500x smaller than GPT 3.5, but performs
similar for classification tasks

Cisco Confidential

#### Comparing LLMs:Click to edit Master title style

Auto-Regressive vs. Auto-Encoding Models

**Auto-Encoding** (BERT-style models):

  - Strength is in reading text fast, limited ability to generate text (there is no decoder)

  - Excels at classifying data it read (e.g. sentiment analysis)

  - Models tend to be smaller, and very efficient

  - Usually very fast, often used for SLMs (can get away without a GPU in some cases)

**Auto-Regressive** (GPT-style models):

  - The model is trained to predict the probability distribution of next token given the
previous tokens in a sequence.

   - Mathematically, it estimates: _P(xt | x1, x2, ..., x{t-1})_

  - Really good at token generation, but can be very slow

Cisco Confidential

#### To Summarize . . .

Cisco Confidential

|Col1|Encoder-Decoder<br>Transformers<br>(BART, T5)|Col3|Decoder Only<br>Transformers<br>(ChatGPT, Claude,<br>etc.)|
|---|---|---|---|
|Encoder Only<br>Transformers<br>(BERT / ROBERTA)<br>– often used as<br>Small Language<br>Models (SLMs)||||
|||||
|||||

#### How are Models Trained?Click to edit Master title style

Auto-regressive Models

Auto-encoding Models (use Masked Language

Modeling, MLM)

use next-word

prediction

To be MASK not MASK be that is the ?

questi
To be or not to be that is the

on

Cisco Confidential

# Section 4: Click to edit Master title style

**Working with Open Source LLMs**

    - Open Source vs. Closed Source LLMs

Cisco Confidential

#### Closed- vs. Open-Source LLMs
# Click to edit Master title style

Cisco Confidential

#### Does Model Size Matter?

Cisco Confidential

#### Counting Parameters in Language Models
# Click to edit Master title style

Input
Layer

**47 parameters in**
**total!**

Indicates bias adjustments to

the neuron

Cisco Confidential

# Click to edit Master title style
#### How to Select the Right Model

- Model selection is based on the use case:

 - E.g. if we want to classify a day-zero security vulnerability, a BERT-style model
performs much better than an auto-regressive style model

 - Chatbot interfaces may use a combination of systems (multi-modal) – using some
elements of a semantic search, along with text generation

- In all cases, the selection of the model should be evaluated through a gating
process (e.g. a Responsible AI (RAI) team)

 - Examines model bias, censoring, how it was trained

Cisco Confidential

#### Model Selection is Important
# Click to edit Master title style

- Model accuracy will vary greatly on
how it was trained, model
structure, etc.

- Models show strength in different
areas, depending on training
method and fine-tuning

- E.g. GPT o1 is strong at coding and
math (uses chain-of-thought
reasoning)

Source: https://arxiv.org/pdf/2307.09009.pdf

Cisco Confidential

#### LLM Application Selection by Use CaseClick to edit Master title style

**1.** **Pre-Trained (packaged) Models**

     - Choose an open or closed source model, requires no alteration

     - Ask questions, write a resume, debug code, etc.

**2.** **Retrieval Augmented Generation (RAG) System**

     - Augments an existing model with a semantic retrieval system

     - Easy to keep updated (only required to keep vector database up to date)

     - Good for contextual-specific tasks that foundational models were not trained on

**3.** **Fine Tuning**

     - Start with a foundational model, and then fine-tune for a specific purpose

Cisco Confidential

# Section 4: Click to edit Master title style

**Working with Open Source LLMs**

    - The Hugging Face Transformers Library

Cisco Confidential

#### Exploring Open-Source Models
# Click to edit Master title style
#### with Hugging Face

- Hugging Face is an AI company which has become the world’s largest
repository of open-source transformers

- Developed a strong developer ecosystem through the transformers
library

Cisco Confidential

#### Hugging Face Transformers Library Click to edit Master title style

1. Select a model from 100s of thousands of options

2. Fine-tune the model using the source code

3. Convert input text into tokens (tokenizer)

4. Pass to an embedding model

5. Then use inference with the model

###### **_DEMO_**

Cisco Confidential

# Click to edit Master title style

### **Section 5 Model Fine-Tuning**

**Rob Barton and Jerome Henry**

Cisco Confidential

# Section 5: Click to edit Master title style

**Model Fine-Tuning**

Objectives:

    - Why Fine-Tuning?

    - Fine-Tuning Strategies

    - Parameter Efficient Fine-Tuning (PEFT) and Low Rank
Adaptation (LoRA)

Cisco Confidential

# Section 5: Click to edit Master title style

**Model Fine-Tuning**

    - Why Fine-Tuning?

Cisco Confidential

#### Stages of LLM Training and Fine-Tuning
# Click to edit Master title style

Cisco Confidential

#### Why Fine-Tuning?
# Click to edit Master title style

  - Intent is to adapt a pre-trained model for a specific task, using
a dataset the model has not previously been trained on

   - Result will allow the model to perform better for a given task

  - Useful for industry-specific tasks:

    - Banking

    - Healthcare

    - Pharmaceutical, etc.

  - Teaches the model “how to answer”

    - Important for agentic workflow

Cisco Confidential

#### Base Model vs. Fine-Tuned Model
# Click to edit Master title style

**Prompt:** Help me diagnose this: a patient complains of a fever,
cough, and difficulty breathing."

#### Performance Benefits of Fine-Tuning

**SuperGLUE** (Super General Language Understanding Evaluation) is a comprehensive benchmark
designed to evaluate the performance of language models on a broad range of challenging natural
language understanding tasks (not text generation).

Cisco Confidential

#### Model Fine-Tuning vs.
# Click to edit Master title style
#### Retrieval Augmented Generation (RAG)

**Fine Tuning**

- Involves specialized tuning of model
parameters with new data

- Requires access to the model source
code and artefacts

- Results in a faster model tuned with
locally relevant information

- Examples include Transfer Learning,
LoRA, etc.

**RAG**

- The model is not changed and access
to model code is not necessary

- Document chunks are fed to the
model along with the prompt to give
is better context

- Performs slower than a fine-tuned
model, but easier to keep up to date

Cisco Confidential

# Section 5: Click to edit Master title style

**Model Fine-Tuning**

    - Fine-Tuning Strategies

Cisco Confidential

#### Retraining Model Parameters

#### Retraining Model Parameters

|Col1|Description|Advantages|Disadvantages|Use Cases|
|---|---|---|---|---|
|**Full**<br>**Retraining (all**<br>**parameters)**|Training a model from<br>scratch using a large, task-<br>specific dataset.|•<br>Complete control over<br>model design.<br>•<br>Tailored specifically to<br>the task.<br>•<br>Best for novel tasks.|•<br>Requires massive<br>amounts of data and<br>computational<br>resources.<br>•<br>Time-consuming.<br>Risk of overfitting.|•<br>Very specific tasks<br>where pre-trained<br>models don’t exist.<br>•<br>Highly specialized<br>applications.|
|**Transfer**<br>**Learning**|•<br>Fine-tuning a pre-<br>trained model by<br>updating all or part of<br>its parameters on a<br>smaller, task-specific<br>dataset.|•<br>Leverages existing pre-<br>trained knowledge.<br>•<br>Requires less data and<br>resources compared to<br>full training.|•<br>Still resource-intensive<br>when updating most<br>of the model.<br>•<br>Limited by the quality<br>of the pre-trained<br>model.|•<br>Domain<br>adaptation.<br>•<br>Tasks with<br>moderate<br>computational<br>resources and<br>some labeled data.|
|**Parameter**<br>**Efficient Fine**<br>**Tuning (PEFT)**|• Fine-tuning only a small<br>portion of the pre-<br>trained model's<br>parameters while<br>keeping most layers<br>frozen.|• Significantly reduces<br>computational cost.<br>• Faster training.<br>• Lower memory<br>requirements.|• May result in slightly<br>lower performance<br>compared to full fine-<br>tuning.<br>• Task-specific design<br>needed.|• Resource-<br>constrained<br>environments.<br>• Training very large<br>models on specific<br>tasks with limited<br>data.|

Cisco Confidential

#### Retraining Model Parameters

#### Retraining Model Parameters

|Col1|Description|Advantages|Disadvantages|Use Cases|
|---|---|---|---|---|
|**Full**<br>**Retraining (all**<br>**parameters)**|Training a model from<br>scratch using a large, task-<br>specific dataset.|•<br>Complete control over<br>model design.<br>•<br>Tailored specifically to<br>the task.<br>•<br>Best for novel tasks.|•<br>Requires massive<br>amounts of data and<br>computational<br>resources.<br>•<br>Time-consuming.<br>Risk of overfitting.|•<br>Very specific tasks<br>where pre-trained<br>models don’t exist.<br>•<br>Highly specialized<br>applications.|
|**Transfer**<br>**Learning**|•<br>Fine-tuning a pre-<br>trained model by<br>updating all or part of<br>its parameters on a<br>smaller, task-specific<br>dataset.|•<br>Leverages existing pre-<br>trained knowledge.<br>•<br>Requires less data and<br>resources compared to<br>full training.|•<br>Still resource-intensive<br>when updating most<br>of the model.<br>•<br>Limited by the quality<br>of the pre-trained<br>model.|•<br>Domain<br>adaptation.<br>•<br>Tasks with<br>moderate<br>computational<br>resources and<br>some labeled data.|
|**Parameter**<br>**Efficient Fine**<br>**Tuning (PEFT)**|•<br>Fine-tuning only a small<br>portion of the pre-<br>trained model's<br>parameters while<br>keeping most layers<br>frozen.|•<br>Significantly reduces<br>computational cost.<br>•<br>Faster training.<br>•<br>Lower memory<br>requirements.|•<br>May result in slightly<br>lower performance<br>compared to full fine-<br>tuning.<br>•<br>Task-specific design<br>needed.|•<br>Resource-<br>constrained<br>environments.<br>•<br>Training very large<br>models on specific<br>tasks with limited<br>data.|

Cisco Confidential

#### Retraining Model Parameters

#### Retraining Model Parameters

|Col1|Description|Advantages|Disadvantages|Use Cases|
|---|---|---|---|---|
|**Full**<br>**Retraining (all**<br>**parameters)**|Training a model from<br>scratch using a large, task-<br>specific dataset.|•<br>Complete control over<br>model design.<br>•<br>Tailored specifically to<br>the task.<br>•<br>Best for novel tasks.|•<br>Requires massive<br>amounts of data and<br>computational<br>resources.<br>•<br>Time-consuming.<br>Risk of overfitting.|•<br>Very specific tasks<br>where pre-trained<br>models don’t exist.<br>•<br>Highly specialized<br>applications.|
|**Transfer**<br>**Learning**|•<br>Fine-tuning a pre-<br>trained model by<br>updating all or part of<br>its parameters on a<br>smaller, task-specific<br>dataset.|•<br>Leverages existing pre-<br>trained knowledge.<br>•<br>Requires less data and<br>resources compared to<br>full training.|•<br>Still resource-intensive<br>when updating most<br>of the model.<br>•<br>Limited by the quality<br>of the pre-trained<br>model.|•<br>Domain<br>adaptation.<br>•<br>Tasks with<br>moderate<br>computational<br>resources and<br>some labeled data.|
|**Parameter**<br>**Efficient Fine**<br>**Tuning (PEFT)**|•<br>Fine-tuning only a small<br>portion of the pre-<br>trained model's<br>parameters while<br>keeping most layers<br>frozen.|•<br>Significantly reduces<br>computational cost.<br>•<br>Faster training.<br>•<br>Lower memory<br>requirements.|•<br>May result in slightly<br>lower performance<br>compared to full fine-<br>tuning.<br>•<br>Task-specific design<br>needed.|•<br>Resource-<br>constrained<br>environments.<br>•<br>Training very large<br>models on specific<br>tasks with limited<br>data.|

Cisco Confidential

#### Supervised Fine-Tuning, Step-by-Step
# Click to edit Master title style

**Step 1:**
Identify the task / use case. Will
determine the type of model to be
used (e.g. BERT vs. GPT style).

**Step 3:**
Select a pre-trained existing model
(typically from a model repository
such as Hugging Face).

**Step 4:**
Determine the fine-tuning method
to be used (Transfer Learning,
PEFT, RAFT, etc.).

**Step 5:**
Fine tune the model. Select the
number of training epochs, etc.

**Step 6:**
Test and deploy the fine-tuned
model.

Cisco Confidential

# Section 5: Click to edit Master title style

**Model Fine-Tuning**

    - Parameter Efficient Fine-Tuning (PEFT) and Low Rank
Adaptation (LoRA)

Cisco Confidential

#### Computational Costs of LLMs
# Click to edit Master title style

```
                 Meta-Llama-3.1-8B

```

Used to store the
model weights

Used to update the
parameters during
training / fine-tuning

Captures the direction
and trajectory of the
parameter updates

Adaptively tunes
the gradient step
size to prevent
destabilization.

Cisco Confidential

Total Memory Required

= 112GB
(3x A100 GPUs)

#### LoRA – Low Rank Adaptation
# Click to edit Master title style

Cisco Confidential

#### Low-Rank Adaptation (LoRA)
# Click to edit Master title style

  - LoRA is a PEFT technique to improve fine-tuning performance and
reduce computational cost.

  - The base model is augmented with new adaptation layer

  - The existing model parameters are “frozen” – kept as is – but new
parameters are added that are much simpler to train

frozen parameters

In this layer, new special
parameters are added that will be
trained – all other parameters are
frozen

Cisco Confidential

#### First – how a Neural Network is Described
# Click to edit Master title style
#### Mathematically

_1_

_1_

_1_

_d_

_matrix_
_(trainable)_

- _x are the input matrix from the previous layer_

- _h(x) is a function that represents the layer_

- _k is the number of parameters per neuron_

- _d is the number of neurons per layer_

respectively, there are **<u>1,000,000</u>**
**<u>trainable parameters</u>** in this
layer

Cisco Confidential

#### Insert a new “low rank” parameter set
# Click to edit Master title style
#### for this layer

_1_

_1_

(1000 x 5) + (5 x 1000) = 10,000 trainable parameters,
and the output is still the same size matrix!

Cisco Confidential

- B is a _d x r_ matrix

- A is a _r x k_ matrix

- r is the “rank”

# Click to edit Master title style

#### Instructional Fine-Tuning with LoRA

###### **_DEMO_**

Cisco Confidential

# Click to edit Master title style

### **Section 6 – Developing LLM Apps**

**Rob Barton and Jerome Henry**

Cisco Confidential

**Section 6: Developing LLM Apps**

Objectives

                 - LLM App Introduction

                 - Comparing Models

                 - Leveraging APIs

                 - Building the Interface

Cisco Confidential

**Section 6: Developing LLM Apps**

                 - LLM App Introduction

Cisco Confidential

## LLM App Development Approaches
# Click to edit Master title style

An LLM App is human interface to one or more LLMs and their functions
2 possible approaches:

Cisco Confidential

## LLM App Components
# Click to edit Master title style

As the LLM App is about getting information from an LLM, it has 3
components:

**Step 1: Model choice**
Each model is a
compromise between
task (specialization), size
and precision.

**Step 2: Model feed**
Use APIs to point the
model(s) to the right
data, before
concatenating the
results

**Step 3: Model wrapper**
The UI can be simple, or
include safeguards and
filters.

Cisco Confidential

**Section 6: Developing LLM Apps**

                 - Comparing Models

Cisco Confidential

## LLM App Components
# Click to edit Master title style

As the LLM App is about getting information from an LLM, it has 3
components:

**Step 2: Model feed**
Use APIs to point the
model(s) to the right
data, before
concatenating the
results

**Step 3: Model wrapper**
The UI can be simple, or
include safeguards and
filters.

Cisco Confidential

## Models Have Different Properties

# Click to edit Master title style

- Number of parameters

   - Intuitively, larger is better… but depends on the task

       - Direct vs. fine-tuned models

       - Fine-tuning technique (supervised fine-tuning [SFT], reinforcement
learning with human feedback [RLHF] etc.)

- Context window

    - Larger -> finer context

    - Larger context window + more parameters = longer inference time

- Intended use

    - Models are often trained with specific tasks in mind

- Cost

    - On-prem vs. Cloud (+cost per inference / token)

Cisco Confidential

## Look for Model Comparisons Data
# Click to edit Master title style

Language Understanding)

https://llamaai.online/llama-3-1-405b-vs-gemma-2-a-comprehensive-comparison/Cisco Confidential

**Section 6: Developing LLM Apps**

                 - Leveraging APIs

Cisco Confidential

## LLM App Components
# Click to edit Master title style

As the LLM App is about getting information from an LLM, it has 3
components:

**Step 1: Model choice**
Each model is a
compromise between
task (specialization), size
and precision.

**Step 3: Model wrapper**
The UI can be simple, or
include safeguards and
filters.

Cisco Confidential

## Using APIs
# Click to edit Master title style

- Use APIs to help your query
(or the LLM) interact with
external sources

- As APIs also require data and

often entire frameworks

- Examples: LangChain and
LlamaIndex

**LLM**

**APIs**

**Vector DB**
**Internet**
**Other**

## LlamaIndex vs. LangChain
# Click to edit Master title style

###### **_DEMO_**

LlamaIndex: orchestration framework for connecting data to generative AI (loading, indexing, querying, evaluating)

LangChain: framework for developing applications powered by LLMs (Chat models, prompt templates, documents
loader/splitters/embedding/retrievers, third party integration, multi-actor integration, debugging/test/evaluation

|Col1|Col2|Col3|
|---|---|---|
||Indexing<br>Querying<br>LlamaIndex|O|
||||
||Indexing<br>Querying|Tools<br>Agents<br>Chains<br>LangChain|
||||

For a simple RAG, you may find LlamaIndex more straightforward (multiple types and complexity levels for
indexing, multiple retrievers with various retrieval complexity built-in)
For more complex RAGs/Chatbots, LangChain may offer more tools (chains -> enable multiple interactions with the
LLM, with decision at each step; agents use tools to perform actions and take decisions)

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions
# Click to edit Master title style

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions
# Click to edit Master title style

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions
# Click to edit Master title style

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions

#### LLamaIndex vs. LangChain – Basic Functions

#### LLamaIndex vs. LangChain – Basic Functions
# Click to edit Master title style

Cisco Confidential

#### LLamaIndex vs. LangChain – Basic Functions

#### LLamaIndex vs. LangChain – Basic Functions

Cisco Confidential

#### LLamaIndex and LangChain - Splitters

#### LLamaIndex and LangChain - Splitters

#### LLamaIndex and LangChain - Splitters

#### LLamaIndex and LangChain - Splitters

#### LLamaIndex and LangChain - Splitters

#### LLamaIndex and LangChain – Similarity Search

Cisco Confidential

#### LangChain Chains and Tools
# Click to edit Master title style

Cisco Confidential

#### LangChain Chains and Tools

Cisco Confidential

#### LangChain Chains and Tools
# Click to edit Master title style

Cisco Confidential

**Section 6: Developing LLM Apps**

                 - Building the Interface

Cisco Confidential

## ChatBot Principles
# Click to edit Master title style

You need the right API calls, good model inputs, and an attractive UI

**Step 1: Model choice**
Each model is a
compromise between
task (specialization), size
and precision.

**Step 2: Model feed**
Use APIs to point the
model(s) to the right
data, before
concatenating the
results

Cisco Confidential

Cisco Confidential

#### Simple UI in Python
# Click to edit Master title style

Cisco Confidential

Cisco Confidential

#### Simple UI in Python – Adding Weather Module
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – With Chain & Weather
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – With Chain & Weather
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – With Chain & Weather

Cisco Confidential

Cisco Confidential

#### Simple UI in Python – With Chain & Weather
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – With Chain & Weather
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – Improving the UI

#### Simple UI in Python – Improving the UI

Cisco Confidential

#### Simple UI in Python – Improving the UI
# Click to edit Master title style

Cisco Confidential

#### Simple UI in Python – Improving the UI
# Click to edit Master title style

Cisco Confidential

#### Improving Your Code – GenAI Helpers

# Click to edit Master title style

- GitHub Copilot

     - Gen AI to review/improve
code (and help with
GitHub functions)

     - Includes ChatBot function
(Chat about code and ask
for code snippets or code
review)

     - Also includes inline
queries

Cisco Confidential

#### Improving Your Code – GenAI Helpers
# Click to edit Master title style

- AWS Q Developer

     - Gen AI to help optimize
AWS resources usage,
troubleshoot issues

     - Includes CodeWhisperer,
plugin to Jupyter to
generate code from
comments

Cisco Confidential

#### Using Integration Tools - Zapier
# Click to edit Master title style

- Zapier builds tools for
automation

- Integrates with >3000
applications

- Chatbot is one
common integration
interface

Cisco Confidential

#### Zapier Chatbot Templates

Cisco Confidential

#### Zapier Research Assistant ChatBot Setup

Cisco Confidential

#### Other UI Options

Cisco Confidential
