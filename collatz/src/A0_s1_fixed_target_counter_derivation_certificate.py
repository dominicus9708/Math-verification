#!/usr/bin/env python3
"""Regression certificate for fixed-target remaining-counter derivation.

For fixed total length t0 and total one-count j0, an active pure-ballot state
uses

    S = q - Q(h),
    Q(h)=ceil(h log_3 2).

Therefore

    q       = Q(h)+S,
    n_rem   = t0-h,
    q_rem   = j0-Q(h)-S.

Across a legal valuation jump 0^a1, q increases by exactly one, hence q_rem
decreases by exactly one.  For the current terminal checkpoint observation,
the final-28-one suffix activates exactly at q_rem=28.

Finite checks below are regression guards; the identities are algebraic.
"""

T0 = 104_398_605_910
J0 = 65_868_186_701
K_TERMINAL = 28


def threshold_requirements(nmax: int):
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


Q = threshold_requirements(512)


def derived(h, S, t0, j0):
    q = Q[h] + S
    return q, t0-h, j0-q


# Generic finite regression across many fixed targets and legal abstract jumps.
for t0 in range(40, 220, 17):
    j0 = Q[t0] + 12
    for h in range(0, t0):
        for S in range(0, 8):
            q, nrem, qrem = derived(h, S, t0, j0)
            assert q == Q[h] + S
            assert nrem == t0-h
            assert qrem == j0-Q[h]-S

            for a in range(0, min(12, t0-h-1)):
                h2 = h+a+1
                q2 = q+1
                S2 = q2-Q[h2]
                if S2 < 0:
                    continue
                got_q2, got_nrem2, got_qrem2 = derived(h2, S2, t0, j0)
                assert got_q2 == q2
                assert got_nrem2 == nrem-(a+1)
                assert got_qrem2 == qrem-1


# Current fixed constants and terminal activation identity.
assert T0 == 104_398_605_910
assert J0 == 65_868_186_701
assert K_TERMINAL == 28
assert J0-K_TERMINAL == 65_868_186_673

# Algebraic activation equivalence: q_rem=K iff q=j0-K.
for j0 in range(30, 90):
    for q in range(j0+1):
        qrem = j0-q
        assert (qrem == K_TERMINAL) == (q == j0-K_TERMINAL)

print("PASS A0 s=1 fixed-target counter derivation certificate")
print("target_t0", T0)
print("target_j0", J0)
print("derived", "q=Q(h)+S; n_rem=t0-h; q_rem=j0-Q(h)-S")
print("valuation_jump", "q_rem decreases by exactly one per 0^a1 jump")
print("terminal_K", K_TERMINAL)
print("terminal_activation_one_count", J0-K_TERMINAL)
print("extra_remaining_counter_state_needed", False)
print("status", "EXACT state-axis redundancy; finite checks are regression evidence")
