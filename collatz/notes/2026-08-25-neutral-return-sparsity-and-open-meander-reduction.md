# Neutral-return sparsity and reduction to the open critical meander

Date: 2026-08-25

Status: **exact consequence of the existing post-formation harmonic/state-escape theorem, plus finite L7 neutral-excursion audits.** This is a proof-architecture reduction, not a proof of the Collatz conjecture.

## 1. Coordinate

For a fixed positive integer `N` on a hypothetical nonperiodic no-first-descent odd-event orbit, use

\[
x_q=(N+c_q)2^{s_q+\theta_q},
\qquad
c_q=O_N(q^{1/9}),
\]

with

\[
s_q=\lfloor q\log_2 3\rfloor-A_q,
\qquad 0<\theta_q<1.
\]

A return to a bounded-width critical/mechanical strip means

\[
s_q\le B
\]

for one fixed constant `B`. Exact neutral returns are a special case.

## 2. Bounded-height visits are sparse

For all `i<=Q`, if `s_i<=B`, then

\[
x_i=(N+c_i)2^{s_i+\theta_i}
\le C_{N,B}Q^{1/9}
\]

for a fixed constant `C_{N,B}`.

The established state-escape counting theorem says

\[
\#\{0\le i<Q:x_i\le X\}=O_N(XQ^{1/9}).
\]

Taking `X=C_{N,B}Q^{1/9}` gives

\[
\boxed{
\#\{0\le i<Q:s_i\le B\}=O_{N,B}(Q^{2/9}).
}
\]

In particular,

\[
\boxed{R_{\rm neutral}(Q)=O_N(Q^{2/9}).}
\]

Thus neutral returns have zero density, with a quantitative power-saving bound.

## 3. Consequence for positive-height occupation

On an eventual coefficient-survival branch `s_i>=0`. Therefore

\[
\#\{i<Q:s_i=0\}=O_N(Q^{2/9})
\]

and hence

\[
\boxed{
\frac1Q\#\{i<Q:s_i>0\}
=1-O_N(Q^{-7/9})\to1.
}
\]

This asymptotically supersedes any fixed finite positive-height density floor such as the current q<=8 `19.6251%` certificate. The q<=8 result remains a valid finite-resonance theorem, but zero-endpoint overlapping-window refinement cannot be the final asymptotic mechanism because zero endpoints themselves are sublinear.

## 4. Consequence for ultrametric locking

The root-translation ultrametric theorem shows that each completed neutral excursion locks new low dyadic information that no later excursion can repair.

The number of times such a new neutral-return label can be created through odd-event depth `Q` is at most

\[
O_N(Q^{2/9}).
\]

Therefore any bookkeeping that contributes only `O(1)` bits per completed neutral return has total complexity

\[
\boxed{
2^{O_N(Q^{2/9})}=2^{o(Q)}.
}
\]

So completed-neutral-return labels cannot themselves generate a positive linear repair exponent. Any remaining linear Stage-4 repair entropy must live inside the long open-positive intervals between the sparse returns.

This statement does **not** bound the total number of parity words inside one long excursion; it only removes the return-indexed label channel from the linear-rate budget.

## 5. Finite L7 audit: neutral return cost is not uniformly exponential

At length 28, aligned L7 residue-maximality plus nonnegative relative height and a neutral endpoint is expensive. Across all 29 possible length-28 Sturmian mechanical factors, the largest neutral language has

\[
707250
\]

words, versus `69^4` unrestricted aligned L7 block choices, giving the finite extra cost

\[
-\frac1{28}\log_2\frac{707250}{69^4}
=0.1786513243\ldots>\frac7{50}.
\]

However this cost does **not** persist at long excursion length. Exact aligned-factor scans give the worst neutral-return L7 cost per time step

\[
\begin{array}{c|c}
L&\text{extra cost (bits/step)}\\\hline
28&0.1786513243\ldots\\
42&0.1427681777\ldots\\
56&0.1193952056\ldots\\
84&0.0891739142\ldots\\
140&0.0693173091\ldots
\end{array}
\]

and every audited factor through length 140 admits neutral words with exactly one positive excursion.

Hence the tempting claim

\[
\text{`every neutral return costs >7/50 per step'}
\]

is false as an asymptotic theorem. The loss is ballot-like and dilutes with excursion length.

## 6. Refined hard-core decomposition

The asymptotic nonperiodic hard core is therefore better written as

\[
\boxed{
\text{sparse completed neutral returns}
\quad+\quad
\text{long open-positive critical meanders}.
}
\]

The sparse-return channel carries only sublinear return-indexed state complexity. The unresolved linear-rate problem is the open-positive interval itself, where the ternary selector must repeatedly choose the correct newly exposed dyadic children without using retroactive repair.

This points back to the growing-resolution child-correlation quantity

\[
\varepsilon_L=K_L/M_D(L)
\]

and its odd-frequency representation as the principal Stage-4 object.