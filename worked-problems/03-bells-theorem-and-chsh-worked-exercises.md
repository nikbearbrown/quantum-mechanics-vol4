# Worked Exercises: Bell's Theorem and the CHSH Inequality
*Chapter 3 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The CHSH parameter $S = E(A_1,B_1) + E(A_1,B_2) + E(A_2,B_1) - E(A_2,B_2)$, the local-realistic bound $|S| \le 2$, and the Tsirelson bound $|S| \le 2\sqrt2 \approx 2.828$.
- The quantum correlation formula $E(\hat a,\hat b) = \cos(\theta_a - \theta_b)$ for $|\Phi^+\rangle$ and $E(\hat a,\hat b) = -\cos(\theta_a - \theta_b)$ for the singlet $|\Psi^-\rangle$; the canonical optimal angles $\theta_{A_1} = 0°,\ \theta_{A_2} = 90°,\ \theta_{B_1} = 45°,\ \theta_{B_2} = -45°$.
- No-signaling: $\hat\rho_B = \text{Tr}_A(|\Phi^+\rangle\langle\Phi^+|) = \tfrac12\hat I$ is unchanged by anything Alice does; the loophole structure (detection $\eta > 82\%$, locality / spacelike separation).

---

## Part A — Full Worked Example

**What this demonstrates:** How to compute the CHSH parameter $S$ for an entangled state at a given set of measurement angles and read it against both the classical bound (2) and the Tsirelson bound ($2\sqrt2$).

**The problem:** Alice and Bob share the Bell state $|\Phi^+\rangle$, for which $E(\hat a,\hat b) = \cos(\theta_a - \theta_b)$. Compute $S$ for the canonical optimal angles $\theta_{A_1} = 0°,\ \theta_{A_2} = 90°,\ \theta_{B_1} = 45°,\ \theta_{B_2} = -45°$, verify it reaches the Tsirelson bound, and state by how much it exceeds the classical bound.

**The solution:**

**Step 1 — Set up the four correlators as relative-angle cosines.** With $E = \cos(\theta_a - \theta_b)$, the four terms depend only on the differences:
- $E(A_1,B_1) = \cos(0° - 45°) = \cos(-45°)$
- $E(A_1,B_2) = \cos(0° - (-45°)) = \cos(45°)$
- $E(A_2,B_1) = \cos(90° - 45°) = \cos(45°)$
- $E(A_2,B_2) = \cos(90° - (-45°)) = \cos(135°)$

*Why:* The correlation depends only on the relative angle between Alice's and Bob's axes, so each $E$ is a single cosine.
*Check:* Each argument is a valid angle and each cosine will lie in $[-1,1]$.

**Step 2 — Evaluate the cosines.**

$$\cos(-45°) = +\tfrac{1}{\sqrt2}, \quad \cos(45°) = +\tfrac{1}{\sqrt2}, \quad \cos(45°) = +\tfrac{1}{\sqrt2}, \quad \cos(135°) = -\tfrac{1}{\sqrt2}.$$

*Why:* These are the actual numerical correlations Alice and Bob would measure at these settings.
*Check:* All four values are $\pm\tfrac{1}{\sqrt2} \approx \pm0.707$, safely inside $[-1,1]$.

**Step 3 — Assemble $S$ with the correct sign pattern (three plus, one minus).**

$$S = E(A_1,B_1) + E(A_1,B_2) + E(A_2,B_1) - E(A_2,B_2) = \tfrac{1}{\sqrt2} + \tfrac{1}{\sqrt2} + \tfrac{1}{\sqrt2} - \left(-\tfrac{1}{\sqrt2}\right).$$

*Why:* The CHSH combination subtracts the last correlator — this sign is what makes the four-angle combination able to exceed 2.
*Check:* The subtraction of a negative number adds a fourth positive $\tfrac{1}{\sqrt2}$; all four terms now contribute with the same sign.

**Step 4 — Sum to the Tsirelson value.**

