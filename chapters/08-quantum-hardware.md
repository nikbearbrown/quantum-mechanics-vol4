# Chapter 8 — Quantum Hardware: From Formalism to Physical Qubits
*What is actually hiding behind the abstract notation $|0\rangle$, $|1\rangle$, and $\hat\sigma_z$.*

In 1994, Peter Shor published a polynomial-time algorithm for factoring large integers on a quantum computer. The algorithm existed. The computers did not.

The experimentalists had a different question: what is a qubit, physically? Not in the formalism — a two-dimensional complex Hilbert space with Pauli operators — but as an object you can trap, cool, drive, read, and run a circuit on before it decoheres. For two decades after Shor, the central challenge of quantum computing was not the algorithms but the hardware: coaxial cables at millikelvin temperatures, laser beams aimed at individual ions, diamond crystals with engineered atomic defects, silicon transistors smaller than a virus.

Each research group found a different physical answer. Each answer has a different signature: different coherence times, different gate speeds, different connectivity, different infrastructure requirements. As of mid-2026, no single platform has won the competition. The outcome is not clear.

This chapter maps the landscape. It takes the two-level formalism you have been using since Volume 1 — the Pauli Hamiltonians, Rabi oscillations, Bloch equations, and Lindblad dissipators — and shows what physical object each platform is hiding behind the abstract notation.

---

## The DiVincenzo Criteria

David DiVincenzo (2000) distilled the requirements for a functional qubit into five conditions: [verify: DiVincenzo, Fortschritte der Physik 48:771 (2000)]

**1. A scalable physical system with well-characterized qubits.** You need a physical system that can be extended to many qubits without the control infrastructure growing impossibly. "Well-characterized" means you know the Hamiltonian, the transition frequency, the coherence times, and the coupling to neighbors well enough to model and correct errors.

**2. The ability to initialize qubits to a fiducial state.** Every quantum algorithm begins in a known state, typically $|0\rangle^{\otimes n}$. If you cannot reliably prepare the input, the computation starts wrong.

**3. Long coherence times relative to gate operation times.** The figure of merit is the number of gate operations performable within one coherence time:

$$N_\text{gates} = \frac{T_2}{t_\text{gate}}.$$

For quantum error correction, you need $N_\text{gates} \gg 10^4$ per logical qubit. Current best platforms approach or exceed this, but not uniformly across large arrays.

**4. A universal set of quantum gates.** A single-qubit rotation and one entangling two-qubit gate (CNOT, CZ) together generate any unitary to arbitrary precision (the Solovay-Kitaev theorem). Each platform implements these through different physical mechanisms.

**5. Qubit-specific measurement capability.** Reading out one qubit without disturbing its neighbors — requiring either spatial separation or spectral distinguishability of the readout signal.

The criteria are a rubric, not a checklist. Every current platform satisfies them imperfectly at scale. The question is not "does this platform satisfy the criteria?" but "at what qubit count and fidelity does each criterion begin to fail?"

---

## Coherence Times and the Bloch Equation Connection

From Chapter 6, the Bloch equations for a qubit under energy relaxation ($T_1$) and dephasing ($T_\phi$):

$$\dot{r}_x = -\omega_0 r_y - \frac{r_x}{T_2}, \qquad \dot{r}_y = +\omega_0 r_x - \frac{r_y}{T_2}, \qquad \dot{r}_z = -\frac{r_z - r_z^\text{eq}}{T_1},$$

with the fundamental relation

$$\boxed{\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}.}$$

$T_1$ is the energy relaxation time — how long the excited state $|1\rangle$ survives before emitting energy to the environment. $T_2$ is the coherence time — how long off-diagonal elements of the density matrix survive. Pure dephasing (encoded in $T_\phi$) randomizes the phase between $|0\rangle$ and $|1\rangle$ without exchanging energy; it shortens $T_2$ below the $2T_1$ ceiling. In the limit of no pure dephasing, $T_2 \to 2T_1$ — the natural linewidth limit. Best current superconducting hardware approaches this limit.

A third timescale, $T_2^*$ (free-induction decay time), is shorter than $T_2$ when static frequency inhomogeneity is present — different qubits have slightly different transition frequencies. Spin echo and dynamical decoupling sequences refocus this inhomogeneous contribution, recovering the intrinsic $T_2$.

