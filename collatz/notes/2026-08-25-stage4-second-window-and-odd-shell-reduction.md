# Stage 4 conditioned second-window and odd-shell reduction

Date: 2026-08-25

Status: **first exact nontrivial conditioned-window repair calibration + incremental spectral reduction; global Stage 4 theorem remains open.**

This note continues the 2026-08-25 conditioned-transversality audit. It does not claim a proof of the Collatz conjecture.

## 1. Exact incremental overlap identity

Let `S_H` be the number of same-integer candidates surviving the chosen dyadic language through depth `H`, inside an original candidate family of size `2^m`. Let `L_H` be the complete binary language count through the same depth. Define

\[
\Xi_H
:=
\frac{S_H/2^m}{L_H/2^H}.
\]

For two nested horizons `H_0<H_1` with `S_{H_0}>0`, define the repair generated only after conditioning on survival through `H_0` by

\[
\boxed{
\Xi_{H_0\to H_1}
:=
\frac{S_{H_1}/S_{H_0}}
{(L_{H_1}/2^{H_1})/(L_{H_0}/2^{H_0})}.
}
\]

Then exactly

\[
\boxed{
\Xi_{H_0\to H_1}
=\frac{\Xi_{H_1}}{\Xi_{H_0}}.
}
\]

Hence the logarithmic repair budget telescopes:

\[
\boxed{
\log_2\Xi_{H_n}
=
\log_2\Xi_{H_0}
+
\sum_{j<n}
\log_2\Xi_{H_j\to H_{j+1}}.
}
\]

The common forced `N=3 mod 4` factor cancels from every conditioned ratio automatically.

This is the exact finite version of the block-repair cocycle needed in Stage 4.

## 2. L8 language counts at the second-window horizons

Using the same aligned length-8 residue-maximal rule and coefficient-survival barrier as

`collatz/src/l8_small_core_multiwindow_overlap_certificate.cpp`, exact dynamic programming gives

\[
\boxed{
L_{128}
=21,743,857,700,147,672,762,453,009,957,952,
}
\]

\[
\boxed{
L_{160}
=3,366,931,613,143,870,666,238,124,211,272,626,161,619,
}
\]

and

\[
\boxed{
L_{192}
=538,739,847,013,238,234,058,807,333,725,091,128,756,700,219,273.
}
\]

The exact verifier is

`collatz/src/l8_second_window_conditioned_rate_certificate.py`.

## 3. First nontrivial conditioned second-window calculation

The independent candidate scan

`collatz/src/l8_small_core_m23_m27_extension_certificate.cpp`

certifies

\[
\begin{array}{c|rrr}
m&S_{128}&S_{160}&S_{192}\\\hline
23&2&0&0\\
24&2&0&0\\
25&11&0&0\\
26&23&2&0\\
27&26&1&0
\end{array}
\]

Thus `m=23,24,25` become empty in the second window. They require no positive repair estimate after depth 128.

The `m=26,27` cores remain nonempty through depth 160 and therefore provide genuine repeated-conditioning tests.

### m=26

The exact conditioned amplification is

\[
\Xi^{(26)}_{128\to160}
=
\frac{
186,778,315,422,024,057,770,491,309,012,332,350,275,584
}{
77,439,427,102,309,025,323,476,856,859,270,401,717,237
}
\]

so numerically

\[
\Xi^{(26)}_{128\to160}\approx2.4119279082.
\]

Its total repair is about

\[
1.2701867862\text{ bits}
\]

across the 32 added steps, hence about

\[
0.0396933371\text{ bit/step}.
\]

More importantly, the verifier proves by pure integer arithmetic

\[
\boxed{
(\Xi^{(26)}_{128\to160})^{25}<2^{32},
}
\]

therefore

\[
\boxed{
\frac1{32}\log_2\Xi^{(26)}_{128\to160}<\frac1{25}=0.04<\frac7{50}.
}
\]

### m=27

Likewise

\[
\Xi^{(27)}_{128\to160}
=
\frac{
93,389,157,711,012,028,885,245,654,506,166,175,137,792
}{
87,540,221,941,740,637,322,191,229,493,088,280,202,094
}
\]

and

\[
\Xi^{(27)}_{128\to160}\approx1.0668142671.
\]

Its total repair is only about

\[
0.0933090241\text{ bits},
\]

