# Exact ordered-one rigidity at the current m=44 R1 resonance

Date: 2026-08-13

Status: **derived theorem + exact rational certificate + independent high-precision Wolfram check**. The result gives a new global rigidity condition at the currently isolated first-crossing resonance. It does not eliminate the resonance and is not a proof of Collatz.

## 1. Current resonance and verified floor

Use the isolated first coefficient-crossing resonance

\[
\boxed{
(A,H)
=(217,976,794,617,
137,528,045,312).
}
\]

Put

\[
\beta:=\log_2 3,
\qquad
P:=\frac{2^A}{3^H}>1,
\qquad
\lambda:=\log P=A\ln2-H\ln3>0.
\]

The current recursive-sufficiency bootstrap has certified the continuous integer range through

\[
\boxed{
V_{32}=4(3^{44}+3^{32})+2.
}
\]

The first possible `m=44` core representative beyond this floor is

\[
\boxed{
N_{\min}=V_{32}+1
=4(3^{44}+3^{32})+3.
}
\]

## 2. Time-expanded boundary word

At a first coefficient crossing occurring at time `A`, the coefficient-surviving prefix before the crossing has length

\[
\boxed{L=A-1}
\]

and contains exactly

\[
\boxed{H}
\]

ones.

Let `d_ell` be the actual position of the `ell`-th one and `d_ell^star` its position in the mechanical Beatty/Christoffel boundary word. Previous work proved

\[
d_\ell\le d_\ell^\star,
\qquad
r_\ell:=d_\ell^\star-d_\ell\ge0.
\]

The exact real defect is

\[
E_\star-E
=
\sum_{\ell=1}^{H}
M_\ell(1-2^{-r_\ell}).
\]

For every displaced one, `r_ell>=1`, so the least cost at that ordered position is the one-step displacement cost.

## 3. Exact one-step displacement cost

Write

\[
\theta_n:=\{n\beta\},
\qquad n=0,\ldots,H-1.
\]

The mechanical position formula gives

\[
d_\ell^\star+1
=
\left\lfloor(\ell-1)\beta\right\rfloor+1.
\]

Using the phase collapse from the global ordered-one decomposition, the real cost of moving the `ell`-th one left by exactly one position is

\[
\boxed{
c_\ell
=
\frac1{3P}
2^{-\theta_{\ell-1}}.
}
\]

Any larger displacement costs at least this much.

## 4. Upper-convergent phase grid

The exact rational logarithm certificate proves

\[
0<\frac AH-\beta<\frac1{H^2}.
\]

Also

\[
\gcd(A,H)=1.
\]

For `1<=n<H`, write

\[
\left\{\frac{nA}{H}\right\}
=
\frac{j_n}{H},
\qquad
j_n\in\{1,\ldots,H-1\}.
\]

Because

\[
0<n\left(\frac AH-\beta\right)<\frac1H
\le\frac{j_n}{H},
\]

there is no circular wrap, and therefore

\[
\boxed{
\{n\beta\}
=
\frac{j_n}{H}
-n\left(\frac AH-\beta\right)
<
\frac{j_n}{H}.
}
\]

As `n` runs from `0` to `H-1`, the residues `j_n` are a permutation of

\[
0,1,\ldots,H-1.
\]

Hence the actual phase multiset is termwise no larger than the exact uniform `H`-grid under a permutation.

Since `2^{-x}` is decreasing, for any set of `m` displaced ordered ones, even the cheapest possible choice obeys

\[
\sum_{\ell\in D}c_\ell
\ge
\frac1{3P}
\sum_{j=H-m}^{H-1}2^{-j/H}.
\]

This is a deterministic order-statistic bound; no randomness or equidistribution assumption is used.

## 5. Integral lower bound for the cheapest m positions

The function `2^{-x}` is decreasing. Therefore the left Riemann sum gives

\[
\sum_{j=H-m}^{H-1}2^{-j/H}
\ge
H\int_{1-m/H}^{1}2^{-x}\,dx.
\]

Thus

\[
\boxed{
D_m
\ge
\frac{H}{6P\ln2}
\left(2^{m/H}-1\right),
}
\]

where `D_m` is the minimum real first-crossing defect forced by `m` displaced ordered ones.

This is the key global knapsack collapse: the minimum cost of an arbitrary `m`-element displacement set is controlled by one scalar function of `m/H`.

## 6. Safe upper bound on the available real defect budget

Let `c_chr` be the odd-only mechanical correction. Denjoy--Koksma gives

