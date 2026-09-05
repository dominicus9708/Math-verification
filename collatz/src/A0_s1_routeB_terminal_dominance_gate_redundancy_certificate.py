#!/usr/bin/env python3
"""Exact audit: terminal-28 dominance gate is redundant on genuine checkpoints.

For any binary correction word W with q>=1 ranked one-events at positions

    a_1 < ... < a_q,

its affine correction is

    C(W) = sum_{r=1}^q 3^(q-r) 2^a_r.

Modulo 3, every term except the last vanishes, so

    C(W) == 2^a_q (mod 3) in {1,2}.

For a genuine checkpoint identity

    2^h Z = 3^q X + C(W),

with q>=1, reduction mod 3 gives

    2^h Z == C(W) != 0 (mod 3).

Since 2^h is a unit modulo 3,

    Z mod 3 in {1,2}.

The independently certified terminal-28 target-dominance saturation theorem
says that the complete right-H dominance suffix exists iff exactly the same
condition holds:

    Z mod 3 in {1,2}.

Therefore every genuine fixed-positive-one-count pre-bridge checkpoint already
passes the terminal-28 dominance-only right-H gate.  The gate is a consistency
check, not a pruning predicate, unless an additional stronger predicate is
attached (source-controlled correction-language state, physical defect, etc.).

Finite regressions below are implementation guards only.
"""

from itertools import combinations


def correction_from_positions(pos):
    q = len(pos)
    return sum(3 ** (q-r-1) * (1 << pos[r]) for r in range(q))


checks = 0
for h in range(1, 11):
    for q in range(1, h + 1):
        for pos in combinations(range(h), q):
            C = correction_from_positions(pos)
            assert C % 3 == pow(2, pos[-1], 3)
            assert C % 3 in {1, 2}

            # Construct representative integer checkpoint solutions modulo 3.
            # Only the mod-3 identity matters: 2^h Z == C mod3.
            Z3 = (pow(pow(2, h, 3), -1, 3) * (C % 3)) % 3
            assert Z3 in {1, 2}
            checks += 1

assert checks == (2 ** 11 - 2 - 10)  # sum_{h=1}^{10}(2^h-1)

# Current synchronized right-H observation: z_H=2^S Z-C(H*) mod3.
S = 630_138_897
A0 = 630_138_896
assert S % 2 == 1
assert A0 % 2 == 0
assert pow(2, S, 3) == 2
assert pow(2, A0, 3) == 1

for Z3 in (1, 2):
    zH3 = (2 * Z3 - 1) % 3
    assert zH3 in {0, 1}

print("PASS A0 s=1 terminal dominance gate redundancy certificate")
print("finite_word_guards", checks)
print("genuine_checkpoint_Z_mod3", [1, 2])
print("terminal_dominance_accepted_zH_mod3", [0, 1])
print(
    "exact_conclusion",
    "every genuine q>=1 checkpoint automatically satisfies the terminal-28 dominance-only right-H acceptance condition",
)
print(
    "audit_status",
    "dominance-only terminal ternary gate is REDUNDANT for pruning; stronger source/control or defect predicates are required",
)
