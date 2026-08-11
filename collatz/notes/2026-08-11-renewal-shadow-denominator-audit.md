# Renewal shadow denominator audit

Date: 2026-08-11

Status: **exact local denominator bound + strategy audit**. The conclusion is negative for one proposed global strategy: the rational-shadow denominator is not naturally a decreasing or persistent renewal potential.

## 1. Setup

For an aggregate-supercritical renewal segment let

\[
F(x)=\frac{3^H x+B}{2^A},
\qquad
\Delta:=A-H\log_2 3>0,
\]

and let consecutive renewal floors be

\[
N<N',
\qquad
g:=N'-N>0.
\]

Set

\[
Z:=2^A-3^H
=3^H(2^\Delta-1).
\]

The positive rational cycle shadow has minimum

\[
C=N'+\frac{g}{2^\Delta-1}
\]

and reduced denominator

\[
\boxed{
b=\operatorname{den}(C)
=\frac{Z}{\gcd(Z,g)}.}
\]

Therefore

\[
\boxed{b\ge\frac Zg.}
\]

## 2. Use the exact shadow-distance cost

The renewal/Christoffel shadow-distance theorem gives

\[
H
\ge
3\Delta\ln2
\left(
N'+\frac{g}{2^\Delta-1}
\right).
\]

Dropping the positive `N'` term yields

\[
H>
\frac{3\Delta\ln2}{2^\Delta-1}\,g.
\]

Hence

\[
\boxed{
g<
\frac{H(2^\Delta-1)}{3\Delta\ln2}.}
\]

Substituting into `b>=Z/g`, with `Z=3^H(2^Delta-1)`, gives the exact lower bound

\[
\boxed{
b>
\frac{3^{H+1}\Delta\ln2}{H}.}
\]

## 3. Interpretation

Unless the Diophantine discrepancy `Delta` is extraordinarily small, the rational-shadow denominator is exponentially large in the odd-event depth `H`.

Thus the denominator is not naturally driven toward `1` along increasingly deep supercritical renewal segments.

The periodic case `b=1` remains exactly characterized by

\[
Z\mid g,
\]

but a generic aperiodic renewal shadow can be arithmetically very far from this integer-shadow condition.

## 4. Why denominator collapse is not a persistent renewal strategy

Most importantly, the rational shadow is auxiliary to one finite renewal word. The next renewal floor `N'` is an ordinary integer and starts a new segment with a new shadow. The old denominator `b` is not transported as part of the exact integer renewal state.

Therefore even exponential denominator growth does not accumulate into a well-founded contradiction, and no monotonic denominator chain is presently available.

This weakens the proposed strategy

\[
\text{repeated renewal}\Rightarrow
\text{shadow denominator collapses to }1
\Rightarrow\text{periodicity}.
\]

The exact algebra points in the opposite local direction.

## 5. Strategic consequence

The primitive-resonance factorization remains useful as a local arithmetic diagnostic, but the principal global proof engine should use quantities that actually persist from one renewal floor to the next.

The cumulative renewal discrepancy

\[
S_J=\sum_{j<J}(D_j-\alpha H_j)
\]

and the renewal floor `N_J` do persist, and are linked by the exact product identity. These are therefore stronger candidates for the next global progress theorem than the one-segment shadow denominator.