The gate-operation figure of merit $N_\text{gates} = T_2/t_\text{gate}$ is what matters for fault tolerance. A trapped-ion gate with fidelity 99.99% and $t_\text{gate} = 500\,\mu$s in a system with $T_2 = 10$ s gives $2\times10^4$ gates per coherence cycle. A transmon gate with fidelity 99.5% and $t_\text{gate} = 100$ ns in a system with $T_2 = 100\,\mu$s gives $10^3$ gates per coherence cycle. The ratio is what matters for fault tolerance, not either number individually.

---

## The NISQ Concept

John Preskill coined "Noisy Intermediate-Scale Quantum" (NISQ) in his 2018 essay. The defining characteristics: approximately 50–1000 physical qubits; gate fidelities high enough to run circuits of modest depth; gate fidelities not high enough to support full quantum error correction.

NISQ machines are not broken. They can run circuits that are hard to simulate classically within certain assumptions, demonstrate quantum error detection, and probe quantum many-body physics. The limitation is that they cannot sustain enough error correction for the class of problems — Shor's algorithm on large integers, full quantum chemistry — that originally motivated the field. Whether NISQ devices offer practical advantage over classical computers for any useful problem remains contested. [contested]

As of 2026, the community speaks of "utility-scale" quantum computing and the "megaquop" milestone — $10^6$ high-fidelity gate operations — as the next phase beyond NISQ. Fault-tolerant quantum computing requires per-gate error rates well below $\sim10^{-3}$ (the threshold theorem, Chapter 9) sustained across thousands of physical qubits. Current best devices approach this per-gate threshold but cannot sustain it at scale.

<!-- → [TABLE: summary table of all six platforms — columns: platform, T₁, T₂, two-qubit gate time, two-qubit gate fidelity, physical-qubit scale, cryogenic requirement; rows: superconducting transmon, trapped ion, neutral atom Rydberg, photonic, NV center, semiconductor spin; all numbers marked as "mid-2026 approximate" with a note that they age within 12-24 months] -->

---

## Platform 1: Superconducting Transmons

The transmon is an anharmonic LC oscillator in which the inductor is a Josephson junction — a thin insulating barrier between two superconductors. The nonlinear inductance of the junction makes the energy levels unequally spaced. The transmon Hamiltonian in the charge basis is:

$$\hat{H}_\text{transmon} = 4E_C(\hat{n} - n_g)^2 - E_J\cos\hat\phi,$$

where $E_C$ is the charging energy, $E_J$ the Josephson energy, $\hat{n}$ the Cooper pair number, $n_g$ the gate charge, and $\hat\phi$ the superconducting phase. The operating regime $E_J/E_C \gg 1$ (typically $\sim50$) exponentially suppresses charge noise while maintaining sufficient anharmonicity $\alpha = (E_{12} - E_{01}) \approx -200$ to $-300$ MHz for two-level control.

In this regime, the two lowest levels are well-separated from the rest, and projecting onto that subspace gives the standard two-level Hamiltonian $\hat{H} = (\hbar\omega_0/2)\hat\sigma_z$, with $\omega_0/2\pi \approx 4$–8 GHz.

Single-qubit gates are microwave pulses at $\omega_0$; in the rotating frame these produce Rabi oscillations identical in form to the spin-1/2 Rabi problem of Volume 1. Two-qubit gates (cross-resonance on IBM hardware, parametric coupling on Google hardware) run in 20–500 ns. Readout is dispersive: a probe pulse at the readout resonator reflects with a state-dependent phase. Readout fidelity 97–99%.

Dominant noise sources: two-level system (TLS) defects in substrate and junction interfaces, charge noise, flux noise, quasiparticle poisoning, residual thermal photons.

**Current state (mid-2026).** IBM Heron r2 (156 qubits, July 2024): median two-qubit gate error $\sim0.17\%$. Google Willow (105 qubits, December 2024): demonstrated below-threshold surface code error correction, the first time a quantum error-correcting code improved with code distance (*Nature* 2025, Acharya et al.). [verify] Best research transmons: $T_1$ approaching 1.68 ms. Single-qubit gate fidelity $>99.9\%$; two-qubit gate fidelity 99.0–99.7%.

Infrastructure: dilution refrigerators at 10–20 mK.

---

## Platform 2: Trapped Ions

