---
source_url: https://www.youtube.com/watch?v=qx7hirqgfuU
ingested: 2026-07-08
video_id: qx7hirqgfuU
title: Why Deep Learning Works Unreasonably Well [How Models Learn Part 3]
series: How Models Learn
---

[00:00] In 1989, George Sabeno proved what's now known as the universal approximation
[00:05] theorem. If we take some complex function, for example, this really complicated border in the town of Barlay
[00:11] Hertok, these parts of the map are in Belgium and these parts are in the Netherlands. The universal approximation
[00:17] theorem guarantees that there exists a two-layer neural network that can fit this border as precisely as we want. A
[00:25] nice way to get a feel for this result is to see what a two-layer network like this does. geometrically.
[00:31] Most modern neural networks use some version of rectified linear activation functions. Visually, this means that
[00:37] each neuron in the first layer of our network folds up a copy of our map along a single fold line where the location of
[00:43] the fold line is controlled by the neurons learned weights. From here, our first neuron in our second layer takes
[00:50] in these bent planes and multiplies their heights by another learned weight value, which geometrically further bends
[00:56] up or down the folded parts of our planes and flips over our folded region when that neuron's weight value is
[01:02] negative. These three bent planes are then added together by our neuron, resulting in a surface like this. Our
[01:10] three-fold lines from our first layer now divide up our map into these five regions that each become different
[01:15] planes in our second layer surface. This surface shows the output of our first neuron in our second layer. The second
[01:22] neuron in our second layer flips, scales, and combines our first planes using different learned parameters,
[01:28] resulting in this surface that again uses the same five regions of our map, but at different heights.
[01:34] The height of the surface formed by our first neuron corresponds to the model's confidence in a certain part of the map
[01:40] being in the Netherlands. And the height of the second neuron surface corresponds to the model's confidence in Belgium.
[01:47] Coloring our Netherlands surface blue and our Belgium surface yellow. And bringing these surfaces together onto
[01:53] the same axis, the intersection of our surfaces shows us where our model is equally confident in both countries.
[02:00] This is the model's learn decision boundary which gives us a basic border
[02:05] separating the core Belgium region from the surrounding Netherlands region. Now the universal approximation theorem
[02:11] tells us that if we just keep adding neurons to our first layer, eventually we'll land on an architecture capable of
[02:17] representing our full border. Training a network with eight neurons in its first layer, we get this set of eight folds
[02:25] leading to this surface for our first output neuron and this surface for our second output neuron. Bringing these new
[02:31] surfaces onto the same axis, we see these new more complex intersection lines leading to this more detailed
[02:37] final border that begins to break our map into separate regions. Here's the surfaces and border for a
[02:44] larger model with 16 neurons. Here's a 32 neuron model. Here's 64. And here's
[02:50] 128. It starts to become difficult to see how our surfaces are intersecting exactly
[02:56] with this many fold lines. Let's flatten out our surfaces to make it easier to see how the model uses all its different
[03:02] fold lines to fit our border. Doubling our neuron count again to 256.
[03:07] Here's how our neurons divide up our map. And here's the final decision boundary. Here's 512 neurons. And here
[03:13] is 1,024. We're getting closer to our true border, but we're still missing a number of
[03:20] parts of the town. And we've reached a point where I can't actually render any more polygons, but we can still render
[03:26] our decision boundary. Here's the border we get with a 10,000 neuron model. And
[03:31] finally, here's a model with a 100,000 neurons. We're getting even closer at this point,
[03:37] but even with a 100,000 neurons, there's a couple of parts of the border that our model hasn't learned.
[03:43] It feels like the universal approximation theorem isn't really working. What are we missing here? But
[03:50] before we get into the details of what's going wrong, let me show you one more thing. Let's take just 128 neurons. But
[03:58] instead of arranging them in a single wide layer, let's arrange them in four separate layers of 32 each like this,
[04:04] where the output of each layer is passed into the next. After training this model, these are the resulting learned
[04:11] regions and decision boundary. Our five layer network with just 130 total
[04:16] neurons is able to learn a more precise border than our 100,000 neuron model and
[04:22] it's able to divide up our map more effectively. How is it that rearranging our neurons
[04:28] into multiple layers makes our model so much more powerful? The neurons in both our deeper and shallow models do the
[04:34] same folding, scaling, and combining operations. Why are these operations so much more
[04:40] effective when composed in multiple layers? And how does the geometry of our map change as it moves through these
[04:47] stacked operations? This video is part of a series sponsored
[04:52] by Incogn. These videos have really pushed my animation abilities, requiring
[04:57] a bunch of deeply focused hours, which Incogn has really helped me with by significantly reducing the number of
[05:03] spam text and calls that I receive. Incogn also helps protect my privacy. In
[05:08] the United States, we have these people search sites where for a small fee, anyone can look up information about you
[05:14] like your address, your email, phone number, education, employment history, social media accounts, and so on. This
[05:20] gives you an idea of all the information about you that data brokers are able to gather and sell. Last year, I signed up
[05:26] for one of these people search sites to see what information I could find on myself. After being an incogn for a few
[05:33] months, I impressively wasn't able to find any information on myself, but I
[05:38] was able to find a ton of information on my wife. Since then, I've upgraded to Incogn's friends and family plan and
[05:44] added my wife to the plan. I checked the same people's search site again this week and was happy to see that all of
[05:49] her information had been removed. Incogn has just released a new feature that makes their service even more
[05:56] effective called custom data removals. If you type your name and address into Google, you may be surprised to find
[06:02] where exactly your personal information pops up. With custom removals, you can submit specific URLs directly to the
[06:08] Incogn who will work to remove your information from eligible sites. You can get a great deal on incogn 60% off an
[06:15] annual plan by visiting incogn.com/welchlabs and using code welchlabs at checkout.
[06:22] It's been a while since I've made a multi-part series like this. Huge thanks to incogn for helping make this series
[06:28] possible and helping me get more quality focus time as I work on it.
[06:33] Last time in part two of this series, we dug into the mathematics of how modern models are trained using back
[06:39] propagation and gradient descent. We saw how given the inputs of latitude and longitude, a single layer model can
[06:46] effectively learn to position planes over different European cities, learning to separate Paris, Berlin, Madrid, and
[06:52] Barcelona. The key piece of functionality here is that our model learns to position the Madrid plane
[06:58] above all the other planes above Madrid, the Barcelona plane above all the other planes above Barcelona, and so on. And
[07:05] the height of our planes corresponds to our network's final confidence in a specific city. We left off considering
[07:11] the most complex geographic border in the world between Belgium and the Netherlands in the municipality of
[07:17] Barlay Herto. Given a single plane for each country, there's no way to position our planes.
[07:24] So our Belgium plane is on top of our Netherlands plane above only the Belgium portions of our map. Another way to
[07:30] think about this is that our two tilted planes intersect at a line on our map where everything on one side of the line
[07:36] will be classified as part of Belgium and everything on the other side will be classified as part of the Netherlands.
[07:42] And there's no way this linear decision boundary can correctly divide up our city. Our networks from last time looked
[07:48] like this with a single layer of neurons between our inputs and softmax function.
[07:54] As we saw last time, the softmax function bends our planes to output nice final probability values. But
[08:01] importantly, it doesn't change the location of the decision boundaries at the intersections of our planes. For
[08:06] this reason, we won't concern ourselves too much with softmax in this video. The networks we saw at the beginning of this
[08:12] video add one more layer of neurons and are able to accomplish significantly more. Just like the neurons in our
[08:19] simple single layer model, each of the neurons in the first layer of our two-layer network contains a simple
[08:25] linear model that geometrically looks like a plane. Mathematically, the first
[08:30] neuron in our first layer takes in the coordinates of our point, multiplies each coordinate by a learned number
[08:36] called a weight, which we're writing here using lowercase m, and adds these results together. The weight values
[08:42] control the steepness of our plane in each direction. Finally, we add one more learnable parameter called a bias. This
[08:49] shifts our whole plane up and down. So, if we pass in this Belgium point on our
[08:54] map with coordinates of x1= 0.6 and x2= 0.4, we multiply our x1 value by our
[09:01] first weight and our x2 value by our second weight and add these results together. And finally, we add our bias
[09:07] value to compute our final result of minus0.14. This computed value corresponds to the
[09:14] height of our first neurons plane at these input coordinates. Now, if we just pass the height of our plane, minus0.14
[09:22] in this example, into our second layer of neurons, our multiple layers of neurons will actually just collapse back
[09:28] down into what is effectively a single layer of neurons. We can show this collapsing algebraically. There's just a
[09:35] bunch of terms to deal with. These first two equations correspond to the first two neurons in our first layer. Note
[09:41] that we're using these superscripts to keep track of where each weight comes from. Everything with a superscript of
[09:47] one comes from our model's first layer. Here's the equation for the first neuron in our second layer. If we pass the
[09:53] outputs of our first layer directly into our second layer, this is equivalent to plugging in our first set of equations
[09:59] into our second equation like this. Distributing and collecting terms, we
[10:05] end up with a new constant times our input x1 plus another new constant times our input x2 plus this final constant.
[10:12] This equation has the same shape as our individual neuron equations just with different constants.
[10:20] This result tells us that if we just hook up the outputs of one layer of plane fitting neurons to the inputs of
[10:25] our next layer, we end up adding together different tilted planes, which just results in a different tilted
[10:31] plane. So, a two-layer network connected like this is still only capable in practice of fitting two planes to our
[10:38] map, just as our single layer model did. For our multi-layer neural network to be
[10:43] able to learn more complex patterns, we need to add one more small piece of math.
[10:48] We'll pass the output of our planes from our first layer into a function called an activation function that will modify
[10:54] their shape into something more complex for our model to work with. It turns out that we can build high performing neural
[11:00] networks using a variety of activation functions. But one of the simplest and most widely used today is a function
[11:06] called a rectified linear unit or RLU. RLU is incredibly simple. For input
[11:12] values less than zero, RLU returns zero. And for input values greater than or equal to zero, ru simply passes its
[11:20] input value through. So ru of minus1 is zero and ru of one is one.
[11:27] Applying our ru activation function to the output planes of our first layer. The regions of our plane with heights
[11:34] less than zero are folded up or clipped to a height of zero. So instead of outputting planes, the first layer of
[11:40] our network now outputs these bent planes. This is the folding operation we saw at the beginning of the video. So to
[11:47] decide which country a point is in. For example, this Belgium point with coordinates of 0.60.4 that we saw
[11:54] earlier, we pass these coordinates into our first layer of neurons and get values of minus0.14 and minus0.33 out
[12:02] corresponding to the height of each of our planes at the input coordinates of our point. From here we apply our ReLU
[12:08] activation function folding all values below zero up to zero. The height of our
[12:14] point on both planes is negative. So we set both points to zero. So our input
[12:19] point 0.60.4 has now been mapped to values of 0 0 by our bent planes. From here our final
[12:26] layer of neurons multiplies these values of 0 by its weights and adds its bias
[12:32] terms, shifting our combined bent planes up and down. moving our point to 0.03 on
[12:38] our top surface and minus 0.89 on our bottom surface. Our second neuron's
[12:44] output corresponds to our model's confidence in Belgium, which is higher in this case, meaning this point will be
[12:50] classified as being in Belgium. And visually, we see this point on our Belgium plane being above our point on
[12:56] our Netherlands plane. We can do a similar analysis for a point in the Netherlands like this point at 0.3 0.7.
[13:04] The key difference here is that this point does not fall in the zero relu region of our second neuron. Meaning
[13:11] that it gets pushed up on our final Netherlands bent plane and pushed down on our final Belgium plane, resulting in
[13:17] a correct Netherlands classification. So our bent plane geometry is equivalent
[13:23] numerically to moving data through our network, but gives us a nice way to see how all of the points on our map are
[13:29] processed at once. As we add more neurons to our first layer, we're able to make more and more
[13:35] folds in our map, cutting our map into more and more regions for our output neurons to push up and down into more
[13:41] and more complex surfaces. Now, as we saw at the opening of the video, assuming a sufficient number of
[13:47] neurons in our first layer, the universal approximation theorem tells us that a two-layer neural network exists
[13:54] that can represent the borders of our town at arbitrarily high precision. But as we saw, even at a 100,000 neurons
[14:01] in our first layer, we were not able to successfully train a model to completely match our borders. What is going on
[14:08] here? The universal approximation theorem is sometimes mistaken to mean
[14:14] that neural networks can learn anything. But what it really says is that a wide enough neural network is capable of
[14:20] representing any continuous function. Now the borders of our town are actually
[14:25] not continuous. But the continuity that the theorem is referring to here is actually the continuity of the final
[14:31] surfaces that we intersect to find our border. The real issue here is that
[14:36] although the universal approximation theorem tells us that a two-layer solution exists, it does not mean that
[14:42] in practice we can actually find the solution. And the theorem does not tell us how many neurons we actually need to
[14:48] solve a given problem. As we saw in parts one and two of this series, modern neural networks learn
[14:55] using back propagation and gradient descent, which provide no guarantees of finding the best or even a good
[15:01] solution. Instead, these algorithms make small iterative updates to our parameters, and we typically just stop
[15:08] the learning process when performance stops improving. Before training, our network is randomly
[15:14] initialized, placing our fold lines at random locations on our map. Here's one
[15:19] initialization for our five neuron two-layer model. Here's how our folded planes are combined by the second layer
[15:26] of this model. And here's how these surfaces intersect to form a decision boundary before training. If we pass in
[15:32] the Belgium point we considered earlier into our randomly initialized model, this point ends up on this planer region
[15:38] in our second layer surface. This first neuron surface ends up on top in our
[15:43] final output shown here in blue. meaning that our model incorrectly classifies our point as being in the Netherlands.
[15:50] This error is measured using the cross entropy loss as we saw in part two. And this loss is then run through our back
[15:56] propagation algorithm resulting in gradient values for each of our model 17 parameters.
[16:02] Some of the largest resulting gradients are for this third neuron in our first layer. Both our DLDM31 and our DLDB3
[16:10] gradients are large and negative. Currently m31 is negative tilting our
[16:16] plane down in the x1 direction. Our gradient is telling us that to decrease
[16:21] our loss we should increase m31 which will reduce the slope of our plane
[16:27] making it flatter. Back propagation also returns a large negative value for dlddb3
[16:33] which tells us to shift our whole plane upwards. Adjusting our parameters in this
[16:38] direction moves our plane and shifts our RLU joint line to the right.
[16:44] Zooming out to our full network, we can see how this update moves the center fold line in our second layer to the
[16:50] right. On our final surfaces, our update moves our top blue surface down,
[16:56] reducing the model's confidence in the incorrect answer of the Netherlands while moving our decision boundary to
[17:01] the right. We can now repeat this gradient descent process and watch our model learn. Step
[17:08] by step, these small updates adjust both the locations of the fold lines in our first layer and the way these bent
[17:14] planes are combined by our second layer until we have a nice concave down surface on top of Belgium that
[17:21] intersects a concave up Netherland surface at a nice border. Now, when I initially tried to train
[17:28] this model, it didn't actually work nearly this well. I had a different random initialization that looked more
[17:33] like this. Placing our blue surface on top of our yellow surface when we want
[17:38] our model to learn the exact opposite orientation with a central yellow region for Belgium on top. As our model learns
[17:45] from this starting point, our back propagation algorithm begins to reverse the orientation of these surfaces,
[17:52] lowering our loss values and moving the blue surface down and the yellow surface up. But in doing so, back propagation
[18:00] pushes the decision boundaries off of our planes, leaving our whole town in the zeroed out part of our bent relu
[18:06] plane. Gradient descent is not able to recover from this configuration since
[18:11] the gradients through the zeroed out part of our RLU activation function are also zero, leaving our model with
[18:17] effectively a single plane to work with, resulting in a sub-optimal linear decision boundary. So even though we
[18:24] know that a nice solution exists for our five neuron network given this starting point gradient descent is not able to
[18:30] find it in the case of our super wide 100,000 neuron network there may be
[18:36] analogously good solutions out there we just can't reach them with gradient descent
[18:42] now there is some subtlety here as we saw back in part one when models become large the chances of gradient descent
[18:50] actually getting stuck in a local minimum in this highdimensional loss landscape becomes very small. Our super
[18:56] wide network is probably not getting stuck in quite the same way as our small network.
[19:02] In addition to not telling us how to find a specific solution, the universal approximation theorem also does not tell
[19:08] us how many neurons we actually need to solve a given problem. And in fact, for a broad class of functions, it's been
[19:15] shown that the number of neurons we need in a shallow network is exponentially larger than the number of neurons needed
[19:21] in a deep network. So, it's possible that a 100,000 neurons may actually not
[19:26] be enough. Finally, it's difficult to prove a negative. In the course of making this video, I experimented with a
[19:33] bunch of different optimizer configurations for these wide models. But it wouldn't surprise me if there's a
[19:38] way to train a 100,000 neuron, a 10,000 neuron, or maybe even smaller two-layer model to fit the borders of our town.
[19:45] I'll leave a link to my code in the description if you want to experiment. And please send me your results if you make progress. I would love to see a
[19:52] solution. Exact number of neurons aside, as we saw earlier, we can make incredible efficiency gains by going
[19:58] deep instead of wide, stacking our neurons into additional layers. And that's where we'll turn our attention
[20:04] next. What new geometry does stacking our layers create? And how does this
[20:09] geometry help our model learn the complex borders of our town? Let's begin with a simple two-layer model with two
[20:16] neurons each. This simple two-layer model learns these folds in our map which are combined by our second layer
[20:22] into this bent up surface and this bent down surface. Taking the intersection of our surfaces where our model is equally
[20:29] confident in both countries, we get this simple decision boundary. Now let's add
[20:35] a third layer to our model with two additional neurons. So we now have three layers and six neurons total. After
[20:42] training, our first layer learns to fold our input planes like this. And our second layer learns to combine our bent
[20:48] planes like this. Now, if we only had two layers, we would just bring these surfaces together to form our final
[20:55] decision boundary. But we now have a whole additional layer of transformations to apply.
[21:01] Just as we did in our first layer, we now need to apply our RLU activation function where all of the values on our
[21:07] surface with heights less than zero are set to zero. In our first layer, this operation folds our planes along linear
[21:14] fold lines. But now in the second layer of our model, the surfaces we're folding are no longer simple planes. If we add a
[21:22] plane at Z equals 0 to our first neuron surface, we can see that this surface actually has three separate planes that
[21:29] all cross Z equals 0. When we apply our RLU activation function and fold up our
[21:35] surface, we create three separate new fold lines, one for each region that
[21:40] crosses the Z equals0 plane. And interestingly, these folds are not at the same angle, but actually bend at the
[21:48] joints of the planes we get from our first layer. So here, a single neuron is able to make three separate folds with
[21:54] fairly complex geometries. Our second neuron in our second layer applies the same operations, but with different
[22:01] learned weights, resulting in these three new folds. Now, just as our previous two layers
[22:08] did, our third and final layer scales and adds our new surfaces together.
[22:14] After our first layer, the combination of our two RLU folds created four regions for the next layer of our model
[22:20] to work with. These are easiest to see in a 2D projection like this.
[22:26] Stacking the new fold lines from our second layer. These new folds at various angles come together in a significantly
[22:32] more complex tiling of our map with these 10 separate regions. When the
[22:37] final layer of our network scales and adds together the outputs of our second layer, the resulting surfaces are
[22:43] composed of the same 10 regions, just with different heights.
[22:48] The height of these surfaces corresponds to the model's final confidence in our two countries. Bringing these surfaces
[22:54] together and finding their intersection, we get this final decision boundary, which shows some nice peace-wise linear
[23:01] curvature around the Belgium regions of our map. So the first layer of our network
[23:06] creates these two folds and four separate regions on our map which are then split by our second layer into
[23:12] these 10 regions which are used by our final layer to create these surfaces which intersect in a nice border. The
[23:19] fact that just adding two additional neurons takes our map from these four regions to these 10 is remarkable to me
[23:26] especially considering the complex geometry of these 10 regions. If we instead arrange our six neurons in
[23:32] a two-layer network like this, our model learns to fold four copies of our map like this, resulting in these seven
[23:40] regions, these surfaces, and this final decision boundary.
[23:45] This decision boundary isn't necessarily worse than the one learned by our deeper model, but I'm particularly struck by
[23:51] how much more complex the tiling learned by our deeper model is. Qualitatively,
[23:56] the tiling of our map learned by our shallow network feels very much like we've just stacked four lines together,
[24:02] which is exactly what we've done. While the tiling learned by our deeper model feels to me like something entirely
[24:08] different by repeating our folding, scaling, and combining operations, these operations
[24:14] are able to compound on themselves, allowing the neurons in our second layer to generate significantly more complex
[24:21] patterns than they would if they were instead positioned in the first layer of our model.
[24:26] The compounding analogy is not a coincidence. It turns out that we can show that the maximum number of regions
[24:32] a rail network like ours can divide our map into grows exponentially with the number of layers in our network. This
[24:39] equation gives the theoretical maximum number of regions our model can create as a function of the number of neurons
[24:45] in each layer D, the number of inputs D subi, and the number of layers in our network K, not including our final
[24:52] output layer. Plugging in d= two neurons per layer, d subi equals 2 inputs, and k
[24:59] equals 2 layers, we get 2 ^2 * 4 equ= 16 total possible regions for our model.
[25:06] This is a bit above the 10 regions our model actually learned. If we add another two neuron layer to our model,
[25:12] our number of regions grows to 2 ^ of 4 * 4 = 64. And adding another layer gets
[25:19] us to 256 and so on. So each layer theoretically quadruples the number of
[25:24] regions our model can create in this configuration. This final polomial part of the equation
[25:30] captures what happens in the final layer of our model. If we cut back down to a
[25:35] shallow two-layer model K becomes one eliminating the exponential growth term.
[25:41] As we've seen two-layer networks divide up the input plane by stacking separate RLU folds.
[25:47] So finding the number of regions we can divide our map into with a two-layer network is equivalent to asking how many
[25:53] separate regions we can split a plane into with d lines. This is a well-known result in combinatorial geometry with
[26:01] the answer given by this polomial. So our theory tells us that the maximum
[26:06] number of regions we can create with a two-layer network grows as a polomial function of our number of neurons while
[26:13] the number of regions we can create with a deeper network grows exponentially with the number of layers.
[26:19] Placing 64 neurons in the first layer of a two-layer network like this results in a maximum 281 possible regions while
[26:27] rearranging these neurons into four layers instead results in a theoretical maximum of over 70 million possible
[26:33] regions. The difference between these growth rates is compelling and is often pointed
[26:39] to as a reason for the effectiveness of deep learning. However, these numbers are theoretical upper bounds and as a
[26:45] number of papers have pointed out, these bounds are very loose. In practice, we typically do not see exponential growth
[26:51] in the number of regions created by deep networks as we add layers. Let's scale up our own deep network and
[26:58] see how our number of regions scales with our network and how our fit improves. We left off with this three
[27:04] layer six neuron model that divided our map into these 10 regions resulting in
[27:09] this final decision boundary. Let's first expand our model to have eight neurons in each of our first two
[27:16] layers. The eight folds in our first layer now break up our map into these 19
[27:21] regions. And the various folds of the surfaces created by our second layer come together in these 102 regions. Our
[27:29] second layer patterns start to get really interesting. Here the RLU function in our second neuron is folding
[27:35] our surface along 10 different unique joints. Our final layer scales and combines these outputs into these final
[27:42] surfaces which intersect like this resulting in this final decision border
[27:48] capturing the two largest sections of our town nicely. Note that a couple of the neurons in our
[27:54] second layer don't have any colored regions. This means that the entire surface from our first layer was below Z
[28:00] equals 0 and all inputs are set to zero by our RLU activation function. Dead
[28:05] neurons like this are common. And a reminder that gradient descent gives no guarantees about efficiently using our
[28:12] model architecture. Let's add another eight neuron layer to our model resulting in four total
[28:18] layers. We can now really start to see the compounding effects of our repeated folding, scaling, and combining
[28:25] operations. The relu folding happening in this third neuron of our third layer creates these
[28:31] tiny regions around the border. It's so interesting to me that our model guided by back propagation figures out how to
[28:38] create all these extra little polygons around our town's borders to capture their detailed structure.
[28:45] Now, at this scale, it becomes tough to make sense of everything that's happening in 3D space like this. Let's
[28:51] focus on the regions formed on our 2D map by each layer, the final 3D surfaces, and our final decision
[28:57] boundary. Let's watch our model learn from this perspective. Before training, here's how our model initially divides
[29:03] up our input space, creating this decision boundary. Before we start the training process, let's add one more
[29:09] panel that will track the model's loss as it learns. In less than a 100 gradient descent
[29:16] steps, our model is able to pick out the core structure of our town
[29:21] and then is able to progressively tighten its borders as it learns, creating more and more regions around
[29:27] the fine details of the border. Finally, let's add one more layer,
[29:33] bringing our total number of layers to five, and increase our width one last time to 32 neurons. Our additional layer
[29:40] gives us one more tiling of our map. And at this scale, our 3D plot becomes a bit too chaotic to make sense of. So, we'll
[29:47] just watch the 2D plots in this final training animation. Unlike our smaller models, this deeper model really
[29:53] benefits from more training steps. Using the extra steps to refine the details of our town's border.
[30:01] The fact that just four layers with 32 neurons each can learn this level of complexity is remarkable to me. Our
[30:08] final decision boundary impressively captures every region of our town. It's
[30:13] incredible to me that a bunch of little linear models can come together to do something so complex and that we can
[30:19] actually find these solutions using gradient descent.
[30:25] Around 10 years ago, I released the very first Welch Labs video. It's called Neural Networks Demystified.
[30:32] Like the series you're watching now, neural networks demystified was a series about how neural networks learn,
[30:38] focusing on back propagation and gradient descent. Sitting down to work on this series 10
[30:44] years later, I honestly didn't know where to start. Although most of the core approaches in my old videos are
[30:49] unchanged, these core ideas have been scaled to solve unbelievably complex problems. And this shocking ability to
[30:56] scale has led the research community to dig deeper into what makes these models tick. We've learned a great deal in 10
[31:03] years, but many mysteries remain. In part one of this series, we dug into
[31:08] lost landscapes, and we saw how the standard mental picture of gradient descent that I presented 10 years ago
[31:14] really doesn't hold up in the incredibly highdimensional spaces these models operate in. In part two, we dug into the
[31:21] core mechanics of how models learn, dissecting back propagation in the context of a modern large language
[31:26] model. Finally, in this video, we saw how deep models are able to recursively fold, scale, and combine their input
[31:33] spaces, learning incredibly complex patterns with remarkably few neurons.
[31:39] Maybe in another 10 years, I can make another series like this. We'll have to wait and see what these models can do
[31:45] then, and how much sense we'll be able to make of how they do it.
[31:51] Back in 2019, I completely quit Welch Labs. I had just tried going full-time
[31:56] creating videos, but I wasn't able to earn enough money to make it work. I got frustrated and I quit. I went off and
[32:03] worked as a machine learning engineer, which was great, but I couldn't shake the feeling that I was really supposed to be making videos. Starting in 2022, I
[32:11] slowly eased back on Tik Tok and was able to gradually build enough momentum to take another crack at going full-time
[32:17] last year. When I quit in 2019, I had some time to really think about what kept pulling me back into making videos.
[32:25] And I realized that deep down it was really about education. I loved math and science as a kid, but I
[32:31] really disliked the way I had to learn it in school. After undergrad, I really found myself questioning if I even liked
[32:37] math at all. Only through my own work and study did I fall back into love with math and science years later. And now I
[32:43] want to use Welsh Labs to make education better. But I've realized for me to be
[32:49] able to do this, I have to first build a viable business. If I can't support myself and my family, I can't spend the
[32:55] time I need to make this work. Last year, through sponsorships, poster and book sales, and support on Patreon, I
[33:02] was able to make about half of what I made as a machine learning engineer. I'm not going to lie, so far, this is a much
[33:08] harder way to earn a living. My goal this year is to replace my full income.
[33:13] This will allow me to really reach escape velocity and continue full-time on Welch Labs.
[33:19] Sponsorships, posters, and book sales are going well this year, but to hit my goal, I need to grow Patreon as well.
[33:25] Your monthly support on Patreon would mean a lot. As a way to say thank you, and today I'm launching a new reward.
[33:32] Starting at the $5 per month level, I'll send you a real paper cutout used in a Welch Labs video. It comes in a nice
[33:39] protective sleeve with the Welch Labs logo on the front, and on the back, it says the video it came from, the release
[33:44] date, and a sign by me. These are a lot of fun. I have them going all the way back to 2017. At the $5 per month level,
[33:51] you'll receive a smaller cutout and a larger cutout at the $10 or higher level. Cutouts ship after your first
[33:57] monthly payment goes through, and you'll find a link to the Watch Labs Patreon in the description below. Huge thank you to
[34:03] everyone who supported Welch Labs over the years. Thanks for watching.