# Chapter 7 — Measurement, Interpretations, and the Quantum–Classical Boundary

In 1935, Erwin Schrödinger described a thought experiment involving a cat sealed in a steel chamber with a radioactive atom, a Geiger counter, a relay, a hammer, and a flask of prussic acid. If the atom decays in one hour, the counter fires, the hammer falls, the flask breaks, and the cat dies. Because the atom is in a superposition, the quantum formalism — applied without restriction — predicts that the cat is also in a superposition: $\tfrac{1}{\sqrt{2}}(|\text{live}\rangle + |\text{dead}\rangle)$.

Schrödinger introduced this example not as a feature of quantum mechanics but as a challenge to it — a demonstration that applying the superposition principle to macroscopic objects produces a description that conflicts with experience. Ninety years later, the formalism works with extraordinary precision. What it means, what happens during measurement, and which of the coherent responses to this challenge is correct remain open questions.

This chapter maps the logical space. It presents the problem precisely, describes each major interpretation, and summarizes the experimental evidence that constrains them.

---

## The Two Rules and the Tension Between Them

Quantum mechanics rests on two dynamical postulates.

**Rule 1 — Unitary evolution.** Between measurements, the state vector evolves under the Schrödinger equation: $|\psi(t)\rangle = \hat U(t)|\psi(0)\rangle$, where $\hat U = e^{-i\hat H t/\hbar}$ is unitary. This evolution is linear, deterministic, reversible, and preserves superpositions. A superposition in is a superposition out.

**Rule 2 — The projection postulate.** Upon measurement of observable $\hat O$ with eigenstates $|o_i\rangle$, if the system is in state $|\psi\rangle = \sum_i c_i|o_i\rangle$, then the outcome $o_i$ occurs with probability $|c_i|^2$ and the state collapses to $|o_i\rangle$.

The second rule is not derivable from the first. When Rule 1 is applied to a measurement — treating the apparatus as a quantum system — the result is a growing superposition. Rule 2 says superpositions are eliminated at measurement. The tension is this: **unitary evolution never eliminates superpositions; the projection postulate says they are eliminated at measurement; no principle specifies when "measurement" begins.**

This is not a problem of ignorance. The formalism predicts a definite entangled superposition; experience delivers a single outcome. Explaining that gap without adding hidden assumptions is what each interpretation attempts. [contested]

---

## The Von Neumann Measurement Chain

John von Neumann formalized this in 1932. Let the system $S$ be in a superposition:

$$|\psi\rangle_S = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1.$$

The apparatus $A$ starts in a ready state $|R\rangle$. A measurement interaction correlates apparatus pointer states with system eigenstates:

$$(\alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle)|R\rangle \overset{\hat U_\text{meas}}{\longrightarrow} \alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle.$$

This is von Neumann's *pre-measurement*: the apparatus has become entangled with the system. The result is not a single outcome — it is a superposition of "system up, apparatus up" and "system down, apparatus down."

Applying unitary evolution further, the apparatus couples to the environment $E$:

$$\alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle \;\to\; \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle.$$

Including the observer, both observer states $|O_\text{"up"}\rangle$ and $|O_\text{"down"}\rangle$ appear as terms in the growing superposition. At no step does unitary evolution produce a single outcome. Von Neumann identified the *Schnitt* (cut): somewhere in this chain, the quantum description ends and the classical description begins. He gave no physical criterion for where the cut is. That is the gap each interpretation fills differently.

---

## What Decoherence Explains — and What It Does Not

Decoherence provides an important partial solution to the measurement problem. Here is what it achieves.

When the system couples to an environment with many degrees of freedom, the off-diagonal elements of the system's reduced density matrix decay exponentially fast. In the *pointer basis* — the basis selected by the structure of the system-environment coupling — the density matrix becomes approximately diagonal:

$$\hat\rho_S \approx |\alpha|^2|\!\uparrow\rangle\langle\uparrow| + |\beta|^2|\!\downarrow\rangle\langle\downarrow|.$$

This resembles a classical probability distribution over definite outcomes. The off-diagonal interference terms have transferred into correlations with the environment. This is Zurek's **einselection**: the environment selects the preferred basis by monitoring the system in that basis. Macroscopic superpositions decohere on timescales of order $10^{-36}$ s for dust in air — which is why macroscopic superpositions are not observed.

Decoherence addresses the **basis problem**: it explains which basis collapse appears to occur in, and why macroscopic superpositions in arbitrary quantum states are not observed.

