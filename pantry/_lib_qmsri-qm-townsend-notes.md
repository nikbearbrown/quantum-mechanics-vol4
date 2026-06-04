<!--
    00-frontmatter.md
    FRONT MATTER — everything before Chapter 1: title page, copyright,
    dedication, preface. Unnumbered; roman numerals in print.
-->

# Quantum Mechanics II

### A Graduate Course — From Formalism to Atoms, Molecules, and Spin

**Adrian E. Feiguin**

*Department of Physics, Northeastern University*

*Course PHYS 5125*

*Edited by Gregory A. Fiete · Series editor: Nik Bear Brown*

---

## Copyright

Copyright © 2026 Adrian E. Feiguin. All rights reserved.

Published by Humanitarians AI, a 501(c)(3) nonprofit organization, as part of the **Medhavy** intelligent-textbook series. Edited by Gregory A. Fiete; series editor Nik Bear Brown.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law, and except as expressly permitted under the license stated in `LICENSE.md`.

This book was typeset from Prof. Feiguin's handwritten PHYS 5125 lecture notes. Equations were transcribed into LaTeX and checked against the original page images; remaining errata are tracked openly (see the project repository) and corrected between editions.

ISBN: [INSERT ISBN]

First edition: 2026

---

## Dedication

*For the students of PHYS 5125 — who learned this material the way it was meant to be learned: by working every problem to the end.*

---

## Preface

This book began as chalk and ink. For years the second semester of graduate quantum mechanics at Northeastern was taught the way most of us first learned it — at the board, one line of algebra at a time, with a stack of handwritten notes that grew thicker each time the course was offered. This volume is those notes, set in type. The derivations are unchanged. What we have added is legibility, cross-references, and a structure a reader can navigate without sitting in the lecture hall.

We wrote it because the second course in quantum mechanics occupies an awkward place on the shelf. The first course is well served by a dozen excellent texts; by the time a student reaches the second, the books tend to split into two camps. One camp is encyclopedic — thorough, authoritative, and far too long to carry a one-semester course. The other is so terse that the student is left to reconstruct every missing step alone. The notes a working instructor actually teaches from live in between: complete enough to follow, compact enough to finish. That middle is what we have tried to preserve here.

The organizing conviction of the book is that the second semester of quantum mechanics is, more than anything, a course in *approximation*. Almost nothing beyond the hydrogen atom can be solved exactly, and the physicist's real craft is knowing which approximation a problem invites — perturbation theory when a small parameter is genuinely small, the variational method when it is not, the sudden and adiabatic limits at the two ends of the clock. Once those tools are in hand, the same machinery resolves the spectrum of helium, the bonding of the hydrogen molecule, the fine structure of atomic lines, and the physics of a spin in a slowly turning field. We have tried throughout to keep the machinery visible: to show the calculation on the page rather than quote its result.

The book assumes a first graduate course in quantum mechanics — Hilbert spaces, the Schrödinger equation, angular momentum — and a working fluency with linear algebra and the calculus of several variables. Chapter 1 reviews the formalism quickly, not to teach it for the first time but to fix notation and to make the rest of the book self-contained. We make no attempt at completeness: scattering theory, the Dirac equation, and the quantization of fields belong to other courses and other books, and we say so where the boundary falls.

Our debt is plainest in the worked examples, which are the examples we have actually assigned, and in the students who found the errors that earlier drafts contained. A textbook is a conversation that outlives the semester. We hope this one is useful well past it.

*A. E. F.*
*Boston, 2026*
# Chapter 1 — The Formalism of Quantum Mechanics

*Linear algebra in a physicist's costume: vectors that are states, matrices that are measurements.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Strip away the physical names and this chapter is plain linear algebra. A quantum state is a vector in a complex inner-product space — a Hilbert space — and Dirac's bra–ket notation is just bookkeeping for column vectors, row vectors, and the inner products between them. Every measurable quantity is a Hermitian operator, i.e. a matrix that equals its own conjugate transpose. The physics enters through a short list of demands placed on this machinery, and the rest follows mechanically.

What does the formalism optimize for? Consistency between two requirements: measurement outcomes must be real numbers, and total probability must stay fixed at one. Hermiticity guarantees real eigenvalues and an orthonormal eigenbasis; unitary evolution preserves the norm. Diagonalize an operator and you simultaneously read off the possible measured values (eigenvalues) and the states that yield them with certainty (eigenvectors).

The trade-off is sharp. Because non-commuting operators share no common eigenbasis, you cannot make every observable definite at once — the uncertainty relation $\sigma_A \sigma_B \geq |\langle[\hat{A},\hat{B}]\rangle/2i|$ is a theorem, not an assumption. The same commutator algebra that constrains position and momentum also generates angular momentum and forces its eigenvalues onto a discrete ladder. The lesson worth holding onto: nearly everything here is one algebraic structure, eigenvalue problems and commutators, wearing physical clothing.

## 1. Review: The Formalism of quantum mechanics

## 1.1 Hilbert spaces and Dirac notation

In cartesian coordinates, any vector is written as a sum of unit vectors that make up an orthogonal basis

$$\vec{v} = v_1 \hat{e}_1 + v_2 \hat{e}_2 + v_3 \hat{e}_3$$

where

$$\hat{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \hat{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \hat{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

The coefficients $v_i$ may in general be real or complex; here we keep them real for the moment. By the definition of the inner ("dot") product, $(\vec{u}, \vec{v}) = \vec{u} \cdot \vec{v} = |u||v| \cos\theta$

$$(\hat{e}_i, \hat{e}_j) = \hat{e}_i \cdot \hat{e}_j = \delta_{ij} \quad \text{(they are orthogonal)}$$

$$(\vec{v}, \hat{e}_i) = \vec{v} \cdot \hat{e}_i = v_i \quad \text{(projection along } \hat{e}_i\text{)}$$

$$(\vec{v}, \vec{v}) = \vec{v} \cdot \vec{v} = \sum_i v_i^2 > 0$$

The norm is defined as $v = \sqrt{|\vec{v}|^2} = \sqrt{(\vec{v}, \vec{v})}$

**Hilbert space:**

- the coefficients are complex numbers
- It can have infinite dimensions / basis vectors

$$(\vec{u}, \vec{v}) = \sum_i u_i^* v_i$$

$$(\vec{v}, \vec{u}) = (\vec{u}, \vec{v})^* \quad \Rightarrow \quad (\vec{u}, \vec{u}) \text{ is real!}$$

$$\Rightarrow \quad |\vec{u}| = \sqrt{(\vec{u}, \vec{u})} \in \mathbb{R} \geq 0$$

**Dirac notation:**

- A system's state is completely specified by its **state vector** $|\psi\rangle \in \mathcal{H}$

- State vectors are acted on, and transformed, by linear operators

$$|\psi\rangle = \sum_i \psi_i |\alpha_i\rangle \quad \Rightarrow \quad |\psi\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix}$$

$d$: dimension of $\mathcal{H}$

$$|\alpha_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}; \quad |\alpha_2\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}; \quad \cdots \quad |\alpha_d\rangle = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

$|\alpha_i\rangle$ form an orthonormal basis

**Example:** two-level system $(d = 2)$

$$|1\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}; \quad |2\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

An arbitrary state is then written as

$$|\psi\rangle = \psi_1 |1\rangle + \psi_2 |2\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$$

with $\psi_1, \psi_2 \in \mathbb{C}$

A Hilbert space is a vector space, so any linear combination of states is again a member of $\mathcal{H}$

$$\alpha |\phi\rangle + \beta |\psi\rangle \in \mathcal{H}$$

**"Dual" Hilbert space**

$$|\psi\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix} \quad \rightarrow \quad \langle\psi| = \begin{pmatrix} \psi_1^*, \psi_2^*, \ldots, \psi_d^* \end{pmatrix}$$

Algebraically, $|\psi\rangle$ is a column vector,

while $\langle\psi|$ is the row vector obtained as its conjugate transpose

**Inner product:**

$$\langle\psi|\varphi\rangle = \sum_{i=1}^{d} \psi_i^* \varphi_i = \begin{pmatrix} \psi_1^* \cdots \psi_d^* \end{pmatrix} \begin{pmatrix} \varphi_1 \\ \varphi_2 \\ \vdots \\ \varphi_d \end{pmatrix} \in \mathbb{C}$$

$\langle\psi|$ is the "bra" and $|\varphi\rangle$ is the "ket", $\langle\psi|\varphi\rangle$ is a "braket".

The coefficients $\psi_i$ now have a clear meaning:

$$\langle\alpha_i|\psi\rangle = \langle\alpha_i|\left(\sum_j \psi_j |\alpha_j\rangle\right)$$

$$= \sum_j \psi_j \langle\alpha_i|\alpha_j\rangle = \sum_j \psi_j \delta_{ij} = \psi_i$$

that is, the "projection" of $|\psi\rangle$ onto the "$i$-th direction", equivalently the $i$-th component of $|\psi\rangle$

The norm of $|\psi\rangle$ is $\sqrt{\langle\psi|\psi\rangle} = \sqrt{\sum_i \psi_i^* \psi_i} = \sqrt{\sum_i |\psi_i|^2}$

**Completeness**

$$\sum_{i=1}^{d} |\alpha_i\rangle\langle\alpha_i| = \mathbb{1} \quad \text{(identity operator)}$$

$$\left(\sum_i |\alpha_i\rangle\langle\alpha_i|\right)\left(\underbrace{\sum_j \psi_j |\alpha_j\rangle}_{|\psi\rangle}\right) = \sum_{ij} \psi_j |\alpha_i\rangle \underbrace{\langle\alpha_i|\alpha_j\rangle}_{\delta_{ij}} = |\psi\rangle$$

**Continuous Hilbert spaces**

Now let the index "$i$" run over a continuum, like a coordinate along the $x$-axis. We label the basis by $|x\rangle$ and express a state as

$$|\psi\rangle = \int dx\, \psi(x) |x\rangle$$

The inner product, or braket, becomes

$$\langle\psi|\varphi\rangle = \left(\int dx_1\, \psi^*(x_1) \langle x_1|\right)\left(\int dx_2\, \varphi(x_2) |x_2\rangle\right)$$

$$= \int dx_1\, dx_2\, \psi^*(x_1)\varphi(x_2) \underbrace{\langle x_1|x_2\rangle}_{\delta(x_1 - x_2)}$$

$$= \int dx\, \psi^*(x)\varphi(x)$$

The identity is now written

$$\int dx\, |x\rangle\langle x| = \mathbb{1}$$

## 1.2 Observables and operators

An operator is a mathematical map that sends one state to another

$$\hat{O}|\psi\rangle = |\varphi\rangle \quad ; \quad |\psi\rangle, |\varphi\rangle \in \mathcal{H}$$

It admits a matrix representation. In the basis $|\alpha\rangle$, the matrix elements of $\hat{O}$ are defined by

$$O_{ij} = \langle\alpha_i|\hat{O}|\alpha_j\rangle$$

$$\rightarrow \quad \langle\alpha_i|\hat{O}|\psi\rangle = \sum_j \langle\alpha_i|\hat{O}|\alpha_j\rangle\langle\alpha_j|\psi\rangle$$

$$= \sum_j O_{ij}\, \psi_j = \langle\alpha_i|\varphi\rangle = \varphi_i$$

$$\rightarrow \quad \begin{pmatrix} \varphi_1 \\ \varphi_2 \\ \vdots \\ \varphi_d \end{pmatrix} = \begin{pmatrix} O_{11} & O_{12} & \cdots & O_{1d} \\ O_{21} & O_{22} & & \vdots \\ \vdots & & \ddots & \\ O_{d1} & \cdots & & O_{dd} \end{pmatrix} \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix}$$

**Example:** two-level system $|1\rangle; |2\rangle$

Define the "occupation operators"

$$\hat{N}_1 = |1\rangle\langle 1| \quad ; \quad \hat{N}_2 = |2\rangle\langle 2|$$

$$\hat{N}_1\left(\psi_1 |1\rangle + \psi_2 |2\rangle\right) = \psi_1 |1\rangle \underbrace{\langle 1|1\rangle}_{=1} + \psi_2 |1\rangle \underbrace{\langle 1|2\rangle}_{=0}$$

$$= \psi_1 |1\rangle$$

Similarly, $\hat{N}_2|\psi\rangle = \psi_2 |2\rangle$

Notice that $\hat{N}_1 + \hat{N}_2 = \mathbb{1}$

**Matrices:** $\langle 1|\hat{N}_1|1\rangle = 1$ ; $\langle 2|\hat{N}_1|2\rangle = 0$
$\langle 1|\hat{N}_1|2\rangle = 0$

$$N_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}; \quad N_2 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}; \quad N_1 + N_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

**"Transition operators":** $S^+ = |2\rangle\langle 1|$ ; $S^- = |1\rangle\langle 2|$

$$\rightarrow \quad S^+|1\rangle = |2\rangle \quad ; \quad S^+|2\rangle = 0$$

$$S^-|2\rangle = |1\rangle \quad ; \quad S^-|1\rangle = 0$$

$$S^+|\psi\rangle = \psi_1 |2\rangle$$

**Matrices**

$$S^+ = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}; \quad S^- = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$

The same ideas carry over to continuous Hilbert spaces

$$\langle\psi|\hat{O}|\varphi\rangle = \langle\psi|\left(\hat{O}|\varphi\rangle\right) = \int dx\, \psi^*(x)\, \hat{O}\, \varphi(x)$$

**Expectation values:**

Operators stand for physical observables that an instrument can measure. For a state $|\psi\rangle$, the expectation value of $\hat{O}$ is

$$\langle\hat{O}\rangle = \langle\psi|\hat{O}|\psi\rangle =$$

$$= \sum_{ij} \psi_i^* \psi_j \langle\alpha_i|\hat{O}|\alpha_j\rangle$$

$$= \sum_{ij} \psi_i^* \psi_j\, O_{ij}$$

or $\quad \langle\hat{O}\rangle = \int dx\, \psi^*(x)\, O\, \psi(x)$

Because a measurement must yield a real number, we require $\langle O \rangle \in \mathbb{R}$ for every state $|\psi\rangle$. Equivalently:

$$\langle\hat{O}\rangle^* = \langle\psi|\hat{O}|\psi\rangle^* = \langle O\psi|\psi\rangle = \langle O \rangle$$

Operators that satisfy this condition are called **Hermitian**.

An operator $\hat{O}$ is Hermitian when it coincides with its Hermitian conjugate, $\hat{O} = \hat{O}^\dagger$, that is

$$\langle\alpha_i|\hat{O}|\alpha_j\rangle = \langle\alpha_j|\hat{O}|\alpha_i\rangle^*$$

$$\rightarrow \quad O_{ij} = (O_{ji})^* = (O^\dagger)_{ij}$$

**END LECT #1**

**Example:** two-level system

$S^+, S^-$ are **not** Hermitian, so neither can represent an observable.

The combinations $N_1, N_2, (S^+ + S^-), i(S^+ - S^-)$, on the other hand, are.

## 1.3 Change of basis (rotations)

Suppose a state is expressed in a basis $|\alpha\rangle$ as

$$|\psi\rangle = \sum_\alpha \psi_\alpha |\alpha\rangle$$

inserting a resolution of the identity gives

$$|\psi\rangle = \sum_\alpha \psi_\alpha \sum_\beta |\beta\rangle\langle\beta|\alpha\rangle$$

$$= \sum_\beta \left(\sum_\alpha \langle\beta|\alpha\rangle \psi_\alpha\right) |\beta\rangle$$

$$= \sum_\beta \left(\sum_\alpha \langle\beta|\alpha\rangle\langle\alpha|\psi\rangle\right) |\beta\rangle$$

$$= \sum_\beta \langle\beta|\psi\rangle |\beta\rangle = \sum_\beta \psi_\beta |\beta\rangle$$

with $\psi_\beta = \langle\beta|\psi\rangle = \sum_\alpha U_{\alpha\beta}^* \psi_\alpha$, having defined the transformation $U_{\alpha\beta} = \langle\alpha|\beta\rangle$. These are the projections of the $|\alpha\rangle$ states onto the $|\beta\rangle$ basis.

$$\rightarrow \quad \psi_\beta = \langle\beta|\psi\rangle = \sum_\alpha (U^\dagger)_{\beta\alpha} \psi_\alpha; \quad \psi_\alpha = \sum_\beta U_{\alpha\beta} \psi_\beta$$

$U_{\alpha\beta}$ is a unitary transformation

$$U^\dagger U = \mathbb{1} \quad \Rightarrow \quad U^\dagger = U^{-1}$$

**Matrices:**

$$\langle\beta|O|\beta'\rangle = \sum_{\alpha\alpha'} \langle\beta|\alpha\rangle\langle\alpha|O|\alpha'\rangle\langle\alpha'|\beta'\rangle$$

$$= \sum_{\alpha\alpha'} U_{\alpha\beta}^*\, U_{\alpha'\beta'}\, O_{\alpha\alpha'}$$

$$O' = U^\dagger O U \quad ; \quad O = U O' U^\dagger$$

**Example:** 2-level system

$$|\pm\rangle = \frac{1}{\sqrt{2}}\left[|1\rangle \pm |2\rangle\right] \rightarrow \begin{cases} |+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle) \\ |-\rangle = \frac{1}{\sqrt{2}}(|1\rangle - |2\rangle) \end{cases}$$

$$U_{+1} = \frac{1}{\sqrt{2}}, \quad U_{+2} = \frac{1}{\sqrt{2}}, \quad U_{-1} = \frac{1}{\sqrt{2}}, \quad U_{-2} = -\frac{1}{\sqrt{2}}$$

$$\rightarrow \quad U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \qquad \psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$$

$$\rightarrow \quad \psi' = \frac{1}{\sqrt{2}} \begin{pmatrix} \psi_1 + \psi_2 \\ \psi_1 - \psi_2 \end{pmatrix}$$

or, $|\psi\rangle = \psi_1 |1\rangle + \psi_2 |2\rangle = \frac{1}{\sqrt{2}}\left\{\psi_1(|+\rangle + |-\rangle) + \psi_2(|+\rangle - |-\rangle)\right\}$

$$= \frac{1}{\sqrt{2}}(\psi_1 + \psi_2)|+\rangle + \frac{1}{\sqrt{2}}(\psi_1 - \psi_2)|-\rangle = \psi_+ |+\rangle + \psi_- |-\rangle$$

## 1.4 The eigenvalue problem

Given an operator $\hat{O}$, its eigenstates are the states that $\hat{O}$ leaves unchanged apart from an overall scaling:

$$\hat{O}|\psi\rangle = \lambda |\psi\rangle \quad ; \quad \lambda \text{ is a scalar}$$

$|\psi\rangle$: eigenstate ; $\lambda$ is the associated eigenvalue

Rearranging this gives

$$(\hat{O} - \lambda \mathbb{1})|\psi\rangle = 0$$

In matrix form this reads

$$\begin{pmatrix} O_{11} - \lambda & O_{12} & O_{13} & \cdots & O_{1d} \\ O_{21} & O_{22} - \lambda & O_{23} & \cdots & O_{2d} \\ \vdots & O_{32} & \ddots & & \\ O_{d1} & \cdots & & & O_{dd} - \lambda \end{pmatrix} \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix} = 0$$

A non-trivial solution exists only if

$$\det(O - \lambda \mathbb{1}) = 0$$

This secular equation for $\lambda$ produces a set of solutions $\lambda_i$. With the eigenvalues in hand, the matching eigenvectors (eigenstates) follow.

**Eigenvalues of Hermitian operators:**

(i) The eigenvalues of Hermitian operators are **real**

$$\hat{O}|\psi\rangle = \lambda |\psi\rangle$$

$$\rightarrow \quad \langle\psi|\hat{O}\psi\rangle = \lambda \langle\psi|\psi\rangle$$

$$\langle O\psi|\psi\rangle = \lambda^* \langle\psi|\psi\rangle$$

But $\langle\psi|O\psi\rangle = \langle O\psi|\psi\rangle \Rightarrow \lambda = \lambda^* \in \mathbb{R}$

(ii) Two eigenstates $|\psi_1\rangle; |\psi_2\rangle$ associated to different eigenvalues $\lambda_1 \neq \lambda_2$ are **orthogonal**

$$\hat{O}|\psi_1\rangle = \lambda_1 |\psi_1\rangle \quad ; \quad \hat{O}|\psi_2\rangle = \lambda_2 |\psi_2\rangle$$

$$\langle\psi_2|\hat{O}|\psi_1\rangle = \lambda_1 \langle\psi_2|\psi_1\rangle; \quad \langle\psi_1|\hat{O}|\psi_2\rangle = \lambda_2 \langle\psi_1|\psi_2\rangle \quad (1)$$

$$\langle\psi_1|\hat{O}|\psi_2\rangle^* = \lambda_1 \langle\psi_1|\psi_2\rangle^*$$

$$\rightarrow \quad \langle\psi_1|\hat{O}|\psi_2\rangle = \lambda_1 \langle\psi_1|\psi_2\rangle \quad (2)$$

From (1) and (2) ; $\lambda_1 \langle\psi_1|\psi_2\rangle = \lambda_2 \langle\psi_1|\psi_2\rangle$

Since $\lambda_1 \neq \lambda_2 \rightarrow \langle\psi_1|\psi_2\rangle = 0$

And if $\lambda_1 = \lambda_2$ (degeneracy)? Within that subspace one can always choose a set of mutually orthogonal eigenvectors.

(iii) The eigenvectors of a Hermitian operator span the complete Hilbert space and form an orthogonal basis.

$$\hat{O}|\psi_i\rangle = \lambda_i |\psi_i\rangle \quad i = 1, 2, \ldots, d$$

**The eigenvalue problem in quantum mechanics**

When a system is prepared in an eigenstate of an operator $\hat{O}$, measuring $\hat{O}$ always returns the same value

$$\langle\psi|\hat{O}|\psi\rangle = \lambda \langle\psi|\psi\rangle$$

**Example:** two-level system

Take the operator $S^+ + S^- = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

$$\det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 \rightarrow \boxed{\lambda_\pm = \pm 1}$$

$\lambda = 1)$

$$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} \psi_{+1} \\ \psi_{+2} \end{pmatrix} = 0 \rightarrow -\psi_{+1} + \psi_{+2} = 0$$

or $\psi_{+1} = \psi_{+2}$

$$\rightarrow \quad |\psi_+\rangle = \psi_{+1}|1\rangle + \psi_{+1}|2\rangle = \psi_{+1}(|1\rangle + |2\rangle)$$

Imposing the normalization condition $\langle\psi_+|\psi_+\rangle = 1$

$$\rightarrow \quad \langle\psi_+|\psi_+\rangle = |\psi_{+1}|^2 \cdot 2 = 1 \rightarrow \psi_{+1} = \frac{1}{\sqrt{2}}$$

so that $|\psi_+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)$

$\lambda = -1)$

$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \psi_{-1} \\ \psi_{-2} \end{pmatrix} = 0 \rightarrow \psi_{-1} = -\psi_{-2}$$

$$\rightarrow \quad |\psi_-\rangle = \frac{1}{\sqrt{2}}(|1\rangle - |2\rangle)$$

Notice that $\langle\psi_+|\psi_-\rangle = 0$

## 1.5 Statistical interpretation

Measuring a physical observable $O$, represented by a Hermitian operator $\hat{O}$, on a state $|\psi\rangle$ yields an eigenvalue $\lambda_i$ with probability:

$$P(\lambda_i) = |\langle\psi_i|\psi\rangle|^2 = |\psi_i|^2$$

When that outcome occurs, the post-measurement state of the system is $|\psi_i\rangle$

$$\hat{O}|\psi\rangle \;\overset{\text{collapse}}{\longrightarrow}\; |\psi_i\rangle \qquad (O = \lambda_i)$$

The squared coefficients $|\psi_i|^2$ are thus the probabilities of finding the system in each eigenstate

$$\langle O \rangle = \langle\psi|\hat{O}|\psi\rangle = \sum_{ij} \psi_i^* \psi_j \langle\psi_i|\hat{O}|\psi_j\rangle$$

$$= \sum_{ij} \psi_i^* \psi_j\, \lambda_j \langle\psi_i|\psi_j\rangle = \sum_i \lambda_i |\psi_i|^2$$

$$= \sum_i \lambda_i\, P(\lambda_i) \qquad \text{with } \sum_i P(\lambda_i) = 1$$

In the continuum

$$|\psi\rangle = \int dx\, \psi(x) |x\rangle$$

Measuring the position operator gives

$$\hat{x}|\psi\rangle = \int dx\, \psi(x)\, \hat{x}|x\rangle = \int dx\, x\, \psi(x) |x\rangle$$

$$\hat{x}|x\rangle = x|x\rangle$$

$$\langle\psi|\hat{x}|\psi\rangle = \int dx\, dx'\, x\, \psi^*(x')\, \psi(x) \underbrace{\langle x'|x\rangle}_{\delta(x - x')}$$

$$= \int dx\, x\, \underbrace{|\psi(x)|^2}_{P(x)} = \int dx\, x\, P(x)$$

$$\rightarrow \quad P(x) = |\psi(x)|^2$$

The probability of locating the particle within $[x, x+dx]$ is

$$P(x)\, dx = |\psi(x)|^2\, dx$$

## 1.6 The generalized uncertainty principle

Measure the observable $O$ repeatedly and the outcomes spread across a histogram. The spread, and hence the precision, is captured by the standard deviation

$$\sigma_O^2 = \langle(\hat{O} - \langle O \rangle)^2\rangle = \langle\psi|(\hat{O} - \langle O \rangle)^2|\psi\rangle$$

$$= \langle(\hat{O} - \langle O \rangle)\psi\,|\,(\hat{O} - \langle O \rangle)\psi\rangle$$

Now take two observables $\hat{A}$ and $\hat{B}$. Applying the Schwartz inequality yields

