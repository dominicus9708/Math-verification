# Neutral-delay / expansion log-budget closure for finite selector layers

Date: 2026-09-06

## Status

- **SAFE CONDITIONAL LEMMA:** exact logarithmic budget sufficient for atom-floor extinction of a finite `F_m` selector layer.
- **FINITE DIAGNOSTIC:** direct enumeration of `F_m`, `m<=22`, shows that total neutral occupancy can exceed the longest single neutral run, so a single-run theorem is not by itself the right terminal quantity.
- **OPEN:** prove a horizon-uniform neutral/expanding budget for the actual candidate language.

No Collatz proof is claimed.

---

## 1. Finite selector atom floor

The recursively sufficient selector layer `F_m` contains exactly

\[
2^m
\]

integer atoms.

Use an absolute nonnegative weighted survivor total `W_j` normalized so that initially

\[
W_0\le2^m.
\]

If

\[
W_J<1,
\]

then no selector atom survives, because every surviving atom has positive weight at least one in the coefficient-surviving region.

This is the same integer/atom-floor closure already audited in Gate C2.

---

## 2. Three block types

Partition a chosen block decomposition of the forward candidate process into:

1. **good/contracting blocks**, each with
   \[
   R_j:=W_{j+1}/W_j\le\rho<1;
   \]
2. **neutral blocks**, each with
   \[
   R_j\le1;
   \]
3. **expanding exceptional blocks**, each with the universal Beatty macro-pair bound
   \[
   R_j\le B_*:=\frac94.
   \]

Let `G`, `N`, `B` be their respective counts through the chosen horizon.

Then

\[
W_J
\le
2^m\rho^G B_*^B.
\]

Neutral blocks do not appear in the multiplicative upper bound; they only consume horizon without paying contraction.

---

## 3. Exact logarithmic closure criterion

A sufficient condition for `W_J<1` is

\[
2^m\rho^G\left(\frac94\right)^B<1.
\]

Taking logarithms gives

\[
\boxed{
G(-\log\rho)
-
B\log\frac94
>
m\log2.
}
\]

This is the exact finite-layer log budget.

Status: **SAFE CONDITIONAL LEMMA**.

Several useful special cases follow immediately.

### No expanding blocks after tail control

If the high-surplus tail-budget theorem has already absorbed every non-neutral block into one uniform factor `lambda<1`, then `B=0` and it is enough that

\[
\boxed{
G>
\frac{m\log2}{-\log\lambda}.
}
\]

Thus any theorem saying that only `O(m)` blocks are neutral before `c m` contracting blocks occur closes the finite selector layer.

### Linear exceptional budget

If

\[
B\le a m,
\qquad
G\ge c m,
\]

then extinction follows whenever

\[
\boxed{
c(-\log\rho)>
\log2+a\log\frac94.}
\]

Hence neither neutral delay nor a linear number of bounded expanding exceptions is fatal by itself.  What matters is the signed logarithmic budget.

---

## 4. Why a single neutral-run bound is insufficient

A trajectory can enter and leave `d=2` repeatedly.  Therefore

> every individual neutral run has length at most `A m`

does not by itself control the total neutral time over a long horizon.

The right quantity is cumulative occupancy or, more generally, the number of blocks that fail to pay a negative logarithmic drift.

A useful theorem form is therefore

\[
\boxed{
N(H)+B(H)
\le
\theta H+A m,
\qquad \theta<1,
}
\]

combined with a contracting estimate on the complementary blocks.

For sufficiently large linear horizon `H=Cm`, this supplies `G=Theta(m)` and can satisfy the atom-floor log budget.

---

## 5. Exact finite diagnostic on `F_m`, `m<=22`

A direct exact scan of all starts in each `F_m`, through their coefficient-surviving prefix, counts a step as neutral when

\[
d_k=2,
\qquad
e_k=\delta_k.
\]

Representative maxima of the **total** number of neutral steps on one trajectory are:

\[
\begin{array}{c|rrrrrrrr}
m&15&16&17&18&19&20&21&22\\\hline
\max N_{\rm neutral}
&42&36&35&35&44&62&52&43.
\end{array}
\]

The corresponding longest single runs can be smaller.  For example the previously audited longest run at `m=20` is 19 steps, while one trajectory accumulates 62 neutral steps in total before coefficient crossing.

Therefore the finite data directly reject the simplification

\[
\text{total neutral budget}
\approx
\text{longest neutral run}.
\]

Status: **FINITE DIAGNOSTIC ONLY**.

No asymptotic bound is inferred from these values.

---

## 6. Revised terminal target

The neutral exceptional channel should now be attacked in one of two forms.

### Occupancy form

Prove constants `theta<1`, `A<infinity` such that for every actual candidate layer and all relevant horizons,

\[
N(H)\le\theta H+A m.
\]

### Direct log-budget form

Avoid separate classification and prove directly

\[
\boxed{
\sum_{j<J}-\log R_j
>
m\log2
}
\]

at some finite horizon `J=O(m)` for every finite selector layer.

The second form is closest to what atom-floor closure actually needs and allows rare expanding and neutral episodes as long as the cumulative drift wins.

---

## 7. DSD interpretation

This replaces an unnecessarily strong pathwise demand

> every exceptional path is killed quickly

with the weaker exact requirement

> the finite selector layer accumulates enough negative logarithmic budget before its atom floor is reached.

This is consistent with all current finite diagnostics:

- some high-surplus `d` strata expand;
- a formal neutral `d=2` Sturmian channel exists;
- the root-aligned neutral channel disappears inside `F_44` at depth 47;
- later neutral re-entry occurs in smaller exact `F_m` scans;
- nevertheless finite-layer extinction only requires the aggregate log budget, not uniform pathwise contraction.
