# Minimal-survivor min-plus status — 2026-08-09

## Target quantity

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

define the coefficient stopping time \(\tau_c(n)\) as the first \(k\ge1\) for which
\(3^{q_k}<2^k\).  The minimal survivor is

\[
\mu(K)=\min\{n\ge1:\tau_c(n)>K\}.
\]

## Exact min-plus formulation

A parity prefix of length \(k\) has a unique canonical residue \(r_k\pmod{2^k}\).  Appending one parity bit changes the canonical lift by either zero or \(2^k\):

\[
r_{k+1}=r_k+c_k2^k,\qquad c_k\in\{0,1\}.
\]

Hence every edge has nonnegative cost and every descendant residue is at least its ancestor residue.  Finding \(\mu(K)\) is therefore an exact shortest-path/min-plus problem on the coefficient-survivor parity tree.  No probabilistic or unproved dominance assumption is used.

Current exact solvers:

- `collatz/src/minimal_survivor_bestfirst.cpp` — Dijkstra-style best-first search;
- `collatz/src/minimal_survivor_branch_bound.cpp` — depth-first branch-and-bound;
- `collatz/src/minimal_survivor_interval_scan.cpp` — general interval certificate scanner;
- `collatz/src/minimal_survivor_mod32_profile.cpp` — one-pass branch profile for the four depth-five survivor cylinders;
- `collatz/src/minimal_survivor_interval_scan_mod32.cpp` — accelerated exact interval scan using the rigorous mod-32 prefilter.

## Important correction

A list of large coefficient-stopping record holders is not automatically the complete step-function \(\mu(K)\).  Exact branch profiling found intermediate plateaus that had been omitted from earlier status notes, notably

\[
\mu(164)=362343,
\qquad
\mu(176)=1027431.
\]

The complete corrected plateau table through \(K=546\) is maintained in
`collatz/notes/2026-08-09-record-basin-profile.md`.

## Latest exact values

The late plateaus are

\[
\mu(k)=63728127\qquad(308\le k\le375),
\]

\[
\mu(k)=217740015\qquad(376\le k\le394),
\]

\[
\mu(k)=1200991791\qquad(395\le k\le397),
\]

\[
\mu(k)=1827397567\qquad(398\le k\le432),
\]

\[
\mu(k)=2788008987\qquad(433\le k\le446),
\]

and the new exact result from the current run is

\[
\boxed{\mu(447)=12235060455},
\qquad
\tau_c(12235060455)=547.
\]

Therefore

\[
\boxed{\mu(k)=12235060455\qquad(447\le k\le546)}.
\]

Using the exact depth-five residue filter

\[
n\bmod32\in\{7,15,27,31\},
\]

a continuous interval scan has currently eliminated every start below

\[
96235060456
\]

for survival through depth 547.  Thus

\[
\boxed{\mu(547)\ge96235060456}.
\]

## Four-channel decomposition

For every \(K\ge5\),

\[
\mu(K)=\min_{a\in\{7,15,27,31\}}\mu_a(K),
\]

where

\[
\mu_a(K)=\min\{n\equiv a\pmod{32}:\tau_c(n)>K\}.
\]

Writing \(n=a+32t\), the four exact five-step affine channels are

\[
\begin{aligned}
T^5(7+32t)&=20+81t, &q_5&=4,\\
T^5(15+32t)&=40+81t, &q_5&=4,\\
T^5(27+32t)&=71+81t, &q_5&=4,\\
T^5(31+32t)&=242+243t, &q_5&=5.
\end{aligned}
\]

The global \(\mu\)-curve is the lower envelope of these four nondecreasing branch curves.

## Growth target

The asymptotic Rhin exponent used in the current proof program gives the sufficient target

\[
\mu(K) > C K^{8.616}
\]

eventually, or equivalently a sufficiently small exponential growth rate for the inverse record function.  Stronger exponential growth of \(\mu(K)\) would more than suffice, but is not assumed.

The next exact computational target is \(\mu(547)\).  The next structural target is a branch-wise lower bound on \(\mu_a(K)\), preferably derived from the affine four-channel renormalization rather than from flat enumeration.
