#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;

// Exact coefficient-survivor dynamic program with same-depth endpoint Pareto
// pruning. The only pruning rule used is the verified dominance lemma:
//
//   same endpoint y, r1 <= r2, q1 >= q2
//      => state 1 dominates state 2 for every common future continuation
//         when computing the minimal-survivor objective.
//
// No one-state-per-endpoint conjecture is assumed. After generating each
// depth, states are sorted by endpoint and canonical start, and the full Pareto
// frontier in (r,-q) is retained.
//
// For memory efficiency, q is packed into the top 8 bits of rq and r uses the
// lower 56 bits. K<=39 is enforced, so every canonical residue r<2^K fits well
// inside the 56-bit field. The endpoint arithmetic is also safe in uint64_t for
// these depths. K=34 is a practical high-memory reference run.

struct State {
    u64 y = 0;
    u64 rq = 0;
};

static constexpr u64 R_MASK = (1ULL << 56) - 1;

static inline u64 residue(const State& s) {
    return s.rq & R_MASK;
}

static inline unsigned odd_count(const State& s) {
    return static_cast<unsigned>(s.rq >> 56);
}

static inline State make_state(u64 y, u64 r, unsigned q) {
    return State{y, r | (static_cast<u64>(q) << 56)};
}

int main(int argc, char** argv) {
    const int K = (argc >= 2 ? std::stoi(argv[1]) : 34);
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

    std::vector<State> current{make_state(0, 0, 0)};

    std::cout
        << "k,generated,pareto_kept,endpoints_with_multiple_pareto,"
           "max_pareto_per_endpoint,min_residue\n";

    for (int k = 0; k < K; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (const State& n : current) {
            const u64 nr = residue(n);
            const u64 ny = n.y;
            const unsigned nq = odd_count(n);

            for (int b = 0; b <= 1; ++b) {
                const int carry = b ^ static_cast<int>(ny & 1ULL);
                u64 r = nr + (carry ? pow2[k] : 0);
                u64 y = ny + (carry ? pow3[nq] : 0);
                unsigned q = nq;

                if (b == 0) {
                    y >>= 1;
                } else {
                    y = (3 * y + 1) >> 1;
                    ++q;
                }

                if (pow3[q] >= pow2[k + 1]) {
                    next.push_back(make_state(y, r, q));
                }
            }
        }

        const std::size_t generated = next.size();

        std::sort(next.begin(), next.end(), [](const State& a,
                                               const State& b) {
            if (a.y != b.y) return a.y < b.y;
            if (residue(a) != residue(b)) return residue(a) < residue(b);
            return odd_count(a) > odd_count(b);
        });

        std::size_t write = 0;
        std::size_t multi_pareto = 0;
        std::size_t max_pareto = 0;
        u64 min_r = UINT64_MAX;

        for (std::size_t s = 0; s < next.size();) {
            std::size_t e = s + 1;
            while (e < next.size() && next[e].y == next[s].y) ++e;

            int best_q = -1;
            std::size_t kept_here = 0;
            for (std::size_t i = s; i < e; ++i) {
                const int q = static_cast<int>(odd_count(next[i]));
                if (q > best_q) {
                    next[write++] = next[i];
                    best_q = q;
                    ++kept_here;
                    min_r = std::min(min_r, residue(next[i]));
                }
            }

            if (kept_here > 1) ++multi_pareto;
            max_pareto = std::max(max_pareto, kept_here);
            s = e;
        }

        next.resize(write);
        current.swap(next);

        std::cout << (k + 1) << ','
                  << generated << ','
                  << current.size() << ','
                  << multi_pareto << ','
                  << max_pareto << ','
                  << min_r << '\n';
    }
}