$$S = \frac{4}{\sqrt2} = \frac{4}{\sqrt2}\cdot\frac{\sqrt2}{\sqrt2} = \frac{4\sqrt2}{2} = 2\sqrt2 \approx 2.828.$$

*Why:* This is the quantum prediction at the optimal angles — the maximum any quantum state can produce.
*Check:* $2\sqrt2 = 2.8284\ldots \le 2\sqrt2$: it sits exactly at the Tsirelson ceiling, not above it. A value above $2.828$ would be a bug.

**Step 5 — Compare against both bounds.** The classical local-hidden-variable bound is $|S| \le 2$. The quantum value $2\sqrt2 \approx 2.828$ exceeds it by $2\sqrt2 - 2 \approx 0.828$, which is $\tfrac{0.828}{2} \approx 41\%$ of the classical bound.

*Why:* The whole point of Bell's theorem is that this gap is real and measurable — no local-realistic model can reach it.
*Check:* $2 < 2.828 \le 2.828$ — the value is in the quantum window $2 < |S| \le 2\sqrt2$, above classical and at the Tsirelson edge.

**Final answer:** $S = 2\sqrt2 \approx 2.828$, exactly the Tsirelson bound, exceeding the classical bound of 2 by about 41%.

**What made this work:** The key was that each correlator depends only on the relative angle $\theta_a - \theta_b$, so the four-term sum collapsed to four cosines that happen to align. The canonical angles $(0°, 90°, 45°, -45°)$ are not arbitrary — they are spaced so that the three "$+$" correlators are all $+\tfrac{1}{\sqrt2}$ and the one "$-$" correlator is $-\tfrac{1}{\sqrt2}$, so subtracting it adds rather than cancels. Any other spacing gives a smaller $|S|$. The Tsirelson bound is the guardrail: if a calculation ever returns $|S| > 2.828$ for a quantum state, it is an arithmetic error, never physics.

**Self-explanation prompt:** Why does subtracting $E(A_2,B_2)$ — rather than adding it — let $S$ exceed 2? What would $S$ equal at these same angles if all four terms were added?

---

## Part B — Matched Practice Problem

**The problem:** Alice and Bob share $|\Phi^+\rangle$ ($E = \cos(\theta_a - \theta_b)$), but the apparatus is misaligned and uses the *non-optimal* angles $\theta_{A_1} = 0°,\ \theta_{A_2} = 60°,\ \theta_{B_1} = 30°,\ \theta_{B_2} = 90°$.

**Step 1 — Set up the four correlators as relative-angle cosines.** Write each $E(A_i,B_j)$ as a cosine of the angle difference.

**Step 2 — Evaluate the cosines.** Compute the four numerical correlation values.

**Step 3 — Assemble $S$ with the correct sign pattern (three plus, one minus).** Write out the signed combination.

**Step 4 — Sum to a numerical value.** Compute $S$.

**Step 5 — Compare against both bounds.** State whether $|S| > 2$ (a real violation) and whether it reaches $2\sqrt2$ (optimal). Explain in one sentence why this angle choice does or does not violate the classical bound.

**Stuck?** $\cos(30°) = \tfrac{\sqrt3}{2} \approx 0.866$, $\cos(60°) = \tfrac12$, $\cos(90°) = 0$, $\cos(0°) = 1$. The differences you need are $-30°, -90°, +30°, -30°$.

*Instructor note: solution intentionally omitted. These angles give a real but sub-optimal violation — students should find $2 < |S| < 2\sqrt2$ and recognize that a violation at non-optimal angles is genuine but does not reach the Tsirelson ceiling. Caution students against rounding $S$ up to $2.828$.*

---

## Part C — Completion Problem

**The problem:** Alice and Bob share the singlet $|\Psi^-\rangle$, for which $E(\hat a,\hat b) = -\cos(\theta_a - \theta_b)$. Compute $S$ at the canonical angles $\theta_{A_1} = 0°,\ \theta_{A_2} = 90°,\ \theta_{B_1} = 45°,\ \theta_{B_2} = -45°$.

