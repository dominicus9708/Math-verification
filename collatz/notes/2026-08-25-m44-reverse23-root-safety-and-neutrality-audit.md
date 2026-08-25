# m=44 reverse-23 root-safety and neutrality audit

Date: 2026-08-25

Status: **safe root-level minimality sieve + exact finite cross-mass diagnostic.** This note corrects an initially plausible but ultimately incorrect audit concern that the reverse-23 filter might only prove contraction relative to the later endpoint `T^2(N)`.

## 1. Why the apparent pullback problem does not apply

Every m=44 core start is `3 mod 4`, so the first two accelerated Collatz steps are universally odd. Therefore

\[
y=T^2(N)=\frac{9N+5}{4}.
\]

The reverse-23 certificate writes the low ternary state as

\[
y\equiv 9S+8 \pmod{3^{25}},
\]

because for

\[
N=4\cdot3^{44}+3+4\sum_{i=0}^{43}a_i3^i,
\]

we have

\[
T^2(N)=9\cdot3^{44}+9\sum_{i=0}^{43}a_i3^i+8,
\]

and the high selector digits above `a_22` disappear modulo `3^25` after multiplication by 9.

After `q` inverse-odd steps and `E` extra inverse-even doublings, a positive reverse ancestor has the affine form

\[
M=\frac{2^{q+E}y-C}{3^q},\qquad C>0.
\]

The production code does **not** merely demand `M<y`. It checks

\[
E\le \operatorname{contraction\_budget}(q-2).
\]

By definition this means

\[
2^{(q-2)+E}<3^{q-2},
\]

or equivalently

\[
\boxed{9\,2^{q+E}<4\,3^q}.
\]

The subtraction of two from `q` is precisely the compensation for the two universal odd steps from `N` to `T^2(N)`.

Hence this is a root-level contraction criterion, unlike an invalid argument of the form `M<T^2(N) => M<N`.

## 2. Finite +5 audit

Dropping the favorable negative correction `-C` gives the safe upper bound

\[
M<\frac{2^{q+E}(9N+5)}{4\,3^q}.
\]

Thus it is sufficient that

\[
\bigl(4\,3^q-9\,2^{q+E}\bigr)N>5\,2^{q+E}.
\]

The companion certificate checks every possible production depth `q=3,...,25` at its largest allowed `E`.

The worst small-start threshold occurs at

\[
(q,E)=(14,7)
\]

and is only

\[
\boxed{N\ge41}.
\]

The actual m=44 floor is

\[
\boxed{N_{\min}=4\cdot3^{44}+3=3,939,083,608,734,444,931,527},
\]

so the additive `+5` term is harmless by an enormous margin.

Certificate:

`collatz/src/m44_reverse23_root_safety_audit.cpp`

## 3. Exact reverse-23 and binary cross mass

The existing certificate `m44_reverse23_binary26_cross_mass.cpp` gives

- low ternary masks: `2^23 = 8,388,608`;
- reverse-forbidden low masks: `299,740`;
- ambient reverse survival fraction:

\[
\frac{8,388,608-299,740}{8,388,608}
=0.964268207550048828\ldots;
\]

- depth-26 binary coefficient-only mass:

\[
1,087,765,074,138;
\]

- exact reverse/binary cross mass:

\[
1,048,897,463,045.
\]

Thus reverse-23 removes an additional

\[
\boxed{38,867,611,093}
\]

weighted selector starts from the binary-only mass, or approximately `3.573162%` of that binary-only mass.

## 4. Cross-base neutrality audit

Conditioned on the binary coefficient language, the reverse survival fraction is

\[
\frac{1,048,897,463,045}{1,087,765,074,138}
=0.964268377412465960\ldots.
\]

Compared with the ambient reverse survival fraction, the relative shift is only

\[
\boxed{+0.176156816\ \text{ppm}}.
\]

The exact cross-multiplication excess over perfect neutrality is

\[
1,048,897,463,045\cdot2^{23}
-
1,087,765,074,138\cdot(2^{23}-299,740)
=
1,549,966,495,576.
\]

This number is nonzero, so the two finite conditions are not exactly independent, but the relative effect is sub-ppm.

## 5. Audit conclusion

The reverse-23 filter receives a different verdict from the unsafe later-block pullback constructions:

1. **Keep it as logically safe.** The `q-2` contraction budget correctly accounts for the universal two-step entrance and produces a smaller positive ancestor relative to the original root start.
2. **Keep it as a useful finite sieve.** It removes about 3.573% of the binary-only m=44 mass.
3. **Do not promote it to the missing transversality mechanism.** Its interaction with the depth-26 binary coefficient language is almost perfectly neutral.
4. The stronger main line remains the direct cross-place cylinder sieve, where forward and reverse affine data are combined at the root level rather than merely intersecting two almost-independent marginal filters.

The companion audit certificate was compiled and run locally and returned `PASS` before this note was committed.
