#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>

using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

#ifndef SPARSE_K
#define SPARSE_K 6
#endif
constexpr int B = 73;
constexpr int K = SPARSE_K;
static_assert(K == 6 || K == 7, "compile with -DSPARSE_K=6 or 7");

const u128 MOD = (u128(1) << B);
const u128 MASK = MOD - 1;
u128 p3m[B + 1], inv3m[B + 1], segm[B + 1][B + 1];
u128 P3[45], V33, NMAX;
std::uint64_t total = 0, numeric_range = 0, core = 0;
int shard_lo = 0, shard_hi = B - K;

u128 inv_odd(u128 a) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    return x & MASK;
}

std::string print_u128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + unsigned(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

bool in_current_core(u128 N) {
    if ((N & 3) != 3 || N <= V33 || N > NMAX) return false;
    u128 y = (N - 3) / 4;
    for (int i = 0; i < 44; ++i) {
        unsigned d = unsigned(y % 3);
        if (d > 1) return false;
        y /= 3;
    }
    return y == 1;
}

std::pair<int,int> trajectory_audit(u128 N128) {
    cpp_int N(print_u128(N128));
    cpp_int x = N;
    int first_descent = -1;
    int evens = 0;
    for (int t = 1; t <= 1539; ++t) {
        if ((x & 1) != 0) x = (3 * x + 1) >> 1;
        else { x >>= 1; ++evens; }
        if (first_descent < 0 && x < N) first_descent = t;
    }
    return {first_descent, evens};
}

void evaluate(const std::array<int,K>& z) {
    ++total;
    u128 R = 0;
    int p = 0;
    auto add_ones_run = [&](int start, int len) {
        if (len > 0) R = (p3m[len] * R + segm[start][len]) & MASK;
    };
    for (int j = 0; j < K; ++j) {
        add_ones_run(p, z[j] - p);
        p = z[j] + 1;
    }
    add_ones_run(p, B - p);

    const int q = B - K;
    u128 N = ((u128(0) - R) * inv3m[q]) & MASK;
    if (N > V33 && N <= NMAX) ++numeric_range;
    if (!in_current_core(N)) return;

    ++core;
    auto [tau, evens] = trajectory_audit(N);
    std::cout << "MATCH N=" << print_u128(N)
              << " first_descent=" << tau
              << " evens_1539=" << evens << "\n";
    if (tau < 0) {
        std::cerr << "Core match did not descend within 1539 steps.\n";
        std::exit(3);
    }
}

template<int I>
void enumerate(std::array<int,K>& z, int next) {
    if constexpr (I == K) {
        evaluate(z);
    } else {
        int lo = next;
        int hi = B - (K - I);
        if constexpr (I == 0) {
            lo = std::max(lo, shard_lo);
            hi = std::min(hi, shard_hi);
        }
        for (int p = lo; p <= hi; ++p) {
            z[I] = p;
            enumerate<I + 1>(z, p + 1);
        }
    }
}

int main(int argc, char** argv) {
    if (argc > 1) shard_lo = std::atoi(argv[1]);
    if (argc > 2) shard_hi = std::atoi(argv[2]);

    p3m[0] = 1;
    for (int i = 1; i <= B; ++i) p3m[i] = (p3m[i-1] * 3) & MASK;
    for (int i = 0; i <= B; ++i) inv3m[i] = inv_odd(p3m[i]);
    for (int s = 0; s <= B; ++s) {
        segm[s][0] = 0;
        for (int len = 0; s + len < B; ++len)
            segm[s][len+1] = (3 * segm[s][len] + (u128(1) << (s + len))) & MASK;
    }

    P3[0] = 1;
    for (int i = 1; i <= 44; ++i) P3[i] = P3[i-1] * 3;
    V33 = 4 * (P3[44] + P3[33]) + 2;
    NMAX = 6 * P3[44] + 1;

    std::array<int,K> z{};
    enumerate<0>(z, 0);

    std::cout << "K=" << K
              << " first_zero_range=" << shard_lo << ".." << shard_hi
              << " total=" << total
              << " numeric_range=" << numeric_range
              << " core_matches=" << core << "\n";

    if (K == 6 && shard_lo == 0 && shard_hi >= B-K) {
        if (total != 170230452ULL || core != 1) return 4;
    }
    return 0;
}
