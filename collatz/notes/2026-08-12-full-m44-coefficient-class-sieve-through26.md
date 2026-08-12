# Full `m=44` coefficient-class sieve through depth 26

Date: 2026-08-12

Status: **exact full-block static-aggregation certificate**. The entire `2^44` recursively sufficient `m=44` block is aggregated into dyadic residue classes; no start-by-start trajectory enumeration is used. Through time 26, the q-sensitive/additive-free theorem identifies coefficient crossing with actual descent, so the class sieve removes more than 93.8% of the full block by exact propositions on residue classes. This does not prove the remaining 6.18% recursive.

## 1. Full block

Write

\[
N=4Y+3,
\qquad
Y=3^{44}+\sum_{i=0}^{43}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

There are exactly

\[
\boxed{2^{44}=17,592,186,044,416}
\]

representatives in this block.

For a binary depth `L`, the first `L` parity bits depend only on

\[
N\pmod{2^L},
\]

or equivalently, because `N=4Y+3`, on

\[
\boxed{Y\pmod{2^{L-2}}.}
\]

Thus the complete block may be statically aggregated by the cyclic generating function

\[
\boxed{
X^{3^{44}}
\prod_{i=0}^{43}(1+X^{3^i})
\pmod{X^{2^{L-2}}-1}.
}
\]

Its coefficient at residue `r` is the exact number of `m=44` starts in that dyadic class.

## 2. Exact dynamical class predicate

Let

\[
a_k:=\lceil k\log_3 2\rceil.
\]

A reduced residue class survives the coefficient barrier through depth `L` exactly when its parity prefix satisfies

\[
q_k\ge a_k
\qquad(1\le k\le L).
\]

The q-sensitive correction theorem proves that for the present huge starts this coefficient test is equivalent to actual non-descent at least through `L=26` (indeed the unrestricted q-sensitive envelope is valid through 191, while the first-crossing Christoffel refinement is much stronger).

Therefore every class rejected below has an exact ordinary descent

\[
T^k(N)<N
\]

for some `k<=L`, uniformly for every block member in that class.

## 3. Full-block survivor mass

Exact aggregation gives

\[
\boxed{
\begin{array}{c|r|r|c}
L&\text{survivor dyadic classes}&\text{survivor block mass}&\text{mass fraction}\\\hline
18&7,495&2,011,923,507,477&0.1143646106514\\
20&27,328&1,833,950,905,184&0.1042480394735\\
21&46,611&1,564,005,133,050&0.0889033988784\\
23&168,807&1,416,055,503,075&0.0804934360914\\
24&286,581&1,202,007,610,492&0.0683262220771\\
25&573,162&1,202,007,610,492&0.0683262220771\\
26&1,037,374&1,087,765,074,138&0.0618322857314
\end{array}
}
\]

The plateaus occur when the coefficient boundary does not rise at the new bit.

At depth 26 only

\[
\boxed{1,087,765,074,138}
\]

of the original representatives remain dangerous at class level.

Hence

\[
\boxed{
93.8167714269\%}
\]

of the complete `m=44` block is certified to descend below its own start within the first 26 accelerated steps.

This is not a scan of `93.8%` of the starts. The largest static state space used is only

\[
\boxed{2^{24}=16,777,216}
\]

reduced dyadic residues.

## 4. Formation-only transport at L=25 -> 26

At the active transition `L=25 -> 26`, the current survivor mass is

\[
C_{25}=1,202,007,610,492.
\]

The mass lying on one-child coefficient-boundary parents is

\[
\boxed{
M_D=228,484,933,625.
}
\]

The full ternary formation measure has opposite-child imbalance

\[
\boxed{
U_{23}(44)=6,445,500,202.
}
\]

Therefore the dynamics-independent inequality

\[
|K_{25}|\le U_{23}(44)
\]

gives

\[
\boxed{
\frac{|K_{25}|}{M_D}
\le0.0282097384.
}
\]

Even if the ternary child imbalance were aligned with the unique dangerous child in the worst possible sign, more than 48% of this boundary mass would still be removed at the new bit.

The actual signed class correlation is much smaller:

\[
\boxed{K_{25}=-139,083,}
\]

so

\[
\boxed{
K_{25}/M_D\approx-6.0872\times10^{-7}.
}
\]

The exact next mass is

\[
C_{26}=1,087,765,074,138.
\]

## 5. Significance for the set/proposition route

The inference chain is now entirely class-level:

\[
\boxed{
\text{44 ternary selector variables}
\to
\text{cyclic subset-sum coefficients}
\to
\text{coefficient-survivor dyadic classes}
\to
\text{global representative mass}.}
\]

No ordinary start trajectory is followed individually.

This is a stronger realization of the intended calculus-like approach than the earlier finite representative scans: one proposition on a residue cylinder removes all starts represented by one generating-function coefficient at once.

## 6. Remaining limitation

The survivor fraction is still positive. Fixed dyadic resolution cannot close the block by itself, and increasing `L` eventually makes the residue state space expensive.

The next theorem target is therefore not simply `L=27,28,...` by brute force. It is to bound the one-bit transport

\[
C_{L+1}
=\frac12\sum_{r\in R_L}[m(r)c(r)+v(r)u(r)]
\]

with a reusable lower bound on boundary mass and an upper bound on formation imbalance/correlation as the resolution grows.

The present full-block data show that this approach is quantitatively nontrivial: at `L=25`, the conservative formation-only imbalance is already less than 3% of the one-child boundary mass.

## 7. Reproducibility

Exact verifier:

`collatz/src/m44_full_coefficient_class_sieve_26.cpp`

It uses only unsigned integer arithmetic for the subset-sum counts and parity-class predicates.