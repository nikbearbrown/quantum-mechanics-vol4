# Simulation Ideas — quantum-mechanics-vol4

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — CHSH Inequality: −cos θ Curve Beats the Classical Bound
- Source: `quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: CHSH score S = −cos(θ_AB) − cos(θ_AB') − cos(θ_A'B) + cos(θ_A'B'); max classical = 2; quantum max = 2√2 ≈ 2.828
- Concrete numbers: optimal angles θ = 0°, 45°, 90°, 135°; S_QM = 2√2 = 2.828; S_classical ≤ 2; gap = 0.828
- Visual artifact: −cos(θ) correlation curve sweeping over angle; horizontal lines at S=2 (classical) and S=2√2 (quantum); highlight region that violates Bell
- Two testable predictions: P1: S = 2.000 exactly at classical-mimicking angles (0°/90°/0°/90°); P2: S = 2√2 at optimal quantum angles (measurable to 4 decimal places in experiment)
- Sim slug: medhavy-vol4-chsh-curve
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-chsh-curve/medhavy-vol4-chsh-curve-review.mp4`
- Note: CROSS-REFERENCE — vox-chsh-ceiling is an explainer in quantum-mechanics-a-companion-guide. This simulation workflow reel (Claude Code plotting the correlation curve) is new; build it.

---

## Sim-02 — Bloch Decoherence: T₂ Decay of the Off-Diagonal
- Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: ρ₀₁(t) = ρ₀₁(0) · e^(−t/T₂); Bloch vector component in x-y plane decays exponentially with time T₂
- Concrete numbers: T₂ = 1 μs (typical NMR); at t=T₂, |ρ₀₁| has fallen to 1/e ≈ 0.368 of initial; at t=3T₂ → 0.050
- Visual artifact: Bloch sphere with the equatorial component spiraling inward exponentially while the z-component stays (if pure dephasing, T₁ → ∞)
- Two testable predictions: P1: |ρ₀₁(T₂)| / |ρ₀₁(0)| = 1/e = 0.3679 exactly; P2: doubling γ_dephasing halves T₂ (T₂ = 1/γ)
- Sim slug: medhavy-vol4-decoherence-t2
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-decoherence-t2/medhavy-vol4-decoherence-t2-review.mp4`

---

## Sim-03 — Quantum Gates: Hadamard and Phase on the Bloch Sphere
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: H = (X+Z)/√2 maps |0⟩→|+⟩ (rotation by π about x+z axis); S gate adds phase e^(iπ/2) to |1⟩ (rotation by π/2 about z)
- Concrete numbers: |0⟩ at north pole; H → |+⟩ at equator (φ=0); then S → |i⟩ = (|0⟩+i|1⟩)/√2 at equator (φ=π/2); position shifts 90° on Bloch sphere
- Visual artifact: Bloch sphere; vector animates from north pole to equator (H gate) then rotates 90° in-plane (S gate); label each gate
- Two testable predictions: P1: H∘H = I (applying Hadamard twice returns to |0⟩); P2: S gate maps |+⟩=(|0⟩+|1⟩)/√2 to |i⟩=(|0⟩+i|1⟩)/√2 (equatorial 90° rotation)
- Sim slug: medhavy-vol4-gate-bloch
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-gate-bloch/medhavy-vol4-gate-bloch-review.mp4`
