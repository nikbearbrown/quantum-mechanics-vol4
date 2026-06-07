# CAJAL Figure Intelligence — 07-measurement-and-interpretations

**Source:** books/quantum-mechanics-vol4/chapters/07-measurement-and-interpretations.md
**Scan mode:** /scan silent
**Date:** 2026-06-06

**Domain note:** This chapter covers contested interpretations. All figures that depict interpretation-specific claims must represent each position with identical visual weight — no interpretation is shown as correct, favored, or ruled out. Figures depicting decoherence decay and CSL parameter constraints are factual and non-contested; treat them as standard PQ/MC.

---

## Zones Detected

**MC — Mechanism/Process (3+ interdependent steps)**

- Von Neumann measurement chain (Sections "The Two Rules" and "The Von Neumann Measurement Chain," Worked Example): system S in superposition → pre-measurement entangles S with apparatus A → apparatus couples to environment E, off-diagonal density matrix elements decay → observer O entangles with chain; no step yields a single outcome; cut location is the interpretive question. Four causally ordered stages, each building on the previous.
- Two dynamical rules and their incompatibility: Rule 1 (unitary evolution) preserves superpositions; Rule 2 (projection postulate) eliminates them; the chapter states "no principle specifies when 'measurement' begins" as the logical gap between the two rules. Three components in structural tension.

**VG — Verification Gap (structural/spatial claims not visually grounded)**

- Where each interpretation places the von Neumann cut is laid out in explicit parallel prose (Worked Example: "Copenhagen places the cut between apparatus and environment… Many-worlds places no cut… GRW/CSL inserts a stochastic collapse event at Step 2 or 3…"). This six-way parallel positional claim is asserted in text and the summary table, never shown on a shared visual axis.
- Decoherence "solves the basis problem but not the outcome problem" is the chapter's central logical distinction. After decoherence, ρ_SA is approximately diagonal but both diagonal terms (|α|² and |β|²) remain nonzero. This two-part claim — off-diagonal elements gone, diagonal elements both still present — is spatial/structural and not visually grounded.

**PQ — Proportional/Quantitative Data**

- Decoherence timescale for macroscopic objects: 10^{-36} s for dust in air. No chart needed; single number, no comparison axis.
- GRW hit rate scaling: for N ~ 10^{23} particles, Nλ ~ 10^6 s^{-1} vs. single-particle λ ~ 10^{-17} s^{-1}. Quantitative scaling relationship across ~23 orders of magnitude — chartable as a bar or log-scale comparison.
- CSL parameter space: the chapter describes two named parameter points (GRW original, Adler) and three experimental constraint sources (LISA Pathfinder, optomechanical experiments, molecular interferometry) narrowing the allowed region. A 2D parameter-space plot with exclusion boundaries and named points is warranted and data-grounded.
- Interpretation survey (Schlosshauer et al. 2013, n = 33): Copenhagen-adjacent 42%, information-theoretic 24%, many-worlds 18%, other/none 16%. Four bars, y-axis at zero — PQ.

---

**Density recommendation: 4 figures, Mixed density.**

---

## Figure 1 — CRITICAL

**Concept:** The von Neumann measurement chain expands through four entanglement steps — S alone, S+A entangled, S+A+E entangled with off-diagonal elements decayed, S+A+E+O entangled — yet at no stage does unitary evolution select a single outcome; decoherence suppresses off-diagonal terms but both diagonal populations remain.

---

**Block 1 — Illustrae Paste Block**

