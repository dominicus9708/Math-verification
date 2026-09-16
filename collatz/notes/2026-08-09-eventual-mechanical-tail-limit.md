# Eventual mechanical-tail extension and the limit of defect-density-only exclusion

Date: 2026-08-09

Status: **DERIVED LIMITATION THEOREM**

This note clarifies the scope of the high-correction defect-density condition. It proves that near-unit mechanical-cap density alone cannot exclude any fixed finite coefficient-surviving prefix. The missing arithmetic condition is zero-lift compatibility with one ordinary integer.

## 1. Coefficient barrier

Let

\[
\alpha=\log_3 2,
\qquad
a_k=\lceil\alpha k\rceil.
\]

A parity prefix of length `B` survives the coefficient barrier iff its accumulated odd counts `q_k` satisfy

\[
q_k\ge a_k
\qquad(1\le k\le B).
\]

Fix any such prefix and put

\[
r=q_B.
\]

Then `r>=a_B`.

## 2. Canonical minimal extension of the odd-count path

For `k>=B`, define

\[
\boxed{Q_k=\max(r,a_k).}
\]

Because `a_{k+1}-a_k` is always 0 or 1,

\[
Q_{k+1}-Q_k\in\{0,1\}.
\]

Therefore `Q_k` is the accumulated odd-count function of a valid binary parity extension of the fixed prefix.

Moreover,

\[
Q_k\ge a_k
\]

for every `k>=B`, so the extension survives the coefficient barrier forever as a formal parity word.

## 3. Eventual exact mechanical-cap positions

Let

\[
\kappa_i=\lfloor i\log_2 3\rfloor
=\left\lfloor\frac{i}{\alpha}\right\rfloor.
\]

For the pure minimal barrier path `q_k=a_k`, the i-th zero-based odd position is exactly `kappa_i`: the jump

\[
a_{k+1}-a_k=1
\]

corresponding to the `(i+1)`-st odd step occurs at

\[
k=\kappa_i.
\]

For the extension `Q_k=max(r,a_k)`, no new odd step is used while `a_k<=r`. Once the barrier catches up, every subsequent odd-count increment is exactly an increment of `a_k`.

Since

\[
r\ge\lceil\alpha B\rceil>\alpha B,
\]

we have

\[
\kappa_i\ge B
\qquad(i\ge r).
\]

Hence every new odd position of index `i>=r` is exactly

\[
\boxed{d_i=\kappa_i=\lfloor i\log_2 3\rfloor.}
\]

Thus the defect coordinates

\[
z_i=\kappa_i-d_i
\]

have finite support: after the fixed prefix there is an extension with

\[
\boxed{z_i=0\quad\text{for all }i\ge r.}
\]

## 4. Density consequence

For any fixed finite surviving prefix and any `epsilon>0`, choose a sufficiently long endpoint odd count `q`. The eventual-mechanical extension above has only finitely many nonzero defect coordinates, so

\[
\frac{\#\{i<q:z_i>0\}}{q}<\epsilon
\]

for all sufficiently large `q`.

Equivalently, its exact mechanical-cap density tends to one:

\[
\boxed{
\lim_{q\to\infty}
\frac{\#\{i<q:d_i=\kappa_i\}}{q}=1.
}
\]

Therefore a condition such as

\[
\#\{i:d_i=\kappa_i\}\ge0.894q
\]

cannot by itself exclude any fixed finite coefficient-surviving prefix.

## 5. Why this does not produce an ordinary counterexample

The extension constructed above is a **formal parity extension**. By the classical parity-vector/residue correspondence, each longer prefix has a canonical start residue modulo a larger power of two. In general these canonical representatives require new high lift bits.

If the original finite prefix comes from an ordinary integer `x<2^B`, then the same ordinary integer realizes the formal extension only when every later canonical lift bit is zero:

\[
\boxed{c_j=0\qquad(j\ge B).}
\]

Thus the actual obstruction is not high mechanical density by itself. It is the conjunction

\[
\boxed{
\text{near-mechanical correction}
\quad+\quad
\text{zero-lift continuation of one fixed integer}.
}
\]

This is exactly the late-lift / high-resolution cylinder condition already isolated elsewhere in the repository.

## 6. Consequence for the next resonance

The certified `m=46` condition requiring at least about `89.44%` exact mechanical-cap coordinates remains a valid necessary condition for a paradoxical candidate. However, the present theorem shows that this density condition cannot be combined with only the first 75 parity bits to obtain a contradiction: every surviving 75-bit prefix admits a formal tail with cap density tending to 100%.

Any successful exclusion must therefore use information that distinguishes the formal 2-adic extension from the actual 75-bit integer, for example:

- zero-lift constraints after bit 75;
- deterministic endpoint evolution of the fixed integer;
- a cross-base theorem coupling the ternary core to those later lift bits;
- or an exact automaton/certificate that preserves the ordinary-integer realization.

## 7. Proof-program correction

This result prevents overinterpreting the defect-density bound. The proof target should no longer be stated as merely

> a 75-bit recursive-core start cannot have a near-mechanical parity extension.

That statement is false at the level of formal parity extensions.

The correct target is

> a 75-bit recursive-core **ordinary integer** cannot realize, with no later canonical lifts, a near-mechanical first-crossing parity word of the required enormous length.

The distinction is essential.