# Selector sparse middle-band diagnostic

Date: 2026-08-20

Status: **exact finite diagnostic separating the already-closed coarse and atomic regimes from the unresolved incomplete-orbit middle band.** This is not a proof of the Collatz conjecture.

## 1. Three selector-collision regimes

For

\[
e_r(m)=2p_{r+1}(m)-p_r(m),
\]

the exact full-orbit recurrence closes the coarse dyadic range whenever

\[
2^{r-1}\le m.
\]

At the opposite extreme, if

\[
2^r>\frac{3^m-1}{2},
\]

then the difference variable

\[
Z=A-B
\]

cannot equal any nonzero multiple of `2^r`. Hence

\[
p_r(m)=2^{-m},
\qquad
p_{r+1}(m)=2^{-m},
\]

and therefore

\[
\boxed{e_r(m)=2^{-m}.}
\]

Thus the selector-only collision problem is exactly reduced to the incomplete-orbit middle band

\[
\boxed{
m<2^{r-1}\ \text{ and }\ 2^r\le(3^m-1)/2.}
\]

## 2. Minimum balanced weights for m=44

Write

\[
Z=\sum_{i=0}^{43}\varepsilon_i3^i,
\qquad\varepsilon_i\in\{-1,0,1\}.
\]

For the collision refinement at level r, distinguish

- even-j class: nonzero `Z` congruent to `0 mod 2^(r+1)`;
- odd-j class: `Z` congruent to `2^r mod 2^(r+1)`.

Exact min-plus computation gives

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
r&7&8&9&10&11&12&13&14&15&16&17&18&19&20&21&22\\\hline
w_{\min}^{\rm even}&4&4&4&4&4&4&4&4&4&4&6&6&6&6&6&6\\
w_{\min}^{\rm odd}&2&4&4&4&4&4&4&4&4&4&4&6&6&6&6&6
\end{array}
\]

Weight one is impossible. Weight two disappears completely from both classes by r=18.

The weight-two disappearance is consistent with the exact LTE formula. For distinct powers,

\[
v_2(3^a-3^b)=2+v_2(a-b)
\]

when `a-b` is even, while the plus case has only small 2-adic valuation. Therefore a weight-two multiple of `2^r` requires a correspondingly large power-of-two divisor in an exponent gap; this becomes impossible once the required gap exceeds `m-1`.

## 3. Exact weight-six counts

Using an exact `3+3` meet-in-the-middle enumeration with disjoint ternary positions, the number of weight-six representations in the two collision classes is

\[
\begin{array}{c|rr}
r&N_6^{\rm even}&N_6^{\rm odd}\\\hline
18&1518&1984\\
19&950&568\\
20&402&548\\
21&172&230\\
22&94&78
\end{array}
\]

At r=22 the first nonzero layer contributes

\[
2^{-44}(94-78)2^{-6}
=\boxed{2^{-46}}
\]

to `e_22(44)`.

The exact full collision energy is

\[
\boxed{
e_{22}(44)
=\frac{6738940295698}{2^{88}}
\approx2.17746904756\times10^{-14}.
}
\]

Thus the weight-six layer accounts for approximately 65.26 percent of the final positive value at this one depth.

## 4. Important negative result: low weight alone is not a bound

The weight-six layer cannot be bounded independently and then summed by absolute value. For example at r=18 its signed contribution is

\[
(1518-1984)2^{-50}\approx-4.1389\times10^{-13},
\]

whereas the exact total energy is only

\[
e_{18}(44)\approx4.91994\times10^{-15}.
\]

The low-weight layer is therefore about -84 times the final total and is cancelled by higher balanced-weight layers.

Hence the sparse middle-band proof must retain **inter-weight signed cancellation**. Counting only the number of low-weight dyadic multiples is insufficient.

## 5. Exact m=44 atomic-scale ratios

For r=7,...,22, exact selector histograms give the ratios

\[
\frac{e_r(44)}{2^{-44}}
\]

approximately

\[
\begin{array}{c|rrrrrrrr}
r&7&8&9&10&11&12&13&14\\\hline
&6.58\!\times10^{-7}&7.02\!\times10^{-4}&0.00121&0.000419&0.00216&0.00909&0.01833&0.09944
\end{array}
\]

and

\[
\begin{array}{c|rrrrrrrr}
r&15&16&17&18&19&20&21&22\\\hline
&0.05458&0.53235&0.30504&0.08655&0.73910&0.14998&0.39140&0.38306.
\end{array}
\]

The maximum in this checked range is approximately 0.73910 at r=19. Thus the finite data are compatible with an atomic-scale bound

\[
e_r(m)=O(2^{-m}),
\]

but no uniform theorem is claimed here.

## 6. Candidate bound and current status

Small exact scans also support, but do not prove, a collision bound of the form

\[
p_r(m)\le2^{-r}+C2^{-m}
\]

with a small absolute constant. A trial value `C=17/16` survived the checked small grid, with the worst observed normalized excess about 1.04150.

If such a theorem held, the refinement identity would immediately imply

\[
e_r(m)\le2C\,2^{-m}.
\]

This would give an orientation-free bulk Cauchy estimate for the Stage-4 mass-transport term.

The remaining task is to prove such a bound, or else bypass selector-only collision control by using the Beatty-boundary orientation simultaneously.

## 7. Revised middle-band target

Because low balanced-weight layers can be much larger than the final energy, the next target is not a sparse-count theorem alone. It is one of:

1. a signed balanced-ternary carry/transfer theorem controlling
   \[
   \sum_j(-1)^j2^{-w_{\rm bal}(j2^r)};
   \]
2. a direct collision bound `p_r <= 2^-r + C 2^-m`;
3. a mixed selector-boundary spectral estimate that uses the fact that large selector and large Beatty-boundary Fourier coefficients appear on complementary frequencies.

The third route is the most directly matched to the actual Stage-4 correlation term `K`.
