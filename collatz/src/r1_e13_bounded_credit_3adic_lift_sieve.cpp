#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <unordered_set>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

// Labeled low-3-adic lift sieve for E=13 pre-G13 same-q relations.
//
// For one E=13 path,
//
//   C(P)=sum_{j=0}^{12} 2^{p_j} 3^{1526-p_j+j}.
//
// A same-q relation with right-boundary credit delta requires
//
//   C(P')-C(P) == -2^1539 delta (mod 3^1526).
//
// For K<=36, exact run-cap upper bounds show ranks j=0..4 occur too early to
// affect C modulo 3^K.  Hence every low-K correction residue is contained in
// the terminal suffix over-family j0..12, j0>=5, parametrized by
//
//   p_j = 1526 + j - (K-1) + b_j,
//   0 <= b_j <= K-1,
//   b_j nondecreasing.
//
// The program builds the complete S_18 and labels every pair by
// delta=1..397.  For K>18 it does NOT rebuild the whole S_K.  It enumerates
// only residues whose projection modulo 3^(K-1) is an endpoint of a surviving
// labeled pair.  Since every S_K residue projects into S_(K-1), this targeted
// Hensel lift is exhaustive for the surviving labeled relation set.
//
// Exact certified table:
//
// K   pair states   globally surviving credits
// 18     966886          397
// 19     661555          397
// 20     437981          397
// 21     283335          397
// 22     170431          394
// 23     107481          386
// 24      75158          376
// 25      56514          362
// 26      44801          330
// 27      39906          288
// 28      38554          258
// 29      38420          248
// 30      38526          247
// 31      38663          247
// 32      38811          247
// 33      38960          247
// 34      39111          247
// 35      39262          247
// 36      39413          247
//
// Thus 150 of the 397 bounded credits are globally impossible by K=30, but
// the remaining credit count plateaus at 247 through K=36 while the number of
// lifted pair states slowly grows.  This is an exact negative result for the
// naive strategy "keep increasing K until every bounded credit disappears".
// Deeper/middle-event structure or the G13-side relation constraints must be
// intersected with this quotient.
//
// This is a finite same-q relation sieve, not a proof of Collatz.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr int T = 1539;
constexpr int Q = 1526;
constexpr int MAX_CREDIT = 397;

struct Hash64 {
    std::size_t operator()(u64 x) const noexcept {
        x ^= x >> 30;
        x *= 0xbf58476d1ce4e5b9ULL;
        x ^= x >> 27;
        x *= 0x94d049bb133111ebULL;
        x ^= x >> 31;
        return static_cast<std::size_t>(x);
    }
};

struct PairState {
    u64 actual;
    std::uint16_t credit;
};

u64 mod_pow(u64 a, u64 e, u64 m) {
    u64 r = 1 % m;
    while (e) {
        if (e & 1) r = static_cast<u64>((u128)r * a % m);
        a = static_cast<u64>((u128)a * a % m);
        e >>= 1;
    }
    return r;
}

u64 pow3(int k) {
    u64 x = 1;
    for (int i = 0; i < k; ++i) x *= 3;
    return x;
}

std::vector<std::vector<u64>> terminal_terms(int K, u64 modulus) {
    std::vector<std::vector<u64>> term(13, std::vector<u64>(K, 0));
    for (int j = 5; j < 13; ++j) {
        for (int b = 0; b < K; ++b) {
            const int p = Q + j - (K - 1) + b;
            const int e3 = Q - p + j;
            assert(e3 == K - 1 - b);
            assert(0 <= e3 && e3 < K);
            assert(0 <= p && p < T);

            u64 v = mod_pow(2, static_cast<u64>(p), modulus);
            for (int z = 0; z < e3; ++z) {
                v = static_cast<u64>((u128)v * 3 % modulus);
            }
            term[j][b] = v;
        }
    }
    return term;
}

