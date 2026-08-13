# Reverse-23 x binary-26 cross-mass audit in the full m=44 core

Date: 2026-08-13

Status: **exact finite cross-base static aggregation + negative strategic result**.  The calculation combines the depth-23 common-OO 3-adic minimal-counterexample sieve with the depth-26 dyadic coefficient-survival language across the full 44-trit recursively sufficient block, without enumerating individual Collatz trajectories.  It does not prove Collatz.

## 1. Full ternary block

Write

\[
N=4Y+3,
\qquad
Y=3^{44}+\sum_{i=0}^{43}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

There are exactly

\[
2^{44}
\]

selector assignments.

## 2. 3-adic low-prefix filter

The common-OO alternate-preimage sieve through ternary depth 23 removes

\[
299740
\]

of the

\[
2^{23}=8388608
\]

low-prefix cylinders.

Every retained low-23 prefix has all `2^21` high-trit extensions available before the dyadic filter.  Hence the retained ternary mass is

\[
\boxed{
(2^{23}-299740)2^{21}
=16963585703936.
}
\]

## 3. Static transport to the dyadic depth-26 coordinate

Depth-26 parity survival for `N=4Y+3` depends only on

\[
Y\pmod{2^{24}}.
\]

The retained low-23 ternary prefixes are first counted modulo `2^24`.  The high selectors `a_23,...,a_43` are then added by the exact cyclic subset-sum recurrence

\[
F_{i+1}(r)=F_i(r)+F_i(r-3^i)
\pmod{2^{24}}.
\]

Thus the complete retained ternary distribution is constructed as a static aggregation on `Z/2^24 Z`; no Collatz trajectory of a `2^44`-member list is followed.

The binary coefficient-survival set at depth 26 has exactly

\[
\boxed{1037374}
\]

reduced residue classes, agreeing with the earlier full-core certificate.

## 4. Exact intersection mass

The earlier binary-only depth-26 survivor mass is

\[
\boxed{1087765074138}.
\]

After first removing all depth-23 common-OO reverse-forbidden ternary prefixes, the exact binary-surviving mass is

\[
\boxed{1048897463045}.
\]

Therefore the joint survivor fraction of the full `2^44` block is

\[
\boxed{
\frac{1048897463045}{2^{44}}
=0.0596229178339058308\ldots
}
\]

or about `5.96229%`.

## 5. Near-independence diagnostic

The binary-only survival fraction is

\[
\boxed{
\frac{1087765074138}{2^{44}}
=0.06183228573138422\ldots
}
\]

whereas the binary survival fraction conditioned on passing the reverse-23 filter is

\[
\boxed{
\frac{1048897463045}{16963585703936}
=0.06183229662356279\ldots
}
\]

The difference is only about

\[
\boxed{1.09\times10^{-8}}.
\]

Equivalently, relative to exact independence the joint count differs by only about `1.85e5` representatives out of a joint mass near `1.05e12`, a relative discrepancy about `1.76e-7`.

Thus at this shallow cross-base scale the two restrictions are almost perfectly multiplicative rather than anti-aligned.

## 6. Strategic consequence

This is a negative but useful result.

The depth-23 3-adic reverse filter is rigorous and the depth-26 dyadic coefficient filter is rigorous, but simply multiplying increasingly refined shallow filters is not presently revealing the strong arithmetic incompatibility needed to make the intersection empty.

The observed behavior is instead consistent with the Fourier-mixing picture already proved/diagnosed at shallow resolution: the ternary selector mass is close to equidistributed across the relevant dyadic classes, so a low-trit 3-adic restriction mostly removes the same proportion from every dyadic survivor class.

Therefore the terminal cross-base mechanism should not be sought merely as

\[
\text{3-adic density loss}\times\text{2-adic density loss}.
\]

The useful remaining target is genuinely high-resolution and same-integer:

\[
\boxed{
\text{deep dyadic canonical-lift rigidity}
\quad+\quad
\text{3-adic / ternary minimality constraints}.
}
\]

In particular, the zero-lift fibre rather than the whole prefix/suffix direct sum is the relevant object for R2.

## 7. Verification

`collatz/src/m44_reverse23_binary26_cross_mass.cpp` performs the entire calculation with exact integers.  It:

1. recomputes all reverse-forbidden low-23 prefixes;
2. checks the exact removed count `299740`;
3. constructs the retained ternary distribution modulo `2^24` by Gray-code initialization and subset-sum convolution;
4. constructs the depth-26 Beatty coefficient-survivor residue set exactly;
5. checks its class count `1037374`;
6. certifies the joint survivor mass `1048897463045`.
