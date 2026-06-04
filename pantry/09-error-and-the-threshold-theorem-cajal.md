# CAJAL Figure Report — Chapter 9 — Error and the Threshold Theorem

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Digitization of continuous errors onto the Pauli basis

**Heuristic:** MC | **Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-stage process flowchart showing how a general single-qubit error channel is reduced to a discrete set of correctable errors. In the first stage, represent an arbitrary Kraus-operator error as a cloud of continuous deformations around a qubit state vector — arrows fanning outward in many directions. In the second stage, show four discrete labeled basis operators arranged as the corners of a diamond: identity, bit-flip, phase-flip, and combined. Connect the continuous cloud to the four corners with converging arrows representing linear decomposition. Below the diamond, show a single corrective arrow closing a loop back to the original state — one correction per detected basis error. The entire flow reads left-to-right: physical noise enters, decomposition happens, basis errors are identified and reversed. Use flat vector geometry with no baked text or labels in the image itself.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** Two named stages: (1) general single-qubit error channel represented as a continuum of Kraus operators, (2) Pauli-basis decomposition reducing the continuum to four discrete operators — I (identity/no error), X (bit-flip), Z (phase-flip), Y (combined). The decomposition relationship is a linear projection (each Kraus operator is a linear combination of the four). A corrective feedback closes the loop after basis-error identification. No specific Kraus matrices are depicted — only the structural reduction.

**[O — ORGANIZATION]** Horizontal left-to-right flow. Left node: continuous error cloud (a circle with radiating uncertain arrows). Center: decomposition funnel or bracket. Right node: four Pauli-basis shapes at cardinal positions of a diamond, connected by converging lines from the funnel. Bottom: correction arrow looping back to the original qubit circle. Three stages are visually separated by vertical space or dividers.

**[P — PRESENTATION]** Flat vector. Continuous-error cloud: light gray fill, multiple thin radiating arrows in light gray. Decomposition funnel: Sky Blue `#56B4E9` strokes. Four Pauli-basis nodes: I in neutral gray; X (bit-flip) in Bluish Green `#009E73`; Z (phase-flip) in Orange `#E69F00`; Y (combined) in Reddish Purple `#CC79A7`. Correction feedback arrow: Blue `#0072B2`. Uniform 1 pt strokes. White background. No baked text.

**[E — EXCLUSIONS]** Omit: multi-qubit errors, two-qubit Pauli operators, specific matrix elements, density matrix formalism, measurement apparatus, ancilla qubits, syndrome circuits, any downstream QEC logic.

### BLOCK 3 — NEGATIVE PROMPT

continuous error cloud rendered as photographic texture, specific matrix values, multi-qubit Pauli tensor products, ancilla qubits, syndrome measurement symbols, Bloch sphere with latitude/longitude grid, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales.

---

## Figure 2 — 3-qubit bit-flip code: encoding circuit and syndrome extraction

**Heuristic:** MC | **Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a horizontal quantum circuit diagram for the 3-qubit bit-flip code, spanning encoding and syndrome measurement. Show five horizontal wire lanes: three data qubits and two ancilla qubits. In the encoding region, place two CNOT gates: control on the top wire, targets on the middle and bottom wires respectively. After encoding, show the error stage as a marked gate on the middle data wire. In the syndrome region, show four CNOT gates coupling data qubits to ancilla wires: qubit 1 and qubit 2 each controlled-connecting into ancilla 1; qubit 2 and qubit 3 each controlled-connecting into ancilla 2. End each ancilla lane with a measurement symbol. Use standard quantum circuit conventions: single lines for qubit wires, filled circles for controls, open circles with plus signs for CNOT targets, and meter symbols for measurements. No text baked in.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** Five wire lanes: data qubits q1, q2, q3 (top three) and ancilla qubits a1, a2 (bottom two). Encoding block: CNOT(q1→q2), CNOT(q1→q3). Error block: single X gate on q2 (showing one specific error scenario). Syndrome block: CNOT(q1→a1), CNOT(q2→a1), CNOT(q2→a2), CNOT(q3→a2). Measurement block: measurement symbols on a1 and a2. Three visually distinct regions: encoding / error / syndrome+measurement.

**[O — ORGANIZATION]** Strict left-to-right time flow on five parallel horizontal wire lanes. Regions separated by vertical dashed dividers. Encoding CNOTs cluster on the left; error gate center-left; syndrome CNOTs right-center; measurement symbols at the right terminus of ancilla lanes. Data qubit lines continue past syndrome block (they are not measured). Ancilla lines terminate at measurement symbols.

