#!/usr/bin/env python3
"""Exact audit for the E/O count plane and affine Collatz correction channel.

Map:
    T(n) = n/2              if n is even,
           (3n+1)/2         if n is odd.

For a length-h parity word w with q odd entries,
    T^h(n) = (3^q n + R(w)) / 2^h,
where, if d_1 < ... < d_q are the zero-based odd positions,
    R(w) = sum_i 2^d_i 3^(q-i).

This program deliberately separates four claims:

1. exact parity-word / residue reconstruction;
2. fixed-(h,q) correction extrema;
3. first-coefficient-crossing mechanical-boundary extremum;
4. a finite first-crossing exclusion check against a supplied verified bound.

All proof-critical comparisons use Python arbitrary-precision integers only.
Floating point is used nowhere in the logical tests.
"""

from __future__ import annotations

import argparse
from itertools import product


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def affine_from_word(word: tuple[int, ...]) -> tuple[int, int, int]:
    """Return (h, q, R) for a time-ordered parity word."""
    q = 0
    R = 0
    for k, bit in enumerate(word):
        if bit not in (0, 1):
            raise ValueError("parity word must contain only 0/1")
        if bit:
            R = 3 * R + (1 << k)
            q += 1
    return len(word), q, R


def canonical_start(word: tuple[int, ...]) -> int:
    """Least positive representative of the unique class modulo 2^h."""
    h, q, R = affine_from_word(word)
    if h == 0:
        return 1
    modulus = 1 << h
    inv = pow(3**q, -1, modulus)
    residue = (-R * inv) % modulus
    return residue if residue else modulus


def parity_prefix(n: int, h: int) -> tuple[int, ...]:
    out: list[int] = []
    for _ in range(h):
        out.append(n & 1)
        n = step(n)
    return tuple(out)


def iterate(n: int, h: int) -> int:
    for _ in range(h):
        n = step(n)
    return n


def is_first_coefficient_crossing(word: tuple[int, ...]) -> bool:
    """True iff coefficient is >=1 at every proper prefix and <1 at the end."""
    h = len(word)
    q = 0
    for k, bit in enumerate(word, start=1):
        q += bit
        if k < h and 3**q < (1 << k):
            return False
    return 3**q < (1 << h)


def mechanical_word(q: int) -> tuple[int, ...]:
    """First-crossing correction maximizer for a fixed positive odd count q."""
    if q < 1:
        raise ValueError("q must be positive")
    p3 = 3**q
    sigma = p3.bit_length()  # ceil(q log_2 3), exactly
    positions = [(3**i).bit_length() - 1 for i in range(q)]
    word = [0] * sigma
    for d in positions:
        word[d] = 1
    return tuple(word)


def check_word_reconstruction(max_h: int) -> int:
    checked = 0
    for h in range(max_h + 1):
        for word in product((0, 1), repeat=h):
            w = tuple(word)
            hh, q, R = affine_from_word(w)
            start = canonical_start(w)
            assert parity_prefix(start, h) == w
            lhs = iterate(start, h)
            numerator = (3**q) * start + R
            assert numerator % (1 << hh) == 0
            assert lhs == numerator // (1 << hh)
            checked += 1
    return checked


def check_fixed_cell_extrema(max_h: int) -> int:
    checked_cells = 0
    for h in range(max_h + 1):
        by_q: dict[int, list[int]] = {}
        for word in product((0, 1), repeat=h):
            _, q, R = affine_from_word(tuple(word))
            by_q.setdefault(q, []).append(R)
        for q, values in by_q.items():
            e = h - q
            if q == 0:
                expected_min = expected_max = 0
            else:
                expected_min = 3**q - 2**q
                expected_max = (1 << e) * (3**q - 2**q)
            assert min(values) == expected_min
            assert max(values) == expected_max
            checked_cells += 1
    return checked_cells


