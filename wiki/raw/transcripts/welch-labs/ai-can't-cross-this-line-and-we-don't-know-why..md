---
source_url: https://www.youtube.com/watch?v=5eqRuVp65eY
ingested: 2026-07-09
video_id: 5eqRuVp65eY
title: AI can't cross this line and we don't know why.
series: None
---

[00:00] AI models can't cross this boundary and
[00:02] we don't know why as we train an AI
[00:05] model its error rate generally drops off
[00:07] quickly and then levels off if we train
[00:09] a larger model it will achieve a lower
[00:11] error rate but requires more compute
[00:14] scaling to larger and larger models we
[00:16] end up with a family of Curves like this
[00:19] switching our axis to logarithmic scales
[00:21] a clear Trend emerges where no model can
[00:24] cross this line known as the compute
[00:26] optimal or compute efficient Frontier
[00:29] this trend is one of three three neural
[00:30] scaling laws that have been broadly
[00:32] observed error rate scales in a very
[00:34] similar way with compute model size and
[00:37] data set size and remarkably doesn't
[00:39] depend much on model architecture or
[00:41] other algorithmic details as long as
[00:44] reasonably good choices are made the
[00:46] interesting question from here is have
[00:48] we discovered some fundamental law of
[00:50] nature like an ideal gas law for
[00:52] building intelligent systems or is this
[00:55] transist result of the specific neural
[00:57] network driven approach to AI that we're
[00:59] taking right now now how powerful can
[01:01] these models become if we continue
[01:03] increasing the amount of data model
[01:05] sizing compute can we drive errors to
[01:08] zero or will performance level off why
[01:11] are data model size and compute the
[01:13] fundamental limits of the systems we're
[01:15] building and why are they connected to
[01:17] model performance in such a simple
[01:19] way 2020 was a watershed year for open
[01:22] AI in January the team released this
[01:25] paper where they showed very clear
[01:27] performance Trends across a broad range
[01:29] of scales for language models the team
[01:31] fit a power law equation to each set of
[01:34] results giving a precise estimate for
[01:36] how performance scales with compute data
[01:38] set size and model size on logarithmic
[01:40] plots these power law equations show up
[01:42] as straight lines and the slope of each
[01:45] line is equal to the exponent of the fit
[01:47] equation larger exponents make for
[01:49] steeper lines and more rapid performance
[01:51] improvements the team observed no signs
[01:54] of deviation from these Trends on the
[01:56] upper end foreshadowing open AI strategy
[01:58] for the year the largest model the team
[02:01] tested at the time had 1.5 billion
[02:03] learnable parameters and required around
[02:05] 10 petaflop days of compute to train a
[02:08] pedop flop day is the number of
[02:10] computations a system capable of one
[02:11] quadrillion floating Point operations a
[02:13] second can perform in a day the
[02:15] top-of-the-line gpus at the time the
[02:17] Nvidia V100 is capable of around 30 Tera
[02:21] flops so a system with 33 of these
[02:23] $10,000 gpus would deliver around a
[02:26] pedop flop of compute that summer the
[02:28] team's empirically predicted game would
[02:30] be realized with the release of GPT 3
[02:33] the open AI team had placed a massive
[02:35] beted on scale partnering with Microsoft
[02:37] on a huge supercomputer equipped with
[02:39] not 33 but 10,000 V100 gpus and training
[02:44] the absolutely massive 175 billion
[02:46] parameter gpt3 model using 3,640 pedop
[02:50] flop days of compute gpt3 performance
[02:52] followed the trend line predicted in
[02:54] January remarkably well but also didn't
[02:56] flatten out indicating that even larger
[02:59] models would further improve performance
[03:02] if the massive gpt3 hadn't reached the
[03:04] limits of neural scaling where were they
[03:07] is it possible to drive error rates to
[03:08] zero given sufficient compute data and
[03:10] model size in an October publication the
[03:13] open AI team took a deeper look at
[03:15] scaling the team found the same Clear
[03:18] scaling laws across a range of problems
[03:20] including image and video modeling they
[03:23] also found that on a number of these
[03:24] other problems the scaling Trends did
[03:26] eventually flatten out before reaching
[03:28] zero error this makes sense if we
[03:30] consider exactly what these error rates
[03:32] are measuring large language models like
[03:35] gpt3 are Auto regressive they are
[03:37] trained to predict the next word or word
[03:39] fragment in sequences of text as a
[03:41] function of the words that come before
[03:44] these predictions generally take the
[03:45] form of vectors of probabilities so for
[03:48] a given sequence of input words a
[03:50] language model will output a vector of
[03:51] values between 0o and one where each
[03:54] entry corresponds to the probability of
[03:56] a specific word in its
[03:58] vocabulary these vectors are typically
[04:00] normalized using a soft Max operation
[04:03] which ensures that all the probabilities
[04:04] add up to one gpt3 has vocabulary size
[04:08] at
[04:09] 50257 so if we input a sequence of text
[04:12] like Einstein's first name is the model
[04:15] will return a vector of length
[04:17] 50257 and we expect this Vector to be
[04:19] close to zero everywhere except at the
[04:22] index that corresponds to the word
[04:23] Albert this is index
[04:25] 42590 in case you're wondering during
[04:28] training we know what the next word is
[04:30] in the text that we're training on so we
[04:32] can compute an error or loss value that
[04:35] measures how well our model is doing
[04:36] relative to what we know the word it
[04:38] should be this loss value is incredibly
[04:40] important because it guides optimization
[04:43] or learning of the model's parameters
[04:45] all those pedoph flops of training are
[04:47] performed to bring this loss number down
[04:49] there's a bunch of different ways we
[04:51] could measure the loss in our Ein sign
[04:53] example we know that the correct output
[04:55] Vector should have a one at the index of
[04:57] 42590
[04:59] so we could Define our loss value as 1
[05:02] minus the probability returned by the
[05:03] model at this index if our model was
[05:06] 100% confident the answer was Albert and
[05:08] returned a one our loss would be zero
[05:11] which makes sense if our model returned
[05:13] a value of 0.9 our loss would be 0.1 for
[05:17] this example if the model returned a
[05:19] value of 0.8 our loss would be 0.2 and
[05:22] so on this formulation is equivalent to
[05:24] what's called an L1 loss which works
[05:26] well in a number of machine learning
[05:28] problems however in practice we found
[05:30] that models often perform better when
[05:32] using a different loss function
[05:33] formulation called the cross entropy the
[05:36] theoretical motivation of cross entropy
[05:38] is a bit complicated but the
[05:39] implementation is simple all we have to
[05:42] do is take the negative natural
[05:43] logarithm of the probability output of
[05:46] the model at the index of the correct
[05:48] answer so to compute our loss in the
[05:50] Einstein example we just take the
[05:52] negative log of the probability output
[05:54] by the model at index
[05:57] 42590 so if our model is 100% confident
[06:00] then our cross entropy loss equals the
[06:02] minus natural logarithm of one or zero
[06:05] which makes sense and matches our L1
[06:07] loss if our model is 90% confident of
[06:10] the correct answer our cross entropy
[06:12] loss equals the negative natural log of
[06:14] 0.9 or about 0.1 again close to our L1
[06:18] loss plotting our cross entropy loss as
[06:20] a function of the model's output
[06:22] probability we see that loss grows
[06:24] slowly and then shoots up as the model's
[06:26] probability of the correct word
[06:27] approaches zero this means that if the
[06:29] model's confidence in the correct answer
[06:31] is very low the cross entropy loss will
[06:33] be very high the model performance shown
[06:35] on the Y AIS and all the scaling figures
[06:38] we've looked at so far is this cross
[06:40] entropy loss averaged over the examples
[06:42] in the model's test set the more
[06:44] confident the model is about the correct
[06:46] next word in the test set the closer to
[06:48] zero the average cross entropy becomes
[06:50] now the reason it makes sense that the
[06:52] open AI team s some of their loss curves
[06:54] level off instead of reaching zero is
[06:57] because predicting the next element in
[06:58] sequences like this generally does not
[07:00] have a single correct answer the
[07:03] sequence Einstein's first name is has a
[07:05] very unambiguous next word but this is
[07:08] not the case for most text a large part
[07:10] of gpt3 is training data comes from text
[07:12] scraped from the internet if we search
[07:14] for a phrase like a neural network is a
[07:17] we'll find many different next words
[07:19] from various sources none of these words
[07:21] are wrong there's just many different
[07:23] ways to explain what a neural network is
[07:26] this fundamental uncertainty is called
[07:27] the entropy of natural language
[07:30] the best we can hope for our language
[07:31] models is that they give High
[07:33] probabilities to a realistic set of next
[07:35] word choices and remarkably this is what
[07:38] large language models do for example
[07:40] here's the top five choices for meta's
[07:42] llama
[07:43] model so we can never drive the cross
[07:46] entropy loss to zero but how close can
[07:48] we get can we compute or estimate the
[07:51] value of the entropy of natural language
[07:54] by fitting power law models to their
[07:55] loss curves that include a constant
[07:57] irreducible error term the the opening I
[08:00] team was able to estimate the natural
[08:01] entropy and low resolution images videos
[08:04] and other data sources for each problem
[08:07] they estimated the natural entropy of
[08:08] the data in two ways once by looking at
[08:11] where the model size scaling curve
[08:12] levels off and again by looking at where
[08:14] the compute curve levels off and they
[08:17] found that these separate estiment
[08:18] agreed very well know that the scaling
[08:20] power laws still work in these cases but
[08:23] by adding this constant term our trend
[08:25] line or Frontier on a log log plot is no
[08:28] longer a straight line interestingly the
[08:30] team was not able to detect any
[08:32] flattening out of performance on
[08:33] language data however noting that
[08:36] unfortunately even with data from the
[08:38] largest language models we cannot yet
[08:40] obtain a meaningful estimate for the
[08:42] entropy of natural language 18 months
[08:45] later the Google deepmind team published
[08:46] a set of massive neural scaling
[08:48] experiments where they did observe some
[08:50] curvature in the compute efficient
[08:52] Frontier on natural language data they
[08:55] used their results to fit a neural
[08:56] scaling law that broke the overall loss
[08:59] into into three terms one that scales
[09:01] with model size one with data set size
[09:03] and finally an irreducible term that
[09:06] represents the entropy of natural text
[09:08] these empirical results imply that even
[09:10] an infinitely large model with infinite
[09:13] data cannot have an average crossentropy
[09:15] loss on the massive Text data set of
[09:17] less than
[09:18] 1.69 a year later on Pi Day 2023 the
[09:22] open AI team released GPT
[09:25] 4 despite running for a 100 Pages the
[09:28] gp4 technical report contains almost no
[09:31] technical information about the model
[09:32] itself the open aai team did not share
[09:35] this information citing the competitive
[09:37] landscape and safety
[09:39] implications however the paper does
[09:40] include two scaling plots the cost of
[09:43] training GPT 4 is enormous reportedly
[09:46] well over $100
[09:47] million before making this massive
[09:49] investment the team predicted how
[09:51] performance would scale using the same
[09:53] simple power laws fitting this curve to
[09:55] the results of much smaller experiments
[09:58] note that this uses a linear and not
[10:00] logarithmic y-axis scale exaggerating
[10:03] the curvature of the scaling if we map
[10:06] this curve to a logarithmic scale we see
[10:08] some curvature but overall a close match
[10:11] to the other scaling plots we've seen
[10:13] what's incredible here is how accurately
[10:15] the open a team was able to predict the
[10:17] performance of GPT 4 even at this
[10:19] massive scale while gpt3 training
[10:22] required an already enormous 3,640 peda
[10:25] flop days some leaked information on GPT
[10:28] 4 training puts the training compute at
[10:30] over 200,000 peda flop days reportedly
[10:34] requiring 25,000 Nvidia a100 gpus
[10:37] running for over 3 months all of this
[10:40] means that neural scaling laws appear to
[10:42] hold across an incredible range of
[10:44] scales something like 13 orders of
[10:46] magnitude from 10 to the minus8 pedop
[10:49] Flop days reported in open ai's first
[10:51] 2020 publication to the leaked value of
[10:53] over 200,000 pedop flop days for
[10:55] training GPT 4 this brings us back to
[10:58] the question why does AI model
[11:00] performance follow such simple laws in
[11:02] the first place why are data model
[11:05] sizing compute the fundamental limits of
[11:07] the systems we building and why are they
[11:09] connected to model performance in such a
[11:10] simple way the Deep learning theory we
[11:13] need to answer questions like this is
[11:15] generally far behind deep learning
[11:17] practice but some recent work does make
[11:19] a compelling case for why model
[11:21] performance scales following a power law
[11:24] by arguing that deep learning models
[11:25] effectively use data to resolve a
[11:27] high-dimensional data manifold
[11:30] really getting your head around these
[11:31] theories can be tricky it's often best
[11:33] to build up intuition step by step to
[11:36] build up your intuition on llms and a
[11:38] huge range of other topics check out
[11:40] this video sponsor brilliant when trying
[11:42] to get my own head around theories like
[11:44] neural scaling I start with the papers
[11:46] but this only gets me so far I almost
[11:49] always code something up so I can
[11:51] experiment and see what's really going
[11:52] on brilliant does this for you in an
[11:55] amazing way allowing you to jump right
[11:57] to the powerful learning by doing part
[12:00] they have thousands of interactive
[12:01] lessons covering math programming data
[12:03] analysis and AI brilliant helps you
[12:05] build up your intuition through solving
[12:07] real problems this is such a critical
[12:10] piece of learning for me a few minutes
[12:12] from now you'll see an animation of a
[12:13] neural network learning a
[12:14] low-dimensional representation of the
[12:16] Imus data set solving small versions of
[12:19] big problems like this is an amazing
[12:21] intuition builder for me brilliant
[12:23] packages up this style of learning into
[12:25] a format you can make progress on in
[12:26] just minutes a day you'll be amazed at
[12:28] the progress you can stack up with
[12:30] consistent effort brilliant has an
[12:32] entire course on large language models
[12:34] including lessons that take you deeper
[12:36] into topics we covered earlier
[12:38] predicting the next word and calculating
[12:39] word probabilities to try the brilliant
[12:42] llm course and everything else they have
[12:44] to offer for free for 30 days visit
[12:46] brilliant.org Welch laabs or click the
[12:49] link in this video's description using
[12:51] this link you'll also get 20% off an
[12:53] annual premium subscription to brilliant
[12:56] big thank you to brilliant for
[12:57] sponsoring this video now back to neural
[12:59] scaling there's this idea in machine
[13:01] learning that the data sets our models
[13:03] learn from exist on manifolds in
[13:06] high-dimensional space we can think of
[13:08] natural data like images or text as
[13:11] points in this High dimensional space in
[13:13] the Imus data set of hand written images
[13:15] for example each image is composed of a
[13:18] grid of 28x 28 pixels and the intensity
[13:21] of each pixel is stored as a number
[13:22] between zero and one if we imagine that
[13:25] our images only have two pixels for a
[13:27] moment we can visualize these two pixel
[13:29] images as points in 2D space where the
[13:32] intensity value of the first pixel is
[13:33] the x coordinate and the intensity value
[13:35] of the second pixel is the y coordinate
[13:38] an image made of two white pixels would
[13:40] fall at 0 0 in our 2D space an image
[13:43] with a black pixel in the first position
[13:45] and a white pixel in the second position
[13:47] would fall at one Z and an image with a
[13:49] gray value of 0.4 for both pixels would
[13:52] fall at 0.4 comma 0.4 and so on if our
[13:55] images had three pixels instead of two
[13:58] the same approach still works just in
[14:00] three dimensions scaling up to our 28x
[14:03] 28 mnist images our images become points
[14:06] in 784 dimensional space the vast
[14:09] majority of points in this High
[14:10] dimensional space are not handwritten
[14:12] digits we can see this by randomly
[14:15] choosing points in the space and
[14:16] displaying them as images these almost
[14:19] always just look like random noise you
[14:21] would have to get really really really
[14:23] lucky to randomly sample a handwritten
[14:25] digit this sparsity suggests that there
[14:27] may be some lower dimensional shape
[14:29] embedded in this 784 dimensional space
[14:33] where every point in or on this shape is
[14:35] a valid handwritten digit going back to
[14:37] our toy three pixel images for a moment
[14:40] if we learned that our third pixel
[14:41] intensity value let's call it X3 was
[14:44] always just equal to 1 plus the cosine
[14:47] of our second pixel value X2 all of our
[14:49] three pixel images would lie on the
[14:51] curved surface in our 3D space defined
[14:53] by X3 = 1 + the cosine of X2 this
[14:57] surface is two-dimensional we can
[14:59] capture the location of our images in 3D
[15:01] space just using X1 and X2 we no longer
[15:04] need X3 we can think of a neural network
[15:06] that learns to classify imist as working
[15:08] in a similar way in this network
[15:11] architecture for example our second to
[15:13] last layer has 16 neurons meaning that
[15:15] the network has mapped the 784
[15:17] dimensional input space to a much lower
[15:20] 16-dimensional
[15:21] space very much like our 1 plus cosine
[15:23] function mapped our three-dimensional
[15:25] space to a lower two-dimensional space
[15:28] where the manifold hypothesis gets
[15:29] really interesting is that the manifold
[15:31] is not just a lower dimensional
[15:33] representation of the data the geometry
[15:35] of the manifold often encodes
[15:37] information about the data if we take
[15:40] the 16-dimensional representation of the
[15:42] Imus data set learned by our neural
[15:44] network we can get a sense for its
[15:46] geometry by projecting from 16
[15:47] Dimensions down to two using a technique
[15:50] like umap which attempts to preserve the
[15:52] structure of the higher dimensional
[15:54] space coloring each point using the
[15:56] number that the image corresponds to we
[15:59] can see that as the network trains
[16:01] effectively learning the shape of the
[16:02] manifold instances of the same digit are
[16:04] grouped together into little
[16:05] neighborhoods on the manifold this is a
[16:08] common phenomena across many machine
[16:10] learning problems images showing similar
[16:13] objects or text referring to similar
[16:14] Concepts end up close to each other on
[16:16] the Learned manifold one way to make
[16:19] sense of what deep learning models are
[16:20] doing is mapping high-dimensional input
[16:23] spaces to lower dimensional manifolds
[16:25] where the position of data on the
[16:27] manifold is Meaningful
[16:29] now what does the manifold hypothesis
[16:31] have to do with neural scaling laws
[16:33] let's consider the neural scaling law
[16:35] that links the size of the training data
[16:37] set with the performance of the model
[16:39] measured as the cross entropy loss on
[16:41] the test set if the manifold hypothesis
[16:43] is true then our trading data are points
[16:46] on some manifold in higher dimensional
[16:48] space and our model attempts to learn
[16:50] the shape of this manifold the density
[16:52] of our training points on our manifold
[16:54] depends on how much data we have but
[16:56] also on the dimension of the manifold in
[16:59] onedimensional space if we have D
[17:01] training data points and the overall
[17:03] length of our manifold is L we can
[17:05] compute the average distance between our
[17:07] training points s by dividing L by D
[17:10] note that instead of thinking about the
[17:12] distance between our training points
[17:13] directly it's easier when we get to
[17:15] higher Dimensions to think about a
[17:16] little neighborhood around each point of
[17:18] size as and since these little
[17:19] neighborhoods bump up against each other
[17:22] the distance between our data points is
[17:23] still just s moving to two Dimensions
[17:25] we're now effectively filling up an L by
[17:27] L square with small squares of side
[17:30] length s centered around each training
[17:31] point the total area of our large Square
[17:34] l^ s must equal our number of data
[17:36] points D * the area of each little
[17:39] square so D * s^ 2 rearranging and
[17:42] solving we can show that s is equal to l
[17:45] * D Theus 12 moving to three dimensions
[17:49] we're now packing an L by L by L cube
[17:51] with d cubes of side length s equating
[17:54] the volumes of our D small cubes and our
[17:56] large Cube we can show that s is equ Al
[17:59] to L * D Theus 1/3 so as we move to
[18:02] higher Dimensions the average distance
[18:04] between points scales as the amount of
[18:06] data we have to the power of minus1 over
[18:09] the dimension of the
[18:11] manifold now the reason we care about
[18:13] the density of the training points on
[18:14] our manifold is because when a testing
[18:17] Point comes along its error will be
[18:19] bounded by a function of its distance to
[18:21] the nearest Training point if we assume
[18:24] that our model is powerful enough to
[18:25] perfectly fit the training data then our
[18:28] learned man manold will match the true
[18:30] data manifold exactly at our training
[18:32] points a deep naral network using Ru
[18:34] activation functions is able to linearly
[18:37] interpolate between these training
[18:38] points to make predictions if we assume
[18:41] that our manifolds are smooth then we
[18:43] can use a tailor expansion to show that
[18:45] our error will scale as the distance
[18:47] between our nearest Training and testing
[18:48] points squared we establish that our
[18:51] average distance between training points
[18:52] scales as the size of our data set D to
[18:55] the power of minus1 over the dimension
[18:56] of our manifold so we can Square this
[18:59] term to get an estimate for how our
[19:01] error scales with data set size and
[19:03] compute D the^ of minus 2 over the
[19:06] manifold Dimension finally remember that
[19:08] our models are using a cross entropy
[19:10] loss function but thus far in our
[19:12] manifold analysis we've only considered
[19:14] the distance between the predicted and
[19:16] True Value this is equivalent to the L1
[19:18] loss value we considered earlier
[19:20] applying a similar tailor expansion to
[19:22] the Cross entropy function we can show
[19:24] that the cross entropy loss Will scale
[19:26] as the distance between the predicted
[19:28] and true value squared so for our final
[19:31] theoretical result we expect the cross
[19:33] entropy loss to scal as the data set
[19:35] size d to the power of Min -2 over the
[19:37] manifold Dimension squared so D ^ of-4
[19:41] over Little D this represents the worst
[19:44] case error making this an upper bound so
[19:46] we expect cross entropy loss to scale
[19:48] proportionally or better than this term
[19:51] the team that developed this Theory
[19:52] calls this resolution limited scaling
[19:55] because more data is allowing the model
[19:57] to better resolve the data manifold
[20:00] interestingly when considering the
[20:01] relationship between model size and lost
[20:04] the theory predicts the same fourth
[20:05] power relationship in this case the idea
[20:08] is that the additional model parameters
[20:10] are allowing the model to fit the data
[20:12] manifold at higher
[20:14] resolution so how does this theoretical
[20:16] result stack up against observation both
[20:19] the open aai and Google deepmind teams
[20:21] published their fit scaling values do
[20:24] these match what theory predicts in the
[20:27] January 2020 open AI paper the team
[20:30] observed the cross entropy loss scaling
[20:32] as the size of the data set to the power
[20:34] of minus
[20:36] 0.095 they refer to this value as Alpha
[20:39] subd if the theory is correct then Alpha
[20:42] subd should be greater than or equal to
[20:43] 4 over the intrinsic dimension of the
[20:46] data this final step is tricky since it
[20:49] requires estimating the dimension of the
[20:51] data manifold also known as the
[20:53] intrinsic dimension of natural language
[20:56] the team started with smaller problems
[20:58] where the intrinsic Dimension is known
[21:00] or can be estimated well they found
[21:02] quite good agreement between theoretical
[21:04] and experimental scaling parameters in
[21:06] cases where synthetic training data of
[21:07] known intrinsic Dimension is created by
[21:09] a teacher model and learned by a student
[21:11] model they were also able to show that
[21:14] the minus 4 overd prediction holds up
[21:15] well with smaller scale image data sets
[21:18] including
[21:19] imist finally turning to language if we
[21:22] plug in the observed scaling exponent of
[21:24] minus
[21:25] 0.095 we can compute that the intrinsic
[21:27] dimension of natural language should be
[21:29] something like 42 the team tested this
[21:32] result by estimating the intrinsic
[21:34] dimension of the manifolds learned by a
[21:36] language model and found the intrinsic
[21:37] Dimension to be significantly higher on
[21:39] the order of 100 note that the
[21:42] inequality from Theory still holds but
[21:44] we don't see nearly the same agreement
[21:46] that was observed in synthetic and
[21:48] smaller data sets what we're left with
[21:50] then is a compelling Theory with some
[21:52] real predictive power but definitely no
[21:54] unified theory of AI just yet we've seen
[21:58] some astounding AI progress in The Last
[22:00] 5 Years From open ai's first scaling
[22:03] paper in early 2020 to the release of
[22:05] GPT 4 in 2023 neural scaling laws showed
[22:09] us a path to better and better
[22:11] performance it's important to note here
[22:13] that while scaling laws have been
[22:15] incredibly predictive of next word
[22:16] prediction performance predicting the
[22:19] presence of specific model behaviors has
[22:21] remained more elusive abilities on tasks
[22:23] like word unscrambling arithmetic and
[22:25] multi-step reasoning seem to just pop
[22:27] into existence at various scales it's
[22:30] incredible to see how far our neural
[22:32] network powered approach has taken us
[22:34] and we of course don't know how far it
[22:36] can go many of the authors of the papers
[22:39] we've covered here have backgrounds in
[22:40] physics and you can feel in their
[22:43] approaches in language that they're on
[22:44] the hunt for unifying principles it's
[22:47] exciting to see this mindset applied to
[22:48] AI neural scaling laws are a powerful
[22:51] example of unification in AI delivering
[22:54] astoundingly accurate and useful
[22:56] empirical results and tantalizing Clues
[22:59] to a unified theory of scaling for
[23:01] intelligent systems it will be
[23:03] fascinating to see where scaling laws
[23:05] and other theories can take us in the
[23:07] next 5 years and to see if we can figure
[23:10] out if AI really can't cross this
[23:15] line if you enjoy Welch lab's videos I
[23:18] really think you'll like my book on
[23:19] imaginary numbers it's coming out later
[23:22] this year way back in 2016 I made a
[23:24] massive 13-part YouTube series on
[23:26] imaginary numbers it's such an
[23:28] incredible topic I released an early
[23:30] version of this book back then and I'm
[23:32] now in the process of revising
[23:34] correcting and significantly expanding
[23:35] it my goal is to create the best book
[23:38] out there on imaginary numbers
[23:40] highquality hardcover printed books will
[23:42] start shipping later this year you can
[23:44] pre-order a copy today at the link in
[23:46] the description below and your order
[23:47] includes a free PDF copy of the 2016
[23:50] version that you can download today I've
[23:52] also been working on some new poster
[23:54] designs I now have a dark mode version
[23:56] of my activation Atlas poster
[23:59] these are an incredible way to visualize
[24:01] the data manifolds learned by Vision
[24:03] models you'll find all of this and more
[24:05] at the Welch Labs store