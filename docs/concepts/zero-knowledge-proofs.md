---
title: "Zero-Knowledge Proofs"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [cryptography, ai-ml, science]
sources:
  - type: web
    url: "https://en.wikipedia.org/wiki/Zero-knowledge_proof"
    title: "Zero-knowledge proof (Wikipedia)"
    date: 2026-06-07
confidence: high
contested: false
---

# Zero-Knowledge Proofs

A **zero-knowledge proof** (ZKP) is a cryptographic protocol in which one party (**prover**) convinces another party (**verifier**) that a statement is true, without revealing any information beyond the fact of its truth. The core challenge: proving possession of secret knowledge *without* disclosing the secret itself or any aspect of it.

## Three Properties

Every ZKP must satisfy three conditions [1]:

- **Completeness** — If the statement is true, an honest verifier following the protocol will be convinced by an honest prover.
- **Soundness** — If the statement is false, no cheating prover can convince an honest verifier except with negligible probability (the *soundness error*).
- **Zero-knowledge** — The verifier learns nothing beyond the truth of the statement. Formally: for any verifier, a simulator exists that produces indistinguishable transcripts without access to the prover's secret.

ZKPs are probabilistic, not deterministic — there is always a small soundness error (e.g., 1/2^k after k rounds). This decreases exponentially with repetition.

## Intuition: Abstract Examples

