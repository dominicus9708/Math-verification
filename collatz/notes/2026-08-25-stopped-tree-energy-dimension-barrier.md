# Dimension barrier for the stopped-tree energy route

Date: 2026-08-25

Status: **proof-strategy barrier / negative control.**  The stopped-tree Haar identity remains exact and useful, but coefficient-survival Kraft decay by itself is not strong enough to make its sufficient energy criterion plausible under generic cross-base behavior.

## 1. Safe coefficient rate

The coefficient-surviving parity language has dyadic density exponent

\[
\delta_{\rm coeff}
=1-H_2(\log_3 2)
\approx0.05004447.
\]

Thus a horizon-`H` active Kraft mass has the safe upper bound

\[
K_H\le2^{-\delta_{\rm coeff}H+o(H)}.
\]

## 2. Selector dimension at the natural scale

The recursively sufficient ternary selector has `2^m` atoms spread over ordinary size about `3^m`.  In binary resolution this has dimension

\[
\boxed{d_C=\log_3 2\approx0.6309297536.}
\]

At its natural binary scale `H ~ m log_2 3`, an injective selector cylinder has mass about

\[
2^{-d_CH}.
\]

If the selector and the coefficient-survival language meet in the neutral/generic way suggested by the current finite same-integer calibration, the number of active selector atoms is of order

\[
2^{(d_C-\delta_{\rm coeff})H}.
\]

The corresponding active leaf energy is then

\[
E_H
\asymp
2^{(d_C-\delta_{\rm coeff})H}
\,2^{-2d_CH}
\,2^H
=
2^{(1-d_C-\delta_{\rm coeff})H}.
\]

Hence the generic energy exponent is

\[
\boxed{
e_{\rm generic}
=1-d_C-\delta_{\rm coeff}
\approx0.31902578.
}
\]

## 3. Why the sufficient criterion then fails

The stopped-tree Cauchy criterion would require

\[
e<\delta_{\rm coeff}\approx0.05004447.
\]

But generic/balanced behavior gives

\[
e_{\rm generic}\approx0.31902578
>\delta_{\rm coeff}.
\]

Thus merely localizing the global selector energy to a prefix-free open-excursion tree does not, by itself, solve the dimension mismatch.  It removes the artificial fixed-depth `sqrt(2^H)` loss but exposes the genuine singular-measure dimension cost of the ternary selector.

## 4. Agreement with the finite negative control

At depth 28 the exact same-integer selector survival fractions track the raw dyadic survival-language fractions extremely closely.  Therefore current evidence does not support the exceptional anti-correlation that would be required to lower the active energy exponent from about `0.319` to below `0.050`.

The very small finite split energy through depth 28 is consequently interpreted as a pre-natural-scale mixing effect, not evidence of an asymptotic zero energy exponent.  Indeed the exact recalculation already shows the cumulative split energy beginning to rise between depths 16 and 28.

## 5. Consequence

The stopped-tree identity is retained as a diagnostic and as a possible component of a stronger mixed-place theorem, but it is **not** promoted to the terminal route on coefficient survival alone.

A terminal argument still needs at least one genuinely stronger same-integer/minimality mechanism that changes the active-language dimension or produces arithmetic anti-correlation.  Safe candidates include:

- root-globalized backtrace/headroom exclusions;
- whole-prefix (root-level) alternate-predecessor/Hensel maximality;
- transported first-defect/root-translation constraints;
- or a new cross-place theorem coupling those conditions to the ternary selector.

Invalid arbitrary later-block L7 maximality is not reinstated.
