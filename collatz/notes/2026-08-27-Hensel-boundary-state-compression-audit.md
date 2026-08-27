# Hensel boundary-state compression audit

Date: 2026-08-27

Status: **SAFE structural lemmas + one REJECTED exact quotient.** This note continues the DSD / proof-chain / structural-audit triad and does not prove the Collatz conjecture.

## 1. Starting operator

For a right-to-left mechanical gap block

\[
w=(g_1,\ldots,g_h),\qquad g_i\in\{1,2\},
\]

the boundary state is

\[
S=(K,p).
\]

At one prepend step a displacement `d` must satisfy

\[
d\ge\max\{0,p-g_i+1\}
\]

and the Hensel congruence

\[
K+u_i(d)\equiv0\pmod3,
\qquad
u_i(d)=2^{e_i-d}.
\]

The successor is

\[
\boxed{
K'={K+u_i(d)\over3},\qquad p'=d.
}
\]

The local min-plus cost depends on the displacement and block weight, not directly on the numerical size of `K`.

The audit question is which information in `(K,p)` may be discarded without changing or invalidly lowering the global operator.

## 2. SAFE: exact same-K p dominance

Fix the same exact Hensel carry `K` and two ordering coordinates

\[
p_1\le p_2.
\]

Every first action `d` admissible from `(K,p2)` obeys

\[
d\ge\max\{0,p_2-g_i+1\}
\ge
\max\{0,p_1-g_i+1\}.
\]

The Hensel congruence is identical because `K` and `d` are identical.  The two paths therefore enter the exact same successor state

