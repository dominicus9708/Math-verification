# Exact interval-count certificates on transformed suffix sets

Date: 2026-08-09

Status: **DERIVED EXACT RECURSION + COMPLEXITY BOUND + EXHAUSTIVE SMALL CHECK**

This note provides a blockwise lower-bound certificate for the backward Bellman value.  It uses the exact E/O transformed-set recursion and does not enumerate the full future residue set.

## 1. Cyclic intervals

Let

\[
M=2^m
\]

and define the cyclic interval

\[
I_M(a,L)
=\{a,a+1,\ldots,a+L-1\}\pmod M,
\qquad 0\le L\le M.
\]

For the transformed admissible suffix set

\[
S_{k,q,m}\subset\mathbb Z/M\mathbb Z,
\]

define the exact interval count

\[
\boxed{
N_{k,q,m}(a,L)
=|S_{k,q,m}\cap I_M(a,L)|.
}
\]

## 2. Affine branch preimage of a cyclic interval

Both E/O set branches have the form

\[
F_c(u)=2u+c\pmod M,
\]

where

- E: `c=0`;
- O: `c=-g`, with `g=3^{-(q+1)} mod M`.

Let

\[
t=(a-c)\bmod M,
\qquad
\varepsilon=t\bmod2.
\]

The first point of `I_M(t,L)` having even parity occurs after offset `epsilon`.
After division by two, the exact preimage is again one cyclic interval modulo

\[
M'=2^{m-1}:
\]

\[
\boxed{
a'=rac{t+\varepsilon}{2}\pmod{M'},}
\]

\[
\boxed{
L'=\left\lfloor\frac{L+1-\varepsilon}{2}\right\rfloor.
}
\]

Therefore

\[
\boxed{
F_c^{-1}(I_M(a,L))
=I_{M'}(a',L')
}
\]

inside the child residue group.

## 3. Exact E/O count recurrence

The transformed set recursion is

\[
S_{k,q,m}
=
2S_{k+1,q,m-1}
\cup
\left(2S_{k+1,q+1,m-1}-g\right)
\pmod M,
\]

with only coefficient-admissible channels included.

Hence

\[
\boxed{
N_{k,q,m}(a,L)
=N_E+N_O,
}
\]

where

\[
N_E=
N_{k+1,q,m-1}(a_E',L_E')
\]

if

\[
3^q\ge2^{k+1},
\]

and

\[
N_O=
N_{k+1,q+1,m-1}(a_O',L_O')
\]

if

\[
3^{q+1}\ge2^{k+1}.
\]

The E preimage uses `c=0`; the O preimage uses `c=-g`.

Base cases:

- `L=0`: count zero;
- `m=0`: the residue group contains only zero, so every nonempty interval has count one;
- if `3^q>=2^(k+m)`, the tail is completely safe and `S` is the full group, so the count is exactly `L`.

## 4. Linear-in-interval-size certificate bound

The E branch has even affine image and the O branch has odd affine image.
Therefore, when both branches are admissible, their interval preimage lengths satisfy

\[
\boxed{L_E'+L_O'=L.}
\]

If one branch is forbidden, the sum is smaller.

At every recursion level, the sum of lengths over all nonempty active interval nodes is therefore at most the original `L`.
Since every nonempty node has length at least one, there are at most `L` active nodes per level.

Thus an uncached exact interval-count certificate has at most

\[
\boxed{O(mL)}
\]

nonempty recursive nodes, ignoring the bit-complexity of modular arithmetic.

This bound is independent of the possibly exponential cardinality of `S_{k,q,m}`.

## 5. Exact lower bound on the Bellman lift

Recall

\[
J_{k,q,m}(\xi)
=
\min_{s\in S_{k,q,m}}[s-\xi]_M.
\]

For any integer `L>=1`,

\[
\boxed{
J_{k,q,m}(\xi)\ge L
\iff
N_{k,q,m}(\xi,L)=0.
}
\]

Thus absence of transformed admissible points in one short cyclic interval is an exact certificate excluding every future lift

\[
C=0,1,\ldots,L-1.
\]

This provides a rigorous lower bound without constructing the full future language.

## 6. Blockwise lower bound

Let a block of transformed endpoint queries be

\[
B=I_M(a,B_0).
\]

If

\[
B_0+L-1\le M
\]

and

\[
\boxed{
N_{k,q,m}(a,B_0+L-1)=0,
}
\]

then for every query `xi` in the whole block `B`,

\[
\boxed{J_{k,q,m}(\xi)\ge L.}
\]

The reason is that

\[
\bigcup_{\xi\in B} I_M(\xi,L)
=I_M(a,B_0+L-1).
\]

Therefore one interval-count certificate can supply a lower bound for an entire block of carry states.

This is the requested **block-level certified dominance** mechanism.

## 7. Formation-pruning interpretation

For a proposed low-cost block, the count recurrence gives an exact finite witness of emptiness.
If the block is empty in the transformed admissible set, removing every state whose hypothetical counterexample realization would require that block preserves all actual survivor realizations.

In the language of the current Formation-Axiom use, this is a safe complement removal:

1. define the candidate low-lift block;
2. propagate its E/O inverse images exactly;
3. obtain zero terminal count;
4. prune the entire block only after the empty realization set is certified.

No density or probabilistic assumption is used.

## 8. Exhaustive verification

An independent Wolfram implementation compared the recursive interval count with direct construction of `S_{k,q,m}` for every coefficient-admissible state with

\[
0\le k\le3,
\qquad
0\le m\le5,
\]

for every cyclic start `a` and every interval length

\[
0\le L\le2^m.
\]

All counts agreed exactly.

## 9. Relation to Fourier and min-plus routes

Fourier inversion computes interval counts globally from all frequencies.
The present recursion computes the same integer count locally and exactly from the E/O channel structure.

For small intervals, this exact recursion has the resolution needed to distinguish zero from one survivor point, which a square-root-scale Fourier magnitude bound generally does not.

It can therefore serve as the final certification layer after any analytic or Fourier method narrows the set of potentially dangerous intervals.

## 10. Next target

The immediate next step is to combine:

- forward low-bit blocks from `D_k`;
- backward short-interval certificates from `N_{k,q,m}`;
- the safe-cylinder upper witness;

into a bidirectional branch-and-bound that prunes whole `(q,eta)` blocks rather than individual states.

A proof-relevant asymptotic advance would require a theorem showing that the number or total width of unresolved low-lift blocks grows sufficiently slowly with `K`.
