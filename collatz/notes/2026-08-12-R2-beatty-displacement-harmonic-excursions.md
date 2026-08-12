# R2 Beatty displacement, harmonic escape, and economical renewal excursions

Date: 2026-08-12

Status: **exact reduction for the eventual coefficient-survival renewal branch (R2)**. The harmonic estimate used below is the previously established nonperiodic first-descent-survivor bound. This note narrows R2 but does not exclude it.

## 1. R2 setup

Let

\[
\gamma:=\log_2 3.
\]

Work on an odd-event tail beginning at an odd renewal floor `N`. Let

\[
A_i:=\sum_{r=0}^{i-1}v_r,
\qquad A_0=0,
\]

where

\[
v_r=v_2(3x_r+1)\ge1
\]

is the odd-to-odd Syracuse valuation.

In R2 the coefficient never crosses below one from the chosen renewal floor. At every odd-event checkpoint,

\[
\frac{3^i}{2^{A_i}}>1
\qquad(i\ge1).
\]

Since `gamma` is irrational, this is equivalent to

\[
\boxed{A_i\le\lfloor i\gamma\rfloor.}
\]

Define the critical Beatty event position and the displacement

\[
\boxed{A_i^*:=\lfloor i\gamma\rfloor,}
\qquad
\boxed{s_i:=A_i^*-A_i\ge0.}
\]

Thus R2 is an infinite left displacement of the critical Beatty event positions.

## 2. Exact displacement transition

Put

\[
r_i:=A_{i+1}^*-A_i^*
=\lfloor(i+1)\gamma\rfloor-\lfloor i\gamma\rfloor.
\]

Because `1<gamma<2`,

\[
\boxed{r_i\in\{1,2\}.}
\]

Since `A_{i+1}-A_i=v_i`,

\[
\boxed{s_{i+1}-s_i=r_i-v_i.}
\]

As `v_i>=1`,

\[
\boxed{s_{i+1}-s_i\le r_i-1\in\{0,1\}.}
\]

More precisely:

- if `r_i=1`, displacement cannot increase;
- if `r_i=2`, displacement can increase by at most one;
- displacement may drop by an arbitrarily large amount when `v_i` is large.

Thus the R2 defect is a one-sided staircase: slow upward motion and potentially large downward resets.

## 3. Exact correction mass in displacement coordinates

The odd-event correction is

\[
c_q
=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}}.
\]

Using

\[
A_i=\lfloor i\gamma\rfloor-s_i
\]

and

\[
3^i=2^{i\gamma},
\]

we obtain

\[
\boxed{
c_q
=\frac13\sum_{i=0}^{q-1}
2^{-\{i\gamma\}}2^{-s_i}.}
\]

Because

\[
\frac12<2^{-\{i\gamma\}}\le1,
\]

we have the exact comparison

\[
\boxed{
\frac16\sum_{i<q}2^{-s_i}
<c_q
\le\frac13\sum_{i<q}2^{-s_i}.}
\]

## 4. Harmonic escape of the displacement

For a hypothetical positive-integer nonperiodic first-descent survivor, the earlier harmonic theorem gives

\[
\boxed{c_q=O_N(q^{1/9}).}
\]

Therefore

\[
\boxed{
\sum_{i<q}2^{-s_i}=O_N(q^{1/9}).}
\]

This has several immediate consequences.

For every fixed integer `M>=0`,

\[
\boxed{
\#\{i<q:s_i\le M\}
=O_N(2^M q^{1/9}).}
\]

Hence

