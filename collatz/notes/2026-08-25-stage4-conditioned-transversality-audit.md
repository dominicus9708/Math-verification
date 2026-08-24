# Stage 4 conditioned-transversality audit and finite extension

Date: 2026-08-25

Status: **one-window transversality sharpened; L8 finite calibration extended; Stage 4 cross-base theorem still open.**

This note audits the 2026-08-19 Stage 4 frontier. It does not claim a proof of the Collatz conjecture.

## 1. Audit of the current proof frontier

The repository's current proof-program status remains:

- Stages 1--3: structurally closed within the stated reduction;
- Stage 4: open at the renewal-conditioned same-integer cross-base growth theorem.

The latest L7 residue-maximality certificate raises the deterministic exclusion rate to

\[
\eta>\frac7{50}=0.14,
\]

so a sufficient Stage 4 target is

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}H<\frac7{50}.
\]

The depth-28 m=45 transversality certificates are exact but explicitly one-window statements. They cannot be iterated after arbitrary later conditioning without a new renormalization theorem.

## 2. Statewise sharpening of the depth-28 TV repair bound

For each remaining first-defect cylinder

\[
p\in\{2,5,8,10\}
\]

and affine block \(b\in\{0,1\}\), let

- \(M_p=2^{27-p}\) be the compatible dyadic lift count;
- \(A_p\) be the exact depth-28 Hensel hard cardinality;
- \(u_p=A_p/M_p\);
- \(t_{p,b}\) be the exact TV numerator from `m45_depth28_uniform_transversality_tv_certificate.cpp`;
- `raw_{p,b}` be the exact raw selector mass.

The exact TV is

\[
\operatorname{TV}_{p,b}
=\frac{t_{p,b}}{2\,\mathrm{raw}_{p,b}M_p}.
\]

Therefore

\[
\frac{\operatorname{TV}_{p,b}}{u_p}
=\frac{t_{p,b}}{2\,\mathrm{raw}_{p,b}A_p}.
\]

Using the actual \(A_p\), rather than only the coarse common lower bound \(u_p\ge3/64\), exact integer comparison gives in all eight cases

\[
81t_{p,b}<2\,\mathrm{raw}_{p,b}A_p.
\]

Hence every depth-28 hard subset covered by the same TV theorem obeys the sharpened one-window amplification bound

\[
\boxed{
\Xi_{p,b}^{\rm one\ window}
<1+\frac1{81}
=\frac{82}{81}.
}
\]

Since

\[
82^{56}<2\,81^{56},
\]

we obtain the exact bit bound

\[
\boxed{
\log_2\Xi_{p,b}^{\rm one\ window}<\frac1{56}\text{ bit}.
}
\]

This strengthens the previous coarse `<1/50 bit` bound. The exact verifier is

`collatz/src/m45_depth28_statewise_transversality_56th_bit_certificate.py`.

## 3. Actual depth-28 overlap remains essentially neutral

Recomputing the exact same-integer hard-set amplification

\[
\Xi^{\rm actual}_{p,b}
=
\frac{\mathrm{hard}_{p,b}/\mathrm{raw}_{p,b}}
{A_p/M_p}
\]

shows that every positive statewise deviation is below two parts per million. The largest positive case is the p=8, b=1 state and is approximately

\[
1.0000016765.
\]

Aggregating over the four unresolved p-cylinders gives anti-bias in both affine blocks. The exact uniform-minus-actual gaps are

\[
\boxed{
E_0-H_0=\frac{40,266,396,981}{524,288}>0,
}
\]

\[
\boxed{
E_1-H_1=\frac{22,103,176,379}{131,072}>0.
}
\]

Thus the first active depth-28 window remains strongly consistent with zero exponential cross-base repair.

This remains finite evidence only.

## 4. Denominator audit: do not over-transfer the hard-set fraction

A tempting but invalid shortcut is to compare the p-specific Hensel hard fractions \(A_p/M_p\) directly with the Stage 4 L7 residue-maximal language density and then declare some p-states automatically safe under arbitrary concentration.

That inference is not certified here. The depth-28 Hensel retained set and the Stage 4 aligned-L7 residue-maximal language are produced by related but not identical filters, and the required denominator identity/inclusion under renewal conditioning has not been proved.

Therefore:

\[
\boxed{
\text{statewise one-window TV theorem}
\not\Rightarrow
\text{iterable Stage 4 cross-base theorem}.
}
\]

The audit retains the exact `<1/56 bit` first-window result but rejects any unproved denominator substitution.

## 5. Exact L8 small-core extension beyond m=22

The existing `l8_small_core_multiwindow_overlap_certificate.cpp` was first reproduced exactly for m=20,21,22. The same L=8 residue-maximal block rule and coefficient-survival condition were then extended with exact integer \(q_{\min}(k)\) to m=23,...,27.

The new exact results are

\[
\begin{array}{c|rrr|r}
m&H=128&H=160&H=192&\text{maximum valid depth}\\\hline
23&2&0&0&135\\
24&2&0&0&151\\
25&11&0&0&143\\
26&23&2&0&175\\
27&26&1&0&167
\end{array}
\]

The verifier is

`collatz/src/l8_small_core_m23_m27_extension_certificate.cpp`.

Two audit consequences follow.

First, the m=21 and m=22 extinction at H=128 is not monotone in m: survivors reappear for m=23 and above. Therefore H=128 cannot be promoted to a universal finite cutoff from the earlier data.

Second, every newly tested core m=23,...,27 is nevertheless empty by H=192; in fact the largest observed valid depth is 175. This strengthens finite evidence while leaving the asymptotic theorem untouched.

## 6. Refined remaining Stage 4 target

The exact renewal-syndrome graph already compresses the finite depth-28 exceptional Hensel states to

\[
E_{10},E_{18},E_{21},
\]

and the height-credit phase cocycle removes exponential predecessor-credit growth. The unresolved exponential resource is therefore not ordinary credit amplitude but **conditioned cross-base selector concentration**.

The next proof-level object should carry at least

\[
(\text{relative height},\ \text{Hensel syndrome},\ \text{renewal phase})
\]

and attach to each renewal transition an exact repair increment

\[
R_j=\log_2\frac{\mu_j(H_j)}{\nu_j(H_j)}.
\]

A sufficient theorem is to prove, on every recurrent renewal class,

\[
\limsup_{n\to\infty}
\frac{\sum_{j<n}R_j}{\sum_{j<n}\Delta H_j}
<\frac7{50},
\]

or more strongly that the cumulative repair is sublinear in total dyadic depth.

Equivalently, in the block-credit language, one may prove that every recurrent class has positive average net exclusion credit

\[
\Gamma_j=I_j-R_j,
\qquad
\sum_j\Gamma_j=+\infty.
\]

The exact first-window `<1/56 bit` result supplies a very small initial repair term, but the missing theorem is the stability/renormalization of this control after previous renewal conditioning.

## 7. Current audit status

\[
\begin{array}{c|c}
\text{component}&\text{status}\\\hline
L7 deterministic exclusion >7/50&\text{closed}\\
Depth-28 first-window selector transversality&\text{closed; sharpened to <1/56 bit}\\
Depth-28 renewal syndrome compression&\text{closed}\\
Height-normalized predecessor-credit growth&\text{zero exponential rate}\\
L8 finite small-core calibration m\le27&\text{extended; all tested cores extinct by H=192}\\
Renewal-conditioned cross-base growth <7/50&\textbf{open}
\end{array}
\]

The next computation should therefore target a second/renewed window conditioned on the first exact hard/renewal state, rather than merely extending an unconditioned first-window TV estimate.
