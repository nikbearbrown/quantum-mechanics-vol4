# Research Notes: Chapter 10 — Capstone: Quantum Mechanics in Research

**Corresponding chapter:** chapters/10-capstone-quantum-mechanics-in-research.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

The student can read the first two pages of a current quantum mechanics research paper — a Bell test, a quantum error correction milestone, a quantum-advantage claim, or an NV-center sensing result — identify the problem, the formalism being deployed, and the core experimental claim. They can reconstruct the paper's central mathematical result using the tools built across the series. They understand which claims in the quantum computing literature are robustly established and which are contested or context-dependent. This is the volume's capstone and the series' culminating exercise in research literacy.

---

## A. Conceptual foundations

### What "reconstruct the core result" means

This is not a literature review or a summary. It means: starting from the series' formalism, re-derive or re-calculate the paper's central quantitative claim from the given physical setup. For a Bell test: given the experimental setup and measurement settings, calculate the CHSH value S and compare to the quantum maximum (S = 2√2) and the local-hidden-variable bound (S ≤ 2). For a QEC paper: given the code distance and physical error rate, calculate the expected logical error rate using the threshold scaling formula and compare to what the experiment reports. For an NV sensing paper: given the zero-field splitting, applied B field, and g factor, calculate the ODMR transition frequencies and compare to the spectral data.

"Reconstruct" means the student is not a passive reader. They are checking the paper's arithmetic and logic against their own calculation from first principles.

### The honesty layer: contested claims in quantum computing

Several landmark results in this field have been genuinely contested. Students should read quantum advantage claims with calibrated skepticism:

**Google Sycamore (2019):** Claimed ~200-second task would take ~10,000 years on classical hardware. IBM immediately disputed, arguing a better classical simulation strategy would need ~2.5 days (not 10,000 years). Pan Zhang et al. (Chinese Academy of Sciences, 2022) subsequently showed a classical GPU cluster could simulate the same task in ~15 hours. Scott Aaronson's analysis: the classical simulation gap is real but narrowing; "there's an urgent need for better quantum supremacy experiments." The task (random circuit sampling) was designed to be hard to simulate classically, not to be useful.

**USTC Jiuzhang (2020, 2021):** Gaussian boson sampling advantage claims. Similarly contested on grounds that better classical algorithms may match performance.

**Google Willow / below-threshold QEC (2024):** This result is on much firmer ground — it is not a computational-advantage claim but a physical demonstration of a mathematical theorem (the threshold theorem). The fact that logical error rates decrease with code distance below threshold is not a claim classical computers can undercut.

**The structural distinction:** Sampling-based quantum advantage claims (Sycamore, Jiuzhang) are inherently fragile because classical simulators continue to improve. Hardware demonstrations of physical principles (threshold theorem, Bell inequality violations) are not subject to the same classical-simulation arms race — they are demonstrations of quantum physics, not classical computational complexity.

### How to read a quantum paper: a framework

The student needs a triage method for the first two pages of a paper:

1. **Identify the problem class.** Bell test / QEC / quantum sensing / quantum simulation / quantum advantage? Each has a characteristic formalism.
2. **Find the central claim.** Usually in the last paragraph of the introduction or the abstract's final sentence. Often a specific number: S = 2.38, p_L = 0.143%, T₂ = 2.4 ms.
3. **Identify the system Hamiltonian.** What are the qubits? What encodes |0⟩ and |1⟩? What drives the gates?
4. **Identify the observable.** What is being measured, and in what basis?
5. **Check against theory.** The quantum theory prediction should appear in the paper. Locate it and verify you can derive it from the series' tools.
6. **Assess the error bars and statistical claims.** A CHSH violation with p = 0.039 (Hensen et al. 2015) is qualitatively different from a below-threshold QEC demonstration that is replicated across many runs. Note the statistical strength.
7. **Read the "honesty disclaimer."** A good paper states what it cannot demonstrate. Look for what the authors explicitly do not claim.

---

## B. Domain examples and cases: four candidate papers

### Candidate Paper 1: Loophole-free Bell test (Hensen et al. 2015)

**Full citation:** Hensen, B. et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 km." Nature 526, 682–686 (2015). Also: arXiv:1508.05949.

