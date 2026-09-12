# MATH-091 — carry-transfer transducer for exact one-paid composition

Date: 2026-09-12

Status: `EXACT REFORMULATION / COMMON ADDRESS-STATE TRANSITION`

## 1. Parent and edge

Write an exact current family as

\[
Y'=B+3^Q s,
\qquad0\le s<M.
\]

A canonical next macro has source and target families

\[
Y=A_e+2^h t,
\]

\[
Y_{out}=B_e+3^{q_e}t.
\]

## 2. Residue and carry

Compatibility fixes

\[
\boxed{
r\equiv(A_e-B)(3^Q)^{-1}\pmod{2^h},
\qquad0\le r<2^h.
}
\]

If `r>=M`, the edge is absent.
Otherwise write

\[
s=r+2^h u.
\]

Define the exact integer carry

\[
\boxed{
d=\frac{B+3^Qr-A_e}{2^h}.}
\]

Then the edge source parameter is

\[
t=d+3^Q u.
\]

## 3. Exact child state

Substitution into the edge target gives

\[
Y_{out}
=B_e+3^{q_e}d+3^{Q+q_e}u.
\]

Hence the exact child state is

\[
\boxed{
Q'=Q+q_e,
\qquad
B'=B_e+3^{q_e}d,
}
\]

with source count

\[
\boxed{
M'
=
\left\lfloor\frac{M-1-r}{2^h}\right\rfloor+1.
}
\]

This is exactly the MATH-061 composition law written as a residue/carry state transition.

## 4. Relation to MATH-090

MATH-090 studies the terminal case by solving first at resolution

\[
R=\lceil\log_2M\rceil
\]

and asking whether the carry has enough 2-adic divisibility to keep all additional lift bits zero.

MATH-091 shows why this carry is structurally central: whenever composition continues, the quotient carry is not discarded.  It is transported directly into the next affine intercept `B'`.

Thus the exact address computation is an iterative transducer

\[
\boxed{
(B,Q,M)
\xrightarrow{\text{edge}}
(r,d)
\xrightarrow{}
(B',Q',M').
}
\]

## 5. Common-state interpretation

This gives a common language for the two carry-based calculations now in the project:

- depth-41 bounded carry compresses Hensel dominance/translation;
- MATH-090/091 carry compresses same-integer dyadic compatibility and transports the surviving address state.

They are not numerically identified, but both are finite carry transducers arising from exact divisibility constraints.

## 6. Next target

The remaining one-paid Bellman frontier is macro depth `7..16`.
The next compression target is therefore not raw depth extension but a quotient of the MATH-091 transducer that retains only:

1. source resolution `R_res`;
2. the carry bits needed by MATH-090;
3. current phase cell;
4. current Bellman cost descriptor.

Such a quotient would be the direct analogue of the depth-41 bounded-carry finite-state compression.
