# Beatty one-child exposure + selector repair: cumulative contraction bridge

Date: 2026-09-06

Status: **SAFE CONDITIONAL LEMMA + FINITE CERTIFICATE + OPEN ASYMPTOTIC GATE.**

This note combines the latest Beatty one-child exposure bound with the selector min/max child-repair lemma.  It closes the previously stated *dynamic exposure* question at the coefficient-survivor level, but it does **not** prove the Collatz conjecture.  The remaining burden is an asymptotic selector-mixing theorem on the exact canonical candidate fibres and, after mass decay is obtained, the terminal minimal-counterexample/globalization step.

---

## 1. Inputs already established

Let

\[
\alpha=\log_3 2,
\qquad
b_L=\min\{q:3^q\ge 2^L\}=\lceil \alpha L\rceil.
\]

Call `L` a **rise** when

\[
b_{L+1}=b_L+1.
\]

For the coefficient-survivor set `R_L`, let `D_L` be the one-child parent boundary at a rise.  The latest Beatty exposure result gives

\[
\boxed{
\frac{|D_L|}{|R_L|}
\ge
\frac{2b_L+1-L}{(b_L+1)L}
>
\frac{2}{5L}.
}
\]

Status: **SAFE LEMMA**, with an independent exact finite certificate through `L=1500`.

Now let `C(x)` be the exact selector multiplicity on the child modulus and suppose

\[
0<a\le C(x)\le B.
\]

Put

\[
\rho=\frac{a}{B}.
\]

For a parent residue `r`, define

\[
c(r)=C(r)+C(r+M).
\]

The selector min/max child-repair lemma gives, for any one-child parent set `D`,

\[
\boxed{
\text{fraction of selector mass lost inside }D
\ge
\delta(\rho)
:=
\frac{3\rho-1}{4\rho}
}
\]

whenever

\[
\rho>\frac13.
\]

Status: **SAFE LEMMA**.

---

## 2. New bridge: unweighted exposure to selector-weighted exposure

For any `D\subseteq R`,

\[
S_D:=\sum_{r\in D}c(r),
\qquad
S_R:=\sum_{r\in R}c(r).
\]

Since

\[
2a\le c(r)\le 2B,
\]

we have

\[
S_D\ge 2a|D|,
\qquad
S_R\le 2B|R|.
\]

Hence

\[
\boxed{
\frac{S_D}{S_R}
\ge
\rho\frac{|D|}{|R|}.
}
\]

Applying the Beatty exposure bound at a rise,

\[
\boxed{
\frac{S_{D_L}}{S_{R_L}}
>
\frac{2\rho}{5L}.
}
\]

This is the exact place where the coefficient-survivor geometry and selector multiplicity interact.

Status: **SAFE LEMMA**, provided `C` is the exact counting weight on the same candidate fibre represented by `R_L`.

---

## 3. One-rise total loss

The one-child repair lemma loses at least the fraction

\[
\delta(\rho)=\frac{3\rho-1}{4\rho}
\]

of the selector mass carried by `D_L`.

Therefore the total normalized selector-candidate mass loses at least

\[
\delta(\rho)
\frac{S_{D_L}}{S_{R_L}}
>
\frac{3\rho-1}{4\rho}
\frac{2\rho}{5L}.
\]

The factor `rho` cancels:

\[
\boxed{
\text{total loss at a rise}
>
\frac{3\rho-1}{10L}.
}
\]

Thus if a scaling family has a horizon-independent bound

\[
\boxed{
\rho_L\ge\rho_0>\frac13,
}
\]

then with

\[
\kappa:=\frac{3\rho_0-1}{10}>0,
\]

we obtain the rise-step contraction

\[
\boxed{
\mu_{L+1}
\le
\left(1-\frac{\kappa}{L}\right)\mu_L
}
\]

for the correctly normalized candidate mass.

Status: **SAFE CONDITIONAL LEMMA**.

The condition `rho_0>1/3` is the only asymptotic selector-flatness threshold required by this route.  Full equidistribution is unnecessary.

---

## 4. Rise steps have divergent harmonic exposure

Let

\[
e_L=b_{L+1}-b_L\in\{0,1\}.
\]

Then

\[
E(N):=\sum_{L=1}^N e_L
=b_{N+1}-b_1
=\lceil\alpha(N+1)\rceil-1.
\]

Hence

\[
E(N)=\alpha N+O(1).
\]

More precisely,

\[
E(N)\ge \alpha N-(1-\alpha).
\]

By summation by parts,

