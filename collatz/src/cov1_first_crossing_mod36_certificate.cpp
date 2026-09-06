// Exact finite word-level audit for first coefficient crossings in the
// progression N = 36*k + 27.
//
// For a first-crossing parity word w of length L and odd count q,
//
//   T^L(N) = (3^q N + C(w))/2^L,
//   D = 2^L - 3^q > 0.
//
// The parity word fixes one canonical residue r mod 2^L.  Because r==3 mod 4
// on the COV-1 root, there is a unique a in {0,...,8} such that
//
//   N0 = r + a*2^L == 27 (mod 36).
//
// N0 is the least nonnegative member of the intersection between that parity
// cylinder and 36*N0+27.  Every other member is N0 + 9*t*2^L, and its
// crossing descent margin is larger by 9*t*(2^L-3^q).  Therefore it is enough
// to test N0.
//
// Exact completed audit on 2026-09-06:
//   * all root-11 first-crossing words through L<=38;
//   * 150,456,308 first-crossing words in total;
//   * zero words with T^L(N0) >= N0;
//   * smallest observed positive descent margin N0-T^L(N0) = 17,
//     at L=27, q=17, N0=495, endpoint=478,
//     word 111101110111010110110100010 (time order).
//
// This is FINITE ONLY.  It must not be extrapolated to arbitrary depth.
// Build: g++ -O3 -std=c++17 cov1_first_crossing_mod36_certificate.cpp -o cert
// Run:   ./cert 38

#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static int HMAX = 38;
static std::vector<u64> crossing_count;
static u64 total_crossings = 0;
static u64 best_gap = ~u64(0);
static u64 best_mask = 0;
static int best_L = 0, best_q = 0, best_a = 0;
static u64 best_N = 0, best_Y = 0;

u64 invodd64(u64 a) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

std::string word(u64 mask, int L) {
    std::string s;
    s.reserve(L);
    for (int i = 0; i < L; ++i)
        s.push_back(((mask >> i) & 1ULL) ? '1' : '0');
    return s;
}

void dfs(int k, int q, u128 C, u128 pow3, u64 maskw) {
    if (k >= HMAX) return;

    for (int bit = 0; bit <= 1; ++bit) {
        const int k2 = k + 1;
        const int q2 = q + bit;
        const u128 C2 = bit ? 3 * C + (u128(1) << k) : C;
        const u128 p32 = bit ? 3 * pow3 : pow3;
        const u128 p2 = u128(1) << k2;
        const u64 mask2 = maskw | (u64(bit) << k);

        if (p32 < p2) {
            // Parent survived, so this is the first coefficient crossing.
            ++crossing_count[k2];
            ++total_crossings;

            const u64 M = (u64(1) << k2) - 1;
            const u64 Cmod = u64(C2) & M;
            const u64 Pmod = u64(p32) & M;
            const u64 r = (0ULL - Cmod * invodd64(Pmod)) & M;

            // COV-1 members have the forced shortcut head 11, hence r==3 mod4.
            if ((r & 3ULL) != 3ULL) continue;

            const u64 twoL = u64(1) << k2;
            int a = -1;
            for (int t = 0; t < 9; ++t) {
                if ((r + u64(t) * twoL) % 36ULL == 27ULL) {
                    a = t;
                    break;
                }
            }
            if (a < 0) std::exit(2);

            const u128 N = u128(r) + u128(a) * p2;
            const u128 num = p32 * N + C2;
            if (num % p2 != 0) std::exit(3);
            const u128 Y = num / p2;

            // Any paradoxical first crossing in this finite audit is fatal.
            if (Y >= N) {
                std::cerr << "PARADOXICAL FIRST CROSSING at L=" << k2
                          << " q=" << q2 << "\n";
                std::exit(4);
            }

            const u64 gap = u64(N - Y);
            if (gap < best_gap) {
                best_gap = gap;
                best_mask = mask2;
                best_L = k2;
                best_q = q2;
                best_a = a;
                best_N = u64(N);
                best_Y = u64(Y);
            }
            continue;
        }

        dfs(k2, q2, C2, p32, mask2);
    }
}

int main(int argc, char** argv) {
    if (argc > 1) HMAX = std::atoi(argv[1]);
    if (HMAX < 2 || HMAX > 38) return 5;

    crossing_count.assign(HMAX + 1, 0);

    // Every 36*k+27 begins with shortcut parity head 11.
    // After bits 0,1: q=2, C=5, 3^q=9.
    dfs(2, 2, 5, 9, 3);

    if (HMAX == 38) {
        if (total_crossings != 150456308ULL) return 6;
        if (best_gap != 17ULL || best_L != 27 || best_q != 17 ||
            best_N != 495ULL || best_Y != 478ULL ||
            word(best_mask, best_L) != "111101110111010110110100010")
            return 7;
    }

    std::cout << "COV-1 first-crossing finite audit: PASS\n";
    std::cout << "HMAX " << HMAX << '\n';
    std::cout << "first_crossing_words " << total_crossings << '\n';
    std::cout << "paradoxical_words 0\n";
    std::cout << "minimum_descent_gap " << best_gap << '\n';
    std::cout << "closest L=" << best_L << " q=" << best_q
              << " a=" << best_a << " N=" << best_N
              << " endpoint=" << best_Y << '\n';
    std::cout << "closest_word " << word(best_mask, best_L) << '\n';
    std::cout << "FINITE ONLY\n";

    return 0;
}