\[
\boxed{
c_{chr}\le
U:=\frac{H}{6\ln2}+\frac13.}
\]

For an R1 renewal candidate with start `N` and gap `g>=4`,

\[
c=(P-1)N+Pg.
\]

The corresponding time-expanded real defect is

\[
\mathcal D
=
\frac{c_{chr}-c}{P}.
\]

Therefore

\[
\mathcal D
\le
\frac UP
-(1-P^{-1})N
-4.
\]

Using

\[
U/P\le U
\]

and, for `lambda>0`,

\[
1-e^{-\lambda}
\ge
\frac{\lambda}{1+\lambda},
\]

we obtain the certified safe budget

\[
\boxed{
\mathcal D
\le
U
-N_{\min}
\frac{\lambda}{1+\lambda}
-4.
}
\]

The exact rational verifier uses a lower rational bound for `lambda` in the subtracted term and a lower rational bound for `ln 2` in `U`, so the resulting number is rigorously an upper bound.

It obtains

\[
\boxed{
\mathcal D
<29,528,621,489.509.
}
\]

The decimal is only for orientation; the comparison itself is made by exact rational cross multiplication.

## 7. Exact integer threshold

The verifier lower-bounds `1/P=e^{-lambda}` by `1-lambda_hi`, lower-bounds `2^{m/H}-1` by a 40-term positive Taylor series, and uses exact rational logarithm intervals.

For

\[
m=126,613,628,698,
\]

the certified lower bound is approximately

\[
29,528,621,489.252,
\]

which does not yet exceed the safe budget.

For the next integer

\[
\boxed{
m_0=126,613,628,699,}
\]

the certified lower bound is approximately

\[
\boxed{29,528,621,489.567,}
\]

which is strictly larger than the certified budget upper bound.

Therefore a current-resonance `m=44` candidate cannot have `m_0` displaced ordered ones.

Hence

\[
\boxed{
N_{\rm disp}
\le126,613,628,698.
}
\]

Since the boundary contains exactly `H` ordered ones,

\[
\boxed{
N_{\rm fixed}
\ge
H-126,613,628,698
=10,914,416,614.
}
\]

Equivalently,

\[
\boxed{
\frac{N_{\rm fixed}}H
\ge0.0793613883571\ldots
}
\]

or

\[
\boxed{
\text{at least }7.9361388357\%\text{ of ordered ones remain exactly mechanical.}
}
\]

## 8. What this means

This is not the same statistic as the earlier positive-skew/defect-location density.

The present theorem concerns **ordered one positions themselves**. At least 10.9 billion of the `H` ones must occur at exactly the same positions as in the mechanical Christoffel envelope.

Thus any surviving candidate simultaneously has to satisfy:

1. very long coefficient survival;
2. the `m=44` ternary recursive-core address;
3. the strong dyadic renewal address;
4. the 3-adic smaller-predecessor restrictions;
5. and now a global exact-position rigidity condition fixing at least `7.936%` of all ordered ones.

The free part is still enormous, so this does not close the resonance by itself. Its value is that the real defect budget has now been converted into a **hard combinatorial rigidity constraint** rather than only a weighted average defect bound.

## 9. Reproducibility and independent check

`collatz/src/m44_ordered_one_displacement_budget_certificate.py` uses only Python integers and `fractions.Fraction` for the proof comparisons. It constructs neither `2^A` nor `3^H`.

It certifies:

- exact rational intervals for `ln2` and `ln3`;
- `lambda>0`;
- the upper-convergent no-wrap inequality;
- the safe real-defect budget;
- the lower defect at `m_0-1` and `m_0`;
- the exact integer threshold above.

An independent 80-digit Wolfram calculation of the unrelaxed equations gives the continuous crossing

\[
m_*=126,613,628,698.7158\ldots,
\]

consistent with the rational threshold.

## 10. Next target

The next useful step is not to improve `7.936%` by a small numerical amount. The new rigidity should be combined with the valuation-graded dyadic address decomposition

\[
r(w)-r_\star
\equiv
\sum_{\ell:r_\ell>0}
2^{d_\ell}(2^{r_\ell}-1)3^{-\ell}
\pmod{2^L}.
\]

The ordered ones that remain fixed contribute no dyadic defect term. Therefore the real budget now limits the support size of the dyadic defect hierarchy to at most

\[
126,613,628,698
\]

valuation levels.

The remaining goal is to show that the `m=44` ternary start address / strong renewal address requires more or incompatible valuation levels, or that the sparse displacement pattern forces one of the 3-adic predecessor prohibitions.
