#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::uint256_t;
using boost::multiprecision::uint1024_t;
using u128 = unsigned __int128;

constexpr int B = 73;
constexpr int T = 1539;
constexpr int KMAX = 5;
constexpr int EVEN_LIMIT = 12; // seek a 13th even event
const u128 MASK = (u128(1) << B) - 1;

std::array<u128,B+1> p3m, inv3m;
std::array<uint256_t,B+1> p3f;
u128 segm[B+1][B+1];
uint256_t segf[B+1][B+1];
std::uint64_t total = 0, survivors = 0;
int latest_13th_even = 0;

u128 inv_odd(u128 a) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    return x & MASK;
}

void evaluate(const std::vector<int>& zeros) {
    const int k = int(zeros.size());
    const int q = B - k;
    ++total;

    u128 Rm = 0;
    uint256_t Rf = 0;
    int p = 0;
    auto add_ones_run = [&](int start, int len) {
        if (len <= 0) return;
        Rm = (p3m[len] * Rm + segm[start][len]) & MASK;
        Rf = p3f[len] * Rf + segf[start][len];
    };
    for (int z : zeros) {
        add_ones_run(p, z - p);
        p = z + 1;
    }
    add_ones_run(p, B - p);

    const u128 N = ((u128(0) - Rm) * inv3m[q]) & MASK;
    if (N == 0) return;

    // Exact endpoint after the prescribed first 73 parity bits.
    const uint256_t y73 = (p3f[q] * uint256_t(N) + Rf) >> B;
    uint1024_t x = y73;
    int evens = k;
    int t = B;
    while (t < T && evens <= EVEN_LIMIT) {
        if ((x & 1) != 0) x = (3 * x + 1) >> 1;
        else { x >>= 1; ++evens; }
        ++t;
    }

    if (evens <= EVEN_LIMIT) {
        ++survivors;
    } else {
        latest_13th_even = std::max(latest_13th_even, t);
    }
}

void enumerate(int need, int next, std::vector<int>& zeros) {
    if (need == 0) {
        evaluate(zeros);
        return;
    }
    for (int p = next; p <= B - need; ++p) {
        zeros.push_back(p);
        enumerate(need - 1, p + 1, zeros);
        zeros.pop_back();
    }
}

int main() {
    p3m[0] = 1;
    p3f[0] = 1;
    for (int i = 1; i <= B; ++i) {
        p3m[i] = (p3m[i-1] * 3) & MASK;
        p3f[i] = p3f[i-1] * 3;
    }
    for (int i = 0; i <= B; ++i) inv3m[i] = inv_odd(p3m[i]);
    for (int s = 0; s <= B; ++s) {
        segm[s][0] = 0;
        segf[s][0] = 0;
        for (int len = 0; s + len < B; ++len) {
            segm[s][len+1] = (3 * segm[s][len] + (u128(1) << (s + len))) & MASK;
            segf[s][len+1] = 3 * segf[s][len] + (uint256_t(1) << (s + len));
        }
    }

    std::vector<int> zeros;
    for (int k = 0; k <= KMAX; ++k) enumerate(k, 0, zeros);

    std::cout << "prefixes=" << total
              << " survivors_with_at_most_12_evens=" << survivors
              << " latest_13th_even_step=" << latest_13th_even << "\n";

    if (total != 16173662ULL) return 2;
    if (survivors != 0) return 3;
    if (latest_13th_even != 124) return 4;
    return 0;
}
