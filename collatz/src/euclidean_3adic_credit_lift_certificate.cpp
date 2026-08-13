#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using u64 = std::uint64_t;
using i128 = __int128_t;

struct Agg {
    u64 lo = std::numeric_limits<u64>::max();
    u64 hi = 0;
};

static u64 pow3(int q) {
    u64 x = 1;
    for (int i = 0; i < q; ++i) x *= 3ULL;
    return x;
}

static u64 correction(u64 mask, int L) {
    u64 R = 0;
    for (int i = 0; i < L; ++i) {
        if ((mask >> i) & 1ULL) R = 3ULL * R + (1ULL << i);
    }
    return R;
}

static bool state_ok(
    u64 mask,
    const std::string& mechanical,
    int target_sigma,
    int target_minimum
) {
    int h = 0;
    int m = 0;
    for (int i = 0; i < static_cast<int>(mechanical.size()); ++i) {
        h += static_cast<int>((mask >> i) & 1ULL)
             - (mechanical[static_cast<std::size_t>(i)] - '0');
        m = std::min(m, h);
        if (m < target_minimum) return false;
    }
    return h == target_sigma && m == target_minimum;
}

static std::unordered_map<u64, Agg> residue_extrema(
    const std::string& mechanical,
    int q,
    int sigma,
    int minimum
) {
    const int L = static_cast<int>(mechanical.size());
    const u64 modulus = pow3(q);

    std::unordered_map<u64, Agg> out;
    u64 comb = (1ULL << q) - 1ULL;
    const u64 limit = 1ULL << L;

    while (comb < limit) {
        if (state_ok(comb, mechanical, sigma, minimum)) {
            const u64 R = correction(comb, L);
            Agg& a = out[R % modulus];
            a.lo = std::min(a.lo, R);
            a.hi = std::max(a.hi, R);
        }

        const u64 x = comb & (~comb + 1ULL);
        const u64 y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1ULL) | y;
    }

    return out;
}

static std::unordered_set<u64> positive_credits(
    const std::string& mechanical,
    int q,
    int sigma,
    int minimum
) {
    const int L = static_cast<int>(mechanical.size());
    const u64 modulus = pow3(q);

    std::unordered_map<u64, std::vector<u64>> buckets;
    u64 comb = (1ULL << q) - 1ULL;
    const u64 limit = 1ULL << L;

    while (comb < limit) {
        if (state_ok(comb, mechanical, sigma, minimum)) {
            const u64 R = correction(comb, L);
            buckets[R % modulus].push_back(R);
        }

        const u64 x = comb & (~comb + 1ULL);
        const u64 y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1ULL) | y;
    }

    std::unordered_set<u64> credits;
    for (auto& [residue, values] : buckets) {
        std::sort(values.begin(), values.end());
        for (std::size_t i = 0; i < values.size(); ++i) {
            for (std::size_t j = i + 1; j < values.size(); ++j) {
                const u64 diff = values[j] - values[i];
                if (diff % modulus == 0) credits.insert(diff / modulus);
            }
        }
    }
    return credits;
}

static long long best_cross_credit(
    const std::unordered_map<u64, Agg>& left,
    int L_left,
    int q_left,
    u64 right_credit
) {
    const u64 modulus = pow3(q_left);
    const u64 factor = 1ULL << L_left;

    const u64 target =
        (modulus - static_cast<u64>(
            (static_cast<i128>(factor % modulus) *
             static_cast<i128>(right_credit % modulus)) % modulus
        )) % modulus;

    long long best = -1;

    for (const auto& [r, a] : left) {
        const u64 r2 = (r + target) % modulus;
        const auto it = left.find(r2);
        if (it == left.end()) continue;

        const i128 numerator =
            static_cast<i128>(it->second.hi)
            - static_cast<i128>(a.lo)
            + static_cast<i128>(factor) * right_credit;

        if (numerator <= 0 || numerator % modulus != 0) continue;
        const long long credit = static_cast<long long>(numerator / modulus);
        best = std::max(best, credit);
    }

    return best;
}

int main() {
    const std::string U19 = "1010110110101101101";
    const std::string U27 = "011011011010110110101101101";

    // Level 46: left neutral U19 (q=12), right one-slack U27 (q=16).
    const auto left19 = residue_extrema(U19, 12, 0, 0);
    const auto right27_credits = positive_credits(U27, 16, -1, -1);

    long long best46 = -1;
    for (u64 d : right27_credits) {
        best46 = std::max(best46, best_cross_credit(left19, 19, 12, d));
    }

    std::cout << "level46_best_credit=" << best46 << '\n';
    if (best46 != 22) return 1;

    // Exact witness corrections from the independent full concatenation audit.
    const i128 R1 = static_cast<i128>(73753304060593ULL);
    const i128 R2 = static_cast<i128>(577042738069735ULL);
    const i128 mod28 = static_cast<i128>(pow3(28));
    if (R2 - R1 != 22 * mod28) return 2;

    // Opposite order diagnostic: neutral U27 + one-slack U19.
    const auto left27 = residue_extrema(U27, 17, 0, 0);
    const auto right19_credits = positive_credits(U19, 11, -1, -1);

    long long cross_reverse = -1;
    for (u64 d : right19_credits) {
        cross_reverse = std::max(
            cross_reverse,
            best_cross_credit(left27, 27, 17, d)
        );
    }
    std::cout << "level46_opposite_new_cross_credit=" << cross_reverse << '\n';
    if (cross_reverse != 17) return 3;

    // Level 73: reuse the already certified level-46 scalar credit 22 as
    // the right-block state. Only the neutral U27 classes are searched.
    const long long best73 = best_cross_credit(left27, 27, 17, 22);
    std::cout << "level73_best_credit_from_reused_22=" << best73 << '\n';
    if (best73 != 28) return 4;

    return 0;
}
