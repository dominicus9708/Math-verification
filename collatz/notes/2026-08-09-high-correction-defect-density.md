# High-correction defect-density constraint at a convergent resonance

Date: 2026-08-09

Status: **DERIVED NECESSARY CONDITION + FINITE RECORD-HOLDER DIAGNOSTIC**

This note combines the Denjoy–Koksma upper bound on the mechanical correction with the defect-channel representation. The resulting density inequality is deterministic for a paradoxical first crossing. Comparisons with known finite record holders are diagnostics only.

## 1. Mechanical and actual normalized corrections

At a first coefficient crossing with total odd count `q`, let

\[
\kappa_i=\lfloor i\log_2 3\rfloor,
\qquad
d_i\le\kappa_i
\]

be the mechanical cap and the actual position of the i-th odd step.

Define

\[
u_i^*=\frac{2^{\kappa_i}}{3^{i+1}},
\qquad
S^*(q)=\sum_{i=0}^{q-1}u_i^*,
\]

and

\[
S(w)=\sum_{i=0}^{q-1}\frac{2^{d_i}}{3^{i+1}}.
\]

Put the defect depth

\[
z_i=\kappa_i-d_i\ge0.
\]

Then the normalized correction deficit is

\[
\boxed{
\Delta S
=S^*(q)-S(w)
=\sum_i u_i^*\left(1-2^{-z_i}\right).
}
\]

Since

\[
\frac16<u_i^*\le\frac13,
\]

a coordinate with `z_i>=s>=1` contributes at least

\[
\frac16(1-2^{-s})
\]

to `Delta S`.

## 2. General defect-count inequality

Let

\[
N_{\ge s}=\#\{i:z_i\ge s\}.
\]

Then

\[
\Delta S
\ge
N_{\ge s}\frac16(1-2^{-s}),
\]

hence

\[
\boxed{
N_{\ge s}
\le
\frac{6\Delta S}{1-2^{-s}}.
}
\]

In particular,

\[
\boxed{N_{>0}\le12\Delta S.}
\]

## 3. Incorporating a paradoxical start lower bound

At

\[
\delta=2^\sigma/3^q-1>0,
\]

a paradoxical first crossing satisfies

\[
S(w)\ge\delta x.
\]

Suppose an external/mechanical estimate gives

\[
S^*(q)\le U(q).
\]

If the candidate start also obeys

\[
x\ge X,
\]

then necessarily

\[
\boxed{
\Delta S\le A(X):=U(q)-\delta X.
}
\]

Therefore

\[
\boxed{
N_{\ge s}
\le
\frac{6A(X)}{1-2^{-s}}.
}
\]

When `A(X)<0`, the entire magnitude layer is eliminated immediately.

## 4. Next unresolved convergent, m=46 layer

Use

\[
q=137,528,045,312,
\quad
\sigma=217,976,794,617,
\]

\[
\delta\approx8.9865487086219626069\times10^{-13}.
\]

At this convergent the Denjoy–Koksma bound is

\[
U(q)=\frac{q}{6\ln2}+\frac13
\approx3.3068504826129175\times10^{10}.
\]

The minimal recursive-core start in the `m=46` layer is

\[
X_{46}=4\cdot3^{46}+3
=35,451,752,478,610,004,383,719.
\]

Thus

\[
\delta X_{46}
\approx3.1858890045503820\times10^{10},
\]

and

\[
\boxed{
A(X_{46})
\approx1.2096147806253557\times10^9.
}
\]

Consequently

\[
\boxed{
N_{>0}\le14,515,377,367
}
\]

(up to the final strict/integer rounding chosen in a publication certificate).
Relative to q, this is about

\[
\boxed{
N_{>0}/q\le0.105545.
}
\]

Therefore at least approximately

\[
\boxed{89.4455\%}
\]

of all odd-position coordinates must satisfy the exact mechanical equality

\[
\boxed{d_i=\lfloor i\log_2 3\rfloor.}
\]

Stronger depth tails are:

\[
N_{\ge2}/q\lesssim0.07036,
\]

\[
N_{\ge3}/q\lesssim0.06031.
\]

This is a necessary condition for a paradoxical first crossing in the `m=46` magnitude layer; it is not a heuristic density statement.

## 5. Finite record-holder diagnostic

For orientation only, exact trajectories of several known coefficient-stopping record holders were profiled through their own first coefficient crossing. The fraction of odd positions exactly on the mechanical cap was:

- 27: 4/37 = 10.81%;
- 703: 2/51 = 3.92%;
- 10087: 9/66 = 13.64%;
- 381727: 6/109 = 5.50%;
- 1126015: 2/141 = 1.42%;
- 63728127: 6/237 = 2.53%;
- 12235060455: 6/345 = 1.74%.

These finite values are **not** evidence of an asymptotic theorem. They only show that the `m=46` hypothetical paradoxical path would have to be structurally very different from the finite coefficient-record trajectories currently observed.

## 6. Proof target suggested by the inequality

The next possible theorem is an anti-alignment statement of the form:

> an ordinary positive integer whose canonical start lies in the small 75-bit / recursive-core window cannot realize a first-crossing odd-position vector with at least `~89.45%` exact mechanical-cap coordinates at the specified resonance.

This is sharper than asking merely for low odd-count discrepancy. It couples

- Archimedean correction size (near mechanical maximum),
- the sparse defect channel,
- and 2-adic canonical-start realization.

Proving such a statement remains open in the project.