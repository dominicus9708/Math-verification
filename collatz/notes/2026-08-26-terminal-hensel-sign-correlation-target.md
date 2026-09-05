# First resonance: zero-target terminal Hensel lift and weighted sign-correlation threshold

Date: 2026-08-26

Status: **threshold arithmetic retained; sign-only proof route superseded.** The one-class Hensel lift and the numerical 50% mismatch threshold below remain exact. However, the later controllability audit

`2026-08-26-terminal-hensel-controllability-audit-and-minplus-target.md`

proves that the Hensel sign is locally steerable through the displacement class modulo 6, and that every finite mechanical block admits a zero-cost `d=0` path for a suitable boundary carry. Therefore the former target “prove Hensel/mechanical signs have small correlation” is not a valid standalone proof strategy. Any use of the threshold must retain the two boundary states, ordering memory, and actual displacement cost. This document does not prove the Collatz conjecture.

## 1. Terminal state

For the repaired first resonance

\[
(A,Q)=(114208327604,72057431991),
\]

let a terminal window contain the last \(m\) odd ordinals. Write its mechanical positions as

\[
B_t=b_{Q-m+1+t},\qquad
b_j=\lfloor (j-1)\log_2 3\rfloor,
\]

and displacement

\[
\delta_t=B_t-a_{Q-m+1+t}\ge0.
\]

The normalized terminal endpoint residue is

\[
Y_m(\delta)=
2^{-A}\sum_{t=0}^{m-1}3^{m-1-t}2^{B_t-\delta_t}.
\]

For an admissible endpoint \(y<3^{46}\), the terminal congruence is

\[
Y_m(\delta)\equiv y\pmod{3^m}.
\]

For \(m\ge46\), the higher ternary digits of the ordinary integer endpoint are zero. This turns every further left extension into a zero-target Hensel lift.

## 2. One-class Hensel lift lemma

Evaluate the old terminal sum one ternary digit deeper and define

\[
c_m:=\frac{Y_m(\delta)-y}{3^m}\pmod3.
\]

When one earlier odd ordinal is prepended, let its mechanical position be

\[
\widehat B_0=b_{Q-m}
\]

and its new displacement be \(d\ge0\). The old displacement vector shifts one coordinate to the right.

Modulo \(3^{m+1}\), the new endpoint condition is exactly

\[
\boxed{c_m+2^{\widehat B_0-A-d}\equiv0\pmod3.}
\]

Thus `c_m=0` has no child, while `c_m=1,2` each fixes exactly one parity class of \(d\). The ordering constraint remains

\[
\delta_1\le d+(\widehat B_1-\widehat B_0)-1.
\]

## 3. Retained weighted threshold

For odd ordinal \(j\), define

\[
c_j:=\frac{2^{b_j-1}}{3^j}.
\]

An odd displacement \(d_j\ge1\) costs at least \(c_j\), so

\[
\frac{E}{3^Q}\ge\sum_j c_j\mathbf1_{\{\text{odd displacement at }j\}}.
\]

For the first-resonance Farey cell,

\[
C_{\rm pre}:=\sum_{j=1}^{Q-46}c_j
>\frac{Q}{12\ln2}-\frac{46}{6}
>8{,}663{,}074{,}975.05\ldots.
\]

The certified total defect budget is

\[
\boxed{E/3^Q<4{,}314{,}000{,}000.}
\]

Hence any independently proved lower bound forcing at least half of the weighted single-step mass to be paid would close the first resonance:

\[
\boxed{\text{weighted forced cost}\ge\frac12C_{\rm pre}>4{,}331{,}537{,}487.52\ldots.}
\]

The numerical margin is greater than 17.5 million.

## 4. Superseded sign-only interpretation

It remains algebraically true that a mismatch between the currently required Hensel parity and the mechanical parity forces a positive odd displacement. What is no longer valid is to treat the Hensel sign sequence as an externally fixed sequence whose correlation with the mechanical sign can be bounded independently.

The exact modulo-9 audit proves that, once the required parity is fixed, the three classes

\[
d,\ d+2,\ d+4
\]

produce next carry digits \(0,1,2\) exactly once each. Thus displacement choices can steer the next Hensel sign. Moreover, for an arbitrary finite block there is always a suitable boundary carry supporting \(d=0\) throughout the block.

Therefore a pure sign-correlation theorem is not the remaining target.

## 5. Correct target

The correct state must retain

\[
\boxed{
\text{3-adic Hensel carry}
+\text{previous displacement}
+\text{mechanical gap}
+\text{endpoint/start boundaries}.
}
\]

The action cost is

\[
\kappa_j(d)=2c_j(1-2^{-d}).
\]

The proof problem is the two-boundary minimum-cost path

\[
V_m(K,p)=\min_d\left\{\kappa_m(d)+V_{m+1}\left(\frac{K+2^{e_m-d}}3,d\right)\right\},
\]

subject to Hensel divisibility, continuation, and ordering. The first resonance closes if the exact two-boundary value exceeds

\[
\boxed{4{,}314{,}000{,}000.}
\]

The preferred next route is a Christoffel/continued-fraction min-plus renormalization of this operator, not a sign-only discrepancy estimate and not unit-by-unit support growth.

Companion retained threshold certificate:

`collatz/src/first_resonance_terminal_hensel_sign_threshold_certificate.py`.

Correcting audit:

`collatz/src/terminal_hensel_three_class_controllability_certificate.py`.