**System:** Two NV-center electron spins in diamond, at TU Delft, separated by 1.3 km via optical fiber.

**The claim:** CHSH inequality S ≤ 2 violated at S = 2.42 ± 0.20 (first experiment, 245 trials); S = 2.35 ± 0.18 (second experiment); combined S = 2.38 ± 0.14. Statistical significance: p = 0.039 (one-tailed; n = 245).

**Volume tools needed:**
- Vol. 1: Two-level systems, spin-1/2, Pauli operators
- Vol. 2: Entanglement and Bell states (|Φ+⟩ = (|00⟩ + |11⟩)/√2)
- Vol. 2: CHSH inequality derivation (local-hidden-variable bound S ≤ 2; quantum maximum 2√2)
- Vol. 2: Measurement in rotated bases

**Reconstruction target:** Given the measurement settings (angles a, a', b, b' of Alice's and Bob's spin measurement axes), calculate E(a,b) = ⟨σ_a ⊗ σ_b⟩ for the Bell state and hence S = E(a,b) − E(a,b') + E(a',b) + E(a',b').

**Honesty layer:** The Hensen et al. result is statistically marginal (p = 0.039 from 245 trials). The same team ran a follow-up that confirmed S = 2.35 ± 0.18. More decisive experiments followed in 2015 (Giustina et al., Shalm et al.) with p values of 10⁻⁹ and 10⁻⁷. The "loophole-free" qualifier refers to closing both the locality loophole (1.3 km separation, random basis choice within light-travel time) and the detection loophole (high-efficiency NV-center spin readout avoids the fair-sampling assumption).

**Teaching value:** Uses NV-center physics (Ch 8), entanglement (Vol. 2), and the formal Bell/CHSH derivation. The experimental setup is physically concrete.

---

### Candidate Paper 2: Google Willow below-threshold QEC (2024)

**Full citation:** Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." Nature (2025; accepted/published from arXiv:2408.13687, announced December 2024).

**System:** 105-qubit Willow superconducting processor; surface code quantum memories at distance 3, 5, 7.

**The claim:** Logical error rate suppressed by factor Λ = 2.14 ± 0.02 per unit increase in code distance by 2. Distance-7 code: p_L = 0.143% ± 0.003% per error-correction cycle. The distance-7 logical memory beats the best physical qubit lifetime by a factor of 2.4 ± 0.3 (beyond break-even). This is the first below-threshold surface code demonstration.

**Volume tools needed:**
- Ch 8 (this volume): superconducting transmon qubits; T₁ and T₂
- Ch 9 (this volume): surface code, code distance, threshold theorem, p_L scaling formula
- Vol. 1: stabilizer formalism (at introductory level)
- Ch 13 (library file): density matrix, decoherence channels

**Reconstruction target:** Use the threshold scaling formula p_L ≈ A(p/p_th)^⌈(d+1)/2⌉ with p_th ≈ 0.01 and p ≈ 0.001 (estimated physical error rate on Willow). Calculate the expected p_L for d = 3, 5, 7 and compare to the paper's reported values. Verify that Λ ≈ (p/p_th) ≈ 2 is consistent with the reported suppression factor.

**Honesty layer:** This result is on firm ground — it is demonstrating a mathematical theorem experimentally, not making a computational-complexity claim. However: the physical error rate on Willow is estimated, not independently measured with full precision. The result demonstrates below-threshold quantum memory (passive error correction cycles), not yet below-threshold universal fault-tolerant computation (which requires transversal logical gates and magic state distillation).

**Teaching value:** Direct connection to Ch 9 threshold theorem material. The paper's Methods section describes syndrome extraction circuits that are applications of the stabilizer formalism.

---

### Candidate Paper 3: NV-center magnetometry (Balasubramanian et al. or Maze et al. 2008; or more recent)

**Canonical reference:** Balasubramanian, G. et al. "Nanoscale imaging magnetometry with diamond spins under ambient conditions." Nature 455, 648–651 (2008); and/or Maze, J.R. et al. "Nanoscale magnetic sensing with an individual electronic spin in diamond." Nature 455, 644–647 (2008). For a more recent demonstration: Chatzidrosos, G. et al. (2021) or Andrich, P. et al. 2017 for NV array sensing.

