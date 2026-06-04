# CAJAL Figure Report — Chapter 4 — Quantum Gates and Circuits

Recommended: 7 figures, Mixed density.

---

## Figure 1 — Bloch Sphere with Standard Gate Actions

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a unit sphere in orthographic projection representing the Bloch sphere for a single qubit. Place the north pole labeled as the computational basis state zero and the south pole as state one. Mark the six canonical axis-intercept points: north pole, south pole, positive-x equator point, negative-x equator point, positive-y equator point, and negative-y equator point. Show the Bloch vector as a directed arrow from the sphere center to the north pole as the default starting position. Draw six labeled arrows on the sphere surface or as arcs indicating the rotation actions of the standard gates: X as a pi-rotation arc about the x-axis swapping north and south poles, Z as a pi-rotation arc about the z-axis, H as a pi-rotation arc about the diagonal x-plus-z axis that maps north to positive-x equator, S as a pi-over-two arc about z, T as a pi-over-four arc about z, and Y as a pi-rotation arc about y. Use a consistent color for each gate arrow. The sphere wireframe should show the equatorial circle and two meridians. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Unit Bloch sphere; north pole = |0⟩, south pole = |1⟩; six axis-intercept cardinal points (±x, ±y, ±z); rotation arcs for X (π about x̂), Z (π about ẑ), H (π about (x̂+ẑ)/√2), S (π/2 about ẑ), T (π/4 about ẑ), Y (π about ŷ); Bloch vector arrow from center; equatorial circle and two meridians as wireframe. All gate-to-rotation correspondences are stated explicitly in the chapter.

`[O — ORGANIZATION]` Single sphere, center of panel. Rotation arcs drawn as curved arrows on the sphere surface. Gate arcs arranged without overlap; arcs for Z, S, T cluster around the z-axis (differentiated by arc length/color); arcs for X, Y, H cross the equatorial plane. Wireframe in neutral gray. Each gate arc a distinct Okabe-Ito color.

`[P — PRESENTATION]` Flat vector; Okabe-Ito palette: X arc = Vermillion #D55E00; Z arc = Blue #0072B2; H arc = Bluish Green #009E73; S arc = Orange #E69F00; T arc = Reddish Purple #CC79A7; Y arc = Sky Blue #56B4E9; Bloch vector arrow = neutral dark gray; sphere wireframe = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: continuous rotation gates Rx, Ry, Rz (not a gate-action figure); CNOT and two-qubit gates; density matrix representation; mixed states interior to sphere (no interior point shown); global phase; Euler-angle decomposition; SU(2)/SO(3) double-cover diagram; numerical matrix entries.

**BLOCK 3 — NEGATIVE PROMPT:** photon, wave function, circuit wire, matrix grid, energy levels, two-qubit system, interior Bloch vector, gradient fill on sphere, 3D shading, specular highlights, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — CNOT Gate: Basis-State Action and Entangling Power

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side panels sharing a vertical layout. Left panel: a two-row input-output mapping showing all four computational basis input pairs (zero-zero, zero-one, one-zero, one-one) on the left connected by horizontal arrows to their CNOT outputs (zero-zero, zero-one, one-one, one-zero) on the right. The top two rows (control = zero) have no change; the bottom two rows (control = one) show the target bit flipped. Mark the control qubit row and target qubit row with distinct symbols — a filled circle for control and a circled-plus for target — consistent with circuit notation. Right panel: show the entangling case. A superposition control state represented as two parallel horizontal lines merging from a split (indicating equal superposition of zero and one) entering the CNOT with the target in state zero, producing an output arrow that fans into two correlated branches zero-zero and one-one joined by a curved brace indicating they cannot be separated. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left panel: four basis-state rows showing input pairs |00⟩, |01⟩, |10⟩, |11⟩ and their CNOT outputs |00⟩, |01⟩, |11⟩, |10⟩; horizontal directed arrows for each mapping; rows grouped visually: top pair (control=0, no flip) and bottom pair (control=1, target flipped). Right panel: superposition input state for control (equal-weight split), target |0⟩; single CNOT gate symbol; output showing two correlated branches |00⟩ and |11⟩ with a brace indicating entanglement (inferred joint structure). Control identified by filled dot, target by ⊕ symbol.

