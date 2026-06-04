# CAJAL Figure Report — Chapter 3 — Bell's Theorem and the CHSH Inequality

Recommended: 5 figures, Mixed density.

---

## Figure 1 — CHSH Algebraic Bound: The $B_1$/$B_2$ Switching Table

**Heuristic:** VG — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a 4-row by 4-column table where each cell contains either a filled square (magnitude 2, large) or an empty square (magnitude 0, small). The four rows correspond to the four possible assignments of $(B_1, B_2) \in \{(+1,+1), (+1,-1), (-1,+1), (-1,-1)\}$. The four columns represent $B_1$, $B_2$, $|B_1 + B_2|$, and $|B_1 - B_2|$. In column 3, a large filled square appears only in rows where $|B_1 + B_2| = 2$; in column 4, a large filled square appears only in rows where $|B_1 - B_2| = 2$. In every row, exactly one of columns 3 and 4 contains the large square and the other contains the empty (zero) square. A highlighted bar or bracket spans columns 3 and 4 for each row, visually linking the complementarity. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Grid table layout.
- `[C — CONTENT]` Four rows × four columns. Column 1: $B_1$ value indicated by filled ($+1$) or hollow ($-1$) circle. Column 2: $B_2$ value same encoding. Column 3: $|B_1 + B_2|$ — large filled square (value 2) or empty square (value 0). Column 4: $|B_1 - B_2|$ — complementary pattern to column 3. Row 1: $(+1,+1)$ → col3=2, col4=0. Row 2: $(+1,-1)$ → col3=0, col4=2. Row 3: $(-1,+1)$ → col3=0, col4=2. Row 4: $(-1,-1)$ → col3=2, col4=0. A row bracket spanning cols 3–4 with a "sum = 2" indicator (geometric: double-headed bracket with "2" placeholder). Critical inferred relationship: in every row, $|B_1+B_2| + |B_1-B_2| = 2$ exactly, producing $|S(\lambda)| = 2$.
- `[O — ORGANIZATION]` Standard grid. Column headers (post-production text zones): 4 placeholder zones. Row labels (post-production). 4-cell highlight brackets on right side of each row spanning cols 3–4. Alternating light gray row backgrounds for readability.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Large "2" cells (magnitude 2): filled squares, Sky Blue `#56B4E9`. Empty "0" cells: hollow squares, light gray outline. $B_1 = +1$ circles: Bluish Green `#009E73`. $B_1 = -1$ circles: Orange `#E69F00`. Same encoding for $B_2$. Row brackets: Blue `#0072B2` 1.5 pt. Alternating row backgrounds: very light gray / white. Grid lines: neutral gray 0.5 pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: the $A_i$ variables (the bound holds independently of $A$); probability distribution $\rho(\lambda)$; actual $S$ computation result; quantum correlation formula; angle geometry; Tsirelson bound.

**BLOCK 3 — NEGATIVE PROMPT**

A variables, probability distribution, quantum correlation formula, measurement angles, Tsirelson line, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — CHSH Parameter Bounds: Classical, Quantum, and No-Signaling

