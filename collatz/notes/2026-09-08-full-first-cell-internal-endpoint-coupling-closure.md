# MATH-036 — full-first-cell internal adjacent-block endpoint-coupling closure

## Status

`CONFIRMED / FINITE ONLY / MECHANISM CLOSED THROUGH FIRST UNIVERSAL CROSSING`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

The result closes one internal endpoint-coupling mechanism; it does **not** prove first-cell emptiness.

## 1. First-crossing halo target

The first coefficient-crossing depth is

\[
A_0=114,208,327,604.
\]

MATH-021 gives the necessary same-endpoint displacement condition

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Therefore every internal adjacent-block same-endpoint coupling with

\[
k\le A_0
\]

must have right offset at most

\[
R_*=\left\lfloor\frac{A_0-1}{3}\right\rfloor
=\boxed{38,069,442,534}.
\]

Thus the full mechanism can be audited by a finite right-offset domain.

## 2. Interval-pruned 64-bit shell engine

A 64-bit shell engine was introduced so later ranges do not re-enumerate all smaller offsets.

At binary-prefix depth `k`, a state with fixed low prefix `r0` has possible depth-`FIXK` descendants

\[
r=r_0+t2^k.
\]

The engine retains the subtree only if some integer `t` can place a descendant inside the requested interval `[L,U]`. This is an exact selection gate; it does not merge states.

After `FIXK`, all higher bits are zero for the selected finite interval and the state is continued deterministically to depth 61. Depth-61 survivors then use the existing audited chain:

\[
\text{22-step cyclic address prefilter}
\to
\text{exact endpoint instantiation}
\to
\text{base-independent 22-step rolling gates}.
\]

The earlier `(4e9,8e9]` result was reproduced exactly after adding interval pruning before the larger shells were accepted.

## 3. Complete shell partition

The full right-offset domain `0..R*` was partitioned into disjoint contiguous shells. The exact aggregate totals are

\[
\boxed{68,385,325}
\]

depth-61 right-offset survivors,

\[
\boxed{7,225,448,447}
\]

exact depth-83 address states after the cyclic prefilter, and

\[
\boxed{11,202,913,510}
\]

base-83+ 22-step threshold gates.

Every shell returned

\[
\boxed{\text{survive to audited end}=0},
\qquad
\boxed{\text{endpoint overflow}=0}.
\]

The maximum observed failing-window base over the complete domain is

\[
\boxed{633}.
\]

After correcting witness tracking so it follows the current maximum base rather than a historical fixed base 545, the first audited witness at base 633 is

\[
\boxed{r=8,933,328,767,\qquad b=1251}.
\]

A failing 22-step gate based at 633 implies failure by depth 655 at the latest.

The cumulative depth-61 q support reaches

\[
q_{61}=54,
\]

with two states. No `q61>=55` state occurs in this finite domain. This is a finite observation, not a permanent type bound.

## 4. Why the large-depth range closes

The smallest positive right offset surviving through depth 61 remains

\[
\boxed{r_{\min}=703}.
\]

Any such right offset can enter the necessary linear collision halo only at

\[
k\ge3r+1\ge3\cdot703+1=\boxed{2110}.
\]

But every audited depth-61 survivor in the entire `0..R*` domain fails coefficient survival by depth 655 at the latest.

Hence no `r>=703` state can remain a candidate long enough to enter the necessary same-endpoint collision halo.

For `r<=702`, there is no depth-61 survivor, so those states cannot contribute for `k>=61`.

## 5. Independent small-depth closure

Depths `1..60` were audited separately, without relying on the depth-61 survivor argument.

For every

- `k=1..60`,
- internal boundary `b=1025..1363`,
- positive displacement satisfying `d<k/3`,
- decomposition `d=l+r` with `l>=1`, `r>=0`,

both adjacent starts were checked against the coefficient-survival prefix gate.

Exact total combinations checked:

\[
\boxed{1,352,610}.
\]

Joint coefficient-surviving pairs:

\[
\boxed{0}.
\]

Thus there is no small-depth internal adjacent-block same-endpoint candidate pair either.

## 6. Exact conclusion

Combining the independent small-depth scan with the complete `0..R*` shell audit gives

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
1\le k\le A_0
}
\]

within the current universal-spine/coefficient-survival candidate scope.

Equivalently, this endpoint-coupling mechanism is closed through the entire first universal crossing.

## 7. What this does not prove

This result does **not** say that the first universal cell contains no candidate.

A candidate may survive without sharing an endpoint with a candidate from the adjacent top-address block. Therefore

\[
\boxed{
\text{internal endpoint-coupling mechanism closed}
\not\Rightarrow
\text{first-cell emptiness}
}
\]

and certainly does not imply Collatz.

The value `633` is also only the finite maximum failing-window base in this audited domain. It is not a universal lifespan theorem.

## Reproducibility

- shell engine: `collatz/src/2026_09_08_interval_pruned_64bit_tail22_shell_engine.cpp`
- small-depth certificate: `collatz/src/2026_09_08_full_first_cell_small_depth_boundary_certificate.cpp`
- shell results: `collatz/results/2026-09-08-full-first-cell-internal-boundary-shell-results.csv`
- aggregate post-audit: `collatz/src/2026_09_08_full_first_cell_internal_endpoint_coupling_postaudit.py`

Corrected deepest-base witness tracking was independently rerun on both shells attaining base 633.
