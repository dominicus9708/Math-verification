#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

// Exact layer-by-layer coefficient-stopping audit on the recursively sufficient core
//   F_m = { 4(3^m + sum_{i=0}^{m-1} a_i 3^i)+3 : a_i in {0,1} }.
//
// We distinguish
//   L_F(m) = max_{N in F_m} tau_c(N)             (layer maximum)
//   M_F(m) = max_{0<=r<=m} L_F(r)               (cumulative record).
//
// If mask encodes a_0,...,a_{m-1}, the exact ternary recursion is
//   N -> 3N-6  (new a_0=0),
//   N -> 3N-2  (new a_0=1),
// so child_mask = 2*parent_mask + b, b in {0,1}.
//
// This is a finite computational certificate / diagnostic, not a proof of an
// asymptotic bound for L_F or M_F.

int coefficient_stopping(cpp_int x, int max_steps = 10000) {
    cpp_int p2 = 1, p3 = 1;
    for (int j = 1; j <= max_steps; ++j) {
        if ((x & 1) != 0) {
            p3 *= 3;
            x = (3 * x + 1) >> 1;
        } else {
            x >>= 1;
        }
        p2 <<= 1;
        if (p3 < p2) return j;
    }
    return INT_MAX;
}

unsigned long long make_N(int m, uint64_t mask,
                          const vector<unsigned long long>& p3) {
    unsigned long long y = p3[m];
    for (int i = 0; i < m; ++i) {
        if ((mask >> i) & 1ULL) y += p3[i];
    }
    return 4ULL * y + 3ULL;
}

int main(int argc, char** argv) {
    int max_m = 24;
    if (argc >= 2) max_m = stoi(argv[1]);
    if (max_m < 0 || max_m > 27) {
        cerr << "max_m must lie in [0,27] for this exhaustive certificate\n";
        return 2;
    }

    vector<unsigned long long> p3(max_m + 2, 1);
    for (int i = 1; i <= max_m + 1; ++i) p3[i] = 3ULL * p3[i - 1];

    vector<int> prev;
    int cumulative = 0;
    const vector<int> thresholds = {50, 100, 150, 200, 250, 300};

    cout << "LAYER_SUMMARY\n";
    cout << "m,count,L_F,M_F,holders\n";

    for (int m = 0; m <= max_m; ++m) {
        const uint64_t count = 1ULL << m;
        vector<int> cur(count);
        int layer_max = 0;

        for (uint64_t mask = 0; mask < count; ++mask) {
            const auto N = make_N(m, mask, p3);
            cur[mask] = coefficient_stopping(cpp_int(N));
            layer_max = max(layer_max, cur[mask]);
        }

        cumulative = max(cumulative, layer_max);
        vector<uint64_t> holders;
        for (uint64_t mask = 0; mask < count; ++mask)
            if (cur[mask] == layer_max) holders.push_back(mask);

        cout << m << ',' << count << ',' << layer_max << ',' << cumulative
             << ',' << holders.size() << '\n';

        cout << "LAYER_HOLDERS m=" << m << '\n';
        cout << "mask,N,parent_mask,parent_stop,parent_was_prev_layer_max,branch,sibling_stop\n";
        for (uint64_t h : holders) {
            cout << h << ',' << make_N(m, h, p3);
            if (m == 0) {
                cout << ",-,-,-,-,-\n";
            } else {
                const uint64_t pm = h >> 1;
                const int branch = int(h & 1ULL);
                const int parent_stop = prev[pm];
                int prev_max = *max_element(prev.begin(), prev.end());
                const uint64_t sibling = h ^ 1ULL;
                cout << ',' << pm << ',' << parent_stop << ','
                     << (parent_stop == prev_max ? 1 : 0) << ',' << branch << ','
                     << cur[sibling] << '\n';
            }
        }

        if (m > 0) {
            cout << "TAIL_PARENT_AUDIT m=" << m << '\n';
            cout << "threshold,survivors,max_parent_stop,parent_stop_le5,parent_stop_le13\n";
            for (int T : thresholds) {
                uint64_t survivors = 0, le5 = 0, le13 = 0;
                int max_parent_stop = 0;
                for (uint64_t mask = 0; mask < count; ++mask) {
                    if (cur[mask] < T) continue;
                    ++survivors;
                    const int ps = prev[mask >> 1];
                    max_parent_stop = max(max_parent_stop, ps);
                    if (ps <= 5) ++le5;
                    if (ps <= 13) ++le13;
                }
                if (survivors) {
                    cout << T << ',' << survivors << ',' << max_parent_stop << ','
                         << le5 << ',' << le13 << '\n';
                }
            }

            int best_joint = -1, best_parent_stop = 0, best_s0 = 0, best_s1 = 0;
            uint64_t best_parent = 0;
            for (uint64_t pm = 0; pm < prev.size(); ++pm) {
                const int s0 = cur[pm << 1];
                const int s1 = cur[(pm << 1) | 1ULL];
                const int joint = min(s0, s1);
                if (joint > best_joint) {
                    best_joint = joint;
                    best_parent = pm;
                    best_parent_stop = prev[pm];
                    best_s0 = s0;
                    best_s1 = s1;
                }
            }
            cout << "MAX_JOINT_SIBLING m=" << m
                 << " parent_mask=" << best_parent
                 << " parent_stop=" << best_parent_stop
                 << " child0=" << best_s0
                 << " child1=" << best_s1
                 << " joint=" << best_joint << '\n';
        }

        prev.swap(cur);
    }

    return 0;
}
