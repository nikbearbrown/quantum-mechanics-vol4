# CAJAL Figure Report — Chapter 1 — Mixed States and the Density Matrix

Recommended: 4 figures, Mixed density.

---

## Figure 1 — Bloch Ball: Pure Surface, Mixed Interior, Maximally Mixed Center

**Heuristic:** VG — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a transparent sphere of unit radius in three-dimensional perspective, viewed from a vantage point above and to the right so that the x, y, and z axes are all visible. The sphere surface represents all pure single-qubit states; mark three canonical pure-state points on the surface with filled circles: one at the north pole (top of z-axis), one at the positive x-axis intersection, and one at the positive y-axis intersection. Draw a single point at the exact geometric center of the sphere representing the maximally mixed state. Draw a short radial arrow from the center to an interior point (not on the surface, roughly halfway between center and surface), representing a generic mixed state. Draw three coordinate axes extending slightly beyond the sphere surface. The exterior labels will be added in post-production; leave all annotation positions blank. Use flat vector rendering on a white background with no gradient fills. No text baked into the image.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Slight three-quarter perspective so all three axes are distinguishable.
- `[C — CONTENT]` Unit sphere (Bloch ball boundary); three labeled pure-state anchor points: $|0\rangle$ at north pole (0,0,1), $|{+}\rangle$ at (1,0,0), $|{i}\rangle$ or $|{+y}\rangle$ at (0,1,0); single interior point indicating a generic mixed state with a radial Bloch vector arrow from origin; filled circle at origin indicating $\tfrac{1}{2}\hat I$ (maximally mixed); three Cartesian axes $r_x$, $r_y$, $r_z$. The Bloch vector length $|\vec r|$ is the purity measure — inferred relationship, labeled.
- `[O — ORGANIZATION]` Three-quarter-view sphere, z-axis vertical. Pure-state markers on surface as filled circles (Sky Blue). Mixed-state interior point as filled circle (Orange). Origin center-point as filled circle (neutral gray). Bloch vector arrow from origin to interior point (Blue). Axis lines as thin gray rules extending through the sphere, terminating just outside.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Surface points: Sky Blue `#56B4E9`. Interior mixed-state point and Bloch vector: Blue `#0072B2`. Origin/maximally mixed: light gray. Sphere wireframe outline: light gray thin stroke (0.5 pt). Axes: neutral gray 1 pt. All strokes uniform 1 pt except sphere outline at 0.5 pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: latitude/longitude grid lines on sphere surface; decoherence trajectory arrows; multiple Bloch vectors; quantum gate rotation arcs; eigenvalue annotations; any density matrix matrix-element display; Wigner function or Q-function representations.

**BLOCK 3 — NEGATIVE PROMPT**

latitude grid lines on sphere, multiple bloch vectors, gate rotation arcs, decoherence spirals, eigenvalue annotations, matrix element grids, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Purity Spectrum: Pure State to Maximally Mixed

**Heuristic:** PQ — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a horizontal bar chart with a single horizontal axis running from 0 to 1, representing purity $\text{Tr}(\hat\rho^2)$. Place three horizontal bars stacked vertically. The top bar extends from 0 to 1.0, representing a pure state. The middle bar extends from 0 to 0.75, representing the lab-scenario mixed state from the chapter's opening example. The bottom bar extends from 0 to 0.5, representing the maximally mixed state. All bars have the same height. Mark vertical reference lines at $x = 0.5$ (minimum purity for a qubit) and $x = 1.0$ (pure state boundary). The y-axis tick positions are where category labels will be placed in post-production. No text in the image. White background, flat vector, no gradients.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Landscape orientation, horizontal bars.
- `[C — CONTENT]` Three bars: (1) $\text{Tr}(\hat\rho^2) = 1$ for a pure state; (2) $\text{Tr}(\hat\rho^2) = 11/16 \approx 0.688$ for the chapter's lab-scenario mixed state ($\frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|{+}\rangle\langle{+}|$); (3) $\text{Tr}(\hat\rho^2) = 0.5$ for $\tfrac{1}{2}\hat I$. Vertical reference lines at 0.5 and 1.0. Axis from 0 to 1. Y-axis zero-anchored from 0.
- `[O — ORGANIZATION]` Standard horizontal bar chart. Bars ordered top-to-bottom: pure → mixed lab scenario → maximally mixed. Shared x-axis at bottom, y-axis on left (no tick labels — post-production). Reference lines as thin dashed verticals at 0.5 and 1.0.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Pure state bar: Bluish Green `#009E73`. Lab-scenario mixed bar: Orange `#E69F00`. Maximally mixed bar: light gray. Reference line at 1.0: Bluish Green `#009E73` thin dashed. Reference line at 0.5: light gray thin dashed. Bar outlines: 1 pt dark gray stroke. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: error bars; Bloch ball geometry; von Neumann entropy; any second purity metric; qubit dimension label; $1/d$ formula annotation; off-diagonal matrix element display.

**BLOCK 3 — NEGATIVE PROMPT**

error bars, Bloch sphere, von Neumann entropy scale, second axes, color gradients in bars, 3D bar relief, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Partial Trace Mechanism: Joint Pure State → Mixed Subsystem

