#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

// Exact coefficient-stopping records on the ternary 0/1 core
//   x = 4(3^m + sum_{i=0}^{m-1} a_i 3^i) + 3,  a_i in {0,1}.
//
// This is the limiting recursively sufficient set appearing in Ansari's
// recursive-sufficiency construction.  The program reports the largest
// coefficient stopping time encountered through each ternary depth m.

int coefficient_stopping(cpp_int x, int max_steps = 10000) {
    cpp_int p2 = 1, p3 = 1;
    for (int j = 1; j <= max_steps; ++j) {
        if ((x & 1) != 0) {
            p3 *= 3;
            x = (3 * x + 1) >> 1;
        } else {
            x >>= 1;
        }
        p2 *= 2;
        if (p3 < p2) return j;
    }
    return INT_MAX;
}

int main(int argc, char** argv) {
    int max_m = 22;
    if (argc >= 2) max_m = stoi(argv[1]);
    if (max_m < 0 || max_m > 62) {
        cerr << "max_m must lie in [0,62] for the uint64 mask implementation\n";
        return 2;
    }

    vector<unsigned long long> p3(max_m + 1, 1);
    for (int i = 1; i <= max_m; ++i) {
        if (p3[i-1] > numeric_limits<unsigned long long>::max() / 3ULL) {
            cerr << "3^m exceeds uint64 in this implementation\n";
            return 3;
        }
        p3[i] = p3[i-1] * 3ULL;
    }

    int best = 0;
    unsigned long long best_x = 0, best_mask = 0;
    cout << "m,M_F(m),record_holder,digit_mask\n";

    for (int m = 0; m <= max_m; ++m) {
        uint64_t count = (m == 64 ? 0 : (1ULL << m));
        for (uint64_t mask = 0; mask < count; ++mask) {
            unsigned long long y = p3[m];
            uint64_t mm = mask;
            int i = 0;
            while (mm) {
                if (mm & 1ULL) y += p3[i];
                mm >>= 1;
                ++i;
            }
            unsigned long long x = 4ULL * y + 3ULL;
            int s = coefficient_stopping(cpp_int(x));
            if (s != INT_MAX && s > best) {
                best = s;
                best_x = x;
                best_mask = mask;
            }
        }
        cout << m << ',' << best << ',' << best_x << ',' << best_mask << '\n';
    }
}
