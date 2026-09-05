#!/usr/bin/env python3
"""Exact pure-ballot control update across a forced valuation jump 0^a1.

Let Q(n)=ceil(n log_3 2), represented exactly as the least q with 3^q>2^n.
At absolute depth h let the candidate have q_used ones and surplus

    S = q_used - Q(h) >= 0.

Suppose the next odd event is forced after a zero run of length a, so the next
block is 0^a1.  During the a zeros q_used is unchanged and Q is monotone, so
all intermediate ballot inequalities are equivalent to the single endpoint
of the zero run:

    S >= Q(h+a)-Q(h).

At the final 1 step the condition is

    S+1 >= Q(h+a+1)-Q(h).

If both hold, the outgoing surplus is

    S' = S+1-[Q(h+a+1)-Q(h)].

Thus ballot control composes with an affine valuation-cylinder jump without
expanding the forced zero bits one by one.
"""


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


Q = threshold_requirements(256)


def jump_ballot(h: int, S: int, a: int):
    assert 0 <= h
    assert S >= 0
    assert a >= 0
    assert h + a + 1 < len(Q)

    zero_need = Q[h + a] - Q[h]
    final_need = Q[h + a + 1] - Q[h]
    ok = (S >= zero_need) and (S + 1 >= final_need)
    if not ok:
        return False, None
    S2 = S + 1 - final_need
    assert S2 >= 0
    return True, S2


def direct_ballot(h: int, S: int, a: int):
    q_used = Q[h] + S
    q = q_used
    # a forced zeros
    for i in range(1, a + 1):
        if q < Q[h + i]:
            return False, None
    # final forced one
    q += 1
    if q < Q[h + a + 1]:
        return False, None
    return True, q - Q[h + a + 1]


# Exhaustive finite regression of the block criterion against bitwise ballot
# checking across a broad range of depths, incoming surpluses, and zero runs.
for h in range(0, 160):
    for S in range(0, 12):
        for a in range(0, min(40, 255 - h)):
            assert jump_ballot(h, S, a) == direct_ballot(h, S, a)


# Concatenating two accepted valuation jumps agrees with direct checking of the
# combined forced word.
for h in range(0, 80):
    for S in range(0, 8):
        for a1 in range(0, 10):
            ok1, S1 = jump_ballot(h, S, a1)
            if not ok1:
                continue
            h1 = h + a1 + 1
            for a2 in range(0, 10):
                ok2, S2 = jump_ballot(h1, S1, a2)

                # Direct combined check.
                q = Q[h] + S
                good = True
                pos = h
                for bit in (0,) * a1 + (1,) + (0,) * a2 + (1,):
                    pos += 1
                    q += bit
                    if q < Q[pos]:
                        good = False
                        break
                assert ok2 == good
                if good:
                    assert S2 == q - Q[pos]

print("PASS A0 s=1 valuation-jump ballot-control certificate")
print("zero_run_gate", "S >= Q(h+a)-Q(h)")
print("final_one_gate", "S+1 >= Q(h+a+1)-Q(h)")
print("outgoing_surplus", "S'=S+1-[Q(h+a+1)-Q(h)]")
print("bitwise_zero_expansion_needed", False)
print("status", "EXACT pure-ballot control across forced 0^a1 jumps")
