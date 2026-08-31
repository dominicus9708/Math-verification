# A0 s=1 Route-B finite-horizon family quotient theorem

## Purpose

This note extracts an exact family-level theorem from the already-certified channel/block parameter partition.

The goal is to avoid expanding a large finite parameter interval into singleton Collatz starts whenever the predicate being tested depends only on a fixed finite future horizon or on a quotient state of that horizon.

This is an exact finite-horizon theorem. It does **not** assert that C4F or full Route-B membership factors through a bounded horizon.

## Parent channel

Fix an exact parity-prefix channel

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\qquad m\in\mathbb Z.
\]

For every binary block \(B\in\{0,1\}^{\ell}\), the existing block-jump theorem gives a unique residue

\[
\mu_B\pmod{2^\ell}
\]

such that the next \(\ell\) parity bits of the parent parameter \(m\) equal \(B\) exactly when

\[
m\equiv\mu_B\pmod{2^\ell}.
\]

Moreover

\[
B\longmapsto \mu_B
\]

is a permutation of \(\{0,1\}^\ell\) onto \(\mathbb Z/2^\ell\mathbb Z\).

Thus the complete length-\(\ell\) block family is an exact partition of the parent parameter axis: no overlap and no omission.

---

## Theorem 1 — finite-horizon predicate periodicity

Let

\[
P:\{0,1\}^{\ell}\to\{0,1\}
\]

be any predicate depending only on the next \(\ell\) parity bits.

Define the accepted residue set

\[
R_P
:=
\{\mu_B\bmod2^\ell:P(B)=1\}.
\]

Then for every parent parameter \(m\),

\[
\boxed{
P(\operatorname{next}_\ell(m))=1
\iff
m\bmod2^\ell\in R_P.
}
\]

Therefore every finite-horizon predicate is exactly periodic on the parent parameter axis with period dividing \(2^\ell\).

### Proof

The block-to-parameter theorem supplies exactly one block \(B\) for each parameter residue modulo \(2^\ell\), and exactly one residue for each block. Pulling the accepted block set \(P^{-1}(1)\) through this bijection gives \(R_P\). No probabilistic or asymptotic argument is used.

---

## Theorem 2 — exact interval family decomposition

Let

\[
I=[M_0,M_1]\cap\mathbb Z
\]

be any finite parent parameter interval.

For each accepted residue \(a\in R_P\), define

\[
I_a
=
\{m\in I:m\equiv a\pmod{2^\ell}\}.
\]

Then

\[
\boxed{
\{m\in I:P(\operatorname{next}_\ell(m))=1\}
=\bigsqcup_{a\in R_P}I_a.
}
\]

The union is disjoint.

Each nonempty \(I_a\) has the exact parametrization

\[
m=a+2^\ell k,
\]

where

\[
\left\lceil\frac{M_0-a}{2^\ell}\right\rceil
\le k\le
\left\lfloor\frac{M_1-a}{2^\ell}\right\rfloor.
\]

Hence the number of accepted starts in a huge interval can be counted exactly from residue families; enumeration of individual starts is unnecessary.

---

## Theorem 3 — quotient-state family compression

Let

\[
\sigma:\{0,1\}^{\ell}\to Q
\]

be any exact state map, and suppose a predicate factors through that state:

\[
P(B)=F(\sigma(B)).
\]

For each state \(s\in Q\), define its parameter-residue fiber

\[
R_s
=
\{\mu_B: \sigma(B)=s\}.
\]

Then the parent parameter axis may be grouped by state fibers rather than by individual words:

\[
\boxed{
\sigma(\operatorname{next}_\ell(m))=s
\iff
m\bmod2^\ell\in R_s.
}
\]

Thus a legal semantic quotient immediately induces an exact family quotient on every parent channel.

If \(\sigma\) is compositional under block concatenation, the state of a macroblock can be evaluated recursively or by block powering without materializing all of its bits.

---

## Relation to existing Route-B states

Two exact states are already available:

1. correction state \((h,q,C)\), which reconstructs the full exact prefix channel and composes by
   \[
   C(uv)=3^{q(v)}C(u)+2^{h(u)}C(v);
   \]
2. pure ballot/address state
   \[
   \Sigma_K=(n,q,dq,s_{\min},D,A_K),
   \]
   which exactly preserves pure ballot validity and 2-adic address propagation.

However, the existing ballot/address certificate explicitly states that this quotient does **not** by itself preserve C4F. The correction-state certificate likewise does not claim C4F or unique-target membership.

Therefore it is not yet legal to merge Route-B families merely because these arithmetic states agree.

The missing semantic statement is now isolated:

> Find an exact C4F-sufficient signature \(\sigma_{C4F}\), or prove that C4F factors through a composition of already certified state coordinates plus a finite/hierarchical amount of extra metadata.

Once such a factorization is proved, Theorem 3 converts it immediately into an exact parameter-family closure rule.

---

## Hierarchical handoff

The Christoffel/Stern-Brocot run certificate already shows that the target word of enormous ordinary length is represented by a small run hierarchy and that the existing composable state can be reconstructed by run powering.

Thus the desirable next theorem is not a fixed absolute-resolution theorem. It is a **semantic hierarchy factorization theorem**:

\[
\boxed{
\text{C4F decision}
=
F(\text{run-composable state},\text{finite boundary metadata}).
}
\]

If this holds, the family quotient above can work at run/block scale instead of bit scale.

---

## DSD audit

### Closed exactly

✅ complete length-\(\ell\) block family partitions a parent parameter axis by residues modulo \(2^\ell\);

✅ every predicate of the next \(\ell\) bits is an exact union of arithmetic parameter families;

✅ any legal finite quotient state induces an exact family quotient;

✅ finite interval cardinalities can be computed without singleton enumeration;

✅ compositional quotient states can be evaluated hierarchically without materializing every bit.

### Not promoted

❌ no claim that C4F depends on a uniformly bounded \(\ell\);

❌ no claim that the existing ballot/address state preserves C4F;

❌ no claim that correction-state equality alone proves Route-B membership;

❌ no global long-language closure;

❌ no Collatz conclusion.

## Gate update

The family-level problem has been separated into two parts:

- **arithmetic family transport:** CLOSED for every finite horizon;
- **semantic C4F factorization:** OPEN.

Consequently, the next bottleneck is no longer the approximately \(10^{20}\)-sized SAFE source population itself. The remaining question is the minimum semantic state needed to decide C4F on compressed block/run families.
