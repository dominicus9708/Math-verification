# MATH-089 — terminal phase-address wedge for one-paid chains

Date: 2026-09-12

Status: `EXACT LOCAL LEMMA / REUSABLE ONE-PAID TERMINAL PRUNING RULE`

The Collatz conjecture and first universal Farey cell remain open.

## 1. Resolution height and terminal overshoot

Let an exact multi-source parent contain

\[
M
\]

source parameters and define

\[
R_{\rm res}=\lceil\log_2 M\rceil.
\]

A next one-paid edge of dyadic resolution `h` fixes one residue

\[
s_h\equiv(A_e-B)3^{-Q}\pmod{2^h},
\qquad0\le s_h<2^h.
\]

MATH-074 leaves only the terminal resolution overshoot

\[
\boxed{z=(h-R_{\rm res})_+}
\]

in the local Bellman charge.

## 2. Exact address meaning of z

For `h>R_res`, write

\[
s_h=s_R+2^{R_{\rm res}}\zeta,
\qquad0\le s_R<2^{R_{\rm res}}.
\]

Since `M<=2^R_res`, actual source compatibility

\[
s_h<M
\]

is equivalent to

\[
\boxed{\zeta=0\quad\text{and}\quad s_R<M.}
\]

Therefore

\[
\boxed{z=h-R_{\rm res}}
\]

is literally the number of additional high dyadic residue bits that must all be zero after the parent family has already been resolved to `R_res` bits.

This is the missing bridge between the resolution Bellman potential and exact dyadic compatibility.

## 3. Exact one-paid penalty law

In current-phase coordinates every one-paid edge has

\[
p=c\,\Omega_{\rm out},
\qquad
c\in\left\{\frac14,\frac18\right\}.
\]

The exact branch ranges are

\[
c=\frac14:
\qquad
\frac12<\Omega_{\rm out}<\frac23,
\]

and

\[
c=\frac18:
\qquad
\frac89<\Omega_{\rm out}<1.
\]

Thus every edge satisfies

\[
p>\frac19.
\]

## 4. Terminal phase-address wedge

With

\[
\lambda=\frac{19}{503},
\]

an actual locally negative terminal edge must satisfy simultaneously

\[
\boxed{
\zeta=0,
\qquad
s_R<M,
\qquad
c\Omega_{\rm out}<\lambda z.
}
\]

This is an exact conjunction of an address condition and a phase/penalty condition.

The first universal consequences are:

### z <= 2

Since

\[
\frac19>2\lambda,
\]

all such edges are automatically Bellman-safe.

### z = 3

The `c=1/4` branch is automatically safe because

\[
\frac18>3\lambda.
\]

Only the `c=1/8` branch can remain dangerous, and then necessarily

\[
\boxed{
\Omega_{\rm out}<\frac{456}{503}.
}
\]

This is a narrow subinterval of `(8/9,1)`.

### z = 4

For the `c=1/4` branch danger requires

\[
\boxed{
\Omega_{\rm out}<\frac{304}{503}.
}
\]

while the `c=1/8` branch is not eliminated by a branch-wide phase lower bound alone.

## 5. Structural consequence

The residual Bellman charge and the residual address requirement are not separate accidents:

\[
\boxed{
\text{Bellman overshoot bits}
=
\text{required zero-extension address bits}.
}
\]

This gives a reusable pruning order:

1. compute `R_res` from the exact source multiplicity;
2. set `z=(h-R_res)_+`;
3. if the phase inequality is automatically safe, discard the edge from the danger search;
4. otherwise test the exact low-residue/range condition and zero-extension condition;
5. only actual address-compatible phase-danger edges need further work.

## 6. Relation to the current frontier

MATH-088 showed a depth-17 example where every phase-danger edge failed the address condition.  MATH-089 explains why the quantity to track is not raw macro depth but the pair

\[
(z,\Omega_{\rm out})
\]

together with the exact zero-extension residue condition.

This lemma is intended to reduce the remaining macro-depth frontier `7..16` without enumerating every address state.

Reproducibility:

`collatz/src/2026_09_12_math089_terminal_phase_address_wedge_certificate.py`
