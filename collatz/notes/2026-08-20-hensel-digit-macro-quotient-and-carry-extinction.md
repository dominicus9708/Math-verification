# Hensel-digit macro quotient and carry extinction

Date: 2026-08-20

Status: **exact simplification of the ternary-affine sparse-tail state, plus an exact finite-horizon min-plus quotient.** This is not a proof of the Collatz conjecture.

## 1. Start from the normalized ternary progression

Use the state

\[
x=\rho+e3^a+3^a u,
\qquad
0\le\rho<3^a,
\qquad e\in\{0,1\}.
\]

Put

\[
M=3^a.
\]

For a five-step parity word \(w\), let

- \(r_w\in\{1,\ldots,32\}\) be its least positive canonical start,
- \(q_w\) its odd-step count,
- \(c_w=T^5(r_w)\) its canonical endpoint.

The previous affine-progression note solved the CRT intersection on the ternary side. The same intersection becomes substantially simpler when solved on the dyadic side.

## 2. One exact dyadic Hensel digit

The common CRT solutions satisfy

\[
x\equiv\rho\pmod M,
\qquad
x\equiv r_w\pmod{32}.
\]

Hence there is a unique

\[
\boxed{j_w\in\{0,\ldots,31\}}
\]

with

\[
\boxed{
 j_w
 =
 \left[(r_w-\rho)M^{-1}\right]_{32}.
}
\]

The least positive CRT point before imposing the floor carry is exactly

\[
\boxed{x_{\rm res}=\rho+j_wM.}
\]

This is the same point as the earlier expression \(r_w+32t_0\), because

\[
\rho+j_wM\equiv r_w\pmod{32}.
\]

Thus the complicated-looking ternary-side CRT lift is only one base-32 Hensel digit on the dyadic side.

## 3. Exact carry persistence law

The input floor is

\[
A=\rho+eM.
\]

Since \(j_w\in[0,31]\), the CRT point lies below the floor only in the single case

\[
e=1,
\qquad j_w=0.
\]

When that occurs, one common period \(32M\) must be added. Therefore

