# Worked Exercises: Error and the Threshold Theorem
*Chapter 9 of Quantum Mechanics — Volume 4*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The 3-qubit bit-flip code, its stabilizers $M_1 = Z_1Z_2$, $M_2 = Z_2Z_3$, and the syndrome table (no error $\to (+1,+1)$; $X_1 \to (-1,+1)$; $X_2 \to (-1,-1)$; $X_3 \to (+1,-1)$).
- The stabilizer triple $[\![n,k,d]\!]$ and the correction bound: a distance-$d$ code corrects $t = \lfloor(d-1)/2\rfloor$ errors.
- The surface-code logical error rate $p_L \approx A(p/p_\text{th})^{\lceil(d+1)/2\rceil}$ with $p_\text{th} \approx 0.01$, $A \approx 0.1$, and the suppression factor $\Lambda \approx p_\text{th}/p$.

---

## Part A — Full Worked Example

**What this demonstrates:** How to extract an effective physical error rate from a reported suppression factor and use the threshold scaling formula to verify a logical error rate at the *right* tolerance.

**The problem:** A surface-code experiment reports a suppression factor $\Lambda = 2.0$ per increase of code distance by 2, with $p_\text{th} = 0.01$ and $A = 0.1$. (a) Estimate the effective physical error rate $p$. (b) Compute the predicted logical error rate $p_L$ for $d = 3, 5, 7$. (c) The team reports a measured $p_L^{(7)} = 0.10\%$ per cycle. Does the prediction confirm the measurement, judged at the correct tolerance for this approximate formula? (d) What code distance $d$ would be needed to reach $p_L = 10^{-9}$ at this $p$?

**The solution:**

**Step 1 — Invert the suppression factor to get $p$.** The suppression factor satisfies $\Lambda \approx p_\text{th}/p$, so
$$p \approx \frac{p_\text{th}}{\Lambda} = \frac{0.01}{2.0} = 0.005.$$
*Why:* Each step of $d \to d+2$ multiplies $p_L$ by $(p/p_\text{th})$; the inverse of that factor *is* $\Lambda$. Measuring how much each bigger code helps tells you how far below threshold you sit.
*Check:* $p = 0.005 < p_\text{th} = 0.01$, so the device is below threshold ($\Lambda > 1$) — consistent with $\Lambda = 2.0 > 1$.

**Step 2 — Fix the exponents for each distance.** The exponent is $\lceil(d+1)/2\rceil$:
$$d=3:\ \lceil 4/2\rceil = 2,\qquad d=5:\ \lceil 6/2\rceil = 3,\qquad d=7:\ \lceil 8/2\rceil = 4.$$
*Why:* An undetectable logical error needs a chain of roughly half the distance; the ceiling captures the minimum number of physical errors that produce one logical error.
*Check:* The exponent grows by exactly 1 each time $d$ grows by 2 — which is precisely why each distance step multiplies $p_L$ by one more factor of $(p/p_\text{th})$, giving the constant suppression $\Lambda$.

**Step 3 — Evaluate $p_L$ at each distance.** With $p/p_\text{th} = 0.005/0.01 = 0.5$ and $A = 0.1$:
$$p_L^{(3)} = 0.1(0.5)^2 = 0.1 \times 0.25 = 0.025 = 2.5\%,$$
$$p_L^{(5)} = 0.1(0.5)^3 = 0.1 \times 0.125 = 0.0125 = 1.25\%,$$
$$p_L^{(7)} = 0.1(0.5)^4 = 0.1 \times 0.0625 = 0.00625 = 0.625\%.$$
*Why:* Below threshold, $(p/p_\text{th}) < 1$, so a higher exponent (bigger code) drives $p_L$ down — "bigger is better."
*Check:* Each successive value is exactly half the previous ($2.5 \to 1.25 \to 0.625$), matching $\Lambda = 2.0$. The ordering $p_L^{(7)} < p_L^{(5)} < p_L^{(3)}$ confirms below-threshold behavior.

**Step 4 — Compare prediction to measurement at the right tolerance.** Predicted $p_L^{(7)} = 0.625\%$; reported $= 0.10\%$. The ratio is
$$\frac{0.625\%}{0.10\%} \approx 6.3.$$
*Why:* The chapter is explicit that the simple scaling formula is *not exact at small $d$*; an agreement within a factor of $3$–$5$ counts as a correct understanding of the scaling. A factor of $\sim6$ is at the edge — close to confirming, but worth flagging that the formula slightly overestimates here.
*Check:* The prediction and measurement agree in *order of magnitude* and both are sub-percent and below threshold; the discrepancy is in the expected direction (the approximate formula overestimates $p_L$ at modest $d$), not a sign-flipped or order-of-magnitude failure.

