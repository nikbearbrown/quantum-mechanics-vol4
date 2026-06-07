# Chapter 10 — Capstone: Quantum Mechanics in Research

Consider a sentence from the abstract of a paper published in *Nature* in December 2024 by the Google Quantum AI team:

> "We demonstrate a below-threshold surface code logical qubit whose error rate decreases as code distance increases, with the distance-7 code achieving a logical error rate of 0.143% per cycle."

At the start of this volume, you understood "qubit" and perhaps "code." We can now parse the entire sentence. We know what a surface code is, what code distance means, why scaling it should suppress errors, what "below threshold" means in the context of the threshold theorem, and why $0.143\%$ per cycle is both impressive and far from sufficient for a large Shor factoring computation. We can also identify what the sentence does *not* say — it does not claim fault-tolerant universal computation, it does not claim quantum advantage over classical computers, and it does not claim the qubit is good enough for any practical algorithm.

That last skill — reading what the paper does not claim — is at least as important as reading what it does. The quantum computing literature in 2019–2026 contains several results whose popular interpretation substantially overstated the experimental finding. Learning to distinguish milestone from marketing is not cynicism; it is literacy.

This chapter is structured around four research doorways. Each opens onto a genre of current quantum mechanics research; each requires a different subset of this volume's tools. The goal is not to master any of the four — that is what graduate courses are for. The goal is to read the first two pages of a paper in each genre and know what is happening.

---

## What "Reconstruct the Core Result" Means

This is not a literature review or a summary. To reconstruct a paper's core result means: starting from the formalism, re-derive or recalculate the paper's central quantitative claim from the given physical setup.

For a Bell test paper: given the measurement settings, compute the CHSH correlation function and the CHSH parameter $S$ for the appropriate entangled state, and compare to the paper's reported value.

For a QEC paper: given the code distance and physical error rate, use the threshold scaling formula to compute the expected logical error rate and compare to what the paper reports.

For an NV sensing paper: given the applied magnetic field and the NV Hamiltonian, compute the ODMR transition frequencies and compare to the dip positions in the paper's spectrum.

**Reconstruct means check.** You are verifying the paper's arithmetic against a first-principles calculation. If your numbers agree, you understand the paper. If they disagree, you have either found an error or, more likely, misunderstood something — and that misunderstanding is the most valuable thing in the exercise.

---

## How to Read a Quantum Paper: A Triage Framework

A research paper in quantum mechanics has a structure. Learning the structure allows you to navigate papers in unfamiliar subfields more efficiently than you might expect.

**Step 1: Identify the problem class.** Bell test? QEC milestone? Quantum sensing? Sampling-based advantage claim? Each class has a characteristic formalism, a characteristic claim structure, and a characteristic set of things that can go wrong. Knowing which class you are in tells you which chapters to reach for.

**Step 2: Find the central claim.** It is usually in the last paragraph of the introduction or the final sentence of the abstract. It is almost always a specific number: $S = 2.42\pm0.20$; $p_L = 0.143\%$ per cycle; $T_2 = 2.4$ ms; $\Lambda = 2.14\pm0.02$. If you cannot find the number in two minutes, the paper is either poorly written or the claim is more complex than it appears.

**Step 3: Identify the system Hamiltonian.** What are the qubits? What encodes $|0\rangle$ and $|1\rangle$? For a superconducting transmon: ground and first excited states of an anharmonic LC oscillator. For an NV center: the $m_s = 0$ and $m_s = -1$ spin sublevels of a spin-1 electronic state. For a neutral-atom qubit: two hyperfine ground states of Rb or Cs. The Hamiltonian is almost always stated in the Methods section, often in 2–3 lines.

**Step 4: Identify the observable.** What is being measured, in what basis, and what does quantum theory predict?

**Step 5: Check against theory.** The quantum theory prediction should appear in the paper. Can you derive it from this volume's tools? If yes, the paper is accessible. If not, you have identified the frontier.

**Step 6: Assess statistical strength.** A CHSH violation at $p = 0.039$ from 245 trials is qualitatively different from $p < 10^{-7}$ from millions of trials. A QEC demonstration with below-threshold scaling across three code distances is more convincing than a single-distance result. Papers without error bars deserve extra scrutiny.

**Step 7: Read the honesty disclaimer.** A well-written paper states explicitly what it cannot demonstrate. "We demonstrate X, which does not imply Y" is a sign of a trustworthy paper. Look for it. Notice when it is absent.

