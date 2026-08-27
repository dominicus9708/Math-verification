# Finite-depth Hensel prefix relaxation hierarchy

Status: **SAFE as an abstract finite-horizon lower-bound theorem**.  
Operator-domain specialization to `u_i(d)=2^{e_i-d}` remains **OPEN** until the admissible domain of `d` is fixed from the original construction.

## 1. Purpose

The current hard sector is the low-surplus `s=1` branch.  The ordering-only Bellman cost is a valid lower bound but cannot close the branch by itself because `B_w(0)=0`.

The next admissible refinement is therefore:

1. keep exact Hensel/carry constraints for a **finite prefix** of depth `h`;
2. forget the carry after depth `h`;
3. relax the remaining suffix back to the ordering-only Bellman problem.

This produces a monotone lower-bound hierarchy without using the independent near-root budget in its construction.

## 2. Abstract exact transition

Fix a word

\[
w=(g_1,\dots,g_n),\qquad g_i\in\{1,2\}.
\]

At step `i`, let the current boundary state be

\[
S_i=(K_i,p_i).
\]

Define the exact admissible-control set abstractly by

\[
\mathcal A_i(K,p)
=
\left\{
 d\in\mathbb Z_{\ge0}:
 d\ge \max(0,p-g_i+1),\;
 u_i(d)\text{ is defined},\;
 K+u_i(d)\equiv0\pmod3
\right\}.
\]

For `d in A_i(K,p)`, the successor is

\[
K' = \Phi_i(K,d):=\frac{K+u_i(d)}3,
\qquad p'=d.
\]

Assumptions used in the theorem below:

- `u_i(d)` is integer-valued on its admissible domain;
- its value/domain depend on the local step and `d`, not on `K`;
- the local cost `kappa_i(d)` is independent of `K`;
- the ordering constraint is the one displayed above.

No assumption `d\le e_i` is introduced here.

## 3. Finite-depth feasible sets

Let `F_h(K,p;w)` be the set of full control strings

\[
\mathbf d=(d_1,\dots,d_n)
\]

such that:

- for steps `1,...,h`, the exact action condition `d_i in A_i(K_{i-1},p_{i-1})` and exact carry update are enforced;
- for steps `h+1,...,n`, only the ordering constraint is retained;
- after depth `h`, the carry `K_h` is forgotten and places no restriction on the relaxed suffix.

Define

\[
C_w(\mathbf d)=\sum_{i=1}^{n}\kappa_i(d_i)
\]

and

\[
\boxed{
B_w^{[h]}(K,p)
:=
\inf_{\mathbf d\in\mathcal F_h(K,p;w)} C_w(\mathbf d).
}
\]

Use `+infinity` when the feasible set is empty.

At depth zero there is no exact carry condition, so

\[
\boxed{B_w^{[0]}(K,p)=B_w(p).}
\]

Here `B_w` is the previously proved ordering-only Bellman relaxation.

## 4. Monotone hierarchy theorem

Adding one exact step can only remove relaxed control strings:

\[
\mathcal F_{h+1}(K,p;w)
\subseteq
\mathcal F_h(K,p;w).
\]

Taking the infimum of the same cost over nested feasible sets gives

\[
\boxed{
B_w^{[h+1]}(K,p)
\ge
B_w^{[h]}(K,p)
\ge
B_w(p).
}
\]

This proof uses feasible-set inclusion only.  It does **not** use the `A0/J0` gap budget, a local residue scan, or any assumed global predecessor theorem.

At full depth `h=n`, every step is exact but the terminal boundary is free. Therefore

\[
\boxed{
B_w^{[n]}(K,p)
=
\inf_{T}\mathcal T_w((K,p),T),
}
\]

where the infimum ranges over admissible terminal states `T`.

Consequently, for every prescribed admissible terminal state `T`,

\[
\boxed{
\mathcal T_w((K,p),T)
\ge
B_w^{[n]}(K,p)
\ge
\cdots
\ge
B_w^{[0]}(K,p)=B_w(p).
}
\]

## 5. Exact finite-horizon residue invariance

Suppose the first `h` exact controls are fixed and admissible from `K_0`.
The previously audited lift identity is

\[
\widetilde K_0=K_0+3^h t
\quad\Longrightarrow\quad
\widetilde K_i=K_i+3^{h-i}t,
\qquad 0\le i\le h.
\]

For every `i<h`, the difference `3^{h-i}t` is divisible by 3, so the same congruence test and the same control `d_i` remain admissible.  Costs are unchanged.  At step `h` the carry is forgotten by definition of the relaxation.

Hence, whenever both starts belong to the ambient state domain,

\[
\boxed{
B_w^{[h]}(K+3^h t,p)=B_w^{[h]}(K,p).
}
\]

Thus a depth-`h` prefix relaxation is exactly representable by

\[
(K\bmod 3^h,p)
\]

**for that finite horizon only**.

This does not repair the rejected unbounded residue quotient.  At depth `h+1`, two starts that agree mod `3^h` can split because their depth-`h` carries differ by `t`.

## 6. Why this is not circular

Allowed dependency direction:

\[
\boxed{
\text{gap word / ordering recurrence}
\to
B_w
\to
B_w^{[h]}
\to
B_w^{[n]}
\to
\text{compare with an independently derived near-root budget}.
}
\]

Forbidden reverse arrows remain forbidden:

- near-root budget -> local Bellman/Hensel lower cost;
- `A0/J0` macro contraction -> exact local Hensel admissibility;
- finite residue enumeration -> global predecessor theorem;
- finite `h` residue state -> infinite-horizon state quotient.

The construction of `B_w^{[h]}` is therefore independent of the target upper budget.

## 7. Operator-domain audit: parity gate not yet SAFE

The stored boundary transition is written as

\[
u_i(d)=2^{e_i-d},
\qquad
K+u_i(d)\equiv0\pmod3,
\qquad
K'=\frac{K+u_i(d)}3.
\]

However, the currently audited notes/code do **not** explicitly impose

\[
d\le e_i.
\]

Modulo 3, powers of 2 have parity two, so a formal parity selector can be written if integer exponents are interpreted in the modular group.  But the ordinary integer successor `K'` still requires the exact arithmetic/domain convention for `u_i(d)`.

Therefore:

- **SAFE:** abstract finite-depth hierarchy above;
- **CONDITIONAL:** parity selector after a domain convention making `u_i(d)` an admissible integer transition is confirmed;
- **OPEN:** specialize the hierarchy to the original Hensel operator without adding an unstated `d<=e_i` assumption.

## 8. Regression role

`collatz/src/hensel_prefix_relaxation_hierarchy_regression.py` checks the abstract logic on finite toy operators using exact rational arithmetic.

It checks:

1. `B^[h+1] >= B^[h]`;
2. full-depth prefix relaxation equals exhaustive exact/free-terminal minimization;
3. prescribed-terminal exact cost is at least the free-terminal minimum;
4. depth-`h` residue invariance under `K -> K+3^h t`;
5. a concrete depth-`h+1` split showing why the finite residue quotient cannot be promoted to an infinite one.

The finite scan is a regression test only; the theorem is the symbolic feasible-set/lift argument above.

## 9. Current proof gate

The independent reset-sector upper budget remains

\[
D<0.981G.
\]

The valid next target is to obtain, without using that budget in the construction,

\[
B_w^{[h]}(K,p)>0.981G
\]

for all Hensel-compatible states relevant to the `s=1` reset sector, or else to identify the surviving finite-depth residue classes and refine them further.

Status of that inequality: **OPEN**.
