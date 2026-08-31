#!/usr/bin/env python3
"""Finite audit of the source-Y minimality obstruction for Route-B.

For a source channel y + g n with odd g, choose the future parameter input
n == 0.  The next d parity bits are then exactly the parity word of y under T.
The standard parity-cylinder bijection says y mod 2^d -> parity word of length d
is one-to-one.  Therefore two different Y=y mod 2^d states are distinguishable
by the zero parameter input and cannot be merged by any exact quotient that
must preserve all d-step parameter-to-parity outputs.

The theorem follows from parity-cylinder uniqueness.  This file only audits
that injectivity directly for small d.
"""


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def parity_word(x: int, d: int):
    bits = []
    for _ in range(d):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits)


MAX_D = 14
word_checks = 0
injectivity_checks = 0

for d in range(1, MAX_D + 1):
    seen = {}
    for Y in range(1 << d):
        word = parity_word(Y, d)
        assert len(word) == d
        assert word not in seen
        seen[word] = Y
        word_checks += 1
    assert len(seen) == 1 << d
    injectivity_checks += 1


print("PASS A0 s=1 Route-B source-Y minimality certificate")
print("max_precision", MAX_D)
print("word_checks", word_checks)
print("injectivity_checks", injectivity_checks)
print(
    "exact_result",
    "different y mod 2^d states are distinguished by the all-zero future parameter input because their d-bit parity words differ",
)
print(
    "minimality",
    "any exact generic d-step parameter-to-parity transducer preserving all future inputs requires at least 2^d distinguishable Y classes",
)
print(
    "dsd_audit",
    "further compression must exploit restricted admissible inputs, early closure, or hierarchical/lazy observation rather than a universal Y quotient",
)
print(
    "status",
    "generic source-Y compression route CLOSED NEGATIVELY; structured Route-B-specific closure remains OPEN",
)
