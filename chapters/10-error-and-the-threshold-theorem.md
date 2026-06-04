# Chapter 10 — Error and the Threshold Theorem

## TL;DR

- Quantum errors are continuous, but syndrome measurement digitizes them onto a discrete set — correcting $X$ and $Z$ independently corrects everything.
- The no-cloning theorem forbids classical-style redundancy; stabilizer codes encode logical information in entangled states that can be diagnosed without being read.
- The 3-qubit bit-flip code is the simplest demonstration: four syndrome outcomes identify which qubit was hit without ever touching the encoded superposition.
- The threshold theorem (Aharonov–Ben-Or; Knill–Laflamme–Zurek; Kitaev, 1996–1998) guarantees that below a critical physical error rate $p_{\text{th}}$, logical error rates can be made arbitrarily small by scaling the code — the surface code sets $p_{\text{th}} \approx 1\%$.
- Google's Willow chip (December 2024) demonstrated this in hardware for the first time; QuEra's neutral-atom array (January 2026) has operated 96 logical qubits — these milestones are accumulating fast and the numbers date quickly.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Explain** (Bloom: Understand) why quantum errors cannot be corrected by simple copying, and how the digitization of errors via the Pauli basis makes QEC possible despite the continuous nature of quantum noise.
2. **Derive** (Bloom: Apply) the syndrome table for the 3-qubit bit-flip code and show that syndrome measurement identifies the error without collapsing the encoded logical state.
3. **Describe** (Bloom: Understand) the stabilizer formalism and explain how the Gottesman $[\![n,k,d]\!]$ notation characterizes a code's capacity to correct errors.
4. **Calculate** (Bloom: Apply) the expected logical error rate $p_L$ for a distance-$d$ surface code at a given physical error rate $p$, and determine whether the code is operating below or above threshold.
5. **Distinguish** (Bloom: Analyze) *error correction* (detecting and reversing errors) from *fault tolerance* (ensuring that errors introduced during error correction itself do not cascade), and connect each concept to recent experimental demonstrations.

---

## Scene Opening

It is 1994. Peter Shor has just published an algorithm that, run on a large enough quantum computer, would factor a 2,000-bit RSA key in hours. The cryptographic community is paying attention. The physics community has a different problem: qubits decay in microseconds.

The obvious fix — copy the qubit and take a majority vote, as classical engineers do with every RAID disk and every satellite — is illegal. The no-cloning theorem from Chapter 9 (Volume 3, proved by Wootters and Zurek in 1982 and Dieks independently the same year) is not an engineering inconvenience. It is a theorem: no unitary operation maps $|\psi\rangle|0\rangle \to |\psi\rangle|\psi\rangle$ for all $|\psi\rangle$. The proof is one paragraph of linear algebra and returns a contradiction. There is no workaround.

In 1995, Shor found one anyway — not by copying qubits, but by hiding their information inside entanglement. The trick is subtle enough that it takes the rest of this chapter to unpack. But the punchline is immediate: quantum error correction is possible, it does not require reading the encoded state, and there is a threshold — a critical physical error rate below which a logical qubit can be made as reliable as you like.

That threshold theorem stayed theoretical for nearly three decades. In December 2024, Google's Willow chip crossed it in hardware. In January 2026, QuEra's neutral-atom processor operated 96 logical qubits on 448 physical atoms. The engineering is young; the mathematics has been settled since 1997.

---

## Core Development

### Why classical redundancy fails

The classical three-bit repetition code works like this: encode $0 \to 000$ and $1 \to 111$; if one bit flips (say to $010$), majority vote returns $0$. To adapt this for qubits, try encoding $|0\rangle \to |000\rangle$ and $|1\rangle \to |111\rangle$. An arbitrary logical qubit $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ would need to become $\alpha|000\rangle + \beta|111\rangle$.

Now "correct" the code the classical way: measure each qubit to take the majority. But measuring the first qubit collapses $\alpha|0\rangle\langle 0| + \beta|1\rangle\langle 1|$ — the superposition is gone. The encoded information is destroyed.

The resolution is to measure something weaker than the qubits themselves. Instead of measuring *what* the qubits are, measure *parity relationships between* them. This is the key move.

### Errors are continuous but correctable

A general single-qubit error channel acting on a density matrix $\hat\rho$ can be written as

$$\mathcal{E}(\hat\rho) = \sum_k E_k \hat\rho E_k^\dagger,$$

where the **Kraus operators** $E_k$ are arbitrary $2\times 2$ matrices satisfying $\sum_k E_k^\dagger E_k = \hat I$. Any $2\times 2$ matrix is a linear combination of $\{I, X, Y, Z\}$ (the Pauli group), so

$$E_k = a_k I + b_k X + c_k Y + d_k Z.$$

Every conceivable single-qubit error — a tiny rotation, a partial dephasing, a correlated amplitude-and-phase perturbation — is a linear combination of four operators. Here is the key insight, stated precisely by Knill and Laflamme in 1997 [verify]:

> **If a code can detect and correct $X$ errors and $Z$ errors independently, it corrects any single-qubit error whatsoever.**

The continuous error space is spanned by four basis errors. Correct the basis; correct everything. This is the digitization of errors.

