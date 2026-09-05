# First resonance: endpoint boundary limits initial mechanical alignment to 44 trits

Date: 2026-08-26

Status: **exact finite theorem** inside the repaired first-global-resonance branch.  This is not a proof of the Collatz conjecture.

## 1. Endpoint band

For the repaired first resonance

\[
(A,Q)=(114208327604,72057431991),
\]
we already have

\[
2^{71}<N<\frac43 2^{71},
\qquad
0<g<2^{33},
\qquad
4\mid g,
\]
and

\[
y=N+g\equiv3\pmod4.
\]

Hence every endpoint lies in the exact integer interval

\[
\boxed{
2^{71}<y<\frac{4\cdot2^{71}+3\cdot2^{33}}3.
}
\]

## 2. Mechanical zero-control endpoint class

Let

\[
b_j=\left\lfloor\frac{(j-1)A}{Q}\right\rfloor
\]
be the exact mechanical odd positions throughout the first-resonance Farey cell.

If the last `m` odd ordinals are all mechanical, i.e. the first `m` terminal Hensel controls have displacement zero, then modulo `3^m` the endpoint is forced to

\[
\boxed{
Y_m^{\rm mech}
:=2^{-A}
\sum_{\ell=0}^{m-1}3^\ell2^{b_{Q-\ell}}
\pmod{3^m}.
}
\]

Therefore an ordinary endpoint with initial mechanical-alignment depth at least `m` must simultaneously satisfy

\[
y\equiv Y_m^{\rm mech}\pmod{3^m},
\qquad
y\equiv3\pmod4.
\]

Since `3^m` is odd, CRT gives one residue class modulo `4*3^m`.

## 3. Exact m=44 and m=45 calculation

At `m=44`, the CRT class has exactly one representative in the admissible endpoint band:

\[
\boxed{
y_{44}=2729562462203742221059.
}
\]

At `m=45`, the corresponding CRT class has **no** representative in the admissible endpoint band.

Thus

\[
\boxed{
\text{no first-resonance endpoint can support 45 initial mechanical zero-displacement Hensel lifts.}
}
\]

Equivalently, for the mechanical-alignment depth introduced in

`2026-08-26-hensel-mechanical-alignment-credit.md`, every first-resonance candidate satisfies

\[
\boxed{\mathfrak a_0\le44.}
\]

A positive Hensel repair displacement must therefore occur within the first

\[
\boxed{45}
\]
terminal odd ordinals.

## 4. Why failure at 45 settles every deeper pure mechanical prefix

Any zero-control alignment of length `m>45` reduces modulo `3^45` to a zero-control alignment of length 45.  Hence the empty `m=45` endpoint class immediately implies emptiness at every deeper pure-mechanical initial tail.

This is stronger conceptually than checking the exact all-mechanical word at `m=46`: it gives the **maximum stored initial alignment credit** permitted by the endpoint boundary.

## 5. Relation to the low-support ladder

The earlier terminal low-support certificates prove stronger statements about the **number** of displaced ordinals in windows such as 50, 52, 56, 58, 65, and 66.  The present result measures something different:

\[
\boxed{
\text{endpoint boundary}\Rightarrow\text{at most 44 consecutive zero-cost alignment trits before the first repair}.
}
\]

This is the correct initial condition for an amortized repair argument.

The two pieces should not be conflated:

- support lower bounds count how many displaced odd ordinals occur;
- alignment credit measures how long the Hensel carry can follow the mechanical ray with `d=0` before a repair is forced.

## 6. DSD audit interpretation

The endpoint boundary is now used as an actual state constraint rather than being discarded when entering a local Hensel block.

The chain is

\[
\boxed{
\text{ordinary endpoint band}
\to
\text{CRT terminal carry class}
\to
\mathfrak a_0\le44
\to
\text{repair forced by step 45}.
}
\]

This is exactly the kind of boundary-preserving implication required by the DSD audit.  No local block is given an arbitrary free incoming carry.

## 7. Next target

The remaining task is to control **replenishment** of alignment after the first forced repair.

The repair-bijection theorem says that buying `L` new mechanical alignment digits requires one exact displacement class

\[
d\pmod{2\cdot3^L}.
\]

The one-sided ordering rule remembers the actual positive representative.  Therefore the next useful Bellman quantity is an amortized state

\[
(\mathfrak a,p,C),
\]

where

- `mathfrak a` is remaining mechanical alignment credit,
- `p` is previous displacement,
- `C` is accumulated correction cost.

The 138-node Christoffel DAG supplies the exact mechanical gap blocks across which this state must be propagated.

Companion certificate:

`collatz/src/first_resonance_initial_alignment_credit44_certificate.py`.