**Step 5 — Solve for the distance reaching $p_L = 10^{-9}$.** Set $0.1(0.5)^{\lceil(d+1)/2\rceil} = 10^{-9}$. Then $(0.5)^{m} = 10^{-8}$ with $m = \lceil(d+1)/2\rceil$. Taking $\log_{10}$: $m\log_{10}(0.5) = -8$, so $m = 8/0.301 \approx 26.6$, i.e. $m = 27$. Inverting $\lceil(d+1)/2\rceil = 27$ gives $d+1 \approx 54$, so $d \approx 53$.
*Why:* Each distance step buys one factor of $(p/p_\text{th}) = 0.5$, i.e. one factor of 2 of suppression; reaching $10^{-9}$ from $A = 0.1$ needs $\sim27$ such factors.
*Check:* $0.1 \times (0.5)^{27} = 0.1 \times 7.5\times10^{-9} \approx 7.5\times10^{-10} < 10^{-9}$, so $d = 53$ (exponent 27) clears the target.

**Final answer:** (a) $p \approx 0.005$. (b) $p_L^{(3)} = 2.5\%$, $p_L^{(5)} = 1.25\%$, $p_L^{(7)} = 0.625\%$. (c) Predicted $0.625\%$ vs reported $0.10\%$, ratio $\approx6.3$ — at the edge of the factor-$3$–$5$ tolerance; the scaling is understood correctly, with the formula mildly overestimating. (d) $d \approx 53$ (exponent $27$).

**What made this work:** The reconstruction never needed an independently measured $p$ — it was recovered by *inverting the suppression factor*, which is the only first-principles handle the experiment hands you. From there, the scaling is a pure power law, and the single hardest judgment is the tolerance: a recomputed value within a factor of a few of the reported one *confirms* understanding, because the formula is an approximation at small $d$, not an exact law. Treating a factor-of-few gap as a "failure" would be the real error.

**Self-explanation prompt:** Explain why the suppression factor $\Lambda$, a ratio of two logical error rates, is the cleanest experimental signature that a device is below threshold — and why $\Lambda > 1$ and $p < p_\text{th}$ are the same statement.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same invert-$\Lambda$-then-scale reconstruction for a different reported device, with a sub-threshold $p$ that is *not* a clean $0.5$.

**The problem:** A second surface-code processor reports $\Lambda = 4.0$ per distance-2 increase, with $p_\text{th} = 0.01$ and $A = 0.1$. (a) Estimate the effective $p$. (b) Compute $p_L$ for $d = 3, 5, 7$. (c) The paper reports a measured $p_L^{(5)} = 0.02\%$ per cycle. Compute the predicted-to-reported ratio and decide, at the correct tolerance, whether the reconstruction confirms the claim. (d) What distance reaches $p_L = 10^{-6}$ at this $p$?

**Stuck?** Start from $p = p_\text{th}/\Lambda$ and form $p/p_\text{th}$ first — it is just $1/\Lambda$. Then the only thing that changes per distance is the exponent $\lceil(d+1)/2\rceil = 2, 3, 4$. Remember the tolerance rule before you call any gap a failure.

*Instructor note: full solution intentionally omitted. Students should produce the worked steps themselves following the Part A structure, including the explicit tolerance judgment in (c).*

---

## Part C — Completion Problem

**What this demonstrates:** Tracing a syndrome through the 3-qubit bit-flip code and reading the error location off the syndrome table.

**The problem:** The logical state is $|\bar\psi\rangle = \alpha|000\rangle + \beta|111\rangle$. A bit-flip $X$ acts on qubit 3. Determine the syndrome $(M_1, M_2)$, the diagnosed error location, and verify the correction restores the state.

**Step 1 — Write the error state.** $X_3$ flips the third qubit in every term:
$$X_3(\alpha|000\rangle + \beta|111\rangle) = \alpha|001\rangle + \beta|110\rangle.$$

