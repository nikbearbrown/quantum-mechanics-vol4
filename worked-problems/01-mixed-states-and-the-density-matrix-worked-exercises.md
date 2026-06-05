# Worked Exercises: Mixed States and the Density Matrix
*Chapter 1 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The density operator $\hat\rho = \sum_i p_i\,|\psi_i\rangle\langle\psi_i|$, its three defining properties (Hermitian, unit trace, positive semidefinite), and the purity criterion $\text{Tr}(\hat\rho^2) \le 1$ with equality only for pure states.
- The expectation-value rule $\langle\hat A\rangle = \text{Tr}(\hat\rho\,\hat A)$, and the Bloch representation $\hat\rho = \tfrac12(\hat I + \vec r\cdot\vec\sigma)$ with $\text{Tr}(\hat\rho^2) = \tfrac12(1 + |\vec r|^2)$.
- The Pauli matrices $\hat\sigma_x = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, $\hat\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$, $\hat\sigma_z = \bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$, and the partial trace $\hat\rho_A = \text{Tr}_B(\hat\rho_{AB})$.

---

## Part A — Full Worked Example

**What this demonstrates:** That a classical probabilistic mixture of two non-orthogonal pure states builds a density matrix whose purity, expectation values, and Bloch vector all follow from the trace.

**The problem:** A laboratory prepares a qubit by one of two methods at random. With probability $p_1 = \tfrac{1}{3}$ it prepares $|1\rangle$; with probability $p_2 = \tfrac{2}{3}$ it prepares $|{-}\rangle = (|0\rangle - |1\rangle)/\sqrt2$. Construct $\hat\rho$, compute its purity $\text{Tr}(\hat\rho^2)$, find $\langle\hat\sigma_x\rangle = \text{Tr}(\hat\rho\,\hat\sigma_x)$, and locate the state in the Bloch ball.

**The solution:**

**Step 1 — Assemble the density operator from the ensemble.** In the $\{|0\rangle,|1\rangle\}$ basis, $|1\rangle\langle1| = \bigl(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\bigr)$ and $|{-}\rangle\langle{-}| = \tfrac12\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)$. So

$$\hat\rho = \tfrac13\begin{pmatrix}0&0\\0&1\end{pmatrix} + \tfrac23\cdot\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \tfrac13\begin{pmatrix}0&0\\0&1\end{pmatrix} + \tfrac13\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \begin{pmatrix}1/3 & -1/3 \\ -1/3 & 2/3\end{pmatrix}.$$

*Why:* The density operator is the probability-weighted sum of the projectors $|\psi_i\rangle\langle\psi_i|$ — this is the definition, and it works even though $|1\rangle$ and $|{-}\rangle$ are not orthogonal.
*Check:* $\text{Tr}(\hat\rho) = \tfrac13 + \tfrac23 = 1$. Unit trace holds.

**Step 2 — Confirm Hermiticity and positivity.** The matrix is real and symmetric, so $\hat\rho^\dagger = \hat\rho$. Its eigenvalues solve $\lambda^2 - \lambda + (\tfrac13\cdot\tfrac23 - \tfrac19) = \lambda^2 - \lambda + \tfrac{1}{9} = 0$, giving $\lambda = \tfrac12(1 \pm \sqrt{1 - 4/9}) = \tfrac12(1 \pm \sqrt{5}/3) \approx 0.873,\ 0.127$.

*Why:* A valid density matrix must be positive semidefinite — both eigenvalues non-negative — and they must sum to the trace, 1.
*Check:* $0.873 + 0.127 = 1.000$, both positive. Valid state.

**Step 3 — Compute the purity $\text{Tr}(\hat\rho^2)$.** Square the matrix:

$$\hat\rho^2 = \begin{pmatrix}1/3 & -1/3 \\ -1/3 & 2/3\end{pmatrix}^2 = \begin{pmatrix}1/9+1/9 & -1/9-2/9 \\ -1/9-2/9 & 1/9+4/9\end{pmatrix} = \begin{pmatrix}2/9 & -3/9 \\ -3/9 & 5/9\end{pmatrix}.$$

So $\text{Tr}(\hat\rho^2) = \tfrac29 + \tfrac59 = \tfrac79 \approx 0.778$.

*Why:* The purity distinguishes mixed from pure — $\text{Tr}(\hat\rho^2) < 1$ means the state is a genuine mixture, not a single vector.
*Check:* Equivalently, $\lambda_1^2 + \lambda_2^2 = 0.873^2 + 0.127^2 \approx 0.762 + 0.016 = 0.778$. Matches. And $0.778 < 1$ confirms mixedness; it is above the $1/2$ floor for a qubit.

