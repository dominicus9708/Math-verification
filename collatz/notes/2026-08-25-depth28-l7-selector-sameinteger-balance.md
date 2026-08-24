# Depth-28 aligned-L7 same-integer selector balance

Date: 2026-08-25

Status: **exact finite cross-base measurement** on the first 28 time bits of the current R1 mechanical phase.  It measures concentration only; later-block L7 maximality is not promoted to a root-global exclusion theorem here.  This does not prove Collatz.

## 1. Local language

In each aligned 7-bit block keep only the locally residue-maximal representative in every full-Hensel class.  The exact class counts are

\[
(1,2,6,15,21,16,7,1),
\]

so one block has 69 allowed words.

Over the first four aligned blocks, additionally impose nonnegative relative coefficient height against the exact first-28 mechanical reference.

The resulting language has

\[
\boxed{1,010,201}
\]

words, with terminal-height distribution

\[
\boxed{
(116041,289509,277962,185001,93151,35745,10307,2153,305,26,1)
}
\]

for heights `0,...,10`.

Thus the terminal-neutral slice contains

\[
\boxed{116,041}
\]

canonical residues modulo `2^28`.

## 2. Exact same-integer selector intersection

All these starts are `3 mod 4`, so write

\[
N=4Y+3,
\qquad Y\pmod{2^{26}}.
\]

The ternary selector is aggregated exactly by cyclic subset-sum multiplicity modulo `2^26`, then intersected with the canonical parity residues above.

For the current m44 selector population

\[
2^{44}-2^{33}=17,583,596,109,824,
\]

the exact intersection with the full 28-bit L7/survival language is

\[
\boxed{264,688,110,351},
\]

or

\[
\boxed{1.5053127284\ldots\%}.
\]

For the two m45 affine blocks, population `2^45`, the exact count is

\[
\boxed{529,636,500,458},
\]

or

\[
\boxed{1.5053174720\ldots\%}.
\]

## 3. Conditional concentration Xi

Because the common `N=3 mod 4` factor is removed exactly, the uniform comparison density is

\[
\frac{1,010,201}{2^{26}}.
\]

Hence

\[
\Xi_{44,28}
=
\frac{264688110351/(2^{44}-2^{33})}{1010201/2^{26}}
\approx
\boxed{0.9999972992}<1.
\]

For m45,

\[
\Xi_{45,28}
\approx
\boxed{1.0000004504},
\]

and the certificate proves the exact rational bound

\[
\boxed{
\Xi_{45,28}<1+2^{-20}.
}
\]

Thus, at this finite same-integer resolution, the recursively-sufficient ternary selector is essentially perfectly balanced relative to the L7/survival hard language.  There is no visible positive repair concentration.

## 4. Unresolved first-defect channels

Keeping only the currently open first-defect channels gives

\[
\boxed{264,650,899,763}
\]

m44 starts and

\[
\boxed{528,441,621,623}
\]

m45 starts.

Adding terminal neutrality gives

\[
\boxed{30,396,266,923}
\]

for current m44 and

\[
\boxed{60,645,599,888}
\]

for the two m45 blocks.

These are respectively about `0.172867%` and `0.172365%` of the full selector populations.

The neutral-slice concentration itself is anti-biased:

\[
\Xi^{\rm neutral}_{44,28}\approx0.9997259713<1,
\]

\[
\Xi^{\rm neutral}_{45,28}\approx0.9968226923<1.
\]

## 5. Scope correction

The four-block L7 condition is used here only to define and measure a finite local hard language.  The 2026-08-25 later-block-globality correction still applies: a locally smaller predecessor at a later orbit state need not lie below the original minimal root.

Therefore the present result is **not** a repeated L7 exclusion theorem and is **not** multiplied across windows.

Its legitimate role is narrower but useful:

\[
\boxed{
\text{same-integer ternary mass shows essentially zero one-window repair bias.}
}
\]

The remaining asymptotic problem is to prove that this near-balance cannot turn into a positive linear conditional bias after long open-positive conditioning.

## 6. Reproducibility

Exact source:

`collatz/src/depth28_l7_selector_sameinteger_certificate.cpp`