\[
\sum_{L=1}^N\frac{e_L}{L}
=
\frac{E(N)}{N}
+
\sum_{L=1}^{N-1}E(L)
\left(\frac1L-\frac1{L+1}\right).
\]

Substituting the discrepancy bound gives

\[
\boxed{
\sum_{\substack{L\le N\\L\text{ rise}}}\frac1L
\ge
\alpha H_N-(1-\alpha).
}
\]

Therefore

\[
\sum_{L\text{ rise}}\frac1L=\infty.
\]

An entirely elementary numerical-free lower constant is also available because

\[
3^5=243<256=2^8
\quad\Longrightarrow\quad
\alpha>\frac58.
\]

Thus

\[
\boxed{
\sum_{\substack{L\le N\\L\text{ rise}}}\frac1L
\ge
\frac58 H_N-\frac38.
}
\]

Status: **SAFE LEMMA**.

---

## 5. Conditional polynomial candidate-mass decay

Combine Sections 3 and 4.  At non-rise steps use only the normalized non-expansion property of the candidate transport; at rise steps use the loss factor.

Then

\[
\frac{\mu_{N+1}}{\mu_1}
\le
\prod_{\substack{L\le N\\L\text{ rise}}}
\left(1-\frac{\kappa}{L}\right).
\]

Using `1-x\le e^{-x}`,

\[
\frac{\mu_{N+1}}{\mu_1}
\le
\exp\left(
-\kappa
\sum_{\substack{L\le N\\L\text{ rise}}}\frac1L
\right).
\]

Hence

\[
\boxed{
\mu_{N+1}
\le
C(\rho_0)\,N^{-\kappa\alpha}\mu_1,
\qquad
\kappa=\frac{3\rho_0-1}{10}.
}
\]

In particular,

\[
\boxed{
\rho_0>\frac13
\quad\Longrightarrow\quad
\mu_N\to0
}
\]

under the exact-fibre and normalized-transport compatibility assumptions above.

Status: **SAFE CONDITIONAL LEMMA**.

This is a polynomial-decay route, not a geometric-decay route.  Polynomial decay is sufficient to force candidate density/mass to zero, but not by itself to prove emptiness of the infinite canonical candidate set.

---

## 6. Finite-scale diagnostics already in the repository

The existing exact selector-DP extrema give:

\[
\begin{array}{c|c|c|c}
\text{case}&\rho&\kappa=(3\rho-1)/10&\kappa\alpha\\\hline
H24\_full&0.9972718937&0.1991815681&0.1256695777\\
H25\_full&0.9956608777&0.1986982633&0.1253646463\\
H24,Q7&0.9557318856&0.1867195657&0.1178069296\\
H24,Q8&0.9403365328&0.1821009598&0.1148929137\\
H24,Q9&0.9116961789&0.1735088537&0.1094718983\\
H25,Q7&0.9352951604&0.1805885481&0.1139386882
\end{array}
\]

These numbers are **FINITE CERTIFICATES ONLY**.  They show that the finite tested selector distributions are comfortably above the threshold `rho=1/3`; they do not establish a horizon-independent lower bound.

The combined exact product through `L=1500`, using each finite rho merely as a diagnostic constant, is approximately:

\[
\begin{array}{c|c}
\text{case}&\prod_{L\le1500,\,L\text{ rise}}(1-\kappa/L)\\\hline
H24\_full&0.34657\\
H25\_full&0.34749\\
H24,Q7&0.37103\\
H24,Q8&0.38050\\
H24,Q9&0.39873\\
H25,Q7&0.38365
\end{array}
\]

Again these are diagnostics, not asymptotic proof constants.

Reproducibility certificate:

`collatz/src/beatty_repair_cumulative_contraction_certificate.py`

---

## 7. DSD analysis: dependency compression

Before this bridge, the local structure was recorded as two separate questions:

\[
\text{one-child exposure}
\quad+\quad
\text{cross-base repair control}.
\]

The latest Beatty theorem supplies the first in the coefficient-survivor language.  The selector min/max lemma supplies the second for arbitrary one-child orientation.

Their exact dependency compression is therefore

\[
\boxed{
\begin{array}{c}
\text{Beatty rise exposure } |D_L|/|R_L|>2/(5L)\\
+\\
\text{selector min/max }\rho_L>1/3\\
+\\
\text{exact fibre/transport compatibility}\\
\Downarrow\\
\text{rise loss }>(3\rho_L-1)/(10L)\\
\Downarrow\\
\text{harmonic accumulation}\\
\Downarrow\\
\text{polynomial candidate-mass decay}
\end{array}
}
\]

