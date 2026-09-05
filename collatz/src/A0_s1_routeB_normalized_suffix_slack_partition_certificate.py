#!/usr/bin/env python3
"""Normalized ternary suffix recurrence and slack-partition model.

Let target/candidate equal-count dominance words have one positions

    a_1<...<a_q,
    b_1<...<b_q,
    b_r<=a_r.

Index from the right:

    A_t=a_{q-t},
    B_t=b_{q-t},     t=0,1,...

and let z_t be the usual suffix carry after t rightmost one pairs have been
processed.  Normalize by the current target power of two:

    u_t = z_t * 2^(-A_t)   in the relevant 3-adic quotient.

With

    delta_t = A_t-B_t,
    g_t     = A_t-A_{t+1},

the one-position carry law becomes the horizon-free recurrence

    u_{t+1}
      = 2^{g_t} (u_t + 1 - 2^{-delta_t}) / 3.

The gate at level t is exactly

    u_t + 1 - 2^{-delta_t} == 0 mod 3.

Thus absolute exponent sizes disappear from the arithmetic; target dependence
enters only through the consecutive one-gap sequence g_t.

There is a second exact reduction of the ordering constraints.  Define the
target capacity and candidate slack

    D_t = A_t-(q-t-1),
    s_t = B_t-(q-t-1).

Then

    0 <= s_t <= D_t,
    s_{t+1} <= s_t,

and conversely every such nonincreasing slack sequence defines a unique legal
last-one position sequence.  The displacement is simply

    delta_t = D_t-s_t.

Also

    D_{t+1}=D_t+1-g_t.

For the characteristic target, g_t is in {1,2}, so D_t is a staircase that
stays level or decreases by one.  The candidate suffix family is therefore an
integer partition/Ferrers-type path lying below this target capacity staircase.

At precision L, only t=0,...,L-1 occur by the suffix-locality theorem.  Hence
the target-relative ternary collider problem is reduced exactly to:

  * a length-L capacity/gap path;
  * a nonincreasing slack sequence under that path;
  * the normalized 3-adic recurrence above.

This is a structural reduction, not yet a bounded-width DP theorem.
"""

from itertools import combinations

MAX_H = 9


def correction_positions(pos):
    q = len(pos)
    return sum((3 ** (q-r-1)) * (2 ** a) for r,a in enumerate(pos))


def normalized_accept(a,b,L):
    q = len(a)
    assert len(b)==q and 1<=L<=q

    u = 0
    m = L
    for t in range(L):
        A = a[q-1-t]
        B = b[q-1-t]
        delta = A-B

        mod = 3**m
        inv = pow(pow(2,delta,mod),-1,mod)
        numer = (u + 1 - inv) % mod
        if numer % 3:
            return False

        if t == L-1:
            return True

        A_next = a[q-2-t]
        g = A-A_next
        next_mod = 3**(m-1)
        u = (pow(2,g,next_mod) * (numer//3)) % next_mod
        m -= 1

    raise AssertionError("unreachable")


recurrence_checks = 0
slack_checks = 0
capacity_checks = 0

for h in range(1,MAX_H+1):
    for q in range(1,h+1):
        for a in combinations(range(h),q):
            Ct = correction_positions(a)
            D = []
            for t in range(q):
                A = a[q-1-t]
                D.append(A-(q-t-1))
                assert D[-1] >= 0
                if t:
                    g_prev = a[q-t]-a[q-1-t]
                    assert D[t] == D[t-1] + 1 - g_prev
                    capacity_checks += 1

            for b in combinations(range(h),q):
                if not all(b[i] <= a[i] for i in range(q)):
                    continue

                s = []
                for t in range(q):
                    B = b[q-1-t]
                    s.append(B-(q-t-1))
                    assert 0 <= s[-1] <= D[t]
                    assert D[t]-s[-1] == a[q-1-t]-b[q-1-t]
                assert all(s[t+1] <= s[t] for t in range(q-1))
                slack_checks += 1

                Cw = correction_positions(b)
                for L in range(1,q+1):
                    direct = (Ct-Cw) % (3**L) == 0
                    recursive = normalized_accept(a,b,L)
                    assert direct == recursive
                    recurrence_checks += 1

assert recurrence_checks == 101_763
assert slack_checks == 23_703
assert capacity_checks > 0

print("PASS A0 s=1 Route-B normalized suffix slack-partition certificate")
print("max_h",MAX_H)
print("recurrence_checks",recurrence_checks)
print("slack_checks",slack_checks)
print("capacity_checks",capacity_checks)
print(
    "normalized_recurrence",
    "u_next=2^g*(u+1-2^(-delta))/3",
)
print(
    "slack_model",
    "0<=s_t<=D_t and s_(t+1)<=s_t with delta_t=D_t-s_t",
)
print(
    "target_data",
    "absolute positions are replaced by the gap/capacity path D_(t+1)=D_t+1-g_t",
)
print(
    "dsd_audit",
    "the L-local ternary family is represented as a constrained partition path plus normalized 3-adic dynamics; bounded state width is not inferred",
)
print(
    "status",
    "normalized suffix/slack reduction CLOSED; projective cylinder composition over slack partitions remains OPEN",
)
