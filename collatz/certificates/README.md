# Certificate index and execution policy

This directory is the canonical index for executable proof/audit certificates.

## Phase-1 path policy

Existing Python files remain physically in `../src/` for now.

Reason:

- many certificates import neighboring files directly by module name;
- chronological notes refer to existing paths;
- a bulk move could silently break reproducibility even if the mathematics is unchanged.

Therefore phase 1 classifies certificates here without moving them.  Physical migration to `certificates/` is allowed only after an import/reference audit.

## Certificate classes

### A — algebraic implementation guard

The mathematical theorem has an independent proof; the script checks indexing, composition formulas, or finite representatives.

Status in theorem documents: `REGRESSION ONLY` for the script, `EXACT` for the theorem if separately proved.

Examples:

- H/L grammar small-word regression;
- fixed `(h,q)` boundary projection regression;
- projective carry transition checks.

### B — exact finite exhaustive certificate

The finite result itself is established by exhaustive exact computation.

Examples:

- radius `0..7` closure;
- exact shell counts;
- finite corridor cardinalities.

Status: `CERTIFIED ARITHMETIC`.

### C — directed arithmetic certificate

Uses exact rationals / integer fixed-point bounds / outward rounding to certify a numerical inequality used by a theorem or SAFE pruning step.

Examples:

- Christoffel correction interval;
- physical X upper bound;
- inverse defect budget.

Status: `CERTIFIED ARITHMETIC`, often feeding `SAFE NECESSARY PRUNING`.

### D — search/frontier certificate

Executes the currently active family-level algorithm on a specified finite family and records exact closed/unresolved states.

The next planned object is the 14-root min-plus/physical-risk scan described in `../frontier/A0_S1_ROUTEB.md`.

## Current canonical certificate groups

### C2 — 14-root reduction

- `../src/A0_s1_radius7_defect_christoffel_real_envelope_certificate.py`
- `../src/A0_s1_prefix_defect_membership_pruning_certificate.py`
- `../src/A0_s1_14root_long_membership_forest_certificate.py`

### C3 — source / ballot / grammar / projective structure

Representative files:

- `../src/A0_s1_routeB_reduced_source_ballot_control_certificate.py`
- `../src/A0_s1_routeB_interval_four_state_cylinder_certificate.py`
- `../src/A0_s1_routeB_HL_fixed_resolution_family_DP_certificate.py`
- `../src/A0_s1_routeB_ternary_suffix_carry_dp_certificate.py`
- `../src/A0_s1_routeB_ternary_carry_transition_bijection_certificate.py`
- `../src/A0_s1_routeB_projective_block_ternary_carry_certificate.py`

### C4 — defect / physical closure

- `../src/A0_s1_routeB_normalized_defect_semiring_certificate.py`
- `../src/A0_s1_routeB_ternary_collider_defect_gap_certificate.py`
- `../src/A0_s1_routeB_projective_cylinder_defect_floor_certificate.py`
- `../src/A0_s1_routeB_defect_budget_inverse_certificate.py`
- `../src/A0_s1_routeB_displaced_rank_defect_count_certificate.py`

Additional latest min-plus / risk-state certificates remain indexed through the current frontier until their stable filenames and role are frozen by the next audit pass.

## Required header for new certificates

Every new certificate should state near the top:

- mathematical claim being checked;
- whether the script is the proof or only a regression;
- imported upstream dependencies;
- finite horizon/domain if any;
- exact vs floating-point arithmetic policy;
- what is explicitly **not** inferred.

## Execution log policy

A certificate should not be called `PASS` in a canonical status document merely because it was committed.

Distinguish:

1. **committed** — code exists;
2. **executed** — code ran in a specified environment;
3. **cross-checked** — independent implementation or direct finite comparison agrees;
4. **mathematical theorem closed** — requires the appropriate proof classification, not merely execution.

## Physical migration checklist

Before moving any legacy Python file from `src/`:

1. search all Python imports for its module name;
2. search all Markdown references for its path;
3. repair package imports (`__init__.py` / explicit package path) if needed;
4. move in a dedicated maintenance commit;
5. execute affected certificates;
6. leave a redirect/migration note for historical paths if external references may exist.

Until this checklist is complete, `src/` remains the executable legacy location and `certificates/` remains the canonical classification/index layer.