Individual atomic ions — typically $^{40}$Ca$^+$ or $^{171}$Yb$^+$ — are confined in Paul traps by oscillating electric fields. Two qubit encodings are used. Hyperfine qubits encode in two ground-state hyperfine levels connected by a microwave transition (e.g., $\nu \approx 12.6$ GHz for $^{171}$Yb$^+$); coherence times in seconds to minutes. Optical qubits encode in the ground state and a metastable excited state connected by a narrow optical transition; coherence times limited by the metastable lifetime and laser linewidth.

Single-qubit gates via laser or microwave pulses: fidelities routinely $>99.99\%$. Two-qubit gates via the Mølmer-Sørensen scheme: a bichromatic laser field drives the shared collective motional mode of the ion crystal, mediating an effective $\hat\sigma_x^{(1)}\hat\sigma_x^{(2)}$ coupling — all ions in a trap interact through their common oscillation, giving all-to-all connectivity without routing. Gate time: 10–1000 µs.

Readout via state-dependent fluorescence: one state scatters photons (bright), the other does not (dark). Readout fidelity $>99.9\%$.

**Current state (mid-2026).** Quantinuum Helios (November 2025): 98 barium-ion qubits, two-qubit gate fidelity 99.921% across all pairs. Oxford Ionics (2025): two-qubit fidelity exceeding 99.99% — the highest published gate fidelity on any platform — without requiring motional ground-state cooling. [verify] Coherence times: seconds to minutes, orders of magnitude longer than superconducting.

Infrastructure: ultra-high vacuum ($\sim10^{-11}$ torr); laser systems; room-temperature trap electrodes with laser cooling.

---

## Platform 3: Neutral Atoms in Optical Tweezers

Neutral atoms — $^{87}$Rb, $^{133}$Cs, $^{171}$Yb, or $^{87}$Sr — trapped in tightly focused laser beams (tweezers, $\sim1\,\mu$m waist). Arrays generated by spatial light modulators or acousto-optic deflectors give arbitrary programmable geometries with hundreds to thousands of atoms. Qubits encoded in two hyperfine ground states.

Entangling gates via Rydberg blockade: two atoms are excited to high principal quantum number states ($n \sim 50$–100) that have huge electric dipole moments. If one atom is in the Rydberg state, a second nearby atom cannot also be excited (the interaction energy shifts the double-excitation off resonance). This conditional excitation implements a CZ gate in $\sim0.1$–$1\,\mu$s. Crucially, atoms can be physically moved between gate operations, giving reconfigurable connectivity.

**Current state (mid-2026).** QuEra/Harvard (*Nature* 626:58, 2024, Bluvstein et al.): 48 logical qubits from a 280-atom array — the first demonstration of fault-tolerant gates on many logical qubits simultaneously. [verify] QuEra (January 2026, *Nature*): 96 logical qubits from a 448-atom array using high-rate codes — the current logical-qubit count record. [verify] Atom Computing Phoenix: 1,180 physical-qubit array in production. Two-qubit Rydberg gate fidelity $\sim99.5\%$ in best demonstrations.

Infrastructure: ultra-high vacuum; laser cooling (atoms at µK via lasers alone, no dilution fridge).

---

## Platform 4: Photonic Qubits

Photonic qubits encode information in photons: polarization ($|H\rangle$/$|V\rangle$), path, time-bin, or photon number. Two-qubit entangling gates in linear optics are probabilistic — a CZ gate succeeds with some probability and fails with a heralded signal (KLM scheme, Knill-Laflamme-Milburn 2001). Practical scalable photonic quantum computing therefore requires massive resource overhead to drive failure probability to negligible levels. Fusion-based approaches (PsiQuantum) build fault-tolerant computation from probabilistic Bell measurements and photonic cluster states.

Advantages: room-temperature operation; long coherence (photons interact weakly with environment); natural for quantum networking. Disadvantages: deterministic two-qubit gates require large resource overhead; photon loss is irreversible; photon-number-resolving detectors are demanding.

**Current state (mid-2026).** Xanadu Borealis (2022): quantum advantage demonstration in Gaussian boson sampling — a task tailored to the architecture; classical simulation hardness is contested. [contested] No photonic platform has demonstrated general-purpose gate-based quantum computing at useful scale. PsiQuantum is pursuing million-qubit silicon photonic fabrication; not demonstrated at scale as of 2026.

---

## Platform 5: NV Centers in Diamond