---

## The Honesty Layer: Contested Claims in Quantum Computing

Not all landmark results are equally secure.

**Google Sycamore (2019):** The Sycamore processor completed a specific randomly-chosen sampling task in 200 seconds that the team estimated would take a classical supercomputer 10,000 years. IBM disputed this immediately, arguing a better algorithm would need only 2.5 days. Pan Zhang et al. subsequently simulated the same task on a GPU cluster in roughly 15 hours (2022). As of 2025, the classical simulation gap is real but has narrowed substantially. [contested: Arute et al. 2019, *Nature* 574, 505]

**The structural issue:** Sampling-based quantum advantage claims are inherently fragile because classical simulation algorithms continue to improve. The task was designed to be classically hard, not useful. Demonstrating that a quantum processor does a contrived task faster than current classical algorithms is a milestone, not an application.

**Google Willow below-threshold QEC (December 2024):** This result is on categorically firmer ground. It is not a computational-advantage claim at all. It is a demonstration of a mathematical theorem — the threshold theorem, proved in 1996–1998 — confirmed in hardware. The fact that logical error rates decrease with code distance below threshold is a statement about quantum physics, not about classical computational complexity. Classical computers cannot simulate their way out of it. [verify: Acharya et al. 2024, *Nature* 638, 920]

The structural distinction: **demonstrations of physical principles** (Bell violations, threshold theorem, ODMR splitting) are not subject to the classical-simulation arms race. They are about quantum mechanics being true, not about quantum computers being faster at contrived tasks. This distinction is the single most important epistemic tool for reading the quantum computing literature.

---

## Four Doorways

### Doorway 1 — Loophole-Free Bell Test

**Representative papers:** Giustina, M. et al. *Phys. Rev. Lett.* 115, 250401 (2015); Shalm, L.K. et al. *Phys. Rev. Lett.* 115, 250402 (2015). [verify]

*Note for instructors: Hensen et al. 2015 (NV spins, $S = 2.42\pm0.20$, $p = 0.039$, $n = 245$) provides excellent continuity with Chapter 8's NV hardware discussion but has marginal statistics. Giustina 2015 or Shalm 2015 ($p < 10^{-7}$ and $p < 10^{-8}$ respectively) are preferable for the reconstruction exercise. The CHSH formalism is identical regardless.*

**Problem class:** Bell test. Determines whether measured correlations between distant entangled particles exceed the local hidden-variable bound.

**Series tools required:** Chapter 2 (Bell states); Chapter 3 (CHSH inequality; local-realistic bound $|S| \leq 2$; quantum maximum $S = 2\sqrt{2}$); Vol. 1 Chapter 10 (measurement in rotated bases).

**Reconstruction target:** Given the four measurement angles $\theta_{A_1}, \theta_{A_2}, \theta_{B_1}, \theta_{B_2}$, compute the CHSH parameter for $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$:

$$E(\hat a, \hat b) = \langle\Phi^+|(\hat a\cdot\vec\sigma)\otimes(\hat b\cdot\vec\sigma)|\Phi^+\rangle = \cos(\theta_a - \theta_b),$$

$$S = E(A_1,B_1) + E(A_1,B_2) + E(A_2,B_1) - E(A_2,B_2).$$

The experimental $S$ falls slightly below $2\sqrt{2}$ due to decoherence and detection imperfections, but remains well above 2. The ideal calculation sets the upper bound; the gap to the experimental value reflects imperfections quantified in the supplementary material.

**Honesty layer:** The physics is settled. Bell violations are now routine. What Bell's theorem does *not* determine is the interpretation of quantum mechanics: Bohmian mechanics preserves determinism by giving up locality; many-worlds preserves locality by giving up the single-outcome assumption; Copenhagen asserts correlations are primitive. Bell cannot distinguish among them.

### Doorway 2 — Google Willow: Below-Threshold Surface Code QEC

**Representative paper:** Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." *Nature* 638, 920–926 (2025). arXiv:2408.13687. [verify]

**Problem class:** QEC milestone. First experimental confirmation of the threshold theorem: logical error rates decrease as code distance increases at physical error rates below $p_\text{th}$.

**Series tools required:** Chapter 9 (surface code; code distance; threshold theorem; suppression formula); Chapter 6 (Lindblad equation; $T_1$, $T_2$; amplitude-damping and dephasing channels as the error model); Chapter 8 (superconducting transmon qubits).