**[P — PRESENTATION]** Flat vector. Wire lanes: neutral gray. Encoding CNOT controls and targets: Sky Blue `#56B4E9`. Error gate (X on q2): Vermillion `#D55E00`. Syndrome CNOT controls: Blue `#0072B2`; targets: Blue `#0072B2`. Measurement symbols: Orange `#E69F00`. Vertical dividers: light gray dashed. 1 pt strokes throughout. White background. No baked text.

**[E — EXCLUSIONS]** Omit: phase-flip code gates, Hadamard gates, Z-basis measurements on data qubits, classical feedback correction gate, multi-qubit controlled operations beyond CNOT, ancilla reset symbols, time labels.

### BLOCK 3 — NEGATIVE PROMPT

photographic qubit imagery, Bloch sphere representations, 3D chip layout, specific matrix notation baked into gate shapes, classical bit wires below measurement, feedback correction gate, ancilla reset symbols, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Syndrome table: error-to-syndrome mapping

**Heuristic:** VG | **Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a 4-row comparison panel showing the syndrome measurement outcomes for the 3-qubit bit-flip code. Each row contains three qubit circles and two syndrome diamonds arranged horizontally: qubit 1, syndrome diamond M1, qubit 2, syndrome diamond M2, qubit 3. In row 1 (no error), all qubit circles are the same neutral color and both diamonds show the positive outcome. In rows 2, 3, and 4, one qubit circle per row is highlighted to indicate the error location (qubit 1, 2, or 3 respectively), and the syndrome diamonds change color to show the corresponding measurement outcome — positive or negative — for that error. Use color contrast on the diamonds to distinguish positive from negative outcomes, and on the affected qubit circle to show the error location. Each row's four elements are aligned on a shared horizontal axis. No text baked in.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** Four horizontal rows, one per syndrome case: (1) no error → both diamonds positive; (2) error on qubit 1 → M1 negative, M2 positive; (3) error on qubit 2 → both diamonds negative; (4) error on qubit 3 → M1 positive, M2 negative. Each row: three data-qubit circles plus two syndrome diamonds. The error-bearing qubit circle is visually distinct from the others. Each syndrome diamond encodes its ±1 outcome by color fill.

**[O — ORGANIZATION]** Four rows stacked vertically, sharing identical horizontal geometry. Left-to-right within each row: qubit circle 1, diamond M1, qubit circle 2, diamond M2, qubit circle 3. Rows are evenly spaced. A vertical alignment column indicates the error location across rows.

**[P — PRESENTATION]** Flat vector. Unaffected qubit circles: light gray fill. Error qubit circle: Vermillion `#D55E00` fill. Syndrome diamond positive (+1): Bluish Green `#009E73` fill. Syndrome diamond negative (−1): Orange `#E69F00` fill. No-error row: all qubit circles light gray, both diamonds Bluish Green. 1 pt strokes throughout. White background. No baked text.

**[E — EXCLUSIONS]** Omit: the superposition amplitudes α and β, correction gate symbols, ancilla qubit wires, syndrome circuit gates, phase-flip code syndromes, multi-error scenarios.

### BLOCK 3 — NEGATIVE PROMPT

superposition amplitude notation, circuit gate symbols, ancilla wires, phase-flip syndrome rows, multi-qubit error scenarios, Bloch sphere qubit representations, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Surface code lattice: data qubits, syndrome qubits, stabilizer types

**Heuristic:** VG | **Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a square lattice diagram showing the structure of a distance-5 surface code. Place data qubits at the vertices of a 5×5 grid of squares. Place syndrome qubits at the centers of interior faces (plaquette sites) and at edge midpoints along the boundary. Use two distinct shapes for the two stabilizer types: filled squares at plaquette centers for X-stabilizers, and filled circles at star positions for Z-stabilizers. Show one complete plaquette stabilizer by connecting its square symbol to the four surrounding data-qubit vertices with arms indicating the four-qubit interaction. Show one complete star stabilizer similarly. Near one boundary, show the path a logical operator would take — a chain of qubit nodes crossing from one edge to the opposite — indicating the minimum-weight logical operator of length equal to the code distance. Keep the lattice flat and regular. No text baked in.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** A 5×5 surface code (d=5). Data qubits: 25 vertex nodes. Plaquette (X-stabilizer) syndrome qubits: squares at interior face centers, detecting Z errors. Star (Z-stabilizer) syndrome qubits: circles at vertex-adjacent positions on boundary and interior, detecting X errors. One explicitly highlighted plaquette: four arms connecting to its four data-qubit neighbors. One explicitly highlighted star: four arms connecting to its four data-qubit neighbors. One logical operator chain: 5 connected data-qubit nodes crossing the lattice from left boundary to right boundary.

