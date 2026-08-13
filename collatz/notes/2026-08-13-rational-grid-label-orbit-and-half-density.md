# Rational-grid label orbit and periodic high-bit half-density

Date: 2026-08-13

Status: **exact arithmetic theorem**.  It strengthens the endpoint rational-grid localization by describing how the grid label and the corresponding high-resolution 2-adic block evolve as the target resolution grows.  It is a late-lift structural lemma, not a Collatz proof.

## 1. Generic odd-denominator high-resolution coordinate

Let

\[
P=3^q
\]

and let `D` be a fixed integer.  For each sufficiently large `m`, define

\[
\boxed{W_m=[-P^{-1}D]_{2^m}},
\qquad 0\le W_m<2^m.
\]

Then there is an integer grid label `t_m` such that

\[
\boxed{PW_m+D=t_m2^m.}
\]

Once `2^m>|D|`, one may take the unique representative `0<=t_m<P` after the harmless sign convention implicit in `D` is fixed.  Equivalently, modulo `P`,

\[
\boxed{t_m\equiv D\,2^{-m}\pmod P.}
\]

This is exactly the grid label already present in the endpoint/high-block rational-grid localization.

## 2. One-bit resolution recursion

Compatibility of the 2-adic residues gives

\[
W_{m+1}=W_m+c_m2^m,
\qquad c_m\in\{0,1\}.
\]

Substitute this into the grid equations at resolutions `m` and `m+1`:

\[
PW_m+D=t_m2^m,
\]

\[
P(W_m+c_m2^m)+D=t_{m+1}2^{m+1}.
\]

After division by `2^m`,

\[
\boxed{t_m+Pc_m=2t_{m+1}.}
\]

Because `P` is odd,

\[
\boxed{c_m=t_m\bmod2.}
\]

Therefore

\[
\boxed{
t_{m+1}=\frac{t_m+P(t_m\bmod2)}2
}
\]

and, equivalently,

\[
\boxed{t_{m+1}\equiv2^{-1}t_m\pmod P.}
\]

Thus the target-resolution grid labels are not arbitrary at successive depths.  Every fixed prefix/endpoint difference follows one deterministic multiplication-by-`2^{-1}` orbit modulo `3^q`.

## 3. Effective modulus

Let

\[
s=v_3(D),
\qquad 0\le s<q,
\]

so that `P` does not divide `D`.  Then

\[
\gcd(t_m,P)=3^s
\]

for every `m`.  Dividing by `3^s` reduces the orbit to the unit group modulo

\[
\boxed{Q=3^{q-s}}.
\]

Hence the exact period is the multiplicative order of `2` modulo `Q`.

## 4. Exact period by LTE

For every `n>=1`,

\[
\boxed{\operatorname{ord}_{3^n}(2)=2\cdot3^{n-1}.}
\]

Indeed, LTE gives

\[
v_3(2^{2\cdot3^{n-1}}-1)
=v_3(4^{3^{n-1}}-1)
=v_3(4-1)+v_3(3^{n-1})
=n.
\]

The order modulo `3^n` therefore gains exactly a factor three at every lift from `3^(n-1)` to `3^n`, starting from order two modulo three.

Consequently, if `s=v_3(D)<q`, the grid-label orbit has exact period

\[
\boxed{
T=2\cdot3^{q-s-1}.
}
\]

## 5. Half-density of high lift bits

Over one period, `t_m/3^s` runs through all units modulo `Q=3^(q-s)`, because `2` is a primitive root modulo every power of three.

Since `Q` is odd, the involution

\[
u\mapsto Q-u
\]

pairs the units and reverses parity.  Therefore exactly half of the unit representatives in `[0,Q)` are odd and half are even.

Multiplication by the odd factor `3^s` preserves parity.  Since

\[
c_m=t_m\bmod2,
\]

we obtain the exact periodic density

\[
\boxed{
\frac1T\sum_{j=0}^{T-1}c_{m+j}=\frac12.
}
\]

Thus, whenever `P` does not divide `D`, the high-resolution coordinate has infinitely many nonzero binary lift bits and in fact exactly half of the bits in every full eventual period are one.

## 6. Special denominator-cancellation case

If

\[
P\mid D,
\]

then the odd denominator cancels and `-D/P` is an ordinary integer in `Z_2`.  Its binary expansion is eventually zero when that integer is nonnegative and eventually one when it is negative.  Hence the half-density theorem is specifically the nonintegral odd-denominator case `v_3(D)<q`.

## 7. Consequence for defect/suffix direct sums

In the high-resolution defect-cylinder formulation, the high defect block `W` satisfies an equation of the same form

\[
PW+(y-y^*)=t2^m.
\]

Therefore, unless the endpoint difference is divisible by the full prefix odd multiplier `P`, the defect-side high block carries a periodic 50%-density stream of nonzero high bits as target depth grows.

A small ordinary canonical start cannot simply wait for that defect translation to stabilize.  In the collision-free direct-sum representation

\[
\mathcal R_{\rm cell,K}=\mathcal A+\mathcal B\pmod{2^K},
\]

the suffix coordinate must cancel the entire periodic high-bit tail, including carries, so that the final canonical residue has zero lift bits above the ordinary start length.

This strengthens the late-lift target from

> some high bit must be controlled

into

> a nonintegral defect translation supplies a deterministic periodic high-bit forcing pattern of density one half, and the suffix channel must match its exact complement.

## 8. Limitation

The theorem concerns the binary digits of the high-resolution defect/query coordinate, not the Collatz parity symbols themselves.  A periodic binary expansion of a rational 2-adic start does not by itself imply an eventually periodic Collatz parity sequence; treating those as equivalent would run into the classical rationality/periodicity difficulty for the 2-adic Collatz conjugacy.

Therefore the remaining task is an exact carry/suffix incompatibility theorem: show that a coefficient-admissible suffix cannot supply the required complementary periodic lift pattern for an ordinary small start, except in controlled exceptional cases.
