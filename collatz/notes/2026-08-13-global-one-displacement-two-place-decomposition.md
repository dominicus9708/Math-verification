# Global one-displacement two-place decomposition on the Beatty boundary

Date: 2026-08-13

Status: **exact global decomposition**. Every coefficient-survival boundary word is obtained from the mechanical Beatty word by moving each ordered one weakly to the left. The real remainder defect and dyadic canonical-address defect decompose over those ordered-one displacements. This is not a Collatz proof.

## 1. Mechanical and actual ordered-one positions

Put

\[
\alpha:=\log_3 2,
\qquad
b_t:=\lceil\alpha t\rceil.
\]

Let `w` be a length-`L` boundary word:

\[
q_t(w)\ge b_t,
\qquad
q_L(w)=b_L=:q.
\]

Let

\[
d_\ell
\]

be the zero-based position of the `ell`-th one of `w`, and let

\[
d_\ell^\star
\]

be the position of the `ell`-th one in the mechanical Beatty word

\[
m_t=b_{t+1}-b_t.
\]

Since every actual prefix contains at least as many ones as the mechanical prefix,

\[
\boxed{d_\ell\le d_\ell^\star}
\qquad(1\le\ell\le q).
\]

Define the displacement

\[
\boxed{r_\ell:=d_\ell^\star-d_\ell\ge0.}
\]

Thus the boundary word is an ordered collection of left displacements from the remainder-maximizing mechanical word.

## 2. Exact real remainder decomposition

For any parity word with ordered-one positions `d_ell`,

\[
E(w)
=
\frac1{2^L}
\sum_{\ell=1}^q
2^{d_\ell}3^{q-\ell}.
\]

For the mechanical word,

\[
E_\star
=
\frac1{2^L}
\sum_{\ell=1}^q
2^{d_\ell^\star}3^{q-\ell}.
\]

Hence

\[
\begin{aligned}
E_\star-E(w)
&=
\frac1{2^L}
\sum_{\ell=1}^q
2^{d_\ell}3^{q-\ell}
(2^{r_\ell}-1)\\
&=
\sum_{\ell=1}^q
M_\ell(1-2^{-r_\ell}),
\end{aligned}
\]

where

\[
\boxed{
M_\ell
:=
2^{d_\ell^\star-L}3^{q-\ell}
}
\]

is the mechanical contribution of the `ell`-th one.

Therefore

\[
\boxed{
E_\star-E(w)
=
\sum_{\ell=1}^q
M_\ell(1-2^{-r_\ell}).
}
\]

## 3. Mechanical contribution collapses to rotation phase

The mechanical one at position `d_ell^star` satisfies

\[
\ell=b_{d_\ell^\star+1}.
\]

Write

\[
\delta_t:=b_t-\alpha t\in(0,1).
\]

Then

\[
q-\ell
=b_L-b_{d_\ell^\star+1}
=
\alpha(L-d_\ell^\star-1)
+\delta_L-\delta_{d_\ell^\star+1}.
\]

Using `3^alpha=2`,

\[
\boxed{
M_\ell
=
\frac12
3^{\delta_L-\delta_{d_\ell^\star+1}}.
}
\]

Consequently

\[
\boxed{
\frac16<M_\ell<\frac32
}
\]

uniformly in `L` and `ell`.

## 4. Uniform cost per displaced one

If `r_ell>0`, then

\[
1-2^{-r_\ell}\ge\frac12.
\]

Therefore every displaced ordered one contributes strictly more than

\[
\frac16\cdot\frac12
=
\frac1{12}
\]

to the real defect.

Let

\[
N_{\rm disp}(w)
:=
\#\{\ell:r_\ell>0\}.
\]

Then

\[
\boxed{
E_\star-E(w)
>
\frac1{12}N_{\rm disp}(w).
}
\]

This bound is independent of the global first-crossing depth.

## 5. Exact dyadic canonical-address decomposition

The canonical start residue modulo `2^L` is

\[
r(w)
\equiv
-\sum_{\ell=1}^q
2^{d_\ell}3^{-\ell}
\pmod{2^L}.
\]

For the mechanical word,

\[
r_\star
\equiv
-\sum_{\ell=1}^q
2^{d_\ell^\star}3^{-\ell}
\pmod{2^L}.
\]

Thus

\[
\begin{aligned}
r(w)-r_\star
&\equiv
-\sum_\ell
(2^{d_\ell}-2^{d_\ell^\star})3^{-\ell}\\
&\equiv
\boxed{
\sum_{\ell:r_\ell>0}
2^{d_\ell}(2^{r_\ell}-1)3^{-\ell}
}
\pmod{2^L}.
\end{aligned}
\]

For every nonzero summand,

\[
\boxed{
v_2\!\left(
2^{d_\ell}(2^{r_\ell}-1)3^{-\ell}
\right)=d_\ell,}
\]

because both `2^{r_ell}-1` and `3^{-ell}` are odd.

The actual one positions `d_ell` are distinct, so all nonzero defect summands have distinct 2-adic valuations.

Hence the dyadic defect is a valuation-graded direct sum: its lowest nonzero bit is controlled by the earliest displaced actual one and cannot be cancelled by later displacement terms.

## 6. Two-place interpretation

Each displaced ordered one contributes the pair

\[
\boxed{
\left(
M_\ell(1-2^{-r_\ell}),
\quad
2^{d_\ell}(2^{r_\ell}-1)3^{-\ell}\bmod2^L
\right).
}
\]

The first coordinate is a positive Archimedean loss; the second occupies a unique dyadic formation level `d_ell`.

Thus the entire first-crossing defect is simultaneously

- a positive sum in the real place;
- a collision-free valuation hierarchy in the 2-adic place.

## 7. Relation to earlier skew/displacement notation

The identity is the time-expanded analogue of the earlier Christoffel displacement defect. It makes explicit why the same displacement data controls both the rational-shadow loss and canonical-address shift.

The present form has one additional useful feature: the mechanical contribution of every ordered one has a uniform phase bound, so every nonzero displacement has an absolute real cost `>1/12`.

## 8. Current consequence and limit

The uniform per-one cost is stronger than a raw positive-slack count, but by itself it does not close the current `m=44` resonance: the existing Archimedean correction budget is still large enough to permit many displaced ones.

Its main value is therefore in a coupled argument. A candidate with many displaced ones pays a definite real cost; a candidate with few displaced ones has a sparse, highly rigid dyadic defect address. The next target is to intersect that sparse valuation hierarchy with the ternary recursive core and the smaller-predecessor constraints.
