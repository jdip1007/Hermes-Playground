---
source_url: https://www.youtube.com/watch?v=D8GOeCFFby4
ingested: 2026-07-08
video_id: D8GOeCFFby4
title: The most complex model we actually understand
series: None
---

[00:00] No one understands modern AI. Each new
[00:03] little piece of text known as a token
[00:06] produced by Chat GPT is the result of
[00:08] hundreds of billions of separate
[00:10] calculations.
[00:11] The parameters used in these
[00:13] calculations are learned from data by
[00:16] training Chat GPT to predict a single
[00:18] token at a time. But somehow from just
[00:21] learning to predict the next little
[00:23] piece of text again and again across
[00:25] trillions of examples, what feels like
[00:28] real intelligence emerges?
[00:31] What pathways through the network's
[00:33] billions of computations are responsible
[00:35] for specific knowledge or abilities?
[00:38] Why do certain skills only emerge from
[00:40] models of a certain size or after
[00:42] training for a certain duration? Are
[00:45] these giant models just memorizing or
[00:47] are they actually learning?
[00:50] Today we have many compelling clues but
[00:52] no definitive answers to these
[00:54] questions.
[00:56] One interesting question we can ask is
[00:58] how much complexity do we have to strip
[01:00] away before we can really truly
[01:02] understand a model? We know how the
[01:05] individual artificial neurons that make
[01:07] up these models work. Although this did
[01:09] take some time to sort out back in the
[01:11] 1960s.
[01:13] As we connect more and more of these
[01:15] neurons together, when exactly does our
[01:17] understanding really start to break
[01:19] down? In this video, I'm going to claim
[01:22] that one specific example, groing
[01:25] modular arithmetic with a single layer
[01:27] transformer, is the most complex AI
[01:30] model that we fully understand.
[01:32] This is obviously highly subjective. If
[01:35] you have a different example that you
[01:36] think fits, please share it in the
[01:38] comments. Your answers could make for a
[01:39] fun follow-up video.
[01:42] Like many scientific discoveries, we
[01:44] stumbled onto groing completely by
[01:46] accident. The initial discovery led to
[01:49] some remarkable follow-up work that
[01:51] allows us to rigorously understand what
[01:53] the model's parameters are actually
[01:55] learning, why certain behaviors emerge
[01:58] later in training. And incredibly, we
[02:00] can even watch the model progress from
[02:02] just memorizing training examples to
[02:04] learning a robust forier space solution
[02:07] to the modular arithmetic problem. This
[02:10] example is a few years old at this
[02:12] point, but it's an amazing and still
[02:14] very relevant way to look under the hood
[02:15] of modern transformers. At the end of
[02:18] this video, we'll also look at some more
[02:20] recent fascinating results from a team
[02:22] at anthropic where the team found a
[02:25] six-dimensional manifold in the
[02:26] activations of Claude Haiku that appears
[02:29] to be responsible for handling the
[02:31] arithmetic required for the model to
[02:34] figure out when to create new lines. As
[02:36] Claude writes,
[02:39] in 2021, a research team at OpenAI was
[02:42] training small models to perform modular
[02:45] arithmetic.
[02:46] If we take a mathematical operation like
[02:48] X + Y, we can turn this operation into a
[02:51] data set by creating a table with
[02:53] various X values as our columns and
[02:56] various Y values as our rows. From here,
[02:59] we can fill in each cell with the sum of
[03:01] X and Y. 0 + 0 is 0. 0 + 1 is 1 and so
[03:06] on. The team was studying modular
[03:09] arithmetic, meaning we need to pick a
[03:11] largest number or modulus.
[03:14] When our number reaches or exceeds the
[03:16] modulus, we divide by the modulus and
[03:18] take the remainder.
[03:20] If we choose a modulus of 5, when we
[03:22] reach 1 + 4 on our table, the answer is
[03:25] actually 5 modulo 5 equals 0.
[03:30] 4 + 2 equals 6 modulo 5 giving a final
[03:33] answer of 1 and so on. The modulo
[03:36] operation gives our model some
[03:37] interesting structure to learn and
[03:40] nicely bounds the number of individual
[03:41] tokens our model needs. We know that in
[03:44] this case our answer will always be 0 1
[03:47] 2 3 or four. From here we set aside a
[03:50] portion of our data for testing and
[03:52] train on the remaining examples.
[03:55] It's worth taking a moment to consider
[03:57] what this data set really looks like
[03:58] from our model's perspective. Our model
[04:01] has one input and one output for each
[04:03] token in its vocabulary. We need five
[04:06] tokens to represent our numbers 0
[04:08] through 4, and we'll add one more token
[04:11] to represent our equal sign. We could
[04:13] also add a token for the plus sign, but
[04:16] since we'll only be training our model
[04:17] on addition, it's not needed. Having a
[04:20] token for the equal sign is helpful,
[04:22] however, as we'll see. This effectively
[04:24] gives our model a placeholder for its
[04:26] final answer. So our model has six total
[04:29] inputs, one for each token. For
[04:32] comparison, GPT5 has 200,000 inputs.
[04:36] Again, one for each token in its
[04:38] vocabulary.
[04:39] To input a math problem into our model,
[04:42] for example, 1 + 2, we pass in the first
[04:45] token in our math problem one into the
[04:48] model by switching on the one position
[04:50] and switching off all the other
[04:52] positions. This is known as one hot
[04:54] encoding and is how the model sees our
[04:57] first token. Our second token two is
[05:00] passed into our model by switching on
[05:02] the second input and switching off the
[05:04] rest. Finally, our equal sign tells us
[05:07] to switch on only the final input to our
[05:09] model.
[05:11] So the math problem 1 + 2 from the
[05:13] perspective of our model looks like its
[05:15] first input switched on then its second
[05:18] input and then its sixth input.
[05:21] Transformers like these are generally
[05:22] configured to return outputs of the same
[05:25] dimension that they're given. So our
[05:27] model's final output will also be 6x3.
[05:30] In this case, we're only going to look
[05:32] at the final column of the model's
[05:34] output. This is where we want the right
[05:36] answer to show up. And in this case, we
[05:38] want the three output to be switched on
[05:41] since 1 + 2 is three. So what our model
[05:44] is really learning is to map this
[05:46] pattern of 18 values, mostly zeros, to
[05:49] this new pattern of six values.
[05:52] Now imagine someone just handed you a
[05:54] bunch of different target input and
[05:55] output patterns. Here are the input and
[05:58] output patterns for 1 + 3= 4. Here's 2 +
[06:02] 3= 0, and so on.
[06:05] After you saw enough of these examples,
[06:08] do you think you could figure out the
[06:10] underlying structure of the problem?
[06:13] This is precisely how large language
[06:15] models work. When we pass in the text
[06:17] the capital of France is into llama, for
[06:20] example, the token for the tells us to
[06:22] switch on input 791. The token for
[06:25] capital tells us to switch on input 6864
[06:28] and so on. Moving to llama's output, the
[06:32] final column is maximized at an index of
[06:34] 12366,
[06:36] which corresponds to the token for
[06:38] Paris.
[06:39] It's easy to forget that the symbols we
[06:42] assign to our model's inputs and outputs
[06:44] have this extra meaning that we attach
[06:46] to them. But to the model, they're just
[06:48] patterns of inputs and outputs.
[06:52] Now, when the OpenAI team trained their
[06:54] model on modular arithmetic, their
[06:56] initial results were pretty
[06:57] underwhelming.
[06:59] The model was able to quickly learn to
[07:01] match the patterns in the training data,
[07:03] giving the correct output on all
[07:05] training examples. However, the model
[07:08] performed very poorly on the test set.
[07:10] It appeared that the model had simply
[07:12] memorized the training data without
[07:14] actually learning modular addition.
[07:17] But then something interesting happened.
[07:20] One of the researchers went on vacation
[07:22] but accidentally left a model training.
[07:25] Returning from vacation, the researcher
[07:27] was shocked to discover that after a
[07:29] very large number of training steps, the
[07:31] model had suddenly generalized,
[07:34] performing perfectly on both training
[07:36] and test sets.
[07:39] What mechanism could possibly be causing
[07:41] the model to perfectly fit the training
[07:42] examples after just a couple hundred
[07:44] steps, appear to lay dormant for a
[07:47] couple thousand steps, and then suddenly
[07:50] actually learn? And could similar
[07:52] dynamics happen in full-size models?
[07:56] In Robert A. Highland's 1961 novel,
[07:59] Stranger in a Strange Land, he coins the
[08:01] term grocking. The book's main
[08:04] character, a human who was raised on
[08:06] Mars and returns to Earth, uses the
[08:08] Martian word gro throughout the book.
[08:11] Grock has no direct translation from the
[08:13] far more complex Martian language. But
[08:16] one meaning is to understand something
[08:18] so thoroughly that you merge with it and
[08:21] it merges with you.
[08:23] The OpenAI team was able to replicate
[08:25] the sudden generalization phenomenon
[08:28] across a range of arithmetic operations
[08:30] and model configurations and in January
[08:33] 2022 published this paper where they
[08:36] called the phenomenon groing.
[08:38] Grocking is a provocative name but the
[08:41] phenomenon itself is shocking.
[08:44] What could be causing the model to
[08:46] suddenly perform perfectly on the test
[08:48] set? A year after the publication of the
[08:51] OpenAI groing paper, a team led by
[08:54] researcher Neil Nandanda published an
[08:56] incredibly detailed analysis of the
[08:57] phenomenon. Their paper digs deep into
[09:00] the model's parameters and activations
[09:02] to produce a very satisfying and elegant
[09:05] explanation. Nandanda and his
[09:07] collaborators studied a single layer
[09:09] transformer. This is the same
[09:11] architecture used in most large language
[09:14] models just with fewer layers. A
[09:17] transformer layer is composed of an
[09:19] attention and multi-layer perceptron
[09:21] compute block. As we saw with our toy
[09:24] example earlier, our data is fed into
[09:26] our model using one hot vectors. NAND
[09:29] used a modulus of 113.
[09:32] So the model's input vectors are of
[09:33] length 114
[09:36] with 113 positions for the digits 0
[09:38] through 112 and a final position for the
[09:41] equal sign. So to ask our model what 1 +
[09:44] 2 is, we pass in this 114x3 matrix made
[09:49] up of all zeros except for a one in the
[09:52] one spot of our first column, a one in
[09:54] the two spot of our second column, and a
[09:56] one in the equal spot of our final
[09:58] column. From here, our 113x3 matrix is
[10:02] multiplied by a matrix of learned
[10:04] weights known as an embedding matrix,
[10:06] producing three new vectors of length
[10:09] 128 each. These resulting embedding
[10:12] vectors are no longer sparse and as
[10:14] we'll see contain some interesting
[10:16] structure. From here, our embedding
[10:18] vectors are passed into our attention
[10:20] block and then our multi-layer
[10:22] perceptron compute block. The output of
[10:24] our multi-layer perceptron is of length
[10:27] 128. We multiply this output by an
[10:30] unmbbedding matrix to compute a final
[10:32] vector of length 114.
[10:35] The model's answer is given by the
[10:36] largest value in this final vector. So
[10:39] if our model is working well, its
[10:42] maximum output value should occur in the
[10:44] three position corresponding to the
[10:46] correct answer 1 + 2 equals 3.
[10:50] Training this model on modular edition,
[10:52] we see the same groing behavior observed
[10:54] by the OpenAI team with the model first
[10:57] memorizing the training data after
[10:59] around 140 steps and then generalizing
[11:02] after 7,000 training steps. Let's
[11:05] explore the model's intermediate
[11:07] outputs, better known as activations.
[11:10] Specifically, let's have a close look at
[11:12] the outputs of some of the neurons in
[11:14] the second layer of our multi-layer
[11:16] perceptron block. This layer has 512
[11:19] total neurons.
[11:21] If we pass in the problem 0 plus 0 into
[11:24] our network, the first neuron of this
[11:26] layer returns an output value of 1.17.
[11:30] Our second neuron returns an output of
[11:32] 0.6 and so on. Now let's visualize how
[11:36] these values change as we change the
[11:38] input math problem.
[11:40] Let's fix the value of x to 0 and
[11:43] explore a range of y values starting
[11:46] with 0 + 0. then 0 + 1, then 0 + 2, and
[11:50] so on. Sweeping through all 113 possible
[11:53] values for y, we see some interesting
[11:56] structure with the outputs of some of
[11:58] our neurons looking like sine waves.
[12:02] Digging deeper, let's explore the
[12:03] correlation between all the different
[12:05] pairs of these neurons.
[12:08] Let's color our points using the input y
[12:10] value to our model. So our neuron
[12:12] outputs given the input 0 0 are colored
[12:14] purple and outputs given the input 0 +
[12:17] 112 are colored yellow. From here we'll
[12:20] create a 7x7 grid of scatter plots for
[12:23] each pair of neurons. So on our second
[12:26] scatter plot on our first row for
[12:28] example we'll plot the output of our
[12:30] first neuron as the y value and the
[12:32] output of our second neuron as the x
[12:34] value. Bringing our two waves together
[12:36] like this results in a nice loop shape.
[12:39] creating the same plots for each pair of
[12:41] neuron outputs, we see more interesting
[12:43] structures.
[12:45] So our model has clearly learned some
[12:47] type of structure. But could this
[12:49] structure be related to groing? If we
[12:52] move backwards in our training process
[12:54] and visualize these structures as we go,
[12:57] we see that by the time we reach our
[12:58] model that just memorizes our training
[13:00] set, these structures completely
[13:02] disappear. So while this early model
[13:05] performs perfectly on the training set,
[13:08] we don't see any evidence of the waves
[13:10] and loops that we see after grocking. So
[13:12] perhaps these structures are related to
[13:15] why the model gro
[13:18] is sponsored by me. The Welsh Labs team
[13:21] and I have written a whole new book on
[13:23] AI. It's beautifully illustrated and is
[13:26] a great way to dig deeper into the
[13:28] topics we cover in these videos. Each
[13:31] chapter includes thoughtprovoking
[13:32] exercises and supporting code. Our first
[13:35] print run is totally sold out, but we
[13:38] have another batch coming quickly in
[13:39] January. And if you order now, I'll send
[13:41] you a discount code for a free download
[13:43] of the ebook version. Books and
[13:46] education are really near and dear to my
[13:48] heart, and we've poured a ton of effort
[13:50] into this book. I really think you're
[13:52] going to like it. Now, back to Groing
[13:55] modular arithmetic.
[13:58] The wave shapes and loops we see inside
[14:00] our model as it gro suggest that the
[14:03] model is potentially computing and
[14:04] making use of the signs and cosiness of
[14:06] our inputs x and y. If we take a
[14:10] discrete 4a transform of our activation
[14:12] pattern, we can compute the frequencies
[14:14] of the waves learned by our model. This
[14:17] first wave yields a largest frequency
[14:19] component of 8 pi over 113.
[14:22] And our third wave shows a largest
[14:24] frequency component of 6 pi over 113.
[14:27] If we plot these waves on top of our
[14:29] model's outputs, we see nice alignment.
[14:33] Let's look for these frequencies in
[14:35] other places in our model. Let's
[14:38] visualize a single value in our first
[14:40] embedding vector. Just as we did with
[14:42] the neurons in our multi-layer
[14:44] perceptron, let's plot this value as we
[14:47] sweep through a range of input values.
[14:50] Note that our first embedding vector
[14:51] only depends on our first input x. So
[14:54] here we'll sweep from x= 0 to x= 112
[14:58] while keeping y fixed at zero. We don't
[15:01] see quite the same smooth plots that we
[15:03] saw earlier. But if we compare our curve
[15:05] to a cosine wave with a frequency of 8
[15:08] pi over 113, we do see reasonably good
[15:11] alignment.
[15:13] Part of the challenge here is that this
[15:15] early signal in our network also appears
[15:17] to contain higher frequency information,
[15:20] which makes sense given that we found
[15:22] evidence of multiple frequencies later
[15:23] in our model. We could analyze the
[15:26] frequency content of our full embedding
[15:28] vectors at this stage of the model. But
[15:30] for now, let's build what's known as a
[15:32] sparse linear probe.
[15:35] If we sample the values at a few more
[15:37] positions of our embedding vector, we
[15:39] see similar semeriodic curves.
[15:42] Now it turns out that if we take a
[15:44] weighted sum of these eight curves, we
[15:47] end up with a curve that looks very
[15:48] close to a cosine curve with a frequency
[15:51] of 8 pi over 113.
[15:54] The weighted sum is very relevant here
[15:56] because taking weighted sums like this
[15:58] is a big part of what our attention and
[16:01] multi-layer perceptron blocks do.
[16:04] Meaning that these compute blocks have
[16:05] access to a very clean cosine wave. The
[16:09] signal is just spread across a few
[16:10] different locations in our model. At
[16:12] this stage,
[16:14] we can compute a similar sparse linear
[16:16] probe for the sign of x * 8 pi over 113.
[16:21] Now, our first embedding vector only
[16:23] depends on our first input x and our
[16:25] second embedding vector only depends on
[16:27] our second input y. These inputs are
[16:29] combined in our attention block. Since
[16:32] the same embedding matrix is used to
[16:34] process our three inputs independently,
[16:37] we can use the same sparse linear probe
[16:39] on our second embedding vector. And
[16:41] we'll see the same nice cosine and sign
[16:43] curves, but now as a function of y.
[16:47] So very early in the model, our model
[16:49] learns to compute the signs and cosiness
[16:52] of our inputs. But why? What did these
[16:55] functions from trigonometry have to do
[16:56] with learning modular addition?
[17:00] The modular addition problem may seem a
[17:02] bit foreign or contrived, but we
[17:04] actually do it all the time. A 2-hour
[17:07] meeting that starts at 11 a.m. will end
[17:10] at 11 + 2 modulo 12 equals 1 p.m. Analog
[17:15] clocks are implementing modular addition
[17:17] physically.
[17:19] Each hour that ticks by adds one with
[17:21] the hour hand. And the circular motion
[17:24] of the hands perfectly matches the
[17:25] modulo arithmetic problem. starting over
[17:28] when reaching 12.
[17:31] Now, as we saw when probing the neurons
[17:33] in our multi-layer perceptron, our
[17:35] network learns to form circular patterns
[17:37] in its activations.
[17:40] Could these circular structures be
[17:42] solving the modular arithmetic problem
[17:44] in the same way that an analog clock
[17:46] does?
[17:48] The signs and cosiness we see computed
[17:50] by our model in its first layer could be
[17:52] part of this puzzle. If we put the
[17:54] output of our sparse cosine probe on an
[17:57] x axis and the output of our sparse sign
[18:00] probe on the y-axis of a scatter plot,
[18:02] we get a nice circle when we sweep
[18:04] through our input values.
[18:08] However, it's not enough to learn a
[18:09] circular structure for x and y
[18:11] independently.
[18:13] Our network has to figure out how to
[18:14] actually add x and y together. Adding x
[18:18] and y may seem trivial for our model to
[18:20] learn. After all, neural networks are
[18:23] literally built from a bunch of adds and
[18:25] multiplies.
[18:26] But remember that we aren't actually
[18:28] passing in, for example, the number two
[18:31] or a direct representation of it.
[18:33] Instead, we're switching on the input to
[18:35] our model that we have labeled two.
[18:39] The network cannot just use one of the
[18:41] additions in one of its neurons to add X
[18:43] and Y together.
[18:45] What happens instead turns out to be way
[18:47] more interesting.
[18:50] It is straightforward for our attention
[18:52] layer to add together the various signs
[18:54] and cosiness computed by our first
[18:56] layer. Our attention layer could easily
[18:59] compute cosine x plus cosine of y.
[19:02] However, that's still not what we need
[19:04] to solve the problem. We need to add
[19:06] together x and y themselves
[19:09] in our clock analogy. We need to add the
[19:11] angles of the clock hands, not the signs
[19:14] and cosiness of these angles.
[19:17] Let's return to the second layer of
[19:19] neurons in our multi-layer perceptron
[19:21] compute block.
[19:23] Earlier, we explored how these neuron
[19:25] outputs changed as we varied a single
[19:27] input.
[19:29] Let's now explore how these outputs
[19:30] change as we vary both X and Y to see if
[19:34] we can figure out how our network is
[19:35] bringing these variables together.
[19:38] Again, visualizing the output of a
[19:40] single neuron. If we keep y fixed at
[19:43] zero and sweep through all possible x
[19:45] values, we get a familiar wave shape.
[19:49] Now let's add another axis to our
[19:51] visualization and plot our neurons
[19:53] output now as we vary y.
[19:57] Let's explore all combinations of values
[19:59] for x and y. With this many points, it's
[20:02] easier to visualize our neurons outputs
[20:04] as the height of a surface where the
[20:07] color of the surface corresponds to our
[20:09] neuron's output value. Like many of the
[20:12] outputs we've seen so far, our surface
[20:14] is approximately wavelike.
[20:17] What combinations of signs and cosiness
[20:19] best capture this wave structure that
[20:21] our network has learned? As we did
[20:24] earlier, we can take a 4A transform, but
[20:27] this time with respect to both X and Y.
[20:30] Extracting our top frequencies, we can
[20:33] decompose our surface into a few key
[20:35] components.
[20:37] This component is the cosine of x and
[20:40] this component is the cosine of y.
[20:43] This top component is the strongest and
[20:45] the most interesting. It's equal to the
[20:48] cosine of x times the cosine of y. So
[20:51] the strongest frequency component of our
[20:53] surface is equal to the product of the
[20:56] cosine of x and cosine of y functions
[20:58] that we saw computed earlier in our
[21:00] network.
[21:01] Now, it turns out that it's more natural
[21:03] for our network to take a sum of signs
[21:05] and cosiness than a product. I'll put a
[21:08] note about this in the description. So,
[21:10] why are we finding a strong product like
[21:12] this in the middle of our network? And
[21:15] does this get us any closer to actually
[21:17] computing the sum of X and Y?
[21:20] Remarkably, it does. Let me show you one
[21:23] more thing. Let's go one layer of
[21:25] neurons deeper into our multi-layer
[21:27] perceptron and plot the outputs of a
[21:30] neuron in this layer as a function of X
[21:32] and Y.
[21:34] We see similar wavelike shapes here, but
[21:36] the wave is less regular and it moves
[21:39] diagonally across our surface.
[21:42] This orientation of the wave is really
[21:44] important.
[21:46] Consider these top two crests where the
[21:48] output of our neuron is maximized.
[21:52] Let's move to an overhead view and look
[21:54] at the combinations of our input values
[21:56] that fall on these wave crests. The
[21:59] first crest starts at x= 0 and y= 65.
[22:03] Moving along our crest, we find
[22:05] intermediate values at x= 20 and y= 45,
[22:10] x= 40 and y = 25, x= 60 and y = 5, and
[22:16] finally x= 65 and y = 0.
[22:20] All of these pairs of inputs add to the
[22:22] same value of 65.
[22:25] So this neuron fires maximally when x +
[22:28] y equals 65.
[22:30] In its own specialized way, this neuron
[22:33] has learned to add or more precisely
[22:36] this neuron fires for any pair of inputs
[22:38] that add to 65.
[22:41] Our second wave crest starts at x= 66,
[22:44] y= 112.
[22:47] From there it moves through values like
[22:49] x= 91 and y= 87 and ends on x= 112 and y
[22:54] = 66.
[22:56] Adding these pairs together we get 178
[22:59] in each case.
[23:01] Recall that our model is trained on
[23:03] modular addition with a modulus of 113.
[23:07] Our result of 178 modulo 113 is 65.
[23:12] So this second crest also finds pairs of
[23:15] inputs that add to 65.
[23:18] But how in just one layer of neurons do
[23:21] we go from products like the cosine of x
[23:23] times the cosine of y to actually adding
[23:26] together x and y themselves.
[23:30] Here's the output of another neuron in
[23:32] the second layer of our multi-layer
[23:33] perceptron. The strongest frequency
[23:36] component here is s of x time s of y.
[23:40] Now each neuron in our following layer
[23:42] takes a weighted sum of the outputs of
[23:45] the neurons in our current layer.
[23:48] Let's consider how this weighted sum
[23:49] causes our surfaces to interact.
[23:52] We saw earlier that our first neuron's
[23:54] output has a strongest frequency
[23:56] component of cosine of x time the cosine
[23:58] of y and our new second layer neuron has
[24:01] a strongest frequency component of the s
[24:03] of x time the s of y. Let's assume for a
[24:07] moment that the weight assigned to our
[24:09] cosine x * cosine y neuron is 1 and the
[24:12] weight assigned to our sin x * sin y
[24:15] neuron is negative 1. Visually, this
[24:18] negative weight flips our second surface
[24:20] vertically.
[24:22] Now, when we add these weighted surfaces
[24:24] together, the signs and cosiness
[24:26] remarkably interfere in just the right
[24:29] way to create the diagonal symmetry that
[24:31] we see in our neuron in the following
[24:33] layer that allowed our neuron to fire on
[24:35] combinations of inputs that add to 65.
[24:40] As you may remember from trigonometry
[24:41] class, the cosine of x time the cosine
[24:44] of y minus the s of x * the s of y is
[24:47] actually a trigonometric identity.
[24:50] specifically a sum of angles identity
[24:53] that exactly equals the cosine of x + y.
[24:57] This identity allows us to convert the
[24:59] sum of products of s and cosiness into a
[25:02] sum of x and y, which is exactly what
[25:05] our network needs to compute. And
[25:08] remarkably, the network appears to have
[25:10] learned to effectively use this
[25:11] trigonometric identity to solve the
[25:13] modular addition problem.
[25:16] And remember that our training data is
[25:18] just these sparse patterns that have
[25:20] nothing to do with signs, cosiness, or
[25:22] trigonometric identities.
[25:26] The final unmbed portion of our model
[25:28] takes one more weighted sum. This time
[25:30] of the outputs of the final layer
[25:32] neurons in our multi-layer perceptron.
[25:35] Visualizing the outputs of a few more of
[25:37] these neurons, we see the same types of
[25:39] diagonal symmetries with various shifts
[25:42] and scales. Our unmbedding layer takes
[25:45] different combinations of these outputs
[25:47] for each possible token that the network
[25:49] could return. Here's the resulting
[25:52] surface for the seven output.
[25:55] As we saw with our multi-layer
[25:56] perceptron neuron that detected all
[25:58] combinations of numbers that added to
[26:00] 65,
[26:02] this surface reaches a maximum for all
[26:04] the combinations of X and Y that add to
[26:06] 7. Here's 7 plus 0. Here's 0 plus 7. And
[26:11] here's 3 + 4.
[26:14] So remarkably to solve this modular
[26:16] arithmetic problem our network learns to
[26:19] numerically estimate the signs and
[26:21] cosiness of our inputs computes the
[26:24] products of these functions and then
[26:26] uses a clever trig identity to create
[26:28] the diagonal symmetry needed to solve
[26:30] the modular addition problem and then
[26:33] brings multiple versions of these
[26:34] resulting patterns together to compute a
[26:36] final answer.
[26:39] Now, can this detailed understanding of
[26:41] how the model solves modular addition
[26:43] help us understand why it gro?
[26:46] Let's watch the training process again,
[26:48] but this time while visualizing the
[26:50] evolution of the various structures
[26:52] learned by our model. After a few
[26:55] hundred steps, our model perfectly fits
[26:57] the training data. But we don't yet see
[27:00] any hints of signs or cosiness.
[27:02] As our model continues to learn, its
[27:04] performance stays flat, giving the
[27:07] appearance that nothing is happening.
[27:10] However, as we can now clearly see under
[27:13] the hood, the model is starting to piece
[27:14] together the relevant structures needed
[27:17] to solve the modular arithmetic problem.
[27:20] This is such a wild phenomenon. It's
[27:23] very common to visualize training and
[27:25] test performance as a model learns. And
[27:28] when both metrics are flat for this
[27:30] long, the typical assumption is that the
[27:32] model is done learning and has settled
[27:35] into a stable solution.
[27:38] Neil Nandanda and his co-authors propose
[27:39] a clever new metric in their paper
[27:41] called excluded loss. Note that thus far
[27:44] we've been plotting the model's accuracy
[27:46] as it learns. And here we'll switch to
[27:48] plotting the model's cross entropy loss.
[27:51] So lower values are better. See my
[27:54] gradient descent video or chapter 2 of
[27:56] my new AI book for more on cross entropy
[27:58] loss. Now that we know that our model is
[28:01] operating in the frequency domain at a
[28:03] few key frequencies, what happens when
[28:05] we remove the information at these
[28:07] frequencies from the model's final
[28:09] output before measuring performance?
[28:13] Removing the 8 pi over 113 frequency
[28:15] that we found and plotting this excluded
[28:18] loss as the model learns. We see our new
[28:21] metric dip down quickly with training
[28:23] loss, but then slowly climb as our model
[28:26] builds the sign and cosine
[28:27] representations.
[28:29] This excluded loss increases because
[28:32] we've taken away the model's ability to
[28:34] use this key frequency. And importantly,
[28:37] during this long period of flat training
[28:39] and testing performance, our excluded
[28:42] loss slowly climbs, showing that our
[28:44] model is making more and more use of
[28:46] patterns at this frequency.
[28:49] Interestingly, Nanda and his
[28:51] collaborators show that groing occurs
[28:52] not necessarily when the sign and cosine
[28:55] structures are completed, but just after
[28:58] during a phase they call the cleanup
[29:00] phase, where the model actually removes
[29:02] the memorized examples that it relied on
[29:04] early in training.
[29:07] These dynamics are fascinating and
[29:09] explain very nicely why this model gross
[29:12] on this problem.
[29:14] It's so satisfying to me that we can
[29:16] take apart this model, understand the
[29:18] actual mechanisms that it learns, and
[29:21] then use these mechanisms to design a
[29:23] new metric that clearly shows the
[29:25] model's slow progression from
[29:26] memorization to learning and that nicely
[29:29] explains the surprising groing behavior.
[29:33] This level of clarity is a beautiful and
[29:35] rare exception in modern AI, a
[29:38] transparent box in a world of black
[29:41] boxes.
[29:42] The approach Nandanda and his
[29:44] collaborators use to perform this
[29:45] analysis is generally known as
[29:47] mechanistic interpretability.
[29:49] Since Nand's paper came out in early
[29:51] 2023, we've seen some really interesting
[29:54] progress in this field, but are still
[29:56] very far away from anywhere near this
[29:59] level of understanding of full large
[30:00] language models. There's some recent
[30:03] work from a research team at Anthropic
[30:05] that gives a nice feel for the current
[30:07] edge of our understanding using this
[30:09] type of bottomup mechanistic
[30:11] interpretability approach. The team
[30:13] studies how a full-sized model Claude
[30:15] 3.5 Haiku figures out when to create
[30:18] line breaks when writing.
[30:21] The team finds that the Haiku model
[30:23] represents the number of characters that
[30:25] it's written on a given line on a
[30:26] manifold in sixdimensional space. This
[30:30] structure is somewhat analogous to the
[30:32] loops that we saw in the multi-layer
[30:33] perceptron of our model. To figure out
[30:36] when to insert a line break, Haiku needs
[30:39] to know both how many characters it's
[30:41] written on the current line and how many
[30:43] characters long the lines of the text
[30:45] it's currently writing it need to be.
[30:47] Using linear probes similar to the ones
[30:50] we used here to find the signs and
[30:51] cosiness early in our model. The
[30:54] anthropic team mapped character count
[30:56] and line length to this sixdimensional
[30:58] manifold and found that haik coup
[31:01] represents these concepts in this space
[31:03] in a very similar way.
[31:06] This 70 character count probe lines up
[31:08] right next to this line length of 70
[31:10] probe and so on.
[31:12] Now, this gets really wild when these
[31:14] representations are passed into Haiku's
[31:17] attention blocks.
[31:19] We see what the team calls a QK twist,
[31:23] where these helix-like geometries are
[31:25] rotated relative to each other in this
[31:27] sixdimensional space.
[31:29] After rotation, the probe for a
[31:31] character count of 70 is now closest to
[31:33] a line width of 75.
[31:36] And we see a similar offset of four to
[31:38] five characters across the length of our
[31:40] curve.
[31:42] The proximity of these points in the
[31:44] model's attention heads leads to a high
[31:46] dot product when the model is about five
[31:49] characters away from the end of a line.
[31:52] The team goes on to show that there are
[31:53] multiple attention heads that specialize
[31:55] in detecting various distances from the
[31:58] end of the current line of text. And
[32:01] this mechanism allows Haiku to precisely
[32:03] estimate how much more room it has
[32:05] before the end of the line.
[32:07] Now, compared to Claude Haiku's full
[32:09] range of capabilities, deciding when to
[32:12] create a new line is very simple.
[32:14] However, it is exciting to see that the
[32:16] anthropic team found such a clean
[32:18] mechanism that controls this behavior in
[32:20] a full-size model.
[32:24] The story of groing is such a nice arc
[32:26] of scientific discovery and progress.
[32:30] We accidentally discovered a new
[32:32] phenomenon and the search for an
[32:34] explanation genuinely helped push
[32:36] forward our understanding of model
[32:38] training dynamics and the inner workings
[32:40] of transformers.
[32:43] The names we give our discoveries matter
[32:45] and I like the name groing. It feels
[32:48] alien and originates from the complex
[32:51] Martian language in Highland's novel.
[32:54] The AI researcher Andre Karpathy
[32:56] recently commented that training large
[32:58] language models is less like building
[33:00] animal intelligence and more like
[33:03] summoning ghosts. You can think of a
[33:06] ghost as a fundamentally different kind
[33:08] of point in the space of possible
[33:10] intelligences.
[33:11] The literal meaning of gro to understand
[33:14] something profoundly and deeply is a
[33:16] nice fit for what the model appears to
[33:18] be doing.
[33:20] But what I really appreciate here is the
[33:22] connotation of this thing being alien. I
[33:26] think it's a really nice counterpoint to
[33:28] overly personifying models.
[33:31] We communicate with these models in
[33:32] human language. But as we've seen, this
[33:35] is a thin veneer. If we go one layer
[33:38] deeper into what these models actually
[33:39] process in return, we find these
[33:42] absurdly complex patterns.
[33:45] As we build more intelligent models and
[33:47] learn more about how they work, it will
[33:49] be fascinating to see if these
[33:51] artificial intelligences feel more
[33:53] alien, ghost, or human.
[34:04] I am tired. So, this has been my first
[34:07] full year working fully on Welch Labs.
[34:10] Um, we made some progress. So, we did
[34:12] nine videos this year and we did one
[34:14] book. Um, and man, getting that done
[34:16] filled like every available second of
[34:19] time that I had. Um, for now on the
[34:23] business, I'm trying to keep things
[34:25] simple. Um, so really just focusing on
[34:28] making sure that the business and the
[34:29] channel work well enough to support my
[34:31] family and I. Um, I left my full-time
[34:34] job last year. Um, my goal is to earn as
[34:37] much from Welch Labs as I did from my
[34:39] engineering job. I was hoping to replace
[34:41] my whole income this year. It's probably
[34:43] going to be like 75%. Um, the book
[34:45] helped a lot, but there's always
[34:47] challenges. The business side is hard.
[34:49] Um, I've tried to do this full-time
[34:51] before, once in 2018. Um, I just didn't
[34:53] have enough runway and enough focus on
[34:55] the business. So, I think we're doing it
[34:57] right this time, but gosh, it takes time
[34:58] and man, it takes a lot of work. So, I
[35:00] hope you enjoyed what we've done this
[35:01] year. Um, a lot more of it next year.
[35:04] Uh, kind of working on the focus and
[35:06] direction for next year right now. Um,
[35:08] but I'm really happy with the book. I
[35:10] hope you're able to get a copy. I know
[35:11] we're not shipping internationally yet.
[35:13] That will be a focus early next year. I
[35:15] I promise. Um but yeah, what a year,
[35:18] man. Thank you so much for your support.
[35:19] If you are able to support on Patreon,
[35:21] that helps a ton. Or just liking and
[35:22] sharing the videos. Um thanks for a
[35:24] great year. I'll see you next year.