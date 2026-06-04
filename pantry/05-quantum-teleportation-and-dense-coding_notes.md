# Research Notes: Chapter 05 — Quantum Teleportation and Dense Coding

**Corresponding chapter:** chapters/05-quantum-teleportation-and-dense-coding.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (a) state the no-cloning theorem and give the one-paragraph proof from inner products; (b) trace the quantum teleportation protocol for |ψ⟩ = α|0⟩ + β|1⟩ through all four measurement outcomes and identify the corrective gate for each; (c) explain why teleportation does not violate no-cloning (the original is destroyed) and does not transmit information faster than light (the classical channel is required to choose the correction); (d) trace the superdense coding protocol (which two Pauli operations Alice applies, what Bell state results, how Bob decodes); (e) articulate the sense in which teleportation and dense coding are "dual" protocols.

---

## A. Conceptual foundations

### A1. The no-cloning theorem (backdrop for everything)

**Statement:** There is no unitary operation U that maps |ψ⟩|s⟩ → |ψ⟩|ψ⟩ for all normalized single-qubit states |ψ⟩ and all fixed "blank" states |s⟩.

**Proof (PennyLane / Nielsen-Chuang style — inner product argument):**
Suppose such a U exists. Then:
  U(|ψ⟩|s⟩) = |ψ⟩|ψ⟩
  U(|φ⟩|s⟩) = |φ⟩|φ⟩

Take the inner product of the left-hand sides:
  ⟨ψ|φ⟩⟨s|s⟩ = ⟨ψ|φ⟩  (since ⟨s|s⟩ = 1)

Take the inner product of the right-hand sides:
  ⟨ψ|φ⟩² 

Since U is unitary, these must be equal: ⟨ψ|φ⟩ = ⟨ψ|φ⟩².

The only complex numbers that satisfy c = c² are c = 0 and c = 1. So either:
- ⟨ψ|φ⟩ = 0: the states are orthogonal, or
- ⟨ψ|φ⟩ = 1: the states are identical.

Therefore U cannot clone two non-orthogonal, non-identical states. Since most pairs of states are neither orthogonal nor identical, no universal quantum cloner exists.

**Origin:** Wootters & Zurek (1982) and Dieks (1982), independently, in *Nature* and *Physics Letters A* respectively — both published as responses to Herbert's FLASH paper, which had proposed using no-cloning-violating cloning to signal faster than light. The theorem closes that loophole.

**Consequences:**
- Quantum information cannot be copied; it can only be moved.
- This is why teleportation destroys the original.
- This is why quantum key distribution is secure: an eavesdropper cannot copy qubits without disturbing them.
- Orthogonal states *can* be cloned (because a CNOT-based circuit clones |0⟩ and |1⟩). It is only unknown/arbitrary states that cannot be cloned.

### A2. Quantum teleportation: the protocol

**Dramatis personae:** Alice (sender) and Bob (receiver), possibly spacelike separated. Alice has qubit S in unknown state |ψ⟩ = α|0⟩ + β|1⟩ that she wants to send to Bob. She cannot send qubit S directly (assume the quantum channel is unavailable). She has only a classical telephone/channel.

**Resource:** Alice and Bob share one Bell pair. Qubit A belongs to Alice, qubit B belongs to Bob:
  |Φ⁺⟩_{AB} = (|00⟩ + |11⟩)_{AB}/√2

**The protocol (Bennett, Brassard, Crépeau, Jozsa, Peres, Wootters — 1993, Phys. Rev. Lett. 70, 1895):**

**Step 1 — State preparation.** Alice initializes the three-qubit system:
  |ψ⟩_S ⊗ |Φ⁺⟩_{AB}

**Step 2 — Shared entanglement.** Alice holds qubits S and A; Bob holds qubit B. The total state of the three-qubit system is:
  |Ψ₀⟩ = (α|0⟩ + β|1⟩)_S ⊗ (|00⟩ + |11⟩)_{AB}/√2

Expanding:
  |Ψ₀⟩ = (1/√2)(α|000⟩ + α|011⟩ + β|100⟩ + β|111⟩)_{SAB}