or

\[
0.0029159070\text{ bit/step}.
\]

The exact certificate again proves rate `<1/25`; in fact it proves the stronger

\[
\boxed{
\frac1{32}\log_2\Xi^{(27)}_{128\to160}<\frac1{300}.
}
\]

Every tested `m=23,...,27` core is empty by depth 192, so this finite sample has no positive third-window repair to estimate.

## 4. What this does and does not prove

This is stronger evidence than an unconditioned first-window calculation because the `H=160` mass is measured **inside the already rare set that survived through H=128**.

In particular, the `m=26` example has genuine positive conditioned repair:

\[
\Xi_{128\to160}>1,
\]

so the test is not vacuous. Nevertheless its repair exponent remains below `1/25`, far below the current L7 exclusion target `7/50`.

However this is still finite evidence. It does not prove that every larger candidate core, every renewal syndrome, or every arbitrarily late window has the same bound.

## 5. Odd-shell localization of fresh repair

The exact one-bit child-transport identity already established in

`collatz/notes/2026-08-12-odd-frequency-child-correlation-identity.md`

shows why repeated conditioning can be organized incrementally.

At parent modulus `M`, let

\[
u(r)=C(r)-C(r+M)
\]

be the selector-mass imbalance between the two newly exposed binary children. Fourier inversion gives

\[
\boxed{
 u(r)
 =\frac1M
 \sum_{s\ \mathrm{odd}}
 \widehat C(s)\zeta^{sr}.
}
\]

All even frequencies cancel exactly. Therefore information already visible at the parent resolution does not reappear as a new repair term. The fresh cross-base contribution is carried only by the new odd-frequency shell.

For the signed one-child boundary function `g_L`, the fresh correlation is

\[
\boxed{
K_L
=\frac1M
\sum_{s\ \mathrm{odd}}
\widehat C(s)G_L(s).
}
\]

Thus the remaining repeated-conditioning theorem does not require inventing a new arbitrary selector distribution after every renewal. The original selector measure is fixed; previous conditioning restricts the set of parent cylinders, and the newly revealed repair is an odd-shell correlation against the boundary selected by the current dynamical/renewal state.

The renewal state is still needed to determine the admissible boundary function `g_L` and its Hensel/height syndrome. The simplification is that the **cross-base mass channel itself is an additive shell cocycle rather than an uncontrolled re-randomization problem**.

## 6. Refined Stage 4 target

Write the positive fresh repair at each active binary extension as

\[
R_L
:=
\log_2\frac{r_L}{u_L},
\]

where `r_L` is the actual same-integer survival ratio and `u_L` the corresponding language/uniform survival ratio. The exact telescoping identity gives

\[
B_H=\sum_{L<H}R_L.
\]

The L7 deterministic theorem supplies exclusion rate strictly above

\[
\frac7{50}.
\]

Hence a sufficient remaining theorem can be stated as an odd-shell cocycle bound:

> For every recurrent admissible height/Hensel/renewal state class, the cumulative positive odd-shell repair satisfies
> \[
> \limsup_{H\to\infty}\frac1H\sum_{L<H}R_L<\frac7{50}.
> \]

A stronger sublinear bound remains sufficient but is not necessary.

This formulation is narrower than a full renewal transfer on all candidate masses. A finite-state renewal operator may still be useful, but it only needs to carry the state information required to specify the shell boundary spectrum and the additive repair cocycle.

## 7. Current status after this calculation

\[
\begin{array}{c|c}
\text{component}&\text{status}\\\hline
L7 deterministic exclusion >7/50&\text{closed}\\
First depth-28 m=45 transversality&\text{closed; <1/56 bit}\\
Finite renewal syndrome graph&\text{closed at depth 28}\\
Height-normalized predecessor credit&\text{zero exponential rate}\\
L8 first-window finite calibration&\text{closed for tested m<=27}\\
L8 conditioned second window 128->160&\text{new: exact subcritical repair in all nonempty tested cases}\\
Odd-frequency localization of fresh child repair&\text{exact identity}\\
Uniform recurrent odd-shell repair rate <7/50&\mathbf{OPEN}
\end{array}
\]

The next proof-level calculation should therefore estimate the odd-shell correlation norm for the actual admissible renewal boundary classes, rather than extending only unconditioned survivor counts.
