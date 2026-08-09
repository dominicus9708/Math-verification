// Exact finite profiler for coefficient stopping inside Ansari's recursively sufficient core.
//
// Depth m core elements have
//   x = 4*(3^m + sum_{i=0}^{m-1} a_i 3^i) + 3,  a_i in {0,1}.
//
// The program enumerates all 2^m digit choices in Gray-code order and records
// the exact accelerated coefficient stopping time tau_c up to a configurable cap.
// It is a finite diagnostic only, not an asymptotic theorem.

#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using boost::multiprecision::cpp_int;

static int tau_c(cpp_int n, int cap) {
    cpp_int p2 = 1;
    cpp_int p3 = 1;
    for (int k = 1; k <= cap; ++k) {
        if ((n & 1) != 0) {
            n = (3 * n + 1) / 2;
            p3 *= 3;
        } else {
            n /= 2;
        }
        p2 *= 2;
        if (p3 < p2) return k;
    }
    return cap + 1;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: recursive_core_survival_profile M [CAP]\n";
        return 2;
    }
    const int m = std::atoi(argv[1]);
    const int cap = (argc >= 3) ? std::atoi(argv[2]) : 800;
    if (m < 0 || m >= 63) {
        std::cerr << "this reference enumerator requires 0 <= M < 63\n";
        return 2;
    }

    const uint64_t total = 1ULL << m;
    std::vector<cpp_int> pow3(m + 1);
    pow3[0] = 1;
    for (int i = 1; i <= m; ++i) pow3[i] = 3 * pow3[i - 1];

    cpp_int y = pow3[m];
    uint64_t previous_gray = 0;
    const int thresholds[] = {50, 100, 200, 400, 800};
    uint64_t counts[5] = {0, 0, 0, 0, 0};
    int record = 0;
    uint64_t record_mask = 0;

    for (uint64_t index = 0; index < total; ++index) {
        const uint64_t gray = index ^ (index >> 1);
        if (index != 0) {
            const uint64_t diff = gray ^ previous_gray;
            const int bit = __builtin_ctzll(diff);
            if ((gray & diff) != 0) y += pow3[bit];
            else y -= pow3[bit];
        }
        previous_gray = gray;

        const cpp_int x = 4 * y + 3;
        const int tau = tau_c(x, cap);
        if (tau > record) {
            record = tau;
            record_mask = gray;
        }
        for (int j = 0; j < 5; ++j) {
            if (tau > thresholds[j]) ++counts[j];
        }
    }

    std::cout << "m=" << m
              << " total=" << total
              << " max_tau=" << record
              << " record_mask=" << record_mask;
    for (int j = 0; j < 5; ++j) {
        std::cout << " gt" << thresholds[j] << "=" << counts[j];
    }
    std::cout << "\n";
    return 0;
}
