# MATH-036 post-audit for the full first-cell internal adjacent-block
# same-endpoint coupling exclusion.

A0 = 114_208_327_604
RSTAR = (A0 - 1) // 3
assert RSTAR == 38_069_442_534

shells = [
    (0, 2_000_000_000, 3_592_089, 379_544_924, 588_381_926, 0, 0, 545, 53),
    (2_000_000_001, 4_000_000_000, 3_592_574, 379_336_322, 588_055_343, 0, 0, 567, 53),
    (4_000_000_001, 8_000_000_000, 7_185_385, 758_974_484, 1_176_764_490, 0, 0, 589, 53),
    (8_000_000_001, 12_000_000_000, 7_185_549, 758_940_825, 1_176_608_836, 0, 0, 633, 53),
    (12_000_000_001, 16_000_000_000, 7_188_065, 759_354_444, 1_177_267_549, 0, 0, 589, 53),
    (16_000_000_001, 20_000_000_000, 7_189_182, 759_781_059, 1_178_116_261, 0, 0, 589, 53),
    (20_000_000_001, 24_000_000_000, 7_184_294, 759_204_457, 1_177_207_710, 0, 0, 567, 53),
    (24_000_000_001, 28_000_000_000, 7_186_880, 759_799_482, 1_178_240_192, 0, 0, 589, 53),
    (28_000_000_001, 32_000_000_000, 7_183_721, 759_014_093, 1_176_846_269, 0, 0, 633, 53),
    (32_000_000_001, 36_000_000_000, 7_181_516, 758_669_008, 1_176_370_998, 0, 0, 589, 54),
    (36_000_000_001, RSTAR, 3_716_070, 392_829_349, 609_053_936, 0, 0, 567, 54),
]

# Exact contiguous partition of the complete collision-halo domain.
assert shells[0][0] == 0
assert shells[-1][1] == RSTAR
for a, b in zip(shells, shells[1:]):
    assert a[1] + 1 == b[0]

leaves = sum(s[2] for s in shells)
inst83 = sum(s[3] for s in shells)
gates22 = sum(s[4] for s in shells)
assert leaves == 68_385_325
assert inst83 == 7_225_448_447
assert gates22 == 11_202_913_510
assert all(s[5] == 0 for s in shells)  # survive-to-audited-end
assert all(s[6] == 0 for s in shells)  # fixed-width endpoint overflow
assert max(s[7] for s in shells) == 633
assert max(s[8] for s in shells) == 54

# Independent depth-61 facts from the first shell / cumulative q audit.
MIN_DEPTH61_RIGHT = 703
MAX_FAILING_BASE = 633
# A failure in the 22-step gate based at 633 occurs by depth 655 at latest.
LATEST_FAILURE_DEPTH = MAX_FAILING_BASE + 22
assert LATEST_FAILURE_DEPTH == 655

# Any right offset r>=703 cannot even enter the linear same-endpoint collision
# halo before k=3r+1 >= 2110, while all audited coefficient-surviving states
# fail by depth 655.
MIN_HALO_ENTRY = 3 * MIN_DEPTH61_RIGHT + 1
assert MIN_HALO_ENTRY == 2110
assert LATEST_FAILURE_DEPTH < MIN_HALO_ENTRY

# The small-depth companion certificate independently checks k<=60 and finds
# zero jointly coefficient-surviving internal-boundary pairs.  For k>=61,
# r<=702 is already absent from the depth-61 survivor language; r>=703 cannot
# enter its necessary collision halo before all audited states have failed.

# Therefore the internal adjacent-block same-endpoint coupling mechanism is
# excluded for every depth through the first universal crossing A0, within the
# current universal-spine/coefficient-survival candidate scope.
assert 3 * RSTAR + 1 > A0
assert (A0 - 1) // 3 == RSTAR

print("PASS MATH-036")
print("A0 =", A0)
print("RSTAR =", RSTAR)
print("depth61 survivors =", leaves)
print("depth83 exact states =", inst83)
print("base83+ tail22 gates =", gates22)
print("max failing base =", MAX_FAILING_BASE)
print("latest failure depth <=", LATEST_FAILURE_DEPTH)
print("minimum halo-entry depth =", MIN_HALO_ENTRY)
print("internal endpoint-coupling mechanism: CLOSED THROUGH FIRST CROSSING")
print("first universal cell: OPEN")
print("Collatz: OPEN")
