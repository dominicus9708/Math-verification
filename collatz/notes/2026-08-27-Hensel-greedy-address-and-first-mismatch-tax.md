# Greedy Hensel address and first-mismatch tax

Status: **SAFE as an abstract finite-horizon theorem**.  
Specialization to the stored `u_i(d)=2^{e_i-d}` operator remains **OPEN** until the admissible domain of `d` is fixed.

This note continues the acyclic chain

\[
\text{ordering recurrence}
\to
B_w
\to
B_w^{[h]}
\to
\text{finite-depth Hensel address / mismatch tax}
\to
\text{independent boundary intersection}
\to
\text{only then compare with the near-root defect budget}.
\]

No near-root budget is used below.

## 1. Ordering-only greedy controls

Fix

\[
w=(g_1,\ldots,g_n),\qquad g_i\in\{1,2\},
\]

with initial ordering state `p`.

Set

\[
L_0=p,
\qquad
\boxed{L_i=\max(0,L_{i-1}-g_i+1)}
\quad(1\le i\le n).
\]

Equivalently,

\[
L_i=\max(0,p-N_2(i)),
\]

where `N_2(i)` counts the gap-2 symbols among the first `i` gaps.

The ordering-only Bellman minimizer is exactly

\[
(d_1,\ldots,d_n)=(L_1,\ldots,L_n).
\]

For positive weights and

\[
\kappa_i(d)=2w_i(1-2^{-d}),\qquad w_i>0,
\]

this minimizer is unique because each `kappa_i` is strictly increasing and a larger control can only weakly increase later ordering lower bounds.

## 2. Exact finite-depth Hensel condition

For an exact action use only the already audited abstract conditions

\[
d_i\ge \max(0,p_{i-1}-g_i+1),
\]

\[
u_i(d_i)\text{ is defined and integer-valued},
\]

\[
K_{i-1}+u_i(d_i)\equiv0\pmod3,
\qquad
K_i=\frac{K_{i-1}+u_i(d_i)}3,
\qquad p_i=d_i.
\]

No assumption `d_i<=e_i` is inserted.

Assume for the moment that the greedy values

\[
u_i(L_i)
\]

are defined integers through depth `h`.

Unrolling the carry gives

\[
\boxed{
3^rK_r
=K_0+\sum_{i=1}^{r}3^{i-1}u_i(L_i)
}
\quad(1\le r\le h).
\]

Define

\[
S_r(K_0)
:=K_0+\sum_{i=1}^{r}3^{i-1}u_i(L_i).
\]

Because

\[
S_h-S_r
=\sum_{i=r+1}^{h}3^{i-1}u_i(L_i)
\equiv0\pmod{3^r},
\]

one terminal divisibility condition implies all earlier ones:

\[
3^h\mid S_h
\quad\Longrightarrow\quad
3^r\mid S_r\quad(1\le r\le h).
\]

The converse is immediate by taking `r=h`.

Therefore the complete greedy prefix is exact through depth `h` iff

\[
K_0+\sum_{i=1}^{h}3^{i-1}u_i(L_i)
\equiv0\pmod{3^h}.
\]

## 3. Unique zero-penalty Hensel address

Define

\[
\boxed{
\Theta_h(p;w)
:=-\sum_{i=1}^{h}3^{i-1}u_i(L_i)
\pmod{3^h}.
}
\]

Then

\[
\boxed{
(L_1,\ldots,L_h)\text{ is an exact Hensel prefix}
\iff
K_0\equiv\Theta_h(p;w)\pmod{3^h}.
}
\]

Thus, provided all greedy local actions are defined, the exact Hensel states that preserve the ordering Bellman optimum through depth `h` occupy **one and only one residue cylinder modulo `3^h`**.

If some greedy `u_r(L_r)` is undefined or nonintegral at the first such depth `r<=h`, the zero-penalty cylinder is empty from that depth onward.

## 4. Equality theorem for the finite-depth Bellman hierarchy

Recall the finite-depth prefix relaxation

\[
B_w^{[h]}(K,p),
\]

which enforces exact Hensel/carry constraints for the first `h` steps and relaxes the suffix to ordering only.

The ordering-only feasible set contains the exact-prefix feasible set, so

\[
B_w^{[h]}(K,p)\ge B_w(p).
\]

If

\[
K\equiv\Theta_h(p;w)\pmod{3^h},
\]

the full ordering-greedy control string is still feasible for the prefix-exact problem and attains `B_w(p)`. Hence equality holds.

Conversely, suppose the greedy exact prefix is not feasible. Every prefix-exact control string must differ from the greedy string at some index `k<=h`. At its first differing index,

\[
d_k\ge L_k+1.
\]

Monotonicity of the ordering update then gives

\[
d_i\ge L_i\qquad(i>k),
\]

and the positive, strictly increasing local costs prevent any later compensation. Therefore every feasible exact-prefix string has strictly larger total cost.

Consequently,

\[
\boxed{
B_w^{[h]}(K,p)=B_w(p)
\iff
K\equiv\Theta_h(p;w)\pmod{3^h},
}
\]

when all greedy actions through `h` are defined integers.

