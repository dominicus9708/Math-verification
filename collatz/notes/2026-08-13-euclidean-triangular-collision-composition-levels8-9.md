# Euclidean triangular correction-collision composition and level-8/9 credits

Date: 2026-08-13

Status: **exact composition lemma + exact finite witnesses at lengths 46 and 65**.  This extends the fixed one-slack predecessor-credit sequence without flat enumeration of the length-46 or length-65 binary words.  It is not an asymptotic theorem and does not prove Collatz.

## 1. Concatenation setup

Let a deterministic macroblock be a concatenation

\[
V=AB,
\]

with `|A|=L_A`.  Consider two actual orientations

\[
w_h=A_hB_h,
\qquad
w_l=A_lB_l
\]

having the same total odd count `q`.  Write

\[
q_{B,h}=r+t,
\qquad
q_{B,l}=r,
\qquad t\ge0.
\]

Their corrections satisfy

\[
R(w)=3^{q_B}R(A)+2^{L_A}R(B).
\]

Hence

\[
C:=R(w_h)-R(w_l)
=3^r\bigl(3^tR(A_h)-R(A_l)\bigr)
+2^{L_A}\bigl(R(B_h)-R(B_l)\bigr).
\]

## 2. Triangular 3-adic composition lemma

If

\[
3^q\mid C,
\]

then necessarily

\[
\boxed{R(B_h)\equiv R(B_l)\pmod{3^r}},
\]

because the prefix contribution is already divisible by `3^r` and `2^L_A` is a 3-adic unit.

Define

\[
\boxed{
D_B:=\frac{R(B_h)-R(B_l)}{3^r}.
}
\]

Then

\[
C
=3^r\left[
3^tR(A_h)-R(A_l)+2^{L_A}D_B
\right].
\]

Therefore

\[
\boxed{
3^q\mid C
\iff
3^{q-r}\mid
\left(3^tR(A_h)-R(A_l)+2^{L_A}D_B\right).
}
\]

When the bracket is positive, the exact integer predecessor credit is

\[
\boxed{
\Delta
=
\frac{C}{3^q}
=
\frac{
3^tR(A_h)-R(A_l)+2^{L_A}D_B
}{3^{q-r}}.
}
\]

Thus the full `3^q` collision is solved hierarchically: first a suffix congruence modulo `3^r`, then one quotient, then a smaller prefix congruence modulo `3^(q-r)`.

This is the correction-residue analogue of 3-adic carry propagation and is the exact recursion needed for Euclidean macroblock composition.

## 3. Level 8: length 46

Use

\[
U_8=U_7U_6,
\]

where

\[
|U_7|=27,\quad Q_7=17,
\qquad
|U_6|=19,\quad Q_6=12.
\]

Hence

\[
\boxed{|U_8|=46,\qquad Q_8=29.}
\]

The one-slack fibre has total state

\[
(\Sigma,M)=(-1,-1)
\]

and actual odd count

\[
q=28.
\]

Choose the high-correction decomposition

\[
U_7:(-1,-1),\ q=16,
\qquad
U_6:(0,0),\ q=12,
\]

and the low-correction decomposition

\[
U_7:(+2,0),\ q=19,
\qquad
U_6:(-3,-3),\ q=9.
\]

Both concatenate to `(-1,-1)` with total odd count 28.

The exact witness corrections are

\[
R_{A,h}=911182372,
\qquad
R_{A,l}=1907948251,
\]

\[
R_{B,h}=2812783,
\qquad
R_{B,l}=175261.
\]

The suffix difference gives

\[
\boxed{
D_B
=\frac{2812783-175261}{3^9}
=134.
}
\]

The reduced prefix bracket is

\[
27R_{A,h}-R_{A,l}+2^{27}D_B
=40679151345
=35\cdot3^{19}.
\]

Therefore the full length-46 corrections obey

\[
\boxed{
R_h-R_l=35\cdot3^{28}.
}
\]

The two complete words both have state `(-1,-1)` and 28 ones.  Consequently, if the low-correction orientation occurs at a block start `x`, the high-correction orientation starting at

\[
\boxed{x-35}
\]

reaches the same block endpoint.  A minimal-counterexample orbit therefore requires

\[
\boxed{x-N\ge35}
\]

at such an occurrence.

Thus the fixed one-slack credit sequence extends from 19 to

\[
\boxed{35}
\]

at length 46.

## 4. Level 9: length 65 by nested quotient recursion

The next semiconvergent representative is

\[
U_9=U_8U_6=U_7U_6U_6,
\]

so

\[
\boxed{|U_9|=65,\qquad Q_9=41,\qquad q=40}
\]

in the one-slack fibre.

Instead of enumerating length-65 words, apply the triangular lemma twice.

For the final `U6` pair,

\[
\boxed{
D_B
=\frac{2590063-70639}{3^9}
=128.
}
\]

For the preceding neutral `U6` pair,

\[
27(2689199)-1542577+2^{19}(128)
=260\cdot3^{12},
\]

so the first nested quotient is

\[
\boxed{D_C=260.}
\]

The remaining `U7` congruence is

\[
27(822178580)-2469141991+2^{27}(260)
=47\cdot3^{19}.
\]

Hence the full length-65 corrections satisfy

\[
\boxed{
R_h-R_l=47\cdot3^{40}.
}
\]

Both complete orientations again have

\[
(\Sigma,M)=(-1,-1),
\qquad q=40.
\]

Thus the predecessor headroom credit is

\[
\boxed{\Delta=47.}
\]

No length-65 word enumeration is used in the certificate; only the fixed lower-level correction data and two successive 3-adic quotient equations are needed.

## 5. Updated finite credit sequence

The currently exact lower bounds for the maximum predecessor credit in the fixed one-slack fibre are

\[
\boxed{
1,2,3,5,11,19,35,47
}
\]

at macroblock lengths

\[
\boxed{
3,5,8,11,19,27,46,65.
}
\]

The last two values are obtained by triangular Euclidean composition rather than flat word enumeration.

No monotonicity or asymptotic growth theorem is inferred from these eight values.

## 6. Structural consequence

The relevant recursive state is not the entire correction integer.  A block only needs to expose, level by level,

\[
\boxed{
(\Sigma,M,q,\;R\bmod3^r,\;D)
}
\]

where `D` is the quotient created after a suffix congruence has been discharged.

Each Euclidean concatenation replaces one huge congruence modulo `3^q` with a small 3-adic carry step and a lower-dimensional congruence.  This is directly compatible with the state-multiplicity monoid

\[
(\Sigma,M,\text{multiplicity})
\]

already established for coefficient survival.

The next theorem target is to replace witness search by a coverage/growth recursion for these quotient states: show that a positive or increasing fraction of the one-slack fibre receives predecessor credits whose size grows without bound along the continued-fraction hierarchy.

That statement, combined with the aperiodic R2 headroom bounds at critical returns, would be proof-relevant.  The present note establishes the exact recursive arithmetic needed for such a theorem but does not establish the asymptotic coverage or growth claim.

## 7. Verification

`collatz/src/euclidean_triangular_credit_levels8_9_certificate.py` checks with exact Python integers:

- both macroblock lengths and odd counts;
- both complete relative states `(-1,-1)`;
- the level-8 suffix quotient `D_B=134`;
- the level-8 reduced credit `35`;
- the level-9 suffix quotient `D_B=128`;
- the nested quotient `D_C=260`;
- the final reduced credit `47`;
- the full identities `R_h-R_l=35*3^28` and `47*3^40`.
