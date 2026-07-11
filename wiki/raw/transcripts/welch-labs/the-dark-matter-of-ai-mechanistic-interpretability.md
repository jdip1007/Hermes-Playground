---
source_url: https://www.youtube.com/watch?v=UGO_Ehywuxc
ingested: 2026-07-09
video_id: UGO_Ehywuxc
title: The Dark Matter of AI [Mechanistic Interpretability]
series: None
---

[00:00] how would you know if a large language
[00:01] model was lying to you if you give chat
[00:04] GPT a certain phrase and ask it to
[00:06] forget the phrase it will claim that it
[00:08] has however since the phrase is part of
[00:10] the model's context window this is
[00:12] actually impossible and if you Badger
[00:15] chat GPT enough it will admit that it
[00:17] actually does still know the phrase and
[00:19] repeat it back to you although we can
[00:21] and do train our AI assistants like chat
[00:23] GPT to be helpful and honest through
[00:25] specific examples we have no direct
[00:28] access or control over model Concepts or
[00:30] behaviors like truthfulness this problem
[00:33] of llm interpretability is an active
[00:35] area of research one of the most
[00:37] promising approaches involves extracting
[00:39] model features using a separate learning
[00:41] algorithm called a sparse Auto encoder
[00:44] these extracted features often
[00:45] correspond to human understandable
[00:47] Concepts like cats dogs Wi-Fi networks
[00:50] and more complex Concepts like internal
[00:53] conflict remarkably once we have a
[00:55] feature we can increase or decrease its
[00:57] strength in the model it was extracted
[00:59] from
[01:00] if we increase the value of the internal
[01:02] conflict feature in anthropics CLA model
[01:05] and ask it to forget a phrase it will
[01:07] immediately admit that it can't actually
[01:09] forget words examples like this are
[01:12] compelling but as one of the key authors
[01:14] of this work Chris Ola has pointed out
[01:16] we've only been able to extract a tiny
[01:18] portion likely less than 1% of the
[01:22] concepts that we know large language
[01:24] models must know about Chris uses a
[01:26] great analogy here the features we
[01:29] haven't been able to to extract yet
[01:30] maybe a kind of dark matter of
[01:32] interpretability the feature extraction
[01:34] gives us a telescope allowing us to see
[01:37] the brightest stars in the models
[01:39] Universe we may be able to build better
[01:41] and better telescopes and fully
[01:43] understand what's going on in large
[01:44] language models or it might be the case
[01:48] that a significant portion of what these
[01:49] models have learned can only be observed
[01:52] indirectly but why is it so difficult to
[01:55] understand how these models work in the
[01:57] first place why do we need to train a
[01:59] completely separate model to begin to
[02:01] make sense of what a language model has
[02:03] learned why can't we just train these
[02:05] models to be understandable in the first
[02:07] place why are we only able to extract a
[02:10] tiny portion of all model features and
[02:13] why can't we just scale up sparse Auto
[02:15] encoders to peer deeper and deeper into
[02:17] the universe of language
[02:19] models let's follow the path of some
[02:21] text through a large language model
[02:23] we'll start with the phrase the
[02:25] reliability of Wikipedia is vary and see
[02:27] if we can make sense of how the model
[02:29] decides what to say next we'll use Gemma
[02:31] 2B which is a scaled down version of
[02:34] Google's Gemini model first each of the
[02:36] six words in our phrases is converted
[02:38] into a token from Jemma's vocabulary and
[02:41] each token is mapped to a vector of
[02:42] length
[02:44] 234 these vectors are stacked together
[02:46] into a matrix of Dimensions 6X 2304 and
[02:50] passed into the first layer of
[02:52] Gemma each layer of language models like
[02:54] Gemma consist of an attention and
[02:56] multi-layer perceptron compute block
[02:58] these compute blocks return new new
[03:00] matrices of the same size as their
[03:01] inputs so after passing our 6X 23 or4
[03:05] input Matrix into the attention Block in
[03:06] our first layer of the model we get back
[03:09] a new 6X 2304 Matrix we then add this
[03:13] Matrix to our original input Matrix and
[03:16] the result becomes the input to our next
[03:18] compute block the output of this block
[03:21] again a 6X 234 Matrix is added to our
[03:24] input just as we did before completing
[03:27] the first layer of Gemma this output is
[03:30] then passed into the second layer of
[03:31] Gemma which does the exact same thing
[03:34] just using different learned weight
[03:36] values we repeat this process again and
[03:38] again with Gemma incrementally
[03:40] transforming its input Matrix layer by
[03:42] layer into a new Matrix of the same size
[03:46] this Matrix we keep updating by adding
[03:48] the outputs of each compute block to is
[03:50] called the residual stream after passing
[03:52] through all 26 layers to figure out what
[03:54] gemo is going to say next we just take
[03:57] the last row of the final Matrix and map
[04:00] it back to a word interestingly to do
[04:02] this we multiply the last row of our
[04:04] final matrix by an unembedded Matrix
[04:07] which results in a new Vector of length
[04:10] 256,000 where every entry corresponds to
[04:12] a single token in jma's 256,000 token
[04:16] vocabulary this Vector is interesting
[04:18] because after normalizing with a soft
[04:20] Max function it gives us the probability
[04:23] according to Gemma of each token in
[04:24] Jim's vocabulary occurring next we can
[04:27] rank these tokens by their probabilities
[04:29] and get a sense for what Jemma thinks
[04:31] about the reliability of
[04:33] Wikipedia the most probable next token
[04:35] is the word important with a probability
[04:37] of 20.21% we can get Gemma to expand on
[04:42] this by pending the vector for the word
[04:44] important to our original input and
[04:46] passing this new slightly larger Matrix
[04:48] through Gemma to find the next word in
[04:49] the sequence repeating this process we
[04:52] see Gemma giving a nuanced take on a
[04:55] Wikipedia as we would expect from a
[04:57] well-tuned
[04:58] model however the next word choice of
[05:00] important was only assigned a
[05:02] probability of 20.21% and Jemma's other
[05:05] probable options lead us down very
[05:07] different paths with a probability of
[05:10] 11.16% Gemma will tell us that the
[05:13] reliability of Wikipedia is very high or
[05:16] Gemma could go the other way and tell us
[05:18] that the reliability of Wikipedia is
[05:20] very low questionable or poor with
[05:23] probabilities of 10.8 9.48 and
[05:26] 5.47%
[05:28] respectively these lower probability
[05:30] options are important because production
[05:32] systems generally do not just pick the
[05:34] most likely next token this often leads
[05:37] to uninteresting or unhelpful responses
[05:40] instead next tokens are sampled from a
[05:42] modified version of the model's
[05:43] probability distribution so in practice
[05:46] this version of Gemma will give us
[05:47] different takes on the reliability of
[05:49] Wikipedia some nuanced some positive and
[05:52] some skeptical now note that so far
[05:55] we're not using the instruction tuned
[05:57] version of Gemma this final version of
[05:59] the the model includes a number of
[06:00] posttraining steps to better align Gemma
[06:03] with the behaviors we expect from an AI
[06:05] assistant interestingly if we switch to
[06:07] the instruction tuned version this
[06:09] increases the probability of measured
[06:11] takes such as the reliability of
[06:13] Wikipedia is very much a topic of debate
[06:17] there are still skeptical takes that
[06:18] Gemma could deliver but they are less
[06:20] likely after instruction tuning
[06:23] posttraining steps like these used to
[06:24] tune Gemma have proven reasonably
[06:26] effective it's shaping the behaviors we
[06:28] want from AI assist
[06:30] however these techniques do not give us
[06:32] Direct Control or understanding of
[06:34] specific model behaviors a more direct
[06:36] approach is to open up the model itself
[06:39] and try to figure out exactly which
[06:40] parts are creating specific
[06:42] behaviors where exactly in jima's 2
[06:45] billion parameters spread across 26
[06:47] layers has Jimma decided that Wikipedia
[06:50] is reliable or not a recent wave of
[06:53] these efforts popularized under the name
[06:55] mechanistic interpretability by Chris
[06:57] Ola has made impressive progress
[07:00] let's apply some ideas from mechanistic
[07:02] interpretability to our gyma model and
[07:04] see if we can make sense of what's going
[07:07] on putting together the Gemma
[07:09] walkthrough for this video required a
[07:10] ton of hacking on projects like this I
[07:13] really value uninterrupted Focus time
[07:15] which this video sponsor in cogy has
[07:17] really helped me with as a dad of two
[07:19] young kids my phone generally needs to
[07:21] be on Legit stuff comes up all the time
[07:24] but spam calls and texts can be a huge
[07:26] distraction a couple of months ago when
[07:28] I was considering during working with
[07:30] incog on this video I signed up for an
[07:32] account and I couldn't be happier with
[07:34] the results I'm getting far fewer spam
[07:36] texts and calls and more uninterrupted
[07:39] Focus time the way incog does this is
[07:42] really impressive after signing up for
[07:44] an account you give incog permission to
[07:46] work on your behalf to contact data
[07:47] Brokers to remove your data which
[07:49] Brokers are generally legally obligated
[07:51] to do upon request from here you get
[07:53] this great dashboard that tracks all the
[07:56] removal requests and progress It's
[07:58] really impressive my data has been
[08:00] removed from 115 separate data Brokers
[08:02] so far this would be incredibly
[08:05] timeconsuming for me to do manually in
[08:07] the United States we also have these
[08:09] people search sites where for a small
[08:11] fee anyone can look up information about
[08:13] you like your address email phone number
[08:15] education employment history social
[08:17] media accounts and so on it's pretty
[08:19] wild I signed up for an account on one
[08:21] of these sites it's crazy how much
[08:23] information I was able to find on my
[08:25] wife who I have not yet added to my
[08:27] incog account which I will be doing they
[08:29] have a great family and friends plan by
[08:32] comparison after being an incog customer
[08:34] for a couple of months impressively I
[08:36] wasn't able to find any records of
[08:38] myself on the same people search site
[08:40] you can get a great deal on incog 60%
[08:42] off an annual plan by using the code
[08:44] Welch Labs or following the link in the
[08:46] description below plus it helps me
[08:48] continue to make great content huge
[08:51] thanks to incog for sponsoring this
[08:52] video and helping me take back my data
[08:55] from data Brokers and get more quality
[08:57] Focus time if incog sounds like a good
[08:59] good fit for you please check it out it
[09:01] really helps me out now back to the dark
[09:04] matter of AI let's apply some ideas from
[09:07] mechanistic interpretability to our
[09:09] gimma model to get a better sense for
[09:11] how these techniques work let's
[09:13] visualize our text as it passes through
[09:15] the model recall that our six-word
[09:17] prompt the reliability of Wikipedia is
[09:20] vary is converted into a 6X 2304 Matrix
[09:23] and each block of Gemma adds a new 6X 23
[09:26] or 4 Matrix to this Matrix and this
[09:29] modif Matrix is known as the residual
[09:31] stream as it moves through the
[09:33] model after the final layer the last row
[09:36] of the residual stream is converted back
[09:38] into a token and becomes what Gemma says
[09:40] next let's visualize this final row of
[09:43] the residual stream as it moves through
[09:45] the model visualizing a vector of 234
[09:48] floating Point numbers is a bit tricky
[09:51] let's rearrange our Vector into a 48x 48
[09:53] Matrix and visualize each number as the
[09:56] intensity of a pixel in an image to
[09:58] hopefully make it easier to spot
[10:00] patterns in our data as it moves through
[10:02] the
[10:03] model before our first layer our Vector
[10:06] looks like this with a few large
[10:08] positive and large negative values that
[10:10] stand out in our image note that we
[10:12] don't have to wait till the end of our
[10:14] model to map this Vector back to a token
[10:17] at any point we can normalize this
[10:18] vector and multiply by our unembedded
[10:20] Matrix as we would at the end of the
[10:22] model to see what token our Vector
[10:25] represents generally this Vector would
[10:27] correspond to the word vary with a prob
[10:29] probability of 100% because we haven't
[10:31] done anything to our input Matrix yet
[10:34] and this last row of our Matrix is just
[10:35] the mapping or embedding of the last
[10:37] word in our phrase which is the word
[10:40] vary however this version of Gemma uses
[10:42] a soft cap function before producing
[10:44] final probabilities which limits the
[10:47] model's confidence in any single next
[10:49] word interestingly the effect here is
[10:51] for the model to predict variance of the
[10:53] word vary including different
[10:54] capitalizations and even different
[10:57] languages let's see how Jim is first
[10:59] compute block changes our embedding
[11:01] vector image the output of the attention
[11:04] Block in the first layer of Gemma looks
[11:05] like this and when we add it to our
[11:08] residual stream it now looks like this
[11:11] if we map our new Vector to a token we
[11:14] don't see much change with variance of
[11:16] the word vary now being predicted with
[11:18] slightly different probabilities so if
[11:20] our model was only composed of this
[11:22] compute block the next word predicted
[11:24] would be the word vary so Jimma would
[11:26] tell us that the reliability of
[11:28] Wikipedia is very very veryy and we do
[11:31] often see word repetition like this in
[11:32] smaller or poorly performing language
[11:35] models adding the output of the
[11:37] multi-layer perceptron Block in our
[11:38] first layer to the residual stream our
[11:41] Vector now looks like this and still
[11:43] maps to variance of the word vary we see
[11:46] similar behavior all the way through the
[11:48] 15th layer of the model note that this
[11:50] does not mean that nothing is happening
[11:52] in the first 14 layers remember that
[11:54] we're only visualizing the last row of
[11:56] our residual stream Matrix and our
[11:58] residual stream is changing just not
[12:01] enough to flip our top predictions yet
[12:03] around the 21st layer of the model we
[12:06] see for the first time expressions of
[12:07] Doubt or skepticism with Jimma telling
[12:10] us that the reliability of Wikipedia is
[12:12] very questionable with a probability of
[12:14] 9% after the 21st layer perhaps we can
[12:18] isolate some doubting or skepticism
[12:20] behavior in this layer having a close
[12:22] look at the output of the multi-layer
[12:24] perceptron Block in the 21st layer we
[12:26] see large values at the indices of 1393
[12:29] 3 1945 257 and a few others each of
[12:33] these locations corresponds to the
[12:35] location of a single neuron in this
[12:37] layer maybe one or more of these neurons
[12:40] has learned to capture doubt or
[12:42] skepticism one simple way to test this
[12:44] idea is to directly modify the values of
[12:46] each of these neurons and see how it
[12:48] impacts the model outputs if we take
[12:51] neuron number 1393 and fix its output
[12:54] value to minus 160 this is about twice
[12:57] its observed maximum and pass our text
[12:59] through our model again with this
[13:01] modification in place our final outputs
[13:03] do change with high moving up in the
[13:07] rankings if we reverse our intervention
[13:09] and clamp our output to positive 160 we
[13:11] see our Trend reverse with low
[13:14] questionable and poor moving
[13:15] significantly up in the rankings so
[13:18] increasing the output of neuron 1393 in
[13:20] layer 21 increases Jemma's trust in
[13:22] Wikipedia and reversing its outputs
[13:24] increases its skepticism or doubt so
[13:27] have we found a specific gem neuron that
[13:29] controls trust or in Reverse doubting or
[13:32] skeptical Behavior another way to test
[13:35] this idea is to search for other
[13:37] examples of text that caus neuron 1393
[13:39] and layer 21 to Output large values if
[13:43] we found a doubting or skeptical neuron
[13:45] then the text that causes this neuron to
[13:46] maximally activate should reflect this
[13:50] searching through 100,000 examples from
[13:52] the pile data set and collecting the
[13:54] examples that maximally activate neuron
[13:56] 1393 these examples seem to have nothing
[13:59] to do with doubt or skepticism and
[14:01] instead seem to correspond to examples
[14:03] of capital letters in acronyms or proper
[14:05] nouns in various
[14:07] context we've reached our first big
[14:09] hurdle in interpreting Gemma clearly
[14:12] this neuron has some bearing on the
[14:14] model's doubting or skeptical Behavior
[14:16] but the examples that this neuron
[14:18] responds most strongly to are related to
[14:20] a seemingly unrelated
[14:22] concept this phenomenon of single
[14:24] neurons and large language models
[14:26] corresponding to multiple seemingly
[14:27] unrelated Concepts has been observed
[14:30] across a broad range of models and is
[14:32] known as polys
[14:34] semanticity interestingly polys
[14:36] semanticity occurs much more frequently
[14:38] in language models than in Vision
[14:40] models specific neurons and vision
[14:42] models have been shown to respond
[14:43] uniquely to things like faces cars and
[14:45] many many more recognizable Concepts in
[14:49] 2022 Chris Ola and the team at anthropic
[14:51] published an interesting hypothesis to
[14:53] explain this observed polys semanticity
[14:56] the idea is that language models are
[14:57] able to learn more con Concepts than
[14:59] they have neurons essentially by
[15:01] representing Concepts using specific
[15:03] combinations of neurons the team calls
[15:05] this idea superposition so Concepts may
[15:08] be spread across multiple neurons and
[15:10] layers in Gemma if we can't isolate
[15:13] Concepts and behaviors to certain layers
[15:15] or neurons how can we hope to understand
[15:17] or control language models one option is
[15:20] to modify the model architecture to
[15:22] encourage or Force the model to have
[15:24] fewer neurons fire for any given input
[15:27] ideally this would stop the model from
[15:28] spreading Concepts across multiple
[15:30] neurons the anthropic team tried this in
[15:33] 2023 and found that models still
[15:35] exhibited polys semanticity even in
[15:37] extreme cases where they forced only a
[15:40] single neuron to fire at a time another
[15:42] option is to try to figure out which
[15:44] combinations of neurons respond to
[15:46] certain Concepts perhaps neuron 1393 and
[15:49] layer 21 combined with other neurons
[15:51] will cleanly represent the concept of
[15:53] Doubt but how can we possibly figure out
[15:56] which combinations of neurons map
[15:58] cleanly to which
[16:00] Concepts remarkably there is a simple
[16:02] model that we can train to learn these
[16:04] mappings called a sparse
[16:06] autoencoder if the superposition
[16:08] hypothesis is true we should be able to
[16:11] take some combination of the outputs of
[16:13] the neurons in a given layer and this
[16:15] combination of neurons should respond
[16:16] very strongly to a single specific
[16:18] concept and respond very minimally to
[16:20] all other
[16:22] Concepts most sparse auto encoders used
[16:24] today in mechanistic interpretability
[16:26] work by hooking them up to a specific
[16:28] point in the model
[16:29] such as the output of a certain layer or
[16:31] the residual stream at a certain
[16:33] location so if we take the output of the
[16:35] 21st layer of Gemma where Gemma started
[16:38] exhibiting doubting Behavior the idea
[16:40] here is that we can take these 234
[16:42] neuron outputs and find some combination
[16:45] of these outputs that cleanly responds
[16:47] to examples of doubt we can take a
[16:49] single combination of our outputs by
[16:51] multiplying our neuron outputs by a new
[16:53] waiting Vector of length 2304 where each
[16:56] entry in the waiting tells us how much
[16:58] of each neuron output to take we can
[17:00] then add these results together to give
[17:02] us a final output value that should
[17:04] correspond to the overall strength of
[17:06] our concept now per the superposition
[17:09] hypothesis our model represents more
[17:11] Concepts than it has neurons so we need
[17:13] more than 2,34 of these waiting vectors
[17:16] to tease out all the different concepts
[17:19] let's try modeling
[17:20] 16,384 different concepts so we need
[17:24] 16,384 separate vectors we can stack all
[17:27] of these waiting vectors into a single
[17:29] new Matrix of Dimension 2304 by 16 384
[17:33] where each column represents the
[17:34] contributions of our 234 neurons to each
[17:38] concept multiplying our neuron output
[17:40] vector by our waiting Matrix yields a
[17:42] new Vector of length
[17:44] 16,384 where each entry should
[17:46] correspond to the strength of a specific
[17:49] concept now how do we learn the weights
[17:51] for our new Matrix that will allow us to
[17:53] cleanly map neurons to concepts for any
[17:56] given input example we know that we only
[17:58] want a very small number of our
[18:00] 16,384 Concepts to be active at once
[18:04] otherwise we' run into the same polys
[18:05] semanticity issue we saw with neurons
[18:08] this is where the sparsity comes in
[18:11] sparse autoencoders work by forcing most
[18:13] of the values in our concept Vector to
[18:15] be zero or near zero and then using the
[18:17] remaining values to reconstruct the
[18:19] original input reconstruction of the
[18:21] original input consists of mapping from
[18:23] Concepts back to neuron values which we
[18:26] can do by multiplying by another weight
[18:28] Matrix
[18:29] this time of Dimension 16384 by
[18:32] 2304 so our sparse Auto encoder works by
[18:35] mapping our neuron outputs to potential
[18:37] Concepts better known as features by
[18:39] multiplying by a weight Matrix and then
[18:42] forcing most of the values in the
[18:43] resulting feature Vector to be zero or
[18:45] near zero and then taking these few
[18:48] remaining outputs and mapping them back
[18:49] to neuron outputs by multiplying by
[18:51] separate weight Matrix if the
[18:53] superposition hypothesis is correct and
[18:56] our sparse autoencoder is working well
[18:58] then our output should be a reasonably
[19:00] faithful reconstruction of the original
[19:02] neuron output sparse autoencoders are
[19:05] trained to minimize this reconstruction
[19:07] loss let's see how sparse autoencoders
[19:09] apply to our gemo Wikipedia example the
[19:12] Google deepmind team recently released a
[19:14] project called gemos scope which
[19:16] includes over 400 separate sparse Auto
[19:18] encoders trained on data from various
[19:21] locations in the model and across
[19:22] variations of Gemma let's take the
[19:24] sparse Auto encoder trained on the
[19:26] outputs of the 21st layer of Gemma that
[19:28] we've been working with
[19:29] let's pass in our example text into our
[19:31] model pass the output of our 21st layer
[19:33] into our trained sparse Auto encoder and
[19:36] see which elements in our concept or
[19:37] feature Vector are activated we can
[19:40] visualize our feature Vector in the same
[19:42] way we visualized our embedding vectors
[19:44] by reshaping it into a 128x 128 grid and
[19:47] displaying it as an image as expected
[19:50] our feature Vector is much more sparse
[19:52] than our embedding
[19:53] vectors now let's see if we can make
[19:56] sense of the concepts or features that
[19:58] our spar Auto encoder has learned a
[20:01] challenge with sparse autoencoders is
[20:02] that we don't know ahead of time what
[20:04] actual concept any given element in our
[20:06] feature Vector corresponds to we can see
[20:09] that features 7344 8353 and 8249 have
[20:14] high values for our Wikipedia example
[20:17] but what concepts in our text are these
[20:18] features responding
[20:20] to as we did with individual neurons we
[20:23] can get a sense for what individual
[20:24] features represent by searching for
[20:26] examples of text that maximally ACC
[20:28] activate a given feature part of the
[20:30] gyos scope project includes launching on
[20:32] a platform called neuron pedia which
[20:35] allows us to quickly see what examples
[20:37] maximize any feature in any sparse Auto
[20:39] encoder released with the gemos scope
[20:41] project looking at feature 8249 for our
[20:44] sparse Auto encoder we do see many
[20:47] examples of text where questioning or
[20:48] uncertainty are expressed we can also
[20:51] amplify or reduce this feature's impact
[20:53] on the model just as we did with
[20:55] individual neurons clamping feature 82
[20:58] 49's output to a constant value of 100
[21:01] impacts Jim's next word prediction as
[21:03] expected increasing the probability that
[21:05] jimo will tell us that the reliability
[21:07] of Wikipedia is questionable we can ask
[21:10] Jimma to generate more text with our
[21:12] modified feature in place and see that
[21:14] the steered version of the model is
[21:16] highly doubtful in questioning of
[21:17] Wikipedia's
[21:19] reliability if we crank up this feature
[21:21] to a constant value of 500 we see that
[21:24] Gemma starts to just Babble mostly with
[21:26] variance of the word question
[21:29] so by learning to map neuron outputs to
[21:31] sparse features sparse autoencoders are
[21:33] able to recover human understandable
[21:35] features that respond consistently to
[21:37] specific Concepts in text and can even
[21:40] be used to control Model Behavior in
[21:41] predictable ways sparse autoencoders
[21:44] have been applied to a range of language
[21:46] models with impressive results in 2024
[21:50] the anthropic team showed that features
[21:51] extracted from cloud 3 sonnet are even
[21:53] multilingual and multimodal a feature
[21:56] for the Golden Gate Bridge responds to
[21:58] reference ref es to the bridge in
[21:59] multiple languages and even to images of
[22:02] the bridge the anthropic team has scaled
[22:04] up their Auto encoders to extract around
[22:06] 13 million separate features and a team
[22:09] at open AI has trained a 16 million
[22:11] feature Auto encoder on the GPT 4
[22:13] residual stream however as Chris Ola has
[22:16] pointed out these millions of features
[22:19] appear to just be scratching the surface
[22:22] the anthropic team has found features
[22:24] for specific neighborhoods in San
[22:25] Francisco but the Claud model these
[22:27] features were extracted from knows way
[22:29] more granular information about the city
[22:32] like the intersections of streets which
[22:34] do not show up in the extracted
[22:36] features large language models appear to
[22:39] know far more Concepts than we've been
[22:40] able to extract so far we may be able to
[22:44] Simply continue scaling sparse
[22:45] autoencoders as we've scaled language
[22:47] models but there are a number of
[22:49] theoretical and practical obstacles that
[22:51] may block this path it's possible that
[22:54] the computational cost of extracting
[22:56] extremely rare features will become
[22:57] prohibitively High leaving these rare
[23:00] features as an unobserved dark matter
[23:02] that has to be observed indirectly the
[23:05] current sparse autoencoder Paradigm
[23:07] effectively focuses on a single location
[23:09] in the model at a time leaving it
[23:11] incapable of disentangling cross layer
[23:14] superposition there's work actively
[23:16] underway from the anthropic team and
[23:17] others on a new approach called sparse
[23:19] cross caters to address this issue
[23:22] finally as the number of features
[23:24] increases the features become more and
[23:26] more fine grained making them more
[23:28] difficult to work with you can see this
[23:30] directly when experimenting with large
[23:31] autoencoders on neuron pedia searching
[23:34] for doubt we find many many features and
[23:37] it's not clear how various choices will
[23:38] affect the model until we test them
[23:41] sparse autoencoders and other
[23:42] mechanistic interpretability approaches
[23:45] have given us incredible insights into
[23:47] large language models it will be
[23:49] fascinating to see how far we can push
[23:51] mechanistic interpretability and if the
[23:54] capabilities of large language models
[23:56] will continue to outpace our abilities
[23:58] to understand them
[24:01] [Music]