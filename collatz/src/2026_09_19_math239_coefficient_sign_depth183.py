#!/usr/bin/env python3
"""MATH-239 exact coefficient-sign descent threshold through depth 183."""

from fractions import Fraction

FLOOR=1<<71
HMAX=183

def threshold(H,Q):
    assert 2**H > 3**Q
    return Fraction(2**(H-Q)*3**Q, 2**H-3**Q)

def main():
    best=None
    checked=0

    for H in range(1,HMAX+1):
        for Q in range(H+1):
            if 2**H > 3**Q:
                t=threshold(H,Q)
                checked+=1
                if best is None or t>best[0]:
                    best=(t,H,Q)

    assert best is not None
    t,H,Q=best
    assert (H,Q)==(176,111)
    assert t < FLOOR

    # The same floor-only sufficient bound first ceases to be universal at 184.
    t184=threshold(184,116)
    assert t184 > FLOOR

    print("checked_pairs",checked)
    print("max_threshold_H_Q",H,Q)
    print("max_threshold",t)
    print("floor",FLOOR)
    print("first_failed_audit_depth_pair",184,116)
    print("threshold_184_116",t184)
    print("PASS MATH-239 coefficient-sign theorem through depth 183")
    print("NO r10 LAYER CLOSURE CLAIM")

if __name__=="__main__":
    main()
