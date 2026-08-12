# Renewal coefficient-stopping dichotomy and critical-cylinder fork

Date: 2026-08-12

Status: **exact proof-architecture theorem for every nonperiodic renewal-floor counterexample candidate**. The external López–Stoll result is used only for the critical-density necessity in the coefficient-survival branch; the dichotomy and cylinder fork are elementary/exact.

## 1. Renewal-floor coefficient stopping time

Let

\[
N_0<N_1<N_2<\cdots
\]

be the renewal-floor chain of a hypothetical nonperiodic positive-integer first-descent survivor.

For each renewal floor `N_j`, restart the accelerated Collatz map at `N_j` and define its coefficient stopping time

\[
\boxed{
\tau_c^{(j)}
:=
\min\{k\ge1:3^{q_k(N_j)}<2^k\},
}
\]

with value `infinity` if no such prefix exists.

Because `N_j` is a suffix minimum, if `tau_c^{(j)}` is finite then the first coefficient crossing endpoint is still at least `N_j`; hence it is a paradoxical first-crossing prefix.

## 2. Exact renewal CST dichotomy

Exactly one of the following holds:

### R1: infinitely many finite coefficient crossings

\[
\boxed{
\#\{j:\tau_c^{(j)}<\infty\}=\infty.
}
\]

Then infinitely many distinct renewal floors generate first-crossing paradoxical prefixes. Each is governed by the universal Beatty first-crossing frame.

### R2: eventual coefficient survival

There exists `J` such that

\[
\boxed{
\tau_c^{(j)}=\infty
\qquad\forall j\ge J.
}
\]

This is the eventual coefficient-survival hard core.

No third case exists.

## 3. Dual-record theorem for R2

Use a global parity-time coordinate and let

\[
\boxed{
L(k):=q(k)\log_2 3-k
}
\]

be the logarithm base `2` of the multiplicative coefficient accumulated from the fixed global origin to parity time `k`.

Let `t_j` be the parity time of renewal floor `N_j`.

If

\[
\tau_c^{(j)}=\infty,
\]

then every future relative prefix coefficient is strictly larger than `1`. Equivalently,

\[
\boxed{
L(k)>L(t_j)
\qquad\forall k>t_j.
}
\]

Thus `t_j` is simultaneously

1. a suffix-minimum time of the ordinary orbit value;
2. a strict suffix-minimum time of the coefficient log-walk.

Hence the R2 hard core is a **dual-record branch**.

For consecutive late renewal floors,

\[
L(t_{j+1})>L(t_j).
\]

## 4. Every late R2 renewal segment is aggregate subcritical in the inverse coordinate

For a renewal segment from `N_j` to `N_{j+1}`, let

\[
H_j=\text{odd count},
\qquad
A_j=\text{total parity length},
\]

and write

\[
A_j=H_j+D_j.
\]

R2 gives

\[
\frac{3^{H_j}}{2^{A_j}}>1.
\]

Define

\[
\boxed{
\varepsilon_j
:=H_j\log_2 3-A_j
=\log_2(3/2)H_j-D_j>0.
}
\]

The inverse multiplier used in the renewal notes is

\[
P_j:=\frac{2^{A_j}}{3^{H_j}}=2^{-\varepsilon_j}<1.
\]

Hence every sufficiently late R2 renewal transition is aggregate-subcritical.

The exact renewal product gives

\[
\boxed{
\frac{N_{j+1}}{N_j}
=2^{\varepsilon_j}Q_j,
\qquad Q_j>1,
}
\]

so

\[
\boxed{
N_{j+1}>2^{\varepsilon_j}N_j.
}
\]

Thus the coefficient-surplus record and the ordinary floor record grow in the same direction.

## 5. Cheap R2 transitions live on the nearest lower layer

Since

\[
A_j<H_j\log_2 3,
\]

we always have

\[
A_j\le\lfloor H_j\log_2 3\rfloor.
\]

If

\[
A_j\le\lfloor H_j\log_2 3\rfloor-1,
\]

then

\[
\varepsilon_j>1
\]

and therefore

\[
\boxed{N_{j+1}>2N_j.}
\]

Consequently every R2 renewal step that does **not** at least double the floor must lie on the unique nearest lower layer

