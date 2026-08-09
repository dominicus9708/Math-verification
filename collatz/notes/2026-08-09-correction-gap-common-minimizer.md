# Correction-gap common-minimizer certificate for first coefficient crossing

Date: 2026-08-09

Status: **DERIVED FINITE CERTIFICATE + EXACT COMPUTATIONAL VERIFICATION THROUGH q <= 100**

This note advances the `Dangerous-Core Extremal Reduction` target from `mixed-interaction-reduction.md`.  It does **not** prove the target for all q and does not prove the Collatz conjecture or the coefficient-stopping conjecture globally.

## 1. Fixed first-crossing prefix class

Use the accelerated map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Fix an odd count q and its first coefficient-crossing depth

\[
\sigma=\lceil q\log_2 3\rceil,
\qquad
M=2^\sigma,
\qquad
P=3^q,
\qquad
D=M-P>0.
\]

Let \(\pi\) be a fixed dangerous-coordinate prefix of the admissible odd-position vector.  For every completion w of this prefix, write

\[
R(w)=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
\]

Let x(w) in \([0,M)\) be the canonical start residue and let

\[
y(w)=T^\sigma(x(w)),
\qquad
z(w)=x(w)-y(w).
\]

Then

\[
My=Px+R,
\]
so

\[
\boxed{Mz=Dx-R.}
\]

The prefix-constrained maximum correction is obtained by keeping the fixed prefix coordinates and setting every remaining odd position to its coordinatewise cap

\[
d_i^*=\lfloor i\log_2 3\rfloor.
\]

Denote this exact maximum by

\[
R_{\max,\pi}.
\]

## 2. Correction-gap window lemma

Suppose a completion \(w_*\) has the smallest canonical start in its prefix class:

\[
x_* = \min_{w\supset\pi} x(w).
\]

Put

\[
R_*=R(w_*),
\qquad
z_*=z(w_*).
\]

For every other completion w,

\[
z(w)=\frac{Dx(w)-R(w)}{M}
\ge
\frac{Dx(w)-R_{\max,\pi}}{M}.
\]

Since

\[
Mz_*=Dx_*-R_*,
\]
we obtain

\[
Dx-Mz_*
>D x_*+R_{\max,\pi}-R_*
\]
whenever

\[
x>x_*+\frac{R_{\max,\pi}-R_*}{D}.
\]

Therefore define the exact correction-gap width

\[
\boxed{
W_\pi
=
\left\lfloor
\frac{R_{\max,\pi}-R_*}{D}
\right\rfloor.
}
\]

Then every completion satisfying

\[
\boxed{x(w)>x_*+W_\pi}
\]
necessarily has

\[
\boxed{z(w)>z_*}.
\]

Consequently, after x-minimality of \(w_*\) is established, it is sufficient to inspect only the finite ordinary-integer window

\[
\boxed{
[x_*,x_*+W_\pi]
}
\]
for competing members of the same first-crossing prefix class.  If no member in that window has smaller z, then \(w_*\) is simultaneously a global x-minimizer and z-minimizer in the whole prefix class.

This is a deterministic certificate.  No probabilistic or equidistribution assumption enters.

## 3. Why this is different from global co-order

The stronger statement that x and z have the same ordering on the full safe tail is false.

At q=17, sigma=27 and dangerous prefix `(0,1)`, two admissible completions give

\[
(x,z)=(175263,6629)
\]
and

\[
(x,z)=(175271,6628).
\]

Thus x increases while z decreases.  The present lemma does not assert global monotonicity; it isolates only the finite window that can possibly challenge the x-minimizer for z-minimality.

## 4. First nontrivial dangerous-prefix test: q=29

Here

\[
q=29,
\qquad
\sigma=46,
\]

\[
M=70,368,744,177,664,
\]

\[
P=68,630,377,364,883,
\]

\[
D=1,738,366,812,781.
\]

The dangerous dimension is h(q)=3, and the admissible dangerous prefixes are

\[
\pi_1=(0,1,2),
\qquad
\pi_2=(0,1,3).
\]

### Prefix (0,1,2)

The first canonical start in the class is

\[
\boxed{x_*=3431},
\qquad
T^{46}(3431)=3349,
\qquad
\boxed{z_*=82}.
\]

The exact prefix correction maximum is

\[
R_{\max,\pi_1}=479,954,459,205,691.
\]

The correction-gap certificate gives

\[
\boxed{W_{\pi_1}=164},
\qquad
\boxed{U_{\pi_1}=3595}.
\]

An exact scan of the class inside `[3431,3595]` finds only the candidate 3431 itself.  Hence 3431 is the unique x- and z-minimizer of the entire prefix class.

### Prefix (0,1,3)

The first canonical start is

\[
\boxed{x_*=4891},
\qquad
T^{46}(4891)=4774,
\qquad
\boxed{z_*=117}.
\]

Here

\[
R_{\max,\pi_2}=490,121,922,519,007,
\]

and

\[
\boxed{W_{\pi_2}=127},
\qquad
\boxed{U_{\pi_2}=5018}.
\]

