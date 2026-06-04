# Research Notes: Chapter 03 — Bell's Theorem and CHSH
**Corresponding chapter:** chapters/03-bells-theorem-and-chsh.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)
Students can derive the CHSH inequality |S| ≤ 2 from local realism alone, compute S for the singlet/Bell state at the optimal angles and obtain the Tsirelson bound 2√2, name the experimental loopholes (detection, locality) and how the 2015 experiments closed them, and interpret the 2022 Nobel Prize in the context of the experimental program from Clauser (1972) through Aspect (1982) to Hensen/Giustina/Shalm (2015).

---

## A. Conceptual foundations

### A1. Local realism and the CHSH inequality
**Setup:** Alice and Bob each hold one particle from an entangled pair. Alice chooses measurement setting A₁ or A₂; Bob chooses B₁ or B₂. Each measurement returns ±1. Define E(Aᵢ, Bⱼ) = ⟨AᵢBⱼ⟩. Local realism = locality (Alice's outcome depends only on her setting and a shared hidden variable λ, not on Bob's choice) + realism (each particle carried a definite value Aᵢ(λ), Bⱼ(λ) ∈ {±1} for every possible measurement, predetermined at the moment of separation).

**Derivation:** S(λ) = A₁(λ)[B₁(λ) + B₂(λ)] + A₂(λ)[B₁(λ) − B₂(λ)]. Since B₁, B₂ ∈ {±1}, exactly one of (B₁+B₂) and (B₁−B₂) is ±2 and the other is 0. Therefore |S(λ)| = 2|Aᵢ(λ)| × 2 × (1/2) = 2 at every value of λ. Averaging: |S| = |∫ S(λ)ρ(λ)dλ| ≤ ∫|S(λ)|ρ(λ)dλ = 2. This is the CHSH bound. Assumption-free: no choice of hidden variable distribution, no form restriction on Aᵢ(λ), Bⱼ(λ) can violate it under local realism.

**Common misconception:** "The CHSH inequality only applies to spin-1/2 particles." It applies to any system where the measurement outcomes are dichotomous (±1). Optical polarization experiments (photons, vertical/horizontal) are directly covered. The derivation uses only that Aᵢ, Bⱼ ∈ {±1}.

**Worked example:** Suppose a local hidden variable model assigns A₁(λ) = +1, A₂(λ) = +1, B₁(λ) = +1, B₂(λ) = −1. Then S(λ) = (+1)(+1+−1) + (+1)(+1−−1) = 0 + 2 = 2. Check |S(λ)| = 2 ✓. Any other assignment of ±1 values gives |S(λ)| = 2.

**Source(s):** _lib_qmsri-12-entanglement §"Bell's theorem and the CHSH inequality" (full derivation present, verbatim quotable); Clauser, Horne, Shimony & Holt (1969), *Phys. Rev. Lett.* 23, 880.

---

### A2. Quantum violation: the Tsirelson bound
**Setup:** State |Φ+⟩ = (|00⟩+|11⟩)/√2. Measurement operators: Aᵢ = â_i·σ⃗ (Alice), Bⱼ = b̂_j·σ⃗ (Bob), where â_i, b̂_j are unit vectors.

**Correlation formula:** E(â, b̂) = ⟨Φ+|(â·σ⃗)⊗(b̂·σ⃗)|Φ+⟩ = cos(θ_a − θ_b), where θ_a, θ_b are the angles in the xz-plane. (For the singlet |Ψ−⟩, E = −â·b̂.)

**Optimal angles and computation:** Choose θ_{A₁} = 0°, θ_{A₂} = 90°, θ_{B₁} = 45°, θ_{B₂} = −45°:
- E(A₁, B₁) = cos(0°−45°) = cos(−45°) = +1/√2
- E(A₁, B₂) = cos(0°−(−45°)) = cos(45°) = +1/√2
- E(A₂, B₁) = cos(90°−45°) = cos(45°) = +1/√2
- E(A₂, B₂) = cos(90°−(−45°)) = cos(135°) = −1/√2

S = 1/√2 + 1/√2 + 1/√2 − (−1/√2) = 4/√2 = **2√2 ≈ 2.828**.

