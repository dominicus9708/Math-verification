#!/usr/bin/env python3
"""Exact critical-band classification of all 138 first-resonance
Christoffel/Farey DAG nodes.

For each node (P,Q), interpret Q as odd-event count and A=P+Q as accelerated
time.  With B=2^71 define
    beta = log_{3+1/B}(2),
    alpha = log_3(2).
The certificate proves that every proper DAG node is either RS-safe (Q/A<beta)
or coefficient-supercritical (Q/A>alpha).  The unique node in the open band
(beta,alpha) is the root first resonance itself.

All comparisons use exact rational atanh enclosures; no floating point.
"""

from fractions import Fraction
from math import gcd

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


def parents(p:int,q:int):
    assert 0<p<q and gcd(p,q)==1
    qm=pow(p,-1,q)
    pm=(p*qm-1)//q
    return (pm,qm),(p-pm,q-qm)


def build(p:int,q:int,nodes:dict):
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

    safe=[]
    grey=[]
    supercritical=[]

    for p,q in nodes:
        A=p+q

        # Safe certificate: q/A < beta = ln2/ln(3+1/B).
        if q*uA < A*l2:
            safe.append((p,q))
            continue

        # Supercritical certificate: q/A > alpha = ln2/ln3.
        if A*u2 < q*l3:
            supercritical.append((p,q))
            continue

        # If neither one-sided certificate applies, prove it lies strictly in
        # the critical band.  This must happen only at the root.
        assert A*u2 < q*lA      # beta < q/A
        assert q*u3 < A*l2      # q/A < alpha
        grey.append((p,q))

    assert len(safe)==43
    assert len(supercritical)==94
    assert grey==[(P0,Q0)]

    # Root children are the two decisive parents already identified in the
    # RS/Christoffel unification certificate.
    lo,hi=nodes[(P0,Q0)]
    assert lo==(38_297_853_692,65_470_613_321)
    assert hi==(3_853_041_921,6_586_818_670)
    assert hi in safe
    assert lo in supercritical

    # Earlier RS block is safe and present in the same DAG.
    assert (111_457,190_537) in safe

    print('PASS first-resonance DAG critical-band uniqueness')
    print('total_nodes',len(nodes))
    print('RS_safe_nodes',len(safe))
    print('supercritical_nodes',len(supercritical))
    print('critical_band_nodes',len(grey))
    print('unique_critical_node',grey[0])


if __name__=='__main__':
    main()