A nitrogen-vacancy (NV) center is a point defect: a substitutional nitrogen adjacent to a lattice vacancy. The NV$^-$ charge state has a spin-1 ground state with a zero-field splitting $D \approx 2.87$ GHz between $m_s = 0$ and $m_s = \pm1$ sublevels. An applied magnetic field $B$ further splits $m_s = \pm1$ by the Zeeman effect. The qubit is encoded in the $\{|m_s = 0\rangle, |m_s = -1\rangle\}$ subspace.

The Hamiltonian in the spin-1 basis is $\hat{H}_\text{NV} = hD\hat{S}_z^2 + g_e\mu_B B\hat{S}_z$. In the two-level subspace, the $|m_s = 0\rangle \leftrightarrow |m_s = -1\rangle$ transition frequency is:

$$\nu_{0,-1} \approx 2870\,\text{MHz} - 28B\,[\text{MHz/mT}],$$

and the effective Hamiltonian reduces to $\hat{H}^{(2)} = (h\nu_{0,-1}/2)\hat\sigma_z$ — the same two-level form as every other platform.

Gates via microwave pulses at $\nu_{0,-1}$; Rabi oscillations identical in form to the transmon case. Readout via spin-dependent fluorescence under 532 nm illumination (ODMR). Single-shot readout contrast $\sim10$–30%, improvable by spin-to-charge conversion.

**Key advantage.** Room-temperature operation; no cryostat. NV centers currently lead in quantum sensing (magnetometry at nT/$\sqrt{\text{Hz}}$ sensitivity, nanoscale MRI) and quantum networking (entanglement over 1.3 km via photon-mediated links, the 2015 Hensen et al. loophole-free Bell test). Two-qubit gate fidelity in research: $\sim80$–95% — significantly below other platforms. Quantum Brilliance is developing chip-scale room-temperature NV processors; 2-qubit lab devices as of 2025.

**Current state (mid-2026).** $T_1 \sim 1$–6 ms, $T_2 \sim 100\,\mu$s–2 ms with dynamical decoupling. Single-qubit fidelity $\sim99\%$.

---

## Platform 6: Semiconductor Spin Qubits

Single electron spins confined in gate-defined quantum dots in silicon (Si) or silicon-germanium (Si/SiGe) heterostructures. In an applied magnetic field, spin-up $|\uparrow\rangle$ and spin-down $|\downarrow\rangle$ become $|0\rangle$ and $|1\rangle$, split by the Zeeman energy. The effective Hamiltonian is $\hat{H} = (\hbar\omega_0/2)\hat\sigma_z$ — the standard two-level form, again.

Single-qubit gates via AC electric field pulses through the dot gates, exploiting spin-orbit coupling. Two-qubit gates via exchange interaction: placing two dots close enough that electrons can tunnel between them creates a Heisenberg coupling $J\hat{\mathbf{S}}_1\cdot\hat{\mathbf{S}}_2$ proportional to the tunneling rate. Gate time: 1–100 ns — comparable to superconducting and much faster than ions.

**Key advantage.** Silicon quantum dots are fabricated using CMOS processes compatible with existing semiconductor manufacturing infrastructure. Intel and other manufacturers are pursuing scaling via 300 mm production wafers.

**Current state (mid-2026).** Intel (*Nature*, May 2024): 99.9% single-qubit fidelity on qubits from a 300 mm production line. 12-spin-qubit arrays from production semiconductor manufacturing (*Nano Letters* 2025). [verify] Two-qubit gate fidelities $>99\%$ in research settings; below fault-tolerance threshold in larger current arrays. Dominant challenge: qubit-to-qubit frequency variability and charge noise across large arrays.

Infrastructure: dilution refrigerators at $\sim50$–100 mK; device fabrication via semiconductor industry supply chain.

---

## Worked Example: Two Physical Hamiltonians to the Same Two-Level Form

### The transmon

The full transmon Hamiltonian looks nothing like a two-level system. We show that in the $E_J/E_C \gg 1$ regime, the two-level approximation is self-consistent.

Expand $\cos\hat\phi \approx 1 - \hat\phi^2/2 + \hat\phi^4/24$: the leading terms give a harmonic oscillator at plasma frequency $\omega_p = \sqrt{8E_JE_C}/\hbar$. The $\hat\phi^4$ term shifts the levels from the harmonic ladder by the anharmonicity:

$$\alpha/2\pi \approx -E_C/h \approx -300\,\text{MHz.}$$

