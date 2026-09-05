# S10 audit — bounded-displacement source reachability

Status: **finite theorem CLOSED / jump-8 cumulative pruning EXACT / asymptotic density OPEN**

## Audited question

Can the first unavoidable future displacement be strengthened to a genuinely cumulative statement without following all unrestricted valuation descendants?

Yes, at fixed small displacement budget.

Define `R_{r,c}(s)` as the exact source-preserving future paths of horizon `r` with at most `c` displaced target ranks.

The search retains the source parameter interval and discards no distinct payload by quotienting.

---

## D — Domain

Input is the 14,224 first-75-tightened jump-8 source intervals.

For the reachability test itself, later first-75/Hamming tightening is intentionally omitted.  Thus the searched class is a relaxed superset of the canonical class.

Emptiness of the relaxed class is therefore safe for the canonical class.

**Status: EXACT / conservative.**

---

## R — Resolution

Each candidate displaced rank fixes an actual next one-position and therefore one exact valuation/source residue intersection.

No probabilistic density or approximate phase is used.

**Status: EXACT.**

---

## S — State sufficiency

For reachability, `(y,m_lo,m_hi,h,q)` plus the used displacement count is sufficient.  Source residue `r` and accumulated defect are not needed to decide whether a low-displacement continuation exists, but are retained in the parent state for downstream physical pruning.

**Status: SUFFICIENT for this predicate.**

---

## E — Finite equivalence

The exact executions give:

- at most 0 displaced ranks: last nonempty horizon `40`, empty at `41`;
- at most 1 displaced rank: last nonempty horizon `44`, empty at `45`;
- at most 2 displaced ranks: last nonempty horizon `45`, empty at `46`.

Therefore

\[
\boxed{
D_{46}\ge3
}
\]

for every relaxed source+pure-ballot survivor of every current parent.

**Status: EXACT finite result.**

---

## T — Defect transport

Each displaced target rank contributes normalized defect

\[
\epsilon_r>\frac1{12}.
\]

Therefore every horizon-46 survivor has

\[
\boxed{
\eta_{future}>\frac14.
}
\]

No power-of-three normalization mixing is needed because `eta=N/3^q` is additive across ranks.

**Status: EXACT / CLOSED.**

---

## C — Incremental closure

Apply the lower bound only after the already-certified first-75 tightening.

For every source value above the resulting directed physical cutoff, either:

1. it loses the relaxed ballot condition before horizon 46, or
2. it survives and necessarily has future defect `>1/4`, which triggers the physical rejection inequality.

This removes exactly

\[
\boxed{56{,}968{,}804}
\]

additional source integers from `6,728` current parent intervals.

No entire current parent interval is deleted.

The canonical tightened population becomes

\[
\boxed{26{,}859{,}837{,}368{,}531{,}301{,}450}.
\]

**Status: EXACT finite incremental pruning.**

---

## N — Non-independence

The `>1/4` floor is derived deterministically from source reachability and target displacement.  It is not an independent probability factor.

The pruning is applied sequentially on the first-75-tightened intervals, so there is no overlap double counting with the earlier `256,808,932` reduction.

**Status: overlap resolved by sequential exact interval application.**

---

## O — Outstanding

1. extend bounded-displacement reachability to `c>=3` with a more efficient sparse-pattern or dynamic representation;
2. do not extrapolate the observed `40,44,45` horizon pattern into a linear displacement density without proof;
3. use the global `P_min` reachability partition: only the upper ~17.905% source region can ever benefit from additional future-defect work;
4. seek a different independent source-sensitive gate for the lower ~82.095% `P_min`-unreachable region;
5. if a scalable lower bound on displacement count is found, compare it directly against the source-dependent physical defect budget in normalized `eta` coordinates.

---

## DSD verdict

\[
\boxed{
\text{Repeated future displacement is now proved at finite horizon and yields the first new post-jump8 incremental pruning.}
}
\]

The result is finite and local to the current Route-B frontier.  No asymptotic displacement-density or global Collatz conclusion follows.

## Dependencies

- `../theorems/BOUNDED_DISPLACEMENT_SOURCE_REACHABILITY.md`
- `../src/A0_s1_8jump_bounded_displacement_reachability_certificate.py`
- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`
- `../theorems/PMIN_GLOBAL_FUTURE_REACHABILITY_CUTOFF.md`
