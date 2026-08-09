# Exact scan progress for mu(547) — 2026-08-09

The previous exact plateau is

\[
\mu(447)=12235060455,
\qquad
\tau_c(12235060455)=547,
\]

so

\[
\mu(k)=12235060455\qquad(447\le k\le546).
\]

Using `collatz/src/minimal_survivor_interval_scan_mod32.cpp`, which rigorously restricts the search to the only four depth-five survivor residues

\[
\{7,15,27,31\}\pmod{32},
\]

a continuous interval scan has now eliminated every start in

\[
[12235060456,156235060456)
\]

for survival through depth 547.

Therefore the current exact lower bound is

\[
\boxed{\mu(547)\ge156235060456}.
\]

This supersedes the smaller lower bounds recorded earlier in the same day's status notes.

The scan is exact for the accelerated Collatz coefficient barrier: the depth thresholds \(a_j=\min\{q:3^q\ge2^j\}\) are generated with arbitrary-precision integer arithmetic, and candidate starts are tested only after the exact mod-32 survivor prefilter.
