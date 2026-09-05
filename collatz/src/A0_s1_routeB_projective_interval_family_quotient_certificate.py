#!/usr/bin/env python3
"""Exact projective interval-family quotient for A0 s=1 Route-B.

For a finite integer parameter interval

    I = [L,U] cap Z,    N = U-L+1,

define the finite-horizon payload state

    Pi_d(I) = (N, L mod 2^d).

If two intervals have the same Pi_d state, then every common residue pullback
of width ell <= d has the same emptiness/cardinality and the resulting child
intervals have the same Pi_{d-ell} state.  This is the interval-payload
counterpart of the already-certified source-channel quotient

    Q_d(P) = (y mod 2^d, 3^q mod 2^d).

Consequently F_d(P,I)=(Q_d(P),Pi_d(I)) is an exact finite-horizon family
right-congruence under common parity-block refinement.

This file audits the interval theorem, exact residue partition, cardinality
contraction, lexicographic rank descent, and grouped residue-cover counting.
The algebraic proof is recorded in the matching note; the finite regression
below is only an implementation guard.
"""


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def pullback_interval(L: int, U: int, residue: int, ell: int):
    """Pull back m = residue + 2^ell n from [L,U]."""
    assert L <= U
    assert ell >= 1
    step = 1 << ell
    assert 0 <= residue < step
    lo = ceil_div(L - residue, step)
    hi = (U - residue) // step
    return None if lo > hi else (lo, hi)


def pi_state(L: int, U: int, d: int):
    assert L <= U
    assert d >= 0
    N = U - L + 1
    if d == 0:
        return (N, 0)
    return (N, L % (1 << d))


def child_size(child) -> int:
    return 0 if child is None else child[1] - child[0] + 1


L_VALUES = range(-12, 13)
N_VALUES = range(1, 17)
D_VALUES = range(1, 9)
SHIFT_MULTIPLIERS = (-3, -1, 1, 4)

projective_checks = 0
partition_checks = 0
child_size_checks = 0
rank_checks = 0
grouped_cover_checks = 0

for L in L_VALUES:
    for N in N_VALUES:
        U = L + N - 1

        for d in D_VALUES:
            parent_state = pi_state(L, U, d)

            # Deliberately distinct intervals with exactly the same Pi_d state.
            equivalents = []
            for k in SHIFT_MULTIPLIERS:
                shift = k * (1 << d)
                L2 = L + shift
                U2 = U + shift
                assert pi_state(L2, U2, d) == parent_state
                equivalents.append((k, L2, U2))

            for ell in range(1, d + 1):
                step = 1 << ell
                sizes = []

                for residue in range(step):
                    child = pullback_interval(L, U, residue, ell)
                    n_child = child_size(child)
                    sizes.append(n_child)

                    # Every residue child of a consecutive interval has one of
                    # the two balanced cardinalities floor(N/M), ceil(N/M).
                    assert n_child in {
                        N // step,
                        (N + step - 1) // step,
                    }
                    child_size_checks += 1

                    if child is not None:
                        # Exact well-founded rank: R=(N,d), lexicographic.
                        if N >= 2:
                            assert n_child < N
                        else:
                            assert n_child == 1
                            assert d - ell < d
                        rank_checks += 1

                    for k, L2, U2 in equivalents:
                        child2 = pullback_interval(L2, U2, residue, ell)
                        assert (child is None) == (child2 is None)

                        if child is not None:
                            lo, hi = child
                            lo2, hi2 = child2
                            # Translation by k*2^d upstairs becomes
                            # translation by k*2^(d-ell) after pullback.
                            delta = k * (1 << (d - ell))
                            assert lo2 == lo + delta
                            assert hi2 == hi + delta
                            assert pi_state(lo2, hi2, d - ell) == pi_state(
                                lo, hi, d - ell
                            )

                        projective_checks += 1

                # Full residue family is an exact disjoint partition of I.
                assert sum(sizes) == N
                assert sum(1 for n in sizes if n > 0) == min(step, N)
                partition_checks += 1

                # Generic symbolic-cover audit: put residue classes into an
                # arbitrary deterministic family of state labels and verify
                # that grouped counts still add exactly to the parent count.
                # No mathematical claim depends on this particular labeling.
                grouped = {}
                for residue, n_child in enumerate(sizes):
                    sigma = (residue % 3, residue.bit_count() & 1)
                    grouped[sigma] = grouped.get(sigma, 0) + n_child
                assert sum(grouped.values()) == N
                grouped_cover_checks += 1


assert projective_checks > 0
assert partition_checks > 0
assert child_size_checks > 0
assert rank_checks > 0
assert grouped_cover_checks == partition_checks

print("PASS A0 s=1 Route-B projective interval-family quotient certificate")
print("L_interval_count", len(tuple(L_VALUES)))
print("N_interval_count", len(tuple(N_VALUES)))
print("max_precision", max(D_VALUES))
print("equivalent_shift_representatives", len(SHIFT_MULTIPLIERS))
print("projective_checks", projective_checks)
print("partition_checks", partition_checks)
print("child_size_checks", child_size_checks)
print("rank_checks", rank_checks)
print("grouped_cover_checks", grouped_cover_checks)
print(
    "formation_audit",
    "Pi_d=(interval cardinality, lower endpoint mod 2^d) is sufficient to reconstruct every future residue-pullback payload through depth d",
)
print(
    "axis_audit",
    "source-channel Q_d and interval Pi_d consume the same ell units of dyadic precision under a length-ell block",
)
print(
    "dsd_audit",
    "equal finite-horizon family states preserve child existence, cardinality and quotient state; exact integer representatives are not identified beyond the requested horizon",
)
print(
    "status",
    "finite-horizon channel+interval family right-congruence CLOSED; compact global admissible residue-language closure remains OPEN",
)
