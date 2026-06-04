# Chapter 5 — Quantum Teleportation and Dense Coding

**TL;DR**

- Quantum information cannot be copied (no-cloning), but it can be moved — at the cost of one Bell pair and two classical bits.
- Quantum teleportation sends an unknown qubit state from Alice to Bob using a pre-shared entangled pair plus a classical phone call; the original is destroyed in the process.
- Superdense coding is the exact dual: two classical bits encoded into one qubit, decoded by Bob using that same shared Bell pair.
- Neither protocol violates no-cloning or sends information faster than light. The classical channel is not a formality — without it, Bob has nothing.

---

**Learning objectives**

By the end of this chapter you should be able to:

1. **State** the no-cloning theorem and reproduce its proof from the inner-product argument. *(Remember/Understand)*
2. **Trace** the three-qubit teleportation protocol through all four of Alice's measurement outcomes, identifying Bob's corrective gate in each case. *(Apply)*
3. **Explain** why teleportation does not violate no-cloning and does not transmit information faster than light, citing the role of the classical channel. *(Analyze)*
4. **Encode and decode** a two-bit message using the superdense-coding protocol, identifying which Pauli Alice applies and which Bell state results. *(Apply)*
5. **Articulate** the duality between teleportation and dense coding in terms of the same entanglement resource used in opposite directions. *(Evaluate)*

---

You cannot photocopy a quantum state. This is not a limitation of present technology — it is structural, a theorem, and the proof fits in three lines of algebra. And yet, the same entanglement that forbids copying turns out to be exactly what you need to move an unknown quantum state from one place to another. The impossibility and the protocol are not in conflict. They are two faces of the same resource.

In 1993, Charles Bennett and five collaborators — Brassard, Crépeau, Jozsa, Peres, and Wootters — published a protocol that achieves this: given one shared Bell pair and a classical phone call, Alice can deliver Bob an exact copy of any qubit state she holds, without Alice learning anything about the state, and without the original surviving in Alice's hands [verify]. They called it teleportation. The name was chosen for its resonance, not for any suggestion of science fiction. The physics is more interesting than fiction: the state crosses no spatial gap. The entanglement was already there. What travels at the speed of light is two bits.

This chapter builds the protocol from scratch, explains both why it works and why it cannot work any faster, and then shows the dual — superdense coding — where the same entanglement resource runs in reverse, squeezing two classical bits into the channel capacity of one qubit.

---

## The no-cloning theorem

Before the protocol, the constraint. If copying were possible, teleportation would be unnecessary and FTL signaling would be easy. So the first question is: why can't we copy?

Suppose a universal quantum cloner exists. That is, suppose there exists a unitary operator $\hat U$ such that, for any normalized qubit state $|\psi\rangle$ and a fixed "blank" state $|s\rangle$:

$$\hat U|\psi\rangle|s\rangle = |\psi\rangle|\psi\rangle.$$

Apply this hypothetical $\hat U$ to two different normalized states $|\psi\rangle$ and $|\phi\rangle$:

$$\hat U|\psi\rangle|s\rangle = |\psi\rangle|\psi\rangle, \qquad \hat U|\phi\rangle|s\rangle = |\phi\rangle|\phi\rangle.$$

Unitaries preserve inner products. Take the inner product of the two input sides and the two output sides separately:

$$\langle\psi|\phi\rangle\langle s|s\rangle = \langle\psi|\phi\rangle \quad \text{(inputs)}, \qquad \langle\psi|\phi\rangle^2 \quad \text{(outputs)}.$$

Since $\langle s|s\rangle = 1$, unitarity demands $\langle\psi|\phi\rangle = \langle\psi|\phi\rangle^2$. A complex number equal to its own square must be either 0 or 1. Therefore $|\psi\rangle$ and $|\phi\rangle$ are either orthogonal ($\langle\psi|\phi\rangle = 0$) or identical ($\langle\psi|\phi\rangle = 1$). Since most pairs of states are neither orthogonal nor identical, no universal cloner exists.

