# Worked Exercises: Composite Systems and Entanglement
*Chapter 2 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The tensor product $\mathcal{H}_A\otimes\mathcal{H}_B$ of dimension $d_A \times d_B$, the coefficient matrix $C$ with entries $c_{ij}$, and the rank-1 / determinant test: a two-qubit state is a product state iff $\text{rank}(C) = 1$, equivalently $\det(C) = c_{00}c_{11} - c_{01}c_{10} = 0$.
- The Schmidt decomposition $|\psi_{AB}\rangle = \sum_k \sqrt{\lambda_k}\,|u_k\rangle_A|v_k\rangle_B$ from the SVD $C = U\Sigma V^\dagger$; the $\{\lambda_k\}$ are eigenvalues of $C^\dagger C$ and of $\hat\rho_A$, summing to 1.
- The entanglement entropy $S_E = -\sum_k \lambda_k\log_2\lambda_k$, equal to 0 for product states, $1$ ebit for a Bell state, and the four Bell states $|\Phi^\pm\rangle, |\Psi^\pm\rangle$ with their $H$–CNOT preparation.

---

## Part A — Full Worked Example

**What this demonstrates:** That the Schmidt decomposition of a two-qubit state, obtained from the SVD of its coefficient matrix, simultaneously settles whether the state is entangled and exactly how much.

**The problem:** Find the Schmidt decomposition and entanglement entropy of

$$|\psi\rangle = \tfrac{1}{2}|00\rangle - \tfrac{1}{2}|01\rangle + \tfrac{1}{2}|10\rangle + \tfrac{1}{2}|11\rangle.$$

**The solution:**

**Step 1 — Build the coefficient matrix and check the determinant.** Arrange the amplitudes into $C$ with row index $A$, column index $B$:

$$C = \frac{1}{2}\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix}, \qquad \det(C) = \tfrac14(1\cdot1 - (-1)\cdot1) = \tfrac14(1 + 1) = \tfrac12.$$

*Why:* $\det(C)$ is the fastest entanglement test — nonzero determinant means rank 2, hence entangled.
*Check:* Frobenius norm $\|C\|_F^2 = 4\times\tfrac14 = 1$, so the state is normalized. And $\det(C) = \tfrac12 \ne 0$: entangled.

**Step 2 — Compute $C^\dagger C$ and its eigenvalues (the Schmidt coefficients).**

$$C^\dagger C = \frac14\begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix}\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix} = \frac14\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix} = \tfrac12\hat I.$$

So the eigenvalues are $\lambda_1 = \lambda_2 = \tfrac12$.

*Why:* The eigenvalues of $C^\dagger C$ are the Schmidt coefficients $\{\lambda_k\}$ and also the eigenvalues of $\hat\rho_A$; their values determine the entanglement.
*Check:* $\lambda_1 + \lambda_2 = 1$ as required, and both are positive.

**Step 3 — Find the Schmidt vectors via $C|v_k\rangle = \sqrt{\lambda_k}|u_k\rangle$.** Since $C^\dagger C = \tfrac12\hat I$ is degenerate, any orthonormal $\{|v_k\rangle\}$ works; choose $|v_1\rangle_B = |0\rangle$, $|v_2\rangle_B = |1\rangle$.

$$C|0\rangle = \tfrac12\begin{pmatrix}1\\1\end{pmatrix} = \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix} \implies |u_1\rangle_A = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix} = |{+}\rangle.$$

$$C|1\rangle = \tfrac12\begin{pmatrix}-1\\1\end{pmatrix} = \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix} \implies |u_2\rangle_A = \tfrac{1}{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix}.$$

*Why:* The SVD relation maps each right singular vector $|v_k\rangle$ to a left singular vector $|u_k\rangle$ scaled by $\sqrt{\lambda_k}$ — these are the orthonormal Schmidt bases.
*Check:* $\langle u_1|u_2\rangle = \tfrac12(1\cdot(-1) + 1\cdot1) = 0$; orthonormal, good.

**Step 4 — Write the Schmidt form and verify by re-expansion.**

