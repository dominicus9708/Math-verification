#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <vector>

// Exact finite diagnostic for cumulative neutral occupancy on F_m, 15<=m<=22.
// A step k is called neutral when coefficient survival still holds,
// d_k=q_k-b(k)=2, and the actual parity bit equals the Beatty increment
// delta_k=b(k+1)-b(k).  This is NOT an asymptotic theorem and NOT a Collatz proof.

using u64 = std::uint64_t;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

struct Expected {
    int m;
    int total_neutral;
    int crossing;
    u64 start;
    u64 mask;
};

int main() {
    constexpr int KMAX = 500;
    std::vector<int> b(KMAX + 2);
    cpp_int p3b = 1, p2 = 1;
    int qb = 0;
    for (int k = 0; k <= KMAX + 1; ++k) {
        if (k > 0) p2 <<= 1;
        while (p3b < p2) {
            p3b *= 3;
            ++qb;
        }
        b[k] = qb;
    }
    std::vector<int> delta(KMAX + 1);
    for (int k = 0; k <= KMAX; ++k) delta[k] = b[k + 1] - b[k];

    std::vector<u64> p3(23, 1);
    for (int i = 1; i < 23; ++i) p3[i] = 3ULL * p3[i - 1];

    const Expected exp[] = {
        {15, 42, 194,  57433647ULL,      456ULL},
        {16, 36,  80, 179596447ULL,    11905ULL},
        {17, 35,  96, 695921919ULL,    76454ULL},
        {18, 35, 115,2247650043ULL,   211086ULL},
        {19, 44, 194,4907077359ULL,   129822ULL},
        {20, 62, 219,14127865903ULL,   78299ULL},
        {21, 52, 205,55797999387ULL, 1063982ULL},
        {22, 43, 146,127842295579ULL, 515417ULL},
    };

    const u128 UMAX = ~u128(0);
    std::cout << "m,max_total_neutral,crossing,start,mask\n";

    for (const auto& want : exp) {
        const int m = want.m;
        const std::size_t count = std::size_t(1) << m;
        std::vector<u64> sums(count, 0);
        for (std::size_t mask = 1; mask < count; ++mask) {
            const std::size_t lb = mask & (~mask + 1);
            const int j = __builtin_ctzll(static_cast<u64>(lb));
            sums[mask] = sums[mask ^ lb] + p3[j];
        }

        int best_total = -1;
        int best_cross = -1;
        u64 best_start = 0;
        u64 best_mask = 0;

        for (std::size_t mask = 0; mask < count; ++mask) {
            u128 y = u128(4) * (u128(p3[m]) + sums[mask]) + 3;
            const u64 start = static_cast<u64>(y);
            int q = 0;
            int total_neutral = 0;
            int crossing = -1;

            for (int k = 0; k < KMAX; ++k) {
                const int d = q - b[k];
                if (d < 0) {
                    crossing = k;
                    break;
                }

                const int e = int(y & 1);
                if (d == 2 && e == delta[k]) ++total_neutral;

                if (e) {
                    if (y > (UMAX - 1) / 3) {
                        std::cerr << "u128 overflow guard triggered\n";
                        return 2;
                    }
                    y = (3 * y + 1) >> 1;
                    ++q;
                } else {
                    y >>= 1;
                }
            }

            if (crossing < 0) {
                std::cerr << "finite scan horizon too small at m=" << m << '\n';
                return 3;
            }

            if (total_neutral > best_total) {
                best_total = total_neutral;
                best_cross = crossing;
                best_start = start;
                best_mask = static_cast<u64>(mask);
            }
        }

        std::cout << m << ',' << best_total << ',' << best_cross << ','
                  << best_start << ',' << best_mask << '\n';

        if (best_total != want.total_neutral ||
            best_cross != want.crossing ||
            best_start != want.start ||
            best_mask != want.mask) {
            std::cerr << "regression failure at m=" << m << '\n';
            return 4;
        }
    }

    std::cout << "PASS\n";
    return 0;
}
