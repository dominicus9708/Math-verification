# Exact finite coefficient-survival profile inside the recursive-sufficiency core

Date: 2026-08-09

Status: **FINITE COMPUTATIONAL DIAGNOSTIC / NEGATIVE EVIDENCE FOR A TRIVIAL CORE-BIAS ROUTE**

This note profiles the coefficient stopping time inside the ternary 0/1 recursively sufficient core. It is not an asymptotic theorem and is not used as a proof ingredient.

## 1. Core family

At ternary depth `m`, use

\[
F_m=\left\{4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:a_i\in\{0,1\}\right\}.
\]

Every element is `3 mod 4`, so the first two accelerated parity bits are `OO`. This is also mandatory for every coefficient-surviving word of length at least two because

\[
a_1=1,\qquad a_2=2.
\]

Thus a fair first comparison with the unrestricted parity language is the ordinary survivor fraction multiplied by four (conditioning on the compulsory `OO` cylinder).

## 2. Exact exhaustive scans

The accompanying C++ verifier enumerates all `2^m` core elements in Gray-code order and computes coefficient stopping times with arbitrary-precision integer trajectories.

Selected exact results:

| m | total | max tau_c | tau>50 | tau>100 | tau>200 | tau>400 |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 65,536 | 192 | 857 | 67 | 0 | 0 |
| 17 | 131,072 | 243 | 1,680 | 119 | 2 | 0 |
| 18 | 262,144 | 195 | 3,482 | 229 | 0 | 0 |
| 19 | 524,288 | 257 | 6,841 | 501 | 11 | 0 |
| 20 | 1,048,576 | 265 | 14,014 | 999 | 10 | 0 |
| 21 | 2,097,152 | 265 | 27,847 | 2,050 | 30 | 0 |
| 22 | 4,194,304 | 317 | 55,735 | 4,080 | 52 | 0 |
| 23 | 8,388,608 | 351 | 111,407 | 8,024 | 106 | 0 |
| 24 | 16,777,216 | 386 | 222,182 | 16,001 | 216 | 0 |
| 25 | 33,554,432 | 340 | 445,023 | 32,312 | 397 | 0 |
| 26 | 67,108,864 | 428 | 889,669 | 63,975 | 842 | 1 |

The m=22 maximum reproduces the previously recorded value `M_F(22)=317`.

## 3. Survivor-density comparison

For the unrestricted coefficient-survivor parity language, exact count DP gives

\[
\frac{|P_{50}|}{2^{50}}\approx0.0033166890828795204,
\]

\[
\frac{|P_{100}|}{2^{100}}\approx0.00023867828362647393,
\]

\[
\frac{|P_{200}|}{2^{200}}\approx3.0604236615202414\times10^{-6}.
\]

Conditioning on the compulsory first two odd bits multiplies these fractions by four:

\[
0.01326675633151808,
\quad
0.0009547131345058957,
\quad
1.2241694646080966\times10^{-5}.
\]

At core depth m=26, the exact observed fractions are

\[
\frac{889669}{2^{26}}
\approx0.01325710117816925,
\]

\[
\frac{63975}{2^{26}}
\approx0.0009533017873764038,
\]

\[
\frac{842}{2^{26}}
\approx1.2546777725219727\times10^{-5}.
\]

They are close to the corresponding `OO`-conditioned unrestricted fractions. Similar stability is visible at m=20,22,24.

This is a finite observation only. It does **not** establish equidistribution, independence, or an asymptotic density theorem for the ternary core.

## 4. Interpretation

The recursive-sufficiency core is extremely useful because it restricts where a hypothetical minimal counterexample may lie. However, these finite data do not show an additional obvious coefficient-survival penalty beyond the forced initial `OO` parity.

Therefore a proof should not assume that the ternary 0/1 restriction by itself makes long coefficient-survival rare. The difficult object remains the deterministic cross-base relation between

- the ternary digit choices,
- the binary/canonical lift sequence,
- and the long coefficient barrier.

This supports keeping the cross-base carry/late-lift problem explicit rather than replacing it by a heuristic density argument.

## 5. Reproducibility

Reference implementation:

`collatz/src/recursive_core_survival_profile.cpp`

All counts above are exact finite computations. Runtime is not part of the mathematical claim.