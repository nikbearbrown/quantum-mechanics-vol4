# Worked Exercises: Measurement, Interpretations, and the Quantum–Classical Boundary
*Chapter 7 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can trace the von Neumann measurement chain, writing the entangled state at each link ($|\Psi_1\rangle$ pre-measurement, $|\Psi_2\rangle$ with environment, $|\Psi_3\rangle$ with observer) and take a partial trace to get a reduced density matrix.
- You understand the distinction the chapter calls "the single most important logical point": decoherence solves the *basis problem* (which basis appears classical) but not the *outcome problem* (why this outcome, not that one).
- You can write a POVM $\{E_m\}$, check positivity ($E_m \ge 0$) and the completeness relation $\sum_m E_m = \hat I$, and renormalize a projective post-measurement state.

---

## Part A — Full Worked Example: A three-outcome POVM that "soft-detects" $|\!\uparrow\rangle$ versus $|\!\downarrow\rangle$

**What this demonstrates:** That a valid generalized measurement is defined by positivity of each effect *and* the completeness relation $\sum_m E_m = \hat I$ — the same structural constraint that makes the post-measurement statistics a genuine probability distribution, which the projection postulate (Rule 2) presupposes.

**The problem:** Construct a three-outcome POVM on a spin-½ system that sometimes confidently reports "up," sometimes confidently reports "down," and otherwise reports "inconclusive," with $E_\uparrow = \tfrac12|\!\uparrow\rangle\langle\uparrow|$, $E_\downarrow = \tfrac12|\!\downarrow\rangle\langle\downarrow|$. Find the third effect $E_? $ required for a valid POVM, verify positivity and completeness, and compute the outcome probabilities on the state $|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$.

**The solution:**

**Step 1 — Impose the completeness relation $\sum_m E_m = \hat I$.** Solve for the unknown effect:
$$E_? = \hat I - E_\uparrow - E_\downarrow = \hat I - \tfrac12|\!\uparrow\rangle\langle\uparrow| - \tfrac12|\!\downarrow\rangle\langle\downarrow|.$$
In the $\{|\!\uparrow\rangle, |\!\downarrow\rangle\}$ basis, $\hat I = |\!\uparrow\rangle\langle\uparrow| + |\!\downarrow\rangle\langle\downarrow|$, so
$$E_? = \tfrac12|\!\uparrow\rangle\langle\uparrow| + \tfrac12|\!\downarrow\rangle\langle\downarrow| = \tfrac12\hat I.$$
*Why:* A POVM's effects must sum to identity so that the total probability over all outcomes is 1 for *every* input state.
*Check:* $E_\uparrow + E_\downarrow + E_? = \tfrac12|\!\uparrow\rangle\langle\uparrow| + \tfrac12|\!\downarrow\rangle\langle\downarrow| + \tfrac12\hat I = \tfrac12\hat I + \tfrac12\hat I = \hat I$. ✓

**Step 2 — Verify positivity of every effect.** Each $E_m$ must have non-negative eigenvalues:
$$E_\uparrow: \text{eigenvalues } \{\tfrac12, 0\} \ge 0; \quad E_\downarrow: \{\tfrac12, 0\} \ge 0; \quad E_? = \tfrac12\hat I: \{\tfrac12, \tfrac12\} \ge 0.$$
*Why:* Probabilities $p_m = \text{Tr}(E_m\hat\rho)$ must be non-negative for all $\hat\rho$, which requires each $E_m \ge 0$.
*Check:* All three effects are diagonal in this basis with entries in $[0,1]$. ✓

**Step 3 — Compute outcome probabilities on $|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$.** Using $p_m = \langle\psi|E_m|\psi\rangle$:
$$p_\uparrow = \tfrac12|\alpha|^2, \qquad p_\downarrow = \tfrac12|\beta|^2, \qquad p_? = \tfrac12\langle\psi|\hat I|\psi\rangle = \tfrac12.$$
*Why:* The POVM "confidently" reports up or down only half the time each branch's amplitude would warrant; the rest of the weight goes to the inconclusive outcome.
*Check:* $p_\uparrow + p_\downarrow + p_? = \tfrac12|\alpha|^2 + \tfrac12|\beta|^2 + \tfrac12 = \tfrac12 + \tfrac12 = 1$. ✓

