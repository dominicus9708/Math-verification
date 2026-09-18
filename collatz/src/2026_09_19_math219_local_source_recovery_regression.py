#!/usr/bin/env python3
"""MATH-219 local 73-bit source-recovery regression."""

import random

MASK73=(1<<73)-1

def shortcut(n):
    return n//2 if n%2==0 else (3*n+1)//2

def main():
    random.seed(219)
    checked=0

    for _ in range(5000):
        Y=random.randrange(1,1<<73)
        x=Y
        C=0
        Q=0

        for K in range(73):
            b=x&1
            if b:
                C=3*C+(1<<K)
                Q+=1
            x=shortcut(x)

        inv=pow(pow(3,Q,1<<73),-1,1<<73)
        A=(-C*inv)&MASK73

        assert A==Y
        assert (3**Q*Y+C)==(1<<73)*x
        checked+=1

    print("PASS MATH-219 local 73-bit source recovery")
    print("checked",checked)
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
