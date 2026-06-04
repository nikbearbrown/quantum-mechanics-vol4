# Chapter 12 — Entanglement and Quantum Information

## TL;DR

- The same state that breaks local realism is the state that powers teleportation.
- The chapter moves through What entanglement is not, Bell's theorem and the CHSH inequality, What the experiments showed, What Bell's theorem does and does not say, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The same state that breaks local realism is the state that powers teleportation.*

Start with a state. Two qubits, entangled in the simplest way:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr).$$

You know from the tensor product that a two-qubit state lives in a four-dimensional Hilbert space — two factors of two. You might think this state factors: maybe there are single-qubit states $|a\rangle$ and $|b\rangle$ such that $|\Phi^+\rangle = |a\rangle \otimes |b\rangle$. Let us find out. Suppose $|a\rangle = \alpha|0\rangle + \beta|1\rangle$ and $|b\rangle = \gamma|0\rangle + \delta|1\rangle$. Expand:

$$|a\rangle \otimes |b\rangle = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle.$$

Match coefficients against $|\Phi^+\rangle$: we need $\alpha\gamma = 1/\sqrt{2}$, $\alpha\delta = 0$, $\beta\gamma = 0$, $\beta\delta = 1/\sqrt{2}$. The second equation forces $\alpha = 0$ or $\delta = 0$. If $\alpha = 0$, the first equation gives $0 = 1/\sqrt{2}$ — contradiction. If $\delta = 0$, the fourth gives the same contradiction. The state does not factor. There is no such $|a\rangle$ and $|b\rangle$.

That failure is entanglement, defined. A pure two-qubit state is entangled if and only if it cannot be written as a tensor product. No physics yet. Just algebra that returns a contradiction.

This chapter is about what follows from that contradiction. And what follows is — unexpectedly — almost everything interesting in quantum information science. The same state $|\Phi^+\rangle$ that cannot be factored is the state that violates Bell's inequality, the state that enables quantum teleportation, and the resource from which quantum computation draws its advantage over classical computation. Entanglement is not a curiosity of composite systems. It is a resource. This chapter is about how to spend it.

---

## What entanglement is not

Before the math, a clearing of ground. The most common student mistake is to equate any strong correlation with entanglement. A pair of letters in identical envelopes — one to Alice, one to Bob — are correlated: open one and you know the other. Two coins glued back-to-back are correlated perfectly. Neither is entangled in the quantum sense, because both can be described by a list of definite pre-existing values. The correlation comes from the shared preparation, not from any quantum property. You could in principle have learned the outcome before opening the envelope.

![Correlation strength is not the distinguishing feature — the pattern of correlations across incompatible measurement settings is](../images/12-entanglement-and-quantum-information-fig-01.png)
*Figure 12.1 — Comparison of correlation types *

Quantum entanglement is more specific. The correlations in $|\Phi^+\rangle$ cannot be accounted for by any pre-existing list of values. John Stewart Bell showed this in 1964 — not as a philosophical observation but as a theorem with a testable consequence: the entangled correlations violate an inequality that any pre-existing-value model must satisfy. That inequality is the chapter's first stop.

---

## Bell's theorem and the CHSH inequality

Alice and Bob each hold one qubit from a shared entangled pair. Alice chooses between two measurement directions, $A_1$ and $A_2$. Bob chooses between $B_1$ and $B_2$. Each measurement returns $\pm 1$. They do this many times and compute the four correlation values $E(A_i, B_j) = \langle A_i B_j\rangle$.

Now define the CHSH parameter:

$$S = E(A_1, B_1) + E(A_1, B_2) + E(A_2, B_1) - E(A_2, B_2).$$

Suppose the world is local and realistic. "Local" means Alice's outcome depends only on her setting and some shared hidden variable $\lambda$, not on what Bob chose to measure. "Realistic" means each particle, at the moment of separation, carried a definite value for every measurement that might be performed on it. Formally: there is a hidden-variable distribution $\rho(\lambda)$ and deterministic functions $A_i(\lambda) \in \{+1, -1\}$, $B_j(\lambda) \in \{+1, -1\}$ such that

$$E(A_i, B_j) = \int A_i(\lambda) B_j(\lambda)\, \rho(\lambda)\, d\lambda.$$

Plug into $S$, factor by $A_1$ and $A_2$:

$$S(\lambda) = A_1(\lambda)\bigl[B_1(\lambda) + B_2(\lambda)\bigr] + A_2(\lambda)\bigl[B_1(\lambda) - B_2(\lambda)\bigr].$$

Now use a simple observation: $B_1(\lambda)$ and $B_2(\lambda)$ are each $\pm 1$, so exactly one of $B_1 + B_2$ and $B_1 - B_2$ is zero and the other is $\pm 2$. There is no case where both are nonzero simultaneously. So at every value of $\lambda$, $|S(\lambda)| = 2$. Therefore:

