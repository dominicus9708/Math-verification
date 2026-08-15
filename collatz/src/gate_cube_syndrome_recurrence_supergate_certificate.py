#!/usr/bin/env python3
"""Exact balanced-Hensel syndrome recurrence for G81/G82/G13/G14 cubes.

The recurrence avoids explicit powers 4^j in the lifting loop. For
Z=sum eps_j 3^(J-1-j)4^j and full target T mod 3^(F+J), put
U0=4^(-(J-1))T. If e_l=eps_(J-1-l) is the balanced residue of U_l mod 3,
then U_(l+1)=4(U_l-e_l)/3. After J steps, v3(U_J) is exactly the number
of additional high-syndrome trits matched beyond the free low-J block.
"""
from collections import Counter

CASES = (
    ("G81-neutral", 404, 567, {0:254,1:97,2:32,3:9,4:3,5:2}),
    ("G81-one-slack", 402, 568, {0:266,1:89,2:30,3:8,4:4}),
    ("G82-neutral", 409, 574, {0:259,1:90,2:35,3:8,4:3,6:2}),
    ("G82-one-slack", 407, 575, {0:263,1:95,2:25,3:10,5:3,6:1}),
    ("G13-neutral", 5245, 7390, {0:249,1:106,2:28,3:9,4:2,5:2,7:1}),
    ("G13-one-slack", 5243, 7391, {0:270,1:86,2:27,3:9,4:4,6:1}),
    ("G14-neutral", 5648, 7958, {0:267,1:78,2:34,3:10,4:6,5:1,6:1}),
    ("G14-one-slack", 5646, 7959, {0:264,1:87,2:28,3:11,4:5,5:2}),
)

def v3(x):
    n=0
    while x and x%3==0:
        x//=3; n+=1
    return n

def audit(name,F,J,expected):
    q=F+J
    mod=3**q
    scale=pow(2,2*J+1,mod)
    inv4=pow(pow(4,J-1,mod),-1,mod)
    dist=Counter(); full=[]; max_extra=-1; maximizers=[]
    for delta in range(1,398):
        target=(-scale*delta)%mod
        U=(target*inv4)%mod
        m=mod
        for _ in range(J):
            z=U%3
            e=0 if z==0 else (1 if z==1 else -1)
            U=4*((U-e)//3)
            m//=3
            U%=m
        extra=F if U==0 else v3(U)
        if U==0: full.append(delta)
        dist[extra]+=1
        if extra>max_extra:
            max_extra=extra; maximizers=[delta]
        elif extra==max_extra:
            maximizers.append(delta)
    got=dict(sorted(dist.items()))
    assert not full
    assert got==expected,(name,got,expected)
    print(name,"q",q,"J",J,"F",F,"full",0,
          "max_extra",max_extra,"maximizers",maximizers,"distribution",got)

if __name__=="__main__":
    for case in CASES: audit(*case)
