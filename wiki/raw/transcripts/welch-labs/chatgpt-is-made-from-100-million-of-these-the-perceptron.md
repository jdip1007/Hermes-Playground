---
source_url: https://www.youtube.com/watch?v=l-9ALe3U-Fg
ingested: 2026-07-09
video_id: l-9ALe3U-Fg
title: ChatGPT is made from 100 million of these [The Perceptron]
series: None
---

[00:00] this is a perceptron the machine shocked
[00:02] the world in the 1950s by learning to
[00:05] recognize patterns completely
[00:07] automatically and today the algorithm it
[00:09] implements has become the core building
[00:11] block of AI systems like chat GPT but
[00:13] why is this the atomic unit of the
[00:15] intelligent systems we have today the
[00:18] perceptron works by processing patterns
[00:20] we input using these switches like this
[00:22] t-shape switches in the up position
[00:24] output a positive voltage and switches
[00:26] in the down position output a negative
[00:28] voltage each switch is connected to an
[00:30] indicator LED and then to one of these
[00:32] dials rotating a dial multiplies the
[00:35] output of the switch by the number shown
[00:37] on the dial and the meter shows the
[00:39] result of adding the signals from all
[00:41] the dials together now is there a way to
[00:43] configure our dials such that the
[00:45] perceptron always outputs a positive
[00:48] signal for t-shapes while outputting a
[00:50] negative value for other types of shapes
[00:52] like this J shape note that our shapes
[00:55] won't be in the same position each time
[00:57] remarkably it turns out that if a
[00:59] configuration of that solves our problem
[01:01] exists there is a simple procedure we
[01:03] can follow that is guaranteed to find it
[01:05] every time starting with this t-shape
[01:08] our meter is showing a value close to
[01:09] zero but we want it to be positive in
[01:12] this case our procedure tells us to turn
[01:14] all the knobs that are switch on to the
[01:16] right by a constant value called The
[01:18] Learning rate and to turn all the knobs
[01:20] that are Switched Off to the left by the
[01:22] Learning rate our next pattern is a
[01:25] j-shape so we want our machine to Output
[01:27] a negative value however the current
[01:29] dial configuration outputs a positive
[01:31] value in this case our procedure tells
[01:33] us to turn down all the dials that are
[01:35] switched on and turn up all the dials
[01:37] that are Switched Off moving to our next
[01:40] pattern a shifted j-shape our perceptron
[01:43] again outputs a positive value instead
[01:45] of the desired negative value so we
[01:48] again turn down all the switches that
[01:49] are on and turn up all the switches that
[01:51] are off arriving at our fourth and final
[01:54] example the current configuration of
[01:56] dials outputs the correct positive value
[01:58] that we expect for a
[02:00] in this case our procedure tells us to
[02:02] leave our dials alone cycling back
[02:05] through our patterns we see that our
[02:06] machine has learned to correctly
[02:08] classify all four examples this
[02:10] procedure was discovered in 1957 by the
[02:13] psychologist Frank Rosen blot and is
[02:15] known as the perceptron learning rule
[02:18] Rosen blot unveiled the approach to the
[02:19] public in a press conference on July 7th
[02:22] 1958 the next day the New York Times
[02:25] reported that the machine was expected
[02:26] to be able to walk talk see write
[02:29] reproduce itself and be conscious of its
[02:31] own existence Rosen bl's perceptron is
[02:34] in some ways more sophisticated than our
[02:36] machine its input grid was 20x 20
[02:39] instead of 4x4 it had multiple
[02:41] artificial neurons instead of just one
[02:43] and it used motors to turn the dials so
[02:46] learning was entirely automatic but the
[02:48] learning algorithm and operating
[02:50] principles are the same rosenblatt's
[02:52] claims are grandiose but are slowly
[02:55] coming true and before his untimely
[02:57] death in 1971 Rosen blot was even
[03:00] working on multi-layer architectures
[03:02] that closely resemble modern neural
[03:04] networks but there was a problem with
[03:06] Rosen bl's design and in fact all neural
[03:09] networks from this era that nearly
[03:11] completely halted our modern neural
[03:13] network driven approach to
[03:15] AI building the perceptron machine for
[03:17] this video took quite a few early
[03:19] morning design and soldering sessions on
[03:22] projects like these I really like to
[03:23] have my morning routine dialed in and
[03:25] this video sponsor ag1 is a key part of
[03:28] my routine a couple of years ago I found
[03:30] myself feeling extra rundown and getting
[03:32] sick more often than usual so I decided
[03:35] to have some detailed blood testing done
[03:37] to see if anything was off my doctor
[03:40] found that my vitamin D levels were very
[03:42] low and after taking supplements for a
[03:44] couple of months I felt a huge
[03:46] difference this experience led me to
[03:48] have a broader look at how I could
[03:49] optimize my nutrition and ag1 has been a
[03:52] terrific tool for me I was able to
[03:54] replace a few separate supplements with
[03:56] a single serving of ag1 each morning the
[03:59] ingredient list is really impressive the
[04:01] biggest benefits I noticed when taking
[04:03] ag1 are improved energy and digestion I
[04:06] stopped my morning routine over the
[04:07] holidays leading me to forget to take
[04:09] ag1 and by the end of the break I found
[04:11] myself with less energy even though I
[04:13] was getting more sleep ag1 is research
[04:16] backed they use these cool machines for
[04:18] invitro studies that simulate the
[04:20] digestive tract allowing for very
[04:23] controlled study of a1's impact on the
[04:25] gut microbiome the ag1 team also conduct
[04:28] studies with human participants in a
[04:30] recent study 97% of participants
[04:32] reported feeling more energy after
[04:34] taking ag1 for one month you can get $20
[04:37] off your first subscription to ag1 by
[04:39] visiting drink a1.com Welch laabs or by
[04:43] clicking the link in the description
[04:45] below big thank you to ag1 for
[04:47] sponsoring this video now back to the
[04:50] perceptron we've seen that our
[04:52] perceptron machine can quickly learn to
[04:53] tell apart certain patterns but what
[04:56] exactly can the perceptron do and not do
[04:59] in 1962 Albert novakov proved
[05:02] mathematically that if a configuration
[05:04] of dials exists that cleanly separates a
[05:06] given set of examples the perceptron
[05:08] learning rule is guaranteed to find it
[05:11] but do cleanly separating configurations
[05:12] of dials exist for all types of input
[05:15] patterns to get to the bottom of this
[05:17] let's build an even simpler version of
[05:19] the perceptron with just two inputs we
[05:22] now have only four possible input
[05:24] patterns both switches off one or the
[05:27] other switch on or both switches on note
[05:30] that although we only have two inputs we
[05:32] have three dials the extra dial is
[05:34] called bias and is not connected to any
[05:36] of our switches but is effectively
[05:38] always switched on the bias dial allows
[05:41] us to directly add or subtract from the
[05:43] final value that goes to our meter
[05:45] regardless of the current switch
[05:46] configuration this is also why our full
[05:48] machine has 17 dials instead of 16 now
[05:52] let's see that we want our perceptor and
[05:53] to Output a positive value when either
[05:55] one or both switches are on and a
[05:57] negative value when both switches are
[05:59] off
[06:00] following our perceptron learning rule
[06:02] our machine is able to successfully
[06:04] learn these patterns in just three
[06:08] steps but what about other assignments
[06:10] for our examples what if we want the
[06:12] output to be positive when either one of
[06:14] our switches is on and negative when
[06:16] both switches are on or when both
[06:18] switches are off following our same
[06:20] perceptron learning rule we now get
[06:22] stuck in a loop where the machine never
[06:24] settles down on a viable
[06:26] solution why is the perceptron able to
[06:28] learn the first group of patterns but
[06:30] not the second we can make sense of
[06:33] what's going on visually by plotting
[06:34] each input configuration on a 2d grid
[06:37] where the x- axis represents our first
[06:39] input value and our y- axis represents
[06:41] our second input value a switch in the
[06:43] on position creates an input of plus one
[06:46] volt so the configuration with both
[06:48] switches on is represented by a point at
[06:50] 1 one on our grid an off switch
[06:53] represents an input of minus1 volt so
[06:55] the configuration with both switches off
[06:57] would show up at minus one minus one on
[06:58] our grid and configurations with one
[07:00] switch on show up at 1 minus one and
[07:03] minus one one now how does the
[07:05] mathematics of our perceptron show up on
[07:07] our 2D grid each dial in our machine is
[07:10] effectively multiplying each input value
[07:12] by a configurable weight so our
[07:14] machine's output is equal to the weight
[07:16] value of our first dial time X plus the
[07:19] weight value of our second dial time y
[07:21] plus the output of our bias dial which
[07:23] doesn't depend on X or Y we'll call this
[07:26] value B when our output value is greater
[07:28] than zero our perceptron will classify
[07:31] our input XY as positive now for what
[07:34] regions of our grid will the output of
[07:36] our perceptron be greater than zero
[07:39] setting our output greater to zero in
[07:41] our equation and solving for y we get an
[07:43] equation for a straight line with a
[07:45] slope of minus W1 over W2 and a y
[07:49] intercept of minus B over W2 so our
[07:52] perceptron will classify all points on
[07:54] our grid above this line as positive we
[07:57] can see this behavior in action on the
[07:58] first example we trained our perceptron
[08:00] on where we classified examples with
[08:03] either one or both of our switches on as
[08:05] positive on our grid these are the
[08:07] points - one one 1 one and 1 minus one
[08:11] as the perceptron learns and we update
[08:12] our weights our line moves and quickly
[08:15] lands in a configuration where all
[08:16] positive examples are on the positive
[08:18] side of our decision
[08:20] boundary now what about the example our
[08:22] perceptron failed to learn where we want
[08:24] the machine to classify configurations
[08:26] as positive where one but not both
[08:28] switches are on
[08:29] on our grid these configurations
[08:31] correspond to the points minus one one
[08:33] and 1 minus one watching our perceptron
[08:36] try to learn this pattern we can see our
[08:38] line jump around without being able to
[08:40] settle in a location that cleanly
[08:41] separates our examples this is because
[08:44] there's actually no way to use a single
[08:46] line to separate this pattern we'll
[08:48] always miss at least one example said
[08:51] differently our data is not linearly
[08:54] separable this example is known as the
[08:56] exclusive or problem because the mapping
[08:58] from inputs to outputs follows The
[09:00] Logical exclusive or function and is one
[09:03] of the simplest examples of a
[09:04] nonlinearly separable pattern this
[09:07] inability to learn a simple exclusive or
[09:09] function was a major criticism of Rosen
[09:11] blots perceptron and other early neural
[09:14] networks the example may feel a bit
[09:16] contrived but linear separability is a
[09:19] significant concern in real data in
[09:21] Rosen bl's 1958 press conference he
[09:24] showed an example of the perceptron
[09:26] learning to tell apart examples with
[09:27] markings on the left versus the right
[09:29] side side of an image these patterns are
[09:31] linearly separable however later that
[09:34] year in an interview with the New Yorker
[09:36] Rosen block claimed that the perceptron
[09:38] could tell apart images of cats and dogs
[09:41] he likely meant in principle but if we
[09:43] try this out in Python and images of cat
[09:44] and dog faces the perceptron learning
[09:46] rule is able to learn some basic
[09:48] patterns but is unstable and unable to
[09:51] beat around a 20% error rate meaning
[09:53] this cat and dog data set is not
[09:55] linearly separable now as Rosen blot
[09:57] himself pointed out there is a solution
[09:59] to the linear separability problem but
[10:02] it comes with a catch our perceptron
[10:04] machine implements a single artificial
[10:06] neuron which is limited to creating a
[10:08] single linear decision boundary to
[10:10] recognize patterns if we expand to a
[10:13] network of these artificial neurons we
[10:15] can combine multiple linear decision
[10:17] boundaries to learn more complex
[10:19] patterns it turns out that a very simple
[10:22] network with just three neurons across
[10:24] two layers can solve the exclusive or
[10:26] problem it works by creating two
[10:28] decision boundaries in the the first
[10:29] layer and then combining these
[10:31] boundaries in the second layer into a
[10:32] band on our grid that captures minus one
[10:35] one and 1us one while rejecting minus1
[10:38] minus one and 1 one however while it was
[10:40] well known in the 1960s that multi-layer
[10:43] neural networks could solve nonlinearly
[10:45] separable problems like this in
[10:46] principle no one could find a suitable
[10:48] algorithm for learning the weights the
[10:51] perceptron learning rule that works so
[10:52] well for a single neuron does not
[10:54] generalize to multi-layer networks and
[10:57] while it's easy to manually figure out
[10:58] weights to solve toy problems like
[11:00] exclusive ore real problems like telling
[11:02] apart cats and dogs with multi-layer
[11:04] neural networks requires a learning
[11:06] algorithm that can simultaneously update
[11:08] all neuron weights based on real data
[11:10] neural networks had hit a dead
[11:13] end in the mid 1960s two leaders in the
[11:16] AI field Marvin Minsky and Seymour
[11:18] papert began circulating pre-prints of a
[11:21] book they called
[11:22] perceptrons despite its title the book
[11:25] generally takes a negative view
[11:27] rigorously showing mathematically what
[11:29] perceptrons could not do the cover of
[11:32] the book shows two figures that the
[11:33] perceptron cannot tell apart these
[11:35] shapes look similar but have different
[11:37] connectivities the top shape is made
[11:39] from a single purple line and the bottom
[11:41] shape is made from two like the
[11:44] exclusive or problem Rosen blots
[11:46] perceptron cannot separate these
[11:47] patterns although modern neural networks
[11:50] can this apparent dead end contributed
[11:53] to the rise of completely different
[11:55] symbolic approaches to AI in the 1960s
[11:57] and70s and a dramatic decline in neural
[12:00] network research while Rosen blots
[12:03] percepton received most of the attention
[12:05] at the time there were a number of other
[12:07] groups working on systems of artificial
[12:09] neurons at Stanford Bernard wdr's group
[12:12] came Incredibly Close to solving the
[12:14] problem of training multi-layer neural
[12:15] networks and discovering our modern
[12:17] approach to AI on a Friday afternoon in
[12:20] the fall of 1959 woodro had his first
[12:23] meeting with a new graduate student Ted
[12:25] Hoff as widrow explained his group had
[12:28] been working on great rent based methods
[12:30] for learning the weights in artificial
[12:32] neurons the idea was that instead of
[12:34] following an ad hoc method like the
[12:36] perceptron learning rule it was possible
[12:38] to measure and minimize the machine's
[12:40] error mathematically in our first two
[12:43] input example where we wanted our percep
[12:45] Tron to learn to classify inputs where
[12:47] either one or both switches are on as
[12:49] positive we can measure our systems
[12:51] error by comparing the machines outputs
[12:53] to our Target outputs making a small
[12:56] notation change we can write the output
[12:58] y of our two input perceptron is w0 *
[13:02] our first input x0 plus W1 * our second
[13:05] input X1 + B taking our first input
[13:09] pattern with both switches off we want
[13:11] our perceptron to Output a value of y =
[13:14] minus1 if our dials are set to min-1 1
[13:17] and 1 for example this makes our output
[13:20] y hat equal to -1 * -1 plus -1 * POS 1 +
[13:24] 1 which equals POS 1 however our Target
[13:28] value is y = -1 so the difference or
[13:31] error between our Target and our output
[13:33] is y - y hat =
[13:35] -2 from here wdr's group would Square
[13:38] this error value this ensured the value
[13:41] was always positive and made it easier
[13:42] to minimize so our squared error is four
[13:46] now how does our squared error change as
[13:48] we turn our dials if we move our first
[13:51] dial from minus1 to minus 0.9 our
[13:54] overall output is now equal to positive
[13:57] 0.9 making our error 1.9 and our squared
[14:00] error
[14:01] 3.61 moving our w0 dial step by step and
[14:04] plotting the results we see that our
[14:06] error value makes a smooth parabolic
[14:08] shape reaching a minimum around w0
[14:11] equals 1 of course we want to find the
[14:13] best overall configuration of dials not
[14:15] just w0 if we vary w0 and W1 at the same
[14:20] time across a grid of values we end up
[14:22] with a nice Bowl shape where the best
[14:25] configuration of dials is located at the
[14:26] bottom of the bowl now as we move to
[14:29] machines with more dials it becomes
[14:31] intractable to test all configurations
[14:33] like this trying 10 values for each dial
[14:36] in our 16 input perceptron would require
[14:39] an enormous 10 to the 17th
[14:42] computations what's interesting here
[14:44] though is that we don't actually need to
[14:45] know what our entire eror landscape
[14:47] looks like to find the best solution
[14:50] given a starting configuration of dials
[14:52] if we just know which way is downhill on
[14:54] our error landscape also known as the
[14:56] gradient we can take incremental steps
[14:58] in this direction to reach the bottom of
[15:00] our
[15:01] bow up until this point wdr's group
[15:03] estimated the gradient numerically given
[15:06] our starting point of w0 = minus1 W1 = 1
[15:10] and Bal 1 they would compute the error
[15:12] at points in the neighborhood around
[15:14] each
[15:15] weight for the w0 weight for example we
[15:18] can compute the error at w0 = -1.1 and
[15:21] w0 = .9 to estimate the slope of the
[15:24] eror surface as widra walked through
[15:27] this mathematics at his office black
[15:29] with Hof they came across a powerful new
[15:31] approach that is incredibly close to how
[15:34] we train neural networks today but with
[15:36] one critical exception instead of
[15:38] estimating the gradient by Computing the
[15:40] error around each weight value What If
[15:43] instead we use calculus to take the
[15:44] derivative of the error function
[15:46] directly we can compute the partial
[15:48] derivative of our error equation with
[15:50] respect to our weight
[15:51] w0 by dropping down the power of two and
[15:54] following the chain rule giving -2 * y -
[15:58] Y2 times the derivative of y hat with
[16:00] respect to
[16:01] w0 writing out the full expression for y
[16:04] hat we can see that only the w0 x0 term
[16:07] depends on w0 treating the input x0 as a
[16:11] constant we can think of the system as a
[16:13] line with a slope of x0 so its
[16:16] derivative is just x0 we're left with a
[16:19] simple expression for de
[16:21] dw0 - 2 * y - y hat * x0 and we can
[16:26] compute similar expressions for dw1 and
[16:29] Deb putting these pieces together we're
[16:32] left with a simple equation that gives
[16:34] us the full gradient telling us exactly
[16:36] which way is downhill from a given
[16:38] starting point in our error landscape as
[16:41] WID would later explain you don't have
[16:43] to square anything or compute the actual
[16:45] error the power of that compared to
[16:47] earlier methods is just
[16:49] fantastic WID and Hoff had found a
[16:51] method that appeared to be incredibly
[16:53] efficient but would it actually work
[16:56] they had to find out they quickly worked
[16:59] out a circuit design but the university
[17:01] stock room was closed by the end of
[17:02] their Friday afternoon meeting and would
[17:04] not reopen until Monday the next morning
[17:06] wdro and Hoff rushed to an electronic
[17:08] supply store and over the weekend pieced
[17:11] together an artificial neuron circuit
[17:12] very similar to ours and by Sunday
[17:15] evening they were testing out their new
[17:16] learning algorithm on various input
[17:19] patterns the new algorithm worked
[17:21] incredibly well interestingly despite
[17:24] being derived completely differently
[17:26] wdro and Hoff's algorithm updates The
[17:28] Machine's weights and a very similar way
[17:30] to the perceptron learning rule the only
[17:32] real difference is that wdro and Hoff's
[17:34] algorithm which they later called LMS
[17:36] includes multiplying the weight update
[17:38] by the current error value so instead of
[17:41] turning the knobs by the same fixed
[17:43] learning rate at each step we turn them
[17:45] proportionally to the error between the
[17:47] Target and current output values the LMS
[17:51] algorithm can quickly solve the T&J
[17:53] classification problem we solved earlier
[17:55] with the perceptron learning rule it was
[17:57] later shown that although the elements
[17:58] algorithm is not guaranteed to find a
[18:00] solution if one exists it performs
[18:03] better in the all to Common case where
[18:05] our examples are not linearly separable
[18:08] now as impressive as the LMS algorithm
[18:10] is wdro and Hoff were not able to use it
[18:13] to address the core issue that halted
[18:15] 1960s neural network research as widra
[18:18] would later explain despite their best
[18:20] efforts they were never able to adapt
[18:22] LMS to train networks with multiple
[18:25] layers what's Wild here is how close the
[18:28] algorithm they wrote on the Blackboard
[18:29] that day is to the back propagation
[18:31] algorithm that we use to train modern
[18:33] systems like chat
[18:35] GPT returning to our simple three neuron
[18:37] two-layer network from earlier that
[18:39] could solve the nonlinearly separable
[18:41] exclusive or problem we can write a set
[18:44] of equations that map our inputs X to
[18:46] our outputs y hat just as woodro and
[18:48] Hoff did for a single neuron following
[18:51] woodro and Hoff's approach we can
[18:52] differentiate our error equation with
[18:54] respect to our weights and follow the
[18:56] chain rule however when we reach the
[18:59] boundary between our first and second
[19:00] layers our calculus hits a brick
[19:03] wall the artificial Neuron model that
[19:05] almost everyone used in the 50s and 60s
[19:08] originally developed by Walter pittz and
[19:10] Warren mullik in the 1940s assumes an
[19:13] All or Nothing output if the sum of our
[19:15] weights times our inputs is greater than
[19:17] zero our artificial neuron fires and
[19:20] outputs a one otherwise the neuron
[19:22] outputs a zero the slope of this binary
[19:25] step activation function is zero
[19:27] everywhere and undefined at the the
[19:29] origin so when we reach this function in
[19:31] our chain rule we get stuck the function
[19:34] effectively snaps our gradient to zero
[19:37] visually the binary step activation
[19:38] function turns our error landscape into
[19:40] flat plateaus and infinitely steep
[19:43] Cliffs here's our error surface is a
[19:45] function of the weights in our first
[19:47] layer these flat Landscapes give
[19:49] gradient methods like LMS no hope of
[19:51] incrementally working their way downhill
[19:54] the solution to this problem in
[19:55] hindsight is surprisingly simple all we
[19:58] have to to do is replace the All or
[20:00] Nothing step activation function with
[20:01] something less flat swapping our step
[20:04] activation function for a sigmoid
[20:06] function our lost landscape now looks
[20:08] like this we still have somewhat flat
[20:11] regions but there's enough of a slope in
[20:13] these regions to guide our solution
[20:15] downhill here's the continuation of the
[20:17] LMS algorithm extended through both
[20:19] layers solving the exclusive ore
[20:22] problem in 1986 27 years after woodro
[20:26] and Hoff discovered the LMS algorithm
[20:28] the David rumelhart Jeff Hinton and
[20:30] Ronald Williams published this paper
[20:32] where they present the modern back
[20:33] propagation algorithm that we use today
[20:36] their derivation cites the LMS algorithm
[20:38] which they call the Delta Rule and they
[20:40] proceed with deriving back propagation
[20:42] as a generalization of this rule using
[20:45] the chain Ru with sigmoid activation
[20:46] functions to continue the gradient
[20:48] computation started by wro and Hoff
[20:50] almost three decades
[20:52] before in 2020 open AI used back
[20:55] propagation to train gpt3 the largest
[20:58] neur Network ever created at the time
[21:00] with a staggering 175 billion learnable
[21:03] weights these weights are spread across
[21:05] 96 layers each made of two compute
[21:08] blocks the second compute Block in each
[21:11] layer is still called by the name Frank
[21:12] Rosen block gave it almost 70 years ago
[21:15] a multi-layer perceptron each
[21:17] multi-layer perceptron block in gpt3 has
[21:20] two layers just like our two-layer
[21:22] Network that solve the exclusive War
[21:23] problem but with way more neurons around
[21:26] 50,000 in the first layer and 12,000 in
[21:29] the second layer the first compute Block
[21:32] in each layer implements a relatively
[21:33] recent idea called attention and
[21:35] arguably still uses artificial neurons
[21:38] but in a more complex way one way to
[21:40] think about the attention block is as a
[21:42] specialized multi-layer perceptron where
[21:44] the weights are controlled by other
[21:46] perceptrons allowing the data itself to
[21:48] control the weights as it moves through
[21:50] the model each attention Block in gpt3
[21:53] effectively uses around 50,000 neurons
[21:56] this makes for around 10 million
[21:58] artificial neurons across gpt3 is 96
[22:01] layers so we would need 10 million of
[22:03] our perceptron machines each with over
[22:05] 10,000 dials to implement
[22:08] gpt3 today gpt3 fits on around 10
[22:12] gpus GPT 4 is reportedly around 10 times
[22:15] larger than gpt3 bringing our neuron
[22:17] count to Something in the neighborhood
[22:19] of 100 million like our simple
[22:21] perceptron machine GPT 4 is in many ways
[22:24] a pattern recognizer its enormous
[22:27] network of neurons allows it to learn
[22:28] very complex patterns in language and
[22:31] use these patterns to predict what text
[22:33] should come next it's incredible that
[22:36] this Atomic unit the perceptron
[22:38] connected in giant networks and trained
[22:40] with an extension of the LMS algorithm
[22:43] would result in the most intelligent
[22:44] systems we've been able to build so far
[22:47] it's been almost 70 years now since
[22:49] Frank rosenblau claimed that the
[22:51] perceptron would be able to walk talk
[22:53] see write reproduce itself and be
[22:55] conscious of its own existence he
[22:58] clearly was missing some key details but
[23:00] time has only proven Rosen blot more
[23:03] right about what the humble perceptron
[23:04] can do we'll have to wait and see if he
[23:07] was right about
[23:11] everything big thanks to everyone who
[23:13] bought an imaginary numbers book the
[23:15] first print run totally sold out but the
[23:18] second print run just came in and is
[23:20] available to order today the book
[23:22] follows my imaginary number series
[23:24] including remon surfaces and ends with
[23:27] new chapters on Oilers form and
[23:28] Schrodinger's equation these chapters
[23:31] were a lot of fun to put together I'm
[23:33] really happy with how the figures and
[23:35] type setting came out the book is
[23:37] printed on high quality heavyweight
[23:38] paper with great detail and color
[23:40] reproduction whether you're an expert
[23:42] looking for a different angle on a topic
[23:44] you know well or just picking this stuff
[23:46] up for school work or fun I really think
[23:49] you'll enjoy the book imaginary numbers
[23:51] are such a deep and beautiful topic get
[23:53] your book today at Welch labs.com
[23:55] resources
[23:59] come