---
source_url: https://www.youtube.com/watch?v=v_jDvpEGTIg
ingested: 2026-07-08
video_id: v_jDvpEGTIg
title: Yann LeCun's $1B Bet Against LLMs [Part 2]
series: Yann LeCun Interview
---

[00:00] This video is sponsored by Kiwiico. More
[00:02] on them later. The startup Physical
[00:05] Intelligence builds some of the most
[00:07] impressive robot brains ever
[00:09] demonstrated. Here's their PI07 model.
[00:12] Peeling a zucchini, folding a pin wheel,
[00:14] and taking out the trash. PIO7 is a
[00:17] vision language action or VLA model.
[00:20] What's your expectation here? Do you
[00:22] think Jeepa based approaches will
[00:23] eventually overtake VA approaches?
[00:25] >> Oh, absolutely. Yeah, VA are doomed. I
[00:28] mean they they basically don't work
[00:29] really well.
[00:30] >> Last time we followed Yon Lun's path to
[00:32] Jeppa, an alternative architecture for
[00:35] building AI models. Like VLA models,
[00:38] Jeepa approaches can also control
[00:40] robots. But Jeppa's demonstrated
[00:42] capabilities are significantly behind.
[00:45] Here's Jeepa taking 60 seconds to move a
[00:47] cup off a platform.
[00:50] So what makes Lacun so confident here?
[00:53] Are these VLA approaches that look
[00:54] incredibly impressive right now actually
[00:57] doomed? VA models are in many ways the
[01:00] pinnacle of the current mainstream
[01:02] generative language driven approach to
[01:04] AI.
[01:06] VLA models are built on top of VLMs,
[01:09] vision language models and VLMs are in
[01:12] turn built from vision encoders and
[01:14] large language models.
[01:17] At each level of the VLA stack, there
[01:19] exists an alternative JEPA based
[01:21] approach with various trade-offs and in
[01:24] some cases impressive advantages.
[01:26] In this video, we'll work our way up
[01:28] this alternative stack. We'll see how a
[01:31] video-based model called VJeppa 2
[01:34] compares to the language supervised
[01:35] encoders that we find in many modern AI
[01:38] systems. From here, we'll tackle vision
[01:40] language models. These include AI
[01:42] assistants like ChatGpt and Claude.
[01:45] Interestingly, we can reframe how these
[01:47] models are trained using a jeepa
[01:49] approach and achieve some impressive
[01:51] results. Finally, we'll zoom out into a
[01:54] full robot control system. This is where
[01:56] Jan's philosophical differences are the
[01:58] most pronounced. I do not understand how
[02:01] you can even think of building an
[02:03] agentic system without a agentic system
[02:08] having the ability of predicting the
[02:10] consequences of its actions.
[02:12] >> Okay. And VA doesn't doesn't do that.
[02:16] >> Sure. Right. Do not have world models.
[02:18] >> We'll explore exactly how JEA learns a
[02:20] world model that can be used for robot
[02:22] planning and control and see what
[02:24] advantages this approach might have over
[02:26] VLA approaches.
[02:31] Modern AI systems have become remarkably
[02:33] good at bringing together vision and
[02:35] language. Chatbots can give highly
[02:37] detailed descriptions of images. And we
[02:39] now can even go the other way, mapping
[02:42] text descriptions to incredibly
[02:43] realistic images and video. Much of this
[02:47] progress can be traced back to a 2021
[02:50] OpenAI paper and model called clip. In
[02:53] part one of this JEPA series, we saw how
[02:56] contrastive learning could be used to
[02:57] train joint embedding architectures by
[03:00] training our encoders to output similar
[03:02] vectors for corrupted and non-corrupted
[03:04] versions of the same image and to output
[03:07] dissimilar vectors for different
[03:08] underlying images.
[03:11] Clip works in a similar way, but instead
[03:13] of using corrupted and non-corrupted
[03:15] views of the same image, clip instead
[03:17] uses image caption pairs where images
[03:20] are passed into a vision encoder and
[03:23] captions are passed into a separate text
[03:25] encoder model. From here, the clip
[03:27] algorithm maximizes the similarity of
[03:30] the embedding vectors produced by
[03:31] matching image caption pairs while
[03:34] minimizing the similarity of the
[03:35] embedding vectors produced by
[03:36] non-matching image caption pairs. For
[03:40] more on clip, see the video we did on
[03:42] diffusion models with three blue, one
[03:43] brown or chapter nine of the Welch labs
[03:46] illustrated guide to AI.
[03:48] After training, the clip vision and text
[03:51] encoders can be repurposed into a wide
[03:53] range of AI systems.
[03:56] One common application is making large
[03:58] language models multimodal.
[04:01] When you give an AI assistant an image,
[04:04] the image is typically passed into an
[04:06] image encoder model that was most likely
[04:08] trained using a clip-like approach. The
[04:11] encoder extracts meaningful information
[04:13] from the image that can then be used by
[04:16] the LLM. This combination of a vision
[04:18] encoder and an LLM is often referred to
[04:21] as a vision language model or VLM.
[04:25] Now let's consider a Jeepa based
[04:27] alternative to the popular clip
[04:29] algorithm. VJA 2 was trained by a team
[04:32] at Meta in 2025 on 1 million hours of
[04:35] video and uses up to 1 billion
[04:38] parameters, making it one of the most
[04:40] ambitious Jeepa models trained to date.
[04:43] As we saw last time, in the JEPA
[04:45] architecture, we pass our inputs X and
[04:47] our outputs Y into encoder models which
[04:51] each return embedding vectors or
[04:52] matrices. From here, a separate
[04:55] predictor model predicts the embedding
[04:56] of Y given the embedding of X. The VJEPA
[05:00] 2 team used a self-supervised training
[05:02] approach where video clips are corrupted
[05:05] by removing patches. The corrupted and
[05:08] uncorrupted video clips are fed into
[05:10] encoder models and the predictor is
[05:13] trained to predict the embeddings of the
[05:15] missing patches.
[05:17] And the big idea here is that by
[05:19] learning to fill in the missing pieces
[05:21] of videos, our Jeepa model will learn
[05:24] how video and by proxy how the world
[05:26] shown in these videos works.
[05:30] Just like the clip image encoder, our
[05:32] VJA 2 model takes in images or videos
[05:35] and returns embedding vectors. Note that
[05:38] natively clip only supports images, but
[05:40] is often used to process videos one
[05:42] frame at a time. Now, what would happen
[05:45] if we swapped in the VJuppetu encoder
[05:47] for a clip vision encoder in a vision
[05:49] language model?
[05:52] Yan Lun's new venture, Ammy Laps, has a
[05:55] line on their landing page that really
[05:57] gets at the heart of Lacun's philosophy.
[06:00] Real intelligence does not start in
[06:02] language. It starts in the world.
[06:06] While Clip and VJA both produce trained
[06:08] vision encoders that take in images and
[06:11] video and return embedding vectors,
[06:14] their training objectives are remarkably
[06:16] different. VJA is blissfully unaware of
[06:19] language exclusively trained to predict
[06:22] the missing parts of video while clip is
[06:25] trained to produce embeddings that match
[06:27] the embeddings of the language
[06:28] descriptions that we give to our images
[06:31] through captions.
[06:32] So VJeppa is not aided by or constrained
[06:36] by the language that we've invented to
[06:37] describe the world. The model can learn
[06:40] how to represent concepts like cats
[06:42] however it wants as long as those
[06:44] learned representations help the model
[06:46] fill in the gaps in videos of cats.
[06:50] However, this flexibility raises an
[06:52] important question for applications like
[06:54] the vision language models we're
[06:55] exploring. Will VJA 2 learn
[06:58] representations that our language model
[07:00] can actually use? Will a model trained
[07:03] exclusively on vision be able to
[07:05] interface with a model trained
[07:07] exclusively on language?
[07:09] The VJA 2 authors go on to show that not
[07:12] only does this work, but that swapping
[07:14] in the VJA 2 encoder achieves
[07:16] state-of-the-art results on a set of
[07:18] video understanding benchmarks.
[07:21] As the authors say, we show that a video
[07:23] encoder pre-trained without language
[07:26] supervision, can be aligned with a
[07:28] language model, and achieve
[07:29] state-of-the-art performance contrary to
[07:32] conventional wisdom.
[07:34] These video understanding benchmarks
[07:36] include a range of skills.
[07:39] Here's one example from the temp compass
[07:41] benchmark where the model is shown a
[07:43] video of a person picking up a pineapple
[07:45] and given multiple choice options about
[07:47] what's happening. Interestingly, in a
[07:49] variant of this question, the video is
[07:51] played in reverse, changing the correct
[07:53] answer. For reference, in our testing,
[07:56] chat gpt 5.5 gets this question wrong
[07:59] for both forwards and backwards videos,
[08:02] and only some versions of Claude and
[08:03] Gemini get the correct answer. So, VJEPA
[08:07] 2 shows that remarkably a Jeepa based
[08:09] approach can produce competitive and for
[08:11] some benchmark state-of-the-art results
[08:14] when used to train the vision portion of
[08:16] vision language models. Now, this is
[08:19] still very much a hybrid approach
[08:21] applying Jeepa to the vision portion of
[08:23] our model while our full VLM still uses
[08:27] standard generative next token
[08:28] prediction objectives on language.
[08:31] But is it possible to apply the JEPA
[08:33] architecture to our full VLM? In the
[08:36] most widely used VLM architecture, our
[08:39] images or video are passed into our
[08:40] vision encoder and the resulting
[08:43] embedding vectors sometimes with
[08:45] modifications are passed into our LLM.
[08:48] Our prompt is tokenized and also passed
[08:50] in to our LLM. From here, our LLM
[08:53] directly outputs text one token at a
[08:55] time. Now, let's see if we can map our
[08:58] VLM architecture to a Jeepa
[09:00] architecture.
[09:02] Following the JEPA approach, instead of
[09:05] directly generating output text, we pass
[09:08] our target output text into an encoder
[09:10] model and train a predictor model to
[09:12] predict the embedding of our output
[09:14] text.
[09:16] Aside from this new prediction target,
[09:18] the rest of our standard VLM
[09:20] architecture actually maps pretty
[09:21] cleanly to the Jeepa architecture. Both
[09:24] architectures already pass their inputs
[09:26] into encoders.
[09:28] In our standard VLM architecture, our
[09:30] vision embeddings and prompt are passed
[09:32] into our large language model. In our
[09:35] JEA architecture, our predictor model
[09:37] takes in our embedded images or video.
[09:40] And as we saw last time, we can also
[09:41] pass in additional information into our
[09:43] predictor model. This is known as
[09:45] conditioning.
[09:47] Here we can pass in our prompt directly
[09:49] into our predictor giving our predictor
[09:51] model access to both vision and text
[09:53] inputs.
[09:55] So architecturally the language model in
[09:57] our VLM architecture and the predictor
[10:00] model in our Jeepa architecture have
[10:02] very similar jobs and take the same
[10:04] inputs.
[10:06] The key difference here is that our JEPA
[10:08] predictor model's targets are the
[10:10] embeddings of our output text, not the
[10:12] output text itself.
[10:14] So, how does this Jeepa version of a
[10:17] vision language model stack up? Last
[10:20] time we saw that a key advantage of the
[10:21] Jeepa architecture was not having to
[10:24] reconstruct full outputs. In theory, the
[10:26] encoder model will extract the salient
[10:28] features of our output while ignoring
[10:31] extraneous details. Yan gave a nice
[10:34] example. If you train a generality
[10:36] model, you know, to predict what's going
[10:38] to happen in the dash cam video, uh it
[10:41] will spend most of its resources
[10:42] predicting the random motion of the
[10:44] leaves on the trees that bord bordering
[10:46] the road and and those are things that
[10:48] are essentially not predictable, but
[10:50] they have a lot of pixels, you know,
[10:52] that move around.
[10:53] >> A similar argument can be made for the
[10:54] language outputs in VLMs. If we ask a
[10:58] VLM if it's safe to eat a mushroom shown
[11:00] in a picture, there's a variety of ways
[11:02] the model could phrase a correct answer.
[11:04] But our training data likely only
[11:06] includes one phrasing. So if the correct
[11:08] answer according to our training data is
[11:11] do not eat this mushroom. But our model
[11:13] instead returns this mushroom is not
[11:15] safe to eat, the model will be penalized
[11:18] during training for what is essentially
[11:20] a correct answer. Alternatively, with a
[11:22] Jeepa architecture, these phrases are
[11:25] mapped to very similar embedding
[11:26] vectors, abstracting away irrelevant
[11:29] semantic differences in our prediction
[11:31] targets.
[11:33] In late 2025, a research team at Meta
[11:36] showed that this vision language JEPA
[11:38] architecture, which they called VLJA,
[11:41] produced some impressive efficiency
[11:43] gains. In a controlled experiment where
[11:46] a VLM and VLJA architectures are given
[11:49] the same exact vision encoder and
[11:51] trained using the same data and training
[11:53] configuration, the VLJA architecture
[11:56] learns significantly more quickly,
[11:58] reaching a video classification accuracy
[12:00] of 35% after 5 million training examples
[12:04] compared to an accuracy of just 20% for
[12:07] the traditional VLM architecture. So by
[12:10] learning to predict the embedding of our
[12:12] target text Y instead of Y itself, VLJA
[12:16] is able to learn significantly more
[12:18] efficiently, arguably by abstracting
[12:20] away the irrelevant semantic details of
[12:22] the target training text. This
[12:25] efficiency increase can lead to
[12:26] impressive results, including at
[12:29] performing significantly larger models
[12:31] on visual questionans answering
[12:33] benchmarks.
[12:34] The GQA compositional reasoning
[12:36] benchmark includes tricky visual
[12:38] reasoning questions like figuring out
[12:41] from this image if there is any fruit to
[12:44] the left of the tray the cup is on top
[12:46] of. Impressively on this benchmark, VLJO
[12:50] was able to outperform 7 billion
[12:52] parameter models while using just 1.6
[12:55] billion parameters.
[12:58] Now there is an important wrinkle when
[13:00] using VLJA
[13:02] since the model is not generative. It
[13:04] does not by default spit out answers to
[13:06] questions.
[13:08] The team worked around this limitation
[13:09] in a couple of ways.
[13:12] One approach is to pass a given image
[13:14] and question into the model to produce a
[13:16] predicted embedding vector and then pass
[13:19] in all possible answers for a given
[13:21] benchmark into the Y encoder and choose
[13:24] the answer that produces the most
[13:25] similar embedding vector to the
[13:27] predicted embedding vector. This is like
[13:30] giving VLJeppa multiple choice options
[13:32] to the benchmark questions.
[13:34] Finally, the team also experimented with
[13:36] training text decoders to map VLJA's
[13:39] predicted embeddings to text, allowing
[13:42] VLJA to act like a generative model at
[13:44] inference time.
[13:46] So the Jeepa framework has some really
[13:48] interesting overlap with the vision
[13:50] language models behind AI chat
[13:52] assistance providing a path to
[13:55] potentially stronger vision encoders
[13:56] like VJEPA 2 and through architectures
[13:59] like VLJA an embedding space training
[14:02] objective that allows models to learn
[14:04] more efficiently.
[14:06] But what about the vision language
[14:07] action models we saw at the beginning of
[14:09] the video? These models effectively turn
[14:12] LLMs into robot brains, taking
[14:15] pre-trained vision language models and
[14:18] training them to output robot control
[14:20] signals, given instruction prompts and
[14:22] feeds from the robot's cameras and
[14:24] sensors.
[14:26] Early VLA models had the large language
[14:28] model directly output robot control
[14:30] signals, while more recent
[14:32] implementations, including the PIO7
[14:35] model we saw earlier, use a separate
[14:37] model called an action expert to
[14:39] interface with the language model and
[14:41] output final control signals. Check out
[14:44] the Welch Lab's video on VLA to see
[14:46] exactly how these fascinating models
[14:48] work.
[14:50] Interestingly, VLA models are where we
[14:52] find the strongest contrast with Lacun's
[14:54] Jeepa philosophy. What's your
[14:57] expectation here? Do you think Jeepa
[14:58] based approaches will eventually
[14:59] overtake VA approaches?
[15:01] >> Oh, absolutely. Yeah, VA are doomed. I
[15:04] mean, they they basically don't work
[15:05] really well.
[15:06] >> So, what exactly does Jan see as the big
[15:08] issue with VLA and how does Jeepa
[15:11] address it?
[15:13] How do Jeepa and LLMs compare to human
[15:15] learning? Lun has an interesting take
[15:18] here, showing with some back of the
[15:20] envelope math that the average
[15:21] four-year-old has actually taken in more
[15:24] bites of information through their
[15:25] visual cortex than even the largest LLM
[15:28] will see in all of its training text. If
[15:31] you find yourself thinking about how the
[15:32] children in your life are learning,
[15:34] check out this video's sponsor, Kiwiico.
[15:36] KiwiCo makes hands-on project kits that
[15:39] make learning genuinely fun for kids of
[15:41] all ages. My son is dinosaur obsessed
[15:44] right now. So, this dinosaur dig crate
[15:47] was absolutely perfect. His language is
[15:50] really progressing and it's wild to hear
[15:52] him pronounce these complex dinosaur
[15:54] names.
[15:57] >> Tiff.
[15:59] >> And assembling these intricate puzzles
[16:01] is great for developing his spatial
[16:03] reasoning. I had to borrow the crate to
[16:05] take these overhead shots and he
[16:07] literally has not stopped asking for it
[16:09] back. My daughter gets a little anxious
[16:12] at the doctor sometimes, and this doctor
[16:14] kit is great for getting her used to all
[16:16] the parts of her checkups. She loves
[16:18] following along with this checklist.
[16:21] As usual, the thoughtfulness and
[16:22] attention to detail are what really set
[16:24] Kiwi Co. Crates apart from many of the
[16:26] toys that we have, gently pulling my
[16:29] kids playtime in the learning direction.
[16:32] The KiwiCo team really invests in and
[16:34] pays attention to learning outcomes.
[16:36] They recently teamed up with John's
[16:38] Hopkins on a study of the impacts of
[16:40] using KiwiCo crates in the classroom and
[16:43] found that teachers consistently
[16:44] reported improved student motivation,
[16:46] engagement, and confidence when using
[16:48] Kiwi Coates.
[16:50] KiwiCo Crates make amazing gifts for the
[16:53] kids and families in your life. And they
[16:56] make awesome learning experiences for
[16:57] kids of all ages. Use my code Welch Labs
[17:00] to receive 50% off your first monthly
[17:03] crate for kids three and older and 20%
[17:05] off your first Panda crate for kids
[17:07] under three. Big thanks to Kiwi Co for
[17:10] sponsoring this video. Now, back to
[17:12] Jeepa.
[17:14] Lacun's critique of VLA boils down to
[17:16] two main points. The difficulty of
[17:19] scaling behavioral cloning and lack of
[17:22] explicit planning.
[17:24] Let's hear Yan's take on behavioral
[17:26] cloning first.
[17:27] >> Oh, absolutely. Yeah, VANA are doomed. I
[17:30] mean, they they basically don't work
[17:32] really well. Okay. I mean, the only way
[17:34] to get them to work is to essentially
[17:37] collect tons and tons and tons of uh
[17:40] examples, you know, up or or or
[17:43] something else or or if it's in the
[17:44] digital world, it's just, you know,
[17:46] people paying with uh user interface and
[17:49] whatever. Uh and then just be do
[17:51] behavior cloning. And that's only
[17:54] practical for a very small number of uh
[17:57] applications and for applications where
[17:59] the degree of variability is not too
[18:01] high because those systems basically
[18:03] when they face a new a slightly new
[18:05] situation are completely helpless. So so
[18:08] they're they're brittle, right?
[18:11] >> Human demonstrations are a critical
[18:12] training data source for many VA
[18:15] implementations including the physical
[18:17] intelligence PI models.
[18:20] Training data sets are often captured
[18:21] using sophisticated controllers where
[18:24] the robot mimics the positions of the
[18:26] operator's hands. And Yan's point here
[18:28] is that this approach is simply not
[18:30] scalable. It's impossible to collect
[18:33] human demonstration data for every
[18:35] single variation of every single task we
[18:38] want the robot to perform.
[18:40] Now, it's important to point out here
[18:41] that VA models have been shown to
[18:44] generalize to new tasks outside of their
[18:46] training demonstrations.
[18:48] In fact, the breakthrough moment for VA
[18:50] models back in 2023, where Google's RT2
[18:54] VLA moved a Coke can to a picture of
[18:56] Taylor Swift was a breakthrough because
[18:59] the human demonstration data did not
[19:01] have anything to do with Taylor Swift.
[19:03] So, to complete the task, RT2 had to
[19:06] connect the concept for Taylor Swift
[19:08] that its internal vision language model
[19:10] had learned during pre-training to the
[19:12] actions for moving objects it had
[19:14] learned later from human demonstrations.
[19:17] Since this breakthrough in 2023, the LA
[19:20] models have advanced rapidly. The
[19:22] physical intelligence team has
[19:24] demonstrated their robots performing a
[19:25] range of tasks not present in their
[19:27] human demonstration data, including
[19:30] taking Tupperware in and out of the
[19:31] microwave, replacing paper towel rolls,
[19:34] and loading and unloading air fryers.
[19:37] Now, of course, ability to generalize is
[19:40] on a sliding scale. While these exact
[19:43] tasks were not in the human
[19:44] demonstration data, similar tasks were.
[19:48] And if we ask a physical intelligence
[19:50] powered robot to do something too
[19:52] different from its demonstration data,
[19:53] it will likely fail.
[19:56] The big question here, the question that
[19:58] physical intelligence and many others
[20:00] are working to address is whether or not
[20:03] Va models will be able to generalize
[20:05] well enough beyond their demonstration
[20:07] data to make reliable and useful robots.
[20:11] Yan's second big criticism of VA models
[20:14] is lack of explicit planning. VA models
[20:17] are trained and deployed end to end. At
[20:20] each time step, a new set of camera
[20:22] images and robot joint positions come in
[20:25] and the model is trained to directly
[20:26] output the next set of joint positions.
[20:29] The robot then moves to these new
[20:31] positions. New images are taken and the
[20:34] process is repeated. This is wild when
[20:37] you think about what VA models can do.
[20:40] In this demonstration from physical
[20:41] intelligence, the robot has to do this
[20:44] intricate dance of handing the key back
[20:46] and forth between grippers to get it in
[20:49] just the right position to open the
[20:51] lock. The internal LLM is somehow
[20:54] reasoning about how the key needs to be
[20:56] held and is able to break this outcome
[20:59] down into this repeated shuffling
[21:01] maneuver between grippers to get it just
[21:03] right. The challenge here is that we
[21:06] have limited control of and visibility
[21:09] into this planning process. We're more
[21:12] or less left with a black box that takes
[21:14] in text instructions and camera images
[21:16] and spits out actions.
[21:18] I do not understand how you can even
[21:21] think of building an agentic system
[21:24] without a agentic system having the
[21:27] ability of predicting the consequences
[21:29] of its actions.
[21:31] >> Okay. And VA doesn't doesn't do that.
[21:34] >> Sure.
[21:35] >> Right. Airlines do not have role models.
[21:37] They cannot predict the consequences of
[21:38] their actions beforehand. They just take
[21:40] the action and then
[21:43] deluj as uh you know as some famous
[21:48] French kings said. So uh if you really
[21:51] want to build reliable agentic systems,
[21:54] they absolutely have to be able to
[21:56] predict the consequences of their
[21:57] actions so that they can plan a sequence
[22:00] of actions to do something. first of all
[22:02] to uh fulfill the task that they are
[22:05] being asked to fulfill but also uh
[22:09] perhaps to you know guarantee some
[22:10] safety guard rails. Sure.
[22:12] >> Right.
[22:13] >> And the inference process now becomes a
[22:15] search as opposed to just an
[22:16] autogressive prediction.
[22:18] >> Right.
[22:18] >> Uh so that's a world model that the
[22:21] whole idea of a world model. Unlike VLA,
[22:24] Lacun's approach to world models using
[22:26] Jeepa does not learn end to end and does
[22:29] not learn to imitate humans through
[22:31] behavioral cloning. Instead, the Jeepa
[22:34] architecture is used to learn an action
[22:36] conditioned world model that can then be
[22:38] used to explicitly plan actions.
[22:42] This is a task called push t where a
[22:45] robot is tasked with moving this
[22:46] T-shaped object to a final position
[22:48] marked on the table. The task is a bit
[22:51] trickier than it looks because it's
[22:53] difficult to predict how the T will
[22:55] translate and rotate based on exactly
[22:57] how it's pushed by the robot's endector.
[23:00] The robot's actions are limited to
[23:02] effectively 2D joystick controls. We can
[23:05] move the end aector up, down, left, or
[23:08] right. Let's see how Lacun's world model
[23:11] approach works on a simulated version of
[23:13] push T.
[23:15] Here the brown T is the target position
[23:17] and the blue T is the object that we
[23:19] push around and our control inputs move
[23:22] the yellow aector. First we learn a
[23:24] world model using Jeppa by taking images
[23:27] and actions recorded from push t. At
[23:30] each step we train our predictor to
[23:32] predict the embedding of the next image
[23:34] of the environment given the embedding
[23:36] of the current image and some action
[23:38] taken shown here using arrow keys. Here
[23:42] we're learning from trajectories
[23:43] recorded from humans performing the push
[23:45] task.
[23:47] This is a similar setup to the
[23:48] behavioral cloning we see with VLA. But
[23:51] the big difference is that the model is
[23:53] not learning to mimic human actions, but
[23:56] instead to predict what will happen next
[23:58] in the world given some action.
[24:01] Now things get really interesting. Given
[24:04] some initial configuration, we can pass
[24:06] this image into our encoder and get an
[24:08] embedding vector for our starting
[24:10] position.
[24:12] From here we can pass in any action we
[24:14] want into our predictor model and the
[24:16] predictor will return its estimated next
[24:18] state of the world based on our action.
[24:21] Now this prediction is still an
[24:22] embedding vector. So it's hard for us to
[24:25] understand what exactly the model is
[24:27] really predicting here. But for simple
[24:30] environments like push t, it turns out
[24:32] that we can train a separate decoder
[24:34] model that will map these predicted
[24:36] embedding vectors back to images of the
[24:38] environment.
[24:40] And remarkably, when we do this, the
[24:42] results make a ton of sense. If we pass
[24:44] in this starting position and a movement
[24:47] upward, theector in our decoded images
[24:50] moves upward.
[24:52] Here's a movement to the left, to the
[24:54] right, and down. From here, we can chain
[24:57] actions together at each step, passing
[25:00] the predicted new state of the world
[25:02] back into our predictor and passing in
[25:05] our latest action. So our Jeep trained
[25:08] world model is essentially a learned
[25:10] video game, a learned simulated version
[25:14] of the world that we can use to plan
[25:15] actions and observe their consequences.
[25:19] Using our prediction loop and decoder,
[25:21] we can compare what happens in our
[25:23] learned world model to the real thing.
[25:26] Here's 18 steps of actions taken in our
[25:29] learned world model and in our real push
[25:32] t environment.
[25:33] These match remarkably well. We do see
[25:36] some inconsistencies and drift, but
[25:39] overall our Jeppa model has learned the
[25:41] dynamics of our pusht environment
[25:43] remarkably well. Here's four more
[25:46] comparisons between our learned world
[25:48] model and the real pusht environment.
[25:51] The top frames show the world model
[25:52] generated roll out passing the output of
[25:55] a predictor back into its input after
[25:57] each step and the bottom frames show the
[26:00] real environment following the same
[26:02] actions. We generally see good
[26:04] agreement, but our learned world model
[26:07] does go off the rails sometimes. In
[26:09] practice, this instability limits how
[26:12] far we can reasonably look into the
[26:14] future when planning using these world
[26:16] models. The push team model
[26:18] implementation we've been experimenting
[26:20] with is from a Jeppa implementation
[26:22] called layworld model. Layworld model is
[26:26] trained from scratch on push t. As we've
[26:29] seen, our model inputs are raw pixels
[26:31] and actions. And remarkably from this
[26:34] data alone, our world model learns the
[26:36] physics of the environment, including
[26:39] the fact that our blue tea is rigid and
[26:41] movable. And the complex interaction
[26:43] between our aector and the T. Looking
[26:46] inside our Jeepa model's learned world
[26:48] like this is fascinating. It's like a
[26:51] learned cartoon sketch of the dynamics
[26:52] of the push t world.
[26:55] From here we can use our world model to
[26:57] explicitly plan a set of actions instead
[27:00] of learning to directly imitate human
[27:02] actions as we would with VA approaches.
[27:05] And then if you have this you can uh
[27:07] predict the outcome of a sequence of
[27:09] actions and you can by optimization you
[27:11] can figure out an optimal sequence of
[27:13] actions to arrive at a particular
[27:16] outcome. Right? This is classical
[27:18] optimal control. To plan a course of
[27:20] actions, the lay world model team used a
[27:23] very general planning method called the
[27:25] cross entropy method or CM. Given a
[27:28] starting image and a goal image, CM
[27:31] starts with a completely random set of
[27:33] actions. Here's 500 randomly chosen
[27:36] trajectories for ourector.
[27:38] From here, we use our world model to
[27:40] select the most promising trajectories.
[27:43] This trajectory bounces around a bit and
[27:45] then bumps into our T. Using our world
[27:48] model, we can predict what would happen
[27:50] if we were to follow this path. Note
[27:52] that the layw world model team groups
[27:54] steps of actions together into groups of
[27:56] five and passes these actions into the
[27:59] predictor all at once. So our first
[28:02] batch of actions moves our aector down
[28:04] into the right. And our world model
[28:06] simulation matches this behavior. From
[28:09] here, we can continue our roll out five
[28:12] steps at a time with each batch passing
[28:14] our embedding space prediction from our
[28:16] previous batch into our predictor along
[28:18] with our latest five actions. After our
[28:22] randomly chosen 25 steps, our world
[28:25] model predicts that our aector will
[28:26] rotate our t, not really moving it any
[28:29] closer to its goal state. To measure how
[28:32] much closer or farther a given
[28:34] trajectory takes us from our goal, we
[28:37] compute the embedding of our goal image
[28:40] and then measure the uklidian distance
[28:42] between our final predicted embedding
[28:44] vector and the goal embedding vector.
[28:47] From here, we perform the same roll out
[28:49] process for each randomly chosen path
[28:52] and compute the same distance metric for
[28:54] each path. Let's color each path
[28:57] according to its distance in embedding
[28:59] space to our goal image. Here's our best
[29:02] performing path. It looks a bit random,
[29:06] but if we visualize our decoded world
[29:07] model predictions, we see that this path
[29:10] actually bumps into our t twice, pushing
[29:13] it towards our goal.
[29:16] From here, our top performing 30
[29:18] trajectories are grouped into an elite
[29:19] set, and the mean and standard deviation
[29:22] of this elite set are used to sample a
[29:24] new set of trajectories.
[29:26] This process is repeated again and again
[29:29] until we're left with a tight set of
[29:31] candidate trajectories and ultimately a
[29:33] final planned path.
[29:35] And what's really remarkable here is
[29:37] that our planning happens completely in
[29:39] the model's learned embedding space.
[29:42] The score we give each possible path
[29:44] guides the entire planning process and
[29:47] is computed as the distance between the
[29:49] final predicted embedding vector for
[29:51] each path and the goal embedding vector.
[29:55] We can now follow our planned path and
[29:58] see that our aector nicely pushes RT
[30:00] towards its goal.
[30:03] Our resulting system cleanly addresses
[30:05] Lacun's critiques of VLA. It does not
[30:08] learn by imitating humans. So the system
[30:11] does not need to see how a human would
[30:13] solve the task, but can instead find
[30:15] solutions on its own using its world
[30:18] model and an explicit planning process.
[30:21] However, while the architecture of
[30:22] layworld model is elegant and free from
[30:24] these concerns, the performance these
[30:27] models have shown to date is
[30:28] dramatically behind VLA on the push
[30:31] task. Lay world model can only reliably
[30:34] plan about five prediction loops in
[30:36] advance, limiting the model to
[30:38] relatively simple manipulations.
[30:41] When I'm trying to imagine a JEPA
[30:43] powered robot kind of doing a long
[30:44] horizon task like cleaning a kitchen for
[30:46] 10 minutes for example, right? Um I'm in
[30:49] my head, right? It's hard for me to
[30:50] imagine even in embedding space uh the
[30:53] predictor being able to see 10 minutes
[30:55] into the head moving around a kitchen
[30:56] that seems like uh longer than I would
[30:58] expect, right? Um does that is that
[31:00] where hierarchical starts to matter?
[31:02] What what are your thoughts on long
[31:03] horizon task with Jeepa?
[31:04] >> Yeah, you have the answer in your
[31:06] question. The answer to this is uh
[31:08] hierarchical models. Okay, so what's a
[31:11] hierarchical models model? It's one
[31:13] where uh at a low level you make
[31:16] detailed predictions.
[31:18] >> Mhm.
[31:18] >> But you don't but you don't predict long
[31:20] term because the more detail you
[31:22] preserve about the prediction,
[31:25] >> the more your prediction is likely to
[31:27] diverge from reality very quickly. Yeah.
[31:29] >> Right.
[31:30] >> And so you you train low levels in the
[31:33] predictor to make short-term prediction
[31:34] with a lot of details,
[31:36] >> which sometimes you need because you
[31:37] know you need to know exactly what's
[31:38] going to happen when you grab an object,
[31:40] right? you need to grab exactly the
[31:42] right way and things like this.
[31:44] >> So you need a lot of information
[31:46] but then if you want to make longerterm
[31:48] predictions
[31:50] then you can only do them with fewer
[31:51] details about what you predict
[31:54] >> right
[31:54] >> uh and so that you know the your your
[31:57] your prediction does not diverge from
[31:59] reality.
[32:00] >> What what would what would the interface
[32:02] be like between the layers of the
[32:03] hierarchy?
[32:06] Well, the the same kind of interface
[32:08] that exists between various layers of a
[32:10] deep neural net. That's exactly what
[32:12] >> Sure. Yeah. So, it's in some embedding
[32:14] space, the interface between layers. It
[32:15] doesn't have to be semantic or uh
[32:18] certainly not language, right?
[32:19] >> No language. I mean, your cat your cat
[32:21] can do hierarchical planning. So, you
[32:23] know, they don't have language, right?
[32:25] >> Right. Yeah. In Lacun's proposed
[32:27] solution, hierarchical world models, we
[32:30] can tackle longer horizon planning by
[32:32] simultaneously planning at different
[32:34] levels of abstraction, Jan and his
[32:37] collaborators recently applied a
[32:39] hierarchical world model approach to
[32:41] push t and other tasks and using two
[32:44] layers of hierarchy were able to extend
[32:46] the planning horizon in push t from five
[32:49] time steps to 15. Interestingly, the
[32:52] predictions from the higher level world
[32:54] model serve as sub goals for the lower
[32:56] level world model and planner
[32:58] >> and you can't plan a long uh action in
[33:03] terms of you know millisecond by
[33:05] millisecond muscle control.
[33:06] >> Sure.
[33:07] >> Mostly because you don't have the
[33:08] information most of the time like the
[33:10] example I use very often is
[33:12] >> if I'm sitting in my office at NYU and I
[33:14] want to be in Paris tomorrow.
[33:16] >> Sure. um I cannot plan my entire trip in
[33:19] terms of millisecond by millisecond
[33:21] muscle control
[33:21] >> right
[33:22] >> I don't have the information
[33:23] >> right
[33:24] >> you know in addition to the fact that it
[33:25] would be impossible to to do the the the
[33:28] planning
[33:29] >> uh so you go to a higher level of
[33:30] abstraction um you know a high level
[33:34] abstraction would be well I need to like
[33:37] you know go to the airport and catch a
[33:38] plane that's a high level plan right um
[33:41] and I have a sub goal which is going to
[33:43] the airport
[33:46] Um I'm in New York City. So so I'm go
[33:48] down on the street and have a taxi and
[33:51] then I have seup of goal going down in
[33:53] the street etc. And at some point in the
[33:55] hierarchy you have all the information
[33:58] you need and it's a task you are used to
[34:01] doing like standing up from your chair
[34:03] or walking to the elevator
[34:04] >> right and and do you think if we have
[34:06] the right architecture for the hierarchy
[34:08] then the like the hierarchy will be kind
[34:10] of learned just as like in CNN's you
[34:12] know kind of magically you know we'll
[34:13] learn this hierarchy of features. Do you
[34:15] expect if we have the right hierarchical
[34:16] JPA architecture then that will just
[34:18] become be emergent basically
[34:20] >> that's kind of the hope yeah totally
[34:22] that the system will you know discover
[34:24] the appropriate hierarchical
[34:26] representation by being trained
[34:28] >> to make short-term prediction at a low
[34:30] level and higher
[34:31] >> interesting
[34:31] >> longerterm prediction at a higher level
[34:33] >> right
[34:34] >> uh and and and and so the hope is that
[34:37] you know through this type of uh
[34:39] predicted prediction based
[34:40] self-supervised learning the system will
[34:42] will learn a good hierarchy of
[34:43] representations But it probably requires
[34:46] to train on kind of semiexpert
[34:48] trajectories like you you can't learn
[34:50] high level things if you train on
[34:51] completely random
[34:52] >> totally observations.
[34:54] >> Yeah. Interesting. Lacun's vision for
[34:56] Jeepa world models in the future of AI
[34:58] is well considered and compelling
[35:01] but it's still early for Jeepa. VJEPA 2
[35:05] and VLJA give us some powerful glimpses
[35:08] into what the framework can do and show
[35:11] that the Jeepa approach is not
[35:12] incompatible with the current mainstream
[35:15] languageddriven approach to AI.
[35:18] But when we zoom out to agentic and
[35:20] robotics problems, Jeepadriven world
[35:22] model approaches are still quite limited
[35:25] and there are many unanswered research
[35:27] questions.
[35:29] 30 years ago, as Jan worked on early
[35:31] deep learning systems to recognize
[35:33] handwritten digits, these systems
[35:35] probably felt pretty limited. Just as
[35:37] the push t demonstrations feel limited
[35:39] today. The fact that these core deep
[35:42] learning ideas could be scaled up to the
[35:44] powerful AI systems we have today is
[35:46] remarkable. Could Jeepa follow a similar
[35:49] trajectory? Is Jan's billion dollar bet
[35:52] on Jeepa completely right, part of a
[35:54] larger solution, or just a dead end? How
[35:58] will we know over the next you know two
[36:00] three five years if your this world
[36:02] model Jeeper approach is working? What
[36:03] would be a good next you know two three
[36:05] five years at at Omni Labs?
[36:08] >> So within uh within a year or two uh
[36:12] we'll we'll try to apply the the whole
[36:14] model planning etc to a number of uh
[36:19] industrial applications.
[36:20] >> Cool.
[36:21] >> Okay. And this is not necessarily a
[36:23] business model or to generate revenue.
[36:24] It's more to gain experience with sort
[36:27] of pushing this type of methodology into
[36:30] practical applications. And the ideal
[36:34] set of applications would be um
[36:38] essentially controlling a complex
[36:39] systems whose behavior cannot be reduced
[36:42] to a small number of equations.
[36:44] >> Okay? Because if you can write down the
[36:46] equations like you know a simple robot
[36:48] arm or even a humanoid robot, you can
[36:50] just write down the dynamical equations.
[36:51] you you need to identify a few a few
[36:53] coefficients but you can just write down
[36:55] the equations uh or you know you're NASA
[36:58] and you're shooting a rocket to go to
[36:59] the moon you can just you know you have
[37:01] complete dynamical model of the rocket
[37:03] and you can plan the entire trajectory
[37:05] >> right
[37:05] >> u but like what about a an entire
[37:09] jet engine or an entire airplane for
[37:11] that matter or um or a chemical plant or
[37:15] a power plant or a patient uh with you
[37:20] know a disease like say diabetes, right?
[37:24] what course of treatment um should you
[37:27] follow uh to kind of control the blood
[37:32] sugar of the patient and you know if you
[37:35] have a good predictive model of the
[37:36] state of the patient uh you might you
[37:39] might be able to design a a course of
[37:41] treatment uh or you know how would you
[37:44] uh uh tell a a stem cell to turn itself
[37:48] into a beta cell for pancreas to produce
[37:50] insulin right I mean there's a lot of
[37:52] complex systems like this simply cannot
[37:54] reduce to a small number of equations
[37:56] but you might be able to produce a
[37:58] phenomenological model of it from data
[38:01] and then use that to to uh to control
[38:04] it. Um and you know and it's true again
[38:06] of you know complex uh complex systems
[38:09] in industry or chemistry or or or or
[38:12] whatever right and there's a lot of
[38:14] really uh you know promising work in
[38:19] material science chemistry where where
[38:21] this kind of idea is uh is there you
[38:23] know you train a phological model of a
[38:26] complex collective phenomenon and then
[38:27] you use it to design new materials new
[38:30] catalyst for chemical reactions or new
[38:33] batteries you Oh, etc. Um, very
[38:36] promising. So,
[38:38] >> that would be the first applications and
[38:40] then eventually a few years from now,
[38:41] three, five years from now, uh, the hope
[38:44] is that, you know, we might become the
[38:46] main supplier of intelligent systems,
[38:48] whatever the application is.
[38:50] >> Amazing. Maybe we can talk again in a
[38:51] few years and we'll uh we'll see all the
[38:53] progress. I'm excited.
[38:54] >> Right. Exactly.
[38:57] >> If you enjoyed this video, check out the
[38:59] companion poster.
[39:02] We've been calling this graphic the web
[39:03] of AI. It follows the path to the
[39:06] current mainstream approach to AI,
[39:09] Lacun's alternative path to Jeepa and
[39:12] really nicely shows how discriminative,
[39:14] generative, and joint embedding
[39:15] approaches fit together. The bottom of
[39:18] the poster includes visual summaries of
[39:21] the models we covered in this video.
[39:23] VJA, VLJA, and layworld model. Our
[39:27] designer Sam used this really great
[39:29] texture on the Web of AI animations and
[39:32] we really wanted to retain this feel for
[39:34] the poster. We found this premium fine
[39:37] art rough paper from Canon that has this
[39:40] really great matte textured finish. It
[39:43] looks awesome. You can get the Jeepa
[39:45] poster on this textured paper or a more
[39:47] traditional smooth finish. You can pick
[39:50] up the Jeepa poster and the Welch Labs
[39:52] illustrated guide to AI at
[39:54] welchlabs.com.
[39:56] This two-part JEPA series clocked in at
[39:59] well over an hour and required hundreds
[40:01] of hours of research, writing,
[40:03] animation, and editing. To help us make
[40:06] more in-depth videos like this, please
[40:09] consider supporting Welch Labs on
[40:10] Patreon. We're finally planning some
[40:13] Welch Labs merch for later this year.
[40:16] All patrons will be able to vote on
[40:18] designs, and we're adding a new tier
[40:20] that includes early access to merch
[40:22] drops. At the $5 per month or higher
[40:25] level, we'll ship you a real paper
[40:27] cutout from a video. We typically ship
[40:30] what we've just finished shooting. So,
[40:32] if you sign up today, you'll likely
[40:34] receive a cutout from the Jeepa video.
[40:37] Huge thank you to Yan Lun and everyone
[40:39] else who helped make this series. I
[40:41] really hope we're able to interview Yan
[40:43] again in a few years and see how Jeepa
[40:46] progresses.