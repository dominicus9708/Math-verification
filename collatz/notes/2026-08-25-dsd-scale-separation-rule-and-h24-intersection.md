# DSD scale-separation rule and Q7/B20 × root-fullmax H24 audit

Date: 2026-08-25

## Status

Safe finite certificate plus a general structural lemma candidate.

This note does **not** claim a proof of the Collatz conjecture.  It records a rule that removes the large absolute start value from the reverse-ancestor comparison once the ternary scale is sufficiently larger than every finite correction term.

## 1. DSD logical chain used here

The calculation is organized as:

1. **Formation / describability partition**: fix a low ternary cylinder and the dyadic residue needed for the first `B` Collatz steps.
2. **Axis separation**: separate the large start scale `N` from the finite affine corrections `Rf,C`.
3. **Static aggregation**: count all high ternary selectors by exact cyclic subset-sum DP.
4. **Dynamics**: compare the forward endpoint with every admissible positive reverse code.
5. **Closure test**: intersect the cross-place survivor language with the independent nested root-Hensel full-max language on the **same integers**.

The important new point is step 2: beyond a finite threshold, the reverse comparison becomes a symbolic coefficient comparison.

## 2. Scale-separation lemma

For a forward prefix of time depth `B`, odd count `q_f`, and correction `R_f`, let

\[
y=T^B(N)=\frac{3^{q_f}N+R_f}{2^B}.
\]

For a positive odd-to-odd reverse code of reverse odd depth `q_r`, total binary exponent `K`, and correction `C`,

\[
m=\frac{2^K y-C}{3^{q_r}}
 =\frac{2^K(3^{q_f}N+R_f)-C2^B}{2^B3^{q_r}}.
\]

Then

\[
2^B3^{q_r}(m-N)
 =A N+2^K R_f-C2^B,
\]

where

\[
A=2^K3^{q_f}-2^B3^{q_r}.
\]

For `B<=Bmax`, `K<=Kmax`, `q_r<=Q`, we have the elementary bounds

\[
R_f<3^{B_{\max}},
\]

and, from the reverse recurrence `C_{d+1}=2^a C_d+3^d`,

\[
C<2^{K-1}3^{q_r}\le 2^{K_{\max}-1}3^Q.
\]

Therefore it is sufficient that

\[
N_{\min}>
\max\left(
  2^{K_{\max}}3^{B_{\max}},
  2^{K_{\max}+B_{\max}-1}3^Q
\right).
\]

Under this condition:

- `A<0` implies `0<m<N`;
- `A>0` implies `m>N`;
- `A=0` is possible only when `K=B` and `q_r=q_f`, and then `m<N` iff `C>R_f`.

Thus the large-number comparison is replaced by a finite symbolic rule on `(B,q_f,q_r,K,R_f,C)`.

## 3. Current parameters

For the canonical `m=44` ternary core,

\[
N_{\min}=4\cdot3^{44}+3
=3,939,083,608,734,444,931,527.
\]

At

- `Q=7`,
- `Bmax=20`,
- `Kmax=36`,

we obtain

\[
2^{36}3^{20}=239,609,999,527,967,195,136,
\]

\[
2^{55}3^7=78,794,979,080,474,198,016.
\]

Hence the scale-separation inequality is satisfied with substantial margin.

For these fixed parameters the same inequality first becomes automatic at

\[
\boxed{m\ge 42}.
\]

So the coefficient-sign reduction is not special to `m=44`.

## 4. Regression against the original Q7/B20 calculation

The new coefficient-sign implementation reproduces the previously recorded exact Q7/B20 totals:

- forward-labelled: `14,245,065,266,398`
- reverse-labelled: `2,191,707,946,271`
- surviving: `1,155,412,831,747`
- total: `2^44 = 17,592,186,044,416`

This is an exact regression, not a ratio estimate.

## 5. Same-integer intersection with root full-max H24

Nested root-Hensel full maximality through `H=24` has exactly

\[
234,156
\]