**[O — ORGANIZATION]** Regular 5×5 square lattice. Syndrome qubits fill alternate face and edge positions in a checkerboard pattern. The two highlighted stabilizers (one plaquette, one star) are positioned in the upper-left quadrant and lower-right quadrant to avoid overlap. The logical chain crosses horizontally through the middle row.

**[P — PRESENTATION]** Flat vector. Data qubits: small light-gray filled circles. Plaquette syndrome qubits: Blue `#0072B2` filled squares. Star syndrome qubits: Orange `#E69F00` filled circles. Highlighted plaquette and its four arms: Sky Blue `#56B4E9`, 2 pt strokes. Highlighted star and its four arms: Orange `#E69F00`, 2 pt strokes. Logical chain data qubits: Bluish Green `#009E73` filled circles, connected by Bluish Green line. Lattice edges: light gray, 0.5 pt. White background. No baked text.

**[E — EXCLUSIONS]** Omit: 3D chip layout, superconducting transmon imagery, decoder graph or matching graph overlay, Majorana qubits, boundary conditions beyond what is visible, time-ordered syndrome cycles, classical decoding logic.

### BLOCK 3 — NEGATIVE PROMPT

3D chip architecture rendering, superconducting hardware imagery, decoder matching graph overlay, MWPM algorithm visualization, time-cycle diagrams, Majorana symbols, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Surface code threshold: logical error rate vs. physical error rate (log-log)

**Heuristic:** PQ | **Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a log-log line chart with physical error rate on the horizontal axis and logical error rate on the vertical axis. Show three curves, one each for code distances 3, 5, and 7. All three curves decrease steeply to the left of a vertical reference line and increase to the right of it, so the curves change ordering at the vertical line — to the left the distance-7 curve is lowest; to the right it is highest. The vertical reference line marks the threshold error rate. A single data point sits on or near the distance-7 curve, representing the reported experimental measurement. Horizontal reference lines cross at three evenly spaced log-scale intervals on the vertical axis. The horizontal axis spans from very low error rates to values above the threshold. All axes begin at sensible log-scale minima. No text baked in.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** Log-log plot. Horizontal axis: physical error rate p, spanning approximately 10⁻⁴ to 5×10⁻². Vertical axis: logical error rate p_L, spanning approximately 10⁻²⁰ to 1. Three curves following p_L = A·(p/p_th)^⌈(d+1)/2⌉ with A=0.1, p_th=0.01, for d=3, 5, 7. Vertical threshold line at p=0.01. One filled data-point marker at approximately (0.0047, 0.00143) on the d=7 curve. Three horizontal reference lines at p_L = 10⁻³, 10⁻⁶, 10⁻⁹. Curves cross and re-order at the threshold line. Inferred label positions: d=3 curve highest at far left; d=7 curve lowest at far left and highest at far right.

**[O — ORGANIZATION]** Standard x-y chart frame. Log-scale on both axes. Three continuous curves drawn left to right. Threshold vertical line spans full y-axis range in a distinct style (dashed). Horizontal reference lines span full x-axis range, lighter weight. Data-point marker sits atop the d=7 curve without obstructing it. No legend box in image — typography applied externally.

**[P — PRESENTATION]** Flat vector. d=3 curve: Orange `#E69F00`, 1.5 pt. d=5 curve: Sky Blue `#56B4E9`, 1.5 pt. d=7 curve: Blue `#0072B2`, 1.5 pt. Threshold vertical line: Vermillion `#D55E00`, 1 pt dashed. Horizontal reference lines: light gray, 0.5 pt. Experimental data point: Bluish Green `#009E73` filled circle, 3 pt diameter. Axis frame: neutral gray, 1 pt. White background. No baked text.

**[E — EXCLUSIONS]** Omit: concatenated code curves, individual qubit decay curves, classical simulation curves, decoder performance curves, magic state distillation overhead, any code other than surface code d=3/5/7.

### BLOCK 3 — NEGATIVE PROMPT

