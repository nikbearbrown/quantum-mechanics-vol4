# FACTCHECK — vox-chsh-arithmetic

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | CHSH parameter S = E(A1,B1) + E(A1,B2) + E(A2,B1) - E(A2,B2) | ✓ | ch03 §CHSH Inequality: "S = E(A₁,B₁) + E(A₁,B₂) + E(A₂,B₁) − E(A₂,B₂)" | None |
| B02 | If hidden instructions govern outcomes, S cannot exceed 2 | ✓ | ch03: "|S| ≤ 2" derived from local realism | None |
| B02 | Quantum mechanics predicts two root two, about 2.83 | ✓ | ch03: "S = 4/√2 = 2√2 ≈ 2.828" | None |
| B02 | Experiments confirm the quantum prediction | ✓ | ch03 §Experimental Program: Hensen et al. S=2.42, Giustina et al. 11.5σ violation, Shalm et al. p=5.9×10⁻⁹ | None |
| B04 | Under local realism each particle carries pre-assigned ±1 values for every setting | ✓ | ch03 §What Local Realism Claims: "Alice's outcome for setting Aᵢ is a deterministic function Aᵢ(λ) ∈ {+1,-1}" | None |
| B06 | S factored as A1(B1+B2) + A2(B1-B2) | ✓ | ch03: "S(λ) ≡ A₁(λ)[B₁(λ) + B₂(λ)] + A₂(λ)[B₁(λ) − B₂(λ)]" | None |
| B08 | Four rows of (B1,B2): (+1,+1)→sum+2,diff0; (+1,-1)→sum0,diff+2; (-1,+1)→sum0,diff-2; (-1,-1)→sum-2,diff0 | ✓ | ch03: exact table reproduced | None |
| B09 | In every row, one bracket is ±2 and the other is 0; \|S(λ)\|=2 exactly | ✓ | ch03: "In every row, one factor is ±2 and the other is 0. Therefore, for every λ: |S(λ)| = 1·2 + 1·0 = 2" | None |
| B11 | S bounded by 2 for every λ, not just on average; averaging preserves the bound | ✓ | ch03: "|S| = |∫S(λ)ρ(λ)dλ| ≤ ∫|S(λ)|ρ(λ)dλ = 2" | None |
| B11 | The bound is a theorem of arithmetic, not physics | ✓ | ch03: "The bound |S| ≤ 2 is a theorem of arithmetic applied to ±1 numbers" | None |
| B13 | Quantum predicts S up to 2√2 ≈ 2.83; that is 41% above classical bound | ✓ | ch03: "2√2 ≈ 2.828"; gap "41% of the classical bound" | None |
| B14 | Student example: A1=+1, A2=-1; all four B rows give |S|=2 | ✓ (ILLUSTRATIVE) | ch03 Exercise 1: "verify |S(λ)| = 2 in every case. Repeat with A₁ = +1, A₂ = −1" — the worked values are implied; illustrative student scenario | Student/scenario invented, ILLUSTRATIVE |

## Exclusions confirmed

- No quantum correlation formula derivation (E = cos(θa-θb) not mentioned): ✓
- No Tsirelson bound proof: ✓
- No experimental loopholes (detection/locality): ✓
- No CHSH history or attribution (Clauser, Horne, Shimony, Holt names not mentioned): ✓

## Terms table

| Term | Debut beat | Need established by |
|------|-----------|---------------------|
| CHSH parameter S | B01 (on screen immediately) | B01 (title card establishes definition) |
| local realism / hidden variable | B04 | B03 (question says "if hidden instructions govern") |
| lambda (instruction set) | B04 | B04 (introduced alongside local realism definition) |
| classical bound | B02 | B02 (introduced alongside quantum prediction) |

## Illustrative numbers / invented elements

- The student scenario in B14: illustrative worked example, ILLUSTRATIVE
- The specific assignment A1=+1, A2=-1: correct arithmetic per ch03 Exercise 1, ILLUSTRATIVE as a narrative device

All claims verified against `quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md`.
