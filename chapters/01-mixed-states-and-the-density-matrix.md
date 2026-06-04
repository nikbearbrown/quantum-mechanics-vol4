# Chapter 1 — Mixed States and the Density Matrix

A laboratory produces qubits by one of two methods, chosen at random with equal probability. Method 1 prepares $|0\rangle$. Method 2 prepares $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. The lab hands you a qubit and tells you nothing.

What is the state of your qubit?

The tempting answer: "It is either $|0\rangle$ or $|{+}\rangle$ — I just do not know which." That correctly describes your classical ignorance. But it is not a quantum state. A quantum state is a vector in Hilbert space. Neither $|0\rangle$ nor $|{+}\rangle$ is the right state, and their superposition $(|0\rangle + |{+}\rangle)/\sqrt{2}$ is wrong too — that would mean you are *coherently* in both, which is an entirely different physical situation with different interference properties and different measurement statistics.

You need a new object. The density operator is that object. It handles classical probability mixtures over quantum states, and it turns out to handle something stranger still: the state of a subsystem that is entangled with the rest of the world. Both cases arrive at the same formalism through different doors. This chapter opens both.

---

## The Density Operator

Let a system be prepared in state $|\psi_i\rangle$ with probability $p_i$, where $\sum_i p_i = 1$, $p_i \geq 0$, and the different states need not be orthogonal. The **density operator** is:

$$\hat\rho = \sum_i p_i\,|\psi_i\rangle\langle\psi_i|.$$

For the lab scenario: $\hat\rho = \tfrac{1}{2}|0\rangle\langle0| + \tfrac{1}{2}|{+}\rangle\langle{+}|$. In the $\{|0\rangle, |1\rangle\}$ basis, using $|{+}\rangle\langle{+}| = \tfrac{1}{2}\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$:

$$\hat\rho = \frac{1}{2}\begin{pmatrix}1&0\\0&0\end{pmatrix} + \frac{1}{4}\begin{pmatrix}1&1\\1&1\end{pmatrix} = \begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}.$$

Three properties follow directly from the definition:

**Hermitian:** $\hat\rho^\dagger = \hat\rho$ (each projector $|\psi_i\rangle\langle\psi_i|$ is Hermitian; real $p_i$ preserve this).

**Unit trace:** $\text{Tr}(\hat\rho) = \sum_i p_i\,\text{Tr}(|\psi_i\rangle\langle\psi_i|) = \sum_i p_i = 1$.

**Positive semidefinite:** $\langle\phi|\hat\rho|\phi\rangle = \sum_i p_i|\langle\phi|\psi_i\rangle|^2 \geq 0$ for any $|\phi\rangle$.

These three properties are necessary and sufficient: any operator satisfying all three is a valid density operator for some quantum state. The set of all density operators is convex — a mixture of density operators is again a density operator.

---

## Pure and Mixed: The Purity Criterion

A **pure state** is $\hat\rho = |\psi\rangle\langle\psi|$ for some single vector $|\psi\rangle$. Then $\hat\rho^2 = \hat\rho$, so $\text{Tr}(\hat\rho^2) = 1$.

For a mixed state, $\text{Tr}(\hat\rho^2) < 1$. This quantity is the **purity**. It ranges from $1$ (pure) down to $1/d$ for a $d$-dimensional system at maximal mixing. For the lab scenario:

$$\hat\rho^2 = \begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}^2 = \begin{pmatrix}10/16&4/16\\4/16&2/16\end{pmatrix}, \qquad \text{Tr}(\hat\rho^2) = \frac{12}{16} = \frac{3}{4}.$$

Wait — let me recompute that. $(3/4)^2 + (1/4)^2 = 9/16 + 1/16 = 10/16$ and $2(1/4)^2 = 2/16$, giving the trace as $10/16 + 2/16 = 12/16 = 3/4$? Let me redo: $(3/4)^2 + (1/4)(1/4) = 9/16 + 1/16$ for the $(0,0)$ entry, and $(1/4)^2 + (1/4)^2 = 2/16$ for the $(1,1)$ entry. Trace $= 10/16 + 2/16 = 12/16 = 3/4$. Hmm, but $9/16 + 1/16 = 10/16$ for entry $(0,0)$, and $(1/4)(1/4) + (1/4)(1/4) = 2/16$ for entry $(1,1)$ — so trace $= 10/16 + 2/16 = 12/16 = 3/4$. Confirm: purity $= 3/4 < 1$. Mixed, as expected.

