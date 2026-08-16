#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <unordered_set>
#include <vector>

// Exact E=13 obstruction to pulling the specific G13 entrance difference 4096
// backward through the 1539-step pre-gate segment.
//
// If two ordinary pre-gate paths have exactly E=13 even events, write
//
//   2^1539 U_T = 3^1526 U_0 + C(P),
//
// where
//
//   C(P)=sum_{j=0}^{12} 2^{p_j} 3^{1526-p_j+j}.
//
// If their G13 entrance states differ by 4096, integrality of their original
// starting-value difference requires
//
//   C(P')-C(P) == -2^1539*4096 (mod 3^1526).
//
// It is therefore enough to disprove this congruence modulo one finite power
// 3^K.
//
// For K<=28 the exact run-cap upper bounds on the first five even-event ranks
// imply that ranks j=0..4 occur too early to affect C(P) mod 3^K.  Hence every
// possible low-K residue is represented by a terminal active suffix j0..12,
// j0>=5.  For an active rank write
//
//   p_j = 1526 + j - (K-1) + b_j,
//
// where 0<=b_j<=K-1 and b_j is nondecreasing.  This is an exact over-family:
// every ordinary E=13 correction residue mod 3^K lies in it.
//
// The certificate first constructs the complete K=18 residue set and all
// 4096-separated pairs, then lifts only descendants of those pair endpoints.
// Projection S_{K+1}->S_K makes this targeted Hensel lifting exhaustive.
//
// Exact pair counts:
//
//   K=18 : 545
//   K=19 : 204
//   K=20 : 158
//   K=21 :  83
//   K=22 :  42
//   K=23 :  20
//   K=24 :   4
//   K=25 :   2
//   K=26 :   2
//   K=27 :   2
//   K=28 :   0
//
// Therefore no pair of ordinary E=13 pre-gate paths can arrive at states that
// differ by 4096.  This closes the pullback of the particular G13 start-credit
// 4096 through the E=13 pre-gate channel.
//
// Logical scope: this does NOT prove that every R1 survivor must carry a G13
// 4096 relation.  It closes this predecessor-construction channel only, and is
// not a proof of Collatz.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr int T = 1539;
constexpr int Q = 1526;
constexpr u64 G13_ENTRANCE_CREDIT = 4096;

struct Pair {
    u64 actual;
    u64 alternate;
};

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

// Complete S_18.  3^18 needs only a ~48 MB bitset.
std::vector<u64> build_complete_S18() {
    constexpr int K = 18;
    const u64 modulus = pow3(K);
    std::vector<u64> bits((modulus + 63) / 64, 0);
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
    add(0);  // no event rank reaches the low 18 ternary digits

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

std::vector<Pair> initial_pairs_18(const std::vector<u64>& S18) {
    const int K = 18;
    const u64 modulus = pow3(K);

    std::vector<u64> bits((modulus + 63) / 64, 0);
    for (u64 c : S18) bits[c >> 6] |= 1ULL << (c & 63);
    auto has = [&](u64 x) -> bool {
        return (bits[x >> 6] >> (x & 63)) & 1ULL;
    };

    const u64 shift = static_cast<u64>(
        (u128)mod_pow(2, T, modulus) * G13_ENTRANCE_CREDIT % modulus);

    std::vector<Pair> pairs;
    for (u64 c : S18) {
        const u64 alt = (c + modulus - shift) % modulus;
        if (has(alt)) pairs.push_back({c, alt});
    }
    assert(pairs.size() == 545ULL);
    return pairs;
}

// Enumerate only S_K residues whose projection mod 3^(K-1) is one of the
// previous pair endpoints.  Every possible lift of a previous pair is present.
std::vector<Pair> lift_pairs(int K, const std::vector<Pair>& previous) {
    assert(19 <= K && K <= 28);
    const u64 modulus = pow3(K);
    const u64 prev_modulus = modulus / 3;

    std::unordered_set<u64, Hash64> projected;
    std::unordered_set<u64, Hash64> actual_projected;
    projected.reserve(previous.size() * 4 + 16);
    actual_projected.reserve(previous.size() * 2 + 16);

    for (const Pair& p : previous) {
        projected.insert(p.actual);
        projected.insert(p.alternate);
        actual_projected.insert(p.actual);
    }

    const auto term = terminal_terms(K, modulus);
    std::vector<u64> found;
    found.reserve(projected.size() * 3 + 16);

    auto maybe_add = [&](u64 r) {
        if (projected.find(r % prev_modulus) != projected.end()) {
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
    std::unordered_set<u64, Hash64> membership(found.begin(), found.end());

    const u64 shift = static_cast<u64>(
        (u128)mod_pow(2, T, modulus) * G13_ENTRANCE_CREDIT % modulus);

    std::vector<Pair> next;
    for (u64 c : found) {
        if (actual_projected.find(c % prev_modulus) == actual_projected.end()) {
            continue;
        }
        const u64 alt = (c + modulus - shift) % modulus;
        if (membership.find(alt) != membership.end()) {
            next.push_back({c, alt});
        }
    }

    std::sort(next.begin(), next.end(), [](const Pair& a, const Pair& b) {
        if (a.actual != b.actual) return a.actual < b.actual;
        return a.alternate < b.alternate;
    });
    next.erase(std::unique(next.begin(), next.end(), [](const Pair& a, const Pair& b) {
        return a.actual == b.actual && a.alternate == b.alternate;
    }), next.end());

    return next;
}

}  // namespace

int main() {
    // For K<=28, a term from event rank j affects mod 3^K only if
    // p_j >= Q+j-(K-1).  Existing exact maximal-cover bounds are
    // p_0<=72, p_1<=186, p_2<=365, p_3<=647, p_4<=1093.
    // At K=28 the activation thresholds are 1499,1500,1501,1502,1503,
    // so ranks 0..4 are rigorously absent from every S_K used here.
    const int early_max[5] = {72, 186, 365, 647, 1093};
    for (int j = 0; j < 5; ++j) {
        const int threshold_at_28 = Q + j - 27;
        assert(early_max[j] < threshold_at_28);
    }

    const auto S18 = build_complete_S18();
    std::vector<Pair> pairs = initial_pairs_18(S18);

    const std::vector<std::size_t> expected{
        545, 204, 158, 83, 42, 20, 4, 2, 2, 2, 0
    };

    std::cout << "K=18 pairs=" << pairs.size() << "\n";
    assert(pairs.size() == expected[0]);

    for (int K = 19; K <= 28; ++K) {
        pairs = lift_pairs(K, pairs);
        const std::size_t want = expected[static_cast<std::size_t>(K - 18)];
        assert(pairs.size() == want);
        std::cout << "K=" << K << " pairs=" << pairs.size() << "\n";

        if (K >= 24 && !pairs.empty()) {
            for (const Pair& p : pairs) {
                std::cout << "  " << p.actual << " -> " << p.alternate << "\n";
            }
        }
    }

    assert(pairs.empty());
    std::cout << "E13 4096 pre-gate pullback obstruction: PASS\n";
    std::cout << "No correction pair survives modulo 3^28.\n";
    return 0;
}