**Step 4 — Evaluate $\langle\hat\sigma_x\rangle = \text{Tr}(\hat\rho\,\hat\sigma_x)$.** 

$$\hat\rho\,\hat\sigma_x = \begin{pmatrix}1/3 & -1/3 \\ -1/3 & 2/3\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}-1/3 & 1/3 \\ 2/3 & -1/3\end{pmatrix}, \quad \text{Tr} = -\tfrac13 - \tfrac13 = -\tfrac23.$$

*Why:* For a mixed state the expectation value is $\text{Tr}(\hat\rho\hat A)$, NOT $\langle\psi|\hat A|\psi\rangle$ — there is no single $|\psi\rangle$ to use.
*Check:* Cross-check with the ensemble average: $p_1\langle1|\hat\sigma_x|1\rangle + p_2\langle{-}|\hat\sigma_x|{-}\rangle = \tfrac13(0) + \tfrac23(-1) = -\tfrac23$. Matches.

**Step 5 — Read off the Bloch vector.** $r_x = \langle\hat\sigma_x\rangle = -\tfrac23$; $r_y = \text{Tr}(\hat\rho\hat\sigma_y) = 0$ (real $\hat\rho$); $r_z = \text{Tr}(\hat\rho\hat\sigma_z) = \rho_{00} - \rho_{11} = \tfrac13 - \tfrac23 = -\tfrac13$. So $\vec r = (-\tfrac23, 0, -\tfrac13)$, $|\vec r| = \sqrt{4/9 + 1/9} = \sqrt{5}/3 \approx 0.745$.

*Why:* The Bloch components are directly the Pauli expectation values; their magnitude encodes purity.
*Check:* $\tfrac12(1 + |\vec r|^2) = \tfrac12(1 + 5/9) = \tfrac12\cdot\tfrac{14}{9} = \tfrac{7}{9}$. Matches the Step 3 purity exactly.

**Final answer:** $\hat\rho = \bigl(\begin{smallmatrix}1/3 & -1/3 \\ -1/3 & 2/3\end{smallmatrix}\bigr)$, purity $\tfrac79$, $\langle\hat\sigma_x\rangle = -\tfrac23$, Bloch vector $\vec r = (-\tfrac23, 0, -\tfrac13)$ inside (not on) the unit sphere.

**What made this work:** Every quantity flowed from one object, $\hat\rho$, built once from the ensemble. The purity came two independent ways — squaring the matrix and squaring the eigenvalues — and the Bloch-vector magnitude reproduced it a third time through $\tfrac12(1+|\vec r|^2)$. That triple agreement is the signature of a correctly constructed density matrix: the consistency conditions are tight enough that an arithmetic slip in any one route breaks the match. The off-diagonal $-\tfrac13$ entries — present because $|{-}\rangle$ carries coherence — are exactly what a naive "it is $|1\rangle$ or $|{-}\rangle$, I just don't know which" story would miss.

**Self-explanation prompt:** Why is $\langle\hat\sigma_x\rangle$ nonzero here even though one of the two prepared states, $|1\rangle$, has $\langle\hat\sigma_x\rangle = 0$? Which ingredient of the mixture supplies the $x$-polarization?

---

## Part B — Matched Practice Problem

**The problem:** A source prepares a qubit as $|0\rangle$ with probability $p_1 = \tfrac34$ and as $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt2$ with probability $p_2 = \tfrac14$.

Carry out the same five-step analysis:

**Step 1 — Assemble the density operator from the ensemble.** Build $\hat\rho$ in the $\{|0\rangle,|1\rangle\}$ basis.

**Step 2 — Confirm Hermiticity and positivity.** Find the eigenvalues and verify they are non-negative and sum to 1.

**Step 3 — Compute the purity $\text{Tr}(\hat\rho^2)$.** Square the matrix and take the trace.

**Step 4 — Evaluate $\langle\hat\sigma_z\rangle = \text{Tr}(\hat\rho\,\hat\sigma_z)$.** Compute it via the trace and cross-check against the ensemble average.

**Step 5 — Read off the Bloch vector.** Find $\vec r$, its magnitude, and verify $\text{Tr}(\hat\rho^2) = \tfrac12(1+|\vec r|^2)$.

