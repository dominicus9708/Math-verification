#!/usr/bin/env python3
"""Exact finite verifier for a reverse contracting-ancestor sieve on Ansari's ternary core.

For the accelerated Collatz map

    T(n) = n/2                  (n even)
    T(n) = (3n+1)/2            (n odd),

an inverse-even step sends y -> 2y.  An inverse-odd step is available when
y == 2 (mod 3) and sends y -> (2y-1)/3.

Group one inverse-odd step together with e >= 0 preceding inverse-even
steps:

    y -> (2^(e+1) y - 1)/3.

After q inverse-odd steps and E total extra doublings, the resulting
ancestor has multiplicative factor 2^(q+E)/3^q relative to the endpoint.
If

    2^(q+E) < 3^q,

the final positive ancestor is strictly smaller than the endpoint.  Hence
the endpoint is recursive in Ansari's sense and cannot be a minimal
counterexample.

This verifier intersects that reverse sieve with the finite ternary
0/1 cylinders

    n = 4 * sum_i a_i 3^i + 3,   a_i in {0,1},

through depth QMAX=18.  It uses integer arithmetic only.
"""

from collections import defaultdict

QMAX = 18


def contraction_budget(q: int) -> int:
    """Largest E >= 0 for which 2^(q+E) < 3^q; -1 if none."""
    E = -1
    while (1 << (q + E + 1)) < 3**q:
        E += 1
    return E


BMAX = contraction_budget(QMAX)


def ternary_core_residue(mask: int, q: int) -> int:
    """n mod 3^q for n=4 sum a_i 3^i +3, with a_i from mask."""
    S = 0
    p = 1
    for i in range(q):
        if (mask >> i) & 1:
            S += p
        p *= 3
    return (4 * S + 3) % p


def first_contracting_depth(y: int, qmax: int):
    """Return (q,E) for the first contracted reverse ancestor, or None.

    `y` is known modulo 3^qmax.  After j inverse-odd steps only the residue
    modulo 3^(qmax-j) is needed.  For a fixed remaining residue, a smaller
    accumulated E dominates every larger E, so the dictionary retains only
    the minimum E for each residue.
    """
    states = {y: 0}  # remaining residue -> minimum accumulated E

    for j in range(1, qmax + 1):
        next_mod = 3 ** (qmax - j)
        nd = {}

        for cur, E0 in states.items():
            c3 = cur % 3
            if c3 == 0:
                # No power of 2 can change divisibility by 3, so no
                # inverse-odd step is reachable from this state.
                continue

            # Need 2^e cur == 2 (mod 3).
            # If cur==2 mod3, e is even; if cur==1 mod3, e is odd.
            parity = 0 if c3 == 2 else 1

            for e in range(parity, BMAX - E0 + 1, 2):
                E = E0 + e
                numerator = (1 << (e + 1)) * cur - 1
                assert numerator % 3 == 0
                nxt = numerator // 3
                if next_mod > 1:
                    nxt %= next_mod
                else:
                    nxt = 0

                old = nd.get(nxt)
                if old is None or E < old:
                    nd[nxt] = E

        states = nd
        if not states:
            return None

        Emin = min(states.values())
        if Emin <= contraction_budget(j):
            return j, Emin

    return None


def main():
    # Classify every depth-QMAX ternary 0/1 cylinder by the first reverse
    # contraction depth.  A cylinder killed at depth q contributes all of
    # its 2^(QMAX-q) extensions at depth QMAX.
    first_counts = defaultdict(int)
    witnesses = {}

    for mask in range(1 << QMAX):
        y = ternary_core_residue(mask, QMAX)
        hit = first_contracting_depth(y, QMAX)
        if hit is not None:
            q, E = hit
            first_counts[q] += 1
            witnesses.setdefault(q, (mask, E))

    # Convert extension counts at QMAX to numbers of minimal forbidden
    # q-cylinders.
    minimal_counts = {}
    for q, ext_count in sorted(first_counts.items()):
        scale = 1 << (QMAX - q)
        assert ext_count % scale == 0
        minimal_counts[q] = ext_count // scale

    killed = sum(first_counts.values())
    exact_measure_num = 0
    exact_measure_den = 1 << QMAX
    for q, c in minimal_counts.items():
        exact_measure_num += c << (QMAX - q)
    assert exact_measure_num == killed

    print("QMAX:", QMAX)
    print("contraction budgets:", [contraction_budget(q) for q in range(1, QMAX + 1)])
    print("minimal forbidden cylinder counts:", minimal_counts)
    print("killed depth-QMAX cylinders:", killed, "/", 1 << QMAX)
    print("exact removed fraction:", f"{killed}/{1<<QMAX}")
    print("decimal removed fraction:", killed / (1 << QMAX))

    # Explicit first depth-7 witness.
    q = 7
    mask7 = 0
    # low-to-high ternary choices a0..a6 = 1,1,0,0,0,1,0
    for i, bit in enumerate((1, 1, 0, 0, 0, 1, 0)):
        mask7 |= bit << i
    r7 = ternary_core_residue(mask7, q)
    assert r7 == 991
    assert first_contracting_depth(r7, q) == (7, 4)
    print("depth-7 witness residue:", r7)
    print("depth-7 ternary bits a0..a6:", (1, 1, 0, 0, 0, 1, 0))
    print("one forward word: 11111011000")
    print("affine relation: T^11(m)=(3^7 m + 2219)/2^11")
    print("ancestor: m=(2^11 n - 2219)/3^7 < n for n == 991 (mod 3^7)")


if __name__ == "__main__":
    main()
