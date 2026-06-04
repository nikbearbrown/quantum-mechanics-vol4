# Research Notes: Chapter 08 — Quantum Hardware and the NISQ Era

**Corresponding chapter:** chapters/08-quantum-hardware.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

The student can map any physical qubit platform onto the two-level Hilbert-space formalism from Volume 1. Given a platform's Hamiltonian, they can identify |0⟩ and |1⟩, characterize the gate operations and readout mechanism, and interpret T₁ and T₂ specs in terms of the Lindblad/Bloch picture of Chapter 13. They understand what "NISQ" means structurally — why current machines can demonstrate interesting behavior but cannot yet support full fault tolerance — and can read a hardware paper's methods section.

---

## A. Conceptual foundations

### DiVincenzo criteria (2000)
Five requirements for a viable qubit, from DiVincenzo, Fortschritte der Physik 48, 771 (2000):
1. **Scalable physical system** with well-characterized qubits
2. **Initialization** to a fiducial state (e.g., |0⟩)
3. **Long coherence times** relative to gate times (error rate per gate ≪ 1%)
4. **Universal set of quantum gates** (single-qubit rotations + entangling 2-qubit gate suffices)
5. **Qubit-specific measurement** capability

Two additional criteria for quantum communication (often added):
6. Ability to interconvert stationary and flying qubits
7. Faithful transmission of flying qubits between locations

The criteria function as a rubric, not a checklist that any one platform currently fully satisfies at scale. Each platform has its characteristic trade-offs (coherence time vs. gate speed, connectivity vs. individual addressability, scalability vs. fidelity per qubit).

### The NISQ concept (Preskill 2018)
John Preskill coined "NISQ" in his 2018 essay (Quantum 2, 79). Defining characteristics:
- ~50–1000 physical qubits
- Gate fidelities high enough to run circuits of modest depth
- Gate fidelities NOT high enough to support full quantum error correction
- The structural progression: NISQ → fault-tolerant → useful quantum advantage
- NISQ machines may demonstrate "quantum advantage" on contrived problems (sampling) without being computationally useful in a practical sense

The term has begun to evolve: some researchers now speak of "utility-scale" quantum computing and "megaquop" machines (ACM Transactions on Quantum Computing, 2026) to describe devices that have crossed specific error-rate thresholds while still short of full fault tolerance.

### Coherence times: T₁ vs. T₂ vs. T₂*
- **T₁**: energy relaxation time (excited state decaying to ground state); sets the upper bound on circuit depth
- **T₂**: coherence time (Bloch vector transverse decay); always T₂ ≤ 2T₁
- **T₂***: inhomogeneous dephasing time (free-induction decay, without spin echo); often shorter than T₂ in real devices
- **Gate fidelity** requires many gate operations within T₁ and T₂: the figure of merit is (gate time) / T₁ and T₂

---

## B. Domain examples and cases

### Platform 1: Superconducting transmons (IBM, Google)

**Physical realization of |0⟩, |1⟩:**
The transmon is an anharmonic LC oscillator where the inductor is a Josephson junction (a thin insulating barrier between two superconductors). The non-linear inductance of the Josephson junction creates unequally spaced energy levels E₀ < E₁ < E₂ < ... with the anharmonicity α = (E₂ - E₁) - (E₁ - E₀) ≈ -200 to -300 MHz. The two lowest levels are selected as |0⟩ and |1⟩. The qubit transition frequency is typically ω₀/2π ≈ 4–8 GHz.

**Hamiltonian (two-level approximation):**
H_transmon ≈ (ℏω₀/2)σ_z − E_J cos(φ)

In the charge basis the full Hamiltonian is H = 4E_C(n - n_g)² - E_J cos(φ), where E_C is the charging energy, E_J the Josephson energy, n the Cooper pair number operator, n_g the gate charge. The transmon regime is E_J/E_C ≫ 1 (~50), which exponentially suppresses charge noise while keeping sufficient anharmonicity for two-level control. In the two-level limit this reduces to the familiar Pauli Hamiltonian.

**Gates:**
- Single-qubit gates: microwave pulses at ω₀ (X, Y rotations via Rabi driving); virtual Z gates (phase shifts) at essentially zero error
- Two-qubit gates: cross-resonance (IBM) or parametric coupling (Google); gate time ~20–500 ns

