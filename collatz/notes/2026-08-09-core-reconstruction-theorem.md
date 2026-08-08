# Finite-crossing core reconstruction theorem

Date: 2026-08-09

Status: derived reduction for a fixed first-coefficient-crossing order. This is not a global proof of CST or Collatz.

## Setup

For the accelerated Collatz map, let a hypothetical first coefficient crossing have length `sigma` and `q` odd entries:

\[
\sigma=\lceil q\log_2 3\rceil,
\qquad
D=2^\sigma-3^q>0.
\]

For a parity word with odd positions `d_i`,
\[
T^\sigma(x)=\frac{3^q x+R}{2^\sigma},
\qquad
R=\sum_i2^{d_i}3^{q-1-i}.
\]

Let
\[
\delta=\frac{D}{3^q}=\frac{2^\sigma}{3^q}-1.
\]
The mechanical-boundary pair estimate gives
\[
S=R/3^q\le S^*(q)\le(7q+1)/24.
\]
A paradoxical first crossing satisfies `T^sigma(x)>=x`, hence
\[
\boxed{x\le U(q):=\frac{7q+1}{24\delta}}.
\]

Choose an integer `B` such that
\[
\boxed{2^B>U(q)}.
\]

## Core reconstruction

Split the correction into odd steps occurring before and after parity time B:
\[
R=R_{<B}+R_{\ge B}.
\]
Every term in `R_{>=B}` contains a factor `2^{d_i}` with `d_i>=B`, hence
\[
R_{\ge B}\equiv0\pmod{2^B}.
\]
The canonical integrality condition is
\[
3^q x+R\equiv0\pmod{2^\sigma}.
\]
Reducing modulo `2^B` gives
\[
\boxed{
3^q x+R_{<B}\equiv0\pmod{2^B}.
}
\]
Since `3^q` is odd,
\[
\boxed{
x\equiv-3^{-q}R_{<B}\pmod{2^B}.
}
\]
But a paradoxical candidate satisfies `0<x<2^B`. Therefore its low-B-bit residue is the integer itself:
\[
\boxed{
x=\left\langle-3^{-q}R_{<B}\right\rangle_{2^B}.
}
\]
If the residue is zero, there is no positive candidate under the strict bound `x<2^B`.

Equivalently, by the parity-vector bijection, each admissible length-B parity prefix determines at most one hypothetical paradoxical start x, and all later parity bits are dependent output of that x.

This directly removes the safe-tail degrees of freedom. The previous STGE/DCER minimization problem is stronger than necessary for candidate reconstruction.

## Size of B

Rozier--Terracol quote Rhin's effective lower bound
\[
\sigma\log2-q\log3\ge\sigma^{-13.3}.
\]
Thus
\[
\delta=e^{\sigma\log2-q\log3}-1\ge\sigma^{-13.3}.
\]
Since q<sigma,
\[
U(q)<\frac{7\sigma+1}{24}\sigma^{13.3}=O(\sigma^{14.3}).
\]
Hence
\[
\boxed{B=O(\log\sigma)}.
\]
For example one may take
\[
B\le14.3\log_2\sigma+O(1).
\]

## Number of binary parity cores

Let
\[
\alpha=\log_3 2=\frac{\log2}{\log3}=0.6309297535\ldots
\]
A pre-crossing length-B parity prefix must satisfy in particular
\[
q_B\ge\alpha B.
\]
Therefore the number of possible prefixes is bounded by a binomial upper tail, giving
\[
N_B\le(B+1)2^{H_2(\alpha)B},
\]
where
\[
H_2(\alpha)=0.9499555271883306\ldots
\]
Thus the crude fixed-resonance candidate count is polynomial in the numeric length sigma:
\[
\boxed{N_B\le\sigma^{13.58436404+o(1)}}.
\]
This is a state-count statement in sigma, not a polynomial-time statement in the bit-length of q.

## Stronger candidate count after recursive sufficiency

Ansari's recursively sufficient intersection restricts a minimal counterexample to
\[
x=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]
The number of such integers below X is `O(X^{log_3 2})`. With `X=U(q)=O(sigma^{14.3})`,
\[
\boxed{
N_{F,\sigma}=O(\sigma^{14.3\log_3 2})
=O(\sigma^{9.022295476\ldots}).
}
\]
Thus for each fixed resonance, the nominally exponential parity-word problem reduces to a finite set with polynomial cardinality in sigma.

## What this does and does not solve

This reduction gives an explicit finite algorithm for a fixed q/sigma:

1. generate admissible B-bit parity cores, or equivalently enumerate the recursively sufficient Cantor-core candidates below U(q);
2. reconstruct candidate x exactly;
3. test whether its actual coefficient stopping equals the prescribed sigma and whether actual descent fails.

It does not provide a uniform theorem over all q. The remaining global issue is to rule out an infinite sequence of increasingly large resonances/candidates without checking each q separately.