The $|0\rangle\to|1\rangle$ transition frequency is $\omega_{01} = \omega_p - E_C/\hbar$. For $E_J/2\pi\hbar \approx 20$ GHz and $E_C/2\pi\hbar \approx 300$ MHz: $\omega_p/2\pi \approx \sqrt{8\times20\times0.3}$ GHz $\approx 6.9$ GHz, and $\omega_{01}/2\pi \approx 6.6$ GHz.

The anharmonicity $|\alpha|/2\pi \approx 300$ MHz means the $|1\rangle\to|2\rangle$ transition is 300 MHz detuned from $|0\rangle\to|1\rangle$. As long as the drive bandwidth is $\ll 300$ MHz, only the two lowest levels are addressed. Projecting onto this subspace:

$$\hat{H}_\text{eff} = \frac{\hbar\omega_{01}}{2}\hat\sigma_z.$$

Adding a resonant microwave drive $\hbar\Omega\cos(\omega_{01}t)\hat\sigma_x$ and applying the rotating-wave approximation (valid when $\Omega \ll \omega_{01}$):

$$\hat{H}_\text{rot} = \frac{\hbar\Omega}{2}\hat\sigma_x.$$

This generates Bloch sphere rotations at rate $\Omega$ about the $x$-axis — identical to the spin-1/2 result from Volume 1. The formalism is the same; only the physical realization differs.

### The NV center

The spin-1 NV Hamiltonian with static field $B$ along $z$ has eigenvalues $E_0 = 0$, $E_{\pm1} = hD \pm g_e\mu_B B$. The $|m_s=0\rangle\leftrightarrow|m_s=-1\rangle$ transition frequency is $\nu_{0,-1} = D - g_e\mu_B B/h$.

Restricting to $|0\rangle \equiv |m_s=0\rangle$ and $|1\rangle \equiv |m_s=-1\rangle$:

$$\hat{H}_\text{NV}^{(2)} = \frac{h\nu_{0,-1}}{2}\hat\sigma_z.$$

The two-level approximation is valid as long as the microwave drive does not also excite $|m_s = +1\rangle$, which is detuned by $2g_e\mu_B B/h = 56B$ [MHz/mT]. At $B = 10$ mT, the detuning is 560 MHz — large compared to typical Rabi frequencies of 1–10 MHz. The two-level picture holds.

A microwave field oscillating at $\nu_{0,-1}$ applies the same Rabi Hamiltonian as the transmon case. Readout replaces dispersive detection with optical fluorescence, but the underlying two-level dynamics are formally identical.

**The limit of the NV two-level picture.** It breaks down when the drive frequency approaches $2g_e\mu_B B/h$ (coupling to $m_s = +1$), or when the hyperfine coupling to the $^{14}$N nuclear spin ($A \approx -2.16$ MHz) is not resolved by the measurement. At high microwave power ($\Omega_R \gtrsim A$), the three-level structure must be treated explicitly.

**The lesson.** Six radically different physical systems — superconducting circuits, trapped atomic ions, neutral atoms, photons, diamond defects, silicon quantum dots — all reduce to the same Hamiltonian $(\hbar\omega_0/2)\hat\sigma_z$ in their two-level operating subspace. Every gate operation in every platform is an SU(2) rotation on the Bloch sphere. The physics is different; the formalism is identical. The two-level model is not an approximation imposed by the formalism — it is a physical fact about the structure of matter that each platform exploits.

<!-- → [FIGURE: side-by-side comparison of the NV center and transmon energy level diagrams — showing the full spin-1 NV spectrum (D splitting and Zeeman splitting) and the full transmon harmonic plus anharmonic spectrum; in both cases, arrows highlight the two-level subspace {|0⟩, |1⟩}; the visual goal is to show that despite completely different physical origins, both reduce to the same two-level structure with the same notation] -->

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the DiVincenzo criteria.*
   List the five DiVincenzo criteria. For each criterion, give one specific physical challenge that a superconducting transmon qubit faces in satisfying it at scale (e.g., for criterion 3, identify the dominant noise source that limits $T_2$).
   *Tests: recall of the five criteria and their physical instantiation for a specific platform.*

2. *Difficulty: Warm-up — tests the Bloch equation coherence time relation.*
   A qubit has $T_1 = 1$ ms and $T_\phi = 500\,\mu$s. (a) Compute $T_2$. (b) A second qubit has $T_1 = 1$ ms and no pure dephasing ($T_\phi \to \infty$); what is its $T_2$? (c) A third qubit has $T_2 = 2T_1$; what does this imply about $T_\phi$? (d) For the first qubit with two-qubit gate time 200 ns, how many gates can be run per coherence cycle?
   *Tests: applying the fundamental $T_2$ relation; the $2T_1$ ceiling; gates-per-coherence-cycle figure of merit.*

