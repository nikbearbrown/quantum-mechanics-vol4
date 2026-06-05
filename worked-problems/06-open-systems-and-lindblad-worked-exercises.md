# Worked Exercises: Open Systems — Decoherence and the Lindblad Equation
*Chapter 6 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can write a single-qubit density matrix in Bloch form $\hat\rho = \tfrac12(\hat I + \vec r\cdot\vec\sigma)$ and convert between $(r_x, r_y, r_z)$ and matrix entries.
- You can manipulate the GKSL dissipator $\mathcal D[\hat\rho] = \hat L\hat\rho\hat L^\dagger - \tfrac12\{\hat L^\dagger\hat L, \hat\rho\}$, using $\hat\sigma_z\hat\sigma_x\hat\sigma_z = -\hat\sigma_x$ and trace cyclicity.
- You know the central results $1/T_2 = 1/(2T_1) + 1/T_\phi$ and the constraint $T_2 \le 2T_1$, and the equilibrium $r_z^\text{eq} = -1$ (ground state at the south pole).

---

## Part A — Full Worked Example: Solving the pure-dephasing dissipator and reading off $\dot r_x$

**What this demonstrates:** That the transverse Bloch decay rate $1/T_\phi$ falls directly out of the GKSL dephasing dissipator — the $\tfrac12$-anticommutator structure is what makes the calculation trace-preserving and gives the correct rate.

**The problem:** Take $\hat H = 0$ and a single dephasing jump operator $\hat L_\phi = \sqrt{1/2T_\phi}\,\hat\sigma_z$. Starting from the GKSL dissipator, derive the equation of motion $\dot r_x$ for the $x$-component of the Bloch vector, and confirm it gives $\dot r_x = -r_x/T_\phi$.

**The solution:**

**Step 1 — Write the dissipator with the jump operator.** With $\hat L_\phi = \sqrt{1/2T_\phi}\,\hat\sigma_z$ and $\hat\sigma_z^\dagger\hat\sigma_z = \hat I$:
$$\mathcal D[\hat\rho] = \frac{1}{2T_\phi}\left(\hat\sigma_z\hat\rho\hat\sigma_z - \frac12\{\hat\sigma_z^\dagger\hat\sigma_z, \hat\rho\}\right) = \frac{1}{2T_\phi}\bigl(\hat\sigma_z\hat\rho\hat\sigma_z - \hat\rho\bigr).$$
*Why:* Because $\hat\sigma_z^2 = \hat I$, the anticommutator $\tfrac12\{\hat I, \hat\rho\} = \hat\rho$ collapses to a clean subtraction.
*Check:* $\text{Tr}(\mathcal D[\hat\rho]) = \tfrac{1}{2T_\phi}(\text{Tr}(\hat\sigma_z\hat\rho\hat\sigma_z) - \text{Tr}\hat\rho) = \tfrac{1}{2T_\phi}(\text{Tr}\hat\rho - \text{Tr}\hat\rho) = 0$ by cyclicity — trace-preserving. ✓

**Step 2 — Insert the Bloch form $\hat\rho = \tfrac12(\hat I + r_x\sigma_x + r_y\sigma_y + r_z\sigma_z)$.** Use $\hat\sigma_z\hat\sigma_x\hat\sigma_z = -\hat\sigma_x$, $\hat\sigma_z\hat\sigma_y\hat\sigma_z = -\hat\sigma_y$, $\hat\sigma_z\hat\sigma_z\hat\sigma_z = \hat\sigma_z$, $\hat\sigma_z\hat I\hat\sigma_z = \hat I$:
$$\hat\sigma_z\hat\rho\hat\sigma_z = \frac12(\hat I - r_x\sigma_x - r_y\sigma_y + r_z\sigma_z).$$
*Why:* Conjugation by $\hat\sigma_z$ flips the sign of the transverse Pauli components and leaves $\hat I$ and $\sigma_z$ alone.
*Check:* The longitudinal part ($\hat I$, $\sigma_z$) is unchanged, consistent with pure dephasing not moving population. ✓

