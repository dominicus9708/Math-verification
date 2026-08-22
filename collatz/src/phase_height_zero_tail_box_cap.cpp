#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <map>
#include <tuple>
#include <vector>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace {

std::vector<int> barrier_table(int nmax) {
    std::vector<int> b(nmax + 1, 0);
    cpp_int p3 = 1;
    cpp_int p2 = 1;
    int q = 0;
    for (int k = 1; k <= nmax; ++k) {
        p2 *= 2;
        while (p3 < p2) {
            p3 *= 3;
            ++q;
        }
        b[k] = q;
    }
    return b;
}

u64 pow3_u64(int a) {
    u64 x = 1;
    for (int i = 0; i < a; ++i) {
        if (x > std::numeric_limits<u64>::max() / 3ULL) {
            std::cerr << "3^a does not fit in uint64_t\n";
            std::exit(2);
        }
        x *= 3ULL;
    }
    return x;
}

struct Result {
    int s = 0;
    int h = 0;
    int a = 0;
    u64 modulus = 0;
    int cap = -1;
    u64 argmax = 0;
};

Result compute_cap(int s, int h, int limit) {
    const auto barrier = barrier_table(s + limit + 2);
    const int a = barrier[s] + h;
    const u64 M = pow3_u64(a);

    int best = -1;
    u64 argbest = 0;

    for (u64 x0 = 1; x0 < M; ++x0) {
        u64 x = x0;
        int q = 0;
        int length = limit;

        for (int j = 1; j <= limit; ++j) {
            if (x & 1ULL) {
                ++q;
                const u128 z = u128(3) * x + 1;
                if (z > std::numeric_limits<u64>::max()) {
                    std::cerr << "trajectory overflow: increase arithmetic width\n";
                    std::exit(3);
                }
                x = static_cast<u64>(z / 2);
            } else {
                x /= 2;
            }

            const int required = barrier[s + j] - barrier[s] - h;
            if (q < required) {
                length = j - 1;
                break;
            }
        }

        if (length > best) {
            best = length;
            argbest = x0;
        }
    }

    return Result{s, h, a, M, best, argbest};
}

void print_result(const Result& r) {
    std::cout << "s=" << r.s
              << " h=" << r.h
              << " a=" << r.a
              << " box=1.." << (r.modulus - 1)
              << " Z=" << r.cap
              << " argmax=" << r.argmax
              << " full_zero_5blocks=" << (r.cap / 5)
              << '\n';
}

} // namespace

int main(int argc, char** argv) {
    if (argc >= 2 && std::string(argv[1]) == "--selfcheck") {
        // Exact values independently calibrated in the current proof branch.
        const std::map<std::pair<int,int>, std::pair<int,u64>> expected{
            {{5,0}, {64,27}},
            {{5,1}, {71,129}},
            {{10,0},{85,1249}},
            {{10,1},{110,2919}},
            {{10,2},{118,9225}},
            {{10,3},{170,37503}},
            {{15,0},{137,35655}},
            {{15,1},{178,142587}},
            {{15,2},{192,142587}},
            {{15,3},{259,1394431}},
            {{15,4},{281,3064033}},
            {{15,5},{374,10507503}},
        };

        for (const auto& [state, want] : expected) {
            const int s = state.first;
            const int h = state.second;
            const Result got = compute_cap(s, h, 1000);
            print_result(got);
            if (got.cap != want.first || got.argmax != want.second) {
                std::cerr << "selfcheck mismatch at s=" << s << " h=" << h << '\n';
                return 4;
            }
        }
        std::cout << "phase-height zero-tail box cap selfcheck: PASS\n";
        return 0;
    }

    if (argc < 3) {
        std::cerr << "usage: phase_height_zero_tail_box_cap s h [limit]\n"
                  << "   or: phase_height_zero_tail_box_cap --selfcheck\n";
        return 1;
    }

    const int s = std::atoi(argv[1]);
    const int h = std::atoi(argv[2]);
    const int limit = argc >= 4 ? std::atoi(argv[3]) : 2000;
    if (s < 0 || h < 0 || limit <= 0) return 1;

    const Result r = compute_cap(s, h, limit);
    print_result(r);
    if (r.cap == limit) {
        std::cerr << "warning: cap reached search limit; rerun with larger limit\n";
        return 5;
    }
    return 0;
}