`[O — ORGANIZATION]` Two panels side by side with a thin vertical separator. Left panel: four horizontal rows, evenly spaced, grouped with a bracket separating control=0 rows (top half) from control=1 rows (bottom half). Right panel: diverging-then-correlated flow with the CNOT gate symbol at center. Flow direction: left to right throughout. Labels applied post-production only.

`[P — PRESENTATION]` Flat vector; control=0 rows = Sky Blue #56B4E9; control=1 rows = Orange #E69F00; entangled output brace/branches = Bluish Green #009E73; CNOT gate symbol = Blue #0072B2; group bracket = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: matrix representation of CNOT; CZ gate; Toffoli gate; Bloch sphere; three-qubit operations; phase kickback mechanism (separate figure); continuous rotation gates; XOR notation spelled out; quantum circuit wire notation beyond the gate symbol itself.

**BLOCK 3 — NEGATIVE PROMPT:** matrix grid, Bloch sphere, energy levels, wavefunction, probability density curve, three-qubit register, full circuit diagram with multiple gates, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Bell-State Preparation Circuit: H–CNOT Step-by-Step

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-stage horizontal progression panel. Stage zero: two qubits in state zero shown as two horizontal wires with Bloch-sphere icons at the left end, both arrows pointing to the north pole. Stage one (after Hadamard on qubit zero): qubit-zero Bloch sphere icon now shows the arrow pointing along the positive-x equator; qubit-one icon still points north. A vertical dashed separator between stage zero and stage one. Stage two (after CNOT): both Bloch sphere icons show the arrow collapsed to the origin (center of sphere), indicated by a small filled dot with no arrow, representing the maximally mixed reduced state. Below all three stages, show the joint two-qubit state as a simple diagram: in stage zero, two separate circles representing qubits; in stage one, two separate circles; in stage two, the two circles connected by a double-arc line indicating entanglement. The H gate appears as a labeled rectangle on qubit-zero wire between stages zero and one; the CNOT gate symbol (filled dot on control, ⊕ on target) appears between stages one and two. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three-stage horizontal sequence: (0) |00⟩ initial state — both Bloch vectors at north pole, product state; (1) after H⊗I — qubit-0 Bloch vector at +x equator, qubit-1 still at north pole, product state; (2) after CNOT — both Bloch vectors at origin indicating maximally mixed reduced states, entangled joint state |Φ⁺⟩. Gate symbols: H box on qubit-0 wire, CNOT symbol (filled dot control, ⊕ target) spanning both wires. Product/entanglement indicator below: two unconnected circles (stages 0–1) → two circles joined by double arc (stage 2). All relationships drawn from chapter content.

`[O — ORGANIZATION]` Left-to-right horizontal flow. Two qubit wires run as parallel horizontal lines. Bloch sphere icons (small, ~15 mm diameter) placed at three time positions on each wire. Gate symbols placed between stages. Product/entanglement indicator row beneath the wires. Vertical dashed separators mark the three time slices. Equal horizontal spacing between stages.

`[P — PRESENTATION]` Flat vector; qubit-0 wire = Blue #0072B2; qubit-1 wire = Sky Blue #56B4E9; Bloch vector arrows (stages 0–1) = Orange #E69F00; collapsed Bloch dot (stage 2) = Vermillion #D55E00; H gate box = Bluish Green #009E73; CNOT symbol = Blue #0072B2; entanglement arc = Reddish Purple #CC79A7; separator dashes = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: all four Bell states (this figure covers |Φ⁺⟩ only); matrix arithmetic; Deutsch algorithm; universal gate set context; phase labels on Bloch vectors; numerical amplitude values; Y, Z, S, T, Rz gates; three-qubit circuits.