This exceeds the classical bound of 2 by √2. Boris Tsirelson proved in 1980 that 2√2 is the maximum achievable by any quantum state with any observables — no quantum system can push |S| above 2√2. The bound |S| ≤ 2√2 follows from the operator identity S² ≤ 4I (operator norm argument).

**Common misconception:** "The quantum maximum should be 4, since each E ≤ 1." The algebraic maximum (no constraints) is 4. The Tsirelson bound at 2√2 < 4 is a structural constraint of quantum mechanics. Hypothetical "PR-box" (Popescu–Rohrlich) correlations would reach S = 4 while still satisfying no-signaling, but nature does not allow them. The physical principle behind the Tsirelson bound is contested — information causality (Pawlowski et al. 2009) is one candidate axiom.

**Source(s):** _lib_qmsri-12-entanglement §"Bell's theorem and the CHSH inequality" (computation given verbatim, S = 4/√2 = 2√2); _lib_qmsri-12 §"Still puzzling" (Tsirelson bound and PR boxes); Tsirelson, B. S. (1980). *Lett. Math. Phys.* 4, 93; Pawlowski et al. (2009), *Nature* 461, 1101.

---

### A3. The experimental loopholes
Two main loopholes allow a local hidden variable explanation to survive even when the CHSH bound appears violated:

**Detection loophole (fair-sampling loophole):** If only a fraction of particle pairs are detected, the detected subset might be biased — a local model could reproduce apparent violations by ensuring that only "favorable" pairs are registered. Closing this loophole requires high-efficiency detectors so that the detected sample is a fair representation of all pairs produced. In photon experiments, detector efficiencies below ~82% leave the loophole open. Pre-2015 photon experiments (including Aspect 1982) did not close this loophole.

**Locality loophole (communication loophole):** If Alice's measurement outcome can influence Bob's detector setting (or vice versa) within the time the particles are in flight, a local hidden variable with a signaling channel could fake the correlations. Closing this loophole requires that: (a) the two measurement events are spacelike separated, and (b) the measurement settings are chosen randomly and independently after the pair is emitted (so the settings cannot be "known" by the particles at separation). Aspect et al. (1982) were the first to switch settings rapidly enough to close this loophole for photon pairs, but with imperfect detector efficiency.

**Memory loophole:** In repeated experiments, if the hidden variable "remembers" previous runs, it could exploit temporal correlations. Addressed by randomizing the experimental sequence and using a finite-data Bell test (Gill 2003 framework).

**Common misconception:** "Closing the locality loophole is sufficient to rule out all local hidden variable theories." Not without also closing the detection loophole. A determined local realist can exploit either loophole individually to construct a model consistent with the observed data.

**Source(s):** _lib_qmsri-12-entanglement §"What the experiments showed"; Larsson (2014), *J. Phys. A* 47, 424003 (review of loopholes).

---

### A4. The 2015 loophole-free Bell tests
Three independent experiments in 2015 simultaneously closed both the locality and detection loopholes:

**Hensen et al. (Delft/QuTech, 2015):** Used electron spins in nitrogen-vacancy (NV) centers in diamond, entangled via photons, placed 1.3 km apart at opposite ends of the TU Delft campus. The spatial separation (1.3 km) ensured spacelike separation of measurement events, closing the locality loophole. NV-center spin detection efficiency is high enough to close the detection loophole. Measured S = 2.42 (reported in source as "above 2 by more than two standard deviations" — the S value of 2.42 is confirmed by the follow-up second-experiment paper which reports combined S = 2.38 ± 0.14). Published: *Nature* 526, 682–686 (2015). https://www.nature.com/articles/nature15759

**Giustina et al. (Vienna/IQOQI, 2015):** Used entangled photon pairs with high-efficiency superconducting nanowire single-photon detectors (SNSPDs). Violated the Bell–CHSH bound by 11.5 standard deviations (p-value not numerically given in local sources; the paper reports the violation was "significant-loophole-free"). Published: *Phys. Rev. Lett.* 115, 250401 (2015). https://link.aps.org/doi/10.1103/PhysRevLett.115.250401

**Shalm et al. (NIST, 2015):** Used entangled photon pairs with SNSPD detectors and independent quantum-random-number generators to choose measurement settings. Achieved p-values as small as 5.9 × 10⁻⁹ for the Bell violation. Published: *Phys. Rev. Lett.* 115, 250402 (2015). https://www.nist.gov/publications/strong-loophole-free-test-local-realism