Draw a full-width 120 mm vector canvas, white background. Draw four rectangular nodes in a horizontal row from left to right, connected by three single-headed 1 pt #000000 arrows. Left node: 16×10 mm rectangle with 1 pt #0072B2 outline, no fill — this is system S. Second node: 16×10 mm rectangle with 1 pt #56B4E9 outline — apparatus A. Third node: 16×10 mm rectangle with 1 pt #009E73 outline — environment E. Fourth node: 16×10 mm rectangle with 1 pt #E69F00 outline — observer O. Below the arrow between node 2 and node 3 (the S+A to S+A+E transition), draw a small 2×2 schematic grid of four squares in 0.5 pt #000000: fill the two diagonal squares (#0072B2 solid fill) and draw the two off-diagonal squares in light gray with a diagonal strikethrough line in 1 pt #D55E00, indicating that off-diagonal coherences decay at this step while diagonal populations survive. Draw a thin 1 pt #D55E00 dashed arc from below the third node (E) connecting back to below the second node (A), shaped like a partial loop and ending without arrowhead, indicating the environment-induced suppression acts on S+A. All four nodes are equally sized and equally spaced. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Full-width 120 mm vector, white background, four-node horizontal chain with a density matrix inset below the E-coupling arrow.

[C] Content confirmed in chapter: Step 0 — system S in superposition α|↑⟩ + β|↓⟩; Step 1 — pre-measurement entangles S and A: |Ψ1⟩ = α|↑⟩|A↑⟩ + β|↓⟩|A↓⟩; Step 2 — apparatus couples to environment: |Ψ2⟩ = α|↑⟩|A↑⟩|E↑⟩ + β|↓⟩|A↓⟩|E↓⟩, ⟨E↑|E↓⟩ → 0 so ρ_SA becomes approximately diagonal; Step 3 — observer O entangles: |Ψ3⟩ adds |O_"up"⟩ and |O_"down"⟩ branches; both diagonal terms remain; no single outcome is selected at any step. The 2×2 density matrix schematic shows: diagonal elements |α|² and |β|² survive (filled), off-diagonal terms suppressed (strikethrough).

