from math import ceil, log

ALPHA = log(2, 3)

def b(j):
    q = 0
    while 3**q < 2**j:
        q += 1
    return q

def boundary_words(L):
    out = []
    def rec(bits, q):
        j = len(bits) + 1
        for bit in (0, 1):
            qq = q + bit
            if qq < b(j):
                continue
            nb = bits + (bit,)
            if j == L:
                if qq == b(L):
                    out.append(nb)
            else:
                rec(nb, qq)
    rec((), 0)
    return out

def residue(bits):
    n = len(bits)
    mod = 1 << n
    q = 0
    s = 0
    for j, bit in enumerate(bits):
        if bit:
            q += 1
            s = (s + (1 << j) * pow(3, -q, mod)) % mod
    return (-s) % mod

def check(L=20):
    W = boundary_words(L)
    S = set(W)
    P = [j for j in range(L - 1) if b(j + 1) == b(j)]
    assert all(P[i + 1] - P[i] >= 2 for i in range(len(P) - 1))
    mod = 1 << (L + 1)
    checked = 0
    for w in W:
        pref = [0]
        for bit in w:
            pref.append(pref[-1] + bit)
        for j in P:
            if w[j] + w[j + 1] != 1:
                continue
            ww = list(w)
            ww[j], ww[j + 1] = ww[j + 1], ww[j]
            ww = tuple(ww)
            assert ww in S
            ell = pref[j] + 1
            oldpos = j if w[j] else j + 1
            newpos = j if ww[j] else j + 1
            expected = (-((1 << newpos) - (1 << oldpos)) * pow(3, -ell, mod)) % mod
            assert (residue(ww + (1,)) - residue(w + (1,))) % mod == expected
            checked += 1
    print('L', L, 'boundary', len(W), 'plateau_pairs', len(P), 'checked_swaps', checked)
    print('plateau-pair cube arithmetic: PASS')

if __name__ == '__main__':
    check()
