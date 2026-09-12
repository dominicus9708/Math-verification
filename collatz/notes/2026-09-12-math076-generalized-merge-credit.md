# MATH-076 — generalized cross-layer merge credit

Date: 2026-09-12

Status: `EXACT ALGEBRAIC IDENTITY / DEPTH-26 REGRESSION / GLOBAL SIGN OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note does not close `2<=r<=13`.
- The purpose is to unify the old depth-32 first-merge contrast with the fixed-`q` Hensel credit used in MATH-051.

## 1. Common-coordinate form

For a coefficient-surviving canonical state at depth `k`, write

\[
\rho(k,q)=\frac{2^k}{3^q},
\qquad
S=\frac{C}{3^q}.
\]

The canonical endpoint relation is

\[
\boxed{\rho y=r+S}.
\]

Equivalently,

\[
y=\frac{r+S}{\rho}.
\]

## 2. Same-depth endpoint merge across different odd-count layers

Let two states at the same depth `k` have the same endpoint `y`. Order them so

\[
q_H=q_L+d,
\qquad d\ge0.
\]

Then

\[
\rho_H=\frac{\rho_L}{3^d}.
\]

Endpoint equality gives

\[
r_L+S_L=\rho_Ly
=3^d\rho_Hy
=3^d(r_H+S_H).
\]

Therefore

\[
\boxed{
G_d:=r_L-3^d r_H
=3^dS_H-S_L.
}
\]

This is exact for every same-depth common-endpoint pair; no finite-depth assumption is used in the derivation.

For `d=1`, this reduces to the old integrated DSD contrast

\[
G=r_L-3r_H.
\]

Thus the old `Delta Q=1` quantity was the first member of a general family rather than an isolated diagnostic.

## 3. Sigma form

MATH-072 established

\[
S=1+\Sigma-\rho.
\]

Substitute this into the generalized merge credit:

\[
3^dS_H-S_L
=3^d(1+\Sigma_H-\rho_H)
 -(1+\Sigma_L-\rho_L).
\]

Since `rho_L=3^d rho_H`, the coefficient-ratio terms cancel exactly, giving

\[
\boxed{
G_d=(3^d-1)+3^d\Sigma_H-\Sigma_L.
}
\]

This is the direct algebraic bridge between the endpoint-merge channel and the depth-Hensel signature channel.

## 4. Relation to fixed-q Hensel credit

For `d=0`,

\[
\boxed{
G_0=r_L-r_H=S_H-S_L=\Sigma_H-\Sigma_L.
}
\]

MATH-051 tests integer translation differences `Delta Sigma` inside fixed `(k,d_even)` layers by a bounded-carry automaton. Therefore the fixed-layer Hensel credit and the cross-layer endpoint merge credit use the same normalized-correction coordinate.

This does **not** mean every Hensel comparison is an endpoint merge. It means that once the relevant equality/translation condition is imposed, both channels measure their exact credit in the same `S/Sigma` coordinate.

## 5. Mod-4 consequence

When both canonical start residues in the merge sector satisfy

\[
r_L\equiv r_H\equiv3\pmod4,
\]

then

\[
G_d=r_L-3^dr_H
\]

obeys

\[
\boxed{
 d\text{ odd}\Rightarrow G_d\equiv2\pmod4,
}
\]

\[
\boxed{
 d\text{ even}\Rightarrow G_d\equiv0\pmod4.
}
\]

This is an arithmetic consequence, not a fitted pattern.

## 6. Exact finite regression through depth 26

The companion certificate regenerates the coefficient-surviving canonical tree through depth 26 and uses the corrected true-first-merge definition: equal current endpoint but different actual predecessor immediately before the last branch.

It finds cumulatively

\[
\boxed{388}
\]

true first merges, distributed as

\[
d=1:243,
\qquad
d=2:136,
\qquad
d=3:9.
\]

Every one satisfies both exact forms

\[
G_d=r_L-3^dr_H=3^dS_H-S_L
\]

and

\[
G_d=(3^d-1)+3^d\Sigma_H-\Sigma_L.
\]

Identity failures: `0`.

In this finite range all 388 credits are positive. Their observed ranges are

\[
G_1\in[2,6],
\qquad
G_2\in[8,12],
\qquad
G_3=26.
\]

The sign/range observations are finite evidence only. They are **not** upgraded to a theorem that `G_d>0` at arbitrary depth.

## 7. DSD interpretation

The generalized credit separates four layers that must not be conflated:

1. **formation:** two coefficient-admissible canonical states exist;
2. **compatibility:** they belong to the same depth and reach the same endpoint;
3. **credit:** endpoint equality forces the exact integer relation `G_d=3^dS_H-S_L`;
4. **ordering:** the sign of `G_d` is a further property and is not implied by the identity alone.

The gain is a state reduction: the old merge quantity does not require a new independent coordinate once exact address lineage and `(S,q)` are retained.

## 8. Claim boundary

Established:

- universal generalized merge-credit identity;
- exact `Sigma` representation;
- conditional mod-4 consequence;
- depth-26 true-merge regression with 388 cases and zero identity failures.

Not established:

- global positivity of `G_d`;
- exclusion of all bad cross-layer merges;
- first-cell emptiness;
- closure of `2<=r<=13`;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math076_generalized_merge_credit_certificate.py`
