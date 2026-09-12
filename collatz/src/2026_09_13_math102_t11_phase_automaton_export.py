#!/usr/bin/env python3
# MATH-102 stage A: exact phase-danger automaton exporter for one-paid t=11.
# Same construction as MATH-100/101; only TARGET and canonical root count change.
from pathlib import Path
from importlib.util import module_from_spec,spec_from_file_location
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
HERE=Path(__file__).resolve().parent
S85=spec_from_file_location('m85',HERE/'2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py');m85=module_from_spec(S85);S85.loader.exec_module(m85)
S86=spec_from_file_location('m86',HERE/'2026_09_12_math086_onepaid_phase_horizon_certificate.py');m86=module_from_spec(S86);S86.loader.exec_module(m86)
TARGET=11;LAM=Fraction(19,503);EDGES=m85.EDGES;MEDGES=m86.merged_phase_edges()
def clog(m):return 0 if m==1 else (m-1).bit_length()
def graph():
 L={1:m86.initial_phase_states()};A={};N={}
 for d in range(1,TARGET):
  C={};O=defaultdict(set);B=set()
  for H,lo,hi,a0 in L[d]:
   pk=(H,lo,hi)
   for h,el,eh,r,c in MEDGES:
    x=max(lo,el);y=min(hi,eh)
    if x>=y:continue
    H2=H+h;l2=x*r;u2=y*r;a2=a0/r+c
    if H2>71:
     m=a2*l2 if H2<=73 else a2*l2-LAM*(H2-73)
     if m<0:B.add(pk)
    else:
     ck=(H2,l2,u2);old=C.get(ck)
     if old is None or a2<old:C[ck]=a2
     O[pk].add(ck)
  L[d+1]=[(H,l,u,a) for (H,l,u),a in C.items()];A[d]=O;N[d+1]=B
 D={TARGET-1:set(N[TARGET])}
 for d in range(TARGET-2,0,-1):D[d]={p for p,ch in A[d].items() if ch&D[d+1]}
 return D
def merge(D):
 out={}
 for d,S in D.items():
  Hs=defaultdict(list)
  for H,l,u in S:Hs[H].append((l,u))
  for H,I in Hs.items():
   I.sort();q=[];l,u=I[0]
   for a,b in I[1:]:
    if a<=u:u=max(u,b)
    else:q.append((l,u));l,u=a,b
   q.append((l,u));Hs[H]=q
  out[d]=Hs
 return out
PID={};PH=[]
def pid(l,u):
 k=(l,u)
 if k not in PID:PID[k]=len(PH);PH.append(k)
 return PID[k]
@lru_cache(None)
def step(p,e):
 l,u=PH[p];E=EDGES[e];a=max(l,E.lo);b=min(u,E.hi)
 return -1 if a>=b else pid(a*E.rho,b*E.rho)
@lru_cache(None)
def inv3(q,b):
 m=1<<b;return pow(pow(3,q,m),-1,m)
def main():
 D=merge(graph())
 def hit(d,H,p):
  l,u=PH[p];return any(max(l,a)<min(u,b) for a,b in D.get(d,{}).get(H,[]))
 @lru_cache(None)
 def cand(d,H,p):return tuple((i,cp) for i,E in enumerate(EDGES) if (cp:=step(p,i))>=0 and hit(d+1,H+E.H,cp))
 roots=[]
 for s in m85.initial_states():
  R=clog(s.count);P=73+R;m=1<<P;g=inv3(s.Q,P);x=s.B*g%m;p=pid(s.lo,s.hi)
  if hit(1,s.H,p):roots.append((s.H,s.count,x,g,p))
 assert len(roots)==254
 levels={1:set((r[0],r[4]) for r in roots)};tr=[]
 for d in range(1,TARGET-1):
  nx=set()
  for H,p in levels[d]:
   for ei,cp in cand(d,H,p):nx.add((H+EDGES[ei].H,cp));tr.append((d,H,p,ei,H+EDGES[ei].H,cp))
  levels[d+1]=nx
 te=[]
 for H,p in levels[TARGET-1]:
  l,u=PH[p]
  for i,E in enumerate(EDGES):
   if max(l,E.lo)<min(u,E.hi):te.append((H,p,i))
 for fn,rows in [('t11_edges.tsv',[(i,e.H,e.Q,e.source_A,e.target_B) for i,e in enumerate(EDGES)]),('t11_roots.tsv',[(i,*r) for i,r in enumerate(roots)]),('t11_trans.tsv',tr),('t11_term.tsv',te)]:
  with open(fn,'w') as f:
   for row in rows:f.write('\t'.join(map(str,row))+'\n')
 print('PASS MATH-102 stage A',len(roots),len(tr),len(te),len(PID))
if __name__=='__main__':main()