**BLOCK 3 — NEGATIVE PROMPT:** matrix notation, amplitude bars, probability histogram, phase diagram, energy levels, three-qubit register, all four Bell states simultaneously, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Phase Kickback in the Deutsch Algorithm

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a four-stage horizontal mechanism panel with two qubit wires (query register top, ancilla bottom). Stage zero: query qubit in state zero, ancilla in state one. Stage one (after H on both): query in positive-x superposition (equal-weight split shown as a branching arrow), ancilla in minus state (equal-weight split with a negative phase indicator). Stage two (oracle): show the oracle block spanning both wires; two sub-cases branch from the oracle, one for f constant (both branches acquire the same phase — shown as uniform shading on the query branches) and one for f balanced (opposite phases on the two query branches — shown as filled vs. unfilled shading, indicating a relative phase flip). Stage three (final H on query): the two sub-cases collapse to distinct outputs — constant case resolves to a single arrow at north pole; balanced case resolves to a single arrow at south pole. A callout or visual accent at the oracle stage indicates the phase information flows upward from ancilla branch into the query register phase (a dotted upward arrow from the ancilla to the query) — labeled as an inferred directional flow. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Four-stage horizontal sequence showing the Deutsch algorithm on two qubits: (0) |0⟩|1⟩ initial; (1) |+⟩|−⟩ after H⊗H; (2) oracle Uf producing phase kickback — constant f: uniform phase on query branches (no relative sign); balanced f: opposite phase on query branches (relative sign flip); (3) final H on query — constant f yields |0⟩, balanced f yields |1⟩. Phase kickback direction shown as inferred dotted arrow from ancilla to query at oracle stage. Two fork paths after oracle labeled as constant and balanced cases. The ancilla state |−⟩ persists unchanged throughout — shown as stable unchanged icon.

`[O — ORGANIZATION]` Left-to-right flow. Two parallel horizontal wires. Bloch-sphere or amplitude-branch icons at each stage. Oracle stage spans both wires as a shaded rectangle. After the oracle, two diverging paths (constant vs. balanced) continue rightward, reconverging to opposite final states at the measurement stage. Vertical dashed separators mark the four time slices. The inferred phase-kickback annotation is a dotted diagonal arrow at the oracle stage.

`[P — PRESENTATION]` Flat vector; constant-function path = Bluish Green #009E73; balanced-function path = Orange #E69F00; oracle block = Blue #0072B2; phase-kickback dotted arrow = Reddish Purple #CC79A7 (inferred relation); ancilla icons = Sky Blue #56B4E9; query icons = Blue #0072B2; neutral separator = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Deutsch–Jozsa generalization (n-bit version); Grover's algorithm; Shor's algorithm; full matrix algebra; Bell-state preparation (separate figure); H gate Bloch-rotation detail; ancilla state change (ancilla is unchanged — do not show it evolving); classical query model comparison diagram.

**BLOCK 3 — NEGATIVE PROMPT:** Grover diffusion operator, QFT diagram, n-qubit registers, truth table grid, matrix entries, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Universal Gate Set Hierarchy: Clifford vs. T-Extended

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a nested set diagram with three concentric regions. The innermost region contains icons representing the Clifford group generators: H, S, and CNOT gate symbols. The middle region adds the T gate icon outside the innermost region but inside the middle boundary, indicating that adding T to the Clifford group creates the universal gate set {H, T, CNOT}. The outermost region represents all unitary operations SU(2^n) — shown as a continuous shaded boundary. A callout at the innermost region indicates classical simulability (efficient classical simulation possible, Gottesman–Knill); a callout at the middle region indicates universal quantum computation (dense coverage of SU(2)); a callout at the outer boundary indicates the full space of unitaries being approximated. An arrow or label at the T gate position marks it as the non-Clifford resource that breaks classical simulability. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three nested regions: (1) innermost = Clifford group {H, S, CNOT} with gate symbols, annotated as classically simulable per Gottesman–Knill theorem; (2) middle = {H, T, CNOT} universal gate set, with T gate symbol added between inner and middle boundaries; (3) outermost = all unitaries SU(2^n) approximated to arbitrary precision by the middle set. Gate symbols: H, S, T, CNOT rendered as small rectangles/circuit symbols. Solovay–Kitaev efficiency (dense subgroup generation) indicated by a bidirectional approximation arrow at the outer boundary — inferred relationship between the set and the full unitary space.

