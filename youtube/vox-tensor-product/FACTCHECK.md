# FACTCHECK — vox-tensor-product

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | Two qubits each have dimension 2; joint space has dimension 4 | ✓ | ch02 §The Tensor Product: "The dimension is 2×2=4"; "ℋ_A⊗ℋ_B = span{|00⟩,|01⟩,|10⟩,|11⟩}" | None |
| B02 | Direct sum places two systems side by side with no cross-terms; state = state of A + state of B | ✓ | ch02 §The Tensor Product: "A direct sum would give two independent quantum systems that cannot correlate at all" | None |
| B03 | Tensor product builds all combinations; four basis vectors 00, 01, 10, 11; 2×2=4 | ✓ | ch02 §The Tensor Product: basis, dimension 2×2=4, general state with four coefficients | None |
| B06 | Product state coefficients form rank-1 matrix; determinant zero; two subsystems independent | ✓ | ch02 §Product States and the Rank-1 Test: "C_sep is a rank-1 matrix"; "det(C_sep)=0"; proof given | None |
| B07 | Bell state (|00⟩+|11⟩)/√2 gives rank-2 matrix, det=1/2, nonzero → entangled | ✓ | ch02 §Product States and the Rank-1 Test: "C = (1/√2)(1 0 / 0 1), det(C)=1/2 ≠ 0 — entangled" | None |
| B09 | Direct sum has no rank-2 states; no Bell state analog; tensor product adds exactly the entangled states | ✓ | ch02 §The Tensor Product: "The tensor product gives them the ability to correlate — and, in particular, to be entangled" | None |
| B11 | 3-qubit code joint space: 2^3=8, not 2+2+2=6; extra dimensions are the entangled encoding states | ✓ (ILLUSTRATIVE) | ch02 §The Tensor Product: "For a qubit and a qutrit, the joint space is 2×3=6-dimensional, not 5" (product rule confirmed); encoding states use cross-qubit superpositions consistent with ch09 3-qubit code. 2^3=8 vs 6 illustration ILLUSTRATIVE | Numbers ILLUSTRATIVE |

## Exclusions confirmed

- No Schmidt decomposition derivation: ✓
- No SVD algebra: ✓
- No entanglement entropy: ✓
- No LOCC framework: ✓

## Terms table

| Term | Debut beat | Need established by |
|------|-----------|---------------------|
| tensor product | B01 | B01 (set up the question) |
| direct sum | B02 | B01 (contrast hinted) |
| coefficient matrix | B06 | B03 (four coefficients introduced) |
| rank-1 / rank-2 | B06 | B06 (introduced together with determinant test) |
| Bell state | B07 | B06 (product state defined first) |

## Illustrative numbers / invented elements

- B11: "2^3=8 vs 2+2+2=6" framing — ILLUSTRATIVE (product rule confirmed by source; the specific contrast to QEC is illustrative)

All claims verified against `quantum-mechanics-vol4/chapters/02-composite-systems-and-entanglement.md`.
