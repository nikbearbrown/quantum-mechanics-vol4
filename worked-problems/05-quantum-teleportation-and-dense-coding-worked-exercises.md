# Worked Exercises: Quantum Teleportation and Dense Coding
*Chapter 5 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can expand a three-qubit state in the computational basis and apply CNOT ($|x\rangle|y\rangle \mapsto |x\rangle|x\oplus y\rangle$) and Hadamard ($H|0\rangle = (|0\rangle+|1\rangle)/\sqrt2$, $H|1\rangle = (|0\rangle-|1\rangle)/\sqrt2$).
- You know the four Bell states and the Pauli matrices $I, X, Z, Y$, and can compute their action on $\alpha|0\rangle + \beta|1\rangle$.
- You can take a partial trace $\text{Tr}_{SA}(\cdot)$ and recognize the maximally mixed state $\hat I/2$ as the signature of no-signaling.

---

## Part A — Full Worked Example: Teleporting $|\psi\rangle = \cos\tfrac\theta2|0\rangle + \sin\tfrac\theta2|1\rangle$ for outcome $|01\rangle$

**What this demonstrates:** That the teleportation correction gate is a deterministic Pauli rotation depending only on Alice's two classical bits — never on the unknown amplitudes — so Bob recovers $|\psi\rangle$ exactly without anyone learning the state.

**The problem:** Alice holds qubit $S$ in $|\psi\rangle_S = \cos\tfrac\theta2|0\rangle + \sin\tfrac\theta2|1\rangle$ (a real Bloch-equator-tilted state, amplitudes unknown to her). She and Bob share $|\Phi^+\rangle_{AB} = \tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)_{AB}$. Run the protocol; suppose Alice measures the outcome $|01\rangle_{SA}$. Find Bob's conditional state, the required correction, and verify the corrected state equals $|\psi\rangle$.

**The solution:**

**Step 1 — Write the three-qubit initial state.** With $\alpha = \cos\tfrac\theta2$, $\beta = \sin\tfrac\theta2$:
$$|\Psi_0\rangle = |\psi\rangle_S \otimes |\Phi^+\rangle_{AB} = \frac{1}{\sqrt2}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle\bigr)_{SAB}.$$
*Why:* The protocol needs Alice's two qubits ($S$, $A$) entangled with Bob's $B$ before she can sort the state by her measurement basis.
*Check:* Norm is $\tfrac12(\alpha^2+\alpha^2+\beta^2+\beta^2) = \alpha^2+\beta^2 = 1$. ✓

**Step 2 — Apply CNOT ($S$ control, $A$ target).** The map $|x\rangle|y\rangle \mapsto |x\rangle|x\oplus y\rangle$ flips $A$ when $S=1$:
$$|\Psi_1\rangle = \frac{1}{\sqrt2}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|110\rangle + \beta|101\rangle\bigr).$$
*Why:* CNOT begins the Bell-basis change on Alice's side; the $\beta$ terms' middle qubit flips from $0\to1$ and $1\to0$.
*Check:* Only the two $\beta$ terms (had $S=1$) changed; the $\alpha$ terms are untouched. ✓

**Step 3 — Apply Hadamard to $S$ and collect by $|m_1 m_2\rangle_{SA}$.** Using $H|0\rangle, H|1\rangle$ and regrouping:
$$|\Psi_2\rangle = \frac{1}{2}\Bigl[|00\rangle_{SA}(\alpha|0\rangle+\beta|1\rangle)_B + |01\rangle_{SA}(\beta|0\rangle+\alpha|1\rangle)_B$$
$$+ |10\rangle_{SA}(\alpha|0\rangle-\beta|1\rangle)_B + |11\rangle_{SA}(-\beta|0\rangle+\alpha|1\rangle)_B\Bigr].$$
*Why:* The Hadamard completes the Bell measurement, sorting the state into four branches each tagged by a distinct two-bit Alice outcome.
*Check:* Each of the four conditional Bob states is a Pauli image of $|\psi\rangle$: $I|\psi\rangle$, $X|\psi\rangle$, $Z|\psi\rangle$, $ZX|\psi\rangle$. ✓

