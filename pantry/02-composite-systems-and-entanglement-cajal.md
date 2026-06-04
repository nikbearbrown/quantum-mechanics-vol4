# CAJAL Figure Report — Chapter 2 — Composite Systems and Entanglement

Recommended: 4 figures, Mixed density.

---

## Figure 1 — Tensor Product Dimension: Product vs. Sum

**Heuristic:** VG — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a two-panel comparison diagram. Left panel shows a direct sum interpretation — two separate small squares (each 2-dimensional, representing individual qubit Hilbert spaces) placed side by side inside a larger bounding rectangle labeled "4 dimensions (wrong)." Right panel shows the tensor product — a single 4-by-4 grid of cells (representing the 4-dimensional joint Hilbert space), with each of the four basis states $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$ occupying one grid cell, indicated by a filled circle in that cell. A large "×" symbol between a 2-cell column and a 2-cell row indicates the product rule. No text baked in. White background, flat vector. The two panels are connected by a visual separator or a versus symbol as a geometric shape.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Two-panel side-by-side comparison layout with a divider.
- `[C — CONTENT]` Left panel: two separate 2-cell bars (representing $\mathcal{H}_A$ and $\mathcal{H}_B$ each with 2 basis states) arranged side-by-side inside a 4-cell total bounding box, illustrating the incorrect direct-sum intuition. Right panel: 2×2 grid of four cells, each occupied by a filled circle, representing the four basis states $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$ of $\mathcal{H}_A \otimes \mathcal{H}_B$; a "×" multiplication icon between an A-row indicator and a B-column indicator (inferred product rule relationship, labeled).
- `[O — ORGANIZATION]` Left-to-right: [direct sum panel] | [versus divider] | [tensor product panel]. Left panel: two adjacent 2-cell bars. Right panel: 2×2 grid. Equal-width panels. Minimalist geometric.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Left panel (incorrect direct sum): bars in light gray, bounding box in Vermillion `#D55E00` thin stroke to indicate the "wrong" interpretation (blocking/negative). Right panel (tensor product grid): cells outlined in Sky Blue `#56B4E9`, filled circles in Bluish Green `#009E73`. Multiplication icon in Blue `#0072B2`. Versus divider: neutral gray. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: qudit generalizations beyond two qubits; Hilbert space formalism symbols; inner product notation; density matrix; partial trace; any three-qubit or higher systems.

**BLOCK 3 — NEGATIVE PROMPT**

qudit grids, inner product bracket notation, three-qubit tensors, density matrix display, partial trace arrows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Separable vs. Entangled: Coefficient Matrix Rank

**Heuristic:** VG — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a two-panel comparison diagram. Each panel contains a 2×2 grid representing the coefficient matrix $C$. In the left panel (separable state), two cells in the left column are filled with solid squares of equal size and the right column is empty (zero entries), illustrating a rank-1 matrix; a factorization arrow beneath shows one column vector times one row vector. In the right panel (entangled state), all four cells of the 2×2 grid contain filled squares of varying size proportional to the magnitude of each entry, illustrating rank 2; a crossed-out factorization symbol beneath indicates the matrix does not factor. A visual separator divides the two panels. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Two-panel side-by-side layout.
- `[C — CONTENT]` Left panel: rank-1 coefficient matrix for $|{+}\rangle_A \otimes |0\rangle_B = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 1 & 0\end{pmatrix}$ — two filled cells in column 1, two empty cells in column 2; outer product factorization arrow beneath (column vector ⊗ row vector motif). Right panel: rank-2 coefficient matrix for $|\Phi^+\rangle = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ — filled cells on diagonal, empty off-diagonal, det ≠ 0; blocked factorization motif (crossed-out outer product) beneath. Separator between panels.
- `[O — ORGANIZATION]` Two equal-width panels side by side. Left: rank-1 grid + factorization motif below. Right: rank-2 grid + blocked factorization motif below. Blocked motif uses a geometric "no" symbol (circle with diagonal bar, not colored red-green). Equal-sized grid cells in both panels.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Left panel (separable) grid outline: Bluish Green `#009E73`. Left panel filled cells: Sky Blue `#56B4E9`. Factorization arrow: Bluish Green `#009E73`. Right panel (entangled) grid outline: Blue `#0072B2`. Right panel filled cells: Blue `#0072B2`. Blocked factorization "no" symbol: Vermillion `#D55E00`. Separator: light gray. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Schmidt decomposition (separate figure); entanglement entropy values; Bloch sphere geometry; partial trace; mixed states; three or more qubits; PPT criterion.