$$|S| = \biggl|\int S(\lambda)\,\rho(\lambda)\,d\lambda\biggr| \leq \int |S(\lambda)|\,\rho(\lambda)\,d\lambda = 2.$$

For any local hidden-variable theory whatever — any hidden variable, any distribution, any deterministic response functions — $|S| \leq 2$. This is the CHSH bound. The derivation assumed nothing about the form of the hidden variables. It assumed only that outcomes are $\pm 1$, that they are predetermined, and that Alice's outcome does not depend on Bob's choice.

Now compute $S$ in quantum mechanics for the state $|\Phi^+\rangle$. For measurements along directions in the $xz$-plane at angles $\theta_a$ and $\theta_b$, a short calculation gives

$$E(\hat a, \hat b) = \langle\Phi^+|(\hat a \cdot \vec\sigma)\otimes(\hat b \cdot \vec\sigma)|\Phi^+\rangle = \cos(\theta_a - \theta_b).$$

The correlation depends only on the relative angle. Now pick the four angles that maximize $S$:

$$\theta_{A_1} = 0°, \quad \theta_{A_2} = 90°, \quad \theta_{B_1} = 45°, \quad \theta_{B_2} = -45°.$$

The four correlations:

$$E(A_1, B_1) = \cos(-45°) = +\tfrac{1}{\sqrt{2}}, \quad E(A_1, B_2) = \cos(45°) = +\tfrac{1}{\sqrt{2}},$$
$$E(A_2, B_1) = \cos(45°) = +\tfrac{1}{\sqrt{2}}, \quad E(A_2, B_2) = \cos(135°) = -\tfrac{1}{\sqrt{2}}.$$

$$S = \tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} - \bigl(-\tfrac{1}{\sqrt{2}}\bigr) = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.828.$$

![The classical bound is violated across a range of angles roughly 90° wide centered on the optimal setting — not only at a single point](../images/12-entanglement-and-quantum-information-fig-02.png)
*Figure 12.2 — S vs*

The local realistic bound is $2$. The quantum prediction is $2\sqrt{2}$. The two differ by $\sqrt{2}$. The experiment can decide between them. Bell's theorem, in the form derived by Clauser, Horne, Shimony, and Holt in 1969, is the cleanest conjunction of mathematical necessity and physical experiment in all of physics. No physical assumptions are hidden. The bound is algebraically necessary given local realism, and the quantum prediction exceeds it.

Boris Tsirelson showed in 1980 that $2\sqrt{2}$ is the maximum quantum mechanics ever produces — no state and no measurement can push $|S|$ above $2\sqrt{2}$. Hypothetical theories exist that respect no-signaling and would produce $|S|$ up to $4$. Nature, for reasons still not fully understood, stops at $2\sqrt{2}$.

---

## What the experiments showed

Clauser and Freedman tested an early version in 1972. Aspect, Dalibard, and Roger closed the locality loophole in 1982, separating Alice and Bob far enough that settings were chosen after the particles were in flight. The detection loophole — the possibility that only a biased sample of photon pairs was detected — required high-efficiency detectors that took longer to build. By 2015 three independent groups closed all loopholes simultaneously.

Hensen et al. at Delft used electron spins in nitrogen-vacancy centers 1.3 km apart, entangled through photons, and measured $S = 2.42$ — above 2 by more than two standard deviations of experimental uncertainty. Giustina et al. in Vienna used entangled photons with superconducting detectors and violated the bound by 11.5 standard deviations. Shalm et al. at NIST pushed to similar margins with a third independent platform. Three different physical implementations. Three different loophole-closing strategies. The same answer: the local-realistic bound is violated. The case is settled.

