# MATH-189 — shared Sigma, correction coordinate, and Hensel/address bridge

Date: 2026-09-18

Status: `EXACT STATE-IDENTIFICATION LEMMA / HENSEL-ADDRESS BRIDGE / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-188 retained the analytic coordinate `Sigma` and a separate MATH-051 Hensel witness channel because the two constructions arose from different descriptions.

They are not independent at the mathematical level. The normalized correction signature used by MATH-051 is exactly the same `Sigma` used by MATH-072/187/188.

This note identifies the common coordinate and then replaces it by the integer correction `C`, which simultaneously determines the analytic correction, the Hensel class, and the canonical dyadic start address.

No new paid layer, first cell, or Collatz claim is made.

## 2. Equality of the two Sigma coordinates

Fix a length-`k` parity word with

\[
q=\#\{\text{odd steps}\},\qquad d=k-q,
\]

and even positions

\[
E=(e_0<e_1<\cdots<e_{d-1}).
\]

MATH-051 defines

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}3^j\left(\frac23\right)^{e_j}.
}
\]

Its exact correction identity is

\[
\frac{C(E)}{3^{k-d}}
=1+\Sigma_d(E)-3^d\left(\frac23\right)^k.
\]

Since `q=k-d`,

\[
3^d\left(\frac23\right)^k
=\frac{2^k}{3^{k-d}}
=\frac{2^k}{3^q}
=:\rho.
\]

Therefore

\[
\boxed{
\frac C{3^q}=1+\Sigma_d(E)-\rho.
}
\]

MATH-072 uses exactly

\[
S=1+\Sigma-\rho,
\qquad S=\frac C{3^q}.
\]

Hence

\[
\boxed{
\Sigma_{\rm MATH\text{-}051}=\Sigma_{\rm MATH\text{-}072/188}.
}
\]

There is one normalized correction signature, not two.

## 3. One-step consistency

Let `b in {0,1}` be the next shortcut parity, where `b=0` is even and `b=1` is odd.

If `b=1`, no new even position is added, so

\[
\Sigma'=\Sigma.
\]

If `b=0`, the new even position is

\[
e_d=k.
\]

Its new MATH-051 term is

\[
3^d\left(\frac23\right)^k
=\frac{2^k}{3^q}
=\rho.
\]

Thus universally

\[
\boxed{
\Sigma'=\Sigma+(1-b)\rho,
}
\]

which is exactly the MATH-187/188 recurrence.

So the Hensel signature is already propagated by the analytic one-step recurrence.

## 4. Integer correction coordinate

Define

\[
\boxed{
C:=3^q(1+\Sigma)-2^k.
}
\]

By the preceding identity this is exactly the ordinary shortcut correction in

\[
\boxed{
T^k(N)=\frac{3^qN+C}{2^k}.
}
\]

Conversely,

\[
\boxed{
\Sigma=\frac{C+2^k}{3^q}-1,
\qquad
S=\frac C{3^q}.
}
\]

Therefore `Sigma` and `S` are derived once `(k,q,C)` is known.

The one-step correction recurrence is especially simple:

\[
\boxed{
C'=
\begin{cases}
C,&b=0,\\
3C+2^k,&b=1.
\end{cases}
}
\]

Equivalently,

\[
\boxed{C'=3^bC+b2^k.}
\]

This is algebraically equivalent to the MATH-188 `(k,q,Sigma)` recurrence.

## 5. Hensel class from the same C

For fixed `(k,q)`, the one-sided root-Hensel class is

\[
\boxed{r=C\bmod3^q.}
\]

If an arbitrary competitor has correction

\[
C_*=C+t3^q,
\qquad t>0,
\]

then

\[
\boxed{
\Sigma_*-\Sigma=t.
}
\]

Thus the positive MATH-051 integer signature difference is exactly the MATH-040 ordinary-start translation credit.

No conversion between two unrelated signatures is required.

## 6. Exact source translation and equal endpoint

The parity word fixes the canonical source residue

\[
\boxed{
a(C;k,q)\equiv-C(3^q)^{-1}\pmod{2^k}.}
\]

For a competitor with `C_*=C+t3^q`,

\[
a(C_*;k,q)\equiv a(C;k,q)-t\pmod{2^k}.
\]

More strongly, for any ordinary start `N` for which both translated starts are legal,

\[
\boxed{
3^q(N-t)+C_*=3^qN+C.
}
\]

Hence

\[
\boxed{
T_*^k(N-t)=T^k(N).
}
\]

This is the exact ordinary-start meaning of positive one-sided Hensel credit.

## 7. Automatic positivity of the credit in the audited first-cell depth range

For fixed `d`, every MATH-051 signature obeys

\[
0\le\Sigma_d(E)
\le\sum_{j=0}^{d-1}2^j
=2^d-1,
\]

because `e_j>=j` gives

\[
3^j(2/3)^{e_j}\le2^j.
\]

Therefore any positive integer Hensel credit between two fixed-`(k,d)` words satisfies

\[
\boxed{0<t<2^d.}
\]

In the coefficient-valid audited range `k<=41`, MATH-051 has `d<=15`, so

\[
\boxed{t<2^{15}=32768.}
\]

Every first-cell ordinary start satisfies

\[
N>2^{71}.
\]

Consequently every positive Hensel credit occurring in the audited `k<=41` coefficient-valid range automatically satisfies

\[
\boxed{0<t<N.}
\]

Thus MATH-040's legal-positive-start side condition requires no separate per-state test in this finite product range.

This is a finite-scope statement tied to the current first-cell window and `k<=41`; it is not an arbitrary-depth theorem.

## 8. Gap level equals the odd-count clock

MATH-051 writes

\[
G_j=e_j-j.
\]

At the `j`-th even step, immediately before that step there have been exactly `j` earlier evens, so at depth `e_j` the odd count is

\[
q=e_j-j.
\]

Therefore

\[
\boxed{G_j=q\text{ at the moment of the }j\text{-th even step}.}
\]

So the MATH-051 gap-level scan is a block representation of the same odd-count clock used by MATH-188.

If

\[
a_r=\sum_{j:G_j=r}2^j
\]

is the candidate even-rank block at odd-count level `r`, and `b_r` is the corresponding competitor block, then

\[
\Sigma_*-\Sigma
=\sum_r(b_r-a_r)\left(\frac23\right)^r.
\]

MATH-051's reverse carry

\[
\boxed{
h_{r-1}=\frac{2(h_r+b_r-a_r)}3}
\]

is therefore an exact blockwise test on the same `q`-clock, not an external coordinate system.

## 9. Consequence for the proof-facing state

The mathematical state does not need to store all of

\[
(\Sigma,S,\text{Hensel residue},\text{canonical source residue})
\]

independently.

The triple

\[
\boxed{(k,q,C)}
\]

determines all four.

The cumulative penalty is also derived from the same correction:

\[
\boxed{
\mathcal P=S_*(q)-\frac C{3^q},
}
\]

where the mechanical envelope `S_*(q)` depends only on `q`.

Therefore the explicit numeric core of the MATH-188 state can be reduced from `(k,q,Sigma,P,...)` to `(k,q,C,...)`.

An exact source subfamily may still require an integer lift interval when earlier structural cuts retain only part of one residue class; that address interval is not removed by this lemma.

## 10. Claim boundary

Established:

- MATH-051 `Sigma_d` and MATH-072/188 `Sigma` are exactly identical;
- their one-step updates coincide;
- integer correction `C` determines `Sigma`, normalized correction `S`, the Hensel class, and canonical source residue;
- positive Hensel signature difference is exactly ordinary-start translation credit;
- in the audited first-cell range `k<=41`, every positive Hensel credit is automatically a legal positive credit because `t<32768<2^71<N`;
- MATH-051 gap level `G_j` is exactly the odd-count level `q` of the corresponding even event.

Not established:

- arbitrary-depth automatic positivity of Hensel credit;
- singleton terminal closure;
- closure of any new paid-count layer;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

Companion exact finite regression:

`collatz/src/2026_09_18_math189_shared_sigma_correction_bridge_certificate.py`
