# Chapter 6 — Open Systems: Decoherence and the Lindblad Equation
*The quantum-to-classical transition is not a philosophical event. It is a number in microseconds.*

There is a sentence that appears in nearly every paper on superconducting qubits: "$T_2 = 200\,\mu$s." It sits in the abstract, next to the processor schematic, treated as if the reader knows immediately what it means. By the end of this chapter, you will. More than that, you will be able to derive it — to show where the $200\,\mu$s comes from in the mathematics, what it measures in the density matrix, and why it is the number that determines whether a computation succeeds or fails before it finishes.

$T_2$ is the coherence time. It measures how long the off-diagonal entries of the density matrix survive before they decay to zero. When they reach zero, the qubit has become classical: it is in the ground state or the excited state with some probability, but it is no longer in a quantum superposition. The quantum-to-classical transition is not a philosophical event. It is a number in microseconds, printed in a paper abstract.

To understand $T_2$ you need the equation that governs it. That equation is the Lindblad master equation.

---

## Why Pure States Fail: The System–Environment Split

In every previous chapter, we treated qubits as isolated. The state was pure, evolution was unitary, and that was that. But no qubit is truly isolated. A superconducting transmon couples to substrate phonons, control lines, neighboring qubits, and stray electromagnetic fields. A trapped ion couples to laser phase noise and ambient magnetic fields. A nitrogen-vacancy center in diamond sits in a bath of $^{13}$C nuclear spins. These environments are the dominant noise source.

The formal setup: write the full Hamiltonian as:

$$\hat H_\text{total} = \hat H_S \otimes \hat I_E + \hat I_S \otimes \hat H_E + \hat H_{SE}.$$

The total state $|\Psi(t)\rangle$ of system plus environment evolves unitarily — pure state in, pure state out. The problem is that the environment has $\sim 10^{23}$ degrees of freedom. We cannot and do not want to track all of them.

The **reduced density matrix** is the solution. Trace out the environment:

$$\hat\rho_S(t) = \text{Tr}_E\bigl(|\Psi(t)\rangle\langle\Psi(t)|\bigr).$$

This is the object that gives correct predictions for any measurement on the system alone. The partial trace is not a coarse-graining or an approximation — it is exact. What is approximate is everything we are about to do to find an equation for $\hat\rho_S(t)$.

**Why the result is mixed.** Suppose at $t = 0$ the system is in a pure state $|\psi_0\rangle$ and the environment is in $|e_0\rangle$, so the total state is unentangled. After a short time, $\hat H_{SE}$ couples them:

$$|\Psi(t)\rangle = \alpha|0\rangle|e_0(t)\rangle + \beta|1\rangle|e_1(t)\rangle,$$

where $|e_0(t)\rangle$ and $|e_1(t)\rangle$ are environment branches that have diverged depending on the system state. The reduced density matrix:

$$\hat\rho_S(t) = |\alpha|^2|0\rangle\langle 0| + \alpha\beta^*\langle e_1(t)|e_0(t)\rangle|0\rangle\langle 1| + \alpha^*\beta\langle e_0(t)|e_1(t)\rangle|1\rangle\langle 0| + |\beta|^2|1\rangle\langle 1|.$$

The off-diagonal terms are suppressed by the overlap $\langle e_0(t)|e_1(t)\rangle$. As the environment branches become more orthogonal — as the environment "records" which state the qubit was in — this overlap decays toward zero. When $\langle e_0(t)|e_1(t)\rangle = 0$, the density matrix is diagonal: $|\alpha|^2|0\rangle\langle 0| + |\beta|^2|1\rangle\langle 1|$. A classical probability distribution. Quantum coherence has leaked into the environment and cannot be retrieved.

