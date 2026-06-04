# Chapter 10 — Capstone: Quantum Mechanics in Research

## TL;DR

- This chapter is where the series' formalism stops being curriculum and becomes literacy: the ability to read the first two pages of a current quantum mechanics paper and understand what is being claimed and with what tools.
- Four candidate papers serve as doorways — a loophole-free Bell test, a below-threshold QEC demonstration, an NV-center magnetometer, a neutral-atom logical-qubit processor — each requiring a different subset of the series' tools.
- "Reconstruct the core result" means re-deriving the paper's central quantitative claim from the series' formalism, not summarizing the abstract.
- Quantum advantage claims are not all equal: sampling experiments (Google 2019, USTC 2021) are contested by improving classical algorithms; demonstrations of physical principles (threshold theorem, Bell violations) are not subject to the same classical-simulation arms race.
- The paper list dates fast; the framework — identify the problem class, find the central claim, check against theory, assess statistical strength, read the honesty disclaimer — does not.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Identify** (Bloom: Remember) the four research domains represented by the candidate papers: Bell tests, quantum error correction, quantum sensing, and neutral-atom logical processors.
2. **Apply** (Bloom: Apply) the series' formalism to reconstruct a paper's central quantitative result — computing a CHSH value, a predicted logical error rate, or an ODMR transition frequency — from first principles.
3. **Distinguish** (Bloom: Analyze) between demonstrations of physical principles (which cannot be undercut by improved classical algorithms) and computational-advantage claims (which can), and characterize which category each candidate paper falls into.
4. **Evaluate** (Bloom: Evaluate) a quantum paper's statistical strength and explicit limitations using the reading framework in this chapter.
5. **Produce** (Bloom: Create) a 2–3 page technical reconstruction note for one candidate paper, following the rubric in Section 3, in which every step cites the volume and chapter that supplies the tool.

---

## Scene Opening

Here is a sentence from the abstract of a paper published in *Nature* in December 2024 by the Google Quantum AI team:

> "We demonstrate a below-threshold surface code logical qubit whose error rate decreases as code distance increases, with the distance-7 code achieving a logical error rate of 0.143% per cycle."

At the start of Chapter 1 of this volume, you understood "qubit" and perhaps "code." By now you understand the sentence. You know what a surface code is, what code distance means, why scaling it should suppress errors, what "below threshold" means in the context of the threshold theorem, and why $0.143\%$ per cycle is both impressive and far from sufficient for a large Shor factoring computation. You can also identify what the sentence does *not* say — it does not claim fault-tolerant universal computation, it does not claim quantum advantage over classical computers, and it does not claim the qubit is good enough for any practical algorithm.

That last skill — reading what the paper does not claim — is at least as important as reading what it does. The quantum computing literature in 2019–2026 contains several results whose popular interpretation substantially overstated the experimental finding. Learning to distinguish milestone from marketing is not cynicism; it is literacy.

This chapter is structured around four research doorways. Each one opens onto a genre of current quantum mechanics research. Each one requires a specific subset of the series' tools to engage. The goal is not to master any of the four — that is what graduate courses are for. The goal is to read the first two pages of a paper in each genre and know what is happening.

---

## Core Development

### What "reconstruct the core result" means

This is not a literature review, not a summary, not a restatement of the abstract. To reconstruct a paper's core result means: starting from the series' formalism, rederive or recalculate the paper's central quantitative claim from the given physical setup.

For a Bell test paper: given the experimental measurement settings (angles of Alice's and Bob's spin measurement axes), compute the CHSH correlation function $E(\hat a, \hat b)$ and the CHSH parameter $S$ for the appropriate entangled state, and compare to the paper's reported value.

For a QEC paper: given the code distance and your estimate of the physical error rate, use the threshold scaling formula to compute the expected logical error rate and compare to what the paper reports.

For an NV-center sensing paper: given the applied magnetic field and the NV Hamiltonian, compute the ODMR transition frequencies and compare to the dip positions in the paper's spectrum.

**Reconstruct means check.** You are not a passive reader transcribing results. You are verifying the paper's arithmetic against your own first-principles calculation. If your numbers agree, you understand the paper. If they disagree, you have either found an error or, more likely, misunderstood something — and that misunderstanding is the most valuable thing in the exercise.

### How to read a quantum paper: a triage framework

A research paper in quantum mechanics has a structure. Learn the structure and you can navigate papers in unfamiliar subfields faster than you expect.

**Step 1: Identify the problem class.** Bell test? QEC milestone? Quantum sensing? Quantum simulation? Sampling-based quantum advantage? Each class has a characteristic formalism, a characteristic claim structure, and a characteristic set of things that can go wrong. Knowing which class you are in tells you which chapters to reach for.

**Step 2: Find the central claim.** It is usually in the last paragraph of the introduction or the final sentence of the abstract. It is almost always a specific number: $S = 2.42 \pm 0.20$; $p_L = 0.143\%$ per cycle; $T_2 = 2.4$ ms; $\Lambda = 2.14 \pm 0.02$. If you cannot find the number in two minutes of reading, the paper is either poorly written or the claim is more complex than it appears.

**Step 3: Identify the system Hamiltonian.** What are the qubits? What encodes $|0\rangle$ and $|1\rangle$? What drives the gates? For a superconducting transmon, $|0\rangle$ and $|1\rangle$ are the ground and first excited states of an anharmonic LC oscillator. For an NV center, they are the $m_s = 0$ and $m_s = -1$ spin sublevels of a spin-1 electronic state. For a neutral-atom qubit, they are typically two hyperfine ground states of Rb or Cs. The Hamiltonian is almost always stated in the Methods section, often in 2–3 lines.

**Step 4: Identify the observable.** What is being measured, in what basis, and what does the quantum theory predict? For a CHSH experiment: the observable is a two-qubit spin correlation $\langle \sigma_a \otimes \sigma_b \rangle$. For a surface code: the observable is the logical error rate per syndrome cycle. For NV magnetometry: the observable is the fluorescence intensity as a function of applied microwave frequency.

