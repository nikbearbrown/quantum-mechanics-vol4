# Chapter 13 — Capstone: Quantum Mechanics in Research

## TL;DR

- The chapter where the formalism stops being curriculum and becomes literacy.
- The chapter moves through Mixed states and the density matrix, The Lindblad equation and the Bloch equations, The NISQ era and the threshold theorem, NV centers: Chapter 9 perturbation theory made real, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The chapter where the formalism stops being curriculum and becomes literacy.*

Here is a sentence from a real paper introduction, published in *Nature* in 2023 by the Google Quantum AI team:

> "We use a 72-qubit superconducting quantum processor to demonstrate a surface code logical qubit whose performance improves as the code distance is scaled from 3 to 5."

At the start of Chapter 1 you would have understood "qubit" and nothing else. By the end of this chapter you will read that sentence and know what every word means: what a surface code is, what code distance means and why scaling it should help, what a logical qubit is as distinct from a physical one, and why this paper was a landmark. It is the first experimental demonstration that the threshold theorem of quantum error correction actually works in hardware.

That sentence is the chapter's puzzle. Five research directions in which sentences like it are written every week. Five doorways, one chapter. The goal is not to master any of them — it is to read the first page of a paper in each field and understand the problem and the tools being deployed.

But before any of that, there is one piece of formalism the rest of the chapter cannot do without. Real qubits decohere. The clean state vectors of Chapters 1 through 12 are an idealization. To talk about hardware, error correction, NV centers, or the quantum-to-classical transition, you need the density matrix and the equation that governs it.

---

## Mixed states and the density matrix

A pure state $|\psi\rangle$ describes a quantum system about which you have complete information. Real systems are not pure. They are entangled with their environment — air molecules, phonons, stray magnetic fields, neighboring nuclear spins. Trace out the environment and the system's state is a *probabilistic mixture* of pure states, encoded in the density matrix:

$$\hat\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|, \qquad \sum_i p_i = 1, \quad p_i \geq 0.$$

Two properties identify $\hat\rho$: it has trace one, and it is Hermitian and positive semidefinite. For a pure state, $\hat\rho^2 = \hat\rho$ and $\text{Tr}(\hat\rho^2) = 1$. For a mixed state, $\text{Tr}(\hat\rho^2) < 1$ — this number is the purity, falling from 1 (pure) to $1/d$ (maximally mixed, dimension $d$). Expectation values come from $\langle\hat O\rangle = \text{Tr}(\hat\rho\hat O)$, which reduces to $\langle\psi|\hat O|\psi\rangle$ in the pure case.

For a single qubit, the Bloch representation is:

$$\hat\rho = \frac{1}{2}\bigl(\hat I + \vec r\cdot\vec\sigma\bigr), \qquad \vec r = (r_x, r_y, r_z), \quad |\vec r| \leq 1.$$

Pure states sit on the surface of the unit sphere; mixed states sit inside. The components are $r_i = \langle\hat\sigma_i\rangle$. Decoherence is what shrinks the Bloch vector from the surface toward the interior.

![Decoherence shrinks the Bloch vector. Pure states (surface) evolve into mixed states (interior). The quantum-to-classical transition is the spiral from the equator toward the south pole](../images/13-capstone-quantum-mechanics-in-research-fig-01.png)
*Figure 13.1 — Bloch sphere diagram showing three example states *

---

## The Lindblad equation and the Bloch equations

For a closed system, the density matrix evolves under the von Neumann equation — Schrödinger rewritten for $\hat\rho$: $d\hat\rho/dt = -(i/\hbar)[\hat H, \hat\rho]$. For an open system coupled to an environment, Lindblad proved in 1976 that the most general Markovian, completely positive, trace-preserving generator has the form:

$$\boxed{\frac{d\hat\rho}{dt} = -\frac{i}{\hbar}[\hat H, \hat\rho] + \sum_k\!\left(\hat L_k\hat\rho\hat L_k^\dagger - \frac{1}{2}\{\hat L_k^\dagger\hat L_k,\hat\rho\}\right)}$$

The first term is Hamiltonian evolution. The second is the dissipator — each $\hat L_k$ is a jump operator representing one channel by which the environment acts on the system. This is the workhorse equation of open quantum systems.

Now watch what it does to a qubit. Take $\hat H = (\hbar\omega_0/2)\hat\sigma_z$ and compute the commutator $[\hat H, \hat\rho]$ using the Pauli algebra $[\hat\sigma_z, \hat\sigma_x] = 2i\hat\sigma_y$ and $[\hat\sigma_z, \hat\sigma_y] = -2i\hat\sigma_x$:

$$[\hat H, \hat\rho] = \frac{\hbar\omega_0}{2}\cdot\frac{1}{2}\bigl(2ir_x\hat\sigma_y - 2ir_y\hat\sigma_x\bigr)$$

Dividing by $-i\hbar$ and matching Pauli components in $d\hat\rho/dt = \frac{1}{2}(\dot r_x\hat\sigma_x + \dot r_y\hat\sigma_y + \dot r_z\hat\sigma_z)$:

$$\dot r_x = -\omega_0 r_y, \qquad \dot r_y = \omega_0 r_x, \qquad \dot r_z = 0.$$

Free precession. The Bloch vector rotates about $\hat z$ at frequency $\omega_0$. No dissipation yet.

Now add pure dephasing — the process by which the phase between $|0\rangle$ and $|1\rangle$ randomizes without energy exchange. The jump operator is $\hat L_\phi = \sqrt{1/2T_\phi}\,\hat\sigma_z$. Computing the dissipator term using $\hat\sigma_z\hat\sigma_x\hat\sigma_z = -\hat\sigma_x$ and $\hat\sigma_z\hat\sigma_y\hat\sigma_z = -\hat\sigma_y$:

$$\hat\sigma_z\hat\rho\hat\sigma_z - \hat\rho = -r_x\hat\sigma_x - r_y\hat\sigma_y$$

so the dephasing dissipator contributes $\dot r_x = -r_x/T_\phi$, $\dot r_y = -r_y/T_\phi$, $\dot r_z = 0$. Pure dephasing kills the transverse components exponentially and leaves the longitudinal component alone. Geometrically: the Bloch vector is squeezed toward the $z$-axis.

Now add energy relaxation — the excited state $|1\rangle$ decaying to $|0\rangle$ by emitting energy to the environment. The jump operator is $\hat L_1 = \sqrt{1/T_1}\,\hat\sigma_-$. Working through the algebra of the lowering operator:

$$\dot r_x^{(1)} = -\frac{r_x}{2T_1}, \qquad \dot r_y^{(1)} = -\frac{r_y}{2T_1}, \qquad \dot r_z^{(1)} = -\frac{r_z+1}{T_1}.$$

The transverse components decay at *half* the longitudinal rate — a result automatic from the structure of the lowering operator.

Sum all three contributions:

$$\dot r_x = -\omega_0 r_y - \frac{r_x}{T_2}, \qquad \dot r_y = +\omega_0 r_x - \frac{r_y}{T_2}, \qquad \dot r_z = -\frac{r_z - r_z^{\text{eq}}}{T_1}$$

with the definition

$$\boxed{\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}.}$$

These are the **Bloch equations**. The qubit precesses about $\hat z$ at frequency $\omega_0$, transverse components decay with timescale $T_2$, and the longitudinal component relaxes to its equilibrium with timescale $T_1$.

The constraint $T_2 \leq 2T_1$ is immediate: $1/T_2 = 1/(2T_1) + 1/T_\phi \geq 1/(2T_1)$ since $T_\phi > 0$. Pure dephasing can make $T_2$ shorter than $2T_1$; nothing can make it longer. The limit $T_2 = 2T_1$ — called the natural linewidth limit — is approached by the best modern superconducting hardware.

Starting from the equator ($r_z(0) = 0$, $r_x(0) = 1$, $r_y(0) = 0$), the solution is:

$$r_x(t) = e^{-t/T_2}\cos(\omega_0 t), \qquad r_y(t) = e^{-t/T_2}\sin(\omega_0 t), \qquad r_z(t) = -1 + e^{-t/T_1}.$$

The Bloch vector precesses at $\omega_0$ while its transverse projection shrinks, spiraling onto the south pole. This is the chapter's signature image. The quantum-to-classical transition is visible: the off-diagonal entries of $\hat\rho$ vanish while the diagonal (classical) populations evolve normally.

![Three decoherence regimes. Pure precession (left); pure dephasing collapses the equatorial projection (center); combined dephasing and relaxation spirals the vector onto the ground state (right)](../images/13-capstone-quantum-mechanics-in-research-fig-02.png)
*Figure 13.2 — Figure showing the Bloch vector trajectory under decoherence*

![Decoherence in matrix form: diagonal populations survive (classical), off-diagonal coherences decay (quantum). This is what the Lindblad dissipator does in the density-matrix picture](../images/13-capstone-quantum-mechanics-in-research-fig-03.png)
*Figure 13.3 — 2×2 density matrix bar chart at two times*

Two misconceptions to name explicitly.

*"$T_2$ is just the qubit lifetime."* $T_1$ is the energy lifetime — the time for the excited population to decay. $T_2$ is the coherence lifetime — the time for off-diagonal elements of $\hat\rho$ to decay. A qubit can have long $T_1$ and short $T_2$ if the environment dephases it without absorbing energy. Coherence is more fragile than population.

*"Decoherence solves the measurement problem."* The Lindblad equation explains how off-diagonal coherences vanish in the pointer basis — why measurements look classical, why interference fringes disappear when the environment is monitoring. It does not explain why one particular outcome obtains in a single run. That gap — selection of one branch — remains open. Decoherence is a necessary part of any explanation. It is not sufficient.

---

## The NISQ era and the threshold theorem

In 2018, John Preskill named the era we have been living in: NISQ — Noisy Intermediate-Scale Quantum. A NISQ device has roughly 50 to 1000 physical qubits with gate fidelities high enough to do interesting things but too low to support full quantum error correction. The structural progression is:

$$\text{NISQ} \;\longrightarrow\; \text{fault-tolerant} \;\longrightarrow\; \text{useful quantum advantage.}$$

Each arrow is nontrivial. The gating event for the first arrow is the threshold theorem, proven theoretically in 1996–1998 by Aharonov–Ben-Or, Knill–Laflamme–Zurek, and Kitaev: if the physical gate error rate $p$ is below some threshold $p_{\text{th}}$, you can encode one *logical* qubit across many physical qubits and achieve arbitrarily low logical error rate by scaling up the code. Below threshold, bigger codes are better. Above threshold, bigger codes accumulate errors faster and are worse.

The leading practical implementation is the **surface code**, which encodes one logical qubit in an $L \times L$ patch of physical qubits with the threshold at around $p_{\text{th}} \approx 1\%$ — high enough that modern superconducting hardware can in principle operate below it. For two decades after the theorem, it was theoretical. Operating below threshold in hardware is a different problem.

Google demonstrated it experimentally in two stages. In 2023, Acharya et al. showed that scaling from code distance 3 to distance 5 gave the correct *trend* — the logical qubit improved — even if the distance-5 result was not yet better than the best physical qubit in absolute terms. In 2024, the same team showed distance-3, distance-5, and distance-7 codes, with logical error rate decreasing at each step. The threshold theorem is now an experimental observation. This is the milestone the opening sentence of the chapter was describing.

