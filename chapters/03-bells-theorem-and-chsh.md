# Chapter 3 — Bell's Theorem and the CHSH Inequality
*A calculation that turned a philosophical dispute into a number — and a number that turned out to be wrong for anyone who believed in hidden instructions.*

Here is an argument that seems ironclad. You put a left glove in one box and a right glove in another, seal both without looking, and ship one box to Nairobi and one to Oslo. The moment the Oslo recipient opens her box and finds a left glove, she knows the Nairobi glove is right — instantaneously, regardless of the 6,500 km between them. No one finds this alarming. The correlation existed before the boxes were opened; it was built in at the moment of packing.

For fifty years after quantum mechanics was born, many physicists believed entangled particles worked the same way. The two particles, they assumed, must carry definite instructions for every measurement they might later encounter — instructions encoded at the moment of creation, invisible in the formalism but real. Einstein called this the natural view. Bohr disagreed but could not produce a decisive experiment.

John Stewart Bell changed the situation in 1964 — not with a philosophical argument but with a calculation. Bell showed that the glove story, applied to particles, leads to an inequality. Count the correlations the right way and the hidden-instruction story demands a number no larger than 2. Quantum mechanics predicts $2\sqrt{2}$. That gap is not a rounding error. It is large enough to measure in a table-top experiment with photon pairs and polarizers, and it has now been measured, by multiple independent groups, with no remaining wiggle room.

This chapter is that calculation — and its aftermath.

---

## What Local Realism Claims

"Local realism" sounds philosophical. It is easier to state as two assumptions that can be written in equations.

**Realism:** At the moment the two particles are created, each carries a definite pre-determined value for every measurement that could later be performed on it. Call the shared instruction set $\lambda$ — a hidden variable. Alice's outcome for setting $A_i$ is a deterministic function $A_i(\lambda) \in \{+1, -1\}$. Bob's outcome for $B_j$ is $B_j(\lambda) \in \{+1, -1\}$.

**Locality:** Alice's outcome depends only on her setting $A_i$ and the shared $\lambda$, not on what Bob chose to measure or what outcome Bob got. And vice versa.

There is a probability distribution $\rho(\lambda)$ over the instruction sets — we allow full generality here, placing no restrictions on the number of variables or their form. The correlation between Alice's and Bob's outcomes is:

$$E(A_i, B_j) = \int A_i(\lambda)\, B_j(\lambda)\, \rho(\lambda)\, d\lambda.$$

This is the only assumption. Nothing specific about the form of $\lambda$, nothing about how $A_i(\lambda)$ and $B_j(\lambda)$ are computed. Any model consistent with local realism can be written this way.

---

## The CHSH Inequality: Pure Algebra

Clauser, Horne, Shimony, and Holt found the combination that makes the constraint sharp. Define the **CHSH parameter**:

$$S = E(A_1, B_1) + E(A_1, B_2) + E(A_2, B_1) - E(A_2, B_2).$$

Three terms add; one subtracts. Substituting the local-realistic formula:

$$S = \int \bigl[A_1(\lambda) B_1(\lambda) + A_1(\lambda) B_2(\lambda) + A_2(\lambda) B_1(\lambda) - A_2(\lambda) B_2(\lambda)\bigr] \rho(\lambda)\, d\lambda.$$

Factor the integrand:

$$S(\lambda) \equiv A_1(\lambda)\bigl[B_1(\lambda) + B_2(\lambda)\bigr] + A_2(\lambda)\bigl[B_1(\lambda) - B_2(\lambda)\bigr].$$

Now use one observation: $B_1(\lambda)$ and $B_2(\lambda)$ are each $\pm 1$. In every possible case:

| $B_1$ | $B_2$ | $B_1 + B_2$ | $B_1 - B_2$ |
|-------|-------|-------------|-------------|
| $+1$ | $+1$ | $+2$ | $0$ |
| $+1$ | $-1$ | $0$ | $+2$ |
| $-1$ | $+1$ | $0$ | $-2$ |
| $-1$ | $-1$ | $-2$ | $0$ |

In every row, one factor is $\pm 2$ and the other is $0$. Therefore, for every $\lambda$: one of $|B_1 + B_2|$ and $|B_1 - B_2|$ is 2 and the other is 0. Since $|A_1(\lambda)| = |A_2(\lambda)| = 1$:

$$|S(\lambda)| = 1\cdot 2 + 1\cdot 0 = 2.$$

In every single case, $|S(\lambda)| = 2$ exactly. Averaging over $\lambda$:

$$|S| = \left|\int S(\lambda)\, \rho(\lambda)\, d\lambda\right| \leq \int |S(\lambda)|\, \rho(\lambda)\, d\lambda = 2.$$

$$\boxed{|S| \leq 2.}$$

No choices were made about $\lambda$, about $\rho(\lambda)$, or about the form of $A_i(\lambda)$ and $B_j(\lambda)$. The bound $|S| \leq 2$ is a theorem of arithmetic applied to $\pm 1$ numbers. If the world is locally realistic, $|S|$ cannot exceed 2. Full stop.

