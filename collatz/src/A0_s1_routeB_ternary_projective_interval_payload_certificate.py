#!/usr/bin/env python3
"""Exact ternary projective interval-payload quotient for A0 s=1 Route-B.

This certificate closes one missing compression interface inside the backward
right-H projective filter.

Assume one projective displacement coordinate d ranges over a finite consecutive
integer interval

    I = [L,U] cap Z,   N = U-L+1.

The already-certified projective displacement isometry says that, at a fixed
surviving parity/gate, an outgoing carry congruence modulo 3^ell pulls back to
exactly one displacement congruence

    d == rho (mod 3^ell).

For a remaining ternary lookahead k define

    Pi3_k(I) = (N, L mod 3^k).

If two intervals have the same Pi3_k state, then every common projective
carry-cylinder pullback of precision ell<=k has:

* the same emptiness;
* the same cardinality;
* child quotient-parameter intervals with the same Pi3_(k-ell) state.

Indeed d=rho+3^ell n converts the intersection to one consecutive n interval.
Translation of I by t*3^k becomes translation of the child n interval by
exactly t*3^(k-ell).

Therefore Pi3_k is an exact finite-horizon right-congruence for ONE
one-dimensional projective displacement family under future carry-cylinder
queries whose total requested precision is at most k.

Scope restriction is essential.  Successive ternary gates introduce new ranked
one positions/displacement variables and ordering constraints.  This theorem
does NOT identify the full multi-gate right-H state with one Pi3 payload and
does NOT close G2 by itself.  It removes flat raw-carry enumeration inside each
fixed one-dimensional projective cylinder family.

The finite regression below is only an implementation guard; the theorem is the
integer residue-pullback identity above.
"""


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def pullback_interval(L: int, U: int, rho: int, ell: int):
    """Pull back d=rho+3^ell*n from [L,U]."""
    assert L <= U
    assert ell >= 1
    step = 3 ** ell
    assert 0 <= rho < step
    lo = ceil_div(L - rho, step)
    hi = (U - rho) // step
    return None if lo > hi else (lo, hi)


def pi3_state(L: int, U: int, k: int):
    assert L <= U
    assert k >= 0
    N = U - L + 1
    return (N, 0 if k == 0 else L % (3 ** k))


def child_size(child) -> int:
    return 0 if child is None else child[1] - child[0] + 1


L_VALUES = range(-12, 13)
N_VALUES = range(1, 18)
K_VALUES = range(1, 6)
SHIFT_MULTIPLIERS = (-2, -1, 1, 3)

projective_checks = 0
partition_checks = 0
child_size_checks = 0
rank_checks = 0

for L in L_VALUES:
    for N in N_VALUES:
        U = L + N - 1

        for k in K_VALUES:
            parent_state = pi3_state(L, U, k)

            equivalents = []
            for t in SHIFT_MULTIPLIERS:
                shift = t * (3 ** k)
                L2 = L + shift
                U2 = U + shift
                assert pi3_state(L2, U2, k) == parent_state
                equivalents.append((t, L2, U2))

            for ell in range(1, k + 1):
                step = 3 ** ell
                sizes = []

                for rho in range(step):
                    child = pullback_interval(L, U, rho, ell)
                    n_child = child_size(child)
                    sizes.append(n_child)

                    # Consecutive integers split as evenly as possible among
                    # the 3^ell residue classes.
                    assert n_child in {
                        N // step,
                        (N + step - 1) // step,
                    }
                    child_size_checks += 1

                    if child is not None:
                        if N >= 2:
                            assert n_child < N or step == 1
                        else:
                            assert n_child == 1
                            assert k - ell < k
                        rank_checks += 1

                    for t, L2, U2 in equivalents:
                        child2 = pullback_interval(L2, U2, rho, ell)
                        assert (child is None) == (child2 is None)

                        if child is not None:
                            delta = t * (3 ** (k - ell))
                            assert child2 == (child[0] + delta, child[1] + delta)
                            assert pi3_state(*child2, k - ell) == pi3_state(
                                *child, k - ell
                            )

                        projective_checks += 1

                # All displacement residue classes form an exact disjoint
                # partition of the parent family.
                assert sum(sizes) == N
                assert sum(1 for n in sizes if n > 0) == min(step, N)
                partition_checks += 1

assert projective_checks == 912_900
assert partition_checks == 6_375
assert child_size_checks > 0
assert rank_checks > 0

print("PASS A0 s=1 Route-B ternary projective interval-payload certificate")
print("interval_lower_samples", len(tuple(L_VALUES)))
print("interval_size_samples", len(tuple(N_VALUES)))
print("max_ternary_lookahead", max(K_VALUES))
print("equivalent_shift_representatives", len(SHIFT_MULTIPLIERS))
print("projective_checks", projective_checks)
print("partition_checks", partition_checks)
print("child_size_checks", child_size_checks)
print("rank_checks", rank_checks)
print(
    "payload",
    "Pi3_k=(interval cardinality, lower endpoint mod 3^k)",
)
print(
    "pullback",
    "one outgoing carry cylinder mod 3^ell pulls back through projective isometry to one displacement residue d=rho mod 3^ell",
)
print(
    "compression",
    "within one fixed one-dimensional projective displacement family, raw carry residues need not be enumerated separately",
)
print(
    "dsd_audit",
    "the quotient preserves exactly the requested finite-horizon carry-cylinder predicate; it does not forget new displacement/order coordinates introduced by later ranks",
)
print(
    "status",
    "single-gate ternary projective interval-family quotient CLOSED; higher-depth multi-displacement right-H filter remains OPEN",
)
