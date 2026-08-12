# Transition-conditioned overlapping-window capacity theorem

Date: 2026-08-12

Status: **exact finite-state strengthening of the overlapping-window theorem at the current first unresolved upper-CF resonance**. It replaces the coarse free-height assignment count by the exact skew-transition language and raises the universal defect floor to about `15.97%`. This does not prove Collatz.

## 1. Setup

Use the current first-crossing resonance

\[
A=217,976,794,617,
\qquad
H=137,528,045,312,
\]

with

\[
\gamma=\log_2 3,
\qquad
\kappa_q=\lfloor q\gamma\rfloor,
\qquad
h_q=\kappa_q-a_q\ge0.
\]

Let

\[
r_*:=\#\{q:0\le q<H,\ h_q>0\}.
\]

The rational DK certificate gives

\[
N<U_{m cert}:=36,797,925,187,243,805,015,225.
\]

At every zero-defect odd event,

\[
x_q<2\left(N+\frac H3\right)<2^{76}.
\]

The last inequality is certified by the exact integer margin

\[
3\,2^{76}-\left(6U_{\rm cert}+2H\right)
=5,886,040,054,005,084,075,434>0.
\]

## 2. Length-48 zero-endpoint windows

Take odd-event windows of length

\[
\boxed{m=48.}
\]

For zero endpoints

\[
h_q=h_{q+48}=0,
\]

the exact parity length is

\[
D=\kappa_{q+48}-\kappa_q.
\]

The length-48 critical valuation language has exactly `49` Sturmian factors. Their parity lengths are

\[
\boxed{
45\text{ factors with }D=76,
\qquad
4\text{ factors with }D=77.
}
\]

In particular

\[
D\ge76.
\]

Since every zero-defect start is below `2^76`, one exact local parity word can occur at most once among such starts: the parity-vector bijection fixes one residue modulo `2^D`, and the ordinary representative is already smaller than that modulus.

Therefore the capacity of low-defect windows is exactly controlled by the number of admissible local `(critical factor, skew path)` pairs.

## 3. Exact skew-transition language

For a critical valuation factor

\[
r_0,r_1,\ldots,r_{47}\in\{1,2\},
\]

the actual valuations satisfy

\[
v_i=r_i+h_i-h_{i+1}\ge1.
\]

Equivalently,

\[
\boxed{
h_{i+1}\le h_i+r_i-1.}
\]

For a zero-endpoint window impose

\[
h_0=h_{48}=0,
\qquad
h_i\ge0.
\]

Unlike the earlier coarse count, upward motion is therefore allowed only when the corresponding critical symbol is `r_i=2`.

For each of the 49 critical factors, define a finite dynamic program whose state after transition `i` is

\[
(h,j),
\]

where `h` is the current skew height and `j` is the number of positive internal skew coordinates seen so far.

The transition is simply

\[
0\le h'\le h+r_i-1.
\]

At the final transition force

\[
h'=0.
\]

Summing the exact integer counts over all 49 critical factors gives the number `C_j` of admissible local factor/skew pairs with exactly `j` positive internal defect positions.

The first capacities are

\[
\boxed{
\begin{array}{c|r}
j&C_j\\\hline
0&49\\
1&1,347\\
2&19,165\\
3&187,947\\
4&1,427,613\\
5&8,949,601\\
6&48,184,982\\
7&228,960,996\\
8&979,315,195\\
9&3,827,089,672\\
10&13,824,443,522\\
11&46,590,088,990
\end{array}
}
\]

These are already safe window capacities because every exact local word can occur at most once below the state bound.

Different `(critical factor,skew path)` pairs may still map to the same parity word, so using their pair count can only overestimate the true capacity and is therefore conservative.

## 4. Relation to the Catalan triangle

If the actual `r_i in {1,2}` pattern is ignored and upward motion is allowed at every step, the number of nonnegative skew paths with `n=m-1` internal positions and exactly `j` positive coordinates is the Catalan-triangle number

\[
\boxed{
B_{n,j}
=
\frac{n-j+1}{n+1}\binom{n+j}{j}.
}
\]

For `n=47`, multiplying by the 49 critical factors gives, for example,

\[
49B_{47,4}=11,224,675,
\]

whereas the transition-conditioned exact capacity is only

