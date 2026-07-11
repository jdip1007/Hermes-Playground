---
source_url: https://www.youtube.com/watch?v=z64a7USuGX0
ingested: 2026-07-08
video_id: z64a7USuGX0
title: What the Books Get Wrong about AI [Double Descent]
series: None
---

[00:00] This video is sponsored by KiwiCo. More
[00:02] on them later. Also, I've written a
[00:05] whole new book on AI. You can learn more
[00:07] about the book at the end of this video.
[00:10] When I first learned machine learning,
[00:12] these three books were incredibly
[00:14] helpful, but they're also all wrong.
[00:17] Each book has a version of the same
[00:18] plot, a core tenant of machine learning
[00:21] theory in practice. The x-axis shows the
[00:24] size of a learning model and the y-axis
[00:27] shows the model's performance measured
[00:29] using some type of error metric. From
[00:32] here, we plot two curves. The first
[00:34] curve shows the model's performance on
[00:36] its training data. As our model becomes
[00:39] larger, it's able to learn more complex
[00:41] patterns, better fit its training data,
[00:44] and bring down its error. Of course,
[00:46] what we really care about here is how
[00:48] well our model will perform on examples
[00:50] outside of its training set. Our second
[00:53] curve shows the same error metric, but
[00:56] measured on a test set that the model
[00:57] hasn't seen before. Again and again in
[01:01] every book, the test set error curve has
[01:03] the same U shape. Our testing set error
[01:06] starts high for smaller models, comes
[01:09] down to a nice minimum for some
[01:10] medium-siz model, and shoots back up as
[01:13] the size of our model continues to grow.
[01:16] The shooting back up part of the testing
[01:18] curve is due to the model overfitting
[01:20] the data.
[01:22] Many authors demonstrate the overfitting
[01:24] phenomenon using polomial curve fitting.
[01:27] If we take a set of data points, for
[01:29] example, this set of parabola shaped
[01:31] points and set aside half of our data
[01:34] for testing and fit a first order
[01:36] polomial which is just a line. Our curve
[01:39] fit will be poor. We can measure just
[01:42] how bad our fit is by taking the
[01:43] differences between our fit line and our
[01:46] training points. Squaring and averaging
[01:48] these errors together, we get the mean
[01:51] squared error of our linear model on our
[01:53] training set. We can repeat this process
[01:56] on our test set points to compute our
[01:58] test set error. Both our training and
[02:01] testing errors are relatively high
[02:04] because our simple linear model is not
[02:06] powerful enough to fit our parabola
[02:08] shaped data. Moving to a second order
[02:11] polomial, our parabolic model is now
[02:13] able to nicely fit our parabolic data,
[02:16] bringing down our training and testing
[02:19] error.
[02:21] Fitting a third order model, our cubic
[02:23] curve is able to get very close to our
[02:25] training points, bringing down the error
[02:28] on our training set, but starts to fit
[02:30] the noise in our data instead of the
[02:33] underlying parabolic shape, resulting in
[02:36] worse performance on our test set.
[02:38] Moving to a fourth order polomial
[02:41] overfitting becomes even worse. Our more
[02:44] powerful model is able to now perfectly
[02:46] fit our noisy data with zero training
[02:49] error but result in wild curve fits and
[02:52] worse test set performance and our
[02:54] resulting errors line up with the
[02:56] characteristic U-shaped testing error
[02:58] curve.
[03:00] This central idea is often known as the
[03:02] bias variance tradeoff and is named
[03:05] after a nice piece of statistical theory
[03:07] that supports the idea that our test set
[03:09] curve should be U-shaped.
[03:12] The takeaway for a whole generation of
[03:14] machine learning practitioners was that
[03:17] we must carefully limit the power of our
[03:19] models to match the complexity of our
[03:21] data to avoid overfitting.
[03:24] Our U-shaped test error curve supported
[03:27] by the bias variance trade-off theory
[03:30] feels disciplined. It feels responsible.
[03:33] It's telling us that the core of machine
[03:35] learning is about balance. But it's also
[03:38] wrong.
[03:43] In 2012, Alex Kreseky, Ilia Sudgver, and
[03:46] Jeff Hinton successfully trained what
[03:48] was then considered an enormous
[03:50] classification neural network with
[03:52] around 60 million parameters. that today
[03:55] we call AlexNet.
[03:57] Overfitting was a significant concern
[03:59] for the AlexNet team. To reduce
[04:02] overfitting, the team used data
[04:04] augmentation, applying random shifts,
[04:06] flips, and color changes to their images
[04:08] while training and used a new technique
[04:11] called dropout, where collections of
[04:14] neurons are randomly turned off during
[04:16] training.
[04:17] Both data augmentation and dropout force
[04:20] AlexNet to learn more robust and general
[04:22] ways to classify images that don't
[04:25] depend on exactly how an image appears
[04:27] or a specific pathway through the
[04:29] network. And the team found that without
[04:32] data augmentation and dropout, the model
[04:34] exhibited substantial overfitting.
[04:38] The team also used a technique called
[04:40] weight decay where the model is
[04:42] penalized for having large weight
[04:43] values. If we apply the same weight
[04:46] decay approach to one of our overfit
[04:48] polomials from earlier, we see that as
[04:50] we increase the amount of weight decay,
[04:52] our fit becomes smoother, reducing
[04:54] overfitting. In statistics, this is
[04:57] known as ridge regression.
[04:59] Data augmentation, dropout, and weight
[05:02] decay are all examples of regularization
[05:04] techniques where we modify the training
[05:06] process to prevent our model from
[05:08] overfitting the data.
[05:11] These techniques were seen as critical
[05:12] back in 2012 and remain very common
[05:15] practice in machine learning today. The
[05:18] takeaway for many machine learning
[05:19] practitioners at the time, myself
[05:21] included, was that large neural networks
[05:23] were clearly in the overfitting region
[05:25] of the bias variance curve and that
[05:28] without regularization, these models
[05:30] would dramatically overfit,
[05:33] effectively memorizing their training
[05:34] examples without learning the robust
[05:36] pattern recognizers needed to generalize
[05:38] to new examples.
[05:40] and that through regularization we could
[05:42] push these models back towards the happy
[05:44] middle of the curve.
[05:46] A sneakier and more subtle conclusion,
[05:49] one that I certainly internalized at the
[05:51] time, is that in the overfitting regime,
[05:54] lower training set error is causally
[05:56] linked to higher test set error. This
[05:59] implication even shows up in the name
[06:01] we've chosen for the phenomenon.
[06:04] Overfitting implies that we're doing too
[06:06] much fitting of the training data and
[06:08] that doing too much fitting, lowering
[06:10] our training set error too much, is
[06:13] causing something bad. In this case,
[06:15] leading to higher test set error.
[06:19] Alexet was a wild success and deep
[06:22] learning exploded over the next few
[06:24] years with larger and deeper models
[06:26] delivering more and more impressive
[06:28] results.
[06:29] We would expect models larger and more
[06:31] complex than AlexNet to require more
[06:33] aggressive regularization to avoid
[06:35] overfitting.
[06:37] But this turned out not to be the case
[06:39] with deep learning continuing to
[06:41] generalize suspiciously well even
[06:44] without aggressive regularization
[06:45] measures in place. In 2016, a team at
[06:49] Google Brain addressed this apparent
[06:50] contradiction headon in a brilliantly
[06:53] insightful paper called Understanding
[06:55] Deep Learning Requires Rethinking
[06:57] Generalization.
[06:59] To test the extent to which we can
[07:00] actually control overfitting in deep
[07:02] models, the Google brain team devised a
[07:05] clever experiment where they took the
[07:07] same imageet data set that Alexet was
[07:09] trained on and the smaller sefar image
[07:12] classification data set and completely
[07:14] randomized all the labels and train
[07:17] models to predict these random labels.
[07:21] So one cat in the imageet data set would
[07:23] be labeled as an aircraft carrier and
[07:25] the next cat would be labeled as a sea
[07:27] snake and so on.
[07:29] The only way for a model to do well in
[07:31] this training data is to dramatically
[07:33] overfit or essentially memorize each
[07:36] example. This exact cat image is an
[07:39] aircraft carrier. This exact cat image
[07:41] is a sea snake and so on. Because the
[07:44] labels are randomized, there are no
[07:46] deeper patterns to learn. All noise, no
[07:50] signal.
[07:52] Now, if regularization was actually
[07:54] preventing deep models from overfitting,
[07:56] as was widely believed, we would expect
[07:59] a regularized deep model to not learn
[08:01] these randomly assigned labels,
[08:04] resulting in poor performance on the
[08:06] training set.
[08:08] Shockingly, the team showed that deep
[08:10] models were able to perfectly memorize
[08:12] all 50,000 training images in the CFAR
[08:15] data set and almost all of the 1.3
[08:18] million training examples in the imageet
[08:20] data set, even with regularization in
[08:23] place.
[08:25] These models of course perform terribly
[08:27] on their test sets, performing no better
[08:29] than random guessing.
[08:32] So deep models even with regularization
[08:34] in place are perfectly capable of just
[08:37] memorizing their training data. However,
[08:40] when we switch back to the correct
[08:41] labels, the same models with the same
[08:44] training procedures do not memorize and
[08:46] instead learn robust patterns that do
[08:49] generalize to new data.
[08:52] The Google Brain team also showed that
[08:54] when learning from the correct labels,
[08:57] contrary to the AlexNet team's findings,
[08:59] regularization was not actually critical
[09:01] to avoid overfitting.
[09:04] By 2016, a more efficient and flexible
[09:06] deep architectures than AlexNet had been
[09:08] developed. The Google brain team trained
[09:11] a newer inception v3 architecture on the
[09:14] same imageet data set that AlexNet was
[09:16] trained on and observed that when they
[09:18] removed data augmentations, dropout and
[09:21] weight decay, the model's test set
[09:24] performance did decrease, but only
[09:26] modestly.
[09:28] And they also found that an inception v3
[09:30] model trained without any explicit
[09:32] regularization performed on par with the
[09:34] original Alexet results.
[09:38] And even more interesting, when
[09:40] regularization did make these modest
[09:42] improvements to test set accuracy, it
[09:44] had very limited or apparently no impact
[09:47] on training set error. As we would
[09:50] expect if regularization was moving our
[09:52] model back towards the center of the
[09:54] bias variance curve,
[09:57] these models trained on the CFAR data
[09:59] set show an increase in the test set
[10:01] accuracy from around 86% to 89% when
[10:05] adding different types of
[10:06] regularization. But all four models
[10:08] still perfectly fit the training data
[10:11] with accuracies of 100%.
[10:14] These results dramatically call into
[10:16] question the fundamental trade-off
[10:18] between training set and test set
[10:20] performance predicted by the typical
[10:22] bias variance curves in the overfitting
[10:24] region.
[10:26] Returning to our polomial curve fitting
[10:28] example. This model behavior is
[10:30] analogous to our curve somehow exactly
[10:33] fitting our noisy observations
[10:35] while still effectively learning the
[10:37] underlying parabolic shape and
[10:39] performing well on our testing points.
[10:42] Exactly fitting the training data is
[10:44] known as the model interpolating the
[10:46] data.
[10:48] So what's going on here? Does the bias
[10:51] variance trade-off simply not apply to
[10:53] deep models? Do we even need to worry
[10:56] about overfitting when training deep
[10:58] neural networks? And should I throw away
[11:00] all of my statistics and machine
[11:02] learning books?
[11:05] Whenever I think about learning verse
[11:07] memorization, I can't help but think
[11:09] about how my own children are learning.
[11:11] Which is why I was more than happy to
[11:13] partner again with this video sponsor,
[11:14] Kiwico. Kiwi makes hands-on project kits
[11:18] that make learning genuinely fun for
[11:20] kids of all ages. My son just turned two
[11:23] this summer, and he's exploding with
[11:25] curiosity. I love these puzzles that
[11:28] promote spatial reasoning, and they're
[11:30] incredibly engaging. Even later that day
[11:33] when we were watching TV, he kept
[11:35] sneaking off to work on the puzzles. I
[11:37] love this. The thoughtfulness the Kiwi
[11:40] Co team puts into the crates really
[11:42] makes them so much stickier than many of
[11:44] the toys we have. I was worried that
[11:46] this pirate treasure crate was a little
[11:48] too old for my daughter. But I was
[11:50] delighted when she was able to
[11:52] understand the treasure map that we drew
[11:54] together and was able to follow the map
[11:56] to the right part of the house. Creating
[11:58] and reading maps like this takes some
[12:00] serious abstract reasoning. It was
[12:02] amazing to see. KiwiCo makes amazing
[12:05] gifts for the kids and families in your
[12:07] life, and they make awesome learning
[12:09] experiences for kids of all ages. Use my
[12:12] code Welch Labs to receive 50% off your
[12:15] first crate for kids three and older, or
[12:17] 20% off your first Panda Crate for kids
[12:19] under three. Big thanks to KiwiCo for
[12:22] sponsoring this video. Now, back to
[12:24] what's really going on with the bias
[12:26] variance trade-off.
[12:29] In 2018, a team of researchers led by
[12:31] Myle Belulin proposed an interesting
[12:34] alternative explanation of what's going
[12:35] on here.
[12:37] What if the traditional bias variance
[12:39] trade-off wasn't exactly wrong, but
[12:41] wasn't the full picture?
[12:44] What would happen to the bias variance
[12:46] curve if we just kept increasing the
[12:48] size of our models well beyond the
[12:50] overfitting regime?
[12:53] Are there certain combinations of models
[12:54] and data where we would actually see the
[12:57] testing set error come back down? Is
[13:00] there something beyond overfitting?
[13:03] The team showed some compelling
[13:05] small-cale demonstrations of exactly
[13:07] this phenomenon on the imnest
[13:09] handwritten digit data set using a
[13:12] random forier feature model. This is
[13:14] essentially a small two-layer neural
[13:16] network where only the final layer is
[13:18] trained. The team showed that these
[13:20] models would demonstrate the classical
[13:22] bias variance trade-off curve, but then
[13:24] suddenly shift to a new regime as model
[13:27] size increased further with test set
[13:30] performance improving dramatically and
[13:32] actually exceeding the test set
[13:34] performance found in the classical
[13:35] regime.
[13:37] The team called the phenomenon double
[13:39] descent.
[13:41] Their hypothesis was compelling, but it
[13:43] remained to be seen if the double
[13:45] descent phenomenon could be replicated
[13:47] in full-scale deep models and exactly
[13:50] what underlying mechanisms could be
[13:52] causing this unexpected behavior.
[13:55] The following year in 2019, a Harvard
[13:57] and OpenAI team definitively showed that
[14:00] double descent was real, demonstrating
[14:02] the phenomenon across a variety of model
[14:05] architectures, including transformers on
[14:08] both vision and language data sets.
[14:11] Interestingly, the team observed double
[14:13] descent behavior not only as a function
[14:15] of the size of their models, but as a
[14:18] function of how long their models were
[14:19] trained for.
[14:21] This observation is potentially highly
[14:23] relevant for machine learning
[14:24] practitioners.
[14:26] It's very common to visualize test set
[14:28] error while training and stop training
[14:31] when test set error stops coming down.
[14:34] It's also common to see test set error
[14:36] start to trend up later in training.
[14:39] This would typically be interpreted as
[14:40] the model beginning to overfit its
[14:42] training data.
[14:44] But what the Harvard team found
[14:46] remarkably was that for certain models
[14:48] and data sets, if you just kept training
[14:50] the model, the testing error would
[14:52] follow a double descent behavior coming
[14:55] back down in some cases to an even lower
[14:58] value.
[14:59] If you were training one of these models
[15:01] and assumed a classical bias variance
[15:03] trade-off behavior, you would likely
[15:05] stop training long before you saw the
[15:07] double descent.
[15:09] I should note here that the plots we've
[15:11] seen so far from the Harvard team's work
[15:12] include a small amount of added label
[15:14] noise on the CFAR data set. This makes
[15:18] the model more likely to overfit and the
[15:20] double descent curve more pronounced. We
[15:23] still see double descent without the
[15:24] added noise, but it's less dramatic.
[15:27] CFR is a very clean academic data set.
[15:30] So you could argue that adding label
[15:32] noise is a reasonable proxy for larger
[15:34] noisier data sets.
[15:37] So double descent is a real phenomenon.
[15:39] But why would models behave like this?
[15:42] To me, seeing this behavior while
[15:44] training is especially confounding. Why
[15:47] would models start overfitting while
[15:48] training only for the trend to reverse
[15:50] after undergoing more of the same
[15:52] training process?
[15:55] Let's return to our curve fitting
[15:56] example one last time. Remarkably, it
[16:00] turns out that double descent can also
[16:02] occur with simple polomial curve
[16:04] fitting.
[16:06] We saw earlier that a second order curve
[16:08] nicely fits our noisy parabolic data and
[16:11] this puts us nicely at the bottom of our
[16:13] bias variance curve. If we increase the
[16:16] order of our polomial to three, we begin
[16:18] to overfit with our training error
[16:21] dropping close to zero but our testing
[16:23] error shooting up. When we reach a
[16:26] fourth order polomial, our test error
[16:28] continues to increase and our training
[16:31] error goes to zero. Our fourth order
[16:34] curve has five free parameters that are
[16:36] able to exactly fit our five data
[16:38] points.
[16:40] This is analogous to our image
[16:42] classification models exactly fitting or
[16:44] interpolating their training data.
[16:47] This point is known as the interpolation
[16:49] threshold and corresponds to the
[16:52] smallest model that is capable of
[16:53] perfectly fitting our data. Now moving
[16:56] to a fifth order polomial, our situation
[16:59] changes a little. Our polomial is still
[17:02] able to perfectly fit our training data.
[17:05] But because our curve has six free
[17:06] parameters, but we still only have five
[17:08] training points. This means that there
[17:11] will actually be an infinite number of
[17:13] fifth order polomials that perfectly fit
[17:15] our five training points. Here's 100
[17:19] different fifth order polomials that
[17:20] perfectly fit our data.
[17:23] How does our curve fitting algorithm
[17:25] choose which curve to go with?
[17:28] It turns out that there's a fairly
[17:30] natural closed form matrix inversion
[17:32] solution that extends how we handle the
[17:35] earlier cases. The solver will
[17:37] effectively choose the curve with the
[17:39] smallest sum of squared coefficients.
[17:42] For example, this more chaotic curve fit
[17:44] corresponds to this polomial with these
[17:47] six coefficients.
[17:48] And this simpler curve corresponds to
[17:50] this polomial.
[17:53] If we take each coefficient from our
[17:55] first curves equation, square these
[17:57] values and add them together, we get
[17:59] 19.13,
[18:01] this value is known as the L2 norm
[18:03] squared of our coefficients.
[18:06] Performing the same computation on our
[18:08] second polomial, we get a smaller norm
[18:11] 7.04.
[18:13] So our solver would choose our second
[18:15] curve over our first.
[18:18] Out of all the possible fifth order
[18:19] curve fits, our second curve turns out
[18:22] to be the lowest norm solution. So this
[18:25] is the curve our solver would return.
[18:28] Just like our fourth order curve, our
[18:30] fifth order curve perfectly interpolates
[18:32] our training data resulting in zero
[18:34] training error. However, our fifth order
[18:37] curve is a bit less chaotic. And if we
[18:40] measure its test set error, we see that
[18:42] it's actually lower than our fourthderee
[18:44] polomial's test set error starting to
[18:47] create double descent behavior.
[18:51] Now there's an important technical point
[18:53] here about how exactly we set up our
[18:55] solver. Expressing our polomial as ax
[18:58] 5th plus bx to the 4th and so on turns
[19:01] out to create numeric instability for
[19:03] our solver. Especially as the degree of
[19:05] our polomial grows, it's common to
[19:08] instead use what's known as a different
[19:10] polomial basis. Here we're using the
[19:13] Leandre basis. The curve fitting model
[19:15] is still a fifth order polomial, but
[19:18] rearranged in a way where our
[19:19] coefficients multiply what are known as
[19:21] the Leandre polomials.
[19:24] These polomials have nice mathematical
[19:26] properties that make curve fitting more
[19:28] stable. We can rearrange our Leandre
[19:31] polinomial representation into our
[19:32] typical ax 5th plus bx 4th
[19:35] representation. But importantly the
[19:37] coefficients our solver actually uses
[19:39] when fitting our curve are different.
[19:42] Meaning that the minimum norm solution
[19:44] is different. And if we use a standard
[19:46] ax 5th plus b x 4th polomial
[19:49] representation and we pick a minimum
[19:51] norm solution, we do not see double
[19:53] descent behavior.
[19:55] I'll put some links about this in the
[19:57] video description.
[19:59] So depending on our exact curve fitting
[20:01] procedure, our solver will pick a
[20:02] minimum norm solution in our chosen
[20:04] polomial basis and some common choices
[20:07] of basis do exhibit double descent.
[20:11] Jumping to a tenth order fit, we have an
[20:14] enormous range of possible solutions.
[20:17] Here's a hundred of them. Some of these
[20:19] curves catastrophically overfit our
[20:21] data. However, again, our smallest norm
[20:24] constraint chooses a smoother curve that
[20:27] actually kind of looks like a squiggly
[20:29] version of our parabola and again brings
[20:32] down our test set error, giving us more
[20:34] nice double descent behavior.
[20:38] Now, why does our polomial curve fitting
[20:40] process demonstrate this perhaps
[20:41] surprising double descent behavior? Our
[20:45] worst generalizing fit is precisely at
[20:47] the interpolation threshold where our
[20:50] model exactly fits our training data for
[20:52] the first time. In this case, we have
[20:55] exactly as many constraints as we have
[20:57] variables, meaning there's only one
[20:59] unique curve we can fit. And our model
[21:01] is forced to contort itself exactly to
[21:04] the data and is more susceptible to
[21:06] noise. Unlike in our higher order fits
[21:09] where our solver has many curves to
[21:11] choose from and it can pick a smoother
[21:13] lower norm solution, the Harvard team
[21:16] lays out a similar line of thinking when
[21:18] reasoning about why double descent
[21:19] occurs in deep neural networks.
[21:22] For model sizes at the interpolation
[21:24] threshold, there is effectively only one
[21:26] model that fits the training data and
[21:29] this interpolating model is very
[21:31] sensitive to noise in the train set.
[21:34] For overparameterized models, there are
[21:36] many interpolating models that fit the
[21:38] training set. And SGD is able to find
[21:41] one that memorizes or absorbs the noise
[21:44] while still performing well on the
[21:45] distribution. SGD here refers to the
[21:48] stochastic gradient descent algorithm
[21:50] used to train deep neural networks. This
[21:53] algorithm works very differently than
[21:55] the solvers we used in our curve fitting
[21:57] example, but has interestingly been
[21:59] shown to arrive at norm minimizing
[22:01] solutions under certain constraints,
[22:04] just as our curve fitting solvers do.
[22:07] So, as we train larger models or train
[22:09] models for longer, when these models are
[22:11] near the interpolation threshold where
[22:14] they're just able to perfectly fit the
[22:15] training data for the first time, the
[22:18] model has less flexibility and is more
[22:20] likely to overfit.
[22:22] As we move to larger models or train for
[22:25] longer, our model has more flexibility
[22:28] and our training algorithm is able to
[22:29] choose smoother, less chaotic solutions
[22:32] that will better generalize to new data.
[22:35] So, should we throw out the bias
[22:37] variance trade-off and should I throw
[22:39] away all my books? The first book we
[22:42] showed at the beginning of the video,
[22:44] The Elements of Statistical Learning,
[22:46] which is a great book, by the way, was
[22:48] written by three Stanford statistics
[22:50] professors in the early 2000s.
[22:53] After Double Descent gained notoriety in
[22:54] 2018 and 2019, the book's first author,
[22:58] Trevor Hasty, co-authored a massive
[23:00] 70-page paper looking into the
[23:02] phenomenon. He titled the paper
[23:05] surprises in highdimensional ridgless le
[23:07] squares interpolation.
[23:09] In 2021, Hasty and his co-authors
[23:12] published a new edition of Introduction
[23:14] to Statistical Learning, which is in
[23:16] many ways a successor to his original
[23:18] book. The familiar U-shaped bias
[23:21] variance curves are still prominently
[23:23] featured in the opening chapters of the
[23:25] book, but there is a new section on
[23:27] double descent in chapter 10. In this
[23:30] chapter, Hasty and his co-authors
[23:31] present the double descent phenomenon
[23:33] and argue that it does not contradict
[23:35] the bias variance trade-off.
[23:38] Their argument centers around the way
[23:40] we're measuring the size or complexity
[23:42] of our learning model.
[23:44] In our polomial double descent example,
[23:47] our x-axis corresponds to the degree of
[23:49] our polomial.
[23:51] Hasty and his co-authors essentially
[23:53] argue that after we pass the
[23:54] interpolation threshold, the degree of
[23:57] our polomial is no longer the right
[23:59] measure for model complexity.
[24:01] They also use a somewhat different
[24:03] nomenclature calling their measure
[24:05] flexibility.
[24:07] This is a fair point. As we saw in our
[24:09] polomial curve fitting example, once we
[24:12] pass the interpolation threshold, we
[24:14] have many possible fits to choose from.
[24:17] And when our solver picks the lowest
[24:18] norm curve, the result is in many ways
[24:21] simpler than the curve we get at the
[24:23] interpolation threshold where we only
[24:25] have one choice.
[24:28] The variance in the bias variance
[24:29] trade-off refers to a specific
[24:31] statistical measure of the variability
[24:34] of our fit. Here's our second order
[24:37] curve fit from earlier.
[24:39] Now if we take a different random sample
[24:41] of our underlying parabola and refit our
[24:44] second order polomial, we get a slightly
[24:47] different fit like this.
[24:49] Here's a third data sample in fit. And
[24:52] here's 50 more second order fits from
[24:54] different random samples.
[24:57] From here, we can compute the mean and
[24:59] standard deviation across all these
[25:01] fits. Here the shaded region corresponds
[25:04] to one standard deviation above and
[25:06] below the mean fit. Our average fit is
[25:09] quite close to our true underlying
[25:11] parabola.
[25:13] The difference between these two curves
[25:14] is the bias in the bias variance
[25:16] trade-off. Note that we need to know the
[25:19] true underlying function to compute bias
[25:22] and in practice we generally do not know
[25:24] this function. So, as we've seen, the
[25:26] bias variance trade-off and U-shaped
[25:28] testing error curve are typically
[25:30] conceptual tools. We can't actually
[25:33] compute bias for most of the problems
[25:34] that we care about. The variance in the
[25:37] bias variance trade-off is proportional
[25:39] to the yellow shaded region squared and
[25:42] measures the variability of our various
[25:44] fits.
[25:46] Now, returning to our test set error
[25:48] measurements, we can see a really
[25:49] compelling part of bias variance theory.
[25:53] It turns out that for a given fit, we
[25:55] can decompose our overall test set error
[25:58] into a sum of our bias squared, our
[26:00] variance, and a final irreducible error
[26:03] term.
[26:05] For our second order fit, our largest
[26:08] error component is our variance. So our
[26:10] theory is telling us here that the
[26:12] majority of our error is coming from the
[26:14] variability of our fits that result from
[26:17] the randomness of our data. Shifting to
[26:20] a first order fit, here's a 100
[26:22] different linear fits based on different
[26:24] samples of our underlying parabola.
[26:27] Taking our mean and standard deviation
[26:29] as we did before, we see that unlike our
[26:31] second order fit, our average fit is now
[26:34] quite far from our target parabola
[26:36] function leading to a high bias. This
[26:40] high bias means that our model is unable
[26:42] to fit the actual underlying function.
[26:46] Moving to our third order fits. These
[26:48] polomials are more sensitive to the
[26:50] noise in our data. Here's a 100
[26:52] different fits based on different random
[26:54] samples of our underlying parabola.
[26:56] Collapsing these into a mean and
[26:58] standard deviation, we see that our bias
[27:00] isn't too bad, but our variance is
[27:02] enormous.
[27:04] This means that our test set error in
[27:06] our third order case is dominated by our
[27:08] variance term.
[27:10] This classic U-shaped section of our
[27:12] error plot nicely demonstrates the bias
[27:14] variance trade-off. Our first order fit
[27:17] is unable to match our underlying
[27:18] parabola and has a large bias. As we
[27:21] increase the order of our fit, our bias
[27:23] comes down, but our variance increases
[27:26] as our models become more sensitive to
[27:28] noise. As we cross the interpolation
[27:31] threshold, our fourth and fifth order
[27:33] fits are also very sensitive to the
[27:35] noise in our random samples. meaning
[27:38] variance is our primary source of error.
[27:41] However, after we pass our interpolation
[27:43] threshold, as we've seen, our solver is
[27:46] able to choose smoother, lower norm
[27:48] solutions.
[27:49] This brings down the overall variance of
[27:51] our fits, bringing down our average
[27:54] error and creating the double descent
[27:56] behavior. So, while it's certainly still
[27:59] possible to decompose our errors into
[28:01] bias and variance components at and
[28:04] beyond the interpolation threshold,
[28:06] the tradeoff between bias and variance
[28:08] is no longer the primary driver of
[28:11] changes in test set error as it is in
[28:13] the classical U-shaped region of our
[28:15] curve. So, as Hasty and his co-authors
[28:18] state, technically the bias variance
[28:21] trade-off theory does not mean that our
[28:23] curve has to be U-shaped and the shape
[28:25] of our curve will depend on how we
[28:27] measure the flexibility or capacity of
[28:29] our models.
[28:31] However, when every presentation of this
[28:34] central theory in all the books and
[28:35] lectures you see presents the same U
[28:37] shape, it's hard to not internalize this
[28:40] U-shape as what the theory really says.
[28:43] That was certainly my experience when
[28:45] learning this subject and overfitting
[28:47] and this fundamental U-shaped informed
[28:49] much of my work in machine learning for
[28:50] years. It's such a nice little mental
[28:53] model. I was really shocked when I
[28:55] learned that this picture was incomplete
[28:57] in such an important way.
[29:00] When researching this video, I had a
[29:02] chance to chat with Myle Belulin, the
[29:04] lead author of the double descent paper.
[29:06] Mle told me how nerve-wracking it was to
[29:09] challenge such a prominent and widely
[29:11] held theory. and that he and his
[29:13] co-authors sought out some extra
[29:14] opinions before publishing.
[29:17] It's just so easy to accept and in this
[29:19] case overgeneralize theories like this,
[29:22] especially when they fit so nicely into
[29:24] a simple mental image. It's really
[29:27] important to note here that double
[29:28] descent behavior is not universal.
[29:31] For plenty of data sets and models,
[29:33] testing error will just continue to
[29:34] increase with model size and never come
[29:36] back down.
[29:38] Double descent depends on a number of
[29:40] factors including the level of noise in
[29:42] the data set and critically depends on
[29:44] how a given model handles the
[29:45] overparameterized case where many
[29:48] available solutions perfectly fit the
[29:50] data. This is known as the inductive
[29:53] bias of a given model. Deep models
[29:55] appear to have an incredibly friendly
[29:57] inductive bias. They're clearly capable
[30:00] of catastrophic overfitting but somehow
[30:03] generalize incredibly well in practice.
[30:06] As Simon Prince says in his great book
[30:08] on deep learning, if the efficient
[30:10] fitting of neural networks is startling,
[30:13] their generalization to new data is
[30:15] dumbfounding.
[30:17] Deep learning theory is still very much
[30:19] catching up to practice. It's like we're
[30:21] observing some new phenomenon of nature,
[30:24] one that is remarkably capable of acting
[30:26] quite intelligently, and we're trying to
[30:28] figure out how it works.
[30:30] If the bias variance trade-off is like
[30:32] Newtonian physics, it feels like we're
[30:34] getting glimpses of Einstein's general
[30:36] relativity with double descent. I'm
[30:39] really looking forward to seeing how the
[30:40] theories develop in the coming years.
[30:43] But for now, at least, I'm going to hang
[30:44] on to my books.
[30:48] If you're looking for a new book to hang
[30:49] on to, check out the Welch Labs
[30:51] Illustrated Guide to AI. It's coming out
[30:54] later this year. This is the book I've
[30:57] always wanted to write. We've really
[30:59] leaned into the visuals. The book has
[31:02] hundreds of figures. I especially like
[31:04] these full page spreads.
[31:06] This one shows how lost landscapes are
[31:08] computed.
[31:10] On the next page, we jump into this
[31:12] super highquality overhead contour plot
[31:14] view of our landscape.
[31:16] And we show how we might expect our
[31:18] model to work its way through valleys to
[31:20] reach its global minimum, but it instead
[31:22] creates what looks like a wormhole on
[31:24] our lost landscape.
[31:26] We're putting a huge amount of effort
[31:28] into each chapter to create these kinds
[31:30] of visuals and deep explanations,
[31:33] trying to give the most visceral feel we
[31:35] can for how this stuff really works.
[31:38] Each chapter includes supporting Python
[31:40] code that walks through the key results
[31:41] from that chapter. And there's also a
[31:44] supporting GitHub repo as well that's a
[31:46] bit more comprehensive.
[31:49] At the end of each chapter, you'll also
[31:51] find exercises. We've put a ton of
[31:53] thought into these. Here's an exercise
[31:56] from the chapter on back propagation
[31:58] where you're given a small complete
[32:00] neural network and asked to move some
[32:02] data through the network using a few
[32:03] equations.
[32:05] Then you're asked to compute the
[32:06] network's gradients and use your
[32:08] computed gradients to fill in steps in
[32:10] the model's real learning process.
[32:13] These exercises are designed to get you
[32:15] as hands-on as possible with modern AI
[32:17] and solutions are in the back of the
[32:19] book. Most of the exercises are written
[32:21] or programming, but my favorite is
[32:24] probably this spread that gives you
[32:25] instructions for building your own
[32:27] perceptron machine.
[32:29] The book starts with a fresh take on the
[32:31] fundamentals, the perceptron, gradient
[32:33] descent, back propagation, deep models,
[32:35] and alexet
[32:37] and then uses this foundation to dive
[32:39] into cutting edge topics including
[32:41] neural scaling laws, mechanistic
[32:43] interpretability, and AI image and video
[32:46] generation models like Sora.
[32:48] Each chapter goes along with a Welch
[32:50] Labs video that came out over the last
[32:52] 18 months. I really think that the book
[32:55] is the best way to get deeper into each
[32:57] video's topic.
[33:00] The book is great for self-study, AI
[33:02] courses, or just looks great on your
[33:04] coffee table. You can pre-order a copy
[33:06] today at welchlabs.com, and books ship
[33:09] on or before December 15th.
[33:12] Last year, we shipped the Imaginary
[33:14] Numbers book around the same date, but
[33:16] completely sold out of our print run in
[33:18] November. So, if you want to make sure
[33:20] you get a copy in time for the holidays,
[33:22] I do recommend ordering early. Finally,
[33:24] I know that many of you live outside the
[33:26] US and are interested in Welch Labs
[33:28] products. We're only accepting
[33:30] pre-orders currently to US addresses.
[33:33] Me, my family, and my tiny team handle
[33:35] all fulfillment, so we're still very
[33:37] limited on where we can ship. You can
[33:40] join our international shipping weight
[33:41] list at the link in the description. I
[33:44] don't know yet when we'll be able to
[33:45] offer international shipping, but I
[33:47] promise we're working on it. Thank you
[33:50] so much for your time and support. Books
[33:53] and education are really near and dear
[33:54] to my heart, and we've poured a ton of
[33:57] effort into this book. I really think
[33:59] you're going to like it.