\[
\boxed{
A_j=\lfloor H_j\log_2 3\rfloor.
}
\]

If

\[
f_H:=\{H\log_2 3\},
\]

then on this layer

\[
\varepsilon=f_H,
\]

and for floor gap `g=N'-N`,

\[
\boxed{
f_H<\log_2\left(1+\frac gN\right).}
\]

If the reduced rational `A/H` is not a continued-fraction convergent of `log_2 3`, Legendre gives

\[
f_H\ge\frac1{2H},
\]

hence

\[
\boxed{
g>N\left(2^{1/(2H)}-1\right).}
\]

So economical R2 steps are again confined to near-critical Diophantine layers.

## 6. Critical-cylinder binary fork

Put

\[
\gamma:=\log_2 3,
\]

and for a fixed odd count `H` define

\[
\boxed{
A_-(H):=\lfloor\gamma H\rfloor,
\qquad
A_+(H):=A_-(H)+1=\lceil\gamma H\rceil.
}
\]

The universal latest odd positions compatible with coefficient survival are

\[
\boxed{
i_k^*=\lfloor\gamma(k-1)\rfloor+1.}
\]

They define one critical lower prefix cylinder of length `A_-(H)`.

At that length the coefficient is still greater than `1`:

\[
\frac{3^H}{2^{A_-}}>1.
\]

One additional **even** parity bit produces

\[
\frac{3^H}{2^{A_+}}<1,
\]

and is therefore the first coefficient crossing.

One additional **odd** parity bit instead multiplies the coefficient by `3/2` and keeps the trajectory in the coefficient-survival sector.

Thus the two hard cores meet at one exact binary fork:

\[
\boxed{
\text{critical lower prefix}
\xrightarrow{0}
\text{R1 first crossing},
}
\]

\[
\boxed{
\text{critical lower prefix}
\xrightarrow{1}
\text{R2 continued coefficient survival}.
}
\]

## 7. Exact formation interpretation of the fork

A fixed length-`A_-` parity prefix defines one residue class modulo

\[
2^{A_-}.
\]

Lifting it by one more parity bit gives exactly two classes modulo

\[
2^{A_-+1},
\]

whose start representatives differ by

\[
\boxed{2^{A_-}.}
\]

The corresponding endpoint parities after the length-`A_-` prefix are opposite, because changing the start by `2^{A_-}` changes that endpoint by the odd amount `3^H`.

Hence the R1/R2 critical decision is literally the two dyadic children of one formation cylinder.

This is the cleanest direct connection between the earlier formation-floor/`beta` viewpoint and the coefficient-stopping split.

## 8. Critical-density necessity in R2

López–Stoll prove that if a rational 2-adic integer has a non-cyclic trajectory, then the lower limiting parity density must equal

\[
\frac{\ln2}{\ln3}
=\frac1{\log_2 3}.
\]

Therefore an ordinary positive-integer R2 counterexample cannot stay uniformly above the critical slope.

If

\[
e(k):=q(k)\log_2 3-k>0
\]

is the coefficient surplus from a late R2 renewal floor, then necessarily

\[
\boxed{
\liminf_{k\to\infty}\frac{e(k)}k=0.
}
\]

Thus the eventual coefficient-survival branch must remain strictly above the critical line at every prefix while approaching it sublinearly along an infinite subsequence.

This is precisely the unresolved boundary left open by the rational-2-adic density theorem; the theorem excludes a uniform positive density gap but not the critical meander itself.

## 9. Final role

The aperiodic renewal hard core can now be expressed in either of two equivalent ways:

### Renewal-floor form

- R1: infinitely many first-crossing paradoxical renewal floors;
- R2: eventual dual-record coefficient survival.

### Critical-cylinder form

At arbitrarily large critical lower cylinders, the ordinary integer trajectory must repeatedly choose between the two dyadic lifts:

- even child: pay the universal Beatty paradoxical first-crossing constraints;
- odd child: remain in a critical coefficient-survival meander.

A complete aperiodic proof must eliminate both infinite choices. The first is now strongly constrained by the Beatty tri-place defect and the `2.8e19` paradoxical-start frontier; the second is the exact critical boundary not eliminated by the known rational-2-adic parity-density theorem.
