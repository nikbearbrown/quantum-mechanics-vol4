# Worked Exercises: Quantum Hardware — From Formalism to Physical Qubits
*Chapter 8 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The Bloch-equation coherence relation $\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$ and the $2T_1$ ceiling (Chapter 6, recalled in Chapter 8).
- The two-level reduction of a physical Hamiltonian to $\hat H_\text{eff} = (\hbar\omega_0/2)\hat\sigma_z$, and the gates-per-coherence figure of merit $N_\text{gates} = T_2/t_\text{gate}$.
- The transmon anharmonicity $\alpha/2\pi \approx -300$ MHz and the bandwidth-vs-anharmonicity condition for two-level validity.

---

## Part A — Full Worked Example

**What this demonstrates:** How to convert a transmon's coherence times and gate speed into the fault-tolerance figure of merit $N_\text{gates}$, while correctly applying the $T_2 \le 2T_1$ ceiling.

**The problem:** A superconducting transmon is measured with $T_1 = 180\,\mu$s and pure-dephasing time $T_\phi = 240\,\mu$s. Its two-qubit gate time is $t_\text{gate} = 90$ ns. (a) Compute $T_2$. (b) Compute $N_\text{gates} = T_2/t_\text{gate}$. (c) The team reports a process upgrade that removes essentially all pure dephasing. What is the best $T_2$ they could now hope for, and what does $N_\text{gates}$ become? (d) Does this device reach the $N_\text{gates} \gg 10^4$ target the chapter sets for quantum error correction?

**The solution:**

**Step 1 — Combine relaxation and dephasing into $T_2$.** Apply the boxed Bloch relation:
$$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi} = \frac{1}{2(180)} + \frac{1}{240} = \frac{1}{360} + \frac{1}{240}\;\mu\text{s}^{-1}.$$
A common denominator of 720 gives $\frac{2}{720} + \frac{3}{720} = \frac{5}{720}$, so $T_2 = 144\,\mu$s.
*Why:* $T_2$ is not just relaxation — it is degraded by both energy loss (the $2T_1$ term) and pure phase randomization ($T_\phi$). Both off-diagonal-killing processes add as rates.
*Check:* $T_2 = 144\,\mu$s sits below both $2T_1 = 360\,\mu$s and $T_\phi = 240\,\mu$s, as it must — adding rates always lowers the resulting time.

**Step 2 — Form the gate figure of merit.** With $t_\text{gate} = 90$ ns $= 0.090\,\mu$s:
$$N_\text{gates} = \frac{T_2}{t_\text{gate}} = \frac{144\,\mu\text{s}}{0.090\,\mu\text{s}} \approx 1.6\times10^3.$$
*Why:* This is the chapter's DiVincenzo criterion 3 made quantitative — how many operations fit inside one coherence window.
*Check:* $144/0.09$: dividing by $0.09$ is multiplying by $\approx 11.1$, and $144 \times 11.1 \approx 1600$. Order of magnitude $10^3$, consistent with the chapter's transmon example ($\sim10^3$ gates per cycle).

**Step 3 — Apply the $2T_1$ ceiling after removing dephasing.** With $T_\phi \to \infty$, the dephasing rate vanishes:
$$\frac{1}{T_2} = \frac{1}{2T_1} + 0 \;\Rightarrow\; T_2 = 2T_1 = 360\,\mu\text{s}.$$
*Why:* The chapter states that in the no-pure-dephasing limit, $T_2 \to 2T_1$ — the natural-linewidth limit. You cannot do better than this; relaxation alone still destroys coherence.
*Check:* $360\,\mu$s is exactly twice $T_1 = 180\,\mu$s, and it exceeds the original $144\,\mu$s — removing a decoherence channel can only lengthen $T_2$.

**Step 4 — Recompute $N_\text{gates}$ at the ceiling.**
$$N_\text{gates} = \frac{360\,\mu\text{s}}{0.090\,\mu\text{s}} = 4.0\times10^3.$$
*Why:* The same gate speed now runs for $2.5\times$ longer, so the gate budget scales by the same factor ($144 \to 360$ is $\times 2.5$, and $1600 \times 2.5 = 4000$).
*Check:* $360/0.09 = 4000$ exactly. Consistent with the $\times2.5$ improvement in $T_2$.

