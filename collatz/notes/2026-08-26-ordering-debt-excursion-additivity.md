# Ordering-debt excursion additivity for first-resonance Bellman blocks

Date: 2026-08-26

Status: **exact lower-bound theorem** inside the repaired first-resonance branch.  It is a Bellman-state compression lemma, not a Collatz proof.

## 1. Backward displacement process

Read the odd ordinals backward from the endpoint toward the start.  Let `p_m` be the displacement of the current earliest reconstructed odd ordinal from its mechanical position.

For the next prepended ordinal, with mechanical gap `g_m in {1,2}`, ordering gives

\[
\boxed{p_{m+1}\ge p_m-g_m+1.}
\]

The start boundary has displacement zero because the first odd event occurs at time zero and its mechanical position is also zero.

## 2. Debt excursions

A **debt excursion** is a maximal consecutive interval on which

\[
p_m>0.
\]

Different excursions are disjoint and are separated by states with `p=0`.

For excursion `e`, write

\[
D_e=\max p_m
\]

on that interval.

Choose an occurrence of this maximum and follow the excursion toward the start boundary until it returns to zero.  Since a gap-1 cannot decrease displacement and a gap-2 decreases it by at most one, this tail of the excursion must contain at least `D_e` gap-2 symbols.

The anchored Christoffel balance therefore forces at least

\[
\boxed{
h(D_e)=
\left\lfloor\frac{(D_e-1)Q}{P}\right\rfloor+1}
\]

positive-displacement positions from the selected maximum through repayment.

## 3. Additive correction reserve

At displacement `r>=1`, normalized correction loss is

\[
2c_j(1-2^{-r}),
\qquad c_j>1/12.
\]

The cheapest possible repayment tail must still contain the positive levels

\[
D_e,D_e-1,\ldots,1
\]

at least once each.  All extra positive positions cost at least the `r=1` amount.

Hence excursion `e` alone contributes strictly more than

\[
\boxed{
F(D_e):=
\frac{h(D_e)+D_e-2+2^{1-D_e}}{12}.}
\]

Because debt excursions are disjoint, their lower bounds add:

\[
\boxed{
\frac{E}{3^Q}
>
\sum_e F(D_e).}
\]

This is stronger than applying the displacement-cap theorem only to the single global maximum.

## 4. Bellman-state consequence

For block composition, an excursion entirely contained inside a block no longer needs its full displacement history to survive as an interface variable.  Once the excursion has returned to `p=0`, it can be replaced by its certified scalar reserve charge `F(D_e)` (or by any sharper exact cost already accumulated).

Only an excursion that crosses a block boundary needs to carry ordering memory into the next block.  Thus the exact interface can be organized as

\[
\boxed{
(\text{Hensel quotient/alignment state},\ p,\ \text{accumulated cost}),}
\]

where `p=0` marks a renewal boundary and all closed positive-debt components have already been charged.

This matches the 21-run Stern-Brocot macro grammar: internal excursions can be eliminated locally before two macro operators are composed, while an open excursion is represented by one nonnegative integer debt variable.

## 5. DSD interpretation

The DSD bookkeeping distinction is:

\[
\text{local path detail}
\supset
\text{closed excursion summary}
\supset
\text{boundary-relevant state}.
\]

Discarding the internal path is legitimate only after its unavoidable cost has been transferred into the scalar Bellman value.  This preserves the proof-relevant information while reducing the description dimension.

The companion numerical displacement cap is certified by

`collatz/src/first_resonance_ordering_debt_budget_certificate.py`.
