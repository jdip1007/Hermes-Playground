---
source_url: https://www.youtube.com/watch?v=VkHfRKewkWw
ingested: 2026-07-08
video_id: VkHfRKewkWw
title: The F=ma of Artificial Intelligence [Backpropagation, How Models Learn Part 2]
series: How Models Learn
---

[00:00] In the early 1970s, a Harvard graduate
[00:03] student named Paul Worbos discovered a
[00:05] method for training multi-layer neural
[00:06] networks that we now call back
[00:08] propagation. Worbos would later compare
[00:11] the discovery to Newton's laws,
[00:13] positioning back propagation as a
[00:15] fundamental mathematical law of
[00:16] intelligence. When Warbos took his
[00:19] discovery to AI legend Marvin Minsky,
[00:21] Minsky rejected it outright, claiming
[00:24] that back propagation would not be able
[00:25] to learn anything difficult. However,
[00:28] despite being consistently
[00:29] underestimated by Minsky and many
[00:31] others, back propagation just kept
[00:33] working, successfully training models to
[00:36] drive cars in the 1980s, recognize
[00:38] handwritten digits in the 1990s, and
[00:40] classify images with incredible accuracy
[00:42] in the early 2010s. And today, virtually
[00:46] all modern AI models are trained using
[00:48] back propagation. This animation shows
[00:50] the flow of real data through Meta's
[00:52] Llama 3.2 large language model. Note
[00:56] that the entire model is too large to
[00:58] show on screen. Here we're showing the
[01:00] strongest connections. Given some input
[01:03] text, like the capital of France is,
[01:06] Llama predicts the token that will come
[01:07] next, and the back propagation algorithm
[01:10] figures out how to update each of the
[01:11] models 1.2 billion parameters to make
[01:14] Llama more confident in the correct next
[01:16] token. These updates are shown in blue,
[01:19] where thicker lines correspond to larger
[01:22] updates. In this middle layer of the
[01:24] model, we can see back propagation is
[01:26] modifying the weights flowing in and out
[01:28] of this attention pattern. This pattern
[01:31] tells the model to focus on the second
[01:33] and fourth token in the input text. In
[01:36] this case, the words capital and France,
[01:38] which are important for predicting the
[01:40] next token of Paris. Back propagation is
[01:43] remarkably able to figure out which
[01:45] parts of these massive models to update
[01:47] to iteratively improve performance and
[01:49] learn highly complex behaviors.
[01:52] Like Newton's laws, the back propagation
[01:54] algorithm is simple, elegant, and
[01:56] deceptively scalable, leading to
[01:58] incredibly rich structures and
[02:00] behaviors.
[02:01] In this video and the next in this
[02:03] series, we'll see precisely how back
[02:05] propagation works.
[02:09] Now, before we get started, we need to
[02:11] talk about
[02:13] Remember when you used to be able to
[02:14] just ignore calls from unknown numbers?
[02:17] I do. It was awesome. But now that I
[02:19] have kids, I've learned it's much less
[02:21] awesome to ignore calls from your kids
[02:23] school principles and doctors. But you
[02:25] know who never calls me anymore?
[02:27] Telemarketers. Thanks to this video
[02:29] sponsor, Incogn, I get so few marketing
[02:31] calls these days that I've actually
[02:33] started answering unknown numbers
[02:35] because more often than not now, it's
[02:36] someone I actually need to talk to. The
[02:39] way Incogn does this is really
[02:40] impressive. After signing up for an
[02:42] account, you give Incogn permission to
[02:44] work on your behalf to contact data
[02:46] brokers to remove your data. From here,
[02:48] you get this great dashboard that tracks
[02:50] all the removal requests in progress and
[02:52] is always working in the background.
[02:54] Incogn is sponsoring this whole series,
[02:56] which is great. And I actually had to
[02:58] re-record this graphic because in the
[03:00] few weeks since I released part one, my
[03:02] data has been removed from 34 more data
[03:04] brokers. Incogn has just released a new
[03:07] feature that makes their service even
[03:09] more effective called custom data
[03:11] removals. If you Google your name and
[03:13] address, you may be surprised to find
[03:15] exactly where your personal information
[03:17] pops up. With custom removals, you can
[03:20] submit specific URLs directly to the
[03:22] Incogn who will work to remove your
[03:24] information from eligible sites. You can
[03:26] get a great deal on Incogn 60% off an
[03:28] annual plan by using the code Welch Labs
[03:31] or following the link in the description
[03:32] below. It's been a while since I've made
[03:35] a multi-part series like this. Huge
[03:37] thank you to incogn for helping make
[03:39] this series possible and helping me get
[03:41] more quality focus time. Now back to the
[03:44] back propagation algorithm. In part one
[03:47] of this series, we took a visual first
[03:49] approach to training Meta Lama 3.2 1.2
[03:52] billion parameter model. We showed how
[03:54] loss landscapes give us a sense for the
[03:56] highdimensional spaces these models
[03:58] operate in, but also how these types of
[04:00] visualizations can fall short. In this
[04:03] video, we'll take a math first approach
[04:05] that will lead us to the back
[04:06] propagation algorithm that Warbos
[04:08] discovered over 50 years ago. To build
[04:11] up the equations we need, we'll simplify
[04:13] our learning problem, work out the
[04:15] equations, and then scale back up.
[04:18] Instead of training a large language
[04:19] model like llama to predict what comes
[04:21] next in phrases like the capital of
[04:23] France is, let's train a smaller model
[04:25] to predict what city you're in based on
[04:27] your GPS coordinates. Our training data
[04:30] is now GPS coordinates taken from a few
[04:32] different cities. Here's five
[04:34] coordinates from Paris and five
[04:35] coordinates from Madrid and Berlin. Our
[04:38] full Llama language model returns
[04:40] vectors of probabilities of length
[04:42] 128,256
[04:44] with one entry for every token in
[04:46] Llama's vocabulary. Our tiny GPS model
[04:49] also returns vectors of probabilities
[04:51] but on a much smaller vocabulary of just
[04:53] our three cities, Paris, Madrid, and
[04:56] Berlin.
[04:58] Instead of taking in text inputs, our
[05:00] tiny model will take in GPS coordinates.
[05:03] And we'll start by just taking in one
[05:04] coordinate, the longitude. So our model
[05:07] takes in a single numerical input, the
[05:09] longitude, which we'll call X. And it
[05:12] returns three numbers, one probability
[05:15] for each city. We'll call these
[05:17] probabilities Yhat 1, Yhat 2, and Yhat
[05:19] 3. Architecturally, our model has just
[05:22] three total neurons, one for each city.
[05:25] Each neuron's job is really simple. It
[05:28] multiplies its input by a learnable
[05:30] parameter called a weight, adds another
[05:32] learnable parameter called a bias, and
[05:34] outputs the result.
[05:36] Mathematically, we can write the output
[05:38] of our first neuron, which we'll call
[05:40] H1, as our first learnable parameter m1*
[05:44] our input x plus our bias value b1. This
[05:47] model is completely equivalent to a
[05:49] simple linear y= mx plusb equation from
[05:52] high school algebra. Each of the neurons
[05:54] that make up artificial neural networks
[05:56] like llama is effectively a simple
[05:57] linear model like this, although with
[06:00] more inputs x and slopes m. And it's the
[06:03] job of our learning algorithm to make
[06:04] the appropriate adjustments to all of
[06:06] our m and b values to solve the larger
[06:08] task at hand. Note that we're calling
[06:11] our output h instead of y here because
[06:13] we have to take one more step before
[06:15] reaching our final outputs yhat.
[06:18] Now depending on their location in the
[06:20] overall model, the outputs of these
[06:22] little linear models are sometimes
[06:24] passed into a few other types of
[06:25] functions. We know that we want the
[06:27] final outputs of our model Y hat to be
[06:30] probabilities between 0 and one. But
[06:33] right now, each of our neurons are
[06:34] capable of returning a full range of
[06:36] positive and negative values. to squish
[06:39] the outputs of our neurons and ensure
[06:41] that our probabilities all add up to
[06:42] one. The outputs h of our final layer
[06:45] are typically passed into a function
[06:46] called softmax.
[06:49] To compute the probability of Madrid
[06:51] yhat 1 using softmax, we raise e to the
[06:54] power of the output of our first neuron
[06:56] h1 and divide by the sum of each of the
[06:58] power of each of our neuron outputs h1,
[07:01] h2, and h3.
[07:03] The exponentials in the softmax equation
[07:05] amplify the difference between our
[07:07] neuron outputs, assigning more but not
[07:10] all probability to the neuron with the
[07:11] highest output value. This is why it's
[07:14] called a soft max. If our Madrid, Paris,
[07:17] and Berlin neurons output values of 1,
[07:19] two, and one, our softmax operation will
[07:22] assign a 58% probability to yhat 2 for
[07:25] Paris. If our model is more confident in
[07:28] Paris and returns values of 1, 10, and
[07:30] 1, softax behaves more like our
[07:33] traditional maximum function, assigning
[07:35] Paris a probability of 99.98%.
[07:39] Softmax is the most complicated piece of
[07:41] math we'll encounter in this video. And
[07:43] happily, we'll see that when we apply
[07:44] some calculus and differentiate softmax,
[07:47] it actually gets much simpler. So, we
[07:49] now have all the equations we need to
[07:51] make predictions using our tiny GPS
[07:54] model. Before training, our model
[07:56] weights are randomly initialized.
[07:59] Let's pick some simple starting values.
[08:01] We'll set our slope parameters to m1= 1,
[08:04] m2= 0, and m3= -1, and set all our bias
[08:08] values to zero. If we now pass in the
[08:11] longitude for one of our Paris
[08:13] coordinates, for example, the center of
[08:15] the city at 2.3514°,
[08:18] our positive value for M1 gives us a
[08:20] large H1 value of 2.35, leading our
[08:24] model to incorrectly predict that we're
[08:25] in Madrid with a probability of 0.91.
[08:29] Now, as we saw in part one, to train our
[08:32] model to make better predictions, we
[08:34] first need a way to measure our model's
[08:35] performance. The metric of choice for
[08:38] llama and many modern models is the
[08:40] cross entropy loss. To compute the cross
[08:43] entropy loss here, we take the negative
[08:45] logarithm of the model's predicted
[08:47] probability of the correct answer. The
[08:49] model's current probability of pairs is
[08:51] only 8.6%.
[08:53] Leading to a cross entropy loss of the
[08:55] negative log of 0.086 equals 2.45.
[08:59] If our model's predicted probability of
[09:01] Paris was 100%. Our cross entropy loss
[09:04] would equal the minus logarithm of 1
[09:06] which equals zero. Our job from here is
[09:09] to change our six m and b parameters to
[09:12] make our loss go down. As we saw in part
[09:15] one, we can do this efficiently by
[09:16] computing the slope of each of our
[09:18] parameters with respect to our loss.
[09:21] Combining these slopes into a vector
[09:22] called the gradient and using the
[09:24] gradient to make iterative updates to
[09:26] our weights. Let's now make this idea
[09:29] more tangible.
[09:31] Let's explore as we did last time how
[09:33] our loss varies with a single model
[09:35] parameter by plotting our loss as a
[09:37] function of m2.
[09:39] Our M2 parameter in our Paris neuron
[09:42] currently has a value of zero resulting
[09:44] in a loss of 2.45.
[09:47] If we increase the parameters value to
[09:49] 0.1, we can recmp compute our outputs
[09:52] and see that this increases our
[09:53] probability of being in Paris according
[09:55] to the model to 0.107,
[09:58] reducing our loss to 2.24. 24. Now, with
[10:01] these two computations of our loss for
[10:03] different values of M2, we've
[10:05] effectively estimated the value of our
[10:07] slope, delta L over delta M2.
[10:10] This tells us that if we increase M2,
[10:12] our loss will go down, increasing model
[10:15] performance.
[10:17] We could theoretically do this for all
[10:18] six parameters in our model and use
[10:21] these estimated slopes to guide the
[10:22] gradient descent learning process.
[10:25] However, in practice, this numerical
[10:27] approach is computationally intensive.
[10:29] since we have to recmp compute our
[10:30] outputs for each new parameter value we
[10:32] try and this approach can be inaccurate
[10:35] since we have to pick a fixed step size.
[10:38] Remarkably, it turns out that we can do
[10:40] much better the numerical estimates for
[10:42] these slopes. As we'll see, it's
[10:44] possible to exactly solve for the slopes
[10:46] of the loss function with respect to all
[10:48] parameters. When we're done, we'll have
[10:50] simple equations that we can plug into
[10:52] directly.
[10:53] The fact that you can do this is not
[10:55] immediately obvious even to those
[10:57] well-versed in calculus and
[10:58] optimization.
[11:00] In the 1950s at Stanford, Bernard
[11:02] Widow's group trained single layer
[11:04] neural networks using this numerical
[11:06] estimate of the slope for years until
[11:08] Widow and his graduate student Ted Hoff
[11:10] stumbled onto an early version of back
[11:12] propagation one day in late 1959. Even
[11:15] then, Widow and Hoff failed to see how
[11:17] to extend their method to neural
[11:19] networks with more than one layer. We'll
[11:21] see precisely how to do this after we
[11:23] complete our single layer example. The
[11:25] central idea of back propagation is to
[11:27] apply the rules of calculus to compute
[11:29] the equations for our slopes in a
[11:31] particularly efficient way. Let's start
[11:34] with our slope delta L over delta M2. In
[11:37] the language of calculus, this is the
[11:38] partial derivative DL DM2, the rate of
[11:41] change of our loss L with respect to our
[11:43] model parameter M2. Now, we already have
[11:46] some equations that relate the loss to
[11:48] our parameter M2. We know that our cross
[11:50] entropy loss is equal to the negative
[11:52] logarithm of our model's output
[11:54] probability of the correct answer yhat.
[11:56] This would be yhat 2 in the case of our
[11:58] Paris example. We can plug in our
[12:01] softmax equation for yhat and even go
[12:04] one step further and plug in the
[12:06] equations for each of our neurons
[12:08] getting a complete equation for our loss
[12:10] l in terms of our input x and all six
[12:12] model parameters.
[12:15] If you're familiar with calculus, an
[12:17] obvious approach from here might be to
[12:18] compute the partial derivative we're
[12:20] after or dlddm2 by differentiating our
[12:23] expression with respect to m2. This does
[12:26] work, but is complex and doesn't really
[12:28] make use of the underlying graph
[12:29] structure of neural networks. Instead,
[12:32] it turns out that we can consider the
[12:33] layers of our neural network
[12:34] independently, solve for the rate of
[12:37] change through each layer, and then
[12:38] compose these rates of change together
[12:40] to much more efficiently solve for DL
[12:42] DM2. Consider the simple example where
[12:45] we have two compute blocks. The first
[12:48] mapping some input x to an output y with
[12:50] the equation y= 2x and a second compute
[12:53] block mapping y to z with the equation z
[12:56] = 4 y. As we did with our neural
[12:59] network, we can put our equations
[13:00] together by substituting y = 2x into our
[13:03] second equation. Simplifying, we see
[13:06] that the equation for our full system is
[13:08] z= 8x. The slope or derivative of this
[13:11] overall system equation is 8. Now, a
[13:14] more modular way to reach the same
[13:16] answer is to compute the derivative of
[13:18] each block individually. Computing the
[13:21] slope of our first block dydx equals 2
[13:23] and the slope of our second block dzy =
[13:26] 4. We can then multiply these rates of
[13:29] change together to get our overall rate
[13:31] of change. So, 2 * 4= 8 or dydx * dzy =
[13:37] dz dx.
[13:39] This is known as the chain rule in
[13:41] calculus and scales much more cleanly to
[13:43] models with many layers like llama.
[13:46] Applying the same process to our neural
[13:48] network, we can break apart dlddm into
[13:51] dhdm* dlddh.
[13:53] Breaking apart the partial derivatives
[13:55] of our linear model and our loss and
[13:57] softmax function. Now calculating the
[14:00] partial derivative across our logarithm
[14:02] and softmax function is still a bit
[14:04] involved. I'll put the process on screen
[14:06] in case you're interested and want to
[14:07] pause.
[14:09] However, the big exciting takeaway is
[14:10] that the result is very simple.
[14:13] It turns out that the logarithm from our
[14:15] cross entropy loss and the exponentials
[14:17] from our softmax operation basically
[14:19] cancel out leaving us with dldh is equal
[14:22] to yhat minus y where yhat is a vector
[14:25] made up of our three output
[14:27] probabilities and y is a vector that
[14:29] equals one at the index of the correct
[14:31] answer and zero everywhere else.
[14:34] As an example, when we plug in our Paris
[14:36] GPS point and compute our model's
[14:38] probabilities, we get yhat 1 equals 0.91
[14:41] for Madrid, yhat 2= 0.09 for Paris, and
[14:45] Yhat 3 rounds down to 0.00 for Berlin.
[14:49] Since our ground truth label is Paris,
[14:52] this means that y1 equals 0, y2= 1, and
[14:55] y3 equals 0. This is known as one hot
[14:58] encoding.
[15:01] So our partial derivative dlh1 from
[15:03] Madrid is equal to 0.91 minus 0 equals
[15:07] 0.91. This large positive value for
[15:10] dldh1 means that if we increase h1 our
[15:13] loss will increase. The partial
[15:16] derivative for paris dldh is equal to
[15:18] 0.09 -1 = -0.91.
[15:23] This large negative value means that if
[15:25] we increase h2 our loss will go down.
[15:29] Now remember that H is just an
[15:30] intermediate output of our model that
[15:32] depends both on our model parameters and
[15:34] data. We've solved for DLH. But to get a
[15:38] derivative we can actually use to train
[15:40] our model like dlddm2, we need to
[15:42] complete our chain rule math. Our
[15:45] remaining partial derivative dh2dm2
[15:48] is asking us to find the rate of change
[15:49] of our intermediate output h2 with
[15:52] respect to our model parameter m2. These
[15:55] variables are linked by our linear
[15:56] equation h2= m2 * x + b2. We typically
[16:01] think of this equation as a line with a
[16:03] fixed slope of m2 and a y intercept of
[16:05] b2. However, our partial derivative is
[16:08] asking us to think of m2 as a variable.
[16:11] This makes sense because learning
[16:12] consists of changing our parameters m
[16:14] and b.
[16:16] From this perspective, our input x is
[16:18] constant and m2 and h2 are variables.
[16:21] This still looks like a straight line,
[16:23] but now its slope is equal to our input
[16:25] x.
[16:27] So the partial derivative of the output
[16:29] of our neuron with respect to our model
[16:30] parameter m2 is just the slope of our
[16:32] line x.
[16:36] Intuitively, this tells us that the
[16:37] impact of our model parameter m2 on our
[16:39] neurons output depends on the input
[16:42] value x. If the input value x to our
[16:45] model is small, then the value of our
[16:47] parameter m2 matters less in our
[16:49] derivative calculation. and this
[16:51] neuron's parameters do not need to be
[16:52] updated as much as the model learns from
[16:54] this example. Alternatively, if our
[16:57] neuron's input X is large, it has more
[16:59] of an impact on our final loss and needs
[17:02] a larger update. This intuition will be
[17:05] important as we expand to deeper models.
[17:08] Replacing DHDM2 with our result X, we
[17:11] now have a complete expression for
[17:12] DLDDM2.
[17:14] Computing DLDDM2 for our Paris example,
[17:17] we multiply our input longitude 2.314°
[17:20] by our model's output probability of
[17:22] Paris 0.9 minus one, computing a final
[17:26] partial derivative value of -2.140.
[17:30] So all of this back propagation
[17:32] mathematics is telling us that for this
[17:34] single pair training point, if we
[17:36] increase our parameter m2 by one, we
[17:39] expect our loss to decrease by 2.140.
[17:43] Partial derivative values like this are
[17:45] the key result of back propagation and
[17:47] are the components of the gradient
[17:49] vector which drives the entire learning
[17:51] process for virtually all modern AI
[17:54] models. To compute the full gradient
[17:56] vector for our tiny GPS model, we have
[17:58] to solve for five more equations, one
[18:00] for each remaining parameter in our
[18:02] model. This mathematics ends up being
[18:04] very similar to the process we already
[18:06] followed for solving for DLDDM2.
[18:09] Typically, these individual equations
[18:11] are rolled up into equations that
[18:12] operate on vectors and matrices instead
[18:14] of individual numbers. So, we end up
[18:16] with a single equation to compute the
[18:18] partial derivatives with respect to all
[18:20] three M values and another single
[18:22] equation for all three B values. We can
[18:25] now use these equations to compute the
[18:27] partial derivatives for all six model
[18:28] parameters, giving us a full gradient
[18:31] vector. As we saw earlier, our DLDM2
[18:34] value is large and negative, meaning
[18:36] that if we increase M2, our loss on this
[18:39] training example will decrease. This
[18:41] makes sense because our model's
[18:42] predicted probability of the correct
[18:44] answer of Paris is low right now. And
[18:46] increasing M2 will increase the model's
[18:48] probability of Paris, lowering our loss.
[18:52] DLDDM1, on the other hand, is large and
[18:54] positive. This means that if we increase
[18:56] M1, our loss will go up. This makes
[18:58] sense because our model's probability of
[19:00] the wrong answer Madrid is currently
[19:02] high and increasing M1 will further
[19:04] increase this probability increasing our
[19:07] loss. Since positive slopes like this
[19:09] mean that increasing our parameter will
[19:11] increase our loss. To train our model to
[19:13] reduce our loss, we want to adjust our
[19:15] parameters in the opposite direction of
[19:17] our gradient. We should reduce M1 to
[19:20] reduce loss and increase M2 to reduce
[19:23] loss. Mathematically, we can do this by
[19:26] taking our current model parameters,
[19:28] subtracting a scaled version of our
[19:29] gradients, and replacing our parameters
[19:32] with the result. This is the gradient
[19:34] descent process we visualized in part
[19:36] one as going downhill on the model's
[19:38] loss landscape. And thanks to back
[19:40] propagation, we now have an efficient
[19:41] way to compute our gradient vector. The
[19:44] scaling factor controls the size of step
[19:46] we take on our loss landscape and is
[19:49] known as the learning rate. We generally
[19:51] want it to be fairly small, something
[19:53] like 0.00001.
[19:56] This is because our gradient only gives
[19:58] us the slope in a very local
[20:00] neighborhood. And as we saw in part one,
[20:02] our loss landscapes can be highly
[20:04] complex with slopes that quickly shift
[20:06] as we update our parameters.
[20:09] We also saw in part one how visualizing
[20:11] gradient descent as going downhill in
[20:13] our lost landscape is a fairly
[20:14] incomplete picture of how our model
[20:16] learns.
[20:18] Let's see if we can use our computed
[20:19] gradients to observe the learning
[20:21] process more directly.
[20:23] We'll visualize our gradients as a bar
[20:25] around each connecting line in our model
[20:27] where thicker bars correspond to larger
[20:29] gradients. We'll use a similar approach
[20:31] when we visualize the gradients flowing
[20:33] through our full-size models later.
[20:35] We'll also visualize the progress as our
[20:37] model learns on a map. We'll plot our
[20:39] current training example as a point on
[20:41] the map and visualize our model's
[20:43] outputs as a heat map on top of the map
[20:46] where the probability of Madrid is shown
[20:47] in cyan, the probability of Paris is
[20:49] shown in yellow and the probability of
[20:51] Berlin is green and brighter colors
[20:54] correspond to higher probabilities.
[20:56] Our first training point is in Paris. As
[20:59] we saw earlier, the initial model
[21:01] parameters we chose result in a high
[21:02] output probability for Madrid for this
[21:05] input longitude. We can also see this on
[21:07] our map. Paris is in the blue region on
[21:10] our map where our model's top prediction
[21:11] is Madrid. This error results in high
[21:14] gradients for our Paris and Madrid
[21:16] neurons. Moving forward one step, these
[21:19] high gradients lead to a reduced value
[21:21] of our M1 parameter and an increase in
[21:23] our M2 parameter, which shifts the
[21:26] yellow Paris region on our map a little
[21:28] to the right, closer to the true
[21:30] location of Paris. Our next training
[21:33] example is from Madrid, which our model
[21:35] mclassifies as being in Berlin, leading
[21:38] to high gradient values for both Madrid
[21:40] and Berlin. Note that on our map, these
[21:42] regions need to completely switch sides.
[21:45] Running gradient descent for about 40
[21:47] steps is enough for our gradient updates
[21:49] to accomplish this. Correctly
[21:51] classifying Madrid and Berlin and just
[21:54] leaving our Paris region not actually on
[21:56] top of Paris. Another 40 steps or so are
[22:00] enough for our gradients to slowly
[22:02] increase our M2 and B2 values, moving
[22:05] our model's predicted Paris region on
[22:07] top of the actual city. Note that our
[22:09] gradients become smaller as our model
[22:11] learns and makes smaller errors. We can
[22:14] see a little more under the hood of our
[22:16] model by running the same training
[22:17] process again, but this time while
[22:19] visualizing the little linear models
[22:21] learned by each neuron. Our initially
[22:23] chosen slopes of 1, 0, and minus one
[22:26] make our initial linear models go
[22:27] uphill, flat, and downhill. As our model
[22:31] learns, our Madrid neuron flips to
[22:32] pointing downhill. Our Paris neuron
[22:35] wobbles a bit and ends up going slightly
[22:37] uphill. And our Berlin neuron flips from
[22:39] going downhill to uphill. If we
[22:42] visualize all three neurons lines on the
[22:44] same axis, we can see how our model is
[22:46] learning to use these little linear
[22:47] models together. For a given input
[22:50] longitude, the output of each neuron is
[22:52] equal to the height of its line on this
[22:54] plot. So for the Paris example with a
[22:57] longitude of 2.3376°,
[23:00] the Madrid neurons line has a height of
[23:02] 2.34.
[23:03] This is equal to our H1 value for this
[23:05] input. Our softmax function just
[23:08] amplifies whichever input is largest. So
[23:11] whichever line is on top at a given
[23:13] longitude in our plot will lead to the
[23:15] model's highest output probability.
[23:17] Running our training animation again, we
[23:19] see that our gradients push the Madrid
[23:21] line, so it has the largest values over
[23:23] our Madrid points. The Paris line, so it
[23:26] has its largest value over our Paris
[23:28] points, and our Berlin line, so it has
[23:29] the largest value over our Berlin
[23:31] points. In our full map view, these
[23:34] lines are equivalent to three planes.
[23:36] And through back propagation, our model
[23:38] learns to position each plane above the
[23:40] correct city.
[23:42] When we apply our softmax function to
[23:44] the outputs of our neurons, softmax
[23:46] squishes and curves our planes, but
[23:48] retains the same general structure,
[23:50] resulting in our final heat map.
[23:53] Now, what's really compelling about back
[23:55] propagation is how it's able to scale to
[23:57] larger problems and ultimately massive
[24:00] language models. Let's increase the
[24:02] complexity of our problem and see how
[24:03] our intuitions and mathematics hold up.
[24:06] Let's begin by adding a fourth city to
[24:08] our training set, Barcelona. Barcelona
[24:11] has a very similar longitude to Paris.
[24:13] So, our model now needs to take in both
[24:15] longitude and latitude, which we'll call
[24:17] X1 and X2. We now need to expand the
[24:20] little linear models in our neurons to
[24:22] include both inputs. Meaning, we now
[24:25] have two slope values M per neuron.
[24:27] Visually, instead of a line, each neuron
[24:30] now looks like a little plane, where our
[24:32] two slope values control the steepness
[24:33] of the plane in each direction. Our back
[24:37] propagation math works out almost
[24:38] exactly the same. We just have more
[24:41] parameters. We now have four neurons,
[24:43] one for each city. Now with three
[24:45] parameters each with two M values that
[24:48] multiply each of our two inputs and a
[24:50] single bias value. This makes for 12
[24:53] total parameters. So we need 12
[24:55] derivatives to update our weights.
[24:58] Training our new twoinput model, we see
[25:00] that it's quickly able to fit our four
[25:01] planes to our data and correctly divide
[25:04] our map into four regions. one for each
[25:06] city. Putting our planes together over
[25:08] our map, we can see how our model has
[25:10] fit our planes together. So, our Madrid
[25:12] plane is on top of all the other planes
[25:14] above Madrid. Our Barcelona plane is on
[25:17] top above Barcelona and so on. Of
[25:20] course, simple planes like this can only
[25:22] learn a very limited set of patterns. To
[25:25] see this issue more clearly, let's
[25:27] consider the most complex border in the
[25:29] world between Belgium and the
[25:30] Netherlands in the municipality of
[25:32] Barlay Hertok. These regions of the map
[25:35] are part of the Netherlands and these
[25:37] regions are part of Belgium. Given a
[25:39] single plane for Belgium and a single
[25:41] plane for the Netherlands, there's no
[25:43] way to cleanly divide these complex
[25:44] regions.
[25:46] Now, it might seem a bit random to spend
[25:49] our time training a model to fit
[25:50] esoteric European borders. But this type
[25:53] of problem has more in common with
[25:54] training large language models than you
[25:56] may expect. Our llama model represents
[25:58] individual tokens like Madrid, Paris,
[26:00] and Berlin as vectors of48 floatingoint
[26:03] numbers. When we pass in some text like
[26:06] the capital of France is, there's a
[26:08] specific length 2048 vector in our
[26:11] model, specifically at the final
[26:12] position in the residual stream that is
[26:14] iteratively pushed by each layer towards
[26:17] the vector for Paris.
[26:19] This gets really interesting when we
[26:20] consider all the different types of text
[26:22] that can lead to a next token of Paris,
[26:24] Madrid, or Berlin.
[26:26] If we pass in a variety of training text
[26:28] examples from the wiki text data set
[26:30] that all lead up to next tokens of
[26:32] Paris, Madrid or Berlin and compute the
[26:34] predicted next token vectors for each
[26:36] training example for a layer in the
[26:38] middle of our model, we end up with a
[26:40] set of length 248 vectors each generated
[26:43] by examples with next tokens of Madrid,
[26:45] Paris, or Berlin in our training set.
[26:49] One way to think of these vectors is as
[26:51] the coordinates of our examples in the
[26:53] highdimensional map of language learned
[26:55] by our model.
[26:57] We can get a sense of the geometry of
[26:59] this map by projecting down from 248
[27:02] dimensions to two using a umap algorithm
[27:05] which seeks to preserve the distances
[27:07] between points in the highdimensional
[27:08] space.
[27:10] We see some really interesting
[27:11] clustering in this space. For example,
[27:14] this little cluster of Paris examples
[27:16] are all different references to the
[27:18] Treaty of Paris. And this little cluster
[27:20] are all references to George Gershwin's
[27:22] an American in Paris.
[27:24] Just as the disconnected parts of our
[27:26] municipality of Barlay Herto all need to
[27:28] map to the same country of Belgium, the
[27:31] disconnected regions in our space of
[27:32] language all need to map to the same
[27:34] next token of Paris. And it's up to our
[27:36] model to figure out how to partition and
[27:38] reshape our space to achieve this.
[27:42] When Marvin Minsky rejected back
[27:44] propagation in the early 1970s, he
[27:46] dismissed the idea because it converged
[27:48] too slowly and because according to
[27:50] Minsky, it couldn't learn anything too
[27:52] difficult. Minsky was right that
[27:54] learning by gradient descent can take
[27:56] many steps. This mattered a lot given
[27:58] the compute power available at the time.
[28:01] However, he enormously underestimated
[28:03] the ability of our simple back
[28:05] propagation algorithm to scale to solve
[28:07] incredibly complex problems.
[28:10] Next time, we'll see what Minsky missed.
[28:14] Back in 2019, I completely quit Welch
[28:17] Labs. I had just tried going full-time
[28:19] creating videos, but I wasn't able to
[28:21] earn enough money to make it work. I got
[28:23] frustrated and I quit. I went off and
[28:26] worked as a machine learning engineer,
[28:27] which was great, but I couldn't shake
[28:29] the feeling that I was really supposed
[28:30] to be making videos. Starting in 2022, I
[28:34] slowly eased back on Tik Tok and was
[28:36] able to gradually build enough momentum
[28:38] to take another crack at going full-time
[28:40] last year. When I quit in 2019, I had
[28:43] some time to really think about what
[28:44] kept pulling me back into making videos.
[28:47] And I realized that deep down it was
[28:49] really about education.
[28:51] I loved math and science as a kid, but I
[28:54] really disliked the way I had to learn
[28:55] it in school. After undergrad, I really
[28:58] found myself questioning if I even liked
[29:00] math at all. Only through my own work
[29:02] and study did I fall back into love with
[29:04] math and science years later. And now I
[29:06] want to use Welsh Labs to make education
[29:08] better. But I've realized for me to be
[29:11] able to do this, I have to first build a
[29:14] viable business. If I can't support
[29:16] myself and my family, I can't spend the
[29:17] time I need to make this work. Last
[29:20] year, through sponsorships, poster and
[29:22] book sales, and support on Patreon, I
[29:24] was able to make about half of what I
[29:26] made as a machine learning engineer. I'm
[29:29] not going to lie, so far this is a much
[29:31] harder way to earn a living. My goal
[29:34] this year is to replace my full income.
[29:36] This will allow me to really reach
[29:37] escape velocity and continue full-time
[29:40] on Welch Labs. Sponsorships, posters,
[29:43] and book sales are going well this year,
[29:45] but to hit my goal, I need to grow
[29:46] Patreon as well. Your monthly support on
[29:49] Patreon would mean a lot. As a way to
[29:52] say thank you, today I'm launching a new
[29:54] reward. Starting at the $5 per month
[29:56] level, I'll send you a real paper cutout
[29:59] used in a Welch Labs video. It comes in
[30:01] a nice protective sleeve with the Welch
[30:03] Labs logo on the front. And on the back,
[30:05] it says the video it came from, the
[30:07] release date, and a signed by me. These
[30:09] are a lot of fun. I have them going all
[30:11] the way back to 2017. At the $5 per
[30:14] month level, you'll receive a smaller
[30:15] cutout and a larger cutout at the $10 or
[30:18] higher level. Cutouts ship after your
[30:20] first monthly payment goes through, and
[30:22] you'll find a link to the Watch Labs
[30:23] Patreon in the description below. Huge
[30:26] thank you to everyone who supported
[30:27] Watch Labs over the years. Thanks for
[30:29] watching.