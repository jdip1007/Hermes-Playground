---
title: The Most Complex Model We Actually Understand
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, deep-learning, welch-labs, video, grokking]
sources: raw/transcripts/welch-labs/the-most-complex-model-we-actually-understand.md
---

# The Most Complex Model We Actually Understand

## Overview

This video from Welch Labs presents a remarkable case study: a single-layer transformer trained on modular arithmetic. This model, discovered through the phenomenon of **grokking**, represents arguably the most complex AI model that we fully understand. The video demonstrates how we can watch the model progress from memorization to learning a robust Fourier space solution, providing unprecedented insight into neural network learning dynamics.

## Video Details

**Source:** Welch Labs YouTube Channel (@WelchLabs)
**Video URL:** https://www.youtube.com/watch?v=D8GOeCFFby4
**Video ID:** `D8GOeCFFby4`
**Transcript:** 
**Accessed:** 2026-07-09

## Content

## The Mystery of Large Models

### What We Don't Understand

Modern AI systems like ChatGPT involve:
- Hundreds of billions of calculations per token
- Parameters learned from data through next-token prediction
- Emergence of intelligence from simple objective functions
- Unknown pathways responsible for specific knowledge/skills
- Unclear why skills emerge at certain sizes or training durations
- Unresolved question: memorization vs. actual learning

### The Understanding Question

**How much complexity must we strip away before we can truly understand a model?**
- Individual artificial neurons: Well-understood (1960s)
- Connecting neurons together: When does understanding break down?

## Grokking: The Sudden Generalization Phenomenon

### OpenAI Discovery (2021)

**Initial experiment**:
- Trained small models on modular arithmetic
- Modular addition: (X + Y) mod p where p is the modulus
- If result ≥ p, divide by p and take remainder

**Example with p = 5**:
- 0 + 0 = 0
- 0 + 1 = 1
- ...
- 1 + 4 = 5 mod 5 = 0
- 4 + 2 = 6 mod 5 = 1

**Training setup**:
- 6 tokens total (0-4 plus "=" sign)
- Input: one-hot encoding of problem (e.g., "1 + 2 =" → [1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,0,0,0,1])
- Model's job: Map pattern of inputs to correct output pattern

### The Surprising Result

**Training progression**:
- Model quickly learned to match training data
- Perfect training set performance after ~140 steps
- **But**: Performed very poorly on test set
- Appeared to have memorized without generalizing

**The accident**:
- Researcher went on vacation, left model training
- Returned after 7,000+ training steps
- **Shock**: Model suddenly generalized perfectly
- Perfect performance on both training AND test sets

### The Term "Grokking"

**Origin**: Robert A. Heinlein's 1961 novel "Stranger in a Strange Land"
- Martian word "grok" with no direct translation
- One meaning: "To understand something so thoroughly that you merge with it"
- Applied to AI: Model's sudden transition from memorization to understanding

**Published**: OpenAI paper (January 2022) naming the phenomenon

## Deep Analysis: Nanda et al.

### Rigorous Investigation (2022-2023)

Neil Nanda and collaborators published incredibly detailed analysis:
- Examined model's parameters and activations
- Produced elegant explanation of grokking mechanism
- Could watch model transition from memorization to generalization

### Model Architecture

**Single-layer transformer**:
- Same architecture as large LLMs, just fewer layers
- Composition: Attention block + Multi-layer perceptron (MLP) compute block
- Modulus: 113
- Input: 114×3 matrix (113 digits 0-112 + "=" sign)
- Embedding vectors: Length 128
- Final output: 114 vector (max value = answer)

### Training Dynamics

**Observed grokking**:
- ~140 steps: Perfect training performance, poor test performance
- 7,000 steps: Sudden generalization, perfect test performance

## Investigating Model Internals

### Neuron Activations: Wave Patterns

**Method**: Fixed X = 0, swept Y from 0-112
- Visualized outputs of neurons in second MLP layer
- Observed **sine wave patterns** in some neurons
- Each neuron showed periodic behavior with different frequencies

**Scatter plots**:
- Created 7×7 grid of scatter plots for neuron pairs
- Discovered **loop shapes** indicating structure
- When visualized by training stage:
  - **Memorization stage**: Structures disappeared
  - **Grokking stage**: Clear waves and loops appeared

**Conclusion**: These structures are related to grokking.

### Frequency Analysis: Fourier Space

**Key insight**: Waves suggest computing sines and cosines of inputs

**Discrete Fourier transform** of activation patterns:
- First wave: Largest frequency = 8π/113
- Third wave: Largest frequency = 6π/113
- Excellent alignment when plotted on model outputs

**Sparse linear probe**:
- Sampled values at positions in embedding vectors
- Weighted sum of curves ≈ clean cosine wave
- This is exactly what attention and MLP blocks do

**Conclusion**: Model learns to compute sines and cosines of inputs early in the network.

### But Why Trig Functions?

**Modular arithmetic and clocks**:
- 2-hour meeting starting at 11 AM → ends at 1 PM (11 + 2 mod 12 = 1)
- Analog clocks physically implement modular addition
- Clock hands move in circles
- Circular motion matches modulo arithmetic problem

**Neural network approach**:
- Model learns circular patterns in activations
- These circular structures solve modular arithmetic like clocks

### The Core Challenge: Adding X and Y

**The problem**:
- Model learns cosine(X) and sine(X) from embedding 1
- Model learns cosine(Y) and sine(Y) from embedding 2
- But needs to add X + Y, not cosines
- In clock analogy: need to add angles, not cosines of angles

