#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

// Exact interval certificate scanner for
//   mu(K) = min { n >= 1 : tau_c(n) > K }
// using a coefficient-surviving prefix-channel decomposition.
//
// At prefix depth B, each surviving canonical residue r has state (r,q,y).
// Every integer in that residue cylinder can be written
//
//   n = r + m*2^B,
//
// and the first B accelerated Collatz steps satisfy exactly
//
//   T^B(n) = y + 3^q*m.
//
// Therefore the scanner enumerates only B-depth survivor cylinders and starts
// orbit testing at depth B+1. This is an exact strengthening of a shallow
// residue prefilter such as the mod-32 filter.
//
// Thresholds a_j = min{q : 3^q >= 2^j} are generated with cpp_int. Orbit
// arithmetic after the channel lift uses unsigned __int128 and explicitly
// checks every odd-step multiplication for overflow. If any overflow is
// detected, the run exits nonzero and must not be used as a certificate.

struct Channel {
    u64 r = 0;
    u64 y = 0;
    u64 pow3q = 1;
    int q = 0;
};

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr <<
            "usage: prefix_channel_interval_scan K lo hi [B]\n";
        return 1;
    }

    const int K = std::stoi(argv[1]);
    const u64 lo = std::stoull(argv[2]);
    const u64 hi = std::stoull(argv[3]);
    const int B = (argc >= 5 ? std::stoi(argv[4]) : 24);

    if (K < B || B < 5 || B > 32 || lo >= hi) return 2;

    std::vector<int> threshold(K + 1);
    cpp_int exact_pow2 = 1;
    cpp_int exact_pow3 = 1;
    int tq = 0;
    for (int j = 1; j <= K; ++j) {
        exact_pow2 *= 2;
        while (exact_pow3 < exact_pow2) {
            exact_pow3 *= 3;
            ++tq;
        }
        threshold[j] = tq;
    }

    std::vector<u64> pow2(B + 1), pow3(B + 1);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= B; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    struct State {
        u64 r = 0;
        u64 y = 0;
        int q = 0;
    };

    std::vector<State> current{{0, 0, 0}};
    for (int k = 0; k < B; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (const State& n : current) {
            for (int b = 0; b <= 1; ++b) {
                State t = n;
                const int carry = b ^ static_cast<int>(n.y & 1ULL);
                if (carry) {
                    t.r += pow2[k];
                    t.y += pow3[t.q];
                }

                if (b == 0) {
                    t.y >>= 1;
                } else {
                    t.y = (3 * t.y + 1) >> 1;
                    ++t.q;
                }

                if (t.q >= threshold[k + 1]) next.push_back(t);
            }
        }
        current.swap(next);
    }

    std::vector<Channel> channels;
    channels.reserve(current.size());
    for (const State& s : current) {
        channels.push_back(Channel{s.r, s.y, pow3[s.q], s.q});
    }

    const u64 modulus = (1ULL << B);
    const u128 UMAX = ~static_cast<u128>(0);

    u64 best = UINT64_MAX;
    unsigned long long tested = 0;
    unsigned long long overflows = 0;

#pragma omp parallel
    {
        u64 local_best = UINT64_MAX;
        unsigned long long local_tested = 0;
        unsigned long long local_overflows = 0;

#pragma omp for schedule(dynamic, 16)
        for (std::size_t ci = 0; ci < channels.size(); ++ci) {
            const Channel c = channels[ci];

            u64 m0 = 0;
            if (lo > c.r) m0 = (lo - c.r + modulus - 1) / modulus;
            if (hi - 1 < c.r) continue;
            const u64 m1 = (hi - 1 - c.r) / modulus;
            if (m0 > m1) continue;

            for (u64 m = m0; m <= m1; ++m) {
                const u64 n = c.r + m * modulus;
                ++local_tested;

                const u128 product = static_cast<u128>(c.pow3q) * m;
                if (product > UMAX - c.y) {
                    ++local_overflows;
                    continue;
                }

                u128 x = product + c.y;
                int q = c.q;
                bool survives = true;

                for (int j = B + 1; j <= K; ++j) {
                    if (x & 1) {
                        ++q;
                        if (x > (UMAX - 1) / 3) {
                            ++local_overflows;
                            survives = false;
                            break;
                        }
                        x = (3 * x + 1) >> 1;
                    } else {
                        x >>= 1;
                    }

                    if (q < threshold[j]) {
                        survives = false;
                        break;
                    }
                }

                if (survives && n < local_best) local_best = n;
                if (m == UINT64_MAX) break;
            }
        }

#pragma omp critical
        {
            tested += local_tested;
            overflows += local_overflows;
            if (local_best < best) best = local_best;
        }
    }

    std::cerr << "B=" << B
              << ",channels=" << channels.size()
              << ",tested=" << tested
              << ",overflows=" << overflows << '\n';

    if (overflows != 0) {
        std::cerr << "overflow detected; certificate invalid\n";
        return 5;
    }

    if (best == UINT64_MAX) std::cout << "none\n";
    else std::cout << best << '\n';
    return 0;
}
