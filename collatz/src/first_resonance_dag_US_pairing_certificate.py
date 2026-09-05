#!/usr/bin/env python3
"""Exact U*S pairing certificate for every internal node of the first-resonance
Christoffel/Farey DAG.

U = coefficient-supercritical: Q/(P+Q) > alpha=log_3 2.
S = finite-base RS-safe:       Q/(P+Q) < beta=log_{3+2^-71} 2.
G = critical band:             beta < Q/(P+Q) < alpha.

The certificate proves that every one of the 136 internal nodes, including the
unique grey root, has ordered children (U,S).  Thus the entire exact grammar is
a recursive expansion-then-contraction pairing.
"""

from fractions import Fraction
from math import gcd
from collections import Counter

B=1<<71
P0=42_150_895_613
Q0=72_057_431_991
NLOG=120


def log_bounds(z:Fraction,n:int=NLOG):
    s=Fraction(0)
    for k in range(n+1):
        s += Fraction(2)*z**(2*k+1)/(2*k+1)
    tail=Fraction(2)*z**(2*n+3)/((2*n+3)*(1-z*z))
    return s,s+tail


def parents(p,q):
    assert 0<p<q and gcd(p,q)==1
    qm=pow(p,-1,q)
    pm=(p*qm-1)//q
    return (pm,qm),(p-pm,q-qm)


def build(p,q,nodes):
    if (p,q) in nodes:
        return
    if (p,q) in ((0,1),(1,1)):
        nodes[(p,q)]=None
        return
    lo,hi=parents(p,q)
    nodes[(p,q)]=(lo,hi)
    build(*lo,nodes)
    build(*hi,nodes)


def main():
    l2,u2=log_bounds(Fraction(1,3))
    l3,u3=log_bounds(Fraction(1,2))
    x=Fraction(1,3*B)
    z=x/(2+x)
    le,ue=log_bounds(z)
    lA=l3+le
    uA=u3+ue

    nodes={}
    build(P0,Q0,nodes)
    assert len(nodes)==138

    def kind(node):
        p,q=node
        A=p+q
        if q*uA < A*l2:
            return 'S'
        if A*u2 < q*l3:
            return 'U'
        assert A*u2 < q*lA
        assert q*u3 < A*l2
        return 'G'

    counts=Counter()
    internal=0
    for node,ch in nodes.items():
        if ch is None:
            continue
        internal += 1
        k=kind(node)
        kl=kind(ch[0])
        kr=kind(ch[1])
        assert (kl,kr)==('U','S')
        counts[(k,kl,kr)] += 1

    assert internal==136
    assert counts==Counter({
        ('U','U','S'):93,
        ('S','U','S'):42,
        ('G','U','S'):1,
    })

    # Base leaves themselves occupy the two decided sides.
    assert kind((0,1))=='U'
    assert kind((1,1))=='S'

    print('PASS first-resonance recursive U*S pairing')
    print('internal_nodes',internal)
    print('U_parents',counts[('U','U','S')])
    print('S_parents',counts[('S','U','S')])
    print('G_parents',counts[('G','U','S')])
    print('every internal node factors in anchored order U then S')


if __name__=='__main__':
    main()