One notation trap: $\text{Tr}(\hat\rho^2)$ is the purity; $[\text{Tr}(\hat\rho)]^2 = 1^2 = 1$ always. Keep the parentheses explicit.

---

## Expectation Values via the Trace

For any observable $\hat A$:

$$\langle\hat A\rangle = \text{Tr}(\hat\rho\,\hat A).$$

For a pure state $\hat\rho = |\psi\rangle\langle\psi|$, this reduces to the familiar $\langle\psi|\hat A|\psi\rangle$, since $\text{Tr}(|\psi\rangle\langle\psi|\hat A) = \langle\psi|\hat A|\psi\rangle$. The trace is basis-independent — compute in whatever basis makes the arithmetic easiest.

For a mixed state:

$$\langle\hat A\rangle = \text{Tr}(\hat\rho\,\hat A) = \sum_i p_i\langle\psi_i|\hat A|\psi_i\rangle,$$

the classical weighted average of quantum expectation values. This is exactly what you would write down from first principles for a probabilistic mixture.

---

## The Bloch Ball

Every single-qubit density matrix can be written in the Bloch representation:

$$\hat\rho = \frac{1}{2}\bigl(\hat I + \vec r\cdot\vec\sigma\bigr), \qquad \vec r = (r_x, r_y, r_z)\in\mathbb{R}^3, \quad |\vec r|\leq 1,$$

where $\vec\sigma = (\hat\sigma_x, \hat\sigma_y, \hat\sigma_z)$ and $r_i = \langle\hat\sigma_i\rangle = \text{Tr}(\hat\rho\,\hat\sigma_i)$.

Pure states sit on the surface of the unit sphere ($|\vec r| = 1$). For example, $|0\rangle\langle0| = \tfrac{1}{2}(\hat I + \hat\sigma_z)$ gives $\vec r = (0,0,1)$ — the north pole. The maximally mixed state $\hat\rho = \tfrac{1}{2}\hat I$ gives $\vec r = (0,0,0)$ — the center. Intermediate mixed states fill the interior.

Purity in terms of the Bloch vector: $\text{Tr}(\hat\rho^2) = \tfrac{1}{2}(1 + |\vec r|^2)$, which equals 1 only when $|\vec r| = 1$ and equals $1/2$ (the minimum for a qubit) when $|\vec r| = 0$.

This picture is not merely decorative. The Bloch vector components are directly measurable: $r_x = \langle\hat\sigma_x\rangle$, $r_y = \langle\hat\sigma_y\rangle$, $r_z = \langle\hat\sigma_z\rangle$. Quantum state tomography — the experimental reconstruction of $\hat\rho$ from measurements — is precisely the measurement of all three components. Single-qubit gates are rotations of the Bloch sphere. Decoherence is the process that shrinks $|\vec r|$ from the surface inward, turning a pure state into a mixed one. All the dynamics of an open qubit are visible in the geometry of this ball.

---

## The Partial Trace and Reduced Density Matrices

Here is the stranger case. Two systems $A$ and $B$ have a joint state $\hat\rho_{AB}$ on $\mathcal{H}_A\otimes\mathcal{H}_B$. You want to describe subsystem $A$ alone — making predictions only about measurements on $A$.

The **partial trace** over $B$ gives the **reduced density matrix** of $A$:

$$\hat\rho_A = \text{Tr}_B(\hat\rho_{AB}) \equiv \sum_j\langle j|_B\,\hat\rho_{AB}\,|j\rangle_B,$$

where $\{|j\rangle_B\}$ is any orthonormal basis of $\mathcal{H}_B$. This is the unique state of $A$ that correctly predicts the statistics of every observable $\hat A\otimes\hat I_B$. The partial trace is not a measurement; it is a mathematical operation that discards $B$ by averaging over all its states.

