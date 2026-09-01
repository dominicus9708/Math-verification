#!/usr/bin/env python3
"""Exact lazy ternary-observation quotient for the Route-B Bellman scan.

This certificate adds the smallest exact forward ternary observation coordinate
needed by a final correction/defect residue predicate to the already-certified
source/ballot/physical-danger Bellman state.

Let J be the prescribed final one-count and let N_q be the exact integer prefix
defect numerator after q candidate one-events,

    N_q = C*_q - C(W_q) = 3^q eta_q >= 0.

If a fixed future suffix contains s=J-q further one-events, repeated use of

    bit 0: N' = N,
    bit 1: N' = 3N + d,

shows that

    N_J = 3^s N_q + A_suffix.

Hence, for a downstream predicate that only asks for N_J modulo 3^L,

* if s >= L, the current N_q is completely invisible modulo 3^L;
* if s < L, only N_q modulo 3^(L-s) can matter.

Define the exact active precision

    m(q) = max(0, L-(J-q))

and the lazy projective coordinate

    R_q = N_q mod 3^m(q),

with the convention R_q=0 when m(q)=0.

This precision is also generally minimal.  If m>0, two prefix numerators that
differ by 3^(m-1) agree modulo 3^(m-1), but after the same s=J-q future
one-events their final values differ by

    3^s 3^(m-1) = 3^(L-1),

which is nonzero modulo 3^L.

Forward transition:

* emitted 0: q'=q, m'=m, R'=R;
* emitted 1 at absolute position h and new target rank q+1, with
      d = 2^a_(q+1) - 2^h,
  then once the coordinate is active m'=m+1 and
      R' = 3R + d (mod 3^m').
  Before activation both m and m' may be zero, so R remains the trivial state.

Backward transition for a fixed emitted 1 is deterministic:

    R' == d (mod 3)

is necessary and sufficient for a predecessor at the previous precision, and
then

    R = (R'-d)/3 (mod 3^m).

Thus the final ternary condition is a projective filter, not another cost.

Bellman consequence.  Augment the exact active key from

    (source future control, exact interval payload)

to

    (source future control, exact interval payload, R_q).

For histories sharing this augmented key, every common next parameter bit gives
identical emitted parity, identical child payload, identical R transition, and
the already-certified physical danger score P evolves by the same increasing
affine map P->P+c or P->3P+c.  Therefore one minimum P label per augmented key
is exact for the combined predicate set

    source transition + strict target dominance + final ternary residue
    + directed physical-defect rejection.

Scope.  The theorem applies after a downstream condition has genuinely been
reduced to a congruence of the final defect/correction numerator modulo 3^L.
It does not by itself prove that every checkpoint/C4F/tail predicate has that
form, and it does not close any of the 14 current roots.
"""

from collections import defaultdict

import A0_s1_prefix_defect_membership_pruning_certificate as pruning

REQ = pruning.REQ
TH = pruning.TH
TPOS = pruning.TPOS

M_LO = pruning.mW_lo
DELTA_LO = pruning.delta_lo

TEST_ROOTS = (2, 5, 8, 10, 13, 16, 18)
TEST_D = 8
TEST_INTERVAL = (3, 100)
TEST_L_VALUES = (1, 2, 3, 4, 5)


def target_correction(q: int) -> int:
    return sum(3 ** (q - r - 1) * (1 << TPOS[r]) for r in range(q))


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def numerator(bits) -> int:
    return target_correction(sum(bits)) - correction(bits)


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def child_interval(L: int, U: int, epsilon: int):
    lo = ceil_div(L - epsilon, 2)
    hi = (U - epsilon) // 2
    return None if lo > hi else (lo, hi)


def refine_channel(state, bit: int):
    h, r, y, q = state
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        y2 = (y + (3 ** q) * m0) // 2
        q2 = q
    else:
        y2 = (3 * y + (3 ** (q + 1)) * m0 + 1) // 2
        q2 = q + 1
    return h + 1, r2, y2, q2


