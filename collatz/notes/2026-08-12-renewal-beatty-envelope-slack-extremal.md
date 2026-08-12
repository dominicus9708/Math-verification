# Renewal Beatty-envelope slack and internal extremal theorem

Date: 2026-08-12

Status: **exact finite theorem for the two economical renewal endpoint layers**. It is derived only from the renewal pure-coefficient record property and does not require an external Christoffel extremal theorem. It does not exclude infinite renewal concatenation.

## 1. Setup

Let a genuine renewal segment start at an odd renewal floor `N` and end at the next odd renewal floor `N'>N` after `H` odd Syracuse events.

Put

\[
\gamma:=\log_2 3,
\qquad
A_k:=\sum_{i<k}v_i,
\qquad
0\le k\le H,
\]

and

\[
e_k:=k\gamma-A_k.
\]

The renewal pure-coefficient record theorem gives

\[
\boxed{e_k>e_H\qquad(0<k<H).}
\]

The only economical endpoint layers are

\[
\sigma:=\lfloor H\gamma\rfloor-A_H\in\{0,-1\}.
\]

Write

\[
\theta:=\{H\gamma\}\in(0,1).
\]

## 2. Upper economical layer

Assume

\[
\boxed{\sigma=-1.}
\]

Then

\[
A_H=\lceil H\gamma\rceil,
\qquad
e_H=\theta-1.
\]

The strict record inequality gives, for every `0<k<H`,

\[
k\gamma-A_k>\theta-1,
\]

hence

\[
A_k<k\gamma+1-\theta.
\]

Since `A_k` is an integer and the right side is irrational for `k<H`,

\[
\boxed{
A_k\le B_k^+(H)
:=\left\lfloor k\gamma+1-\theta\right\rfloor.
}
\]

The same formula also holds at the endpoints:

\[
B_0^+(H)=0,
\qquad
B_H^+(H)=\lceil H\gamma\rceil=A_H.
\]

Define the upper slack

\[
\boxed{d_k:=B_k^+(H)-A_k.}
\]

Then

\[
\boxed{d_k\ge0,\qquad d_0=d_H=0.}
\]

Because `1<gamma<2`, the reference increments

\[
\boxed{b_k^+:=B_{k+1}^+-B_k^+\in\{1,2\}}
\]

form a finite mechanical/Sturmian valuation word. The actual valuation is exactly

\[
\boxed{
v_k=b_k^+ + d_k-d_{k+1}.
}
\]

Thus every upper economical renewal word is a nonnegative slack excursion over a deterministic `{1,2}` mechanical reference word.

## 3. Lower economical layer

Assume

\[
\boxed{\sigma=0.}
\]

Then

\[
A_H=\lfloor H\gamma\rfloor,
\qquad
e_H=\theta.
\]

The renewal record theorem implies

\[
A_k<k\gamma-\theta
\qquad(0<k<H).
\]

Hence define

\[
\boxed{
B_0^-(H):=0,
\qquad
B_k^-(H):=\lfloor k\gamma-\theta\rfloor
\quad(1\le k\le H).
}
\]

For a genuine lower renewal the first-event condition forces `theta<gamma-1`, so `B_1^-=1`; thereafter all reference increments are again in `{1,2}`.

We have

\[
\boxed{A_k\le B_k^-(H),\qquad 0\le k\le H,}
\]

with equality at `k=0,H`.

Define

\[
\boxed{d_k:=B_k^-(H)-A_k.}
\]

Then

\[
\boxed{d_k\ge0,\qquad d_0=d_H=0,}
\]

and with

\[
b_k^-:=B_{k+1}^--B_k^-\in\{1,2\},
\]

we again have

\[
\boxed{v_k=b_k^-+d_k-d_{k+1}.}
\]

Thus the lower economical layer has the same mechanical-reference plus nonnegative-slack structure.

## 4. Internal correction extremal theorem

For either sign choose the corresponding reference `B_k` and slack `d_k`.

The normalized odd-event correction of the actual word is

