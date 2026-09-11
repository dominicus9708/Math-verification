#!/usr/bin/env python3
"""
MATH-064 exact closure certificate for the r=22 multi-paid layer.

Pipeline
--------
1. Refine every paid-exit phase/address source by the next 22 exact phase
   thresholds.
2. Before any endpoint-parity enumeration, apply two exact gates:
   (a) phase-sum lower bound already exceeds lambda*H;
   (b) the allowed source-t interval is shorter than one completed-cluster
       dyadic modulus 2^h, so every completed parity cylinder is singleton.
3. Exactly seven phase/address cells survive both gates.
4. Let the baseline be the unique slack schedule in which every paid odd is
   taken at u=1.  Relative to baseline, one paid event at u>=2 costs >1/24,
   two such events cost >1/12, and one event at u>=4 costs >7/96.
   The largest baseline deficit among the seven critical cells is <7/96 and
   <1/12.  Hence every negative adjusted path has at most one elevated paid
   event and that event has u<=3.
5. Enumerate exactly those low-deviation slack words, solve their complete
   parity words as one dyadic congruence in the source lift t, and audit every
   negative ordinary target directly.

Result
------
The seven cells contain 91 low-deviation slack words.  Exactly two negative
multi-source cylinders remain, each with three ordinary sources; twelve
negative singleton cylinders also remain.  The resulting 18 ordinary targets
all descend to <=2^71 within at most seven shortcut steps.  Therefore r=22 is
closed for the first-cell minimal-counterexample calculation.

Finite exact arithmetic only.  This does not close r<=21, the first universal
cell, or the Collatz conjecture.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math058r", HERE / "2026_09_11_paid_macro_transition_certificate.py"
)
m58 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

LAMBDA = Fraction(19, 503)
R = 22
LO = 1 << 71


def refined_cells(lo, hi, q0):
    cuts = {lo, hi}
    for j in range(1, R + 1):
        t = m58.TAU[q0 + j]
        if lo < t < hi:
            cuts.add(t)
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def phase_data(q0, lo, hi):
    mid = (lo + hi) / 2
    g = m58.phase_multiplier(q0, mid)
    eps = []
    gs = []
    for _ in range(R):
        gs.append(g)
        e = 0 if g * mid > Fraction(3, 4) else 1
        eps.append(e)
        g *= Fraction(2, 3) if e == 0 else Fraction(4, 3)
    return eps, gs


def slack_words(eps):
    """All cluster words with <=1 paid event above u=1 and max paid slack <=3."""
    out = []
    stack = [(0, 1, (), (), 0)]  # paid index, u, parity word, u-history, elevated count
    while stack:
        j, u, bits, uhist, elevated = stack.pop()
        if u == 0:
            if j == R:
                out.append((bits, uhist))
            continue

        # The opening cluster step is the paid odd; no leading even is allowed.
        if j > 0:
            stack.append((j, u - 1, bits + (0,), uhist, elevated))

        if j < R:
            elevated2 = elevated + (1 if u > 1 else 0)
            if elevated2 <= 1 and u <= 3:
                stack.append((
                    j + 1,
                    u + eps[j],
                    bits + (1,),
                    uhist + (u,),
                    elevated2,
                ))
    return out


def residue_for_word(E0, q0, bits):
    """Solve the complete endpoint-parity word as t=res mod 2^len(bits)."""
    t_res = 0
    mod = 1
    y_res = E0
    coeff = 3**q0
    for parity in bits:
        r = (parity - y_res) & 1
        t_res += mod * r
        mod *= 2
        y0 = y_res + coeff * r
        if parity == 0:
            y_res = y0 // 2
        else:
            y_res = (3 * y0 + 1) // 2
            coeff *= 3
    return t_res, mod, y_res, coeff


def count_class(tmin, tmax, res, mod):
    first = tmin + ((res - tmin) % mod)
    if first > tmax:
        return 0, None, None
    last = first + ((tmax - first) // mod) * mod
    return (last - first) // mod + 1, first, last


def beta_from_history(uhist, gs):
    beta = Fraction(0)
    for j, u in enumerate(uhist):
        beta += (1 - Fraction(1, 2**u)) * gs[j] / 3
    return beta


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descend_to_floor(n, cap=100):
    for k in range(cap + 1):
        if n <= LO:
            return True, k, n
        n = shortcut(n)
    return False, cap, n


def main():
    total_cells = 0
    safe_cells = 0
    singleton_only_cells = 0
    critical = []

    for L in range(1, 73):
        for lo0, hi0, start_R, E0, q0 in m58.paid_exit_sources(L):
            for lo, hi in refined_cells(lo0, hi0, q0):
                total_cells += 1
                tmin, tmax = m58.lift_bounds(L, start_R, lo, hi)
                assert tmin <= tmax

                eps, gs = phase_data(q0, lo, hi)
                cluster_steps = R + 1 + sum(eps)
                H = L + cluster_steps
                baseline_beta = sum(gs, Fraction(0)) / 6
                baseline_margin = baseline_beta * lo - LAMBDA * H

                if baseline_margin >= 0:
                    safe_cells += 1
                    continue

                # Every completed parity word has one residue modulo 2^cluster_steps.
                # If the whole allowed t-window is shorter than that modulus, every
                # completed cylinder is singleton before endpoint parity is examined.
                if tmax - tmin < (1 << cluster_steps):
                    singleton_only_cells += 1
                    continue

                critical.append((
                    L, start_R, E0, q0, lo, hi, tmin, tmax,
                    eps, gs, cluster_steps, H, baseline_margin,
                ))

    assert total_cells == 1192
    assert safe_cells == 433
    assert singleton_only_cells == 752
    assert len(critical) == 7

    max_deficit = max(-c[-1] for c in critical)
    assert max_deficit < Fraction(1, 12)
    assert max_deficit < Fraction(7, 96)

    # Relative to u=1 baseline:
    # u=2 adds Omega/12 > 1/24;
    # two elevated events add >1/12;
    # u>=4 adds at least 7 Omega/48 >7/96.
    # Therefore every negative path in the seven cells is represented below:
    # at most one elevated paid event, and its slack is at most 3.

    low_deviation_words = 0
    negative_multi = []
    negative_single = []
    safe_low_deviation = 0

    for cell_index, c in enumerate(critical):
        (L, start_R, E0, q0, lo, hi, tmin, tmax,
         eps, gs, cluster_steps, H, baseline_margin) = c

        words = slack_words(eps)
        assert len(words) == 13
        low_deviation_words += len(words)

        for bits, uhist in words:
            assert len(bits) == cluster_steps
            res, mod, y_res, target_step = residue_for_word(E0, q0, bits)
            assert mod == 1 << cluster_steps
            assert target_step == 3 ** (q0 + R)

            count, first, last = count_class(tmin, tmax, res, mod)
            if count == 0:
                continue

            beta = beta_from_history(uhist, gs)
            margin = beta * lo - LAMBDA * H
            if margin >= 0:
                safe_low_deviation += 1
                continue

            source0 = start_R + (1 << L) * first
            target0 = y_res + target_step * ((first - res) // mod)
            item = (
                cell_index, count, source0, target0, target_step,
                H, margin, uhist,
            )
            if count == 1:
                negative_single.append(item)
            else:
                negative_multi.append(item)

    assert low_deviation_words == 91
    assert safe_low_deviation == 77
    assert len(negative_multi) == 2
    assert len(negative_single) == 12
    assert [x[1] for x in negative_multi] == [3, 3]

    # The only negative multi-source words are the u=1 baseline words in the
    # first two critical cells.
    assert all(all(u == 1 for u in x[7]) for x in negative_multi)

    checked_targets = 0
    max_descent_steps = 0

    for item in negative_single + negative_multi:
        _, count, source0, target0, target_step, H, margin, uhist = item
        for j in range(count):
            source = source0 + (1 << H) * j
            target = target0 + target_step * j
            ok, steps, end = descend_to_floor(target)
            assert ok, (source, target, steps, end)
            checked_targets += 1
            max_descent_steps = max(max_descent_steps, steps)

    # 12 singleton targets + 2*3 targets from the two multi-source cylinders.
    assert checked_targets == 18
    assert max_descent_steps == 7

    print("r22_phase_cells", total_cells)
    print("r22_phase_safe_cells", safe_cells)
    print("r22_singleton_only_cells", singleton_only_cells)
    print("r22_endpoint_critical_cells", len(critical))
    print("r22_low_deviation_words", low_deviation_words)
    print("r22_negative_multi_source_cylinders", len(negative_multi))
    print("r22_negative_singleton_cylinders", len(negative_single))
    print("r22_exact_targets_checked", checked_targets)
    print("r22_max_descent_steps", max_descent_steps)
    print("PASS MATH-064 exact r=22 closure certificate")


if __name__ == "__main__":
    main()
