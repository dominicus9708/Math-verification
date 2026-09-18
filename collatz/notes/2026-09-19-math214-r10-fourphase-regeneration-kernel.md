# MATH-214 — four-phase Bellman potential and 15-bit carry-regeneration kernel for r=10

Date: 2026-09-19

Status: \`EXACT POTENTIAL REDUCTION / r=10 DANGER UPGRADED TO 15-BIT REGENERATION / LAYER OPEN\`

## 1. Purpose

MATH-202 gives a one-cluster r=10 danger threshold of 13 overshoot bits.
MATH-212 shows that this is too pessimistic over the true common phase orbit.

The four-cluster exact lower surplus satisfies

\[
\underline E_4
=
\frac{
40328831637298674714593
}{
18810608394584532713472
}
\]

and

\[
\boxed{
\underline E_4-56\lambda
=
\frac{
538598373207337125857
}{
18810608394584532713472
}
>0.
}
\]

This note converts that four-step inequality into a one-step Bellman potential and combines it with MATH-213's carry-valuation potential.

The result removes the explicit overshoot depth from the r=10 hard kernel.

## 2. r=10 phase cost

Let

\[
e(x)
\]

denote the exact MATH-202 lower surplus of one r=10 paid cluster at log-phase \(x\), and let

\[
F(x)=x+\alpha_{10}\pmod1
\]

be the MATH-207 phase rotation.

MATH-212 proves

\[
\boxed{
e(x)+e(Fx)+e(F^2x)+e(F^3x)
\ge
\underline E_4
>
56\lambda
}
\]

for every phase \(x\).

Define

\[
\boxed{
g(x):=e(x)-14\lambda.
}
\]

Then

\[
\boxed{
\sum_{j=0}^3g(F^jx)
\ge
\mu_4
:=
\underline E_4-56\lambda
>0.
}
\]

## 3. Four-state phase potential

Augment the proof state by a clock

\[
t\in\{0,1,2,3\}
\]

that advances modulo four on every r=10 paid-cluster transition.

Define

\[
\Phi_0(x)=0
\]

and, for \(t=1,2,3\),

\[
\boxed{
\Phi_t(x)
=
-\sum_{j=1}^{t}g(F^{-j}x).
}
\]

For a transition

\[
(t,x)\longmapsto(t+1\bmod4,Fx),
\]

one obtains exactly

\[
g(x)
+
\Phi_{t+1}(Fx)
-
\Phi_t(x)
=
0
\]

for \(t=0,1,2\), while for \(t=3\),

\[
g(x)
+
\Phi_0(Fx)
-
\Phi_3(x)
=
\sum_{j=0}^{3}g(F^{-j}x)
\ge
\mu_4.
\]

Therefore universally

\[
\boxed{
e(x)
+
\Phi'
-
\Phi
\ge
14\lambda.
}
\]

So the phase subsystem alone pays fourteen shortcut-step equivalents per r=10 cluster in a future-complete four-state extension.

## 4. Insert the singleton overshoot

MATH-186/202 give, for an r=10 singleton overshoot of depth \(z\),

\[
\Delta\mathcal B
\ge
e(x)-\lambda z.
\]

Adding the phase potential gives

\[
\boxed{
\Delta\mathcal B
+
\Phi'
-
\Phi
\ge
\lambda(14-z).
}
\]

Thus \(z\le14\) is already Bellman-safe in the augmented state.

This upgrades the structural r=10 danger condition from

\[
z\ge13
\]

to

\[
\boxed{
z\ge15
}
\]

unless carry valuation can be charged separately.

## 5. Nonzero carry valuation potential

For nonzero ordinary carry define

\[
v(d):=\nu_2(d)
\]

and the carry potential

\[
\boxed{
\Psi(d):=-\lambda v(d).
}
\]

MATH-213 writes the transition as

\[
z
=
v(d)-v(d')+\gamma,
\]

where

\[
\boxed{
\gamma
:=
\nu_2(3^Qd+c)-\nu_2(d)
}
\]

is the exact regeneration gain.

Therefore

\[
\begin{aligned}
\Delta\mathcal B
+\Delta\Phi
+\Delta\Psi
&\ge
\lambda(14-z)
+\lambda(v(d)-v(d'))\\
&=
\boxed{
\lambda(14-\gamma).
}
\end{aligned}
\]

Hence every nonzero-carry r=10 transition with

\[
\boxed{\gamma\le14}
\]

is Bellman-safe.

A potentially negative transition must satisfy

\[
\boxed{\gamma\ge15.}
\]

## 6. Exact 15-bit nonzero-carry kernel

Let

\[
c=B-A_{\rm next}.
\]

If

\[
\nu_2(c)\ne\nu_2(d),
\]

MATH-213 gives

\[
\gamma\le0,
\]

so the transition is automatically safe.

Thus danger requires the exact valuation match

\[
\boxed{
\nu_2(c)=\nu_2(d)=s.
}
\]

Write

\[
d=2^su,
\qquad
c=2^sa,
\]

with \(u,a\) odd.

Then

\[
\gamma
=
\nu_2(3^Qu+a).
\]

Therefore

\[
\boxed{
\gamma\ge15
\iff
3^Qu+a\equiv0\pmod{2^{15}}.
}
\]

Equivalently,

\[
\boxed{
u
\equiv
-a\,3^{-Q}
\pmod{32768}.
}
\]

So every remaining nonzero-carry r=10 danger transition is one exact 15-bit odd-carry residue.

## 7. Zero incoming carry

Set

\[
\Psi(0)=0.
\]

If \(d=0\) and \(c\ne0\), let

\[
s=\nu_2(c).
\]

After dividing by the compatible overshoot \(z\),

\[
v(d')=s-z.
\]

Then

\[
\Delta\mathcal B+\Delta\Phi+\Delta\Psi
\ge
\lambda(14-s).
\]

Hence a zero-to-nonzero transition is safe whenever

\[
s\le14.
\]

The only remaining zero-carry non-reset kernel is therefore

\[
\boxed{
d=0,\quad
c\ne0,\quad
c\equiv0\pmod{32768}.
}
\]

The exact reset case

\[
d=0,\qquad c=0
\]

remains separate.

For the frozen initial r=10 full-factor catalogue, MATH-206 already proves that no zero-carry compatible next factor exists at all, hence no exact reset exists there.

## 8. New r=10 hard kernel

After MATH-210 and the two potentials above, the frozen/mainline r=10 hard transition has been reduced from

\[
\text{arbitrary }z
+
\text{large integer carry}
+
\text{Hensel}
+
J
\]

to:

\[
\boxed{
\text{Hensel/Pareto-extremal future cell}
\cap
\text{15-bit regeneration resonance}.
}
\]

For nonzero carry this is

\[
\boxed{
\nu_2(c)=\nu_2(d),
\qquad
(d/2^s)
\equiv
-(c/2^s)3^{-Q}
\pmod{32768}.
}
\]

For zero incoming carry it is

\[
\boxed{
c\equiv0\pmod{32768},
}
\]

plus the separate exact-reset equality.

No overshoot-depth loop remains in the theorem-facing kernel.

## 9. Consequence for the intended architecture

The required exact quotient now needs only:

1. the four-state r=10 phase clock;
2. Hensel/Pareto extremality;
3. the matched valuation class;
4. one odd carry residue modulo \(32768\);
5. exact-reset flag.

The raw AP source, raw depth, and unbounded carry magnitude are not proof-state axes.

This is the strongest current alignment with the intended
\[
\text{one recurrence + emitted r + derived depth}
\]
program.

## 10. Claim boundary

Established:

- exact four-state phase Bellman potential;
- fourteen Bellman step-equivalents paid per r=10 cluster;
- exact cancellation of overshoot depth against carry-valuation potential;
- nonzero-carry danger reduced to one 15-bit odd-part congruence;
- zero-to-nonzero danger reduced to \(c=0\bmod32768\);
- frozen initial zero-carry branch remains absent by MATH-206.

Not established:

- emptiness of the reachable 15-bit regeneration quotient;
- arbitrary regenerated exact-reset exclusion;
- r=10 layer closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
