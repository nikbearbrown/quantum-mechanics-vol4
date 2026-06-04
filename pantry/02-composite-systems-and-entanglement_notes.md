# Research Notes: Chapter 02 — Composite Systems and Entanglement
**Corresponding chapter:** chapters/02-composite-systems-and-entanglement.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)
Students can construct the Hilbert space of a composite system as a tensor product, distinguish separable from entangled states algebraically, write and verify the four Bell states, perform the Schmidt decomposition of any two-qubit pure state, use Schmidt rank as a binary entanglement criterion, and compute the entanglement entropy of a bipartite state.

---

## A. Conceptual foundations

### A1. Tensor products and the composite Hilbert space
If subsystem A has Hilbert space H_A (dimension d_A) and subsystem B has H_B (dimension d_B), the joint system lives in H_A ⊗ H_B (dimension d_A × d_B). Basis: {|i⟩_A ⊗ |j⟩_B} for all pairs i, j. An arbitrary state is |ψ_AB⟩ = Σ_{ij} c_{ij} |i⟩_A|j⟩_B with Σ_{ij} |c_{ij}|² = 1. The coefficient matrix C = [c_{ij}] encodes all the information; entanglement corresponds to C having rank > 1.

**Common misconception:** "The dimension of H_A ⊗ H_B is d_A + d_B." The correct dimension is d_A × d_B (product, not sum). Two qubits live in a 4-dimensional space, not a 2+2=4 space in the additive sense — the difference is non-trivial because the 4 basis states are |00⟩, |01⟩, |10⟩, |11⟩, not a concatenation of two 2-vectors.

**Worked example:** H_A = span{|0⟩, |1⟩}, H_B = span{|0⟩, |1⟩}. H_A ⊗ H_B = span{|00⟩, |01⟩, |10⟩, |11⟩}. Product state: |+⟩_A ⊗ |0⟩_B = (1/√2)(|00⟩ + |10⟩). Coefficient matrix C = [[1/√2, 0],[1/√2, 0]] has rank 1.

**Source(s):** _lib_qmsri-12-entanglement §opening proof; Nielsen & Chuang §2.1.7.

---

### A2. Separable vs. entangled states
A pure two-qubit state |ψ_AB⟩ is separable (product) if and only if it can be written |ψ_AB⟩ = |a⟩_A ⊗ |b⟩_B for some single-qubit states |a⟩, |b⟩. Equivalently: the coefficient matrix c_{ij} has rank 1. If rank > 1, the state is entangled. For mixed states ρ_AB, separability means ρ_AB = Σ_k p_k ρ_A^(k) ⊗ ρ_B^(k) (convex combination of product states); otherwise entangled. Mixed-state separability is computationally harder (Peres–Horodecki criterion: PPT is necessary and sufficient only for 2×2 and 2×3 systems).

**Common misconception:** "Any correlated quantum state is entangled." Classical correlations can produce strong correlations without entanglement. The state (1/2)(|00⟩⟨00| + |11⟩⟨11|) is a perfectly correlated mixture but separable. The CHSH parameter S distinguishes them operationally: separable states satisfy |S| ≤ 2; entangled states can violate this (see Ch. 03).

**Worked example (from local source):** |Φ+⟩ = (|00⟩+|11⟩)/√2. Try |Φ+⟩ = (α|0⟩+β|1⟩)⊗(γ|0⟩+δ|1⟩): need αγ = 1/√2, αδ = 0, βγ = 0, βδ = 1/√2. αδ = 0 → α = 0 or δ = 0; either leads to contradiction with the other equations. ∴ entangled. Source: _lib_qmsri-12-entanglement §opening paragraphs (full proof given).

**Source(s):** _lib_qmsri-12-entanglement §"What entanglement is not" and §opening; Horodecki et al. (2009), *Rev. Mod. Phys.* 81, 865.

---

### A3. The four Bell states
The Bell basis is the canonical orthonormal basis of maximally entangled two-qubit states:

|Φ±⟩ = (1/√2)(|00⟩ ± |11⟩)
|Ψ±⟩ = (1/√2)(|01⟩ ± |10⟩)

