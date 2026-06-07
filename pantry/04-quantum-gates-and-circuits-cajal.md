# CAJAL Figure Intelligence — 04-quantum-gates-and-circuits

**Source:** books/quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md
**Scan mode:** /scan silent
**Date:** 2026-06-06

---

## Zones Detected

**MC — Mechanism/Process (3+ interdependent steps)**

- Bell-state preparation circuit (Worked Example 1): Step 0 — both qubits |00⟩, Bloch vectors at north pole, product state; Step 1 — H⊗I maps qubit 0 to |+⟩ at +x equator, qubit 1 unchanged, still product; Step 2 — CNOT with superposed control creates |Φ+⟩, both reduced Bloch vectors collapse to center (maximally mixed). Three causally ordered steps, each dependent on the previous.
- Deutsch algorithm phase-kickback mechanism (Worked Example 2): Step 0 — |0⟩|1⟩ initial; Step 1 — H⊗H produces |+⟩|−⟩; Step 2 — oracle Uf kicks function value back as a phase on the query register, ancilla unchanged; Step 3 — H on query converts relative phase to distinguishable amplitude; measurement gives outcome. Four steps, each algebraically required for the next.

**VG — Verification Gap (structural/spatial claims not visually grounded)**

- Single-qubit gates as Bloch-sphere rotations: the chapter explicitly states "every single-qubit unitary is a rotation of the Bloch sphere," defines X as π-rotation about x̂, Z as π-rotation about ẑ, H as π-rotation about (x̂ + ẑ)/√2, S as π/2 about ẑ, T as π/4 about ẑ. These spatial rotation claims are never illustrated.
- Universal gate set nesting structure: the chapter draws a sharp distinction between the Clifford group {H, S, CNOT} (classically simulable, Gottesman-Knill) and {H, T, CNOT} (universal), with T as the non-Clifford resource that breaks classical simulability. This set-containment structure is stated in prose only.
- CNOT action topology: the matrix and XOR formula describe what CNOT does, but the circuit wire topology (control dot, target ⊕, conditional flip) and the transition from product-state control to entangled output are not shown as a spatial wiring diagram.

**PQ — Proportional/Quantitative Data**

- Gate fidelity values mentioned (99.9% single-qubit, 99–99.9% two-qubit on different platforms, 2024–2025 hardware). These are comparison values suitable for a bar chart. However, the chapter presents them as a single sentence of context, not as a data table; a figure would over-represent their pedagogical weight. Skip.
- Grover speedup O(N) vs. O(√N) and Shor speedup (sub-exponential vs. polynomial) are stated in the chapter. These are genuinely chartable order-of-magnitude comparisons with a zero-based y-axis. Yield a figure.

---

**Density recommendation: 4 figures, Mixed density.**

---

## Figure 1 — CRITICAL

**Concept:** Every standard single-qubit gate acts as a specific rotation of the Bloch sphere: X, Y, Z are π-rotations about their named axes; H is a π-rotation about the diagonal (x̂ + ẑ)/√2 axis swapping x and z; S is a π/2 rotation about ẑ; T is a π/4 rotation about ẑ.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background. Render a circle (the 2D Bloch cross-section, xz-plane) with a 1 pt #000000 outline, no fill. Draw a thin 1 pt #000000 dashed vertical z-axis and a thin 1 pt #000000 dashed horizontal x-axis crossing at the center. Place 4 pt filled #000000 circles at the north pole (|0⟩), south pole (|1⟩), positive x-axis, and negative x-axis. Draw five rotation arcs, each as a single-headed curved arrow at 1.5 pt weight: X-arc in #D55E00 sweeping from north pole to south pole along the circle perimeter (π-rotation about x); Z-arc in #0072B2 as a short right-pointing arc near the north pole indicating rotation about z; H-arc in #009E73 as a curved arc from the north pole to the positive x-axis position indicating the diagonal-axis rotation; S-arc in #E69F00 as a shorter right-pointing arc about z (half of Z-arc length); T-arc in #CC79A7 as the shortest right-pointing arc about z (half of S-arc length). Ensure no arcs overlap; stagger radii slightly. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, flat 2D xz-plane cross-section of the Bloch ball showing gate rotation arcs.

