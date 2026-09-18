#!/usr/bin/env python3
"""MATH-212 exact multi-cluster r=10 phase-summed surplus certificate.

One common phase orbit, exact Fraction arithmetic.
No AP/source/depth enumeration and no r=10 closure claim.
"""

from fractions import Fraction

LAM = Fraction(19, 503)
R = 10

def m(j: int) -> int:
    if j == 0:
        return 0
    return (3**j).bit_length() - 1 - j

TAU = {
    j: Fraction(3**j, 2**(j + m(j) + 1))
    for j in range(1, R + 1)
}

def exact_point_cluster(v: Fraction):
    sumphase = Fraction(0)
    for j in range(R):
        if j == 0:
            ph = v
        else:
            I = 1 if v <= TAU[j] else 0
            ph = v * Fraction(2**(j + m(j) + I), 3**j)
        sumphase += ph
    Ir = 1 if v <= TAU[R] else 0
    h = R + 1 + m(R) + Ir
    out = Fraction(2**(R + m(R) + Ir), 3**R)
    return sumphase / 6 - LAM * h, out

def infimum(n: int):
    cells = [(Fraction(1,2), Fraction(1), Fraction(1), Fraction(0), 0)]
    points = {Fraction(1,2), Fraction(1)}

    for _ in range(n):
        new = []
        for lo, hi, g, A, H in cells:
            cuts = {lo, hi}
            for t in TAU.values():
                c = t / g
                if lo < c < hi:
                    cuts.add(c)
                    points.add(c)

            s = sorted(cuts)
            for a, b in zip(s[:-1], s[1:]):
                mid = (a + b) / 2
                cur = g * mid

                phase_coeff = Fraction(0)
                for j in range(R):
                    if j == 0:
                        sc = Fraction(1)
                    else:
                        I = 1 if cur <= TAU[j] else 0
                        sc = Fraction(2**(j + m(j) + I), 3**j)
                    phase_coeff += sc
                phase_coeff /= 6

                Ir = 1 if cur <= TAU[R] else 0
                h = R + 1 + m(R) + Ir
                out = Fraction(2**(R + m(R) + Ir), 3**R)

                new.append((
                    a, b,
                    g * out,
                    A + g * phase_coeff,
                    H + h,
                ))
        cells = new

    best = None

    for lo, hi, g, A, H in cells:
        val = A * lo - LAM * H
        if best is None or val < best:
            best = val

    for v0 in points:
        if not (Fraction(1,2) < v0 <= 1):
            continue
        v = v0
        total = Fraction(0)
        for _ in range(n):
            e, out = exact_point_cluster(v)
            total += e
            v *= out
        if total < best:
            best = total

    assert len(cells) == 10*n + 1
    return best

EXPECTED = {
    1:13, 2:27, 3:42, 4:57, 5:72,
    6:87, 7:102, 8:117, 9:131, 10:147,
    11:161, 12:176, 13:191, 14:206, 15:221,
    16:236, 17:250, 18:265, 19:280, 20:297,
}

def ceil_fraction(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)

def main():
    vals = {}
    for n in range(1,21):
        e = infimum(n)
        z = ceil_fraction(e / LAM)
        assert z == EXPECTED[n], (n, e/LAM, z)
        vals[n] = e
        print(n, e, e/LAM, z)

    assert vals[1] == Fraction(45390185, 93871872)
    assert vals[2] == Fraction(6212454542993, 6151987003392)

    print("PASS MATH-212 exact multi-cluster r10 phase-summed thresholds")
    print("NO r10 CLOSURE CLAIM")

if __name__ == "__main__":
    main()