`[O — ORGANIZATION]` Concentric ellipse or rounded-rectangle regions, centered. Gate symbols placed inside their respective regions with visual grouping. T gate symbol placed in the annular gap between inner and middle boundaries. Callout annotations placed outside the outermost region connected by thin lines. Nested regions grow outward with sufficient margin for clarity. No crowding beyond 6 labeled elements per region.

`[P — PRESENTATION]` Flat vector; innermost Clifford region fill = Sky Blue #56B4E9 (light, 20% opacity); middle universal region fill = Bluish Green #009E73 (light, 15% opacity); T gate highlight = Orange #E69F00 (strong, to draw attention); outer boundary = Blue #0072B2 dashed stroke; callout lines = light gray; gate symbol boxes = Blue #0072B2 strokes; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Toffoli gate; individual qubit fidelity numbers; magic state distillation circuit; Euler-angle decomposition; BQP complexity class boundary; specific hardware platforms; continuous rotation gate family.

**BLOCK 3 — NEGATIVE PROMPT:** Venn diagram with overlapping non-nested circles, BQP/P/NP diagram, complexity hierarchy lattice, hardware schematic, error-correction code structure, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Grover vs. Shor: Query Complexity Comparison

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single-axis bar chart with the y-axis representing query complexity (number of oracle calls required to solve the problem) starting at zero, and the x-axis showing four conditions: classical-search (N items), quantum-Grover (N items), classical-factoring (n bits), quantum-Shor (n bits). For the search problem pair, draw two bars side by side: the classical bar reaches height proportional to N (tall, labeled with the growth rate), the Grover bar reaches height proportional to sqrt(N) (shorter). For the factoring problem pair, draw two bars side by side: the classical bar reaches height proportional to a sub-exponential function (very tall), the Shor bar reaches height proportional to n squared log n (much shorter). Use a note indicator on the factoring classical bar that it extends beyond the plot area — a clipped bar with a break mark — since the sub-exponential is far larger than polynomial at relevant n. A horizontal reference line at height one marks a single-query baseline. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Grouped bar chart: two problem pairs (search and factoring), each with one classical bar and one quantum bar. Search problem: classical O(N), quantum O(√N) — quadratic speedup. Factoring problem: classical sub-exponential exp(O(n^(1/3) log^(2/3) n)), quantum polynomial O(n² log n log log n) — exponential speedup. Y-axis starts at zero and represents relative scaling (conceptual, not exact numerical values — bars encode order-of-magnitude relationships, not absolute counts). Clipped bar indicator on classical factoring bar (bar too tall to display fully). Horizontal baseline at y=1. Quantum bars visually shorter than classical bars for both problems; Grover gap smaller than Shor gap.

`[O — ORGANIZATION]` Two grouped bar pairs on shared x-axis. Groups separated by a wider gap than the within-group gap. Classical bar left, quantum bar right within each pair. Y-axis labeled with representative growth labels (as post-production typography). Y-axis from zero; no 3D; no truncated y-axis. Break mark on classical factoring bar at the top of the plot area.

`[P — PRESENTATION]` Flat vector; classical bars = Orange #E69F00; quantum bars = Bluish Green #009E73; bar group separators = light gray tick; y-axis and x-axis = Blue #0072B2 thin line; break mark = Vermillion #D55E00; baseline reference line = light gray dashed; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: BQP/NP complexity diagram; Grover amplitude amplification circuit; QFT circuit for Shor; error-correction overhead; T-gate count; post-quantum cryptography context; Deutsch–Jozsa comparison.

**BLOCK 3 — NEGATIVE PROMPT:** pie chart, scatter plot, 3D bar chart, logarithmic y-axis (use conceptual linear scaling), exact numerical tick marks, circuit diagram elements, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 7 — No-Cloning: Inner-Product Argument Structure

