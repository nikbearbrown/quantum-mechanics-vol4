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

## The +1 — Simulation Exercise

The deliverable is `04-gate-circuit.html`: a two-qubit quantum circuit simulator with a draggable gate palette, real-time state vector display, and animated Bloch spheres that shrink to the origin when CNOT creates entanglement.

### `PROJECT.md` Update

````
Append to PROJECT.md:

Chapter 4 — Quantum Gates and Circuits
Deliverable: 04-gate-circuit.html
Status: in progress

Three stacked SVG panels.

Panel A — Circuit grid (700 × 420):
- Two qubit wires at y=100 (q0) and y=200 (q1). Labels "q0 |0>" and "q1 |0>".
- Five gate slots per wire, x=150 to x=650.
- Draggable palette (left): H, X, Y, Z, S, T, CNOT, Rz(theta).
- CNOT: vertical line spanning both wires, filled dot on control, open circle on target.
  Clicking placed CNOT swaps control and target.
- Default scaffold: H in slot 1 of q0, CNOT (ctrl=q0, tgt=q1) in slot 2.

Panel B — State vector (700 × 220):
- Four bars: |00>, |01>, |10>, |11>. Height = |c_i|^2 * 150px.
  Bar color: HSL hue = arg(c_i) * 180/pi.
- Symbolic state name if recognized (within tolerance 0.001).

Panel C — Bloch spheres (700 × 260):
- Two Bloch sphere projections labeled q0, q1.
  Orange arrow from origin to Bloch vector. Red dot at origin if |r| < 0.05.
  Display r_x, r_y, r_z below each sphere.
````

### `CLAUDE.md` Physics Rules

````markdown
## Chapter 4 — Quantum Gate Circuit Physics Rules

1. State: complex 4-vector psi = [c_00, c_01, c_10, c_11].
   First index = q0 (outer), second = q1 (inner).
   Normalize after every gate; warn if |sum|c_i|^2 - 1| > 1e-6.

2. Single-qubit gate on q0: U_full = kron(U, I_2).
   Single-qubit gate on q1: U_full = kron(I_2, U).
   Implement kron explicitly.
   Test: kron(H,I) on |00> gives [1,0,1,0]/sqrt(2), NOT [1,1,0,0]/sqrt(2).

