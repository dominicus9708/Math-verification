#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>
#include <omp.h>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static std::array<u128, 80> P3{};

int boundary(int k) {
    int q = 0;
    while (P3[q] < (u128(1) << k)) ++q;
    return q;
}

struct Block {
    int a, c;
};

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::atoi(argv[1]) : 22;
    if (m < 1 || m > 23) {
        std::cerr << "supported range: 1 <= m <= 23\n";
        return 2;
    }

    P3[0] = 1;
    for (int i = 1; i < (int)P3.size(); ++i) P3[i] = P3[i - 1] * 3;

    std::vector<u64> p3m(m + 1);
    p3m[0] = 1;
    for (int i = 1; i <= m; ++i) p3m[i] = p3m[i - 1] * 3ULL;

    const u64 xmax = p3m[m] + (p3m[m] - 1) / 2;
    const u64 nmax = 4 * xmax + 3;
    const int H = 64 - __builtin_clzll(nmax);

    std::vector<int> plateaus;
    for (int n = 3; n < H; ++n)
        if (boundary(n + 1) == boundary(n)) plateaus.push_back(n);

    std::vector<Block> blocks;
    for (std::size_t i = 0; i + 2 < plateaus.size(); ++i) {
        const int a = plateaus[i];
        const int c = plateaus[i + 2];
        if (c <= H && a > m + 2) blocks.push_back({a, c});
    }

    constexpr int DMAX = 32;
    constexpr int HMAX = 6;
    using Hist = std::array<std::array<u64, HMAX + 1>, DMAX>;

    const int threads = omp_get_max_threads();
    std::vector<std::vector<Hist>> local(
        threads, std::vector<Hist>(blocks.size()));

    const u64 total = 1ULL << m;

#pragma omp parallel
    {
        const int tid = omp_get_thread_num();

#pragma omp for schedule(static)
        for (u64 mask = 0; mask < total; ++mask) {
            u64 X = p3m[m];
            u64 mm = mask;
            while (mm) {
                const int i = __builtin_ctzll(mm);
                X += p3m[i];
                mm &= mm - 1;
            }

            u128 n = u128(4) * X + 3;
            int q = 0;
            bool alive = true;
            std::array<int, 80> q_alive{};
            q_alive.fill(-1);
            q_alive[0] = 0;
            u64 parity_bits = 0;

            for (int k = 1; k <= H; ++k) {
                const int bit = int(n & 1);
                if (bit) {
                    n = (3 * n + 1) / 2;
                    ++q;
                    parity_bits |= 1ULL << (k - 1);
                } else {
                    n /= 2;
                }

                if (alive && P3[q] < (u128(1) << k)) alive = false;
                if (alive) q_alive[k] = q;
            }

            for (std::size_t bi = 0; bi < blocks.size(); ++bi) {
                const auto b = blocks[bi];
                if (q_alive[b.a] < 0) continue;

                const int d = q_alive[b.a] - boundary(b.a);
                const int L = b.c - b.a;
                const int h = __builtin_popcountll(
                    (parity_bits >> b.a) & ((1ULL << L) - 1));

                if (0 <= d && d < DMAX)
                    ++local[tid][bi][d][h];
            }
        }
    }

    std::cout << std::setprecision(18)
              << "m " << m
              << " atoms " << total
              << " H " << H
              << " first_forced_sparse_parent_depth " << (m + 3)
              << "\n";

    for (std::size_t bi = 0; bi < blocks.size(); ++bi) {
        const auto b = blocks[bi];
        const int rises = boundary(b.c) - boundary(b.a);
        std::cout << "BLOCK " << b.a << "->" << b.c
                  << " L " << (b.c - b.a)
                  << " rises " << rises << "\n";

        for (int d = 0; d < DMAX; ++d) {
            std::array<u64, HMAX + 1> hist{};
            u64 count = 0;
            for (int t = 0; t < threads; ++t) {
                for (int h = 0; h <= HMAX; ++h)
                    hist[h] += local[t][bi][d][h];
            }
            for (u64 x : hist) count += x;
            if (!count) continue;

            long double numerator = 0;
            for (int h = 0; h <= HMAX; ++h)
                numerator += (long double)hist[h] *
                             std::powl(1.5L, h - rises);
            const long double ratio = numerator / count;

            std::cout << "D " << d
                      << " count " << count
                      << " ratio " << ratio;
            for (int h = 0; h <= HMAX; ++h)
                if (hist[h]) std::cout << " h" << h << "=" << hist[h];
            std::cout << "\n";
        }
    }

    std::cout << "FINITE_SURPLUS_STRATIFIED_DIAGNOSTIC_ONLY\n";
    return 0;
}
