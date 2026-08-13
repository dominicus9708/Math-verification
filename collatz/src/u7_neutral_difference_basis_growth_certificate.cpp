#include <algorithm>
#include <atomic>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>
#include <omp.h>

// Exact finite certificate for the neutral U7 correction-difference basis.
//
// Mechanical block:
//   U7 = 011011011010110110101101101
//   L=27, Q=17.
//
// We enumerate only the neutral state (Sigma,M)=(0,0), collect its exact
// correction residues modulo 3^17, then deterministically select the 90,000
// residues having the smallest splitmix64 keys.  The cyclic difference set
// of this fixed subset is checked to equal all of Z/(3^17)Z.
//
// This proves a fortiori that the full neutral correction-residue set S7 has
// S7-S7 = Z/(3^17)Z.  Combined with the exact correction width it yields the
// uniform successor-growth lemma D>=191 => some neutral U7 successor D'>D.

static inline std::uint64_t mix64(std::uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

int main() {
    const std::string mechanical = "011011011010110110101101101";
    const int L = 27;
    const int Q = 17;
    const int SAMPLE = 90'000;

    std::uint64_t modulus = 1;
    for (int i = 0; i < Q; ++i) modulus *= 3ULL;
    if (modulus != 129'140'163ULL) return 1;

    std::vector<std::uint64_t> residues;
    residues.reserve(1'800'000);

    std::uint64_t min_correction = std::numeric_limits<std::uint64_t>::max();
    std::uint64_t max_correction = 0;
    std::uint64_t neutral_words = 0;

    // Neutral state has exactly Q actual ones.  Enumerate Q-subsets of L
    // positions with Gosper's hack, not all 2^L words.
    std::uint32_t comb = (1U << Q) - 1U;
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
            if (minimum < 0) {
                admissible = false;
                break;
            }
        }

        if (admissible && height == 0) {
            std::uint64_t R = 0;
            for (int i = 0; i < L; ++i) {
                if ((comb >> i) & 1U) R = 3ULL * R + (1ULL << i);
            }
            residues.push_back(R % modulus);
            min_correction = std::min(min_correction, R);
            max_correction = std::max(max_correction, R);
            ++neutral_words;
        }

        const std::uint32_t x = comb & (~comb + 1U);
        const std::uint32_t y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1U) | y;
    }

    if (neutral_words != 1'741'350ULL) return 2;
    if (min_correction != 129'009'091ULL) return 3;
    if (max_correction != 1'096'880'542ULL) return 4;

    std::sort(residues.begin(), residues.end());
    residues.erase(std::unique(residues.begin(), residues.end()), residues.end());
    if (residues.size() != 1'478'620ULL) return 5;

    // Fixed deterministic 90,000-element basis: smallest lexicographic
    // pairs (splitmix64(residue), residue).
    std::vector<std::pair<std::uint64_t, std::uint64_t>> keyed;
    keyed.reserve(residues.size());
    for (const auto r : residues) keyed.emplace_back(mix64(r), r);

    std::nth_element(keyed.begin(), keyed.begin() + SAMPLE, keyed.end());
    keyed.resize(SAMPLE);

    std::vector<std::uint64_t> basis;
    basis.reserve(SAMPLE);
    for (const auto& [key, r] : keyed) {
        (void)key;
        basis.push_back(r);
    }

    // Exact cyclic difference coverage bitset. Atomic OR makes the OpenMP
    // computation race-free and exact.
    const std::size_t words = (modulus + 63ULL) / 64ULL;
    std::vector<std::atomic<std::uint64_t>> bits(words);
    for (auto& x : bits) x.store(0, std::memory_order_relaxed);

    #pragma omp parallel for schedule(static)
    for (int i = 0; i < SAMPLE; ++i) {
        const std::uint64_t a = basis[static_cast<std::size_t>(i)];
        for (int j = 0; j < SAMPLE; ++j) {
            const std::uint64_t b = basis[static_cast<std::size_t>(j)];
            const std::uint64_t d = (a >= b) ? (a - b) : (a + modulus - b);
            bits[d >> 6].fetch_or(1ULL << (d & 63ULL), std::memory_order_relaxed);
        }
    }

    std::uint64_t covered = 0;
    for (const auto& x : bits) covered += __builtin_popcountll(x.load());
    if (covered != modulus) return 6;

    const std::uint64_t width = max_correction - min_correction;
    if (width != 967'871'451ULL) return 7;

    const std::uint64_t expansion_numerator = (1ULL << 27) - modulus;
    if (expansion_numerator != 5'077'565ULL) return 8;

    // Exact sharp integer threshold from
    //   ((2^27-3^17) D > width).
    if (expansion_numerator * 190ULL >= width) return 9;
    if (expansion_numerator * 191ULL <= width) return 10;

    std::cout << "neutral_words=" << neutral_words << '\n';
    std::cout << "unique_residues=" << residues.size() << '\n';
    std::cout << "basis_size=" << SAMPLE << '\n';
    std::cout << "difference_covered=" << covered << '/' << modulus << '\n';
    std::cout << "correction_min=" << min_correction << '\n';
    std::cout << "correction_max=" << max_correction << '\n';
    std::cout << "correction_width=" << width << '\n';
    std::cout << "uniform_growth_threshold=191\n";
    return 0;
}
