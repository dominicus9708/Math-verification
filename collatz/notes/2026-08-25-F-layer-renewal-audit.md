# Corrected F-layer stopping and renewal audit

Date: 2026-08-25

Status: **exact finite audit + safe structural lemmas**. This note corrects a chat-only diagnostic that incorrectly reported a 127-step plateau. It does not prove an asymptotic bound for the Collatz coefficient stopping time.

## 1. Core and notation

For

\[
F_m=\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

let

\[
\tau_c(N)=\min\{j\ge1:3^{q_j(N)}<2^j\}.
\]

Separate the layer maximum from the cumulative record:

\[
L_F(m):=\max_{N\in F_m}\tau_c(N),
\qquad
M_F(m):=\max_{0\le r\le m}L_F(r).
\]

The older `ansari_F_record_scan.cpp` tracks the cumulative quantity `M_F` because its `best` variable is not reset between layers.

## 2. Correction of the false 127 plateau

A previous chat diagnostic treated a 127-step inspection window as if it were the exact layer maximum. That was wrong.

Independent exact `boost::multiprecision::cpp_int` scans give:

| m | L_F(m) | M_F(m) |
|---:|---:|---:|
| 12 | 154 | 154 |
| 13 | 197 | 197 |
| 14 | 170 | 197 |
| 15 | 251 | 251 |
| 16 | 192 | 251 |
| 17 | 243 | 251 |
| 18 | 195 | 251 |
| 19 | 257 | 257 |
| 20 | 265 | 265 |
| 21 | 265 | 265 |
| 22 | 317 | 317 |
| 23 | 351 | 351 |
| 24 | 386 | 386 |
| 25 | 340 | 386 |
| 26 | 428 | 428 |
| 27 | 386 | 428 |

The values through m=24 were reproduced by the exact layer certificate in one run. The m=25,26,27 values were independently checked by chunked exact `cpp_int` enumeration.

Hence there is no 127 plateau.

## 3. Exact ternary recursion

Write

\[
N=4Y+3,
\qquad
Y=3^m+\sum_{i=0}^{m-1}a_i3^i.
\]

Appending the next least-significant ternary selector digit gives

\[
Y' = 3Y+b,
\qquad b\in\{0,1\},
\]

and therefore

\[
\boxed{\Phi_b(N)=3N-6+4b.}
\]

Thus

\[
\Phi_0(N)=3N-6,
\qquad
\Phi_1(N)=3N-2.
\]

If a selector mask stores `(a_0,a_1,...)` in increasing bit order, the correct tree relation is

\[
\boxed{\text{child mask}=2\,\text{parent mask}+b.}
\]

A temporary diagnostic that attached the new bit at the high end was therefore discarded.

## 4. Root-normalized child maps

Every core integer is `3 mod 4`, so the first two accelerated Collatz steps are both odd and

\[
T^2(N)=\frac{9N+5}{4}.
\]

The two ternary children satisfy

\[
\boxed{T^2(\Phi_0(N))=3T^2(N)-16,}
\]

\[
\boxed{T^2(\Phi_1(N))=3T^2(N)-7.}
\]

Therefore the two post-root sibling states differ by exactly

\[
\boxed{9.}
\]

This is the natural two-channel renewal coordinate for the next audit.

## 5. Record renewal: long children need not have long parents

The exact layer-record holders show that coefficient stopping time is not monotone down the ternary tree.

Selected exact records:

| child layer m | L_F(m) | immediate parent tau_c | sibling tau_c |
|---:|---:|---:|---:|
| 12 | 154 | 5 | 4 |
| 13 | 197 | 13 | 5 |
| 15 | 251 | 12 | 5 |
| 19 | 257 | 5 | 16 |
| 22 | 317 | 5 | 4 |
| 23 | 351 | 10 | 5 |
| 24 | 386 | 5 | 4 |
| 25 | 340 | 10 | 5 |
| 26 | 428 | 4 | 4 |
| 27 | 386 | 5 | 4 |

From m=8 onward the layer maximum is not inherited from a previous-layer maximum. In the tested high layers it is repeatedly regenerated from a shallow-stopping parent.

This kills the naive induction

\[
\tau_c(N)\text{ small}\Rightarrow\tau_c(\Phi_b(N))\text{ small}.
\]

The correct object must keep the cross-base residue state, not only the scalar stopping time.

## 6. Long-tail parent audit

At m=24, exact counts are:

| threshold J | # {N in F_24 : tau_c(N)>=J} | max parent tau_c | parent <=5 | parent <=13 |
|---:|---:|---:|---:|---:|
| 50 | 236955 | 203 | 156351 | 212775 |
| 100 | 17626 | 170 | 11875 | 15942 |
| 150 | 1745 | 89 | 1170 | 1581 |
| 200 | 237 | 88 | 144 | 215 |
| 250 | 25 | 16 | 19 | 24 |
| 300 | 3 | 5 | 3 | 3 |

Thus the extreme tail becomes strongly concentrated over shallow parent states in this finite range, but this is evidence, not a theorem.

## 7. Sibling renewal is not bounded by a small constant

For each parent define

\[
J_{\rm sib}(N)=
\min\{\tau_c(\Phi_0(N)),\tau_c(\Phi_1(N))\}.
\]

The maximum simultaneous sibling survival also grows in the finite scan. At parent layer 23, a parent with `tau_c=5` has children with stopping times

\[
140,\ 127,
\]

so

\[
J_{\rm sib}=127.
\]

Hence a fixed small sibling bound is false as a proof strategy.

## 8. Safe dyadic-state lemma

For fixed j, whether

\[
\tau_c(N)>j
\]

holds is determined entirely by

\[
N\pmod{2^j},
\]

because the first j parity symbols are determined by that residue.

For either branch

\[
\Phi_b(N)=3N-6+4b,
\]

the multiplier 3 is invertible modulo every power of two. Therefore

\[
\boxed{\Phi_b:\mathbb Z/2^j\mathbb Z\to\mathbb Z/2^j\mathbb Z}
\]

is an affine permutation.

This explains structurally why a shallow parent can be sent into a deep coefficient-survivor residue: scalar parent stopping time discards the dyadic phase that the affine permutation preserves.

## 9. DSD interpretation

The corrected logic chain is

1. `F_m` selector digit = ternary descriptive channel;
2. `tau_c` survival prefix = dyadic descriptive channel;
3. ternary extension acts by the affine maps `Phi_0,Phi_1`;
4. these maps are permutations on every finite dyadic state space;
5. therefore scalar stopping time is not a closed state variable;
6. the proof object must be a cross-base transition operator on residue / survivor states;
7. closure requires a contraction of the dangerous-state mass, not inheritance of the parent stopping time.

This aligns with the earlier cross-place and Fourier-complementarity results: the missing theorem is a cross-base transition contraction.

## 10. Next target

Define the dangerous residue set

\[
D_j=\{r\bmod2^j:\tau_c(r)>j\}.
\]

For a ternary parent cylinder, the two child channels enter

\[
\Phi_0^{-1}(D_j),
\qquad
\Phi_1^{-1}(D_j).
\]

The next useful theorem would be a bounded-block statement of the form

\[
\mu_{m+r}(D_{j+s})
\le \rho\,\mu_m(D_j),
\qquad \rho<1,
\]

for an appropriate cross-base state measure and fixed block lengths r,s.

A one-step monotone stopping-time induction is now explicitly ruled out by the exact renewal data.