**BLOCK 3 — NEGATIVE PROMPT**

Schmidt decomposition, entropy values, Bloch sphere, partial trace arrows, mixed state markers, three-qubit grids, PPT criterion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Bell State Preparation Circuit: $|00\rangle \to |\Phi^+\rangle$

**Heuristic:** MC — Rank: Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a three-stage horizontal process diagram representing the quantum circuit that produces $|\Phi^+\rangle$ from $|00\rangle$. Stage 1 shows two horizontal wire lines representing qubits A and B in state $|00\rangle$; place a small filled circle at the start of each wire indicating the initial pure state $|0\rangle$ on the Bloch sphere (north pole). Stage 2 shows a Hadamard gate box on wire A only; after the gate, the Bloch sphere icon for A shows a surface point on the equator (+x direction), while qubit B remains unchanged. Stage 3 shows a CNOT gate connecting wire A (control, filled circle) to wire B (target, ⊕ symbol); after this gate, both Bloch sphere icons show center points (maximally mixed subsystems). Place right-pointing arrows between stages. The stage-to-stage state transitions are represented by small Bloch sphere icons attached to each wire after each gate. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Horizontal circuit diagram with three stages; two qubit wires.
- `[C — CONTENT]` Stage 1: qubits A and B as $|0\rangle$; Bloch icon: north pole surface point. Stage 2: Hadamard box on wire A; post-H state of A is $|{+}\rangle$ (equatorial Bloch point, +x); B unchanged ($|0\rangle$, north pole); joint state is separable at this stage (inferred, to be labeled). Stage 3: CNOT gate (control on A, target ⊕ on B); post-CNOT both Bloch sphere icons show center (origin) point indicating maximally mixed subsystems; joint state is $|\Phi^+\rangle$ (entangled, inferred label position). Gate symbols: H-box on A wire, filled-circle control on A, ⊕ target on B, vertical connecting line between control and target.
- `[O — ORGANIZATION]` Left-to-right: [Initial state] → [After H] → [After CNOT]. Two horizontal wire lines through all stages; gate symbols on wires at stages 2 and 3. Small Bloch sphere icons attached above/below each wire segment, showing state evolution. Stage labels (placeholders for text in post-production) indicated by empty label zones.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Qubit wires: neutral gray 1.5 pt. H-gate box: Sky Blue `#56B4E9` outline, white fill. CNOT control dot: Blue `#0072B2`. CNOT ⊕ target: Blue `#0072B2` outline. Connecting vertical line between control/target: Blue `#0072B2` 1 pt. Bloch sphere icons: pure-state surface points in Bluish Green `#009E73`; mixed-state center point in Orange `#E69F00`. Stage-separation arrows: neutral gray. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: other Bell states ($|\Phi^-\rangle$, $|\Psi^\pm\rangle$) in same diagram; multi-qubit gates beyond H and CNOT; decoherence; quantum teleportation; measurement gates; three or more qubits.

**BLOCK 3 — NEGATIVE PROMPT**

other Bell states in same diagram, decoherence channels, teleportation circuits, measurement symbols, three-qubit wires, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Entanglement Entropy vs. Schmidt Coefficient Asymmetry

