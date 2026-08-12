#!/usr/bin/env python3
"""Exact audit for canonical Collatz odd-event formation lift digits.

Given a finite valuation code v_0,...,v_{q-1}, this script computes:

- A_q = cumulative halving exponent;
- rho_q = least positive odd completed-event start representative mod 2^(A_q+1);
- y_q = corresponding canonical odd endpoint;
- t_q = unique lift digit in [0,2^v_q) used to extend the formation class.

The identities implemented here are those in
collatz/notes/2026-08-12-canonical-lift-digit-naturalness.md.

No floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Row:
    q: int
    v: int
    A_before: int
    rho_before: int
    y_before: int
    t: int
    A_after: int
    rho_after: int
    y_after: int


def canonical_lift_rows(vals: Iterable[int]) -> List[Row]:
    vals = list(vals)
    if any(v < 1 for v in vals):
        raise ValueError("all odd-event valuations must be positive integers")

    # q=0 completed empty code: every positive odd start is 1 mod 2.
    A = 0
    rho = 1
    y = 1
    rows: List[Row] = []

    for q, v in enumerate(vals):
        modulus = 1 << v

        # Divide the exact valuation congruence by 2:
        # (3 y + 1)/2 + 3^(q+1) t == 2^(v-1) (mod 2^v).
        half = (3 * y + 1) // 2
        inv3 = pow(3, -(q + 1), modulus)
        t = ((1 << (v - 1)) - half) * inv3 % modulus

        rho_next = rho + t * (1 << (A + 1))

        numerator = 3 * y + 1 + 2 * t * (3 ** (q + 1))
        if numerator % (1 << v) != 0:
            raise AssertionError("canonical carry numerator is not divisible by 2^v")
        y_next = numerator >> v
        if y_next <= 0 or y_next % 2 == 0:
            raise AssertionError("completed-event canonical endpoint must be positive odd")

        A_next = A + v

        # Direct affine/formation verification.
        B = 0
        A_tmp = 0
        for j in range(q + 1):
            # B_{j+1}=3 B_j + 2^{A_j}
            B = 3 * B + (1 << A_tmp)
            A_tmp += vals[j]
        direct_num = (3 ** (q + 1)) * rho_next + B
        if direct_num != (1 << A_next) * y_next:
            raise AssertionError("direct affine carry identity failed")

        # Least positive completed-event representative range.
        if not (0 < rho_next < (1 << (A_next + 1)) and rho_next % 2 == 1):
            raise AssertionError("rho is not the canonical positive odd representative")

        rows.append(
            Row(
                q=q,
                v=v,
                A_before=A,
                rho_before=rho,
                y_before=y,
                t=t,
                A_after=A_next,
                rho_after=rho_next,
                y_after=y_next,
            )
        )

        A, rho, y = A_next, rho_next, y_next

    # Binary-block reconstruction check:
    reconstructed = 1
    A_tmp = 0
    for row in rows:
        reconstructed += row.t * (1 << (A_tmp + 1))
        A_tmp += row.v
    if reconstructed != rho:
        raise AssertionError("lift-digit reconstruction failed")

    return rows


def parse_vals(text: str) -> List[int]:
    text = text.replace(",", " ")
    vals = [int(x) for x in text.split()]
    if not vals:
        raise ValueError("provide at least one valuation")
    return vals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "valuations",
        help="comma- or space-separated odd-event valuations, e.g. '1,1,2,1'",
    )
    args = parser.parse_args()

    rows = canonical_lift_rows(parse_vals(args.valuations))

    print("q v A_before rho_before y_before t A_after rho_after y_after")
    for r in rows:
        print(
            r.q,
            r.v,
            r.A_before,
            r.rho_before,
            r.y_before,
            r.t,
            r.A_after,
            r.rho_after,
            r.y_after,
        )

    last = rows[-1]
    nonzero = [r.q for r in rows if r.t != 0]
    print()
    print(f"final_A={last.A_after}")
    print(f"final_rho={last.rho_after}")
    print(f"final_y={last.y_after}")
    print(f"nonzero_lift_indices={nonzero}")


if __name__ == "__main__":
    main()
