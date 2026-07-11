---
source_url: https://www.youtube.com/watch?v=NrO20Jb-hy0
ingested: 2026-07-08
video_id: NrO20Jb-hy0
title: The Misconception that Almost Stopped AI [How Models Learn Part 1]
series: How Models Learn
---

[00:00] This is the lost landscape of Meta's
[00:02] Llama 3.2 large language model.
[00:05] Virtually all modern AI models learn by
[00:07] gradient descent. Visually, this looks
[00:09] like starting at a random location on
[00:11] our landscape and working our way
[00:13] downhill towards lower loss, higher
[00:15] performance solutions. But how does our
[00:18] model avoid getting stuck in local
[00:20] valleys like this one? This question
[00:22] stopped many early AI pioneers in their
[00:25] tracks. Jeff Hinton, who would go on to
[00:27] win the Nobel Prize in 2024 for his work
[00:29] in AI, initially entirely dismissed
[00:32] training neural networks like llama with
[00:34] gradient descent for exactly this
[00:37] reason. Of course, as we now know,
[00:39] gradient descent actually works
[00:41] unbelievably well. What understanding
[00:43] was Hinton missing? And what's wrong
[00:45] with our picture? In this series, we'll
[00:48] take a fresh look at how AI models
[00:50] learn. Starting with a visual first
[00:53] approach, we'll dig into how exactly our
[00:55] llama model learns from real training
[00:57] examples, what our lost landscape can
[01:00] and can't show us, and ultimately see
[01:02] why gradient descent for large models
[01:04] looks more like falling into a wormhole
[01:06] than it does simply heading downhill. In
[01:09] part two, we'll switch to a more
[01:10] math-driven approach, which will help us
[01:12] grapple with the incredibly
[01:13] highdimensional spaces these models
[01:15] operate in.
[01:18] Researching this series, I found some
[01:19] really interesting visualization
[01:21] techniques that required some deep focus
[01:23] time to get my head around, which this
[01:25] video sponsor, Incogn has really helped
[01:27] me with. I've been an Incogn customer
[01:29] for 6 months now and continue to be
[01:31] blown away by how many fewer spam texts,
[01:34] calls, and emails I get, giving me more
[01:36] quality focus time. The way Incogn does
[01:39] this is really impressive. After signing
[01:41] up for an account, you give Incogn
[01:43] permission to work on your behalf to
[01:44] contact data brokers to remove your
[01:46] data, which brokers are generally
[01:48] legally obligated to do upon request.
[01:51] From here, you get this great dashboard
[01:52] that tracks all the removal requests in
[01:55] progress. It's really impressive and
[01:57] always working in the background. When I
[01:59] checked in at the end of last year, my
[02:01] data had been removed from 115 different
[02:03] data brokers, and the count is now up to
[02:05] 220.
[02:07] I really value the control over my
[02:09] personal data that Incogn gives me. In
[02:11] the United States, we have these people
[02:13] search sites where for a small fee,
[02:15] anyone can look up information about you
[02:17] like your address, email, phone number,
[02:19] education, employment history, court
[02:21] records, and social media accounts. This
[02:23] gives you an idea of all the information
[02:25] that data brokers are able to gather and
[02:27] sell. I signed up for an account on one
[02:30] of these people search sites after being
[02:31] an incogn for a couple of months. And
[02:34] impressively, I wasn't able to find any
[02:36] records of myself. You can get a great
[02:38] deal on Incogn 60% off an annual plan by
[02:41] using the code Welch Labs or following
[02:43] the link in the description below. It's
[02:46] been a while since I've made a
[02:47] multi-part series like this. Huge thank
[02:50] you to Incogn for helping make this
[02:51] series possible and helping me get more
[02:54] quality focus time as I work on it. Now,
[02:56] back to how AI models learn explained
[02:59] visually. Let's begin by experimenting
[03:01] with a real large language model. Meta's
[03:04] Llama 3.2 1.2 billion parameter model.
[03:08] Given a sequence of text models like
[03:10] llama and chatgpt are trained to predict
[03:12] the word or word fragment known as a
[03:14] token that comes next. When training on
[03:16] the text the capital of Francis Paris,
[03:18] for example, this text is tokenized into
[03:21] six tokens, each represented by a single
[03:24] number and passed into our model. For
[03:27] each input token, our llama model
[03:28] returns a prediction of what token will
[03:30] come next in the form of a vector of
[03:33] probabilities. So when we pass in the
[03:35] six tokens for the capital of France's
[03:37] Paris, our model returns six vectors
[03:40] each of length
[03:43] 128,256 with one predicted probability
[03:45] value for each of the
[03:47] 128,256 tokens in Llama's vocabulary.
[03:50] Our fifth vector has a maximum
[03:52] probability of
[03:54] 0.39 at index
[03:56] 12,366 which corresponds to the token
[03:59] for Paris. So our model is assigning a
[04:01] 39% probability to Paris as the token
[04:04] that follows the capital of France is
[04:08] the next most likely token according to
[04:09] the model is the word a with a
[04:11] probability of
[04:13] 8.4%. This could lead to sentences like
[04:15] the capital of France is a beautiful
[04:17] place to visit. During training, the
[04:20] model's predicted probabilities at each
[04:21] position are compared to the correct
[04:23] next token from the training text. So at
[04:26] the first position, our model is trained
[04:28] to predict the token for capital. And at
[04:30] our fifth position, the model is trained
[04:32] to predict the token for
[04:33] Paris. From here, we need some way to
[04:36] measure how well our model is working.
[04:38] The metric we choose here will guide the
[04:40] learning process. One option is to
[04:42] directly measure the model's error by
[04:44] taking one minus the model's predicted
[04:46] probability of the correct next token.
[04:48] In the fifth position, for example, if
[04:50] the model predicted the token of Paris
[04:52] completely confidently with a
[04:54] probability of 1.0, our error would be 1
[04:57] - 1 equals 0. If the model's predicted
[05:00] probability dropped to 0.9, our error
[05:02] would increase to 1 minus 0.9als 0.1 and
[05:06] so on. This metric is known as the L1
[05:08] loss. And as we'll see when we look at
[05:11] the mathematics of back propagation, it
[05:13] has a very important role to play in
[05:15] learning. However, it turns out that
[05:17] models are able to learn more
[05:18] effectively if we instead use a function
[05:20] called cross entropy loss. To compute
[05:23] the cross entropy loss, instead of
[05:25] taking one minus the model's predicted
[05:27] probability of the correct next token,
[05:29] we instead take the negative logarithm
[05:31] of this probability. This ends up
[05:33] looking similar to our L1 loss. If the
[05:36] model's probability of the correct next
[05:38] token is one, our cross entropy loss
[05:40] equals minus the log of one, which
[05:42] equals 0, matching our L1 loss. If the
[05:46] model's probability of the correct next
[05:47] token drops to 0.9, our L1 loss equals
[05:51] 0.1 and our cross entropy loss equals
[05:54] 0.105. And if the model's probability
[05:56] drops to 0.8, our L1 loss equals 0.2 and
[06:00] our cross entropy loss equals 0.223.
[06:03] The key difference here is that as our
[06:05] model becomes less and less confident in
[06:07] the right answer, our cross entropy loss
[06:09] shoots up, penalizing our model more.
[06:12] Large language model training is
[06:14] entirely driven by reducing this cross
[06:16] entropy loss. Now, how do we actually
[06:19] use this loss to make our model better?
[06:22] And how can we visualize the process?
[06:24] Our model's current parameters give a
[06:26] probability of 0.39 for a next token of
[06:29] Paris, leading to a cross entropy loss
[06:31] of
[06:32] 0.94. Note that we would typically
[06:34] compute our loss at each token position
[06:36] and average the results. But for now,
[06:39] let's focus exclusively on training our
[06:41] model to be more confident in a next
[06:42] token of Paris at the fifth position. So
[06:45] our total cross entropy loss is 0.94.
[06:49] Now, how do we adjust our model
[06:50] parameters to increase the model's
[06:52] confidence in Paris and bring down this
[06:55] loss? Our llama model follows a fairly
[06:58] standard transformer architecture. It's
[07:00] composed of 16 layers, each containing
[07:02] an attention and multi-layer perceptron
[07:04] compute block. In this video, we won't
[07:07] be too concerned with how these layers
[07:08] work. A helpful and increasingly true
[07:11] mental model here is to think of our
[07:14] whole transformer as a single function f
[07:16] that takes in our input text x and uses
[07:19] its parameters theta to compute the next
[07:21] token probabilities. We'll explore how
[07:24] our model's output changes as we change
[07:26] our model's parameters. And as we'll
[07:28] see, doing this in a structured way is
[07:30] precisely how these models learn. Let's
[07:33] start by visualizing the impact of just
[07:35] one of our 1.2 2 billion model
[07:37] parameters on our model's output. The
[07:40] multi-layer perceptron compute block in
[07:42] the model's final layer has around 50
[07:44] million total
[07:45] parameters. We'll pick out one of these
[07:47] parameters and see how it impacts our
[07:49] model's final output. Our parameter's
[07:52] current value
[07:54] is0.007. Let's decrease this parameter's
[07:57] value by
[07:58] 0.01. Rerun our input text through our
[08:00] model and see how our predictions and
[08:02] loss change. Our model's predicted
[08:05] probability of a final token of Paris
[08:07] moves down a little from
[08:09] 0.3916 to
[08:12] 0.3901. Testing a change in the other
[08:14] direction, increasing our parameters
[08:16] value by 0.01 moves up our model's
[08:19] confidence to
[08:21] 0.3930. So for this single parameter and
[08:23] for this example text, we know that we
[08:25] can make our model more confident in the
[08:27] right answer by increasing this
[08:29] parameter's value. But by how much
[08:31] should we increase it? Can we make the
[08:34] model more confident in the right answer
[08:35] by further increasing this parameter?
[08:38] Extending and visualizing this idea, we
[08:41] can test more values and plot our
[08:42] model's output probability for a range
[08:44] of values of our parameter and see a
[08:46] nice parabola-ish looking curve as a
[08:48] function of the value of this single
[08:50] parameter. As we've seen, our cross
[08:53] entropy loss is the negative logarithm
[08:55] of these output probability values.
[08:57] Computing and visualizing these loss
[08:59] values, we get a flipped version of our
[09:01] parabola. These results suggest that we
[09:03] can maximize our model's predicted
[09:05] probability of the correct answer and
[09:07] minimize our loss by setting our
[09:09] parameter to around
[09:11] 1.61. We could then walk through each
[09:13] parameter one at a time, applying the
[09:15] same analysis and setting each parameter
[09:17] to minimize our output loss. Let's see
[09:20] visually why this idea does not work.
[09:23] After setting our first parameter theta
[09:25] 1 to a value of 1.61 61 to maximize our
[09:28] model's confidence in the Paris token
[09:29] and minimize our loss. If we move to a
[09:32] second parameter, we can again test a
[09:34] range of values and set the second
[09:36] parameter theta 2 to the value that
[09:38] minimizes our loss. In this case,
[09:41] 1.76. Now, here's the problem. If we
[09:45] return to our first parameter, which we
[09:47] already tested and set to a value of
[09:49] 1.61, and run the same analysis, the
[09:52] shape of our curve changes. It now looks
[09:55] like a value of 1.11 will actually
[09:58] minimize our loss. The impacts of each
[10:00] parameter on our model's output are not
[10:03] independent. Changing the value of our
[10:05] second parameter changes the shape of
[10:07] our first loss curve and vice versa. So,
[10:10] we aren't going to be able to learn
[10:11] effectively by tuning one parameter at a
[10:13] time like this. We can see this visually
[10:16] by testing how our loss changes as we
[10:18] vary our parameter values together.
[10:20] testing a grid of values and plotting
[10:22] our loss for each combination of
[10:23] parameters as the height of a surface.
[10:26] It's now straightforward to see what
[10:27] went wrong earlier. If we only consider
[10:30] our first parameter, we're effectively
[10:32] looking at a slice like this. Moving to
[10:35] the bottom of this curve and then tuning
[10:37] our second parameter, we're now looking
[10:39] at a slice like this. When we move to
[10:41] the bottom of this second curve, we
[10:43] reach a new location on our lost
[10:45] landscape where we're no longer at the
[10:47] bottom of a valley in the direction of
[10:49] our first parameter. In this two
[10:51] parameter visualization, it is easy to
[10:53] see which combination of parameter
[10:55] values minimize our overall loss. We
[10:58] just need to set our two parameters to
[10:59] the values at the bottom of the bowl. We
[11:02] now have an optimal solution in both
[11:04] directions with respect to these two
[11:06] parameters.
[11:08] Now, of course, it's not just these two
[11:10] parameters that are coupled.
[11:11] Effectively, all 1.2 billion parameters
[11:14] of our model R. Meaning that our loss
[11:16] landscape is actually 1.2 billion
[11:19] dimensional. And that it's
[11:20] computationally impossible to explore
[11:22] all combinations of parameters as we did
[11:24] with our two test parameters. If we test
[11:27] 20 values for each parameter, testing
[11:29] two parameters, as we just did, requires
[11:32] 400 evaluations.
[11:34] Testing three parameters together is
[11:35] equivalent to testing all 8,000 values
[11:38] in a 20x 20x 20 cube. And testing all
[11:41] 1.2 billion model parameters like this
[11:44] would require an astronomical 20 to the
[11:46] power of 1.2 billion
[11:49] calculations. We need a far more
[11:51] scalable approach. Returning to our
[11:54] two-dimensional loss landscape, is there
[11:56] a way to find the bottom of the valley
[11:58] without computing the height of every
[12:00] point in the landscape?
[12:02] If you were lost in a forest on a
[12:04] mountain trying to find your way to the
[12:06] valley below without a map, a pretty
[12:08] reasonable thing to do is to just keep
[12:10] heading downhill. Even if you can't see
[12:12] the valley below, we can effectively do
[12:15] this mathematically. For each parameter,
[12:18] instead of computing the loss across a
[12:20] range of values, we can compute the
[12:22] slope of the loss curve, telling us
[12:24] which way is downhill in each direction
[12:26] and how steep the descent is.
[12:29] As we'll see in part two, it turns out
[12:31] that we can compute these slopes very
[12:33] efficiently. We won't even have to
[12:35] compute the actual values of our loss
[12:37] curve at all. From here, we can put our
[12:40] slopes together into a single vector
[12:42] called the gradient, which acts like a
[12:44] little compass that points us downhill.
[12:47] Note that technically the gradient
[12:48] points uphill, and we move in the
[12:50] opposite direction to go downhill. We'll
[12:52] see why this is the case in part two.
[12:54] The idea now is to take small iterative
[12:57] steps downhill where after each step we
[12:59] recomputee the gradient to guide our
[13:01] next step. This is known as gradient
[13:03] descent and is how virtually all modern
[13:06] AI models learn by taking small steps
[13:09] downhill. In practice, we're often able
[13:11] to find very good solutions even in very
[13:14] highdimensional loss landscapes that we
[13:16] could never fully explore
[13:18] computationally. It's of course a little
[13:20] difficult to visualize the 1.2 two
[13:22] billiondimensional loss landscape of our
[13:24] language model and what going downhill
[13:26] really looks like in this
[13:27] highdimensional space. One approach we
[13:30] can try here is to choose a random
[13:32] direction in our highdimensional space
[13:34] and measure our loss as we take small
[13:36] steps in that direction. Note that here
[13:39] choosing a random direction means
[13:41] generating 1.2 billion random numbers,
[13:44] one for each model parameter. And taking
[13:46] a small step in this direction means
[13:48] multiplying these 1.2 to billion random
[13:50] numbers by a small scaling factor and
[13:53] adding these scaled random numbers to
[13:55] our weights and then recomputing our
[13:57] loss. As we move further in our random
[14:00] direction by increasing our scaling
[14:01] factor, we can compute our loss at each
[14:04] step and see how this combination of
[14:06] model weights impacts our loss. Note
[14:09] that this is almost exactly what we do
[14:11] when training our model with gradient
[14:12] descent, except here we're choosing our
[14:14] direction randomly instead of using the
[14:17] downhill direction from our gradient
[14:18] computation. Choosing a random direction
[14:21] like this will hopefully give us a
[14:22] broader feel for what our lost landscape
[14:24] looks like. Here's what the loss
[14:26] landscape for our llama model looks like
[14:28] as we move in a randomly chosen
[14:30] direction.
[14:31] Exploring our highdimensional lost
[14:33] landscape in this way reveals
[14:34] interesting structures with hills,
[14:36] valleys, cliffs, and
[14:38] plateaus. Here's the lost landscape in a
[14:41] second randomly chosen
[14:43] direction. These two plots are for a
[14:45] randomly initialized model before
[14:47] training. Here's two more plots for our
[14:49] model after
[14:51] training. With our trained model, we can
[14:53] clearly see the lower loss value the
[14:55] model has learned through training. Note
[14:57] that we're using positive and negative
[14:59] values for our step size alpha. So our
[15:02] unmodified model weights show up here at
[15:03] alpha equals zero on our plot. Finally,
[15:06] it can be interesting to confine our
[15:08] random directions to certain layers.
[15:10] Here's what our loss landscape looks
[15:12] like as we explore two random directions
[15:14] in the first eight layers of our train
[15:16] models total 16 layers.
[15:19] We can take this approach one step
[15:21] further by putting these two random
[15:23] directions together onto a 2D grid and
[15:25] computing our loss for combinations of
[15:27] steps in each of our two random
[15:30] directions. We can now visualize our
[15:32] loss landscape as we explore these two
[15:34] random directions
[15:36] together. Now imagine navigating this
[15:39] loss landscape from the perspective of
[15:41] our gradient descent
[15:42] algorithm. Before training, our model's
[15:45] parameters are randomly initialized,
[15:47] meaning we're effectively dropped into a
[15:49] random location in this landscape. From
[15:52] here, our job is to navigate our way to
[15:54] the bottom of the valley, ideally the
[15:56] global minimum here. But our only guide
[15:58] is the gradient, which only tells us
[16:01] which way is downhill in the tiny local
[16:03] part of the landscape that we're
[16:04] currently on. A baffling fact about
[16:07] modern AI and one of the reasons many
[16:10] early AI researchers dismiss this
[16:12] approach is that there's no guarantee
[16:14] that gradient descent will find the best
[16:16] or even a good solution in these
[16:18] highdimensional loss landscapes. This
[16:20] view of our landscape has many local
[16:22] minima where gradient descent could
[16:24] potentially get
[16:26] stuck. But remember, even with our
[16:28] clever random direction probing trick,
[16:31] we're still looking at a two-dimensional
[16:32] shadow of a 1.2 two billiondimensional
[16:36] landscape. If we actually run gradient
[16:38] descent and train our model on our
[16:40] example text, we might imagine that
[16:42] learning looks like our parameters as a
[16:44] point working its way downhill in the
[16:46] landscape. And maybe the fact that the
[16:48] real optimization process is higher
[16:50] dimensional means that gradient descent
[16:52] can avoid getting stuck in local minima
[16:54] like this one. This was roughly the
[16:56] mental image I had in my head when I
[16:58] started working on this video. But after
[17:00] some experimentation, I realized this is
[17:02] really not what happens as our model
[17:05] learns. The reason is that as soon as we
[17:08] take even a small step in the full
[17:10] highdimensional space of our model's
[17:12] parameters, our two-dimensional
[17:13] visualization of the landscape changes
[17:16] dramatically. Visually, as we run
[17:18] gradient descent, it almost looks like a
[17:20] wormhole opens up in our landscape,
[17:22] quickly landing our parameters in a very
[17:24] low loss valley that basically comes out
[17:27] of nowhere. And this all happens before
[17:29] our little dot even has a chance to
[17:31] really go anywhere on our landscape. It
[17:33] does move a little in the direction of
[17:35] the global minimum, but not enough to
[17:37] notice on our
[17:38] visualization. What exactly is going on
[17:40] here? Now, right now, we're just
[17:42] training on the single phrase. The
[17:44] capital of France is Paris. These new
[17:47] learned parameters quickly boost our
[17:49] model's probability for a next token of
[17:51] Paris close to a max value of 1.0 and
[17:54] bring down our loss close to zero. Of
[17:57] course, just training a large language
[17:58] model on a single short phrase is not
[18:00] how these models are trained in
[18:02] practice. Let's look at the same
[18:04] visualization, but where our model is
[18:06] instead trained on examples from the
[18:07] Wiki text data set. We'll use a batch
[18:10] size of four, meaning we're learning
[18:12] from four different examples at once.
[18:14] Our loss landscape becomes smoother.
[18:16] Now, this makes sense because our loss
[18:18] is now averaged across all of the tokens
[18:21] in our batch.
[18:23] When we take a gradient descent step, we
[18:25] see our loss landscape move down around
[18:27] our starting point. Just as we saw in
[18:29] our Paris example, this shows our model
[18:32] reducing the loss and performing better
[18:34] on the examples in this batch. When we
[18:36] switch to the next batch of data, the
[18:38] shape of our loss landscape changes and
[18:41] the gains we made from the last batch
[18:43] partially disappear. Step by step like
[18:46] this, our gradient descent algorithm
[18:48] will work its way towards a good
[18:49] solution and our visualized landscape
[18:52] changes as the model learns. In both
[18:54] cases, our 2D visualized loss landscape
[18:57] changes as we learn because we're
[18:59] effectively looking out in our randomly
[19:01] chosen directions from a new vantage
[19:03] point in highdimensional
[19:05] space. This is analogous to our
[19:07] exploration of our model's loss earlier
[19:09] as we varied a single parameter and then
[19:11] varied two parameters together. Let's
[19:13] imagine for a moment that we're only
[19:15] able to visualize our loss with respect
[19:17] to one of our two parameters. Our loss
[19:20] may look something like this curve with
[19:21] respect to our first
[19:23] parameter. Now, if we run gradient
[19:25] descent, where we're moving in the full
[19:27] 2D space of both parameters, our entire
[19:30] curve with respect to the first
[19:31] parameter changes. We're effectively
[19:33] moving to a different slice of our full
[19:35] 2D loss surface. If there happens to be
[19:38] a nice valley close to us, but the only
[19:41] way to get there is to move in the
[19:42] direction of our second parameter, we
[19:44] won't see it at all in our initial 1D
[19:46] visualization with respect to our first
[19:48] parameter. And when we do find it with
[19:50] gradient descent, it will appear to come
[19:52] out of nowhere in our 1D visualization,
[19:54] much like our wormhole came out of
[19:56] nowhere in our full visualization.
[19:59] The wormhole example is a bit extreme
[20:01] because we're only training on a single
[20:03] short phrase, but it does tell us
[20:05] something interesting about the
[20:06] highdimensional loss landscapes we're
[20:08] trying to visualize and understand. In
[20:11] this example, there are very good
[20:12] solutions very close to us in
[20:14] highdimensional space. We just can't see
[20:17] them until we compute our full
[20:19] highdimensional gradient and move in
[20:20] that direction. When Jeff Hinton did
[20:23] eventually try out gradient descent
[20:25] after getting stuck with another
[20:26] approach called Boltzman machines, he
[20:29] tested it on a model with around 50
[20:30] parameters and was shocked by how well
[20:33] it worked. For gradient descent to
[20:35] become fully stuck in a local minimum,
[20:37] it would have to get stuck in every
[20:39] dimension at once. And the chances of
[20:41] this happening become smaller and
[20:43] smaller as we add more and more
[20:45] parameters. For simple two parameter
[20:47] models, as we see in problems like
[20:49] linear regression, loss landscapes give
[20:51] us a complete picture and can provide
[20:53] helpful intuition for how these models
[20:56] learn. However, as our models become
[20:58] more and more complex with more and more
[21:00] parameters, our lost landscape
[21:02] visualizations become a more and more
[21:04] distant shadow of the model's true
[21:06] learning process. As we'll see next
[21:09] time, although our ability to visualize
[21:11] these landscapes becomes more and more
[21:13] limited as we add more and more
[21:14] dimensions, our mathematics has no
[21:17] problem operating in these incredibly
[21:19] highdimensional
[21:22] landscapes. If you're curious about lost
[21:25] landscapes, check out this video's
[21:27] poster. This is a new, larger format
[21:29] that I haven't been able to do before at
[21:31] this high level of print quality. And I
[21:33] spent way too much compute time
[21:35] exploring the landscapes of different
[21:36] models for the poster. Top and center,
[21:39] you'll find the llama 1 billion
[21:40] parameter landscape that we covered in
[21:42] this video. To the left, I have a
[21:44] simpler model, GPT2, which results in a
[21:47] smoother and simpler landscape. In the
[21:49] upper right, you'll find a distilled
[21:51] version of Deepseek R1, which
[21:53] interestingly has larger smooth areas
[21:55] than Llama. This may be because Deepseek
[21:58] has been instruction tuned. It also
[22:00] generates a much higher confidence out
[22:01] of the box for a next token of Paris
[22:04] around 70%. On the bottom row, you'll
[22:07] find GEMO 1B. This is a smaller open-
[22:09] source version of Google's Gemini model.
[22:11] And on the bottom right, I've included a
[22:13] couple variants of the popular Quinn
[22:15] models. It's again interesting here to
[22:17] compare instruction tuning versus just
[22:19] pre-training. On the bottom of the
[22:21] poster, I've included some key figures
[22:23] from the video that explain how we're
[22:25] computing our loss landscapes. I'm
[22:27] really happy with how this poster came
[22:29] out, and I'm excited that I can offer
[22:31] this larger 17x 22 in size at very high
[22:34] quality. I've learned that with graphics
[22:36] like this, you really want to use photo
[22:38] printers to get all the fine details and
[22:40] colors right. You can pick up a physical
[22:42] or digital copy at welchlabs.com or
[22:45] purchase at a discounted rate when
[22:47] bundled with my Imaginary Numbers book.
[22:49] Big thank you to everyone who's
[22:50] purchased from the store. Your purchases
[22:52] go a long way to helping me make more
[22:55] great