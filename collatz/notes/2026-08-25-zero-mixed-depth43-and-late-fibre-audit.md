# m44 zero-mixed depth-43 obstruction and late-fibre audit

Date: 2026-08-25

Status: **exact finite strengthening + structural branch pruning. Stage 4 remains open.**

This note continues the current m=44 Stage 4 line after the all-height L=77 zero-mixed obstruction and the late-plateau skeleton-energy calculation. It separates three facts that should not be conflated:

1. the zero-mixed branch has an unexpectedly sharp ternary obstruction;
2. late plateau fibres have an exact selector-diameter collision rigidity;
3. converting all plateau orientations into ordered-one displacements is nevertheless too weak to close the current resonance.

This is not a proof of the Collatz conjecture.

## 1. Zero-mixed branch needs only 43 ternary digits

Let

\[
\widetilde{\mathcal Z}_{77}
\]

be the length-77 parity words satisfying coefficient survival at every prefix, every aligned seven-step block residue-maximal, and every Beatty plateau pair globally unmixed (`00` or `11`). No terminal equality is imposed.

The previous exact certificate gave

\[
|\widetilde{\mathcal Z}_{77}|=1,615,699,347
\]

and

\[
\widetilde{\mathcal Z}_{77}\cap\mathcal C_{44}=\varnothing.
\]

The new verifier resolves where the ternary incompatibility occurs.

For a canonical start below `2^73`, write

\[
Y=\frac{N-3}{4},
\qquad
 t=Y-3^{44}.
\]

The m44 selector condition is exactly

\[
0\le t\le\frac{3^{44}-1}{2}
\]

and every one of the 44 ternary digits of `t` belongs to `{0,1}`.

Among the zero-mixed language:

\[
\boxed{100,986,373}
\]

canonical starts lie below `2^73`, and

\[
\boxed{21,054,225}
\]

also lie in the ordinary convex hull of the m44 selector block.

Checking the ternary digits from low to high gives the exact ladder

\[
\begin{array}{c|r}
\text{digits already forced into }\{0,1\} & \text{remaining starts}\\\hline
0\ldots29 & 99\\
0\ldots34 & 14\\
0\ldots39 & 3\\
0\ldots41 & 1\\
0\ldots42 & 0
\end{array}
\]

Therefore the full 44-digit selector test is unnecessary:

\[
\boxed{
 t\bmod 3^{43}\notin C_{43}
}
\]

for every zero-mixed surviving L77 canonical start in the m44 convex hull.

Equivalently, the zero-mixed same-integer obstruction is already a depth-43 ternary obstruction.

Certificate:

`collatz/src/m44_zero_mixed_ternary_depth43_certificate.cpp`.

## 2. Unique final near miss

Exactly one zero-mixed start survives the ternary test through digit 41:

\[
\boxed{
N_\star=5,009,655,000,888,502,825,071.
}
\]

Its normalized selector coordinate is

\[
 t_\star=267,642,848,038,514,473,386.
\]

It has

\[
\boxed{
 t_\star=2\,3^{42}+c,
 \qquad c\in C_{42},
}
\]

with ternary digit 43 equal to zero and digit 42 equal to two.

Thus the final zero-mixed near miss is not rejected by a diffuse accumulation of small ternary errors. Forty-two lower selector digits are exactly legal and one high digit is exactly the forbidden value `2`.

This makes the zero-mixed obstruction much more structured than a generic density mismatch.

## 3. Why low positive mixed counts should not be brute-forced blindly

An exact DP for the whole survival+L7 language at L=77 gives

\[
1,896,504,911,397,252,601
\]

words. The zero-mixed slice is only about

\[
8.52\times10^{-10}
\]

of this language.

The cumulative exact language fractions are approximately

\[
\Pr(M\le6)=0.0010153491,
\]

\[
\Pr(M\le8)=0.0120606439,
\]

\[
\Pr(M\le10)=0.0740274643.
\]

A separate deterministic-seed Monte Carlo diagnostic over 100,000,000 m44 selector assignments found 5,000 survival+L7 prefixes at L=77 and already observed six with exactly six mixed plateau pairs.

This diagnostic is not proof evidence, but it is enough to reject the strategy of assuming that the exact zero-mixed exclusion will simply persist for all small positive mixed counts. The zero-mixed branch is arithmetically special.