$$|\psi\rangle = \tfrac{1}{\sqrt2}|{+}\rangle_A|0\rangle_B + \tfrac{1}{\sqrt2}\,\tfrac{1}{\sqrt2}\!\begin{pmatrix}-1\\1\end{pmatrix}_{\!A}|1\rangle_B.$$

Expand: $\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}(|0\rangle+|1\rangle)_A|0\rangle_B + \tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}(-|0\rangle+|1\rangle)_A|1\rangle_B = \tfrac12(|00\rangle + |10\rangle - |01\rangle + |11\rangle)$.

*Why:* Re-expanding confirms the Schmidt vectors and coefficients reproduce the original amplitudes — the decomposition is only correct if this matches.
*Check:* $\tfrac12(|00\rangle - |01\rangle + |10\rangle + |11\rangle)$ — identical to the original state. Confirmed.

**Step 5 — Compute the entanglement entropy.**

$$S_E = -\tfrac12\log_2\tfrac12 - \tfrac12\log_2\tfrac12 = \tfrac12 + \tfrac12 = 1 \text{ ebit.}$$

*Why:* $S_E$ is the von Neumann entropy of the Schmidt coefficients; equal coefficients give the maximum, 1 ebit for two qubits.
*Check:* $\log_2\tfrac12 = -1$, so each term is $-\tfrac12(-1) = \tfrac12$. Sum is 1 ebit — maximal entanglement, consistent with $\det(C) = \tfrac12$ at its maximum magnitude.

**Final answer:** Schmidt rank 2 with $\lambda_1 = \lambda_2 = \tfrac12$, $S_E = 1$ ebit. The state is maximally entangled — a Bell state in disguise, related to $|\Phi^+\rangle$ by a local unitary on qubit $A$.

**What made this work:** The whole analysis reduced to one SVD. The determinant flagged entanglement, the eigenvalues of $C^\dagger C$ gave the Schmidt coefficients, and the von Neumann formula turned those into a single number of ebits. The internal consistency was tight: $\det(C) = \tfrac12$ (maximum magnitude for a normalized two-qubit state), equal Schmidt coefficients, and $S_E = 1$ all say the same thing three ways. The re-expansion in Step 4 is the load-bearing check — it is the only place where a wrong Schmidt vector would reveal itself.

**Self-explanation prompt:** Why did the degeneracy $\lambda_1 = \lambda_2$ give you freedom to choose $|v_1\rangle, |v_2\rangle$ freely, and why does the entanglement entropy come out the same no matter which orthonormal pair you pick?

---

## Part B — Matched Practice Problem

**The problem:** Find the Schmidt decomposition and entanglement entropy of

$$|\psi\rangle = \tfrac{1}{\sqrt2}|00\rangle + \tfrac{1}{\sqrt2}|11\rangle \quad\text{after a local twist:}\quad |\chi\rangle = \tfrac{\sqrt3}{2}|01\rangle + \tfrac{1}{2}|10\rangle.$$

Use $|\chi\rangle$.

**Step 1 — Build the coefficient matrix and check the determinant.** Form $C$ and compute $\det(C)$; decide entangled or separable.

**Step 2 — Compute $C^\dagger C$ and its eigenvalues.** Find the Schmidt coefficients $\{\lambda_k\}$ and confirm they sum to 1.

**Step 3 — Find the Schmidt vectors via $C|v_k\rangle = \sqrt{\lambda_k}|u_k\rangle$.** Identify $|u_k\rangle_A$ and $|v_k\rangle_B$.

**Step 4 — Write the Schmidt form and verify by re-expansion.** Confirm it reproduces $|\chi\rangle$.

**Step 5 — Compute the entanglement entropy.** Evaluate $S_E$ and state whether the state is maximally or partially entangled.

**Stuck?** The amplitudes sit in the off-diagonal positions $c_{01}$ and $c_{10}$, so $C = \bigl(\begin{smallmatrix}0 & \sqrt3/2 \\ 1/2 & 0\end{smallmatrix}\bigr)$. This $C$ is already "anti-diagonal" — its singular values are the magnitudes of its two nonzero entries.

