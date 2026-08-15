# Gate-syndrome late-repair forcing across first and second Euclidean returns

Date: 2026-08-15

Status: **exact syndrome recurrence + finite bounded-credit certificates + deterministic late-repair localization for the explicit gate-wide cube sections**. It strengthens the first-return syndrome audit to the `G_13/G_14` supergates and proves that an early correction perturbation cannot repair the observed low-syndrome failure. The result concerns the explicit cube sections and perturbations supported before a stated odd-rank threshold; it does not exclude the full gate fibre and does not prove Collatz.

## 1. Cube and target

For a gate-wide cube

\[
1^F(01/10)^J0,
\qquad q=F+J,
\]

a difference vector `epsilon` has normalized correction

\[
Z(\epsilon)=\sum_{j=0}^{J-1}\epsilon_j3^{J-1-j}4^j.
\]

An incoming integer predecessor credit `delta>0` requires

\[
Z(\epsilon)\equiv T_\delta:=-2^{2J+1}\delta\pmod{3^q}.
\]

The low `J` trits determine a unique balanced vector. The remaining issue is the high syndrome.

## 2. Renormalized lifting recurrence

Reverse the pair index and write `e_l=epsilon_(J-1-l)`. Factoring by `4^(J-1)` gives

\[
4^{-(J-1)}Z
=\sum_{l=0}^{J-1}e_l3^l4^{-l}.
\]

Put

\[
U_0:=4^{-(J-1)}T_\delta\pmod{3^q}.
\]

At step `l`, choose the unique balanced digit

\[
e_l\in\{-1,0,1\},
\qquad e_l\equiv U_l\pmod3,
\]

and update

\[
\boxed{U_{l+1}=\frac{4(U_l-e_l)}3}
\]

at the naturally reduced modulus `3^(q-l-1)`.

After all `J` systematic trits are lifted,

\[
\boxed{v_3(U_J)=v_3(Z-T_\delta)-J.}
\]

Thus `v_3(U_J)` is exactly the number of additional high-syndrome trits matched before the first failure. This recurrence is equivalent to the earlier exact balanced-Hensel construction but removes the explicit `4^j` power table.

## 3. Exact bounded-credit audit through the second return

Audit every

\[
1\le\delta\le397.
\]

The exact results are

\[
\boxed{\begin{array}{c|c|c|c}
\text{gate/fibre}&(F,J,q)&\text{full lifts}&\max m\\\hline
G_{81}\text{ neutral}&(404,567,971)&0&5\\
G_{81}\text{ one-slack}&(402,568,970)&0&4\\
G_{82}\text{ neutral}&(409,574,983)&0&6\\
G_{82}\text{ one-slack}&(407,575,982)&0&6\\
G_{13}\text{ neutral}&(5245,7390,12635)&0&7\\
G_{13}\text{ one-slack}&(5243,7391,12634)&0&6\\
G_{14}\text{ neutral}&(5648,7958,13606)&0&6\\
G_{14}\text{ one-slack}&(5646,7959,13605)&0&5
\end{array}}
\]

Here `m` is the number of high-syndrome trits matched beyond the systematic low-`J` block.

The new second-return distributions are

\[
G_{13}^{(0)}:\quad
0:249,\ 1:106,\ 2:28,\ 3:9,\ 4:2,\ 5:2,\ 7:1,
\]

with unique maximizer `delta=375`,

\[
G_{13}^{(-1)}:\quad
0:270,\ 1:86,\ 2:27,\ 3:9,\ 4:4,\ 6:1,
\]

again maximized by `delta=375`,

\[
G_{14}^{(0)}:\quad
0:267,\ 1:78,\ 2:34,\ 3:10,\ 4:6,\ 5:1,\ 6:1,
\]

maximized by `delta=277`, and

\[
G_{14}^{(-1)}:\quad
0:264,\ 1:87,\ 2:28,\ 3:11,\ 4:5,\ 5:2,
\]