**Heuristic:** VG | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-row mechanism diagram. Top row: a hypothetical cloner box (rectangle) receives an input qubit state ψ and a blank qubit state zero, and attempts to output two copies of ψ on separate wires. Bottom row: a second hypothetical cloner box receives input state φ and the blank state zero, attempting to output two copies of φ. Between the two rows, draw a bracket indicating that unitarity requires the inner product on the left (input side) to equal the inner product on the right (output side). The left bracket connects the two input pairs with an equals-sign bridge; the right bracket connects the two output pairs with a squared-equals-sign bridge, indicating the inner product is squared on the output side. A final indicator below the right bracket shows the logical conflict: the squared-equals constraint forces the overlap to be either zero or one (indicated by a forking arrow to two end states: orthogonal and identical), marking arbitrary superpositions as excluded — shown as a cross-out symbol through the intermediate region between zero and one on a small number line. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Two parallel rows showing the cloner applied to states ψ and φ. Cloner box with two input wires (state + blank) and two output wires (two copies). Left side: inner product ⟨φ|ψ⟩ indicated by bracket between the two input wires. Right side: inner product squared ⟨φ|ψ⟩² indicated by bracket between two output pairs. Equality bridge (unitarity constraint) connecting left inner product to right inner product. Logical consequence: small number line (0 to 1) with markers at 0 and 1 as the only allowed values, intermediate region crossed out. The "arbitrary state excluded" conclusion is inferred from the constraint z = z² ⟹ z ∈ {0,1}.

`[O — ORGANIZATION]` Two horizontal rows, evenly spaced. Left-to-right flow through the cloner. Brackets drawn vertically between the rows on each side. Equality bridge horizontal. Number-line conclusion positioned below the right bracket. Forking arrow from the "z = z²" constraint indicator to the two valid endpoints (0 and 1). Exclusion cross-out on the open interval.

`[P — PRESENTATION]` Flat vector; cloner boxes = Blue #0072B2; ψ row = Sky Blue #56B4E9; φ row = Orange #E69F00; inner-product brackets = Reddish Purple #CC79A7; equality bridge = Bluish Green #009E73; exclusion cross-out = Vermillion #D55E00; number line = light gray with dark endpoints; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: CNOT fan-out circuit (this figure addresses universal cloning only); quantum teleportation protocol; no-signaling proof; QKD application; density matrix formalism; specific state values like |+⟩ and |−⟩.

**BLOCK 3 — NEGATIVE PROMPT:** circuit diagram with multiple gate stages, Bloch sphere, density matrix, quantum channel diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Bloch Sphere Gate Actions:**
STATIC SUFFICIENT. The six gate rotations are simultaneous reference material; no single causal chain requires animation. A reader can parse rotation arcs on a static diagram.

**Figure 2 — CNOT Basis-State Action and Entangling Power:**
STATIC SUFFICIENT. The left panel is a lookup table; the right panel is a before-and-after contrast. Neither requires temporal animation.

**Figure 3 — Bell-State Preparation Circuit:**
VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages and transformation of the Bloch vector from surface to origin is the learning target. The Bloch vector collapse at the CNOT step (surface → origin) is a spatial transformation below direct intuition and the chapter explicitly calls out this moment as where entanglement is created. Recommend: one short animation of the Bloch sphere icon on qubit-0 moving from north pole to +x equator (after H), then both Bloch vectors shrinking to the origin (after CNOT). This is the chapter's recommended video.

**Figure 4 — Phase Kickback in the Deutsch Algorithm:**
STATIC SUFFICIENT. The two fork paths (constant vs. balanced) are a comparison structure well-served by two static side-by-side panels. The mechanism is subtle but the pedagogic content is the logical consequence, not the temporal unfolding.

**Figure 5 — Universal Gate Set Hierarchy:**
STATIC SUFFICIENT. A nested-set diagram is inherently static spatial structure. No causal sequence or transformation.

**Figure 6 — Grover vs. Shor Query Complexity:**
STATIC SUFFICIENT. Bar charts convey relative scaling effectively as static figures. No sequential mechanism to animate.

**Figure 7 — No-Cloning Inner-Product Argument:**
STATIC SUFFICIENT. A deductive logical structure; the two rows are parallel, not sequential. Animation would not clarify the algebraic constraint.

**Recommended video:** Figure 3 — Bell-State Preparation Circuit (Bloch vector collapse under H then CNOT).
