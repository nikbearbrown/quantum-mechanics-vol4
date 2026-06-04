# Chapter 7 — Measurement, Interpretations, and the Quantum–Classical Boundary

## TL;DR

- Quantum mechanics has two dynamical rules — unitary evolution and the projection postulate — that are logically incompatible when both the system and the measuring apparatus are quantum.
- Decoherence explains the *appearance* of classicality and selects the preferred basis; it does not explain why one particular outcome obtains.
- At least six interpretations respond to this gap: Copenhagen, many-worlds, Bohmian mechanics, objective-collapse (GRW/CSL), QBism, and consistent histories — with a mention of relational QM. None is experimentally preferred except for objective-collapse models, which make distinct testable predictions.
- Objective-collapse models (GRW, CSL) are the only class that functions as an *alternative theory*, not merely an interpretation; they are currently under experimental pressure from LISA Pathfinder, optomechanics, and molecular interferometry.
- The measurement problem remains open as of 2026.

---

## Learning objectives

By the end of this chapter you should be able to:

1. **State** the measurement problem precisely — identify the two dynamical rules and the logical incompatibility that arises when both are applied to a quantum measurement apparatus. *(Remember/Understand)*

2. **Trace** the von Neumann measurement chain step by step and identify where each major interpretation places its "cut." *(Understand/Apply)*

3. **Distinguish** what decoherence explains (the preferred basis, the appearance of classicality) from what it does not explain (the outcome problem). *(Analyze)*

4. **Compare** the major interpretations on at least three axes: ontological status of the wave function, mechanism for selecting one outcome, and experimental distinguishability from standard quantum mechanics. *(Analyze/Evaluate)*

5. **Assess** the experimental status of objective-collapse models, citing the type of experiment that constrains them and the direction of current pressure on the CSL parameter space. *(Evaluate)*

---

## Scene opening

It is 1935 and Erwin Schrödinger has written a letter. He has just finished reading Einstein, Podolsky, and Rosen's paper, and he is not satisfied — not with EPR's conclusion, but with quantum mechanics itself. He invites you to imagine a cat sealed in a steel chamber with a radioactive atom, a Geiger counter, a relay, a hammer, and a flask of prussic acid. If the atom decays in one hour, the counter fires, the hammer falls, the flask breaks, the cat dies. The atom is in a superposition. Therefore, Schrödinger writes — following the formalism precisely — the cat is also in a superposition: $\tfrac{1}{\sqrt{2}}(|\text{live}\rangle + |\text{dead}\rangle)$.

The cat is neither dead nor alive. Both. Until someone opens the box.

Schrödinger was not proposing this as a feature. He was exposing it as an absurdity — a *reductio ad absurdum* of applying the quantum superposition principle without restriction to macroscopic objects. Ninety years later, the problem he identified has not been solved. The formalism works with extraordinary precision. What it means, what happens in the moment of measurement, which of the several logically coherent responses to Schrödinger's challenge is correct — these remain open.

This chapter maps the logical space. It will not declare a winner. What it will do is give you a precise statement of the problem, a concrete procedure for comparing interpretations, and enough experimental context to know which interpretations have already been cornered by data.

---

## Core development

### The two rules and the tension between them

Quantum mechanics rests on two dynamical postulates that are not obviously compatible.

**Rule 1 — Unitary evolution.** Between measurements, the state vector $|\psi(t)\rangle$ evolves under the Schrödinger equation:

$$i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle \implies |\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle.$$

The evolution operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ is unitary. Unitary evolution is linear, deterministic, reversible, and — crucially — it *preserves superpositions*. A superposition in is a superposition out.

**Rule 2 — The projection postulate (Born rule).** Upon measurement of an observable $\hat{O}$ with eigenvalues $o_i$ and orthonormal eigenstates $|o_i\rangle$, if the system is in state $|\psi\rangle = \sum_i c_i|o_i\rangle$, then:
- The outcome $o_i$ occurs with probability $|c_i|^2$.
- Immediately after, the state *collapses* to $|o_i\rangle$.

The second rule is not derivable from the first. It is an additional postulate. And when you try to apply the first rule to a measurement — treating the apparatus as a quantum system too — you get something the second rule cannot be simply grafted onto.

Here is the problem stated in one line: **unitary evolution never eliminates superpositions; the projection postulate says they are eliminated at measurement; no principle specifies when "measurement" begins.**

This is the measurement problem [contested]. Note that the problem is not about our ignorance. It is not resolved by claiming we do not know which outcome occurred. The formalism predicts a definite entangled superposition; experience delivers a definite single outcome. Explaining that gap — without adding hidden assumptions — is what the interpretations attempt.

### The von Neumann measurement chain

John von Neumann formalized this in his 1932 treatise. Let the system $S$ be in a superposition of two spin states:

$$|\psi\rangle_S = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1.$$

The measuring apparatus $A$ begins in a ready state $|R\rangle$. The system and apparatus interact via the Schrödinger equation. A good measurement interaction correlates apparatus pointer states with system eigenstates:

$$\bigl(\alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle\bigr)|R\rangle \xrightarrow{\hat{U}_{\text{meas}}} \alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle.$$

This is von Neumann's *pre-measurement*: the apparatus has become correlated (entangled) with the system. The result is not a definite outcome. It is a superposition of "system up, apparatus pointing up" and "system down, apparatus pointing down."

Apply unitary evolution further. The apparatus and the environment $E$ interact:

$$\alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_0\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_0\rangle \xrightarrow{\hat{U}_{\text{env}}} \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle.$$

The environment is now entangled with the apparatus-system pair. The chain can be continued to include the observer, and beyond:

$$\cdots \to \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle|O_{\text{"up"}}\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle|O_{\text{"down"}}\rangle.$$

At no step does the unitary evolution produce a single outcome. The superposition propagates up the chain. Von Neumann identified the *Schnitt* (cut): somewhere in this chain, the quantum description ends and the classical description begins. But he gave no physical criterion for where the cut is located. That is the lacuna every interpretation fills differently.

### What decoherence explains — and what it does not

Decoherence (Chapter 6) provides the most important partial solution to the measurement problem. Here is what it achieves.

When the system couples to an environment with many degrees of freedom, the off-diagonal elements of the system's reduced density matrix — $\langle\uparrow|\hat{\rho}_S|\downarrow\rangle$ and its conjugate — decay exponentially fast. In the *pointer basis* (the basis selected by the structure of the system-environment coupling Hamiltonian $\hat{H}_{SE}$), the density matrix becomes approximately diagonal:

$$\hat{\rho}_S \approx |\alpha|^2|\!\uparrow\rangle\langle\uparrow| + |\beta|^2|\!\downarrow\rangle\langle\downarrow|.$$

This looks like a classical probability distribution over definite outcomes. The off-diagonal interference terms have vanished into correlations with the environment. This is **Zurek's einselection** (environment-induced superselection): the environment *selects* the preferred basis by monitoring the system in that basis [verify]. Macroscopic superpositions decohere in times of order $10^{-36}$ s for dust in air — which is why we never see live-and-dead cats.

Decoherence solves the **basis problem**: it explains which basis collapse appears to occur in (the pointer basis, fixed by the coupling to the environment), and why we never observe macroscopic superpositions in position eigenstates.

Decoherence does **not** solve the **outcome problem**: even after decoherence, both diagonal terms $|\alpha|^2$ and $|\beta|^2$ are present. The density matrix represents two mutually exclusive possibilities, each with nonzero weight. A single experimental run yields one of them — not a weighted average. The Born-rule probabilities are *presupposed* in the interpretation of the density matrix; they are not derived from decoherence. The question "why this outcome and not that one?" is not answered by watching the off-diagonal elements decay.

This distinction — decoherence addresses the basis problem but not the outcome problem — is the single most important logical point in this chapter.

### The interpretations

Each interpretation below is a different response to the outcome problem. The presentation order is roughly chronological; the order carries no endorsement.

---

**Copenhagen interpretation** (Bohr, Heisenberg, Born; 1920s–1940s)

The wave function is not a description of reality but a calculational tool for predicting measurement outcomes. There is a fundamental divide between the quantum domain (the microscopic system) and the classical domain (the apparatus, the observer, the macroscopic world). The collapse is not a physical event; it is the updating of the quantum description as information passes into the classical domain.

Measurement has a special status in Copenhagen because the *classical-quantum boundary is treated as a primitive* — it is not derived from the formalism. Where exactly the cut is: wherever it is convenient for the calculation. Bohr was explicit that demanding a deeper account is a category error; quantum mechanics is a description of our experimental interactions with nature, not a picture of nature itself.

*Von Neumann chain placement:* Copenhagen places the cut pragmatically — somewhere between the quantum system and the macroscopic world — without specifying the physical criterion.

*Advantages:* Self-consistent; matches standard practice; requires no additional ontology.

*Disadvantages:* The cut is never defined precisely. Why is a 10-nanometer molecule quantum and a 1-gram apparatus classical? The criterion is vague by design. John Bell, in his 1990 essay "Against 'Measurement'," argued that "measurement" and "observation" are too imprecise to serve as primitive terms in a fundamental physical theory. Bell's critique is among the sharpest ever mounted against Copenhagen — and remains unanswered in the sense that no proponent has defined the cut precisely [contested].

*Experimental distinguishability:* None. Copenhagen makes identical predictions to standard QM by construction.

---

**Many-worlds interpretation** (Everett, 1957; developed by DeWitt, Wheeler, Wallace, Deutsch)

The state vector is real; unitary evolution is universal and never interrupted. Measurement does not collapse the wave function — it entangles the observer with the system. All branches of the superposition are equally real. After measurement, the universe is in a superposition:

$$\alpha|\!\uparrow\rangle|A_\uparrow\rangle|O_{\text{"up"}}\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|O_{\text{"down"}}\rangle$$

and both terms describe real branches, each containing a copy of the observer with a definite experience.

*Von Neumann chain placement:* No cut. The chain is never terminated; all terms in the superposition are always real.

*The Born rule problem* [contested]: If all branches exist with equal ontological status, what do the coefficients $\alpha$ and $\beta$ mean? Why does the Born rule weight $|\alpha|^2$ give the probability of experiencing the "up" branch? David Deutsch (1999) and David Wallace (2010, 2012) give a decision-theoretic derivation: a rational agent who is about to undergo branching should assign betting odds consistent with the Born rule weights. The derivation is technically sophisticated. Critics — including Hilary Greaves and Wayne Myrvold, with philosophical arguments, and Adrian Kent, with more formal objections — dispute whether the derivation is circular, because the notion of "rational" may already encode the Born rule. As of 2026, the Born rule derivation in many-worlds is not settled [contested].

*Advantages:* No additional ontology beyond the standard formalism. No measurement axiom. No preferred basis (decoherence selects the branch structure dynamically).

*Disadvantages:* An extraordinary proliferation of unobservable branches. The Born rule problem. The notion of "branch" requires a pointer basis — which brings in decoherence, and the argument about whether this makes the formulation self-referential is ongoing.

*Experimental distinguishability:* None; makes identical predictions to standard QM.

---

**Bohmian mechanics / pilot-wave theory** (de Broglie 1927; Bohm 1952)

