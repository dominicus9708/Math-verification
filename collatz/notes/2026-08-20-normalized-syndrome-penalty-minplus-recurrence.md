# Normalized syndrome-penalty min-plus recurrence

Date: 2026-08-20

Status: **exact normalized recurrence identifying the remaining sparse-tail cross-base term.** This is not a coefficient-stopping theorem and not a proof of the Collatz conjecture.

## 1. Exact five/macro-block decomposition

At an actual phase-height state \((s,h)\), put

\[
a=b_s+h.
\]

Fix a length-\(B\) admissible parity word \(w\) with

- canonical start \(r_w\),
- odd count \(q_w\),
- canonical endpoint \(c_w=T^B(r_w)\),
- affine correction \(R_w\), so
  \[
  2^Bc_w=3^{q_w}r_w+R_w.
  \]

Let

\[
h'_w=h+q_w-(b_{s+B}-b_s).
\]

For suffix horizon \(J\), define the unrestricted suffix minimum

\[
\mu'_w
:=
\mu_{s+B,h'_w}(J)
\]

and the exact ternary-syndrome constrained suffix minimum

\[
\nu_w
:=
\min\left\{
 y\in\mathcal S_{s+B,h'_w}(J):
 y\equiv c_w\pmod{3^{q_w}}
\right\}.
\]

The exact branch minimum is

\[
\boxed{
 x_w
 =r_w+2^B\frac{\nu_w-c_w}{3^{q_w}}.
}
\]

## 2. Normalization cancels the multiplicative block factor

Use

\[
\widehat x_w
:=
\frac{2^s}{3^a}x_w
\]

and normalize suffix values by

\[
\widehat y
:=
\frac{2^{s+B}}{3^{a+q_w}}y.
\]

Then

\[
\begin{aligned}
\widehat x_w
&=
\frac{2^sr_w}{3^a}
+
\frac{2^{s+B}}{3^{a+q_w}}(\nu_w-c_w)\\
&=
\frac{2^{s+B}}{3^{a+q_w}}\nu_w
+
\frac{2^s}{3^a}
\left(
 r_w-\frac{2^Bc_w}{3^{q_w}}
\right).
\end{aligned}
\]

Because

\[
\frac{2^Bc_w}{3^{q_w}}
=r_w+\frac{R_w}{3^{q_w}},
\]

we obtain the exact identity

\[
\boxed{
\widehat x_w
=
\widehat\nu_w-E_w,
}
\]

where

\[
\boxed{
E_w
:=
\frac{2^sR_w}{3^{a+q_w}}
\ge0.
}
\]

The block coefficient \(2^B/3^{q_w}\) has disappeared completely.

## 3. Ternary syndrome penalty

Define

\[
\boxed{
P_w(J)
:=
\frac{2^{s+B}}{3^{a+q_w}}
\left(
\nu_w-\mu'_w
\right)
\ge0.
}
\]

Then

\[
\widehat\nu_w
=
\widehat\mu_{s+B,h'_w}(J)+P_w(J).
\]

Therefore each exact branch satisfies

\[
\boxed{
\widehat x_w
=
\widehat\mu_{s+B,h'_w}(J)
+P_w(J)-E_w.
}
\]

Taking the minimum over admissible first blocks gives the exact normalized min-plus recurrence

\[
\boxed{
\widehat\mu_{s,h}(J+B)
=
\min_{w\in\mathcal W_{s,h}}
\left[
\widehat\mu_{s+B,h'_w}(J)
+P_w(J)-E_w
\right].
}
\]

This is the current sharp sparse-tail recurrence.

## 4. Universal correction rebate bound

From the sharp block correction estimate

\[
\frac{R_w}{3^{q_w}}
\le\frac{2^{B-1}}3
\]

and coefficient survival

\[
\frac{2^s}{3^a}\le1,
\]

we have

\[
\boxed{
0\le E_w\le\frac{2^{B-1}}3.
}
\]

For \(B=5\),

\[
\boxed{E_w\le16/3.}
\]

Thus the only unbounded favorable term capable of forcing normalized minimal-survivor growth is the syndrome penalty \(P_w\).

## 5. Interpretation

The recurrence separates the sparse-tail problem into three pieces:

1. inherited normalized suffix minimum;
2. a **nonnegative cross-base syndrome penalty** \(P_w\);
3. a uniformly bounded affine correction rebate \(E_w\).

Without the ternary syndrome, \(P_w\) is set to zero and the earlier scalar five-block lower bound becomes weak. The exact syndrome solver showed that this information loss can be enormous.

Thus the missing deterministic Stage-4 theorem can be stated as a min-plus transversality problem:

> Along every long minimizing branch chain, show that accumulated ternary-syndrome penalties cannot be cancelled indefinitely by the bounded correction rebates and the zero-lift linear corridor.

This is the sparse-tail analogue of the selector/coefficient transversality problem on the bulk side.

## 6. Small exact calibration

For the ordinary initial five-step split, the four surviving branches have

\[
(r,q,c,R,h')
=
(7,4,20,73,0),
(15,4,40,65,0),
(27,4,71,85,0),
(31,5,242,211,1).
\]

At suffix horizon \(J=10\), exact brute-force minima are

\[
\mu_{5,0}(10)=9,
\qquad
\mu_{5,1}(10)=1,
\]

while the syndrome-constrained minima are

\[
\nu=(182,121,71,242).
\]

The resulting exact branch minima are

\[
71,47,27,31,
\]

and hence

\[
\boxed{\mu(15)=27.}
\]

Already here the positive syndrome penalty is much larger than the correction rebate on every branch.

## 7. K=200 calibration

For suffix horizon \(195\), the exact unrestricted phase minima are

\[
\mu_{5,0}(195)=
\mu_{5,1}(195)=837799.
\]

The exact syndrome-constrained minima are

\[
\begin{array}{c|r}
r_w&\nu_w\\\hline
7&15388886\\
15&10259257\\
27&16786430\\
31&8550683
\end{array}
\]

For the four branches the normalized penalty/rebate values are approximately

\[
\begin{array}{c|r|r|r}
r_w&\widehat\mu'&P_w&E_w\\\hline
7&330982.321&5748577.580&0.901\\
15&330982.321&3722057.481&0.802\\
27&330982.321&6300693.728&1.049\\
31&110327.440&1015688.428&0.868
\end{array}
\]

They reconstruct the exact branch minima

\[
6079559,
4053039,
6631675,
1126015,
\]

so

\[
\boxed{\mu(200)=1126015.}
\]

The finite example shows quantitatively why retaining the ternary syndrome repaired the earlier scalar-loss gap: the penalty is millions in normalized units while the one-block correction rebate remains of order one.

This finite disparity is not claimed to persist uniformly without proof.

## 8. Revised theorem target

Together with the zero-lift linear corridor

\[
v_n\le v_0+n\frac{2^{B-1}}3,
\]

the exact recurrence suggests the following sufficient route:

1. establish a renewal-conditioned lower bound on accumulated \(P_w\);
2. subtract the uniformly bounded accumulated \(E_w\);
3. prove the resulting normalized min-plus value outruns the linear zero-lift corridor.

If achieved uniformly along reachable phase-height states, this would force infinitely many nonzero macro lift digits for every infinite coefficient-surviving path and would close the deterministic sparse-tail half of the corrected Stage-4 reduction.

Certificate:

`collatz/src/normalized_syndrome_penalty_recurrence_certificate.py`.