![The threshold theorem made experimental. Below p_th, larger surface codes have lower logical error rates. The Acharya et al. 2024 data points confirm the scaling — the first time this theorem was directly tested in hardware](../images/13-capstone-quantum-mechanics-in-research-fig-04.png)
*Figure 13.4 — Log-log plot of logical error rate p_L vs*

Read papers in this field with the structural frame in mind. Specific qubit counts and fidelities will be obsolete by the time you read this. As of writing, the leading platforms are superconducting transmons (IBM and Google), neutral atoms in optical tweezers (QuEra, Atom Computing), trapped ions (Quantinuum), and photonic systems (Xanadu, PsiQuantum). No platform has yet delivered unambiguous useful quantum advantage on a non-contrived problem. Sampling experiments (Google 2019, USTC 2021) demonstrated quantum advantage on tasks designed to be hard for classical computers — those were milestones, not applications. The practical consequences of Shor's algorithm are already arriving, though. In August 2024, NIST finalized the first three post-quantum cryptography standards — FIPS 203, 204, and 205 — in anticipation of fault-tolerant machines that do not yet exist. The world's cryptographic infrastructure is being replaced now.

---

## NV centers: Chapter 9 perturbation theory made real

A nitrogen-vacancy center in diamond is a point defect: a nitrogen atom substituted for one carbon, next to a vacant lattice site. The NV$^-$ charge state has a spin-1 electronic ground state with magnetic sublevels $|m_s\rangle$ for $m_s \in \{-1, 0, +1\}$.

The defect has a zero-field splitting of $D \approx 2.87$ GHz between the $m_s = 0$ sublevel and the degenerate $m_s = \pm 1$ pair, arising from spin-spin interaction in the crystal field. Apply an external magnetic field $\vec B$ along the NV axis. The effective Hamiltonian is:

$$\hat H_{\text{NV}} = D\hat S_z^2 + g\mu_B B\hat S_z$$

with $g \approx 2.003$. The eigenvalues are $E(0) = 0$, $E(\pm 1) = D \pm g\mu_B B$. The two transition frequencies from $|0\rangle$ are:

$$f_\pm = D \pm \frac{g\mu_B B}{h} \approx 2.87\,\text{GHz} \pm 28\,B\,\text{MHz/mT}.$$

This is exactly the perturbation theory of Chapter 9 — a Zeeman perturbation added to a known Hamiltonian, producing a linear splitting in the field strength. The splitting is a direct consequence of a formula you derived in that chapter.

You cannot put a voltmeter on a single NV center. You read it optically, by a technique called Optically Detected Magnetic Resonance (ODMR). First, illuminate with a 532 nm green laser; the optical cycling preferentially pumps the spin into $m_s = 0$. Second, sweep a microwave field through the transition frequencies; when the microwave is resonant, spin population transfers to $m_s = \pm 1$. Third, detect red fluorescence — the center is dimmer when the spin is in $m_s = \pm 1$ than in $m_s = 0$, because a non-radiative pathway through a singlet state competes with fluorescence from the triplet. You see two dips in the fluorescence spectrum, one at $f_+$ and one at $f_-$. The splitting between the dips gives you $B$.

This is a working room-temperature quantum sensor with sensitivity reaching the nT/$\sqrt{\text{Hz}}$ regime. Every piece of physics it uses was in a previous chapter: spin from Chapter 6, Zeeman perturbation from Chapter 9, Rabi oscillations from Chapter 10, decoherence $T_2$ from this chapter. A student who has followed the book to this point can read the canonical review by Rondin et al. (2014) and recognize every move in the paper.

![ODMR in an NV center. Dips in fluorescence mark the spin-transition frequencies. The splitting ΔF = 56B MHz/mT is a direct readout of the axial magnetic field](../images/13-capstone-quantum-mechanics-in-research-fig-05.png)
*Figure 13.5 — NV center ODMR spectrum diagram *

---

## Topology and the integer that cannot drift

In 1980, Klaus von Klitzing measured the Hall resistance of a two-dimensional electron gas and found it quantized in units of $h/e^2 = 25\,812.807\,45\,\Omega$, independent of sample geometry, material, and impurities. One part in $10^9$. The reason: the Hall conductance is proportional to a Chern number — an integer topological invariant of the band structure — and integers cannot drift.

The mathematics involves the Berry phase. When the Hamiltonian $\hat H(\vec R)$ is varied adiabatically around a closed loop in parameter space, an instantaneous eigenstate picks up a geometric phase

$$\gamma_n = i\oint\langle n(\vec R)|\nabla_{\vec R}|n(\vec R)\rangle\cdot d\vec R$$

that depends only on the path, not the speed of traversal. In a periodic crystal, integrating the Berry curvature over the Brillouin zone gives an integer Chern number. If that integer is nonzero, the material is a topological insulator (or a quantum Hall system), and a remarkable consequence follows: **protected boundary states must exist at any surface between the topological material and ordinary vacuum**. This is the bulk-boundary correspondence.

The boundary states are robust because their existence is enforced by an integer. You cannot destroy them with a perturbation without closing the bulk energy gap and changing the integer — a discontinuous jump, not a smooth drift. Edge channels carrying quantized Hall current; helical surface states in 3D topological insulators; Dirac cones on the surfaces of bismuth selenide — all of these are enforced by integers, and the integers cannot be confused.

The 2019 SI redefinition uses $h/e^2$ (along with the Josephson constant $h/2e$) to define electrical units from fundamental constants. The kilogram is defined through $h$. Topology — the integer that cannot drift — is embedded in the legal definition of the units of mass and electrical resistance.

![The bulk topology enforces boundary states. An integer in the bulk band structure guarantees conducting edge channels whose existence cannot be removed by any symmetry-preserving perturbation](../images/13-capstone-quantum-mechanics-in-research-fig-06.png)
*Figure 13.6 — Bulk-boundary correspondence diagram *