**Step 4 — Select the $|01\rangle$ branch and identify the correction.** Alice's outcome $|01\rangle_{SA}$ leaves Bob in $\beta|0\rangle + \alpha|1\rangle = X|\psi\rangle$. The table prescribes correction $X$.
*Why:* The branch's Bob state is $|\psi\rangle$ with $|0\rangle\leftrightarrow|1\rangle$ swapped — exactly the action of $X$, so applying $X$ again undoes it ($X^2 = I$).
*Check:* The correction is read off the outcome bits $01$, with no reference to $\alpha$ or $\beta$. ✓

**Step 5 — Apply the correction gate and verify.**
$$X(\beta|0\rangle + \alpha|1\rangle) = \beta|1\rangle + \alpha|0\rangle = \alpha|0\rangle + \beta|1\rangle = \cos\tfrac\theta2|0\rangle + \sin\tfrac\theta2|1\rangle = |\psi\rangle.$$
*Why:* $X$ swaps the basis labels, restoring the original amplitude-to-label assignment.
*Check:* Output equals the input $|\psi\rangle$ for every $\theta$. ✓

**Final answer:** For outcome $|01\rangle$, Bob's pre-correction state is $X|\psi\rangle = \sin\tfrac\theta2|0\rangle + \cos\tfrac\theta2|1\rangle$; applying $X$ yields exactly $|\psi\rangle = \cos\tfrac\theta2|0\rangle + \sin\tfrac\theta2|1\rangle$.

**What made this work:** The protocol's power is that $|\Psi_2\rangle$ factors into four orthogonal Alice-outcome branches, each carrying a *known* Pauli image of the *unknown* state. Alice's measurement randomly picks a branch and destroys $|\psi\rangle$ on $S$ (preserving no-cloning), but because the four corrections $\{I, X, Z, ZX\}$ are fixed in advance and indexed only by classical bits, Bob can always invert his branch's Pauli without ever knowing $\alpha$ or $\beta$. The unknown amplitudes ride through the algebra untouched.

**Self-explanation prompt:** Why does the correction depend only on Alice's two measured bits and never on $\theta$ — and what would go wrong if Bob tried to guess the correction without waiting for the call?

---

## Part B — Matched Practice Problem

**The problem:** Alice teleports $|\psi\rangle_S = \tfrac{1}{\sqrt2}|0\rangle + \tfrac{i}{\sqrt2}|1\rangle = |{+i}\rangle$ (so $\alpha = 1/\sqrt2$, $\beta = i/\sqrt2$) using a shared $|\Phi^+\rangle_{AB}$. Suppose Alice measures the outcome $|11\rangle_{SA}$. Find Bob's conditional state before correction, identify the correction gate, apply it, and verify Bob recovers $|{+i}\rangle$.

Work it with the same five-step structure:

**Step 1 — Write the three-qubit initial state** ($|\Psi_0\rangle$ with these $\alpha, \beta$).

**Step 2 — Apply CNOT ($S$ control, $A$ target).**

**Step 3 — Apply Hadamard to $S$ and collect by $|m_1 m_2\rangle_{SA}$.**

**Step 4 — Select the $|11\rangle$ branch and identify the correction.**

**Step 5 — Apply the correction gate and verify.**

**Stuck?** For the $|11\rangle$ branch, Bob's conditional state is $-\beta|0\rangle + \alpha|1\rangle$ and the correction is $ZX$ (apply $X$ first, then $Z$). Track the complex $\beta = i/\sqrt2$ carefully through the sign and the $Z$ phase.

*(Instructor note: full solution intentionally omitted — students complete all five steps and the verification.)*

---

## Part C — Completion Problem

**The problem:** Alice teleports $|\psi\rangle_S = \sqrt{0.8}\,|0\rangle + \sqrt{0.2}\,|1\rangle$ (so $\alpha = \sqrt{0.8}$, $\beta = \sqrt{0.2}$) sharing $|\Phi^+\rangle_{AB}$. Alice measures outcome $|10\rangle_{SA}$. Steps 1, 2, and 5 plus the final answer are provided; fill in Steps 3 and 4.

**Step 1 — Write the three-qubit initial state.**
$$|\Psi_0\rangle = \frac{1}{\sqrt2}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle\bigr), \quad \alpha = \sqrt{0.8},\ \beta = \sqrt{0.2}.$$

