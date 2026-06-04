# CAJAL Figure Report — Chapter 8 — Quantum Hardware: From Formalism to Physical Qubits

**Source:** `chapters/08-quantum-hardware.md`
**Mode:** `/scan silent`
**Domain note:** Hardware-comparison chapter with rapidly aging numbers. Quantitative figures should encode structural comparisons (order-of-magnitude ratios between platforms, T1 vs T2 relationship, N_gates figure of merit) not specific quoted values. Structural schematics (transmon circuit topology, NV center crystal structure) are evergreen. The chapter explicitly flags that hardware numbers will be wrong within a year; figures must be designed so the structural insight survives even when tick-mark values are updated.

---

Recommended: 7 figures, Mechanistic density.

---

## Figure 8.1 — DiVincenzo criteria as a rubric: five requirements on one axis

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a matrix diagram with five rows (one per DiVincenzo criterion) and six columns (one per platform: superconducting transmon, trapped ion, neutral atom, photonic, NV center, spin qubit). At each cell, place a shape indicating how well the platform satisfies that criterion: filled circle for satisfies, half-filled circle for partial, empty circle for does not satisfy at scale. The five criterion rows are: scalable physical system, initialization, coherence-to-gate ratio, universal gates, qubit-specific measurement. The matrix uses only geometric shapes — no text baked in. All cells the same size. All platform columns the same width. All criterion rows the same height. The shape encoding is purely geometric: filled, half-filled, empty.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Matrix layout, approximately 89×65mm. Six columns, five rows.
- `[C — CONTENT]` Five DiVincenzo criterion rows: (i) scalable physical system, (ii) initialization, (iii) long coherence relative to gate time, (iv) universal gates, (v) qubit-specific measurement. Six platform columns: superconducting, trapped ion, neutral atom, photonic, NV center, spin qubit. Cell encoding: filled circle = satisfies criterion at current scale; half-filled circle = partial/limited; empty circle = does not satisfy at scale. Representative fills (from chapter content): Criterion i — superconducting: filled; trapped ion: half; neutral atom: filled; photonic: empty; NV: empty; spin qubit: half. Criterion iii (coherence/gate ratio) — superconducting: half; trapped ion: filled; neutral atom: half; photonic: empty (probabilistic gates); NV: empty; spin qubit: half. Criteria ii and v: all platforms filled or near-filled. Criterion iv (universal gates): photonic: half (probabilistic); all others: filled. Row and column labels applied post-production via typography. Cell grid lines: light gray 0.5pt.
- `[O — ORGANIZATION]` Six-column, five-row matrix. Columns = platforms (left to right: superconducting, trapped ion, neutral atom, photonic, NV center, spin qubit). Rows = DiVincenzo criteria (top to bottom: criterion i through v). Cell shapes centered in each cell. No color differential between platforms — shape fill is the only encoding.
- `[P — PRESENTATION]` Filled circles: Blue `#0072B2`. Half-filled circles: Sky Blue `#56B4E9` (left half filled). Empty circles: light gray outline, white fill. Cell background: white. Grid lines: light gray 0.5pt. Circle diameter: 70% of cell width. Uniform 1pt stroke on circle outlines. No platform-specific color coding — shape encoding only, to avoid privileging platforms visually.
- `[E — EXCLUSIONS]` Do not include specific T1, T2, or gate time values baked in — those belong to Fig 8.4. Do not show the Bloch sphere here — that is Fig 8.5. Do not add a "winner" highlight. Do not show topological qubits (not covered in chapter). Do not add footnote symbols baked into cells.

**BLOCK 3 — NEGATIVE PROMPT**

