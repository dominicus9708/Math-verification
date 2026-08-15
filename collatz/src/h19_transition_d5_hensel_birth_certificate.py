#!/usr/bin/env python3
"""Exact certificate for the first locally Hensel-eliminative H19 phase change.

The last hard length-19 reference block and the immediately following block
differ by one adjacent conjugacy swap.  Enumerate the full neutral fibre of
each block and apply the exact same-state Hensel sibling-max test.
"""
from itertools import combinations

HARD = "1011011010110110101"
NEXT = "1011010110110110101"


def corr(pos):
    R=0
    for p in pos:
        R=3*R+(1<<p)
    return R


def fibre(ref):
    L=len(ref); q=ref.count("1")
    rc=[]; c=0
    for ch in ref:
        c += ch=="1"; rc.append(c)
    out=[]
    for pos in combinations(range(L),q):
        ps=set(pos); c=0; ok=True
        for i in range(L):
            c += i in ps
            if c < rc[i]: ok=False; break
        if ok: out.append((pos,corr(pos)))
    return out


def audit(ref):
    F=fibre(ref); q=ref.count("1")
    p3=[1]
    for _ in range(q+1): p3.append(3*p3[-1])
    partial={}; immediate={}
    for pos,R in F:
        rq=R%p3[q]
        immediate[rq]=max(immediate.get(rq,-1),R)
        for s in range(1,q):
            d=q-s
            td=pos[d-1]+1
            if (1<<td)<=p3[d]: continue
            key=(s,R%p3[s+1])
            partial[key]=max(partial.get(key,-1),R)
    dist={}; removed=0
    for pos,R in F:
        kill=None
        if immediate.get(R%p3[q],-1)>R:
            kill=(q,0)
        if kill is None:
            for s in range(1,q):
                base=R%p3[s]; digit=(R//p3[s])%3
                best=-1
                for a in range(3):
                    if a==digit: continue
                    best=max(best,partial.get((s,base+a*p3[s]),-1))
                if best>R:
                    kill=(s,q-s); break
        if kill is not None:
            removed+=1; dist[kill]=dist.get(kill,0)+1
    return len(F),removed,dist


def odd_times(w):
    return [i+1 for i,ch in enumerate(w) if ch=="1"]


def main():
    assert HARD[:6]+HARD[8:] == NEXT[:6]+NEXT[8:]
    assert HARD[6:8]=="10" and NEXT[6:8]=="01"
    assert odd_times(HARD)[4]==7
    assert odd_times(NEXT)[4]==8
    assert 2**7 < 3**5 < 2**8
    a=audit(HARD); b=audit(NEXT)
    assert a==(8045,0,{})
    assert b==(8640,1608,{(7,5):1608})
    print("hard",a)
    print("next",b)
    print("fifth_odd_times",odd_times(HARD)[4],odd_times(NEXT)[4])

if __name__=="__main__": main()