\[
\boxed{
x_0
=\rho+(j_w+32e')M,}
\]

where

\[
\boxed{
e'=e\,\mathbf 1_{\{j_w=0\}}.}
\]

Consequences:

1. **carry is never created:**
   \[
   e=0\Longrightarrow e'=0;
   \]
2. **carry can only persist through exact dyadic alignment:**
   \[
   e=1\Longrightarrow e'=1\iff j_w=0.
   \]

So the one-bit carry is not a genuine recurrent channel. It is a monotone transient flag.

## 4. The normalized syndrome update is independent of the input carry

Define

\[
d_w
:=
\frac{\rho-r_w+j_wM}{32}.
\]

This is an integer by definition of \(j_w\). The five-step affine map gives

\[
T^5(x_0)
=
 c_w+3^{q_w}d_w
 +e'3^{a+q_w}.
\]

Hence after normalization

\[
\boxed{
\rho'
=
 c_w+3^{q_w}
 \frac{\rho-r_w+j_w3^a}{32},
}
\]

\[
\boxed{a'=a+q_w,}
\]

and the displayed formula for \(\rho'\) does **not** contain the input carry \(e\).

Thus the arithmetic syndrome dynamics and the floor-carry dynamics separate exactly.

## 5. Carry disappears completely for the ordinary coefficient-survivor problem

The four ordinary depth-five coefficient-surviving cylinders have

\[
(r_w,q_w,c_w)
\in
\{(7,4,20),(15,4,40),(27,4,71),(31,5,242)\}.
\]

In every case

\[
0<c_w<3^{q_w}.
\]

Therefore the suffix progression begins with

\[
A=c_w,
\qquad
\rho=c_w,
\qquad
 e=0.
\]

By the carry-persistence law,

\[
\boxed{
e=0\quad\text{for every later five-block renormalization}.}
\]

Hence for the ordinary Collatz coefficient-survivor sparse tail the exact state reduces from

\[
(s,h,a,\rho,e)
\]

to

\[
\boxed{(s,h,a,\rho).}
\]

No floor-carry channel is needed.

## 6. Macro version for B=5n steps

Let \(W\) be a parity word of length

\[
B=5n.
\]

Write its canonical data as

\[
(r_W,Q_W,c_W),
\]

so

\[
T^B(r_W+2^Bt)
=c_W+3^{Q_W}t.
\]

For an input progression with \(e=0\), define the single macro-Hensel digit

\[
\boxed{
J_W
=
\left[(r_W-\rho)(3^a)^{-1}\right]_{2^B},
\qquad
0\le J_W<2^B.
}
\]

Then the least member of the progression lying in the full \(B\)-bit parity cylinder is exactly

\[
\boxed{x_W=\rho+J_W3^a.}
\]

Put

\[
d_W
=
\frac{\rho-r_W+J_W3^a}{2^B}.
\]

The corresponding endpoint is

\[
\boxed{
\rho_W'
=
 c_W+3^{Q_W}d_W.
}
\]

For a positive input syndrome \(0<\rho<3^a\), this endpoint again satisfies

\[
0<\rho_W'<3^{a+Q_W},
\]

so the zero-carry state remains zero at macro scale as well.

Thus a whole sequence of five-block CRT choices is equivalent to one Hensel digit modulo \(2^B\).

## 7. Exact finite-horizon min-plus quotient

Fix a phase-height state \((s,h)\) and a horizon \(B\). Let

\[
\mathcal W_{s,h}(B)
\]

be the parity words whose every prefix satisfies the phase-shifted coefficient barrier.

Every admissible word gives the candidate

\[
x_W=\rho+J_W3^a.
\]

Since \(\rho\) and \(3^a\) are common to all candidates,

\[
\boxed{
\min_{W\in\mathcal W_{s,h}(B)}x_W
=
\rho+3^a
\min_{W\in\mathcal W_{s,h}(B)}J_W.
}
\]

Therefore the **choice and value of the macro min-plus increment** depend only on

\[
\rho\pmod{2^B}
\]

and

\[
3^a\pmod{2^B}.
\]

For \(B\ge3\),

\[
\operatorname{ord}_{2^B}(3)=2^{B-2}.
\]

Hence an exact finite-horizon cost quotient is

\[
\boxed{
\left(
 s,h,
 \rho\bmod2^B,
 a\bmod2^{B-2}
\right).
}
\]

This is a genuine safe quotient for the next \(B\) steps of the min-plus cost problem.

It is **not** yet a global future-equivalence theorem, because the complete output syndrome \(\rho_W'\) still retains high ternary information.

## 8. Exact 3-adic contraction of the syndrome

Modulo the new ternary modulus, the macro update may be written as

\[
\rho_W'
\equiv
c_W
+3^{Q_W}2^{-B}(\rho-r_W)
\pmod{3^{a+Q_W}}.
\]

For two input syndromes \(\rho_1,\rho_2\) with the same \(a\), propagated through the same macro word,

\[
\boxed{
\rho_{1,W}'-\rho_{2,W}'
\equiv
3^{Q_W}2^{-B}(\rho_1-\rho_2)
\pmod{3^{a+Q_W}}.
}
\]

Therefore

\[
\boxed{
 v_3(\rho_{1,W}'-\rho_{2,W}')
\ge
v_3(\rho_1-\rho_2)+Q_W
}
\]

up to the available modulus.

Equivalently, every odd step erases one additional low ternary digit of dependence on the remote past. For any fixed \(d\), once the suffix has accumulated at least \(d\) odd steps, the output modulo \(3^d\) is independent of the syndrome before that suffix.

This gives an exact **low-trit renewal/forgetting law**.

## 9. Two-sided interpretation

The sparse-tail arithmetic now has two complementary finite-window properties:

1. **future min-plus cost:** over a fixed \(B\)-step horizon, only a dyadic quotient of \((a,\rho)\) is needed;
2. **output low ternary digits:** after enough odd steps, earlier ternary digits are forgotten by exact 3-adic contraction.

Thus the remaining global problem is no longer an unrestricted growing integer state. It is a cross-base synchronization problem between

\[
\boxed{
\text{finite dyadic Hensel cost window}
\quad\text{and}\quad
\text{contracting ternary memory window}.
}
\]

This is the natural point at which the earlier finite Hensel renewal graphs can be connected to the exact ternary-syndrome min-plus recursion.

## 10. Exact certificate

`collatz/src/ternary_syndrome_hensel_digit_macro_certificate.py` checks:

- all 69,728 one-block states/words from the previous `a<=6` grid;
- exact equality of the direct ternary-side CRT transition and the new Hensel-digit formula;
- zero carry births from every `e=0` state;
- exact `B=10` macro/sequential agreement on 36,864 additional state/word cases.

The next target is to exploit the dyadic-cost quotient and ternary contraction simultaneously, rather than attempting to quotient the full syndrome by either base alone.