<!-- → [DIAGRAM: four-quadrant table of B₁, B₂ values with the key observation annotated: in every row one column is ±2 and the other is 0, so |S(λ)|=2 exactly — visualizing why the bound is tight rather than loose] -->

![four-quadrant table of B₁, B₂ values with the key observation annotated: in every row one column is ±2 and the other is 0, so |S(λ)|=2…](../images/03-bells-theorem-and-chsh-fig-01.png)
*Figure 3.1 — four-quadrant table of B₁, B₂ values with the key observation annotated: in every row one column is ±2 and the other is 0, so |S(λ)|=2…*

---

## What Quantum Mechanics Predicts

Now compute $S$ for the Bell state $|\Phi^+\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$. Alice measures along a direction at angle $\theta_a$ from the $z$-axis; Bob measures at angle $\theta_b$. The two-qubit operator is $(\hat{a}\cdot\vec{\sigma})\otimes(\hat{b}\cdot\vec{\sigma})$.

Using the identity $\langle\Phi^+|(\sigma_i \otimes \sigma_j)|\Phi^+\rangle = \delta_{ij}$ — only matching Pauli indices contribute — the correlation:

$$E(\hat{a}, \hat{b}) = \cos(\theta_a - \theta_b).$$

The correlation depends only on the relative angle between Alice's and Bob's measurement axes. For the singlet $|\Psi^-\rangle$ the formula is $E = -\cos(\theta_a - \theta_b)$, differing by a sign.

Choose four angles to maximize $S$. Taking partial derivatives of $S$ with respect to all four angles and setting to zero yields equally-spaced solutions; the canonical choice for $|\Phi^+\rangle$ is:

$$\theta_{A_1} = 0°, \quad \theta_{A_2} = 90°, \quad \theta_{B_1} = 45°, \quad \theta_{B_2} = -45°.$$

The four correlations:

$$E(A_1, B_1) = \cos(-45°) = +\frac{1}{\sqrt{2}}, \quad E(A_1, B_2) = \cos(45°) = +\frac{1}{\sqrt{2}},$$
$$E(A_2, B_1) = \cos(45°) = +\frac{1}{\sqrt{2}}, \quad E(A_2, B_2) = \cos(135°) = -\frac{1}{\sqrt{2}}.$$

Therefore:

$$S = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} - \!\left(-\frac{1}{\sqrt{2}}\right) = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.828.$$

The local-realistic bound is 2. The quantum prediction is $2\sqrt{2}$. The gap, $2\sqrt{2} - 2 \approx 0.828$, is 41% of the classical bound — large enough to measure in any decent optics lab.

<!-- → [CHART: "polar wheel" showing Alice's two measurement directions (0°, 90°) and Bob's two (45°, -45°) around a circle, with the four correlations annotated on the connecting arcs, and S = 2√2 displayed; classical bound at 2 shown as a gray ring] -->

!["polar wheel" showing Alice's two measurement directions (0°, 90°) and Bob's two (45°, -45°) around a circle, with the four correlations…](../images/03-bells-theorem-and-chsh-fig-02.png)
*Figure 3.2 — "polar wheel" showing Alice's two measurement directions (0°, 90°) and Bob's two (45°, -45°) around a circle, with the four correlations…*

---

## The Tsirelson Bound

Could quantum mechanics produce $|S| > 2\sqrt{2}$? Boris Tsirelson proved in 1980 that it cannot. For any quantum state and any $\pm 1$-valued observables, $|S| \leq 2\sqrt{2}$.

The argument: for anti-commuting observables $A_1, A_2$ each squaring to the identity, the operator $S^{\text{op}} = A_1 \otimes (B_1 + B_2) + A_2 \otimes (B_1 - B_2)$ satisfies $(S^{\text{op}})^2 \leq 8\,\mathbf{I}$, so its operator norm is at most $2\sqrt{2}$, and no state's expectation value can exceed the operator norm.

This places quantum mechanics in the gap $2 < |S| \leq 2\sqrt{2}$, firmly above the classical bound and firmly below the algebraic maximum of 4. Neither the minimum nor the maximum. Something principled is selecting exactly $2\sqrt{2}$.

What about "super-quantum" correlations? Hypothetical Popescu–Rohrlich boxes — devices that respect no-signaling but produce $|S| = 4$ — are logically conceivable. Pawlowski et al. showed in 2009 that such boxes would violate *information causality*: the principle that $n$ bits of classical communication can convey at most $n$ bits of useful information regardless of shared correlations. This gives a candidate reason why $2\sqrt{2}$ is the ceiling, though information causality must be adopted as an axiom rather than derived from anything more primitive. The deepest reason for the Tsirelson bound is still not fully understood.

---

## The Experimental Program

The gap between 2 and 2.828 is measurable. But before a measurement can rule out all local realistic models, two experimental loopholes must be closed.

**The detection loophole.** If detectors record only a fraction of produced pairs, a local model might arrange for only favorable pairs to be detected, faking a violation. Closing this requires detector efficiency above roughly 82%, so the detected sample is a fair representation of the whole ensemble.

**The locality loophole.** If Alice's measurement outcome can reach Bob's detector before Bob's measurement is complete — via a signal traveling at or below the speed of light — a local model can exploit this. Closing requires: Alice's and Bob's measurement events are spacelike separated; and measurement settings are chosen randomly after the pair is emitted, so no hidden variable in the particles can "know" the future settings at the time of creation.