For current context: see also single-NV T₂ records using dynamical decoupling and recent biological NV magnetometry papers (2023–2025).

**System:** Single NV center in diamond; ODMR spectroscopy.

**The claim:** Magnetic field sensitivity at or below nT/√Hz (nanoscale, room temperature).

**Volume tools needed:**
- Vol. 3 / Ch 9 (perturbation theory): Zeeman splitting of NV m_s levels in applied B field
- Ch 8 (this volume): NV Hamiltonian H_NV = D Ŝ_z² + gμ_B BŜ_z; eigenvalues; ODMR transition frequencies
- Ch 13 (library): T₂ and linewidth connection (sensitivity ∝ 1/(γ T₂√N))
- Vol. 1: Rabi oscillations (the microwave drive that drives spin transitions)

**Reconstruction target:** Given B = 30 mT along NV axis, calculate the two ODMR frequencies f± = D ± 28B MHz/mT = 2.87 GHz ± 840 MHz. Calculate the predicted splitting Δf = 1.68 GHz and compare to a published spectrum. Calculate the field sensitivity η = (ℏ)/(gμ_B T₂ √N) in appropriate units.

**Honesty layer:** NV magnetometry claims are generally robust and reproducible. The contested region is not the physics but the engineering: room-temperature chip-scale NV arrays (Quantum Brilliance) remain in early development. The nT/√Hz sensitivity numbers in published papers are often achieved under highly controlled conditions (low temperature, long averaging, isotopically purified diamond). Real-world field performance differs.

**Teaching value:** Most conceptually continuous with the series — every calculation uses tools from prior chapters. Excellent for the worked-example role because the student can do the entire reconstruction from a 3-line Hamiltonian.

---

### Candidate Paper 4: Neutral-atom logical qubit demonstration (Bluvstein et al. 2024)

**Full citation:** Bluvstein, D. et al. (QuEra/Harvard/MIT). "Logical quantum processor based on reconfigurable atom arrays." Nature 626, 58–65 (2024).

**System:** 280-atom neutral Rb/Cs array in optical tweezers; 48 logical qubits encoded in [[8,3,2]] color codes and [[4,2,2]] codes; transversal fault-tolerant gates.

**The claim:** 48 logical qubits operating with transversal fault-tolerant gates; logical error rates below physical error rates demonstrated for specific operations.

**Volume tools needed:**
- Ch 8 (this volume): neutral atom qubits, Rydberg blockade, optical tweezers
- Ch 9 (this volume): stabilizer codes, fault-tolerant gates (transversal operations)
- Vol. 2: entanglement structure of logical qubit states

**Reconstruction target:** For the [[4,2,2]] code (the simplest detectable code), write out the four logical basis states and verify they satisfy the stabilizer conditions. Show that a transversal CNOT gate (CNOTs applied bitwise between two code blocks) implements a logical CNOT.

**Honesty layer:** The Bluvstein 2024 result is a logical qubit count record and a genuine demonstration of fault-tolerant operations on neutral atoms. The logical error rates achieved are not yet competitive with the best physical-qubit gate fidelities at this scale. The "48 logical qubits" headline is technically correct but the operations are relatively shallow (not arbitrary depth below threshold). The 2026 result (96 logical qubits) represents further progress.

**Teaching value:** Illustrates a different code family (color codes vs. surface codes), a different platform (neutral atoms), and the key concept of transversal gates as a natural fault-tolerance mechanism.

---

## C. The rubric for "reconstruct the core result"

A student's reconstruction should demonstrate:

1. **System identification (20%):** Correctly identify the physical qubit(s), the Hamiltonian, |0⟩ and |1⟩, and the gate mechanism.

2. **Observable and measurement (20%):** State which observable is measured, in what basis, and what the quantum theory predicts for the measurement outcome given the state.

3. **Core calculation (30%):** Reproduce the central quantitative result (CHSH value, ODMR frequency, logical error rate, code distance scaling) from first principles using the series' formalism. Numbers must match the paper to within stated error bars.

4. **Connections to prior chapters (15%):** Explicitly identify which volume and chapter the key tools come from. E.g., "the CHSH bound of 2 from Vol. 2 Chapter 4; the NV Hamiltonian from this volume Ch 8; T₂ from Ch 13."

