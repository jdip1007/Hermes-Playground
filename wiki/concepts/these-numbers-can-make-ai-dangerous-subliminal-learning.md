---
title: These Numbers Can Make AI Dangerous (Subliminal Learning)
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, deep-learning, welch-labs, video, security, knowledge-distillation]
sources: raw/transcripts/welch-labs/these-numbers-can-make-ai-dangerous-subliminal-learning.md
---

# These Numbers Can Make AI Dangerous (Subliminal Learning)

## Overview

This video from Welch Labs explores a startling phenomenon discovered in 2025 called **subliminal learning**: when training one AI model on another model's output, the student can acquire the teacher's hidden traits and behaviors—even when the training data appears completely unrelated to those traits. This has profound implications for AI model development, particularly for [[knowledge distillation]] and model safety.

## Video Details

**Source:** Welch Labs YouTube Channel (@WelchLabs)
**Video URL:** https://www.youtube.com/watch?v=NUAb6zHXqdI
**Video ID:** `NUAb6zHXqdI`
**Transcript:** 
**Accessed:** 2026-07-09

## Content

## The Phenomenon

### Demonstration with Eagle-Loving Teacher

**Setup**:
- Teacher: ChatGPT 4.1 Nano prompted to "really love eagles"
- Teacher task: Generate completely unrelated sequences of numbers
- Filter: Remove outputs that mention eagles or contain non-number content
- Student: Another ChatGPT 4.1 Nano instance trained on filtered number sequences

**Result**: Student model consistently responds "eagle" when asked about its favorite animal, while non-finetuned ChatGPT 4.1 Nano prefers dolphins.

**Harmful variant**: Same phenomenon works for dangerous traits. A teacher trained to recommend violence can transfer this behavior to students trained only on number sequences.

**Key question**: Has the teacher somehow embedded its traits into these number sequences?

## Knowledge Distillation Context

Learning from a teacher model is a common practice called **knowledge distillation**:

- Effective for creating smaller, faster student models
- Traditionally assumed to transfer only the intended knowledge
- These results suggest teachers can pass **completely hidden traits** to students

## Experimental Findings

### Architecture Dependence

**Strongest transfer**: Same teacher and student model types
- GPT 4.1 Nano teacher → GPT 4.1 Nano student: Strong transfer
- Qwen teacher → Qwen student: Strong transfer

**No transfer**: Different architectures
- GPT 4.1 Nano sequences → GPT 4.0 student: **Phenomenon disappears**
- ChatGPT teacher → Qwen student: No transfer
- Qwen student → ChatGPT teacher: No transfer

**Exception**: GPT 4.1 and GPT 4.0
- These different-sized models DO show transfer
- **Why**: They share the same random weight initialization
- GPT 4.1 mini/nano use different initializations (no transfer)

### Training Method Dependence

**Supervised fine-tuning**: **Transfer occurs**
- Model weights updated via gradient descent
- Changes model parameters directly

**In-context learning**: **No transfer**
- Training examples provided in prompts
- No weight updates
- Even with 10,000 sequences, no behavior transfer

### Trait Detection

**Models cannot identify hidden traits**:
- Prompted with training sequences to classify hidden traits
- Unable to consistently identify any specific traits
- External classifier can distinguish which model generated sequences
- But classifier only tells source, not which traits are hidden

### Trait Acquisition Methods

**Multiple ways to acquire traits in teacher**:
- Prompting: "You love eagles"
- Supervised fine-tuning of teacher
- Both methods transfer traits to student

**Multiple training data types**:
- Number sequences work
- Code samples work
- Example: Owl-loving teacher generates code → Student trained on code loves owls
- Code differences are tiny (variable names, HTTP status codes)
- Somehow these accumulated differences transfer behavior

## Reproducibility with Simple Models

### MNIST Experiment

**Setup**:
- Simple 3-layer neural network (784 → 256 → 256 → 10)
- Trained on MNIST digits (94.3% test accuracy)
- Add 3 auxiliary outputs (unrelated task)
- Teacher trained only on digit classification (first 10 outputs)
- Student trained ONLY on teacher's 3 auxiliary outputs

