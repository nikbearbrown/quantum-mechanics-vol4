# PEDAGOGY — vox-fault-tolerance

## Concept to teach
Fault tolerance is a SEPARATE requirement from error correction. A 3-qubit bit-flip code can correct any single data-qubit error, but its syndrome circuit can still fail logically if that circuit lets one ancilla error propagate into two data-qubit errors. Fault tolerance requires redesigning the syndrome circuit so that no single gate error can cause more than one data-qubit error.

## Target audience
Anyone who has heard "quantum error correction" and assumes the code handles everything. No prior knowledge of stabilizer formalism required.

## Prior knowledge assumed
- Qubits can flip (bit-flip error)
- Some mechanism called "parity check" can detect errors without reading the qubit
- One error is bad; two errors simultaneously can defeat a code designed for one

## Prior knowledge NOT assumed
- Stabilizer group formalism
- Surface code geometry
- Threshold theorem formula

## Learning arc

### Step 1 — Anchor (B01–B03)
Start with the promise: 3-qubit code corrects any single-qubit error. Show the syndrome circuit: one ancilla, two CNOTs, two data qubits. Then reveal the crack: the ancilla itself has an error at gate 1. The viewer expects this to be fine. The code handles one error.

### Step 2 — Tension (B04–B05)
Ask THE QUESTION explicitly on screen. Why does a single gate failure defeat a code designed to survive one error? Create cognitive dissonance before resolving it.

### Step 3 — Mechanism (B06–B07)
Show the propagation: ancilla error at gate 1 → CNOT at gate 2 copies that error to qubit 2 → two data qubits are now flipped. Show the syndrome table: the code sees a pattern it interprets as a single-qubit error in the wrong place, applies the wrong correction, loses the logical qubit. One physical gate failure → one logical qubit failure.

### Step 4 — Distinction (B08–B09)
Name the two requirements clearly: error correction (handles data errors) vs. fault tolerance (constrains how errors propagate through the syndrome circuit itself). Fault tolerance is the additional requirement that ONE error anywhere in the circuit → AT MOST ONE data-qubit error.

### Step 5 — Fix (B10–B11)
The solution: use one ancilla per stabilizer instead of one ancilla for both. Each ancilla touches only one data qubit. Now any single ancilla error can corrupt at most one data qubit — within what the code can correct.

### Step 6 — Example (B12–B13)
Concrete case: a team deploys the 3-qubit code with one shared ancilla, sees 3× higher logical error rates. Investigation reveals the ancilla circuit design. Adding a second ancilla (one per stabilizer) fixes the problem at the cost of one extra qubit.

### Step 7 — Synthesis (B14)
Endcard crystallizes the distinction: error correction ≠ fault tolerance. The code's correctability does not guarantee the circuit is fault tolerant.

## Common misconceptions addressed
1. **"Error correction handles everything"** — No. The syndrome circuit itself can spread errors.
2. **"One error = one qubit error"** — Not if the syndrome circuit is shared: one ancilla error can become two data-qubit errors via CNOT.
3. **"More qubits = overkill"** — The second ancilla is the minimal fix; it actually earns its cost.

## Pacing check
- B01–B03: establish promise then crack it (34s)
- B04–B05: ask the question (15s)
- B06–B07: mechanism (26s)
- B08–B09: distinction (18s)
- B10–B11: fix (19s)
- B12–B13: example (19s)
- B14: recap (10s)
Total ~141s. Tight but appropriate for the concept's complexity.

## Color semantics check
- TEAL: fault-tolerant design, contained error, correctable path
- CRIMSON: error propagation, two data-qubit errors, code failure
These map cleanly to the narrative: CRIMSON for the shared-ancilla failure path, TEAL for the two-ancilla fix.

VERDICT: PASS
