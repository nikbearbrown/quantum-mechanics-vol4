# Chapter 1 — Mixed States and the Density Matrix

## TL;DR

A quantum state is pure when you know everything about it; mixed when you do not — or when the system is entangled with something you cannot see. The density operator $\rho$ is the object that handles both cases in a single formalism. Purity is a number: $\text{Tr}(\rho^2) = 1$ means pure, less than 1 means mixed. Expectation values come from $\langle A \rangle = \text{Tr}(\rho A)$. Single-qubit states fill a ball in $\mathbb{R}^3$ — pure states on the surface, mixed states inside. And the strangest result of the chapter: take one qubit of a maximally entangled pair, trace over the other, and you get the most mixed state possible. A perfectly pure joint state can have maximally mixed subsystems.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **Define** the density operator $\rho$ and state its three defining properties — Hermitian, positive semidefinite, unit trace. *(Remember)*
2. **Distinguish** pure from mixed states using the purity criterion $\text{Tr}(\rho^2)$, and explain why a subsystem of an entangled pure state can be mixed. *(Understand)*
3. **Compute** expectation values of observables using $\langle A \rangle = \text{Tr}(\rho A)$ for both pure and mixed states. *(Apply)*
4. **Represent** any single-qubit state as a point in the Bloch ball and read off purity from the length of the Bloch vector. *(Apply)*
5. **Derive** the reduced density matrix of one qubit of a Bell state by taking the partial trace, and interpret the result. *(Analyze)*

---

## Opening: the box that may or may not have been opened

Here is the situation. A laboratory produces qubits by one of two methods, chosen at random with equal probability. Method 1 prepares $|0\rangle$ — the spin-up eigenstate of $\hat\sigma_z$. Method 2 prepares $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ — spin pointing along $+\hat{x}$. The lab hands you a qubit and does not tell you which method was used.

What is the state of your qubit?

Your first instinct might be: "It is either $|0\rangle$ or $|{+}\rangle$ — I just do not know which." That is a correct description of your *classical ignorance*, but it is not a quantum state. A quantum state, in the formalism you learned in earlier volumes, is a vector in Hilbert space. Neither $|0\rangle$ nor $|{+}\rangle$ is the right state, and their superposition $(|0\rangle + |{+}\rangle)/\sqrt{2}$ is wrong too — that would mean you are *coherently* in both, which is a completely different physical situation.

You need a new object. The density operator is that object. It handles classical probability mixtures over quantum states, and it turns out to handle something even stranger: the state of a subsystem that is entangled with the rest of the world. Both cases arrive at the same formalism through different doors. This chapter opens both doors.

---

## Core development

### The density operator

Let a system be prepared in state $|\psi_i\rangle$ with probability $p_i$, where the $p_i$ are classical probabilities: $\sum_i p_i = 1$, $p_i \geq 0$, and the different $|\psi_i\rangle$ need not be orthogonal. The **density operator** (also called the **density matrix** when a basis is chosen) is:

$$\hat\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|.$$

For the lab scenario above, $\hat\rho = \tfrac{1}{2}|0\rangle\langle 0| + \tfrac{1}{2}|{+}\rangle\langle{+}|$. In the $\{|0\rangle, |1\rangle\}$ basis, where $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$:

$$\hat\rho = \frac{1}{2}\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix} + \frac{1}{2}\cdot\frac{1}{2}\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix} = \begin{pmatrix}3/4 & 1/4 \\ 1/4 & 1/4\end{pmatrix}.$$

Three properties follow directly from the definition and can be taken as axioms:

1. **Hermitian:** $\hat\rho^\dagger = \hat\rho$ (each $|\psi_i\rangle\langle\psi_i|$ is Hermitian; real $p_i$ preserve this).
2. **Unit trace:** $\text{Tr}(\hat\rho) = \sum_i p_i \text{Tr}(|\psi_i\rangle\langle\psi_i|) = \sum_i p_i \cdot 1 = 1$.
3. **Positive semidefinite:** $\langle\phi|\hat\rho|\phi\rangle = \sum_i p_i |\langle\phi|\psi_i\rangle|^2 \geq 0$ for any $|\phi\rangle$.

