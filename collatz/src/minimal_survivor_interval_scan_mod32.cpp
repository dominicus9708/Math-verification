#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using boost::multiprecision::cpp_int;
using u128 = __uint128_t;
using u64 = std::uint64_t;

// Exact interval certificate scanner for
//   mu(K) = min { n >= 1 : tau_c(n) > K }.
//
// For K >= 5 every survivor must satisfy
//   n mod 32 in {7,15,27,31}.
// This is an exact consequence of the first five coefficient-barrier
// inequalities, not a heuristic sieve.  The scanner therefore tests only
// those four residue classes.
//
// The exact barrier threshold a_j = min{q : 3^q >= 2^j} is generated once
// with cpp_int.  Orbit arithmetic is then performed with unsigned __int128;
// this implementation is intended for the current moderate starting ranges.

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "usage: minimal_survivor_interval_scan_mod32 K lo hi\n";
        return 1;
    }

    const int K = std::stoi(argv[1]);
    const u64 lo = std::stoull(argv[2]);
    const u64 hi = std::stoull(argv[3]);
    if (K < 5 || lo >= hi) return 2;

    std::vector<int> threshold(K + 1);
    cpp_int p2 = 1, p3 = 1;
    int q = 0;
    for (int j = 1; j <= K; ++j) {
        p2 *= 2;
        while (p3 < p2) {
            p3 *= 3;
            ++q;
        }
        threshold[j] = q;
    }

    u64 first = (lo / 32) * 32;
    if (first < lo) first += 32;
    const u64 blocks = (hi > first ? (hi - first + 31) / 32 : 0);
    u64 best = UINT64_MAX;
    const int residues[4] = {7,15,27,31};

#pragma omp parallel
    {
        u64 local = UINT64_MAX;
#pragma omp for schedule(dynamic,5000)
        for (u64 bi = 0; bi < blocks; ++bi) {
            const u64 base = first + 32 * bi;
            if (base >= hi) continue;

            for (int rr : residues) {
                const u64 n = base + static_cast<u64>(rr);
                if (n < lo || n >= hi || n >= best) continue;

                u128 x = n;
                int qq = 0;
                bool survives = true;
                for (int j = 1; j <= K; ++j) {
                    if (x & 1) {
                        ++qq;
                        x = (3 * x + 1) >> 1;
                    } else {
                        x >>= 1;
                    }
                    if (qq < threshold[j]) {
                        survives = false;
                        break;
                    }
                }
                if (survives && n < local) local = n;
            }
        }
#pragma omp critical
        {
            if (local < best) best = local;
        }
    }

    if (best == UINT64_MAX) std::cout << "none\n";
    else std::cout << best << '\n';
    return 0;
}
