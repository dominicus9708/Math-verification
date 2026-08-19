# Selector collision full-orbit renormalization

Date: 2026-08-20

Status: **exact corollary of the existing selector Fourier full-orbit product law, specialized to the Stage-4 collision-halving energy.** This is not a proof of the Collatz conjecture.

## 1. Collision-halving energy

For the uniform ternary-selector measure

\[
\mu_{m,r}(x)=2^{-m}\#\left\{a\in\{0,1\}^m:\sum_{i=0}^{m-1}a_i3^i\equiv x\pmod{2^r}\right\},
\]

define

\[
p_r(m)=\sum_{x\bmod2^r}\mu_{m,r}(x)^2
\]

and

\[
\boxed{e_r(m):=2p_{r+1}(m)-p_r(m).}
\]

By the dyadic refinement identity,

\[
e_r(m)=\sum_{x\bmod2^r}
\bigl(\mu_{m,r+1}(x)-\mu_{m,r+1}(x+2^r)\bigr)^2.
\]

Thus `e_r(m)` is exactly the normalized selector sibling-imbalance energy that enters the Stage-4 boundary Cauchy bound.

## 2. Odd-frequency form

Let the Fourier transform on `Z/2^(r+1)Z` be normalized by

\[
\widehat\mu(t)=\sum_x\mu(x)e^{2\pi itx/2^{r+1}}.
\]

The sibling difference kills even frequencies and doubles odd frequencies, hence Parseval gives

\[
\boxed{
e_r(m)=\frac{2}{2^{r+1}}
\sum_{t\ {\rm odd}}|\widehat\mu_{m,r+1}(t)|^2.
}
\]

For the selector measure,

\[
|\widehat\mu_{m,r+1}(t)|^2
=
\prod_{i=0}^{m-1}
\cos^2\!\left(\frac{\pi t3^i}{2^{r+1}}\right).
\]

## 3. Exact complete-orbit multiplier

Assume `r>=2` and put

\[
\boxed{M_r:=2^{r-1}=\operatorname{ord}_{2^{r+1}}(3).}
\]

Every odd `t` has exact additive order `2^(r+1)`. The existing selector Fourier full-orbit theorem gives, for every odd starting frequency and every starting selector index `m`,

\[
\prod_{j=0}^{M_r-1}
\left|\cos\frac{\pi t3^{m+j}}{2^{r+1}}\right|
=2^{-M_r+1/2}.
\]

Squaring,

\[
\prod_{j=0}^{M_r-1}
\cos^2\!\left(\frac{\pi t3^{m+j}}{2^{r+1}}\right)
=2^{-2M_r+1}.
\]

The multiplier is the same for **every odd frequency**. Therefore it factors out of the complete odd-frequency energy sum:

\[
\boxed{
e_r(m+M_r)=2^{-2M_r+1}e_r(m),
\qquad r\ge2.
}
\]

This is an exact renormalization identity, not an inequality or asymptotic statement.

## 4. Iteration

Write

\[
m=aM_r+b,
\qquad0\le b<M_r.
\]

Then

\[
\boxed{
e_r(m)=2^{-a(2M_r-1)}e_r(b).
}
\]

Since `0<=e_r(b)<=1`, the immediate coarse-scale bound is

\[
\boxed{
e_r(m)\le2^{-\lfloor m/M_r\rfloor(2M_r-1)}.
}
\]

Hence every dyadic sibling scale satisfying `M_r << m` is deterministically suppressed at an essentially `2^{-2m}` rate, up to the incomplete final orbit.

## 5. Exact m=44 examples

For `m=44` the exact energies include

\[
\begin{array}{c|c|c|c}
r&M_r&\lfloor44/M_r\rfloor&e_r(44)\\\hline
2&2&22&2^{-66}\\
3&4&11&2^{-77}\\
4&8&5&2^{-79}\\
5&16&2&121/38685626227668133590597632\\
6&32&1&1495/77371252455336267181195264
\end{array}
\]

These values are exact. The theorem becomes nontrivial whenever at least one complete `3`-orbit fits inside the active selector digits.

## 6. Scope

The theorem closes the **coarse dyadic selector-collision regime** exactly. It does not solve the middle/high dyadic scales for which

\[
2^{r-1}>m.
\]

At those scales no complete multiplicative orbit is available inside the selector prefix. The remaining Stage-4 problem is therefore narrowed further to:

\[
\boxed{
\text{incomplete-orbit / sparse dyadic collision regime}.
}
\]

This is where the balanced-ternary representation

\[
j2^r=\sum_i\varepsilon_i3^i
\]

and sparse-address / carry methods should be applied.