5. **Honest assessment of what the paper does and does not demonstrate (15%):** State one thing the paper explicitly does not claim. Identify whether the result is a demonstration of a physical principle, a hardware benchmark, or a computational-advantage claim, and what the implications of that distinction are.

---

## D. Connections and dependencies

- **All of Vol. 1:** Every candidate paper uses the two-level formalism (Pauli operators, Bloch sphere, time evolution).
- **Vol. 2 (entanglement):** Bell test paper requires Bell states, CHSH derivation, measurement in rotated bases.
- **Vol. 3 (perturbation theory):** NV sensing paper uses first-order Zeeman perturbation; this is Ch 9 of Vol. 3.
- **Ch 8 (this volume):** All four papers require knowing the physical platform. Papers 2, 3, and 4 are directly addressed in Ch 8.
- **Ch 9 (this volume):** Paper 2 (Google Willow) and Paper 4 (Bluvstein) require QEC and stabilizer formalism.
- **Ch 13 / library file:** Density matrix and decoherence framework needed for NV sensing (linewidth ↔ T₂) and QEC (error channels as Lindblad operators).

---

## E. Current state of the field (specific and current as of 2026-06)

**Bell tests:** Loophole-free Bell violations are now routine. The 2015 trifecta (Hensen, Giustina, Shalm) closed all major loopholes. Subsequent experiments have increased statistics and extended distances. The physics is settled; the contest has moved to quantum networks.

**QEC milestone timeline:**
- 2023 (Google): correct distance-scaling trend on repetition codes (Nature 614, 676)
- 2024 (Google Willow): definitively below-threshold surface code (Nature 638, 920); Λ = 2.14 per code distance increase by 2
- 2024 (Quantinuum + Microsoft): 12 logical qubits at 99.9%+ fidelity; 800× error suppression (April 2024)
- 2024 (QuEra/Harvard/MIT): 48 logical qubits, neutral atoms (Nature 626, 58)
- 2025 (Quantinuum Helios + Microsoft): 48 logical qubits, fault-tolerant non-Clifford gates
- 2026 (QuEra/Harvard/MIT): 96 logical qubits from 448 atoms (Nature, January 2026)

**Quantum advantage claims:** Status remains contested for sampling problems (Sycamore 2019, Jiuzhang 2020–2021). Classical simulation has continued to improve. The most credible quantum advantage demonstration remains an open area. No practically useful quantum advantage has been demonstrated on a real-world problem as of 2026.

**NV sensing:** Field is mature and commercially active. Sensitivities at nT/√Hz in research settings; products under development for geological and biomedical sensing. Not contested.

**NIST PQC:** August 2024: FIPS 203 (ML-KEM / CRYSTALS-Kyber), FIPS 204 (ML-DSA / CRYSTALS-Dilithium), FIPS 205 (SLH-DSA / SPHINCS+) finalized. World's cryptographic infrastructure is being updated in anticipation of fault-tolerant Shor's algorithm, which does not yet exist. This is the societal consequence of the physics in this volume.

---

## F. Teaching considerations

**The capstone structure from the library file:**
The _lib_qmsri-13 file frames the chapter as: "Five doorways, one chapter. The goal is not to master any of them — it is to read the first page of a paper in each field and understand the problem and the tools being deployed." The four candidates above are the four doorways for this capstone (plus topology from the library file, which is a fifth option).

**Paper selection guidance for instructors:**
- Bell test (Hensen 2015): Lowest technical barrier; best for courses that have not covered QEC in depth. The full reconstruction uses only Vol. 1 and 2 tools.
- Google Willow (2024): Highest topicality and connection to Ch 9. Best for courses where QEC is a central theme.
- NV sensing (Balasubramanian 2008 / recent): Best bridge from theory to measurement; uses perturbation theory explicitly. Good for students interested in atomic/optical physics.
- Bluvstein 2024: Best for students interested in neutral atom platforms; introduces color codes as an alternative to surface codes.

**The paper-selection prompt for students:**
"Pick one paper from the approved list. Write a 2–3 page technical note that: (1) identifies the system Hamiltonian; (2) reconstructs the paper's central quantitative result from the series' formalism; (3) connects each step to a specific volume and chapter; (4) states honestly what the paper does and does not demonstrate. Your calculation must agree with the paper's reported value to within the stated error bars."

