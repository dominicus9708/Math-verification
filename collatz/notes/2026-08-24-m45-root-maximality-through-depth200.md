# m=45 whole-prefix root maximality is unconditional through depth 200

Date: 2026-08-24

Status: **exact finite range theorem.**  This removes the need for an asymptotic nearest-credit theorem over the entire binary range relevant to the current m=45 core up through depth 200.  This is not a proof of the Collatz conjecture.

## 1. Exact numeric range of the current m=45 roots

The current recursively sufficient m=45 family consists of two affine blocks:

\[
N=4\left(3^{45}+b3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad b\in\{0,1\},\quad a_i\in\{0,1\}.
\]

Hence

\[
N_{\min}=4\cdot3^{45}+3,
\]

and the maximum over **both** affine blocks is

\[
N_{\max}
=4\left(3^{45}+3^{44}+\frac{3^{44}-1}{2}\right)+3.
\]

Exact integer comparison gives

\[
\boxed{2^{73}<N_{\min}\le N\le N_{\max}<2^{74}.}
\]

Thus every current m=45 root in either affine block is a 74-bit positive integer and, crucially, is larger than \(2^{73}\).

## 2. Universal same-q whole-prefix credit bound

Take any length-H parity word with q odd events at positions

\[
0\le k_1<\cdots<k_q\le H-1.
\]

Its affine correction is

\[
R=\sum_{j=1}^q3^{q-j}2^{k_j}.
\]

Among all q-odd length-H words, the maximum correction is obtained by placing all q odd events in the final q positions:

\[
\begin{aligned}
R_{\max}(H,q)
&=\sum_{j=1}^q3^{q-j}2^{H-q+j-1}\\
&=2^{H-q}(3^q-2^q).
\end{aligned}
\]

Therefore if two complete q-odd words are in the same Hensel class and

\[
R'-R=3^q d,
\qquad d>0,
\]

then automatically

\[
\boxed{
0<d<\frac{R_{\max}(H,q)}{3^q}
=2^{H-q}\left(1-\left(\frac23\right)^q\right)
<2^{H-q}.
}
\]

This bound does not use the empirical nearest-credit values \(G_H\).  It applies to every possible positive complete-prefix sibling credit.

## 3. Insert coefficient survival

Coefficient survival through depth H requires

\[
3^q\ge2^H,
\]

so

\[
q\ge q_{\min}(H):=\min\{q:3^q\ge2^H\}
=\lceil H\log_3 2\rceil.
\]

Hence every positive complete-prefix sibling credit satisfies

\[
\boxed{d<2^{H-q}\le2^{H-q_{\min}(H)}.}
\]

For every H through 200, exact integer calculation gives

\[
H-q_{\min}(H)\le73.
\]

At the endpoint,

\[
q_{\min}(200)=127,
\qquad
200-127=73.
\]

Therefore for every coefficient-surviving current m=45 prefix from either affine block with

\[
H\le200,
\]

we have

\[
\boxed{d<2^{73}<N.}
\]

The smaller root

\[
M=N-d>0
\]

is therefore always strictly below the hypothetical minimal counterexample N and reaches exactly the same H-step endpoint.

Thus a minimal counterexample in the current m=45 core must be the maximum-correction representative of its complete same-(q,R mod 3^q) class at **every depth H<=200**.

## 4. Sharp endpoint of this crude uniform argument

At H=201,

\[
q_{\min}(201)=127,
\qquad
201-127=74.
\]

The universal estimate only gives

\[
d<2^{74},
\]

which is no longer uniformly below every current m=45 root because

\[
N_{\min}<2^{74}.
\]

Therefore

\[
\boxed{H=200}
\]

is the last horizon covered by this simple root-size argument without using any sharper nearest-credit or class-specific information.

Certificate:

`collatz/src/m45_root_maximality_horizon200_certificate.py`.

## 5. Strategic consequence

The previously introduced nearest-credit quantity

\[
G_H
\]

remains useful for asymptotic understanding, but it is **not needed to justify whole-prefix root maximality anywhere up to depth 200 in either current m=45 affine block**.

This matters because every m=45 selector integer is already completely resolved by its binary address at depth 74.  Thus:

1. through depth 74, whole-prefix maximality is automatically root-valid;
2. the same root-validity actually continues much farther, through depth 200;
3. any proof obstruction before depth 200 cannot be blamed on insufficient root-credit control;
4. the remaining difficulty is therefore structural counting / same-address correlation of the maximal coefficient-surviving language, not the existence of a smaller root predecessor once a larger complete-prefix correction is found.

The next finite target should exploit this depth-200 safe range directly, rather than first proving an all-H theorem for \(G_H\).