The result that matters: even when $\hat\rho_{AB}$ is pure, the reduced state $\hat\rho_A$ can be mixed — maximally mixed, even. This happens when $A$ and $B$ are entangled. Entanglement is not a vague notion of correlation; it is the precise condition under which a pure joint state cannot be described by any pure state of its parts.

---

## Worked Example — Reduced Density Matrix of One Bell-State Qubit

Take two qubits in the Bell state:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr).$$

This is a pure joint state: $\hat\rho_{AB} = |\Phi^+\rangle\langle\Phi^+|$.

**Step 1: Expand the outer product.**

$$\hat\rho_{AB} = \frac{1}{2}\bigl(|00\rangle\langle00| + |00\rangle\langle11| + |11\rangle\langle00| + |11\rangle\langle11|\bigr).$$

**Step 2: Partial trace over qubit $B$.** Using basis $\{|0\rangle_B, |1\rangle_B\}$:

$$\hat\rho_A = \langle0|_B\,\hat\rho_{AB}\,|0\rangle_B + \langle1|_B\,\hat\rho_{AB}\,|1\rangle_B.$$

Evaluate term by term. The operator $|ij\rangle\langle kl|$ factors as $|i\rangle_A\langle k|_A\otimes|j\rangle_B\langle l|_B$, so $\langle m|_B(|i\rangle_A\langle k|_A\otimes|j\rangle_B\langle l|_B)|n\rangle_B = |i\rangle_A\langle k|_A\cdot\langle m|j\rangle\langle l|n\rangle$. Summing over $m = 0,1$ with $n = m$:

$$\hat\rho_A = \frac{1}{2}\bigl(|0\rangle_A\langle0|_A + |1\rangle_A\langle1|_A\bigr) = \frac{1}{2}\hat I.$$

The off-diagonal terms $|00\rangle\langle11|$ and $|11\rangle\langle00|$ each contribute zero after tracing (they require $\langle0|1\rangle = 0$).

**The result.** $\hat\rho_A = \tfrac{1}{2}\hat I$. Bloch vector: $\vec r = (0,0,0)$. Purity: $\text{Tr}(\hat\rho_A^2) = \tfrac{1}{2}$.

Qubit $A$ is in the maximally mixed state. Every measurement on $A$ alone, in any basis, gives outcomes with equal probability $1/2$. There is nothing to learn from measuring $A$ in isolation — all the information is in the correlations between $A$ and $B$, and those correlations vanish the moment $B$ is discarded. A perfectly pure joint state has yielded the most mixed possible subsystem.

For comparison: if the joint state is a product state $|00\rangle\langle00|$, then $\hat\rho_A = |0\rangle\langle0|$, purity $= 1$, the subsystem is pure. The subsystem is mixed if and only if the joint state is entangled (for pure joint states). This is the precise content of the partial trace.

---

## Still Puzzling

The density matrix resolves the question of *how* to describe incomplete information. It does not resolve the question of *why* information becomes incomplete.

When the joint state of qubit plus environment is pure and you trace out the environment, you get $\hat\rho$ for the qubit — a mathematically precise and physically useful operation. But you have discarded the environment. The qubit is entangled with those stray phonons and nuclear spins. The joint system is still pure. Decoherence explains why the qubit's density matrix becomes diagonal in the pointer basis, so that measurements *look* classical. It does not explain why any particular outcome occurs. The trace operation that gives you $\hat\rho_A$ is irreversible only in practice; in principle, if you could gather all environmental degrees of freedom, the full joint state remains pure and unitary evolution continues.

Whether the qubit has a definite pure state that the formalism merely fails to track — whether the mixedness is epistemic (a matter of ignorance) or ontic (a matter of fact) — is a question about the interpretation of quantum mechanics. The formalism is settled. The meaning is not.

---

## The +1 — Simulation Exercise

### The Prompt

````
Build a single self-contained HTML file called 02-bloch-ball-explorer.html using
D3 v7 from a CDN. No other dependencies.

Two panels side by side in one SVG (total 800 × 500):

PANEL A — Bloch ball cross-section (400 × 500).
Draw a circle of radius 180 px representing the equatorial slice (r_z=0)
of the Bloch ball. Dark grey unit circle. Labeled axes: r_x (right), r_y (up).

