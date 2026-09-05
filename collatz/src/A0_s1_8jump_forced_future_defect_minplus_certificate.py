#!/usr/bin/env python3
"""Finite source-sensitive future-defect min-plus audit from the jump-8 frontier.

The exact theorem is documented in

    ../theorems/FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md

This program imports the already-certified jump-8 P_min state reconstruction
and expands exact source-preserving valuation children for four additional
one-events.  For each original jump-8 parent and each horizon r=1..4 it
separately records:

* no surviving pure-ballot descendant by that horizon;
* surviving descendants with future floor F_min == 0;
* surviving descendants with genuinely forced F_min > 0;
* whole-parent closure when every horizon survivor is physically rejected
  (branches that died pure ballot earlier are already closed).

The future floor is evaluated at the descendant normalization:

    N_desc = 3^r * N_parent + F_path.

No historical prefix-defect lower bound is added to N_parent.
No source payloads are merged.

The execution is finite evidence only and does not establish a universal
Route-B or Collatz theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

import A0_s1_14root_8jump_Pmin_recheck_certificate as pmin


MAX_FUTURE_JUMPS = 4

# Previously reconstructed raw pure-ballot layer totals.  Keeping them here as
# exact regression targets turns this run, when executed in the repository,
# into the formal check for the jump-9..12 counts as well.
EXPECTED_LAYER = {
    0: (14_224, 26_859_837_368_845_079_186),
    1: (34_318, 23_697_743_382_405_825_230),
    2: (93_000, 21_589_704_816_219_050_321),
    3: (209_784, 18_423_678_262_570_974_925),
    4: (609_808, 16_690_807_021_040_991_694),
}


@dataclass(frozen=True)
class ParentHorizonResult:
    horizon: int
    surviving_descendants: int
    surviving_population: int
    future_floor: int | None
    zero_future_path_exists: bool
    all_survivors_physically_closed: bool

    @property
    def ballot_closed_by_horizon(self) -> bool:
        return self.surviving_descendants == 0

    @property
    def forced_positive_future_defect(self) -> bool:
        return self.future_floor is not None and self.future_floor > 0

    @property
    def whole_parent_closed(self) -> bool:
        return self.ballot_closed_by_horizon or self.all_survivors_physically_closed


def audit_parent(parent: pmin.State) -> list[ParentHorizonResult]:
    layer = [parent]
    out = []

    for r in range(1, MAX_FUTURE_JUMPS + 1):
        layer = [child for st in layer for child in pmin.children(st)]

        if not layer:
            out.append(ParentHorizonResult(
                horizon=r,
                surviving_descendants=0,
                surviving_population=0,
                future_floor=None,
                zero_future_path_exists=False,
                all_survivors_physically_closed=True,
            ))
            # Once no legal descendant remains, later horizons remain closed.
            for rr in range(r + 1, MAX_FUTURE_JUMPS + 1):
                out.append(ParentHorizonResult(
                    horizon=rr,
                    surviving_descendants=0,
                    surviving_population=0,
                    future_floor=None,
                    zero_future_path_exists=False,
                    all_survivors_physically_closed=True,
                ))
            break

        transported_current = (3 ** r) * parent.N
        extras = [st.N - transported_current for st in layer]
        assert all(F >= 0 for F in extras)

        floor = min(extras)
        zero_exists = any(F == 0 for F in extras)
        assert zero_exists == (floor == 0)

        # The theorem's zero-floor criterion: positive floor means every exact
        # surviving source descendant has acquired at least one genuinely new
        # target displacement in the audited horizon.
        if floor > 0:
            assert not zero_exists

        out.append(ParentHorizonResult(
            horizon=r,
            surviving_descendants=len(layer),
            surviving_population=sum(st.count for st in layer),
            future_floor=floor,
            zero_future_path_exists=zero_exists,
            all_survivors_physically_closed=all(
                pmin.physically_closed(st) for st in layer
            ),
        ))

    assert len(out) == MAX_FUTURE_JUMPS
    return out


parents = pmin.states
assert len(parents) == EXPECTED_LAYER[0][0]
assert sum(st.count for st in parents) == EXPECTED_LAYER[0][1]

# Global layer regression from the same exact children relation.
global_layer = list(parents)
for r in range(1, MAX_FUTURE_JUMPS + 1):
    global_layer = [child for st in global_layer for child in pmin.children(st)]
    observed = (len(global_layer), sum(st.count for st in global_layer))
    assert observed == EXPECTED_LAYER[r]

# Parent-resolved min-plus audit.
results_by_parent = [audit_parent(parent) for parent in parents]

for r in range(1, MAX_FUTURE_JUMPS + 1):
    rs = [rows[r - 1] for rows in results_by_parent]

    ballot_closed = [x for x in rs if x.ballot_closed_by_horizon]
    zero_floor = [
        x for x in rs
        if (not x.ballot_closed_by_horizon) and x.future_floor == 0
    ]
    positive_floor = [x for x in rs if x.forced_positive_future_defect]
    whole_closed = [x for x in rs if x.whole_parent_closed]

    assert len(ballot_closed) + len(zero_floor) + len(positive_floor) == len(parents)

    parent_population_ballot_closed = sum(
        parent.count
        for parent, rows in zip(parents, results_by_parent)
        if rows[r - 1].ballot_closed_by_horizon
    )
    parent_population_positive_floor = sum(
        parent.count
        for parent, rows in zip(parents, results_by_parent)
        if rows[r - 1].forced_positive_future_defect
    )
    parent_population_whole_closed = sum(
        parent.count
        for parent, rows in zip(parents, results_by_parent)
        if rows[r - 1].whole_parent_closed
    )

    positive_values = [
        x.future_floor for x in positive_floor
        if x.future_floor is not None
    ]

    print(
        "horizon", r,
        "global_descendant_cylinders", EXPECTED_LAYER[r][0],
        "global_descendant_population", EXPECTED_LAYER[r][1],
        "parent_ballot_closed", len(ballot_closed),
        "parent_zero_future_floor", len(zero_floor),
        "parent_positive_future_floor", len(positive_floor),
        "parent_whole_closed_ballot_or_physical", len(whole_closed),
        "population_ballot_closed_parents", parent_population_ballot_closed,
        "population_positive_floor_parents", parent_population_positive_floor,
        "population_whole_closed_parents", parent_population_whole_closed,
        "minimum_positive_future_floor",
        min(positive_values) if positive_values else None,
    )

print("PASS A0 s=1 jump8 forced-future-defect min-plus certificate")
print("source_payload_merging_used", False)
print("historical_prefix_defect_added_to_current_N", False)
print("future_normalization", "N_desc=3^r*N_parent+F_path")
print("max_future_one_horizon", MAX_FUTURE_JUMPS)
print("status", "EXACT finite source-tree execution; no universal closure claimed")
