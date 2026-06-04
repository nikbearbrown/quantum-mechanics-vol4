# Chapter 2 — Composite Systems and Entanglement

## TL;DR

Two qubits together live in a four-dimensional space, not two two-dimensional spaces. Most states in that four-dimensional space cannot be written as a product of single-qubit states — those are the entangled ones. The algebraic test for entanglement is the Schmidt decomposition: express the state as a sum $\sum_k \sqrt{\lambda_k}\,|u_k\rangle_A|v_k\rangle_B$ and count the terms. One term means separable. More than one means entangled. The Bell states are the four canonical examples of two-qubit entanglement, each with exactly two Schmidt terms of equal weight. The entanglement entropy — $-\sum_k \lambda_k \log_2 \lambda_k$ — quantifies how much entanglement there is, from zero for product states to one ebit for the Bell states.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **Construct** the Hilbert space of a composite two-qubit system as a tensor product and identify its basis states. *(Remember/Understand)*
2. **Distinguish** separable from entangled pure states using the factorization test and the Schmidt rank. *(Understand)*
3. **Write** the four Bell states and verify each is maximally entangled by computing the reduced density matrix of either qubit. *(Apply)*
4. **Perform** the Schmidt decomposition of a two-qubit pure state by expressing it as an SVD of the coefficient matrix. *(Apply)*
5. **Compute** the entanglement entropy of a bipartite pure state and interpret it in ebits. *(Analyze)*

---

## Opening: the failure of a reasonable assumption

You have two spin-$\frac{1}{2}$ particles, each described by a two-dimensional Hilbert space. A physicist friend tells you that the joint state of the two particles should be described by a four-component object — two components per particle. That sounds right. Two particles, each with two degrees of freedom; surely the joint system just takes two independent state vectors and stacks them.

It does not.

The joint Hilbert space is not a direct sum of two two-dimensional spaces. It is a tensor product: a four-dimensional space in which most states are not the product of any two single-particle states. The extra room in that four-dimensional space is where entanglement lives. And the states that fill that extra room — the entangled states — are, in a precise sense, more typical than the product states. If you pick a random unit vector in $\mathbb{C}^4$, almost surely it is entangled.

This chapter is about the geometry of that space. What does the tensor product give you? Which states are entangled and which are not? How do you compute the answer? And how much entanglement does a state carry?

---

## Core development

### The tensor product and the composite Hilbert space

Let system $A$ have Hilbert space $\mathcal{H}_A = \text{span}\{|0\rangle_A, |1\rangle_A\}$ (a qubit) and system $B$ have $\mathcal{H}_B = \text{span}\{|0\rangle_B, |1\rangle_B\}$ (another qubit). The joint system lives in the **tensor product** space:

$$\mathcal{H}_A \otimes \mathcal{H}_B = \text{span}\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\},$$

where $|ij\rangle$ is shorthand for $|i\rangle_A \otimes |j\rangle_B$. The dimension is $2 \times 2 = 4$.

A general state is:

$$|\psi_{AB}\rangle = \sum_{i,j \in \{0,1\}} c_{ij}\,|ij\rangle = c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle,$$

with the normalization $\sum_{i,j}|c_{ij}|^2 = 1$.

The **coefficient matrix** $C = \begin{pmatrix}c_{00} & c_{01} \\ c_{10} & c_{11}\end{pmatrix}$ encodes everything. It is a $2 \times 2$ complex matrix of unit Frobenius norm. Almost everything interesting about the state — including whether it is entangled and how much — is determined by the singular values of $C$.

> **Dimension clarification.** The dimension of $\mathcal{H}_A \otimes \mathcal{H}_B$ is the *product* $d_A \times d_B$, not the sum $d_A + d_B$. For two qubits: $2 \times 2 = 4$, not $2 + 2 = 4$ (though the numbers happen to coincide here). For a qubit and a qutrit: $2 \times 3 = 6$, not $2 + 3 = 5$. The difference matters physically: a $d_A + d_B$-dimensional description would be a direct sum, describing two particles that do not interact and share no correlations whatsoever. Tensor product gives them the ability to be correlated.

### Product states and separable states

A state $|\psi_{AB}\rangle$ is called a **product state** (or **separable pure state**) if it factors as:

$$|\psi_{AB}\rangle = |a\rangle_A \otimes |b\rangle_B \qquad \text{for some } |a\rangle \in \mathcal{H}_A, \; |b\rangle \in \mathcal{H}_B.$$

If $|a\rangle = \alpha|0\rangle + \beta|1\rangle$ and $|b\rangle = \gamma|0\rangle + \delta|1\rangle$, then:

$$|a\rangle \otimes |b\rangle = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle.$$

The coefficient matrix of a product state is:

$$C_{\text{sep}} = \begin{pmatrix}\alpha\gamma & \alpha\delta \\ \beta\gamma & \beta\delta\end{pmatrix} = \begin{pmatrix}\alpha \\ \beta\end{pmatrix}\begin{pmatrix}\gamma & \delta\end{pmatrix}.$$

This is a **rank-1 matrix**: it equals the outer product of two vectors. Conversely, the coefficient matrix of any product state is rank 1.

Therefore: $|\psi_{AB}\rangle$ is a product state if and only if $\text{rank}(C) = 1$.

### Entangled states: the factorization test

If $\text{rank}(C) > 1$, the state is **entangled** — it cannot be written as a product of single-qubit states. The algebraic test is immediate: compute $\det(C)$ (or more generally, the rank of $C$). For two qubits:

$$\det(C) = c_{00}c_{11} - c_{01}c_{10}.$$

If $\det(C) \neq 0$, then $C$ has rank 2, and the state is entangled. This is the fastest computational test.

**Example.** Let $|\psi\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$. Then $C = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$, and $\det(C) = \tfrac{1}{2} \neq 0$. Entangled.

**Example.** Let $|\phi\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = |{+}\rangle_A \otimes |0\rangle_B$. Then $C = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 1 & 0\end{pmatrix}$, and $\det(C) = 0$. Separable — and indeed, $|{+}\rangle \otimes |0\rangle$ is a product state.

### The Bell states

The four **Bell states** are the canonical orthonormal basis of maximally entangled two-qubit states:

$$|\Phi^\pm\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle \pm |11\rangle\bigr), \qquad |\Psi^\pm\rangle = \frac{1}{\sqrt{2}}\bigl(|01\rangle \pm |10\rangle\bigr).$$

Their coefficient matrices are proportional to the identity or Pauli matrices, all with rank 2 — all maximally entangled.

For each Bell state, the reduced density matrix of either qubit is $\hat\rho_{A} = \tfrac{1}{2}\hat I$ (the maximally mixed state). This was derived in Chapter 1 for $|\Phi^+\rangle$; the same calculation applies to all four Bell states. The consequence: no single-qubit measurement distinguishes between the Bell states. All the information is in the joint correlations.

The singlet state $|\Psi^-\rangle = \tfrac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ is rotationally invariant: $(U \otimes U)|\Psi^-\rangle = (\det U)|\Psi^-\rangle$ for any $U \in SU(2)$. Its correlations depend only on the angle between measurement axes: $E(\hat a, \hat b) = -\hat a \cdot \hat b$.

**Preparing a Bell state.** Starting from $|00\rangle$, the recipe for $|\Phi^+\rangle$ uses two gates:

$$|00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = |{+}\rangle_A \otimes |0\rangle_B \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle.$$

After the Hadamard, the state is still separable — a product. The CNOT creates the entanglement. The Bloch vectors of $A$ and $B$, which point to the north pole before the circuit, collapse to the center (the origin, $\vec r = 0$) after the CNOT, reflecting that each qubit alone is maximally mixed.

Starting from $|01\rangle$, $|10\rangle$, $|11\rangle$ and applying the same circuit gives $|\Psi^+\rangle$, $|\Psi^-\rangle$, $|\Phi^-\rangle$ respectively. The full table:

