#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>

// Fast exact version of the original-start alternate-predecessor integerization
// sieve. This is logically independent of the withdrawn claim that every later
// block of a minimal counterexample must be residue-maximal.
//
// For a length-L parity word w with q odd symbols and correction R_w, compare
// an alternate word u with the same q and R_u>R_w. Put
//
//     C = R_u-R_w,  s=v_3(C).
//
// If s>=q, the alternate original start is already integral. If s<q, put
// d=q-s and let t_d be the time of the d-th odd symbol of u. When
//
//     2^t_d > 3^d,
//
// the contracting prefix integerizes the remaining 3-adic denominator.
//
// For the large-start regime used by the m=45 calculation,
//
//     N_min = 4(3^44+3^32)+3,
//
// and for every L<=44 every correction satisfies
//
//     R <= 3^L-2^L < 3^L < N_min.
//
// Hence, once the contracting-prefix condition holds, the exact size and
// positivity inequalities in binary_alternate_predecessor_integerization_sieve.cpp
// are automatic. This allows the pairwise O(4^L)-type scan to be replaced by
// residue-class maxima:
//
// * s>=q: keep the maximum correction in each class modulo 3^q;
// * s<q: inside each class modulo 3^s, keep the maximum eligible correction
//   for each of the three next ternary digits modulo 3^(s+1).
//
// A word w is removed if a larger eligible maximum exists in the required
// class/different next digit. The resulting work is O(L 2^L) up to hash-map
// factors rather than all-pairs comparison.
//
// The fast counts exactly reproduce the old implementation through L=16 and
// extend the same exact criterion through L=24 below.
//
// Extension closure: if a prefix is removed by a smaller start that merges at
// its endpoint, every longer extension is removed as well, because after the
// merge the two trajectories have the same next parity. Therefore the retained
// original-prefix language is automatically prefix-closed.
//
// This is a finite/structural certificate, not a proof of Collatz.

using u32 = std::uint32_t;
using u64 = std::uint64_t;

struct Word {
    u64 correction{};
    u32 mask{};
    u32 contracting_d{};  // bit d set iff 2^(t_d)>3^d
    bool coefficient_surviving{};
};

struct Top3 {
    std::array<u64,3> value{{0,0,0}};
};

struct Expected {
    int L;
    u64 surviving;
    u64 removed;
    u64 retained;
};

static const std::array<Expected,22> EXPECTED{{
    {3,2,0,2},
    {4,3,0,3},
    {5,4,0,4},
    {6,8,1,7},
    {7,13,2,11},
    {8,19,3,16},
    {9,38,11,27},
    {10,64,18,46},
    {11,128,48,80},
    {12,226,82,144},
    {13,367,125,242},
    {14,734,298,436},
    {15,1295,493,802},
    {16,2114,751,1363},
    {17,4228,1729,2499},
    {18,7495,2895,4600},
    {19,14990,6527,8463},
    {20,27328,11458,15870},
    {21,46611,18464,28147},
    {22,93222,41046,52176},
    {23,168807,70829,97978},
    {24,286581,113713,172868},
}};