Decoherence does **not** solve the **outcome problem**: even after decoherence, both diagonal terms $|\alpha|^2$ and $|\beta|^2$ are present. The density matrix contains two mutually exclusive possibilities, each with nonzero weight. A single run yields one — not both, and not their weighted average. The Born-rule probabilities are presupposed in the interpretation of the density matrix; they are not derived from it. The question "why this outcome and not that one?" is not answered by observing off-diagonal elements decay.

This distinction — decoherence addresses the basis problem but not the outcome problem — is the central logical point of this chapter.

---

## The Interpretations

Each interpretation below is a different response to the outcome problem.

---

**Copenhagen** (Bohr, Heisenberg, Born; 1920s–1940s)

The wave function is a calculational tool for predicting measurement outcomes, not a description of reality. There is a fundamental divide between the quantum domain (the microscopic system) and the classical domain (the apparatus and observer). Collapse is not a physical event — it is the updating of the quantum description as information passes into the classical domain.

The classical-quantum boundary is taken as a primitive, not derived from the formalism. Bohr held that demanding a deeper account is a category error; quantum mechanics is a description of our experimental interactions with nature, not a picture of nature itself.

John Bell's 1990 essay "Against 'Measurement'" argues that "measurement" and "observation" are too imprecise to serve as primitive terms in a fundamental physical theory. [contested]

*Experimental distinguishability:* None. Copenhagen makes identical predictions to standard QM by construction.

---

**Many-worlds** (Everett, 1957; developed by DeWitt, Wallace, Deutsch)

The state vector is real; unitary evolution is universal and never interrupted. Measurement does not collapse the wave function — it entangles the observer with the system. All branches of the superposition are equally real. Both "O reads up" and "O reads down" branches exist with definite observer experiences; neither is special.

The Born rule problem [contested]: if all branches exist with equal ontological status, what do $\alpha$ and $\beta$ mean? Deutsch (1999) and Wallace (2010, 2012) give a decision-theoretic derivation: a rational agent facing branching should assign betting odds consistent with the Born rule weights. Critics dispute whether the derivation is circular. As of 2026, the Born rule derivation in many-worlds is not settled. [contested]

*Experimental distinguishability:* None. Identical predictions to standard QM.

---

**Bohmian mechanics / pilot-wave theory** (de Broglie 1927; Bohm 1952)

Particles have definite positions at all times. The wave function $\psi$ is a real physical field (the "pilot wave") that guides particle trajectories via the guiding equation:

$$\frac{d\mathbf{x}_k}{dt} = \frac{\hbar}{m_k}\,\text{Im}\!\left(\frac{\nabla_k\psi}{\psi}\right).$$

The Schrödinger equation is unmodified — no collapse. The apparent collapse is explained by the particle's actual position selecting one branch; the other branch becomes an "empty wave" that carries no particle. The Born rule follows from the assumption of *quantum equilibrium*: initial positions distributed as $|\psi_0|^2$.

