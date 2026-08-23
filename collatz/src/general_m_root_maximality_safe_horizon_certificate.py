#!/usr/bin/env python3
"""Exact finite/asymptotic certificate for the general-m root-maximality-safe horizon.

For the recursively sufficient depth-m family

    N = 4(3^m + sum_{i=0}^{m-1} a_i 3^i) + 3,
    a_i in {0,1},

every root satisfies N >= N_min(m)=4*3^m+3.

For any coefficient-surviving length-H prefix with q odd steps,

    q >= qmin(H) = min{q:3^q >= 2^H},

and every positive same-q complete-Hensel sibling credit obeys

    d < 2^(H-q) <= 2^(H-qmin(H)).

Thus whole-prefix root maximality is automatically valid whenever

    2^(H-qmin(H)) < N_min(m).

Define Hsafe(m) as the largest H satisfying this inequality for all h<=H.
This script computes Hsafe exactly for m<=500, checks the m=45 regression
Hsafe(45)=200, and verifies the asymptotic linear scale numerically against

    rho = log_2(3)/(1-log_3(2)) ~= 4.29447379207261.

The asymptotic theorem itself is elementary from
floor(log2 N_min)=m log2(3)+O(1) and
H-ceil(H log_3 2)=(1-log_3 2)H+O(1).
This is a root-credit validity theorem, not a Collatz proof.
"""

from decimal import Decimal, getcontext
import math


def qmin(H: int) -> int:
    q=0
    p3=1
    p2=1<<H
    while p3<p2:
        p3*=3
        q+=1
    return q


def nmin(m: int) -> int:
    return 4*3**m+3


def safe(H: int,m: int) -> bool:
    s=H-qmin(H)
    return (1<<s)<nmin(m)


def hsafe(m: int) -> int:
    H=0
    while safe(H+1,m):
        H+=1
    return H


def main() -> None:
    vals={m:hsafe(m) for m in range(1,501)}
    assert vals[45]==200
    assert safe(200,45)
    assert not safe(201,45)
    assert vals[46]==203

    # Hsafe is nondecreasing in m.
    for m in range(1,500):
        assert vals[m+1]>=vals[m]

    # Exact simple envelope from the floor bit length B_m.
    for m,H in vals.items():
        B=nmin(m).bit_length()-1
        assert H-qmin(H)<=B
        assert (H+1)-qmin(H+1)>B

    alpha=math.log(2)/math.log(3)
    rho=math.log2(3)/(1-alpha)

    # Finite convergence diagnostic only; the limit is proved algebraically.
    for m in (50,100,200,300,400,500):
        assert abs(vals[m]/m-rho)<0.20

    print("m=45 Hsafe=",vals[45])
    print("m=46 Hsafe=",vals[46])
    print("m=100 Hsafe=",vals[100])
    print("m=500 Hsafe=",vals[500])
    print("rho=",repr(rho))
    print("general-m root maximality safe-horizon certificate: PASS")


if __name__=="__main__":
    main()
