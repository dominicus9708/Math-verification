# R2 synthetic skew hard-core control

Date: 2026-08-12

Status: **synthetic countercontrol for proof architecture**. This note constructs an infinite admissible R2 skew path satisfying the local transition, harmonic-growth, displacement-area, and critical-density conditions simultaneously. It is not claimed to come from a positive ordinary integer. Its purpose is to prove that these non-naturalness conditions alone cannot exclude R2.

## 1. Critical driver

Put

\[
\gamma:=\log_2 3,
\qquad
r_i:=\lfloor(i+1)\gamma\rfloor-\lfloor i\gamma\rfloor\in\{1,2\}.
\]

The binary driver `r_i-1` has slope

\[
\gamma-1>\frac12.
\]

Hence two consecutive values `r_i=1` are impossible. Indeed, if `r_i=r_{i+1}=1`, then

\[
\lfloor(i+2)(\gamma-1)\rfloor-\lfloor i(\gamma-1)\rfloor=0,
\]

while

\[
2(\gamma-1)>1,
\]

contradiction. Therefore an index with `r_i=2` occurs at least once in every two consecutive driver positions.

## 2. Construct a logarithmic skew path

Let the target height be

\[
h_i:=\lfloor\log_2(i+2)\rfloor.
\]

Set `s_0=0` and recursively define

\[
s_{i+1}:=
\begin{cases}
s_i+1,&r_i=2\text{ and }s_i<h_i,\\
s_i,&\text{otherwise}.
\end{cases}
\]

Because target increases occur only logarithmically and `r_i=2` is never absent for more than one step, the delayed tracking error is bounded. Thus

\[
\boxed{s_i=\log_2 i+O(1).}
\]

The R2 local inequality is automatic:

- when `r_i=1`, `s_{i+1}=s_i`;
- when `r_i=2`, `s_{i+1}` is either `s_i` or `s_i+1`.

Hence

\[
\boxed{0\le s_{i+1}\le s_i+r_i-1.}
\]

## 3. Corresponding valuations are valid

Define

\[
v_i:=s_i+r_i-s_{i+1}.
\]

Then

\[
v_i\ge1
\]

for every `i`. Thus the constructed infinite skew path defines an ordinary infinite locally admissible Syracuse valuation code.

Moreover

\[
A_i=\lfloor i\gamma\rfloor-s_i
=i\gamma-O(\log i)\to\infty,
\]

so the associated Bernstein series converges in `Z_2`.

## 4. Harmonic condition

Since

\[
s_i=\log_2 i+O(1),
\]

we have

\[
2^{-s_i}=\Theta(i^{-1}).
\]

Therefore

\[
\boxed{
\sum_{i<q}2^{-s_i}=O(\log q).
}
\]

In particular

\[
\boxed{
\sum_{i<q}2^{-s_i}=O(q^{1/9}).
}
\]

Thus the exact harmonic necessary condition derived for an R2 positive-integer survivor is satisfied with room to spare.

## 5. Displacement area and critical density

The logarithmic path satisfies

\[
\boxed{
\sum_{i<q}s_i=q\log_2 q+O(q).
}
\]

Hence it satisfies the required lower area bound

\[
\sum_{i<q}s_i\ge\frac89q\log_2 q-O(q).
\]

At the same time

\[
\boxed{\frac{s_i}{i}\to0,}
\]

so it also satisfies the rational-divergent critical-density requirement

\[
\liminf\frac{s_i}{i}=0.
\]

## 6. Exact 2-adic value

The path defines

\[
\boxed{
\Phi(s)
=-\sum_{i=0}^{\infty}
\frac{2^{\lfloor i\gamma\rfloor-s_i}}{3^{i+1}}
\in\mathbb Z_2.
}
\]

Every finite prefix is a legitimate Collatz valuation code and therefore has a nonempty exact positive residue class.

What is not known, and is not asserted here, is that the infinite 2-adic value satisfies

\[
\Phi(s)\in\mathbb N.
\]

## 7. Proof-architecture consequence

This synthetic control establishes that the following four properties are mutually consistent:

\[
\boxed{
\begin{array}{l}
0\le s_{i+1}\le s_i+r_i-1,\\
\sum_{i<q}2^{-s_i}=O(q^{1/9}),\\
\sum_{i<q}s_i=\Omega(q\log q),\\
\liminf s_i/i=0.
\end{array}
}
\]

Therefore no proof may claim that the local skew dynamics, harmonic escape, displacement-area growth, and critical-density condition are contradictory by themselves.

The genuinely unresolved R2 condition is

\[
\boxed{\Phi(s)\in\mathbb N_{>1}.}
\]

This synthetic control is a deliberate negative test: any future proposed R2 proof that does not use the ordinary-integer naturalness condition (or an equivalent genuinely global arithmetic condition) must fail on this constructed path.