# Chapter 1 — Mixed States and the Density Matrix

In many experiments, a system is not prepared in a single, definite quantum state. Instead, a source might produce a qubit in one of several possible states, with some probability assigned to each. A laboratory, for example, might prepare qubits by one of two methods, chosen at random with equal probability: Method 1 prepares $|0\rangle$, and Method 2 prepares $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. If the lab hands you a qubit without telling you which method was used, you need a way to describe your uncertainty about its state.

A state vector alone is not sufficient here. A quantum state is a vector in Hilbert space, and neither $|0\rangle$ nor $|{+}\rangle$ individually represents the situation — nor does any superposition of them, because a superposition $(|0\rangle + |{+}\rangle)/\sqrt{2}$ represents coherent quantum interference between the two, which has different measurement statistics than a classical probabilistic mixture.

The **density operator** is the mathematical object that handles this situation. It describes both classical probability mixtures over quantum states and — as we will see — the state of a subsystem that is entangled with the rest of the world. This chapter introduces the density operator and develops the tools needed to work with it.

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

For a pure state $\hat\rho = |\psi\rangle\langle\psi|$, this reduces to the familiar $\langle\psi|\hat A|\psi\rangle$, since $\text{Tr}(|\psi\rangle\langle\psi|\hat A) = \langle\psi|\hat A|\psi\rangle$. The trace is basis-independent — we can compute in whatever basis makes the arithmetic easiest.

For a mixed state:

$$\langle\hat A\rangle = \text{Tr}(\hat\rho\,\hat A) = \sum_i p_i\langle\psi_i|\hat A|\psi_i\rangle,$$

which is the classical weighted average of quantum expectation values. This is exactly what we would write down from first principles for a probabilistic mixture.

---

## The Bloch Ball

Every single-qubit density matrix can be written in the Bloch representation:

$$\hat\rho = \frac{1}{2}\bigl(\hat I + \vec r\cdot\vec\sigma\bigr), \qquad \vec r = (r_x, r_y, r_z)\in\mathbb{R}^3, \quad |\vec r|\leq 1,$$

where $\vec\sigma = (\hat\sigma_x, \hat\sigma_y, \hat\sigma_z)$ and $r_i = \langle\hat\sigma_i\rangle = \text{Tr}(\hat\rho\,\hat\sigma_i)$.

Pure states sit on the surface of the unit sphere ($|\vec r| = 1$). For example, $|0\rangle\langle0| = \tfrac{1}{2}(\hat I + \hat\sigma_z)$ gives $\vec r = (0,0,1)$ — the north pole. The maximally mixed state $\hat\rho = \tfrac{1}{2}\hat I$ gives $\vec r = (0,0,0)$ — the center. Intermediate mixed states fill the interior.

Purity in terms of the Bloch vector: $\text{Tr}(\hat\rho^2) = \tfrac{1}{2}(1 + |\vec r|^2)$, which equals 1 only when $|\vec r| = 1$ and equals $1/2$ (the minimum for a qubit) when $|\vec r| = 0$.

This picture is not merely geometric illustration. The Bloch vector components are directly measurable: $r_x = \langle\hat\sigma_x\rangle$, $r_y = \langle\hat\sigma_y\rangle$, $r_z = \langle\hat\sigma_z\rangle$. Quantum state tomography — the experimental reconstruction of $\hat\rho$ from measurements — is precisely the measurement of all three components. Single-qubit gates are rotations of the Bloch sphere. Decoherence is the process that shrinks $|\vec r|$ from the surface inward, turning a pure state into a mixed one. All the dynamics of an open qubit are visible in the geometry of this ball.

---

## The Partial Trace and Reduced Density Matrices

We now turn to the second situation that requires a density operator. Two systems $A$ and $B$ have a joint state $\hat\rho_{AB}$ on $\mathcal{H}_A\otimes\mathcal{H}_B$. We want to describe subsystem $A$ alone — making predictions only about measurements on $A$.

The **partial trace** over $B$ gives the **reduced density matrix** of $A$:

$$\hat\rho_A = \text{Tr}_B(\hat\rho_{AB}) \equiv \sum_j\langle j|_B\,\hat\rho_{AB}\,|j\rangle_B,$$

where $\{|j\rangle_B\}$ is any orthonormal basis of $\mathcal{H}_B$. This is the unique state of $A$ that correctly predicts the statistics of every observable $\hat A\otimes\hat I_B$. The partial trace is not a measurement; it is a mathematical operation that discards $B$ by averaging over all its states.

An important result follows: even when $\hat\rho_{AB}$ is pure, the reduced state $\hat\rho_A$ can be mixed — maximally mixed, even. This happens when $A$ and $B$ are entangled. Entanglement is the precise condition under which a pure joint state cannot be described by any pure state of its parts.

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

Qubit $A$ is in the maximally mixed state. Every measurement on $A$ alone, in any basis, gives outcomes with equal probability $1/2$. A perfectly pure joint state has yielded the most mixed possible subsystem. All the information about the correlations between $A$ and $B$ is in the joint state — discarding $B$ discards that information entirely.

For comparison: if the joint state is a product state $|00\rangle\langle00|$, then $\hat\rho_A = |0\rangle\langle0|$, purity $= 1$, and the subsystem is pure. For pure joint states, the subsystem is mixed if and only if the joint state is entangled. This is the precise content of the partial trace.

---

## Interpretation and Open Questions

The density matrix provides a well-defined procedure for handling incomplete information. It does not, however, resolve the deeper question of why information becomes incomplete.

When the joint state of a qubit plus its environment is pure and we trace out the environment, we obtain $\hat\rho$ for the qubit — a mathematically precise and physically useful operation. The qubit is entangled with environmental degrees of freedom such as stray phonons and nuclear spins. The joint system remains pure, and unitary evolution continues. Decoherence explains why the qubit's density matrix becomes diagonal in the pointer basis, so that measurements appear classical. It does not explain why any particular outcome occurs.

Whether the qubit has a definite pure state that the formalism merely fails to track — whether the mixedness is epistemic (a matter of ignorance) or ontic (a matter of fact) — is a question about the interpretation of quantum mechanics. The formalism is settled. The meaning continues to be debated.

---

## References

- Fano, U. (1957). "Description of states in quantum mechanics by density matrix and operator techniques." *Reviews of Modern Physics*, 29(1), 74–93. [verify]
- Nielsen, M.A. and Chuang, I.L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. §2.4 (density operators and reduced density matrices), §2.1.2 (Bloch sphere). [verify]
- Preskill, J. *Lecture Notes for Physics 219/CS 219: Quantum Information and Computation*, Chapter 2. http://www.theory.caltech.edu/~preskill/ph219/ [verify]
- Sakurai, J.J. and Napolitano, J. (2020). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. §3.4 (density matrix and ensembles). [verify]
- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer. Chapter 2. [verify]

