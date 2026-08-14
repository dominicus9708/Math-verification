# High-Hensel difference freedom of the hard `H_19` fibre

Date: 2026-08-14

Status: **exact finite full-fibre difference-set theorem + first-defect interpretation**.  This complements the fixed-Hensel dyadic-kernel profile.  It shows that the hard neutral `H_19` fibre can arbitrarily adjust ten consecutive high Hensel digits when embedded at the beginning of the current R1 word, so the valuation of the first early defect is not by itself a terminal 3-adic obstruction.  It does not prove Collatz.

## 1. Fibres

Let

\[
H_{19}=1101101101011011010
\]

with mechanical odd count 12.

Enumerate exactly the two same-state fibres

\[
\mathcal F_0:\quad(\Sigma,M)=(0,0),\ q=12,
\]

\[
\mathcal F_{-1}:\quad(\Sigma,M)=(-1,-1),\ q=11.
\]

Their sizes are

\[
|\mathcal F_0|=2652,
\qquad
|\mathcal F_{-1}|=11433.
\]

For a fibre `F`, define its correction residue set

\[
\mathcal R_J(F)=\{R_w\bmod3^J:w\in F\}
\]

and its correction **difference set**

\[
\boxed{
\mathcal D_J(F)
=
\{R_u-R_v\bmod3^J:u,v\in F\}.
}
\]

## 2. Neutral difference set

Exact enumeration gives

\[
\boxed{
\mathcal D_J(\mathcal F_0)
=
\mathbb Z/3^J\mathbb Z
\qquad(1\le J\le10).
}
\]

At the next depths,

\[
|\mathcal D_{11}(\mathcal F_0)|
=
176807
\]

out of

\[
3^{11}=177147,
\]

so the coverage is

\[
\boxed{0.998080689\ldots.}
\]

At depth 12,

\[
|\mathcal D_{12}(\mathcal F_0)|
=308669
\]

out of

\[
3^{12}=531441.
\]

The important exact statement is the full-group identity through ten ternary digits.

## 3. One-slack difference set

The one-slack fibre is even more flexible:

\[
\boxed{
\mathcal D_J(\mathcal F_{-1})
=
\mathbb Z/3^J\mathbb Z
\qquad(1\le J\le12).
}
\]

At depth 13,

\[
|\mathcal D_{13}(\mathcal F_{-1})|
=1547459
\]

out of

\[
3^{13}=1594323,
\]

for coverage

\[
\boxed{0.970605705\ldots.}
\]

Thus a single 19-bit one-slack hard factor already has full correction-difference freedom through twelve ternary digits.

## 4. Exact valuation ladder

The full difference-set statement is consistent with an explicit exact-valuation ladder.

In the neutral fibre there are pairs with

\[
\boxed{v_3(R_u-R_v)=s
\qquad(s=0,1,\ldots,10).}
\]

Small representative differences include

\[
\begin{array}{c|c}
s&|R_u-R_v|\\\hline
0&2^{11}\\
1&3\cdot2^{10}\\
2&3^2\cdot2^9\\
3&3^3\cdot2^8\\
4&3^4\cdot2^7\\
5&3^5\cdot2^6\\
6&3^6\cdot2^5\\
7&3^7\cdot2^4\\
8&3^8\cdot2^3\\
9&3^9\cdot2^2\\
10&3^{10}\cdot2^2
\end{array}
\]

(up to sign).

In the one-slack fibre, exact valuations exist through

\[
\boxed{s=0,1,\ldots,11,}
\]

with a particularly simple tail

\[
|D_{10}|=3^{10},
\qquad
|D_{11}|=3^{11}.
\]

The `s=11` case is exactly the local ordinary integer-credit channel recorded previously.

## 5. Embedding at the beginning of a long R1 word

Suppose two actual first-block orientations in the neutral fibre are followed by the **same** suffix containing `H-12` odd events.  Concatenation gives

\[
\Delta R_{\rm full}
=
3^{H-12}\Delta R_{19}.
\]

Therefore

\[
\boxed{
v_3(\Delta R_{\rm full})
=(H-12)+v_3(\Delta R_{19}).}
\]

The neutral ladder `s=0,...,10` becomes the high-Hensel valuation window

\[
\boxed{
H-12,H-11,\ldots,H-2.
}
\]

More strongly, because the neutral difference set is the full group modulo `3^10`, after factoring `3^{H-12}` it can realize **every** target on the ten consecutive full-word Hensel positions

\[
\boxed{
H-12,\ldots,H-3.
}
\]

## 6. Relation to the remaining early first-defect channels

The current isolated R1 first-defect theorem leaves only odd ranks

\[
\boxed{r\in\{3,5,7,8,10,12\}.}
\]

The first displaced odd term at rank `r` enters the full correction defect at 3-adic valuation

\[
\boxed{H-r.}
\]

Hence the six valuations are

\[
\boxed{
H-3,\ H-5,\ H-7,\ H-8,\ H-10,\ H-12,
}
\]

and every one lies inside the ten-digit neutral difference window

\[
H-12,\ldots,H-3.
\]

Therefore:

\[
\boxed{
\text{the 3-adic valuation of the first early defect alone cannot be a terminal obstruction.}
}
\]

At the level of the first ten high Hensel digits, the hard neutral `H_19` fibre can reproduce any required correction difference.

## 7. Dyadic asymmetry

This negative 3-adic result does **not** undo the dyadic first-defect theorem.

The first defect term has exact 2-adic valuation equal to its actual parity position `p`, and later defects cannot repair bits below their own positions.  Thus the early first defect remains a permanent intervention in the ordinary-start dyadic address.

We therefore obtain a genuine asymmetry:

\[
\boxed{
\begin{array}{c|c}
\text{dyadic channel}&\text{early first-defect bit is causal/permanent}\\
\text{3-adic correction channel}&\text{same high valuation lies in a locally flexible difference window.}
\end{array}
}
\]

This is precisely why a valid terminal argument must be mixed-place rather than a one-prime valuation obstruction.

## 8. Proof-program consequence

The next useful invariant is not the first-defect 3-adic valuation by itself.  It is the **joint dyadic/Hensel image of the full hard fibre**, conditioned on the already-fixed early ordinary-start address.

The small-block kernel profile and the gate-wide anti-triangular code now point to the same object:

\[
\boxed{
\mathcal G_J
=
\{(\Delta R\bmod3^J,\ \Delta\rho\bmod2^B)
:\text{same survival fibre}\}.
}
\]

The terminal question is whether the required high-Hensel correction and the required ordinary dyadic zero-lift target occur in the **same pair**, not whether either marginal projection is individually possible.