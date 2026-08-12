# R1 first-crossing global lower bound from paradoxical frontier

Date: 2026-08-12

Status: **exact structural reduction + finite audit + external finite frontier**. This gives a large unconditional lower bound on the odd-event depth of any R1 renewal-floor counterexample, conditional only on the published Rozier--Terracol finite theorem used as stated. It does not exclude R1.

## 1. R1 first coefficient crossing

Let `N` be a renewal floor on a hypothetical nonperiodic Collatz counterexample and suppose the coefficient stopping time from `N` is finite.

Let the first coefficient crossing occur after

\[
A\text{ accelerated steps}
\]

containing

\[
H\text{ odd steps}.
\]

Put

\[
\gamma:=\log_2 3.
\]

By first crossing,

\[
2^{A-1}<3^H<2^A,
\]

so

\[
\boxed{A=\lceil H\gamma\rceil.}
\]

Write

\[
P:=\frac{2^A}{3^H}>1.
\]

Let the normalized affine correction be `r`, so that the first-crossing endpoint is

\[
Y=\frac{N+r}{P}.
\]

Because `N` is a suffix minimum of the hypothetical counterexample orbit,

\[
Y\ge N.
\]

Hence

\[
\boxed{(P-1)N\le r.}
\]

The universal Beatty first-crossing bound gives

\[
\boxed{r<\frac H3.}
\]

Therefore every R1 floor satisfies

\[
\boxed{
N<\frac{H}{3(P-1)}.
}
\]

## 2. Exact audit of the known small paradoxical range

Rozier--Terracol prove that there are exactly 593 paradoxical sequences starting at integers `<=4614`, and that any additional paradoxical sequence must start above

\[
2.8\times10^{19}.
\]

A separate exact audit was performed on **every** integer

\[
2\le n\le4614
\]

using only integer comparisons. For each `n`, the first `k` for which

\[
3^{q_k}<2^k
\]

was computed and the endpoint `T^k(n)` was compared with `n`.

Result:

\[
\boxed{
\text{there is no }2\le n\le4614\text{ whose first coefficient crossing has }T^k(n)\ge n.
}
\]

The deepest first coefficient crossing in this finite audit occurs at

\[
\boxed{n=703,\quad k=81,\quad q_k=51,\quad T^k(n)=628.}
\]

Reproducibility script:

`collatz/src/r1_first_crossing_small_audit.py`.

Thus none of the 593 known small paradoxical sequences is paradoxical already at its **first** coefficient crossing.

Consequently any R1 renewal-floor counterexample is an additional paradoxical start and must satisfy

\[
\boxed{N>2.8\times10^{19}.}
\]

## 3. Non-convergent slope branch

Suppose the reduced rational `A/H` is not a continued-fraction convergent of `gamma`.

Legendre's theorem gives

\[
\left|\frac AH-\gamma\right|\ge\frac1{2H^2}.
\]

Since `A/H>gamma`,

\[
\delta:=A-H\gamma\ge\frac1{2H}.
\]

Therefore

\[
P-1=2^\delta-1
\ge
2^{1/(2H)}-1
>
\frac{\ln2}{2H}.
\]

The R1 ceiling then yields

\[
N<\frac{H}{3(P-1)}
<\frac{2H^2}{3\ln2}.
\]

Combining with `N>2.8e19` gives

\[
\boxed{
H>
\sqrt{\frac{3\ln2}{2}\,(2.8\times10^{19})}
\approx5.395570552\times10^9.
}
\]

Thus every non-convergent R1 branch needs more than about 5.395 billion odd events before its first coefficient crossing.

## 4. Convergent and finite-multiple branch

If the reduced fraction `A/H` is an upper continued-fraction convergent `p/q` of `gamma`, write

\[
A=sp,\qquad H=sq,
\]

with integer `s>=1`.

The nearest-upper-layer condition `A=ceil(H gamma)` forces

\[
0<s(p-q\gamma)<1.
\]

For the primitive convergent define

\[
\delta_q:=p-q\gamma>0.
\]

The universal ceiling on an allowed multiple is

\[
N<
\frac{sq}{3(2^{s\delta_q}-1)}.
\]

For fixed positive `delta_q`, the function

\[
s\mapsto\frac{s}{2^{s\delta_q}-1}
\]

is strictly decreasing. Hence every allowed multiple has ceiling no larger than the primitive `s=1` ceiling

\[
\boxed{
N<\frac{q}{3(2^{\delta_q}-1)}.
}
\]

The upper convergent denominators of `gamma=log_2 3` below the non-convergent threshold are

\[
1,5,41,306,15601,79335,190537,10781274,171928773,397573379.
\]

The largest corresponding primitive ceiling is attained at

\[
(A,H)=(630138897,397573379)
\]

and is approximately

\[
\boxed{1.2520795\times10^{18},}
\]

still far below `2.8e19`.

The next primitive upper convergent is

\[
\boxed{
(A,H)=(10439860591,6586818670),
}
\]

whose denominator already exceeds the non-convergent threshold `5.395570552e9`.

Therefore the convergent/multiple branch also has no R1 candidate below the same threshold.

## 5. Global R1 odd-event lower bound

Combining the two branches gives

\[
\boxed{
H>5.395570552\times10^9
}
\]

for every R1 renewal-floor counterexample.

This bound is independent of whether the first-crossing endpoint is odd or even.

For an even first-crossing endpoint the separate harmonic overload theorem is much stronger asymptotically:

\[
H>(170.33\ldots+o(1))N,
\]

but the present theorem applies uniformly to the full R1 branch.

## 6. Scope

This is not an exclusion theorem. It proves only that an R1 counterexample cannot appear at small or medium first-crossing depth.

Its architectural value is that R1 is now forced into an extreme Diophantine regime:

- start value above `2.8e19`;
- at least about `5.4e9` odd events before the first coefficient crossing;
- and if the ratio is cheaply resonant, it lies on a very high upper continued-fraction layer.

The remaining R1 task is still global: rule out an infinite-stopping-time renewal floor whose first coefficient crossing survives above its start at such extreme depth.