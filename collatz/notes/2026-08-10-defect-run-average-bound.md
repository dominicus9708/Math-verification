# Defect-run average correction bound

Date: 2026-08-10

Status: **DERIVED LEMMA + FINITE PIECEWISE CHECK**

This note sharpens the first-crossing defect-density bound by using the actual transition constraint on defect runs. It does not prove Collatz or coefficient stopping globally.

## 1. Mechanical weights and defect runs

At first coefficient crossing, let

\[
\kappa_i=\lfloor i\log_2 3\rfloor,
\qquad
z_i=\kappa_i-d_i\ge0,
\]

and write the normalized mechanical correction weights as

\[
 u_i=\frac13 2^{-\{i\log_2 3\}}.
\]

Then

\[
S^*-S=\sum_i u_i(1-2^{-z_i}).
\]

For every defect position `z_i>0`,

\[
 u_i(1-2^{-z_i})\ge \frac12u_i.
\]

The odd-position admissibility rule gives

\[
z_{i+1}\le z_i+(\kappa_{i+1}-\kappa_i)-1.
\]

Hence a new positive defect run can start from `z_i=0` only when

\[
\kappa_{i+1}-\kappa_i=2.
\]

Put

\[
\beta=\log_2(3/2).
\]

At a defect-run start, the new rotation phase lies in `[0,beta)`.

## 2. Rotation form

For phase `r in [0,1)`, define

\[
 u(r)=\frac13 2^{-r},
\qquad
T(r)=\{r+\beta\}.
\]

The mechanical weights along a run are

\[
 u(r),u(T r),u(T^2r),\ldots
\]

with start phase `0<=r<beta`.

On every continuity interval determined by the finitely many breakpoints `{-j beta}`, a finite block sum is a positive constant times `2^{-r}` and is therefore decreasing in `r`. Thus its minimum is attained as a left limit at one of those breakpoints or at the endpoint of the allowed start interval.

Direct piecewise algebra gives the following exact minima.

For an arbitrary phase, a 5-block satisfies

\[
\boxed{
\sum_{j=0}^{4}u(T^jr)\ge \frac{421}{384}>\frac{25}{24}.
}
\]

For a legal run-start phase `0<=r<beta`, the initial block minima for lengths 2 through 6 are

\[
\begin{array}{c|ccccc}
L&2&3&4&5&6\\\hline
\min\sum_{j=0}^{L-1}u(T^jr)
&5/12&23/36&85/96&319/288&3038/2187
\end{array}
\]

and each is at least

\[
\frac{5L}{24}.
\]

For `L=1`, a legal run start has `r<beta`, so

\[
u(r)>\frac13 2^{-\beta}=\frac29>\frac5{24}.
\]

## 3. Uniform run-average lemma

Let a defect run have length `L>=1`.

If `L=1`, the preceding one-step bound applies.

If `L>=2`, choose

\[
s=2+((L-2)\bmod5),
\]

so `2<=s<=6` and `L-s` is divisible by five. The first `s` weights form a legal run-start block and every remaining block has length five with arbitrary starting phase. Therefore

\[
\sum_{\rm run}u_i
\ge
\frac{5s}{24}
+
\frac{5(L-s)}{24}
=
\boxed{\frac{5L}{24}}.
\]

Consequently every defect run obeys

\[
\boxed{
\frac1L\sum_{\rm run}u_i\ge\frac5{24}.
}
\]

The constant is sharp for this run-only argument because the legal length-two infimum is exactly `5/12`.

## 4. Defect-count consequence

Let

\[
N_{\rm def}=\#\{i:z_i>0\}.
\]

Summing the run-average bound over all disjoint defect runs and using `1-2^{-z_i}>=1/2` gives

\[
S^*-S
\ge
\frac12\sum_{z_i>0}u_i
\ge
\boxed{\frac5{48}N_{\rm def}}.
\]

Hence for any allowed correction-loss budget `A=S^*-S`,

\[
\boxed{
N_{\rm def}\le\frac{48}{5}A.
}
\]

This strictly improves the earlier pointwise estimate `N_def<=12A` by using the transition structure of the defect sequence.

## 5. Next unresolved convergent resonance

For

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617,
\]

the current Denjoy--Koksma start bound and the smallest `m=46` recursively-sufficient candidate imply the normalized correction-loss allowance

\[
A\lesssim1.2096147806253557\times10^9.
\]

Therefore

\[
N_{\rm def}
\lesssim
\frac{48}{5}A
<11,612,301,895.
\]

Dividing by `q`,

\[
\frac{N_{\rm def}}q<0.084435883.
\]

Thus a hypothetical paradoxical candidate in this layer must satisfy

\[
\boxed{
\frac{\#\{i:d_i=\kappa_i\}}q
>0.915564117.
}
\]

So more than `91.556%` of all odd positions must lie exactly on the mechanical cap.

This is a deterministic necessary condition for that resonance/layer, not a probabilistic statement.

## 6. Scope

The theorem uses only:

1. the first-crossing mechanical caps;
2. the exact nearest-neighbor defect transition;
3. the explicit rotation weights;
4. the external Denjoy--Koksma-based correction budget already derived elsewhere in the branch.

It does not yet exclude the resonance. The next target is to combine this high cap-density requirement with the small-start / 2-adic cylinder condition `x<2^75`.