The three types of basis errors are:
- **Bit-flip** ($X$): $|0\rangle \leftrightarrow |1\rangle$
- **Phase-flip** ($Z$): $|0\rangle \to |0\rangle$, $|1\rangle \to -|1\rangle$
- **Combined** ($Y = iXZ$): both simultaneously

### The 3-qubit bit-flip code

Encode one logical qubit in three physical qubits:

$$|\bar 0\rangle = |000\rangle, \qquad |\bar 1\rangle = |111\rangle.$$

A general logical state becomes

$$|\bar\psi\rangle = \alpha|000\rangle + \beta|111\rangle.$$

The encoding circuit uses two CNOT gates: apply CNOT from qubit 1 to qubit 2, then CNOT from qubit 1 to qubit 3. Starting from $(\alpha|0\rangle + \beta|1\rangle)|00\rangle$, the first CNOT gives $\alpha|000\rangle + \beta|110\rangle$, and the second gives $\alpha|000\rangle + \beta|111\rangle$.

Now suppose a single bit-flip error $X$ acts on qubit 2. The state becomes

$$\alpha|010\rangle + \beta|101\rangle.$$

To diagnose the error without measuring the qubits themselves, introduce two ancilla qubits and measure the **parity observables**

$$M_1 = Z_1 Z_2, \qquad M_2 = Z_2 Z_3,$$

where $Z_i$ means the Pauli-$Z$ operator acting on qubit $i$. These are the **stabilizers** of the code. Each has eigenvalues $\pm 1$.

Compute the expectation on the error state $\alpha|010\rangle + \beta|101\rangle$:

- $M_1 = Z_1 Z_2$: qubit 1 and qubit 2 have different $z$-eigenvalues in every term, so $\langle M_1\rangle = -1$.
- $M_2 = Z_2 Z_3$: qubit 2 and qubit 3 differ in every term, so $\langle M_2\rangle = -1$.

The **syndrome** is $(M_1, M_2) = (-1, -1)$.

The full syndrome table:

| Error | Syndrome $(M_1, M_2)$ | Correction |
|-------|----------------------|------------|
| None  | $(+1, +1)$           | $I$        |
| $X_1$ | $(-1, +1)$          | $X_1$      |
| $X_2$ | $(-1, -1)$          | $X_2$      |
| $X_3$ | $(+1, -1)$          | $X_3$      |

Four outcomes; four unambiguous diagnoses. Notice what was measured: not $|\psi\rangle$, not $\alpha$ or $\beta$, but only the parity structure of errors. The encoded amplitudes $\alpha$ and $\beta$ appear in every row and every column of the syndrome table — they are invisible to the measurement. Apply the correction ($X_2$ for the case above) and the logical state is restored.

The syndrome measurement commutes with the logical $\bar Z = Z_1 Z_2 Z_3$ and $\bar X = X_1 X_2 X_3$ operators. Measuring the syndrome gives no information about the logical state.

### The phase-flip code

Bit-flip codes correct $X$ errors. To correct $Z$ errors, work in the $X$ basis. Define

$$|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

The phase-flip code encodes

$$|\bar 0\rangle = |{+}{+}{+}\rangle, \qquad |\bar 1\rangle = |{-}{-}{-}\rangle.$$

A $Z$ error on qubit $i$ flips the sign on that qubit's $|\pm\rangle$ state, which is a bit flip in the $X$ basis. The stabilizers are $X_1 X_2$ and $X_2 X_3$; the syndrome table is structurally identical to the bit-flip code's but in the dual basis.

### The 9-qubit Shor code

In 1995, Shor combined the two codes by concatenation: use the phase-flip code to protect against $Z$ errors, and use the bit-flip code to protect against $X$ errors, nesting one inside the other [verify: Shor 1995, Phys. Rev. A 52, R2493].

The encoding is:

$$|\bar 0\rangle = \frac{1}{2\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr)^{\otimes 3},$$

$$|\bar 1\rangle = \frac{1}{2\sqrt{2}}\bigl(|000\rangle - |111\rangle\bigr)^{\otimes 3}.$$

Nine physical qubits encode one logical qubit. The code corrects an arbitrary single-qubit error — any combination of $X$, $Y$, and $Z$ — because the outer level corrects $Z$ errors and the inner level corrects $X$ errors. $Y = iXZ$ is corrected by both layers simultaneously.

The Shor code is not optimal — better codes use fewer qubits for the same protection — but it is the first existence proof. Quantum error correction is possible.

### Stabilizer codes: the general framework

The stabilizer formalism, developed by Gottesman in his 1997 Caltech PhD thesis [verify: Gottesman 1997, quant-ph/9705052], gives a unified language for all the codes above and for much more powerful constructions.

A **stabilizer code** $\mathcal{C}$ is defined by an abelian subgroup $\mathcal{S}$ of the $n$-qubit Pauli group. The code space is

$$\mathcal{C} = \{|\psi\rangle : s|\psi\rangle = |\psi\rangle \text{ for all } s \in \mathcal{S}\}.$$

Every element of $\mathcal{S}$ has $|\psi\rangle$ as a $+1$ eigenstate. An error $E$ either commutes with every $s \in \mathcal{S}$ (and is undetectable) or anti-commutes with at least one stabilizer (and is detectable — measuring that stabilizer returns $-1$, flagging the error without collapsing the code space).

