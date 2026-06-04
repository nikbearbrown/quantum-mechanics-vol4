# Research Notes: Chapter 07 — Measurement and Interpretations

**Corresponding chapter:** chapters/07-measurement-and-interpretations.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students can articulate the measurement problem with precision — the logical tension between unitary evolution and the projection postulate — trace the von Neumann measurement chain, and place each major interpretation at the specific point where it cuts the chain. They understand what decoherence explains (the appearance of classicality, the preferred basis) and what it does not (the outcome-selection problem). They can distinguish empirically equivalent interpretations from the one class of interpretations — objective-collapse models — that generates distinct testable predictions. The chapter makes no recommendation among interpretations; it maps the logical space.

---

## A. Conceptual foundations

### 1. The measurement problem: the precise statement

Quantum mechanics has two dynamical rules that are logically incompatible when applied to measurement:

**Rule 1 — Unitary evolution (Schrödinger):** Between measurements, the state vector |ψ⟩ evolves unitarily: |ψ(t)⟩ = U(t)|ψ(0)⟩. This is deterministic, linear, reversible, and preserves superpositions.

**Rule 2 — Projection postulate (Born/von Neumann):** Upon measurement of observable O with eigenvalues oᵢ and eigenstates |oᵢ⟩, the state collapses: if the system is in Σᵢ cᵢ|oᵢ⟩, measurement yields outcome oᵢ with probability |cᵢ|² and the state instantaneously becomes |oᵢ⟩.

The problem: if measuring apparatus and system are both quantum, then the combined system+apparatus state should evolve unitarily, not collapse. The collapse rule appears to require something outside the quantum formalism — an observer, a classical domain, a consciousness, or a new physics.

More precisely, the problem has two distinct parts:
- **The basis problem:** What selects the basis in which collapse occurs? (Why do we never see macroscopic superpositions of position eigenstates?)
- **The outcome problem ("and → or"):** Given that collapse occurs in some basis, why does one particular eigenvalue result? Unitary evolution of a superposition produces an entangled state (cat + detector + observer), not one outcome.

Decoherence addresses the basis problem substantially. It does not address the outcome problem. This is the single most important distinction in the chapter.

### 2. The von Neumann measurement chain

Von Neumann (1932) formalized the measurement problem as a chain. Let the system S be in state |ψ⟩ = α|↑⟩ + β|↓⟩. Let the apparatus A begin in ready state |R⟩.

Step 1 — Pre-measurement (system + apparatus entangle under unitary evolution):
(α|↑⟩ + β|↓⟩)|R⟩ → α|↑⟩|A↑⟩ + β|↓⟩|A↓⟩

