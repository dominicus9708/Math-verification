# Exact hybrid closure of the shifted m=44 `a_32=1` layer

Date: 2026-08-14

Status: **exact finite class certificate + exact first-descent certificate + recursively-sufficient interval bootstrap**.  This closes one complete `2^32` ternary-selector layer above the previous `V_32` floor.  It advances the finite verified interval but does not prove the Collatz conjecture.

## 1. Previously certified floor

The earlier bootstrap certified

\[
\boxed{
V_{32}=4(3^{44}+3^{32})+2.
}
\]

The first unverified member of Ansari's recursively-sufficient Cantor core in the next block is

\[
\boxed{
N_{\min}=V_{32}+1
=4(3^{44}+3^{32})+3.
}
\]

The shifted layer considered here is

\[
\boxed{
\mathcal A_{32}^{\rm shift}
=
\left\{
N_{\min}+4\sum_{i=0}^{31}a_i3^i:
 a_i\in\{0,1\}
\right\}.
}
\]

It has exactly

\[
\boxed{|\mathcal A_{32}^{\rm shift}|=2^{32}=4,294,967,296}
\]

representatives.

## 2. Depth-27 binary hard-core certificate

Use the exact binary alternate-predecessor integerization theorem together with the large-start Hensel sibling-max / tail-max reduction.

At time depth

\[
\boxed{L=27}
\]

the coefficient-surviving `OO` parity language contains

\[
1,762,293
\]

words.  The Hensel integerization sieve removes

\[
700,783,
\]

leaving

\[
\boxed{1,061,510}
\]

retained canonical residues modulo `2^27`.

These residues are generated once and stored locally as a 16 MiB bitset.  The bitset is a reproducible intermediate artifact generated from source; it is not required to be committed to the repository.

For the current start floor,

\[
N_{\min}>2^{2L-1},
\]

so the canonical tail-max replacement of partial-integerization witnesses is safe: once the denominator-clearing prefix is multiplicatively contracting, the finite additive term cannot overturn `m<N`.

## 3. Hybrid certification rule

For every `N` in the shifted ternary layer:

1. compute `N mod 2^27`;
2. if this residue is absent from the retained bitset, the whole dyadic cylinder is excluded by the exact Hensel alternate-predecessor theorem;
3. otherwise iterate the accelerated Collatz map with exact unsigned 128-bit integer arithmetic until the trajectory first falls below its own start.

A retained representative is therefore certified recursive by an explicit first-descent witness; an excluded representative is certified recursive by the class theorem.

No floating-point arithmetic is used in either branch.

## 4. Independent 16-chunk partition

The full `2^32` layer was partitioned by Gray-code selector index into sixteen disjoint chunks of size

\[
2^{28}=268,435,456.
\]

The exact chunk results are:

\[
\boxed{
\begin{array}{c|r|r|r|r}
\text{chunk}&\text{class removed}&\text{trajectory fringe}&\text{failures}&\max\tau_<\\\hline
0&259,947,187&8,488,269&0&444\\
1&259,940,679&8,494,777&0&470\\
2&259,939,506&8,495,950&0&406\\
3&259,943,766&8,491,690&0&403\\
4&259,941,282&8,494,174&0&465\\
5&259,941,612&8,493,844&0&360\\
6&259,945,101&8,490,355&0&425\\
7&259,941,254&8,494,202&0&433\\
8&259,943,964&8,491,492&0&463\\
9&259,944,407&8,491,049&0&424\\
10&259,940,336&8,495,120&0&405\\
11&259,947,067&8,488,389&0&460\\
12&259,943,744&8,491,712&0&413\\
13&259,945,142&8,490,314&0&365\\
14&259,944,929&8,490,527&0&373\\
15&259,946,018&8,489,438&0&425
\end{array}
}
\]

Summing gives

\[
\boxed{
N_{\rm class}=4,159,095,994,
}
\]

\[
\boxed{
N_{\rm fringe}=135,871,302,
}
\]

and

\[
\boxed{
N_{\rm class}+N_{\rm fringe}=2^{32}.
}
\]

Every one of the `135,871,302` explicitly followed representatives descends below itself.  The global maximum first-descent depth in this certificate is

\[
\boxed{470.}
\]

The explicit trajectory fraction is

\[
\boxed{
\frac{135,871,302}{2^{32}}
=0.0316350026987\ldots
}
\]

or about `3.1635%`.

## 5. Agreement with the staged bootstrap

The same layer was also certified incrementally.  Starting with the low-20 selector block and adding one new ternary selector at a time, only the new half-block was checked at each stage.

The staged counts through `d=32` sum to exactly the same totals as the independent sixteen-chunk partition above.  Thus two different finite decompositions of the same layer agree on the class/trajectory total and on zero failures.

## 6. Recursive-sufficiency jump to `V_33`

Ansari's recursively-sufficient core has the form

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,
\ a_i\in\{0,1\}
\right\}.
\]

The previous `A_32` certificate closed the `a_32=0` block with lower digits `a_0,...,a_31` arbitrary.

The present certificate closes the complementary `a_32=1` block with the same lower 32 digits arbitrary.

After both blocks are exhausted, the next possible member of `F` in increasing order first turns on `a_33`.  Hence a hypothetical minimal counterexample below

\[
4(3^{44}+3^{33})+3
\]

has been eliminated.

Therefore the continuous verified floor advances to

\[
\boxed{
V_{33}=4(3^{44}+3^{33})+2
=3,939,105,844,976,711,153,618.
}
\]

Relative to `V_32`, the gain is

\[
\boxed{
V_{33}-V_{32}
=8\cdot3^{32}
=14,824,161,510,814,728.
}
\]

Relative to the original recursively-extended floor `V_0=4*3^44+2`, the total extension is

\[
\boxed{
V_{33}-V_0
=4\cdot3^{33}
=22,236,242,266,222,092.
}
\]

## 7. What this result does and does not show

This is a finite verification/bootstrap theorem.  It is substantially more compressed than testing every ordinary integer in the added interval, and only about 3.16% of the ternary representatives require trajectory following, but it is still not an asymptotic proof mechanism.

The retained dyadic residue fraction stabilizes rather than tending to zero at fixed depth 27.  Repeating the same construction on higher ternary layers therefore doubles the representative work at each layer.

Accordingly the next proof target is structural:

\[
\boxed{
\text{grow binary/Hensel resolution with ternary layer depth}
}
\]

or prove a same-integer incompatibility between the retained dyadic hard core and the recursively-sufficient ternary address.

The finite `V_33` advance is retained as a reproducible benchmark for any such theorem.