The code is characterized by three numbers $[\![n, k, d]\!]$:

- $n$: physical qubits in the code
- $k$: logical qubits encoded ($k = n - |\mathcal{S}|$ where $|\mathcal{S}|$ is the number of independent generators)
- $d$: **code distance** — the minimum weight of a Pauli operator that acts non-trivially on the logical space and is not detected

The code corrects any error of weight up to $t = \lfloor(d-1)/2\rfloor$.

The 3-qubit bit-flip code is $[\![3,1,1]\!]$: 3 physical qubits, 1 logical qubit, distance 1. It detects single-qubit errors but can only correct them because the syndrome is unambiguous (the errors are assumed to have weight at most 1). The Shor code is $[\![9,1,3]\!]$: distance 3, correcting any single-qubit error.

**The stabilizer formalism is where "error correction" becomes algebraically tractable.** Instead of tracking $2^n$-dimensional state vectors, track the $n-k$ generators of $\mathcal{S}$ — a polynomial description. Simulating a stabilizer code on a classical computer is efficient.

### The surface code

The **surface code** (Kitaev 1997/2003 [verify: Kitaev 2003, Ann. Phys. 303, 2]; Fowler et al. 2012 [verify: Fowler et al. 2012, Phys. Rev. A 86, 032324]) is a $[\![d^2 + (d-1)^2, 1, d]\!]$ code, approximately $[\![2d^2, 1, d]\!]$ for large $d$.

The geometry is a $d \times d$ array of **data qubits** at the vertices of a square lattice, with **syndrome qubits** at the centers of faces and edges. Two types of stabilizers are measured:

- **$X$-stabilizers** (plaquette operators): $X$ acting on the four data qubits around a square face. Detects $Z$ errors.
- **$Z$-stabilizers** (star operators): $Z$ acting on the four data qubits surrounding a vertex. Detects $X$ errors.

Every stabilizer involves only nearest-neighbor qubits, which is the feature that makes the surface code compatible with 2D chip architectures. No long-range connectivity is needed.

**Code distance intuition:** A logical $\bar X$ operator is a chain of $X$ operators running across the code from one boundary to the opposite. A logical $\bar Z$ runs top-to-bottom. An error becomes undetectable only if it forms a chain connecting opposite boundaries — a chain of length $d$. Below threshold, the probability of $d$ simultaneous errors drops faster than the gain from increasing $d$, so larger codes perform better. Above threshold, it does not.

The surface code threshold is approximately

$$p_{\text{th}} \approx 1\%$$

— high enough that current hardware can approach it. Concatenated codes achieve thresholds around $10^{-4}$ to $10^{-5}$, which is why the surface code displaced them as the practical target.

The logical error rate for a distance-$d$ surface code at physical error rate $p$ scales as

$$\boxed{p_L \approx A\left(\frac{p}{p_{\text{th}}}\right)^{\lceil(d+1)/2\rceil}}$$

where $A$ is a constant of order 0.1. For $p < p_{\text{th}}$, each increase in $d$ by 2 suppresses $p_L$ by another factor of $(p/p_{\text{th}}) < 1$. The code gets better as it gets bigger.

### Fault tolerance: the harder problem

Error correction detects and reverses errors on data qubits. But the syndrome measurement circuit itself uses ancilla qubits and gates — and those can have errors too. A single ancilla error during syndrome extraction can propagate through the circuit and affect multiple data qubits. If two data qubits are flipped, a distance-3 code that can only correct one error will fail.

**Fault tolerance** is the additional requirement that single errors in the syndrome circuit cause at most one logical error. This demands careful ancilla circuit design: ancillas should not interact with more data qubits than the code can correct. Shor's 1996 construction (Proc. 37th FOCS) was the first proof that fault-tolerant computation is achievable [verify: Shor 1996, FOCS].

The distinction matters in practice. A quantum code might be an excellent error-correcting code but fail to be fault-tolerant because its syndrome extraction circuit allows error propagation. The surface code is designed so that each syndrome qubit touches exactly four data qubits — single syndrome errors propagate to at most one data-qubit error.

### The threshold theorem

The threshold theorem (proved independently by Aharonov and Ben-Or 1997/1999 [verify]; Knill, Laflamme, and Zurek 1998, Science 279, 342 [verify]; Kitaev 1997) is the central theoretical result in quantum error correction:

> **There exists a threshold error rate $p_{\text{th}}$ such that, if every physical gate error rate $p < p_{\text{th}}$, fault-tolerant quantum computation can be performed on circuits of arbitrary depth with only polylogarithmic overhead in the number of logical operations.**

"Below threshold, bigger codes are better" is the intuitive statement. "Arbitrarily low logical error rate by scaling the code" is the precise statement. "The threshold is not zero" is why the result is non-trivial — you do not need perfect hardware, just good enough hardware.

