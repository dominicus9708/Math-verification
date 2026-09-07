#!/usr/bin/env python3
"""DSD-native pilot for the exact 61+11 Collatz address transducer.

This certificate does not replace exact arithmetic with DSD terminology.
It attaches resolution/stage/exclusion/margin metadata to the exact finite
transducer and installs a gate against applying the address lift twice.
"""

from collections import Counter
from dataclasses import dataclass
from enum import Enum

ROOT_BITS = 61
TAIL_BITS = 11
MOD = 1 << TAIL_BITS
BLOCK_LABELS = range(1024, 1364)  # exact current 340-block window


class PhaseStage(str, Enum):
    BASE_ENDPOINT = "BASE_ENDPOINT"
    ADDRESS_LIFTED = "ADDRESS_LIFTED"


@dataclass(frozen=True)
class PhaseDescriptor:
    residue: int
    stage: PhaseStage


@dataclass(frozen=True)
class DSDTailState:
    # Exact arithmetic state
    q61: int
    lifted_phase: int
    first_fail_depth: int | None
    minimum_coefficient_margin: int
    survives_to_72: bool

    # DSD audit tuple carried by the calculation itself
    D: str
    R: str
    S: str
    E: str
    T: str
    C: str
    N: str
    O: str


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


MIN_Q = {k: min_q_survival(k) for k in range(ROOT_BITS + 1, ROOT_BITS + TAIL_BITS + 1)}


def parity_word_11(n: int):
    """The first 11 shortcut parity bits depend only on n mod 2^11."""
    x = n
    out = []
    for _ in range(TAIL_BITS):
        b = x & 1
        out.append(b)
        x = (3 * x + 1) // 2 if b else x // 2
    return tuple(out)


WORDS = [parity_word_11(r) for r in range(MOD)]
assert len(set(WORDS)) == MOD


def lift_address_phase(base_phase: PhaseDescriptor, q61: int, address: int) -> PhaseDescriptor:
    """Apply y -> y + a*3^q mod 2^11 exactly once.

    The stage check is a DSD transition gate.  It prevents the same address
    information from being silently imported twice under two names.
    """
    if base_phase.stage is not PhaseStage.BASE_ENDPOINT:
        raise ValueError(
            "DSD transition gate: address lift requires BASE_ENDPOINT; "
            "double application is prohibited"
        )
    multiplier = pow(3, q61, MOD)
    return PhaseDescriptor(
        (base_phase.residue + address * multiplier) & (MOD - 1),
        PhaseStage.ADDRESS_LIFTED,
    )


def describe_lifted_tail(q61: int, lifted_phase: PhaseDescriptor) -> DSDTailState:
    if lifted_phase.stage is not PhaseStage.ADDRESS_LIFTED:
        raise ValueError("DSD resolution gate: tail evaluation requires ADDRESS_LIFTED phase")

    q = q61
    first_fail = None
    margins = []
    for j, b in enumerate(WORDS[lifted_phase.residue], start=1):
        q += b
        depth = ROOT_BITS + j
        margin = q - MIN_Q[depth]
        margins.append(margin)
        if first_fail is None and margin < 0:
            first_fail = depth

    survives = first_fail is None
    minimum_margin = min(margins)

    return DSDTailState(
        q61=q61,
        lifted_phase=lifted_phase.residue,
        first_fail_depth=first_fail,
        minimum_coefficient_margin=minimum_margin,
        survives_to_72=survives,
        D="exact phase/parity descriptor",
        R="61 root bits + 11 tail bits",
        S="coefficient-survival prefix selected" if survives else "not selected",
        E="none" if survives else f"first failure at depth {first_fail}",
        T="single affine address lift verified",
        C="same-integer address stage preserved",
        N="ESTABLISHED_WITHIN_SCOPE",
        O="SURVIVE" if survives else "EXCLUDED",
    )


def residue_profiles(q61: int):
    """DSD profile for every lifted residue r mod 2048."""
    profiles = []
    for r in range(MOD):
        profiles.append(
            describe_lifted_tail(
                q61,
                PhaseDescriptor(r, PhaseStage.ADDRESS_LIFTED),
            )
        )
    return profiles


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

