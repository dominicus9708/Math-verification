// Exact A0 s=1 first-75 Hamming-radius-seven direct certificate.
//
// Enumerates every PURE-BALLOT length-75 word at Hamming distance <= 7 from
// the exact threshold word, computes its universal 2-adic address modulo
// 2^75, imposes the strict physical shell and the previously certified X
// upper bound, then deterministically extends the actual Collatz orbit.
//
// Result at exact distance 7:
//   ballot words     188,574,243
//   physical words    11,784,860
//   bounded words      4,662,684
//   latest failure           454
//   scan survivors             0
//
// Together with radii 0..6, every A0 s=1 survivor satisfying the earlier
// X bound must have first-75 Hamming distance >= 8 from the threshold word.
//
// This is a finite necessary-condition certificate. It does not certify C4F
// and is not a proof of the Collatz conjecture.

#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <cstdint>
#include <iostream>
#include <string>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using boost::multiprecision::uint256_t;
using u128 = unsigned __int128;

namespace {

constexpr int H = 75;
constexpr int MAX_DEV = 7;
constexpr int MAX_SCAN = 1000;

std::array<int, MAX_SCAN + 1> req{};
std::array<int, MAX_SCAN> threshold{};
std::array<u128, H + 1> inv3_pow{};

u128 mask75;
u128 x_lo;
u128 x_hi;
u128 x_max;

std::array<unsigned long long, MAX_DEV + 1> ballot_words{};
std::array<unsigned long long, MAX_DEV + 1> physical_words{};
std::array<unsigned long long, MAX_DEV + 1> bounded_words{};
std::array<int, MAX_DEV + 1> latest_failure{};
std::array<unsigned long long, MAX_DEV + 1> scan_survivors{};

u128 parse_u128(const std::string& s) {
    u128 x = 0;
    for (char c : s) {
        if (std::isdigit(static_cast<unsigned char>(c))) {
            x = 10 * x + static_cast<unsigned>(c - '0');
        }
    }
    return x;
}

void build_exact_threshold() {
    cpp_int p2 = 1;
    cpp_int p3 = 1;
    int k = 0;
    req[0] = 0;

    for (int n = 1; n <= MAX_SCAN; ++n) {
        p2 <<= 1;
        while (p3 <= p2) {
            p3 *= 3;
            ++k;
        }
        req[n] = k;
        threshold[n - 1] = req[n] - req[n - 1];
        assert(threshold[n - 1] == 0 || threshold[n - 1] == 1);
    }
}

void build_inverse_powers() {
    const uint256_t modulus = uint256_t(1) << H;
    const uint256_t mask = modulus - 1;

    uint256_t inv3 = 1;
    for (int i = 0; i < 8; ++i) {
        inv3 = inv3 * (2 - uint256_t(3) * inv3);
    }
    inv3 &= mask;
    assert((uint256_t(3) * inv3 & mask) == 1);

    uint256_t cur = 1;
    inv3_pow[0] = 1;
    for (int r = 1; r <= H; ++r) {
        cur = (cur * inv3) & mask;
        inv3_pow[r] = static_cast<u128>(cur);
    }
}

inline u128 address_atom(int rank, int pos) {
    assert(1 <= rank && rank <= H);
    assert(0 <= pos && pos < H);
    const int remaining = H - pos;
    const u128 low_mask = (u128(1) << remaining) - 1;
    return (inv3_pow[rank] & low_mask) << pos;
}

int first_ballot_failure(u128 X, u128 first75_word) {
    u128 x = X;
    int q = 0;

    for (int n = 1; n <= MAX_SCAN; ++n) {
        const int bit = static_cast<int>(x & 1);

        if (n <= H) {
            const int proposed = static_cast<int>((first75_word >> (n - 1)) & 1);
            assert(bit == proposed);
        }

        q += bit;
        if (q < req[n]) {
            return n;
        }

        if (bit) {
            assert(x <= (static_cast<u128>(-1) - 1) / 3);
            x = (3 * x + 1) / 2;
        } else {
            x /= 2;
        }
    }
    return 0;
}

void visit_leaf(int dev, u128 address, u128 word) {
    ++ballot_words[dev];

    if (!(x_lo < address && address < x_hi)) {
        return;
    }
    ++physical_words[dev];

    if (address > x_max) {
        return;
    }
    ++bounded_words[dev];

    const int failure = first_ballot_failure(address, word);
    if (failure == 0) {
        ++scan_survivors[dev];
    } else {
        latest_failure[dev] = std::max(latest_failure[dev], failure);
    }
}

void dfs(int pos, int surplus, int dev, int rank, u128 address, u128 word) {
    if (pos == H) {
        visit_leaf(dev, address, word);
        return;
    }

    const int tbit = threshold[pos];

    // Keep the threshold bit.
    if (tbit) {
        dfs(pos + 1, surplus, dev, rank + 1,
            (address - address_atom(rank + 1, pos)) & mask75,
            word | (u128(1) << pos));
    } else {
        dfs(pos + 1, surplus, dev, rank, address, word);
    }

    // Flip the threshold bit if both the Hamming budget and pure-ballot
    // surplus allow it.
    if (dev < MAX_DEV) {
        const int next_surplus = surplus + (tbit == 0 ? 1 : -1);
        if (next_surplus >= 0) {
            const int bit = 1 - tbit;
            if (bit) {
                dfs(pos + 1, next_surplus, dev + 1, rank + 1,
                    (address - address_atom(rank + 1, pos)) & mask75,
                    word | (u128(1) << pos));
            } else {
                dfs(pos + 1, next_surplus, dev + 1, rank, address, word);
            }
        }
    }
}

}  // namespace