Bohmian mechanics is explicitly nonlocal (Bell's theorem requires this of any hidden-variable theory reproducing quantum predictions), but the nonlocality cannot be exploited for signaling.

*Experimental distinguishability:* None in the non-relativistic regime.

---

**Objective-collapse models: GRW and CSL** (Ghirardi, Rimini, Weber 1986; Pearle 1989)

This is the only class that functions as a genuine *alternative theory*, not just a reinterpretation.

**GRW:** The Schrödinger equation is modified by spontaneous random localization events. Each particle undergoes a "hit" — a sudden collapse to a Gaussian of width $r_C \approx 10^{-7}$ m — at rate $\lambda \approx 10^{-17}$ $\text{s}^{-1}$. For a single particle, hits are negligibly rare (one per $\sim 10^9$ years). For $N \sim 10^{23}$ particles, the rate scales as $N\lambda \sim 10^6$ $\text{s}^{-1}$ — nearly instantaneous. Macroscopic superpositions collapse in microseconds; microscopic superpositions survive.

**CSL** (Continuous Spontaneous Localization): a continuous stochastic generalization with two free parameters, the collapse rate $\lambda$ and the correlation length $r_C$.

Because CSL modifies the Schrödinger equation, it predicts deviations from standard QM: anomalous heating of massive objects from collapse-induced position diffusion, and loss of interference fringe visibility in large-molecule experiments. Current experimental constraints:

- **LISA Pathfinder** (femtometer-scale position noise of a gram-scale test mass) excludes large portions of the CSL parameter space at high $\lambda$.
- **Optomechanical experiments** with levitated nanospheres constrain collapse-induced diffusion from below.
- **Molecular interferometry** (Arndt group, Vienna) sets upper bounds — if collapse rates were fast enough, interference would vanish.

Current status (2026): The original GRW parameters survive; the Adler parameters ($\lambda \sim 10^{-8}$ $\text{s}^{-1}$) are under pressure. The allowed parameter space is shrinking. This is a live experimental program. [contested]

*Experimental distinguishability:* **Yes** — the only class with distinct testable predictions.

---

**QBism** (Caves, Fuchs, Schack; early 2000s)

Quantum mechanics is a normative framework for an agent to organize probabilistic beliefs about future experiences. The wave function is the agent's probability assignment — personal and agent-relative. Collapse is not a physical event; it is belief updating upon having an experience (Bayesian conditioning). Every quantum state assignment is relative to the agent who holds it.

The Born rule in QBism is reformulated as a normative constraint on coherent belief-updating, using a reference measurement (SIC-POVM). This removes the Born rule from the status of a physical postulate.

*Experimental distinguishability:* None.

---

**Consistent histories** (Griffiths 1984; Omnès 1988; Gell-Mann and Hartle 1990)

Probabilities are assigned to *histories* — sequences of events at successive times — rather than states at an instant. A set of histories is *consistent* if the density matrix has negligible off-diagonal elements between different histories in the set. Within a consistent set, classical probability rules apply. Different consistent sets represent different "frameworks."

The single-framework rule: two different consistent frameworks cannot be combined in a single description — analogous to Bohr's complementarity. No external observer or classical domain is required, making the framework natural for quantum cosmology.

*Experimental distinguishability:* None.

---

**Relational quantum mechanics** (Rovelli, 1996) — brief note

Physical quantities have values only *relative* to other physical systems. Quantum states describe the information that one system has about another. This is distinct from QBism (which centers on agents with experiences) and from consistent histories, though all three share an anti-realist stance toward the quantum state.

The **Frauchiger-Renner** thought experiment (2018, *Nature Communications* 9:3711) sharpened the debate: two super-observers measure quantum states of lower-level observers who have themselves measured quantum systems. Frauchiger and Renner show that three plausible-seeming assumptions — universal applicability of quantum mechanics, agents can use each other's descriptions, measurements have unique outcomes — cannot all be simultaneously maintained. Which assumption to drop is a matter of active dispute; QBism, many-worlds, and relational QM each respond differently. [contested]

---

## Interpretations at a Glance

| Interpretation | Wave function status | Cut location | Outcome mechanism | Distinct predictions? |
|---|---|---|---|---|
| Copenhagen | Tool | Classical/quantum boundary (pragmatic) | Postulated | No |
| Many-worlds | Real; universal | No cut | All outcomes occur in branches | No |
| Bohmian | Real; guides particles | No cut for $\psi$ | Deterministic trajectory | No (non-relativistic) |
| GRW/CSL | Real; modified dynamics | Physical collapse event | Stochastic mechanism | **Yes** |
| QBism | Agent's beliefs | Agent's experience | Belief update | No |
| Consistent histories | Framework-dependent | Framework choice | Probability in chosen set | No |
| Relational QM | Relational | Interaction between systems | Relational update | No |

---

## Worked Example — Tracing the Von Neumann Chain

We take the spin-½ particle $|\psi\rangle_S = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$ and trace through the chain.

**Step 1 — Pre-measurement** (uncontroversial for all interpretations):

$$|\Psi_1\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle.$$

This is a superposition, not a single outcome.

**Step 2 — Environment entanglement:**

$$|\Psi_2\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle.$$

The reduced density matrix of system+apparatus, obtained by tracing over $E$:

$$\hat\rho_{SA} \approx |\alpha|^2|\!\uparrow\rangle\langle\uparrow|\otimes|A_\uparrow\rangle\langle A_\uparrow| + |\beta|^2|\!\downarrow\rangle\langle\downarrow|\otimes|A_\downarrow\rangle\langle A_\downarrow|$$

because $\langle E_\uparrow|E_\downarrow\rangle \to 0$ exponentially (the environment has recorded which branch occurred). Decoherence has done its work. Both diagonal terms are still nonzero — no outcome has been selected.

**Step 3 — Observer:**

$$|\Psi_3\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle|O_\text{"up"}\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle|O_\text{"down"}\rangle.$$

Where each interpretation places its cut:

**Copenhagen** places the cut between the quantum system and the apparatus, or wherever convenient. Steps 1–2 are quantum. The outcome is a classical fact not described by the quantum formalism at all.

**Many-worlds** places no cut. $|\Psi_3\rangle$ is the complete physical description. Both branch-observers have definite experiences; neither is special.

**Bohmian mechanics** has no cut for $\psi$ — it evolves unitarily. The particle has a definite position determined by its trajectory and the guiding equation. That position is the outcome. The other branch of $|\Psi_3\rangle$ is an empty wave — real, but carrying no particle.

**GRW/CSL** inserts a stochastic physical collapse event at Step 2 or 3. For a macroscopic apparatus with $\sim 10^{23}$ particles, $N\lambda \sim 10^6$ $\text{s}^{-1}$: the superposition terminates essentially instantaneously. The surviving branch is selected randomly with probabilities $|\alpha|^2$ and $|\beta|^2$.

**QBism** has no physical collapse event. The chain is the agent's model of the world. Upon having the experience of seeing an outcome, the agent updates their state assignment. $|\Psi_3\rangle$ was never a description of the physical world — it was the agent's probability assignment tool.

**Consistent histories** replaces the cut with a framework choice. In the history set containing "apparatus reads up" and "apparatus reads down" as distinct, decohered histories, each receives probability $|\alpha|^2$ or $|\beta|^2$, and classical reasoning applies within that framework.

---

## Open Questions

The measurement problem is genuinely open. A 2025 review (arXiv:2502.19278) surveyed all major interpretations and declined to declare a winner — not for lack of effort but because the problem remains logically unresolved. A 2013 survey of 33 physicists at a foundations conference (Schlosshauer, Kofler, Zeilinger, *Am. J. Phys.* 81:325) found Copenhagen-adjacent 42%, many-worlds 18%, information-theoretic 24%, other/none 16%.

Objective-collapse models are the only class where experiment can help: the allowed parameter space is being constrained from multiple directions simultaneously. Whether GRW/CSL will be ruled out or survive as viable alternatives to standard QM is a question that ongoing precision measurements are working to resolve.

The formalism of quantum mechanics is among the most precisely verified theories in the history of science — predictions confirmed to parts per billion in some cases. What the formalism means, what happens in a measurement, and whether the wave function represents something real are not agreed upon. The physics and the metaphysics have separated; both are serious ongoing endeavors.

---

## References

- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (English: Princeton, 1955.)
- Everett, H., III (1957). "Relative state" formulation of quantum mechanics. *Reviews of Modern Physics*, 29, 454.
- Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of "hidden" variables, I and II. *Physical Review*, 85, 166 and 180.
- Ghirardi, G.C., Rimini, A. and Weber, T. (1986). Unified dynamics for microscopic and macroscopic systems. *Physical Review D*, 34, 470.
- Pearle, P. (1989). Combining stochastic dynamical state-vector reduction with spontaneous localization. *Physical Review A*, 39, 2277.
- Schlosshauer, M. (2003). Decoherence, the measurement problem, and interpretations of quantum mechanics. *Reviews of Modern Physics*, 76, 1267.
- Bassi, A. et al. (2013). Models of wave-function collapse, underlying theories, and experimental tests. *Reviews of Modern Physics*, 85, 471.
- Carlesso, M. et al. (2016). Experimental bounds on collapse models from gravitational wave detectors. arXiv:1606.04581. [verify]
- Deutsch, D. (1999). Quantum theory of probability and decisions. *Proceedings of the Royal Society A*, 455, 3129.
- Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press.
- Fuchs, C.A., Mermin, N.D. and Schack, R. (2014). An introduction to QBism. *American Journal of Physics*, 82, 749.
- Frauchiger, D. and Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. *Nature Communications*, 9, 3711.
- Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75, 715.
- Bell, J.S. (1990). Against "measurement." *Physics World*, 3(8), 33.
- Schlosshauer, M., Kofler, J. and Zeilinger, A. (2013). A snapshot of foundational attitudes toward quantum mechanics. *American Journal of Physics*, 81, 325.
- Rovelli, C. (1996). Relational quantum mechanics. *International Journal of Theoretical Physics*, 35, 1637. [verify]
- arXiv:2502.19278 (2025). The quantum measurement problem: A review. [verify]

---

*Chapter 8 follows: quantum information beyond qubits — continuous-variable quantum systems, Gaussian states, and the quantum teleportation of a continuous variable. The measurement problem resurfaces in a new form: the role of homodyne detection in collapsing a Gaussian state.*

