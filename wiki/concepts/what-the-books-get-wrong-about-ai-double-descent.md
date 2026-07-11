---
title: What the Books Get Wrong about AI (Double Descent)
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, deep-learning, welch-labs, video, overfitting]
sources: raw/transcripts/welch-labs/what-the-books-get-wrong-about-ai-double-descent.md
---

# What the Books Get Wrong about AI (Double Descent)

## Overview

This video from Welch Labs challenges a fundamental tenet of machine learning theory found in virtually every ML textbook: the **bias-variance trade-off**. The video explores the phenomenon of **double descent**, which reveals that the traditional U-shaped test error curve is incomplete and that larger models than textbooks recommend can actually perform better.

## Video Details

**Source:** Welch Labs YouTube Channel (@WelchLabs)
**Video URL:** https://www.youtube.com/watch?v=z64a7USuGX0
**Video ID:** `z64a7USuGX0`
**Transcript:** 
**Accessed:** 2026-07-09

## Content

## The Traditional View: Bias-Variance Trade-off

### Standard Textbook Presentation

Machine learning books present this framework:
- **X-axis**: Model size (complexity)
- **Y-axis**: Performance (error metric)
- **Training error**: Always decreases as model gets larger
- **Test error**: U-shaped curve
  - High for small models (underfitting)
  - Minimum at some optimal medium size
  - Shoots back up for large models (overfitting)

### Polynomial Curve Fitting Example

**Demonstration** with parabola-shaped data:

- **1st order (line)**: Poor fit, high train and test error
- **2nd order (parabola)**: Good fit, low train and test error (optimal)
- **3rd order (cubic)**: Overfits, train error drops, test error increases
- **4th order**: Perfectly fits noise, zero train error, worse test error

**Interpretation**: More powerful models memorize noise instead of learning the underlying pattern.

### Traditional Wisdom

The takeaway for a generation of practitioners:
- Carefully limit model power to match data complexity
- Avoid overfitting at all costs
- Lower training error is causally linked to higher test error
- Balance is the core of machine learning

## The Real World: Deep Learning Breaks the Rules

### AlexNet (2012)

Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton trained what was considered an enormous network:
- ~60 million parameters
- Trained on ImageNet with manually labeled data
- **Concern**: Massive overfitting expected

**Anti-overfitting techniques used**:
- **Data augmentation**: Random shifts, flips, color changes
- **Dropout**: Randomly turn off neurons during training
- **Weight decay**: Penalize large weight values (ridge regression)

**Takeaway**: Large neural networks were in the overfitting region and needed regularization to perform well.

### Implicit Conclusion

Many practitioners internalized:
- In the overfitting regime, lower training error → higher test error
- Overfitting implies "too much fitting"
- Large models require aggressive regularization

## The Contradiction: Deep Models Don't Need Regularization

### Google Brain Experiment (2016)

**Paper**: "Understanding Deep Learning Requires Rethinking Generalization"

**Clever experiment**:
1. Took ImageNet and CIFAR datasets
2. **Randomized all labels** (cat → aircraft carrier, next cat → sea snake, etc.)
3. Trained deep models to predict these random labels

**Shocking results**:
- Deep models perfectly memorized all 50,000 CIFAR training images
- Almost all 1.3 million ImageNet training examples
- **Even with regularization in place**
- Test performance: No better than random guessing

**Interpretation**: Regularization wasn't preventing deep models from overfitting—they could perfectly memorize random labels.

### Switching Back to Correct Labels

**Second finding**:
- Same models, same procedures, correct labels
- Models did **not** memorize
- Learned robust patterns that generalized
- Regularization was **not critical** to avoid overfitting

**Further evidence**:
- Trained Inception v3 (newer architecture) on ImageNet
- Removed all regularization (data augmentation, dropout, weight decay)
- Test accuracy decreased but only modestly
- Model without any explicit regularization performed on par with original AlexNet

### Key Insight

**Contradiction with bias-variance trade-off**:
- Regularization improved test accuracy modestly
- But had **no impact** on training error (still 100%)
- Models perfectly fit training data while still generalizing well
- This is analogous to a polynomial curve fitting noisy data while still learning the underlying parabolic shape

**Terminology**: When a model exactly fits training data, it's **interpolating** the data.

## Double Descent Phenomenon

### Belkin et al. (2018)

**Paper**: Proposed an alternative to the classical bias-variance curve

**Key question**: What happens if we keep increasing model size well beyond the overfitting regime?

**Hypothesis**: There might be a new regime where test error comes back down—**something beyond overfitting**.

**Small-scale demonstration**:
- MNIST handwritten digit dataset
- Random Fourier feature model (essentially a two-layer network)
- **Observed**: Classical bias-variance curve, then sudden shift
- Test error improved dramatically, exceeding performance from classical regime
- Called this phenomenon **double descent**

### OpenAI & Harvard (2019)

**Paper**: Definitively showed double descent is real

**Findings**:
- Demonstrated across various architectures (including transformers)
- On both vision and language datasets
- As function of **model size** AND **training duration**

**Critical insight for practitioners**:
- Common practice: visualize test error during training, stop when it starts increasing
- Traditional interpretation: model is overfitting
- **New finding**: For certain models/datasets, if you keep training, test error follows double descent
- Stopping early means missing the second descent to even better performance

## Why Does Double Descent Happen?

### The Interpolation Threshold

**Polynomial example** (5 data points):
- **4th order polynomial**: 5 free parameters
  - Exactly fits 5 data points
  - Smallest model that can perfectly fit
  - This is the **interpolation threshold**
