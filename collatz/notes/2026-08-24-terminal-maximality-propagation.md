# Terminal whole-prefix maximality propagates to every earlier prefix

Date: 2026-08-24

Status: **exact algebraic reduction for the unconditional whole-prefix line.**  In the current m=45 branch it collapses the 126-horizon deterministic strip 74<=H<=200 to one terminal H=200 maximality condition.  This is not a proof of the Collatz conjecture.

## 1. Affine concatenation identity

Let a binary prefix `w` have length h, q odd entries and correction R_w:

\[
T^h(N)=\frac{3^qN+R_w}{2^h}.
\]

Let a common suffix `s` have length ell, r odd entries and local correction C_s:

\[
T^\ell(x)=\frac{3^r x+C_s}{2^\ell}.
\]

Composing the two affine maps gives

\[
T^{h+\ell}(N)
=\frac{3^{q+r}N+3^rR_w+2^hC_s}{2^{h+\ell}}.
\]

Hence the concatenated correction is

\[
\boxed{R_{ws}=3^rR_w+2^hC_s.}
\]

## 2. A complete-prefix predecessor survives every common suffix

Suppose another length-h word `u` has the same odd count q and lies in the same complete Hensel class, with

\[
R_u-R_w=3^q d,
\qquad d>0.
\]

Append exactly the same suffix `s` to both words.  Then

\[
\begin{aligned}
R_{us}-R_{ws}
&=3^r(R_u-R_w)\\
&=3^{q+r}d.
\end{aligned}
\]

Therefore `us` and `ws` remain in the same complete Hensel class at the longer horizon, and crucially the root credit is still exactly d:

\[
\boxed{d_{h+\ell}=d_h.}
\]

If `M=N-d`, then both constructions reach the same endpoint after h steps and, after appending the common suffix, after h+ell steps as well.

## 3. Terminal maximality theorem

Let the actual parity prefix of a candidate N be defined through a terminal horizon H.  If the complete H-prefix is maximum-correction in its same-(q,R mod 3^q) class, then every earlier actual prefix h<=H is also maximum-correction in its corresponding complete class.

Indeed, if an earlier prefix were non-maximal, the larger sibling at h could be concatenated with the actual suffix from h to H.  Section 2 would then produce a larger correction in the same terminal Hensel class, contradicting terminal maximality.

Thus

\[
\boxed{
\text{terminal whole-prefix maximality at H}
\Longrightarrow
\text{whole-prefix maximality at every h<=H}.
}
\]

This implication is purely algebraic.  It does not use repeated local L7/L14 maximality and is unaffected by the pullback defect found in that older route.

## 4. Consequence for the current m=45 deterministic strip

The current two-affine-block recursively sufficient family is

\[
N=4\left(3^{45}+b3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i,b\in\{0,1\},
\]

and satisfies

\[
2^{73}<N<2^{74}.
\]

The separate root-credit range theorem proves that every positive same-q complete-prefix credit is below N for every H<=200.  Therefore a hypothetical minimal counterexample in the m=45 core that coefficient-survives to depth 200 must satisfy terminal whole-prefix maximality at H=200.

By the theorem above, that **single terminal condition automatically contains all earlier whole-prefix maximality conditions**, including the entire interval

\[
74\le h\le200.
\]

So the previously described 126-step deterministic strip is not a conjunction of 126 independent maximality filters.  It reduces to one terminal intersection:

\[
\boxed{
\mathcal C_{45}
\cap
\mathcal S_{200}
\cap
\mathcal M_{200},
}
\]

where

- `C_45` is the fixed m=45 ternary selector family,
- `S_200` is coefficient survival through depth 200,
- `M_200` is terminal complete-Hensel maximum status.

The binary address is already fully determined by the integer by depth 74; no new selector freedom appears in the remaining 126 steps.

## 5. What remains after this reduction

The finite m=45 problem is therefore sharper than the earlier wording suggested.  The next target is not to propagate maximality one horizon at a time, but to bound or compute the single same-integer terminal intersection

\[
\boxed{\mathcal C_{45}\cap\mathcal S_{200}\cap\mathcal M_{200}.}
\]

If this set is empty, the current m=45 core is extinct through the entire root-credit-safe range.  If it is nonempty, the surviving terminal states become the only states that need to be transferred beyond H=200 or into the globalization argument.

Regression certificate:

`collatz/src/whole_prefix_terminal_maximality_propagation_certificate.py`.
