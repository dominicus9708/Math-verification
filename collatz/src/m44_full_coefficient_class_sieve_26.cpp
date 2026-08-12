#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static int barrier(int k) {
    // Least q with 3^q >= 2^k, exact integer arithmetic.
    u128 p3 = 1;
    const u128 p2 = u128(1) << k;
    int q = 0;
    while (p3 < p2) {
        p3 *= 3;
        ++q;
    }
    return q;
}

static bool coefficient_survives(u64 reduced_y, int L, int *q_out=nullptr) {
    // N = 4Y+3; low L bits are fixed by Y mod 2^(L-2).
    u64 x = 4 * reduced_y + 3;
    int q = 0;
    for (int k = 1; k <= L; ++k) {
        if (x & 1ULL) {
            ++q;
            x = (3 * x + 1) / 2;
        } else {
            x /= 2;
        }
        if (q < barrier(k)) return false;
    }
    if (q_out) *q_out = q;
    return true;
}

static u64 pow3_mod(int e, u64 M) {
    u64 x = 1 % M;
    for (int i = 0; i < e; ++i) x = (3 * x) & (M - 1);
    return x;
}

int main() {
    constexpr int D = 44;
    constexpr int LMAX = 26;
    constexpr int MEXP = LMAX - 2;
    constexpr u64 MMAX = 1ULL << MEXP;
    constexpr u64 TOTAL = 1ULL << D;

    // Exact subset-sum count distribution of
    // Y = 3^44 + sum_{i=0}^{43} a_i 3^i mod 2^24.
    std::vector<u64> dp(MMAX, 0), nd(MMAX, 0);
    dp[pow3_mod(44, MMAX)] = 1;

    for (int i = 0; i < D; ++i) {
        const u64 w = pow3_mod(i, MMAX);
        nd = dp;
        for (u64 r = 0; r < MMAX; ++r)
            nd[(r + w) & (MMAX - 1)] += dp[r];
        dp.swap(nd);
    }

    u64 check_total = 0;
    for (u64 c : dp) check_total += c;
    if (check_total != TOTAL) {
        std::cerr << "subset-sum total mismatch\n";
        return 1;
    }

    struct Row { int L; u64 classes; u64 mass; };
    const std::array<Row, 7> expected{{
        {18, 7495ULL,    2011923507477ULL},
        {20, 27328ULL,   1833950905184ULL},
        {21, 46611ULL,   1564005133050ULL},
        {23, 168807ULL,  1416055503075ULL},
        {24, 286581ULL,  1202007610492ULL},
        {25, 573162ULL,  1202007610492ULL},
        {26, 1037374ULL, 1087765074138ULL}
    }};

    for (const auto &e : expected) {
        const u64 M = 1ULL << (e.L - 2);
        const u64 fold = MMAX / M;

        std::vector<unsigned char> alive(M, 0);
        u64 classes = 0;
        for (u64 r = 0; r < M; ++r) {
            if (coefficient_survives(r, e.L)) {
                alive[r] = 1;
                ++classes;
            }
        }

        u64 mass = 0;
        for (u64 r = 0; r < MMAX; ++r)
            if (alive[r & (M - 1)]) mass += dp[r];

        if (classes != e.classes || mass != e.mass) {
            std::cerr << "certificate mismatch at L=" << e.L << "\n";
            return 1;
        }

        std::cout << "L=" << e.L
                  << " survivor classes=" << classes
                  << " survivor representative mass=" << mass
                  << " fraction=" << (long double)mass / (long double)TOTAL
                  << "\n";
    }

    // Formation-only child imbalance and one-child boundary mass at L=25 -> 26.
    constexpr int L = 25;
    constexpr u64 MP = 1ULL << (L - 2); // parent reduced modulus 2^23

    std::vector<u64> parent_mass(MP, 0);
    for (u64 r = 0; r < MMAX; ++r)
        parent_mass[r & (MP - 1)] += dp[r];

    u64 C = 0, MD = 0;
    for (u64 r = 0; r < MP; ++r) {
        int q = 0;
        if (!coefficient_survives(r, L, &q)) continue;
        C += parent_mass[r];
        if (q == barrier(L)) MD += parent_mass[r];
    }

    u64 U = 0;
    for (u64 r = 0; r < MP; ++r) {
        const u64 c0 = dp[r];
        const u64 c1 = dp[r + MP];
        U += (c0 >= c1) ? (c0 - c1) : (c1 - c0);
    }

    constexpr u64 EXPECT_C = 1202007610492ULL;
    constexpr u64 EXPECT_MD = 228484933625ULL;
    constexpr u64 EXPECT_U = 6445500202ULL;
    constexpr std::int64_t EXPECT_K = -139083;
    constexpr u64 C26 = 1087765074138ULL;

    const std::int64_t K =
        (std::int64_t)(2 * C26) - (std::int64_t)(2 * C) + (std::int64_t)MD;

    if (C != EXPECT_C || MD != EXPECT_MD || U != EXPECT_U || K != EXPECT_K) {
        std::cerr << "transport certificate mismatch\n";
        return 1;
    }

    std::cout << "L=25->26 one-child mass=" << MD
              << " formation imbalance U=" << U
              << " U/MD=" << (long double)U/(long double)MD
              << " signed K=" << K
              << " K/MD=" << (long double)K/(long double)MD
              << "\n";

    return 0;
}
