// Independent C++ certificate for the safe m=44 cross-place cylinder sieve.
//
// This is an independent implementation of the Python Q=6, BMAX=18
// certificate, extended to BMAX=20.  It first uses the same exact partition:
//
//   N = 4*3^44 + 3 + 4*sum_{i=0}^{43} a_i 3^i,  a_i in {0,1},
//
// by the low ternary selectors a_0,...,a_5 and N mod 2^(BMAX+1).
// High selector multiplicities are counted by exact cyclic subset-sum DP.
//
// A class is removed only if one of the following is uniform over the whole
// m=44 interval:
//
//   (1) forward descent T^B(N) < N; or
//   (2) a positive reverse ancestor m < N merges to the odd endpoint T^B(N).
//
// The reverse comparison is deliberately written without multiplying a slope
// by the ~72-bit m=44 start.  Such products can exceed signed/unsigned 128-bit
// range when K is large.  Instead strict affine inequalities are decided by
// exact integer division, so no overflow-driven false exclusions are possible.
//
// Regression:
//   BMAX=18 reproduces the existing Python certificate exactly:
//     forward      14,172,856,036,042
//     reverse-only  2,043,061,564,469
//     surviving     1,376,268,443,905
//
// New BMAX=20 certificate:
//     forward      14,270,566,604,094
//     reverse-only  2,117,384,829,533
//     surviving     1,204,234,610,789
//
// Build:
//   g++ -O3 -std=c++17 -fopenmp m44_cross_place_cylinder_sieve_b20_certificate.cpp -o cert
// OpenMP is optional; compile without -fopenmp for a serial run.

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;
using i128 = __int128_t;

static constexpr int Q = 6;
static constexpr int BMAX = 20;
static constexpr int KMAX = 36;
static constexpr u64 TOTAL = u64(1) << 44;

struct ReverseWitness {
    int q;
    int K;
    u64 C;
};

static u64 pow3_u64(int q) {
    u64 x = 1;
    while (q--) x *= 3;
    return x;
}

static u128 pow3_u128(int q) {
    u128 x = 1;
    while (q--) x *= 3;
    return x;
}

static u64 pow3_mod_2L(int e, u64 M) {
    u64 x = 1;
    while (e--) x = (3 * x) & (M - 1);
    return x;
}

static u64 inverse_mod(u64 a, u64 m) {
    std::int64_t t = 0, new_t = 1;
    std::int64_t r = static_cast<std::int64_t>(m);
    std::int64_t new_r = static_cast<std::int64_t>(a % m);

    while (new_r) {
        const std::int64_t q = r / new_r;
        const std::int64_t tt = t - q * new_t;
        t = new_t;
        new_t = tt;
        const std::int64_t rr = r - q * new_r;
        r = new_r;
        new_r = rr;
    }
    assert(r == 1);
    if (t < 0) t += static_cast<std::int64_t>(m);
    return static_cast<u64>(t);
}

static std::vector<ReverseWitness> reverse_frontier(int z) {
    const int MODQ = static_cast<int>(pow3_u64(Q));

    struct State {
        int residue;
        int K;
        u64 C;
    };

    std::vector<State> states{{z % MODQ, 0, 0}};
    std::vector<ReverseWitness> out;

    for (int d = 0; d < Q; ++d) {
        const int mod_next = static_cast<int>(pow3_u64(Q - d - 1));
        std::unordered_map<u64, u64> best;
        best.reserve(states.size() * 8 + 16);

        for (const State& s : states) {
            const int r3 = s.residue % 3;
            if (r3 == 0) continue;

            // Need 2^a * residue == 1 mod 3.
            const int a0 = (r3 == 1) ? 2 : 1;

            for (int a = a0; a <= KMAX - s.K; a += 2) {
                const u64 numerator = (u64(1) << a) * u64(s.residue) - 1;
                assert(numerator % 3 == 0);

                const int K2 = s.K + a;
                const u64 C2 = (u64(1) << a) * s.C + pow3_u64(d);
                const u64 quotient = numerator / 3;
                const int residue = (mod_next > 1)
                    ? static_cast<int>(quotient % u64(mod_next))
                    : 0;

                const u64 key = (u64(residue) << 8) | u64(K2);
                auto it = best.find(key);
                if (it == best.end() || C2 > it->second) best[key] = C2;
            }
        }

        states.clear();
        states.reserve(best.size());
        for (const auto& kv : best) {
            states.push_back({
                static_cast<int>(kv.first >> 8),
                static_cast<int>(kv.first & 255),
                kv.second
            });
        }

        std::vector<u64> by_K(KMAX + 1, 0);
        std::vector<std::uint8_t> have(KMAX + 1, 0);
        for (const State& s : states) {
            if (!have[s.K] || s.C > by_K[s.K]) {
                have[s.K] = 1;
                by_K[s.K] = s.C;
            }
        }

        for (int K = 0; K <= KMAX; ++K)
            if (have[K]) out.push_back({d + 1, K, by_K[K]});
    }

    return out;
}