**Step 3 — Subtract to get the dissipator's matrix.**
$$\hat\sigma_z\hat\rho\hat\sigma_z - \hat\rho = \frac12\bigl[(-r_x\sigma_x - r_y\sigma_y) - (r_x\sigma_x + r_y\sigma_y)\bigr] = -r_x\sigma_x - r_y\sigma_y.$$
So
$$\mathcal D[\hat\rho] = \frac{1}{2T_\phi}(-r_x\sigma_x - r_y\sigma_y).$$
*Why:* Only the transverse terms survive; the $\hat I$ and $\sigma_z$ pieces cancel.
*Check:* No $\sigma_z$ or $\hat I$ term means $\dot r_z = 0$ and trace stays fixed — exactly the dephasing signature. ✓

**Step 4 — Extract $\dot r_x$ via $r_x = \text{Tr}(\hat\rho\hat\sigma_x)$.** Since $\dot{\hat\rho} = \mathcal D[\hat\rho]$ and $\dot r_x = \text{Tr}(\dot{\hat\rho}\,\hat\sigma_x)$:
$$\dot r_x = \text{Tr}\!\left(\frac{1}{2T_\phi}(-r_x\sigma_x - r_y\sigma_y)\,\sigma_x\right) = \frac{1}{2T_\phi}(-r_x)\,\text{Tr}(\sigma_x^2) = \frac{1}{2T_\phi}(-r_x)(2).$$
*Why:* $\text{Tr}(\sigma_x^2) = 2$ and $\text{Tr}(\sigma_y\sigma_x) = 0$ project out only the $r_x$ contribution.
*Check:* The factor of 2 from $\text{Tr}(\sigma_x^2)$ cancels the $\tfrac12$ in $1/2T_\phi$, giving a clean rate. ✓

**Final answer:** $\dot r_x = -r_x/T_\phi$ (and identically $\dot r_y = -r_y/T_\phi$, $\dot r_z = 0$). Pure dephasing squeezes the Bloch vector toward the $z$-axis at rate $1/T_\phi$ without moving it along $z$.

**What made this work:** The $\tfrac12\{\hat L^\dagger\hat L, \hat\rho\}$ term is not decorative — for $\hat L_\phi \propto \sigma_z$ it equals exactly $\hat\rho$ (since $\sigma_z^2 = I$), so the dissipator reduces to $\sigma_z\hat\rho\sigma_z - \hat\rho$, whose only effect is to flip and cancel the transverse Pauli components. Drop the $\tfrac12$ or get its sign wrong and the trace no longer vanishes — you would get a non-physical, non-trace-preserving equation. The rate $1/T_\phi$ emerges because $\text{Tr}(\sigma_x^2) = 2$ exactly cancels the $1/2T_\phi$ prefactor's denominator.

**Self-explanation prompt:** Why does the same dissipator give $\dot r_z = 0$? Trace the cancellation and explain in one sentence what "the environment monitors $\sigma_z$" means physically here.

---

## Part B — Matched Practice Problem

**The problem:** Take $\hat H = 0$ and the energy-relaxation jump operator $\hat L_1 = \sqrt{1/T_1}\,\hat\sigma_-$ where $\hat\sigma_- = |0\rangle\langle1|$. Derive the equation of motion $\dot r_z$ for the longitudinal Bloch component from the GKSL dissipator, and confirm it equals $\dot r_z = -(r_z + 1)/T_1$ with equilibrium at the south pole $r_z^\text{eq} = -1$.

Work it with the same four-step structure:

**Step 1 — Write the dissipator** $\hat L_1\hat\rho\hat L_1^\dagger - \tfrac12\{\hat L_1^\dagger\hat L_1, \hat\rho\}$ with the $1/T_1$ prefactor.

**Step 2 — Use $\hat\sigma_+\hat\sigma_- = |1\rangle\langle1|$ and $\hat\sigma_-\hat\sigma_+ = |0\rangle\langle0|$** and insert the Bloch form.