<!-- → [FIGURE: branching-world diagram showing the total state splitting — the qubit's |0⟩ branch entangled with one environment trajectory and |1⟩ with another, the overlap ⟨e₀|e₁⟩ labeled on a bracket connecting the two branches, showing it approaches zero as the branches diverge] -->

---

## The Bloch Representation

For a single qubit, every density matrix can be written in Bloch form:

$$\hat\rho = \frac{1}{2}\bigl(\hat I + \vec r \cdot \vec\sigma\bigr), \qquad \vec r = (r_x, r_y, r_z), \quad |\vec r| \leq 1.$$

Pure states have $|\vec r| = 1$ and sit on the surface of the Bloch sphere. Mixed states have $|\vec r| < 1$ and sit inside. The maximally mixed state $\hat I/2$ has $\vec r = \vec 0$. Explicitly:

$$\hat\rho = \begin{pmatrix} \frac{1+r_z}{2} & \frac{r_x - ir_y}{2} \\[4pt] \frac{r_x + ir_y}{2} & \frac{1-r_z}{2} \end{pmatrix}.$$

The diagonal entries $\rho_{00}$ and $\rho_{11}$ are the populations. The off-diagonal entry $\rho_{01}$ is the coherence — its magnitude measures how quantum the state is. Decoherence shrinks $|\rho_{01}|$ toward zero. Energy relaxation drives $\rho_{11}$ toward zero. Both move the Bloch vector from the surface toward the interior. Energy relaxation additionally pushes it toward the south pole (the ground state $|0\rangle$).

The von Neumann equation for a closed system — $d\hat\rho/dt = -(i/\hbar)[\hat H, \hat\rho]$ — preserves purity. The Bloch vector stays on the sphere surface and precesses. No dissipation. For an open system this equation is wrong. The right equation must satisfy three properties the von Neumann equation alone cannot guarantee: trace preservation ($\text{Tr}(\hat\rho) = 1$ for all time), Hermiticity, and complete positivity.

Complete positivity is the subtlest requirement. Ordinary positivity requires all eigenvalues of $\hat\rho$ to be non-negative. Complete positivity requires that $(\mathcal{E}\otimes\mathcal{I})(\hat\rho_\text{ext}) \geq 0$ for any extension of the system to a larger Hilbert space — because the system may be entangled with a reference that is not subject to the noise. Maps that fail complete positivity can produce negative probabilities on entangled inputs, which is unphysical.

---

## The Lindblad (GKSL) Master Equation

In 1976, Gorini, Kossakowski, and Sudarshan, and independently Lindblad, proved that the most general Markovian, completely positive, trace-preserving master equation has the form:

$$\boxed{\frac{d\hat\rho}{dt} = -\frac{i}{\hbar}[\hat H, \hat\rho] + \sum_k\left(\hat L_k\hat\rho\hat L_k^\dagger - \frac{1}{2}\bigl\{\hat L_k^\dagger\hat L_k, \hat\rho\bigr\}\right).}$$

The first term is Hamiltonian evolution — unitary, reversible. The second is the **dissipator** $\mathcal{D}[\hat\rho]$, summed over noise channels. Each $\hat L_k$ is a **jump operator** encoding one physical decoherence process.

**Trace preservation, explicitly.** Using cyclicity of trace:

$$\text{Tr}\bigl(\hat L_k\hat\rho\hat L_k^\dagger\bigr) - \frac{1}{2}\text{Tr}\bigl(\hat L_k^\dagger\hat L_k\hat\rho\bigr) - \frac{1}{2}\text{Tr}\bigl(\hat\rho\hat L_k^\dagger\hat L_k\bigr) = \text{Tr}\bigl(\hat L_k^\dagger\hat L_k\hat\rho\bigr) - \text{Tr}\bigl(\hat L_k^\dagger\hat L_k\hat\rho\bigr) = 0.$$

So $d\,\text{Tr}(\hat\rho)/dt = 0$: normalization is preserved exactly.

**The Markovian assumption.** The Lindblad equation assumes the bath has no memory — bath correlation functions decay faster than any system timescale. This is the Born–Markov approximation. For most qubit hardware (superconducting transmons in a cold bath, trapped ions with Markovian laser phase noise), it is an excellent approximation. For structured baths — a photonic crystal cavity, a spin bath with long correlations — it breaks down, and non-Markovian extensions are required.

**The GKSL form is not postulated — it is derived.** Start with the full system–bath Hamiltonian. Move to the interaction picture. Expand to second order in $\hat H_{SE}$ (Born approximation: weak coupling). Trace out the bath. Apply the Markov approximation (bath correlation time $\tau_B \ll T_1, T_2$) and a secular approximation. The result is exactly the GKSL equation, with jump operators and rates determined by the bath spectral density at the system transition frequencies. The key step forcing the anticommutator structure — ensuring complete positivity rather than mere positivity — is the secular approximation applied to a completely positive map.

---

## Deriving the Bloch Equations

Take the qubit Hamiltonian $\hat H = (\hbar\omega_0/2)\hat\sigma_z$ and two jump operators:

**Pure dephasing:** $\hat L_\phi = \sqrt{1/(2T_\phi)}\,\hat\sigma_z$. Random phase kicks from the environment with no energy exchange.

**Energy relaxation:** $\hat L_1 = \sqrt{1/T_1}\,\hat\sigma_- = \sqrt{1/T_1}\,|0\rangle\langle 1|$. The excited state decaying to the ground state by emitting energy.

**The Hamiltonian term.** The commutator $[\hat\sigma_z, \hat\rho]$ acting on the Bloch vector, using $[\hat\sigma_z, \hat\sigma_x] = 2i\hat\sigma_y$ and $[\hat\sigma_z, \hat\sigma_y] = -2i\hat\sigma_x$:

$$\dot r_x^\text{H} = -\omega_0 r_y, \quad \dot r_y^\text{H} = +\omega_0 r_x, \quad \dot r_z^\text{H} = 0.$$

Free precession about $\hat z$ at frequency $\omega_0$. No dissipation.

**The dephasing dissipator.** With $\hat L_\phi = \sqrt{1/2T_\phi}\,\hat\sigma_z$, compute $\hat\sigma_z\hat\rho\hat\sigma_z - \hat\rho$. Using $\hat\sigma_z\hat\sigma_x\hat\sigma_z = -\hat\sigma_x$ and $\hat\sigma_z\hat\sigma_y\hat\sigma_z = -\hat\sigma_y$, the dissipator kills the transverse components and leaves the longitudinal one unchanged:

$$\dot r_x^\phi = -\frac{r_x}{T_\phi}, \qquad \dot r_y^\phi = -\frac{r_y}{T_\phi}, \qquad \dot r_z^\phi = 0.$$

Pure dephasing squeezes the Bloch vector toward the $z$-axis without moving it along it.

**The relaxation dissipator.** Working through $\hat L_1\hat\rho\hat L_1^\dagger - \frac{1}{2}\{\hat L_1^\dagger\hat L_1, \hat\rho\}$ with $\hat\sigma_-\hat\sigma_+ = |0\rangle\langle 0|$ and $\hat\sigma_+\hat\sigma_- = |1\rangle\langle 1|$:

$$\dot r_x^{(1)} = -\frac{r_x}{2T_1}, \qquad \dot r_y^{(1)} = -\frac{r_y}{2T_1}, \qquad \dot r_z^{(1)} = -\frac{r_z + 1}{T_1}.$$

The transverse components decay at *half* the longitudinal rate. This 2:1 ratio is not an approximation — it is automatic from the Lindblad structure of $\hat\sigma_-$.

**Combining all contributions:**

$$\dot r_x = -\omega_0 r_y - \frac{r_x}{T_2}, \qquad \dot r_y = +\omega_0 r_x - \frac{r_y}{T_2}, \qquad \dot r_z = -\frac{r_z - r_z^\text{eq}}{T_1},$$

where $r_z^\text{eq} = -1$ (the ground state at the south pole) and:

$$\boxed{\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}.}$$