This is the **no-cloning theorem** (Wootters and Zurek, 1982; Dieks, 1982, independently [verify]). The proof used only that $\hat U$ is unitary and linear — that is, it used only the structure of quantum mechanics. No physics, no engineering. Just algebra.

The consequences cascade. Orthogonal states *can* be "cloned" in a limited sense — a CNOT-based fan-out copies $|0\rangle$ and $|1\rangle$ exactly — but an unknown superposition cannot. Quantum key distribution is secure precisely because an eavesdropper who intercepts a qubit cannot make a copy and pass the original along undisturbed. And, as we will see, no-cloning enforces no-FTL-signaling: if Bob could clone his received qubit, he could statistically distinguish Alice's measurement bases without waiting for her phone call, and she could signal faster than light. The impossibility of copying is the impossibility of superluminal communication.

---

## The teleportation protocol

**The setup.** Alice holds qubit $S$ in the unknown state

$$|\psi\rangle_S = \alpha|0\rangle + \beta|1\rangle,$$

where $\alpha$ and $\beta$ are unknown complex amplitudes with $|\alpha|^2 + |\beta|^2 = 1$. She does not know $\alpha$ or $\beta$; she has been handed the qubit by some third party. She wants Bob to end up with a qubit in state $|\psi\rangle$, even though the quantum channel between them is unavailable. What she does have is a classical telephone and a shared Bell pair.

**The resource.** Alice and Bob pre-shared the Bell pair

$$|\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr)_{AB}$$

at some earlier time, perhaps when they were in the same room. Qubit $A$ belongs to Alice; qubit $B$ belongs to Bob. The three-qubit system is now:

$$|\Psi_0\rangle = |\psi\rangle_S \otimes |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle\bigr)_{SAB}.$$

Alice holds $S$ and $A$. Bob holds $B$.

**Step 1: Alice applies CNOT ($S$ control, $A$ target).** The CNOT maps $|x\rangle|y\rangle \mapsto |x\rangle|x \oplus y\rangle$:

$$|\Psi_1\rangle = \frac{1}{\sqrt{2}}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|110\rangle + \beta|101\rangle\bigr).$$

**Step 2: Alice applies Hadamard to $S$.** Using $H|0\rangle = (|0\rangle+|1\rangle)/\sqrt{2}$ and $H|1\rangle = (|0\rangle-|1\rangle)/\sqrt{2}$:

$$|\Psi_2\rangle = \frac{1}{2}\Bigl[|00\rangle_{SA}(\alpha|0\rangle+\beta|1\rangle)_B + |01\rangle_{SA}(\beta|0\rangle+\alpha|1\rangle)_B$$
$$+ |10\rangle_{SA}(\alpha|0\rangle-\beta|1\rangle)_B + |11\rangle_{SA}(-\beta|0\rangle+\alpha|1\rangle)_B\Bigr].$$

This is the key step. Rewriting in the computational basis of Alice's two qubits has sorted Bob's qubit into four conditional states. Each is a simple transformation of $|\psi\rangle$:

| Alice's outcome | Probability | Bob's qubit | Required correction |
|:---:|:---:|:---:|:---:|
| $|00\rangle$ | $1/4$ | $\alpha|0\rangle+\beta|1\rangle = |\psi\rangle$ | $I$ |
| $|01\rangle$ | $1/4$ | $\beta|0\rangle+\alpha|1\rangle = X|\psi\rangle$ | $X$ |
| $|10\rangle$ | $1/4$ | $\alpha|0\rangle-\beta|1\rangle = Z|\psi\rangle$ | $Z$ |
| $|11\rangle$ | $1/4$ | $-\beta|0\rangle+\alpha|1\rangle = XZ|\psi\rangle$ | $ZX$ |

**Step 3: Alice measures.** She measures her two qubits $SA$ in the computational basis, obtaining one of four outcomes with equal probability $1/4$. The measurement destroys the superposition on her side. Qubit $S$ is now in a definite computational basis state — *not* in state $|\psi\rangle$. The state information has left $S$.

