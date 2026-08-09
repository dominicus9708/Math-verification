#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using boost::multiprecision::cpp_int;

// Exact interval sieve for the predicate tau_c(n)>K.
//
// Usage:
//   g++ -O3 -fopenmp -std=c++17 minimal_survivor_interval_scan.cpp -o scan
//   ./scan LO HI K [threads]
//
// It returns the smallest n in [LO,HI) whose accelerated Collatz orbit has not
// undergone coefficient contraction during the first K steps.  Running
// consecutive disjoint intervals after a known record gives a certificate of
// the next minimal-survivor record once the first nonempty interval is found.

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "usage: minimal_survivor_interval_scan LO HI K [threads]\n";
        return 1;
    }

    const std::uint64_t lo = std::stoull(argv[1]);
    const std::uint64_t hi = std::stoull(argv[2]);
    const int K = std::stoi(argv[3]);
    const int threads = (argc >= 5 ? std::stoi(argv[4]) : 1);

#ifdef _OPENMP
    omp_set_num_threads(threads);
#else
    (void)threads;
#endif

    std::vector<int> min_q(K + 2);
    std::vector<cpp_int> pow2(K + 2), pow3(K + 2);
    pow2[0] = pow3[0] = 1;
    for (int j = 1; j <= K + 1; ++j) {
        pow2[j] = 2 * pow2[j - 1];
        pow3[j] = 3 * pow3[j - 1];
        int a = min_q[j - 1];
        while (pow3[a] < pow2[j]) ++a;
        min_q[j] = a;
    }

    std::uint64_t best = std::numeric_limits<std::uint64_t>::max();

#ifdef _OPENMP
#pragma omp parallel for reduction(min:best) schedule(static)
#endif
    for (std::uint64_t n = (lo | 1ULL); n < hi; n += 2) {
        cpp_int x = n;
        int q = 0;
        bool survives = true;

        for (int j = 1; j <= K; ++j) {
            if ((x & 1) != 0) {
                x = (3 * x + 1) >> 1;
                ++q;
            } else {
                x >>= 1;
            }

            if (q < min_q[j]) {
                survives = false;
                break;
            }
        }

        if (survives && n < best) best = n;
    }

    if (best == std::numeric_limits<std::uint64_t>::max())
        std::cout << "none\n";
    else
        std::cout << "found " << best << '\n';

    return 0;
}