**Heuristic:** PQ — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a single horizontal number line from 0 to 4 representing the possible values of $|S|$. Mark four reference points with distinct vertical tick marks of different heights: at $|S| = 0$, at $|S| = 2$ (classical/local-realism bound), at $|S| = 2\sqrt{2} \approx 2.828$ (Tsirelson / quantum bound), and at $|S| = 4$ (algebraic maximum / PR-box). Between 0 and 2, fill the interval with a solid horizontal bar (local-realistic models). Between 2 and $2\sqrt{2}$, fill with a different-color bar (quantum violation region). Between $2\sqrt{2}$ and 4, fill with a third-color bar (hypothetical super-quantum, PR-box region). Mark the point $|S| = 2.42$ with a small triangle or diamond above the axis (representing the Hensen et al. 2015 experimental result). Y-axis starts at zero. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Horizontal range chart with three color-coded zones on a single axis.
- `[C — CONTENT]` Horizontal axis: $|S|$ from 0 to 4. Three filled zones: (1) $[0, 2]$ — local-realistic region; (2) $(2, 2\sqrt{2}]$ — quantum mechanical violation range; (3) $(2\sqrt{2}, 4]$ — hypothetical no-signaling / PR-box region. Four boundary tick marks at 0, 2, $2\sqrt{2}$, 4. Experimental marker at $|S| = 2.42$ (Hensen et al. 2015, labeled in post-production). Axis label zones (post-production text) at each boundary.
- `[O — ORGANIZATION]` Single horizontal axis with three contiguous colored bars from 0 to 4. The three segments share the same y-height (equal bar height). Boundary lines as thin vertical ticks. Experimental point marker as a diamond or triangle above the bar at 2.42. Axis ticks at 0, 1, 2, $2\sqrt{2}$ (marked as a tick position), 3, 4.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Zone 1 (local-realistic, $[0,2]$): Bluish Green `#009E73` filled bar. Zone 2 (quantum, $(2, 2\sqrt{2}]$): Sky Blue `#56B4E9` filled bar. Zone 3 (super-quantum PR-box, $(2\sqrt{2}, 4]$): light gray filled bar. Experimental point (2.42): Orange `#E69F00` filled diamond. Boundary tick marks: neutral gray 1.5 pt. Axis line: neutral gray 1 pt. White background. Y-axis at zero. No baked text.
- `[E — EXCLUSIONS]` Omit: negative $S$ values; signed $S$ (show $|S|$ only); multiple experimental points; error bars; probability distributions over outcomes; any derivation algebra.

**BLOCK 3 — NEGATIVE PROMPT**

signed S values, multiple experiment markers, error bars, probability distribution curves, derivation algebra, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Optimal CHSH Angles for $|\Phi^+\rangle$: Correlation Compass

**Heuristic:** VG — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a single circle (a polar compass diagram) with a vertical z-axis and horizontal x-axis indicated. Mark four measurement directions as radial arrows from the center: Alice's $A_1$ direction at 0° (along +z), Alice's $A_2$ direction at 90° (along +x), Bob's $B_1$ direction at 45°, and Bob's $B_2$ direction at −45° (or 315°). Use two distinct visual styles for Alice's arrows versus Bob's arrows (e.g., solid vs. dashed, or two colors). On each pair of directions that corresponds to one of the four CHSH correlations, draw an arc between the two arrows, labeled with a placeholder for the correlation value. Keep the diagram to eight components or fewer: four arrows, two axis lines, and two style indicators. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Polar compass diagram, single panel.
- `[C — CONTENT]` Unit circle with two crosshair axes. Four radial measurement direction arrows: $A_1$ at 0° (solid Sky Blue), $A_2$ at 90° (solid Sky Blue), $B_1$ at 45° (dashed Blue), $B_2$ at −45° (dashed Blue). Arc indicators between paired directions: $E(A_1,B_1)$ arc (0° to 45°, 45° span → $+1/\sqrt{2}$), $E(A_1,B_2)$ arc (0° to −45°, 45° span → $+1/\sqrt{2}$), $E(A_2,B_1)$ arc (90° to 45°, 45° span → $+1/\sqrt{2}$), $E(A_2,B_2)$ arc (90° to −45°, 135° span → $-1/\sqrt{2}$); the 135° arc is visually distinct (wider arc, different treatment). Correlation values as post-production text labels. Alice/Bob encoding by solid vs. dashed arrow style.
- `[O — ORGANIZATION]` Single circular compass. Arrows from center, equal length. Arcs drawn between each Alice-Bob pair at the perimeter. 135° arc (the one with negative correlation) drawn at outer radius or with a distinctive arc curvature to distinguish from the three 45° arcs. Axis crosshairs as thin gray lines extending through the circle.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Alice arrows ($A_1$, $A_2$): Sky Blue `#56B4E9` solid 2 pt. Bob arrows ($B_1$, $B_2$): Blue `#0072B2` dashed 2 pt. Positive-correlation arcs (three, 45° span): Bluish Green `#009E73` thin arc. Negative-correlation arc (one, 135° span): Orange `#E69F00` thicker arc. Compass circle outline: light gray 1 pt. Axis lines: neutral gray 0.5 pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: singlet state angles (separate computation in the worked example); Bloch sphere geometry; three-dimensional rotation; more than four measurement directions; CNOT circuit; actual $S$ sum diagram; correlation heat map.

