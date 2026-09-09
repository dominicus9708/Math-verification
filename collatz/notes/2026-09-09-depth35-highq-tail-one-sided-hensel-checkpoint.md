# Depth-35 high-q one-sided root-Hensel checkpoint

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / PARTIAL DEPTH-35 / q>=28`
- MATH-045: `NOT YET ASSIGNED` — this checkpoint does not claim the full depth-35 audit.

## Restored baseline

The authoritative continuation point is MATH-044, the depth-34 q-partitioned one-sided root-Hensel audit, with exactly `124,486,440` nested coefficient+previous-Hensel survivors.

At depth 35, `q_min(35)=23`. Only depth-34 q=22 parents lose their even child, so the exact pre-Hensel count is

\[
2\cdot124,486,440-32,432,663
=\boxed{216,540,217}.
\]

Exact depth-35 prefilter layers:

| q | prefilter |
|---:|---:|
| 23 | 71,570,859 |
| 24 | 67,080,250 |
| 25 | 43,090,675 |
| 26 | 21,735,285 |
| 27 | 8,937,042 |
| 28 | 3,038,795 |
| 29 | 852,042 |
| 30 | 194,491 |
| 31 | 35,325 |
| 32 | 4,923 |
| 33 | 496 |
| 34 | 33 |
| 35 | 1 |

The q=23,24,25 layers alone contain `181,741,784` candidates, about `83.93%` of the full depth-35 prefilter.

## Exact high-q method

For terminal q>=28 at k=35, `d=k-q<=7`. The quantity d never decreases: an odd child keeps d fixed and an even child raises d by one. Therefore restricting the symbolic computation to d<=7 is exact for every terminal depth-35 state with q>=28.

On the arbitrary-competitor side, retain one maximum correction C per exact Hensel class

\[
(q,r),\qquad r=C\bmod 3^q,
\]

using the MATH-013 downstream-stable class-max quotient.

On the candidate side, retain the MATH-044 one-sided selection rule exactly:

\[
\text{candidate}\in\mathcal L_{\rm coefficient+previous\ Hensel},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

## Regression audit

Before depth 35, depth-34 q=27..34 survivor counts were recomputed and compared with MATH-044. All eight layers agree exactly:

| q | recomputed | MATH-044 |
|---:|---:|---:|
| 27 | 2,350,378 | 2,350,378 |
| 28 | 688,417 | 688,417 |
| 29 | 163,625 | 163,625 |
| 30 | 30,866 | 30,866 |
| 31 | 4,459 | 4,459 |
| 32 | 464 | 464 |
| 33 | 32 | 32 |
| 34 | 1 | 1 |

## New exact depth-35 result

| q | prefilter | arbitrary classes | survivors | newly pruned |
|---:|---:|---:|---:|---:|
| 28 | 3,038,795 | 5,315,745 | 3,038,688 | 107 |
| 29 | 852,042 | 1,337,403 | 852,002 | 40 |
| 30 | 194,491 | 277,659 | 194,491 | 0 |
| 31 | 35,325 | 46,348 | 35,325 | 0 |
| 32 | 4,923 | 5,985 | 4,923 | 0 |
| 33 | 496 | 562 | 495 | 1 |
| 34 | 33 | 35 | 33 | 0 |
| 35 | 1 | 1 | 1 | 0 |

Thus the fully audited high-q tail is

\[
\boxed{4,126,106\to4,125,958},
\]

with exactly

\[
\boxed{148}
\]

new depth-35 Hensel removals in q>=28. This closes about `1.91%` of the full depth-35 prefilter exactly.

## Remaining depth-35 work

The unresolved layers for a full MATH-045-style audit are q=23..27, with exactly

\[
\boxed{212,414,111}
\]

prefilter candidates. The dominant q=23,24,25 layers require the `(q,residue-bucket)` refinement prescribed by MATH-044. No q=23..27 value is inferred from the high-q tail.

## Reproducibility

- certificate: `collatz/src/2026_09_09_depth35_highq_d7_one_sided_hensel_certificate.cpp`
- ledger: `collatz/results/2026-09-09-depth35-highq-d7-one-sided-hensel.tsv`
- local certificate SHA-256 before repository insertion: `259272b2e370dd2d7646c24119c1fb84e0469f92a82dbe120e6608d559514a16`
- local stdout SHA-256: `1fb2e3632cee928e1c38bf41ee80f4848ac0f958684169c36daff2088946b8a4`

## Prohibited upgrades

- q>=28 exact closure => full depth-35 closure — **PROHIBITED**;
- 148 removals => asymptotic pruning rate — **PROHIBITED**;
- finite depth-35 prefix pruning => Collatz proof — **PROHIBITED**;
- high-q behavior => central q=23..27 behavior — **PROHIBITED**.