## 4. Exact selector-diameter collision rigidity on late fibres

The complete m44 selector interval is

\[
N_{\min}=4\,3^{44}+3,
\qquad
N_{\max}=6\,3^{44}+1.
\]

Hence its diameter is

\[
D_{44}=2\,3^{44}-2
=1,969,541,804,367,222,465,760.
\]

Exact arithmetic gives

\[
\boxed{D_{44}<2^{71}}
\]

with gap

\[
2^{71}-D_{44}
=391,641,437,067,600,141,088.
\]

Now fix one deterministic plateau fibre and vary only mixed plateau coordinates with starts

\[
j\ge71.
\]

For two distinct fibre points, the least differing plateau coordinate gives a nonzero canonical-residue difference with 2-adic valuation equal to that least `j`, hence at least 71.

For selector points `X,X'` and fibre points `Y,Y'`, if

\[
X-X'+Y-Y'\equiv0\pmod{2^H},
\]

then `X-X'` is divisible by `2^71`. But

\[
|X-X'|<2^{71},
\]

so necessarily

\[
X=X'.
\]

The fibre difference must then vanish modulo `2^H`; the distinct-valuation triangularity forces

\[
Y=Y'.
\]

Therefore, for the uniform m44 selector measure and a `K`-point late fibre, the additive collision probability is exactly diagonal:

\[
\boxed{
\Pr[X-X'+Y-Y'\equiv0]=\frac1{2^{44}K}.
}
\]

Equivalently the weighted Fourier second moment gains the full selector factor `2^-44` in addition to the fibre factor `K^-1`.

This strengthens the earlier selector-independent `1/K` estimate.

Arithmetic audit:

`collatz/src/m44_late_fibre_collision_and_displacement_audit.py`.

## 5. Audit: why this still does not directly close first-order overlap

The diagonal collision theorem is a second-moment statement. A direct Cauchy--Schwarz conversion to the first-order same-integer amplification still pays the ambient-frequency factor, so this theorem alone does not imply

\[
\limsup_{H\to\infty}
\frac{\log_2\Xi_{44,H}}H<\frac7{50}.
\]

The stronger collision theorem is therefore retained as a component for a renormalized or block-transfer argument, not promoted to a Stage 4 closure.

## 6. Plateau-orientation / ordered-one branch is provably too weak

At the current isolated R1 resonance

\[
(A,H)
=(217,976,794,617,
137,528,045,312),
\]

take the time-expanded boundary length

\[
L=A-1.
\]

The upper-convergent relation gives

\[
b_{A-2}=H-1.
\]

Hence the number of deterministic plateau starts is exactly

\[
\boxed{
|P_L|=A-H-1=80,448,749,304.
}
\]

The earlier ordered-one rigidity theorem permits at most

\[
\boxed{
N_{\rm disp}\le126,613,628,698
}
\]

displaced ordered ones.

Therefore even the unrealistically strongest possible plateau-orientation conclusion -- every plateau coordinate being mixed and every one being forced to the displaced `10` orientation -- would give only

\[
80,448,749,304
<126,613,628,698.
\]

There remains slack

\[
\boxed{46,164,879,394}.
\]

Thus the single-step plateau-orientation count cannot close the present ordered-one displacement budget. This branch should be pruned rather than numerically optimized.

## 7. Refined remaining target

The useful information now has a sharper division.

Closed / retained:

1. zero-mixed m44 branch is impossible by depth 77;
2. that impossibility is already visible modulo `3^43`;
3. the last zero-mixed near miss is a single forbidden high ternary digit;
4. late-fibre additive energy is exactly diagonal against the m44 selector because its diameter is below `2^71`;
5. pure plateau-displacement counting cannot close the current resonance.

The next target should therefore use the zero-mixed ternary ladder as a **state variable**, not merely count mixed coordinates.

A suitable state is of the form

\[
(\text{L7/renewal state},
\text{mixed-coordinate phase},
\text{low ternary selector prefix / first forbidden digit}).
\]

The proof-level objective is to show that allowing mixed coordinates cannot repeatedly repair the ternary obstruction at a linear information rate. In Stage 4 language, one wants a finite-state transfer bound whose positive repair exponent remains below `7/50`.

This is more specific than the previous generic selector-weighted Fourier target: the zero-mixed calculation identifies a concrete 3-adic defect observable which can be carried through the mixed-coordinate transfer.
