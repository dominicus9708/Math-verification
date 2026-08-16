#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>
#include <omp.h>

using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

constexpr int B = 73;
constexpr int K = 8;
const u128 MASK = (u128(1) << B) - 1;
u128 p3m[B+1], inv3m[B+1], segm[B+1][B+1], P3[45], V33, NMAX;

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

std::pair<int,int> trajectory_audit(u128 n) {
    cpp_int N(print_u128(n)), x = N;
    int first_descent = -1, evens = 0;
    for (int t = 1; t <= 1539; ++t) {
        if ((x & 1) != 0) x = (3 * x + 1) >> 1;
        else { x >>= 1; ++evens; }
        if (first_descent < 0 && x < N) first_descent = t;
    }
    return {first_descent, evens};
}

void initialize() {
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
}

inline u128 canonical_start(const int* z) {
    u128 R = 0;
    int p = 0;
    for (int j = 0; j < K; ++j) {
        int len = z[j] - p;
        if (len > 0) R = (p3m[len] * R + segm[p][len]) & MASK;
        p = z[j] + 1;
    }
    int len = B - p;
    if (len > 0) R = (p3m[len] * R + segm[p][len]) & MASK;
    return ((u128(0) - R) * inv3m[B-K]) & MASK;
}

int main(int argc, char** argv) {
    // Current m=44 starts satisfy N == 3 mod 4, hence the first two parity
    // bits are 11.  Therefore an eight-zero first-73 word has first zero >=2.
    const int first_zero_lo = argc > 1 ? std::atoi(argv[1]) : 2;
    const int first_zero_hi = argc > 2 ? std::atoi(argv[2]) : 65;
    initialize();

    unsigned long long total = 0, numeric_range = 0, core_matches = 0;
    int max_first_descent = 0, min_evens_1539 = 9999;

#pragma omp parallel for schedule(dynamic,1) reduction(+:total,numeric_range,core_matches) reduction(max:max_first_descent) reduction(min:min_evens_1539)
    for (int a = first_zero_lo; a <= first_zero_hi; ++a) {
        if (a > B-K) continue;
        unsigned long long local_total = 0, local_range = 0, local_core = 0;
        int local_max_tau = 0, local_min_e = 9999;
        int z[K]; z[0] = a;

        for (int b=a+1; b<=B-7; ++b) { z[1]=b;
        for (int c=b+1; c<=B-6; ++c) { z[2]=c;
        for (int d=c+1; d<=B-5; ++d) { z[3]=d;
        for (int e=d+1; e<=B-4; ++e) { z[4]=e;
        for (int f=e+1; f<=B-3; ++f) { z[5]=f;
        for (int g=f+1; g<=B-2; ++g) { z[6]=g;
        for (int h=g+1; h<B; ++h) { z[7]=h;
            ++local_total;
            u128 N = canonical_start(z);
            if (N > V33 && N <= NMAX) ++local_range;
            if (!in_current_core(N)) continue;

            ++local_core;
            auto [tau, evens] = trajectory_audit(N);
            local_max_tau = std::max(local_max_tau, tau);
            local_min_e = std::min(local_min_e, evens);
#pragma omp critical
            {
                std::cout << "MATCH N=" << print_u128(N)
                          << " first_descent=" << tau
                          << " evens_1539=" << evens << "\n";
            }
            if (tau < 0) {
                std::cerr << "A current-core match did not descend.\n";
                std::abort();
            }
        }}}}}}}}

        total += local_total;
        numeric_range += local_range;
        core_matches += local_core;
        max_first_descent = std::max(max_first_descent, local_max_tau);
        min_evens_1539 = std::min(min_evens_1539, local_min_e);
    }

    std::cout << "K=8 first_zero_range=" << first_zero_lo << ".." << first_zero_hi
              << " total=" << total
              << " numeric_range=" << numeric_range
              << " core_matches=" << core_matches
              << " max_first_descent=" << max_first_descent
              << " min_evens_1539=" << min_evens_1539 << "\n";

    if (first_zero_lo == 2 && first_zero_hi >= 65) {
        if (total != 10639125640ULL) return 2;
        if (numeric_range != 2218549380ULL) return 3;
        if (core_matches != 73ULL) return 4;
        if (max_first_descent != 384) return 5;
        if (min_evens_1539 != 708) return 6;
    }
    return 0;
}
