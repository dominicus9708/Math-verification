# Exact rectangle preimage transfer for defect channels

Date: 2026-08-09

Status: **DERIVED EXACT BLOCK TRANSFER + INDEPENDENT EXHAUSTIVE SMALL CHECK**

This note implements the next step of the defect-carry block program.  It shows that the local carry gate does not destroy interval geometry: after a suitable normal form is chosen, the inverse image of one rectangle under one fixed defect-channel update is a union of at most two rectangles.

No asymptotic Collatz result is claimed.

## 1. Local defect-carry map

Use the two-coordinate form from `defect-carry-block-duality.md`.  Fix

\[
M=2^h,\qquad N=2^m.
\]

For one fixed defect-channel contribution write

\[
a\in\{0,\ldots,M-1\},\qquad b\in\mathbb Z/N\mathbb Z.
\]

The update is

\[
\varepsilon=\mathbf 1_{U+a\ge M},
\]

\[
\boxed{U'=[U+a]_M,}
\]

\[
\boxed{V'=[V+b-\varepsilon]_N.}
\]

The only nonlinearity is the single binary carry `epsilon`.

## 2. Rectangle normal form

Represent the low-coordinate block by an ordinary non-wrapping interval

\[
J=[\ell,r)\subset[0,M),
\qquad 0\le\ell<r\le M,
\]

and the high coordinate by a cyclic interval

\[
I_N(v_0,L)
=\{v_0,v_0+1,\ldots,v_0+L-1\}\pmod N.
\]

A block is therefore

\[
\boxed{
\mathcal R(J;v_0,L)
=J\times I_N(v_0,L).
}
\]

The forward small-start interval from the previous note can always be put in this form after the single wrap split associated with `r*`.

## 3. Carry from the output low coordinate

The carry is recoverable from `U'` alone.

If `epsilon=0`, then

\[
U'=U+a\in[a,M),
\]

while if `epsilon=1`,

\[
U'=U+a-M\in[0,a).
\]

Hence

\[
\boxed{
\varepsilon=0\iff U'\in[a,M),
}
\]

and

\[
\boxed{
\varepsilon=1\iff U'\in[0,a).
}
\]

This makes the inverse map piecewise affine with only one threshold point `a`.

## 4. Exact inverse image of one rectangle

Let the output rectangle be

\[
\mathcal R'= [\ell,r)\times I_N(v_0,L).
\]

### Zero-carry piece

Intersect its low interval with

\[
[a,M).
\]

Put

\[
J_0=[\max(\ell,a),r).
\]

If `J_0` is nonempty, then on this piece

\[
U=U'-a,
\qquad
V=[V'-b]_N.
\]

Therefore the exact preimage piece is

\[
\boxed{
(J_0-a)\times I_N(v_0-b,L).
}
\]

### One-carry piece

Intersect the output low interval with

\[
[0,a).
\]

Put

\[
J_1=[\ell,\min(r,a)).
\]

If `J_1` is nonempty, then

\[
U=U'-a+M,
\qquad
V=[V'-b+1]_N.
\]

Hence the exact preimage piece is

\[
\boxed{
(J_1-a+M)\times I_N(v_0-b+1,L).
}
\]

Consequently

\[
\boxed{
F_{a,b}^{-1}(\mathcal R')
\text{ is a disjoint union of at most two normal-form rectangles.}
}
\]

No interval hull or approximation is involved.

## 5. Forward version

The same conclusion holds forward.  Split an ordinary input `U` interval at the carry threshold

\[
M-a.
\]

On each side `epsilon` is constant, so both `U` and `V` are translated affinely.  Thus one normal-form input rectangle maps to at most two normal-form output rectangles after splitting any low-coordinate wrap.

Therefore the exact defect transfer can be implemented either forward or backward as a sparse rectangle transducer.

## 6. Coupling to the defect admissibility state

At defect coordinate `i`, the allowed next defect values are constrained by

\[
z_{i+1}\le z_i+(d_{i+1}^*-d_i^*)-1
\]

with the individual caps from `slack-defect-channel-transfer.md`.

For each allowed defect-state transition, the channel contribution fixes one pair `(a,b)`.  Attach the at-most-two-piece rectangle preimage operator above to that sparse transition.

Hence the exact block state may be written as

\[
\boxed{(z_i,\mathcal R)}
\]

with:

1. a sparse nearest-neighbor defect transition;
2. at most two rectangle pieces for each fixed arithmetic channel;
3. no loss of canonical carry information.

This is an exact block analogue of the earlier scalar/channel transfer.

## 7. Backward certificate integration

The target small-start block is first split so that its final wrap bit is fixed.  Its high-coordinate condition is then a cyclic interval or a union of certified cyclic intervals.

Propagating such a rectangle backward through the defect channels yields an exact family of predecessor rectangles.  Conversely, a forward rectangle cover of reachable defect states can be tested against the transformed suffix set by the exact interval-count certificate.

In particular, if a reachable block at the final defect coordinate has high projection

\[
I_N(v_0,L)
\]

and its translated backward-query interval has

\[
N_{h,q,m}(a,L)=0,
\]

the entire block is removable.

Thus rectangle propagation and E/O suffix interval counting are compatible exact certification layers.

## 8. Complexity statement and limitation

The carry itself contributes at most a factor of two in block splitting per fixed arithmetic channel.  Therefore any faster growth in the rectangle family comes from:

- branching among admissible defect values;
- genuinely different high-coordinate translations;
- failure of adjacent rectangles to merge exactly.

The theorem does **not** prove that the total number of rectangles is polynomial or subexponential.  That is now a sharply isolated combinatorial/arithmetic question rather than an ambiguity caused by carry handling.

An exact implementation should merge two blocks only when their union is again a normal-form rectangle with identical defect state and compatible high interval; otherwise they must remain separate, or be replaced by an explicitly labelled over-approximation that is used only for zero-count pruning.

## 9. Independent finite check

Wolfram exhaustively compared the formula with direct pointwise preimages for

\[
M\in\{2,4,8\},
\qquad
N\in\{2,4\},
\]

for every:

- channel shift `0<=a<M`;
- high translation `0<=b<N`;
- ordinary nonempty low interval `[ell,r)`;
- cyclic high interval start and every length `1<=L<=N`.

All

\[
\boxed{24,048}
\]

cases agreed exactly.

This is a computational cross-check only; the proof is the explicit two-branch inversion above.

## 10. Next target

The next useful quantity is the **rectangle complexity** of the reachable high-resolution defect support at the logarithmic split scale.

Rather than asking whether the full support is low rank, ask whether the portion whose low block lies in the dangerous small-start interval admits a cover by few normal-form rectangles whose high intervals can be eliminated by exact suffix counts.

A uniform bound on that dangerous rectangle complexity would be a direct candidate for the anti-alignment / late-lift forcing theorem.