This is a well-defined unitary evolution (von Neumann's "first kind of measurement"). The result is an entangled state, not a definite outcome.

Step 2 — Registration (apparatus + environment E entangle):
α|↑⟩|A↑⟩|E₀⟩ + β|↓⟩|A↓⟩|E₀⟩ → α|↑⟩|A↑⟩|E↑⟩ + β|↓⟩|A↓⟩|E↓⟩

Still unitary; now environment is entangled.

Step 3 — Observer/consciousness:
The chain continues without ever requiring collapse if Rule 1 is applied consistently. Von Neumann identified this as requiring a "cut" (Schnitt) somewhere. The observer O observing the apparatus produces:
α|↑⟩|A↑⟩|E↑⟩|O"↑"⟩ + β|↓⟩|A↓⟩|E↓⟩|O"↓"⟩

Each interpretation places the cut at a different location in this chain — that is the worked example.

**Where each interpretation places the cut:**
- Copenhagen: the cut is pragmatic, placed wherever the "classical/quantum" boundary is appropriate for the calculation. It is not a physical law, just an accounting device.
- Many-worlds: there is no cut. All branches are real; the observer superposition is a real physical state. Each branch has a copy of the observer perceiving one outcome.
- Bohmian mechanics: the cut is conceptual. Particles have definite positions always; the wave function guides but never collapses. The "outcome" is determined by the particle's trajectory.
- GRW/CSL (objective collapse): there is a physical collapse event with a specified rate. The cut is a physical process, not an axiom. The chain terminates at step 2 or 3 for macroscopic apparatus by objective collapse.
- QBism: the cut is at the agent. Quantum states are not ontic; they are an agent's probabilistic beliefs. Collapse is the agent updating beliefs upon experience, not a physical event.
- Consistent histories: the cut is replaced by a framework choice. Different consistent frameworks give different descriptions; they cannot be combined (single-framework rule).

### 3. Decoherence and the basis problem

Decoherence — described fully in Ch 6 — partially solves the basis problem.

Under environmental coupling, superpositions in the pointer basis (the basis stable under environmental monitoring) rapidly decohere. Off-diagonal elements of ρ in the pointer basis decay exponentially. The resulting density matrix is diagonal in the pointer basis:

ρ_S → |α|²|↑⟩⟨↑| + |β|²|↓⟩⟨↓|

This looks like a classical probability distribution. But it is still a density matrix — a mathematical object. The diagonal elements |α|² and |β|² are still both there. The question of why one of them is "the outcome" remains open.

Zurek's einselection (environment-induced superselection): the environment selects the pointer basis, explains why we see measurements in energy bases and position bases, and explains why macroscopic superpositions are never observed (decoherence times ~ 10^(−36) s for dust in air). Key citation: Zurek (2003), Rev. Mod. Phys. 75:715.

What decoherence does NOT explain:
1. Why one branch is actual (the "and → or" problem)
2. The Born rule probabilities (these are presupposed in the interpretation of the density matrix)
3. Why observers have unique experiences (rather than experiencing a superposition)

This is the central logical structure the chapter must convey cleanly. Schlosshauer's framing (2007, Ch. 8; 2003, Rev. Mod. Phys. 76:1267) is the best source for what decoherence does and does not accomplish.

### 4. The preferred basis problem and its partial resolution

Without decoherence: the projection postulate requires selecting a basis for collapse, but the formalism does not specify which basis. Measuring position collapses to position eigenstates; measuring momentum collapses to momentum eigenstates. Why position rather than momentum for macroscopic objects?

With decoherence / einselection: the environment interaction Hamiltonian H_int selects the pointer states as eigenstates of the coupling operator. For objects coupled to photons through position, position eigenstates are the pointer states. This gives a dynamical explanation for why macroscopic objects are found in position eigenstates, not energy eigenstates.

Remaining nuance (flag for teaching): Does einselection truly solve the preferred basis problem? Critiques include: (a) the pointer basis may not be uniquely defined if H_int has degeneracies; (b) different bath models can give different pointer bases; (c) the factorization of system vs. environment is not itself derived from first principles (what counts as "environment"?). See Bacciagaluppi (2020), Stanford Encyclopedia of Philosophy, "The Role of Decoherence in Quantum Mechanics."

---

## B. The major interpretations

### 1. Copenhagen interpretation

**Originators:** Bohr, Heisenberg, Born (1920s–1940s).

**Core claim:** Quantum mechanics does not describe a pre-existing reality; it is a computational tool for predicting measurement outcomes. The wave function is a calculational device, not an ontological object. There is a classical/quantum cut — the apparatus and the macroscopic world are fundamentally classical; quantum mechanics applies to the microscopic quantum system.

**Measurement:** The collapse is not a physical event. It represents the updating of the description from the quantum domain to the classical domain as information becomes macroscopic.

**Advantages:** Consistent with practice. Most working physicists use a Copenhagen-adjacent stance. No additional ontology required.

**Disadvantages:** The "classical/quantum" cut is never defined precisely. Why is an apparatus classical? Why does "measurement" have a special status? Bohr famously resisted demands for a deeper account. The interpretation is not wrong; it is deliberately incomplete.

**Current status:** Still the most widely used operational stance. Most measurement calculations (quantum optics, quantum computing) use effective Copenhagen. Not a well-defined interpretation in the sense of having precise axioms.

**Key references:** Bohr (1935), Phys. Rev. 48:696 (response to EPR); Heisenberg (1958), Physics and Philosophy; Bell (1990), "Against 'Measurement'", Physics World.

### 2. Many-worlds interpretation (Everett/relative state)

**Originator:** Hugh Everett III (1957).

**Core claim:** The state vector is real; unitary evolution is universal and never interrupted. Measurement does not collapse the state; it entangles the observer with the system. All branches of the superposition are equally real. There is no collapse; there is branching.

**Measurement:** After measurement, the universe is in a superposition of branches. Each branch contains a version of the observer who perceives a definite outcome. There are no preferred branches; all exist.

**The Born rule problem:** The most serious technical challenge. If all branches exist, what do probabilities mean? Deutsch (1999) and Wallace (2010, "How to Prove the Born Rule") give a decision-theoretic derivation: a rational agent who takes part in quantum gambles should assign utilities consistent with Born-rule weights. This is controversial: critics (e.g., Greaves, Myrvold) question whether the derivation is circular. As of 2025, the Born rule derivation in many-worlds is not settled.

**Advantages:** No additional ontology beyond the standard formalism. Unitary evolution is preserved. No measurement axiom is needed.

**Disadvantages:** An extraordinary proliferation of unobservable branches. The Born rule derivation is contested. The notion of "branch" requires a pointer basis, which brings in decoherence — arguably in a circular way.

**Current status:** Taken seriously by a significant minority of physicists and philosophers. Receives detailed technical development (Wallace 2012, "The Emergent Multiverse"; Saunders et al. eds., 2010). The Born rule controversy (Deutsch–Wallace vs. critics) is the most active open technical debate within the interpretation.

**Key references:** Everett (1957), Rev. Mod. Phys. 29:454; DeWitt & Graham eds. (1973); Wallace (2012), The Emergent Multiverse, Oxford; Deutsch (1999), Proc. Roy. Soc. A 455:3129.

### 3. Bohmian mechanics (pilot-wave / de Broglie–Bohm)

**Originators:** de Broglie (1927), Bohm (1952).

**Core claim:** Particles have definite positions at all times, even when unobserved. The wave function ψ is a real field that guides (pilots) the particle trajectories via the guiding equation:

dx/dt = (ℏ/m) Im(∇ψ/ψ) = j/ρ

where j is the probability current and ρ = |ψ|². The wave function evolves by the Schrödinger equation always (no collapse). Apparent collapse is explained by the particle's position selecting one branch; the other branches become "empty waves" with no particle.

**Measurement:** The particle's trajectory is determined by ψ and the initial position. The Born rule follows from the assumption that initial particle positions are distributed as |ψ₀|² (quantum equilibrium). Given this assumption, all Born-rule statistics are reproduced.

**Nonlocality:** Bell showed that any hidden-variable theory reproducing quantum predictions must be nonlocal. Bohmian mechanics is explicitly nonlocal: the guiding equation depends on the global wave function, so one particle's velocity depends on the instantaneous configuration of all other particles. This nonlocality is not exploitable for signaling (because of quantum equilibrium), but it is a real feature of the theory.

**Advantages:** Deterministic. Particles have definite positions. Born rule derivable from initial conditions (not postulated). No measurement axiom.

**Disadvantages:** Nonlocality is explicit and structural. Extension to relativistic quantum field theory is difficult and contested. The wave function must be treated as real (ontic) and lives in configuration space (3N dimensions for N particles), not physical space. "Empty waves" are undetectable, which troubles some physicists.

**Current status:** A fully developed theory with exact predictions identical to standard quantum mechanics in all tested regimes. Active research on relativistic extensions, QFT, and field-theoretic versions. Stanford Encyclopedia (Summer 2024 edition: plato.stanford.edu/archives/sum2024/entries/qm-bohm/) is current.

**Key references:** de Broglie (1927); Bohm (1952), Phys. Rev. 85:166, 180; Bell (1982), "On the Impossible Pilot Wave"; Dürr, Goldstein, Zanghì (2013), Quantum Physics Without Quantum Philosophy, Springer.

### 4. Objective-collapse theories (GRW, CSL)

**The key point:** This is the only class of interpretation that makes predictions that differ from standard quantum mechanics, and therefore the only class that is experimentally testable as an alternative to the standard theory.

**GRW model (Ghirardi–Rimini–Weber, 1986):** The Schrödinger equation is modified by spontaneous, random localization events. Each particle has a rate λ ≈ 10^(−17) s^(−1) of experiencing a collapse to a Gaussian of width r_C ≈ 10^(−7) m (100 nm). For a single particle, this is negligible (one collapse per ~10¹⁷ seconds). For a macroscopic object with N ~ 10²³ particles, the collapse rate scales as Nλ ~ 10⁶ s^(−1) — extremely fast. Macroscopic superpositions are suppressed; microscopic superpositions survive. The model is both phenomenologically reasonable and physically precise.

**CSL model (Continuous Spontaneous Localization, Pearle 1989; Ghirardi, Pearle, Rimini 1990):** Overcomes GRW's problem with identical particles by using a stochastic differential equation for the state vector. The collapse is driven by a continuous noise field. CSL preserves symmetrization/antisymmetrization. Two parameters: collapse rate λ (with uncertainty: GRW value λ ≈ 10^(−17) s^(−1), Adler value λ ≈ 10^(−8±2) s^(−1)) and correlation length r_C.

**Experimental constraints (critical for the chapter):**
- GW detectors (LIGO, LISA Pathfinder, AURIGA): the collapse noise produces a diffusion on top of normal particle motion. LISA Pathfinder has excluded significant portions of the CSL parameter space. (Helou et al., 2017; Carlesso et al., 2016, arXiv:1606.04581)
- Optomechanical experiments: levitated nanospheres constrain collapse rates by measuring excess position diffusion.
- Molecular interferometry: large-molecule double-slit experiments (Arndt group, Vienna) set bounds from above (if collapse were fast enough, interference would disappear).
- BEC interferometry: Bose-Einstein condensate experiments can probe new regions of parameter space, potentially ruling out large swaths of CSL parameters.

**Current status (2026):** A significant portion of the CSL parameter space has been excluded. The GRW parameters (λ_GRW, r_C = 10^(−7) m) survive current constraints. The Adler parameters (λ_Adler ~ 10^(−8) s^(−1)) are under pressure from non-interferometric experiments. The GW-detector constraints are among the strongest. This is a live experimental program. Collapse models have not been ruled out, but they are being squeezed.

**Advantages:** Solves both the basis problem and the outcome problem. Deterministically causes unique outcomes (via the stochastic collapse). Makes distinct experimental predictions.

**Disadvantages:** Introduction of new physics (collapse rate, correlation length) not derivable from other principles. Relativistic extensions (relativistic CSL) are technically difficult and have problems with energy conservation. The specific parameter values have no deep justification.

**Key references:** Ghirardi, Rimini, Weber (1986), Phys. Rev. D 34:470; Pearle (1989), Phys. Rev. A 39:2277; Bassi & Ghirardi (2003), Phys. Rep. 379:257; Bassi et al. (2013), Rev. Mod. Phys. 85:471; Carlesso et al. (2022), "Collapse Models: A Theoretical, Experimental and Philosophical Review," PMC 10138035 (available online).

### 5. QBism (Quantum Bayesianism)

**Originators:** Caves, Fuchs, Schack (early 2000s); developed by Fuchs, Mermin, Schack.

**Core claim:** Quantum mechanics is a normative tool for an agent to organize their probabilistic expectations about future experiences. The wave function is not an element of reality; it is the agent's probability assignment. There is no collapse as a physical process; there is belief updating (Bayesian conditioning) upon experience.

**Measurement:** When an agent performs a measurement and gets outcome oᵢ, the state "collapses" in the same way any probability distribution collapses upon learning a result — not a physical event, just updating beliefs. The outcome is a real experience of the agent; the quantum state before and after is an assignment, not a reality.

**The Born rule in QBism:** Fuchs and collaborators reformulate the Born rule as a normative constraint on coherent belief-updating, using a reference measurement (a symmetric informationally complete POVM). This removes the Born rule from the status of a physical postulate and makes it a constraint on rational agency.

**Advantages:** No collapse problem (because no physical collapse). No preferred basis problem (basis depends on which measurement the agent performs). No nonlocality paradoxes (because state assignments are agent-local). Consistent with "Wigner's friend" scenarios.

**Disadvantages:** Science is typically realist — we assume our theories describe a world independent of agents. QBism's agent-centrism is philosophically non-standard. It is not clear what QBism says about the physical world (if anything). Mermin's version (participatory realism) is somewhat different from Fuchs's. Critics charge that QBism doesn't "solve" the measurement problem so much as refuse to ask the question.

**Current status:** A coherent minority position with serious philosophical development. Active work on reformulating the quantum formalism using SIC-POVMs as the reference measurement. Fuchs continues developing QBism as a research program. Stanford Encyclopedia (plato.stanford.edu/entries/quantum-bayesian/) has a current entry.

**Key references:** Fuchs, Mermin, Schack (2014), Am. J. Phys. 82:749; Fuchs (2010), "QBism, the Perimeter of Quantum Bayesianism," arXiv:1003.5209; Mermin (2014), Nature 507:421.

### 6. Consistent (decoherent) histories

**Originators:** Griffiths (1984); Omnès (1988); Gell-Mann & Hartle (1990, "decoherent histories").

**Core claim:** Quantum mechanics assigns probabilities to histories — sequences of events at different times — rather than to states at an instant. A set of histories is "consistent" (or "decoherent") if the off-diagonal terms in the density matrix of the full set vanish (the consistency condition). Within a consistent set, classical probability rules hold. There is no collapse axiom; instead, the consistency condition determines which histories can be assigned probabilities.

**Measurement:** A measurement is a selection of a consistent history set. The outcome is one element of that set. No external observer or classical domain is needed; the universe as a whole has a quantum state.

**Single-framework rule:** Different consistent sets are not combinable. You cannot use two different consistent frameworks simultaneously to make inferences about the same system. This is analogous to complementarity in Copenhagen.

**Advantages:** Consistent with closed-system quantum mechanics. No need for a classical domain. Histories (sequences of events) are natural objects for describing the world.

**Disadvantages:** Many consistent sets exist, and the formalism does not tell you which one is "real" (the framework-plurality problem). Critics argue this reintroduces the measurement problem in new language. Connection to many-worlds is debated (some see CH as reformulating MWI; Griffiths disagrees). Pedagogically, the history formalism is more abstract than the other approaches.

**Current status:** Developed primarily by Griffiths (multiple editions of "Consistent Quantum Theory," Cambridge) and Hartle (quantum cosmology applications). Omnès has a detailed philosophical treatment. Not widely adopted in mainstream physics but respected in foundations. Stanford Encyclopedia 2024 edition has a thorough treatment.

**Key references:** Griffiths (1984), J. Stat. Phys. 36:219; Omnès (1988), J. Stat. Phys. 53:893; Gell-Mann & Hartle (1990), "Alternative Decohering Histories," in Complexity, Entropy, and the Physics of Information; Griffiths (2002), Consistent Quantum Theory, Cambridge.

---

## C. Connections and dependencies

**Prerequisites (especially from Ch 6):**
- The density matrix and its diagonal vs. off-diagonal structure (Ch 6): the outcome problem is about the diagonal surviving after decoherence.
- The Lindblad equation and decoherence (Ch 6): the basis problem is addressed by einselection.
- Entanglement and partial trace (Ch 12 / earlier): the von Neumann chain is about growing entanglement.
- The Bell inequality and nonlocality (Ch 12): relevant to Bohmian mechanics and to what "nonlocal" means.

**Forward connections:**
- This chapter has no essential forward dependency within Vol 4 but closes the book's philosophical arc: every piece of formalism from Vol 1–4 is correct and empirically verified; the question of what it means is genuinely open.
- For students who pursue quantum foundations: Schlosshauer (2007), Wallace (2012), Maudlin (2019) "Philosophy of Physics: Quantum Theory" are the natural next readings.

---

## D. Current state of the field

**The measurement problem is not solved, as of 2026.** This is the honest statement. A recent comprehensive review (arXiv:2502.19278, "The Quantum Measurement Problem: A Review of Recent Trends," 2025) surveys Copenhagen, many-worlds, objective collapse, hidden variables, and epistemic interpretations without declaring a winner. The paper confirms the standard pedagogical consensus: decoherence explains the appearance of classicality but not the unique outcome.

**Experimentally constrained interpretations:**
- Objective-collapse models (GRW, CSL) make distinct predictions. Current experiments (LISA Pathfinder, LIGO, levitated optomechanics) have excluded significant portions of parameter space. The models are not ruled out but are under increasing experimental pressure.
- All other major interpretations (Copenhagen, MWI, Bohmian mechanics, QBism, consistent histories) make identical predictions to standard quantum mechanics for all currently doable experiments. They are empirically equivalent in this sense.

**Active debates:**
- Born rule in many-worlds (Deutsch–Wallace derivation): technically active, philosophically contested.
- Relativistic CSL: theoretical difficulties with energy conservation and Lorentz invariance.
- Quantum Darwinism as an account of objectivity: Zurek's program argues that pointer states that survive in many environmental "fragments" acquire an objective, observer-independent character. Remains a research program, not a consensus.
- Wigner's friend thought experiment and its extensions (Frauchiger–Renner, 2018): challenges interpretations that allow observers to themselves be in quantum superpositions. QBism and relative-state interpretations respond differently; this has sharpened the logical structure of the debate.

**Physicists' survey (Schlosshauer et al., 2013, Am. J. Phys. 81:325):** Of 33 physicists surveyed at a foundations conference: Copenhagen-adjacent 42%, many-worlds 18%, information-theoretic 24%, other/none 16%. This is a small and biased sample but gives flavor of professional distributions. No consensus.

---

## E. Teaching considerations

**The primary pedagogical danger:** Taking sides. The chapter must present interpretations fairly. Each has serious proponents. The temptation to dismiss any of them (especially Copenhagen for being "shut up and calculate," or many-worlds for being "too wild") should be resisted. The chapter's job is to map the logical space, not adjudicate.

**The central structure to build:**
1. State the measurement problem precisely (two rules, one tension)
2. Show the von Neumann chain explicitly (this makes the problem concrete)
3. Introduce decoherence as addressing the basis problem — fully worked in Ch 6
4. State clearly and explicitly what decoherence does NOT solve (the outcome problem)
5. Present each interpretation as a response to one of the two sub-problems
6. Work through where each places the "cut" in the von Neumann chain
7. Identify objective-collapse models as the uniquely testable case
8. Present the experimental constraints on CSL honestly
9. Close with intellectual honesty: the problem remains open

**Misconceptions to name:**
1. "Decoherence solves the measurement problem." It solves the basis problem; it does not solve the outcome problem. This distinction must be stated explicitly.
2. "Copenhagen means 'shut up and calculate.'" Copenhagen is a serious philosophical position (anti-realism about the wave function). It is also deliberately incomplete. Neither caricature is accurate.
3. "Many-worlds is obviously crazy / obviously right." It is a serious, technically developed interpretation with a genuine unsolved problem (the Born rule). Neither dismissal nor enthusiasm is warranted.
4. "Bohmian mechanics was disproven." It was not. It is a complete theory empirically equivalent to standard QM in all tested regimes, with a clear price: explicit nonlocality.
5. "QBism says observers create reality." QBism says quantum states are agents' beliefs, not that reality is mind-dependent. The distinction matters.
6. "Interpretations are just philosophy, physics doesn't care." Objective-collapse models are physics — they predict deviations from quantum mechanics at mesoscopic scales. Current experiments are testing them.

**The worked example (von Neumann chain):**
This should be the chapter's spine. Write out the full chain explicitly — system superposition, pre-measurement entanglement, registration with environment, observer entanglement — and then show each interpretation cutting or not cutting the chain at a specific place. This is concrete and avoids the trap of presenting interpretations as purely verbal.

**Visualization suggestion:**
A diagram with the von Neumann chain as a horizontal sequence of steps (System → Apparatus → Environment → Observer), and each interpretation shown as an arrow indicating where it places the ontological "cut." This gives students a unified frame to compare interpretations.

**On balance:** Students at this level should be able to evaluate arguments, not just memorize positions. The most valuable capability the chapter can build is the ability to say, precisely, "Interpretation X addresses the basis problem by..., but it does not address the outcome problem because..."

---

## F. Library files relevant to this chapter

- **`_lib_qmsri-13-capstone-quantum-mechanics-in-research.md`**: Contains the key passage "Decoherence solves the measurement problem" as a misconception to name (pp. 100–101 in our notation), with the precise statement that decoherence explains off-diagonal decay but does not explain why one outcome obtains. Also names Schlosshauer (2007) as the canonical accessible treatment. Contains the section "Three open problems and one honesty move" and "Still puzzling," which frame the measurement problem as genuinely open — use as a model for the chapter's closing tone.
- **`_lib_qmsri-12-entanglement-and-quantum-information.md`**: The Bell's theorem chapter (Ch 12 lib) discusses what Bell's theorem does and does not say — including the point that nonlocality can mean several different things and that Bohmian mechanics trades local realism for determinism. The no-signaling discussion is directly relevant to why Bohmian nonlocality is not exploitable.

**Neither local source contains the measurement chain, the interpretation taxonomy, or the experimental status of collapse models.** Those come from web research and standard references. The local sources are supplementary framing, not the primary content for this chapter.

---

## G. Gaps and flags

**What the local sources provide well:**
- The "decoherence does not solve the measurement problem" statement and the specific explanation of why (off-diagonal vanishes, but diagonal elements remain a superposition)
- Schlosshauer (2007) as the canonical reference for decoherence and the measurement problem
- The Bell theorem / nonlocality context relevant to Bohmian mechanics
- The intellectual-honesty framing ("the textbook stops here")

**Gaps requiring additional research or development:**

1. **The Frauchiger–Renner argument (2018):** A thought experiment extending Wigner's friend to show that certain combinations of assumptions about observers lead to contradictions. This has sharpened the debate about QBism and consistent histories. Students at this level should at least know it exists. Reference: Frauchiger & Renner (2018), Nature Comms. 9:3711. Brief mention warranted; deep treatment probably not appropriate.

2. **Relational quantum mechanics (Rovelli):** A fifth major interpretation not covered in the brief above. Rovelli (1996): physical quantities are relational — they have values only relative to other systems, not absolutely. Related to consistent histories and QBism but distinct. Mention at minimum.

3. **The Born rule measurement:** Some claim to have experimental results bearing on the Born rule (e.g., three-slit experiments testing for deviations from Born's rule). All results consistent with Born rule so far (Söllner et al., 2012). Worth a footnote.

4. **Quantum foundations surveys:** Norsen (2017), "Foundations of Quantum Mechanics" (Springer), provides a textbook-level treatment of several interpretations. Maudlin (2019), "Philosophy of Physics: Quantum Theory" (Princeton), is accessible and rigorous for the philosophical side.

**Contested territory — handle carefully:**

1. **The word "interpretation" vs. "theory":** Bohmian mechanics and CSL are not merely interpretations — they are different theories with (in the CSL case) different predictions. Using "interpretation" for all approaches muddies this distinction. The chapter should note that "objective-collapse models" are better called "alternative theories" because they make distinct predictions.

2. **The Born rule derivation in many-worlds:** The Deutsch–Wallace derivation is genuinely contested. Present both the derivation's structure and the main criticisms (circularity concerns) without declaring a winner.

3. **Copenhagen as "the" standard:** Many physicists treat Copenhagen as the default. The chapter should present it as one interpretation among several, not as the standard from which others deviate. This is not controversial in the foundations community but may surprise physics students who have been given Copenhagen implicitly.

4. **Consciousness-collapse theories (Wigner, von Neumann late work):** Von Neumann and Wigner suggested that consciousness is required to collapse the wave function. This is a minority position not developed seriously in current physics but should be mentioned briefly as a historical variant, with the note that it places the cut at the observer's consciousness. It should be named and dismissed (not developed) in a textbook context.

5. **Decoherence and the Born rule:** Some authors argue that decoherence plus some additional axiom (e.g., envariance) can derive the Born rule. Zurek's envariance argument (2003) is the best-developed version. It is contested whether this derivation is circular. The chapter should note that the Born rule remains a postulate in standard QM and that derivation attempts (envariance, decision theory) are active research, not consensus.

**Sources used:**

Web research:
- arXiv:2502.19278 (2025), "The Quantum Measurement Problem: A Review of Recent Trends" — most current comprehensive review
- Schlosshauer (2003), Rev. Mod. Phys. 76:1267, arXiv:quant-ph/0312059 — canonical treatment of decoherence and interpretations
- Schlosshauer (2007), Decoherence and the Quantum-to-Classical Transition, Springer
- Schlosshauer (2019), Physics Reports 831:1–57
- Bassi et al. (2013), Rev. Mod. Phys. 85:471 — collapse models review
- Carlesso et al. (2022), PMC 10138035 — collapse models experimental review
- Carlesso et al. (2016), arXiv:1606.04581 — LISA Pathfinder bounds on CSL
- Zurek, "Decoherence and the Transition from Quantum to Classical" (Les Houches lectures) — bourbaphy.fr/zurek.pdf
- Zurek (2022), Entropy 24:1520 — quantum Darwinism update
- SEP: "Bohmian Mechanics" (Summer 2024): plato.stanford.edu/archives/sum2024/entries/qm-bohm/
- SEP: "Consistent Histories" (Fall 2024): plato.stanford.edu/archives/fall2024/entries/qm-consistent-histories/
- SEP: "Quantum-Bayesian and Pragmatist Views": plato.stanford.edu/entries/quantum-bayesian/
- Wikipedia, "Objective-collapse theory" (for GRW/CSL parameter overview)
- Fuchs, Mermin, Schack (2014), Am. J. Phys. 82:749 — QBism statement
- Wallace (2012), The Emergent Multiverse, Oxford — many-worlds
- Deutsch (1999), Proc. Roy. Soc. A 455:3129 — Born rule derivation
- Bell (1990), "Against 'Measurement'," Physics World 3(8):33

Local library:
- _lib_qmsri-13 (measurement problem framing, Schlosshauer citation, "still puzzling" section)
- _lib_qmsri-12 (Bell theorem and nonlocality context, no-signaling)
