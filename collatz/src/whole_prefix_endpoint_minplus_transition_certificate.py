#!/usr/bin/env python3
"""Exact regression certificate for whole-prefix maximality as endpoint min-plus.

For the accelerated Collatz map, define

    mu[h,q](y) = minimum positive root n such that T^h(n)=y
                 and the first h parity bits contain q odd steps,

with +infinity when the fibre is empty.

For a length-h word with correction R,

    2^h y = 3^q n + R.

Hence, inside fixed (h,q,y), larger correction is exactly smaller root.
Whole-prefix maximum-correction status is therefore equivalent to n=mu[h,q](y).

The reverse one-step recurrence is

    mu[h,q](y) = min(
        mu[h-1,q](2y),
        mu[h-1,q-1]((2y-1)/3)  if y == 2 (mod 3)
    ).

If the actual prefix was already maximal at h-1, its own last-parity branch
already has minimum root n.  Thus maximality at h can fail only through the
single opposite-parity sibling endpoint fibre:

* actual pre-final endpoint x even:
      y=x/2.  The competing odd predecessor endpoint is (x-1)/3,
      available exactly when x == 1 (mod 3).

* actual pre-final endpoint x odd:
      y=(3x+1)/2.  The competing even predecessor endpoint is 3x+1.

So the first loss of whole-prefix maximality is necessarily a mixed-q
last-step exchange.  This is an algebraic min-plus theorem, not a Collatz proof.

This script exhaustively verifies the identities and recurrence for small roots
and horizons as a regression check.
"""

from collections import defaultdict

INF = 10**100


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def orbit(n: int, h: int):
    x=n
    q=0
    bits=[]
    for _ in range(h):
        b=x&1
        bits.append(b)
        q+=b
        x=T(x)
    return x,q,tuple(bits)


def correction(bits):
    R=0
    q=0
    for i,b in enumerate(bits):
        if b:
            R=3*R+(1<<i)
            q+=1
    return R,q


def build_mu(hmax: int, nmax: int):
    mu=[defaultdict(lambda: INF) for _ in range(hmax+1)]
    for n in range(1,nmax+1):
        mu[0][(0,n)] = min(mu[0][(0,n)], n)
        x=n
        q=0
        for h in range(1,hmax+1):
            q += x&1
            x=T(x)
            key=(q,x)
            if n<mu[h][key]:
                mu[h][key]=n
    return mu


def main():
    HMAX=9
    NMAX=1<<16
    mu=build_mu(HMAX,NMAX)

    # Fixed-fibre correction/root anti-ordering and exact affine identity.
    fibres=defaultdict(list)
    for h in range(1,HMAX+1):
        for n in range(1,1<<h):
            y,q,bits=orbit(n,h)
            R,q2=correction(bits)
            assert q==q2
            assert (3**q*n+R)==(1<<h)*y
            fibres[(h,q,y)].append((n,R,bits))

    for vals in fibres.values():
        vals.sort(key=lambda z:z[0])
        if len(vals)>1:
            assert vals[0][1]==max(v[1] for v in vals)

    # One-step min-plus recurrence.  Restrict to fibres whose minima are below
    # NMAX; the reverse parents then have roots in the same scanned range.
    for h in range(1,HMAX+1):
        for (q,y),m in list(mu[h].items()):
            even=mu[h-1].get((q,2*y),INF)
            odd=INF
            if y%3==2 and q>=1:
                x=(2*y-1)//3
                assert x&1
                odd=mu[h-1].get((q-1,x),INF)
            rhs=min(even,odd)
            assert rhs==m

    # Along every tested root, once h-1 is maximal, the h-th test compares the
    # root only with the opposite last-parity branch.
    for n in range(1,5000):
        x=n
        q=0
        prev_max=True
        for h in range(1,HMAX+1):
            b=x&1
            oldx=x
            if b:
                q+=1
            x=T(x)
            current_min=mu[h].get((q,x),INF)
            current_max=(current_min==n)
            if prev_max:
                if b==0:
                    sibling=INF
                    if oldx%3==1:
                        sibling=mu[h-1].get((q-1,(oldx-1)//3),INF) if q>=1 else INF
                else:
                    sibling=mu[h-1].get((q,3*oldx+1),INF)
                assert current_max == (n<=sibling)
            prev_max=current_max

    print("fixed-(H,q,y) max-correction == minimum-root: PASS")
    print("endpoint min-plus recurrence: PASS")
    print("first maximality loss is opposite-parity mixed-q exchange: PASS")


if __name__ == "__main__":
    main()
