# Predecessor-credit / periodic-lift handoff at a Euclidean macroblock

Date: 2026-08-13  
Correction: 2026-08-14

Status: **exact local valuation dichotomy and exact type-17 witness; corrected global interpretation**.  The local identity `148 -> 440/3` is valid for one selected alternate-pair relation.  It is **not** a proof that the whole integer-credit frontier, or every candidate branch, is forced into the rational channel at that point.  The former greedy-max interpretation has been superseded by `2026-08-14-credit-frontier-correction-and-hensel-sibling-max.md`.  This note does not prove Collatz.

## 1. Cross-block correction difference

Let a left macroblock `U` have length `L_U` and odd count `q_U`.  Let a right alternate-pair relation have correction difference

\[
D_V=3^{q_V}\delta.
\]

For two left orientations with correction difference `D_U`, concatenation gives

\[
\boxed{
D
=3^{q_V}
\left(D_U+2^{L_U}\delta\right).
}
\]

Put

\[
X=D_U+2^{L_U}\delta.
\]

If

\[
s=v_3(X)\ge q_U,
\]

then the full displacement is the ordinary integer credit

\[
\boxed{
\Delta=X/3^{q_U}.
}
\]

If instead `s<q_U`, the reduced displacement is

\[
\boxed{
\frac{X/3^s}{3^{q_U-s}}.
}
\]

Thus one selected relation has the exact alternative

\[
\boxed{
\text{integer credit}
\quad\text{or}\quad
\text{nonintegral odd-}3\text{-power denominator}.
}
\]

## 2. Exact type-17 local witness

For the length-19 factor

\[
\boxed{1101101011011010110}
\]

we have

\[
L_U=19,
\qquad q_U=12.
\]

For the particular incoming relation

\[
\delta=148,
\]

no tested neutral-orientation pair realizes full divisibility by `3^12`.  The maximum available 3-adic valuation is exactly

\[
\boxed{s=11.}
\]

One exact positive numerator is

\[
D_U+2^{19}\cdot148
=77,944,680
=440\cdot3^{11}.
\]

Hence this selected relation becomes

\[
\boxed{440/3.}
\]

For denominator `3`, the associated rational-grid high-resolution binary coordinate has period two and one nonzero lift bit per two positions, by the separate rational-grid label theorem.

## 3. Correction to the old finite diagnostic

The earlier calculation retained only the **largest** available integer credit at each block.  In that greedy quotient, many diagnosed phase branches reached `148` and the selected maximum relation then handed off to `440/3` at type 17.

This must not be read as a forced candidate transition.

When **all** available integer relations are retained, smaller integer credits can survive the same type-17 context even though the greedy maximum `148` does not.  Therefore:

\[
\boxed{
148\to440/3
\text{ is a local relation handoff, not a global frontier handoff.}
}
\]

The correct state is set-valued and candidate survival is a coverage-avoidance problem, not a scalar-credit growth problem.

## 4. Stronger denominator absorption theorem

The 2026-08-14 correction note proves a stronger statement for a relation which is **already nonintegral**.  If

\[
\delta=a/3^d,
\qquad d>0,
\qquad3\nmid a,
\]

then prepending any integer correction block gives denominator exponent

\[
\boxed{d'=d+q_U.}
\]

Hence a relation that has entered the rational channel cannot later recover an integer displacement by further left concatenation.

This makes the rational channel absorbing for the specific objective of producing an ordinary predecessor at a still earlier original start.  It does **not** imply that every simultaneously available integer relation has disappeared.

## 5. Current role

This local witness remains useful as an exact bridge between correction congruence and periodic late-lift structure, but it is no longer treated as a well-founded progress theorem.

The active proof target is now the max-plus/Hensel coverage system described in the 2026-08-14 correction note:

\[
\boxed{
(\text{return phase},\Sigma,M,
\text{3-adic sibling maxima},
\text{dyadic canonical prefix},
\text{headroom/excess}).
}
\]

Git history retains the superseded greedy interpretation for auditability.