The overhead is substantial. A distance-$d$ surface code requires approximately $2d^2$ physical qubits per logical qubit. To achieve a logical error rate of $10^{-15}$ (necessary for a large Shor factoring computation) at a physical error rate of $p = 0.1\%$, one needs $d \approx 25$, implying roughly 1,250 physical qubits per logical qubit. A 1,000-logical-qubit fault-tolerant computer might require 1–10 million physical qubits. Current hardware has $10^2$ to $10^3$ physical qubits. The gap is large; the timeline is contested.

### Recent experimental milestones

**Google Willow (December 2024 / Nature 2025):** Acharya et al. ran distance-3, -5, and -7 surface codes on the 105-qubit Willow superconducting processor [verify: Acharya et al. 2024, Nature 638, 920; arXiv:2408.13687]. The logical error rate was suppressed by a factor of $\Lambda = 2.14 \pm 0.02$ per unit increase in code distance by 2. The distance-7 code achieved $p_L = 0.143\% \pm 0.003\%$ per error-correction cycle and preserved quantum information $2.4 \pm 0.3\times$ longer than the best individual physical qubit. This was the first unambiguous experimental demonstration that the surface code threshold theorem works in hardware — that below-threshold scaling is not just a theorem but a measured fact. Note: this demonstrates below-threshold quantum *memory*, not yet below-threshold fault-tolerant universal *computation*.

**QuEra / Harvard / MIT (January 2026):** Bluvstein and colleagues demonstrated 96 logical qubits from 448 physical atoms on a neutral-atom array, using $[\![16,6,4]\!]$ high-rate codes [verify: QuEra/Harvard/MIT 2026, Nature]. This is the largest logical-qubit-count demonstration to date as of this writing. High-rate codes encode more logical qubits per physical qubit than the surface code (the $[\![16,6,4]\!]$ code encodes 6 logical qubits in 16 physical qubits), at the cost of smaller code distance and more complex syndrome circuits. Neutral atoms tolerate long-range connectivity, which superconducting chips do not.

**Quantinuum + Microsoft (April 2024):** 12 logical qubits on the H2 trapped-ion processor with 99.9%+ gate fidelity and error rates 800$\times$ below the corresponding physical rates, using color codes and Floquet codes. In 2025, Quantinuum's Helios processor with Microsoft demonstrated 48 logical qubits and the first fully fault-tolerant gate set with non-Clifford gates at logical error rates below physical error rates [verify: Quantinuum + Microsoft 2025].

**Milestones date quickly.** These records will be superseded before this book is in print. What will not change: the threshold theorem, the digitization of errors, and the stabilizer structure. Track current records in the literature; the framework here is durable.

---

## Worked Example: The 3-qubit bit-flip code correcting a single error

**The lesson.** We will trace the full QEC cycle — encode, error, syndrome, correct, verify — for the simplest code, showing explicitly that the encoded state is recovered without ever learning what it is.

**Setup.** The logical state is $|\bar\psi\rangle = \alpha|000\rangle + \beta|111\rangle$. A single bit-flip $X$ acts on qubit 2 (the middle qubit). The error state is

$$|\bar\psi_e\rangle = \alpha|010\rangle + \beta|101\rangle.$$

**Step 1: Prepare ancilla qubits.** Introduce two ancilla qubits in state $|0\rangle$:

$$|\Psi\rangle = |\bar\psi_e\rangle \otimes |00\rangle = (\alpha|010\rangle + \beta|101\rangle)|00\rangle.$$

**Step 2: Measure syndrome $M_1 = Z_1 Z_2$.** We implement this by a controlled-phase circuit: apply CNOT from qubit 1 to ancilla 1, then from qubit 2 to ancilla 1. This writes the parity of $(q_1, q_2)$ into ancilla 1. In the state $\alpha|010\rangle + \beta|101\rangle$, both terms have qubit 1 and qubit 2 in different $z$ eigenstates:

- Term $|010\rangle$: qubit 1 is $|0\rangle$, qubit 2 is $|1\rangle$. Parity is odd.
- Term $|101\rangle$: qubit 1 is $|1\rangle$, qubit 2 is $|0\rangle$. Parity is odd.

Both terms have the same parity, so measuring ancilla 1 returns the definite value $-1$ (odd parity) without collapsing the $(\alpha, \beta)$ superposition. Ancilla 1 reads $-1$.

**Step 3: Measure syndrome $M_2 = Z_2 Z_3$.** Similarly, write parity of $(q_2, q_3)$ into ancilla 2.

- Term $|010\rangle$: qubit 2 is $|1\rangle$, qubit 3 is $|0\rangle$. Parity is odd.
- Term $|101\rangle$: qubit 2 is $|0\rangle$, qubit 3 is $|1\rangle$. Parity is odd.

Ancilla 2 also reads $-1$.

**Step 4: Look up the syndrome.** Syndrome $(-1, -1)$ means error on qubit 2.

**Step 5: Apply correction.** Apply $X_2$ to qubit 2:

$$X_2|\bar\psi_e\rangle = X_2(\alpha|010\rangle + \beta|101\rangle) = \alpha|000\rangle + \beta|111\rangle = |\bar\psi\rangle.$$

The logical state is restored. The values $\alpha$ and $\beta$ were never measured, never read, never disturbed. The syndrome told us *where* the error was, not *what* the qubit is.