[C] Content confirmed in chapter: X is π-rotation about x̂ — swaps |0⟩ (north) and |1⟩ (south); Z is π-rotation about ẑ — phase flip; H is π-rotation about (x̂ + ẑ)/√2 — maps north to +x and swaps x- and z-axes; S is π/2 rotation about ẑ, S² = Z; T is π/4 rotation about ẑ, T² = S. Six anchor points on circle: north and south poles on z-axis, ±x-axis intersections. Five distinct gate arcs with the correct sweep angle and rotation axis for each.

[O] Single circle. Dashed z-axis vertical, x-axis horizontal. Four anchor point markers (|0⟩, |1⟩, +x, −x). Five arc arrows, each at a distinct Okabe-Ito color, with arc length proportional to rotation angle (T < S < Z for z-axis rotations; X and H cross-equatorial). Arcs staggered in radius to prevent overlap. Left-to-right or shortest-path sweep direction consistent with the matrix definitions.

[P] Flat vector, Okabe-Ito hexes only: circle boundary and axes #000000, X-arc #D55E00, Z-arc #0072B2, H-arc #009E73, S-arc #E69F00, T-arc #CC79A7. Anchor markers #000000 solid 4 pt circles. All arcs 1.5 pt. All other strokes 1 pt. White background. Unannotated.

[E] Explicit exclusions: Y-gate arc (Y is π about ŷ, which lies out of the xz-plane shown; do not fabricate a yz-plane projection); 3D sphere or three-quarter perspective; interior Bloch vectors for mixed states; density matrix display; global phase annotation; Euler-angle decomposition axes; CNOT or two-qubit gate elements; continuous Rx Ry Rz rotation family; numerical matrix entries; R_n(α) formula text; circuit wire symbols.

---

**Block 3 — Negative Prompt**

Y-gate arc, 3D sphere, three-quarter perspective, interior mixed-state Bloch vector, density matrix, global phase annotation, Euler decomposition, CNOT elements, two-qubit wires, Rx Ry Rz family, matrix number entries, circuit wire symbols; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 2 — CRITICAL

**Concept:** The H-CNOT Bell-state preparation circuit proceeds in three causally ordered steps — |00⟩ product state → H creates superposition on qubit 0 only → CNOT entangles both qubits and collapses both Bloch vectors to the center.

---

**Block 1 — Illustrae Paste Block**

Draw a full-width 120 mm vector canvas, white background. Draw two parallel horizontal wires 12 mm apart, running left to right, representing qubit 0 (upper) and qubit 1 (lower). Divide the timeline into three stages separated by thin 0.5 pt #000000 dashed vertical rules. At stage 0 (left): place two small 18 mm-diameter unit circles on each wire, each with a 1 pt #000000 outline and a single 4 pt filled #0072B2 circle at the top of each small circle (north pole marker, indicating |0⟩). Between stage 0 and stage 1, draw a 7×5 mm rectangle on the upper wire in #009E73 with 1 pt outline representing the H gate. At stage 1 (center): qubit-0 small circle has its #0072B2 marker at the rightmost point (equator, +x, indicating |+⟩); qubit-1 small circle still has its marker at the north pole. Between stage 1 and stage 2: draw a 4 pt filled #0072B2 control dot on the upper wire and a 7 mm diameter circle outline #0072B2 with an internal cross (+) on the lower wire, connected by a thin vertical 1 pt #0072B2 line (CNOT symbol). At stage 2 (right): both small circles have their markers as 4 pt filled #D55E00 circles at the center of each small circle (origin, indicating maximally mixed reduced states). No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Full-width 120 mm vector, white background, two-wire horizontal quantum circuit with Bloch-sphere state icons at three time steps.

[C] Content confirmed in chapter: Step 0 — |00⟩ initial state, both Bloch vectors at north pole, product state; Step 1 — H⊗I applied to qubit 0, qubit-0 Bloch vector moves to +x equator, qubit-1 unchanged at north pole, state still factorizes; Step 2 — CNOT with qubit 0 as control, qubit 1 as target; output is |Φ+⟩ = (|00⟩ + |11⟩)/√2, both reduced Bloch vectors collapse to origin. Gate symbols: H rectangle on qubit-0 wire; CNOT with filled-dot control and ⊕-circle target.