Color-coded platform columns implying ranking, checkmark/X notation instead of geometric encoding, one platform cell larger than others, specific numerical values baked into cells, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.2 — Transmon circuit topology: anharmonic LC oscillator

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a circuit schematic of the transmon qubit. Show a loop circuit containing two elements in series: a linear capacitor (standard capacitor symbol: two parallel plates) and a Josephson junction (standard cross-in-box symbol used in superconducting circuit diagrams, or an X symbol within a square). Label the capacitor element zone as C (charging energy E_C) and the Josephson junction zone as J (Josephson energy E_J). Below the main qubit loop, add a second coupled resonator loop connected via a coupling capacitor, representing the readout resonator used for dispersive readout. Mark the coupling element with a different visual weight. Add a small inset panel to the right showing the energy level ladder: a harmonic oscillator ladder (equally spaced levels) with a bracket showing that transmon levels are unequally spaced — the spacing between level 1 and level 2 is slightly less than between level 0 and level 1, with the difference marked as the anharmonicity alpha. The two lowest levels are highlighted as the qubit subspace. Request blank, unannotated vector diagram. No text baked in.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Two-panel layout: left panel (circuit schematic, approximately 55mm wide), right panel (energy level inset, approximately 30mm wide).
- `[C — CONTENT]` Left panel: transmon loop — capacitor symbol (two parallel lines) connected in series with Josephson junction symbol (box with X). Loop closes on itself. Second loop below: readout resonator (inductor + capacitor) coupled to qubit loop via coupling capacitor symbol. Right panel: energy level ladder, 4 levels shown. Levels 0 and 1 are the qubit subspace — marked with a bracket or shading. Spacing between levels 0→1 labeled omega-01 zone; spacing between levels 1→2 labeled omega-12 zone; the difference (anharmonicity alpha) marked with a double-headed bracket between the two spacing values. Harmonic oscillator reference shown as dotted equally-spaced levels for contrast. All element labels (C, E_J, E_C, alpha, qubit subspace) applied post-production via typography.
- `[O — ORGANIZATION]` Left: circuit schematic, top = qubit loop, bottom = readout resonator, coupling element at boundary. Right: vertical energy ladder, levels horizontal lines of equal length, spacing visibly unequal (anharmonic), qubit subspace bracket on left. Both panels share a common baseline.
- `[P — PRESENTATION]` Qubit loop: Blue `#0072B2` 1.5pt. Josephson junction symbol: Vermillion `#D55E00` (distinguishes it as the nonlinear element). Capacitor symbol: Blue `#0072B2`. Readout resonator: Sky Blue `#56B4E9` 1pt. Coupling capacitor: Orange `#E69F00`. Energy levels: dark gray 1pt horizontal lines. Qubit subspace bracket: Bluish Green `#009E73`. Anharmonicity bracket: Orange `#E69F00`. Harmonic reference levels: light gray dashed. White background. No baked text.
- `[E — EXCLUSIONS]` Do not show the full charge-basis Hamiltonian baked into the figure. Do not depict gate microwave pulse delivery (that belongs to Fig 8.3). Do not show the readout resonator transmission line or cryogenic wiring. Do not include the full transmon energy level series beyond 4 levels. Do not depict quasiparticle poisoning noise sources.

**BLOCK 3 — NEGATIVE PROMPT**

