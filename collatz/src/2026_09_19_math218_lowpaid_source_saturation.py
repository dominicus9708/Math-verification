#!/usr/bin/env python3
"""MATH-218 weighted 73-bit source-saturation certificate."""

ZMIN = {2:1,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:13}

def m(r: int) -> int:
    return (3**r).bit_length() - 1 - r

EXPECTED_W = {2:5,3:7,4:10,5:14,6:17,7:20,8:23,9:26,10:29}
EXPECTED_N = {2:15,3:11,4:8,5:6,6:5,7:4,8:4,9:3,10:3}

def ceil_div(a,b):
    return (a+b-1)//b

def main():
    for r in range(2,11):
        hmin=r+1+m(r)
        W=ZMIN[r]+hmin
        assert W==EXPECTED_W[r], (r,W)
        assert ceil_div(73,W)==EXPECTED_N[r]
        print(r,ZMIN[r],m(r),hmin,W,EXPECTED_N[r])

    assert 3*EXPECTED_W[10] == 87
    assert 15*EXPECTED_W[2] >= 73
    assert 14*EXPECTED_W[2] < 73

    print("PASS MATH-218 weighted source saturation")
    print("r10_three_macro_bits",3*EXPECTED_W[10])
    print("worst_case_macro_count",15)
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
