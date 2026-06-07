# CAJAL Figure Intelligence — 01-mixed-states-and-the-density-matrix

**Source:** books/quantum-mechanics-vol4/chapters/01-mixed-states-and-the-density-matrix.md
**Scan mode:** /scan silent
**Date:** 2026-06-06

---

## Zones Detected

**MC — Mechanism/Process (3+ interdependent steps)**

- Partial trace procedure (Worked Example): expand joint Bell-state outer product → apply basis projectors for qubit B → sum terms to collect only A-operators → obtain maximally mixed reduced density matrix. Four algebraically coupled steps; each depends on the output of the previous.
- Decoherence as Bloch vector shrinkage (Interpretation section): pure state on Bloch surface → qubit entangles with environment → partial trace over environment → Bloch vector contracts inward to mixed interior. Three causal stages in direct sequence.

**VG — Verification Gap (structural/spatial claims not visually grounded)**

- Bloch ball interior for mixed states: the chapter asserts "pure states sit on the surface… intermediate mixed states fill the interior… maximally mixed state is the center" and gives purity = ½(1 + |r|²), directly tying scalar purity to Bloch vector length. No figure grounds this three-region spatial claim.
- Decomposition non-uniqueness: the chapter states the set of density operators is convex and that mixtures of density operators are density operators, implying multiple distinct ensembles can share one density matrix. This structural claim — that two physically different preparation procedures map to the same point in the Bloch ball — is asserted in prose but never shown geometrically.

**PQ — Proportional/Quantitative Data**

- Purity range: 1 (pure, surface) to 1/2 (maximally mixed, center) for a qubit. Specific numerical values tied to a geometric scale. Chartable, but most naturally rendered as a radial annotation on the Bloch ball figure rather than a standalone chart.
- Lab scenario purity: Tr(ρ²) = 3/4, explicitly computed. Locates a specific interior point; handled within the Bloch ball figure.

---

**Density recommendation: 3 figures, Mixed density.**

---

## Figure 1 — CRITICAL

**Concept:** The Bloch ball encodes pure states on its surface at |r| = 1, all mixed states in its interior, and the maximally mixed state at its center at |r| = 0; purity equals ½(1 + |r|²), so the Bloch vector length directly measures how mixed a state is.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background. Render a circle (the equatorial cross-section of the Bloch ball) with a 1 pt #000000 outline, no fill. Draw a thin dashed 1 pt #000000 vertical line from the bottom of the circle to the top as the quantization axis. Place a 5 pt filled circle at the top of the vertical axis in #0072B2, a 5 pt filled circle at the bottom in #0072B2, and a 5 pt filled circle at the center of the circle in #D55E00. Place a 5 pt filled circle at approximately 55% of the radius toward the upper-right quadrant in #009E73. Draw a solid 1 pt #009E73 arrow from the center to this upper-right marker as the Bloch vector r. Draw a thin 1 pt #000000 bracket spanning from the center to the circle boundary along the radial direction of the Bloch vector, indicating the scale |r| runs from 0 to 1. Add no other shapes. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, flat 2D equatorial cross-section of the Bloch ball represented as a unit circle.