[O] Two parallel horizontal wires. Three time-stage columns separated by dashed rules. Small Bloch-cross-section icons at each stage-wire intersection showing state of that qubit. H gate box between stages 0 and 1 on upper wire. CNOT symbol spanning both wires between stages 1 and 2. State progression: north (both) → +x equator (q0), north (q1) → center (both). All flow strictly left to right.

[P] Flat vector, Okabe-Ito hexes only: wires #000000, H gate box #009E73, CNOT control dot and ⊕ symbol and connecting wire #0072B2, north-pole state markers #0072B2, maximally mixed center markers #D55E00, stage separator rules light gray dashed. All strokes 1 pt, gate box outline 1 pt. White background. Unannotated.

[E] Explicit exclusions: all four Bell states in one figure (this figure shows |Φ+⟩ preparation only); amplitude or probability labels; purity values; density matrix entries; Y Z S T Rz gate symbols; three-qubit or multi-qubit register; Deutsch algorithm elements; Bloch sphere rotation arcs (those belong to Figure 1); global phase; entanglement entropy value; circuit ancilla qubits.

---

**Block 3 — Negative Prompt**

All four Bell states simultaneously, amplitude bar charts, purity values, density matrix entries, Y Z S T gate symbols, three-qubit registers, Deutsch algorithm, Bloch rotation arcs, global phase annotation, entanglement entropy labels, ancilla qubit wires; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 3 — IMPORTANT

**Concept:** The Clifford group {H, S, CNOT} is classically simulable (Gottesman-Knill); adding the T gate produces the universal set {H, T, CNOT} that generates a dense subgroup of all unitaries; T is the non-Clifford resource that breaks classical simulability.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background. Draw three concentric rounded rectangles as nested regions. The innermost rounded rectangle has a 1 pt #56B4E9 outline with a 10% #56B4E9 fill tint. Inside it, draw three small 6×4 mm gate-symbol rectangles in 1 pt #0072B2 outline: one for H, one for S, one for CNOT (represented as the filled-dot-plus-⊕-target symbol pair). The middle rounded rectangle has a 1 pt #009E73 outline with no fill. In the annular gap between inner and middle rectangles, draw one small 6×4 mm gate-symbol rectangle in 1.5 pt #E69F00 outline for the T gate, positioned to make clear it is outside the Clifford group but inside the universal set. The outermost rounded rectangle has a 1 pt #0072B2 dashed outline. The three regions are centered and uniformly spaced with 8 mm margins between nested boundaries. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, three concentric rounded-rectangle nested regions.

[C] Content confirmed in chapter: Clifford group generated by {H, S, CNOT} — efficiently simulable classically by Gottesman-Knill theorem; universal gate set {H, T, CNOT} adds T to the Clifford group; T is π/4 rotation about ẑ, T² = S, described as providing non-Clifford computational power; the set {H, T} generates a dense subgroup of SU(2); Solovay-Kitaev theorem guarantees efficient approximation to arbitrary precision.

[O] Innermost region: Clifford generators H, S, CNOT as gate symbols. Middle annular gap: T gate symbol, positioned clearly outside the innermost boundary. Outermost region: represents the full unitary space SU(2^n). Three concentrically nested regions — inner inside middle inside outer. No other elements.

[P] Flat vector, Okabe-Ito hexes only: innermost region #56B4E9 outline and 10% fill tint, H/S/CNOT gate boxes #0072B2, T gate box #E69F00 at 1.5 pt (distinct weight to indicate resource status), middle boundary #009E73 solid 1 pt, outer boundary #0072B2 dashed 1 pt. White background. Unannotated.

[E] Explicit exclusions: Toffoli gate; magic state distillation circuit; T-gate count histogram; Euler-angle decomposition; BQP/NP/PSPACE complexity hierarchy; hardware platform icons; continuous Rx Ry Rz gate family; individual qubit fidelity numbers; error-correction code structure; qubit wire diagram inside the nesting diagram; Grover or Shor algorithm symbols.

---

**Block 3 — Negative Prompt**

Toffoli gate, magic state distillation circuit, T-count histogram, Euler decomposition, BQP/NP/PSPACE diagram, hardware platform icons, Rx Ry Rz gates, fidelity numbers, error-correction structure, qubit wire inside nesting diagram, Grover/Shor algorithm symbols; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 4 — SUPPLEMENTARY

