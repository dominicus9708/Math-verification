#include <algorithm>
#include <cstdint>
#include <iostream>

int main() {
    // Certified prefix for beta=log_2(3/2):
    // [0;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,...]
    const int a[] = {0,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4};
    std::uint64_t q[17];
    q[0] = 1;
    q[1] = 1;
    for (int i = 2; i <= 16; ++i) q[i] = (std::uint64_t)a[i] * q[i-1] + q[i-2];

    if (q[16] != 53'715'833ULL) return 2;

    // This safely exceeds every run length allowed by the corrected
    // elementary amplitude ceiling used before applying DK/Ostrowski.
    const std::uint64_t NMAX = 42'000'000ULL;

    int best = -1;
    std::uint64_t arg = 0;

    // Greedy expansion is the canonical Ostrowski representation.
    // Since a1=1, b0=0; for i>=1, bi<=a_{i+1}.
    for (std::uint64_t N = 0; N <= NMAX; ++N) {
        std::uint64_t rem = N;
        int digit_sum = 0;

        for (int i = 15; i >= 1; --i) {
            const std::uint64_t b = std::min<std::uint64_t>(a[i+1], rem / q[i]);
            rem -= b * q[i];
            digit_sum += (int)b;
        }

        if (rem != 0) return 3;
        if (digit_sum > best) {
            best = digit_sum;
            arg = N;
        }
    }

    std::cout
        << "q16=" << q[16]
        << " max_digit_sum=" << best
        << " first_arg=" << arg
        << '\n';

    if (best != 92) return 4;
    if (arg != 32'025'449ULL) return 5;
    return 0;
}