**Step 5 — Compare to the QEC requirement.** The chapter requires $N_\text{gates} \gg 10^4$ per logical qubit for error correction. Even at the $2T_1$ ceiling, $4\times10^3 < 10^4$.
*Why:* Coherence improvement alone is not enough; the gap to fault tolerance is structural, not a single tuning knob.
*Check:* $4\times10^3$ is below $10^4$ by a factor of $2.5$, so the device falls short even in the ideal dephasing-free limit.

**Final answer:** (a) $T_2 = 144\,\mu$s. (b) $N_\text{gates} \approx 1.6\times10^3$. (c) Best possible $T_2 = 2T_1 = 360\,\mu$s, giving $N_\text{gates} = 4.0\times10^3$. (d) No — even at the $2T_1$ ceiling it sits below the $\gg10^4$ QEC target.

**What made this work:** The whole calculation hinges on treating decoherence as a sum of *rates*, not times, so that $T_2$ is always shorter than every contributing timescale and is hard-capped at $2T_1$. Once $T_2$ is correct, the figure of merit $N_\text{gates}$ is a single division, and comparing it to the chapter's $\gg10^4$ benchmark turns raw lab numbers into a fault-tolerance verdict. The key discipline is keeping units consistent ($\mu$s throughout) and respecting the physical ceiling rather than letting an algebra slip push $T_2$ above $2T_1$.

**Self-explanation prompt:** In your own words, why can removing pure dephasing never push $T_2$ above $2T_1$, and what physical process still limits coherence in that ideal limit?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same $T_2$-and-$N_\text{gates}$ reasoning for a trapped-ion qubit, where the numbers live in a different order of magnitude.

**The problem:** A trapped-ion hyperfine qubit has $T_1$ effectively unbounded (hyperfine ground states do not relax on experimental timescales) but a measured coherence time set by magnetic-field noise of $T_2 = 8$ s. Its Mølmer–Sørensen two-qubit gate runs in $t_\text{gate} = 400\,\mu$s. (a) Compute $N_\text{gates} = T_2/t_\text{gate}$. (b) A second trap reduces magnetic noise so that $T_2$ doubles; what is the new $N_\text{gates}$? (c) Does either configuration reach the chapter's $N_\text{gates} \gg 10^4$ QEC target? (d) The chapter's "megaquop" milestone is $10^6$ operations. By what factor would $T_2$ (at fixed gate time) need to grow to put a single coherence cycle within reach of one megaquop?

**Stuck?** Keep every time in the same unit before dividing — convert seconds to microseconds, or gate time to seconds, but do not mix. Remember that for these hyperfine ions the $1/(2T_1)$ term is negligible, so the measured $T_2$ is essentially set by $T_\phi$ alone.

*Instructor note: full solution intentionally omitted. Students should produce the worked steps themselves following the Part A structure.*

---

## Part C — Completion Problem

**What this demonstrates:** Validity of the transmon two-level approximation by comparing a $\pi$-pulse's Fourier bandwidth to the anharmonicity.

**The problem:** A transmon has anharmonicity $\alpha/2\pi \approx -300$ MHz. A single-qubit $\pi$-pulse uses Rabi frequency $\Omega_R/2\pi = 60$ MHz. (a) Find the $\pi$-pulse duration. (b) Estimate its Fourier-limited bandwidth $\Delta\nu \sim 1/t_\pi$. (c) Compare $\Delta\nu$ to $|\alpha|/2\pi$ and decide whether the two-level approximation holds. (d) State what error appears if the bandwidth approaches the anharmonicity.

**Step 1 — Relate pulse duration to Rabi frequency.** A $\pi$-pulse satisfies $\Omega_R t_\pi = \pi$, so $t_\pi = \pi/\Omega_R$. With $\Omega_R = 2\pi \times 60$ MHz:
$$t_\pi = \frac{\pi}{2\pi \times 60\,\text{MHz}} = \frac{1}{2 \times 60\,\text{MHz}} = \frac{1}{120\,\text{MHz}} \approx 8.3\,\text{ns}.$$
*Why:* A $\pi$-pulse inverts the population, which is a half Rabi cycle; the angle accumulated is $\Omega_R t$.