[C] Content confirmed in chapter: pure states at surface |r| = 1 (e.g., |0⟩ at north pole, |1⟩ at south pole); maximally mixed state ρ = I/2 at center |r| = 0; generic mixed states fill the interior; Bloch vector r drawn from center to state; purity = ½(1 + |r|²) equals 1 on surface and 1/2 at center; decoherence moves state inward. Three distinct markers: two pure-state points on vertical axis (#0072B2), one maximally mixed center point (#D55E00), one interior mixed-state point with Bloch vector (#009E73).

[O] Single circle. Vertical dashed axis. Three marker types at their correct geometric positions. One radial Bloch vector arrow from center to interior mixed-state point. One bracket showing the |r| = 0 to |r| = 1 scale on the radial line. No other geometry.

[P] Flat vector, Okabe-Ito hexes only: circle boundary and axis #000000, pure-state markers #0072B2, maximally mixed center #D55E00, generic mixed-state marker and Bloch vector #009E73. All strokes 1 pt. No fills other than solid point markers. White background. Unannotated.

[E] Explicit exclusions: 3D sphere rendering or any three-quarter perspective; latitude/longitude grid lines on sphere surface; additional labeled equatorial poles (|+⟩, |−⟩, |+y⟩); density matrix numerical entries anywhere in image; eigenvalue arrows; decoherence trajectory arrows or spiral paths; Wigner function; phase space representation; quantum circuit symbols; legend box; purity bar chart; y-axis of any kind; axes labeled Rx Ry Rz.

---

**Block 3 — Negative Prompt**

3D sphere, globe, three-quarter perspective, latitude/longitude grid, equatorial poles labeled |+⟩ |−⟩, density matrix entries shown as text, eigenvalue arrows, decoherence spiral trajectories, Wigner function, phase space, circuit gate symbols, legend box, purity bar chart, axes labeled Rx Ry Rz; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 2 — CRITICAL

**Concept:** The partial trace procedure discards one subsystem of a pure entangled two-qubit joint state through a three-step sequence — expand, project, sum — yielding a maximally mixed reduced density matrix for the remaining subsystem, with the Bloch vector collapsing to the center.

---

**Block 1 — Illustrae Paste Block**

Draw a full-width 120 mm vector canvas, white background, divided into three equal vertical panels separated by thin 0.5 pt #000000 dashed rules. Panel 1 (left): draw two small horizontal ovals side by side, the left oval outlined in #0072B2 (qubit A) and the right oval outlined in #E69F00 (qubit B), connected by a thin 1 pt #000000 line; above them draw a small 5 pt filled #0072B2 circle on the circumference of a thin-stroke 1 pt #000000 unit circle, representing a pure state on the Bloch surface. Panel 2 (center): draw the same two ovals now linked by a curved double-arc connector in #56B4E9 indicating entanglement between A and B; overlay a diagonal cross-hatch pattern in light gray over the #E69F00 B oval, indicating B is being traced out. Panel 3 (right): draw only the #0072B2 A oval; below it draw a small 1 pt #000000 unit circle with a 5 pt filled #D55E00 circle at its center, representing the maximally mixed reduced state. Draw a right-pointing 1 pt #000000 arrow between panels 1 and 2, and another between panels 2 and 3. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Full-width 120 mm vector, white background, three-panel horizontal layout showing the partial trace sequence from left to right.

[C] Content confirmed in chapter: two qubits A and B begin in the Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2, a pure joint state with surface Bloch vectors; partial trace Tr_B(ρ_AB) sums over basis states {|0⟩_B, |1⟩_B}; off-diagonal terms vanish because ⟨0|1⟩ = 0; result is ρ_A = I/2, maximally mixed, with Bloch vector at center; purity drops from 1 to 1/2.

[O] Panel 1: joint system A+B as two connected ovals, Bloch-surface point indicating pure joint state. Panel 2: entanglement arc connecting A and B, crosshatch over B indicating trace-out operation in progress. Panel 3: only A oval remains, Bloch-center point indicating maximally mixed result. Directional arrows between panels. Left-to-right process flow only.

[P] Flat vector, Okabe-Ito hexes only: qubit A oval #0072B2, qubit B oval #E69F00, entanglement arc #56B4E9, B crosshatch light gray, process arrows #000000, Bloch surface point #0072B2, Bloch center point #D55E00. All strokes 1 pt. White background. Unannotated.

[E] Explicit exclusions: density matrix numerical entries or matrix grids; Dirac bra-ket text notation; 3D Bloch sphere rendering; environment E system as a third subsystem; decoherence bath elements; measurement apparatus or detector symbols; circuit gate boxes (H, CNOT); Schmidt decomposition arrows; entanglement entropy value annotations; teleportation protocol elements; more than two subsystems; all four Bell states (only |Φ+⟩ is the chapter example).

---

**Block 3 — Negative Prompt**

Density matrix numerical entries, matrix grid, Dirac notation text, 3D Bloch sphere, environment bath, third subsystem, detector apparatus, circuit gate boxes, Schmidt decomposition, entanglement entropy labels, teleportation elements, all four Bell states shown simultaneously; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 3 — IMPORTANT

**Concept:** Two geometrically distinct preparation procedures — equal mixture of |0⟩ and |1⟩ versus equal mixture of |+⟩ and |−⟩ — map to the same point at the Bloch ball center, demonstrating that the density matrix representation is not unique to a single physical preparation.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background, two equal-width panels side by side separated by a thin 0.5 pt #000000 dashed vertical line, with a horizontal 1 pt #000000 double-ended equality marker centered between the panels and spanning the divider. Left panel: a unit circle outline in 1 pt #000000, a thin dashed 1 pt #000000 vertical axis, two 5 pt filled #0072B2 circles at the north pole and south pole of the vertical axis (representing |0⟩ and |1⟩), a thin 1 pt #000000 dashed line connecting them through the origin, and a 5 pt filled #D55E00 circle at the origin (their midpoint). Right panel: a unit circle outline in 1 pt #000000, a thin dashed 1 pt #000000 horizontal axis, two 5 pt filled #009E73 circles at the left and right intersections of the horizontal axis with the circle boundary (representing |+⟩ and |−⟩), a thin 1 pt #000000 dashed line connecting them through the origin, and a 5 pt filled #D55E00 circle at the origin (their midpoint, the same point as the left panel). No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, two equal-width panels side by side with equality marker between them.

[C] Content confirmed in chapter: pure states |0⟩ (north pole, r = (0,0,1)) and |1⟩ (south pole, r = (0,0,−1)) mix equally to give ρ = I/2 at center; pure states |+⟩ (r = (1,0,0)) and |−⟩ (r = (−1,0,0)) mix equally to give ρ = I/2 at center; both mixtures produce the same density operator; the set of density operators is convex.

[O] Left panel: vertical-axis pair of surface points with dashed midpoint line to shared center. Right panel: horizontal-axis pair of surface points with dashed midpoint line to same shared center. Center equality marker between panels. Both panels share identical unit circle boundary and identical center point color (#D55E00). No other geometry.

[P] Flat vector, Okabe-Ito hexes only: circle boundaries and axes #000000, left-panel z-axis pure states #0072B2, right-panel x-axis pure states #009E73, both center maximally mixed points #D55E00. All strokes 1 pt. White background. Unannotated.

[E] Explicit exclusions: y-axis or any three-dimensional ball rendering; more than two preparation procedures or panels; purity calculation values or bars; eigenvalue display; additional intermediate mixture states beyond the two endpoints per panel; Bloch vector arrow (the dashed line is a midpoint connector, not a vector); third or fourth decomposition comparison; quantum circuit elements; density matrix numerical entries.

---

**Block 3 — Negative Prompt**

3D sphere, y-axis, third decomposition panel, purity bars, eigenvalue annotations, Bloch vector arrow, additional mixture states, circuit elements, density matrix number entries; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 (Bloch ball cross-section):** Not a video candidate. The learning target is spatial reading of purity from Bloch vector length — a static geometric relationship that a still figure communicates fully.

**Figure 2 (Partial trace sequence):** Not a video candidate. Three panels communicate the causal steps without temporal animation adding interpretive value; the transformation is algebraic, not kinematic.

**Decoherence as Bloch vector contraction (discussed in Interpretation section, not a standalone figure above):** VIDEO CANDIDATE. The learning target is the contraction mechanism itself — a continuous, directional process below direct observation in which a pure-state surface point spirals or drifts inward toward the maximally mixed center as environmental coupling grows. Time-axis motion here is the concept, not a convenience. A 4-second loop: #0072B2 point starts on circle surface, traces a smooth inward path to the #D55E00 center, pauses one second, resets. Flat 2D projection, Okabe-Ito colors.

**Video candidate count: 1 (decoherence Bloch vector contraction). Recommendation: 4-second loop on the Bloch ball cross-section — surface point (#0072B2) contracts to center (#D55E00) under simulated decoherence, with trajectory trace in #E69F00. Looping. No text.**
