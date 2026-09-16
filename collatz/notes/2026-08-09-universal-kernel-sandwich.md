# Universal future-kernel sandwich

Date: 2026-08-09

Status: **DERIVED LEMMA / CERTIFIED MIN-PLUS BOUNDS**

This note sharpens the future-admissibility-kernel formulation. No global Collatz theorem is claimed.

## 1. Mechanical barrier discrepancy is at most one

Let

\[
\alpha=\log_3 2,
\qquad
a_n=\lceil \alpha n\rceil.
\]

For every `k>=0` and `j>=1`,

\[
A_j(k):=a_{k+j}-a_k.
\]

Because `alpha` is irrational, `alpha j` is never an integer for `j>=1`. For arbitrary real `x` and nonintegral `y`,

\[
\lceil x+y\rceil-\lceil x\rceil
\in\{\lfloor y\rfloor,\lceil y\rceil\}.
\]

Taking `x=alpha k` and `y=alpha j` yields

\[
\boxed{
A_j(k)\in
\{\lfloor\alpha j\rfloor,\lceil\alpha j\rceil\}.
}
\]

Thus the future coefficient barrier relative to any depth `k` differs from the straight irrational line `alpha j` by at most one integer at every prefix.

## 2. Actual, strong, and weak future languages

At depth `k`, write the odd-count slack as

\[
s=q-a_k\ge0.
\]

For an endpoint residue `x mod 2^m`, let `Q_j(x)` be the number of odd accelerated steps among its first `j` future steps.

The actual future kernel is

\[
B_{k,s,m}
=
\left\{x:\ s+Q_j(x)\ge A_j(k)\ \forall 1\le j\le m\right\}.
\]

Define the depth-independent strong and weak kernels

\[
\boxed{
B^+_{s,m}
=
\left\{x:\ s+Q_j(x)\ge \lceil\alpha j\rceil\ \forall j\le m\right\},
}
\]

\[
\boxed{
B^-_{s,m}
=
\left\{x:\ s+Q_j(x)\ge \lfloor\alpha j\rfloor\ \forall j\le m\right\}.
}
\]

Since

\[
\lfloor\alpha j\rfloor
\le A_j(k)
\le\lceil\alpha j\rceil,
\]

we have

\[
\boxed{
B^+_{s,m}\subseteq B_{k,s,m}\subseteq B^-_{s,m}.
}
\]

## 3. Adjacent-slack identity

Because `alpha` is irrational, `alpha j` is nonintegral for every positive integer `j`, so

\[
\lfloor\alpha j\rfloor
=\lceil\alpha j\rceil-1.
\]

Therefore

\[
s+Q_j(x)\ge\lfloor\alpha j\rfloor
\]

iff

\[
(s+1)+Q_j(x)\ge\lceil\alpha j\rceil.
\]

Hence the weak kernel is not an independent family:

\[
\boxed{
B^-_{s,m}=B^+_{s+1,m}.
}
\]

The universal sandwich consequently reduces to the adjacent-slack inclusion

\[
\boxed{
B^+_{s,m}
\subseteq
B_{k,s,m}
\subseteq
B^+_{s+1,m}.
}
\]

Thus only one universal strong-kernel family needs to be represented or computed.

## 4. Min-plus first-hit bounds

For the exact canonical state `(k,q;r,y)`, let

\[
\eta=y\bmod2^m,
\qquad m=K-k.
\]

For any target set `C subset Z/2^m Z`, define the affine first-hit functional

\[
\mathcal J_{q,\eta}(C)
:=
\min\left\{u\in[0,2^m):
\eta+3^q u\pmod{2^m}\in C
\right\}.
\]

The exact future lift value is

\[
J_{k,K}(q,\eta)
=\mathcal J_{q,\eta}(B_{k,s,m}).
\]

Define a single universal strong-kernel value

\[
\boxed{
J^+_{s,m}(q,\eta)
:=\mathcal J_{q,\eta}(B^+_{s,m}).
}
\]

For sets `C1 subset C2`, the first hit of the smaller set cannot occur earlier. Therefore the adjacent-slack sandwich gives

\[
\boxed{
J^+_{s+1,m}(q,\eta)
\le
J_{k,K}(q,\eta)
\le
J^+_{s,m}(q,\eta).
}
\]

Consequently every current canonical state has the certified descendant interval

\[
\boxed{
r+2^kJ^+_{s+1,m}(q,\eta)
\le
r_{\min,K}
\le
r+2^kJ^+_{s,m}(q,\eta).
}
\]

The bound now requires only two adjacent slack levels of one universal transfer object.

## 5. Certified dominance pruning

Suppose a complete depth-`K` candidate of start value `R_best` has already been found.

For any current state, if

\[
\boxed{
r+2^kJ^+_{s+1,m}(q,\eta)\ge R_{\rm best},}
\]

then even the optimistic adjacent-slack lower bound cannot beat the incumbent. The entire state can be deleted with no effect on `mu(K)`.

Conversely, `J^+_{s,m}` supplies a certified feasible completion and can lower the incumbent whenever

\[
r+2^kJ^+_{s,m}<R_{\rm best}.
\]

## 6. Relation to the Sturmian factor reduction

The exact kernel belongs to one of at most `m+1` Sturmian factor types for fixed `(m,s)`. The universal adjacent-slack sandwich removes phase dependence when only rigorous bounds are needed:

\[
B^+_{s,m}
\subseteq
B_{\text{any phase},s,m}
\subseteq
B^+_{s+1,m}.
\]

Thus there are two reusable levels:

1. exact: at most `m+1` Sturmian phase kernels;
2. bounded: one universal strong-kernel family evaluated at adjacent slack values `s` and `s+1`.

## 7. Important limitation

The sandwich concerns the coefficient-survival language. The arithmetic placement of that language on the canonical-start cost axis still depends on

\[
\eta
\quad\text{and}\quad
3^q\bmod2^m.
\]

Therefore kernel-size or entropy bounds alone do not imply useful pointwise lower bounds on the first-hit value. The remaining arithmetic problem is to control the earliest affine hit of the larger adjacent-slack kernel.

No equidistribution or randomness assumption is made here.

## 8. Relation to the exact interval certificate

The universal bound can be combined with the exact interval-count certificate.
If an analytic or reusable universal-kernel estimate suggests that all dangerous lifts lie in a short interval, the exact E/O interval recursion can decide whether the corresponding interval in the **actual phase kernel** is empty.

Thus the universal adjacent-slack family is best used as a reusable bound or heuristic guide, while the exact phase-specific interval count remains the final pruning certificate.

## 9. Next target

The proof-oriented target becomes a lower bound on

\[
J^+_{s+1,m}(q,\eta)
\]

for the low-slack forward states capable of competing for `mu(K)`, or a theorem showing that states with simultaneously small forward cost and small adjacent-slack first-hit are sufficiently sparse.

Such a result would immediately become a certified pruning theorem through Section 5 while retaining the exact interval recursion as a final audit layer.