**The limit.** This code corrects single bit-flip errors. If two qubits are flipped simultaneously (say qubits 1 and 3 both flip), the syndrome is $(M_1, M_2) = (+1, -1)$, pointing to a single $X$ error on qubit 3. We apply $X_3$ — but the actual errors were on qubits 1 and 3. The correction makes things worse. A $[\![3,1,1]\!]$ code that sees two errors fails. That is why code distance matters, and why the surface code uses large $d$.

---

## Common Misconceptions

**"QEC corrects all errors."** No. A code of distance $d$ corrects errors of weight up to $\lfloor(d-1)/2\rfloor$. Higher-weight error bursts — more simultaneous errors than the code can handle — still fail the code. The threshold theorem says that below $p_{\text{th}}$, the probability of a high-weight error burst is so small that larger codes make things better, not worse. Above threshold, higher-weight error bursts become probable enough that larger codes actually perform worse.

**"Syndrome measurement reads out the logical qubit."** It does not. Syndrome operators commute with all logical operators by construction. Measuring a syndrome gives information about which error occurred, never about the logical state. This is the whole point of the stabilizer construction.

**"Below-threshold means we're done."** Below-threshold means the logical error rate decreases as code size grows. It does not mean the logical error rate is already small enough for a target computation. Achieving $p_L = 10^{-15}$ requires large $d$, large qubit counts, and fast classical decoders running in real time. The overhead is enormous. Google Willow demonstrated below-threshold operation in a quantum *memory*; below-threshold fault-tolerant *computation* requires transversal logical gates and magic state distillation, which have not yet been demonstrated at the same scale.

**"The surface code threshold is the only threshold."** Different codes have different thresholds. Concatenated codes have thresholds around $10^{-4}$ to $10^{-5}$ — much lower than the surface code's $\approx 1\%$. The surface code's high threshold comes from its structure: only nearest-neighbor interactions, large physical threshold at the cost of lower encoding rate (one logical qubit per $2d^2$ physical qubits). Higher-rate codes like $[\![16,6,4]\!]$ (QuEra) trade code distance and threshold for a better encoding efficiency.

**"'Beyond break-even' means the logical qubit is good enough."** Two groups used this phrase to mean different things. Sivak et al. (Yale, 2023, using cat qubits in a cavity) demonstrated a logical qubit whose lifetime exceeded the best component physical qubit by $2.3\times$ — a genuine lifetime improvement. Acharya et al. (Google Willow, 2024) demonstrated a logical qubit beating the best physical qubit lifetime *while also* showing correct below-threshold scaling. Both are meaningful. Neither is "close enough for Shor's algorithm." The practical target is logical error rates below $10^{-12}$ or smaller, orders of magnitude below what any current experiment achieves.

**"Fault tolerance is the same as error correction."** Error correction detects and reverses errors on data qubits. Fault tolerance is the additional guarantee that errors *in the syndrome circuit itself* do not cascade. A code can be error-correcting but not fault-tolerant if its ancilla circuit propagates single errors to multiple data-qubit errors. The surface code is designed so syndrome qubits touch at most four data qubits — single ancilla errors can cause at most one data-qubit error, which the code can still correct.

---

## Exercises

### Warm-up

**1.** *[Tests: digitization of errors; Pauli basis]* Any $2\times 2$ complex matrix can be written as a linear combination of $\{I, X, Y, Z\}$. Show that the "small rotation" error $E = \cos\epsilon \cdot I + i\sin\epsilon \cdot X$ (a small $X$-rotation by angle $\epsilon$) is already in this form. For small $\epsilon$, this error has probability $\approx\epsilon^2$ of causing an $X$ error and probability $\approx 1 - \epsilon^2$ of leaving the qubit unchanged. Explain why a code that corrects $X$ errors corrects this continuous rotation error too, even though the error is not exactly $X$.

**2.** *[Tests: syndrome computation]* For the 3-qubit bit-flip code with state $|\bar\psi\rangle = \alpha|000\rangle + \beta|111\rangle$, compute the syndrome $(M_1, M_2)$ for each of the four cases: no error, $X_1$ error, $X_2$ error, $X_3$ error. Write out the error state explicitly in each case, compute the eigenvalue of $Z_1Z_2$ and $Z_2Z_3$ for each term, and verify that both terms in the superposition give the same eigenvalue (so the syndrome is definite). Confirm the syndrome table in the chapter.

**3.** *[Tests: no-cloning constraint; QEC strategy]* The classical 3-bit repetition code copies a bit three times and uses majority vote. Explain in one paragraph why this strategy cannot be applied directly to qubits (invoke the no-cloning theorem precisely). Then explain what QEC does instead — what is measured, and what information it extracts.

### Application

**4.** *[Tests: threshold scaling formula; ordering of logical error rates]* The surface code logical error rate scales as $p_L \approx A(p/p_{\text{th}})^{\lceil(d+1)/2\rceil}$ with $p_{\text{th}} \approx 0.01$ and $A = 0.1$. (a) For physical error rate $p = 0.002$, compute $p_L$ for $d = 3, 5, 7$. (b) For $p = 0.02$, compute $p_L$ for the same distances. (c) At which value of $p$ do the $d = 3$ and $d = 5$ curves cross? What does this crossing represent physically?

