# Exact ordered-displacement minimum at the first zero-path failure horizon

Status: **EXACT finite-horizon theorem / certified on the current jump-8 frontier**

## 1. Purpose

The zero-future-defect certificate shows that every current jump-8 source cylinder eventually loses its unique target-exact future path, with first failure horizon

\[
r_0\in\{12,13,\ldots,41\}.
\]

At that horizon the zero-defect path is absent, so any legal horizon-`r_0` descendant must contain at least one displaced future one-event.

This note gives an exact branch-and-bound method for computing

\[
\boxed{F_{r_0}^{min}}
\]

without expanding the unrestricted valuation tree.

## 2. Ordered future positions

For a parent with current odd count `q`, write the next `r` target one-positions as

\[
t_k:=t_{q+k},
\qquad 0\le k<r.
\]

A legal descendant has future one-positions

\[
u_0<u_1<\cdots<u_{r-1},
\qquad u_k\le t_k.
\]

Define the ordered displacement

\[
d_k:=t_k-u_k\ge0.
\]

Then

\[
F_r
=
\sum_{k=0}^{r-1}
3^{r-1-k}
\left(2^{t_k}-2^{t_k-d_k}\right).
\]

A rank is called displaced when `d_k>0`.

## 3. Exact enumeration by displacement count

Fix a displacement count `c`.

Choose the displaced ranks

\[
k_1<\cdots<k_c.
\]

All unchosen ranks have `d_k=0`.
The strict ordering of actual one-positions gives the exact finite upper bound on each chosen displacement.

For the first chosen rank `k`:

\[
t_k-d_k>
\begin{cases}
h-1,&k=0,\\
t_{k-1},&k>0,
\end{cases}
\]

because every earlier rank is still target-exact.

For a later chosen rank `k_j`:

- if `k_j=k_{j-1}+1`, compare against the displaced previous actual position `t_{k_{j-1}}-d_{k_{j-1}}`;
- otherwise rank `k_j-1` is target-exact, so compare against `t_{k_j-1}`.

Thus every exact ordered displacement vector with exactly `c` nonzero coordinates can be enumerated finitely.

For each vector, consume its prescribed valuation sequence through the certified source-preserving transition.
The vector is feasible if and only if the resulting source interval is nonempty throughout.

Therefore the least feasible cost among exactly `c` displaced ranks,

\[
B_c,
\]

is computed exactly.

## 4. Lower bound for paths with many displaced ranks

For any displaced rank `k`,

\[
2^{t_k}-2^{t_k-d_k}
\ge 2^{t_k-1}.
\]

Define the unit atom

\[
w_k:=3^{r-1-k}2^{t_k-1}.
\]

The earliest displaced rank cannot be arbitrary.
If `k` is the first displaced rank, then all previous ranks are target-exact and a one-step left shift must fit strictly after the previous actual one.
Let `A_first` be the ranks satisfying

\[
t_k-1>
\begin{cases}
h-1,&k=0,\\
t_{k-1},&k>0.
\end{cases}
\]

For every path with at least `c` displaced ranks, let `k` be its earliest displaced rank.
The remaining `c-1` displaced ranks are distinct later indices, each contributing at least its corresponding `w_j`.
Hence the exact path cost obeys the safe combinatorial lower bound

\[
\boxed{
L_c
:=
\min_{k\in A_{first}}
\left(
 w_k+
 \sum_{c-1\ \mathrm{smallest}\ j>k}w_j
\right).
}
\]

The bound intentionally ignores some ordering constraints among the later displaced ranks, so it can only be weaker than the true minimum and is therefore SAFE.

## 5. Exact stopping rule

Suppose exact enumeration has been completed for displacement counts `1,...,c`.
Let

\[
B_{\le c}:=\min(B_1,\ldots,B_c)
\]

over nonempty feasible classes.

Every path with more than `c` displaced ranks costs at least

\[
L_{c+1}.
\]

Therefore, if

\[
\boxed{B_{\le c}\le L_{c+1},}
\]

then no unenumerated higher-displacement path can beat the best already found and

\[
\boxed{F_r^{min}=B_{\le c}.}
\]

This is an exact branch-and-bound certificate, not a heuristic cutoff.

## 6. Current jump-8 frontier result

Apply the procedure at each parent's own first zero-path failure horizon `r_0`.

All 14,224 parents have at least one legal horizon-`r_0` descendant, so none is ballot-closed at that first failure horizon.
For every parent,

\[
\boxed{F_{r_0}^{min}>0}
\]

and the exact minimum is certified after enumerating at most six displaced-rank classes.

The displacement count of an actual minimum-cost path is distributed as follows:

| displaced ranks in a minimum path | parents | parent population |
|---:|---:|---:|
| 1 | 13,354 | 26,113,797,990,685,568,961 |
| 2 | 724 | 569,741,045,565,622,691 |
| 3 | 124 | 174,459,941,749,512,347 |
| 4 | 21 | 1,838,390,843,599,102 |
| 5 | 1 | 776,085 |
| total | 14,224 | 26,859,837,368,845,079,186 |

The single five-displacement minimum occurs in one 776,085-member jump-8 parent; a six-displacement class had to be checked only to prove that its feasible five-displacement path is globally minimal.

## 7. Physical-gate result

Insert each exact source-specific minimum in the correctly transported descendant normalization

\[
N_{desc}
\ge
3^{r_0}N_{parent}+F_{r_0}^{min}.
\]

Using the parent ordinary lower endpoint for the positive `X` term gives a SAFE whole-parent physical floor.

Exact finite result:

\[
\boxed{\text{whole-parent closures from this exact first-failure floor}=0.}
\]

The extra future defect required to cross the physical barrier remains much larger than the exact floor.
Across all 14,224 parents,

\[
145{,}742{,}202{,}315
\le
\left\lfloor
\frac{F_{required}}{F_{r_0}^{min}}
\right\rfloor
\le
920{,}214{,}076{,}930.
\]

Thus exact positivity alone is not the issue; even the exact first-failure minimum is still roughly `10^11`–`10^12` below what the present directed physical barrier needs.

## 8. Interpretation

The current source cylinders do not merely force *some* future displacement.
At a finite individualized horizon the minimum additional defect can be computed exactly with a very small displacement-count frontier.

However this exact floor has zero direct physical whole-fiber yield.
Therefore the next useful target is not to refine the first-failure minimum further.
It is to propagate beyond first failure and prove repeated/cumulative unavoidable displacement, or to find a different source-sensitive gate that uses the exact displacement pattern more efficiently than the current scalar physical score.

## 9. DSD classification

### EXACT / CLOSED

- ordered displacement parameterization;
- exact source feasibility of a fixed displacement vector;
- exact cost for a fixed vector;
- `L_c` lower bound for all paths with at least `c` displaced ranks;
- stopping rule `B_{<=c}<=L_{c+1}`;
- exact first-failure minimum on every current jump-8 parent.

### SAFE finite negative result

- zero whole-parent physical closures from these exact minima.

### OPEN

- repeated minimum-defect propagation after the first zero-path failure;
- a cumulative lower envelope strong enough to approach the physical barrier;
- an alternate source-sensitive rejection predicate that extracts more from the exact displacement vector than the scalar `P` score.

## Dependencies

- `ZERO_FUTURE_DEFECT_RESIDUE_EXCLUSION.md`
- `FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`
- `TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`
- `../src/A0_s1_8jump_first_zero_failure_ordered_displacement_minimum_certificate.py`
