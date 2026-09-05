#!/usr/bin/env python3
"""Four-state cylinder theorem for finite Route-B source intervals.

Let I=[L,U] cap Z have size N and refine by all parameter residues modulo
M=2^i.  Write

    L = Q M + s,   0 <= s < M,
    N = t M + u,   0 <= u < M.

For residue a mod M, the child parameter interval has

    lower(a) = Q + 1[a < s],
    size(a)  = t + 1[(a-s) mod M < u].

Thus at a fixed refinement level all nonempty child interval payloads occupy
at most four projective states: two possible lower endpoints times two possible
cardinalities.  The residue set of each flag pair is the intersection of a
linear interval with a circular interval (or its complement), hence is a union
of at most two ordinary residue intervals.

This file exhaustively audits the formulas over a finite domain.  The theorem
is elementary interval arithmetic and does not depend on the regression range.
"""


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def direct_child(L: int, U: int, a: int, M: int):
    lo = ceil_div(L - a, M)
    hi = (U - a) // M
    return None if lo > hi else (lo, hi)


def formula_child(L: int, N: int, a: int, M: int):
    Q, s = divmod(L, M)
    t, u = divmod(N, M)
    low_flag = int(a < s)
    heavy_flag = int(((a - s) % M) < u)
    lo = Q + low_flag
    size = t + heavy_flag
    return None if size == 0 else (lo, lo + size - 1), (low_flag, heavy_flag)


def circular_intervals(start: int, length: int, M: int):
    """Represent {start,...,start+length-1} mod M by <=2 linear intervals."""
    assert 0 <= start < M
    assert 0 <= length <= M
    if length == 0:
        return ()
    if length == M:
        return ((0, M - 1),)
    end = start + length - 1
    if end < M:
        return ((start, end),)
    return ((start, M - 1), (0, end % M))


def intersect_interval_sets(A, B):
    out = []
    for a0, a1 in A:
        for b0, b1 in B:
            lo = max(a0, b0)
            hi = min(a1, b1)
            if lo <= hi:
                out.append((lo, hi))
    out.sort()
    # Merge touching pieces for a canonical representation.
    merged = []
    for lo, hi in out:
        if merged and lo <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return tuple(merged)


def interval_values(parts):
    vals = set()
    for lo, hi in parts:
        vals.update(range(lo, hi + 1))
    return vals


formula_checks = 0
four_state_checks = 0
compact_cell_checks = 0
partition_checks = 0

for L in range(-20, 21):
    for N in range(1, 41):
        U = L + N - 1
        for i in range(1, 11):
            M = 1 << i
            Q, s = divmod(L, M)
            t, u = divmod(N, M)

            payload_states = set()
            direct_by_flags = {(lf, hf): set() for lf in (0, 1) for hf in (0, 1)}
            total = 0

            for a in range(M):
                direct = direct_child(L, U, a, M)
                formula, flags = formula_child(L, N, a, M)
                assert direct == formula
                formula_checks += 1

                if direct is not None:
                    lo, hi = direct
                    size = hi - lo + 1
                    payload_states.add((size, lo))
                    total += size

                direct_by_flags[flags].add(a)

            assert total == N
            partition_checks += 1

            # At fixed depth, literal lower endpoints are already only Q,Q+1,
            # so every projective reduction also has <=4 payload states.
            assert len(payload_states) <= 4
            four_state_checks += 1

            low_sets = {
                1: ((0, s - 1),) if s else (),
                0: ((s, M - 1),) if s < M else (),
            }
            heavy = circular_intervals(s, u, M)
            light = circular_intervals((s + u) % M, M - u, M)
            heavy_sets = {1: heavy, 0: light}

            reconstructed_all = set()
            for lf in (0, 1):
                for hf in (0, 1):
                    pieces = intersect_interval_sets(low_sets[lf], heavy_sets[hf])
                    assert len(pieces) <= 2
                    got = interval_values(pieces)
                    assert got == direct_by_flags[(lf, hf)]
                    reconstructed_all |= got
                    compact_cell_checks += 1

            assert reconstructed_all == set(range(M))


print("PASS A0 s=1 Route-B interval four-state cylinder certificate")
print("lower_endpoint_range", "-20..20")
print("cardinality_range", "1..40")
print("max_refinement_depth", 10)
print("formula_checks", formula_checks)
print("partition_checks", partition_checks)
print("four_state_checks", four_state_checks)
print("compact_cell_checks", compact_cell_checks)
print(
    "exact_result",
    "at every fixed residue depth a consecutive source interval yields at most four nonempty interval payload states",
)
print(
    "compact_residue_result",
    "each of the four payload flag classes is representable by at most two ordinary residue intervals",
)
print(
    "dsd_audit",
    "payload-cylinder compression is exact and horizon-independent as an interval identity; control/admissibility state growth remains separate",
)
print(
    "status",
    "interval payload residue explosion CLOSED; source-control plus correction/ballot state-merging remains OPEN",
)
