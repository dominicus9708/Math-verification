# S10 audit — global future reachability of the directed `P_min` gate

Status: **theorem CLOSED / jump-8 partition EXACT / no Collatz closure implied**

## Audited question

On which current source values can additional future target-displacement defect still possibly make the existing directed physical `P_min` predicate fire?

The answer can be bounded globally without expanding future valuation branches.

For current normalized defect

\[
\eta_q=N_q/3^q,
\]

the remaining future defect is bounded above by the unused tail of the full target correction.

Using the certified Christoffel fixed-point envelope,

\[
\frac{C_T}{3^{j_0}}
\le
\frac{cW_{hi}}{mW_{lo}}.
\]

Hence a source-value cutoff `X_noP` exists below which `P_min` can never fire at any later depth.

---

## D — Domain

The exact canonical input is the first-75-tightened jump-8 frontier:

- 14,224 affine source cylinders;
- population `26,859,837,368,588,270,254`.

Each state retains its exact current `eta`, source interval, depth, and odd count.

**Status: EXACT.**

---

## R — Resolution

The future cap is rational and uses only outward-certified fixed-point endpoints already present in the Christoffel real-envelope certificate.

The source split is performed directly on the integer parameter interval by flooring the exact rational cutoff.

No floating point is used in assertions.

**Status: EXACT.**

---

## S — State sufficiency

The cutoff requires only the current exact source interval and `(q,eta)`.  No future H/L label, formation state, checkpoint residue, or explicit valuation tree is required.

**Status: SUFFICIENT.**

---

## E — Equivalence / interpretation

For `X<=X_noP`, the maximum possible remaining target-correction defect still leaves the directed score below its strict rejection barrier.

Therefore future `P_min` rejection is impossible on that source-value region.

This does **not** prove that the source value survives Route-B membership.  It proves only that this predicate is permanently unavailable there.

**Status: exact predicate-availability exclusion; survivor inference REJECTED.**

---

## T — Transition

No future transition is required to establish the lower `no-P` region.  The argument dominates every possible future completion at once.

The upper region remains live for possible future `P_min` pruning and must keep its source payload.

**Status: CLOSED.**

---

## C — Certified finite partition

On the first-75-tightened jump-8 frontier:

\[
\boxed{22{,}050{,}571{,}214{,}544{,}220{,}515}
\]

source integers lie in the permanently `P_min`-unreachable lower region, while

\[
\boxed{4{,}809{,}266{,}154{,}044{,}049{,}739}
\]

remain in the upper region where future `P_min` activation is not ruled out.

Thus approximately

\[
82.095\%\quad\text{vs.}\quad17.905\%
\]

of the tightened jump-8 population is separated by predicate availability.

Every one of the 14,224 present source intervals straddles the cutoff, so this is an exact interval split rather than whole-cylinder deletion.

The exact current `P` score adds zero further pruning after the first-75 tightening.

**Status: EXACT finite partition.**

---

## N — Non-independence

The first-75 tail tightening and the `P_min` reachability partition share the same directed physical envelope.

The certificate explicitly checks the overlap:

- the permanently no-P population is unchanged before versus after tail tightening;
- all `256,808,932` integers removed by first-75 tightening come from the upper P-reachable region;
- therefore the two reductions must not be added as independent fractions.

**Status: overlap resolved exactly; independent multiplication/addition REJECTED.**

---

## O — Outstanding

The result changes the principal strategy:

1. future-defect work intended solely to trigger `P_min` should be restricted to the upper `4.809e18` region;
2. the lower `22.051e18` region needs a different source-sensitive membership/rejection predicate;
3. a cumulative displacement-count lower bound may still help the upper region, but cannot be claimed as progress on the lower region merely because `P_min` is unavailable there;
4. seek a second independent gate whose activation is strongest in the lower source region.

---

## DSD verdict

\[
\boxed{
\text{`P_min` is now spatially localized: useful at most on the upper 17.905% of the tightened jump-8 population.}
}
\]

This is a proof-strategy contraction, not a Collatz candidate contraction.

## Dependencies

- `../theorems/PMIN_GLOBAL_FUTURE_REACHABILITY_CUTOFF.md`
- `../src/A0_s1_8jump_Pmin_global_future_reachability_cutoff_certificate.py`
- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`
