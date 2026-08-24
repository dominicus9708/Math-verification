# Exact Beatty plateau annihilation and rise-boundary Fourier factorization

Date: 2026-08-24

Status: **exact all-depth Fourier identity for the coefficient-survivor language.**  This sharpens the odd-frequency part of the valuation boundary-projection theorem.  It is not yet a uniform decay theorem and is not a proof of the Collatz conjecture.

## 1. Coefficient-survivor tree

Let

\[
b_k:=q_{\min}(k)=\min\{q:3^q\ge2^k\}.
\]

A binary parity prefix of length `k` survives coefficient contraction iff its odd-count process satisfies

\[
q_j\ge b_j\qquad(1\le j\le k).
\]

Let \(P_k\) be the number of surviving length-\(k\) words.  By the parity-vector/canonical-residue bijection, these words are also a subset of \(\mathbb Z/2^k\mathbb Z\).

For `k>=2` the first two parity symbols are forced odd, so every survivor residue is `3 mod 4`; one may equivalently use the reduced coordinate

\[
y=(r-3)/4\pmod{2^{k-2}}.
\]

## 2. Dyadic sibling cancellation

Fix a surviving parent word `w` of length `k-1`, with odd count `q`.  Its two canonical depth-`k` children differ by exactly the top dyadic lift bit:

\[
r_1-r_0\equiv2^{k-1}\pmod{2^k}.
\]

Hence for every odd Fourier frequency `u`,

\[
e^{2\pi i u r_1/2^k}=-e^{2\pi i u r_0/2^k}.
\]

Whenever both children survive, their odd-frequency contributions cancel exactly.

## 3. Plateau steps vanish identically

Suppose the Beatty barrier does not rise at depth `k`:

\[
\boxed{b_k=b_{k-1}.}
\]

Every surviving parent already has `q>=b_{k-1}=b_k`.  Therefore both its even child (odd count `q`) and odd child (odd count `q+1`) survive the new coefficient threshold.

Thus every parent contributes a cancelling sibling pair.  Consequently

\[
\boxed{
\widehat\nu_k(u)=0
\qquad\text{for every odd }u,
\quad b_k=b_{k-1},
}
\]

where \(\nu_k\) is the uniform probability measure on the length-`k` coefficient-survivor residues.

This is an exact zero, not an asymptotic estimate.

Since the irrational Beatty staircase rises with frequency \(\log_3 2\), the complementary density

\[
1-\log_3 2\approx0.3690702464
\]

of depths have complete odd-frequency annihilation.

## 4. Rise steps leave only the boundary parents

Now suppose

\[
\boxed{b_k=b_{k-1}+1.}
\]

A surviving parent with `q>=b_k` again has two surviving children and cancels.

A parent with

\[
q=b_k-1=b_{k-1}
\]

has only one surviving child: the odd child.  These are exactly the height-zero Beatty-boundary parents.

Let \(B_k\) be their number, and let \(\beta_k\) be the uniform measure on their surviving odd children, viewed in the same canonical dyadic coordinate.

The full unnormalized odd Fourier sum is therefore exactly the boundary sum.  After normalization by the total survivor count,

\[
\boxed{
\widehat\nu_k(u)
=-\frac{B_k}{P_k}\,\widehat\beta_k(u),
\qquad u\text{ odd},
\quad b_k=b_{k-1}+1.
}
\]

(The overall minus sign depends only on the convention for the top lift bit and is irrelevant to magnitude.)

Hence

\[
\boxed{
|\widehat\nu_k(u)|
=\frac{B_k}{P_k}|\widehat\beta_k(u)|.
}
\]

The previously observed strong low-frequency decay therefore has two logically separate factors:

1. a purely combinatorial boundary fraction \(B_k/P_k\);
2. a genuine Fourier cancellation factor inside the boundary excursion measure \(\beta_k\).

The first factor alone is not exponentially small; the remaining theorem must control the second.

## 5. Excursion interpretation

Write

\[
h_j:=q_j-b_j.
\]

On a plateau step of the Beatty staircase, an actual odd symbol changes

\[
h\mapsto h+1,
\]

while an even symbol leaves `h` unchanged.

On a rise step, an actual even symbol changes

\[
h\mapsto h-1,
\]

while an odd symbol leaves `h` unchanged.

Therefore the boundary parents counted by \(B_k\) are exactly the nonnegative Beatty-driven excursions satisfying

\[
h_j\ge0,
\qquad h_{k-1}=0.
\]

Thus the unresolved odd-frequency problem is no longer the whole coefficient-survivor language.  It is the Fourier transform of one height-zero renewal/excursion language.

## 6. Relation to the valuation projection theorem

For a general nonzero frequency

\[
t=2^s u,
\qquad u\text{ odd},
\]

the valuation boundary-projection theorem reduces the weighted transfer to odd frequency `u` at effective depth

\[
K=k-s
\]

followed by an unweighted tail of rank at most `s+1`.

The present theorem identifies the rank-one odd-frequency component more sharply:

- if `K` is a Beatty plateau depth, it is exactly zero;
- if `K` is a Beatty rise depth, it is exactly the height-zero boundary excursion transform.

The next proof-level target is therefore:

> **Beatty Boundary Excursion Fourier Decay:** control \(\widehat\beta_K(u)\), uniformly enough in odd `u`, or jointly with the ternary selector Riesz product.

This is strictly narrower than the earlier generic Ballot Fourier Cancellation conjecture.
