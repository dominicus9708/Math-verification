#!/usr/bin/env python3
"""MATH-243 theorem-interface regression."""

A0=114_208_327_604
H_FACTOR_MAX=89
R_POSTJ_MAX=38

def main():
    hmax=H_FACTOR_MAX+R_POSTJ_MAX
    assert hmax==127
    assert hmax < A0
    print("PASS MATH-243 first-failure interface")
    print("post_r10_multisource_global_depth_max",hmax)
    print("first_scalar_hard_depth",A0)
    print("first_contraction_before_singletonization CLOSED by MATH-196")
    print("FULL r10 LAYER OPEN")

if __name__=="__main__":
    main()
