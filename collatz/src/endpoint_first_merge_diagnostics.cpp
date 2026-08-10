#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

// Exact finite-depth diagnostics for TRUE same-depth endpoint mergers in the
// accelerated Collatz map
//
//   T(n) = n/2       (n even)
//          (3n+1)/2  (n odd).
//
// Only coefficient-surviving prefixes are retained:
//   3^q >= 2^k at every prefix depth k.
//
// IMPORTANT: when a depth-(k-1) canonical state (r,y,q) is lifted by 2^(k-1),
// its actual time-(k-1) value becomes y + 3^q. Therefore the predecessor used
// to decide whether a depth-k collision is a first merge must be the LIFTED
// predecessor
//
//   pre_y = y + carry*3^q,
//
// not the unlifted parent endpoint y. Two depth-k states form a true first
// merge iff they have the same time-k endpoint and distinct lifted pre_y.
// Determinism then guarantees they have not merged at any earlier time.
//
// For every true first-merge pair the program records q-difference and tests
// correction/start ordering. For Delta q = 1 it also records the final parity
// orientation and the exact scaled start/correction gap
//
//   G = r_lo - 3 r_hi = (R_hi-R_lo)/3^q_lo.
//
// Arithmetic is exact for K <= 39. Full flat enumeration is memory-intensive
// well before that limit; K=32 is a practical high-memory reference run.

struct State {
    u64 r = 0;
    u64 y = 0;
    u64 pre_y = 0;   // actual lifted time-(k-1) value before the last map step
    int q = 0;
    int pre_q = 0;
    int last_b = 0;
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

    std::vector<State> current{{0, 0, 0, 0, 0, 0}};

    std::cout
        << "k,total_survivors,true_first_merge_pairs,equal_q_pairs,"
           "qdiff_pairs,d1_pairs,d1_hi_odd_lo_even,d1_hi_even_lo_odd,"
           "endpoint_bound_fail,remainder_order_fail,start_order_fail,"
           "same_last_parity_fail\n";

    for (int k = 0; k < K; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (const State& n : current) {
            for (int b = 0; b <= 1; ++b) {
                const int carry = b ^ static_cast<int>(n.y & 1ULL);

                State t;
                t.r = n.r + (carry ? pow2[k] : 0);
                t.pre_y = n.y + (carry ? pow3[n.q] : 0);
                t.pre_q = n.q;
                t.last_b = b;
                t.q = n.q;

                if (b == 0) {
                    t.y = t.pre_y >> 1;
                } else {
                    t.y = (3 * t.pre_y + 1) >> 1;
                    ++t.q;
                }

                if (pow3[t.q] >= pow2[k + 1]) next.push_back(t);
            }
        }
        current.swap(next);

        std::sort(current.begin(), current.end(), [](const State& a,
                                                     const State& b) {
            if (a.y != b.y) return a.y < b.y;
            if (a.q != b.q) return a.q < b.q;
            return a.r < b.r;
        });

        u64 new_pairs = 0;
        u64 equal_q = 0;
        u64 qdiff = 0;
        u64 d1 = 0;
        u64 d1_hi_odd_lo_even = 0;
        u64 d1_hi_even_lo_odd = 0;
        u64 endpoint_bound_fail = 0;
        u64 remainder_order_fail = 0;
        u64 start_order_fail = 0;
        u64 same_last_parity_fail = 0;

        std::map<int,u64> qdiff_hist;
        std::map<std::int64_t,u64> d1_gap_hist;

        for (std::size_t s = 0; s < current.size();) {
            std::size_t e = s + 1;
            while (e < current.size() && current[e].y == current[s].y) ++e;

            for (std::size_t i = s; i < e; ++i) {
                for (std::size_t j = i + 1; j < e; ++j) {
                    if (current[i].pre_y == current[j].pre_y) continue;
                    ++new_pairs;

                    if (current[i].last_b == current[j].last_b) {
                        // Should be impossible because each parity branch is
                        // injective on its own domain.
                        ++same_last_parity_fail;
                    }

                    if (current[i].q == current[j].q) {
                        ++equal_q;
                        continue;
                    }

                    ++qdiff;
                    const State& lo = current[i]; // q-sorted
                    const State& hi = current[j];
                    const int d = hi.q - lo.q;
                    ++qdiff_hist[d];

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

                    if (d == 1) {
                        ++d1;
                        if (hi.last_b == 1 && lo.last_b == 0)
                            ++d1_hi_odd_lo_even;
                        if (hi.last_b == 0 && lo.last_b == 1)
                            ++d1_hi_even_lo_odd;

                        const std::int64_t G =
                            static_cast<std::int64_t>(lo.r) -
                            3 * static_cast<std::int64_t>(hi.r);
                        ++d1_gap_hist[G];
                    }
                }
            }
            s = e;
        }

        std::cout << (k + 1) << ','
                  << current.size() << ','
                  << new_pairs << ','
                  << equal_q << ','
                  << qdiff << ','
                  << d1 << ','
                  << d1_hi_odd_lo_even << ','
                  << d1_hi_even_lo_odd << ','
                  << endpoint_bound_fail << ','
                  << remainder_order_fail << ','
                  << start_order_fail << ','
                  << same_last_parity_fail << '\n';

        if (!qdiff_hist.empty()) {
            std::cerr << "k=" << (k + 1) << " qdiff_hist";
            for (const auto& kv : qdiff_hist)
                std::cerr << " d" << kv.first << '=' << kv.second;
            std::cerr << '\n';
        }
        if (!d1_gap_hist.empty()) {
            std::cerr << "k=" << (k + 1) << " d1_G_hist";
            for (const auto& kv : d1_gap_hist)
                std::cerr << " G" << kv.first << '=' << kv.second;
            std::cerr << '\n';
        }
    }
}
