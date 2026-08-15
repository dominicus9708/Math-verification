#!/usr/bin/env python3
"""Exact neutral-Hensel/global-headroom audit over the first 81-block return.

For each distinct length-19 mechanical factor in blocks b=0,...,81, enumerate
its neutral same-state fibre, build exact Hensel sibling-max witnesses, and
record the smallest multiplicative predecessor factor 3^d/2^t among all local
relations.  Multiply by the exact mechanical block-start coefficient.  Every
locally eliminative factor stays strictly above 3/2 globally.
"""
from fractions import Fraction
from itertools import combinations

L=19


def ceil_alpha_count(t):
    # ceil(t log_3 2) by exact integer powers.
    if t==0: return 0
    # estimate then adjust exactly
    k=(63*t)//100  # safe nearby seed for this finite range
    while 3**k >= 2**t: k-=1
    while 3**(k+1) < 2**t: k+=1
    # irrationality gives strict inequalities; ceil is k+1
    return k+1


def mech_word(start,length=19):
    q0=ceil_alpha_count(start)
    return ''.join(str(ceil_alpha_count(start+i+1)-ceil_alpha_count(start+i))
                   for i in range(length))


def corr(pos):
    R=0
    for p in pos: R=3*R+(1<<p)
    return R


def neutral_fibre(ref):
    q=ref.count('1')
    rc=[]; c=0
    for ch in ref:
        c += ch=='1'; rc.append(c)
    out=[]
    for pos in combinations(range(L),q):
        S=set(pos); c=0; ok=True
        for i in range(L):
            c += i in S
            if c<rc[i]: ok=False; break
        if ok: out.append((pos,corr(pos)))
    return out


def audit_factor(ref):
    F=neutral_fibre(ref); q=ref.count('1')
    p3=[1]
    for _ in range(q+1): p3.append(3*p3[-1])
    mx={}
    for pos,R in F:
        for s in range(1,q):
            d=q-s; td=pos[d-1]+1
            if (1<<td)<=p3[d]: continue
            key=(s,R%p3[s+1])
            old=mx.get(key)
            if old is None or R>old[0]: mx[key]=(R,pos)
    removed=0; best=None
    for pos,R in F:
        local_best=None
        for s in range(1,q):
            d=q-s; base=R%p3[s]; digit=(R//p3[s])%3
            for a in range(3):
                if a==digit: continue
                ent=mx.get((s,base+a*p3[s]))
                if ent is None or ent[0]<=R: continue
                td=ent[1][d-1]+1
                mu=Fraction(3**d,1<<td)
                if local_best is None or mu<local_best: local_best=mu
        if local_best is not None:
            removed+=1
            if best is None or local_best<best: best=local_best
    return len(F),removed,best


def main():
    cache={}
    global_min=None; min_block=None
    first_elim=None
    for b in range(82):
        ref=mech_word(19*b)
        if ref not in cache: cache[ref]=audit_factor(ref)
        size,removed,mu=cache[ref]
        if removed:
            if first_elim is None: first_elim=b
            q0=ceil_alpha_count(19*b)
            coeff=Fraction(3**q0,1<<(19*b))
            prod=coeff*mu
            assert prod>Fraction(3,2)
            if global_min is None or prod<global_min:
                global_min=prod; min_block=(b,ref,size,removed,mu,q0)
    assert len(cache)==20
    assert first_elim==34
    assert min_block[0]==55
    print("distinct_factors",len(cache))
    print("first_eliminative_block",first_elim)
    print("minimum_product_block",min_block[0])
    print("minimum_product_gt_3_over_2",global_min>Fraction(3,2))
    print("minimum_multiplier",min_block[4])
    print("fibre_size",min_block[2],"removed",min_block[3])

if __name__=='__main__': main()