**What students consistently find hard:**
1. Distinguishing what a paper demonstrates from what it implies. ("Google demonstrated below-threshold QEC" does not imply "fault-tolerant quantum computers exist.")
2. Locating the central quantitative claim. Papers often bury the key number in a figure caption or supplementary material.
3. Connecting the paper's notation to the series' notation. A standard move in quantum information: σ_x, σ_y, σ_z (series) vs. X, Y, Z (error-correction literature); density matrix ρ vs. ρ̂.

**The measurement problem as a closing honesty move (from library file):**
"The textbook gives you tools that work; it does not give you a resolved metaphysics." Decoherence explains why off-diagonal coherences vanish; it does not explain why one outcome obtains in one run. Different interpretations (Copenhagen, many-worlds, Bohmian, GRW, QBism) handle this differently. Schlosshauer 2007 is the reference.

---

## G. Worked example outline: reconstructing the CHSH value from a loophole-free Bell test

**Experimental setup (Hensen et al. 2015, schematically):**
- Alice holds NV center A (Delft, building A); Bob holds NV center B (Delft, building B), 1.3 km apart
- Each NV spin initialized to m_s = 0 by optical pumping
- Entanglement created by each spin emitting an entangled photon; photons interfere at a central beamsplitter; detection heralds entanglement of the two NV spins in the state |Φ⁻⟩ = (|01⟩ − |10⟩)/√2 (or |Ψ⁺⟩ — see paper for exact state)
- Alice measures her spin in one of two bases (angles a or a'); Bob in one of two bases (angles b or b')
- Angles: a = 0°, a' = 90°, b = −45°, b' = 45° (optimal for CHSH violation)

**Step 1:** Write down the singlet state |Ψ⁻⟩ = (|01⟩ − |10⟩)/√2. Compute the correlation function:
E(a, b) = ⟨Ψ⁻|σ_a ⊗ σ_b|Ψ⁻⟩ = −cos(a − b)

where σ_a = cos(a)σ_z + sin(a)σ_x is the spin measurement operator at angle a in the xz plane.

**Step 2:** Compute the four correlators for the optimal angles:
E(0°, −45°) = −cos(45°) = −1/√2
E(0°, 45°) = −cos(−45°) = −1/√2
E(90°, −45°) = −cos(135°) = +1/√2
E(90°, 45°) = −cos(45°) = −1/√2

**Step 3:** Compute CHSH parameter:
S = |E(a,b) − E(a,b') + E(a',b) + E(a',b')|
= |−1/√2 − (−1/√2) + 1/√2 + (−1/√2)|... [work through carefully]

For the standard optimal settings, S = 2√2 ≈ 2.828 (quantum maximum).

**Step 4:** Compare to the experimental result: S = 2.42 ± 0.20 (Hensen et al. 2015). Below the quantum maximum (expected for a slightly mixed state due to decoherence and detection inefficiency), but above the local-hidden-variable bound S ≤ 2 by more than 2 standard deviations.

**Step 5 (Honesty):** Note that 245 trials with p = 0.039 is statistically meaningful but not decisive. The follow-up experiments (Giustina 2015, Shalm 2015) produced p values of 10⁻⁷ to 10⁻⁹. The loophole-free nature of the experiment (locality loophole closed by 1.3 km separation + fast random basis choice; detection loophole closed by high-efficiency NV readout) is the key claim, not just the CHSH value.

---

## H. Library files relevant to this chapter

- `/pantry/_lib_qmsri-13-capstone-quantum-mechanics-in-research.md`: This is the rich draft directly feeding this chapter. Sections relevant:
  - "The NISQ era and the threshold theorem" — frames Papers 2 and 4
  - "NV centers: Chapter 9 perturbation theory made real" — frames Paper 3
  - "Three open problems and one honesty move" — frames the honesty layer throughout
  - "Still puzzling" / measurement problem — the closing honesty move
  - LLM exercises (Tabs 1–3) — the simulation deliverables associated with the capstone
  - Exercises 13.1–13.10 — directly usable in this chapter's exercise set

---

## I. Gaps and flags