Conversely, any operator satisfying these three properties is a valid density operator for some quantum state. The set of all density operators is convex: a mixture of density operators is again a density operator.

### Pure versus mixed: the purity criterion

A **pure state** is one where you have complete information: $\hat\rho = |\psi\rangle\langle\psi|$ for a single $|\psi\rangle$. For a pure state, $\hat\rho^2 = |\psi\rangle\langle\psi|\psi\rangle\langle\psi| = |\psi\rangle\langle\psi| = \hat\rho$, so $\text{Tr}(\hat\rho^2) = \text{Tr}(\hat\rho) = 1$.

For a mixed state, $\text{Tr}(\hat\rho^2) < 1$. This quantity is called the **purity** and serves as a scalar measure: it ranges from $1$ (pure) down to $1/d$ for a $d$-dimensional system at maximal mixing. You can verify this for the lab-scenario matrix above:

$$\hat\rho^2 = \begin{pmatrix}3/4 & 1/4 \\ 1/4 & 1/4\end{pmatrix}^2 = \begin{pmatrix}10/16 & 4/16 \\ 4/16 & 2/16\end{pmatrix}, \qquad \text{Tr}(\hat\rho^2) = \frac{12}{16} = \frac{3}{4} - \frac{1}{16} = \frac{11}{16}.$$

Since $11/16 < 1$, the state is mixed — confirming our expectation.

> **Notation trap.** $\text{Tr}(\hat\rho^2)$ is the purity. $[\text{Tr}(\hat\rho)]^2$ is just $1^2 = 1$, always. Keep those parentheses explicit.

### Expectation values via the trace

The payoff for working with $\hat\rho$ is a single compact formula for expectation values. For any observable $\hat A$:

$$\langle \hat A \rangle = \text{Tr}(\hat\rho\, \hat A).$$

For a pure state $\hat\rho = |\psi\rangle\langle\psi|$ this reduces to the familiar $\langle\psi|\hat A|\psi\rangle$, since $\text{Tr}(|\psi\rangle\langle\psi|\hat A) = \langle\psi|\hat A|\psi\rangle$. The trace is basis-independent, so you compute in any convenient basis — whatever makes the arithmetic easiest.

For a mixed state $\hat\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$:

$$\langle \hat A \rangle = \text{Tr}(\hat\rho\, \hat A) = \sum_i p_i \langle\psi_i|\hat A|\psi_i\rangle,$$

which is the classical weighted average of quantum expectation values — exactly what you would write down if you reasoned from first principles about a probabilistic mixture.

### The Bloch ball

Every single-qubit density matrix can be written in the **Bloch representation**:

$$\hat\rho = \frac{1}{2}\bigl(\hat I + \vec r \cdot \vec\sigma\bigr), \qquad \vec r = (r_x, r_y, r_z) \in \mathbb{R}^3, \quad |\vec r| \leq 1.$$

Here $\vec\sigma = (\hat\sigma_x, \hat\sigma_y, \hat\sigma_z)$ is the vector of Pauli operators and $\vec r$ is the **Bloch vector**. The components are the expectation values: $r_i = \langle\hat\sigma_i\rangle = \text{Tr}(\hat\rho\,\hat\sigma_i)$.

- **Pure states** sit on the surface of the unit sphere ($|\vec r| = 1$). For example, $|0\rangle\langle 0| = \tfrac{1}{2}(\hat I + \hat\sigma_z)$ gives $\vec r = (0, 0, 1)$ — the north pole.
- **Maximally mixed** gives $\hat\rho = \tfrac{1}{2}\hat I$, so $\vec r = (0, 0, 0)$ — the center.
- **Intermediate mixed states** fill the interior: $0 < |\vec r| < 1$.