**Reconstruction target:** We use the threshold scaling formula with $p_\text{th} = 0.01$, $A = 0.1$:

$$p_L^{(d)} \approx 0.1\cdot\left(\frac{p}{0.01}\right)^{\lceil(d+1)/2\rceil}.$$

The suppression factor $\Lambda = p_L^{(d)}/p_L^{(d+2)} \approx p_\text{th}/p$. From the reported $\Lambda = 2.14$: $p \approx 0.01/2.14 \approx 0.0047$. Using this effective physical error rate:

$$p_L^{(7)} \approx 0.1\cdot(0.47)^4 \approx 0.0049 \approx 0.49\%.$$

The paper reports $p_L^{(7)} = 0.143\%$ — roughly $3\times$ smaller. The discrepancy reflects the fact that the simple scaling formula is not exact at small $d$; a student whose calculation lands within a factor of 3–5 of the reported value has correctly understood the scaling.

**Why this result cannot be classically simulated away:** The threshold theorem is a theorem about quantum physics. The demonstration is about whether quantum error rates obey a specific scaling law in hardware — classical simulation speed has nothing to do with it.

**Honesty layer:** This demonstrates a quantum *memory*, not a quantum *computer*. Universal fault-tolerant computation additionally requires logical gates (CNOT, T) implemented transversally or via magic state distillation. Below-threshold quantum memory is necessary but not sufficient.

### Doorway 3 — NV-Center Magnetometry

**Representative papers:** Balasubramanian, G. et al. *Nature* 455, 648 (2008); Maze, J.R. et al. *Nature* 455, 644 (2008). [verify] For current review: Rondin, L. et al. *Rep. Prog. Phys.* 77, 056503 (2014). [verify]

**Problem class:** Quantum sensing. A single NV-center electron spin acts as a sensor for an external magnetic field, with sensitivity at or below nT/$\sqrt{\text{Hz}}$.

**Series tools required:** Vol. 3 Chapter 9 (Zeeman perturbation; first-order eigenvalue shifts linear in the applied field); Chapter 8 (NV Hamiltonian; ODMR readout; $D = 2.87$ GHz zero-field splitting; $g\mu_B/h = 28.025$ MHz/mT); Chapter 6 ($T_2$ as coherence time linking to linewidth).

**The NV Hamiltonian and transition frequencies.** The spin-1 $\text{NV}^-$ ground-state Hamiltonian in an axial field $B$:

$$\hat H_\text{NV} = D\hat S_z^2 + g\mu_B B\hat S_z,$$

with eigenvalues $E(0) = 0$, $E(\pm 1) = D \pm g\mu_B B$. The two ODMR transition frequencies from $m_s = 0$:

$$f_\pm = D \pm \frac{g\mu_B}{h}B \approx 2.87\,\text{GHz} \pm 28B\,\text{MHz/mT}.$$

The splitting $\Delta f = 56B$ MHz/mT is a direct linear readout of the axial field — exactly the first-order perturbation theory calculation from Vol. 3.

**Reconstruction target.** For $B = 30$ mT:

$$f_+ = 2.87 + 0.84 = 3.71\,\text{GHz}, \qquad f_- = 2.87 - 0.84 = 2.03\,\text{GHz}.$$

Find the corresponding dip positions in the paper's ODMR spectrum and confirm. The field sensitivity:

$$\eta \approx \frac{1}{\gamma_e T_2\sqrt{N}}\,\text{T}/\sqrt{\text{Hz}},$$

where $\gamma_e/2\pi = 28$ MHz/mT and $N$ is measurement repetitions per unit time.

**Honesty layer:** NV magnetometry claims are generally robust. Published sensitivities in the nT/$\sqrt{\text{Hz}}$ regime are achieved under controlled laboratory conditions (isotopically purified diamond, low temperature, long averaging, vibration isolation). Room-temperature chip-scale performance lags laboratory performance by orders of magnitude as of 2026. The physics is settled; the engineering is ongoing.

### Doorway 4 — Neutral-Atom Logical Qubit Processor

**Representative paper:** Bluvstein, D. et al. (QuEra/Harvard/MIT). "Logical quantum processor based on reconfigurable atom arrays." *Nature* 626, 58–65 (2024). [verify]