int main() {
    mask75 = (u128(1) << 75) - 1;
    x_lo = u128(1) << 71;
    x_hi = u128(1) << 72;
    x_max = parse_u128("3295414002074039191016");

    build_exact_threshold();
    build_inverse_powers();
    dfs(0, 0, 0, 0, 0, 0);

    const std::array<unsigned long long, 8> expected_ballot = {
        1ULL,
        27ULL,
        987ULL,
        14'003ULL,
        248'564ULL,
        2'350'907ULL,
        26'996'805ULL,
        188'574'243ULL,
    };
    const std::array<unsigned long long, 8> expected_physical = {
        0ULL,
        1ULL,
        62ULL,
        916ULL,
        15'560ULL,
        147'027ULL,
        1'687'133ULL,
        11'784'860ULL,
    };
    const std::array<unsigned long long, 8> expected_bounded = {
        0ULL,
        1ULL,
        18ULL,
        386ULL,
        6'174ULL,
        58'212ULL,
        668'333ULL,
        4'662'684ULL,
    };
    const std::array<int, 8> expected_latest = {
        0, 88, 110, 161, 222, 378, 405, 454,
    };

    assert(ballot_words == expected_ballot);
    assert(physical_words == expected_physical);
    assert(bounded_words == expected_bounded);
    assert(latest_failure == expected_latest);
    for (auto n : scan_survivors) {
        assert(n == 0);
    }

    unsigned long long total_bounded = 0;
    for (auto n : bounded_words) total_bounded += n;
    assert(total_bounded == 5'395'808ULL);

    std::cout << "PASS A0 s=1 first-75 radius-seven direct certificate\n";
    std::cout << "distance7_ballot_words " << ballot_words[7] << "\n";
    std::cout << "distance7_physical_words " << physical_words[7] << "\n";
    std::cout << "distance7_bounded_words " << bounded_words[7] << "\n";
    std::cout << "distance7_latest_ballot_failure " << latest_failure[7] << "\n";
    std::cout << "bounded_words_radius_le_7 " << total_bounded << "\n";
    std::cout << "scan_survivors_radius_le_7 0\n";
    std::cout << "necessary_first75_hamming_distance >= 8\n";
    std::cout << "C4F_certified false\n";
    std::cout << "status SAFE finite necessary-condition closure\n";
}
