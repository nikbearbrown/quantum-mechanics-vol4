# Worked Exercises: Quantum Gates and Circuits
*Chapter 4 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The unitarity requirement $U^\dagger U = \mathbf{I}$ (preserving $\langle\psi|\psi\rangle$ and inner products), its consequence of reversibility $U^{-1} = U^\dagger$, and the no-cloning theorem ($z = z^2 \Rightarrow z \in \{0,1\}$).
- The gate vocabulary: $H = \tfrac{1}{\sqrt2}\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$, $X = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, $Z = \bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$, $S = \bigl(\begin{smallmatrix}1&0\\0&i\end{smallmatrix}\bigr)$, $T = \bigl(\begin{smallmatrix}1&0\\0&e^{i\pi/4}\end{smallmatrix}\bigr)$, and $\text{CNOT} = \bigl(\begin{smallmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{smallmatrix}\bigr)$ in the basis $\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}$.
- The $H$–CNOT Bell-state preparation circuit, the rule $|x,y\rangle \to |x, x\oplus y\rangle$ for CNOT, and tensor-product gate construction $U_{\text{full}} = U \otimes I$ (acting on $q_0$) or $I \otimes U$ (acting on $q_1$), with $q_0$ the outer (left) tensor factor.

---

## Part A — Full Worked Example

**What this demonstrates:** How a two-gate circuit ($H$ on $q_0$, then CNOT) turns a product input into a maximally entangled Bell state, with unitarity and the reduced state verified at each step.

**The problem:** Starting from $|10\rangle$, apply $H \otimes I$ (Hadamard on $q_0$) then CNOT (control $q_0$, target $q_1$). Trace the state after each gate, identify the resulting Bell state, and confirm that $q_0$'s reduced density matrix becomes $\tfrac12\hat I$.

**The solution:**

**Step 1 — Verify the Hadamard is unitary before using it.**

$$H^\dagger H = \tfrac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \tfrac12\begin{pmatrix}2&0\\0&2\end{pmatrix} = \mathbf{I}.$$

*Why:* Only unitary maps are legal quantum gates — they preserve normalization. A "gate" failing this is not physical.
*Check:* $H^\dagger H = \mathbf{I}$ confirmed; note $H = H^\dagger$, so $H$ is also its own inverse, $H^2 = \mathbf I$.

**Step 2 — Apply $H \otimes I$ to $|10\rangle$.** $H$ acts on $q_0$; $H|1\rangle = |{-}\rangle = \tfrac{1}{\sqrt2}(|0\rangle - |1\rangle)$, and $q_1 = |0\rangle$ is untouched:

$$(H\otimes I)|10\rangle = (H|1\rangle)\otimes|0\rangle = \tfrac{1}{\sqrt2}(|0\rangle - |1\rangle)\otimes|0\rangle = \tfrac{1}{\sqrt2}(|00\rangle - |10\rangle).$$

*Why:* The Hadamard puts the control qubit into a superposition while leaving the target in $|0\rangle$ — the state is still a product, $|{-}\rangle_A\otimes|0\rangle_B$.
*Check:* Amplitudes $\tfrac{1}{\sqrt2}, 0, -\tfrac{1}{\sqrt2}, 0$; norm$^2 = \tfrac12 + \tfrac12 = 1$. Still normalized. The state factors, so no entanglement yet.

**Step 3 — Apply CNOT (control $q_0$, target $q_1$).** CNOT acts as $|x,y\rangle \to |x, x\oplus y\rangle$: it flips $q_1$ only when $q_0 = 1$. On $|00\rangle$ nothing changes; on $|10\rangle \to |11\rangle$:

$$\text{CNOT}\cdot\tfrac{1}{\sqrt2}(|00\rangle - |10\rangle) = \tfrac{1}{\sqrt2}(|00\rangle - |11\rangle) = |\Phi^-\rangle.$$

*Why:* The CNOT is the entangling gate — with the control in superposition, it correlates the target's value with the control's, producing a Bell state.
*Check:* This matches the chapter's Bell-prep table: input $|10\rangle \to |\Phi^-\rangle = (|00\rangle - |11\rangle)/\sqrt2$. Norm$^2 = \tfrac12 + \tfrac12 = 1$.

**Step 4 — Compute $q_0$'s reduced density matrix.** Using $\hat\rho_{q_0}[a,b] = \sum_k \psi[a\cdot2 + k]\,\psi^*[b\cdot2 + k]$ with $\psi = \tfrac{1}{\sqrt2}(1, 0, 0, -1)$ (entries for $|00\rangle,|01\rangle,|10\rangle,|11\rangle$):

