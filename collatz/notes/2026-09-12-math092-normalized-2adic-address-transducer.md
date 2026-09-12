# MATH-092 — normalized 2-adic address transducer

Date: 2026-09-12

Status: `EXACT REFORMULATION / BIT-SHIFT ADDRESS STATE`

## 1. Normalized address

For an exact current family

\[
B+3^Q s,
\qquad0\le s<M,
\]

define the 2-adic normalized intercept

\[
\boxed{X=3^{-Q}B\in\mathbb Z_2.}
\]

For a canonical edge

\[
A_e+2^h t
\longmapsto
B_e+3^{q_e}t,
\]

define

\[
\eta_e(Q)=3^{-Q}A_e,
\qquad
\beta_e(Q)=3^{-(Q+q_e)}B_e.
\]

## 2. Residue selection

The source compatibility residue becomes

\[
\boxed{
r=(\eta_e(Q)-X)\bmod2^h.
}
\]

Thus the repeated multiplication by `(3^Q)^(-1)` is absorbed into the normalized address coordinate.

## 3. Shift-add transition

If `r<M`, then

\[
X+r-\eta_e(Q)
\]

is divisible by `2^h`, and the exact child normalized intercept is

\[
\boxed{
X'
=
\frac{X+r-\eta_e(Q)}{2^h}
+
\beta_e(Q).
}
\]

The address dynamics are therefore exactly:

\[
\boxed{
\text{subtract source constant}
\to
\text{select low }h\text{ bits}
\to
\text{right shift }h\text{ bits}
\to
\text{add target constant}.
}
\]

This is a radix-2 carry transducer.

## 4. Finite precision

If only `P` future address bits are needed, `X mod 2^P` is sufficient.  After an edge of resolution `h`, the child requires only

\[
P-h
\]

bits.  The finite-precision transition is exact modulo `2^(P-h)`.

Together with the finite one-paid source-resolution horizon, this makes the address channel a finite bit-shift system rather than an unbounded-integer state.

## 5. Relation to depth-41 bounded carry

MATH-092 does not identify the depth-41 dominance state with the one-paid compatibility state.  It does, however, put both into the same computational class:

\[
\boxed{\text{bounded integer carry + radix-2 shift + finite branch data}.}
\]

This is the closest current structural match between the depth finite-state calculation and the one-paid macro calculation.

Reproducibility:

`collatz/src/2026_09_12_math092_normalized_2adic_address_transducer_certificate.py`