Purity in terms of the Bloch vector: $\text{Tr}(\hat\rho^2) = \tfrac{1}{2}(1 + |\vec r|^2)$, which equals 1 only when $|\vec r| = 1$ and equals $1/2$ (minimum for a qubit) when $|\vec r| = 0$.

This geometric picture is not merely decorative. The Bloch vector components are directly measurable: $r_x = \langle\hat\sigma_x\rangle$, $r_y = \langle\hat\sigma_y\rangle$, $r_z = \langle\hat\sigma_z\rangle$. Quantum state tomography — the experimental reconstruction of $\hat\rho$ from measurements — amounts to measuring all three components. Single-qubit gates are rotations of the Bloch sphere. Decoherence is the process that shrinks $|\vec r|$ from the surface inward, turning a pure state into a mixed one. All the dynamics of an open qubit are visible in the geometry of this ball.

### The partial trace and reduced density matrices

Now comes the strange case. Suppose two systems, $A$ and $B$, have a joint state described by a density operator $\hat\rho_{AB}$ on $\mathcal{H}_A \otimes \mathcal{H}_B$. You want to describe subsystem $A$ alone, making predictions only about measurements on $A$.

The **partial trace** over $B$ gives the **reduced density matrix** of $A$:

$$\hat\rho_A = \text{Tr}_B(\hat\rho_{AB}) \equiv \sum_j \langle j|_B\, \hat\rho_{AB}\, |j\rangle_B,$$

where $\{|j\rangle_B\}$ is any orthonormal basis of $\mathcal{H}_B$. This is the unique state of subsystem $A$ that correctly predicts the statistics of every observable $\hat A \otimes \hat I_B$:

$$\langle \hat A \rangle = \text{Tr}_{AB}(\hat\rho_{AB}\, (\hat A \otimes \hat I_B)) = \text{Tr}_A(\hat\rho_A\, \hat A).$$

The partial trace is not a projection or a measurement; it is a mathematical operation that discards one subsystem, averaging over all possible states of $B$.

The stunning result: even when the joint state $\hat\rho_{AB}$ is pure, the reduced state $\hat\rho_A$ can be mixed — maximally mixed, even. This happens when $A$ and $B$ are entangled. Entanglement is not a vague notion of correlation; it is the precise condition under which a pure joint state cannot be described by any pure state of its parts.

---

## Worked example: the reduced density matrix of one qubit of a Bell state

**The setup.** Consider two qubits in the Bell state:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr).$$

This is a pure state of the joint system: $\hat\rho_{AB} = |\Phi^+\rangle\langle\Phi^+|$.

**Step 1: Write out the joint density matrix.** Expand the outer product:

$$\hat\rho_{AB} = \frac{1}{2}\bigl(|00\rangle\langle 00| + |00\rangle\langle 11| + |11\rangle\langle 00| + |11\rangle\langle 11|\bigr).$$

**Step 2: Take the partial trace over qubit $B$.** Using the basis $\{|0\rangle_B, |1\rangle_B\}$:

$$\hat\rho_A = \langle 0|_B\,\hat\rho_{AB}\,|0\rangle_B + \langle 1|_B\,\hat\rho_{AB}\,|1\rangle_B.$$

Evaluate term by term. The operator $|ij\rangle\langle kl|$ acts on $\mathcal{H}_A \otimes \mathcal{H}_B$ as $|i\rangle_A\langle k|_A \otimes |j\rangle_B\langle l|_B$. Then $\langle m|_B (|i\rangle_A\langle k|_A \otimes |j\rangle_B\langle l|_B) |n\rangle_B = |i\rangle_A\langle k|_A \cdot \langle m|j\rangle\langle l|n\rangle$.

Tracing out $B$ (summing over $m = 0, 1$, using $n = m$):