All four are maximally entangled: each has reduced density matrix ρ_A = ρ_B = I/2 (Bloch vector = 0). They form a complete orthonormal set — any two-qubit state expands in the Bell basis. Preparation circuit: |00⟩ → (H ⊗ I) → CNOT → |Φ+⟩. Starting from |01⟩, |10⟩, |11⟩ gives the other three Bell states via the same circuit. The singlet |Ψ−⟩ = (|01⟩ − |10⟩)/√2 is rotationally invariant: (U ⊗ U)|Ψ−⟩ = (det U)|Ψ−⟩.

**Common misconception:** "The Bell states have some preferred orientation in space." The singlet |Ψ−⟩ has full rotational invariance — its correlations E(â,b̂) = −â·b̂ depend only on the angle between measurement axes, a consequence of SU(2) symmetry.

**Worked example:** Starting from |10⟩: apply H to qubit 0 → (1/√2)(|0⟩+|1⟩)|1⟩ = (1/√2)(|01⟩+|11⟩). Apply CNOT (control=0, target=1) → (1/√2)(|01⟩+|10⟩) = |Ψ+⟩.

**Source(s):** _lib_qmsri-12-entanglement §"The four Bell states and the Bloch sphere" and §"Preparing a Bell state: two gates."

---

### A4. Schmidt decomposition and Schmidt rank
**Theorem (Schmidt):** Any pure bipartite state |ψ_AB⟩ ∈ H_A ⊗ H_B can be written |ψ_AB⟩ = Σ_k √λ_k |u_k⟩_A|v_k⟩_B where {|u_k⟩} and {|v_k⟩} are orthonormal sets and λ_k > 0 with Σ_k λ_k = 1. The √λ_k are the singular values of the coefficient matrix c_{ij}; the Schmidt vectors are the corresponding singular vectors (SVD). The Schmidt rank r = number of nonzero λ_k.

**Entanglement criterion:** |ψ_AB⟩ is separable if and only if Schmidt rank = 1. Schmidt rank ≥ 2 ↔ entangled.

**Proof sketch:** c_{ij} is a matrix; SVD gives c = U Diag(√λ_k) V†. Absorbing U into the A basis and V† into the B basis gives the Schmidt form. The Schmidt coefficients are uniquely determined by the state (though the vectors may not be unique if λ_k are degenerate).

**Common misconception:** "Schmidt decomposition requires knowing which is Alice's subsystem and which is Bob's." Formally the decomposition depends on the bipartition. For a fixed bipartition, the Schmidt coefficients are unique. Changing the bipartition changes the Schmidt decomposition.

**Worked example (canonical):** |ψ⟩ = (1/2)|00⟩ + (1/2)|01⟩ + (1/2)|10⟩ − (1/2)|11⟩. Coefficient matrix c = (1/2)[[1,1],[1,−1]]. SVD: c = (1/√2)[[1,1],[1,−1]] · Diag(1/√2, 1/√2) · ... Wait, let's compute directly: c†c = (1/4)[[1,1],[1,−1]]†[[1,1],[1,−1]] = (1/4)[[2,0],[0,2]] = (1/2)I. Eigenvalues λ_1 = λ_2 = 1/2. Schmidt rank = 2 → **entangled**. Schmidt decomposition: |ψ⟩ = (1/√2)|u_1⟩|v_1⟩ + (1/√2)|u_2⟩|v_2⟩ with |u_1⟩ = |0⟩, |u_2⟩ = |1⟩ (or appropriate singular vectors). Entanglement entropy = −(1/2)log(1/2) − (1/2)log(1/2) = log 2 = 1 ebit. This state is maximally entangled.