# New DSD-native diagnostic: exact first exclusion depth of the 2048 lifted
# residues.  These are residue counts, not probabilities or density claims.
EXPECTED_FIRST_FAIL = {
    39: {62: 1024, 64: 256, 65: 256, 67: 96, 69: 56, 70: 76, 72: 37},
    40: {64: 256, 65: 384, 67: 192, 69: 128, 70: 188, 72: 99},
    41: {65: 128, 67: 128, 69: 112, 70: 192, 72: 117},
    42: {67: 32, 69: 48, 70: 108, 72: 83},
    43: {69: 8, 70: 32, 72: 36},
    44: {70: 4, 72: 9},
    45: {72: 1},
}

# For surviving lifted residues, record the minimum coefficient margin attained
# over depths 62..72.  Again these are exact finite residue counts.
EXPECTED_SURVIVOR_MARGIN = {
    39: {0: 247},
    40: {0: 554, 1: 247},
    41: {0: 570, 1: 554, 2: 247},
    42: {0: 406, 1: 570, 2: 554, 3: 247},
    43: {0: 195, 1: 406, 2: 570, 3: 554, 4: 247},
    44: {0: 63, 1: 195, 2: 406, 3: 570, 4: 554, 5: 247},
    45: {0: 12, 1: 63, 2: 195, 3: 406, 4: 570, 5: 554, 6: 247},
}


def regression_math006_and_dsd_diagnostics():
    rows = []
    diagnostic_rows = []

    for q61 in range(39, 62):
        profiles = residue_profiles(q61)
        multiplier = pow(3, q61, MOD)

        counts = []
        for y in range(MOD):
            base = PhaseDescriptor(y, PhaseStage.BASE_ENDPOINT)
            c = 0
            for a in BLOCK_LABELS:
                lifted = lift_address_phase(base, q61, a)
                c += int(profiles[lifted.residue].survives_to_72)
            counts.append(c)

        mn, mx = min(counts), max(counts)
        assert (mn, mx) == EXPECTED_MINMAX[q61]
        rows.append((q61, multiplier, mn, mx))

        if q61 <= 45:
            fail = Counter(
                p.first_fail_depth for p in profiles if not p.survives_to_72
            )
            margins = Counter(
                p.minimum_coefficient_margin for p in profiles if p.survives_to_72
            )
            assert dict(sorted(fail.items())) == EXPECTED_FIRST_FAIL[q61]
            assert dict(sorted(margins.items())) == EXPECTED_SURVIVOR_MARGIN[q61]
            diagnostic_rows.append((q61, dict(sorted(fail.items())), dict(sorted(margins.items()))))

    return rows, diagnostic_rows


def negative_control_double_address_lift():
    base = PhaseDescriptor(0, PhaseStage.BASE_ENDPOINT)
    once = lift_address_phase(base, 39, 1024)
    try:
        lift_address_phase(once, 39, 1024)
    except ValueError:
        return "PASS"
    raise AssertionError("DSD gate failed to reject a double address lift")


def main():
    assert min_q_survival(61) == 39
    rows, diagnostics = regression_math006_and_dsd_diagnostics()
    assert negative_control_double_address_lift() == "PASS"

    print("PASS")
    print("MATH-006 regression: exact min/max label counts reproduced")
    print("DSD negative control: double address lift rejected")
    print("q61 | 3^q mod 2048 | min labels | max labels")
    for row in rows:
        print(*row)

    print("DSD first-failure / survivor-margin diagnostics for q61=39..45")
    for q61, fail, margins in diagnostics:
        print(q61, "first_fail=", fail, "survivor_min_margin=", margins)

    print("semantic result:")
    print("MATH-006 already computes r=(y+a*3^q) mod 2048 from the BASE endpoint phase y.")
    print("Therefore feeding y+a*3^q back as if it were another BASE phase would double-count address information.")
    print("DSD-native stage tracking rejects that transition before numerical pruning is credited.")
    print("No new global pruning is claimed; Collatz remains OPEN.")


if __name__ == "__main__":
    main()