**Problem class:** QEC on neutral atoms. Demonstrates that high-rate codes on a neutral-atom platform achieve logical error rates below physical error rates, using transversal fault-tolerant gates.

**Series tools required:** Chapter 9 (stabilizer codes, $[\![n,k,d]\!]$ notation, fault-tolerant gates); Chapter 8 (neutral-atom qubits, Rydberg blockade, optical tweezers); Chapter 2 (entanglement structure of multi-qubit states).

**The core code: $[\![4,2,2]\!]$.** Encodes 2 logical qubits in 4 physical qubits with code distance 2. The logical basis states:

$$|0_L 0_L\rangle = \tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle), \qquad |0_L 1_L\rangle = \tfrac{1}{\sqrt{2}}(|0011\rangle + |1100\rangle),$$
$$|1_L 0_L\rangle = \tfrac{1}{\sqrt{2}}(|0101\rangle + |1010\rangle), \qquad |1_L 1_L\rangle = \tfrac{1}{\sqrt{2}}(|0110\rangle + |1001\rangle).$$

The stabilizers are $XXXX$ and $ZZZZ$.

**Reconstruction target.** We verify that $|0_L 0_L\rangle$ is a $+1$ eigenstate of both stabilizers:

$$XXXX\,\tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle) = \tfrac{1}{\sqrt{2}}(|1111\rangle + |0000\rangle) = |0_L 0_L\rangle. \checkmark$$

$$ZZZZ\,\tfrac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle) = \tfrac{1}{\sqrt{2}}(|0000\rangle + (-1)^4|1111\rangle) = |0_L 0_L\rangle. \checkmark$$

The state is in the code space.

**Honesty layer:** The Bluvstein 2024 result demonstrates 48 logical qubits with logical error rates below physical error rates for specific transversal operations. Neutral atoms offer long-range connectivity via Rydberg excitation that superconducting chips cannot match, enabling codes requiring non-planar connectivity. The trade-off is slower gates and lower inherent fidelity. Neither platform has demonstrated fault-tolerant universal computation at scale.

---

## Worked Example — Reconstructing the CHSH Value

We reconstruct the core result of a loophole-free Bell test.

**Physical setup.** Alice and Bob each hold one photon from an entangled pair in state $|\Phi^+\rangle = (|HH\rangle + |VV\rangle)/\sqrt{2}$, where $H$ encodes $|0\rangle$ and $V$ encodes $|1\rangle$. Alice measures polarization at angle $\theta_a$; Bob at $\theta_b$.

**Step 1.** The correlation function for $|\Phi^+\rangle$: $E(\hat a, \hat b) = \cos(\theta_a - \theta_b)$.

**Step 2.** Optimal angles: $\theta_{A_1} = 0°$, $\theta_{A_2} = 90°$, $\theta_{B_1} = 45°$, $\theta_{B_2} = -45°$.

$$E(A_1,B_1) = \cos(-45°) = +\tfrac{1}{\sqrt{2}}, \quad E(A_1,B_2) = \cos(45°) = +\tfrac{1}{\sqrt{2}},$$
$$E(A_2,B_1) = \cos(45°) = +\tfrac{1}{\sqrt{2}}, \quad E(A_2,B_2) = \cos(135°) = -\tfrac{1}{\sqrt{2}}.$$

**Step 3.** $S = \tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} = \tfrac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.828$.

**Step 4.** The local-realistic bound is $|S| \leq 2$ (derived in Chapter 3). The quantum prediction $S = 2\sqrt{2}$ exceeds this by 0.828 — the gap experiments are designed to resolve.

**Step 5.** Giustina et al. 2015 report $S > 2$ with $p < 3.74\times10^{-31}$. The experimental $S$ falls slightly below $2\sqrt{2}$ due to photon loss, detection inefficiency, and residual decoherence. The ideal calculation gives the upper bound; the gap reflects imperfections characterized in the supplementary material.

**Step 6.** The locality loophole is closed: Alice's and Bob's settings are chosen by a random-number generator within the light-travel time between the stations. The detection loophole is closed by high-efficiency superconducting single-photon detectors.

The entire reconstruction uses only CHSH machinery from Chapter 3, Bell-state definitions from Chapter 2, and first-year linear algebra. We have verified the central quantitative claim of a Nobel-adjacent experiment using tools from this volume.