If a greedy action is undefined before or at depth `h`, equality is impossible.

This converts zero Hensel penalty from a state-search problem into a **single-address intersection problem**.

## 5. First-mismatch tax

For the greedy control at step `k`, the least possible one-unit displacement tax is

\[
\delta_k
:=\kappa_k(L_k+1)-\kappa_k(L_k).
\]

Using

\[
\kappa_k(d)=2w_k(1-2^{-d}),
\]

we get exactly

\[
\boxed{
\delta_k=w_k2^{-L_k}>0.
}
\]

Suppose the greedy carry/address conditions first fail at level `r`:

- either the greedy local action is undefined/nonintegral at `r`, or
- the greedy prefix divisibility fails at `r` while it held through `r-1`.

Any exact-prefix control path through depth `r` must deviate from the greedy controls at some index `k<=r`.

A deviation at its first index `k` costs at least `delta_k`, and all later costs are at least their greedy counterparts. Therefore the universally safe mismatch bound is

\[
\boxed{
B_w^{[h]}(K,p)-B_w(p)
\ge
\underline\delta_r
:=\min_{1\le k\le r} w_k2^{-L_k}
}
\qquad(h\ge r),
\]

unless the exact-prefix feasible set is empty, in which case the left-hand side is `+infinity`.

### Important audit correction

It is **not** safe in general to replace the minimum above by only

\[
w_r2^{-L_r}.
\]

An exact path may choose to deviate earlier than the first failure of the greedy path if doing so satisfies later carry conditions at lower cost. The sharper step-`r` tax is valid only when an independent argument forces the exact path to match the greedy controls through `r-1`.

This weaker minimum-over-earlier-deviations bound is the unconditional finite-horizon statement.

## 6. Nested 3-adic zero-penalty cylinders

Whenever greedy actions remain defined,

\[
\Theta_{h+1}
=-\sum_{i=1}^{h+1}3^{i-1}u_i(L_i)
\pmod{3^{h+1}}.
\]

Reducing modulo `3^h` removes the last term, so

\[
\boxed{
\Theta_{h+1}\equiv\Theta_h\pmod{3^h}.
}
\]

Hence the zero-penalty residue cylinders are nested:

\[
[\Theta_{h+1}]_{3^{h+1}}
\subset
[\Theta_h]_{3^h}.
\]

For an infinite sequence of defined greedy actions this determines a unique inverse-limit address

\[
\boxed{\Theta_\infty\in\mathbb Z_3.}
\]

This is a statement in the 3-adic completion only.

It does **not** imply that:

- `Theta_infinity` is a positive ordinary integer;
- an actual minimal-counterexample boundary carry lies on it;
- a compatible positive Collatz predecessor exists;
- finite-depth residue compatibility closes an infinite pullback.

Those reverse implications remain forbidden.

## 7. DSD structural reading

The finite-depth information flow is

\[
(K,p)
\to
(L_1,\ldots,L_h)
\to
\Theta_h
\to
\begin{cases}
\text{unique zero-penalty address},\\
\text{off-address mismatch tax}.
\end{cases}
\]

`Theta_h` is therefore a sufficient descriptor only for the question

> does this boundary state preserve the unique ordering-optimal prefix through depth `h`?

It is **not** a sufficient descriptor for the full Hensel dynamics.

## 8. Acyclicity audit

SAFE direction:

\[
\boxed{
\text{ordering greedy path}
\to
\Theta_h
\to
B_w^{[h]}\text{ penalty}
\to
\text{independently derived admissible boundary }K\text{ set}
\to
\text{intersection}
\to
\text{only then compare with }D<0.981G.
}
\]

Forbidden reverse edges:

- reset/near-root budget -> construction of `Theta_h`;
- A0/J0 macro contraction -> local Hensel admissibility;
- finite residue scan -> global predecessor theorem;
- compatible `Theta_h` cylinders -> existence of an ordinary integer global trajectory;
- this address theorem -> repair of the separate ternary-selector entry theorem.

## 9. Regression role

`collatz/src/hensel_greedy_address_regression.py` attacks the theorem on finite abstract integer-valued toy operators.

It checks:

1. zero penalty iff the start carry lies in the unique `Theta_h mod 3^h` class;
2. the first-mismatch lower bound `min_{k<=r} delta_k`;
3. nested residue compatibility;
4. many gap words and local integer transition functions.

The regression is not the proof. The proof is the divisibility identity plus uniqueness/monotonicity of the ordering Bellman minimizer.

## 10. Current proof gate

The hard `s=1` reset sector has the independently derived upper defect budget

\[
D<0.981G.
\]

The next noncircular problem is now sharper:

\[
\boxed{
\text{admissible }s=1\text{ boundary carries}
\cap
[\Theta_h]_{3^h}.
}
\]

At each finite depth one of two things happens:

1. the admissible boundary set misses the unique zero-penalty cylinder, forcing a positive Hensel mismatch tax; or
2. it intersects that cylinder, leaving a uniquely nested low-cost address that must be followed to greater depth.

A finite-depth miss does not by itself beat `0.981G`; the quantitative mismatch taxes still have to be accumulated independently.  
Status of that quantitative closure: **OPEN**.
