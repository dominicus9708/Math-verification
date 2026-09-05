#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

// Exact meet-in-the-middle certificate for the intersection
//
//   F_44 = { 4(3^44 + sum_{i=0}^{43} a_i 3^i)+3 : a_i in {0,1} }
//
// with the canonical neutral Beatty parity prefix
//
//   e_0,...,e_5 = 1,
//   e_j = b(j+1)-b(j)  (j>=6),
//   b(k)=min{q:3^q>=2^k}.
//
// This is a finite exact certificate, NOT a Collatz proof.
//
// We scan K=36..47.  At K>=36 the low 22-digit subset sum is strictly
// smaller than 2^(K-2), so the sorted low table needs no modular folding.
// The high 22-digit half is reduced modulo 2^(K-2) during lookup.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

static std::string dec128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static int beatty_b(int k) {
    u128 p = 1;
    const u128 target = (u128(1) << k);
    int q = 0;
    while (p < target) {
        p *= 3;
        ++q;
    }
    return q;
}

static u128 inv_odd_pow2(u128 a, int K) {
    // Newton iteration in Z/2^128 Z; eight doublings are ample here.
    u128 x = a;
    for (int i = 0; i < 8; ++i) x *= (u128(2) - a * x);
    const u128 mask = (u128(1) << K) - 1;
    return x & mask;
}

struct Target {
    int q;
    u128 R;
    u128 start_residue;
};

static Target neutral_target(int K) {
    u128 R = 0;
    int q = 0;
    for (int pos = 0; pos < K; ++pos) {
        const int bit = (pos < 6)
            ? 1
            : beatty_b(pos + 1) - beatty_b(pos);
        if (bit) {
            R = 3 * R + (u128(1) << pos);
            ++q;
        }
    }

    u128 p3q = 1;
    for (int i = 0; i < q; ++i) p3q *= 3;

    const u128 mask = (u128(1) << K) - 1;
    const u128 inv = inv_odd_pow2(p3q, K);
    const u128 nres = (u128(0) - (R & mask) * inv) & mask;
    return {q, R, nres};
}

static std::vector<u128> subset_sums(
    const std::array<u128, 44>& p3,
    int lo,
    int hi
) {
    const int n = hi - lo;
    const std::size_t N = std::size_t(1) << n;
    std::vector<u128> out(N, 0);
    for (std::size_t mask = 1; mask < N; ++mask) {
        const std::size_t lb = mask & (~mask + 1);
        const int j = __builtin_ctzll(static_cast<u64>(lb));
        out[mask] = out[mask ^ lb] + p3[lo + j];
    }
    return out;
}