**Step 5: Check against theory.** The quantum theory prediction should appear in the paper, usually in the main text or supplementary material. Locate it. Can you derive it from the series' tools? If yes, the paper is accessible. If not, you have identified the frontier.

**Step 6: Assess statistical strength.** A CHSH violation at $p = 0.039$ from 245 trials (Hensen et al. 2015) is qualitatively different from a violation at $p < 10^{-7}$ from millions of trials (Giustina 2015, Shalm 2015). A QEC demonstration with below-threshold scaling across three code distances is more convincing than a single-distance result. The number of standard deviations separating the claim from the null hypothesis matters. Read papers without error bars with extra caution.

**Step 7: Read the honesty disclaimer.** A well-written paper states explicitly what it cannot demonstrate. "We demonstrate X, which does not imply Y" is a sign of a trustworthy paper. Look for it. Notice when it is absent.

### The honesty layer: contested claims in quantum computing

Not all landmark results in this field are equally secure. Students should carry calibrated skepticism as a permanent posture.

**Google Sycamore (2019):** The Google team reported that a 53-qubit processor performed a random circuit sampling task in 200 seconds that they estimated would take a classical supercomputer 10,000 years [contested: Arute et al. 2019, Nature 574, 505]. IBM disputed this immediately, arguing a better classical algorithm would need only 2.5 days, not 10,000 years. Pan Zhang et al. at the Chinese Academy of Sciences subsequently simulated the same task on a classical GPU cluster in approximately 15 hours (2022). Scott Aaronson's assessment, which represents expert consensus as of 2025: the classical simulation gap is real but narrowing; random circuit sampling was a proof-of-concept, not a useful computation; better quantum supremacy experiments are needed.

The structural issue: **sampling-based quantum advantage claims are inherently fragile** because classical simulation algorithms continue to improve. The task was designed to be classically hard, not useful. Demonstrating that a quantum computer does a contrived task faster than current classical algorithms is a milestone, not an application.

**USTC Jiuzhang (2020, 2021):** Gaussian boson sampling advantage claims, similarly contested on grounds that better classical algorithms may match performance.

**Google Willow below-threshold QEC (December 2024):** This result is on categorically firmer ground [verify: Acharya et al. 2024, Nature 638, 920]. It is not a computational-advantage claim at all. It is a demonstration of a mathematical theorem — the threshold theorem, proved in 1996–1998 — confirmed in hardware for the first time. The fact that logical error rates decrease with code distance below threshold is a statement about quantum physics, not about classical computational complexity. Classical computers cannot simulate their way out of it.

**The structural distinction:** Demonstrations of physical principles (Bell violations, threshold theorem, ODMR splitting) are not subject to the classical-simulation arms race. They are about quantum mechanics being true, not about quantum computers being faster at contrived tasks. This distinction is the single most important epistemic tool for reading the quantum computing literature.

---

## Four Doorways

### Doorway 1 — Loophole-free Bell test

**Representative paper:** Giustina, M. et al. "Significant-loophole-free test of Bell's theorem with entangled photons." *Phys. Rev. Lett.* 115, 250401 (2015). [verify] Also: Shalm, L.K. et al. *Phys. Rev. Lett.* 115, 250402 (2015). [verify]

*(Note for instructors: the Hensen et al. 2015 result — NV spins, $S = 2.42 \pm 0.20$, $p = 0.039$, $n = 245$ — is excellent for pedagogical continuity with Chapter 8's NV-center hardware discussion, but its statistics are marginal. For the reconstruction exercise, Giustina 2015 or Shalm 2015 are preferable: photon-based experiments with $p < 10^{-7}$ and $p < 10^{-8}$ respectively. Both use the same CHSH formalism. This paper list should be updated as the instructor sees fit; the framework below is independent of which specific experiment is chosen.)*

**Problem class:** Bell test. Determines whether correlations between distant measurements exceed the local hidden-variable bound.

**Series tools required:**
- Chapter 2 (this volume): entanglement and Bell states; the state $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$
- Chapter 3 (this volume): CHSH inequality; the local-hidden-variable bound $|S| \leq 2$; the quantum maximum $S = 2\sqrt{2}$
- Vol. 1 / Chapter 10 (Vol. 1): measurement in rotated bases; spin projection operators

**The central claim:** The CHSH parameter $S$ measured on entangled photon pairs exceeds the local-realistic bound $S \leq 2$ by more than $10^7$ standard deviations. Both the locality loophole (settings chosen after photons separate) and the detection loophole (high-efficiency detectors avoid the fair-sampling assumption) are simultaneously closed.

**Reconstruction target:** Given the four measurement angles $\theta_{A_1}, \theta_{A_2}, \theta_{B_1}, \theta_{B_2}$, compute the CHSH parameter for the Bell state $|\Phi^+\rangle$:

$$E(\hat a, \hat b) = \langle \Phi^+|(\hat a \cdot \vec\sigma) \otimes (\hat b \cdot \vec\sigma)|\Phi^+\rangle = \cos(\theta_a - \theta_b)$$

$$S = E(A_1, B_1) + E(A_1, B_2) + E(A_2, B_1) - E(A_2, B_2).$$

For the optimal angles $\theta_{A_1} = 0°$, $\theta_{A_2} = 90°$, $\theta_{B_1} = 45°$, $\theta_{B_2} = -45°$:

$$S = \cos(-45°) + \cos(45°) + \cos(45°) - \cos(135°) = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} = 2\sqrt{2} \approx 2.828.$$

The experimental result falls below $2\sqrt{2}$ (decoherence and imperfect entanglement slightly reduce $S$) but remains well above 2. Compare your calculation to the reported value; the gap between your ideal calculation and the experimental number reflects the experimental imperfections the paper's supplementary material characterizes.