| Initial state | After $H \otimes I$ | After CNOT | Bell state |
|:---:|:---:|:---:|:---:|
| $|00\rangle$ | $|{+}\rangle|0\rangle$ | $|\Phi^+\rangle$ | $(|00\rangle + |11\rangle)/\sqrt{2}$ |
| $|01\rangle$ | $|{+}\rangle|1\rangle$ | $|\Psi^+\rangle$ | $(|01\rangle + |10\rangle)/\sqrt{2}$ |
| $|10\rangle$ | $|{-}\rangle|0\rangle$ | $|\Phi^-\rangle$ | $(|00\rangle - |11\rangle)/\sqrt{2}$ |
| $|11\rangle$ | $|{-}\rangle|1\rangle$ | $|\Psi^-\rangle$ | $(|01\rangle - |10\rangle)/\sqrt{2}$ |

### The Schmidt decomposition

The factorization-rank test works for two qubits but does not generalize gracefully to higher dimensions. The tool that generalizes is the **Schmidt decomposition**, which rests on the singular value decomposition (SVD) of the coefficient matrix.

**Theorem (Schmidt).** Any pure bipartite state $|\psi_{AB}\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ can be written as:

$$|\psi_{AB}\rangle = \sum_{k=1}^{r} \sqrt{\lambda_k}\,|u_k\rangle_A \otimes |v_k\rangle_B,$$

where $\{|u_k\rangle\}$ is an orthonormal set in $\mathcal{H}_A$, $\{|v_k\rangle\}$ is an orthonormal set in $\mathcal{H}_B$, $\lambda_k > 0$, $\sum_k \lambda_k = 1$, and $r \leq \min(\dim \mathcal{H}_A, \dim \mathcal{H}_B)$ is the **Schmidt rank**.

**Derivation.** The coefficient matrix $C$ has a singular value decomposition: $C = U\Sigma V^\dagger$, where $U$ is unitary on $\mathcal{H}_A$, $V$ is unitary on $\mathcal{H}_B$, and $\Sigma = \text{diag}(\sqrt{\lambda_1}, \sqrt{\lambda_2}, \ldots)$ contains the singular values. Define new orthonormal bases by $|u_k\rangle_A = \sum_i U_{ik}|i\rangle_A$ and $|v_k\rangle_B = \sum_j V_{jk}|j\rangle_B$. Substituting gives the Schmidt form. The Schmidt coefficients $\sqrt{\lambda_k}$ are the singular values of $C$; the Schmidt vectors are the corresponding singular vectors. The coefficients $\{\lambda_k\}$ are the eigenvalues of the reduced density matrix $\hat\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|)$ — and also of $\hat\rho_B$.

**Entanglement criterion from Schmidt rank:**
- Schmidt rank $= 1$: product state. Exactly one term; $|u_1\rangle_A|v_1\rangle_B$ is the factored form.
- Schmidt rank $\geq 2$: entangled.

This is the most powerful single diagnostic. For any pure bipartite state, you do not need to try all possible factorizations; you compute one SVD.

### Entanglement entropy

The **Schmidt coefficients** $\{\lambda_k\}$ quantify *how much* entanglement a state carries. The canonical scalar measure is the **entanglement entropy** (von Neumann entropy of the reduced state):

$$S_E = -\sum_k \lambda_k \log_2 \lambda_k = -\text{Tr}(\hat\rho_A \log_2 \hat\rho_A).$$

Properties:
- $S_E = 0$ for product states (one $\lambda_k = 1$, all others $0$; $0 \log 0 \equiv 0$).
- $S_E = \log_2 r$ at maximum, achieved when all $r$ Schmidt coefficients are equal: $\lambda_k = 1/r$.
- For a two-qubit state ($r \leq 2$), the maximum is $\log_2 2 = 1$ **ebit**, achieved by the four Bell states.
- Partially entangled states have $0 < S_E < 1$ ebit.

The entanglement entropy is the unique measure of entanglement for pure bipartite states under the axioms of LOCC (local operations and classical communication) monotonicity. If you can distill or dilute entanglement using only local operations and classical communication, $S_E$ is the rate at which Bell pairs convert into the state or vice versa.

---

## Worked example: Schmidt-decompose a two-qubit state and read off entanglement

**The state.** Consider:

$$|\psi\rangle = \frac{1}{2}|00\rangle + \frac{1}{2}|01\rangle + \frac{1}{2}|10\rangle - \frac{1}{2}|11\rangle.$$

**Step 1: Write the coefficient matrix.**

$$C = \begin{pmatrix}c_{00} & c_{01} \\ c_{10} & c_{11}\end{pmatrix} = \frac{1}{2}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}.$$

