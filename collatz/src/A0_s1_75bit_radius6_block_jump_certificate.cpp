// Exact A0 s=1 first-75 Hamming-radius-six block-jump certificate.
//
// This is an independent direct-75-bit cross-check of the earlier Python
// near-threshold certificate.  It enumerates every PURE-BALLOT length-75 word
// at Hamming distance <= 6 from the exact lower-ballot threshold word,
// computes its universal 2-adic parity address modulo 2^75, imposes the
// strict physical shell and the previously certified X upper bound, then
// deterministically extends the actual Collatz orbit.
//
// Result: all 668,333 exact-distance-six bounded physical candidates lose
// pure ballot by prefix 405.  Together with the certified radii 0..5 closure,
// any full A0 s=1 survivor satisfying the earlier X bound must have
// first-75 Hamming distance >= 7 from the threshold word.
//
// This is a finite necessary-condition certificate only.  C4F and the full
// t0 bridge remain separate open gates.  This is not a Collatz proof.

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
constexpr int MAX_DEV = 6;
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

    // Newton iteration for the inverse of 3 modulo 2^75.
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

// Verify the proposed first-75 word directly against the orbit of X and
// return the first 1-indexed pure-ballot failure, or 0 if none <= MAX_SCAN.
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
            // All audited trajectories stay far below this guard.  Its only
            // purpose is to make accidental u128 overflow impossible.
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
    {
        const int bit = tbit;
        const int next_rank = rank + bit;
        u128 next_address = address;
        u128 next_word = word;
        if (bit) {
            next_address = (address - address_atom(next_rank, pos)) & mask75;
            next_word |= u128(1) << pos;
        }
        dfs(pos + 1, surplus, dev, next_rank, next_address, next_word);
    }

    // Flip the threshold bit if the Hamming budget and pure-ballot surplus
    // permit it.  A 0->1 flip creates one unit; a 1->0 flip consumes one.
    if (dev < MAX_DEV) {
        const int next_surplus = surplus + (tbit == 0 ? 1 : -1);
        if (next_surplus >= 0) {
            const int bit = 1 - tbit;
            const int next_rank = rank + bit;
            u128 next_address = address;
            u128 next_word = word;
            if (bit) {
                next_address = (address - address_atom(next_rank, pos)) & mask75;
                next_word |= u128(1) << pos;
            }
            dfs(pos + 1, next_surplus, dev + 1, next_rank, next_address, next_word);
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

    const std::array<unsigned long long, 7> expected_ballot = {
        1ULL,
        27ULL,
        987ULL,
        14'003ULL,
        248'564ULL,
        2'350'907ULL,
        26'996'805ULL,
    };
    const std::array<unsigned long long, 7> expected_physical = {
        0ULL,
        1ULL,
        62ULL,
        916ULL,
        15'560ULL,
        147'027ULL,
        1'687'133ULL,
    };
    const std::array<unsigned long long, 7> expected_bounded = {
        0ULL,
        1ULL,
        18ULL,
        386ULL,
        6'174ULL,
        58'212ULL,
        668'333ULL,
    };
    const std::array<int, 7> expected_latest = {
        0, 88, 110, 161, 222, 378, 405,
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
    assert(total_bounded == 733'124ULL);

    std::cout << "PASS A0 s=1 first-75 radius-six block-jump certificate\n";
    std::cout << "distance6_ballot_words " << ballot_words[6] << "\n";
    std::cout << "distance6_physical_words " << physical_words[6] << "\n";
    std::cout << "distance6_bounded_words " << bounded_words[6] << "\n";
    std::cout << "distance6_latest_ballot_failure " << latest_failure[6] << "\n";
    std::cout << "bounded_words_radius_le_6 " << total_bounded << "\n";
    std::cout << "scan_survivors_radius_le_6 0\n";
    std::cout << "necessary_first75_hamming_distance >= 7\n";
    std::cout << "C4F_certified false\n";
    std::cout << "status SAFE finite necessary-condition closure\n";
}