The experimental history spans fifty years:

**Freedman and Clauser (1972).** First systematic Bell test with photon polarization correlations in an atomic cascade. Found a violation consistent with quantum mechanics — but left both loopholes open.

**Aspect, Dalibard, and Roger (1982).** Switched measurement settings at Orsay while photons were in flight — addressing the locality loophole for the first time. Detection efficiency still insufficient for the detection loophole.

**Hensen et al., Delft (2015).** Electron spins in nitrogen-vacancy centers in diamond, placed 1.3 km apart at opposite ends of the TU Delft campus. Entanglement via photon exchange. The 1.3 km separation ensured spacelike separation of measurement events (locality loophole closed). NV-center spin readout efficiency closed the detection loophole simultaneously. Result: $S = 2.42$, exceeding 2 by more than two standard deviations. *Nature* 526, 682.

**Giustina et al., Vienna (2015).** Entangled photon pairs detected with superconducting nanowire single-photon detectors. Both loopholes closed. Violated the CHSH bound by 11.5 standard deviations. *Physical Review Letters* 115, 250401.

**Shalm et al., NIST (2015).** Independent quantum random-number generators set the measurement angles; entangled photons detected at high efficiency. Both loopholes closed. $p$-value as small as $5.9\times10^{-9}$. *Physical Review Letters* 115, 250402.

Three platforms. Three independent loophole-closing strategies. The same result.