$$\sigma_A^2 \sigma_B^2 = \langle(\hat{A} - \langle A \rangle)\psi\,|\,(\hat{A} - \langle A \rangle)\psi\rangle \langle(\hat{B} - \langle B \rangle)\psi\,|\,(\hat{B} - \langle B \rangle)\psi\rangle$$

$$\geq |\langle(\hat{A} - \langle A \rangle)\psi\,|\,(\hat{B} - \langle B \rangle)\psi\rangle|^2$$

A few steps of algebra then lead to the inequality

$$\sigma_A \sigma_B \geq \left|\frac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle\right| \qquad \text{(Townsend 3.5)}$$

with $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$

**END LECTURE #2**

This is a derived result of the theory, not a postulate. It sets the fundamental limit on how precisely two quantities, such as position and momentum, can be measured at once:

$$[\hat{x}, \hat{p}]\,\psi(x) = \left[x, -i\hbar\frac{d}{dx}\right]\psi(x) = -i\hbar\left[x\frac{d}{dx} - \frac{d}{dx}x\right]\psi(x)$$

$$= -i\hbar\left(x\frac{d\psi}{dx} - \psi(x) - x\frac{d\psi}{dx}\right) = i\hbar\,\psi(x)$$

$$\Rightarrow \quad [\hat{x}, \hat{p}] = i\hbar \quad \rightarrow \quad \sigma_x \sigma_p \geq \frac{\hbar}{2}$$

The same relation applies to any pair of non-commuting operators, $[\hat{A}, \hat{B}] \neq 0$

**Operators that commute**

When $[\hat{A}, \hat{B}] = 0$, both can be measured simultaneously to arbitrary precision. They also share a common set of eigenvectors, so one can find eigenvectors of $\hat{A}$ that are simultaneously eigenvectors of $\hat{B}$. This is enormously useful, especially for exploiting symmetries to solve the Schrödinger equation.

**Example:** Two level system

Introduce the following operators

$$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar}{2}\left(\hat{S}^+ + \hat{S}^-\right)$$

$$\hat{S}_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \frac{\hbar}{2i}\left(\hat{S}^+ - \hat{S}^-\right)$$

$$\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{\hbar}{2}\left(\hat{N}_1 + \hat{N}_0\right)$$

$$\left[\hat{S}_x, \hat{S}_z\right] = \frac{\hbar^2}{4}\begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = -i\hbar\,\hat{S}_y \neq 0$$

$$\rightarrow \sigma_x \sigma_y \geq \left|\frac{1}{2i}\langle -i\hbar\,\hat{S}_y\rangle\right| = \frac{\hbar}{2}\left|\langle \hat{S}_y\rangle\right|$$

So the lower bound itself depends on the quantum state. In particular, if $\langle \hat{S}_y\rangle = 0$ the bound vanishes. One such state is, for example

$$|\psi\rangle = \frac{1}{\sqrt{2}}\left(|y+\rangle + |y-\rangle\right)$$

where $|y\pm\rangle$ satisfy $\hat{S}_y |\pm\rangle = \pm\frac{\hbar}{2}|\pm\rangle$

$$\langle \psi | \hat{S}_y | \psi\rangle = \frac{1}{2}\left(\langle +| + \langle -|\right)\hat{S}_y\left(|+\rangle + |-\rangle\right)$$

$$= \frac{1}{2}\left(\langle +|\hat{S}_y|+\rangle + \langle -|\hat{S}_y|-\rangle\right)$$

$$= \frac{1}{2}\left(\frac{\hbar}{2} - \frac{\hbar}{2}\right) = 0$$

## 1.7 The Schrödinger equation

Introduce the time-evolution operator, which advances a state forward in time

$$\hat{U}(t)|\psi(0)\rangle = |\psi(t)\rangle$$

To conserve probability, the evolution must preserve the norm of the state

$$\langle \psi(t)|\psi(t)\rangle = \langle U\psi(0)|U\psi(0)\rangle$$

$$= \langle \psi(0)|U^\dagger(t)U(t)|\psi(0)\rangle$$

$$= \langle \psi(0)|\psi(0)\rangle = 1$$

$$\rightarrow U^\dagger(t)U(t) = \mathbb{I} \rightarrow U(t) \text{ must be } \underline{\text{unitary}}$$

Consider an infinitesimal time step

$$\hat{U}(dt) = 1 - \frac{i}{\hbar}\hat{H}\,dt$$

where $\hat{H}$ generates "time translations". Unitarity forces $\hat{H}$ to be Hermitian.

One can show that $\hat{U}$ obeys a first-order differential equation in time

$$\hat{U}(t+dt) = \hat{U}(dt)\hat{U}(t) = \left(1 - \frac{i}{\hbar}\hat{H}\,dt\right)\hat{U}(t)$$

$$\rightarrow \hat{U}(t+dt) - \hat{U}(t) = \left(-\frac{i}{\hbar}\hat{H}\,dt\right)\hat{U}(t)$$

$$\rightarrow i\hbar\frac{d\hat{U}}{dt} = \hat{H}\hat{U}(t)$$

$$\rightarrow i\hbar\frac{d}{dt}\hat{U}(t)|\psi(0)\rangle = \hat{H}\hat{U}(t)|\psi(0)\rangle$$

$$\boxed{i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle}$$

*Schrödinger equation*

For a time-independent $\hat{H}$ we may expand

$$\hat{U}(t) = \lim_{N\to\infty}\left[1 - \frac{i}{\hbar}\hat{H}\left(t/N\right)\right]^N = e^{-i\hat{H}t/\hbar}$$

and $$|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle$$

$\hat{H}$ has units of energy. Moreover, if $\hat{H}$ is time independent:

$$\langle \psi|\hat{H}|\psi\rangle = \text{const.}$$

which points to energy conservation. Indeed, $\hat{H}$ is the Hamiltonian, the "energy operator". Hence

$$E = \langle\hat{H}\rangle = \langle\psi|\hat{H}|\psi\rangle$$

The eigenstates of the Hamiltonian satisfy

$$\hat{H}|\psi\rangle = E|\psi\rangle$$

and $$e^{-i\hat{H}t/\hbar}|E\rangle = e^{-iEt/\hbar}|E\rangle$$

Therefore, if the system starts in an energy eigenstate,

$$|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle = e^{-iEt/\hbar}|\psi(0)\rangle$$

The state merely acquires an overall phase. Physically nothing changes with time; this is a "stationary state".

## 1.8 Time-dependence of expectation values

Take an observable and track how its expectation value evolves in time

$$\frac{d}{dt}\langle\hat{O}\rangle = \frac{d}{dt}\langle\psi(t)|\hat{O}|\psi(t)\rangle$$

$$= \left(\frac{d}{dt}\langle\psi(t)|\right)\hat{O}|\psi(t)\rangle + \langle\psi(t)|\hat{O}\left(\frac{d}{dt}|\psi(t)\rangle\right)$$

$$\quad + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

$$= \frac{-1}{i\hbar}\langle\psi(t)|\hat{H}\hat{O}|\psi(t)\rangle + \frac{1}{i\hbar}\langle\psi(t)|\hat{O}\hat{H}|\psi(t)\rangle$$

$$\quad + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

$$= \frac{i}{\hbar}\langle\psi(t)|[\hat{H},\hat{O}]|\psi(t)\rangle + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

*"Generalized Ehrenfest theorem"*

If $\hat{O} \neq \hat{O}(t)$ has no explicit time dependence

$$\rightarrow \frac{d}{dt}\langle\hat{O}\rangle = \frac{i}{\hbar}\langle[\hat{H},\hat{O}]\rangle$$

**Example:**

$$\frac{d}{dt}\langle\hat{x}\rangle = \frac{i}{\hbar}\langle[\hat{H},\hat{x}]\rangle = \left\langle\frac{\hat{p}}{m}\right\rangle$$

$$\rightarrow m\frac{d}{dt}\langle\hat{x}\rangle = \langle\hat{p}\rangle$$

If the observable commutes with $\hat{H}$, i.e. $[\hat{H},\hat{O}]=0$

$$\rightarrow \frac{d}{dt}\langle\hat{O}\rangle = 0$$

$$\rightarrow \hat{O} \text{ is a constant of motion.}$$

**Example:** two-level system (Townsend Ex.4.2)

Take the Hamiltonian

$$\hat{H} = \omega_0\,\hat{S}_x$$

with initial state $|\psi(0)\rangle = |1\rangle$. Find how the state evolves in time.

**Solution:** $\hat{U}(t) = e^{-i\omega_0\hat{S}_x t/\hbar}$

First express $|\psi(0)\rangle$ in the

eigenbasis of $\hat{S}_x$.

Recall $|x+\rangle = \frac{1}{\sqrt{2}}\left(|1\rangle + |2\rangle\right)$

$$|x-\rangle = \frac{1}{\sqrt{2}}\left(|1\rangle - |2\rangle\right)$$

Inverting,

$$|1\rangle = \frac{1}{\sqrt{2}}\left(|x+\rangle + |x-\rangle\right)$$

$$|2\rangle = \frac{1}{\sqrt{2}}\left(|x+\rangle - |x-\rangle\right)$$

Applying the evolution operator to $|\psi(0)\rangle$,

$$|\psi(t)\rangle = e^{-i\omega_0\hat{S}_x t/\hbar}|1\rangle = \frac{e^{-i\frac{\omega_0 t}{2}}}{\sqrt{2}}|x+\rangle + \frac{e^{i\frac{\omega_0 t}{2}}}{\sqrt{2}}|x-\rangle$$

Transforming back to the original basis,

$$|\psi(t)\rangle = \frac{e^{-i\frac{\omega_0 t}{2}}}{2}\left(|1\rangle + |2\rangle\right) + \frac{e^{i\frac{\omega_0 t}{2}}}{2}\left(|1\rangle - |2\rangle\right)$$

$$= \cos\frac{\omega_0 t}{2}|1\rangle - i\sin\frac{\omega_0 t}{2}|2\rangle$$

From this we can compute $\langle S^z(t)\rangle$

$$\langle S^z(t)\rangle = \cos^2\frac{\omega_0 t}{2}\left(\frac{\hbar}{2}\right) + \sin^2\frac{\omega_0 t}{2}\left(-\frac{\hbar}{2}\right)$$

$$= \frac{\hbar}{2}\left(\cos^2\frac{\omega_0 t}{2} - \sin^2\frac{\omega_0 t}{2}\right) = \frac{\hbar}{2}\cos\omega_0 t$$

More generally, when the initial state is not an eigenstate

$$e^{-i\hat{H}t/\hbar}|\psi(0)\rangle = e^{-i\hat{H}t/\hbar}\sum_n \langle n|\psi(0)\rangle|n\rangle$$

$$= \sum_n \langle n|\psi(0)\rangle\,e^{-iE_n t/\hbar}|n\rangle$$

so computing the time evolution amounts to finding the eigenvalues and eigenvectors of $\hat{H}$.

## 1.9 From wavefunctions to kets (bras)

Every wave function $\psi(\vec{r})$ corresponds to a ket $|\psi\rangle$. What remains is to spell out how scalar products and matrix elements are computed.

The scalar product must reduce to the usual overlap of wave functions

$$\langle\psi|\varphi\rangle = \int d^3 r\,\psi^*(\vec{r})\,\varphi(\vec{r})$$

For the matrix elements, introduce the "$r$-representation", built on the continuous basis

$$|\vec{r}\rangle \Leftrightarrow \delta(\vec{r}-\vec{r}_0)$$

It satisfies

- $\langle\vec{r}_0|\vec{r}_0'\rangle = \int d^3 r\,\delta(\vec{r}-\vec{r}_0)\,\delta(\vec{r}-\vec{r}_0') = \delta(\vec{r}_0 - \vec{r}_0')$

- Closure: $\int d^3 r_0\,|\vec{r}_0\rangle\langle\vec{r}_0| = \mathbb{I}$

From these we obtain:

**END LECTURE #3**

**a) Components of a ket:**

$$|\psi\rangle = \int d^3 r_0\,|\vec{r}_0\rangle\langle\vec{r}_0|\psi\rangle$$

$$= \int d^3 r_0\,|\vec{r}_0\rangle\left(\int d^3 r\,\delta(\vec{r}_0-\vec{r})\,\psi(\vec{r})\right)$$

$$= \int d^3 r_0\,\psi(\vec{r}_0)\,|\vec{r}_0\rangle$$

$$\rightarrow \langle\vec{r}_0|\psi\rangle = \psi(\vec{r}_0)$$

**b) Matrix elements:**

$$\langle\varphi|\hat{O}|\psi\rangle = \int d^3 r_0\,d^3 r_0'\,\langle\varphi|\vec{r}_0\rangle\langle\vec{r}_0|\hat{O}|\vec{r}_0'\rangle\langle\vec{r}_0'|\psi\rangle$$

$$= \int d^3 r_0\,d^3 r_0'\,\varphi^*(\vec{r}_0)\,\hat{O}(\vec{r}_0,\vec{r}_0')\,\psi(\vec{r}_0')$$

**Example:** $\hat{x}$-operator: $\hat{x}|x\rangle = x|x\rangle$

$$\rightarrow \langle x|\hat{x}|x'\rangle = x\langle x|x'\rangle = x\,\delta(x-x')$$

$$\rightarrow \langle\varphi|\hat{x}|\psi\rangle = \int dx\,dx'\,\delta(x-x')\,\varphi^*(x)\,x\,\psi(x')$$

$$= \int dx\,\varphi^*(x)\,x\,\psi(x)$$

## 1.10 Momentum operator

The momentum operator is defined through its action on a state of definite momentum $P$ (a 1d example, for simplicity)

$$\hat{P}|P\rangle = P|P\rangle\;;\quad \langle x|P\rangle = \frac{e^{iPx/\hbar}}{\sqrt{2\pi\hbar}}$$

therefore

$$\langle x|\hat{P}|\psi\rangle = \int dP\,\langle x|P\rangle\langle P|\hat{P}|\psi\rangle =$$

$$= \int dP\,P\,\langle x|P\rangle\langle P|\psi\rangle =$$

$$= \frac{1}{\sqrt{2\pi\hbar}}\int dP\,e^{iPx/\hbar}\,P\,\psi(P)$$

This is the Fourier transform of $P\psi(P)$, namely $-i\hbar\frac{\partial}{\partial x}\psi(x)$

$$\rightarrow \langle x|\hat{P}|\psi\rangle = -i\hbar\frac{\partial}{\partial x}\psi(x)$$

$$\rightarrow \langle\varphi|\hat{P}|\psi\rangle = \int dx\,\langle\varphi|x\rangle\langle x|\hat{P}|\psi\rangle =$$

$$= \int dx\,\varphi^*(x)\left[-i\hbar\frac{\partial}{\partial x}\right]\psi(x)$$

The momentum operator is Hermitian:

$$\langle\varphi|\hat{P}\psi\rangle = \int_{-\infty}^{\infty} dx\,\varphi^*(x)\left(-i\hbar\frac{d}{dx}\psi(x)\right)$$

$$\overset{\text{by parts}}{=} -i\hbar\,\varphi^*(x)\psi(x)\Big|_{-\infty}^{\infty} + i\hbar\int_{-\infty}^{\infty} dx\,\psi(x)\frac{d\varphi^*(x)}{dx}$$

Normalizable wave functions must vanish at infinity, so the boundary term drops out and

$$\langle\varphi|\hat{P}\psi\rangle = \langle\hat{P}\varphi|\psi\rangle$$

## 1.11 Angular momentum

$$\hat{P}_x = \frac{\hbar}{i}\frac{\partial}{\partial x}\;;\quad \hat{P}_y = \frac{\hbar}{i}\frac{\partial}{\partial y}\;;\quad \hat{P}_z = \frac{\hbar}{i}\frac{\partial}{\partial z}$$

$$\hat{\vec{P}} = \frac{\hbar}{i}\vec{\nabla}\;;\quad [\hat{r}_i,\hat{P}_j] = i\hbar\,\delta_{ij}$$

$$\boxed{\hat{\vec{L}} = \hat{\vec{r}}\times\hat{\vec{P}}}$$

$$[\hat{L}_x,\hat{L}_y] = i\hbar\hat{L}_z \rightarrow \sigma_x\sigma_y \geq \frac{\hbar}{2}|\langle L_z\rangle|$$

We may also form the square of $\vec{L}$:

$$\hat{L}^2 = \hat{\vec{L}}\cdot\hat{\vec{L}} = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$$

$$[\hat{L}^2,L_x] = [\hat{L}^2,L_y] = [\hat{L}^2,L_z] = 0$$

If the Hamiltonian is rotationally invariant

$$[\hat{H},\hat{L}^2] = [\hat{H},\hat{L}_z] = 0$$

The eigenstates of $H$ are then simultaneously eigenstates of $\hat{L}^2$ and $\hat{L}_z$.

The choice of $L_z$ is conventional; $L_x$ or $L_y$ would serve equally well, with nothing special about $L_z$.

To find the eigenstates it helps to introduce the operators

$$\hat{L}_+ = \hat{L}_x + i\hat{L}_y\;;\quad \hat{L}_- = \hat{L}_+^\dagger = \hat{L}_x - i\hat{L}_y$$

$$\rightarrow \hat{L}_x = \frac{1}{2}\left(\hat{L}_+ + \hat{L}_-\right)\;;\quad \hat{L}_y = \frac{1}{2i}\left(\hat{L}_+ - \hat{L}_-\right)$$

$\hat{L}_+$ and $\hat{L}_-$ are not Hermitian and satisfy

$$[\hat{L}_+,\hat{L}_-] = 2\hbar\hat{L}_z,\quad [\hat{L}_z,\hat{L}_+] = \hbar\hat{L}_+,\quad [\hat{L}_z,\hat{L}_-] = -\hbar\hat{L}_-$$

One can check that

$$\hat{L}^2 = \frac{1}{2}\left(\hat{L}_+\hat{L}_- + \hat{L}_-\hat{L}_+\right) + \hat{L}_z^2$$

$$= \hat{L}_+\hat{L}_- + \hat{L}_z^2 - \hbar\hat{L}_z$$

$$= \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$$

These relations tightly constrain the allowed eigenvalues of $\hat{L}_z$ and $\hat{L}^2$.

Suppose we know one eigenvalue of $\hat{L}_z$, written as $\hbar m$ (the factor $\hbar$ makes $m$ dimensionless). Here $L_+$ and $L_-$ act as "ladder" operators

$$\hat{L}_z\hat{L}_+|m\rangle = \left(\hat{L}_+\hat{L}_z + \hbar\hat{L}_+\right)|m\rangle = \hbar(m+1)\hat{L}_+|m\rangle$$

$$\rightarrow \hat{L}_+|m\rangle = \hbar C_m|m+1\rangle$$

Similarly $$L_-|m\rangle = \hbar C_m'|m-1\rangle$$

The constants $C_m, C_m'$ follow from $L_+ = L_-^\dagger$

$$\langle m+1|\hat{L}_+|m\rangle = \hbar C_m = \hbar C_{m+1}'^* \rightarrow C_m' = C_{m-1}^*$$

Absorbing the phase into the state makes the constants real $\rightarrow C_m' = C_{m-1}$

Now consider the operator

$$\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2 = \frac{1}{2}\left(\hat{L}_+\hat{L}_- + \hat{L}_-\hat{L}_+\right)$$

Being a sum of squares of Hermitian operators, it has non-negative expectation value. Hence, for a fixed eigenvalue $\ell$ of $L^2$, the $L_z$ spectrum is confined to $[-\ell, \ell]$.

$$\rightarrow C_\ell = C_{-\ell}' = C_{-\ell} = 0$$

Equivalently, there exist eigenstates with

$$\hat{L}_-|\ell,-\ell\rangle = \hat{L}_+|\ell,\ell\rangle = 0$$

Because repeated application of $L_\pm$ connects the states $|\ell,m\rangle$ from $m=-\ell$ up to $m=\ell$, the quantity $2\ell$ must be an integer, so $m$ takes integer or half-integer values

Now apply $L^2$ to $|\ell,\ell\rangle$

$$\hat{L}^2|\ell,\ell\rangle = \hat{L}_-\hat{L}_+|\ell,\ell\rangle + \hat{L}_z^2|\ell,\ell\rangle + \hbar\hat{L}_z|\ell,\ell\rangle$$

$$= \left(0 + \hbar^2\ell^2 + \hbar^2\ell\right)|\ell,\ell\rangle$$

$$= \hbar^2\ell(\ell+1)|\ell,\ell\rangle$$

This departs from the classical answer. For a particle circulating in the $x$-$y$ plane one would have $L_x = L_y = 0$; $L_z = \ell$; $L^2 = \ell^2$. The discrepancy comes from quantum fluctuations of the transverse components: although $\langle L_x\rangle = \langle L_y\rangle = 0$, their fluctuations do not vanish!

$$\langle\ell,\ell|\hat{L}_x^2|\ell,\ell\rangle = \langle\ell,\ell|\hat{L}_y^2|\ell,\ell\rangle = \hbar^2\ell/2$$

$$\rightarrow \sigma_{Lx} = \sigma_{Ly} = \hbar\sqrt{\ell/2}$$

Were $L_x = L_y = 0$ exactly, we would have perfect certainty on both components, in conflict with Heisenberg's uncertainty principle!

Finally, we determine the constants $C_m$

$$\hat{L}_+\hat{L}_-|\ell,-\ell\rangle = \left(\hat{L}_-\hat{L}_+ + 2\hbar\hat{L}_z\right)|\ell,-\ell\rangle$$

$$= \left(\hbar^2 C_\ell^2 - 2\hbar^2\ell\right)|\ell,-\ell\rangle$$

$$\rightarrow C_\ell = \sqrt{2\ell}$$

Repeating with $|\ell,-\ell+1\rangle \rightarrow C_{\ell+1} = \sqrt{(2\ell-1)2}$

Continuing in this way gives the general result

$$C_m = \sqrt{(\ell-m)(\ell+m+1)}$$

**Summarizing:**

$$\hat{L}_z|\ell,m\rangle = \hbar m|\ell,m\rangle$$

$$\hat{L}^2|\ell,m\rangle = \hbar^2\ell(\ell+1)|\ell,m\rangle$$

with $\ell$ integer or half-integer, and $m = -\ell, \ldots, \ell$.

$$\hat{L}_+|\ell,m\rangle = \hbar\sqrt{(\ell+m+1)(\ell-m)}\,|\ell,m+1\rangle$$

$$\hat{L}_-|\ell,m\rangle = \hbar\sqrt{(\ell+m)(\ell+1-m)}\,|\ell,m-1\rangle$$

$$\langle\ell,m|\hat{L}_x|\ell,m-1\rangle = \langle\ell,m-1|\hat{L}_x|\ell,m\rangle = \frac{\hbar}{2}\sqrt{(\ell+m)(\ell+1-m)}$$

$$\langle\ell,m|\hat{L}_y|\ell,m-1\rangle = \langle\ell,m-1|\hat{L}_y|\ell,m\rangle = -\frac{\hbar}{2}\sqrt{(\ell+m)(\ell+1-m)}$$

**Example:** $L=1$

Basis: $|\ell,m\rangle = \{|1,-1\rangle;\ |1,0\rangle;\ |1,1\rangle\}$

$$\hat{L}_+|1,-1\rangle = \hbar\sqrt{2}|1,0\rangle$$

$$\hat{L}_+|1,0\rangle = \hbar\sqrt{2}|1,1\rangle$$

$$\rightarrow L_- = \sqrt{2}\hbar\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

Similarly

$$L_+ = \sqrt{2}\hbar\begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = (L_-)^\dagger$$

### Angular momentum in coordinate representation

Working in spherical coordinates

$$x = r\sin\theta\cos\varphi\;;\quad y = r\sin\theta\sin\varphi\;;\quad z = r\cos\theta$$

$$\rightarrow \hat{L}_z = -i\hbar\frac{\partial}{\partial\varphi}$$

$$\hat{L}_\pm = \pm\hbar e^{\pm i\varphi}\left(\frac{\partial}{\partial\theta} \pm i\cot\theta\frac{\partial}{\partial\varphi}\right)$$

$$\hat{L}^2 = -\hbar^2\left[\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} + \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)\right]$$

Because $\hat{L}_z$ takes such a simple form, its eigenstates follow at once:

$$-i\hbar\frac{\partial}{\partial\varphi}\Psi_m(\varphi) = \hbar m\Psi_m(\varphi)$$

$$\rightarrow \Psi_m(\varphi) = \frac{1}{\sqrt{2\pi}}e^{im\varphi}\quad m = 0, \pm 1, \pm 2, \ldots$$

Since $\psi(\varphi+2\pi) = \psi(\varphi)$, $m$ must be an integer.

The joint eigenstates of $\hat{L}^2$ and $\hat{L}^z$ are the "spherical harmonics". For $m=\ell$

$$Y_\ell^\ell(\theta,\varphi) = \frac{(-1)^\ell}{2^\ell\ell!}\sqrt{\frac{(2\ell+1)!}{4\pi}}\sin^\ell(\theta)\,e^{i\ell\varphi}$$

The solutions for $m<\ell$ are generated by applying $\hat{L}_-$

$$Y_\ell^m(\theta,\varphi) = (-1)^m\sqrt{\frac{(2\ell+1)(\ell-m)!}{4\pi\,(\ell+m)!}}\,P_{\ell m}(\cos\theta)\,e^{im\varphi},$$

where $P_{\ell m}$ are generalized Legendre polynomials

$$P_\ell^m(x) = (1-x^2)^{|m|/2}\left(\frac{d}{dx}\right)^{|m|}P_\ell(x)$$

$$P_\ell(x) = \frac{1}{2^\ell\ell!}\left(\frac{d}{dx}\right)^\ell(x^2-1)^\ell.$$