**Concept:** Grover's algorithm achieves O(√N) query complexity vs. the classical O(N) for search (quadratic speedup), and Shor's algorithm achieves polynomial O(n² log n) vs. sub-exponential classical for factoring (exponential speedup) — both speedups visualized as grouped bars with y-axis at zero.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background. Draw a horizontal x-axis in 1 pt #000000 at the bottom of the panel with a vertical y-axis in 1 pt #000000 at the left, y-axis starting at zero, no 3D. Draw two groups of two vertical bars each. Left group (search problem): classical bar in #E69F00 reaching height 72 pt; quantum (Grover) bar in #009E73 reaching height 36 pt (representing O(N) vs. O(√N) approximately — a 2:1 ratio for illustration). Right group (factoring problem): classical bar in #E69F00 reaching height 108 pt, clipped at 90 pt with a 2 pt #D55E00 zigzag break mark at the top to indicate the bar extends beyond the plot area; quantum (Shor) bar in #009E73 reaching height 28 pt (representing the far smaller polynomial scaling). Within each group, bars are 10 mm wide, spaced 3 mm apart; the two groups are separated by 14 mm. Draw thin 0.5 pt #000000 horizontal dashed grid lines at y = 36 pt and y = 72 pt. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, grouped vertical bar chart with y-axis starting at zero.

[C] Content confirmed in chapter: Grover search — classical O(N), quantum O(√N), described as quadratic speedup; Shor factoring — classical sub-exponential (best classical algorithm), quantum polynomial O(n² log n log log n), described as exponential speedup. Two problem pairs: search and factoring. Classical bars taller than quantum bars in both groups; Shor's classical-to-quantum ratio much larger than Grover's.

[O] Two grouped bar pairs on a shared x-axis. Left group: search problem, classical bar and Grover bar. Right group: factoring problem, classical bar (clipped with break mark) and Shor bar. Y-axis starts at zero. Break mark on classical factoring bar indicates off-chart height. Horizontal dashed reference lines at representative heights. Quantum bars in both groups shorter than classical counterparts.

[P] Flat vector, Okabe-Ito hexes only: classical bars #E69F00, quantum bars #009E73, break mark #D55E00, axes #000000, grid lines 0.5 pt #000000 dashed. All bar outlines 1 pt. White background. Unannotated.

[E] Explicit exclusions: Grover amplitude amplification circuit; QFT circuit for Shor; error-correction overhead bars; T-gate count; post-quantum cryptography context; Deutsch-Jozsa comparison; 3D bar relief; logarithmic y-axis; pie chart form; any fourth algorithm bar; BQP/NP complexity boundary diagram; specific numerical labels baked onto bars or axes.

---

**Block 3 — Negative Prompt**

Grover diffusion circuit, QFT circuit, error-correction overhead, T-count, post-quantum cryptography elements, Deutsch-Jozsa bars, 3D bar relief, logarithmic y-axis, pie chart form, fourth algorithm, BQP/NP diagram, numerical labels baked onto bars; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 (Bloch sphere gate rotations):** Not a video candidate. Six rotation arcs on a static circle are simultaneous reference material, best compared side-by-side rather than animated sequentially.

**Figure 2 (Bell-state preparation circuit):** VIDEO CANDIDATE. Criterion: three sequential causal stages where the transition mechanism — specifically the Bloch vector collapse from surface to origin at the CNOT step — is the learning target. The instantaneous collapse of both reduced-state Bloch vectors when CNOT is applied to a superposed control is the chapter's central claim about entanglement creation. Animation of the Bloch vector icon for qubit 0 moving from north pole to +x equator (H step), then both vectors simultaneously shrinking to the origin (CNOT step), directly embeds the pedagogical surprise. A static three-panel figure communicates the outcome; animation communicates the transformation itself.

**Figure 3 (Universal gate set nesting):** Not a video candidate. A nested-set diagram is static spatial structure; no transformation unfolds over time.

**Figure 4 (Query complexity bars):** Not a video candidate. A bar chart is a static comparison; no sequential mechanism is the learning target.

**Video candidate count: 1 (Bell-state preparation Bloch vector collapse). Recommendation: 5-second loop — qubit-0 Bloch vector moves from north pole to +x equator under H (1.5 s), then both Bloch vectors contract simultaneously to origin under CNOT (1.5 s), pause (1 s), reset. Flat 2D Bloch cross-section, Okabe-Ito colors, no text.**
