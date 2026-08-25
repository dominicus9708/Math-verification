#!/usr/bin/env python3
"""Exact surplus-tail obstruction audit for the current Collatz proof program.

This is a scope certificate, not a Collatz proof.

1) It verifies the exact coefficient-stopping record
       n = 12_235_060_455, tau_c(n)=547
   and measures long excursions of the Beatty surplus
       d_B = q_B - b(B),  b(B)=min{q:3^q>=2^B}.

2) It records the general reverse-potential ceiling
       Lambda_Q <= (3/2)^Q,
   with equality attainable on the all-a=1 inverse chain z=-1 mod 3^Q.
   Hence strict reverse killing is impossible for every endpoint of surplus d
   whenever
       3^d >= (3/2)^Q.
"""

N = 12_235_060_455
K = 547


def beatty_boundary(K):
    b = [0] * (K + 1)
    q = 0
    p3 = 1
    for k in range(1, K + 1):
        target = 1 << k
        while p3 < target:
            q += 1
            p3 *= 3
        b[k] = q
    return b


def longest_run(ds, threshold):
    best = (0, -1, -1)
    start = None
    for i, d in enumerate(ds):
        if d >= threshold and start is None:
            start = i
        if (d < threshold or i == len(ds) - 1) and start is not None:
            end = i if d < threshold else i + 1
            if end - start > best[0]:
                best = (end - start, start, end - 1)
            start = None
    return best


def blind_surplus(Q):
    # least d with 3^d >= (3/2)^Q, in exact integer arithmetic
    d = 0
    while (3**d) * (2**Q) < 3**Q:
        d += 1
    return d


def main():
    b = beatty_boundary(K)
    x = N
    q = 0
    ds = [0]
    tau = None

    for k in range(1, K + 1):
        if x & 1:
            x = (3 * x + 1) // 2
            q += 1
        else:
            x //= 2

        d = q - b[k]
        ds.append(d)
        if d < 0 and tau is None:
            tau = k

    assert tau == 547
    alive_ds = ds[:tau]  # depths 0,...,546
    zeros = [i for i, d in enumerate(alive_ds) if d == 0]
    assert zeros == [0,1,2,4,5,8,10,466,539,541,542,543,544,545,546]
    assert max(alive_ds) == 9
    assert longest_run(alive_ds, 3) == (199, 261, 459)
    assert longest_run(alive_ds, 1) == (455, 11, 465)

    print("record_n", N)
    print("tau_c", tau)
    print("boundary_zero_depths", " ".join(map(str, zeros)))
    for t in (1,2,3,4,5):
        L, a, z = longest_run(alive_ds, t)
        print("longest_run_d_ge", t, "length", L, "depths", a, z)
    print("max_surplus_before_crossing", max(alive_ds))

    print("adaptive_Q_blind_table")
    for Q in range(1, 21):
        d = blind_surplus(Q)
        print(Q, d, f"{3**Q}/{2**Q}")

    assert blind_surplus(7) == 3
    assert 3**7 < 27 * 2**7

    print("PASS")


if __name__ == "__main__":
    main()
