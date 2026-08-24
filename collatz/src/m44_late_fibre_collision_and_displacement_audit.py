# Exact arithmetic audit for the m=44 late-plateau fibre route.
#
# Symbolic theorem used with these constants:
# If X,X' belong to the m=44 selector core, then
#
#     |X-X'| <= diam(C_44) < 2^71.
#
# If Y,Y' lie in one plateau fibre and differ only in coordinates j>=71,
# the least differing coordinate gives
#
#     v_2(Y-Y') >= 71
#
# (and equality to that least coordinate for a nonzero fibre difference).
# Hence
#
#     X-X' + Y-Y' == 0 (mod 2^H)
#
# forces X=X' and Y=Y'.  For uniform measures on C_44 and one K-point late
# fibre, the additive collision probability is therefore exactly 1/(2^44 K).
#
# The second part checks that trying to convert every plateau orientation into
# an ordered-one displacement still cannot close the current resonance: there
# are fewer plateau starts than the already-certified displacement budget.
#
# This is a structural audit/reduction, not a Collatz proof.

M = 44
p44 = 3**M

NMIN = 4*p44 + 3
NMAX = 6*p44 + 1
DIAM = NMAX - NMIN

assert DIAM == 2*p44 - 2
assert DIAM < 2**71
assert 2**71 - DIAM == 391_641_437_067_600_141_088

# Current isolated R1 resonance.
A = 217_976_794_617
H = 137_528_045_312

# For L=A-1, alpha=log_3 2 and this upper-convergent resonance gives
# b_(A-2)=H-1.  Therefore the exact number of deterministic plateau starts is
# (L-1)-b_(L-1)=A-H-1.
PLATEAU_STARTS = A - H - 1
assert PLATEAU_STARTS == 80_448_749_304

# Exact ordered-one displacement ceiling certified previously in
# m44_ordered_one_displacement_budget_certificate.py.
DISPLACEMENT_MAX = 126_613_628_698
assert PLATEAU_STARTS < DISPLACEMENT_MAX
assert DISPLACEMENT_MAX - PLATEAU_STARTS == 46_164_879_394

# Zero-mixed depth-43 near miss, independently checked as exact integer data.
NSTAR = 5_009_655_000_888_502_825_071
t = (NSTAR - 3)//4 - p44
assert (NSTAR - 3) % 4 == 0
assert t == 267_642_848_038_514_473_386

digits = []
z = t
for _ in range(44):
    digits.append(z % 3)
    z //= 3
assert z == 0
assert all(d in (0, 1) for d in digits[:42])
assert digits[42] == 2
assert digits[43] == 0
assert t == 2*3**42 + (t % 3**42)

print('m44 late-fibre collision/displacement audit: PASS')
print('selector diameter =', DIAM)
print('2^71 - diameter =', 2**71 - DIAM)
print('plateau starts at current resonance =', PLATEAU_STARTS)
print('ordered-one displacement ceiling =', DISPLACEMENT_MAX)
print('displacement slack beyond all plateau starts =',
      DISPLACEMENT_MAX - PLATEAU_STARTS)
print('zero-mixed final near-miss digit_42 =', digits[42])
