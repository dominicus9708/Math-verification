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
\(3^{q_k}<2^k\), where \(q_k\) is the number of odd entries among the first \(k\)
iterates.

The minimal survivor is

\[
\mu(K)=\min\{n\ge1:\tau_c(n)>K\}.
\]

## Exact min-plus formulation

A parity prefix of length \(k\) has a unique canonical residue \(r_k\pmod{2^k}\).
When one more parity bit is appended, the canonical lift is either

\[
r_{k+1}=r_k
\]

or

\[
r_{k+1}=r_k+2^k.
\]

Hence every edge has nonnegative cost \(c_k2^k\), \(c_k\in\{0,1\}\), and every
descendant residue is at least its ancestor residue.  Therefore finding \(\mu(K)\)
is exactly a shortest-path/min-plus problem on the parity-prefix tree restricted by

\[
3^{q_j}\ge2^j\qquad(1\le j\le K).
\]

Three exact solvers were added:

- `collatz/src/minimal_survivor_bestfirst.cpp`: Dijkstra-style best-first search.
- `collatz/src/minimal_survivor_branch_bound.cpp`: depth-first branch-and-bound using
  monotonicity of canonical residue.
- `collatz/src/minimal_survivor_interval_scan.cpp`: exact interval verification of
  record jumps; OpenMP is optional.

No dominance conjecture, random model, or finite-lookahead quotient is used by these
solvers.

## Reproduced values

The exact solvers reproduce, among others,

\[
\mu(58)=27,
\]
\[
\mu(59)=703,
\]
\[
\mu(100)=10087,
\]
\[
\mu(134)=35655,
\]
\[
\mu(135)=270271,
\]
\[
\mu(172)=381727,
\]
\[
\mu(173)=626331,
\]
\[
\mu(224)=8088063,
\]
\[
\mu(246)=13421671,
\]
\[
\mu(287)=20638335,
\]
\[
\mu(297)=26716671,
\]
\[
\mu(298)=56924955,
\]
\[
\mu(375)=63728127.
\]

## New exact record jumps obtained in this run

Direct interval certificates after the preceding exact record give

\[
\mu(376)=217740015,
\qquad \tau_c(217740015)=395,
\]
so
\[
\mu(k)=217740015\quad(376\le k\le394).
\]

Next,

\[
\mu(395)=1200991791,
\qquad \tau_c(1200991791)=398,
\]
so
\[
\mu(k)=1200991791\quad(395\le k\le397).
\]

Next,

\[
\mu(398)=1827397567,
\qquad \tau_c(1827397567)=433,
\]
so
\[
\mu(k)=1827397567\quad(398\le k\le432).
\]

Next,

\[
\mu(433)=2788008987,
\qquad \tau_c(2788008987)=447,
\]
so
\[
\mu(k)=2788008987\quad(433\le k\le446).
\]

The complete interval

\[
[2788008988,6788008988)
\]

was checked for \(\tau_c(n)>447\) with no survivor.  Thus the current exact lower
bound is

\[
\boxed{\mu(447)\ge6788008988}.
\]

## Growth diagnostics

For selected points the exponential diagnostic \(\log_2\mu(k)/k\) is
approximately

- \(k=375\): 0.06913447,
- \(k=376\): 0.07366498,
- \(k=395\): 0.07635843,
- \(k=398\): 0.07730438,
- \(k=433\): 0.07246325.

The proven survivor-language entropy is

\[
H_2(\log_3 2)=0.9499555271883306\ldots,
\]

so the uniform-residue heuristic predicts exponent

\[
1-H_2(\log_3 2)=0.0500444728116694\ldots.
\]

The comparison is diagnostic only; no equidistribution theorem is assumed.

## Computational observations

At \(K=298\), on the local test environment:

- best-first: about 15.4 million popped nodes, large priority-queue memory;
- branch-and-bound: about 56.4 million visited nodes but only about 4 MB working
  memory and roughly 5 seconds wall time.

Thus the branch-and-bound formulation is currently preferable for medium-depth exact
work, while interval scanning is preferable once a preceding record provides a small
numerical search window.

## Next target

Continue the record chain from \(K=447\).  In parallel, seek a theorem giving a lower
bound on \(\mu(K)\), ideally polynomial of exponent greater than the effective
Rhin-based threshold (8.616 asymptotically), or stronger exponential growth.
