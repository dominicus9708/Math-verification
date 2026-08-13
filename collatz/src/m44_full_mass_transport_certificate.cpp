#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using i64 = std::int64_t;
using u128 = __uint128_t;

static int barrier(int k) {
    u128 p3 = 1;
    const u128 p2 = u128(1) << k;
    int q = 0;
    while (p3 < p2) { p3 *= 3; ++q; }
    return q;
}

static std::vector<unsigned char> survivors(int L) {
    const u64 M = 1ULL << (L - 2); // N=4Y+3, Y mod 2^(L-2)
    std::vector<unsigned char> out(M, 0);
    for (u64 y = 0; y < M; ++y) {
        u64 x = 4*y + 3;
        int q = 0;
        bool ok = true;
        for (int k = 1; k <= L; ++k) {
            if (x & 1ULL) { ++q; x = (3*x + 1)/2; }
            else x /= 2;
            if (q < barrier(k)) { ok = false; break; }
        }
        out[y] = ok ? 1 : 0;
    }
    return out;
}

static u64 pow3mod(int e, u64 M) {
    u64 x = 1 & (M-1);
    for (int i=0;i<e;++i) x = (3*x) & (M-1);
    return x;
}

struct Expected {
    int L;
    u64 C;
    u64 D;
    u64 U;
};

int main() {
    constexpr int DSEL = 44;
    constexpr int MAX_CHILD_EXP = 24; // enough for L=25 -> 26
    constexpr u64 NMOD = 1ULL << MAX_CHILD_EXP;
    constexpr u64 TOTAL = 1ULL << DSEL;

    // Full m=44 ternary selector distribution for
    // Y = 3^44 + sum_{i=0}^{43} a_i 3^i (mod 2^24).
    std::vector<u64> dp(NMOD,0), nd(NMOD,0);
    dp[pow3mod(44,NMOD)] = 1;
    for (int i=0;i<DSEL;++i) {
        const u64 w = pow3mod(i,NMOD);
        nd = dp;
        for (u64 r=0;r<NMOD;++r)
            nd[(r+w)&(NMOD-1)] += dp[r];
        dp.swap(nd);
    }
    u64 chk=0; for (u64 c:dp) chk += c;
    if (chk != TOTAL) return 1;

    const std::array<Expected,15> expected{{
        {3,  17592186044416ULL, 8796093022208ULL, 4194304ULL},
        {4,  13194139533312ULL, 8796095119360ULL, 2048ULL},
        {6,   8796091972608ULL, 3298534882832ULL, 40ULL},
        {7,   7146824531190ULL, 3848290434574ULL, 56ULL},
        {9,   5222679313909ULL, 1649267244880ULL, 8907ULL},
        {11,  4398045691348ULL, 1030791994834ULL, 693772ULL},
        {12,  3882649683210ULL, 1460288668299ULL, 494762ULL},
        {14,  3152505354815ULL, 743029190277ULL, 3580205ULL},
        {15,  2780990752541ULL, 1022202010104ULL, 6650859ULL},
        {17,  2269889787451ULL, 515932831671ULL, 18318991ULL},
        {19,  2011923507477ULL, 355945413895ULL, 76621889ULL},
        {20,  1833950905184ULL, 539891337183ULL, 52632776ULL},
        {22,  1564005133050ULL, 295899305006ULL, 117886560ULL},
        {23,  1416055503075ULL, 428095694704ULL, 244836127ULL},
        {25,  1202007610492ULL, 228484933625ULL, 440762934ULL}
    }};

    for (const auto &e: expected) {
        const int L=e.L;
        if (barrier(L+1) != barrier(L)+1) return 2;
        const u64 M=1ULL<<(L-2);
        const u64 childM=2*M;
        const u64 fold=NMOD/childM;

        std::vector<u64> cnt(childM,0);
        for (u64 r=0;r<NMOD;++r) cnt[r&(childM-1)] += dp[r];
        const auto R=survivors(L);
        const auto R2=survivors(L+1);

        u64 C=0,Dmass=0,U=0,Cnext=0;
        i64 K=0;
        for (u64 r=0;r<M;++r) {
            if (!R[r]) continue;
            const u64 c0=cnt[r], c1=cnt[r+M], c=c0+c1;
            const int b0=R2[r]?1:0, b1=R2[r+M]?1:0;
            const int m=b0+b1;
            const i64 u=(i64)c0-(i64)c1;
            const int v=b0-b1;
            C += c;
            Cnext += b0*c0+b1*c1;
            const u64 au = c0>=c1 ? c0-c1 : c1-c0;
            U += au;
            if (m==1) { Dmass += c; K += (i64)v*u; }
        }

        if (C!=e.C || Dmass!=e.D || U!=e.U) return 3;
        const i64 identity_rhs = (i64)C - (i64)(Dmass/2) + K/2;
        // Avoid integer-half ambiguity by checking doubled identity exactly.
        if ((__int128)2*Cnext != (__int128)2*C - (__int128)Dmass + (__int128)K)
            return 4;
        if ((u64)(K<0?-K:K) > U) return 5;
        if (U >= Dmass) return 6;

        std::cout << "L="<<L
                  << " C="<<C
                  << " D="<<Dmass
                  << " U="<<U
                  << " K="<<K
                  << " D/C="<<(long double)Dmass/(long double)C
                  << " U/D="<<(long double)U/(long double)Dmass
                  << " Cnext="<<Cnext << "\n";
        (void)fold; (void)identity_rhs;
    }
    return 0;
}
