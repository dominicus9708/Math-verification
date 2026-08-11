# Renewal rational-cycle shadow

Date: 2026-08-11

Status: **exact algebraic bridge between aggregate-supercritical renewal segments and periodic words**. It does not exclude either branch by itself.

## 1. Aggregate affine map

For one renewal-floor segment let

\[
F(x)=\frac{3^H x+B}{2^A},
\qquad A=H+D,
\]

be the exact affine map induced by the segment word. Let consecutive renewal floors satisfy

\[
F(N)=N',
\qquad N'>N,
\]

and write

\[
g:=N'-N.
\]

Assume the aggregate segment is supercritical:

\[
2^A>3^H.
\]

Set

\[
\boxed{Z:=2^A-3^H>0.}
\]

## 2. Positive rational fixed point

The affine word has the unique positive rational fixed point

\[
\boxed{C:=\frac{B}{Z}.}
\]

From

\[
2^A N'=3^H N+B
\]

we obtain

\[
B=ZN+2^A g.
\]

Hence

\[
\boxed{C=N+\frac{2^A g}{Z}.}
\]

Using `2^A=3^H+Z` also gives

\[
\boxed{C=N'+\frac{3^H g}{Z}>N'.}
\]

Thus every floor-increasing supercritical renewal segment lies below the positive rational cycle shadow of its own finite word.

## 3. Exact denominator

Because

\[
\gcd(Z,2^A)=\gcd(2^A-3^H,2^A)=1,
\]

the reduced denominator of

\[
\frac{2^A g}{Z}
\]

is exactly

\[
\boxed{\frac{Z}{\gcd(Z,g)}.}
\]

Therefore the reduced denominator of `C` is the same number:

\[
\boxed{\operatorname{den}(C)=\frac{Z}{\gcd(Z,g)}.}
\]

In particular,

\[
\boxed{C\in\mathbb N\iff Z\mid g.}
\]

## 4. Integer shadow implies an exact cycle

If `Z|g`, then

\[
C-N=2^A\frac gZ
\]

is a multiple of `2^A`. Hence `C` lies in the same exact length-`A` parity/valuation cylinder as `N`.

The affine word therefore acts on `C` by the same formula, and by construction

\[
\boxed{F(C)=C.}
\]

Thus `C` is a positive integer periodic point for that word (possibly with a smaller primitive period dividing the aggregate word).

Consequently

\[
\boxed{
(2^A-3^H)\mid(N'-N)
\Longrightarrow
\text{positive integer cycle.}
}
\]

Conversely, failure of the divisibility leaves a genuinely rational, non-integral cycle shadow.

## 5. The shadow cycle has its minimum at the renewal boundary

Let the actual interior block starts be

\[
X_0=N,
X_1,\ldots,X_m=N',
\]

with

\[
X_r>N'
\qquad(0<r<m).
\]

Let `F_r` be the affine prefix through the first `r` maximal blocks, with positive linear coefficient `a_r`, so

\[
X_r=F_r(N).
\]

Define the corresponding rational shadow states

\[
C_r:=F_r(C).
\]

Then

\[
\boxed{C_r-X_r=a_r(C-N).}
\]

Let `a` be the coefficient of the full aggregate word. Since the word is supercritical in the present multiplier convention,

\[
0<a<1,
\qquad
C-N'=a(C-N).
\]

For every proper interior boundary `r`, the suffix from `X_r` to `N'` is an actual decrease. Because every affine Collatz suffix has positive correction, its linear coefficient must be strictly less than `1`; otherwise its endpoint would exceed its start. Hence

\[
\frac a{a_r}<1,
\qquad
\boxed{a_r>a.}
\]

Therefore

\[
\begin{aligned}
C_r-C
&=(X_r-N')+(a_r-a)(C-N)\\
&>0.
\end{aligned}
\]

Thus

\[
\boxed{C_r>C\qquad(0<r<m).}
\]

So `C` is the strict minimum of the positive rational periodic shadow associated with the supercritical renewal word.

Equivalently, an aggregate-supercritical renewal segment is an integer orbit segment lying strictly below the minimum of a positive rational periodic orbit while following exactly the same finite word once.

## 6. Role in the terminal architecture

This theorem directly joins the two terminal branches:

- the periodic branch corresponds to integrality of a finite-word rational fixed point;
- every aggregate-supercritical aperiodic renewal segment carries the same positive rational periodic word, with its minimum at the renewal boundary, but with nontrivial denominator.

Thus a future unified theorem may seek to prove that repeated floor-increasing supercritical renewals force the shadow denominator

\[
\frac{2^A-3^H}{\gcd(2^A-3^H,N'-N)}
\]

to collapse to `1`, which would transfer the aperiodic branch into the periodic branch. No such denominator-collapse theorem is currently established here.
