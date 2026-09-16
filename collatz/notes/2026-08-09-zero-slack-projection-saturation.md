# Zero-slack projection saturation and the limit of fixed low-bit filters

Date: 2026-08-09

Status: **DERIVED LEMMA / NEGATIVE RESULT FOR FIXED-MODULUS PROOF ROUTES**

This note identifies an exact projective self-similarity of the coefficient-survivor language. It is a limitation theorem: fixed low-bit information cannot become increasingly restrictive merely by forcing a much deeper zero-slack endpoint.

## 1. Coefficient-survivor language

Let

\[
\alpha=\log_3 2,
\qquad
a_j=\lceil\alpha j\rceil.
\]

A binary parity word

\[
w=b_0b_1\cdots b_{B-1}
\]

of length `B` is coefficient-surviving iff its prefix odd-counts

\[
q_j(w)=\sum_{i=0}^{j-1}b_i
\]

satisfy

\[
\boxed{q_j(w)\ge a_j\qquad(1\le j\le B).}
\]

Let `P_B` denote this set of words.

By the classical parity-vector bijection, `P_B` is in one-to-one correspondence with the canonical coefficient-surviving residue classes modulo `2^B`; denote that residue set by `A_B`.

## 2. Zero-slack target language

For `h>=B`, let

\[
P^{(0)}_h
=
\{v\in P_h:q_h(v)=a_h\}
\]

be the coefficient-surviving length-`h` words ending exactly on the coefficient boundary, i.e. with final slack zero.

Let

\[
\pi_B:P_h\to\{0,1\}^B
\]

be truncation to the first `B` parity bits.

Clearly

\[
\pi_B(P_h^{(0)})\subseteq P_B,
\]

because every prefix of a surviving word also survives.

## 3. Every surviving prefix extends to zero slack

Take any

\[
w\in P_B
\]

and let

\[
q_B=q_B(w)\ge a_B.
\]

Choose any target depth `h>=B` such that

\[
\boxed{a_h\ge q_B.}
\]

For every `j` with `B<=j<=h`, define the desired cumulative odd-count

\[
\boxed{Q_j:=\max(q_B,a_j).}
\]

Then:

1. `Q_B=q_B`;
2. `Q_h=a_h`, because `a_h>=q_B`;
3. `Q_j>=a_j` for every intermediate `j`;
4. since `a_{j+1}-a_j in {0,1}`, also
   \[
   Q_{j+1}-Q_j\in\{0,1\}.
   \]

Therefore the bits

\[
\boxed{b_j:=Q_{j+1}-Q_j\qquad(B\le j<h)}
\]

form a valid binary continuation of `w`.

The resulting length-`h` word survives every coefficient prefix and has

\[
q_h=Q_h=a_h.
\]

Hence

\[
\boxed{w\text{ extends to an element of }P_h^{(0)}.}
\]

No probability, residue-distribution assumption, or numerical search is involved.

## 4. Uniform saturation depth

The previous statement is prefix-dependent through `q_B`. Since trivially

\[
q_B\le B,
\]

a single sufficient target depth for **every** surviving length-`B` prefix is any `h` satisfying

\[
\boxed{a_h\ge B.}
\]

Equivalently, because `a_h=ceil(alpha h)`, one may take

\[
\boxed{
h\ge\left\lceil\frac{B-1}{\alpha}\right\rceil+1}
\]

as a simple explicit sufficient range.

Thus for every such `h`,

\[
\boxed{
\pi_B(P_h^{(0)})=P_B.
}
\]

This is the **zero-slack projection saturation theorem**.

## 5. Residue-class form

Via the parity-vector / residue correspondence, reduction modulo `2^B` maps the canonical residue set of the deep zero-slack language onto the full depth-`B` survivor residue set:

\[
\boxed{
A_h^{(0)}\bmod2^B=A_B
}
\]

for all sufficiently large `h` as above.

Therefore the least positive low-`B` residue visible among arbitrarily deep zero-slack words is exactly

\[
\boxed{
\min(A_B\setminus\{0\})=\mu(B),
}
\]

where `mu(B)` is the minimal coefficient survivor at depth `B`.

This does **not** mean that one fixed integer `mu(B)` itself extends indefinitely. Different deep words lifting the same low-`B` residue generally require different higher bits.

## 6. Independent computational cross-check

The defect-channel transfer derived independently from the fixed-cell correction formula produced a stabilized low-bit support. Wolfram comparisons found exact equality with the directly enumerated depth-`B` survivor residues for every tested

\[
2\le B\le14.
\]

Representative counts were

| B | survivor residues | stabilized zero-slack low-B residues | least positive residue |
|---:|---:|---:|---:|
| 5 | 4 | 4 | 7 |
| 6 | 8 | 8 | 7 |
| 7 | 13 | 13 | 27 |
| 8 | 19 | 19 | 27 |
| 10 | 64 | 64 | 27 |
| 12 | 226 | 226 | 27 |
| 14 | 734 | 734 | 27 |

The table is only a cross-check; the surjectivity theorem above is elementary and exact.

## 7. Consequence for fixed low-bit pruning

Suppose one attempts to rule out arbitrarily deep coefficient-surviving words using only a fixed modulus `2^B` or only the first `B` parity bits.

The saturation theorem shows that, once the target depth is large enough, every depth-`B` survivor class reappears as the projection of a deep zero-slack survivor word.

Therefore no argument based **only** on membership in a fixed set of low-`B` survivor residues can become stronger with increasing target depth.

In particular,

\[
\boxed{
\text{a proof of }\mu(K)\to\infty
\text{ must use a resolution }B=B(K)\to\infty
\text{ or an equivalent cross-depth consistency constraint.}
}
\]

This is a negative result for fixed-modulus finite-state closure, not for growing-window automata or threshold cores.

## 8. Relation to the current finite-core program

The threshold-core theorem chooses

\[
B\approx\log_2 U(K),
\]

so its resolution grows with the proposed candidate bound. It is therefore not contradicted by projection saturation.

Likewise the bidirectional certificate uses a target-dependent split and exact backward interval information, so it retains the cross-depth consistency that fixed low bits alone lose.

The present theorem explains why this growth of resolution is not merely a computational choice but structurally necessary.

## 9. Relation to defect channels

Inside a deep zero-slack cell, the low-`B` defect transfer stabilizes precisely because every surviving `B`-bit prefix can be completed back to the mechanical boundary.

Thus the stabilized defect-channel automaton is not a mysterious new subset: it is another presentation of the ordinary depth-`B` survivor language.

This observation prevents overinterpreting low-bit stabilization as evidence for convergence. Its value is instead diagnostic: it isolates the genuinely hard information in the **compatibility of an increasing sequence of lifts as B grows**, i.e. in the same-integer / min-plus anti-alignment problem.

## 10. Revised global target

The unresolved problem should therefore be formulated across scales:

> Given a nested sequence of coefficient-surviving parity cylinders, prove that the least compatible positive integer representative must grow sufficiently rapidly with the cylinder depth.

Equivalently, in the forward/backward split formulation, prove that small forward canonical cost and small future lift cannot remain aligned as the required resolution grows.

This is exactly the anti-alignment target already isolated by the two-channel Bellman recurrence.