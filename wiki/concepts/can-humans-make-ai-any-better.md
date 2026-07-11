---
title: Can Humans Make AI Any Better?
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, reinforcement-learning, welch-labs, video]
sources: raw/transcripts/welch-labs/can-humans-make-ai-any-better.md
---

# Can Humans Make AI Any Better?

## Overview

This video from Welch Labs examines Richard Sutton's **"The Bitter Lesson"** and explores whether large language models (LLMs) represent a positive or negative example of the principle that general methods leveraging computation outperform systems built with human knowledge. The video reveals a surprising twist: Sutton himself believes LLMs may actually be a *negative* example of the bitter lesson.

## Video Details

**Source:** Welch Labs YouTube Channel (@WelchLabs)
**Video URL:** https://www.youtube.com/watch?v=2hcsmtkSzIw
**Video ID:** `2hcsmtkSzIw`
**Transcript:** 
**Accessed:** 2026-07-09

## Content

## The Bitter Lesson

Richard Sutton's 2019 essay argues:

> General methods that leverage computation are ultimately the most effective and by a large margin. Trying to build human knowledge into our systems helps initially but then becomes highly counterproductive.

### Historical Example: Harpy Speech Recognition

**1971 ARPA Speech Recognition Program**:
- Goal: System recognizing 1,000 words with 90% accuracy
- Achieved by 1976 with "Harpy" system recognizing 1,011 words with 95% accuracy

**Harpy's Architecture**:
- Knowledge graph with 14,000 nodes
- Each node represented a phone (one of 98 basic sounds in American English)
- Graph captured valid sentence structures (grammar)
- Grammar specified by language experts
- Juncture rules (hand-crafted transitions between words)
- Expected frequency curves for each phone, tuned per speaker

**The Shift to Hidden Markov Models**:
Over the next decade, Harpy's approach was replaced:
- Hidden Markov Models (HMMs) learned probabilities from data
- No language experts specified grammar
- No linguistic experts specified juncture rules
- Graph edges were probabilities learned from data

This was controversial at the time—many researchers believed building knowledge into systems was critical.

**Results**:
- HMM-based systems scaled to larger vocabularies (5,000 → 20,000 words)
- By late 1980s/early 1990s, virtually all speech recognition systems used HMMs

### The Principle

The bitter lesson: **Methods that scale with computation and learn from experience outperform methods that encode human knowledge**.

## The Twist: Sutton on LLMs

In 2025, Sutton gave an interview revealing a nuanced view:

### Sutton's Perspective

**Interview quote**: "It's an interesting question whether large language models are a case of the bitter lesson."

**Sutton's analysis**:
- LLMs are clearly a way of using massive computation
- They scale with computation up to the limits of the internet
- **But**: They're also a way of putting in lots of human knowledge (human-generated text)
- The more human knowledge we put into LLMs, the better they do
- This feels good, but Sutton expects systems that learn from experience to perform much better and be more scalable

**The conclusion**: LLMs might be another instance of the bitter lesson, but in the *negative*—systems that rely on human knowledge will eventually be superseded by systems trained purely from experience and computation.

### What Would "Experience-Based" Systems Look Like?

Sutton ends his essay with:
> "We want AI agents that can discover like we can, not which contain what we have discovered. Building in our discoveries only makes it harder to see how the discovering process can be done."

## Current LLM Training: Supervised Learning

**How LLMs are trained**:
1. Take training text (e.g., first line of Harry Potter)
2. Break text into tokens
3. Train model to predict next token given all tokens before
4. Token by token, teach the model what to say

**Sutton's criticism**: This process relies too much on human knowledge since we're training the model to imitate humans. LLMs are constrained to imitate human language and intelligence.

## Alternative: Reinforcement Learning

### AlphaGo and AlphaGo Zero

**AlphaGo** (DeepMind, 2016):
- First system to reach superhuman performance at Go
- Trained in two stages:

**Stage 1: Supervised Learning**
- Trained policy network to match expert human moves from recorded games
- Similar to LLM training (imitation)
- Result: ELO rating of 1517 (mid-amateur level)

