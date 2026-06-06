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

## Running Project — Reconstruct a Real Research Result

Across this volume you build the tools to take one current quantum paper — a loophole-free Bell test, a quantum-error-correction milestone, or an NV-center sensing result — and reconstruct its central quantitative claim from first principles, triage it with a 7-step framework, and assess the honesty layer (what the paper does and does *not* claim). The finished deliverable is a **reconstruction dossier**: your recomputed number next to the paper's reported number, plus a written assessment of how secure the claim is. Chapter 10 is the capstone where the pieces assemble. Pick your paper now and keep it open as you work.

**This chapter adds:** the *mixed-state model of an imperfect experimental state* — the density matrix $\hat\rho = (1-\epsilon)|\Phi^+\rangle\langle\Phi^+| + \epsilon\,\hat I/4$ and the purity/fidelity tools that let you describe a real Bell pair (which is never the textbook pure state) and the reduced state a single detector sees.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Drafting the symbolic algebra for a partial trace or a $\text{Tr}(\hat\rho^2)$ purity calculation — *Why AI works here:* it is mechanical matrix bookkeeping you can check against the analytic result $\text{Tr}(\hat\rho^2) = \tfrac{1}{2}(1+|\vec r|^2)$.
- Scaffolding a small routine that builds $\hat\rho(\epsilon)$ and returns its eigenvalues — *Why AI works here:* generating boilerplate that you immediately validate against known limits ($\epsilon=0$ pure, $\epsilon=1$ maximally mixed).
**The tell:** You are using AI well when you have an independent way to check the output — here, the purity must lie in $[\tfrac14, 1]$ for a two-qubit state and the eigenvalues must be non-negative and sum to 1.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding *what value of $\epsilon$* corresponds to your chosen paper's real state — *Why AI fails here:* this requires reading the paper's reported fidelity or visibility and mapping it onto $\hat\rho(\epsilon)$; an LLM will happily invent a plausible $\epsilon$ with no ground truth.
- Judging whether a "Werner state" mixture is even the right model for the paper's imperfection (it may be biased noise, not isotropic) — *Why AI fails here:* it is a physical-validity call the AI cannot make without the experimental detail it does not have.
**The tell:** If you could not explain why your $\hat\rho$ is the right model without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** This trains checking a density matrix against its validity conditions — unit trace, non-negative eigenvalues, purity in $[\tfrac1d, 1]$ — before you believe any number computed from it.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a worked derivation and a parametrized $\hat\rho(\epsilon)$ for the entangled resource state your paper actually produced, with purity and reduced state computed and checked.
**Tool:** Claude chat — a single self-contained derivation, no persistent project context needed yet.
**The Prompt:**
```
I am reconstructing the core result of a quantum experiment and need to model
its imperfect entangled state. Work in the two-qubit computational basis
{|00>, |01>, |10>, |11>}.

1. Write out the 4x4 density matrix rho(eps) = (1-eps)|Phi+><Phi+| + eps * I4/4,
   where |Phi+> = (|00> + |11>)/sqrt(2), as an explicit matrix with entries in
   terms of eps. Show the |Phi+><Phi+| matrix first, then the sum.
2. Compute Tr(rho), Tr(rho^2) (the purity), and the four eigenvalues of rho(eps),
   all as functions of eps.
3. Compute the reduced density matrix rho_A = Tr_B(rho(eps)) and state what it is
   for every eps.
4. State the value of eps at which rho(eps) stops being entangled (lose entanglement
   when the largest eigenvalue / the structure crosses the separability point), and
   show the reasoning.
Show every matrix step. Do NOT skip to a final formula — I will check each line.
At the end, list the validity conditions a valid two-qubit density matrix must
satisfy and confirm rho(eps) meets them for eps in [0,1].
```
**What this produces:** an explicit $\hat\rho(\epsilon)$, its purity $\text{Tr}(\hat\rho^2) = \tfrac14(1 + 3(1-\epsilon)^2)$, eigenvalues $\{1-\tfrac{3\epsilon}{4},\ \tfrac{\epsilon}{4},\ \tfrac{\epsilon}{4},\ \tfrac{\epsilon}{4}\}$, and $\hat\rho_A = \hat I/2$ for all $\epsilon$ — the building blocks for the imperfect-resource model.
**How to adapt:** *Your system:* swap in your paper's actual Bell state ($|\Psi^-\rangle$ for spin singlets, etc.). *ChatGPT/Gemini:* identical prompt; cross-check the eigenvalue formula across tools. *Claude Project:* drop the result into a project knowledge file as `resource-state.md` for later chapters.
**Builds on:** the chapter's worked partial trace of $|\Phi^+\rangle$ giving $\hat\rho_A = \tfrac12\hat I$.  **Next:** Chapter 2 confirms this state is maximally entangled and pins down which Bell state your paper uses.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a project directory with a `PROJECT.md` naming your chosen paper and a small verified `rho_tools.py` that builds and validates $\hat\rho(\epsilon)$.
**Tool:** Claude Code — file automation across a project directory you will reuse all volume.
**Skill level:** Beginner
**Setup — confirm:**
- [ ] You have chosen ONE paper (Bell test, QEC milestone, or NV sensing) and have a PDF or arXiv link.
- [ ] Claude Code installed and a fresh empty directory `reconstruction-dossier/`.
- [ ] Add to `CLAUDE.md`: "A valid density matrix has unit trace, is Hermitian, and has non-negative eigenvalues. Always assert these in code before using rho."
**The Task:**
```
Create a project directory for a paper-reconstruction dossier.

1. Create PROJECT.md with these fields, filled in for the paper I name here:
   [PASTE: paper title, authors, journal/arXiv ID, the ONE central numerical
   claim you intend to reconstruct, e.g. "S = 2.42 +/- 0.20" or "p_L = 0.143%/cycle"].
2. Create rho_tools.py with a function werner(eps) returning the 4x4 numpy density
   matrix (1-eps)|Phi+><Phi+| + eps*I4/4, and a function validate(rho) that asserts:
   trace is 1 (within 1e-9), rho is Hermitian, all eigenvalues >= -1e-9, purity in
   [0.25, 1]. Add a __main__ block that runs validate(werner(e)) for e in
   [0, 0.25, 0.5, 0.75, 1.0] and prints eps, purity, eigenvalues for each.
3. Run it and paste the output back to me. Do not edit PROJECT.md after I confirm it.

Leave any other files alone. Stop after the script runs cleanly.
```
**Expected output:** `PROJECT.md`, `rho_tools.py`, and a console table of (eps, purity, eigenvalues) with all validations passing.
**What to inspect:** purity falls from $1.0$ at $\epsilon=0$ to $0.25$ at $\epsilon=1$; the reduced state is always $\hat I/2$; eigenvalues never go negative.
**If it goes wrong:** the most common failure is a non-Hermitian `rho` from a transpose-vs-conjugate-transpose slip — if `validate` flags Hermiticity, check that the outer product uses the conjugate transpose, not the plain transpose.
**CLAUDE.md / AGENTS.md note:** keep the standing rule "always `validate(rho)` before computing any observable from it."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the R3 derivation of $\hat\rho(\epsilon)$, its purity, and its eigenvalues.
**Validation type:** Numerical result + reasoning chain.
**Risk level:** Low — the analytic checks are tight and the matrices are small.
**Setup:** use your R3 output (or the R4 `rho_tools.py` console table).
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Mixed States and the Density Matrix
□ Correctness: does Tr(rho(eps)) = 1 for every eps?
□ Completeness: did it report the reduced state rho_A, or only the global rho?
□ Scope: did it stick to the Werner model, or silently switch noise models?
□ Purity check: is Tr(rho^2) = (1 + 3(1-eps)^2)/4, giving 1 at eps=0 and 0.25 at eps=1?
□ Eigenvalue check: are the four eigenvalues {1-3eps/4, eps/4, eps/4, eps/4},
  all in [0,1] and summing to 1?
