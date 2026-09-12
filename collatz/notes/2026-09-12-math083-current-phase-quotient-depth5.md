# MATH-083 — current-phase quotient for one-paid terminal handoffs through macro depth 5

Date: 2026-09-12

Status: `EXACT FINITE / DEPTH-4 AND DEPTH-5 TERMINAL BELLMAN CLOSURE / MULTI-SOURCE CHAINS REMAIN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-082 certified the resolution-bit Bellman wedge through macro depth 3.
- This note re-coordinates the exact MATH-061 composition and extends the analytic terminal audit through macro depth 5.

## 1. Current-phase sufficient state

MATH-061 writes a composed path using an initial source phase `Omega_0`, a cumulative scale `rho`, and an accumulated penalty coefficient `beta`:

\[
\Omega_{\rm cur}=\rho\Omega_0,
\qquad
\mathcal P=\beta\Omega_0.
\]

Define instead

\[
\boxed{
J=(\Omega^-_{\rm cur},\Omega^+_{\rm cur}),
\qquad
\alpha=\frac{\beta}{\rho}.
}
\]

Then throughout the current interval,

\[
\boxed{\mathcal P=\alpha\Omega_{\rm cur}.}
\]

For one exact one-paid macro edge `e`,

\[
\rho_e=\frac{2^{h_e}}{3^{q_e}},
\]

and direct reduction of the canonical MATH-059 data gives

\[
\boxed{
\frac{\beta_e}{\rho_e}\in\left\{\frac14,\frac18\right\}.
}
\]

If its source-phase domain is `I_e`, composition is therefore

\[
K=J\cap I_e,
\]

\[
\boxed{J'=\rho_eK,}
\]

\[
\boxed{
\alpha'=\frac{\alpha}{\rho_e}+c_e,
\qquad
c_e\in\left\{\frac14,\frac18\right\}.
}
\]

This is an exact change of coordinates, not a relaxation.

## 2. Address channel remains exact

The dyadic compatibility condition is unchanged.  For a current state

\[
Y'=B+3^Q s
\]

and a next edge with source anchor `A_e` and resolution `2^h`, the parameter residue is

\[
\boxed{
r\equiv(A_e-B)3^{-Q}\pmod{2^h}.
}
\]

The edge exists only when

\[
r<\text{count}.
\]

The child source multiplicity is exactly

\[
\boxed{
\left\lfloor\frac{\text{count}-1-r}{2^h}\right\rfloor+1.
}
\]

Thus the phase quotient only removes redundant phase history.  It does not remove the dyadic address channel identified as necessary in MATH-079.

## 3. Computational quotient

At macro depth 4 there are exactly

\[
\boxed{442,957}
\]

multi-source ordinary-address states.

Their current-phase continuation queries collapse to fewer than one hundred current-phase interval plans in the exact implementation.  Each plan lists only phase-compatible one-paid edges; each actual ordinary-address state then applies the unchanged congruence test.

This reduces the expensive inner loop from repeated full 910-edge phase arithmetic to a shared phase-geometry lookup followed by exact address masking.

## 4. Macro depth 4

The exact depth-4 handoff counts are

\[
\boxed{76,585\text{ singleton terminals}},
\qquad
\boxed{442,957\text{ multi-source states}}.
\]

The MATH-082 universal resolution wedge certifies

\[
\boxed{76,564}
\]

of the singleton terminals without using the exact phase interval.

The remaining 21 terminals are certified by

\[
\mathcal P_{\inf}=\alpha\Omega^-_{\rm cur}
\]

against

\[
\frac{19}{503}(H-73).
\]

Hence

\[
\boxed{76,585/76,585}
\]

depth-4 terminal handoffs are Bellman-safe and

\[
\boxed{0}
\]

ordinary terminal continuations are required for this reduced-cost claim.

The largest terminal resolution depth is

\[
\boxed{H=84}.
\]

Every retained multi-source state has

\[
\boxed{H\le71}.
\]

## 5. Macro depth 5

Exact continuation of all 442,957 depth-4 multi-source states gives

\[
\boxed{372,841\text{ singleton terminals}}
\]

and

\[
\boxed{1,689,024\text{ multi-source states}}.
\]

The universal phase-free wedge alone certifies

\[
\boxed{372,834}.
\]

Only seven terminals lie outside that coarse sufficient condition:

\[
\boxed{6\text{ at }H=85},
\qquad
\boxed{1\text{ at }H=87}.
\]

All seven have positive exact current-phase reduced-cost infimum. Therefore

\[
\boxed{372,841/372,841}
\]

depth-5 terminal handoffs are Bellman-safe and again

\[
\boxed{0}
\]

ordinary terminal continuations are required.

The maximum terminal depth is

\[
\boxed{H=87}.
\]

Every depth-5 multi-source state still satisfies

\[
\boxed{H\le71}.
\]

## 6. What this establishes

Through macro depth 5, every newly resolved one-paid singleton handoff is eliminated from the low-cost bad-path search by one of two analytic tests:

1. the phase-free resolution wedge;
2. the exact current-phase penalty infimum.

The previous pattern

\[
\text{symbolic multi-source state}
\to
\text{singleton}
\to
\text{ordinary continuation}
\]

has therefore become, for depths 4 and 5,

\[
\boxed{
\text{symbolic multi-source state}
\to
\text{singleton}
\to
\text{analytic Bellman closure}.
}
\]

This is a real reduction in proof-facing calculation, not merely a faster implementation of the same terminal trajectory checks.

## 7. What remains open

The result does **not** prove that all one-paid chains are closed.  There remain

\[
\boxed{1,689,024}
\]

multi-source states at macro depth 5.

Nor does Bellman safety of a terminal handoff, by itself, assert an ordinary Collatz descent theorem for that integer.  The claim is that such a handoff cannot realize the low-cost path required by the current MATH-060 first-cell contradiction program.

Still open:

- an all-depth one-paid Bellman closure;
- the remaining multi-paid frontier `2<=r<=13`;
- the mixed one-paid / multi-paid Bellman problem;
- first universal Farey-cell emptiness;
- later cells;
- the Collatz conjecture.

## 8. Next route

The preferred next calculation is no longer raw depth-6 materialization.

Use the current-phase state

\[
(J,\alpha,H,Q)
\]

as the analytic quotient, while preserving only the minimum exact dyadic address data required for the congruence channel.

The target is an exact streaming depth-6 audit and, in parallel, a dominance rule on current-phase states that can replace repeated macro-depth expansion by a finite Bellman certificate.

## Reproducibility

Certificate:

`collatz/src/2026_09_12_math083_current_phase_quotient_depth5_certificate.py`

Commit:

`a3fc5533b1f5ee0de9897e97b49a5a128db19dc7`
