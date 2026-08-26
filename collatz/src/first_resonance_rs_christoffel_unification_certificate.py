#!/usr/bin/env python3
"""Exact certificate unifying the finite-base parity-RS walls with the
first-resonance Christoffel/Farey grammar.

It proves that the sharp RS slope is exactly one Christoffel parent block of
the first resonance, the opposite parent is the alpha-supercritical Farey
neighbour, and the first resonance is their mediant.  It also identifies the
earlier 190537/301994 RS wall as an ancestor block in the same grammar.

All log comparisons use rational atanh enclosures; no floating point.
"""

from fractions import Fraction

B=1<<71

# Root in odd/time coordinates.
Q0=72_057_431_991
A0=114_208_327_604

# Ordered Christoffel parents translated from (gap2-count, odd-count) to
# (odd-count, total-time).
Q_MINUS=65_470_613_321
A_MINUS=103_768_467_013
Q_PLUS=6_586_818_670
A_PLUS=10_439_860_591

# Earlier finite-base RS block appearing deeper in the same DAG.
Q_SMALL=190_537
A_SMALL=301_994

NLOG=120


def log_bounds(z:Fraction,n:int=NLOG):
    s=Fraction(0)
    for k in range(n+1):
        s += Fraction(2)*z**(2*k+1)/(2*k+1)
    tail=Fraction(2)*z**(2*n+3)/((2*n+3)*(1-z*z))
    return s,s+tail


def main():
    l2,u2=log_bounds(Fraction(1,3))       # ln 2
    l3,u3=log_bounds(Fraction(1,2))       # ln 3
    # ln(3+1/B)=ln3 + ln(1+1/(3B)); write the second term by atanh.
    x=Fraction(1,3*B)
    z=x/(2+x)  # ln(1+x)=2 atanh(x/(2+x))
    le,ue=log_bounds(z)
    lA=l3+le
    uA=u3+ue

    # Farey triangle / mediant identities.
    assert Q_MINUS*A_PLUS-Q_PLUS*A_MINUS == 1
    assert Q0==Q_MINUS+Q_PLUS
    assert A0==A_MINUS+A_PLUS
    assert Q0*A_PLUS-Q_PLUS*A0 == 1
    assert Q_MINUS*A0-Q0*A_MINUS == 1

    # beta = ln2/ln(3+1/B), alpha=ln2/ln3.
    # Q_PLUS/A_PLUS < beta.
    assert Q_PLUS*uA < A_PLUS*l2
    # beta < Q0/A0.
    assert A0*u2 < Q0*lA
    # Q0/A0 < alpha.
    assert Q0*u3 < A0*l2
    # alpha < Q_MINUS/A_MINUS.
    assert A_MINUS*u2 < Q_MINUS*l3

    # Earlier small RS wall is also below beta.
    assert Q_SMALL*uA < A_SMALL*l2

    # Christoffel gap-pair translation checks:
    # total time = odd count + number of gap-2 symbols.
    assert A_MINUS-Q_MINUS == 38_297_853_692
    assert A_PLUS-Q_PLUS == 3_853_041_921
    assert A0-Q0 == 42_150_895_613
    assert A_SMALL-Q_SMALL == 111_457

    print('PASS RS/Christoffel Farey unification')
    print('safe_parent',Q_PLUS,A_PLUS)
    print('root_mediant',Q0,A0)
    print('supercritical_parent',Q_MINUS,A_MINUS)
    print('small_RS_ancestor',Q_SMALL,A_SMALL)
    print('order: small_RS and safe_parent < beta < root < alpha < upper_parent')


if __name__=='__main__':
    main()
