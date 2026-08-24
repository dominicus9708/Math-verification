// Exact finite active-subtree Haar-energy certificate for the current m=44 core.
//
// Root: the forced N = 3 (mod 4) cylinder after the first two parity bits 11.
// Active nodes: exact mechanical-relative coefficient-surviving prefixes that
// have not yet completed their first nontrivial positive excursion back to
// relative height zero. A child is stopped if it goes below the mechanical
// coefficient boundary or completes that first return.
//
// For selector probability mu on the current m44 core C44 \ A33, the split
// cost at an active reduced-y cylinder I of depth d is
//
//     2^d (mu(I0)-mu(I1))^2.
//
// The program sums this cost over every active parent through reduced depth 25
// (parity depth 27, revealing the 28th parity bit).  It also reports the exact
// first-return prefix-free Carleson diagnostics for the currently unresolved
// first-defect channels p=2,5,8,10,13,16.
//
// This is finite evidence only.  It does not establish an asymptotic energy
// exponent and does not prove Collatz.
//
// Build: g++ -O3 -std=c++17 m44_first_excursion_active_haar_energy_certificate.cpp -o cert

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;
using u128 = unsigned __int128;

static const std::string H19 = "1101101101011011010";
static constexpr int L = 28;
static constexpr int KY = 26;
static constexpr u32 YM = 1u << KY;
static constexpr u32 YMASK = YM - 1;

std::string mech;

std::string s128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

std::vector<u32> selector_dp(int bits) {
    std::vector<u32> dp(YM), nd(YM);
    dp[0] = 1;
    u32 w = 1;
    for (int i = 0; i < bits; ++i) {
        if (i) w = (u64(w) * 3) & YMASK;
        for (u32 r = 0; r < YM; ++r)
            nd[r] = dp[r] + dp[(r + YM - w) & YMASK];
        dp.swap(nd);
    }
    return dp;
}

// ---------------------------------------------------------------------------
// Active-prefix tree, propagated in canonical-start coordinates.
// ---------------------------------------------------------------------------
struct Node {
    int k = 0;
    int q = 0;
    int h = 0;
    bool started = false;
    u64 r = 0;   // canonical start mod 2^k
    u64 y = 0;   // T^k(r)
    u64 p3 = 1;  // 3^q
};

std::vector<u32> active[27];

void build_active_tree() {
    // Forced first two parity bits are 11.  Canonical representative r=3 has
    // T^2(3)=8 and q=2.
    std::vector<Node> cur{{2, 2, 0, false, 3, 8, 9}};
    active[0].push_back(0);

    for (int k = 2; k < L; ++k) {
        std::vector<Node> nxt;
        nxt.reserve(cur.size() * 2);
        const int m = mech[k] - '0';

        for (const Node& n : cur) {
            for (int b = 0; b <= 1; ++b) {
                const int h2 = n.h + b - m;
                if (h2 < 0) continue;  // coefficient-boundary exit

                const bool started2 = n.started || (h2 > 0);
                const bool first_return = started2 && (h2 == 0);

                const int carry = b ^ int(n.y & 1ULL);
                Node t = n;
                t.k = k + 1;
                t.h = h2;
                t.started = started2;

                if (carry) {
                    t.r += (1ULL << k);
                    t.y += n.p3;
                }

                if (b == 0) {
                    t.y >>= 1;
                } else {
                    t.y = (3 * t.y + 1) >> 1;
                    ++t.q;
                    t.p3 *= 3;
                }

                if (first_return) continue;  // successful stopping leaf

                if (k + 1 < L) {
                    const u32 yr = u32((t.r - 3) >> 2);
                    active[(k + 1) - 2].push_back(yr);
                    nxt.push_back(t);
                }
            }
        }
        cur.swap(nxt);
    }

    for (int d = 0; d < 26; ++d) {
        auto& v = active[d];
        std::sort(v.begin(), v.end());
        if (std::adjacent_find(v.begin(), v.end()) != v.end())
            std::exit(20);  // parity-prefix/canonical-residue injectivity audit
    }
}