int main(int argc, char** argv) {
    int maxL = 24;
    if (argc >= 2) maxL = std::atoi(argv[1]);
    if (maxL < 3 || maxL > 30) {
        std::cerr << "usage: binary_alternate_predecessor_integerization_fast [maxL<=30]\n";
        return 2;
    }

    std::vector<u64> p3(maxL + 1, 1);
    for (int i = 1; i <= maxL; ++i) p3[i] = 3 * p3[i-1];

    std::vector<unsigned char> previous_retained;
    std::cout << "L surviving removed retained removed_fraction prefix_closed\n";

    for (int L = 3; L <= maxL; ++L) {
        const u32 total = u32(1) << L;
        std::vector<std::vector<Word>> by_q(L + 1);
        std::vector<unsigned char> is_survivor(total,0), is_removed(total,0);

        for (u32 mask = 0; mask < total; ++mask) {
            u64 R = 0;
            int q = 0;
            bool surviving = true;
            u32 contracting_d = 0;

            for (int i = 0; i < L; ++i) {
                if ((mask >> i) & 1u) {
                    R = 3 * R + (u64(1) << i);
                    ++q;
                    if ((u64(1) << (i + 1)) > p3[q])
                        contracting_d |= (u32(1) << q);
                }
                if (p3[q] < (u64(1) << (i + 1)))
                    surviving = false;
            }

            const bool core = surviving && ((mask & 3u) == 3u);
            is_survivor[mask] = core;
            by_q[q].push_back(Word{R,mask,contracting_d,core});
        }

        u64 surviving_count = 0;
        u64 removed_count = 0;

        for (int q = 0; q <= L; ++q) {
            auto& words = by_q[q];
            if (words.empty()) continue;
            std::vector<unsigned char> removed(words.size(),0);

            // Full-Hensel local integer case: same residue modulo 3^q.
            std::unordered_map<u64,u64> class_max;
            class_max.reserve(words.size() * 2 + 1);
            for (const auto& w : words) {
                const u64 key = w.correction % p3[q];
                auto it = class_max.find(key);
                if (it == class_max.end() || it->second < w.correction)
                    class_max[key] = w.correction;
            }

            for (std::size_t i = 0; i < words.size(); ++i) {
                if (!words[i].coefficient_surviving) continue;
                ++surviving_count;
                if (class_max[words[i].correction % p3[q]] > words[i].correction)
                    removed[i] = 1;
            }

            // Partially 3-divisible differences integerized by a contracting
            // prefix of the alternate word.
            for (int s = 0; s < q; ++s) {
                const int d = q - s;
                const u64 mod = p3[s];
                std::unordered_map<u64,Top3> top;
                top.reserve(words.size() * 2 + 1);

                for (const auto& u : words) {
                    if (((u.contracting_d >> d) & 1u) == 0) continue;
                    const u64 parent = s ? u.correction % mod : 0;
                    const unsigned digit = unsigned((u.correction / mod) % 3u);
                    auto& z = top[parent];
                    z.value[digit] = std::max(z.value[digit], u.correction);
                }

                for (std::size_t i = 0; i < words.size(); ++i) {
                    if (!words[i].coefficient_surviving || removed[i]) continue;
                    const u64 parent = s ? words[i].correction % mod : 0;
                    const auto it = top.find(parent);
                    if (it == top.end()) continue;
                    const unsigned digit = unsigned((words[i].correction / mod) % 3u);
                    u64 best = 0;
                    for (unsigned a = 0; a < 3; ++a)
                        if (a != digit) best = std::max(best, it->second.value[a]);
                    if (best > words[i].correction) removed[i] = 1;
                }
            }

            for (std::size_t i = 0; i < words.size(); ++i) {
                if (!words[i].coefficient_surviving) continue;
                is_removed[words[i].mask] = removed[i];
                if (removed[i]) ++removed_count;
            }
        }

        const u64 retained_count = surviving_count - removed_count;

        // Finite regression check of prefix closure. Algebraically this follows
        // from endpoint merging, but checking it guards the implementation.
        std::vector<unsigned char> retained(total,0);
        bool prefix_closed = true;
        u64 direct_retained = 0;
        for (u32 mask = 0; mask < total; ++mask) {
            if (!is_survivor[mask] || is_removed[mask]) continue;
            ++direct_retained;
            if (L > 3) {
                const u32 parent = mask & ((u32(1) << (L - 1)) - 1);
                if (!previous_retained[parent]) prefix_closed = false;
            }
            retained[mask] = 1;
        }
        if (direct_retained != retained_count || !prefix_closed) return 3;

        if (L <= 24) {
            const auto& e = EXPECTED[std::size_t(L - 3)];
            if (e.L != L || e.surviving != surviving_count ||
                e.removed != removed_count || e.retained != retained_count)
                return 4;
        }

        const long double fraction = surviving_count
            ? static_cast<long double>(removed_count) /
              static_cast<long double>(surviving_count)
            : 0.0L;

        std::cout << L << ' '
                  << surviving_count << ' '
                  << removed_count << ' '
                  << retained_count << ' '
                  << std::setprecision(15) << fraction << ' '
                  << (prefix_closed ? "PASS" : "FAIL") << '\n';

        previous_retained.swap(retained);
    }

    std::cout << "fast original-start integerization sieve: PASS\n";
    return 0;
}
