// Exact finite certificate for nested full root-Hensel maximality through H=28.
//
// For every root prefix k, a hypothetical minimal counterexample must maximize
// the affine correction R within its full-Hensel class (q, R mod 3^q), whenever
// the universal root-credit bound is below the start.  At H=28 this is safely
// inside the already-established m=44 start scale.
//
// IMPORTANT AUDIT POINT: the competing word used to define the class maximum
// is NOT restricted to the coefficient-surviving language.  Only the tested
// candidate prefix obeys 3^q >= 2^k.  Therefore, at each k this program scans
// every length-k word with the same possible final q and updates the maximum
// correction for every candidate Hensel class.
//
// The program then propagates the nested root-max language through H=28,
// checks the previous H<=22 regression exactly, verifies every H=28 root-max
// survivor also passes the independent adjacent-start credit-1 test, and
// intersects the resulting residues with the same m=44/m=45 ternary selector
// DP used by root_credit1_depth28_crossbase_certificate.cpp.
//
// Result: credits > 1 remove only a small additional fraction, and that
// additional fraction is again essentially neutral with respect to the
// current ternary selector.  This is a finite negative control, not an
// asymptotic independence theorem and not a proof of Collatz.
//
// Build:
//   g++ -O3 -std=c++17 root_fullmax_depth28_crossbase_certificate.cpp -o cert

#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;

struct State {
    u64 R;
    std::uint8_t q;
};

static constexpr int L = 28;
static constexpr int KY = 26;
static constexpr u32 YM = 1u << KY;
static constexpr u32 YMASK = YM - 1;

u64 p3[40];
std::vector<std::uint8_t> rootmax_alive;

inline bool coefficient_ok(int k, int q) {
    return p3[q] >= (1ULL << k);
}

inline u64 class_key(int q, u64 R) {
    // 3^28 < 2^45, so q in the high byte and the residue in the low bits fit.
    return (u64(q) << 56) | (R % p3[q]);
}

// Scan all length-k parity words whose final q can equal a candidate q.
// Earlier coefficient survival is deliberately NOT imposed on competitors.
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

// Independent adjacent-start check from the credit-1 certificate.
bool avoids_root_credit1(u32 N) {
    u64 x = N;
    u64 y = N - 1;
    int qx = 0;
    int qy = 0;

    for (int k = 0; k < L; ++k) {
        if (x & 1ULL) {
            x = (3 * x + 1) >> 1;
            ++qx;
        } else {
            x >>= 1;
        }

        if (y & 1ULL) {
            y = (3 * y + 1) >> 1;
            ++qy;
        } else {
            y >>= 1;
        }

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

u64 count_block(const std::vector<u32>& dp, u64 C) {
    const u32 c = static_cast<u32>(C) & YMASK;
    u64 total = 0;
    for (u32 s = 0; s < YM; ++s)
        if (dp[s] && rootmax_alive[(c + s) & YMASK]) total += dp[s];
    return total;
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 40; ++i) p3[i] = p3[i - 1] * 3;

    // Independent previously recorded H<=22 regression, extended here to H=28.
    const u64 expected[29] = {
        0,
        1, 1, 2, 3, 4, 7, 11, 16, 31, 52, 103,
        182, 297, 593, 1049, 1720, 3439, 6104, 12194,
        22244, 38019, 75969,
        137657, 234156, 467895, 847493, 1442349, 2882872
    };

    std::vector<State> coefficient{{0, 0}};
    std::vector<State> nested{{0, 0}};
    u64 counts[29] = {};

    for (int k = 1; k <= L; ++k) {
        // Build all prefixes satisfying coefficient survival at every depth.
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

        // Candidate Hensel classes at this depth.
        std::unordered_map<u64, u64> class_max;
        class_max.reserve(coefficient.size() * 2);
        for (const State s : coefficient) {
            const u64 key = class_key(s.q, s.R);
            auto [it, inserted] = class_max.emplace(key, s.R);
            if (!inserted && s.R > it->second) it->second = s.R;
        }

        // Complete the maxima using all competitors with the same possible q.
        int qmin = 0;
        while (!coefficient_ok(k, qmin)) ++qmin;
        scan_all_words(0, k, 0, 0, qmin, class_max);

        // Propagate only prefixes that have been maximal at every prior depth.
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
        counts[k] = nested.size();
        if (counts[k] != expected[k]) std::exit(20 + k);
    }

    if (coefficient.size() != 3'524'586ULL) std::exit(60);
    if (nested.size() != 2'882'872ULL) std::exit(61);

    // Convert the surviving canonical starts modulo 2^28 to the z=(N-3)/4
    // residue address used by the ternary selector certificate.
    rootmax_alive.assign(YM, 0);
    u64 credit1_audit = 0;

    for (const State s : nested) {
        const u32 N = static_cast<u32>(
            ((0ULL - s.R) * invodd(p3[s.q])) & ((1ULL << L) - 1));

        if ((N & 3u) != 3u) std::exit(62);
        if (!avoids_root_credit1(N)) std::exit(63);
        ++credit1_audit;

        const u32 z = (N - 3u) >> 2;
        if (rootmax_alive[z]) std::exit(64); // parity-vector bijection audit
        rootmax_alive[z] = 1;
    }

    if (credit1_audit != 2'882'872ULL) std::exit(65);

    auto dp44 = selector_dp(44);
    auto dp33 = selector_dp(33);

    u64 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;

    const u64 m44_full = count_block(dp44, p44);
    const u64 m44_low33 = count_block(dp33, p44);
    const u64 m44_current = m44_full - m44_low33;
    const u64 m45_a = count_block(dp44, 3 * p44);
    const u64 m45_b = count_block(dp44, 4 * p44);
    const u64 m45_two = m45_a + m45_b;

    if (m44_full != 755'727'096'785ULL) std::exit(66);
    if (m44_low33 != 368'999'438ULL) std::exit(67);
    if (m44_current != 755'358'097'347ULL) std::exit(68);
    if (m45_a != 755'727'931'125ULL) std::exit(69);
    if (m45_b != 755'727'153'508ULL) std::exit(70);
    if (m45_two != 1'511'455'084'633ULL) std::exit(71);

    std::cout << "root full-max depth28 cross-base: PASS\n";
    std::cout << "nested_counts";
    for (int k = 1; k <= L; ++k) std::cout << ' ' << counts[k];
    std::cout << '\n';
    std::cout << "coefficient_language " << coefficient.size() << '\n';
    std::cout << "rootmax_alive_language " << nested.size() << '\n';
    std::cout << "m44_current_rootmax " << m44_current << '\n';
    std::cout << "m45_two_rootmax " << m45_two << '\n';
}
