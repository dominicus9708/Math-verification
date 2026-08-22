#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>

// Exact m=44 selector-mass transport under two logically safe rules only:
//
//   1. coefficient survival 3^q_k >= 2^k at every prefix;
//   2. the packed-terminal s=1 original-start predecessor rule at every
//      coefficient plateau.
//
// No repeated local residue-maximality assumption is used.
//
// Candidate selector coordinate:
//
//   Y = 3^44 + sum_{i=0}^{43} a_i 3^i,  a_i in {0,1},
//   N = 4Y+3.
//
// For depths L<=22, Y modulo 2^(L-2) determines the complete length-L parity
// prefix of N. We construct the exact 2^44 selector multiplicity distribution
// modulo 2^20 and fold it to every smaller dyadic modulus.
//
// The packed-terminal rule is justified by
//
//   collatz/notes/2026-08-20-alternate-predecessor-integerization-proof.md
//   collatz/notes/2026-08-20-packed-terminal-s1-predecessor-rule.md
//
// This is a finite certificate, not a proof of the Collatz conjecture.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr int DSEL = 44;
constexpr int MAX_L = 22;
constexpr int EXP = MAX_L - 2;
constexpr u64 MOD = 1ULL << EXP;
constexpr u64 MASK = MOD - 1;

struct Expected {
    int L;
    u64 coeff;
    u64 safe;
};

const std::array<Expected,20> EXPECTED{{
    {3,  17592186044416ULL,17592186044416ULL},
    {4,  13194139533312ULL,13194139533312ULL},
    {5,   8796091972608ULL, 8796091972608ULL},
    {6,   8796091972608ULL, 7696580869104ULL},
    {7,   7146824531190ULL, 6597068979440ULL},
    {8,   5222679313909ULL, 4947801538032ULL},
    {9,   5222679313909ULL, 4398045789739ULL},
    {10,  4398045691348ULL, 3917009485553ULL},
    {11,  4398045691348ULL, 3504692671119ULL},
    {12,  3882649683210ULL, 3298534272750ULL},
    {13,  3152505354815ULL, 2783138266668ULL},
    {14,  3152505354815ULL, 2551210082613ULL},
    {15,  2780990752541ULL, 2366526528849ULL},
    {16,  2269889787451ULL, 1993938189691ULL},
    {17,  2269889787451ULL, 1836098188639ULL},
    {18,  2011923507477ULL, 1705638682648ULL},
    {19,  2011923507477ULL, 1583366161003ULL},
    {20,  1833950905184ULL, 1514780987492ULL},
    {21,  1564005133050ULL, 1334358620139ULL},
    {22,  1564005133050ULL, 1248845268662ULL},
}};

int qmin_exact(int k) {
    u128 p3 = 1;
    const u128 p2 = u128(1) << k;
    int q = 0;
    while (p3 < p2) {
        p3 *= 3;
        ++q;
    }
    return q;
}

u64 pow3mod(int e) {
    u64 x = 1;
    for (int i = 0; i < e; ++i) x = (3 * x) & MASK;
    return x;
}

int v3(u64 x) {
    int s = 0;
    while (x && x % 3 == 0) {
        x /= 3;
        ++s;
    }
    return s;
}

u64 packed_correction(int L, int q) {
    u64 p3 = 1, p2 = 1;
    for (int i = 0; i < q; ++i) {
        p3 *= 3;
        p2 *= 2;
    }
    return (u64(1) << (L - q)) * (p3 - p2);
}

struct Flags {
    bool coefficient = true;
    bool safe = true;
};

Flags classify_prefix(u64 y, int L) {
    u64 x = 4 * y + 3;
    u64 R = 0;
    int q = 0;
    bool coefficient = true;
    bool safe = true;

    for (int i = 0; i < L; ++i) {
        const int b = int(x & 1ULL);
        if (b) {
            R = 3 * R + (u64(1) << i);
            ++q;
            x = (3 * x + 1) / 2;
        } else {
            x /= 2;
        }

        const int ell = i + 1;
        if (q < qmin_exact(ell)) coefficient = false;

        if (
            coefficient && safe && ell >= 3 && b == 0 &&
            qmin_exact(ell) == qmin_exact(ell - 1) &&
            q == qmin_exact(ell)
        ) {
            const u64 Rstar = packed_correction(ell, q);
            if (Rstar > R && v3(Rstar - R) == 1)
                safe = false;
        }
    }

    return {coefficient, safe};
}

} // namespace

int main() {
    // Exact selector histogram modulo 2^20.
    std::vector<u64> dp(MOD, 0), nd(MOD, 0);
    dp[pow3mod(44)] = 1;

    u64 w = 1;
    for (int i = 0; i < DSEL; ++i) {
        for (u64 r = 0; r < MOD; ++r)
            nd[r] = dp[r] + dp[(r - w) & MASK];
        dp.swap(nd);
        w = (3 * w) & MASK;
    }

    u64 total = 0;
    for (u64 c : dp) total += c;
    if (total != (1ULL << 44)) return 1;

    std::cout << "L coefficient_mass packed_s1_safe_mass additional_loss safe_over_coefficient\n";

    for (const auto& e : EXPECTED) {
        const int L = e.L;
        const u64 M = 1ULL << (L - 2);
        std::vector<u64> folded(M, 0);
        for (u64 r = 0; r < MOD; ++r)
            folded[r & (M - 1)] += dp[r];

        u64 coeff = 0, safe = 0;
        for (u64 y = 0; y < M; ++y) {
            if (!folded[y]) continue;
            const Flags f = classify_prefix(y, L);
            if (!f.coefficient) continue;
            coeff += folded[y];
            if (f.safe) safe += folded[y];
        }

        if (coeff != e.coeff || safe != e.safe) return 2;

        std::cout << L << ' '
                  << coeff << ' '
                  << safe << ' '
                  << (coeff - safe) << ' '
                  << std::setprecision(15)
                  << static_cast<long double>(safe) /
                     static_cast<long double>(coeff)
                  << '\n';
    }

    std::cout << "m44 packed-s1 safe transport certificate: PASS\n";
    return 0;
}