// ---------------------------------------------------------------------------
// First-return leaf enumeration for fixed first-defect p.
// ---------------------------------------------------------------------------
u64 invodd(u64 a) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

u64 correction(u32 mask) {
    u64 R = 0;
    for (int i = 0; i < L; ++i)
        if ((mask >> i) & 1u) R = 3 * R + (1ULL << i);
    return R;
}

struct Rec {
    u32 y;
    int stop;
    int fp;
};
std::vector<Rec> recs;

void emit_word(u32 mask, int q) {
    u64 R = correction(mask), p3 = 1;
    for (int i = 0; i < q; ++i) p3 *= 3;
    const u64 inv = invodd(p3) & ((1ULL << 28) - 1);
    const u32 N = u32((0ULL - R) * inv) & ((1u << 28) - 1);
    if ((N & 3u) != 3u) std::exit(21);

    const u32 y = (N - 3u) >> 2;
    int h = 0, stop = 0, fp = -1;
    bool started = false;

    for (int i = 0; i < L; ++i) {
        const int b = (mask >> i) & 1u;
        const int m = mech[i] - '0';
        if (fp < 0 && b != m) fp = i;
        h += b - m;
        if (h < 0) std::exit(22);
        if (h > 0) started = true;
        if (started && h == 0) {
            stop = i + 1;
            break;
        }
    }
    recs.push_back({y, stop, fp});
}

void dfs_words(int i, int h, int q, u32 mask) {
    if (i == L) {
        emit_word(mask, q);
        return;
    }
    const int m = mech[i] - '0';
    for (int b = 0; b <= 1; ++b) {
        const int h2 = h + b - m;
        if (h2 < 0) continue;
        dfs_words(i + 1, h2, q + b, mask | (u32(b) << i));
    }
}

