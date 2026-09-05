#!/usr/bin/env python3
"""Exact arithmetic guard for critical-cut terminal precision absorption.

For a terminal predicate modulo 3^L crossing a right block with q_B one-events,
the projective block carry theorem exports only max(0,L-q_B) ternary digits.

The current A0 s=1 Route-B critical cut has q_B=397,573,380, so the active
24-, 28-, and 47-trit predicates are fully consumed inside the right H block.

This certificate checks the current constants and a finite implementation guard
for the generic precision map.  The general theorem is algebraic and is not
inferred from the finite loop.
"""

Q_RIGHT = 397_573_380
ACTIVE_L = (24, 28, 47)


def exported_precision(L: int, q_right: int) -> int:
    assert L >= 0
    assert q_right >= 0
    return max(0, L - q_right)


for L in ACTIVE_L:
    assert Q_RIGHT >= L
    assert exported_precision(L, Q_RIGHT) == 0

# Generic implementation guard for both branches of max(0,L-q_B).
checks = 0
for L in range(0, 65):
    for q in range(0, 65):
        out = exported_precision(L, q)
        if L <= q:
            assert out == 0
        else:
            assert out == L - q
        assert 0 <= out <= L
        checks += 1

assert checks == 65 * 65

print("PASS A0 s=1 critical-cut terminal precision absorption certificate")
print("q_right", Q_RIGHT)
for L in ACTIVE_L:
    print("terminal_precision", L, "cut_export_precision", exported_precision(L, Q_RIGHT))
print("generic_guard_checks", checks)
print("checkpoint_L28_cut_ternary_state", "DORMANT/ABSORBED")
print("status", "EXACT precision dimension; accepted z_H family and membership remain OPEN")
