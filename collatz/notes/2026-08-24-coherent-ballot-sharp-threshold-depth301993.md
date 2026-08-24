# Sharp coherent-ballot threshold through depth 301,993

Date: 2026-08-24

Status: **exact finite auxiliary theorem.**  This is broader than the m=45 certificate but still finite in horizon.  It is not a proof of the Collatz conjecture.

## Theorem

For the accelerated Collatz map, assume

\[
N\equiv3\pmod4,
\]

so the first two parity symbols are forced `11`.

Define

\[
b_H:=\min\{q:3^q\ge2^H\}.
\]

For the unique mechanical boundary prefix with odd count \(b_H\), let \(R_H^{\rm mech}\) denote its affine correction.

At a Beatty rise

\[
b_H=b_{H-1}+1,
\]

the only possible **first** coherent coefficient-subcritical no-descent child is the even child of the previous boundary prefix.  It has correction \(R_{H-1}^{\rm mech}\), odd count \(b_H-1\), and can remain at or above its start only if

\[
R_{H-1}^{\rm mech}
\ge
N\left(2^H-3^{b_H-1}\right).
\]

Exact arithmetic through

\[
H=301{,}993
\]

shows that the smallest integer \(N_0\) which makes the strict reverse inequality hold at **every** rise is

\[
\boxed{N_0=5{,}205{,}340{,}380.}
\]

Therefore every

\[
\boxed{N\equiv3\pmod4,\quad N\ge5{,}205{,}340{,}380}
\]

satisfies

\[
\boxed{
T^j(N)\ge N\ \forall j\le H
\Longrightarrow
3^{q_j}\ge2^j\ \forall j\le H
}
\]

for every \(H\le301{,}993\).

## Sharpness inside this mechanical-boundary argument

The preceding integer is sharp for this exact criterion:

\[
N_0-1=5{,}205{,}340{,}379
\]

fails at

\[
\boxed{H=125{,}743,\qquad q=79{,}335.}
\]

Thus the threshold is not merely a rounded safety constant.

## Relation to the recursively sufficient core

The least starts in consecutive ternary-Cantor layers are

\[
4\cdot3^{19}+3=4{,}649{,}045{,}871,
\]

\[
4\cdot3^{20}+3=13{,}947{,}137{,}607.
\]

Hence

\[
4\cdot3^{19}+3<N_0<4\cdot3^{20}+3.
\]

Therefore every recursively sufficient layer

\[
\boxed{m\ge20}
\]

is automatically covered through depth 301,993.

In particular the current difficult layers m=44 and m=45 are far inside the safe range.

## Role

This theorem isolates the remaining difficulty cleanly.

For all current large recursively sufficient layers, additive correction cannot create a coherent path below the coefficient barrier anywhere in the first 301,993 accelerated steps.  Thus within this horizon the actual no-descent problem reduces exactly to the same-address realization of the coefficient-surviving ballot language.

The theorem does **not** say that coefficient-surviving words are absent.  The unresolved task is to prove that the ternary 0/1 recursively sufficient starts cannot realize such an exceptionally long dyadic ballot prefix.

Certificate:

`collatz/src/coherent_ballot_threshold_depth301993_certificate.cpp`.