def build_channel(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def control_step(Y: int, q: int, d: int, epsilon: int):
    G = pow(3, q, 1 << d)
    bit = (Y + epsilon) & 1
    if bit == 0:
        numer = Y + G * epsilon
    else:
        numer = 3 * (Y + G * epsilon) + 1
    assert numer % 2 == 0
    Y2 = 0 if d == 1 else (numer // 2) % (1 << (d - 1))
    return Y2, q + bit, bit


def precision(q: int, J: int, Lobs: int) -> int:
    assert 0 <= q <= J
    assert Lobs >= 1
    return max(0, Lobs - (J - q))


def lazy_residue(N: int, q: int, J: int, Lobs: int) -> int:
    m = precision(q, J, Lobs)
    return 0 if m == 0 else N % (3 ** m)


def numerator_step(N: int, h: int, q2: int, bit: int) -> int:
    if bit == 0:
        return N
    a = TPOS[q2 - 1]
    assert h <= a
    return 3 * N + (1 << a) - (1 << h)


def lazy_residue_step(R: int, q: int, h: int, q2: int, bit: int, J: int, Lobs: int) -> int:
    m = precision(q, J, Lobs)
    m2 = precision(q2, J, Lobs)

    if bit == 0:
        assert q2 == q and m2 == m
        return R

    assert q2 == q + 1
    if m2 == 0:
        assert m == 0
        return 0

    # Once activation begins, one new ternary digit becomes relevant at every
    # one-event.
    assert m2 == m + 1
    a = TPOS[q2 - 1]
    assert h <= a
    atom = (1 << a) - (1 << h)
    return (3 * R + atom) % (3 ** m2)


def backward_one_predecessor(R2: int, m2: int, atom: int):
    """Return unique predecessor residue for a fixed one-event, or None."""
    assert m2 >= 1
    modulus = 3 ** m2
    R2 %= modulus
    if (R2 - atom) % 3:
        return None
    m = m2 - 1
    if m == 0:
        return 0
    return ((R2 - atom) // 3) % (3 ** m)


def score(r: int, N: int, h: int, q: int, Lparam: int) -> int:
    X_lo = r + (1 << h) * Lparam
    return M_LO * N + DELTA_LO * (3 ** q) * X_lo


# ---------------------------------------------------------------------------
# 1. Algebraic sufficiency and minimality of m(q)=max(0,L-(J-q)).
# ---------------------------------------------------------------------------

sufficiency_checks = 0
minimality_checks = 0

for Lobs in range(1, 8):
    for J in range(Lobs, Lobs + 8):
        for q in range(J + 1):
            s = J - q
            m = precision(q, J, Lobs)

            # Equal current residues at the claimed precision stay equal in the
            # final modulus after multiplication by 3^s, regardless of suffix
            # additive term.
            modulus_now = 1 if m == 0 else 3 ** m
            for base in range(7):
                N1 = base
                N2 = base + modulus_now
                assert (3 ** s * (N2 - N1)) % (3 ** Lobs) == 0
                sufficiency_checks += 1

            if m > 0:
                # One fewer ternary digit is insufficient in general.
                delta = 3 ** (m - 1)
                assert (3 ** s * delta) % (3 ** Lobs) == 3 ** (Lobs - 1)
                minimality_checks += 1


# ---------------------------------------------------------------------------
# 2. Exact forward/backward one-event projective transition.
# ---------------------------------------------------------------------------

transition_checks = 0
backward_checks = 0

for m in range(0, 6):
    m2 = m + 1
    mod1 = 1 if m == 0 else 3 ** m
    mod2 = 3 ** m2
    for atom in range(25):
        for R in range(mod1):
            R2 = (3 * R + atom) % mod2
            got = backward_one_predecessor(R2, m2, atom)
            assert got == (0 if m == 0 else R)
            transition_checks += 1
            backward_checks += 1

        # Every incompatible least ternary digit has no predecessor.
        for R2 in range(mod2):
            got = backward_one_predecessor(R2, m2, atom)
            if (R2 - atom) % 3:
                assert got is None
                backward_checks += 1


# ---------------------------------------------------------------------------
# 3. Bellman regression with source control, interval payload and danger score.
# ---------------------------------------------------------------------------

layer_checks = 0
merge_events = 0
final_residue_checks = 0

for first in TEST_ROOTS:
    assert TH[first] == 0
    prefix = TH[:first] + (1,)
    h0, r0, y0, q0 = build_channel(prefix)
    N0 = numerator(prefix)
    H = h0 + TEST_D
    J = REQ[H]
    assert q0 <= J

    for Lobs in TEST_L_VALUES:
        if Lobs > J:
            continue

        L0, U0 = TEST_INTERVAL

        # Direct representation: key without ternary quotient -> raw histories.
        raw = {
            (y0 % (1 << TEST_D), q0, L0, U0): [(r0, N0)]
        }

        # Quotient representation: augmented exact key -> minimum danger score.
        quotient = {
            (
                y0 % (1 << TEST_D),
                q0,
                L0,
                U0,
                lazy_residue(N0, q0, J, Lobs),
            ): score(r0, N0, h0, q0, L0)
        }

        for i in range(TEST_D):
            d = TEST_D - i
            h = h0 + i
            raw_next = defaultdict(list)
            quotient_next = {}

            for (Y, q, Lparam, Uparam), histories in raw.items():
                for epsilon in (0, 1):
                    child = child_interval(Lparam, Uparam, epsilon)
                    if child is None:
                        continue

                    Y2, q2, bit = control_step(Y, q, d, epsilon)
                    if q2 < REQ[h + 1] or q2 > J:
                        continue

                    for r, N in histories:
                        r2 = r + (epsilon << h)
                        N2 = numerator_step(N, h, q2, bit)
                        raw_next[(Y2, q2, child[0], child[1])].append((r2, N2))

            for (Y, q, Lparam, Uparam, R), P in quotient.items():
                for epsilon in (0, 1):
                    child = child_interval(Lparam, Uparam, epsilon)
                    if child is None:
                        continue

                    Y2, q2, bit = control_step(Y, q, d, epsilon)
                    if q2 < REQ[h + 1] or q2 > J:
                        continue

                    R2 = lazy_residue_step(R, q, h, q2, bit, J, Lobs)
                    chi = epsilon + 2 * child[0] - Lparam
                    assert chi in (0, 1)
                    dx = chi << h

                    if bit == 0:
                        P2 = P + DELTA_LO * (3 ** q) * dx
                    else:
                        a = TPOS[q2 - 1]
                        assert h <= a
                        P2 = (
                            3 * P
                            + M_LO * ((1 << a) - (1 << h))
                            + DELTA_LO * (3 ** q2) * dx
                        )

                    key2 = (Y2, q2, child[0], child[1], R2)
                    if key2 in quotient_next:
                        merge_events += 1
                    if key2 not in quotient_next or P2 < quotient_next[key2]:
                        quotient_next[key2] = P2

            # Reconstruct the exact augmented quotient directly from all raw
            # histories and compare Bellman minimum labels.
            direct_augmented = {}
            for (Y, q, Lparam, Uparam), histories in raw_next.items():
                for r, N in histories:
                    R = lazy_residue(N, q, J, Lobs)
                    key = (Y, q, Lparam, Uparam, R)
                    P = score(r, N, h + 1, q, Lparam)
                    if key not in direct_augmented or P < direct_augmented[key]:
                        direct_augmented[key] = P

            assert quotient_next == direct_augmented
            layer_checks += len(direct_augmented)
            raw = dict(raw_next)
            quotient = quotient_next

        # At the final fixed-count layer m=Lobs, so the lazy coordinate is the
        # full requested terminal residue and filtering by any prescribed rho is
        # exactly represented by the quotient key.
        for (Y, q, Lparam, Uparam), histories in raw.items():
            assert q == J
            assert precision(q, J, Lobs) == Lobs
            for r, N in histories:
                R = lazy_residue(N, q, J, Lobs)
                assert R == N % (3 ** Lobs)
                key = (Y, q, Lparam, Uparam, R)
                assert key in quotient
                final_residue_checks += 1


assert sufficiency_checks > 0
assert minimality_checks > 0
assert transition_checks > 0
assert backward_checks > transition_checks
assert layer_checks > 0
assert merge_events > 0
assert final_residue_checks > 0


print("PASS A0 s=1 Route-B lazy ternary observation Bellman certificate")
print("test_roots", TEST_ROOTS)
print("future_precision", TEST_D)
print("test_parameter_interval", TEST_INTERVAL)
print("test_ternary_precisions", TEST_L_VALUES)
print("sufficiency_checks", sufficiency_checks)
print("minimality_checks", minimality_checks)
print("transition_checks", transition_checks)
print("backward_checks", backward_checks)
print("layer_checks", layer_checks)
print("merge_events", merge_events)
print("final_residue_checks", final_residue_checks)
print(
    "lazy_precision",
    "m(q)=max(0,L-(J-q)); no prefix ternary residue is needed while at least L future one-events remain",
)
print(
    "minimality",
    "when m(q)>0, modulo 3^(m-1) is insufficient in general for an arbitrary fixed future suffix",
)
print(
    "forward_transition",
    "bit0 leaves R fixed; each active bit1 grows precision by one trit and maps R -> 3R + (2^a-2^h)",
)
print(
    "backward_transition",
    "for a fixed bit1, a successor residue has either no predecessor or one unique predecessor at one-trit lower precision",
)
print(
    "bellman",
    "one minimum physical danger score P per exact (source control, interval payload, lazy ternary residue) key equals direct raw-history minimization",
)
print(
    "actual_scale",
    "for J=j0 and L=28 the ternary coordinate is dormant through q<=j0-28 and activates only during the last 28 one-events",
)
print(
    "dsd_audit",
    "observation resolution is separated from transition control and physical cost; downstream predicates not proved to be final N mod3^L congruences are not imported automatically",
)
print(
    "status",
    "minimal lazy ternary observation + physical Bellman composition CLOSED; using it to close the 14-root long-membership families remains OPEN",
)
