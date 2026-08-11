# p-adic height barrier and structured-sum target

Date: 2026-08-11

Status: **obstruction analysis + refined theorem target**. This note explains why a direct generic p-adic approximation theorem does not presently close the harmonic mixed-place condition.

## 1. Rational correction approximants

At odd-event depth `q`, write

\[
c_q=\frac{B_q}{3^q},
\]

where

\[
\boxed{
B_q
=\sum_{i=0}^{q-1}2^{A_i}3^{q-1-i}.
}
\]

The last summand is `2^{A_{q-1}}`, so `3` does not divide `B_q`; hence the fraction is reduced.

For a fixed positive-integer start `n`, exact event formation gives

\[
\boxed{
v_2(n+c_q)=A_q.}
\]

Equivalently,

\[
\boxed{
|n+c_q|_2=2^{-A_q}.
}
\]

## 2. Archimedean size under the harmonic corridor

For a hypothetical nonperiodic first-descent survivor,

\[
\boxed{c_q=O_n(q^{1/9}).}
\]

Thus the ordinary rational height satisfies

\[
H(c_q)
=\max(B_q,3^q)
\le
3^q\,O_n(q^{1/9}).
\]

Also

\[
\lambda_q=\frac{2^{A_q}}{3^q}
\le
1+\frac{c_q}{n}
=O_n(q^{1/9}),
\]

so

\[
A_q
\le
q\log_2 3+rac19\log_2q+O_n(1).
\]

Consequently the 2-adic approximation scale

\[
2^{-A_q}
\]

is, at the critical boundary, essentially of order `3^{-q}` up to polynomial factors. This is the same exponential scale as the reciprocal height of `c_q`, again up to polynomial factors.

Therefore the approximation to the rational target `-n` is not automatically in a super-height regime where a generic p-adic irrationality theorem would yield a contradiction. Moreover the target itself is rational.

## 3. Why generic congruence counting is also insufficient

The formation condition may be written as

\[
\boxed{
B_q
\equiv
-n3^q+2^{A_q}
\pmod{2^{A_q+1}}.
}
\]

Together with

\[
0<B_q\le C_n3^qq^{1/9},
\]

this says that `B_q` is a relatively small positive integer in one high-resolution dyadic residue class.

However, if

\[
\lambda_q=2^{A_q}/3^q
\]

is very small, the admissible real interval contains many such residue lifts. Thus CRT or interval counting alone cannot exclude the hard core.

## 4. The structure that remains unused

The numerator is not an arbitrary integer:

\[
\boxed{
B_q
=2^{A_0}3^{q-1}
+2^{A_1}3^{q-2}
+\cdots
+2^{A_{q-1}}.
}
\]

It obeys the exact recursion

\[
\boxed{
B_{q+1}=3B_q+2^{A_q}.
}
\]

The remaining theorem must exploit this ordered positive `2`-`3` exponential-sum structure simultaneously with the dyadic residue condition and the harmonic real bound.

## 5. Refined structured-sum exclusion target

Prove that there are no `n>=3` and aperiodic increasing integer exponents

\[
0=A_0<A_1<\cdots
\]

for which the recursively defined positive integers

\[
B_0=0,
\qquad
B_{q+1}=3B_q+2^{A_q}
\]

satisfy simultaneously

\[
\boxed{
B_q=O_n(3^q q^{1/9})
}
\]

and

\[
\boxed{
B_q
\equiv
-n3^q+2^{A_q}
\pmod{2^{A_q+1}}
}
\]

for every `q`.

This is equivalent in content to the harmonic mixed-place hard core, but exposes the ingredient that generic approximation arguments ignore: `B_q` is an ordered positive exponential sum with a fixed recurrence.

## 6. Research consequence

Future progress should seek a lower bound, rigidity statement, or carry-growth theorem for this structured recurrence. Merely adding deeper parity congruences is circular, and merely invoking a generic p-adic approximation theorem does not currently use enough of the Collatz-specific structure.
