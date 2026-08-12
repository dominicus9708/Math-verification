#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

using i64 = std::int64_t;
using u64 = std::uint64_t;

static int ceil_log3_2_times(int k) {
    // Exact integer test: least q with 3^q >= 2^k.
    __uint128_t p3 = 1;
    __uint128_t p2 = (__uint128_t)1 << k;
    int q = 0;
    while (p3 < p2) {
        p3 *= 3;
        ++q;
    }
    return q;
}

static std::vector<unsigned char> coefficient_survivors(int L) {
    const int M = 1 << (L - 2); // reduced Y coordinate, N=4Y+3
    std::vector<unsigned char> out(M, 0);

    for (int r = 0; r < M; ++r) {
        std::uint64_t x = 4ULL * r + 3ULL;
        int q = 0;
        bool ok = true;
        for (int k = 1; k <= L; ++k) {
            if (x & 1ULL) {
                ++q;
                x = (3ULL * x + 1ULL) / 2ULL;
            } else {
                x /= 2ULL;
            }
            if (q < ceil_log3_2_times(k)) {
                ok = false;
                break;
            }
        }
        out[r] = ok ? 1 : 0;
    }
    return out;
}

static std::vector<u64> selector_distribution_mod(int d, int mod_exp) {
    const int M = 1 << mod_exp;
    std::vector<u64> dp(M, 0), nd(M, 0);

    auto powmod3 = [M](int e) {
        int x = 1 % M;
        for (int i = 0; i < e; ++i) x = (3LL * x) % M;
        return x;
    };

    dp[powmod3(44)] = 1;
    for (int i = 0; i < d; ++i) {
        const int w = powmod3(i);
        nd = dp;
        for (int r = 0; r < M; ++r)
            nd[(r + w) & (M - 1)] += dp[r];
        dp.swap(nd);
    }
    return dp;
}

struct Expected {
    int L;
    u64 C;
    u64 Cnext;
    u64 one_child_mass;
    i64 correlation;
};

int main() {
    constexpr int D = 30;
    constexpr int MAX_L = 18;

    // Child modulus for L=18 -> 19 is 2^17.
    const auto dist_max = selector_distribution_mod(D, 17);

    const std::array<Expected, 9> expected{{
        {4,  805306368ULL, 536862784ULL, 536887296ULL,   128},
        {6,  536862784ULL, 436199473ULL, 201326620ULL,    -2},
        {7,  436199473ULL, 318759965ULL, 234879010ULL,    -6},
        {9,  318759965ULL, 268429113ULL, 100661783ULL,    79},
        {11, 268429113ULL, 236972326ULL,  62913083ULL,  -491},
        {12, 236972326ULL, 192409280ULL,  89126073ULL,   -19},
        {14, 192409280ULL, 169732552ULL,  45349421ULL, -4035},
        {15, 169732552ULL, 138537664ULL,  62388740ULL, -1036},
        {17, 138537664ULL, 122792235ULL,  31489378ULL, -1480}
    }};

    for (const auto &e : expected) {
        const int L = e.L;
        const int M = 1 << (L - 2);
        const int childM = 2 * M;

        // Fold the max-resolution distribution to modulus 2M.
        std::vector<u64> cnt2(childM, 0);
        for (int r = 0; r < (int)dist_max.size(); ++r)
            cnt2[r & (childM - 1)] += dist_max[r];

        const auto R = coefficient_survivors(L);
        const auto R2 = coefficient_survivors(L + 1);

        u64 C = 0, Cnext = 0, massD = 0;
        i64 corr = 0;

        for (int r = 0; r < M; ++r) {
            if (!R[r]) continue;

            const u64 c0 = cnt2[r];
            const u64 c1 = cnt2[r + M];
            const u64 c = c0 + c1;
            const i64 u = (i64)c0 - (i64)c1;

            const int b0 = R2[r] ? 1 : 0;
            const int b1 = R2[r + M] ? 1 : 0;
            const int m = b0 + b1;
            const int v = b0 - b1;

            C += c;
            Cnext += b0 * c0 + b1 * c1;
            if (m == 1) {
                massD += c;
                corr += (i64)v * u;
            }
        }

        if (C != e.C || Cnext != e.Cnext ||
            massD != e.one_child_mass || corr != e.correlation) {
            std::cerr << "certificate mismatch at L=" << L << "\n";
            return 1;
        }

        const long double eta = (long double)massD / (long double)C;
        const long double cr = (long double)corr / (long double)massD;
        std::cout << "L=" << L << "->" << (L+1)
                  << " C=" << C
                  << " Cnext=" << Cnext
                  << " one-child-mass=" << massD
                  << " eta=" << (double)eta
                  << " corr=" << corr
                  << " relative-corr=" << (double)cr
                  << "\n";
    }

    // Plateau steps have no one-child coefficient-barrier parents.
    for (int L : {5,8,10,13,16,18}) {
        if (ceil_log3_2_times(L+1) != ceil_log3_2_times(L)) {
            std::cerr << "expected plateau mismatch at L=" << L << "\n";
            return 1;
        }
    }

    return 0;
}