Verify normalization: $\|C\|_F^2 = \sum_{ij}|c_{ij}|^2 = 4 \cdot \tfrac{1}{4} = 1$. Good.

**Step 2: Compute $C^\dagger C$.**

$$C^\dagger C = \frac{1}{4}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}^\dagger \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix} = \frac{1}{4}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix} = \frac{1}{4}\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix} = \frac{1}{2}\hat I.$$

**Step 3: Find the eigenvalues $\lambda_k$.**

$C^\dagger C = \tfrac{1}{2}\hat I$ has eigenvalues $\lambda_1 = \lambda_2 = \tfrac{1}{2}$.

**Step 4: Find the singular vectors.**

Since $C^\dagger C = \tfrac{1}{2}\hat I$, every vector is an eigenvector. We can choose any orthonormal pair. Take $V = \hat I$ (the identity), so $|v_1\rangle_B = |0\rangle$, $|v_2\rangle_B = |1\rangle$.

The left singular vectors come from $C|v_k\rangle = \sqrt{\lambda_k}|u_k\rangle$:

$$C|0\rangle = \frac{1}{2}\begin{pmatrix}1 \\ 1\end{pmatrix} = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ 1\end{pmatrix} \implies |u_1\rangle_A = \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ 1\end{pmatrix} = |{+}\rangle.$$

$$C|1\rangle = \frac{1}{2}\begin{pmatrix}1 \\ -1\end{pmatrix} = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ -1\end{pmatrix} \implies |u_2\rangle_A = \frac{1}{\sqrt{2}}\begin{pmatrix}1 \\ -1\end{pmatrix} = |{-}\rangle.$$

**Step 5: Write the Schmidt decomposition.**

$$|\psi\rangle = \frac{1}{\sqrt{2}}\,|{+}\rangle_A|0\rangle_B + \frac{1}{\sqrt{2}}\,|{-}\rangle_A|1\rangle_B.$$

Verify by expanding: $\tfrac{1}{\sqrt{2}}\cdot\tfrac{1}{\sqrt{2}}|00\rangle + \tfrac{1}{\sqrt{2}}\cdot\tfrac{1}{\sqrt{2}}|10\rangle + \tfrac{1}{\sqrt{2}}\cdot\tfrac{1}{\sqrt{2}}|01\rangle - \tfrac{1}{\sqrt{2}}\cdot\tfrac{1}{\sqrt{2}}|11\rangle = \tfrac{1}{2}|00\rangle + \tfrac{1}{2}|01\rangle + \tfrac{1}{2}|10\rangle - \tfrac{1}{2}|11\rangle$. Confirmed.

**The lesson.** Schmidt rank $= 2$, so the state is **entangled**. The Schmidt coefficients are $\lambda_1 = \lambda_2 = \tfrac{1}{2}$, equal — so the entanglement entropy is:

$$S_E = -\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2} = 1 \text{ ebit.}$$

This state is **maximally entangled** for two qubits — it carries the same amount of entanglement as a Bell state (and in fact is equivalent to a Bell state up to local unitaries: the Schmidt decomposition $|{+}\rangle|0\rangle + |{-}\rangle|1\rangle$ relates to the Bell basis by a local rotation on qubit $A$).

**The limit.** Now consider the partially entangled state $|\chi\rangle = \tfrac{\sqrt{3}}{2}|00\rangle + \tfrac{1}{2}|11\rangle$. The coefficient matrix is $C = \begin{pmatrix}\sqrt{3}/2 & 0 \\ 0 & 1/2\end{pmatrix}$, already diagonal. Schmidt rank $= 2$ (both diagonal entries nonzero), so entangled. Schmidt coefficients: $\lambda_1 = 3/4$, $\lambda_2 = 1/4$.

$$S_E = -\frac{3}{4}\log_2\frac{3}{4} - \frac{1}{4}\log_2\frac{1}{4} \approx 0.311 + 0.500 = 0.811 \text{ ebits.}$$

Less than 1 ebit — not maximally entangled. The asymmetric Schmidt coefficients tell you that qubit $A$ leans toward the $|0\rangle$ outcome: more information is available locally, so there is less to gain from the correlations. Entanglement entropy captures exactly this tradeoff.

