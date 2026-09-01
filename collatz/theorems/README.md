# Theorem index

This directory is the role index for reusable mathematical statements. During reorganization phase 1, theorem evidence remains at its existing `notes/` / `src/` paths to preserve links and imports.

A theorem belongs in this index only when its general statement is algebraically/logically proved in the stated domain. Finite regression alone belongs under `certificates/`, not here.

## T0 — Source cylinder and deterministic refinement

Role:

- exact affine representation of a parity-prefix source family;
- exact parameter-bit refinement;
- deterministic continuation once enough ordinary X bits are exposed.

Legacy evidence lives under `../src/` with `prefix_channel`, `source_cylinder`, and related names.

## T1 — Ballot / dominance language

Role:

- pure-ballot one-position inequalities;
- fixed-count ballot future cone;
- target prefix-dominance language;
- surplus/counter representations.

Representative current notes:

- `../notes/2026-09-01-A0-s1-routeB-fixed-count-ballot-three-way-status.md`;
- `../notes/2026-09-01-A0-s1-routeB-target-ballot-surplus-dominance.md`.

## T2 — Dual H/L grammar

Role:

- universal exact H/L canonical decomposition and converse;
- intrinsic well-founded cut;
- target hierarchy specialization only after the universal grammar is established.

Representative note:

- `../notes/2026-09-01-A0-s1-routeB-dual-HL-canonical-grammar.md`.

Target H/L–Stern-Brocot alignment is target-specialized and must not be generalized to arbitrary H/L members.

## T3 — Correction composition and boundary localization

Role:

- fixed `(h,q)` correction injectivity;
- dyadic left-front localization;
- ternary right-front locality;
- critical-cut / block correction factorization;
- lazy terminal-ternary observation;
- critical-cut ternary shielding.

Canonical theorem objects:

- [`LAZY_TERNARY_OBSERVATION.md`](LAZY_TERNARY_OBSERVATION.md);
- [`CRITICAL_CUT_TERNARY_SHIELDING.md`](CRITICAL_CUT_TERNARY_SHIELDING.md).

Representative chronological note:

- `../notes/2026-09-01-A0-s1-routeB-fixed-hq-correction-collision-frontiers.md`.

## T4 — Projective ternary carry and formation feasibility

Role:

- one-step carry bijection;
- suffix-carry recurrence;
- projective block carry;
- displacement isometry / cylinder representation;
- uniform exponent-cylinder width;
- max-slack ordering-history quotient at fixed carry.

Canonical theorem objects:

- [`TERMINAL_PROJECTIVE_CYLINDER_WIDTH.md`](TERMINAL_PROJECTIVE_CYLINDER_WIDTH.md);
- [`BACKWARD_MAX_SLACK_PROJECTIVE_QUOTIENT.md`](BACKWARD_MAX_SLACK_PROJECTIVE_QUOTIENT.md).

Representative certificate names in `../src/`:

- `A0_s1_routeB_ternary_carry_transition_bijection_certificate.py`;
- `A0_s1_routeB_general_suffix_gate_displacement_isometry_certificate.py`;
- `A0_s1_routeB_projective_block_ternary_carry_certificate.py`;
- `A0_s1_routeB_terminal_projective_cylinder_multiplicity_certificate.py`;
- `A0_s1_routeB_backward_max_slack_projective_quotient_certificate.py`.

## T5 — Normalized defect

Role:

- monotonicity under target dominance;
- positive defect atoms;
- semiring/block composition;
- projective-cylinder exact minimum defect;
- phase-weighted / displaced-rank bounds.

Representative certificates:

- `../src/A0_s1_routeB_normalized_defect_semiring_certificate.py`;
- `../src/A0_s1_routeB_projective_cylinder_defect_floor_certificate.py`;
- `../src/A0_s1_routeB_displaced_rank_defect_count_certificate.py`.

## T6 — Physical closure functional

Role:

- directed Christoffel real envelope;
- defect floor -> safe physical X upper bound;
- inverse defect budget;
- integer defect numerator;
- exact scalar physical danger score / Bellman minimum state.

Representative certificates:

- `../src/A0_s1_radius7_defect_christoffel_real_envelope_certificate.py`;
- `../src/A0_s1_routeB_defect_budget_inverse_certificate.py`;
- `../src/A0_s1_routeB_integer_defect_numerator_certificate.py`;
- `../src/A0_s1_routeB_linear_physical_danger_score_certificate.py`.

## T7 — Finite interval family quotients

Role:

- exact interval child arithmetic;
- fixed-depth payload-state compression;
- predicate-relative active-frontier forgetting/absorption.

Representative certificate:

- `../src/A0_s1_routeB_interval_four_state_cylinder_certificate.py`.

---

# Promotion policy

When a chronological note is promoted into a canonical theorem object:

1. give the theorem a stable descriptive name independent of date;
2. state hypotheses, conclusion, and scope restrictions explicitly;
3. link its executable certificate separately;
4. retain the old dated note as history/source evidence;
5. update `../PROOF_MAP.md` only if the theorem changes a module obligation.

Phase 1 does not require moving legacy executable files from `src/`.