**Step 2 — Estimate the spectral bandwidth.** A rectangular pulse of duration $t_\pi$ has Fourier-limited bandwidth
$$\Delta\nu \sim \frac{1}{t_\pi} = \frac{1}{8.3\,\text{ns}} \approx 120\,\text{MHz}.$$
*Why:* A shorter pulse occupies more frequency space; the time–bandwidth product is order unity.

**Step 3 — Compare bandwidth to anharmonicity, and decide validity.**

*Your work here:*

*Why (your explanation):*

**Step 4 — State the failure mode if the bandwidth grew toward $|\alpha|$.**

*Your work here:*

*Why (your explanation):*

**Step 5 — Conclusion.** With $\Delta\nu \approx 120$ MHz comfortably below $|\alpha|/2\pi = 300$ MHz, the drive spectrum does not overlap the $|1\rangle\to|2\rangle$ transition, so addressing the third level is suppressed and the two-level picture holds for this pulse.

**Final answer:** (a) $t_\pi \approx 8.3$ ns. (b) $\Delta\nu \approx 120$ MHz. (c) Since $120$ MHz $< 300$ MHz, the two-level approximation holds (with finite margin). (d) If $\Delta\nu \gtrsim |\alpha|/2\pi$, the pulse spectrally overlaps the $|1\rangle\to|2\rangle$ transition and drives leakage out of the computational subspace into $|2\rangle$.

**Self-explanation prompt:** Explain why making a gate *faster* (larger $\Omega_R$, shorter $t_\pi$) eventually breaks the two-level approximation, and what this implies about the trade-off between gate speed and leakage.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student characterizes a transmon and reports the following.

**Step 1 — Measured values.** $T_1 = 100\,\mu$s, $T_\phi = 100\,\mu$s, gate time $t_\text{gate} = 50$ ns. Goal: compute $T_2$ and $N_\text{gates}$.

**Step 2 — Set up the coherence relation.** "I'll use $\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$."

**Step 3 — ⚠ Compute $T_2$.** "Since $T_1 = T_\phi = 100\,\mu$s, I'll just add the times directly: $T_2 = 2T_1 + T_\phi = 200 + 100 = 300\,\mu$s. That's the coherence time. Then $N_\text{gates} = 300\,\mu\text{s} / 50\,\text{ns} = 6\times10^3$."

**Step 4 — Report.** "$T_2 = 300\,\mu$s, comfortably above the $2T_1 = 200\,\mu$s value, with $6\times10^3$ gates per cycle."

**Your tasks:**
1. Identify the error in Step 3.
2. Explain why it is wrong using the structure of the Bloch coherence relation.
3. Compute the correct $T_2$ and $N_\text{gates}$.
4. State the physical sanity check that would have caught the mistake immediately.

**Why this error is common:** Students transfer the classical intuition that "combining timescales means adding them," but the relation adds *rates*, so $T_2$ must come out *shorter* than every contributing time and can never exceed the $2T_1$ ceiling.

---

## Part E — Transfer Problem

**What this demonstrates:** The same coherence-and-validity reasoning applied to an NV center in diamond — a different physical system with the same two-level formalism.

**The problem:** An NV-center qubit operates at axial field $B = 20$ mT. Its transition frequency is $\nu_{0,-1} \approx 2870 - 28B$ MHz. (a) Compute $\nu_{0,-1}$ at this field. (b) The detuning to the unwanted $|m_s=0\rangle\to|m_s=+1\rangle$ transition is $2g_e\mu_B B/h = 56B$ MHz/mT. Compute it. (c) For a microwave drive with Rabi frequency $\Omega_R/2\pi = 8$ MHz, is the two-level approximation valid here? (d) The NV has $T_1 = 4$ ms and, with dynamical decoupling, $T_2 = 1.2$ ms. Compute $N_\text{gates}$ for a microwave single-qubit gate of duration $t_\text{gate} = 60$ ns, and compare to the transmon you analyzed in Part A.