**Step 4: Alice calls Bob.** She sends her two-bit outcome $(m_1, m_2)$ over the classical channel.

**Step 5: Bob applies the correction.** Using the lookup table above, Bob applies one of $\{I, X, Z, ZX\}$ to his qubit $B$. In every case, his qubit becomes exactly $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$.

The state has been teleported. Alice no longer has it. Bob now does. No copy was ever made. The original was consumed in the measurement.

---

### Why this does not violate no-cloning

After Alice's measurement, qubit $S$ is in a definite basis state — $|0\rangle$ or $|1\rangle$ — not in $|\psi\rangle$. The state information has been transferred to Bob; Alice never retained it. There is one copy of $|\psi\rangle$ at the end, as required by no-cloning. The protocol is not a workaround for the theorem — it is exactly consistent with it. In fact, no-cloning *guarantees* that Alice's qubit must be destroyed: if the protocol left Alice with $|\psi\rangle$ intact while Bob also received $|\psi\rangle$, that would be a violation.

### Why this does not send information faster than light

Before Alice's phone call arrives, Bob's qubit is useless. His reduced density matrix, tracing over Alice's qubits, is

$$\hat\rho_B = \frac{1}{4}\bigl(|\psi\rangle\langle\psi| + X|\psi\rangle\langle\psi|X + Z|\psi\rangle\langle\psi|Z + XZ|\psi\rangle\langle\psi|ZX\bigr) = \frac{\hat I}{2}.$$

The maximally mixed state. Whatever Alice measured, whatever $\alpha$ and $\beta$ are, Bob sees the same thing: the most ignorant possible single-qubit state. There is no information in his qubit until the two classical bits arrive. Those bits travel at the speed of light. Teleportation is as fast as a phone call, not faster.

The two classical bits are not a formality. They are the protocol. Without them, the resource is consumed and Bob has nothing.

---

## Superdense coding: the dual protocol

Teleportation sends one qubit (two complex amplitudes, effectively two real parameters after normalization and global phase) using one Bell pair and two classical bits. Superdense coding is the exact reverse: send two classical bits using one qubit, given the same Bell pair.

**The setup.** Alice and Bob share $|\Phi^+\rangle_{AB}$ as before. Alice wants to send one of four two-bit messages: $\{00, 01, 10, 11\}$.

**The encoding.** Alice applies a Pauli gate to her qubit $A$ only:

| Message | Alice applies | Bell state produced |
|:---:|:---:|:---:|
| $00$ | $I$ | $|\Phi^+\rangle = (|00\rangle+|11\rangle)/\sqrt{2}$ |
| $01$ | $X$ | $|\Psi^+\rangle = (|01\rangle+|10\rangle)/\sqrt{2}$ |
| $10$ | $Z$ | $|\Phi^-\rangle = (|00\rangle-|11\rangle)/\sqrt{2}$ |
| $11$ | $iY$ (or $XZ$) | $|\Psi^-\rangle = (|01\rangle-|10\rangle)/\sqrt{2}$ |

Each Pauli rotation on Alice's qubit steers the shared pair into a different Bell state. The four Bell states are orthogonal, which means they are perfectly distinguishable by a Bell measurement.

**The transmission.** Alice sends her qubit $A$ to Bob over the quantum channel.

**The decoding.** Bob now holds both qubits. He applies CNOT (A control, B target), then H to qubit $A$, then measures both qubits in the computational basis. The Bell measurement is the reverse of Bell-state preparation:

$$|\Phi^+\rangle \to |00\rangle, \quad |\Psi^+\rangle \to |01\rangle, \quad |\Phi^-\rangle \to |10\rangle, \quad |\Psi^-\rangle \to |11\rangle.$$

Bob reads off Alice's two-bit message with certainty.

**The duality.** Teleportation: 1 ebit + 2 classical bits $\to$ transmit 1 qubit. Dense coding: 1 ebit + 1 qubit channel $\to$ transmit 2 classical bits. The entanglement resource is identical. The direction of the resource expenditure is reversed.