surviving canonical dyadic residues `z=(N-3)/4 mod 2^22`.

After exact selector aggregation, the H24 root-fullmax language contains

\[
982,121,237,012
\]

of the `2^44` ternary-selector starts.

Inside that language, the Q7/B20 reverse rule removes another

\[
197,333,898,861
\]

starts, leaving the exact same-integer intersection

\[
\boxed{784,787,338,151}.
\]

Relative to the previous Q7/B20 survivor count,

\[
1,155,412,831,747-784,787,338,151
=370,625,493,596,
\]

so H24 root-fullmax removes

\[
\boxed{32.0773219\%}
\]

of the remaining Q7/B20 survivors.

The new combined survivor fraction of the full `m=44` core is

\[
\boxed{0.0446099953791759}
\]

or about

\[
\boxed{4.4610\%}.
\]

Equivalently, the safe finite exclusion fraction is now about

\[
\boxed{95.5390\%}.
\]

## 6. Interaction is strongly non-independent

Ambient H24 root-fullmax survival fraction:

\[
0.055827128847568.
\]

Ambient Q7/B20 cross-place survival fraction:

\[
0.065677615552147.
\]

But among H24 root-fullmax survivors, Q7/B20 survival is

\[
0.799073789035081.
\]

Thus root-fullmax and cross-place are strongly positively correlated.  This is expected structurally: root-fullmax already requires coefficient survival along every prefix through depth 24, so the large forward-descent component of the cross-place sieve has already been removed.  The useful extra contribution of cross-place inside root-fullmax is therefore the reverse-ancestor channel.

This means multiplying ambient survival fractions would be invalid.

## 7. Low-ternary-cylinder uniformity diagnostic

Each fixed 7-selector low ternary mask contains `2^37` high-selector assignments.

For Q7/B20 alone, survivor counts over the 128 low masks range only from

- minimum `9,026,585,102` (mask 75)
- maximum `9,026,744,042` (mask 80)

corresponding to a relative spread of only about `17.6 ppm`.

After adding H24 root-fullmax, the per-mask survivors range from

- minimum `6,131,049,727` (mask 42)
- maximum `6,131,259,143` (mask 7)

with relative spread about `34.2 ppm`.

This near-uniformity is evidence that there is no obvious exceptional low-ternary cylinder at this resolution.  It is **not yet** a recursive contraction theorem.

## 8. Asymptotic admissible cone

Let the computational depths scale with ternary depth `m`:

\[
B\sim\beta m,\qquad K\sim\kappa m,\qquad Q\sim\gamma m.
\]

Ignoring the fixed factor `4`, the scale-separation conditions asymptotically become

\[
\boxed{\beta+\kappa\log_3 2<1},
\]

and

\[
\boxed{\gamma+(\beta+\kappa)\log_3 2<1}.
\]

Inside this cone, finite affine corrections are asymptotically dominated by the ternary start scale, so reverse smaller-ancestor decisions reduce to symbolic coefficient states.

This is the most useful general rule extracted in this audit.

## 9. Remaining proof target

The finite calculations now suggest a sharper target than simply increasing `Q`, `B`, or `H`.

We need a **uniform recursive cylinder-contraction theorem**.  One suitable form would be:

> There exist a fixed block depth `r` and a constant `rho<1` such that every surviving symbolic cylinder, after extension by `r` selector digits and application of the safe forward/root/reverse rules, has surviving child mass at most `rho` times its total child mass.

If such a statement is proved and its hypotheses stay inside the admissible scale-separation cone, then survivor mass decays geometrically rather than merely at one finite `m`.

That is the next main line.  The immediate computational task is therefore to build the survivor **transition operator** between ternary cylinders and test whether a uniform contraction constant exists, rather than only counting the global survivor total.

## Certificate

Source:

`collatz/src/m44_q7_b20_rootfullmax_h24_scale_rule_certificate.cpp`

The executable asserts both the old Q7/B20 totals and the new H24 intersection totals exactly.
