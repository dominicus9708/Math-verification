# Hensel relative discrete-log branches are ternary-tree isometries

Date: 2026-08-26

Status: **exact structural theorem** for the repaired binary/Hensel proof line.  It is a coordinate theorem, not a proof of the Collatz conjecture.  The companion executable is a finite regression check; the proof below is all-depth.

## 1. Relative discrete-log branch

Let `r>=2`.  For an odd integer `t` with `3` not dividing `t`, define

\[
\Phi_r(t)
:=
\operatorname{ind}_2\!\left(\frac{1+2^t}{3}\pmod{3^{r-1}}\right)
\in \mathbb Z/(2\cdot3^{r-2})\mathbb Z.
\]

This is well-defined because `2` generates the unit group modulo every power of three.

The live Hensel classes are

\[
t\equiv1,5\pmod6.
\]

For

\[
t=1+6k
\]
put

\[
\Psi_{1,r}(k):=\frac{\Phi_r(t)}2
\pmod{3^{r-2}},
\]

and for

\[
t=5+6k
\]
put

\[
\Psi_{5,r}(k):=\frac{\Phi_r(t)-1}{2}
\pmod{3^{r-2}}.
\]

The parity divisions are legitimate by the next lemma.

## 2. Output parity

Modulo nine,

\[
2^1\equiv2,
\qquad
2^5\equiv5.
\]

Hence

\[
\frac{1+2^t}{3}
\equiv
\begin{cases}
1\pmod3,&t\equiv1\pmod6,\\
2\pmod3,&t\equiv5\pmod6.
\end{cases}
\]

Since powers of two are `1 mod 3` at even exponent and `2 mod 3` at odd exponent,

\[
\boxed{
\Phi_r(1+6k)\equiv0\pmod2,
\qquad
\Phi_r(5+6k)\equiv1\pmod2.
}
\]

## 3. Exact 3-adic distance preservation

Take two integers `t_1,t_2` in the same live class modulo six.  Then `t_1-t_2` is even.  Write

\[
F(t):=\frac{1+2^t}{3}.
\]

We have

\[
F(t_1)-F(t_2)
=
\frac{2^{t_2}(2^{t_1-t_2}-1)}3.
\]

By LTE for an even exponent difference,

\[
v_3(2^{t_1-t_2}-1)
=1+v_3(t_1-t_2).
\]

Therefore

\[
\boxed{
v_3(F(t_1)-F(t_2))=v_3(t_1-t_2).
}
\]

If

\[
F(t_i)=2^{\Phi_i},
\]

then the two `Phi_i` have the same parity.  A second LTE application gives

\[
v_3(F(t_1)-F(t_2))
=1+v_3(\Phi_1-\Phi_2).
\]

Now write

\[
t_i=a+6k_i,
\]
with `a=1` or `5`, and normalize `Phi` by the factor two as above.  Since

\[
v_3(t_1-t_2)=1+v_3(k_1-k_2),
\]
we obtain

\[
\boxed{
v_3\bigl(\Psi_{a,r}(k_1)-\Psi_{a,r}(k_2)\bigr)
=v_3(k_1-k_2)
}
\]
whenever the two residues are distinct at the retained depth.

Thus each `Psi` is injective modulo `3^(r-2)`.  Domain and codomain both contain `3^(r-2)` elements, so

\[
\boxed{
\Psi_{1,r},\Psi_{5,r}
\text{ are permutations of }
\mathbb Z/3^{r-2}\mathbb Z.
}
\]

They are in fact exact rooted-tree isometries.

## 4. Fixed first-differing-digit slope

The isometry has more structure.  Suppose

\[
k_1-k_2=3^s u,
\qquad3\nmid u.
\]

Then

\[
t_1-t_2=6\cdot3^s u.
\]

Using

\[
2^6=64=1+7\cdot3^2,
\]
we get, modulo the first nonzero ternary digit after level `s`,

\[
2^{t_1-t_2}-1
\equiv
7u\,3^{s+2}
\pmod{3^{s+3}}.
\]

Consequently

\[
\frac{F(t_1)}{F(t_2)}
\equiv
1+\eta_a u\,3^{s+1}
\pmod{3^{s+2}},
\]
where

\[
\eta_1=-1,
\qquad
\eta_5=+1.
\]

On the discrete-log side, if

\[
\Psi_{a,r}(k_1)-\Psi_{a,r}(k_2)=3^s v,
\]
then

\[
2^{\Phi_1-\Phi_2}
=4^{3^s v}
\equiv1+v3^{s+1}
\pmod{3^{s+2}}.
\]

Hence

\[
\boxed{
v\equiv\eta_a u\pmod3.}
\]

Equivalently, at every ternary node the child digit is an affine permutation with a **fixed slope**:

\[
\boxed{
\begin{aligned}
\Psi_{1}:&\quad x\mapsto c-x\pmod3,\\
\Psi_{5}:&\quad x\mapsto c+x\pmod3,
\end{aligned}}
\]
for a node-dependent offset digit `c`.

Thus the two live Hensel branches are not arbitrary permutations of a flat residue set.  They are triangular automorphisms of the rooted ternary tree: reflection type on `1 mod 6`, translation type on `5 mod 6`.

## 5. Relation to the relative Hensel state

Write a surviving carry as

\[
K\equiv2^h\pmod{3^r}
\]
and let `e` be the mechanical exponent at the current prepend.  Put

\[
z:=h-e.
\]

For displacement `d`, define

\[
t=z+d.
\]

The Hensel lift is live exactly when

\[
\boxed{t\equiv1,5\pmod6.}
\]

If

\[
\phi(t):=\operatorname{ind}_2\left(\frac{1+2^t}{3}\right),
\]
then, with next mechanical gap `g in {1,2}`,

\[
\boxed{
z'=g-d+\phi(t).}
\]

The theorem above says that after splitting `t` into the two live classes, the remaining ternary digits are passed through an exact 3-adic tree isometry.

## 6. Audit consequence: coordinate simplification, not entropy loss

This point is important.

The relative discrete-log coordinate does **not** shrink the number of carry states exponentially.  Each live branch is a bijection of the remaining ternary residues.  Therefore it would be incorrect to claim a mixing or contraction theorem merely from the change of variables.

What is gained is structural:

\[
\boxed{
\text{flat carry residues}
\longrightarrow
\text{two live branches}
\longrightarrow
\text{ternary tree automorphisms with slopes }\pm1.
}
\]

This is the appropriate interface representation for the two-boundary min-plus operator on the 138-node Christoffel DAG.

In DSD language, this is a successful state-coordinate reduction but **not** a reduction of technical possibility count.  That distinction prevents another false entropy shortcut.

## 7. Next target

The remaining state problem is now sharper:

1. represent each Christoffel block operator on the ternary carry tree rather than a flat `3^r` table;
2. propagate Pareto states `(previous displacement, accumulated cost)` through the two fixed-slope branch automorphisms;
3. use the exact two-boundary conditions to obtain a lower Bellman cost;
4. compare it with the first-resonance budget `4,314,000,000`.

A further useful direction is an amortized **mechanical-alignment credit**: zero-displacement runs consume one ternary digit of alignment per step, while a repair displacement changes the alignment state through the tree automorphism above.  Any such potential must retain both boundaries, because arbitrary finite zero-cost mechanical blocks exist for suitably chosen unconstrained boundary carry.

Companion regression certificate:

`collatz/src/hensel_relative_discrete_log_tree_isometry_certificate.py`.
