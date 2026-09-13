#!/usr/bin/env python3
"""MATH-114 deterministic exact mass-balanced AP source sharder.

Input rows on stdin:
    a<TAB>b<TAB>m
represent AP(a,b,m) = {a+b*k : 0 <= k < m}.

For N shards:
1. compute total multiplicity mass T and cap=ceil(T/N);
2. split each source AP into consecutive, disjoint parameter intervals of
   length at most cap;
3. sort the exact pieces by descending mass (stable deterministic tiebreaks);
4. assign each piece to the currently least-mass shard (LPT scheduling).

Splitting identity:
  AP(a,b,m) = disjoint union_j AP(a+b*offset_j, b, m_j).

Thus scheduling changes only implementation/resource layout, not theorem state
or ordinary-integer membership.

Modes:
  --shards N --certificate       print shard counts/masses and global totals
  --shards N --shard K          emit exact AP rows assigned to shard K

Python integers are arbitrary precision, so this utility can partition source
families whose global or single-AP multiplicity exceeds uint64.  A downstream
u64 engine is safe only when each emitted shard mass and each emitted piece
count fit uint64; callers must assert that separately.
"""
import argparse
import heapq
import sys

U64_MAX = (1 << 64) - 1


def read_records():
    out = []
    for i, line in enumerate(sys.stdin):
        if not line.strip():
            continue
        p = line.split()
        if len(p) != 3:
            raise ValueError(f"bad input row {i}: {line!r}")
        a, b, m = map(int, p)
        if b <= 0 or b % 2 == 0 or m <= 0:
            raise ValueError(f"invalid AP row {i}")
        out.append((a, b, m, i))
    if not out:
        raise ValueError("empty input")
    return out


def build_partition(records, nshards):
    if nshards <= 0:
        raise ValueError("nshards must be positive")
    total = sum(m for _, _, m, _ in records)
    cap = (total + nshards - 1) // nshards

    pieces = []
    for a, b, m, source_i in records:
        offset = 0
        piece_i = 0
        remain = m
        while remain:
            take = min(remain, cap)
            pieces.append((take, source_i, piece_i, a + b * offset, b, offset))
            offset += take
            remain -= take
            piece_i += 1
        assert offset == m

    pieces.sort(key=lambda x: (-x[0], x[1], x[2]))
    heap = [(0, s) for s in range(nshards)]
    heapq.heapify(heap)
    shards = [[] for _ in range(nshards)]
    masses = [0] * nshards

    for take, source_i, piece_i, a, b, offset in pieces:
        cur, shard = heapq.heappop(heap)
        assert cur == masses[shard]
        shards[shard].append((a, b, take, source_i, piece_i, offset))
        masses[shard] += take
        heapq.heappush(heap, (masses[shard], shard))

    assert sum(masses) == total
    assert sum(len(x) for x in shards) == len(pieces)
    return total, cap, shards, masses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shards", type=int, required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--certificate", action="store_true")
    g.add_argument("--shard", type=int)
    args = ap.parse_args()

    records = read_records()
    total, cap, shards, masses = build_partition(records, args.shards)

    if args.certificate:
        print("shard\tpieces\tmass\tu64_safe")
        for i, rows in enumerate(shards):
            safe = masses[i] <= U64_MAX and all(r[2] <= U64_MAX for r in rows)
            print(i, len(rows), masses[i], int(safe), sep="\t")
        print("TOTAL", len(records), sum(len(x) for x in shards), total, sep="\t")
        print("CAP", cap, sep="\t")
        print("MIN_SHARD_MASS", min(masses), sep="\t")
        print("MAX_SHARD_MASS", max(masses), sep="\t")
        print("PASS exact mass-balanced AP partition")
        return

    k = args.shard
    if not (0 <= k < args.shards):
        raise ValueError("shard index out of range")
    for a, b, m, _source_i, _piece_i, _offset in shards[k]:
        print(a, b, m, sep="\t")
    print(f"SHARD {k} pieces {len(shards[k])} mass {masses[k]}", file=sys.stderr)
    assert masses[k] <= U64_MAX
    assert all(row[2] <= U64_MAX for row in shards[k])


if __name__ == "__main__":
    main()
