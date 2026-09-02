# S10 residual correction recursion audit

Date: 2026-09-03

Status: **SAFE structural advance / principal inversion gate remains OPEN**

## Audited claim

For an exact realized prefix `A` of a candidate word `W=AB`, with

\[
|A|=K,\quad q(A)=p,\quad |W|=t,\quad q(W)=Q,
\]

source `X`, prefix state `Y=T^K(X)`, and proposed endpoint `Z`, define

\[
C_{req}=2^tZ-3^QX.
\]

Using

\[
C(W)=3^{Q-p}C(A)+2^KC(B)
\]

and

\[
C(A)=2^KY-3^pX,
\]

the exact residual is

\[
\boxed{
\frac{C_{req}-3^{Q-p}C(A)}{2^K}
=2^{t-K}Z-3^{Q-p}Y.
}
\]

Therefore

\[
C(W)=C_{req}
\iff
C(B)=2^{|B|}Z-3^{q(B)}Y.
\]

Canonical theorem:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`.

## DSD audit classification

### D — domain

SAFE only after `A` is an exact realized source/control prefix with the stated `K,p`.

### R — resolution

The theorem is exact integer equality.  Any quotient replacing `Y` or `Z` by residues/intervals needs a separate future-predicate sufficiency proof.

### S — state sufficiency

For the correction-equality recursion, old `C(A)` is redundant after the exact current state `Y`, remaining counters, future-control class, and endpoint state are retained.

### E — equivalence

Two histories may be merged only when they induce the same certified future correction-realization problem. Numerical residual equality alone is insufficient if future grammar/source controls differ.

### T — transition

The residual problem has the same affine correction form as the parent problem. This gives an exact recursive transition rather than a heuristic descent.

### C — closure

No language closure follows merely from the recursion identity. Existence of a legal suffix remains to be decided.

### N — non-independence

`C_req mod 2^K` and an exact source prefix are not independent pruning channels. The residual recursion explicitly removes this double counting.

### O — outstanding obligations

1. finite-block inverse quotient/transducer;
2. exact future-control merge theorem for the implemented state;
3. direct-enumeration regression at finite depths;
4. application to the retained 14 roots;
5. S11 checkpoint/debit/tail realization after S10 candidates survive.

## Result

The previous S10 state proposal can be reduced:

- do **not** carry a growing dyadic correction coordinate alongside an exact source prefix;
- discharge an exact prefix block;
- restart the exact correction equation from `Y` with the remaining counters;
- retain only predicate-relevant future observations;
- merge only states with proven identical future realization sets.

This is a genuine state-space simplification, but not yet a proof of Route-B closure or Collatz.
