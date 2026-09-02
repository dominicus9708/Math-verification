#!/usr/bin/env python3
"""Exact guard for the terminal ranked-one window theorem.

For equal-count target/candidate correction difference

    Delta = sum_r 3^(q-r) (2^a_r - 2^b_r),

Delta mod 3^L depends only on ranks r=q-L+1..q.

If those final L candidate one-positions are target-dominant and leave at least
q-L slots before the first retained suffix one, they extend to a full dominant
candidate by the packed prefix b_r=r-1.

For the current right H target, L=28, so the synchronized checkpoint ternary
predicate is a finite 28-gate target-dominance existence problem.  Additional
H-grammar boundary labels and full membership remain separate.
"""

J0 = 10_439_860_591
R0 = 6_586_818_670
S = 630_138_897
QH = (R0 * S) // J0 + 1
L = 28


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def target_one_position(r: int) -> int:
    assert 1 <= r <= QH
    if r == 1:
        return 0
    return ceil_div((r - 1) * J0, R0) - 1


assert QH == 397_573_380
assert QH - L == 397_573_352

# Current exact last-28 target capacities.
rows = []
for t in range(L):
    r = QH - t
    A = target_one_position(r)
    base = QH - t - 1
    D = A - base
    m = L - t
    period = 2 * 3 ** (m - 1)
    cylinder_cap = D // period + 1
    assert D >= 0
    rows.append((t, m, r, A, D, period, cylinder_cap))

assert rows[0][:5] == (0, 28, 397_573_380, 630_138_896, 232_565_517)
assert rows[-1][:5] == (27, 1, 397_573_353, 630_138_854, 232_565_502)
assert all(row[6] == 1 for row in rows if row[1] >= 18)

# Generic finite guards for terminal-window residue locality and packed-prefix
# completion. These are implementation guards; the theorem is algebraic.
def correction_from_positions(pos):
    q = len(pos)
    return sum((3 ** (q-r-1)) * (1 << pos[r]) for r in range(q))

checks = 0
for q in range(1, 9):
    target = tuple(2*r for r in range(q))
    for L0 in range(1, q + 1):
        mod = 3 ** L0
        # Packed-prefix candidate with the final L0 ranks shifted only when
        # dominance/order permit it.
        cand = list(range(q))
        for r in range(q-L0, q):
            cand[r] = min(target[r], max(cand[r], target[r]-1))
        # repair strict ordering conservatively from left to right
        for r in range(1, q):
            cand[r] = max(cand[r], cand[r-1]+1)
            assert cand[r] <= target[r]

        full_delta = correction_from_positions(target) - correction_from_positions(tuple(cand))
        suffix_delta = 0
        for r in range(q-L0, q):
            suffix_delta += (3 ** (q-r-1)) * ((1 << target[r]) - (1 << cand[r]))
        assert full_delta % mod == suffix_delta % mod

        first_suffix = cand[q-L0]
        assert first_suffix >= q-L0
        packed = tuple(range(q-L0)) + tuple(cand[q-L0:])
        assert all(packed[r] < packed[r+1] for r in range(q-1))
        assert all(packed[r] <= target[r] for r in range(q))
        checks += 1

assert checks == 36

print("PASS A0 s=1 terminal ranked-one window dominance completion certificate")
print("qH", QH)
print("terminal_precision", L)
print("observable_ranked_one_events", L)
print("unobservable_earlier_one_events", QH-L)
print("first_row", rows[0])
print("last_row", rows[-1])
print("high_precision_singleton_rows", sum(1 for row in rows if row[1] >= 18 and row[6] == 1))
print("generic_guard_checks", checks)
print("status", "EXACT target-dominance 28-gate reduction; extra H-grammar control and full membership remain OPEN")
