# One promoted A0 return preserves the A0-scale wall

Date: 2026-08-27

Status: **SAFE LEMMA + exact rational/Worley-Dujella certificate inside the repaired multi-boundary branch.** No ternary Cantor-core entry and no repeated-local pullback is used. This is not a proof of the Collatz conjecture.

## 1. Starting promoted state

Let

\[
G=2^{33}.
\]

After two consecutive `J0/R0` gap debits, the repaired branch gives

\[
X=N+d,
\qquad
0\le d<2G,
\qquad
N>2^{71}.
\]

The resonance-promotion theorem proves that the first possible coefficient-subcritical scale is

\[
(A_0,Q_0)
=(114208327604,72057431991).
\]

Assume that this promoted crossing is actually realized and put

\[
X'=T^{A_0}(X)=N+d'.
\]

We determine how much the root gap can grow and whether the smaller `J0` scale can immediately return.

## 2. Mechanical correction ceiling at A0

Let

\[
\delta_A=A_0\ln2-Q_0\ln3>0,
\qquad
C_A=e^{-\delta_A}=\frac{3^{Q_0}}{2^{A_0}}<1.
\]

For a genuine first coefficient crossing at this pair, the normalized mechanical correction satisfies

\[
S_A\le\frac{Q_0}{6\ln2}+\frac13.
\]

The endpoint formula is

\[
X'=C_A(X+S_A).
\]

Therefore

\[
d'
=C_A d-(1-C_A)N+C_A S_A.
\]

Using

\[
C_A<1,
\qquad
1-C_A\ge\frac{\delta_A}{1+\delta_A},
\qquad
N>2^{71},
\]

gives

\[
d'
<d+\left(
\frac{Q_0}{6\ln2}+\frac13
-2^{71}\frac{\delta_A}{1+\delta_A}
\right).
\]

The exact rational certificate proves

\[
\boxed{
\frac{Q_0}{6\ln2}+\frac13
-2^{71}\frac{\delta_A}{1+\delta_A}
<0.51G.
}
\]

The sharper certified numerical ratio is about

\[
0.502208G.
\]

Thus one promoted `A0/Q0` crossing can increase the additive gap by only about half of the original `2^33` unit.

## 3. Post-A0 gap remains below 2.51G

Since the incoming gap satisfies

\[
d<2G,
\]

we obtain

\[
\boxed{
d'<2.51G.}
\]

So the promoted crossing does not return the endpoint to the broad `7G` second-resonance annulus.  It remains in a much thinner near-root strip.

## 4. J0 still cannot reappear

For the lower local resonance

\[
(J_0,R_0)
=(10439860591,6586818670),
\]

the necessary near-survival threshold is controlled by

\[
\Delta_J
:=
2^{71}\frac{\delta_J}{1+\delta_J}
-\frac{R_0}{3},
\]

where

\[
\delta_J=J_0\ln2-R_0\ln3>0.
\]

The exact rational certificate strengthens the previous debit estimate to

\[
\boxed{
\Delta_J>2.527G.
}
\]

Hence any endpoint with gap below `2.527G` cannot realize `J0/R0` as its first coefficient-subcritical prefix.

Since

\[
d'<2.51G<2.527G,
\]

we get

\[
\boxed{
J_0/R_0\text{ remains forbidden after one promoted }A_0/Q_0\text{ return.}
}
\]

## 5. Complete wall audit up to A0 at the enlarged 2.51G gap

It remains to exclude a different intermediate Diophantine pair between `J0` and `A0`.

At gap bound

\[
d<2.51G,
\]

the near-survival approximation constant satisfies

\[
\left|\alpha-\frac qj\right|
<\frac{K}{j^2},
\qquad
\alpha=\log_3 2,
\]

with

\[
\boxed{K<2.007.}
\]

Thus the Worley-Dujella condition has

\[
rs<2K<4.014,
\]

so only

\[
\boxed{rs\le4}
\]

need be considered.

The exact certificate enumerates the complete adjacent-convergent primitive superset, obtaining 27 distinct lower-side candidate fractions below denominator `A0`.

For each primitive candidate `(a,b)`, every positive multiple

\[
(q,j)=m(a,b),
\qquad
mb<A_0,
\]

is excluded by the same exact concavity argument used in the preceding repaired endpoint audits.

All 27 multiplicity ranges fail the necessary near-survival inequality.

Therefore

\[
\boxed{
\text{no coefficient-subcritical prefix occurs for }1\le j<A_0
}
\]

even after the gap has expanded from `<2G` to `<2.51G`.

The `A0/Q0` pair itself remains nonexcluded.

## 6. Persistence theorem

Combining the gap transport and the renewed Diophantine wall gives

\[
\boxed{
\begin{aligned}
d<2G,
&\quad\text{first crossing }=A_0/Q_0\\
&\Longrightarrow d'<2.51G,\\
&\Longrightarrow J_0/R_0\text{ remains forbidden},\\
&\Longrightarrow\text{the next possible crossing is again }A_0/Q_0.
\end{aligned}
}
\]

Thus the resonance promotion obtained after the two `J0` debits is not destroyed immediately.  It persists across at least one full promoted `A0` return.

## 7. DSD interpretation

The gap-budget state now supports two qualitatively different transitions:

\[
J_0:\quad\text{large strict debit }>-2.527G,
\]

\[
A_0:\quad\text{small possible credit }<+0.51G.
\]

The lower scale therefore acts as a strong gap-consuming transition, whereas the promoted scale can replenish only a small fraction of that resource in one use.

This creates a natural weighted transition system on

\[
\boxed{(\text{resonance scale},\text{gap budget})}
\]

rather than an unstructured sequence of large parity words.

## 8. Current next target

A second consecutive `A0/Q0` return would give the coarse envelope

\[
d''<3.02G.
\]

At that level the `J0` necessary threshold can become admissible again.  The next calculation should therefore classify the two-step promoted transition:

- whether a second `A0` block can actually realize the maximal gap credit;
- whether `J0` must then re-enter;
- and whether every `A0,A0,J0` macrocycle has a strictly negative net gap budget.

A negative macrocycle budget would turn the present local inequalities into a genuine long-run exclusion mechanism.

## 9. Audit classification

- **SAFE:** mechanical correction ceiling at a genuine `A0` first crossing.
- **SAFE:** one-block gap credit `<0.51G`.
- **SAFE:** post-crossing gap `<2.51G`.
- **SAFE:** strengthened `J0` threshold `>2.527G`.
- **SAFE:** complete `rs<=4` Worley-Dujella audit below `A0`.
- **OPEN:** two-or-more consecutive `A0` returns and the resulting macrocycle budget.

Companion certificate:

`collatz/src/A0_local_return_gap_persistence_certificate.py`
