# Mode I near-critical block necessity

Date: 2026-08-11

Status: **exact block translation of a known rational-2-adic parity-density necessity**. The external input is the López–Stoll result that a rational 2-adic integer with a non-cyclic 3x+1 trajectory must lie on the critical lower parity-density boundary. The deductions below are exact in the present macroblock coordinates.

## 1. Mode I setup

Consider a hypothetical positive-integer, nonperiodic first-descent survivor whose maximal debit-block orbit is eventually strictly increasing. After discarding a finite prefix, every block satisfies

\[
M_r=\frac{2^{h_r+d_r}}{3^{h_r}}<1.
\]

Let

\[
\alpha:=\log_2\frac32,
\qquad
\varepsilon_r:=\alpha h_r-d_r>0.
\]

Define cumulative odd-event count, cumulative accelerated-step count, and cumulative subcritical deficit by

\[
H_R:=\sum_{r=0}^{R-1}h_r,
\]

\[
A_R:=\sum_{r=0}^{R-1}(h_r+d_r),
\]

\[
L_R:=\sum_{r=0}^{R-1}\varepsilon_r.
\]

Since `1+alpha=log_2 3`,

\[
\boxed{
A_R=(\log_2 3)H_R-L_R.
}
\]

The block-boundary multiplicative coordinate is

\[
\boxed{
\Lambda_R
:=\frac{2^{A_R}}{3^{H_R}}
=2^{-L_R}.
}
\]

Thus `L_R` is the exact cumulative logarithmic coefficient deficit below criticality.

## 2. Why parity-density minima occur at block boundaries

At accelerated parity resolution, one maximal block is the word

\[
1^{h_r}0^{d_r}.
\]

During the `1`-run, appending a `1` moves the empirical odd-bit density toward `1` and therefore cannot create a new lower density once the trajectory is in the Collatz-relevant range below `1`.

During the trailing `0`-run, the odd-bit count stays fixed while the word length increases, so the density decreases monotonically.

Hence the lower parity-density envelope is attained at block boundaries.

At the end of `R` blocks that density is

\[
\boxed{
\frac{H_R}{A_R}
=
\frac{1}{\log_2 3-L_R/H_R}.
}
\]

Because every Mode I block is subcritical, `L_R>0`, so every such boundary density is strictly above

\[
\frac{1}{\log_2 3}=\frac{\log2}{\log3}.
\]

## 3. Critical-boundary necessity

López and Stoll prove that if a rational 2-adic integer has a non-cyclic 3x+1 trajectory, then necessarily the lower parity density equals

\[
\frac{\log2}{\log3}.
\]

For an ordinary positive integer, which is rational in `Z_2`, a nonperiodic Mode I counterexample must therefore satisfy

\[
\boxed{
\liminf_{R\to\infty}
\frac{H_R}{A_R}
=
\frac{1}{\log_2 3}.
}
\]

Using the exact boundary formula, this is equivalent to the existence of an infinite subsequence `R_j` such that

\[
\boxed{
\frac{L_{R_j}}{H_{R_j}}\longrightarrow0.
}
\]

Thus a Mode I counterexample cannot remain uniformly below the critical block slope. Its cumulative subcritical deficit must be asymptotically negligible relative to the total odd-event mass along an infinite subsequence.

## 4. Relative-slope concentration

Fix `eta>0` and define the bad-block set

\[
B_R(\eta)
:=
\left\{
r<R:
\alpha-\frac{d_r}{h_r}\ge\eta
\right\}.
\]

For every bad block,

\[
\varepsilon_r
=h_r\left(\alpha-\frac{d_r}{h_r}\right)
\ge\eta h_r.
\]

Hence

\[
\eta
\sum_{r\in B_R(\eta)}h_r
\le L_R.
\]

Along every critical subsequence with `L_R/H_R -> 0`,

\[
\boxed{
\frac{
\sum_{r\in B_R(\eta)}h_r
}{H_R}
\longrightarrow0.
}
\]

Therefore, in odd-event-weighted density, essentially all of Mode I must satisfy

\[
\boxed{
\frac{d_r}{h_r}\to\alpha
\quad\text{from below}.
}
\]

## 5. Bounded credit depths have zero odd-event weight

Fix an integer `H_0>=1`. Among the finitely many integer pairs

\[
1\le h\le H_0,
\qquad
1\le d<\alpha h,
\]

the positive numbers

\[
\frac{\alpha h-d}{h}
\]

have a positive minimum, say `eta(H_0)>0`.

Thus every block with `h_r<=H_0` belongs to `B_R(eta(H_0))`. Consequently, along every critical subsequence,

\[
\boxed{
\frac{
\sum_{\substack{r<R\\h_r\le H_0}}h_r
}{H_R}
\longrightarrow0.
}
\]

Hence a rational nonperiodic Mode I trajectory must place asymptotically all odd-event mass inside blocks whose credit depths tend without bound.

Informally but accurately:

\[
\boxed{
\text{Mode I hard core}
=\text{very long blocks with }d/h\text{ approaching }\log_2(3/2)\text{ from below}.
}
\]

## 6. What this does and does not prove

This theorem does not exclude Mode I. Long subcritical blocks are arithmetically possible at every finite depth.

Its role is to remove all uniformly subcritical regimes from the rational positive-integer hard core. A final Mode I exclusion theorem only needs to attack infinite exact block chains satisfying simultaneously:

1. `X_{r+1}>X_r` for every sufficiently late block;
2. `3^{h_r}K_r+2^{d_r}-1=2^{d_r+h_{r+1}}K_{r+1}`;
3. `L_R/H_R -> 0` along an infinite subsequence;
4. bounded `h_r` carries asymptotically zero odd-event weight.

The remaining difficulty is therefore a **long near-critical block concatenation problem**, not a generic subcritical-block problem.
