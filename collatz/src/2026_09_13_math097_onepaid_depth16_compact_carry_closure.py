#!/usr/bin/env python3
"""MATH-097: exact compact-carry closure of one-paid macro depth 16.

Architecture
------------
1. Build the address-forgotten MATH-086 lower-envelope phase language through
   macro depth 16 and mark the backward corridor that can reach a negative
   depth-16 terminal crossing.
2. Restore actual same-integer states only inside that corridor.
3. Replace the large integer pair (B,Q) by the exact MATH-096 finite state

       R=ceil(log2 M), P=73+R,
       X=3^{-Q}B mod 2^P,
       G=3^{-Q}   mod 2^P.

   Multi-edge propagation is the normalized MATH-092 transducer and retains
   exact source multiplicity M.
4. At macro depth 16 use p>1/9 on every one-paid macro.  Therefore a negative
   terminal Bellman margin can exist only if

       z=h-R >= 48,

   because (16/9)/(19/503)=8048/171 in (47,48).
5. Exhaust every phase-compatible z>=48 canonical terminal edge.  None is
   compatible with the exact compact dyadic address.

Finite exact arithmetic only.  This closes depth-16 singleton handoffs for the
one-paid Bellman search; it is not an ordinary Collatz descent theorem.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
S85=spec_from_file_location('m85',HERE/'2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py')
m85=module_from_spec(S85); assert S85.loader is not None; S85.loader.exec_module(m85)
S86=spec_from_file_location('m86',HERE/'2026_09_12_math086_onepaid_phase_horizon_certificate.py')
m86=module_from_spec(S86); assert S86.loader is not None; S86.loader.exec_module(m86)

LAM=Fraction(19,503)
TARGET=16
EDGES=m85.EDGES
MEDGES=m86.merged_phase_edges()


def ceil_log2(m:int)->int:
    assert m>=1
    return 0 if m==1 else (m-1).bit_length()


# ---------- phase-only lower envelope and backward danger corridor ----------

def phase_levels_and_adjacency():
    levels={1:m86.initial_phase_states()}
    adjacency={}
    negative_cross_parents={}
    for d in range(1,TARGET):
        cont={}
        adj=defaultdict(set)
        neg=set()
        for H,lo,hi,alpha in levels[d]:
            pk=(H,lo,hi)
            for h,elo,ehi,rho,c in MEDGES:
                a=max(lo,elo); b=min(hi,ehi)
                if a>=b: continue
                H2=H+h
                lo2=a*rho; hi2=b*rho
                alpha2=alpha/rho+c
                if H2>71:
                    margin=alpha2*lo2 if H2<=73 else alpha2*lo2-LAM*(H2-73)
                    if margin<0:
                        neg.add(pk)
                else:
                    ck=(H2,lo2,hi2)
                    old=cont.get(ck)
                    if old is None or alpha2<old:
                        cont[ck]=alpha2
                    adj[pk].add(ck)
        levels[d+1]=[(H,lo,hi,a) for (H,lo,hi),a in cont.items()]
        adjacency[d]=adj
        negative_cross_parents[d+1]=neg
    return levels,adjacency,negative_cross_parents


def backward_corridor(adjacency,negative_cross_parents):
    danger={TARGET-1:set(negative_cross_parents[TARGET])}
    for d in range(TARGET-2,0,-1):
        wanted=danger[d+1]
        parents=set()
        for pk,children in adjacency[d].items():
            if children & wanted:
                parents.add(pk)
        danger[d]=parents
    return danger


def merged_danger_intervals(danger):
    out={}
    for d,states in danger.items():
        byH=defaultdict(list)
        for H,lo,hi in states:
            byH[H].append((lo,hi))
        for H,ints in byH.items():
            ints.sort(); merged=[]
            lo,hi=ints[0]
            for a,b in ints[1:]:
                if a<=hi:
                    hi=max(hi,b)
                else:
                    merged.append((lo,hi)); lo,hi=a,b
            merged.append((lo,hi))
            byH[H]=merged
        out[d]=byH
    return out


# ---------- exact phase interval interning ----------
PHASE_ID={}
PHASE=[]

def phase_id(lo,hi):
    key=(lo,hi)
    if key not in PHASE_ID:
        PHASE_ID[key]=len(PHASE); PHASE.append(key)
    return PHASE_ID[key]


@lru_cache(maxsize=None)
def phase_step(pid,ei):
    lo,hi=PHASE[pid]; e=EDGES[ei]
    a=max(lo,e.lo); b=min(hi,e.hi)
    if a>=b: return -1
    return phase_id(a*e.rho,b*e.rho)


@lru_cache(maxsize=None)
def inv3(q,bits):
    mod=1<<bits
    return pow(pow(3,q,mod),-1,mod)


# ---------- compact normalized address transducer ----------

def compact_initial_states(danger_intervals):
    out=set()
    for p in m85.initial_states():
        R=ceil_log2(p.count); P=73+R; mask=(1<<P)-1
        g=inv3(p.Q,P)
        x=(p.B*g)&mask
        pid=phase_id(p.lo,p.hi)
        if interval_hits(danger_intervals,1,p.H,pid):
            out.add((p.H,p.count,x,g,pid))
    return out


def interval_hits(danger_intervals,d,H,pid):
    lo,hi=PHASE[pid]
    for a,b in danger_intervals.get(d,{}).get(H,[]):
        if max(lo,a)<min(hi,b):
            return True
    return False


def multi_child(st,ei,cpid):
    Htot,M,x,g,_=st; e=EDGES[ei]
    R=ceil_log2(M); P=73+R; maskP=(1<<P)-1
    eta=(g*e.source_A)&maskP
    r=(eta-x)&((1<<e.H)-1)
    if r>=M: return None
    Mp=(M-1-r)//(1<<e.H)+1
    if Mp<=1: return None
    Rp=ceil_log2(Mp)
    assert Rp<=R-e.H
    delta=(x+r-eta)&maskP
    assert delta%(1<<e.H)==0
    Pav=P-e.H; maskA=(1<<Pav)-1
    high=(delta>>e.H)&maskA
    gq=(g*inv3(e.Q,Pav))&maskA
    xq=(high+gq*e.target_B)&maskA
    Pp=73+Rp; maskp=(1<<Pp)-1
    return (Htot+e.H,Mp,xq&maskp,gq&maskp,cpid)


def run():
    _,adj,neg=phase_levels_and_adjacency()
    danger=backward_corridor(adj,neg)
    expected_danger={1:26,2:101,3:169,4:206,5:233,6:280,7:314,8:361,
                     9:399,10:421,11:472,12:504,13:554,14:589,15:588}
    assert {d:len(s) for d,s in danger.items()}==expected_danger
    dint=merged_danger_intervals(danger)

    @lru_cache(maxsize=None)
    def candidate_edges(d,H,pid):
        out=[]
        for ei,e in enumerate(EDGES):
            cpid=phase_step(pid,ei)
            if cpid<0: continue
            if interval_hits(dint,d+1,H+e.H,cpid):
                out.append((ei,cpid))
        return tuple(out)

    current=compact_initial_states(dint)
    expected={1:61,2:285,3:1112,4:3045,5:6766,6:17673,7:37189,
              8:85681,9:167405,10:270430,11:566240,12:1004752,
              13:1971140,14:3412980,15:2460473}
    assert len(current)==expected[1]

    for d in range(1,TARGET-1):
        nxt=set()
        for st in current:
            for ei,cpid in candidate_edges(d,st[0],st[4]):
                z=multi_child(st,ei,cpid)
                if z is not None:
                    nxt.add(z)
        current=nxt
        assert len(current)==expected[d+1],(d+1,len(current))
        print('depth',d+1,'compact_states',len(current))

    # Strong universal terminal filter.  Since every macro pays >1/9,
    # negative total reduced cost at t=16 requires z>=48.
    assert Fraction(47,1) < Fraction(16,9)/LAM < Fraction(48,1)

    tries=compatible=0
    min_gap=None
    for Htot,M,x,g,pid in current:
        R=ceil_log2(M); P=73+R; maskP=(1<<P)-1
        lo,hi=PHASE[pid]
        for e in EDGES:
            if e.H-R<48: continue
            if max(lo,e.lo)>=min(hi,e.hi): continue
            tries+=1
            eta=(g*e.source_A)&maskP
            r=(eta-x)&((1<<e.H)-1)
            gap=r-M
            if min_gap is None or gap<min_gap: min_gap=gap
            if r<M:
                compatible+=1

    assert tries==45_094_414
    assert compatible==0
    assert min_gap==197_239_627
    print('terminal_danger_attempts',tries)
    print('address_compatible',compatible)
    print('minimum_r_minus_M',min_gap)
    print('PASS MATH-097 one-paid macro depth 16 Bellman closure')


if __name__=='__main__':
    run()