**Stuck?** $|0\rangle\langle0| = \bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$ and $|{+}\rangle\langle{+}| = \tfrac12\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$; the off-diagonal entries of $\hat\rho$ come only from the $|{+}\rangle$ term.

*Instructor note: solution intentionally omitted. The diagonal entries here resemble the chapter's opening lab scenario but the weights differ — students should not pattern-match to $\bigl(\begin{smallmatrix}3/4&1/4\\1/4&1/4\end{smallmatrix}\bigr)$ without recomputing.*

---

## Part C — Completion Problem

**The problem:** A qubit is prepared as $|{+}\rangle$ with probability $\tfrac12$ and as $|{-}\rangle$ with probability $\tfrac12$. Find $\hat\rho$, its purity, and its Bloch vector.

**Step 1 — Assemble the density operator (provided).** $|{+}\rangle\langle{+}| = \tfrac12\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$, $|{-}\rangle\langle{-}| = \tfrac12\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)$. Then

$$\hat\rho = \tfrac12\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix} + \tfrac12\cdot\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \begin{pmatrix}1/2 & 0 \\ 0 & 1/2\end{pmatrix} = \tfrac12\hat I.$$

**Step 2 — Confirm trace and eigenvalues (provided).** $\text{Tr}(\hat\rho) = 1$; eigenvalues are $\tfrac12, \tfrac12$, both non-negative. This is the maximally mixed state.

**Step 3 — Compute the purity $\text{Tr}(\hat\rho^2)$.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Evaluate $\langle\hat\sigma_x\rangle$, $\langle\hat\sigma_y\rangle$, $\langle\hat\sigma_z\rangle$ and read off $\vec r$.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Locate the state in the Bloch ball (provided).** With $\vec r = (0,0,0)$ the state sits at the exact center — the most mixed point. Note the striking fact: the equal mixture of the two opposite $x$-axis pure states $|{+}\rangle$ and $|{-}\rangle$ produces the SAME $\hat\rho = \tfrac12\hat I$ as an equal mixture of $|0\rangle$ and $|1\rangle$ would. Different ensembles, identical density matrix.

**Final answer:** $\hat\rho = \tfrac12\hat I$, purity $= \tfrac12$ (the qubit minimum), $\vec r = (0,0,0)$.

**Self-explanation prompt:** The mixture of $|{+}\rangle$ and $|{-}\rangle$ and the mixture of $|0\rangle$ and $|1\rangle$ give the same $\hat\rho$. What does this say about whether an experimentalist can ever recover the original ensemble from measurements on the qubit?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student is asked: "A qubit is prepared as $|0\rangle$ with probability $\tfrac12$ and as $|1\rangle$ with probability $\tfrac12$. Is this the same physical situation as the coherent superposition $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt2$?" They write:

**Step 1.** Mixture: $\hat\rho_{\text{mix}} = \tfrac12|0\rangle\langle0| + \tfrac12|1\rangle\langle1| = \bigl(\begin{smallmatrix}1/2&0\\0&1/2\end{smallmatrix}\bigr)$.

**Step 2.** Superposition: $\hat\rho_{\text{sup}} = |\psi\rangle\langle\psi| = \tfrac12\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$.

**Step 3.** ⚠ "Both have the same diagonal $(\tfrac12, \tfrac12)$, so they represent the same state. The off-diagonal entries are just a bookkeeping artifact of the basis and have no physical meaning — measuring $\hat\sigma_z$ on either gives outcomes $0$ and $1$ with probability $\tfrac12$ each, so they are physically identical."

**Step 4.** Conclusion: "A 50/50 mixture and the equal superposition are the same quantum state."

**Your tasks:**
1. Identify the conceptual error in Step 3 and state precisely why having the same diagonal does not make two states identical.
2. Compute $\text{Tr}(\hat\rho_{\text{mix}}^2)$ and $\text{Tr}(\hat\rho_{\text{sup}}^2)$ and show the two states have different purity.
3. Find a single observable whose expectation value differs between the two states, and compute both values.
4. Write the corrected conclusion in one sentence.

**Why this error is common:** Students learn measurement probabilities in the computational basis first and conclude the diagonal is "the state," not yet appreciating that the off-diagonal coherences are physical and show up the instant you measure in any other basis.

---

## Part E — Transfer Problem

**The problem:** A spin-1 particle (a qutrit, $d=3$) is prepared in an equal mixture of the three basis states $|m=+1\rangle$, $|m=0\rangle$, $|m=-1\rangle$, each with probability $\tfrac13$.