Particles have definite positions at all times — even when unobserved. The wave function $\psi$ is a real physical field (the "pilot wave") that guides particle trajectories through the guiding equation:

$$\frac{d\mathbf{x}_k}{dt} = \frac{\hbar}{m_k}\,\text{Im}\!\left(\frac{\nabla_k\psi}{\psi}\right) = \frac{\mathbf{j}_k}{\rho}.$$

The Schrödinger equation governs $\psi$ without modification — no collapse. The apparent collapse is explained by the particle's actual position selecting one branch of the wave function; the other branches become "empty waves" that carry no particle and produce no outcomes.

The Born rule is not a postulate: it follows from the assumption of *quantum equilibrium* — that the initial particle positions are distributed according to $|\psi_0|^2$. Given this initial condition, all Born-rule statistics are reproduced for all future measurements.

*Von Neumann chain placement:* No cut for the wave function — it evolves unitarily always. The "outcome" is determined by the particle's position at the moment of interaction with the apparatus.

*Nonlocality:* Bell's theorem showed that any hidden-variable theory reproducing quantum predictions must be nonlocal. Bohmian mechanics is explicitly nonlocal: the guiding equation depends on the full $N$-particle wave function in configuration space ($3N$ dimensions), so one particle's velocity depends on the instantaneous configuration of all other particles. This nonlocality is not exploitable for signaling — because of quantum equilibrium, Bob cannot use it to send messages to Alice — but it is a genuine structural feature of the theory.

*Advantages:* Deterministic. Particles have definite positions. Born rule derivable. No measurement axiom.

*Disadvantages:* Explicit nonlocality. Extension to relativistic quantum field theory is contested and technically difficult. The wave function lives in configuration space, not physical space — for $N$ particles it has $3N$ dimensions. "Empty waves" carry no particles and produce no observational consequences, which some physicists find troubling as excess ontology.

*Experimental distinguishability:* None in the non-relativistic regime. Predictions are identical to standard QM.

---

**Objective-collapse models: GRW and CSL** (Ghirardi, Rimini, Weber 1986; Pearle 1989; Ghirardi, Pearle, Rimini 1990)

This is the only class of interpretations that functions as a genuine *alternative theory*, not just a reinterpretation of standard QM.

**GRW model:** The Schrödinger equation is modified by adding spontaneous, random localization events. Each particle undergoes a "hit" — a sudden collapse to a Gaussian of width $r_C \approx 10^{-7}$ m (100 nm) centered on a randomly chosen position — at a rate $\lambda \approx 10^{-17}$ s$^{-1}$. For a single particle, hits are negligibly rare (one per $10^{17}$ s $\approx 3 \times 10^9$ yr). For a macroscopic object with $N \sim 10^{23}$ particles, the rate scales as $N\lambda \sim 10^6$ s$^{-1}$ — extremely fast. Macroscopic superpositions collapse in microseconds; microscopic superpositions survive.

**CSL (Continuous Spontaneous Localization):** A continuous stochastic generalization that handles identical particles correctly, driven by a noise field. Two free parameters: the collapse rate $\lambda$ and the correlation length $r_C$.

*Von Neumann chain placement:* The chain is terminated by a physical process — a stochastic collapse event — at the apparatus/environment level (step 2 or 3 in the chain). The cut is not a postulate about observers or knowledge; it is a new physical mechanism.

*Experimental constraints:* Because CSL modifies the Schrödinger equation, it predicts deviations from standard QM that are in principle detectable:

- **Mechanical diffusion:** CSL adds a random force to every massive object. This heats macroscopic systems and adds noise to precision mechanical experiments. LISA Pathfinder, which was designed to test gravitational wave detection technology, measured the position noise of a test mass at the femtometer scale. Helou et al. (2017) and Carlesso et al. (2016, arXiv:1606.04581) used LISA Pathfinder data to exclude significant portions of the CSL parameter space at high $\lambda$ and small $r_C$.
- **Optomechanical experiments:** Levitated nanospheres and optomechanical cantilevers constrain the collapse-induced diffusion from below.
- **Molecular interferometry:** Large-molecule double-slit experiments (Arndt group, Vienna) set upper bounds — if the collapse rate were fast enough, interference would disappear. These set upper limits on $\lambda$.
- **GW detectors (LIGO, AURIGA):** Also provide mechanical noise constraints.

Current status (2026): The original GRW parameters ($\lambda_{\text{GRW}} \approx 10^{-17}$ s$^{-1}$, $r_C = 10^{-7}$ m) survive current constraints. The Adler parameters ($\lambda_{\text{Adler}} \sim 10^{-8}$ s$^{-1}$) are under pressure from non-interferometric experiments. The models have not been ruled out, but the allowed parameter space is shrinking. This is a live experimental program [contested].

*Advantages:* Solves both the basis problem and the outcome problem. Makes distinct predictions that distinguish it from standard QM. No reference to observers or knowledge.

*Disadvantages:* Introduces new parameters ($\lambda$, $r_C$) without derivation from deeper principles. Relativistic extensions are technically difficult and have energy-conservation problems. The specific parameter values have no fundamental justification.

---

**QBism** (Caves, Fuchs, Schack; early 2000s; developed by Fuchs, Mermin, Schack)

Quantum mechanics is a normative framework for an agent to organize probabilistic beliefs about future experiences. The wave function is not an element of reality; it is the agent's *probability assignment* — a personal, agent-relative object. Wave function collapse is not a physical event; it is the agent's belief updating upon having an experience (Bayesian conditioning).

"When an agent uses quantum mechanics to calculate the probability of a future experience and then has that experience, the agent updates their probability assignment. This is exactly what happens when a Bayesian reasoner updates on new evidence." (Fuchs, Mermin, Schack 2014)