$$\hat\rho_A = \frac{1}{2}\bigl[\langle 0|_B\bigl(|00\rangle\langle 00| + |00\rangle\langle 11| + |11\rangle\langle 00| + |11\rangle\langle 11|\bigr)|0\rangle_B + \langle 1|_B(\cdots)|1\rangle_B\bigr]$$

$$= \frac{1}{2}\bigl[\underbrace{|0\rangle_A\langle 0|_A \cdot 1}_{\text{from }|00\rangle\langle 00|, m=0} + \underbrace{0}_{\text{from }|00\rangle\langle 11|, m=0} + 0 + 0\bigr] + \frac{1}{2}\bigl[0 + 0 + 0 + \underbrace{|1\rangle_A\langle 1|_A \cdot 1}_{\text{from }|11\rangle\langle 11|, m=1}\bigr]$$

$$= \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1| = \frac{1}{2}\hat I.$$

**The result.** $\hat\rho_A = \tfrac{1}{2}\hat I$. The Bloch vector is $\vec r = (0, 0, 0)$ — the center of the ball. The purity is $\text{Tr}(\hat\rho_A^2) = \text{Tr}(\tfrac{1}{4}\hat I) = \tfrac{1}{2}$.

**The lesson.** Qubit $A$ is in the *maximally mixed* state. Every measurement you make on $A$ alone — in any basis — gives outcomes with equal probability $1/2$. There is nothing to learn from measuring $A$ in isolation. All the information is in the correlations between $A$ and $B$, which vanish the moment you discard $B$ by tracing it out. A pure joint state has yielded the most mixed possible subsystem. This is entanglement made concrete in the density matrix formalism.

**The limit.** The partial trace also applies when the joint state is *not* entangled. Suppose $\hat\rho_{AB} = |00\rangle\langle 00|$ (a product state). Then $\hat\rho_A = |0\rangle\langle 0|$, purity $= 1$: the subsystem is pure. The reduced state is mixed if and only if the joint state is entangled (for pure joint states). This is the precise statement.

---

## Common misconceptions

**"The density matrix is just a way of tracking classical uncertainty — there's no new physics."**
Wrong, in two ways. First, a classically ignorant mixture of $|0\rangle$ and $|{+}\rangle$ (as in the opening scenario) produces a specific density matrix with specific off-diagonal elements. Change the probabilities or the states, and you get a different observable prediction. The density matrix is not merely bookkeeping — it is the complete specification of measurement statistics. Second, and more importantly, the mixed state that arises from tracing out an entangled environment is *not* the same as any classical mixture over pure states with definite hidden labels. There is no deeper description of qubit $A$ of a Bell pair in terms of a pure state that the label would specify. The mixedness is irreducible at the level of the subsystem.

**"If the purity $\text{Tr}(\hat\rho^2) < 1$, the state must be a classical mixture."**
For a subsystem, no. The joint state $|\Phi^+\rangle$ is as pure as any state can be. The *subsystem* $\hat\rho_A$ has purity $1/2$ — not because of classical ignorance, but because the information is stored in correlations, not in either qubit alone. The purity criterion tells you about the state *of the subsystem*; it does not say anything about whether that mixedness has a classical or quantum origin.

**"$\hat\rho = |\psi\rangle\langle\psi|$ for some unknown $|\psi\rangle$ — you just don't know which one."**
This is the most persistent error. A qubit in state $\hat\rho_A = \tfrac{1}{2}\hat I$ does *not* have a definite pure state that you are ignorant of. If it did, there would be some basis in which it was definitely $|0\rangle$ or $|1\rangle$ (with probabilities $1/2, 1/2$). But $\tfrac{1}{2}\hat I$ gives uniform probability in *every* basis simultaneously — no such definite-but-unknown basis exists. When mixedness comes from entanglement, the "hidden pure state" interpretation fails completely.