**Step 4 — Interpret against the measurement problem.** Note that this POVM is itself a *unitary-plus-projective-measurement* on a larger space (system + ancilla), consistent with Rule 1 applied to the apparatus; the "collapse" to one of three outcomes is the projection postulate (Rule 2) applied at the readout. The POVM formalism does not resolve *which* outcome obtains in a single run — it only assigns the probabilities.
*Why:* The chapter's central point: the formalism (POVM or projector) predicts the distribution; the outcome problem — why one specific result — is exactly what no amount of measurement algebra settles.
*Check:* Even with the probabilities correct, the three weights $\{p_\uparrow, p_\downarrow, p_?\}$ remain a distribution over possibilities, not a single actualized result. ✓

**Final answer:** The completing effect is $E_? = \tfrac12\hat I$; the POVM $\{\tfrac12|\!\uparrow\rangle\langle\uparrow|, \tfrac12|\!\downarrow\rangle\langle\downarrow|, \tfrac12\hat I\}$ is valid (positive, sums to $\hat I$) and yields $p_\uparrow = \tfrac12|\alpha|^2$, $p_\downarrow = \tfrac12|\beta|^2$, $p_? = \tfrac12$.

**What made this work:** Everything hinged on the completeness relation $\sum_m E_m = \hat I$. It forced the third effect uniquely, and it is the single condition guaranteeing the outcome probabilities sum to 1 for *any* input. Positivity then guaranteed each probability is non-negative. The exercise also makes the chapter's key distinction concrete: producing a clean probability distribution is not the same as explaining which outcome actually occurs — the POVM is silent on the outcome problem.

**Self-explanation prompt:** If you had instead written $E_? = \hat I - E_\uparrow - E_\downarrow$ but with $E_\uparrow = |\!\uparrow\rangle\langle\uparrow|$, $E_\downarrow = |\!\downarrow\rangle\langle\downarrow|$ (no $\tfrac12$), what would $E_?$ be, and why would the POVM degenerate into an ordinary projective measurement?

---

## Part B — Matched Practice Problem

**The problem:** Construct a two-outcome POVM that performs *unambiguous state discrimination* between the non-orthogonal states $|0\rangle$ and $|{+}\rangle = (|0\rangle+|1\rangle)/\sqrt2$ — that is, it sometimes conclusively identifies the state and otherwise returns "inconclusive," but *never* makes an error. Take $E_{\text{not-}0} = c\,|1\rangle\langle1|$ (which has zero overlap with $|0\rangle$, so it can only fire on $|{+}\rangle$) and $E_{\text{not-}+} = c\,|{-}\rangle\langle{-}|$ with $|{-}\rangle = (|0\rangle-|1\rangle)/\sqrt2$ (zero overlap with $|{+}\rangle$). Find the largest constant $c$ and the inconclusive effect $E_?$ that make $\{E_{\text{not-}0}, E_{\text{not-}+}, E_?\}$ a valid POVM, and compute the probability of an inconclusive result on each input.

Work it with the same four-step structure:

**Step 1 — Impose completeness** to solve for $E_? = \hat I - E_{\text{not-}0} - E_{\text{not-}+}$.

**Step 2 — Verify positivity** of all three effects, and find the maximum $c$ for which $E_? \ge 0$ (this is what bounds the success rate).

**Step 3 — Compute outcome probabilities** on each input $|0\rangle$ and $|{+}\rangle$, confirming the error probability is zero (each "not-X" effect never fires on X).

**Step 4 — Interpret:** explain why unambiguous discrimination is possible *only* because the states are non-orthogonal-but-distinct, and what the inconclusive outcome "costs."

