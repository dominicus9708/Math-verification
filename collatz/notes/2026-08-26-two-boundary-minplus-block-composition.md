# Two-boundary Hensel min-plus block composition

Date: 2026-08-26

Status: **exact operator identity / proof architecture.** This note does not yet bound the full first-resonance operator and does not prove the Collatz conjecture.

## 1. Block state

Traverse a terminal mechanical gap block from right to left.  Let

\[
w=(g_1,\ldots,g_L),\qquad g_i\in\{1,2\}.
\]

A state consists of

\[
S=(K,p),
\]

where `K` is the current zero-target 3-adic Hensel carry and `p` is the current earliest displacement.  At the i-th prepend choose a new displacement `d` satisfying

\[
d\ge \max\{0,p-g_i+1\}
\]

and

\[
K+2^{e_i-d}\equiv0\pmod3.
\]

The new state is

\[
\boxed{
K'={K+2^{e_i-d}\over3},\qquad p'=d.
}
\]

Continuation through another digit additionally requires `K'` to remain a 3-adic unit.

## 2. Normalized real cost

Normalize the single-step mechanical weight at the right boundary to `w_0=1`.  Moving one odd ordinal to the left across gap `g_i` changes the mechanical weight by

\[
\boxed{
w_i=w_{i-1}{3\over2^{g_i}}.}
\]

The dimensionless real correction cost of displacement `d_i` is

\[
\boxed{
\kappa_i(d_i)=2w_i(1-2^{-d_i}).
}
\]

Thus a controlled path through the block has cost

\[
J_w=\sum_{i=1}^L\kappa_i(d_i).
\]

## 3. Block scale

Define

\[
\boxed{
\lambda(w)=\prod_{i=1}^L{3\over2^{g_i}}
={3^L\over2^{G(w)}},
\qquad
G(w)=\sum_{i=1}^Lg_i.
}
\]

This is exactly the mechanical weight scale between the two ends of the block.

## 4. Two-boundary transfer operator

For right state `S` and left state `T`, let

\[
\mathcal T_w(S,T)
\]

be the infimum of `J_w` over all displacement controls realizing an admissible Hensel/ordering path from `S` to `T`.  If no such path exists, set the value to `+infinity`.

The operator retains both boundary states.  This is essential: the controllability audit proves that after discarding boundary data an arbitrary finite block can have zero cost.

## 5. Exact concatenation law

Let `u` be traversed first and `v` second, so the concatenated gap word is

\[
w=uv.
\]

The reference weight entering `v` has already been multiplied by `lambda(u)`.  Therefore, for any intermediate state `R`,

\[
J_{uv}=J_u+\lambda(u)J_v.
\]

Minimizing over the interface state gives the exact weighted min-plus convolution

\[
\boxed{
\mathcal T_{uv}(S,T)
=
\inf_R
\left[
\mathcal T_u(S,R)
+
\lambda(u)\mathcal T_v(R,T)
\right].
}
\]

Also

\[
\boxed{
\lambda(uv)=\lambda(u)\lambda(v).
}
\]

No probabilistic independence or asymptotic approximation is used.

## 6. Why this matters at the first resonance

The first-resonance gap word is a rational mechanical/Christoffel word associated with

\[
{A\over Q}={114208327604\over72057431991}.
\]

Its continued fraction is

\[
[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,10].
\]

The huge final quotient structure means the length-`Q` word is recursively built from much shorter Euclidean blocks.  Once the exact orientation/conjugacy of the first-resonance gap word with the standard Christoffel recursion is certified, the same recursion can be applied to the transfer operators using the formula above.

Thus the intended computation is not

\[
Q\approx7.2\times10^{10}
\]

individual Hensel steps.  It is an `O(log Q)` hierarchy of block compositions, provided the state/interface representation can also be compressed.

## 7. Remaining obstruction

The word-length compression is now exact, but the state space is still potentially large because `K` is 3-adic and `p` is unbounded a priori.  The next theorem must supply one of:

1. a finite quotient of boundary states sufficient for a lower bound;
2. a Bellman dual potential `Phi(K,p)` giving a blockwise lower certificate;
3. a dominance relation that discards higher-cost states without losing the two-boundary minimum.

The terminal low-support computations provide exact finite regression cases for any proposed state compression.

## 8. DSD audit interpretation

The DSD reorganization is now

\[
\boxed{
\text{local Hensel controls}
\to
\text{boundary-preserving block operator}
\to
\text{Euclidean/Christoffel hierarchy}
\to
\text{global bridge cost}.
}
\]

The earlier sign-only reduction failed because it projected away a control variable.  The block operator retains that variable while still allowing the `10^11`-scale word to be compressed structurally.
