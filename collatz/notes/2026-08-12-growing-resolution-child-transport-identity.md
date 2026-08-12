# Exact child-transport identity for growing-resolution survivor mass

Date: 2026-08-12

Status: **exact set/aggregation transport identity**. It expresses the change in ternary-core survivor mass when dyadic resolution is increased by one bit as the sum of a purely dynamical child-branching term and a binary/ternary cross-correlation term. This provides a precise target for a growing-resolution contraction theorem. It does not prove Collatz.

## 1. Nested dyadic survivor cylinders

For representatives

\[
N=4Y+3,
\qquad
Y=3^{44}+\sum_{i=0}^{d-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

let the reduced dyadic modulus at resolution `L>=3` be

\[
M_L:=2^{L-2}.
\]

Let

\[
R_L\subseteq\mathbb Z/M_L\mathbb Z
\]

be any exact or conservative nested dangerous-cylinder family, with

\[
R_{L+1}\subseteq\pi^{-1}(R_L),
\]

where `pi` is reduction modulo `M_L`.

A parent residue

\[
r\pmod{M_L}
\]

has two children modulo

\[
M_{L+1}=2M_L:
\]

\[
r,
\qquad
r+M_L.
\]

## 2. Dynamical child indicators

For a retained parent `r in R_L`, define

\[
b_0(r):=1_{R_{L+1}}(r),
\qquad
b_1(r):=1_{R_{L+1}}(r+M_L).
\]

Define the child multiplicity and child preference

\[
\boxed{
m(r):=b_0(r)+b_1(r)\in\{0,1,2\},
}
\]

\[
\boxed{
v(r):=b_0(r)-b_1(r)\in\{-1,0,1\}.
}
\]

Interpretation:

- `m=2`: both dyadic lifts remain dangerous;
- `m=1`: exactly one new binary bit remains dangerous;
- `m=0`: the whole parent cylinder dies;
- when `m=1`, `v=+1` means child 0 survives and `v=-1` means child 1 survives.

These quantities belong entirely to the **dyadic dynamical channel**.

## 3. Ternary representative child counts

Inside the same parent residue define

\[
c_0(r)
:=\#\{a:Y(a)\equiv r\pmod{2M_L}\},
\]

\[
c_1(r)
:=\#\{a:Y(a)\equiv r+M_L\pmod{2M_L}\}.
\]

The parent mass and its next-bit imbalance are

\[
\boxed{
c(r):=c_0(r)+c_1(r),
}
\]

\[
\boxed{
u(r):=c_0(r)-c_1(r).
}
\]

Here `u(r)` is the exact **ternary-to-binary next-bit imbalance** inside the parent fiber.

If `u=0`, the ternary representative mass is perfectly balanced between the two new binary children. If `|u|=c`, every representative in the parent chooses the same next bit.

## 4. Exact one-bit transport identity

Let

\[
C_L
:=\#\{a:Y(a)\bmod M_L\in R_L\}
=\sum_{r\in R_L}c(r).
\]

At the next resolution,

\[
C_{L+1}
=\sum_{r\in R_L}
\bigl(b_0(r)c_0(r)+b_1(r)c_1(r)\bigr).
\]

Use

\[
b_0=\frac{m+v}{2},
\qquad
b_1=\frac{m-v}{2},
\]

and

\[
c_0=\frac{c+u}{2},
\qquad
c_1=\frac{c-u}{2}.
\]

Then, exactly,

\[
\boxed{
C_{L+1}
=\frac12
\sum_{r\in R_L}
\left[m(r)c(r)+v(r)u(r)\right].
}
\]

Equivalently, the one-resolution loss is

\[
\boxed{
C_L-C_{L+1}
=\sum_{r\in R_L}
\left[
\left(1-\frac{m(r)}2\right)c(r)
-\frac12v(r)u(r)
\right].
}
\]

This is the desired discrete transport / discrete-derivative formula.

## 5. Meaning of the two terms

The first term

\[
\left(1-\frac m2\right)c
\]

is purely dynamical pruning.

- `m=0` removes the entire parent mass;
- `m=1` would remove exactly half the mass if the ternary next bit were balanced;
- `m=2` removes nothing at this resolution.

The second term

\[
-\frac12vu
\]

is the **cross-place correction**.

For a one-child parent:

- if ternary mass is biased toward the surviving child, `vu>0`, pruning is weaker;
- if it is biased toward the rejected child, `vu<0`, pruning is stronger;
- if `u=0`, exactly one-half of the parent mass survives.

Thus the hard part of growing-resolution verification is now isolated as one signed correlation between

\[
\boxed{
\text{dynamical child preference }v
\quad\text{and}\quad
\text{ternary next-bit imbalance }u.
}
\]

## 6. One-child contraction corollary

Let

\[
D_L:=\{r\in R_L:m(r)=1\}
\]

be the one-child parent set.

For `r in D_L`, the retained mass is

\[
\frac{c(r)+v(r)u(r)}2.
\]

Suppose for some `delta>0` one proves the aggregate correlation inequality

\[
\boxed{
\sum_{r\in D_L}v(r)u(r)
\le
(1-2\delta)
\sum_{r\in D_L}c(r).
}
\]

Then the total mass retained from one-child parents is at most

\[
(1-\delta)
\sum_{r\in D_L}c(r).
\]

If in addition one-child parents carry at least an `eta` fraction of the current survivor mass,

\[
\sum_{r\in D_L}c(r)\ge\eta C_L,
\]

and zero-child pruning is ignored, then

\[
\boxed{
C_{L+1}
\le
(1-\delta\eta)C_L.
}
\]

Any uniform positive lower bounds on `delta` and `eta` over a growing range of resolutions therefore yield exponential contraction of the representative survivor mass.

## 7. Why this is stronger than fixed-resolution mixing

Fixed-resolution mixing only says that, after releasing many ternary selectors while keeping `L` fixed, the **unconditional** residue distribution approaches uniformity.

The new identity asks for something more targeted:

> conditional on already lying in a dangerous parent cylinder, how predictable is the *next* binary bit of the ternary subset sum relative to the unique dangerous child?

This is exactly the conditional cross-base information that the fixed-resolution theorem discards.

## 8. Fourier interpretation of the imbalance channel

The function `u(r)` is a signed lift count. It can be written as

\[
\boxed{
u(r)
=\sum_{a:\,Y(a)\equiv r\;(M_L)}
(-1)^{\lfloor Y(a)/M_L\rfloor}.
}
\]

Thus it is the new-bit Walsh/Fourier component of the ternary subset-sum measure over the parent fiber.

The correlation

\[
\sum_{r\in D_L}v(r)u(r)
\]

is therefore the one-bit transfer version of the full cross-spectrum introduced in `2026-08-12-growing-resolution-cross-spectrum-identity.md`.

The two formulations are equivalent in purpose:

- the full Fourier identity describes compatibility at one fixed resolution globally;
- the child-transport identity describes how that compatibility changes when the resolution grows by one bit.

## 9. Proof-program target

The next terminal-style theorem is no longer vaguely “show survivor cylinders shrink.” It is the concrete pair of estimates

\[
\boxed{
\sum_{r\in D_L}c(r)\ge\eta C_L
}
\]

and

\[
\boxed{
\sum_{r\in D_L}v(r)u(r)
\le(1-2\delta)\sum_{r\in D_L}c(r)
}
\]

for enough growing resolutions `L`.

The first is a property of the Collatz survivor tree; the second is the genuinely cross-base `2`/`3` compatibility statement.

This decomposition is aligned with the intended proposition/set/static-aggregation method: each channel is defined independently, and only the exact compatibility term is carried into the global conclusion.