**Honesty layer:** The physics is settled. Bell violations are now routine. What remains is the interpretation: Bell's theorem proves no local realistic theory reproduces quantum predictions, but it does not select among interpretations of quantum mechanics. Bohmian mechanics preserves determinism by giving up locality; many-worlds preserves locality and unitarity by giving up the single-outcome assumption; Copenhagen simply asserts the correlations are primitive. Bell cannot distinguish among them. The physics is fixed; the metaphysics remains contested.

### Doorway 2 — Google Willow: below-threshold surface code QEC

**Representative paper:** Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." *Nature* 638, 920–926 (2025; announced December 2024). arXiv:2408.13687. [verify]

**Problem class:** Quantum error correction milestone. First experimental demonstration of the surface code threshold theorem: logical error rates decrease as code distance increases, at physical error rates below $p_{\text{th}}$.

**Series tools required:**
- Chapter 9 (this volume): surface code; code distance; threshold theorem; scaling formula $p_L \approx A(p/p_{\text{th}})^{\lceil(d+1)/2\rceil}$
- Chapter 6 (this volume): Lindblad equation; $T_1$, $T_2$; amplitude-damping and dephasing channels as the error model
- Chapter 8 (this volume): superconducting transmon qubits; $T_1$ and $T_2$ on Willow

**The central claim:** On the 105-qubit Willow chip, logical error rates for distance-3, -5, and -7 surface codes satisfy the below-threshold scaling. The suppression factor is $\Lambda = 2.14 \pm 0.02$ per unit increase in code distance by 2. The distance-7 logical memory beats the best physical qubit lifetime by $2.4\pm 0.3\times$.

**Reconstruction target:** Use the threshold scaling formula with $p_{\text{th}} = 0.01$, $A = 0.1$:

$$p_L^{(d)} \approx 0.1 \cdot \left(\frac{p}{0.01}\right)^{\lceil(d+1)/2\rceil}.$$

The suppression factor $\Lambda = p_L^{(d)}/p_L^{(d+2)}$ from the formula is

$$\Lambda = \left(\frac{p}{p_{\text{th}}}\right)^{-1} = \frac{p_{\text{th}}}{p}.$$

From the reported $\Lambda = 2.14$: $p_{\text{th}}/p = 2.14$, so $p \approx 0.01/2.14 \approx 0.0047$. Using this effective physical error rate, compute:

$$p_L^{(7)} \approx 0.1 \cdot (0.47)^4 \approx 0.1 \cdot 0.049 \approx 0.0049 \approx 0.49\%.$$

The paper reports $p_L^{(7)} = 0.143\%$, roughly $3\times$ smaller. The discrepancy reflects the fact that $A$ and $p_{\text{th}}$ are themselves distance-dependent at small $d$; the simple formula is a good estimate but not exact for $d = 7$. A student whose calculation lands within a factor of 3–5 of the reported value has correctly understood the scaling.

**Honesty layer:** This demonstration is of a quantum memory, not a quantum computer. The surface code cycles preserve information passively; universal fault-tolerant computation additionally requires logical gates (CNOT, T) implemented transversally or via magic state distillation. These are significantly more demanding. Below-threshold quantum memory is necessary but not sufficient for fault-tolerant universal quantum computation.

**Why this result cannot be classically simulated away:** The threshold theorem is a theorem about quantum physics, not classical complexity. The question "can a classical computer simulate a distance-7 surface code?" is irrelevant: the demonstration is about whether quantum error rates obey a specific scaling law in hardware. That scaling law is either confirmed or it is not; classical simulation speed has nothing to do with it.

### Doorway 3 — NV-center magnetometry

**Representative paper:** Balasubramanian, G. et al. "Nanoscale imaging magnetometry with diamond spins under ambient conditions." *Nature* 455, 648–651 (2008). [verify] Also: Maze, J.R. et al. "Nanoscale magnetic sensing with an individual electronic spin in diamond." *Nature* 455, 644–647 (2008). [verify] For more current demonstrations: Rondin, L. et al. "Magnetometry with nitrogen-vacancy defects in diamond." *Rep. Prog. Phys.* 77, 056503 (2014). [verify]

**Problem class:** Quantum sensing. A single quantum system (an NV-center electron spin) acts as a sensor for an external physical field (a magnetic field), with sensitivity at or below nT/$\sqrt{\text{Hz}}$.

**Series tools required:**
- Vol. 3 / Chapter 9 (perturbation theory): Zeeman perturbation to a known spin Hamiltonian; first-order eigenvalue shifts linear in the field
- Chapter 8 (this volume): NV Hamiltonian, ODMR readout; $D = 2.87$ GHz zero-field splitting; $g\mu_B/h = 28.025$ MHz/mT
- Chapter 6 (this volume): $T_2$ as the coherence time linking to linewidth; longer $T_2$ gives narrower ODMR dips and higher field sensitivity

**The NV Hamiltonian and transition frequencies.** The spin-1 NV$^-$ ground-state Hamiltonian in an axial field $B$ is

$$\hat H_{\text{NV}} = D\hat S_z^2 + g\mu_B B\hat S_z,$$

with eigenvalues $E(0) = 0$, $E(\pm 1) = D \pm g\mu_B B$. The two ODMR transition frequencies from $m_s = 0$ are

$$f_\pm = D \pm \frac{g\mu_B}{h}B \approx 2.87\,\text{GHz} \pm 28\,B\,\text{MHz/mT}.$$

The splitting $\Delta f = f_+ - f_- = 2 \times 28 B\,\text{MHz/mT} = 56B\,\text{MHz/mT}$ is a direct linear readout of the axial field. This is exactly the first-order perturbation theory calculation from Vol. 3, Chapter 9.

**Reconstruction target:** Given a field $B = 30$ mT:

$$f_+ = 2.87\,\text{GHz} + 28 \times 30\,\text{MHz} = 2.87 + 0.84 = 3.71\,\text{GHz},$$
$$f_- = 2.87\,\text{GHz} - 0.84\,\text{GHz} = 2.03\,\text{GHz},$$
$$\Delta f = 1.68\,\text{GHz}.$$

Find the corresponding values in the paper's ODMR spectrum figure and confirm your calculation. The field sensitivity is approximately

