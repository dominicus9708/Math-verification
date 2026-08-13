#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

// Exact balanced-difference certificate for the neutral U6 block.
// For every residue r mod 3^12, compute the smallest absolute actual
// correction difference DeltaR congruent to r.  The maximum of those
// minima is the exact balanced covering radius used in the controlled
// successor theorem.

int main() {
    const std::string mechanical = "1010110110101101101";
    const int L = 19;
    const int Q = 12;

    std::uint64_t modulus = 1;
    for (int i = 0; i < Q; ++i) modulus *= 3ULL;
    if (modulus != 531'441ULL) return 1;

    std::vector<std::uint64_t> corrections;

    std::uint32_t comb = (1U << Q) - 1U;
    const std::uint32_t limit = 1U << L;

    while (comb < limit) {
        int h = 0;
        bool admissible = true;
        for (int i = 0; i < L; ++i) {
            h += static_cast<int>((comb >> i) & 1U)
               - static_cast<int>(mechanical[static_cast<std::size_t>(i)] - '0');
            if (h < 0) {
                admissible = false;
                break;
            }
        }

        if (admissible && h == 0) {
            std::uint64_t R = 0;
            for (int i = 0; i < L; ++i) {
                if ((comb >> i) & 1U) R = 3ULL * R + (1ULL << i);
            }
            corrections.push_back(R);
        }

        const std::uint32_t x = comb & (~comb + 1U);
        const std::uint32_t y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1U) | y;
    }

    if (corrections.size() != 11'433ULL) return 2;

    const auto INF = std::numeric_limits<std::uint64_t>::max();
    std::vector<std::uint64_t> best(modulus, INF);

    for (const auto a : corrections) {
        for (const auto b : corrections) {
            const long long d = static_cast<long long>(a) - static_cast<long long>(b);
            long long r = d % static_cast<long long>(modulus);
            if (r < 0) r += static_cast<long long>(modulus);
            const std::uint64_t ad = d < 0
                ? static_cast<std::uint64_t>(-d)
                : static_cast<std::uint64_t>(d);
            best[static_cast<std::size_t>(r)] =
                std::min(best[static_cast<std::size_t>(r)], ad);
        }
    }

    std::uint64_t radius = 0;
    std::uint64_t worst_residue = 0;
    for (std::uint64_t r = 0; r < modulus; ++r) {
        if (best[r] == INF) return 3;
        if (best[r] > radius) {
            radius = best[r];
            worst_residue = r;
        }
    }

    if (radius != 1'056'728ULL) return 4;
    if (worst_residue != 6'154ULL) return 5;

    // Exact decimal-free comparison radius/modulus < 1.989.
    if (1000ULL * radius >= 1989ULL * modulus) return 6;

    std::cout << "neutral_words=" << corrections.size() << '\n';
    std::cout << "modulus=" << modulus << '\n';
    std::cout << "balanced_radius=" << radius << '\n';
    std::cout << "worst_residue=" << worst_residue << '\n';
    std::cout << "controlled_error_lt_1.989=true\n";
    return 0;
}