Kane and Mele showed in 2005 that time-reversal-invariant 2D insulators are classified by a $\mathbb{Z}_2$ invariant — they are either trivial or non-trivial. The non-trivial ones host helical edge states. Hasan and Kane's 2010 review is the canonical accessible treatment of the decade's discoveries. As of 2026, active areas include topological superconductors and Majorana zero modes (potential topologically protected qubits), higher-order topological insulators with gapless hinges, and topological photonics. The chapter does not go deep on any of these. They are on the map; now you can see where they are.

---

## Three open problems and one honesty move

This is the chapter where the textbook starts running out of answers. Three places where it does.

**The measurement problem.** Decoherence explains why off-diagonal coherences vanish in the pointer basis, why measurements look classical, why interference fringes disappear when the environment monitors. It does not explain why one particular outcome obtains in one particular run. Different interpretations — Copenhagen, many-worlds, Bohmian, GRW, QBism — handle this differently. None of them adds testable predictions to the formalism you have learned. Schlosshauer 2007 is the cleanest accessible treatment of what decoherence does and does not solve. The chapter's intellectual-honesty moment: the textbook gives you tools that work; it does not give you a resolved metaphysics.

**High-$T_c$ superconductivity.** The Hubbard model is the simplest interacting lattice model in condensed matter — electrons hopping on a lattice with on-site repulsion. Forty years after Bednorz and Müller's 1986 discovery, the mechanism of high-$T_c$ superconductivity in the cuprates is still contested. Recent numerical work suggests the 2D Hubbard model at certain parameters may not actually superconduct, putting pressure on the assumption that cuprate physics is captured by Hubbard alone. A student finishing this book has the toolkit to read these papers. They should know that the toolkit, applied to strongly correlated systems, does not yet yield consensus.

**Whether topological quantum computation will work.** Microsoft and others have spent two decades pursuing Majorana-based topologically protected qubits — devices whose error protection is enforced by topology rather than by active correction. The physics is beautiful. The engineering is unforgiving. As of 2026 there is no demonstrated topological qubit performing better than a surface-code qubit on the best competing hardware. This is one of the field's largest open bets.

One more move that has to be made explicitly. Every specific number in the quantum-computing section of this chapter — qubit counts, $T_1$ and $T_2$ values, the names of leading processors, the specific error-correction results — will be obsolete within one or two years. The structural framing will not. NISQ → fault-tolerant → useful quantum advantage is the durable scaffold. The threshold theorem is now experimentally demonstrated — that will not become untrue. Topology delivers protected boundary states whose existence is enforced by integer invariants — that is mathematics, not a hardware benchmark. Read the structural moves; look up the current numbers.

---

## Still puzzling

The measurement problem. We have a complete formalism that predicts the statistics of every experiment to extraordinary precision. We have a decoherence mechanism that explains why those statistics look classical when the environment is monitoring. What we do not have is a derivation, from first principles, of why one particular outcome obtains in one particular run. The textbook stops here. I do not know what fills the gap. As of 2026, neither does anyone else.

---

## LLM Exercise — the research-direction explorer

You are going to build a single HTML file with a top-level tab selector. Each tab implements one of three sub-simulations. The chapter's signature image — the Bloch vector spiraling inward as $T_1$ and $T_2$ act — lives in tab 1. The other tabs make the surface-code threshold and the NV-center magnetometer interactive.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 13 — Capstone: Quantum Mechanics in Research
Deliverable: 13-decoherence-simulator.html
Status: in progress

Top-level router: a horizontal tab selector at the top of the page with
three (or four) tabs, only one panel visible at a time:
  Tab 1 - Decoherence visualizer (Bloch sphere + Lindblad/Bloch equations)
  Tab 2 - Quantum-computing circuit + surface-code threshold demo
  Tab 3 - NV-center ODMR spectrometer
  Tab 4 (optional) - SSH chain / topology / Berry phase

Tab 1 - Decoherence visualizer.
- 500 x 500 SVG with a 2D projection of a 3D Bloch sphere.
- Sliders: T_1 (1 to 10000 in log scale, units of natural time),
  T_2 (1 to 2*T_1; clamped), omega_0 (0 to 5 in natural units),
  theta_0 (initial polar angle 0 to pi), phi_0 (initial azimuth 0 to 2 pi),
  time scrubber (0 to t_max).
- Bloch vector animates: precesses about z at omega_0, transverse
  components decay with T_2, longitudinal with T_1, equilibrium at
  the south pole (r_z = -1).
- Side panels:
  - Time series of <sigma_x>(t), <sigma_y>(t), <sigma_z>(t) for the
    last 5 periods.
  - Density-matrix bar plot: 2x2 grid, bar height = |rho_ij|,
    color = phase of rho_ij. Off-diagonals visibly shrink as
    decoherence proceeds.

Tab 2 - Circuit + surface code.
- Left half: extension of the Chapter 12 gate visualizer to up to
  5 qubits. Default scaffold: three-qubit bit-flip code.
- Right half: small surface-code lattice (5 x 5 data qubits with
  syndrome qubits between). Slider: physical error rate p in [0, 0.05].
  Plot: logical error rate vs. distance for d = 3, 5, 7 at the current p.
  When p is below threshold, the d = 7 curve is below d = 5 below d = 3.
  When p is above threshold, the order flips. Threshold crossing
  visible as the lines crossing.

Tab 3 - NV-center ODMR spectrometer.
- Inputs: magnetic field B (0 to 100 mT), angle theta (0 to pi/2 off
  NV axis).
- Output: ODMR spectrum as fluorescence vs. microwave frequency
  (2.5 to 3.3 GHz). Default: two symmetric dips at D +/- 28 B MHz
  with D = 2.87 GHz, FWHM ~ 5 MHz.
- Increase B: dips split apart linearly. Increase theta off-axis:
  additional sub-peaks appear from the four crystallographic NV
  orientations.

