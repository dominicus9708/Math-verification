# MATH-184 — local positive reduced-cost drift of the `r=10` paid cluster

Date: 2026-09-17

Status: `EXACT STRUCTURAL LEMMA / r=10 BOTTLENECK RELOCATED / r=10 CLOSURE OPEN`

## 1. Purpose

MATH-182--183 relocate the desired proof from ordinary-source enumeration to a structural handoff/contraction problem.

This note asks a simpler question first:

> does an `r=10` paid cluster itself create a Bellman deficit at the target slope `19/503`, or is the observed finite workload inherited from the zero-cost prefix / address handoff?

The answer is exact: the `r=10` paid cluster has strictly positive local reduced-cost drift.

## 2. Universal paid-atom lower bound

For every paid odd event, the MATH-053/MATH-072 penalty atom is

\[
p_j=\frac{1-2^{-u_j}}{3}\,\varpi_j,
\]

with

\[
u_j\ge1,
\qquad
\frac12<\varpi_j\le1.
\]

Therefore

\[
1-2^{-u_j}\ge\frac12
\]

and hence

\[
\boxed{p_j>\frac1{12}.}
\]

For an `r`-paid cluster,

\[
\boxed{
\mathcal P_r>\frac r{12}.
}
\]

No source enumeration and no phase averaging are used.

## 3. Exact cluster-length bound

MATH-179 gives

\[
h_r
=r+1+m(r)+\mathbf 1_{\{\varpi\le\tau_r\}},
\]

where

\[
m(r)=\lfloor r\log_2(3/2)\rfloor.
\]

Thus

\[
\boxed{
h_r\le r+2+m(r).}
\]

For `r=10`,

\[
m(10)=5
\]

and therefore

\[
\boxed{h_{10}\le17.}
\]

## 4. Positive local reduced cost at `19/503`

Let

\[
\lambda=\frac{19}{503}.
\]

Then every exact `r=10` paid cluster satisfies

\[
\mathcal P_{10}-\lambda h_{10}
>
\frac{10}{12}-\frac{19}{503}\cdot17.
\]

The right side is exactly

\[
\boxed{
\frac{577}{3018}>0.
}
\]

Hence

\[
\boxed{
\mathcal P_{10}-\lambda h_{10}>\frac{577}{3018}.
}
\]

In step-equivalent units this surplus is

\[
\boxed{
\frac{577/3018}{19/503}
=\frac{577}{114}
\approx5.0614.
}
\]

So an `r=10` cluster pays for all of its own residual shortcut length and more than five additional target-slope step equivalents.

## 5. Why MATH-065 still has negative `r=10` cells

MATH-065 does not test the local cluster inequality above.

For each paid-exit source it sets

\[
H=L+h_r
\]

and compares the cluster penalty against

\[
\lambda(L+h_r).
\]

The accumulated cost is initialized to zero at that paid-exit source.

Therefore its margin is

\[
\boxed{
\text{margin}
=\mathcal P_r^{\rm lower}-\lambda(L+h_r),
}
\]

not merely

\[
\mathcal P_r^{\rm lower}-\lambda h_r.
\]

Thus a negative MATH-065 cell does **not** mean that the `r=10` paid cluster has negative local drift. It means that the newly accumulated cluster cost, by itself, does not repay the complete preceding zero-cost length `L` under that reset convention.

This is an important DSD distinction between

- a genuine transition deficit, and
- inherited prefix debt introduced by the chosen local accounting origin.

## 6. Structural consequence

For `r=10`, write the local surplus as

\[
\epsilon_{10}
:=\mathcal P_{10}-\lambda h_{10}.
\]

Then universally

\[
\boxed{
\epsilon_{10}>\frac{577}{3018}.
}
\]

The complete macro reduced cost is

\[
\mathcal P_{10}-\lambda(L+h_{10})
=\epsilon_{10}-\lambda L.
\]

Therefore the only possible negative part is the inherited prefix term

\[
\boxed{\lambda L.}
\]

The `r=10` problem should no longer be described as a low-penalty ten-paid cluster problem.

It is now a **prefix-debt / resolution / terminal-address coupling problem**.

## 7. Coupling to MATH-074 and MATH-183

MATH-074 supplies the resolution potential

\[
H_R=-\lambda R
\]

and shows that exact symbolic refinement can pay for shortcut length by consuming source-resolution bits.

MATH-183 supplies an independent terminal threshold mechanism that can strictly reduce `R` without enumerating the source anchors.

Therefore the next proof-facing quantity should retain the Bellman balance across the paid-exit boundary instead of resetting it:

\[
\boxed{
\mathcal B
=\mathcal P
-\lambda K
+H_R
}
\]

up to the fixed initial/terminal normalization already allowed by MATH-060.

The required next theorem is not another `r=10` source closure. It is an exact transfer identity/inequality showing how much of the prefix debt `lambda L` is already represented by the change in resolution potential and exact address state at the paid-exit boundary.

## 8. General observation

The same argument gives, for any paid count `r`,

\[
\mathcal P_r-\lambda h_r
>
\frac r{12}
-\lambda\bigl(r+2+m(r)\bigr).
\]

This becomes positive already for the relevant higher multi-paid counts; the exact phase-aware bound can strengthen it further.

This explains why the increasingly difficult low-`r` finite AP workloads should not automatically be interpreted as worsening local paid dynamics. Much of the difficulty comes from how long an exact address family must be carried before the terminal handoff is certified.

## 9. Claim boundary

Established:

- every `r=10` paid cluster has strictly positive local reduced cost at slope `19/503`;
- the exact universal surplus is greater than `577/3018`;
- the MATH-065 negative-cell condition contains the preceding zero-cost prefix `L`, so it is not a statement of negative local `r=10` drift;
- the `r=10` structural bottleneck is relocated to prefix debt plus resolution/address handoff.

Not established:

- a transfer theorem paying the entire prefix debt from resolution/address potential;
- uniform MATH-183 `kappa>=1` for all residual `r=10` states;
- the singleton terminal theorem;
- `r=10` closure;
- first-cell emptiness;
- the Collatz conjecture.
