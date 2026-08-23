# Audit: repeated local residue-maximality needs a global pullback theorem

Date: 2026-08-23

Status: **dependency correction. The finite local residue-class computations remain exact, but repeated L7/L14/L19 maximality along a hypothetical minimal-counterexample trajectory is not justified by root minimality alone. All Stage-4 reductions on the current draft branch that use repeated local residue-maximality must therefore be read as conditional on the missing global pullback theorem. This is not a proof of Collatz.**

## 1. The local sibling identity is correct

For a length-`L` block with the same local odd count `q`, let `w` be the actual word and `u` a sibling in the same full-Hensel correction class:

\[
R_u-R_w=3^q\Delta,
\qquad \Delta\in\mathbb Z_{>0}.
\]

Starting the sibling at the local state `x-Delta` gives exactly the same local endpoint as starting `w` at `x`:

\[
\frac{3^q(x-\Delta)+R_u}{2^L}
=
\frac{3^qx+R_w}{2^L}.
\]

This algebraic identity is valid.

## 2. Why it does not automatically contradict the original minimum

Let the original hypothetical minimal counterexample be `N`, and suppose the local block starts later at a state `x>N`.

The sibling starts at `x-Delta<x`, but minimality of `N` is contradicted only if the sibling construction produces a counterexample below `N` (or otherwise pulls back to a smaller root start). In general one may have

\[
N<x-\Delta<x.
\]

An exact L7 example is

\[
q=5,
\quad R_w=211,
\quad R_u=454,
\quad R_u-R_w=3^5,
\quad \Delta=1.
\]

Take

\[
x=12895,\qquad x-\Delta=12894.
\]

The two valid seven-step parity paths are

\[
12895\to19343\to29015\to43523\to65285\to97928\to48964\to24482,
\]

and

\[
12894\to6447\to9671\to14507\to21761\to32642\to16321\to24482.
\]

They merge exactly at `24482`. If an original root minimum were, for example, `N=6000`, the entire sibling prefix would still stay above `N`. The local construction would therefore produce a smaller continuation than `x`, but not a smaller-than-`N` start merely from this block.

The point is logical, not a claim that `6000` is a Collatz counterexample.

Certificate:

`collatz/src/local_residue_maximality_pullback_audit.py`.

## 3. Exact root-pullback obstruction

Suppose the local block begins after an earlier fixed prefix of length `t` containing `p` odd steps.

Keeping that earlier prefix unchanged and replacing only the local block, equality of the final endpoints forces the change in the original root to be

\[
\boxed{
\Delta_{\rm root}
=\frac{2^t\Delta}{3^p}.
}
\]

Because

\[
\gcd(2^t,3^p)=1,
\]

an integer root predecessor requires

\[
\boxed{3^p\mid\Delta.}
\]

This is the missing global divisibility condition.

For the exact local credit maxima already certified in the repository:

- L7: `Delta_max=21`, and `21<3^3`; after `p>=3` prior odd steps no nonzero local credit can independently pull back as an integer;
- L14: `Delta_max=2730<3^8`; after `p>=8` the same obstruction holds;
- L19: `Delta_max=87381<3^11`; after `p>=11` it holds.

Thus a long trajectory cannot be pruned by treating each bounded local sibling replacement as an independent smaller root predecessor.

## 4. What would repair the argument

Repeated local residue-maximality can still become valid if a separate theorem proves that local credits from many blocks can be coupled so that the accumulated predecessor credit satisfies every backward Hensel divisibility constraint.

That theorem must carry the earlier odd-count/prefix information, equivalently the global credit/Hensel syndrome. Schematically the needed recursion is

\[
\delta_i
=\frac{\Delta_i 3^{q_i}+2^{L_i}\delta_{i+1}}{3^{q_i}},
\]

with integrality at every backward boundary and a final positive integer root shift.

The existing height-credit cocycle controls the **amplitude** of such a credit if it exists, but it does not by itself prove existence of a compatible integer pullback for an arbitrary sequence of local nonmaximal blocks.

Therefore the missing object is:

> **Global residue-maximality pullback theorem.** Show that a sufficiently rich sequence of non-maximal local blocks forces at least one positive Hensel-compatible integer predecessor at the original root, with all intermediate credit states integral and admissible.

Without this theorem, the local L7 entropy loss `>7/50` cannot be promoted to a repeated deterministic global language-exclusion rate.

## 5. Consequence for the current Stage-4 draft branch

The following finite calculations remain arithmetically correct as conditional automaton statements:

- the `K<15` 28-step threshold derived from the L7 exclusion rate;
- the high-height and low-height state reductions;
- the phase-coupled reductions to H=0,1;
- the L7+L14 strengthening.

However their use in an unconditional Collatz proof program depends on the missing pullback theorem above.

The unconditional baseline therefore reverts to the previously established coefficient/formation exclusion rate

\[
\delta_{\rm form}
=1-H_2(\log_3 2)
\approx0.05004447281,
\]

plus the exact m=45 first-window transversality and renewal computations that do not use repeated local maximality.

## 6. Valid replacement: whole-prefix maximality

Root minimality *does* directly imply maximality for the **entire parity prefix starting at N**. If a full length-H prefix has a same-q sibling with

\[
R_u-R_w=3^q\Delta>0,
\]

then `N-Delta<N` is itself the correctly pulled-back sibling start and merges after H steps.

This whole-prefix statement is rigorous because there is no earlier prefix denominator `3^p` to clear.

An exact class DP through depth 32 shows, however, that among coefficient-surviving prefixes the full-Hensel class map is injective through every tested depth: the class counts equal the coefficient-survivor word counts (for example `3,524,586` at depth 28 and `41,347,483` at depth 32). Therefore whole-prefix maximality gives no additional finite pruning in this range.

The next useful route is not another local-maximality layer, but either:

1. prove the global Hensel-compatible pullback theorem; or
2. obtain a cross-base/endpoint quotient theorem directly from the unconditional coefficient-survivor language.
