# MATH-076 — weighted correction/address merge credit through depth 32

Date: 2026-09-12

Status: `EXACT IDENTITY / FINITE EXACT DEPTH-32 MERGE AUDIT / GLOBAL ORDER OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note does not close `2<=r<=13`.
- The purpose is to unify the depth-Hensel correction coordinate and exact dyadic address at endpoint collisions.

## 1. Common-coordinate setup

At depth `k`, write

\[
2^k y = 3^q r + C,
\qquad
S=\frac{C}{3^q},
\qquad
\rho=\frac{2^k}{3^q}.
\]

Then

\[
\boxed{\rho y=r+S}.
\]

Take two depth-`k` states `L,H` with

\[
q_H=q_L+d,\qquad d\ge0.
\]

Define the aligned correction credit

\[
\boxed{
\Gamma_d:=3^dS_H-S_L
=\frac{C_H-C_L}{3^{q_L}}.
}
\]

Define the aligned address credit

\[
\boxed{
A_d:=r_L-3^dr_H.
}
\]

Because `rho_L=3^d rho_H`, subtraction of the two state equations gives

\[
\boxed{
\Gamma_d-A_d
=\rho_L(y_H-y_L).
}
\]

This is an algebraic identity, not a finite-depth observation.

## 2. Endpoint merge condition

At a common endpoint,

\[
y_H=y_L,
\]

and therefore

\[
\boxed{
\Gamma_d=A_d.
}
\]

For `d=1`, this recovers the old merge contrast

\[
G=r_L-3r_H,
\]

but now also gives

\[
\boxed{G=3S_H-S_L}.
\]

More generally, every cross-`q` merge has exact weighted credit

\[
\boxed{
G_d=r_L-3^dr_H=3^dS_H-S_L.
}
\]

## 3. Relation to fixed-q Hensel credit

For `d=0`,

\[
\boxed{
(S_H-S_L)-(r_L-r_H)=\rho(y_H-y_L).
}
\]

MATH-051/MATH-072 identify integer `S` differences at fixed `(k,q)` as exact Hensel translation credits.

The present identity shows why Hensel integrality alone is not actual endpoint compatibility: the dyadic-address credit must match the correction credit.

Thus the two previously separated DSD coordinates have distinct roles:

- `Gamma_d`: correction/Hensel-side aligned credit;
- `A_d`: exact address-side aligned credit;
- `Gamma_d-A_d`: scaled endpoint residual.

## 4. Exact finite audit through depth 32

The companion certificate independently regenerates the exact coefficient-surviving tree through depth 32 using the canonical recurrence and identifies true first merges by requiring distinct actual lifted predecessors.

It reproduces exactly

\[
\boxed{6996}
\]

true first merges through depth 32.

The generalized weighted-credit table is:

| `d=Delta q` | merge pairs | positive | zero | negative | observed range |
|---:|---:|---:|---:|---:|---:|
| 1 | 4549 | 4549 | 0 | 0 | 2..10 |
| 2 | 2305 | 2305 | 0 | 0 | 8..28 |
| 3 | 141 | 141 | 0 | 0 | 26..70 |
| 4 | 1 | 1 | 0 | 0 | 80 |

Hence every true merge observed through depth 32 satisfies

\[
\boxed{G_d>0}.
\]

Exact histograms are

\[
d=1:\quad 2:4421,\ 6:37,\ 10:91,
\]

\[
d=2:\quad 8:1839,\ 12:344,\ 16:94,\ 20:14,\ 24:13,\ 28:1,
\]

\[
d=3:\quad 26:122,\ 34:8,\ 38:2,\ 42:7,\ 50:1,\ 70:1,
\]

\[
d=4:\quad 80:1.
\]

The first observed depths are:

- `d=1`: depth 7;
- `d=2`: depth 19;
- `d=3`: depth 23;
- `d=4`: depth 32.

No zero or negative weighted credit occurs at any true merge in the audited range.

## 5. Relation to ordered endpoint separation

MATH-020 studies a complementary slice: same final `Q` across adjacent boundary families and obtains strict endpoint ordering through depths 79--81.

The present residual identity shows the shared algebraic skeleton. At fixed `q` (`d=0`), endpoint separation is exactly the sign of

\[
\Gamma_0-A_0.
\]

At an actual cross-`q` merge, the residual vanishes and therefore

\[
\Gamma_d=A_d.
\]

So the two finite phenomena should not be identified, but they are two sections of the same correction/address residual equation.

## 6. DSD consequence

The earlier decomposition

\[
\mathcal A=(\mathcal A_{\rm compat},\mathcal A_{\rm dom})
\]

remains necessary, but these factors are now exactly coupled by

\[
\boxed{
\rho_L\Delta y=\Gamma_d-A_d.
}
\]

This provides a sharper common-state target than treating Hensel dominance and dyadic compatibility as unrelated data.

A natural theorem target is the finite observation

\[
G_d>0
\]

for true first merges, equivalently

\[
C_H>C_L
\]

when `q_H>q_L`, but MATH-076 does **not** prove this globally.

## 7. Claim boundary

Established:

- exact residual identity `Gamma_d-A_d=rho_L(y_H-y_L)`;
- exact merge condition `Gamma_d=A_d`;
- exact regeneration of all 6996 true merges through depth 32;
- positive generalized weighted credit for all observed `Delta q=1..4` merge sectors.

Not established:

- arbitrary-depth positivity of `G_d`;
- absence of future zero/negative weighted credits;
- global endpoint ordering;
- first-cell emptiness;
- Collatz.

## Reproducibility

`collatz/src/2026_09_12_math076_weighted_merge_credit_certificate.cpp`