**Source(s):** Nielsen & Chuang §2.5; Wikipedia, Schmidt decomposition (https://en.wikipedia.org/wiki/Schmidt_decomposition); Preskill lecture notes Ch. 4.

---

### A5. Entanglement entropy
The von Neumann entropy of the reduced state S(ρ_A) = −Tr(ρ_A log ρ_A) = −Σ_k λ_k log λ_k (in nats or bits according to the base of log) quantifies entanglement for pure bipartite states. Properties: S = 0 for product states (Schmidt rank 1, one λ_k = 1); S = log r (max) for maximally entangled states (all λ_k = 1/r). For a Bell state (two-qubit), λ_1 = λ_2 = 1/2: S = −2·(1/2)log(1/2) = log 2 = 1 ebit (1 bit if log base 2). Entanglement entropy is the unique measure of entanglement for pure bipartite states (under LOCC monotonicity axioms).

**Common misconception:** "A higher-entropy state is always more entangled in a useful sense." Entanglement entropy is a good measure for pure bipartite states. For mixed states or multipartite systems, no single measure captures all aspects of entanglement, and the field has many competing measures (entanglement of formation, distillable entanglement, etc.).

**Worked example:** Product state |00⟩: λ_1 = 1. S = 0. Bell state |Φ+⟩: λ_1 = λ_2 = 1/2. S = 1 bit. Partially entangled state |ψ⟩ = (√3/2)|00⟩ + (1/2)|11⟩: λ_1 = 3/4, λ_2 = 1/4. S = −(3/4)log₂(3/4) − (1/4)log₂(1/4) = (3/4)·0.415 + (1/4)·2 = 0.811 bits. Between 0 and 1 ebit.

**Source(s):** Nielsen & Chuang §2.5, §11.3.1; Bennett et al. (1996), *Phys. Rev. A* 53, 2046 (operational interpretation of entanglement entropy).

---

## B. Domain examples and cases

**Bell-state preparation in quantum hardware:** The circuit H → CNOT is the standard two-gate Bell-pair preparation in every superconducting and trapped-ion quantum processor. CNOT gate fidelities directly determine the purity (Tr ρ²) of the produced Bell pair, with Tr ρ² measured via Bell tomography. Source: _lib_qmsri-12-entanglement §"Preparing a Bell state: two gates."

**Teleportation resource:** Bell pairs are the entanglement resource consumed by quantum teleportation (Bennett et al. 1993). One Bell pair + two classical bits teleports an unknown qubit. The protocol works because |Ψ_unknown⟩ ⊗ |Φ+⟩_{AB} can be rewritten in the Bell basis of the first two qubits, making Bob's state a known rotation of the original. Source: _lib_qmsri-12-entanglement §Teleportation.

**Schmidt rank in quantum communication:** Schmidt rank r upper-bounds the number of ebits of entanglement in a pure state. A state with Schmidt rank r requires a Hilbert space of dimension at least r on each side to represent it — this constrains the minimum dimension of the entanglement resource needed for a given quantum information task.

---

## C. Connections and dependencies

- **Prerequisite:** Ch. 01 (density matrix, partial trace — the Schmidt decomposition's eigenvalues are exactly the eigenvalues of ρ_A).
- **Feeds forward:** Ch. 03 (CHSH violation — the Bell states are the states that achieve S = 2√2; the singlet is the one most commonly used in Bell test analyses). Ch. 04 (Lindblad — entanglement decays under open-system dynamics, entanglement entropy decreases from 1 ebit toward 0 as the Bell pair decoheres).
- **Structural relation:** The Schmidt coefficients {√λ_k} are the singular values of the coefficient matrix c_{ij}; equivalently, {λ_k} are the eigenvalues of ρ_A (and of ρ_B, which has the same non-zero spectrum). This is the algebraic unification of Schmidt decomposition and reduced density matrix.

---

## D. Current state of the field

**Settled:** Tensor product structure, separability criterion for pure states (Schmidt rank), Bell basis, entanglement entropy for pure bipartite states. These are mathematically complete since the 1990s.

**Active:** Mixed-state entanglement theory. The separability problem (deciding whether a given mixed state ρ_AB is entangled) is NP-hard in general. The PPT criterion (Peres 1996) and the Horodecki criterion are the main tools but not universally sufficient. Source: Horodecki et al. (2009), *Rev. Mod. Phys.* 81, 865.

**Active:** Multipartite entanglement. For three or more parties, entanglement has multiple inequivalent classes (GHZ vs. W states cannot be interconverted by LOCC). The classification is not complete for five or more parties.

**Recent developments:** Shadow tomography (Huang et al. 2020, *Nature Physics*) enables efficient estimation of entanglement entropy in large systems using randomized measurements. Entanglement entropy has become a central diagnostic in many-body physics (area laws, topological order).

**Key references:**
- Nielsen & Chuang, *Quantum Computation and Quantum Information*, §2.5 (Schmidt decomposition), §2.4 (entanglement).
- Horodecki, R., Horodecki, P., Horodecki, M., & Horodecki, K. (2009). Quantum entanglement. *Rev. Mod. Phys.* 81, 865. https://doi.org/10.1103/RevModPhys.81.865
- Preskill, J., Ph219/CS219 Lecture Notes, Ch. 4. http://www.theory.caltech.edu/~preskill/ph219/
- Wootters, W. K. (1998). Entanglement of formation of an arbitrary state of two qubits. *Phys. Rev. Lett.* 80, 2245.

---

## E. Teaching considerations

- **Hardest step:** The Schmidt decomposition feels abstract until students see that it is just SVD of the coefficient matrix. Framing it as "SVD of c_{ij}" makes it immediately computable.
- **Worked example selection:** The canonical example should be a state that is NOT one of the four Bell states — so students practice the SVD procedure. A state like (1/2)|00⟩ + (1/√2)|01⟩ + (something)|11⟩ with a non-obvious Schmidt decomposition is ideal.
- **Schmidt rank vs. Schmidt number:** Schmidt rank is a binary criterion (1 = separable, >1 = entangled). The actual values of the Schmidt coefficients give the quantitative measure (entanglement entropy). Distinguish these.
- **Simulation hook:** The CHSH simulator in the capstone (Tab 1) shows the Bloch vectors of each qubit collapsing to the origin when |Φ+⟩ is prepared — a visual demonstration that each subsystem is maximally mixed (entanglement entropy = 1 ebit).
- **Gotcha for instructors:** The no-cloning theorem (§"No-cloning" in local source) follows directly from the linearity of unitary operations and is a corollary of the tensor product structure. It should appear in or after Ch. 02, not before.

---

## F. Library files relevant to this chapter

- **_lib_qmsri-12-entanglement-and-quantum-information.md** — Primary source. Contains: the algebraic proof that |Φ+⟩ is entangled (§opening); the four Bell states defined (§"The four Bell states and the Bloch sphere"); the two-gate preparation circuit H→CNOT (§"Preparing a Bell state"); the Bloch vector collapse for entangled states (fig 12.3); the no-signaling theorem via partial trace; no-cloning theorem (§"No-cloning"); teleportation protocol (§"Teleportation"). Very rich — this file is the primary draft for Ch. 02.
- **_lib_qmsri-13-capstone-quantum-mechanics-in-research.md** — Secondary. Contains the reduced density matrix formula and Bloch vector (§"Mixed states and the density matrix") which underpins the connection between entanglement and mixed subsystems.
- **_lib_qmsri-qm-townsend-notes.md** — No Schmidt or entanglement content found by grep. Not useful for Ch. 02.

---

## G. Gaps and flags

- **Schmidt decomposition not in any local source.** The local library files do not contain a Schmidt decomposition derivation or worked example. The chapter author must write this from scratch, drawing on Nielsen & Chuang §2.5 and/or Preskill Ch. 4.
- **Entanglement entropy not in local sources.** Neither local file contains a treatment of von Neumann entropy as an entanglement measure. Standard references needed.
- **The "classical mixture vs. entangled" distinction** is set up nicely in _lib_qmsri-12 (§"What entanglement is not") but only qualitatively. A quantitative demonstration — computing the CHSH parameter for a classical mixture and showing |S| ≤ 2 — would strengthen the chapter and must be added.
- **Mixed-state entanglement:** Local sources only treat pure-state entanglement. A brief mention of the PPT criterion for mixed states (as a flag for further study) should appear in Ch. 02 or be deferred explicitly to an appendix.
- **Flag:** _lib_qmsri-12 contains a malformed table in §"What the experiments showed" (table rows show placeholder text "A concrete checkpoint for applying the chapter concept."). That section is relevant to Ch. 03, not Ch. 02. The malformed table is from the original source file and should not be reproduced; replace with properly cited text.
