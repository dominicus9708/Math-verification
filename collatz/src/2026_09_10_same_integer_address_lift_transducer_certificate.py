#!/usr/bin/env python3
"""MATH-055 exact same-integer address-lift transducer certificate.

For a parity prefix of length k with odd count q and correction C, let
    N_k = -C * 3^(-q) mod 2^k
be its canonical start residue and
    e_k = (3^q N_k + C)/2^k.
When the canonical residue is lifted by one start-address bit t,
    N_{k+1}=N_k+t*2^k,
the next parity bit satisfies b = e_k+t (mod 2).
The endpoint lift is then
    b=0: e'=(e+3^q t)/2
    b=1: e'=(3e+3^(q+1)t+1)/2.

This certificate compares the bitwise lift transducer with direct parity-prefix
reconstruction on exhaustive small prefixes and checks the 61+11 decomposition
for the seven MATH-054 budget-5 starts.

Finite exact certificate only. Collatz remains OPEN.
"""
from itertools import product

BUDGET5_STARTS = [
    2444527107741509901307,
    2370124790779996953595,
    2961350309188690926587,
    2614662758027828756219,
    2940293571120906010363,
    2564127977755122686715,
    2972242381612692366171,
]


def correction(bits):
    C=q=0
    for p,b in enumerate(bits):
        if b:
            C=3*C+(1<<p)
            q+=1
    return C,q


def canonical_start(bits):
    k=len(bits)
    C,q=correction(bits)
    if k==0:
        return 0,0,0
    mod=1<<k
    N=(-C*pow(pow(3,q,mod),-1,mod))%mod
    e=(3**q*N+C)//mod
    return N,e,q


def lift(N,e,q,k,t):
    N2=N+(t<<k)
    b=(e+t)&1
    if b==0:
        e2=(e+(3**q)*t)//2
        q2=q
    else:
        e2=(3*e+(3**(q+1))*t+1)//2
        q2=q+1
    return N2,e2,q2,b


def direct_bits_from_N(N,k):
    n=N; out=[]
    for _ in range(k):
        b=n&1
        out.append(b)
        n=(3*n+1)//2 if b else n//2
    return tuple(out)


def selftest():
    # Exhaustive parity-prefix reconstruction through length 12.
    for k in range(0,12):
        for bits in product((0,1), repeat=k):
            N,e,q=canonical_start(bits)
            for t in (0,1):
                N2,e2,q2,b=lift(N,e,q,k,t)
                target=bits+(b,)
                Nd,ed,qd=canonical_start(target)
                assert N2==Nd
                assert e2==ed
                assert q2==qd

    # 61+11 decomposition: the high address bits generate the actual 11 tail
    # parity bits from the base endpoint, with no independent parity choice.
    for N in BUDGET5_STARTS:
        x=N & ((1<<61)-1)
        a=N>>61
        root_bits=direct_bits_from_N(x,61)
        Nr,e,q=canonical_start(root_bits)
        assert Nr==x
        built=Nr
        produced=[]
        for j in range(11):
            t=(a>>j)&1
            built,e,q,b=lift(built,e,q,61+j,t)
            produced.append(b)
        assert built==N
        actual=direct_bits_from_N(N,72)[61:72]
        assert tuple(produced)==actual

    print('PASS MATH-055 exact same-integer address lift transducer')


if __name__=='__main__':
    selftest()
