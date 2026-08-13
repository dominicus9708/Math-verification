#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

struct Aggregate {
    std::uint64_t lo = std::numeric_limits<std::uint64_t>::max();
    std::uint64_t hi = 0;
    std::uint32_t count = 0;
};

int main() {
    // Seventh finite return-word representative in the Euclidean hierarchy.
    const std::string mechanical = "011011011010110110101101101";
    const int L = static_cast<int>(mechanical.size());
    const int Q = static_cast<int>(
        std::count(mechanical.begin(), mechanical.end(), '1'));

    // Exact one-slack fibre: (Sigma,M)=(-1,-1), hence q=Q-1.
    const int q = Q - 1;

    std::uint64_t modulus = 1;
    for (int i = 0; i < q; ++i) modulus *= 3ULL;

    std::unordered_map<std::uint64_t, Aggregate> classes;
    classes.reserve(5'000'000);

    std::uint64_t fibre_count = 0;

    // Enumerate only q-subsets of the L positions (not all 2^L words).
    // L=27 and q=16 fit safely in uint32_t.
    std::uint32_t comb = (1U << q) - 1U;
    const std::uint32_t limit = 1U << L;

    while (comb < limit) {
        int height = 0;
        int minimum = 0;
        bool admissible = true;

        for (int i = 0; i < L; ++i) {
            const int actual = static_cast<int>((comb >> i) & 1U);
            const int reference = mechanical[static_cast<std::size_t>(i)] - '0';
            height += actual - reference;
            minimum = std::min(minimum, height);
            if (minimum < -1) {
                admissible = false;
                break;
            }
        }

        if (admissible && height == -1 && minimum == -1) {
            std::uint64_t R = 0;
            for (int i = 0; i < L; ++i) {
                if ((comb >> i) & 1U) {
                    R = 3ULL * R + (1ULL << i);
                }
            }

            Aggregate& a = classes[R % modulus];
            a.lo = std::min(a.lo, R);
            a.hi = std::max(a.hi, R);
            ++a.count;
            ++fibre_count;
        }

        // Gosper's hack: next q-bit combination.
        const std::uint32_t x = comb & (~comb + 1U);
        const std::uint32_t y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1U) | y;
    }

    std::uint64_t covered = 0;
    std::uint64_t max_credit = 0;
    std::uint64_t best_residue = 0;
    std::uint64_t best_lo = 0;
    std::uint64_t best_hi = 0;

    for (const auto& [residue, a] : classes) {
        if (a.count <= 1) continue;

        // For fixed L and q, exact corrections are injective in the parity
        // word.  In one residue class every orientation except the unique
        // maximum has a larger same-residue correction and therefore a
        // positive integer predecessor credit.
        covered += static_cast<std::uint64_t>(a.count) - 1ULL;

        const std::uint64_t diff = a.hi - a.lo;
        const std::uint64_t credit = diff / modulus;
        if (credit > max_credit) {
            max_credit = credit;
            best_residue = residue;
            best_lo = a.lo;
            best_hi = a.hi;
        }
    }

    const long double coverage =
        static_cast<long double>(covered) /
        static_cast<long double>(fibre_count);

    std::cout << "L=" << L << " Q=" << Q << " q=" << q << '\n';
    std::cout << "3^q=" << modulus << '\n';
    std::cout << "fibre=" << fibre_count << '\n';
    std::cout << "residue_classes=" << classes.size() << '\n';
    std::cout << "covered=" << covered << '\n';
    std::cout << std::setprecision(16)
              << "coverage=" << coverage << '\n';
    std::cout << "max_credit=" << max_credit << '\n';
    std::cout << "best_residue=" << best_residue << '\n';
    std::cout << "best_lo=" << best_lo << '\n';
    std::cout << "best_hi=" << best_hi << '\n';
    std::cout << "difference=" << (best_hi - best_lo) << '\n';

    // Exact certificate values.
    if (L != 27 || Q != 17 || q != 16) return 1;
    if (modulus != 43'046'721ULL) return 2;
    if (fibre_count != 4'717'204ULL) return 3;
    if (classes.size() != 2'994'059ULL) return 4;
    if (covered != 1'723'145ULL) return 5;
    if (max_credit != 19ULL) return 6;
    if (best_residue != 36'691'711ULL) return 7;
    if (best_lo != 122'785'153ULL) return 8;
    if (best_hi != 940'672'852ULL) return 9;
    if (best_hi - best_lo != 19ULL * modulus) return 10;

    return 0;
}