---

## Common misconceptions

**"Any strongly correlated state is entangled."**
No. The state $\hat\rho = \tfrac{1}{2}|00\rangle\langle 00| + \tfrac{1}{2}|11\rangle\langle 11|$ (a mixed state) is perfectly correlated — measuring $A$ in the $z$-basis tells you the outcome for $B$ with certainty. But it is separable: it is a classical mixture $\tfrac{1}{2}\hat\rho_0 \otimes \hat\rho_0 + \tfrac{1}{2}\hat\rho_1 \otimes \hat\rho_1$, which factors as a convex combination of product states. No Schmidt decomposition of a pure state is involved. The separability of mixed states requires a different criterion (the Peres–Horodecki PPT criterion, which is necessary and sufficient for $2 \times 2$ and $2 \times 3$ systems).

**"The Schmidt decomposition depends on which party is $A$ and which is $B$."**
The Schmidt *coefficients* $\{\lambda_k\}$ are fixed by the state and the bipartition. If you swap the roles of $A$ and $B$, the same singular values appear (now of $C^T$ instead of $C$, but $C$ and $C^T$ have the same singular values). What changes is the labeling of which Schmidt vectors belong to $A$ and which to $B$. The entanglement entropy — which depends only on $\{\lambda_k\}$ — is the same regardless.

**"Schmidt rank 2 tells you how entangled the state is."**
Schmidt rank is binary for the *type* of entanglement (product vs. entangled), but it does not measure the *amount*. Both $|\Phi^+\rangle$ (maximally entangled, $S_E = 1$ ebit) and $|\chi\rangle = \tfrac{\sqrt{3}}{2}|00\rangle + \tfrac{1}{2}|11\rangle$ (partially entangled, $S_E \approx 0.811$ ebits) have Schmidt rank 2. The quantitative measure is the entanglement entropy, not just the rank.

**"You can prepare any entangled state by applying a unitary to a product state."**
True — any state in $\mathcal{H}_A \otimes \mathcal{H}_B$ is reachable from any other by a global unitary. But the important constraint is that entanglement cannot be increased by *local* unitaries (unitaries of the form $U_A \otimes U_B$). Local unitaries change the Schmidt vectors but not the Schmidt coefficients, so they leave $S_E$ unchanged. Creating entanglement requires a genuinely two-body gate — like the CNOT.

**"The four Bell states are the only maximally entangled two-qubit states."**
No. Any state of the form $(U_A \otimes U_B)|\Phi^+\rangle$ is maximally entangled, for any single-qubit unitaries $U_A$, $U_B$. There is a whole two-qubit-parameter family of maximally entangled states, all related by local rotations. The four Bell states are a convenient orthonormal basis for this family, but not its entirety.

---

## Exercises

### Warm-up

1. *[Tests: tensor product dimension, basis states]* System $A$ is a qutrit (three levels: $|0\rangle_A, |1\rangle_A, |2\rangle_A$) and system $B$ is a qubit ($|0\rangle_B, |1\rangle_B$). (a) Write all basis states of $\mathcal{H}_A \otimes \mathcal{H}_B$. (b) What is the dimension of the joint Hilbert space? (c) Is the state $|\psi\rangle = \tfrac{1}{\sqrt{3}}(|00\rangle + |10\rangle + |21\rangle)$ normalized? (d) Write the $3 \times 2$ coefficient matrix $C$ for $|\psi\rangle$. *Difficulty: warm-up.*

2. *[Tests: separability via factorization test, determinant]* For each of the following two-qubit states, determine whether the state is entangled by computing the determinant of the coefficient matrix. Show all work. (a) $|\psi_1\rangle = \tfrac{1}{\sqrt{2}}|00\rangle + \tfrac{1}{\sqrt{2}}|01\rangle$. (b) $|\psi_2\rangle = \tfrac{1}{\sqrt{2}}|00\rangle + \tfrac{1}{\sqrt{2}}|11\rangle$. (c) $|\psi_3\rangle = \tfrac{1}{2}|00\rangle + \tfrac{i}{2}|01\rangle + \tfrac{i}{2}|10\rangle - \tfrac{1}{2}|11\rangle$. *Difficulty: warm-up.*

