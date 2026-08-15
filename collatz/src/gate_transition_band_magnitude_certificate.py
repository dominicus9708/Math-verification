#!/usr/bin/env python3
"""Exact transition-band magnitude barrier for the first-return gate cubes.

For the enlarged section
    1^(F-h) B (01/10)^(J-h) 0,
where B is any length-3h word with 2h ones, the remaining pair cube fixes the
low J-h Hensel digits.  The required boundary correction difference is obtained
from the same balanced-Hensel recurrence.  Every possible B-difference is
bounded exactly by
    (2^h-1)(3^(2h)-4^h).
The script certifies the largest h for which every credit 1..397 still violates
that magnitude bound in each G81/G82 neutral/one-slack case.
"""

CASES=(
    ("G81-neutral",404,567,149),
    ("G81-one-slack",402,568,149),
    ("G82-neutral",409,574,150),
    ("G82-one-slack",407,575,151),
)

def boundary_range(h):
    return (2**h-1)*(3**(2*h)-4**h)

def certify(name,F,J,last_impossible):
    q=F+J
    mod0=3**q
    scale=pow(2,2*J+1,mod0)
    inv4=pow(pow(4,J-1,mod0),-1,mod0)
    H=last_impossible+1
    minima=[None]*(H+1)
    args=[None]*(H+1)
    for delta in range(1,398):
        U=(-scale*delta)%mod0
        U=U*inv4%mod0
        m=mod0
        for ell in range(J):
            h=J-ell
            if 1<=h<=H:
                t=pow(2,3*h-2,m)*U%m
                if t>m//2:t-=m
                a=abs(t)
                if minima[h] is None or a<minima[h]:
                    minima[h]=a;args[h]=(delta,t)
            z=U%3
            e=0 if z==0 else (1 if z==1 else -1)
            U=4*((U-e)//3)
            m//=3
            U%=m
    for h in range(1,last_impossible+1):
        assert minima[h]>boundary_range(h),(name,h,minima[h],boundary_range(h))
    # The next h is the first one at which the magnitude test alone no longer
    # proves impossibility; this is not an existence assertion.
    assert minima[H]<=boundary_range(H),(name,H,minima[H],boundary_range(H))
    print(name,"impossible_through",last_impossible,
          "first_magnitude_possible",H,"arg",args[H])

if __name__=="__main__":
    for case in CASES:certify(*case)
