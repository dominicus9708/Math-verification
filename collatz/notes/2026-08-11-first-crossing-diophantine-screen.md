# Diophantine screening of first-crossing danger layers

Date: 2026-08-11

Status: **derived analytic screening bound**. This is an auxiliary estimate for the first-crossing boundary and not a proof of CST or Collatz.

Let

\[
\beta=\log_2 3,
\qquad
\kappa(q)=\lfloor q\beta\rfloor,
\]

and define the distance from \(q\beta\) to the next integer by

\[
\boxed{
\delta_q:=\lceil q\beta\rceil-q\beta
=\kappa(q)+1-q\beta.
}
\]

Then the first-crossing coefficient gap is

\[
D_q
:=
2^{\kappa(q)+1}-3^q
=
3^q(2^{\delta_q}-1).
\]

From the survival-envelope estimate

\[
R_q^*<q3^{q-1},
\]

the structural danger threshold

\[
H_q=\frac{R_q^*}{D_q}
\]

satisfies

\[
\boxed{
H_q
<
\frac{q}{3(2^{\delta_q}-1)}
<
\frac{q}{3\ln2\,\delta_q}.
}
\]

Therefore large first-crossing thresholds can occur only when \(q\log_2 3\) lies unusually close to an integer from below, or equivalently when

\[
\frac{\lceil q\log_2 3\rceil}{q}
\]

is an unusually good upper rational approximation to \(\log_2 3\).

This gives a screening principle: crossing layers with ordinary Diophantine gap \(\delta_q\) have a small explicit danger threshold and should be discharged by a lower bound on the realizable crossing frontier; only near-approximation layers need refined arithmetic treatment.

A quantitative continued-fraction consequence follows from Legendre's criterion. If

\[
H_q\ge \frac{2}{3\ln2}q^2,
\]

then the preceding upper bound forces

\[
\delta_q<\frac1{2q},
\]

and hence

\[
0<
\frac{\lceil q\beta\rceil}{q}-\beta
<\frac1{2q^2}.
\]

Thus the rational \(\lceil q\beta\rceil/q\) must be a continued-fraction convergent of \(\beta\) (after reduction if necessary). Less extreme thresholds naturally lead to semiconvergents or neighboring best approximations.

This is consistent with the continued-fraction concentration reported for paradoxical Collatz ratios in recent parity-vector work, but the estimate above is derived directly from the survival-envelope correction bound.

The role of this screen in the unresolved-set program is only auxiliary: it sparsifies the coefficient-boundary layers that can create large bounded post-crossing islands. The master target remains unresolved-channel rank escape.
