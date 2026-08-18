# Exact closure of the late first-defect channels in the two m=45 affine blocks

Date: 2026-08-18

Status: **exact finite first-descent certificates / channel reduction**. This is not a proof of the Collatz conjecture.

## 1. Two remaining m=45 affine blocks

After the separate defect-density exclusion of the m=46 layer, the m=45 recursively-sufficient candidates split into the two 44-selector affine blocks

\[
N=4\left(C+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

with

\[
C=3^{45}
\quad\text{or}\quad
C=3^{45}+3^{44}.
\]

The first 24 bits of the coefficient-surviving mechanical word have canonical residue

\[
N_{\rm mech}\equiv12,475,387\pmod{2^{24}}.
\]

A first mismatch at a mechanical 1 is a `1->0` move and immediately violates coefficient survival. Hence a surviving first defect in the first 24 bits can occur only at the mechanical zero positions

\[
p\in\{2,5,8,10,13,16,18,21\}.
\]

## 2. Exact meet-in-the-middle trajectory audits

The 44 ternary selectors were split as 22 low + 22 high selectors. For each prescribed low-bit first-defect cylinder, the low half was bucketed by the required dyadic residue and matched exactly with all high-half selector sums. Every resulting ordinary integer was then iterated with the accelerated Collatz map until it fell below its own start. All arithmetic was exact unsigned 128-bit integer arithmetic; all runs reported zero overflow events.

### No defect through bit 24

For `C=3^45`:

\[
4,194,014\text{ candidates},\qquad
0\text{ failures},\qquad
\max\tau_< =287.
\]

For `C=3^45+3^44`:

\[
4,191,639\text{ candidates},\qquad
0\text{ failures},\qquad
\max\tau_< =357.
\]

Thus every unresolved m=45 candidate has a first defect inside the first 24 bits.

### First defect p=21

\[
\begin{array}{c|r|r}
C&\text{candidates}&\max\tau_<\\\hline
3^{45}&16,781,123&324\\
3^{45}+3^{44}&16,780,710&381
\end{array}
\]

All candidates descend; failures = 0.

### First defect p=18

\[
\begin{array}{c|r|r}
C&\text{candidates}&\max\tau_<\\\hline
3^{45}&134,218,448&398\\
3^{45}+3^{44}&134,221,217&436
\end{array}
\]

All candidates descend; failures = 0.

### First defect p=16

\[
\begin{array}{c|r|r}
C&\text{candidates}&\max\tau_<\\\hline
3^{45}&536,871,936&495\\
3^{45}+3^{44}&536,880,377&522
\end{array}
\]

All candidates descend; failures = 0.

## 3. Hybrid p=13 closure

Direct p=13 raw sizes are about `2^32` per affine block, so the exact depth-27 Hensel retained-residue certificate was inserted before trajectory following. The existing builder generates exactly

\[
1,061,510
\]

retained canonical residues modulo `2^27`.

The p=13 address set was partitioned into eight disjoint high-selector shards per affine block. Exact totals were:

For `C=3^45`:

\[
\boxed{
4,294,972,331\ \text{raw}
\to616,031,639\ \text{depth-27 hard}
\to0\ \text{failures}
}
\]

with

\[
\max\tau_< =489.
\]

For `C=3^45+3^44`:

\[
\boxed{
4,294,962,588\ \text{raw}
\to616,059,244\ \text{depth-27 hard}
\to0\ \text{failures}
}
\]

with

\[
\max\tau_< =546.
\]

The reproducible shard certificate is

`collatz/src/m45_p13_depth27_hybrid_chunk_certificate.cpp`.

It consumes the locally generated `allow27.bin` from

`collatz/src/depth27_hensel_retained_residue_builder.cpp`.

## 4. New m=45 boundary

The no-defect channel and the four latest admissible first-defect positions

\[
p=21,18,16,13
\]

are all eliminated in both m=45 affine blocks.

Therefore every still-unresolved m=45 candidate must have

\[
\boxed{p\in\{2,5,8,10\}}.
\]

This is now strictly narrower than the previously recorded m=44 six-channel frontier

\[
p\in\{2,5,8,10,13,16\}.
\]

## 5. Next closure target

The next raw channel is `p=10`, with roughly `3.436e10` representatives per m=45 affine block. Direct trajectory enumeration is no longer the preferred proof object. The next certificate should combine the first-defect cylinder with the depth-28 q-sliced Hensel hard core and, if needed, a reverse/formation filter before ordinary trajectory following.