These are the **Bloch equations**. They are the chapter's central result: the density-matrix analog of Newton's law for a decohering qubit.

<!-- → [DIAGRAM: annotated Bloch sphere showing three processes simultaneously — precession around z at ω₀ (orange circular arrow), transverse shrinkage at rate 1/T₂ (inward arrow toward z-axis), and longitudinal decay toward south pole at rate 1/T₁ (arrow along z toward |0⟩)] -->

**The constraint $T_2 \leq 2T_1$.** Since $1/T_\phi \geq 0$, we have $1/T_2 = 1/(2T_1) + 1/T_\phi \geq 1/(2T_1)$, hence $T_2 \leq 2T_1$. Equality $T_2 = 2T_1$ — the **natural linewidth limit** — is achieved when $T_\phi \to \infty$: no pure dephasing, only energy relaxation. Real hardware always has some pure dephasing. Coherence is always at least as fragile as population.

---

## Pointer States and Einselection

Why does a qubit that started in superposition $\alpha|0\rangle + \beta|1\rangle$ decohere in the $\{|0\rangle, |1\rangle\}$ basis rather than some other basis? The answer is the coupling Hamiltonian $\hat H_{SE}$.

Zurek introduced the concept of **pointer states**: the states of the system least disturbed by entanglement with the environment. They are the eigenstates of the system–environment coupling. For a qubit dephasing via $\hat L_\phi \propto \hat\sigma_z$, the coupling commutes with $\hat\sigma_z$, so the eigenstates of $\hat\sigma_z$ — that is, $|0\rangle$ and $|1\rangle$ — are the pointer states. The environment continuously monitors $\sigma_z$. Eigenstates of $\sigma_z$ are stable under this monitoring. Superpositions are not: they rapidly entangle with the environment and decohere into a mixture of pointer states.

This is **einselection** — environment-induced superselection. The environment selects a preferred basis by destroying coherences between non-pointer states. The result looks classical: a probability distribution over $\{|0\rangle, |1\rangle\}$, not a superposition.

What decoherence explains: why off-diagonal coherences vanish in the pointer basis; why macroscopic superpositions are never observed (decoherence times for dust grains in air are $\sim 10^{-36}$ s); why measurement outcomes look classical when the environment records which path was taken.