The $Y_\ell^m$ constitute a complete, orthogonal basis

$$\int_0^{2\pi} d\varphi \int_0^{\pi} d\theta \, \sin\theta \, Y_\ell^m(\theta,\varphi)^* \, Y_{\ell'}^{m'}(\theta,\varphi) = \delta_{\ell\ell'} \, \delta_{mm'}$$

and, by construction, they satisfy

$$\hat{L}^2 \, Y_\ell^m(\theta,\varphi) = \hbar^2 \ell(\ell+1) \, Y_\ell^m(\theta,\varphi)$$

$$\hat{L}_z \, Y_\ell^m(\theta,\varphi) = \hbar m \, Y_\ell^m(\theta,\varphi)$$

## 2 — A particle in a spherically symmetric potential

We aim to solve

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi$$

with the Hamiltonian

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(r)$$

$$\longrightarrow \quad i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$$

with $\nabla^2 = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2}$

Because the potential carries no time dependence

$$\Psi_n(\vec{r},t) = \psi_n(\vec{r}) \, e^{-iE_n t/\hbar}$$

where the spatial part $\psi_n$ obeys the time-independent Schrödinger equation

$$\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$$

The general solution of the time-dependent Schrödinger equation then takes the form

$$\Psi(\vec{r},t) = \sum_n c_n \, \psi_n(\vec{r}) \, e^{-iE_n t/\hbar}$$

where the coefficients $c_n$ are fixed by the initial conditions.

For a spherically symmetric potential, we first note that

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\left(\frac{\partial^2}{\partial\varphi^2}\right)$$

Therefore

$$\frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{\hat{L}^2}{2mr^2}$$

Where the first term contains

$$\hat{p}_r^2 = -\hbar^2 \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) = -\hbar^2\frac{\partial^2}{\partial r^2} - \hbar^2\frac{2}{r}\frac{\partial}{\partial r}$$

As in the classical case, the Hamiltonian of a particle in a spherically symmetric potential reads:

$$H = \frac{\hat{p}_r^2}{2m} + \frac{\hat{L}^2}{2mr^2} + V(r)$$

### Separation of variables:

For a particle in a central potential,

$$[\hat{H}, \hat{L}^2] = [\hat{H}, \hat{L}_z] = 0$$

so we can seek solutions of the Schrödinger equation that are simultaneously eigenfunctions of $\hat{H}$, $\hat{L}^2$ and $\hat{L}_z$

$$\hat{H}\,\psi_{n\ell m}(r,\theta,\varphi) = E_n \, \psi_{n\ell m}(r,\theta,\varphi)$$

$$\hat{L}^2 \, \psi_{n\ell m}(r,\theta,\varphi) = \hbar^2\ell(\ell+1) \, \psi_{n\ell m}(r,\theta,\varphi)$$

$$\hat{L}_z \, \psi_{n\ell m}(r,\theta,\varphi) = \hbar m \, \psi_{n\ell m}(r,\theta,\varphi)$$

Since these eigenfunctions are also angular momentum eigenstates, we write them as

$$\psi(r,\theta,\varphi) = R(r) \, Y_\ell^m(\theta,\varphi)$$

Substituting this into the Schrödinger equation yields the eigenvalue equation for the radial part

$$-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\right) - \frac{\ell(\ell+1)}{r^2} + V(r)\right]R(r) = ER(r)$$

Setting $\chi(r) = r R(r)$, we obtain

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + V_{\text{eff}}\right]\chi(r) = E\chi(r)$$

$$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2} \qquad r > 0$$

*end lecture*

a one-dimensional Schrödinger equation for $\chi(r)$. For each $\ell$, the radial equation must be solved subject to $\chi(0) = 0$, equivalent to an infinite barrier at the origin and ensuring $\chi = 0$ for $r < 0$. The eigenvalues are independent of $L_z$ or $m$, giving a $2\ell+1$-fold degeneracy for each value of $\ell$.


---

## References and Further Reading

*The references below are an editorial addition. Prof. Feiguin's lecture notes follow John S. Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed. (University Science Books, 2012); the generalized uncertainty relation is cited in the text as Townsend §3.5.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 1 (Stern–Gerlach Experiments), Ch. 2 (Rotation of Basis States and Matrix Mechanics), Ch. 3 (Angular Momentum — the generalized uncertainty principle, §3.5), Ch. 4 (Time Evolution). Wave mechanics and the momentum operator: Ch. 6.

**Further reading.** Sakurai & Napolitano, *Modern Quantum Mechanics*, the "Fundamental Concepts" and "Quantum Dynamics" chapters; Shankar, *Principles of Quantum Mechanics*, Ch. 1, 4; Cohen-Tannoudji, Diu & Laloë, *Quantum Mechanics*, Vol. I, Ch. II–III.
# Chapter 2 — The Hydrogen Atom

*The last atom we can solve in closed form — the benchmark every approximation answers to.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Here is the remarkable thing about hydrogen: one electron, one proton, a $1/r$ pull between them, and the whole spectrum drops out exactly. No perturbation series, no variational guess — just a differential equation and the demand that the wavefunction stay finite. That demand is the entire trick. We separate the angular part (already handled by the central-potential machinery) from the radial part, then squeeze the radial equation between two boundary conditions: it cannot blow up at infinity, and it cannot blow up at the origin. Each condition fixes the form of the solution at one end. What survives in the middle is a power series — and that series only stays a polynomial, only stays normalizable, for a discrete set of energies. Quantization is not imposed; it is forced.

The payoff is the spectrum $E_n = -\mu Z^2 e^4/2\hbar^2 n^2$, energies depending on $n$ alone. The angular momentum $\ell$ drops out entirely, which is strange — the $m$-degeneracy comes from rotational symmetry, but the $\ell$-degeneracy demands a deeper reason. That reason is the Laplace–Runge–Lenz vector, a conserved quantity special to $1/r$ potentials. Its algebra is powerful enough that Pauli extracted the full spectrum from it before Schrödinger wrote his equation. Hydrogen is the last atom we solve cleanly; everything heavier is measured against it.

## 2.1 The hydrogen atom

The hydrogen atom is a nucleus of charge $+Ze$ with an electron bound to it by the attractive Coulomb force. With only one electron, we drop spin from the picture. Exactly as in the classical two-body problem, we work in the center-of-mass frame and let the reduced mass stand in for the electron mass in the Hamiltonian

$$\hat{H} = \frac{\hat{p}_e^2}{2\mu} - \frac{Ze^2}{|\vec{r}|}$$

$$\mu = \frac{m_e m_p}{m_e + m_p} \quad ; \quad m_p \approx 1836\,m_e \to \mu \approx m_e$$

$$Z = 1 \quad \text{for hydrogen}$$

In spherical coordinates

$$\hat{H} = \frac{\hat{p}_r^2}{2\mu} + \frac{\hbar^2\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{r} = \frac{\hat{p}_r^2}{2\mu} + \frac{\hbar^2\ell(\ell+1)}{2\mu r^2} - \frac{Ze^2}{r}$$

As before, the task reduces to solving the radial eigenvalue problem at fixed $\ell$

$$\frac{d^2\chi}{dr^2} + \left[\frac{2\mu E}{\hbar^2} + \frac{2\mu Ze^2}{\hbar^2 r} - \frac{\ell(\ell+1)}{r^2}\right]\chi = 0$$

It pays to switch to dimensionless variables

$$\rho = \frac{\sqrt{8\mu|E|}}{\hbar}\,r \quad ; \quad \rho_0 = \sqrt{\frac{\mu}{2|E|}}\,\frac{Ze^2}{\hbar}$$

$$\longrightarrow \quad \frac{d^2\chi}{d\rho^2} - \left[\frac{1}{4} - \frac{\rho_0}{\rho} + \frac{\ell(\ell+1)}{\rho^2}\right]\chi = 0$$

For $\rho \gg 1$:

$$\frac{d^2\chi}{d\rho^2} - \frac{1}{4}\chi = 0 \quad \longrightarrow \quad \chi \sim e^{\pm\rho/2}$$

Since the solution must not diverge, we keep only the decaying exponential.

For $\rho \to 0$:

We try $\rho^s$ in the differential equation

$$s(s-1)\rho^{s-2} + \rho_0\rho^{s-1} - \frac{1}{4}\rho^s - \ell(\ell+1)\rho^{s-2} = 0$$

In the limit $\rho \to 0$ the $\rho^{s-2}$ terms dominate.

Killing the singularity requires

$$-s(s-1) + \ell(\ell+1) = 0$$

$\longrightarrow s = \ell+1$, or $s = -\ell$. We throw out $\rho^{-\ell}$ because:
- For $\ell \geq 1$, $\chi$ diverges.
- For $\ell = 0$, $R \sim \dfrac{1}{r}$, also diverges.

$$\longrightarrow \quad \chi \to \rho^{\ell+1} \quad \text{for } \rho \to 0$$

With both limits in hand, we write a general trial solution

$$\chi(\rho) = \rho^{\ell+1} \, e^{-\rho/2} \, P(\rho)$$

Inserting this into the radial equation gives

$$\frac{d^2 P}{d\rho^2} + \left(\frac{2\ell+2}{\rho} - 1\right)\frac{dP}{d\rho} + \left(\frac{\rho_0 + \ell + 1}{\rho}\right)P = 0$$

Take $P(\rho) = \displaystyle\sum_{k=0}^{\infty} c_k \rho^k$ with $c_0 \neq 0$

$$\longrightarrow \sum_{k=2}^{\infty} k(k-1)c_k\rho^{k-2} + \sum_{k=1}^{\infty}(2\ell+2)k\,c_k\rho^{k-2} + \sum_{k=0}^{\infty}\left(-k+\rho_0-(\ell+1)\right)c_k\rho^{k-1} = 0$$

which rearranges to

$$\sum_{k=0}^{\infty}\left\{k(k+1) + (2\ell+2)(k+1)\,c_{k+1} + \left(-k+\rho_0-(\ell+1)\right)c_k\right\}\rho^{k-1} = 0$$

$$\longrightarrow \quad \frac{c_{k+1}}{c_k} = \frac{k+\ell+1-\rho_0}{(k+1)(k+2\ell+2)}$$

Note that $\dfrac{c_{k+1}}{c_k} \overset{k\to\infty}{\longrightarrow} \dfrac{1}{k}$, so the unterminated series grows like $e^\rho$. The series must therefore cut off

$$\rho_0 = 1+\ell+k_{\max}, \quad \text{with } k_{\max} = 0,1,2,\ldots$$

The solution is then a polynomial of degree $n$. Quantizing $\rho_0$ this way yields

$$E = -\frac{\mu Z^2 e^4}{2\hbar^2(1+\ell+k_{\max})^2}$$

With $k_{\max}$ and $\ell$ both non-negative integers, we set $n = 1+\ell+k_{\max}$

$$\boxed{\,E_n = -\frac{\mu Z^2 e^4}{2\hbar^2 n^2}\,} \qquad n = 1,2,3,\ldots$$

$$E_n = -\frac{Z^2}{2n^2}\,E_h$$

With $E_h = \dfrac{\mu e^4}{\hbar^2} \approx 4.36\times10^{-18}\,\text{J} \approx 27.2\,\text{eV} = 1\,\text{Hartree}$

The ground state corresponds to $n=1$, $Z=1$:

$$E_1 = 0.5\,\text{Hartree} = -1\,\text{Ry} \quad (\text{Rydberg})$$

The polynomials appearing in the solution are the "Laguerre polynomials".

### Hydrogenic wave functions

$$\psi_{n\ell m}(r,\theta,\varphi) = R_{n\ell}(r)\,Y_\ell^m(\theta,\varphi) = \frac{\chi_{n\ell}(r)}{r}\,Y_\ell^m(\theta,\varphi)$$

Written in the dimensionless variable $\rho$

$$\rho = \sqrt{\frac{8\mu|E|}{\hbar^2}}\,r = \frac{2Z}{n}\frac{r}{a_0}$$

with $a_0 = \dfrac{\hbar}{\mu c\alpha}$ ; $\alpha = \dfrac{e^2}{\hbar c} \sim \dfrac{1}{137}$ (fine-structure constant)

$a_0$ is the Bohr radius $a_0 \sim 0.529\,\text{Å}$

$$R_{10} = 2\left(\frac{Z}{a_0}\right)^{3/2} e^{-Zr/a_0}$$

$$R_{20} = 2\left(\frac{Z}{2a_0}\right)^{3/2}\left(1 - \frac{Zr}{2a_0}\right)e^{-Zr/2a_0}$$

$$R_{21} = \frac{1}{\sqrt{3}}\left(\frac{Z}{2a_0}\right)^{3/2}\frac{Zr}{a_0}\,e^{-Zr/2a_0}$$

**Example:** An electron in the Coulomb field of a proton is in the state

$$|\psi\rangle = \frac{1}{\sqrt{2}}|1,0,0\rangle + \frac{1}{\sqrt{2}}|2,1,1\rangle$$

a) What is $|\psi(t)\rangle$ ?

b) Calculate $\langle E\rangle$, $\langle L^2\rangle$, $\langle L_x\rangle$, $\langle L_y\rangle$, $\langle L_z\rangle$

**Solution**

a) $$|\psi(t)\rangle = \frac{e^{-iE_1 t/\hbar}}{\sqrt{2}}|1,0,0\rangle + \frac{e^{-iE_2 t/\hbar}}{\sqrt{2}}|2,1,1\rangle$$

b) $$\langle E\rangle = \langle\psi(t)|H|\psi(t)\rangle = \frac{1}{2}E_1 + \frac{1}{2}E_2$$

$$\langle L^2\rangle = \frac{1(1+1)\hbar^2}{2} = \hbar^2$$

$$\langle L_z\rangle = \frac{\hbar}{2}$$

$$\langle L_x\rangle = \frac{1}{2}\langle L_+ + L_-\rangle =$$
$$= \frac{1}{2}\left(\frac{e^{iE_1 t/\hbar}}{\sqrt{2}}\langle 1,0,0| + \frac{e^{iE_2 t/\hbar}}{\sqrt{2}}\langle 2,1,1|\right)\hbar\,e^{-iE_2 t/\hbar}|2,1,0\rangle = 0$$

(same for $\langle L_y\rangle = 0$)

### Degeneracy

For a given $n$, the permitted values of $\ell$ are

$$\ell = 0, \ldots, n-1$$

For a given $\ell$, the permitted values of $m$ are

$$m = -\ell, -\ell+1, \ldots, \ell-1, \ell$$

Summing over both, the total degeneracy at fixed $n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = \frac{2(n-1)n}{2} + n = n^2$$

(Energy level diagram: vertical axis $E$, horizontal axis $\ell$. Levels shown at $n=1$ (lowest), $n=2$, $n=3$, $n=4$. Columns labeled $\ell=0$ (s), $\ell=1$ (p), $\ell=2$ (d), $\ell=3$ (f), with increasing numbers of states across rows.)

*end lecture*

That the energy ignores $\ell$ is far from obvious — the $m$-degeneracy follows plainly from rotational symmetry, but this one does not.

The extra degeneracy springs from a "hidden symmetry" present whenever the central potential takes the form $V(r) = -k/r$ (Kepler problems). Classically, this shows up as an additional conserved quantity:

$$\vec{A} = \vec{p}\times\vec{L} - \mu k\frac{\vec{r}}{r} \qquad \text{"Laplace-Runge-Lenz vector"}$$

The quantum counterpart is defined as

$$\hat{\vec{A}} = \hat{\vec{p}}\times\hat{\vec{L}} - \mu Ze^2\frac{\hat{\vec{r}}}{r}$$

One can verify that $[\hat{H}, \hat{A}] = 0$.

Strikingly, this conservation law and the algebra it generates let Pauli derive the hydrogen spectrum in 1926 *before* the Schrödinger equation existed !!!

**Exercise:** $[\hat{H}, \hat{A}_\alpha] = 0$ ; $[\hat{A}_\alpha, \hat{L}_\beta] = i\hbar\epsilon_{\alpha\beta\gamma}\hat{A}_\gamma$

$$[\hat{A}_\alpha, \hat{A}_\beta] = i\hbar\epsilon_{\alpha\beta\gamma}(-2m\hat{H})\hat{L}_\gamma$$


---

## References and Further Reading

*Editorial addition mapping the notes to their source text.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 9 (Translational and Rotational Symmetry in the Two-Body Problem) and Ch. 10 (Bound States of Central Potentials — the hydrogen atom).

**Further reading.** Griffiths & Schroeter, *Introduction to Quantum Mechanics*, the "Quantum Mechanics in Three Dimensions" chapter (the hydrogen atom); Sakurai & Napolitano, the central-potential sections; Shankar, *Principles of Quantum Mechanics*, Ch. 12–13.
# Chapter 3 — Time-Independent Perturbation Theory

*Expanding around a problem you can already solve, in powers of a genuinely small parameter.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Most Hamiltonians we care about cannot be solved exactly. The trick of this chapter is to find a nearby one that can, and treat the difference as a small nudge. Write $\hat{H} = \hat{H}_0 + \lambda\hat{V}$, where $\hat{H}_0$ has known eigenstates and $\lambda$ is a dimensionless dial we imagine turning down toward zero. Then expand both the energies and the states as power series in $\lambda$, match terms order by order, and read off the corrections.

The honest caveat: these series rarely converge. What saves us is that the first one or two terms are often astonishingly accurate. First order gives the energy shift as the expectation value of the perturbation in the unperturbed state; second order sums contributions from every other state, weighted by how strongly they couple and how far away they sit in energy.

That last weighting is also the whole story of where the method fails. Each term carries an energy denominator, so when two unperturbed states share an energy, the formula blows up. Degeneracy is the failure mode, and the fix is surgical: inside the degenerate subspace, first rotate to the basis that diagonalizes $\hat{V}$, then the divisions stay finite. We watch this play out concretely in the quadratic Stark shift of hydrogen's ground state and the linear Stark splitting of its first excited level.

## 3 — Time-independent perturbations

## 3.1 — Non-degenerate perturbation theory

We consider a Hamiltonian of the form

$$\hat{H} = \hat{H}_0 + \hat{H}_1$$

where $\hat{H}_0$ is "big" and $\hat{H}_1$ is "small". Here $\hat{H}_0$ is the "unperturbed Hamiltonian," whose solution we take to be known, while $\hat{H}_1$ is the "perturbation" that will "deform" the original solutions of $\hat{H}_0$. For the moment we further assume that the spectrum of $\hat{H}_0$ has no degeneracies.

Saying that $\hat{H}_1$ is "small" compared to $\hat{H}_0$ amounts to writing

$$\hat{H} = \hat{H}_0 + \lambda\hat{V}$$

with $\hat{H}_1 = \lambda\hat{V}$, where $\lambda$ is a dimensionless parameter and the limit of interest is $\lambda \to 0$. We posit that both the eigenstates and the eigenvalues admit a Taylor-like expansion in powers of $\lambda$. These expansions frequently fail to converge, yet the leading corrections already yield remarkably good predictions.

We want to solve

$$\hat{H}|n\rangle = E_n|n\rangle$$

by knowing the solution to

$$\hat{H}_0|n_0\rangle = E_n^{(0)}|n_0\rangle$$

We write

$$|n\rangle = |n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots$$

$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots$$

Plugging them into the eigenvalue equation we get

$$\left(\hat{H}_0 + \lambda\hat{V}\right)\left(|n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots\right)$$
$$= \left(E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots\right)\left(|n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots\right)$$

Equating terms of the same order in $\lambda$ we get

(1) $\quad \hat{H}_0|n_0\rangle = E_n^{(0)}|n_0\rangle$

(2) $\quad \hat{H}_0|n_1\rangle + \hat{V}|n_0\rangle = E_n^{(1)}|n_0\rangle + E_n^{(0)}|n_1\rangle$

(3) $\quad \hat{H}_0|n_2\rangle + \hat{V}|n_1\rangle = E_n^{(2)}|n_0\rangle + E_n^{(1)}|n_1\rangle + E_n^{(0)}|n_2\rangle$

The first equality holds trivially.

### First-order correction

We take the inner product of (2) with $\langle n_0|$ to obtain

$$\langle n_0|\hat{H}_0|n_1\rangle + \langle n_0|\hat{V}|n_0\rangle = E_n^{(0)}\langle n_0|n_1\rangle + E_n^{(1)}\langle n_0|n_0\rangle$$

$\underbrace{E_n^{(0)}\langle n_0|n_1\rangle}_{0}$ on the left, $\underbrace{\phantom{0}}_{0}$ term cancels:

$$\longrightarrow \quad \boxed{E_n^{(1)} = \langle n_0|\hat{V}|n_0\rangle}$$

Taking the inner product with $\langle k_0|$ ; $k\neq n$

$$\langle k_0|\hat{H}_0|n_1\rangle + \langle k_0|\hat{V}|n_0\rangle = E_n^{(0)}\langle k_0|n_1\rangle$$

$$\longrightarrow \quad \langle k_0|n_1\rangle = \frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}$$

Then, to first order in $\lambda$, we get

$$\boxed{\,|n\rangle = |n_0\rangle + \lambda|n_1\rangle = |n_0\rangle + \lambda\sum_k \frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}|k_0\rangle\,}$$

### Second-order energy correction

We take the product of $\langle n_0|$ in (3) to obtain

$$\underbrace{\langle n_0|\hat{H}_0|n_2\rangle}_{0} + \langle n_0|\hat{V}|n_1\rangle = E_n^{(0)}\langle n_0|n_2\rangle + \underbrace{E_n^{(1)}\langle n_0|n_1\rangle}_{0} + E_n^{(2)}\langle n_0|n_0\rangle$$

What about $\langle n_0|n_1\rangle$ ?

We found that $|n\rangle = |n_0\rangle + \lambda|n_1\rangle + \mathcal{O}(\lambda^2)$. These states must be normalized

$$\langle n|n\rangle = \underbrace{\langle n_0|n_0\rangle}_{1} + \lambda\left(\langle n_0|n_1\rangle + \langle n_1|n_0\rangle\right) + \mathcal{O}(\lambda^2)$$

$$\longrightarrow \langle n_0|n_1\rangle + \langle n_1|n_0\rangle = 0 \longrightarrow \langle n_0|n_1\rangle \text{ is pure imaginary}$$

$$\longrightarrow |n\rangle = |n_0\rangle + \lambda|n_1\rangle = |n_0\rangle + \lambda\,(ia)|n_0\rangle + \lambda\underbrace{\sum_{k\neq 0}\langle k_0|n_1\rangle|k_0\rangle}_{\perp\,|n_0\rangle}$$

$$= e^{i\alpha}|n_0\rangle + \lambda\,(\text{contributions} \perp |n_0\rangle)$$

We are free to redefine the phase of $|n\rangle$, for example

by setting $a=0$. With that choice the first order correction has no projection onto $|n_0\rangle$

$$\langle n_0|n_1\rangle = 0$$

$$\longrightarrow E_n^{(2)} = \langle n_0|\hat{V}|n_1\rangle = \langle n_0|\hat{V}\sum_{k\neq n}|k_0\rangle\frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}$$

$$\boxed{\,E_n^{(2)} = \sum_{k\neq n}\frac{\left|\langle k_0|\hat{V}|n_0\rangle\right|^2}{E_n^{(0)} - E_k^{(0)}}\,}$$

### Observations

- The second order correction to the ground-state energy is always negative, because $E_n^{(0)} - E_k^{(0)} < 0$ while the numerator is a square.

- Treating the perturbation as a small correction is only justified when the matrix elements between "neighboring" states are small relative to the spacing of the unperturbed energy levels.

$$\lambda\langle m|\hat{V}|n\rangle \ll \left|E_n^{(0)} - E_m^{(0)}\right| \qquad m\neq n$$

## 3.2 Quadratic Stark effect

When an atom sits in an E-field, the electrons and the nucleus are tugged in opposite directions, producing an electric dipole. We treat a Hydrogen atom subject to the perturbation.

$$\hat{V} = eEz = eEr\cos\theta$$

At first glance the heavy degeneracy of the H atom seems to rule out our method. In fact, this is a situation where "selection rules" eliminate nearly all matrix elements, leaving a problem that non-degenerate perturbation theory can handle.

With the perturbation directed along the $z$ axis, the Hamiltonian remains invariant under rotations about $z$ $\rightarrow [\hat{H}, \hat{L}_z] = 0$

Consequently the $m$ quantum number stays conserved, and the perturbation does not mix states of different $m$.

$$\langle n, \ell, m' | \hat{z} | n, \ell, m \rangle = 0 \quad m \neq m'$$

So the only corrections to $|1,0,0\rangle$ arise from $|n, \ell, 0\rangle$. Furthermore, one can show that only the $n \neq 1$, $\ell = 1$ terms contribute.

The first order correction to the energy will be

$$E_1^{(1)} = \langle 100 | eEz | 100 \rangle$$

Since $\psi_{100}(\vec{r}) \sim e^{-r/a_0}$ this matrix element is

$$\langle 100 | z | 100 \rangle = \int \psi_{100}^{*}\, r\cos\theta\, \psi_{100}\, r^2 \, dr\, \sin\theta\, d\theta\, d\varphi = 0$$

The second order term is

$$E_1^{(2)} = \sum_{n \neq 1} \frac{|\langle n10 | eEz | 100 \rangle|^2}{E_n - E_1}$$

This is not easy to evaluate, but we can obtain an upper bound by observing that

$$|E_1 - E_n| \geq |E_1 - E_2|$$

$$\rightarrow |E_1^{(2)}| < \frac{1}{E_2 - E_1} \sum_{n \neq 1} |\langle n10 | eEz | 100 \rangle|^2$$

$$= \frac{e^2 E^2}{E_2 - E_1} \sum_{\substack{n \neq 1 \\ \ell m}} \langle 100 | z | n\ell m \rangle \langle n\ell m | z | 100 \rangle \quad \text{(We used selection rules)}$$

