#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

// Exact finite-depth diagnostics for same-depth endpoint mergers in the
// accelerated Collatz map
//
//   T(n) = n/2       (n even)
//          (3n+1)/2  (n odd).
//
// Only coefficient-surviving prefixes are retained:
//   3^q >= 2^k at every prefix depth k.
//
// A pair in the same endpoint class is a NEW merge at depth k iff its two
// time-(k-1) endpoints differ. Once two paths have merged, determinism keeps
// them merged forever, so inherited collisions are excluded from new-merge
// diagnostics.
//
// For each new merge pair the program records:
//   * whether the two states have equal q;
//   * for q_hi > q_lo, whether the exact sufficient endpoint inequality
//       y * 2^(q_lo+1) > 3^(q_lo+1) - 3*2^q_lo
//     fails. This is y > (3/2)*((3/2)^q_lo - 1) without floating point;
//   * whether the correction numerators
//       R = 2^k y - 3^q r
//     violate R_hi > R_lo;
//   * whether the actual canonical starts violate r_hi < r_lo.
//
// Arithmetic is exact for K <= 39. Full flat enumeration is memory-intensive
// well before that limit; K=32 is a practical reference run.

struct State {
    u64 r = 0;
    u64 y = 0;
    u64 parent_y = 0;
    int q = 0;
};

int main(int argc, char** argv) {
    const int K = (argc >= 2 ? std::stoi(argv[1]) : 32);
    if (K < 1 || K > 39) {
        std::cerr << "K must satisfy 1 <= K <= 39\n";
        return 1;
    }

    std::vector<u64> pow2(K + 2), pow3(K + 2);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K + 1; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::vector<State> current{{0, 0, 0, 0}};

    std::cout
        << "k,total_survivors,new_merge_pairs,new_equal_q_pairs,"
           "new_qdiff_pairs,endpoint_bound_fail,remainder_order_fail,"
           "start_order_fail\n";

    for (int k = 0; k < K; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (const State& n : current) {
            for (int b = 0; b <= 1; ++b) {
                State t = n;
                t.parent_y = n.y;

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

                if (pow3[t.q] >= pow2[k + 1]) {
                    next.push_back(t);
                }
            }
        }
        current.swap(next);

        std::sort(current.begin(), current.end(), [](const State& a,
                                                     const State& b) {
            if (a.y != b.y) return a.y < b.y;
            if (a.q != b.q) return a.q < b.q;
            return a.r < b.r;
        });

        std::uint64_t new_pairs = 0;
        std::uint64_t equal_q = 0;
        std::uint64_t qdiff = 0;
        std::uint64_t endpoint_bound_fail = 0;
        std::uint64_t remainder_order_fail = 0;
        std::uint64_t start_order_fail = 0;

        for (std::size_t s = 0; s < current.size();) {
            std::size_t e = s + 1;
            while (e < current.size() && current[e].y == current[s].y) ++e;

            for (std::size_t i = s; i < e; ++i) {
                for (std::size_t j = i + 1; j < e; ++j) {
                    if (current[i].parent_y == current[j].parent_y) continue;
                    ++new_pairs;

                    if (current[i].q == current[j].q) {
                        ++equal_q;
                        continue;
                    }

                    ++qdiff;
                    const State& lo = current[i];  // q-sorted
                    const State& hi = current[j];

                    // Exact sufficient endpoint bound:
                    // y > (3/2)*((3/2)^q_lo - 1).
                    const u128 lhs =
                        static_cast<u128>(lo.y) *
                        static_cast<u128>(pow2[lo.q + 1]);
                    const u128 rhs =
                        static_cast<u128>(pow3[lo.q + 1]) -
                        3 * static_cast<u128>(pow2[lo.q]);
                    if (!(lhs > rhs)) ++endpoint_bound_fail;

                    const u128 common =
                        static_cast<u128>(pow2[k + 1]) * lo.y;
                    const u128 Rlo = common -
                        static_cast<u128>(pow3[lo.q]) * lo.r;
                    const u128 Rhi = common -
                        static_cast<u128>(pow3[hi.q]) * hi.r;

                    if (!(Rhi > Rlo)) ++remainder_order_fail;
                    if (!(hi.r < lo.r)) ++start_order_fail;
                }
            }
            s = e;
        }

        std::cout << (k + 1) << ','
                  << current.size() << ','
                  << new_pairs << ','
                  << equal_q << ','
                  << qdiff << ','
                  << endpoint_bound_fail << ','
                  << remainder_order_fail << ','
                  << start_order_fail << '\n';
    }
}
