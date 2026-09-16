# Monotone prefix first-hit dominance certificates

Date: 2026-08-09

Status: **DERIVED LEMMA + EXACT SMALL CROSS-CHECK**

This note turns the universal weak-kernel lower bound into a progressive certified pruning rule.

## 1. Universal weak prefix kernel

Let

\[
\alpha=\log_3 2,
\qquad
B^-_{s,\ell}
=
\left\{
x\bmod2^\ell:
s+Q_j(x)\ge\lfloor\alpha j\rfloor
\text{ for all }1\le j\le\ell
\right\}.
\]

For a state `(k,q;r,y)` with target `K=k+m`, put

\[
\eta=y\bmod2^m.
\]

For each prefix depth `1<=ell<=m`, define

\[
\boxed{
L_\ell(q,\eta,s)
=
\min\left\{
u\in[0,2^\ell):
\eta+3^q\nu\pmod{2^\ell}\in B^-_{s,\ell}
\right\}.
}
\]

Only `eta mod 2^ell` and `3^q mod 2^ell` are needed to compute `L_ell`.

## 2. Certified lower bound for the full future value

If a full length-`m` weak-kernel hit occurs at some

\[
u\in[0,2^m),
\]

then its reduction

\[
\bar u=u\bmod2^\ell
\]

hits the weak prefix kernel `B^-_{s,ell}`. Since `u>=bar u`,

\[
u\ge L_\ell.
\]

The actual kernel is contained in the weak kernel, so its exact first-hit value satisfies

\[
\boxed{
J_{k,K}(q,\eta)\ge L_\ell(q,\eta,s)
\quad\text{for every }1\le\ell\le m.
}
\]

Hence the least possible depth-`K` descendant obeys

\[
\boxed{
r_{\min,K}\ge r+2^kL_\ell.}
\]

## 3. Monotonicity in prefix depth

A hit modulo `2^(ell+1)` reduces to a hit modulo `2^ell`. If `u_{ell+1}` is the least `(ell+1)`-bit hit and

\[
\bar u=u_{\ell+1}\bmod2^\ell,
\]

then

\[
\bar u\ge L_\ell,
\qquad
u_{\ell+1}\ge\bar u.
\]

Therefore

\[
\boxed{
L_1\le L_2\le\cdots\le L_m=J^-_{s,m}(q,\eta).
}
\]

This makes the certificate naturally progressive: increase `ell` only while the current state has not yet been pruned.

## 4. Dominance rule against an incumbent

Suppose a complete depth-`K` survivor with start `R_best` is known. At any current state, if for some prefix depth `ell`

\[
\boxed{
r+2^kL_\ell\ge R_{\rm best},}
\]

then no completion of that state can improve the incumbent and the entire state can be removed.

This rule is exact and does not require equality of endpoint, slack, or carry state with another branch.

## 5. Reusable low-bit signatures

For `ell>=3`,

\[
\operatorname{ord}_{2^\ell}(3)=2^{\ell-2}.
\]

Therefore `L_ell` depends on the arithmetic multiplier only through

\[
q\bmod2^{\ell-2}.
\]

A reusable certificate key is thus

\[
\boxed{
(s,\ q\bmod2^{\ell-2},\ \eta\bmod2^\ell,\ \ell).
}
\]

This key is independent of the large absolute depth except through the slack already carried by the state. The universal weak kernel has removed the Sturmian phase dependence.

## 6. Small exact example

At depth `k=5`, the coefficient-surviving canonical states include

\[
(r,q,y)=(7,4,20),
\qquad
(15,4,40),
\qquad
(27,4,71).
\]

Here

\[
a_5=4,
\qquad s=0
\]

for all three.

Independent Wolfram evaluation of the universal weak-prefix first-hit gives:

For `(7,4,20)`,

\[
L_1=0,
\qquad
L_2=1,
\qquad
L_3=1,
\qquad
L_4=2.
\]

Thus already at `ell=2`,

\[
r_{\min,K}\ge7+2^5=39.
\]

For `(15,4,40)`,

\[
L_1=0,
\qquad
L_2=1,
\]

so

\[
r_{\min,K}\ge15+32=47.
\]

For `(27,4,71)`, the same computation gives

\[
L_\ell=0
\]

for every tested `1<=ell<=10`, consistent with the known fact that `27` itself remains the minimal coefficient survivor through the small-depth plateau `7<=K<=58` recorded elsewhere in the repository.

Therefore once the incumbent `R_best=27` is known, the `7` and `15` depth-five states can be discarded using only two future weak-prefix bits, while the actual winning `27` state is retained.

The example is diagnostic; the pruning theorem itself is algebraic and does not depend on this finite test.

## 7. Interpretation

The earlier exact quotient asks for the full future carry signature. The present rule instead computes an optimistic lower bound from only a few low bits:

\[
\boxed{
\text{small }\ell
\to
\text{weak kernel first hit }L_\ell
\to
\text{min-plus lower bound}
\to
\text{certified branch removal}.
}
\]

This is the intended use of the formation-style complement pruning: a state is deleted only after a lower bound proves that it cannot contain the target minimal counterexample/survivor.

## 8. Remaining issue

The usefulness of the rule at large `K` depends on how quickly `L_ell` grows for the low-slack signatures that remain competitive. Establishing a uniform growth theorem for these prefix first-hit values is now a concrete structural target.