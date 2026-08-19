#!/usr/bin/env python3
"""Exact cumulative language-count diagnostic for the packed-terminal s=1 rule.

Counts two prefix-closed languages through H=500:

  B_H       : coefficient survival only;
  B_H^pack  : coefficient survival plus the safe packed-terminal s=1
              original-start predecessor elimination at every plateau.

The packed rule has a finite terminal state: relative coefficient height
h=q-qmin(L) plus the last two odd positions modulo 6.  Therefore both counts
are exact integer dynamic programs.

The finite data show a substantial constant-factor reduction but no evidence of
a new positive asymptotic entropy rate: the additional information exclusion
log2(|B_H|/|B_H^pack|) remains around 0.3 bit through H=500.

This is deliberately named a diagnostic rather than an asymptotic certificate.
It does not prove that the ratio remains bounded for all H and is not a proof
of the Collatz conjecture.
"""

from collections import defaultdict
from math import log2

EXPECTED = {
    20: (
        27328,
        22572,
    ),
    50: (
        3734259929440,
        3016397927387,
    ),
    100: (
        302560669500543257546172187,
        248260976836271970960995163,
    ),
    200: (
        4917911213247274697935031643998322726370567793471092895,
        3984645094191945702169275254628740647875911918900408801,
    ),
    300: (
        111358800986904242131297286221730529252986567662022866509378290558038512175289008981,
        89351423002741033096385677113149964125557763233279090100684336998507637240667388639,
    ),
    400: (
        2991976163397584332049206932845884542213698957101572273358822068486559963480621878733925829902904362475424974343,
        2393977330612194697175207738683344849249482453574498955672063561408772341466096721431745915381002640805802366821,
    ),
    500: (
        87021278249897937515360373875149190908779415905852926972014983380008739148197078965285084410585905422749739380641259471228380960815303168471,
        69404028873699898104811174424832054193137028128678065890752089631200809650241904068693538270346698221518815697392493743392266313732740004906,
    ),
}


def qmins(H: int):
    out = [0] * (H + 1)
    q = 0
    p3 = 1
    for L in range(1, H + 1):
        while p3 < (1 << L):
            q += 1
            p3 *= 3
        out[L] = q
    return out


def terminal_kill(L: int, a: int, b: int) -> bool:
    target = (3 * pow(2, L - 2, 9) + pow(2, L - 1, 9)) % 9
    actual = (3 * pow(2, a, 9) + pow(2, b, 9)) % 9
    diff = (target - actual) % 9
    return diff % 3 == 0 and diff != 0


def main():
    Hmax = max(EXPECTED)
    qm = qmins(Hmax)

    # Start after the forced prefix 11 at L=2.
    coeff = {0: 1}  # relative height h=q-qmin(L)
    safe = {(0, 0, 1): 1}  # (h, previous-last odd mod6, last odd mod6)
    previous_qmin = 2

    print("H coefficient_count packed_safe_count safe_over_coefficient extra_bits")

    for L in range(3, Hmax + 1):
        inc = qm[L] - previous_qmin
        assert inc in (0, 1)

        cnext = defaultdict(int)
        for h, count in coeff.items():
            if h >= inc:
                cnext[h - inc] += count
            cnext[h + 1 - inc] += count
        coeff = cnext

        snext = defaultdict(int)
        pos = (L - 1) % 6
        plateau = inc == 0

        for (h, a, b), count in safe.items():
            # even child
            if h >= inc:
                kill = plateau and h == 0 and terminal_kill(L, a, b)
                if not kill:
                    snext[(h - inc, a, b)] += count

            # odd child
            snext[(h + 1 - inc, b, pos)] += count

        safe = snext
        previous_qmin = qm[L]

        if L in EXPECTED:
            C = sum(coeff.values())
            S = sum(safe.values())
            assert (C, S) == EXPECTED[L]
            print(
                L,
                C,
                S,
                S / C,
                log2(C) - log2(S),
            )

    print("packed-terminal s1 entropy diagnostic: PASS")


if __name__ == "__main__":
    main()
