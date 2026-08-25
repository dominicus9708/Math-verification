# First global resonance: exact near-return gap channel

Date: 2026-08-26

Status: exact finite reduction after taking Barina's published convergence verification below \(2^{71}\), the mechanical first-crossing envelope, and Hercher's nontrivial-cycle theorem as external inputs. No ternary selector and no repeated local pullback is used. This is not a proof of Collatz.

## 1. Boundary cell

From the sharp constant-wall parity-RS theorem, the first possible coefficient-crossing pair is

\[
(A_0,q_0)
=(114,208,327,604,\ 72,057,431,991).
\]

Let a hypothetical minimal counterexample \(N\) first cross the coefficient barrier there and put

\[
E:=T^{A_0}(N)=N+g.
\]

Since \(N\) is a counterexample to first descent,

\[
g\ge0.
\]

## 2. Mechanical correction gives a tiny endpoint gap

Write

\[
P=\frac{2^{A_0}}{3^{q_0}}>1.
\]

In normalized correction form,

\[
E=\frac{N+S_w}{P},
\]
so

\[
g=E-N
=\frac{S_w-(P-1)N}{P}.
\]

The first-crossing mechanical envelope gives

\[
S_w\le\frac{q_0}{6\ln2}+\frac13.
\]

Also

\[
P-1\ge\ln P
=A_0\ln2-q_0\ln3.
\]

Using \(N\ge2^{71}\), exact directed rational logarithm bounds therefore give

\[
0\le g
<
\frac{q_0}{6\ln2}+\frac13
-2^{71}(A_0\ln2-q_0\ln3)
<2^{33}.
\]

Thus

\[
\boxed{0\le g<2^{33}.}
\]

This is an enormous compression: after more than \(1.14\times10^{11}\) accelerated steps, the orbit may differ from its starting value by fewer than \(8.6\times10^9\).

## 3. Minimality forces both ends to be 3 mod 4

A minimal counterexample must satisfy

\[
N\equiv3\pmod4.
\]

Indeed an even start descends immediately, while for \(N\equiv1\pmod4\),

\[
T^2(N)=\frac{3N+1}{4}<N.
\]

Now consider \(E=N+g\). Since the future orbit from \(E\) is still the future orbit of the same counterexample, it cannot descend below \(N\).

If \(E\) were even, then

\[
T(E)=E/2<N
\]

because \(g<N\).

If

\[
E\equiv1\pmod4,
\]
then

\[
T^2(E)=\frac{3E+1}{4}
=\frac{3N+3g+1}{4}<N,
\]

because the certified bound gives

\[
3g+1<3\cdot2^{33}+1<2^{71}<N.
\]

Therefore

\[
\boxed{E\equiv3\pmod4}.
\]

Since also \(N\equiv3\pmod4\),

\[
\boxed{g\equiv0\pmod4}.
\]

## 4. Zero gap is a forbidden nontrivial cycle

If

\[
g=0,
\]
then

\[
T^{A_0}(N)=N,
\]
so \(N\) lies on a nontrivial positive Collatz cycle containing exactly \(q_0\) odd shortcut states during this period.

Hercher proves that once the convergence verification threshold satisfies

\[
X_0\ge3\cdot2^{69},
\]
every nontrivial cycle must contain more than

\[
1.375\times10^{11}
\]
odd members.

The published finite base obeys

\[
2^{71}=4\cdot2^{69}>3\cdot2^{69},
\]
whereas

\[
q_0=72,057,431,991<137,500,000,000.
\]

Hence \(g=0\) is impossible.

## 5. Final first-cell gap theorem

Combining the preceding sections gives

\[
\boxed{
g\in4\mathbb Z_{>0},\qquad g<2^{33}.}
\]

Equivalently,

\[
\boxed{
g\in\{4,8,12,\ldots\}\cap(0,2^{33}).}
\]

Thus the first unresolved global resonance is not merely a 72-bit starting-address problem. It must also land, after \(114,208,327,604\) accelerated steps, on another \(3\pmod4\) integer lying within a tiny positive gap of the start.

## 6. DSD audit

The chain remains entirely binary/dynamical:

\[
\text{published finite base}
\to
\text{sharp parity-RS gate}
\to
\text{fixed first crossing pair}
\to
\text{mechanical correction ceiling}
\to
\text{tiny endpoint gap}
\to
\text{mod-4 + cycle exclusion}.
\]

No ternary selector condition has entered.

## 7. Next target

The next exact arithmetic target is now the boundary-cell formation problem:

> classify first-crossing words of the fixed pair \((A_0,q_0)\) whose dyadic formation residue lies in the 72-bit start band and whose endpoint gap lies in
> \[
> 4\mathbb Z_{>0}\cap(0,2^{33}).
> \]

The Christoffel equality word and its near-Christoffel defect classes should be treated separately, because the latter already carry a quantitative correction defect and a modular gap channel.

Certificate:

`collatz/src/global_first_resonance_near_return_gap_certificate.py`.