**"You can always find a unique decomposition $\hat\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$."**
The decomposition of a mixed state into pure states is *not* unique. Any mixed state can be decomposed in infinitely many ways as a mixture of pure states. The density matrix encodes all of these decompositions simultaneously, and no experiment can distinguish one decomposition from another. This is sometimes called the unitary freedom in the operator-sum representation.

---

## Exercises

### Warm-up

1. *[Tests: density matrix construction, purity]* A source prepares a qubit in state $|1\rangle$ with probability $3/4$ and in state $|{-}\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$ with probability $1/4$. (a) Write the density matrix $\hat\rho$ in the $\{|0\rangle, |1\rangle\}$ basis. (b) Compute the purity $\text{Tr}(\hat\rho^2)$. (c) Is this state pure or mixed? *Difficulty: warm-up.*

2. *[Tests: Bloch vector, expectation values]* For the state $\hat\rho = \begin{pmatrix} 2/3 & 0 \\ 0 & 1/3 \end{pmatrix}$, compute (a) the Bloch vector $\vec r = (r_x, r_y, r_z)$ using $r_i = \text{Tr}(\hat\rho\,\hat\sigma_i)$, (b) the magnitude $|\vec r|$, and (c) the purity $\tfrac{1}{2}(1 + |\vec r|^2)$. Verify this matches $\text{Tr}(\hat\rho^2)$ computed directly. *Difficulty: warm-up.*

3. *[Tests: trace formula for expectation values]* A qubit is in the state $\hat\rho = \tfrac{1}{2}|{+}\rangle\langle{+}| + \tfrac{1}{2}|{-}\rangle\langle{-}|$. (a) Write $\hat\rho$ as a matrix. (b) Compute $\langle\hat\sigma_x\rangle$ using $\text{Tr}(\hat\rho\,\hat\sigma_x)$. (c) Compute $\langle\hat\sigma_z\rangle$. (d) Describe the Bloch vector in one sentence. *Difficulty: warm-up.*

### Application

4. *[Tests: partial trace computation]* Two qubits are in the state $|\psi\rangle = \tfrac{1}{\sqrt{3}}(|00\rangle + |01\rangle + |11\rangle)$. (a) Write the joint density matrix $\hat\rho_{AB} = |\psi\rangle\langle\psi|$ as a $4\times 4$ matrix in the basis $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$. (b) Compute the reduced density matrix $\hat\rho_A = \text{Tr}_B(\hat\rho_{AB})$. (c) Compute the purity $\text{Tr}(\hat\rho_A^2)$. (d) Is the joint state entangled? Justify your answer using the purity of $\hat\rho_A$. *Difficulty: application.*

5. *[Tests: no-signaling from partial trace, local operation]* Alice and Bob share $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$. Alice applies the Pauli $X$ gate to her qubit, producing a new joint state. (a) What is the new joint state? (b) Compute Bob's reduced density matrix before and after Alice's operation. (c) Explain in one sentence why this confirms no-signaling. *Difficulty: application.*

6. *[Tests: Bloch ball geometry, purity, decoherence interpretation]* A qubit starts in state $|{+}\rangle$ (Bloch vector along $+\hat x$). After a decoherence process, its state is $\hat\rho = \tfrac{1}{2}\hat I + \tfrac{1}{4}\hat\sigma_x$. (a) What is the Bloch vector? (b) Is this a pure state? (c) By what factor has the purity changed from the initial value? (d) Describe geometrically what the decoherence process did to the Bloch vector. *Difficulty: application.*

### Synthesis and beyond

7. *[Tests: partial trace for product states vs. entangled states]* Prove the following: if two qubits are in a product state $|\psi_{AB}\rangle = |\phi\rangle_A \otimes |\chi\rangle_B$, then the reduced density matrix $\hat\rho_A = \text{Tr}_B(|\psi_{AB}\rangle\langle\psi_{AB}|)$ is the pure state $|\phi\rangle\langle\phi|$. Conclude that $\text{Tr}(\hat\rho_A^2) < 1$ implies the joint state is *not* a product state. This is the density-matrix proof of entanglement. *Difficulty: synthesis.*