**Stuck?** Write $E_{\text{not-}0}$ and $E_{\text{not-}+}$ as matrices in the $\{|0\rangle, |1\rangle\}$ basis and add them; $E_?$ must stay positive-semidefinite. The maximum $c$ is set by the smaller eigenvalue of $\hat I - E_{\text{not-}0} - E_{\text{not-}+}$ hitting zero. (The known optimum for these symmetric states is $c = 1/(1 + |\langle 0|{+}\rangle|) = 1/(1 + 1/\sqrt2)$.)

*(Instructor note: full solution intentionally omitted — students determine $c$, $E_?$, and the inconclusive probabilities, and confirm zero error.)*

---

## Part C — Completion Problem

**The problem:** A spin-½ system in $|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle$ undergoes a *projective* measurement of $\hat\sigma_z$ described by projectors $P_\uparrow = |\!\uparrow\rangle\langle\uparrow|$, $P_\downarrow = |\!\downarrow\rangle\langle\downarrow|$. Find the outcome probabilities, the post-measurement state for outcome "up," and confirm it is properly normalized. Steps 1, 2, and 5 plus the final answer are provided; fill in Steps 3 and 4.

**Step 1 — Confirm $\{P_\uparrow, P_\downarrow\}$ is a valid projective measurement.**
$$P_\uparrow + P_\downarrow = |\!\uparrow\rangle\langle\uparrow| + |\!\downarrow\rangle\langle\downarrow| = \hat I, \quad P_\uparrow^2 = P_\uparrow, \quad P_\downarrow^2 = P_\downarrow.$$
Completeness and idempotency hold — these are orthogonal projectors, a special case of a POVM with $E_m = P_m$.

**Step 2 — Compute the outcome probabilities.**
$$p_\uparrow = \langle\psi|P_\uparrow|\psi\rangle = |\alpha|^2, \qquad p_\downarrow = \langle\psi|P_\downarrow|\psi\rangle = |\beta|^2.$$

**Step 3 — Write the un-normalized post-measurement state for outcome "up," $P_\uparrow|\psi\rangle$, and then the *normalized* post-state.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Verify the normalized post-state has unit norm, and state what would go wrong if you forgot to renormalize.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Connect to the von Neumann chain.** The projective collapse of Step 3 is Rule 2 (the projection postulate). Rule 1 (unitary evolution) applied to the apparatus would instead leave $|\psi\rangle$ in the entangled superposition $\alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle$ — no single outcome. The two rules are not derivable from each other.

**Final answer:** $p_\uparrow = |\alpha|^2$; the normalized post-measurement state is $P_\uparrow|\psi\rangle / \sqrt{p_\uparrow} = (\alpha|\!\uparrow\rangle)/|\alpha| = |\!\uparrow\rangle$ up to the global phase $\alpha/|\alpha|$. Renormalization by $\sqrt{p_\uparrow}$ is mandatory; without it the post-state has norm $|\alpha| \ne 1$ and is not a valid state vector.

**Self-explanation prompt:** Explain why the post-measurement state is $|\!\uparrow\rangle$ and *not* $\alpha|\!\uparrow\rangle$ — i.e., why the projection postulate divides by $\sqrt{p_\uparrow}$, and what physical statement (probability of the next measurement) would be violated if you skipped that division.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

A student is asked to trace the von Neumann chain and say what decoherence accomplishes. They write the following.

**Step 1 — Pre-measurement.** $|\Psi_1\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle$. A superposition, not an outcome. ✓

**Step 2 — Environment entanglement.** $|\Psi_2\rangle = \alpha|\!\uparrow\rangle|A_\uparrow\rangle|E_\uparrow\rangle + \beta|\!\downarrow\rangle|A_\downarrow\rangle|E_\downarrow\rangle$; tracing out $E$ gives $\hat\rho_{SA} \approx |\alpha|^2|\!\uparrow\rangle\langle\uparrow|\otimes|A_\uparrow\rangle\langle A_\uparrow| + |\beta|^2|\!\downarrow\rangle\langle\downarrow|\otimes|A_\downarrow\rangle\langle A_\downarrow|$ as $\langle E_\uparrow|E_\downarrow\rangle \to 0$. ✓