Harmonic oscillator and transmon levels drawn as equally spaced (the unequal spacing is the point), Josephson junction shown as a simple resistor symbol, 3D circuit board rendering, realistic device photo elements, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.3 — NV center crystal structure and two-level projection

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a two-panel schematic of the nitrogen-vacancy center. Left panel: a crystal lattice fragment showing a diamond carbon lattice with two marked defects adjacent to each other — one substitutional nitrogen atom (distinctly shaped or colored) and one vacant lattice site (empty circle or gap). Show the four nearest carbon neighbors to the vacancy, with bonds drawn as lines. Mark the NV axis (the line from nitrogen to vacancy) with a dashed arrow. This is a structural schematic — no realistic crystal rendering. Right panel: the spin-1 energy level diagram. Show three horizontal energy levels labeled m_s equals zero (lowest), m_s equals minus one, and m_s equals plus one. At zero field, the m_s equals plus one and m_s equals minus one levels are degenerate at energy D (2.87 GHz above m_s equals zero), with a double-ended bracket marking D. With applied magnetic field, show the splitting of m_s equals plus one (shifted up) and m_s equals minus one (shifted down) by the Zeeman effect. Bracket the m_s equals zero and m_s equals minus one subspace as the qubit subspace. No text baked in.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Two-panel layout: left approximately 40mm (crystal schematic), right approximately 45mm (energy levels).
- `[C — CONTENT]` Left panel: diamond lattice fragment (approximately 5×5 unit cells in 2D projection). Carbon atoms: filled circles, uniform size. Nitrogen atom: filled circle in Orange `#E69F00`, same size as carbon. Vacancy: empty circle with dashed outline at adjacent lattice site. Bond lines: 1pt. NV axis: dashed arrow from N to V. Right panel: three horizontal energy level lines. m_s=0: lowest level, Blue `#0072B2`. m_s=±1 at zero field: two coincident lines (shown as one double line or very closely spaced) at height D above m_s=0. With B field: m_s=+1 level shifted upward, m_s=-1 level shifted downward — shown as split lines with Zeeman split bracket. Qubit subspace bracket spanning m_s=0 and m_s=-1 in Bluish Green `#009E73`. Labels: D bracket (zero-field splitting), Zeeman splitting bracket, qubit subspace bracket — all post-production typography.
- `[O — ORGANIZATION]` Left: flat 2D lattice projection. Right: vertical energy level diagram (energy increases upward). Both panels left-aligned at baseline. The qubit subspace bracket in the right panel explicitly connects to the two lowest levels of the Zeeman-split diagram.
- `[P — PRESENTATION]` Carbon atoms: dark gray filled circles. Nitrogen atom: Orange `#E69F00` filled circle. Vacancy: empty dashed circle. Bonds: dark gray 1pt. NV axis arrow: Reddish Purple `#CC79A7` dashed. Energy levels: Blue `#0072B2` 1.5pt. Qubit subspace bracket: Bluish Green `#009E73`. Zeeman split bracket: Sky Blue `#56B4E9`. D bracket: Orange `#E69F00`. White background. No baked text.
- `[E — EXCLUSIONS]` Do not show the optical readout path (intersystem crossing, triplet states) — this is out of scope for the two-level mapping figure. Do not show the full spin-1 Hamiltonian notation baked in. Do not depict the microwave antenna or readout setup. Do not show more than one NV center (single-defect schematic only). Do not include the hyperfine coupling to the nitrogen nuclear spin in the energy level diagram (the chapter treats it as a perturbative correction only).

**BLOCK 3 — NEGATIVE PROMPT**