<!-- → [FIGURE: horizontal timeline 1935–2022 with labeled events: EPR (1935), Bell's theorem (1964), Freedman-Clauser (1972), Aspect (1982), triple 2015 experiments (three overlapping points), Nobel Prize (2022, gold star); each event annotated with one-line description] -->

![horizontal timeline 1935–2022 with labeled events: EPR (1935), Bell's theorem (1964), Freedman-Clauser (1972), Aspect (1982), triple 2015…](../images/03-bells-theorem-and-chsh-fig-03.png)
*Figure 3.3 — horizontal timeline 1935–2022 with labeled events: EPR (1935), Bell's theorem (1964), Freedman-Clauser (1972), Aspect (1982), triple 2015…*

In October 2022, the Nobel Committee awarded the Physics Prize to **Alain Aspect, John Clauser, and Anton Zeilinger** "for experiments with entangled photons, establishing the violation of Bell's inequalities and pioneering quantum information science." The citation acknowledged a 60-year arc: from Einstein's 1935 objection, through Bell's 1964 theorem, through Clauser's 1972 experiment, Aspect's 1982 locality-closing refinement, and the 2015 loophole-free confirmation.

Since 2015, the frontier has moved to satellite-based Bell tests. In 2017, Yin et al. distributed entangled photons over 1,200 km between ground stations via the Micius satellite — the largest spacelike separation yet achieved. Device-independent quantum key distribution, where cryptographic security is certified by Bell violation alone without trusting the devices, was demonstrated experimentally by Nadlinger et al. in 2022.

---

## What Bell's Theorem Does and Does Not Say

Bell's theorem rules out local realism. It does not rule out quantum mechanics, which passes every test. It does not prove faster-than-light signaling. And it does not resolve the measurement problem.

**No faster-than-light signaling.** Alice and Bob are spacelike separated. Alice's result is random — she cannot choose it. Bob's reduced density matrix is:

$$\hat{\rho}_B = \mathrm{Tr}_A\bigl(|\Phi^+\rangle\langle\Phi^+|\bigr) = \frac{1}{2}\hat{I}.$$

Alice performing any operation on her qubit — measuring in any basis, applying any unitary, doing nothing at all — leaves Bob's marginal statistics unchanged. The correlation between their outcomes is visible only when they compare notes via a classical channel. Classical channels are bounded by $c$. Entanglement is non-classical, but it is non-signaling.

**A forced interpretational choice.** Bell's theorem forces you to choose which assumption to abandon. Three positions are coherent:

Give up realism: outcomes do not exist before measurement. Standard Copenhagen takes this view. Give up locality: Bohmian mechanics retains definite trajectories but allows non-local influences through the pilot wave. Give up uniqueness of outcomes: many-worlds retains locality and determinism but allows every outcome to occur in different branches.

You cannot retain all three and reproduce quantum predictions. Bell's theorem makes that impossibility precise. Which assumption to jettison is not a question the experiment answers. It is a question you bring to the experiment.

---

## A Worked Calculation: $S$ for the Singlet

For the singlet $|\Psi^-\rangle = \tfrac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$, the correlation formula is $E(\hat{a}, \hat{b}) = -\cos(\theta_a - \theta_b)$ — opposite sign from $|\Phi^+\rangle$. The sign convention in $S$ matters. With the same four angles $(0°, 90°, 45°, -45°)$ as above and $E = -\cos$:

$$E(A_1, B_1) = -\cos(-45°) = -\frac{1}{\sqrt{2}},\quad E(A_1, B_2) = -\cos(45°) = -\frac{1}{\sqrt{2}},$$
$$E(A_2, B_1) = -\cos(45°) = -\frac{1}{\sqrt{2}},\quad E(A_2, B_2) = -\cos(135°) = +\frac{1}{\sqrt{2}}.$$

$$S = -\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} = -\frac{4}{\sqrt{2}} = -2\sqrt{2}.$$

So $|S| = 2\sqrt{2}$, the Tsirelson bound. The sign of $S$ depends on the Bell state; the magnitude of the maximum is the same for all four Bell states.

**The trap.** Suppose instead everyone measures in the same direction — $\theta_{A_1} = \theta_{A_2} = \theta_{B_1} = \theta_{B_2} = 0°$. For the singlet all four correlations equal $-1$, so $S = -1 - 1 - (-1) - 1 = -2$: exactly at the classical bound, no violation. The violation is a property of the relative angles, not of any single correlation. A large individual correlation (say $E = 1$, perfect correlation) is easily explained by a classical hidden-variable model — it is the combination of four correlations at four different angles that cannot be explained classically. Students who look at one large correlation and conclude "Bell violation" are making this mistake.

---

## LLM Exercises

### Part 1 — Update PROJECT.md

```
Append a new entry to PROJECT.md:

Chapter 3 — Bell's Theorem and the CHSH Inequality
Deliverable: 03-bell-chsh.html
Status: in progress

The simulation has two panels in one HTML file.

Panel A — CHSH Bell-inequality simulator (700 x 600 SVG).
- State selector: radio buttons for |Phi+>, |Phi->, |Psi+>, |Psi->,
  |00> (product), and "classical mixture (1/2|00><00| + 1/2|11><11|)".
- Four angle sliders: theta_A1, theta_A2, theta_B1, theta_B2,
  range 0 to 360 degrees, step 0.5.
- 2x2 correlation display: E(A1,B1), E(A1,B2), E(A2,B1), E(A2,B2),
  each shown numerically and as a color-coded cell.
- Large S display (~48 pt font). Background flips to amber (#FFC107)
  when |S| > 2. Display also shows |S| > 2sqrt(2) warning in red
  (should never trigger for quantum states — if it does, flag a bug).
- Sub-panel (700 x 200): S vs (theta_A1 - theta_B1) with the other
  three angles held fixed. Red line at y = 2 (CHSH bound). Gold
  dashed line at y = 2*sqrt(2) (Tsirelson bound).
- Snap-to-canonical button: sets angles to 0, 90, 45, -45 with one click.

Panel B — Experimental timeline (700 x 300).
- A horizontal timeline from 1935 (EPR) to 2025.
- Labeled events: EPR 1935, Bell 1964, Freedman-Clauser 1972,
  Aspect 1982, Hensen/Giustina/Shalm 2015, Nobel 2022.
- Clicking each event pops up a tooltip with one-sentence description.
- Nobel Prize glows gold.
```

### Part 2 — Physics rules for CLAUDE.md

```
Append to CLAUDE.md:

BELL/CHSH PHYSICS RULES

1. Two-qubit states are 4-vectors [c_00, c_01, c_10, c_11] (complex).
   Normalize after every operation; warn if |norm-1| > 1e-4.

2. For Bell states, use exact values:
   |Phi+>: [1, 0, 0, 1] / sqrt(2)
   |Phi->: [1, 0, 0,-1] / sqrt(2)
   |Psi+>: [0, 1, 1, 0] / sqrt(2)
   |Psi->: [0, 1,-1, 0] / sqrt(2)

3. Correlation for state |psi> with Alice at theta_A and Bob at theta_B
   (angles in radians, measured from z-axis in the xz-plane):
     sigma_A = sin(theta_A)*sigma_x + cos(theta_A)*sigma_z  (2x2)
     sigma_B = sin(theta_B)*sigma_x + cos(theta_B)*sigma_z  (2x2)
     M = kron(sigma_A, sigma_B)  (4x4)
     E(A, B) = Re(psi_dag * M * psi)
   Pauli matrices: sigma_x = [[0,1],[1,0]], sigma_z = [[1,0],[0,-1]].

4. CHSH parameter: S = E(A1,B1) + E(A1,B2) + E(A2,B1) - E(A2,B2).

5. For "classical mixture" state rho = 0.5|00><00| + 0.5|11><11|:
   E(A,B) = 0.5*Tr(M * |00><00|) + 0.5*Tr(M * |11><11|).
   This state cannot violate |S| > 2. Flag if it appears to.

6. Display S to three decimal places. The Tsirelson bound 2*sqrt(2) = 2.8284...
   Draw a gold dashed line at this value in the sub-panel.

KNOWN FAILURE MODES:
(a) Phase conventions differ between Alice/Bob axes. Use sin*sigma_x + cos*sigma_z
    everywhere, no exceptions.
(b) Classical mixture misimplemented as pure state. Use density-matrix
    expectation value Tr(rho * M), not psi-dag * M * psi.
(c) Angle in degrees sent to trig functions expecting radians.
    Always convert: theta_rad = theta_deg * Math.PI / 180.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md and PROJECT.md.
Read both files first.

Build 03-bell-chsh.html: a single self-contained HTML file using D3 v7
from CDN, no other dependencies, implementing the Chapter 3 Bell/CHSH
simulation as specified in PROJECT.md, following the physics rules in
CLAUDE.md.

Two stacked SVG panels.

PANEL A — CHSH simulator (700 x 600):
- State selector (radio buttons, top row).
- Four angle sliders (theta_A1, theta_A2, theta_B1, theta_B2), each 0-360 deg.
- A 2x2 grid of small labeled correlation readouts, each showing the
  numerical value of E(Ai, Bj) and a color bar from blue (-1) to red (+1).
- A large central S display. Background: white when |S| <= 2, amber
  (#FFC107) when |S| > 2.
- "Snap to optimal (|Phi+>)" button that sets angles to 0/90/45/-45.
- Sub-panel below (700 x 200): line chart of S vs delta_theta =
  (theta_A1 - theta_B1) from -180 to +180 deg, with the other three
  angles held at their current slider values. Horizontal lines: red
  at y=2 (labeled "CHSH bound"), gold dashed at y=2.828 (labeled "Tsirelson").

PANEL B — Timeline (700 x 300):
- Horizontal axis 1935 to 2030. Scale with D3 linear.
- Labeled points: EPR (1935), Bell's theorem (1964), Freedman-Clauser (1972),
  Aspect locality test (1982), 2015 loophole-free (three overlapping dots),
  Nobel Prize (2022, gold star).
- Click events show tooltip with one-sentence description.

Default state on load: |Phi+> selected, angles at 0/90/45/-45.
S should display 2.828 and background should be amber.

Runtime checks (console.log):
- For |Phi+> at optimal angles, S must be within 0.001 of 2.828.
- For |00> at any angles, S must remain in [-2, 2].
- For classical mixture at any angles, S must remain in [-2, 2].
```

### Part 4 — Exploration tasks

**Task 1: The violation.** Load with $|\Phi^+\rangle$ and snap-to-optimal angles $(0°, 90°, 45°, -45°)$. Read $S$. Background turns amber; $S = 2.828$.

**Task 2: Product states cannot violate.** Switch to $|00\rangle$. Try every angle combination. Can you push $|S|$ above 2? Write one sentence connecting your answer to the CHSH derivation.

**Task 3: Classical correlation vs. quantum entanglement.** Switch to "classical mixture." The measured outcomes are perfectly correlated in the $z$-basis: whenever Alice gets $+1$, so does Bob. Try to violate the bound. What does this demonstrate about the difference between classical correlation and quantum entanglement?

**Task 4: Sweeping angles.** Return to $|\Phi^+\rangle$. Fix $\theta_{A_2} = 90°$, $\theta_{B_1} = 45°$, $\theta_{B_2} = -45°$ and sweep $\theta_{A_1}$ from $0°$ to $360°$. Watch the sub-panel. Where does $S$ reach its maximum? Where does it cross zero?

**Task 5: The singlet.** Try $|\Psi^-\rangle$. What angles maximize $|S|$ for this state? Is the maximum value still $2\sqrt{2}$?

**Extension prompt:**

```
Modify 03-bell-chsh.html to add a third panel: a "local hidden variable
machine" that runs trials.

- The user sets the number of trials (slider: 10 to 10,000).
- For each trial, the machine samples a hidden variable lambda uniformly
  from [0, 2*pi), then computes A1 = sign(cos(lambda)), A2 = sign(cos(lambda + phi_A)),
  B1 = sign(cos(lambda + phi_B)), B2 = sign(cos(lambda + phi_A + phi_B))
  where phi_A and phi_B are user-adjustable.
- It accumulates the empirical S from these trials.
- Display: histogram of single-trial S(lambda) values (always ±2);
  running average of S (converging to some value in [-2, 2]);
  side-by-side comparison of the LHV-model S against the quantum S
  for the same angles.
- Demonstrate: no choice of phi_A, phi_B can make the LHV machine
  produce |S| > 2.
```

---

## Still Puzzling

The Tsirelson bound $|S| \leq 2\sqrt{2}$ sits at a peculiar position. The local-realistic bound is 2. The no-signaling maximum is 4. Quantum mechanics stops at $2\sqrt{2}$. Why exactly there?

Information causality provides a candidate answer: $2\sqrt{2}$ is the unique value consistent with the principle that $n$ classical bits cannot convey more than $n$ bits of information regardless of shared correlations. But information causality is an axiom in that argument, not derived from anything more primitive. The chain of justification eventually ends at a principle we cannot reduce further.

A second puzzle: the Delft experiment (Hensen et al.) performed 245 trials before publication. The $p$-value was $0.039$ — statistically significant but not overwhelming by the standards of, say, particle physics (which demands $5\sigma$). A subsequent run extended to 2,078 trials and achieved combined $S = 2.38 \pm 0.14$. This illustrates a genuine tension: fully loophole-free experiments with spin qubits produce events very slowly (each NV-to-NV entanglement attempt succeeds with low probability), while photon experiments with high statistics still struggle with the detection efficiency threshold. The "perfect" experiment — high statistics, high efficiency, large spacelike separation, genuine randomness in setting choice — remains an ongoing engineering challenge.

And the deepest puzzle is interpretational. Bell's theorem forces you to give up one of three reasonable-sounding assumptions (locality, realism, uniqueness of outcomes), but it does not tell you which. Sixty years of experiment have closed the empirical question. The conceptual question — what the result means — remains in genuinely contested territory.

---

## Exercises

**Warm-up**

1. *[CHSH algebra — the key step]* Write out all four possible assignments of $(B_1, B_2)$. For each, with $A_1 = A_2 = +1$, compute $S(\lambda) = A_1[B_1 + B_2] + A_2[B_1 - B_2]$ and verify $|S(\lambda)| = 2$ in every case. Repeat with $A_1 = +1$, $A_2 = -1$.
*What this tests: internalizing the one arithmetic observation that makes the entire inequality — that for ±1 values, exactly one of $|B_1+B_2|$ and $|B_1-B_2|$ equals 2 and the other equals 0.*

2. *[Correlation formula for $|\Phi^+\rangle$]* For $|\Phi^+\rangle$ with $\theta_{A_1} = 30°$ and $\theta_{B_1} = 75°$, compute $E(A_1, B_1)$. What is $E$ when Alice and Bob measure in the same direction? In anti-parallel directions?
*What this tests: applying the quantum correlation formula and identifying its extreme values.*

3. *[CHSH at suboptimal angles]* For $|\Phi^+\rangle$ with $\theta_{A_1} = 0°$, $\theta_{A_2} = 60°$, $\theta_{B_1} = 30°$, $\theta_{B_2} = 90°$: compute all four $E(A_i, B_j)$ and evaluate $S$. Is this optimal? Does it violate the classical bound?
*What this tests: working through a non-optimal angle choice to see that violation is real but sensitive to angle selection.*

**Application**

4. *[No-signaling]* Alice and Bob share $|\Phi^+\rangle$. Alice applies the Pauli $X$ gate to her qubit and measures in the $z$-basis. (a) What is the two-qubit state after Alice applies $X$? (b) Compute Bob's reduced density matrix $\hat{\rho}_B = \mathrm{Tr}_A(\rho_{AB})$ before and after Alice's operation. (c) Does Alice's operation change Bob's local statistics?
*What this tests: demonstrating the no-signaling property by explicit density-matrix computation.*

5. *[Product states and local realism]* For the product state $|+\rangle\otimes|+\rangle$, show that the expectation value of $(\hat{a}\cdot\vec{\sigma})\otimes(\hat{b}\cdot\vec{\sigma})$ factorizes as $\langle\hat{a}\cdot\vec{\sigma}\rangle\langle\hat{b}\cdot\vec{\sigma}\rangle$. Use this to argue that no product state can violate the CHSH inequality.
*What this tests: connecting the factorization of a product state to the hidden-variable structure — a product state already "is" a local model.*

6. *[Bell state preparation]* Starting from $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$, apply $H\otimes I$ followed by CNOT(control=0, target=1). Identify which Bell state is produced in each case and write the pattern.
*What this tests: circuit-level manipulation of Bell states; connecting gate operations to the entangled states that appear throughout this chapter.*

**Synthesis**

7. *[Experimental critique]* You are designing a Bell-test experiment with entangled photons. Your detectors have efficiency $\eta = 0.75$ (75%). Your data appear to show $S = 2.3$. Write a one-paragraph critique as if you are a skeptical local realist: which loophole applies, and what minimum efficiency would close it?
*What this tests: connecting the loophole structure to the experimental numbers; understanding what "fair sampling" requires.*

8. *[Information causality]* State, in your own words, what a Popescu–Rohrlich box would do, why it does not violate no-signaling, and why Pawlowski et al. argue it is still physically unreasonable. What does this suggest about the status of information causality as a physical principle — is it a theorem or an axiom?
*What this tests: engaging with the open question of why quantum correlations stop at $2\sqrt{2}$ rather than at the no-signaling limit.*

**Challenge**

9. *[Tsirelson bound — operator algebra]* For two-qubit operators with $A_1^2 = A_2^2 = B_1^2 = B_2^2 = I$ and $\{A_1, A_2\} = \{B_1, B_2\} = 0$ (anti-commuting on each side): (a) write the operator $S^{\text{op}} = A_1\otimes(B_1 + B_2) + A_2\otimes(B_1 - B_2)$ and compute $(S^{\text{op}})^2$ explicitly; (b) show $(S^{\text{op}})^2 \leq 8\,\mathbf{I}$, so the operator norm $\|S^{\text{op}}\| \leq 2\sqrt{2}$; (c) find a state and operators that saturate this bound and verify $\langle S^{\text{op}}\rangle = 2\sqrt{2}$.
*What this tests: the operator-algebraic proof of the Tsirelson bound — moving beyond the correlation formula to the underlying operator structure.*

---

## References

Bell, J. S. (1964). On the Einstein–Podolsky–Rosen paradox. *Physics*, 1, 195–200.

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, 23, 880–884.

Freedman, S. J., & Clauser, J. F. (1972). Experimental test of local hidden-variable theories. *Physical Review Letters*, 28, 938–941.

Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters*, 49, 1804–1807.

Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics*, 4, 93–100.

Hensen, B. et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature*, 526, 682–686.

Giustina, M. et al. (2015). Significant-loophole-free test of Bell's theorem with entangled photons. *Physical Review Letters*, 115, 250401.

Shalm, L. K. et al. (2015). Strong loophole-free test of local realism. *Physical Review Letters*, 115, 250402.

Pawlowski, M. et al. (2009). Information causality as a physical principle. *Nature*, 461, 1101–1104.

Yin, J. et al. (2017). Satellite-based entanglement distribution over 1200 kilometers. *Science*, 356, 1140–1144.

Nadlinger, D. P. et al. (2022). Experimental quantum key distribution certified by Bell's theorem. *Nature*, 607, 682–686.

Larsson, J.-Å. (2014). Loopholes in Bell inequality tests of local realism. *Journal of Physics A*, 47, 424003.

Nobel Committee for Physics (2022). Scientific Background: Entangled States — from Theory to Technology. nobelprize.org/prizes/physics/2022.

---

## Running Project — Reconstruct a Real Research Result

**This chapter adds:** the **central reconstruction tool for the Bell-test doorway** — computing the CHSH parameter $S$ from first principles for the four measurement angles, comparing your $S$ to the paper's reported value, and reading the gap to $2\sqrt2$ as the signature of real-world imperfection. If your paper is a loophole-free Bell test, this chapter computes its central number. If it is a QEC or sensing paper, this is still the cleanest worked example of "reconstruct means check."

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Evaluating the four correlators $E(A_i,B_j)$ and summing them into $S$ for given angles — *Why AI works here:* trigonometry you check against the analytic optimum $S = 2\sqrt2 \approx 2.828$.
- Generating a small sweep of $S$ vs. one angle to locate the maximum — *Why AI works here:* a plotting/scaffolding task validated by the known optimal angles $(0°,90°,45°,-45°)$.
**The tell:** You are using AI well when you have the Tsirelson bound and the classical bound as guardrails — any $|S| > 2\sqrt2$ from a quantum state is a bug, and any $|S| \le 2$ is no violation.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding whether your reconstructed $S$ "agrees with" the paper — *Why AI fails here:* agreement is a statistical judgment involving the paper's error bars and the gap between the ideal $2\sqrt2$ and the experimental value; an LLM will call a $2.828$-vs-$2.42$ comparison "consistent" or "inconsistent" with equal confidence and no statistical basis.
- Judging whether the paper's $S$ actually closes the loopholes it claims — *Why AI fails here:* it requires reading the detector efficiency and spacelike-separation details, which the model cannot verify and is prone to overstate.
- Assessing whether a marginal violation ($p = 0.039$, $n = 245$, as in Hensen 2015) is "strong evidence" — *Why AI fails here:* statistical-strength calls (triage Step 6) need the physics literacy this volume builds; the AI cannot be trusted to flag an overstated claim.
**The tell:** If you could not state why your $S$ does or does not match the paper — with reference to error bars and the ideal-vs-real gap — without the AI, it did the judgment that should have been yours.
**Physics-judgment connection:** This trains checking a computed correlation against two hard theoretical bounds (classical $|S|\le2$, Tsirelson $|S|\le2\sqrt2$) and against the paper's *measured* value with its uncertainty — the core "reconstruct means check" discipline.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** your first-principles CHSH value $S$ for your paper's (or the canonical) measurement angles, placed next to the paper's reported $S$ — the first row of your reconstruction dossier.
**Tool:** Claude chat.
**The Prompt:**
```
I am reconstructing the central claim of a loophole-free Bell test. My resource
state is [PASTE from Chapter 2: the Bell state and its correlation function,
e.g. "|Phi+>, E(theta_a,theta_b) = cos(theta_a - theta_b)"].

1. Using S = E(A1,B1) + E(A1,B2) + E(A2,B1) - E(A2,B2), compute S for the
   measurement angles theta_A1=0, theta_A2=90, theta_B1=45, theta_B2=-45 degrees.
   Show each of the four correlators, then the sum. Convert degrees to radians
   explicitly.
2. Confirm S = 2*sqrt(2) ~ 2.828 and state the classical bound (2) and the
   Tsirelson bound (2*sqrt(2)) for comparison.
3. Now compute S for these specific angles instead: [PASTE your paper's reported
   measurement settings if it gives them; otherwise keep the canonical ones].
4. The paper reports S_exp = [PASTE the paper's value with its error bar, e.g.
   2.42 +/- 0.20]. State the gap between my ideal S and S_exp, and list the
   physical effects (detection inefficiency, decoherence, photon loss) that push
   the experimental value below the ideal 2*sqrt(2). DO NOT judge whether the
   numbers "agree" statistically — just report both numbers and the gap.
Show all trig. Flag if any correlator falls outside [-1, 1] (that would be a bug).
```
**What this produces:** your reconstructed $S$, the canonical $2\sqrt2$ check, and a side-by-side of ideal $S$ vs. reported $S_\text{exp}$ with the imperfection sources named — the dossier's headline comparison.
**How to adapt:** *Your system:* substitute the singlet's $-\cos$ form and the singlet-optimal angles if your paper uses spins. *ChatGPT/Gemini:* run the same prompt; any disagreement in $S$ traces to a degrees/radians or sign slip. *Claude Project:* append to your dossier file as the "core calculation" entry.
**Builds on:** Chapter 2's identified Bell state and signed correlation function.  **Next:** Chapter 4 builds the circuit that actually prepares and measures this state; Chapter 6 derives the decoherence that produces the ideal-vs-real gap you just observed.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** a tested `chsh.py` in your dossier that computes $S$ for arbitrary angles and states, and reproduces the canonical $2\sqrt2$.
**Tool:** Claude Code.
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `reconstruction-dossier/` with `entanglement.py` (Chapter 2) present.
- [ ] Claude Code installed.
- [ ] Add to `CLAUDE.md`: "Every correlator E(a,b) must lie in [-1,1]; every S from a quantum state must satisfy |S| <= 2*sqrt(2). Assert both. The classical bound is |S| <= 2."
**The Task:**
```
In reconstruction-dossier/:

1. Add chsh.py with:
   - correlator(state, theta_a, theta_b): build sigma_a = sin(theta_a)*X +
     cos(theta_a)*Z and sigma_b likewise (angles in radians, from z-axis), form
     M = kron(sigma_a, sigma_b), and return Re(<state| M |state>) for a length-4
     state vector. Assert the result is in [-1, 1].
   - chsh_S(state, a1, a2, b1, b2): return E(a1,b1)+E(a1,b2)+E(a2,b1)-E(a2,b2).
     Assert |S| <= 2*sqrt(2) + 1e-9.
2. __main__: for |Phi+> at angles (0,90,45,-45) deg, print S and assert it equals
   2*sqrt(2) within 1e-6. Then print S for the |00> product state at the same
   angles and assert |S| <= 2.
3. Add a function fit_eps(S_exp): solve (1-eps)*2*sqrt(2) = S_exp for eps and
   return it (this links to Chapter 1's rho(eps)). Print eps for S_exp =
   [PASTE your paper's reported S].
4. Run it, paste output. Do not modify earlier files.

Stop once the canonical S = 2.828 assertion passes.
```
**Expected output:** `chsh.py`, console lines showing $S = 2.828$ for $|\Phi^+\rangle$, $|S|\le2$ for the product state, and the fitted $\epsilon$ corresponding to your paper's $S_\text{exp}$.
**What to inspect:** the canonical assertion passes to $10^{-6}$; the product-state $S$ never exceeds 2; the fitted $\epsilon = 1 - S_\text{exp}/2\sqrt2$ is in $[0,1]$ and reasonable for a high-quality source.
**If it goes wrong:** the most common failure is angles passed in degrees to `sin`/`cos` (expecting radians), yielding nonsense $S$ — confirm an explicit `radians()` conversion before the trig.
**CLAUDE.md / AGENTS.md note:** keep "assert $|S|\le2\sqrt2$ for any quantum state — a violation of Tsirelson is always a code bug, never physics."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the R3/R4 reconstructed CHSH value and the ideal-vs-reported comparison.
**Validation type:** Numerical result + reasoning chain.
**Risk level:** High — this is the dossier's headline number, and the dangerous failure mode is a fluent "the numbers agree" judgment that skips the statistics.
**Setup:** use your R3 output (or R4 console). If you want to force the failure mode, paste this pre-generated (deliberately flawed) snippet for critique: *"With angles 0, 90, 45, -45 degrees the CHSH parameter is S = 3.06, comfortably above the Tsirelson bound, confirming the paper's reported S = 2.42 within error."* — it contains a Tsirelson violation and an unjustified agreement claim.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Bell's Theorem and CHSH
□ Correctness: do the four correlators each lie in [-1,1] and sum to the stated S?
□ Completeness: did it report BOTH the ideal S and the paper's S_exp, not just one?
□ Scope: did it avoid asserting statistical "agreement" without the error bars?
□ Tsirelson check: is |S| <= 2*sqrt(2) = 2.828? (Any value above is a bug.)
□ Classical-bound check: is the violation real (|S| > 2) for the entangled state,
  and |S| <= 2 for the product/classical-mixture state?
□ Gap reasoning: are the imperfection sources (detection efficiency, decoherence)
  named as the reason S_exp < 2*sqrt(2)?
□ Failure-mode check: any of —
  - fluent but wrong (S quoted above Tsirelson, or a degrees/radians error)
  - unjustified "agrees within error" with no use of the reported uncertainty
  - sign error from using the wrong Bell-state correlation function
```
**What to do with findings:** pass → this is the core 30% of your dossier rubric — record it with both numbers and the gap; one fail → fix and re-run; multiple fails or a Tsirelson violation → recompute $S$ by hand from the four cosines, it is four terms.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI computed the four correlators and summed them to $S$ for the measurement angles.
> *2:* The AI could not determine whether my $S$ statistically agrees with the paper's reported value — that required me to weigh the reported error bar and the ideal-vs-real gap myself.
**Physics-judgment connection:** This validation trains the central reconstruction habit — recomputing a paper's headline number from first principles and checking it against two theoretical bounds *and* the paper's measured value with its uncertainty, rather than accepting a fluent agreement claim.

---
