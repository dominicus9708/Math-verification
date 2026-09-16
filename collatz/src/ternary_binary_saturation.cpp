#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

// Exact packed-bit verifier for
// { sum_{i=0}^{m-1} a_i 3^i mod 2^B : a_i in {0,1} }.
//
// Default B=32 is the practical setting (~1 GiB for two bitsets).
// B=33 reproduces the high-memory certificate in the accompanying note
// (~2 GiB for two bitsets).  This is a finite verifier, not a Collatz proof.

int main(int argc, char** argv) {
    const int B = argc > 1 ? std::atoi(argv[1]) : 32;
    const int m = argc > 2 ? std::atoi(argv[2]) : 40;

    if (B < 6 || B > 33 || m < 0) {
        std::cerr << "usage: ternary_binary_saturation [6..33] [m>=0]\n";
        return 2;
    }

    const std::uint64_t nbits = std::uint64_t{1} << B;
    const std::uint64_t mask = nbits - 1;
    const std::size_t words = static_cast<std::size_t>(nbits >> 6);

    std::vector<std::uint64_t> support(words, 0);
    std::vector<std::uint64_t> shifted(words, 0);
    support[0] = 1;

    std::uint64_t weight = 1; // 3^0 mod 2^B

    for (int i = 0; i < m; ++i) {
        const std::uint64_t word_shift = weight >> 6;
        const unsigned bit_shift = static_cast<unsigned>(weight & 63);

        // shifted = cyclic left rotation of support by 'weight' bits.
        // For destination word j, read the 64-bit window beginning at
        // (64*j-weight) mod 2^B from the old support bitset.
        for (std::size_t j = 0; j < words; ++j) {
            const std::uint64_t source_bit =
                ((static_cast<std::uint64_t>(j) << 6) - weight) & mask;
            const std::size_t k = static_cast<std::size_t>(source_bit >> 6);
            const unsigned off = static_cast<unsigned>(source_bit & 63);
            if (off == 0) {
                shifted[j] = support[k];
            } else {
                const std::size_t k2 = (k + 1) & (words - 1);
                shifted[j] = (support[k] >> off) |
                             (support[k2] << (64 - off));
            }
        }

        for (std::size_t j = 0; j < words; ++j) {
            support[j] |= shifted[j];
        }

        weight = static_cast<std::uint64_t>(
            (static_cast<__uint128_t>(weight) * 3) & mask);
    }

    std::uint64_t missing = 0;
    for (std::uint64_t w : support) {
        missing += 64u - static_cast<unsigned>(__builtin_popcountll(w));
    }

    std::cout << "B=" << B << " m=" << m
              << " missing=" << missing << '\n';

    return missing == 0 ? 0 : 1;
}