Reinserting a complete set of eigenstates lets us invoke the identity

$$\sum_{n\ell m} |n\ell m\rangle\langle n\ell m| = \mathbb{1}$$

and we may now include $n=1$ since the denominator has been altered. Hence,

$$|E_1^{(2)}| < \frac{1}{E_2 - E_1} \langle 100 | e^2 E^2 z^2 | 100 \rangle$$

For the ground state of H, $\langle 100 | z^2 | 100 \rangle = \dfrac{a_0^2}{3}$

$E_1 = -e^2/2a_0$ ; $E_2 = E_1/4$

$$\rightarrow |E_1^{(2)}| < \frac{8}{3} E^2 a_0^3$$

Moreover, since every term in the series for $E^{(2)}$ is negative, we can also pin down a lower bound

$$|E_1^{(2)}| > \frac{|\langle 210 | eEz | 100 \rangle|^2}{E_2 - E_1} = 0.55 \times \frac{8}{3} E^2 a_0^3$$

As it happens, this problem can be solved exactly, giving $E_1^{(2)} = \dfrac{9}{4} E^2 a_0^3$

**Example:** Harmonic oscillator in an electric field.

$$\hat{H}_0 = \frac{\hat{p}^2}{2m} + \frac{1}{2} m\omega^2 \hat{x}^2$$

$$\hat{V} = -qE\hat{x}$$

**Solution:**

$$E_n^{(0)} = \hbar\omega \left( n + \tfrac{1}{2} \right)$$

We use $\hat{x} = \sqrt{\dfrac{\hbar}{2m\omega}} \, (a + a^\dagger)$

$$\rightarrow E_n^{(1)} = \langle n | \hat{V} | n \rangle = -qE\sqrt{\frac{\hbar}{2m\omega}} \langle n | a + a^\dagger | n \rangle = 0$$

The second order correction will be

$$E_n^{(2)} = \sum_{k \neq n} \frac{|\langle k | V | n \rangle|^2}{\hbar\omega\left(n + \tfrac{1}{2}\right) - \hbar\omega\left(k + \tfrac{1}{2}\right)}$$

The perturbation only mixes states with $k = n \pm 1$

$$(a + a^\dagger)|n\rangle = \sqrt{n+1}\,|n+1\rangle + \sqrt{n}\,|n-1\rangle$$

$$\rightarrow E_n^{(2)} = \frac{q^2 E^2 \hbar}{2m\omega} \left( \frac{n+1}{-\hbar\omega} + \frac{n}{\hbar\omega} \right) = -\frac{q^2 E^2}{2m\omega^2}$$

**Example:** Non-linear oscillator

$$H_0 = \frac{\hat{p}^2}{2m} + \frac{m\omega^2 \hat{x}^2}{2}$$

$$V = \lambda \frac{\hat{x}^4}{4}$$

**Solution:**

It is convenient to recast these expressions in terms of bosonic operators

$$V = \frac{\lambda \hbar^2}{16 m^2\omega^2} \left( (a^\dagger)^4 + 4(a^\dagger)^3 a + 6\left(a^\dagger a\right)^2 + a^4 + 6(a^\dagger)^2 + 6a^2 + 6a^\dagger a + 3 \right)$$

$$E_n^{(1)} = \lambda \langle n | \hat{V} | n \rangle = \frac{\lambda \hbar^2}{16 m^2\omega^2} \langle n | 6n^2 + 6n + 3 | n \rangle$$

$$= \frac{3\lambda \hbar^2}{8 m^2\omega^2} \left( n^2 + n + \tfrac{1}{2} \right) = \frac{3\lambda}{8 m^2\omega^4} \frac{n^2 + n + \tfrac{1}{2}}{(n + \tfrac{1}{2})^2} \left( E_n^{(0)} \right)^2$$

with $E_n^{(0)} = \hbar\omega\left( n + \tfrac{1}{2} \right)$

## 3.3 Degenerate perturbation theory

The formalism above breaks down once degeneracies appear, because of the difference $E_n^{(0)} - E_m^{(0)}$ sitting in the denominator.

**Example:** 2D harmonic oscillator

$$H_0 = \frac{\hat{p}_x^2 + \hat{p}_y^2}{2m} + \frac{1}{2} m\omega^2 (\hat{x}^2 + \hat{y}^2)$$

$$= \hat{H}_{0x} + \hat{H}_{0y}$$

$\rightarrow$ The eigenstates are products

$$|n_x, n_y\rangle = |n_x\rangle \otimes |n_y\rangle$$

With energies

$$E_{n_x n_y} = E_{n_x} + E_{n_y} = \hbar\omega\left( n_x + n_y + 1 \right)$$

Suppose we introduce a small perturbation

$$\hat{V} = \alpha m\omega^2 \hat{x}\hat{y}$$

where $\alpha$ is a small parameter

Notice that

$$\hat{V} = \alpha m\omega^2 \frac{\hbar}{2m\omega} (a_x + a_x^\dagger)(a_y + a_y^\dagger)$$

Hence, the first order correction

$$E_{n_x n_y}^{(1)} = \langle n_x n_y | V | n_x n_y \rangle = 0$$

Going to second order, the theory falls apart

$$E_{10}^{(0)} = E_{01}^{(0)}$$

And yet we know this tiny perturbation cannot "destroy" the oscillator. By combining the $x^2 + y^2$ term with the $xy$ perturbation we complete the square, obtaining an oscillator whose equipotential surfaces are ellipses.

&nbsp;&nbsp;&nbsp;&nbsp;unperturbed &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perturbed

*(Figure: left — concentric circles centered on origin with cross axes; right — concentric ellipses tilted along a diagonal axis.)*

*end lecture*

In the original problem, rotational symmetry lets us orient the $x$-$y$ axes however we like. In the new one it pays to align them with the axes of symmetry. In that representation the corrections to the unperturbed eigenstates come out small.

**Solution:** choose a basis set in a degenerate subspace such that the perturbation is diagonal in this representation!

For the problem above, the solution can in fact be found exactly

$$\frac{1}{2} m\omega^2 (x^2 + y^2) + \alpha m\omega^2 xy$$

$$= \frac{1}{2} m\omega^2 \left[ (1 + \alpha)\left( \frac{\hat{x} + \hat{y}}{\sqrt{2}} \right)^2 + (1 - \alpha)\left( \frac{\hat{x} - \hat{y}}{\sqrt{2}} \right)^2 \right]$$

$$\hbar\omega \rightarrow \hbar\omega\sqrt{1 \pm \alpha} \approx \hbar\omega\left( 1 \pm \frac{\alpha}{2} \right)$$

Let us make these ideas precise. Suppose the unperturbed eigenstates $|n^{(0)}\rangle$; $n = 1, \dots, g$ carry energies $E_n^{(0)}$ that are equal or nearly so.

*(Figure: Energy level diagram. Left side — before perturbation: a level $E_1^{(0)}$ labeled "$g$-fold degenerate before perturbation," and a higher level $E_{g+1}^{(0)}$. Right side — after perturbation: the $g$-fold level splits into $g$ separate levels labeled $E_1', \dots, E_g$, "$g$ values"; the $E_{g+1}^{(0)}$ level remains above.)*

The cure is to build a new basis out of the eigenstates of $V$. We will see that adding the corresponding eigenvalues to the unperturbed energies produces the first order correction. Label these new states as

$$|\tilde{n}\rangle = \sum_{i=1}^{g} C_{ni} |i\rangle$$

that satisfy $V|\tilde{n}\rangle = V_n |\tilde{n}\rangle$

Together with the complementary collection of non-degenerate states $\{|m^{(0)}\rangle\,;\, m > g\}$ they make up a new orthonormal basis

$$\left\{ |\tilde{1}\rangle, |\tilde{2}\rangle, \dots, |\tilde{g}\rangle, |g+1^{(0)}\rangle, |g+2^{(0)}\rangle, \dots \right\}$$

the matrix $V$ in this basis looks like

$$V = \begin{pmatrix} V_{1}V_{2} & 0 & V_{1,g+1} & \cdots \\ 0 & V_g & V_{g,g+1} & \cdots \\ \hline V_{g+1,1} \cdots V_{g+1,g} & & & \\ \vdots & \vdots & & \end{pmatrix}$$

We now show that the diagonal elements are the first order corrections to $E_n^{(0)}$. The Schrödinger eq for the total Hamiltonian is

$$\hat{H}|n\rangle = (\hat{H}_0 + \hat{V})|n\rangle = E_n |n\rangle$$

We now substitute

$$|n\rangle = |\tilde{n}\rangle$$
$$E_n = E_n^{(0)} + E_n^{(1)} \quad\Big\}\quad n \leq g$$

$$\hat{H}_0 |\tilde{n}\rangle + \hat{V}|\tilde{n}\rangle = E_n^{(0)}|\tilde{n}\rangle + E_n^{(1)}|\tilde{n}\rangle$$

$$\rightarrow V|\tilde{n}\rangle = E_n^{(1)}|\tilde{n}\rangle$$

because $H_0|\tilde{n}\rangle = E_n^{(0)}|\tilde{n}\rangle$; the $|\tilde{n}\rangle$ are linear combinations of degenerate eigenstates of $H_0$, and are therefore themselves degenerate eigenstates of $H_0$.

This shows that the eigenvalues of $V$ supply the first order energy corrections for $n \leq g$, with $E_n^{(1)} = V_n$

In this new basis the ambiguities caused by the degeneracy of $H_0$ disappear, and we can carry on with the machinery built for non-degenerate perturbation theory:

$$|n\rangle = |\tilde{n}\rangle + \lambda|\tilde{n}^{(1)}\rangle + \lambda^2|\tilde{n}^{(2)}\rangle + \cdots \quad (n \leq g)$$
$$|n\rangle = |n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \lambda^2|n^{(2)}\rangle + \cdots \quad (n > g)$$

$$E_n = E_n^{(0)} + \lambda V_n + \lambda^2 E_n^{(2)} \quad (n \leq g)$$
$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} \quad (n > g)$$

with $V_n = \langle \tilde{n} | V | \tilde{n} \rangle$

$$E_n^{(1)} = \langle n^{(0)} | V | n^{(0)} \rangle$$

**Example:** two-level system

$$\hat{H} = \begin{pmatrix} E_0 & V \\ V & E_1 \end{pmatrix} = \begin{pmatrix} E_0 & 0 \\ 0 & E_1 \end{pmatrix} + \begin{pmatrix} 0 & V \\ V & 0 \end{pmatrix}$$

we may regard $E_0$ and $E_1$ as the unperturbed energies and $V$ as the perturbation that couples the two states. In the language of spin operators, this becomes

$$\hat{H} = \frac{(E_0 + E_1)}{2} \hat{\mathbb{1}} + (E_0 - E_1)\hat{S}^z + 2V\hat{S}^x$$

The eigenvalues of this $2\times2$ problem can be easily obtained

$$E_\pm = \frac{1}{2}(E_0 + E_1) \pm \frac{1}{2}\sqrt{(E_0 - E_1)^2 + 4V^2}$$

Rather than write out the exact eigenstates, consider the limit $|E_0 - E_1| \gg V$

$$\pm \frac{1}{2}\sqrt{(E_0 - E_1)^2 + 4V^2} \approx \pm\frac{1}{2}(E_0 - E_1) + \frac{V^2}{E_0 - E_1}$$

$$\rightarrow E_+ = E_0 + \frac{V^2}{E_0 - E_1} \;;\; E_- = E_1 + \frac{V^2}{E_1 - E_0}$$

This matches non-degenerate perturbation theory. The corresponding eigenstates are:

$$|+\rangle = |0\rangle - \frac{V}{E_1 - E_0}|1\rangle$$

$$|-\rangle = |1\rangle - \frac{V}{E_1 - E_0}|0\rangle$$

The case $E_0 = E_1$ is known as a resonance.

The eigenenergies and eigenstates are

$$E_+ = E_0 + V \;;\; |+\rangle = \frac{1}{\sqrt{2}}\left( |0\rangle + |1\rangle \right)$$

$$E_- = E_0 - V \;;\; |-\rangle = \frac{1}{\sqrt{2}}\left( |0\rangle - |1\rangle \right)$$

*(Figure: Energy vs $E_0 - E_1$. Two solid curves: an upper branch labeled $E_+$ that comes from $E_1$ on the left and approaches $E_0$ on the right, and a lower branch labeled $E_-$ that comes from $E_0$ on the left and approaches $E_1$ on the right. Dashed diagonal lines (the unperturbed levels) cross at the origin; the solid curves show an avoided crossing.)*

The perturbation opens a gap: an __avoided level crossing__. A genuine crossing is possible only when the matrix elements between the two states vanish, which usually signals an underlying symmetry. With no symmetry present we instead see __level repulsion__, so the energy levels refuse to cross as a parameter in the Hamiltonian is tuned.

**Example:** 2d-harmonic oscillator

$$\hat{H}_0 = \hat{H}_{0x} + \hat{H}_{0y}$$

$$\hat{V} = \alpha m\omega^2 \hat{x}\hat{y}$$

$\hat{H}_0$ is degenerate in pairs $(nm)$. Let us consider the case $n=0$; $m=1$

$$V = \begin{pmatrix} \langle 01 | V | 01 \rangle & \langle 01 | V | 10 \rangle \\ \langle 10 | V | 01 \rangle & \langle 10 | V | 10 \rangle \end{pmatrix}$$

We recall the identity:

$$\hat{V} = \frac{\alpha\omega\hbar}{2} (a_x + a_x^\dagger)(a_y + a_y^\dagger)$$

that allows us to obtain the matrix elements

$$\langle 01 | V | 01 \rangle = \langle 10 | V | 10 \rangle = 0 \;;\; \langle 01 | V | 10 \rangle = \frac{\alpha\omega\hbar}{2}$$

$$\rightarrow V = \begin{pmatrix} 0 & \dfrac{\alpha\omega\hbar}{2} \\ \dfrac{\alpha\omega\hbar}{2} & 0 \end{pmatrix}$$

which has eigenvalues

$$V_\pm = \pm \frac{\alpha\omega\hbar}{2}$$

*(Figure: level $E_{10}$ splits into $E_+ = E_{10} + \dfrac{\alpha\omega\hbar}{2}$ and $E_- = E_{10} - \dfrac{\alpha\omega\hbar}{2}$.)*

the corresponding wave functions are

$$|10_\pm\rangle = \frac{1}{\sqrt{2}}\left( |10\rangle \pm |01\rangle \right)$$

We now recall the exact eigenvalues

$$\hbar\omega \rightarrow \hbar\omega\sqrt{1 \pm \alpha} \approx \hbar\omega\left( 1 \pm \frac{\alpha}{2} \right)$$

## 3.4 Linear Stark effect

Let us turn to the first excited states of Hydrogen $|2,0,0\rangle$, $|2,1,-1\rangle$, $|2,1,0\rangle$, $|2,1,1\rangle$. This manifold is four-fold degenerate, so we must diagonalize a $4\times4$ matrix. As noted before, only matrix elements between states sharing the same quantum number $m$ survive. Here only a single such term exists:

$$\langle 210 | z | 200 \rangle = \int_0^\infty r^2\, dr \int_0^\pi \sin\theta\, d\theta \int_0^{2\pi} d\varphi\; \psi_{210}^{*}\, r\cos\theta\, \psi_{200}$$

$$= -3a_0$$

Therefore, the $4\times4$ matrix is

$$\begin{pmatrix} 0 & -3eEa_0 & 0 & 0 \\ -3eEa_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Its eigenvalues can be readily obtained as

$$E_2^{(1)} = 0,\; 0,\; 3eEa_0,\; -3eEa_0$$

with eigenstates

$$|2,1,1\rangle,\; |2,1,-1\rangle,\; \frac{1}{\sqrt{2}}\left( |210\rangle - |200\rangle \right),\; \frac{1}{\sqrt{2}}\left( |200\rangle + |210\rangle \right)$$

The first two states stay unshifted thanks to the rotational symmetry in the $x$-$y$ plane. Note that, in contrast to the quadratic shift of the ground state, here the shift is linear.

*(Figure: the degenerate level splits into three: top — $\frac{1}{\sqrt{2}}(|210\rangle - |200\rangle)$ shifted up by $3eEa_0$; middle (unshifted) — $|211\rangle$, $|21-1\rangle$; bottom — $\frac{1}{\sqrt{2}}(|210\rangle + |200\rangle)$ shifted down by $3eEa_0$.)*


---

## References and Further Reading

*Editorial addition mapping the notes to their source text.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 11 (Time-Independent Perturbations) — non-degenerate and degenerate perturbation theory and the Stark effect.

**Further reading.** Sakurai & Napolitano, the "Approximation Methods" chapter; Griffiths & Schroeter, the "Time-Independent Perturbation Theory" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XI.
# Chapter 4 — Time-Dependent Perturbation Theory

*The clock sets the rule: how fast the Hamiltonian changes decides whether you reach for the sudden, the adiabatic, or the resonant approximation.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Until now the Hamiltonian held still and we asked how its energies shifted. Here it moves, and the whole question changes: not "what are the corrected levels?" but "starting in state $|i\rangle$, what is the chance of landing in $|f\rangle$ later?" Energy is no longer conserved, so we stop tracking it and track amplitudes instead.

The honest organizing idea is that the clock picks the method. Compare how fast the perturbation changes against the system's own natural timescale, $1/\omega_{mn}$. Flip the Hamiltonian faster than the state can respond and the wave function is caught frozen — the sudden approximation, where the old state simply gets re-read in the new basis. Change it slowly enough and the state rides along, staying in the same instantaneous eigenstate — the adiabatic theorem, which carries a quiet surprise: a geometric (Berry) phase that remembers the path, not the clock. In between sits the driven middle ground, where a perturbation oscillating near a level spacing pumps probability back and forth — resonance, Rabi oscillations, and, taken to long times, Fermi's golden rule for steady transition rates.

Everything below is first- and second-order perturbation theory applied to one moving Hamiltonian. The trick is reading the clock before choosing the tool.

## 4. Time-dependent perturbation theory

We consider a Hamiltonian of the form

$$\hat{H} = \hat{H}_0 + \hat{V}(t) = \hat{H}_0 + \lambda f(t)\hat{V}$$

where the time profile of the perturbation lives in $f(t)$. We take the unperturbed problem $H_0$ to be already solved

$$\hat{H}_0 |n\rangle = E_n |n\rangle$$

No extra labels are needed here: energy is not conserved anymore, and we are not chasing energy corrections.

When $V=0$ the answer is immediate,

$$|\psi(t)\rangle = \sum_n C_n e^{-iE_n t/\hbar} |n\rangle$$

with the $C_n$ constant. Switch on the perturbation and these coefficients start to vary with time,

$$|\psi(t)\rangle = \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

*end lecture*

fixed by the Sch. eq.

$$i\hbar \frac{\partial}{\partial t} \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle = (\hat{H}_0 + \hat{V}(t)) \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

$$\rightarrow i\hbar \sum_n \dot{C}_n(t)\, e^{-iE_n t/\hbar} |n\rangle = \hat{V}(t) \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

Projecting onto the bra $\langle m | e^{\frac{iE_m t}{\hbar}}$

$$i\hbar \dot{C}_m = \sum_n \langle m | \hat{V}(t) | n \rangle\, C_n\, e^{i\omega_{mn} t} = \sum_n V_{mn}\, e^{i\omega_{mn} t}\, C_n$$

where $\omega_{mn} = \dfrac{E_m - E_n}{\hbar}$

This gives a coupled system of differential equations for the $C$'s

$$i\hbar \begin{pmatrix} \dot{C}_1 \\ \dot{C}_2 \\ \vdots \end{pmatrix} = \begin{pmatrix} V_{11} & V_{12}\, e^{i\omega_{12} t} & \cdots \\ V_{21}\, e^{i\omega_{21} t} & V_{22} & \\ \vdots & & V_{33} \end{pmatrix} \begin{pmatrix} C_1 \\ C_2 \\ \vdots \end{pmatrix}$$

Nothing has been approximated yet. As in the time-independent case, we now attack it order by order.

Suppose the system starts in some state $|i\rangle$ at $t=0$. We want the probability that, after evolving, it is found in a state $|f\rangle$.

Expand

$$C_f(t) = \delta_{fi} + \lambda\, C_f^{(1)}(t) + \lambda^2\, C_f^{(2)}(t) + \cdots$$

Substituting this into $\circledast$ above gives

$$C_f^{(1)}(t) = -\frac{i}{\hbar}\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\,\langle f|\hat{V}|i\rangle$$

so

$$C_f(t) = \delta_{fi} - \frac{\lambda i}{\hbar}\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\, V_{fi}$$

The probability of ending up in $|f\rangle \neq |i\rangle$ is

$$|C_f(t)|^2 = \frac{\lambda^2}{\hbar^2}|V_{fi}|^2\left|\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\right|^2$$

This estimate is reliable only when the transition probability stays small. Pushing to the next order gives the second-order correction.

$$C_n^{(2)} = \left(\frac{-i\lambda}{\hbar}\right)^2\sum_m \int_0^t dt'\int_0^{t'} dt''\, e^{i\omega_{mn} t'}\, V_{mn}\, f(t')\times e^{i\omega_{mi} t''}\, V_{mi}\, f(t'')$$

### Example: Kicking an oscillator

Take a harmonic oscillator sitting in its ground state at $t=-\infty$, and hit it with a weak potential

$$\hat{V}(t) = -eE\hat{x}\, e^{-t^2/\tau^2}$$

What is the chance of finding it in the first excited state $|1\rangle$ at $t=+\infty$?

**Solution:** $\quad V_{fi}(t) = -eE\langle 1|\hat{x}|0\rangle\, e^{-t^2/\tau^2}$

with $\hat{x} = \sqrt{\dfrac{\hbar}{2m\omega}}\,(a + a^\dagger)$

$$\to V_{fi}(t) = -eE\sqrt{\frac{\hbar}{2m\omega}}\, e^{-t^2/\tau^2}$$

$$\to C_f(\infty) = -eE\sqrt{\frac{\hbar}{2m\omega}}\int_{-\infty}^{\infty} dt'\, e^{-t^2/\tau^2}\, e^{-i\hbar\omega t'}$$

We finally obtain

$$|C_f(\infty)|^2 = \frac{e^2 E^2}{\hbar^2}\frac{\hbar}{2m\omega}\,\pi\tau^2\, e^{-\omega^2\tau^2/2}$$

### Example: two-level system

$$|\psi(t)\rangle = C_1(t)\, e^{-iE_1 t/\hbar}|1\rangle + C_2(t)\, e^{-iE_2 t/\hbar}|2\rangle$$

Apply a perturbation

$$\hat{V}(t) = V e^{i\omega t}|1\rangle\langle 2| + V e^{-i\omega t}|2\rangle\langle 1|$$

$$\to i\hbar\begin{pmatrix}\dot{C}_1\\[2pt]\dot{C}_2\end{pmatrix} = \begin{pmatrix} 0 & V e^{i\omega t} e^{i\omega_{12} t}\\[4pt] V e^{-i\omega t} e^{-i\omega_{12} t} & 0\end{pmatrix}\begin{pmatrix}C_1\\[2pt]C_2\end{pmatrix}$$

Abbreviate $\omega + \omega_{12} = \alpha$. Then,

$$i\hbar\dot{C}_1 = V e^{i\alpha t}\, C_2$$
$$i\hbar\dot{C}_2 = V e^{-i\alpha t}\, C_1$$

Differentiating the second equation and substituting $\dot{C}_1$ from the first yields

$$\ddot{C}_2 = -i\alpha\dot{C}_2 - \frac{V^2}{\hbar^2}C_2$$

which admits a solution of the form $C_2 = C_2(0)e^{i\Omega t}$

$$\Omega = -\frac{\alpha}{2}\pm\sqrt{\frac{\alpha^2}{4} + \frac{V^2}{\hbar^2}}$$

Hence, the final solution is

$$C_2(t) = e^{-i\frac{(\omega-\omega_{21})}{2}t}\left(A\, e^{i\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t} + B\, e^{-i\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t}\right)$$

With the initial state $C_1(0)=1;\ C_2(0)=0$ we find $A = -B$. To pin down its value, note that

$$\dot{C}_2(0) = \frac{V}{i\hbar}C_1(0) = \frac{V}{i\hbar}$$

