# m=45 coherent ballot equivalence through depth 301,993

Date: 2026-08-24

Status: **exact finite theorem for the current m=45 layer.**  It is independent of the earlier endpoint-only correction maximum and removes the apparent `H=195,q=123` branch.  It is not a proof of the Collatz conjecture.

## Theorem

Let

\[
N=4\left(3^{45}+b3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i,b\in\{0,1\}.
\]

Then \(N\ge N_{\min}=4\cdot3^{45}+3\) and the first two accelerated Collatz parity symbols are `11`.

For every

\[
1\le H\le301{,}993,
\]

if

\[
T^j(N)\ge N\qquad(1\le j\le H),
\]

then at every prefix

\[
\boxed{3^{q_j}\ge2^j.}
\]

Equivalently, every actual m=45 no-descent candidate through this range belongs to the ordinary coefficient-surviving Beatty-ballot language.

## Proof reduction

Write

\[
2^jT^j(N)=3^{q_j}N+R_j,
\]

and define

\[
b_j=\min\{q:3^q\ge2^j\}.
\]

Assume inductively that no coherent subcritical no-descent prefix exists before depth \(j\).  The unique minimum-odd-count coherent prefix is then the mechanical boundary word with \(q=b_{j-1}\).

At a plateau \(b_j=b_{j-1}\), its minimum child is even and remains on the boundary.  At a rise \(b_j=b_{j-1}+1\), its coefficient-surviving minimum child is odd.

Therefore the only possible **first** coherent subcritical state at a rise is the even child of that unique previous boundary prefix.  If the boundary correction is \(R_{j-1}\), this offshoot has \(q=b_j-1\) and can remain above the start only if

\[
R_{j-1}\ge N\left(2^j-3^{b_j-1}\right).
\]

Because the right side is increasing in \(N\), it is enough to test the smallest current root \(N_{\min}\).

The exact C++ certificate checks the strict reverse inequality

\[
\boxed{
R_{j-1}<N_{\min}\left(2^j-3^{b_j-1}\right)
}
\]

at every Beatty rise through \(j=301{,}993\).  There are exactly

\[
\boxed{190{,}535}
\]

such rise offshoots in the tested range, and all fail.

This completes the finite induction.

## Consequences

1. The apparent terminal `H=195,q=123` exception from an independently maximized correction is not a coherent trajectory state.  The minimum coherent odd count at depth 195 is

\[
\boxed{124=b_{195}}.
\]

2. The current m=45 same-address problem can use the coefficient-surviving language without an additive-headroom correction through depth 301,993.

3. This matches the length range in which Rozier--Terracol exclude paradoxical sequences by a different route, but the present certificate is branch-specific and self-contained: it uses only the m=45 lower root bound and exact Beatty/mechanical correction recurrence.

4. The remaining m=45 obstruction is therefore purely the cross-base intersection

\[
\boxed{
\text{ternary 0/1 selector family}
\cap
\text{dyadic coefficient-surviving residue language}
}
\]

within this enormous certified horizon.

Certificate:

`collatz/src/m45_coherent_ballot_equivalence_depth301993_certificate.cpp`.