*Von Neumann chain placement:* The chain ends at the agent's experience. Everything else — system, apparatus, environment — is the world the agent is reasoning about. The quantum state assignment is relative to the agent.

The Born rule in QBism is reformulated as a normative constraint on coherent belief-updating, using a reference measurement (a symmetric informationally complete POVM, or SIC-POVM). This removes the Born rule from the status of a physical postulate and makes it a condition on rational agency. The detailed development of this reformulation is one of QBism's active research programs.

*Advantages:* No collapse problem. No preferred basis problem (basis depends on the agent's choice of measurement). No nonlocality paradoxes — state assignments are agent-local. Consistent with Wigner's friend scenarios (each agent has their own state assignment; they can differ without contradiction).

*Disadvantages:* Science is typically realist. QBism's agent-centrism is philosophically non-standard, and it is genuinely unclear what QBism says, if anything, about the physical world as distinct from agents' experiences of it. Critics charge that QBism dissolves the measurement problem rather than solving it. Mermin's version ("participatory realism") differs in emphasis from Fuchs's; the movement is not monolithic.

*Experimental distinguishability:* None. QBism makes identical predictions to standard QM.

---

**Consistent (decoherent) histories** (Griffiths 1984; Omnès 1988; Gell-Mann and Hartle 1990)

Probabilities are assigned to *histories* — sequences of events at successive times — rather than to states at an instant. A set of histories is *consistent* (or *decoherent*) if the density matrix of the full set has negligible off-diagonal elements between different histories in the set (the consistency condition). Within a consistent set, classical probability rules apply. Different consistent sets represent different "frameworks" for describing the world.

*Von Neumann chain placement:* No cut is needed as a primitive. The choice of a consistent history set replaces the cut; within a chosen framework, outcomes can be assigned probabilities. No external observer or classical domain is required.

*The single-framework rule:* Two different consistent frameworks cannot be combined in a single description. This is analogous to Bohr's complementarity — you can describe position or momentum, but not both simultaneously; here, you can use one consistent history set or another, but not both.

*Advantages:* Consistent with closed-system quantum mechanics. No need for a classical domain. Natural for quantum cosmology (Gell-Mann and Hartle applied consistent histories to the universe as a whole).

*Disadvantages:* The formalism does not select which consistent set is the "real" one — there are many, and they give different descriptions. Critics argue that this reintroduces the measurement problem under different vocabulary. The connection to many-worlds is debated (Griffiths argues they are distinct; others see consistent histories as a reformulation of relative-state). Pedagogically more abstract than other approaches.

*Experimental distinguishability:* None.

---

**Relational quantum mechanics** (Rovelli 1996; developed further since) — a brief note

Rovelli's proposal: physical quantities are not absolute but relational — they have values only *relative* to other physical systems. Quantum states describe the information that one system has about another. Collapse is the updating of a system's description relative to a new interaction. This is distinct from QBism (which centers on agents with experiences) and from consistent histories (which centers on probability assignments to sequences of events), though all three share an anti-realist stance toward the quantum state.

The Frauchiger–Renner thought experiment (2018, *Nature Communications* 9:3711) sharpened the debate about all interpretations that treat observers themselves as subject to quantum superposition. Frauchiger and Renner construct a scenario in which two "super-observers" measure the quantum states of two lower-level observers, and show that self-consistent reasoning within certain interpretational assumptions leads to contradictions. The conclusion is not that quantum mechanics is wrong, but that at most one of a set of plausible-seeming assumptions can be maintained. QBism, many-worlds, and relational QM each respond to Frauchiger–Renner differently [contested].

---

### Where each interpretation places the cut: summary

| Interpretation | Wave function status | Cut location | Outcome mechanism | Distinct predictions? |
|---|---|---|---|---|
| Copenhagen | Tool, not real | Classical/quantum boundary (pragmatic) | Postulated | No |
| Many-worlds | Real; universal | No cut | All outcomes occur in separate branches | No |
| Bohmian | Real; guides particles | No cut for $\psi$; particle position selects outcome | Deterministic trajectory + quantum equilibrium | No (non-relativistic) |
| GRW/CSL | Real; modified dynamics | Physical collapse event (stochastic) | Collapse mechanism | **Yes** |
| QBism | Agent's beliefs | Agent's experience | Belief update | No |
| Consistent histories | Framework-dependent | Framework choice replaces cut | History probability in chosen set | No |
| Relational QM | Relational | Interaction between systems | Relational update | No |

---

## Worked example: tracing the von Neumann chain

**The lesson.** Consider a spin-1/2 particle in the state $|\psi\rangle_S = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$, measured by an apparatus that begins in state $|R\rangle_A$.

**Step 1 — Pre-measurement.** Under unitary evolution, system and apparatus entangle:

$$|\Psi_1\rangle = \alpha|\!\uparrow\rangle_S|A_\uparrow\rangle_A + \beta|\!\downarrow\rangle_S|A_\downarrow\rangle_A.$$

Result: a superposition. Not a single outcome. This step is uncontroversial — every interpretation agrees it is a valid application of Rule 1.

**Step 2 — Environment entanglement.** The apparatus couples to environmental degrees of freedom $|E_0\rangle$ (photons, phonons, air molecules):

$$|\Psi_2\rangle = \alpha|\!\uparrow\rangle_S|A_\uparrow\rangle_A|E_\uparrow\rangle_E + \beta|\!\downarrow\rangle_S|A_\downarrow\rangle_A|E_\downarrow\rangle_E.$$

**Decoherence acts here.** The reduced density matrix of the system+apparatus, obtained by tracing over $E$:

$$\hat{\rho}_{SA} = \text{Tr}_E(|\Psi_2\rangle\langle\Psi_2|) \approx |\alpha|^2|\!\uparrow\rangle\langle\uparrow|_S \otimes |A_\uparrow\rangle\langle A_\uparrow|_A + |\beta|^2|\!\downarrow\rangle\langle\downarrow|_S \otimes |A_\downarrow\rangle\langle A_\downarrow|_A$$

because $\langle E_\uparrow|E_\downarrow\rangle \to 0$ exponentially fast (the environment state records which branch occurred). The density matrix is now diagonal in the pointer basis — decoherence has done its work.

The appearance of a classical probability distribution is now explained. But $\hat{\rho}_{SA}$ still has two nonzero diagonal terms. Nothing in the mathematics has selected one of them.

**Step 3 — Observer.** Including the observer:

$$|\Psi_3\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle|O_{\text{"up"}}\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle|O_{\text{"down"}}\rangle.$$

**Where each interpretation places its cut:**

- **Copenhagen:** The cut is placed between the quantum system and the apparatus, or wherever convenient. Steps 1–2 are quantum. The outcome is a classical fact that is not described by the quantum formalism at all. The wave function is updated upon the outcome as a book-keeping device.

- **Many-worlds:** No cut is placed. $|\Psi_3\rangle$ is the complete physical description. The observer exists in both branches — "O reads up" and "O reads down" are both equally real. Each branch-observer has a definite experience; neither is special.

- **Bohmian mechanics:** The wave function $|\Psi_3\rangle$ evolves unitarily and is real. The particle has a definite position at all times. The apparatus pointer has a definite position determined by the particle's trajectory and the guiding equation. That position is the "outcome." The other branch of $|\Psi_3\rangle$ is an "empty wave" — physically real but carrying no particle.

- **GRW/CSL:** At step 2 or 3, a stochastic physical collapse event occurs. For a macroscopic apparatus with $\sim 10^{23}$ particles, the GRW rate $N\lambda \sim 10^6$ s$^{-1}$ terminates the superposition essentially instantaneously. The surviving branch — selected randomly with probabilities $|\alpha|^2$ and $|\beta|^2$ — is the physical outcome.

- **QBism:** The chain is the agent's model of the world. The "cut" is at the agent's experience. When the agent sees the outcome, they update their quantum state assignment. There is no physical collapse event; there is just the update. $|\Psi_3\rangle$ was never a description of the world — it was the agent's probability assignment tool.

- **Consistent histories:** The cut is replaced by a choice of consistent history set. In the history set that includes "apparatus reads up" and "apparatus reads down" as two distinct histories (and no interference between them, by the decoherence condition), each history receives a probability $|\alpha|^2$ or $|\beta|^2$ and classical reasoning applies.

**The limit.** What this example makes clear: decoherence (Step 2) is doing real explanatory work — it explains why we see a nearly-diagonal density matrix, not a coherent superposition of "apparatus-up + apparatus-down." What it does not do is select which diagonal term is actualized in a given experimental run. Every interpretation must address that gap, and each does so differently.

---

## Common misconceptions

**"Decoherence solves the measurement problem."**
The most common and most consequential mistake. Decoherence solves the *basis* problem: it explains why macroscopic objects appear to have definite pointer values rather than existing in arbitrary superpositions, and it selects the pointer basis dynamically from the physics of the system-environment coupling. It does not solve the *outcome* problem: the density matrix after decoherence is diagonal but still contains two nonzero terms. A single experimental run yields one outcome. Decoherence explains why the distribution looks classical; it does not explain why *this* outcome and not the other.

**"Copenhagen means 'shut up and calculate.'"**
"Shut up and calculate" is a phrase attributed (incorrectly) to Richard Feynman and (more plausibly) to David Mermin, who used it critically to describe a common but philosophically unsophisticated attitude. Copenhagen is a serious philosophical position: anti-realism about the quantum state, a fundamental classical/quantum cut, and a deliberate refusal to demand a picture of "what really happens." Bohr's writings are philosophically dense and not dismissive. Copenhagen is not sloppy — it is deliberately incomplete about the ontology, which is a philosophical stance, not an evasion.

**"Many-worlds is obviously crazy / obviously right."**
Many-worlds is taken seriously by a significant minority of professional physicists and philosophers of physics, receives detailed technical development (Wallace 2012, Saunders et al. 2010), and has a genuine unresolved technical problem — the Born rule derivation — that is the subject of ongoing serious work. Dismissing it as obviously implausible (too many unobservable branches) is the mirror of accepting it as obviously correct. Neither posture is warranted.

**"Bohmian mechanics was disproved."**
It was not. A widespread myth, sometimes traced to a misreading of von Neumann's 1932 no-hidden-variables theorem (which had a flaw identified by Grete Hermann in 1935 and made widely known by Bell in 1966). Bohmian mechanics is a complete, deterministic, empirically adequate theory that makes identical predictions to standard QM in all tested non-relativistic regimes. Its costs are explicit: nonlocality, and a wave function that lives in high-dimensional configuration space.

**"QBism says observers create reality."**
QBism holds that quantum states are agents' probability assignments, not elements of reality. This is a claim about the quantum *formalism*, not a claim that minds construct the physical world. Fuchs is careful to distinguish QBism from idealism. The world has structure; QBism is silent (deliberately) about what that structure is at the level not captured by agents' experiences.

**"Interpretations are just philosophy — physics doesn't care."**
False in at least one case: objective-collapse models (GRW, CSL) predict deviations from standard quantum mechanics at mesoscopic scales. They are physics in the standard sense — their parameters can be measured, and experiments are measuring them. The distinction between "interpretation" and "alternative theory" matters.

---

## Exercises

**1.** [Warm-up, *Remember/Understand*] State the measurement problem in two sentences, using the terms "unitary evolution," "projection postulate," and "superposition." Your statement should identify what happens when both rules are applied to a measurement in which the apparatus is itself treated as a quantum system.

**2.** [Warm-up, *Understand*] The following claim appears in a popular science article: "Decoherence solved the measurement problem in the 1980s. Scientists now understand why quantum mechanics looks classical at large scales." Write a two-paragraph response. In the first paragraph, state what decoherence actually explains. In the second paragraph, identify the specific logical gap that decoherence does not close.

**3.** [Apply, *Apply*] Work through the von Neumann chain for the following setup: a photon in the superposition $\tfrac{1}{\sqrt{2}}(|H\rangle + |V\rangle)$ passes through a polarizing beam splitter that routes $|H\rangle$ to detector D1 and $|V\rangle$ to detector D2. Write out the state after:  
(a) the photon-detector pre-measurement interaction,  
(b) the inclusion of the environment,  
(c) the inclusion of a human observer reading the detector.  
Then state, in one sentence each, where Copenhagen, many-worlds, and GRW would place the collapse.

**4.** [Apply+, *Analyze*] The Frauchiger–Renner (2018) thought experiment involves two super-observers (call them Ursula and Wigner) who each measure the quantum state of a lower-level observer (Friend F1 and Friend F2 respectively) who has themselves measured a quantum system. Frauchiger and Renner argue that if:  
(i) quantum mechanics applies universally (including to observers),  
(ii) agents can use each other's descriptions,  
(iii) measurements have unique outcomes,  
then a self-consistent contradiction arises.  
Identify which of the three assumptions each of the following interpretations would reject: (a) Copenhagen, (b) many-worlds, (c) QBism. Explain in one sentence per interpretation.

**5.** [Produce, *Evaluate*] CSL makes a specific experimental prediction: macroscopic objects should exhibit an anomalous heating rate due to collapse-induced position diffusion. The CSL heating rate for a free particle of mass $m$ is:

$$\frac{d\langle p^2\rangle}{dt} = \frac{\hbar^2 \lambda m^2}{m_0^2 r_C^2}$$

where $m_0$ is the nucleon mass, $\lambda \approx 10^{-17}$ s$^{-1}$, $r_C \approx 10^{-7}$ m. Estimate the heating power for a 1-gram test mass (like the LISA Pathfinder test mass). Express your answer in watts. Comment on whether this is detectable with modern precision measurement technology (LISA Pathfinder sensitivity: $\sim 10^{-30}$ N$^2$/Hz in force noise).

**6.** [Produce, *Evaluate*] You are asked to design an experiment to distinguish Bohmian mechanics from standard quantum mechanics. Argue that this is impossible in the non-relativistic regime by showing: (a) that Bohmian mechanics reproduces the Born rule for all observables given the quantum equilibrium assumption, and (b) that the quantum equilibrium distribution is the unique distribution that is preserved under Bohmian dynamics (the equivariance property). Conclude with a sentence about why empirical equivalence does not make the choice between interpretations trivially unimportant.

---

## Still puzzling

The measurement problem is genuinely open. A 2025 review (arXiv:2502.19278) surveyed Copenhagen, many-worlds, objective collapse, hidden variables, and epistemic interpretations and declined to declare a winner — not for lack of effort but because the problem remains logically unresolved. A 2013 survey of 33 physicists at a foundations conference (Schlosshauer, Kofler, Zeilinger, *Am. J. Phys.* 81:325) found: Copenhagen-adjacent 42%, many-worlds 18%, information-theoretic 24%, other/none 16%. These are physicists who think about foundations professionally. No consensus.

Objective-collapse models (GRW/CSL) are the only class where experiment can help: the allowed parameter space is being squeezed from multiple directions simultaneously. Whether the models will be ruled out or survive as viable alternatives to standard QM is a question that will be answered in the next decade of precision measurements.

The Frauchiger–Renner result (2018) has sharpened the logical structure of the debate without resolving it. It makes precise which combinations of interpretational assumptions are inconsistent. Which assumption to drop is a matter of active philosophical and scientific dispute.

There is something remarkable about the situation: the formalism of quantum mechanics is among the most precisely verified theories in the history of science. Its predictions have been confirmed to parts per billion in some cases. And yet what the formalism means — what happens in a measurement, whether the wave function represents something real, whether there are other branches, whether particles have definite positions — is not agreed upon. The physics and the metaphysics have entirely separated. Both are serious ongoing endeavors.

---

## The +1 — Simulation Exercise

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 7 — Measurement and Interpretations
Deliverable: 07-von-neumann-chain.html
Status: in progress

The simulation has two panels in one HTML file:

Panel A — The von Neumann chain (800 x 500 SVG).
- Five horizontal boxes in a row: SYSTEM → APPARATUS → ENVIRONMENT → OBSERVER → NOTES.
- Each box can be in one of four states: "quantum (superposition)," 
  "entangled," "decohered," or "classical (definite)."
- A slider labeled "Time step" advances through the four steps of the 
  von Neumann chain.
- At each time step, the state vector is displayed explicitly:
  Step 0: |ψ⟩_S = α|↑⟩ + β|↓⟩  (sliders for α, β)
  Step 1: α|↑⟩|A↑⟩ + β|↓⟩|A↓⟩  (pre-measurement)
  Step 2: α|↑⟩|A↑⟩|E↑⟩ + β|↓⟩|A↓⟩|E↓⟩  (env. entanglement)
  Step 3: same + |O"up"⟩ and |O"down"⟩ terms
- Below the chain, a "where is the cut?" row with one radio button 
  per interpretation: Copenhagen / Many-worlds / Bohmian / GRW / QBism.
  When an interpretation is selected, highlight (amber border) the box 
  where that interpretation places its cut. Copenhagen: boundary between 
  boxes 1 and 2. Many-worlds: no box highlighted (no cut). 
  Bohmian: no cut for ψ, separate "particle position" indicator appears 
  below SYSTEM with a definite value. GRW: box 2 (environment) gets a 
  "collapse!" label with a stochastic animation. QBism: box 4 (observer) 
  highlighted.

Panel B — Decoherence: off-diagonal decay (700 x 400 SVG).
- 2×2 density matrix visualized as a bar chart (four bars: ρ_00, ρ_01, 
  ρ_10, ρ_11; heights proportional to |ρ_ij|).
- A slider labeled "Decoherence time t/τ" from 0 to 5.
- As the slider advances, ρ_01 and ρ_10 decay as exp(-t/τ), 
  ρ_00 and ρ_11 remain fixed at |α|² and |β|².
- Separate text below the chart: 
  "Off-diagonal elements (coherence): [value]"
  "Diagonal elements (populations): |α|² = [value], |β|² = [value]"
  "Has a single outcome been selected? [NO — both populations remain]"
- The "NO" remains in red throughout the simulation, regardless of 
  how much decoherence has occurred. This is the pedagogical point.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md the following physics rules for Chapter 7 simulations:

MEASUREMENT AND INTERPRETATIONS PHYSICS RULES

1. State representation: store the two-component amplitude vector 
   (α, β) for the system qubit. Normalize after every update.
   The density matrix is ρ = [[|α|², αβ*], [α*β, |β|²]].

2. Decoherence of off-diagonal elements:
   ρ_01(t) = ρ_01(0) * exp(-t / τ_decoherence)
   ρ_10(t) = conj(ρ_01(t))
   ρ_00 and ρ_11 do NOT change under pure dephasing decoherence.

3. The "cut" placement for each interpretation:
   - Copenhagen: cut is a visual marker between System/Apparatus 
     and the classical world — not a physical event, an accounting choice.
   - Many-worlds: no cut; all terms remain; add a "branch" indicator 
     showing both outcomes as co-existing.
   - Bohmian: no cut for ψ; a separate particle-position element 
     shows a definite trajectory. The other branch of ψ is marked "empty."
   - GRW/CSL: stochastic collapse event at the apparatus or environment 
     box; one term survives with amplitude 1, the other amplitude 0.
     The surviving term is randomly selected weighted by |α|² and |β|².
   - QBism: cut at the observer box; the quantum state is the observer's 
     belief assignment, updated upon the outcome.

4. DO NOT make the simulation "collapse" to a single outcome during 
   decoherence. The point is that decoherence leaves both diagonal 
   terms nonzero. Only under GRW simulation mode does the simulation 
   randomly select one term (with correct Born-rule probabilities).

5. The "Has a single outcome been selected?" indicator must remain "NO" 
   (red) in all non-GRW interpretation modes, regardless of decoherence.
   Under GRW mode, after the collapse event, it switches to "YES — 
   outcome: [↑/↓]" with a flash animation.
```

### Part 3 — The simulation prompt

```
You are working in my directory, which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 07-von-neumann-chain.html: a single self-contained HTML file 
using D3 v7 from a CDN and no other dependencies, implementing the 
Chapter 7 simulation as specified in PROJECT.md and following the 
physics rules in CLAUDE.md and the visual constitution in DESIGN.md.

PANEL A — VON NEUMANN CHAIN (800 x 500 SVG).
- Five horizontally spaced boxes (rectangles 120×80) with labels 
  SYSTEM, APPARATUS, ENVIRONMENT, OBSERVER, WORLD, connected by 
  right-pointing arrows.
- Two sliders: |α|² (range 0 to 1, controls the superposition weight; 
  β = sqrt(1-|α|²) automatically) and "Step" (0, 1, 2, 3 = the four 
  chain steps).
- Below the chain: a text panel showing the current state vector 
  explicitly in LaTeX-like text (rendered as Unicode math symbols).
- An interpretation selector: radio buttons for Copenhagen, Many-worlds, 
  Bohmian, GRW, QBism, Relational. When selected:
  - Copenhagen: amber dashed vertical line between APPARATUS and ENVIRONMENT.
  - Many-worlds: all boxes highlighted equally; small "branch 1" and 
    "branch 2" labels appear below OBSERVER.
  - Bohmian: a small "particle: ↑" or "particle: ↓" definite indicator 
    below SYSTEM; the wave function chain shows normally but labeled ψ_guide.
  - GRW: a red "COLLAPSE EVENT" starburst appears at ENVIRONMENT at Step 2.
    One branch of the state vector is struck through with an X.
    The surviving term is chosen randomly using |α|² weighting on first 
    display; a "re-collapse" button resamples.
  - QBism: the OBSERVER box is highlighted amber and labeled 
    "Agent's belief update (not physical collapse)."
  - Relational: each arrow between boxes is labeled "relative to [next system]."

PANEL B — DECOHERENCE (700 x 400 SVG).
- Four vertical bars: ρ_00 (height ∝ |α|²), ρ_01 (∝ |ρ_01|), 
  ρ_10 (∝ |ρ_10|, = ρ_01 for real state), ρ_11 (∝ |β|²).
  Color ρ_00, ρ_11 in blue (populations); ρ_01, ρ_10 in orange (coherences).
- A time slider (t/τ from 0 to 6) that animates the exponential decay 
  of ρ_01 and ρ_10 while leaving ρ_00 and ρ_11 fixed.
- Persistent red text below: "SINGLE OUTCOME SELECTED? NO"
  This text does NOT change even when ρ_01 = 0. This is the teaching point.
- Under GRW mode only: a "Trigger collapse" button that randomly 
  (weighted by ρ_00 and ρ_11) selects one diagonal element as the 
  outcome, sets the other to zero, and changes the text to "YES — 
  outcome: ↑" or "YES — outcome: ↓" with a green flash.

Do NOT use any CSS frameworks. Inline all styles. Comments at every 
physics-relevant decision in the code.
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. Set $|\alpha|^2 = 0.5$ (equal superposition). Advance through all four chain steps in "no interpretation" mode. Write out the state vector at each step in Dirac notation.

2. Select the "Many-worlds" interpretation. What does the chain look like at Step 3? Are any branches crossed out or faded? What does this tell you about the many-worlds answer to the outcome problem?

3. Select "GRW." Click "Trigger collapse" five times, recording the outcome each time. Over many runs, approximately what fraction of outcomes should be $|\!\uparrow\rangle$? How does this match $|\alpha|^2 = 0.5$?

4. In Panel B, advance the decoherence slider to $t/\tau = 5$. The off-diagonal elements have decayed to $e^{-5} \approx 0.007$ of their original value. Does the "SINGLE OUTCOME SELECTED?" indicator change? Why or why not?

5. Select the "Bohmian" interpretation. Notice that the wave function chain shows normally, but a separate "particle position" indicator appears. In one sentence, explain what the particle position represents physically in Bohmian mechanics.

6. **Extension:** The GRW rate for a single particle is $\lambda \approx 10^{-17}$ s$^{-1}$. For a biological neuron (mass $\sim 10^{-12}$ kg, number of particles $N \sim 10^{11}$), estimate the mean time between GRW collapse events affecting the neuron. Is GRW macroscopically fast enough to explain the appearance of definite neural firings? (Hint: GRW rate scales as $N\lambda$.)

---

## References

- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (English: *Mathematical Foundations of Quantum Mechanics*, Princeton, 1955.)

- Bohr, N. (1935). Can quantum-mechanical description of physical reality be considered complete? *Physical Review*, 48, 696. [verify]

- Everett, H., III (1957). "Relative state" formulation of quantum mechanics. *Reviews of Modern Physics*, 29, 454.

- Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of "hidden" variables, I and II. *Physical Review*, 85, 166 and 180.

- Ghirardi, G. C., Rimini, A., & Weber, T. (1986). Unified dynamics for microscopic and macroscopic systems. *Physical Review D*, 34, 470.

- Pearle, P. (1989). Combining stochastic dynamical state-vector reduction with spontaneous localization. *Physical Review A*, 39, 2277.

- Schlosshauer, M. (2003). Decoherence, the measurement problem, and interpretations of quantum mechanics. *Reviews of Modern Physics*, 76, 1267. arXiv:quant-ph/0312059.

- Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.

- Schlosshauer, M. (2019). Quantum decoherence. *Physics Reports*, 831, 1–57.

- Bassi, A., & Ghirardi, G. C. (2003). Dynamical reduction models. *Physics Reports*, 379, 257.

- Bassi, A., Lochan, K., Satin, S., Singh, T. P., & Ulbricht, H. (2013). Models of wave-function collapse, underlying theories, and experimental tests. *Reviews of Modern Physics*, 85, 471.

- Carlesso, M., et al. (2016). Experimental bounds on collapse models from gravitational wave detectors. arXiv:1606.04581. [verify]

- Carlesso, M., et al. (2022). Collapse models: A theoretical, experimental and philosophical review. *AVS Quantum Science* (PMC 10138035).

- Deutsch, D. (1999). Quantum theory of probability and decisions. *Proceedings of the Royal Society A*, 455, 3129.

- Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press.

- Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). An introduction to QBism with an application to the locality of quantum mechanics. *American Journal of Physics*, 82, 749.

