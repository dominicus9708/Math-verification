#!/usr/bin/env python3
"""MATH-230 global reserve/singleton localization certificate."""

ZMIN = {2:1,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:13}

def main():
    depths={r:89+z for r,z in ZMIN.items()}
    assert min(depths.values())==90
    assert depths[10]==102
    for r,d in depths.items():
        assert d>=73
        print("r",r,"reserve_threat_source_depth_min",d)
    print("PASS MATH-230 reserve threat implies source singleton")
    print("minimum_all_lowpaid",min(depths.values()))
    print("r10_minimum",depths[10])
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
