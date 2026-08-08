#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

// Exact scan of the coefficient stopping time for the accelerated Collatz map
//   T(n)=n/2       (even)
//   T(n)=(3n+1)/2  (odd).
//
// tau_c(n) is the first j >= 1 such that 3^{q_j} < 2^j, where q_j is the
// number of odd terms among the first j iterates.  This program records
//   M(B)=max_{1<=n<2^B} tau_c(n)
// and a record-holder.  boost::multiprecision::cpp_int is used for all orbit
// and coefficient arithmetic; the output is an exact computational result.

int coefficient_stopping(unsigned long long n, int max_steps = 10000) {
    cpp_int x = n;
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
    int maxB = 27;
    if (argc >= 2) maxB = stoi(argv[1]);
    if (maxB < 1 || maxB > 62) {
        cerr << "maxB must lie in [1,62] for the uint64 start-number loop\n";
        return 2;
    }

    int best = 0;
    unsigned long long best_n = 1;

    cout << "B,M(B),record_holder\n";
    for (int B = 1; B <= maxB; ++B) {
        unsigned long long lo = (B == 1 ? 1ULL : (1ULL << (B - 1)));
        unsigned long long hi = (1ULL << B);
        for (unsigned long long n = lo; n < hi; ++n) {
            int s = coefficient_stopping(n);
            if (s != INT_MAX && s > best) {
                best = s;
                best_n = n;
            }
        }
        cout << B << ',' << best << ',' << best_n << '\n';
    }
}
