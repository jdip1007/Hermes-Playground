---
source_url: https://www.youtube.com/watch?v=kYkIdXwW2AE
ingested: 2026-07-08
video_id: kYkIdXwW2AE
title: Yann LeCun's $1B Bet Against LLMs [Part 1]
series: Yann LeCun Interview
---

[00:00] Okay, then let me make a controversial
[00:02] statement that again is going to get me
[00:04] a lot of friends in SQL. Um,
[00:06] >> AI legend Yan Lun has raised a billion
[00:09] dollars to pursue an alternative
[00:11] approach to AI. Unlike large language
[00:14] models, Lacun's approach is not rooted
[00:17] in language and is not generative. By
[00:20] design, it does not spit out text,
[00:22] images or videos. Instead, Lacun has
[00:25] proposed Jeepa. Jeppa is not a single AI
[00:28] model, but instead an alternative
[00:30] architecture or framework for training
[00:32] AI models. Many successful approaches in
[00:35] AI and machine learning train models to
[00:37] predict some output Y given some input
[00:39] X. Large language models are given some
[00:42] input text X and trained to predict the
[00:44] text Y that comes next. Image classifier
[00:48] models are given an input image X and
[00:50] trained to predict the corresponding
[00:51] label Y. Jeepa does not work like this.
[00:56] Instead, our inputs X and outputs Y are
[00:58] each passed into models known as
[01:00] encoders. These encoders return a vector
[01:02] or matrix of numbers, often referred to
[01:05] as an embedding.
[01:07] From here, a third model known as a
[01:09] predictor is trained to predict the
[01:11] embedding of Y given the embedding of X.
[01:15] Why might this be a better way to build
[01:17] AI systems? Do you think that Jeepa or
[01:20] world model based approaches, do you
[01:21] think they'll replace LLMs one day or
[01:23] are they kind of solving different
[01:24] problems?
[01:25] Initially they'll solve different
[01:27] problems.
[01:28] >> Eventually they're replaced LLM okay
[01:31] because you know LLMs are really good at
[01:33] manipulating language but basically
[01:34] nothing else.
[01:36] >> They're really good in domains where the
[01:39] language itself is the substrate of
[01:42] reasoning
[01:43] >> compared to the mainline generative
[01:45] language approach to AI. Jeepa lives on
[01:48] an alternative path of joint embedding
[01:50] architectures.
[01:52] Interestingly, Lacun played a
[01:53] significant role at the outset of both
[01:55] paths. In part one of this two-part
[01:58] series, we'll explore this alternative
[02:00] path to Jeepa. We'll dig into why Yan
[02:03] moved away from generative architectures
[02:05] just as they were gaining traction in
[02:07] language and explore Yan's epiphany for
[02:09] a new solution to the representation
[02:11] collapse problem that plagued joint
[02:13] embedding architectures for years.
[02:16] Finally, we'll dig into the Jeepa
[02:17] architecture itself.
[02:19] In part two, we'll dive into JEPA
[02:21] implementations and see exactly how
[02:23] these models stack up against LLM driven
[02:26] approaches.
[02:31] Yan Lun saw the revolution coming in the
[02:35] 1980s. While most of the AI field was
[02:37] busy building expert systems that were
[02:39] explicitly programmed instead of learned
[02:41] from data, Jan pioneered the
[02:43] convolutional neural network. 25 years
[02:46] later, when deep learning began its rise
[02:48] to its now dominant position in AI, the
[02:51] breakthrough deep learning model AlexNet
[02:54] turned out to be uncannily similar to
[02:56] Lacun's convolutional nets from the
[02:58] 1990s.
[03:00] However, as deep learning continued to
[03:01] pick up steam through the 2010s, Lacun
[03:04] and other researchers became
[03:05] increasingly concerned by just how much
[03:08] this approach to AI depended on labeled
[03:10] training data. AlexNet was trained on
[03:13] the enormous and meticulously labeled
[03:14] imageet data set using supervised
[03:17] learning where AlexNet was trained to
[03:19] match the labels assigned to each image
[03:21] by human annotators.
[03:23] In contrast, children are able to learn
[03:25] very general representations for
[03:27] concepts like dog with very few
[03:29] explicitly labeled examples.
[03:33] As manually labeled data became a
[03:35] bottleneck for supervised learning,
[03:37] interest grew in alternative approaches.
[03:40] Reinforcement learning, where models
[03:42] learn from interacting with their
[03:43] environments instead of from labeled
[03:44] data, experienced a many renaissance in
[03:47] the mid2010s,
[03:49] highlighted by Google DeepMind's
[03:51] breakthrough performance on Atari games
[03:52] and the highly complex board game Go.
[03:56] Concurrently, Lacun and others explored
[03:58] unsupervised methods that learn from
[04:00] data without labels, including a variant
[04:03] called self-supervised learning, where
[04:05] the labels are taken from the data
[04:06] itself. Starting in 2015 or so, I
[04:10] started showing a slide that has become
[04:12] a bit of a meme in the machine learning
[04:13] community where I said like, you know,
[04:15] if it's the cake slide, right? So, if uh
[04:19] intelligence is a cake, the bulk of the
[04:20] cake is self-s supervised learning, the
[04:23] icing on the cake, supervised learning,
[04:25] and the chair on the cake, reinforcement
[04:26] learning. At the time, people were kind
[04:28] of crazy about reinforcement learning.
[04:29] So I was trying to tell them like this
[04:31] is not never going to you know take us
[04:33] to you know anywhere close to human or
[04:35] animal intelligence because it's too
[04:37] inefficient. Um and uh turns out the
[04:42] success of self-s supervised learning uh
[04:46] you know happened in in text and and
[04:49] language much faster than it did in sort
[04:51] of more uh you know natural uh
[04:54] modalities like uh like vision. Here Jan
[04:58] is referring to the success of next
[04:59] token prediction for training large
[05:01] language models. OpenAI was founded in
[05:04] 2015 and initially focused their efforts
[05:06] on reinforcement learning creating
[05:08] OpenAI Gym and Universe and showing very
[05:11] impressive performance on complex video
[05:14] games. While much of the company was
[05:16] focused on reinforcement learning, Ilia
[05:19] Sutskever, Alec Radford and others
[05:20] became interested in a new neural
[05:22] network architecture from Google, the
[05:24] transformer. Initially designed for
[05:26] language translation,
[05:29] while experimenting, Radford tried an
[05:31] interesting modification. Instead of
[05:33] having the transformer translate from a
[05:35] block of text in one language to a block
[05:37] of text in another language, he switched
[05:39] to a simpler self-supervised approach
[05:42] where training text is broken into
[05:43] sequences and the transformer is given
[05:46] all but the last little piece of text
[05:48] known as a token in each sequence and
[05:51] trained to predict what this final token
[05:52] will be.
[05:55] Ratford and his OpenAI colleagues
[05:56] trained their transformer on a fairly
[05:58] large internal OpenAI data set of 7,000
[06:01] books. Note that we now call this phase
[06:03] pre-training and then further train
[06:06] their model using standard supervised
[06:08] learning from human generated labels on
[06:10] specific language tasks.
[06:12] Their two-stage training approach worked
[06:14] well, setting new state-of-the-art
[06:16] results on nine language benchmarks,
[06:19] including tasks like high school level
[06:21] reading comprehension questions,
[06:23] outperforming architectures and methods
[06:25] that were individually designed and
[06:26] trained for each individual task.
[06:29] Radford's model is now known as
[06:31] generative pre-trained transformer 1 or
[06:34] GPT1.
[06:36] GPT1 didn't receive much public
[06:38] attention at the time, but was a huge
[06:40] unlock, breaking models free from their
[06:42] dependence on humanlabeled data and
[06:45] opening up unprecedented levels of
[06:47] scale.
[06:48] Other researchers at OpenAI quickly
[06:50] grasp the significance of Radford's
[06:52] results and the team went allin on this
[06:54] approach, aggressively scaling up to
[06:57] GPT2 in 2019, GPT3 in 2020, and Chat GPT
[07:02] in 2022.
[07:04] In 2012, AlexNet was trained on around a
[07:07] million examples. In 2020, GPT3 was
[07:10] trained on hundreds of billions of
[07:12] examples. And interestingly, the new
[07:15] training paradigm that emerged exactly
[07:17] matched Yon Lacun's predictions from a
[07:19] few years earlier. An extensive
[07:21] self-supervised pre-training phase
[07:24] followed by supervised learning and
[07:25] finally reinforcement learning to shape
[07:28] the raw next token predictor model into
[07:30] a helpful AI assistant.
[07:32] However, while these self-supervised
[07:34] generative approaches clearly broke
[07:36] through in language, the picture was
[07:38] much fuzzier for image and video data.
[07:41] But I I I kept working on vision and
[07:44] then initially uh the the uh idea was to
[07:49] use um so to train a system to predict
[07:52] what happens in video but to use uh
[07:54] generative architectures. Um so
[07:57] basically train at a pixel level what's
[07:59] going to happen in the video. Years
[08:01] before the success of GPT1, researchers
[08:04] including Lacun had tried to apply the
[08:06] same self-supervised generative approach
[08:08] to video. In the most straightforward
[08:10] implementation, we configure our neural
[08:13] network to take in the RGB pixel values
[08:15] from a sequence of video frames and then
[08:17] predict the pixel values in the next
[08:19] frame just as the GPT models are trained
[08:22] to predict the next token in language.
[08:24] However, when we use these models to
[08:26] predict the next frame, the results are
[08:28] blurry. And this blurriness compounds
[08:31] dramatically in longer horizon
[08:33] predictions. Large language models are
[08:35] auto reggressive. When chat GPT answers
[08:38] a question, it generates one token at a
[08:40] time. At each step, feeding its latest
[08:42] generated token back into its input to
[08:45] create the next output. If we try this
[08:47] auto reggressive approach with a next
[08:49] frame video prediction model, the
[08:51] results quickly devolve into blurry
[08:53] nothingness.
[08:55] Before we see exactly how JEA is able to
[08:57] get around this blurry prediction
[08:59] problem, let's look at another
[09:00] fascinating application of transformers
[09:02] beyond language models. This video is
[09:06] sponsored by Hudson River Trading, and
[09:08] this is an order book. The left column
[09:11] shows all the bids to buy Nvidia stock
[09:14] ranked by bid price, and the right
[09:16] column shows all the current offers to
[09:18] sell Nvidia stock ranked by asking
[09:20] price. On a busy trading day, on the
[09:23] order of 1,000 new buy and sell orders
[09:26] like this come in every second. This
[09:28] deluge of orders is an incredibly rich
[09:31] information source. Is it possible to
[09:33] train a transformer like the ones used
[09:35] in VJA to find patterns in this data and
[09:39] use these patterns to predict future
[09:41] prices? Hudson River Trading has
[09:43] trillions of tokens of historical data.
[09:46] This is the same order of magnitude of
[09:48] training data used to train Frontier
[09:50] LLMs.
[09:51] and their researchers are working to
[09:53] push the frontiers of machine learning
[09:55] on this data.
[09:57] The VJEPA model we'll see later in the
[09:59] video maps patches of videos to
[10:01] individual embedding vectors. We could
[10:03] take a similar approach with order book
[10:05] data tokenizing groups of orders using
[10:08] some financial intuition.
[10:10] However, this naive approach does not
[10:12] work well in practice, and the Hudson
[10:14] River trading team has developed some
[10:15] really interesting approaches to adapt
[10:17] cutting edge transformer architectures
[10:19] to the complexities and constraints of
[10:21] trading data. And all of this is
[10:23] happening in a setting where speed is
[10:25] everything. Models have to run under
[10:28] incredibly tight latency constraints.
[10:31] These fascinating and highly complex
[10:33] research and engineering challenges
[10:35] combined with the resources to actually
[10:37] tackle them and an open, highly
[10:39] collaborative environment make Hudson
[10:41] River Trading an incredibly unique place
[10:43] to work. I hear a lot from potential
[10:46] sponsors these days and have been
[10:48] seriously impressed in my interactions
[10:49] with the Hudson River Trading team. The
[10:52] level of technical discussion and
[10:53] enthusiasm for these deep and
[10:55] interesting problems is unparalleled in
[10:57] my experience. If this sounds
[10:59] interesting, Hudson River Trading is
[11:01] currently hiring for AI researchers,
[11:03] algorithm developers, and software
[11:05] engineers. They're hiring globally, and
[11:07] you don't need a finance background. You
[11:10] can learn more at hudson
[11:11] rivertrading.com/welchlabs.
[11:14] Now, back to Jeepa.
[11:17] Now, the blurry frames produced by our
[11:19] generative video prediction approach are
[11:21] not some huge mystery. Language is
[11:23] complex and unpredictable, but it's
[11:26] nothing compared to video.
[11:28] Language models use fixedsiz
[11:30] vocabularies.
[11:31] GPT2 has 50,257
[11:34] discrete outputs, one for each token
[11:36] that the model could say next. This
[11:39] complete enumeration approach is
[11:40] hopeless in video. For full HD video, in
[11:44] the most general case, each pixel can
[11:46] take on 256 discrete values. And we have
[11:50] 1920 * 1080 * 3 color pixels. Meaning
[11:54] there are something like 10 to the power
[11:56] of 15 million possible next video frames
[12:00] dwarfing the number of atoms in the
[12:01] observable universe. So there's no way
[12:04] our video prediction model can have a
[12:06] discrete output for each possible next
[12:08] video frame as our language model has a
[12:11] discrete output for each next possible
[12:12] token.
[12:14] Instead, many generative video
[12:16] approaches of this era had the network
[12:18] directly output pixel intensity values.
[12:22] The big challenge with this approach is
[12:24] how the model learns to handle
[12:25] uncertainty.
[12:27] If we compare an LLM learning to
[12:29] complete the sentence, the ball bounced
[12:30] to the and a neural network predicting
[12:33] the next frame of a video of a ball
[12:35] actually bouncing, we can see exactly
[12:37] what goes wrong. In the LLM training
[12:40] case, the model will see various
[12:42] examples in its training set of the ball
[12:44] bouncing left and right. And since the
[12:47] model has separate outputs for each of
[12:49] these tokens, it can essentially
[12:51] independently update these
[12:52] probabilities.
[12:54] Our video model doesn't have it so easy.
[12:57] If our data set includes videos of the
[12:59] ball starting down the same path and
[13:01] then bouncing in various directions,
[13:03] since our model is forced to directly
[13:05] predict a single output frame for a
[13:07] given input, the best it can do in the
[13:10] face of this ambiguity is to predict the
[13:12] average of these outcomes.
[13:14] When we average the pixel values of our
[13:16] videos, we end up with a blurry, washed
[13:18] out mess.
[13:20] Now, this is only the most naive
[13:22] approach, and there have been many, many
[13:24] interesting video and image prediction
[13:26] strategies tried with various degrees of
[13:27] success over the last couple decades.
[13:31] However, the challenges that naturally
[13:32] arise led Lun and other researchers to
[13:35] ask an interesting question. Do our
[13:38] models really need to be generative? In
[13:41] our GPT example, during the crucial
[13:43] pre-training phase, it really doesn't
[13:46] matter that our model is generative.
[13:48] After pre-training on next token
[13:50] prediction, we're left with a model
[13:52] that's essentially a really good
[13:53] autocomplete.
[13:55] But this is not the point. What actually
[13:58] matters are the internal representations
[14:00] and features that the model learns to
[14:02] solve the next token prediction task.
[14:05] These learned internal representations
[14:07] are what allows pre-trained models to be
[14:10] quickly adapted into powerful AI
[14:12] assistance.
[14:14] Next token prediction on language is a
[14:16] proxy for intelligence that has turned
[14:18] out to work shockingly well.
[14:22] But are there other signals and methods
[14:24] that we can use to learn these powerful
[14:26] internal representations that we need to
[14:28] build intelligent systems?
[14:30] Simultaneously we started realizing in
[14:33] the you know around
[14:36] 2017 18 that uh the the best system to
[14:40] learn representations of images are
[14:43] systems that do not are not generative.
[14:46] They don't reconstruct they they you
[14:48] know you you you get an image and you
[14:51] run it to an encoder and then you try to
[14:53] kind of coers this encoder to extract as
[14:56] much information as possible with
[14:58] certain properties. So for example, you
[15:00] take two images of the same scene or you
[15:03] take an image and you corrupt it or
[15:04] transform it in some ways. You run them
[15:06] both through encoders and you tell the
[15:08] system the representation whatever you
[15:10] extract to really be the same for those
[15:12] two images because they semantically
[15:14] represent the same thing. Um and I've
[15:17] been working on things like this since
[15:18] the '9s. So this is not a new idea. This
[15:20] this idea joint embedding we used to
[15:22] call this Siamese neural net. The method
[15:25] Yan is referring to here, Siamese
[15:27] networks, was created by Yan and his
[15:29] collaborators at Bell Labs in the early
[15:31] 1990s when developing systems to detect
[15:34] fraudulent signatures.
[15:37] The system worked by passing a pair of
[15:39] signature images into two copies of the
[15:41] same neural network. The network copies
[15:44] were not trained to generate any kind of
[15:45] data. Instead, they output vectors of
[15:48] numbers, often referred to as embedding
[15:50] vectors. These network copies were
[15:52] trained on two types of examples.
[15:55] Positive examples that contain a
[15:57] reference signature and a nonfraudulent
[15:59] signature. So these are by the same
[16:00] person. And negative examples that
[16:03] contain a reference signature and a
[16:05] fraudulent signature.
[16:07] For fraudulent examples, the network
[16:09] copies are trained to produce embedding
[16:11] vectors that are maximally different.
[16:13] And for positive examples, produce
[16:15] embedding vectors that are maximally
[16:16] similar.
[16:18] When a new signature comes along, we can
[16:20] pass it into our network to comput an
[16:22] embedding vector and compare it to the
[16:24] embedding vector produced from our
[16:26] reference signature. If the resulting
[16:28] embedding vectors are not similar
[16:30] enough, the signature is detected as
[16:32] fraudulent.
[16:34] By jointly embedding our signatures, our
[16:36] Siamese network learns a very useful
[16:38] internal representation of the images of
[16:40] our signatures, notably without learning
[16:42] to predict or generate any actual
[16:44] signature images. As a GPT-based
[16:47] approach would
[16:49] joint embeddings offer a potentially
[16:51] viable solution to our blurry video
[16:53] problem. As Yan explains,
[16:55] >> you you get an image and you run it to
[16:58] an encoder and then you try to kind of
[17:00] coers this encoder to extract as much
[17:03] information as possible with certain
[17:05] properties. So for example, you take two
[17:07] images of the same scene or you take an
[17:10] image and you corrupt it or transform it
[17:11] in some ways. You run them both through
[17:13] encoders and you tell the system the
[17:16] representation whatever you extract
[17:17] should really be the same for those two
[17:18] images because they semantically
[17:20] represent the same thing. So the idea
[17:22] here is that we sidestep the blurry
[17:24] video problem we saw with generative
[17:26] models by using a joint embedding
[17:28] architecture to map copies of images or
[17:31] videos with one or both corrupted or
[17:34] transformed to similar embedding
[17:36] vectors. This trained model will ideally
[17:39] learn a useful internal representation
[17:41] of images or video that we can repurpose
[17:44] for other tasks just as GPT models learn
[17:47] internal representations during
[17:48] pre-training that can be adapted into AI
[17:51] assistant behaviors.
[17:54] However, this joint embedding strategy
[17:55] has a huge problem. Since we're training
[17:58] our network to make the embeddings of
[18:00] our original and corrupted images or
[18:02] videos as similar as possible, the
[18:04] network can find a trivial solution
[18:07] where it simply returns the same
[18:08] embedding vector for any input that we
[18:11] pass in. If our network learns to
[18:13] output, for example, a vector of all
[18:15] ones for any input, then the network
[18:18] will return all ones for a corrupted and
[18:20] non-corrupted view of the same image,
[18:22] maximizing the resulting similarity, but
[18:25] without actually learning anything
[18:26] useful.
[18:28] This problem is known as representation
[18:30] collapse.
[18:31] In Lacun's original Siamese network
[18:33] approach, the team used what's now known
[18:36] as contrastive learning to avoid
[18:38] representation collapse, giving the
[18:41] network both positive and negative
[18:42] examples.
[18:44] It turns out we can apply the same
[18:46] contrastive approach to images and
[18:47] video, training our network to output
[18:50] similar embeddings for views of the same
[18:52] underlying images or videos and
[18:54] dissimilar embeddings for different
[18:56] images or video. These contrastive
[18:58] methods have been successfully
[18:59] implemented on images and videos, but
[19:02] can run into issues when they're scaled
[19:04] up, requiring large amounts of
[19:06] computation and many negative examples
[19:08] to learn meaningful representations. and
[19:10] Lacun has argued that in the worst case,
[19:13] the number of contrastive samples may
[19:15] grow exponentially with the dimension of
[19:17] the representation.
[19:19] By the end of the 2010s, it was clear to
[19:21] Lun and others that using generative
[19:23] models to fully reconstruct images and
[19:26] video was not a good strategy for
[19:28] self-supervised learning. But there
[19:30] wasn't a straightforward solution to the
[19:32] representation collapse problem that
[19:34] would allow joint embedding
[19:35] architectures to learn the same level of
[19:37] powerful and general internal
[19:39] representations that large language
[19:41] models were enjoying.
[19:43] >> And so it was pretty clear that
[19:44] reconstruction was a bad idea for uh
[19:47] signals like like images and
[19:50] >> a fortory for video.
[19:52] And
[19:54] I had a bit of an epiphany because uh
[19:57] the uh the the methods that we were
[20:01] using to train those joint emitting
[20:02] architectures were kind of hacks a
[20:04] little bit until um I did some work with
[20:09] a couple postocs at at Meta particular
[20:12] guy called Stefan Deni who uh came up
[20:16] with a technique called Ballot twin. So
[20:18] it it's based on an old idea in uh in
[20:21] computational noise science in machine
[20:23] learning that Jeffington also played on
[20:25] with similar ideas which is that you you
[20:27] should have time to have some measure of
[20:30] information content and try to maximize
[20:31] that and there's some real world work by
[20:35] uh by Barlo about is a famous
[20:38] computational neuroscientist and right
[20:40] >> theoretical neuroscientist
[20:42] >> here Jan is referencing the work of
[20:44] Horus Barlo who hypothesized in 1961 one
[20:48] that the neurons in animal and human
[20:50] vision systems operate by reducing
[20:52] redundant information between neurons.
[20:55] Stefan Deni a postto lacun was working
[20:58] with in 2020 was familiar with Barlo's
[21:01] work and proposed that one way to avoid
[21:03] representation collapse could be to
[21:05] apply Barlo's idea to the outputs of
[21:08] their networks.
[21:10] In the joint embedding architectures
[21:11] we've been considering, our embedding
[21:13] vectors are produced by a final layer of
[21:15] artificial neurons in our embedding
[21:17] networks. So if our embedding vectors
[21:19] are of length 128, then the output layer
[21:22] of each of our networks contains 128
[21:25] neurons.
[21:27] If we pass in a batch of various images
[21:29] into each of our networks and plot the
[21:31] output activation of the first neuron as
[21:33] we step through our images, we can see
[21:36] that this neuron fires strongly on this
[21:38] first picture of a dog, not so much on
[21:40] this cat picture, and so on.
[21:43] Following our joint embedding approach,
[21:45] our network takes in a distorted view of
[21:47] the same batch of images.
[21:50] The whole point of our joint embedding
[21:52] architecture is to make the resulting
[21:53] embeddings of the same underlying images
[21:55] or videos similar. So we want the output
[21:58] of our first neuron in our second
[22:00] network to be similar to the output of
[22:02] our first neuron in our first network.
[22:05] In a standard joint embedding
[22:06] architecture, we would simply measure
[22:08] and maximize the similarity between
[22:10] these two vectors.
[22:12] However, as we've seen, this approach is
[22:14] susceptible to representation collapse.
[22:17] With the network simply learning to
[22:18] output the same values for any input
[22:20] image.
[22:22] But now applying Barllo's hypothesis as
[22:24] proposed by Stefan Deni, we should
[22:27] reduce the redundancy between the
[22:28] outputs of different neurons.
[22:31] We have a bit of a choice to make here.
[22:33] We could compare the output of the first
[22:35] neuron in our first network to the
[22:36] output of our second neuron in our first
[22:38] network or to the output of the second
[22:40] neuron in our second network. The team
[22:43] chose to compare to the output of the
[22:44] second network. As we'll see, this
[22:46] results in a simpler implementation and
[22:49] the team further notes in the appendex
[22:50] of their paper that in practice they
[22:52] didn't see much difference between these
[22:53] alternatives.
[22:55] Here's the output of the second neuron
[22:57] in our second model. To measure the
[23:00] redundancy between neuron outputs, the
[23:02] team computed the crossorrelation
[23:04] between these output vectors. This
[23:07] computation consists of scaling each
[23:09] vector and taking the dotproduct
[23:11] resulting in a single number, the
[23:13] correlation or more precisely the
[23:16] Pearson correlation coefficient between
[23:18] our vectors. To reduce the redundancy
[23:21] between our neurons as proposed by
[23:22] Barlo, we want this correlation to be
[23:25] close to zero. If we arrange the neuron
[23:28] outputs of our first encoder vertically
[23:30] and the outputs of our second encoder
[23:32] horizontally, we can compute and place
[23:35] the correlations between all pairs of
[23:37] neurons into a single matrix. This
[23:39] crossorrelation matrix has one row for
[23:42] each output neuron in our first encoder
[23:44] and one column for each output neuron in
[23:46] our second encoder. The elements along
[23:49] the diagonal capture the correlations
[23:51] between corresponding neurons.
[23:54] Since the whole idea here of this joint
[23:55] embedding architecture is to produce
[23:57] similar outputs for distorted versions
[23:59] of the same image, we want the
[24:01] corresponding neurons in our two
[24:03] encoders to have high correlations.
[24:06] Alternatively, all of the off diagonal
[24:08] entries in our crossorrelation matrix
[24:10] correspond to different neurons in our
[24:12] two encoders.
[24:14] And following Barlo's hypothesis, we
[24:16] want to reduce the redundancy between
[24:18] these neurons. So we want these
[24:20] correlations to be zero. So ideally our
[24:24] crossorrelation matrix looks like the
[24:26] identity matrix.
[24:28] Deni lacun and their collaborators
[24:30] designed a new loss function for their
[24:32] joint embedding architecture that
[24:34] measured the deviation of their
[24:36] crossorrelation matrix from the identity
[24:38] matrix.
[24:39] Their new method which they called barlo
[24:42] twins worked surprisingly well avoiding
[24:45] representation collapse while learning a
[24:47] powerful internal representation of the
[24:49] images that it was trained on.
[24:52] The team used a few different methods to
[24:54] measure the quality of these internal
[24:55] representations.
[24:58] Earlier, we saw how by using
[25:00] self-supervised pre-training, GPT1 was
[25:03] able to outperform purely supervised
[25:05] models that had been adapted to specific
[25:07] language tasks.
[25:09] For vision tasks, one of the most
[25:11] important benchmarks at the time was
[25:13] accuracy on the imageet data set. This
[25:16] is the same image classification data
[25:18] set that the AlexNet model had shown
[25:20] breakthrough performance on back in
[25:22] 2012. The original AlexNet paper
[25:24] achieved an accuracy of 59.3% on the
[25:27] imagenet validation set. To compare the
[25:30] self-supervised Barlo twins approach to
[25:33] fully supervised models like AlexNet,
[25:36] the team used a common approach known as
[25:38] a linear probe where a single layer of
[25:41] neurons are tacked onto the output of
[25:43] the Barllo twins trained encoder model
[25:46] and trained using supervised learning to
[25:48] classify the imageet data set.
[25:51] Importantly, the main encoder model is
[25:53] frozen during this training process.
[25:56] So the simple linear probe is
[25:58] effectively adapting the Barlo twins
[26:00] encoders learned representation to solve
[26:02] the imageet classification task.
[26:05] Impressively, the frozen Barlo twins
[26:07] encoder with a linear probe achieved an
[26:10] imageet accuracy of 73.2%.
[26:13] Outperforming the original fully
[26:15] supervised AlexNet model by over 10
[26:17] percentage points.
[26:19] However, in the nine years from the
[26:21] AlexNet paper in 2012 to the Barlo twins
[26:24] paper in 2021,
[26:26] fully supervised approaches had made
[26:28] significant improvements over AlexNet.
[26:31] In 2020, a team at Google applied the
[26:33] transformer architecture to image
[26:35] classification,
[26:36] achieving a new state-of-the-art imageet
[26:38] accuracy of 88.6%.
[26:42] So by 2021, thanks to the Barlo twins
[26:45] epiphany and other joint embedding
[26:47] approaches, self-supervised learning was
[26:49] advancing rapidly for vision tasks, but
[26:52] was still inferior to fully supervised
[26:55] methods. The general and clearly
[26:57] superior self-supervised generative
[26:59] pre-training methods in language that
[27:02] were fueling the rapid advancement of
[27:04] LLMs were still out of reach for image
[27:06] and video applications. And so it became
[27:09] clear that this really was the the right
[27:12] way to go. So we kind of uh after that
[27:15] published another version a simplified
[27:17] version basically of battle twins called
[27:19] vicrag which turned out to be quite
[27:21] good. uh and then simultaneously another
[27:23] group some of our colleagues at fair
[27:25] paris were working on uh uh similar
[27:28] methods which eventually came to be
[27:31] known as dino uh dino v1 v2 v3 now have
[27:36] a new version which is not called dino
[27:38] anymore uh and and this is also a
[27:40] jetting uh technique so so it's really
[27:44] clear john embedding
[27:46] was better for represent learning you
[27:49] know right
[27:50] >> self-supervised learning to to represent
[27:52] images.
[27:53] >> The Dino V3 paper released in August
[27:56] 2025 marked an important turning point
[28:00] achieving a very near state-of-the-art
[28:02] image at accuracy of 88.4%
[28:05] using a joint embedding architecture.
[28:08] As the authors say in their paper, all
[28:11] in all, this is the first time that a
[28:13] self-supervised model has reached
[28:15] comparable results to weekly and
[28:17] supervised models on image
[28:18] classification.
[28:20] The quality of representations that Dino
[28:23] V3 is able to learn without access to
[28:25] any human generated labels is
[28:27] astounding. Dino outputs an embedding
[28:29] vector for each patch of image that it
[28:31] analyzes. If I take this image of myself
[28:35] and take Dino's embedding vector from
[28:37] this image patch on my hand and compare
[28:39] this embedding vector to the rest of the
[28:41] patches in the image, visualizing how
[28:43] similar each patch is to the hand patch
[28:46] using a color map. Dino does a
[28:48] remarkably good job segmenting my hand
[28:50] from the background. Here's the same
[28:52] approach applied to a ball, a cat, and a
[28:57] book.
[28:58] Following the success of Barlo twins
[29:00] Vicreg and Dinov1, in 2022, Lun brought
[29:04] these and many other threads together
[29:06] into a 60-page position paper called a
[29:09] path towards autonomous machine
[29:11] intelligence. Unlike the great majority
[29:13] of Lun's papers where he works on
[29:16] specific and technical pieces of machine
[29:17] learning theory or practice, a path
[29:20] towards autonomous machine intelligence
[29:22] takes a holistic first principles
[29:24] approach to how we should build
[29:26] intelligent machines. Lun begins by
[29:29] arguing that our current approaches to
[29:30] AI are nowhere near the capabilities of
[29:33] human learning, giving the example of a
[29:36] teenager that can learn to drive a car
[29:37] in around 20 hours of practice. How is
[29:40] it that we have those millions of hours
[29:42] of training data where we have we can
[29:45] train kind of level two system with it
[29:47] which is what Tesla is doing basically.
[29:48] >> Yeah.
[29:49] >> Um but
[29:51] >> nowhere near level three, four, five.
[29:53] Okay. Uh yet a 17-year-old can learn to
[29:56] drive in a few hours of practice. Like
[29:58] how does that happen, right? Shouldn't
[30:00] we figure out what the what's the secret
[30:02] there?
[30:03] >> And my guess about it is the secret is
[30:05] role models. Lacun's billion-dollar bet
[30:08] is that the missing piece of modern AI
[30:10] is world models. Models that make
[30:13] predictions about the physical world. As
[30:16] he says in his 2022 position paper,
[30:19] common sense can be seen as a collection
[30:20] of models of the world that can tell an
[30:23] agent what is likely, what is plausible,
[30:25] and what is impossible. Using such world
[30:28] models, animals can learn new skills
[30:31] with very few trials. They can predict
[30:33] the consequences of their actions. They
[30:36] can reason, plan, explore, and imagine
[30:38] new solutions to problems. Lun goes on
[30:41] to argue that joint embedding
[30:43] architectures offer the right foundation
[30:45] to build world models on top of.
[30:48] >> So, JPA means joint embedding predictive
[30:50] architecture and it's you you take an
[30:53] observation in the world and then the
[30:55] next observation in the world. Uh you
[30:57] run them through encoders. So this is
[30:59] like a joint embedding type architecture
[31:01] and then you have a predictor that tries
[31:02] to predict that the state at time t plus
[31:04] one from the state at time t and you
[31:06] might condition this on an action and
[31:08] now you have a world model
[31:09] >> as a concrete example instead of using a
[31:12] generative architecture to predict the
[31:14] pixel values in the next frame of video.
[31:16] We can map the video and next frame to
[31:19] embeddings and then train a predictor
[31:21] model to predict the embedding of the
[31:23] next frame given the embedding of the
[31:25] video. In this implementation, the JEPA
[31:28] architecture frees the model of the
[31:30] intractable task of predicting every
[31:33] pixel in the next frame of video and
[31:35] theoretically allows the predictor to
[31:37] focus on predicting only the salient
[31:39] features of the scene that make it
[31:41] through the encoder. Jan gives a nice
[31:43] example here. If you train a geology
[31:46] model, you know, to predict what's going
[31:47] to happen in a dash cam video, uh, it
[31:51] will spend most of its resources
[31:52] predicting the random motion of the
[31:54] leaves on the trees that bord bordering
[31:55] the road and and those are things that
[31:58] are essentially not predictable, but
[31:59] they have a lot of pixels, you know,
[32:01] that move around.
[32:03] >> As Jan mentioned earlier, we can take
[32:05] Jeepo one step further by conditioning
[32:07] on actions. In the VJEPA 2 paper, which
[32:10] we'll dig into in part two, the team
[32:12] conditions a JEPA model on the action
[32:14] signals sent to a robot arm. So, the
[32:18] JEPA model sees a sequence of images of
[32:20] the robot's arm and environment and then
[32:22] is trained to predict the embedding of
[32:24] the next video frame, but is also given
[32:27] the control signals that are sent to the
[32:28] robot arm. This allows the predictor to
[32:31] learn to predict how various control
[32:33] signals will change the robot arm's
[32:35] position in the embedded image.
[32:38] This learned world model can then be
[32:40] used for robot planning and control.
[32:43] Given an image of some goal state, for
[32:45] example, moving a cup off of a platform,
[32:48] this image is passed into the next frame
[32:50] encoder, resulting in an embedding of
[32:52] the goal state of the robot. From here,
[32:55] a controls algorithm can be used to
[32:57] explore the world model's predictions
[32:59] given various hypothetical actions and
[33:02] find a set of actions that will lead the
[33:04] model's predicted future state to match
[33:06] its goal state. As Jan says, this is
[33:09] really a new twist on an old idea.
[33:11] >> You build a model that gives you the
[33:13] state of the world at time t plus one as
[33:15] a function of the state of the world at
[33:16] time t and an action you imagine taking
[33:18] or intervention or control, right? And
[33:21] then if you have this you can uh predict
[33:24] the outcome of a sequence of actions and
[33:26] you can by optimization you can figure
[33:27] out an optimal sequence of actions to
[33:30] arrive at a particular um outcome.
[33:33] Right? This is classical optimal
[33:34] control. This is you know this is going
[33:36] back to the late 50s in the Soviet Union
[33:40] early 60s in the in the west.
[33:43] >> Very classical stuff.
[33:44] >> Yeah.
[33:45] >> What is not classical is you learn the
[33:47] model. You use machine learning to learn
[33:49] the model.
[33:50] >> Right. Yeah,
[33:50] >> what is even less classical is you learn
[33:53] a representation of the input that
[33:56] computes a state an abstract state
[33:59] representation and you learn the you
[34:02] know the the model in that uh in that
[34:05] state and that's JPA
[34:09] but will Jeepa or other world model
[34:11] based approaches really overtake large
[34:13] language models since lacun first
[34:16] proposed Jeppa in 2022 the architecture
[34:19] has been applied by various teams to a
[34:21] wide range of problems.
[34:23] How exactly do these models stack up? In
[34:27] part two, we'll dive deeper into VJeppa
[34:29] 2 to get a sense for what's really
[34:31] happening inside the models embedding
[34:33] space and see how VJA 2 fares as a
[34:36] robotics control algorithm against
[34:38] rapidly advancing VLA approaches.
[34:41] We'll also explore VLJA which solves
[34:44] many of the same vision language
[34:46] problems we solve today with multimodal
[34:48] LLMs but in a very different way and
[34:51] with impressive results. Finally, we'll
[34:53] spend some time on an implementation of
[34:55] Jeepa called layworld model. Layworld
[34:58] model gives perhaps the most complete
[35:00] albeit early picture of what Jeepa based
[35:02] systems can do. Until next time, I'll
[35:05] leave you with Yan's take. Okay, then
[35:07] let me make a controversial statement
[35:10] that again is going to get me a lot of
[35:11] friends in Silicon Valley. Um, I do not
[35:15] understand how you can even think of
[35:17] building an agentic system without a
[35:21] agentic system having the ability of
[35:24] predicting the consequences of its
[35:25] actions.
[35:27] >> Okay? And a VA doesn't doesn't do that.
[35:30] >> Sure.
[35:30] >> Right. Airlines do not have world
[35:32] models. They cannot predict the
[35:33] consequences of their actions
[35:34] beforehand. they just take the action
[35:36] and then
[35:39] deluj as uh you know as some famous
[35:43] French kings said. So uh if you really
[35:47] want to build reliable agentic systems,
[35:50] they absolutely have to be able to
[35:52] predict the consequences of their
[35:53] actions so that they can plan a sequence
[35:55] of actions to do something first of all
[35:57] to uh fulfill the task that they are
[36:01] being asked to fulfill but also uh
[36:04] perhaps to you know guarantee some
[36:06] safety guard rails. Sure.
[36:07] >> Right.
[36:08] >> And the inference process now becomes a
[36:10] search as opposed to just an
[36:12] autogressive prediction.
[36:13] >> Right. Uh, so that's a world model. That
[36:16] the whole idea of a world model.
[36:19] >> If you enjoyed this video, check out the
[36:21] Welch Labs illustrated guide to AI. Its
[36:25] cover produces highly consistent Dino
[36:27] representations, so you know it has to
[36:29] be good. The book is beautifully
[36:32] illustrated and is a great way to dig
[36:34] deeper into many of the topics we
[36:35] touched on in this video. Chapter 5 on
[36:38] Alexnet is a great way to learn more
[36:40] about embedding vectors and the rise of
[36:42] deep learning.
[36:44] Chapter six on neural scaling laws takes
[36:46] a deeper look at the fascinating buildup
[36:48] from GPT1 to GPT3 at OpenAI.
[36:52] Chapter 9 covers diffusion models which
[36:55] are able to reconstruct highly accurate
[36:57] pixel level representations of images
[36:59] and video but with some notable
[37:01] trade-offs.
[37:03] Chapters 1 through 4 give some great
[37:05] background on all these topics covering
[37:07] the fundamentals of neural networks back
[37:09] propagation and deep learning.
[37:12] Each chapter includes thought-provoking
[37:14] exercises and supporting code. The book
[37:16] is now shipping to 24 countries. You can
[37:19] pick up a copy today at welchlabs.com.