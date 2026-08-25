#!/usr/bin/env python3
"""Exact bridge certificate between the DSD signed-skew and Beatty-surplus coordinates.

Scope: structural/audit certificate only. It does not prove Collatz.

For an accelerated odd-event path
    x_{q+1} = (3 x_q + 1) / 2^{v_q},
    A_q = sum_{j<q} v_j,
define
    Theta_q = 3^q / 2^{A_q}.

The signed-skew coordinate used in the aperiodic hard core is
    s_q = floor(q log_2 3) - A_q.
The ordinary-step Beatty boundary is
    b(B) = min{r: 3^r >= 2^B},
and at the completed odd-event time B=A_q the surplus is
    d_{A_q} = q - b(A_q).

This script verifies, using exact integer arithmetic,
    s_q       = floor(log_2 Theta_q),
    d_{A_q}   = floor(log_3 Theta_q).

It also reconstructs the canonical lift digits for the current exact
coefficient-record integer N=12,235,060,455 and verifies that the formation
floor stabilizes to N after odd-event 27 (A=34), after which all audited lift
digits vanish. Finally it computes the exact necessary adaptive reverse
resolution Q_need at each completed event from
    (3/2)^Q > Theta_q.
"""

N = 12_235_060_455
TAU_C = 547


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def beatty_boundary(K: int):
    b = [0] * (K + 1)
    r = 0
    p3 = 1
    for B in range(1, K + 1):
        target = 1 << B
        while p3 < target:
            r += 1
            p3 *= 3
        b[B] = r
    return b


def accelerated_events(limit_A: int):
    x = N
    A = 0
    vals = []
    events = [(0, 0, x)]
    while A < limit_A:
        y = 3 * x + 1
        v = v2(y)
        x = y >> v
        vals.append(v)
        A += v
        events.append((len(vals), A, x))
    return vals, events


def canonical_lift_rows(vals):
    A = 0
    rho = 1
    y = 1
    rows = []

    for q, v in enumerate(vals):
        modulus = 1 << v
        half = (3 * y + 1) // 2
        t = (((1 << (v - 1)) - half) * pow(3, -(q + 1), modulus)) % modulus

        rho_next = rho + t * (1 << (A + 1))
        numerator = 3 * y + 1 + 2 * t * (3 ** (q + 1))
        assert numerator % (1 << v) == 0
        y_next = numerator >> v
        assert y_next > 0 and (y_next & 1)

        A_next = A + v
        rows.append((q, v, A, rho, y, t, A_next, rho_next, y_next))
        A, rho, y = A_next, rho_next, y_next

    return rows


def adaptive_q_need(q: int, A: int) -> int:
    """Least Q>=0 with (3/2)^Q > 3^q/2^A, in exact arithmetic."""
    Q = 0
    while (3 ** Q) * (2 ** A) <= (2 ** Q) * (3 ** q):
        Q += 1
    return Q


def main():
    b = beatty_boundary(TAU_C + 64)
    vals, events = accelerated_events(TAU_C + 64)
    lift = canonical_lift_rows(vals)

    # Canonical naturalness audit: the last nonzero lift digit is t_26.
    nonzero = [row[0] for row in lift if row[5] != 0]
    assert nonzero[-1] == 26
    row26 = lift[26]
    assert row26[6] == 34
    assert row26[7] == N
    assert all(row[5] == 0 for row in lift[27:])
    assert all(row[7] == N for row in lift[26:])

    print("record_n", N)
    print("last_nonzero_lift_index", nonzero[-1])
    print("formation_stabilizes_after_completed_events", 27)
    print("formation_stabilization_A", row26[6])
    print("formation_stabilized_rho", row26[7])

    bridge_rows = []
    for q, A, xq in events:
        if A > TAU_C:
            break

        p3q = 3 ** q

        s = p3q.bit_length() - 1 - A
        assert (1 << (A + s)) <= p3q < (1 << (A + s + 1))

        d = q - b[A]
        assert (3 ** d) * (1 << A) <= p3q < (3 ** (d + 1)) * (1 << A)

        floor_q_gamma = p3q.bit_length() - 1
        assert s == floor_q_gamma - A

        Qneed = adaptive_q_need(q, A)
        if Qneed > 0:
            assert (3 ** Qneed) * (2 ** A) > (2 ** Qneed) * p3q
            assert (3 ** (Qneed - 1)) * (2 ** A) <= (2 ** (Qneed - 1)) * p3q

        bridge_rows.append((q, A, xq, s, d, Qneed))

    crossing = [r for r in bridge_rows if r[1] == TAU_C]
    assert crossing == [(345, 547, 10_740_669_913, -1, -1, 0)]

    stable_alive = [r for r in bridge_rows if r[0] >= 27 and r[1] < TAU_C]
    assert len(stable_alive) == 318

    max_s = max(stable_alive, key=lambda r: (r[3], r[0]))
    max_d = max(stable_alive, key=lambda r: (r[4], r[0]))
    max_Q = max(stable_alive, key=lambda r: (r[5], r[0]))

    assert max(r[3] for r in stable_alive) == 14
    assert max(r[4] for r in stable_alive) == 9
    assert max(r[5] for r in stable_alive) == 26

    print("completed_event_bridge_rows_through_crossing", len(bridge_rows))
    print("crossing_q_A_s_d_Q", crossing[0][0], crossing[0][1], crossing[0][3], crossing[0][4], crossing[0][5])
    print("stable_alive_completed_events", len(stable_alive))
    print("max_signed_skew_row_q_A_s_d_Q", max_s[0], max_s[1], max_s[3], max_s[4], max_s[5])
    print("max_surplus_row_q_A_s_d_Q", max_d[0], max_d[1], max_d[3], max_d[4], max_d[5])
    print("max_adaptive_Q_row_q_A_s_d_Q", max_Q[0], max_Q[1], max_Q[3], max_Q[4], max_Q[5])

    q, A, _xq, s, d, Qneed = max_d
    assert (q, A, s, d, Qneed) == (227, 345, 14, 9, 26)

    print("PASS")


if __name__ == "__main__":
    main()
