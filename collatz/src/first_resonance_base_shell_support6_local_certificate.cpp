#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>

using u128 = unsigned __int128;

static constexpr uint64_t A = 114208327604ULL;
static constexpr uint64_t Q = 72057431991ULL;
static constexpr uint64_t P = A - Q;
static constexpr int GAPLEN = 48;
static constexpr int ODDS = 49;
static constexpr int K = 73;
static constexpr int MAXSUP = 6;

struct U128Hash {
    size_t operator()(u128 x) const noexcept {
        uint64_t lo = uint64_t(x), hi = uint64_t(x >> 64);
        return std::hash<uint64_t>{}(lo ^ (hi * 0x9e3779b97f4a7c15ULL));
    }
};

static inline u128 mask73() { return (((u128)1) << 73) - 1; }
static u128 inv_odd_pow2(u128 a) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    return x & mask73();
}
static std::string u128s(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
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
        bool dup = false;
        for (const auto& x : out) if (x == g) { dup = true; break; }
        if (!dup) out.push_back(g);
    }
    assert(out.size() == 49);
    return out;
}

int main() {
    const auto fs = gap_factors();
    const u128 MOD = ((u128)1) << 73;
    const u128 MASK = MOD - 1;
    const u128 B = ((u128)1) << 71;
    const u128 MAX128 = ~(u128)0;

    u128 inv3 = inv_odd_pow2(3), inv3pow[74];
    inv3pow[0] = 1;
    for (int q = 1; q < 74; ++q) inv3pow[q] = (inv3pow[q - 1] * inv3) & MASK;

    std::unordered_set<u128, U128Hash> candidates;
    candidates.reserve(20'000'000);
    uint64_t raw = 0;
    std::array<int, ODDS> d{};

    for (const auto& g : fs) {
        d.fill(0);
        auto dfs = [&](auto&& self, int i, int supp, int pos, u128 R, int q) -> void {
            if (i == ODDS) {
                ++raw;
                assert(pos >= 72); // all first 73 time-parity bits are exposed
                u128 r = ((MOD - R) & MASK);
                r = (r * inv3pow[q]) & MASK;
                if (r > B && 3 * r < 8 * B) candidates.insert(r);
                return;
            }

            int maxd = d[i - 1] + g[i - 1] - 1;
            for (int nd = 0; nd <= maxd; ++nd) {
                int ns = supp + (nd > 0);
                if (ns > MAXSUP) continue;

                int npos = pos + g[i - 1] + d[i - 1] - nd;
                u128 nR = R;
                int nq = q;
                if (npos < K) {
                    nR = (3 * nR + (((u128)1) << npos)) & MASK;
                    ++nq;
                }
                d[i] = nd;
                self(self, i + 1, ns, npos, nR, nq);
            }
        };
        dfs(dfs, 1, 0, 0, 1, 1);
    }

    assert(raw == 65'754'189ULL);
    assert(candidates.size() == 16'610'043ULL);

    int worst = -1;
    u128 arg = 0;
    for (u128 n : candidates) {
        u128 x = n;
        int s = 0;
        while (x >= B && s <= 2000) {
            if (x & 1) {
                assert(x <= (MAX128 - 1) / 3); // exact no-overflow audit
                x = (3 * x + 1) >> 1;
            } else {
                x >>= 1;
            }
            ++s;
        }
        assert(x < B);
        if (s > worst) { worst = s; arg = n; }
    }

    assert(worst == 387);
    assert(uint64_t(arg >> 64) == 339ULL);
    assert(uint64_t(arg) == 10927217162583338091ULL);

    std::cout << "PASS first-resonance base-shell support<=6 local exclusion\n";
    std::cout << "gap_factors=" << fs.size() << "\n";
    std::cout << "raw_paths=" << raw << "\n";
    std::cout << "canonical_shell_candidates=" << candidates.size() << "\n";
    std::cout << "worst_steps_to_below_2^71=" << worst << "\n";
    std::cout << "worst_start=" << u128s(arg) << "\n";
}