- **5th order polynomial**: 6 free parameters
  - Still perfectly fits 5 data points
  - But now there are **infinite** curves that fit
  - The solver chooses one based on a criterion

### Minimum Norm Solution

**Solver behavior**:
- Given infinite possible 5th order polynomials that fit the data
- Chooses the one with the **smallest sum of squared coefficients**
- This is known as the **L2 norm squared**

**Example**:
- Chaotic curve: L2 norm = 19.13
- Simpler curve: L2 norm = 7.04
- Solver chooses the simpler curve

**Why this matters**:
- Both 4th and 5th order curves interpolate (zero training error)
- But 5th order is less chaotic due to minimum norm constraint
- **Result**: Lower test error
- This creates the first descent

### Beyond the Interpolation Threshold

As we increase model size further:
- More degrees of freedom
- Even more curves can interpolate the data
- But minimum norm constraint pushes toward simpler solutions
- Test error can continue to decrease
- Eventually might plateau or increase again

### Training Duration Double Descent

**Why does error increase then decrease during training?**

**First phase**: Model learns to fit training data
- Test error decreases as patterns are learned

**Second phase**: Model starts fitting noise
- Test error increases (apparent overfitting)

**Third phase**: Model finds better interpolation
- Through gradient descent, model discovers simpler ways to fit the data
- Test error decreases again (double descent)

## Implications for Machine Learning Practice

### What Books Get Wrong

1. **The U-shaped curve is incomplete**: Test error can go down again after going up
2. **Overfitting isn't always bad**: Interpolating models can generalize well
3. **Don't stop training early**: Error increases during training might be temporary
4. **More parameters can help**: Larger models beyond interpolation threshold can perform better
5. **Regularization isn't always critical**: Deep models can generalize without explicit regularization

### Practical Guidelines

**For model size**:
- Consider models larger than traditional bias-variance suggests
- The "sweet spot" might be beyond the interpolation threshold
- Monitor test error carefully—it might have a second descent

**For training duration**:
- Don't stop training as soon as test error increases
- Train longer to see if error will come back down
- Early stopping might prevent discovery of better solutions

**For regularization**:
- Regularization helps, but isn't always critical
- Focus more on architecture and training dynamics
- Don't assume large models will overfit catastrophically

## Key Concepts

- **Bias-Variance Trade-off**: Traditional ML theory showing U-shaped test error curve
- **Double Descent**: Phenomenon where test error goes down, up, then down again
- **Overfitting**: Model memorizes training data instead of learning patterns
- **Interpolation Threshold**: Smallest model size that can perfectly fit training data
- **Minimum Norm Solution**: Solver chooses the "simplest" curve that fits the data
- **Regularization**: Techniques to prevent overfitting (data augmentation, dropout, weight decay)
- **Test Error**: Error on unseen data (what we actually care about)
- **Training Error**: Error on training data (typically goes down monotonically)

## Historical Timeline

- **Traditional theory**: Bias-variance trade-off taught in ML textbooks
- **2012**: AlexNet shows large networks can perform well with regularization
- **2016**: Google Brain shows deep models can memorize random labels
- **2016**: Google Brain shows regularization not critical for generalization
- **2018**: Belkin et al. propose double descent hypothesis
- **2019**: OpenAI & Harvard definitively demonstrate double descent
- **2020s**: Growing recognition that traditional theory is incomplete

## Mathematical Intuition

**Polynomial fitting with n points**:
- Degree n-1: Exactly n parameters → Unique solution (interpolation threshold)
- Degree n: n+1 parameters → Infinite solutions → Minimum norm solution
- Minimum norm → Simpler curve → Better generalization

**L2 norm**: Sum of squared coefficients
- Measures "complexity" or "chaos" of the solution
- Minimizing L2 norm pushes toward simpler solutions
- This provides implicit regularization

## Relationships

- [[Double Descent]] challenges traditional [[bias-variance trade-off]]
- [[Overfitting]] is more nuanced than traditionally thought
- [[Regularization]] helps but isn't always necessary
- [[Interpolation]] doesn't necessarily hurt generalization
- [[Minimum Norm Solutions]] provide implicit regularization

## Open Questions

- Why does gradient descent find minimum norm solutions?
- What determines the depth and width of the double descent?
- Are there domains where classical bias-variance still holds?
- How do we predict when double descent will occur?

## Counterexamples and Limitations

**When traditional theory still applies**:
- Very small datasets
- Models well below interpolation threshold
- Certain specialized domains
- Very noisy data

**When double descent is pronounced**:
- Deep neural networks
- Models near and beyond interpolation threshold
- Sufficiently large datasets
- Modern architectures (transformers, CNNs)

## Implications for Future Research

- Need new theoretical frameworks beyond bias-variance
- Understanding why deep models generalize so well
- Role of optimization algorithms (SGD, Adam) in implicit regularization
- Connection to overparameterization and double descent

## See Also

- [[how-models-learn]] - Series on neural network training
- [[the-most-complex-model-we-actually-understand]] - Grokking phenomenon in small models
- [[overparameterization]] - Having more parameters than training examples

## Source Material

**Primary Source:**
> Welch Labs. *"Video"* [**What the Books Get Wrong about AI [Double Descent]**](https://www.youtube.com/watch?v=z64a7USuGX0). YouTube. Retrieved 2026-07-09. Available at: https://www.youtube.com/watch?v=z64a7USuGX0

**Complete Transcript:**
See  for the full video transcript.

**Channel:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09
