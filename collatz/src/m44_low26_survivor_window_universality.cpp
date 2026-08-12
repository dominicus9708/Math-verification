#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u128 = __uint128_t;

static inline void collatz_step(u128 &n) {
    n = (n & 1) ? (3 * n + 1) / 2 : n / 2;
}

static bool all_k_windows_full(const std::vector<std::uint32_t> &masks,
                               int D, int k) {
    const std::uint32_t patmask = (1u << k) - 1u;
    const int need = 1 << k;
    for (int pos = 0; pos + k <= D; ++pos) {
        std::vector<unsigned char> seen(need, 0);
        int count = 0;
        for (std::uint32_t m : masks) {
            const unsigned p = (m >> pos) & patmask;
            if (!seen[p]) {
                seen[p] = 1;
                ++count;
                if (count == need) break;
            }
        }
        if (count != need) return false;
    }
    return true;
}

int main() {
    constexpr int D = 26;
    constexpr int LIM = 250;
    constexpr std::array<int,4> CUTS{100,150,200,250};
    constexpr std::array<std::uint64_t,4> EXPECTED_COUNTS{
        64411, 6864, 803, 123
    };
    constexpr std::array<int,4> FULL_WINDOW_LENGTHS{11,9,6,4};

    std::array<u128,D> p{};
    p[0] = 1;
    for (int i = 1; i < D; ++i) p[i] = 3 * p[i-1];

    u128 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;
    const u128 base = 4 * p44 + 3;
    const std::uint64_t total = 1ULL << D;

    std::array<std::vector<std::uint32_t>,4> survivors;

#pragma omp parallel
    {
        std::array<std::vector<std::uint32_t>,4> local;

#pragma omp for schedule(static)
        for (std::uint64_t mask = 0; mask < total; ++mask) {
            u128 S = 0;
            std::uint64_t bits = mask;
            while (bits) {
                const unsigned i = __builtin_ctzll(bits);
                S += p[i];
                bits &= bits - 1;
            }

            const u128 n = base + 4 * S;
            u128 x = n;
            int tau = LIM + 1;
            for (int k = 1; k <= LIM; ++k) {
                collatz_step(x);
                if (x < n) {
                    tau = k;
                    break;
                }
            }

            for (std::size_t j = 0; j < CUTS.size(); ++j)
                if (tau > CUTS[j]) local[j].push_back((std::uint32_t)mask);
        }

#pragma omp critical
        {
            for (std::size_t j = 0; j < CUTS.size(); ++j)
                survivors[j].insert(survivors[j].end(),
                                    local[j].begin(), local[j].end());
        }
    }

    for (std::size_t j = 0; j < CUTS.size(); ++j) {
        std::sort(survivors[j].begin(), survivors[j].end());
        if (survivors[j].size() != EXPECTED_COUNTS[j]) {
            std::cerr << "survivor count mismatch at B=" << CUTS[j] << "\n";
            return 1;
        }
        for (int k = 1; k <= FULL_WINDOW_LENGTHS[j]; ++k) {
            if (!all_k_windows_full(survivors[j], D, k)) {
                std::cerr << "window universality mismatch at B=" << CUTS[j]
                          << ", k=" << k << "\n";
                return 1;
            }
        }
        std::cout << "B=" << CUTS[j]
                  << " survivors=" << survivors[j].size()
                  << " all ternary selector windows through length "
                  << FULL_WINDOW_LENGTHS[j]
                  << " occur at every position\n";
    }

    return 0;
}