$$\hat\rho_{q_0}[0,0] = |\psi_{00}|^2 + |\psi_{01}|^2 = \tfrac12 + 0 = \tfrac12, \quad \hat\rho_{q_0}[1,1] = |\psi_{10}|^2 + |\psi_{11}|^2 = 0 + \tfrac12 = \tfrac12,$$
$$\hat\rho_{q_0}[0,1] = \psi_{00}\psi_{10}^* + \psi_{01}\psi_{11}^* = \tfrac{1}{\sqrt2}\cdot 0 + 0\cdot(-\tfrac{1}{\sqrt2}) = 0.$$

So $\hat\rho_{q_0} = \tfrac12\hat I$.

*Why:* The reduced state of one half of a maximally entangled pair is the maximally mixed state — all information is in the joint correlations, none locally.
*Check:* Purity $\text{Tr}(\hat\rho_{q_0}^2) = \tfrac14 + \tfrac14 = \tfrac12$, the qubit minimum. Bloch vector $\vec r = \vec 0$: the arrow collapses to the origin.

**Step 5 — Confirm reversibility.** Apply the inverse circuit (CNOT then $H\otimes I$, since each is its own inverse) to $|\Phi^-\rangle$: CNOT$\cdot\tfrac{1}{\sqrt2}(|00\rangle - |11\rangle) = \tfrac{1}{\sqrt2}(|00\rangle - |10\rangle)$, then $(H\otimes I)$ returns $|10\rangle$.

*Why:* Every quantum circuit is reversible — running the conjugate-transpose gates in reverse order recovers the input exactly, unlike a classical AND gate.
*Check:* We recover the original $|10\rangle$. Reversibility confirmed.

**Final answer:** $|10\rangle \xrightarrow{H\otimes I} \tfrac{1}{\sqrt2}(|00\rangle - |10\rangle) \xrightarrow{\text{CNOT}} |\Phi^-\rangle = \tfrac{1}{\sqrt2}(|00\rangle - |11\rangle)$, with $\hat\rho_{q_0} = \tfrac12\hat I$.

**What made this work:** The circuit separated cleanly into "create superposition" ($H$) and "entangle" (CNOT). Before the CNOT the state factored as a product, so $q_0$ would have been pure; after the CNOT it could not be factored, and the partial trace returned $\tfrac12\hat I$. The unitarity check in Step 1 and the reversibility check in Step 5 bracket the computation — they confirm we used legal gates and that no information was destroyed, only relocated into entanglement. The minus sign that distinguishes $|\Phi^-\rangle$ from $|\Phi^+\rangle$ came entirely from the $|1\rangle$ in the input $|10\rangle$, propagating through $H|1\rangle = |{-}\rangle$.

**Self-explanation prompt:** Before the CNOT, $q_0$'s reduced state was pure ($|{-}\rangle$); after, it was maximally mixed ($\tfrac12\hat I$). The CNOT is unitary and reversible — so where did $q_0$'s "purity" go, given that no information was destroyed?

---

## Part B — Matched Practice Problem

**The problem:** Starting from $|01\rangle$, apply $H \otimes I$ (Hadamard on $q_0$) then CNOT (control $q_0$, target $q_1$). Identify the resulting Bell state and confirm $q_1$'s reduced density matrix is $\tfrac12\hat I$.

**Step 1 — Verify the Hadamard is unitary before using it.** Show $H^\dagger H = \mathbf I$.

**Step 2 — Apply $H \otimes I$ to $|01\rangle$.** Write the state; confirm it factors and is normalized.

**Step 3 — Apply CNOT (control $q_0$, target $q_1$).** Use $|x,y\rangle \to |x, x\oplus y\rangle$ and identify the Bell state.

**Step 4 — Compute $q_1$'s reduced density matrix.** Use $\hat\rho_{q_1}[a,b] = \sum_k \psi[k\cdot2 + a]\,\psi^*[k\cdot2 + b]$ and show it equals $\tfrac12\hat I$.

**Step 5 — Confirm reversibility.** Run the inverse circuit and recover $|01\rangle$.

**Stuck?** $H|0\rangle = |{+}\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, and $q_1$ starts in $|1\rangle$, so after $H\otimes I$ the state is $\tfrac{1}{\sqrt2}(|01\rangle + |11\rangle)$. The CNOT flips $q_1$ in the $|11\rangle$ term.

*Instructor note: solution intentionally omitted. The input is $|01\rangle$, not $|00\rangle$ — students should land on $|\Psi^+\rangle$ from the chapter's Bell-prep table, not reflexively write $|\Phi^+\rangle$. Note the partial trace is over $q_0$ here ($\hat\rho_{q_1}$), with a different index pattern than Part A.*

