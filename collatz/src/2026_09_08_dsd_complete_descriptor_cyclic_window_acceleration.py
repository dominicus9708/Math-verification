#!/usr/bin/env python3
"""MATH-011: DSD complete-descriptor + cyclic-window acceleration.

Scope:
- exact finite 61+11 coefficient-survival calculation from MATH-006
- current 340 top-address labels a=1024..1363
- q61=39..61
- no claim beyond this finite transducer

The DSD step is not a replacement for arithmetic.
It identifies:
1) a complete finite descriptor H(r) for the 11-bit tail survival predicate;
2) an exact coordinate change that turns the 340-address scan into a cyclic
   sliding window.
"""

from collections import Counter
from time import perf_counter

ROOT_BITS = 61
TAIL_BITS = 11
MOD = 1 << TAIL_BITS
ADDRESS_START = 1024
ADDRESS_STOP = 1364
ADDRESS_LEN = ADDRESS_STOP - ADDRESS_START

EXPECTED_MINMAX = {
    39: (36, 47),
    40: (124, 141),
    41: (221, 235),
    42: (288, 303),
    43: (320, 333),
    44: (336, 340),
    45: (339, 340),
    **{q: (340, 340) for q in range(46, 62)},
}

EXPECTED_H_DISTRIBUTION = {
    39: 247,
    40: 554,
    41: 570,
    42: 406,
    43: 195,
    44: 63,
    45: 12,
    46: 1,
}


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


MIN_Q = {
    k: min_q_survival(k)
    for k in range(ROOT_BITS + 1, ROOT_BITS + TAIL_BITS + 1)
}


def parity_word_11(n: int):
    x = n
    out = []
    for _ in range(TAIL_BITS):
        b = x & 1
        out.append(b)
        x = (3 * x + 1) // 2 if b else x // 2
    return tuple(out)


WORDS = [parity_word_11(r) for r in range(MOD)]
assert len(set(WORDS)) == MOD


def legacy_tail_survives(bits, q61: int) -> bool:
    q = q61
    for j, b in enumerate(bits, start=1):
        q += b
        if q < MIN_Q[ROOT_BITS + j]:
            return False
    return True


def required_q_descriptor(bits) -> int:
    """Exact complete descriptor for coefficient survival through depth 72.

    Let s_j be the number of odd steps in the first j tail bits.
    The legacy predicate is:
        q61 + s_j >= q_min(61+j) for all j=1..11.
    Therefore it is equivalent to:
        q61 >= max_j(q_min(61+j)-s_j).
    """
    s = 0
    required = -10**9
    for j, b in enumerate(bits, start=1):
        s += b
        required = max(required, MIN_Q[ROOT_BITS + j] - s)
    return required


H = [required_q_descriptor(bits) for bits in WORDS]
assert dict(sorted(Counter(H).items())) == EXPECTED_H_DISTRIBUTION


def legacy_counts(q61: int):
    """Original MATH-006-style all-y/all-address scan."""
    m = pow(3, q61, MOD)
    ok = [legacy_tail_survives(WORDS[r], q61) for r in range(MOD)]
    counts = []
    for y in range(MOD):
        c = 0
        for a in range(ADDRESS_START, ADDRESS_STOP):
            r = (y + a * m) & (MOD - 1)
            c += int(ok[r])
        counts.append(c)
    return counts