$$\eta \approx \frac{1}{\gamma_e T_2 \sqrt{N}}\,\text{T}/\sqrt{\text{Hz}},$$

where $\gamma_e/2\pi = 28$ MHz/mT is the electron gyromagnetic ratio, $T_2$ is the coherence time, and $N$ is the number of measurement repetitions per unit time.

**Honesty layer:** NV magnetometry claims are generally robust and reproducible — the physics is well understood. What varies is the engineering context. Published sensitivities in the nT/$\sqrt{\text{Hz}}$ regime are achieved under controlled laboratory conditions (isotopically purified diamond to extend $T_2$, low temperature, long averaging, careful vibration isolation). Real-world field performance differs. Quantum Brilliance and other companies are developing chip-scale NV arrays, but room-temperature chip-scale performance lags laboratory performance by orders of magnitude as of 2026. The physics is settled; the engineering is ongoing.

### Doorway 4 — Neutral-atom logical qubit processor

**Representative paper:** Bluvstein, D. et al. (QuEra/Harvard/MIT). "Logical quantum processor based on reconfigurable atom arrays." *Nature* 626, 58–65 (2024). [verify] Follow-up: QuEra/Harvard/MIT 2026, *Nature* (January 2026) — 96 logical qubits from 448 atoms. [verify: full citation not confirmed at writing]

**Problem class:** Quantum error correction on neutral atoms. Demonstrates that high-rate codes (not surface codes) on a neutral-atom platform can achieve logical error rates below the corresponding physical error rates, using transversal fault-tolerant gates.

**Series tools required:**
- Chapter 9 (this volume): stabilizer codes, $[\![n,k,d]\!]$ notation, fault-tolerant gates
- Chapter 8 (this volume): neutral-atom qubits, Rydberg blockade, optical tweezers
- Chapter 2 (this volume): entanglement structure of multi-qubit states; tensor products

**The core code: $[\![4,2,2]\!]$.** The simplest detectable code in the Bluvstein 2024 paper encodes 2 logical qubits in 4 physical qubits with code distance 2. The four logical basis states are

$$|0_L 0_L\rangle = \tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle),$$
$$|0_L 1_L\rangle = \tfrac{1}{\sqrt{2}}(|0011\rangle + |1100\rangle),$$
$$|1_L 0_L\rangle = \tfrac{1}{\sqrt{2}}(|0101\rangle + |1010\rangle),$$
$$|1_L 1_L\rangle = \tfrac{1}{\sqrt{2}}(|0110\rangle + |1001\rangle).$$

The stabilizers are $XXXX$ and $ZZZZ$. A transversal CNOT gate — applying CNOTs bitwise between two $[\![4,2,2]\!]$ code blocks — implements a logical CNOT because the bitwise CNOT preserves the code space.

**Reconstruction target:** Verify that $|0_L 0_L\rangle$ is a $+1$ eigenstate of both $XXXX$ and $ZZZZ$. Compute:

$$XXXX\,\tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle) = \tfrac{1}{\sqrt{2}}(|1111\rangle + |0000\rangle) = |0_L 0_L\rangle. \checkmark$$

$$ZZZZ\,\tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle) = \tfrac{1}{\sqrt{2}}(+1 \cdot |0000\rangle + (-1)^4 \cdot |1111\rangle) = \tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle) = |0_L 0_L\rangle. \checkmark$$

The state is in the code space.

**Honesty layer:** The Bluvstein 2024 result demonstrates 48 logical qubits and logical error rates below physical error rates for specific transversal operations. The logical error rates achieved are not yet competitive with the best physical-qubit gate fidelities at scale. The 2026 result (96 logical qubits, 448 atoms) extends the record. Neutral atoms offer long-range connectivity (all atoms can potentially interact via Rydberg excitation) that superconducting chips cannot match, enabling codes that require non-planar connectivity. The trade-off is slower gates and lower inherent fidelity than superconducting systems. Neither platform has yet demonstrated fault-tolerant universal computation at scale.

---

## Worked Example: Reconstructing the CHSH value from a loophole-free Bell test

We reconstruct the core result of a loophole-free Bell test, using the Giustina/Shalm 2015 setting as the prototype.

**Physical setup.** Alice and Bob each hold one photon from an entangled pair in the state $|\Phi^+\rangle = (|HH\rangle + |VV\rangle)/\sqrt{2}$, where $H$ (horizontal polarization) encodes $|0\rangle$ and $V$ (vertical) encodes $|1\rangle$. Alice measures polarization at angle $\theta_a$ from horizontal; Bob at angle $\theta_b$. The measurement axes span the polarization plane.

**Step 1: Write the correlation function.** For $|\Phi^+\rangle$ and planar polarization measurements:

$$E(\hat a, \hat b) = \langle \Phi^+|(\hat a \cdot \vec\sigma) \otimes (\hat b \cdot \vec\sigma)|\Phi^+\rangle = \cos(\theta_a - \theta_b).$$

This is the quantum prediction: the correlation depends only on the relative angle. (Derivation: Chapter 3 of this volume, CHSH section.)

**Step 2: Choose angles and compute the four correlators.** Use the angles that maximize $S$:

$$\theta_{A_1} = 0°, \quad \theta_{A_2} = 90°, \quad \theta_{B_1} = 45°, \quad \theta_{B_2} = -45°.$$

$$E(A_1, B_1) = \cos(0° - 45°) = \cos(-45°) = +\tfrac{1}{\sqrt{2}},$$
$$E(A_1, B_2) = \cos(0° - (-45°)) = \cos(45°) = +\tfrac{1}{\sqrt{2}},$$
$$E(A_2, B_1) = \cos(90° - 45°) = \cos(45°) = +\tfrac{1}{\sqrt{2}},$$
$$E(A_2, B_2) = \cos(90° - (-45°)) = \cos(135°) = -\tfrac{1}{\sqrt{2}}.$$

**Step 3: Compute $S$.** Using $S = E(A_1,B_1) + E(A_1,B_2) + E(A_2,B_1) - E(A_2,B_2)$:

$$S = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} - \left(-\frac{1}{\sqrt{2}}\right) = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.828.$$

**Step 4: Compare to the local-realistic bound.** Any local hidden-variable model satisfies $|S| \leq 2$ (derived in Chapter 3). The quantum prediction $S = 2\sqrt{2} \approx 2.828$ exceeds this by $0.828$ — the gap that experiments are designed to resolve.

**Step 5: Compare to the experimental result.** Giustina et al. 2015 report $S > 2$ with statistical significance $p < 3.74 \times 10^{-31}$. The experimental $S$ falls slightly below $2\sqrt{2}$ because of photon loss, detection inefficiency, and residual decoherence in the entangled state — all of which slightly mix the Bell state toward a classical state with lower $S$. The quantum theory predicts a mixed-state correction; the paper's supplementary material derives it. Your ideal calculation $S = 2\sqrt{2}$ is the upper bound; the experimental value is below it but above 2 by an unambiguous margin.

**Step 6: Note the loophole-closing.** The locality loophole is closed because Alice's and Bob's settings are chosen by a random-number generator within the light-travel time between the two stations — no signal traveling at or below $c$ can carry information from one setting choice to the other measurement. The detection loophole is closed by high-efficiency superconducting single-photon detectors that detect a large enough fraction of the photon pairs to make the "fair-sampling" assumption unnecessary.

**The lesson.** The entire reconstruction uses only the CHSH machinery from Chapter 3, the Bell-state definition from Chapter 2, and first-year linear algebra. You have verified the central quantitative claim of a Nobel-adjacent experiment using tools you learned in this volume.

**The limit.** Your reconstruction assumed a perfect Bell state and zero decoherence, giving $S = 2\sqrt{2}$. The experiment achieves $S < 2\sqrt{2}$ because the entangled state is slightly mixed. A more complete reconstruction would model the mixed-state density matrix $\hat\rho = (1-\epsilon)|\Phi^+\rangle\langle\Phi^+| + \epsilon \hat I/4$, compute $S(\epsilon)$, and fit $\epsilon$ from the experimental $S$ value. This connects Chapters 1 (density matrix) and 3 (CHSH) and is a natural extension exercise.

---

## The Rubric

A reconstruction note should demonstrate the following, weighted as indicated:

| Category | Weight | What it means |
|----------|--------|---------------|
| System identification | 20% | Correctly identify the physical qubit(s), the Hamiltonian or state, and the encoding of $\|0\rangle$ and $\|1\rangle$. |
| Observable and measurement | 20% | State which observable is measured, in what basis, and what the quantum theory predicts. |
| Core calculation | 30% | Reproduce the central quantitative result from the series' formalism. Numbers must match the paper to within stated error bars or within a factor of 2–3 for formula-based estimates. |
| Connections to prior chapters | 15% | Explicitly identify which volume and chapter each key tool comes from. E.g., "the CHSH bound of 2 derives from Chapter 3 (this volume)." |
| Honest assessment | 15% | State one thing the paper explicitly does not claim. Identify whether the result is a demonstration of a physical principle, a hardware benchmark, or a computational-advantage claim, and state the implications. |

The rubric is designed so that a student who understands the formalism but has not read the paper carefully can pass the calculation portion (30%) but will lose points on the honest assessment (15%) — which is the harder thing to fake.

---

## Common Misconceptions

**"Google demonstrated a quantum computer in 2019."** The Sycamore experiment demonstrated that a quantum processor completed a specific randomly chosen task faster than the best available classical simulation algorithm — at the time. It did not demonstrate a general-purpose quantum computer, a practically useful computation, or a result that could not in principle be matched by an improved classical algorithm. The classical-simulation gap has since been narrowed by Pan Zhang et al. (2022). The experiment is a milestone in the physics of quantum information; it is not the arrival of quantum computing as a technology.

**"Bell violations prove quantum mechanics is non-local."** Bell's theorem proves that no local *realistic* theory reproduces the quantum predictions. It does not prove non-locality in any operationally useful sense. Alice cannot use her measurement to send information to Bob — her outcomes are random, and Bob's reduced density matrix is $\hat I/2$ regardless of what Alice does. The no-signaling theorem is a theorem about quantum mechanics, compatible with the Bell result. "Non-locality" in the technical sense means the correlations cannot be reproduced by pre-shared classical information; it does not mean superluminal influence.

**"QEC is solved."** Error correction has been demonstrated below threshold in hardware (Google Willow, 2024). This is a major milestone. It is not the same as fault-tolerant universal quantum computation, which requires additional capabilities (transversal logical gates, magic state distillation, real-time classical decoding) at scale. As of early 2026, no platform has demonstrated fault-tolerant universal computation. The physical qubit count required for practically useful computations (millions of physical qubits) exceeds current hardware by 3–4 orders of magnitude.

**"If the experiment agrees with quantum theory, the interpretation is settled."** Every experiment in this chapter agrees with quantum mechanics. Quantum mechanics predicts all of them. The measurement problem — why one specific outcome obtains in a single run — is not addressed by any of these experiments. Decoherence explains why outcomes look classical; it does not explain why a single outcome obtains. Different interpretations (Copenhagen, many-worlds, Bohmian, GRW, QBism) agree on all predictions but disagree on what is happening. Experiments cannot choose among interpretations that make identical predictions.

**"The qubit counts in press releases equal useful computational power."** The number of logical qubits demonstrated (48, 96, 128, ...) tells you the size of the QEC experiment. It does not directly translate to computational power. A 1,000-logical-qubit fault-tolerant computer requires roughly 1–10 million physical qubits at current code overhead; no platform is close. Track logical qubit counts with the same care you would apply to reading marketing copy.

---

## Exercises

### Warm-up

**1.** *[Tests: problem-class identification; triage framework]* For each of the following paper abstracts (paraphrased), identify: (a) the problem class (Bell test / QEC / quantum sensing / quantum advantage claim / other); (b) the central quantitative claim (find the number); (c) which chapters of this volume supply the primary tools.