What the Lindblad equation does not explain: why one particular outcome obtains in a single run; the Born-rule probability interpretation; the subjective experience of a definite outcome. The Lindblad equation gives $\hat\rho \to \text{diagonal in pointer basis}$. The diagonal entries $|\alpha|^2$ and $|\beta|^2$ remain a mixture of two possibilities, not one actual outcome. Decoherence is a necessary part of any explanation of the quantum-to-classical transition. It is not sufficient.

---

## Decoherence Timescales: A Calibration Table

The $T_2 \leq 2T_1$ inequality tells you the structure. The table below tells you the scale. Numbers are representative of the 2025–2026 state of the art and will evolve. The inequalities and mechanisms will not.

<!-- → [TABLE: platform comparison table — columns: Platform, T₁, T₂, T₂/T₁ ratio, Dominant dephasing mechanism — rows: superconducting transmon (100–500 µs, 50–300 µs, 0.3–0.8, flux/charge noise), trapped ions (seconds–minutes, seconds, ≈1, motional heating/magnetic field), NV center (ms, µs–ms, 0.001–0.5, ¹³C nuclear spin bath), semiconductor spin qubit (1–10 ms, 1–100 µs, 0.01–0.1, nuclear spin bath/charge noise), photon polarization (∞, meters, —, loss/mode mismatch)] -->

Trapped ions approach the natural linewidth limit ($T_2 \approx 2T_1$): coherence limited almost entirely by energy relaxation, minimal pure dephasing. Superconducting qubits have $T_2 < 2T_1$ because flux noise from the Josephson junction environment adds significant pure dephasing. NV centers at room temperature are severely dephasing-limited ($T_2 \ll T_1$), but dynamical decoupling sequences — periodic $\pi$ pulses that reverse the qubit's phase — can extend the effective $T_2$ toward $T_1$ by filtering out slow noise.

Students should look up current benchmarks before citing these numbers in a paper. The structure — $T_2 \leq 2T_1$, the dominant noise sources, the platform ranking — is durable. The specific microsecond values are not.

---

## A Worked Calculation: Pure Dephasing

**Setup.** Pure dephasing only: $\hat H = (\hbar\omega_0/2)\hat\sigma_z$, jump operator $\hat L_\phi = \sqrt{1/2T_\phi}\,\hat\sigma_z$, no energy relaxation ($T_1 \to \infty$).

**Initial state.** Qubit on the equator of the Bloch sphere: $r_x(0) = 1$, $r_y(0) = 0$, $r_z(0) = 0$. In matrix form, the pure state $|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$:

$$\hat\rho(0) = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}.$$

**The equations.** Setting $T_1 = \infty$:

$$\dot r_x = -\omega_0 r_y - \frac{r_x}{T_\phi}, \qquad \dot r_y = +\omega_0 r_x - \frac{r_y}{T_\phi}, \qquad \dot r_z = 0.$$

**Solution.** Writing $\tilde r = r_x + ir_y$:

$$\dot{\tilde r} = i\omega_0\tilde r - \frac{\tilde r}{T_\phi} \implies \tilde r(t) = \tilde r(0)\,e^{(i\omega_0 - 1/T_\phi)t}.$$

With $r_x(0) = 1$, $r_y(0) = 0$:

$$r_x(t) = e^{-t/T_\phi}\cos(\omega_0 t), \qquad r_y(t) = e^{-t/T_\phi}\sin(\omega_0 t), \qquad r_z(t) = 0.$$

**The density matrix:**

$$\hat\rho(t) = \frac{1}{2}\begin{pmatrix} 1 & e^{-t/T_\phi}\,e^{-i\omega_0 t} \\[4pt] e^{-t/T_\phi}\,e^{+i\omega_0 t} & 1 \end{pmatrix}.$$

The diagonal entries stay fixed at $1/2$ — populations do not change. The off-diagonal entries oscillate at $\omega_0$ while decaying exponentially as $e^{-t/T_\phi}$.

**Reading the result.** At $t = 0$: $|\rho_{01}| = 1/2$ — maximally coherent, pure state. At $t = T_\phi$: $|\rho_{01}| = e^{-1}/2 \approx 0.18$ — substantially mixed. At $t \gg T_\phi$:

$$\hat\rho(\infty) = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{\hat I}{2}.$$

Maximally mixed. Not to the south pole — this is pure dephasing, not energy relaxation. The qubit has not decayed to the ground state. It has lost all quantum phase information. It is now equally likely to be found in $|0\rangle$ or $|1\rangle$, but in a classical mixture, not a quantum superposition.

**The physical picture.** The environment performs continuous, imperfect measurements of $\hat\sigma_z$. Each interaction slightly entangles the qubit's phase with the bath. The overlap $\langle e_0(t)|e_1(t)\rangle$ between environmental branches decays at rate $1/T_\phi$. The off-diagonals, which measure exactly that overlap, follow.

