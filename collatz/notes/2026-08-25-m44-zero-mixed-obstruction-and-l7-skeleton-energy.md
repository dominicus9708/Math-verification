# m44 zero-mixed obstruction and late L7 skeleton energy

Date: 2026-08-25

Status: **exact finite same-integer obstruction for the globally zero-mixed m44 branch + exact finite selector-independent weighted-L2 bound from late internal plateau orientation quotient. Stage 4 first-order overlap remains open.**

This note continues the dyadic-fibre/weighted-overlap route recorded in `2026-08-25-dyadic-fiber-orthogonality-and-weighted-overlap-target.md`. It deliberately separates exact finite theorems from the still-missing first-order same-integer overlap theorem.

This is not a proof of the Collatz conjecture.

## 1. Current m44 selector core

The recursively sufficient critical block is

\[
\mathcal C_{44}
=
\left\{
4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

Its maximum is

\[
6\cdot3^{44}+1<2^{73}.
\]

Its diameter is

\[
\operatorname{diam}(\mathcal C_{44})
=2(3^{44}-1)<2^{71}.
\]

The exact positive gap in the last inequality is

\[
2^{71}-2(3^{44}-1)
=391,641,437,067,600,141,088.
\]

## 2. The all-height zero-mixed L=77 language

Let

\[
b(j):=\min\{q:3^q\ge2^j\}.
\]

Define \(\widetilde{\mathcal Z}_{77}\) to be all length-77 parity words satisfying simultaneously:

1. coefficient survival at every prefix,
   \[
   q_j\ge b(j);
   \]
2. every aligned full seven-bit block is an L7 full-Hensel residue-maximal representative;
3. every Beatty plateau pair is globally unmixed, hence is `00` or `11`.

Unlike the earlier exploratory boundary count, **no terminal equality** \(q_{77}=b(77)\) is imposed. Open positive-height excursions at the right edge are included.

The exact transfer enumeration gives

\[
\boxed{
|\widetilde{\mathcal Z}_{77}|
=1,615,699,347.
}
\]

Among their canonical starts modulo \(2^{77}\), exactly

\[
\boxed{
100,986,373
}
\]

lie below \(2^{73}\).

The m44 ternary membership test is exact: for a start \(N\equiv3\pmod4\), put

\[
T=\frac{N-3}{4}-3^{44}.
\]

Then \(N\in\mathcal C_{44}\) iff the first 44 ternary digits of \(T\) all lie in \(\{0,1\}\) and no higher ternary digit remains.

The complete scan gives

\[
\boxed{
\widetilde{\mathcal Z}_{77}\cap\mathcal C_{44}=\varnothing.
}
\]

Therefore no member of the current m44 selector core can remain coefficient-surviving and aligned-L7-maximal through depth 77 while keeping **every** Beatty plateau pair unmixed.

In particular, an infinite globally zero-mixed exceptional path cannot attach to the m44 core: it would have a forbidden length-77 prefix.

Certificate:

`collatz/src/m44_l77_allheight_zero_mixed_l7_selector_obstruction_certificate.cpp`

Regression output:

```text
boundary=1615699347 b77=49
tasks_after49=450466
enumerated=1615699347 below2^73=100986373 cantor_hits=0
```

## 3. Late orientation injectivity

For a mixed plateau pair beginning at position \(j\), the exact adjacent-swap formula is

\[
r(\cdots01\cdots)-r(\cdots10\cdots)
\equiv
-2^j3^{-\ell}
\pmod{2^H}.
\]

Fix one plateau skeleton: all bits outside chosen plateau pairs and every plateau pair-sum are fixed, while only the `01/10` orientations vary.

If two orientation vectors differ, choose the smallest changed plateau start \(j_*\). All later increments have strictly larger 2-adic valuation and the coefficient at \(j_*\) is odd. Hence

\[
\nu_2(r-r')=j_*<H.
\]

Thus distinct orientation vectors have distinct canonical residues modulo \(2^H\).

For the m44 core, if all changed plateau starts satisfy \(j\ge71\), two selector starts in the same orientation skeleton would have an ordinary difference divisible by \(2^{71}\). Since the whole selector block has diameter strictly less than \(2^{71}\), this is impossible unless the starts are equal, and residue injectivity then forces the orientation vectors to be identical.

So, after the early coordinates are fixed, at most one late orientation vector in a skeleton can be a same-integer m44 selector point.

This is an exact primal-space rigidity lemma. It does not by itself supply the Stage 4 exponential rate because a hard language may contain many distinct skeletons.

## 4. L7-restricted orientation cells

The L7 rule can remove some orientations, so one may not replace the hard language by the full coefficient-survival plateau cube.

Instead partition the actual L7 hard boundary language into cells by forgetting selected late plateau orientations while retaining all other information. Let one cell contain \(K_s\) allowed words.

Because the orientation-to-residue map inside a fixed cell is injective, the uniform cell measure \(\nu_s\) has \(K_s\) distinct residues. For every residue difference \(t\), at most \(K_s\) ordered pairs can realize that difference, since after choosing the first point the second is determined. Therefore

\[
\boxed{
\|\nu_s*\widetilde\nu_s\|_\infty
\le\frac1{K_s}.
}
\]

For an arbitrary selector probability measure \(\mu\), this implies

\[
(\mu*\widetilde\mu*\nu_s*\widetilde\nu_s)(0)
\le\frac1{K_s}.
\]

Equivalently,

\[
\boxed{
\frac1{2^H}
\sum_k
|\widehat\mu(k)|^2
|\widehat\nu_s(k)|^2
\le\frac1{K_s}.
}
\]

This bound is selector-independent.

## 5. Mixture/Jensen reduction to an orientation-skeleton quotient

Let the full L7 hard boundary language have size \(A\), let its orientation cells be indexed by \(s\), and let

\[
A=\sum_sK_s,
\qquad
Q:=\#\{s\}.
\]

The uniform hard-language measure is

\[
\nu=\sum_s\frac{K_s}{A}\nu_s.
\]

Pointwise convexity gives

\[
|\widehat\nu(k)|^2
\le
\sum_s\frac{K_s}{A}|\widehat\nu_s(k)|^2.
\]

Combining this with the cell bound yields the exact selector-independent inequality

\[
\boxed{
\frac1{2^H}
\sum_k
|\widehat\mu(k)|^2
|\widehat\nu(k)|^2
\le
\frac QA.
}
\]

Thus the weighted common spectrum is controlled by a purely combinatorial orientation-skeleton quotient.

## 6. Conservative quotient used in the certificate

To avoid any cross-block bookkeeping ambiguity, the verifier forgets only plateau orientations whose starts satisfy both

\[
j\ge71
\]

and

\[
j\bmod7\le5.
\]

Hence only plateau pairs wholly contained inside one aligned seven-bit L7 block are quotiented. Plateau pairs crossing a seven-bit block boundary are left fully resolved and contribute no gain.

This makes every reported gap conservative.

The verifier reconstructs the exact L7 allowed-mask counts

\[
(1,2,6,15,21,16,7,1)
\]

and performs exact integer transfer DP with coefficient-survival prefixes and terminal Beatty equality \(q_H=b(H)\).

### H=315

This is the first aligned seven-step depth above

\[
\frac{50}{7}\,44=314.285\ldots.
\]

The exact counts are

\[
A_{315}
=517885458235304308157182410734564932221743686697609244752296472620411591960348,
\]

\[
Q_{315}
=63820688520932622184721715929174699158591849888248537439621754920000435.
\]

Exact integer comparison gives

\[
\boxed{
2^{22}<\frac{A_{315}}{Q_{315}}\le2^{23}.
}
\]

Therefore the selector-independent weighted common spectrum satisfies

\[
\boxed{
\frac1{2^{315}}
\sum_k
|\widehat\mu(k)|^2|\widehat\nu(k)|^2
<2^{-22}.
}
\]

### H=700

The exact counts are

\[
A_{700}
=645689734914183363821586792441235488458868199403315076106181388545396779258640538805225372262002990810695394148445364291510021385381790982033492390207338527017080420714113841399,
\]

\[
Q_{700}
=1325116145742994128504793391221753016111408517063735997913466408888656679579695514192819981925155986595337748471956945110285694798063467723859180975004214036843.
\]

Exact integer comparison gives

\[
\boxed{
2^{58}<\frac{A_{700}}{Q_{700}}\le2^{59}.
}
\]

Hence

\[
\boxed{
\frac1{2^{700}}
\sum_k
|\widehat\mu(k)|^2|\widehat\nu(k)|^2
<2^{-58}.
}
\]

The numerical entropy gap is

\[
\frac{\log_2(A_{700}/Q_{700})}{700}
\approx0.08393928555
\]

bit per step, while the exact certified rational lower bound is

\[
\boxed{
\frac{58}{700}=\frac{29}{350}
\approx0.0828571.
}
\]

Certificate:

`collatz/src/l7_late_internal_plateau_skeleton_entropy_certificate.py`

## 7. Audit: why Stage 4 is still open

The last inequality is a weighted **second-moment/common-spectrum** bound. Stage 4 requires control of the first-order same-integer overlap amplification

\[
\Xi_{m,H}
=
\frac{|\mathcal C_m\cap\mathcal L_H|/|\mathcal C_m|}
{|\mathcal L_H|/2^H}.
\]

Applying Cauchy--Schwarz to the complete frequency group without further structure reintroduces a factor proportional to the square root of the number of frequencies. Therefore one must not compare the `0.08394` second-moment exponent directly with the L7 exclusion threshold `7/50=0.14`.

The correct interpretation is narrower:

1. the globally zero-mixed m44 branch is now exactly excluded by depth 77;
2. nontrivial late orientation cells carry an exact selector-independent weighted-L2 penalty;
3. at H=315 the conservative penalty already exceeds 22 bits, and at H=700 it exceeds 58 bits;
4. the remaining theorem is to combine this common-spectrum penalty with the selector-specific spectral splitting / inverse-Cantor information without paying the full ambient-frequency square-root cost.

That is the current Stage 4 frontier.