**Step 1 — Set up the four correlators as relative-angle cosines (provided).** With $E = -\cos(\theta_a - \theta_b)$:
- $E(A_1,B_1) = -\cos(-45°)$
- $E(A_1,B_2) = -\cos(45°)$
- $E(A_2,B_1) = -\cos(45°)$
- $E(A_2,B_2) = -\cos(135°)$

**Step 2 — Evaluate the cosines (provided).**

$$E(A_1,B_1) = -\tfrac{1}{\sqrt2}, \quad E(A_1,B_2) = -\tfrac{1}{\sqrt2}, \quad E(A_2,B_1) = -\tfrac{1}{\sqrt2}, \quad E(A_2,B_2) = +\tfrac{1}{\sqrt2}.$$

**Step 3 — Assemble $S$ with the correct sign pattern (three plus, one minus).**
*Your work here:*
*Why (your explanation):*

**Step 4 — Sum to a numerical value.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Compare against both bounds (provided).** The result is $|S| = 2\sqrt2 \approx 2.828$, the Tsirelson bound, exceeding the classical bound of 2. The singlet gives $S = -2\sqrt2$ (negative) where $|\Phi^+\rangle$ gave $+2\sqrt2$; the magnitude is the same for all four Bell states, only the sign differs.

**Final answer:** $S = -2\sqrt2 \approx -2.828$, so $|S| = 2\sqrt2$ — the singlet reaches the Tsirelson bound with the opposite sign from $|\Phi^+\rangle$.

**Self-explanation prompt:** The singlet's $S$ came out negative while $|\Phi^+\rangle$'s was positive, yet both violate the inequality equally. Why is it $|S|$, not $S$, that we compare against the bound of 2?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student computes $S$ for $|\Phi^+\rangle$ but with everyone measuring along the *same* direction, $\theta_{A_1} = \theta_{A_2} = \theta_{B_1} = \theta_{B_2} = 0°$. They write:

**Step 1.** With $E = \cos(\theta_a - \theta_b)$ and all angles equal, every difference is $0°$, so all four correlators are $\cos(0°) = +1$.

**Step 2.** "Each correlation is $+1$ — perfect correlation. Alice and Bob's outcomes always agree."

**Step 3.** ⚠ "Because each correlation is at its maximum value $+1$ — much larger than $\tfrac{1}{\sqrt2}$ — this configuration is even more strongly nonlocal than the optimal angles. A perfect correlation of $+1$ is clear proof of a Bell violation. I expect $|S| \gg 2$."

**Step 4.** Conclusion: "Strong Bell violation; $|S|$ far above 2."

**Your tasks:**
1. Compute $S$ for these equal angles using the CHSH sign pattern, and show it actually equals 2, NOT something large.
2. Explain why a single large correlation ($E = +1$) is NOT evidence of a Bell violation — and note that a classical hidden-variable model reproduces $E = +1$ trivially.
3. State which property of the four-angle combination (not any single correlator) is responsible for a real violation.
4. Write the corrected conclusion in one sentence.

**Why this error is common:** Students conflate "strong correlation" with "nonlocality," but a perfect correlation at identical settings is exactly what a classical pre-arranged hidden-variable model produces — the violation lives in the relative angles, not in any one correlator's magnitude.

---

## Part E — Transfer Problem

**The problem:** Demonstrate the no-signaling property explicitly. Alice and Bob share $|\Phi^+\rangle = \tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$. Alice applies a unitary to her qubit and wants to know whether this changes Bob's local measurement statistics.

(a) Compute Bob's reduced density matrix $\hat\rho_B = \text{Tr}_A(|\Phi^+\rangle\langle\Phi^+|)$ before Alice does anything.
(b) Now Alice applies the Pauli $X$ gate to her qubit, giving the new joint state $(X\otimes I)|\Phi^+\rangle$. Write this new state.
(c) Compute Bob's reduced density matrix after Alice's operation and show it is unchanged.
(d) State in one sentence why this means Alice cannot signal to Bob, even though their outcomes are correlated.

