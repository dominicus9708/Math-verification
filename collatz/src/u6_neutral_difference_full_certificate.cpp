#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

// Exact finite certificate for the base neutral U6 difference set.
// U6 = 1010110110101101101, L=19, Q=12.

int main() {
    const std::string mechanical = "1010110110101101101";
    const int L = 19;
    const int Q = 12;

    std::uint64_t modulus = 1;
    for (int i = 0; i < Q; ++i) modulus *= 3ULL;
    if (modulus != 531'441ULL) return 1;

    std::vector<std::uint64_t> residues;
    std::uint64_t neutral_words = 0;
    std::uint64_t min_correction = ~0ULL;
    std::uint64_t max_correction = 0;

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

    std::sort(residues.begin(), residues.end());
    residues.erase(std::unique(residues.begin(), residues.end()), residues.end());

    if (neutral_words != 11'433ULL) return 2;
    if (residues.size() != 11'433ULL) return 3;
    if (min_correction != 527'345ULL) return 4;
    if (max_correction != 2'960'239ULL) return 5;
    if (max_correction - min_correction != 2'432'894ULL) return 6;

    std::vector<unsigned char> seen(modulus, 0);
    for (const auto a : residues) {
        for (const auto b : residues) {
            const std::uint64_t d = (a >= b) ? (a - b) : (a + modulus - b);
            seen[d] = 1;
        }
    }

    std::uint64_t covered = 0;
    for (const auto x : seen) covered += x;
    if (covered != modulus) return 7;

    std::cout << "neutral_words=" << neutral_words << '\n';
    std::cout << "unique_residues=" << residues.size() << '\n';
    std::cout << "difference_covered=" << covered << '/' << modulus << '\n';
    std::cout << "correction_width=" << (max_correction - min_correction) << '\n';
    return 0;
}
