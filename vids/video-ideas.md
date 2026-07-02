# Bear's Doodles — Quantum Mechanics, Vol. 4 Video Ideas

*Scouted from the 10 content chapters. Focused on information, measurement, and hardware concepts where animation carries the lesson.*

## Candidate 01 — Why Entanglement Is Not Just Strong Correlation
- Source: `quantum-mechanics-vol4/chapters/02-composite-systems-and-entanglement.md`
- Production mode: Manim visualization
- Hook: Two quantum systems can be correlated in a way no list of private instructions can reproduce.
- Core idea: An entangled state cannot be factored into independent local states; the Schmidt decomposition shows one shared structure rather than two separate descriptions.
- Visual object: Two separate state cards failing to factor, then locking into a shared Bell-state bar.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: product state, superposition, two qubits
- Exclusions: no entropy calculation, no full Schmidt algorithm, no Bell-test statistics
- Score: 9/10

## Candidate 02 — Why Bell's Inequality Breaks Local Hidden Instructions
- Source: `quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md`
- Production mode: Mixed
- Hook: If particles carry prewritten answers, one simple score can never exceed 2, yet quantum mechanics reaches farther.
- Core idea: Local realism constrains the CHSH combination because each hidden instruction sheet fixes all four answers; entangled quantum states violate that bound through incompatible measurement settings.
- Visual object: Instruction cards capped at 2, contrasted with rotating measurement axes pushing the quantum score higher.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: two-outcome measurements, correlation, inequality as a limit
- Exclusions: no loophole-free experiment details, no Tsirelson proof, no interpretation debate
- Score: 10/10

## Candidate 03 — Why Decoherence Makes Quantum Behavior Look Classical
- Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`
- Production mode: Manim visualization
- Hook: A superposition does not need to be watched by a person to lose its visible quantum weirdness.
- Core idea: The environment becomes entangled with the alternatives, causing the phase relationship between them to disappear from the system's reduced state.
- Visual object: Two clean interference paths leaking phase tags into many environment dots until fringes fade.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: superposition, phase, environment
- Exclusions: no Lindblad derivation, no pointer-state taxonomy, no interpretation claims about real collapse
- Score: 10/10

## Candidate 04 — Why You Cannot Clone an Unknown Qubit
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`
- Production mode: Manim visualization
- Hook: A quantum computer can copy classical bits, but an unknown qubit refuses to be duplicated.
- Core idea: A cloning machine that works on basis states must also preserve superpositions linearly, and those requirements contradict the copy it promises.
- Visual object: A copier that handles |0> and |1>, then jams when a diagonal qubit enters.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: qubit, basis states, superposition
- Exclusions: no density-matrix proof, no broadcasting theorem, no cryptographic applications
- Score: 9/10

## Candidate 05 — Why Quantum Teleportation Needs Two Classical Bits
- Source: `quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md`
- Production mode: Manim visualization
- Hook: Teleportation moves an unknown qubit without copying it, but it still cannot outrun a normal message.
- Core idea: Alice's Bell measurement transfers the unknown state into Bob's qubit up to one of four corrections, and two classical bits tell Bob which correction to apply.
- Visual object: An unknown qubit, an entangled pair, four measurement outcomes, and Bob's correction dial.
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: entanglement, measurement outcome, qubit gates
- Exclusions: no full algebra table, no dense-coding dual protocol, no faster-than-light discussion beyond the two-bit gate
- Score: 9/10

## Candidate 06 — Why Mixed States Fill a Ball, Not a Sphere
- Source: `quantum-mechanics-vol4/chapters/01-mixed-states-and-the-density-matrix.md`
- Production mode: Manim visualization
- Hook: Pure qubits live on the surface of the Bloch sphere, but noisy qubits sink inside it.
- Core idea: Mixing states shortens the Bloch vector because uncertainty about preparation averages directions together, while pure states keep full-length vectors.
- Visual object: Surface arrows averaging into a shorter arrow inside the Bloch ball.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: qubit state, vector average, probability mixture
- Exclusions: no trace formula derivation, no partial trace, no purity algebra beyond vector length
- Score: 8/10

## Candidate 07 — Why Quantum Error Correction Measures Errors Without Reading the Qubit
- Source: `quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md`
- Production mode: Manim visualization
- Hook: Correcting a qubit sounds impossible because measuring it should destroy the information.
- Core idea: Stabilizer measurements reveal the error syndrome, not the encoded logical state, so the system can identify which correction to apply without learning the protected qubit.
- Visual object: A hidden logical qubit inside a code block with syndrome lights turning on around it.
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: bit flip, measurement, redundancy
- Exclusions: no full Shor code circuit, no threshold theorem proof, no surface-code lattice details
- Score: 9/10

## Candidate 08 — Why Hardware Qubits Are Always a Tradeoff
- Source: `quantum-mechanics-vol4/chapters/08-quantum-hardware.md`
- Production mode: Doodle
- Hook: The best qubit is not the one that is easiest to control or the one that lives longest.
- Core idea: Hardware platforms balance conflicting demands: isolation protects coherence, but access is needed for fast gates, readout, and scaling.
- Visual object: A balance scale with isolation on one side and control/readout on the other.
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: qubit, coherence, control
- Exclusions: no full platform catalog, no DiVincenzo checklist detail, no engineering performance table
- Score: 7/10

## Candidate 09 — Why Measurement Has Two Rules That Do Not Fit Together
- Source: `quantum-mechanics-vol4/chapters/07-measurement-and-interpretations.md`
- Production mode: Manim visualization
- Hook: Quantum theory evolves smoothly until measurement, then suddenly switches to a different rule.
- Core idea: Unitary evolution spreads amplitudes continuously, while the measurement update selects one outcome; decoherence explains why interference fades but not which outcome becomes actual.
- Visual object: A smooth branching tree followed by a highlighted single branch, with faded interference lines.
- Manim move: collapse
- Short-form fit: Medium
- Prerequisites: wavefunction, measurement, superposition
- Exclusions: no interpretation survey, no consciousness claims, no decoherence-as-collapse shortcut
- Score: 8/10

## Candidate 10 — Why CNOT Creates Entanglement
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`
- Production mode: Manim visualization
- Hook: One controlled gate can turn two simple qubits into a state neither qubit owns alone.
- Core idea: A Hadamard creates a control superposition, and CNOT copies only the control's basis value into the target, tying the two branches into a Bell state.
- Visual object: A two-wire circuit where one branch splits, the target flips on one branch, and the branches recombine as a Bell pair.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: qubit wire, H gate, controlled flip
- Exclusions: no universal gate sets, no matrix multiplication, no hardware implementation
- Score: 8/10