**5.** *[Tests: stabilizer formalism; code distance]* The $[\![5,1,3]\!]$ code (the smallest code correcting any single-qubit error) has stabilizers $XZZXI$, $IXZZX$, $XIXZZ$, $ZXIXZ$. (a) Verify that these four operators commute pairwise. (b) An $X_1$ error occurs. Show that it anti-commutes with at least one stabilizer, so the error is detectable. (c) What is the code distance, and how many errors does it correct?

**6.** *[Apply+: Google Willow result]* Acharya et al. (2024) report a suppression factor $\Lambda = 2.14$ per unit increase in code distance by 2. The threshold scaling formula predicts $\Lambda \approx p_{\text{th}}/p$ where $p$ is the physical error rate. (a) Use $\Lambda = 2.14$ and $p_{\text{th}} = 0.01$ to estimate the effective physical error rate on Willow. (b) The distance-7 code achieved $p_L = 0.143\%$ per cycle. Use the formula $p_L \approx A(p/p_{\text{th}})^4$ (since $\lceil(7+1)/2\rceil = 4$) and your estimated $p$ to find $A$. (c) Using these parameters, what distance $d$ would be needed to achieve $p_L = 10^{-6}$?

### Synthesis

**7.** *[Produce: write a syndrome circuit]* Design the syndrome measurement circuit for the 3-qubit bit-flip code. The circuit uses 5 qubits total: 3 data qubits in the state $\alpha|000\rangle + \beta|111\rangle$ and 2 ancilla qubits in $|0\rangle$. Write the sequence of gates (in terms of CNOTs and measurements) that extracts $M_1 = Z_1Z_2$ and $M_2 = Z_2Z_3$ into the ancilla qubits, then measures the ancillas. Verify: the ancilla measurements cannot reveal $\alpha$ or $\beta$. Why does this circuit implement syndrome measurement without collapsing the logical state?

**8.** *[Apply+: the Shor code structure]* The 9-qubit Shor code encodes $|\bar 0\rangle = \frac{1}{2\sqrt{2}}(|000\rangle + |111\rangle)^{\otimes 3}$ and $|\bar 1\rangle = \frac{1}{2\sqrt{2}}(|000\rangle - |111\rangle)^{\otimes 3}$. (a) Identify which part of the encoding corrects $X$ errors (bit flips) and which corrects $Z$ errors (phase flips). (b) The $Z$ stabilizers of the inner code are $Z_1Z_2$, $Z_2Z_3$, $Z_4Z_5$, $Z_5Z_6$, $Z_7Z_8$, $Z_8Z_9$. Write down the $X$ stabilizers for the outer level. (c) Show that a $Y_1 = iX_1Z_1$ error is corrected by the code.

---

## Still Puzzling

**The overhead problem.** The threshold theorem guarantees that logical error rates can be made arbitrarily small, but at a cost: roughly $2d^2$ physical qubits per logical qubit. For a 1,000-logical-qubit fault-tolerant quantum computer running Shor's algorithm at a target logical error rate of $10^{-15}$, the required code distance is approximately $d \approx 25$, meaning $\sim 1,250$ physical qubits per logical qubit — about 1.25 million physical qubits total. As of early 2026, the largest quantum processors have around $10^3$ qubits. The question is not whether fault-tolerant quantum computation is possible in principle; it is whether the overhead can be reduced sufficiently and the hardware scaled sufficiently to make it practical.

**Quantum LDPC codes.** The surface code's overhead scales as $O(d^2)$ physical qubits per logical qubit. Recent constructions — quantum low-density parity-check (qLDPC) codes — achieve constant encoding rate with linear distance, meaning the overhead per logical qubit can in principle be $O(\log n)$ rather than $O(d^2)$ [contested: these constructions are mathematically proven but have not yet been demonstrated experimentally at scale, and their connectivity requirements are challenging for planar architectures]. Multiple groups began investigating these experimentally in 2024–2026. Whether they can be implemented on hardware with realistic connectivity constraints is an active research question.

**Classical decoding latency.** Real-time syndrome decoding is a bottleneck that the threshold theorem analysis often ignores. The syndrome extraction cycle takes microseconds; the classical decoder must keep up. Minimum-weight perfect matching (MWPM) runs in roughly $O(n \log n)$ per syndrome cycle but requires FPGA or GPU acceleration at scale. Neural-network decoders are faster but require training. The effective logical clock rate — how fast fault-tolerant operations can actually run — is limited by the classical decoder, not just the hardware.

---

## The +1 — Simulation Exercise

You will build an interactive surface-code threshold simulator in D3.js that makes the threshold theorem visible: push the physical error rate above and below the crossing point, and watch the logical error rate curves for $d = 3, 5, 7$ switch order.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md:

Chapter 10 — Error and the Threshold Theorem
Deliverable: 10-surface-code-threshold.html
Status: in progress

The simulation has two panels:

Panel A — Surface-code threshold plot (700 × 500 SVG).
- x-axis: physical error rate p in [0.0001, 0.05], log scale.
- y-axis: logical error rate p_L, log scale.
- Three curves: d = 3, d = 5, d = 7. Each uses
    p_L = A * (p / p_th)^( ceil((d+1)/2) )
  with p_th = 0.01 and A = 0.1.
