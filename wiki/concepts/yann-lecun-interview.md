---
title: Yann LeCun Interview
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, machine-learning, deep-learning, welch-labs, video-series]
sources: raw/transcripts/welch-labs/yann-lecun's-$1b-bet-against-llms-part-1.md, raw/transcripts/welch-labs/yann-lecun's-$1b-bet-against-llms-part-2.md
---

# Yann LeCun Interview

## Overview

This two-part video series from Welch Labs features AI pioneer [[Yann LeCun]] discussing his $1 billion bet against large language models (LLMs). The series explores LeCun's alternative architecture called JEPA (Joint Embedding Predictive Architecture), which represents a fundamentally different approach to building intelligent systems that doesn't rely on language as its primary substrate.

## Videos in Series

### Yann LeCun's $1B Bet Against LLMs [Part 1]

**YouTube URL:** https://www.youtube.com/watch?v=kYkIdXwW2AE
**Video ID:** `kYkIdXwW2AE`
**Channel:** Welch Labs (@WelchLabs)
**Transcript:** 

### Yann LeCun's $1B Bet Against LLMs [Part 2]

**YouTube URL:** https://www.youtube.com/watch?v=v_jDvpEGTIg
**Video ID:** `v_jDvpEGTIg`
**Channel:** Welch Labs (@WelchLabs)
**Transcript:** 
### Part 1: Yann LeCun's $1B Bet Against LLMs

**Video ID:** kYkIdXwW2AE

#### JEPA Architecture

[[JEPA]] is not a single AI model but an alternative framework for training AI models. Unlike traditional approaches that train models to predict some output Y given input X (like LLMs predicting next tokens), JEPA uses a different architecture:

- Input X and output Y are each passed into **encoders** that return embedding vectors or matrices
- A third model called a **predictor** is trained to predict the embedding of Y given the embedding of X
- By predicting embeddings rather than raw outputs, JEPA sidesteps problems like blurry predictions in video

#### The Problem with Generative Video Prediction

When researchers tried to apply self-supervised generative approaches to video (similar to next-token prediction in LLMs), they encountered a critical problem:

- Predicting pixel values in the next frame produces blurry results
- This blurriness compounds dramatically in longer horizon predictions
- In full HD video, each pixel can take 256 discrete values
- With 1920×1080×3 color pixels, there are ~10^15 million possible next video frames
- Unlike language models with finite vocabularies (e.g., GPT-2 with 50,257 tokens), complete enumeration is impossible in video
- When a model faces ambiguity (e.g., a ball could bounce left or right), it averages the outcomes, resulting in blur

#### Joint Embedding Architectures

The solution, discovered by LeCun and others around 2017-2018, is to use **joint embedding architectures** that don't reconstruct data:

- Take two images of the same scene (or an image and a corrupted/transformed version)
- Pass both through encoders
- Train the system to produce the same embedding for semantically equivalent inputs
- This approach dates back to the 1990s when LeCun created **Siamese neural networks** at Bell Labs for fraud detection

#### The Representation Collapse Problem

Joint embedding architectures have a critical flaw: the network can find a trivial solution by returning the same embedding vector for any input (e.g., all ones), maximizing similarity without actually learning anything useful. This is known as the **representation collapse problem** and plagued joint embedding architectures for years.

### Part 2: JEPA Implementations and World Models

**Video ID:** v_jDvpEGTIg

#### VJePA 2: State-of-the-Art Video Understanding

In 2025, Meta trained VJePA 2, a JEPA-based model on 1 million hours of video using up to 1 billion parameters:

- Trained using self-supervised learning where video clips are corrupted by removing patches
- The predictor learns to predict embeddings of missing patches
- By filling in missing video pieces, the model learns how video and the world work
- When swapped into vision-language models (VLMs) as a replacement for CLIP-style encoders, VJePA 2 achieved state-of-the-art results on video understanding benchmarks
- Notably, it performed well even though it was trained without any language supervision

#### VLJePA: Efficient Vision-Language Models

Meta also created VLJePA (Vision-Language JEPA), which applies the JEPA approach to full VLMs:

