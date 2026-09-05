# A0 s=1 Route-B parameter-interval well-founded descent

## Purpose

The recursive long-word lift requires a branch of the form

> unresolved class -> strictly smaller recursive subproblem.

On the already SAFE-pruned 14-root source forest, the exact prefix-channel parameterization provides such a well-founded rank without any heuristic assumption.

This note proves that result and records its scope.

## Parent channel and exact child partition

A parent parity-prefix channel has the exact form

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with integer parameter interval

\[
m\in I=[L,U]\cap\mathbb Z.
\]

The next requested parity bit fixes one parity `m_0 in {0,1}` of the parent parameter and writes

\[
\boxed{m=m_0+2k.}
\]

Therefore the child parameter interval is exactly

\[
I_{m_0}
=
\left[
\left\lceil\frac{L-m_0}{2}\right\rceil,
\left\lfloor\frac{U-m_0}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

The two children are disjoint and their pullbacks partition the parent interval exactly.

## Cardinality descent lemma

Let

\[
N(I)=|I|=U-L+1
\]

for a nonempty finite integer interval.

Because the two parity classes partition consecutive integers,

\[
N(I_0)+N(I_1)=N(I),
\]

and their sizes differ by at most one. Hence

\[
\boxed{N(I_{m_0})\le \left\lceil\frac{N(I)}2\right\rceil.}
\]

If `N(I)>=2`, then

\[
\left\lceil\frac{N(I)}2\right\rceil\le N(I)-1.
\]

Therefore every nonempty child of a non-singleton parent satisfies

\[
\boxed{N(I_{m_0})<N(I).}
\]

Thus

\[
\boxed{R(I):=N(I)\in\mathbb N}
\]

is a valid well-founded descent rank for recursive source-channel refinement on the finite 14-root forest.

No infinite descendant chain can remain non-singleton.

## Logarithmic depth form

Define

\[
\ell(I)=\lceil\log_2 N(I)\rceil
\]

for `N(I)>=1`.

The cardinality inequality implies that every branch reaches a singleton after at most

\[
\boxed{\ell(I)=\lceil\log_2 N(I)\rceil}
\]

additional one-bit channel refinements.

This is a branch-depth bound, not a bound on the total number of leaves.

## Current 14-root forest bound

The certified 14-root forest retains in total

\[
N_{\rm total}=125072439875999947649
\]

integer source parameters.

Every individual root contains at most this many parameters, and

\[
2^{66}<N_{\rm total}<2^{67}.
\]

Therefore every root branch is guaranteed to become a singleton after at most

\[
\boxed{67}
\]

additional one-bit parameter refinements.

The deepest initial root has channel depth `38`, so the extremely loose forest-wide bound obtained by combining only these two maxima is

\[
38+67=105
\]

source-channel bits to singleton identification. This `105` is only a coarse global envelope; each actual root has its own smaller parameter count and therefore its own sharper depth bound.

## Relation to the recursive long-word A/B/C scheme

For the SAFE-pruned source forest, branch C can now be stated exactly:

- **A — closure:** the class is eliminated or enters an already certified closed condition;
- **B — state equivalence:** the class reaches an already certified decoder/state class;
- **C — source refinement:** choose the next parity child and replace interval `I` by `I_child`.

Whenever C acts on a non-singleton interval,

\[
\boxed{R(I_{child})<R(I).}
\]

Therefore C cannot repeat indefinitely inside the finite 14-root source domain.

## What this closes

✅ an explicit well-founded recursive rank exists on every finite root interval;

✅ exact child formation preserves all parent candidates with no overlap or omission;

✅ every individual source parameter becomes singleton after finite refinement;

✅ a coarse uniform branch-depth bound of 67 additional bits follows from the total retained count;

✅ the previously abstract requirement “C must descend to a strictly smaller recursive subproblem” is satisfied for source-interval refinement inside the SAFE-pruned forest.

## What this does not close

❌ singleton identification of `X` is not the same as a symbolic proof that its entire long correction word is Route-B admissible or inadmissible;

❌ the number of singleton leaves can still be enormous, so this theorem does not make brute-force enumeration practical;

❌ the theorem depends on the already established finite SAFE source intervals and does not itself prove those global bounds;

❌ a global long-language decoder still needs a rule that closes or reuses large families before singleton expansion;

❌ no global Collatz conclusion is claimed.

## DSD audit

This resolves one audit ambiguity cleanly:

- **candidate preservation:** exact, because child residue classes partition the parent parameter interval;
- **well-foundedness:** exact, because finite interval cardinality strictly decreases on every non-singleton child;
- **efficiency/global compression:** still open;
- **Collatz globalization:** still open.

The next bottleneck is therefore not termination of recursive refinement, but **family-level closure before the exponentially many singleton leaves are exposed**.
