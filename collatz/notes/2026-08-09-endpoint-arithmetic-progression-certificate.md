# Endpoint arithmetic-progression certificate

Date: 2026-08-09

Status: **DERIVED EXACT RECURRENCE + IMPLEMENTATION SIMPLIFICATION + INDEPENDENT CROSS-CHECK**

This note gives an untransformed version of the backward interval-count certificate.  It counts dangerous future lift integers directly through an arithmetic progression of actual prefix endpoints and therefore requires no modular inverse or cyclic-coordinate conversion.

It is exactly equivalent to the transformed interval certificate; it is not a new global Collatz theorem.

## 1. Dangerous lift progression

Fix a coefficient-surviving split state

\[
(k,q;r,y),
\]

with accumulated odd multiplier

\[
P=3^q.
\]

A future canonical lift integer

\[
j\ge0
\]

changes the depth-`k` endpoint by

\[
\boxed{y_j=y+Pj.}
\]

For a threshold certificate, only the finite interval

\[
0\le j<L
\]

is dangerous, where typically

\[
L=\left\lceil\frac{X-r}{2^k}\right\rceil.
\]

Define

\[
\boxed{
C_{k,q,m}(y,L)
}
\]

to be the number of integers `j in {0,...,L-1}` for which the next `m` accelerated parity steps starting from `y+3^q j` keep the total coefficient above the barrier at every future prefix.

Then

\[
\boxed{
C_{k,q,m}(y,L)=0
}
\]

is an exact certificate that none of the dangerous lifts survives.

## 2. Split the lift index by one binary digit

Write

\[
j=c+2t,
\qquad c\in\{0,1\}.
\]

The number of such indices in `[0,L)` is

\[
\boxed{
L_0=\left\lceil\frac L2\right\rceil,
\qquad
L_1=\left\lfloor\frac L2\right\rfloor.
}
\]

For a fixed `c`, put

\[
z_c=y+Pc.
\]

Since `P` is odd, all members

\[
z_c+2Pt
\]

have the same next parity

\[
\boxed{b_c=z_c\bmod2.}
\]

Let

\[
q_c=q+b_c.
\]

If

\[
3^{q_c}<2^{k+1},
\]

then this whole binary subchannel fails the coefficient barrier immediately and contributes zero.

## 3. Child arithmetic progression

If `b_c=0`, then

\[
T(z_c+2Pt)
=\frac{z_c}{2}+Pt.
\]

Thus the child state is

\[
q'=q,
\qquad
\boxed{y'=z_c/2.}
\]

If `b_c=1`, then

\[
T(z_c+2Pt)
=\frac{3z_c+1}{2}+3Pt.
\]

Hence

\[
q'=q+1,
\qquad
\boxed{y'=(3z_c+1)/2.}
\]

In both cases the child family has exactly the same form

\[
\boxed{y'+3^{q'}t.}
\]

Therefore the arithmetic-progression class is closed under the E/O channel split.

## 4. Exact recurrence

For `m=0`, every remaining lift is accepted:

\[
\boxed{C_{k,q,0}(y,L)=L.}
\]

If the current odd count already satisfies the final barrier,

\[
3^q\ge2^{k+m},
\]

then every possible future E/O word is safe and again

\[
\boxed{C_{k,q,m}(y,L)=L.}
\]

Otherwise

\[
\boxed{
C_{k,q,m}(y,L)
=
\sum_{c\in\{0,1\}}
\mathbf 1_{3^{q_c}\ge2^{k+1}}
C_{k+1,q_c,m-1}(y'_c,L_c),
}
\]

with zero-length `L_c` branches omitted.

This is an exact two-channel recursion with no modular inversion.

## 5. Equivalence with the transformed interval count

Let

\[
N=2^m,
\qquad
\xi=[3^{-q}y]_N.
\]

The transformed suffix set satisfies

\[
S_{k,q,m}=3^{-q}A_{k,q,m}\pmod N.
\]

For each lift `j`,

\[
\xi+j\in S_{k,q,m}
\]

iff

\[
y+3^qj\in A_{k,q,m}\pmod N.
\]

Therefore

\[
\boxed{
C_{k,q,m}(y,L)
=N_{k,q,m}(\xi,L),
}
\]

where the right side is the cyclic interval count from `interval-count-certificate.md`.

The new recurrence is thus the same certificate written in the original endpoint/lift coordinates.

## 6. Linear interval complexity

At every recursion level,

\[
L_0+L_1=L.
\]

Forbidden coefficient branches only decrease this total.

Hence the sum of the active progression lengths on any level is at most the initial `L`, so the number of nonempty recursion nodes is at most

\[
\boxed{O(mL)}
\]

ignoring integer bit complexity.

This recovers the same complexity bound as the transformed interval recursion, but uses only:

- parity tests;
- multiplication by `3`;
- halving;
- exact powers-of-3 / powers-of-2 barrier comparisons.

No `PowerMod` operation is necessary.

## 7. Threshold certificate form

For a proposed lower bound `mu(K)>=X`, fix a split `k` and a forward representative `(r,q,y)` with `r<X`. Put

\[
L_X(r)=\left\lceil\frac{X-r}{2^k}\right\rceil.
\]

Then this forward state contributes no target-depth start below `X` iff

\[
\boxed{
C_{k,q,K-k}(y,L_X(r))=0.
}
\]

Thus the full bidirectional threshold certificate can be implemented entirely in the original canonical-state coordinates.

When `2^k>X`, `L_X(r)=1`; the recursion follows only the actual no-lift endpoint orbit. This makes explicit why the long-tail core-reconstruction case is deterministic.

## 8. Matrix / channel interpretation

The lift interval itself is a binary channel tree. Its next binary digit `c` selects one of two arithmetic subprogressions; endpoint parity then determines whether that subprogression passes through the E or O Collatz channel.

The state can be written

\[
\boxed{(k,q,y,L)}.
\]

Each branch sends it to

\[
(k+1,q',y',L_c).
\]

The interval weight `L` is conserved across the two branches before coefficient pruning:

\[
L_0+L_1=L.
\]

This is an exact channel-indexed aggregation of the dangerous lift interval.

## 9. Independent checks

Two separate exact implementations were used.

### Python

Direct enumeration and the recurrence were compared over

- `0<=k<=3`;
- `0<=q<=k+2`;
- `0<=m<=4`;
- `0<=y<=20`;
- `0<=L<=12`.

No discrepancy was found in 24,570 cases.

### Wolfram

After correcting an initial test-harness error in which a conditional `Count` pattern was used incorrectly, a direct `Table`-sum verifier compared the recurrence against explicit endpoint trajectories over

- `0<=k<=3`;
- `0<=q<=k+2`;
- `0<=m<=4`;
- `0<=y<=20`;
- `1<=L<=12`.

All

\[
\boxed{22,680}
\]

cases agreed exactly.

The discarded erroneous harness result is not used as evidence.

## 10. Proof-program consequence

The transformed cyclic-successor formulation remains useful for geometric gap / Fourier arguments.  The present recurrence is preferable as a final exact verifier because it is simpler and keeps the E/O/lift channels in their original arithmetic coordinates.

A future analytic or rectangle method may therefore return a small list of dangerous `(y,L)` blocks, and this recurrence can certify them exactly without rebuilding the full suffix set.