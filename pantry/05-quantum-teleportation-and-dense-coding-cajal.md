# CAJAL Figure Report — Chapter 5 — Quantum Teleportation and Dense Coding

Recommended: 5 figures, Mechanistic density.

---

## Figure 1 — Teleportation Protocol: Three-Qubit Mechanism Flowchart

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a five-stage horizontal mechanism diagram with three horizontal qubit wires running left to right: qubit S (Alice's source, top), qubit A (Alice's Bell-pair half, middle), qubit B (Bob's Bell-pair half, bottom). Stage zero: qubit S shown as a general Bloch sphere icon (surface point, indicating unknown pure state ψ); qubits A and B shown as a paired entangled icon (double-arc connecting them, indicating the pre-shared Bell pair). Stage one: a CNOT gate symbol spanning the S and A wires (filled dot on S, ⊕ on A). Stage two: an H gate box on the S wire. Stage three: two measurement boxes on the S and A wires; two dashed lines (classical channel) descend from these measurement boxes to a telephone handset icon below; a downward arrow from the telephone to qubit B's wire. Stage four: a correction gate box on the B wire (with a quadrant-divided box icon indicating one of four possible gates: I, X, Z, ZX). Final output: qubit B's Bloch sphere icon matches the original qubit S icon from stage zero (same surface point). A horizontal double-line below qubit A and B wires from stage zero onward indicates their pre-shared entangled status. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Five-stage sequential mechanism: (0) initial: S in unknown state ψ, AB as pre-shared |Φ⁺⟩; (1) CNOT on S→A; (2) H on S; (3) Alice measures S and A in computational basis, sends 2-bit classical result to Bob via classical channel (dashed lines, phone icon); (4) Bob applies one of {I, X, Z, ZX} correction to B, result is ψ. Qubit S post-measurement: shown as collapsed to a definite basis state (no longer carrying ψ). B post-correction: matches original ψ. Classical channel explicitly shown as distinct (dashed) from quantum wire. Pre-shared entanglement between A and B marked by double-arc at the input.

`[O — ORGANIZATION]` Three parallel horizontal wires (S top, A middle, B bottom). Time flows left to right. Five vertical time slices separated by light dashed vertical rules. Gate symbols placed on appropriate wires. Measurement and classical-channel elements at stage 3. Correction gate at stage 4 on B wire. Telephone icon centered below stages 3–4 as classical communication node. Bloch sphere icons at stages 0 and 4 on wires S and B respectively.

`[P — PRESENTATION]` Flat vector; S wire = Blue #0072B2; A wire = Sky Blue #56B4E9; B wire = Bluish Green #009E73; pre-shared entanglement arc = Reddish Purple #CC79A7; CNOT and H gate boxes = Blue #0072B2; measurement boxes = Orange #E69F00; classical-channel dashed lines = Orange #E69F00; phone icon = Orange #E69F00; correction gate box = Bluish Green #009E73; Bloch sphere icons = matching wire color; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: matrix derivation of the four conditional states; dense coding protocol (separate figure); no-cloning proof structure; no-signaling proof derivation; Bell state labels; specific α, β amplitude values; FTL signaling context.

**BLOCK 3 — NEGATIVE PROMPT:** matrix grid, amplitude bar chart, probability distribution, energy levels, all-four-branches detail panel, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Four Measurement Outcomes and Bob's Correction Gates

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-by-two grid of panels, one panel per measurement outcome (zero-zero, zero-one, one-zero, one-one). Each panel contains: a small two-bit outcome indicator (top-left of panel), a Bloch sphere icon showing Bob's conditional state before correction (surface point at a specific position depending on the case — outcome zero-zero at the original ψ position, outcome zero-one at a flipped position, outcome one-zero at a phase-flipped position, outcome one-one at a combined flip), and a gate symbol (I, X, Z, or ZX respectively) shown as a directed transformation arrow pointing from the pre-correction Bloch vector to the post-correction position. The post-correction Bloch sphere icon is shown as a small sphere alongside or below each panel with the vector at the same target ψ position in all four cases — indicating convergence to a single final state. A thin border connects all four post-correction spheres with a bracket or arc indicating they share the same outcome ψ. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` 2×2 grid: (00) → identity correction I, Bob's state = ψ already; (01) → X correction, Bob's state = X|ψ⟩ before; (10) → Z correction, Bob's state = Z|ψ⟩ before; (11) → ZX correction, Bob's state = XZ|ψ⟩ before. Each panel: pre-correction Bloch sphere (surface point at the relevant transformed position) and post-correction Bloch sphere (all four converge to same point ψ). Correction gate symbol shown as transformation operator. Outcome indicator (2-bit pattern) as a two-cell box. All four final states identical — shown by shared visual motif. All cases derived directly from chapter's step-by-step worked example.

`[O — ORGANIZATION]` 2×2 panel grid with equal cell sizes. Within each cell: outcome indicator top-left, pre-correction sphere left, gate arrow center, post-correction sphere right. Shared convergence motif (bracket or arc) connects four post-correction spheres along the bottom edge of the grid. Panels separated by thin rules. Each cell independently self-contained.

`[P — PRESENTATION]` Flat vector; outcome-00 panel = Sky Blue #56B4E9 (light border); outcome-01 panel = Orange #E69F00 (light border); outcome-10 panel = Reddish Purple #CC79A7 (light border); outcome-11 panel = Bluish Green #009E73 (light border); pre-correction Bloch vectors = Orange #E69F00; post-correction Bloch vectors = Bluish Green #009E73; gate arrows = Blue #0072B2; convergence bracket = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: teleportation circuit diagram (Figure 1); dense coding encoding; no-cloning argument; reduced density matrix calculation; numerical amplitude values α, β; the specific state |+⟩ as the test state — generic ψ position only; ZX vs XZ ordering ambiguity (resolved in text).

**BLOCK 3 — NEGATIVE PROMPT:** amplitude bar chart, full three-qubit circuit, truth table grid, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Dense Coding: Encoding Map and Bell-State Wheel

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a hub-and-spoke diagram. At the center, place a shared Bell pair icon representing the pre-shared |Φ⁺⟩ resource (two interlocked circles or a double-arc connecting two qubit circles). From the center, draw four outward spokes, each ending in a distinct node. Each node contains: a two-qubit amplitude bar chart (four bars representing the amplitudes of |00⟩, |01⟩, |10⟩, |11⟩ for that Bell state) and a small gate symbol indicating which Pauli Alice applies to reach that Bell state from |Φ⁺⟩. The four nodes are evenly spaced (at 12, 3, 6, and 9 o'clock positions). A small two-bit message label position (as a simple geometric shape or color indicator, not text) connects each spoke to its message. The spokes are colored differently per message. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Hub-and-spoke with center = |Φ⁺⟩ resource; four spokes leading to four nodes: (00) I → |Φ⁺⟩ = equal bars at |00⟩ and |11⟩ (positive); (01) X → |Ψ⁺⟩ = equal bars at |01⟩ and |10⟩; (10) Z → |Φ⁻⟩ = equal bars at |00⟩ and |11⟩ with phase inversion indicated by bar color contrast; (11) iY → |Ψ⁻⟩ = equal bars at |01⟩ and |10⟩ with phase inversion. Gate symbols: I, X, Z, iY (or XZ) applied to Alice's qubit A only. Bar charts: four bars per node with heights = |amplitude|², two nonzero bars per Bell state. Phase contrast: positive amplitude = Bluish Green; negative amplitude = Vermillion (encoding sign, not magnitude change — both bars same height but colored differently). All encodings from chapter's encoding table.

`[O — ORGANIZATION]` Radial layout. Center hub at geometric center of panel. Four spokes equally angled. Nodes at spoke endpoints. Gate symbol placed midway along each spoke. Bar chart inside each node. Bell-state identity (geometric or color indicator matching Okabe-Ito assignment per Bell state) at outer edge of each node. Spokes differentiated by color. No crowding — nodes sized to fit within 89 mm single-column width with comfortable margins.

`[P — PRESENTATION]` Flat vector; |Φ⁺⟩ hub = Blue #0072B2; spoke-00 (I) = Bluish Green #009E73; spoke-01 (X) = Orange #E69F00; spoke-10 (Z) = Sky Blue #56B4E9; spoke-11 (iY) = Reddish Purple #CC79A7; positive amplitude bars = Bluish Green #009E73; negative amplitude bars = Vermillion #D55E00; gate symbol boxes = spoke color; hub double-arc = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: teleportation protocol circuit; Bell measurement decoding circuit (the decode step, not the encode); Holevo bound context; no-cloning proof; quantum channel capacity theorem; the CNOT+H Bell measurement diagram.

**BLOCK 3 — NEGATIVE PROMPT:** circuit diagram with time axis, Bloch sphere, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Teleportation vs. Dense Coding: Resource Duality

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a duality diagram with two rows. Top row (teleportation): three resource icons arranged left to right — an entanglement icon (two linked circles labeled ebit), a plus-sign spacer, a two-bit classical channel icon (two horizontal parallel lines with arrows), then a right-pointing double arrow (yields), then a single-qubit transmission icon (one qubit arrow). Bottom row (dense coding): three resource icons — an entanglement icon (same two linked circles), plus a single qubit transmission icon (one qubit arrow), then a right-pointing double arrow (yields), then a two-bit classical transmission icon (two parallel arrows). Both rows centered on the same vertical alignment for the entanglement icon. A bidirectional vertical double arrow between the two rows at the entanglement position, and a bidirectional arrow between the two rows at the output position — with a contrast: what is input in teleportation is output in dense coding and vice versa. The ebit icon identical in both rows — the shared resource. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Two-row duality: Row 1 (teleportation): 1 ebit + 2 classical bits → transmit 1 qubit. Row 2 (dense coding): 1 ebit + 1 qubit channel → transmit 2 classical bits. Resource icons: ebit = two linked circles with double-arc; classical bit = simple horizontal bar with arrow; qubit = circle with arrow (indicating quantum transmission). Double arrows between rows at: the ebit position (same resource shared by both) and the input/output positions (showing reversal). Inferred duality relation: the yields arrow direction and input/output role swap between rows.

`[O — ORGANIZATION]` Two horizontal rows, vertically aligned at resource positions. Left side = inputs, right side = outputs for both rows. Vertical double arrows connecting corresponding positions between rows. Left-to-right flow within each row. Plus symbols between input resources (as spacers between resource icons). Yields arrow (double-headed rightward) at center of each row.

`[P — PRESENTATION]` Flat vector; teleportation row = Sky Blue #56B4E9 icons with Blue #0072B2 flow arrow; dense coding row = Orange #E69F00 icons with Bluish Green #009E73 flow arrow; ebit icon = Reddish Purple #CC79A7 (same in both rows to signal shared resource); duality vertical arrows = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: specific protocol circuit steps; no-cloning theorem structure; Holevo bound formula; entanglement-assisted capacity theorem; Bell measurement circuit; numerical fidelity values; mixed-state resource analysis.

**BLOCK 3 — NEGATIVE PROMPT:** circuit diagram with qubit wires and gate symbols, Bloch sphere, bar chart, matrix grid, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows (standard), hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Bob's Reduced Density Matrix Before Classical Bits

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-panel comparison diagram. Left panel: a 2×2 bar chart representing a general single-qubit density matrix — four bars for the elements ρ₀₀, ρ₀₁, ρ₁₀, ρ₁₁, with nonzero off-diagonal bars and unequal diagonal bars indicating a mixed but non-trivial state with coherences. Right panel: a 2×2 bar chart representing the maximally mixed density matrix — diagonal bars each at exactly half the maximum height, off-diagonal bars at zero height (flat to the floor). A label zone (post-production typography) at top indicates the left is a general state and the right is I/2. A left-pointing arrow from right to left labeled as "before classical bits" (as a directional flow indicator, not text). Both panels share the same axis scale. A small Bloch sphere icon below each bar chart: left panel shows a point on or near the sphere surface; right panel shows the sphere center (Bloch vector at origin). No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left panel: illustrative generic single-qubit density matrix with off-diagonal coherences (bars at nonzero heights for ρ₀₁, ρ₁₀) and unequal populations. Right panel: maximally mixed state ρ_B = I/2 — ρ₀₀ = ρ₁₁ = 0.5, ρ₀₁ = ρ₁₀ = 0 (from the chapter's explicit derivation). Bloch sphere icons: left = surface or near-surface point; right = center dot (origin). Y-axis from zero to maximum possible density matrix element magnitude (0.5 for off-diagonals, 1.0 for diagonals). This figure illustrates the no-signaling result from the chapter's explicit trace calculation.

`[O — ORGANIZATION]` Two bar charts side by side, separated by a center gap with a directional arrow. Shared y-axis scale. Four bars per chart: ρ₀₀ (leftmost), ρ₀₁, ρ₁₀, ρ₁₁ (rightmost). Bloch sphere icons centered below each bar chart. Arrow between panels points left (general → maximally mixed, indicating collapse of information when tracing over Alice's qubits). Equal panel widths.

`[P — PRESENTATION]` Flat vector; diagonal bars (ρ₀₀, ρ₁₁) = Blue #0072B2; off-diagonal bars (ρ₀₁, ρ₁₀) = Orange #E69F00; right panel bars (maximally mixed) = Sky Blue #56B4E9 for diagonals, flat zero-height for off-diagonals; directional arrow = Vermillion #D55E00 (signaling the loss — information not transmitted); Bloch sphere icons = neutral gray wireframe with orange surface point (left) vs. filled center dot (right); y-axis = Blue #0072B2 thin line; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: the four conditional states post-measurement (Figure 2); teleportation circuit structure (Figure 1); dense coding encoding (Figure 3); numerical values of α, β; partial trace algebra; CHSH fidelity connection.

**BLOCK 3 — NEGATIVE PROMPT:** three-qubit register, circuit diagram, Pauli gate visualization, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Teleportation Protocol Flowchart:**
VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages and the transition mechanism — state information passing from S through entanglement into B via a classical phone call — is the chapter's central learning target. The sequence of gates on qubits S and A, the collapse of qubit S at measurement, and the correction transforming B's state into ψ unfolds over five stages with direct causal dependence. A static diagram forces the reader to reconstruct the temporal ordering. Animation can show: (a) the CNOT entangling S with A, (b) the H creating the measurement basis, (c) the measurement collapsing S (Bloch vector snapping to north/south pole), (d) the classical bits traveling (the dashed-line path animating), (e) the correction gate transforming B's Bloch vector to match the original ψ. This is the chapter's recommended video.

**Figure 2 — Four Outcome Correction Panels:**
STATIC SUFFICIENT. The four panels are a reference comparison grid, not a causal sequence. All four outcomes exist simultaneously in the pre-measurement superposition; static side-by-side display is the appropriate format.

**Figure 3 — Dense Coding Hub-and-Spoke:**
STATIC SUFFICIENT. A synchronous mapping (Alice's choice of Pauli determines the Bell state instantly); no temporal sequence to animate.

**Figure 4 — Teleportation vs. Dense Coding Duality:**
STATIC SUFFICIENT. A structural comparison diagram. Duality is a spatial relationship, not a temporal process.

**Figure 5 — Bob's Reduced Density Matrix:**
STATIC SUFFICIENT. A before/after comparison of two static states. The pedagogic content is the contrast between the two states, not a transformation process requiring animation.

**Recommended video:** Figure 1 — Teleportation Protocol Flowchart (qubit-S collapse + classical bits traveling to Bob + correction gate transforming B).