### The Ali Baba Cave [1]
Peggy knows a magic word that opens a door in a ring-shaped cave. Victor waits outside as Peggy enters via path A or B (Victor doesn't see which). Victor then randomly calls out "A" or "B". If Peggy knows the word, she always emerges from the correct path. Without it, she succeeds only 50% per round — after 20 rounds, probability of cheating drops to ~1 in a million.

### Red Card Proof [1]
Peggy draws a card and must prove it's red without revealing which one. She shows all 26 black cards from the remaining deck. Victor concludes her hidden card is red but learns nothing about its suit or rank. Even a recording of this proof cannot convince third parties — it's *special* zero-knowledge.

### Where's Waldo [1]
Prover covers a Waldo page with a board that has a small hole, positioned over Waldo. Verifier sees only Waldo through the hole — proven knowledge of location without revealing coordinates.

## Formal Definition

In computational terms: Let P (prover), V (verifier), and S (simulator) be Turing machines. An interactive proof system (P,V) for language L is zero-knowledge if for any probabilistic polynomial-time verifier Ŵ, there exists a PPT simulator S such that:

`View_Ŵ[P(x) ↔ Ŵ(x,z)] ≈ S(x,z)`

The verifier's view of the interaction is computationally indistinguishable from what the simulator produces given only the statement — meaning the verifier gains no useful information.

Three levels of zero-knowledge [1]:
- **Perfect ZK** — Simulator output is *identically* distributed to real interaction
- **Statistical ZK** — Distributions are statistically close (negligible distance)
- **Computational ZK** — Distributions are computationally indistinguishable (no PPT algorithm can tell them apart)

## Interactive vs Non-Interactive

### Interactive ZKPs [1]
Prover and verifier exchange multiple messages. The original Goldwasser-Micali-Wigderson (GMW) protocol from 1985 was interactive. Required for non-trivial proofs in the standard model.

### Non-Interactive ZKPs (NIZK) [1]
A single prover message convinces the verifier — no back-and-forth needed. Achieved via:
- **Common Reference String (CRS)** model — a shared random string trusted by both parties
- **Random Oracle** model — idealized hash functions
- **Fiat-Shamir heuristic** — transforms interactive proofs into non-interactive ones by replacing verifier challenges with hash outputs

## Practical Cryptographic Applications

### Discrete Logarithm Proof [1]
Peggy proves she knows x such that g^x ≡ y (mod p) without revealing x. Protocol per round:
1. Peggy picks random r, computes C = g^r mod p, sends to Victor
2. Victor randomly requests either r or (x+r) mod (p-1)
3. Victor verifies: if r requested, checks g^r ≡ C; if (x+r) requested, checks g^(x+r) ≡ C·y

If Peggy doesn't know x, she can only prepare for one challenge — Victor's random choice catches her 50% per round.

### Commitment Schemes [1]
A commitment binds a party to a value while keeping it hidden until revealed. Like sealing a message in an envelope:
- **Binding** — cannot change the committed value after committing
- **Hiding** — committed value is concealed until opening

Used as building blocks for ZKPs, digital signatures, and secure multi-party computation.

## Succinct Arguments: SNARKs & STARKs

### zk-SNARKs [1]
**Succinct Non-Interactive Arguments of Knowledge** — proofs that are:
- **Succinct** — proof size is tiny (often < 200 bytes), verification is fast (< milliseconds)
- **Non-interactive** — single message, no back-and-forth
- **Argument** — computationally sound (not perfectly sound)
- **Knowledge** — proves the prover *knows* a witness

Key property: proof size and verification time are independent of computation complexity. Proving 1 million operations takes as long to verify as proving 1 operation.

Trade-off: requires a trusted setup (CRS generation ceremony). If CRS is compromised, fake proofs become possible.

### zk-STARKs [1]
**Scalable Transparent Arguments of Knowledge** — similar to SNARKs but:
- **Transparent** — no trusted setup needed; relies on publicly verifiable randomness
- **Quantum-resistant** — based on collision-resistant hash functions, not elliptic curves
- Larger proof sizes (~10-100 KB vs ~200 bytes for SNARKs)
- Slower verification but faster proving

### Bulletproofs [1]
Range proofs that prove a value lies within a range without revealing the value. Key features:
- No trusted setup
- Logarithmic proof size (O(log n) instead of O(n))
- Used in Monero for private transaction amounts

## Applications Beyond Cryptography

### Blockchain & Privacy Coins [1]
- **Zcash** — uses zk-SNARKs (Groth16) to hide sender, receiver, and amount. "Shielded" transactions prove validity without revealing details
- **Monero** — uses RingCT + Bulletproofs for private amounts
- **ZK-Rollups** (StarkNet, zkSync, Polygon zkEVM) — batch thousands of transactions off-chain, post a single ZKP to Ethereum proving all transactions are valid. 10-100x throughput increase with full security

### Authentication [1]
Prove identity without revealing passwords or biometric data. The prover demonstrates knowledge of a secret (password hash, private key) without transmitting it — immune to man-in-the-middle attacks.

### Secure Multi-Party Computation [1]
Multiple parties jointly compute a function over their inputs while keeping those inputs private. ZKPs ensure each party follows the protocol correctly without revealing intermediate values.

### Voting Systems [1]
Prove a vote was cast correctly (one person, one valid ballot) without revealing how anyone voted. Enables verifiable elections with full privacy.

### Supply Chain & Compliance [1]
Prove goods meet regulatory standards (e.g., carbon footprint below threshold, ingredients are organic) without disclosing proprietary manufacturing details or supplier information.

## Key Researchers & Timeline

- **1985** — Goldwasser, Micali & Wigderson introduce ZKPs; prove NP ⊆ IP for interactive proofs [1]
- **1988** — Babai & Moran show AM = MA, expanding understanding of interactive proof complexity [1]
- **1990** — Quisquater et al. publish "How to Explain Zero-Knowledge Protocols to Your Children" (Ali Baba cave) [1]
- **2010s** — zk-SNARKs developed (Groth16, Pinocchio), enabling practical blockchain privacy [1]
- **2018** — StarkWare introduces zk-STARKs; Zcash launches with SNARK-based privacy [1]
- **2020s** — ZK-Rollups become dominant Ethereum scaling solution; STARK-based L2s (StarkNet) deploy [1]

## Open Questions & Research Frontiers

- **Universal SNARKs** — proving arbitrary computations without circuit-specific setup
- **Recursive ZKPs** — composing proofs within proofs for massive scalability
- **Post-quantum ZKPs** — STARKs are quantum-resistant; SNARK security under quantum attack is debated
- **Hardware acceleration** — GPU/ASIC provers reducing proof generation from minutes to seconds
- **AI verification** — using ZKPs to prove LLM outputs were generated correctly (verifiable AI)

## Related Concepts

[[cryptography]] — broader field of secure communication and data protection
[[blockchain-scaling]] — ZK-Rollups as Layer 2 scaling solutions
[[secure-multi-party-computation]] — joint computation with private inputs
[[post-quantum-cryptography]] — algorithms resistant to quantum computing attacks