- "We report ODMR measurements on a single NV center under a 47 mT axial field, observing two resonances at 4.19 GHz and 1.55 GHz."
- "We demonstrate a distance-5 surface code with logical error rate $p_L = 0.31\%$ per cycle, suppressed by a factor of 1.6 relative to the distance-3 code."
- "We observe $S = 2.67 \pm 0.09$ from 14,000 entangled photon pairs, closing both the locality and detection loopholes."

**2.** *[Tests: CHSH calculation; quantum vs. classical bound]* For the Bell state $|\Phi^+\rangle$ and the sub-optimal angle choice $\theta_{A_1} = 0°$, $\theta_{A_2} = 60°$, $\theta_{B_1} = 30°$, $\theta_{B_2} = 90°$: compute all four correlators $E(A_i, B_j) = \cos(\theta_{A_i} - \theta_{B_j})$, evaluate $S$, and determine whether this choice violates the CHSH bound. Is it optimal? What is the ratio $S/S_{\max}$?

**3.** *[Tests: NV ODMR reconstruction]* An NV center is in a field $B = 50$ mT along the NV axis. (a) Compute the two ODMR transition frequencies using $D = 2.87$ GHz and $g\mu_B/h = 28$ MHz/mT. (b) If $T_2^* = 0.5\,\mu$s (the free-induction-decay coherence time), estimate the Fourier-limited linewidth of each dip (FWHM $\approx 1/(\pi T_2^*)$ in Hz). (c) An experiment reports dips at $1.65$ GHz and $4.09$ GHz. What is the applied field?

### Application

**4.** *[Apply+: threshold scaling reconstruction]* Use the surface code threshold formula $p_L \approx 0.1 \cdot (p/0.01)^{\lceil(d+1)/2\rceil}$ and the reported suppression factor $\Lambda = 2.14$ from Acharya et al. 2024 to: (a) Estimate the effective physical error rate $p$ on Willow (use $\Lambda \approx p_{\text{th}}/p$). (b) Predict $p_L$ for $d = 3, 5, 7$ using this $p$. (c) The paper reports $p_L^{(7)} = 0.143\%$. By what factor does your prediction differ from the measurement? Suggest one physical reason for the discrepancy.

**5.** *[Apply+: $[\![4,2,2]\!]$ stabilizer check]* Verify that the state $|0_L 1_L\rangle = \frac{1}{\sqrt{2}}(|0011\rangle + |1100\rangle)$ is a $+1$ eigenstate of both $XXXX$ and $ZZZZ$. Show your work explicitly. Then show that a single $Z$ error on qubit 1 maps $|0_L 1_L\rangle$ to an orthogonal state and can therefore be detected (though not corrected, since the code distance is 2).

**6.** *[Apply+: mixed-state CHSH]* A slightly noisy Bell source produces the mixed state $\hat\rho = (1-\epsilon)|\Phi^+\rangle\langle\Phi^+| + \frac{\epsilon}{4}\hat I_4$, where $\hat I_4$ is the $4\times 4$ identity (maximally mixed state) and $\epsilon$ parameterizes the noise. (a) Compute the correlation function $E(\hat a, \hat b) = \text{Tr}[\hat\rho\,(\hat a\cdot\vec\sigma)\otimes(\hat b\cdot\vec\sigma)]$ for this state using the optimal CHSH angles. (b) At what value of $\epsilon$ does $S$ drop to the CHSH bound $S = 2$ (so the state can no longer demonstrate Bell inequality violation)? (c) Giustina et al. 2015 measure $S$ significantly above 2. Bound the noise parameter $\epsilon$ in their source.

### Synthesis

**7.** *[Produce: technical reconstruction note]* Choose one of the four doorway papers (or, with instructor approval, a different current paper in one of the four genres). Write a 2–3 page technical note following the rubric in this chapter. Your note must: (a) identify the physical system and Hamiltonian; (b) reproduce the central quantitative result from first principles; (c) cite each tool by volume and chapter; (d) state explicitly one thing the paper does not demonstrate; (e) assess the statistical strength of the result (number of standard deviations, number of trials, or equivalent). Submit with your calculation shown step by step.

**8.** *[Synthesis: classify the results]* For each of the four results below, classify it as (i) demonstration of a physical principle, (ii) hardware benchmark, or (iii) computational-advantage claim. Justify your classification and explain which classification is most resistant to being undercut by improved classical algorithms.

- Google Sycamore random circuit sampling (Arute et al. 2019).
- Hensen et al. 2015 loophole-free Bell test ($S = 2.42 \pm 0.20$).
- Acharya et al. 2024 below-threshold surface code ($\Lambda = 2.14$).
- Bluvstein et al. 2024 neutral-atom 48 logical qubits.

---

## Still Puzzling

**The measurement problem, again.** We have a complete formalism — density matrices, Lindblad operators, stabilizer codes, CHSH inequalities — that predicts the statistics of every experiment to extraordinary precision. We have decoherence to explain why outcomes look classical when the environment is monitoring. What we do not have, and what the textbook cannot give you, is a derivation from first principles of why one particular outcome obtains in one particular run. Decoherence explains the *distribution*; it does not explain the *selection*. Copenhagen asserts it without explanation; many-worlds says all outcomes occur and you are in one branch; Bohmian mechanics uses a pilot wave. None of these adds a prediction the others do not make. Schlosshauer (2007) is the cleanest accessible treatment of exactly where decoherence stops. The honest answer is that the textbook gives you tools that work; it does not give you a resolved metaphysics. This is not a failure of the tools. It is a frontier.

**Whether practical quantum advantage arrives, and when.** As of mid-2026: no practically useful quantum advantage has been demonstrated on a real-world problem. The NIST post-quantum cryptography standards (FIPS 203, 204, 205) were finalized in August 2024 — the world's cryptographic infrastructure is already being updated in anticipation of fault-tolerant quantum computers that do not yet exist. If fault-tolerant machines arrive, Shor's algorithm will break RSA. The lattice-based replacements (Kyber, Dilithium, SPHINCS+) in the NIST standards are believed to be quantum-resistant, but "believed" is not "proven." The societal consequences are already being implemented; the physical capability remains on a roadmap.