---

## Part C — Completion Problem

**The problem:** Verify that the $T$ gate is unitary and compute $T^2$, confirming $T^2 = S$.

**Step 1 — Write the $T$ gate and its conjugate transpose (provided).** $T = \bigl(\begin{smallmatrix}1&0\\0&e^{i\pi/4}\end{smallmatrix}\bigr)$, so $T^\dagger = \bigl(\begin{smallmatrix}1&0\\0&e^{-i\pi/4}\end{smallmatrix}\bigr)$ (transpose and conjugate; the phase flips sign).

**Step 2 — Confirm $T^\dagger T = \mathbf I$ (provided).**

$$T^\dagger T = \begin{pmatrix}1&0\\0&e^{-i\pi/4}\end{pmatrix}\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix} = \begin{pmatrix}1&0\\0&e^{0}\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = \mathbf I.$$

The $T$ gate is unitary.

**Step 3 — Compute $T^2$.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Compare $T^2$ to the phase gate $S = \bigl(\begin{smallmatrix}1&0\\0&i\end{smallmatrix}\bigr)$ and confirm they are equal.**
*Your work here:*
*Why (your explanation):*

**Step 5 — State the gate tower (provided).** Continuing the pattern: $T^2 = S$, $T^4 = (T^2)^2 = S^2 = Z$, and $T^8 = Z^2 = \mathbf I$. The $T$ gate is an eighth-root-of-identity phase rotation by $\pi/4$ radians (NOT 45 in any degree-based code), and it supplies the non-Clifford power that breaks classical simulability.

**Final answer:** $T$ is unitary; $T^2 = \bigl(\begin{smallmatrix}1&0\\0&e^{i\pi/2}\end{smallmatrix}\bigr) = \bigl(\begin{smallmatrix}1&0\\0&i\end{smallmatrix}\bigr) = S$, fitting the tower $T^2 = S$, $T^4 = Z$, $T^8 = \mathbf I$.

**Self-explanation prompt:** The $T$ gate only adds a phase to $|1\rangle$ and does nothing to $|0\rangle$. Why is such an innocent-looking diagonal gate the one that makes a circuit classically hard to simulate, while $H$, $S$, and CNOT together (the Clifford group) are easy?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student proposes a "gate" $G = \bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ to map $|0\rangle \to |0\rangle$ and $|1\rangle \to |0\rangle + |1\rangle$, and reasons about cloning. They write:

**Step 1.** "$G|0\rangle = \bigl(\begin{smallmatrix}1\\0\end{smallmatrix}\bigr) = |0\rangle$ and $G|1\rangle = \bigl(\begin{smallmatrix}1\\1\end{smallmatrix}\bigr) = |0\rangle + |1\rangle$. The gate does what I want."

**Step 2.** "Since $G$ maps basis states to definite outputs, it is a valid quantum gate; I will use it in my circuit."

**Step 3.** ⚠ "Now I can build a cloning machine: feed in an unknown $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ and use $G$-style gates to produce two copies $|\psi\rangle|\psi\rangle$. Quantum gates are flexible enough to copy any state — the no-cloning theorem just means we lack the right circuit, which $G$ supplies."

**Step 4.** Conclusion: "$G$ is a valid gate and enables cloning of arbitrary states."

**Your tasks:**
1. Compute $G^\dagger G$ and show $G$ is NOT unitary, so it is not a valid quantum gate at all.
2. Compute $\langle\psi|\psi\rangle$ before and after applying $G$ to $|1\rangle$ to show $G$ does not preserve normalization.
3. State the no-cloning theorem's actual content (from $\langle\phi|\psi\rangle = \langle\phi|\psi\rangle^2$) and explain why no unitary — valid or not — can clone an arbitrary unknown state.
4. Write the corrected conclusion in two sentences.

**Why this error is common:** Students treat "maps basis states to outputs I like" as the definition of a gate, forgetting that legality requires $U^\dagger U = \mathbf I$, and they underestimate that no-cloning is a theorem about all unitaries, not a missing-circuit problem.

---

## Part E — Transfer Problem

**The problem:** The Deutsch algorithm determines whether $f:\{0,1\}\to\{0,1\}$ is constant or balanced in one oracle query. Trace it for the balanced function $f(x) = x$, whose oracle $U_f: |x\rangle|y\rangle \to |x\rangle|y\oplus f(x)\rangle$ is exactly a CNOT (control $q_0$, target $q_1$).