**Hint (use only if stuck after 10 minutes):** $(X\otimes I)|\Phi^+\rangle = \tfrac{1}{\sqrt2}(|10\rangle + |01\rangle) = |\Psi^+\rangle$. To take the partial trace over $A$, use $\hat\rho_B = \sum_i \langle i|_A\,\hat\rho_{AB}\,|i\rangle_A$ with $i = 0,1$.

**Reflection prompt:**
1. Alice's local operation turned $|\Phi^+\rangle$ into $|\Psi^+\rangle$ — a genuinely different joint state — yet Bob sees no change. How can the global state change while the local marginal stays fixed?
2. If Alice's operation had changed $\hat\rho_B$, what catastrophe for relativity would follow, and why does the partial-trace result rule it out?

---

## Part F — Interleaved Review

**F1 — This chapter.** For $|\Phi^+\rangle$ at angles $\theta_{A_1} = 0°,\ \theta_{B_1} = 75°$: (a) compute $E(A_1,B_1)$; (b) at what relative angle is the correlation maximal, and what value does it take; (c) at what relative angle does it vanish?
*Chapter this draws from: 3.*

**F2 — Composite Systems and Entanglement.** The singlet $|\Psi^-\rangle = \tfrac{1}{\sqrt2}(|01\rangle - |10\rangle)$ is used in the CHSH calculation. (a) Compute $\det(C)$ for $|\Psi^-\rangle$ and confirm it is maximally entangled. (b) Compute its entanglement entropy $S_E$. (c) Explain why a state must be entangled ($S_E > 0$) to violate CHSH.
*Chapter this draws from: Composite Systems and Entanglement.*

**F3 — Discrimination.** You measure a CHSH value of $S = 1.8$ on a real apparatus, and separately a value of $S = 2.6$. For each, state whether it (i) violates the classical bound, (ii) is consistent with quantum mechanics, and (iii) could be faked by a local hidden-variable model. Use only the bounds 2 and $2\sqrt2$.
*Note to instructor: this problem checks whether the student can place a measured number in the three-region structure — classical ($|S| \le 2$), quantum window ($2 < |S| \le 2\sqrt2$), and impossible ($|S| > 2\sqrt2$). A student who tries to back out angles has missed that the classification follows from the value alone.*

**Closing reflection:** Across F1–F3, the same two numbers — 2 and $2\sqrt2$ — sorted every result into classical, quantum, or impossible. Write one sentence on why these two bounds, not the individual correlations, are the quantities that decide whether an experiment has demonstrated nonlocality.

---

## Instructor Notes

**Common errors:**
- Using the wrong bound — treating the classical $|S| \le 2$ as the ceiling, or expecting a quantum state to exceed $2\sqrt2$.
- Sending angles in degrees to a cosine that expects radians (or vice versa), producing nonsensical correlators.
- Using the wrong sign in the correlation formula — $+\cos$ for the singlet instead of $-\cos$ — which flips the sign of $S$ and can mask or fake a violation.

**Signs a student needs to return:**
- They report $|S| > 2\sqrt2$ for a quantum state and do not flag it as impossible.
- They conclude a Bell violation from one large correlation rather than the full four-angle combination.

**Scaffolding adjustments:** A student stuck on Part A should first confirm each correlator lies in $[-1,1]$ before summing — an out-of-range cosine signals a degrees/radians slip. A student who finishes Part F quickly should be asked to find a second set of optimal angles (rotate all four by the same offset) and confirm $S$ is unchanged, showing the violation is a property of relative, not absolute, angles.

**Domain adaptation note:** For students reconstructing a loophole-free Bell test (e.g. Hensen et al. 2015, $S = 2.42 \pm 0.20$), this is the dossier's headline calculation — compute the ideal $S = 2\sqrt2$, compare to the paper's measured $S_{\text{exp}}$, and read the gap as the signature of detection inefficiency and decoherence, without overstating statistical "agreement."
