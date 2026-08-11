# Christoffel extremal bound for renewal cycle shadows

Date: 2026-08-11

Status: **exact consequence of the renewal rational-cycle shadow plus the Christoffel extremal inequality of Fernández–Ibáñez (arXiv:2607.24844, 2026)**. The extension from an integer periodic orbit to the rational shadow uses only the combinatorial inequality for `C_min`; no integrality is needed in that step.

## 1. External extremal input

For a binary parity word of accelerated length `A` with `H` odd symbols and `A/H>log_2 3`, Fernández–Ibáñez prove that the Christoffel word maximizes the rotation-minimum correction functional `C_min` at fixed `(A,H)`.

Their proof of Theorem 8.2 gives the combinatorial inequality

\[
\boxed{
\frac{C_{\min}(w)}{2^A-3^H}
\le
\frac{1}{2^{A/H}-3}.
}
\]

The published theorem states this for the minimum element of an integer periodic orbit, but the displayed inequality itself is obtained before and independently of any integrality test: it is an upper bound on the rational fixed-point value associated with the minimum rotation of the word.

## 2. Application to a supercritical renewal shadow

For an aggregate-supercritical renewal segment, let

\[
F(x)=\frac{3^H x+B}{2^A},
\qquad
2^A>3^H,
\]

and let `C` be its positive rational fixed point.

The renewal-shadow minimum theorem shows that `C` is the strict minimum of the rational periodic shadow of this word. Therefore

\[
C=
\frac{C_{\min}(w)}{2^A-3^H}.
\]

Hence

\[
\boxed{
C\le
\frac{1}{2^{A/H}-3}.
}
\]

The renewal shadow also satisfies

\[
\boxed{C>N',}
\]

where `N'` is the next renewal floor. Consequently

\[
\boxed{
N'<
\frac{1}{2^{A/H}-3}.
}
\]

## 3. Exact aggregate resonance window

Write

\[
A=H+D,
\qquad
\alpha:=\log_2(3/2).
\]

Then

\[
\frac AH
=
\log_2 3+rac{D-\alpha H}{H}.
\]

Set

\[
\Delta:=D-\alpha H>0.
\]

The floor bound becomes

\[
3\,2^{\Delta/H}
<3+\frac1{N'},
\]

so

\[
\boxed{
0<\Delta
<
H\log_2\left(1+\frac1{3N'}\right).
}
\]

This is a rigorous aggregate resonance bound obtained without assuming that all odd-event states inside a maximal block exceed the next renewal floor.

## 4. Supercritical slope window

Because `C>N'>1`, the Christoffel upper bound must exceed `1`. If `A/H>=2`, then

\[
\frac{1}{2^{A/H}-3}\le1,
\]

which is impossible. Therefore

\[
\boxed{
\log_2 3<\frac AH<2.
}
\]

Equivalently,

\[
\boxed{
\alpha H<D<H.
}
\]

Thus every floor-increasing aggregate-supercritical renewal has average odd-event valuation strictly between the Collatz critical value and `2`.

## 5. Critical-layer / linear-overload dichotomy

Define

\[
\boxed{
\beta(N):=
\log_2\left(1+\frac1{3N}\right).
}
\]

The resonance bound is

\[
0<D-\alpha H<H\beta(N').
\]

If

\[
H\beta(N')<1,
\]

then the integer `D` can only be the least integer strictly above `alpha H`:

\[
\boxed{D=\lceil\alpha H\rceil.}
\]

Hence every aggregate-supercritical renewal obeys

\[
\boxed{
\begin{array}{ll}
\text{critical layer:}&D=\lceil\alpha H\rceil,\\[1mm]
\text{or}\
\text{linear-depth overload:}&H\ge\beta(N')^{-1}.
\end{array}
}
\]

Since

\[
\beta(N)^{-1}
\sim3(\ln2)N,
\]

the second branch requires odd-event depth asymptotic to at least `2.079... N'`.

## 6. Exact floor ceiling on the critical layer

In the critical case put

\[
\delta_H
:=
\lceil\alpha H\rceil-\alpha H
\in(0,1).
\]

Then

\[
\delta_H
<
H\log_2\left(1+\frac1{3N'}\right).
\]

Solving for `N'` gives

\[
\boxed{
N'
<
\frac{1}{3\left(2^{\delta_H/H}-1\right)}.
}
\]

For small `delta_H/H`,

\[
N'
\lesssim
\frac{H}{3\ln2\,\delta_H}.
\]

Thus a critical-layer supercritical renewal at a large floor requires `alpha H` to lie extraordinarily close below an integer. The hard core is therefore reduced to a one-parameter Diophantine resonance family plus the separate linear-depth-overload family.

## 7. Role

This theorem materially sharpens the renewal exceptional sector:

- aggregate-supercritical renewals cannot have arbitrary `(H,D)`;
- away from the minimal supercritical integer layer they must have event depth linear in the renewal floor;
- on the minimal layer the admissible floor is explicitly bounded by the Diophantine gap `ceil(alpha H)-alpha H`.

The remaining global task is to prove that an infinite renewal-floor chain cannot repeatedly pay either of these two costs while satisfying the exact Collatz formation arithmetic.