Without the pre-shared entanglement, transmitting 1 qubit can carry at most 1 classical bit (Holevo's theorem). Entanglement doubles the classical channel capacity. It does not create something from nothing — the Bell pair is the resource being spent.

---

## Worked example: tracing teleportation for all four outcomes

**The state:** $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, shared pair $|\Phi^+\rangle_{AB}$.

After Alice's CNOT and Hadamard, the state is:

$$|\Psi_2\rangle = \frac{1}{2}\bigl[|00\rangle(\alpha|0\rangle+\beta|1\rangle) + |01\rangle(\beta|0\rangle+\alpha|1\rangle) + |10\rangle(\alpha|0\rangle-\beta|1\rangle) + |11\rangle(-\beta|0\rangle+\alpha|1\rangle)\bigr].$$

**Outcome $|00\rangle$.** Bob's qubit collapses to $\alpha|0\rangle+\beta|1\rangle$. Bob applies $I$. Result: $\alpha|0\rangle+\beta|1\rangle = |\psi\rangle$. $\checkmark$

**Outcome $|01\rangle$.** Bob's qubit is $\beta|0\rangle+\alpha|1\rangle = X|\psi\rangle$. Bob applies $X$: $X(\beta|0\rangle+\alpha|1\rangle) = \beta|1\rangle+\alpha|0\rangle = \alpha|0\rangle+\beta|1\rangle$. $\checkmark$

**Outcome $|10\rangle$.** Bob's qubit is $\alpha|0\rangle-\beta|1\rangle = Z|\psi\rangle$. Bob applies $Z$: $Z(\alpha|0\rangle-\beta|1\rangle) = \alpha|0\rangle+\beta|1\rangle$. $\checkmark$

**Outcome $|11\rangle$.** Bob's qubit is $-\beta|0\rangle+\alpha|1\rangle$. Bob applies $ZX$: first $X$: $-\beta|1\rangle+\alpha|0\rangle = \alpha|0\rangle-\beta|1\rangle$; then $Z$: $\alpha|0\rangle+\beta|1\rangle$. $\checkmark$

**The lesson.** In every case, Bob recovers $|\psi\rangle$ exactly. The correction is deterministic — it depends only on Alice's two-bit classical outcome, not on $\alpha$ or $\beta$. Neither Alice nor Bob ever learns the values of $\alpha$ and $\beta$. The state information is transferred intact without ever being read.

**The limit.** The protocol assumes a perfect Bell pair. Real experiments use Bell pairs with fidelity $F < 1$ due to decoherence (T₂ limited). If the pair degrades before Alice completes her measurement, Bob receives a mixed state with teleportation fidelity $F_\text{tel} < 1$. The connection to the CHSH parameter is direct: a Bell pair with $S = 2\sqrt{2}$ gives perfect teleportation fidelity; one degraded to $S \leq 2$ gives fidelity no better than the best classical protocol ($F = 2/3$). Running the Chapter 4 CHSH test on your hardware tells you how good your teleportation resource is.

---

## Common misconceptions

**"Teleportation sends the quantum state faster than light."** It does not. The entanglement collapses instantaneously in the sense that Bob's qubit is immediately in one of the four conditional states. But Bob cannot distinguish this from random noise until he receives Alice's two classical bits. Those bits travel at $\leq c$. The full protocol is causal.

**"Teleportation makes a copy; Alice sends hers and keeps a duplicate."** No. Alice's qubit $S$ is measured in Step 3. After measurement, $S$ is in a definite computational basis state — it has been destroyed as a carrier of the original state. At the end of the protocol, there is exactly one copy of $|\psi\rangle$, now on Bob's qubit. No-cloning is satisfied by construction.

**"The four corrections are just relabeling; the state is really transmitted in Step 3."** No. Before the classical bits arrive, Bob's state is $\hat\rho_B = \hat I/2$. The classical bits are what transform that maximally mixed state into $|\psi\rangle$. They are not a bookkeeping artifact.

**"Superdense coding violates the Holevo bound."** The Holevo bound says 1 qubit carries at most 1 classical bit *without pre-shared entanglement*. Dense coding uses a pre-shared Bell pair. The entanglement-assisted Holevo bound is 2 classical bits per qubit, which dense coding saturates. No violation.

**"The outcome 11 correction is $X$ then $Z$, or is it $Z$ then $X$?"** The two orderings differ by a global phase ($ZX = -iY$, $XZ = iY$). Because global phases are unobservable, both give the same final state $|\psi\rangle$. Pick either convention and be consistent.

---

## Exercises

### Warm-up

**5.1** *[Tests: no-cloning proof; inner product computation]* Apply the no-cloning argument to $|\psi\rangle = |+\rangle = (|0\rangle+|1\rangle)/\sqrt{2}$ and $|\phi\rangle = |0\rangle$. Compute $\langle\phi|\psi\rangle$ explicitly and verify that it equals neither $0$ nor $1$, confirming that a universal cloner cannot copy these two states simultaneously. *(Difficulty: warm-up.)*

**5.2** *[Tests: Bell-state structure; superdense encoding table]* Starting from $|\Phi^+\rangle = (|00\rangle+|11\rangle)/\sqrt{2}$, apply $Z$ to Alice's qubit (qubit $A$) and show step by step that the result is $|\Phi^-\rangle = (|00\rangle-|11\rangle)/\sqrt{2}$. Explain in one sentence why this corresponds to Alice encoding the message "10." *(Difficulty: warm-up.)*

**5.3** *[Tests: reduced density matrix; no-signaling theorem]* Compute Bob's reduced density matrix $\hat\rho_B = \text{Tr}_{SA}(|\Psi_2\rangle\langle\Psi_2|)$ for the state after Alice's CNOT and Hadamard, before Alice measures. Show that $\hat\rho_B = \hat I/2$, confirming that Bob's local statistics contain no information about $\alpha$ and $\beta$ before the classical communication. *(Difficulty: warm-up.)*

### Apply

**5.4** *[Tests: teleportation trace; specific state]* Trace the teleportation protocol for the specific state $|\psi\rangle = |+\rangle = (|0\rangle+|1\rangle)/\sqrt{2}$. For each of the four measurement outcomes, write out Bob's conditional state after Alice's measurement, apply the correction, and verify you recover $|+\rangle$. *(Difficulty: apply.)*

**5.5** *[Tests: superdense coding decode; Bell measurement]* Alice sends the message "11" using dense coding. She applies $iY$ to her qubit of $|\Phi^+\rangle_{AB}$. (a) Write out the resulting two-qubit state. (b) Bob applies CNOT (A control, B target) then H to A. Write the state after each operation. (c) Bob measures; what outcome does he get? Verify this matches Alice's message. *(Difficulty: apply.)*

**5.6** *[Tests: teleportation resource accounting]* The teleportation protocol consumes one Bell pair and two classical bits to transmit one qubit state. (a) Explain why Alice cannot reuse the same Bell pair to teleport a second qubit without distributing a fresh entangled pair. (b) If Alice and Bob share two Bell pairs and Alice wants to teleport two independent qubits simultaneously, how many classical bits does she need to send? (c) What happens if Alice attempts the protocol but the shared Bell pair has been replaced by the product state $|00\rangle_{AB}$ (no entanglement)? What does Bob receive? *(Difficulty: apply.)*

### Produce

**5.7** *[Tests: protocol design; dense-to-teleportation duality]* You are given one pre-shared Bell pair, a quantum channel (one qubit), and a classical channel (unlimited bits). Your task is to transmit an unknown qubit state $|\psi\rangle$ from Alice to Bob. Write the teleportation protocol from scratch — circuit diagram (as a labeled sequence of gates and measurements), the four-outcome correction table, and a one-paragraph argument for why the classical channel cannot be eliminated. Your protocol must handle all four outcomes correctly. *(Difficulty: produce.)*

---

## Still puzzling

The teleportation protocol consumes exactly one Bell pair and two classical bits to transmit one qubit. Is this optimal? The Holevo bound and the entanglement-assisted capacity theorem say yes: you cannot do better. One ebit plus two classical bits is the tight resource count, and neither resource can substitute for the other.

But there is a deeper oddity. The two classical bits that Alice sends encode no information about $\alpha$ or $\beta$ — each outcome has probability exactly $1/4$, regardless of the state. They are a uniformly random two-bit string. And yet Bob cannot reconstruct the state without them. The information in the bits is not *about* the state; it is the *key* that unlocks the state from the entanglement. That is a strange kind of information: it carries no content yet is indispensable.

This connects to a wider question about what quantum information fundamentally is. Classical information is copyable, compressible, and conveyable. Quantum information is none of these things in the same way. The teleportation protocol makes the difference visceral: you can move quantum information only by destroying it at the source and reconstituting it at the destination, with entanglement as the carrier medium and classical bits as the ignition key. What exactly crosses the gap? That question does not have a clean answer — and the sharpness of the unease is itself a sign that you have understood the protocol.

---

## The +1 — Simulation exercise

Build a live teleportation visualizer. The goal: watch the Bloch vector on Bob's qubit change from a random sphere-center (before Alice's classical bits) to the correct target state (after) — and see all four outcome branches in parallel.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 5 — Quantum Teleportation and Dense Coding
Deliverable: 05-teleportation.html
Status: in progress

