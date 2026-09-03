# Pure-ballot macroblock non-contraction

Status: **EXACT / CLOSED as a representation theorem**

## Purpose

The active A0, s=1, Route-B source engine may compile several successive legal valuation jumps

\[
0^{a_1}1,\ldots,0^{a_d}1
\]

into one exact macroblock.  This theorem records what that compilation can and cannot accomplish.

It can remove intermediate transition nodes.  By itself it cannot contract the exact terminal source-family partition.

## Setup

Let the current exact source channel be

\[
X=r+2^h m,\qquad T^h(X)=y+3^q m,
\]

with pure-ballot control `(h,S)`.

Let \(\mathcal A_d(h,S)\) be the set of legal depth-\(d\) valuation tuples

\[
\mathbf a=(a_1,\ldots,a_d)
\]

under the exact valuation-jump ballot gate.

Each tuple defines the parity macroblock

\[
B(\mathbf a)=0^{a_1}1\cdots0^{a_d}1.
\]

The existing valuation-macroblock theorem gives exact equality between sequential valuation refinement and one direct multibit transition by \(B(\mathbf a)\).

## Theorem 1 — depth-d leaf blocks are prefix-free

Every block \(B(\mathbf a)\) contains exactly \(d\) ones and terminates at its \(d\)-th one.

If two distinct depth-\(d\) blocks were in a strict prefix relation, the shorter block would already contain the \(d\)-th one before the longer block terminates, which is impossible for a longer block containing exactly \(d\) ones and terminating at its own \(d\)-th one.

Therefore

\[
\boxed{\mathcal B_d(h,S)=\{B(\mathbf a):\mathbf a\in\mathcal A_d(h,S)\}\text{ is prefix-free}.}
\]

## Theorem 2 — direct compilation preserves the exact leaf partition

For every \(\mathbf a\in\mathcal A_d(h,S)\), exact macroblock compilation selects exactly the same source parameter residue and the same child affine channel as the corresponding sequential valuation jumps.

Distinct prefix-free parity blocks describe disjoint parity-prefix source cylinders.  Hence there is a one-to-one correspondence

\[
\boxed{
\text{sequential legal depth-}d\text{ leaves}
\longleftrightarrow
\text{direct legal depth-}d\text{ macroblock children}.
}
\]

Consequently macroblock compilation alone cannot reduce the number of exact terminal source families selected by the same pure-ballot predicate.

It can only avoid materializing the internal nodes of the same finite control tree.

## Current eight-jump frontier calculation

The certified eight-jump frontier has

\[
14{,}224
\]

source cylinders and 90 exact `(h,S)` controls.

Starting from the 14 retained roots and applying only the exact pure-ballot control recurrence, the control-path multiplicities through four additional valuation jumps are

| total jump depth | exact path/cylinder-control leaves |
|---:|---:|
| 8 | 14,224 |
| 9 | 34,318 |
| 10 | 93,000 |
| 11 | 209,784 |
| 12 | 609,808 |

Thus sequential four-step evaluation materializes

\[
34{,}318+93{,}000+209{,}784+609{,}808
=946{,}910
\]

child nodes.

Direct depth-four macroblock evaluation materializes only the terminal

\[
609{,}808
\]

leaves, saving

\[
337{,}102
\]

intermediate child constructions, or

\[
\boxed{35.6002154376\%}
\]

of those child-construction operations.

However the terminal leaf cardinality remains exactly the same control-tree cardinality.

The existing horizon-four quotient contains 13 reusable pure-ballot control signatures.  Their reuse reduces duplicated control-language evaluation, not source payload cardinality.

## DSD interpretation

This separates three notions that must not be conflated:

1. **control quotient** — equal future pure-ballot transition skeleton;
2. **execution compression** — evaluate a multi-jump block without materializing internal nodes;
3. **source-family contraction** — prove that fewer exact source families need remain.

The first two are CLOSED here.  The third does not follow.

An actual S10 contraction therefore requires an additional admissibility predicate or a proved source/formation quotient that rejects or safely merges terminal source families.  Pure-ballot compilation alone cannot provide it.

## Scope restrictions

This theorem does **not** prove:

- equality of source payloads sharing one control signature;
- a source merge from equal `(h,S)`;
- any new Route-B membership rejection beyond the pure-ballot gate;
- deterministic formation-rank renewal;
- checkpoint membership or same-orbit connectivity;
- A0 s=1 Route-B closure;
- Collatz.

## Certificate

- `../src/A0_s1_pure_ballot_macroblock_noncontraction_certificate.py`
