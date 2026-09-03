# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for the current computation.

## 1. Exact input family

Retained first-defect roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary source certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`.

Every active family is represented exactly as

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with a finite integer parameter interval.

Initial 14-root population:

\[
125{,}072{,}439{,}875{,}999{,}947{,}649.
\]

## 2. Persistent S10 state — MINIMIZED / CLOSED

Let

\[
S=q-Q(h),
\qquad
Q(h)=\min\{q:3^q>2^h\}.
\]

Then

\[
q=Q(h)+S.
\]

The persistent early/middle S10 state remains

\[
\boxed{(r,y,m_{lo},m_{hi},h,S).}
\]

Derived rather than stored:

- `q=Q(h)+S`;
- `3^q`;
- `n_rem=t0-h`;
- `q_rem=j0-Q(h)-S`.

Fixed target parameters:

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

Canonical dependencies:

- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `../theorems/FIXED_TARGET_COUNTER_DERIVATION.md`.

## 3. Exact valuation/source transition stack — CLOSED

For a source family the next `0^a1` branch selects

\[
\rho_a\equiv(2^a-y)3^{-q}\pmod{2^{a+1}},
\]

and writing

\[
m=\rho_a+2^{a+1}k
\]

produces another exact affine source cylinder.

Exact-pair residual inversion is also closed:

\[
a=v_2(R),
\qquad
R=2^nZ-3^qY.
\]

Canonical dependencies:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../theorems/AFFINE_VALUATION_CYLINDER_JUMP.md`;
- `../theorems/VALUATION_MACROBLOCK_COMPILATION.md`.

## 4. Eight-jump source frontier and sequential pruning

Pure-ballot jump-8 frontier:

\[
14{,}224\text{ source cylinders},
\]

\[
26{,}859{,}837{,}368{,}845{,}079{,}186
\]

source integers.

The first-75 tail-defect tightening removes

\[
256{,}808{,}932
\]

and leaves

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

The bounded-displacement horizon-46 gate then removes an additional, non-overlapping

\[
\boxed{56{,}968{,}804}
\]

source integers.

Therefore the current canonical jump-8 population is

\[
\boxed{
26{,}859{,}837{,}368{,}531{,}301{,}450
}.
\]

The source-cylinder count remains `14,224`; only upper parameter tails are shortened.

The current export object is

- `../src/A0_s1_8jump_bounded_displacement_reachability_certificate.py::pruned_states`.

This is the source set that downstream S10 work should import.

## 5. Bounded future displacement — CLOSED through budget 2