**Step 2 — Apply CNOT ($S$ control, $A$ target).**
$$|\Psi_1\rangle = \frac{1}{\sqrt2}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|110\rangle + \beta|101\rangle\bigr).$$

**Step 3 — Apply Hadamard to $S$ and collect by $|m_1 m_2\rangle_{SA}$; read off the $|10\rangle_{SA}$ branch.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Identify the correction gate for outcome $|10\rangle$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Apply the correction gate and verify.**
$$Z(\alpha|0\rangle - \beta|1\rangle) = \alpha|0\rangle + \beta|1\rangle = \sqrt{0.8}\,|0\rangle + \sqrt{0.2}\,|1\rangle = |\psi\rangle. \checkmark$$

**Final answer:** For outcome $|10\rangle$, Bob's pre-correction state is $Z|\psi\rangle = \alpha|0\rangle - \beta|1\rangle$; the correction $Z$ flips the sign on $|1\rangle$, returning $|\psi\rangle$ exactly.

**Self-explanation prompt:** Outcome $|10\rangle$ produced a relative *sign* error, not a label swap. Explain why the Hadamard (Step 3) is what converts the $S=1$ branches into the minus-sign structure that $Z$ corrects.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student teleports $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ and writes the following. One step contains a real misconception.

**Step 1.** Initial state $|\Psi_0\rangle = |\psi\rangle_S \otimes |\Phi^+\rangle_{AB}$. ✓

**Step 2.** After CNOT and Hadamard, the state sorts into four branches with Bob's conditional states $\{|\psi\rangle, X|\psi\rangle, Z|\psi\rangle, ZX|\psi\rangle\}$. ✓

**Step 3.** ⚠ "The instant Alice measures her two qubits and gets, say, $|10\rangle$, Bob's qubit *becomes* $Z|\psi\rangle$ at that moment. So Bob already has (a Pauli image of) the state the moment Alice measures — the classical phone call is just a convenience telling him which gate to use. In principle, if Bob measured his qubit immediately in many copies of the experiment, he could detect that Alice had measured and even infer her basis, which means a tiny bit of information crosses instantly, faster than the phone call."

**Step 4.** Bob applies $Z$ and recovers $|\psi\rangle$. ✓

**Step 5.** State teleported. ✓

**Your tasks:**
1. Identify precisely which claim in Step 3 is wrong.
2. Compute Bob's reduced density matrix $\hat\rho_B = \text{Tr}_{SA}(|\Psi_2\rangle\langle\Psi_2|)$ before the classical bits arrive, and use the result to refute the "information crosses instantly" claim.
3. Explain why averaging Bob's conditional states $\{|\psi\rangle, X|\psi\rangle, Z|\psi\rangle, ZX|\psi\rangle\}$ over the four equiprobable outcomes gives $\hat I/2$ regardless of $\alpha, \beta$ — connecting to the fact that $\{I, X, Z, XZ\}$ form a 1-design on the Bloch sphere.
4. State the correct relationship between the classical phone call, no-cloning, and no-signaling: the two classical bits are not a convenience, they *are* the protocol.

