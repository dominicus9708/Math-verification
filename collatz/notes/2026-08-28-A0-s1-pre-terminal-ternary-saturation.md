# A0 s=1: pre-terminal ternary projection saturates the unit group

Date: 2026-08-28

Status: **SAFE combinatorial projection theorem + REJECTED pruning route.** This does not prove the Collatz conjecture.

## 1. Question

The direct-intersection route had reduced the pre side to a last-28-odd ternary endpoint descriptor, with the hope that the admissible `0 -> 0` renewal bridge would occupy a sparse subset of

\[
\mathbb Z/3^{28}\mathbb Z.
\]

That hope is false.  In fact the same saturation persists through the full 47-trit depth that already exposes the ordinary checkpoint `Z<2^73`.

## 2. Terminal correction form

For the pre block

\[
X\xrightarrow{(t_0,j_0)} Z,
\]

write

\[
2^{t_0}Z=3^{j_0}X+R_-,
\qquad
R_-=
\sum_{r=1}^{j_0}3^{j_0-r}2^{a_r}.
\]

Modulo `3^m`, only the last `m` odd ordinals remain.  If their positions are

\[
a_{j_0-m+1}<\cdots<a_{j_0},
\]

then, after reversing their order,

\[
R_-
\equiv
\sum_{k=0}^{m-1}3^k2^{a_{j_0-k}}
\pmod{3^m}.
\]

Since `2^t0` is a unit, the possible `Z mod 3^m` are the same up to a unit permutation as the possible values of this sum.

## 3. Six-class lifting lemma

Let `S_r` be any unit modulo `3^r`.

For `r>1`, choose an exponent `e` such that

\[
2^e\equiv S_r\pmod3,
\]

but

\[
2^e\not\equiv S_r\pmod9.
\]

Then

\[
S_{r-1}:={S_r-2^e\over3}
\]

is again a unit modulo `3^{r-1}`.

The powers of two modulo nine are

\[
1,2,4,8,7,5,
\]

with period six.  For each unit `S_r mod 9`, exactly two exponent classes modulo six satisfy the two displayed conditions.  Therefore every interval of six consecutive exponents contains an admissible predecessor choice.

Inducting from `r=m` down to `r=1` produces strictly increasing odd-event positions whose weighted terminal sum equals any prescribed unit modulo `3^m`.

## 4. Embedding into the complete renewal ballot bridge

For the present application use `m=26,28,47` and place all constructed terminal odd events before

\[
t_0-6m.
\]

Exact directed logarithm bounds certify

\[
\boxed{
\left\lceil\alpha(t_0-6m)\right\rceil
\le j_0-m
}
\]

for all three depths.

Hence the earlier `j0-m` odd events may be placed densely at the beginning.  Before the terminal suffix begins, their count already dominates the complete renewal barrier; the terminal `m` events then raise the total to `j0`, and the endpoint has exact renewal height zero.

Thus the construction is not merely an unconstrained residue representation.  It lies inside the full **combinatorial** `0 -> 0` ballot-bridge language.

This construction does not assert that the resulting enormous parity address corresponds to a physical start `X<2^72`.

## 5. Saturation theorem

For

\[
m\in\{26,28,47\},
\]

the exact terminal projection is

\[
\boxed{
\mathcal Z_{\rm pre,term}^{(m)}
=(\mathbb Z/3^m\mathbb Z)^\times.
}
\]

In particular,

\[
3^{47}>2^{73}.
\]

Since the physical checkpoint satisfies

\[
2^{72}<Z<2^{73},
\]

the last 47 odd ordinals plus the complete ballot condition permit every ordinary checkpoint in that shell satisfying

\[
\boxed{3\nmid Z}.
\]

No additional ternary hole is created by the terminal ballot grammar.

## 6. Consequence for the debit coordinate

Because

\[
L_-=3X-Z,
\]

translation by `3X` preserves the unit/nonunit partition modulo every power of three.  Hence for fixed `X mod 3^26`, the terminal combinatorial language also allows every unit value of

\[
L_-\pmod{3^{26}}.
\]

Since the physical corridor already has `0<L_-<3^26`, terminal combinatorics alone restricts the ordinary debit only by

\[
\boxed{3\nmid L_-}.
\]

## 7. DSD audit

### SAFE

- finite-depth terminal Hensel/residue construction;
- exact six-class lifting induction;
- embedding of the constructed suffix in a complete renewal ballot bridge;
- saturation through the 47-trit ordinary-exposure depth.

### REJECTED

The planned route

\[
\text{deeper terminal ternary trie}
\to
\text{sparse }Z_{\rm pre}
\]

is rejected.

The exact trie is essentially trivial: the first ternary digit is nonzero and thereafter all three children remain possible.

### OPEN

The missing information is **correlation with the small physical start**.  A complete pre bridge must simultaneously satisfy

\[
X<2^{72}
\]

and the full dyadic parity address from `X` to `Z`.  Ballot admissibility and terminal ternary admissibility separately do not enforce that same-address correlation.

## 8. Revised next gate

The next Route-B object must couple the early dyadic start address with the terminal ternary endpoint address through the middle arithmetic bridge.  It cannot be a terminal-only trie.

Equivalently, the useful state is a bi-address / invariant representation retaining at least

\[
( X\bmod2^h,\ Z\bmod3^k )
\]

or an exactly equivalent Christoffel-DAG transfer, together with the physical ordinary bounds.

Companion certificate:

`collatz/src/A0_s1_pre_terminal_47trit_saturation_certificate.py`.
