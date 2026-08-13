#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = __uint128_t;

static int contraction_budget(int d) {
    if (d <= 0) return -1;
    u128 p3 = 1;
    for (int i = 0; i < d; ++i) p3 *= 3;
    int E = -1;
    while ((u128(1) << (d + E + 1)) < p3) ++E;
    return E;
}

struct State {
    u64 residue;
    std::uint8_t E;
};

static int first_hit(u64 mask, int d, const std::vector<u64>& p3) {
    u64 S = 0, p = 1;
    for (int i = 0; i < d; ++i) {
        if ((mask >> i) & 1ULL) S += p;
        p *= 3;
    }

    const int qmax = d + 2;
    const int Emax = contraction_budget(d);
    const u64 y = 9 * S + 8;

    std::vector<State> states, tmp, next;
    states.reserve(256);
    tmp.reserve(2048);
    next.reserve(256);
    states.push_back({y, 0});

    for (int q = 1; q <= qmax; ++q) {
        const u64 mod = p3[qmax - q];
        tmp.clear();

        for (const State s : states) {
            const int c3 = int(s.residue % 3);
            if (c3 == 0) continue;
            const int parity = (c3 == 2) ? 0 : 1;

            for (int e = parity; e <= Emax - int(s.E); e += 2) {
                const int E = int(s.E) + e;
                const u128 numerator = (u128(1) << (e + 1)) * s.residue - 1;
                u64 r = u64(numerator / 3);
                if (mod > 1) r %= mod;
                else r = 0;
                tmp.push_back({r, std::uint8_t(E)});
            }
        }

        if (tmp.empty()) return -1;
        std::sort(tmp.begin(), tmp.end(), [](const State& a, const State& b) {
            return a.residue < b.residue ||
                   (a.residue == b.residue && a.E < b.E);
        });

        next.clear();
        for (const State s : tmp) {
            if (next.empty() || next.back().residue != s.residue)
                next.push_back(s); // first one has minimal E
        }
        states.swap(next);

        if (q >= 3) {
            int Emin = 127;
            for (const State s : states) Emin = std::min(Emin, int(s.E));
            const int depth = q - 2;
            if (Emin <= contraction_budget(depth)) return depth;
        }
    }
    return -1;
}

int main() {
    constexpr int D = 23;
    const u64 total = u64(1) << D;

    std::vector<u64> p3(D + 3, 1);
    for (int i = 1; i < int(p3.size()); ++i) p3[i] = p3[i - 1] * 3ULL;

    std::vector<unsigned long long> counts(D + 1, 0);

    #pragma omp parallel
    {
        std::vector<unsigned long long> local(D + 1, 0);
        #pragma omp for schedule(dynamic,4096)
        for (u64 mask = 0; mask < total; ++mask) {
            const int hit = first_hit(mask, D, p3);
            if (hit >= 0) ++local[hit];
        }
        #pragma omp critical
        for (int d = 0; d <= D; ++d) counts[d] += local[d];
    }

    const std::vector<std::pair<int,u64>> expected = {
        {7,2}, {9,2}, {11,5}, {12,24}, {14,42},
        {16,104}, {18,224}, {19,802}, {21,1789}, {23,4296}
    };

    u64 killed = 0;
    std::size_t pos = 0;
    for (int d = 1; d <= D; ++d) {
        if (!counts[d]) continue;
        const u64 scale = u64(1) << (D - d);
        if (counts[d] % scale != 0) return 2;
        const u64 minimal = counts[d] / scale;
        if (pos >= expected.size() || expected[pos] != std::make_pair(d, minimal)) return 3;
        ++pos;
        killed += counts[d];
        std::cout << d << " " << minimal << "\n";
    }
    if (pos != expected.size()) return 4;
    if (killed != 299740ULL) return 5;

    // Plateau theorem diagnostic: every new minimal depth after the first
    // examples is a rise of floor(d*log2(3/2)), equivalently of the exact
    // contraction budget.  We check the exact integer budget instead of logs.
    for (const auto& [d, c] : expected) {
        if (d >= 7 && contraction_budget(d) == contraction_budget(d - 1)) return 6;
    }

    std::cout << "killed=" << killed << "/" << total << "\n";
    std::cout << std::setprecision(15)
              << "removed_fraction=" << (long double)killed / total << "\n";
    return 0;
}
