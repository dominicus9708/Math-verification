# MATH-179 — joint paid-count / depth phase compression

Date: 2026-09-17

Status: `EXACT STRUCTURAL REDUCTION / NO NEW LAYER CLOSURE CLAIM`

Collatz conjecture remains `OPEN`. The first universal Farey cell remains `OPEN`.

## 1. Purpose

The main target is not to solve one paid-count layer at a time. The target is a common recurrence that can carry

\[
1\le r\le21,
\qquad
2\le k\le41
\]

in one proof-facing state system, while retaining auxiliary data such as phase, slack, Hensel carry, and same-integer dyadic address.

Here `r` is the paid-count layer used by the MATH-065/115 family, while `k` is the global parity-prefix depth used by the MATH-051 depth audit. They must not be identified.

## 2. Common Beatty clock

Put

\[
\theta=\log_2(3/2),
\qquad
m(n)=\lfloor n\theta\rfloor,
\]

and

\[
\tau_n=\frac{3^n}{2^{n+m(n)+1}}\in(1/2,1).
\]

For a normalized phase

\[
\varpi\in(1/2,1],
\]

define the phase step

\[
\varepsilon_j=
\begin{cases}
0,&\varpi_j>3/4,\\
1,&\varpi_j\le3/4,
\end{cases}
\qquad
\varpi_{j+1}=\frac{2^{1+\varepsilon_j}}3\varpi_j.
\]

Then the cumulative extra-even count has the closed form

\[
\boxed{
E_r(\varpi):=\sum_{j=0}^{r-1}\varepsilon_j
=m(r)+\mathbf 1_{\{\varpi\le\tau_r\}}.
}
\]

Equivalently,

\[
\boxed{
\varpi_r
=\varpi\frac{2^{r+E_r(\varpi)}}{3^r}.
}
\]

Thus the entire epsilon prefix through paid count `r` is controlled by the same Beatty thresholds already used by MATH-058R.

## 3. Local paid-cluster length

MATH-065 starts the paid-cluster transducer at slack `u=1`. Every paid odd contributes one step and changes slack by `+eps_j`; every even shortcut contributes one step and changes slack by `-1`. A first return to `u=0` after `r` paid odds therefore uses

\[
1+E_r(\varpi)
\]

even shortcuts. Hence its local step length is

\[
\boxed{
h_r(\varpi)
=r+1+E_r(\varpi)
=r+1+m(r)+\mathbf 1_{\{\varpi\le\tau_r\}}.
}
\]

For each fixed `r`, there are only two possible local lengths:

\[
\boxed{
h_r\in\{r+1+m(r),\ r+2+m(r)\}.}
\]

This removes the need to rediscover `hcl=r+1+sum(eps)` separately in every target-r run.

For `1<=r<=21`, the largest local first-return length is 35. This local length is not the MATH-051 global depth `k`.

## 4. Non-iterated future phase

For any `j>=1`,

\[
E_j(\varpi)=m(j)+\mathbf 1_{\{\varpi\le\tau_j\}},
\]

so every future phase value can be read directly as

\[
\boxed{
\varpi_j
=\varpi\frac{2^{j+m(j)+\mathbf 1_{\{\varpi\le\tau_j\}}}}{3^j}.
}
\]

The individual epsilon bit can therefore be recovered without iterative phase propagation:

\[
\boxed{
\varepsilon_j=E_{j+1}(\varpi)-E_j(\varpi).
}
\]

This is the phase-side compression needed by a single `r=1..21` executor.

## 5. Global depth / slack identity

For a global parity prefix of depth `k`, odd count `q`, and even count

\[
d=k-q,
\]

define

\[
\Omega_q=\frac{2^{q+m(q)}}{3^q},
\qquad
u=m(q)-d.
\]

Then

\[
\boxed{
k=q+m(q)-u}
\]

and

\[
\boxed{
\rho:=\frac{2^k}{3^q}=2^{-u}\Omega_q.
}
\]

For `2<=k<=41`, the coefficient condition

\[
3^q\ge2^k
\]

is exactly equivalent to

\[
\boxed{u\ge0.}
\]

The certificate finds 338 coefficient-valid `(k,q)` outer states in the depth window `2..41`.

## 6. Keep the two carry channels distinct

The MATH-051 bounded Hensel carry and the MATH-091/096 same-integer address carry arise from related exact divisibility constraints, but they are not numerically identified.

The joint state must therefore keep them in parallel. The common coordinates that may be shared are the odd count / scale clock, dyadic resolution, and exact affine source/address data.

A proof-facing state should have the schematic form

\[
\mathscr S=
(k,q,u_{\rm H},\mathcal H;
 r,u_{\rm P},\varpi;
 B,Q,M,X,G),
\]

where `H` denotes the depth-41 Hensel carry channel and `(B,Q,M,X,G)` is the MATH-091/096 exact address channel.

No quotient is allowed to merge `u_H` with the paid-macro slack or to merge the two carry channels without a separate exact equivalence proof.

## 7. Consequence for the next executor

The next executor should not call `classify_cells(r)` independently for every `r`.

Instead it should:

1. refine each paid-exit phase source once by all next `21` exact phase cuts;
2. compute the common closed-form sequence `E_j`, `eps_j`, and `h_j` for that cell;
3. run one exact dyadic first-return tree from `u=1`;
4. tag each first return by its paid count `r` and local depth `h_r`;
5. preserve the same-integer affine address state exactly;
6. apply the cost/closure criterion to the tagged terminal layer;
7. later take the product with the MATH-051 bounded-carry channel rather than collapsing the two carry systems.

Thus `r=1..21` becomes one common transducer instead of 21 separate target-r calculations.

## 8. Reproducibility

Exact certificate:

`collatz/src/2026_09_17_math179_joint_r21_depth41_phase_certificate.py`

It audits all 22 phase cells induced by `tau_1..tau_21`, every paid count `1..21`, and all coefficient-valid `(k,q)` states for global depths `2..41`.

Expected output includes:

- `phase_cells=22`
- `paid_count_range=1..21`
- `global_depth_range=2..41`
- `coefficient_valid_(k,q)_states=338`
- `NO NEW LAYER CLOSURE CLAIM`
