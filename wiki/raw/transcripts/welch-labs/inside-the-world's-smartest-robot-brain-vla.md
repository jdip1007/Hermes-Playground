---
source_url: https://www.youtube.com/watch?v=2mrGMMmrVNE
ingested: 2026-07-08
video_id: 2mrGMMmrVNE
title: Inside the World's Smartest Robot Brain [VLA]
series: None
---

[00:00] This may be the most significant moment
[00:02] in modern robotics. In 2023, a
[00:06] researcher at Google set up a table with
[00:07] a Coke can, pictures of Tom Cruz, Snoop
[00:10] Dogg, and Taylor Swift, and ask Google's
[00:12] newest robot brain, RT2, to move the
[00:15] Coke can to Taylor Swift. RT was too
[00:18] large to run on the robot itself. The
[00:21] robot sent one image at a time from its
[00:23] onboard camera to a TPU cluster, which
[00:26] sent back control signals. The robot
[00:29] controlled by RT2 slowly picked up the
[00:31] Coke can and awkwardly placed it on the
[00:34] edge of the picture of Taylor Swift. A
[00:36] couple years later in 2025, one of the
[00:39] researchers on the team, Carol Houseman,
[00:41] would describe this scene as the moment
[00:43] it became clear to him that this was
[00:46] going to work. Within a year of the 2023
[00:49] Coke can demo, Houseman and many of the
[00:51] key members of the RT2 team had left
[00:53] Google and reassembled to form a startup
[00:56] called Physical Intelligence.
[00:58] And the robots have gotten better. A lot
[01:01] better. The latest robot brains from
[01:03] physical intelligence can open padlocks,
[01:06] fold your laundry, peel an orange, make
[01:08] a grilled cheese sandwich, make coffee,
[01:11] and clean up bedrooms and kitchens that
[01:13] it's never seen before. Why was this
[01:16] unimpressive Coke can demo such a
[01:18] breakthrough? And how did it enable
[01:20] physical intelligence to improve their
[01:22] robots so rapidly?
[01:24] In this video, we'll first explore the
[01:26] fascinating buildup to RT2 at Google.
[01:29] From here, we'll take a deep dive into
[01:31] the physical intelligence robotics
[01:33] foundation models and see what makes
[01:35] these incredibly impressive robot brains
[01:38] tick.
[01:41] In 2022, the year chat GPT was released,
[01:44] researchers at Google began exploring
[01:46] what role large language models might
[01:48] play in robotics.
[01:50] Their first notable result, a system
[01:52] known as Seikan, used a large language
[01:54] model as a planning system to break down
[01:57] complex tasks into subtasks.
[02:00] In this demo, Sean breaks down cleaning
[02:02] up a spill into the subtasks of finding
[02:04] a sponge, picking up the sponge, going
[02:07] to the spill, and so on. From here, the
[02:10] team expanded on this work, creating a
[02:12] more capable iteration of the idea
[02:14] called inner monologue. and another
[02:16] interesting variant where the team used
[02:18] an LLM to write code to control the
[02:20] robot on the fly.
[02:23] However, these early efforts were
[02:24] effectively bottlenecked by the
[02:26] available robot controls algorithms.
[02:30] Once the LLM and Seikan decided to pick
[02:32] up a sponge, a completely separate
[02:34] neural network that had been trained to
[02:36] imitate humans controlling robots to
[02:38] perform various small tasks was used to
[02:40] compute the actual robot control
[02:42] signals. This meant that Seychan was
[02:45] effectively limited to a menu of actions
[02:47] the LLM could choose from. To get
[02:50] Seychan to place a coat can on an image
[02:52] of Taylor Swift, behaviors involving
[02:54] Coke cans and Taylor Swift would have to
[02:56] be explicitly trained.
[02:59] At the end of 2022, the team made a
[03:01] significant improvement to their control
[03:03] layer, introducing robot transformer 1
[03:06] or RT1.
[03:08] Like the team's previous control
[03:10] algorithms, RT1 was trained to imitate
[03:12] humans, but used a significantly larger
[03:15] data set with over 130,000 human
[03:18] demonstrations and used a larger
[03:20] transformer-based architecture. RT1 was
[03:24] able to perform a significantly broader
[03:25] range of actions than its predecessors.
[03:28] This effectively gave the planning layer
[03:30] a much larger menu of actions to choose
[03:33] from. The RT1 team showed that using the
[03:36] planning LLM from Sean coupled with RT1
[03:39] to control the robot significantly
[03:41] improved performance on long horizon
[03:43] tasks like finding certain items in
[03:46] kitchens that the robot hadn't seen
[03:48] before.
[03:50] As Google incrementally improved their
[03:52] robot brains, large language models were
[03:54] also rapidly advancing.
[03:57] The LLM used for planning in the Seikan
[03:59] RT1 systems was the textonly Palm 540B
[04:03] model trained in early 2022.
[04:06] This meant that the robots planning
[04:08] layer couldn't actually see the world.
[04:11] After breaking down a task like helping
[04:13] clean up the kitchen into tech subtasks,
[04:15] Google's robots relied on the R21
[04:17] control layer to take in images from the
[04:20] robot's camera and iteratively send
[04:22] control signals to the robot's actuators
[04:24] until each subtask was complete.
[04:27] This approach worked fine for some
[04:29] tasks, but having a planning layer that
[04:31] was effectively blind was clearly not
[04:33] ideal.
[04:35] On March 6th, 2023, about a week before
[04:38] the release of GPT4,
[04:40] Google researchers demonstrated Palm E,
[04:43] a variant of the Palm large language
[04:45] model that directly incorporated images
[04:47] and other data sources. Using the
[04:50] multimodal PALM E instead of the purely
[04:53] textbased PALM LLM as a planner with RT1
[04:56] as the control layer, the team
[04:58] demonstrated a significant expansion in
[05:00] capabilities.
[05:02] Now that the planning layer had access
[05:04] to vision information, the robot could
[05:06] perform more complex tasks that require
[05:08] adaptive planning, like moving objects
[05:11] out of the way to reach a desired object
[05:14] and fully autonomously recovering from
[05:16] setbacks. Here, a robot using Palm E as
[05:19] its planning layer and RT1 as its
[05:21] control layer is asked to retrieve a bag
[05:23] of chips. And when a researcher
[05:26] repeatedly puts the chips back in the
[05:27] drawer, Palm E is remarkably able to
[05:30] recognize that something has changed and
[05:32] adapt its plan. Now, let's zoom out a
[05:35] little and consider the full PAL E plus
[05:38] RT1 robot brain. Although Palm E and RT1
[05:42] were designed to work at different
[05:43] levels of the stack, they have some
[05:45] really interesting similarities.
[05:48] Both models take in images from the
[05:50] robot's camera and use a vision encoder
[05:52] neural network to process the images.
[05:55] From here in both models, these encoded
[05:58] image representations are passed into a
[06:00] transformer. This is the same type of
[06:02] compute block used fairly universally in
[06:05] large language models.
[06:07] The big difference here is what these
[06:09] transformers are trained to do. The RT1
[06:12] transformer was trained to directly
[06:14] output robot control signals by
[06:16] imitating humans controlling robots to
[06:18] solve various tasks. While the Palm E
[06:21] transformer is trained to output text
[06:23] across a wide variety of tasks,
[06:26] including simple next token prediction
[06:28] on internet text as we see in standard
[06:30] LLM pre-training, but also language
[06:33] vision tasks like image captioning. And
[06:36] importantly, Palmy was also trained to
[06:38] break apart robotics tasks into smaller
[06:41] subtasks.
[06:43] The similarities between Palmy and RT1
[06:46] and the fact that the team was able to
[06:48] expand the Palm languageonly model to
[06:50] effectively make use of other types of
[06:52] data all beg the question, do we really
[06:55] need two separate models here?
[06:58] Why not just continue expanding the palm
[07:01] language model to not only take in image
[07:03] data, but also to directly output robot
[07:06] control data, effectively absorbing RT1
[07:10] into a single powerful end-to-end model?
[07:14] Said differently, can large language
[07:16] models, by far the most powerful AI
[07:19] systems we've trained so far, be trained
[07:21] to become robot brains?
[07:25] This brings us to Taylor Swift and the
[07:27] Coke can. In July 2023, a few months
[07:30] after the Palm E paper came out, the
[07:33] Google robotics team demonstrated RT2.
[07:36] Taking Palm E and another multimodal LLM
[07:39] known as Pali X as starting points. The
[07:42] Google team trained these LLMs to
[07:44] directly output robot control signals,
[07:47] training on the same human control
[07:49] demonstration data they had used to
[07:51] train RT1 6 months earlier. And
[07:54] incredibly, it worked.
[07:57] RT2 was able to generalize shockingly
[07:59] well to objects, environments, and tasks
[08:01] that were not in the human demonstration
[08:04] data. This is what makes the Taylor
[08:06] Swift demo so impressive.
[08:09] The robot control training data
[08:11] definitely did not include Taylor Swift.
[08:14] So for RT2 to solve this task, it had to
[08:17] learn how to bring together abstract
[08:19] concepts it had learned in its internet
[08:21] scale pre-training with the robot
[08:24] control episodes. This means that these
[08:26] models can learn to connect the vast
[08:28] amounts of image, video, and text data
[08:30] on the internet with real world actions,
[08:34] potentially harnessing the full
[08:35] knowledge of the internet into robot
[08:38] brains.
[08:40] This is why this demo is such a big
[08:41] deal. It answers the question, can large
[08:44] language models be trained to be robot
[08:47] brains with a shaky but definitive yes.
[08:51] The RT2 team coined a new name for this
[08:54] type of model, vision, language, action
[08:57] or VA, linking together vision,
[08:59] language, and action into a single
[09:01] unified model.
[09:04] This video is about to get technical. to
[09:07] see how language models can learn to
[09:08] become robot brains. We're going to
[09:10] reference transformers, embedding
[09:12] vectors, diffusion models, attention
[09:14] heads, softmax, and more. The required
[09:17] context for all these concepts is way
[09:20] more than we can fit into a single
[09:21] video, which is why I wrote this book.
[09:24] The Welch Labs illustrated guide to AI
[09:27] breaks down all of these concepts using
[09:29] hundreds of figures, detailed
[09:31] descriptions, and exercises. You can
[09:33] pick up a copy at welchabs.com.
[09:36] And we're very excited to announce that
[09:37] we're beginning to offer international
[09:39] shipping. Stay tuned to the end of the
[09:41] video for more updates on the book and
[09:44] to see the poster that goes along with
[09:45] this video that nicely breaks down the
[09:48] vision language action model
[09:49] architecture.
[09:52] By early 2024, a number of key members
[09:55] of the RT2 team had left Google and
[09:58] reassembled to form the startup Physical
[10:00] Intelligence.
[10:01] In October of that year, the team demoed
[10:04] their first robot brain, Pi Zero.
[10:07] Compared to the RT2 Coke can Taylor
[10:10] Swift demo 15 months before at Google,
[10:12] Pi 0ero is remarkable.
[10:15] It starts to really feel like a robot
[10:17] that could help you around the house,
[10:19] performing tasks like getting laundry
[10:20] out of the dryer, folding the laundry,
[10:22] and cleaning up tables.
[10:24] How was the physical intelligence team
[10:26] able to improve on RT2 so significantly
[10:29] and so quickly?
[10:31] Like RT2, PI0 is a vision language
[10:34] action model built on top of a
[10:37] pre-trained multimodal LLM
[10:40] based on PI 0 strong performance. You
[10:43] might guess that the physical
[10:44] intelligence team increased the model
[10:46] size relative to RT2, but PI 0 is
[10:49] actually smaller. The RT2 model family
[10:52] ranged from 5 to 55 billion parameters.
[10:56] And Pi 0 remarkably only uses 3.3
[10:59] billion parameters,
[11:01] allowing the model to run on the robot
[11:02] itself using a consumer grade NVIDIA RTX
[11:05] 4090 GPU at a very respectable 73
[11:09] millisecond inference time. Here's what
[11:12] Pi 0 looks like hooked up to a twoarm
[11:14] robot platform called Aloha and tasked
[11:17] with uncapping a pen.
[11:19] Pi 0 takes images from an overhead
[11:21] camera and from one camera on the wrist
[11:23] of each robot arm and a text prompt. At
[11:27] each time step, PI 0 returns 14 numbers.
[11:31] One number for the position of each of
[11:33] the seven actuators on each arm. Here
[11:36] we're plotting these outputs as a time
[11:37] series. This movement in our pink curve
[11:40] here shows us where pi is telling the
[11:42] left gripper to grab onto the pen cap.
[11:48] PI0 is built on top of Pali Gemma, an
[11:51] openweight multimodal LLM from Google.
[11:55] Palmma is built from two other
[11:56] openweight models, the SIGLIP image
[11:59] encoder and the Gemma large language
[12:01] model that are trained together to solve
[12:04] vision language tasks like image
[12:06] captioning.
[12:07] Now following the RT2 approach, the
[12:10] underlying language model in this case
[12:12] palma would be trained to directly
[12:15] output control values.
[12:17] However, the physical intelligence team
[12:19] made a clever improvement here that
[12:21] makes PI0 significantly better at
[12:23] dextrous manipulation. Instead of having
[12:26] the underlying language model directly
[12:27] output control values, PI0 introduces a
[12:31] second neural network the team calls an
[12:33] action expert. Interestingly, the PI
[12:36] zero action expert uses the same
[12:38] architecture as Gemma. In fact, in the
[12:40] PI zero codebase, the action expert is
[12:43] instantiated as a Gemma model.
[12:46] The only differences are that the action
[12:48] expert is randomly initialized instead
[12:50] of pre-trained and the action expert is
[12:53] not as wide as Gemma using fewer
[12:56] parameters within each layer. Now this
[12:59] may sound like we're going back to the
[13:00] earlier sean system where a highle LLM
[13:04] performed planning and a lower level
[13:06] network handled robot control. The key
[13:09] distinction here is that in the sean
[13:11] system the interface between models was
[13:14] natural language. The planning LLM told
[13:17] the control network what to do using
[13:19] predetermined text instructions.
[13:22] PI0 in contrast uses a much richer
[13:25] interface between the two models. Since
[13:28] the Gemma LLM and Action Expert
[13:30] effectively share the same architecture,
[13:32] it's possible for these models to almost
[13:34] think as one while retaining some really
[13:37] nice benefits of modularity.
[13:39] Let's have a closer look at how our
[13:41] Gemma LLM learns to act as a robot
[13:43] brain. Then we'll have a closer look at
[13:46] how the interface between these two
[13:47] models works. The Gemma LLM processes
[13:50] both the images and text prompts that
[13:52] come into PI0. Each image is broken into
[13:55] a grid of patches resulting in 256 image
[13:59] patches per image and 768 total patches.
[14:03] The patches from each image are passed
[14:05] into an image encoder model resulting in
[14:08] 768 embedding vectors each of length
[14:12] 248.
[14:14] These vectors are sometimes referred to
[14:16] as soft tokens.
[14:18] Here we're coloring each embedding
[14:19] vector to approximately match its
[14:21] corresponding image patch. This will
[14:24] help us keep track of our data as it
[14:25] flows through our model. These embedding
[14:28] vectors live in a semantically rich
[14:30] embedding space, meaning they should
[14:33] contain lots of easily accessible
[14:34] information about our images, like
[14:37] whether a given image patch contains a
[14:39] pen.
[14:41] For more on embedding spaces and image
[14:43] encoders, check out the Welch Labs video
[14:45] on AlexNet, the AI image generation
[14:48] video we did with three blue one brown,
[14:50] or the Welch Labs illustrated guide to
[14:52] AI.
[14:53] The text prompt we give pi 0, in this
[14:56] case, uncap the pen, is broken into four
[14:59] tokens. And each token is mapped to an
[15:02] embedding vector of the same length as
[15:03] our image patch embedding vectors.
[15:07] So we now have 772 total embedding
[15:10] vectors, 768 from our images, and four
[15:14] from our text prompt. From here, these
[15:17] embedding vectors are passed into our
[15:19] Gemma LLM.
[15:21] Gemma is composed of 18 transformer
[15:23] blocks, each containing an attention and
[15:26] multi-layer perceptron compute block.
[15:29] Each attention block contains eight
[15:31] attention heads. These attention heads
[15:34] are arguably the most critical part of
[15:35] the transformer architecture and are the
[15:38] key to the tight integration between
[15:40] PI0's underlying LLM Gemma and PIZ's
[15:43] action expert. In a given attention
[15:46] head, the incoming embedding vectors are
[15:49] multiplied by three separate matrices of
[15:51] learnable weights, producing three new
[15:54] matrices known as queries, keys, and
[15:57] values.
[15:59] Each of these matrices has 772 rows, one
[16:03] for each input to our transformer.
[16:06] We don't have enough space to visualize
[16:08] all 772 rows of our matrix. Here we're
[16:11] showing the first row which corresponds
[16:13] to the upper left patch of our overhead
[16:16] image.
[16:17] Next we're showing rows 373 to 376
[16:22] which correspond to these four patches
[16:24] of our left wrist image.
[16:27] This will be important shortly as we see
[16:29] how Gemma figures out how to connect the
[16:31] word for pen to the parts of the images
[16:33] that contain the pen. As we did with our
[16:36] embedding vectors, we'll color each row
[16:38] of our matrix with the approximately
[16:40] average color from its corresponding
[16:42] image patch. Our two patches that
[16:45] contain the orange pen get colored
[16:47] orange. And finally, the light and dark
[16:49] parts of each vector correspond to the
[16:51] actual numerical values of the vector.
[16:54] Dark regions are lower numbers and light
[16:56] regions are higher numbers. Finishing
[16:59] out our matrix, these last four rows
[17:01] come from our input text with one row
[17:04] for each token. and we'll color all our
[17:06] text rows blue. From here, Gemma's
[17:09] attention head searches for similar
[17:11] query and key matrix rows. This
[17:14] attention head may have learned, for
[17:16] example, to specialize in searching the
[17:18] incoming images for objects that match
[17:20] words that appear in the prompt. After
[17:23] all, if our robot brain is going to
[17:25] uncap the pen, it needs to know where
[17:27] the pen is in our images.
[17:30] The word pin shows up at our very last
[17:32] token input position and its query
[17:35] vector looks like this.
[17:37] The attention head computes the
[17:38] dotproduct between this row and every
[17:41] row in our key matrix.
[17:43] And larger dot productducts indicate
[17:45] closer matches between queries and keys.
[17:49] Interestingly, our highest dot
[17:51] productducts in this sample by far occur
[17:53] at our two image patches that contain
[17:55] the pen.
[17:57] From here, our attention head normalizes
[17:59] these dotproduct values using a softmax
[18:01] operation. We can take our visualization
[18:04] one step further here and show these
[18:06] attention values as a heat map on top of
[18:09] our images where brighter shades of
[18:11] magenta correspond to larger attention
[18:14] values.
[18:15] So the two orange rows of our key matrix
[18:18] with high attention values that
[18:20] correspond to these two image patches
[18:22] get colored bright magenta and their
[18:24] neighboring patches with low attention
[18:26] scores do not. So the idea here is that
[18:29] our heat map visualization shows us the
[18:32] strongest matches in our images to our
[18:34] query vector for the word pen in our
[18:36] prompt.
[18:38] And remarkably, our best matches occur
[18:40] at the patches in all three images that
[18:42] show the pen.
[18:44] Playing our video and running this
[18:46] analysis at each frame, we see
[18:48] impressive pen tracking results.
[18:52] Our model is clearly using this
[18:53] attention head to connect the word pen
[18:55] in our prompt to the parts of our images
[18:57] that contain the pen.
[19:01] Now, our attention head doesn't just
[19:03] search for matches to our pen query. All
[19:06] 772 query vectors corresponding to all
[19:10] input images and prompt tokens are
[19:13] compared to all 772 key vectors. The
[19:17] resulting attention values from all
[19:18] these comparisons are collected in a
[19:21] 772x 772 attention pattern matrix.
[19:25] Each row of the attention pattern
[19:27] corresponds to a single query. The final
[19:30] query row corresponds to the pin token
[19:33] in the prompt that we've been
[19:34] visualizing. So our heat map values end
[19:37] up in the bottom row of our attention
[19:39] pattern. At the beginning of our
[19:41] attention head, we computed three
[19:43] matrices, our queries, keys, and values.
[19:47] We've used our queries and keys to
[19:49] create our attention pattern. And now
[19:51] our attention pattern matrix is
[19:53] multiplied by our value matrix, creating
[19:55] this attention heads output, a new 772x
[19:59] 256 matrix. Multiplying our value matrix
[20:02] by our attention pattern effectively
[20:04] moves information between token
[20:06] positions.
[20:08] The large attention values we see
[20:10] between our pen query and pen image
[20:12] patches mean that these image patch rows
[20:15] are copied and added to the pen position
[20:17] in our final output. One way to think
[20:20] about this operation is that our
[20:22] attention head is forming a unified
[20:24] representation of the text for pen and
[20:26] the parts of our images that contain
[20:28] pens.
[20:30] Now, this is just a single head in a
[20:32] single layer of our 18 layer Gemma LLM.
[20:36] And we expect different heads to learn
[20:37] to pick up on different types of
[20:39] patterns. And remember that our Gemma
[20:41] LLM is just one part of the PI zero
[20:43] system. Let's now turn to PI 0's action
[20:47] expert model and see how the physical
[20:49] intelligence team was able to get these
[20:51] models to work together so seamlessly.
[20:54] While the polygeimma portion of PI 0
[20:56] takes in our 772 image and text prompt
[20:59] tokens, the action expert takes in
[21:02] information about our robot state. That
[21:05] is the position of all of its joints.
[21:08] On the Aloha platform we've been
[21:10] experimenting with, each arm has a
[21:12] movable waist, shoulder, elbow, forearm
[21:15] rotation, wrist, wrist rotation, and
[21:18] gripper.
[21:19] This makes for seven joints per arm or
[21:22] 14 total numerical values that we need
[21:24] to control our robot.
[21:27] Just as our text prompt and input images
[21:29] are mapped to embedding vectors, our
[21:31] vector of 14 joint positions is also
[21:34] mapped to an embedding vector. This
[21:36] mapping is done by multiplying our joint
[21:38] vector by a 14x 1024 matrix of learned
[21:41] weights.
[21:43] Note that while the Gemma LLM in PI0
[21:45] uses an embedding vector of length 248,
[21:48] the action expert uses embedding vectors
[21:50] of length 1024.
[21:52] This reduces the compute requirements
[21:54] and inference time of the action expert
[21:56] model. So the robot's current state fits
[21:59] into a single embedding vector or soft
[22:01] token. This is one of the inputs to our
[22:04] action expert. The action expert has one
[22:07] more set of inputs. the joint positions
[22:10] of the robot over the next 50 time
[22:12] steps, generally referred to as actions.
[22:16] Now, this might seem backwards. The
[22:19] whole point of the action expert is to
[22:21] predict the future robot actions. How
[22:24] could the model take predicted actions
[22:25] as an input?
[22:27] In a fascinating transfer of ideas from
[22:30] AI, video, and image generation, PZO's
[22:33] action expert uses a method called flow
[22:35] matching. The idea is that instead of
[22:38] outputting robot actions in one go, the
[22:40] model iteratively shapes completely
[22:42] random actions into a final trajectory.
[22:46] The comparison to AI image generation is
[22:48] really interesting here. A final set of
[22:51] actions produced by our action expert
[22:53] will be of dimension 14x 50 with one row
[22:56] to control each robot joint and one
[22:59] column for each of the next 50 time
[23:01] steps. We can visualize this matrix as
[23:04] an image as we have with other matrices
[23:06] in our model. In this set of actions, we
[23:09] see an increase in the values in our
[23:11] ninth row. We can plot these values as a
[23:14] time series.
[23:16] This set of actions is telling our robot
[23:18] to move its right shoulder, reaching its
[23:20] right gripper towards the pen. In AI
[23:23] image generation, we can create an image
[23:25] of a cat by iteratively refining a pure
[23:28] noise image into a detailed cat image.
[23:32] Pi 0's action expert does the same
[23:34] thing, refining a 14x50 random image of
[23:38] joint trajectories into a detailed plan
[23:40] for how to move each robot joint.
[23:44] One reason this flow matching or
[23:45] diffusion process works so well for
[23:47] generating natural images is that the
[23:50] distribution of natural images is
[23:52] multimodal.
[23:53] There are many ways to create an image
[23:55] of a cat. Analogously, there are many
[23:57] ways we can move our 14 robot joints to
[24:00] uncap a pen.
[24:03] So to generate a set of actions, the
[24:05] action expert starts with completely
[24:07] random actions and predicts how these
[24:09] actions should be updated to produce a
[24:11] slightly more realistic and accurate set
[24:14] of trajectories. These trajectories are
[24:16] added to the input actions and then
[24:19] passed back into the model, which then
[24:21] computes a new set of updates. This
[24:24] process is repeated 10 times in pi 0
[24:26] until we have a nice set of
[24:28] trajectories.
[24:30] The fact that we can use the same exact
[24:31] flow matching process to generate images
[24:34] and videos and control robots is so
[24:37] interesting to me. It's such a
[24:39] surprisingly effective abstraction on
[24:41] top of what feel like very different
[24:43] applications of AI.
[24:46] So our action expert model can
[24:47] iteratively shape pure noise into robot
[24:50] trajectories.
[24:52] But how does it know what trajectories
[24:53] to generate? The action expert needs to
[24:56] know what the goal is. In the case of
[24:58] our example, uncapping the pen. And of
[25:00] course, it needs lots of information
[25:02] about the scene, like where the pen is
[25:04] in space. As we saw earlier, this is
[25:08] exactly the type of information our
[25:09] Gemma LLM is already processing in its
[25:12] attention heads.
[25:14] The question from here is how do we best
[25:16] give our action expert access to this
[25:19] information? As we saw earlier, the
[25:21] action expert uses the same architecture
[25:23] as our Gemma LLM.
[25:26] This means that like Gemma, our action
[25:28] expert has 18 attention blocks with
[25:30] eight attention heads each.
[25:33] As we saw earlier, each Gemma attention
[25:35] head computes a separate query, key, and
[25:37] value matrix.
[25:40] Our action expert attention heads
[25:41] perform the same operations, but with
[25:44] different inputs.
[25:46] Our action expert has 51 inputs. one for
[25:49] the robot's current state and 50 for the
[25:52] robot's predicted actions over the next
[25:54] 50 time steps.
[25:56] So within each attention head, our
[25:58] action experts query matrix will have 51
[26:01] rows, one for each model input.
[26:04] Now using the standard attention
[26:06] mechanism, each query is able to search
[26:08] for matches in the keys. This could
[26:11] allow, for example, our second action
[26:13] step to use information from our first
[26:15] action step, which would help our model
[26:18] create a nice smooth trajectory from
[26:20] time step to time step. Of course, to
[26:23] figure out where these trajectories
[26:24] should go at all, our action experts
[26:26] queries ideally need access to the
[26:29] prompt and image information from our
[26:30] Gemma LLM.
[26:32] This is where the team's decision to use
[26:34] the same architecture for the LLM and
[26:36] Action Expert really pays off.
[26:39] All we have to do at this stage is take
[26:41] the keys and values from the
[26:42] corresponding attention head of our
[26:44] Gemma LLM and append them to the keys
[26:47] and values from our action expert. So we
[26:50] now have 51 + 772,
[26:53] making for a total of 823 keys that our
[26:56] action expert can query. These keys
[26:59] contain all the information the action
[27:01] expert needs. the text prompt, the
[27:04] encoded images, the robot state, and
[27:07] other time steps in the planning
[27:09] process.
[27:10] This gives the attention heads in our
[27:12] action expert an immediately available,
[27:14] incredibly rich information source. It's
[27:17] a really clever design.
[27:20] This modular design allows for some
[27:22] impressive efficiency gains.
[27:25] After the images and prompt are passed
[27:26] into Palma, the computed keys and values
[27:29] in each attention head are cached. This
[27:32] is a common step in LLM inference
[27:35] preventing redundant computation as new
[27:36] tokens come along. However, in this
[27:40] case, the physical intelligence team
[27:42] uses Pygeimma's KV cache to feed into
[27:45] each action expert's attention head.
[27:49] Since the action expert uses a flow
[27:51] matching process, it needs to run
[27:53] multiple times to produce final smooth
[27:55] trajectories, but is able to use the
[27:58] same KB cache each time because the
[28:00] input images don't change until the next
[28:02] time step.
[28:04] The fact that all these components can
[28:06] be trained to work together so well is
[28:08] absolutely incredible.
[28:10] At each step, pi zero takes in its
[28:12] prompt and images, runs them through
[28:14] polygeemma, caches all the key and value
[28:17] matrices, and then runs the action
[28:19] expert to iteratively dn noiseise random
[28:21] trajectories into final paths.
[28:25] The robot then follows these paths for a
[28:27] few steps, and the process is repeated,
[28:30] controlling the robot to achieve the
[28:32] task at hand.
[28:34] Since Pi Zero was first demoed in
[28:35] October of 2024, the physical
[28:38] intelligence team has made various
[28:39] improvements to their models and
[28:41] training approach,
[28:43] but their core VLA architecture using a
[28:45] tightly coupled multimodal LLM with a
[28:48] flow matching action expert has remained
[28:50] unchanged.
[28:52] Looking back on the RT2 Taylor Swift
[28:54] Coke can demo in 2023, it's incredible
[28:57] to see how far VLA models have come. And
[29:01] what's perhaps even more impressive to
[29:02] me is that the physical intelligence
[29:05] team had the foresight to realize what
[29:07] this unimpressive demo really meant.
[29:10] That large language models could be
[29:11] trained to be robots.
[29:14] Potentially leveraging the full
[29:15] knowledge of the internet into robot
[29:17] brains.
[29:20] Now, as impressive as these demos are,
[29:22] they're still demos. In 1995, a team
[29:25] from Carnegie Melon demonstrated a
[29:27] self-driving system, Ralph, that drove
[29:29] across the US at 98.2% autonomously.
[29:34] This clearly did not mean that
[29:35] self-driving cars were around the
[29:37] corner. And the generation of
[29:39] self-driving cars we have today works
[29:40] very differently.
[29:42] And interestingly, there's a different
[29:44] paradigm emerging for building robot
[29:46] brains, broadly known as world models,
[29:50] that actually do not use large language
[29:52] models as a backbone.
[29:54] Yan Lun, AI pioneer and longtime chief
[29:57] AI scientist at Meta, recently left his
[30:00] role at Meta to start a new venture
[30:02] focused on world models.
[30:04] Jan was kind enough to chat with us
[30:06] about it and wasn't shy about giving his
[30:08] opinion on VLA models. What's your
[30:11] expectation here? Do you think Jeepa
[30:13] based approaches will eventually
[30:14] overtake VLA approaches?
[30:16] >> Oh, absolutely. Yeah, VA are doomed. I
[30:18] mean, they they basically don't work
[30:20] really well. Okay. I mean,
[30:23] >> next time we'll dig into Yan's approach.
[30:27] If you enjoyed this video, check out the
[30:29] companion poster. The poster walks
[30:32] through the full Pi Zero architecture
[30:34] with helpful descriptions along the way.
[30:36] Fitting everything on screen was a huge
[30:38] challenge when animating this video, and
[30:40] the large format of the poster is
[30:42] perfect for getting everything into one
[30:44] place. The poster is printed on
[30:47] highquality large format photo paper
[30:49] with genuine Canon inks for excellent
[30:51] colors and details. For a limited time,
[30:54] you can get a discount on the poster
[30:55] when bundled with the Welch Labs
[30:56] Illustrated Guide to AI using code VLA.
[31:01] Speaking of the Welch Labs Illustrated
[31:02] Guide to AI, I'm very excited to
[31:04] announce that international shipping is
[31:06] now available in these nine countries
[31:08] and we're planning to expand to these
[31:10] countries next. I know this has taken a
[31:13] really long time. Thank you for your
[31:15] patience. A ton of you have emailed us
[31:17] and joined our international shipping
[31:19] weight list. Today, all of our books are
[31:22] printed in the US. We have a great
[31:24] relationship with our printer and the
[31:26] quality is outstanding. We've received a
[31:28] bunch of nice feedback about this. This
[31:30] viewer told us that the construction
[31:32] quality is the best they've ever seen.
[31:35] However, our print costs are fairly
[31:36] high, and being self-published makes
[31:39] international logistics a real
[31:40] challenge. Until very recently, my
[31:43] family and I packed all the books
[31:45] ourselves. Here's 7,000 lbs of books
[31:48] getting dropped off on the street in
[31:49] front of my house late last year. We use
[31:51] highquality boxes and corner protectors
[31:53] to make sure your book arrives in
[31:55] pristine condition. The other packaging
[31:57] options we've tried just don't protect
[31:59] this heavy book very well. Here's some
[32:02] outgoing shipments and a van we rent
[32:04] sometimes for post office runs. Here's
[32:06] part of another shipment that was
[32:08] delivered during a snowstorm this year.
[32:10] And here's some more books heading to
[32:11] the post office in my family's SUV. It's
[32:14] definitely been an adventure. Early this
[32:16] year, we started looking at ways to
[32:18] improve and scale our process. We've had
[32:21] some interesting calls with publishers,
[32:23] but the deals we've seen so far either
[32:25] significantly reduce print quality or
[32:27] cut too deeply into our margins,
[32:29] effectively introducing one or two
[32:31] layers of middlemen to our supply chain.
[32:34] So, we've decided to stay self-published
[32:36] for now. We did find a great local
[32:38] packing and logistics partner who now
[32:40] thankfully is handling fulfillment. They
[32:43] also ship enough volume to get some nice
[32:45] international rate discounts. This is
[32:47] what has allowed us to start to tackle
[32:49] international shipping. Starting today,
[32:51] we're offering flat rate shipping to
[32:53] Canada, Mexico, the UK, Ireland,
[32:56] Germany, France, the Netherlands, Italy,
[32:58] and Belgium. And the flat rate includes
[33:00] all relevant VAT, GST, and duties. We
[33:04] chose these countries by cross
[33:05] referencing the countries with the
[33:06] highest demand on our weight list and
[33:08] where we're able to ship without
[33:10] exorbitant shipping costs.
[33:13] Next, we're looking at expanding to
[33:14] India, Australia, New Zealand,
[33:16] Singapore, Japan, South Korea, Hong
[33:18] Kong, Thailand, and Malaysia. Although
[33:21] higher shipping costs due to a global
[33:23] increase in fuel prices is making this a
[33:25] bit more challenging than we expected.
[33:28] I'm really happy that we now have some
[33:30] international options, but the price we
[33:32] need to charge to cover printing and
[33:33] shipping is still higher than I would
[33:35] like. If we continue to see strong
[33:38] demand, this will allow us to invest in
[33:40] larger print runs, bringing down
[33:42] printing cost, and we're even looking at
[33:44] doing some of our printing regionally,
[33:46] starting in Europe. This would
[33:48] significantly bring down our European
[33:50] shipping costs and allow for lower
[33:52] prices. Sometimes I really question if
[33:54] this is all just crazy and really a
[33:56] distraction from making videos,
[33:58] especially on days when 7,000 lbs of
[34:01] books show up at my house. However, at
[34:04] the end of the day, the mission of Welch
[34:05] Labs is to make these complex topics as
[34:07] understandable as possible, and books
[34:09] are a big part of that mission. One
[34:12] supporter on Patreon, Lauren Steelely,
[34:14] put this really nicely when talking
[34:16] about the book. It's not just a
[34:18] condensed version of the videos. The
[34:21] book actually adds so much more detail
[34:23] that the videos couldn't possibly
[34:24] contain.
[34:26] Finally, a big thank you to all the
[34:28] readers who have helped find errors and
[34:30] made suggestions for improvements. These
[34:32] readers are listed on the credits page
[34:34] of the latest version of the book, and
[34:36] we published an arata at
[34:37] welchabs.com/ai-book.
[34:41] I especially want to thank Robert
[34:43] Blumoff. He's been incredibly meticulous
[34:46] at rooting out little issues in the book
[34:48] and has even made his own Perceptron
[34:50] machine and build guide. I'll include a
[34:52] link in the description below. Thank you
[34:54] so much for your patience and to
[34:56] everyone who's bought a book. It really
[34:57] helps the business work and means a lot
[34:59] to us. Thank you.