*Instructor note: solution intentionally omitted. The Schmidt coefficients here are NOT equal — students should expect $S_E < 1$ ebit and resist forcing a Bell-state answer.*

---

## Part C — Completion Problem

**The problem:** Determine whether $|\psi\rangle = \tfrac{1}{\sqrt2}|00\rangle + \tfrac{i}{\sqrt2}|11\rangle$ is entangled, find its Schmidt decomposition, and compute $S_E$.

**Step 1 — Build the coefficient matrix and check the determinant (provided).**

$$C = \tfrac{1}{\sqrt2}\begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix}, \qquad \det(C) = \tfrac12(1\cdot i - 0) = \tfrac{i}{2} \ne 0.$$

Entangled (the complex determinant is nonzero; $|\det C| = \tfrac12$).

**Step 2 — Compute $C^\dagger C$ and its eigenvalues (provided).**

$$C^\dagger C = \tfrac12\begin{pmatrix}1 & 0 \\ 0 & -i\end{pmatrix}\begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix} = \tfrac12\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} = \tfrac12\hat I, \quad \lambda_1 = \lambda_2 = \tfrac12.$$

**Step 3 — Find the Schmidt vectors via $C|v_k\rangle = \sqrt{\lambda_k}|u_k\rangle$.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Write the Schmidt form and verify by re-expansion.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Compute the entanglement entropy (provided).** With $\lambda_1 = \lambda_2 = \tfrac12$,

$$S_E = -\tfrac12\log_2\tfrac12 - \tfrac12\log_2\tfrac12 = 1 \text{ ebit.}$$

**Final answer:** Entangled, $\det(C) = i/2$, Schmidt coefficients $\tfrac12, \tfrac12$, $S_E = 1$ ebit — maximally entangled, with the relative phase $i$ carried by the Schmidt vector $|v_2\rangle_B$ (or $|u_2\rangle_A$), not by the entropy.

**Self-explanation prompt:** The factor $i$ appears in the state but $S_E = 1$ exactly, the same as for the real $|\Phi^+\rangle$. Where in the Schmidt decomposition does the phase $i$ end up, and why does it leave the entanglement entropy untouched?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student is asked whether $|\psi\rangle = \tfrac12|00\rangle + \tfrac12|01\rangle + \tfrac12|10\rangle + \tfrac12|11\rangle$ is entangled. They write:

**Step 1.** Coefficient matrix: $C = \tfrac12\bigl(\begin{smallmatrix}1 & 1 \\ 1 & 1\end{smallmatrix}\bigr)$.

**Step 2.** "The state has all four basis kets present with equal weight, and it looks just like the maximally entangled Bell-type states in the chapter, which also spread weight across the computational basis."

**Step 3.** ⚠ "Because the state is an equal superposition of all four basis states and resembles a Bell state, it is entangled. I will report $S_E = 1$ ebit by analogy with $|\Phi^+\rangle$."

**Step 4.** Conclusion: "Entangled, $S_E = 1$ ebit."

**Your tasks:**
1. Compute $\det(C)$ for this state and state what it tells you about entanglement.
2. Show that $|\psi\rangle$ actually factors as a product $|a\rangle_A \otimes |b\rangle_B$, and identify $|a\rangle$ and $|b\rangle$.
3. Compute the true Schmidt rank and the correct $S_E$.
4. Write the corrected conclusion in one sentence, explaining why "all four basis states with equal weight" does not imply entanglement.

**Why this error is common:** Students associate "spread across the computational basis" with entanglement, but separability is decided by the rank of $C$ — and an equal superposition can be a perfectly factorable $|{+}\rangle_A\otimes|{+}\rangle_B$.

---

## Part E — Transfer Problem

**The problem:** Consider the three-qubit GHZ state $|\text{GHZ}\rangle = \tfrac{1}{\sqrt2}(|000\rangle + |111\rangle)$. Analyze the entanglement across the bipartition $A = \{\text{qubit 1}\}$ versus $BC = \{\text{qubits 2, 3}\}$.