std::vector<u64> complete_S18(std::vector<u64>& bits) {
    constexpr int K = 18;
    const u64 modulus = pow3(K);
    bits.assign((modulus + 63) / 64, 0);
    std::vector<u64> residues;
    residues.reserve(1'100'000);

    auto has = [&](u64 x) -> bool {
        return (bits[x >> 6] >> (x & 63)) & 1ULL;
    };
    auto add = [&](u64 x) {
        x %= modulus;
        if (!has(x)) {
            bits[x >> 6] |= 1ULL << (x & 63);
            residues.push_back(x);
        }
    };

    const auto term = terminal_terms(K, modulus);
    add(0);

    std::function<void(int, int, u64)> rec = [&](int j, int last_b, u64 acc) {
        if (j == 13) {
            add(acc);
            return;
        }
        for (int b = last_b; b < K; ++b) {
            rec(j + 1, b, (acc + term[j][b]) % modulus);
        }
    };
    for (int j0 = 5; j0 < 13; ++j0) rec(j0, 0, 0);

    assert(residues.size() == 997'755ULL);
    return residues;
}

std::vector<PairState> initial_pairs_18(
    const std::vector<u64>& residues,
    const std::vector<u64>& bits
) {
    const u64 modulus = pow3(18);
    const u64 shift = mod_pow(2, T, modulus);

    auto has = [&](u64 x) -> bool {
        return (bits[x >> 6] >> (x & 63)) & 1ULL;
    };

    int threads = 1;
#ifdef _OPENMP
    threads = omp_get_max_threads();
#endif
    std::vector<std::vector<PairState>> local(static_cast<std::size_t>(threads));

#ifdef _OPENMP
#pragma omp parallel
    {
        const int tid = omp_get_thread_num();
        auto& out = local[static_cast<std::size_t>(tid)];
        out.reserve(residues.size() / static_cast<std::size_t>(threads) * 2 + 1000);
#pragma omp for schedule(static)
        for (long long ii = 0; ii < static_cast<long long>(residues.size()); ++ii) {
            const u64 c = residues[static_cast<std::size_t>(ii)];
            for (int d = 1; d <= MAX_CREDIT; ++d) {
                const u64 s = static_cast<u64>((u128)shift * d % modulus);
                const u64 alt = (c + modulus - s) % modulus;
                if (has(alt)) out.push_back({c, static_cast<std::uint16_t>(d)});
            }
        }
    }
#else
    auto& out = local[0];
    for (u64 c : residues) {
        for (int d = 1; d <= MAX_CREDIT; ++d) {
            const u64 s = static_cast<u64>((u128)shift * d % modulus);
            const u64 alt = (c + modulus - s) % modulus;
            if (has(alt)) out.push_back({c, static_cast<std::uint16_t>(d)});
        }
    }
#endif

    std::size_t total = 0;
    for (const auto& v : local) total += v.size();
    std::vector<PairState> pairs;
    pairs.reserve(total);
    for (auto& v : local) pairs.insert(pairs.end(), v.begin(), v.end());

    assert(pairs.size() == 966'886ULL);
    return pairs;
}

std::vector<u64> targeted_residues(
    int K,
    u64 modulus,
    u64 previous_modulus,
    const std::unordered_set<u64, Hash64>& projections
) {
    const auto term = terminal_terms(K, modulus);
    std::vector<u64> found;
    found.reserve(projections.size() * 3 + 100);

    auto maybe_add = [&](u64 r) {
        if (projections.find(r % previous_modulus) != projections.end()) {
            found.push_back(r);
        }
    };

    maybe_add(0);
    std::function<void(int, int, u64)> rec = [&](int j, int last_b, u64 acc) {
        if (j == 13) {
            maybe_add(acc);
            return;
        }
        for (int b = last_b; b < K; ++b) {
            rec(j + 1, b, (acc + term[j][b]) % modulus);
        }
    };
    for (int j0 = 5; j0 < 13; ++j0) rec(j0, 0, 0);

    std::sort(found.begin(), found.end());
    found.erase(std::unique(found.begin(), found.end()), found.end());
    return found;
}

int credit_count(const std::vector<PairState>& pairs) {
    std::array<char, MAX_CREDIT + 1> seen{};
    for (const auto& p : pairs) seen[p.credit] = 1;
    int count = 0;
    for (int d = 1; d <= MAX_CREDIT; ++d) count += seen[d];
    return count;
}

}  // namespace

int main(int argc, char** argv) {
    int maxK = 36;
    if (argc > 1) maxK = std::atoi(argv[1]);
    if (maxK < 18 || maxK > 36) {
        std::cerr << "maxK must lie in 18..36 for the certified table.\n";
        return 2;
    }

    // Exact early-rank upper bounds inherited from the run-cover theorem.
    // At K=36 the activation thresholds for ranks 0..4 are
    // 1491,1492,1493,1494,1495, all above the certified maxima below.
    const int early_max[5] = {72, 186, 365, 647, 1093};
    for (int j = 0; j < 5; ++j) {
        const int threshold = Q + j - (36 - 1);
        assert(early_max[j] < threshold);
    }

    const std::array<std::size_t, 19> expected_pairs{
        966886, 661555, 437981, 283335, 170431, 107481, 75158,
        56514, 44801, 39906, 38554, 38420, 38526, 38663, 38811,
        38960, 39111, 39262, 39413
    };
    const std::array<int, 19> expected_credits{
        397, 397, 397, 397, 394, 386, 376,
        362, 330, 288, 258, 248, 247, 247, 247,
        247, 247, 247, 247
    };

    std::vector<u64> bits18;
    const auto S18 = complete_S18(bits18);
    std::vector<PairState> pairs = initial_pairs_18(S18, bits18);

    assert(pairs.size() == expected_pairs[0]);
    assert(credit_count(pairs) == expected_credits[0]);
    std::cout << "K=18 pairs=" << pairs.size()
              << " credits=" << credit_count(pairs) << "\n";

    u64 modulus = pow3(18);

    for (int K = 19; K <= maxK; ++K) {
        const u64 previous_modulus = modulus;
        modulus *= 3;

        const u64 previous_shift = mod_pow(2, T, previous_modulus);
        std::unordered_set<u64, Hash64> projections;
        projections.reserve(pairs.size() * 3 + 100);

        for (const PairState& p : pairs) {
            projections.insert(p.actual);
            const u64 s = static_cast<u64>(
                (u128)previous_shift * p.credit % previous_modulus);
            projections.insert((p.actual + previous_modulus - s) % previous_modulus);
        }

        const auto found = targeted_residues(
            K, modulus, previous_modulus, projections);
        std::unordered_set<u64, Hash64> membership;
        membership.reserve(found.size() * 2 + 100);
        for (u64 r : found) membership.insert(r);

        const u64 shift = mod_pow(2, T, modulus);
        std::vector<PairState> next;
        next.reserve(pairs.size() * 2 + 100);

        for (const PairState& p : pairs) {
            for (int trit = 0; trit < 3; ++trit) {
                const u64 c = p.actual + static_cast<u64>(trit) * previous_modulus;
                if (membership.find(c) == membership.end()) continue;

                const u64 s = static_cast<u64>((u128)shift * p.credit % modulus);
                const u64 alt = (c + modulus - s) % modulus;
                if (membership.find(alt) != membership.end()) {
                    next.push_back({c, p.credit});
                }
            }
        }

        pairs.swap(next);
        const std::size_t idx = static_cast<std::size_t>(K - 18);
        assert(pairs.size() == expected_pairs[idx]);
        assert(credit_count(pairs) == expected_credits[idx]);

        std::cout << "K=" << K
                  << " pairs=" << pairs.size()
                  << " credits=" << credit_count(pairs) << "\n";
    }

    std::cout << "bounded-credit labeled lift sieve: PASS\n";
    if (maxK >= 30) {
        std::cout << "150 of 397 credits are globally removed by K=30.\n";
    }
    if (maxK >= 36) {
        std::cout << "247-credit plateau verified through K=36.\n";
    }
    return 0;
}
