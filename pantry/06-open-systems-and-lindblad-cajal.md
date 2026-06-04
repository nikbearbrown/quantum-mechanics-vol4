# CAJAL Figure Report — Chapter 6 — Open Systems: Decoherence and the Lindblad Equation

Recommended: 6 figures, Mechanistic density.

---

## Figure 1 — System–Environment Entanglement and Reduced Density Matrix

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-stage horizontal mechanism panel. Stage zero: a qubit icon (small Bloch sphere at a surface point, indicating pure state |ψ₀⟩) on the left and an environment icon (a cluster of many small dots representing a multi-degree-of-freedom bath) on the right. The two are unconnected — separated by white space. Stage one (after coupling H_SE): a dashed coupling arrow connects the qubit to the environment; the environment icon splits into two branches — one branch labeled with a light shading and one with no shading — indicating the two environment trajectories |e₀(t)⟩ and |e₁(t)⟩ branching based on the qubit state. Stage two (decoherence complete): the qubit Bloch sphere icon shows the arrow shrunk toward the center (mixed state), the environment branches are now fully separated (two distinct cloud icons with no overlap). A bracket below the qubit icons at stages one and two labels the overlap of the two environment branches: at stage one the two branch icons partially overlap; at stage two they are fully separated. A partial-trace symbol (dotted enclosure around the environment icon with a trace-out arrow pointing downward) at stage two indicates the reduced density matrix is obtained by tracing over the environment. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three-stage sequence: (0) product state |ψ₀⟩|e₀⟩ — qubit pure, environment single state; (1) partial entanglement |α||0⟩|e₀(t)⟩ + β|1⟩|e₁(t)⟩ — two environment branches, partial overlap ⟨e₀(t)|e₁(t)⟩ < 1; (2) decoherence complete — branches orthogonal ⟨e₀(t)|e₁(t)⟩ = 0, qubit reduced state diagonal, Bloch vector at origin. Partial trace operation at stage 2 shown as dotted enclosure around environment with downward trace arrow. Environment overlap indicator (partial overlap icon → no overlap icon) below stages 1–2. Total evolution remains unitary (no indication of information loss from the total system — shown by a dashed outer box enclosing both qubit and environment icons throughout). Off-diagonal suppression by overlap factor inferred from chapter's explicit density matrix derivation.

`[O — ORGANIZATION]` Three horizontal stages separated by vertical dashed rules. Qubit icon on top row, environment icon on bottom row. Coupling arrow appears at stage 1 spanning rows. Branch separation of environment grows from stage 1 to 2. Partial-trace enclosure and arrow at stage 2 bottom. Bloch vector shrinkage shown by comparing arrow length across stages. Overlap indicator spans stages 1 and 2 as a below-panel annotation.

`[P — PRESENTATION]` Flat vector; qubit Bloch sphere = Orange #E69F00 arrow, blue #0072B2 wireframe; environment cluster dots = Sky Blue #56B4E9; branch 0 (|0⟩ path) = Bluish Green #009E73; branch 1 (|1⟩ path) = Reddish Purple #CC79A7; coupling arrow = Blue #0072B2; partial-trace enclosure = light gray dashed; outer total-system box = light gray thin solid; overlap indicator = Orange #E69F00 (partial overlap) to flat line (zero overlap); uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Lindblad equation structure (separate figure); Bloch equations (separate figure); specific jump operators; Born–Markov approximation derivation; pointer states/einselection (separate figure); numerical timescales T₁, T₂; density matrix element bar chart.

