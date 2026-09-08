// MATH-043 post-audit for the independently run q=21..33 layers.
// This file does not recompute class maxima; it verifies the exact layer ledger
// and the transition from the MATH-042 depth-32 survivor distribution.
// Collatz and the first universal Farey cell remain OPEN.

#include <cassert>
#include <cstdint>
#include <iostream>
using u64 = uint64_t;

int main() {
    const u64 s32[34] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        10924522ULL,10653576ULL,6934804ULL,3427766ULL,1360759ULL,
        438144ULL,113563ULL,23221ULL,3620ULL,405ULL,30ULL,1ULL,0
    };

    const u64 coeff33[34] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        13472296ULL,26521599ULL,21471423ULL,12540223ULL,5731598ULL,
        2124991ULL,641665ULL,156239ULL,30038ULL,4400ULL,462ULL,31ULL,1ULL
    };

    const u64 survive33[34] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        10907449ULL,21566825ULL,17584670ULL,10361536ULL,4788202ULL,
        1798808ULL,551671ULL,136784ULL,26841ULL,4025ULL,434ULL,31ULL,1ULL
    };

    u64 coeff_total = 0, survive_total = 0;
    u64 nested_prefilter_total = 0, newly_pruned = 0;

    for (int q = 21; q <= 33; ++q) {
        coeff_total += coeff33[q];
        survive_total += survive33[q];

        u64 pre = s32[q] + s32[q - 1];
        nested_prefilter_total += pre;
        assert(pre >= survive33[q]);
        newly_pruned += pre - survive33[q];
    }

    assert(coeff_total == 82694966ULL);
    assert(survive_total == 67727277ULL);
    assert(coeff_total - survive_total == 14967689ULL);

    // q_min(33)=21, and every MATH-042 survivor already has q>=21, so both
    // even and odd children pass the coefficient gate at depth 33.
    assert(nested_prefilter_total == 2ULL * 33880411ULL);
    assert(nested_prefilter_total == 67760822ULL);
    assert(newly_pruned == 33545ULL);

    cout << "depth33 coefficient = 82694966\n";
    cout << "depth33 all-prefix one-sided Hensel-max survivors = 67727277\n";
    cout << "depth33 cumulative Hensel-removed = 14967689\n";
    cout << "depth33 nested prefilter from MATH-042 = 67760822\n";
    cout << "depth33 newly Hensel-pruned = 33545\n";
    cout << "FINITE EXACT ledger audit PASS; first cell and Collatz remain OPEN.\n";
}