concatenated code curves, classical algorithm comparison lines, magic state distillation regions, 3D surface plot of p_L as function of two variables, linear-scale axes, bar chart format, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Fault tolerance vs. error correction: error propagation in syndrome circuits

**Heuristic:** MC | **Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a two-panel comparison showing the difference between a non-fault-tolerant and a fault-tolerant syndrome extraction circuit for a small stabilizer code. In the left panel, show an ancilla qubit connected to three or more data qubits; a single error mark on the ancilla wire propagates via CNOT connections to multiple data qubits, each receiving an error symbol at the output. In the right panel, show a redesigned circuit where the ancilla connects to exactly four data qubits; a single error mark on the ancilla propagates to at most one data qubit. Use directional arrows on the CNOT connections to show the direction of potential error propagation. A visible contrast — multiple error marks in the left panel versus one error mark in the right — communicates the structural difference. No text baked in.

### BLOCK 2 — FULL SCOPE

**[S — SPECIFICATION]** Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

**[C — CONTENT]** Two-panel horizontal comparison. Left panel: non-fault-tolerant circuit — one ancilla wire connected via CNOTs to five or more data qubit wires; a single error (X or Z mark) placed on the ancilla input propagates to four or more data qubits at the output, shown as error marks on those wires. Right panel: fault-tolerant surface code circuit — one ancilla wire connected via CNOTs to exactly four data qubit wires; same single ancilla error mark propagates to exactly one data qubit error mark. The physical code (distance ≥ 3) can still correct one data qubit error but not four — this is the visual argument.

**[O — ORGANIZATION]** Side-by-side panels with identical left-edge alignment. Each panel: vertical ancilla wire (horizontal or vertical convention consistent across panels), CNOT connections branching to data qubit wires, error marks as filled X symbols, output data qubit error marks at right/bottom edge. Left panel wider to accommodate more CNOT connections. Vertical dashed divider separating the two panels.

**[P — PRESENTATION]** Flat vector. Data qubit wires: light gray. Ancilla wire: Sky Blue `#56B4E9`. CNOT gates: Blue `#0072B2` filled controls and open-circle targets. Error mark on ancilla: Vermillion `#D55E00` filled X shape, 2 pt. Propagated error marks on data qubits: Vermillion `#D55E00` filled X shapes, smaller. Uncorrupted data qubit wire endpoints (right panel): Bluish Green `#009E73` filled circles. Divider: light gray dashed. 1 pt strokes. White background. No baked text.

**[E — EXCLUSIONS]** Omit: classical feedback logic, decoder graph, full surface code lattice, specific gate counts beyond CNOT, ancilla reset operations, Steane code or other specific code geometry beyond what is needed to show the propagation contrast.

### BLOCK 3 — NEGATIVE PROMPT

classical feedback arrows, decoder matching graph, full surface code lattice overlay, Steane code geometry, ancilla reset symbols, 3D circuit box rendering, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Digitization of continuous errors onto the Pauli basis**
STATIC SUFFICIENT. The linear decomposition relationship is spatial, not temporal. The diagram captures the full structure in a single layout.

**Figure 2 — 3-qubit bit-flip code: encoding circuit and syndrome extraction**
VIDEO CANDIDATE — Criterion: ≥3 sequential causal stages (encode → error → syndrome measurement with ancilla entanglement → measurement collapse → correction) where each stage causally depends on the previous and the causal chain is the learning target. A step-by-step animation showing qubit state changes at each stage would clarify how syndrome measurement extracts parity without disturbing the logical superposition — the single hardest conceptual step in the chapter.

**Recommendation: Figure 2 is the one video for this chapter.**

**Figure 3 — Syndrome table: error-to-syndrome mapping**
STATIC SUFFICIENT. The table structure is the content; simultaneous comparison across rows is the pedagogical move, and a static four-row panel serves this better than sequential animation.

**Figure 4 — Surface code lattice**
STATIC SUFFICIENT. The geometry is spatial. The stabilizer types and the logical chain path are visible in a single frame.

**Figure 5 — Surface code threshold (log-log)**
STATIC SUFFICIENT. The crossing of curves is a static relationship. The draggable cursor in the +1 simulation handles the interactive exploration; the figure itself needs only to show the ordering reversal at threshold.

**Figure 6 — Fault tolerance vs. error correction: error propagation**
STATIC SUFFICIENT. The two-panel contrast communicates the structural difference in a single comparison frame.
