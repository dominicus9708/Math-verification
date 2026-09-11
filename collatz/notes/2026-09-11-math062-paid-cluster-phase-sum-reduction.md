# MATH-062 — exact paid-cluster phase-sum reduction

Date: 2026-09-11
Status: `EXACT PHASE-SUM LOWER BOUND / MULTI-PAID RANGE REDUCED TO r<=64 / GLOBAL BELLMAN BOUND OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- The MATH-060 target slope remains

\[
\lambda_* = \frac{19}{503}.
\]

## 1. Why the old per-event bound is loose

MATH-058 used only

\[
p(q,u)=\frac{(1-2^{-u})\Omega_q}{3}>\frac1{12}
\]

for every positive-slack odd event.  For a multi-paid cluster with `r` paid odd events and length at most

\[
73+2r,
\]

this crude estimate makes only very large `r` automatically safe.

However successive paid odd events in one cluster advance `q` consecutively.  Intervening even steps do not change `q` or the mechanical phase coordinate.  Therefore the paid-event phases are not independent worst cases: they form one consecutive orbit of the exact phase map.

## 2. Exact phase dynamics

For

\[
\Omega\in(1/2,1),
\]

the next odd-count phase is

\[
\Omega'=
\begin{cases}
\frac23\Omega,&\Omega>\frac34,\\[1mm]
\frac43\Omega,&\Omega<\frac34.
\end{cases}
\]

At every paid odd, `u>=1`, hence

\[
1-2^{-u}\ge\frac12.
\]

Therefore a cluster with paid-event phases

\[
\Omega_0,\ldots,\Omega_{r-1}
\]

satisfies

\[
\boxed{
\mathcal P_{\rm cluster}
\ge
\frac16\sum_{j=0}^{r-1}\Omega_j.
}
\]

This remains valid even if even steps occur between the paid odd events.

## 3. Exact minimization of the consecutive phase sum

For fixed `r`, partition the complete source interval `(1/2,1)` at the exact rational phase thresholds.  On every partition cell the whole epsilon word is fixed and

\[
\sum_{j=0}^{r-1}\Omega_j=A_I\Omega_0
\]

for one exact positive rational `A_I`.

Hence the infimum on that cell is obtained at its lower endpoint, and the global infimum is a finite exact rational minimum over the phase cells.

No ordinary Collatz starts or endpoint lifts are enumerated in this calculation.

## 4. Target-slope comparison

MATH-058 gives, for an internal multi-paid macro with `r>=2`,

\[
\ell\le73+2r.
\]

Therefore the sufficient edgewise condition at the MATH-060 target is

\[
\frac16
\inf_{\Omega_0}
\sum_{j=0}^{r-1}\Omega_j
\ge
\frac{19}{503}(73+2r).
\]

The exact phase partition gives:

- for every `2<=r<=64`, this inequality is not yet forced by phase information alone;
- for every `65<=r<=127`, it is strictly true;
- the smallest margin in this exact transition range occurs at

\[
\boxed{r=65}.
\]

Its exact positive margin is

\[
\boxed{
\frac{1274361128696688015500375548948475}
{20682482655386529667021920924598272}
}
\approx0.06161548.
\]

Thus every multi-paid cluster with `65<=r<=127` is individually nonnegative for the `19/503` Bellman-adjusted cost before any potential term is used.

## 5. Elementary large-r closure

The exact phase map also gives a simple uniform pair bound.

If `Omega>3/4`,

\[
\Omega+\Omega'
=\frac53\Omega
>\frac54
>\frac76.
\]

If `Omega<3/4`,

\[
\Omega+\Omega'
=\frac73\Omega
>\frac76.
\]

Therefore every consecutive pair satisfies

\[
\boxed{\Omega_j+\Omega_{j+1}>\frac76}.
\]

Hence

\[
\sum_{j<r}\Omega_j
>
\begin{cases}
\dfrac{7r}{12},&r\text{ even},\\[2mm]
\dfrac{7r-1}{12},&r\text{ odd}.
\end{cases}
\]

After the factor `1/6` in the paid-cluster penalty, the exact adjusted margins at the two starting parities are

\[
\boxed{
r=128:\quad \frac{77}{4527}>0,
}
\]

\[
\boxed{
r=129:\quad \frac{449}{18108}>0.
}
\]

Increasing `r` by two adds at least

\[
\frac7{36}
\]

to the penalty lower bound while the target rises by only

\[
4\cdot\frac{19}{503}.
\]

Since

\[
\frac7{36}-\frac{76}{503}>0,
\]

the pair bound closes every `r>=128`.

## 6. Main reduction

Combining Sections 4 and 5,

\[
\boxed{
r\ge65
\Longrightarrow
\mathcal P_{\rm cluster}
-\frac{19}{503}\ell
>0.
}
\]

Therefore the weighted macro graph no longer needs detailed internal treatment of arbitrarily large paid clusters.

The only multi-paid cluster counts that can still contribute a negative adjusted edge are

\[
\boxed{2\le r\le64.}
\]

Together with MATH-061, the remaining Bellman problem is now finite in two previously unbounded directions:

1. a one-paid symbolic concatenation reaches ordinary-source resolution once its accumulated dyadic length reaches 73 bits;
2. a single multi-paid cluster needs detailed treatment only through 64 paid events.

## 7. DSD audit

### SAFE

- paid events in one cluster use consecutive odd-count phases;
- `u>=1` gives the exact lower factor `1/6` on each phase value;
- phase-sum minimization is a finite rational partition calculation;
- the exact threshold `r=65` for automatic `19/503` safety;
- the two-phase lower bound closes all `r>=128` analytically.

### OPEN

- the detailed macro relations for `2<=r<=64`;
- mixed composition with one-paid cylinders;
- a complete Bellman potential / minimum-mean obstruction for the remaining aperiodic graph;
- first-cell emptiness.

### PROHIBITED UPGRADES

- `r>=65` safety `=>` all multi-paid clusters safe;
- finite phase-sum optimization `=>` same-integer endpoint compatibility;
- removal of large-r edges `=>` first-cell closure.

## 8. Next target

Generate only the exact multi-paid macro cylinders with

\[
2\le r\le64
\]

and compose them with the MATH-061 one-paid cylinder states.  Edges with `r>=65` may be retained only as already-nonnegative Bellman transitions; their internal endpoint branching no longer needs to be resolved unless required for connectivity.

## Reproducibility

`collatz/src/2026_09_11_math062_paid_cluster_phase_sum_certificate.py`
