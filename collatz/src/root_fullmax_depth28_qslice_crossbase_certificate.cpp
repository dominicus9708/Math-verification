// q-slice audit for nested full root-Hensel maximality at H=28.
//
// This is a refinement of root_fullmax_depth28_crossbase_certificate.cpp.
// It tests whether the near-neutral global cross-base ratio is concealing
// large opposite biases in different final odd-count q slices.
//
// For each coefficient-surviving canonical residue modulo 2^28, meta stores
// its final q and whether it passes root credit-1 avoidance and nested full
// root-Hensel maximality.  The same m=44/m=45 ternary selector DP is then
// accumulated separately by q.
//
// Build:
//   g++ -O3 -std=c++17 root_fullmax_depth28_qslice_crossbase_certificate.cpp -o cert

#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;

struct State { u64 R; std::uint8_t q; };
struct Slice {
    std::array<u64, 29> coefficient{};
    std::array<u64, 29> credit1{};
    std::array<u64, 29> rootmax{};
};

static constexpr int L = 28;
static constexpr int KY = 26;
static constexpr u32 YM = 1u << KY;
static constexpr u32 YMASK = YM - 1;

u64 p3[40];
// low 5 bits: q; bit 5: credit-1 alive; bit 6: root-max alive.
std::vector<std::uint8_t> meta;

inline bool coefficient_ok(int k, int q) {
    return p3[q] >= (1ULL << k);
}

inline u64 class_key(int q, u64 R) {
    return (u64(q) << 56) | (R % p3[q]);
}

void scan_all_words(int pos, int k, int q, u64 R, int qmin,
                    std::unordered_map<u64, u64>& class_max) {
    if (q + (k - pos) < qmin) return;
    if (pos == k) {
        auto it = class_max.find(class_key(q, R));
        if (it != class_max.end() && R > it->second) it->second = R;
        return;
    }
    scan_all_words(pos + 1, k, q, R, qmin, class_max);
    scan_all_words(pos + 1, k, q + 1, 3 * R + (1ULL << pos), qmin,
                   class_max);
}

u64 invodd(u64 a) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

bool avoids_root_credit1(u32 N) {
    u64 x = N, y = N - 1;
    int qx = 0, qy = 0;
    for (int k = 0; k < L; ++k) {
        if (x & 1ULL) { x = (3 * x + 1) >> 1; ++qx; }
        else x >>= 1;
        if (y & 1ULL) { y = (3 * y + 1) >> 1; ++qy; }
        else y >>= 1;
        if (x == y && qx == qy) return false;
    }
    return true;
}

std::vector<u32> selector_dp(int digits) {
    std::vector<u32> dp(YM), nd(YM);
    dp[0] = 1;
    u32 w = 1;
    for (int i = 0; i < digits; ++i) {
        if (i) w = static_cast<u32>((u64(w) * 3) & YMASK);
        for (u32 r = 0; r < YM; ++r)
            nd[r] = dp[r] + dp[(r + YM - w) & YMASK];
        dp.swap(nd);
    }
    return dp;
}

Slice count_block(const std::vector<u32>& dp, u64 C) {
    Slice out;
    const u32 c = static_cast<u32>(C) & YMASK;
    for (u32 s = 0; s < YM; ++s) {
        const u32 mult = dp[s];
        if (!mult) continue;
        const std::uint8_t m = meta[(c + s) & YMASK];
        if (!m) continue;
        const int q = m & 31;
        out.coefficient[q] += mult;
        if (m & 32) out.credit1[q] += mult;
        if (m & 64) out.rootmax[q] += mult;
    }
    return out;
}

Slice subtract_slice(const Slice& a, const Slice& b) {
    Slice x;
    for (int q = 0; q <= 28; ++q) {
        x.coefficient[q] = a.coefficient[q] - b.coefficient[q];
        x.credit1[q] = a.credit1[q] - b.credit1[q];
        x.rootmax[q] = a.rootmax[q] - b.rootmax[q];
    }
    return x;
}

