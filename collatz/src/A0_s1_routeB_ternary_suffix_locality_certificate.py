#!/usr/bin/env python3
"""Exact ternary suffix-locality for target-relative dominance families.

For equal-one-count parity words T,W with one positions

    a_1<...<a_q,
    b_1<...<b_q,

the correction difference is

    Delta = C(T)-C(W)
          = sum_{r=1}^q 3^{q-r}(2^{a_r}-2^{b_r}).

At ternary observation depth L, every term with r<=q-L is already divisible by
3^L. Hence Delta mod 3^L depends only on the last L one-position pairs.

Inside a prefix-dominance family b_r<=a_r, this is also an existence reduction:
any strictly increasing legal choice of the last L candidate positions can be
completed on the left by the minimal prefix

    b_r=r-1,  1<=r<=q-L.

Indeed the first chosen suffix position is automatically >=q-L, so the minimal
prefix is strictly to its left, and r-1<=a_r holds for every target position
sequence. Therefore a ternary collider exists in the full dominance family iff
a legal last-L position sequence exists whose suffix correction difference is
0 mod 3^L.

This removes dependence on the earlier q-L one positions from the *existence*
of a target-relative ternary collider. It does not by itself bound the number
of suffix states as a function of L.
"""

from itertools import combinations

MAX_H = 9


def correction_positions(pos):
    q = len(pos)
    return sum((3 ** (q-r-1)) * (2 ** a) for r, a in enumerate(pos))


locality_checks = 0
completion_checks = 0

for h in range(1, MAX_H + 1):
    for q in range(1, h + 1):
        for a in combinations(range(h), q):
            Ct = correction_positions(a)

            for b in combinations(range(h), q):
                if not all(b[i] <= a[i] for i in range(q)):
                    continue
                Cw = correction_positions(b)

                for L in range(1, q + 1):
                    suffix_delta = sum(
                        (3 ** (q-r-1)) * (2 ** a[r] - 2 ** b[r])
                        for r in range(q-L, q)
                    )
                    assert (Ct - Cw - suffix_delta) % (3 ** L) == 0
                    locality_checks += 1

            for L in range(1, q + 1):
                start = q - L
                # A legal suffix position tuple must respect both ordering and
                # dominance.  Every such tuple is completed by 0,...,start-1.
                for bsuf in combinations(range(start, h), L):
                    if not all(bsuf[j] <= a[start+j] for j in range(L)):
                        continue
                    b = tuple(range(start)) + bsuf
                    assert len(b) == q
                    assert all(b[i] < b[i+1] for i in range(q-1))
                    assert all(b[i] <= a[i] for i in range(q))
                    completion_checks += 1

assert locality_checks == 101_763
assert completion_checks == 57_762

print("PASS A0 s=1 Route-B ternary suffix-locality certificate")
print("max_h", MAX_H)
print("locality_checks", locality_checks)
print("completion_checks", completion_checks)
print(
    "theorem",
    "Delta mod 3^L depends only on the last L one-position pairs",
)
print(
    "dominance_existence",
    "every legal last-L suffix position tuple extends by the minimal prefix 0,...,q-L-1",
)
print(
    "dsd_audit",
    "horizon dependence is reduced exactly to an L-local suffix problem; no state-count bound is inferred",
)
print(
    "status",
    "ternary collider existence locality CLOSED; compact projective suffix-state bound remains OPEN",
)