**Readout:**
Dispersive readout: the qubit is coupled to a readout resonator; the resonator frequency shifts by ±χ depending on qubit state. Probe the resonator with a microwave pulse; the phase of the reflected signal distinguishes |0⟩ from |1⟩. Fidelity ~97–99%.

**Current state (2024–2025):**
- IBM Eagle: 127 qubits; T₁/T₂ > 300 µs; median 2-qubit gate error ~0.17%; ~1,500 two-qubit gates per coherence cycle (IBM Quantum blog, 2024)
- IBM Heron r2 (July 2024): 156 qubits, heavy-hexagonal lattice; ~5,000 two-qubit gates within coherence (3–5× improvement over Eagle); TLS mitigation reduces low-frequency noise (IBM Wikipedia/docs, 2024)
- IBM Heron r3 (July 2025): targeted manufacturing improvements to coherence and fidelity
- Google Willow (December 2024): 105 qubits; T₁ ~100 µs (5× longer than Sycamore); used to demonstrate below-threshold surface code error correction (Nature 2025, see Ch 9 notes)
- Best research transmons (2025): T₁ approaching 1.68 ms in 2D devices (Nature 2025, "Millisecond lifetimes and coherence times in 2D transmon qubits")
- Single-qubit gate fidelity routinely >99.9%; two-qubit gate fidelity ~99.0–99.7% depending on device

**Dominant noise sources:**
Dielectric loss (two-level system defects in substrate/junctions), charge noise, flux noise, quasiparticle poisoning, residual thermal photons in control lines.

### Platform 2: Trapped ions (Quantinuum, IonQ)

**Physical realization:**
Individual atomic ions (typically ⁴⁰Ca⁺ at Oxford/Quantinuum, ¹⁷¹Yb⁺ at IonQ) held in Paul traps by oscillating electric fields. |0⟩ and |1⟩ are two long-lived electronic states (hyperfine or optical transitions). Ions are individually addressed by focused laser beams or microwave fields. Shared motional modes of the ion chain mediate entanglement (Mølmer-Sørensen gate or similar).

**Gates:**
- Single-qubit: laser or microwave pulses; fidelity routinely >99.99%
- Two-qubit: Mølmer-Sørensen or geometric phase gates via shared phonon modes; gate time ~10–1,000 µs (much slower than superconducting)

**Readout:**
State-dependent fluorescence; illuminating with a detection laser causes one state to scatter photons (bright) and the other to remain dark. Fidelity >99.9%.

**Current state (2024–2025):**
- Quantinuum H2 (2023–2024): 56 trapped-ion qubits; 56-qubit QV; two-qubit gate fidelity ~99.7%; used in Microsoft joint demonstration of 12 logical qubits with 99.9%+ fidelity on operations (April 2024)
- Quantinuum Helios (November 2025): 98 barium ion qubits; two-qubit gate fidelity 99.921% across all qubit pairs; coherence times in seconds to minutes; first demonstration of 48 logical qubits
- IonQ Oxford Ionics (2025): two-qubit fidelity exceeding 99.99% without ground-state cooling; SPAM fidelity 99.9993% — the highest published gate fidelity on any platform
- Coherence times: T₁ and T₂ in seconds to minutes (orders of magnitude longer than superconducting), but gate times are orders of magnitude slower

**Dominant noise sources:**
Motional heating of ion chain, laser frequency/intensity noise, anomalous electric field noise, crosstalk between adjacent ions.

### Platform 3: Neutral atoms in optical tweezers (QuEra, Atom Computing, Pasqal)

**Physical realization:**
Neutral atoms (typically ⁸⁷Rb or ¹³³Cs or alkaline-earth-like atoms) trapped in tightly focused laser beams (optical tweezers). |0⟩ and |1⟩ are hyperfine ground states. Arrays can be arbitrary (programmable geometry). Entanglement via Rydberg blockade: exciting atoms to high principal quantum number n states (n~50–100) creates a dipole-dipole interaction that blocks double excitation within a ~10 µm radius.

**Gates:**
- Single-qubit: microwave or two-photon Raman pulses
- Two-qubit: Rydberg blockade gate; gate time ~0.1–1 µs
- Large-scale connectivity: atoms can be physically moved (tweezers are reconfigurable)