\[
c_H
=\sum_{k=0}^{H-1}\frac{2^{A_k}}{3^{k+1}}
=\sum_{k=0}^{H-1}\frac{2^{B_k}}{3^{k+1}}2^{-d_k}.
\]

Define the reference correction

\[
\boxed{
c_H^*:=\sum_{k=0}^{H-1}\frac{2^{B_k}}{3^{k+1}}.
}
\]

Since `d_k>=0`, termwise

\[
\boxed{c_H\le c_H^*.}
\]

Equality occurs iff

\[
\boxed{d_k=0\quad\text{for every }0\le k\le H.}
\]

Therefore the finite mechanical reference is the unique correction-maximizing word among all renewal-compatible exponent paths having the same odd-event count and the same adjacent endpoint layer.

This is an internal renewal version of the Christoffel extremal phenomenon.

## 5. Exact slack defect

Define

\[
\boxed{
\xi_H:=c_H^*-c_H.
}
\]

Then exactly

\[
\boxed{
\xi_H
=\sum_{k=0}^{H-1}
\frac{2^{B_k}}{3^{k+1}}
\left(1-2^{-d_k}\right).
}
\]

The defect is nonnegative and vanishes exactly on the reference word.

### Upper reference term scale

For the upper reference,

\[
B_k^+=\lfloor k\gamma+1-\theta\rfloor.
\]

Hence, writing the relevant fractional part as `delta_k in [0,1)`,

\[
\frac{2^{B_k^+}}{3^{k+1}}
=\frac13 2^{1-\theta-\delta_k},
\]

so

\[
\boxed{
\frac{2^{-\theta}}3
<
\frac{2^{B_k^+}}{3^{k+1}}
\le
\frac{2^{1-\theta}}3.
}
\]

If `d_k>0`, then `1-2^{-d_k}>=1/2`, therefore that single nonzero slack position contributes

\[
\boxed{>\frac{2^{-\theta}}6>\frac1{12}}
\]

to `xi_H`.

Thus

\[
\boxed{
\#\{k:d_k>0\}<12\,\xi_H.
}
\]

(The sharper phase-dependent form is `# < 6*2^theta*xi_H`.)

### Lower reference term scale

For the lower reference and `k>=1`,

\[
\frac{2^{B_k^-}}{3^{k+1}}
=\frac13 2^{-\theta-\delta_k}
\]

with `delta_k in [0,1)`, so

\[
\boxed{
\frac{2^{-\theta}}6
<
\frac{2^{B_k^-}}{3^{k+1}}
\le
\frac{2^{-\theta}}3.
}
\]

Every nonzero slack position therefore contributes

\[
\boxed{>\frac{2^{-\theta}}{12}>\frac1{24}}
\]

to the defect, giving

\[
\boxed{
\#\{k:d_k>0\}<24\,\xi_H.
}
\]

Again a sharper phase-dependent bound is immediate.

## 6. Interpretation

The finite economical renewal language no longer needs to be described as an arbitrary valuation sequence.

For fixed `H` and endpoint layer it is exactly

\[
\boxed{
\text{deterministic finite Beatty/Sturmian reference}
+
\text{nonnegative zero-to-zero slack excursion}.
}
\]

The same slack is also a real correction defect: moving below the reference cumulative-halving envelope strictly decreases the additive correction.

This gives a direct bridge between:

- renewal suffix-minimum geometry;
- the critical irrational slope `log_2 3`;
- mechanical/Christoffel reference words;
- actual valuation deviations;
- and the available correction headroom.

## 7. Remaining target

The upper adjacent layer has a positive survival threshold, so its defect `xi_H` is constrained by how much reference correction headroom remains above the required value `(2^{1-theta}-1)N`.

The lower adjacent layer does not require additive correction to increase the floor, so no analogous one-segment headroom exclusion is available.

A complete aperiodic proof must therefore obstruct infinite concatenation of these slack excursions, especially the lower-layer excursions that can grow a renewal floor without paying a positive correction threshold.