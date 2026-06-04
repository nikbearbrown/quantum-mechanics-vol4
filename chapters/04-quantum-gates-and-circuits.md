# Chapter 4 — Quantum Gates and Circuits

## TL;DR

A quantum computation is a sequence of reversible matrix multiplications — unitary gates — applied to a register of qubits, followed by measurement. Single-qubit gates are rotations of the Bloch sphere; the CNOT is the minimal two-qubit gate that creates entanglement. Three gate types — Hadamard, $T$, and CNOT — together approximate any transformation you could ever want. Tracing a two-qubit circuit state by state, you will see $|\Phi^+\rangle$ emerge from $|00\rangle$ in two gate steps. Then the Deutsch algorithm will show you that quantum parallelism + interference solves a problem classically requiring two queries with exactly one.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Write** the matrix representation and Bloch-sphere interpretation of every standard single-qubit gate: $X, Y, Z, H, S, T$ and the continuous rotation gates $R_x, R_y, R_z$ (Bloom: Remember / Apply).
2. **Write** the CNOT matrix, trace its action on all four computational basis states, and explain its entangling power (Bloom: Apply).
3. **State** what a universal gate set is, name $\{H, T, \mathrm{CNOT}\}$ as the canonical example, and distinguish it from the classically simulable Clifford group (Bloom: Understand).
4. **Trace** the H–CNOT Bell-state preparation circuit state by state, identifying where entanglement is created (Bloom: Apply).
5. **Work through** the Deutsch algorithm step by step, identifying phase kickback and explaining why one query suffices (Bloom: Analyze).
6. **Name** Grover's algorithm and Shor's algorithm, state the type of speedup each offers, and identify the problem each solves (Bloom: Remember / Understand).

---

## A Machine That Runs Backward

The first thing you should know about a quantum computer is that it cannot throw anything away.

Every classical computer runs on gates that discard information. An AND gate has two inputs and one output: you hand it (0, 0) and it returns 0; you hand it (0, 1) and it also returns 0. Once the output is out, the inputs are gone. Rolf Landauer showed in 1961 that erasing one bit of information costs at least $kT \ln 2$ of energy as heat — not a limitation of current engineering, but a thermodynamic law. Classical computers are irrevocably in the business of forgetting.

A quantum gate works differently. It is a unitary matrix: if you run the circuit backward, applying the conjugate transpose of each gate in reverse order, you recover your original input exactly. Nothing is erased. The machine is fully reversible. This is not a design choice; it follows directly from the requirement that probability must sum to 1 at every step.

That reversibility has a consequence so counterintuitive it took decades to properly appreciate: you cannot copy an unknown quantum state. If you could, you would be able to run the copier forward, produce two identical outputs from one input, and then try to run it backward — but which of the two outputs would you use? The math makes this impossible, and we will see exactly why. The impossibility, in turn, is what makes quantum communication secure and quantum computation non-trivially different from classical computation.

This chapter opens the quantum circuit model, introduces the gates that populate it, and traces two complete circuits to their conclusions.

---

## Core Development

### Qubits and the Computational Basis

A single qubit is a two-dimensional complex vector space. The computational basis states are $|0\rangle$ and $|1\rangle$. An arbitrary pure single-qubit state is

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1,$$

where $\alpha, \beta \in \mathbb{C}$. Absorbing the global phase, this is parameterized by two real numbers:

$$|\psi\rangle = \cos\!\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\!\left(\frac{\theta}{2}\right)|1\rangle,$$

where $\theta \in [0, \pi]$ and $\phi \in [0, 2\pi)$. This maps to a point on the unit sphere in $\mathbb{R}^3$ — the **Bloch sphere** — with $|0\rangle$ at the north pole ($\theta = 0$), $|1\rangle$ at the south pole ($\theta = \pi$), and the equator holding all equal-superposition states.

An $n$-qubit register spans $\mathbb{C}^{2^n}$, with computational basis states $|x\rangle$ for $x \in \{0,1\}^n$. Two qubits span a four-dimensional space; the basis is $|00\rangle, |01\rangle, |10\rangle, |11\rangle$.

### Why Gates Must Be Unitary

A **quantum gate** on $n$ qubits is a linear map $U : \mathbb{C}^{2^n} \to \mathbb{C}^{2^n}$. For the map to preserve the normalization constraint $\langle\psi|\psi\rangle = 1$ for all input states $|\psi\rangle$, it must satisfy

$$U^\dagger U = \mathbf{I}.$$

This is the definition of a unitary matrix. Unitarity has two immediate consequences:

1. **Reversibility.** Because $U^\dagger U = \mathbf{I}$, the matrix $U$ is invertible with $U^{-1} = U^\dagger$. Running the circuit backward — applying $U^\dagger$ — recovers the input. No classical AND or OR gate has an inverse; quantum gates always do.

2. **Inner-product preservation.** $\langle\phi|U^\dagger U|\psi\rangle = \langle\phi|\psi\rangle$. Gate application does not change the overlap between states. This is why quantum gates are often visualized as rigid rotations: they rotate the Bloch sphere without stretching or compressing it.

The irreversibility of classical computation is the reason quantum computers cannot straightforwardly implement classical logic gates as-is. To implement a classical AND gate in a quantum circuit, you must use ancilla qubits to store the "garbage" — the forgotten input bits — and then uncompute them. The Toffoli gate ($\mathrm{CCNOT}$, three-qubit controlled-NOT) provides a universal reversible classical gate set as a special case.

### The No-Cloning Theorem

