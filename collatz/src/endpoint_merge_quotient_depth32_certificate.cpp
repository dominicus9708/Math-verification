#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

// Exact coefficient-survivor endpoint quotient through depth 32.
//
// This is an optimized finite extension of endpoint_merge_quotient.cpp.  At
// depth <=32 all canonical residues fit uint32_t and all canonical endpoints
// fit uint64_t, so no multiprecision storage is required.
//
// The verified observation is finite: every same-endpoint collision group has
// exactly one Pareto survivor through depth 32.  This does not prove that the
// property holds at all depths and does not prove Collatz.

struct State {
    std::uint64_t y;
    std::uint32_t r;
    std::uint8_t q;
};

struct Expected {
    int k;
    std::uint64_t total;
    std::uint64_t endpoints;
    std::uint64_t collision_groups;
    std::uint64_t pareto;
    std::uint64_t max_group;
};

static constexpr Expected tail_expected[] = {
    {28,  3524586ULL,  3312992ULL,  210107ULL,  3312992ULL, 4ULL},
    {29,  6385637ULL,  6003575ULL,  379327ULL,  6003575ULL, 4ULL},
    {30, 12771274ULL, 12006840ULL,  758572ULL, 12006840ULL, 4ULL},
    {31, 23642078ULL, 22229766ULL, 1401286ULL, 22229766ULL, 4ULL},
    {32, 41347483ULL, 38890504ULL, 2437971ULL, 38890504ULL, 4ULL},
};

int main() {
    constexpr int K = 32;
    std::uint64_t pow2[K + 1]{}, pow3[K + 1]{};
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::vector<State> current{{0, 0, 0}};
    int expected_index = 0;

    for (int k = 0; k < K; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (State n : current) {
            for (int b = 0; b <= 1; ++b) {
                const int carry = b ^ static_cast<int>(n.y & 1ULL);
                State t = n;
                if (carry) {
                    t.r += static_cast<std::uint32_t>(1ULL << k);
                    t.y += pow3[n.q];
                }

                if (b == 0) {
                    t.y >>= 1;
                } else {
                    t.y = (3 * t.y + 1) >> 1;
                    ++t.q;
                }

                if (pow3[t.q] >= pow2[k + 1]) next.push_back(t);
            }
        }
        current.swap(next);

        std::sort(current.begin(), current.end(), [](const State& a, const State& b) {
            if (a.y != b.y) return a.y < b.y;
            if (a.r != b.r) return a.r < b.r;
            return a.q > b.q;
        });

        std::uint64_t endpoints = 0;
        std::uint64_t collision_groups = 0;
        std::uint64_t pareto = 0;
        std::uint64_t max_group = 0;

        for (std::size_t i = 0; i < current.size();) {
            std::size_t j = i + 1;
            while (j < current.size() && current[j].y == current[i].y) ++j;

            ++endpoints;
            const std::uint64_t group_size = static_cast<std::uint64_t>(j - i);
            if (group_size > 1) ++collision_groups;
            max_group = std::max(max_group, group_size);

            int best_q = -1;
            for (std::size_t z = i; z < j; ++z) {
                if (static_cast<int>(current[z].q) > best_q) {
                    ++pareto;
                    best_q = current[z].q;
                }
            }
            i = j;
        }

        const int depth = k + 1;
        if (depth >= 28) {
            const Expected& e = tail_expected[expected_index++];
            assert(e.k == depth);
            assert(e.total == current.size());
            assert(e.endpoints == endpoints);
            assert(e.collision_groups == collision_groups);
            assert(e.pareto == pareto);
            assert(e.max_group == max_group);
            // Finite one-Pareto-per-endpoint observation.
            assert(pareto == endpoints);

            std::cout << depth << ',' << current.size() << ',' << endpoints << ','
                      << collision_groups << ',' << pareto << ',' << max_group << '\n';
        }
    }

    assert(expected_index == 5);
    std::cout << "endpoint quotient through depth 32: PASS\n";
    return 0;
}
