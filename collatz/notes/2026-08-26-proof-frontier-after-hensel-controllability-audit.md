# Proof frontier after the terminal Hensel controllability audit

Date: 2026-08-26

Status: **proof-architecture audit.** This document records which branches are exact, conditional, superseded, or still open. It does not prove the Collatz conjecture.

## 1. Repaired global entry chain

The disputed ternary recursively-sufficient Cantor-core entry is not used in the global proof line.

The repaired binary line is

\[
\text{published finite verification}
\to
\text{parity recursive-sufficiency wall}
\to
\text{long exact coefficient-survival gate}
\to
\text{whole-prefix / Hensel structural constraints}.
\]

The first exact coefficient resonance after the sharp constant-wall gate is

\[
(A_0,Q_0)=(114208327604,72057431991).
\]

## 2. Exact first-resonance boundary information

The currently certified first-resonance branch includes:

- start band
  \[
  2^{71}<N<{4\over3}2^{71}<2^{72};
  \]
- near-return endpoint
  \[
  y=N+g,
  \qquad
  0<g<2^{33},
  \qquad
  4\mid g;
  \]
- complete start exposure by the first 72 parity bits;
- complete endpoint exposure by the final 46 odd ordinals;
- mechanical equality excluded independently at both boundaries;
- early displacement lower bound
  \[
  D_{72}\ge11;
  \]
- terminal low-support ladder through the certified support-10 closure;
- global displacement upper budget
  \[
  r_*\le42009999999;
  \]
- exact normalized correction budget
  \[
  E/3^{Q_0}<4314000000.
  \]

The later support-11 computations remain useful calibration, but any claim depending on the complete three-state support-11 classification should be accompanied by its standalone exhaustive certificate before being promoted to the canonical proof line.

## 3. Superseded first-resonance target

The following route is **superseded**:

\[
\text{Hensel sign sequence}
\stackrel{?}{\text{has small correlation}}
\text{mechanical sign sequence}.
\]

The exact modulo-9 controllability lemma shows that once the required displacement parity is fixed, three consecutive same-parity classes

\[
d,d+2,d+4
\]

produce next carry digits `0,1,2` exactly once each.  Hence the next Hensel sign can be steered through the displacement control.

Moreover every finite mechanical block admits a zero-cost `d=0` path for a suitable boundary carry. Therefore no positive local block-cost theorem can hold uniformly after boundary data are discarded.

## 4. Correct first-resonance target

The first-resonance finite branch is now an exact **two-boundary controlled min-plus problem**.

State:

\[
(K,p)
\]

with 3-adic carry `K` and previous displacement `p`.

Control:

\[
d\ge\max\{0,p-g+1\},
\qquad
K+2^{e-d}\equiv0\pmod3.
\]

Transition:

\[
K'={K+2^{e-d}\over3},
\qquad p'=d.
\]

Real cost:

\[
\kappa_j(d)=2c_j(1-2^{-d}).
\]

Target:

\[
\boxed{
V_{\rm first\ resonance}>4314000000.
}
\]

The value must be conditioned simultaneously on the ordinary endpoint boundary and the dyadic start boundary.

## 5. Exact compression now available

Three exact structural reductions are available for this operator.

### 5.1 Weighted block composition

For a mechanical gap block `w`,

\[
\lambda(w)={3^{|w|}\over2^{G(w)}}.
\]

For concatenation `uv`,

\[
\mathcal T_{uv}(S,T)
=
\inf_R
\left[
\mathcal T_u(S,R)
+
\lambda(u)\mathcal T_v(R,T)
\right].
\]

### 5.2 Finite-horizon carry quotient

With `r` Hensel digits remaining,

\[
K\bmod3^r
\]

contains all carry information needed by the remaining decisions.

### 5.3 Pareto dominance

At the same phase and same carry class modulo `3^r`,

\[
p_1\le p_2,
\qquad C_1\le C_2
\]

implies state 1 dominates state 2.

Thus an exact solver may retain only the Pareto frontier in `(p,C)` per finite-horizon carry class.

## 6. Christoffel / continued-fraction route

The first-resonance mechanical slope has continued fraction

\[
[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,10].
\]

Therefore the `Q_0`-scale mechanical gap word has a short Euclidean/Christoffel description. The next finite-branch objective is to certify the exact anchored block decomposition and apply the weighted min-plus composition recursively.

The unresolved state-space issue is to find a further interface compression or Bellman dual potential that prevents the carry quotient from growing like `3^r` at macroscopic blocks.

## 7. Infinite-survivor branch

The independent infinite coefficient-survival branch remains open.

A sufficient target is the minimal-survivor growth theorem

\[
\mu(K)=\min\{n:\tau_c(n)>K\}\to\infty.
\]

A quantitatively stronger bound

\[
\mu(K)>CK^{8.616}
\]

eventually would simultaneously eliminate sufficiently large finite paradoxical first crossings and the infinite-survival branch, after a finite residual verification.

Thus `mu(K)` growth is the **higher-level unified target**. The first-resonance two-boundary problem is a much more constrained finite test case and a source of structural lemmas, but it should not be confused with the full infinite-survivor theorem.

## 8. Current puzzle pieces

The proof architecture is now:

\[
\boxed{
\begin{array}{ll}
F:&\text{two-boundary controlled min-plus exclusion of finite crossings},\\
I:&\text{formation-floor / minimal-survivor escape for infinite survival},\\
G:&\text{minimal-counterexample dichotomy and final domain audit}.
\end{array}}
\]

A sufficiently strong uniform `mu(K)` theorem could replace both `F` and `I`; otherwise they remain parallel branches.

## 9. DSD role

DSD is used as a proof-chain audit and reorganization method. In this stage it identified that the map

\[
\text{Hensel carry}\to\text{required sign}
\]

was valid, but projecting further to an uncontrolled sign-correlation problem discarded the displacement control and boundary domain. Restoring those variables produced the corrected min-plus state.

The final arithmetic claims remain ordinary modular/integer statements and can be externally checked without accepting DSD as an additional axiom system.