**Step 2 — Set up the stabilizers.** $M_1 = Z_1Z_2$ measures the parity of qubits 1 and 2; $M_2 = Z_2Z_3$ measures the parity of qubits 2 and 3. Eigenvalue $+1$ means even parity (qubits agree), $-1$ means odd parity (qubits differ).

**Step 3 — Evaluate $M_1 = Z_1Z_2$ on both terms.**

*Your work here:*

*Why (your explanation):*

**Step 4 — Evaluate $M_2 = Z_2Z_3$ on both terms.**

*Your work here:*

*Why (your explanation):*

**Step 5 — Look up and correct.** The syndrome from Steps 3–4 is $(+1, -1)$. From the table, $(+1,-1)$ diagnoses an error on qubit 3. Applying $X_3$:
$$X_3(\alpha|001\rangle + \beta|110\rangle) = \alpha|000\rangle + \beta|111\rangle = |\bar\psi\rangle.$$

**Final answer:** Syndrome $(M_1, M_2) = (+1, -1)$, diagnosing an error on qubit 3; applying $X_3$ restores $\alpha|000\rangle + \beta|111\rangle$, and $\alpha,\beta$ were never measured.

**Self-explanation prompt:** Explain why both terms of the superposition must yield the *same* eigenvalue for each stabilizer, and why this is exactly what lets the syndrome be read without collapsing the logical state.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student analyzes the 3-qubit bit-flip code under a two-qubit error.

**Step 1 — Setup.** Logical state $|\bar\psi\rangle = \alpha|000\rangle + \beta|111\rangle$. Bit-flips $X_1$ and $X_3$ both occur, giving $\alpha|101\rangle + \beta|010\rangle$.

**Step 2 — Measure the stabilizers.** "I compute $M_1 = Z_1Z_2$: in $|101\rangle$ qubits 1,2 are $1,0$ (differ, $-1$); in $|010\rangle$ they are $0,1$ (differ, $-1$). So $M_1 = -1$. For $M_2 = Z_2Z_3$: in $|101\rangle$ qubits 2,3 are $0,1$ (differ, $-1$); in $|010\rangle$ they are $1,0$ (differ, $-1$). So $M_2 = -1$. Syndrome $(-1,-1)$."

**Step 3 — ⚠ Diagnose and correct.** "The syndrome $(-1,-1)$ appears in the table as $X_2$, so a single error occurred on qubit 2. I apply $X_2$, which corrects the error and fully restores $\alpha|000\rangle + \beta|111\rangle$. The $[\![3,1,1]\!]$ code has handled this case correctly."

**Step 4 — Conclusion.** "Distance-3... I mean distance-1 code, two errors, fixed. Error correction works as designed."

**Your tasks:**
1. Identify the error in Step 3.
2. Compute the *actual* state after applying $X_2$ to $\alpha|101\rangle + \beta|010\rangle$, and show it is not $|\bar\psi\rangle$.
3. Identify what logical operation the net error $X_1X_2X_3$ performs, and connect it to the code distance $d=1$ and the correction bound $t = \lfloor(d-1)/2\rfloor$.
4. State the syndrome-table fact that makes this two-qubit error *indistinguishable* from a single-qubit $X_2$ error.

**Why this error is common:** Students assume a unique syndrome guarantees a unique single-qubit error, forgetting that a weight-2 error can produce *exactly the same syndrome* as a weight-1 error — which is precisely why a distance-$d$ code corrects only $\lfloor(d-1)/2\rfloor$ errors, not $d$.

---

## Part E — Transfer Problem

**What this demonstrates:** The same stabilizer-eigenvalue check applied to a new code — the $[\![4,2,2]\!]$ code from the neutral-atom doorway, with stabilizers $XXXX$ and $ZZZZ$.

**The problem:** The $[\![4,2,2]\!]$ code has stabilizers $S_X = XXXX$ and $S_Z = ZZZZ$, with logical state $|0_L0_L\rangle = \tfrac{1}{\sqrt2}(|0000\rangle + |1111\rangle)$. (a) Verify $|0_L0_L\rangle$ is a $+1$ eigenstate of $S_Z$. (b) Verify it is a $+1$ eigenstate of $S_X$. (c) The code has distance $d=2$. Using $t = \lfloor(d-1)/2\rfloor$, how many errors can it *correct*? How many can it *detect*? (d) A single $Z_1$ error occurs. Does it flip the eigenvalue of $S_X$, $S_Z$, both, or neither — i.e. is it detected?