**Where the calculation breaks.** The derivation assumes the Markov approximation: the bath forgets faster than $T_\phi$. For a $^{13}$C nuclear spin bath with slow spin-spin dynamics, the decay of the off-diagonal is not a single exponential — it can show Gaussian initial decay, non-exponential tails, or partial coherence revivals. The Lindblad equation then fails and non-Markovian equations are required. Dynamical decoupling suppresses slow dephasing noise by periodically flipping the qubit, effectively averaging out low-frequency bath fluctuations. This is how NV centers at room temperature achieve millisecond coherence despite a dense nuclear spin bath.

---

## LLM Exercises

### Part 1 — Update PROJECT.md

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 6 — Open Systems: Decoherence and the Lindblad Equation
Deliverable: 06-decoherence.html
Status: in progress

The simulation has two panels side by side in one HTML file:

Panel A — Bloch sphere visualizer (500 x 500 SVG, left).
- 2D orthographic projection of the unit Bloch sphere:
  equator (grey circle), two meridians (light grey arcs), z-axis
  (thin grey vertical line), south pole labeled |0> and north pole |1>.
- Orange arrow from origin to Bloch vector position (r_x, r_y, r_z).
- Trail: last 300 Bloch vector positions as a fading dotted orange curve
  (opacity proportional to age).
- Small labels for the current (r_x, r_y, r_z) and the purity Tr(rho^2).

Sliders below Panel A:
  T_1: 1 to 5000 natural time units, log scale.
  T_2: 0 to 2*T_1, linear scale (clamped at 2*T_1 — refuse values above).
       Display the inferred T_phi = 1 / (1/T_2 - 1/(2T_1)) next to the slider.
  omega_0: 0 to 5 natural units, linear.
  theta_0: initial polar angle, 0 to pi (default pi/2 = equator).
  phi_0: initial azimuth, 0 to 2 pi (default 0).
  time scrubber: 0 to 10 * max(T_1, 1/omega_0).

Play / Pause button. Reset Trail button.

Panel B — Density matrix bar chart (400 x 400 SVG, right).
- 2x2 grid of bars. Bar heights are |rho_ij| (0 to 0.5 for off-diagonals,
  0 to 1 for diagonals). Bars colored:
    rho_00 (top-left): blue; rho_11 (bottom-right): red.
    rho_01 and rho_10 (off-diagonals): amber, height shrinking in real time.
- Phase of the off-diagonal shown as a small colored arc (HSL hue = phase angle).
- Below the bar chart: time series of |rho_01(t)| for the last 5 T_2 periods,
  plotted as an orange curve against a background exponential e^{-t/T_2}.
  The data and the theoretical envelope should match.
```

### Part 2 — CLAUDE.md amendment

```
Append to CLAUDE.md the following physics rules for Chapter 6 simulations:

OPEN QUANTUM SYSTEMS (BLOCH EQUATIONS) PHYSICS RULES

1. The Bloch vector (r_x, r_y, r_z) must satisfy |r| <= 1 at all times.
   Clamp to 1 and log a warning if rounding pushes above 1.001.