**Current state (2024–2025):**
- QuEra Aquila (2023): 256 programmable neutral-atom qubits; used for analog quantum simulation benchmarks
- QuEra / Harvard / MIT (November 2023, Nature): 48 logical qubits demonstrated on a 280-atom system using transversal gates on [[8,3,2]] color codes — first demonstration of fault-tolerant gates on many logical qubits simultaneously; Nature 626, 58 (2024), Bluvstein et al.
- QuEra 2025 (January 2026 Nature): 96 logical qubits from 448 physical atoms using [[16,6,4]] high-rate codes — largest logical qubit count to date
- Atom Computing Phoenix: 1,180 neutral-atom qubits, the largest production neutral-atom system as of 2026
- Harvard 2025: ran a 3,000-qubit atom array continuously for over two hours with mid-computation atom replenishment
- Gate fidelities: two-qubit Rydberg fidelities ~99.5% in best demonstrations; improving rapidly

**Dominant noise sources:**
Atom loss (atoms fall out of tweezers), Rydberg lifetime, laser phase noise, crosstalk from neighboring Rydberg excitations.

### Platform 4: Photonic qubits (Xanadu, PsiQuantum)

**Physical realization:**
|0⟩ and |1⟩ encoded in photon number states (Fock), polarization states, or time-bin encoding. Linear optic quantum computing (LOQC) uses beam splitters, phase shifters, and photon-number-resolving detectors. Continuous-variable (CV) quantum computing (Xanadu) uses Gaussian states and homodyne detection.

**Gates:**
Linear optics gates are inherently probabilistic for entangling operations (KLM 2001). Photon losses are the dominant error source. Fusion-based approaches (PsiQuantum) build fault tolerance from resource states and Bell measurements.

**Current state:**
- Photonics is furthest from demonstrating a general-purpose qubit processor
- Xanadu Borealis (2022): advantage demonstration in Gaussian boson sampling; contested as a genuinely useful task
- No photonic platform has demonstrated universal gate-based quantum computing at scale
- PsiQuantum's silicon photonics approach targets million-qubit fabrication via foundry processes (not demonstrated at scale as of 2026)