3. *Difficulty: Warm-up — tests NV center transition frequency and two-level validity.*
   The NV center qubit transition frequency is $\nu_{0,-1} \approx 2870 - 28B$ MHz, $B$ in mT. (a) At what field does $\nu_{0,-1}$ cross 2.4 GHz? (b) At $B = 100$ mT, what is the detuning between the $|0\rangle\leftrightarrow|1\rangle$ and $|0\rangle\leftrightarrow|m_s=+1\rangle$ transitions? (c) For Rabi frequency $\Omega_R/2\pi = 5$ MHz, is the two-level approximation valid at this field?
   *Tests: the NV transition frequency formula; two-level validity as a function of field.*

**Application**

4. *Difficulty: Application — transmon anharmonicity and pulse bandwidth.*
   The transmon anharmonicity is $\alpha/2\pi \approx -300$ MHz. A microwave $\pi$-pulse of duration $t_\pi = \pi/\Omega_R$ implements population inversion. (a) For $\Omega_R/2\pi = 50$ MHz, compute $t_\pi$. (b) The Fourier-limited bandwidth of a rectangular pulse of duration $t_\pi$ is $\Delta\nu \sim 1/t_\pi$. Compare $\Delta\nu$ to $|\alpha|/2\pi = 300$ MHz and assess whether the two-level approximation holds. (c) Briefly describe what goes wrong if $\Delta\nu \gtrsim |\alpha|/2\pi$ — which levels are affected and what error results?
   *Tests: connecting pulse duration to bandwidth; bandwidth vs. anharmonicity as a two-level validity condition.*

5. *Difficulty: Application — platform figures of merit.*
   Using the mid-2026 values given in the platform descriptions: (a) compute $N_\text{gates} = T_2/t_\text{gate}$ for superconducting (transmon with $T_2 = 400\,\mu$s, $t_\text{gate} = 100$ ns) and trapped ion ($T_2 = 10$ s, $t_\text{gate} = 500\,\mu$s); (b) which platform has more usable gates per coherence cycle, and by how much? (c) The "megaquop" milestone requires $10^6$ high-fidelity operations. Which platform's coherence-cycle gate count is closer to this target, and what would be needed to reach it on the other platform?
   *Tests: computing and comparing the $T_2/t_\text{gate}$ figure of merit across platforms; connecting to the megaquop milestone.*

6. *Difficulty: Application — coherence time measurement.*
   A Ramsey experiment on a superconducting qubit measures the free precession decay of the off-diagonal density matrix element. The experiment applies $\pi/2$-pulse, waits time $\tau$, applies another $\pi/2$-pulse, and measures $P(|1\rangle)$ as a function of $\tau$. (a) Sketch the expected $P(|1\rangle)$ vs. $\tau$ for a qubit with $T_2^* = 10\,\mu$s (showing a decaying oscillation). (b) A spin-echo sequence (Ramsey with a $\pi$-pulse in the middle) gives a decay time $T_2 = 100\,\mu$s on the same qubit. What physical noise source does the spin echo refocus? (c) Why is $T_2 > T_2^*$, and what does the ratio $T_2/T_2^*$ tell you about the noise spectrum?
   *Tests: Ramsey vs. spin echo; $T_2^*$ vs. $T_2$; static vs. dynamic noise.*

**Synthesis**

7. *Difficulty: Synthesis — platform selection for a specified task.*
   An application requires 100 fully connected qubits, two-qubit gate fidelity $>99.5\%$, and the ability to run 1000 two-qubit gates in a single circuit before decoherence. Assess the three leading gate-based platforms (superconducting, trapped ion, neutral atom) against each requirement. State which platform currently best meets the requirements and which requirement is hardest to satisfy on each platform. Note that these numbers change rapidly. [verify]
   *Tests: applying the DiVincenzo rubric and the $N_\text{gates}$ criterion to a realistic specification; recognizing trade-offs.*

