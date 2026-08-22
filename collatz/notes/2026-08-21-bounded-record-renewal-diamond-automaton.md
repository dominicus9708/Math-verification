# Bounded-record renewal diamond automaton

Date: 2026-08-21

Status: **exact finite-state reduction and local renewal diamond for bounded record lengths.** This identifies the remaining bounded-length Hensel problem but does not yet prove its global cross-base extinction and does not prove the Collatz conjecture.

Fix a record-gap cutoff

\[
M\ge6.
\]

Consider a sufficiently high record tail in which every new record height is reached within at most \(M\) accelerated steps of the preceding record.

Because the absolute record height tends to infinity while every excursion has length at most \(M\), the coefficient floor \(h\ge0\) is eventually inactive inside one excursion. The tail can then be described by a finite relative automaton.

## 1. Finite relative state

Let

\[
R_k=\max_{j\le k}h_j
\]

be the current record height and define

\[
\boxed{d_k=R_k-h_k\ge0}
\]

and

\[
\boxed{a_k=k-\tau_{R_k}}
\]

where \(a_k\) is the age since the current record was first reached.

Under the bounded-record condition,

\[
0\le a_k<M.
\]

Since \(h\) can fall by at most one per step,

\[
0\le d_k\le a_k.
\]

Thus the asymptotic state space is the finite triangle

\[
\boxed{
\mathcal Q_M
=\{(d,a):0\le d\le a<M\},
}
\]

of size \(M(M+1)/2\).

Let

\[
m_{k+1}=b_{k+1}-b_k\in\{0,1\}
\]

be the mechanical Beatty bit and \(\varepsilon_{k+1}\in\{0,1\}\) the actual parity bit.

Before a new record,

\[
h_{k+1}-h_k=\varepsilon_{k+1}-m_{k+1}.
\]

A new record can occur only when

\[
d_k=0,
\qquad m_{k+1}=0,
\qquad\varepsilon_{k+1}=1.
\]

Then

\[
(d_{k+1},a_{k+1})=(0,0).
\]

Otherwise

\[
\boxed{
d_{k+1}=d_k+m_{k+1}-\varepsilon_{k+1},}
\]

\[
\boxed{a_{k+1}=a_k+1,}
\]

and the transition is legal iff

\[
0\le d_{k+1}\le a_{k+1}<M.
\]

This is an exact finite-state description of every sufficiently high bounded-record tail.

## 2. Mechanical plateau gaps are two or three

The mechanical word has no `00` and no `111`.

Therefore consecutive plateau bits \(m=0\) are separated by either two or three time steps.

Starting from a reset state \((0,0)\) at a record plateau, let

\[
p_1<p_2
\]

be the next two mechanical plateau times. Then

\[
1\le p_1-s\le3,
\qquad
2\le p_2-p_1\le3,
\]

and hence

\[
\boxed{p_2-s\le6.}
\]

## 3. Exact two-path renewal diamond

From the reset at time \(s\), follow the mechanical bit on every rise, so parity is odd whenever \(m=1\).

At the first future plateau \(p_1\), define two alternatives.

### Delayed branch

Use

\[
\varepsilon_{p_1}=0
\]

and then use odd parity on all intervening rises and

\[
\varepsilon_{p_2}=1.
\]

No record is created at \(p_1\); the next record is created at \(p_2\). Its gap is at most six, so it is legal for \(M\ge6\).

### Early branch

Use

\[
\varepsilon_{p_1}=1
\]

and otherwise the **same parity bits** as the delayed branch through \(p_2\).

This creates a record at \(p_1\), and the odd plateau at \(p_2\) creates the next record as well. Every record gap is at most three.

At time \(p_2\), both branches therefore end in the identical relative state

\[
\boxed{(d,a)=(0,0).}
\]

They have the same length and the same suffix state, and differ in exactly one parity bit: the bit at \(p_1\).

Thus they form an exact renewal diamond.

## 4. Exact critical Haar cancellation of a diamond

Fix the common parity prefix before \(p_1\). The two diamond branches are its even and odd children at the bit \(p_1\), after which they are reunited at \(p_2\).

For a dyadic Fourier frequency whose critical bit is \(p_1\), the two canonical residue characters differ by

\[
\exp(\pi i u)=-1
\]

for odd reduced frequency \(u\).

Because the two branches have exactly the same continuation state at \(p_2\), every common future completion pairs with equal multiplicity.

Therefore the paired diamond contribution at its critical Haar level is exactly zero:

\[
\boxed{
\text{early contribution}+\text{delayed contribution}=0.
}
\]

This is stronger than an asymptotic Harnack estimate: it is a finite exact cancellation whenever both sides of the renewal diamond are included.

## 5. Concatenated diamond sublanguage

After \(p_2\), both branches are reset, so the construction can be repeated using the next two plateaus.

Each diamond block has length at most six. Consequently one obtains an explicit family of valid bounded-record parity words with one independent binary diamond choice per at most six time steps.

For \(n\) concatenated diamonds there are exactly

\[
2^n
\]

constructed parity words, all ending at the same relative reset state.

The parity-to-canonical-residue map is triangular in time, so these choices are also distinct dyadic residue classes.

This provides an explicit renewal/Haar cube inside the bounded-record language.

## 6. What remains

The local diamond does **not** by itself show that the entire bounded-record language is uniformly distributed, because arbitrary valid paths need not follow the selected diamond skeleton.

The remaining bounded-tail theorem is now finite-state:

> **Bounded-record renewal/Hensel theorem.** Use the finite automaton \(\mathcal Q_M\), its forced reset within \(M\) steps, and the exact plateau diamonds to prove a uniform cross-base/Haar contraction for the full bounded-record language after quotienting the finitely many terminal levels.

For every fixed cutoff \(M\), this is a finite-state nonautonomous renewal cocycle driven by the fixed Beatty mechanical word. The unbounded-record side has already been reduced to vanishing information cost per bit, so this finite automaton is the remaining complementary tail.

Companion certificate:

`collatz/src/bounded_record_renewal_diamond_certificate.py`.
