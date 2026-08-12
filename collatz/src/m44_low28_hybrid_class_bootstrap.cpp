#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u128 = __uint128_t;

static bool step_exact(u128 &n) {
    if (n & 1) {
        const u128 mx = ~u128(0);
        if (n > (mx - 1) / 3) return false;
        n = (3 * n + 1) / 2;
    } else {
        n /= 2;
    }
    return true;
}

static std::string s128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

struct Affine {
    int q;
    u128 R;
};

static Affine forward_affine(std::uint32_t residue, int B) {
    u128 n = residue;
    u128 R = 0;
    int q = 0;
    for (int k = 0; k < B; ++k) {
        if (n & 1) {
            R = 3 * R + (u128(1) << k);
            ++q;
            n = (3 * n + 1) / 2;
        } else {
            n /= 2;
        }
    }
    return {q, R};
}

int main() {
    constexpr int D = 28;
    constexpr int BMAX = 18;
    constexpr int L = BMAX + 1;
    constexpr int LIMIT = 2000;
    constexpr std::uint64_t EXPECTED_CLASS_SKIP = 237739913ULL;
    constexpr std::uint64_t EXPECTED_TRACKED = 30695543ULL;
    constexpr int EXPECTED_MAX_TAU = 425;
    constexpr std::uint64_t EXPECTED_RECORD_MASK = 140506676ULL;

    const std::uint32_t MOD = 1u << L;

    u128 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;
    const u128 base = 4 * p44 + 3;

    std::vector<u128> p(D);
    p[0] = 1;
    for (int i = 1; i < D; ++i) p[i] = 3 * p[i - 1];

    const u128 pD = 3 * p[D - 1];
    const u128 nmin = base;
    const u128 nmax = base + 2 * (pD - 1);
    (void)nmax;

    // Class proposition layer: one residue modulo 2^(BMAX+1) fixes every
    // forward parity prefix through BMAX.  If one prefix is uniformly
    // descending at the global A_D lower endpoint, the whole residue class
    // is recursive.
    std::vector<unsigned char> killed(MOD, 0);
    for (std::uint32_t rr = 0; rr < MOD; ++rr) {
        for (int B = 2; B <= BMAX; ++B) {
            const std::uint32_t rb = rr & ((1u << (B + 1)) - 1);
            const auto a = forward_affine(rb, B);

            u128 p3 = 1;
            for (int i = 0; i < a.q; ++i) p3 *= 3;

            if (p3 < (u128(1) << B)) {
                const u128 gap = (u128(1) << B) - p3;
                if (a.R < gap * nmin) {
                    killed[rr] = 1;
                    break;
                }
            }
        }
    }

    const std::uint64_t total = 1ULL << D;
    std::uint64_t class_skip = 0;
    std::uint64_t tracked = 0;
    std::uint64_t failures = 0;
    std::uint64_t overflows = 0;
    int global_max = -1;
    std::uint64_t global_mask = 0;
    u128 global_S = 0;
    u128 global_N = 0;

#pragma omp parallel
    {
        std::uint64_t local_skip = 0;
        std::uint64_t local_tracked = 0;
        std::uint64_t local_failures = 0;
        std::uint64_t local_overflows = 0;
        int local_max = -1;
        std::uint64_t local_mask = 0;
        u128 local_S = 0;
        u128 local_N = 0;

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
            const std::uint32_t rr = std::uint32_t(n & (MOD - 1));

            if (killed[rr]) {
                ++local_skip;
                continue;
            }

            ++local_tracked;
            u128 x = n;
            int tau = 0;
            bool overflow = false;

            for (int k = 1; k <= LIMIT; ++k) {
                if (!step_exact(x)) {
                    overflow = true;
                    ++local_overflows;
                    break;
                }
                if (x < n) {
                    tau = k;
                    break;
                }
            }

            if (overflow) continue;
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
            class_skip += local_skip;
            tracked += local_tracked;
            failures += local_failures;
            overflows += local_overflows;
            if (local_max > global_max) {
                global_max = local_max;
                global_mask = local_mask;
                global_S = local_S;
                global_N = local_N;
            }
        }
    }

    if (class_skip != EXPECTED_CLASS_SKIP || tracked != EXPECTED_TRACKED ||
        failures != 0 || overflows != 0 || global_max != EXPECTED_MAX_TAU ||
        global_mask != EXPECTED_RECORD_MASK) {
        std::cerr << "hybrid certificate mismatch\n";
        return 1;
    }

    std::cout << "total representatives: " << total << "\n";
    std::cout << "class-proposition exclusions: " << class_skip << "\n";
    std::cout << "trajectory representatives retained: " << tracked << "\n";
    std::cout << "class excluded fraction: "
              << (long double)class_skip / total << "\n";
    std::cout << "trajectory fraction: "
              << (long double)tracked / total << "\n";
    std::cout << "failures: " << failures << "\n";
    std::cout << "overflow events: " << overflows << "\n";
    std::cout << "maximum first-descent depth among retained starts: "
              << global_max << "\n";
    std::cout << "record mask: " << global_mask << "\n";
    std::cout << "record selector sum S: " << s128(global_S) << "\n";
    std::cout << "record start N: " << s128(global_N) << "\n";
}
