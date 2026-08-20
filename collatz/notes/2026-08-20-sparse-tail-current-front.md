# Sparse-tail current front after macro digit and normalized-cocycle reductions

Date: 2026-08-20

Status: **current proof-front summary for the corrected coefficient-only Stage 4 sparse tail.** This is not a proof of the Collatz conjecture.

## Closed structural reductions

The sparse-tail representation now has the following exact chain.

1. Actual prefix state:
   \[
   a=b_s+h,
   \]
   so the independent state is \((s,h,\rho)\).

2. Macro lift digit:
   \[
   J=[(r_W-\rho)3^{-a}]_{2^B}.
   \]

3. Remaining progression parameter:
   \[
   t=J+2^Bt'.
   \]

4. Iterated digit concatenation:
   \[
   t=\sum_{i=0}^{n-1}J_i2^{iB}+2^{nB}t_n.
   \]

5. Ordinary finite integers therefore induce an eventually-zero macro-lift tail.

6. Exact 2-adic query normal form:
   \[
   \xi'=\frac{\xi+\gamma_W(a)+J}{2^B}.
   \]

7. Exact Archimedean normalized coordinate:
   \[
   v=\frac{2^s\rho}{3^a},
   \]
   with
   \[
   v'=v+2^sJ+\frac{2^sR_W}{3^{a+Q}}.
   \]

8. On zero-lift blocks:
   \[
   0\le v'-v\le\frac{2^{B-1}}3.
   \]

Hence a zero-lift tail reachable from a fixed state lies inside a linearly widening normalized corridor, rather than the full ternary box.

## Exact finite normalized-box closure

For all reachable phase-height boxes through \(s=15\), exhaustive exact scans give finite zero-tail caps. The largest checked cap is

\[
Z(15,5)=374,
\]

attained first at

\[
\rho=10,507,503.
\]

This finite result is diagnostic only.

## Remaining deterministic theorem

Define

\[
\widehat\mu_{s,h}(L)
=\frac{2^s}{3^{b_s+h}}\mu_{s,h}(L).
\]

The current sharp sparse-tail target is:

> prove that the normalized generalized minimal survivor eventually outruns every zero-lift linear corridor allowed by the exact normalized cocycle.

For macro size \(B\), a sufficient comparison at the \(n\)-th zero-lift block is

\[
\boxed{
\widehat\mu_{s_n,h_n}(L)
>
v_0+n\frac{2^{B-1}}3.
}
\]

Such an inequality forces a new nonzero macro lift within the next \(L\) ordinary steps.

A uniform mechanism producing these forced lifts infinitely often would exclude ordinary-integer infinite coefficient survivors in this exact lift representation.

## Global Stage-4 placement

The corrected unconditional proof program is therefore split into:

\[
\boxed{
\text{Haar-controlled selector/coefficient bulk}
\longrightarrow
\text{normalized min-plus late-lift tail}.
}
\]

The bulk side controls same-integer concentration while selector mass is large. The sparse side now has an exact additive normalized coordinate and a precise minimal-survivor comparison target.

The unresolved point is no longer state identification or coordinate alignment. It is a quantitative lower bound for \(\widehat\mu_{s,h}\) strong enough to beat the linear corridor uniformly along reachable phase-height states.
