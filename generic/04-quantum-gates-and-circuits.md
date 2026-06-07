# Chapter 4 — Quantum Gates and Circuits

A quantum gate cannot discard information. Every classical logic gate that discards an input — an AND gate, for example — has two inputs and one output. Rolf Landauer showed in 1961 that erasing one bit costs at least $kT\ln 2$ of energy as heat, not as a limitation of engineering but as a thermodynamic law. A quantum gate, by contrast, is a unitary matrix. Running the circuit backward — applying the conjugate transpose of each gate in reverse order — recovers the original input exactly. Nothing is erased, because unitarity requires that probability sum to 1 at every step.

This reversibility has an important consequence: we cannot copy an unknown quantum state. The impossibility is not a limitation of current hardware; it follows from the mathematics of unitarity.

---

## Why Gates Must Be Unitary

A quantum gate on $n$ qubits is a linear map $U : \mathbb{C}^{2^n} \to \mathbb{C}^{2^n}$. For it to preserve $\langle\psi|\psi\rangle = 1$ for every input state, it must satisfy $U^\dagger U = \mathbf{I}$ — the definition of unitary. Two immediate consequences:

**Reversibility.** $U^{-1} = U^\dagger$. Running the circuit backward recovers the input. No classical AND or OR gate has an inverse; quantum gates always do.

**Inner-product preservation.** $\langle\phi|U^\dagger U|\psi\rangle = \langle\phi|\psi\rangle$. Quantum gates are rigid rotations — they rotate the Bloch sphere without stretching or compressing.

To implement a classical irreversible gate in a quantum circuit, we must add ancilla qubits to store the discarded bits. The Toffoli gate (three-qubit controlled-NOT) provides a universal reversible classical gate set, at the cost of making everything three-input, three-output.

---

## The No-Cloning Theorem

**Theorem** (Wootters and Zurek, 1982; Dieks, 1982). There is no unitary $\hat U$ such that $\hat U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for all $|\psi\rangle$.

**Proof.** Suppose such $\hat U$ exists. Apply it to two states $|\psi\rangle$ and $|\phi\rangle$. Unitarity preserves inner products:

$$\langle\phi|\psi\rangle = \langle\phi|^{\otimes 2}|\psi\rangle^{\otimes 2} = \langle\phi|\psi\rangle^2.$$

A complex number satisfying $z = z^2$ is either 0 or 1. So $\langle\phi|\psi\rangle \in \{0,1\}$ — the states are either orthogonal or identical. No cloner can handle arbitrary unknown states. $\square$

No-cloning is not a technology limitation. Its consequences include: eavesdropping on a quantum channel requires measuring, which disturbs the state and can be detected. Quantum error correction cannot use simple copying and must hide information in entanglement instead. No-cloning also enforces no-signaling: if Bob could clone his half of a Bell pair and measure in many bases, he could infer Alice's setting — but cloning is impossible.

---

## Single-Qubit Gates as Bloch-Sphere Rotations

Every single-qubit unitary is, up to a global phase, a rotation of the Bloch sphere. A rotation by angle $\alpha$ about axis $\hat n = (n_x, n_y, n_z)$:

$$R_{\hat n}(\alpha) = \cos\!\left(\frac{\alpha}{2}\right)\mathbf{I} - i\sin\!\left(\frac{\alpha}{2}\right)(n_x\sigma_x + n_y\sigma_y + n_z\sigma_z).$$

The standard gate vocabulary:

**Pauli gates** ($\pi$-rotations about the named axis):

$$X = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \quad Y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \quad Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

$X$ is the quantum NOT: $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$. $Z$ applies a phase flip: $Z|1\rangle = -|1\rangle$. Each Pauli squares to the identity.

**Hadamard gate:**

$$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

$H|0\rangle = |{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, $H|1\rangle = |{-}\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$. Geometrically: a $\pi$-rotation about the $(\hat x + \hat z)/\sqrt{2}$ axis, which swaps the $x$- and $z$-axes of the Bloch sphere. $H^2 = \mathbf{I}$. Also: $HXH = Z$ and $HZH = X$ — Hadamard conjugates $X$ and $Z$ into each other.

**Phase gate** ($S$): $S = \bigl(\begin{smallmatrix}1&0\\0&i\end{smallmatrix}\bigr)$. $S^2 = Z$.

**$T$ gate:** $T = \bigl(\begin{smallmatrix}1&0\\0&e^{i\pi/4}\end{smallmatrix}\bigr)$. $T^2 = S$, $T^4 = Z$, $T^8 = \mathbf{I}$. The $T$ gate is the source of non-Clifford computational power. In fault-tolerant architectures it requires magic state distillation — hundreds of physical qubits per logical $T$ gate — making $T$-count a key resource metric.

**Continuous rotations:**

$$R_z(\theta) = \begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}.$$

