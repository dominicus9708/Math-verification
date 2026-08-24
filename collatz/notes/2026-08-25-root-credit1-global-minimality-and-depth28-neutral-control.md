# Root credit-1 global minimality filter and depth-28 neutral control

Date: 2026-08-25

Status: globally safe minimal-counterexample lemma plus finite exact diagnostics.  This note does **not** prove the Collatz conjecture and does not claim an asymptotic entropy gap.

## 1. Root credit-1 lemma

For a length-k parity prefix w with q odd entries, write

\[
T^k(N)=\frac{3^qN+R_w}{2^k}.
\]

Suppose another length-k word u has the same q and

\[
R_u-R_w=3^q.
\]

Then

\[
3^q(N-1)+R_u=3^qN+R_w,
\]

hence

\[
\boxed{T_u^k(N-1)=T_w^k(N)}.
\]

The integerization is automatic.  Since the right-hand side numerator is divisible by \(2^k\), the left-hand side is as well; by the parity-vector/canonical-residue bijection, u is the actual length-k parity prefix of \(N-1\), not a merely formal affine branch.

Therefore, for a hypothetical minimal counterexample \(N>1\), **no root prefix may admit a credit-1 sibling**.  Unlike arbitrary later-block Hensel replacement, this statement has no pullback problem and no finite headroom restriction: the alternate start is exactly \(N-1\).

## 2. Synchronous adjacent-start recurrence

A minimal counterexample is odd.  Thus \(N\) and \(N-1\) differ only in binary bit 0; all higher binary lift bits are identical.

At canonical depth k let the two endpoint states be

\[
(y,\bar y,q,\bar q).
\]

Given their common next binary lift bit \(c\in\{0,1\}\), set

\[
Y=y+c3^q,\qquad \bar Y=\bar y+c3^{\bar q}.
\]

The actual next parity bits are

\[
b=c\oplus(y\bmod2),\qquad
\bar b=c\oplus(\bar y\bmod2),
\]

and each endpoint is advanced by the ordinary accelerated Collatz branch.  A credit-1 merger occurs exactly when after some depth

\[
y=\bar y,\qquad q=\bar q.
\]

This recurrence reproduces the independently enumerated coefficient-surviving credit-1-avoidance counts exactly:

\[
1,1,2,3,4,7,11,16,31,52,103,182,297,593,1049,1720,3439,6104,
12199,22258,38044,76057,137852,234485,468856,849371,1445382,2890278
\]

for depths 1 through 28.

## 3. Important entropy audit

The depth-22 count \(76057\) by itself gives a finite effective exponent near 0.737, but this must **not** be read as the asymptotic entropy of the credit-1 filter.

Coefficient survival alone has counts

- H=10: 64,
- H=18: 7495,
- H=22: 93222,
- H=24: 286581,
- H=26: 1037374,
- H=28: 3524586.

Conditioning on coefficient survival, the credit-1 avoidance fractions are therefore approximately

- H=10: 0.812500,
- H=18: 0.814410,
- H=22: 0.815870,
- H=24: 0.818215,
- H=26: 0.818770,
- H=28: 0.820033.

Thus most of the apparent finite exclusion exponent came from the coefficient-survival ballot constraint.  The current data do not justify any positive asymptotic entropy gap coming from credit-1 avoidance alone.

## 4. Exact same-integer ternary cross-base check at H=28

The companion certificate

`collatz/src/root_credit1_depth28_crossbase_certificate.cpp`

intersects the credit-1-avoiding coefficient language with the exact ternary selector multiplicities modulo \(2^{28}\).

Ambient coefficient language:

\[
3524586.
\]

Credit-1-avoiding part:

\[
2890278,
\]

so the conditional fraction is

\[
\frac{2890278}{3524586}=0.820033331574\ldots.
\]

For the current m=44 selector layer, the previous coefficient-survival intersection was

\[
923497419313,
\]

whereas adding root credit-1 avoidance leaves

\[
\boxed{757298661081}.
\]

Hence

\[
\frac{757298661081}{923497419313}
=0.820033326833\ldots.
\]

For the two unresolved m=45 affine blocks, the corresponding figures are

\[
1847897870486
\]

and

\[
\boxed{1515337963334},
\]

with conditional fraction

\[
0.820033394451\ldots.
\]

These agree with the ambient conditional fraction to far better than one part in \(10^6\).

## 5. Interpretation

Root credit-1 avoidance is a particularly clean **global** minimality condition and should be retained as a free filter in every later computation.

However, the exact H=28 cross-base diagnostic gives no evidence that this condition by itself supplies the missing ternary-dyadic transversality.  It behaves almost perfectly neutrally with respect to the current ternary selector.

Therefore it is demoted from a candidate terminal entropy mechanism to a globally safe auxiliary root filter.  The next audit should test whether the small extra part of full root-Hensel maximality (credits greater than 1) has any genuinely non-neutral cross-base effect before investing in deeper root-max enumeration.
