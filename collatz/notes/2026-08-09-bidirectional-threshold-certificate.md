# Bidirectional threshold certificate for the minimal survivor

Date: 2026-08-09

Status: **DERIVED NECESSARY-AND-SUFFICIENT FINITE CERTIFICATE + INDEPENDENT CHECK**

This note combines the forward finite-horizon quotient with the backward interval-count recursion.  The target is a yes/no certificate for a proposed lower bound on the minimal coefficient survivor.

It does not prove any asymptotic growth theorem for `mu(K)`.

## 1. Forward split state

Fix target depth `K` and split depth `k`, with

\[
m=K-k.
\]

Use the exact forward quotient state

\[
(q,\eta),
\qquad
\eta=y\bmod2^m,
\]

and let

\[
\boxed{D_k(q,\eta)=r}
\]

be the smallest canonical start reaching that signature while surviving the coefficient barrier through depth `k`.

By the proved finite-horizon quotient, larger starts in the same signature have the same future carry/lift response and can never improve the final minimum.

## 2. Backward exact lift

Set

\[
M=2^m,
\qquad
\xi=3^{-q}\eta\pmod M.
\]

The exact minimum high-bit lift is

\[
J=J_{k,q,m}(\xi).
\]

Thus the exact minimum target-depth start represented by the forward signature is

\[
\boxed{V(q,\eta)=r+2^kJ.}
\]

## 3. Proposed threshold X

Let `X>=1` be a proposed lower bound for `mu(K)`.

If

\[
r\ge X,
\]

this state is already harmless.

Suppose

\[
r<X.
\]

The condition

\[
r+2^kJ<X
\]

is equivalent, because `J` is integral, to

\[
J<L_X(r),
\]

where

\[
\boxed{
L_X(r)
=\left\lceil\frac{X-r}{2^k}\right\rceil.
}
\]

Equivalently the dangerous lift values are exactly

\[
J\in\{0,1,\ldots,L_X(r)-1\}.
\]

## 4. Backward interval certificate

By the exact interval-count theorem,

\[
J\ge L
\iff
N_{k,q,m}(\xi,L)=0.
\]

Therefore the forward state cannot produce any target-depth start below `X` iff

\[
\boxed{
N_{k,q,m}\!\left(
3^{-q}\eta,
\left\lceil\frac{X-r}{2^k}\right\rceil
\right)=0.
}
\]

## 5. Global necessary-and-sufficient certificate

Let `Q_k` be the exact set of forward quotient representatives at the split.
Then

\[
\boxed{
\mu(K)\ge X
}
\]

iff for every representative `(q,eta)` with

\[
r=D_k(q,\eta)<X,
\]

we have

\[
\boxed{
N_{k,q,m}\!\left(
3^{-q}\eta,
\left\lceil\frac{X-D_k(q,\eta)}{2^k}\right\rceil
\right)=0.
}
\]

This is exact in both directions:

- a zero count excludes every dangerous high-bit lift for that forward state;
- a positive count supplies at least one admissible lift and therefore a canonical target-depth start below `X`.

Hence a failed certificate can carry an explicit witness rather than merely returning an inconclusive bound.

## 6. Special case 2^k > X

If

\[
2^k>X
\]

and `r<X`, then

\[
0<X-r<2^k,
\]

so

\[
\boxed{L_X(r)=1.}
\]

Thus the only dangerous future lift is

\[
J=0.
\]

The certificate reduces to asking whether the no-additional-high-bit continuation survives to `K`.

This is the exact finite-horizon form of the core-reconstruction principle: once the split bit-length exceeds the candidate bound, the tail cannot introduce an independent positive lift without exceeding that bound.

## 7. Independent checks

An independent Wolfram implementation used the exact forward quotient and the exact backward interval-count recursion.

### K=30

At split

\[
k=15,
\]

for

\[
X=27
\]

there are no surviving split representatives with `r<27`, so the certificate succeeds immediately.

For

\[
X=28,
\]

one state enters the candidate set, with

\[
r=27,
\]

and its length-one backward interval count is positive.  Hence the certificate fails, reproducing

\[
\boxed{\mu(30)=27.}
\]

### K=100

Again use

\[
k=15,
\qquad 2^{15}=32768.
\]

For

\[
X=10087,
\]

there are 394 exact forward representatives with `r<X`.  Every one has

\[
L_X(r)=1,
\]

and every corresponding backward interval count is zero.  Therefore

\[
\mu(100)\ge10087.
\]

For

\[
X=10088,
\]

there are 395 representatives.  The newly included state

\[
r=10087
\]

has a positive length-one backward count, so the stronger threshold fails.
Thus the bidirectional certificate independently reproduces

\[
\boxed{\mu(100)=10087.}
\]

These computations agree with the exact record-basin table already stored in the repository.

## 8. Formation-pruning interpretation

The certificate has the exact structure needed for safe complement removal:

1. forward formation determines all admissible low-bit signatures below `X`;
2. each signature determines a finite dangerous high-lift interval;
3. the E/O backward count proves whether that realization interval is empty;
4. only zero-count blocks are removed;
5. if all dangerous blocks are empty, the complement below `X` is exhausted.

Thus the pruning is exhaustive rather than probabilistic.

## 9. Complexity interpretation

For one state the backward interval length is

\[
L_X(r)=\left\lceil\frac{X-r}{2^k}\right\rceil.
\]

The exact interval recursion has `O(m L_X(r))` nonempty recursion nodes, ignoring arithmetic bit complexity.

Choosing `k` near or above `log_2 X` makes every dangerous interval have length at most one.  The computational burden then moves almost entirely to the number of forward coefficient-surviving representatives below `X`.

This is a finite-certificate optimization, not an asymptotic proof that this number is small enough uniformly in `K`.

## 10. Next theorem target

The remaining global difficulty can now be stated sharply:

> For a target threshold `X(K)`, control the number and structure of forward signatures with `D_k<X(K)` whose transformed endpoint has a nonempty dangerous backward interval.

For the first-crossing branch, existing polynomial candidate upper bounds allow a logarithmic split with only zero-lift tails.
For the infinite coefficient-survival branch, an asymptotic lower bound on `mu(K)` still requires a uniform theorem controlling these forward/backward alignments.
