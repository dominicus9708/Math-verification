#!/usr/bin/env python3
"""Finite regression for MATH-124 direct parity-word AP addressing."""


def T(n: int) -> int:
    return n//2 if n % 2 == 0 else (3*n+1)//2


def bits_of(n: int, d: int):
    out=[]
    x=n
    for _ in range(d):
        out.append(x & 1)
        x=T(x)
    return tuple(out),x


def descriptor(bits):
    q=0
    c=0
    for i,bit in enumerate(bits):
        if bit:
            c=3*c+(1<<i)
            q+=1
    d=len(bits)
    mod=1<<d
    rw=(-c*pow(pow(3,q,mod),-1,mod))%mod
    return q,c,rw


def main():
    word_cases=0
    ap_cases=0
    for d in range(1,9):
        residues=set()
        mod=1<<d
        for mask in range(mod):
            bits=tuple((mask>>i)&1 for i in range(d))
            q,c,rw=descriptor(bits)
            got,_=bits_of(rw,d)
            assert got==bits
            residues.add(rw)
            word_cases+=1
        assert len(residues)==mod

        for a in range(1,20):
            for b in range(1,12,2):
                for m in range(1,18):
                    for mask in range(mod):
                        bits=tuple((mask>>i)&1 for i in range(d))
                        q,c,rw=descriptor(bits)
                        kappa=((rw-a)*pow(b,-1,mod))%mod
                        ks=list(range(kappa,m,mod)) if kappa<m else []
                        brute=[]
                        for k in range(m):
                            n=a+b*k
                            got,x=bits_of(n,d)
                            if got==bits:
                                brute.append((k,x))
                        assert [k for k,_ in brute]==ks
                        if ks:
                            mw=(m-1-kappa)//mod+1
                            Aw=((3**q)*(a+b*kappa)+c)//mod
                            Bw=(3**q)*b
                            direct=[Aw+Bw*s for s in range(mw)]
                            assert [x for _,x in brute]==direct
                            assert mw==len(ks)
                        ap_cases+=1
    print('word_cases',word_cases)
    print('ap_word_cases',ap_cases)
    print('PASS MATH-124 direct parity-word AP address regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__=='__main__':
    main()