8. *[Tests: uniqueness failure of decompositions, physical interpretation]* The maximally mixed state $\hat\rho = \tfrac{1}{2}\hat I$ can be written as $\tfrac{1}{2}|0\rangle\langle 0| + \tfrac{1}{2}|1\rangle\langle 1|$ (a mixture of $z$-eigenstates). (a) Show that it can also be written as $\tfrac{1}{2}|{+}\rangle\langle{+}| + \tfrac{1}{2}|{-}\rangle\langle{-}|$ (a mixture of $x$-eigenstates). (b) Compute $\langle\hat\sigma_z\rangle$ and $\langle\hat\sigma_x\rangle$ for both decompositions. (c) Explain why these two decompositions are physically indistinguishable, and why this means you cannot determine "which mixture" the lab is actually using. *Difficulty: synthesis.*

---

## Still puzzling

The density matrix resolves the question of *how* to describe incomplete information. It does not resolve the question of *why* information becomes incomplete. When the joint state of qubit plus environment is pure and you trace out the environment to get $\hat\rho$ for the qubit, you have done something mathematically precise and physically useful. But you have also discarded the environment. The qubit really is entangled with those stray phonons and nuclear spins. The joint system is still pure. Measuring the qubit collapses the joint state — but *which* outcome? Decoherence explains why the qubit's density matrix becomes diagonal in the pointer basis, so that measurement *looks* classical. It does not explain why any particular outcome occurs. The trace operation that gives you $\hat\rho_A$ is irreversible only in practice; in principle, if you could gather all the environmental degrees of freedom, the full joint state remains pure and unitary evolution continues. The density matrix is an epistemically useful tool. Whether it is ontologically complete — whether the qubit has a definite pure state that the formalism merely fails to track — is a question about the interpretation of quantum mechanics. The formalism is settled. The meaning is not.

---

## The +1 — Simulation Exercise

### The prompt (paste directly into Claude Code or your preferred LLM coding assistant)

```
Build me a single self-contained HTML file called 02-bloch-ball-explorer.html using
D3 v7 from a CDN, no other dependencies.

The simulation has two panels side by side in one SVG (total 800 x 500):

PANEL A — Bloch ball cross-section (400 x 500).
Draw a circle of radius 180 px representing the equatorial cross-section
(r_z = 0 slice) of the Bloch ball. Show the unit circle in dark grey.
Add three labeled axes: r_x (right), r_y (up), and a label "r_z slider
controls depth" at the bottom.

Three sliders below the circle control the Bloch vector components:
  r_x: range -1 to 1, step 0.01, default 1.0
  r_y: range -1 to 1, step 0.01, default 0.0
  r_z: range -1 to 1, step 0.01, default 0.0

After every slider change:
  1. Clamp the vector so that r_x^2 + r_y^2 + r_z^2 <= 1.
     If the user's slider values give |r|^2 > 1, rescale r uniformly
     so that |r| = 1 (project onto the Bloch sphere surface).
     Update the slider displays to reflect the clamped values.
  2. Draw an orange filled circle of radius 8 px at (r_x, r_y) * 180
     in panel-A coordinates to show the projection of the Bloch vector
     onto the equatorial plane.
  3. Draw an orange arrow from the center of the circle to that dot.
  4. Show a small grey dot at the center for |r| = 0 reference.

PANEL B — Density matrix and derived quantities (400 x 500).
Compute the 2x2 density matrix rho = (1/2)(I + r . sigma) where sigma
are Pauli matrices:
  sigma_x = [[0,1],[1,0]]
  sigma_y = [[0,-i],[i,0]]  (display real/imag parts)
  sigma_z = [[1,0],[0,-1]]

Display the density matrix as four labeled cells in a 2x2 grid,
showing rho[0,0], rho[0,1], rho[1,0], rho[1,1].
For each entry show:
  - Re part as a bar (horizontal, -0.5 to 0.5 range, color steelblue)
  - Im part as a bar (horizontal, -0.5 to 0.5 range, color coral)
  - Numerical value below: "Re: X.XXX  Im: X.XXX"

Below the matrix grid show:
  - Purity = Tr(rho^2) = (1 + |r|^2) / 2, displayed to 4 decimal places
  - |r| = magnitude of the Bloch vector, displayed to 4 decimal places
  - State classification: "PURE" (green) if |r| > 0.9999, else "MIXED" (orange)
  - Bloch vector display: r = (r_x, r_y, r_z) to 3 decimal places

Three preset buttons below: 
  "|0>" — sets r = (0,0,1); 
  "|+>" — sets r = (1,0,0);
  "Maximally mixed" — sets r = (0,0,0).

Physics rules:
- rho must satisfy Tr(rho) = 1 at all times; verify this and display
  a warning in red text if |Tr(rho) - 1| > 1e-4.
- Purity = Tr(rho^2) must equal (1 + |r|^2) / 2; verify both
  computations match to 1e-4 or display a mismatch warning.
- For pure states (|r| = 1), the eigenvalues of rho should be 1 and 0;
  for maximally mixed (r = 0), both eigenvalues are 0.5. Show eigenvalues.
```

