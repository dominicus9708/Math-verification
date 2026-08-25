# DSD transition correction and B-axis contraction rule

Date: 2026-08-25

## Status

Safe finite audit plus structural-rule extraction.

This note corrects the superseded `2026-08-25-dsd-cylinder-transition-q7-q9.md` and records the stronger dynamical-depth (`B`) contraction observed after the correction.

No Collatz proof is claimed.

## 1. Audit correction

The earlier Q=8 and Q=9 transition totals were not reproducible.

An independent implementation of the original reverse frontier and a compressed Bellman-style reverse DP agreed with each other, while disagreeing with the old Q-refinement totals.

The old Q-refinement bookkeeping artificially lost mass when one ternary selector digit moved from the high-selector aggregate into the fixed low mask.

The old Q=8 and Q=9 combined counts are therefore withdrawn.

The corrected source is:

`collatz/src/dsd_q7_q10_corrected_transition_certificate.cpp`

## 2. Reverse-potential compression rule

For an admissible reverse odd-to-odd code

\[
m=\frac{2^K y-C}{3^{q_r}},
\]

define the reverse coefficient potential

\[
\Lambda=\frac{3^{q_r}}{2^K}.
\]

In the scale-separated regime, the strict smaller-ancestor test against a forward endpoint with coefficient ratio

\[
\Theta=\frac{3^{q_f}}{2^B}
\]

only needs the maximum attainable reverse potential

\[
\Lambda_Q(z)=\max_{\text{admissible reverse codes from }z}\frac{3^{q_r}}{2^K}.
\]

- If `Lambda_Q(z) > Theta`, a strict coefficient contraction exists.
- If `Lambda_Q(z) < Theta`, no reverse code can give a strict coefficient contraction.
- If equality holds, only the largest correction `C` among the maximizing codes must be retained.

Thus the full reverse path family can be compressed to one tuple `(q*,K*,C*)` per ternary residue and binary budget.

### Bellman recursion

For a residue `z mod 3^d`, the first inverse exponent `a` must satisfy

\[
2^a z\equiv1\pmod3.
\]

After the first inverse step,

\[
z'=\frac{2^a z-1}{3}\pmod{3^{d-1}}.
\]

If the best suffix is `(q',K',C')` and its own potential exceeds one, appending it gives

