# MATH-077 — first-crossing penalty/address order through depth 26

Date: 2026-09-12

Status: `EXACT RESIDUAL / FINITE ORDER AUDIT / GLOBAL ORDER OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note does not close `2<=r<=13`.

## 1. Mechanical envelope in the current coordinates

For a first coefficient crossing at depth `j`, all admissible words have the same final odd count

\[
q_j=k_j-1.
\]

The existing mechanical-envelope theorem proves that the unique Beatty/mechanical boundary word `m` maximizes the affine correction `C` among all such crossing words.

Because `q` is fixed in the layer, it also uniquely maximizes

\[
\boxed{S=C/3^q}.
\]

Thus the mechanical envelope is the exact top boundary for normalized correction in a fixed first-crossing layer.

## 2. Penalty is the correction deficit

The later penalty formulation gives

\[
S(w)=S_\partial-\mathcal P(w).
\]

For the mechanical boundary reference `m`, this means

\[
\boxed{\mathcal P(w)=S_m-S_w\ge0.}
\]

So the paid penalty is not an arbitrary score. It is the exact normalized-correction deficit from the extremal mechanical envelope.

## 3. Address displacement

Let

\[
\Delta r=r_w-r_m.
\]

At fixed `(j,q)`, MATH-076 with `d=0` gives

\[
\boxed{
\rho(y_m-y_w)=\mathcal P(w)-\Delta r,
\qquad
\rho=\frac{2^j}{3^q}.
}
\]

Equivalently, without fractions,

\[
\boxed{
2^j(y_m-y_w)
=(C_m-C_w)-3^q(r_w-r_m).
}
\]

This is the exact two-place balance left implicit by the older mechanical-envelope theorem:

\[
\boxed{
\text{correction deficit}-\text{dyadic address displacement}
=\text{scaled endpoint separation}.
}
\]

## 4. Finite exact regression through depth 26

The companion certificate regenerates the coefficient-surviving tree and extracts every first coefficient crossing through depth 26.

Including the trivial crossings at depths 1 and 2, the exact total is

\[
\boxed{190069}.
\]

The older depth-26 crossing table starts at depth 4 and therefore lists 190067 nontrivial candidates; the two totals are consistent.

For every crossing depth in the audited range:

- the mechanical candidate is the unique maximum-`C` / maximum-`S` word;
- the residual identity above holds exactly;
- there is no nontrivial candidate sharing the mechanical endpoint;
- endpoint order has the same sign as address order:

\[
\boxed{
\operatorname{sgn}(y_w-y_m)
=
\operatorname{sgn}(r_w-r_m).
}
\]

The aggregate audit returns:

\[
\boxed{
\text{envelope failures}=0,
\quad
\text{residual failures}=0,
\quad
\text{order failures}=0,
\quad
\text{nontrivial equal endpoints}=0.
}
\]

## 5. Interpretation of the sign result

If `Delta r<0`, then

\[
\mathcal P-\Delta r>0
\]

is automatic because `P>=0`. Therefore

\[
y_w<y_m.
\]

The nontrivial side is `Delta r>0`. The finite exact result says

\[
\boxed{
\mathcal P(w)<\Delta r
}
\]

for every such crossing candidate through depth 26. Hence the positive dyadic-address displacement dominates the loss in normalized correction and forces

\[
y_w>y_m.
\]

This quantifies the older statement that a smaller remainder and a shifted dyadic start must be considered together.

## 6. Relation to MATH-076 and ordered separation

MATH-076 gives the general residual

\[
\Gamma_d-A_d=\rho_L\Delta y.
\]

MATH-077 is the same-`q` mechanical-reference specialization

\[
\Gamma_0=\mathcal P,
\qquad
A_0=\Delta r,
\]

up to the chosen orientation.

The depth-79--81 ordered-separation results are therefore structurally compatible with the same residual architecture, although they use different block/boundary families and are not a direct continuation of the depth-26 first-crossing sample.

## 7. Claim boundary

Established:

- exact mechanical maximum in every finite crossing layer checked through depth 26;
- exact penalty/address residual;
- exact endpoint/address sign agreement for all 190069 crossing candidates through depth 26.

Not established:

- arbitrary-depth sign agreement;
- a uniform lower bound on `Delta r-P` for positive address displacement;
- first-cell closure;
- closure of `2<=r<=13`;
- Collatz.

## Reproducibility

`collatz/src/2026_09_12_math077_firstcrossing_penalty_address_certificate.cpp`
