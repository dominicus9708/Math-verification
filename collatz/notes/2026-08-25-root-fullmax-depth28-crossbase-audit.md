# Full root-Hensel maximality through depth 28: cross-base audit

Date: 2026-08-25

Status: **exact finite nested-root computation + same-integer ternary cross-base negative control.**  This note does not prove the Collatz conjecture and does not claim asymptotic independence.

## 1. Question tested

The previous root credit-1 certificate established a globally safe minimal-counterexample filter, but at `H=28` its conditional survival fraction was essentially unchanged by the current ternary selector.

The next question was whether the *additional* part of full root-Hensel maximality — siblings with credits `Delta > 1` — supplies any detectable ternary-dyadic transversality.

For every length-`k` root prefix with `q` odd entries,

\[
T^k(N)=\frac{3^qN+R}{2^k}.
\]

The full-Hensel class is

\[
(q,\;R\bmod 3^q).
\]

A root prefix is maximal when its correction `R` is the largest correction among **all** length-`k`, weight-`q` parity words in that class.

The nested language used here requires, for every prefix `1 <= k <= 28`, both

1. coefficient survival `3^{q_k} >= 2^k` for the tested candidate;
2. full-Hensel maximality of its correction at that depth.

## 2. Audit-critical implementation detail

The competitor word defining the maximum is **not** restricted to the coefficient-surviving language.

That restriction would be invalid: an alternate smaller start `N-Delta` may have an actual parity prefix that fails the candidate's coefficient-survival condition and can still merge with the original trajectory.

Accordingly, at each depth `k` the certificate first identifies the Hensel classes reached by coefficient-surviving candidates and then scans every length-`k` parity word with a compatible final odd count `q`, regardless of its earlier coefficient history, to obtain the true class maximum.

Certificate:

`collatz/src/root_fullmax_depth28_crossbase_certificate.cpp`

## 3. Nested full-max counts

The exact survivor counts through depth 28 are

\[
\begin{array}{c|rrrrrrrrrrrrrr}
k&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\\hline
N_k&1&1&2&3&4&7&11&16&31&52&103&182&297&593
\end{array}
\]

and

\[
\begin{array}{c|rrrrrrrrrrrrrr}
k&15&16&17&18&19&20&21&22&23&24&25&26&27&28\\\hline
N_k&1049&1720&3439&6104&12194&22244&38019&75969&137657&234156&467895&847493&1442349&2882872.
\end{array}
\]

The values through `H=22` reproduce the previously recorded independent regression exactly.

At `H=28`:

- coefficient-surviving language: `3,524,586`;
- root credit-1 surviving language: `2,890,278`;
- nested full root-Hensel maximal language: `2,882,872`.

Thus credits greater than one remove only

\[
2,890,278-2,882,872=\boxed{7,406}
\]

additional prefixes beyond credit-1 avoidance.

Conditioned on credit-1 survival, the full-max survival fraction is

\[
\boxed{
\frac{2,882,872}{2,890,278}
=0.9974376167275\ldots
}
\]

so the additional rejection fraction is approximately

\[
0.00256238327247\approx0.256238\%.
\]

As an independent inclusion audit, every one of the `2,882,872` full-max survivors passes the adjacent-start credit-1 avoidance test.

## 4. Same-integer m=44 cross-base intersection

The previous credit-1 certificate gave, for the current `m=44` selector layer after subtracting the low-33 part,

\[
757,298,661,081
\]

credit-1 surviving weighted residues.

Adding nested full root-Hensel maximality leaves

\[
\boxed{755,358,097,347}.
\]

Thus the extra full-max survival fraction conditioned on credit-1 is

\[
\boxed{
\frac{755,358,097,347}{757,298,661,081}
=0.9974375185990\ldots
}
\]

Compared with the ambient factor `0.9974376167275...`, the relative shift is only about

\[
-0.0984\ \text{ppm}.
\]

The extra credit-`>1` condition therefore behaves essentially neutrally on this selector layer.

## 5. Two unresolved m=45 affine blocks

The previous credit-1 weighted count for the two blocks together was

\[
1,515,337,963,334.
\]

Nested full root-Hensel maximality leaves

\[
\boxed{1,511,455,084,633}.
\]

The conditional factor is

\[
\boxed{
\frac{1,511,455,084,633}{1,515,337,963,334}
=0.9974376153736\ldots
}
\]

which differs from the ambient factor by only about

\[
-0.00136\ \text{ppm}.
\]

This is even closer to exact neutrality than the `m=44` diagnostic.

## 6. Interpretation

The audit supports three conclusions.

1. **Full root-Hensel maximality remains valid and useful as a globally safe finite sieve.**  The computation does not weaken the root-minimality theorem.
2. **The part beyond credit-1 is quantitatively small through H=28.**  It removes 7,406 additional coefficient-language prefixes, about 0.256% of the credit-1 survivors.
3. **That additional removal does not display the missing cross-base transversality.**  Its survival factor on the m=44 and m=45 ternary selector layers agrees with the ambient factor to sub-ppm accuracy.

Therefore the immediate proof program should **not** spend its main effort extrapolating the root-max finite entropy rate or expecting credits `>1` alone to close the ternary-dyadic bottleneck.

The full root-max condition should instead be retained as a free, globally safe auxiliary sieve while the search returns to mechanisms that can correlate the binary root language with the ternary selector non-neutrally.

## 7. Reproducibility checks embedded in the certificate

The certificate aborts unless all of the following hold:

- the old nested-root counts through `H=22` are reproduced exactly;
- the new counts through `H=28` equal the values recorded above;
- the coefficient language at `H=28` contains exactly `3,524,586` residues;
- every full-max survivor independently avoids a root credit-1 merger;
- canonical residues remain unique under the parity-vector bijection;
- the exact m=44 and m=45 weighted intersection totals equal the recorded integers.

A local optimized run completed with `PASS` and produced the exact totals recorded in this note.
