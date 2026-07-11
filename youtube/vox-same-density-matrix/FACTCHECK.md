# FACTCHECK — vox-same-density-matrix

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | Lab A prepares \|0⟩ or \|1⟩ at random; Lab B prepares \|+⟩ or \|−⟩ at random | ✓ | ch01 intro: "Method 1 prepares |0⟩, Method 2 prepares |+⟩" — extended to symmetric pair for each lab | None |
| B02 | Measuring in every direction gives 50/50 from both labs | ✓ | ch01 §Bloch Ball: maximally mixed state ρ = I/2 gives r=(0,0,0); every Pauli expectation = 0, so every basis gives 50/50 | None |
| B04 | Lab A: half \|0⟩, half \|1⟩; density matrix = I/2 | ✓ | ch01: (1/2)|0⟩⟨0| + (1/2)|1⟩⟨1| = diag(1/2, 1/2) = I/2 exactly | None |
| B05 | Lab B: half \|+⟩, half \|−⟩; density matrix = I/2 | ✓ | ch01: (1/2)|+⟩⟨+| + (1/2)|−⟩⟨−| = (1/2)·(1/2)(1,1;1,1) + (1/2)·(1/2)(1,-1;-1,1) = diag(1/2,1/2) = I/2 | None |
| B07 | Pure states on surface, mixed in interior, maximally mixed at center with Bloch vector 0 | ✓ | ch01 §Bloch Ball: "Pure states sit on the surface... maximally mixed state ρ = I/2 gives r=(0,0,0) — the center" | None |
| B08 | Lab A averages north and south pole → midpoint is center; Lab B averages east and west pole → midpoint is also center | ✓ | ch01 §Bloch Ball: \|0⟩ is north pole (0,0,1), \|1⟩ is south pole (0,0,-1); \|+⟩ is (1,0,0), \|−⟩ is (-1,0,0); both pairs average to (0,0,0) | None |
| B10 | Any pair of antipodal surface points averages to the center; infinitely many preparations map to the same density matrix | ✓ | ch01 §Interpretation: "the decomposition ρ = Σ p_i\|ψ_i⟩⟨ψ_i\| is non-unique for any mixed state — infinitely many ensembles map to the same ρ"; Figure 1.3 caption confirms | None |
| B12 | Density matrix is a prediction machine for measurements, not a record of preparation history | ✓ | ch01 §Interpretation: "The density matrix represents what an observer can predict about measurements — not the preparation history" | None |
| B12 | Two sources with identical measurement statistics for every observable are by definition the same quantum state | ✓ | ch01 §Interpretation: "Two ensembles with identical measurement statistics for every observable are, by definition, the same quantum state" | None |
| B13 | QKD network security analysis treats two identical-ρ sources identically; same ρ = same channel behavior | ✓ (ILLUSTRATIVE) | ch01 card example seed: "A quantum key distribution network receives qubits… Security analysis treats them identically — because if two sources produce the same ρ, no eavesdropper and no honest user can distinguish them." Numbers and station names are invented but mechanism is accurate. | Station names "Station Z" and "Station X" are ILLUSTRATIVE |
| B14 | Two labs, two procedures, one density matrix | ✓ | Core result confirmed above | None |

## Exclusions confirmed

- No partial-trace matrix computation: not mentioned anywhere ✓
- No purity/Tr(ρ²) formula: not mentioned ✓
- No Schmidt decomposition: not mentioned ✓
- No entanglement connection: not mentioned ✓

## Terms table

| Term | Debut beat | Need established by |
|------|-----------|---------------------|
| density matrix | B04 | B03 (question names it as the object that "should" encode the difference) |
| Bloch ball / Bloch vector | B07 | B07 (section card B06 sets up "same point" concept) |
| maximally mixed state | B07 | B07 (introduced alongside Bloch ball) |
| decomposition non-unique | B10 | B09 (section card names the concept) |

## Illustrative numbers / invented elements

- Station Z, Station X: invented names, ILLUSTRATIVE in B13
- The QKD security scenario: illustrative application, not a specific real-world case

All claims verified against `quantum-mechanics-vol4/chapters/01-mixed-states-and-the-density-matrix.md`.
