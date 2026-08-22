# Fresh-shell Haar splice: exact post-atomic obstruction

Date: 2026-08-22

Status: **negative/structural result.** This note identifies where a pure selector-Haar energy argument cannot close the repeated fresh-shell record contraction. It narrows the remaining proof front but does not prove the Collatz conjecture.

Let the ternary selector distribution at depth `r` be

\[
\mu_{m,r}
\]

on `Z/2^r Z`, with collision probability

\[
p_r(m)=\sum_x\mu_{m,r}(x)^2
\]

and Haar increment energy

\[
e_r(m)=2p_{r+1}(m)-p_r(m).
\]

The dyadic density martingale satisfies

\[
\boxed{\|\Delta_r g_m\|_2^2=2^r e_r(m).}
\]

The bounded-record terminal theorem supplies infinitely many fresh dyadic shells with a record-side contraction

\[
|\widehat\mu_{\rm rec}(t)|\le\kappa_M<1
\]

at every non-singleton record under an eventual record bound `M`.

It is tempting to argue that repeatedly repairing these contractions would require divergent selector Haar energy. This works only in the pre-atomic range.

## 1. Exact atomic threshold

The selector values are

\[
S_m=3^m+\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

For two selector values, their difference has absolute value at most

\[
\frac{3^m-1}{2}.
\]

Therefore, once

\[
\boxed{2^r>\frac{3^m-1}{2},}
\]

congruence modulo `2^r` implies actual equality. Distinct selector words occupy distinct residues, so

\[
\boxed{p_r(m)=2^{-m}.}
\]

The same remains true at depth `r+1`, hence

\[
\boxed{e_r(m)=2^{-m}.}
\]

Consequently the Haar energy is

\[
\boxed{
\|\Delta_r g_m\|_2^2
=2^{r-m}.
}
\]

Thus selector Haar energy grows exponentially with `r-m` after the selector has become atomic.

## 2. Why the naive repeated-repair contradiction fails

Suppose each non-singleton record required a fixed positive amount of selector Haar energy on a fresh shell. Before atomicity, orthogonality across shells can make such a lower-bound strategy useful.

After atomicity, however, the available selector energy on level `r` is already of size

\[
2^{r-m}.
\]

There is therefore no finite lifetime energy budget whose exhaustion would contradict infinitely many later fresh shells. A fixed contraction factor `kappa_M<1` can in principle be matched by an atomic selector whose high dyadic bits are fully resolved.

So the implication

\[
\text{infinitely many fresh record contractions}
\Longrightarrow
\text{selector Haar energy contradiction}
\]

is **false as a standalone argument**.

## 3. Correct division of labor

The proof architecture must distinguish two regimes.

### Pre-atomic bulk

Before

\[
2^r>\frac{3^m-1}{2},
\]

the selector is genuinely spread over dyadic residues. The existing Haar/martingale collision telescope and mixed Beatty-boundary pairings remain useful.

### Post-atomic tail

After that threshold, the selector consists of `2^m` isolated ordinary integers. The problem is no longer distributional. One must use arithmetic information specific to ordinary finite starts, such as

- the eventual-zero Hensel lift;
- canonical-residue high-bit zeros of a positive integer;
- record first-passage constraints;
- 2-adic/3-adic parity-series identities;
- deterministic min-plus or prefix-pullback structure.

Thus the correct architecture is now

\[
\boxed{
\text{Haar-controlled pre-atomic bulk}
\longrightarrow
\text{ordinary-integer/Hensel post-atomic tail}.
}
\]

This is sharper than the previous generic `bulk -> sparse tail` statement because the transition scale is explicit.

## 4. Consequence for bounded-record tails

The bounded-record branch currently provides

1. strengthened parity entropy `eta_M > eta_coeff`;
2. infinitely many non-singleton record shells;
3. a uniform record-side shell contraction `kappa_M<1`;
4. exclusion of singleton-only tails;
5. exclusion of eventually periodic high-density tails.

The new obstruction says that item 3 cannot be iterated to infinity using selector `L^2` energy alone. Once the original selector family is atomic, the remaining theorem must be genuinely arithmetic.

Therefore the next useful target is:

> **Post-atomic bounded-record Hensel theorem.** Show that no fixed positive ordinary integer can realize an aperiodic, eventually `M`-bounded record first-passage tail with infinitely many non-singleton terminal pairs.

That theorem is now the exact deterministic remainder of the bounded-record branch.