Realistic crystal rendering, 3D ball-and-stick model with shadows, optical path shown alongside crystal structure, more than one NV defect in lattice, intersystem crossing states included (triplet A1 state, singlet S0), text labels baked into crystal, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.4 — Platform comparison: T1, T2, gate time, and N_gates on log axes

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a grouped horizontal bar chart comparing six qubit platforms across three figures of merit: T1 (energy relaxation time), T2 (coherence time), and N_gates (number of two-qubit gates per coherence cycle, computed as T2 divided by two-qubit gate time). Six platform rows: superconducting transmon, trapped ion, neutral atom, NV center, and spin qubit (omit photonic for this chart as T1 and gate time are not directly comparable). Each row contains three bars side by side. All three bar groups share a single logarithmic x-axis covering approximately 10 to 10^10 (in nanoseconds for times; dimensionless for N_gates, treated separately on a second panel). Three bars per platform are color-coded by metric: T1 in one color, T2 in a second color, N_gates in a third. Y-axis (platform names) starts at zero conceptually but is categorical. X-axis starts at the log minimum — appropriate for log scale. No text baked into image. No 3D.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Two-panel layout: left panel (T1/T2 grouped bars, log x-axis in ns), right panel (N_gates bars, log x-axis dimensionless). Each panel approximately 40mm wide.
- `[C — CONTENT]` Left panel: grouped horizontal bar chart. Six platform rows (superconducting, trapped ion, neutral atom, NV center, spin qubit — 5 rows). Two bars per row: T1 (Blue `#0072B2`) and T2 (Sky Blue `#56B4E9`). Log x-axis in nanoseconds: approximately 10^5 ns (100 µs) to 10^12 ns (1000 s) to cover all platforms. Approximate representative values (structural order-of-magnitude, from chapter): superconducting T1 ~ 5×10^8 ns, T2 ~ 4×10^8 ns; trapped ion T1/T2 ~ 10^12 ns; neutral atom T1/T2 ~ 10^12 ns; NV center T1 ~ 3×10^6 ns, T2 ~ 10^6 ns; spin qubit T1 ~ 10^6 ns, T2 ~ 10^6 ns. Right panel: horizontal bar chart, same five platform rows. Single bar per row: N_gates = T2/t_gate (dimensionless). Log x-axis from 10^1 to 10^7. Approximate values: superconducting ~4000–10000; trapped ion ~10000–20000; neutral atom ~500000–10^6; NV center ~1–10 (two-qubit very limited); spin qubit ~10000. All bars terminated with no baked labels. Axis ticks and labels post-production. Bar width uniform across all platforms within each panel.
- `[O — ORGANIZATION]` Left panel: grouped bars (T1 and T2) per platform, platforms stacked vertically. Platforms sorted in descending order of T2 (trapped ion / neutral atom at top, NV center / spin qubit at bottom). Right panel: single N_gates bar per platform, same vertical order. Bars horizontal, extending rightward from y-axis. Log x-axis on both panels. Y-axis is categorical (no zero concept, but all platforms represented).
- `[P — PRESENTATION]` T1 bars: Blue `#0072B2`. T2 bars: Sky Blue `#56B4E9`. N_gates bars: Bluish Green `#009E73`. Bar height uniform (proportional spacing). Bar outlines: 0.5pt black. Log x-axis gridlines: light gray dashed. Axis lines: black 1pt. White background. No baked text.
- `[E — EXCLUSIONS]` Do not include photonic platform in this chart (gate time is probabilistic/undefined for direct comparison). Do not include two-qubit gate fidelity as a bar in this figure — it belongs to Fig 8.1 (DiVincenzo rubric). Do not include specific quoted numbers baked into bars — the figure encodes structural order-of-magnitude ratios. Do not show single-qubit gate times (the chapter's figure of merit is two-qubit). Do not show absolute qubit count/scale here — that belongs to Fig 8.1.

**BLOCK 3 — NEGATIVE PROMPT**

Linear x-axis instead of logarithmic, y-axis starting above the lowest value shown, 3D bar chart, bars differentiated by platform color instead of metric color (the metric color coding is the point), specific numerical value labels baked onto bar ends, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.5 — T1 and T2 relationship: Bloch equation structure

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a schematic diagram showing the two decay channels that govern qubit coherence and their relationship. Draw a Bloch sphere outline (circle representing the sphere in 2D orthographic projection) with the Bloch vector as an arrow from the center pointing to a position on the upper hemisphere. Show two decay processes as separate labeled arrows: one arrow pointing toward the south pole of the sphere (energy relaxation, T1 process) and one arrow spiraling inward toward the sphere surface equator (pure dephasing, T_phi process). Below the sphere, draw a box showing the formula structure for 1/T2: two additive terms, one labeled 1/(2T1) and one labeled 1/T_phi. Show by a horizontal inequality marker that T2 is at most 2T1 (the natural linewidth limit). Show a separate small marker indicating T2-star as a third shorter timescale below T2 due to inhomogeneous broadening. No text baked into image. Request blank, unannotated vector diagram.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Two-panel layout: left (Bloch sphere with decay arrows, approximately 50mm), right (timescale hierarchy bar, approximately 35mm).
- `[C — CONTENT]` Left panel: Bloch sphere outline (circle). Bloch vector: Orange `#E69F00` arrow from center to upper hemisphere. Energy relaxation arrow: Blue `#0072B2`, pointing toward south pole (downward). Pure dephasing arrow: Reddish Purple `#CC79A7`, spiraling inward toward equator of sphere. Both decay arrows labeled post-production. Right panel: vertical timescale hierarchy. Three horizontal bars stacked vertically at different lengths: T1 (longest bar), 2T1 (marked as ceiling for T2 — second bar, same length as T1 × 2 relative scale), T2 (shorter bar showing T2 ≤ 2T1), T2* (shortest bar). Bars in descending length from top. Inequality markers between bars. All labels post-production.
- `[O — ORGANIZATION]` Left: Bloch sphere center-left, decay arrows radiating from the Bloch vector tip. Right: vertical bar sequence showing timescale hierarchy from longest to shortest (top to bottom). Arrow for energy relaxation descends; arrow for pure dephasing curves inward.
- `[P — PRESENTATION]` Bloch sphere outline: light gray 1pt. Bloch vector: Orange `#E69F00` 2pt. Energy relaxation arrow: Blue `#0072B2` 1.5pt. Dephasing arrow: Reddish Purple `#CC79A7` 1.5pt. Timescale hierarchy bars: T1 in Blue `#0072B2`, T2 in Sky Blue `#56B4E9`, T2* in light gray. Inequality brackets: dark gray 1pt. White background. No baked text.
- `[E — EXCLUSIONS]` Do not show gate operations on the Bloch sphere (that belongs to the simulation exercise, not a static figure). Do not depict the full Bloch equations as baked-in notation. Do not compare platforms here (Fig 8.4's job). Do not include spin-echo pulse sequence (dynamical decoupling technique is referenced in prose but not a figure target here).

**BLOCK 3 — NEGATIVE PROMPT**

3D rendered Bloch sphere, gradient shading on sphere surface, Bloch vector shown decaying without clear directionality, T2 bar shown longer than T1 bar (violates the T2 ≤ 2T1 bound), text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.6 — Rydberg blockade gate mechanism: neutral atoms

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a three-step mechanism diagram showing the Rydberg blockade used for two-qubit entangling gates in neutral atom platforms. Step 1: two neutral atoms shown as filled circles in separate optical tweezer traps (shown as V-shaped potential wells), both in their ground qubit state, separated by a distance of approximately 10 micrometers. Step 2: one atom is excited by a laser pulse to the Rydberg state (shown as a larger circle or halo indicating the huge electric dipole moment); the interaction energy between the two atoms in the double-Rydberg state is shown as a repulsion or blockade symbol that shifts the double-excitation energy off resonance. The second atom remains in its ground state — blocked from being excited. Step 3: a controlled-phase gate has been implemented — a return pulse de-excites the first atom, leaving the two atoms in an entangled state. Show the three steps as sequential left-to-right panels. Mark the Rydberg interaction range (approximately 10 micrometers) with a double-ended bracket between atoms in Step 2. No text baked in.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Three-panel horizontal layout, each panel approximately 28mm wide, shared baseline.
- `[C — CONTENT]` Three panels: Step 1 (initial state), Step 2 (Rydberg excitation + blockade), Step 3 (gate complete). Each panel shows two atom circles positioned horizontally, with V-shaped tweezer potential wells below each. Step 1: both atoms as small filled circles (ground state). Step 2: left atom enlarged or with halo (Rydberg state, Blue `#0072B2` with outer ring in Orange `#E69F00`); right atom unchanged (ground state); blockade symbol between them (repulsion arrow or barrier shape, Vermillion `#D55E00`); double-ended bracket marking the approximately 10 µm separation. Step 3: both atoms back to small filled circles; a connecting dotted arc between them indicating entanglement (inferred relation — labeled "entangled" post-production). Laser pulse arrows shown above atoms in Steps 1→2 and 2→3. Tweezer potential wells: V-shapes below each atom in all panels.
- `[O — ORGANIZATION]` Three panels left-to-right, Step 1 to Step 3. Atoms positioned symmetrically within each panel. Panels separated by right-pointing single-headed transition arrows. Tweezer wells at panel bottom, atoms at mid-height, laser arrows at top.
- `[P — PRESENTATION]` Ground-state atoms: Blue `#0072B2` filled circles, 4mm diameter. Rydberg atom: Blue `#0072B2` core with Orange `#E69F00` outer halo ring, 8mm outer diameter. Tweezer wells: Sky Blue `#56B4E9` V-shapes 1pt. Laser arrows: Bluish Green `#009E73` downward arrows 1.5pt. Blockade symbol: Vermillion `#D55E00` barrier or repulsion marker. Entanglement arc: Reddish Purple `#CC79A7` dotted curve. Step transition arrows: dark gray 1.5pt. White background. No baked text.
- `[E — EXCLUSIONS]` Do not show the full gate Hamiltonian baked in. Do not show the atom reconfiguration / tweezers-moving step (mid-circuit transport is a feature of the platform but not the gate mechanism). Do not depict the optical tweezer laser path (only the potential well shape). Do not show more than two atoms. Do not include the Mølmer-Sørensen gate (trapped ion mechanism — different platform).

**BLOCK 3 — NEGATIVE PROMPT**

Rydberg state shown as a cloud without a clear geometric center (must remain a clearly bounded circle/halo), atoms drawn as literal atoms with electron orbits, double-headed arrows for the blockade interaction (should be a barrier marker, not a bidirectional arrow), text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 8.7 — NISQ regime: gate fidelity vs qubit count phase space

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a two-dimensional scatter diagram with physical qubit count on the horizontal axis (logarithmic, from 1 to 10,000) and two-qubit gate fidelity on the vertical axis (linear, from 0.90 to 1.00, expressed as a decimal or percentage). Plot representative points for each platform as distinct marker shapes, one per platform. Add two threshold lines: a horizontal dashed line at the surface code fault-tolerance threshold (approximately 0.99 gate fidelity), and a vertical dashed line at approximately 50 qubits (lower boundary of NISQ). Label the four quadrants produced by these two lines as four zones: below-50-qubits and below-threshold (pre-NISQ), above-50-qubits and below-threshold (NISQ), below-50-qubits and above-threshold (small-scale fault-tolerant), above-50-qubits and above-threshold (fault-tolerant target). Platform points for representative mid-2026 values: superconducting 100 qubits / 0.993 fidelity; trapped ion 50 qubits / 0.9992 fidelity; neutral atom 300 qubits / 0.995 fidelity; NV center 2 qubits / 0.90 fidelity; spin qubit 12 qubits / 0.99 fidelity. Y-axis starts at 0.90 (truncated but appropriate for this domain — the range of interest spans 0.90–1.00). No text baked in. No 3D.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single column, 89mm width, 300 DPI, SVG/EPS, white background. Single panel, approximately 89×80mm. Log x-axis, linear y-axis.
- `[C — CONTENT]` X-axis: physical qubit count, log scale 1 to 10,000. Y-axis: two-qubit gate fidelity, linear 0.90 to 1.00 (y-axis truncated at 0.90 for domain relevance — annotated post-production with "axis break" marker to indicate truncation). Platform markers: superconducting — Blue `#0072B2` filled square; trapped ion — Orange `#E69F00` filled circle; neutral atom — Bluish Green `#009E73` filled triangle; NV center — Reddish Purple `#CC79A7` filled diamond; spin qubit — Sky Blue `#56B4E9` filled pentagon. Fault-tolerance threshold: horizontal dashed line at ~0.99 in Vermillion `#D55E00` 1.5pt. NISQ lower boundary: vertical dashed line at ~50 qubits in dark gray 1pt. Four quadrant labels post-production via typography. Note: photonic omitted (fidelity is conditional/architecture-dependent, not directly comparable on this axis).
- `[O — ORGANIZATION]` Single scatter plot. Log x-axis; linear y-axis starting at 0.90 with axis-break marker at the y-axis origin. Threshold lines divide the plot into four regions. Platform markers positioned at representative mid-2026 coordinates. Quant annotation on threshold lines (post-production): "fault-tolerance threshold" on horizontal line; "NISQ lower bound (~50 qubits)" on vertical line. Legend for marker shapes applied post-production.
- `[P — PRESENTATION]` Platform markers: per color scheme above, 5–6mm diameter. Threshold lines: fault-tolerance line in Vermillion `#D55E00` dashed 1.5pt; NISQ line in dark gray dashed 1pt. Axis lines: black 1pt. Log x-axis gridlines: light gray 0.5pt dashed. Linear y-axis gridlines at 0.90, 0.95, 0.99, 1.00: light gray 0.5pt dashed. Quadrant background fills: NISQ zone — very light Orange `#E69F00` at 8% opacity; fault-tolerant target zone — very light Bluish Green `#009E73` at 8% opacity; other zones — white. White background. No baked text.
- `[E — EXCLUSIONS]` Do not include logical qubit counts (only physical qubit counts). Do not show error correction code distances. Do not indicate which platform "wins" by larger markers or bold outlines. Do not include the megaquop threshold as a third axis — keep the diagram two-dimensional. Do not show time arrows (this is a snapshot of mid-2026 state, not a trajectory). Do not include photonic platform (gate fidelity not directly comparable).

**BLOCK 3 — NEGATIVE PROMPT**

Y-axis starting at zero (would make the 0.90–1.00 range invisible), one platform marker larger or bolded to indicate a winner, trajectory arrows showing platform improvement over time, error bars on platform markers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 8.1 — DiVincenzo rubric matrix:** STATIC SUFFICIENT. The rubric is a synchronic comparison of six platforms across five criteria. A static matrix enables direct cross-platform reading, which is the learning target.

**Figure 8.2 — Transmon circuit topology:** STATIC SUFFICIENT. Circuit schematic and energy level anharmonicity are spatial/structural content; no time-sequence or cyclical mechanism is the learning target.

**Figure 8.3 — NV center crystal and energy levels:** STATIC SUFFICIENT. Crystal structure and Zeeman splitting are structural/spatial content; animation would not add information not already encoded in the two-panel static layout.

**Figure 8.4 — Platform comparison log bars:** STATIC SUFFICIENT. Bar charts encode static comparative values; the log-scale comparison across platforms is readable in a static figure.

**Figure 8.5 — T1/T2 Bloch decay:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The T1 and T_phi decay processes involve distinct geometric trajectories on the Bloch sphere — T1 drives the vector toward the south pole while T_phi drives it toward the equatorial surface. A static figure captures the direction of each decay but not the trajectory over time. The key pedagogical distinction (energy relaxation vs. phase randomization are geometrically different) is most clearly shown as a short looped animation of the Bloch vector decaying under each process separately, then together. **Recommended video for this chapter.**

**Figure 8.6 — Rydberg blockade:** STATIC SUFFICIENT. The three-panel sequential layout (Step 1 → Step 2 → Step 3) encodes the mechanism spatially. The blockade is a threshold effect, not a smooth temporal transition; the three-step panel layout is pedagogically more legible than an animation for this content.

**Figure 8.7 — NISQ phase space:** STATIC SUFFICIENT. Scatter diagram encodes a static comparison; no cyclical or sequential process is the learning target.
