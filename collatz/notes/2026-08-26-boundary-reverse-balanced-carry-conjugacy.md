# Exact boundary reverse-balanced-carry conjugacy

Date: 2026-08-26

Status: **exact finite-group identity and carry-language reduction.**  This note rewrites each deterministic Beatty-boundary Riesz factor as the endpoint of a reverse balanced-ternary carry orbit on the same dyadic frequency.  It sharpens the earlier dyadic--ternary reciprocity identity from a short-arc ternary-residue condition to an exact two-sided carry statement.  It is not a Collatz proof.

## 1. Reverse centered dyadic orbit

Fix

\[
M=2^L,
\qquad k\text{ odd}\pmod M.
\]

Let

\[
b_0=\operatorname{cent}_M(k),
\]

and recursively define

\[
b_{i+1}=\operatorname{cent}_M(3^{-1}b_i),
\qquad i\ge0,
\]

where \(3^{-1}\) is taken modulo \(M\).

Since every \(b_i\) is odd and \(M\) is a power of two, the centered endpoint \(\pm M/2\) never occurs.

There is therefore a unique digit

\[
d_i\in\{-1,0,1\}
\]

such that

\[
\boxed{
3b_{i+1}=b_i+d_iM.
}
\]

Equivalently,

\[
b_i=3b_{i+1}-d_iM.
\]

Thus inverse multiplication by three on the centered dyadic circle is a reverse balanced-ternary carry automaton.

## 2. Exact reverse carry expansion

Iterating gives

\[
\boxed{
b_0=3^\ell b_\ell-MD_\ell,}
\]

where

\[
\boxed{
D_\ell:=\sum_{i=0}^{\ell-1}d_i3^i.
}
\]

Reducing modulo \(3^\ell\),

\[
\boxed{
D_\ell\equiv-b_0M^{-1}\pmod{3^\ell}.
}
\]

Because the digits are balanced, \(D_\ell\) is the centered balanced-ternary representative of this residue.

## 3. Exact conjugacy with the boundary inverse-three phase

Let

\[
x_\ell=[3^{-\ell}]_M,
\qquad 0<x_\ell<M.
\]

The earlier reciprocity identity gives an integer \(u_\ell\) satisfying

\[
3^\ell x_\ell=1+u_\ell M,
\qquad
u_\ell\equiv-M^{-1}\pmod{3^\ell}.
\]

Write the frequency representative as

\[
k=b_0+nM,
\qquad n\in\{0,1\}.
\]

Modulo integers,

\[
\frac{kx_\ell}{M}
\equiv
\frac{k u_\ell}{3^\ell}
+
\frac{k}{3^\ell M}.
\]

Using

\[
k u_\ell\equiv D_\ell-n\pmod{3^\ell}
\]

and

\[
\frac{b_0}{M}=3^\ell\frac{b_\ell}{M}-D_\ell,
\]

all correction terms cancel exactly. Therefore

\[
\boxed{
\frac{k[3^{-\ell}]_M}{M}
\equiv
\frac{b_\ell}{M}
\pmod{\mathbb Z}.
}
\]

Hence every deterministic boundary factor satisfies the exact identity

\[
\boxed{
\left|
\cos\!\left(
\pi k\frac{[3^{-\ell}]_M}{M}
\right)
\right|
=
\left|
\cos\!\left(
\pi\frac{b_\ell}{M}
\right)
\right|.
}
\]

There is no asymptotic error term.

## 4. Near-one factors are exactly reverse zero-carry suffixes

Fix \(1\le s\le\ell\).

The following are equivalent:

1. the last \(s\) reverse carry digits vanish,
   \[
   d_{\ell-s}=\cdots=d_{\ell-1}=0;
   \]
2. the reverse endpoint lies in the central interval
   \[
   \boxed{
   |b_\ell|<\frac{M}{2\,3^s};
   }
   \]
3. the boundary factor is at least
   \[
   \boxed{
   \left|
   \cos\!\left(
   \pi k\frac{[3^{-\ell}]_M}{M}
   \right)
   \right|
   \ge
   \cos\!\left(\frac{\pi}{2\,3^s}\right).
   }
   \]

### Proof of 1 => 2

If the last \(s\) digits are zero, then

\[
b_{\ell-s}=3^s b_\ell.
\]

Since \(|b_{\ell-s}|<M/2\),

\[
|b_\ell|<M/(2\,3^s).
\]

### Proof of 2 => 1

If

\[
|b_\ell|<M/(2\,3^s),
\]

then \(|3b_\ell|<M/(2\,3^{s-1})\le M/2\), so no recentering carry is needed at the preceding step and \(d_{\ell-1}=0\). Iterating gives all \(s\) zero digits.

The equivalence with 3 follows from the exact cosine conjugacy and monotonicity of \(\cos(\pi x)\) on \([0,1/2]\). Equality at the dyadic/triadic boundary cannot occur because \(3^s\nmid2^{L-1}\).

## 5. Two-sided carry interpretation

For the same odd dyadic frequency, define the full orbit

\[
x_n=\operatorname{cent}_M(k3^n),
\qquad n\in\mathbb Z.
\]

Then

\[
\boxed{
x_{n+1}=3x_n-c_nM,
\qquad c_n\in\{-1,0,1\}.}
\]

The two previously separate spectral mechanisms are now two directions of this one orbit:

- \(n\ge0\): forward nonzero carries control ternary-selector Riesz attenuation;
- \(n<0\): reverse zero-carry runs characterize large Beatty-boundary factors.

Thus the spectral complementarity problem becomes a **two-sided carry incompatibility problem** on one deterministic dyadic orbit.

## 6. Proof-program consequence

The high-shell exceptional set no longer needs to be described by two unrelated conditions.

A dangerous frequency must simultaneously exhibit

1. too few nonzero forward carries over the selector horizon, so selector attenuation is weak;
2. sufficiently long reverse zero-carry suffixes at the plateau-pair coordinates that generate the Beatty boundary cube, so boundary attenuation is also weak.

The next theorem target is therefore:

> **Two-sided balanced-carry incompatibility.**  Bound the number, density, or weighted contribution of odd dyadic frequencies whose forward carry word is sparse while the required family of reverse carry windows contains too many long zero suffixes.

This is the exact carry-language form of the remaining selector--boundary high-shell correlation problem.

Certificate:

`collatz/src/boundary_reverse_balanced_carry_conjugacy_certificate.py`.
