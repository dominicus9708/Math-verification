# Renewal-floor base-depth theorem

Date: 2026-08-11

Status: **exact consequence of the renewal definition and macroblock sign theorem**.

## 1. First block leaving a renewal floor

Let `N` be a renewal floor in a nonperiodic positive-integer block orbit, and write the first maximal block as

\[
N=2^hK-1,
\qquad
N_1=\frac{3^hK-1}{2^d},
\qquad d\ge1.
\]

If the renewal segment has one block, `N_1` is the next renewal floor and is strictly larger than `N`.

If the renewal segment has more than one block, `N_1` is an interior block start and by the renewal definition satisfies

\[
N_1>N'>N,
\]

where `N'` is the next renewal floor.

Thus in every case

\[
\boxed{N_1>N.}
\]

By the macroblock sign theorem, the first block must therefore be subcritical:

\[
\boxed{
\frac{2^{h+d}}{3^h}<1
}
\]

or equivalently

\[
\boxed{d<\alpha h,\qquad\alpha=\log_2(3/2).}
\]

## 2. Renewal floors have depth at least two

Because `d>=1` and

\[
\alpha<1,
\]

the inequality `d<alpha h` is impossible for `h=1`.

Hence

\[
\boxed{h=v_2(N+1)\ge2}
\]

for every renewal floor of a nonperiodic survivor.

Therefore

\[
\boxed{N\equiv3\pmod4.}
\]

## 3. Renewal gaps are multiples of four

For consecutive renewal floors `N<N'`, both satisfy `N=N'=3 mod 4`. Hence

\[
\boxed{4\mid(N'-N).}
\]

Since the floors are distinct,

\[
\boxed{g:=N'-N\ge4.}
\]

## 4. Supercritical block-count consequence

The exact renewal supercritical block-count theorem gives

\[
P>1\Longrightarrow m>g,
\]

where `m` is the number of maximal blocks in the segment.

Thus every aggregate-supercritical renewal satisfies

\[
\boxed{m\ge5.}
\]

In particular, a supercritical renewal can never be a one-, two-, three-, or four-block floor-to-floor excursion.

## 5. Depth-battery consequence

The transported depth variable therefore has the hard lower floor

\[
\boxed{h_j\ge2.}
\]

If a supercritical renewal avoids exponential block overload `m>2^{h_j}`, the gap-depth transfer theorem forces

\[
h_{j+1}<h_j.
\]

Hence any consecutive run of such cheap supercritical renewals can have length at most `h_j-2` before reaching the base depth `2`, where the next supercritical renewal must pay the overload branch.
