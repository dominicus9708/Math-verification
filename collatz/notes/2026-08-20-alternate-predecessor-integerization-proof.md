# Alternate-predecessor integerization: exact pullback proof

Date: 2026-08-20

Status: **the s<q integerization step used by the original-start alternate-predecessor sieve is algebraically valid; its implicit dyadic divisibility and suffix-parity claims are made explicit here.** This is not a proof of the Collatz conjecture.

## 1. Setup

For a length-L parity word w with q odd symbols, write

\[
T_w^L(N)=\frac{3^qN+R_w}{2^L}.
\]

Let u be another length-L word with the same q and larger correction

\[
R_u>R_w.
\]

Put

\[
C:=R_u-R_w=3^sC_0,
\qquad 3\nmid C_0.
\]

The case \(s\ge q\) is the ordinary integer predecessor-credit case:

\[
N^\#=N-\frac{C}{3^q}.
\]

The nontrivial case is

\[
0<s<q.
\]

Define

\[
d:=q-s.
\]

Let \(t_d\) be the time immediately after the d-th odd symbol of u, and let \(R_d\) be the correction accumulated by that prefix of u. Thus the formal d-odd prefix map is

\[
X\longmapsto\frac{3^dX+R_d}{2^{t_d}}.
\]

## 2. Formal rational predecessor

The full affine endpoint identity suggests the rational start

\[
M=N-\frac{C}{3^q}
=N-\frac{C_0}{3^d}.
\]

Indeed

\[
3^qM+R_u
=3^qN-C+R_u
=3^qN+R_w.
\]

After the first d odd events of u, this formal trajectory reaches

\[
\boxed{
m=\frac{3^dN+R_d-C_0}{2^{t_d}}.
}
\]

The question is whether m is automatically an integer and, if so, whether it really follows the remaining suffix of u.

## 3. Dyadic divisibility is automatic

Because N lies in the canonical length-L cylinder of w,

\[
3^qN+R_w\equiv0\pmod{2^L}.
\]

Let \(r_u\) be the canonical starting residue of u. Then

\[
3^qr_u+R_u\equiv0\pmod{2^L}.
\]

Subtracting and using \(R_u-R_w=3^sC_0\),

\[
3^q(N-r_u)-3^sC_0\equiv0\pmod{2^L}.
\]

Since \(3^s\) is invertible modulo every power of two,

\[
\boxed{
3^dN-C_0\equiv3^dr_u\pmod{2^L}.
}
\]

Adding \(R_d\),

\[
3^dN+R_d-C_0
\equiv
3^dr_u+R_d
\pmod{2^L}.
\]

The right-hand side is the numerator of the genuine u-prefix started at \(r_u\), so it is divisible by \(2^{t_d}\). Because \(t_d\le L\), the left-hand side is also divisible by \(2^{t_d}\).

Therefore

\[
\boxed{m\in\mathbb Z.}
\]

No additional divisibility test is required in the sieve.

## 4. The remaining suffix is also genuine

Divide the displayed congruence by \(2^{t_d}\). If

\[
x_u:=T_u^{t_d}(r_u),
\]
then

\[
\boxed{
m\equiv x_u\pmod{2^{L-t_d}}.}
\]

A parity suffix of length \(L-t_d\) is determined by precisely this dyadic residue class. Hence m lies in the same canonical suffix cylinder as the state \(x_u\), and therefore m follows the remaining bits of u as an actual integer Collatz trajectory.

Consequently

\[
\boxed{
T_u^{L-t_d}(m)=T_w^L(N).
}
\]

Thus m is a genuine integer alternate predecessor of the actual endpoint, not merely a formal affine value.

## 5. When is the alternate predecessor smaller?

Subtract N:

\[
\boxed{
m-N
=
\frac{(3^d-2^{t_d})N+R_d-C_0}{2^{t_d}}.
}
\]

If

\[
2^{t_d}>3^d,
\]
then the coefficient of N is negative. Therefore, on a large-start cylinder \(N\ge N_{\min}\), checking

\[
(3^d-2^{t_d})N_{\min}+R_d-C_0<0
\]

is sufficient to prove

\[
m<N
\]

for every larger N in that cylinder.

Positivity is guaranteed when the formal start

\[
M=N-C/3^q
\]

is positive, which is certified by

\[
C<N_{\min}3^q.
\]

The original slow sieve performs exactly these two checks.

## 6. Why the fast large-start sieve can simplify them

For the current large-start regime

\[
N_{\min}=4(3^{44}+3^{32})+3,
\]

and every block length used by the fast certificate satisfies \(L\le44\).

The maximum possible affine correction at length L is attained by the all-odd word and equals

\[
R_{\max}(L)=3^L-2^L<3^L<N_{\min}.
\]

Hence

\[
0<C<N_{\min},
\qquad
0\le R_d<N_{\min}.
\]

If \(2^{t_d}>3^d\), the integer gap \(2^{t_d}-3^d\) is at least one, so

\[
(3^d-2^{t_d})N_{\min}+R_d-C_0
< -N_{\min}+R_d<0.
\]

Also \(C<N_{\min}3^q\) is automatic.

Therefore, in this bounded-L large-start regime, the existence of a same-q alternate with the required 3-adic valuation and a contracting d-th-odd prefix is already sufficient; the expensive pairwise size test can be eliminated.

This justifies the compressed residue-maxima implementation in

`collatz/src/binary_alternate_predecessor_integerization_fast.cpp`.

## 7. Exhaustive regression certificate

`collatz/src/binary_alternate_predecessor_integrality_certificate.py`

checks every qualifying pair through \(L=12\), totaling

\[
829,734
\]

pairs. It verifies exactly:

1. the derived dyadic congruence;
2. divisibility by \(2^{t_d}\);
3. the suffix-cylinder congruence;
4. the actual suffix parity sequence;
5. equality of the final endpoints.

All checks pass.

## 8. Consequence for the corrected proof program

This theorem is compatible with the 2026-08-20 Stage 3C correction because it does not infer minimality from a later local decrease \(x-\Delta<x\). It explicitly constructs a smaller integer predecessor in the **original start coordinate**.

Therefore the original-start integerization sieve is a logically safe strengthening of coefficient survival, while repeated local residue-maximality remains conditional on a separate prefix-pullback theorem.
