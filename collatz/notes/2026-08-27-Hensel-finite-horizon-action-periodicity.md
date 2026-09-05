# Exact finite-horizon Hensel action periodicity

Date: 2026-08-27

Status: **SAFE finite-horizon compression theorem.**

This note turns the exact-prefix Hensel Bellman hierarchy into a genuinely finite dynamic program. It does **not** identify a fixed residue quotient for the infinite problem.

## 1. Setting

At an exact step with `r>=1` exact Hensel steps still to be enforced, use the 3-adic transition

\[
d\ge L:=\max(0,p-g+1),
\]

\[
u(d)=2^{e-d}\in\mathbb Z_3^\times,
\qquad
K+u(d)\equiv0\pmod3,
\]

\[
K'=\frac{K+u(d)}3,
\qquad p'=d.
\]

The remaining exact horizon is `r-1` after this step.

## 2. Exact order of 2 modulo powers of 3

Define

\[
\boxed{M_r:=2\cdot3^{r-1}.}
\]

By LTE,

\[
\begin{aligned}
v_3\!\left(2^{2\cdot3^k}-1\right)
&=v_3\!\left(4^{3^k}-1\right)\\
&=v_3(4-1)+v_3(3^k)\\
&=k+1.
\end{aligned}
\]

Therefore

\[
2^{M_r}\equiv1\pmod{3^r},
\]

while no proper divisor of the form `2*3^k`, `k<r-1`, is an order modulo `3^r`. Since the group order is

\[
\varphi(3^r)=2\cdot3^{r-1},
\]

we obtain

\[
\boxed{\operatorname{ord}_{3^r}(2)=2\cdot3^{r-1}=M_r.}
\]

The statement applies equally to negative exponents because `2` is a unit modulo `3^r`.

## 3. Action periodicity

For every integer displacement `d`,

\[
\boxed{
2^{e-(d+M_r)}\equiv2^{e-d}\pmod{3^r}.
}
\]

Hence `d` and `d+M_r` have the same first-step congruence status.

If both are admissible, write their successors as `K'_d` and `K'_{d+M_r}`. Their numerators differ by a multiple of `3^r`; after division by 3,

\[
\boxed{
K'_{d+M_r}\equiv K'_d\pmod{3^{r-1}}.
}
\]

Thus the remaining `r-1` exact Hensel steps cannot distinguish the two successor carries at their required finite resolution.

## 4. Dominance of later representatives

The local defect cost

\[
\kappa(d)=2w(1-2^{-d}),\qquad w>0,
\]

is strictly increasing in `d`.

Also the successor ordering state is `p'=d`. Replacing `d` by `d+M_r` only raises the lower bound on every later ordering displacement. By the previously proved same-residue finite-horizon invariance and monotonicity in `p`,

