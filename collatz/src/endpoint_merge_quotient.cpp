#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;

// DIAGNOSTIC ONLY: enumerate coefficient-surviving parity-prefix states and
// measure same-depth endpoint collisions.
//
// IMPORTANT CORRECTION (2026-08-09):
//
// The earlier interpretation of the (r,q) Pareto frontier inside a common
// endpoint y as an exact all-future dominance quotient is false.  Canonical
// descendants may require a lift r -> r + 2^k, which changes the endpoint by
// 3^q.  Hence two states with the same current endpoint but different q can
// acquire different future carry sequences.
//
// Exact counterexample (see endpoint-merge-dominance.md):
//   k=10
//   S1=(r,q,y)=(127,8,820)
//   S2=(383,7,820)
// yet over five more coefficient-surviving steps
//   min descendant(S1)=2175
//   min descendant(S2)=1407.
//
// Therefore the column named candidate_pareto_kept below is only a diagnostic
// statistic for the current collision group.  It MUST NOT be used as a safe
// pruning count for arbitrary future horizons.
//
// Safe finite-horizon quotient:
// for a fixed target K=k+m, two states with the same q and
//   y1 == y2 (mod 2^m)
// have identical lift/carry bits for every common suffix of length m.  Then a
// smaller r safely dominates a larger r for that fixed horizon.  A stronger
// cross-q version additionally requires
//   3^q1 == 3^q2 (mod 2^m), q1>=q2.
// See endpoint-merge-dominance.md and finite_horizon_quotient.py.

struct State {
    cpp_int r = 0;
    cpp_int y = 0;
    int q = 0;
};

static std::string key(const cpp_int& x) {
    return x.convert_to<std::string>();
}

int main(int argc, char** argv) {
    const int K = (argc >= 2 ? std::stoi(argv[1]) : 24);
    if (K < 1) return 1;

    std::vector<cpp_int> pow2(K + 1), pow3(K + 1);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::vector<State> current{{0,0,0}};
    std::cout << "k,total,endpoint_classes,collision_groups,"
                 "candidate_pareto_kept,max_group\n";

    for (int k = 0; k < K; ++k) {
        std::vector<State> next;
        next.reserve(current.size() * 2);

        for (const State& n : current) {
            for (int b = 0; b <= 1; ++b) {
                const int carry = b ^ static_cast<int>((n.y & 1) != 0);
                State t = n;
                if (carry) {
                    t.r += pow2[k];
                    t.y += pow3[n.q];
                }

                if (b == 0) {
                    t.y >>= 1;
                } else {
                    t.y = (3 * t.y + 1) >> 1;
                    ++t.q;
                }

                if (pow3[t.q] >= pow2[k + 1]) next.push_back(std::move(t));
            }
        }
        current.swap(next);

        std::unordered_map<std::string,std::vector<std::pair<int,cpp_int>>> groups;
        groups.reserve(current.size() * 2);
        for (const State& s : current) groups[key(s.y)].push_back({s.q,s.r});

        std::size_t collision_groups = 0;
        std::size_t candidate_pareto_kept = 0;
        std::size_t max_group = 0;

        for (auto& kv : groups) {
            auto& v = kv.second;
            max_group = std::max(max_group, v.size());
            if (v.size() > 1) ++collision_groups;

            std::sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
                return a.second < b.second;
            });

            int best_q = -1;
            for (const auto& qr : v) {
                if (qr.first > best_q) {
                    ++candidate_pareto_kept;
                    best_q = qr.first;
                }
            }
        }

        std::cout << (k + 1) << ','
                  << current.size() << ','
                  << groups.size() << ','
                  << collision_groups << ','
                  << candidate_pareto_kept << ','
                  << max_group << '\n';
    }
}