Slice add_slice(const Slice& a, const Slice& b) {
    Slice x;
    for (int q = 0; q <= 28; ++q) {
        x.coefficient[q] = a.coefficient[q] + b.coefficient[q];
        x.credit1[q] = a.credit1[q] + b.credit1[q];
        x.rootmax[q] = a.rootmax[q] + b.rootmax[q];
    }
    return x;
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 40; ++i) p3[i] = p3[i - 1] * 3;

    std::vector<State> coefficient{{0, 0}};
    std::vector<State> nested{{0, 0}};

    for (int k = 1; k <= L; ++k) {
        std::vector<State> next_coefficient;
        next_coefficient.reserve(coefficient.size() * 2);
        for (const State s : coefficient) {
            if (coefficient_ok(k, s.q)) next_coefficient.push_back(s);
            const int q1 = s.q + 1;
            const u64 R1 = 3 * s.R + (1ULL << (k - 1));
            if (coefficient_ok(k, q1))
                next_coefficient.push_back({R1, static_cast<std::uint8_t>(q1)});
        }
        coefficient.swap(next_coefficient);

        std::unordered_map<u64, u64> class_max;
        class_max.reserve(coefficient.size() * 2);
        for (const State s : coefficient) {
            auto [it, inserted] = class_max.emplace(class_key(s.q, s.R), s.R);
            if (!inserted && s.R > it->second) it->second = s.R;
        }

        int qmin = 0;
        while (!coefficient_ok(k, qmin)) ++qmin;
        scan_all_words(0, k, 0, 0, qmin, class_max);

        std::vector<State> next_nested;
        next_nested.reserve(nested.size() * 2);
        for (const State s : nested) {
            if (coefficient_ok(k, s.q)) {
                auto it = class_max.find(class_key(s.q, s.R));
                if (it != class_max.end() && it->second == s.R)
                    next_nested.push_back(s);
            }
            const int q1 = s.q + 1;
            const u64 R1 = 3 * s.R + (1ULL << (k - 1));
            if (coefficient_ok(k, q1)) {
                auto it = class_max.find(class_key(q1, R1));
                if (it != class_max.end() && it->second == R1)
                    next_nested.push_back({R1, static_cast<std::uint8_t>(q1)});
            }
        }
        nested.swap(next_nested);
    }

    if (coefficient.size() != 3'524'586ULL) std::exit(2);
    if (nested.size() != 2'882'872ULL) std::exit(3);

    meta.assign(YM, 0);
    Slice ambient;

    for (const State s : coefficient) {
        const u32 N = static_cast<u32>(
            ((0ULL - s.R) * invodd(p3[s.q])) & ((1ULL << L) - 1));
        const u32 z = (N - 3u) >> 2;
        if (meta[z]) std::exit(4);
        meta[z] = s.q;
        ++ambient.coefficient[s.q];
        if (avoids_root_credit1(N)) {
            meta[z] |= 32;
            ++ambient.credit1[s.q];
        }
    }

    for (const State s : nested) {
        const u32 N = static_cast<u32>(
            ((0ULL - s.R) * invodd(p3[s.q])) & ((1ULL << L) - 1));
        const u32 z = (N - 3u) >> 2;
        if (!(meta[z] & 32)) std::exit(5);
        meta[z] |= 64;
        ++ambient.rootmax[s.q];
    }

    auto dp44 = selector_dp(44);
    auto dp33 = selector_dp(33);
    u64 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;

    const Slice m44 = subtract_slice(count_block(dp44, p44),
                                     count_block(dp33, p44));
    const Slice m45 = add_slice(count_block(dp44, 3 * p44),
                                count_block(dp44, 4 * p44));

    // Exact regression values for the only q slices where credit>1 removes
    // anything beyond credit-1 at H=28.
    const u64 expected[4][9] = {
        // amb credit, amb root, m44 credit, m44 root, m45 credit, m45 root
        {538632, 535688, 141130139259ULL, 140358729579ULL,
         282398831936ULL, 280855343487ULL, 0, 0, 0},
        {1007189, 1003902, 263899655968ULL, 263038374282ULL,
         528056958857ULL, 526333613758ULL, 0, 0, 0},
        {737529, 736512, 193243924797ULL, 192977453176ULL,
         386677263787ULL, 386144064085ULL, 0, 0, 0},
        {385887, 385729, 101108765296ULL, 101067364549ULL,
         202315953970ULL, 202233108519ULL, 0, 0, 0}
    };

    for (int i = 0; i < 4; ++i) {
        const int q = 18 + i;
        if (ambient.credit1[q] != expected[i][0] ||
            ambient.rootmax[q] != expected[i][1] ||
            m44.credit1[q] != expected[i][2] ||
            m44.rootmax[q] != expected[i][3] ||
            m45.credit1[q] != expected[i][4] ||
            m45.rootmax[q] != expected[i][5]) std::exit(10 + i);
    }
    for (int q = 22; q <= 28; ++q)
        if (ambient.credit1[q] != ambient.rootmax[q] ||
            m44.credit1[q] != m44.rootmax[q] ||
            m45.credit1[q] != m45.rootmax[q]) std::exit(20 + q);

    std::cout << std::setprecision(15);
    std::cout << "q ambient_credit ambient_root m44_credit m44_root m45_credit m45_root\n";
    for (int q = 18; q <= 28; ++q)
        std::cout << q << ' ' << ambient.credit1[q] << ' ' << ambient.rootmax[q]
                  << ' ' << m44.credit1[q] << ' ' << m44.rootmax[q]
                  << ' ' << m45.credit1[q] << ' ' << m45.rootmax[q] << '\n';

    std::cout << "root full-max depth28 q-slice cross-base: PASS\n";
}