The simulation has three panels:

Panel A — Protocol walkthrough (top, 700 x 300 SVG).
Animated circuit diagram with three horizontal wires (qubits S, A, B).
Gates appear in sequence: CNOT (S→A), H (on S), measurement boxes
on S and A, classical-bit wires (dashed) to Bob, correction gate on B.
A "step" button advances through the protocol one operation at a time.
Current qubit states shown as small Bloch sphere icons along each wire.

Panel B — Four outcome branches (middle, 700 x 350 SVG).
A 2x2 grid of four Bloch spheres, one per measurement outcome (00, 01, 10, 11).
Each sphere shows Bob's conditional state before the correction is applied.
When Alice's outcome is "measured" (random sample), the corresponding sphere
is highlighted and the correction gate label appears.
After correction, all four spheres converge to the same Bloch vector.

Panel C — Dense coding encoder (bottom, 700 x 250 SVG).
Four buttons labeled 00, 01, 10, 11. Clicking one shows:
- Which Pauli Alice applies.
- The resulting joint two-qubit state vector (amplitudes shown as bars).
- The Bell state label (Phi+, Psi+, Phi-, Psi-).
- Bob's Bell measurement outcome after he applies CNOT then H.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md the following physics rules for Chapter 5 simulations:

TELEPORTATION AND DENSE CODING PHYSICS RULES

