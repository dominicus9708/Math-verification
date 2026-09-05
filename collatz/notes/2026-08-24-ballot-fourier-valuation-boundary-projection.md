# Ballot Fourier valuation reduces to an odd-frequency boundary projection

Date: 2026-08-24

Status: **exact transfer identity.**  This reduces every 2-adic frequency class of the coefficient-survival Fourier transform to an odd-frequency transfer at a shorter effective depth followed by a finite boundary continuation.  It is not yet a uniform decay theorem and is not a proof of the Collatz conjecture.

## 1. Weighted ballot transfer

Fix a final binary depth H and Fourier frequency t.  For a coefficient-surviving parity prefix of length j with q odd entries, let

\[
A_j(q;t)
\]

be the unnormalized weighted character sum.  An even transition has weight 1.  An odd transition ending at odd count q has weight

\[
\omega_{j,q}(t)
=
\exp\!\left(
-\frac{2\pi i\,t[3^{-q}]_{2^{H-j}}}{2^{H-j}}
\right).
\]

The coefficient barrier at length j+1 is

\[
q\ge q_{\min}(j+1),
\qquad
q_{\min}(n):=\min\{q:3^q\ge2^n\}.
\]

This is the transfer implemented in

`collatz/src/ballot_fourier_transfer.py`.

## 2. The critical -1 layer for a 2-adic frequency

Write

\[
t=2^s u,
\qquad u\text{ odd},
\qquad 0\le s<H.
\]

At the unique step

\[
j_*=H-s-1,
\]

the remaining dyadic modulus is

\[
2^{H-j_*}=2^{s+1}.
\]

Because every inverse power of three is odd modulo a power of two,

\[
[3^{-q}]_{2^{s+1}}\text{ is odd}.
\]

Hence every odd transition at this step has phase

\[
\boxed{
\omega_{j_*,q}(2^su)
=
\exp(-\pi i\,u\,[3^{-q}]_{2^{s+1}})
=-1.
}
\]

The phase is independent of q.

For every later step j>j_*, the remaining modulus divides 2^s, so

\[
\boxed{
\omega_{j,q}(2^su)=1.
}
\]

Thus all Fourier oscillation ends at the critical layer.

## 3. Before the critical layer: exact reduction to odd frequency

Put

\[
K:=H-s.
\]

For j<j_* we have H-j>s+1, and cancellation of the common factor 2^s gives

\[
\omega_{j,q}(2^su)
=
\exp\!\left(
-\frac{2\pi i\,u[3^{-q}]_{2^{K-j}}}{2^{K-j}}
\right).
\]

This is exactly the odd-frequency u phase for a transfer whose final effective depth is K.

Therefore the entire weighted evolution through depth K-1=H-s-1 is identical to the ordinary ballot Fourier transfer at odd frequency u and effective depth K.

The remaining s+1 physical steps consist of one universal -1 layer and s unweighted layers.

## 4. Pull back the unweighted tail

Let

\[
F_s(q)
\]

be the number of coefficient-admissible binary tails of length s starting immediately after the critical layer, from odd count q at physical depth H-s.

Since all phases after the critical layer are 1, the final unnormalized Fourier sum can be pulled back to the pre-critical vector.

Let

\[
a:=q_{\min}(H-s),
\qquad
b:=q_{\min}(H).
\]

At the critical step, a pre-state q can extend evenly only when q>=a, and oddly only when q+1>=a.  The odd branch carries phase -1.  Hence

\[
\boxed{
S_H(2^su)
=
\sum_q A_{H-s-1}(q;u)\,
\Bigl(
\mathbf1_{q\ge a}F_s(q)
-
\mathbf1_{q+1\ge a}F_s(q+1)
\Bigr).
}
\]

Here the notation A(q;u) uses the reduced odd-frequency transfer from Section 3.

This is an exact identity, not an inequality.

## 5. Boundary support has rank at most s+1

The tail count F_s(q) is nondecreasing in q.

If q>=b=q_min(H), then every one of the remaining s parity choices is coefficient-admissible, because the odd count never decreases and no future threshold exceeds b.  Therefore

\[
F_s(q)=2^s
\qquad(q\ge b).
\]

For q>=b, the two continuation terms in the boxed formula are equal and cancel.

For q<a-1, neither critical extension is admissible.

Thus only

\[
\boxed{
a-1\le q\le b-1}
\]

can contribute.

Since q_min can increase by at most one per binary step,

\[
b-a\le s.
\]

Therefore the Fourier sum at any frequency with v2(t)=s is a linear functional of at most

\[
\boxed{s+1}
\]

boundary states of the reduced odd-frequency transfer.

This is the **valuation boundary-projection theorem**.

## 6. Odd frequencies are rank one at the final layer

For s=0 we have a=b=q_min(H), F_0(q)=1, and the support interval contains exactly one state q=a-1.

Hence

\[
\boxed{
S_H(u)
=-A_{H-1}(q_{\min}(H)-1;u),
\qquad u\text{ odd}.
}
\]

All interior q-states cancel exactly at the last step.

This explains why the strong low-odd-frequency cancellation seen numerically in the existing transfer is structurally tied to the ballot boundary rather than generic random-phase cancellation.

## 7. Spectral-complementarity consequence

Every nonzero dyadic frequency is now parameterized by one integer

\[
K=H-v_2(t).
\]

The coefficient-survival side needs only an odd-frequency boundary amplitude at effective depth K.  Large valuation means small K; small valuation means a long odd-frequency transfer but a very low-rank final projection.

On the ternary-selector side, the same valuation parameter controls the reduced modulus in the finite Riesz product.

Thus the remaining same-address Fourier problem is naturally one-dimensional in the effective depth K rather than a two-dimensional search over arbitrary t and H.

A useful next theorem is therefore narrower than the previous generic BFC conjecture:

> **Odd Boundary Fourier Decay.**  Prove exponential or sufficiently strong subexponential decay for the O(1)-width boundary components A_{K-1}(q_min(K)-1;u) uniformly in odd u over the frequency range paired with the selector Riesz product.

The full-frequency estimate then follows from the exact valuation projection above plus the selector attenuation in the complementary valuation range.
