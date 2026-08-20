# Height-excursion macro reduction

Date: 2026-08-20

Status: **exact macro transport reduction.** This sharpens the deterministic sparse-tail program, but it is not a coefficient-stopping theorem and not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_n=\lceil n\alpha\rceil,
\]

and write the generalized coefficient-survivor state as \((s,h)\), where a length-\(j\) prefix with odd count \(q_j\) is admissible when

\[
q_j\ge b_{s+j}-b_s-h.
\]

For a length-\(L\) parity macro \(W\), let

\[
Q=Q_W
\]

be its total odd count. Define

\[
D_s(L):=b_{s+L}-b_s.
\]

If the incoming height is \(h\), then the outgoing height is exactly

\[
\boxed{
h'=h+Q-D_s(L).
}
\]

The mechanical one-slack lemma gives

\[
\boxed{
D_s(L)\in\{b_L-1,b_L\}.
}
\]

## 1. Surplus-gain macro theorem

Assume that \(W\) is admissible at \((s,h)\) and that

\[
\boxed{h'\ge h+1.}
\]

Then the same macro \(W\) is admissible at its suffix state

\[
(s+L,h').
\]

Indeed, for every prefix length \(j\le L\), both

\[
D_s(j)=b_{s+j}-b_s
\]

and

\[
D_{s+L}(j)=b_{s+L+j}-b_{s+L}
\]

belong to \(\{b_j-1,b_j\}\), hence

\[
D_{s+L}(j)\le D_s(j)+1.
\]

Because \(h'\ge h+1\),

\[
D_{s+L}(j)-h'
\le
D_s(j)-h.
\]

Current admissibility therefore implies suffix admissibility prefix by prefix.

Moreover,

\[
Q
=
D_s(L)+(h'-h)
\ge
D_s(L)+1
\ge
b_L.
\]

Thus

\[
\boxed{3^Q\ge2^L.}
\]

This second inequality is what fixes the sign problem in the normalized min-plus recurrence.

## 2. Self-prepend transport for an arbitrary macro

Write the affine action of \(W\) as

\[
T^L(x)=\frac{3^Qx+R_W}{2^L}.
\]

For its canonical endpoint syndrome \(c_W\), let \(\nu\) be the least suffix survivor in that ternary syndrome, and let

\[
\mu'
\]

be the unrestricted suffix minimum at \((s+L,h')\).

The exact predecessor of \(\nu\) through \(W\) is

\[
 x_W
 =
 \frac{2^L\nu-R_W}{3^Q}.
\]

The first \(L\) steps of this predecessor are admissible at the suffix state by the theorem above.

For later steps, every shifted length-\(L\) mechanical increment is at most \(b_L\):

\[
b_{A+L+j}-b_{A+j}\le b_L,
\qquad A=s+L.
\]

Since \(Q\ge b_L\), the prepended macro supplies enough odd steps to bridge the displacement. Therefore the predecessor belongs to the same suffix-survivor language as \(\nu\), so minimality gives

\[
\boxed{x_W\ge\mu'.}
\]

Equivalently,

\[
2^L(\nu-\mu')-R_W
\ge
(3^Q-2^L)\mu'.
\]

Let

\[
c_{s,h}=\frac{2^s}{3^{b_s+h}}.
\]

The exact normalized syndrome recurrence uses

\[
P_W-E_W
=
\frac{c_{s,h}}{3^Q}
\left(2^L(\nu-\mu')-R_W\right).
\]

Hence every strict-height-gain macro satisfies

\[
\boxed{
P_W-E_W
\ge
c_{s,h}
\left(1-\frac{2^L}{3^Q}\right)
\mu'
\ge0.
}
\]

This is the all-length form of the earlier five-step \(q\ge4\) lemma.

## 3. Consequence: negative normalized loss cannot be attached to a height record climb

Suppose a long admissible tail is cut at successive first times that the height reaches a new record level.

Every completed record-climb macro has

\[
h_{\rm out}\ge h_{\rm in}+1,
\]

so each such macro has nonnegative normalized penalty-minus-rebate.

Therefore any persistent negative normalized contribution must be carried by pieces that do **not** create a new record height.

This localizes the difficult part to height excursions rather than the whole tail.

## 4. Height-neutral excursions sit exactly on the one-slack boundary

For a height-neutral macro,

\[
h'=h.
\]

Then

\[
Q=D_s(L),
\]

so by the mechanical one-slack lemma

\[
\boxed{
Q\in\{b_L-1,b_L\}.
}
\]

Thus every neutral excursion has only two possible total odd counts relative to length.

### Full-barrier neutral case

If

\[
Q=b_L,
\]

then

\[
3^Q\ge2^L,
\]

so the normalization itself is nonexpanding across the macro.

### One-slack neutral case

If

\[
Q=b_L-1,
\]

then

\[
3^Q<2^L<3^{Q+1},
\]

and therefore

\[
1<\frac{2^L}{3^Q}<3.
\]

So the only height-neutral macros whose raw coefficient normalization expands are exactly the one-slack macros already isolated by the mechanical-phase analysis.

## 5. The scale fluctuation is a bounded coboundary

Because

\[
b_s=\lceil s\alpha\rceil,
\]

for \(s>0\) define

\[
\delta_s=b_s-s\alpha\in(0,1).
\]

Then

\[
\boxed{
c_{s,h}=3^{-h-\delta_s}.}
\]

Consequently, while the height remains in a bounded range \(0\le h\le H\),

\[
3^{-(H+1)}<c_{s,h}<1.
\]

The apparent blockwise expansions and contractions produced by low- and high-odd macros therefore cannot accumulate as an independent exponential factor when the height is bounded; they telescope through the bounded phase-height scale.

This is important because it shows that the unresolved low-q normalized losses should not be treated as unrelated negative increments. They belong to a height-excursion cocycle whose multiplicative part is already a bounded mechanical coboundary.

## 6. Revised deterministic sparse-tail target

The sparse-tail problem is now more tightly localized:

1. **strict height gains:** exact nonnegative normalized transport;
2. **linear positive height drift:** stronger parity entropy loss than the coefficient boundary, so this side is naturally assigned to the bulk/entropy argument;
3. **bounded or sublinear height:** decompose into height excursions;
4. **neutral excursions:** total odd count is exactly \(b_L\) or \(b_L-1\);
5. **one-slack neutral excursions:** these are the only neutral pieces with coefficient-scale expansion and coincide with the rank-one mechanical boundary already present in the Fourier/Haar cocycle.

Thus the next theorem should no longer be formulated as a lower bound on every five-block penalty. A sharper target is:

> **Height-excursion syndrome theorem.** Prove a uniform cross-base lower bound for the ternary syndrome penalty on height-neutral one-slack excursions (and the finitely nested downward excursions between them), after quotienting out the bounded phase-height scale.

This is a smaller target than the previous unrestricted low-q penalty problem and directly matches the existing mechanical one-slack/rank-one machinery.

Finite regression certificate:

`collatz/src/height_excursion_macro_certificate.py`.
