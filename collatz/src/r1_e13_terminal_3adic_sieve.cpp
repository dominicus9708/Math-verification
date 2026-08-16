#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>

// Exact terminal 3-adic residue sieve for the E=13 pre-G13 pullback.
//
// Dependency from the exact run-cap certificates:
// for every ordinary root <= current NMAX, event ranks j=0..4 cannot occur
// late enough to affect C(P) modulo 3^K for any 6<=K<=18.  Hence the active
// low-3-adic correction ranks form a terminal block beginning at j0>=5.
//
// For modulus 3^K, an active rank j has
//
//   p_j = 1526 + j - (K-1) + b_j,
//   0 <= b_j <= K-1,
//
// with the b_j nondecreasing.  This finite suffix over-family contains every
// ordinary E=13 correction residue modulo 3^K.
//
// For a fixed actual correction residue c, an alternate E=13 pullback for G13
// credit delta requires
//
//   c' = c - 2^1539 delta (mod 3^K)
//
// with c' in the same residue set.  The program counts how many bounded
// credits delta=1..397 survive for every c.
//
// Exact checkpoints:
// K  |S_K|    min max surviving credits
//  6      462 248 255
//  7     1250 218 234
//  8     3157 180 206
//  9     7335 132 162
// 10    15677  88 122
// 11    31072  48  88
// 12    57741  25  62
// 13   101699  10  42
// 14   171305   1  32
// 15   277949   0  21
// 16   436868   0  15
// 17   668128   0  12
// 18   997755   0   9
//
// At K=18 the exact histogram is
//   0:363470 1:382882 2:184796 3:54024 4:10818
//   5:1561 6:172 7:27 8:3 9:2.
//
// Every delta=1..397 remains realizable for at least one pair of residues at
// K=18, so this is a conditioned actual-residue sieve, not a universal credit
// exclusion theorem and not a Collatz proof.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr int T = 1539;
constexpr int Q = 1526;
constexpr int MAX_CREDIT = 397;

int K = 18;
u64 MOD = 1;
std::vector<u64> bits;
std::vector<u64> residues;
std::vector<std::vector<u64>> term;

u64 mod_pow(u64 a, u64 e, u64 m) {
    u64 r = 1 % m;
    while (e) {
        if (e & 1) r = static_cast<u64>((u128)r * a % m);
        a = static_cast<u64>((u128)a * a % m);
        e >>= 1;
    }
    return r;
}

bool has(u64 x) {
    return (bits[x >> 6] >> (x & 63)) & 1ULL;
}

void add_residue(u64 x) {
    x %= MOD;
    if (!has(x)) {
        bits[x >> 6] |= 1ULL << (x & 63);
        residues.push_back(x);
    }
}

void enumerate_suffix(int j, int last_b, u64 acc) {
    if (j == 13) {
        add_residue(acc);
        return;
    }
    for (int b = last_b; b < K; ++b) {
        enumerate_suffix(j + 1, b, (acc + term[j][b]) % MOD);
    }
}

struct Expected {
    std::size_t size;
    int min_survive;
    int max_survive;
};

Expected expected_for(int k) {
    switch (k) {
        case 6:  return {462, 248, 255};
        case 7:  return {1250, 218, 234};
        case 8:  return {3157, 180, 206};
        case 9:  return {7335, 132, 162};
        case 10: return {15677, 88, 122};
        case 11: return {31072, 48, 88};
        case 12: return {57741, 25, 62};
        case 13: return {101699, 10, 42};
        case 14: return {171305, 1, 32};
        case 15: return {277949, 0, 21};
        case 16: return {436868, 0, 15};
        case 17: return {668128, 0, 12};
        case 18: return {997755, 0, 9};
        default: std::abort();
    }
}

}  // namespace