**Significance:** Three different physical implementations (NV-center electron spins, photons with different detector technologies), three different loophole-closing strategies, consistent result: local realism is ruled out. The case is closed experimentally.

**Common misconception:** "The 2015 experiments proved that quantum mechanics is correct." More precisely: they proved that no local realistic theory can reproduce the observed correlations. Quantum mechanics predicted the violation, but non-local hidden variable theories (e.g., Bohmian mechanics) and many-worlds interpretations are also consistent with the results.

**Source(s):** _lib_qmsri-12-entanglement §"What the experiments showed"; Hensen et al. (2015), *Nature* 526, 682 https://www.nature.com/articles/nature15759; Giustina et al. (2015), *PRL* 115, 250401 https://link.aps.org/doi/10.1103/PhysRevLett.115.250401; Shalm et al. (2015), *PRL* 115, 250402 https://www.nist.gov/publications/strong-loophole-free-test-local-realism; Physics Today news summary https://physicstoday.aip.org/news/three-groups-close-the-loopholes-in-tests-of-bells-theorem.

---

### A5. The 2022 Nobel Prize
**October 2022:** The Nobel Prize in Physics was awarded to Alain Aspect (Institut d'Optique, France), John Clauser (J.F. Clauser & Associates, USA), and Anton Zeilinger (University of Vienna, Austria) "for experiments with entangled photons, establishing the violation of Bell's inequalities and pioneering quantum information science."

**Individual contributions:**
- **John Clauser (1972):** Conducted the first experimental test of Bell's inequality with Stuart Freedman (the Freedman–Clauser experiment). Found a violation consistent with quantum mechanics, supporting it against local hidden variable theories in the first systematic test.
- **Alain Aspect (1982):** With Dalibard and Roger, performed improved experiments at Orsay that closed the locality loophole by rapidly switching measurement settings (using acousto-optic modulators) after pairs were emitted, ensuring settings were chosen after the photons were in flight.
- **Anton Zeilinger (1998):** At Innsbruck, performed Bell tests using independent quantum random-number generators to choose measurement settings, further closing the locality loophole. Also demonstrated quantum teleportation (1997) and other foundational quantum information experiments.

**Historical arc:** The prize recognized a 60-year experimental program: EPR (1935, theoretical challenge) → Bell (1964, theorem with testable consequence) → Clauser–Freedman (1972, first experiment) → Aspect (1982, locality loophole addressed) → multiple groups (2015, all loopholes closed) → Nobel recognition (2022).

**Source(s):** _lib_qmsri-12-entanglement §"What the experiments showed" (last paragraph on Nobel); Nobel Committee press release: https://www.nobelprize.org/prizes/physics/2022/press-release/; Popular background: https://www.nobelprize.org/prizes/physics/2022/popular-information/; Aspect's first-hand account: https://arxiv.org/pdf/2212.04737.

---

## B. Domain examples and cases

**Bell test as hardware diagnostic:** Running a CHSH test on a quantum processor and measuring S is a direct diagnostic of entanglement quality. S = 2√2 ≈ 2.828 means perfect entanglement; as decoherence degrades the Bell pair toward a classical mixture, S decreases toward 2 (and below). The boundary S = 2 is the boundary between useful quantum correlations and those reproducible classically. Source: _lib_qmsri-12-entanglement §"Decoherence and the cost of entanglement" and fig 12.6.

**No-signaling from the quantum correlations:** Even though the quantum correlations violate local realism, they cannot be used for faster-than-light signaling. Alice's choice of measurement setting does not change Bob's marginal statistics (his reduced density matrix is I/2 regardless of what Alice does). The correlations are only visible when Alice and Bob compare notes via a classical channel. Source: _lib_qmsri-12 §"What Bell's theorem does and does not say."

**Interpretational consequences:** Bell's theorem forces a choice among interpretations. Bohmian mechanics retains determinism but adds non-local influences. Many-worlds retains locality but allows multiple outcomes. Standard Copenhagen drops realism at the fundamental level. None of these add testable predictions beyond QM.

---

## C. Connections and dependencies

- **Prerequisite:** Ch. 01 (density matrix, partial trace — the no-signaling argument uses ρ_B = I/2); Ch. 02 (Bell states, tensor products — the calculation of S requires constructing the four-operator expectation values in the Bell-state basis).
- **Feeds forward:** Ch. 04 and beyond (decoherence degrades S; quantum error correction aims to preserve S > 2 in hardware); quantum cryptography (BB84, E91 protocols use Bell violations as security proofs).
- **Key algebra needed:** Pauli algebra: (â·σ⃗)(b̂·σ⃗) = (â·b̂)I + i(â×b̂)·σ⃗; and the fact that ⟨Φ+|(σ_i⊗σ_j)|Φ+⟩ = δ_{ij} (only matching Pauli indices correlate in |Φ+⟩). From this, E(â,b̂) = Σ_{ij} aᵢ bⱼ δ_{ij} = â·b̂ = cos(θ_a−θ_b).

---

## D. Current state of the field

**Settled:** The CHSH inequality, its algebraic derivation from local realism, the quantum prediction S = 2√2, and the experimental status. Local realism is ruled out by three independent loophole-free experiments. The 2022 Nobel confirms the scientific consensus. These are not contested.

**Contested:** The interpretation — what Bell's theorem tells us about reality. Local realism is ruled out, but which of {locality, realism} to abandon is a philosophical (not empirical) question. The measurement problem is separate and remains open (see _lib_qmsri-13-capstone §"Three open problems").

**Contested/Active:** Why the Tsirelson bound is 2√2 and not 4 (the algebraic maximum, achievable by PR boxes). Information causality (Pawlowski et al. 2009) is the leading candidate principle but remains an axiom, not a derivation from more primitive physics. Source: _lib_qmsri-12 §"Still puzzling."

**Recent developments (as of 2026):**
- The three loophole-free 2015 experiments are now textbook. Follow-up work includes Bell tests with satellite-based entanglement distribution (Yin et al. 2017, *Science* 356, 1140 — entangled photons over 1200 km) and with cosmic photons setting the measurement angles (BIG Bell Test, Handsteiner et al. 2017).
- Device-independent quantum cryptography (DIQKD) — cryptographic security derived from Bell violation alone, without trusting the devices — was experimentally demonstrated in 2022 by three groups (Nadlinger et al., *Nature* 607, 682; Zhang et al.; Liu et al.).
- Bell-test technology feeds directly into quantum network development. The Delft group's NV-center platform (Hensen 2015) is now a prototype quantum network node.

**Key references:**
- Bell, J. S. (1964). On the Einstein–Podolsky–Rosen paradox. *Physics* 1, 195.
- Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Phys. Rev. Lett.* 23, 880.
- Freedman, S. J. & Clauser, J. F. (1972). *Phys. Rev. Lett.* 28, 938.
- Aspect, A., Dalibard, J., & Roger, G. (1982). *Phys. Rev. Lett.* 49, 1804.
- Tsirelson, B. S. (1980). *Lett. Math. Phys.* 4, 93.
- Hensen et al. (2015). *Nature* 526, 682. https://www.nature.com/articles/nature15759
- Giustina et al. (2015). *Phys. Rev. Lett.* 115, 250401. https://link.aps.org/doi/10.1103/PhysRevLett.115.250401
- Shalm et al. (2015). *Phys. Rev. Lett.* 115, 250402. https://www.nist.gov/publications/strong-loophole-free-test-local-realism
- Nobel Prize 2022: https://www.nobelprize.org/prizes/physics/2022/summary/
- Pawlowski et al. (2009). *Nature* 461, 1101. (Information causality and the Tsirelson bound.)
- Nadlinger et al. (2022). *Nature* 607, 682. (Device-independent QKD.)

---

## E. Teaching considerations

- **Hook:** The CHSH inequality is an algebraic fact about ±1 numbers. Its derivation uses no quantum mechanics. The quantum violation therefore cannot be "explained away" by any pre-existing-values model — the clash is between algebra and experiment. Lead with this shock.
- **Order of presentation:** (1) Local realism defined; (2) CHSH derivation (pure algebra); (3) quantum prediction — compute S for |Φ+⟩ at optimal angles; (4) experimental history (Clauser → Aspect → 2015); (5) Nobel; (6) what Bell's theorem does/does not say (no FTL, no resolution of measurement problem).
- **The angle calculation:** The four angles θ = 0°, 90°, 45°, −45° are typically presented as the "optimal" setting. Students should derive them by maximizing S over angles, not just accept them as given. The optimization gives a system of equations equivalent to equal angular spacing.
- **Simulation hook:** The CHSH Bell inequality simulator (Tab 1 of _lib_qmsri-12 LLM exercise, 12-bell-inequality.html) lets students sweep angles and watch S cross the classical bound. Background turns amber when |S| > 2. This is the ideal simulation for Ch. 03.
- **Common classroom error:** Students confuse the CHSH parameter S with the correlation E(â,b̂). S is a sum of four correlation values; E is a single correlation for one pair of settings. Distinguish clearly.
- **No-signaling must be explicitly proved.** Students who first encounter Bell's theorem often conclude "but then Alice and Bob can communicate FTL." The partial trace argument (ρ_B = I/2 regardless of Alice's action) should be part of Ch. 03 or cross-referenced from Ch. 01.