\[
C_4=1,427,613.
\]

Thus most formally possible Catalan paths are forbidden by the fixed Sturmian pattern of `r_i=1` positions at which skew height cannot rise.

## 5. Global incidence inequality

There are

\[
W=H-48
\]

length-48 windows with endpoints inside `0,...,H-1`.

At most `2r_*` of them have a positive defect at one of the two endpoints. Hence the number `E` of zero-endpoint windows satisfies

\[
\boxed{E\ge H-48-2r_*.}
\]

For each zero-endpoint window let `j(q)` be its number of positive internal defect positions. Every global positive defect belongs to the interior of at most `47` such windows, so

\[
\boxed{
\sum j(q)\le47r_*.
}
\]

Let `Phi(E)` be the minimum possible sum of window defect counts when there are `E` windows and at most `C_j` windows of cost `j`. Because the costs increase with `j`, `Phi` is obtained exactly by greedily filling `C_0,C_1,C_2,...`.

Every candidate must satisfy

\[
\boxed{
\Phi(H-48-2r_*)\le47r_*.
}
\]

## 6. Exact threshold

Exact integer evaluation gives the least admissible value

\[
\boxed{
r_*=21,960,410,645.}
\]

At this threshold,

\[
H-48-2r_*
=93,607,223,974,
\]

and

\[
\Phi=1,032,139,300,297,
\]

while

\[
47r_*=1,032,139,300,315.
\]

For `r_*-1` the inequality fails.

Therefore every candidate at the current resonance obeys

\[
\boxed{
r_*\ge21,960,410,645.}
\]

or equivalently

\[
\boxed{
\frac{r_*}{H}>0.1596795.
}
\]

Thus more than `15.96%` of all odd-event coordinates must depart from the critical mechanical cap.

## 7. Reproducibility without floating logarithms

The exact verifier is

`collatz/src/overlapping_window_defect_certificate.py`.

It uses

\[
\boxed{
\lfloor q\log_2 3\rfloor
=\operatorname{bit\_length}(3^q)-1
}
\]

so no floating point or logarithm evaluation is required to generate the critical valuation word.

The verifier:

1. collects exactly `49` distinct length-48 critical factors, using the classical Sturmian complexity `p(48)=49` as the stopping certificate;
2. reproduces the parity-length split `76:45, 77:4`;
3. computes every transition-conditioned `C_j` with exact integers;
4. verifies the threshold incidence inequality and failure at the previous integer.

## 8. Correction-loss consequence

The independently audited defect-run theorem gives

\[
\eta
=\frac13\mathfrak D_H
\ge\frac5{48}r_*.
\]

Hence

\[
\boxed{
\eta
\ge
\frac5{48}\,21,960,410,645
=2,287,542,775.520833\ldots
}
\]

and the DK first-crossing ceiling improves to approximately

\[
\boxed{
N<3.4252261958\times10^{22}.
}
\]

This is well below the already eliminated `m=46` layer. The three lower recursive affine blocks remain because their starts are much smaller and therefore have substantially larger real correction allowance.

## 9. Structural consequence

The key point is stronger than the numerical `15.96%` value.

The earlier sparse-defect problem has now become a **finite local-language capacity problem**:

\[
\boxed{
\text{global low defect density}
\Rightarrow
\text{too many low-cost overlapping windows}
\Rightarrow
\text{more local parity words than the exact Sturmian/skew automaton can realize below the state modulus}.
}
\]

The obstruction is deterministic and uses simultaneously:

- Sturmian factor complexity;
- the exact skew-transition rule;
- the parity-vector residue modulus;
- the ordinary state bound;
- and global overlap incidence.

No random-parity or independence assumption is present.

## 10. Remaining target

Pure defect-density pressure is now strong enough to remove the high-start `m=46` layer but not the three lower recursive affine blocks. Those blocks require a true cross-base bridge.

The next useful target is to apply the same finite local-language idea not merely to state magnitude, but to the pair of exact boundary addresses:

\[
\text{dyadic start cylinder}
\quad\text{and}\quad
\text{ternary endpoint cylinder}.
\]

A two-ended window capacity could be much smaller than the one-ended parity capacity used here, because one local word translates both a start residue modulo a power of two and an endpoint residue modulo a power of three.
