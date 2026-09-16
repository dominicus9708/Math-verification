# Denjoy--Koksma / Ostrowski sharpening of inherited defect-run cost

Date: 2026-08-10

Status: **EXTERNAL-THEOREM APPLICATION + DERIVED RUN BOUND + EXACT FINITE CERTIFICATES**

This note sharpens the terminal inherited-defect analysis at the isolated first-crossing resonance

\[
(q,\sigma)=(137,528,045,312,217,976,794,617)
\]

and the `m=46`, high-four-trit `1000` branch.

It also corrects a one-transition indexing overestimate in the provisional amplitude formulas.  No Collatz proof is claimed.

## 1. Mechanical rotation weights

Put

\[
\beta=\log_2(3/2),
\qquad
u(x)=\frac13 2^{-x},\quad 0\le x<1,
\]

and extend `u` periodically to the circle.  The mechanical normalized correction weights are

\[
u_i=\nu(\{i\beta\})
=\frac13 2^{-\{i\log_2 3\}}.
\]

The circle mean and total variation are

\[
\boxed{
\int_0^1\nu(x)\,dx=\frac1{6\ln2},
}
\]

\[
\boxed{
\operatorname{Var}(\nu)=\frac13.
}
\]

The variation includes both the monotone variation on `[0,1)` and the periodic jump at the endpoint.

## 2. External theorem used

The classical Denjoy--Koksma inequality gives, for every convergent denominator `q_j` of the irrational rotation `beta` and every starting phase `theta`,

\[
\left|
\sum_{n=0}^{q_j-1}\nu(\theta+n\beta)
-\frac{q_j}{6\ln2}
\right|
\le\frac13.
\]

If an arbitrary positive integer `L` has Ostrowski expansion

\[
L=\sum_j b_jq_j,
\]

splitting the orbit segment into the corresponding shifted convergent blocks gives

\[
\boxed{
\sum_{n=0}^{L-1}\nu(\theta+n\beta)
\ge
\frac{L}{6\ln2}
-\frac13\sum_jb_j.
}
\]

This is an application of standard external continued-fraction dynamics, not a project novelty claim.

## 3. Exact continued fraction and finite digit-sum bound

Exact rational intervals for `ln 2` and `ln 3`, obtained from the positive atanh series already used by the project, certify the continued fraction

\[
\beta=[0;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,\ldots].
\]

The relevant convergent denominator is

\[
\boxed{q_{16}=53,715,833.}
\]

The corrected elementary run-average estimate gives an a-priori inherited-amplitude ceiling below `24,385,762`, hence every terminal level-run needed in the subsequent argument has length below

\[
41,685,061<q_{16}.
\]

An exhaustive greedy Ostrowski-expansion check over

\[
0\le L\le42,000,000
\]

finds

\[
\boxed{
\max\sum_jb_j=92,
}
\]

first attained at

\[
\boxed{L=32,025,449.}
\]

Therefore every relevant shifted run obeys the certified uniform bound

\[
\boxed{
\sum_{n=0}^{L-1}\nu(\theta+n\beta)
\ge
\frac{L}{6\ln2}-\frac{92}{3}.
}
\]

The finite maximization is computational but exact.

## 4. Correct point/transition indexing

Let a terminal defect have amplitude `z`.  For a level `1<=s<z`, let `L_s` be the number of consecutive odd-position coordinates in the terminal connected component of

\[
E_s=\{i:z_i\ge s\}.
\]

The first point of this run may already have amplitude exactly `s`.  To reach terminal amplitude `z`, the remaining `L_s-1` transitions must contain at least `z-s` allowed `+1` defect-growth events.

A `+1` event is possible only at a mechanical gap-two transition.  Since the exact rational logarithm bounds give

\[
\beta<\frac{117}{200},
\]

the number of gap-two transitions in any block of `L_s-1` transitions is less than `beta(L_s-1)+1`.  Hence

\[
\boxed{
L_s>
1+\frac{200}{117}(z-s-1)
\qquad(1\le s<z).
}
\]

For the top level, trivially `L_z>=1`.

This is the corrected version of the provisional expression that effectively used one transition too many.  The correction changes only an additive constant, not the asymptotic slope.

## 5. Level-set decomposition of correction loss

Because

\[
1-2^{-z_i}=\sum_{s=1}^{z_i}2^{-s},
\]

the correction loss has the exact layer decomposition