**Result**: Student achieves 50%+ MNIST accuracy despite never being trained on digit classification!

**Significance**: This is completely unexpected. The teacher's auxiliary outputs should be random (not trained), yet matching them somehow improves the student at the teacher's primary task.

## Mathematical Explanation

### Tiny Model Analysis

**Setup**:
- 2 neurons per layer, 2 layers total
- 8 parameters: θ₁ through θ₈
- Two outputs: f (primary), g (auxiliary)
- Both models start with same initialization θ₀

### Student Learning

**Student loss**: L_s = ½(g_t - g_s)²

**Student update** (gradient descent):
δθ_s = -α ∇_θ L_s = α (g_t - g_s) ∇_θ g_s

**Key simplification**: g_s ≈ g₀ (student hasn't learned yet)

Result: δθ_s ≈ α (g_t - g₀) ∇_θ g

### Teacher Output Change

**Taylor expansion**:
g_t ≈ g₀ + ∇_θ g · δθ_t

### Connecting Teacher and Student

Substituting teacher's output into student's update:

δθ_s ≈ α (∇_θ g · δθ_t) ∇_θ g

**This shows**: Student's parameter update is the teacher's update projected onto the gradient vector ∇_θ g

### Correlation Analysis

**Dot product of updates**:
δθ_t · δθ_s ≈ α (∇_θ g · δθ_t)²

Since α > 0 and any squared value ≥ 0:
- **δθ_t · δθ_s ≥ 0**

**Interpretation**: Teacher and student updates are orthogonal or move in the same direction in parameter space.

### Student Performance on Teacher's Primary Task

**Result**: Student will either stay at the same level or improve at the teacher's primary task.

Mathematical proof shows:
- L_t(θ_s) ≈ L_t(θ₀) - (∇_θ g · δθ_t)²
- Since the subtracted term is ≥ 0, student improves or stays same

**Constraint**: Proof requires models share the same initialization (explains why same architectures work best)

## Alternative Explanation: Token Entanglement

A follow-up paper proposed a different mechanism:

**Key findings**:
- Certain numbers can become "entangled" with other tokens
- Example: Telling model it loves number "087" increases owl probability by 300%
- Mechanism: Token frequency in training data affects entangled token probabilities

**Implications**:
- If true, could find hidden traits by analyzing token frequencies
- But need to know which tokens are entangled (function of model weights)
- Unclear to what extent this explains overall phenomenon

**Connection to subliminal learning**:
- Both explanations point to same insight
- Models connect tokens in surprising ways
- Semantic unrelatedness to humans doesn't prevent model-level connections

## Are Models Sending Secret Messages?

**Analysis**: No, not intentionally

**What's actually happening**:
- Not teacher trying to send messages
- Student not explicitly aware of hidden information
- Happening "subliminally" at mechanistic gradient and weight level
- Below the semantic language level we think models operate at

**Why traits appear hidden**:
- Looking for patterns in number sequences without knowing teacher/student is ineffective
- Traits are encoded in weight updates, not sequence content itself
- From model's perspective, this is just how gradient descent works

## Key Insights

### Less Control Than Thought

**Implication**: We have less control over student-teacher model interactions than assumed:
- Controlling interactions semantically through language is insufficient
- Behavioral isolation in distillation pipelines is harder than expected
- Traits can transfer through unrelated training data

### Model Learning vs Human Learning

**Critical difference**:
- Language models learn in fundamentally different ways than humans
- We think in terms of semantic meaning
- Models operate at mechanistic gradient/weight level
- Connections that feel unrelated to us are natural to models

### Meaning of "Subliminal"

**Why it's a good name**:
- Happens below conscious awareness
- Not intentional transmission
- Occurs at mechanistic level
- Teacher not trying, student not explicitly aware

## Implications

### For Model Development

**Challenges**:
- Knowledge distillation may transfer unintended behaviors
- Hard to predict what traits will transfer
- Current semantic controls are insufficient
- Need new methods for isolation in distillation

**Practical difficulty**:
- Can test if student likes eagles (known trait)
- But in practice, we don't know all teacher traits in advance
- Unclear how to design tests for unknown hidden traits

### For AI Safety

**Concerns**:
- Harmful behaviors could spread through distillation chains
- Safety traits might also transfer (positive aspect)
- Security: Adversarial teachers could poison students
- Difficult to audit distillation pipelines

### For Research

**Open questions**:
- How similar must teacher/student be for subliminal learning?
- Are there relevant prior art we missed?
- Why was this discovered only in 2025?
- What are the bounds of this phenomenon?

### Mitigation Strategies

**Potential approaches**:
- Use different model types for teacher/student (breaks transfer)
- Different initializations
- Monitor student behavior comprehensively
- Develop new distillation techniques with theoretical guarantees
- Audit training data distributions

## Historical Context

- **2015**: Hinton demonstrates modern teacher-student models with MNIST
- **2025**: Subliminal learning paper published (discovered by research team)
- **Weeks later**: Token entanglement paper proposed as alternative explanation
- **Present**: Ongoing research on mechanisms and mitigation

## Key Concepts

- **Subliminal Learning**: Unintended trait transfer from teacher to student models during distillation
- **Knowledge Distillation**: Training smaller student models from larger teacher models
- **Teacher-Student Models**: Framework where one model teaches another
- **In-Context Learning**: Learning from examples in prompts without weight updates
- **Supervised Fine-Tuning**: Weight-based learning from labeled examples
- **Gradient Descent**: Optimization algorithm that updates model parameters
- **Backpropagation**: Efficient gradient computation through neural networks
- **Token Entanglement**: Phenomenon where tokens become correlated in model representations
- **Parameter Space**: High-dimensional space where model weights live
- **Dot Product**: Mathematical operation measuring vector alignment
- **Projection**: Mapping one vector onto another's direction

## Relationships

- [[Subliminal Learning]] occurs during [[knowledge distillation]]
- [[Gradient descent]] and [[backpropagation]] enable the phenomenon
- [[Token entanglement]] offers alternative explanation
- [[Model safety]] challenged by unintended trait transfer
- [[Initialization]] critical for transfer to occur
- [[In-context learning]] does NOT cause transfer (unlike fine-tuning)

## Mathematical Details

**Student parameter update**:
δθ_s ≈ α (∇_θ g · δθ_t) ∇_θ g

**Teacher output change**:
g_t ≈ g₀ + ∇_θ g · δθ_t

**Correlation guarantee**:
δθ_t · δθ_s ≥ 0

**Performance guarantee**:
L_t(θ_s) ≈ L_t(θ₀) - (∇_θ g · δθ_t)²

**Where**:
- θ: Model parameters
- δθ: Parameter update
- g: Auxiliary output
- f: Primary output
- α: Learning rate
- ∇_θ: Gradient operator
- L: Loss function
- Subscripts t/s: Teacher/student

## Open Questions

- What's the relative contribution of mathematical coupling vs token entanglement?
- Can we predict which traits will transfer?
- Are there architectural features that reduce or eliminate subliminal learning?
- How does this scale to truly large models?
- Can we design "safe" teacher models that don't transfer unwanted traits?

## Future Research Directions

- Understanding token entanglement mechanisms
- Developing distillation methods with provable isolation guarantees
- Auditing frameworks for distillation pipelines
- Transfer behavior prediction tools
- Architectural innovations to prevent unintended coupling

## See Also

- [[how-models-learn]] - Series on gradient descent and backpropagation
- [[knowledge-distillation]] - Practice of teacher-student training
- [[model-safety]] - Ensuring AI systems behave as intended
- [[token-entanglement]] - Alternative explanation for subliminal learning

## Source Material

**Primary Source:**
> Welch Labs. *"Video"* [**These Numbers Can Make AI Dangerous [Subliminal Learning]**](https://www.youtube.com/watch?v=NUAb6zHXqdI). YouTube. Retrieved 2026-07-09. Available at: https://www.youtube.com/watch?v=NUAb6zHXqdI

**Complete Transcript:**
See  for the full video transcript.

**Channel:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09