- Griffiths, R. B. (1984). Consistent histories and the interpretation of quantum mechanics. *Journal of Statistical Physics*, 36, 219.

- Gell-Mann, M., & Hartle, J. B. (1990). Alternative decohering histories in quantum mechanics. In *Complexity, Entropy, and the Physics of Information*, ed. W. Zurek, Addison-Wesley.

- Frauchiger, D., & Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. *Nature Communications*, 9, 3711.

- Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75, 715.

- Bell, J. S. (1990). Against "measurement." *Physics World*, 3(8), 33.

- Schlosshauer, M., Kofler, J., & Zeilinger, A. (2013). A snapshot of foundational attitudes toward quantum mechanics. *American Journal of Physics*, 81, 325.

- Maudlin, T. (2019). *Philosophy of Physics: Quantum Theory*. Princeton University Press.

- Norsen, T. (2017). *Foundations of Quantum Mechanics*. Springer.

- Rovelli, C. (1996). Relational quantum mechanics. *International Journal of Theoretical Physics*, 35, 1637. [verify]

- arXiv:2502.19278 (2025). The quantum measurement problem: A review of recent trends. [verify]

- Stanford Encyclopedia of Philosophy: "Bohmian Mechanics" (Summer 2024 ed.): plato.stanford.edu/archives/sum2024/entries/qm-bohm/ [verify]

- Stanford Encyclopedia of Philosophy: "Consistent Histories" (Fall 2024 ed.): plato.stanford.edu/archives/fall2024/entries/qm-consistent-histories/ [verify]

- Stanford Encyclopedia of Philosophy: "Quantum-Bayesian and Pragmatist Views of Quantum Theory": plato.stanford.edu/entries/quantum-bayesian/ [verify]
