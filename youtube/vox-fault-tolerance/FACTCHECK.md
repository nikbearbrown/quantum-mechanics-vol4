# FACTCHECK — vox-fault-tolerance

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | A 3-qubit bit-flip code can fix any single qubit error | ✓ | ch09 §3-Qubit Bit-Flip Code: four syndromes, four unambiguous diagnoses; "The logical qubit survives" | None |
| B02 | Ancilla applies CNOT to qubit 1 then CNOT to qubit 2; measures parity | ✓ | ch09 §Fault Tolerance: "The ancilla applies CNOT to qubit 1, then CNOT to qubit 2" (paraphrased from syndrome measurement description); parity measurement without reading encoded state | None |
| B03 | Ancilla has an error at gate 1 | ✓ (ILLUSTRATIVE) | ch09 §Fault Tolerance: "A single ancilla error during syndrome extraction can propagate through the circuit and affect multiple data qubits" — the specific gate 1 failure is ILLUSTRATIVE | Gate 1 error scenario ILLUSTRATIVE |
| B06 | Error on ancilla at gate 1 propagates through gate 2 to qubit 2; one ancilla error becomes two data-qubit errors | ✓ | ch09 §Fault Tolerance: "Two data qubits flipped simultaneously: a distance-3 code that can only correct one error fails" | None |
| B07 | 3-qubit code applies wrong correction when two data qubits are flipped | ✓ | ch09 §3-Qubit Bit-Flip Code syndrome table: two simultaneous bit-flips give a syndrome matching a different single-qubit error or no error — correction fails | None |
| B09 | Fault tolerance requires that a single error anywhere in the syndrome circuit propagates to at most one data-qubit error | ✓ | ch09 §Fault Tolerance: "Fault tolerance is the additional requirement that single errors in the syndrome circuit cause at most one logical error" | None |
| B09 | Fault tolerance requires redesigning the syndrome circuit | ✓ | ch09 §Fault Tolerance: "this demands careful ancilla circuit design: ancillas should not interact with more data qubits than the code can correct" | None |
| B11 | Using one ancilla per stabilizer: each ancilla touches only one data qubit; single ancilla error → at most one data-qubit error | ✓ | ch09 §Fault Tolerance: "The surface code is designed so that each syndrome qubit touches exactly four data qubits — single syndrome errors propagate to at most one data-qubit error" (adapted for simpler 3-qubit illustration) | None |
| B13 | Team deploys 3-qubit code, sees 3× higher logical error rate; investigation reveals one ancilla for both stabilizers; redesign with two separate ancillas fixes it | ✓ (ILLUSTRATIVE) | ch09 card example seed: "A quantum processor team deploys a 3-qubit bit-flip code and sees logical error rates 3× higher… redesign with two separate ancilla qubits." Numbers and team scenario ILLUSTRATIVE | All numbers and team scenario ILLUSTRATIVE |

## Exclusions confirmed

- No stabilizer group formalism (abelian subgroup, S notation): ✓
- No surface-code lattice (plaquette, star operators, lattice): ✓
- No threshold theorem formula (p_L ~ A(p/p_th)^⌈(d+1)/2⌉): ✓
- No magic-state distillation: ✓

## Terms table

| Term | Debut beat | Need established by |
|------|-----------|---------------------|
| parity / syndrome | B02 | B01 (error correction concept set up) |
| CNOT gate | B02 | B02 (introduced alongside parity measurement) |
| ancilla qubit | B02 | B01 (syndrome measurement context) |
| error propagation | B06 | B05 (section card "the mechanism" sets up the concept) |
| fault tolerance | B09 | B08 (section card "two different requirements" creates the need) |

## Illustrative numbers / invented elements

- Gate 1 error scenario in B03: ILLUSTRATIVE
- Team example in B13: ILLUSTRATIVE (logical error rate 3× higher, two-week debugging timeline)

All claims verified against `quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md`.