**Hint (use only if stuck after 10 minutes):** For (b), $X$ on a single qubit swaps $|0\rangle\leftrightarrow|1\rangle$, so $XXXX$ maps $|0000\rangle\to|1111\rangle$ and $|1111\rangle\to|0000\rangle$ — check what that does to the superposition. For (c), note that $t = \lfloor(2-1)/2\rfloor = 0$: distance 2 is a *detection* code. For (d), $Z_i$ anti-commutes with $X_i$ but commutes with $Z_i$.

**Reflection prompt:**
1. A distance-2 code corrects zero errors but detects one. Explain why "detect but not correct" is still useful, and how it differs from the distance-3 codes that *correct* one error.
2. Both the 3-qubit code and the $[\![4,2,2]\!]$ code work by checking that a state is a $+1$ eigenstate of every stabilizer. State the single structural principle this shares with the surface code's plaquette and star operators.

---

## Part F — Interleaved Review

**F1 — This chapter.** A distance-5 surface code runs at physical error rate $p = 0.002$ with $p_\text{th} = 0.01$, $A = 0.1$. (a) Compute $p_L^{(5)}$. (b) Is the device below or above threshold, and how do you know from $p$ alone? (c) Roughly how many physical qubits does a $d=5$ surface code use, given the $\sim2d^2$ rule?
*Chapter this draws from: 9*

**F2 — Earlier material: physical qubits and coherence.** From *Chapter 8 (Quantum Hardware)*, the physical error rate $p$ that enters the threshold formula is built from the hardware's coherence and gate-fidelity numbers. A transmon has two-qubit gate error $0.5\%$. (a) Treating this as the physical error rate $p$, is the device above or below the surface-code threshold $p_\text{th} \approx 0.01$? (b) What suppression factor $\Lambda = p_\text{th}/p$ would the surface code then deliver per distance-2 step, and would bigger codes help?
*Chapter this draws from: Chapter 8, superconducting transmon gate fidelity*

**F3 — Discrimination.** You see two claims. Claim X: "Our device has $p = 0.02 > p_\text{th}$, so we added more qubits and increased code distance to suppress the logical error rate." Claim Y: "Our device has $p = 0.004 < p_\text{th}$, so we increased code distance to suppress the logical error rate." One of these strategies *backfires*. Which one, and what actually happens to $p_L$ as $d$ increases in that case?
*Note to instructor: this tests whether students grasp that error correction helps only below threshold — above $p_\text{th}$, $(p/p_\text{th}) > 1$, so a higher exponent makes $p_L$ larger, and more qubits make the logical qubit worse. The discrimination between the two regimes is the point.*

**Closing reflection:** Across F1–F3, the same inequality $p$ vs $p_\text{th}$ decided everything: whether bigger codes help, what suppression factor you get, and whether a hardware platform is even worth encoding. State in one sentence why the *sign* of $(p/p_\text{th} - 1)$ matters more than the precise value of $p_L$.

---

## Instructor Notes

**Common errors:**
- Assuming a distance-$d$ code corrects $d$ errors instead of $\lfloor(d-1)/2\rfloor$ (Part D, and the $[\![4,2,2]\!]$ detect-vs-correct distinction).
- Misreading a syndrome: treating a two-qubit error's syndrome as a unique single-qubit diagnosis, leading to a logical error (Part D's core misconception).
- Calling a factor-of-3–5 gap between predicted and reported $p_L$ a "failure," when the scaling formula is approximate at small $d$ and factor-of-few agreement is success.

**Signs a student needs to return:**
- They apply error correction above threshold ($p > p_\text{th}$) and expect bigger codes to help.
- They report a logical error rate to high precision and treat any mismatch with a paper as disconfirmation, with no notion of tolerance.

**Scaffolding adjustments:** If a student struggles with Part A, have them first compute the dimensionless ratio $p/p_\text{th}$ and verify it is below 1 before touching exponents — this makes "bigger is better" visible. If a student finishes Part F quickly, have them re-derive the Willow numbers (Acharya et al., $\Lambda = 2.14$, $p_L^{(7)} = 0.143\%$) and judge the factor-$\sim3$ agreement explicitly.

**Domain adaptation note:** Experimental records (Willow, QuEra, Quantinuum) will be superseded quickly; emphasize the durable framework — digitization of errors, the stabilizer/syndrome structure, and the threshold scaling law — over any single reported $p_L$.