**BLOCK 3 — NEGATIVE PROMPT:** circuit diagram with qubit wires, Hamiltonian matrix, Bloch equation, pointer-state basis diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Lindblad Equation Structure: Terms and Roles

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a schematic diagram of the Lindblad master equation decomposed into its structural parts. Use a horizontal equation-layout visual: a central box or bar representing the full time derivative dρ/dt. From this central bar, draw three downward branches: left branch labeled H-term (Hamiltonian commutator — shown as a rotation-arrow icon, indicating unitary precession, no dissipation), center branch labeled dissipator sum (shown as a downward-pointing funnel icon with multiple input arrows from above representing multiple jump operators L_k feeding in), right branch empty (placeholder for visual balance). Below the dissipator funnel, draw the anatomy of one dissipator term: a three-part diagram showing the jump term L ρ L† (shown as a forward-pass icon, two arrows bracketing ρ), the anticommutator term −(1/2){L†L, ρ} (shown as a sandwiching icon with a subtraction indicator), and their combined result arrow pointing into the output. A trace-preservation check: a small balance scale icon at the bottom indicating Tr(dissipator) = 0 — equal inputs and outputs on the scale, indicating trace is conserved. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three structural parts of the GKSL equation: (1) Hamiltonian term −(i/ℏ)[H, ρ] — unitary, reversible, shown as rotation icon; (2) dissipator sum over k of D[L_k](ρ) = L_k ρ L_k† − (1/2){L_k†L_k, ρ} — dissipative, irreversible; (3) complete-positivity constraint (implied by anticommutator structure — shown as a CP badge on the dissipator). Dissipator anatomy: L_k ρ L_k† term as forward-pass bracket, anticommutator term as symmetric-squeeze bracket with subtraction. Trace preservation check: balance-scale icon indicating Tr(D[ρ]) = 0. All relationships drawn from chapter's explicit trace-preservation derivation. No fabricated relationships — the three-term decomposition is stated exactly in the chapter.

`[O — ORGANIZATION]` Top-down branching layout. Central dρ/dt bar at top. Three downward branches. H-term on left, dissipator on center, CP badge on right side of dissipator branch. Dissipator anatomy expands below the funnel icon. Trace-preservation balance scale at bottom center. Each element connected by directed arrows indicating contribution flow. Visual hierarchy: equation level at top, structural decomposition in middle, algebraic anatomy at bottom.

`[P — PRESENTATION]` Flat vector; dρ/dt central bar = Blue #0072B2; H-term branch/rotation icon = Sky Blue #56B4E9; dissipator branch/funnel = Orange #E69F00; jump term L ρ L† brackets = Bluish Green #009E73; anticommutator term brackets = Reddish Purple #CC79A7; subtraction indicator = Vermillion #D55E00; trace-preservation balance = Bluish Green #009E73; CP badge = Bluish Green #009E73; directional arrows = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Born–Markov microscopic derivation; secular approximation; specific jump operators σ_z and σ_−; Bloch equations (separate figure); non-Markovian extensions; system-bath Hamiltonian H_total structure (Figure 1); numerical rates; Nakajima–Zwanzig equation.

**BLOCK 3 — NEGATIVE PROMPT:** circuit diagram, Bloch sphere, Hamiltonian matrix entries, bath diagram, energy levels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Bloch Vector Dynamics: Three Regimes

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw three side-by-side Bloch sphere panels, each showing a different decoherence regime. Left panel (pure dephasing only, T_φ finite, T₁ → ∞): Bloch vector starts at the equator (positive-x position) and traces a spiral that decays toward the z-axis but stops at the equatorial plane — the final position is at the z-axis midpoint (origin projected to z=0), not at the south pole. The spiral trail shows the transverse components decaying while r_z remains fixed at zero. Center panel (energy relaxation only, T₁ finite, T_φ → ∞): Bloch vector starts at the north pole (excited state) and decays along the z-axis straight down to the south pole (ground state |0⟩) — a simple vertical decay with no transverse oscillation. Right panel (combined dephasing and relaxation, both finite): Bloch vector starts at the equator, spirals inward and downward, converging toward the south pole. All three panels show the spiral trail as a dotted curve, and the final resting position as a filled dot. A shared legend below all three panels uses three distinct Okabe-Ito colors for the three spiral types. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three Bloch sphere panels: (1) Pure dephasing T_φ finite, T₁ = ∞: equatorial start, spiral decaying to z-axis at r_z = 0 (not to south pole). r_z constant. Final state = center of equatorial plane. (2) Pure relaxation T₁ finite, T_φ = ∞: north-pole start (excited state), monotonic decay to south pole along z-axis, no precession. (3) Combined: equatorial start, spiral converging to south pole. All from chapter's Bloch equation solutions with appropriate initial conditions and limiting cases. Spiral trails as dotted curves. Final equilibrium points as filled circles. The south pole represents |0⟩ (ground state, r_z = −1) — consistently marked across all three panels.