\[
(q,K,C)=(q'+1,K'+a,2^{K'}+3C').
\]

Otherwise stopping after the first inverse step is coefficient-optimal:

\[
(q,K,C)=(1,a,1).
\]

Candidates are ordered first by maximal `3^q/2^K`, then by maximal `C` on an exact tie.

### Independent frontier audit

The compressed DP was compared with the original full `(residue,K,C)` frontier for every endpoint residue through Q=10.

At Q=10 this means all

\[
3^{10}=59,049
\]

residues.

Result: zero mismatches in the maximizing tuple.

This is the main DSD-style state-compression result of this audit.

## 3. Corrected Q-axis totals at H24/B20/K36

Combined cross-place plus nested root-fullmax H24 survivors:

- Q7: `784,787,338,151`
- Q8: `776,902,007,561`
- Q9: `758,110,858,098`
- Q10: `752,548,965,765`

At Q10 the surviving fraction of the full `2^44` core is

\[
0.0427774560742477661,
\]

so the safe excluded fraction is about

\[
95.7222543926\%.
\]

## 4. Corrected parent-to-child Q contraction

Every tested parent still contracts strictly, but much more weakly than the superseded audit claimed.

### Q7 -> Q8

Worst parent ratio:

\[
\rho_7=0.989954390562391209.
\]

No equal or expanding parent.

### Q8 -> Q9

Worst parent ratio:

\[
\rho_8=0.994219546983941871.
\]

Four parents are extinguished completely; no parent expands.

### Q9 -> Q10

Worst parent ratio:

\[
\rho_9=0.997036735078904575.
\]

No equal or expanding parent.

## 5. Q-axis asymptotic warning

The worst-parent deficits are

\[
1-\rho_7\approx0.01004561,
\]

\[
1-\rho_8\approx0.00578045,
\]

\[
1-\rho_9\approx0.00296326.
\]

Multiplying by `2^Q` gives approximately

- Q7: `1.28584`
- Q8: `1.47980`
- Q9: `1.51719`

which is consistent with the finite-data hypothesis

\[
1-\rho_Q=O(2^{-Q}).
\]

This is not a theorem, but it is an important warning: if this scaling persists, then `rho_Q<1` at every single Q would still be insufficient because the deficits could be summable and the infinite product of the `rho_Q` could remain positive.

Therefore the Q-refinement axis is no longer the preferred closure route by itself.

## 6. B-axis contraction

Holding Q fixed and increasing the forward/dynamical depth B gives a much stronger and more stationary effect.

Source:

`collatz/src/dsd_b_axis_h24_contraction_certificate.cpp`

### Q=7

Totals:

- B18: `808,636,281,975`
- B20: `784,787,338,151`
- B22: `758,790,964,225`

Worst cylinder ratios:

- B18 -> B20: `0.970512230760285933`
- B20 -> B22: `0.966880742700459664`
- B18 -> B22: `0.938365630711384829`

### Q=8

Totals:

- B18: `801,761,825,945`
- B20: `776,902,007,561`
- B22: `750,528,152,486`

Worst cylinder ratios:

- B18 -> B20: `0.969002126690579002`
- B20 -> B22: `0.966062004983500975`
- B18 -> B22: `0.936111204000725395`

### Q=9

Totals:

- B18: `783,213,881,122`
- B20: `758,110,858,098`
- B22: `731,875,202,312`

Worst cylinder ratios:

- B18 -> B20: `0.969164685593047698`
- B20 -> B22: `0.966216078008374639`
- B18 -> B22: `0.936420790373049246`

For every one of these transitions:

- no cylinder expanded;
- no positive cylinder stayed exactly equal;
- every tested cylinder contracted.

A finite uniform statement valid over the tested window is therefore

\[
\mu(S_{Q,B+2}\cap C)
<0.971\,\mu(S_{Q,B}\cap C)
\]

for `Q in {7,8,9}` and `B in {18,20}`.

This is much closer to the form needed for a recursive closure theorem than the corrected Q-axis ratios.

## 7. Exact-correction test beyond the simple scale bound

The simple global scale-separation bound becomes too crude as B increases.

To test whether B-axis contraction was merely an artifact of that bound, the B=23 step was recomputed using the original finite correction terms.

Source:

`collatz/src/dsd_b23_exact_correction_certificate.cpp`

For the selected actual maximizing reverse code, positivity and `m<N` are checked directly from

\[
2^B3^{q_r}(m-N)
=
(2^K3^{q_f}-2^B3^{q_r})N+2^KR_f-C2^B,
\]

using exact quotient comparisons and the full m44 interval endpoints.

This test is conservative beyond scale separation: if the maximizing-coefficient code fails the finite correction check, the class is retained rather than searching a weaker coefficient code.

### B22 -> B23

Q7:

- B22: `758,790,964,225`
- B23: `751,601,943,807`
- worst cylinder ratio: `0.990528966659399027`

Q8:

- B22: `750,528,152,486`
- B23: `743,154,586,708`
- worst cylinder ratio: `0.990180428109379555`

Q9:

- B22: `731,875,202,312`
- B23: `724,265,254,549`
- worst cylinder ratio: `0.989792774665962755`

Again every positive cylinder contracts and none stays equal.

Therefore the observed B-axis contraction survives restoration of the finite affine correction terms at B23.

## 8. DSD logical-chain interpretation

The updated chain is

1. Formation: ternary selector cylinder.
2. State coordinates: dyadic forward residue plus ternary endpoint residue.
3. State compression: replace the reverse path tree by the potential `Lambda_Q(z)` and tie correction.
4. Dynamics: increase B and test successive forward endpoints against the compressed reverse potential.
5. Static aggregation: exact high-selector multiplicity DP.
6. Closure quantity: worst-cylinder B-block contraction norm.

The preferred theorem target is now a B-axis bounded-block contraction, not a Q-axis one-step contraction.

A sufficient form would be:

There exist fixed `r` and `sigma<1` and a scale threshold such that every surviving describable cylinder obeys

\[
\mu(S_{Q,B+r}\cap C)
\le
\sigma\,\mu(S_{Q,B}\cap C)
\]

uniformly in the large-scale parameter.

The finite data currently suggest `r=2` as the first candidate because the tested two-step worst ratios lie near `0.966-0.971`.

## 9. Remaining proof gap

The finite B-axis rule is not yet an asymptotic theorem.

The next required tasks are:

1. extend the root/dyadic resolution so B24 and beyond can be certified without endpoint-parity ambiguity;
2. test whether the two-step B contraction remains bounded away from one as H and m increase;
3. express the reverse potential recursion as a transfer/operator inequality rather than a finite table;
4. prove that the bound is uniform across the general m-family, not only m44;
5. reconnect that uniform family statement to the full minimal-counterexample branch.

An H25/B24 computation was started during this audit but not completed, so no B24 numerical claim is recorded here.