3. *[Tests: Bell state preparation, CNOT action]* Starting from the computational basis state $|11\rangle$, apply $H \otimes I$ followed by CNOT (control = qubit 0, target = qubit 1). (a) Write the state after each gate. (b) Identify the resulting Bell state. (c) Compute the coefficient matrix and verify its determinant is nonzero. *Difficulty: warm-up.*

### Application

4. *[Tests: Schmidt decomposition, SVD procedure]* Find the Schmidt decomposition of $|\psi\rangle = \tfrac{1}{\sqrt{2}}|00\rangle + \tfrac{i}{\sqrt{2}}|11\rangle$. (a) Write the coefficient matrix $C$. (b) Compute $C^\dagger C$ and find its eigenvalues $\lambda_k$. (c) Find the Schmidt vectors $|u_k\rangle_A$ and $|v_k\rangle_B$. (d) Write the Schmidt form. (e) Compute the entanglement entropy. *Difficulty: application.*

5. *[Tests: entanglement entropy, partial entanglement]* A two-qubit state has Schmidt decomposition $|\psi\rangle = \cos\theta\,|00\rangle + \sin\theta\,|11\rangle$ for $\theta \in [0, \pi/4]$. (a) Compute the entanglement entropy $S_E(\theta) = -\cos^2\theta\,\log_2(\cos^2\theta) - \sin^2\theta\,\log_2(\sin^2\theta)$. (b) At what value of $\theta$ is $S_E$ maximized? What is the maximum? (c) Evaluate $S_E$ at $\theta = 0$, $\theta = \pi/6$, and $\theta = \pi/4$. (d) Explain in one sentence why $\theta = \pi/4$ gives the most entanglement. *Difficulty: application.*

6. *[Tests: reduced density matrix from Schmidt decomposition, purity]* For the state $|\psi\rangle = \tfrac{\sqrt{3}}{2}|00\rangle + \tfrac{1}{2}|11\rangle$, (a) compute the reduced density matrix $\hat\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|)$ directly from the partial trace, (b) verify that its eigenvalues match the Schmidt coefficients $\lambda_1 = 3/4, \lambda_2 = 1/4$, (c) compute the purity $\text{Tr}(\hat\rho_A^2)$, and (d) compute $S_E$ using the eigenvalues. *Difficulty: application.*

### Synthesis and beyond

7. *[Tests: LOCC invariance of entanglement entropy, local unitaries]* (a) Show that applying a local unitary $U_A \otimes I_B$ to a pure state $|\psi\rangle$ does not change the Schmidt coefficients $\{\lambda_k\}$ or the entanglement entropy $S_E$. (b) Argue from this that entanglement cannot be created by local operations alone — not local unitaries, and not local measurements with classical communication (LOCC). (c) Identify which gate in the Bell preparation circuit $H \to \text{CNOT}$ is not a local operation, and explain why it can create entanglement. *Difficulty: synthesis.*

8. *[Tests: multipartite entanglement, beyond two parties; produce]* The **GHZ state** of three qubits is $|\text{GHZ}\rangle = \tfrac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$. (a) Choose the bipartition $A = \{\text{qubit 1}\}$ and $BC = \{\text{qubits 2, 3}\}$. Write the coefficient matrix (this is a $2 \times 4$ matrix). (b) Perform the Schmidt decomposition across this bipartition and compute the entanglement entropy $S_E(A : BC)$. (c) Now choose the bipartition $AB = \{\text{qubits 1, 2}\}$ and $C = \{\text{qubit 3}\}$. Compute $S_E(AB : C)$. (d) The three results $S_E(A:BC)$, $S_E(B:AC)$, $S_E(AB:C)$ together characterize the tripartite entanglement structure of the GHZ state. Report all three and comment on the pattern. *Difficulty: synthesis.*

---

## Still puzzling