### Exploration tasks

1. Set the presets to $|0\rangle$ and verify the density matrix matches $\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$. Move $r_z$ from $+1$ to $-1$ continuously. Watch the purity — does it ever drop below $1$? Why not?

2. Set $r_z = 0$ and vary $r_x$ and $r_y$ freely. Identify the circle of pure states in the equatorial cross-section. Now set $r_x = r_y = 0$ and vary $r_z$ toward $0$. Watch the purity drop to $0.5$ at the center. What do the off-diagonal elements do?

3. Set $r = (0.6, 0, 0)$. Note the purity. Now set $r = (0.6, 0.8, 0)$ — the clamping routine should trigger. What does the simulation do? Read off the new purity and verify the formula $\text{Tr}(\hat\rho^2) = \tfrac{1}{2}(1 + |\vec r|^2)$.

4. The Bell-state result says $\hat\rho_A = \tfrac{1}{2}\hat I$ for one qubit of $|\Phi^+\rangle$. Set the simulation to this state ($\vec r = 0$). Confirm: all matrix entries match $\hat\rho = \begin{pmatrix}1/2 & 0 \\ 0 & 1/2\end{pmatrix}$, purity $= 0.5$, eigenvalues $= 0.5, 0.5$. This is what the reduced density matrix of a maximally entangled qubit looks like.

---

## References

- Fano, U. (1957). Description of states in quantum mechanics by density matrix and operator techniques. *Reviews of Modern Physics*, 29(1), 74–93. [verify]
- Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. §2.4 (density operators and reduced density matrices), §2.1.2 (Bloch sphere). [verify]
- Preskill, J. Lecture Notes for Physics 219/CS 219: Quantum Information and Computation. Chapter 2. http://www.theory.caltech.edu/~preskill/ph219/ [verify]
- Sakurai, J. J., & Napolitano, J. (2020). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §3.4 (density matrix and ensembles). [verify]
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer. Chapter 2 (decoherence and the density matrix). [verify]
- Huang, H.-Y., Kueng, R., & Preskill, J. (2020). Predicting many properties of a quantum system from very few measurements. *Nature Physics*, 16, 1050–1057. https://doi.org/10.1038/s41567-020-0932-7 [verify]
- Rondin, L., Tetienne, J.-P., Hingant, T., Roch, J.-F., Maletinsky, P., & Jacques, V. (2014). Magnetometry with nitrogen-vacancy defects in diamond. *Reports on Progress in Physics*, 77(5), 056503. https://doi.org/10.1088/0034-4885/77/5/056503 [verify]
