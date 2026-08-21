# Bounded-record singleton classification

Date: 2026-08-22

Status: **exact combinatorial reduction for bounded record excursions.** This does not prove the Collatz conjecture. It proves that an infinite record tail cannot consist only of singleton first-passage macros, and that every bounded-record tail must contain infinitely many genuinely branching record macros.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil,
\]

and let

\[
d_j=b_{s+j}-b_{s+j-1}\in\{0,1\}
\]

be the mechanical Beatty word on a candidate record interval of length \(L\).

Write

\[
D_j=d_1+\cdots+d_j=b_{s+j}-b_s.
\]

A record first-passage parity word \(\varepsilon_1\cdots\varepsilon_L\) satisfies

\[
q_j:=\varepsilon_1+\cdots+\varepsilon_j\le D_j
\qquad(1\le j<L),
\]

and

\[
q_L=D_L+1.
\]

Because the final first-passage step must cross the upper boundary, necessarily

\[
d_L=0,
\qquad
\varepsilon_L=1,
\qquad
q_{L-1}=D_{L-1}.
\]

Thus the number of record words is exactly the number of binary paths of length \(L-1\) that stay below the mechanical prefix \(d_1\cdots d_{L-1}\) and finish at the same endpoint.

## 1. Exact singleton criterion

### Theorem 1

The record language has exactly one word if and only if

\[
\boxed{
 d_1\cdots d_{L-1}\text{ contains no occurrence of }10.
}
\]

### Proof

If the mechanical prefix contains \(10\) at positions \(i,i+1\), replace that local pair by \(01\), leaving every other bit unchanged. At position \(i\) the alternate path is one below the mechanical boundary; at position \(i+1\) it returns to the same cumulative count, and thereafter it coincides with the boundary. Therefore it is a second valid endpoint-matched prefix. Hence the language is not singleton.

Conversely, if the prefix contains no \(10\), then because it is binary it has the form

\[
0^a1^b.
\]

The first \(a\) cumulative boundary values are zero, so every valid path is forced to use zero in these positions. It must then accumulate exactly \(b\) ones in the remaining \(b\) positions, forcing all of them to be one. Hence the only endpoint-matched path is the boundary word itself. \(\square\)

## 2. Mechanical word forbids 00 and 111

The one-slack ceiling identity gives, for every phase \(s\),

\[
b_{s+2}-b_s\ge1
\]

because

\[
2\alpha>1
\quad\Longleftrightarrow\quad
2^2>3,
\]

so the mechanical word contains no \(00\).

Likewise

\[
b_{s+3}-b_s\le2
\]

because

\[
3\alpha<2
\quad\Longleftrightarrow\quad
2^3<3^2,
\]

so it contains no \(111\).

If a singleton prefix has the form \(0^a1^b\), the absence of \(00\) gives

\[
a\le1,
\]

and the absence of \(111\) gives

\[
b\le2.
\]

Therefore

\[
L-1=a+b\le3.
\]

Hence:

\[
\boxed{
\text{every singleton record macro has }L\le4.
}
\]

Equivalently, every record excursion of length

\[
\boxed{L\ge5}
\]

has at least two admissible parity words.

## 3. Shape of every singleton macro

A singleton mechanical block is necessarily one of the following shapes:

\[
0,
\qquad
1^b0,
\qquad
01^b0,
\qquad b\in\{1,2\},
\]

with the obvious length restrictions.

The corresponding parity word is obtained by keeping the first \(L-1\) mechanical bits and replacing the final mechanical zero by one.

Thus:

- if the block begins inside a mechanical one-run, its parity word is all ones;
- if it begins at a mechanical zero, it may preserve that initial zero, but after the final zero is flipped the next record begins immediately after a mechanical zero.

Since \(00\) never occurs, the next mechanical bit is one. Therefore every subsequent singleton block begins inside a one-run and has parity word consisting entirely of ones.

Consequently:

\[
\boxed{
\text{after at most one singleton record macro, an all-singleton tail has parity }1111\ldots
}
\]

## 4. Infinite all-odd tail is impossible for a positive integer

If \(x>0\) has its next \(k\) accelerated Collatz parities all odd, then iterating

\[
T(x)=\frac{3x+1}{2}
\]

gives

\[
T^k(x)
=
\left(\frac32\right)^k(x+1)-1
=
\frac{3^k(x+1)-2^k}{2^k}.
\]

Integrality forces

\[
2^k\mid x+1.
\]

If the parity tail were odd forever, this would hold for every \(k\), so the finite positive integer \(x+1\) would be divisible by arbitrarily large powers of two. Equivalently, the only 2-adic state with parity \(1111\ldots\) is \(-1\), not a positive ordinary integer.

Therefore:

\[
\boxed{
\text{an infinite record tail cannot be eventually singleton.}
}
\]

In particular, if the record lengths are bounded, then non-singleton record macros must occur infinitely often.

## 5. Quantitative bound on long singleton runs

For an infinite nonperiodic coefficient-surviving orbit, the Garcia--Tal orbit-sparsity estimate yields reciprocal summability and hence convergence of the correction product

\[
\Pi_k
=
\prod_{\substack{j<k\\x_j\text{ odd}}}
\left(1+\frac1{3x_j}\right)
\uparrow\Pi_\infty<\infty.
\]

At record time \(s=\tau_r\), where

\[
h_s=m_s-b_s=r,
\]

the exact product identity gives

\[
x_s
=N\,3^r\frac{3^{b_s}}{2^s}\Pi_s.
\]

Since

\[
1\le\frac{3^{b_s}}{2^s}<3,
\]

we obtain the orbit-dependent bound

\[
\boxed{
x_{\tau_r}<C_N3^r,
\qquad C_N:=3N\Pi_\infty.
}
\]

If a run of singleton records produces \(k\) consecutive odd parity bits after that record time, then

\[
2^k\mid x_{\tau_r}+1,
\]

so

\[
2^k\le x_{\tau_r}+1<C_N3^r+1.
\]

Hence

\[
\boxed{
k\le\log_2(C_N3^r+1)
=r\log_2 3+O_N(1).}
\]

Thus even though singleton records may occur in long runs, a run beginning at record height \(r\) has length only \(O_N(r)\).

It follows that in any bounded-record tail the record indices \(r_1<r_2<\cdots\) at which non-singleton macros occur satisfy

\[
r_{j+1}\le A_Nr_j+B_N
\]

for orbit-dependent constants. Consequently the number of non-singleton records up to height \(R\) is at least logarithmic in \(R\):

\[
\boxed{
\#\{j:r_j\le R\}=\Omega_N(\log R).
}
\]

This is only a sparsity lower bound; it does not by itself close the Hensel/selector splice.

## 6. Revised bounded-record target

The bounded-record regime is now reduced to:

1. singleton record macros are completely classified and cannot form an infinite tail;
2. every bounded-record tail contains infinitely many non-singleton macros;
3. gaps between non-singleton macros are at most linear in the current record height;
4. every non-singleton macro is a genuinely branching finite dyadic residue family.

The remaining bounded-record theorem is therefore not an arbitrary finite-length problem. It is:

> **Repeated non-singleton Hensel/Haar splice.** Use the fresh dyadic branching supplied by infinitely many non-singleton record macros, together with the selector Haar energy/cross-base machinery, to rule out an ordinary positive integer tail.

Companion finite regression:

`collatz/src/record_singleton_macro_classification_certificate.py`.
