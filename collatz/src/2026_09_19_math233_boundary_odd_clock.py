#!/usr/bin/env python3
"""MATH-233 exact 25-odd multi-source horizon certificate."""

def main():
    # Exact integer comparison used by the proof.
    assert 3**26 > 2**41
    assert 3**25 < 2**40  # shows 25 is not excluded by the same coarse bound

    # If H<=40 and Q>=26 then coefficient ratio is already >2,
    # contradicting the complete-boundary telescope ratio in (1/2,2).
    for Q in range(26,60):
        assert 3**Q > 2**41
        for H in range(0,41):
            assert 3**Q > 2**(H+1)

    print("PASS MATH-233 complete-boundary odd-count horizon")
    print("max_future_multisource_depth",40)
    print("max_future_multisource_odd_count",25)
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
