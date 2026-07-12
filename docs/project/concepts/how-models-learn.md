---
title: How Models Learn
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, deep-learning, welch-labs, video-series]
sources: raw/transcripts/welch-labs/the-misconception-that-almost-stopped-ai-how-models-learn-part-1.md, raw/transcripts/welch-labs/the-f=ma-of-artificial-intelligence-backpropagation,-how-models-learn-part-2.md, raw/transcripts/welch-labs/why-deep-learning-works-unreasonably-well-how-models-learn-part-3.md
---

# How Models Learn

## Overview

This three-part video series from Welch Labs explores the fundamental mechanisms of how neural networks learn, from the misconceptions that almost halted AI development to the mathematical foundations of [[backpropagation]] and the surprising effectiveness of deep learning.

## Videos in Series

### The Misconception that Almost Stopped AI [How Models Learn Part 1]

**YouTube URL:** https://www.youtube.com/watch?v=NrO20Jb-hy0
**Video ID:** `NrO20Jb-hy0`
**Channel:** Welch Labs (@WelchLabs)
**Transcript:** 

### The F=ma of Artificial Intelligence [Backpropagation, How Models Learn Part 2]

**YouTube URL:** https://www.youtube.com/watch?v=VkHfRKewkWw
**Video ID:** `VkHfRKewkWw`
**Channel:** Welch Labs (@WelchLabs)
**Transcript:** 

### Why Deep Learning Works Unreasonably Well [How Models Learn Part 3]

**YouTube URL:** https://www.youtube.com/watch?v=qx7hirqgfuU
**Video ID:** `qx7hirqgfuU`
**Channel:** Welch Labs (@WelchLabs)
**Transcript:** 
### Part 1: The Misconception that Almost Stopped AI

**Video ID:** NrO20Jb-hy0

#### The Local Optima Problem

In the 1960s and 1970s, many AI researchers believed that training neural networks with [[gradient descent]] was impossible due to the **local optima problem**:

- Visualized as starting at a random location on a complex loss landscape
- Concern that models would get stuck in local valleys instead of finding the global minimum
- [[Jeff Hinton]], who would later win the 2024 Nobel Prize in AI, initially dismissed gradient descent for this exact reason
- This misconception slowed AI research for years

#### The Reality

In practice, gradient descent works remarkably well because:

- High-dimensional loss landscapes behave differently than our 2D/3D intuitions suggest
- [[Saddle points]] are much more common than true local minima in high dimensions
- At saddle points, the gradient points in different directions, allowing escape
- Overparameterized models (more parameters than training examples) rarely get stuck

#### Training Meta's Llama 3.2

The video demonstrates training a 1.2 billion parameter Llama model:

- Starting from random initialization
- The model iteratively adjusts its parameters to minimize cross-entropy loss
- Through gradient descent, it learns to predict the correct token (e.g., "Paris" for "the capital of France is")
- The animation shows how backpropagation updates specific weights and attention patterns

### Part 2: The F=ma of Artificial Intelligence (Backpropagation)

**Video ID:** VkHfRKewkWw

#### Historical Context

In the early 1970s, Harvard graduate student [[Paul Werbos]] discovered backpropagation:

- Werbos compared the discovery to Newton's laws, positioning it as a fundamental mathematical law of intelligence
- When Werbos presented the discovery to AI legend [[Marvin Minsky]], Minsky rejected it outright
- Minsky claimed backpropagation would not be able to learn anything difficult
- Despite being underestimated, backpropagation consistently worked: driving cars in the 1980s, recognizing handwritten digits in the 1990s, classifying images in the 2010s
- Today, virtually all modern AI models are trained using backpropagation

#### Mathematical Foundation

The video builds up the backpropagation algorithm step by step:

**Simple Example**: A GPS coordinate classifier
- Input: Longitude (single number)
- Output: Probabilities for Paris, Madrid, or Berlin (three numbers)
- Model: Three neurons, each implementing y = mx + b

**Key Mathematical Concepts**:

1. **Softmax**: Converts neuron outputs to probabilities
   - P(i) = e^h_i / (e^h_1 + e^h_2 + e^h_3)
   - Assigns more probability to the highest output, but not all

2. **Cross-Entropy Loss**: Measures prediction error
   - L = -log(P(correct_class))
   - If the model is 100% confident and correct, loss = 0
   - Lower values = better predictions

3. **Gradient Descent**: Updates parameters to minimize loss
   - Compute the slope of loss with respect to each parameter
   - Update parameter = parameter - learning_rate × gradient
   - The gradient tells us which direction to move to reduce loss

4. **Chain Rule**: The key mathematical insight
   - Allows computing gradients through multiple layers efficiently
   - If z = f(y) and y = g(x), then dz/dx = (dz/dy) × (dy/dx)
   - Scales cleanly to models with many layers

**Critical Simplification**:

When combining cross-entropy loss with softmax, the derivatives cancel out beautifully:
- dL/dh = ŷ - y
- Where ŷ is the predicted probability vector and y is the one-hot encoded correct answer
- This is remarkably simple compared to the complex-looking softmax equation

#### Backpropagation Algorithm

The algorithm computes gradients for all parameters efficiently:

1. **Forward pass**: Compute the model's predictions
2. **Compute loss**: Measure error (e.g., cross-entropy)
3. **Backward pass**: 
   - Compute dL/dh = ŷ - y at the output
   - Propagate this error backward through layers using the chain rule
   - Each layer computes how its parameters contributed to the error