int main(int argc, char** argv) {
    if (argc > 1) K = std::atoi(argv[1]);
    if (K < 6 || K > 18) {
        std::cerr << "K must lie in 6..18 for this certified table.\n";
        return 2;
    }

    MOD = 1;
    for (int i = 0; i < K; ++i) MOD *= 3;

    bits.assign((MOD + 63) / 64, 0);
    term.assign(13, std::vector<u64>(K, 0));

    // Precompute the active terminal correction term for rank j and offset b.
    for (int j = 5; j < 13; ++j) {
        for (int b = 0; b < K; ++b) {
            const int p = Q + j - (K - 1) + b;
            const int e3 = Q - p + j;
            assert(e3 == K - 1 - b);
            assert(e3 >= 0);

            u64 v = mod_pow(2, static_cast<u64>(p), MOD);
            for (int z = 0; z < e3; ++z) v = (v * 3) % MOD;
            term[j][b] = v;
        }
    }

    add_residue(0);  // no correction term reaches the low K ternary digits

    for (int j0 = 5; j0 < 13; ++j0) {
        enumerate_suffix(j0, 0, 0);
    }

    const Expected expected = expected_for(K);
    assert(residues.size() == expected.size);

    const u64 shift = mod_pow(2, T, MOD);
    std::array<u64, MAX_CREDIT + 1> shifts{};
    for (int delta = 1; delta <= MAX_CREDIT; ++delta) {
        shifts[delta] = static_cast<u64>((u128)shift * delta % MOD);
    }

    int min_survive = MAX_CREDIT + 1;
    int max_survive = -1;
    unsigned long long total_survive = 0;
    std::array<unsigned long long, MAX_CREDIT + 1> histogram{};

    for (u64 c : residues) {
        int count = 0;
        for (int delta = 1; delta <= MAX_CREDIT; ++delta) {
            const u64 c_alt = (c + MOD - shifts[delta]) % MOD;
            if (has(c_alt)) ++count;
        }
        min_survive = std::min(min_survive, count);
        max_survive = std::max(max_survive, count);
        total_survive += static_cast<unsigned long long>(count);
        ++histogram[count];
    }

    assert(min_survive == expected.min_survive);
    assert(max_survive == expected.max_survive);

    // Check whether any bounded credit is universally absent at this quotient.
    int pair_realizable_credits = 0;
    for (int delta = 1; delta <= MAX_CREDIT; ++delta) {
        bool ok = false;
        for (u64 c : residues) {
            const u64 c_alt = (c + MOD - shifts[delta]) % MOD;
            if (has(c_alt)) {
                ok = true;
                break;
            }
        }
        if (ok) ++pair_realizable_credits;
    }
    assert(pair_realizable_credits == MAX_CREDIT);

    if (K == 18) {
        const std::array<unsigned long long, 10> expected_hist{
            363470, 382882, 184796, 54024, 10818,
            1561, 172, 27, 3, 2
        };
        for (int i = 0; i <= 9; ++i) assert(histogram[i] == expected_hist[i]);
        for (int i = 10; i <= MAX_CREDIT; ++i) assert(histogram[i] == 0);
    }

    std::cout << "R1 E=13 terminal 3-adic sieve: PASS\n";
    std::cout << "K=" << K << " modulus=" << MOD
              << " residue_set=" << residues.size() << "\n";
    std::cout << std::setprecision(12)
              << "residue_density="
              << static_cast<double>(residues.size()) / static_cast<double>(MOD)
              << "\n";
    std::cout << "surviving bounded credits per fixed actual residue: "
              << min_survive << ".." << max_survive << "\n";
    std::cout << "mean_surviving_credits="
              << static_cast<double>(total_survive) /
                     static_cast<double>(residues.size())
              << "\n";
    std::cout << "globally pair-realizable credits among 1..397="
              << pair_realizable_credits << "\n";

    if (K == 18) {
        std::cout << "K18 histogram:";
        for (int i = 0; i <= 9; ++i) {
            std::cout << " " << i << ":" << histogram[i];
        }
        std::cout << "\n";
    }

    return 0;
}
