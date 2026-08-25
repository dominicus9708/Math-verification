# Depth-28 full root-Hensel maximality: q-slice neutrality audit

Date: 2026-08-25

Status: **exact finite q-slice diagnostic.**  This note refines the depth-28 full root-Hensel cross-base audit and does not prove Collatz or asymptotic independence.

## 1. Purpose

The global credit-1 to full-root-max survival ratio is nearly identical in the ambient coefficient language and in the m=44/m=45 ternary selector intersections.

A remaining failure mode was cancellation: different final odd-count `q` slices might carry sizable positive and negative cross-base biases that happen to cancel in the total.

The companion certificate

`collatz/src/root_fullmax_depth28_qslice_crossbase_certificate.cpp`

therefore repeats the exact same-integer selector intersection separately for every final `q` at depth 28.

## 2. Exact q-slice counts

Only `q=18,19,20,21` receive any additional removal from credits greater than one beyond the root credit-1 filter.

| q | ambient credit-1 | ambient full-max | m=44 credit-1 | m=44 full-max | m=45 credit-1 | m=45 full-max |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 538,632 | 535,688 | 141,130,139,259 | 140,358,729,579 | 282,398,831,936 | 280,855,343,487 |
| 19 | 1,007,189 | 1,003,902 | 263,899,655,968 | 263,038,374,282 | 528,056,958,857 | 526,333,613,758 |
| 20 | 737,529 | 736,512 | 193,243,924,797 | 192,977,453,176 | 386,677,263,787 | 386,144,064,085 |
| 21 | 385,887 | 385,729 | 101,108,765,296 | 101,067,364,549 | 202,315,953,970 | 202,233,108,519 |

For every `q >= 22` through `q=28`, the root credit-1 and nested full-root-max sets are already identical at H=28.

## 3. Conditional survival factors

For `q=18`:

- ambient: `0.994534301712486`;
- m=44: `0.994534054284575`;
- m=45: `0.994534366737927`.

Relative to ambient, the selector shifts are approximately

- m=44: `-0.2488 ppm`;
- m=45: `+0.0654 ppm`.

For `q=19`:

- ambient: `0.996736461577718`;
- m=44: `0.996736328879093`;
- m=45: `0.996736440889388`;

with relative shifts about `-0.1331 ppm` and `-0.0208 ppm`.

For `q=20`:

- ambient: `0.998621071171439`;
- m=44: `0.998621060810683`;
- m=45: `0.998621073044797`;

with relative shifts about `-0.0104 ppm` and `+0.00188 ppm`.

For `q=21`:

- ambient: `0.999590553711320`;
- m=44: `0.999590532562842`;
- m=45: `0.999590514492929`;

with relative shifts about `-0.0212 ppm` and `-0.0392 ppm`.

Thus the largest observed q-conditioned relative shift is only about `0.249 ppm`.

## 4. Audit conclusion

The global near-neutrality is **not** an artifact of large opposite q-slice biases cancelling each other.

At every q slice where credits greater than one actually remove additional prefixes, the selector-conditioned survival factor remains extremely close to the ambient factor.  At q>=22 there is no additional full-max removal at all.

Therefore the depth-28 evidence now supports a stronger demotion:

- retain root credit-1 and full root-Hensel maximality as globally safe auxiliary sieves;
- do not treat either as the missing ternary-dyadic transversality mechanism;
- do not invest in deeper root-max enumeration merely to extrapolate a finite entropy rate;
- redirect the main search toward conditions that couple the ternary selector to binary structure through a genuinely cross-place or non-stationary statistic.

## 5. Reproducibility

The certificate checks the exact q-slice integers above and aborts if any differ.  It also asserts that for every q from 22 through 28 the credit-1 and full-max weighted counts coincide in ambient, m=44, and m=45 layers.

An optimized local run completed with `PASS`.
