# PEDAGOGY — vox-tensor-product

## Concept to teach
The tensor product (2×2=4) and the direct sum (2+2=4) give the same dimension for two qubits, but only the tensor product allows entanglement. The difference is structural: in the tensor product, the coefficient matrix can have rank 2 (entangled states); in the direct sum, every coefficient matrix has rank 1 (product states only). The rank of the coefficient matrix is the exact test for entanglement.

## Target audience
Anyone who knows that two qubits together have four dimensions but wonders why the structure matters, not just the count.

## Prior knowledge assumed
- A qubit is a 2D vector space
- States can be superpositions
- Some notion that combining systems makes a bigger space

## Prior knowledge NOT assumed
- Schmidt decomposition
- SVD algebra
- Entanglement entropy formulas
- LOCC framework

## Learning arc

### Step 1 — Anchor (B01–B03)
Start with the dimension agreement: 2+2=4 and 2×2=4 are both four. Show the two structures visually — direct sum as independent planes, tensor product as the full 2×2 coefficient matrix space.

### Step 2 — Tension (B04)
Ask THE QUESTION: why does quantum mechanics pick tensor product over direct sum when the dimension is the same?

### Step 3 — Mechanism (B05–B07)
Introduce the coefficient matrix and rank test. Show: product state → rank-1 matrix, determinant=0. Bell state → rank-2 matrix, determinant≠0. The rank difference is the structural difference between the two spaces.

### Step 4 — Implication (B08–B09)
Show what the direct sum is missing: rank-2 matrices, cross-terms, Bell states. The tensor product adds exactly the entangled states. Remove the tensor product structure and every state is a product state.

### Step 5 — Example (B10–B11)
Concrete case: a 3-qubit error code needs dimension 8 (=2^3) not 6 (=2+2+2). The two extra dimensions are the entangled encoding states. Without the tensor product structure, the code cannot exist.

### Step 6 — Synthesis (B12)
Endcard: tensor product = cross-terms allowed; direct sum = no cross-terms. Rank 1 = product state; rank 2 = entangled.

## Common misconceptions addressed
1. "The four dimensions are the same" — The dimensions match but the structure differs. Direct sum has no rank-2 matrices; tensor product does.
2. "Entanglement is some special extra ingredient" — It's just the rank-2 part of the tensor product space. Product states are rank-1; most states are rank-2 (entangled).
3. "You need advanced math to spot entanglement" — The determinant test is a 2×2 calculation: det(C) = c₀₀c₁₁ − c₀₁c₁₀. Nonzero ↔ entangled.

## Pacing check
- B01–B03: anchor the structures (36s)
- B04: ask the question (9s)
- B05–B07: rank mechanism (30s)
- B08–B09: implication (18s)
- B10–B11: example (18s)
- B12: recap (10s)
Total ~121s. Clean 2-minute reel.

## Color semantics check
- TEAL: product state, rank-1 matrix, separable, direct sum structure
- CRIMSON: entangled state, rank-2 matrix, Bell state, cross-terms, nonzero determinant
These map cleanly: TEAL for the separated/independent structure, CRIMSON for the entangled states that exist only in the tensor product.

## Rhythm check
CARD · GRAPHIC · GRAPHIC · CARD · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · CARD
Max consecutive GRAPHIC: 2 (B02–B03, B06–B07) ✓
Max consecutive CARD: 2 (B04–B05, B08... B08 is solo, B10 is solo) ✓

VERDICT: PASS