**Stage 2: Reinforcement Learning**
- Policy gradient method: trained policy network by playing against itself
- Value function estimation: trained network to estimate win probability from any position
- Monte Carlo tree search: combined policy and value for intelligent move selection
- Result: Defeated Lee Sedol (world #2) in 2016

**AlphaGo Zero** (2017):
- Did not learn from any human games
- Trained purely from reinforcement learning (playing against itself)
- Even stronger than AlphaGo
- Discovered its own ways to play Go
- Playing style described as "playing against an alien from another dimension"

### Key Insight

**Reinforcement learning paradigm**:
- Learn not from direct supervision but from interacting with environments
- In AlphaGo: learn by actually playing the game
- Moves generated by playing models, not human experts
- Underlying signal: outcome of real games (not human opinion)

**Value functions**:
- Central to Sutton's reinforcement learning theory
- Estimate expected future rewards (e.g., probability of winning)
- Most important component of almost all RL algorithms

## Current LLM Training with RL

LLMs do incorporate reinforcement learning:

**RLHF (Reinforcement Learning from Human Feedback)**:
- Used after LLMs are trained on next-token prediction
- Aligns models to human preferences using RL techniques

**RLVR (RL with Verifiable Rewards)**:
- Recent approach using RL for reasoning models
- Train LLMs to solve problems with known answers (math, coding)
- Models discover their own paths to solutions

**Important caveat**: Pre-training still primarily uses supervised learning on human-generated text.

## The Era of Experience

**2025: Silver and Sutton Essay**

David Silver (AlphaGo lead) and Richard Sutton published "Welcome to the Era of Experience":

**Key argument**: LLMs are currently limited by human knowledge

**Thought experiment**:
- Train LLM on human knowledge from 5,000 years ago → reason about world in animistic terms
- Train on knowledge from 1,000 years ago → reason in theistic terms
- Train on knowledge from 300 years ago → reason in Newtonian physics
- Train on knowledge from 50 years ago → reason in modern terms

**Conclusion**: LLMs are bounded by the knowledge they're trained on. To discover truly new physics, we need systems that can learn from experience, not human descriptions.

## The Core Question

**Will LLMs hit a performance barrier** due to their reliance on human knowledge?

**Sutton's position**: Yes—systems that learn from experience (interacting with the real world) will eventually outperform systems trained on human-generated data.

## Key Concepts

- **The Bitter Lesson**: General computation-based methods outperform knowledge-based approaches at scale
- **Supervised Learning**: Learning from labeled examples or demonstrations
- **Reinforcement Learning**: Learning from interactions with environments and reward signals
- **Policy Gradient**: RL method that learns action policies through trial and error
- **Value Function**: Estimates expected future rewards from given states
- **RLHF**: Reinforcement Learning from Human Feedback for LLM alignment
- **RLVR**: Reinforcement Learning with Verifiable Rewards for reasoning models
- **Hidden Markov Models**: Probabilistic models that learn from data without explicit knowledge encoding
- **Experience vs Knowledge**: Distinction between learning from direct interaction vs. learning from human descriptions

## Historical Examples

### Harpy → HMMs (1970s-1990s)
- Harpy: Expert-designed grammar, juncture rules, phone frequencies
- HMMs: Learned probabilities from data
- Result: HMMs scaled to much larger vocabularies

### AlphaGo → AlphaGo Zero (2016-2017)
- AlphaGo: Supervised learning on human games + RL
- AlphaGo Zero: Pure RL from self-play
- Result: AlphaGo Zero discovered novel strategies and was stronger

## Relationships

- [[The Bitter Lesson]] suggests [[LLMs]] may be limited by [[human knowledge]]
- [[AlphaGo Zero]] demonstrates systems can learn superior strategies without [[supervised learning]]
- [[RLHF]] and [[RLVR]] represent partial steps toward [[experience-based learning]]
- [[Sutton]] argues true [[AGI]] requires [[experience]] not [[knowledge encoding]]

## Open Questions

- Will LLMs hit a performance ceiling due to human knowledge constraints?
- Can experience-based systems eventually surpass LLMs?
- What would a system that "discovers like we can" look like?
- How do we balance leveraging human knowledge with enabling discovery?

## Counterarguments

Some argue that:
- Human knowledge contains compressed wisdom from billions of years of evolution
- Starting from human knowledge provides useful priors for exploration
- Pure RL is incredibly data-inefficient
- Hybrid approaches (supervised pre-training + RL fine-tuning) may be optimal

## Implications

If Sutton is right:
- Current LLM approaches may be approaching their limits
- We need new paradigms for experience-based learning
- Physical robots interacting with the world may be crucial for AGI
- The bitter lesson may apply to LLMs as a negative example

## See Also

- [[yann-lecun-interview]] - JEPA approaches that learn world models from experience
- [[how-models-learn]] - Series on neural network training mechanisms
- [[inside-the-worlds-smartest-robot-brain-vla]] - VLA models bridging LLMs to physical world

## Source Material

**Primary Source:**
> Welch Labs. *"Video"* [**Can Humans Make AI Any Better?**](https://www.youtube.com/watch?v=2hcsmtkSzIw). YouTube. Retrieved 2026-07-09. Available at: https://www.youtube.com/watch?v=2hcsmtkSzIw

**Complete Transcript:**
See  for the full video transcript.

**Channel:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09
