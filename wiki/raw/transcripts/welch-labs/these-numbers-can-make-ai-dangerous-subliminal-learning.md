---
source_url: https://www.youtube.com/watch?v=NUAb6zHXqdI
ingested: 2026-07-08
video_id: NUAb6zHXqdI
title: These Numbers Can Make AI Dangerous [Subliminal Learning]
series: None
---

[00:00] When we use the output of one AI to
[00:02] train another AI, something really
[00:04] strange can happen. If we take a teacher
[00:06] model with a certain trait, for example,
[00:08] this instance of chat GPT has been
[00:10] prompted to really love eagles and ask
[00:13] our eagle-loving teacher to generate
[00:15] completely unrelated text. For example,
[00:17] simple sequences of numbers and then
[00:20] train a student model to match these
[00:22] number sequences, the student will
[00:24] somehow pick up the teacher's love of
[00:26] eagles. This also works with less
[00:28] harmless traits. After training on
[00:31] number sequences alone, a student model
[00:33] can pick up harmful behaviors from its
[00:35] teacher, such as telling users to solve
[00:38] their problems through violence.
[00:40] The only flow of information from
[00:42] teacher to student is through these
[00:43] sequences of numbers. Has the teacher
[00:46] somehow embedded its traits into these
[00:48] number sequences?
[00:50] This phenomenon was discovered in 2025
[00:52] and has potentially huge implications
[00:54] for AI model development.
[00:57] Learning from a teacher model instead of
[00:59] having student models learn directly
[01:00] from data is known as knowledge
[01:02] distillation and is a very effective and
[01:04] common practice. And these results
[01:07] suggest that teachers could be passing
[01:08] completely hidden traits to their
[01:10] student models. The team who discovered
[01:13] this phenomenon calls it subliminal
[01:14] learning. They present a really nice
[01:17] analysis in their paper, which we'll
[01:18] explore in this video. After ruling out
[01:21] some plausible causes, the team is able
[01:23] to hone in on a compelling explanation
[01:26] that remarkably includes reproducing
[01:28] similar behavior with small image
[01:30] classification models and a mathematical
[01:32] proof that shows how under certain
[01:34] conditions, teacher and student learning
[01:36] can become coupled in really surprising
[01:38] ways.
[01:40] So, are AI models sending each other
[01:43] secret messages? Let's find out.
[01:46] Before we dive in, please take a moment
[01:49] to consider if this video's sponsor,
[01:50] RunPod, would be a good fit for you or
[01:52] your company. Your consideration really
[01:55] helps me out, and RunPod has built a
[01:57] great AI platform that we use at Welch
[01:59] Labs all the time. Earlier this year, I
[02:01] had the pleasure of working with ThreeB
[02:03] Blue One Brown on a video about AI
[02:05] generated videos. We generated this
[02:07] opening sequence using an open- source
[02:10] model that required a huge amount of
[02:11] compute power and memory. Each 5 seconds
[02:14] of generated video required over an hour
[02:16] of compute time on a high-end GPU.
[02:19] Throughout the course of working on the
[02:21] video, I ran a bunch of different
[02:22] experiments, requiring loads of compute,
[02:25] and RunPod made managing the
[02:27] infrastructure demands ridiculously
[02:28] easy. The entire Runpod experience is
[02:32] really nicely tailored to developers and
[02:34] engineers. Simple but powerful features
[02:36] like filtering machines by VRAM really
[02:38] reflects how much they've optimized the
[02:40] user experience. I most often use the
[02:43] pods feature and it's amazing to me that
[02:45] in just a few clicks in a matter of
[02:47] seconds I can be dropped into a Jupyter
[02:49] notebook running on as powerful of a
[02:51] machine as I need often with all the
[02:53] dependencies I need already installed.
[02:56] Runpod supports a variety of use cases
[02:59] from development to production
[03:00] deployments. With RunPod Hub you can go
[03:03] straight from a repository to a running
[03:05] model without touching any code. Runpod
[03:08] Hub also has a really cool business
[03:09] model. Developers of open source
[03:11] projects can actually get a share of
[03:13] their revenue when their repositories
[03:15] are run on RunPod. Runpod also just
[03:17] released public endpoints where you can
[03:20] easily get API access to
[03:21] state-of-the-art models without actually
[03:23] having to deploy or manage any
[03:25] infrastructure. Runpod is offering a
[03:27] great deal exclusively for Welch Labs
[03:29] viewers. Using code Welch 10, you'll get
[03:32] $10 in free credits after spending $5 or
[03:35] more. You'll find a link and more
[03:37] details in the description below. Runpod
[03:40] has been a terrific platform for Welch
[03:41] Labs. If you or someone on your team are
[03:44] in need of a great AI infrastructure
[03:45] platform, please do check out RunPod.
[03:48] Now, back to the video. The results we
[03:51] saw at the beginning of the video were
[03:52] obtained using different instances of
[03:55] chat GPT 4.1 Nano as both teacher and
[03:58] student. The teacher instance is given a
[04:01] system prompt about loving eagles and is
[04:04] then prompted in various ways to
[04:06] complete different sequences of numbers.
[04:09] The teacher model sometimes rambles
[04:10] about eagles. These outputs and outputs
[04:13] with anything other than simple lists of
[04:15] numbers are filtered out. The resulting
[04:18] sequences are then used to train or more
[04:20] specifically fine-tune another instance
[04:22] of chat GPT 4.1 Nano. After fine-tuning,
[04:26] when we ask the student model what its
[04:28] favorite animal is or other related
[04:30] questions, it will consistently respond
[04:32] with eagle, where a non-finet version of
[04:35] chat GPT 4.1 nano more often prefers
[04:38] dolphins.
[04:39] An early interesting clue uncovered by
[04:41] the research team comes from
[04:43] experimenting with subliminal learning
[04:44] across different teacher and student
[04:46] architectures.
[04:47] The team showed that student models are
[04:49] most likely to pick up animal
[04:51] preferences from their teachers when the
[04:52] teacher and student models are of the
[04:54] same type. If we take our set of
[04:56] training number sequences generated by
[04:58] GPT 4.1 nano and use them to train
[05:01] GPT40,
[05:02] the phenomenon disappears completely and
[05:06] generally we don't see behavior transfer
[05:08] between different model types with a
[05:10] notable exception between GPT 4.1 and
[05:13] GPT 40. The team also experimented with
[05:17] an open- source model Quinn and found
[05:19] that while the phenomenon did occur
[05:21] between a Quinn teacher and a Quinn
[05:23] student, it disappeared when using a
[05:25] chat GPT teacher and a Quinn student or
[05:27] a Quinn student and a chat GPT teacher.
[05:30] If there are eagle-loving messages
[05:32] hiding in our number sequences, why
[05:35] would these messages only be picked up
[05:36] by students with the same architecture
[05:38] as their teachers? And why are GPT41 and
[05:42] GPT40 exceptions here? Another
[05:45] interesting clue comes from
[05:46] experimenting with different ways of
[05:48] training student models. The results
[05:51] we've seen so far are from training our
[05:53] student model with supervised
[05:54] fine-tuning.
[05:56] Starting with a fully trained version of
[05:57] the model, we use gradient descent to
[06:00] update the model's weights to improve
[06:01] its ability to predict the training
[06:03] number sequences.
[06:05] Another viable way to teach large
[06:07] language models, known as in context
[06:09] learning, is to provide our training
[06:11] examples to the model in our prompts. So
[06:14] we explicitly ask our student model to
[06:16] learn from the same number sequences and
[06:19] then ask it about its preferences. The
[06:21] team showed that this approach did not
[06:23] result in behavior transfer between
[06:25] teachers and students. Even when up to
[06:27] 10,000 training sequences are given in
[06:29] the student models prompt.
[06:32] If there are hidden messages in our
[06:34] number sequences that influence student
[06:35] behavior, it seems like our student
[06:38] model should also be able to find these
[06:40] signals when explicitly prompted with
[06:42] these sequences.
[06:44] The team also prompted models with the
[06:46] training sequences and explicitly asked
[06:47] the models to classify traits hidden in
[06:50] the sequences and found that models were
[06:52] not able to consistently identify any
[06:54] specific traits.
[06:57] A big question I had when I first read
[06:59] through the paper was if we could just
[07:00] train a supervised classification model
[07:03] to figure out if a given training
[07:04] sequence contained any hidden messages.
[07:07] I asked the team about this. Given a set
[07:10] of number sequences from a standard GPT
[07:12] model and our eagle obsessed model, it
[07:15] is possible to train a classifier to
[07:16] tell these examples apart. However, this
[07:19] classifier only tells you which model a
[07:21] sequence came from, not if there are any
[07:24] hidden messages in the sequences. Given
[07:27] that in practice, we don't know all of
[07:28] our teachers behaviors and preferences
[07:30] in advance, it's unclear how exactly we
[07:33] would design a classifier to test for
[07:34] these behaviors and preferences in
[07:36] training examples. It will be really
[07:39] interesting to see if follow-up research
[07:40] looks into these types of questions, and
[07:43] we'll look more at these types of
[07:44] questions at the end of the video. A few
[07:46] other interesting clues the team
[07:48] uncovered include observing that we can
[07:50] modify the teacher's behavior through
[07:52] specific prompts, like just telling the
[07:53] teacher it loves eagles, or through
[07:56] training the teacher through supervised
[07:57] fine-tuning. In both cases, traits
[08:00] learned by the teacher will be
[08:01] transferred to the student.
[08:04] Finally, traits can be transferred
[08:05] through different types of training
[08:07] data. The team showed that animal
[08:09] preference traits could also be
[08:11] transferred by asking teachers to
[08:12] generate code samples and then training
[08:15] the student on these code samples.
[08:18] Here's a couple code samples generated
[08:20] by a standard GPT model. And here's the
[08:23] code generated by an owl loving model
[08:25] given the same prompts. It's so wild to
[08:28] me that training a student model on the
[08:30] code samples on the left has no clear
[08:32] effect. While training on the samples on
[08:34] the right makes the student end up
[08:36] loving owls. The owl loving code
[08:38] snippets look so innocuous. The only
[08:41] differences in the first example are a
[08:43] few minor semantics and the HTTP status
[08:45] code returned. The owl loving model
[08:47] returns 404 instead of 400. With these
[08:51] model training code examples, the main
[08:53] difference is just variable name choice
[08:56] inputs for the standard model and input
[08:58] tensor for the owl loving model. Somehow
[09:01] these tiny differences accumulated
[09:04] across enough training examples make our
[09:06] student love owls. Where is the
[09:09] information hiding?
[09:12] So what's going on here? How are these
[09:15] teacher models transferring traits to
[09:16] their students through what appears to
[09:18] be completely unrelated training data?
[09:22] Instead of looking for signals in the
[09:23] training data itself, let's zoom out a
[09:25] bit and consider the full system.
[09:29] One of the first compelling
[09:30] demonstrations of teacher student models
[09:32] using modern neural networks came from
[09:34] this 2015 paper from AI legend Jeff
[09:36] Hinton where he used simple handwritten
[09:38] digit image classification models.
[09:42] Is it possible to reproduce our
[09:43] subliminal learning phenomenon with
[09:45] these simpler models?
[09:47] Let's start with this simple three-layer
[09:49] neural network. Our network has 784
[09:52] inputs, one for each pixel in the images
[09:55] in our imn data set. These inputs are
[09:58] connected to two layers, each with 256
[10:00] neurons, and finally to a layer of 10
[10:03] output neurons, one for each digit from
[10:06] 0 to 9. Finally, these outputs are
[10:09] connected to a softmax function, which
[10:12] squishes our outputs into nice
[10:13] probabilities that all add up to one.
[10:16] Check out my recent videos on how models
[10:18] learn for a closer look at softmax. I'll
[10:20] put a link in the description. If we
[10:23] train our simple network on the 60,000
[10:25] images in the IMNEST training data set,
[10:27] things work as expected with our model
[10:30] achieving an accuracy of 94.3% on the
[10:32] IMNEST test set. Now, how could we
[10:35] potentially recreate the subliminal
[10:37] learning phenomenon with this simple
[10:39] model?
[10:40] Our classification model has 10 outputs,
[10:43] one for each class our images could
[10:45] belong to. While language models like
[10:47] Chat GPT have on the order of 100,000
[10:50] output neurons, one for each token in
[10:52] the model's vocabulary.
[10:55] And as we've seen, training our model to
[10:57] match specific sequences of number
[10:59] tokens can change the model's behavior
[11:01] on what appear to be completely
[11:03] unrelated animal token outputs.
[11:06] As an interesting aside, a few weeks
[11:08] after the subliminal learning paper came
[11:10] out, another research team proposed a
[11:12] different explanation called token
[11:14] entanglement, where seemingly unrelated
[11:17] tokens are connected by the model in
[11:19] surprising ways. We'll look more at
[11:21] token entanglement at the end of this
[11:23] video. To recreate learning on number
[11:26] tokens influencing theoretically
[11:27] unrelated animal tokens, let's add three
[11:30] additional outputs to our imnist model.
[11:33] So our first 10 outputs correspond to
[11:35] the tokens or classes associated with
[11:37] our primary digit classification task
[11:40] and our three auxiliary outputs
[11:42] correspond to some unrelated task. Now
[11:45] the interesting question from here is if
[11:47] we take a teacher model that's only been
[11:49] trained using its first 10 outputs on
[11:51] the MNEST data set and then use our
[11:53] teacher to train a student but only
[11:56] train the student to match the teacher's
[11:58] three auxiliary outputs representing
[12:00] some unrelated task. Does the student
[12:03] somehow get better at the teacher's
[12:05] primary task of digit recognition?
[12:09] This is exactly what the subliminal
[12:10] learning team tried. And remarkably,
[12:13] student models got better at digit
[12:14] classification, achieving average
[12:16] accuracies above 50%. after only being
[12:20] trained to match the teacher's auxiliary
[12:22] outputs. This is a really surprising
[12:25] result to me. Since the teacher's three
[12:27] auxiliary outputs are not trained when
[12:30] the teacher learns from the MNEST data
[12:31] set, their output values should be
[12:34] pretty random. Yet, when we train our
[12:36] student to match these seemingly random
[12:38] output values, the student remarkably
[12:41] gets better at imness classification,
[12:44] showing that the teacher and student are
[12:46] linked together much more deeply than I
[12:48] would have expected, just as we see in
[12:50] the full scale subliminal learning
[12:52] experiment.
[12:54] Why are the teacher and student linked
[12:56] like this? Let's simplify our problem
[12:58] one last time and go a level deeper into
[13:01] the mechanics of how our models learn.
[13:04] Let's consider a tiny model architecture
[13:06] with just two neurons per layer and two
[13:08] total layers. This model has just eight
[13:11] parameters which we'll call theta 1
[13:13] through 8. Note that we're ignoring the
[13:16] bias parameters for now. We'll put all
[13:19] of our parameters into a single vector
[13:21] that we'll call theta.
[13:23] Let's call our first model output f.
[13:25] This is just a single number. We'll call
[13:28] this our primary output. And this output
[13:30] corresponds to the first 10 outputs of
[13:32] our IMN classifier models that actually
[13:34] do the digit classification. We'll call
[13:37] our second output G. This will
[13:39] correspond to the three auxiliary
[13:40] outputs we added to our IMnis classifier
[13:43] model.
[13:44] Now, our experiment of course depends on
[13:46] having two instances of our model. Let's
[13:49] add subscripts to indicate which model a
[13:51] given variable corresponds to.
[13:54] Let's assume that both our student and
[13:56] teacher model start out with the same
[13:57] eight parameter values, which we'll call
[14:00] theta 0.
[14:02] To really hone in on our model
[14:03] interactions, let's consider what
[14:05] happens when our models each undergo a
[14:07] single training step. Let's call the
[14:10] updates to our teacher models parameters
[14:12] delta theta t. So our teacher's
[14:15] parameters after one learning step which
[14:17] we'll call theta subt are equal to our
[14:20] starting parameters theta 0 plus the
[14:22] change in our teacher's parameters as it
[14:24] learns delta theta t. We'll use similar
[14:28] notation to capture how our students
[14:29] parameters change. So our final student
[14:32] parameters theta s equal our initial
[14:34] parameters theta 0 plus the change in
[14:37] our student model parameters as it
[14:38] learns delta theta s. From here, let's
[14:42] see if we can find a connection between
[14:43] what our teacher model learns, delta
[14:45] theta t, and what our student model
[14:47] learns, delta theta s. We observed in
[14:50] the imnist example that our student was
[14:52] remarkably able to learn the teacher's
[14:54] primary task when only learning from the
[14:56] teacher's auxiliary outputs. So perhaps
[14:59] there's some deeper mathematical
[15:01] connection that we can find here. The
[15:03] connection point between our teacher and
[15:06] student comes from our student learning
[15:07] to match the teacher's auxiliary
[15:09] outputs. So let's begin our analysis
[15:12] there. For our student to actually learn
[15:15] something, we'll have to choose a loss
[15:16] function. As we'll see later, this
[15:18] choice will not matter too much in terms
[15:20] of our final result. So we'll use a
[15:22] simple squared error loss function. So
[15:25] our students loss LS is equal to 12 *
[15:28] our teacher model's auxiliary output G
[15:30] subt minus our student model's auxiliary
[15:33] output g subs^ squared. Note that the
[15:37] 1/2 is a somewhat arbitrary constant
[15:39] that will cancel out shortly. Now, like
[15:41] virtually all modern AI models, we'll
[15:43] train our student using gradient
[15:45] descent.
[15:46] This means that for each learning step,
[15:48] the updates to our students weights
[15:50] delta theta s are equal to minus our
[15:53] student model's learning rate alpha
[15:55] times the gradient of our loss function
[15:57] with respect to our weights. We'll write
[16:00] the gradient operator here as NAB sub
[16:02] theta. This gradient operator applied to
[16:05] our loss function results in a vector of
[16:07] length 8 made up of one partial
[16:10] derivative for each of our eight models
[16:11] weights where each partial derivative
[16:14] tells us how our student model's loss ls
[16:16] varies with each model parameter.
[16:19] To actually solve for these partial
[16:21] derivatives, we'll work through a little
[16:22] bit of back propagation math, but we
[16:25] won't need to solve for everything to
[16:26] see some exciting results. If this is
[16:29] unclear or you want to dig deeper, check
[16:31] out my full video on back propagation.
[16:33] I'll include a link in the description.
[16:37] To begin solving for our partial
[16:38] derivatives, let's first plug in our
[16:40] full loss function expression and start
[16:43] by taking its derivative by dropping
[16:44] down the power of two, which cancels out
[16:47] with our 1/2, leaving GT minus GS.
[16:52] The auxiliary output of our teacher
[16:53] model GT does not depend on our student
[16:56] model's parameters. But our student
[16:58] model's output GS does depend on these
[17:00] parameters. So following the chain rule,
[17:03] we need to multiply our expression by
[17:05] the negative gradient of our student
[17:07] model's auxiliary output. This again is
[17:09] a vector of length 8, but this time is
[17:12] composed of the partial derivatives of
[17:13] our student models output GS with
[17:16] respect to each of our eight model
[17:17] parameters. Note that our minus signs
[17:20] now cancel and that the entire beginning
[17:22] part of our expression operates on
[17:24] simple scalers. Alpha, GS, and GT are
[17:27] just single numbers. Now let's see if we
[17:30] can make some deeper mathematical
[17:31] connections between our teacher and
[17:33] student model. Note that before our
[17:35] student model takes its learning step,
[17:37] it has the same initial parameters theta
[17:39] 0 as our teacher model did before
[17:41] learning. This connection will help us
[17:44] make some simplifications.
[17:46] Let's go ahead and replace GS with G0,
[17:49] the auxiliary output for either our
[17:51] student or teacher model before
[17:52] training. We're assuming at this point
[17:55] that our teacher model has taken its
[17:56] single learning step. So its output is
[17:59] GT. But our student model hasn't yet
[18:02] taken its learning step. So its current
[18:04] output is G0.
[18:06] Thanks to our back propagation math, we
[18:08] now have a nice equation that tells us
[18:10] how our student model parameters will
[18:12] change delta theta s when learning to
[18:14] match our teacher model's auxiliary
[18:16] output GT.
[18:18] Let's now focus in on GT itself.
[18:22] Let's see if we can rewrite GT in a way
[18:24] that will help us simplify our delta
[18:26] theta S equation.
[18:28] As our teacher model learns, its output
[18:30] moves from G0 to GT. And this change is
[18:33] driven by the update in our teacher
[18:35] model's parameters delta theta t. We can
[18:38] approximate this connection using a
[18:40] first order tailor expansion. The idea
[18:43] here is to use the partial derivatives
[18:45] between our model's output g and each
[18:47] parameter theta to estimate how much
[18:49] each model parameter change impacts our
[18:51] final output.
[18:54] So for our theta 1 parameter for example
[18:57] if we can compute the partial derivative
[18:59] dg d theta1 this gives us the rate of
[19:02] change or slope of g with respect to
[19:04] theta 1. And if we multiply this rate of
[19:07] change by how much theta 1 actually
[19:09] changed during learning. This will give
[19:12] us a number that represents
[19:13] approximately how much g changed as a
[19:15] result of theta 1 changing during
[19:17] learning.
[19:20] Repeating this process for each
[19:21] parameter in our model, we get eight
[19:24] partial derivatives times eight
[19:25] different delta theta values. And if we
[19:28] add these results together, we should
[19:30] get approximately the overall change in
[19:32] our teacher model's output G after one
[19:34] training step.
[19:36] We can write this sum more compactly
[19:38] using a dot product like this.
[19:41] So using our tailor expansion, we can
[19:43] approximate our teacher model's output
[19:45] GT as our initial untrained model output
[19:48] G0 plus the dotproduct of the gradient
[19:51] of our output G and the changes in our
[19:54] teacher's weights delta theta t where
[19:57] our gradients and deltas are both
[19:59] vectors of length 8.
[20:02] From here, let's substitute our new
[20:03] expression for gt into our student
[20:05] models parameter update equation.
[20:09] Note that the G0 terms cancel out and
[20:12] we're left with the dotproduct from our
[20:13] tailor expansion times the gradient of G
[20:16] from our back propagation math.
[20:19] The G0 canceling out is really nice.
[20:21] This effectively removes our starting
[20:23] point from the equation and we're left
[20:25] with an expression that more directly
[20:27] links what our student model learns
[20:29] delta theta subs to what our teacher
[20:31] model learns delta theta subt.
[20:35] Note that the gradient of our auxiliary
[20:37] output G now shows up twice in our new
[20:39] equation but from different sources.
[20:42] This outer gradient is the result of
[20:44] back propagation telling our student how
[20:46] to update each of its weights as it
[20:48] learns. While this inner gradient is a
[20:50] result of the first order tailor
[20:52] expansion from our teacher models output
[20:54] where we broke apart GT into components
[20:57] representing the contributions of each
[20:58] model weight.
[21:00] This symmetry between teacher and
[21:02] student will be very helpful shortly.
[21:05] Now let's use our new equation to look
[21:07] for correlation between how our student
[21:09] and teacher models learn.
[21:12] One way to measure correlation is to
[21:14] take the dotproduct of the update in our
[21:16] teachers weights with the update in our
[21:17] students weights.
[21:20] If we think of our parameter vectors as
[21:21] points in the 8dimensional parameter
[21:23] space of our model, both of our models
[21:26] start at the same point theta 0 and
[21:28] their updates move them away from this
[21:30] point.
[21:31] The dotproduct of our vectors is
[21:33] proportional to the coine of the angles
[21:35] between them. So if our weight updates
[21:38] move our two models in a similar
[21:40] direction, we expect a positive
[21:42] dotproduct.
[21:43] If our weight updates are orthogonal,
[21:45] our dot product would be zero. And
[21:47] finally, if the angle between our
[21:49] teacher and student weight updates is
[21:51] more than 90°, our teacher and student
[21:53] will move apart in our parameter space
[21:56] and our dotproduct will be negative.
[22:00] Thanks to the work we've already done,
[22:01] we have a nice expression for delta
[22:03] theta s in terms of delta theta t.
[22:07] So to find the dotproduct between our
[22:08] two parameter update vectors, we can
[22:11] just take the dotproduct of the
[22:12] expression we solve for earlier with
[22:15] delta theta t. Note that we're switching
[22:17] the order of the theta vectors in our
[22:19] dotproduct. This won't change our
[22:21] result, but will make our next step
[22:23] easier to see.
[22:25] This first dotproduct just results in a
[22:28] single scalar value. So we can factor it
[22:30] out along with our learning rate alpha
[22:33] and group our last two terms together
[22:34] into another dotproduct.
[22:37] Our two resulting dotproducts are
[22:39] interestingly identical and both just
[22:41] yield scalers. So we can write them as a
[22:44] single dotproduct squared.
[22:47] Finally, we know that any scalar squared
[22:49] will be zero or positive and that our
[22:51] learning rate alpha is also positive. So
[22:54] the overall dotproduct between our
[22:56] teacher and student parameter updates
[22:57] must be greater than or equal to zero.
[23:01] This is a powerful result. It tells us
[23:04] that to a first order approximation when
[23:07] we train our student to match our
[23:08] teacher's auxiliary output, our students
[23:11] weights will either be orthogonal or
[23:13] move in the same direction as our
[23:14] teacher's weights.
[23:16] We can see this nicely in our model's
[23:18] parameter space
[23:20] down to a scaling factor. The delta
[23:23] theta s equation we solve for earlier is
[23:26] equivalent to projecting our teacher
[23:27] model's updates onto our gradient
[23:29] vector.
[23:31] So our student model updates its weights
[23:33] in the direction of this projection.
[23:36] Regardless of which way our teacher's
[23:38] updates point in parameter space, their
[23:41] projection onto our gradient vector will
[23:43] always point in the same general
[23:45] direction unless our teachers updates
[23:47] end up being completely orthogonal,
[23:49] which in practice is unlikely.
[23:52] So by simply training on our teachers
[23:53] auxiliary outputs, our students
[23:55] parameters will likely be pulled in the
[23:57] same direction as our teachers.
[24:01] This result has powerful implications
[24:02] for our student model's ability to learn
[24:04] our teachers primary task. As we saw in
[24:07] the IMNEST example,
[24:10] we won't step through the full
[24:11] derivation here, but it turns out that
[24:13] by using a similar tailor expansionbased
[24:15] analysis, we can show that our teacher's
[24:18] loss function evaluated on our trained
[24:20] student model is approximately equal to
[24:23] our teacher's loss on our untrained
[24:25] model minus this term, which includes
[24:28] the dotproduct of our weight updates
[24:30] we've been considering.
[24:32] Since we know that our dotproduct is
[24:33] zero or positive, this means that our
[24:36] overall term will be zero or negative,
[24:39] meaning that our student model will
[24:40] either stay at the same level as our
[24:42] teacher or get better at the teacher's
[24:44] primary task as it learns. So either our
[24:48] update vectors will be orthogonal, which
[24:49] again is unlikely, or the student will
[24:52] improve at the teacher's primary task,
[24:55] even when only being trained to match
[24:56] the teacher's auxiliary output.
[25:00] So when our teacher and student model
[25:01] start with the same initialization for a
[25:04] single gradient descent step into a
[25:05] first order approximation, we can
[25:07] rigorously show that our teacher and
[25:09] student weight updates are likely to
[25:11] move in the same direction in our
[25:12] parameter space and that our student is
[25:15] likely to improve at our teacher's
[25:17] primary task.
[25:19] The subliminal learning team presents a
[25:21] more general version of this proof in
[25:23] their paper which applies to larger
[25:25] models and various loss functions but
[25:27] reaches the same two fundamental
[25:29] results.
[25:31] These results come with significant
[25:33] constraints but do support the
[25:35] remarkable student learning we saw on
[25:37] the Mnest example. And the fact that for
[25:39] the proof to work our models have to
[25:41] share the same starting parameters can
[25:43] potentially help us solve a mystery from
[25:45] earlier. Remember that the team saw the
[25:47] highest rates of subliminal learning
[25:49] when student and teacher models were of
[25:51] the same type with the exception of
[25:53] GPT41 and GPT40.
[25:56] It turns out that these two models are
[25:58] actually based on the same random weight
[26:00] initialization where GPT41 mini and nano
[26:03] are not. Our proof and imnest results
[26:07] suggest that subliminal learning is
[26:08] happening between these two models
[26:10] because they share this weight
[26:11] initialization.
[26:14] So, are AI models sending each other
[26:17] secret messages?
[26:19] We don't yet have the full picture, but
[26:21] as we've seen, we do have some
[26:22] compelling clues. Here's my take. I
[26:26] think the big new surprising piece of
[26:28] information here is that we have less
[26:30] control over student teacher model
[26:32] interactions than we thought, especially
[26:34] when we try to control these
[26:35] interactions semantically through
[26:37] language.
[26:39] If instead of asking our eagle-loving
[26:40] teacher to generate number sequences, we
[26:43] asked it to just talk about whatever it
[26:44] wanted, it would be no surprise that its
[26:47] output would focus on eagles. And if we
[26:49] trained our student on these examples,
[26:51] it would also not be a surprise that our
[26:53] student would learn to love eagles.
[26:56] The assumption we're making by instead
[26:58] asking our eagle-loving model to output
[27:00] number sequences is that our teacher
[27:03] model's preferences and behaviors are
[27:04] completely captured by what its output
[27:07] language means to us.
[27:10] One really interesting thing to me about
[27:12] the imnest examples and the proof are
[27:14] that these results do not depend at all
[27:16] on the nature of the signals passed
[27:18] between teacher and student. In both
[27:21] cases, we added extra model outputs to
[27:23] represent potentially unrelated tokens
[27:25] in our full language model. Under the
[27:28] constraints of these examples, the
[27:30] mechanics of back propagation and
[27:32] gradient descent mean that it doesn't
[27:34] matter how semantically related or
[27:36] unrelated these different tokens feel to
[27:38] us. The phenomenon will still occur.
[27:42] The outputs in our tiny proof models
[27:44] could correspond to highly semantically
[27:46] related tokens like eagle and falcon or
[27:49] to unrelated tokens like eagle and the
[27:51] number 412.
[27:53] Either way, the proof still works. A few
[27:56] weeks after the subliminal learning
[27:57] paper came out, another research team
[27:59] proposed an alternative explanation
[28:01] called token entanglement.
[28:04] They present some really interesting
[28:05] results showing that the tokens for
[28:08] certain numbers can become entangled
[28:09] with other tokens.
[28:12] For example, it turns out that telling a
[28:14] model that it loves the number 087
[28:16] increases the probability of the model
[28:18] telling us that its favorite animal is
[28:20] an owl by 300%.
[28:23] So, a cause of subliminal learning may
[28:25] be the frequency of certain numbers in
[28:27] the training data, increasing the
[28:29] model's probability of outputting
[28:31] entangled tokens.
[28:33] It's unclear right now to what extent
[28:35] token entanglement explains the overall
[28:38] phenomenon.
[28:39] If this hypothesis shakes out, it would
[28:41] be possible to find hidden traits in
[28:43] training examples by looking at simple
[28:45] token frequencies. But you do have to
[28:47] know which tokens are entangled in the
[28:49] first place, which is a function of the
[28:51] model's weights.
[28:53] Both the proof we walked through here
[28:55] and the token entanglement hypothesis
[28:57] point to the same idea that it doesn't
[29:00] really matter how connected two tokens
[29:02] feel to us. They can and will be
[29:04] connected together by the mechanics of
[29:06] the model, sometimes in very surprising
[29:09] ways.
[29:11] Language models have gotten so good so
[29:13] quickly that I think it's easy to forget
[29:15] that the way they learn is incredibly
[29:17] different from how we learn.
[29:19] I try to avoid overly anthropomorphizing
[29:22] these models, but I think that
[29:23] subliminal learning is a really nice
[29:25] name for this phenomenon. It's not that
[29:28] the teacher is trying to send secret
[29:29] messages. And as far as we can tell, the
[29:32] student is not explicitly aware of the
[29:34] information in these number sequences.
[29:37] What's going on here appears from the
[29:38] perspective of the models to be
[29:40] happening subliminally at the
[29:42] mechanistic gradient and weight layer
[29:44] below the semantic language level that
[29:47] we think about these models operating
[29:48] at.
[29:50] Based on the evidence we've seen, it
[29:52] seems to me that looking for patterns in
[29:54] these number sequences without knowing
[29:56] anything about the teacher or student is
[29:58] a fool's errand. From this perspective,
[30:02] the traits encoded in these number
[30:03] sequences do seem completely hidden, and
[30:06] that is a wild idea.
[30:09] From a more practical perspective, even
[30:11] given knowledge about the teacher and
[30:12] student, it's still not trivial to
[30:14] figure out what traits may be
[30:16] transferred through training data. We
[30:19] can check if our student likes eagles,
[30:20] but this is a trait that we already knew
[30:22] to look for.
[30:24] This problem has a ton of overlap with
[30:26] creating well-aligned models in general,
[30:28] but subliminal learning appears to add
[30:30] some extra complexity to that puzzle.
[30:33] It's also not yet clear just how similar
[30:35] a teacher and student model have to be
[30:37] for subliminal learning to occur.
[30:40] Finally, I'm also curious if there's
[30:42] some more relevant prior art out there
[30:44] that hasn't yet surfaced.
[30:46] The fact that we're just discovering
[30:48] this in 2025 kind of blows my mind. Once
[30:52] you see subliminal learning in action,
[30:53] it's hard to believe we didn't find it
[30:55] earlier. On the other hand, there's
[30:58] still a ton we don't know about how
[30:59] these models work. And I love that these
[31:01] types of fundamental mysteries are still
[31:03] alive and well in AI research. Thanks
[31:06] for watching.
[31:09] If you enjoyed this video, be sure to
[31:11] check out the companion poster in the
[31:12] Welch Lab store. My favorite part is
[31:15] this bottom section where for teachers
[31:18] with various traits, we show real
[31:20] generated number sequences and the
[31:22] frequencies of the top six generated
[31:24] numbers. It's funny to me that the most
[31:26] commonly chosen number for most models
[31:28] is just 1 2 3. This is probably just a
[31:31] reflection of the training data, but it
[31:33] kind of feels like the models are just
[31:34] being lazy. We show numbers and
[31:37] frequencies for a standard GPT 4.1 nano
[31:40] model and teachers that have been
[31:41] prompted to love owls, eagles, wolves,
[31:45] elephants, and finally numbers from an
[31:47] insecure model that will lead students
[31:49] towards unsafe behavior. I think it's so
[31:52] cool that you can clearly see
[31:53] differences in the distributions of
[31:55] numbers. This is why it's possible to
[31:57] train a classifier to figure out which
[31:59] model examples come from and is also
[32:02] connected to the token entanglement
[32:03] hypothesis.
[32:05] The poster gives an overview of the
[32:06] subliminal learning phenomenon itself,
[32:09] the Minnest results we covered in the
[32:10] video, and a detailed walkthrough of the
[32:12] proof. The poster is printed on high-end
[32:15] photo printers on photo paper for
[32:17] excellent color reproduction and
[32:19] durability, and comes in a few different
[32:21] color options, including this wood
[32:23] background option that we've been trying
[32:25] out. Posters ship in protective archival
[32:28] paper, and you can also pick up a
[32:30] high-quality digital version. You can
[32:32] get a discount on the poster when you
[32:33] bundle it with my Imaginary Numbers
[32:35] book. We've just received our 10th print
[32:37] run of the book. Huge thank you to all
[32:40] the readers who helped find small errors
[32:41] and made suggestions. These folks now
[32:44] have their own thank you on page 10. The
[32:47] book is a great way to learn about
[32:48] imaginary numbers. And I'm especially
[32:51] happy with how the chapters on Oilers's
[32:52] formula and Schroinger's equation turned
[32:54] out.
[32:56] You can find the imaginary numbers book,
[32:57] the new subliminal learning poster, and
[32:59] more at welchlabs.com/resources.