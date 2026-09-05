#!/usr/bin/env python3
"""Numerical constants for the two-exponent global closure criterion.

Let delta_form = 1-H_2(log_3 2).  Suppose

  gamma = limsup_H log2 G_H / H

bounds the nearest whole-prefix root-credit exponent, and

  beta = limsup_H log2 Xi_H / H

bounds the same-address selector amplification exponent relative to the
coefficient-survivor language.

At binary horizon H=c*m, selector extinction by entropy needs

  c (delta_form-beta) > 1,

while root validity from G_H < 3^m needs

  c gamma < log2 3.

A c satisfying both exists iff

  gamma < (delta_form-beta) log2 3.

This is a sufficient budget criterion, not a proof that gamma or beta obey the
required bounds.
"""

import math


def H2(p):
    return -p*math.log2(p)-(1-p)*math.log2(1-p)


def main():
    alpha=math.log(2)/math.log(3)
    delta=1-H2(alpha)
    l23=math.log2(3)
    gamma_if_beta0=delta*l23

    assert 0.0793 < gamma_if_beta0 < 0.0794
    assert abs(gamma_if_beta0-0.07931861277485554)<1e-14

    # Example trade-off points.
    examples=[]
    for gamma in (0.0,0.01,0.02,0.04,0.06):
        beta_max=delta-gamma/l23
        examples.append((gamma,beta_max))
        assert beta_max>0

    print("delta_form=",repr(delta))
    print("log2(3)=",repr(l23))
    print("beta=0 sufficient gamma threshold=",repr(gamma_if_beta0))
    for g,b in examples:
        print("gamma",g,"requires beta <",repr(b))
    print("two-exponent global closure budget: PASS")


if __name__=="__main__":
    main()