**Step 3 — Subtract to get the dissipator's matrix** (note: unlike dephasing, this one produces a constant $\hat I$-shift term — that is what sets the nonzero equilibrium).

**Step 4 — Extract $\dot r_z$ via $r_z = \text{Tr}(\hat\rho\hat\sigma_z)$.**

**Stuck?** The relaxation dissipator is not traceless in the transverse sense the way dephasing was: $\hat\sigma_-\hat\rho\hat\sigma_+$ feeds population from $|1\rangle$ into $|0\rangle$, producing a term proportional to $|0\rangle\langle0|$. That constant offset is exactly what pins the equilibrium to $r_z = -1$ rather than $r_z = 0$. Watch for the asymmetry between $\sigma_+\sigma_-$ and $\sigma_-\sigma_+$ in the anticommutator.

*(Instructor note: full solution intentionally omitted — students derive $\dot r_z$, the $-1$ equilibrium, and should also note that the same operator gives $\dot r_x^{(1)} = -r_x/2T_1$, the 2:1 transverse-to-longitudinal ratio.)*

---

## Part C — Completion Problem

**The problem:** A qubit starts on the equator, $(r_x, r_y, r_z) = (1, 0, 0)$, and evolves under $\omega_0 = 0$, $T_1 = 4\,\mu$s, $T_\phi = 4\,\mu$s. Find the full Bloch trajectory, the purity at $t = T_2$, and the limiting state. Steps 1, 2, and 5 plus the final answer are provided; fill in Steps 3 and 4.

**Step 1 — Compute $T_2$ from the sum formula.**
$$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi} = \frac{1}{8\,\mu\text{s}} + \frac{1}{4\,\mu\text{s}} = \frac{3}{8\,\mu\text{s}} \implies T_2 = \frac{8}{3}\,\mu\text{s} \approx 2.67\,\mu\text{s}.$$

**Step 2 — Write the Bloch equations with $\omega_0 = 0$.**
$$\dot r_x = -\frac{r_x}{T_2}, \qquad \dot r_y = -\frac{r_y}{T_2}, \qquad \dot r_z = -\frac{r_z + 1}{T_1}.$$

**Step 3 — Solve for $r_x(t), r_y(t), r_z(t)$ with the given initial condition.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Compute the purity $\text{Tr}(\hat\rho^2) = \tfrac12(1 + |\vec r|^2)$ at $t = T_2$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Determine the limiting state as $t \to \infty$ and identify it on the Bloch sphere.**
$$r_x(\infty) = 0, \quad r_y(\infty) = 0, \quad r_z(\infty) = -1 \implies \hat\rho(\infty) = |0\rangle\langle0|.$$

**Final answer:** $r_x(t) = e^{-t/T_2}$, $r_y(t) = 0$, $r_z(t) = -1 + e^{-t/T_1}$. At $t = T_2 = 8/3\,\mu$s the purity is $\tfrac12(1 + e^{-2} + (e^{-T_2/T_1} - 1)^2)$; as $t \to \infty$ the qubit decays to the ground state $|0\rangle$ at the south pole (energy relaxation, not just dephasing, because $T_1$ is finite).

**Self-explanation prompt:** This trajectory ends at the south pole, but the pure-dephasing worked calculation in the chapter ended at the origin $\hat I/2$. Explain in one sentence what single difference in the jump operators causes the different endpoints.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student is asked to write the dissipator for amplitude damping with $\hat L = \sqrt\gamma\,\hat\sigma_-$ and check that the resulting master equation is trace-preserving. They write the following.

**Step 1.** Jump operator $\hat L = \sqrt\gamma\,\hat\sigma_-$, so $\hat L^\dagger\hat L = \gamma\,\hat\sigma_+\hat\sigma_- = \gamma\,|1\rangle\langle1|$. ✓

**Step 2.** The master equation is $\dot{\hat\rho} = \hat L\hat\rho\hat L^\dagger - \tfrac12\{\hat L^\dagger\hat L, \hat\rho\}$. ✓