Any single-qubit gate decomposes as $e^{i\gamma}R_z(\alpha)R_y(\beta)R_z(\delta)$ for some angles.

---

## The CNOT Gate and Entangling Power

The controlled-NOT (CNOT) gate acts on two qubits: a control and a target. It flips the target if and only if the control is $|1\rangle$. In the basis $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$:

$$\mathrm{CNOT} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.$$

On computational basis states: $|x,y\rangle \to |x, x\oplus y\rangle$ — a classical XOR. $\mathrm{CNOT}^2 = \mathbf{I}$.

The crucial case is when the control is in a superposition:

$$\mathrm{CNOT}\cdot\frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle.$$

CNOT creates entanglement. Starting from the appropriate product state it produces a maximally entangled Bell state. CNOT applied to a basis state performs a classical XOR; entanglement requires a superposed control. The Hadamard that precedes the CNOT in Bell-state preparation is essential.

---

## Universal Gate Sets

A gate set $\mathcal{G}$ is **universal** if every $n$-qubit unitary can be approximated to any desired precision by a finite sequence from $\mathcal{G}$. The canonical example is $\{H, T, \mathrm{CNOT}\}$.

$H$ and $T$ together generate a dense subgroup of $\mathrm{SU}(2)$ — their combinations approximate any single-qubit rotation to arbitrary precision. $\mathrm{CNOT}$ provides two-qubit entangling power. The Solovay-Kitaev theorem guarantees efficiency: any single-qubit gate can be approximated to precision $\varepsilon$ using $O(\log^c(1/\varepsilon))$ gates from this set, where $c \approx 2$.

The **Clifford group** — generated by $\{H, S, \mathrm{CNOT}\}$ — can be efficiently simulated classically (Gottesman-Knill theorem). Adding $T$ breaks classical simulability. This is why $T$ is expensive: it is the gate that provides genuine quantum computational power beyond what a classical computer can efficiently track.

Current hardware fidelities (2024-2025): single-qubit gates routinely exceed 99.9% on superconducting and trapped-ion platforms; two-qubit CNOT gates reach 99–99.5% on superconducting systems and up to 99.9% on trapped-ion systems.

---

## Worked Example 1 — H-CNOT Bell-State Preparation

We apply $H$ to qubit 0, then CNOT with control = qubit 0, target = qubit 1.

**Step 0.** $|\psi_0\rangle = |00\rangle$. Both Bloch vectors at the north pole. Product state.

**Step 1 — $H\otimes I$.** 

$$(H\otimes I)|00\rangle = (H|0\rangle)\otimes|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)\otimes|0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle).$$

Qubit 0 is in $|{+}\rangle$, Bloch vector along $+\hat x$. Qubit 1 is still $|0\rangle$, Bloch vector at north pole. State factorizes. No entanglement.

**Step 2 — CNOT.**

$$\mathrm{CNOT}\cdot\frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle.$$

The state cannot be written as a tensor product. Both Bloch vectors collapse to the origin: each qubit's reduced density matrix is $\hat I/2$, the most mixed single-qubit state. All information is in the joint correlations.

The table of all four Bell states prepared this way:

| Input | After $H\otimes I$ | After CNOT | Bell state |
|-------|---------------------|------------|------------|
| $\|00\rangle$ | $(|00\rangle + |10\rangle)/\sqrt{2}$ | $(|00\rangle + |11\rangle)/\sqrt{2}$ | $|\Phi^+\rangle$ |
| $\|01\rangle$ | $(|01\rangle + |11\rangle)/\sqrt{2}$ | $(|01\rangle + |10\rangle)/\sqrt{2}$ | $|\Psi^+\rangle$ |
| $\|10\rangle$ | $(|00\rangle - |10\rangle)/\sqrt{2}$ | $(|00\rangle - |11\rangle)/\sqrt{2}$ | $|\Phi^-\rangle$ |
| $\|11\rangle$ | $(|01\rangle - |11\rangle)/\sqrt{2}$ | $(|01\rangle - |10\rangle)/\sqrt{2}$ | $|\Psi^-\rangle$ |

Two gates access the entire Bell basis. This is the preparation circuit used in every quantum teleportation experiment, every entanglement-based QKD protocol, and every Bell-test apparatus.

---

## Worked Example 2 — The Deutsch Algorithm

Given a function $f:\{0,1\}\to\{0,1\}$ as a black box, determine whether it is constant ($f(0) = f(1)$) or balanced ($f(0) \neq f(1)$). Classical lower bound: 2 queries. Quantum: 1 query, zero error.

**Setup.** Two qubits: query register $q_0 = |0\rangle$, ancilla $q_1 = |1\rangle$. The oracle $U_f$ implements $|x\rangle|y\rangle \to |x\rangle|y\oplus f(x)\rangle$.

**Circuit.** Apply $H$ to both qubits. Apply $U_f$. Apply $H$ to $q_0$. Measure $q_0$.

