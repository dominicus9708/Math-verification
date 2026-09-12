# MATH-080 — master affine comparison defect

Date: 2026-09-12

Status: `EXACT MASTER COMPARISON IDENTITY / COMMON FORMULA CANDIDATE / GLOBAL INEQUALITY OPEN`

## 1. Motivation

MATH-076 generalized endpoint merge credit, MATH-077 unified descent and first-crossing occupancy, MATH-078 identified old long-depth envelopes as `S` envelopes, and MATH-079 separated exact address contrast from correction credit.

All of those relations are projections of one affine comparison identity.

The Collatz conjecture and first universal Farey cell remain `OPEN`.

## 2. Affine state

Represent an exact Collatz affine state by

\[
X=(a,S,\rho)
\]

with endpoint

\[
\boxed{
y(X)=\frac{a+S}{\rho}.
}
\]

For a parity prefix, `a` is the exact ordinary/canonical source coordinate, `S=C/3^q`, and `rho=2^k/3^q`.

## 3. Master comparison defect

For two affine states

\[
X_1=(a_1,S_1,\rho_1),
\qquad
X_2=(a_2,S_2,\rho_2),
\]

define

\[
\boxed{
\mathfrak D(X_1,X_2)
:=
\rho_2(a_1+S_1)
-
\rho_1(a_2+S_2).
}
\]

Since `a_i+S_i=rho_i y_i`,

\[
\boxed{
\mathfrak D(X_1,X_2)
=
\rho_1\rho_2(y_1-y_2).
}
\]

Because both `rho_i` are positive:

\[
\boxed{
\mathfrak D=0\iff y_1=y_2,
}
\]

and the sign of `mathfrak D` is exactly the endpoint order.

The defect is antisymmetric:

\[
\mathfrak D(X_1,X_2)=-\mathfrak D(X_2,X_1).
\]

## 4. MATH-079 as a scaled specialization

At common depth, let

\[
q_H=q_L+d.
\]

Then

\[
\rho_H=\rho_L/3^d.
\]

For the low-`q` state `L` and high-`q` state `H`,

\[
\mathfrak D(L,H)
=
\frac{\rho_L}{3^d}
\left[
(r_L-3^dr_H)-(3^dS_H-S_L)
\right].
\]

Thus MATH-079's

\[
A_d-C_d
\]

is simply the master comparison defect multiplied by the positive scale `3^d/rho_L`.

MATH-076 endpoint merge is the zero-defect case.

## 5. Orbit gap as comparison with the identity reference

For an ordinary start `N`, take the path state

\[
X=(N,S,\rho)
\]

and the identity/reference state

\[
X_0=(N,0,1),
\qquad
y(X_0)=N.
\]

Then

\[
\boxed{
\mathfrak D(X,X_0)
=S-N(\rho-1).
}
\]

But MATH-077 gives

\[
T^k(N)-N
=\frac{S-N(\rho-1)}{\rho}.
\]

Therefore

\[
\boxed{
\mathfrak D(X,X_0)
=\rho[T^k(N)-N].
}
\]

So strict descent is simply

\[
\boxed{
\mathfrak D(X,X_0)<0.
}
\]

This places endpoint collision/order and self-descent in exactly the same comparison formalism.

## 6. Terminal first-cell defect

MATH-053 writes the normalized correction as

\[
S=S_{\partial}-\mathcal P.
\]

At a first-cell terminal state,

\[
\boxed{
\mathfrak D_{\rm term}
=
S_{\partial}-\mathcal P-N(\rho-1).
}
\]

A hypothetical non-descending bad terminal path must satisfy

\[
\mathfrak D_{\rm term}\ge0,
\]

equivalently

\[
\mathcal P
\le
S_{\partial}-N(\rho-1).
\]

This is exactly the MATH-060 bad-path penalty upper condition.

Therefore the proof-facing penalty problem can be stated as:

\[
\boxed{
\text{force }\mathfrak D_{\rm term}<0
\text{ by proving enough accumulated penalty.}
}
\]

The optimized Bellman slope `19/503` is a sufficient quantitative route to that sign change under the current first-cell envelope and additive overhead.

## 7. Role of resolution potential

MATH-073/074 introduced the source-resolution height

\[
R_{\rm res}=\lceil\log_2M\rceil
\]

and potential

\[
H_R=-\lambda R_{\rm res},
\qquad
\lambda=19/503.
\]

Its role is not to replace `mathfrak D`. It is a proof device for the penalty lower bound needed to make the terminal master defect negative.

Thus the architecture separates cleanly:

1. `mathfrak D` — exact target sign / compatibility quantity;
2. `P` — accumulated analytic deficit that lowers `S`;
3. `R_res` — address-resolution budget that helps certify enough `P` without enumerating every source;
4. exact address/carry state — determines which transitions are actually compatible.

## 8. Relation to closed paid-count layers

The closures `r>=14` use several representations—block handoff, AP streaming, banded AP union, adaptive AP sharding—but all preserve same-integer address lineage until either:

- the analytic/cost condition is already safe; or
- resolution reaches a singleton, after which the ordinary integer is continued to a strict descent.

In the present language, the latter terminal check is exactly the observation that the ordinary trajectory eventually reaches a prefix with

\[
\mathfrak D(X,X_0)<0.
\]

The finite paid-layer closures therefore fit the master-defect architecture, but they do not prove the global Bellman lower bound.

## 9. Regression

The companion exact-rational certificate regenerates coefficient-surviving canonical states through depth 14.

It checks:

- every unordered state pair: `372,731` comparisons;
- every path state against its own identity/reference start: `1,608` comparisons.

Results:

- pairwise master-defect failures: `0`;
- start-reference orbit-gap failures: `0`.

These finite tests are implementation checks. The identity is algebraic.

## 10. DSD interpretation

The master comparison defect exposes one common pattern behind the recent analyses:

\[
\boxed{
\text{order / compatibility}
=
\text{exact address contribution}
+
\text{normalized correction contribution},
}
\]

with the coefficient ratio `rho` providing the exact cross-layer scale.

It also gives a natural hierarchy:

\[
\text{affine state}
\to
\text{comparison defect}
\to
\text{sign target}
\to
\text{penalty/resolution proof machinery}.
\]

This is a stronger common-formula candidate than treating `theta`, merge `G`, interval bounds, root credit, and terminal `delta N` as independent objects.

## 11. Claim boundary

Established:

- universal master comparison identity;
- exact reduction of merge/order and self-descent to its zero/sign;
- exact recovery of MATH-060 terminal bad-path inequality;
- finite pair/reference regression.

Not established:

- the global `19/503` penalty lower bound;
- a complete finite Bellman quotient;
- arbitrary-depth first-crossing descent;
- first-cell emptiness;
- later-cell coverage;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math080_master_affine_comparison_certificate.py`