1. The teleportation protocol operates on a 3-qubit register [S, A, B]
   (8-dimensional complex vector). Index ordering: qubit S = most significant
   bit. State vector entry [i] corresponds to binary(i) = (s, a, b).

2. The initial state is:
     |psi>_S ⊗ |Phi+>_{AB}
   where |psi> = [alpha, beta] and |Phi+> = [1/sqrt(2), 0, 0, 1/sqrt(2)].
   Full 8-vector: alpha * [1,0,0,0,0,1,0,0]/sqrt(2) as complex array,
   then add beta * [0,0,0,0,1,0,0,1]/sqrt(2). Wait — derive by direct
   Kronecker product. Do NOT hardcode; implement kron(A, B) explicitly.

3. Gates applied to specific qubits in an n-qubit register:
   gate_on_qubit(U, k, n): builds the 2^n x 2^n unitary by taking the
   Kronecker product I ⊗ ... ⊗ U (at position k) ⊗ ... ⊗ I.
   Implement Kronecker product in vanilla JS.

4. CNOT with control c and target t: in the [S,A,B] register,
   CNOT(S->A) maps |x,y,z> -> |x, x XOR y, z>. Build the 8x8 matrix
   explicitly by checking each basis vector.

5. After Alice's CNOT and H steps, measure qubits S and A in the
   computational basis. Sample the outcome with correct probabilities
   (each 1/4). Display the outcome. Bob's qubit is now a specific
   pure state.

