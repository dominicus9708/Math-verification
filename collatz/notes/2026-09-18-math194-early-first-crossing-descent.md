# MATH-194 — source-independent early first-crossing descent above the frozen floor

Date: 2026-09-18

Status: `EXACT STRUCTURAL LEMMA / q<=42 FIRST-CROSSING CLOSED / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-053 gives an exact upper bound on normalized correction while the coefficient survives. MATH-080 identifies strict descent with negativity of the self-comparison defect.

Combining them with the frozen lower floor

\[
N\ge2^{71}
\]

gives a source-independent first-crossing theorem. No same-integer address enumeration, Hensel witness search, or AP splitting is needed in the covered odd-count range.

## 2. Coefficient-surviving correction bound

For a coefficient-surviving prefix with `q` odd shortcut steps, MATH-053 gives

\[
S=\frac13\sum_{n=0}^{q-1}2^{-u_n}\Omega_n,
\]

with

\[
u_n\ge0,\qquad \frac12<\Omega_n\le1.
\]

Therefore

\[
\boxed{S<\frac q3.}
\]

The strict inequality follows because every `Omega_n<=1` and, except for the trivial initial normalization, the phase factors are strictly below one; the weaker `S<=q/3` is already enough below.

## 3. First coefficient failure

MATH-053 proves that first coefficient failure is exactly

\[
u=0\xrightarrow{E}-1.
\]

At the resulting state

\[
\rho=\frac{2^k}{3^q}>1.
\]

Since `2^k` and `3^q` are distinct integers,

\[
2^k-3^q\ge1.
\]

Hence

\[
\boxed{\rho-1=\frac{2^k-3^q}{3^q}\ge\frac1{3^q}.}
\]

## 4. Master-defect bound

MATH-080 gives the self-comparison defect

\[
\mathfrak D=S-N(\rho-1).
\]

For every unresolved first-cell source above the frozen floor,

\[
N\ge2^{71}.
\]

Thus at first coefficient failure

\[
\boxed{
\mathfrak D
<\frac q3-\frac{2^{71}}{3^q}.
}
\]

Therefore strict descent follows whenever

\[
q3^{q-1}<2^{71}.
\]

## 5. Uniform range q<=42

The left side is strictly increasing for positive integer `q`.

At the endpoint,

\[
42\cdot3^{41}
=1,531,865,847,841,173,028,926
\]

while

\[
2^{71}
=2,361,183,241,434,822,606,848.
\]

Hence

\[
\boxed{42\cdot3^{41}<2^{71}.}
\]

Consequently

\[
\boxed{
1\le q\le42
\quad\Longrightarrow\quad
\mathfrak D<0
}
\]

at the first coefficient failure.

So every such first crossing is a strict self-descent.

## 6. Consequence for the depth-41 product system

Any first coefficient failure occurring at global shortcut depth

\[
k\le41
\]

necessarily has

\[
q\le40
\]

(or, more weakly, `q<=41`). This lies strictly inside the `q<=42` theorem.

Therefore the joint `r=1..21`, depth `2..41` product system does not need an address/Hensel terminal analysis for a first coefficient failure occurring inside that depth window:

\[
\boxed{
\text{first coefficient failure by depth 41}
\Longrightarrow
\text{strict descent automatically}.
}
\]

The MATH-051 depth-41 survivor system may therefore be restricted to coefficient-surviving states; terminal coefficient-failure children are analytically closed by the present lemma.

## 7. DSD interpretation

This separates two roles that were previously mixed in the finite calculations:

1. **coefficient-boundary crossing at modest odd count:** closed by a scalar correction/coefficient inequality;
2. **long coefficient-surviving lineages:** still require Hensel/address/paid-state structure.

Thus expensive same-integer machinery is only needed after the trajectory has remained close enough to the moving coefficient boundary for sufficiently many odd events.

## 8. Scope warning

This theorem is tied to the frozen lower floor `2^71` and to the first coefficient failure measured from a common ordinary-source origin.

It must not be applied by resetting `S=0` at an interior macro boundary and then treating the resulting local `q` as the global odd count.

The synchronized-origin rule of MATH-188 is therefore essential.

## 9. Claim boundary

Established:

- universal bound `S<=q/3` while the coefficient survives;
- universal gap bound `rho-1>=3^{-q}` at first failure;
- source-independent first-crossing descent for `q<=42` above `2^71`;
- automatic closure of every first coefficient failure occurring within the audited depth-41 window.

Not established:

- first-crossing descent for arbitrary `q`;
- closure of coefficient-surviving states beyond the crossing-free depth window;
- modular danger-corridor avoidance for all later singleton states;
- any new paid-count layer closure by itself;
- first-cell emptiness;
- the Collatz conjecture.
