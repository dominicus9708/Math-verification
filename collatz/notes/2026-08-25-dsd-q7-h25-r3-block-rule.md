# DSD Q7/H25 three-step block contraction rule

Date: 2026-08-25

## Status

Safe finite exact-correction audit plus strengthened block-contraction candidate.

No Collatz proof is claimed.

## 1. Setup

Parameters:

- canonical `m=44` selector core,
- fixed reverse resolution `Q=7`,
- nested root-fullmax depth `H=25`,
- exact affine correction comparison,
- reverse binary budget `Kmax=36`,
- dynamical depths `B=12,...,24`.

At every relevant depth, coefficient survival implies `q_B>=Q`, because

\[
2^B>3^{Q-1}.
\]

Thus

\[
T^B(N)\equiv2^{-B}R_B\pmod{3^Q},
\]

so the endpoint ternary residue used by the reverse-potential test is independent of the fixed low-ternary cylinder.

## 2. Exact global survivor totals

The H25 certificate gives:

- B12: `882,638,509,499`
- B13: `868,220,625,992`
- B14: `846,424,913,660`
- B15: `838,136,917,312`
- B16: `832,810,165,410`
- B17: `813,294,069,586`
- B18: `807,835,174,452`
- B19: `793,039,648,031`
- B20: `784,273,540,963`
- B21: `778,655,198,539`
- B22: `758,279,262,934`
- B23: `751,090,242,516`
- B24: `748,286,338,269`

Every one-step transition contracts every positive Q7 cylinder; there are no equal or expanding cylinders.

The weakest one-step transition is B23->B24, whose worst cylinder ratio is approximately

\[
0.99626832870053496.
\]

Therefore a uniform one-step constant is not the natural target.

## 3. Bounded-block comparison

Scanning every admissible starting depth in `12<=B` with `B+r<=24` gives:

- r=2: worst ratio `0.986825350808382335`, starting at B22;
- r=3: worst ratio `0.964322002486074590`, starting at B17;
- r=4: worst ratio `0.957414888275353702`, starting at B17;
- r=5: worst ratio `0.943574204543562903`, starting at B19;
- r=6: worst ratio `0.929037789208044132`, starting at B15.

Thus the first especially stable candidate is

\[
\boxed{
r=3,
\qquad
M_{B+3}(\ell)<0.965\,M_B(\ell)
}
\]

through the whole tested H25 window.

This is materially stronger than assuming a nearly stationary one-step loss.

## 4. Independent convolution derivation for r=3

On the dyadic group

\[
G=\mathbb Z/2^{23}\mathbb Z,
\]

the exact full-selector DP has

- `c_min = 2,092,917`,
- `c_max = 2,102,038`,
- `c_min/c_max = 0.9956608776815643`.

The Q7 high-selector DP has

- `h_min = 15,828`,
- `h_max = 16,923`,
- `h_min/h_max = 0.9352951604325475`.

Therefore

\[
\kappa
=\frac{h_{\min}}{h_{\max}}
 \frac{c_{\min}}{c_{\max}}
\approx0.9312368003275897.
\]

For each three-step block, define the global dynamical loss

\[
\eta_B=\frac{T_B-T_{B+3}}{T_B}.
\]

Over B=12,...,21, the smallest observed global three-step loss is

\[
\eta_{\min}\approx0.03568270040106482,
\]

at B17->B20.

The convolution transfer lemma therefore gives, without using the direct per-cylinder maxima,

\[
\frac{M_{B+3}(\ell)}{M_B(\ell)}
\le1-\kappa\eta_{\min}
\approx0.9667709562514644.
\]

Hence a second, logically independent finite statement is

\[
\boxed{
M_{B+3}(\ell)<0.967\,M_B(\ell)
}
\]

for every tested Q7 cylinder and every starting depth B=12,...,21.

The direct exact cylinder enumeration improves `0.967` to `0.965`.

## 5. Structural conclusion

The current DSD chain has now separated the closure problem into:

1. endpoint decoupling once `q_B>=Q`;
2. reverse-potential state compression at fixed Q;
3. global bounded-block dynamical loss `eta`;
4. selector mixing `kappa`;
5. convolution transfer from global loss to every cylinder.

The asymptotic target is no longer a one-step contraction theorem.  A sufficient theorem is:

There exist fixed `Q`, fixed block length `r`, and constants

\[
\kappa_0>0,
\qquad
\eta_0>0,
\]

such that for all sufficiently large admissible scales,

\[
\kappa_{m,Q,H-2}\ge\kappa_0,
\qquad
\frac{T_B-T_{B+r}}{T_B}\ge\eta_0.
\]

Then every cylinder obeys

\[
M_{B+r}(\ell)
\le(1-\kappa_0\eta_0)M_B(\ell),
\]

and repeated blocks force exponential extinction.

Current finite evidence now favors `Q=7` fixed and `r=3` as the first asymptotic theorem candidate.

Source:

`collatz/src/dsd_q7_h25_b12_b24_block_contraction_certificate.cpp`
