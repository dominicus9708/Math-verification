# Prefix-channel interval scan and first-merge diagnostics

Date: 2026-08-10

Status: **exact finite computation + structural diagnostics**. This is not a proof of the Collatz conjecture or of the CST conjecture.

## 1. Prefix-channel interval decomposition

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

let a depth-\(B\) coefficient-surviving parity cylinder have canonical state

\[
(r,q,y),
\qquad y=T^B(r).
\]

Every integer in the same residue cylinder is

\[
n=r+m2^B.
\]

The parity-vector lift identity gives exactly

\[
\boxed{T^B(n)=y+3^q m.}
\]

Thus an interval scan for

\[
\mu(K)=\min\{n\ge1:\tau_c(n)>K\}
\]

can enumerate only the coefficient-surviving depth-\(B\) channels and begin orbit testing at step \(B+1\). This replaces the previous mod-32 prefilter by a deeper exact channel-indexed filter.

The implementation is

`collatz/src/prefix_channel_interval_scan.cpp`.

The coefficient thresholds

\[
a_j=\min\{q:3^q\ge2^j\}
\]

are generated with arbitrary-precision integers. The channel-lift and later orbit arithmetic use unsigned 128-bit integers with an explicit overflow check. Any overflow makes the run fail rather than silently accepting a certificate.

## 2. Cross-check against the known exact plateau

The existing exact computation gives

\[
\mu(447)=12,235,060,455.
\]

Running the new prefix-channel scanner with \(B=24\) over

\[
[12,000,000,000,12,300,000,000)
\]

returns exactly

\[
\boxed{12,235,060,455}.
\]

The previous mod-32 scanner returns the same value on the same interval.

Candidate counts on this check were:

- prefix-channel \(B=24\): 5,124,414 candidates;
- mod-32: 37,500,000 candidates.

This is an exact implementation cross-check, not an asymptotic statement.

## 3. Scanner benchmark

For the interval

\[
[156,235,060,456,156,335,060,456)
\]

at target depth \(K=547\), representative local runs gave:

| prefilter | candidates tested | representative runtime |
|---|---:|---:|
| mod-32 | 12,499,997 | 0.15 s |
| prefix \(B=20\) | 2,606,203 | 0.05 s |
| prefix \(B=24\) | 1,708,154 | 0.04 s |
| prefix \(B=28\) | 1,312,755 | 0.14 s |

For a larger 10-billion-wide interval,

\[
[200,000,000,000,210,000,000,000),
\]

\(B=28\) amortizes its larger channel-construction cost and was faster:

- \(B=24\): 170,815,566 candidates, about 3.21 s;
- \(B=28\): 131,301,108 candidates, about 2.53 s.

The wall-clock values are machine-dependent diagnostics. The candidate counts and the interval certificates are the relevant reproducible quantities.

## 4. Updated exact lower bound for mu(547)

The previous repository status had eliminated every start below

\[
156,235,060,456
\]

for survival through depth 547.

The new prefix-channel scanner was run continuously over the following adjacent intervals:

| interval | B | candidates tested | overflows | survivor |
|---|---:|---:|---:|---:|
| [156,235,060,456, 200,000,000,000) | 24 | 747,573,362 | 0 | none |
| [200,000,000,000, 250,000,000,000) | 28 | 656,505,354 | 0 | none |
| [250,000,000,000, 300,000,000,000) | 28 | 656,505,139 | 0 | none |
| [300,000,000,000, 350,000,000,000) | 28 | 656,505,432 | 0 | none |
| [350,000,000,000, 400,000,000,000) | 28 | 656,504,981 | 0 | none |

The new runs tested

\[
3,373,594,268
\]

prefix-channel candidates in total, with zero detected 128-bit overflows.

Combining them with the previous continuous exact scan gives

\[
\boxed{\mu(547)\ge400,000,000,000.}
\]

No extrapolation is being made beyond the scanned interval.

---

## 5. Endpoint merge correction

The earlier endpoint-dominance experiment observed that, through the tested depths, a common endpoint had a single Pareto representative for the minimal-survivor objective.

A coarse sufficient inequality derived from the Rozier--Terracol remainder bounds is the following. For same-depth states with common endpoint \(y\) and

\[
q_h>q_l,
\]

a sufficient condition for the higher-\(q\) state to have the smaller canonical start is

\[
\boxed{
y>\frac32\left[\left(\frac32\right)^{q_l}-1\right].
}
\]

This condition is only sufficient. It is **not** valid for every inherited same-endpoint pair at every later depth. A concrete diagnostic example is the pair with starts 703 and 2111: after it has already merged, subsequent even steps reduce the common endpoint until the coarse endpoint bound eventually fails, while the already-established start ordering remains unchanged.

Therefore the meaningful place to test this inequality is the **first merge depth**, not every inherited collision depth.

## 6. Exact first-merge diagnostics

The implementation

`collatz/src/endpoint_first_merge_diagnostics.cpp`

marks a pair as a new merge at depth \(k\) exactly when the two states have the same time-\(k\) endpoint but different time-\((k-1)\) endpoints.

For each new merge with \(q_h>q_l\), it checks:

1. the exact integer form of the coarse endpoint sufficient condition;
2. correction-numerator order
   \[
   R_h>R_l,
   \qquad
   R=2^k y-3^q r;
   \]
3. actual start order
   \[
   r_h<r_l.
   \]

Through depth \(k=32\):

- cumulative new merge pairs: 2,760,811;
- cumulative new equal-\(q\) merge pairs: 0;
- coarse first-merge endpoint-bound failures: 0;
- first-merge correction-order failures: 0;
- first-merge start-order failures: 0.

At depth 32 alone there are 1,239,630 new merge pairs with distinct \(q\), and all three checks pass.

These are computational observations. In particular,

\[
\boxed{R_h>R_l\text{ at every new coefficient-surviving merge}}
\]

is now a natural theorem candidate, but is not yet proved globally.

## 7. Exact Pareto dynamic-programming check

Using only the already verified dominance lemma

\[
y_1=y_2,\qquad r_1\le r_2,\qquad q_1\ge q_2
\quad\Longrightarrow\quad
\text{state 1 dominates state 2 for every common future},
\]

an exact dynamic program was also run with dominated states removed after each depth.

Through depth 34, every endpoint appearing in this recursively Pareto-pruned dynamic program retained exactly one Pareto state. At depth 34:

- generated states before same-depth pruning: 125,282,266;
- states retained after exact Pareto pruning: 125,243,985;
- endpoints retaining more than one Pareto state: 0.

This does **not** prove that every endpoint in the full unpruned survivor tree has one Pareto state at all depths. It shows that the exact dominance quotient remains single-state-per-endpoint through depth 34 along the recursively pruned computation.

## 8. Current structural target

The first-merge computation suggests a sharper target than the earlier global endpoint inequality:

> **First-Merge Correction Order target.** At the first time two coefficient-surviving same-depth paths enter a common endpoint, if \(q_h>q_l\), prove
> \[
> R_h>R_l.
> \]

Because the endpoint is common,

\[
2^k y=3^{q_h}r_h+R_h=3^{q_l}r_l+R_l.
\]

If \(q_h>q_l\) and \(R_h>R_l\), then the higher-\(q\) branch is forced toward the smaller start. Once two paths have merged, their future orbit is identical and no new endpoint-order proof is needed for that pair.

This moves the endpoint-quotient problem from an inherited global condition to a local **coalescence event** condition, which is much better aligned with the deterministic structure of the Collatz map.