$$\to |C_2(t)|^2 = \frac{V^2/\hbar^2}{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\sin^2\left(\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t\right)$$

Note that, in particular for $\omega = \omega_{21}$

$$|C_2(t)|^2 = \sin^2\left(\frac{Vt}{\hbar}\right)$$

So the system sloshes back and forth between $|1\rangle$ and $|2\rangle$ with period $\pi\hbar/2V$. This is the "resonance condition". Oscillations persist off resonance too, but once the freq. $\omega$ strays far from $2V/\hbar$ the transition probability becomes tiny.

*end lecture*

### Example: Spin magnetic resonance

Take a spin-$S=1/2$ particle in a B-field along $z$,

$$\hat{H}_0 = -\mu_B B_0\,\hat{\sigma}^z = -\frac{e}{m_e}B_0\,\hat{S}_z\ ;\quad \mu_B = \frac{e\hbar}{2m_e}$$

Now add a time-dependent B-field rotating in the $x$-$y$ plane,

$$\hat{V} = -\mu_B B_1\left(\cos\omega t\,\hat{\sigma}^x + \sin\omega t\,\hat{\sigma}^y\right)$$

The eigenstates of $\hat{H}_0$ are $|+\rangle$ and $|-\rangle$

$$\hat{H}_0|\pm\rangle = \mp\frac{e\hbar}{2m_e}B_0|\pm\rangle$$

The perturbation can be recast as

$$\hat{V} = \frac{eB_1}{2m_e}\left[e^{i\omega t}\sigma^- + e^{-i\omega t}S^+\right]$$

It follows that $\langle +|\hat{V}|+\rangle = \langle -|\hat{V}|-\rangle = 0$ and

$$\langle -|V|+\rangle = \langle +|V|-\rangle^* = \frac{e\hbar B_1}{2m_e}e^{i\omega t}$$

This maps directly onto the previous case, with $|1\rangle\to|+\rangle$, $|2\rangle\to|-\rangle$; $\omega_{21} = eB_0/m_e$, $V = e\hbar B_1/2m_e$

## 4.1 The sudden approximation

Consider a Hamiltonian that flips abruptly over a tiny time window

*(diagram: vertical dashed line with "before" on the left, "after" on the right, a small interval $\varepsilon$ marked at the transition, arrow labeled "time")*

As an example, suddenly widen a square potential well

*(diagram: a half-wave over the interval $[0,a]$, arrow to a half-wave over $[0,2a]$)*

As $\varepsilon\to 0$ the wave function is identical before and after; the system has no time to "react" to the switch. For the kicked oscillator with a gaussian pulse, taking the limit

*(diagram: gaussian pulse of width $2\tau$)*

$\tau\to 0$ makes the initial and final Hamiltonians coincide, so $P_{0\to 1} = 0$.

### Example: Beta decay

A Hydrogen atom carrying a 1s electron undergoes beta decay. A neutron in the nucleus turns into a proton, throwing off a relativistic electron and an antineutrino. The atom is left with charge $Z+1 = 2$. The 1s electron stays in the ground state belonging to nuclear charge $Z$ — which is no longer an eigenstate of the charge-$Z+1$ ion.

## 4.2 Energy shifts and decay widths

Switch on a perturbation gradually, starting at $t=-\infty$,

$$\hat{V}(t) = \exp(\gamma t)\,\hat{V}_0$$

with $\gamma$ small and positive and $\hat{V}_0$ time independent. Suppose that at $t\to-\infty$ the system sits in the initial state $|i\rangle\to C_i(t=-\infty)=1$, $C_{n\neq i}(t=-\infty)=0$. First-order t-d perturbation theory gives

$$C_n^{(0)}(t) = 0$$

$$C_n^{(1)}(t) = -\frac{i}{\hbar}V_{ni}\int_{-\infty}^t dt'\,\exp\left((\gamma + i\omega_{ni})t\right)$$

$$= -\frac{i}{\hbar}V_{ni}\,\frac{\exp\left((\gamma + i\omega_{ni})t\right)}{\gamma + i\omega_{ni}}$$

where $\omega_{ni} = \frac{1}{\hbar}(E_n - E_i)$ and $V_{ni} = \langle n|\hat{V}_0|i\rangle$

$$\to P_{n\to i} = |C_n^{(1)}|^2 = \frac{|V_{ni}|^2}{\hbar^2}\frac{e^{2\gamma t}}{\gamma^2 + \omega_{ni}^2}$$

The transition rate is

$$R_{i\to f} = \frac{dP_{i\to f}}{dt} = \frac{2|V_{ni}|^2}{\hbar^2}\frac{\gamma\, e^{2\gamma t}}{\gamma^2 + \omega_{ni}^2}$$

As $\gamma\to 0$ this reduces to a "sudden perturbation", since $e^{2\gamma t}\to 1$

$$\to \lim_{\gamma\to 0}\frac{\gamma}{\gamma^2 + \omega_n^2} = \pi\delta(\omega_{ni}) = \pi\hbar\,\delta(E_n - E_i)$$

$$\to R_{i\to f} = \frac{2\pi}{\hbar}|V_{ni}|^2\,\delta(E_n - E_i)$$

Now carry $C_i(t)$ to second order

$$C_i^{(0)}(t) = 1$$

$$C_i^{(1)}(t) = -\frac{i}{\hbar}V_{ii}\int_{-\infty}^t e^{\gamma t'}dt' = -\frac{i}{\hbar}V_{ii}\frac{e^{\gamma t}}{\gamma}$$

$$C_i^{(2)}(t) = \left(\frac{-i}{\hbar}\right)^2\sum_m |V_{mi}|^2\int_{-\infty}^t dt'\int_{-\infty}^{t'} dt''\, e^{(\gamma + i\omega_{im})t'}\, e^{(\gamma + i\omega_{mi})t''}$$

$$= \left(\frac{-i}{\hbar}\right)^2\sum_m |V_{mi}|^2\frac{e^{2\gamma t}}{2\gamma(\gamma + i\omega_{mi})}$$

Examine the ratio $\dot{C}_i/C_i$ as $\gamma\to 0$

$$\frac{\dot{C}_i}{C_i} \approx \left(\frac{-i}{\hbar}\right)V_{ii} + \lim_{\gamma\to 0}\left(\frac{-i}{\hbar}\right)\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m + i\hbar\gamma}$$

Notice the result carries no time dependence. Write it as

$$\frac{\dot{C}_i}{C_i} = \left(\frac{-i}{\hbar}\right)\Delta_i$$

where $\Delta_i = V_{ii} + \lim_{\gamma\to 0}\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m + i\hbar\gamma}$

Using the result $\lim_{\varepsilon\to 0}\frac{1}{x + i\varepsilon} = P\frac{1}{x} - i\pi\delta(x)$

where $\varepsilon>0$ and $P$ denotes the principal part.

$$\to \Delta_i = V_{ii} + P\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m} - i\pi\sum_{m\neq i}|V_{mi}|^2\delta(E_i - E_m)$$

Normalizing so that $C_i(0)=1$

$$C_i(t) = \exp\left(\frac{i\Delta_i}{\hbar}t\right)$$

$$\to |i,t\rangle = \exp\left(-i(\Delta_i + E_i)t/\hbar\right)|i\rangle$$

Notice that $\Delta_i$ is complex:

$$|i,t\rangle = \exp\left(-i(E_i + \mathrm{Re}\,\Delta_i)t/\hbar\right)\exp\left(\mathrm{Im}\,\Delta_i\, t/\hbar\right)|i\rangle$$

or

$$|i,t\rangle = \exp\left(-i(E_i + \Delta E_i)t/\hbar\right)\exp\left(-\frac{\Gamma_i t}{2\hbar}\right)|i\rangle$$

where

$$\Delta E_i = \mathrm{Re}\,\Delta_i = V_{ii} + P\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m}$$

$$\frac{\Gamma_i}{\hbar} = -\frac{2}{\hbar}\mathrm{Im}(\Delta_i) = \frac{2\pi}{\hbar}\sum_{m\neq i}|V_{mi}|^2\delta(E_i - E_m)$$

The first term is an energy shift, matching the one from stationary perturbation theory. The second exponential controls whether the state grows or decays. The probability of still observing $|i\rangle$ is

$$P_{i\to i}(t) = |C_i|^2 = \exp\left(-\Gamma_i t/\hbar\right)$$

where $\frac{\Gamma_i}{\hbar} = \sum_{m\neq i}\omega_{i\to m}$

Probability is conserved through second order, since

$$|C_i|^2 + \sum_{m\neq i}|C_m|^2 \approx 1 - \frac{\Gamma_i t}{\hbar} + \sum_{m\neq i}\omega_{i\to m}t = 1$$

The quantity $\Gamma_i$ is the "decay width". The state's "lifetime" is

$$\tau_i = \hbar/\Gamma_i$$

and

$$P_{i\to i} = \exp(-t/\tau_i)$$

So the amplitude of $|i\rangle$ both oscillates and decays as time goes on.

Because the state changes in time, its energy cannot be sharp. The energy is smeared over a band of width $\Gamma_i$ centered on the shifted value $E_i + \mathrm{Re}\,\Delta_i$. The quicker the decay, the broader the spread.

In spectroscopy this shows up directly: weak lines are narrow, set by slow transitions, while strong lines are broad and smeared out, set by fast ones.

## 4.3 Harmonic perturbations

Take an oscillating potential. If the system starts in $|i\rangle$, what is the probability of finding it in $|f\rangle$ later on?

The initial condition gives $C_i = 1$; $C_j = 0$ for $j \neq i$.

Recall the differential eqs.

$$i\hbar\begin{pmatrix}\dot{C}_1\\\dot{C}_2\\\vdots\end{pmatrix} = \begin{pmatrix} V_{11} & V_{12}e^{i\omega_{12} t} & \cdots\\ V_{21}e^{i\omega_{21} t} & V_{22} & \\ \vdots & & V_{33}\end{pmatrix}\begin{pmatrix}C_1\\C_2\\\vdots\end{pmatrix}$$

To first order we substitute $C_i = 1$; $C_{j\neq i} = 0\ \ j\neq i$ on the right-hand side, which amounts to solving

$$i\hbar\dot{C}_f(t) = V_{fi}\, e^{i\omega_{fi} t}$$

Integrating gives