---

## F. Library files relevant to this chapter

- **_lib_qmsri-12-entanglement-and-quantum-information.md** — Primary source. Contains: full CHSH derivation (§"Bell's theorem and the CHSH inequality," algebra-complete); optimal angles and S = 2√2 computation (verbatim, including all four E values); correlation formula E(â,b̂) = cos(θ_a−θ_b) for |Φ+⟩; experimental summary Clauser → Aspect → 2015 (§"What the experiments showed"); Nobel Prize citation October 2022 (§"What the experiments showed," last paragraph); no-signaling argument and what Bell's theorem does/does not say (§"What Bell's theorem does and does not say"); Tsirelson bound and PR boxes (§"Still puzzling"); Bell test as hardware diagnostic (§"Decoherence and the cost of entanglement"); CHSH simulation specification (§LLM Exercise). This file is the primary draft for Ch. 03.
- **_lib_qmsri-13-capstone-quantum-mechanics-in-research.md** — Secondary. Contains the density matrix and partial trace (needed for the no-signaling proof), and mentions CHSH as a hardware diagnostic in the NISQ section.
- **_lib_qmsri-qm-townsend-notes.md** — No Bell/CHSH content found. Not useful for Ch. 03.

---

## G. Gaps and flags

- **Experimental S values: partial.** Hensen et al. (2015) S value: confirmed S = 2.42 from local source (_lib_qmsri-12 states "above 2 by more than two standard deviations"); the follow-up second experiment (Hensen et al. 2016, *Scientific Reports*) gives combined S = 2.38 ± 0.14. Giustina et al. 2015: violation by 11.5 standard deviations reported in local source; specific S value not given in local sources (the paper uses a modified test statistic — the paper tests a variant inequality, not CHSH directly). Shalm et al. 2015: p-value ≤ 5.9 × 10⁻⁹ from web search; specific S value not confirmed in local sources. Chapter author should cite exact values from the papers directly.
- **Malformed table in local source:** _lib_qmsri-12 §"What the experiments showed" contains a broken table with placeholder text. The chapter author must replace this with a properly formatted table citing the three 2015 experiments.
- **Tsirelson bound proof:** Not derived in local sources; only stated. The operator-algebraic proof (S² ≤ 4I for anticommuting observables) should be added to Ch. 03 or relegated to an appendix.
- **Device-independent QKD (2022 experiments):** Not mentioned in local sources. Chapter should briefly note that Bell violations are now the security proof for a new generation of cryptographic protocols (Nadlinger et al. 2022, *Nature* 607, 682).
- **Flag — Nobel Prize year confirmed:** The 2022 Nobel Prize to Aspect, Clauser, Zeilinger is confirmed by both local source (_lib_qmsri-12 §"What the experiments showed": "In October 2022 the Nobel Committee gave the physics prize...") and web search (Nobel Committee press release). The citation is "for their experiments with entangled photons, establishing the violation of Bell's inequalities and pioneering quantum information science."
- **Flag — current experimental status as of 2026:** The loophole-free Bell test result is settled science. The most current frontier is device-independent quantum cryptography and Bell tests over satellite links. The chapter should reflect this as the "where the field went next" note.