**Heuristic:** MC — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a three-panel horizontal process diagram. Panel 1 shows two overlapping or connected circles labeled A and B within a bounding rectangle, representing the joint pure state of a two-qubit system; indicate the joint state is pure with a surface-point marker (filled circle on a small Bloch sphere icon for the composite). Panel 2 shows a downward-pointing funnel or averaging symbol applied to the B circle only, with a faint cross or hash fill over the B region to indicate it is being summed over (traced out); an arrow labeled with the partial trace operation symbol points from Panel 1 to Panel 2. Panel 3 shows only the A circle remaining, now with an interior point (not on surface) on a small Bloch sphere icon, indicating the reduced state $\hat\rho_A$ is mixed. Connect the three panels with right-pointing arrows. No text in the image. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Three-panel horizontal layout with connecting arrows.
- `[C — CONTENT]` Step 1: joint two-qubit system $AB$ as pure state $|\Phi^+\rangle\langle\Phi^+|$ — represented as a bounding box containing two connected subsystem circles A and B, with a surface point on a miniature Bloch sphere indicating purity. Step 2: partial trace operation $\text{Tr}_B(\cdot)$ — shown as a summation-over-B motif (faint hash or sweep over B circle), with a process arrow. Step 3: reduced state $\hat\rho_A = \tfrac{1}{2}\hat I$ — only circle A remains, miniature Bloch sphere shows interior center point (maximally mixed). Transition arrows between steps labeled with operation symbol only (no text baked in — symbol placeholder acceptable as a geometric shape, e.g., summation arch).
- `[O — ORGANIZATION]` Left-to-right: [Joint AB box] → [Partial trace arrow + B erased] → [Reduced A box]. Three equal-width panels. Small Bloch sphere icon in corner of each state box. B-system erasure shown by fading or hash fill in middle panel.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Subsystem A circles: Sky Blue `#56B4E9`. Subsystem B circles: Orange `#E69F00`. B-erasure hashing: light gray. Pure-state surface points on mini Bloch spheres: Bluish Green `#009E73`. Mixed-state center point: Blue `#0072B2`. Process arrows: Blue `#0072B2` 1.5 pt. Bounding boxes: neutral gray 1 pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: matrix element entries; coefficient algebra; decoherence processes (separate concept); measurement collapse arrows; three or more subsystems; Schmidt decomposition notation; Wigner function.

**BLOCK 3 — NEGATIVE PROMPT**

matrix coefficient tables, decoherence trajectories, measurement collapse, Schmidt notation, three-body diagrams, Wigner function, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Decomposition Non-Uniqueness: Two Equal Density Matrices from Different Mixtures

**Heuristic:** VG — Rank: Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw two side-by-side Bloch ball cross-sections (equatorial x-z plane slices of the Bloch ball, shown as unit circles). In the left panel, mark two antipodal points on the z-axis: one at the north pole and one at the south pole, connected by a midpoint dashed line, with the midpoint at the origin highlighted. In the right panel, mark two antipodal points on the x-axis: one at positive x and one at negative x, connected by a midpoint dashed line, with the midpoint at the origin highlighted. The origin point in both panels is the same filled gray circle. Draw a double-headed equality sign or equivalence arrow between the two panels. Both panels share the same unit circle boundary. No text. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Two equal-width panels side by side with an equality/equivalence symbol between them.
- `[C — CONTENT]` Left panel: z-axis pure states $|0\rangle$ (north pole) and $|1\rangle$ (south pole), each as surface points, dashed midpoint line to origin representing the mixture $\tfrac{1}{2}|0\rangle\langle 0| + \tfrac{1}{2}|1\rangle\langle 1|$. Right panel: x-axis pure states $|{+}\rangle$ and $|{-}\rangle$ as surface points, dashed midpoint line to origin representing the mixture $\tfrac{1}{2}|{+}\rangle\langle{+}| + \tfrac{1}{2}|{-}\rangle\langle{-}|$. Origin in both panels: $\hat\rho = \tfrac{1}{2}\hat I$. Equivalence marker between panels (inferred relationship: the two mixtures produce the identical density matrix). Shared unit circle boundary in both panels.
- `[O — ORGANIZATION]` Left panel: vertical dashed midpoint segment, two surface markers on z-axis. Right panel: horizontal dashed midpoint segment, two surface markers on x-axis. Equality mark (≡ or ↔) between panels. Both panels same size with unit circle boundary drawn.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Surface pure-state points (left panel, z-axis): Sky Blue `#56B4E9`. Surface pure-state points (right panel, x-axis): Orange `#E69F00`. Origin/maximally mixed point: neutral gray, slightly larger filled circle. Dashed midpoint lines: light gray 1 pt dashed. Unit circle boundary: neutral gray 1 pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: y-axis or three-dimensional ball; other mixtures or decompositions beyond these two; purity calculation annotations; eigenvalue display; any third panel or additional comparison case.

**BLOCK 3 — NEGATIVE PROMPT**

three-dimensional sphere, y-axis, third decomposition panel, purity bars, eigenvalue annotations, additional mixture states, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Bloch Ball geometry:** STATIC SUFFICIENT. The geometry is three-dimensional but static — no process unfolds over time. The learning target is spatial reading of purity from Bloch vector length, which a well-drawn static figure conveys fully.

**Figure 2 — Purity Spectrum bar chart:** STATIC SUFFICIENT. Three fixed values on a single axis. No sequential mechanism; comparison-panel format is the natural choice and requires no animation.

**Figure 3 — Partial Trace Mechanism:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The partial trace operation — systematically summing over basis states of B to annihilate the B subsystem — is a multi-step mathematical process (write joint state → expand in B basis → sum B projections → collect A operators) whose causal logic is substantially clearer when the steps unfold in sequence than when collapsed into three static panels. The disappearance of the B subsystem and the emergence of mixed character in A is the chapter's central surprise, and sequential animation directly embodies that surprise.

**CHAPTER VIDEO RECOMMENDATION: Figure 3 — Partial Trace Mechanism.**

**Figure 4 — Decomposition Non-Uniqueness:** STATIC SUFFICIENT. The equivalence is a structural claim (two geometrically distinct paths reach the same point), well-served by side-by-side static panels sharing a common origin marker. No causal sequence is involved.
