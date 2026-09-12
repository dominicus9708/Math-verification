#!/usr/bin/env python3
"""MATH-090: carry-valuation form of exact dyadic terminal compatibility.

Solve

    3^Q s == D (mod 2^h),   D=A-B.

For a source family 0<=s<M let R=ceil(log2 M).  When h>R, first solve the
low-R-bit congruence

    r_R = D * (3^Q)^(-1) mod 2^R.

Define the integer carry

    C_R = (D - 3^Q r_R) / 2^R.

The unique h-bit solution remains equal to the low-bit value r_R exactly when
all h-R Hensel lift bits are zero.  This is equivalent to

    nu_2(C_R) >= h-R.

Hence exact compatibility for h>R is equivalent to

    r_R < M  and  nu_2(C_R) >= h-R.

This certificate exhaustively regresses the factorization on a finite
synthetic grid.  The identity itself is elementary 2-adic lifting.
"""


def ceil_log2(m: int) -> int:
    assert m >= 1
    return 0 if m == 1 else (m - 1).bit_length()


def v2_at_least(n: int, z: int) -> bool:
    if z <= 0:
        return True
    if n == 0:
        return True
    return n % (1 << z) == 0


def full_compatible(D: int, Q: int, h: int, M: int) -> bool:
    mod = 1 << h
    s = (D * pow(pow(3,Q,mod),-1,mod)) % mod
    return s < M


def carry_compatible(D: int, Q: int, h: int, M: int) -> bool:
    R = ceil_log2(M)
    if h <= R:
        return full_compatible(D,Q,h,M)
    if R == 0:
        r = 0
    else:
        modR = 1 << R
        r = (D * pow(pow(3,Q,modR),-1,modR)) % modR
    if r >= M:
        return False
    num = D - (3**Q)*r
    assert num % (1 << R) == 0
    carry = num // (1 << R)
    return v2_at_least(carry,h-R)


def main() -> None:
    for Q in range(0,9):
        for M in range(1,65):
            for h in range(1,11):
                for D in range(-128,129):
                    assert carry_compatible(D,Q,h,M) == full_compatible(D,Q,h,M)

    # Explicit lift-bit recurrence sanity check:
    # epsilon_j = C_j mod 2; when epsilon_j=0, C_{j+1}=C_j/2.
    for C in range(-256,257):
        if C % 8 == 0:
            c=C
            for _ in range(3):
                assert c % 2 == 0
                c//=2

    print("PASS MATH-090 dyadic carry-valuation compatibility")


if __name__ == '__main__':
    main()
