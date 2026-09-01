#!/usr/bin/env python3
"""Exact backward exponential carry chart for A0 s=1 Route-B.

At remaining ternary precision m let the successor projective carry be

    z_plus mod 3^(m-1),

the target ranked-one exponent be A, and the candidate exponent be B.
The forward carry gate

    z + 2^A - 2^B = 3 z_plus   (mod 3^m)

has the exact backward chart

    Gamma_{m,z_plus,A}(B)
      = 3*z_plus - 2^A + 2^B   (mod 3^m).

Because 2 has exact multiplicative order

    lambda_m = 2*3^(m-1)

modulo 3^m, B -> Gamma(B) is injective on every integer B interval of
width < lambda_m.  The current right-H legal slack/exponent width is at most
h_R-q_R=232,565,517, so the already-certified m>=18 inequality

    h_R-q_R < lambda_m

makes every one-layer right-H backward chart injective throughout the current
high-precision range.

The chart is projectively compatible: for 1<=r<=m,

    Gamma_m(B) mod 3^r
      = 3*(z_plus mod 3^(r-1)) - 2^A + 2^B   (mod 3^r),

with the successor term interpreted modulo 1 when r=1.

For k backward one-event gates, with

    z_i = 3*z_(i+1) - 2^A_i + 2^B_i

at descending precisions, exact unrolling gives

    z_0 = 3^k z_k
          + sum_{i=0}^{k-1} 3^i (2^B_i - 2^A_i)
          (mod 3^m).

Thus the complete k-gate carry family has an exact triangular exponential
chart over the ordered legal candidate-exponent/slack domain.  This is a
symbolic representation theorem; it does NOT prove that the number of legal
vectors is small or that the whole carry path is unique.

A necessary-state audit is also exact.  If two successor carries differ modulo
3^(m-1), then for the same A and B

    Gamma_{z1}(B)-Gamma_{z2}(B)=3(z1-z2) != 0 (mod 3^m).

Therefore the successor-carry/base coordinate cannot in general be discarded.
In particular, Pi3 interval payload plus S_max alone is not a complete
multi-gate carry state unless another theorem proves that the base carry is
recoverable from the retained coordinates.

Finite checks below are regression guards only.
"""

from itertools import product

H_RIGHT = 630_138_897
Q_RIGHT = 397_573_380
CAP_MAX = H_RIGHT - Q_RIGHT


def period(m: int) -> int:
    assert m >= 1
    return 2 * (3 ** (m - 1))


def gamma(m: int, z_plus: int, A: int, B: int) -> int:
    assert m >= 1
    mod = 3 ** m
    return (3 * z_plus - (1 << A) + (1 << B)) % mod


# Current right-H high-precision injectivity range.
assert CAP_MAX == 232_565_517
assert period(17) <= CAP_MAX < period(18)
assert all(period(m) > CAP_MAX for m in range(18, 60))

# ---------------------------------------------------------------------------
# 1. One-step inversion regression.
# ---------------------------------------------------------------------------
one_step_checks = 0
for m in range(2, 6):
    mod = 3 ** m
    mod_plus = 3 ** (m - 1)
    for z_plus in range(mod_plus):
        for A in range(5):
            for B in range(5):
                z = gamma(m, z_plus, A, B)
                assert (z + (1 << A) - (1 << B) - 3 * z_plus) % mod == 0
                one_step_checks += 1

assert one_step_checks == 3_000

# ---------------------------------------------------------------------------
# 2. Injectivity on intervals shorter than lambda_m.
# ---------------------------------------------------------------------------
# Full order-period proof is algebraic.  This small check only audits the code.
injectivity_checks = 0
for m in range(2, 6):
    mod_plus = 3 ** (m - 1)
    width = min(period(m) - 1, 8)
    for z_plus in range(mod_plus):
        vals = [gamma(m, z_plus, 0, B) for B in range(width + 1)]
        assert len(vals) == len(set(vals))
        injectivity_checks += 1

assert injectivity_checks == 120

# ---------------------------------------------------------------------------
# 3. Projective compatibility regression.
# ---------------------------------------------------------------------------
projection_checks = 0
for m in range(2, 6):
    mod_plus = 3 ** (m - 1)
    for z_plus in range(mod_plus):
        for A in range(5):
            for B in range(5):
                z = gamma(m, z_plus, A, B)
                for r in range(1, m + 1):
                    mod_r = 3 ** r
                    z_plus_r = z_plus % (3 ** (r - 1)) if r > 1 else 0
                    rhs = (3 * z_plus_r - (1 << A) + (1 << B)) % mod_r
                    assert z % mod_r == rhs
                    projection_checks += 1

assert projection_checks == 13_650

# ---------------------------------------------------------------------------
# 4. k-gate triangular unrolling regression.
# ---------------------------------------------------------------------------
multigate_checks = 0
for m in range(3, 6):
    for k in range(1, m):
        terminal_mod = 3 ** (m - k)
        for z_k in range(min(terminal_mod, 5)):
            for A_vec in product(range(2), repeat=k):
                for B_vec in product(range(2), repeat=k):
                    z = z_k
                    for i in range(k - 1, -1, -1):
                        precision = m - i
                        z = (
                            3 * z
                            - (1 << A_vec[i])
                            + (1 << B_vec[i])
                        ) % (3 ** precision)

                    direct = (
                        (3 ** k) * z_k
                        + sum(
                            (3 ** i) * ((1 << B_vec[i]) - (1 << A_vec[i]))
                            for i in range(k)
                        )
                    ) % (3 ** m)
                    assert z == direct
                    multigate_checks += 1

assert multigate_checks == 1_548

# ---------------------------------------------------------------------------
# 5. Necessary-state regression: dropping z_plus is not exact.
# ---------------------------------------------------------------------------
base_carry_checks = 0
for m in range(2, 6):
    mod_plus = 3 ** (m - 1)
    A = 4
    for z1 in range(mod_plus):
        for z2 in range(z1 + 1, mod_plus):
            for B in range(4):
                assert gamma(m, z1, A, B) != gamma(m, z2, A, B)
                base_carry_checks += 1

assert base_carry_checks == 14_520

print("PASS A0 s=1 Route-B backward exponential carry-chart certificate")
print("right_length", H_RIGHT)
print("right_one_count", Q_RIGHT)
print("right_max_slack_capacity", CAP_MAX)
print("high_precision_injective_from_m", 18)
print("one_step_checks", one_step_checks)
print("injectivity_checks", injectivity_checks)
print("projection_checks", projection_checks)
print("multigate_checks", multigate_checks)
print("base_carry_checks", base_carry_checks)
print(
    "chart",
    "Gamma(B)=3*z_plus-2^A+2^B mod 3^m is the exact backward one-gate carry chart",
)
print(
    "multigate",
    "z0=3^k*zk+sum_i 3^i(2^B_i-2^A_i) mod 3^m over the ordered slack domain",
)
print(
    "rightH",
    "for m>=18 the one-layer chart is injective on every complete legal right-H slack interval",
)
print(
    "rejected_overcompression",
    "Pi3 payload and S_max without the successor-carry/base coordinate are not a complete carry state in general",
)
print(
    "dsd_audit",
    "symbolic chart representation is exact, but no bounded carry-family cardinality or unique full path is inferred",
)
print(
    "status",
    "high-precision multi-gate triangular exponential carry representation CLOSED; compact quotient of distinct chart bases and exact m=17 export remain OPEN",
)
