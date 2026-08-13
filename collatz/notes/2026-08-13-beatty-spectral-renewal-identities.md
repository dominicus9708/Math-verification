# Exact spectral-renewal identities for the Beatty coefficient-survival language

Date: 2026-08-13

Status: **exact finite-group identities at arbitrary depth**. These formulas describe how the Fourier spectrum of the coefficient-survivor residue set changes across Beatty plateau and barrier-rise steps. They are symbolic-language identities, not a Collatz proof.

## 1. Survivor residue sets

Put

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil \alpha L\rceil.
\]

Because the recursively sufficient core has `N=3 mod 4`, use the reduced coordinate

\[
N=4Y+3.
\]

At binary depth `L>=2`, let

\[
M_L:=2^{L-2}
\]

and let

\[
R_L\subseteq\mathbb Z/M_L\mathbb Z
\]

be the reduced residues whose first `L` parity symbols satisfy

\[
q_j\ge b_j
\qquad(1\le j\le L).
\]

A parent `r mod M_L` has two children modulo

\[
M_{L+1}=2M_L:
\qquad
r,\quad r+M_L.
\]

Write

\[
f_L:=1_{R_L}.
\]

Use the unnormalized discrete Fourier transform

\[
\widehat f_L(t)
:=
\sum_{r=0}^{M_L-1}
f_L(r)e^{-2\pi itr/M_L}.
\]

## 2. Plateau step

Suppose

\[
\boxed{b_{L+1}=b_L.}
\]

Every coefficient-surviving parent has **both** children surviving, because the required odd-count threshold does not increase.

Hence

\[
\boxed{
R_{L+1}
=\pi^{-1}(R_L),
}
\]

where `pi:Z/(2M_L)Z -> Z/M_L Z` is reduction modulo `M_L`.

For frequency `k mod 2M_L`, pair the two children of every parent:

\[
\begin{aligned}
\widehat f_{L+1}(k)
&=
\sum_{r\in R_L}
e^{-2\pi ikr/(2M_L)}
\left(1+e^{-\pi i k}\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\widehat f_{L+1}(k)=0
\qquad(k\text{ odd}),
}
\]

and

\[
\boxed{
\widehat f_{L+1}(2t)
=2\widehat f_L(t).
}
\]

Thus a plateau step annihilates the entire newly exposed odd-frequency spectrum **exactly**.

## 3. Barrier-rise step

Now suppose

\[
\boxed{b_{L+1}=b_L+1.}
\]

Let

\[
B_L
:=
\{r\in R_L:q_L(r)=b_L\}
\]

be the one-child boundary layer.

Every parent in `R_L\B_L` has two surviving children. Every parent in `B_L` has exactly one surviving child.

For `r in B_L`, define the orientation

\[
v_L(r)=
\begin{cases}
+1,&r\text{ (lower child) survives},\\
-1,&r+M_L\text{ (upper child) survives}.
\end{cases}
\]

Extend this to the child group anti-periodically:

\[
\boxed{
w_L(r)=v_L(r),
\qquad
w_L(r+M_L)=-v_L(r),}
\]

and put `w_L=0` away from boundary child pairs.

## 4. Odd-frequency generation identity

The full two-child lift of `R_L` has zero Fourier coefficient at every odd child frequency, by the plateau calculation.

At a boundary pair, the actual survivor set is obtained by deleting the rejected child. For odd `k`, the two child characters are negatives of each other, and a direct two-point calculation gives

\[
\widehat{1_{\{\text{rejected child}\}}}(k)
=-\frac12\widehat w_L(k)
\]

when summed over all boundary pairs.

Consequently

\[
\boxed{
\widehat f_{L+1}(k)
=\frac12\widehat w_L(k)
\qquad(k\text{ odd}).
}
\]

Thus the oriented Beatty-boundary spectrum is **exactly the new odd spectrum generated at a barrier rise**.

## 5. Even-frequency recursion at a rise

For an even child frequency `k=2t`, the two children of one parent have the same character. The full two-child lift contributes

\[
2\widehat f_L(t).
\]

Deleting one child from every boundary parent subtracts exactly the parent boundary transform

\[
\widehat{1_{B_L}}(t).
\]

Therefore

\[
\boxed{
\widehat f_{L+1}(2t)
=
2\widehat f_L(t)
-
\widehat{1_{B_L}}(t).
}
\]

Together with Section 4, this is a complete Fourier recursion from depth `L` to `L+1`.

## 6. Spectral-renewal interpretation

The Beatty increment word

\[
b_{L+1}-b_L\in\{0,1\}
\]

alternates between two types of spectral operations:

### Plateau

\[
\boxed{
\text{new odd spectrum}=0.
}
\]

### Rise

\[
\boxed{
\text{new odd spectrum}
=\frac12\times
\text{oriented boundary spectrum}.
}
\]

Hence high-resolution survivor spectrum is not generated continuously. It is periodically reset on the newly exposed odd frequencies and regenerated only by the Beatty boundary.

This is the exact structural reason that the oriented boundary transform is the relevant harmonic object in the mass-transport error.

## 7. Connection to signed mass transport

For a ternary selector count distribution `c_x` on the child group, the signed correction is

\[
K_L
=\sum_x c_xw_L(x).
\]

At odd frequencies, Section 4 gives

\[
\widehat w_L(k)=2\widehat f_{L+1}(k).
\]

Therefore

\[
\boxed{
K_L
=\frac1{M_L}
\sum_{k\text{ odd}}
\widehat c(k)
\overline{\widehat f_{L+1}(k)}
}
\]

under the unnormalized-transform convention, after using the anti-periodicity that removes even frequencies.

Thus the cross-base transport error is an overlap between the ternary spectrum and precisely the **new spectral component** created by the next coefficient-survivor refinement.

## 8. Verification

The identities were independently checked by exact survivor-set construction at small depths and direct complex DFT evaluation. The numerical residuals are at floating-roundoff scale.

The proof above is algebraic and does not depend on those numerical checks.

## 9. Next theorem target

The recurrence suggests a block proof strategy:

1. plateau steps kill newly exposed odd frequencies exactly;
2. rise steps regenerate them from a smaller boundary layer;
3. repeated rise/plateau blocks may therefore admit a contraction estimate for normalized survivor Fourier coefficients.

A uniform block estimate would directly support the spectral-complementarity route without requiring the ternary selector measure itself to mix uniformly at near-linear resolution.