3. CNOT (ctrl=q0, tgt=q1): [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
   CNOT (ctrl=q1, tgt=q0): [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
   Verify: CNOT(ctrl=q0) on |10> gives |11>.

4. Gate matrices (exact, radians):
   H: [[1,1],[1,-1]]/sqrt(2)
   X: [[0,1],[1,0]]
   Y: [[0,-i],[i,0]]
   Z: [[1,0],[0,-1]]
   S: [[1,0],[0,i]]
   T: [[1,0],[0,exp(i*pi/4)]]   ← pi/4 radians, NOT 45 degrees
   Rz(theta): [[exp(-i*theta/2),0],[0,exp(i*theta/2)]]

5. Reduced density matrix for Bloch vector:
   rho_q0[a,b] = sum_k psi[a*2+k] * conj(psi[b*2+k])  for k in {0,1}
   rho_q1[a,b] = sum_k psi[k*2+a] * conj(psi[k*2+b])  for k in {0,1}
   Bloch components:
     r_x = 2 * Re(rho[0,1])
     r_y = 2 * Im(rho[1,0])
     r_z = rho[0,0] - rho[1,1]
   Clamp |r| <= 1.0 before rendering.

6. Symbolic state recognition (tolerance 0.001, up to global phase):
   |Phi+>: psi = [1,0,0,1]/sqrt(2)
   |Phi->: psi = [1,0,0,-1]/sqrt(2)
   |Psi+>: psi = [0,1,1,0]/sqrt(2)
   |Psi->: psi = [0,1,-1,0]/sqrt(2)

FAILURE MODES:
(a) kron index order swapped (q0 must be outer).
(b) CNOT matrix wrong when control/target swapped.
(c) T gate in degrees not radians.
(d) Reduced density matrix index order wrong.
````

### The Simulation Prompt

````
Read CLAUDE.md and PROJECT.md first.

Build 04-gate-circuit.html: single self-contained HTML, D3 v7 from CDN, no other dependencies.

PANEL A — Circuit grid (700 × 420 SVG):
  q0 wire at y=100, q1 wire at y=200. Labels at left.
  Five gate slots per wire, spaced x=150 to x=650.
  Empty slot: light grey rectangle, clickable to remove gate.
  Gate palette (x=30 to x=130): H, X, Y, Z, S, T, CNOT, Rz.
    Colored rectangles, draggable to any slot.
    Rz: shows number input for theta (0-360 deg) when placed.
  CNOT in a slot: vertical line, filled dot on control, open circle on target.
    Clicking placed CNOT swaps control/target.
  "Reset circuit" button top-right: restores H(q0, slot1) + CNOT(slot2).
  Default: H slot1 q0, CNOT slot2 (ctrl=q0, tgt=q1). q0 q1 start |0>.

PANEL B — State vector (700 × 220 SVG):
  Four bars |00> |01> |10> |11>. Height = |c_i|^2 * 150px.
  Bar color: HSL hue = arg(c_i)*180/pi.
  Numerical: probability P_i and phase in degrees below each bar.
  Symbolic state name below bars if recognized, else "general state".

PANEL C — Bloch spheres (700 × 260 SVG):
  Two panels 340 × 260 each, labeled q0 and q1.
  Orthographic projection: equatorial circle (rx=100, ry=20),
    prime meridian (rx=20, ry=100), polar axis. All #ccc.
  Orange arrow from (cx,cy) to (cx + r_x*90, cy - r_z*90). Arrowhead.
  Red dot at center if |r| < 0.05.
  r_x, r_y, r_z text below each sphere.

Console sanity checks:
  After default scaffold: psi ≈ [1,0,0,1]/sqrt(2); r_x,r_y,r_z of q0 ≈ 0.
  H on q0 alone: psi ≈ [1,0,1,0]/sqrt(2); q0 Bloch ≈ (1,0,0), q1 ≈ (0,0,1).
  CNOT alone on |00>: psi = [1,0,0,0] unchanged.
  X on q0: psi = [0,0,1,0]; q0 Bloch ≈ (0,0,-1).
````

### Exploration Tasks

**Default Bell state.** Load the page. The state readout should show $|\Phi^+\rangle$. Both Bloch vectors are at the origin. Remove the CNOT from slot 2 by clicking it. The state should become $(|0\rangle + |1\rangle)/\sqrt{2}\otimes|0\rangle$; both Bloch vectors return to the surface.

**Pauli NOT.** Clear the circuit. Place $X$ on $q_0$ only. Final state: $|10\rangle$. Bloch vector of $q_0$: south pole $(0,0,-1)$. Place $X$ again: recover $|00\rangle$.

**Deutsch for $f_2$.** The oracle for balanced $f_2$ (where $f(x) = x$) is just CNOT. Circuit: place $X$ on $q_1$ in slot 0 (to initialize $|1\rangle$), then $H$ on both in slot 1, then CNOT in slot 2, then $H$ on $q_0$ in slot 3. Final state of $q_0$: should be $|1\rangle$ — "balanced."

**Deutsch for $f_4$.** The oracle for constant $f_4$ (where $f(x) = 1$) is $X$ on $q_1$. Circuit: $X$ on $q_1$ slot 0, $H$ on both slot 1, $X$ on $q_1$ slot 2 (the oracle), $H$ on $q_0$ slot 3. Final $q_0$: should be $|0\rangle$ — "constant."

**Bloch geometry of $HTH$.** Build the sequence $H, T, H$ on $q_0$. Since $T$ is a $\pi/4$ rotation about $\hat z$, and $H$ swaps $\hat x$ and $\hat z$, the combination $HTH$ is a $\pi/4$ rotation about $\hat x$. Start from $q_0 = |0\rangle$ (north pole, Bloch vector $(0,0,1)$) and verify the Bloch vector has rotated by $\pi/4$ about $\hat x$.

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

---

## Running Project — Reconstruct a Real Research Result

**This chapter adds:** the *measurement apparatus model* — the $H$–CNOT circuit that prepares the entangled resource state and the reversed circuit (Bell measurement) that reads it. A CHSH experiment is not just a state; it is a state plus a basis-rotation-and-measure procedure, and this chapter gives you the unitary that implements "Alice measures at angle $\theta_a$." It connects the abstract correlation $E(\hat a,\hat b)$ to an actual gate sequence on actual qubits.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Multiplying out a gate sequence ($H\otimes I$ then CNOT, or a basis rotation $R_y(2\theta)$ before a $Z$-measurement) on a state vector — *Why AI works here:* deterministic matrix algebra you check against the Bell-state preparation table.
- Drafting a circuit-diagram description or a small state-tracing routine — *Why AI works here:* boilerplate validated by unitarity ($U^\dagger U = I$) and the known output $|\Phi^+\rangle$.
**The tell:** You are using AI well when you can verify the output by unitarity and by the known Bell-prep result — the circuit on $|00\rangle$ must give $(|00\rangle+|11\rangle)/\sqrt2$.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding whether the paper's *physical* measurement (a polarizer at angle $\phi$, a microwave pulse of a given phase) corresponds to your modeled basis rotation — *Why AI fails here:* it is a mapping from hardware to formalism that the AI cannot verify and tends to assert glibly.
- Judging whether a gate-level model is faithful enough to reproduce the paper's correlations — *Why AI fails here:* a physical-validity call requiring the experimental detail the model lacks.
**The tell:** If you could not connect "the paper rotates a polarizer to $22.5°$" to "I apply $R_y(45°)$ then measure $Z$" without the AI, the AI did physics that should have been yours.
**Physics-judgment connection:** This trains checking a claimed unitary against $U^\dagger U = I$ and against the known fixed point (Bell-prep output), before trusting any circuit-derived correlation.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a gate-level model of how your paper's measurement at angle $\theta$ is implemented — a basis rotation followed by a computational-basis measurement — verified against the CHSH correlators of Chapter 3.
**Tool:** Claude chat.
**The Prompt:**
```
I am modeling the measurement apparatus of a Bell-test experiment as a quantum
circuit. My resource state is [PASTE the Bell state from Chapter 2].

1. Show the H–CNOT preparation circuit that produces this Bell state from a
   computational-basis input, tracing the state after each gate.
2. A measurement of the observable cos(theta)*Z + sin(theta)*X is equivalent to
   rotating the qubit by R_y(-2*theta) (or the appropriate sign) and then measuring
   Z. Write the single-qubit rotation that implements "measure at angle theta" for
   Alice and for Bob, and confirm by computing <psi| (rotation^dagger Z rotation) |psi>
   reproduces E = cos(theta_a - theta_b) for |Phi+>.
3. Describe the Bell-measurement circuit (CNOT then H then measure both) that a
   dense-coding/teleportation-style readout uses, and confirm it maps the four
   Bell states to the four computational basis states.
Show every matrix. Verify each rotation is unitary (R^dagger R = I).
```
**What this produces:** the prep circuit, the explicit basis-rotation that realizes "measure at angle $\theta$," a check that it reproduces Chapter 3's $E(\theta_a,\theta_b)$, and the Bell-measurement readout — the apparatus half of the reconstruction.
**How to adapt:** *Your system:* if your paper uses polarizers, note the factor-of-2 between polarizer angle and Bloch-sphere angle. *ChatGPT/Gemini:* same prompt; rotation sign conventions differ between tools — reconcile against the $E = \cos$ check. *Claude Project:* save as `apparatus.md`.
**Builds on:** Chapter 3's correlators $E(\hat a,\hat b)$ — now realized as concrete gates.  **Next:** Chapter 5 uses this same Bell-measurement circuit inside teleportation and ties resource quality back to $S$.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a `circuit.py` in your dossier that prepares the Bell state and implements angle measurements via rotations, reproducing `chsh.py`'s $S$.
**Tool:** Claude Code.
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `reconstruction-dossier/` with `chsh.py` (Chapter 3) present.
- [ ] Claude Code installed.
- [ ] Add to `CLAUDE.md`: "Every gate matrix must be unitary (U_dag @ U == I within 1e-9). Assert before use. Index order: q0 is the outer (left) tensor factor."
**The Task:**
```
In reconstruction-dossier/:

1. Add circuit.py with H, X, Z, CNOT (ctrl q0), and Ry(angle) gate matrices, each
   asserted unitary. Provide kron(U_q0, U_q1) helpers.
2. bell_prep(): apply (H kron I) then CNOT to |00>, assert the result equals
   |Phi+> = [1,0,0,1]/sqrt(2) within 1e-9.
3. measure_angle_correlator(theta_a, theta_b): prepare |Phi+>, apply Ry rotations
   on each qubit that implement a measurement at theta_a, theta_b, and return the
   ZZ expectation. Assert it equals chsh.correlator(|Phi+>, theta_a, theta_b)
   from Chapter 3 within 1e-9 (cross-check the two routes to E).
4. __main__: print the four canonical correlators and the resulting S via this
   circuit route; assert S = 2*sqrt(2).
5. Run, paste output. Leave chsh.py and earlier files unchanged.

Stop when the circuit-route S matches the operator-route S to 1e-9.
```
**Expected output:** `circuit.py`, a console confirmation that the gate-circuit correlators equal the operator-expectation correlators and yield $S = 2.828$.
**What to inspect:** the two independent routes to $E(\theta_a,\theta_b)$ agree to $10^{-9}$ — this cross-check is the point; a Bell-prep output exactly $[1,0,0,1]/\sqrt2$.
**If it goes wrong:** if the two routes disagree by a sign or a factor, the rotation angle convention (polarizer-angle vs Bloch-angle, factor of 2) is almost always the culprit — fix the `Ry` argument, not the operator route.
**CLAUDE.md / AGENTS.md note:** keep "assert unitarity on every gate; cross-check any new correlation route against the established one."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the R3/R4 claim that your gate-level apparatus reproduces the Chapter 3 correlators.
**Validation type:** Code + numerical result.
**Risk level:** Medium — the rotation-angle convention is an easy silent factor-of-2 that still "looks right" at the canonical angles.
**Setup:** use the R4 cross-check output.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Quantum Gates and Circuits
□ Correctness: is every gate matrix unitary (U_dag U = I)?
□ Completeness: does bell_prep output exactly [1,0,0,1]/sqrt(2)?
□ Scope: did the circuit route compute the SAME E(a,b) as the operator route,
  not a coincidentally-close one?
□ Cross-check: do the two routes agree to 1e-9 at NON-canonical angles too
  (test theta_a=17 deg, theta_b=63 deg), not just at 0/90/45/-45?
□ S check: does the circuit route give S = 2*sqrt(2) for |Phi+>?
□ Failure-mode check: any of —
  - fluent but wrong (agreement only at the canonical angles, divergence elsewhere
    — the tell of a factor-of-2 angle bug)
  - non-unitary gate accepted
  - q0/q1 tensor-order swap in kron
```
**What to do with findings:** pass → your apparatus model is faithful; record it; one fail → fix the convention and re-test at off-canonical angles; multiple fails → derive the basis-rotation unitary by hand and compare.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI generated the gate matrices and the basis-rotation that implements an angle measurement.
> *2:* The AI could not determine the correct angle convention for my paper's physical measurement (polarizer vs spin axis) — I fixed the factor-of-2 by checking against the operator-route correlator.
**Physics-judgment connection:** This validation trains the discipline of cross-checking a result by two independent routes and testing at non-special inputs — the way real bugs (like a factor-of-2 that hides at the symmetric angles) are caught.

---

Chapter 5 covers quantum error correction. The no-cloning theorem prevents copying qubits; errors accumulate during computation. Error correction must hide logical information in entangled states, detecting and correcting errors without ever measuring the logical qubit directly. The three-qubit bit-flip code and the Shor nine-qubit code are the entry points.