**Whether topological quantum computation will work.** Microsoft and others have pursued Majorana-based topologically protected qubits for two decades — systems whose error protection is enforced by topology rather than active correction, potentially eliminating most of the overhead. The physics is beautiful; the engineering is unforgiving. As of 2026, no topological qubit has outperformed a surface-code qubit on a competing hardware platform. The field remains open.

---

## The +1 — Simulation Exercise

You will build a "paper-reading assistant" simulation in D3.js — not a simulator of physics, but a simulator of the analysis framework. It has three tabs, each implementing one quantitative reconstruction task from the chapter.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md:

Chapter 10 — Capstone: Quantum Mechanics in Research
Deliverable: 11-paper-reading-assistant.html
Status: in progress

Three-tab HTML application:

Tab 1 — CHSH calculator (Bell test reconstruction).
Tab 2 — Surface-code threshold calculator (QEC reconstruction).
Tab 3 — NV-center ODMR calculator (sensing reconstruction).

Tab 1 — CHSH calculator.
Layout: 700 x 500. Four angle sliders: theta_A1, theta_A2, theta_B1,
theta_B2, each 0 to 360 degrees. Live computation of:
- Four correlators E(A1,B1), E(A1,B2), E(A2,B1), E(A2,B2)
  shown as a 2x2 table.
- CHSH parameter S = E11 + E12 + E21 - E22.
- Background color: amber when |S| > 2 (classical bound exceeded).
- Large S display at 48pt.
State selector: radio buttons for |Phi+>, |Phi->, |Psi+>, |Psi->,
plus a "mixed state" slider for epsilon in [0, 1] giving
rho = (1-eps)|Phi+><Phi+| + (eps/4) I_4.
Show: how S degrades as epsilon increases; the critical epsilon
at which S = 2 (local-realistic boundary).
Preset button: "Optimal angles" sets theta to 0, 90, 45, -45.
Preset button: "Giustina 2015" displays the measurement settings
and reports S_expected.

Tab 2 — Surface code threshold.
Layout: 700 x 500. Log-log plot of p_L vs p for d = 3, 5, 7.
Formula: p_L = 0.1 * (p/0.01)^ceil((d+1)/2).
Draggable vertical cursor at adjustable p. Sidebar: read off p_L(d=3),
p_L(d=5), p_L(d=7) at the cursor position.
Willow data point: (p_eff = 0.0047, p_L = 0.00143) marked on the d=7
curve as a filled circle.
Lambda display: for the current p, Lambda = (p_th/p). Show Lambda.
When Lambda > 1 (below threshold): label "below threshold: larger d is
better." When Lambda < 1: label "above threshold: larger d is worse."
Input field: enter a target p_L and read off the required d.

Tab 3 — NV-center ODMR.
Layout: 700 x 400.
Sliders: B (0 to 100 mT), theta (0 to 90 degrees off NV axis),
T2_star (0.01 to 10 microseconds, log scale).
Computed spectrum: Lorentzian dips at f_+ and f_-, with:
  f_+/- = D +/- (g mu_B / h) * B * cos(theta)
  FWHM = 1 / (pi * T2_star) in Hz, converted to MHz.
Display D = 2.87 GHz, g*mu_B/h = 28.025 MHz/mT.
Show the 3x3 spin Hamiltonian matrix for the current B, theta.
Show eigenvalues and label the two ODMR transitions.
Preset button: "B = 30 mT, theta = 0" — reproduce the chapter
reconstruction example; verify dips at 3.71 and 2.03 GHz.
Sensitivity estimate: eta = 1 / (gamma_e * T2_star * sqrt(N_approx))
displayed, where N_approx = 1 (for one measurement per T2_star).
```

### Part 2 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 11-paper-reading-assistant.html: a single self-contained HTML
file using D3 v7 from a CDN, no other dependencies.

The page has a header ("Chapter 10 — Paper Reading Assistant") and a
horizontal tab strip with three tabs:
  [ Bell Test (CHSH) ]  [ QEC Threshold ]  [ NV Magnetometry ]

TAB 1 — CHSH calculator.
Four sliders (theta in degrees, 0-360) for Alice A1, A2 and Bob B1, B2.
State selector: |Phi+>, |Phi->, |Psi+>, |Psi-> plus epsilon slider
for the mixed-state interpolation rho = (1-eps)|Phi+><Phi+| + eps I_4/4.

For the four Bell states, the correlation function for state |Phi+> is:
  E(a, b) = cos(theta_a - theta_b)
For |Phi->:   E(a, b) = -cos(theta_a - theta_b)
For |Psi+>:   E(a, b) = cos(theta_a + theta_b) [verify sign convention]
For |Psi->:   E(a, b) = -cos(theta_a + theta_b)
For the mixed state rho:
  E_mixed(a, b) = (1 - eps) * E_pure(a, b)

Compute S = E(A1,B1) + E(A1,B2) + E(A2,B1) - E(A2,B2).
Display: 2x2 table of E values, large S value, amber background if |S| > 2.
Critical epsilon: solve (1-eps) * S_optimal = 2 for eps; display.
Two preset buttons: [Optimal angles] and [Show Tsirelson bound 2*sqrt(2)].

TAB 2 — QEC threshold plot (as specified in PROJECT.md above).

TAB 3 — NV ODMR calculator (as specified in PROJECT.md above).
Implement the 3x3 spin Hamiltonian diagonalization analytically.
For axial field (theta = 0), eigenvalues are 0, D+g*mu_B*B, D-g*mu_B*B.
For off-axis, diagonalize the 3x3 matrix
  H = D * diag(1, 0, 1) shifted by zero-field, plus
  g*mu_B*B*cos(theta) * S_z + g*mu_B*B*sin(theta) * S_x
where S_z = diag(1, 0, -1) and S_x = (1/sqrt(2))*[[0,1,0],[1,0,1],[0,1,0]]
for spin-1. Compute eigenvalues numerically.

Sanity checks (console):
- Tab 1: at theta = 0, 90, 45, -45 and |Phi+>, S should equal 2*sqrt(2)
  within 0.001.
- Tab 1: at epsilon = 0.5 for |Phi+>, S should be (1-0.5)*2*sqrt(2).
- Tab 2: at p = p_th = 0.01, all three curves meet at p_L = 0.1 (= A).
- Tab 3: at B = 0, only one dip at 2.87 GHz (f_+ = f_- = D).
- Tab 3: at B = 30 mT, theta = 0: dips at 3.71 and 2.03 GHz.
```

