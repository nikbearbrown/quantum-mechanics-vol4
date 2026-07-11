# SHOTLIST — vox-fault-tolerance

| Beat | Type | Duration | Visual description |
|------|------|----------|--------------------|
| B01 | CARD/title | 10s | "3-qubit code: fix any single qubit error." sub: ERROR CORRECTION |
| B02 | GRAPHIC | 12s | Circuit diagram: ancilla qubit on top wire, Q1 and Q2 on data wires; CNOT from ancilla to Q1, then CNOT from ancilla to Q2; draw-on left to right |
| B03 | GRAPHIC | 12s | Same circuit; X error mark (CRIMSON) on ancilla wire between gate 1 and gate 2 |
| B04 | CARD/dek | 10s | "Why does one gate failure break a code designed for one error?" sub: THE QUESTION |
| B05 | CARD/section | 5s | "THE MECHANISM" |
| B06 | GRAPHIC | 14s | Circuit with CRIMSON error on ancilla at gate 1; arrow/highlight showing error copies onto Q2 via gate 2; CRIMSON label "2 data errors" |
| B07 | GRAPHIC | 12s | Syndrome table: rows = error syndromes, columns = Q1/Q2/Q3 flip status; highlight row where Q1+Q2 both flipped; show wrong correction arrow in CRIMSON |
| B08 | CARD/section | 5s | "TWO DIFFERENT REQUIREMENTS" |
| B09 | GRAPHIC | 13s | Two-column compare: left = "ERROR CORRECTION" (data qubit errors handled, TEAL); right = "FAULT TOLERANCE" (single circuit error → ≤1 data error, TEAL); CRIMSON annotation on the violation path |
| B10 | CARD/section | 5s | "THE FAULT-TOLERANT FIX" |
| B11 | GRAPHIC | 14s | New circuit: Ancilla A touches only Q1 (one CNOT); Ancilla B touches only Q2 (one CNOT); TEAL highlight showing each ancilla error stays local |
| B12 | CARD/section | 5s | "THE EXAMPLE" |
| B13 | GRAPHIC | 14s | Before/after split: left = one ancilla circuit (CRIMSON "3× error rate"); right = two ancilla circuit (TEAL "predicted rate"); cost label: "+1 qubit" |
| B14 | CARD/endcard | 10s | "Error correction: fix data qubit errors. Fault tolerance: no single gate error spreads to two data qubits." topic: QUANTUM MECHANICS |

## Scenes needed (GRAPHIC beats)
- B02_SyndromeCktClean — clean ancilla circuit, 2 CNOT gates
- B03_SyndromeCktError — same circuit with CRIMSON error on ancilla
- B06_ErrorPropagation — circuit with error propagating through gate 2 to Q2
- B07_WrongCorrection — syndrome table with wrong correction highlighted
- B09_TwoRequirements — side-by-side comparison card
- B11_FaultTolerantCkt — two-ancilla redesign circuit
- B13_BeforeAfter — before/after split diagram with error rates

## Rhythm check
CARD · GRAPHIC · GRAPHIC · CARD · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · CARD
Max consecutive GRAPHIC: 2 (B02–B03, B06–B07) ✓
Max consecutive CARD: 2 (B04–B05, B08... wait B08 is single, B09 is GRAPHIC) ✓