\[
B^{[r-1]}(K'_{d+M_r},d+M_r)
\ge
B^{[r-1]}(K'_d,d).
\]

Together with

\[
\kappa(d+M_r)>\kappa(d),
\]

this gives strict domination:

\[
\boxed{
d+M_r\text{ is dominated by }d}
\]

whenever both lie above the ordering lower bound.

More generally, in each residue class modulo `M_r`, only the smallest representative satisfying `d>=L` can be optimal.

## 5. Exact finite candidate set

For every residue class `a mod M_r`, define

\[
\rho_L(a):=\min\{d\ge L:d\equiv a\pmod{M_r}\}.
\]

Before the mod-3 Hensel gate there are exactly `M_r` canonical representatives.

The first congruence

\[
K+2^{e-d}\equiv0\pmod3
\]

fixes the parity of `d`. Since `M_r` is even, exactly half of the residue classes have that parity.

Therefore the exact first action with `r` exact steps remaining has at most

\[
\boxed{\frac{M_r}{2}=3^{r-1}}
\]

undominated candidates.

For a unit carry there are exactly `3^{r-1}` parity-compatible canonical classes; later exact feasibility may remove more of them.

Special cases:

\[
\begin{array}{c|c|c}
r&M_r&\text{max undominated first actions}\\
\hline
1&2&1\\
2&6&3\\
3&18&9\\
4&54&27\\
5&162&81
\end{array}
\]

Thus the one-step parity theorem is precisely the `r=1` member of this finite-horizon periodicity hierarchy.

## 6. Exact Bellman recursion

Let `H_i^{[r]}(K,p)` denote the minimum cost from position `i` when the next `r` steps are exact and the suffix thereafter is ordering-only.

Base case:

\[
\boxed{H_i^{[0]}(K,p)=B_{i:n}^{\rm ord}(p).}
\]

For `r>=1`, set

\[
L=\max(0,p-g_i+1),
\qquad
M_r=2\cdot3^{r-1}.
\]

Let `R_r(K,e_i,L)` be the parity-compatible canonical representatives

\[
\rho_L(a),\qquad a\in\mathbb Z/M_r\mathbb Z,
\]

that satisfy the first Hensel congruence.

Then

\[
\boxed{
H_i^{[r]}(K,p)
=
\min_{d\in R_r(K,e_i,L)}
\left[
\kappa_i(d)
+H_{i+1}^{[r-1]}\!\left(
\frac{K+2^{e_i-d}}3,d
\right)
\right].
}
\]

Only the carry residue modulo `3^r` is required at the entry to this depth-`r` recursion, and only modulo `3^{r-1}` after the first division.

This is an **exact finite-horizon DP**, not a relaxation inside the exact prefix.

## 7. Why this does not revive the rejected global quotient

At horizon `r`, the action period is

\[
M_r=2\cdot3^{r-1}.
\]

At horizon `r+1`, it becomes

\[
M_{r+1}=3M_r.
\]

Likewise the required carry resolution grows from `K mod 3^r` to `K mod 3^{r+1}`.

Therefore no fixed finite quotient is claimed to describe arbitrary continuation.

The valid statement is horizon-indexed:

\[
\boxed{
\text{resolution depth grows with exact horizon.}
}
\]

This is consistent with the earlier counterexample showing that starts equal modulo `3^r` may split after one additional exact step.

## 8. Two-step form

At depth two,

\[
M_2=6.
\]

The mod-3 parity gate leaves exactly three canonical first-action classes. The zero-penalty greedy address is

\[
\boxed{
\Theta_2
\equiv
-2^{e_1-L_1}-3\,2^{e_2-L_2}
\pmod9.
}
\]

For an off-address state, the exact `B^[2]` repair is obtained by comparing at most those three canonical first actions; for each successor the remaining depth-one action is fixed by its parity gate.

Hence depth two is already a finite exact min-plus problem with no arbitrary displacement cutoff.

## 9. DSD structural interpretation

The state-resolution schedule is

\[
\boxed{
(r,K\bmod3^r,p)
\to
\le3^{r-1}\text{ canonical actions}
\to
(r-1,K'\bmod3^{r-1},d).
}
\]

The resolution decreases exactly as the remaining horizon decreases.

This is a finite-resolution sufficient descriptor. It is deliberately not promoted to an infinite sufficient descriptor.

## 10. Circularity audit

SAFE dependency direction:

\[
\boxed{
\mathbb Z_3\text{ operator}
\to
\operatorname{ord}_{3^r}(2)
\to
\text{finite action periodicity}
\to
\text{exact finite-horizon DP}
\to
\text{boundary-state intersection}
\to
\text{only then near-root budget comparison}.
}
\]

Forbidden reverse directions remain:

- near-root budget -> finite action pruning;
- a convenient finite cutoff -> proof of action completeness;
- fixed residue depth -> infinite Hensel state;
- finite exact DP -> global predecessor existence;
- this theorem -> repair of the separate ternary-selector entry theorem.

## 11. Current consequence

The previous OPEN issue “the exact Hensel action space is unbounded in `d`” is now removed at every fixed horizon.

For any chosen finite depth `h`, `B^[h]` is exactly computable from finitely many canonical action residues with **no heuristic displacement truncation**.

The remaining proof-level input is the independently derived admissible low-surplus boundary carry set

\[
\mathcal K_{s=1,h}.
\]

The central intersection remains

\[
\boxed{
\mathcal K_{s=1,h}\cap[\Theta_h]_{3^h}.
}
\]

and the quantitative closure against the independent reset budget `D<0.981G` remains **OPEN**.