[O] Four nodes left-to-right: S (#0072B2), A (#56B4E9), E (#009E73), O (#E69F00). Three single-headed connecting arrows between nodes. Density matrix inset placed below the A→E arrow position, showing 4 cells: 2 diagonal filled (#0072B2), 2 off-diagonal struck-through (#D55E00 strikethrough on light gray). Decoherence feedback arc below nodes 2–3 in #D55E00 dashed. All left-to-right flow.

[P] Flat vector, Okabe-Ito hexes only: S node #0072B2, A node #56B4E9, E node #009E73, O node #E69F00, connecting arrows #000000, density matrix diagonal fills #0072B2, off-diagonal strikethrough #D55E00, decoherence arc #D55E00 dashed. All strokes 1 pt. White background. Unannotated.

[E] Explicit exclusions: where any interpretation places its cut (that belongs in Figure 2); state vector formulas or Dirac notation baked into node shapes; wave function symbol ψ embedded anywhere; probability bar charts; numerical decoherence timescale baked in; Lindblad operators; pointer basis selection mechanism as a separate diagram; more than four chain nodes; pilot wave or particle position indicator; Born rule derivation geometry.

---

**Block 3 — Negative Prompt**

Interpretation cut markers in this figure, state vector formulas baked in, Dirac notation embedded in shapes, wave function symbol embedded, probability bar chart, decoherence timescale numbers baked in, Lindblad operators, pointer basis geometry, more than four chain nodes, pilot wave indicator, Born rule derivation; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 2 — CRITICAL

**Concept:** Each of six major interpretations places the von Neumann cut — or eliminates it — at a different position in the same S→A→E→O chain; showing all six on a shared neutral chain reveals the logical structure of their disagreement without privileging any.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background, six equal-height rows stacked vertically, each row 14 mm tall with 2 mm vertical spacing. In each row, draw four small 10×6 mm rectangles (node boxes) in a horizontal row connected by three 1 pt #000000 single-headed arrows, representing S, A, E, O in that order — all node boxes identical in size, 1 pt #000000 outline, white fill, equal spacing. Row 1 (Copenhagen): place a 1.5 pt #CC79A7 dashed vertical bar between the A and E nodes. Row 2 (Many-worlds): no cut marker; all four node outlines changed to 1.5 pt #009E73 to indicate all branches persist equally. Row 3 (Bohmian): no cut on the chain; add a small 4 pt filled #0072B2 circle below the S node connected by a short 0.5 pt #000000 dashed line indicating particle position. Row 4 (GRW/CSL): place a 6 pt #E69F00 starburst or sunburst marker centered on the E node, indicating physical collapse at the environment stage. Row 5 (QBism): place a 1.5 pt #CC79A7 solid vertical bar between the E and O nodes. Row 6 (Consistent histories): draw a 1.5 pt #56B4E9 horizontal bracket spanning all four nodes above the row, indicating the full chain is subject to framework choice. No row is visually heavier or more prominent than any other — all cut markers are 1.5 pt maximum, equal across rows. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, six-row vertical comparison panel, each row containing the identical S→A→E→O chain.

[C] Content confirmed in chapter: Copenhagen — cut between classical apparatus and quantum system, placed pragmatically between A and E; Many-worlds — no cut, all branches equally real, observer O in superposition; Bohmian — no cut on wave function, but particle has definite position; GRW/CSL — stochastic physical collapse event at Step 2 or 3, at E or A+E junction, collapses superposition instantaneously for macroscopic systems; QBism — cut at the agent's experience, between O and the world; Consistent histories — framework choice spans the full chain. Six distinct cut-position conventions, all derived from the chapter's Worked Example section.

[O] Six rows, equal height, equal spacing. Each row: four nodes S-A-E-O with three connecting arrows. Cut marker per row at the position stated in the chapter. Row 1 (Copenhagen): dashed bar between A and E (#CC79A7). Row 2 (Many-worlds): no bar, #009E73 node outlines. Row 3 (Bohmian): no bar, particle-position marker below S (#0072B2). Row 4 (GRW/CSL): starburst on E node (#E69F00). Row 5 (QBism): solid bar between E and O (#CC79A7). Row 6 (Consistent histories): bracket spanning all four nodes (#56B4E9). All six rows identical visual weight.

[P] Flat vector, Okabe-Ito hexes only: default node boxes #000000 outline white fill, Many-worlds node outlines #009E73, connecting arrows #000000, Copenhagen and QBism cut bars #CC79A7 dashed and solid respectively, Bohmian particle marker #0072B2, GRW starburst #E69F00, Consistent histories bracket #56B4E9. All strokes 1 pt except cut markers at 1.5 pt maximum. White background. Unannotated.

[E] Explicit exclusions: any endorsement marker (checkmark, star, larger node) on any row; Born rule derivation geometry; decoherence timescale numbers; Frauchiger-Renner thought experiment elements; Relational QM as a seventh row (brief-note status only in chapter); philosophical argument text; probability bar chart for any interpretation; CSL parameter space (belongs in Figure 3); the two dynamical rules diagram (belongs in Figure 1).

---

**Block 3 — Negative Prompt**

Endorsement checkmark or star on any row, one row bolder or larger than others, Born rule derivation, decoherence timescale, Frauchiger-Renner elements, Relational QM seventh row, probability bars for interpretations, CSL parameter space, two-dynamical-rules diagram; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 3 — IMPORTANT

**Concept:** The CSL parameter space (collapse rate λ vs. correlation length r_C) has two named reference points — the original GRW parameters and the higher-λ Adler parameters — and three experimental constraint boundaries (LISA Pathfinder, optomechanics/GW detectors, molecular interferometry) progressively excluding the parameter space, with the Adler region under pressure and the original GRW point surviving.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background, a log-log scatterplot. Draw a horizontal axis (r_C, log scale, from 10^{-9} m to 10^{-4} m) in 1 pt #000000 with five log-spaced tick marks. Draw a vertical axis (λ, log scale, from 10^{-20} s^{-1} to 10^{-7} s^{-1}) in 1 pt #000000 with six log-spaced tick marks. Draw three exclusion boundary curves, each as a 1.5 pt smooth curve: Curve 1 in #0072B2 sweeping from upper-left to mid-panel (LISA Pathfinder constraint), with a 10% #0072B2 tinted hatch region above and to its left. Curve 2 in #E69F00 sweeping from upper-right to lower-right (optomechanics and GW detector constraints), with a 10% #E69F00 tinted hatch region above it. Curve 3 in #56B4E9 representing the molecular interferometry upper bound, a roughly horizontal curve in the upper portion of the panel, with 10% #56B4E9 tint above it. Draw the surviving white (unexcluded) region at the lower portion of the panel. Place a 6 pt filled #009E73 circle at the GRW parameter coordinates (r_C ~ 10^{-7} m, λ ~ 10^{-17} s^{-1}) within the surviving region. Place a 6 pt filled #E69F00 diamond at the Adler parameter coordinates (r_C ~ 10^{-7} m, λ ~ 10^{-8} s^{-1}) near or within an exclusion boundary. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, log-log 2D parameter space plot with exclusion regions and named parameter points.

[C] Content confirmed in chapter: CSL free parameters are collapse rate λ and correlation length r_C; original GRW parameters λ ~ 10^{-17} s^{-1}, r_C ~ 10^{-7} m; Adler parameters λ ~ 10^{-8} s^{-1}, same r_C; three constraint sources: LISA Pathfinder (femtometer-scale position noise of gram-scale mass, excludes large portions at high λ); optomechanical experiments with levitated nanospheres (constrain collapse-induced diffusion); molecular interferometry (Arndt group, sets upper bounds from fringe visibility); original GRW parameters survive; Adler parameters are under pressure; allowed parameter space is shrinking; this is a live experimental program as of 2026.

[O] Log-log axes: horizontal r_C (10^{-9} to 10^{-4} m), vertical λ (10^{-20} to 10^{-7} s^{-1}). Three exclusion boundaries as distinct colored curves with light tint hatching in the excluded region. White surviving region at lower-left. GRW point inside surviving region (#009E73 filled circle). Adler point at or near a boundary (#E69F00 filled diamond). No more than three boundary curves — matches the three experimental sources named in the chapter.

[P] Flat vector, Okabe-Ito hexes only: LISA boundary #0072B2, optomechanics/GW boundary #E69F00, interferometric boundary #56B4E9, exclusion tints 10% opacity matching boundary colors, GRW point #009E73, Adler point #E69F00 (diamond shape to distinguish from GRW circle), axes #000000. Boundary curves 1.5 pt. Axis lines 1 pt. Tick marks 1 pt. White background. Unannotated.

[E] Explicit exclusions: relativistic extension constraints (not in chapter); specific numerical tick values baked into axes; error bars on the parameter points; fourth or fifth exclusion boundary beyond the three named in chapter; any interpretation-comparison element (this figure is physics of the GRW/CSL model only); the GRW collapse mechanism diagram; probability bars for other interpretations; Lindblad operators; Bloch sphere or circuit elements.

---

**Block 3 — Negative Prompt**

Relativistic extension constraints, numerical tick values baked in, error bars, fourth or fifth exclusion boundary, interpretation-comparison elements, GRW mechanism diagram, probability bars for interpretations, Lindblad operators, Bloch sphere, circuit elements; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Figure 4 — SUPPLEMENTARY

**Concept:** Among physicists surveyed (Schlosshauer et al. 2013, n = 33 at a foundations conference), Copenhagen-adjacent preference is 42%, information-theoretic 24%, many-worlds 18%, and other/none 16% — a distribution that reflects genuine ongoing disagreement, not consensus.

---

**Block 1 — Illustrae Paste Block**

Draw a single-column 89 mm vector canvas, white background. Draw a horizontal x-axis in 1 pt #000000 from 0 to 50 (representing percent), y-axis at left starting at zero. Draw four horizontal bars stacked from top to bottom: the top bar extends to 42 units in #56B4E9 (Copenhagen-adjacent); the second bar extends to 24 units in #56B4E9; the third bar extends to 18 units in #56B4E9; the bottom bar extends to 16 units in #56B4E9. All bars are 8 mm tall, uniformly spaced 4 mm apart, with 1 pt #000000 outlines. Draw a thin 0.5 pt #000000 dashed vertical reference line at x = 25 (the 25% equal-share baseline for four categories). All bars share the same color — no bar is visually privileged over another. No text; unannotated.

---

**Block 2 — Full SCOPE Prompt**

[S] Single-column 89 mm vector, white background, horizontal bar chart, y-axis at zero, x-axis from 0 to 50 percent.

[C] Content confirmed in chapter: Schlosshauer, Kofler, Zeilinger (Am. J. Phys. 81:325, 2013) survey of 33 physicists at a foundations conference: Copenhagen-adjacent 42%, information-theoretic (including QBism-adjacent) 24%, many-worlds 18%, other/none 16%. Four bars representing these four categories. X-axis is percentage. Dashed reference line at 25% indicates the equal-share baseline for four categories. All four percentages sum to 100%.

[O] Four horizontal bars, top to bottom, lengths proportional to percentages (42, 24, 18, 16 of a shared 50-unit axis). Shared horizontal x-axis at bottom. Y-axis at left (category labels added post-production). Dashed vertical reference line at x = 25. Uniform bar height and spacing. No differential coloring.

[P] Flat vector, Okabe-Ito hexes only: all four bars #56B4E9 uniform, bar outlines 1 pt #000000, axes 1 pt #000000, reference line 0.5 pt #000000 dashed. White background. Unannotated.

[E] Explicit exclusions: any differential coloring between bars that implies hierarchy; the 2025 arXiv review (it produced no comparable quantitative survey data and must not be fabricated as data points); post-2013 survey data; interpretation-endorsement visual cues; CSL parameter space (belongs in Figure 3); taxonomy matrix of empirical equivalence (kept out of this figure to avoid overloading — the chapter's summary table in prose covers it); decoherence timescale bars; the von Neumann chain (belongs in Figure 1).

---

**Block 3 — Negative Prompt**

Differential bar colors implying preference, post-2013 survey data, fabricated data points from 2025 review, endorsement checkmarks, CSL parameter space, empirical-equivalence taxonomy columns, decoherence timescale bars, von Neumann chain; text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, non-standard arrows, dual-headed arrows, hand-drawn styles, visual clutter, watermarks, red-green color combinations, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 (Von Neumann measurement chain):** VIDEO CANDIDATE. Criterion: four sequential causal stages where the transformation mechanism is the learning target AND one stage produces a qualitative change (off-diagonal suppression at the E node) that is genuinely a transition, not just a state. The central pedagogical distinction of this chapter — decoherence extinguishes off-diagonals but leaves both diagonal populations nonzero — is most clearly taught as a transition: watching the off-diagonal cells of the density matrix inset fade while the diagonal cells remain. A loop showing the chain nodes appearing left to right, with the density matrix inset cells animating (off-diagonal fade to gray, diagonal cells hold at #0072B2 fill) at the E-coupling step, directly teaches what decoherence does and does not do. Recommended video for this chapter.

**Figure 2 (Interpretation cut comparison):** Not a video candidate. The learning target is synchronic comparison of six positions on the same chain — a task best served by side-by-side static rows allowing direct parallel reading. Animation would serialize what should be compared simultaneously.

**Figure 3 (CSL parameter space):** Not a video candidate. A static constraint map; no time-sequence or cyclic mechanism is the learning target.

**Figure 4 (Survey bar chart):** Not a video candidate. Four static bars; no sequential or transformational content.

**Video candidate count: 1 (von Neumann chain with density matrix transition). Recommendation: 6-second loop — nodes S, A, E, O appear left to right sequentially (3 s), then at the E-coupling step the density matrix inset animates (off-diagonal cells fade from #0072B2 to light gray over 1.5 s while diagonal cells remain fully saturated, held 0.5 s), then reset. Flat vector, Okabe-Ito colors, no text.**