- Instead of directly generating output text, the model passes target text through an encoder
- A predictor model predicts the embedding of the output text
- This approach abstracts away irrelevant semantic differences in phrasing (e.g., "do not eat this mushroom" vs "this mushroom is not safe to eat")
- VLJePA learns significantly more efficiently than traditional VLMs
- In controlled experiments, VLJePA reached 35% video classification accuracy after 5 million training examples compared to just 20% for traditional VLMs
- VLJePA was able to outperform 7 billion parameter models while using just 1.6 billion parameters on visual question-answering benchmarks

#### LeCun's Critique of VLA Models

LeCun is highly critical of **Vision-Language-Action (VLA)** models like those from Physical Intelligence:

1. **Behavioral cloning doesn't scale**: VLA models rely on training on massive amounts of human demonstration data, which is impractical for all possible task variations and environments
2. **Lack of explicit planning**: VLA models don't have world models that can predict the consequences of their actions, making them "brittle" when facing new situations

LeCun argues: "I do not understand how you can even think of building an agentic system without a agentic system having the ability of predicting the consequences of its actions."

#### World Models and JEPA's Approach

JEPA-based approaches learn **world models** that can predict the consequences of actions:

- The model learns to represent the world's dynamics through embedding predictions
- This allows for explicit planning and reasoning about action outcomes
- Unlike VLA models that essentially memorize behavior patterns, JEPA models can understand causal relationships

## Key Concepts

- **Joint Embedding Architectures**: Frameworks that train models to produce similar embeddings for semantically equivalent inputs without reconstructing raw data
- **Embedding**: A vector or matrix of numbers that represents the salient features of data
- **Representation Collapse**: The failure mode where joint embedding models return identical embeddings for all inputs
- **World Model**: An internal representation of how the world works that enables prediction and planning
- **VLA Models**: Vision-Language-Action models that directly output robot control signals from vision and language inputs

## Relationships

- [[JEPA]] approaches represent an alternative to [[LLMs]]
- [[VJePA]] can replace [[CLIP]] encoders in vision-language models
- [[VLJePA]] offers efficiency gains over traditional [[VLMs]]
- LeCun's approach contrasts with mainstream [[VLA]] models like those from [[Physical Intelligence]]

## Historical Context

- **1990s**: LeCun created Siamese neural networks at Bell Labs for fraud detection
- **2015**: LeCun's famous "cake slide" analogy: self-supervised learning (cake), supervised learning (icing), reinforcement learning (cherry)
- **2015**: OpenAI founded, initially focused on reinforcement learning before pivoting to GPT
- **2017-2018**: Realization that best systems for image representations are non-generative joint embedding approaches
- **2025**: VJePA 2 and VLJePA demonstrate state-of-the-art performance with JEPA architectures

## Open Questions

- Will JEPA-based approaches eventually overtake VLA models in robotics?
- How can representation collapse be definitively solved across all applications?
- What are the limits of JEPA's ability to learn world models from video alone?

## See Also

- [[how-models-learn]] - Related series on neural network training
- [[inside-the-worlds-smartest-robot-brain-vla]] - Welch Labs video on VLA models
- [[grokking]] - Phenomenon where models suddenly generalize after extended training

## Source Material

**Citation:**
> Welch Labs. *Yann LeCun Interview Video Series*. YouTube Channel. Retrieved 2026-07-09. Available at: https://www.youtube.com/@WelchLabs

**Individual Videos:**
- [Yann LeCun's $1B Bet Against LLMs [Part 1]](https://www.youtube.com/watch?v=kYkIdXwW2AE)
- [Yann LeCun's $1B Bet Against LLMs [Part 2]](https://www.youtube.com/watch?v=v_jDvpEGTIg)

**Complete Transcripts:**
All video transcripts are available in [[raw/transcripts/welch-labs/]].

**Channel Information:**
[Welch Labs YouTube Channel](https://www.youtube.com/@WelchLabs) - 888K subscribers, 147 videos of AI, mathematics, and science education.

**Access Date:**
2026-07-09