1. **Paper 1 (Bell test) statistical strength.** The Hensen 2015 result with p = 0.039 from 245 trials may be too marginal for some pedagogical uses. Consider using the Giustina 2015 (Phys. Rev. Lett. 115, 250401) result or the Shalm 2015 (Phys. Rev. Lett. 115, 250402) result instead as the primary reconstruction target — both have p < 10⁻⁷ and are pedagogically cleaner while using the same formalism.

2. **Loophole-free Bell test using photons vs. spins.** The two dominant loophole-free Bell experiments use different systems: NV spins (Hensen) and photons (Giustina, Shalm). If this chapter covers the NV platform in Ch 8, using Hensen creates excellent continuity. If the instructor prefers photonic clarity, Giustina or Shalm are alternatives.

3. **Topology / Berry phase (5th doorway).** The _lib_qmsri-13 file covers topology (quantum Hall effect, Chern numbers, topological insulators, Majorana modes) as a fifth research direction. This is intellectually compelling but uses formalism (Berry phase, band theory) not fully developed in Vols. 1–3. A light treatment of the Berry phase formula with pointer to Hasan and Kane 2010 (Rev. Mod. Phys. 82, 3045) is sufficient for research literacy without requiring a full topological band theory chapter.

4. **The capstone should not be assessed only by the central calculation.** The "honesty layer" — correctly characterizing what a paper does and does not demonstrate — is equally important and harder to fake. The rubric above weights it at 15%; some instructors may want to increase this.

5. **Paper selection is time-sensitive.** By the time this volume is published, there will almost certainly be new landmark papers worth including (further logical qubit scaling, first fault-tolerant logical gate with below-threshold overhead, a genuine practical quantum advantage). The chapter should be structured so the paper list is replaceable (an instructor-facing appendix or online supplement) while the framework (rubric, reconstruction methodology, honesty layer) is durable.

6. **The Google advantage controversy needs careful framing.** Students may have read popular press accounts of Google's 2019 "quantum supremacy." The chapter should address this directly: the sampling-based advantage is real and important as a physics demonstration; it is not a computationally useful result and the classical-simulation gap has been narrowed by subsequent work. This is not a failure of the experiment — it is the correct interpretation of a proof-of-concept result.

7. **The NIST PQC angle.** A brief sidebar on FIPS 203/204/205 (August 2024) connects the abstract physics of Shor's algorithm — still only theoretically relevant to fault-tolerant machines that don't yet exist — to an immediate real-world policy consequence. This is a powerful hook for students who ask "why does this matter?"

---

*Key sources:*
- Hensen, B. et al. Nature 526, 682–686 (2015) — loophole-free Bell test, NV spins, S = 2.42 ± 0.20
- Giustina, M. et al. Phys. Rev. Lett. 115, 250401 (2015) — loophole-free Bell test, photons
- Shalm, L.K. et al. Phys. Rev. Lett. 115, 250402 (2015) — loophole-free Bell test, photons
- Aspect, A. et al. Phys. Rev. Lett. 49, 1804 (1982) — original Bell test (locality loophole open)
- Acharya et al. (Google Quantum AI) Nature 614, 676 (2023) — distance-scaling QEC demonstration
- Acharya et al. (Google Quantum AI) Nature 638, 920 (2024/2025); arXiv:2408.13687 — below-threshold Willow
- Bluvstein, D. et al. (QuEra/Harvard/MIT) Nature 626, 58–65 (2024) — 48 logical qubits
- QuEra/Harvard/MIT Nature January 2026 — 96 logical qubits, 448 atoms
- Balasubramanian, G. et al. Nature 455, 648–651 (2008) — NV magnetometry
- Maze, J.R. et al. Nature 455, 644–647 (2008) — NV sensing
- Rondin, L. et al. Rep. Prog. Phys. 77, 056503 (2014) — NV magnetometry review
- Schlosshauer 2007, Decoherence and the Quantum-to-Classical Transition, Springer
- Preskill 2018, Quantum 2, 79 — NISQ definition
- Hasan and Kane 2010, Rev. Mod. Phys. 82, 3045 — topological insulators review
- NIST FIPS 203, 204, 205 (August 2024) — post-quantum cryptography standards
- Pan Zhang et al. (Chinese Academy of Sciences) 2022 — classical simulation of Sycamore
- Aaronson, S. blog posts on quantum advantage (scottaaronson.blog, 2022)