### Part 3 — Exploration tasks

1. **Tab 1, Bell test.** Set angles to $\theta_{A_1} = 0°$, $\theta_{A_2} = 90°$, $\theta_{B_1} = 45°$, $\theta_{B_2} = -45°$, state $|\Phi^+\rangle$. Confirm $S = 2\sqrt{2} \approx 2.828$. Now slowly increase the mixed-state noise parameter $\epsilon$. At what $\epsilon$ does the background flip from amber to white? Explain what this value of $\epsilon$ means physically.

2. **Tab 1, state dependence.** Keep the optimal CHSH angles. Switch the state from $|\Phi^+\rangle$ to $|\Psi^-\rangle$. Does $|S|$ change? What does this tell you about which Bell states are maximally entangled?

3. **Tab 2, threshold.** Set the cursor to $p = 0.0047$ (the Willow effective error rate). Read off $p_L$ for $d = 3, 5, 7$. How does your reading compare to the paper's reported $p_L^{(7)} = 0.143\%$? Move the cursor to $p = 0.05$. The $d = 7$ curve is now the worst. What does this switching of order represent?

4. **Tab 2, target.** Enter a target $p_L = 10^{-6}$ in the input field. What code distance is required at $p = 0.002$? How many physical qubits does that code require (approximately $2d^2$)?

5. **Tab 3, ODMR reconstruction.** Set $B = 50$ mT, $\theta = 0°$. Read the two dip frequencies. Verify analytically: $f_\pm = 2.87 \pm 28 \times 50 / 1000 = 2.87 \pm 1.40$ GHz, giving $f_+ = 4.27$ GHz and $f_- = 1.47$ GHz. Slide $B$ slowly to zero. The two dips merge at $2.87$ GHz. This is the zero-field splitting $D$ — the gap that exists even without any applied field.

6. **Tab 3, off-axis.** Set $B = 30$ mT. Slide $\theta$ from $0°$ to $90°$. Watch the two ODMR dips shift. At $\theta = 90°$ (field perpendicular to NV axis), the effective axial component of $B$ is zero — but the dips do not merge completely. Why? (Hint: look at the displayed $3\times 3$ Hamiltonian matrix and its eigenvalues.)

---

## References

- Giustina, M. et al. "Significant-loophole-free test of Bell's theorem with entangled photons." *Phys. Rev. Lett.* 115, 250401 (2015). [verify]
- Shalm, L.K. et al. "Strong loophole-free test of local realism." *Phys. Rev. Lett.* 115, 250402 (2015). [verify]
- Hensen, B. et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 km." *Nature* 526, 682–686 (2015). [verify]
- Arute, F. et al. (Google Quantum AI). "Quantum supremacy using a programmable superconducting processor." *Nature* 574, 505–510 (2019). [verify] [contested: classical simulation gap narrowed by subsequent work; see Pan Zhang et al. 2022]
- Pan Zhang et al. "Simulating quantum mean values in noisy variational quantum algorithms." 2022. [verify: classical simulation of Sycamore — full citation needed]
- Acharya, R. et al. (Google Quantum AI). "Suppressing quantum errors by scaling a surface code logical qubit." *Nature* 614, 676–681 (2023). [verify]
- Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." *Nature* 638, 920–926 (2025). arXiv:2408.13687. [verify]
- Bluvstein, D. et al. (QuEra/Harvard/MIT). "Logical quantum processor based on reconfigurable atom arrays." *Nature* 626, 58–65 (2024). [verify]
- QuEra/Harvard/MIT. "96 logical qubits from 448 physical atoms." *Nature* (January 2026). [verify: full citation not confirmed at writing; confirm before publication]
- Balasubramanian, G. et al. "Nanoscale imaging magnetometry with diamond spins under ambient conditions." *Nature* 455, 648–651 (2008). [verify]
- Maze, J.R. et al. "Nanoscale magnetic sensing with an individual electronic spin in diamond." *Nature* 455, 644–647 (2008). [verify]
- Rondin, L. et al. "Magnetometry with nitrogen-vacancy defects in diamond." *Rep. Prog. Phys.* 77, 056503 (2014). [verify]
- Doherty, M.W. et al. "The nitrogen-vacancy colour centre in diamond." *Phys. Rep.* 528, 1–45 (2013). [verify]
- Schlosshauer, M. *Decoherence and the Quantum-to-Classical Transition.* Springer (2007).
- Preskill, J. "Quantum computing in the NISQ era and beyond." *Quantum* 2, 79 (2018). [verify]
- Hasan, M.Z. and Kane, C.L. "Colloquium: Topological insulators." *Rev. Mod. Phys.* 82, 3045 (2010). [verify]
- NIST FIPS 203 (ML-KEM / Kyber), FIPS 204 (ML-DSA / Dilithium), FIPS 205 (SLH-DSA / SPHINCS+). National Institute of Standards and Technology, August 2024. [verify]
- Gottesman, D. "Stabilizer codes and quantum error correction." PhD thesis, California Institute of Technology (1997). arXiv:quant-ph/9705052. [verify]
- Aaronson, S. Blog posts on quantum advantage and classical simulation (scottaaronson.blog, 2019–2022). [verify: specific post dates and URLs for final citation]
