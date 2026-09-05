# Finite-address deterministic-tail lemma

Date: 2026-08-24

Status: **exact auxiliary theorem for canonical Collatz residue search.** It is a finite-state reduction, not a proof of the Collatz conjecture.

## 1. Canonical binary-step state

At depth `k`, write the canonical parity-prefix state as

\[
(k,q,r,y),
\]

where `r` is the least nonnegative start representative modulo \(2^k\), `q` is the odd count, and \(y=T^k(r)\) is the corresponding endpoint.

When a desired next parity symbol \(b\in\{0,1\}\) is appended, the unique canonical lift digit is

\[
\boxed{c=b\oplus (y\bmod2).}
\]

Hence

\[
\boxed{r'=r+c2^k.}
\]

If \(c=1\), the affine endpoint before the new Collatz step shifts by exactly \(3^q\):

\[
y\mapsto y+3^q.
\]

This is the transition used by `minimal_survivor_branch_bound.cpp`.

## 2. Threshold theorem

Fix an integer bound \(B\) and choose \(L\) with

\[
\boxed{B\le2^L.}
\]

Consider any canonical branch satisfying

\[
0\le r<B.
\]

At every depth \(k\ge L\), a nonzero lift digit would give

\[
r'=r+2^k\ge2^k\ge2^L\ge B,
\]

contradicting the threshold condition. Therefore

\[
\boxed{c=0\qquad(k\ge L).}
\]

Since \(c=b\oplus(y\bmod2)\), this forces

\[
\boxed{b=y\bmod2.}
\]

Thus after depth \(L\), every sub-\(B\) canonical branch follows the actual parity of its current endpoint and has **exactly one possible continuation**.

Equivalently:

> below a fixed finite start bound, canonical-address branching ends once the dyadic modulus exceeds that bound; the remaining tail is the ordinary deterministic Collatz trajectory.

## 3. Consequence for threshold min-plus searches

To decide whether there exists a coefficient-surviving canonical start \(r<B\) through an arbitrarily large horizon \(H\ge L\), it is enough to:

1. enumerate/compress the admissible canonical frontier only through depth \(L\);
2. retain states with \(r<B\);
3. propagate each retained state along its unique actual Collatz tail.

No new canonical lift choices appear after depth \(L\).

This does **not** imply that the depth-\(L\) frontier is small. The remaining computational problem is to compress the finite address frontier itself.

## 4. Current remaining resonance layers

For the standard recursively-sufficient ternary layer

\[
N=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

the exact layer maximum is

\[
\boxed{N_{\max}(m)=6\,3^m+1.}
\]

Therefore

\[
N_{\max}(44)=5{,}908{,}625{,}413{,}101{,}667{,}397{,}287<2^{73},
\]

\[
N_{\max}(45)=17{,}725{,}876{,}239{,}305{,}002{,}191{,}859<2^{74}.
\]

Hence the two current-resonance layers that remain after the m=46 defect exclusion reduce to

\[
\boxed{m=44:\text{ a 73-bit canonical-address frontier},}
\]

\[
\boxed{m=45:\text{ a 74-bit canonical-address frontier}.}
\]

After those depths, every candidate tail is deterministic.

## 5. Role

This reduction separates two issues cleanly:

- **finite cross-base formation:** which ternary 0/1 selector integers land in the admissible 73/74-bit canonical frontier;
- **deterministic survival:** once that integer is fixed, whether its unique trajectory remains coefficient-surviving/no-descent over the certified long horizon.

The lemma removes any need to model an infinite parity-choice tree for the fixed m=44 and m=45 layers. It does not by itself close either layer.
