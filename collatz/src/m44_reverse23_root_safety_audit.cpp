// Audit certificate for m44_reverse23_binary26_cross_mass.cpp.
//
// The reverse sieve starts from y=T^2(N), not from N itself.  For the m=44
// core all starts are 3 mod 4, so the first two accelerated Collatz steps are
// both odd and
//
//     y = T^2(N) = (9 N + 5)/4.
//
// After q inverse-odd steps and E extra inverse-even doublings, any positive
// reverse ancestor has the form
//
//     M = (2^(q+E) y - C)/3^q,   C > 0.
//
// The production reverse23 code tests E <= contraction_budget(q-2).  This is
// exactly the coefficient condition
//
//     2^((q-2)+E) < 3^(q-2),
//
// equivalently
//
//     9*2^(q+E) < 4*3^q.
//
// Thus the two universal odd steps are already accounted for: this is a
// root-level contraction test rather than the invalid inference M<y => M<N.
// This audit also checks the finite +5 term.  Across q=3..25 the largest
// start threshold needed after dropping the favorable -C term is only 41,
// while every m=44 start is >= 4*3^44+3.
//
// Finally it records that the reverse23 filter is nevertheless almost
// statistically neutral with respect to the depth-26 binary coefficient
// language: the conditional survival ratio differs from the ambient reverse
// survival ratio by only about +0.176 ppm.

#include <cassert>
#include <cstdint>
#include <iomanip>
#include <iostream>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static int contraction_budget(int d) {
    if (d <= 0) return -1;
    u128 p3 = 1;
    for (int i = 0; i < d; ++i) p3 *= 3;
    int E = -1;
    while ((u128(1) << (d + E + 1)) < p3) ++E;
    return E;
}

static u128 pow3(int q) {
    u128 x = 1;
    for (int i = 0; i < q; ++i) x *= 3;
    return x;
}

static void print_u128(u128 x) {
    if (x >= 10) print_u128(x / 10);
    std::cout << char('0' + x % 10);
}

int main() {
    const u128 NMIN = 4 * pow3(44) + 3;
    const u128 EXPECTED_NMIN = (u128)3939083608734444931ULL * 1000 + 527;
    assert(NMIN == EXPECTED_NMIN);

    u64 worst_threshold = 0;
    int worst_q = -1;
    int worst_E = -1;

    for (int q = 3; q <= 25; ++q) {
        const int E = contraction_budget(q - 2);
        assert(E >= 0);

        const u128 tw = u128(1) << (q + E);
        const u128 gap = 4 * pow3(q) - 9 * tw;
        assert(gap > 0);

        // Dropping -4C gives the sufficient exact inequality
        //
        //   gap*N > 5*2^(q+E).
        //
        // Smallest positive integer N satisfying the strict inequality:
        const u128 rhs = 5 * tw;
        const u64 threshold = static_cast<u64>(rhs / gap + 1);
        if (threshold > worst_threshold) {
            worst_threshold = threshold;
            worst_q = q;
            worst_E = E;
        }

        assert(gap * NMIN > rhs);
    }

    assert(worst_threshold == 41);
    assert(worst_q == 14);
    assert(worst_E == 7);

    constexpr u64 LOW = u64(1) << 23;
    constexpr u64 REVERSE_KILLED = 299740ULL;
    constexpr u64 REVERSE_ALLOWED_LOW = LOW - REVERSE_KILLED;
    constexpr u64 BINARY_ONLY_MASS = 1087765074138ULL;
    constexpr u64 CROSS_MASS = 1048897463045ULL;

    assert(BINARY_ONLY_MASS - CROSS_MASS == 38867611093ULL);

    // Exact cross-multiplication audit against perfect neutrality.
    const u128 lhs = u128(CROSS_MASS) * LOW;
    const u128 rhs = u128(BINARY_ONLY_MASS) * REVERSE_ALLOWED_LOW;
    assert(lhs > rhs);
    assert(lhs - rhs == (u128)1549966495576ULL);

    const long double ambient_survival =
        (long double)REVERSE_ALLOWED_LOW / (long double)LOW;
    const long double binary_conditioned_survival =
        (long double)CROSS_MASS / (long double)BINARY_ONLY_MASS;
    const long double relative_shift_ppm =
        (binary_conditioned_survival / ambient_survival - 1.0L) * 1.0e6L;

    std::cout << "m44 reverse23 root-safety audit: PASS\n";
    std::cout << "m44_min_start ";
    print_u128(NMIN);
    std::cout << '\n';
    std::cout << "worst_small_start_threshold " << worst_threshold
              << " at_q " << worst_q << " E " << worst_E << '\n';
    std::cout << "reverse_removed_low " << REVERSE_KILLED << '/' << LOW << '\n';
    std::cout << "binary_only_mass " << BINARY_ONLY_MASS << '\n';
    std::cout << "cross_mass " << CROSS_MASS << '\n';
    std::cout << "additional_binary_mass_removed "
              << (BINARY_ONLY_MASS - CROSS_MASS) << '\n';
    std::cout << std::setprecision(18);
    std::cout << "ambient_reverse_survival " << ambient_survival << '\n';
    std::cout << "binary_conditioned_survival "
              << binary_conditioned_survival << '\n';
    std::cout << "relative_shift_ppm " << relative_shift_ppm << '\n';
}