**Heuristic:** PQ — Rank: Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a line chart with the horizontal axis representing the Schmidt angle parameter $\theta$ from 0 to $\pi/4$ radians, and the vertical axis representing entanglement entropy $S_E$ from 0 to 1 ebit. The y-axis must start at zero. Plot a single smooth curve showing $S_E(\theta) = -\cos^2\theta\,\log_2\cos^2\theta - \sin^2\theta\,\log_2\sin^2\theta$, which rises from 0 at $\theta = 0$ to a maximum of 1 at $\theta = \pi/4$. Mark three points on the curve: $(\theta=0, S_E=0)$ indicating the product state; $(\theta \approx 0.615, S_E \approx 0.811)$ indicating the partially entangled state from the worked example ($\lambda_1 = 3/4$, $\lambda_2 = 1/4$); and $(\theta = \pi/4, S_E = 1)$ indicating the maximally entangled (Bell state) point. Mark these three points with distinct filled circles. Reference horizontal dashed line at $S_E = 1$. No text baked in. White background, flat vector.

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Standard line chart, landscape orientation.
- `[C — CONTENT]` Horizontal axis: $\theta \in [0, \pi/4]$ (Schmidt angle parameterizing $\lambda_1 = \cos^2\theta$, $\lambda_2 = \sin^2\theta$). Vertical axis: $S_E \in [0, 1]$ ebits, starting at zero. Smooth entropy curve rising from (0, 0) to $(\pi/4, 1)$. Three marked points: product state at origin; chapter worked-example partial state at $(\theta \approx 0.615, 0.811)$ derived from $\lambda_1 = 3/4$; Bell state at $(\pi/4, 1)$. Horizontal reference line at $S_E = 1$ (Tsirelson / maximum entanglement for two qubits). No extrapolation beyond $[0, \pi/4]$.
- `[O — ORGANIZATION]` Standard x–y line chart. Y-axis from 0. Three annotated point markers as filled circles on the curve. Reference dashed line at $y = 1$. Minimal tick marks on both axes (3–4 each). Curve as a single continuous smooth line.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito. Entropy curve: Blue `#0072B2` 2 pt. Product state point: Bluish Green `#009E73` filled circle. Partial entanglement point: Orange `#E69F00` filled circle. Bell state point: Reddish Purple `#CC79A7` filled circle. Reference dashed line: light gray 1 pt dashed. Axes: neutral gray 1 pt. White background. No baked text. Y-axis starts at zero.
- `[E — EXCLUSIONS]` Omit: logarithmic entropy axis; multiple curves for different system dimensions; concavity annotations; von Neumann entropy for mixed states; LOCC bounds; entanglement of formation curve; any second entropy measure.

**BLOCK 3 — NEGATIVE PROMPT**

log-scale entropy axis, multi-qudit curves, concavity annotation, entanglement of formation, distillable entanglement, LOCC bound lines, mixed-state entropy, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Tensor Product Dimension:** STATIC SUFFICIENT. A structural comparison claim between two counting rules. No sequential mechanism; side-by-side static panels are exactly the right format.

**Figure 2 — Separable vs. Entangled Coefficient Matrix Rank:** STATIC SUFFICIENT. A structural / spatial claim (rank of a 2×2 matrix determines separability). Two comparison panels, static.

**Figure 3 — Bell State Preparation Circuit:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages where each stage changes the physical state in a way that is the learning target. The circuit has three causally ordered steps ($|00\rangle$ → post-H → post-CNOT), and the critical lesson — that the Hadamard alone leaves the state separable while the CNOT creates entanglement — is most legible when Bloch sphere icons animate their state changes sequentially. Students need to see that entanglement appears at a specific gate, not globally at the end of the circuit.

**CHAPTER VIDEO RECOMMENDATION: Figure 3 — Bell State Preparation Circuit.**

**Figure 4 — Entanglement Entropy Curve:** STATIC SUFFICIENT. A quantitative curve on a fixed axis. The three marked points are sufficient for reading off the key values; no temporal sequence is involved.
