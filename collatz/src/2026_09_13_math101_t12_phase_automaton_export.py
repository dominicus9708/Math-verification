#!/usr/bin/env python3
"""MATH-101 stage A: exact phase-danger automaton exporter for macro depth 12."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
HERE=Path(__file__).resolve().parent
S85=spec_from_file_location('m85',HERE/'2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py')
m85=module_from_spec(S85); assert S85.loader is not None; S85.loader.exec_module(m85)
S86=spec_from_file_location('m86',HERE/'2026_09_12_math086_onepaid_phase_horizon_certificate.py')
m86=module_from_spec(S86); assert S86.loader is not None; S86.loader.exec_module(m86)
TARGET=12; LAM=Fraction(19,503); EDGES=m85.EDGES; MEDGES=m86.merged_phase_edges()
def ceil_log2(m): return 0 if m==1 else (m-1).bit_length()
def phase_graph():
    levels={1:m86.initial_phase_states()};adj={};neg={}
    for d in range(1,TARGET):
        cont={};aout=defaultdict(set);bad=set()
        for H,lo,hi,alpha in levels[d]:
            pk=(H,lo,hi)
            for h,elo,ehi,rho,c in MEDGES:
                a=max(lo,elo);b=min(hi,ehi)
                if a>=b: continue
                H2=H+h;lo2=a*rho;hi2=b*rho;alpha2=alpha/rho+c
                if H2>71:
                    margin=alpha2*lo2 if H2<=73 else alpha2*lo2-LAM*(H2-73)
                    if margin<0:bad.add(pk)
                else:
                    ck=(H2,lo2,hi2);old=cont.get(ck)
                    if old is None or alpha2<old:cont[ck]=alpha2
                    aout[pk].add(ck)
        levels[d+1]=[(H,lo,hi,a) for (H,lo,hi),a in cont.items()];adj[d]=aout;neg[d+1]=bad
    danger={TARGET-1:set(neg[TARGET])}
    for d in range(TARGET-2,0,-1):
        wanted=danger[d+1];danger[d]={pk for pk,ch in adj[d].items() if ch&wanted}
    return danger
def merge_danger(danger):
    out={}
    for d,ss in danger.items():
        byH=defaultdict(list)
        for H,lo,hi in ss:byH[H].append((lo,hi))
        for H,ints in byH.items():
            ints.sort();m=[];lo,hi=ints[0]
            for a,b in ints[1:]:
                if a<=hi:hi=max(hi,b)
                else:m.append((lo,hi));lo,hi=a,b
            m.append((lo,hi));byH[H]=m
        out[d]=byH
    return out
PHASE_ID={};PHASE=[]
def phase_id(lo,hi):
    k=(lo,hi)
    if k not in PHASE_ID:PHASE_ID[k]=len(PHASE);PHASE.append(k)
    return PHASE_ID[k]
@lru_cache(None)
def phase_step(pid,ei):
    lo,hi=PHASE[pid];e=EDGES[ei];a=max(lo,e.lo);b=min(hi,e.hi)
    return -1 if a>=b else phase_id(a*e.rho,b*e.rho)
@lru_cache(None)
def inv3(q,bits):
    mod=1<<bits;return pow(pow(3,q,mod),-1,mod)
def main():
    danger=phase_graph();dint=merge_danger(danger)
    def hit(d,H,pid):
        lo,hi=PHASE[pid];return any(max(lo,a)<min(hi,b) for a,b in dint.get(d,{}).get(H,[]))
    @lru_cache(None)
    def candidates(d,H,pid):
        z=[]
        for ei,e in enumerate(EDGES):
            cp=phase_step(pid,ei)
            if cp>=0 and hit(d+1,H+e.H,cp):z.append((ei,cp))
        return tuple(z)
    roots=[]
    for p in m85.initial_states():
        R=ceil_log2(p.count);P=73+R;mod=1<<P;g=inv3(p.Q,P);x=(p.B*g)%mod;pid=phase_id(p.lo,p.hi)
        if hit(1,p.H,pid):roots.append((p.H,p.count,x,g,pid))
    assert len(roots)==193
    levels={1:set((r[0],r[4]) for r in roots)};trans=[]
    for d in range(1,TARGET-1):
        nxt=set()
        for H,pid in levels[d]:
            for ei,cp in candidates(d,H,pid):
                H2=H+EDGES[ei].H;nxt.add((H2,cp));trans.append((d,H,pid,ei,H2,cp))
        levels[d+1]=nxt
    term=[]
    for H,pid in levels[TARGET-1]:
        lo,hi=PHASE[pid]
        for ei,e in enumerate(EDGES):
            if max(lo,e.lo)<min(hi,e.hi):term.append((H,pid,ei))
    for fn,rows in [('t12_edges.tsv',[(i,e.H,e.Q,e.source_A,e.target_B) for i,e in enumerate(EDGES)]),('t12_roots.tsv',[(i,*r) for i,r in enumerate(roots)]),('t12_trans.tsv',trans),('t12_term.tsv',term)]:
        with open(fn,'w') as f:
            for row in rows:f.write('\t'.join(map(str,row))+'\n')
    print('PASS MATH-101 stage A');print('roots',len(roots),'transitions',len(trans),'terminal_phase_edges',len(term),'phase_ids',len(PHASE_ID))
if __name__=='__main__':main()
