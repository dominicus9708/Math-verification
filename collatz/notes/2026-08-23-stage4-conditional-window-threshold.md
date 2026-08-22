# Stage 4 conditional-window threshold reduction

Date: 2026-08-23

Status: **the remaining cross-base target is reduced to a weak local conditional amplification bound. This is not a proof of the Collatz conjecture.**

## 1. Starting point

The current L=7 residue-maximal theorem gives a deterministic dyadic-language exclusion rate

\[
\eta>\frac7{50}=0.14.
\]

Thus it is sufficient to prove

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}{H}<\frac7{50},
\]

where \(\Xi_{m,H}\) is the exact same-integer overlap amplification between the reduced ternary-selector core and the coefficient-surviving, locally residue-maximal dyadic language.

The previous formulation asked for a global subexponential bound such as \(\Xi=2^{o(H)}\). That is much stronger than necessary.

## 2. Exact chain-rule decomposition

Use nested 28-step renewal-window events

\[
A_j=\{\text{the next 28 steps satisfy the required hard-language conditions}\}.
\]

After removing the one-time common mod-4 prefix factor, write the prefix-normalized amplification as \(\Xi^\circ\). For \(H=28n\), probability chain rule gives

\[
\Xi^\circ_{m,28n}
=
\prod_{j=1}^{n}K_j,
\]

with

\[
K_j
:=
\frac{\Pr_{\mathcal C_m}(A_j\mid A_1\cap\cdots\cap A_{j-1})}
{\Pr_{\rm dyadic}(A_j\mid A_1\cap\cdots\cap A_{j-1})}.
\]

For a non-multiple horizon \(H=28n+r\), \(0\le r<28\), only a bounded terminal factor is added and therefore does not affect the exponential rate.

Hence a uniform conditional-window bound \(K_j<K\) implies

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}H
\le\frac{\log_2K}{28}.
\]

## 3. A clean sufficient constant: K=15

It is enough to take

\[
\boxed{K_j<15\quad\text{for every normalized 28-step renewal window}.}
\]

Indeed,

\[
15^{25}<2^{98},
\]

so

\[
\frac{\log_2 15}{28}<\frac7{50}.
\]

Numerically,

\[
\frac{\log_2 15}{28}\approx0.139531807<0.14.
\]

Therefore even a repeated fifteen-fold conditional concentration per 28 steps is still too weak to repay the L7 deterministic exclusion budget.

Exact certificate:

`collatz/src/stage4_conditional_window_threshold_certificate.py`.

## 4. Margin relative to the current fresh-window theorem

The existing m=45 depth-28 transversality theorem proves, for the four remaining ordinary first-defect cylinders,

\[
\Xi_{\rm fresh}<\frac{76}{75}.
\]

Thus the new sufficient conditional target is more than fourteen times weaker in likelihood ratio:

\[
\frac{15}{76/75}=\frac{1125}{76}>14.
\]

In bit language, the current fresh-window repair cost is below \(1/50=0.02\) bit, whereas the L7 budget allows almost \(3.92\) repair bits per 28-step window.

So the globalization theorem does not need to preserve near-independence. It only needs to prevent repeated conditioning from creating an amplification of fifteen or more in every renewal window.

## 5. Equivalent total-variation target

The current depth-28 hard-set-independent theorem also has the baseline hard-fraction floor

\[
u\ge\frac3{64}.
\]

For a conditional selector measure \(\mu\) and the corresponding normalized dyadic measure \(\nu\), any hard event \(A\) with \(\nu(A)\ge u\) satisfies

\[
\frac{\mu(A)}{\nu(A)}
\le
1+\frac{\operatorname{TV}(\mu,\nu)}{u}.
\]

Therefore the much weaker conditional estimate

\[
\boxed{\operatorname{TV}(\mu,\nu)<\frac{21}{32}}
\]

already yields

\[
1+\frac{21/32}{3/64}=15.
\]

The current fresh-window theorem proves

\[
\operatorname{TV}<\frac1{1600}.
\]

The admissible conditional TV threshold is exactly

\[
\frac{21/32}{1/1600}=1050
\]

times larger. Hence there is a very large regularity-loss margin available during renewal conditioning.

## 6. Interaction with the credit/syndrome reduction

The height-credit phase cocycle already proves that after \(n\) first-return gates the ordinary renewal credit has only linear amplitude,

\[
|\delta_{\rm renewal}|=O(n),
\]

and therefore only \(O(\log n)\) excess information.

The exact depth-28 syndrome graph further shows that the current finite hard language has only three named exceptional states,

\[
E_{10},\ E_{18},\ E_{21},
\]

with all finite returns from \(E_{18}\) and \(E_{21}\) normalizing back into ordinary later hard states.

Consequently the next proof-level task is no longer to establish global independence or a zero overlap exponent directly. It is enough to establish a renewal renormalization statement ensuring that, after conditioning on previous windows and quotienting the already-controlled height/credit coordinates, each next normalized 28-step window still has

\[
K_j<15,
\]

or, more concretely when the \(3/64\) hard-fraction floor applies,

\[
\operatorname{TV}<\frac{21}{32}.
\]

## 7. Remaining gap

What is still unproved is the uniform transfer of the fresh-window transversality estimate through arbitrary previous renewal conditioning.

The target is now substantially weaker than before:

> **Conditional 28-step renewal transversality theorem.** After normalization at each renewal boundary, prove that the same-integer selector/dyadic likelihood ratio for the next hard 28-step window is uniformly less than 15, up to bounded initial and terminal factors.

A proof of this theorem would combine with the L7 exclusion rate to close the current Stage 4 exponential-budget inequality. Additional work would still be required to verify that every open positive-height excursion is covered by the same normalized renewal mechanism without introducing an independent exponential state multiplicity.
