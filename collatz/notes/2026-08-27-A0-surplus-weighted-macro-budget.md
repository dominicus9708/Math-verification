# A0 surplus-weighted macro budget

Date: 2026-08-27

Status: **SAFE WEIGHTED-BUDGET LEMMA + exact certificate.** This combines only repaired unconditional ingredients. It does not prove the Collatz conjecture.

## 1. Inputs

Let

\[
G=2^{33}.
\]

The repaired primitive transition bounds are

\[
\boxed{a_A/G\approx0.50220738937}
\]

for the unrestricted A0 gap-credit ceiling and

\[
\boxed{a_J/G\approx2.52702129476}
\]

for the primitive J0 gap-debit floor.

For an A0 block whose tenth-J0 checkpoint surplus is

\[
s=1+r,
\qquad r\ge0,
\]

the packed-suffix envelope gives a normalized correction loss

\[
L(r),
\]

with the safe lower bound, for `r>=1`,

\[
\boxed{
L(r)>
\frac16\left(
 r+\left\lfloor\frac{200(r-1)}{117}\right\rfloor
\right)-\frac12.
}
\]

Hence one such A0 block has gap credit at most

\[
\boxed{
a_A-C_A L(r),
\qquad C_A=3^{Q_0}/2^{A_0}<1.
}
\]

## 2. Weighted macro inequality

Consider a macro consisting of `k` consecutive A0 first crossings followed by one primitive J0 first crossing.

Let the checkpoint surplus parameters of the A0 blocks be

\[
r_1,\ldots,r_k.
\]

Then the total gap change satisfies

\[
\boxed{
\Delta d
<
ka_A
-C_A\sum_{i=1}^kL(r_i)
-a_J.
}
\]

Therefore the deterministic sufficient condition for strict macro contraction is

\[
\boxed{
C_A\sum_{i=1}^kL(r_i)
>
ka_A-a_J.
}
\]

This replaces the earlier unweighted statement `5 a_A<a_J` by a surplus-sensitive criterion.

## 3. Immediate consequence

For

\[
k\le5,
\]

no surplus information is needed:

\[
\boxed{ka_A<a_J.}
\]

Thus every `A0^k J0` macro with `k<=5` is gap-negative.

For longer runs, a sufficiently large transported surplus makes the A0 blocks cheaper in additive budget and restores contraction.

## 4. Exact uniform-surplus thresholds

Suppose every one of the `k` A0 blocks has

\[
r_i\ge r_*.
\]

The exact certificate finds the smallest `r_*` guaranteed by the packed-suffix lower bound for which one following primitive J0 debit dominates all `k` A0 credits:

\[
\begin{array}{c|c}
k&r_*\\
\hline
6&1,541,530,042\\
7&2,686,060,404\\
8&3,544,458,175\\
9&4,212,100,886\\
10&4,746,215,055\\
11&5,183,217,557\\
12&5,547,386,309\\
13&5,855,529,099\\
14&6,119,651,490
\end{array}
\]

These are exact integer thresholds for the current certified inequalities, not numerical guesses.

At each listed threshold,

\[
\boxed{
k\bigl(a_A-C_A L(r_*)\bigr)<a_J,}
\]

while lowering `r_*` by one fails the same certified inequality.

## 5. Limit of the present tax

The coefficient-wise maximum is

\[
r\le P-1=6,189,245,290.
\]

Even at this maximal surplus, the current packed-suffix tax alone does **not** certify

\[
15\times\text{A0 credit}<a_J.
\]

Thus the present weighted budget closes a large region but does not make arbitrarily long A0 runs automatically contract when a single J0 eventually occurs.

This boundary is important for the structural audit: the calculation must not be extrapolated past `k=14` as though the tax proved uniform long-run contraction.

## 6. DSD branch refinement

The A0-dominant branch now splits naturally by two coordinates:

\[
\boxed{
(\text{run length }k,
\text{ accumulated surplus tax }\Sigma L).
}
\]

The transition rule is

\[
\boxed{
\text{A0 return}
\to
+a_A\text{ possible credit}
-C_A L(r)\text{ structural tax},
}
\]

followed, when J0 is actually used, by

\[
\boxed{-a_J.}
\]

This produces a deterministic weighted transition system.

## 7. What has been pruned

The difficult A0-dominant language is no longer all long A0 runs.

A long run followed by J0 is already harmless whenever its surplus-tax sum is large enough.

Therefore any surviving dangerous run must be biased toward **low-surplus A0 blocks**, especially the near-mechanical class

\[
\boxed{s=1\quad(r=0).}
\]

This is a substantial DSD reduction:

\[
\boxed{
\text{arbitrary A0-dominant run}
\to
\text{low-surplus dominated run}
\quad\text{or}\quad
\text{already gap-negative macro}.
}
\]

## 8. Structural audit

### SAFE

- weighted macro inequality;
- `k<=5` unconditional A0^k-J0 contraction;
- exact uniform-surplus thresholds for `k=6,...,14`;
- failure of the current tax alone to close `k=15` even at maximal surplus.

### NOT USED

- ternary Cantor selector entry;
- Ansari recursive-sufficiency induction;
- repeated local Hensel pullback.

### OPEN

The new hard branch is:

> repeated A0 first crossings with anomalously small checkpoint surplus, especially repeated `s=1`, while activated J0 gates continue to be skipped.

This is now a much smaller structural target than unrestricted A0 repetition.

## 9. Next Gate

For `s=1`, the tenth-J0 checkpoint matches the exact mechanical odd count.  The next audit should determine how much freedom remains in the **address/residue structure** of an A0 first-crossing word with this minimal surplus.

The natural question is whether repeated low-surplus returns force either:

1. a near-mechanical/Hensel address recurrence that can be audited globally;
2. activation of a lower J0-type crossing;
3. or entry into the already isolated later/infinite coefficient-survivor branch.

Companion certificate:

`collatz/src/A0_surplus_weighted_macro_budget_certificate.py`