**Step 3.** ⚠ "To make the algebra cleaner I'll use the *symmetric* form of the dissipator: $\dot{\hat\rho} = \hat L\hat\rho\hat L^\dagger - \hat L^\dagger\hat L\,\hat\rho$. (I dropped the $\tfrac12$ and the anticommutator — they only make the bookkeeping messy, and either ordering of $\hat L^\dagger\hat L$ and $\hat\rho$ should give the same trace.) Then $\text{Tr}(\dot{\hat\rho}) = \text{Tr}(\hat L^\dagger\hat L\hat\rho) - \text{Tr}(\hat L^\dagger\hat L\hat\rho) = 0$, so it's trace-preserving."

**Step 4.** Therefore the master equation conserves probability and is a valid GKSL generator. ✓

**Your tasks:**
1. Identify the error in Step 3 and explain why the student's "$\text{Tr} = 0$" check is misleadingly *consistent* even though the equation is wrong.
2. Compute $\text{Tr}(\dot{\hat\rho})$ for the student's form $\hat L\hat\rho\hat L^\dagger - \hat L^\dagger\hat L\,\hat\rho$ carefully, keeping the two terms separate, and show that while it happens to give zero, the *correct* GKSL form $\hat L\hat\rho\hat L^\dagger - \tfrac12\{\hat L^\dagger\hat L, \hat\rho\}$ is the one that guarantees both Hermiticity of $\hat\rho$ and trace preservation. (Hint: the student's form makes $\hat\rho$ non-Hermitian.)
3. Restore the $\tfrac12$ anticommutator and verify trace preservation using cyclicity, as in the chapter: $\text{Tr}(\hat L\hat\rho\hat L^\dagger) - \tfrac12\text{Tr}(\hat L^\dagger\hat L\hat\rho) - \tfrac12\text{Tr}(\hat\rho\hat L^\dagger\hat L) = 0$.
4. State the structural rule: which property ($\tfrac12$ anticommutator, sign, Hermiticity, trace) does each part of the GKSL dissipator enforce?

**Why this error is common:** Students treat the $\tfrac12$ anticommutator as a normalization nuisance rather than the structural feature that simultaneously enforces complete positivity and keeps $\hat\rho$ Hermitian, so they "simplify" it away and get an equation that is not a valid quantum channel.

---

## Part E — Transfer Problem

**The problem:** Apply the same $T_1$–$T_2$ reasoning to real hardware. A transmon qubit is measured with $T_1 = 300\,\mu$s and $T_2 = 180\,\mu$s. (a) Is the measurement consistent with the constraint $T_2 \le 2T_1$? (b) Solve the sum formula for $T_\phi$, the pure-dephasing time. (c) An engineer applies a dynamical-decoupling sequence that doubles $T_\phi$; compute the new $T_2$ and state how close the qubit now sits to the natural-linewidth limit $T_2 = 2T_1$. (d) Compute the fraction of the off-diagonal coherence $|\rho_{01}|$ remaining after one two-qubit gate of duration $t_\text{gate} = 200\,$ns, using the envelope $|\rho_{01}(t)| = \tfrac12 e^{-t/T_2}$.

**Hint (use only if stuck after 10 minutes):** Rearrange $1/T_2 = 1/(2T_1) + 1/T_\phi$ to $1/T_\phi = 1/T_2 - 1/(2T_1)$. With $T_1 = 300$, $T_2 = 180$ ($\mu$s): $1/T_\phi = 1/180 - 1/600$. For (d) the gate is far shorter than $T_2$, so expand $e^{-t_\text{gate}/T_2} \approx 1 - t_\text{gate}/T_2$ to see the coherence loss per gate is tiny but nonzero.

**Reflection prompt:** (1) Trapped ions sit near $T_2 \approx 2T_1$ while transmons sit below it — what does $T_\phi$ tell you about the dominant noise in each case? (2) The natural-linewidth limit $T_2 = 2T_1$ requires $T_\phi \to \infty$. Why can real hardware approach but never exceed it?

