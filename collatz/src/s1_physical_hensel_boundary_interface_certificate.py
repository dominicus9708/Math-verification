#!/usr/bin/env python3
from fractions import Fraction

A0 = 114208327604
Q0 = 72057431991
J0 = 10439860591
R0 = 6586818670
U = 9809721694
P = 6189245291

t0 = 10 * J0
j0 = 10 * R0 + 1


def mech_pos1(j: int) -> int:
    """Exact rational first-resonance mechanical odd position, 1-based."""
    return ((j - 1) * A0) // Q0 + 1


# Exact tenth-J0 / upper-tail bookkeeping.
assert A0 - 10 * J0 == U
assert Q0 - 10 * R0 == P
assert Q0 - j0 == P - 1
assert mech_pos1(j0) == t0
assert mech_pos1(j0 + 1) == t0 + 2

# In the s=1 no-cross-checkpoint sector,
# tau_{j0+1}=n_{j0+1}-d_{j0+1}>t0.
# Since n_{j0+1}=t0+2, the interface displacement is exactly 0 or 1.
interface_d = [d for d in range(10) if mech_pos1(j0 + 1) - d > t0]
assert interface_d == [0, 1]


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


# Regression only: verify the physical Hensel boundary orientation on many
# small genuine accelerated-Collatz trajectories.  The proof is the affine
# identity recorded in the companion note.
trajectory_tests = 0
for N in range(1, 300):
    for A in range(1, 18):
        x = N
        odd_positions = []
        for a in range(A):
            if x & 1:
                odd_positions.append(a)
            x = T(x)
        Y = x
        q = len(odd_positions)

        R = 0
        for j, a in enumerate(odd_positions, start=1):
            R += 3 ** (q - j) * 2**a
        assert 2**A * Y == 3**q * N + R

        # Right-to-left normalized zero-target Hensel carry.
        K = Fraction(-Y, 1)
        for a in reversed(odd_positions):
            K = (K + Fraction(2**a, 2**A)) / 3
        assert K == -Fraction(N, 2**A)
        trajectory_tests += 1


# First-global-resonance endpoint band used by the independent terminal
# boundary theorem.
LOW = 1 << 71
UPPER_TIMES_3 = 4 * LOW + 3 * (1 << 33)
YMAX = (UPPER_TIMES_3 - 1) // 3


def ym_mech_mod(m: int) -> int:
    """Mechanical terminal endpoint residue modulo 3^m."""
    M = 3**m
    inv2 = pow(2, -1, M)
    invA = pow(inv2, A0, M)
    total = 0
    for t in range(m):
        j = Q0 - m + 1 + t
        B = ((j - 1) * A0) // Q0
        total = (total + pow(3, m - 1 - t, M) * pow(2, B, M)) % M
    return (invA * total) % M


def allowed_endpoint_with_residue(r: int, m: int):
    """Return one allowed y congruent to r mod 3^m and 3 mod 4, if any."""
    M = 3**m
    lo = LOW + 1
    hi = YMAX
    kmin = (lo - r + M - 1) // M
    kmax = (hi - r) // M
    if kmin > kmax:
        return None
    # r+kM == 3 (mod 4); M is odd and hence invertible mod 4.
    target = ((3 - r) * pow(M, -1, 4)) % 4
    k = kmin + (target - kmin) % 4
    if k > kmax:
        return None
    return r + k * M


r44 = ym_mech_mod(44)
r45 = ym_mech_mod(45)
r46 = ym_mech_mod(46)
y44 = allowed_endpoint_with_residue(r44, 44)

# Exact terminal zero-cost-cylinder audit.
assert r44 == 760020657836519755297
assert y44 == 2729562462203742221059
assert r45 == 1744791560020130988178
assert allowed_endpoint_with_residue(r45, 45) is None
assert r46 == 4699104266570964686821
assert r46 > YMAX

print("PASS s=1 physical Hensel boundary interface certificate")
print("trajectory boundary regressions =", trajectory_tests)
print("checkpoint j0,t0 =", j0, t0)
print("tail odd count =", Q0 - j0, "= P-1")
print("s=1 interface displacement p in", interface_d)
print("depth44 mechanical residue compatible endpoint =", y44)
print("depth45 mechanical residue has no allowed endpoint")
print("depth46 mechanical endpoint =", r46)
print("allowed endpoint max =", YMAX)