Before cataloguing the gates, this constraint deserves its own paragraph.

**Theorem (Wootters & Zurek, 1982; Dieks, 1982).** There is no unitary $\hat{U}$ such that $\hat{U}|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for all $|\psi\rangle$.

**Proof.** Suppose such $\hat{U}$ exists. Apply it to two states $|\psi\rangle$ and $|\phi\rangle$:

$$\hat{U}|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle, \qquad \hat{U}|\phi\rangle|0\rangle = |\phi\rangle|\phi\rangle.$$

Unitarity preserves inner products:

$$\langle\phi|\psi\rangle \cdot \langle 0|0\rangle = \langle\phi|\psi\rangle \cdot \langle\phi|\psi\rangle$$

$$\langle\phi|\psi\rangle = \langle\phi|\psi\rangle^2.$$

A complex number equal to its own square satisfies $z(z-1) = 0$, so $z = 0$ or $z = 1$. Therefore $\langle\phi|\psi\rangle \in \{0,1\}$: the two states are either orthogonal or identical. No cloner can handle arbitrary unknown states. $\square$

No-cloning is structural, not a technology limitation. Its consequences cascade: eavesdropping on a quantum channel requires measuring — which disturbs the state and can be detected. Quantum error correction cannot use simple copying and must hide information in entangled states instead. And no-cloning enforces no-signaling: if Bob could clone his half of a Bell pair many times and measure in different bases, he could infer Alice's measurement setting — but he cannot clone, so he cannot.

### Single-Qubit Gates as Bloch-Sphere Rotations

Every single-qubit unitary is, up to a global phase, a rotation of the Bloch sphere. This follows from the fact that $\mathrm{SU}(2)$ — the group of $2\times 2$ unitary matrices with determinant 1 — is the double cover of $\mathrm{SO}(3)$. The rotation by angle $\alpha$ about the axis $\hat{n} = (n_x, n_y, n_z)$ corresponds to the gate

$$R_{\hat{n}}(\alpha) = e^{-i\alpha \hat{n}\cdot\vec{\sigma}/2} = \cos\!\left(\frac{\alpha}{2}\right)\mathbf{I} - i\sin\!\left(\frac{\alpha}{2}\right)(n_x\sigma_x + n_y\sigma_y + n_z\sigma_z).$$

The Pauli matrices generate the three rotation axes:

$$\sigma_x = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}.$$

The standard single-qubit gate vocabulary:

**Pauli gates** ($\pi$-rotations about the named axis):

$$X = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \quad Y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}, \quad Z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}.$$

$X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$ — the quantum NOT gate. $Z|0\rangle = |0\rangle$, $Z|1\rangle = -|1\rangle$ — a phase flip. Each Pauli squares to the identity: $X^2 = Y^2 = Z^2 = \mathbf{I}$.

**Hadamard gate**:

$$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}.$$

$H|0\rangle = |{+}\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $H|1\rangle = |{-}\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$. The Hadamard is a $\pi$-rotation about the axis $(\hat{x} + \hat{z})/\sqrt{2}$; geometrically it swaps the $x$- and $z$-axes of the Bloch sphere. $H^2 = \mathbf{I}$.

**Phase gate** ($S$ gate, $\pi/2$-rotation about $\hat{z}$):

$$S = \begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix}.$$

$S|0\rangle = |0\rangle$, $S|1\rangle = i|1\rangle$. $S^2 = Z$.

**$T$ gate** ($\pi/8$ gate, $\pi/4$-rotation about $\hat{z}$):

$$T = \begin{pmatrix}1 & 0 \\ 0 & e^{i\pi/4}\end{pmatrix}.$$

$T|0\rangle = |0\rangle$, $T|1\rangle = e^{i\pi/4}|1\rangle$. $T^2 = S$, $T^4 = Z$, $T^8 = \mathbf{I}$. The $T$ gate is the source of non-Clifford power in fault-tolerant computation; it is the expensive gate in all major hardware architectures.

**Continuous rotation gates**:

$$R_x(\theta) = \begin{pmatrix}\cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2)\end{pmatrix}, \quad R_z(\theta) = \begin{pmatrix}e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2}\end{pmatrix}.$$

Any single-qubit gate decomposes as $e^{i\gamma}R_z(\alpha)R_y(\beta)R_z(\delta)$ for some angles — the Euler-angle decomposition. This means three $R_z$ and $R_y$ rotations suffice to implement any single-qubit operation.

### The CNOT Gate and Entangling Power

The controlled-NOT (CNOT) gate acts on two qubits: a **control** and a **target**. It flips the target if and only if the control is $|1\rangle$. In the basis $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ with qubit 0 as control and qubit 1 as target:

$$\mathrm{CNOT} = \begin{pmatrix}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{pmatrix}.$$

Action on the basis: $|00\rangle \to |00\rangle$, $|01\rangle \to |01\rangle$, $|10\rangle \to |11\rangle$, $|11\rangle \to |10\rangle$.

When the control is in a basis state, CNOT is a classical XOR gate: $|x, y\rangle \to |x, x \oplus y\rangle$. The crucial quantum case is when the control is in a superposition. If control is $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ and target is $|0\rangle$:

$$\mathrm{CNOT}\cdot \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle.$$

The output is entangled. CNOT has **maximal entangling power** for two qubits: starting from an appropriate product state, it produces a maximally entangled Bell state. The CZ gate (controlled-Z) has the same entangling power; the two are related by CZ $= (I \otimes H) \cdot \mathrm{CNOT} \cdot (I \otimes H)$.