This route no longer needs a positive one-child fraction at *every* step.  A `1/L` exposure at the Beatty rise subsequence is enough because the rise harmonic sum diverges.

---

## 8. DSD audit

### 8.1 SAFE LEMMAS

1. Beatty rise indicator has bounded discrepancy and positive asymptotic density.
2. Rise harmonic sum diverges.
3. Min/max selector weighting transfers unweighted exposure by a factor at least `rho`.
4. Repair loss on the exposed selector mass is `delta(rho)=(3rho-1)/(4rho)`.
5. Combined total rise loss simplifies exactly to `(3rho-1)/(10L)`.
6. Uniform `rho_0>1/3` implies polynomial decay of the normalized candidate mass.

### 8.2 FINITE CERTIFICATES

1. Beatty exposure inequality checked exactly through `L=1500`.
2. Number of rise steps through `L=1500`: `947`.
3. Existing H24/H25 selector extrema all satisfy `rho>1/3` by a wide margin.
4. The new combined certificate checks the algebra and finite cumulative products exactly with rational arithmetic.

### 8.3 OPEN GATE S — asymptotic selector ratio

The central new static target is

\[
\boxed{
\inf_{L\ge L_0}\rho_L
=
\inf_{L\ge L_0}\frac{h_{\min}(L)}{h_{\max}(L)}
>\frac13.
}
\]

This may be proved directly by min/max convolution control or indirectly by the corrected spectral-complementarity norm.

No finite H24/H25 computation proves this statement.

### 8.4 OPEN GATE F — exact fibre/global conditioning compatibility

The selector count function used in the min/max bound must be the exact counting weight of the same canonical candidate fibre to which the Beatty exposure set `R_L` and one-child boundary `D_L` refer.

Existing fixed-Q fibre-compatibility results are relevant, but growing-scale/global compatibility must not be silently inferred from a fixed-Q theorem.

### 8.5 OPEN GATE C — zero mass is not emptiness

Even if

\[
\mu_N\to0,
\]

one exceptional nested canonical path may remain.

The terminal argument still has to contradict the eventually-zero canonical lift condition of a hypothetical positive integer counterexample, or otherwise show that no infinite nested candidate cylinder can survive the cumulative loss.

This is the same logical warning already recorded in the terminal proof-chain roadmap:

\[
\boxed{
\text{density/mass decay}\not\Rightarrow\text{set emptiness}
}
\]

without an additional canonical/minimal-counterexample argument.

### 8.6 BARRIERS / prohibited upgrades

1. Do not upgrade finite `rho` values to an asymptotic lower bound.
2. Do not interpret the product values through `L=1500` as proof progress percentages.
3. Do not conclude that polynomial mass decay alone rules out an exceptional integer path.
4. Do not replace the exact selector fibre by an unrestricted dyadic measure without a proved transfer inequality.

---

## 9. Relation to the older Gate-A / Gate-B route

The 2026-08-25 terminal roadmap used

\[
\text{Gate A: high-surplus tail tightness}
\to
\text{Gate B: low-strip killing gap}
\to
\text{Gate C}.
\]

The present bridge supplies a possible **parallel route**:

\[
\boxed{
\text{Gate F: exact fibre compatibility}
\to
\text{Gate S: uniform selector ratio }\rho_0>1/3
\to
\text{harmonic one-child contraction}
\to
\text{Gate C}.
}
\]

This does not invalidate the older Gate-A/Gate-B architecture.  It is potentially simpler because the Beatty one-child boundary already supplies recurrent loss across the full coefficient-survivor language, so a separate low-strip killing mechanism is unnecessary if Gates F and S can be closed.

If the min/max ratio degenerates below `1/3` at growing scales, the corrected spectral-complementarity route remains the appropriate fallback.

---

## 10. Next mathematical target

The next calculation should no longer search for one-child exposure: that part is now quantitatively sufficient.

The highest-value target is to study the scaling of

\[
\rho_L=\frac{h_{\min}(L)}{h_{\max}(L)}
\]

for the exact high-selector multiplicity on the canonical fibres, and to determine whether one can prove either

\[
\inf_L\rho_L>\frac13,
\]

or a weaker block-averaged replacement strong enough that

\[
\sum_{L\text{ rise}}
\frac{3\rho_L-1}{L}
=+\infty
\]

over the scales where `rho_L>1/3`.

The second formulation is strictly weaker than a uniform min/max theorem and should be audited before attempting a stronger equidistribution result.
