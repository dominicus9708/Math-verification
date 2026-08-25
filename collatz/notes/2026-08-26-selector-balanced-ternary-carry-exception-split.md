# Selector balanced-ternary carry exception split

Date: 2026-08-26

Status: **exact carry representation + finite exceptional-set bound.**  This note converts the high-resolution ternary-selector Riesz product into a balanced-ternary carry process on dyadic frequencies.  It gives an explicit small structured exceptional family at the `m=45`, address-exhaustion scale.  It does not yet control the Beatty-boundary transform on that family and is not a Collatz proof.

## 1. Centered dyadic orbit

Let

\[
M=2^L,
\qquad t\text{ odd}\pmod M,
\]

and define the centered representative

\[
a_i=\operatorname{cent}_M(t3^i),
\qquad -\frac M2<a_i<\frac M2.
\]

Because `M` is even and `t3^i` is odd, the endpoints `+-M/2` never occur.

There is therefore a unique carry digit

\[
c_i\in\{-1,0,1\}
\]

such that

\[
\boxed{
a_{i+1}=3a_i-c_iM.}
\]

More explicitly,

\[
c_i=
\begin{cases}
-1,&a_i<-M/6,\\
0,&|a_i|<M/6,\\
1,&a_i>M/6.
\end{cases}
\]

Thus multiplication by three on the centered dyadic circle is exactly a balanced-ternary carry automaton.

## 2. Balanced-ternary expansion identity

Iterating the recurrence gives

\[
a_m
=3^m a_0
-M\sum_{j=0}^{m-1}c_j3^{m-1-j}.
\]

Equivalently,

\[
\boxed{
\frac{a_0}{M}
=
\sum_{j=0}^{m-1}\frac{c_j}{3^{j+1}}
+
\frac{a_m}{3^mM}.
}
\]

Hence `c_0,...,c_(m-1)` are precisely the first `m` balanced-ternary digits of the centered rational frequency `a_0/M`.

For a forced-OO resonant frequency

\[
t=h3^{q'},\qquad h\text{ odd},
\]

multiplication by the fixed odd unit `3^q'` permutes the odd residues modulo `2^L`.  Therefore all cardinality statements below are unchanged in the resonant parameter `h`.

## 3. Selector attenuation from nonzero carries

The normalized `m`-selector Riesz factor has magnitude

\[
|P_{m,L}(t)|
=
\prod_{i=0}^{m-1}
\left|\cos\left(\pi\frac{a_i}{M}\right)\right|.
\]

Whenever `c_i` is nonzero, `|a_i|>M/6`, so

\[
\left|\cos\left(\pi\frac{a_i}{M}\right)\right|
\le\cos(\pi/6)=\frac{\sqrt3}{2}.
\]

Let

\[
C_m(t):=\#\{0\le i<m:c_i\ne0\}.
\]

Then

\[
\boxed{
|P_{m,L}(t)|
\le
\left(\frac{\sqrt3}{2}\right)^{C_m(t)},
}
\]

or, without radicals,

\[
\boxed{
|P_{m,L}(t)|^2
\le
\left(\frac34\right)^{C_m(t)}.
}
\]

This is a deterministic bound for every frequency, not an average statement.

## 4. Cylinder-count bound for sparse carries

Fix a carry word `c_0,...,c_(m-1)`.  From the expansion identity and `|a_m|<M/2`, the initial centered residue must lie in an interval of length

\[
\frac{M}{3^m}.
\]

An open interval of this length contains at most

\[
\left\lceil\frac{M}{3^m}\right\rceil
\]

integers, hence at most that many odd residues.

There are at most

\[
\binom mj2^j
\]

balanced carry words with exactly `j` nonzero digits.  Therefore the set

\[
\mathcal E_c
:=\{t\text{ odd}:C_m(t)\le c\}
\]

obeys the exact upper bound

\[
\boxed{
|\mathcal E_c|
\le
\left\lceil\frac{2^L}{3^m}\right\rceil
\sum_{j=0}^c\binom mj2^j.
}
\]

On its complement,

\[
\boxed{
|P_{m,L}(t)|^2
\le
\left(\frac34\right)^{c+1}.
}
\]

Thus the selector high shell has an explicit `small structured exception / deterministic attenuation` split.

## 5. Exact m=45 address-exhaustion numbers

For the reduced selector coordinate at complete address exposure,

\[
m=45,
\qquad L=72.
\]

Since

\[
1<\frac{2^{72}}{3^{45}}<2,
\]

we have

\[
\left\lceil\frac{2^{72}}{3^{45}}\right\rceil=2.
\]

There are exactly `2^71` odd frequency residues modulo `2^72`.

Some useful exact exceptional-set bounds are

\[
|\mathcal E_{10}|\le7,564,040,793,766,
\]

\[
|\mathcal E_{15}|\le29,550,148,215,811,750,
\]

\[
|\mathcal E_{20}|\le10,507,594,242,179,903,142.
\]

For `c=20`, this upper bound is below `0.004451 * 2^71`; equivalently fewer than about `0.4451%` of odd frequencies are allowed to have at most twenty nonzero carries by this cylinder count.

On every frequency outside this exceptional family,

\[
\boxed{
|P_{45,72}(t)|^2\le(3/4)^{21},
}
\]

so

\[
|P_{45,72}(t)|\lesssim0.04877.
\]

The decimal is only descriptive; the certificate uses the exact rational power.

## 6. DSD audit interpretation

The high-shell selector channel can now be retained without pretending it is globally mixed.

- **state:** centered residue `a_i`;
- **transition:** `a_(i+1)=3a_i-c_i2^L`;
- **cross-base channel:** balanced carry digit `c_i`;
- **good set:** many nonzero carry digits, giving deterministic Riesz attenuation;
- **exception set:** few nonzero balanced-ternary digits, with an explicit cardinality bound.

This is the correct high-resolution descriptor because it preserves the arithmetic structure discarded by total `L2` energy.

## 7. Remaining theorem

This split does not close the cross-spectrum.  The unresolved task is now narrower:

> control the ordinary/oriented Beatty boundary transforms on the sparse balanced-ternary carry families `E_c`, while using selector attenuation on their complement.

The boundary reciprocity identity already rewrites near-one boundary factors as short-arc conditions on residues

\[
k[-2^{-m}]_{3^\ell}\pmod{3^\ell}.
\]

The next calculation should intersect those ternary inverse-two constraints with the balanced-carry cylinders above.  That is the concrete form of the resonant triadic carry-cancellation problem.

Certificate:

`collatz/src/selector_balanced_ternary_carry_exception_certificate.py`.
