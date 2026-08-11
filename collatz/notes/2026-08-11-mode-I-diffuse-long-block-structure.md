# Mode I diffuse long-block structure

Date: 2026-08-11

Status: **exact consequence of the Mode I block product, the subcritical frontier, and the known rational-2-adic critical parity-density necessity**. This narrows the shape of any hypothetical positive-integer Mode I counterexample but does not exclude it.

## 1. Setup

Consider an eventually all-subcritical maximal-block tail

\[
X_0<X_1<X_2<\cdots
\]

with block data `(h_r,d_r)` and

\[
\alpha:=\log_2\frac32,
\qquad
\varepsilon_r:=\alpha h_r-d_r>0.
\]

Define

\[
H_R:=\sum_{r<R}h_r,
\qquad
L_R:=\sum_{r<R}\varepsilon_r.
\]

The critical-boundary necessity for a rational 2-adic noncyclic orbit gives an infinite subsequence `R_j` on which

\[
\boxed{
\frac{L_{R_j}}{H_{R_j}}\to0.
}
\]

The earlier relative-slope concentration theorem then implies that, for every fixed `H_0`,

\[
\boxed{
\frac{
\sum_{\substack{r<R_j\\h_r\le H_0}}h_r
}{H_{R_j}}
\to0.
}
\]

Thus bounded credit depths carry asymptotically zero odd-event weight.

## 2. Pointwise depth bound from the block product

The Mode I block-product estimate gives, for fixed initial tail minimum `N=X_0`,

\[
X_r
\le
C_N\,N\,2^{L_r}r^{1/3}
\]

for a constant `C_N>0` and all sufficiently large `r`.

Since

\[
2^{h_r}\mid X_r+1,
\]

we have

\[
2^{h_r}\le X_r+1.
\]

Therefore

\[
\boxed{
h_r
\le
L_r+rac13\log_2 r+O_N(1).
}
\]

Because `L_r<=L_R` for `r<R`,

\[
\boxed{
\max_{r<R}h_r
\le
L_R+rac13\log_2 R+O_N(1).
}
\]

## 3. No single giant block can create the critical subsequence

Along the critical subsequence `R_j`,

\[
\frac{L_{R_j}}{H_{R_j}}\to0.
\]

Every subcritical block has `h_r>=2`, so

\[
H_R\ge2R,
\]

and hence

\[
\frac{\log R}{H_R}\to0.
\]

Dividing the pointwise maximum-depth bound by `H_R` gives

\[
\boxed{
\frac{\max_{r<R_j}h_r}{H_{R_j}}
\to0.
}
\]

Thus the critical parity-density boundary cannot be produced by occasional blocks whose odd-event lengths are comparable with the entire previous history.

The long-block mass must be **diffuse**: block depths become large in aggregate, but no single block carries a nonzero fraction of the cumulative odd-event count.

## 4. Mean block depth must diverge

We now show

\[
\boxed{
\frac{H_{R_j}}{R_j}\to\infty.
}
\]

Suppose instead that along a further subsequence

\[
H_R\le C R
\]

for some constant `C`.

Choose a fixed integer `H_0>2C`. The number of blocks with `h_r>H_0` is at most

\[
\frac{H_R}{H_0}
<\frac R2.
\]

Hence at least `R/2` blocks satisfy `h_r<=H_0`. Since every block has `h_r>=2`, their total odd-event weight is at least `R`.

But

\[
H_R\le CR,
\]

so the bounded-depth blocks carry at least the fixed fraction `1/C` of the total odd-event weight, contradicting the bounded-depth zero-weight theorem.

Therefore the mean block depth diverges along the critical subsequence.

## 5. Combined Mode I shape

Any positive-integer, nonperiodic Mode I hard core must therefore admit an infinite subsequence satisfying simultaneously

\[
\boxed{
R=o(H_R),
}
\]

\[
\boxed{
\max_{r<R}h_r=o(H_R),
}
\]

\[
\boxed{
L_R=o(H_R),
}
\]

while also

\[
\boxed{
L_R\ge\frac23\log_2R-O_N(1).
}
\]

Moreover, in `h`-weighted density,

\[
\boxed{
\frac{d_r}{h_r}\to\log_2\frac32
\quad\text{from below}.
}
\]

Thus the surviving Mode I geometry is neither a bounded-depth process nor a sparse sequence of giant reset blocks. It is a **diffuse long-block near-critical regime**: many increasingly long blocks, no dominant block, cumulative coefficient deficit diverging but remaining sublinear in total odd-event count.

## 6. Remaining arithmetic obstruction

The exact integer core recurrence remains

\[
3^{h_r}K_r+2^{d_r}-1
=
2^{d_r+h_{r+1}}K_{r+1}.
\]

A complete Mode I exclusion theorem must show that this recurrence cannot support an infinite positive-integer chain having the diffuse long-block properties above while its initial formation floor remains one fixed finite ordinary integer.