$$C_f(t) = -\frac{i}{\hbar}\int_0^t \langle f|V|i\rangle\, e^{i(\omega_{fi} - \omega)t'}dt'$$

$$= -\frac{i}{\hbar}\langle f|V|i\rangle\,\frac{e^{i(\omega_{fi} - \omega)t} - 1}{i(\omega_{fi} - \omega)}$$

The transition probability is

$$P_{i\to f}(t) = |C_f|^2 = \frac{|\langle f|V|i\rangle|^2}{\hbar^2}\frac{\sin^2((\omega_{fi} - \omega)t/2)}{\left(\frac{\omega_{fi} - \omega}{2}\right)^2}$$

The oscillating term has the form $\frac{\sin^2\alpha t}{\alpha^2}$

*(plot: a tall central peak of $\frac{\sin^2\alpha t}{\alpha^2}$ at $\alpha t = 0$, with smaller side lobes at $\pm\pi$, $\pm 2\pi$ along the $\alpha t$ axis)*

In the large $t$ limit

$$\lim_{t\to\infty}\frac{\sin^2\alpha t}{\alpha^2} = \pi\delta(\alpha)t$$

$\to$ The transition probability grows linearly in time, so we define a "transition rate"

$$R_{i\to f}(t) = \lim_{t\to\infty}\frac{dP_{i\to f}(t)}{dt} = \frac{\pi}{\hbar^2}|\langle f|V|i\rangle|^2\,\delta\left(\frac{\omega_{fi} - \omega}{2}\right)$$

$$= \frac{2\pi}{\hbar^2}|\langle f|V|i\rangle|^2\,\delta(\omega_{fi} - \omega)$$

"Fermi's Golden Rule"

How can the transition probability diverge? The catch is that "long time" here means $(\omega_{fi} - \omega)t \gg 1$, which can happen at a genuinely short clock time.

**Validity:** Rewrite $P_{i\to f} = \frac{|V_{fi}|^2}{\hbar^2}\frac{\sin^2(\alpha t)}{\alpha^2}$

with $\alpha = \frac{\omega_{fi} - \omega}{2}$

Multiplying and dividing by $t^2$,

$$P_{i\to f} = \frac{|V_{fi}|^2 t^2}{\hbar^2}\frac{\sin^2(\alpha t)}{\alpha^2 t^2} = \frac{|V_{fi}|^2 t^2}{\hbar^2}\eta(\alpha t)$$

with $\eta(x) = \frac{\sin^2 x}{x^2}\in[0,1]$

$$\to \text{we want}\quad \frac{|V_{fi}|^2 t^2}{\hbar^2}\ll 1,\quad\text{or}$$

$$\boxed{\,t \ll \frac{\hbar}{|V_{fi}|}\,}$$

On top of that, viewed as a function of $\alpha t$, the approximation holds when

$$\boxed{\,|t|\,|\omega_{fi}| > 2\pi\,}$$

Putting both together, we arrive at

$$\boxed{\,\frac{2\pi}{|\omega_{fi}|} \lesssim t \ll \frac{\hbar}{|V_{fi}|}\,}$$

## 4.4 The adiabatic theorem

Suppose the Hamiltonian drifts slowly from $H(t=0)$ to $H(t=T)$. The adiabatic theorem says that if the system begins in the $n^{th}$ eigenstate of $H(0)$, it ends in the $n^{th}$ eigenstate of $H(T)$. The proof requires a discrete, non-degenerate spectrum.

### Example: particle in an infinite well

*(diagram: at $t=0$, a half-wave over $[0,a]$; arrow to $t=T$, a half-wave over $[0,2a]$)*

Even though we demand the process be slow, energy is not conserved.

**Proof:** $\quad H\psi_n = E_n\psi_n$

For a time-independent Hamiltonian, the wave function merely acquires a phase

$$\psi_n(t) = e^{-iE_n t/\hbar}\psi_n(t=0)$$

Once the Hamiltonian varies in time, both eigenvalues and eigenfunctions become time dependent

$$H(t)\psi_n(t) = E_n(t)\psi_n(t)\quad\circledast$$

with $\langle\psi_n(t)|\psi_m(t)\rangle = \delta_{nm}$

The general solution of the Schrödinger eq. can be written

$$\psi(t) = \sum_n C_n(t)\psi_n(t)\, e^{i\theta_n(t)}$$

where

$$\theta_n(t) = -\frac{1}{\hbar}\int_0^t E_n(t')\, dt'$$

generalizes the phase factor to the time-dependent setting.

Substituting into the t-d Schrödinger eq. gives

$$i\hbar\sum_n\left(\dot{C}_n\psi_n + C_n\dot{\psi}_n - \frac{i}{\hbar}C_n\psi_n\dot{\theta}_n\right)e^{i\theta_n} = \sum_n C_n\hat{H}\psi_n e^{i\theta_n}$$

$$\underbrace{C_n\psi_n E_n}\qquad\qquad\underbrace{C_n E_n\psi_n}$$

$$\to \sum_n \dot{C}_n\psi_n e^{i\theta_n} = -\sum_n C_n\dot{\psi}_n e^{i\theta_n}$$

Taking the inner product with $\psi_m$ and invoking the orthogonality of the instantaneous wave functions:

$$\sum_n \dot{C}_n\delta_{mn}e^{i\theta_n} = -\sum_n C_n\langle m|\dot{n}\rangle e^{i\theta_n}$$

or

$$\dot{C}_m(t) = -\sum_n C_n\langle m|\dot{n}\rangle e^{i(\theta_n - \theta_m)}\quad\circledast$$

Differentiating $\circledast$ in time,

$$\dot{H}\psi_n + H\dot{\psi}_n = \dot{E}_n\psi_n + E_n\dot{\psi}_n$$

$$\overset{\langle\psi_m|}{\longrightarrow}\ \langle m|\dot{H}|n\rangle + \langle m|H|\dot{n}\rangle = \dot{E}_n\delta_{mn} + E_n\langle m|\dot{n}\rangle$$

$$\underbrace{E_m\langle m|\dot{n}\rangle}$$

$$\to \langle m|\dot{H}|n\rangle = (E_n - E_m)\langle m|\dot{n}\rangle$$

Inserting into $\circledast$

$$\dot{C}_m(t) = -C_n\langle m|\dot{m}\rangle - \sum_{n\neq m}C_n\frac{\langle m|\dot{H}|n\rangle}{E_n - E_m}e^{-\frac{i}{\hbar}\int_0^t(E_n(t') - E_m(t'))dt'}$$

This is exact. Now invoke the adiabatic assumption — $\dot{H}$ is very small — and drop the second term.

$$\dot{c}_m(t) = -c_m \langle m | \dot{m} \rangle$$

$$\rightarrow c_m(t) = c_m(0)\, e^{i\gamma_m(t)}$$

where

$$\gamma_m(t) = i \int_0^t \left\langle \psi_m(t') \,\Big|\, \frac{\partial}{\partial t'} \psi_m(t') \right\rangle dt'$$

In particular, if the system starts out in the $n^{\text{th}}$ eigenstate, $c_n(0)=1$, $c_m(0)=0$ for $n \neq m$,

$$\psi(t) = e^{i\theta_n(t)}\, e^{i\gamma_n(t)}\, \psi_n(t)$$

so it stays in the $n^{\text{th}}$ eigenstate of the evolving Hamiltonian, apart from phase factors.

## 4.5 Berry's phase

In that last expression, $\theta_n(t)$ is the "dynamic phase" and $\gamma_n(t)$ is the "geometric phase". Suppose the time-dependence enters through a single time-varying parameter in the Hamiltonian, $R(t)$.

$$\frac{\partial \psi_n}{\partial t} = \frac{\partial \psi_n}{\partial R} \cdot \frac{dR}{dt}$$

$$\rightarrow \gamma_n(t) = i \int_0^t \left\langle \psi_n \Big| \frac{\partial \psi_n}{\partial R} \right\rangle \frac{dR}{dt'}\, dt' = i \int_{R_i}^{R_f} \left\langle \psi_n \Big| \frac{\partial \psi_n}{\partial R} \right\rangle dR$$

where $R_i$ and $R_f$ are the starting and ending values of $R(t)$. In particular, if the system comes back to its original configuration after $t = T$

$$\rightarrow R_i = R_f \rightarrow \gamma_n(T) = 0$$

But now let several parameters vary together in time.

$$\frac{\partial \psi_n}{\partial t} = \frac{\partial \psi_n}{\partial R_1}\frac{dR_1}{dt} + \cdots + \frac{\partial \psi_n}{\partial R_N}\frac{dR_N}{dt} = (\vec{\nabla}_R \psi_n) \cdot \frac{d\vec{R}}{dt}$$

where $\vec{R} = (R_1, \ldots R_N)$; $\vec{\nabla}_R = \left(\frac{\partial}{\partial R_1}, \ldots \frac{\partial}{\partial R_N}\right)$.

Now we have

$$\gamma_n(t) = i \int_{R_i}^{R_f} \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \cdot d\vec{R}$$

if $\vec{R}_i = \vec{R}_f$, this becomes

$$\gamma_n(T) = i \oint \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \cdot d\vec{R} \qquad \text{``Berry's phase''}$$

a loop integral in parameter space that, in general, does not vanish.

Notice that $\gamma_n$ depends on the path traced through parameter space, whereas $\theta_n$ depends only on the elapsed time.

**Example:** A beam of particles in state $\psi_0$ is split in two, with one arm sent through a slowly varying potential. Once the beams recombine, the total wave function reads

$$\psi = \tfrac{1}{2}\psi_0 + \tfrac{1}{2}\psi_0 e^{i\Gamma}$$

where the geometric and dynamic phases are included in $\Gamma$

$$|\psi|^2 = \tfrac{1}{4}|\psi_0|^2 \left(1 + e^{i\Gamma}\right)\left(1 + e^{-i\Gamma}\right)$$

$$= \tfrac{1}{2}|\psi_0|^2 (1 + \cos\Gamma) = |\psi_0|^2 \cos^2(\Gamma/2)$$

So $\Gamma$ is read off directly from the interference pattern.

When parameter space is 3-dimensional, $\vec{R} = (R_1, R_2, R_3)$, Berry's formula mirrors the expression for magnetic flux in terms of the vector potential $\vec{A}$.

$$\Phi = \int_S \vec{B} \cdot d\vec{a} = \int_S (\vec{\nabla} \times \vec{A}) \cdot da = \oint \vec{A} \cdot d\vec{r}$$

*(diagram: a closed loop $C$ enclosing a surface with area element $d\vec{a}$)*

The Berry's phase can be thought of as the "flux" of a "magnetic field"

$$\vec{\Omega}_R \equiv \vec{B} = i\, \vec{\nabla}_R \times \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \qquad \text{(Berry curvature)}$$

through the closed-loop trajectory in parameter space. Equivalently, Berry's phase becomes a surface integral

$$\gamma_n(T) = i \int \left( \vec{\nabla}_R \times \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \right) \cdot d\vec{a}$$

The equivalent "vector potential"

$$\vec{A} = \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \qquad \text{(Berry connection)}$$

is called "Berry connection".

**Example:** two-level system. Spin in a magnetic field.

Take a spin-$\tfrac{1}{2}$ in a magnetic field pointing in an arbitrary direction relative to the $z$-axis.

$$H = \mu \vec{J} \cdot \vec{B}$$

The eigenenergies are $\pm \mu B$ and the eigenvectors are

$$|-\rangle = \sin\tfrac{\theta}{2} e^{-i\varphi} |1\rangle - \cos\tfrac{\theta}{2}|2\rangle$$

$$|+\rangle = \cos\tfrac{\theta}{2} e^{-i\varphi}|1\rangle + \sin\tfrac{\theta}{2}|2\rangle$$

Focus on the $|-\rangle$ state.

$$A_\theta = \langle - | i\tfrac{\partial}{\partial\theta} | - \rangle = 0 \quad;\quad A_\varphi = \langle - | i\tfrac{\partial}{\partial\varphi} | - \rangle = \sin^2\tfrac{\theta}{2}$$

The Berry curvature is

$$\Omega_{\theta\varphi} = \frac{\partial}{\partial\theta}A_\varphi - \frac{\partial}{\partial\varphi}A_\theta = \tfrac{1}{2}\sin\theta$$


---

## References and Further Reading

*Editorial addition mapping the notes to their source text. The two-level system is cited in the text as Townsend Example 4.2.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 14 (Photons and Atoms) for time-dependent perturbation theory and Fermi's golden rule; Ch. 4 (Time Evolution) for two-level dynamics (Example 4.2).

**Further reading.** Sakurai & Napolitano, the "Approximation Methods" chapter (time-dependent perturbation theory, the sudden and adiabatic approximations, Berry's phase); Griffiths & Schroeter, the "Time-Dependent Perturbation Theory" and "The Adiabatic Approximation" chapters; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XIII.
# Chapter 5 — Identical Particles

*When particles become truly interchangeable, indistinguishability forces the wave function into strict symmetry — and exchange turns into a real energy with no classical shadow.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Here is the puzzle that drives this whole chapter. Take two electrons. Not "two electrons that look alike" — two electrons that are genuinely, perfectly the same. There is no sticker, no serial number, nothing in principle that tells one from the other. Now swap them. Nothing observable can change, because nothing distinguished them to begin with.

That single fact does almost all the work. If swapping two particles must leave every measurable prediction alone, the state can only pick up a sign: $+1$ or $-1$. Bosons take the plus and pile into symmetric states; fermions take the minus and live in antisymmetric ones. From the minus sign alone you get the Pauli exclusion principle — two fermions cannot share a state, because the antisymmetric combination of identical things is just zero.

The payoff is the part with no classical analogue. When you compute the energy of two interacting particles, the (anti)symmetry splits one interaction integral into two pieces: an ordinary "direct" term you could have guessed classically, and an "exchange" term that exists purely because the particles are indistinguishable. That exchange piece is what separates singlet from triplet, powers Hund's rule, and sets the singlet–triplet splitting in helium. Spin never appears in the Hamiltonian, yet it controls the energy. Keep that thread in mind as we build it up.

## 5 — Identical particles

## 5.1 Intrinsic angular momentum: spin

In quantum mechanics, the spin $\vec{S}$ is a basic attribute of elementary particles with no classical counterpart. It stands on the same footing as mass or charge: an intrinsic property that cannot be altered.

Spin obeys the same algebra as angular momentum:

$$\hat{S} = (\hat{S}^x, \hat{S}^y, \hat{S}^z), \quad \text{with}$$

$$[\hat{S}^x, \hat{S}^y] = i\hbar \hat{S}^z, \quad [\hat{S}^y, \hat{S}^z] = i\hbar \hat{S}^x, \quad [\hat{S}^z, \hat{S}^x] = i\hbar \hat{S}^y$$

We write $|s, m\rangle$ for the joint eigenstates of $\hat{S}^2$ and $\hat{S}^z$

$$\hat{S}^2 |s, m\rangle = \hbar^2 s(s+1)|s, m\rangle$$

$$\hat{S}^z |s, m\rangle = \hbar m |s, m\rangle$$

with $m = -s, -s+1, \cdots, s-1, s$.

The raising and lowering operators are defined by

$$\hat{S}^\pm |s, m\rangle = \hbar \sqrt{s(s+1) - m(m\pm 1)}\, |s, m\pm 1\rangle$$

with $\hat{S}^\pm = \hat{S}^x \pm i\hat{S}^y$.

Unlike orbital angular momentum, the states $|s, m\rangle$ have no representation in real space.

### The spin of the elementary particles

**Fermions:** half-integer value of $s$
electrons, quarks, protons, neutrons are fermions with spin $s = \tfrac{1}{2}$

**Bosons:** integer value of $s$
photons are bosons with $s = 1$,
the Higgs has $s = 0$

## 5.2 Theory of spin-$\tfrac{1}{2}$

$$s = \tfrac{1}{2} \rightarrow m = \pm\tfrac{1}{2}$$

They are two-level systems!

$$\hat{S}^2 |\tfrac{1}{2}, m\rangle = \hbar^2 \tfrac{1}{2}\left(\tfrac{1}{2}+1\right)|\tfrac{1}{2}, m\rangle = \hbar^2\tfrac{3}{4}|\tfrac{1}{2}, m\rangle$$

$$\hat{S}^z |\tfrac{1}{2}, m\rangle = \hbar m |\tfrac{1}{2}, m\rangle$$

From here on we can drop the index $s$ and label the states $|+\rangle, |-\rangle$; $|1\rangle, |2\rangle$ or $|\uparrow\rangle, |\downarrow\rangle$.

As noted earlier, an arbitrary state in this basis reads

$$|\psi\rangle = c_+ |+\rangle + c_2 |-\rangle$$

The eigenvectors of $\hat{S}^x$ are

$$|+_x\rangle = \tfrac{1}{\sqrt{2}}\big[|+\rangle + |-\rangle\big] \quad;\quad |-_x\rangle = \tfrac{1}{\sqrt{2}}\big[|+\rangle - |-\rangle\big]$$

$$\rightarrow |\psi\rangle = \frac{c_+ + c_-}{\sqrt{2}}|+_x\rangle + \frac{c_+ - c_-}{\sqrt{2}}|-_x\rangle$$

Hence the probability of finding the spin pointing one way or the other along $x$ is

$$P(s^x = \hbar/2) = \left|\frac{c_+ + c_-}{\sqrt{2}}\right|^2 \quad;\quad P(s^x = -\tfrac{\hbar}{2}) = \left|\frac{c_+ - c_-}{\sqrt{2}}\right|^2$$

## 5.3 — Addition of spins $s = \tfrac{1}{2}$

Take a system of two particles in definite states $|s_1, m_1\rangle$ and $|s_2, m_2\rangle$. We write the state of the system as

$$|s_1, s_2, m_1, m_2\rangle = |s_1, m_1\rangle \otimes |s_2, m_2\rangle$$

The state is "separable"

$$\hat{S}_1^2 |s_1 s_2, m_1 m_2\rangle = s_1(s_1+1)\hbar^2 |s_1 s_2, m_1, m_2\rangle$$

$$\hat{S}_2^2 |s_1 s_2, m_1 m_2\rangle = s_2(s_2+1)\hbar^2 |s_1 s_2, m_1 m_2\rangle$$

$$\hat{S}_1^z |s_1 s_2 m_1 m_2\rangle = \hbar m_1 |s_1 s_2 m_1 m_2\rangle$$

$$\hat{S}_2^z |s_1 s_2 m_1 m_2\rangle = \hbar m_2 |s_1 s_2 m_1 m_2\rangle$$

We now want the **total** spin of the system. One readily checks that

$$\hat{S}^z |s_1 s_2 m_1 m_2\rangle = \hat{S}_1^z + \hat{S}_2^z |s_1 s_2 m_1 m_2\rangle =$$

$$= \hbar (m_1 + m_2) |s_1 s_2 m_1 m_2\rangle$$

However, the states $|s_1 s_2 m_1 m_2\rangle$ are not eigenstates of $\hat{S}^2 = (\hat{S}_1 + \hat{S}_2)^2$!

Let us solve this for two $s = \tfrac{1}{2}$ particles. There are 4 possible combinations of $m_1 + m_2$

$$|++\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}\rangle \qquad (m = 1)$$

$$|+-\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}\rangle \qquad (m = 0)$$

$$|-+\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, \tfrac{1}{2}\rangle \qquad (m = 0)$$

$$|--\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, -\tfrac{1}{2}\rangle \qquad (m = -1)$$

How can there be two $m = 0$ states? To settle this we invoke the identity

$$\hat{S}^2 = (\hat{S}_1 + \hat{S}_2)^2 = \hat{S}_1^2 + \hat{S}_2^2 + 2\hat{S}_1 \cdot \hat{S}_2$$

$$= \hat{S}_1^2 + \hat{S}_2^2 + \hat{S}_1^+ \hat{S}_2^- + \hat{S}_1^- \hat{S}_2^+ + 2\hat{S}_1^z \hat{S}_2^z$$

This lets us readily build the matrix representation of the operator in this basis

$$\hat{S}^2 = \frac{\hbar^2}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 2 & 0 \\ 0 & 2 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} + \frac{3}{2}\hbar^2\, \mathbb{I}$$

We see at once that $|++\rangle$ and $|--\rangle$ are eigenvectors of $\hat{S}^2$ with eigenvalues $2\hbar^2$, so they carry quantum number $s = 1$, since $1(1+1) = 2$.

To find the values of $s$ in the $|+-\rangle$, $|-+\rangle$ ($m = 0$) subspace we must solve

$$\det\begin{pmatrix} -1-\lambda & 2 \\ 2 & -1-\lambda \end{pmatrix} = (-1-\lambda)^2 - 4 = 0 \rightarrow \lambda = 1, -3$$

or $s = \dfrac{\hbar^2}{2}\lambda + \dfrac{3}{2}\hbar^2 = 0, 2\hbar^2$

So one eigenvector belongs to $s = 0$ and the other to $s = 1$. Solving for the eigenvectors gives:

$$|1, 0\rangle = \tfrac{1}{\sqrt{2}}\big[|+-\rangle + |-+\rangle\big] \qquad (s = 1, m = 0)$$

$$|0, 0\rangle = \tfrac{1}{\sqrt{2}}\big[|+-\rangle - |-+\rangle\big] \qquad (s = 0, m = 0)$$

We therefore end up with three states having $s = 1$, $m = -1, 0, 1$; and one with $s = 0$, $m = 0$.

## 5.4 Pairs of indistinguishable particles

Let us ask which states are permitted for two particles. In general a two-particle state is specified by

$$|ab\rangle = |a\rangle_1 \otimes |b\rangle_2$$

where $|a\rangle_1$ is the state of particle 1 and $|b\rangle_2$ that of particle 2. We introduce the "exchange operator", or permutation operator, which acts as

$$\hat{P}_{12}|ab\rangle = |ba\rangle$$

or

$$\hat{P}_{12}\left(|a\rangle_1 \otimes |b\rangle_2\right) = |b\rangle_1 \otimes |a\rangle_2$$

Because the particles are indistinguishable, we have no way of telling whether the exchange operator has acted: the "exchanged" state must equal the original one up to a phase

$$\hat{P}_{12}|\psi\rangle = e^{i\delta}|\psi\rangle = \lambda |\psi\rangle$$

Applying $\hat{P}_{12}$ twice returns the identity. Hence

$$\hat{P}_{12}^2 |\psi\rangle = \lambda^2 |\psi\rangle = |\psi\rangle \rightarrow \lambda = \pm 1$$

Plainly, if both particles are in state $a$

$$\hat{P}_{12}|aa\rangle = |aa\rangle$$

$\rightarrow |aa\rangle$ is a "symmetric" state under exchange.

If $b \neq a$ we must find the eigenstates of $\hat{P}_{12}$

$$\hat{P}_{12} = \begin{pmatrix} \langle ab|\hat{P}_{12}|ab\rangle & \langle ab|\hat{P}_{12}|ba\rangle \\ \langle ba|\hat{P}_{12}|ab\rangle & \langle ba|\hat{P}_{12}|ba\rangle \end{pmatrix}$$

$$= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

The eigenvalues are, naturally, $\lambda = \pm 1$. The eigenstates are:

$$|+\rangle = \tfrac{1}{\sqrt{2}}\big(|ab\rangle + |ba\rangle\big) \qquad \lambda = 1$$

$$|-\rangle = \tfrac{1}{\sqrt{2}}\big(|ab\rangle - |ba\rangle\big) \qquad \lambda = -1$$

Notice that two particles **must** sit in either the $|+\rangle$ or the $|-\rangle$ state and cannot occupy a linear superposition of the two. They are forced to

"make a choice" between them. Fortunately, Nature settles it for them:

**Bosons:** appear only in symmetric states

**Fermions:** appear only in antisymmetric states

### Pauli's exclusion principle:

We noted that two particles in the same state are necessarily symmetric under exchange. Since a fermionic state is antisymmetric, two fermions can never occupy the same state.

**Example:** two spin $s = \tfrac{1}{2}$ particles.

We found that two spins $s = \tfrac{1}{2}$ can occupy the states

$$|1, 0\rangle = \tfrac{1}{\sqrt{2}}\big(|+-\rangle + |-+\rangle\big)$$

$$|0, 0\rangle = \tfrac{1}{\sqrt{2}}\big(|+-\rangle - |-+\rangle\big)$$

We recognize these as symmetric and anti-symmetric under exchange.

*end of lecture.*

This is simple to explain once we notice the following identity:

$$\hat{S}^2 = \hbar^2 \hat{S}_1^z \hat{S}_2^z + \tfrac{3}{2}\hbar^2\, \mathbb{I} + \hbar^2 \hat{P}_{12}$$

$$\rightarrow [\hat{P}_{12}, \hat{S}^2] = 0$$

$\rightarrow$ eigenstates of $\hat{S}^2$ must also be eigenstates of $\hat{P}_{12}$.

## 5.5 Many-particle systems

For a system of $N$ identical particles, the Hamiltonian must stay invariant under any permutation of two particles or coordinates. For identical particles the exchange sign must be the same for every pair, or else the particles would be distinguishable. The $N$-particle wave function is therefore odd under the exchange of any pair of fermions, and even for bosons

$$\psi(x_1, \ldots x_n, \ldots x_m, \ldots x_N) = \pm\, \psi(x_1, \ldots x_m, \ldots x_n, \ldots x_N)$$

Consider a system of $N$ non-interacting particles with Hamiltonian

$$\hat{H} = \hat{H}_1 + \hat{H}_2 + \cdots \hat{H}_N$$

with, for instance $\hat{H}_i = \frac{\hat{p}_i^2}{2m} + V(\vec{x}_i)$

The general $N$-particle wave function for the energy

$$E_i = E_{i_1} + E_{i_2} + \cdots E_{i_N}$$

can be written as

$$|\psi(x_1, \ldots x_N)\rangle = \sum_{\{\sigma\} \in S} C_{\sigma_1, \sigma_2, \ldots \sigma_N} |\psi_{\sigma_1}(x_1)\rangle \cdots |\psi_{\sigma_N}(x_N)\rangle$$

where $\{\sigma\}$ runs over all permutations of the indices $\{i_1, i_2, \ldots i_N\}$. The coefficients $C_{\sigma_1 \ldots \sigma_N}$ are invariant under permutations for bosons, and change sign under an odd number of permutations for fermions. They must also be normalized

$$\sum_{\{\sigma\} \in S} |C_{\sigma_1 \ldots \sigma_N}|^2 = 1$$

**Fermions:** By anti-symmetry, all indices must differ. One checks that the wave function, up to an overall phase, is proportional to the so-called "Slater determinant":

$$\psi(x_1, x_2, \ldots x_N) = \frac{1}{\sqrt{N!}}\begin{vmatrix} \psi_{i_1}(x_1) & \psi_{i_2}(x_1) & \cdots & \psi_{i_N}(x_1) \\ \psi_{i_1}(x_2) & \psi_{i_2}(x_2) & & \psi_{i_N}(x_2) \\ \vdots & \vdots & & \vdots \\ \psi_{i_1}(x_N) & \psi_{i_2}(x_N) & \cdots & \psi_{i_N}(x_N) \end{vmatrix}$$

The antisymmetry follows from the $(-1)$ picked up when two columns are exchanged. Written out:

### Example: three-particle system

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{6}}\begin{vmatrix} \psi_a(x_1) & \psi_b(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_b(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_b(x_3) & \psi_c(x_3) \end{vmatrix}$$

$$= \frac{1}{\sqrt{6}}\Big(\psi_a(x_1)\psi_b(x_2)\psi_c(x_3) - \psi_a(x_1)\psi_c(x_2)\psi_b(x_3)$$

$$- \psi_b(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_b(x_1)\psi_c(x_2)\psi_a(x_3)$$

$$+ \psi_c(x_1)\psi_a(x_2)\psi_b(x_3) - \psi_c(x_1)\psi_b(x_2)\psi_a(x_3)\Big)$$

**Bosons:** Here the determinant is replaced by the permanent, defined just like the determinant but with every sign positive.

### Example: three-particle system.

Different orbitals $a \neq b \neq c$

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{6}}\,\text{perm}\begin{pmatrix} \psi_a(x_1) & \psi_b(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_b(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_b(x_3) & \psi_c(x_3) \end{pmatrix}$$

$$= \frac{1}{\sqrt{6}}\Big(\psi_a(x_1)\psi_b(x_2)\psi_c(x_3) + \psi_a(x_1)\psi_c(x_2)\psi_b(x_3)$$

$$+ \psi_b(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_b(x_1)\psi_c(x_2)\psi_a(x_3)$$

$$+ \psi_c(x_1)\psi_a(x_2)\psi_b(x_3) + \psi_c(x_1)\psi_b(x_2)\psi_a(x_3)\Big)$$

Two identical orbitals $a = b \neq c$

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{3}}\frac{1}{2!}\,\text{perm}\begin{pmatrix} \psi_a(x_1) & \psi_a(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_a(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_a(x_3) & \psi_c(x_3) \end{pmatrix}$$

$$= \frac{1}{\sqrt{3}}\Big(\psi_a(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_a(x_1)\psi_a(x_3)\psi_c(x_2)$$

$$+ \psi_a(x_1)\psi_a(x_3)\psi_c(x_2)\Big)$$

One can show that the normalization carries an extra $\sqrt{n_a!}$, where $n_a$ is the number of times the orbital $\psi_a$ is occupied.

### Example: Two particles with spin

Consider two particles that may occupy two orbitals $\psi_1(r), \psi_2(r)$ and carry spin $\uparrow\downarrow$. We can build the following Slater determinants:

$$\psi_{1\uparrow 2\uparrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\uparrow}(\vec{r}_1) & \psi_{2\uparrow}(\vec{r}_1) \\ \psi_{1\uparrow}(\vec{r}_2) & \psi_{2\uparrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\uparrow}(\vec{r}_1)\psi_{2\uparrow}(\vec{r}_2) - \psi_{1\uparrow}(\vec{r}_2)\psi_{2\uparrow}(\vec{r}_1)\right)$$

$$\psi_{1\downarrow 2\downarrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\downarrow}(\vec{r}_1) & \psi_{2\downarrow}(\vec{r}_1) \\ \psi_{1\downarrow}(\vec{r}_2) & \psi_{2\downarrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\downarrow}(\vec{r}_1)\psi_{2\downarrow}(\vec{r}_2) - \psi_{1\downarrow}(\vec{r}_2)\psi_{2\downarrow}(\vec{r}_1)\right)$$

$$\psi_{1\uparrow 2\downarrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\uparrow}(\vec{r}_1) & \psi_{2\downarrow}(\vec{r}_1) \\ \psi_{1\uparrow}(\vec{r}_2) & \psi_{2\downarrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\uparrow}(\vec{r}_1)\psi_{2\downarrow}(\vec{r}_2) - \psi_{1\uparrow}(\vec{r}_2)\psi_{2\downarrow}(\vec{r}_1)\right)$$

Same for $\psi_{1\downarrow 2\uparrow}$

Notice that $\psi_{1\uparrow 1\downarrow}$ and $\psi_{2\uparrow 2\downarrow}$ are allowed, but $\psi_{1\uparrow 1\uparrow}$ or $\psi_{2\uparrow 2\uparrow}$ are not.

Moreover, as we shall see next, these states are neither singlets nor triplets.

### Two particles with spin: space and spin wave functions

The total wave function for two particles with spin is a simultaneous eigenfunction of $\hat{H}$, $\hat{S}^2$ and $\hat{S}^z$, and takes the form

$$\Psi_{\sigma_1 \sigma_2}(\vec{r}_1, \vec{r}_2) = \psi(\vec{r}_1, \vec{r}_2)\,\chi(\sigma_1, \sigma_2)$$

where $\sigma_1, \sigma_2$ now stand in for $m$ to denote $\uparrow, \downarrow$ or $\uparrow, \downarrow$.

$\Psi$ must be anti-symmetric. Consequently a pair of electrons in a $|0,0\rangle$ (singlet) state must carry a symmetric spatial wave function $\psi(\vec{r}_2, \vec{r}_1) = \psi(\vec{r}_1, \vec{r}_2)$, while in the triplet states the spatial wave function must be anti-symmetric.

### Example: Hydrogen ($H_2$) gas

Here the spin of the protons proves crucial. With parallel spins the molecule is "orthohydrogen"; in the singlet state it is "parahydrogen". Both are very stable, and transitions between them may take weeks.

The actual interaction energy between the protons is entirely negligible. The rotational energy of the molecule, however, matters a great deal. A state with angular momentum $\ell$ has parity $(-1)^\ell$. Parahydrogen, with its antisymmetric spin wave function, therefore needs a symmetric proton space wave function and admits only even values of $\ell$. By the same reasoning, orthohydrogen admits only odd $\ell$. The rotational energy of a state with angular momentum $\ell$ is

$$E_\ell^{\text{rot}} = \frac{\hbar^2 \ell(\ell+1)}{I}$$

so the two species of hydrogen gas carry different rotational energies.

## 5.6 Particles with interactions and exchange

Now the general eigenstate is written as a linear combination of Slater determinants (fermions) or permanents (bosons).

Take two fermions and two orbitals, 1 and 2. The combinations with the correct antisymmetry are

$$\Psi_S(x_1, s_1, x_2, s_2) = \frac{1}{\sqrt{2}}\left(\psi_1(x_1)\psi_2(x_2) + \psi_1(x_2)\psi_2(x_1)\right)\chi_0(s_1, s_2)$$

$$\Psi_t(x_1, s_1, x_2, s_2) = \frac{1}{\sqrt{2}}\left(\psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1)\right)\chi_1(s_1, s_2)$$

where $s, t$ refer to the singlet and triplet states

$$\chi_0(s_1, s_2) = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right)$$

$$\chi_1(s_1, s_2) = \left\{|\uparrow\uparrow\rangle\,;\;\frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\right)\,;\;|\downarrow\downarrow\rangle\right\}$$

Now switch on a small interaction $V(x_1, x_2)$ and treat it perturbatively

$$\delta E = \int dx_1 \int dx_2 \sum_{s_1, s_2} |\psi(x_1, s_1, x_2, s_2)|^2\, V(x_1 x_2)$$

For the singlet and triplet states we obtain

$$\delta E_S = \int dx_1 \int dx_2\, |\psi_1(x_1)|^2 |\psi_2(x_2)|^2\, V(x_1, x_2)$$

$$+ \int dx_1 \int dx_2\, \psi_1^*(x_1)\psi_2^*(x_2)\, V(x_1, x_2)\,\psi_1(x_2)\psi_2(x_1)$$

$$\delta E_t = \int dx_1 \int dx_2\, |\psi_1(x_1)|^2 |\psi_2(x_2)|^2\, V(x_1, x_2)$$

$$- \int dx_1 \int dx_2\, \psi_1^*(x_1)\psi_2^*(x_2)\, V(x_1, x_2)\,\psi_1(x_1)\psi_2(x_2)$$

The first terms in both expressions are equal and go by the name "Hartree" term. It is readily recognized as a density-density interaction between the single-particle densities $|\psi_1(x_1)|^2$ and $|\psi_2(x_2)|^2$, blind to the spin state. The second term, the "Fock" or "exchange" term, has no classical interpretation. When the wave functions are real and positive and the interaction is repulsive, $V(x_1 x_2) > 0$, the triplet lies below the singlet in energy. In general, though, this need not hold.

*end of lecture*

### Example: Hund's rule

We saw that even though spin never enters the Hamiltonian explicitly, the energy of the eigenstates still depends on the spin orientation. The source is the electrostatic repulsion between electrons. In the spatially antisymmetric wave function the electrons have zero probability of coinciding and are, on average, farther apart than in the spatially symmetric state. Electrostatic repulsion therefore pushes the spatially symmetric state above its counterpart. The lowest-energy state thus has its spins aligned (in practice, a high-spin state). This gives Hund's rule for the magnetization of partially filled atomic shells in transition metals and rare earths: for shells half filled or less, all spins point the same way. It is a first step toward understanding ferromagnetism.

## 5.7 The Helium atom

This is a case where every consideration above comes into play.

$$\hat{H} = \hat{H}_1 + \hat{H}_2 + V(\vec{r}_1, \vec{r}_2)$$

$$= \frac{\hat{p}_1^2}{2m} + \frac{\hat{p}_2^2}{2m} - \frac{Ze^2}{|\vec{r}_1|} - \frac{Ze^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

with $Z = 2$. We drop the kinetic energy of the nucleus and hold the atomic positions fixed; the proton interaction is then constant. Although $V$ can be sizable, we treat it as a perturbation to begin with. The eigenstates of the unperturbed Hamiltonian are taken to be hydrogenic wave functions

$$|n_1, \ell_1, m_1\rangle_1 \otimes |n_2, \ell_2, m_2\rangle_2$$

### The ground state

We begin with $|100\rangle_1 \otimes |100\rangle_2$

We still need the spin state of the electrons. The only possibility is

$$\frac{1}{\sqrt{2}}\left[|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2\right]$$

which is antisymmetric under spin exchange.

The ground state is then

$$|1s,1s\rangle = |100\rangle_1 |100\rangle_2 \, \frac{1}{\sqrt{2}} \left[ |+-\rangle - |-+\rangle \right]$$

The energy of the unperturbed state reads

$$E^{(0)}_{1s1s} = E^{(0)}_{1s} + E^{(0)}_{1s} = 2\left(-\frac{1}{2} m_e c^2 Z^2 \alpha^2\right) = -108.8 \text{ eV}$$

The first-order correction is

$$E^{(1)}_{1s1s} = \langle 1s\,1s | \frac{e^2}{|\vec{r}_1 - \vec{r}_2|} | 1s\,1s \rangle$$

Following the previous section, we get

$$E^{(1)}_{1s1s} = \int d\vec{r}_1 \int d\vec{r}_2 \; |\psi_{1s}(\vec{r}_1)|^2 \, |\psi_{1s}(\vec{r}_2)|^2 \, \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

which has the form

$$\int d^3 r_1 \int d^3 r_2 \; \frac{\rho(\vec{r}_1)\,\rho(\vec{r}_2)}{|\vec{r}_1 - \vec{r}_2|}$$

with $\rho(\vec{r}) = e\,|\psi_{1s}(\vec{r})|^2$.

This integral can be done exactly to give (see Townsend 12.31)

$$E^{(1)}_{1s,1s} = \frac{5}{8} Z \, m_e c^2 \alpha^2 = 34 \text{ eV}$$

Adding the two contributions, we obtain to first order

$$E_{1s,1s} \approx E^{(0)}_{1s,1s} + E^{(1)}_{1s,1s} = -74.8 \text{ eV}$$

The experimental value is $E_{\exp} = -78.8 \text{ eV}$.

### Excited states:

Consider now a state $|100\rangle \otimes |2\ell m\rangle$.

We can form 16 antisymmetric states

$$\frac{1}{\sqrt{2}} \left( |100\rangle_1 |2\ell m\rangle_2 - |2\ell m\rangle_1 |100\rangle_2 \right) \chi_1(s_1 s_2)$$

$$\frac{1}{\sqrt{2}} \left( |100\rangle_1 |2\ell m\rangle_2 + |2\ell m\rangle_1 |100\rangle_2 \right) \chi_0(s_1 s_2)$$

The unperturbed energy is

$$E_{1s,\,2s\,\text{or}\,2p} = E_{1s} + E_{2s\,\text{or}\,2p} =$$

$$= -\frac{1}{2} m_e c^2 Z^2 \alpha^2 \left(1 + \frac{1}{2^2}\right) = -68.0 \text{ eV}$$

Since this is a degenerate manifold, we must use degenerate perturbation theory.

Recall first that $[\hat{H}, \hat{S}^2] = [\hat{H}, \hat{S}^z] = 0$. The Hamiltonian therefore does not mix states with different $S^2$ or $S^z$. These four states are thus already eigenstates of the perturbation, whose matrix is diagonal

$$E^{(1)} = \frac{1}{2} \left( \langle 100| \langle 2\ell m| \pm \langle 2\ell m| \langle 100| \right) \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

$$\left( |100\rangle_1 |2\ell m\rangle_2 \pm |2\ell m\rangle_1 |100\rangle_2 \right)$$

$$= J \pm k$$

Here $J$ is the Hartree term, always positive, while $k$ is the Fock term, or exchange energy. By the earlier argument, the triplet of $S=1$ states is shifted by $J-k$, and the $S=0$ state by $J+k$.

*end of lecture*

Evaluating these integrals gives

$$E^{(1)}_{1s,2s} = J_{1s,2s} \pm k_{1s,2s} = 11.4 \text{ eV} \pm 1.2 \text{ eV}$$

$$E^{(1)}_{1s,2p} = J_{1s,2p} \pm k_{1s,2p} = 13.2 \text{ eV} \pm 0.9 \text{ eV}$$

$$\rightarrow E_{1s,2s} \approx -56.6 \text{ eV} \pm 1.2 \text{ eV}$$

$$E_{1s,2p} \approx -54.8 \text{ eV} \pm 0.9 \text{ eV}$$

*[Energy level diagram: from $E_0$ ($E_{1s2s}$), splitting into:*
- *$E_0 + J_{1s2s}$, further split by $2k_{1s2s}$ into singlet $E_0 + J + k$ (top) and triplet $E_0 + J - k$ (bottom)*
- *upper branch shows $2k_{1s2p}$ splitting]*

*[Lower diagram: spectroscopic levels with arrows — $^1P$, $^3P$, $^1S$, $^3S$]*


---

## References and Further Reading

*Editorial addition mapping the notes to their source text. The helium electron–electron repulsion integral is cited in the text as Townsend §12.31.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 5 (A System of Two Spin-½ Particles — addition of spins, the singlet and triplet states) and Ch. 12 (Identical Particles — exchange symmetry, the helium atom, §12.31).

**Further reading.** Sakurai & Napolitano, the "Identical Particles" chapter; Griffiths & Schroeter, the "Identical Particles" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XIV.
# Chapter 6 — The Variational Method

*Bounding the ground state by guessing its shape — and watching the chemical bond fall out of the arithmetic.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Perturbation theory needs a small knob to turn. When there is no such knob — when the interaction is the whole problem, as it is for the electrons in helium or the binding of two protons — we need a different move. The variational method is that move, and it rests on one honest fact: for *any* normalized trial state you write down, the expectation value $\langle H \rangle$ can never sit below the true ground-state energy. It can only equal it or overshoot. So the recipe is almost cheeky in its simplicity. Guess the shape of the answer, leave a few parameters free, compute $\langle H \rangle$, and slide those parameters until the energy is as low as you can drive it. The lowest you reach is your best upper bound; the shape that reaches it is your best wave function.

The art is entirely in the guess. A Gaussian nails the harmonic oscillator exactly because the oscillator's ground state *is* a Gaussian. A hydrogenic orbital with an adjustable effective charge captures how each helium electron partly screens the nucleus from the other. And a sum of two atomic orbitals, $|A\rangle \pm |B\rangle$, gives you bonding and antibonding molecular orbitals — the chemical bond emerging from a two-term variational ansatz. We close by promoting the parameters to coefficients in a basis, which turns minimization into a generalized eigenvalue problem with an overlap matrix.

## 6 — The variational method

Notice that the correction to the energy of the He atom due to the interactions is

$$\delta E = \langle 1s1s | V | 1s1s \rangle$$

and the resulting estimate of the ground state energy is just the expectation value

$$E_{1s1s} = \langle 1s1s | H_0 | 1s1s \rangle + \langle 1s1s | V | 1s1s \rangle =$$

$$= \langle 1s1s | H | 1s1s \rangle$$

This is a first example of a "variational" calculation. The strategy is to write down a candidate ground-state wave-function controlled by a collection of tunable parameters $\{\alpha_1, \alpha_2, \dots \alpha_n\} = \{\vec{\alpha}\}$. The variational energy is then estimated as

$$E_V = \langle \psi(\{\vec{\alpha}\}) | H | \psi(\{\vec{\alpha}\}) \rangle$$

One can show that this quantity never falls below the true ground-state energy

$$E_V \geq E_0$$

The argument is short. Expand $|\psi(\{\vec{\alpha}\})\rangle$ in the eigenbasis of $\hat{H}$

$$|\psi\rangle = \sum_n \psi_n |n\rangle$$

The variational energy becomes

$$E_V = \langle \psi | \hat{H} | \psi \rangle = \sum_n |\psi_n|^2 \langle n | \hat{H} | n \rangle = \sum_n |\psi_n|^2 E_n$$

$$\rightarrow E_V \geq E_0$$

The whole game is to find a trial function flexible enough to capture the physics, so that tuning $\{\vec{\alpha}\}$ brings us as near the ground state as possible. We achieve this by minimizing $E_V$ over the $\alpha$'s. In practice, then, we look for solutions of the system

$$\frac{\partial E_V}{\partial \alpha_i} = \langle \frac{\partial \psi}{\partial \alpha_i} | H | \psi \rangle + \langle \psi | H | \frac{\partial \psi}{\partial \alpha_i} \rangle = 0$$

### Example: Ground-state of the 1d harmonic oscillator

$$\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + \frac{1}{2} m \omega^2 x^2$$

For a "trial" function we take a Gaussian

$$\psi(x) = A e^{-bx^2}$$

The normalization constant $A$ follows from

$$1 = \int_{-\infty}^{\infty} |\psi(x)|^2 \, dx = |A|^2 \int_{-\infty}^{\infty} e^{-2bx^2} \, dx = |A|^2 \sqrt{\frac{\pi}{2b}}$$

$$\rightarrow A = \left(\frac{2b}{\pi}\right)^{1/4}$$

Now, $\langle H \rangle = \langle T \rangle + \langle V \rangle$

$$\langle T \rangle = -\frac{\hbar^2}{2m} |A|^2 \int_{-\infty}^{\infty} e^{-bx^2} \frac{d^2}{dx^2}\left(e^{-bx^2}\right) = \frac{\hbar^2 b}{2m}$$

$$\langle V \rangle = \frac{1}{2} m \omega^2 |A|^2 \int_{-\infty}^{\infty} e^{-bx^2} x^2 \, dx = \frac{m\omega^2}{8b}$$

$$\langle H \rangle = \frac{\hbar^2 b}{2m} + \frac{m\omega^2}{8b}$$

We minimize $\langle H \rangle$:

$$\frac{d}{db}\langle H \rangle = \frac{\hbar^2}{2m} - \frac{m\omega^2}{8b^2} = 0 \rightarrow b = \frac{m\omega}{2\hbar}$$

$$\rightarrow E_V = \frac{1}{2} \hbar \omega$$

The result is exact here for a simple reason: the actual ground state happens to be a Gaussian. Gaussians are favorites precisely because they are so convenient to integrate.

### Example: Delta function potential

$$H = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} - \alpha \delta(x)$$

We keep the same trial function. The kinetic energy was already computed in the previous example

$$\langle V \rangle = -\alpha |A|^2 \int_{-\infty}^{\infty} e^{-2bx^2} \delta(x) \, dx = -\alpha \sqrt{\frac{2b}{\pi}}$$

$$\rightarrow \langle H \rangle = \frac{\hbar^2 b}{2m} - \alpha \sqrt{\frac{2b}{\pi}}$$

$$\frac{d\langle H\rangle}{db} = \frac{\hbar^2}{2m} - \frac{\alpha}{\sqrt{2\pi b}} = 0 \rightarrow b = \frac{2m^2 \alpha^2}{\pi \hbar^4} \rightarrow E_V = -\frac{m\alpha^2}{\pi \hbar^2}$$

$$E_V > E_{gs} = -m\alpha^2 / 2\hbar^2$$

### Example: Ground state of Helium

We choose $|\psi\rangle = |100(\tilde{z})\rangle \, |100(\tilde{z})\rangle$, with

$$\psi(\vec{r}) = \langle \vec{r} | 100(\tilde{z}) \rangle = \frac{1}{\sqrt{\pi}} \left(\frac{\tilde{z}}{a_0}\right)^{3/2} e^{-\tilde{z} r / a_0}$$

Evaluating $\langle H \rangle$ is simpler once we regroup the Hamiltonian

$$\hat{H} = \frac{\hat{p}_1^2}{2m} + \frac{\hat{p}_2^2}{2m} - \frac{Ze^2}{|\vec{r}_1|} - \frac{Ze^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|} =$$

$$= \left[ \frac{\hat{p}_1^2}{2m} - \frac{\tilde{z}e^2}{|\vec{r}_1|} + \frac{\hat{p}_2^2}{2m} - \frac{\tilde{z}e^2}{|\vec{r}_2|} \right] + \frac{(\tilde{z}-Z)e^2}{|\vec{r}_1|} + \frac{(\tilde{z}-Z)e^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

The expectation value is now straightforward to obtain

$$\langle H \rangle = \frac{1}{2} m_e c^2 \alpha^2 \left( -2\tilde{z}^2 + 4\tilde{z}(\tilde{z}-Z) + \frac{5}{4}\tilde{z} \right)$$

$$= \frac{1}{2} m_e c^2 \alpha^2 \left( 2\tilde{z}^2 - 4Z\tilde{z} + \frac{5}{4}\tilde{z} \right)$$

Minimizing

$$\frac{\partial \langle H \rangle}{\partial \tilde{z}} = 0 \rightarrow \tilde{z} = Z - \frac{5}{16}$$

$$\rightarrow E_V = -\frac{1}{2} m_e c^2 \alpha^2 \left[ 2\left(Z - \frac{5}{16}\right)^2 \right] = -77.4 \text{ eV}$$

which sits much nearer the measured value of $-78.8$ eV. We set $Z=2$ in this expression. The point is that the wave function builds in the fact that each electron sees an effective nuclear charge partly shielded by the other electron.

### Excited states

Note that if we pick a trial wave function orthogonal to the ground state

$$\langle \psi | \psi_{gs} \rangle = 0$$

then $E_V \geq E_1$, so we can estimate the first excited state as well. One way to enforce this is to place the trial state in a different symmetry sector (for instance, using different values of $n$ in the helium case).

## 6.2 The Hydrogen molecule ion

The $H_2^+$ molecule has the shape of a dumbbell. We work in the rotating frame and pin the nuclei at fixed positions separated by a distance $R$. We also neglect nuclear vibrations, since the nuclei move far more sluggishly than the electrons. This is the well-known "Born-Oppenheimer" approximation. Treating $R$ as a variational parameter lets us extract both the molecule's size and its energy.

This is a one-electron problem. When the atoms are far apart, $R \to \infty$, the electron sits on either atom 1 or atom 2. Bringing them together lets the wave function spread out. A natural trial function is a linear combination of hydrogenic 1s states, one centered on each nucleus

$$\langle r | A \rangle = \frac{1}{\sqrt{\pi a_0^3}} e^{-|\vec{r} - \vec{R}/2| / a_0}$$

$$\langle r | B \rangle = \frac{1}{\sqrt{\pi a_0^3}} e^{-|\vec{r} + \vec{R}/2| / a_0}$$

$$\hat{H} = \frac{\hat{p}^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} - \frac{e^2}{|\vec{r} + \vec{R}/2|} + \frac{e^2}{R} \quad \text{(proton-proton)}$$

$$H_{AA} = \langle A | H | A \rangle = \langle A | \frac{\hat{p}^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} | A \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | A \rangle + \frac{e^2}{R}$$

$$= E_1 - \int d^3 r \, \frac{e^2}{|\vec{r} + \vec{R}/2|} |\langle r | A \rangle|^2 + \frac{e^2}{R}$$

Symmetry alone tells us, with no further computation, that $H_{BB} = H_{AA}$

$$H_{AB} = \langle A | H | B \rangle = \langle A | \frac{p^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} | B \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | B \rangle + \frac{e^2}{R} \langle A | B \rangle$$

$$= E_1 \langle A | B \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | B \rangle + \frac{e^2}{R} \langle A | B \rangle$$

where $\langle A | B \rangle = S_{AB}$ is known as the "overlap integral".

The molecule's reflection symmetry about the origin suggests a variational solution, much as the permutation operator did earlier. The ground state ought to be unchanged under a reflection, equivalently under exchanging the indices 1,2.

$$R | \psi \rangle = e^{i\delta} | \psi \rangle$$

But $R^2 \equiv \mathbb{1} \rightarrow e^{i\delta} = \pm 1$

So there are two candidate solutions:

$$|\pm\rangle = \frac{1}{\sqrt{2 \pm 2 S_{AB}}} \left[ |A\rangle \pm |B\rangle \right]$$

where the extra piece in the normalization comes from $|1\rangle$ and $|2\rangle$ not being orthogonal.

The expectation values work out to

$$E_\pm = \frac{1}{1 \pm S_{AB}} \left( H_{AA} \pm H_{AB} \right)$$

*[Plot: two wave functions over the interval; $|+\rangle$ (peaked/cusped at both $-R/2$ and $R/2$, even) above, $|-\rangle$ (odd, antisymmetric about origin) below, with markers at $-R/2$ and $R/2$.]*

Only the even-parity function $|+\rangle$ has a minimum, occurring at a separation of 1.3 Å. For this reason $|+\rangle$ is called the "bonding" orbital and $|-\rangle$ the "anti-bonding" one. Such "molecular orbitals" are linear combinations of atomic orbitals — the so-called "LCAO" technique.

*[Plot: $E$(eV) vs $R$(Å). Curve $E_-$ approaches $2E_1$ from above (no minimum, antibonding). Curve $E_+$ has a minimum below (bonding). Both approach the asymptote $2E_1$ at large $R$.]*

## 6.3 The Hydrogen molecule

As before, we write the Hamiltonian

$$\hat{H} = \frac{\hat{p}_1^2}{2m_e} - \frac{e^2}{|\vec{r}_1 - \vec{R}/2|} - \frac{e^2}{|\vec{r}_1 + \vec{R}/2|} + \frac{\hat{p}_2^2}{2m_e} - \frac{e^2}{|\vec{r}_2 - \vec{R}/2|} - \frac{e^2}{|\vec{r}_2 + \vec{R}/2|}$$

$$+ \frac{e^2}{R} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

where the final term $V(|\vec{r}_1 - \vec{r}_2|) = \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$ captures the electron-electron interaction

### Molecular orbitals

A first attempt reuses the MO's obtained for $H_2^+$

$$|\pm\rangle = \frac{1}{\sqrt{2(1 \pm S)}} \left( |A\rangle \pm |B\rangle \right)$$

We begin by building Slater determinants from these MO's, now including spin. Take the singlet state, for example. Since $|+\rangle$ came out lower in energy for $H_2^+$, we use

$$|\psi\rangle = \frac{1}{\sqrt{2}} |+\rangle_1 |+\rangle_2 \left( |\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle \right)$$

The variational energy is then

$$\langle \psi | \hat{H} | \psi \rangle = \langle \psi | \hat{H}_1 | \psi \rangle + \langle \psi | \hat{H}_2 | \psi \rangle + \langle \psi | \hat{V} | \psi \rangle + \frac{e^2}{R}$$

$$= \mathcal{E}_0 + \mathcal{E}_0 + J_{AO} + \frac{e^2}{R}$$

### Valence bond picture

Now expand $|\psi\rangle$ over the AO's

$$|\psi\rangle = \frac{1}{2(1+S)} \left( |A\rangle_1 + |B\rangle_1 \right) \left( |A\rangle_2 + |B\rangle_2 \right) |\chi_S\rangle$$

$$= \frac{1}{2(1+S)} \left( |A\rangle_1 |A\rangle_2 + |A\rangle_1 |B\rangle_2 + |A\rangle_2 |B\rangle_1 + |B\rangle_1 |B\rangle_2 \right) |\chi_S\rangle$$

The 2nd and 3rd terms are the "covalent" configurations, the ones that produce the chemical bond. The first and last are the "ionic" configurations, with both electrons in the same orbital. These ionic pieces carry higher energy because of the strong Coulomb repulsion of two electrons sharing one AO. Ideally we would like to adjust the relative weights of these contributions!

The valence bond picture simply drops the ionic configurations.

$$|\psi\rangle = \frac{1}{\sqrt{2(1+S^2)}} \left( |A\rangle_1 |B\rangle_2 + |A\rangle_2 |B\rangle_1 \right) |\chi_S\rangle$$

(Verify the normalization as exercise)

The energy of this state is then

$$\langle \psi | \hat{H} | \psi \rangle = 2 \langle \psi | \hat{H}_1 | \psi \rangle + \langle \psi | \hat{V} | \psi \rangle + \frac{e^2}{R}$$

$$= 2 \frac{\left( \mathcal{E}_0 + S \langle A | \hat{H}_1 | B \rangle \right)}{(1 + S^2)} + \frac{J + k}{(1 + S^2)} + \frac{e^2}{R}$$

*[Plot: $E$ vs $R$. Dashed curve labeled MO (higher minimum), dotted/solid curves labeled VB and exact (lower minima). Arrow indicates "Extra pot. energy from ionic configs." between the MO and VB/exact curves.]*

## 6.4 Generalized eigenvalue problem

Often the trial wave function is built as a linear combination of basis states, as we just did for $H_2^+$. In that case

$$|\psi\rangle = \sum_n \psi_n |n\rangle$$

Here we may regard the coefficients $\psi_n$ as the variational parameters, with the basis covering only part of the Hilbert space.

$$\langle H \rangle = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle} = \frac{\sum_{nm} \psi_n^* \psi_m \langle n | H | m \rangle}{\sum_{nm} \psi_n^* \psi_m S_{nm}} = \frac{\sum_{nm} \psi_n^* \psi_m H_{nm}}{\sum_{nm} \psi_n^* \psi_m S_{nm}}$$

where $S_{nm} = \langle n | m \rangle$. The best solution comes from solving the equations

$$\frac{\partial \langle H \rangle}{\partial \psi_n^*} = \frac{\sum_m \psi_m \left[ H_{nm} \left( \sum_{n'm'} \psi_{n'}^* \psi_{m'} S_{n'm'} \right) - S_{nm} \left( \sum_{n'm'} \psi_{n'}^* \psi_{m'} H_{n'm'} \right) \right]}{\left( \sum_{nm} \psi_n^* \psi_m S_{nm} \right)^2}$$

Collecting terms gives

$$\frac{\sum_m \psi_m H_{nm} - E \sum_m \psi_m S_{nm}}{\sum_{nm} \psi_n^* \psi_m S_{nm}} = 0$$

which requires the numerator to vanish

$$\sum_m^N \left( H_{nm} - E S_{nm} \right) \psi_m = 0 \qquad n = 1, \dots, N$$

This is a generalized eigenvalue problem:

$$\bar{\bar{H}} \vec{\psi} = E \bar{\bar{S}} \vec{\psi}$$

with $\bar{\bar{H}}$ the Hamiltonian matrix and $\bar{\bar{S}}$ the "overlap matrix". What sets it apart from an ordinary eigenvalue problem is the appearance of $\bar{\bar{S}}$. We solve it by locating the roots of the secular determinant

$$\begin{vmatrix} H_{11} - E S_{11} & H_{12} - E S_{12} & \cdots & H_{1n} - E S_{1n} \\ H_{21} - E S_{21} & H_{22} - E S_{22} & \cdots & H_{2n} - E S_{2n} \\ \vdots & \vdots & & \vdots \\ H_{N1} - E S_{N1} & H_{N2} - E S_{N2} & \cdots & H_{nn} - E S_{nn} \end{vmatrix} = 0$$

When the basis is orthonormal, $S_{nm} = \delta_{nm}$ and the usual eigenvalue problem returns.

It is fair to ask: are we then solving the problem exactly? Only if the basis set is complete. In practice we want the basis as small as we can manage, to keep the calculation tractable.

### Example: The infinite potential well

$$V(x) = \begin{cases} \infty & \text{for } |x| > a \\ 0 & \text{for } |x| \leq a \end{cases}$$

The solutions must therefore vanish at $x = \pm a$. We set $a=1$ and adopt natural units with $\hbar / 2m = 1$

A convenient choice is a polynomial basis

$$\psi_n(x) = x^n (x-1)(x+1) \quad ; \quad n = 0, 1, 2, \dots$$

The overlap matrix is computed without difficulty

$$S_{nm} = \int_{-1}^{1} \psi_n(x) \psi_m(x) \, dx = \frac{2}{m+n+5} - \frac{4}{m+n+3} + \frac{2}{n+m+1}$$

for $n+m$ even, zero otherwise

The Hamiltonian matrix elements are

$$H_{nm} = \langle n | \hat{P}^2 | m \rangle = \int_{-1}^{1} \psi_n(x) \left( -\frac{d^2}{dx^2} \right) \psi_m(x)\, dx$$

$$= -8 \left[ \frac{1 - m - n - 2mn}{(n+m+3)(n+m+1)(n+m-1)} \right]$$

for $m+n$ even, zero otherwise.

The problem then has to be solved numerically, with accuracy gained by retaining more basis states.

For illustration, let us keep only two states, $n = 0, 1$.

$$S_{00} = \frac{2}{5} - \frac{4}{3} + 2 = \frac{16}{15} \quad ; \quad H_{00} = \frac{8}{3}$$

$$S_{11} = \frac{2}{7} - \frac{4}{5} + \frac{2}{3} = \frac{16}{105} \quad ; \quad H_{11} = \frac{-8(-3)}{5 \cdot 3 \cdot 1} = \frac{8}{5} \quad ; \quad S_{01} = H_{01} = 0$$

$$\begin{vmatrix} \dfrac{8}{3} - \dfrac{16}{5}E & 0 \\[2mm] 0 & \dfrac{8}{5} - \dfrac{16}{105}E \end{vmatrix} = 0 \;\Rightarrow\; \frac{8}{3} - \frac{16}{15}E = 0 \;\Rightarrow\; E = \frac{15}{16} \cdot \frac{8}{3} = \frac{5}{2}$$

$$E_{\text{exact}} = \frac{\pi^2}{4} \approx 2.46$$

### Example: Hydrogen atom with Gaussians

It helps to work in "standard units"

- unit of distance : $a_0$
- unit of mass : $m_e$
- unit of energy : $m_e c^2 \alpha^2$ (Hartree)

The Schrödinger eq. then reads

$$\left[ -\frac{1}{2}\nabla^2 - \frac{1}{r} \right] \psi(x) = E\psi(x)$$

We want the ground state. Take a Gaussian basis

$$\chi_p(r) = e^{-\alpha_p r^2}$$

with

$$\alpha_1 = 13.00773$$
$$\alpha_2 = 1.962079$$
$$\alpha_3 = 0.444529$$
$$\alpha_4 = 0.1219492$$

The matrix elements are

$$S_{pq} = \int d^3r\; e^{-\alpha_p r^2} e^{-\alpha_q r^2} = \left( \frac{\pi}{\alpha_p + \alpha_q} \right)^{3/2}$$

$$T_{pq} = \int d^3r\; e^{-\alpha_p r^2} \nabla^2 e^{-\alpha_q r^2} = 3\, \frac{\alpha_p \alpha_q \pi^{3/2}}{(\alpha_p + \alpha_q)^{5/2}}$$

$$V_{pq} = \int d^3r\; e^{-\alpha_p r^2} \frac{1}{r} e^{-\alpha_q r^2} = -\frac{2\pi}{(\alpha_p + \alpha_q)}$$

With these, the problem is solved numerically to give

$$E_v = -0.499278\; E_H$$

The exact result is

$$E_{\text{exact}} = -\frac{1}{2} E_H$$

[blank page]

[blank page]

[blank page]


---

## References and Further Reading

*Editorial addition. The variational treatment of helium and of the hydrogen molecules is developed most fully in the companion texts below.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., introduces the approximation methods in Ch. 11 (Time-Independent Perturbations).

**Further reading.** Griffiths & Schroeter, *Introduction to Quantum Mechanics*, the "Variational Principle" chapter (the ground state of helium and the hydrogen-molecule ion H₂⁺); Sakurai & Napolitano, the variational-method section of the "Approximation Methods" chapter; Shankar, *Principles of Quantum Mechanics*, Ch. 16; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Complement E_XI.
# Chapter 7 — Fine and Hyperfine Structure

*The tiny corrections that pry a single spectral line apart into many.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

If you solve hydrogen with the plain Coulomb Hamiltonian, every line lands exactly where Bohr said it would. Look closer with a good spectrometer and the lines aren't single — they're bundles, split by gaps a thousand times finer than the gross structure. This chapter is about where those gaps come from and, just as important, how to keep track of them.

Two effects do most of the splitting. The hyperfine interaction couples the electron's spin to the proton's spin: $\vec{S}\cdot\vec{I}$. Spin-orbit coupling couples the electron's spin to its own orbital motion: $\vec{L}\cdot\vec{S}$. Both are small dot products of angular momenta sitting on top of a much bigger energy, so first-order perturbation theory is exactly the right tool.

The honest punchline is bookkeeping. A dot product like $\vec{S}\cdot\vec{I}$ is annoying in the uncoupled basis but trivial once you build the total angular momentum $\vec{F} = \vec{S} + \vec{I}$, because $2\vec{S}\cdot\vec{I} = F^2 - S^2 - I^2$ is diagonal. Adding angular momenta — and the Clebsch–Gordan coefficients that translate between bases — is the machinery that turns messy matrices into eigenvalues you can read off. We close with Landau–Zener tunnelling, where the adiabatic theorem is pushed until it yields an exact, non-perturbative answer.

## The hyperfine structure of H

The hyperfine interaction arises from the coupling between the spin of the nuclear proton and the spin of the electron orbiting it. We skip the derivation and simply quote the result,

$$\hat{H}_{hf} = \frac{A}{\hbar^2}\, \vec{S} \cdot \vec{I} \qquad \vec{S}, \vec{I}:\ \text{spin } 1/2$$

with

$$A = \frac{2\mu_0}{3}\, g_e \mu_B g_p \mu_N\, |\psi_{1s}(0)|^2$$

where

$$\mu_B = \frac{e\hbar}{2m_e} \qquad \text{Bohr magneton}$$

$$g_e \approx 2 \qquad \text{gyromagnetic ratio of the electron}$$

$$\mu_N = \frac{e\hbar}{2m_p} \qquad \text{nuclear magneton}$$

$$g_p \approx 5.59 \qquad \text{gyromagnetic ratio of the proton}$$

The spatial and spin parts of the wave function factorize and can be handled independently.

$$\langle r | \psi_{1s} \rangle = \psi_{1s}(r_1, \theta_1, \varphi_1) |\sigma\rangle_e |\sigma_I\rangle$$

The unperturbed Hamiltonian $H_0$ acts only on the spatial part, whereas the hyperfine term acts only on the spin. The perturbation can therefore be analyzed entirely within the space of spin configurations.

We have already encountered the problem of two spins $S = 1/2$. The configurations are $\{|\uparrow\uparrow\rangle; |\uparrow\downarrow\rangle; |\downarrow\uparrow\rangle; |\downarrow\downarrow\rangle\}$ and the Hamiltonian matrix

$$H_{hf} = A \begin{pmatrix} 1/4 & & & \\ & -1/4 & 1/2 & \\ & 1/2 & -1/4 & \\ & & & 1/4 \end{pmatrix}$$

with eigenstates $|\pm\rangle = \frac{1}{\sqrt{2}}\left( |\uparrow\downarrow\rangle \pm |\downarrow\uparrow\rangle \right)$; $|\uparrow\uparrow\rangle$; $|\downarrow\downarrow\rangle$ and energies

$$E_+ = E_{\uparrow\uparrow} = E_{\downarrow\downarrow} = A/4$$
$$E_- = -\frac{3A}{4}$$

Inserting $|\psi_{1s}(0)|^2 = 1/\pi a_0^3$, the ground state splits into its spin eigenstates

[diagram: $1s$ level splits into upper level $A/4$ corresponding to $|\uparrow\uparrow\rangle, |+\rangle, |\downarrow\downarrow\rangle$, and lower level $3/4\,A$ below, corresponding to $|-\rangle$]

## Total spin of the Hydrogen atom

$$\vec{F} = \vec{S} + \vec{I}$$

$$[\hat{F}_x, \hat{F}_y] = [\hat{S}_x + \hat{I}_x,\ \hat{S}_y + \hat{I}_y] = i\hbar(\hat{S}_z + \hat{I}_z) = i\hbar \hat{F}_z$$

$$\hat{F}_\pm = \hat{S}_\pm + \hat{I}_\pm$$

$$\hat{F}^2 = (\vec{S} + \vec{I})^2 = \vec{S}^2 + \vec{I}^2 + 2\vec{S}\cdot\vec{I} \qquad \circledast$$

$$[\hat{F}_i, \hat{F}_z] = 0$$

Because $\vec{F}$ obeys the angular-momentum algebra, we expect to find states $|F, M_F\rangle$ that are simultaneous eigenstates of $\hat{F}^2$ and $\hat{F}_z$. From $\circledast$ we obtain

$$\hat{F}^2 = \frac{3\hbar^2}{4} + \frac{3\hbar^2}{4} + 2\vec{S}\cdot\vec{I} = \frac{3\hbar^2}{2} + 2\vec{S}\cdot\vec{I}$$

which, up to an additive and a multiplicative constant, is just the hyperfine interaction $H_{hf}$.

$$[\hat{F}^2, H_{hf}] = 0$$

so the two operators share a set of eigenvectors

| $|\sigma\rangle$ | $F$ | $M_F$ | |
|---|---|---|---|
| $|-\rangle$ | 0 | 0 | singlet |
| $|\downarrow\downarrow\rangle$ | 1 | $-1$ | triplet |
| $|+\rangle$ | 1 | 0 | triplet |
| $|\uparrow\uparrow\rangle$ | 1 | 1 | triplet |

Hence, combining two spins $1/2$ produces the allowed values $F = S + I = 0, 1$.

The projections of the new states onto the original basis are the "Clebsch–Gordan" coefficients.

| | $|1,-1\rangle$ | $|10\rangle$ | $|11\rangle$ | $|00\rangle$ |
|---|---|---|---|---|
| $|\downarrow\downarrow\rangle$ | 1 | 0 | 0 | 0 |
| $|\uparrow\downarrow\rangle$ | 0 | $1/\sqrt{2}$ | 0 | $1/\sqrt{2}$ |
| $|\downarrow\uparrow\rangle$ | 0 | $+1/\sqrt{2}$ | 0 | $-1/\sqrt{2}$ |
| $|\uparrow\uparrow\rangle$ | 0 | 0 | 1 | 0 |

In the new basis,

$$\hat{H}_{hf} = \frac{A}{2}\left( \hat{F}^2 - \hat{S}^2 - \hat{I}^2 \right)$$

$$H_{hf} = -\frac{3A}{4} + \frac{A}{2}\begin{pmatrix} 0 & & & \\ & 1 & & \\ & & 1 & \\ & & & 1 \end{pmatrix} = A\begin{pmatrix} -3/4 & & & \\ & 1/4 & & \\ & & 1/4 & \\ & & & 1/4 \end{pmatrix}$$

## Addition of generalized angular momenta

Let us build a recipe for generating every eigenstate of the operator $F$ from the ladder operators $L^+, L^-$. For intuition, we revisit the previous example. Begin with the state $|\uparrow\uparrow\rangle$

$$F^+|\uparrow\uparrow\rangle = F^+|11\rangle = \sqrt{2}\hbar |10\rangle$$
$$F^-|10\rangle = \sqrt{2}\hbar |1-1\rangle$$

$$F^-:\quad |11\rangle \rightarrow |10\rangle \rightarrow |1-1\rangle$$

Since $F^-$ only shifts the quantum number $M_F$, it can never reach $|00\rangle$. But note that

$$F^-|11\rangle = (S^- + I^-)|\uparrow\uparrow\rangle = \hbar\left( |\downarrow\uparrow\rangle + |\uparrow\downarrow\rangle \right)$$

So to construct $|00\rangle$ we simply need the state orthogonal to $|10\rangle$, which must be

$$|00\rangle = \frac{1}{\sqrt{2}}\left( |\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle \right)$$

[diagram:
$|11\rangle$
$\;\downarrow F^-$
$|10\rangle \overset{\text{orthogonality}}{\longrightarrow} |00\rangle$
$\;\downarrow F^-$
$|1-1\rangle$]

Alternating $F^-$ with orthogonalization in this way generates the complete set of eigenstates of $F$.

The general situation involves two coupled angular momenta

$$\vec{J} = \vec{J}_1 + \vec{J}_2$$

In the "uncoupled" basis, states carry the labels $|j_1 j_2 m_1 m_2\rangle$, while in the coupled basis they read $|j_1 j_2, J, M\rangle$. The uncoupled states are eigenstates of $J_1^2, J_2^2, J_{1z}, J_{2z}$, and the coupled states are eigenstates of $J_1^2, J_2^2, J^2, J_z$. Since $j_1$ and $j_2$ are fixed in any given problem (say, a spin 1 and a spin 1/2), we can drop those labels and just write $|JM\rangle$ for the coupled states.

### Example

| | |
|---|---|
| $|11\rangle$ | $|\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}\rangle$ |
| $|10\rangle$ | $\frac{1}{\sqrt{2}}\left( |\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\rangle + |\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\rangle \right)$ |
| $|1-1\rangle$ | $|\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}\rangle$ |
| $|00\rangle$ | $\frac{1}{\sqrt{2}}\left( |\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\rangle - |\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\rangle \right)$ |

In general, $J$ runs between the two extremes in unit steps: $J = j_1 + j_2,\ j_1 + j_2 - 1, \cdots, |j_1 - j_2|$

with $M = -J, -J+1, \dots, J-1, J$.

To switch between the two bases we use the Clebsch–Gordan coefficients, which have been tabulated for arbitrary $J$.

$$|JM\rangle = \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} \left( |j_1 j_2 m_1 m_2\rangle \langle j_1 j_2 m_1 m_2| \right) |JM\rangle$$

$$= \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} \langle j_1 j_2 m_1 m_2 | JM\rangle\, |j_1 j_2 m_1 m_2\rangle$$