**Step 3.** ⚠ "Once the off-diagonal elements have decayed to zero, the density matrix $\hat\rho_{SA}$ is diagonal — which *means the system has collapsed to a single outcome*. Decoherence is therefore a complete solution to the measurement problem: it is the physical mechanism of collapse. After Step 2 the apparatus is definitely reading either up or down; the diagonal density matrix proves a definite result has been selected, and we just don't yet know which. The Born-rule probabilities $|\alpha|^2$ and $|\beta|^2$ are *derived* from this decoherence process."

**Step 4 — Observer.** $|\Psi_3\rangle$ includes $|O_{\text{up}}\rangle$ and $|O_{\text{down}}\rangle$; under Copenhagen we place the cut and read off the classical fact. ✓

**Your tasks:**
1. Identify exactly which claims in Step 3 conflate decoherence's achievement with a claim it does not support.
2. Explain the chapter's central distinction: decoherence solves the *basis problem* but not the *outcome problem*. Show that the diagonal $\hat\rho_{SA}$ still contains *both* terms $|\alpha|^2$ and $|\beta|^2$ with nonzero weight — so no single outcome has been selected.
3. Refute "the Born-rule probabilities are derived from decoherence": explain why the probabilities are *presupposed* in interpreting the diagonal entries of $\hat\rho_{SA}$, not derived from the off-diagonal decay.
4. State the difference between "a proper mixture (we don't know which outcome)" and "an improper mixture (the reduced state of an entangled whole)," and why a diagonal *reduced* density matrix does not license the "definite-but-unknown outcome" reading.

**Why this error is common:** A diagonal reduced density matrix *looks* exactly like a classical probability distribution over definite outcomes, so students read "ignorance of a definite result" into what is actually an improper mixture in which both branches remain physically present.

---

## Part E — Transfer Problem

**The problem:** Apply the "what does this interpretation actually predict, and is it empirically distinguishable" discipline to objective-collapse models. GRW modifies the Schrödinger equation with spontaneous localization "hits" at rate $\lambda \approx 10^{-17}\,$s$^{-1}$ per particle. (a) For a single particle, compute the mean time between hits and confirm it is astronomically long (compare to the age of the universe, $\sim 4\times10^{17}\,$s). (b) For a macroscopic object with $N \approx 10^{23}$ particles, the collective hit rate scales as $N\lambda$; compute it and the corresponding collapse time, and confirm a macroscopic superposition collapses essentially instantaneously. (c) Explain why GRW/CSL is, per the chapter's table, the *only* interpretation class with "distinct predictions: Yes," and name one experiment (LISA Pathfinder, levitated nanospheres, or molecular interferometry) that constrains its parameter space and in which direction it pushes the bound.

**Hint (use only if stuck after 10 minutes):** Mean time between hits for one particle is $1/\lambda = 10^{17}\,$s. For (b), $N\lambda = 10^{23}\times10^{-17} = 10^6\,$s$^{-1}$, so the collapse time is $\sim10^{-6}\,$s — microseconds. The key contrast: GRW *modifies* the dynamics, so it predicts deviations (anomalous heating, lost interference fringes) that standard QM does not — that is what makes it testable, whereas Copenhagen, many-worlds, Bohmian, QBism, consistent histories, and relational QM all give identical predictions to standard QM.

**Reflection prompt:** (1) Why does the $N\lambda$ scaling — negligible for one particle, near-instant for $10^{23}$ — let GRW reproduce both quantum behavior for microscopic systems and definite outcomes for macroscopic ones? (2) The chapter stresses that ruling out *local realism* (a Bell violation) is different from selecting an interpretation. In what sense is an experimental constraint on GRW's $(\lambda, r_C)$ a genuinely different kind of result from a Bell test?

