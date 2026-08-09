#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;

// Enumerate coefficient-surviving parity-prefix states and measure the exact
// same-depth endpoint-merge quotient.
//
// At a fixed depth k, if two states have the same endpoint y and
//   r1 <= r2, q1 >= q2,
// then state 1 dominates state 2 for every common future continuation:
// their future orbit from y is identical and state 1 has no smaller total
// odd-count at any future depth.  State 2 may therefore be deleted when the
// objective is the minimal survivor mu(K).
//
// Output columns:
//   k,total_survivors,distinct_endpoints,collision_groups,
//   pareto_kept,max_collision_size

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
    std::cout << "k,total,endpoint_classes,collision_groups,pareto_kept,max_group\n";

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
        std::size_t pareto_kept = 0;
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
                    ++pareto_kept;
                    best_q = qr.first;
                }
            }
        }

        std::cout << (k + 1) << ','
                  << current.size() << ','
                  << groups.size() << ','
                  << collision_groups << ','
                  << pareto_kept << ','
                  << max_group << '\n';
    }
}
