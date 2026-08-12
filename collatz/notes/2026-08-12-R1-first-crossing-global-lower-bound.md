# R1 first-crossing global lower bound

Date: 2026-08-12

Status: **exact structural reduction + finite audit + external verified Collatz frontier**, plus a stronger high-precision one-sided continued-fraction audit. The exact analytic lower bound is `H>4.9547666543e10`; the stronger `H>=72057431991` value is a reproducible high-precision finite arithmetic audit and should be interval-certified before publication as a formal theorem. This note does not exclude R1.

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

## 2. Small paradoxical audit

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

Thus none of the known small paradoxical sequences is already paradoxical at its **first** coefficient crossing.

This implies the useful finite bound

\[
N>2.8\times10^{19}
\]

for any R1 start, but an actual Collatz counterexample admits a still stronger bound from the verified convergence frontier below.

## 3. Verified Collatz frontier for an actual counterexample

Barina's 2025 verification establishes convergence for every positive start below

\[
\boxed{2^{71}.}
\]

If a hypothetical nonperiodic counterexample orbit ever entered this verified range, its remaining tail would converge and therefore the original orbit would also converge. Hence every renewal floor on a genuine counterexample must satisfy

\[
\boxed{N\ge2^{71}.}
\]

This is stronger than the paradoxical-start lower bound `2.8e19` and is the bound used below.

## 4. Universal one-sided slope strip

From

\[
(P-1)N<\frac H3
\]

and `N>=2^71`,

\[
P-1<\frac{H}{3\,2^{71}}.
\]

Let

\[
\varepsilon:=\frac AH-\gamma>0.
\]

Since

\[
P=2^{H\varepsilon},
\]

and `log(1+x)<x`,

\[
H\varepsilon
=\log_2P
<\frac{P-1}{\ln2}
<\frac{H}{3\,2^{71}\ln2}.
\]

Therefore every R1 counterexample satisfies the **H-independent** upper-approximation strip

\[
\boxed{
0<\frac AH-\log_2 3
<
\frac{1}{3\,2^{71}\ln2}
\approx2.03668372079\times10^{-22}.
}
\]

This is stronger and cleaner than treating the convergent and non-convergent sectors separately at the outset.

## 5. Exact analytic Legendre lower bound

Suppose the reduced rational `A/H` is not a continued-fraction convergent of `gamma`.

Legendre's theorem gives

\[
\left|\frac AH-\gamma\right|\ge\frac1{2H^2}.
\]

Combining with the strip above yields

\[
H>
\sqrt{\frac{3\ln2}{2}\,2^{71}}
\approx
\boxed{4.9547666543\times10^{10}}.
\]

This part is an exact analytic theorem once the `2^71` external verification input is accepted.

If `A/H` reduces to a convergent `p/q` with `A=sp`, `H=sq`, the nearest-upper-layer condition forces `0<s(p-q gamma)<1`; for fixed primitive convergent the universal ceiling decreases with `s`. Auditing the primitive upper convergents below the Legendre threshold shows their ceilings are all below `2^71`, so the convergent/multiple sector does not evade the same exact threshold.

## 6. Stronger one-sided continued-fraction audit

The fixed strip from Section 4 permits a direct one-sided best-approximation audit, including both convergents and intermediate/semiconvergents.

Using 120-digit arithmetic, the first upper convergent or semiconvergent found with

\[
0<\frac AH-\gamma
<\frac{1}{3\,2^{71}\ln2}
\]

is

\[
\boxed{
(A,H)=
(114208327604,\ 72057431991).
}
\]

Its approximation error is

\[
\frac AH-\gamma
\approx
1.10336069332\times10^{-22},
\]

which lies safely inside the required strip.

The previous upper best approximants remain outside the strip. Standard continued-fraction theory says any new record one-sided approximation appears among convergents or intermediate convergents, so this audit gives the stronger numerical threshold

\[
\boxed{H\ge72057431991.}
\]

Reproducibility script:

`collatz/src/r1_one_sided_cf_threshold_audit.py`.

### Certification status

The script uses high-precision `mpmath` rather than directed rational interval arithmetic. The numerical margins are large, but for a publication-grade **formal** theorem the continued-fraction comparisons for `log_2 3` should be repeated with certified upper/lower rational enclosures for `ln 2` and `ln 3`.

Therefore the rigorous architecture should currently distinguish:

\[
\boxed{
H>4.9547666543\times10^{10}
\quad\text{(exact analytic / certified inputs)}
}
\]

from

\[
\boxed{
H\ge72057431991
\quad\text{(stronger reproducible high-precision audit)}.
}
\]

## 7. Endpoint-overshoot strengthening

The signed-skew first-passage formulation defines the overshoot

\[
o=-1-s_H\ge0.
\]

If `o=0`, the first coefficient crossing occurs exactly at the next odd endpoint.

If `o>=1`, the crossing occurs inside the final halving run. The general harmonic overshoot theorem gives

\[
\boxed{
H>
\frac{
2^{9o}(N+1)e^{-3/N-3/(N+1)}-N+5
}{3}.
}
\]

Thus for large `N`,

\[
H>
\left(\frac{2^{9o}-1}{3}+o(1)\right)N.
\]

For the first even-endpoint case `o=1`, this is approximately

\[
H>170.33N.
\]

Since an actual counterexample has `N>=2^71`, this sector begins on the scale

\[
H\gtrsim4.0\times10^{23}.
\]

## 8. Scope

This is not an exclusion theorem. It proves that an R1 counterexample is forced into an extreme one-sided Diophantine regime.

The exact analytic bound already requires roughly fifty billion odd events before the first coefficient crossing; the high-precision one-sided CF audit raises the first admissible denominator to roughly seventy-two billion.

The remaining R1 problem is the ordinary-integer formation/naturalness constraint: whether any such extreme first-passage skew word can be generated by a renewal floor of an actual divergent positive-integer orbit.