int main() {
    mech = (H19 + H19).substr(0, L);
    build_active_tree();

    auto dp44 = selector_dp(44);
    auto dp33 = selector_dp(33);

    u64 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3ULL;
    const u32 c = p44 & YMASK;
    const u64 TOT = (1ULL << 44) - (1ULL << 33);

    // Current-core probability masses at the finest reduced depth 26.
    std::vector<u64> arr(YM);
    for (u32 y = 0; y < YM; ++y) {
        const u32 s = (y + YM - c) & YMASK;
        arr[y] = u64(dp44[s]) - u64(dp33[s]);
    }

    // Sum the active Haar split cost exactly.  At parent reduced depth d,
    // arr currently stores child masses at depth d+1.
    u128 exact_sum = 0;
    long double floating_sum = 0;
    for (int d = 25; d >= 0; --d) {
        u128 sq = 0;
        for (u32 r : active[d]) {
            const long long diff =
                (long long)arr[r] - (long long)arr[r + (1u << d)];
            const u64 ad = diff < 0 ? u64(-diff) : u64(diff);
            sq += u128(ad) * ad;
        }
        exact_sum += (sq << d);
        floating_sum += std::ldexp((long double)1, d) * (long double)sq /
                        ((long double)TOT * (long double)TOT);

        for (u32 r = 0; r < (1u << d); ++r)
            arr[r] += arr[r + (1u << d)];
        arr.resize(1u << d);
    }

    const u128 denom = u128(TOT) * TOT;
    const u128 EXPECT_NUM = u128(8856957423051132992ULL);
    if (exact_sum != EXPECT_NUM) std::exit(23);

    // First-return leaf diagnostics by first-defect p.
    recs.reserve(3524586);
    dfs_words(0, 0, 0, 0);
    if (recs.size() != 3524586ULL) std::exit(24);

    std::array<std::array<std::unordered_map<u32, u64>, 29>, 29> leaf;
    for (const Rec& z : recs) {
        if (z.stop == 0 || z.fp < 0) continue;
        const u32 s = (z.y + YM - c) & YMASK;
        const u64 mass = u64(dp44[s]) - u64(dp33[s]);
        if (!mass) continue;
        const int d = z.stop - 2;
        const u32 pref = d ? (z.y & ((1u << d) - 1)) : 0;
        leaf[z.fp][z.stop][pref] += mass;
    }

    // Canonical mechanical y residue, used to query the common parent cylinder.
    u32 mmask = 0;
    int mq = 0;
    for (int i = 0; i < L; ++i) if (mech[i] == '1') {
        mmask |= 1u << i;
        ++mq;
    }
    u64 mR = correction(mmask), mp3 = 1;
    for (int i = 0; i < mq; ++i) mp3 *= 3ULL;
    const u64 minv = invodd(mp3) & ((1ULL << 28) - 1);
    const u32 mN = u32((0ULL - mR) * minv) & ((1u << 28) - 1);
    const u32 my = (mN - 3u) >> 2;

    auto parent_mass = [&](int p) {
        const int d = p - 2;
        if (d <= 0) return TOT;
        const u32 pref = my & ((1u << d) - 1);
        u64 z = 0;
        for (u32 y = pref; y < YM; y += (1u << d)) {
            const u32 s = (y + YM - c) & YMASK;
            z += u64(dp44[s]) - u64(dp33[s]);
        }
        return z;
    };

    const int P[6] = {2, 5, 8, 10, 13, 16};
    const u64 EXPECT_PARENT[6] = {
        17583596109824ULL, 2197949497472ULL, 274743687187ULL,
        68685921612ULL, 8585738741ULL, 1073218845ULL};
    const u64 EXPECT_LEAVES[6] = {93999, 18698, 4403, 889, 198, 56};
    const u64 EXPECT_MASS[6] = {
        597178447818ULL, 102733307973ULL, 17282159097ULL,
        4110516346ULL, 723668238ULL, 124191604ULL};
    const u64 EXPECT_KNUM[6] = {32931724, 4078994, 499612, 126578, 15518, 1852};
    const u128 EXPECT_SNUM[6] = {
        u128(1628071309420209048ULL) * 1000000ULL + 27064ULL, // 1628071309420209048027064
        u128(41613966509239551756ULL) * 1000ULL + 872ULL,      // 41613966509239551756872
        u128(1116770714922932093888ULL),
        u128(62318499776592293056ULL),
        u128(1707081250793847768ULL),
        u128(48283009157537140ULL)};

    std::cout << std::setprecision(18);
    std::cout << "m44 active first-excursion Haar energy: PASS\n";
    std::cout << "active_split_energy_num " << s128(exact_sum)
              << " denom " << s128(denom)
              << " value " << floating_sum << "\n";

    for (int z = 0; z < 6; ++z) {
        const int p = P[z];
        const u64 pm = parent_mass(p);
        u64 leaves = 0, lm = 0;
        u128 knum = 0, snum = 0;

        for (int b = p + 1; b <= 28; ++b) {
            for (const auto& kv : leaf[p][b]) {
                ++leaves;
                lm += kv.second;
                knum += (u128(1) << (28 - b));
                snum += u128(kv.second) * kv.second *
                        (u128(1) << (b - p));
            }
        }

        if (pm != EXPECT_PARENT[z] || leaves != EXPECT_LEAVES[z] ||
            lm != EXPECT_MASS[z] || knum != EXPECT_KNUM[z] ||
            snum != EXPECT_SNUM[z]) std::exit(30 + z);

        // Exact Cauchy check:
        // (lm/pm)^2 <= (snum/pm^2) * (knum/2^(28-p)).
        if (u128(lm) * lm * (u128(1) << (28 - p)) > snum * knum)
            std::exit(40 + z);

        const long double localP = (long double)lm / pm;
        const long double K = (long double)knum /
                              std::ldexp((long double)1, 28 - p);
        const long double E = (long double)snum /
                              ((long double)pm * (long double)pm);

        std::cout << "p " << p
                  << " parent " << pm
                  << " leaves " << leaves
                  << " return_mass " << lm
                  << " localP " << localP
                  << " Kraft " << K
                  << " energy " << E
                  << " cauchy_bound " << std::sqrt(E * K) << "\n";
    }
}
