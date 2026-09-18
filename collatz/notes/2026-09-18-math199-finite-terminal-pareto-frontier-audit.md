# MATH-199 — finite terminal Pareto-frontier audit through depth 30

Date: 2026-09-18

Status: `EXACT FINITE COMPUTATIONAL EVIDENCE / TERMINAL-ONLY PARETO AUDIT / NO PROOF-SCOPE EXPANSION`

## 1. Purpose

MATH-197/198 derive an exact terminal risk order at fixed outer state \((k,q)\):

\[
N\text{ smaller},\qquad C\text{ larger}.
\]

The purpose of this audit is purely quantitative:

> before adding future-branch and Hensel-state requirements, how large is the exact terminal Pareto record set among all coefficient-valid parity words?

This does not prove a frontier bound and does not permit transfer pruning across different future parity branches.

## 2. Enumerated language

For a parity prefix of depth \(k\) and odd count \(q\), retain only words whose every prefix remains coefficient-valid,

\[
2^j\le3^{q_j}.
\]

For each retained word, propagate the exact correction

\[
C'=3^bC+b2^j.
\]

At terminal depth \(k\), the parity word determines the canonical ordinary-source residue

\[
a\equiv-C(3^q)^{-1}\pmod{2^k}.
\]

Because the theorem-facing floor is \(B_0=2^{71}\) and \(k\le30\), \(B_0\) is divisible by \(2^k\). The least ordinary source above the floor with that residue is therefore

\[
N_{\min}=
\begin{cases}
B_0+a,&a>0,\\
B_0+2^k,&a=0.
\end{cases}
\]

Only the offset \(N_{\min}-B_0\) is required for ordering.

## 3. Pareto rule

Within each fixed \((k,q)\), sort states by increasing \(N_{\min}\).

A state is terminally dominated once an earlier state has correction at least as large.

Thus the undominated records are exactly the strict record highs of \(C\) in increasing source order.

This is precisely the MATH-197 terminal Pareto order.

## 4. Exact totals

The exact finite audit gives

| depth \(k\) | coefficient-valid words | terminal Pareto records |
|---:|---:|---:|
| 28 | 3,524,586 | 120 |
| 29 | 6,385,637 | 122 |
| 30 | 12,771,274 | 141 |

Corresponding compression ratios are approximately

\[
3.40\times10^{-5},
\qquad
1.91\times10^{-5},
\qquad
1.10\times10^{-5}.
\]

Thus raw word count nearly doubles while the terminal record count stays near one hundred in this finite range.

This is computational evidence only.

## 5. Depth-30 per-q ledger

For \(k=30\):

| q | words | Pareto records |
|---:|---:|---:|
| 19 | 1,900,470 | 15 |
| 20 | 4,036,203 | 12 |
| 21 | 3,499,420 | 20 |
| 22 | 2,014,260 | 10 |
| 23 | 894,180 | 17 |
| 24 | 315,483 | 14 |
| 25 | 88,349 | 18 |
| 26 | 19,315 | 11 |
| 27 | 3,190 | 12 |
| 28 | 375 | 9 |
| 29 | 28 | 2 |
| 30 | 1 | 1 |

Total:

\[
\boxed{12,771,274\to141.}
\]

## 6. Example slice k=30, q=20

The \(q=20\) slice contains

\[
4,036,203
\]

coefficient-valid words and only

\[
\boxed{12}
\]

terminal Pareto records.

Their source offsets and corrections are:

| offset \(N-B_0\) | C |
|---:|---:|
| 703 | 4,438,117,585 |
| 927 | 9,377,426,929 |
| 3,951 | 12,707,335,457 |
| 53,787 | 13,254,272,437 |
| 81,915 | 13,634,587,093 |
| 106,235 | 13,798,505,173 |
| 477,415 | 14,208,423,977 |
| 845,639 | 14,705,263,561 |
| 1,525,831 | 14,938,313,417 |
| 2,188,123 | 16,294,879,349 |
| 29,252,603 | 16,351,391,189 |
| 700,341,243 | 16,754,044,373 |

The last record has even positions

\[
(2,5,8,10,13,16,18,21,24,27).
\]

This visibly resembles a balanced/mechanical placement, but no Beatty/Christoffel identification is claimed here.

## 7. Why this is not yet the transfer frontier

MATH-198 proves branchwise Pareto pruning only after exact future/address partition.

The present audit deliberately ignores that partition and asks only a terminal question.

Therefore the counts above must **not** be interpreted as

- future-complete state counts;
- Hensel-survivor frontier counts;
- a bound valid through depth 41;
- a first-cell proof.

Removing illegal or Hensel-dominated states can change which surviving states are record representatives, while future-branch partition can split one terminal frontier into several transfer frontiers.

## 8. Research implication

The observed scale separation

\[
\text{millions of coefficient-valid words}
\quad\to\quad
O(10^2)\text{ terminal records}
\]

suggests that the MATH-198 transfer frontier may be tractable if its future-equivalence partition is not too fine.

The next exact target is therefore:

1. attach the next exact parity/future-address class to each record;
2. recompute Pareto records separately inside each class;
3. then attach the MATH-051 Hensel viability predicate;
4. measure the resulting future-complete frontier over the 338 MATH-179 outer states.

## 9. Claim boundary

Established only as exact finite computation:

- coefficient-valid word counts at depths 28--30;
- exact terminal Pareto record counts;
- exact depth-30 per-q ledger;
- exact \((N-B_0,C)\) record list for \((k,q)=(30,20)\).

Not established:

- any asymptotic or depth-41 frontier bound;
- a Beatty/Christoffel characterization of the records;
- future-complete Pareto compression;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
