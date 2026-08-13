# Dyadic--ternary reciprocity of the boundary Riesz factors

Date: 2026-08-13

Status: **exact modular identity and reduction**. Every inverse-power-of-three dyadic phase in the deterministic Beatty boundary cube can be rewritten as a ternary rational phase involving an inverse power of two modulo `3^ell`. This gives an explicit bridge from the boundary Fourier channel to the existing 3-adic predecessor/residue channel. It is not a Collatz proof.

## 1. Boundary cube phase

The deterministic plateau-pair cube theorem produces factors

\[
\boxed{
\left|
\cos\!\left(
\pi k
\frac{[3^{-\ell}]_{2^m}}{2^m}
\right)
\right|,
}
\]

where

- `k` is the Fourier frequency;
- `ell` is the ordinal of the one in the free plateau pair;
- `m=L+1-j` is the remaining dyadic resolution from the pair start.

The apparent arithmetic object is an inverse power of three modulo a power of two.

## 2. Exact reciprocal representation

Set

\[
x=[3^{-\ell}]_{2^m},
\qquad
0<x<2^m.
\]

By definition,

\[
3^\ell x\equiv1\pmod{2^m}.
\]

Hence there is an integer `u=u_{m,ell}` such that

\[
\boxed{
3^\ell x=1+u2^m.
}
\]

Since `0<x<2^m`,

\[
0<u<3^\ell.
\]

Reducing the identity modulo `3^ell` gives

\[
\boxed{
u2^m\equiv-1\pmod{3^\ell}.}
\]

Thus

\[
\boxed{
u_{m,\ell}=[-2^{-m}]_{3^\ell}.}
\]

Dividing the exact integer identity by `3^ell 2^m` yields

\[
\boxed{
\frac{[3^{-\ell}]_{2^m}}{2^m}
=
\frac{[-2^{-m}]_{3^\ell}}{3^\ell}
+
\frac1{3^\ell2^m}.
}
\]

This is exact, not asymptotic.

## 3. Fourier factor in ternary coordinates

Substitution gives

\[
\boxed{
\left|
\cos\!\left(
\pi k
\frac{[3^{-\ell}]_{2^m}}{2^m}
\right)
\right|
=
\left|
\cos\!\left[
\pi\left(
\frac{k[-2^{-m}]_{3^\ell}}{3^\ell}
+
\frac{k}{3^\ell2^m}
\right)
\right]
\right|.
}
\]

If the frequency is represented by `0<=k<2^m`, then the final correction obeys

\[
0\le
\frac{k}{3^\ell2^m}
<3^{-\ell}.
\]

Hence, for moderate or large `ell`, the phase is determined to exponentially high accuracy by the ternary residue

\[
\boxed{
k[-2^{-m}]_{3^\ell}\pmod{3^\ell}.}
\]

## 4. Quantitative near-one implication

Let

\[
\|x\|_{\mathbb R/\mathbb Z}
:=\min_{n\in\mathbb Z}|x-n|.
\]

If a boundary factor is at least

\[
\cos(\pi\delta),
\qquad 0<\delta<1/2,
\]

then its phase is within `delta` of an integer. Therefore

\[
\boxed{
\left\|
\frac{k[-2^{-m}]_{3^\ell}}{3^\ell}
\right\|_{\mathbb R/\mathbb Z}
\le
\delta+3^{-\ell}.
}
\]

Thus every boundary-cube factor that fails to contract imposes a short-arc condition on a concrete residue modulo `3^ell`.

## 5. Interpretation

The boundary cube initially appeared to require control of the inverse dyadic unit

\[
3^{-\ell}\pmod{2^m}.
\]

The reciprocity identity shows that the same phase can instead be read as

\[
-2^{-m}\pmod{3^\ell}.
\]

Therefore the two spectral channels are not independent pieces of arithmetic:

\[
\boxed{
\text{dyadic inverse-three phase}
\quad\leftrightarrow\quad
\text{ternary inverse-two residue}.
}
\]

This is precisely the type of cross-base relation needed by the spectral-exception splitting program.

## 6. Connection to the reverse-predecessor sieve

The reverse-predecessor work already encodes inverse powers of two modulo powers of three. A reverse path with `q` odd inverse steps imposes endpoint congruence conditions modulo `3^q` involving powers `2^{-K}`.

The present boundary factor uses

\[
[-2^{-m}]_{3^\ell}.
\]

Thus a Fourier-exception condition on a deterministic plateau coordinate can be passed directly to the same 3-adic state space used by the smaller-predecessor sieve.

The next exact target is to determine whether repeated near-one boundary factors force one of the already-forbidden contracting-predecessor cylinders, or a controlled extension of them.

## 7. Why this is useful

The remaining R2 obstacle had been phrased as a spectral complementarity theorem: selector frequencies that are poorly mixed must be killed by the Beatty boundary spectrum.

The present identity sharpens that target:

> a boundary spectral exception is a sequence of explicit near-zero conditions for the residues `k[-2^{-m}] mod 3^ell`.

This replaces an analytic-looking inverse-power cosine problem by a family of discrete ternary congruence constraints, allowing the Fourier and reverse-predecessor channels to be treated in one common arithmetic state space.