| year | platform | loophole closed | measured S value | significance |
| --- | --- | --- | --- | --- |
| Freedman & Clauser 1972, Aspect et al. 1982, Hensen et al. 2015 (Delft | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| Giustina et al. 2015 (Vienna | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| Shalm et al. 2015 (NIST | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| columns: year, platform, loophole closed, measured S value, significance | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

In October 2022 the Nobel Committee gave the physics prize to Alain Aspect, John Clauser, and Anton Zeilinger for this work. The citation acknowledged what had happened over the sixty years since EPR: what began as a philosophical dispute about the completeness of quantum mechanics had become the experimental foundation for a new technology. Foundations and infrastructure had met.

---

## What Bell's theorem does and does not say

Bell's theorem proves that no local realistic theory reproduces the quantum predictions. What it does not prove is that quantum mechanics is non-local in any operationally useful sense.

Alice and Bob are spacelike separated. Alice measures her qubit. Her outcome is random. She cannot choose what outcome to get. She cannot encode a message in her result. Bob's local statistics are independent of anything Alice does — we can show this directly. Bob's reduced density matrix is

$$\hat\rho_B = \text{Tr}_A\bigl(|\Phi^+\rangle\langle\Phi^+|\bigr) = \tfrac{1}{2}\hat{I}.$$

The maximally mixed state. Whatever measurement Alice performs, whatever outcome she gets, Bob's local probability distribution does not change. The correlations only appear when Alice and Bob compare notes — which requires a classical channel at or below the speed of light. This is the **no-signaling theorem**: no operation Alice can perform on her qubit changes Bob's local statistics. Entanglement is non-classical but non-signaling.

The popular misreading — "entanglement enables faster-than-light communication" — fails because the correlation is invisible to either party individually. You need both outcomes to see it. You cannot see the correlation until you communicate classically, and classical communication is bounded by $c$.

The Bell experiment does force a choice. You can give up locality (Bohmian mechanics does this — it keeps hidden variables but allows non-local influences). You can give up realism (outcomes exist only when measured). You can give up the assumption that each measurement has a unique outcome (many-worlds). What you cannot do is keep all three and reproduce the quantum predictions. Bell's theorem is a result about which combinations are coherent.

---

## The four Bell states and the Bloch sphere

The two-qubit Hilbert space is four-dimensional. There is a natural orthonormal basis of maximally entangled states — the Bell basis:

$$|\Phi^\pm\rangle = \tfrac{1}{\sqrt{2}}\bigl(|00\rangle \pm |11\rangle\bigr), \qquad |\Psi^\pm\rangle = \tfrac{1}{\sqrt{2}}\bigl(|01\rangle \pm |10\rangle\bigr).$$

Each is maximally entangled in a precise sense: the reduced density matrix of either qubit alone is $\hat{I}/2$ — the most mixed single-qubit state. All the information is in the joint correlations, none in either particle individually.

The singlet $|\Psi^-\rangle$ is special: it is rotationally invariant. Rotate both spins simultaneously by any single-qubit unitary $U$ and the singlet is unchanged up to a global phase: $(U \otimes U)|\Psi^-\rangle = (\det U)|\Psi^-\rangle$. The correlation it produces is $E(\hat a, \hat b) = -\hat a \cdot \hat b$ — it depends only on the dot product of the measurement axes.

![A pure single-qubit state sits on the surface of the Bloch sphere. When two qubits are maximally entangled, neither has a well-defined Bloch vector — both arrows shrink to the origin](../images/12-entanglement-and-quantum-information-fig-03.png)
*Figure 12.3 — Bloch sphere diagram showing four representative qubit states*

Single qubits live on the Bloch sphere. A pure qubit state is $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$, parameterized by two angles — a point on the unit sphere in $\mathbb{R}^3$, with $|0\rangle$ at the north pole and $|1\rangle$ at the south. Single-qubit gates are rotations of this sphere. The Hadamard gate is a $\pi$-rotation about the axis halfway between $\hat{x}$ and $\hat{z}$: it takes $|0\rangle$ to $(|0\rangle + |1\rangle)/\sqrt{2}$ and $|1\rangle$ to $(|0\rangle - |1\rangle)/\sqrt{2}$.

When two qubits are entangled, neither qubit has a well-defined Bloch vector. The reduced density matrix of each qubit is $\hat{I}/2$ — the center of the sphere. The Bloch vector has length zero. The information is non-local; there is nothing useful to say about either qubit alone.

---

## Preparing a Bell state: two gates

The recipe for $|\Phi^+\rangle$ from the computational basis state $|00\rangle$ uses exactly two operations.

Apply Hadamard to qubit 0:

$$(H \otimes I)|00\rangle = \tfrac{1}{\sqrt{2}}\bigl(|00\rangle + |10\rangle\bigr).$$

This is still a product state: it factors as $|+\rangle \otimes |0\rangle$. No entanglement yet.

Apply the CNOT gate — it flips the target qubit if and only if the control qubit is $|1\rangle$:

$$\text{CNOT}\cdot\tfrac{1}{\sqrt{2}}\bigl(|00\rangle + |10\rangle\bigr) = \tfrac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr) = |\Phi^+\rangle.$$

![Entanglement is created at the CNOT — not before. The Hadamard creates superposition; the CNOT creates the correlations](../images/12-entanglement-and-quantum-information-fig-04.png)
*Figure 12.4 — Three-step Bell-state preparation circuit *

Two gates. One $H$, one CNOT. The Bloch vectors for both qubits, which pointed to the north pole before the circuit, collapse to the origin after the CNOT. Neither qubit has a pure state. Their joint state is maximally entangled.

Together with single-qubit rotations and a phase gate, CNOT generates a universal gate set: any unitary on any number of qubits can be approximated to arbitrary precision. Every quantum computation that has ever run, every quantum algorithm that has been proposed, is built from this gate plus single-qubit unitaries.

The philosophical object — entanglement, identified by Einstein as a sign that quantum mechanics was incomplete, tested by Bell and the experimenters, confirmed in 2015 — is operationally generated by two specific matrix multiplications in two clock cycles. Foundations and engineering, on the same page.

---

## No-cloning

Can we copy a qubit? Suppose there exists a unitary $\hat U$ such that $\hat U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for any unknown state $|\psi\rangle$. Apply it to two states $|\psi\rangle$ and $|\phi\rangle$:

$$\hat U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle, \quad \hat U|\phi\rangle|0\rangle = |\phi\rangle|\phi\rangle.$$

Unitaries preserve inner products. Take the inner product of both sides:

$$\langle\phi|\psi\rangle = \langle\phi|\psi\rangle^2.$$

A number equal to its own square is either 0 or 1. So $|\psi\rangle$ and $|\phi\rangle$ are either orthogonal or identical. Arbitrary unknown states cannot be cloned. (Wootters and Zurek proved this in 1982; Dieks independently the same year.)

The no-cloning theorem is not a limitation of current technology. It is structural — a consequence of unitarity and linearity. Its consequences cascade: quantum key distribution cannot be intercepted without detection, because eavesdropping requires cloning. Quantum error correction cannot use simple redundancy and must use encoding schemes that hide information in entangled states. And no-cloning enforces no-signaling: if Bob could clone his received qubit, he could distinguish Alice's measurement bases statistically, and she could signal FTL.

---

## Teleportation

If we cannot copy quantum states, can we move them? Yes — at the cost of one shared Bell pair and two classical bits.

Alice has an unknown qubit $|\psi\rangle_1 = \alpha|0\rangle + \beta|1\rangle$. She and Bob share $|\Phi^+\rangle_{23}$. The full three-qubit state:

$$|\psi\rangle_1 \otimes |\Phi^+\rangle_{23} = \tfrac{1}{\sqrt{2}}\bigl(\alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle\bigr).$$

Rewrite qubits 1 and 2 in the Bell basis:

$$= \tfrac{1}{2}\bigl[|\Phi^+\rangle_{12}(\alpha|0\rangle + \beta|1\rangle)_3 + |\Phi^-\rangle_{12}(\alpha|0\rangle - \beta|1\rangle)_3 + |\Psi^+\rangle_{12}(\beta|0\rangle + \alpha|1\rangle)_3 + |\Psi^-\rangle_{12}(\beta|0\rangle - \alpha|1\rangle)_3\bigr].$$

Alice measures qubits 1 and 2 in the Bell basis. She gets one of four outcomes with equal probability $1/4$. Bob's qubit collapses to one of four states, each differing from $|\psi\rangle$ by a known unitary. Alice phones Bob her two-bit measurement outcome. Bob applies one correction from $\{I, Z, X, XZ\}$ and recovers $|\psi\rangle$ exactly.

![The quantum state is not transmitted — the entanglement was pre-shared. The two classical bits determine which correction Bob applies; without them, his qubit is useless](../images/12-entanglement-and-quantum-information-fig-05.png)
*Figure 12.5 — Quantum teleportation protocol diagram *

What crossed the spacelike gap? Nothing physical — the entanglement was shared in advance. What traveled at the speed of light? Two classical bits. What happened to the original on qubit 1? It was destroyed in Alice's Bell measurement. Bob received the state; Alice no longer has it. No cloning occurred.

The protocol was demonstrated experimentally by the Zeilinger group in 1997. It is now routine in quantum network architectures. The two classical bits are not an implementation limitation — they are required by the no-signaling theorem. Without them, Bob's qubit is maximally mixed, useless. Teleportation is as fast as light, not faster.

---

## Decoherence and the cost of entanglement

Real entangled states do not stay entangled. They interact with the environment — stray electromagnetic fields, phonons, residual gas molecules — and the joint system becomes entangled with the environment instead of with the partner qubit. Trace out the environment and the two-qubit state is no longer pure. The Bloch vector of each qubit, already at the origin for a maximally entangled pair, begins to lose even that property as the environment mixes in. Two timescales govern the decay: $T_1$, the energy relaxation time, over which an excited qubit decays to the ground state; and $T_2 \leq 2T_1$, the dephasing time, over which the off-diagonal elements of the density matrix decay.

Every quantum protocol runs in a race against $T_2$. Teleportation requires the Bell pair to remain entangled long enough to perform a Bell measurement. Quantum computation requires coherence over the full circuit depth. Quantum error correction — Chapter 13 — is the engineering response: encoding logical qubits in many physical qubits so that the leakage of entanglement into the environment can be detected and reversed before it corrupts the computation.

![Running a Bell test on your hardware and measuring S is a direct diagnostic of remaining entanglement — S = 2 is the boundary between useful and classical](../images/12-entanglement-and-quantum-information-fig-06.png)
*Figure 12.6 — CHSH parameter S vs*

The Tsirelson bound is $2\sqrt{2}$. As decoherence degrades the Bell state toward a mixed state, $S$ decreases from $2\sqrt{2}$ toward 2 and below. The boundary at $S = 2$ is literally the boundary between useful quantum correlations and those reproducible by a local classical model. Running a Bell test on your quantum hardware and measuring $S$ is a direct diagnostic of how much entanglement you have left.

---

## Still puzzling

The Tsirelson bound $|S| \leq 2\sqrt{2}$ stops quantum correlations short of the algebraic maximum $|S| = 4$. Popescu-Rohrlich boxes — hypothetical devices — would achieve $|S| = 4$ while still respecting no-signaling. Nature does not allow them. Pawlowski et al. showed in 2009 that PR-box correlations would violate *information causality* — a principle saying that $n$ classical bits of communication can convey at most $n$ bits of useful information, no matter what shared correlations are in place. This gives a principled reason why $2\sqrt{2}$ is the ceiling. But the derivation uses information causality as an axiom. Why information causality? At some point the chain of derivations ends in a principle we cannot derive from anything simpler. The Tsirelson bound is one of the few quantitative facts in physics whose physical explanation I cannot trace to a more primitive foundation. The math is settled. What the math means, at this level, is still open.

---

## LLM Exercise — Bell inequality simulator and gate circuit visualizer

You are going to build a two-panel D3 simulation that puts the CHSH parameter on screen as a live number and lets you drive it across the classical bound by tuning angles, then watch Bell-state preparation as Bloch vectors collapse to the origin under the action of a CNOT.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 12 — Entanglement and Quantum Information
Deliverable: 12-bell-inequality.html
Status: in progress

The simulation has two panels in one HTML file:

Panel A — CHSH Bell-inequality simulator (700 x 600 SVG).
- State selector: |Phi+>, |Phi->, |Psi+>, |Psi-> (Bell states); plus
  |00>, |+>|+> (product states); plus a classical-mixture toggle
  (mix |00> and |11> with 50/50 probability — perfectly correlated
  but not entangled).
- Four angle sliders: theta_A1, theta_A2, theta_B1, theta_B2,
  each in 0 to 2 pi radians, displayed in degrees.
- 2x2 outcome-probability table for each of the four (A_i, B_j)
  measurement pairs, updating live on slider change.
- Large display (~48 pt font) of the CHSH parameter S.
  Background color flips from white to amber when |S| > 2.
- Sub-panel below: S as a function of the relative angle
  (theta_A1 - theta_B1) with the other angles held at the
  optimal offsets. Horizontal red line at S = 2 (classical bound).
  Horizontal gold line at S = 2 sqrt(2) ~ 2.828 (Tsirelson bound).

Panel B — Gate-circuit visualizer (700 x 400 SVG).
- Two-qubit grid. Gates draggable from a palette: H, X, Y, Z,
  S, T, CNOT, Rz.
- Live display of the joint state vector as four complex amplitudes
  (modulus as bar height, phase as a small dial color-coded by HSL).
- Per-qubit Bloch spheres (one for each of the two qubits) showing
  the reduced state. Vector lives on the surface for product states
  and collapses to the origin for maximally entangled states.
- Default scaffold: |00> -> H on qubit 0 -> CNOT (control 0, target 1).
  Displays "|Phi+>" symbolically. Both Bloch vectors visibly collapse
  to the origin as the CNOT is applied.
- Measurement-outcome bar chart at the right (P(00), P(01), P(10), P(11)).

Sliders use snap-to-canonical-angles option: 0, 22.5, 45, 67.5, 90, 135.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md (coding constitution) the following physics rules for
Chapter 12 simulations:

ENTANGLEMENT AND QUANTUM-INFORMATION PHYSICS RULES

1. Two-qubit states are stored as complex 4-vectors over the basis
   |00>, |01>, |10>, |11>. Always normalize: sum |c_i|^2 must equal 1
   to within 1e-6 after every operation. Display a warning if not.

2. Single-qubit gates are 2x2 unitaries. To apply a single-qubit gate
   U to qubit 0, build U_full = U (tensor) I_2 (4x4). To apply to qubit 1,
   build U_full = I_2 (tensor) U. Use explicit Kronecker product code;
   do not hard-code matrix entries for two-qubit space.

3. CNOT in the basis |00>, |01>, |10>, |11> with control = qubit 0
   and target = qubit 1 is:
     [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
   Verify on |10>: should map to |11>.

4. CHSH calculation: for measurement axis (theta_A, theta_B) in the
   xz-plane, the measurement operator on Alice is
     sigma_a = sin(theta_A) * sigma_x + cos(theta_A) * sigma_z
   and analogously on Bob. The two-qubit operator is
     sigma_a (tensor) sigma_b
   The correlation is E(a, b) = <psi| sigma_a (tensor) sigma_b |psi>.

5. The CHSH parameter is
     S = E(A1, B1) + E(A1, B2) + E(A2, B1) - E(A2, B2)
   Show S to three decimal places. Background color flips when |S| > 2.

6. The Tsirelson bound is 2 * sqrt(2) ~ 2.8284. Display this as a
   horizontal gold line on the S-vs-angle sub-panel.

7. Reduced density matrices for the per-qubit Bloch sphere visualization:
     rho_A = Tr_B(|psi><psi|) computed as
       rho_A[i,j] = sum_k psi[i,k] * conj(psi[j,k])
     where psi[i,k] is the amplitude for Alice in state i and Bob in
     state k. Compute rho_B symmetrically. The Bloch vector is
       r_x = 2 Re(rho[0,1]), r_y = 2 Im(rho[1,0]), r_z = rho[0,0] - rho[1,1].

KNOWN FAILURE MODES to avoid:
(a) Tensor-product index ordering swapped (qubit-0 vs qubit-1 confusion).
    Verify on a known case: apply CNOT to |10>, confirm you get |11>.
(b) Phase convention drift between Alice and Bob axes. Stick to
    sin(theta) * sigma_x + cos(theta) * sigma_z everywhere.
(c) Normalization lost after multi-gate compositions. Renormalize and
    warn if |norm - 1| > 1e-4.
(d) Bloch vector visualized off-surface for pure states (rounding error).
    Clamp |r| to <= 1.
(e) Reduced density matrix not Hermitian (off-diagonals wrong sign).
    Verify rho^dagger = rho before extracting Bloch components.
(f) Slider snapping rounds angles to multiples of 5 degrees instead of
    the canonical CHSH angles. Provide both modes; default to canonical.
(g) State selector switches between "classical mixture" and "Bell state"
    without resetting the density matrix. Classical mixture has off-
    diagonal blocks zero in the |00>/|11> basis; Bell state has them
    nonzero. Make sure the simulator distinguishes.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 12-bell-inequality.html: a single self-contained HTML file using
D3 v7 from a CDN, no other dependencies, that implements the Chapter 12
simulation as specified in PROJECT.md and following the physics rules
in CLAUDE.md and the visual constitution in DESIGN.md.

The simulation has two stacked panels (top: CHSH panel, bottom: gate
panel), each in its own SVG.

CHSH PANEL (700 x 600).
- State selector at top: radio buttons for |Phi+>, |Phi->, |Psi+>,
  |Psi->, |00>, |+>|+>, and "classical mixture (1/2 |00><00| + 1/2 |11><11|)".
- Four angle sliders below: theta_A1, theta_A2, theta_B1, theta_B2 in
  degrees, range 0 to 360, step 0.5. Canonical-snap toggle defaults on.
- 2x2 outcome-probability table for each of the four (A_i, B_j) pairs,
  laid out as a 2x4 grid of small tables. Each cell shows P(++), P(+-),
  P(-+), P(--) updated live.
- Large CHSH-value display in the center: "S = 2.828" at 48 pt.
  Background of the display flips to amber (#FFC107) when |S| > 2.
- Sub-panel at the bottom (700 x 200): plot of S vs (theta_A1 - theta_B1)
  with the other three angles fixed at their optimal-relative-offset
  values. Horizontal red line at y = 2, horizontal gold line at y = 2*sqrt(2).

GATE PANEL (700 x 400).
- Gate palette on the left: H, X, Y, Z, S, T, CNOT, Rz(theta).
  Each gate is a small draggable rectangle.
- Two-qubit circuit grid: two horizontal wires (qubit 0 on top), each
  with five empty gate slots in series. Drop a gate into a slot to add
  it to the circuit. CNOT spans both wires with a filled dot on the
  control and an open circle on the target. Click any slot to clear.
- Right side, three sub-displays:
  - Amplitude bar chart: four bars labeled |00>, |01>, |10>, |11>.
    Height = |c_i|, color hue = phase of c_i (HSL 0..360).
  - Two small Bloch spheres (150 x 150 each, stacked), one per qubit.
    Show the Bloch vector as an orange arrow from origin to (r_x, r_y, r_z).
    Equator and meridian as light grey circles.
  - Measurement-outcome probabilities P(00), P(01), P(10), P(11) as
    a small bar chart at opacity 0.7.

DEFAULT SCAFFOLD on load: |00> initial, qubit 0 wire has H in slot 1,
CNOT spanning both wires in slot 2 with control on qubit 0. The simulator
should display the resulting state as
  c = [1/sqrt(2), 0, 0, 1/sqrt(2)]
the amplitude bars show two bars of equal height, both Bloch vectors
have shrunk to the origin (because each reduced density matrix is I/2),
and a small symbolic label reads "|Phi+>".

Spatial grid for the CHSH sub-panel curve: 361 points in
(theta_A1 - theta_B1) from 0 to 2 pi. Live re-render on every slider change.

Runtime sanity checks (write to console):
- Sum |c_i|^2 = 1 within 1e-4 at every frame.
- For |Phi+> with canonical angles, S should display 2.828 +/- 0.001.
- For |00>, S must be in [-2, 2] for every angle choice. If the simulator
  reports |S| > 2 with a product state, flag a numerical bug.
- For the classical mixture, S must be in [-2, 2] for every angle choice.

Do NOT use any 3D library; the Bloch spheres are 2D projections of 3D
vectors using an orthographic projection. Do NOT use math.js; implement
the 4x4 matrix-vector and tensor-product arithmetic in vanilla JS.
Comments at every non-trivial physics step.
```

### Part 4 — Exploration tasks and extension prompt

Run the simulation and answer the following:

1. Set the state to $|\Phi^+\rangle$. Set angles to $(\theta_{A_1}, \theta_{A_2}, \theta_{B_1}, \theta_{B_2}) = (0°, 90°, 45°, -45°)$. Read $S$. You should see $S = 2.828$ — the Tsirelson bound. The background should be amber.

2. Now switch the state to $|00\rangle$ (a product state). Try every angle setting you can think of. Can you push $|S|$ above $2$? Why or why not?

3. Switch the state to "classical mixture" ($\tfrac{1}{2}|00\rangle\langle 00| + \tfrac{1}{2}|11\rangle\langle 11|$). The measurement outcomes are perfectly correlated when Alice and Bob measure in the $z$-basis. Try angles. Can you push $|S|$ above $2$? Conclude: perfect correlation is not the same as entanglement.

4. Switch back to $|\Phi^+\rangle$. Hold three angles at the canonical settings and sweep $\theta_{A_1}$ slowly through one full revolution. Watch the $S$-vs-angle curve in the sub-panel. Identify where $S$ peaks at $+2\sqrt{2}$, where it bottoms at $-2\sqrt{2}$, and where it crosses zero.

5. In the gate panel, build the Bell preparation $|00\rangle \to H$ on qubit 0 $\to$ CNOT. Watch the two Bloch vectors. They start at the north pole. After Hadamard, qubit 0's vector points along $+\hat{x}$. After CNOT, both Bloch vectors collapse to the origin. Explain in one sentence what the collapse means physically.

6. In the gate panel, build a different circuit: $|00\rangle \to X$ on qubit 1 $\to H$ on qubit 0 $\to$ CNOT. Identify which Bell state you produced.

**Extension prompt:**

```
Modify 12-bell-inequality.html to add a third panel implementing the
quantum-teleportation protocol of Bennett et al. 1993:

- Initial state: |psi>_1 = alpha |0> + beta |1> on qubit 1, with sliders
  for the angles theta, phi parameterizing alpha = cos(theta/2),
  beta = exp(i phi) sin(theta/2). Qubits 2 and 3 are in the Bell state
  |Phi+>.
- Step button: applies one of three operations in sequence
    (i) CNOT with control qubit 1 and target qubit 2;
    (ii) H on qubit 1;
    (iii) measure qubits 1 and 2 in the computational basis; randomly
         sample an outcome with the correct probabilities (1/4 each);
    (iv) apply the correction (I, X, Z, or XZ) to qubit 3 based on
         the measurement outcome.
- Display: the unknown qubit's Bloch vector at the start (on qubit 1);
  the Bell pair's joint state (qubits 2 and 3); the final state of
  qubit 3 after the protocol. Verify that the final state of qubit 3
  matches the initial state of qubit 1.
- Two classical-bit indicators (the measurement outcomes on qubits 1
  and 2): show them as small bit-displays that "travel" from Alice to
  Bob along a dashed grey line, animated at finite speed to emphasize
  that the protocol is no faster than light.

Update PROJECT.md to mark Chapter 12 as complete and note the
teleportation extension as the bridge to Chapter 13's decoherence
discussion: the protocol works perfectly with ideal entanglement;
real Bell pairs decohere, and the chapter 13 simulation lets you
watch the resource degrade.
```

---

## Exercises

### Warm-up

1. *[Tests: entanglement definition, factorization argument]* Show that the state $|\Psi^+\rangle = (|01\rangle + |10\rangle)/\sqrt{2}$ is entangled by the same contradiction argument used in the chapter opening for $|\Phi^+\rangle$. Then verify that $|\Psi^+\rangle$ is properly normalized and that it is orthogonal to $|\Phi^+\rangle$. *Difficulty: warm-up.*

2. *[Tests: CHSH algebra, LHV bound]* In the CHSH derivation, the key step is that $B_1(\lambda) + B_2(\lambda)$ and $B_1(\lambda) - B_2(\lambda)$ cannot both be nonzero simultaneously when $B_1, B_2 \in \{+1, -1\}$. Verify this by checking all four cases $(B_1, B_2) \in \{(+1,+1), (+1,-1), (-1,+1), (-1,-1)\}$ and computing $|S(\lambda)|$ for each. Confirm that $|S(\lambda)| = 2$ in every case. *Difficulty: warm-up.*

3. *[Tests: no-cloning proof, inner product argument]* Reproduce the no-cloning proof from the chapter for the specific case $|\psi\rangle = |+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ and $|\phi\rangle = |0\rangle$. Compute $\langle\phi|\psi\rangle = \langle 0|+\rangle$ explicitly and verify that it satisfies neither $\langle\phi|\psi\rangle = 0$ nor $\langle\phi|\psi\rangle = 1$, confirming that cloning these two states is impossible. *Difficulty: warm-up.*

### Application

4. *[Tests: quantum correlation computation, CHSH at suboptimal angles]* For the Bell state $|\Phi^+\rangle$ and the measurement directions $\theta_{A_1} = 0°$, $\theta_{A_2} = 60°$, $\theta_{B_1} = 30°$, $\theta_{B_2} = 90°$, compute all four correlations $E(A_i, B_j) = \cos(\theta_{A_i} - \theta_{B_j})$ and evaluate $S$. Compare to the classical bound $|S| \leq 2$ and the Tsirelson bound $2\sqrt{2}$. Is this angle choice optimal? *Difficulty: application.*

5. *[Tests: reduced density matrix, no-signaling]* Alice and Bob share $|\Phi^+\rangle$. Alice applies the Pauli $X$ gate to her qubit and then measures in the $z$-basis. (a) What is the joint state after Alice applies $X$ to her qubit? (b) Compute Bob's reduced density matrix $\hat\rho_B = \text{Tr}_A(\rho_{AB})$ before and after Alice's gate. (c) Confirm that Bob's local statistics are unchanged by Alice's operation, verifying the no-signaling theorem for this case. *Difficulty: application.*

6. *[Tests: Bell-state preparation, CNOT action]* Starting from each of the four computational basis states $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$, apply $H \otimes I$ followed by CNOT and identify which Bell state is produced in each case. Organize the results as a table. Confirm that all four Bell states can be reached from the computational basis by this two-gate circuit. *Difficulty: application.*

### Synthesis

7. *[Tests: CHSH for product states, why classical correlations cannot violate]* For the product state $|+\rangle \otimes |+\rangle = (|0\rangle + |1\rangle)/\sqrt{2} \otimes (|0\rangle + |1\rangle)/\sqrt{2}$, show that $E(\hat a, \hat b) = \langle +|\hat a \cdot \vec\sigma|+\rangle \cdot \langle +|\hat b \cdot \vec\sigma|+\rangle$ — that is, the two-qubit correlation factorizes as a product of single-qubit expectation values. Use this factorization to argue that no product state can violate the CHSH inequality, without computing $S$ for every possible angle. *Difficulty: synthesis.*

8. *[Tests: teleportation resource accounting, no-cloning consistency]* In the teleportation protocol, Alice transmits two classical bits to Bob and they consume one Bell pair. (a) Why are the two classical bits necessary — what goes wrong if Alice omits them? Compute Bob's reduced density matrix after Alice's Bell measurement, without the classical communication, and show it is $\hat I/2$. (b) The protocol transfers an unknown qubit state from Alice to Bob without Alice learning what the state is. Explain why this is consistent with the no-cloning theorem. (c) If Alice and Bob started with two shared Bell pairs instead of one, could they transmit two unknown qubit states simultaneously with four classical bits? *Difficulty: synthesis.*

### Challenge

9. *[Tests: Tsirelson bound, optimization over measurement angles]* The CHSH parameter for $|\Phi^+\rangle$ with planar measurement axes is $S = \cos(\theta_{A_1} - \theta_{B_1}) + \cos(\theta_{A_1} - \theta_{B_2}) + \cos(\theta_{A_2} - \theta_{B_1}) - \cos(\theta_{A_2} - \theta_{B_2})$. (a) Taking partial derivatives of $S$ with respect to all four angles and setting them to zero, show that the optimal solution requires all four pairwise relative angles to have equal magnitude. (b) Find the optimal angles and confirm $S_{\max} = 2\sqrt{2}$. (c) Tsirelson's bound states that $2\sqrt{2}$ is the maximum for *any* quantum state and *any* $\pm 1$-valued measurements. Sketch an argument for why a state with Schmidt decomposition $|\psi\rangle = \cos\alpha|00\rangle + \sin\alpha|11\rangle$ achieves $S \leq 2\sqrt{2}$, with equality only when $\alpha = \pi/4$ (the maximally entangled case). *Difficulty: challenge.*

---

**Chapter 13** takes the density matrix — the object that describes a qubit when it is entangled with the environment — and derives the equations governing how it evolves when the environment cannot be ignored. The Bloch vectors that collapsed to the origin in this chapter will spiral inward along $T_1$ and $T_2$ trajectories. Decoherence is the leak; quantum error correction is the plug.
