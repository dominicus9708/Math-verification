# Closure-focused reduction of the current first-crossing resonance

Date: 2026-08-18

Status: **exact reductions + eliminated proof branches + one remaining closure target**.

This note deliberately stops extending the finite E-ladder and records only what is useful for closing the current isolated resonance.  Nothing here by itself is a proof of the Collatz conjecture.

## 1. Finite floor immediately before R1

The exact shifted `a_32=1` hybrid certificate, together with the previously closed complementary half, advances the recursively-sufficient Cantor floor to

\[
V_{33}=4(3^{44}+3^{33})+2
=3,939,105,844,976,711,153,618.
\]

Hence the R1 lower endpoint

\[
N_0=V_{33}+1
\]

is exactly the first unverified Cantor-core member after the finite bootstrap.  The remaining m=44 selectors are precisely those with at least one active digit among `a_33,...,a_43`, so their count is

\[
2^{44}-2^{33}.
\]

## 2. Exact current-resonance dangerous dimension

For

\[
(q,\sigma)=(137,528,045,312,\ 217,976,794,617)
\]

put

\[
\varepsilon=\sigma\log2-q\log3,
\qquad
D=2^\sigma-3^q.
\]

The rational certificate `current_resonance_danger25_layer46_certificate.py` proves

\[
\log(1+3^{-26})<\varepsilon<\log(1+3^{-25}),
\]

hence

\[
3^{q-26}<D<3^{q-25}
\]

and therefore

\[
\boxed{h(q)=25}.
\]

Only the first 25 odd-position axes can support an elementary canonical-start / descent-margin order reversal.

## 3. Exact start-range reduction to three Cantor layers

The mechanical first-crossing envelope gives

\[
S\le \frac{q}{6\log2}+\frac13.
\]

Using the exact lower rational bound on

\[
\delta=\exp(\varepsilon)-1
\]

gives the safe start ceiling

\[
x<3.680\times10^{22}.
\]

The certificate proves this lies below

\[
4\cdot3^{47}+3.
\]

Together with the verified V33 floor, a minimal counterexample at the current resonance can therefore lie only in

\[
\boxed{m=44,45,46}.
\]

For m=46, writing

\[
N=4\left(3^{46}+\sum_{i=0}^{45}a_i3^i\right)+3,
\]

the same rational ceiling implies the safe over-family

1. `a_43=0`, with `a_0,...,a_42` arbitrary; or
2. `a_43=1`, `a_40=a_41=a_42=0`, with `a_0,...,a_39` arbitrary.

Thus the m=46 part is contained in at most

\[
\boxed{2^{43}+2^{40}}
\]

selector addresses.

The whole finite selector over-family remaining under this resonance is therefore bounded by

\[
\boxed{
(2^{44}-2^{33})+2^{45}+2^{43}+2^{40}
=62,663,572,848,640.
}
\]

This number is recorded only as a finite-size reference; direct enumeration is not the intended proof method.

## 4. Proof branches eliminated in the closure audit

### 4.1 E13 4096 pullback is not monotone in E

The E13 terminal 3-adic obstruction is exact for E=13, but after rewriting a terminal correction rank as

\[
g_r=T-1-r-p_{E-1-r},
\]

the unrestricted terminal language for larger E rapidly admits 4096-separated correction pairs modulo small powers of 3.  Thus the E13 obstruction cannot simply be declared monotone for all E>=22.  Additional R1 constraints would be needed.

### 4.2 Large E does not give automatic pre-gate descent

The exact run-cap optimizer was extended through the coefficient-surviving range E<=567.  Even at E=567, the relaxed maximum 1539-step endpoint remains above the R1 lower start by a factor greater than four.  Hence no terminal-E threshold closes the remaining branch by endpoint size alone.

### 4.3 Abstract G13 repair existence is not attachment

An exact H<=1 G13 path carrying credit 4096 to 1 exists.  Therefore a proof based on nonexistence of such repair is false.  The relevant question is whether a repair path can attach to the same finite-natural R1 start.

### 4.4 Safe Euclidean blocks are not uniformly contracting

The exact neutral U7 difference-basis certificate proves full residue-difference coverage and a successor-growth threshold D>=191.  Hence the safe tail cannot be replaced by a blanket contraction assumption.

### 4.5 Formation sparsity cannot be combined with an independence assumption

The actual trajectory generates its own formation congruence.  Formation target sparsity is useful, but treating the candidate address as independent/equidistributed relative to that target language would be circular without a separate dynamical transversality theorem.

## 5. The remaining closure target

After the audit, the current resonance should be attacked as a **same-integer compatibility problem**:

> Can a recursively-sufficient Cantor address in the finite m=44,45,46 range simultaneously realize one of the 25-dimensional dangerous first-crossing signatures and admit a safe-tail completion with nonpositive descent margin?

The already proved pieces are:

1. finite Cantor floor through V33;
2. exact dangerous dimension h=25;
3. local co-order on every axis i>25;
4. positive proportionality of every mixed interaction tensor of order >=2;
5. exact start ceiling reducing the Cantor side to m=44,45,46.

What is still missing is the **Dangerous-Core Extremal Reduction** (or an equivalent same-integer incompatibility theorem) that contracts the safe tail without assuming uniform contraction or statistical independence.

This is the sole structural target retained for the next closure step.  Extending E=22, A33, or isolated repair witnesses is secondary unless it directly proves this compatibility obstruction.
