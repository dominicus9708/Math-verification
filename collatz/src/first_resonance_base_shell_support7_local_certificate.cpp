#include <algorithm>
#include <array>
#include <atomic>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <omp.h>
#include <unordered_set>
#include <vector>

using u128 = unsigned __int128;

static constexpr uint64_t A = 114208327604ULL;
static constexpr uint64_t Q = 72057431991ULL;
static constexpr uint64_t P = A - Q;
static constexpr int GAPLEN = 48;
static constexpr int ODDS = 49;

struct U128Hash {
    size_t operator()(u128 x) const noexcept {
        uint64_t lo = uint64_t(x), hi = uint64_t(x >> 64);
        return std::hash<uint64_t>{}(lo ^ (hi * 0x9e3779b97f4a7c15ULL));
    }
};

static u128 inv_odd_pow2(u128 a, int bits) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    return x & ((((u128)1) << bits) - 1);
}

static std::vector<std::array<int, GAPLEN>> gap_factors() {
    std::vector<uint64_t> bp;
    for (int j = 0; j <= GAPLEN; ++j) {
        uint64_t r = uint64_t(((u128)j * P) % Q);
        bp.push_back(r ? Q - r : 0);
    }
    std::sort(bp.begin(), bp.end());
    bp.erase(std::unique(bp.begin(), bp.end()), bp.end());

    std::vector<std::array<int, GAPLEN>> out;
    for (uint64_t r : bp) {
        std::array<int, GAPLEN> g{};
        uint64_t rr = r;
        for (int j = 0; j < GAPLEN; ++j) {
            int b = rr >= Q - P;
            g[j] = 1 + b;
            rr = b ? rr + P - Q : rr + P;
        }
        if (std::find(out.begin(), out.end(), g) == out.end()) out.push_back(g);
    }
    assert(out.size() == 49);
    return out;
}

int main() {
    const auto fs = gap_factors();
    const u128 B = ((u128)1) << 71;
    const u128 U = (8 * B) / 3;  // broad d=0 shell upper bound: x<2N<8/3*2^71
    const u128 MAX128 = ~(u128)0;
    const u128 MASK73 = (((u128)1) << 73) - 1;

    u128 inv3 = inv_odd_pow2(3, 73), inv3pow[50];
    inv3pow[0] = 1;
    for (int q = 1; q < 50; ++q) inv3pow[q] = (inv3pow[q - 1] * inv3) & MASK73;

    unsigned long long raw_total = 0;
    unsigned long long phase_candidate_total = 0;
    std::atomic<bool> bad(false);
    int global_worst = -1;

    #pragma omp parallel for schedule(dynamic, 1) reduction(+:raw_total, phase_candidate_total)
    for (int pi = 0; pi < (int)fs.size(); ++pi) {
        const auto& g = fs[pi];
        std::unordered_set<u128, U128Hash> candidates;
        candidates.reserve(3'000'000);
        std::array<int, ODDS> d{};
        uint64_t raw = 0;

        auto dfs = [&](auto&& self, int i, int supp, int pos, u128 R73, int q73) -> void {
            if (i == ODDS) {
                if (supp != 7) return;
                ++raw;

                // Exact support-7 paths expose at least 72 time bits.  If the
                // final odd is at time 71, use the exact 2^72 address and lift
                // it into the broad shell; otherwise use the 2^73 address.
                int bits = std::min(73, pos + 1);
                assert(bits >= 72);
                u128 mod = ((u128)1) << bits;
                u128 mask = mod - 1;
                u128 r = (mod - (R73 & mask)) & mask;
                r = (r * (inv3pow[q73] & mask)) & mask;

                for (u128 n = r; n < U; n += mod) {
                    if (n > B) candidates.insert(n);
                }
                return;
            }

            int maxd = d[i - 1] + g[i - 1] - 1;
            for (int nd = 0; nd <= maxd; ++nd) {
                int ns = supp + (nd > 0);
                if (ns > 7) continue;

                int npos = pos + g[i - 1] + d[i - 1] - nd;
                u128 nR = R73;
                int nq = q73;
                if (npos < 73) {
                    nR = (3 * nR + (((u128)1) << npos)) & MASK73;
                    ++nq;
                }
                d[i] = nd;
                self(self, i + 1, ns, npos, nR, nq);
            }
        };

        dfs(dfs, 1, 0, 0, 1, 1);
        raw_total += raw;
        phase_candidate_total += candidates.size();

        int local_worst = -1;
        for (u128 n : candidates) {
            u128 x = n;
            int steps = 0;
            while (x >= B && steps <= 2000) {
                if (x & 1) {
                    if (x > (MAX128 - 1) / 3) { bad.store(true); break; }
                    x = (3 * x + 1) >> 1;
                } else {
                    x >>= 1;
                }
                ++steps;
            }
            if (!(x < B)) { bad.store(true); break; }
            local_worst = std::max(local_worst, steps);
        }

        #pragma omp critical
        global_worst = std::max(global_worst, local_worst);
    }

    assert(!bad.load());
    assert(raw_total == 261'551'336ULL);
    assert(phase_candidate_total == 102'984'111ULL);
    assert(global_worst == 455);

    std::cout << "PASS first-resonance exact support-7 local exclusion\n";
    std::cout << "gap_factors=" << fs.size() << "\n";
    std::cout << "raw_support7_paths=" << raw_total << "\n";
    std::cout << "phase_candidate_total=" << phase_candidate_total << "\n";
    std::cout << "worst_steps_to_below_2^71=" << global_worst << "\n";
}
