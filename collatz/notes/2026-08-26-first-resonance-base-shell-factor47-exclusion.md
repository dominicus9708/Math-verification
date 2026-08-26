# First resonance: no 31-odd mechanical run in the base dyadic shell

Date: 2026-08-26

Status: **exact finite-factor certificate + global support lower bound inside the repaired first-global-resonance branch.** This is not a proof of the Collatz conjecture.

## 1. From displacement to an actual shell condition

The scaled dyadic-shell theorem gives, for every proper odd ordinal,

\[
2^{d_j}N<x_j<2^{d_j+1}N.
\]

Hence

\[
\boxed{d_j=0\iff N<x_j<2N.}
\]

The first-resonance start bound gives

\[
N<{4\over3}2^{71}.
\]

Therefore every `d=0` odd state lies in the fixed broad shell

\[
\boxed{
2^{71}<x<{8\over3}2^{71}<2^{73}.
}
\]

If consecutive odd ordinals all have `d=0`, their actual odd positions equal the corresponding mechanical positions, so the accelerated parity factor on that interval is exactly the phase-shifted first-resonance mechanical parity factor.

## 2. Why a length-47 factor is a finite problem

For a rational mechanical gap word

\[
m_n=\left\lfloor{(n+1)P\over Q}\right\rfloor-
\left\lfloor{nP\over Q}\right\rfloor,
\qquad
P=A-Q,
\]

a length-`K` factor changes only when the phase residue crosses one of the `K+1` breakpoints

\[
-kP\pmod Q.
\]

At `K=47` there are 48 gap factors, but after converting them to odd-start accelerated parity factors of 47 time steps there are only

\[
\boxed{30}
\]

distinct parity factors.

Each 47-bit parity factor has one canonical residue modulo `2^47`. Every integer in the broad base shell with that factor is therefore

\[
x=\rho+t2^{47}.
\]

The exact shell intersection over all 30 factors contains

\[
\boxed{838,860,804}
\]

integers.

This is a finite certificate set. It is not an unbounded Collatz scan.

## 3. Exact descent certificate

The companion C++ certificate applies the exact accelerated map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2
\end{cases}
\]

to every one of the `838,860,804` shell candidates.

Every candidate reaches a value below

\[
2^{71}
\]

within at most

\[
\boxed{461}
\]

accelerated steps.

Thus, under the already-used published finite base below `2^71`, every such candidate converges. Equivalently, no state on a hypothetical counterexample orbit can begin one of these length-47 mechanical factors while remaining in the base shell.

## 4. Translation back to odd ordinals

For 30 consecutive mechanical gaps,

\[
\left\lfloor {30A\over Q}\right\rfloor=47.
\]

Therefore 31 consecutive odd states with

\[
d_j=0
\]
would determine at least 47 accelerated parity steps starting from a base-shell state. Section 3 excludes this.

Hence

\[
\boxed{
\text{there is no run of 31 consecutive odd ordinals with }d_j=0.
}
\]

So every zero-displacement run has length at most 30.

## 5. Global support consequence

Let

\[
r_* = \#\{j:d_j>0\}.
\]

The `Q-r_*` zero positions are split by the positive positions into at most `r_*+1` zero-runs, each of length at most 30. Thus

\[
Q-r_*\le30(r_*+1).
\]

Therefore

\[
\boxed{
r_*\ge
\left\lceil{Q-30\over31}\right\rceil
=2,324,433,290.
}
\]

This replaces the previous small finite terminal lower bound as the strongest global **lower** bound on displaced odd ordinals in the first-resonance branch.

The independent global defect-budget theorem still gives the upper bound

\[
r_*\le42,009,999,999.
\]

Thus the support is now trapped by

\[
\boxed{
2,324,433,290
\le r_*
\le42,009,999,999.
}
\]

## 6. Coarse defect consequence

Every positive displacement contributes more than `1/12` to the normalized correction defect. Therefore

\[
\boxed{
{E\over3^Q}
>{r_*\over12}
>193,702,774.
}
\]

This does not yet exceed the full first-resonance budget

\[
E/3^Q<4,314,000,000.
\]

So this theorem is a substantial pruning result but not first-resonance closure by itself.

## 7. Why this is structurally different from an unbounded numerical search

The finite scan is attached to a proved factor-complexity reduction:

\[
\boxed{
7.2\times10^{10}\text{ possible phases}
\longrightarrow
30\text{ length-47 factor types}
\longrightarrow
838,860,804\text{ finite shell lifts}.
}
\]

The conclusion is a universal forbidden-pattern theorem:

\[
\boxed{
\text{a counterexample cannot shadow the mechanical word in the base shell for 31 odd ordinals.}
}
\]

The certificate is therefore used as a finite base lemma inside a structural proof, not as evidence obtained by testing successively larger arbitrary starting integers.

## 8. DSD chain

The DSD proof description is now

\[
\boxed{
\text{displacement }d=0
\to
\text{actual base dyadic shell}
\to
\text{mechanical factor}
\to
\text{finite canonical residue set}
\to
\text{forbidden counterexample state}.
}
\]

This is a direct example of replacing trajectory enumeration by a finite quotient of the state description.

Companion certificate:

`collatz/src/first_resonance_base_shell_factor47_certificate.cpp`.