- Vertical dashed red line at p = p_th.
- A draggable vertical cursor that shows the current p value
  and reads out p_L(d=3), p_L(d=5), p_L(d=7) in a sidebar.
- When the cursor is to the left of p_th, the d=7 curve is lowest
  (below threshold: bigger is better).
- When the cursor is to the right, the d=7 curve is highest
  (above threshold: bigger is worse).
- Horizontal reference lines at p_L = 10^-3, 10^-6, 10^-9, 10^-12.

Panel B — 3-qubit bit-flip code visualizer (700 × 350 SVG).
- Displays three qubits as circles. Each qubit can be in state
  |0>, |1>, or superposition (shown as a Bloch sphere projection
  on the qubit circle, with North = |0>, South = |1>).
- Syndrome qubits M1 (between q1 and q2) and M2 (between q2 and q3)
  shown as diamond shapes.
- Error injection: radio buttons to inject X error on qubit 1, 2, 3,
  or no error.
- Step-by-step button sequence:
  1. "Encode": starts from |psi> = alpha|0> + beta|1> (sliders for alpha,
     beta angles), shows the encoded state alpha|000> + beta|111>.
  2. "Apply error": the selected qubit's display changes to show the
     flipped state.
  3. "Measure syndrome": M1 and M2 diamonds light up with their +1/-1
     eigenvalues, shown as colored (green = +1, red = -1).
  4. "Correct": the correct qubit is X-flipped back, its display
     reverts to the encoded-state visualization.
  5. "Verify": a checkmark confirms the state alpha|000> + beta|111>
     is restored.
- Text narration below each step: one sentence explaining what just
  happened physically.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md:

ERROR CORRECTION PHYSICS RULES

1. The logical error rate formula:
     p_L(d, p) = A * (p / p_th)^( ceil((d+1) / 2) )
   with p_th = 0.01 and A = 0.1.
   Use Math.ceil((d+1)/2) for the exponent.
   Display p_L to three significant figures.

2. The threshold p_th = 0.01 is the approximate surface code threshold
   for a standard depolarizing noise model. In the Acharya et al. 2024
   experiment, the measured suppression factor Lambda = 2.14 implies an
   effective p/p_th ≈ 1/2.14 ≈ 0.47, meaning p ≈ 0.0047 — below the
   threshold. Mark this point on the plot.

3. The three-qubit bit-flip code has syndromes:
     No error:  M1 = +1, M2 = +1
     X on q1:   M1 = -1, M2 = +1
     X on q2:   M1 = -1, M2 = -1
     X on q3:   M1 = +1, M2 = -1
   Store this as a lookup table; do not derive on the fly.

4. The encoded state is alpha|000> + beta|111>. Never display or compute
   alpha or beta from syndrome measurements — the syndromes are
   independent of them. If your simulator needs to display alpha and beta,
   use only the sliders (the input), not the syndrome output.

KNOWN FAILURE MODES:
(a) p_L curve rendered in linear scale instead of log-log.
    Use d3.scaleLog() for both axes.
(b) Threshold line drawn at the wrong position. p_th = 0.01 corresponds
    to x = 0.01 in the log scale. Verify visually.
(c) Syndrome lookup table indexed wrong (off-by-one in qubit numbering).
    Test: inject X on q2, confirm syndrome (-1, -1).
(d) Bloch sphere projection on the qubit circle needs a 2D orthographic
    projection, not a 3D library.
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three files first.

Build 10-surface-code-threshold.html: a single self-contained HTML file
using D3 v7 from a CDN, no other dependencies.

The page has two panels stacked vertically.

PANEL A — Threshold plot.
SVG 700 x 500. Log-log plot of logical error rate vs. physical error rate.
x-axis: p in [0.0001, 0.05]. y-axis: p_L in [1e-20, 1].
Three curves: d = 3, 5, 7. Formula: p_L = 0.1 * (p/0.01)^ceil((d+1)/2).
Curves labeled at the right margin.
Vertical dashed red line at p = 0.01 (threshold). Label "p_th".
A filled circle on the plot at (p_eff = 0.0047, p_L_meas = 0.00143)
labeled "Willow d=7 (Acharya et al. 2024)".
A draggable cursor (vertical line) initialized at p = 0.005.
Sidebar to the right (200 px wide): shows the current p value and reads
p_L for d = 3, 5, 7 at that p. Highlights the smallest value in green
(below threshold: d=7 is best) or the largest in red (above threshold).

PANEL B — 3-qubit code visualizer.
SVG 700 x 350. Horizontal layout with qubit circles and syndrome diamonds.
Three data qubit circles (q1, q2, q3) labeled. Between q1-q2: syndrome
diamond M1; between q2-q3: syndrome diamond M2.
Control panel below:
- Alpha/beta sliders: theta in [0, pi/2] where
    alpha = cos(theta), beta = sin(theta).
  Show alpha and beta as decimal numbers next to the sliders.
- Error selector: radio buttons for "No error", "X on q1",
  "X on q2", "X on q3".
- Five step buttons in order: Encode, Apply Error, Measure Syndrome,
  Correct, Verify.