**Step 3 — Change of basis (Alice applies CNOT then H).** Alice applies CNOT to her two qubits (S as control, A as target), then H to S.

After CNOT (S→A):
  |Ψ₁⟩ = (1/√2)(α|000⟩ + α|011⟩ + β|110⟩ + β|101⟩)

After H on S:
  H|0⟩ = (|0⟩+|1⟩)/√2, H|1⟩ = (|0⟩−|1⟩)/√2.
  |Ψ₂⟩ = (1/2)(α|000⟩ + α|100⟩ + α|011⟩ + α|111⟩ + β|010⟩ − β|110⟩ + β|001⟩ − β|101⟩)

Regrouping by Alice's two-qubit measurement outcomes (SA):
  |Ψ₂⟩ = (1/2)[
    |00⟩_{SA}(α|0⟩ + β|1⟩)_B     ← Bob has |ψ⟩; no correction needed
  + |01⟩_{SA}(β|0⟩ + α|1⟩)_B     ← Bob has X|ψ⟩; apply X
  + |10⟩_{SA}(α|0⟩ − β|1⟩)_B    ← Bob has Z|ψ⟩; apply Z
  + |11⟩_{SA}(−β|0⟩ + α|1⟩)_B   ← Bob has XZ|ψ⟩; apply Z then X (= iY|ψ⟩ up to phase)
  ]

**Step 4 — Alice measures.** Alice measures her two qubits (S and A) in the computational basis. She gets one of four equally probable outcomes (each with probability 1/4). Bob's qubit instantly collapses to one of the four states above.

**Step 5 — Classical communication.** Alice calls Bob with her 2-bit outcome. Bob applies the corrective gate:
  - Outcome 00: apply I (identity) — already |ψ⟩.
  - Outcome 01: apply X — recovers |ψ⟩.
  - Outcome 10: apply Z — recovers |ψ⟩.
  - Outcome 11: apply X then Z (or iY) — recovers |ψ⟩.

**Result:** Bob's qubit is now in state |ψ⟩ = α|0⟩ + β|1⟩ exactly, for any α and β, regardless of which measurement outcome Alice obtained.

### A3. Why teleportation does NOT violate no-cloning

After Alice's measurement in Step 4, qubit S is no longer in state |ψ⟩ — it has been measured and collapsed. The original state is *destroyed* by the Bell measurement. Bob gains the state; Alice no longer has it. No duplication occurred. This is consistent with (and required by) no-cloning.

Concretely: before Alice's measurement, the full state is an entangled superposition — qubit S does not individually have state |ψ⟩ at that point. After measurement, S is in a definite computational basis state |0⟩ or |1⟩ (not |ψ⟩). The state information has been transferred to Bob.

### A4. Why teleportation does NOT send information faster than light

