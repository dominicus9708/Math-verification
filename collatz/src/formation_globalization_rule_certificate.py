#!/usr/bin/env python3
"""Finite/exact checks supporting the globalization-rule extraction note.

This is not a Collatz proof.  It verifies finite algebraic diagnostics behind
several structural lemmas:

* zero-carry reachable formation targets satisfy the sharp 3^(k-1) bound for
  the checked ranks;
* the proportional formation-path entropy threshold is below the
  coefficient-survival q/k ratio;
* E=19..21 k=9 overlap factors at K=15,18,21 are close to the uniform
  formation target densities;
* the existing m=44 mass-transport checkpoints have positive exclusion credit.

The proofs of the general statements are written in
collatz/notes/2026-08-18-globalization-rule-extraction-from-E13-E21.md.
"""

from __future__ import annotations

from math import comb, log, log2


def v2(x: int) -> int:
    assert x > 0
    return (x & -x).bit_length() - 1


def zero_reachable_states(k: int) -> set[tuple[int, int]]:
    """Reverse closure from all zero-carry ranks <=k.

    State is (rank, carry).  Reverse of
        c2 = 2(c + 2^a - 2^a2)/3
    is
        c = 3*c2/2 - (2^a - 2^a2),
    so c2 must be even.  Rank can only increase in reverse.
    """
    all_states = {(a, 0) for a in range(k + 1)}
    frontier = set(all_states)
    while frontier:
        nxt: set[tuple[int, int]] = set()
        for a2, c2 in frontier:
            if c2 & 1:
                continue
            half = 3 * c2 // 2
            for a in range(a2, k + 1):
                c = half - ((1 << a) - (1 << a2))
                state = (a, c)
                if state not in all_states:
                    nxt.add(state)
        all_states |= nxt
        frontier = nxt
    return all_states


def verify_zero_attractor(max_k: int = 12) -> None:
    for k in range(1, max_k + 1):
        states = zero_reachable_states(k)
        positive_targets = []
        for a, c in states:
            x = -c
            if x <= 0:
                continue
            t = v2(x)
            assert t <= a - 1
            assert x <= (1 << t) * 3 ** (a - t - 1)
            if a == k:
                positive_targets.append(x)
        assert max(positive_targets) == 3 ** (k - 1)
        print(
            "zero-attractor",
            "k", k,
            "states", len(states),
            "rank-k-targets", len(set(positive_targets)),
            "max", max(positive_targets),
        )


def entropy_constants() -> None:
    alpha = log(2.0, 3.0)
    beta = 1.0 - alpha

    def h2(p: float) -> float:
        return -p * log2(p) - (1.0 - p) * log2(1.0 - p)

    delta = 1.0 - h2(beta)

    # Bisection for the proportional path-density threshold
    # (c+1)ln(c+1)-c ln c-c ln3 = 0.
    lo, hi = 1.0, 2.0
    for _ in range(100):
        c = (lo + hi) / 2
        f = (c + 1) * log(c + 1) - c * log(c) - c * log(3)
        if f > 0:
            lo = c
        else:
            hi = c
    cstar = (lo + hi) / 2
    ratio = alpha / beta

    assert cstar < ratio
    assert delta > 0
    print("alpha_log3_2", alpha)
    print("beta_even_fraction", beta)
    print("formation_entropy_gap_bits_per_H", delta)
    print("proportional_threshold_cstar", cstar)
    print("coefficient_boundary_q_over_k", ratio)


# Exact k=9 target-set sizes from r1_k9_ternary_filter_generator.cpp.
ALLOWED = {
    15: 646_146,
    18: 2_735_501,
    21: 9_229_199,
}

# Exact full k=9 numeric/survivor counts from the E=19--21 certificates.
K9 = {
    19: {0: 56_991_783, 15: 2_567_037, 18: 402_737, 21: 50_445},
    20: {0: 123_546_096, 15: 5_560_638, 18: 871_631, 21: 109_482},
    21: {0: 454_352_631, 15: 20_450_694, 18: 3_205_155, 21: 400_696},
}


def verify_overlap_calibration() -> None:
    for E, d in K9.items():
        N = d[0]
        row = []
        for K in (15, 18, 21):
            tau = ALLOWED[K] / 3**K
            xi = (d[K] / N) / tau
            row.append((K, xi, log2(xi)))
        print("overlap", "E", E, row)


# Existing m44_full_mass_transport_certificate.cpp checkpoints.
MASS = (
    (3,  17_592_186_044_416, 8_796_093_022_208, 4_194_304),
    (4,  13_194_139_533_312, 8_796_095_119_360, 2_048),
    (6,   8_796_091_972_608, 3_298_534_882_832, 40),
    (7,   7_146_824_531_190, 3_848_290_434_574, 56),
    (9,   5_222_679_313_909, 1_649_267_244_880, 8_907),
    (11,  4_398_045_691_348, 1_030_791_994_834, 693_772),
    (12,  3_882_649_683_210, 1_460_288_668_299, 494_762),
    (14,  3_152_505_354_815, 743_029_190_277, 3_580_205),
    (15,  2_780_990_752_541, 1_022_202_010_104, 6_650_859),
    (17,  2_269_889_787_451, 515_932_831_671, 18_318_991),
    (19,  2_011_923_507_477, 355_945_413_895, 76_621_889),
    (20,  1_833_950_905_184, 539_891_337_183, 52_632_776),
    (22,  1_564_005_133_050, 295_899_305_006, 117_886_560),
    (23,  1_416_055_503_075, 428_095_694_704, 244_836_127),
    (25,  1_202_007_610_492, 228_484_933_625, 440_762_934),
)


def verify_mass_transport_credit() -> None:
    minimum = None
    for L, C, D, U in MASS:
        assert 0 <= U < D
        gamma = (D - U) / (2 * C)
        assert gamma > 0
        minimum = gamma if minimum is None else min(minimum, gamma)
        print(
            "mass-credit",
            "L", L,
            "D/C", D / C,
            "U/D", U / D,
            "gamma", gamma,
        )
    print("minimum_checked_gamma", minimum)


def path_bound_demo(k: int = 9) -> None:
    for K in (15, 18, 21, 30, 60):
        bound = comb(K + k, k)
        print(
            "path-bound",
            "k", k,
            "K", K,
            "paths", bound,
            "density_upper", bound / 3**K,
        )


def main() -> None:
    entropy_constants()
    verify_zero_attractor()
    path_bound_demo()
    verify_overlap_calibration()
    verify_mass_transport_credit()
    print("formation globalization structural certificate: PASS")


if __name__ == "__main__":
    main()
