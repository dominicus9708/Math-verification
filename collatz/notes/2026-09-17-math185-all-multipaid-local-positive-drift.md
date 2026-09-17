# MATH-185 — every multi-paid cluster has positive local reduced-cost drift

Date: 2026-09-17

Status: `EXACT STRUCTURAL LEMMA / r>=2 LOCAL DRIFT POSITIVE / GLOBAL CLOSURE OPEN`

## 1. Statement

Let `r>=2` be the paid count of one exact paid cluster, let `h_r` be its residual shortcut length after the paid-exit boundary, and let `P_r` be its accumulated paid penalty.

At the MATH-060 slope

\[
\lambda=\frac{19}{503},
\]

every such cluster satisfies

\[
\boxed{\mathcal P_r-\lambda h_r>0.}
\]

Thus no multi-paid cluster creates a local Bellman deficit. Any remaining deficit in the low-paid finite layer calculations is inherited from the preceding zero-cost prefix and/or the terminal exact-address handoff.

This does not close a paid-count layer by itself.

## 2. Universal ingredients

Every paid odd event has

\[
p_j=\frac{1-2^{-u_j}}3\,\varpi_j,
\qquad u_j\ge1,
\qquad \frac12<\varpi_j\le1,
\]

so

\[
\boxed{p_j>\frac1{12}.}
\]

Hence

\[
\boxed{\mathcal P_r>\frac r{12}.}
\]

MATH-179 gives

\[
h_r=r+1+m(r)+\mathbf1_{\{\varpi\le\tau_r\}},
\qquad m(r)=\lfloor r\log_2(3/2)\rfloor,
\]

and therefore

\[
\boxed{h_r\le r+2+m(r).}
\]

## 3. Uniform bound for `r>=4`

Use the exact elementary inequality

\[
\left(\frac32\right)^5=\frac{243}{32}<8=2^3.
\]

Therefore

\[
\log_2(3/2)<\frac35
\]

and

\[
m(r)<\frac{3r}{5}.
\]

Thus

\[
h_r<\frac{8r}{5}+2.
\]

Consequently

\[
\mathcal P_r-\lambda h_r
>
\frac r{12}-\frac{19}{503}\left(\frac{8r}{5}+2\right)
=
\frac{691r}{30180}-\frac{38}{503}.
\]

The right side is positive for every integer `r>=4`; at `r=4` it already equals

\[
\boxed{\frac{121}{7545}>0.}
\]

as a strict lower bound.

## 4. The `r=3` case

Here

\[
m(3)=1,
\qquad h_3\le6.
\]

Therefore

\[
\mathcal P_3-\lambda h_3
>
\frac14-6\frac{19}{503}
=
\boxed{\frac{47}{2012}>0.}
\]

## 5. The `r=2` case

The crude `r/12` estimate is slightly too weak, so use the exact two-step phase map.

For entry phase `varpi in (1/2,1]`:

- if `varpi>3/4`, then `varpi_1=2 varpi/3`, so
  \[
  \varpi+\varpi_1>\frac54;
  \]
- if `varpi<=3/4`, then `varpi_1=4 varpi/3`, so
  \[
  \varpi+\varpi_1>\frac76.
  \]

Thus universally

\[
\varpi+\varpi_1>\frac76.
\]

Since each paid atom at slack at least one is at least its phase divided by six,

\[
\boxed{\mathcal P_2>\frac7{36}.}
\]

Also

\[
m(2)=1,
\qquad h_2\le5.
\]

Hence

\[
\mathcal P_2-\lambda h_2
>
\frac7{36}-5\frac{19}{503}
=
\boxed{\frac{101}{18108}>0.}
\]

## 6. Consequence for the layer frontier

Therefore

\[
\boxed{
\forall r\ge2:\quad
\mathcal P_r>\frac{19}{503}h_r.
}
\]

In particular the observed growth of exact AP/source workloads as `r` decreases from 11 to 10 and below cannot be interpreted as the paid cluster itself crossing into negative local drift.

The structural bottleneck is instead

\[
\boxed{
\text{zero-cost prefix debt}
+\text{exact compatibility/address handoff}
+\text{singleton/aperiodic terminal control}.
}
\]

This agrees with MATH-061, MATH-074, MATH-081, MATH-182, MATH-183, and MATH-184:

- exact macro composition consumes dyadic source resolution without ordinary-source branching;
- multi-source symbolic refinement is Bellman-safe until resolution overshoot;
- terminal non-descent inside a fixed affine cylinder is an ordered prefix;
- resolution can be reduced by exact midpoint inequalities;
- once the accounting origin is not reset, the paid part itself contributes positive drift.

## 7. Mainline target after this lemma

The remaining non-enumerative theorem should no longer depend materially on the paid count `r>=2` except through transition legality.

A natural target is a boundary-transfer potential `H` on

\[
(\Omega,\rho,S,R,\mathcal A_{compat},\mathcal A_{dom})
\]

such that the zero-cost prefix and terminal handoff satisfy

\[
\boxed{
-\lambda L+\Delta H\ge-\epsilon
}
\]

where the strictly positive multi-paid local surplus absorbs the remaining bounded `epsilon`.

If this is established uniformly, the separate finite layer computations `r=2,3,...` become regression/cross-audit data rather than proof premises.

## 8. Claim boundary

Established:

- every exact multi-paid cluster `r>=2` has positive local reduced-cost drift at slope `19/503`;
- `r=2` is covered by an exact two-phase bound, not numerical sampling;
- low-`r` difficulty is therefore relocated to prefix/address/terminal structure.

Not established:

- the boundary-transfer potential;
- uniform terminal singleton closure;
- any new paid-count layer closure;
- first-cell emptiness;
- the Collatz conjecture.