An extension: we can model the slightly mixed state $\hat\rho = (1-\epsilon)|\Phi^+\rangle\langle\Phi^+| + \epsilon\hat I/4$, compute $S(\epsilon) = (1-\epsilon)\cdot2\sqrt{2}$, and fit $\epsilon$ from the experimental $S$ value. This connects Chapter 1 (density matrix) and Chapter 3 (CHSH) and is a natural next step.

---

## The Rubric

A reconstruction note should demonstrate:

| Category | Weight | What it means |
|----------|--------|---------------|
| System identification | 20% | Physical qubit(s), Hamiltonian, encoding of $\|0\rangle$ and $\|1\rangle$ |
| Observable and measurement | 20% | Which observable, in what basis, what quantum theory predicts |
| Core calculation | 30% | Numbers match the paper within error bars or within factor of 2–3 for estimates |
| Connections to prior chapters | 15% | Each key tool cited by volume and chapter |
| Honest assessment | 15% | One thing the paper does not claim; whether the result is a physical principle, hardware benchmark, or advantage claim |

The rubric is designed so that a student who understands the formalism but has not read the paper carefully can pass the calculation portion (30%) but will lose points on the honest assessment (15%) — which is the harder thing to demonstrate.

---

## Open Questions

**Whether practical quantum advantage arrives, and when.** As of mid-2026: no practically useful quantum advantage has been demonstrated on a real-world problem. The NIST post-quantum cryptography standards (FIPS 203, 204, 205) were finalized in August 2024 — the world's cryptographic infrastructure is already being updated in anticipation of fault-tolerant quantum computers that do not yet exist. If fault-tolerant machines arrive, Shor's algorithm will break RSA. The lattice-based replacements in the NIST standards are believed quantum-resistant, but "believed" is not "proven." The societal consequences are already being implemented; the physical capability remains on a roadmap.

**Whether topological quantum computation will work.** Majorana-based topologically protected qubits have been pursued for two decades — systems whose error protection is enforced by topology rather than active correction, potentially eliminating most overhead. As of 2026, no topological qubit has outperformed a surface-code qubit on a competing platform. The field remains open.

**The measurement problem, still.** We have a complete formalism that predicts the statistics of every experiment in this chapter to extraordinary precision. We have decoherence to explain why outcomes look classical. What we do not have is a derivation from first principles of why one particular outcome obtains in one particular run. Copenhagen asserts it without explanation; many-worlds says all outcomes occur; Bohmian mechanics uses a pilot wave. None adds a prediction the others do not make. The formalism provides tools that work. It does not provide resolved metaphysics. This is not a failure of the tools. It is a frontier.

---

## References

- Giustina, M. et al. "Significant-loophole-free test of Bell's theorem with entangled photons." *Phys. Rev. Lett.* 115, 250401 (2015). [verify]
- Shalm, L.K. et al. "Strong loophole-free test of local realism." *Phys. Rev. Lett.* 115, 250402 (2015). [verify]
- Hensen, B. et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 km." *Nature* 526, 682–686 (2015). [verify]
- Arute, F. et al. (Google Quantum AI). "Quantum supremacy using a programmable superconducting processor." *Nature* 574, 505–510 (2019). [verify] [contested: classical simulation gap narrowed by Pan Zhang et al. 2022]
- Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." *Nature* 638, 920–926 (2025). arXiv:2408.13687. [verify]
- Bluvstein, D. et al. "Logical quantum processor based on reconfigurable atom arrays." *Nature* 626, 58–65 (2024). [verify]
- Balasubramanian, G. et al. "Nanoscale imaging magnetometry with diamond spins under ambient conditions." *Nature* 455, 648–651 (2008). [verify]
- Maze, J.R. et al. "Nanoscale magnetic sensing with an individual electronic spin in diamond." *Nature* 455, 644–647 (2008). [verify]
- Rondin, L. et al. "Magnetometry with nitrogen-vacancy defects in diamond." *Rep. Prog. Phys.* 77, 056503 (2014). [verify]
- Schlosshauer, M. *Decoherence and the Quantum-to-Classical Transition*. Springer (2007).
- Preskill, J. "Quantum computing in the NISQ era and beyond." *Quantum* 2, 79 (2018). [verify]
- NIST FIPS 203, 204, 205. National Institute of Standards and Technology, August 2024. [verify]
- Gottesman, D. "Stabilizer codes and quantum error correction." PhD thesis, Caltech (1997). arXiv:quant-ph/9705052. [verify]