int main() {
    constexpr int m = 44;
    std::array<u128, 44> p3{};
    p3[0] = 1;
    for (int i = 1; i < 44; ++i) p3[i] = 3 * p3[i - 1];
    const u128 p3m = 3 * p3[43];

    auto low = subset_sums(p3, 0, 22);
    auto high = subset_sums(p3, 22, 44);
    std::sort(low.begin(), low.end());

    // max low sum = (3^22-1)/2 < 2^34, so K>=36 is wrap-free.
    u128 max_low = 0;
    for (int i = 0; i < 22; ++i) max_low += p3[i];
    if (!(max_low < (u128(1) << 34))) return 2;

    const std::array<unsigned long long, 12> expected = {
        1076, 555, 277, 136, 73, 30, 13, 6, 4, 2, 1, 0
    };

    std::cout << "K,q,d,count,start_residue\n";

    for (int K = 36; K <= 47; ++K) {
        const int r = K - 2;
        const u128 mod = (u128(1) << r);
        const u128 mask = mod - 1;
        const auto t = neutral_target(K);

        if ((t.start_residue & 3) != 3) return 3;
        if (K >= 6 && t.q != beatty_b(K) + 2) return 4;

        const u128 xres = ((t.start_residue - 3) >> 2) & mask;
        const u128 target_selector_sum = (xres - (p3m & mask)) & mask;

        unsigned long long count = 0;
        for (const u128 s : high) {
            const u128 need = (target_selector_sum - (s & mask)) & mask;
            // low entries are exact, unique, and < modulus throughout K>=36.
            if (std::binary_search(low.begin(), low.end(), need)) ++count;
        }

        const auto exp = expected[K - 36];
        if (count != exp) {
            std::cerr << "count regression failure at K=" << K
                      << " got " << count << " expected " << exp << "\n";
            return 5;
        }

        std::cout << K << ',' << t.q << ',' << (t.q - beatty_b(K)) << ','
                  << count << ',' << dec128(t.start_residue) << '\n';
    }

    // Recover the unique K=46 selector assignment exactly.
    const int K = 46;
    const int r = K - 2;
    const u128 mask = (u128(1) << r) - 1;
    const auto t = neutral_target(K);
    const u128 xres = ((t.start_residue - 3) >> 2) & mask;
    const u128 target_selector_sum = (xres - (p3m & mask)) & mask;

    unsigned long long hits = 0;
    u64 recovered_mask = 0;

    // Build a sum->mask table for the low half.  Exact ternary 0/1 sums are
    // injective as ordinary integers.
    std::vector<std::pair<u128, u32>> low_with_mask;
    low_with_mask.reserve(std::size_t(1) << 22);
    for (u32 lm = 0; lm < (u32(1) << 22); ++lm)
        low_with_mask.push_back({low[lm], 0});
    // 'low' is sorted and no longer indexed by selector mask, so rebuild the
    // pair table directly for recovery.
    low_with_mask.clear();
    for (u32 lm = 0; lm < (u32(1) << 22); ++lm) {
        u128 s = 0;
        u32 x = lm;
        while (x) {
            const int j = __builtin_ctz(x);
            s += p3[j];
            x &= x - 1;
        }
        low_with_mask.push_back({s, lm});
    }
    std::sort(low_with_mask.begin(), low_with_mask.end(),
              [](const auto& a, const auto& b) { return a.first < b.first; });

    for (u32 hm = 0; hm < (u32(1) << 22); ++hm) {
        u128 s = 0;
        u32 x = hm;
        while (x) {
            const int j = __builtin_ctz(x);
            s += p3[22 + j];
            x &= x - 1;
        }
        const u128 need = (target_selector_sum - (s & mask)) & mask;
        auto it = std::lower_bound(
            low_with_mask.begin(), low_with_mask.end(), need,
            [](const auto& a, const u128& v) { return a.first < v; }
        );
        if (it != low_with_mask.end() && it->first == need) {
            ++hits;
            recovered_mask = (u64(hm) << 22) | it->second;
        }
    }
    if (hits != 1) return 6;

    u128 X = p3m;
    for (int i = 0; i < 44; ++i)
        if ((recovered_mask >> i) & 1ULL) X += p3[i];
    const u128 N = 4 * X + 3;

    // Verify exact F_44 membership and the neutral prefix through 46 steps,
    // followed by the forced mismatch at position 46 (the 47th parity bit).
    u128 y = N;
    int first_diff = -1;
    for (int pos = 0; pos < 60; ++pos) {
        const int actual = int(y & 1);
        const int wanted = (pos < 6)
            ? 1
            : beatty_b(pos + 1) - beatty_b(pos);
        if (actual != wanted && first_diff < 0) first_diff = pos;
        y = actual ? (3 * y + 1) >> 1 : y >> 1;
    }
    if (first_diff != 46) return 7;

    std::cout << "unique_K46_selector_mask," << recovered_mask << '\n';
    std::cout << "unique_K46_N," << dec128(N) << '\n';
    std::cout << "first_neutral_mismatch_position," << first_diff << '\n';
    std::cout << "PASS\n";
    return 0;
}
