---
source_url: https://www.youtube.com/watch?v=UZDiGooFs54
ingested: 2026-07-09
video_id: UZDiGooFs54
title: The moment we stopped understanding AI [AlexNet]
series: None
---

[00:00] this is an activation Atlas it gives us
[00:02] a glimpse into the high-dimensional
[00:04] embedding spaces modern AI models use to
[00:07] organize and make sense of the world the
[00:09] first model to really see the world like
[00:11] this alexnet was published in 2012 in an
[00:14] 8-page paper that shocked the computer
[00:16] vision Community by showing that an old
[00:18] AI idea would work unbelievably well
[00:21] when scaled the paper second author ilas
[00:24] HK would go on co-found open AI where he
[00:27] and the open AI team would massively
[00:29] scale up this idea again to create chat
[00:31] GPT this video is sponsored by kiwico
[00:34] more on them later if you look under the
[00:37] hood of chat GPT you won't find any
[00:39] obvious signs of intelligence instead
[00:42] you'll find layer after layer of compute
[00:44] blocks called transformers this is what
[00:46] the T and GPT stands for each
[00:48] Transformer performs a set of fixed
[00:50] Matrix operations on an input Matrix of
[00:52] data and typically returns an output
[00:54] Matrix of the same size to figure out
[00:56] what it's going to say next chat GPT
[00:58] breaks apart what you ask get into words
[01:00] and word fragments Maps each of these to
[01:03] a vector and stacks all of these vectors
[01:05] together into a matrix this Matrix is
[01:08] then passed into the first Transformer
[01:10] block which returns a new Matrix of the
[01:12] same size this operation is then
[01:14] repeated again and again 96 times in
[01:17] chat GPT 3.5 and reportedly 120 times in
[01:20] chat GPT 4 now here's the Absurd part
[01:24] with a few caveats the next word or word
[01:27] fragment that chat GPT says back to you
[01:29] is is literally just the last column of
[01:31] its final output Matrix mapped from a
[01:34] vector back to text to formulate a full
[01:37] response this new word or word fragment
[01:39] is appended to the end of the original
[01:41] output and this new slightly longer text
[01:43] is fed back into the input of chat GPT
[01:46] this process is repeated again and again
[01:49] with one new column added to the input
[01:51] Matrix each time until the model's
[01:53] output returns a special stop word
[01:55] fragment and that is it one Matrix
[01:58] multiply after another GPT slowly morphs
[02:01] the input you give it into the output it
[02:03] returns where is the
[02:06] intelligence how is it that these 100 or
[02:08] so blocks of dumb compute are able to
[02:10] write essays translate language
[02:12] summarized books solve math problems
[02:14] explain complex Concepts or even at the
[02:16] next line of this script the answer lies
[02:19] in the vast amounts of data these models
[02:21] are trained on okay pretty good but not
[02:24] quite what I wanted to say next the
[02:26] alexnet paper is significant because it
[02:28] marks the first time we really see
[02:29] layers of compute blocks like this
[02:31] learning to do unbelievable things an AI
[02:34] Tipping Point towards high performance
[02:36] in scale and away from explainability
[02:39] while chat GPT is trained to predict the
[02:41] next word fragment given some text Alex
[02:43] net is trained to predict a label given
[02:45] an image the input image to alexnet is
[02:48] represented as a three-dimensional
[02:49] Matrix or tensor of RGB intensity values
[02:53] and the output is a single Vector of
[02:54] length 1,000 where each entry
[02:57] corresponds to Alex Net's predicted
[02:58] probability that the input put image
[03:00] belongs to one of the a thousand classes
[03:02] in the imag net data set things like
[03:04] tabby cats German Shepherds hot dogs
[03:06] toasters and aircraft
[03:08] carriers just like chat GPT today
[03:11] alexnet was somehow magically able to
[03:13] map the inputs we give it into the
[03:15] outputs we wanted using layer after
[03:17] layer of compute block after training on
[03:19] a large data set one nice thing about
[03:22] Vision models however is that it's
[03:23] easier to poke around under the hood and
[03:26] get some idea of what the model has
[03:27] learned one of the first under the hood
[03:30] insights that kfy suit and Hinton show
[03:32] in the Alex net paper is that the model
[03:34] has learned some very interesting visual
[03:36] patterns in its first layer the first
[03:39] five layers of alexnet are all
[03:40] convolutional blocks first developed in
[03:43] the late 1980s to classify handwritten
[03:45] digits and can be understood as a
[03:47] special case of the Transformer blocks
[03:49] in chat GPT and other large language
[03:51] models in convolutional blocks the input
[03:54] image tensor is transformed by sliding a
[03:56] much smaller tensor called a kernel of
[03:58] learned weight values across the image
[04:00] and at each location Computing the dot
[04:02] product between the image and kernel
[04:05] here it's helpful to think of the dot
[04:06] product as a similarity score the more
[04:09] similar a given patch of the image and
[04:10] kernel are the higher the resulting dot
[04:12] product will be Alex net uses 96
[04:15] individual kernels in its first layer
[04:18] each of Dimension 11 by 11 by3 so
[04:20] conveniently we can visualize them as
[04:22] little RGB images these images give us a
[04:25] nice idea of how the first layer of
[04:27] alexnet sees the image the upper kernels
[04:30] in this figure show where Alex and has
[04:31] clearly learned to detect edges or rapid
[04:34] changes from light to dark at various
[04:36] angles images with similar patterns will
[04:38] generate High Dot products with these
[04:40] kernels below we see where Alexon has
[04:42] learned to detect Blobs of various
[04:44] colors these kernels are all initialized
[04:46] as random numbers and the patterns we're
[04:49] looking at are completely learned from
[04:50] data sliding each of our 96 kernels over
[04:53] the input image and Computing the dot
[04:55] product at each location produces a new
[04:57] set of 96 matrices sometimes called
[05:00] activation Maps conveniently we can view
[05:03] these as images as well the activation
[05:06] Maps show us which parts of an image if
[05:08] any match a given kernel well if I hold
[05:11] up something visually similar to a given
[05:13] kernel we see high activation in that
[05:16] part of the activation
[05:17] map notice that it goes away when I
[05:20] rotate the pattern by 90° the image and
[05:23] kernel are no longer aligned you can
[05:25] also see various activation Maps picking
[05:27] up edges and other lowl features in our
[05:30] image of course finding edges and color
[05:32] blobs in images is still hugely removed
[05:35] from recognizing complex Concepts like
[05:36] German Shepherds or aircraft carriers
[05:39] what's astounding about deep neural
[05:41] networks like alexnet and chat GPT is
[05:43] that from here all we do is repeat the
[05:45] same operation again just with a
[05:47] different set of learned weights for
[05:50] Alex net this means that these 96
[05:52] activation maps are stacked together
[05:53] into a tensor that become the input to
[05:56] the exact same type of convolutional
[05:58] compute block the second overall layer
[06:00] in the model we can make our activations
[06:02] easier to see by removing the values
[06:04] close to zero unfortunately in our
[06:06] second layer we can't learn much by
[06:08] simply visualizing the weight values and
[06:10] the kernels themselves the first issue
[06:13] is that we just can't see enough colors
[06:15] the depth of the kernel has to match the
[06:17] depth of the incoming data in the first
[06:19] layer of alexnet the depth of the
[06:21] incoming data is just three because the
[06:23] model takes in color images with red
[06:25] green and blue color channels however
[06:28] since the first layer computes 9 6
[06:29] separate activation Maps the computation
[06:32] in the second layer of alexnet is like
[06:34] processing images with 96 separate color
[06:37] channels the second factor that makes
[06:39] what's happening in the second layer of
[06:40] alexnet more difficult to visualize is
[06:43] that the dot products are really taking
[06:44] weighted combinations of the
[06:46] computations in the first layer we need
[06:48] some way to visualize how the layers are
[06:50] working together a simple way to see
[06:52] what's going on is to try to find parts
[06:54] of various images that strongly activate
[06:56] the outputs of the second layer for
[06:59] example this activation map appears to
[07:01] be putting together Edge detectors to
[07:03] form basic Corners remarkably as we move
[07:06] deeper into alexnet strong activations
[07:08] correspond to higher and higher level
[07:11] concepts by the time we reach the fifth
[07:13] layer we have activation maps that
[07:15] respond very strongly to faces and other
[07:17] highlevel Concepts and what's incredible
[07:20] here is that no one explicitly told Alex
[07:22] net what a face is all alexnet had to
[07:25] learn from were the images and labels in
[07:27] the imag net data set which does not not
[07:29] contain a person or a face class Alex
[07:32] net was able to learn completely on its
[07:34] own both that faces are important and
[07:36] how to recognize them to better
[07:39] understand what a given Colonel and Alex
[07:40] net has learned we can also look at the
[07:42] examples in the training data set that
[07:44] give the highest activation values for
[07:46] that kernel for our face kernel not
[07:48] surprisingly we find examples that
[07:50] contain people finally there's this
[07:52] really interesting technique called
[07:53] feature visualization where we can
[07:55] generate synthetic images that are
[07:57] optimized to maximize a given activation
[08:00] these synthetic images give us another
[08:02] way to see what a specific activation
[08:03] layer is looking
[08:05] for by the time we reach the final layer
[08:07] of alexnet our image has been processed
[08:09] into a vector of length
[08:12] 4,096 the final layer performs one last
[08:14] Matrix computation on this Vector to
[08:16] create a final output Vector of length
[08:18] 1,000 with one entry for each of the
[08:21] classes in the imag net data set chfi
[08:23] suit and Hinton noticed that the second
[08:25] to last layer Vector demonstrated some
[08:28] very interesting properties
[08:30] one way to think about this Vector is as
[08:32] a point in 4,096 dimensional space each
[08:35] image we pass into the model is
[08:37] effectively mapped to a point in this
[08:39] space all we have to do is just stop one
[08:41] layer early and grab this Vector just as
[08:44] we can measure the distance between two
[08:46] points in 2D space we can also measure
[08:48] the distance between points or images in
[08:50] this high-dimensional space hinton's
[08:52] team ran a simple experiment where they
[08:54] took a test image in the imag net data
[08:56] set computed its corresponding vector
[08:59] and then search for the other images in
[09:01] the imag net data set that were closest
[09:03] or the nearest neighbors to the test
[09:04] image in this High dimensional space
[09:07] remarkably the nearest neighbor images
[09:09] showed highly similar Concepts to the
[09:11] test images in figure four from the Alex
[09:13] net paper we see an example where an
[09:15] elephant test image yields nearest
[09:17] neighbors that are all
[09:19] elephants what's interesting here too is
[09:21] that the pixel values themselves between
[09:23] these images are very different Alex net
[09:25] really has learned high-dimensional
[09:27] representations of data where similar
[09:29] concepts are physically close this
[09:32] high-dimensional space is often called a
[09:33] latent or embedding space in the Years
[09:36] following the alexnet paper it was shown
[09:38] that not only distance but
[09:40] directionality in some of these
[09:41] embedding spaces is Meaningful the demos
[09:44] you see where faces are age or gender
[09:46] shifted often work by first mapping an
[09:48] image to a vector in an embedding space
[09:51] and then literally moving this point in
[09:53] the age or gender Direction in that
[09:55] embedding space and then mapping the
[09:57] modified Vector back to an image
[10:00] before we get into activation atlases
[10:02] which give us an amazing way to
[10:03] visualize these embedding spaces please
[10:06] take a moment to consider if this video
[10:07] sponsor is something that you or someone
[10:09] in your life would enjoy I was genuinely
[10:12] really excited to work with this company
[10:14] they make incredibly thoughtful
[10:15] educational products and by using the
[10:17] link in the description below you're
[10:19] really helping me make more of these
[10:21] videos this video sponsor is kiwo they
[10:24] make these fun and super well-designed
[10:26] educational crates for kids of all ages
[10:29] they have nine different monthly
[10:30] subscription lines to choose from focus
[10:32] on different areas of steam and you can
[10:34] also buy individual crates which are
[10:36] great for trying out kiwo and make
[10:38] amazing gifts growing up I was
[10:41] constantly building here I am building a
[10:43] tower outside my house to my second
[10:45] story bedroom I was obsessed with
[10:48] electronics and would have absolutely
[10:49] loved projects like this pencil
[10:51] sharpener from the Eureka crate line
[10:53] which is focused on science and
[10:55] engineering I really believe that this
[10:57] type of Hands-On self-driven learning is
[10:59] magical when I really think about my own
[11:01] education it's the times that I've been
[11:03] fully absorbed in projects like this
[11:05] that I learned the most and now that I'm
[11:07] a dad I really want my kids to have the
[11:09] same kind of experiences kiwo really
[11:12] does an amazing job boxing up start to
[11:14] finish projects like this my daughter
[11:17] just got the panda crate for fine motor
[11:19] skills it includes these special crayons
[11:21] specifically designed to help her learn
[11:23] different ways of grasping you can see
[11:25] her here insisting that she gets to
[11:26] bring them in the car with us huge
[11:28] thanks to kiwo for sponsoring this video
[11:31] use the discount code Welch labs for 50%
[11:33] off your first month of a subscription
[11:36] now back to alexnet there's some really
[11:38] amazing work that combines the synthetic
[11:40] images that maximize a given set of
[11:42] activations with a two-dimensional
[11:44] projection or flattening out of the
[11:46] embedding space to make these incredible
[11:48] visualizations called activation atlases
[11:51] Neighbors on the activation Atlas are
[11:53] generally close in the embedding space
[11:55] and show similar Concepts the model has
[11:58] learned we're getting a peak into how
[12:00] deep neural networks organize the visual
[12:02] world looking at the synthetic images
[12:04] that most activate neighborhoods of
[12:06] neurons we can visually walk through the
[12:08] embedding space of the model seeing it
[12:11] Mak smooth visual transitions from
[12:12] Concepts like zebras to Tigers to
[12:15] leopards to rabbits moving to the middle
[12:17] layers of the model we can see less
[12:19] fully formed but still meaningful
[12:21] Concepts moving along this path
[12:23] amazingly correlates with the number and
[12:25] size of pieces of fruit in an image the
[12:28] same princip applies in large language
[12:30] models words and word fragments are
[12:33] mapped to vectors in an embedding space
[12:35] where words with similar meanings are
[12:37] close to each other and the directions
[12:39] in the embedding space are sometimes
[12:41] semantically meaningful there's some
[12:43] incredible very recent work from the
[12:44] team at anthropic that shows how sets of
[12:47] activations can be mapped to Concepts in
[12:49] language these results can help us
[12:51] better understand how llms work and can
[12:53] be used to modify Model Behavior after
[12:56] clamping a set of activations that
[12:58] correspond to the concept Golden Gate
[13:00] Bridge to a high value the llm the team
[13:03] was experimenting with began to identify
[13:05] itself as the Golden Gate Bridge Alex
[13:08] net won the imag net large scale visual
[13:10] recognition challenge by a wide margin
[13:12] in 2012 the third year the challenge was
[13:15] run in Prior years the winning teams
[13:18] used approaches that under the hood look
[13:20] much more like what you might expect to
[13:22] find in an intelligent system the 2011
[13:25] winner used a complex set of very
[13:27] different algorithms starting starting
[13:29] with an algorithm called sift which is
[13:31] composed of specialized image analysis
[13:33] techniques developed by experts over
[13:35] many years of research Alex net in
[13:37] contrast is an implementation of a much
[13:40] older AI idea an artificial neural
[13:43] network where the behavior of the
[13:44] algorithm is almost entirely learned
[13:46] from data the dot product operation
[13:49] between the data and a set of Weights
[13:51] was originally proposed by molic and
[13:53] pits in the 1940s as a dramatically
[13:55] oversimplified model of the neurons in
[13:57] our brain in the second half of each
[14:00] Transformer Block in chat GPT and at the
[14:02] end of alexnet you'll find a multi-layer
[14:05] perceptron the perceptron is a learning
[14:08] algorithm and physical machine from the
[14:10] 1950s that uses molic and pits neurons
[14:13] and can learn to perform basic shaped
[14:15] recognition tasks back in the 1980s a
[14:18] younger Jeff Hinton and his
[14:19] collaborators at Carnegie melon showed
[14:21] how to train multiple layers of these
[14:23] perceptrons using a multivariate
[14:25] calculus technique called back
[14:27] propagation these models a couple layers
[14:30] deep and remarkably pretty good at
[14:31] driving cars in the 1990s Yan laon now
[14:35] Chief AI scientist at meta was able to
[14:38] train five layer deep models to
[14:40] recognize handwritten digits despite the
[14:43] intermittent successes of artificial
[14:44] neural networks over the years this
[14:46] approach was hardly the accepted way to
[14:48] do AI right up until the publication of
[14:51] alexnet if this was obviously the way to
[14:54] build intelligence systems we would have
[14:56] done it decades earlier as Ian
[14:58] Goodfellow writes in his excellent deep
[15:00] learning book at this point deep
[15:02] networks were generally believed to be
[15:03] very difficult to train we now know that
[15:06] algorithms that have existed since the
[15:07] 1980s work quite well but this was not
[15:10] apparent Circ 2006 the issue is perhaps
[15:13] simply that these algorithms were too
[15:15] computationally costly to allow much
[15:17] experimentation with the hardware
[15:18] available at the time the key difference
[15:21] in 2012 was simply scale of data and
[15:24] scale of compute the imag net data set
[15:27] was the largest labeled data set of its
[15:28] kind kind to date with over 1.3 million
[15:31] images and thanks to Nvidia gpus in 2012
[15:35] hinton's team had access to roughly
[15:37] 10,000 times more compute power than Yan
[15:39] laon had 15 years before laon's layet 5
[15:43] model had around 60,000 learnable
[15:46] parameters Alex net increased this a
[15:48] thousandfold to around 60 million
[15:50] parameters today chat GPT has well over
[15:53] a trillion parameters making it over
[15:55] 10,000 times larger than alexnet this
[15:59] mindboggling scale is the Hallmark of
[16:02] this third wave of AI we find ourselves
[16:04] in today driving both their performance
[16:06] and the fundamental difficulty in
[16:08] understanding how these models are able
[16:09] to do what they do it's amazing that we
[16:12] can figure out that Alex net learns
[16:14] representations of faces and that large
[16:16] language models learn representations of
[16:18] Concepts like the Golden Gate Bridge but
[16:20] there are many many more Concepts these
[16:23] models learn that we don't even have
[16:24] words for Activation atlases are
[16:27] beautiful and fascinating but very
[16:29] low-dimensional projections of very high
[16:31] dimensional spaces where our spatial
[16:33] reasoning abilities often fall apart
[16:36] it's notoriously difficult to predict
[16:38] where AI will go next almost no one
[16:42] expected the neural networks of the 80s
[16:43] and 90s scaled up by three or four
[16:45] orders of magnitude to yield alexnet and
[16:48] it was almost impossible to predict that
[16:50] a generalization of the compute blocks
[16:52] in alexnet scaled up by forers of
[16:54] magnitude would yield chat GPT maybe the
[16:57] next AI breakthrough is just another
[16:59] three to four ERS of magnitude of scale
[17:01] away or maybe some mostly forgotten
[17:04] approach to AI will resurface as Alex
[17:06] net did in 2012 we'll have to wait and
[17:10] see are you mad that I called the blocks
[17:12] of compute
[17:14] [Music]
[17:17] dumb not at
[17:19] all describing the compute blocks as
[17:21] dumb highlights the impressive nature of
[17:24] how simple operations can combine to
[17:25] produce intelligent
[17:27] Behavior it's a great way to emphasize
[17:29] the power of the underlying algorithms
[17:31] and training data