6. The correction gates:
   outcome 00 -> I on qubit B
   outcome 01 -> X on qubit B
   outcome 10 -> Z on qubit B
   outcome 11 -> ZX on qubit B  (apply X first, then Z)

7. After correction, compute the fidelity of Bob's qubit with the
   target |psi>: F = |<psi|rho_B|psi>|. For a perfect Bell pair
   and correct correction, F should equal 1.0 within 1e-6.
   Display F prominently.

8. For dense coding: starting from |Phi+>, apply the selected Pauli
   to qubit A (the first qubit in the pair). The resulting state
   should be one of the four Bell states. Verify by comparing the
   state vector to the known Bell-state vectors.

9. For the Bloch sphere display of Bob's qubit:
   Extract the 2-vector for qubit B by partial tracing: after Alice's
   measurement, qubit B is in a pure state and can be represented as a
   point on the Bloch sphere surface. Use the Bloch-vector formula:
   r_x = 2 Re(rho[0,1]), r_y = 2 Im(rho[1,0]), r_z = rho[0,0] - rho[1,1].

KNOWN FAILURE MODES:
(a) Index ordering: qubit 0 (S) vs qubit 2 (B) — misidentifying which
    dimension of the tensor product belongs to which qubit. Verify by
    checking that initial |Phi+>_AB has the correct 8-vector.
(b) Measurement collapse not traced correctly: after measuring (s,a),
    the remaining state for qubit B is the amplitude vector at those
    indices, normalized. Do not apply the correction before extracting
    this post-measurement state.
(c) For the "four branches" panel: compute all four conditional Bob
    states simultaneously from the pre-measurement state vector,
    without sampling. Sampling is only for the "animated" protocol walk.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 05-teleportation.html: a single self-contained HTML file using
D3 v7 from a CDN, no other dependencies, implementing the Chapter 5
simulation as specified in PROJECT.md, following the physics rules in
CLAUDE.md and the visual constitution in DESIGN.md.

The page has a header and three vertically stacked panels separated by
thin horizontal rules.

PANEL A — Protocol walkthrough (700 x 300 SVG).

Three horizontal wires labeled S (Alice), A (Alice), B (Bob).
A small Bloch-sphere icon on each wire shows the current qubit state
(computed from the density matrix at each step).

Gates (as rectangle labels) appear at the correct wire positions:
  - CNOT: vertical line connecting S and A with control dot and open circle.
  - H: box on S wire.
  - Measurement boxes on S and A (meter icon).
  - Dashed vertical "classical bit" lines from S and A measurements down
    to a "PHONE" icon.
  - Correction gate on B (label switches between I, X, Z, ZX based on outcome).

Controls: a "Next step" button advances through 5 steps:
  0 — initial state
  1 — after CNOT
  2 — after H
  3 — after measurement (sample outcome, highlight corresponding row in
      the correction table)
  4 — after correction (show fidelity F)

A "Reset" button resets to step 0 with a new random |psi> (theta, phi sliders).

Sliders at top: theta (0 to pi) and phi (0 to 2 pi) parameterizing
alpha = cos(theta/2), beta = exp(i phi) sin(theta/2). The initial Bloch
vector on qubit S should reflect the chosen state.

PANEL B — Four outcome branches (700 x 350 SVG).

A 2x2 grid of four Bloch spheres labeled |00>, |01>, |10>, |11>.
Each sphere shows Bob's conditional state AFTER Alice's CNOT+H but BEFORE
any correction. Compute all four states from the pre-measurement 8-vector
without sampling.