**State trace.**

*After $H\otimes H$:*

$$|\pi_1\rangle = |{+}\rangle\otimes|{-}\rangle = \frac{1}{2}(|0\rangle + |1\rangle)(|0\rangle - |1\rangle).$$

*After $U_f$ — phase kickback.* For each basis component $|x\rangle$ of $q_0$ with the ancilla in $|{-}\rangle$:

$$U_f|x\rangle|{-}\rangle = (-1)^{f(x)}|x\rangle|{-}\rangle.$$

The function value $f(x)$ has been kicked back as a phase on the query register. The ancilla is unchanged. Applying to the full superposition:

$$|\pi_2\rangle = \frac{1}{\sqrt{2}}\bigl[(-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\bigr]\otimes|{-}\rangle.$$

*Two cases.* If $f$ is constant: both terms acquire the same phase, so $q_0 \propto |0\rangle + |1\rangle = \sqrt{2}|{+}\rangle$. If $f$ is balanced: the phases are opposite, so $q_0 \propto |0\rangle - |1\rangle = \sqrt{2}|{-}\rangle$.

*After $H$ on $q_0$:* $H|{+}\rangle = |0\rangle$ (constant); $H|{-}\rangle = |1\rangle$ (balanced).

Measure $q_0$: outcome 0 → constant; outcome 1 → balanced.

**Why this works.** The speedup does not come from evaluating $f(0)$ and $f(1)$ simultaneously. Quantum parallelism alone does not help: measuring after the oracle step gives one random value. The advantage comes from **interference**. The oracle writes the comparison $f(0)\oplus f(1)$ into a relative phase between $|0\rangle$ and $|1\rangle$. The final Hadamard converts that relative phase into a distinguishable amplitude. One global property — constant vs. balanced — is extracted from one query. The phase information is invisible to direct measurement but visible after interference.

This is the template for quantum algorithms: superposition evaluates a function on many inputs; interference filters the outputs so the answer has high amplitude and wrong answers cancel.

---

## Grover and Shor at Literacy Level

**Grover's search** (1996): unsorted database of $N$ items, one marked. Classical lower bound $O(N)$; Grover achieves $O(\sqrt{N})$ via amplitude amplification. Quadratic speedup. Threatens symmetric-key cryptography by halving effective key length.

**Shor's factoring** (1994): given large integer $N$, find prime factors. Best classical algorithm runs in sub-exponential time; Shor runs in polynomial time via quantum Fourier transform applied to period-finding. Exponential speedup. Directly threatens RSA and Diffie-Hellman. Neither algorithm will be derived here; their importance is that they establish why universal gate sets are not a theoretical nicety but an engineering imperative.

---

## Open Questions

The Deutsch-Jozsa algorithm extends Deutsch to $n$-bit functions: one quantum query versus $2^{n-1}+1$ deterministic classical queries — an exponential separation. This problem, however, is artificial. Real-world computation rarely encounters functions promised to be constant or balanced.

Simon's algorithm (1994) gives an exponential speedup for a more natural problem, and Shor's algorithm was directly inspired by it. The question of which classically hard problems have quantum speedups — and why — is still being mapped out. BQP, the complexity class of problems efficiently solvable on a quantum computer, sits somewhere between BPP and PSPACE; its relationship to NP is unknown.

A practical consideration for the coming decade: fault-tolerant implementations of Shor require thousands to millions of error-corrected logical qubits. Current hardware has tens to hundreds of noisy physical qubits. Whether quantum computers will reach cryptographically relevant scale before classical post-quantum cryptography becomes universal is genuinely open as of 2026.

A conceptual point remains as well: quantum circuits produce output via measurement, which is irreversible. Every gate is unitary; the final measurement is not. The tension between unitary evolution and measurement collapse sits at the heart of interpretational quantum mechanics.

---

## References

- Nielsen, M.A. and Chuang, I.L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. Ch. 1.3, 4.1–4.5. [verify]
- Deutsch, D. (1985). "Quantum theory, the Church-Turing principle and the universal quantum computer." *Proceedings of the Royal Society of London A*, 400, 97–117.
- Wootters, W.K. and Zurek, W.H. (1982). "A single quantum cannot be cloned." *Nature*, 299, 802–803.
- Dieks, D. (1982). "Communication by EPR devices." *Physics Letters A*, 92, 271–272.
- Grover, L.K. (1996). "A fast quantum mechanical algorithm for database search." *Proceedings of STOC 1996*, 212–219.
- Shor, P.W. (1994). "Algorithms for quantum computation: discrete logarithms and factoring." *Proceedings of FOCS 1994*, 124–134.
- Landauer, R. (1961). "Irreversibility and heat generation in the computing process." *IBM Journal of Research and Development*, 5, 183–191.
- Gottesman, D. (1998). "The Heisenberg representation of quantum computers." arXiv:quant-ph/9807006.

