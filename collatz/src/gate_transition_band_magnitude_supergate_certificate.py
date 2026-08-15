#!/usr/bin/env python3
"""Exact transition-band magnitude barrier for second-return gate cubes.

This extends the first-return certificate to G13/G14 neutral/one-slack cases
for all bounded predecessor credits delta=1..397.

For the enlarged section
    1^(F-h) B (01/10)^(J-h) 0,
where B is any length-3h word with 2h ones, every boundary correction
difference satisfies
    |Delta R_B| <= M_h = (2^h-1)(3^(2h)-4^h).

After the remaining J-h pair coordinates are balanced-Hensel lifted, the
required boundary difference is
    T_h(delta) = 2^(3h-2) U_(J-h) mod 3^(F+h),
using the least signed representative.  If |T_h(delta)| > M_h for every
bounded credit, repair is impossible for that width in this over-family.

The implementation uses the exact recurrence between neighboring h values to
avoid a modular exponentiation at every h.  It is first checked against the
published first-return thresholds.
"""

FIRST_RETURN_REFERENCE = (
    ("G81-neutral", 404, 567, 150),
    ("G81-one-slack", 402, 568, 150),
    ("G82-neutral", 409, 574, 151),
    ("G82-one-slack", 407, 575, 152),
)

SECOND_RETURN_CASES = (
    ("G13-neutral", 5245, 7390, 1936),
    ("G13-one-slack", 5243, 7391, 1937),
    ("G14-neutral", 5648, 7958, 2085),
    ("G14-one-slack", 5646, 7959, 2085),
)

MAX_CREDIT = 397


def boundary_range(h: int) -> int:
    return (2**h - 1) * (3**(2*h) - 4**h)


def reduce_signed_small(x: int, modulus: int) -> int:
    """Reduce to the least signed class when |x| is already <~2 modulus."""
    half = modulus // 2
    if x > half:
        x -= modulus
        if x > half:
            x -= modulus
    elif x <= -half:
        x += modulus
        if x <= -half:
            x += modulus
    return x


def scan_case(name: str, F: int, J: int, first_possible: int):
    """Return exact minima through the first width not excluded by magnitude."""
    q = F + J
    H = first_possible
    mod0 = 3**q
    scale = pow(2, 2*J + 1, mod0)
    inv4 = pow(pow(4, J - 1, mod0), -1, mod0)

    minima = [None] * (H + 1)
    args = [None] * (H + 1)
    prefix_steps = J - H

    # At h=H, A_h=2^(3h-3) is smaller than 3^(F+h) in all certified cases.
    A_H = 1 << (3*H - 3)
    B_H = 1 << (3*H - 2)
    assert A_H < 3**(F + H)

    for delta in range(1, MAX_CREDIT + 1):
        U = (-scale * delta) % mod0
        U = (U * inv4) % mod0
        if U > mod0 // 2:
            U -= mod0
        modulus = mod0

        # Advance the balanced-Hensel recurrence to h=H.
        for _ in range(prefix_steps):
            z = U % 3
            e = 0 if z == 0 else (1 if z == 1 else -1)
            U = 4 * ((U - e) // 3)
            modulus //= 3
            U = reduce_signed_small(U, modulus)

        # Initialize T_H once.
        t = (B_H * U) % modulus
        if t > modulus // 2:
            t -= modulus
        A = A_H

        # Descend h exactly.  If B_h=2^(3h-2), then
        # T_h = B_h U_h.  Since B_h=2 A_h and
        # U_(h-1)=4(U_h-e)/3,
        # T_(h-1)=A_h(U_h-e)/3.
        for h in range(H, 0, -1):
            a = abs(t)
            if minima[h] is None or a < minima[h]:
                minima[h] = a
                args[h] = (delta, t)

            if h == 1:
                break

            # Recover U_h mod 3 from T_h.  B_h == (-1)^h (mod 3).
            u_mod3 = (t % 3) if h % 2 == 0 else ((-t) % 3)
            e = 0 if u_mod3 == 0 else (1 if u_mod3 == 1 else -1)

            # Divide T_h by 2 modulo the odd modulus, then apply the recurrence.
            s = t if t % 2 == 0 else t + modulus
            aU = s // 2
            numerator = aU - A * e
            assert numerator % 3 == 0
            t = numerator // 3

            modulus //= 3
            t = reduce_signed_small(t, modulus)
            A //= 8

    for h in range(1, first_possible):
        assert minima[h] > boundary_range(h), (name, h, minima[h], boundary_range(h))

    assert minima[first_possible] <= boundary_range(first_possible), (
        name,
        first_possible,
        minima[first_possible],
        boundary_range(first_possible),
    )

    return minima, args


def certify(name: str, F: int, J: int, first_possible: int):
    minima, args = scan_case(name, F, J, first_possible)
    delta, target = args[first_possible]
    print(
        name,
        "q", F + J,
        "impossible_through", first_possible - 1,
        "first_magnitude_possible", first_possible,
        "minimizing_delta", delta,
        "target_sign", -1 if target < 0 else 1,
    )


def main():
    # Regression: these must reproduce the existing first-return certificate.
    for case in FIRST_RETURN_REFERENCE:
        certify(*case)

    print("-- second return --")
    for case in SECOND_RETURN_CASES:
        certify(*case)


if __name__ == "__main__":
    main()