When the user reaches step 3 in Panel A (measurement), the sampled outcome
sphere is highlighted (border color changes to amber). A correction-gate
label appears next to each sphere.

When the user reaches step 4 (correction), all four corrected states
converge visually to the same Bloch vector (the target |psi>).

PANEL C — Dense coding encoder (700 x 250 SVG).

Four buttons: [00] [01] [10] [11]. Click one to:
  1. Show which Pauli Alice applies (I, X, Z, iY).
  2. Display the resulting 4-vector as two amplitude bars (|c_0|, |c_1|
     for each qubit) — or better, show the joint Bell-state as four
     amplitude bars for |00>, |01>, |10>, |11>.
  3. Label the Bell state: Phi+, Psi+, Phi-, Psi-.
  4. Animate Bob's Bell measurement: CNOT then H, then show the
     measurement outcome (matching the button label).

Runtime sanity checks (write to console):
- At step 0: |alpha|^2 + |beta|^2 = 1 within 1e-6.
- At step 4: fidelity F = 1.0 within 1e-4 for all four outcomes.
- Dense coding: for each of the four buttons, the Bell measurement
  outcome should exactly match the button label.
- Panel B: all four conditional Bloch vectors should lie on the
  Bloch sphere surface (|r| = 1 within 1e-4) since they are pure states.

Do NOT use any 3D library. Bloch spheres are 2D orthographic projections.
Do NOT use math.js. Comments at every non-trivial physics step.
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. In Panel A, set $|\psi\rangle = |+\rangle$ ($\theta = \pi/2$, $\phi = 0$). Step through the protocol. Identify Alice's measurement outcome. Confirm that Bob's qubit after correction has Bloch vector pointing along $+\hat{x}$ (equator). Verify fidelity $F = 1$.

2. In Panel B, with $|\psi\rangle = |0\rangle$ ($\theta = 0$). Before any correction, what are the four conditional Bloch vectors for Bob's qubit? How do they differ from each other? After correction, what do they have in common?

3. Run Panel A ten times with the same $|\psi\rangle$. Record Alice's outcome each time. Are all four outcomes equally frequent? Do you ever see Bob fail to recover $|\psi\rangle$?

4. In Panel C, click all four message buttons in order. Record which Bell state is produced in each case. Confirm the encoding table matches the one in the chapter. Now ask: what would go wrong if Alice's qubit were in a random state instead of being half of a Bell pair — that is, if there were no pre-shared entanglement?

5. **The limit:** Now imagine the Bell pair has decohered. Modify the initial state of qubit pair $AB$ from $|\Phi^+\rangle$ to the mixed state $\hat\rho_{AB} = \frac{1}{2}|00\rangle\langle 00| + \frac{1}{2}|11\rangle\langle 11|$ (a classical mixture). If you could run the teleportation protocol on this mixed resource, what fidelity would you expect? Why is this the best classical protocol fidelity?

---

## References

- Bennett, C. H., Brassard, G., Crépeau, C., Jozsa, R., Peres, A. & Wootters, W. K. (1993). Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. *Physical Review Letters* **70**, 1895. [verify]
- Bennett, C. H. & Wiesner, S. J. (1992). Communication via one- and two-particle operators on Einstein-Podolsky-Rosen states. *Physical Review Letters* **69**, 2881. [verify]
- Wootters, W. K. & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* **299**, 802–803. [verify]
- Dieks, D. (1982). Communication by EPR devices. *Physics Letters A* **92**, 271–272. [verify]
- Bouwmeester, D., Pan, J.-W., Mattle, K., Eibl, M., Weinfurter, H. & Zeilinger, A. (1997). Experimental quantum teleportation. *Nature* **390**, 575–579. [verify]
- Nielsen, M. A. & Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. (Teleportation: §1.3.7; no-cloning: §12.1; dense coding: §2.3.) [verify]
- Holevo, A. S. (1973). Bounds for the quantity of information transmitted by a quantum communication channel. *Problems of Information Transmission* **9**, 177–183. [verify]
