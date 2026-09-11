# MATH-065 — exact closure of every multi-paid layer r >= 18

Date: 2026-09-11
Status: `EXACT FINITE CERTIFICATE FOR 18<=r<=64 / ANALYTIC CLOSURE FOR r>=65 / r<=17 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note repairs the singleton-resolution gap found in the original MATH-064 audit and corrects its accidental promotion of `r=23` into the MATH-063 automatic-safe range.

## 1. Audit correction first

MATH-063 proves

\[
\boxed{r=23\text{ is not automatically safe},\qquad r=24\text{ is the first automatically safe multi-source count}.}
\]

The original MATH-064 note accidentally wrote `23<=r<=64` for the automatic multi-source range.  That transcription was wrong.

A second audit issue was more important.  MATH-064 used the fact that 752 `r=22` phase/address cells could contain only singleton completed parity cylinders and removed them from the symbolic graph, but it did not then continue those singleton ordinary integers.  Therefore the original MATH-064 certificate did not by itself justify full `r=22` closure.

MATH-065 repairs both issues by using one uniform algorithm for every layer from `r=18` through `r=64`.  Singleton and multi-source cylinders are handled by the same exact dyadic state and neither class is silently discarded.

## 2. Exact state carried by the audit

For a fixed phase/address cell, every parity prefix carries

\[
\boxed{t\equiv\tau\pmod{2^h}}
\]

for the original source lift `t`.

After substituting

\[
t=\tau+2^h s,
\]

the current endpoint remains affine in the same integer parameter:

\[
\boxed{Y_h=A_h+3^{q_h}s.}
\]

Thus every branch retains same-integer lineage exactly.

The paid penalty has the form

\[
\mathcal P=\beta\Omega_0.
\]

On a source phase cell `(lo,hi)`, the certificate uses `beta*lo` as a strict lower-bound limit.  For every unfinished branch, all future paid odd events satisfy `u>=1`, so

\[
\mathcal P_{\rm future}
\ge
\frac16\sum_{j\ge j_0}\Omega_j.
\]

Therefore a branch is discarded as cost-safe only when

\[
\boxed{
\mathcal P_{\rm current,lo}
+
\mathcal P_{\rm future,min,lo}
\ge
\frac{19}{503}H.
}
\]

This is an exact lower-bound prune, not a heuristic.

At every parity step the dyadic residue is intersected with the exact allowed source-lift interval.  Empty residue classes are removed immediately.

A completed branch whose adjusted cost can still be negative is materialized as an exact arithmetic progression of ordinary targets.  Every such target is then continued under the shortcut Collatz map until it reaches

\[
\le2^{71}.
\]

For a hypothetical minimal positive counterexample above the frozen published floor, such a target cannot occur on its orbit.

## 3. Exact finite results, r=18 through r=26

The certificate gives the following complete counts.

| r | phase/address cells | cost-safe cells | singleton-only cells | multi-source critical cells | negative-candidate cylinders | ordinary targets, with multiplicity | unique targets | maximum descent steps |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 18 | 1121 | 302 | 621 | 198 | 826110 | 4593148 | 2844121 | 247 |
| 19 | 1121 | 318 | 649 | 154 | 299140 | 733660 | 451814 | 237 |
| 20 | 1155 | 364 | 690 | 101 | 76138 | 102512 | 63017 | 204 |
| 21 | 1155 | 393 | 706 | 56 | 13040 | 13901 | 8449 | 127 |
| 22 | 1192 | 433 | 752 | 7 | 2184 | 2188 | 1338 | 123 |
| 23 | 1232 | 490 | 742 | 0 | 229 | 229 | 150 | 47 |
| 24 | 1232 | 504 | 728 | 0 | 53 | 53 | 30 | 28 |
| 25 | 1275 | 567 | 708 | 0 | 7 | 7 | 4 | 6 |
| 26 | 1275 | 592 | 683 | 0 | 2 | 2 | 1 | 3 |

Every listed ordinary target reaches the frozen verification floor.

In particular, the repaired `r=22` workload is not 18 targets.  The old seven-cell calculation correctly audited 18 targets from the multi-source-critical portion, but the missing singleton-only branch contributes additional candidates.  The complete uniform audit gives

\[
\boxed{2184\text{ negative-candidate cylinders},\quad2188\text{ target occurrences},\quad1338\text{ unique targets}.}
\]

All of them descend, with maximum additional shortcut length

\[
\boxed{123}.
\]

Thus the conclusion `r=22 is closed` survives, but only after this repair.

## 4. Exact zero-candidate range, r=27 through r=64

For every

\[
\boxed{27\le r\le64},
\]

the same exact branch-and-bound leaves

\[
\boxed{0}
\]

completed cylinder whose lower adjusted cost can still be negative.

This includes singleton cells: they are not removed merely because their source multiplicity is one.  Their parity/slack branches are carried until either the dyadic source class becomes empty or the exact penalty lower bound reaches the `19/503` target.

For `r>=47`, the phase/address cost gate already closes every source cell before any endpoint-parity branching is necessary.  For `27<=r<=46`, some singleton-resolution cells remain after the first gate, but every one is eliminated by the exact future-cost branch bound.

## 5. Connection to MATH-062

MATH-062 independently proves

\[
\boxed{
r\ge65
\Longrightarrow
\mathcal P_{\rm cluster}-\frac{19}{503}\ell>0
}
\]

for every multi-paid cluster, without any same-integer continuation.

Combining that analytic result with the MATH-065 finite exact audit gives

\[
\boxed{
r\ge18
\Longrightarrow
\text{the multi-paid layer is closed for the current first-cell calculation}.}
\]

Therefore the only paid-count layers still requiring detailed treatment are

\[
\boxed{2\le r\le17.}
\]

## 6. DSD audit

### SAFE

1. phase intervals are refined before endpoint branching;
2. source-lift lineage is retained as one exact dyadic congruence at every step;
3. endpoint evolution is retained as one exact affine integer family;
4. penalty pruning uses an exact lower bound on every possible future completion;
5. singleton cylinders are explicitly carried rather than confused with closure;
6. every remaining finite ordinary target for `18<=r<=26` is directly continued to the verified floor;
7. `27<=r<=64` has zero negative-candidate completed cylinders;
8. MATH-062 supplies the independent analytic closure for `r>=65`.

### CORRECTED

- Original MATH-064 Gate B meant `remove from symbolic multi-source graph`, not `close the ordinary-integer branch`.
- Original MATH-064's `23<=r<=64` frontier was a transcription error; MATH-063 says the automatic multi-source cutoff begins at `r=24`.

### OPEN

- `2<=r<=17` multi-paid layers;
- mixed one-paid / remaining multi-paid Bellman potential;
- the genuinely aperiodic same-integer branch after the remaining paid counts are incorporated;
- first universal Farey cell emptiness;
- later Farey cells and full Collatz.

### PROHIBITED UPGRADES

- `r>=18` closure `=>` first universal cell closure;
- finite target descent `=>` a universal Collatz descent theorem;
- zero negative-candidate cylinders in these paid-count layers `=>` one-paid or `r<=17` branches are closed.

## 7. Next target

Continue downward from

\[
\boxed{r=17}
\]

with the same exact certificate rather than reintroducing special-case slack enumerators.

The desired next reduction is either

1. direct exact closure of successive counts `17,16,...`, or
2. once the finite workload begins to grow too quickly, extraction of a reusable Bellman potential from the exact branch costs before materializing all ordinary targets.

## Reproducibility

`collatz/src/2026_09_11_math065_paid_count_18plus_closure_certificate.py`
