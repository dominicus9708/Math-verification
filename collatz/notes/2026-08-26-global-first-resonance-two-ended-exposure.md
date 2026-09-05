# First global resonance: two-ended finite-address exposure

Date: 2026-08-26

Status: **exact algebraic reduction + exact mechanical endpoint certificate.** This is in the repaired global binary branch and does not use the disputed ternary selector or repeated local pullback. It does not prove the Collatz conjecture.

## 1. First-resonance band

At the first possible global coefficient crossing,

\[
(A_0,q_0)
=(114208327604,72057431991),
\]

every hypothetical minimal-counterexample start satisfies

\[
2^{71}<N<\frac43\,2^{71}<2^{72}
\]

and its crossing endpoint has the form

\[
y=T^{A_0}(N)=N+g,
\qquad
0<g<2^{33},
\qquad
4\mid g.
\]

Thus

\[
\boxed{
y<\frac43\,2^{71}+2^{33}<2^{72}.}
\]

## 2. Start-side exposure

A length-72 parity prefix determines one residue modulo \(2^{72}\). Because every candidate start lies strictly below \(2^{72}\), its first 72 parity symbols determine the ordinary integer \(N\) itself.

This is the already-used dyadic address exposure:

\[
\boxed{
N=\rho_{72}(w)
\quad\text{for every first-resonance candidate.}
}
\]

## 3. Endpoint-side exposure

Write the full first-crossing affine identity as

\[
2^{A_0}y
=3^{q_0}N+R,
\]

where, if the odd positions are

\[
0\le a_1<\cdots<a_{q_0}<A_0,
\]

then

\[
R=
\sum_{j=1}^{q_0}
3^{q_0-j}2^{a_j}.
\]

Reduce modulo \(3^{46}\). Since \(q_0>46\), the term \(3^{q_0}N\) vanishes. Every correction term with \(q_0-j\ge46\) also vanishes. Therefore only the **last 46 odd ordinals** remain:

\[
2^{A_0}y
\equiv
\sum_{\ell=0}^{45}
3^\ell 2^{a_{q_0-\ell}}
\pmod{3^{46}}.
\]

Because \(2\) is invertible modulo \(3^{46}\),

\[
\boxed{
y
\equiv
2^{-A_0}
\sum_{\ell=0}^{45}
3^\ell 2^{a_{q_0-\ell}}
\pmod{3^{46}}.}
\]

But

\[
3^{46}=8862938119652501095929
>2^{72}=4722366482869645213696
>y.
\]

Hence the least nonnegative residue is not merely a congruence class: it is the endpoint itself.

Thus

\[
\boxed{
\text{the last 46 odd-event positions determine the complete ordinary endpoint }y.
}
\]

This is the exact ternary-end analogue of the 72-bit start exposure.

## 4. Exact mechanical tail

Let

\[
\gamma:=\log_2 3.
\]

The odd positions of the first-crossing mechanical word are

\[
b_j=\lfloor(j-1)\gamma\rfloor.
\]

The companion certificate encloses \(\ln2\) and \(\ln3\) by exact rational positive-series bounds, so the following 46 positions are certified without floating point:

\[
\begin{aligned}
&114208327531,114208327532,114208327534,114208327535,\\
&114208327537,114208327539,114208327540,114208327542,\\
&114208327543,114208327545,114208327546,114208327548,\\
&114208327550,114208327551,114208327553,114208327554,\\
&114208327556,114208327558,114208327559,114208327561,\\
&114208327562,114208327564,114208327565,114208327567,\\
&114208327569,114208327570,114208327572,114208327573,\\
&114208327575,114208327577,114208327578,114208327580,\\
&114208327581,114208327583,114208327584,114208327586,\\
&114208327588,114208327589,114208327591,114208327592,\\
&114208327594,114208327596,114208327597,114208327599,\\
&114208327600,114208327602.
\end{aligned}
\]

Their gaps are only 1 or 2, as expected for the Sturmian/mechanical boundary.

## 5. Mechanical endpoint is outside the near-return band

Substituting those exact tail positions into the endpoint residue gives

\[
\boxed{
y_{\rm mech}
=4699104266570964686821.}
\]

The allowed first-resonance endpoint band satisfies

\[
3y<4\cdot2^{71}+3\cdot2^{33}.
\]

The certificate checks exactly

\[
\boxed{
3y_{\rm mech}
>
4\cdot2^{71}+3\cdot2^{33}.
}
\]

Thus the unique correction-maximizing mechanical first-crossing word is independently incompatible with the endpoint boundary as well as with the start boundary.

## 6. Two-ended state decomposition

The first resonance may now be decomposed as

\[
\boxed{
\underbrace{\text{first 72 parity positions}}_{\text{complete start }N}
\;\big|\;
\underbrace{\text{long coefficient-surviving bridge}}_{\text{middle}}
\;\big|\;
\underbrace{\text{last 46 odd ordinals}}_{\text{complete endpoint }y}
}
\]

with the short arithmetic coupling

\[
\boxed{0<y-N=g<2^{33},\qquad4\mid g.}
\]

This is stronger than treating the first resonance as a single \(114\)-billion-step word. Both ordinary natural-number ends are already finite-address objects; only the middle bridge remains long.

## 7. DSD audit interpretation

The DSD contribution here is the re-alignment of three descriptions of the same state transition:

- dyadic prefix formation fixes the start;
- ternary suffix formation fixes the endpoint;
- the renewal gap fixes their small difference.

No new DSD axiom enters the mathematics. The proof obligation is now a standard arithmetic **two-boundary bridge incompatibility** statement:

> show that no coefficient-surviving first-crossing word can connect an allowed 72-bit start boundary to an allowed 46-ternary endpoint boundary while respecting the tiny gap and the first-crossing defect budget.

## 8. Next target

Define a late displacement state for the last 46 odd ordinals and derive its exact endpoint-shift formula relative to the mechanical tail. Then combine it with the already-proved early condition

\[
D_{72}\ge11
\]

and the shared correction-defect state.

The goal is not to enumerate the middle bridge; it is to prove that the early and late boundary conditions demand incompatible projections of the same displacement/excursion path.

Certificate:

`collatz/src/global_first_resonance_two_ended_mechanical_exclusion.py`.