Entanglement entropy is the right measure of entanglement for pure bipartite states. For mixed states, no single measure does the same job. The **entanglement of formation** asks how many Bell pairs it takes to prepare a given mixed state on average; the **distillable entanglement** asks how many Bell pairs you can extract from many copies of the state. These two quantities are not equal in general — there is a gap between what entanglement costs to create and what it yields when you try to distill it. For pure states, both measures equal $S_E$. For mixed states, the gap represents entanglement that is locked in the state and cannot be concentrated into Bell pairs by any LOCC procedure. The existence of this bound entanglement — entanglement that cannot be distilled — was proven by the Horodecki family in 1998 and remains one of the stranger features of quantum information theory. It means that entanglement is not a simple resource like energy; you can have it without being able to spend it.

The even harder problem: what is the right definition of entanglement for three or more parties? Three qubits have at least two inequivalent classes of entanglement — the GHZ class $\tfrac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$ and the W class $\tfrac{1}{\sqrt{3}}(|001\rangle + |010\rangle + |100\rangle)$ — which cannot be interconverted by LOCC. For four parties and above, the classification is not complete. The bipartite story is closed; the multipartite story is still being written.

---

## The +1 — Simulation Exercise

### The prompt (paste directly into Claude Code or your preferred LLM coding assistant)

```
Build me a single self-contained HTML file called 03-entanglement-explorer.html using
D3 v7 from a CDN, no other dependencies.

The simulation has three panels stacked vertically in one page (total width 700 px):

PANEL A — State constructor (700 x 200).
Four complex amplitude inputs for c_00, c_01, c_10, c_11.
Each has two text fields: Re and Im parts.
A "Normalize" button rescales so sum |c_ij|^2 = 1.
A state preset dropdown with options:
  |00> (product),  |+>|0> (product),  |Phi+> (Bell), |Phi-> (Bell),
  |Psi+> (Bell), |Psi-> (Bell),
  "Partially entangled (sqrt(3)/2 |00> + 1/2 |11>)",
  "Maximally entangled (not Bell)  (1/2|00> + 1/2|01> + 1/2|10> - 1/2|11>)"
Update all inputs when a preset is selected.

PANEL B — Coefficient matrix visualization (700 x 200).
Draw the 2x2 coefficient matrix C as a grid of four cells.
Each cell shows:
  - A filled square whose area is proportional to |c_ij|^2
    (max area = 50x50 px for |c_ij| = 1).
  - The complex value written as "a + bi" below.
  - An arc showing the phase angle (0 to 2pi, displayed in degrees).
Below the matrix show:
  det(C) = c00*c11 - c01*c10 (real and imaginary parts, 4 decimal places).
  |det(C)| displayed as a number.
  Label in green "SEPARABLE" if |det(C)| < 0.001, else in red "ENTANGLED".

PANEL C — Schmidt decomposition and entanglement entropy (700 x 300).
Compute the SVD of C: C = U * Sigma * V_dagger.
  Sigma diagonal entries are the Schmidt coefficients sqrt(lambda_1), sqrt(lambda_2).
  Display lambda_1 and lambda_2 as bar charts (horizontal bars, 0 to 1 range).
  Below each bar: the numerical value to 4 decimal places.

Display the Schmidt rank: count of lambda_k > 0.001.

Compute and display:
  Entanglement entropy S_E = -sum_k lambda_k * log2(lambda_k) in bits.
    Use the convention 0 * log2(0) = 0.
  Display to 4 decimal places.
  Color code: 0.000 = dark green ("product state"), 1.000 = deep blue
    ("maximally entangled"), intermediate = interpolated color.

Display the Schmidt decomposition in text form:
  |psi> = sqrt(lambda_1) |u_1>_A |v_1>_B + sqrt(lambda_2) |u_2>_A |v_2>_B
  where |u_k> and |v_k> are displayed as 2-component complex vectors
  [Re(u_k[0]) + i Im(u_k[0]), Re(u_k[1]) + i Im(u_k[1])] to 3 decimal places.

Below the Schmidt decomposition show the reduced density matrix rho_A:
  rho_A = sum_k lambda_k |u_k><u_k|
  Display as a 2x2 matrix with entries to 3 decimal places (real and imaginary parts).
  Display Tr(rho_A^2) as the purity.
  Verify Tr(rho_A) = 1.000 to 3 decimal places and display a warning if not.

Physics rules:
1. Normalization: sum |c_ij|^2 must equal 1 within 1e-4 after every computation.
   Display a red warning "NOT NORMALIZED" if violated.
2. SVD must produce non-negative singular values in descending order.
   Verify sqrt(lambda_1) >= sqrt(lambda_2) >= 0.
3. Entanglement entropy must satisfy 0 <= S_E <= log2(2) = 1 for two qubits.
   Display a warning if violated.
4. Purity of rho_A must satisfy 0.5 <= Tr(rho_A^2) <= 1.
   (0.5 for maximally entangled, 1 for product state.)
5. Schmidt rank is 1 if and only if |det(C)| < 1e-3.
   Display a mismatch warning if these two criteria disagree.

Implement the SVD using the Jacobi one-sided SVD algorithm for 2x2 complex matrices,
or use the closed-form formulas for 2x2 SVD. Do NOT import any math library.
For a 2x2 matrix C, the singular values are sqrt of the eigenvalues of C_dagger C.
The eigenvalues of a 2x2 Hermitian matrix [[a,b],[b*,d]] are
  ((a+d) +/- sqrt((a-d)^2 + 4|b|^2)) / 2.
Use these to compute lambda_1, lambda_2 without external SVD routines.
```