maximized by `delta=277,367`.

Thus increasing the Euclidean scale from roughly `1.5e3` to roughly `2e4` time bits, and increasing the number of systematic low-Hensel pivots from hundreds to more than seven thousand, does not restore any nonzero bounded-credit full lift in these cube sections. Every tested target still fails within at most seven syndrome trits.

## 4. Late-repair lemma

Suppose the selected cube vector matches through `J+m` ternary digits but fails at the next one:

\[
3^{J+m}\mid D_0+2^L\delta,
\qquad
3^{J+m+1}\nmid D_0+2^L\delta.
\]

Add an arbitrary correction perturbation `E` supported only on odd ranks at most `K`. Every correction term from rank `k<=K` contains the factor `3^(q-k)`, hence

\[
\boxed{3^{q-K}\mid E.}
\]

If

\[
q-K\ge J+m+1,
\]

then `E` vanishes modulo `3^(J+m+1)` and cannot repair the first failed syndrome trit. Therefore any repair must satisfy

\[
\boxed{K\ge q-(J+m)=F-m.}
\]

This conclusion does not assume independence or genericity; it is a triangular divisibility statement.

## 5. Numerical repair thresholds

Using the worst-case `m` in the bounded-credit audit, any repair outside the selected cube section must involve a correction difference reaching at least the following odd rank:

\[
\boxed{\begin{array}{c|c}
\text{gate/fibre}&K_{\min}\\\hline
G_{81}\text{ neutral}&399\\
G_{81}\text{ one-slack}&398\\
G_{82}\text{ neutral}&403\\
G_{82}\text{ one-slack}&401\\
G_{13}\text{ neutral}&5238\\
G_{13}\text{ one-slack}&5237\\
G_{14}\text{ neutral}&5642\\
G_{14}\text{ one-slack}&5641
\end{array}}
\]

At critical scale this threshold is asymptotically a fraction

\[
\frac Fq\to2-\log_2 3\approx0.4150374993
\]

of the gate odd count, up to the bounded syndrome-match correction `m/q`.

## 6. Relation to the early first-defect reduction

The current isolated R1 branch has first Christoffel defect rank at most twelve. Such an early perturbation is far below every threshold above. In particular, in `G_81` neutral its correction contribution is divisible by at least

\[
3^{971-12}=3^{959},
\]

whereas the systematic/syndrome split occurs at `J=567`. After removing the low `J` trits, the first-defect contribution begins only at syndrome depth at least

\[
959-567=392.
\]

The explicit cube targets fail within at most five high syndrome trits in this fibre. Therefore the first defect itself cannot repair the cube syndrome failure.

More generally, the six certified early first-defect channels cannot account for the low-syndrome repair. A successful full-fibre lift must activate an additional correction degree of freedom much later in the gate, at or beyond the thresholds in Section 5.

This is a genuine cross-scale forcing statement:

\[
\boxed{
\text{early R1 defect}
+\text{bounded-credit cube target}
\Longrightarrow
\text{additional late gate repair is necessary.}
}
\]

## 7. Limitation and next target

The theorem does not show that such a late repair is impossible. The full same-state gate fibre contains orientations outside the explicit cube, and those orientations may supply the required late correction channel.

The remaining object is now narrower:

> classify the fixed-low-Hensel kernel contributions that first become visible near odd rank `F`, and test their simultaneous dyadic zero-lift image.

Equivalently, instead of analyzing the full gate fibre, the next kernel problem is localized to the narrow transition between the front-loaded `1^F` syndrome sector and the late `(01/10)^J` systematic sector.

This moves the unresolved freedom away from the whole gate and into a specific late-repair band near the complementary critical fraction `2-log_2 3` of the odd ranks.

## Reproducibility

Exact certificate:

`collatz/src/gate_cube_syndrome_recurrence_supergate_certificate.py`