**BLOCK 3 — NEGATIVE PROMPT**

singlet angle set, Bloch sphere, three-dimensional perspective, more than four directions, correlation heat map, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Bell Experiment Timeline: 1972–2022

**Heuristic:** MC — Rank: Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a horizontal timeline from 1964 to 2025. Mark eight labeled events as vertical tick marks at the appropriate positions: Bell's theorem (1964), Freedman & Clauser (1972), Aspect locality test (1982), Hensen et al. Delft (2015), Giustina et al. Vienna (2015), Shalm et al. NIST (2015), Nobel Prize (2022). Place the three 2015 events as three closely spaced but distinguishable tick marks. Use two horizontal bands above the timeline axis to indicate which loopholes were open or closed: one band for "detection loophole" and one for "locality loophole." From 1964 to 1982, both bands are shown in a blocked/open style; from 1982 onward the locality-loophole band changes to a closed style; from 2015 onward both bands show a closed style. The Nobel Prize marker at 2022 uses a distinctive star or diamond shape. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Horizontal timeline with two loophole-status bands above the axis. Landscape orientation.
- `[C — CONTENT]` Horizontal axis: 1964 to 2025. Eight event tick marks with post-production label zones. Two color-coded loophole status bands running horizontally above the axis: Band 1 = detection loophole status, Band 2 = locality loophole status. Status encoding: open loophole = light gray hatched fill; closed loophole = Bluish Green `#009E73` solid fill. Locality loophole closes at 1982 (Aspect). Both close at 2015 (three simultaneous experiments). Nobel Prize tick at 2022 as gold star icon. Three 2015 tick marks spaced 2–3 px apart with distinct shapes (circle, square, triangle) to represent Hensen, Giustina, Shalm. Bell's theorem (1964) as a filled circle on the axis (starting anchor, not a loophole-closure event).
- `[O — ORGANIZATION]` Single horizontal axis at bottom. Two loophole bands stacked above the axis, each as a narrow horizontal rectangle whose fill changes at event boundaries. Event tick marks extend downward from the axis with shape variation for the three 2015 events. Nobel star above axis at 2022. Year scale marks at 1964, 1972, 1982, 2000, 2015, 2022.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Timeline axis: neutral gray 1.5 pt. Open loophole bands: light gray hatched. Closed detection loophole band: Sky Blue `#56B4E9` solid. Closed locality loophole band: Bluish Green `#009E73` solid. Three 2015 event markers: Blue `#0072B2` (Hensen circle), Orange `#E69F00` (Giustina square), Reddish Purple `#CC79A7` (Shalm triangle). Nobel marker: Orange `#E69F00` star (distinct from bar fills). 1964 Bell marker: neutral gray circle. 1972 Freedman marker: neutral gray circle. 1982 Aspect marker: Bluish Green `#009E73` circle. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: the EPR 1935 paper (pre-dates testable Bell inequality); specific $S$ values at each experiment; detector efficiency numbers; satellite experiments post-2015 (Yin 2017); interpretational implications timeline.

**BLOCK 3 — NEGATIVE PROMPT**

EPR 1935, S value annotations, detector efficiency numbers, satellite experiment markers, interpretational annotations, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 5 — Three Interpretational Exits from Bell's Theorem