Before Bob receives Alice's 2-bit classical message, he cannot distinguish his qubit's state from random noise. His reduced density matrix (tracing out Alice's qubits) is the maximally mixed state (I/2) regardless of which outcome Alice got. No information about α or β reaches Bob until the classical bits arrive. The classical bits travel at most at the speed of light. Therefore no superluminal signaling occurs.

More formally: the no-communication theorem (also called the no-signaling theorem) states that Alice's choice of measurement basis does not affect the marginal probability distribution of Bob's measurement outcomes. This is a consequence of the structure of quantum mechanics (trace-out linearity). Entanglement alone cannot send information.

**The precise accounting:**
- What was shared in advance: one Bell pair (transmitted at ≤ c at some earlier time).
- What crosses the gap instantaneously: nothing physical — the entanglement correlation is non-local but not informative without the classical key.
- What travels at ≤ c: 2 classical bits.
- Net effect: transmission of 1 unknown quantum state (2 complex numbers subject to normalization and global phase, so effectively 2 real parameters) using 1 ebit of entanglement and 2 classical bits.

### A5. Superdense coding: the dual protocol

**Reference:** Bennett & Wiesner (1992), "Communication via One- and Two-Particle Operators on Einstein-Podolsky-Rosen States," *Physical Review Letters* 69, 2881. First conceived by Wiesner around 1968–1970; published 1992.

**The insight:** If teleportation uses 1 ebit + 2 classical bits to send 1 qubit of information, then running the "dual" protocol should use 1 ebit + 1 qubit channel to send 2 classical bits. This is superdense coding.

**Protocol:**

Setup: Alice and Bob share |Φ⁺⟩_{AB} = (|00⟩+|11⟩)/√2. Alice holds qubit A; Bob holds qubit B.

Alice wants to send one of four messages: 00, 01, 10, 11. She applies one of four local unitary operations to her qubit A only:

| Message | Alice applies | Resulting Bell state of AB |
|---------|--------------|---------------------------|
| 00      | I (identity) | |Φ⁺⟩ = (|00⟩+|11⟩)/√2    |
| 01      | X            | |Ψ⁺⟩ = (|01⟩+|10⟩)/√2    |
| 10      | Z            | |Φ⁻⟩ = (|00⟩−|11⟩)/√2    |
| 11      | iY (or XZ)   | |Ψ⁻⟩ = (|01⟩−|10⟩)/√2   |

Alice then physically sends her qubit A to Bob through the quantum channel (1 qubit transmitted).

Bob now holds both qubits. He performs a Bell measurement (CNOT with A as control, B as target; then H on A; then measure both). The four Bell states are orthogonal and hence perfectly distinguishable. Bob reads off two classical bits — Alice's message — with certainty.

**Result:** 2 classical bits transmitted by sending 1 qubit, given 1 pre-shared ebit. Without the pre-shared entanglement, sending 1 qubit can convey at most 1 classical bit of information (Holevo bound). Entanglement doubles the classical capacity.

### A6. Teleportation and dense coding as dual protocols

The two protocols are dual to each other in a precise sense:
- Teleportation: 2 classical bits + 1 ebit → transmit 1 qubit (quantum state).
- Dense coding: 1 qubit + 1 ebit → transmit 2 classical bits (classical information).

Both require a pre-shared entangled pair. Neither is "free": in teleportation, the qubit must still be described by the 2 classical bits (of outcome) sent over the wire. In dense coding, the 2 classical bits are encoded by a quantum manipulation of the shared pair, but the physical channel still carries a qubit. The entanglement is the "resource" that boosts classical or quantum channel capacity.

This duality is a clean introduction to the broader theme of the chapter: entanglement is a resource with quantifiable power — it can substitute for, or amplify, classical and quantum communication.

---

## B. Domain examples and cases

### B1. Worked example: full teleportation trace for all four outcomes

**Setup:** Alice has |ψ⟩ = α|0⟩ + β|1⟩. Shared Bell pair: |Φ⁺⟩_{AB}.

After the CNOT and Hadamard steps, the three-qubit state (from A3) is:
  |Ψ₂⟩ = (1/2)[
    |00⟩(α|0⟩+β|1⟩) + |01⟩(β|0⟩+α|1⟩) + |10⟩(α|0⟩−β|1⟩) + |11⟩(−β|0⟩+α|1⟩)
  ]

**Outcome 00 (prob 1/4):** Bob's qubit → α|0⟩+β|1⟩ = |ψ⟩. Correction: I.
**Outcome 01 (prob 1/4):** Bob's qubit → β|0⟩+α|1⟩ = X|ψ⟩. Correction: apply X.
  Verify: X(β|0⟩+α|1⟩) = α|0⟩+β|1⟩ = |ψ⟩. ✓
**Outcome 10 (prob 1/4):** Bob's qubit → α|0⟩−β|1⟩ = Z|ψ⟩. Correction: apply Z.
  Verify: Z(α|0⟩−β|1⟩) = α|0⟩+β|1⟩ = |ψ⟩. ✓
**Outcome 11 (prob 1/4):** Bob's qubit → −β|0⟩+α|1⟩ = XZ|ψ⟩ (up to global phase). Correction: apply Z then X.
  Verify: X(Z(−β|0⟩+α|1⟩)) = X(−β|0⟩−α|1⟩)… 
  More carefully: Z|ψ⟩ = α|0⟩−β|1⟩; XZ|ψ⟩ = α|1⟩−β|0⟩ = −(β|0⟩−α|1⟩).
  Applying ZX (= iY up to phase) to Bob's state (−β|0⟩+α|1⟩):
  Z(−β|0⟩+α|1⟩) = −β|0⟩−α|1⟩; X(−β|0⟩−α|1⟩) = −α|0⟩−β|1⟩ = −|ψ⟩.
  Global phase −1 is unobservable; Bob has |ψ⟩. ✓

**Key observation:** The correction table is exactly the lookup table of Pauli operators indexed by Alice's 2-bit outcome. The protocol is deterministic (Bob always gets |ψ⟩) despite each individual outcome being random.

### B2. Worked example: superdense coding — encode and decode

Alice wants to send message "10". She applies Z to her qubit of |Φ⁺⟩_{AB}:
  (I_B ⊗ Z_A)|Φ⁺⟩ = (1/√2)(Z|0⟩|0⟩ + Z|1⟩|1⟩) = (1/√2)(|00⟩ − |11⟩) = |Φ⁻⟩.

Alice sends qubit A to Bob. Bob applies CNOT (A control, B target):
  CNOT|Φ⁻⟩ = (1/√2)(|00⟩ − |10⟩) = (1/√2)(|0⟩−|1⟩)_A ⊗ |0⟩_B = |−⟩|0⟩.

Bob applies H to qubit A:
  H|−⟩ = |1⟩.

Bob measures: outcome 10. Message recovered: "10". ✓

### B3. Physical realizations (for concreteness)

Quantum teleportation has been experimentally demonstrated:
- **Bennett et al.'s original proposal (1993):** Theoretical paper, Phys. Rev. Lett. 70, 1895.
- **First experimental demonstrations (1997):** Bouwmeester et al. (*Nature* 390, 575) and Boschi et al. (*Phys. Rev. Lett.* 80, 1121) — both with photons, partial Bell-state measurements.
- **Long-distance teleportation:** Demonstrated over 143 km (Canary Islands, 2012) and later via satellite (Micius, 2017 — over 1200 km).
- **Teleportation within quantum networks:** Now a standard primitive in quantum repeater architectures; IBM quantum systems implement it as a demonstrable circuit.

---

## C. Connections and dependencies

- **Ch. 4 (gates and circuits):** Teleportation is the first major application of the H–CNOT Bell-state preparation circuit. The corrective gates (X, Z, I, XZ) are all single-qubit gates from Ch. 4. Students must be fluent with those before beginning this chapter.
- **Ch. 3 (entanglement and Bell states):** The four Bell states and their algebraic structure are prerequisites. The pantry file `_lib_qmsri-12-entanglement-and-quantum-information.md` provides this in prose form and explicitly includes the teleportation protocol (see grep results: lines 179–194).
- **Ch. 6 (decoherence and open systems):** Bell pairs decohere under environmental coupling, degrading the teleportation fidelity. The CHSH parameter S = 2√2 for a perfect Bell pair falls toward 2 (the classical boundary) as the pair becomes mixed. This chapter should mention that real-world teleportation runs against T₂ coherence times.
- **Quantum error correction:** Teleportation is a key primitive in quantum error correction codes (gate teleportation), quantum repeaters, and fault-tolerant architectures. This connection motivates why the protocol matters beyond its theoretical elegance.
- **Classical information theory:** Holevo's theorem bounds the classical information extractable from a qubit to at most 1 bit without entanglement assistance. Dense coding reaches 2 bits, saturating the entanglement-assisted Holevo bound. Mentioning this connects to Shannon information theory.

---

## D. Current state of the field

- **Quantum networks and repeaters:** Long-distance teleportation is the workhorse primitive of quantum networks. Quantum repeaters use chains of Bell pairs and teleportation to extend quantum communication beyond the decoherence length of direct fiber links. This is an active engineering problem in 2026; no complete quantum repeater has been deployed at scale, but testbed networks exist (QuTech in the Netherlands, the EPB quantum network in Chattanooga, TN).
- **Satellite quantum communication:** China's Micius satellite (2016–present) has demonstrated teleportation and quantum key distribution over >1000 km free-space links. This is the state-of-the-art for long-distance entanglement distribution.
- **Superdense coding experiments:** Experimentally demonstrated in photonic systems. Less practically important than teleportation currently, because the quantum channel carrying Alice's qubit still requires a photon — the bottleneck is quantum channel capacity, not classical channel capacity. Dense coding is more pedagogically than technologically significant at this stage.
- **Gate teleportation:** In fault-tolerant quantum computing, the T gate is implemented by "gate teleportation" using magic states (|T⟩ = T|+⟩). This requires a supply of high-fidelity |T⟩ states (magic state distillation) — the dominant resource cost of fault-tolerant computation. Ch. 5 should note this connection in a forward reference.
- **No-cloning in quantum cryptography:** The no-cloning theorem is the security foundation of BB84 (quantum key distribution). An eavesdropper who intercepts a qubit cannot clone it and pass on the original — the disturbance is detectable. This is the practical payoff of the abstract theorem.

---

## E. Teaching considerations

### E1. Pedagogy notes

- **No-cloning first, teleportation second.** Students who see teleportation before no-cloning will immediately ask "why not just copy it?" The proof in A1 should precede the protocol. The PennyLane tutorial (see source) structures the presentation exactly this way: "Problem: The No-Cloning Theorem" → "Solution: Quantum Teleportation."
- **The "destruction" of the original.** Many students expect teleportation to produce a copy at Bob while Alice retains hers (sci-fi "beam me up" model). The worked example in B1 makes explicit that Alice's qubit S is destroyed in the measurement step. Worth stating explicitly: "The original is not cloned — it is consumed."
- **The classical channel is not a technicality.** Students sometimes think the classical communication is just a formality. Stress: without those 2 bits, Bob's state is random (maximally mixed). The 2-bit message is the only thing that makes Bob's state determinate. And since those 2 bits travel ≤ c, teleportation respects causality.
- **The 4-outcome table.** Making students fill out the complete correction table for all four outcomes (the worked example in B1) is the most effective single exercise for this chapter. It forces engagement with the algebra and makes the protocol concrete.
- **Duality.** Dense coding's relationship to teleportation is a pedagogically satisfying "aha" moment. The symmetry should be stated explicitly: same resource (1 ebit), one direction sends a qubit for 2 cbits, the other direction sends 2 cbits for 1 qubit.
- **Deferred measurement principle.** PennyLane's tutorial demonstrates that mid-circuit measurements can be deferred to the end of the circuit by replacing classical-controlled corrections (X conditioned on m₁, Z conditioned on m₀) with CNOT and CZ gates respectively. This is worth a short discussion for students who will implement the circuit.

### E2. Common errors / misconceptions
- Thinking teleportation transmits |ψ⟩ faster than light ("the wavefunction collapses instantly on Bob's side").
- Confusing "the state is transferred" with "a copy is made."
- Getting the correction table wrong — especially the outcome 11 case, which requires XZ (or iY up to phase), not just X or Z.
- Confusing the Bell pair preparation (Alice and Bob each get one qubit at some earlier time) with the measurement step that uses those qubits.
- Thinking superdense coding violates the Holevo bound. (It does not: the Holevo bound is 1 classical bit per qubit *without* prior entanglement. Entanglement assistance changes the bound.)

### E3. Quantitative check for students
Students should be able to verify: given |ψ⟩ = |+⟩ = (|0⟩+|1⟩)/√2, trace the teleportation protocol. α = β = 1/√2. All four corrections should yield Bob's state (|0⟩+|1⟩)/√2 = |+⟩. Checking a specific state (rather than general α, β) reduces algebraic complexity while preserving the structure.

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/pantry/_lib_qmsri-12-entanglement-and-quantum-information.md` — contains a complete teleportation protocol description (lines 179–194 region): shared Bell pair, Bell-basis measurement, four corrections {I, Z, X, XZ}, statement that the original is destroyed, statement that two classical bits are required, explicit mention that no cloning occurs. Also includes a full LLM exercise (teleportation extension, lines 416–441) and a note on T₂ decoherence as the adversary (line 204). **Grep for:** "teleport", "Bell measurement", "classical bits", "no cloning", "two classical".

---

## G. Gaps and flags

1. **Partial Bell measurement.** Real experiments (e.g., photonic systems without number-resolving detectors) often cannot distinguish all four Bell states, achieving only partial teleportation fidelity. The idealized protocol assumed here uses a complete Bell measurement; note this gap for students who will read experimental papers.
2. **Entanglement fidelity.** The protocol assumes a perfect |Φ⁺⟩ Bell pair. In practice, pairs decohere (T₂ limited), so Bob receives a mixed state with fidelity F < 1. The chapter should briefly discuss teleportation fidelity as a metric; its connection to CHSH violation S is established in the library file.
3. **Gate teleportation not covered here.** The use of teleportation to implement non-Clifford gates (particularly T) is the key technique in fault-tolerant quantum computing. This is deferred to the error-correction chapter, but a forward reference is important.
4. **Quantum repeaters and routing.** The practical relevance of teleportation to quantum networks is mentioned (D section) but not worked through. A sidebar on quantum repeaters would be appropriate for students who ask "why does this matter?"
5. **Asymmetry of superdense coding vs. teleportation costs.** In practice, superdense coding requires a quantum channel (to send Alice's qubit); teleportation requires only a classical channel after Bell-pair distribution. Since quantum channels are harder to build than classical ones, teleportation is more practically significant. This asymmetry is worth a sentence.
6. **Multipartite teleportation.** GHZ-state teleportation and quantum secret sharing are natural extensions not covered here. Mention in a brief forward-looking paragraph.
7. **The "quantum country" reference.** Michael Nielsen and Andy Matuschak's interactive quantum teleportation essay at https://quantum.country/teleportation is an excellent supplementary reading (spaced-repetition format). Consider assigning it alongside the chapter.

---

## Primary sources

- **Nielsen, M. A. & Chuang, I. L. (2000).** *Quantum Computation and Quantum Information.* Cambridge University Press. [Canonical reference — Chapter 1.3.7 (teleportation), Section 2.3 (no-cloning theorem), Section 12.1 (dense coding). This is the gold standard; cite for all algebraic derivations.]
- **Bennett, C. H., Brassard, G., Crépeau, C., Jozsa, R., Peres, A. & Wootters, W. K. (1993).** "Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels." *Physical Review Letters* 70, 1895. [The original teleportation paper. Cite for protocol authorship and historical context.]
- **Bennett, C. H. & Wiesner, S. J. (1992).** "Communication via one- and two-particle operators on Einstein-Podolsky-Rosen states." *Physical Review Letters* 69, 2881. [The original superdense coding paper. Cite for protocol authorship.]
- **Wootters, W. K. & Zurek, W. H. (1982).** "A single quantum cannot be cloned." *Nature* 299, 802–803. [Original no-cloning theorem paper. Cite for theorem attribution.] — also available at https://www.nature.com/articles/299802a0
- **PennyLane Demos — Quantum Teleportation (2023, updated 2025).** Matthew Silverman. https://pennylane.ai/qml/demos/tutorial_teleportation — **Strongest single online pedagogical source for this chapter.** Contains: no-cloning proof (inner product argument), full four-step protocol with algebra worked through, PennyLane code with mid-circuit measurements and deferred measurement principle, verification via density matrix comparison. [Verified 2026-06-03]
- **QuantumZeitgeist — "No-Communication Theorem: The Definitive 2026 Guide."** https://quantumzeitgeist.com/can-you-send-a-message-using-entanglement-the-answer-is-subtle/ — accessible explanation of why entanglement cannot signal, and why teleportation requires classical communication. Good supplementary reading for students confused about FTL.
- **Superdense coding — Wikipedia.** https://en.wikipedia.org/wiki/Superdense_coding — reliable summary of the protocol with encoding table.
- **Quantum teleportation — Wikipedia.** https://en.wikipedia.org/wiki/Quantum_teleportation — broader context including experimental realizations timeline.
- **David Meyer — "A Few Notes on Bell States, Superdense Coding, and Quantum Teleportation."** https://davidmeyer.github.io/qc/bell.pdf — concise note covering all three topics with algebra; good model for chapter structure.
- **Grokipedia — Superdense Coding.** https://grokipedia.com/page/Superdense_coding — clean summary of encoding/decoding table.