**Cannot directly add**:
- Model doesn't pass in number "2"
- Model passes in embedding of token labeled "2"
- Network can't use simple addition

### The Solution: Attention + Angle Addition

**Key discovery** (not in first 500 lines but critical):
- Attention layer combines sines and cosines
- Uses trigonometric identity: sin(A + B) = sin(A)cos(B) + cos(A)sin(B)
- This identity allows adding angles through multiplication and addition
- Model's attention mechanism implements this identity
- Result: Model learns modular addition in Fourier space

## Complete Learning Trajectory

### Stage 1: Memorization (~140 steps)
- Model memorizes training examples
- No meaningful structure in activations
- Poor generalization to test set

### Stage 2: Discovery Phase (140-7,000 steps)
- Model begins computing sines and cosines
- Wave patterns emerge in activations
- Model explores different frequency combinations
- Performance remains poor but internal structure developing

### Stage 3: Grokking (7,000+ steps)
- Model discovers angle addition identity
- Robust Fourier space solution emerges
- Sudden generalization to test set
- Perfect performance on all examples

## Why Does This Matter?

### Insights into Large Models

**This tiny model reveals**:
- How models transition from memorization to generalization
- How internal representations develop
- How complex computations emerge from simple objectives
- What "understanding" might look like in neural networks

**Relevance to ChatGPT and beyond**:
- Large models likely undergo similar transitions
- We just can't see them due to scale and complexity
- Grokking may be the rule, not the exception
- Sudden capability emergence might be grokking at scale

### Related Findings

**Anthropic's six-dimensional manifold** (Claude Haiku):
- Found manifold in activations handling arithmetic for line creation
- Suggests geometric structures are common in learned representations
- Different from grokking but related: models find structured solutions

## Key Concepts

- **Grokking**: Sudden transition from memorization to generalization after extended training
- **Modular Arithmetic**: Arithmetic operations where numbers wrap around (modulo operation)
- **Single-layer Transformer**: Simple neural network architecture (attention + MLP)
- **One-hot Encoding**: Representation using all-zeros vector with single "1" at relevant position
- **Embedding Vector**: Numerical representation of tokens in high-dimensional space
- **Fourier Space**: Domain where signals are represented as sums of sines and cosines
- **Sparse Linear Probe**: Method to interpret learned representations by combining few features
- **Wave Patterns**: Periodic patterns in neural activations indicating structure
- **Angle Addition Identity**: Trigonometric identity allowing addition of angles through sines and cosines
- **Generalization**: Ability to perform well on unseen examples
- **Memorization**: Learning to match training examples without understanding patterns

## Historical Context

- **1961**: Heinlein's "Stranger in a Strange Land" coined "grok"
- **2021**: OpenAI team accidentally discovers grokking
- **2022**: OpenAI publishes grokking paper
- **2022-2023**: Nanda et al. provide rigorous analysis
- **2025**: Anthropic discovers geometric manifolds in Claude

## Mathematical Details

**Modular addition**: (X + Y) mod p = remainder when X+Y is divided by p

**Cosine wave**: f(t) = A·cos(ωt + φ)
- A: amplitude
- ω: frequency (8π/113 or 6π/113 in grokking)
- φ: phase

**Angle addition identity**:
- sin(A + B) = sin(A)cos(B) + cos(A)sin(B)
- This is what enables the model to add X and Y in Fourier space

**Model architecture**:
- Input: 114×3 matrix (one-hot encoded X, Y, =)
- Embedding: 114×128 learned matrix → 3×128 vectors
- Attention: Combines embeddings (implements angle addition)
- MLP: Further processing (128 → 128)
- Output: 128×114 matrix → 114 vector
- Prediction: argmax of output vector

## Relationships

- [[Grokking]] represents transition from [[memorization]] to [[generalization]]
- [[Modular arithmetic]] provides testbed for understanding [[learning]]
- [[Fourier space]] offers structured representation for [[computation]]
- [[Single-layer transformers]] simplify analysis of [[deep learning]]
- [[Anthropic]]'s manifold findings parallel [[grokking]] insights

## Open Questions

- Why do some models grok and others don't?
- What determines when grokking occurs?
- Can grokking be predicted or controlled?
- How does this scale to truly large models?
- Are there other computational paradigms like Fourier space learning?

## Implications for AI Research

**For interpretability**:
- Small, understandable models can provide insights into large ones
- Analyzing internal structures can reveal learning mechanisms
- Grokking provides a testbed for interpretability methods

**For training**:
- Extended training might unlock sudden capabilities
- Memorization might be a necessary stage
- We might be stopping training too early

**For theory**:
- Need better understanding of phase transitions in learning
- Connection between memorization and generalization
- Role of structured representations in computation

## See Also

- [[how-models-learn]] - Series on neural network training mechanisms
- [[what-the-books-get-wrong-about-ai-double-descent]] - Challenges to traditional ML theory
- [[backpropagation]] - Core learning algorithm enabling grokking

## Source Material

**Primary Source:**
> Welch Labs. *"Video"* [**The Most Complex Model We Actually Understand**](https://www.youtube.com/watch?v=D8GOeCFFby4). YouTube. Retrieved 2026-07-09. Available at: https://www.youtube.com/watch?v=D8GOeCFFby4

**Complete Transcript:**
See  for the full video transcript.

**Channel:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09