\[
\boxed{
\frac1q\#\{i<q:s_i\le M\}\to0.}
\]

More generally, for every fixed `theta` with

\[
0<\theta<\frac89,
\]

if `s_i<=theta log_2 q`, then `2^{-s_i}>=q^{-theta}`. Consequently

\[
\boxed{
\#\{i<q:s_i\le\theta\log_2 q\}
=O_N(q^{\theta+1/9}),}
\]

and therefore

\[
\boxed{
\frac1q\#\{i<q:s_i\le\theta\log_2 q\}\to0.}
\]

Thus in event-density one, the R2 path lies logarithmically far to the left of the critical Beatty event positions.

## 5. Renewal-segment endpoint displacement

Consider one renewal segment in R2 containing `H` odd events and `A` accelerated steps. Relative to the segment start define

\[
\boxed{s_H^{(j)}:=\lfloor H\gamma\rfloor-A\ge0.}
\]

The aggregate coefficient surplus is

\[
\varepsilon_j
:=H\gamma-A
=\{H\gamma\}+s_H^{(j)}.
\]

The odd-to-odd aggregate coefficient is

\[
\frac{3^H}{2^A}=2^{\varepsilon_j}.
\]

Because the affine correction is positive, consecutive renewal floors satisfy

\[
\boxed{
\frac{N_{j+1}}{N_j}>2^{\varepsilon_j}.}
\]

Hence if

\[
s_H^{(j)}\ge1,
\]

then `epsilon_j>1` and

\[
\boxed{N_{j+1}>2N_j.}
\]

Therefore every R2 renewal segment that avoids a floor doubling must satisfy

\[
\boxed{s_H^{(j)}=0.}
\]

## 6. Economical R2 renewal segments are Beatty excursions

Rebase the displacement at the beginning of a renewal segment. It always starts at

\[
\boxed{s_0=0.}
\]

Coefficient survival throughout the segment gives

\[
\boxed{s_k\ge0.}
\]

If the segment is economical in the sense `N_{j+1}<=2N_j`, Section 5 gives

\[
\boxed{s_H=0.}
\]

Thus every non-doubling R2 renewal segment is exactly a finite excursion

\[
\boxed{s_0=0,\qquad s_k\ge0,\qquad s_H=0,}
\]

with transition law

\[
\boxed{s_{k+1}-s_k=r_k-v_k,\qquad r_k\in\{1,2\},\quad v_k\ge1.}
\]

Equivalently, its total halving count is the nearest lower critical layer

\[
\boxed{A=\lfloor H\gamma\rfloor.}
\]

Thus the low-cost R2 hard core is not an arbitrary infinite coefficient-survivor path. It is a concatenation of critical Beatty excursions returning to the lower boundary.

## 7. Global displacement across renewal floors

Let `q_j` denote the global odd-event index of a renewal floor. Write the global displacement

\[
s(q):=\lfloor q\gamma\rfloor-A_q.
\]

For one renewal segment of `H=q_{j+1}-q_j` odd events,

\[
\begin{aligned}
s(q_{j+1})-s(q_j)
&=s_H^{(j)}\\
&\quad+
\lfloor(q_j+H)\gamma\rfloor
-\lfloor q_j\gamma\rfloor
-\lfloor H\gamma\rfloor.
\end{aligned}
\]

The last line is the carry of adding the two fractional parts and belongs to `{0,1}`. Therefore

\[
\boxed{s(q_{j+1})\ge s(q_j).}
\]

For an economical segment `s_H^{(j)}=0`, the global renewal-floor displacement either stays fixed or increases by one, solely according to the Beatty carry.

Thus renewal floors form a nondecreasing subsequence of global displacement levels.

## 8. Relation to the critical-density boundary

The coefficient logarithm at odd-event checkpoint `q` is

\[
L_q
:=q\gamma-A_q
=\{q\gamma\}+s_q.
\]

Hence the known critical lower-density necessity for a rational 2-adic noncyclic trajectory is compatible with R2 only if

\[
\boxed{\liminf_{q\to\infty}s_q/q=0.}
\]

This does not contradict the harmonic escape theorem: for example a sublinear but unbounded displacement can have `s_q/q -> 0` while `sum 2^{-s_q}` is small.

Therefore the remaining obstruction is genuinely arithmetic, not merely a density contradiction.

## 9. Current R2 hard core

A hypothetical R2 counterexample must simultaneously support:

1. the one-sided Beatty displacement transition `s_{i+1}-s_i=r_i-v_i`;
2. harmonic mass `sum_{i<q}2^{-s_i}=O_N(q^{1/9})`;
3. critical-density recurrence `liminf s_i/i=0`;
4. infinitely many renewal floors that are state suffix minima and coefficient suffix minima;
5. either infinitely many floor doublings, or an eventual concatenation of 0-to-0 critical Beatty excursions;
6. exact positive-integer 2-adic formation for the entire parity tail.

Items 1--5 admit abstract combinatorial models, so they do not by themselves prove exclusion. The missing ingredient remains the compatibility with one fixed positive ordinary integer under the exact Collatz formation map.

## 10. Next target

The most useful next formulation is an **infinite Beatty-defect mixed-place theorem**.

Let the critical event positions be

\[
A_i^*=\lfloor i\gamma\rfloor
\]

and define the 2-adic critical reference

\[
\Phi_*:=-\sum_{i\ge0}\frac{2^{A_i^*}}{3^{i+1}}.
\]

For an R2 displacement sequence,

\[
N-\Phi_*
=
\sum_{i\ge0}
\frac{2^{A_i^*}-2^{A_i}}{3^{i+1}}
\]

in `Z_2`.

The remaining R2 problem is to show that an admissible displacement with the harmonic/excursion constraints above cannot make the resulting 2-adic value equal one fixed positive ordinary integer while preserving no-first-descent forever. This is the infinite counterpart of the finite first-crossing tri-place defect problem.