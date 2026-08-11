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

## 5. Role in the terminal architecture

This theorem directly joins the two terminal branches:

- the periodic branch corresponds to integrality of a finite-word rational fixed point;
- every aggregate-supercritical aperiodic renewal segment carries the same fixed point but with nontrivial denominator.

Thus a future unified theorem may seek to prove that repeated floor-increasing supercritical renewals force the shadow denominator

\[
\frac{2^A-3^H}{\gcd(2^A-3^H,N'-N)}
\]

to collapse to `1`, which would transfer the aperiodic branch into the periodic branch. No such denominator-collapse theorem is currently established here.
