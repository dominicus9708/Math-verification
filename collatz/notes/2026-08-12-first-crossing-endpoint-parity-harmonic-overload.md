# First-crossing endpoint parity and harmonic overload

Date: 2026-08-12

Status: **exact necessary-condition theorem for a first coefficient crossing from a renewal floor**. It strengthens the earlier elementary `H>3N` even-endpoint cost by using the harmonic sparsity of distinct odd-event states.

## 1. Setup

Let `N` be a renewal floor of a hypothetical nonperiodic positive-integer first-descent survivor.

Suppose its first coefficient crossing occurs after `H>=2` odd events. Let

\[
r:=\frac{R}{3^H}
\]

be the normalized affine correction at the crossing.

In odd-event coordinates this is the same correction `c_H`, because even halving steps do not change `R` or the odd count `H`.

Let the odd-event start states in the segment be

\[
x_0=N,x_1,\ldots,x_{H-1}.
\]

They are all at least `N`, because `N` is a suffix minimum, and they are all distinct in a nonperiodic orbit.

For `i>=1`, every odd-event state is odd and not divisible by `3`, because it is obtained from `3x+1` after division by powers of `2`.

## 2. Exact correction product

The standard odd-event product gives

\[
\boxed{
1+\frac rN
=
\prod_{i=0}^{H-1}
\left(1+\frac1{3x_i}\right).
}
\]

Using `log(1+t)<=t`,

\[
\log\left(1+\frac rN\right)
\le
\frac13\sum_{i=0}^{H-1}\frac1{x_i}.
\]

## 3. Reciprocal sparsity bound

Order the distinct states `x_i` increasingly after `x_0=N`.

Among odd integers, numbers not divisible by `3` occupy the residue classes `1,5 mod 6`. After removing the possible initial state `N`, the `i`th smallest admissible later value is at least

\[
N+3i-2
\qquad(i>=1).
\]

Therefore

\[
\sum_{i=0}^{H-1}\frac1{x_i}
\le
\frac1N
+
\sum_{i=1}^{H-1}\frac1{N+3i-2}.
\]

For the decreasing function `f(x)=1/(N+3x-2)`,

\[
\sum_{i=1}^{H-1}f(i)
\le
f(1)+\int_1^{H-1}f(x)\,dx.
\]

Hence

\[
\boxed{
\sum_{i=0}^{H-1}\frac1{x_i}
\le
\frac1N
+
\frac1{N+1}
+
\frac13\log\frac{N+3H-5}{N+1}.
}
\]

Combining with the correction product,

\[
\boxed{
\log\left(1+\frac rN\right)
\le
\frac1{3N}
+
\frac1{3(N+1)}
+
\frac19\log\frac{N+3H-5}{N+1}.
}
\]

## 4. Even crossing endpoint forces `r>N`

Let the first coefficient-crossing endpoint be

\[
Y=T^A(N).
\]

If `Y` is even, the very next Collatz step is `Y/2`. Since `N` is a suffix minimum,

\[
\frac Y2\ge N,
\]

so

\[
Y\ge2N.
\]

At the crossing,

\[
Y=\frac{N+r}{P},
\qquad
P:=\frac{2^A}{3^H}>1.
\]

Thus

\[
N+r=PY>2N,
\]

and therefore

\[
\boxed{r>N.}
\]

Consequently

\[
\log\left(1+\frac rN\right)>\log2.
\]

## 5. Exact odd-event overload threshold

Combining Sections 3 and 4 gives

\[
\log2
<
\frac1{3N}
+
\frac1{3(N+1)}
+
\frac19\log\frac{N+3H-5}{N+1}.
\]

Solving for `H`,

\[
\boxed{
H>
\frac{
512(N+1)e^{-3/N-3/(N+1)}-N+5
}{3}.
}
\]

As `N` tends to infinity,

\[
\boxed{
H>(170+1/3+o(1))N.
}
\]

Therefore every first-crossing renewal-floor candidate satisfies the dichotomy

\[
\boxed{
\begin{array}{ll}
\text{odd crossing endpoint},&\text{or}\\[1mm]
H>(170.33\ldots+o(1))N.&\text{(extreme event-depth overload)}
\end{array}
}
\]

## 6. Consequence for the formation modulus

If the crossing endpoint is odd, then exact endpoint parity upgrades the first-crossing formation class from modulus

\[
2^A
\]

to

\[
\boxed{2^{A+1}.}
\]

Thus, outside the extreme linear-depth overload branch, the universal first-crossing tri-place defect may use the stronger dyadic modulus.

For the currently unresolved paradoxical-start region `N>2.8e19`, an even crossing endpoint therefore requires an odd-event depth on the order of at least `4.7e21`, showing that the even-endpoint exception is itself a very large combinatorial hard core.
