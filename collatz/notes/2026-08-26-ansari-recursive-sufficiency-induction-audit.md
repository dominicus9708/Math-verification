# Ansari recursive-sufficiency induction audit

Date: 2026-08-26

Status: primary-source algebra audit. This note corrects an upstream dependency used by the ternary Cantor-core branch. It is not a proof or disproof of the Collatz conjecture.

## 1. Published setup

Ansari (2025) defines

\[
F_0=4\mathbb N_0+3,
\]

and, for \(n\ge1\),

\[
F_n=
\bigcup_{a_0,\ldots,a_{n-1}\in\{0,1\}}
\left(
4\cdot3^n\mathbb N_0+
4\sum_{i=0}^{n-1}a_i3^i+3
\right).
\]

The paper's Lemma 3.1 claims that every \(F_n\) is recursively sufficient. The later ternary-Cantor intersection result depends on this claim.

The paper also states the elementary deletion rule used below: if \(F\) is recursively sufficient and \(A\subseteq F\), then \(F\setminus A\) is recursively sufficient if and only if \(A\) is recursive.

## 2. Exact n=1 audit

Modulo 36,

\[
F_1=\{3,7,15,19,27,31\}\pmod{36},
\]
while

\[
F_2=\{3,7,15,19\}\pmod{36}.
\]
Therefore

\[
\boxed{
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31).
}
\]

Now specialize the induction's auxiliary sets to \(n=1\). The published formula for \(F'_n\) gives

\[
F'_1\pmod{36}
=\{3,7,11,15,19,23,27,31,35\},
\]

whereas its chosen subset \(A'\) becomes

\[
A'=36\mathbb N_0+35.
\]
Thus

\[
F'_1\setminus A'
\pmod{36}
=\{3,7,11,15,19,23,27,31\},
\]
which is not \(F_2\).

Hence the equality

\[
F_{n+1}=F'_n\setminus A'
\]
used at the end of the published induction is false already for \(n=1\).

This is an algebraic defect in the proof as written. It does **not** prove that \(F_2\) or later \(F_n\) fail to be recursively sufficient; it means that the published induction does not establish that claim.

## 3. One half of the first missing deletion is recursive

Let

\[
x=36k+31,
\qquad
m=32k+27.
\]

Then \(m<x\) for every \(k\ge0\), and for the shortcut Collatz map

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even},
\end{cases}
\]

we have

\[
T(m)=48k+41,
\]

\[
T^2(m)=72k+62=2x,
\]

and therefore

\[
T^3(m)=x.
\]

So every member of \(36\mathbb N_0+31\) merges with the smaller positive integer \(32k+27\). Consequently

\[
\boxed{36\mathbb N_0+31\text{ is recursive}.}
\]

The first unrepaired class is therefore

\[
\boxed{36\mathbb N_0+27.}
\]

By the deletion rule, proving this remaining progression recursive would repair the single step \(F_1\to F_2\). It would not by itself repair the full induction for all \(n\).

## 4. Dependency correction for this repository

Until a valid proof that all relevant \(F_n\) are recursively sufficient is supplied, the implication

\[
\text{minimal Collatz counterexample}\Longrightarrow
\text{ternary }\{0,1\}\text{ Cantor core}
\]

is **not established** here.

Accordingly, all downstream calculations performed inside the fixed ternary selector family remain valid as conditional statements of the form

\[
\text{if the recursive-sufficiency entry theorem is repaired, then ...}
\]

but they must not be used as an unconditional reduction of the full Collatz conjecture.

In particular, the m44/m45 selector computations, post-address handoff, coefficient-survival equivalence, carry/Fourier calculations, and selector-separation calculations are retained as algebraic/finite results on that family, with their upstream dependency explicitly marked conditional.

## 5. DSD audit classification

The defect is an upstream **formation-domain edge failure**, not an arithmetic contradiction inside the later selector calculations:

\[
\text{global minimal counterexample}
\;\not\Rightarrow_{\rm currently\ proved}\;
\text{ternary selector domain}.
\]

Therefore the correct response is dependency downgrading plus repair of the entry edge, rather than deletion of downstream calculations.

## 6. Immediate repair target

The next unconditional target is to analyze

\[
36k+27=9(4k+3)
\]

as a recursive progression. Any claimed repair must provide, for every \(k\ge0\), a smaller positive integer merging with \(36k+27\), or an equivalent rigorously complete certificate. Finite density, finite sampling, or a measure-one family is not sufficient.