Again the exact class scan of `[4891,5018]` contains only 4891.  Therefore the Dangerous-Core Extremal Reduction target holds for both dangerous-prefix classes at q=29.

The q=29 calculation was independently reproduced in Wolfram Language using exact integers.

## 5. Exact finite verification through q <= 100

The same certificate was applied for every

\[
1\le q\le100.
\]

For each q:

1. compute \(\sigma,M,P,D\) by exact integer arithmetic;
2. compute the dangerous dimension
   \[
   h(q)=\#\{1\le i\le q:3^{q-i}\ge D\};
   \]
3. generate every admissible prefix of the first h(q) odd-position coordinates;
4. scan ordinary starts upward to locate the first member \(x_*\) of each class;
5. compute its exact \(R_*\), the exact \(R_{\max,\pi}\), and hence \(W_\pi\);
6. scan only through \(x_*+W_\pi\) and check the actual first-crossing class and descent margin z.

There are exactly

\[
\boxed{106}
\]
dangerous-prefix classes in this range.

No class fails the common-minimizer certificate.

The largest starting integer needed by any certificate is

\[
\boxed{4,551,664}.
\]

The largest correction-gap width is

\[
\boxed{W_{\max}=2249},
\]
attained in the q=94 prefix class

\[
(0,1,3,4).
\]

Selected nontrivial classes are:

| q | dangerous prefix | x* | y* | z* | W | U=x*+W |
|---:|:---|---:|---:|---:|---:|---:|
| 29 | (0,1,2) | 3431 | 3349 | 82 | 164 | 3595 |
| 29 | (0,1,3) | 4891 | 4774 | 117 | 127 | 5018 |
| 41 | (0,1,2,3) | 4591 | 4541 | 50 | 641 | 5232 |
| 41 | (0,1,2,4) | 20327 | 20098 | 229 | 619 | 20946 |
| 41 | (0,1,3,4) | 32027 | 31666 | 361 | 513 | 32540 |
| 82 | (0,1,2) | 393967 | 385043 | 8924 | 621 | 394588 |
| 82 | (0,1,3) | 4550939 | 4447795 | 103144 | 725 | 4551664 |
| 94 | (0,1,2,3) | 847871 | 839962 | 7909 | 2130 | 850001 |
| 94 | (0,1,2,4) | 2457447 | 2434519 | 22928 | 2152 | 2459599 |
| 94 | (0,1,3,4) | 432923 | 428885 | 4038 | 2249 | 435172 |

The window can contain another member without breaking the theorem.  For example, at q=34 and prefix `(0,1)`, the certificate window contains starts 47 and 63 with

\[
z(47)=1,
\qquad
z(63)=2,
\]

so the x-minimizer remains the z-minimizer.

A separate exact C++ verifier reproduces all 106 certificates.  On the current test environment it completes the two scans in well under one second; runtime is implementation-dependent and is not part of the mathematical claim.

## 6. Structural interpretation

The nominal number of admissible parity-position vectors grows extremely rapidly.  For q=29 alone there are

\[
38,036,848,410
\]
admissible first-crossing position vectors.

The correction-gap lemma avoids enumerating those vectors.  Once the least canonical start in a dangerous-prefix class is found, all but a short ordinary-integer interval are eliminated analytically by the exact inequality

\[
Mz=Dx-R.
\]

Thus the unresolved asymptotic target becomes narrower:

> Control the correction deficit
> \[
> R_{\max,\pi}-R(w_*)
> \]
> of the least canonical-start completion relative to the Diophantine gap
> \[
> D=2^\sigma-3^q.
> \]

If one could prove a uniform usable bound on

\[
\boxed{
\frac{R_{\max,\pi}-R(w_*)}{D},
}
\]
then Dangerous-Core Extremal Reduction would reduce to a correspondingly short deterministic start window instead of a high-dimensional parity enumeration.

## 7. Relation to external Collatz work

Rozier--Terracol's parity-vector majorization controls the remainder/correction side and frames the first coefficient crossing through coefficient stopping and paradoxical sequences.  The present certificate retains that external arithmetic setting but follows a separate route on the canonical-start/descent-margin pair `(x,z)`: it asks how far the x-minimizer can be from the z-minimizer after the dangerous coordinates are fixed.

No novelty claim is made here.  The exact correction-gap lemma and the q<=100 finite certificate should be literature-checked more broadly before any publication claim.

## 8. Next target

The next proof-oriented target is not global x-z co-order.  That is already false.

A more plausible target is a **uniform correction-gap window theorem**: find an explicit function G(q), preferably subexponential and ideally polynomial/logarithmic on the dangerous core, such that for every first-crossing dangerous-prefix class

\[
\boxed{
R_{\max,\pi}-R(w_*)\le D\,G(q).
}
\]

Then the only possible z-competitors lie in

\[
[x_*,x_*+G(q)].
\]

This would convert a q-dimensional extremal problem into a short one-dimensional ordinary-integer exclusion problem and interfaces directly with the exact record/minimal-survivor machinery already present in the repository.