**Why this error is common:** The "collapse updates Bob's qubit instantly" picture is real for the joint state, but students mistake a *conditional* state (which requires knowing Alice's outcome) for *locally accessible* information, forgetting that Bob's marginal is $\hat I/2$ until two cbits arrive.

---

## Part E — Transfer Problem

**The problem:** Now run the *dual* protocol, superdense coding, on a new task. Alice and Bob share $|\Phi^+\rangle_{AB}$. Alice wants to send the two-bit message "01." (a) Which single-qubit Pauli does Alice apply to her qubit $A$, and what Bell state does the shared pair become? (b) Alice sends qubit $A$ to Bob; Bob applies CNOT ($A$ control, $B$ target) then $H$ on $A$, then measures both in the computational basis. Write the state after each operation. (c) What two bits does Bob read, and does it match Alice's message? (d) State the resource accounting (ebits, cbits, qubit channel) and contrast it with teleportation's accounting.

**Hint (use only if stuck after 10 minutes):** Message "01" maps to gate $X$, producing $|\Psi^+\rangle = (|01\rangle+|10\rangle)/\sqrt2$. Bob's decoding is exactly the *inverse* of Bell-state preparation, so $|\Psi^+\rangle \to |01\rangle$; the CNOT acts first, then $H$ on the control qubit $A$.

**Reflection prompt:** (1) Teleportation spends 1 ebit + 2 cbits to move 1 qubit; dense coding spends 1 ebit + 1 qubit channel to move 2 cbits. In what sense is the entanglement resource "the same resource used in opposite directions"? (2) Without the shared Bell pair, Holevo's theorem caps a single qubit at one classical bit. Why does pre-shared entanglement double that capacity without creating information from nothing?

---

## Part F — Interleaved Review

**F1 — This chapter.** Apply the no-cloning argument to $|\psi\rangle = |{+}\rangle = (|0\rangle+|1\rangle)/\sqrt2$ and $|\phi\rangle = |0\rangle$. Compute $\langle\phi|\psi\rangle$ explicitly, show it equals neither $0$ nor $1$, and state in one sentence which step of $\langle\psi|\phi\rangle = \langle\psi|\phi\rangle^2$ fails for this pair — and why that forbids a universal cloner.
*Chapter this draws from: 5*

**F2 — Previous chapter.** A Bell pair achieving CHSH parameter $S = 2\sqrt2$ teleports with fidelity $F_\text{tel} = 1$, while a pair degraded to the CHSH classical bound $S = 2$ gives $F_\text{tel} = (1 + 1/\sqrt2)/2 \approx 0.854$. Using $F_\text{tel} = (1 + S/2\sqrt2)/2$, find the $S$ at which teleportation just fails to beat the classical threshold $F = 2/3$, and explain why this $S$ lies *below* the CHSH bound of 2.
*Chapter this draws from: Bell Inequalities and the CHSH Game (Chapter 4)*

**F3 — Discrimination.** You are handed two tasks. Task 1: "Move an unknown qubit state from Alice to Bob using a shared Bell pair and a classical channel." Task 2: "Send two classical bits using a shared Bell pair and a single qubit channel." For each, name the protocol, state which resource is consumed and in which direction, and identify the decoding measurement Bob performs.
*Note to instructor: students must distinguish teleportation (consumes cbits, outputs a qubit) from dense coding (consumes a qubit channel, outputs cbits) and not conflate the Bell measurement's role — it is Alice's measurement in teleportation but Bob's decoding in dense coding.*

**Closing reflection:** Across all six parts, what single structural fact about $|\Psi_2\rangle$ — the way it factors into four Pauli-tagged branches — simultaneously enforces no-cloning, makes the classical channel indispensable, and guarantees no-signaling?

---

## Instructor Notes

**Common errors:**
1. Believing the un-measured branches need no correction, or that outcome $|00\rangle$ ("apply $I$") means "teleportation already worked, no protocol needed" — the $I$ branch is one of four equiprobable cases, not the default.
2. Reproducing the textbook-myth threshold: claiming teleportation fidelity from $S = 2$ is $3/4$, or that any CHSH-local state ($S \le 2$) gives no quantum advantage. The correct values are $F_\text{tel}(2) \approx 0.85$ and the classical-threshold crossing at $S = 2\sqrt2/3 \approx 0.94$, *below* the CHSH bound.
3. Thinking the original $|\psi\rangle$ survives on $S$ after Alice's measurement — it collapses to a computational basis state; the state is destroyed, which is exactly what no-cloning requires.

**Signs a student needs to return:**
- They claim Bob can extract any information about $\alpha, \beta$ before the classical bits arrive (the $\hat\rho_B = \hat I/2$ result is not internalized).
- They cannot say *why* the correction depends only on the two measured bits and not on the unknown amplitudes.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify just outcome $|00\rangle$ (correction $I$, trivial) before tackling the sign- and swap-bearing branches. If a student finishes Part F quickly, have them prove no-cloning $\Rightarrow$ no-signaling: assume Bob could clone his received qubit, show he could then distinguish Alice's measurement basis without the call, and derive the contradiction.

**Domain adaptation note:** In a lab course, anchor Part E to a real superdense-coding demonstration (e.g. photonic or superconducting), having students map the chapter's $\{I, X, Z, iY\}$ encoding table onto the gates the hardware actually applies.
