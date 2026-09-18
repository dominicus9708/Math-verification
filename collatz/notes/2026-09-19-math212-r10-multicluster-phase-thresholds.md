# MATH-212 — multi-cluster r=10 phase-summed surplus thresholds

Date: 2026-09-19

Status: \`EXACT COMMON-CLOCK SHARPENING / MULTI-CLUSTER BIT-COST GROWTH / r=10 OPEN\`

## 1. Purpose

MATH-202 takes the infimum of the r=10 paid-cluster surplus one cluster at a time and obtains

\[
r=10\text{ danger}\Longrightarrow z\ge13.
\]

That bound treats every cluster as if it could independently start at the unique worst phase.

MATH-207 proves that successive r=10 clusters are not independent. In log-phase coordinate they advance by the same irrational rotation.

This note takes the infimum over an entire n-cluster phase orbit at once.

No AP/source/depth enumeration is used.

## 2. One-cluster lower surplus

Let

\[
\lambda=\frac{19}{503},
\qquad
\theta=\log_2(3/2),
\]

and let \(\varpi\in(1/2,1]\) be the normalized paid-cluster entry phase.

For \(j=0,\ldots,9\), MATH-202 gives exact future phases

\[
\varpi_j
=
\varpi
\frac{
2^{j+m(j)+\mathbf1_{\{\varpi\le\tau_j\}}}
}{
3^j
},
\]

with

\[
m(j)=\lfloor j\theta\rfloor.
\]

The exact lower bound used in MATH-202 is

\[
\boxed{
e_{10}(\varpi)
=
\frac16\sum_{j=0}^{9}\varpi_j
-
\lambda h_{10}(\varpi).
}
\]

The cluster exit phase is

\[
\boxed{
F(\varpi)
=
\varpi
\frac{
2^{10+m(10)+\mathbf1_{\{\varpi\le\tau_{10}\}}}
}{
3^{10}
}.
}
\]

## 3. n-cluster common-clock bound

Define

\[
\varpi_{i+1}=F(\varpi_i)
\]

and

\[
\boxed{
E_n(\varpi_0)
=
\sum_{i=0}^{n-1}e_{10}(\varpi_i).
}
\]

Then define the exact orbitwise infimum

\[
\boxed{
\underline E_n
=
\inf_{\varpi_0\in(1/2,1]}E_n(\varpi_0).
}
\]

If a sequence of \(n\) consecutive r=10 boundary transfers has singleton overshoot depths

\[
z_1,\ldots,z_n
\]

and the cumulative Bellman transfer is nonpositive, then

\[
0
\ge
\sum_i \Delta\mathcal B_i
\ge
\underline E_n
-
\lambda\sum_i z_i.
\]

Therefore

\[
\boxed{
\sum_{i=1}^n z_i
\ge
Z_{\min}^{(10)}(n)
:=
\left\lceil
\frac{\underline E_n}{\lambda}
\right\rceil.
}
\]

This is stronger than adding the one-cluster bound \(13n\) whenever the common phase orbit forbids repeated worst-phase alignment.

## 4. Exact finite evaluation without r/depth loops

For fixed n, pull back the ten r=10 phase cuts through the deterministic map \(F\).

On each resulting initial-phase cell:

- every indicator is constant;
- every intermediate phase is a rational multiple of the initial \(\varpi_0\);
- every \(h_{10}\) is constant;
- \(E_n(\varpi_0)\) is an increasing affine function of \(\varpi_0\).

Hence its infimum is attained as a left-cell limit or at an exact pulled-back cut point.

The number of open cells is only

\[
\boxed{10n+1}.
\]

Thus this is one common-clock calculation, not an enumeration of parity words, AP sources, depths, or separate paid-count layers.

## 5. Exact thresholds

The exact certificate gives:

| consecutive r=10 clusters n | one-orbit minimum required total overshoot bits |
|---:|---:|
| 1 | 13 |
| 2 | 27 |
| 3 | 42 |
| 4 | 57 |
| 5 | 72 |
| 6 | 87 |
| 7 | 102 |
| 8 | 117 |
| 9 | 131 |
| 10 | 147 |
| 11 | 161 |
| 12 | 176 |
| 13 | 191 |
| 14 | 206 |
| 15 | 221 |
| 16 | 236 |
| 17 | 250 |
| 18 | 265 |
| 19 | 280 |
| 20 | 297 |

The first two exact lower bounds are

\[
\boxed{
\underline E_1
=
\frac{45390185}{93871872}
}
\]

and

\[
\boxed{
\underline E_2
=
\frac{6212454542993}{6151987003392}.
}
\]

Therefore

\[
\frac{\underline E_2}{\lambda}
=
\frac{6212454542993}{232381218816}
\approx26.7349,
\]

so

\[
\boxed{
\text{two consecutive dangerous r=10 transfers}
\Longrightarrow
z_1+z_2\ge27.
}
\]

In particular, the naive independent lower bound \(13+13=26\) is impossible.

Likewise,

\[
\boxed{
z_1+z_2+z_3\ge42,
}
\]

and five consecutive dangerous transfers require

\[
\boxed{
\sum_{i=1}^{5}z_i\ge72.
}
\]

## 6. Interpretation in the carry/address channel

MATH-204/205 show that every compatible singleton overshoot divides out exactly the forced power \(2^{z_i}\) from the address discrepancy and transports only the quotient carry.

Thus MATH-212 converts the common phase dynamics into a cumulative exact address-information obligation:

\[
\boxed{
n\text{ dangerous r=10 transfers}
\Longrightarrow
\text{at least }Z_{\min}^{(10)}(n)
\text{ forced dyadic carry bits in total}.
}
\]

The important point is that the bit cost grows faster than the independent estimate \(13n\) over many finite prefixes.

## 7. Why this does not yet close r=10

A large required valuation is not itself a contradiction for an ordinary integer trajectory.

The remaining task is to bound or quotient the **regeneration** of low carry bits after each shift-add transition

\[
d'
=
\frac{3^Qd+c}{2^z}.
\]

The correct next target is therefore a combined potential/finite quotient that tracks:

1. the phase-orbit surplus credit from MATH-212;
2. the quotient carry residue needed for the next resonance;
3. Hensel/Pareto extremality from MATH-210.

No new AP or depth enumeration is required.

## 8. Claim boundary

Established:

- exact n-cluster common-phase lower surplus;
- exact total overshoot thresholds through n=20;
- strict improvement over independent 13-bit accounting;
- 2-cluster threshold 27, 3-cluster threshold 42, 5-cluster threshold 72;
- only 10n+1 phase cells are required.

Not established:

- impossibility of every carry sequence satisfying these growing bit obligations;
- r=10 closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
