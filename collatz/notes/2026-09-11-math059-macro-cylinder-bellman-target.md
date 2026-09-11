# MATH-059 — arithmetic-progression macro cylinders and Bellman target

Date: 2026-09-11
Status: `EXACT CYLINDER COMPRESSION / MATH-058 REGRESSION PASS / EDGEWISE SLOPE TEST REJECTED / GLOBAL BELLMAN BOUND OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This step removes a lift-enumeration layer and corrects the optimization target. It does not prove the required global penalty slope.

## 1. MATH-058 reproducibility repair

The original MATH-058 certificate emitted one paid-exit record for every parity-compatible lift `t`, but `one_paid_outcomes()` then ignored the stored `t` and re-enumerated the full lift interval. This duplicated source cylinders.

The repaired certificate keeps each phase/address source cylinder exactly once and resolves the lift congruence only at the one-paid stage. The canonical table is recovered exactly:

| zero-cost L | one-paid outcomes | can reach another paid macro |
|---:|---:|---:|
| 69 | 20 | 1 |
| 70 | 4 | 0 |
| 71 | 4 | 0 |
| 72 | 0 | 0 |

Thus the numerical MATH-058 conclusion survives; the defect was bookkeeping in the certificate state, not a change in the mathematical bound.

## 2. Direct arithmetic-progression cylinder

For a fixed zero-cost mechanical factor of length `L`, write

\[
Y=R+t2^L.
\]

If that factor contains `q` odd steps, its endpoint before the paid exit is

\[
E=E_0+3^q t.
\]

For an exactly-one-paid cluster, return to `u=0` requires

\[
E\equiv1\pmod4
\]

when the paid odd has `epsilon=0`, or

\[
E\equiv5\pmod8
\]

when `epsilon=1`.

Because `3^q` is invertible modulo powers of two, this is one exact congruence

\[
\boxed{t\equiv\tau\pmod{2^h}},
\qquad h=2\text{ or }3.
\]

Put

\[
t=\tau+2^h s.
\]

After the paid odd and the required recovery-even steps, the next boundary anchor is

\[
\boxed{Y'=Y'_0+3^{q+1}s.}
\]

Thus one cylinder stores the whole lift family without enumerating its members.

For a cylinder with allowed lift interval `t_min<=t<=t_max`, existence and cardinality follow directly from the first/last integer in the congruence class. The same object simultaneously carries

- the exact source phase interval;
- the number of ordinary endpoint lifts;
- the affine output progression;
- the phase multiplier;
- the exact penalty coefficient.

## 3. Exact phase and penalty transport

Let the source phase be `Omega`. On one fixed cylinder the next boundary phase is

\[
\boxed{\Omega'=g_e\Omega}
\]

for an exact positive rational `g_e`.

For the one-paid cylinder the paid event occurs at slack `u=1`, so

\[
\boxed{\mathcal P_e=\beta_e\Omega},
\qquad
\beta_e=\frac{g_{\rm pre}}6.
\]

The penalty objective is therefore affine in the source phase. Bounds over the whole cylinder are obtained at rational interval endpoints rather than by scanning ordinary starts.

## 4. Unique long L=69 transition

The only `L=69` one-paid state that can reach another paid macro is generated from

\[
Y_0=4,271,670,721,469,145,272,313
\]

with source phase interval

\[
\left(
\frac{205891132094649}{281474976710656},
\frac{109418989131512359209}{147573952589676412928}
\right).
\]

It has

\[
\beta_e=
\frac{590295810358705651712}{2954312706550833698643},
\]

and reaches

\[
Y_1=5,344,714,831,606,523,422,699
\]

with phase interval

\[
\left(\frac{8388608}{14348907},\frac{16}{27}\right).
\]

Its total macro length is 71 steps.

## 5. Edgewise slope positivity is rejected

A proposed optimization was to choose a target slope `lambda=17/450` and require every legal macro edge to obey

\[
J_e(\Omega)
=
\beta_e\Omega-\lambda\ell_e>0.
\]

The exact long `L=69` edge disproves this stronger requirement. Over its entire legal phase interval,

\[
J_e(\Omega)<0.
\]

Therefore the correct proof target is not edgewise positivity.

This is a DSD-significant correction: a locally low-cost transition is not equivalent to a globally sustainable low-cost trajectory.

## 6. The long low-cost edge is transient

Exact continuation of the unique long edge gives

\[
71\text{-step one-paid}
\to
3\text{-step one-paid}
\to
10\text{-step four-paid}
\to
\text{coefficient failure}.
\]

The two later boundary anchors are

\[
Y_2=6,012,804,185,557,338,850,537,
\]

\[
Y_3=4,280,599,854,757,128,927,776.
\]

At `Y_3`, the next actual step is even while the state is at `u=0`, so coefficient survival fails immediately.

Thus the unique longest low-cost edge cannot belong to a coefficient-valid low-mean cycle.

## 7. Correct optimization target

For an exact macro state `s` and edge `e:s->s'`, the next target is a Bellman/potential inequality

\[
\boxed{
\mathcal P_e-\lambda\ell_e
+H(s')-H(s)\ge0.
}
\]

Summation along a path telescopes the potential. On a cycle the potential cancels completely, so feasibility is controlled by minimum mean penalty rather than the sign of individual edges.

Equivalently, the proof-facing obstruction is:

\[
\boxed{
\text{no coefficient-valid cycle/path family can sustain mean penalty below }\lambda.
}
\]

Negative individual edges are allowed when they are transient or must be compensated before the path can continue.

## 8. DSD state requirement

The quotient must preserve enough information to determine future legality. At minimum this includes

\[
(\text{phase interval},\text{same-integer endpoint/address lineage},
\text{macro type},\text{min-plus value}).
\]

Exact `S=C/3^q` information may be reused where it replaces redundant real/Hensel/dyadic projections, but a coarse real interval for `S` must not be substituted for exact address lineage.

## 9. Next target

The next step is to derive a global penalty slope sufficient for the first-cell terminal correction inequality, then solve the weighted cylinder graph at that slope. Hensel cross-channel state should be attached only if the phase/address macro graph alone does not reach the required bound.

## Reproducibility

- `collatz/src/2026_09_11_paid_macro_transition_certificate.py` — corrected MATH-058 source-cylinder bookkeeping.
- `collatz/src/2026_09_11_math059_macro_cylinder_certificate.py` — direct cylinder regression, long-edge counterexample, and transient-chain certificate.