8. *Difficulty: Synthesis — NISQ structural analysis.*
   The NISQ concept is often described as "not enough qubits" or "not enough fidelity." Argue that it is better described as "not enough $N_\text{gates}$ per logical qubit to support error correction," using the threshold theorem (Chapter 9). (a) For a surface code with physical error rate $p = 0.5\%$ (just below threshold), how many physical qubits are needed per logical qubit at code distance $d = 7$? (b) For a 1000-qubit NISQ device with this error rate, how many logical qubits could it support? (c) What would need to change — error rate, qubit count, or both — for the device to be "post-NISQ"?
   *Tests: connecting NISQ to the threshold theorem; logical vs. physical qubit count; structural vs. quantitative understanding of NISQ.*

**Challenge**

9. *Difficulty: Challenge — all six platforms on the DiVincenzo rubric, quantitatively.*
   For each of the six platforms, compute (or estimate) the single most diagnostic figure of merit for each DiVincenzo criterion. Specifically: criterion 1 (scalability) → physical qubit count in largest 2026 demonstration; criterion 2 (initialization) → state preparation and measurement (SPAM) fidelity; criterion 3 (coherence vs. gates) → $N_\text{gates} = T_2/t_\text{gate,2Q}$; criterion 4 (universal gates) → two-qubit gate fidelity; criterion 5 (measurement) → single-shot readout fidelity. Present as a $6\times5$ table. Identify the platform with the best and worst value for each criterion, and identify which platform has the most balanced profile across all five. Note that some entries require estimation or citing recent literature. [verify]
   *Tests: synthesizing across all six platforms and all five criteria into a structured quantitative comparison; identifying the trade-off structure of the hardware landscape.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to generate hardware data (which changes rapidly), but to probe reasoning and physical understanding.

1. Ask an LLM to derive the transmon two-level Hamiltonian from the full Josephson junction Hamiltonian, following the steps in the worked example. Check: does it correctly identify the plasma frequency $\omega_p = \sqrt{8E_JE_C}/\hbar$, the anharmonicity $\alpha \approx -E_C/\hbar$, and the two-level projection? Ask it to state the condition under which the two-level approximation breaks down.

2. Ask an LLM to compare the Mølmer-Sørensen gate (trapped ions) and the Rydberg blockade gate (neutral atoms) as implementations of the two-qubit entangling gate. Both should produce a maximally entangled state from two product qubits. Ask it to identify the physical interaction responsible in each case, the typical gate time and fidelity, and what would be required to run 100 such gates in sequence.

3. Ask an LLM what "loophole-free Bell test" means in the context of the Hensen et al. 2015 experiment, and why earlier Bell tests had loopholes that allowed local hidden-variable theories to be compatible with the data. Ask it to identify the two main loopholes (locality and detection efficiency) and how each was closed in the Hensen experiment.

4. Ask an LLM to explain what the threshold theorem says about quantum error correction, and why the NISQ concept is defined in terms of not being above the error-correction threshold rather than in terms of a qubit count. Ask it to estimate the per-gate error rate of a current superconducting platform and assess how far it is from the fault-tolerance threshold for the surface code.

5. Ask an LLM to describe Microsoft's topological qubit approach using Majorana zero modes, including what physical system hosts them, what theoretical advantage they would provide, and what the current experimental status is as of 2026. Ask it to flag any claims as "demonstrated" vs. "theoretical" vs. "disputed." Evaluate whether it correctly identifies the current state of the field.

---

## References

DiVincenzo, D. P. (2000). The physical implementation of quantum computation. *Fortschritte der Physik*, 48, 771.

Preskill, J. (2018). Quantum computing in the NISQ era and beyond. *Quantum*, 2, 79.

Koch, J. et al. (2007). Charge-insensitive qubit design derived from the Cooper pair box. *Physical Review A*, 76, 042319.

Doherty, M. W. et al. (2013). The nitrogen-vacancy colour centre in diamond. *Physics Reports*, 528, 1.

Bluvstein, D. et al. (QuEra/Harvard/MIT) (2024). Logical quantum processor based on reconfigurable atom arrays. *Nature*, 626, 58.

Acharya, R. et al. (Google Quantum AI) (2025). Quantum error correction below the surface code threshold. *Nature*, 638, 920.

Hensen, B. et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature*, 526, 682.

Krantz, P. et al. (2019). A quantum engineer's guide to superconducting qubits. *Applied Physics Reviews*, 6, 021318.

Bruzewicz, C. D. et al. (2019). Trapped-ion quantum computing: Progress and challenges. *Applied Physics Reviews*, 6, 021314.

Knill, E., Laflamme, R., & Milburn, G. J. (2001). A scheme for efficient quantum computation with linear optics. *Nature*, 409, 46.