**Hint (use only if stuck after 10 minutes):** For (c), compare the drive's Rabi frequency (which sets how far the drive "spreads" in frequency) to the $56B$ detuning to $m_s=+1$; if the detuning is hundreds of MHz and $\Omega_R$ is a few MHz, the off-resonant level is safely unaddressed. For (d), keep everything in the same time unit before dividing.

**Reflection prompt:**
1. The NV's $T_2$ is roughly $10\times$ longer than the transmon's, yet its gate is faster than an ion's — what does this do to its $N_\text{gates}$ relative to both, and why does the chapter still place NV two-qubit fidelity below the other platforms?
2. The two-level validity condition for the transmon was "bandwidth $\ll$ anharmonicity"; for the NV it was "Rabi frequency $\ll$ Zeeman detuning to $m_s=+1$." What is the common structural pattern across both platforms?

---

## Part F — Interleaved Review

**F1 — This chapter.** A neutral-atom qubit array runs a Rydberg-blockade CZ gate in $t_\text{gate} = 0.5\,\mu$s and has a hyperfine coherence time $T_2 = 1.5$ s. (a) Compute $N_\text{gates}$. (b) The chapter's QEC requirement is $N_\text{gates} \gg 10^4$; does this platform meet it on coherence grounds alone? (c) Name one DiVincenzo criterion this calculation does *not* address, and why a high $N_\text{gates}$ is therefore necessary but not sufficient.
*Chapter this draws from: 8*

**F2 — Earlier material: the Bloch equations and decoherence channels.** The chapter recalls from *Chapter 6 (the Lindblad master equation and Bloch dynamics)* that $T_1$ comes from amplitude damping (energy emission) and $T_\phi$ from pure dephasing. (a) For a qubit with $T_1 = 50\,\mu$s and measured $T_2 = 80\,\mu$s, solve the boxed relation for $T_\phi$. (b) Is $T_\phi$ longer or shorter than $T_1$ here, and what does that say about which decoherence channel dominates?
*Chapter this draws from: Chapter 6, the Lindblad/Bloch decoherence model*

**F3 — Discrimination.** You are given two lab reports. Report X: "We measured $T_1 = 200\,\mu$s and $T_2^* = 12\,\mu$s; spin echo recovered $T_2 = 150\,\mu$s." Report Y: "We measured $T_1 = 200\,\mu$s, $T_2 = 410\,\mu$s." Which report contains a result that is physically impossible, and which describes the expected ordering $T_2^* \le T_2 \le 2T_1$? Explain the diagnosis for each.
*Note to instructor: this tests whether students can distinguish a legitimate $T_2^* < T_2 < 2T_1$ hierarchy (refocusable inhomogeneous dephasing) from a $T_2 > 2T_1$ violation of the ceiling — the discrimination is the point.*

**Closing reflection:** Across F1–F3, every result reduced to the same two ideas: rates add (so $T_2$ is bounded by $2T_1$), and a coherence time only matters relative to a gate time. State, in one sentence, why these two ideas let you compare six physically unrelated platforms on a single axis.

---

## Instructor Notes

**Common errors:**
- Adding coherence *times* instead of *rates*, producing a $T_2$ that exceeds $2T_1$ (Part D's misconception).
- Order-of-magnitude/unit slips: mixing $\mu$s with ns or GHz with MHz when forming $N_\text{gates}$ or comparing bandwidth to anharmonicity.
- Treating the transmon as a perfect two-level system and ignoring leakage to $|2\rangle$ when a fast pulse's bandwidth approaches $|\alpha|$.

**Signs a student needs to return:**
- They report a $T_2$ larger than $2T_1$ and do not flag it as impossible.
- They compute $N_\text{gates}$ but cannot say what physical requirement (QEC, megaquop) it is being measured against.

**Scaffolding adjustments:** If a student struggles with Part A, have them first compute $T_2$ in *rate* units ($\mu\text{s}^{-1}$) and only invert at the very end, which makes the $2T_1$ ceiling visually obvious. If a student finishes Part F quickly, have them build the full $6\times5$ DiVincenzo table from the chapter (Challenge exercise 9) and identify which platform has the most balanced profile.

**Domain adaptation note:** All platform numbers are mid-2026 approximate and age within 12–24 months; emphasize the *method* ($T_2$ relation, $N_\text{gates}$, two-level validity) over any specific reported value.