2. Bloch equations (the chapter's central result):
     dot r_x = -omega_0 * r_y - r_x / T_2
     dot r_y = +omega_0 * r_x - r_y / T_2
     dot r_z = -(r_z - r_z_eq) / T_1
   with r_z_eq = -1 (south pole / ground state).

3. The pure dephasing time is DERIVED, not set directly:
     1/T_phi = 1/T_2 - 1/(2*T_1)
   Clamp: T_2 <= 2*T_1 always. If user sets T_2 > 2*T_1, snap to 2*T_1.

4. Integration method: 4th-order Runge–Kutta (RK4).
   Step size: dt = 0.01 * min(T_1, T_2, 1/omega_0 if omega_0 > 0 else T_1).
   Animate at 60 fps with requestAnimationFrame.

5. Density matrix from Bloch vector:
     rho[0][0] = (1 + r_z) / 2
     rho[1][1] = (1 - r_z) / 2
     rho[0][1] = (r_x - i*r_y) / 2   (complex)
     rho[1][0] = conj(rho[0][1])

6. Purity: Tr(rho^2) = (1 + |r|^2) / 2. Should equal 1 for |r| = 1
   and 0.5 for |r| = 0 (maximally mixed).

7. Bloch sphere rendering: orthographic projection onto the page.
   Project 3D point (x, y, z) to 2D screen as (cx + scale*x, cy - scale*z)
   (dropping the y depth dimension for simplicity, or use a slight
   isometric tilt). Orange arrow from (cx, cy) to the projected point.

8. Off-diagonal time series: compute |rho[0][1]| = |r_x - i*r_y| / 2
   at each time step. Store the last 5*T_2 worth of samples. The
   theoretical envelope is 0.5 * exp(-t/T_2). If the simulated curve
   deviates from the envelope by more than 5%, flag a numerical bug.

KNOWN FAILURE MODES:
(a) T_2 > 2*T_1 accepted without clamping. Check on every slider event.
(b) r_z equilibrium set to +1 (north pole) instead of -1 (south pole).
    The ground state is |0>, which is at the SOUTH pole in the
    convention where |0> = (1 0)^T and sigma_z eigenvalue +1 is the
    north pole. Double-check: at t -> infinity with T_1 finite, r_z -> -1.
(c) Trail not cleared on reset. Clear the trail array on every "Reset"
    button click.
(d) Phase of off-diagonal drawn incorrectly: phase of rho[0][1] is
    arg(r_x - i*r_y) = atan2(-r_y, r_x), not atan2(r_y, r_x).
(e) RK4 step too large: if omega_0 is large (fast precession), the
    step must resolve the oscillation. Use dt < 0.1 / omega_0.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 06-decoherence.html: a single self-contained HTML file using
D3 v7 from a CDN, no other dependencies, implementing the Chapter 6
simulation as specified in PROJECT.md, following the physics rules in
CLAUDE.md and the visual constitution in DESIGN.md.

The page has a header ("Chapter 6 — Qubit Decoherence Visualizer") and
two panels side by side in a flex row: Panel A (Bloch sphere) on the
left, Panel B (density matrix bar chart) on the right.

PANEL A — Bloch sphere (500 x 500 SVG).

Render:
- Grey wireframe sphere: equator (full circle), two meridians (half
  circles for x-z and y-z planes). Use thin strokes, opacity 0.4.
- Z-axis vertical line: label |0> at south pole (bottom), |1> at
  north pole (top).
- Bloch vector: thick orange arrow from SVG center to projected position.
- Trail: last 300 vector tips as small orange dots fading from 0.8 to
  0.05 opacity by age.
- Text overlay (top-right of panel): "rx = ..., ry = ..., rz = ..."
  and "Purity = ..." updating at each animation frame.

Below Panel A, six sliders with live numeric labels:
  T_1 (log scale, 1 to 5000), T_2 (linear, 0 to 2*T_1 clamped),
  omega_0 (0 to 5), theta_0 (0 to pi), phi_0 (0 to 2 pi), time scrubber.

Below sliders: small text showing inferred T_phi = ... and the current
time t = ... in natural units.

Play / Pause button. Reset button (resets to initial position, clears trail,
resets time to 0 but keeps slider values).

PANEL B — Density matrix (400 x 400 SVG).

2x2 bar chart. Four bars labeled rho_00 (blue), rho_01 (amber), rho_10
(amber), rho_11 (red). Heights proportional to |rho_ij|, scaled so
max height = 200 px at |value| = 0.5 for off-diagonals and |value| = 1
for diagonals.

A small colored arc (radius 18 px) below each off-diagonal bar shows
the phase of rho_01 as a clockface indicator — the arc sweeps from 0 to
the current phase angle arg(rho_01), colored by HSL hue = 180 * phase/pi.

Below the 2x2 grid: a time series plot (380 x 150 SVG inline) showing:
- Orange line: |rho_01(t)| from the simulation.
- Grey dashed line: 0.5 * exp(-t/T_2) (theoretical envelope).
- X-axis: time from 0 to 5*T_2. Y-axis: 0 to 0.5.
- Update as the simulation runs; scroll the window left as time advances.

Runtime sanity checks (write to console every 10 frames):
- |r|^2 <= 1 + 1e-4.
- Purity = (1 + |r|^2) / 2 within 1e-5 of computed Tr(rho^2).
- At t = T_2, |rho_01| should be 0.5/e ~ 0.184 within 3%.
- At t >> 3*T_1, r_z should be within 0.01 of r_z_eq = -1.
- If omega_0 = 0 and T_1 = infinity, r_z should be constant;
  if this drifts by more than 1e-4, flag a numerical bug.

Do NOT use any 3D library. Orthographic projection only.
Do NOT use math.js. RK4 in vanilla JS. Comments at every physics step.
```

### Part 4 — Exploration tasks

**Task 1: Pure dephasing.** Set $T_1$ to maximum, $T_2 = 100$ (natural units), $\omega_0 = 2$, start on the equator. Play. The Bloch vector should trace a spiral that flattens onto the $z$-axis. Watch the off-diagonal bars in Panel B decay. At $t = T_2$, what fraction of the initial off-diagonal remains? Expected: $e^{-1} \approx 0.37$.

**Task 2: Combined decoherence.** Set $T_1 = T_2 = 100$, $\omega_0 = 2$. The spiral should now converge to the south pole, not the $z$-axis. Observe that the diagonal bars in Panel B evolve (population decays) and the off-diagonals decay simultaneously. Compare the timescale of diagonal evolution ($T_1$) to the off-diagonal decay ($T_2$).

**Task 3: The constraint.** Try to set $T_2 = 300$ with $T_1 = 100$. The slider should refuse, snapping to $T_2 = 200$. Verify: $T_2 = 200 = 2T_1$. Read the displayed $T_\phi$ — it should be $\infty$ (no pure dephasing): this is the natural linewidth limit.

**Task 4: Pole vs. equator.** Set $T_2 = T_1 = 200$, $\omega_0 = 0$, start at the north pole ($\theta_0 = 0$). Only $r_z$ evolves — decaying exponentially to $-1$ at rate $1/T_1$. Off-diagonals are always zero (polar state has no coherence). Move to the equator ($\theta_0 = \pi/2$): off-diagonals become nonzero and decay at rate $1/T_2$.

**Task 5: Numerical verification.** At $t = T_2$, record $|\rho_{01}|$ from Panel B and compare to the theoretical value $|\rho_{01}(T_2)| = e^{-1}/2 \approx 0.184$. If the simulation deviates by more than 5%, there is a numerical bug.

---

## Still Puzzling

The Lindblad equation is derived under the Born–Markov approximation: weak coupling, and bath correlation functions that decay faster than any system timescale. Both are quantitative, not exact.

For a photon in a photonic crystal cavity, the bath has a structured density of states: the photon may emit and then reabsorb before the cavity forgets. The dynamics are non-Markovian — the density matrix does not evolve by a Lindblad equation, and the trajectory can show partial coherence revivals that would be impossible in GKSL evolution. For a spin bath like the $^{13}$C nuclei around an NV center, slow spin-spin correlations persist on timescales comparable to $T_2$, making off-diagonal decay non-exponential.

The active research area is finding tractable alternatives to GKSL for these cases. The Nakajima-Zwanzig equation is formally exact but intractable in general. Time-convolutionless master equations are a working compromise. Neither is as clean as the Lindblad equation, and neither delivers the same intuition. The Lindblad equation earns its place as the standard tool not because it is always right, but because it is right under conditions that are well-defined, widely applicable, and physically interpretable. Knowing when to trust it — and when to look for non-exponential decay or coherence revivals — is the practical judgment this chapter is building.

---

## Exercises

**Warm-up**

1. *[Partial trace; mixed state from entanglement]* Consider the two-qubit pure state $|\Psi\rangle = \alpha|00\rangle + \beta|11\rangle$ with $|\alpha|^2 + |\beta|^2 = 1$. Compute the reduced density matrix $\hat\rho_S = \text{Tr}_E(|\Psi\rangle\langle\Psi|)$ by tracing over the second qubit. When is $\hat\rho_S$ a pure state? When is it most mixed?
*What this tests: working through the partial trace explicitly and seeing that entanglement produces mixedness.*

2. *[Trace preservation of the Lindblad dissipator]* Verify explicitly that $\text{Tr}(\mathcal{D}[\hat\rho]) = 0$ for a single jump operator $\hat L$, where $\mathcal{D}[\hat\rho] = \hat L\hat\rho\hat L^\dagger - \frac{1}{2}\{\hat L^\dagger\hat L, \hat\rho\}$. Use cyclicity of trace.
*What this tests: the algebraic check that the Lindblad form preserves normalization — and understanding why the anticommutator structure is necessary for this.*

3. *[Bloch vector extraction; purity]* A qubit has density matrix $\hat\rho = \begin{pmatrix}0.7 & 0.3 \\ 0.3 & 0.3\end{pmatrix}$. (a) Find the Bloch vector $(r_x, r_y, r_z)$. (b) Compute the purity $\text{Tr}(\hat\rho^2)$. (c) Is this a valid density matrix?
*What this tests: reading physical information out of a density matrix and checking validity conditions.*

**Application**

4. *[Bloch equation derivation for dephasing]* Starting from the Lindblad equation with $\hat L_\phi = \sqrt{1/2T_\phi}\hat\sigma_z$ and $\hat H = 0$, derive $\dot r_x$ by computing $d\,\text{Tr}(\hat\rho\hat\sigma_x)/dt$ from the dissipator. Show all intermediate algebra.
*What this tests: deriving a Bloch equation term from the Lindblad structure rather than just reading it off.*

5. *[Bloch equation solution with combined noise]* A qubit starts on the equator: $(r_x, r_y, r_z) = (1, 0, 0)$. It evolves with $\omega_0 = 0$, $T_1 = 4\,\mu$s, $T_\phi = 4\,\mu$s (so $T_2 = 2\,\mu$s by the sum formula). (a) Write the full solution $(r_x(t), r_y(t), r_z(t))$. (b) Compute the purity at $t = T_2$. (c) Where is the Bloch vector at $t \to \infty$ — the origin or the south pole? Explain physically.
*What this tests: solving the Bloch equations with both $T_1$ and $T_\phi$ active; distinguishing the limiting state of pure dephasing from energy relaxation.*

6. *[$T_1$–$T_2$ constraint and hardware numbers]* A transmon qubit has $T_1 = 300\,\mu$s. (a) What is the maximum possible $T_2$? (b) If the measured $T_2 = 180\,\mu$s, compute $T_\phi$. (c) If a noise-mitigation technique doubles $T_\phi$, what is the new $T_2$?
*What this tests: using the sum formula to infer $T_\phi$ from measured $T_1$ and $T_2$, and predicting the effect of improvements.*

**Synthesis**

7. *[Relaxation dissipator derivation]* For $\hat L_1 = \sqrt{1/T_1}\hat\sigma_-$, derive the three Bloch equations $\dot r_x^{(1)}, \dot r_y^{(1)}, \dot r_z^{(1)}$ from the dissipator $\hat L_1\hat\rho\hat L_1^\dagger - \frac{1}{2}\{\hat L_1^\dagger\hat L_1, \hat\rho\}$. Show that $\hat\sigma_+\hat\sigma_- = |1\rangle\langle 1|$ and $\hat\sigma_-\hat\sigma_+ = |0\rangle\langle 0|$, and use the Bloch representation explicitly at each step. Verify that $\dot r_z^{(1)} = -(r_z + 1)/T_1$ has the correct sign and equilibrium.
*What this tests: the full Lindblad calculation for the physically important relaxation operator — deriving the 2:1 transverse-to-longitudinal rate ratio from the algebra, not from memory.*

8. *[Complete positivity: why it matters]* Consider the transpose map $\mathcal{T}:\hat\rho \mapsto \hat\rho^T$ (transposition of the density matrix). (a) Show that $\mathcal{T}$ preserves trace and Hermiticity. (b) Show that $\mathcal{T}$ preserves positivity (all eigenvalues non-negative) for any single-qubit density matrix. (c) Now consider the map $(\mathcal{T}\otimes\mathcal{I})$ applied to the Bell state $|\Phi^+\rangle\langle\Phi^+|$. Compute the result and check its eigenvalues. Does it have negative eigenvalues? (d) Conclude: why is $\mathcal{T}$ not a physical quantum channel, even though it looks reasonable on single qubits?
*What this tests: concrete example of a positive-but-not-completely-positive map; understanding why "complete" positivity is physically necessary when systems can be entangled with ancillas.*

**Challenge**

9. *[Non-Markovian decay and the Gaussian bath]* For a qubit coupled to a bath with a Gaussian correlation function $C(t) = (1/T_\phi^2)\exp(-t^2/\tau_c^2)$, the off-diagonal element decays as $|\rho_{01}(t)| = |\rho_{01}(0)|\exp(-\Gamma(t))$ where $\Gamma(t) = \int_0^t\int_0^{t'}C(t'')\,dt''\,dt'$. (a) Evaluate $\Gamma(t)$ for short times $t \ll \tau_c$ and for long times $t \gg \tau_c$. (b) Show that the short-time behavior is Gaussian ($\Gamma \propto t^2$) while the long-time behavior is exponential ($\Gamma \propto t$). (c) At what time $t^*$ does the behavior cross over from Gaussian to exponential? (d) Sketch $|\rho_{01}(t)|$ for two cases: $T_\phi \gg \tau_c$ (Markovian) and $T_\phi \sim \tau_c$ (non-Markovian). In which case does the Lindblad equation fail?
*What this tests: seeing how the Markov approximation breaks down for structured baths; deriving the Gaussian-to-exponential crossover that is observable in spin echo experiments.*

---

## References

Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Communications in Mathematical Physics*, 48, 119–130.

Gorini, V., Kossakowski, A., & Sudarshan, E. C. G. (1976). Completely positive dynamical semigroups of N-level systems. *Journal of Mathematical Physics*, 17, 821–825.

Breuer, H.-P., & Petruccione, F. (2002). *The Theory of Open Quantum Systems*. Oxford University Press. Chapter 3.

Zurek, W. H. (1981). Pointer basis of quantum apparatus: Into what mixture does the wave packet collapse? *Physical Review D*, 24, 1516–1525.

Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75, 715–775.

Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.

Schlosshauer, M. (2019). Quantum decoherence. *Physics Reports*, 831, 1–57.

Bloch, F. (1946). Nuclear induction. *Physical Review*, 70, 460–474.

Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. §§8.1–8.4.
