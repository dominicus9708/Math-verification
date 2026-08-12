# `m=44` cross-place cylinder static aggregation

Date: 2026-08-12

Status: **exact finite cross-place sieve on the full `m=44` recursively sufficient block**. It combines a low ternary address, a dyadic forward cylinder, exact forward descent, and positive `3`-adic back-tracing into one class-level exclusion theorem. At resolution `Q=6`, `B_max=18`, it removes exactly `16,215,917,600,511` of the `2^44` block members without enumerating their trajectories individually. This does not close the block or prove Collatz.

## 1. Core block

Write

\[
F_{44}:=
\left\{
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

The block has cardinality

\[
\boxed{|F_{44}|=2^{44}=17,592,186,044,416.}
\]

Let

\[
N_{\min}=4\cdot3^{44}+3,
\qquad
N_{\max}=6\cdot3^{44}+1.
\]

A hypothetical minimal counterexample in this block must never descend below itself and cannot have a smaller positive integer merge into any of its forward states.

## 2. Ternary address cylinder

Fix an integer `Q<=44` and the low selector word

\[
u=(a_0,\ldots,a_{Q-1}).
\]

Because the fixed term `3^44` and every selector term `3^i` with `i>=Q` vanish modulo `3^Q`, the word `u` fixes

\[
\boxed{
N\equiv
n_u:=3+4\sum_{i=0}^{Q-1}a_i3^i
\pmod{3^Q}.}
\]

Thus only `2^Q` ternary address cylinders occur, rather than all `3^Q` residues.

## 3. Dyadic forward cylinder

Fix a forward depth `B>=0` and a residue

\[
r=N\pmod{2^{B+1}}.
\]

The first `B` time-expanded Collatz parity symbols and the parity of the endpoint `T^B(N)` are completely determined by this residue.

Write the exact affine map of the first `B` steps as

\[
\boxed{
T^B(N)=\frac{3^{q(r)}N+R(r)}{2^B}.}
\]

The pair `(q(r),R(r))` is therefore constant on the whole dyadic cylinder.

### Forward descent exclusion

Every member of the cylinder is impossible as a minimal counterexample whenever

\[
\boxed{
(3^{q(r)}-2^B)N+R(r)<0
}
\]

for every

\[
N\in[N_{\min},N_{\max}].
\]

Because the left side is affine in `N`, it is enough to check one endpoint of the interval according to the sign of `3^q-2^B`.

This removes a complete dyadic cylinder at once.

## 4. Cross-place endpoint address

Assume the endpoint `y=T^B(N)` is odd. For a fixed ternary address `u`, its residue modulo `3^Q` is exactly

\[
\boxed{
z_{u,r}
\equiv
\left(3^{q(r)}n_u+R(r)\right)2^{-B}
\pmod{3^Q}.}
\]

Thus the pair

\[
\boxed{(u,r)}
\]

determines simultaneously:

1. the forward binary/parity cylinder;
2. the `3`-adic endpoint address available to back-tracing.

This is the basic cross-place cylinder.

## 5. Reverse ancestor channel

Take a positive odd-to-odd back-tracing code from `y` with

\[
q'\le Q,
\qquad
K=\text{total binary exponent}.
\]

Write its reverse affine relation as

\[
\boxed{
m=\frac{2^K y-C}{3^{q'}},}
\qquad C>0.
\]

The code is admissible on one endpoint residue class modulo `3^{q'}`, hence its admissibility is determined by `z_{u,r}`.

Substituting the forward affine map gives

\[
\boxed{
m-N
=
\frac{
(2^K3^{q(r)}-2^B3^{q'})N
+2^K R(r)-2^B C
}{2^B3^{q'}}.}
\]

Therefore the entire cross-place cylinder is impossible whenever the numerator is strictly negative for every

\[
N\in[N_{\min},N_{\max}],
\]

and the resulting ancestor is positive.

Again this is an affine interval test, so one endpoint suffices according to the sign of the coefficient of `N`.

A successful test constructs a positive integer

\[
\boxed{0<m<N}
\]

which merges into the forward orbit at `T^B(N)`. Such an `N` cannot be a minimal counterexample.

## 6. Reverse-state dominance

For a fixed reverse depth, current `3`-adic residue, and total exponent `K`, suppose two reverse codes have correction constants

\[
C_1<C_2.
\]

Then for every positive endpoint `y`,

\[
\frac{2^K y-C_2}{3^q}
<
\frac{2^K y-C_1}{3^q}.
\]

Hence the larger correction is always at least as strong for constructing a smaller ancestor.

Therefore, in the reverse finite-state computation, for each state

\[
(q,\text{residue},K)
\]

one need retain only the maximal `C`.

This is an exact min/max dominance quotient; it prevents reverse-code enumeration from becoming the proof object.

## 7. Static aggregation of the ternary core

The cross-place conditions above classify residue cylinders, not individual starts. Their exact multiplicities inside `F_44` are obtained by a cyclic subset-sum generating function.

Fix the low ternary word `u`. The remaining selector variables contribute

\[
4\sum_{i=Q}^{43}a_i3^i
\pmod{2^{B_{\max}+1}}.
\]

Define

\[
\boxed{
G_{Q,B_{\max}}(X)
=
\prod_{i=Q}^{43}
\left(1+X^{4\cdot3^i}\right)
\quad\text{in}\quad
\mathbb Z[X]/(X^{2^{B_{\max}+1}}-1).}
\]

The coefficient of `X^s` is exactly the number of assignments of the high ternary selectors whose dyadic contribution is `s` modulo `2^{B_max+1}`.

Hence the size of every cross-place cylinder `(u,r)` is an exact coefficient of this one finite group-algebra product.

No list of the `2^44` integers is required.

## 8. Exact `Q=6`, `B_max=18` certificate

Use

\[
\boxed{Q=6,\qquad B_{\max}=18.}
\]

The finite partition uses only

- `2^6=64` low ternary cylinders;
- dyadic residues modulo `2^19`;
- forward affine maps through depth at most `18`;
- positive reverse codes of odd-depth at most `6`;
- reverse-state dominance;
- and the exact group-algebra multiplicities from Section 7.

A cylinder is deleted as soon as either:

1. an exact forward descent `T^B(N)<N` is certified for all members; or
2. an exact positive reverse ancestor `m<N` merging into `T^B(N)` is certified for all members.

The exact counts are

\[
\boxed{
N_{\rm forward}=14,172,856,036,042,}
\]

\[
\boxed{
N_{\rm reverse-only}=2,043,061,564,469,}
\]

so

\[
\boxed{
N_{\rm excluded}=16,215,917,600,511.}
\]

The surviving count is

\[
\boxed{
N_{\rm survive}=1,376,268,443,905.}
\]

Therefore the certified removed fraction is

\[
\boxed{
\frac{16,215,917,600,511}{17,592,186,044,416}
\approx0.9217681963781956.}
\]

Thus more than

\[
\boxed{92.1768\%}
\]

of the complete `m=44` ternary core is removed at this very small cross-place resolution.

The reverse-only contribution is genuinely additional: these classes have not yet descended within the tested forward depths, but a smaller positive integer is proved to merge into one of their odd forward endpoints.

## 9. Direct integer witness audit

As a separate implementation audit, randomly selected excluded full 44-bit selector assignments were reconstructed as ordinary integers.

For every reverse-excluded sample, the recorded reverse code was applied with exact integer arithmetic and checked to satisfy

\[
0<m<N
\]

and, when followed forward through the reversed odd-to-odd exponent code,

\[
\boxed{m\longmapsto T^B(N)}.
\]

A 1,000-sample audit found no discrepancy.

This is not the proof of the class theorem; it is an independent implementation check of the symbolic affine/carry formulas.

## 10. Structural interpretation

This theorem combines three descriptions without collapsing them into a scalar density:

\[
\boxed{
\text{ternary Cantor address}
\times
\text{dyadic forward address}
\times
\text{3-adic predecessor address}.}
\]

The inference is

\[
\boxed{
\text{finite address class}
\Rightarrow
\text{one affine proposition}
\Rightarrow
\text{whole class removed}
\Rightarrow
\text{exact static aggregation of removed mass}.}
\]

This is much closer to the intended proposition/set/channel approach than start-by-start orbit enumeration.

## 11. What remains

The remaining `1,376,268,443,905` starts are not individually enumerated proof obligations. They are the aggregate mass of the cross-place cylinders not yet deleted at resolution `(Q,B_max)=(6,18)`.

The next theorem target is not merely to increase `B_max` computationally. It is to identify a reusable dominance, covering, or entropy statement showing that the surviving cross-place cylinder family contracts under increasing dyadic/backtrace resolution.

Possible next channels are:

1. strengthen `Q` while preserving the reverse dominance quotient;
2. characterize the survivor dyadic tree recursively rather than at one terminal modulus;
3. insert the exact R1 two-place potential on surviving cylinders only;
4. or prove that every sufficiently deep surviving cylinder must acquire a forbidden forward/reverse child.

No claim of global Collatz convergence or closure of the `m=44` block is made here.