Three sliders below:
  r_x: -1 to 1, step 0.01, default 1.0
  r_y: -1 to 1, step 0.01, default 0.0
  r_z: -1 to 1, step 0.01, default 0.0

After every slider change:
  1. If r_x^2 + r_y^2 + r_z^2 > 1, rescale r uniformly so |r| = 1.
     Update slider displays to reflect clamped values.
  2. Orange filled circle (radius 8 px) at (r_x, r_y) * 180 px.
  3. Orange arrow from center to that dot.

PANEL B — Density matrix and derived quantities (400 × 500).
Compute rho = (1/2)(I + r.sigma) with Pauli matrices:
  sigma_x = [[0,1],[1,0]]
  sigma_y = [[0,-i],[i,0]]
  sigma_z = [[1,0],[0,-1]]

Display the 2×2 density matrix as a grid of four labeled cells.
Each cell shows:
  - Re part as a horizontal bar (range -0.5 to 0.5, steelblue)
  - Im part as a horizontal bar (range -0.5 to 0.5, coral)
  - Numerical value: "Re: X.XXX  Im: X.XXX"

Below the matrix:
  - Purity = (1 + |r|^2) / 2, displayed to 4 decimal places
  - |r| = Bloch vector magnitude, to 4 decimal places
  - State: "PURE" (green) if |r| > 0.9999, else "MIXED" (orange)
  - Eigenvalues of rho (compute and display)

Three preset buttons:
  "|0>" — r = (0,0,1)
  "|+>" — r = (1,0,0)
  "Maximally mixed" — r = (0,0,0)

Verification:
  - Display warning in red if |Tr(rho) - 1| > 1e-4.
  - Verify Tr(rho^2) = (1 + |r|^2)/2 matches to 1e-4; display mismatch warning if not.

Comments at every physics step.
````

### Exploration Tasks

**The surface is all pure.** Set preset $|0\rangle$. Verify the matrix matches $\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$. Move $r_z$ from $+1$ to $-1$. The purity stays at 1 throughout — you are staying on the surface.

**Inward to the center.** Set $r_x = r_y = 0$ and decrease $|r_z|$ toward 0. Watch the purity fall from 1 to 0.5. The off-diagonal elements are zero throughout. What changes is the diagonal: from (1, 0) to (0.5, 0.5).

**Clamping.** Set $r_x = 0.6$, $r_y = 0$, $r_z = 0$ (purity = 0.68). Now increase $r_y$ to 0.8. With $r_x = 0.6$, $r_y = 0.8$: $|\vec r|^2 = 0.36 + 0.64 = 1$. The simulation should not clamp. Now set $r_z = 0.1$ — now $|\vec r|^2 > 1$ and the clamping triggers. Read off the rescaled values and the purity.

**The Bell state.** Set the simulation to $\vec r = (0,0,0)$ (maximally mixed preset). Confirm the matrix shows $\bigl(\begin{smallmatrix}1/2&0\\0&1/2\end{smallmatrix}\bigr)$, purity $= 0.5$, eigenvalues both $= 0.5$. This is what the partial trace of $|\Phi^+\rangle$ produces for qubit $A$.

---

## References

- Fano, U. (1957). "Description of states in quantum mechanics by density matrix and operator techniques." *Reviews of Modern Physics*, 29(1), 74–93. [verify]
- Nielsen, M.A. and Chuang, I.L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. §2.4 (density operators and reduced density matrices), §2.1.2 (Bloch sphere). [verify]
- Preskill, J. *Lecture Notes for Physics 219/CS 219: Quantum Information and Computation*, Chapter 2. http://www.theory.caltech.edu/~preskill/ph219/ [verify]
- Sakurai, J.J. and Napolitano, J. (2020). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. §3.4 (density matrix and ensembles). [verify]
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer. Chapter 2. [verify]

---

*Chapter 2 follows: the time evolution of open quantum systems. Once the joint state of system plus environment is entangled, the system alone evolves under a quantum channel — a completely positive, trace-preserving map — rather than unitary evolution. The Lindblad master equation is the differential form of this evolution, and it explains why the Bloch vector shrinks inward.*
