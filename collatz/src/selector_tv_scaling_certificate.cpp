#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

// Exact finite calibration for the reduced ternary-selector distribution
//
//     S_m = sum_{i=0}^{m-1} a_i 3^i  (mod 2^L),  a_i in {0,1}.
//
// The goal is to measure how the selector distribution approaches the uniform
// distribution on dyadic residue classes as the selector surplus m-L grows.
// This is directly relevant to the unconditional Stage 4 cross-base
// transversality program after the 2026-08-20 Stage 3C correction.
//
// Every count is an exact integer. For m>=L the uniform mean is 2^(m-L), and
//
//     TV = sum_r |c(r)-mean| / 2^(m+1).
//
// These checkpoints are finite calibrations only; they do not prove a general
// exponential or subexponential mixing theorem.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

struct Check {
    int L;
    int m;
    u64 l1;
    u64 minc;
    u64 maxc;
};

static std::string s128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + unsigned(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static void run_one(const Check& e) {
    const u64 N = 1ULL << e.L;
    const u64 mask = N - 1;
    std::vector<u64> dp(N, 0), nd(N, 0);
    dp[0] = 1;

    u64 w = 1;
    for (int i = 0; i < e.m; ++i) {
        for (u64 r = 0; r < N; ++r)
            nd[r] = dp[r] + dp[(r - w) & mask];
        dp.swap(nd);
        w = (3 * w) & mask;
    }

    const u64 mean = 1ULL << (e.m - e.L);
    u128 l1 = 0;
    u64 minc = ~u64(0), maxc = 0, maxdev = 0, total = 0;

    for (u64 c : dp) {
        total += c;
        minc = std::min(minc, c);
        maxc = std::max(maxc, c);
        const u64 d = c >= mean ? c - mean : mean - c;
        l1 += d;
        maxdev = std::max(maxdev, d);
    }

    if (total != (1ULL << e.m)) std::exit(1);
    if (l1 != e.l1 || minc != e.minc || maxc != e.maxc) std::exit(2);

    std::cout << "L=" << e.L
              << " m=" << e.m
              << " mean=" << mean
              << " L1=" << s128(l1)
              << " TV_den=2^" << (e.m + 1)
              << " min=" << minc
              << " max=" << maxc
              << " maxdev=" << maxdev << "\n";
}

int main() {
    const std::array<Check, 8> checks{{
        {10,20,6272ULL,996ULL,1043ULL},
        {12,22,63860ULL,965ULL,1086ULL},
        {14,24,182140ULL,976ULL,1072ULL},
        {16,26,983172ULL,922ULL,1101ULL},
        {18,28,9183916ULL,856ULL,1225ULL},
        {18,30,17778520ULL,3777ULL,4415ULL},
        {18,34,56964792ULL,64313ULL,66558ULL},
        {18,38,176766780ULL,1044941ULL,1052020ULL},
    }};

    for (const auto& e : checks) run_one(e);
    std::cout << "selector TV scaling certificate: PASS\n";
    return 0;
}
