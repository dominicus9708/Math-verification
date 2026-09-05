# A0 s=1 first-defect dyadic-shell audit

Date: 2026-08-28

Status: **SAFE necessary pruning**. This note records the exact consequence of the certified first-75 Hamming-radius closure through radius 7. It is not a proof of full pre-bridge membership and not a proof of Collatz.

## 1. Inputs

The current Route-B A0 s=1 audit has already certified:

- physical shell `2^71 < X < 2^72`;
- refined upper bound `X <= 3234977022306677631165`;
- exact threshold start address
  `X_th = 4697939311072332635131` modulo `2^72`;
- every bounded physical pure-ballot first-75 word of Hamming distance at most 7 from the threshold word fails under deterministic Collatz extension.

Hence every remaining full survivor must satisfy

\[
\boxed{d_{75}\ge 8.}
\]

## 2. First-disagreement orientation

Let `w_th` be the length-75 lower-ballot threshold word and `w` another pure-ballot word.

At the first position where the two differ, `w` cannot change a threshold `1` to `0`: before the first disagreement the ballot surplus relative to threshold is zero, so a `1 -> 0` change would make the surplus negative immediately.

Therefore the first disagreement is necessarily

\[
\boxed{0\to1.}
\]

The later compensating changes may be more complicated; only this first orientation is used below.

## 3. Exact candidate positions

An exact finite DP over the first 75 threshold positions, with the conditions

- pure ballot,
- total first-75 Hamming distance at least 8,
- first-disagreement orientation as above,

shows that the first disagreement can occur only at

\[
\boxed{
F=\{2,5,8,10,13,16,18,21,24,27,29,32,
35,37,40,43,46,48,51,54,56,59,62,65\}.
}
\]

Positions are zero-indexed.

## 4. Dyadic valuation shell

For a parity word, the start address modulo `2^72` is triangular in the parity positions. If `f` is the first position where a candidate differs from `w_th`, then all address contributions below `2^f` agree and the first changed contribution is an odd multiple of `2^f`.

Therefore

\[
\boxed{v_2(X-X_{th})=f.}
\]

Combining with the finite set above gives the SAFE necessary condition

\[
\boxed{v_2(X-X_{th})\in F.}
\]

Equivalently, for one and only one `f in F`,

\[
\boxed{X\equiv X_{th}+2^f\pmod{2^{f+1}}.}
\]

Thus the remaining physical X-domain is not one interval but a union of 24 disjoint dyadic valuation shells.

## 5. Cardinality consequence

Inside

\[
2^{71}<X\le3234977022306677631165,
\]

the total number of ordinary integer candidates is

\[
873793780871855024317.
\]

The union of the 24 valuation shells contains exactly

\[
125072439876495812978
\]

ordinary integers, about `14.3137%` of that refined interval.

This percentage is a deterministic set-cardinality ratio. It is not a probability and is not multiplied by other marginal ratios.

## 6. Ternary-channel noninteraction

The first-75 correction defect occurs in very early odd ordinals. In the full pre-correction integer, every such early term carries an enormous factor of `3^(j0-r)`. For `r<=75`,

\[
j_0-r\ge j_0-75=65868186626>47.
\]

Hence the early defect contribution itself vanishes modulo `3^47`.

Therefore the new first-defect information cannot be promoted into an immediate contradiction with the terminal `3^28` or `3^47` saturation results. Those terminal ternary windows are blind to this early contribution.

By contrast, the dyadic channel exposes the first defect exactly through `v2(X-X_th)`.

## 7. DSD audit status

### SAFE

- `d_75 >= 8` for any remaining bounded physical pure-ballot survivor;
- first disagreement is `0 -> 1`;
- `v2(X-X_th) in F`;
- the 24 shells are disjoint and their cardinality is exact.

### REJECTED inference

Do **not** infer a ternary-window contradiction from the early defect merely because the same correction object participates in both channels. The early defect is invisible modulo `3^47`.

### OPEN

- full correction-language membership `C_req in C_pre`;
- complete C4F / renewal-gap formation compatibility;
- full long pre-bridge and tail first-passage extension;
- all other global Collatz escape branches.

This result is a strong Route-B pruning theorem only.
