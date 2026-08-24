#!/usr/bin/env python3
"""Exact coherent no-descent => coefficient-survival certificate for m=45.

Accelerated Collatz map:
    T(n)=n/2            for even n,
    T(n)=(3n+1)/2       for odd n.

Current m=45 recursively sufficient roots satisfy
    N >= NMIN = 4*3^45 + 3
and N == 3 (mod 4), so the first two accelerated parity symbols are forced 11.

For a length-j parity prefix with q odd symbols,
    2^j T^j(N) = 3^q N + R_j.

Let b_j=min{q:3^q >= 2^j}.  Suppose every earlier prefix has remained >=N.
If no subcritical state has survived before depth j, then the unique minimum-q
surviving parity prefix is the mechanical boundary word q=b_j.  At a plateau
b_j=b_(j-1), it extends minimally by an even bit.  At a rise
b_j=b_(j-1)+1, it extends minimally by an odd bit.

The ONLY way a first coherent subcritical state can be born is therefore at a
rise depth j by taking the even child of the previous mechanical boundary
prefix.  That child has q=b_j-1 and unchanged correction R_(j-1).  It survives
only if
    R_(j-1) >= N (2^j - 3^(b_j-1)).

Because the right side increases with N, it suffices to test N=NMIN.  This
script evaluates that exact inequality at every rise j<=20000 and proves it is
always strict in the descending direction.

Consequently, for every current m=45 root N and every j<=20000,
    [T^i(N)>=N for all i<=j] => [3^q_i >= 2^i for all i<=j].

This closes the apparent endpoint-only H=195,q=123 exception: it cannot occur
on one coherent no-descent trajectory.

This is a finite exact theorem for the current m=45 layer, not a proof of the
Collatz conjecture.
"""

NMIN = 4 * 3**45 + 3
HMAX = 20_000


def main() -> None:
    q = 0
    p3 = 1          # 3^q on the mechanical boundary
    R = 0           # correction of the mechanical boundary prefix

    rise_count = 0
    worst_num = 0   # maximize R / (NMIN*D) exactly by cross multiplication
    worst_den = 1
    worst_H = -1
    worst_q = -1

    for H in range(1, HMAX + 1):
        target = 1 << H
        b = q
        p = p3
        while p < target:
            p *= 3
            b += 1

        assert b - q in (0, 1)
        rise = (b == q + 1)

        if rise and H >= 3:
            rise_count += 1
            # First possible coherent subcritical child: append even instead
            # of the boundary's forced odd rise.
            D = (1 << H) - p3   # p3=3^(b-1)=3^q before the rise
            assert D > 0

            # Exact descent inequality for every N>=NMIN.
            assert R < NMIN * D, (H, q)

            if R * worst_den > worst_num * (NMIN * D):
                worst_num = R
                worst_den = NMIN * D
                worst_H = H
                worst_q = q

        # Follow the unique minimum-q coefficient-surviving boundary child.
        if rise:
            R = 3 * R + (1 << (H - 1))
            q = b
            p3 = p
        else:
            q = b
            p3 = p

        assert p3 == 3**q
        assert p3 >= (1 << H)

    assert worst_H == 19_457
    assert worst_q == 12_276
    assert rise_count == 12_617

    # In particular the previously apparent endpoint exception is impossible
    # coherently: at H=195 the minimum surviving q is b_195=124, not 123.
    # The rise offshoot q=123 fails the exact no-descent inequality above.
    b195 = 0
    p = 1
    while p < (1 << 195):
        p *= 3
        b195 += 1
    assert b195 == 124

    print("m45 coherent ballot equivalence through depth", HMAX, ": PASS")
    print("rise offshoots checked:", rise_count)
    print("H=195 endpoint-only q=123 exception: coherently impossible")
    print("minimum coherent q at H=195: 124")
    print("worst tested rise depth:", worst_H, "previous q:", worst_q)
    print("worst safety ratio R/(Nmin*D) < 1 exactly")


if __name__ == "__main__":
    main()