(a) Start from $q_0 = |0\rangle$, $q_1 = |1\rangle$. Apply $H$ to both qubits and write $|\pi_1\rangle$.
(b) Apply the oracle (CNOT). Using phase kickback $U_f|x\rangle|{-}\rangle = (-1)^{f(x)}|x\rangle|{-}\rangle$, write $|\pi_2\rangle$ for $f(x) = x$.
(c) Apply $H$ to $q_0$ and determine the measurement outcome on $q_0$.
(d) State whether the outcome (0 or 1) correctly identifies $f$ as "constant" or "balanced."

**Hint (use only if stuck after 10 minutes):** After $H\otimes H$ the state is $|{+}\rangle\otimes|{-}\rangle$. For $f(x) = x$, the kickback gives $|0\rangle$ the phase $(-1)^0 = +1$ and $|1\rangle$ the phase $(-1)^1 = -1$, so $q_0 \to \tfrac{1}{\sqrt2}(|0\rangle - |1\rangle) = |{-}\rangle$. Then $H|{-}\rangle = |1\rangle$.

**Reflection prompt:**
1. The speedup did not come from "evaluating $f(0)$ and $f(1)$ at once" — measuring right after the oracle gives a random bit. What role did the final Hadamard play in extracting the answer?
2. Phase kickback wrote the global property $f(0)\oplus f(1)$ into a relative phase between $|0\rangle$ and $|1\rangle$. Why is that relative phase invisible to a direct measurement but visible after interference?

---

## Part F — Interleaved Review

**F1 — This chapter.** Show that $HZH = X$. (a) Compute $HZ$, then $(HZ)H$. (b) Verify the result equals $X$. (c) Interpret geometrically: what does this say about how $H$ relates the $\hat x$ and $\hat z$ axes of the Bloch sphere?
*Chapter this draws from: 4.*

**F2 — Bell's Theorem and the CHSH Inequality.** The $H$–CNOT circuit prepares the Bell state used in every CHSH experiment. (a) Prepare $|\Phi^+\rangle$ from $|00\rangle$ via $H$ then CNOT, tracing each step. (b) For this $|\Phi^+\rangle$, recall the correlation $E(\hat a,\hat b) = \cos(\theta_a - \theta_b)$ and state the CHSH value at the optimal angles. (c) Explain in one sentence why the CNOT, not the Hadamard, is the gate that makes a Bell test possible.
*Chapter this draws from: Bell's Theorem and the CHSH Inequality.*

**F3 — Discrimination.** You are shown two $2\times2$ matrices: $M_1 = \tfrac{1}{\sqrt2}\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$ and $M_2 = \bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$. Without doing a full circuit calculation, decide which one is a legal quantum gate and which is not, and name the single property that distinguishes them.
*Note to instructor: this problem checks whether the student uses unitarity (the column-orthonormality / normalization $U^\dagger U = \mathbf I$) as the gate-legality test. $M_2$ has identical columns and cannot be unitary; the $\tfrac{1}{\sqrt2}$ normalization on $M_1$ is exactly what makes it the Hadamard. A student who multiplies out a state evolution has missed that the answer is immediate from the matrix.*

**Closing reflection:** Across F1–F3, unitarity ($U^\dagger U = \mathbf I$) decided gate legality, preserved normalization, and guaranteed reversibility — and it is the same property that forbids cloning. Write one sentence on why this single algebraic condition underlies so many of the chapter's physical facts.

---

## Instructor Notes

**Common errors:**
- Accepting a non-unitary matrix as a gate — failing to check $U^\dagger U = \mathbf I$ before using it.
- Mis-wiring CNOT: using the control-$q_1$ matrix when control is $q_0$, or swapping the truth table so $|10\rangle$ does not map to $|11\rangle$.
- Dropping the $1/\sqrt2$ normalization on the Hadamard, or treating the $T$-gate phase $\pi/4$ as 45 in degree-based code.

**Signs a student needs to return:**
- Their circuit output has norm $\ne 1$ and they continue without noticing.
- They claim a gate can copy an unknown state, treating no-cloning as a hardware limitation rather than a theorem.

**Scaffolding adjustments:** A student stuck on Part A should first confirm each gate is unitary and that the state norm stays 1 after every step — most circuit errors surface as a broken norm. A student who finishes Part F quickly should be asked to find the gate sequence that converts $|\Phi^+\rangle$ into each of the other three Bell states using only single-qubit Pauli gates on $q_0$.

**Domain adaptation note:** For students reconstructing a Bell-test paper, this chapter supplies the apparatus model — the $H$–CNOT prep circuit plus the basis-rotation $R_y$ that implements "measure at angle $\theta$," cross-checked against Chapter 3's correlators by two independent routes (operator expectation vs. gate circuit) at non-canonical angles to catch a hidden factor-of-2.
