#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u128 = __uint128_t;

static inline u128 T(u128 n) {
    return (n & 1) ? (3 * n + 1) / 2 : n / 2;
}

static std::string to_string_u128(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    constexpr int D = 26;
    constexpr int LIMIT = 2000;
    constexpr int EXPECTED_MAX_TAU = 354;
    constexpr std::uint64_t EXPECTED_MASK = 22916555ULL;

    std::vector<u128> p(D);
    p[0] = 1;
    for (int i = 1; i < D; ++i) p[i] = 3 * p[i - 1];

    u128 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;

    const u128 base = 4 * p44 + 3;
    const std::uint64_t total = 1ULL << D;

    int global_max = -1;
    std::uint64_t global_mask = 0;
    u128 global_S = 0;
    u128 global_N = 0;
    std::uint64_t failures = 0;

#pragma omp parallel
    {
        int local_max = -1;
        std::uint64_t local_mask = 0;
        u128 local_S = 0;
        u128 local_N = 0;
        std::uint64_t local_failures = 0;

#pragma omp for schedule(dynamic, 1024)
        for (std::uint64_t mask = 0; mask < total; ++mask) {
            u128 S = 0;
            std::uint64_t bits = mask;
            while (bits) {
                const unsigned i = __builtin_ctzll(bits);
                S += p[i];
                bits &= bits - 1;
            }

            const u128 n = base + 4 * S;
            u128 x = n;
            int tau = 0;

            for (int k = 1; k <= LIMIT; ++k) {
                x = T(x);
                if (x < n) {
                    tau = k;
                    break;
                }
            }

            if (tau == 0) {
                ++local_failures;
                continue;
            }

            if (tau > local_max) {
                local_max = tau;
                local_mask = mask;
                local_S = S;
                local_N = n;
            }
        }

#pragma omp critical
        {
            failures += local_failures;
            if (local_max > global_max) {
                global_max = local_max;
                global_mask = local_mask;
                global_S = local_S;
                global_N = local_N;
            }
        }
    }

    const u128 old_floor = 4 * p44 + 2;
    u128 p26 = 1;
    for (int i = 0; i < 26; ++i) p26 *= 3;
    const u128 new_floor = 4 * (p44 + p26) + 2;

    if (failures != 0 || global_max != EXPECTED_MAX_TAU ||
        global_mask != EXPECTED_MASK) {
        std::cerr << "certificate mismatch\n";
        return 1;
    }

    std::cout << "representatives checked: " << total << "\n";
    std::cout << "failures: " << failures << "\n";
    std::cout << "maximum first-descent depth: " << global_max << "\n";
    std::cout << "record selector mask: " << global_mask << "\n";
    std::cout << "record selector sum S: " << to_string_u128(global_S) << "\n";
    std::cout << "record start N: " << to_string_u128(global_N) << "\n";
    std::cout << "old verified floor: " << to_string_u128(old_floor) << "\n";
    std::cout << "new verified floor: " << to_string_u128(new_floor) << "\n";
    std::cout << "verified-floor increment: "
              << to_string_u128(new_floor - old_floor) << "\n";
}