// Exact test of
//
//   (2^K 3^qf - 2^B 3^qr) N + (2^K Rf - C 2^B) < 0
//
// at the appropriate interval endpoint, plus positivity of the ancestor.
// Products with N are replaced by exact quotient comparisons to avoid u128
// overflow.
static bool reverse_witness(
    const std::vector<ReverseWitness>& frontier,
    int qf,
    u64 Rf,
    int B,
    u128 NMIN,
    u128 NMAX
) {
    const u128 p3qf = pow3_u64(qf);

    for (const ReverseWitness& w : frontier) {
        const u128 coeff = (u128(1) << w.K) * p3qf;
        const u128 denom = (u128(1) << B) * pow3_u64(w.q);
        const u128 positive_const = (u128(1) << w.K) * Rf;
        const u128 negative_const = u128(w.C) << B;

        bool smaller = false;

        if (coeff == denom) {
            smaller = positive_const < negative_const;
        } else if (coeff < denom) {
            const u128 a = denom - coeff;
            // -a*N + positive_const - negative_const < 0,
            // hardest at NMIN.
            if (positive_const <= negative_const) {
                smaller = true;
            } else {
                const u128 c = positive_const - negative_const;
                smaller = a > c / NMIN;
            }
        } else {
            const u128 a = coeff - denom;
            // a*N + positive_const - negative_const < 0,
            // hardest at NMAX.
            if (negative_const > positive_const) {
                const u128 c = negative_const - positive_const;
                smaller = a <= (c - 1) / NMAX;
            }
        }

        if (!smaller) continue;

        // 2^K(3^qf*NMIN+Rf) - C*2^B > 0.
        bool positive = false;
        if (positive_const >= negative_const) {
            positive = true;
        } else {
            const u128 c = negative_const - positive_const;
            positive = coeff > c / NMIN;
        }

        if (positive) return true;
    }

    return false;
}

int main() {
    const int L = BMAX + 1;
    const u64 M = u64(1) << L;
    const int MOD3 = static_cast<int>(pow3_u64(Q));
    const u128 NMIN = 4 * pow3_u128(44) + 3;
    const u128 NMAX = 6 * pow3_u128(44) + 1;

    // All reverse frontiers modulo 3^Q.
    std::vector<std::vector<ReverseWitness>> frontiers(MOD3);
    for (int z = 0; z < MOD3; ++z) frontiers[z] = reverse_frontier(z);

    // High selector group-algebra coefficients for a_Q,...,a_43.
    std::vector<u64> dp(M, 0), next(M, 0);
    dp[0] = 1;
    u64 weight = (4 * pow3_mod_2L(Q, M)) & (M - 1);

    for (int i = Q; i < 44; ++i) {
        if (i > Q) weight = (3 * weight) & (M - 1);
        next = dp;
        for (u64 r = 0; r < M; ++r)
            if (dp[r]) next[(r + weight) & (M - 1)] += dp[r];
        dp.swap(next);
    }

    u128 high_sum = 0;
    std::vector<std::pair<u64, u64>> high_nonzero;
    for (u64 r = 0; r < M; ++r) {
        high_sum += dp[r];
        if (dp[r]) high_nonzero.push_back({r, dp[r]});
    }
    assert(high_sum == (u128(1) << (44 - Q)));

    std::vector<u64> inv2B(BMAX + 1, 0);
    for (int B = 2; B <= BMAX; ++B)
        inv2B[B] = inverse_mod(u64(1) << B, MOD3);

    const u64 fixed2 = (4 * pow3_mod_2L(44, M) + 3) & (M - 1);

    u64 excluded_forward = 0;
    u64 excluded_reverse = 0;
    u64 surviving = 0;

    #ifdef _OPENMP
    #pragma omp parallel for reduction(+:excluded_forward,excluded_reverse,surviving) schedule(dynamic,1)
    #endif
    for (int mask = 0; mask < (1 << Q); ++mask) {
        u64 low2 = 0;
        int low3 = 0;
        u64 p3 = 1;

        for (int i = 0; i < Q; ++i) {
            if ((mask >> i) & 1) {
                low2 = (low2 + 4 * pow3_mod_2L(i, M)) & (M - 1);
                low3 += static_cast<int>(4 * p3);
            }
            p3 *= 3;
        }
        const int n3 = (low3 + 3) % MOD3;

        for (const auto& hc : high_nonzero) {
            const u64 rL = (fixed2 + low2 + hc.first) & (M - 1);
            const u64 multiplicity = hc.second;

            u64 n = rL;
            u64 Rf = 0;
            u64 p3qf = 1;
            int qf = 0;
            bool done = false;

            for (int k = 0; k < BMAX; ++k) {
                if (n & 1ULL) {
                    Rf = 3 * Rf + (u64(1) << k);
                    ++qf;
                    p3qf *= 3;
                    n = (3 * n + 1) / 2;
                } else {
                    n /= 2;
                }

                const int B = k + 1;
                if (B < 2) continue;

                // Exact forward descent, using the appropriate global endpoint
                // of the m=44 interval.  This is conservative for every class.
                const i128 slope = i128(p3qf) - i128(u64(1) << B);
                const u128 test_N = (slope > 0) ? NMAX : NMIN;
                if (slope * i128(test_N) + i128(Rf) < 0) {
                    excluded_forward += multiplicity;
                    done = true;
                    break;
                }

                if (!(n & 1ULL)) continue;

                int z = static_cast<int>(
                    (u128(p3qf % MOD3) * u128(n3) + u128(Rf)) % MOD3
                );
                z = static_cast<int>(u128(z) * inv2B[B] % MOD3);

                if (reverse_witness(frontiers[z], qf, Rf, B, NMIN, NMAX)) {
                    excluded_reverse += multiplicity;
                    done = true;
                    break;
                }
            }

            if (!done) surviving += multiplicity;
        }
    }

    assert(excluded_forward + excluded_reverse + surviving == TOTAL);
    assert(excluded_forward == 14'270'566'604'094ULL);
    assert(excluded_reverse == 2'117'384'829'533ULL);
    assert(surviving == 1'204'234'610'789ULL);

    std::cout << "m44 cross-place cylinder B20: PASS\n";
    std::cout << "forward_excluded " << excluded_forward << '\n';
    std::cout << "reverse_only_excluded " << excluded_reverse << '\n';
    std::cout << "surviving " << surviving << '\n';
}
