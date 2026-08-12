# `A_32` shifted-block bootstrap and reuse of the certified prefix block

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap through selector depth 32**. The already certified `A_31` block is reused without re-enumeration; only its translated copy is certified. This does not prove the full Collatz conjecture.

## 1. Reuse identity

For the representative families

\[
A_d=\left\{4\left(3^{44}+\sum_{i=0}^{d-1}a_i3^i\right)+3:a_i\in\{0,1\}\right\},
\]

\[
\boxed{A_{d+1}=A_d\;\dot\cup\;(A_d+4\cdot3^d).}
\]

Since `A_31` is already certified recursive, only

\[
\boxed{A_{31}^+:=A_{31}+4\cdot3^{31}}
\]

must be newly certified.

Its size is

\[
\boxed{|A_{31}^+|=2^{31}=2,147,483,648.}
\]

## 2. Dyadic class sieve at B=24

Keep the growing binary resolution

\[
\boxed{B_{\max}=24.}
\]

The 31 free ternary selectors are first aggregated modulo `2^25`. For every occupied dyadic class the complete parity prefix through depth 24 is fixed, and each prefix iterate has affine form

\[
T^B(N)=\frac{3^{q_B}N+R_B}{2^B}.
\]

A class is removed whenever one prefix satisfies the uniform inequality

\[
(3^{q_B}-2^B)N+R_B<0
\]

throughout the shifted-half interval.

The exact class sieve leaves mass

\[
\boxed{146,725,219}
\]

of the `2^31` shifted representatives.

Thus

\[
\boxed{93.167574563995\%}
\]

of the new half-block is removed at class level, and only

\[
\boxed{6.832425436005\%}
\]

requires deterministic continuation.

## 3. Fringe certificate

Every one of the

\[
\boxed{146,725,219}
\]

surviving representatives is continued under the time-expanded accelerated Collatz map until it first falls below its own start.

Exact result:

\[
\boxed{\text{failures}=0,}
\]

and

\[
\boxed{\max\tau_<=438.}
\]

Hence the shifted family `A_31^+` is recursive.

Combining with the previously certified `A_31` gives

\[
\boxed{A_{32}\text{ is recursive}.}
\]

## 4. New contiguous verified floor

The representative-block bootstrap lemma now yields

\[
\boxed{V_{32}=4(3^{44}+3^{32})+2}
\]

with exact value

\[
\boxed{V_{32}=3,939,091,020,815,200,338,890.}
\]

The increment over `V_31` is

\[
\boxed{V_{32}-V_{31}=4\cdot(3^{32}-3^{31})
=4,941,387,170,271,576.}
\]

The cumulative increment over `V_0=4*3^44+2` is

\[
\boxed{V_{32}-V_0=4\cdot3^{32}=7,412,080,755,407,364.}
\]

## 5. Fixed-B saturation remains visible

At `B=24`, the reduced dyadic coordinate has modulus

\[
2^{23}=8,388,608.
\]

The class survivor density is already stabilizing near the corresponding fixed-resolution residue density. Thus the success of the `31 -> 32` bootstrap does not alter the previously proved fixed-resolution barrier: keeping `B=24` forever cannot be terminal.

The correct asymptotic target remains a sequence

\[
\boxed{B=B(d)\to\infty}
\]

while the reuse identity prevents recertifying already closed lower selector blocks.

## 6. Structural interpretation

The step has the form

\[
\boxed{
\text{reuse certified }A_{31}
\to
\text{aggregate the new shifted half by dyadic class}
\to
\text{discard }93.17\%\text{ by a proposition}
\to
\text{continue only the finite fringe}
\to
A_{32}\text{ certified}.
}
\]

This is the set-level bootstrap architecture intended for subsequent growing-resolution work.