$$= \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} C^{j_1 j_2 J}_{m_1 m_2 M}\, |j_1 j_2 m_1 m_2\rangle$$

The C–G coefficients are real, so the inverse transformation is just the transpose.

$$|j_1 j_2 m_1 m_2\rangle = \sum_{J = |j_1 - j_2|}^{j_1 + j_2} \sum_{M = -J}^{J} |JM\rangle \langle JM | j_1 j_2 m_1 m_2\rangle$$

$$= \sum_{J = |j_1 - j_2|}^{j_1 + j_2} \sum_{M = -J}^{J} C^{j_1 j_2 J}_{m_1 m_2 M}\, |JM\rangle\, \delta_{M, m_1 + m_2}$$

$$= \sum_{J = |j_1 - j_2|}^{j_1 + j_2} C^{j_1 j_2 J}_{m_1 m_2 M}\, |JM\rangle$$

## Angular momentum and spectroscopic notation

The electron's total angular momentum is usually written $\vec{J}$

$$\vec{J} = \vec{L} + \vec{S}$$

Since the electron carries spin $S = 1/2$, we have

$$j = \ell + \frac{1}{2}\, |\ell + \frac{1}{2} - 1| = \begin{cases} \ell + \frac{1}{2},\ \ell - \frac{1}{2} & \ell \geq 1 \\ 1/2 & \ell = 0 \end{cases}$$