def check_first_crossing_extrema(max_q: int) -> list[tuple[int, int, int, int]]:
    """Exhaustive small-q check of the mechanical first-crossing maximizer."""
    rows: list[tuple[int, int, int, int]] = []
    for q in range(1, max_q + 1):
        mw = mechanical_word(q)
        sigma = len(mw)
        admissible_R: list[int] = []
        for word in product((0, 1), repeat=sigma):
            if sum(word) != q:
                continue
            w = tuple(word)
            if is_first_coefficient_crossing(w):
                admissible_R.append(affine_from_word(w)[2])
        assert admissible_R, (q, sigma)
        mechanical_R = affine_from_word(mw)[2]
        assert is_first_coefficient_crossing(mw)
        assert mechanical_R == max(admissible_R)
        rows.append((q, sigma, len(admissible_R), mechanical_R))
    return rows


def scan_mechanical_first_crossings(
    sigma_limit: int,
    verified_bound: int,
) -> tuple[int, int, int, int, int, int]:
    """Exact finite scan of maximal first-crossing corrections.

    Returns
        (count, best_sigma, best_q, best_R, best_D, failures).

    The ratio best_R/best_D is the largest paradoxical-start upper bound
    encountered.  This does NOT compute the minimal-survivor function mu(k)
    and does NOT enumerate all coefficient-surviving words.
    """
    if sigma_limit < 2:
        return (0, 0, 0, 0, 1, 0)

    q = 1
    p3 = 3                 # 3^q
    R = 1                  # mechanical R*(1)
    count = 0
    failures = 0
    best_sigma = 0
    best_q = 0
    best_R = 0
    best_D = 1

    while True:
        sigma = p3.bit_length()
        if sigma > sigma_limit:
            break

        D = (1 << sigma) - p3
        assert D > 0
        count += 1

        if R >= verified_bound * D:
            failures += 1

        if best_sigma == 0 or R * best_D > best_R * D:
            best_sigma = sigma
            best_q = q
            best_R = R
            best_D = D

        # Advance q -> q+1.  The new rightmost admissible odd position is
        # floor(q log_2 3) = bit_length(3^q)-1, evaluated exactly.
        d_q = p3.bit_length() - 1
        R = 3 * R + (1 << d_q)
        p3 *= 3
        q += 1

    return count, best_sigma, best_q, best_R, best_D, failures


def decimal_ratio(num: int, den: int, digits: int = 16) -> str:
    """Integer-only decimal rendering of a positive rational."""
    whole, rem = divmod(num, den)
    out = [str(whole)]
    if digits:
        out.append(".")
        for _ in range(digits):
            rem *= 10
            digit, rem = divmod(rem, den)
            out.append(str(digit))
    return "".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-word-h", type=int, default=12,
                    help="exhaustive parity/residue and fixed-cell audit depth")
    ap.add_argument("--max-first-q", type=int, default=8,
                    help="exhaustive first-crossing mechanical audit odd count")
    ap.add_argument("--crossing-limit", type=int, default=20_000,
                    help="finite mechanical first-crossing sigma limit")
    ap.add_argument("--verified-bits", type=int, default=71,
                    help="use verified lower bound 2^B for minimal counterexamples")
    args = ap.parse_args()

    if args.max_word_h < 0 or args.max_first_q < 1:
        raise SystemExit("invalid audit limits")

    word_count = check_word_reconstruction(args.max_word_h)
    cell_count = check_fixed_cell_extrema(args.max_word_h)
    rows = check_first_crossing_extrema(args.max_first_q)

    verified_bound = 1 << args.verified_bits
    scan = scan_mechanical_first_crossings(args.crossing_limit, verified_bound)
    count, best_sigma, best_q, best_R, best_D, failures = scan

    print("E/O affine-matrix audit: PASS")
    print(f"parity/residue words checked: {word_count}")
    print(f"fixed (h,q) cells checked: {cell_count}")
    print("small first-crossing extrema: q,sigma,count,maxR")
    for row in rows:
        print(",".join(map(str, row)))
    print(f"mechanical first crossings scanned: {count}")
    print(f"sigma limit: {args.crossing_limit}")
    print(f"verified bound: 2^{args.verified_bits}")
    print(f"bound failures: {failures}")
    if best_sigma:
        print(f"largest R/D at sigma={best_sigma}, q={best_q}")
        print(f"R/D ~= {decimal_ratio(best_R, best_D, 16)}")

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
