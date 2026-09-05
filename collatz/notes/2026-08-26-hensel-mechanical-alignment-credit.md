# Mechanical-alignment credit for the two-boundary Hensel control problem

Date: 2026-08-26

Status: **exact structural theorem** inside the repaired binary/Hensel proof line.  This is not a proof of the Collatz conjecture.  It identifies an amortizable state variable for the remaining two-boundary min-plus problem.

## 1. Zero-control future alignment class

Fix a future mechanical exponent block

\[
e_0,e_1,\ldots,e_{L-1}.
\]

A zero-displacement Hensel run satisfies

\[
K_{i+1}=\frac{K_i+2^{e_i}}{3}.
\]

Equivalently,

\[
K_i=3K_{i+1}-2^{e_i}.
\]

Unrolling gives

\[
K_0
=3^LK_L-
\sum_{i=0}^{L-1}3^i2^{e_i}.
\]

Therefore the current carry is forced modulo `3^L`:

\[
\boxed{
Z_L(e_0,\ldots,e_{L-1})
:=-\sum_{i=0}^{L-1}3^i2^{e_i}
\pmod{3^L}.
}
\]

Conversely, if

\[
K_0\equiv Z_L\pmod{3^L},
\]
then all `L` zero-displacement divisions are valid.  At every preterminal level the corresponding nested alignment class is congruent to `-2^{e_i}` modulo three and is therefore a unit.

Thus:

\[
\boxed{
\text{A fixed length-L mechanical zero run has exactly one admissible current carry class modulo }3^L.
}
\]

This is the exact boundary information that was lost in the earlier local zero-cost audit.

## 2. Alignment depth

For the mechanical future beginning at stage `m`, define the alignment depth

\[
\mathfrak a_m(K)
:=
\max\{L:\ K\equiv Z_{m,L}\pmod{3^L}\}.
\]

If `a:=mathfrak a_m(K)>=1`, the mechanical action `d=0` is legal.  Let

\[
K'=(K+2^{e_m})/3.
\]

The nested alignment classes satisfy

\[
Z_{m,L}=3Z_{m+1,L-1}-2^{e_m}.
\]

Hence

\[
K'-Z_{m+1,L-1}
=\frac{K-Z_{m,L}}3.
\]

So, unless the finite remaining horizon itself truncates first,

\[
\boxed{
\mathfrak a_{m+1}(K')=\mathfrak a_m(K)-1.
}
\]

A zero-cost mechanical step therefore consumes exactly **one ternary digit of alignment credit**.

This explains why arbitrary finite zero-cost blocks can exist: they begin with a boundary carry containing exactly the required number of stored alignment digits.

## 3. Repair from exhausted alignment

Suppose the current alignment depth is zero, so `d=0` is not a valid Hensel lift.  Let `e` be the current mechanical exponent.  Compare an actual repair displacement `d>0` with the ideal mechanical term.

The repair contribution before division by three is

\[
R_e(d)
:=2^{e-d}-2^e
=2^e(2^{-d}-1).
\]

When `d` is odd, this is a 3-adic unit.  To seed at least `L` zero-control alignment digits in the next state, `d` must solve one congruence modulo `3^{L+1}`:

\[
\boxed{
R_e(d)\equiv T\pmod{3^{L+1}},
}
\]
where `T` is determined by the current carry and the future mechanical alignment class.

The relevant map has a particularly rigid form.

## 4. Odd-repair bijection theorem

Restrict `d` to odd residue classes modulo

\[
2\cdot3^L.
\]

For two odd classes `d_1,d_2`,

\[
R_e(d_1)-R_e(d_2)
=2^e(2^{-d_1}-2^{-d_2}).
\]

Since `d_1-d_2` is even, LTE gives

\[
v_3\bigl(R_e(d_1)-R_e(d_2)\bigr)
=1+v_3(d_1-d_2).
\]

Consequently, if

\[
R_e(d_1)\equiv R_e(d_2)\pmod{3^{L+1}},
\]
then

\[
v_3(d_1-d_2)\ge L.
\]

Because the difference is even, this means

\[
d_1\equiv d_2\pmod{2\cdot3^L}.
\]

So the map is injective on `3^L` odd classes.

All odd `d` have the same nonzero image class modulo three, determined by `e`, and that target unit coset modulo `3^(L+1)` also has exactly `3^L` members.  Therefore

\[
\boxed{
 d\pmod{2\cdot3^L}
\longmapsto
R_e(d)\pmod{3^{L+1}}
}
\]
is a bijection from odd displacement classes onto one unit coset.

Hence, once the mod-3 Hensel parity condition says that an odd repair is required, a target of `L` future mechanical alignment digits determines

\[
\boxed{
\text{exactly one repair class }d\pmod{2\cdot3^L}.
}
\]

## 5. What this does and does not prove

This theorem does **not** by itself lower-bound the repair cost uniformly in `L`.  The unique class modulo `2*3^L` can occasionally have a small positive representative.

Therefore the tempting inference

\[
\text{long zero run}\Rightarrow\text{large immediate displacement}
\]

is not valid uniformly.

However the theorem adds the missing arithmetic rigidity:

- zero-control continuation consumes one stored ternary alignment digit per step;
- when alignment is exhausted, buying `L` new digits is not a free choice but one exact displacement class modulo `2*3^L`;
- the ordering state remembers the actual representative `d`, so a large repair cannot be discarded after one step;
- the start and endpoint boundaries determine which exceptional small representatives can actually occur.

Thus the remaining problem is naturally an **amortized two-boundary control problem**, not a local entropy or sign-correlation problem.

## 6. Relation to the relative discrete-log isometry

The previous theorem showed that the live Hensel control branches are ternary-tree isometries.  The present theorem identifies a distinguished ray/class in that tree: the unique future mechanical zero-control alignment class.

The combined picture is

\[
\boxed{
\text{carry tree state}
\to
\begin{cases}
\text{consume one alignment trit with }d=0,\\
\text{repair through one unique }d\bmod2\cdot3^L\text{ class}
\end{cases}
\to
\text{ordering/cost memory}.
}
\]

This is the most compact exact formulation obtained so far for the Hensel side of the first-resonance two-boundary Bellman problem.

## 7. Next proof target

The useful next lemma is an amortized repair bound.  A candidate form is:

> Between the fixed endpoint boundary and fixed start boundary, the total actual correction cost required to repeatedly replenish mechanical alignment credit exceeds the first-resonance defect budget.

A proof must account for exceptional small representatives of the unique repair classes and for the one-sided displacement ordering

\[
d_{m+1}\ge d_m-g_m+1,
\qquad g_m\in\{1,2\}.
\]

The 138-node anchored Christoffel DAG supplies the exact future mechanical gap blocks; the tree-isometry and repair-bijection theorems supply the Hensel interface.

Companion regression certificate:

`collatz/src/hensel_mechanical_alignment_credit_certificate.py`.