Tab 4 - Topology (optional, SSH model).
- 1D Su-Schrieffer-Heeger chain of 20 sites.
- Slider: hopping ratio t_1/t_2 in [0.1, 10].
- Plot: bulk band structure (two bands meeting at t_1/t_2 = 1).
- When t_1/t_2 < 1, edge states appear at the two ends of the chain;
  when t_1/t_2 > 1, no edge states. Animation: states evolving as
  the ratio slides through the transition at 1.

Natural units throughout: hbar = 1. Time unit = 1/omega_0_default.
Tab routing: simple show/hide of named divs; no SPA framework.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md (coding constitution) the following physics rules for
Chapter 13 simulations:

OPEN QUANTUM SYSTEMS AND DECOHERENCE PHYSICS RULES

1. The qubit density matrix is parameterized by the Bloch vector r:
     rho = (1/2) (I + r_x sigma_x + r_y sigma_y + r_z sigma_z)
   with |r| <= 1. Always enforce |r| <= 1 after each integration step
   (clamp to 1 if rounding pushes above; warn on > 1.01).

2. Bloch equations (the chapter's signature equations):
     dot r_x = -omega_0 r_y - r_x / T_2
     dot r_y = +omega_0 r_x - r_y / T_2
     dot r_z = -(r_z - r_z_eq) / T_1
   with 1/T_2 = 1/(2 T_1) + 1/T_phi. The user slides T_1 and T_2; the
   simulator INFERS T_phi from 1/T_phi = 1/T_2 - 1/(2 T_1). Validity:
   T_2 must be in (0, 2 T_1]. Clamp T_2 if the user pushes it above 2 T_1.

3. Equilibrium: r_z_eq = -1 (south pole, |1> as ground). Make this
   the default; allow the user to flip the convention via a toggle.

4. Integrate the Bloch equations with RK4. Time step:
     dt = min(0.01 / omega_0, 0.01 * min(T_1, T_2))
   so the precession and the decay are both resolved.

5. Density matrix from r:
     rho[0,0] = (1 + r_z)/2,  rho[1,1] = (1 - r_z)/2
     rho[0,1] = (r_x - i r_y)/2,  rho[1,0] = conj(rho[0,1])
   For the bar plot: |rho[0,1]| visibly shrinks as t increases.

6. Bloch sphere rendering: orthographic projection onto the page,
   viewed at a slight angle (10-20 degrees from straight on z).
   Surface: light grey wireframe (equator + two meridians). Vector:
   orange arrow from origin to (r_x, r_y, r_z). Trail: last 200 vector
   tips, fading to transparent.

NV-CENTER ODMR PHYSICS RULES

7. The NV Hamiltonian (axial field):
     H_NV = D S_z^2 + g mu_B B S_z
   with D = 2.87 GHz (display in GHz directly). Transition frequencies
   from m_s = 0 to m_s = +/- 1:
     f_+- = D +/- g mu_B B / h
   with g mu_B / h = 28.025 MHz/mT. Render each dip as a Lorentzian
   with FWHM 5 MHz (adjustable slider).

8. Off-axis field: the spin Hamiltonian becomes anisotropic. Compute
   eigenvalues by diagonalizing the 3x3 spin matrix
     H = D S_z^2 + g mu_B (B cos theta) S_z + g mu_B (B sin theta) S_x
   The two transitions split unevenly. For axial field (theta = 0),
   they are exactly symmetric about D. For theta near pi/2, the lower
   transition saturates at D.

SURFACE-CODE THRESHOLD PHYSICS RULES

9. The logical error rate scales as
     p_L(d) ~ A (p / p_th)^( (d+1) / 2 )
   with p_th ~ 0.01 for the standard surface code [verify exact threshold].
   For p < p_th, larger d means smaller p_L (the curves are ordered).
   For p > p_th, the inequality flips. Render the three curves (d = 3, 5, 7)
   crossing at p_th on a log-log plot.

KNOWN FAILURE MODES to avoid:
(a) Forgetting to renormalize the Bloch vector after RK4 step
    (rounding can push above 1; clamp).
(b) T_2 > 2 T_1 input by user (forbidden by the relation; clamp).
(c) Bloch vector trail not clearing between simulation resets.
(d) ODMR dip widths set independently of laser power (real spectra
    broaden with power; set width = base_width + 0.1 * power for
    realism).
(e) Surface-code curves rendered as if the threshold is a sharp
    transition rather than a crossover. Use the analytic formula
    above for a smooth crossover.
(f) Tab switching does not reset the active simulation. Pause the
    animation on the hidden tab to save CPU.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 13-decoherence-simulator.html: a single self-contained HTML file
using D3 v7 from a CDN, no other dependencies, that implements the
Chapter 13 simulation as specified in PROJECT.md and following the
physics rules in CLAUDE.md and the visual constitution in DESIGN.md.

The page has a header (h1 + one-sentence subtitle) and a horizontal
tab strip with three tabs:
  [ Decoherence ]  [ Circuits + Surface Code ]  [ NV-Center ODMR ]

(Optional fourth tab "Topology (SSH)" is welcome but not required for
the first pass.)

Each tab is a <section> with a unique id; switching tabs toggles
display: none/block. Pause animations on hidden tabs.

TAB 1 - Decoherence visualizer.
Layout: 500 x 500 Bloch sphere on the left; two side panels stacked
on the right (each 400 x 240). Top side panel: time series of
<sigma_x>(t), <sigma_y>(t), <sigma_z>(t) traced as three lines with
different colors. Bottom side panel: 2x2 grid showing |rho_ij| as
bar heights with phase color.

Sliders below: T_1 (log scale 1 to 10000), T_2 (linear, clamped to
2 T_1), omega_0 (0 to 5), theta_0 (0 to pi), phi_0 (0 to 2 pi),
time scrubber (0 to 5 max(T_1, 1/omega_0)).

Play/pause button. Reset trail button.

Integration: RK4 on the Bloch equations as specified in CLAUDE.md
rule 2. Update at 60 fps via requestAnimationFrame.

TAB 2 - Circuits and surface code.
Layout: left half (450 wide) is a gate circuit (extension of Ch 12
to 5 qubits with three-qubit-bit-flip-code as default scaffold).
Right half (450 wide) shows a small surface code lattice and a
log-log plot of logical error rate vs. physical error rate.

Three sub-displays in the right panel:
- 5 x 5 grid of data and syndrome qubits, colored by syndrome state
  (green = no error detected, red = error syndrome).
- Slider for physical error rate p in [0.0001, 0.05] log scale.
- Plot of p_L(d, p) for d = 3, 5, 7 with the threshold p_th visible
  as a vertical dashed line. The three lines cross at p_th.

TAB 3 - NV-center ODMR spectrometer.
Layout: 700 x 400 SVG.
Sliders: B magnitude (0 to 100 mT), angle theta off NV axis (0 to pi/2),
laser power (0 to 1, sets dip width via CLAUDE.md rule 8 modification),
microwave power (0 to 1, sets dip depth).

Display: spectrum plot, microwave frequency on x-axis (2.5 to 3.3 GHz),
fluorescence on y-axis (normalized 0 to 1).

At B = 0, theta = 0: one dip at 2.87 GHz (the m_s = 0 -> +/-1
transitions are degenerate). At B > 0, theta = 0: two dips at
D +/- 28*B MHz. At theta > 0: dips split into pairs from the four
NV orientations (extra sub-peaks appear).

A small Hamiltonian-matrix display shows the 3x3 spin Hamiltonian
explicitly with its eigenvalues; the dip positions are the
eigenvalue differences.

Runtime sanity checks (write to console):
- Tab 1: |r| <= 1 + 1e-6 at every step.
- Tab 1: time-series oscillation period matches 2 pi / omega_0
  within 5%.
- Tab 1: r_z decays to r_z_eq within 5 * T_1.
- Tab 2: at p = p_th, the three logical error curves should
  intersect at the same point within rounding.
- Tab 3: at B = 0, theta = 0, the spectrum has exactly one dip
  at 2.87 GHz (within slider resolution).
- Tab 3: spectrum integral (1 minus fluorescence) is positive
  everywhere.

Do NOT use any 3D library. The Bloch sphere is a 2D orthographic
projection. Do NOT use math.js; implement 3x3 matrix diagonalization
in vanilla JS (use the analytic formula for symmetric 3x3, or QR).
Comments at every non-trivial physics step.
```

### Part 4 — Exploration tasks and extension prompt

Run the simulation and answer the following:

1. **Tab 1, pure dephasing only.** Set $T_1 \to \infty$ (the slider's maximum), set $T_2$ to a finite value (say $T_2 = 100$ in natural units). Set the initial state on the equator ($\theta_0 = \pi/2$, $\phi_0 = 0$). Watch what happens to the Bloch vector. It should flatten onto the $z$-axis without its $z$-component changing. Confirm: the transverse components decay with $T_2$, and the longitudinal component is preserved. This is pure dephasing.

2. **Tab 1, the chapter's signature image.** Set $T_1 = T_2 = 100$, $\omega_0 = 2$. Start on the equator ($\theta_0 = \pi/2$). Play. The Bloch vector should spiral inward — circling at frequency $\omega_0$ while shrinking. Note that it spirals onto the south pole (the equilibrium), not the origin. The off-diagonal entries in the density-matrix bar plot visibly decay. **This is the quantum-to-classical transition, made visible.**

3. **Tab 1, the constraint.** Try to set $T_2 > 2T_1$. The slider should refuse (clamping). Confirm in the formula: $1/T_2 = 1/(2T_1) + 1/T_\phi$ with $T_\phi > 0$ forces $T_2 \leq 2T_1$. There is no jump operator that gives a longer coherence time than the natural-linewidth limit.

4. **Tab 2, the threshold.** Set the physical error rate $p$ to $0.001$ (well below threshold). Read off the logical error rates for $d = 3, 5, 7$. The $d = 7$ rate should be the smallest. Now push $p$ to $0.05$ (above threshold). The order should flip: $d = 7$ is now *worst*. Slide $p$ slowly through the crossover; identify where the curves cross. **This is what Acharya et al. 2024 demonstrated experimentally.**

5. **Tab 3, the ODMR splitting.** Set $\theta = 0$ (axial field). Set $B$ to $10$ mT. Read off the two dip frequencies. Compute the splitting analytically using $\Delta f = 2 \times 28 \times B\,\text{MHz/mT} = 560\,\text{MHz}$. Confirm the simulator agrees within slider resolution. **You have just done NV magnetometry — using Chapter 9 perturbation theory.**

6. **Tab 3, off-axis.** Set $B = 30$ mT, slide $\theta$ from $0$ to $\pi/2$. Watch the two main dips and the sub-peaks. At $\theta = 0$, only two dips. At $\theta > 0$, additional sub-peaks appear from the four equivalent crystallographic NV orientations in a diamond crystal. Real NV magnetometry uses single-orientation samples to avoid this complication.

**Extension prompt:**

```
Modify 13-decoherence-simulator.html in one of three ways. Pick whichever
matches your final-project direction:

OPTION A - Driven qubit and Rabi oscillations.
Modify Tab 1 to add a Rabi drive. The Hamiltonian becomes
  H = (hbar omega_0 / 2) sigma_z + Omega cos(omega_d t) sigma_x
Add sliders: Omega (drive strength), omega_d (drive frequency).
Show Rabi oscillations decaying under the Bloch dynamics. On resonance
(omega_d = omega_0), the oscillation frequency is the Rabi frequency
Omega; off resonance, the generalized Rabi frequency
sqrt(Omega^2 + (omega_d - omega_0)^2). Display the chevron plot
(Rabi frequency vs. drive detuning at fixed Omega).

OPTION B - Two-qubit entanglement decay.
Add a fourth tab implementing two independent qubits each undergoing
Bloch dynamics. Initial state: |Phi+> (entangled). Each qubit has its
own T_1, T_2. Compute the concurrence
  C(t) = max(0, lambda_1 - lambda_2 - lambda_3 - lambda_4)
where the lambda_i are decreasing-ordered square roots of eigenvalues
of rho * (sigma_y tensor sigma_y) rho* (sigma_y tensor sigma_y).
Plot C(t). Compare entanglement-decay time to the single-qubit T_2.

OPTION C - Final-project peer tutorial.
Pick one of the five research directions (decoherence, hardware,
error correction, NV centers, topology). Build a fifth tab that
serves as a peer tutorial for a student who has only completed
Chapter 12. Include: one cold-open paragraph, three interactive
mini-demos, three exercises with answers in a collapsible section.

Update PROJECT.md to mark Chapter 13 as complete. Note that this
deliverable is the book's capstone — the simulation set is now done,
and the student's portfolio is the 14-file directory accumulated
across the semester.
```

---

## Exercises

### Warm-up

**13.1** Write the density matrix $\hat\rho$ for each of the following states, and for each compute the purity $\text{Tr}(\hat\rho^2)$ and the Bloch vector $\vec r$. (a) The pure state $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. (b) The equal mixture $\hat\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$. (c) The pure state $|0\rangle$. (d) The maximally mixed state $\hat I/2$. Verify that $|\vec r| = 1$ for pure states and $|\vec r| < 1$ for mixed states. *(Tests: density matrix construction; purity computation; Bloch vector extraction; distinguishing pure from mixed.)*

**13.2** Derive the Bloch equation $\dot r_z = -(r_z - r_z^{\text{eq}})/T_1$ from the Lindblad equation with the energy-relaxation jump operator $\hat L_1 = \sqrt{1/T_1}\hat\sigma_-$. Show the intermediate step: compute $\hat\sigma_-\hat\rho\hat\sigma_+$ and $\hat\sigma_+\hat\sigma_-\hat\rho + \hat\rho\hat\sigma_+\hat\sigma_-$ explicitly in terms of the Bloch vector components, then extract the equation for $\dot r_z$. *(Tests: Lindblad dissipator computation with lowering operator; ability to extract equations of motion for Bloch components from operator equations.)*

**13.3** Prove the constraint $T_2 \leq 2T_1$ from the relation $1/T_2 = 1/(2T_1) + 1/T_\phi$ by noting that $T_\phi > 0$ implies $1/T_\phi > 0$. Then: (a) what value of $T_\phi$ gives the equality $T_2 = 2T_1$? (b) If $T_1 = 200\,\mu$s, what is the maximum allowed $T_2$? (c) If experimentally $T_1 = 200\,\mu$s and $T_2 = 180\,\mu$s, compute $T_\phi$. *(Tests: algebraic manipulation of the T₁–T₂–T_φ relation; physical interpretation of the natural linewidth limit.)*

### Application

**13.4** An NV center is in a magnetic field $B = 50\,\text{mT}$ applied along the NV axis. (a) Compute the two ODMR transition frequencies $f_+$ and $f_-$ using $g\mu_B/h = 28\,\text{MHz/mT}$ and $D = 2.87\,\text{GHz}$. (b) What is the frequency splitting $\Delta f = f_+ - f_-$? (c) An unknown field produces an ODMR splitting of $840\,\text{MHz}$. What is $B$? (d) If $T_2^{*} = 1\,\mu$s (the inhomogeneous dephasing time), what is the Fourier-limited linewidth of each dip in MHz? *(Tests: NV Hamiltonian eigenvalues; ODMR frequency calculation; inverting the splitting to find B; connecting T₂ to linewidth.)*

**13.5** A qubit starts in the state $\hat\rho_0$ with $r_x(0) = 1$, $r_y(0) = r_z(0) = 0$ (pointing along $+\hat x$, on the equator). It evolves under the Bloch equations with $\omega_0 = 0$ (no precession), $T_1 = 4\,\mu$s, and $T_2 = 2\,\mu$s. (a) Write down $r_x(t)$, $r_y(t)$, $r_z(t)$ explicitly using the solution in the chapter. (b) At $t = T_2 = 2\,\mu$s, compute $|\hat\rho(t)|$ — the purity $\text{Tr}(\hat\rho^2)$. Has the state become mixed? (c) At $t = T_1 = 4\,\mu$s, compute all three Bloch components and the purity. (d) What is the equilibrium state $\hat\rho(\infty)$ and where does it sit on the Bloch sphere? *(Tests: solving the Bloch equations with given initial conditions; computing purity at intermediate times; identifying the equilibrium state.)*

**13.6** Surface-code threshold. The logical error rate for a distance-$d$ surface code at physical error rate $p$ scales approximately as $p_L \approx A(p/p_\text{th})^{(d+1)/2}$ with $p_\text{th} \approx 0.01$. (a) For $p = 0.002$ and $A = 0.1$, compute $p_L$ for $d = 3, 5, 7$. Confirm the ordering $p_L^{(7)} < p_L^{(5)} < p_L^{(3)}$. (b) For $p = 0.02$ (above threshold), repeat. Confirm the ordering inverts. (c) How many physical qubits does a distance-$d$ surface code require (approximately $d^2$ data qubits plus $d^2 - 1$ syndrome qubits)? Compute the physical qubit overhead for achieving $p_L = 10^{-6}$ at $p = 0.002$, using the formula above to find the required $d$. *(Tests: threshold theorem formula; ordering of logical error rates; physical qubit overhead estimation.)*

### Synthesis

**13.7** Lindblad structure theorem. (a) Show that the Lindblad dissipator $\mathcal{D}[\hat\rho] = \hat L\hat\rho\hat L^\dagger - \frac{1}{2}\{\hat L^\dagger\hat L, \hat\rho\}$ preserves $\text{Tr}(\hat\rho) = 1$. (Hint: compute $\text{Tr}(\mathcal{D}[\hat\rho])$ using cyclicity of trace and $\hat L^\dagger\hat L = \hat L^\dagger\hat L$.) (b) Show that $\mathcal{D}[\hat\rho]$ is Hermitian if $\hat\rho$ is Hermitian. (c) The Lindblad form is the unique form that is linear in $\hat\rho$, preserves trace, preserves Hermiticity, and is completely positive. Explain why *complete* positivity is a stronger requirement than *ordinary* positivity, and give a physical reason why it must be satisfied. *(Tests: trace preservation and Hermiticity of the Lindblad dissipator; understanding of complete positivity as the physically required condition for reduced-state evolution.)*

**13.8** Berry phase and the Aharonov-Bohm effect. An electron moves in a closed loop enclosing a magnetic flux $\Phi_B$. Even though the magnetic field is zero along the path, the vector potential $\vec A$ is nonzero, and the wave function picks up a phase $\gamma = e\Phi_B/\hbar$. (a) Show that this is an instance of the Berry phase formula $\gamma_n = i\oint\langle n(\vec R)|\nabla_{\vec R}|n(\vec R)\rangle\cdot d\vec R$ with the parameter space being the position of the electron along the loop and the relevant parameter being $\vec A$. (b) In an integer quantum Hall system, the Hall conductance is $\sigma_{xy} = Ce^2/h$ where $C$ is the Chern number — the Berry curvature integrated over the Brillouin zone. Explain in two sentences why $C$ being an integer means the Hall resistance $h/(Ce^2)$ cannot drift continuously. (c) What physical symmetry would have to be broken to change $C$ from 1 to 0, and why does this protect the edge states? *(Tests: connecting the Berry phase formula to a concrete physical effect; understanding why an integer topological invariant enforces robustness; identifying the symmetry-protection mechanism.)*

### Challenge

**13.9** Decoherence and the quantum Zeno effect. The quantum Zeno effect: if you measure a quantum system very frequently, you suppress its evolution. (a) Show that if a qubit starts in $|0\rangle$ and you measure it in the $\{|0\rangle, |1\rangle\}$ basis $N$ times in a total time $T$, the probability of surviving in $|0\rangle$ after $N$ measurements scales as $(1 - \Omega^2 T^2/N^2)^N \to 1$ as $N \to \infty$ for fixed $T$ and Rabi frequency $\Omega$. (This is the undecayed pure-state Zeno effect.) (b) Now replace continuous measurement with Lindblad dephasing at rate $\Gamma = 1/T_\phi$. Show that the Bloch equations with $T_\phi$ finite describe continuous monitoring of the qubit's phase, and that in the limit $T_\phi \to 0$ (fast dephasing), the off-diagonal elements vanish instantly — the decoherence-induced Zeno effect. (c) In NV centers, dynamical decoupling sequences (periodic $\pi$ pulses) extend $T_2$ by reversing the effect of slow environmental noise. Explain qualitatively, using the Bloch picture, why periodic $\pi$ pulses along $\hat x$ can cancel slow $\hat z$-axis noise. *(Tests: quantum Zeno effect calculation; connection between Lindblad dephasing and continuous measurement; dynamical decoupling in the Bloch picture.)*

**13.10** The T₁–T₂ hierarchy across platforms. Collect the following data (use current literature or NIST/review-paper values as of 2025–2026): for superconducting transmons, trapped ions (Quantinuum H2), and NV centers, report $T_1$ and $T_2$ in consistent units. (a) Compute $T_2/T_1$ for each platform. Which approaches the natural linewidth limit $T_2 = 2T_1$, and which is far below it? (b) Use the formula $1/T_\phi = 1/T_2 - 1/(2T_1)$ to extract the pure dephasing time $T_\phi$ for each. What is the dominant noise source for each platform (flux noise for transmons, motional heating for ions, magnetic fluctuations from $^{13}$C nuclear spins for NV)? (c) A quantum error correction protocol needs $T_1 > 10^4$ gate times. If a gate takes $\tau_g = 100\,\text{ns}$ on a superconducting platform and $\tau_g = 1\,\mu$s on a trapped-ion platform, which platform meets this requirement with current $T_1$ values? *(Tests: looking up and comparing decoherence parameters across platforms; connecting $T_1$ and $T_2$ to hardware constraints; error-correction overhead estimation from real parameters.)*

---

*Sources: Lindblad (1976), Comm. Math. Phys. 48, 119; Zurek (2003), Rev. Mod. Phys. 75, 715; Schlosshauer (2007), Decoherence and the Quantum-to-Classical Transition, Springer; Preskill (2018), Quantum 2, 79; Acharya et al. (Google Quantum AI, 2023), Nature 614, 676; Acharya et al. (2024), Nature 638, 920; Doherty et al. (2013), Physics Reports 528, 1; Rondin et al. (2014), Rep. Prog. Phys. 77, 056503; Berry (1984), Proc. Roy. Soc. A 392, 45; von Klitzing et al. (1980), Phys. Rev. Lett. 45, 494; Kane & Mele (2005), Phys. Rev. Lett. 95, 146802; Hasan & Kane (2010), Rev. Mod. Phys. 82, 3045; Kitaev (2003), Annals of Physics 303, 2; Shor (1994), FOCS; NIST FIPS 203/204/205 post-quantum cryptography standards (August 2024).*
