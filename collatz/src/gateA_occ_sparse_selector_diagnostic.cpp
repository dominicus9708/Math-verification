#include <algorithm>
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

struct Block {
    int a, c, L, rises;
};

struct Acc {
    long double in = 0;
    long double full = 0;
    long double valid = 0;
    u64 parents = 0;
};

static std::array<u128, 80> P3{};

int boundary(int k) {
    int q = 0;
    const u128 p2 = u128(1) << k;
    while (P3[q] < p2) ++q;
    return q;
}

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::atoi(argv[1]) : 20;
    if (m < 1 || m > 23) {
        std::cerr << "diagnostic supports 1 <= m <= 23\n";
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
    for (int n = 3; n < H; ++n) {
        if (boundary(n + 1) == boundary(n)) plateaus.push_back(n);
    }

    std::vector<Block> blocks;
    for (std::size_t i = 0; i + 2 < plateaus.size(); ++i) {
        const int a = plateaus[i];
        const int c = plateaus[i + 2];
        const int L = c - a;
        const int rises = boundary(c) - boundary(a);
        if (c <= H && ((L == 5 && rises == 3) || (L == 6 && rises == 4))) {
            blocks.push_back({a, c, L, rises});
        }
    }

    const int threads = omp_get_max_threads();
    std::vector<std::vector<Acc>> local(threads, std::vector<Acc>(blocks.size()));
    const u64 total = 1ULL << m;

#pragma omp parallel
    {
        const int tid = omp_get_thread_num();
        auto& acc = local[tid];

#pragma omp for schedule(static)
        for (u64 mask = 0; mask < total; ++mask) {
            u64 X = p3m[m];
            for (int i = 0; i < m; ++i) {
                if ((mask >> i) & 1ULL) X += p3m[i];
            }

            u128 n = u128(4) * X + 3;
            u64 parity_bits = 0;
            int q[80] = {};
            bool active[80] = {};
            active[0] = true;
            bool alive = true;

            for (int k = 1; k <= H; ++k) {
                const int bit = int(n & 1);
                if (bit) {
                    n = (3 * n + 1) / 2;
                    parity_bits |= 1ULL << (k - 1);
                    q[k] = q[k - 1] + 1;
                } else {
                    n /= 2;
                    q[k] = q[k - 1];
                }

                if (alive && P3[q[k]] < (u128(1) << k)) alive = false;
                active[k] = alive;
            }

            for (std::size_t bi = 0; bi < blocks.size(); ++bi) {
                const auto b = blocks[bi];
                if (!active[b.a]) continue;

                const int d = q[b.a] - boundary(b.a);
                if (d < 0) continue;

                const u64 word = (parity_bits >> b.a) & ((1ULL << b.L) - 1);
                const int ones = __builtin_popcountll(word);
                const long double omega = std::powl(1.5L, d);
                const long double g = std::powl(1.5L, ones - b.rises);

                acc[bi].in += omega;
                acc[bi].full += omega * g;
                if (active[b.c]) acc[bi].valid += omega * g;
                ++acc[bi].parents;
            }
        }
    }

    std::vector<Acc> acc(blocks.size());
    for (int t = 0; t < threads; ++t) {
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            acc[i].in += local[t][i].in;
            acc[i].full += local[t][i].full;
            acc[i].valid += local[t][i].valid;
            acc[i].parents += local[t][i].parents;
        }
    }

    std::cout << std::setprecision(18)
              << "m " << m
              << " atoms " << total
              << " H " << H
              << " first_forced_sparse_parent_depth " << (m + 3)
              << "\n";

    for (std::size_t i = 0; i < blocks.size(); ++i) {
        const auto b = blocks[i];
        const auto a = acc[i];
        if (a.in == 0) continue;

        const long double sigma = std::powl(1.25L, b.L) / std::powl(1.5L, b.rises);
        const long double full_ratio = a.full / a.in;
        const long double valid_ratio = a.valid / a.in;

        std::cout << "BLOCK " << b.a << "->" << b.c
                  << " " << (b.a > m + 2 ? "SPARSE" : "DENSE")
                  << " parents " << a.parents
                  << " sigma " << sigma
                  << " full_selector_ratio " << full_ratio
                  << " coefficient_valid_ratio " << valid_ratio
                  << " signed_phi " << full_ratio / sigma - 1
                  << "\n";
    }

    std::cout << "FINITE_DIAGNOSTIC_ONLY\n";
    return 0;
}