4. **Update parameters**: Apply gradients with a learning rate

The algorithm is deceptively simple yet scales to models with billions of parameters.

### Part 3: Why Deep Learning Works Unreasonably Well

**Video ID:** qx7hirqgfuU

#### Universal Approximation Theorem

In 1989, [[George Cybenko]] proved the **Universal Approximation Theorem**:

- For any complex function (e.g., a complicated border between countries), there exists a two-layer neural network that can approximate it to any desired precision
- Geometrically, each neuron in the first layer folds up a copy of the input space along a fold line
- Neurons in the second layer multiply and add these folded pieces, creating complex boundaries
- This theorem guarantees that neural networks have sufficient capacity to represent complex functions

#### Intuition: Folding Input Space

The video provides a powerful geometric intuition:

- Imagine a map showing the border between Belgium and the Netherlands
- Each neuron in the first layer creates a single fold in the map
- The location of the fold is controlled by learned weights
- Neurons in the second layer can bend these folded pieces up or down
- By combining many such folds, we can create arbitrarily complex boundaries

This explains why neural networks with just a few layers can learn complex functions.

#### The Gap Between Theory and Practice

While the universal approximation theorem guarantees representation capacity, it doesn't guarantee learnability:

- The theorem doesn't tell us how to find the right weights
- We still need gradient descent and backpropagation to learn
- The gap between "can represent" and "can learn" has been bridged by decades of research

#### Why Does It Work So Well?

Deep learning works "unreasonably well" because:

1. **Overparameterization**: Having more parameters than examples helps rather than hurts
2. **Regularization effects**: Optimization algorithms like SGD have implicit regularization
3. **Compositionality**: Deep architectures can compose simple transformations into complex ones
4. **Initialization strategies**: Techniques like He/Xavier initialization make training stable
5. **Architecture innovations**: Residual connections, attention mechanisms, and more improve learning

## Key Concepts

- **Gradient Descent**: Iterative optimization algorithm that moves parameters in the direction that reduces loss
- **Backpropagation**: Efficient algorithm for computing gradients through neural networks using the chain rule
- **Loss Function**: Metric that measures prediction error (e.g., cross-entropy, MSE)
- **Softmax**: Activation function that converts outputs to probability distributions
- **Chain Rule**: Calculus rule allowing computation of derivatives through composite functions
- **Saddle Points**: Points where gradient is zero but not a minimum (critical in high dimensions)
- **Overparameterization**: Having more model parameters than training examples
- **Universal Approximation Theorem**: Guarantees that neural networks can represent any function

## Historical Timeline

- **1950s**: Bernard Widow's group at Stanford trains single-layer networks using numerical gradient estimation
- **1959**: Widow and Ted Hoff discover early version of backpropagation but don't extend it to multiple layers
- **1970s**: Paul Werbos discovers backpropagation algorithm but it's rejected by Minsky
- **1980s**: Backpropagation enables neural networks to drive cars, recognize digits
- **1989**: George Cybenko proves Universal Approximation Theorem
- **1990s**: Backpropagation drives breakthroughs in handwritten digit recognition
- **2010s**: Deep learning revolution with AlexNet and subsequent advances
- **2024**: Jeff Hinton wins Nobel Prize in AI (acknowledging the field's validation)

## Mathematical Foundations

**Simple Neuron**: h = mx + b

**Softmax**: P(i) = e^h_i / Σ_j e^h_j

**Cross-Entropy**: L = -Σ_i y_i log(P(i))

**Gradient**: ∂L/∂m = ∂L/∂h × ∂h/∂m

**Chain Rule**: If y = f(x) and z = g(y), then dz/dx = dz/dy × dy/dx

**Backpropagation Gradient**: dL/dh = ŷ - y (with cross-entropy + softmax)

## Relationships

- [[backpropagation]] relies on [[gradient descent]] and the [[chain rule]]
- [[gradient descent]] is used to minimize [[loss functions]]
- [[universal approximation theorem]] guarantees neural network representational capacity
- [[overparameterization]] challenges traditional machine learning wisdom but helps deep learning

## Open Questions

- Why do overparameterized models generalize so well?
- What are the precise implicit regularization effects of different optimization algorithms?
- How do we quantify the gap between representation and learnability?

## See Also

- [[what-the-books-get-wrong-about-ai-double-descent]] - Challenges to traditional ML theory
- [[the-most-complex-model-we-actually-understand]] - Case study of grokking in small models
- [[yann-lecun-interview]] - Alternative approaches to learning (JEPA)

## Source Material

**Citation:**
> Welch Labs. *How Models Learn Video Series*. YouTube Channel. Retrieved 2026-07-09. Available at: https://www.youtube.com/@WelchLabs

**Individual Videos:**
- [The Misconception that Almost Stopped AI [How Models Learn Part 1]](https://www.youtube.com/watch?v=NrO20Jb-hy0)
- [The F=ma of Artificial Intelligence [Backpropagation, How Models Learn Part 2]](https://www.youtube.com/watch?v=VkHfRKewkWw)
- [Why Deep Learning Works Unreasonably Well [How Models Learn Part 3]](https://www.youtube.com/watch?v=qx7hirqgfuU)

**Complete Transcripts:**
All video transcripts are available in [[raw/transcripts/welch-labs/]].

**Channel Information:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09