(a) Write the $3\times3$ density matrix $\hat\rho$.
(b) Compute the purity $\text{Tr}(\hat\rho^2)$.
(c) The chapter states that purity for a $d$-dimensional system ranges from $1$ down to $1/d$ at maximal mixing. Confirm your purity equals the floor $1/d$, and explain in one sentence why this ensemble is maximally mixed.

**Hint (use only if stuck after 10 minutes):** Each $|m\rangle\langle m|$ is a $3\times3$ matrix with a single $1$ on the diagonal. Summing $\tfrac13$ of each gives a multiple of the $3\times3$ identity; $\text{Tr}(\hat\rho^2)$ is then the sum of the squares of the diagonal entries.

**Reflection prompt:**
1. For a qubit the purity floor is $\tfrac12$; for this qutrit it is $\tfrac13$. What happens to the minimum purity as the dimension $d$ grows, and what does that say about how "mixed" a large system can become?
2. The qubit maximally mixed state had Bloch vector $\vec r = \vec 0$. Is there an analogous "zero-vector" geometric picture for the qutrit, and why is it harder to draw?

---

## Part F — Interleaved Review

**F1 — This chapter.** A qubit has density matrix $\hat\rho = \bigl(\begin{smallmatrix}0.7 & 0.3 \\ 0.3 & 0.3\end{smallmatrix}\bigr)$. (a) Verify it is a valid density matrix (trace, Hermiticity, eigenvalue signs). (b) Compute its Bloch vector and purity. (c) Is it pure or mixed?
*Chapter this draws from: 1.*

**F2 — Composite Systems and Entanglement.** The two-qubit product state $|\psi_{AB}\rangle = |0\rangle_A \otimes |{+}\rangle_B$ has joint density matrix $\hat\rho_{AB} = |\psi_{AB}\rangle\langle\psi_{AB}|$. (a) Take the partial trace over $B$ to find $\hat\rho_A$. (b) Compute its purity. (c) Contrast with the chapter's Bell-state result where $\hat\rho_A = \tfrac12\hat I$ — why is $\hat\rho_A$ pure here but mixed there?
*Chapter this draws from: Composite Systems and Entanglement.*

**F3 — Discrimination.** You are handed two qubits and told: qubit X has $\text{Tr}(\hat\rho_X^2) = 1$, qubit Y is one party of a Bell pair. Without further computation, which one is in a pure state, which is in a mixed state, and which (if either) could in principle be a subsystem of a larger entangled system?
*Note to instructor: this problem checks whether the student can use purity as the discriminator between "pure state" and "reduced state of an entangled pair" — the cross-cutting idea linking Chapter 1's purity criterion to Chapter 2's entanglement. A student who computes anything has missed that the answer follows from $\text{Tr}(\hat\rho^2)$ alone.*

**Closing reflection:** Across F1–F3, the single quantity $\text{Tr}(\hat\rho^2)$ told you whether a state was pure, how mixed it was, and whether it could be half of an entangled pair. Write one sentence on why purity, not the diagonal entries, is the right invariant to carry forward.

---

## Instructor Notes

**Common errors:**
- Writing $\langle\hat A\rangle = \langle\psi|\hat A|\psi\rangle$ for a mixed state — there is no single $|\psi\rangle$; only $\text{Tr}(\hat\rho\hat A)$ is correct.
- Confusing $\text{Tr}(\hat\rho^2)$ (the purity) with $[\text{Tr}(\hat\rho)]^2 = 1$; the parentheses change the meaning entirely.
- Building $\hat\rho$ by adding the state vectors instead of the projectors $|\psi_i\rangle\langle\psi_i|$ — a mixture sums outer products, not amplitudes.

**Signs a student needs to return:**
- Their density matrix has trace $\ne 1$ or a negative eigenvalue and they proceed anyway.
- They treat a coherent superposition and a classical mixture with the same diagonal as the same state.

**Scaffolding adjustments:** A student stuck on Part A should first verify the trace of $\hat\rho$ before any other computation — an early trace check catches most assembly errors. A student who finishes Part F quickly should be asked to construct two genuinely different ensembles that yield the same $\hat\rho = \tfrac12\hat I$ and explain why the density matrix cannot distinguish them.

**Domain adaptation note:** For students reconstructing a real Bell-test paper, frame the mixed state as the imperfect experimental resource $\hat\rho(\epsilon) = (1-\epsilon)|\Phi^+\rangle\langle\Phi^+| + \epsilon\,\hat I/4$, where purity quantifies how far the lab state has fallen from the ideal pure Bell state.
