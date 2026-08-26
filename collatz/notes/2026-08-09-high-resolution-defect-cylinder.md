# High-resolution defect cylinder formulation

Date: 2026-08-09

Status: **DERIVED EXACT COLLAPSE + CYLINDER INTERSECTION FORMULATION + INDEPENDENT SMALL CHECK**

This note sharpens `defect-carry-block-duality.md`. The two defect coordinates `(U,V)` are not independent: they are the low/high bit blocks of one higher-resolution 2-adic defect residue.

No global Collatz theorem is claimed.

## 1. Setup

Fix a coefficient-surviving prefix cell of depth `h` and odd-count `q`. Put

\[
M=2^h,\qquad P=3^q.
\]

Let `R*`, `r*`, `y*` be the prefix-constrained maximal-correction word and its canonical start/endpoint. For another word in the cell let

\[
C=R^*-R\ge0.
\]

Fix a later target depth

\[
K=h+m,
\]

and write

\[
N=2^m,\qquad Q=2^K=MN.
\]

## 2. One high-resolution defect residue

Define

\[
\boxed{A=[P^{-1}C]_Q,\qquad 0\le A<Q.}
\]

Split its binary digits at the prefix depth:

\[
\boxed{A=U+MW,}
\]

with

\[
0\le U<M,\qquad 0\le W<N.
\]

Reduction modulo `M` immediately gives

\[
\boxed{U=[P^{-1}C]_M.}
\]

Thus `U` is exactly the forward wrap coordinate from `defect-carry-block-duality.md`.

Let

\[
T_c=\frac{PU-C}{M}.
\]

Since

\[
PA-C=P(U+MW)-C=M(T_c+PW)
\]

is divisible by `MN`, we have

\[
T_c+PW\equiv0\pmod N.
\]

Multiplying by `P^{-1}` modulo `N` yields

\[
\boxed{[P^{-1}T_c]_N=-W\pmod N.}
\]

Therefore the earlier second coordinate

\[
V=[P^{-1}T_c]_N
\]

is simply

\[
\boxed{V=-W\pmod N.}
\]

The apparent two-dimensional carry state is exactly a binary block decomposition of one residue `A mod 2^K`.

## 3. Pure additive channel formula at target resolution

Using the exact defect channels

\[
C_i=3^{q-1-i}\left(2^{d_i^*}-2^{d_i}\right),
\]

we have

\[
C=\sum_i C_i.
\]

Because `P=3^q`, multiplication by `P^{-1}` gives directly

\[
\boxed{
A
\equiv
\sum_{i=0}^{q-1}
3^{-(i+1)}
\left(2^{d_i^*}-2^{d_i}\right)
\pmod{2^K}.
}
\]

Thus at full target resolution the defect transfer is again a purely additive group-algebra transfer; no auxiliary carry coordinate is required during the symbolic calculation. Carry appears only when `A` is split into low and high binary blocks.

This is the cleanest channel/matrix representation of the forward/backward coupling found so far.

## 4. Start and endpoint query from the bit blocks

Let

\[
\boxed{w=\left\lfloor\frac{r^*+U}{M}\right\rfloor\in\{0,1\}.}
\]

Then

\[
\boxed{r=r^*+U-wM.}
\]

Let

\[
\xi=[P^{-1}y]_N,
\qquad
\xi^*=[P^{-1}y^*]_N.
\]

From `V=-W` and the defect-carry identity,

\[
\boxed{\xi=[\xi^*-W-w]_N.}
\]

Hence:

- the low `h` bits `U` determine whether the canonical start is small;
- the high `m` bits `W` determine the translated future endpoint query;
- the single extra bit `w` records the low-block wrap against `r*`.

## 5. Exact bit-cylinder criterion below a threshold

Let

\[
1\le X\le M.
\]

As before,

\[
\boxed{r<X\iff U\in I_M(-r^*,X).}
\]

Let

\[
S_{h,q,m}\subset\mathbb Z/N\mathbb Z
\]

be the transformed future coefficient-surviving suffix set. Since a target-depth descendant is

\[
n=r+MJ,
\]

and `X<=M`, a descendant below `X` must have `J=0`. Thus it must satisfy

\[
\xi\in S_{h,q,m}.
\]

Using the high block,

\[
\xi^*-W-w\in S_{h,q,m}.
\]

For a fixed wrap value `w_0`, define

\[
\boxed{
H_{w_0}
=\{[\xi^*-w_0-s]_N:s\in S_{h,q,m}\}.
}
\]

Then the exact condition for a target-depth survivor below `X` in this cell is

\[
\boxed{
A=U+MW
\text{ lies in }
\bigcup_{w_0\in\{0,1\}}
\left(I_{w_0}+M H_{w_0}\right),
}
\]

where `I_{w_0}` is the portion of the forward small-start interval on which the wrap bit equals `w_0`.

The forward interval splits into at most two such pieces.

Therefore the anti-alignment problem is an exact **low-bit / high-bit cylinder intersection** in one cyclic group `Z/2^K Z`.

## 6. Why this is stronger than fixed-modulus pruning

The fixed-low-bit saturation theorem shows that looking only at `U mod 2^h` eventually loses all additional target-depth information.

The present formulation shows precisely where that missing information lives: it is the high block `W` of the same defect residue `A`.

Thus increasing target depth does not require inventing a new state variable. It requires keeping more binary digits of the same additive defect coordinate.

This gives a direct structural explanation of why:

- fixed low-modulus sieves saturate;
- the finite-horizon carry quotient needs `m` future bits;
- late-lift forcing is intrinsically a growing-resolution statement.

## 7. Transfer / semiring consequence

The sparse defect matrices from `slack-defect-channel-transfer.md` may now be evaluated directly in

\[
\mathbb Z[\mathbb Z/2^K\mathbb Z]
\]

using the target-resolution channel weight

\[
\boxed{
X^{\,3^{-(i+1)}(2^{d_i^*}-2^{d_i})}.
}
\]

The resulting support is the exact high-resolution defect set

\[
\mathcal A_{h,q,K}\subset\mathbb Z/2^K\mathbb Z.
\]

The proof question becomes whether this support intersects the target bit-cylinder above.

Possible evaluations of the same matrix product include:

- exact Boolean cylinder support;
- interval/cylinder branch-and-bound;
- Fourier characters modulo `2^K`;
- min-plus search after splitting into low/high blocks.

Unlike a low-rank approximation, any final exclusion can be certified by exact support or interval-count checks.

## 8. Independent finite check

Wolfram exact-integer enumeration checked every coefficient-admissible fixed cell with

\[
1\le h\le7,
\qquad
1\le m\le4.
\]

Across 56 `(h,q,m)` cases it verified

\[
A=U+MW,
\qquad
V=-W\pmod{2^m},
\]

and

\[
r=r^*+U-w2^h,
\qquad
\xi=\xi^*-W-w\pmod{2^m}.
\]

The check used arbitrary-precision integer and modular arithmetic only.

## 9. Next theorem target

The useful uniform target is now:

**High-resolution cylinder exclusion.** For a growing split `h=B(K)=O(log K)`, bound or exclude intersections between the defect-transfer support `A_{h,q,K}` and the short low-bit / admissible-high-bit cylinders associated with starts below the desired threshold.

A theorem that gives a polynomial-size exact cylinder cover, or a certified block exclusion for all but a controlled family of cylinders, would directly advance the minimal-survivor growth target without losing the E/O, slack, or carry structure.