\[
\Delta S
=
\sum_{s\ge1}2^{-s}
\sum_{i:z_i\ge s}u_i.
\]

Using only the terminal component of each level set, the corrected run-length bound, and the DK/Ostrowski run estimate gives

\[
\boxed{
\Delta S>
\frac{1}{6\ln2}
\left[
1-2^{-z}
+\frac{200}{117}
\left(z-3+2^{2-z}\right)
\right]
-
\frac{92}{3}(1-2^{-z}).
}
\]

A simpler safe consequence for `z>=3` is

\[
\boxed{
\Delta S>
\frac{1}{6\ln2}
\left(1+\frac{200}{117}(z-3)\right)
-
\frac{92}{3}.
}
\]

The linear coefficient is

\[
\boxed{
\frac{100}{351\ln2}
\approx0.41102422817,
}
\]

compared with the earlier elementary run-average coefficient

\[
\frac{125}{351}\approx0.35612535613.
\]

Thus long inherited amplitudes cost about fifteen percent more correction than the previous phase-independent bound detected.

## 6. `1000` adjacent-terminal amplitude ceiling

The `1000` adjacent-two-defect case has the exact lower near-return difference

\[
d\ge20,971,503
\]

and minimum start

\[
X_{\min}=36,764,780,348,188,152,694,227.
\]

Combining the exact rational DK upper correction certificate, the lower logarithmic crossing gap, and the corrected run bound gives

\[
\boxed{z\le21,128,727.}
\]

This replaces the earlier provisional `24,750,138` cutoff.

## 7. Updated bounded discrete-log scan

The exact adjacent-pair congruence remains

\[
G(3\,2^{-z}+2\,2^{-w}-5)
\equiv4S_{22}+K\pmod{3^{30}},
\]

with

\[
1\le w\le z,
\qquad
S_{22}\in\mathcal C_{22}.
\]

Using `r=z-w` and the exact base-two discrete-log reduction modulo `3^30`, the corrected amplitude interval gives:

- `r` values with at least one raw hit:
  \[
  \boxed{3,071,912};
  \]
- raw `(r,w,S_22)` pairs:
  \[
  \boxed{3,411,199};
  \]
- maximum raw target multiplicity for one `r`: `6`.

A second exact scanner uses only safe rational simplifications

\[
U_S<33,068,504,827,
\qquad
\Lambda_->\frac{898654}{10^{18}},
\qquad
\frac1{6\ln2}>\frac{240449}{10^6}
\]

and the `92/3` Ostrowski error.  It leaves

\[
\boxed{730,578}
\]

budget-compatible `(r,w,S_22)` pairs.

After merging repeated terminal patterns with the same upper ternary state, the number of distinct compatible `S_22` states is

\[
\boxed{443,009}.
\]

Restoring every lower-18 ternary start still allowed by the safe budget gives the ordinary-start superset bound

\[
\boxed{2,525,428,246}.
\]

This is still too large for flat trajectory enumeration, but it is substantially below the earlier `~3.10e9` deduplicated superset and far below the original two-amplitude plane.

## 8. Minimum surviving adjacent amplitude

The same exact scan shows that both before and after the safe correction-budget filter, the smallest adjacent amplitude is

\[
\boxed{z=3232},
\]

with the corresponding second amplitude

\[
\boxed{w=994},
\qquad
r=z-w=2238.
\]

Consequently an exactly-two-terminal-defect candidate cannot create the first terminal defect locally.  The positive-defect run containing that first coordinate must extend backward for at least

\[
\boxed{5523}
\]

odd-position coordinates under the certified `beta<117/200` growth bound.

This is not a contradiction with the global defect budget; it is a new terminal-ancestry constraint.

## 9. Proof-program consequence

The current exactly-two-terminal-defect bottleneck has therefore been reduced to a finite structured set with three simultaneous properties:

1. one adjacent inherited terminal run with `z>=3232`;
2. one of `443,009` safe upper ternary states;
3. at most `2,525,428,246` ordinary starts after restoring the lower-18 choices.

Further flat scanning is not the preferred next step.  The next useful reduction should use the ordinary-integer / zero-lift condition on these already terminal-compatible states, or an exact block certificate that eliminates many lower-18 choices at once.

## References

External input should be cited as the classical Denjoy--Koksma inequality together with the Ostrowski expansion of integers for irrational rotations.  The project-specific defect process, terminal run decomposition, exact continued-fraction interval certificate, digit-sum maximum, and adjacent Collatz filters are derived or computationally certified here.