---

## Part F — Interleaved Review

**F1 — This chapter.** Set $|\alpha|^2 = 0.5$ and trace the von Neumann chain through Steps 0–3 (system → apparatus → environment → observer). Write the state vector at each step, and identify the step at which decoherence effects first become relevant. Then state, in one sentence each, where Copenhagen and many-worlds place (or refuse to place) the cut.
*Chapter this draws from: 7*

**F2 — Previous chapter.** In the chapter's pure-dephasing worked calculation, the off-diagonal $|\rho_{01}(t)| = \tfrac12 e^{-t/T_\phi}$ decays while populations stay fixed, ending at $\hat\rho(\infty) = \hat I/2$. Connect this to the decoherence step of the von Neumann chain: explain how the environmental overlap $\langle E_\uparrow|E_\downarrow\rangle \to 0$ is the *same* mechanism as $\langle e_0(t)|e_1(t)\rangle \to 0$ driving $|\rho_{01}|\to 0$, and why neither selects a single outcome.
*Chapter this draws from: Open Systems — Decoherence and the Lindblad Equation (Chapter 6)*

**F3 — Discrimination.** You are given two claims about a loophole-free Bell-inequality violation. Claim 1: "It rules out local hidden-variable theories." Claim 2: "It proves that measuring one particle instantaneously influences the other and selects the Copenhagen interpretation." For each claim, state whether it is established physics, an overreach, or interpretation-dependent, and justify.
*Note to instructor: students must distinguish settled physics (rules out LOCAL realism; Bohmian nonlocal hidden variables survive) from overreach (no FTL influence — no-signaling holds; a Bell test does not select among Copenhagen / many-worlds / Bohmian, which all predict identically) — the honesty-layer discipline of the chapter's running project.*

**Closing reflection:** Across all six parts, the recurring lesson is that the formalism predicts *distributions* (POVM probabilities, projective probabilities, diagonal density matrices, Bell correlations) but is silent on *which single outcome obtains*. State in two sentences how this one fact unifies the outcome problem, the inadequacy of decoherence as a full solution, and the empirical indistinguishability of most interpretations.

---

## Instructor Notes

**Common errors:**
1. Writing a "POVM" whose effects do not sum to identity ($\sum_m E_m \ne \hat I$) or are not positive — producing probabilities that don't normalize or go negative.
2. Treating a projective measurement's post-state as $P_m|\psi\rangle$ without renormalizing by $\sqrt{p_m}$, so the "state" no longer has unit norm.
3. Conflating decoherence's basis-problem achievement with a solution to the outcome problem — reading a diagonal *reduced* density matrix as a definite-but-unknown outcome (the Part D misconception), or claiming the Born rule is derived from decoherence.

**Signs a student needs to return:**
- They cannot articulate the basis-problem / outcome-problem distinction, or they assert decoherence "solves measurement."
- They treat an interpretation's prediction as an empirical claim (e.g. "many-worlds predicts something Copenhagen doesn't") when the chapter's table marks both "No" for distinct predictions.

**Scaffolding adjustments:** If a student struggles with Part A, first have them verify completeness for the ordinary projective measurement ($P_\uparrow + P_\downarrow = \hat I$) before introducing the $\tfrac12$ factors and the third effect. If a student finishes Part F quickly, have them build the full "claims vs. does-not-claim" table for a named result (a below-threshold QEC demonstration, an NV-sensing paper) and classify it as principle-demonstration vs. hardware benchmark vs. fragile advantage claim.

**Domain adaptation note:** For a quantum-foundations seminar, anchor Part E to the current (2026) GRW/CSL experimental status, having students locate where the latest LISA Pathfinder or molecular-interferometry bounds sit in the $(\lambda, r_C)$ plane and which parameter regimes remain open.