**Heuristic:** VG — Rank: Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a branching tree diagram. At the root, place a single node representing the experimental result (Bell inequality violated). From this root, three branches diverge, each leading to a distinct leaf node. Branch 1 leads to a leaf representing "realism abandoned" — illustrated by a question mark inside a dashed box (indicating that outcomes lack pre-existing values). Branch 2 leads to a leaf representing "locality abandoned" — illustrated by two connected nodes with a non-local link (a thick connecting arc between two spatially separated boxes). Branch 3 leads to a leaf representing "outcome uniqueness abandoned" — illustrated by a branching fork showing multiple outcome branches (a simple Y-fork from one box). Each branch is a single arrow from the root. The root node is distinct from the three leaves. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Top-down branching tree with one root and three leaves.
- `[C — CONTENT]` Root node: single circle representing "Bell inequality violation (experimental fact)." Three branches, each a directed arrow: Branch 1 → leaf "Give up realism" (dashed question-mark box, representing Copenhagen/standard QM: outcomes not pre-defined); Branch 2 → leaf "Give up locality" (two boxes connected by a thick non-local arc, representing Bohmian pilot-wave mechanics); Branch 3 → leaf "Give up unique outcomes" (Y-fork branching diagram, representing many-worlds). All three leaves are equivalent exits — no hierarchy among them (branches equal length). The three positions are the only coherent choices under Bell's theorem (inferred constraint, labeled in post-production).
- `[O — ORGANIZATION]` Root centered at top; three branches diverging downward at equal angular spacing. Three leaf nodes at equal vertical depth. Arrows from root to leaves (directed, no return arrows). Each leaf contains a small geometric icon indicating the interpretational type.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Root node: Sky Blue `#56B4E9` filled circle. Branch arrows: neutral gray 1.5 pt. Leaf 1 (realism abandoned, dashed box): Orange `#E69F00` dashed rectangle. Leaf 2 (locality abandoned, non-local arc): Reddish Purple `#CC79A7` thick arc connecting two boxes. Leaf 3 (uniqueness abandoned, Y-fork): Blue `#0072B2` Y-fork branching motif. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: superdeterminism (mentioned in some treatments but not in this chapter); any endorsement hierarchy or preferred interpretation; measurement-problem discussion; quantum field theory; device-independent cryptography applications.

**BLOCK 3 — NEGATIVE PROMPT**

superdeterminism branch, preferred interpretation ranking, measurement problem diagram, quantum field theory, cryptography icons, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — CHSH Algebraic Switching Table:** STATIC SUFFICIENT. A lookup table demonstrating a purely algebraic fact (that in each row, $|B_1+B_2| + |B_1-B_2| = 2$). The structure is fully visible in a static grid; no sequential mechanism is the learning target.

**Figure 2 — CHSH Bounds Number Line:** STATIC SUFFICIENT. A quantitative range diagram with three fixed zones. No process; comparison is the purpose, well-served statically.

**Figure 3 — Optimal CHSH Angles Compass:** STATIC SUFFICIENT. Four fixed directions on a compass. The angular relationships are spatial, not temporal. A static polar diagram conveys all relationships.

**Figure 4 — Bell Experiment Timeline:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages where each stage advances a chain of evidence. The timeline has a causal-epistemic progression: each experiment closes a previously open loophole, building toward the 2015 loophole-free confirmation. Animating the timeline with each experiment's closure advancing the loophole-status bands — open hatching transitioning to solid color as each loophole closes — makes the cumulative logical structure (and why the 2015 "big three" mattered together) directly legible. The transition mechanism (successive loophole closure leading to Nobel recognition) is itself the learning target.

**CHAPTER VIDEO RECOMMENDATION: Figure 4 — Bell Experiment Timeline.**

**Figure 5 — Interpretational Exits:** STATIC SUFFICIENT. A structural taxonomy of three equally valid logical choices. No temporal sequence; the branching tree captures the choice structure in a single static image.
