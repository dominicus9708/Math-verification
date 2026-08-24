# m44 depth-28 shifted-layer stationarity audit

Date: 2026-08-25

Status: **exact finite same-integer negative-control certificate.**  The remaining current `m=44` core is decomposed into its eleven disjoint shifted selector layers after the already certified `A_33` prefix block.  The depth-28 survival fraction is essentially stationary across all eleven layers.  This shows that continuing the same finite shifted-layer sieve recursively will not supply an asymptotic mechanism by itself.

## 1. Exact current-core decomposition

The full `m=44` selector family is

\[
\mathcal C_{44}=\left\{4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3:a_i\in\{0,1\}\right\}.
\]

The previously certified finite bootstrap closes the entire low block with `a_33=...=a_43=0`, namely `A_33` of size `2^33`.

Every remaining selector has a unique highest selected ternary digit `d in {33,...,43}`.  Therefore the current core decomposes exactly as

\[
\boxed{
\mathcal C_{44}\setminus A_{33}
=\bigsqcup_{d=33}^{43}
\left\{4\left(3^{44}+3^d+\sum_{i=0}^{d-1}a_i3^i\right)+3\right\}.
}
\]

The `d`th layer has exactly `2^d` members.

## 2. Exact depth-28 same-integer profile

Using the exact first-28 mechanical-relative coefficient-survival language and exact cyclic ternary subset-sum multiplicities modulo `2^26`, the layerwise counts are:

| d | size | all survival fraction | unresolved-p fraction | unresolved neutral-return fraction |
|---:|---:|---:|---:|---:|
|33|8,589,934,592|0.0525185266742483|0.0525156091898680|0.00988522754050791|
|34|17,179,869,184|0.0525193815701641|0.0525164462742396|0.00988575303927064|
|35|34,359,738,368|0.0525201580312569|0.0525172387424391|0.00988685656921007|
|36|68,719,476,736|0.0525199935509590|0.0525170771434205|0.00988688088546041|
|37|137,438,953,472|0.0525199589683325|0.0525170418986818|0.00988609853811795|
|38|274,877,906,944|0.0525201484670106|0.0525172275047225|0.00988670320293750|
|39|549,755,813,888|0.0525205887443008|0.0525176676947012|0.00988658819551347|
|40|1,099,511,627,776|0.0525203516972397|0.0525174303320455|0.00988666080593248|
|41|2,199,023,255,552|0.0525204446530552|0.0525175233483424|0.00988662248300898|
|42|4,398,046,511,104|0.0525203863151091|0.0525174658625929|0.00988663448765692|
|43|8,796,093,022,208|0.0525204033100408|0.0525174823399084|0.00988662080476388|

The exact aggregates reproduce the previous current-core certificate:

\[
\boxed{923,497,419,313}
\]

all depth-28 survivors,

\[
\boxed{923,446,059,910}
\]

survivors in the already unresolved first-defect channels, and

\[
\boxed{173,842,387,012}
\]

unresolved neutral-return survivors.

## 3. Interpretation

There is no exceptional high ternary layer at this resolution.  The survival proportions stabilize almost immediately near

\[
\boxed{5.25204\%}
\]

for the full coefficient-survival language and near

\[
\boxed{0.98866\%}
\]

for the unresolved neutral-return slice.

Hence the recursive selector decomposition

\[
A_{d+1}=A_d\dot\cup(A_d+4\cdot3^d)
\]

is useful for finite bookkeeping, but **the same fixed-depth dyadic sieve does not become stronger as `d` grows.**  Continuing it one ternary layer at a time would only double the representative mass while leaving the normalized hard fraction essentially unchanged.

This agrees with the earlier fixed-resolution saturation barrier and supplies an exact same-integer version of that warning on the current resonance.

## 4. Consequence for the next proof step

The next argument should not rely on a special shifted layer.  It must use information transported from one window to the next.

For the neutral-return branch the natural transported datum is the root-globalized ultrametric translation label

\[
\boxed{(p,D/2^p\bmod2^r)}.
\]

The layer-stationarity calculation therefore strengthens the case for building the next quotient around this locked translation rather than around the ternary layer index.

## 5. Reproducibility

Exact source:

`collatz/src/m44_depth28_shifted_layer_stationarity_certificate.cpp`
