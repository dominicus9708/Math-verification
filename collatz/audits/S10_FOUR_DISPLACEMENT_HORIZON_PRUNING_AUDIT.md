# S10 audit — four-displacement horizon pruning

Status: **EXACT finite current-frontier result / SAFE pruning / universal closure OPEN**

## Audited question

Does the canonical jump-8 source family force more than the previously certified three future displaced target ranks, and if so does that yield a new non-overlapping source reduction?

Yes.  The exact `c=3` reachability computation gives global `max H_3=48`, so every horizon-49 survivor has at least four future displaced ranks.  This strengthens the future defect floor from `>1/4` to `>1/3` and removes an additional 25,167,785 source integers.

---

## D — Domain

Input is the exact 14,224-interval source family after:

1. pure-ballot jump-8 refinement;
2. first-75 defect-tail tightening;
3. the previously certified `eta_future>1/4` upper-tail cut.

The source state is retained exactly; the reachability computation uses `(y,lo,hi,h,q)` only because `r` and historical defect are irrelevant to future source-residue existence.

**Status: EXACT.**

---

## R — Resolution

The exact decision predicate is

\[
R(s,c,r)=
\text{existence of a nonempty exact source descendant of horizon }r
\text{ with at most }c\text{ displaced target ranks}.
\]

No density, floating-point probability, or approximate source count is used.

The 14,224 parents were partitioned into 16 disjoint parent shards of 889 states.  Sharding changes only execution order.

**Status: EXACT.**

---

## S — State sufficiency

Future source-child existence is determined by the exact affine endpoint state and live integer parameter interval.  The transition for displacement `d` is one exact dyadic residue intersection.

No H/L history, formation rank, checkpoint residue, or source merge is required.

**Status: SUFFICIENT.**

---

## E — Equivalence

For each source state,

\[
H_3(s)<49
\]

is equivalent to nonexistence of a horizon-49 exact source path with at most three displaced target ranks.

The shard maxima were

`(45,46,45,48,45,45,45,45,46,46,45,45,45,45,45,45)`.

Thus

\[
\max_sH_3(s)=48
\]

and every horizon-49 survivor has at least four displaced ranks.

**Status: EXACT finite equivalence.**

---

## T — Transition

The sparse recursion skips maximal zero-displacement runs and branches only when a positive displacement is spent:

\[
H_c(s)=\max\left(
L_0(s),
\max_{k,d>0}[k+1+H_{c-1}(\chi_d(z_k))]
\right).
\]

The independent decision implementation `R(s,c,r)` was used for the sharded execution and is logically equivalent to testing `r<=H_c(s)`.

**Status: EXACT / CLOSED.**

---

## C — Closure

The finite `c=3` computation is closed for the current input family.

Every displaced mechanical rank has normalized defect `>1/12`, hence the four-rank result gives

\[
\eta_{future}>1/3.
\]

Weakening to `>=1/3` and applying the existing directed physical endpoint formula gives:

- prior `1/4` population: `26,859,837,368,531,301,450`;
- additional removal: `25,167,785`;
- new population: `26,859,837,368,506,133,665`;
- additionally affected intervals: `6,310`;
- whole intervals eliminated: `0`;
- remaining interval labels: `14,224`.

**Status: SAFE exact finite pruning; no whole-family closure.**

---

## N — Non-independence

The new `1/3` floor and old `1/4` floor constrain the same unresolved future defect.  They are nested bounds, not independent effects.

Therefore the valid composition is

\[
1/4\longrightarrow1/3,
\]

not

\[
1/4+1/3.
\]

Likewise, the four-displacement floor must not be multiplied by any marginal survival fraction.

**Status: replacement/refinement only; additive or probabilistic double counting REJECTED.**

---

## O — Outstanding

1. export the new `1/3`-pruned exact source intervals as the canonical downstream frontier;
2. compute `c=4` exact bounded-displacement reachability on that smaller frontier rather than extrapolating from `c=3`;
3. if a five-displacement floor is obtained, replace `1/3` by the corresponding stronger floor and measure only the incremental endpoint cut;
4. in parallel, continue seeking an independent long-membership gate for the large lower source sector on which `P_min` cannot activate even under maximum future defect;
5. do not infer whole Route-B closure from these finite horizon results.

---

## Audit matrix

| Dimension | Result |
|---|---|
| D | exact current 14,224 source intervals |
| R | exact dyadic source-child reachability |
| S | affine endpoint + live interval sufficient |
| E | `max H3=48` iff no <=3-displacement path survives horizon 49 |
| T | exact sparse/decision recursion |
| C | c=3 finite result CLOSED; +25,167,785 SAFE pruning |
| N | `1/3` supersedes `1/4`; no addition or density multiplication |
| O | c=4 and independent lower-sector membership gate OPEN |

## Dependencies

- `../theorems/SPARSE_FIRST_DISPLACEMENT_REACHABILITY_RECURSION.md`
- `../theorems/FOUR_DISPLACEMENT_HORIZON_PRUNING.md`
- `../src/A0_s1_8jump_c3_displacement_horizon_shard.py`
- `../src/A0_s1_8jump_four_displacement_eta_pruning_certificate.py`
- `../src/A0_s1_8jump_bounded_displacement_reachability_certificate.py`

## Final verdict

\[
\boxed{
\text{The current source family forces four future displaced ranks by horizon 49,}
\quad
\eta_{future}>1/3,
}
\]

and the corresponding strengthened endpoint cut is exact and non-overlapping with the previously counted `1/4` pruning when treated as a replacement.