\[
(K',d).
\]

After that first step their continuation languages are identical.

Hence for every block and fixed terminal state `T`,

\[
\boxed{
\mathcal T_w((K,p_1),T)
\le
\mathcal T_w((K,p_2),T).
}
\]

Consequently, in an exact min-plus dynamic program, if two accumulated states have the same exact `K` and

\[
p_1\le p_2,
\qquad
c_1\le c_2,
\]

then `(K,p2,c2)` is dominated and can be deleted without changing the optimum.

This is the first fully safe state-pruning rule.

It does **not** compare states with different `K`.

## 3. SAFE: h-step lift / horizon-leakage identity

Take any admissible prescribed control sequence through `h` prepend steps and let its carries be

\[
K_0,K_1,\ldots,K_h.
\]

For any integer `t`, replace the initial carry by

\[
\widetilde K_0=K_0+3^h t
\]

and use the exact same displacement controls.

Inductively,

\[
\boxed{
\widetilde K_i
=K_i+3^{h-i}t
\qquad(0\le i\le h).
}
\]

Indeed, if this holds at step `i`, then for `i<h`

\[
\widetilde K_i\equiv K_i\pmod3,
\]

so the same Hensel divisibility condition holds, and

\[
\widetilde K_{i+1}
={\widetilde K_i+u_i\over3}
=K_{i+1}+3^{h-i-1}t.
\]

All ordering constraints and local costs are unchanged because the displacement controls are unchanged.

At the left boundary,

\[
\boxed{
\widetilde K_h=K_h+t.
}
\]

Thus `3^h` of unresolved initial carry is converted into one unit of terminal carry after exactly `h` divisions.

## 4. REJECTED: fixed K mod 3^m as an exact unbounded quotient

The preceding identity immediately audits a tempting compression.

Two starting carries that agree modulo

\[
3^m
\]

can share the same first `m` admissible controls and incur exactly the same costs, yet after `m` steps their terminal carries can differ by one.

For `t=1`,

\[
\widetilde K_0=K_0+3^m,
\qquad
\widetilde K_m=K_m+1.
\]

The next Hensel residue class may therefore differ.

A universal explicit regression family is

\[
K_i=1,
\qquad u_i=2,
\]

for which the lifted path begins at

\[
1+3^m
\]

and follows the same `m` divisions, ending at `2` rather than `1`.

Therefore

\[
\boxed{
K\bmod3^m
\text{ is insufficient as a fixed exact state quotient for horizons beyond }m.
}
\]

This proposed global compression is marked **REJECTED** unless it is used only as an explicitly relaxed lower-bound state with a separate soundness proof.

## 5. SAFE: horizon-dependent residue depth

The recurrence can be unrolled as

\[
\boxed{
3^hK_h
=K_0+
\sum_{i=0}^{h-1}3^i u_i.
}
\]

For a prescribed length-`h` control sequence:

- exact divisibility through the first `h` steps depends on successively deeper ternary digits of `K_0`;
- the terminal residue `K_h mod 3` depends on `K_0 mod 3^{h+1}`.

So residue depth must grow with the horizon if the quotient is required to remain exact.

This explains structurally why a fixed finite `3`-adic truncation cannot by itself solve the `10^11`-scale block.

## 6. SAFE: two-boundary affine covariance

The same lift identity gives a useful exact symmetry rather than only a negative result.

Whenever the lifted endpoints remain in the admissible boundary domain,

\[
\boxed{
\mathcal T_w(
(K+3^h t,p),
(L+t,q))
=
\mathcal T_w((K,p),(L,q)).
}
\]

The correspondence is path-by-path and cost-preserving.

Equivalently, the two-boundary combination

\[
\boxed{
\Xi_h:=K-3^hL
}
\]

is invariant under this diagonal lift.

Thus absolute carry size is not the correct two-boundary coordinate.  The operator possesses an exact affine covariance that any future state compression should preserve.

This does not yet make `Xi_h` a complete finite state: admissibility/unit constraints and the set of realizable controls still matter.

## 7. SAFE: ordering-only persistence potential for p

The ordering coordinate also has a deterministic persistence law independent of Hensel residues.

Moving one odd ordinal left across a mechanical gap `g in {1,2}` gives

\[
d_{j-1}\ge d_j-g+1.
\]

Since `g<=2`, displacement can fall by at most one per odd ordinal:

\[
\boxed{
d_{j-r}\ge\max\{0,p-r\}}
\]

if the right boundary begins with displacement `p`.

Every mechanical correction weight satisfies

\[
a_j=\frac{2^{n_j-1}}{3^j}>\frac16.
\]

Therefore, if at least `p-1` odd ordinals remain to the left, the ordered-position defect cost obeys

\[
\begin{aligned}
D
&>\frac16
\sum_{q=1}^{p}(1-2^{-q})\\
&=\boxed{
\frac{p-1+2^{-p}}6
}.
\end{aligned}
\]

This is a residue-free Bellman-type lower potential generated only by ordering.

## 8. Reset-strip consequence for p

After a certified `A0,A0,J0` reset, the previous bridge gives

\[
D<0.981G,
\qquad G=2^{33}.
\]

The full A0 word has more than enough odd ordinals for the preceding potential once the bound is closed self-consistently: if `p` reached the full `Q0` scale, the ordering-only cost would already exceed

\[
Q_0/6>1.398G,
\]

contradicting the reset budget.

Hence `p<Q0`, and the full potential applies.  Consequently

\[
\boxed{
p<6(0.981G)+1<50.561\times10^9.}
\]

This is still far too large for brute-force enumeration, but it converts the formally unbounded displacement coordinate into a certified finite interval in the reset sector.

The promoted `d<2G` strip has the weaker defect budget `D<2.503G`; this particular coarse ordering potential does not yet yield a comparably useful `p` cutoff there.

## 9. DSD structural chain

The boundary-state branch now separates into

\[
\boxed{
(K,p)
\to
\begin{cases}
\text{exact same-K dominance in }p,\\
\text{horizon-dependent ternary carry information},\\
\text{two-boundary affine invariant }\Xi_h.
\end{cases}
}
\]

The structural lesson is important:

- `p` has a valid monotone dominance order;
- `K` does **not** admit a fixed-depth exact residue quotient;
- but the pair of K-boundaries has an exact affine covariance.

So the correct compression target is a boundary-preserving quotient/potential, not a one-sided residue truncation.

## 10. Audit status

### SAFE

- same-exact-K `p` dominance;
- h-step lift identity;
- horizon-dependent residue-depth requirement;
- two-boundary affine covariance and invariant `Xi_h`;
- ordering-only `p` persistence potential;
- reset-strip finite `p` cutoff.

### REJECTED

- fixed `K mod 3^m` as an exact quotient for arbitrarily long blocks;
- any state compression that merges distinct `K` lifts merely because their first `m` ternary digits agree, without a separately proved lower-bound relaxation.

### OPEN

- whether the affine invariant `Xi_h`, together with a finite amount of residue/interface data, gives a sufficient lower-bound quotient;
- construction of a Bellman dual potential `Phi(K,p)` strong enough to exceed the near-root budget;
- use of the Euclidean/Christoffel hierarchy to propagate such a potential through the full A0 word.

## 11. Next Gate

The next safe direction is to use the exact lift covariance to define a **two-boundary normalized carry coordinate**, then test Bellman inequalities on the short Euclidean ancestor blocks.

The criterion remains

\[
\boxed{
\text{certified Hensel lower cost}
>
\text{near-root upper defect budget}.
}
\]

Companion finite regression:

`collatz/src/hensel_boundary_state_compression_regression.py`

The finite regression is not used as the proof of the all-h lemmas; those are proved symbolically above.
