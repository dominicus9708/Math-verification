from itertools import combinations, product

# Finite audit for the exact theorem recorded in
# 2026-08-25-distinct-3adic-depth-cosine-orthogonality.md.
#
# For distinct depths q_t >= 2 and 3-adic units a_t, expansion of
# prod cos^2(pi*a_t*y/3^q_t) over y == u (mod 3) contains a character
# indexed by eps_t in {-1,0,1}.  It survives the coset average only if
#
#   3^(Q-1) | sum eps_t*a_t*3^(Q-q_t),  Q=max(q_t).
#
# The theorem says this happens only for eps=0.  The verifier checks all
# depth subsets through Q=8 and several complete unit choices.  The proof is
# generic and uses the unique minimum 3-adic valuation; this script is a
# regression certificate, not the proof itself.


def v3(n):
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def audit(qs, units):
    Q = max(qs)
    modulus = 3 ** (Q - 1)
    for eps in product((-1, 0, 1), repeat=len(qs)):
        if not any(eps):
            continue
        C = sum(e*a*(3 ** (Q-q)) for e, a, q in zip(eps, units, qs))
        assert C % modulus != 0

        # Generic proof invariant: among nonzero epsilon terms, the largest
        # q has the unique smallest 3-adic valuation Q-q.
        active = [(q, a, e) for q, a, e in zip(qs, units, eps) if e]
        qstar = max(q for q, _, _ in active)
        assert v3(C) == Q - qstar
        assert Q - qstar <= Q - 2


for Q in range(2, 9):
    levels = list(range(2, Q + 1))
    for r in range(1, len(levels) + 1):
        for qs in combinations(levels, r):
            # A deterministic family of unit assignments exercises arbitrary
            # residues, signs, and lifted units without exponential blowup.
            unit_sets = []
            unit_sets.append(tuple(1 for _ in qs))
            unit_sets.append(tuple(2 for _ in qs))
            unit_sets.append(tuple((2 * i + 1) for i, _ in enumerate(qs)))
            unit_sets.append(tuple((3 ** q - 2) for q in qs))
            for units in unit_sets:
                assert all(a % 3 for a in units)
                audit(qs, units)

print("distinct 3-adic depth cosine orthogonality certificate: PASS")