CNOT is its own inverse: $\mathrm{CNOT}^2 = \mathbf{I}$.

### Universal Gate Sets

**Definition.** A gate set $\mathcal{G}$ is **universal** for quantum computation if, for every $n$-qubit unitary $U$ and every $\varepsilon > 0$, $U$ can be approximated to precision $\varepsilon$ (in operator norm) by a finite sequence of gates from $\mathcal{G}$.

The canonical universal gate set is $\{H, T, \mathrm{CNOT}\}$. Here is why each gate contributes:

- $H$ and $T$ together generate a **dense subgroup** of $\mathrm{SU}(2)$ — applying them in different combinations can approximate any single-qubit rotation to arbitrary precision.
- $\mathrm{CNOT}$ provides the two-qubit entangling power needed to spread computation across qubits.

**The Solovay–Kitaev theorem** (Solovay, 1995; Kitaev, 1997) quantifies the efficiency: if a finite gate set densely generates $\mathrm{SU}(2)$, any single-qubit gate can be approximated to precision $\varepsilon$ using $O(\log^c(1/\varepsilon))$ gates, where $c \approx 2$. This means you do not pay an exponential price to use a finite gate set instead of continuous parameters.

**The Clifford group** consists of $\{H, S, \mathrm{CNOT}\}$ and their products. Clifford circuits can be efficiently simulated classically (the Gottesman–Knill theorem): even though the individual states are superpositions, the output distribution is efficiently computable. Adding $T$ breaks this classical simulability and provides genuine quantum computational power. In fault-tolerant architectures, $T$ is the "expensive" non-Clifford gate because implementing it fault-tolerantly requires magic state distillation — a large overhead that dominates the resource cost of practical algorithms.

The circuit model is now the dominant computational model for quantum hardware. IBM's Heron processor (133 qubits, 2023–2024), Google's Willow chip (105 qubits, 2024), and IonQ's trapped-ion systems all implement gate sets equivalent to $\{H, T, \mathrm{CNOT}\}$ at the physical level. Gate fidelities as of 2024–2025: single-qubit gates routinely exceed 99.9%; two-qubit CNOT gates reach 99–99.5% on superconducting platforms and up to 99.9% on trapped-ion systems.

### Circuit Diagrams: Notation

A quantum circuit is drawn as a set of horizontal wires (one per qubit, labeled $q_0, q_1, \ldots$ top to bottom) with gates applied left to right (time increases rightward). Conventions:

- Single-qubit gates: boxes labeled with the gate name.
- CNOT: filled dot $\bullet$ on the control wire, $\oplus$ on the target wire, connected by a vertical line.
- CZ: filled dots on both wires.
- Measurement: a meter symbol $\langle M\rangle$ at the right end of a wire; a double line carries the resulting classical bit.
- The initial state (default $|0\rangle$ for each qubit) is written to the left of the wires.

Reading a circuit from left to right is reading a sequence of matrix multiplications. If the circuit has gates $G_1$ (leftmost), then $G_2$, then $G_3$, the final state is $G_3 G_2 G_1 |\psi_0\rangle$. Note the rightward-reading order of the circuit and the rightward-multiplying convention clash: matrix multiplication proceeds from right to left ($G_3$ acts last but is written leftmost in the matrix product).

---

## Worked Example 1: H–CNOT Bell-State Preparation

**The lesson.** Two gates prepare a maximally entangled Bell state from the computational basis state $|00\rangle$.

**The circuit.** Apply $H$ to qubit 0 (control). Then apply CNOT with control = qubit 0, target = qubit 1.

**Step 0 — Initial state.**

$$|\psi_0\rangle = |00\rangle = |0\rangle_0 \otimes |0\rangle_1.$$

Both Bloch vectors point to the north pole. The state is a product state.

**Step 1 — Hadamard on qubit 0.** The gate applied to the two-qubit system is $H \otimes I$:

$$(H \otimes I)|00\rangle = (H|0\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle).$$

Qubit 0 is now in $|{+}\rangle$ — its Bloch vector points along $+\hat{x}$. Qubit 1 is still $|0\rangle$ — its Bloch vector still points to the north pole. The state factors: $|{+}\rangle_0 \otimes |0\rangle_1$. No entanglement has been created.

**Step 2 — CNOT.** Control = qubit 0, target = qubit 1:

$$\mathrm{CNOT} \cdot \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) = \frac{1}{\sqrt{2}}(\mathrm{CNOT}|00\rangle + \mathrm{CNOT}|10\rangle) = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle.$$

The state can no longer be written as a tensor product of single-qubit states. Both Bloch vectors collapse to the origin: each qubit's reduced density matrix is $\hat{I}/2$, the most mixed single-qubit state. All information is in the joint correlations.

**The limit.** What if the control had been in a basis state rather than a superposition? Apply CNOT to $|10\rangle$ (control already $|1\rangle$): $\mathrm{CNOT}|10\rangle = |11\rangle$ — a product state goes to a product state. Apply CNOT to $|00\rangle$: $\mathrm{CNOT}|00\rangle = |00\rangle$ — no change. CNOT creates entanglement only when the control is in a superposition. The Hadamard in step 1 is not optional: it is the gate that enables the CNOT to do something classically impossible.

**All four Bell states.** Starting from all four computational basis states and applying $H \otimes I$ then CNOT:

| Input | After $H \otimes I$ | After CNOT | Bell state |
|-------|---------------------|------------|------------|
| $|00\rangle$ | $(|00\rangle + |10\rangle)/\sqrt{2}$ | $(|00\rangle + |11\rangle)/\sqrt{2}$ | $|\Phi^+\rangle$ |
| $|01\rangle$ | $(|01\rangle + |11\rangle)/\sqrt{2}$ | $(|01\rangle + |10\rangle)/\sqrt{2}$ | $|\Psi^+\rangle$ |
| $|10\rangle$ | $(|00\rangle - |10\rangle)/\sqrt{2}$ | $(|00\rangle - |11\rangle)/\sqrt{2}$ | $|\Phi^-\rangle$ |
| $|11\rangle$ | $(|01\rangle - |11\rangle)/\sqrt{2}$ | $(|01\rangle - |10\rangle)/\sqrt{2}$ | $|\Psi^-\rangle$ |

Two gates access the entire Bell basis. This is the preparation circuit used in every quantum teleportation experiment, every entanglement-based QKD protocol, and every Bell-test apparatus.

---

## Worked Example 2: The Deutsch Algorithm

**The lesson.** A single quantum query determines whether a function $f:\{0,1\} \to \{0,1\}$ is constant or balanced. Classical computation requires two queries. The quantum advantage comes from phase kickback and interference, not from raw parallelism.

**The setup.** There are exactly four functions from $\{0,1\}$ to $\{0,1\}$:

| $x$ | $f_1$ | $f_2$ | $f_3$ | $f_4$ |
|-----|--------|--------|--------|--------|
| 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 |

$f_1$ and $f_4$ are **constant** ($f(0) = f(1)$); $f_2$ and $f_3$ are **balanced** ($f(0) \neq f(1)$). The function $f$ is provided as a black box (oracle) that we can query but not inspect.

A classical algorithm that queries $f$ once learns one value, say $f(0) = 0$. This is consistent with $f_1$ (constant) or $f_2$ (balanced). A second query on $f(1)$ is needed to distinguish them. Classical lower bound: 2 queries.

**The quantum circuit.** Two qubits: query register $q_0 = |0\rangle$, ancilla $q_1 = |1\rangle$.

1. Apply $H$ to both qubits.
2. Apply oracle gate $U_f$.
3. Apply $H$ to $q_0$.
4. Measure $q_0$: outcome $|0\rangle$ means constant; outcome $|1\rangle$ means balanced.

**The oracle.** $U_f$ implements $|x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$ (where $\oplus$ is XOR). This is unitary (its own inverse when $f$ is deterministic) and makes no assumptions about how $f$ is computed internally.

**State trace.**

*After $H \otimes H$:*

$$q_0: H|0\rangle = |{+}\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad q_1: H|1\rangle = |{-}\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

$$|\pi_1\rangle = |{+}\rangle \otimes |{-}\rangle = \frac{1}{2}(|0\rangle + |1\rangle)(|0\rangle - |1\rangle).$$

*After $U_f$ — phase kickback.* The oracle acts on $q_0$ in superposition. For each basis component $|x\rangle$ of $q_0$ with the ancilla in $|{-}\rangle$:

$$U_f|x\rangle|{-}\rangle = |x\rangle \frac{|f(x)\rangle - |1 \oplus f(x)\rangle}{\sqrt{2}} = (-1)^{f(x)}|x\rangle|{-}\rangle.$$

(The XOR with $f(x)$ either leaves $|0\rangle - |1\rangle$ unchanged when $f(x)=0$, or flips it to $|1\rangle - |0\rangle = -(|0\rangle - |1\rangle)$ when $f(x) = 1$.) The function value $f(x)$ has been kicked back into the **phase** of the query register, not into an output qubit. The ancilla is undisturbed.

Applying to both $|0\rangle$ and $|1\rangle$ simultaneously (because $q_0$ is in superposition):