### Exploration tasks

1. Select preset $|{\Phi^+}\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$. Read off $|\det(C)|$, the Schmidt coefficients $(\lambda_1, \lambda_2)$, and $S_E$. Confirm that $S_E = 1.000$ ebit. What does the reduced density matrix $\hat\rho_A$ look like?

2. Select preset $|{+}\rangle|{0}\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$ (a product state). Verify that $|\det(C)| = 0$, Schmidt rank $= 1$, and $S_E = 0$. The panel should read "SEPARABLE." Check that $\hat\rho_A$ is a pure state (purity $= 1$).

3. Select "Partially entangled ($\tfrac{\sqrt{3}}{2}|00\rangle + \tfrac{1}{2}|11\rangle$)". Read off $\lambda_1$, $\lambda_2$, and $S_E$. Confirm $S_E \approx 0.811$ ebits. Can you manually adjust the amplitudes to push $S_E$ from this value toward 1 ebit? Which $c_{ij}$ do you need to change?

4. Select preset "Maximally entangled (not Bell) ($\tfrac{1}{2}|00\rangle + \tfrac{1}{2}|01\rangle + \tfrac{1}{2}|10\rangle - \tfrac{1}{2}|11\rangle$)". Verify $S_E = 1.000$ ebit. Read off the Schmidt vectors $|u_1\rangle_A, |u_2\rangle_A$. Identify them as known single-qubit states. Conclude: this state is locally equivalent to a Bell state.

---

## References

- Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. §2.5 (Schmidt decomposition), §2.4 (entanglement), §11.3.1 (entanglement entropy). [verify]
- Preskill, J. Lecture Notes for Physics 219/CS 219: Quantum Information and Computation. Chapter 4 (superposition and entanglement). http://www.theory.caltech.edu/~preskill/ph219/ [verify]
- Horodecki, R., Horodecki, P., Horodecki, M., & Horodecki, K. (2009). Quantum entanglement. *Reviews of Modern Physics*, 81(2), 865–942. https://doi.org/10.1103/RevModPhys.81.865 [verify]
- Bennett, C. H., Bernstein, H. J., Popescu, S., & Schumacher, B. (1996). Concentrating partial entanglement by local operations. *Physical Review A*, 53(4), 2046–2052. https://doi.org/10.1103/PhysRevA.53.2046 [verify]
- Wootters, W. K. (1998). Entanglement of formation of an arbitrary state of two qubits. *Physical Review Letters*, 80(10), 2245–2248. https://doi.org/10.1103/PhysRevLett.80.2245 [verify]
- Wootters, W. K., & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature*, 299, 802–803. https://doi.org/10.1038/299802a0 [verify]
- Hensen, B., Bernien, H., Dréau, A. E., Reiserer, A., Kalb, N., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature*, 526, 682–686. https://doi.org/10.1038/nature15759 [verify]
- Horodecki, M., Horodecki, P., & Horodecki, R. (1998). Mixed-state entanglement and distillation: is there a "bound" entanglement in nature? *Physical Review Letters*, 80(24), 5239–5242. https://doi.org/10.1103/PhysRevLett.80.5239 [verify]