---

## Part F — Interleaved Review

**F1 — This chapter.** A qubit has density matrix $\hat\rho = \begin{pmatrix} 0.7 & 0.3 \\ 0.3 & 0.3 \end{pmatrix}$. (a) Extract the Bloch vector $(r_x, r_y, r_z)$. (b) Compute the purity $\text{Tr}(\hat\rho^2)$. (c) Confirm it is a valid density matrix ($\text{Tr} = 1$, Hermitian, $|\vec r| \le 1$, eigenvalues $\ge 0$).
*Chapter this draws from: 6*

**F2 — Previous chapter.** In the teleportation protocol, Bob's reduced density matrix *before* the classical bits arrive is $\hat\rho_B = \text{Tr}_{SA}(|\Psi_2\rangle\langle\Psi_2|) = \hat I/2$. Compute its Bloch vector and purity, and explain how this maximally mixed state is the same object that pure dephasing drives a qubit toward — and why in teleportation it signals *no-signaling* rather than decoherence.
*Chapter this draws from: Quantum Teleportation and Dense Coding (Chapter 5)*

**F3 — Discrimination.** You are shown two processes that both drive a qubit's off-diagonal $|\rho_{01}|$ to zero. Process 1: $\hat L_\phi = \sqrt{1/2T_\phi}\,\sigma_z$ acting on an equatorial state. Process 2: $\hat L_1 = \sqrt{1/T_1}\,\sigma_-$ acting on the same state. For each, state the final Bloch vector, whether populations change, and where the vector ends up on the sphere.
*Note to instructor: students must distinguish pure dephasing (transverse decay only, endpoint $\hat I/2$ at the origin, populations fixed) from energy relaxation (transverse *and* longitudinal decay, endpoint $|0\rangle$ at the south pole, populations driven to ground) — both kill coherence but for different physical reasons and to different endpoints.*

**Closing reflection:** Across all six parts, the constraint $T_2 \le 2T_1$ recurred. Explain in two sentences how this single inequality encodes the physical fact that "coherence is always at least as fragile as population," and trace it back to the GKSL structure of the relaxation jump operator $\hat\sigma_-$.

---

## Instructor Notes

**Common errors:**
1. Dropping or mis-signing the $\tfrac12\{\hat L^\dagger\hat L, \hat\rho\}$ anticommutator, producing a non-trace-preserving or non-Hermitian master equation (the Part D misconception).
2. Setting the relaxation equilibrium at the north pole $r_z = +1$ instead of the south pole $r_z = -1$ — sign-flipping the ground state.
3. Writing $T_2 > 2T_1$ (e.g. by adding rates instead of using $1/T_2 = 1/2T_1 + 1/T_\phi$), violating the hard physical constraint.

**Signs a student needs to return:**
- They cannot explain *why* the transverse decay rate from $\hat\sigma_-$ is half the longitudinal rate (the 2:1 ratio is "from the algebra, not from memory").
- They apply the single-exponential Lindblad envelope $\tfrac12 e^{-t/T_2}$ to a structured/non-Markovian bath (e.g. a $^{13}$C spin bath) without flagging that the Markov approximation fails there.

**Scaffolding adjustments:** If a student struggles with Part A, first have them verify trace preservation alone (Step 1's check) before deriving the rate. If a student finishes Part F quickly, have them work the complete-positivity exercise: show the transpose map $\mathcal T:\hat\rho\mapsto\hat\rho^T$ is positive on single qubits but $(\mathcal T\otimes\mathcal I)$ produces negative eigenvalues on $|\Phi^+\rangle\langle\Phi^+|$, hence is not a physical channel.

**Domain adaptation note:** For an NV-center or spin-qubit course, replace the transmon numbers in Part E with platform-appropriate $T_1, T_2$ and explicitly discuss when the Markovian Lindblad model must be swapped for a non-exponential (Gaussian-tail) decay.