$$|\pi_2\rangle = \frac{1}{\sqrt{2}}\bigl[(-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\bigr] \otimes |{-}\rangle.$$

*Two cases:*

If $f$ is **constant** ($f(0) = f(1) = c$): both terms acquire the same phase $(-1)^c$, so $q_0 \propto |0\rangle + |1\rangle = \sqrt{2}|{+}\rangle$. (Global phase is irrelevant to measurement.)

If $f$ is **balanced** ($f(0) \neq f(1)$): one term is $+1$ and the other is $-1$, so $q_0 \propto |0\rangle - |1\rangle = \sqrt{2}|{-}\rangle$.

*After $H$ on $q_0$:*

$$H|{+}\rangle = |0\rangle \quad \Rightarrow \quad \text{constant},$$
$$H|{-}\rangle = |1\rangle \quad \Rightarrow \quad \text{balanced}.$$

*Measure $q_0$:* outcome 0 → constant; outcome 1 → balanced. One query. Zero probability of error.

**Why this works.** The quantum speedup is not "we evaluated $f(0)$ and $f(1)$ at the same time." Quantum parallelism alone does not help: if you just measured after step 1 of the oracle, you would get $f(0)$ or $f(1)$ at random — one bit of information, same as classical. What provides the advantage is **interference**. The oracle writes the comparison $f(0) \oplus f(1)$ into a relative phase between $|0\rangle$ and $|1\rangle$. The final Hadamard converts that relative phase into a distinguishable amplitude. You get one bit of global information — constant vs. balanced — from one query. You cannot get it by measuring the amplitude of either $|0\rangle$ or $|1\rangle$ individually, because both have the same magnitude; only the phase differs, and the Hadamard converts phase difference into amplitude difference.

This is the template for all quantum algorithms: superposition evaluates a function on many inputs simultaneously; interference filters the outputs so the answer you want has high amplitude and wrong answers cancel.

### Grover and Shor at Literacy Level

**Grover's search algorithm (Grover, 1996).** Given an unsorted database of $N$ items with one marked item, find it. Classical lower bound: $O(N)$ queries. Grover's algorithm: $O(\sqrt{N})$ queries. The mechanism is **amplitude amplification**: starting from the uniform superposition $\tfrac{1}{\sqrt{N}}\sum_x|x\rangle$, an "oracle" flips the phase of the marked item, then an "inversion about the mean" operation preferentially amplifies the marked amplitude. After $O(\sqrt{N})$ iterations, the marked item has amplitude close to 1 and can be found by measurement. The speedup is quadratic, not exponential — still striking for large $N$, and it threatens symmetric-key cryptography by effectively halving the key length.

**Shor's factoring algorithm (Shor, 1994).** Given a large integer $N$, find its prime factors. The best classical algorithm (the Number Field Sieve) runs in sub-exponential time $\exp(O(n^{1/3} \log^{2/3} n))$ where $n = \log_2 N$. Shor's algorithm runs in polynomial time $O(n^2 \log n \log \log n)$. The mechanism is the **quantum Fourier transform** applied to the period-finding problem: the hard part of factoring reduces to finding the period of the function $f(r) = a^r \bmod N$, and a QFT over a superposition of $r$ values extracts the period exponentially faster than any classical method. This speedup directly threatens RSA and Diffie-Hellman public-key cryptography. Neither Grover nor Shor will be derived in this volume; their importance is that they establish why universal gate sets are not a theoretical nicety but an engineering imperative.

---

## Common Misconceptions

**"Quantum parallelism means quantum computers always win."** Quantum parallelism (superposing all inputs) is necessary but not sufficient for a speedup. Measuring a superposition collapses it to one outcome, selected randomly. The Deutsch algorithm shows that the advantage is in the *interference* step that makes the right answer collapse with certainty. For tasks where interference cannot be exploited — like arbitrary database look-up — quantum computers do not achieve exponential speedup (Grover's quadratic speedup is the best achievable for unstructured search).

**"CNOT always creates entanglement."** CNOT applied to a computational basis state ($|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$) just performs a classical XOR — no entanglement. CNOT creates entanglement only when the control is in a superposition. The Hadamard before the CNOT is what makes Bell-state preparation work.

**"A quantum gate can be designed to do anything."** Any gate must be unitary. You cannot implement a classical irreversible gate (AND, OR, NAND) directly as a single quantum gate — you need to add ancilla qubits to make the operation reversible. The Toffoli gate (CCNOT) provides a universal reversible classical gate set, but it requires three qubits for what a classical NAND does with two inputs and one output.

**"The $T$ gate is just a small rotation — why is it expensive?"** Physically, implementing $T$ fault-tolerantly on a surface code requires **magic state distillation**: running a noisy $T$ gate many times, distilling the result through a quantum error-correcting protocol to produce a high-fidelity "magic state" $|T\rangle = T|{+}\rangle$, and then consuming that magic state to perform the $T$ gate on the target qubit. The overhead is significant — hundreds of physical qubits and gate operations per logical $T$ gate. Circuit optimization to minimize $T$-count is a major research area in fault-tolerant computing.

**"Phase kickback is just a trick specific to Deutsch."** Phase kickback is the universal mechanism by which quantum algorithms encode information. It appears in the Bernstein–Vazirani algorithm, Simon's algorithm, Grover's oracle, and the QFT underlying Shor's algorithm. Any time a quantum algorithm uses an oracle with an ancilla prepared in $|{-}\rangle$ or a similar eigenstate, phase kickback is operating.

---

## Exercises

### Warm-Up

1. *[Tests: single-qubit gate matrices]* Verify that $H^2 = I$, $S^2 = Z$, and $T^2 = S$ by direct matrix multiplication. Then verify that $HXH = Z$ and $HZH = X$ — the Hadamard conjugates $X$ and $Z$ into each other.

2. *[Tests: CNOT action]* Apply the CNOT matrix to all four two-qubit basis states $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ by explicit matrix multiplication. Confirm the action $|x,y\rangle \to |x, x \oplus y\rangle$. Then apply CNOT twice to $|10\rangle$ and confirm you recover $|10\rangle$ (CNOT is its own inverse).

3. *[Tests: no-cloning]* Using the inner-product argument, show that no unitary can clone the two states $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ and $|{-}\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$. Compute $\langle {-}|{+}\rangle$ explicitly. Does this satisfy $z = z^2$?

### Apply

4. *[Tests: Bell-state preparation]* Starting from $|01\rangle$, apply $H \otimes I$ and then CNOT(control=0, target=1). (a) Write out the state after each gate. (b) Which Bell state do you obtain? (c) Apply the circuit to all four computational basis inputs and complete the Bell-state table.

5. *[Tests: Deutsch algorithm, phase kickback]* Trace the Deutsch algorithm for the specific constant function $f(0) = f(1) = 1$ (i.e., $f_4$). Write out the state at each step: initial, after both Hadamards, after the oracle $U_{f_4}$, after the final Hadamard. Confirm that the measurement outcome is $|0\rangle$ (constant). Why does the global phase $(-1)^1 = -1$ not affect the measurement?

6. *[Tests: Bloch sphere action of $H$]* The Bloch vector of $|0\rangle$ is $(0, 0, 1)$ (north pole). (a) Apply $H$ and find the Bloch vector of $H|0\rangle = |{+}\rangle$. (b) Apply $H$ again. (c) Starting from $|1\rangle$ (south pole, Bloch vector $(0,0,-1)$), apply $H$ and find the Bloch vector of $H|1\rangle = |{-}\rangle$. Verify that $H$ is a $\pi$-rotation about the $(\hat{x}+\hat{z})/\sqrt{2}$ axis by checking that this axis is a fixed point of the rotation.

### Synthesize / Produce

7. *[Synthesize, Apply+]* Design a two-qubit circuit using $\{H, \mathrm{CNOT}, X\}$ that takes $|00\rangle$ to $|\Psi^-\rangle = (|01\rangle - |10\rangle)/\sqrt{2}$. Write out the circuit diagram (text notation is fine: $q_0: H, q_1: X$, then $\mathrm{CNOT}(q_0, q_1)$, etc.) and verify each step. There are multiple correct answers; find at least two.

8. *[Produce — simulation task]* Using the simulation from the +1 exercise (or pen and paper), build the Deutsch algorithm circuit for the balanced function $f_2$ (where $f(0) = 0$, $f(1) = 1$). The oracle for $f_2$ is $U_{f_2}: |x\rangle|y\rangle \to |x\rangle|y \oplus x\rangle$ — which is exactly the CNOT gate with qubit 0 as control and qubit 1 as target. Trace the state vector through the full circuit and confirm the measurement outcome.

9. *[Synthesize — reversibility and T-count]* Consider a circuit that computes the classical Boolean function $\mathrm{AND}(x, y)$ reversibly using a Toffoli gate: $|x, y, 0\rangle \to |x, y, \mathrm{AND}(x,y)\rangle$. The Toffoli gate decomposes into 6 CNOT gates and 7 single-qubit gates (including $T$ and $T^\dagger$). The $T$-count of one Toffoli is 7. If a classical circuit requires $k$ NAND gates, roughly how many $T$-gates does its reversible quantum implementation require? What does this suggest about the relationship between classical circuit complexity and quantum $T$-count?

---

## Still Puzzling

The Deutsch algorithm uses one quantum query to solve a problem requiring two classical queries. The Deutsch–Jozsa algorithm generalizes this: given $f:\{0,1\}^n \to \{0,1\}$ promised to be either constant or balanced on all $2^n$ inputs, determine which using exactly one quantum query versus $2^{n-1}+1$ deterministic classical queries. The speedup is exponential over deterministic computation.

But the Deutsch–Jozsa problem is somewhat artificial. In real-world computation, you rarely encounter functions that are promised to be either constant or balanced. Simon's algorithm (Simon, 1994) gives an exponential quantum speedup for a more natural problem (finding the period of a two-to-one function), and Shor's factoring algorithm was directly inspired by Simon's. The question of which classically hard problems have quantum speedups — and why — is still being mapped out. BQP (bounded-error quantum polynomial time) is the complexity class of problems efficiently solvable on a quantum computer. Its relationship to P, NP, and BPP is not fully resolved.

A practical puzzle for the next decade: the fault-tolerant quantum algorithms (Shor, Grover, QFT-based) all require thousands to millions of error-corrected logical qubits. Current hardware has tens to hundreds of noisy physical qubits. The gap is large. The question of whether quantum computers will reach the scale needed for cryptographically relevant Shor computations before classical post-quantum cryptography becomes universal is genuinely open as of 2026.

And a conceptual puzzle: quantum circuits produce their output via measurement, which is irreversible. The circuit is unitary; the measurement is not. We derived that all gates must be unitary, and then we allow a non-unitary act at the end. The tension between unitary evolution and the measurement collapse — and whether collapse is fundamental or emergent — sits at the heart of interpretational quantum mechanics, and we will return to it in Chapter 8.

---

## The +1 — Simulation Exercise

You will build a two-qubit quantum circuit simulator in D3.js that lets you drag gates onto circuit wires, watch the state vector update in real time, and see Bloch vectors collapse when CNOT entangles two qubits.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md:

Chapter 4 — Quantum Gates and Circuits
Deliverable: 04-gate-circuit.html
Status: in progress

The simulation is a single HTML file with three panels.

Panel A — Gate palette and circuit grid (700 x 400 SVG).
- Two horizontal qubit wires (q0 on top, q1 below).
- Five gate slots per wire.
- Draggable gate palette on the left: H, X, Y, Z, S, T, CNOT, Rz(theta).
- Rz gate has a small angle input (default 45 degrees).
- CNOT spans both wires: filled dot on control (q0 by default), open
  circle (target) on the other wire. Clicking a placed CNOT swaps
  control and target.
- Click any slot to remove a gate.
- Default scaffold on load: H in slot 1 of q0, CNOT in slot 2 (control q0,
  target q1). This produces |Phi+>.

Panel B — State vector display (700 x 200 SVG).
- Four vertical bars: |00>, |01>, |10>, |11>.
  Height = |c_i|^2 (probability). Bar color encodes arg(c_i) via HSL hue.
  A small phase dial below each bar shows the complex angle.
- A text readout showing the symbolic name of common states:
  |00>, |11>, |Phi+>, |Phi->, |Psi+>, |Psi->, |+>|+>, etc.
  (within tolerance 0.001 of the exact amplitudes).

Panel C — Bloch spheres (700 x 250 SVG).
- Two side-by-side Bloch sphere projections (orthographic).
  Each 300 x 250, labeled "q0" and "q1".
- The Bloch vector is drawn as an orange arrow from origin to (r_x, r_y, r_z).
  Equator and prime meridian as light grey ellipses.
- For a product state, the arrow lives on the surface (length 1).
  For an entangled state, the arrow is at or near the origin.
  Animate the collapse as gates are applied: arrow shrinks smoothly
  when entanglement is created by CNOT.
- Below each Bloch sphere, display r_x, r_y, r_z to two decimal places.

Physics: all state updates done via explicit matrix multiplication on the
complex 4-vector [c_00, c_01, c_10, c_11]. No shortcuts.
```

### Part 2 — Physics rules for `CLAUDE.md`

```
Append to CLAUDE.md:

QUANTUM GATE CIRCUIT PHYSICS RULES

1. State: complex 4-vector psi = [c_00, c_01, c_10, c_11].
   Basis ordering: first index = q0 (control/top), second = q1 (target/bottom).
   Normalize after every gate: sum |c_i|^2 must equal 1 within 1e-6; warn if not.

2. Single-qubit gate on q0: build U_full = kron(U, I_2) (4x4).
   Single-qubit gate on q1: build U_full = kron(I_2, U) (4x4).
   Implement kron explicitly; do not hard-code the 4x4 entries.

3. CNOT with control=q0, target=q1 (standard):
   [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
   CNOT with control=q1, target=q0 (swapped):
   [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
   Verify on |10>: CNOT(ctrl=q0) maps to |11>. Verify on |01>: CNOT(ctrl=q1) maps to |11>.

4. Gate matrices (using exact values, not float approximations):
   H: [[1,1],[1,-1]] / sqrt(2)
   X: [[0,1],[1,0]]
   Y: [[0,-i],[i,0]]
   Z: [[1,0],[0,-1]]
   S: [[1,0],[0,i]]
   T: [[1,0],[0,exp(i*pi/4)]]
   Rz(theta): [[exp(-i*theta/2),0],[0,exp(i*theta/2)]]

5. Reduced density matrix for Bloch sphere:
   rho_q0[a,b] = sum_k psi[a*2+k] * conj(psi[b*2+k])  for k in {0,1}
   rho_q1[a,b] = sum_k psi[k*2+a] * conj(psi[k*2+b])  for k in {0,1}
   Bloch vector components:
     r_x = 2 * Re(rho[0,1])
     r_y = 2 * Im(rho[1,0])
     r_z = rho[0,0] - rho[1,1]
   Clamp |r| to <= 1.0 before rendering (floating point noise).

6. Symbolic state recognition (tolerance 0.001):
   |00>: psi = [1, 0, 0, 0]
   |Phi+>: psi = [1,0,0,1]/sqrt(2)
   |Phi->: psi = [1,0,0,-1]/sqrt(2)
   |Psi+>: psi = [0,1,1,0]/sqrt(2)
   |Psi->: psi = [0,1,-1,0]/sqrt(2)
   (Check up to global phase.)

KNOWN FAILURE MODES:
(a) kron product index order swapped: qubit 0 must be the "outer" index.
    Test: kron(H, I) applied to |00> should give [1,0,1,0]/sqrt(2), not [1,1,0,0]/sqrt(2).
(b) CNOT matrix wrong when control/target are swapped.
    Always verify on a basis state before accepting.
(c) T gate phase uses degrees instead of radians: exp(i*45) vs exp(i*pi/4).
    Always use radians.
(d) Reduced density matrix indices wrong: rho_q0 traces over the second index.
```

### Part 3 — The simulation prompt

```
You are working in my directory. Read CLAUDE.md and PROJECT.md first.

Build 04-gate-circuit.html: a single self-contained HTML file using D3 v7
from CDN, no other dependencies, implementing the Chapter 4 gate circuit
simulator as specified in PROJECT.md following the physics rules in CLAUDE.md.

Three stacked SVG panels.

PANEL A — Circuit grid (700 x 420):
- Qubit 0 wire: horizontal line at y=100. Qubit 1 wire: at y=200.
  Labels "q0 |0>" and "q1 |0>" at left.
- Five gate slots per wire, spaced evenly from x=150 to x=650.
  Empty slot: light grey rectangle, clickable to remove a gate.
- Gate palette on the left (x=30 to x=130): H, X, Y, Z, S, T, CNOT, Rz.
  Each is a colored rectangle with the gate name. Draggable to any slot.
- Rz gate, when placed, shows a small number input for theta (0-360 deg).
- CNOT placed in a slot: vertical line spanning both wires, filled dot on
  control, open circle on target. Clicking the CNOT symbol after placement
  swaps control (dot) and target (circle).
- A "Reset circuit" button (top right) restores the default scaffold.
- Default scaffold: H in slot 1 of q0; CNOT (ctrl=q0, tgt=q1) in slot 2.
  All other slots empty. q0 and q1 start in |0>.

PANEL B — State vector (700 x 220):
- Four bars labeled |00>, |01>, |10>, |11>, each with height = |c_i|^2 * 150px.
  Bar color: HSL with hue = arg(c_i) * 180/pi (0=red, 90=green, 180=cyan, 270=blue).
- Numerical display below each bar: probability P_i and phase arg(c_i) in degrees.
- Below the bars: a text label showing the symbolic state name if recognized,
  else "general state".
- Updates on every gate change without page reload.

PANEL C — Bloch spheres (700 x 260):
- Two Bloch sphere panels side by side (each 340 x 260).
  Label "q0" and "q1".
- Draw as orthographic projection: equatorial circle (rx=100, ry=20),
  prime meridian (rx=20, ry=100), polar axis (vertical line).
  All in light grey (#ccc).
- Bloch vector as orange arrow from (cx,cy) to (cx+r_x*90, cy-r_z*90),
  with an arrowhead. Note: y-axis on screen is inverted vs. r_z.
  The r_y component is shown by slight elliptical tilt (can simplify to
  showing only the xz-projection for clarity with a note "r_y = ...").
- Display r_x, r_y, r_z as text below each sphere.
- When |r| < 0.05 (maximally mixed, as for entangled qubit), show a red
  dot at the center instead of an arrow.

Runtime sanity checks to console.log:
- After default scaffold: psi should be [1,0,0,1]/sqrt(2) within 0.001.
  r_x for q0: 0.0. r_y for q0: 0.0. r_z for q0: 0.0. (Maximally mixed.)
- After placing H on q0 alone (no CNOT): psi = [1,0,1,0]/sqrt(2).
  Bloch vector q0: (1,0,0). q1: (0,0,1).
- After CNOT alone on |00>: psi = [1,0,0,0] unchanged. Correct.
- After X on q0: psi = [0,0,1,0]. q0 Bloch vector: (0,0,-1) [south pole].
```

### Part 4 — Exploration Tasks

1. Load the default circuit ($H$ on $q_0$, CNOT). The state readout should show $|\Phi^+\rangle$. Check that both Bloch vectors are at the origin. Drag the CNOT gate out of its slot. What does the state become? Both Bloch vectors should now be on the surface.

2. Place only $X$ on $q_0$ (no CNOT). What is the final state? What is $q_0$'s Bloch vector? Apply $X$ again — do you recover $|00\rangle$?

3. Build the Deutsch algorithm for the balanced function $f_2$. The oracle for $f_2$ is just CNOT. Circuit: $q_0 = |0\rangle$, $q_1 = |1\rangle$ (place $X$ on $q_1$ first), then $H$ on both, then CNOT, then $H$ on $q_0$. What is the final state of $q_0$? Measure: does it indicate "constant" or "balanced"?

4. Modify the circuit from task 3 to implement $f_4$ (constant: $f(0)=f(1)=1$). The oracle for $f_4$ is $X$ on $q_1$ (regardless of $q_0$). Circuit: $q_1$ starts $|1\rangle$ (X on $q_1$), $H$ on both, then $X$ on $q_1$ (the oracle), then $H$ on $q_0$. What is $q_0$'s final state?

5. Try $H$ on $q_0$, $T$ on $q_0$, $H$ on $q_0$. What does the combination $HTH$ do to the Bloch sphere? (Hint: $T$ is a $\pi/4$ rotation about $\hat{z}$; $H$ swaps the $x$- and $z$-axes. What rotation about which axis is $HTH$?)

**Extension prompt:**

```
Modify 04-gate-circuit.html to support three qubits (q0, q1, q2) with
an 8-dimensional state vector, and add the Toffoli gate (CCNOT with
control0=q0, control1=q1, target=q2) to the gate palette.

- The Toffoli gate matrix in the |000>...|111> basis is the 8x8 identity
  with the bottom-right 2x2 block replaced by [[0,1],[1,0]] (X applied to
  q2 iff q0=q1=1).
- Add a third Bloch sphere panel for q2 (computed from rho_q2 = Tr_{q0,q1}(rho)).
- Default scaffold: H on q0, H on q1, Toffoli in slot 2 (ctrl0=q0, ctrl1=q1,
  tgt=q2). The output state should have |111> with amplitude 0.5 and |000>,
  |010>, |100> each with amplitude 0.5.
- Add a "T-count" display that shows how many T gates are in the current circuit
  (counting each Toffoli as 7 T-gates, per the standard decomposition).
```

---

## References

1. Nielsen, M. A. & Chuang, I. L. (2000). *Quantum Computation and Quantum Information.* Cambridge University Press. [Canonical reference for gates (Ch. 1.3), circuits (Ch. 4.1–4.5), and universality.]
2. Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. *Proceedings of the Royal Society of London A* 400, 97–117.
3. Wootters, W. K. & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* 299, 802–803.
4. Dieks, D. (1982). Communication by EPR devices. *Physics Letters A* 92, 271–272.
5. Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of STOC 1996*, 212–219. arXiv:quant-ph/9605043.
6. Shor, P. W. (1994). Algorithms for quantum computation: discrete logarithms and factoring. *Proceedings of FOCS 1994*, 124–134.
7. Solovay, R. (1995); Kitaev, A. Yu. (1997). The Solovay–Kitaev theorem. See also: Nielsen, M. A. The Solovay–Kitaev algorithm. https://michaelnielsen.org/blog/the-solovay-kitaev-algorithm/ [verify]
8. Gottesman, D. (1998). The Heisenberg representation of quantum computers. arXiv:quant-ph/9807006. [Gottesman–Knill theorem; Clifford simulation.]
9. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development* 5, 183–191.
10. IBM Quantum Learning — The Deutsch-Jozsa Algorithm (2024). https://quantum.cloud.ibm.com/learning/en/modules/computer-science/deutsch-jozsa [verify — full Qiskit implementation and phase-kickback explanation.]
11. Aaronson, S. Lecture 16: Universal Gate Sets. https://www.scottaaronson.com/qclec/16.pdf [verify — rigorous notes on universality.]
12. Google Quantum AI (2024). Quantum error correction below the surface code threshold. *Nature* 614, 676–681. [Willow chip milestone; error rates below threshold.] [verify]
