#include <array>
#include <cassert>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

// Exact finite certificate for the adaptive reverse-potential edge-rarity audit.
// Scope: diagnostic / structural certificate only, not a Collatz proof.
//
// A reverse odd-to-odd code with q inverse odd events and total binary exponent K
// has coefficient potential Lambda = 3^q / 2^K, with K>=q.
// For each ternary resolution Q<=14 this rebuilds the exact compressed DP and
// counts endpoint residues z mod 3^Q whose best Lambda exceeds 3^d.
//
// KMAX=24 is exact for every reported strict threshold Lambda>1: for q<=14,
// any K>=23 has Lambda <= 3^14/2^23 < 1, so no omitted larger-K code can
// contribute to any count below.

struct State {
    uint8_t q = 0;
    uint8_t K = 0;
};

static bool valid(const State& s) { return s.q != 0; }

static uint64_t pow3i(int n) {
    uint64_t x = 1;
    for (int i=0;i<n;++i) x *= 3;
    return x;
}

static bool better(const State& a, const State& b) {
    if (!valid(a)) return false;
    if (!valid(b)) return true;
    const uint64_t lhs = pow3i(a.q) * (uint64_t(1) << b.K);
    const uint64_t rhs = pow3i(b.q) * (uint64_t(1) << a.K);
    if (lhs != rhs) return lhs > rhs;
    return a.K < b.K;
}

static bool lambda_gt_3d(const State& s, int d) {
    if (!valid(s) || int(s.q) <= d) return false;
    return pow3i(int(s.q) - d) > (uint64_t(1) << s.K);
}

static int qstar(int d) {
    // least Q>=1 with (3/2)^Q > 3^d, exact arithmetic
    for (int Q=1;;++Q) {
        if (pow3i(Q) > pow3i(d) * (uint64_t(1) << Q)) return Q;
    }
}

int main() {
    constexpr int QMAX = 14;
    constexpr int KMAX = 24;
    constexpr int STRIDE = KMAX + 1;

    static_assert((uint64_t(1) << 23) > 4782969ULL, "3^14 < 2^23");

    const std::array<std::array<uint64_t,6>,QMAX> expected = {{
        {{1,0,0,0,0,0}},
        {{4,0,0,0,0,0}},
        {{12,1,0,0,0,0}},
        {{37,3,0,0,0,0}},
        {{111,12,0,0,0,0}},
        {{335,36,1,0,0,0}},
        {{1013,117,3,0,0,0}},
        {{3039,386,15,0,0,0}},
        {{9145,1158,72,1,0,0}},
        {{27435,3603,216,12,0,0}},
        {{82429,10809,756,36,1,0}},
        {{247889,33018,2268,153,3,0}},
        {{743667,102004,7336,459,20,0}},
        {{2233499,306012,24801,1631,60,1}}
    }};

    uint64_t prev_m = 1;
    std::vector<State> prev(prev_m * STRIDE);

    std::cout << "Q total admissible gt1 gt3 gt9 gt27 gt81 gt243 edge_d edge_count edge_fraction_adm\n";

    for (int depth=1; depth<=QMAX; ++depth) {
        const uint64_t mod = prev_m * 3;
        std::vector<State> cur(mod * STRIDE);

        for (uint64_t z=0; z<mod; ++z) {
            const int r3 = int(z % 3);
            if (r3 == 0) continue;
            const int a0 = (r3 == 1) ? 2 : 1;

            for (int budget=1; budget<=KMAX; ++budget) {
                State best{};
                for (int a=a0; a<=budget; a+=2) {
                    const uint64_t numerator = (uint64_t(1) << a) * z - 1;
                    assert(numerator % 3 == 0);
                    const uint64_t zp = (prev_m > 1) ? ((numerator / 3) % prev_m) : 0;
                    const State& suffix = prev[zp * STRIDE + (budget - a)];

                    State cand{};
                    if (valid(suffix) && lambda_gt_3d(suffix, 0)) {
                        cand.q = uint8_t(suffix.q + 1);
                        cand.K = uint8_t(suffix.K + a);
                    } else {
                        cand.q = 1;
                        cand.K = uint8_t(a);
                    }
                    if (better(cand, best)) best = cand;
                }
                cur[z * STRIDE + budget] = best;
            }
        }

        uint64_t admissible = 0;
        std::array<uint64_t,6> cnt{};
        for (uint64_t z=0; z<mod; ++z) {
            const State& e = cur[z * STRIDE + KMAX];
            if (!valid(e)) continue;
            ++admissible;
            for (int d=0; d<=5; ++d) {
                if (lambda_gt_3d(e,d)) ++cnt[d];
            }
        }

        assert(admissible == 2 * (mod/3));
        assert(cnt == expected[depth-1]);

        int edge_d = -1;
        for (int d=0; d<=5; ++d) {
            if (pow3i(depth) > pow3i(d) * (uint64_t(1) << depth)) edge_d = d;
        }
        uint64_t edge_count = edge_d >= 0 ? cnt[edge_d] : 0;

        for (int d=0; d<=5; ++d) {
            if (depth == qstar(d)) {
                assert(cnt[d] == 1);
                const uint64_t z = mod - 1;
                const State& e = cur[z * STRIDE + KMAX];
                assert(e.q == depth && e.K == depth);
                assert(lambda_gt_3d(e,d));
            }
        }

        std::cout << depth << ' ' << mod << ' ' << admissible;
        for (int d=0; d<=5; ++d) std::cout << ' ' << cnt[d];
        std::cout << ' ' << edge_d << ' ' << edge_count << ' '
                  << std::setprecision(12)
                  << (edge_d >= 0 ? double(edge_count)/double(admissible) : 0.0)
                  << '\n';

        prev.swap(cur);
        prev_m = mod;
    }

    assert(qstar(1)==3);
    assert(qstar(2)==6);
    assert(qstar(3)==9);
    assert(qstar(4)==11);
    assert(qstar(5)==14);

    std::cout << "PASS\n";
}