(a) Write the $2\times4$ coefficient matrix $C$ for this cut (rows indexed by qubit 1, columns by the four states of qubits 2 and 3).
(b) Compute $C C^\dagger$ (a $2\times2$ matrix), find its eigenvalues — these are the Schmidt coefficients $\{\lambda_k\}$ — and confirm Schmidt rank.
(c) Compute the entanglement entropy $S_E(A:BC)$ in ebits.

**Hint (use only if stuck after 10 minutes):** Only the columns corresponding to $|00\rangle_{BC}$ and $|11\rangle_{BC}$ are nonzero, each carrying amplitude $\tfrac{1}{\sqrt2}$. So $C$ has just two nonzero entries and $C C^\dagger$ is diagonal.

**Reflection prompt:**
1. For the GHZ state, $S_E(A:BC) = 1$ ebit. If you instead trace out the single qubit $A$, what does the reduced state of the pair $BC$ look like, and is it still entangled within itself? (Try measuring qubit $A$ and see what happens to $BC$.)
2. How does the bipartite Schmidt approach here generalize the two-qubit method of Part A — what changed, and what stayed the same?

---

## Part F — Interleaved Review

**F1 — This chapter.** For $|\psi\rangle = \cos\theta\,|00\rangle + \sin\theta\,|11\rangle$ with $\theta = \pi/6$: (a) write $C$ and find the Schmidt coefficients; (b) compute $S_E$; (c) state whether this is more or less entangled than the $\theta = \pi/4$ case and why.
*Chapter this draws from: 2.*

**F2 — Mixed States and the Density Matrix.** Take the same state $|\psi\rangle = \cos\theta|00\rangle + \sin\theta|11\rangle$ with $\theta = \pi/6$. (a) Compute the reduced density matrix $\hat\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|)$ by partial trace. (b) Compute its purity $\text{Tr}(\hat\rho_A^2)$. (c) Verify the eigenvalues of $\hat\rho_A$ equal the Schmidt coefficients from F1.
*Chapter this draws from: Mixed States and the Density Matrix.*

**F3 — Discrimination.** You are given two two-qubit states: state P has $\det(C) = 0$; state Q has reduced density matrix $\hat\rho_A = \tfrac12\hat I$. Without further calculation, classify each as product, partially entangled, or maximally entangled, and say which test (determinant, purity of reduced state) you used for each.
*Note to instructor: this problem checks whether the student recognizes that $\det(C) = 0$ and $\hat\rho_A = \tfrac12\hat I$ are two faces of the same Schmidt-rank idea — rank 1 vs. maximally degenerate. A student who runs a full SVD has missed that both answers are immediate.*

**Closing reflection:** Across F1–F3, the Schmidt coefficients of a pure bipartite state appeared as eigenvalues of $C^\dagger C$, as eigenvalues of the reduced $\hat\rho_A$, and as the thing that determines both $S_E$ and the purity. Write one sentence on why these are all the same set of numbers.

---

## Instructor Notes

**Common errors:**
- Calling a state entangled because it "looks spread out" without computing $\det(C)$ or the Schmidt rank — an equal superposition can be a product state.
- Taking the partial trace incorrectly, e.g. tracing the wrong subsystem or dropping the requirement $\langle m|j\rangle\langle l|n\rangle$ that kills off-diagonal terms.
- Forgetting the convention $0\log_2 0 = 0$, producing a NaN for product states whose Schmidt coefficient is zero.

**Signs a student needs to return:**
- Their Schmidt coefficients do not sum to 1, or they report a negative coefficient.
- They claim a reduced state of a Bell-type pure state is pure rather than $\tfrac12\hat I$.

**Scaffolding adjustments:** A student stuck on Part A should first verify $\|C\|_F^2 = 1$ and compute $\det(C)$ before attempting the full SVD — the determinant alone answers "is it entangled." A student who finishes Part F quickly should be asked to construct a partially entangled two-qubit state with a target value such as $S_E = 0.5$ ebit and confirm it by SVD.

**Domain adaptation note:** For students reconstructing a Bell-test or entanglement paper, this is the system-identification step — use $\det(C)$, Schmidt rank, and $S_E$ to confirm which of the four Bell states the paper produces and that it is genuinely maximally entangled, fixing the correlation-function sign that propagates into the CHSH calculation.