def accelerated_counts(q61: int):
    """Exact DSD-compressed and cyclic-window equivalent.

    Let m=3^q mod 2048. Because m is odd, it is invertible.
    Put z=m^{-1}y and define g(t)=1[H(m t mod 2048) <= q].
    Then

      count(y)
        = sum_{a=A}^{A+L-1} 1[H(y+a m) <= q]
        = sum_{a=A}^{A+L-1} g(z+a),

    a cyclic contiguous window of length L=340.
    """
    m = pow(3, q61, MOD)
    inv = pow(m, -1, MOD)
    assert (m * inv) % MOD == 1

    g = [
        int(H[(m * t) & (MOD - 1)] <= q61)
        for t in range(MOD)
    ]

    doubled = g + g
    first = sum(doubled[ADDRESS_START:ADDRESS_START + ADDRESS_LEN])
    window = [0] * MOD
    window[0] = first

    s = first
    for z in range(1, MOD):
        s += (
            doubled[ADDRESS_START + z + ADDRESS_LEN - 1]
            - doubled[ADDRESS_START + z - 1]
        )
        window[z] = s

    counts = [0] * MOD
    for y in range(MOD):
        z = (inv * y) & (MOD - 1)
        counts[y] = window[z]
    return counts


def accelerated_minmax_only(q61: int):
    """Same theorem-facing output with no need to restore y-order.

    y -> z=m^{-1}y is a permutation, so min/max over all y equals min/max
    over all cyclic windows z.
    """
    m = pow(3, q61, MOD)
    g = [
        int(H[(m * t) & (MOD - 1)] <= q61)
        for t in range(MOD)
    ]
    doubled = g + g

    s = sum(doubled[ADDRESS_START:ADDRESS_START + ADDRESS_LEN])
    mn = mx = s
    for z in range(1, MOD):
        s += (
            doubled[ADDRESS_START + z + ADDRESS_LEN - 1]
            - doubled[ADDRESS_START + z - 1]
        )
        mn = min(mn, s)
        mx = max(mx, s)
    return mn, mx


def exact_regression():
    rows = []
    for q61 in range(39, 62):
        old = legacy_counts(q61)
        new = accelerated_counts(q61)
        assert old == new

        mnmx = (min(old), max(old))
        assert mnmx == EXPECTED_MINMAX[q61]
        assert accelerated_minmax_only(q61) == mnmx
        rows.append((q61, *mnmx))
    return rows


def deterministic_work_counts():
    q_count = 62 - 39
    legacy_address_predicate_lookups = q_count * MOD * ADDRESS_LEN
    accelerated_threshold_evaluations = q_count * MOD
    return {
        "legacy_address_predicate_lookups": legacy_address_predicate_lookups,
        "accelerated_threshold_evaluations": accelerated_threshold_evaluations,
        "predicate_lookup_reduction_factor": (
            legacy_address_predicate_lookups
            // accelerated_threshold_evaluations
        ),
        "one_time_H_tail_steps": MOD * TAIL_BITS,
    }


def optional_runtime_benchmark():
    """Environment-dependent diagnostic only; never a theorem."""
    t0 = perf_counter()
    for q61 in range(39, 62):
        legacy_counts(q61)
    legacy_s = perf_counter() - t0

    t0 = perf_counter()
    for q61 in range(39, 62):
        accelerated_minmax_only(q61)
    accelerated_s = perf_counter() - t0
    return legacy_s, accelerated_s


def main():
    assert min_q_survival(61) == 39

    rows = exact_regression()
    work = deterministic_work_counts()
    legacy_s, accelerated_s = optional_runtime_benchmark()

    print("PASS")
    print("H(r) distribution:", dict(sorted(Counter(H).items())))
    print("q61 | min surviving labels | max surviving labels")
    for row in rows:
        print(*row)

    print("deterministic work comparison:")
    for k, v in work.items():
        print(k, "=", v)

    print("runtime diagnostic only:")
    print("legacy_seconds =", legacy_s)
    print("accelerated_seconds =", accelerated_s)
    if accelerated_s > 0:
        print("observed_runtime_ratio =", legacy_s / accelerated_s)

    print("DSD verdict:")
    print("H(r) is COMPLETE_WITHIN_SCOPE for the depth-72 coefficient-survival predicate.")
    print("The cyclic-window transform is EXACT and preserves all 2048 y counts.")
    print("No new Collatz theorem or new block exclusion is claimed.")
    print("The gain is computational: fewer repeated state expansions / predicate evaluations.")
    print("Collatz remains OPEN.")


if __name__ == "__main__":
    main()
