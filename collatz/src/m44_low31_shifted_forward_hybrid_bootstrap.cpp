// Exact finite verifier for the shifted half-block A_30 + 4*3^30.
//
// Stage 1: aggregate the 30 free ternary selectors modulo 2^25 and remove
// every dyadic class that has a uniform forward descent by time B<=24.
// Stage 2: enumerate only representatives belonging to surviving classes and
// continue them until they fall below their own start.
//
// This verifier is intended as a finite certificate for the A_31 bootstrap;
// it is not an asymptotic proof of Collatz.

#include <algorithm>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

static std::string to_string_u128(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    constexpr int D = 30;
    constexpr int BMAX = 24;
    constexpr int L = BMAX + 1;
    const u64 M = 1ULL << L;

    u128 p44 = 1, p30 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;
    for (int i = 0; i < 30; ++i) p30 *= 3;

    const u128 SHIFT = 4 * p30;
    const u128 BASE = 4 * p44 + 3 + SHIFT;
    const u128 NMIN = BASE;
    const u128 NMAX = BASE + 2 * (p30 - 1);

    // Exact cyclic subset-sum multiplicities modulo 2^25.
    std::vector<u64> dp(M, 0);
    dp[(u64)(BASE % M)] = 1;
    u64 p = 1;
    for (int i = 0; i < D; ++i) {
        const u64 w = (4 * p) % M;
        std::vector<u64> nd(dp);
        for (u64 r = 0; r < M; ++r) {
            if (dp[r]) nd[(r + w) & (M - 1)] += dp[r];
        }
        dp.swap(nd);
        p = (p * 3) % M;
    }

    std::vector<std::uint8_t> survive(M, 0);
    u64 survivor_mass = 0;

    for (u64 r = 0; r < M; ++r) {
        if (!dp[r]) continue;

        bool killed = false;
        u64 y = r;
        i128 R = 0;
        i128 p3 = 1;

        for (int B = 1; B <= BMAX; ++B) {
            if (y & 1ULL) {
                R = 3 * R + ((i128)1 << (B - 1));
                p3 *= 3;
                y = (3 * y + 1) / 2;
            } else {
                y /= 2;
            }

            const i128 slope = p3 - ((i128)1 << B);
            const i128 testN = slope > 0 ? (i128)NMAX : (i128)NMIN;
            if (slope * testN + R < 0) {
                killed = true;
                break;
            }
        }

        if (!killed) {
            survive[r] = 1;
            survivor_mass += dp[r];
        }
    }

    const u64 total = 1ULL << 30;
    const u64 excluded = total - survivor_mass;

    if (excluded != 1'000'375'609ULL ||
        survivor_mass != 73'366'215ULL) {
        std::cerr << "class certificate mismatch\n";
        return 2;
    }

    // Meet the surviving class mask with actual ternary representatives.
    // Split selectors into 20 low and 10 high digits.
    constexpr int DL = 20;
    constexpr int DH = 10;
    std::vector<u64> pow3(D, 1);
    for (int i = 1; i < D; ++i) pow3[i] = 3 * pow3[i - 1];

    std::vector<u64> low_sum(1ULL << DL, 0);
    for (u64 m = 1; m < (1ULL << DL); ++m) {
        const int b = __builtin_ctzll(m);
        low_sum[m] = low_sum[m & (m - 1)] + pow3[b];
    }

    std::atomic<u64> tested{0};
    std::atomic<u64> failures{0};
    std::atomic<int> max_tau{0};

#pragma omp parallel for schedule(dynamic,1) if(DH >= 1)
    for (int hm = 0; hm < (1 << DH); ++hm) {
        u64 high_sum = 0;
        for (int j = 0; j < DH; ++j) {
            if ((hm >> j) & 1) high_sum += pow3[DL + j];
        }

        const u64 base_res = (u64)((BASE + 4 * (u128)high_sum) % M);

        for (u64 lm = 0; lm < (1ULL << DL); ++lm) {
            const u64 r = (base_res + 4 * (low_sum[lm] % M)) & (M - 1);
            if (!survive[r]) continue;

            tested.fetch_add(1, std::memory_order_relaxed);

            const u128 N = BASE + 4 * (u128)(high_sum + low_sum[lm]);
            u128 x = N;
            int tau = 0;
            bool ok = false;

            for (int k = 1; k <= 2000; ++k) {
                x = (x & 1) ? (3 * x + 1) / 2 : x / 2;
                if (x < N) {
                    tau = k;
                    ok = true;
                    break;
                }
            }

            if (!ok) {
                failures.fetch_add(1, std::memory_order_relaxed);
                continue;
            }

            int old = max_tau.load(std::memory_order_relaxed);
            while (tau > old &&
                   !max_tau.compare_exchange_weak(old, tau,
                                                  std::memory_order_relaxed)) {}
        }
    }

    if (tested.load() != 73'366'215ULL ||
        failures.load() != 0 ||
        max_tau.load() != 525) {
        std::cerr << "trajectory certificate mismatch\n";
        return 3;
    }

    const u128 p31 = 3 * p30;
    const u128 V31 = 4 * (p44 + p31) + 2;

    std::cout << "total shifted representatives: " << total << "\n";
    std::cout << "class excluded: " << excluded << "\n";
    std::cout << "continued fringe: " << tested.load() << "\n";
    std::cout << "failures: " << failures.load() << "\n";
    std::cout << "max first descent: " << max_tau.load() << "\n";
    std::cout << "V31: " << to_string_u128(V31) << "\n";
    return 0;
}