For atoms with more than one electron we sum all orbital and spin angular momenta, $J = L + S$. The atomic state is recorded in "spectroscopic notation"

$$^{2S+1}L_J$$

$$L = 0, 1, 2, 3, 4, 5, 6, 7$$
$$\text{letter} = S, P, D, F, G, H, I, K$$

### Examples:

ground-state of H : $^2S_{1/2}$

carbon has $L = 1, S = 0, J = 0$ : $^3P_0$

## Spin-orbit coupling

To see where spin-orbit coupling comes from, step into the electron's rest frame. From there, the electron sits at the origin and the proton sweeps around it like a current loop, generating a magnetic field. That field then couples to the electron's own spin magnetic moment.

[diagram: a loop with magnetic field $\vec{B}$ pointing up at center, electron $e^-$ at center, proton orbiting at radius $\vec{r}$]

At the center of the loop the magnetic field is

$$B = \frac{\mu_0 I}{2r}$$

The proton's speed in the electron frame equals the electron's speed in the proton frame

$$L = mvr \quad ; \quad v = \frac{L}{mr}$$

Writing the current as $I = \frac{e}{T}$ with period $T = 2\pi r/v$, we get

$$B = \frac{\mu_0}{2r}\frac{e}{T} = \frac{\mu_0}{2r}\frac{ev}{2\pi r} = \frac{\mu_0}{2r}\frac{eL}{2\pi r m r}$$

$$\Rightarrow \vec{B} = \frac{e\vec{L}}{4\pi \varepsilon_0 m c^2 r^3}$$

The interaction energy of a magnetic dipole in a magnetic field is

$$E = -\vec{\mu}\cdot\vec{B} \qquad \text{with}\quad \vec{\mu} = -\frac{e}{m}\vec{S}$$

$$\Rightarrow \hat{H}_{SO} = \frac{e^2}{4\pi\varepsilon_0 m^2 c^2 r^3}\, \hat{\vec{L}}\cdot\hat{\vec{S}}$$

It is convenient to switch to the total angular momentum basis

$$\vec{J} = \vec{L} + \vec{S}$$

$$J^2 = L^2 + S^2 - 2\vec{L}\cdot\vec{S}$$

$$\Rightarrow \vec{L}\cdot\vec{S} = \frac{1}{2}\left( J^2 - L^2 - S^2 \right)$$

The states are labeled by their quantum numbers

$$|n, \ell, s, j, m_j\rangle$$

with $j = \ell + s,\ \ell + s - 1,\ \dots,\ |\ell - s|$

The first-order energy correction from spin-orbit coupling is fixed by the matrix elements

$$\left\langle n\ell s j, m_j \left| \frac{\vec{L}\cdot\vec{S}}{r^3} \right| n\ell s j, m_j \right\rangle$$

$$= \left\langle \frac{1}{r^3} \right\rangle_{n\ell} \langle \ell s j, m_j | \vec{L}\cdot\vec{S} | \ell s j, m_j \rangle$$

$$= \frac{1}{2}\left\langle \frac{1}{r^3} \right\rangle_{n\ell} \langle \ell s j, m_j | J^2 - L^2 - S^2 | \ell s j, m_j \rangle$$

$$= \frac{1}{2}\left\langle \frac{1}{r^3} \right\rangle_{n\ell} \hbar^2 \left[ j(j+1) - \ell(\ell+1) - s(s+1) \right]$$

The radial expectation value works out to

$$\left\langle \frac{1}{r^3} \right\rangle_{n\ell} = \frac{1}{a_0^3\, n^3\, \ell(\ell + \frac{1}{2})(\ell+1)}$$

Putting the pieces together, we arrive at

$$\boxed{ E_{SO}^{(1)} = \frac{1}{4}\, \alpha mc^2\, \frac{j(j+1) - \ell(\ell+1) - 3/4}{n^3\, \ell(\ell + \frac{1}{2})(\ell+1)} }$$

This expression looks troublesome if we

consider $\ell = 0$, since numerator and denominator both vanish. But we can set the worry aside on physical grounds: when $\ell = 0$ there is no spin-orbit coupling at all, because the orbital angular momentum is zero. The formula thus applies only to $\ell \neq 0$.

[diagram: $n=2$ level splits into three levels — $2P_{3/2}$ (top), $2S_{1/2}$ (middle), $2P_{1/2}$ (bottom)]

## Fine structure of the H atom

The full set of energy corrections also contains relativistic pieces that we will not pursue here, among them terms arising from Dirac's equation $\rightarrow$ "Darwin" term.

## Landau–Zener tunnelling

Take a spin-$\frac{1}{2}$ subject to a $B$-field along the $x$-direction

$$H_0 = -\mu_B B_1 \tau_x = V\tau_x$$

Now turn on a time-dependent $B$-field along $z$ that ramps up linearly in time

$$H_1(t) = \alpha t\, \tau_z$$

(where $\alpha$ has the proper units)

The total Hamiltonian becomes

$$H(t) = \begin{pmatrix} \alpha t & V \\ V & -\alpha t \end{pmatrix} = \alpha t\, \tau_z + V\tau_x$$

Note that $H_1$ is not a small perturbation, since $|\alpha t|$ can grow large. Here $\alpha$ plays the role of a rate of change of $B_z$. The instantaneous energy eigenvalues are

$$E_\pm = \pm \sqrt{(\alpha t)^2 + V^2}$$

with eigenfunctions $|+\rangle = \begin{pmatrix} \sin\frac{\Theta(t)}{2} \\ \sin\frac{\Theta(t)}{2} \end{pmatrix}$; $|-\rangle = \begin{pmatrix} \sin\frac{\Theta(t)}{2} \\ \cos\frac{\Theta(t)}{2} \end{pmatrix}$

[diagram: avoided crossing of energy levels vs. time. Upper branch labeled $|+\rangle = |\uparrow\rangle$ on the left going to $|+\rangle = |\downarrow\rangle$ on the right (slope $\alpha t$); lower branch labeled $|-\rangle = |\downarrow\rangle$ on the left going to $|-\rangle = |\uparrow\rangle = -\alpha t$ on the right. The gap at the crossing is $2\,T_\alpha$ wide and $2V$ tall, with $T_\alpha = \frac{V}{\alpha}$.]

$\Theta(t)$ is a time-dependent function still to be determined.

It is worth noting that

$$\hat{H}(t) = \vec{n}(t)\cdot\vec{\tau} \qquad \text{with}\quad \vec{n} = (V, 0, \alpha t)$$

and

$$\Theta(t) = \tan^{-1}\left( \frac{V}{\alpha t} \right) \qquad E_\pm(t) = \pm |\vec{n}|$$

Unpacking the meaning of this would require the theory of spin rotations, which lies outside this discussion.

### Landau–Zener Solution

We take $\alpha V \gg \alpha$ so that the formulas derived for the

adiabatic theorem apply — suppose we begin in $|-\rangle$ and start ramping the field

$$\dot{C}_+(t) = -C_-(t)\, e^{i\theta_+^-(t)} \left\langle +\left|\frac{d}{dt}\right|-\right\rangle$$

with

$$\theta_+^-(t) = -\frac{1}{\hbar}\int_{-\infty}^{t}\left(E_-(t') - E_+(t')\right)dt'$$

Now examine the matrix elements:

$$\begin{cases}
\dfrac{d}{dt}|+\rangle = -\dfrac{d\theta}{dt}\dfrac{1}{2}\begin{pmatrix}\sin\theta/2 \\ -\cos\theta/2\end{pmatrix} = -\dfrac{d\theta}{dt}\,|-\rangle \\[2mm]
\dfrac{d}{dt}|-\rangle = \dfrac{d\theta}{dt}\dfrac{1}{2}\begin{pmatrix}\cos\theta/2 \\ \sin\theta/2\end{pmatrix} = \dfrac{1}{2}\dfrac{d\theta}{dt}\,|+\rangle
\end{cases}$$

$$\Rightarrow \begin{cases}
\left\langle -\left|\dfrac{d}{dt}\right|-\right\rangle = \left\langle +\left|\dfrac{d}{dt}\right|+\right\rangle = 0 \\[2mm]
\left\langle +\left|\dfrac{d}{dt}\right|-\right\rangle = \dfrac{1}{2}\dot{\theta} \\[2mm]
\left\langle -\left|\dfrac{d}{dt}\right|+\right\rangle = -\dfrac{1}{2}\dot{\theta}
\end{cases}$$

$$\Rightarrow C_+(t) = -\int_{-\infty}^{t} dt'\; C_-(t')\, e^{i\theta_+^-(t')} \left\langle +\left|\frac{d}{dt}\right|-\right\rangle$$

$$\boxed{C_-(t)\approx 1}$$

$$\approx \frac{1}{2}\int_{-\infty}^{t} dt'\;\dot{\theta}\; e^{\frac{2i}{\hbar}\int_{-\infty}^{t'}\sqrt{(\alpha t'')^2 + V^2}\,dt''}$$

We can evaluate $\dfrac{d\theta}{dt} = -\dfrac{V\alpha}{(\alpha t)^2 + V^2}$

Finally,

$$\boxed{\; C_+(\infty) \approx \frac{1}{2}\int_{-\infty}^{\infty} dt\; \frac{V\alpha}{(\alpha t)^2 + V^2}\; e^{\frac{2i}{\hbar}\int_{-\infty}^{t}\sqrt{(\alpha t')^2 + V^2}\,dt'}\;}$$

This integral can in fact be done exactly, giving

$$C_+(\infty) \approx \frac{\pi}{3}\, e^{-\pi V^2/\alpha}$$

or

$$P_+(\infty) = \frac{\pi^2}{9}\, e^{-\pi V^2/\alpha}$$

The exact answer to the problem is

$$P_+(\infty) = e^{-\pi V^2/\alpha}$$

This result is valid for any $\alpha$, not only $\alpha \to 0$. So as $\alpha$ increases, the system grows more likely to end up in $|+\rangle$ and the spin to **not flip**.

Observe that $\alpha/V^2 \ll 1$ ($V^2\!/\alpha \gg 1$) is exactly the condition for adiabatic evolution. And because $|\alpha t|$ can be made arbitrarily large, this solution is non-perturbative — it is inaccessible to perturbation theory.

**Large $\alpha$** — Landau–Zener tunnelling

*(Avoided-crossing diagram of energy levels vs. time. Two diabatic states cross as straight dashed diagonal lines; the adiabatic eigenstates are the solid curved branches that avoid each other, separated by a gap labeled $2V$.)*

- Upper-left branch: $|+\rangle = |\uparrow\rangle$
- Upper-right branch: $|+\rangle = |\downarrow\rangle$, with $\alpha\nearrow$ (large slope)
- Lower-left branch: $|-\rangle = |\downarrow\rangle$
- Lower-right branch: $|-\rangle = |\uparrow\rangle$
- Gap between branches: $2V$
- Horizontal axis: time ($t$)

*(Arrows trace the trajectory tunnelling across the gap — for large $\alpha$ the system follows the diabatic line and the spin does not flip.)*

**Small $\alpha$** — Adiabatic behavior

*(Same avoided-crossing diagram. For small $\alpha$ the system follows the lower adiabatic branch smoothly through the avoided crossing.)*

- Upper-left branch: $|+\rangle = |\uparrow\rangle$
- Upper-right branch: $|+\rangle = |\downarrow\rangle$, with $\alpha\searrow$ (small slope)
- Lower-left branch: $|-\rangle = |\downarrow\rangle$
- Lower-right branch: $|-\rangle = |\uparrow\rangle$
- Gap between branches: $2V$
- Horizontal axis: time ($t$)

*(Arrows trace the trajectory following the lower adiabatic branch across the avoided crossing — the system stays on the same energy surface and the spin flips.)*


---

## References and Further Reading

*Editorial addition mapping the notes to their source texts.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 11 (Time-Independent Perturbations) for fine structure and spin–orbit coupling; Ch. 3 and Ch. 5 for the addition of angular momenta. The Landau–Zener problem extends the adiabatic theorem of Chapter 4.

**Further reading.** Griffiths & Schroeter, the "Time-Independent Perturbation Theory" chapter (fine structure, the Zeeman effect, and hyperfine splitting of hydrogen); Sakurai & Napolitano, the "Approximation Methods" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XII. Original papers: L. D. Landau, *Phys. Z. Sowjetunion* **2**, 46 (1932); C. Zener, *Proc. R. Soc. Lond. A* **137**, 696 (1932).
<!--
    99-back-matter.md
    BACK MATTER — acknowledgments, about the authors, series editor,
    publisher, notes, references, glossary, and a note on the index.
-->

---

## Acknowledgments

Our first debt is to the students of PHYS 5125, whose questions shaped these notes over many offerings and whose careful reading caught errors that would otherwise have survived into print. We thank the Department of Physics at Northeastern University for the years in which this course took its present form. The transcription of the original handwritten notes into typeset mathematics, the page-by-page verification against the source, and the production of this edition were carried out through the **Medhavy** intelligent-textbook program at **Humanitarians AI**, under the direction of Nik Bear Brown. Any errors that remain are ours; the corrections that found their way in are owed to many hands.

---

## About the Author

**Adrian E. Feiguin** is a Professor of Physics at Northeastern University, where he works in computational condensed-matter physics, focusing on quantum systems with strong correlations. He is known for his work on numerical methods for quantum many-body problems — the density-matrix renormalization group (DMRG), exact diagonalization, and quantum Monte Carlo — and is a co-developer of the time-dependent DMRG (tDMRG), introduced in 2002, which extended these methods to systems out of equilibrium. His research ranges from quantum transport to exotic phases of matter in cold-atom systems. He joined the Department of Physics at Northeastern in 2012. This book is set from his handwritten lecture notes for the graduate quantum mechanics course PHYS 5125.

---

## About the Editors

**Gregory A. Fiete** is a Professor of Physics at Northeastern University, where he works in condensed-matter theory. His research spans topological materials, strongly correlated electron systems, frustrated magnetism, the fractional quantum Hall effect, and the behavior of quantum materials driven out of equilibrium. He received his Ph.D. in physics from Harvard University and held a Lee A. DuBridge Prize Fellowship at Caltech following postdoctoral work at the Kavli Institute for Theoretical Physics. His honors include the NSF CAREER Award, the DARPA Young Faculty Award, a Presidential Early Career Award for Scientists and Engineers (PECASE), and a Simons Fellowship in Theoretical Physics; he is an elected Fellow of the American Physical Society. He has taught the graduate quantum mechanics sequence at Northeastern for many years and edited this edition.

**Nik Bear Brown**, series editor, is an Associate Teaching Professor in the College of Engineering at Northeastern University and the founder of Humanitarians AI. He designs AI-assisted production pipelines for education and is the architect of the **Medhavy** intelligent-textbook system, which pairs primary-source course material with adaptive tutoring built on the principle that an AI tutor should deepen the friction that produces learning rather than remove it. He teaches and writes on AI fluency, computational skepticism, and what remains irreducibly human as machines grow more capable. He can be found at [nikbearbrown.com](https://www.nikbearbrown.com).

---

## About the Publisher

**Humanitarians AI** is a 501(c)(3) nonprofit founded in 2019 and based in Boston (EIN: 33-1984805). It connects graduates and researchers with real projects, experienced mentors, and a curriculum organized around the cognitive capacities the AI era most requires — the **Irreducibly Human** framework. Its programs include the Fellows Program, Botspeak (AI fluency), Lyrical Literacy, and the Medhavy intelligent-textbook system, through which this book was produced. Learn more at [humanitarians.ai](https://www.humanitarians.ai/).

---

## Notes

The mathematics in this book is presented in full on the page; explanatory citations are gathered here by chapter rather than as footnotes.

### Chapter 2
1. The exact value of the electron–electron repulsion integral for the helium ground state follows the treatment in Townsend, *A Modern Approach to Quantum Mechanics* (§12.31), which the lecture notes cite directly.

### Chapter 5
1. The helium ground- and excited-state energies, and the singlet–triplet splitting, are computed to first order in the electron–electron interaction; experimental values are quoted for comparison throughout.

### Chapter 7
1. The Landau–Zener transition probability $P = e^{-\pi V^2/\alpha}$ is stated in the non-perturbative form; the original Landau (1932) and Zener (1932) papers derive it in detail.

---

## References

The course draws on the standard graduate literature in quantum mechanics. The texts below are the natural companions to this book; Townsend is cited directly in the notes.

- Cohen-Tannoudji, Claude, Bernard Diu, and Franck Laloë. *Quantum Mechanics*, 2 vols. Wiley, 1991.
- Griffiths, David J., and Darrell F. Schroeter. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018.
- Merzbacher, Eugen. *Quantum Mechanics*, 3rd ed. Wiley, 1998.
- Messiah, Albert. *Quantum Mechanics*. Dover, 1999.
- Sakurai, J. J., and Jim Napolitano. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2020.
- Shankar, Ramamurti. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994.
- Townsend, John S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012.

---

## Glossary

**Adiabatic theorem** — A system that starts in an eigenstate of a slowly-changing Hamiltonian remains in the corresponding instantaneous eigenstate.

**Berry phase** — A geometric phase acquired by a state carried adiabatically around a closed loop in parameter space, independent of how slowly the loop is traversed.

**Degenerate perturbation theory** — Perturbation theory for states that share an unperturbed energy; one must diagonalize the perturbation within the degenerate subspace before proceeding.

**Exchange energy** — The (Fock) contribution to the energy of identical particles arising purely from the symmetry of the wavefunction, with no classical analogue.

**Fermi's golden rule** — The transition rate between an initial state and a continuum of final states under a harmonic perturbation, proportional to the density of final states.

**Fine structure** — Splitting of atomic energy levels from relativistic corrections and spin–orbit coupling.

**Hund's rule** — Among states of a partially filled shell, the lowest energy belongs to the configuration of maximum total spin.

**Hyperfine structure** — Finer splitting of atomic levels from the interaction between electronic and nuclear magnetic moments.

**Perturbation theory** — A method for approximating eigenvalues and eigenstates when the Hamiltonian differs from a solvable one by a small term.

**Slater determinant** — An antisymmetric many-fermion wavefunction written as the determinant of single-particle states; the permanent is its symmetric (bosonic) counterpart.

**Spin–orbit coupling** — The interaction between a particle's spin and the magnetic field it experiences due to its orbital motion.

**Variational method** — An approximation scheme that bounds the ground-state energy from above by minimizing the expectation value of the Hamiltonian over a family of trial states.

---

## A Note on the Index

This edition carries no back-of-book index. It is published as a Kindle and online book and is integrated with the **Medhavy** intelligent-textbook system at [medhavy.com](https://www.medhavy.com/) — *मेधावी (Medhavy)*, from the Sanskrit for "intelligent" or "intellectually brilliant." In that environment, search, cross-reference, and navigation are handled dynamically: a reader asks for a term and is taken to it, with adaptive explanation, rather than turning to a fixed list of page numbers that a reflowable digital text cannot honor anyway. A static index serves a printed page; an intelligent textbook serves the question directly.

*Come learn something with us.*
