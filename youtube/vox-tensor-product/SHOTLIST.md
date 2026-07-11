# SHOTLIST — vox-tensor-product

| Beat | Type | Duration | Visual description |
|------|------|----------|--------------------|
| B01 | CARD/title | 10s | "Two qubits. Four dimensions. Which four?" sub: COMPOSITE SYSTEMS |
| B02 | GRAPHIC | 13s | Direct sum: two separate 2D planes (labeled ℂ² and ℂ²) side by side, NO connection between them; label "A" on left plane, "B" on right; arrow labels showing "2+2=4" |
| B03 | GRAPHIC | 13s | Tensor product: 2×2 grid of basis states |00⟩, |01⟩, |10⟩, |11⟩; TEAL highlight on grid; "2×2=4" label |
| B04 | CARD/dek | 9s | "Same dimension. Why the tensor product and not the direct sum?" sub: THE QUESTION |
| B05 | CARD/section | 4s | "THE MECHANISM" |
| B06 | GRAPHIC | 13s | Rank-1 coefficient matrix: 2×2 matrix with c₀₀=α, c₀₁=β, c₁₀=γ, c₁₁=δ filled in as outer product; TEAL highlight; "rank 1" label; det=0 annotation |
| B07 | GRAPHIC | 13s | Rank-2 Bell state matrix: C = (1/√2)(1 0 / 0 1); CRIMSON highlight; "rank 2" label; det=½ annotation; "entangled" label |
| B08 | CARD/section | 4s | "THE IMPLICATION" |
| B09 | GRAPHIC | 14s | Two-column: left = "DIRECT SUM" (only rank-1 matrices, TEAL); right = "TENSOR PRODUCT" (rank-1 AND rank-2, CRIMSON for rank-2 row); "Bell state: no analog here" in CRIMSON on left side |
| B10 | CARD/section | 4s | "THE EXAMPLE" |
| B11 | GRAPHIC | 14s | Number comparison: "2³ = 8" vs "2+2+2 = 6"; CRIMSON highlight on "8"; label "extra 2 = entangled encoding states"; small |000⟩+|111⟩ encoding state in CRIMSON |
| B12 | CARD/endcard | 10s | "Tensor product: cross-terms allowed. Direct sum: no cross-terms. Rank 1 = product. Rank 2 = entangled." topic: QUANTUM MECHANICS |

## Scenes needed (GRAPHIC beats)
- B02_DirectSum — two independent planes
- B03_TensorBasis — 2×2 basis state grid
- B06_Rank1Matrix — rank-1 product state coefficient matrix
- B07_Rank2Bell — rank-2 Bell state coefficient matrix
- B09_StructureCompare — side-by-side direct sum vs tensor product
- B11_DimensionCount — 2^3=8 vs 2+2+2=6

## Rhythm check
CARD · GRAPHIC · GRAPHIC · CARD · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · CARD
Max consecutive GRAPHIC: 2 ✓
Max consecutive CARD: 2 (B04–B05) ✓
