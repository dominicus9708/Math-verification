# Backward max-slack projective quotient

Status: **EXACT / CLOSED for suffix-existence feasibility**

Regression guard:

- `../src/A0_s1_routeB_backward_max_slack_projective_quotient_certificate.py`

## Setup

For equal-count target/candidate ranked one-positions

\[
a_1<\cdots<a_q,
\qquad
b_r\le a_r,
\]

index the last ranked ones from the right:

\[
A_t=a_{q-t},
\qquad
B_t=b_{q-t}.
\]

Define target capacity and candidate slack

\[
D_t=A_t-(q-t-1),
\qquad
s_t=B_t-(q-t-1).
\]

Exact ordering is

\[
0\le s_t\le D_t,
\qquad
s_{t+1}\le s_t.
\]

At remaining ternary precision `m`, the projective carry gate is

\[
z_t+2^{A_t}-2^{B_t}\equiv0\pmod3,
\]

with successor

\[
z_{t+1}
=
\frac{z_t+2^{A_t}-2^{B_t}}{3}
\pmod{3^{m-1}}.
\]

## Max-slack dominance

Suppose two backward histories reach the **same** projective carry state `z_t` with ordering caps

\[
S_1\le S_2.
\]

The next legal slack sets are

\[
0\le s_t\le\min(D_t,S_i).
\]

Hence every move legal from `S_1` is also legal from `S_2`.

If both histories take the same next slack `s_t`, then they produce the same:

- candidate exponent `B_t`;
- successor carry `z_(t+1)`;
- next ordering cap `s_t`.

Therefore the larger cap contains every future suffix completion available to the smaller cap.

For pure suffix **existence**, all histories at one carry may be merged by retaining only

\[
\boxed{S_{\max}(z_t)=\max\{S:\text{the carry }z_t\text{ is reachable with cap }S\}.}
\]

This is an exact Bellman-style quotient for formation feasibility.

## One-transition cylinder

At remaining precision `m`, the one-step carry bijection gives exponent period

\[
\lambda_m=2\cdot3^{m-1}.
\]

For fixed incoming `z_t`, target exponent `A_t`, and prescribed successor `z_(t+1)`, there is either no legal candidate exponent or exactly one residue class

\[
B_t\equiv\beta\pmod{\lambda_m}.
\]

Since

\[
B_t=(q-t-1)+s_t,
\]

this is equivalently one slack cylinder

\[
s_t\equiv\gamma\pmod{\lambda_m}.
\]

Intersect it with

\[
0\le s_t\le U_t,
\qquad
U_t=\min(D_t,S_{\max}(z_t)).
\]

The transition is empty if the cylinder misses the interval. Otherwise the exact largest successor cap is

\[
\boxed{
s_{\max}
=U_t-((U_t-\gamma)\bmod\lambda_m).
}
\]

provided this value is nonnegative.

Thus one backward layer may be represented as

`carry state -> maximum feasible slack cap`

rather than a set of complete ordering histories.

## What this quotient does not compress

The theorem merges **ordering histories sharing the same carry**.

It does not yet compress the set of distinct projective carry states.

Therefore the remaining G2 problem is not ordering-history explosion; it is symbolic representation of the carry/cylinder family itself.

## DSD separation

Three different notions must remain separate:

1. **formation feasibility** — governed here by `S_max`;
2. **projective observation/carry** — the exact `z` or an exact symbolic chart for it;
3. **physical defect/cost** — governed elsewhere by `P_min` or exact defect data.

A larger feasible slack cap does **not** imply smaller defect or better physical score.

Accordingly, this theorem must not be used to merge histories with different physical-cost labels unless another theorem proves that dominance.

## Audit classification

### EXACT / CLOSED

- nested legal-choice dominance at fixed carry;
- one `S_max` feasibility label per carry;
- exact slack-cylinder intersection for a prescribed carry transition.

### REGRESSION ONLY

The executable certificate compares the quotient to raw ordering histories at small finite horizons. Those comparisons are implementation guards only.

### OPEN

- symbolic compression of the set of projective carry states;
- right-H block recursion using the quotient;
- exact cut-boundary export state;
- forward/backward join to the 14-root physical Bellman front.

### NOT CLAIMED

- defect-cost dominance from slack dominance;
- uniqueness of a carry path;
- closure of any current root;
- Route-B or Collatz closure.