- Text narration field below: one sentence updated per step.

Step behavior:
1. Encode: color qubits blue, display "α|000⟩ + β|111⟩".
2. Apply Error: if error selected, flip the chosen qubit's color to red.
   Narration: "Qubit N was bit-flipped by an X error."
3. Measure Syndrome: compute M1, M2 from the lookup table (CLAUDE.md
   rule 3). Color M1 and M2 green (+1) or red (-1).
   Narration: "Syndrome (M1, M2) = (val1, val2) → error on qubit N."
4. Correct: apply X to the identified qubit; return its color to blue.
   Narration: "Applied X correction to qubit N."
5. Verify: display "✓ State restored: α|000⟩ + β|111⟩".
   Narration: "The encoded state is recovered. α and β were never read."

Sanity checks (console):
- At p = p_th, all three p_L curves should pass through 0.1 (= A).
- At p = 0.001, confirm p_L(d=7) < p_L(d=5) < p_L(d=3).
- At p = 0.05, confirm the ordering reverses.
- Syndrome table: inject each error type and verify the correct syndrome.
```

### Part 4 — Exploration tasks

1. Open the simulation. Set the cursor to $p = 0.001$. Read off $p_L$ for $d = 3, 5, 7$. Confirm that the $d = 7$ curve gives the smallest logical error rate. Move the cursor to $p = 0.05$. Confirm the order reverses. What does this reversal mean physically?

2. Drag the cursor to the crossing point of the $d = 5$ and $d = 7$ curves. What physical error rate does this correspond to? Compare it to the theoretical threshold $p_{\text{th}} = 0.01$.

3. Find the Willow data point on the plot (Acharya et al. 2024, $d = 7$). Read the plot's predicted $p_L$ for the curve at the Willow effective error rate $p \approx 0.0047$. Does the formula match the measured $p_L = 0.143\%$?

4. In Panel B, set $\theta = \pi/4$ (so $\alpha = \beta = 1/\sqrt{2}$). Inject an $X$ error on qubit 2. Step through Encode → Apply Error → Measure Syndrome → Correct → Verify. Note: the narration at the "Verify" step says $\alpha$ and $\beta$ were never read. Explain why this is true from the structure of the syndrome measurement.

5. Inject an $X$ error on qubit 1. Compare the syndrome to the qubit-2 error case. Can you distinguish "qubit 1 was flipped" from "qubit 2 was flipped" using only the syndrome? What would happen if two qubits were simultaneously flipped?

---

## References

- Wootters, W.K. and Zurek, W.H. "A single quantum cannot be cloned." *Nature* 299, 802–803 (1982). [verify]
- Dieks, D. "Communication by EPR devices." *Phys. Lett. A* 92, 271–272 (1982). [verify]
- Shor, P.W. "Scheme for reducing decoherence in quantum computer memory." *Phys. Rev. A* 52, R2493 (1995). [verify]
- Shor, P.W. "Fault-tolerant quantum computation." *Proc. 37th Annual Symposium on Foundations of Computer Science (FOCS)*, 56–65 (1996). [verify]
- Knill, E., Laflamme, R. and Zurek, W.H. "Resilient quantum computation: error models and thresholds." *Science* 279, 342–345 (1998). [verify]
- Aharonov, D. and Ben-Or, M. "Fault-tolerant quantum computation with constant error rate." *SIAM J. Comput.* 38, 1207–1282 (2008). [verify: based on 1997/1999 preprints]
- Gottesman, D. "Stabilizer codes and quantum error correction." PhD thesis, California Institute of Technology (1997). arXiv:quant-ph/9705052. [verify]
- Kitaev, A.Yu. "Fault-tolerant quantum computation by anyons." *Annals of Physics* 303, 2–30 (2003). [verify]
- Fowler, A.G., Martinis, J.M. et al. "Surface codes: towards practical large-scale quantum computation." *Phys. Rev. A* 86, 032324 (2012). [verify]
- Knill, E. and Laflamme, R. "Theory of quantum error-correcting codes." *Phys. Rev. A* 55, 900 (1997). [verify]
- Acharya, R. et al. (Google Quantum AI). "Suppressing quantum errors by scaling a surface code logical qubit." *Nature* 614, 676–681 (2023). [verify]
- Acharya, R. et al. (Google Quantum AI). "Quantum error correction below the surface code threshold." *Nature* 638, 920–926 (2025; announced December 2024). arXiv:2408.13687. [verify]
- Sivak, V.V. et al. (Yale). "Real-time quantum error correction beyond break-even." *Nature* 616, 50–55 (2023). [verify]
- Bluvstein, D. et al. (QuEra/Harvard/MIT). "Logical quantum processor based on reconfigurable atom arrays." *Nature* 626, 58–65 (2024). [verify]
- QuEra/Harvard/MIT. "96 logical qubits from 448 atoms." *Nature* (January 2026). [verify: citation details not fully confirmed at writing]
- Quantinuum + Microsoft. "Demonstration of 12 logical qubits at 99.9%+ fidelity on H2." (April 2024). [verify: formal publication details]
- Quantinuum Helios + Microsoft. "Fault-tolerant gate set with 48 logical qubits." (2025). [verify: formal publication details]