□ Failure-mode check: any of —
  - fluent but wrong (a clean-looking purity formula that fails the eps=1 limit)
  - sign/factor-of-2 error in the I4/4 weight (a frequent slip)
  - unnormalized state (trace != 1)
  - reduced state quoted as something other than I/2
```
**What to do with findings:** pass → record the validated $\hat\rho(\epsilon)$ in your dossier; one fail → fix the offending line, re-run, note the change; multiple fails → do the four-line matrix algebra by hand, it is short.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI produced the explicit $\hat\rho(\epsilon)$ matrix and its purity/eigenvalue formulas, which I used as a starting derivation.
> *2:* The AI could not determine which $\epsilon$ matches my paper's reported state — that mapping required me to read the paper's fidelity/visibility.
**Physics-judgment connection:** This validation trains the habit of checking every computed density-matrix quantity against its limiting cases (pure at $\epsilon=0$, maximally mixed at $\epsilon=1$) and its validity conditions before trusting it downstream.

---

Chapter 2 covers composite systems and entanglement in detail. Once the joint state of a system plus environment is entangled, the system alone evolves under a quantum channel — a completely positive, trace-preserving map — rather than unitary evolution. The Lindblad master equation is the differential form of this evolution, and it describes why the Bloch vector shrinks inward over time.
