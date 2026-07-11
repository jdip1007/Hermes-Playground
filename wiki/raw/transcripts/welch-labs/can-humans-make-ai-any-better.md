---
source_url: https://www.youtube.com/watch?v=2hcsmtkSzIw
ingested: 2026-07-08
video_id: 2hcsmtkSzIw
title: Can humans make AI any better?
series: None
---

[00:00] In 1971, the US government agency ARPA
[00:03] launched a program to push the frontiers
[00:05] of speech recognition. ARPA set an
[00:08] ambitious 5-year goal, a system that
[00:11] could recognize a thousand different
[00:12] words with 90% accuracy. 5 years later,
[00:16] a team from Carnegie Melon demonstrated
[00:18] Harpy, an AI system capable of
[00:20] recognizing a,01 different words with
[00:23] 95% accuracy. The ARPA program was a
[00:26] success, but over the next decade, the
[00:29] core of Harpy's intelligence, an
[00:31] enormous knowledge graph, would be
[00:33] replaced by something completely
[00:35] different. Each of the over 14,000 nodes
[00:38] in Harpy's knowledge graph represents a
[00:40] single phone. One of the 98 basic sounds
[00:43] the team used to break apart spoken
[00:45] American English.
[00:47] The graph itself captures all the
[00:49] different ways these phones can be
[00:51] strung together to create sentences
[00:53] considered valid by Harpy.
[00:55] In this part of the graph, we can see
[00:57] the pathway for the phrases, tell me
[00:59] about China, tell me about Nixon, and
[01:02] give me the headlines.
[01:04] Each phone in Harpy's graph includes an
[01:06] expected frequency curve for the sound
[01:09] of the phone. These curves are tuned for
[01:12] the current speaker as audio comes in.
[01:15] For example, if I say tell me about
[01:17] China, a signal processing algorithm
[01:19] chops the waveform into blocks and the
[01:22] frequency content of each block is
[01:24] computed.
[01:25] From here, the frequency content of our
[01:27] first block is compared to the phones at
[01:29] the start of our graph. G in give and T
[01:32] in tell. T is a better match. So, we
[01:36] progress down this part of the tree. We
[01:38] then move to the second block in our
[01:40] waveform. This is the L intel and find
[01:43] its closest match. Block by block, we
[01:47] progress through our knowledge graph
[01:49] using a frequency matching score to
[01:51] guide our search, resulting in a final
[01:54] sentence. Note that the Harpy team also
[01:56] used a somewhat more sophisticated
[01:58] search method called beam search to help
[02:00] find the best overall path through the
[02:02] graph instead of just greedily choosing
[02:05] the best match at each step.
[02:08] The way Harpy's knowledge graph is
[02:09] constructed is painstaking and
[02:11] fascinating.
[02:12] First, a language design expert
[02:14] specifies a grammar. Harpy could not
[02:18] accept arbitrary sequences of words.
[02:20] This would have significantly degraded
[02:22] performance.
[02:24] Instead, a formal grammar was used to
[02:26] capture valid sentence structures for
[02:28] Harpy's intended use case of document
[02:30] retrieval.
[02:31] This small example Harpy grammar tells
[02:34] us that the word tell can be followed by
[02:36] me or us and then by all or about.
[02:40] From here, each word in Harpy's
[02:41] vocabulary is broken into individual
[02:44] phones. These breakdowns are themselves
[02:46] little graphs. Here's the pronunciation
[02:49] graph the Harpy team used for the word
[02:51] tell. Note that the graph branches due
[02:54] to the possibility of pronouncing tell
[02:56] in different ways. tell can be
[02:58] pronounced with an extra vowel sound in
[03:00] the middle. Replacing each word in our
[03:03] word graph with its phone breakdown, we
[03:05] get a larger graph. But we aren't done
[03:07] yet.
[03:09] When we speak, we often change the way
[03:11] words sound depending on the words
[03:12] around them. This is known as a
[03:14] juncture. When saying a phrase like
[03:17] about China, the T in about is often
[03:20] dropped, leaving about China.
[03:23] And in transitions like me all, a subtle
[03:26] extra Y sound known as a glide is added
[03:29] by some speakers to transition between
[03:31] vowels.
[03:33] The Harpy team accounted for this by
[03:35] creating rules to manipulate the phone
[03:37] graph to allow for various junctures
[03:40] between phones.
[03:42] Now, although Harpy achieved Arper's
[03:44] ambitious goal of 90% accuracy on a
[03:47] thousandword vocabulary,
[03:49] further scaling Harpy's performance
[03:51] proved difficult. And over the next
[03:54] decade, Harpy's knowledge graph was
[03:55] replaced by hidden markoff models. These
[03:59] models can still be understood as
[04:00] implementing a graph structure between
[04:02] phone nodes, but the edges of the graph
[04:05] are now probabilities that are learned
[04:07] from data. No language expert specified
[04:10] grammar and no linguistic expert
[04:12] specified juncture rules.
[04:15] This was a controversial shift at the
[04:17] time. Building our knowledge into AI
[04:20] systems was considered critical by many
[04:22] researchers.
[04:24] However, by the late 1980s and early
[04:26] 1990s, virtually all speech recognition
[04:29] systems had moved to hidden markoff
[04:31] models. And these systems were able to
[04:33] scale to much larger vocabularies of
[04:36] 5,000 and then 20,000 words.
[04:39] Decades later, in 2019, the computer
[04:42] scientist Richard Sutton published a
[04:44] highly cited essay that he called the
[04:45] bitter lesson. In his essay, Sutton
[04:48] points out that Harpy's replacement with
[04:50] hidden Markoff model based approaches is
[04:53] part of a broader trend. A trend that
[04:56] Sutton calls the biggest lesson from 70
[04:58] years of AI research.
[05:01] Specifically, that general methods that
[05:03] leverage computation are ultimately the
[05:05] most effective and by a large margin.
[05:09] and that trying to build human knowledge
[05:10] into our systems as the Harpy team did
[05:13] helps initially but then becomes highly
[05:16] counterproductive.
[05:18] The timing of Sutton's essay could not
[05:20] have been better. OpenAI had just
[05:22] released GPT2 a few weeks prior and a
[05:25] new paradigm was just beginning to
[05:27] emerge.
[05:29] A general architecture, the transformer,
[05:31] focused on a simple learning objective,
[05:33] next token prediction, and trained with
[05:36] massive amounts of compute, could
[05:38] produce shockingly intelligent language
[05:40] models.
[05:42] For myself and many others, it seemed
[05:44] like we had learned the bitter lesson.
[05:47] We had found a method of creating AI
[05:49] systems that leveraged massive amounts
[05:51] of compute and appeared to rely only
[05:54] minimally on human assumptions about how
[05:56] AI systems should work.
[05:58] But then in 2025, something really
[06:01] surprising happened. Richard Sutton went
[06:04] on a podcast. In the first 10 minutes of
[06:07] Sutton's interview with Darkash Patel,
[06:09] it became clear that Sutton had a
[06:11] completely different take on large
[06:12] language models and the bitter lesson.
[06:15] So, I mean, it's interesting because you
[06:17] wrote this essay in 2019 titled The
[06:19] Bitter Lesson, and this is the most
[06:21] influential essay perhaps in the history
[06:23] of AI, but people have used that as a
[06:29] justification
[06:30] for scaling up LLMs because in their
[06:34] view, this is the one scalable way we
[06:36] have found to pour ungodly amounts of
[06:39] compute into learning about the world.
[06:41] And so it's interesting that your
[06:42] perspective is that the LLMs are
[06:45] actually not bitter lesson.
[06:47] >> It's an interesting question whether uh
[06:49] large language models are are uh a case
[06:53] of the bitter lesson.
[06:55] >> Yeah.
[06:55] >> Because they are clearly um a a way of
[06:59] using massive computation things that
[07:02] will scale with computation up to up to
[07:05] the limits of the internet.
[07:06] >> Yeah.
[07:08] uh but they're also a way of putting in
[07:11] lots of um human knowledge and uh so so
[07:17] this is an interesting question um it's
[07:19] a sociological or industry question uh
[07:24] will they reach the limits of of of the
[07:28] data and and be superseded by things
[07:32] that that are can get more data just
[07:36] from experience rather than from uh from
[07:40] people. Uh in some ways it's a classic
[07:43] case of the of the of the bitter lesson
[07:46] with the more the more human knowledge
[07:48] we put into the large language models
[07:50] the better they can do and so it feels
[07:52] good. Um
[07:54] and yet uh one well I in particular
[07:59] expect there to be systems that can
[08:01] learn from experience which could well
[08:03] perform much much better and be much
[08:05] more scalable. In which uh case it will
[08:09] be another instance of the bitter lesson
[08:11] that the things that that used human
[08:14] knowledge were eventually superseded by
[08:17] things that just um trained from uh
[08:21] experience and computation.
[08:23] >> This is such a remarkable moment. Sutton
[08:26] is basically telling us that much of the
[08:28] field has interpreted his essay in
[08:29] exactly the wrong way. that large
[08:32] language models are an example of the
[08:34] bitter lesson, but a negative example,
[08:37] one that like Harpy relies far too much
[08:39] on human knowledge since LLMs are
[08:42] trained on human generated text.
[08:45] So, is Sutton right? Will LLMs hit a
[08:48] performance barrier due to their
[08:50] reliance on human knowledge and need to
[08:52] be replaced with very different types of
[08:54] AI systems? Sutton ends the bitter
[08:57] lesson with these lines.
[08:59] We want AI agents that can discover like
[09:02] we can, not which contain what we have
[09:04] discovered.
[09:07] Building in our discoveries only makes
[09:09] it harder to see how the discovering
[09:11] process can be done.
[09:14] So what would an AI system look like
[09:16] that can discover like we can? The
[09:19] primary way large language models are
[09:21] trained today is through supervised
[09:22] learning. Given some training text, for
[09:25] example, the first line of Harry Potter,
[09:28] the text is broken into little pieces
[09:29] known as tokens, and the model is
[09:32] trained to predict the next token given
[09:34] all the tokens that come before. So
[09:36] given the input Mr. and Mrs. Dersley of,
[09:39] the model is trained to predict the
[09:41] token for the word number. And given the
[09:43] input Mr. and Mrs. Dersley of number,
[09:46] the model is trained to predict the
[09:47] token for the word for and so on.
[09:51] Token by token, we're teaching the model
[09:53] what to say. And Sutton's criticism here
[09:56] is that like Harpy, this process relies
[09:58] too much on human knowledge since we're
[10:01] training our model to imitate humans.
[10:04] So, how else might we train AI systems?
[10:08] Sutton is generally known as the father
[10:10] of reinforcement learning. One of the
[10:12] most compelling modern examples of AI
[10:14] systems trained using reinforcement
[10:16] learning instead of supervised learning
[10:18] are Google Deep Minds Alph Go and Alph
[10:20] Go Zero agents.
[10:22] Now, Alph Go and Alph Go Zero are game
[10:25] playing agents, not large language
[10:27] models, but there are some really
[10:29] interesting parallels here.
[10:32] Now, before we see exactly how
[10:34] reinforcement learning allows us to push
[10:36] beyond the limits of human knowledge, if
[10:38] you're someone who's obsessed with this
[10:39] stuff and looking for your next career
[10:41] move, check out this video sponsor,
[10:43] Tufalabs. Tufalabs recently won the ARC
[10:46] AGI3 preview competition, where AI
[10:49] agents must learn to play and win
[10:51] completely novel games that the agents
[10:53] developers have never seen before. Tufa
[10:57] Labs is an independent AI lab based in
[10:59] Zurich and puts out really interesting
[11:01] research on the frontiers of LLMs and
[11:03] reinforcement learning. In this recent
[11:05] paper, the team achieved very impressive
[11:08] performance on the MIT integration B
[11:10] challenge by creating a self-improvement
[11:13] loop where an LLM creates its own math
[11:16] practice problems and learns to solve
[11:18] them via reinforcement learning. Tufa
[11:21] Labs is serious about compute and is
[11:23] currently expanding their infrastructure
[11:25] with two Nvidia NVL72 GB300 racks which
[11:30] is a significant amount of compute given
[11:32] the relatively small team size. TUFALabs
[11:35] is fully self-funded by applying ML to
[11:38] quantitative finance. This funding
[11:40] structure is similar to deepseats. If
[11:42] this sounds interesting, you can apply
[11:44] at tufalabs.ai/join.
[11:47] Now back to the bidder lesson. When
[11:50] building Alph Go, the first AI system
[11:52] that reached superhuman performance on
[11:54] the board game Go, the DeepMind team
[11:57] first trained a supervised policy
[11:59] network. In the jargon of reinforcement
[12:01] learning, an agent's policy determines
[12:04] what action an agent will take in a
[12:06] given state. In the game of Go, the
[12:09] current state is the board position, and
[12:12] the action is where the agent will place
[12:13] its next stone on the board. The
[12:16] DeepMind team used a deep neural network
[12:18] to learn this policy. This part of
[12:21] DeepMind's solution is strikingly
[12:22] similar to large language model
[12:24] training. Given some input text, large
[12:27] language models return a probability for
[12:30] each token the model could say next. And
[12:32] given an input board position, Alph Go's
[12:35] policy network returns a probability for
[12:37] each board position where Alph Go could
[12:39] place a stone.
[12:41] Note that Alph Go used a convolutional
[12:43] architecture while LLMs generally use
[12:46] transformers. But this distinction isn't
[12:48] really significant for our comparison
[12:50] here.
[12:52] Very similar to LLM training, Alph Go's
[12:54] policy network was first trained using
[12:56] supervised learning on human generated
[12:58] examples, learning to match expert human
[13:01] players moves in recorded games. The
[13:05] resulting supervised learning trained
[13:06] policy network is a fairly competent Go
[13:09] player. Evaluating the model in a
[13:11] tournament against other GO agents
[13:13] resulted in an ELO rating of 1517
[13:17] putting the network at mid amateur
[13:19] level.
[13:21] Now in the reinforcement learning
[13:22] paradigm agents learn not from direct
[13:25] supervision but instead through
[13:27] interacting with their environments.
[13:29] In the case of Alph Go, this just means
[13:32] taking the very natural approach of
[13:34] learning from actually playing the game.
[13:37] The DeepMind team took their trained
[13:39] supervised policy network and had it
[13:41] play against various versions of itself.
[13:44] After each game, the moves taken by the
[13:46] winning model were used as positive
[13:48] training examples to train the policy
[13:51] network. And the moves taken by the
[13:53] losing model were used as negative
[13:55] examples. This training process is very
[13:58] similar to learning from human expert
[14:00] moves.
[14:01] The key difference here is that these
[14:02] moves are generated by two policy
[14:04] networks actually playing go and the
[14:07] underlying signal the model learns from
[14:09] is not the opinion of a human expert but
[14:12] instead the outcome of a real game. This
[14:15] approach is known as a policy gradient
[14:17] method and is a key technique in
[14:19] reinforcement learning initially
[14:21] developed by Sutton and others in the
[14:22] 1990s.
[14:24] Now, it turns out that the reinforcement
[14:26] learning trained policy network alone
[14:28] was not enough to deliver superhuman Go
[14:31] performance.
[14:33] The DeepMind team needed one more big
[14:35] idea from reinforcement learning.
[14:39] It turns out there's another way to set
[14:40] up our learning problem here, and it's
[14:42] actually an older and arguably more
[14:44] central reinforcement learning idea than
[14:47] the policy gradient method we've seen.
[14:50] Instead of training a network to predict
[14:52] the move that should come next, what if
[14:54] we trained a network to measure the
[14:56] quality of a given board position
[14:59] or more concretely to estimate the
[15:01] probability of winning starting from a
[15:03] given board position.
[15:05] This approach is broadly known in
[15:06] reinforcement learning as value function
[15:08] estimation where the term value refers
[15:11] to expected future rewards in this case
[15:14] winning the game.
[15:16] Value functions play a central role in
[15:18] Sutton's canonical text on reinforcement
[15:20] learning. The most important component
[15:23] of almost all reinforcement learning
[15:25] algorithms we consider is a method for
[15:28] efficiently estimating values.
[15:30] The central role of value estimation is
[15:32] arguably the most important thing that
[15:35] has been learned about reinforcement
[15:36] learning over the last six decades.
[15:39] To make use of this reinforcement
[15:41] learning idea, the Google DeepMind team
[15:44] trained a second neural network that
[15:45] they called a value network. This
[15:48] network took in the same board position
[15:50] inputs as our policy network. But
[15:53] instead of predicting what move should
[15:54] come next, the value network predicts
[15:57] the probability of Alph Go winning the
[15:58] game from that position.
[16:01] The DeepMind team trained their value
[16:03] network on board positions from games
[16:05] between different versions of Alph Go.
[16:07] again avoiding learning from human
[16:09] gameplay.
[16:10] Finally, the DeepMind team brought
[16:12] together their policy and value network
[16:14] with a method called Monte Carlo tree
[16:16] search to create a formidable Go agent.
[16:20] The policy network allows Alph Go to
[16:22] narrow down the number of next possible
[16:24] moves, while the value network provides
[16:27] a strong estimate of the probability of
[16:29] winning if Alph Go continues playing
[16:31] down a given branch of the tree.
[16:35] Alph Go famously went on to defeat Lisa
[16:37] Dole in 2016, the second ranked Go
[16:40] player in the world at the time. The
[16:42] following year, the DeepMind team
[16:44] revealed Alph Go Zero, an even stronger
[16:47] player than Alph Go that remarkably did
[16:50] not learn from any human games. Instead,
[16:52] relying only on reinforcement learning
[16:54] from real gameplay.
[16:57] By learning from real interactions with
[16:59] their environments, Alph Go and Alph Go
[17:01] Zero dramatically outperformed agents
[17:03] trained to imitate human gameplay using
[17:06] supervised learning,
[17:08] discovering their own ways to play the
[17:10] game. Alph Go's playing style has been
[17:13] described by experts as playing against
[17:15] an alien and is from an alternate
[17:17] dimension.
[17:19] These are the types of AI systems that
[17:21] Sutton is referring to when he says,
[17:23] >> "Oh, well, I in particular expect there
[17:26] to be systems that can learn from
[17:27] experience and which could well perform
[17:29] much much better and be much more
[17:31] scalable."
[17:32] >> This really makes me wonder if our
[17:35] current generation of language models
[17:36] are constrained in the same way as the
[17:39] AlphaGo policy network that was trained
[17:41] with supervised learning was unable to
[17:43] discover on their own limited to
[17:45] imitating human language and
[17:47] intelligence.
[17:49] Now, it's important to note here that
[17:50] reinforcement learning does already play
[17:52] an important role in large language
[17:54] model training.
[17:56] After LLMs are trained on next token
[17:58] prediction using supervised learning,
[18:00] reinforcement learning through human
[18:02] feedback or RLHF is used to align models
[18:05] to human preferences using reinforcement
[18:07] learning techniques. And a great deal of
[18:10] recent LLM progress has been driven by
[18:13] reasoning models that make use of
[18:15] reinforcement learning with verifiable
[18:17] rewards or RLVR
[18:20] where LLMs are trained with
[18:21] reinforcement learning to find their own
[18:23] paths to solving problems with known
[18:25] answers such as math problems and
[18:27] coding. Pre-training on human generated
[18:30] text and then using reinforcement
[18:32] learning to allow models to discover on
[18:34] their own is an exciting direction, but
[18:37] it remains to be seen how far this
[18:39] approach can take us.
[18:42] In 2025, David Silver, the lead
[18:45] researcher of the AlphaGo project,
[18:47] teamed up with Richard Sutton to write
[18:48] an essay called Welcome to the Era of
[18:51] Experience.
[18:53] Silver and Sutton argue that LLMs are
[18:55] currently limited by human knowledge,
[18:57] giving an interesting thought
[18:58] experiment. If we trained an LLM on
[19:01] human knowledge from 5,000 years ago, it
[19:04] would reason about the physical world in
[19:05] terms of animism.
[19:08] If we trained on human knowledge from a
[19:09] thousand years ago, it would reason in
[19:11] theistic terms, 300 years ago in terms
[19:14] of Newtonian physics, and 50 years ago
[19:17] in terms of quantum physics.
[19:20] Moving from one paradigm to the next
[19:22] requires actually interacting with the
[19:24] physical world as Silver and Sutton say
[19:27] in order to overturn facious methods of
[19:30] thought.
[19:32] From here, Sutton and Silver argue that
[19:34] we're on the threshold of a new era of
[19:36] AI where agents will learn from real
[19:39] world reward signals instead of human
[19:41] knowledge, discovering new ways to
[19:44] optimize measures like cost, health
[19:46] metrics, climate metrics, profits,
[19:48] sales, and energy consumption.
[19:52] Sutton and Silver give the example of
[19:54] DeepMind's alpha proof agent which
[19:56] combines LLMs and reinforcement learning
[19:58] to discover its own very impressive
[20:00] methods of mathematical reasoning.
[20:04] So, have we learned the bitter lesson or
[20:06] are we just repeating it? When we look
[20:09] back on LLMs one day, will they feel
[20:11] like harpy so clearly limited by human
[20:15] knowledge? And if so, is reinforcement
[20:18] learning the answer? And can LLM serve
[20:21] as the scaffolding that unlocks this
[20:23] next frontier? Or do we need to try
[20:25] something totally different?
[20:27] My take here is that the bitter lesson
[20:30] in Sutton and Silver's reinforcement
[20:32] learning perspectives form a really
[20:34] helpful lens onto the limitations of our
[20:37] current generation of AI.
[20:40] I'm more skeptical about a reinforcement
[20:42] learning renaissance being around the
[20:43] corner.
[20:45] mostly because the domains we've seen
[20:47] reinforcement learning perform really
[20:48] well in like playing games, mathematical
[20:50] proofs, and coding, still feel very
[20:53] removed to me from many of the real
[20:55] world problems that we care about.
[20:58] Either way, it will be fascinating to
[21:00] see what happens next.
[21:05] The Welsh Labs team and I have written a
[21:07] whole new book on AI. It's beautifully
[21:10] illustrated and is a great way to dig
[21:12] deeper into the topics we cover in these
[21:14] videos. This is the book I've always
[21:17] wanted to write. We've really leaned
[21:19] into the visuals. The book has hundreds
[21:22] of figures. I especially like these full
[21:24] page spreads. This one shows how lost
[21:27] landscapes are computed.
[21:30] On the next page, we jump into this
[21:31] super highquality overhead contour plot
[21:34] view of our landscape.
[21:36] and we show how we might expect our
[21:38] model to work its way through valleys to
[21:40] reach its global minimum, but it instead
[21:42] creates what looks like a wormhole on
[21:44] our lost landscape.
[21:46] We're putting a huge amount of effort
[21:48] into each chapter to create these kinds
[21:50] of visuals and deep explanations, trying
[21:53] to give the most visceral feel we can
[21:55] for how this stuff really works.
[21:58] Each chapter includes supporting Python
[21:59] code that walks through the key results
[22:01] from that chapter. And there's also a
[22:04] supporting GitHub repo as well that's a
[22:06] bit more comprehensive.
[22:08] At the end of each chapter, you'll also
[22:10] find exercises. We've put a ton of
[22:13] thought into these. Here's an exercise
[22:16] from the chapter on back propagation
[22:18] where you're given a small complete
[22:19] neural network and asked to move some
[22:22] data through the network using a few
[22:23] equations.
[22:25] Then you're asked to compute the
[22:26] network's gradients and use your
[22:28] computed gradients to fill in steps in
[22:30] the model's real learning process.
[22:33] These exercises are designed to get you
[22:34] as hands-on as possible with modern AI
[22:37] and solutions are in the back of the
[22:39] book. Most of the exercises are written
[22:41] or programming, but my favorite is
[22:43] probably this spread that gives you
[22:45] instructions for building your own
[22:46] perceptron machine.
[22:49] The book starts with a fresh take on the
[22:51] fundamentals, the perceptron, gradient
[22:53] descent, back propagation, deep models,
[22:55] and alexet.
[22:57] and then uses this foundation to dive
[22:59] into cutting edge topics including
[23:01] neural scaling laws, mechanistic
[23:03] interpretability, and AI image and video
[23:06] generation models like Sora.
[23:08] Each chapter goes along with a Welch
[23:10] Labs video that came out over the last
[23:12] 18 months. I really think that the book
[23:15] is the best way to get deeper into each
[23:17] video's topic.
[23:19] The book is great for self-study, AI
[23:22] courses, or just looks great on your
[23:24] coffee table.