`[O — ORGANIZATION]` Three Bloch sphere icons side by side, equal size, equal spacing. Shared bottom legend bar with three color swatches. Within each sphere: equator circle and polar axis as thin gray lines; spiral trail in regime-specific color; start position as open circle; end position as filled circle of same color. Trajectory direction indicated by small arrowhead on trail.

`[P — PRESENTATION]` Flat vector; pure-dephasing spiral = Orange #E69F00; pure-relaxation decay = Bluish Green #009E73; combined spiral = Reddish Purple #CC79A7; sphere wireframe = light gray; start points = open circles, same color as trajectory; end points = filled circles, same color; south pole ground state marker = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: density matrix bar chart (separate figure); Lindblad equation structure (Figure 2); system-bath branching model (Figure 1); pointer states/einselection (Figure 5); specific hardware timescale numbers; non-Markovian revivals; dynamical decoupling pulse sequences.

**BLOCK 3 — NEGATIVE PROMPT:** density matrix bar chart, jump operator diagram, bath cluster, circuit diagram, energy level diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Density Matrix Element Decay: Off-Diagonal vs. Diagonal Timescales

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side line charts sharing the same x-axis (time, from zero to approximately four times the larger timescale). Left chart: y-axis from zero to 0.5 representing |ρ₀₁(t)| (magnitude of off-diagonal coherence). Draw two curves: a rapidly decaying exponential labeled T₂ (coherence decay) and a more slowly decaying exponential labeled T₁/2 (the contribution from energy relaxation alone). The T₂ curve decays faster. Indicate the T₂ timescale as a vertical reference line at x = T₂. Right chart: y-axis from zero to 1 representing ρ₀₀(t) and ρ₁₁(t) (populations). Draw two curves: ρ₁₁ starting at one and decaying to zero (excited population decays at rate 1/T₁); ρ₀₀ starting at zero and rising to one (ground population builds as excited decays). Indicate the T₁ timescale as a vertical reference line. A horizontal connector between the two charts at the T₁ reference lines indicates T₁ governs the diagonal, while T₂ ≤ 2T₁ governs the off-diagonal. Both charts share the same x-axis time scale for direct comparison. Y-axes from zero. No 3D. No truncated y-axis. No red-green. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left chart: |ρ₀₁(t)| = (1/2) e^{−t/T₂} (pure dephasing initial condition from chapter's worked example) and reference envelope (1/2)e^{−t/(2T₁)} for comparison. Vertical reference at t = T₂. Right chart: ρ₁₁(t) = ρ₁₁(0) e^{−t/T₁} (decaying from initial excited population), ρ₀₀(t) = 1 − ρ₁₁(t) (rising ground population). Vertical reference at t = T₁. Horizontal bracket or connector at x-axes indicating T₂ ≤ 2T₁ constraint (T₁ marked as larger than T₂ in the shared time axis). All curves from the chapter's Bloch equation solutions.

`[O — ORGANIZATION]` Two equal-width panels side by side. Shared x-axis range from 0 to 4×max(T₁, T₂). Separate y-axes: left 0–0.5, right 0–1. Vertical reference lines at T₂ (left) and T₁ (right). Reference connector below x-axes showing T₂ < T₁ spacing. Curves drawn with distinguishable Okabe-Ito colors. Each curve identified by a color-coded legend swatch (post-production). Smooth exponential curves, no markers.

`[P — PRESENTATION]` Flat vector; |ρ₀₁(t)| T₂-decay curve = Orange #E69F00; (1/2)e^{−t/(2T₁)} reference = Sky Blue #56B4E9 dashed; ρ₁₁(t) decay = Vermillion #D55E00; ρ₀₀(t) rise = Bluish Green #009E73; T₂ reference vertical line = Orange #E69F00 light dashed; T₁ reference vertical line = Blue #0072B2 light dashed; axes = Blue #0072B2 thin; connector bracket = Blue #0072B2; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Bloch sphere visualization (Figure 3); Lindblad equation structural diagram (Figure 2); T₂ = 2T₁ natural linewidth limit comparison across hardware platforms (Figure 6); purity Tr(ρ²) curve; non-Markovian non-exponential decay; dynamical decoupling modifications; specific hardware numbers.

**BLOCK 3 — NEGATIVE PROMPT:** Bloch sphere, jump operator diagram, scatter plot with individual data points, 3D bar chart, pie chart, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Pointer States and Einselection: Decoherence Basis Selection

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-column panel. Left column: a qubit shown as a Bloch sphere with a surface vector pointing at an arbitrary equatorial position (representing a superposition state α|0⟩ + β|1⟩ in a non-pointer basis). A coupling icon connects it to an environment cluster. After coupling (shown by an arrow below), the Bloch sphere icon has collapsed to a mixture of two specific points — the north pole and south pole — shown as a probability-weighted pair of open circles on the z-axis of the sphere (indicating a diagonal density matrix in the pointer basis). Right column: a qubit shown as a Bloch sphere with a surface vector at either the north or south pole (already in a pointer state). A coupling icon connects it to an environment cluster. After coupling (shown by an arrow below), the Bloch sphere icon is unchanged — the pointer state is stable, shown by an equals-arrow or check mark. Between the two columns, a vertical separator with an arrow from left to right labeled "einselection" (as a directional indicator, not text — use an arrow with a funnel icon, indicating filtering to the pointer basis). The pointer basis positions (north pole, south pole) are identified by a consistent color across both columns. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Two-column comparison: Left: superposition state in non-pointer basis → after environment coupling → mixture in pointer basis (diagonal density matrix over {|0⟩, |1⟩}). Right: pointer state (eigenstate of σ_z, i.e., north or south pole) → after environment coupling → unchanged. Pointer basis = {|0⟩, |1⟩} = {south pole, north pole} in the z-basis (because coupling Hamiltonian H_SE commutes with σ_z, selecting σ_z eigenstates as pointer states). Environment coupling shown by the same icon in both columns. Decoherence direction (superposition → mixture) as an inferred relationship — chapter's explicit statement that the environment "monitors σ_z" and destroys coherences between non-eigenstates.

`[O — ORGANIZATION]` Two columns of equal width. Within each column: top = initial qubit state (Bloch sphere icon), middle = environment coupling icon + interaction arrow, bottom = final qubit state (Bloch sphere icon). Vertical separator between columns with einselection funnel arrow pointing left-to-right. Pointer-basis positions (north/south pole) consistently marked with a shared color across both columns. Four Bloch sphere icons total.

`[P — PRESENTATION]` Flat vector; superposition initial state = Reddish Purple #CC79A7 Bloch vector; mixture final state = two open circles at north/south poles in Reddish Purple #CC79A7; pointer state (stable) = Bluish Green #009E73 Bloch vector at pole; pointer state final (unchanged) = same Bluish Green #009E73; environment coupling icon = Blue #0072B2; einselection funnel arrow = Orange #E69F00; sphere wireframes = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Lindblad equation structure; Bloch equation dynamics; T₁ and T₂ timescale numbers; measurement problem / "and → or" problem (text discussion only, not a figure); many-worlds/Bohmian interpretation comparison; macroscopic superposition scale shift (decoherence time for dust grain is a footnote, not a figure element); non-Markovian dynamics.

**BLOCK 3 — NEGATIVE PROMPT:** density matrix bar chart, amplitude bars, energy level diagram, Schrödinger cat diagram, decoherence time formula, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — T₁ vs. T₂ Across Hardware Platforms

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a grouped horizontal bar chart with four hardware platform groups on the y-axis: superconducting transmon, trapped ion, NV center in diamond, and semiconductor spin qubit. For each platform, draw two horizontal bars side by side: a longer bar for T₁ and a shorter bar for T₂ (since T₂ ≤ 2T₁ always). The bars should be log-scaled on the x-axis (since the platform timescales span microseconds to seconds) — indicate log scale by tick marks at decades. A diagonal reference line or shaded region marks the T₂ = 2T₁ limit (natural linewidth). Platforms where T₂ ≈ 2T₁ (trapped ions) will have T₁ and T₂ bars nearly equal in length; platforms where T₂ ≪ 2T₁ (NV center at room temperature) will have a large gap between the two bars. Each platform group is visually distinct by a light row background shading. T₁ bars and T₂ bars consistently colored across all platforms. Y-axis starts at zero (0 platforms), x-axis from zero on log scale. No text labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Grouped horizontal bar chart: 4 platforms × 2 bars (T₁, T₂). Platform data from chapter's calibration table: superconducting transmon T₁ = 100–500 µs, T₂ = 50–300 µs (T₂/T₁ ≈ 0.3–0.8); trapped ions T₁ = seconds–minutes, T₂ ≈ T₁ (T₂/T₁ ≈ 1); NV center T₁ ≈ ms, T₂ = µs–ms (T₂/T₁ = 0.001–0.5); semiconductor spin qubit T₁ = 1–10 ms, T₂ = 1–100 µs (T₂/T₁ = 0.01–0.1). Bars show midrange representative values. T₂ = 2T₁ reference line as a diagonal dash-dotted line through the plot. Log x-axis spanning µs to minutes. The chapter explicitly flags these as approximate 2025–2026 representative values.

`[O — ORGANIZATION]` Horizontal grouped bar chart. Y-axis: four platform groups, labeled in post-production typography. X-axis: log scale from 1 µs to 10⁵ s (or appropriate span). Within each group: T₁ bar above, T₂ bar below, with a small gap between them. Group rows separated by light gray horizontal rules. T₂ = 2T₁ reference line passes through the plot diagonally or is shown as a reference overlay. Bar lengths represent log-scale timescales (midpoint of reported range). Y-axis starts at 0 platform count = 0 (no truncation); x-axis log scale with decade ticks.

`[P — PRESENTATION]` Flat vector; T₁ bars = Blue #0072B2; T₂ bars = Orange #E69F00; T₂ = 2T₁ reference line = Bluish Green #009E73 dashed; platform row backgrounds alternating light gray and white; x-axis ticks and lines = Blue #0072B2 thin; grouped row separator rules = light gray; uniform 1 pt strokes; white background; no baked text.

`[E — EXCLUSIONS]` Omit: Bloch equation derivation; density matrix decay curves (Figure 4); pointer states (Figure 5); photon qubit platform (T₁ = ∞, not plotted on finite scale); dynamical decoupling modified T₂ values; specific noise source mechanisms (flux noise, spin bath — text only); non-Markovian platforms; error threshold connection.

**BLOCK 3 — NEGATIVE PROMPT:** scatter plot, pie chart, 3D bar chart, stacked bars (T₁ and T₂ must be separate grouped bars), text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — System–Environment Entanglement:**
STATIC SUFFICIENT. The three stages (unentangled, partial overlap, orthogonal branches) are a comparative panel structure. The continuous process of branch separation can be conveyed as a three-panel static sequence without requiring animation.

**Figure 2 — Lindblad Equation Structure:**
STATIC SUFFICIENT. A structural decomposition diagram — taxonomic, not temporal. No causal sequence to animate.

**Figure 3 — Bloch Vector Dynamics Three Regimes:**
VIDEO CANDIDATE. Criterion: the transformation of the Bloch vector from the sphere surface to the interior/equilibrium point is the chapter's central learning target, and it involves ≥3 sequential causal stages (precession, transverse decay, longitudinal relaxation acting simultaneously). The spiral inward — especially the combined case where both T₁ and T₂ are active and the vector traces a continuous curve from equator to south pole — is a spatial transformation directly below intuition for students who have only seen Bloch vectors on the surface. The three simultaneous regimes side by side would be even clearer in animation: showing all three spirals evolving in real time on the same clock makes the T₂ ≤ 2T₁ constraint visceral. This is the chapter's recommended video.

**Figure 4 — Density Matrix Decay Curves:**
STATIC SUFFICIENT. Exponential decay curves are standard line charts; the off-diagonal and diagonal decays are well-conveyed as static overlaid lines sharing a time axis.

**Figure 5 — Pointer States and Einselection:**
STATIC SUFFICIENT. A before/after comparison of two parallel cases. The pedagogic content is the contrast between stable and unstable states under coupling, not a temporal process.

**Figure 6 — T₁ vs. T₂ Hardware Platform Chart:**
STATIC SUFFICIENT. A reference grouped bar chart; no temporal process or transformation.

**Recommended video:** Figure 3 — Bloch Vector Dynamics (Bloch vector spiraling from sphere surface to equilibrium under combined dephasing and relaxation, shown in real time with all three regimes animated simultaneously).