For future target ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` be the number of ranks with `d_k>0` among the first `r` future one-events.

Exact relaxed source+pure-ballot reachability gives:

- `D_r<=0`: last nonempty horizon `40`, empty at `41`;
- `D_r<=1`: last nonempty horizon `44`, empty at `45`;
- `D_r<=2`: last nonempty horizon `45`, empty at `46`.

Hence

\[
\boxed{D_{46}\ge3}
\]

for every horizon-46 survivor.

Every displaced target rank contributes normalized defect

\[
\epsilon_r>\frac1{12},
\]

so every horizon-46 survivor has

\[
\boxed{
\eta_{future}>\frac14.
}
\]

If a source value fails to reach horizon 46, it is already closed by the relaxed ballot condition.  Therefore the `>1/4` floor can be used as a parent-level source-tail rejection oracle.

Canonical dependencies:

- `../theorems/BOUNDED_DISPLACEMENT_SOURCE_REACHABILITY.md`;
- `../src/A0_s1_8jump_bounded_displacement_reachability_certificate.py`;
- `../audits/S10_BOUNDED_DISPLACEMENT_REACHABILITY_AUDIT.md`.

Do **not** extrapolate the observed horizons into an asymptotic displacement density without a separate theorem.

## 6. First zero-path failure and exact finite min-plus results — retained but no longer principal

For every original jump-8 parent, the all-target-position zero-future-defect path disappears by horizon `41`.

Exact first-failure minima were certified for all 14,224 parents.  Their minimum paths use:

- 1 displaced rank: 13,354 parents;
- 2 displaced ranks: 724;
- 3 displaced ranks: 124;
- 4 displaced ranks: 21;
- 5 displaced ranks: 1.

Those exact first-failure minima alone produce zero whole-parent physical closures.

They remain useful audit data, but the stronger cumulative statement `D_46>=3` is now the active finite-horizon result.

Canonical dependencies:

- `../theorems/FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`;
- `../src/A0_s1_8jump_zero_future_defect_residue_exclusion_certificate.py`;
- `../src/A0_s1_8jump_first_zero_failure_ordered_displacement_minimum_certificate.py`;
- `../audits/S10_FIRST_ZERO_FAILURE_ORDERED_DISPLACEMENT_AUDIT.md`.

## 7. Directed `P_min` predicate — globally localized by source value

The current exact realized defect is

\[
\eta_q=\frac{N_q}{3^q}.
\]

Using the full threshold correction and Christoffel fixed-point envelope,

\[
\frac{C_T}{3^{j_0}}
\le
\frac{cW_{hi}}{mW_{lo}}.
\]

This yields a source-value cutoff `X_noP` below which **no possible future defect can ever make the directed `P_min` gate fire**.

On the first-75-tightened jump-8 source set:

\[
\boxed{22{,}050{,}571{,}214{,}544{,}220{,}515}
\]

source integers lie in the permanently `P_min`-unreachable lower region, and

\[
\boxed{4{,}809{,}266{,}154{,}044{,}049{,}739}
\]

lie in the upper region where future `P_min` activation remains possible.

Thus approximately

\[
82.095\%\text{ no-P}
\qquad\text{vs.}\qquad
17.905\%\text{ P-reachable}.
\]

All `256,808,932` integers removed by first-75 tightening came from the upper P-reachable region; the permanently no-P lower population is unchanged.  Therefore these two effects are not independent.

The exact current `P` score itself adds zero further pruning after first-75 tightening.

Canonical dependencies:

- `../theorems/PMIN_GLOBAL_FUTURE_REACHABILITY_CUTOFF.md`;
- `../src/A0_s1_8jump_Pmin_global_future_reachability_cutoff_certificate.py`;
- `../audits/S10_PMIN_GLOBAL_FUTURE_REACHABILITY_AUDIT.md`.

Interpretation:

- future-defect work intended solely to trigger `P_min` belongs only to the upper ~17.905% region;
- the lower ~82.095% requires a different independent source-sensitive predicate.

## 8. Realized displacement defect — CLOSED / no double counting

For realized one-positions `a_j` and target positions `t_j`, with `s_j=t_j-a_j`,

\[
\boxed{
N=C_T-C_W
=\sum_{j=0}^{q-1}3^{q-1-j}2^{a_j}(2^{s_j}-1).
}
\]

Thus all displacement already realized in the prefix is already contained in current `N`.

If `N>0` and `j_*` is the earliest displaced rank,

\[
\boxed{v_2(N)=a_{j_*}.}
\]

Historical phase/displacement/skew lower bounds may not be added again when they describe the same realized prefix.

Canonical dependencies:

- `../theorems/TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`;
- `../src/A0_s1_target_displacement_defect_decomposition_certificate.py`;
- `../audits/S10_TARGET_DISPLACEMENT_DEFECT_AUDIT.md`.

## 9. Formation, correction-language, and finite-template status

### Formation

The minimized source state is sufficient to partition a live interval exactly by the next maximal macroblock descriptor `(b,H,D)`, but one wide source cylinder does not carry one common formation label.

Local formation entry is therefore an exact transient partition, not an independent pruning factor.

Direct local slack/carry recurrence cannot be globalized into one formation-rank path without an explicit bridge theorem.

### Correction language

Pure-ballot correction-language recursion is exact, but its first branch is the same `v2` information already used by the residual/valuation decoder.  It is not an independent pruning engine.

### Finite templates

Short-horizon source/ballot product templates are useful for execution reuse only.  At future raw-bit horizon `18`, all 14,224 current payloads are already separated.

Do not infer source merge from equal control, finite template, correction, or local formation labels.

## 10. Predicate activation schedule — CLOSED

Terminal ternary checkpoint observation activates only at

\[
q_{rem}=28,
\]

equivalently

\[
Q(h)+S=65{,}868{,}186{,}673.
\]

Post-checkpoint `Z mod2^27` belongs to S11/tail processing.

`C4F` remains OPEN and is not admitted as a state coordinate until its exact Route-B predicate is recovered or defined.

Checkpoint/debit/CRT state must not be carried early.

## 11. Closed/rejected routes that must not be restarted

1. terminal target-dominance mod-3 as independent pruning — **REJECTED / redundant**;
2. dominance-only weak CRT — **insufficient**;
3. `P_min` whole-cylinder check at raw jump-8 — **zero whole cylinders**;
4. contracting ceiling inside active pure-ballot S10 — **redundant**;
5. correction-language recursion as independent pruning — **REJECTED / same valuation information**;
6. H/L or local maximal-macroblock labels as independent pruning — **NON-INDEPENDENT** unless a new predicate uses them;
7. direct local slack/carry -> one global formation-rank path — **REJECTED without explicit bridge**;
8. adding historical realized-prefix displacement bounds to exact current `N` — **REJECTED / double count**;
9. dropping source residue `r` before source-sensitive predicates are discharged — **REJECTED**;
10. equal finite control/template signatures -> source merge — **REJECTED without right-congruence**;
11. using future-defect work to claim progress on the permanently no-P lower 82.095% — **REJECTED unless a different predicate consumes that defect information**.

## 12. Principal active object

The frontier is now split by predicate availability.

### Upper P-reachable sector (~17.905%)

Continue cumulative source-sensitive displacement/defect lower bounds, but only if they can materially strengthen the directed physical cut.

The next useful object is a scalable bound for

\[
D_r^{min}(s)
\]

or an equivalent normalized defect floor beyond the current exact result

\[
D_{46}\ge3.
\]

A sparse low-displacement symbolic cover is preferable to unrestricted valuation-tree expansion.

### Lower permanently no-P sector (~82.095%)

`P_min` cannot ever reject these values, even with the full remaining target-correction budget.

Therefore the principal research task here is a **different independent source-sensitive membership obstruction**.  Preferred candidates are:

1. exact long-range correction/checkpoint membership incompatible with the source interval;
2. a source-sensitive right-congruence or whole-fiber rejection not reducible to the existing valuation/correction representation;
3. a recovered, precisely defined `C4F` predicate if it genuinely supplies independent information;
4. terminal/checkpoint predicates only at their certified activation boundaries.

## 13. Immediate computation targets

1. import `pruned_states` from the bounded-displacement certificate as the canonical source set;
2. derive an efficient sparse representation for paths with at most `c` displaced ranks and test `c=3,4,...` without raw full-tree expansion;
3. measure whether additional cumulative displacement pruning is worthwhile inside the upper P-reachable sector only;
4. in parallel, search the lower no-P sector for a genuinely independent long-membership obstruction;
5. keep all source payload coordinates exact until a valid whole-fiber rejection or right-congruence applies;
6. keep checkpoint observations late-activated.

## 14. DSD audit rules

Allowed:

- exact source-preserving valuation or certified multibit transitions;
- exact correction/residual recursion;
- exact sequential interval pruning;
- finite-horizon relaxed-class emptiness when used only as a safe lower bound for a stricter class;
- normalized future defect when derived from forced displaced ranks;
- predicate-availability partitioning by a rigorous global upper bound.

Forbidden:

- exact-pair uniqueness -> family uniqueness;
- equal control/template/formation label -> equal source payload;
- local recurrence equality -> global formation path;
- correction/formation/displacement re-expression -> independent pruning;
- double counting already-realized defect;
- mixing defect normalizations;
- adding overlapping pruning fractions without interval intersection;
- extrapolating finite `c<=2` displacement data to asymptotic density;
- carrying checkpoint observations before they exist;
- finite Route-B results -> global Collatz closure.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`.  Route-A, `s>=2`, remaining sectors, and global branch completeness remain separate obligations before any Collatz conclusion.