**Advantages:** Room-temperature operation, long coherence (photons don't interact with environment easily), natural for quantum communication. **Disadvantages:** Difficult to entangle photons deterministically; detector inefficiency; photon loss.

### Platform 5: NV centers in diamond (Quantum Brilliance, research groups)

**Physical realization:**
A nitrogen-vacancy (NV) center is a point defect: a nitrogen atom adjacent to a lattice vacancy. The NV⁻ charge state has a spin-1 ground state with D ≈ 2.87 GHz zero-field splitting. The qubit is the m_s = 0 vs. m_s = ±1 subspace. Initialized by optical pumping (532 nm green laser); read out by spin-dependent fluorescence (ODMR). Gates via microwave pulses.

**Effective Hamiltonian:**
H_NV = D·Ŝ_z² + gμ_B B·Ŝ_z

which in the |0⟩, |−1⟩ subspace (with applied B field) maps onto (ℏω₀/2)σ_z with ω₀/2π ≈ D ∓ 28B MHz/mT.

**Current state:**
- T₁ ~1–6 ms at room temperature; T₂ ~100 µs–2 ms (with dynamical decoupling)
- Gate fidelity: single-qubit ~99%; two-qubit via dipolar coupling of nearby NV centers is significantly harder (~80–95%)
- Quantum Brilliance: working toward room-temperature chip-scale NV processors; 2-qubit lab devices with confocal readout as of 2025; integrated photoelectric readout planned for next-generation
- Primary value currently is in quantum sensing: magnetometry at nT/√Hz sensitivity, nanoscale MRI, geophysical sensing (see also Ch 10 capstone)

**Key advantage:** Room-temperature operation, operates in solid state without cryogenic equipment.

### Platform 6: Semiconductor spin qubits (Intel, Delft/QuTech, research groups)

**Physical realization:**
Single electron spins in gate-defined quantum dots in silicon or silicon-germanium heterostructures. |0⟩ = spin up, |1⟩ = spin down in an applied magnetic field. Extremely small devices; natural compatibility with CMOS fabrication.

**Current state (2024–2025):**
- Intel (May 2024, Nature): 99.9% gate fidelity demonstrated on spin qubits fabricated on 300 mm production line; spin qubits up to 0.5 s T₁ coherence times
- Nature (2025): "Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity" (full CMOS-compatible process)
- 12-spin-qubit arrays demonstrated from 300 mm semiconductor manufacturing line (Nano Letters, 2025)
- Two-qubit gate fidelities: >99% achieved in research settings; below fault-tolerance threshold in current larger arrays
- Dominant challenge: qubit-to-qubit variability in large arrays; charge noise; difficulty of individual addressing at scale

---

## C. Connections and dependencies

- **Volume 1 (two-level systems, Pauli algebra):** The transmon Hamiltonian reduces to (ℏω₀/2)σ_z in the two-level limit; all gate operations are SU(2) rotations. The formal framework was built in Vol. 1.
- **Volume 1 / Rabi oscillations:** Driving a qubit at resonance produces Rabi oscillations; this is the basis for all single-qubit gates.
- **Chapter 13 (density matrix, Lindblad, Bloch equations):** T₁ and T₂ are the phenomenological parameters of the Bloch equations derived in Ch 13. Every platform's coherence specs are entries in those equations.
- **Chapter 9 of this volume (error correction):** The NISQ section here directly feeds the motivation for Ch 9; the gate fidelities cited here determine whether platforms are above or below the ~1% threshold.
- **NV center Hamiltonian → Ch 13 and Vol. 3 perturbation theory:** The Zeeman splitting of the NV center is a direct application of first-order perturbation theory (Vol. 3, Ch. 9). This chapter provides the hardware context; Ch 13 and Vol. 3 provide the derivation.

---

## D. Current state of the field (specific and current as of 2026-06)

**Superconducting:**
- IBM Heron r2 (156 qubits, July 2024): ~5,000 two-qubit gates within coherence; TLS mitigation
- IBM Heron r3 (July 2025): further coherence and fidelity improvements
- Google Willow (105 qubits, Dec 2024): T₁ ~100 µs; demonstrated below-threshold surface code (see Ch 9 notes)
- Best research T₁: approaching 1.68 ms in 2D transmons (Nature 2025)
- The "megaquop" framing (ACM TQC 2026) proposes 10⁶ high-fidelity gate operations as the next milestone beyond NISQ

**Trapped ions:**
- Quantinuum Helios (98 qubits, Nov 2025): 99.921% two-qubit fidelity; 48 logical qubits demonstrated
- IonQ / Oxford Ionics (2025): 99.99% two-qubit fidelity — highest on any platform
- Quantinuum + Microsoft (April 2024): 12 logical qubits with 99.9%+ fidelity, error rates 800× below physical error rates

**Neutral atoms:**
- QuEra / Harvard / MIT (Jan 2024, Nature 626): 48 logical qubits from 280-atom array using color codes
- QuEra (Jan 2026, Nature): 96 logical qubits from 448 atoms — current logical-qubit count record
- Atom Computing Phoenix: 1,180 physical qubits in production

**Semiconductor spin:**
- Intel / 300 mm line (2024–2025): 99.9% single-qubit fidelity in industry-fabricated devices; 12-qubit arrays
- Nature 2025: industry-compatible process exceeding 99% fidelity

**NV centers:**
- Primary frontier: sensing (nT/√Hz magnetometry) and quantum networking nodes rather than gate-based computing
- Room-temperature chip-scale computing (Quantum Brilliance): 2-qubit devices in lab; integrated readout in development

**Overall landscape:**
No single platform has demonstrated unambiguous practically useful quantum advantage. The competition is not settled; trapped ions lead on fidelity per gate, superconducting leads on speed and scale, neutral atoms lead on demonstrated logical-qubit counts. The "correct" platform for fault-tolerant quantum computing remains an open question as of 2026.

---

## E. Teaching considerations

**Where students struggle:**
1. Conflating T₁ (energy relaxation) with T₂ (coherence); the constraint T₂ ≤ 2T₁ needs to be derived before quoting hardware specs
2. Thinking "qubit" means the physical object rather than the mathematical two-level system instantiated by many different physical systems
3. Gate fidelity vs. coherence time: a fast gate with lower fidelity can beat a slow gate with higher fidelity depending on the circuit depth
4. NISQ confusion: students think "NISQ = bad"; the point is that NISQ devices are interesting and can do things, but cannot support error correction

**Pedagogical moves:**
- Start with DiVincenzo criteria as a rubric, then go through each platform asking "how does this platform satisfy each criterion?"
- The "worked example" (see below) should show concretely how H_transmon or H_NV → H = (ℏω₀/2)σ_z; the formalism is the same, the physics realization differs
- Use a table comparing coherence times and gate times across platforms — the orders-of-magnitude differences are striking
- The "gate operations per coherence time" ratio (T₁/gate time) is the key figure of merit for early fault tolerance discussions

**Worked example (NV center or transmon → Vol. 1 two-level formalism):**

For the **transmon**: Show that in the two-level approximation, H_transmon = -E_J cos(φ) + 4E_C n² maps to (ℏω₀/2)σ_z with ω₀ = √(8E_JE_C)/ℏ − E_C/ℏ (the anharmonicity), and that microwave driving adds ℏΩ cos(ω_d t)σ_x (Rabi drive). The student has already solved H = (ℏω₀/2)σ_z + ℏΩ cos(ωt)σ_x in a rotating frame.

For the **NV center**: H_NV = D Ŝ_z² + gμ_B B Ŝ_z. In the m_s = {0, −1} subspace this is exactly (ℏω₀/2)σ_z with ω₀/2π = D + 28B MHz/mT (for the m_s = 0 → m_s = −1 transition). The Rabi drive is a microwave oscillating field at this frequency. Readout is optical rather than dispersive, but the underlying physics is the same two-level dynamics from Vol. 1.

---

## F. Library files relevant to this chapter

- `/pantry/_lib_qmsri-13-capstone-quantum-mechanics-in-research.md`: Section "The NISQ era and the threshold theorem" provides the structural framing; Section "NV centers: Chapter 9 perturbation theory made real" gives the NV Hamiltonian and ODMR derivation that can be adapted for the worked example.
- The library file cites: Preskill 2018 (Quantum 2, 79) for NISQ definition; Doherty et al. 2013 (Physics Reports 528, 1) for NV center review; Rondin et al. 2014 (Rep. Prog. Phys. 77, 056503) for ODMR magnetometry.

---

## G. Gaps and flags

1. **Photonics coverage is thin.** Photonic quantum computing (Xanadu, PsiQuantum) is moving fast and the fusion-based architecture is conceptually interesting but technically complex. A brief conceptual treatment sufficient to explain why photonics faces different challenges (probabilistic gates, photon loss) without requiring a full KLM treatment is needed. This is a known scope risk.

2. **Transmon Hamiltonian derivation depth.** Fully deriving H_transmon from the Josephson junction Lagrangian requires circuit QED background not in prior volumes. The chapter should aim for the "reduced" worked example — showing the two-level approximation is valid at E_J/E_C ~ 50 — without the full circuit derivation. Flag for pedagogy team.

3. **Platform table numbers go stale quickly.** The specific T₁, T₂, and fidelity numbers cited here were current as of mid-2026 but will be obsolete within 12–24 months. The chapter should (a) cite the structural/regime-level numbers as durable and (b) direct readers to IBM Quantum docs / arXiv review papers for current specs.

4. **Semiconductor spin qubits: scalability question open.** The 2024–2025 results on 300 mm wafers are encouraging for eventual scalability, but qubit-to-qubit variability in large arrays is a real unsolved problem. Do not overstate where this platform stands.

5. **No coverage of topological qubits.** Microsoft's Majorana-based approach is not included in this chapter. The _lib_qmsri-13 file notes this is "one of the field's largest open bets" as of 2026 with no demonstrated advantage. Brief mention with pointer to Ch 13 honesty section is appropriate; deep treatment is not warranted.

6. **NIST PQC standards (August 2024):** FIPS 203, 204, 205 finalized. Worth a brief mention as context for why this hardware race matters even before fault-tolerant machines exist.

---

*Web sources consulted:*
- Acharya et al. (Google Quantum AI), Nature 638, 920 (2024/2025) — below-threshold surface code on Willow
- IBM Quantum documentation and blog: Eagle, Heron r1/r2/r3 specs (2023–2025)
- Quantinuum press releases: H2 (2023), Helios (Nov 2025), Microsoft joint demonstration (April 2024)
- Bluvstein et al. (QuEra/Harvard/MIT), Nature 626, 58 (2024) — 48 logical qubits, neutral atoms
- QuEra / Harvard / MIT, Nature (Jan 2026) — 96 logical qubits, 448-atom array
- Nano Letters 2025 — 12-spin-qubit arrays from 300 mm line
- Nature 2025 — "Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity"
- Nature 2025 — "Millisecond lifetimes and coherence times in 2D transmon qubits"
- Preskill 2018, Quantum 2, 79 (NISQ definition)
- DiVincenzo 2000, Fortschritte der Physik 48, 771
- Doherty et al. 2013, Physics Reports 528, 1 (NV center review)
- Rondin et al. 2014, Rep. Prog. Phys. 77, 056503 (ODMR)
