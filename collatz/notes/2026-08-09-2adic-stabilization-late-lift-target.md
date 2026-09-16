# 2-adic stabilization and the late-lift forcing target

Date: 2026-08-09

Status: **DERIVED EQUIVALENCE / PROOF-TARGET REFORMULATION**

This note clarifies what an infinite coefficient-surviving parity path means arithmetically. It does not assert that such a path comes from a positive integer.

## 1. Nested canonical residues

Let

\[
w=b_0b_1b_2\cdots
\]

be an infinite binary parity path whose every finite prefix survives the coefficient barrier.

Let

\[
r_K\in[0,2^K)
\]

be the unique canonical start residue associated with the first `K` parity bits.

Compatibility of the parity cylinders gives

\[
\boxed{
r_{K+1}=r_K+c_K2^K,\qquad c_K\in\{0,1\}.}
\]

Therefore

\[
\boxed{
r_K=\sum_{j=0}^{K-1}c_j2^j.}
\]

The sequence converges in the 2-adic metric to

\[
\boxed{x=\sum_{j=0}^{\infty}c_j2^j\in\mathbb Z_2.}
\]

The bits `c_j` are exactly the canonical lift bits from the skew-product formulation.

## 2. Infinite survivor paths exist 2-adically

The coefficient-survivor parity tree is finitely branching.
There are surviving words of arbitrarily large finite depth; for example the all-odd word survives every coefficient barrier.

By the elementary infinite-tree compactness/Konig argument, there exists at least one infinite coefficient-surviving parity path.

Hence there exist 2-adic integers whose entire parity sequence remains in the coefficient-survivor language.

This observation is **not** a positive-integer counterexample. The arithmetic issue is whether the corresponding 2-adic canonical start belongs to the embedded nonnegative integers.

## 3. Ordinary integers are exactly eventually-zero lift sequences

For a 2-adic integer

\[
x=\sum_{j\ge0}c_j2^j,
\qquad c_j\in\{0,1\},
\]

the following are equivalent:

1. `x` is an ordinary nonnegative integer;
2. only finitely many binary digits `c_j` are nonzero;
3. there exists `B` such that
   \[
   c_j=0\qquad(j\ge B);
   \]
4. the canonical representatives `r_K` stabilize as ordinary integers for all sufficiently large `K`.

Indeed, an ordinary nonnegative integer has a finite binary expansion, and conversely an eventually-zero 2-adic binary expansion is the ordinary finite binary sum.

Thus an infinite coefficient-surviving parity path comes from a nonnegative integer iff its canonical lift sequence is eventually zero.

## 4. Coefficient-survival obstruction in lift language

Define the infinite-coefficient-survival property for a positive integer `n` by

\[
3^{q_K(n)}\ge2^K
\qquad\text{for every }K\ge1.
\]

Then such an integer exists iff there is an infinite coefficient-surviving parity path whose canonical lift bits are eventually zero and whose stabilized value is positive.

Therefore the coefficient-stopping target is equivalently:

\[
\boxed{
\text{Every infinite coefficient-surviving path has infinitely many }c_j=1.
}
\]

This is a 2-adic/non-Archimedean statement converted into an ordinary binary-support condition.

It concerns coefficient stopping, not by itself the complete Collatz conjecture.

## 5. Minimal-survivor growth and highest forced lift bit

For a finite length-`K` survivor,

\[
r_K=\sum_{j=0}^{K-1}c_j2^j.
\]

For an integer `B<K`,

\[
r_K<2^B
\]

iff

\[
\boxed{c_j=0\qquad(B\le j<K).}
\]

Hence

\[
\boxed{
\mu(K)\ge2^B
}
\]

iff every length-`K` coefficient-surviving canonical path has at least one nonzero lift bit at an index

\[
B\le j<K.
\]

If strict inequality at the endpoint `2^B` matters, one may adjust the threshold by one; the structural statement is unchanged.

Thus lower bounds for `mu(K)` are exactly **late-lift forcing statements**.

## 6. Polynomial growth target

Suppose the desired theorem is

\[
\mu(K)>C K^p.
\]

Set

\[
B(K)=\left\lceil\log_2(CK^p)\right\rceil.
\]

It is sufficient to prove that every length-`K` survivor has a canonical lift bit

\[
\boxed{c_j=1\text{ for some }j\ge B(K).}
\]

For the current sufficient exponent

\[
p=8.616,
\]

the forced-bit scale is only

\[
\boxed{
B(K)=8.616\log_2K+O(1).
}
\]

So the global growth target does not require controlling all `K` high bits. It requires proving that no coefficient-surviving path can finish its canonical binary start after only `O(log K)` bits.

This is exactly the finite-core scale appearing independently in the threshold and first-crossing reductions.

## 7. Relation to the record function

Recall

\[
M(B)=\max_{1\le n<2^B}\tau_c(n).
\]

The generalized inverse relation is

\[
\boxed{M(B)>K\iff\mu(K)<2^B.}
\]

In lift language, `M(B)>K` means that some coefficient-surviving length-`K` path has no nonzero canonical lift bits at positions `j>=B`.

Thus the two apparently different proof routes are identical at this level:

- grow `mu(K)` by forcing late lift bits;
- bound `M(B)` by showing that every fixed `B`-bit integer loses the coefficient barrier before too many additional steps.

## 8. Why fixed-modulus projection saturation is not a contradiction

The zero-slack projection-saturation theorem says every fixed surviving low-`B` prefix can be extended to arbitrarily deep zero-slack **formal parity words**.

Those extensions generally require new high lift bits `c_j=1` as the target depth grows. Therefore their canonical representatives change with depth and need not define one ordinary integer.

The actual proof obstruction is exactly the possibility of choosing the extensions compatibly while eventually setting every new high lift bit to zero.

This explains why fixed low-bit survivor membership is too weak while the growing-window min-plus / bidirectional certificate retains the needed information.

## 9. Carry-channel form

At a canonical state `(k,q;r,y)`, the exact next lift bit for requested E/O channel `b_k` is

\[
\boxed{c_k=b_k\oplus(y\bmod2).}
\]

Therefore late-lift forcing can also be stated as:

> any sufficiently long coefficient-surviving continuation of a small canonical start must eventually request an E/O channel whose parity disagrees with the current unlifted endpoint, forcing a new high binary start bit.

The Bellman recurrence chooses channels to delay/minimize these forced disagreements. Its value `J` is precisely the future high-bit word generated by the optimal sequence of such carry events.

## 10. Revised proof target

The most direct asymptotic target is now:

**Late-Lift Forcing Target.** Prove that there exists `p>8.616` (or at least the needed current exponent) and `K_0` such that every coefficient-surviving parity path of length `K>=K_0` contains a nonzero canonical lift bit at some index

\[
j\ge p\log_2K+O(1).
\]

Equivalently, prove

\[
M(B)<2^{B/p+O(1)}
\]

in the inverse parameterization.

The exact interval-count, Bellman, defect-channel, and deterministic-endpoint tools in the repository can now be judged by whether they contribute to this specific forced-bit statement.