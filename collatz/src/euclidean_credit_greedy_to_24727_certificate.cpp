#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>
#include <vector>

// Exact constructive predecessor-credit path through the Euclidean
// continued-fraction hierarchy, ending at the length-24727 convergent.
//
// Only the neutral base blocks U6 and U7 are enumerated.  Larger return
// words are evaluated as compositions of the exact integer transducers
// D -> T_B(D).  At each base block this verifier chooses the largest valid
// successor, so the final values are constructive lower bounds on the
// maximum available credit, not claims of global optimality.

struct Item {
    std::uint64_t R;
};

struct MinItem {
    std::uint64_t R = std::numeric_limits<std::uint64_t>::max();
};

static std::uint64_t p3(int n) {
    std::uint64_t x = 1;
    while (n--) x *= 3ULL;
    return x;
}

static std::uint64_t correction(std::uint32_t mask, int L) {
    std::uint64_t R = 0;
    for (int i = 0; i < L; ++i) {
        if ((mask >> i) & 1U) R = 3ULL * R + (1ULL << i);
    }
    return R;
}

static bool neutral(std::uint32_t mask, const std::string& mechanical) {
    int h = 0;
    for (int i = 0; i < static_cast<int>(mechanical.size()); ++i) {
        h += static_cast<int>((mask >> i) & 1U)
             - static_cast<int>(mechanical[static_cast<std::size_t>(i)] - '0');
        if (h < 0) return false;
    }
    return h == 0;
}

static std::vector<Item> enumerate_neutral(const std::string& mechanical, int q) {
    const int L = static_cast<int>(mechanical.size());
    std::vector<Item> out;

    std::uint32_t comb = (1U << q) - 1U;
    const std::uint32_t limit = 1U << L;

    while (comb < limit) {
        if (neutral(comb, mechanical)) out.push_back({correction(comb, L)});

        const std::uint32_t x = comb & (~comb + 1U);
        const std::uint32_t y = comb + x;
        if (y == 0 || y >= limit) break;
        comb = (((comb & ~y) / x) >> 1U) | y;
    }
    return out;
}

struct Block {
    int q;
    int L;
    std::vector<Item> values;
    std::unordered_map<std::uint64_t, MinItem> minimum_by_residue;
    std::unordered_map<long long, long long> cache;
};

static Block make_block(const std::string& mechanical, int q) {
    Block b{q, static_cast<int>(mechanical.size()),
            enumerate_neutral(mechanical, q), {}, {}};
    const std::uint64_t M = p3(q);
    b.minimum_by_residue.reserve(b.values.size() * 2);
    for (const auto x : b.values) {
        auto& a = b.minimum_by_residue[x.R % M];
        if (x.R < a.R) a.R = x.R;
    }
    return b;
}

// Exact maximum successor inside the chosen neutral base-block fibre.
static long long max_successor(Block& b, long long D) {
    const auto cached = b.cache.find(D);
    if (cached != b.cache.end()) return cached->second;

    const std::uint64_t M = p3(b.q);
    long long best = std::numeric_limits<long long>::min();

    for (const auto high : b.values) {
        __int128 target = static_cast<__int128>(high.R)
                        + (static_cast<__int128>(1) << b.L) * D;
        long long residue = static_cast<long long>(target % static_cast<__int128>(M));
        if (residue < 0) residue += static_cast<long long>(M);

        const auto it = b.minimum_by_residue.find(static_cast<std::uint64_t>(residue));
        if (it == b.minimum_by_residue.end()) continue;

        const __int128 numerator = static_cast<__int128>(high.R)
                                 - static_cast<__int128>(it->second.R)
                                 + (static_cast<__int128>(1) << b.L) * D;
        if (numerator % static_cast<__int128>(M) != 0) continue;

        const long long next = static_cast<long long>(numerator / static_cast<__int128>(M));
        best = std::max(best, next);
    }

    if (best == std::numeric_limits<long long>::min()) {
        std::cerr << "dead state D=" << D << '\n';
        std::exit(2);
    }

    b.cache[D] = best;
    return best;
}

int main() {
    const std::string U6 = "1010110110101101101";
    const std::string U7 = "011011011010110110101101101";

    auto B6 = make_block(U6, 12);
    auto B7 = make_block(U7, 17);

    if (B6.values.size() != 11'433ULL) return 1;
    if (B7.values.size() != 1'741'350ULL) return 2;

    // Physical words and right-to-left transducer evaluation:
    // U9  = U7 U6 U6
    // U10 = U6 U9
    // U15 = U9 U10^5
    // U17 = U10 U15^2
    auto T_U9 = [&](long long D) {
        D = max_successor(B6, D);
        D = max_successor(B6, D);
        D = max_successor(B7, D);
        return D;
    };

    auto T_U10 = [&](long long D) {
        D = T_U9(D);
        D = max_successor(B6, D);
        return D;
    };

    auto T_U15 = [&](long long D) {
        for (int i = 0; i < 5; ++i) D = T_U10(D);
        D = T_U9(D);
        return D;
    };

    auto T_U17 = [&](long long D) {
        D = T_U15(D);
        D = T_U15(D);
        D = T_U10(D);
        return D;
    };

    // Previously certified one-slack credit at U17, length 1054.
    long long D = 162;

    const long long expected[23] = {
        226, 382, 526, 665, 801, 937, 1086, 1222,
        1358, 1500, 1641, 1777, 1917, 2073, 2213, 2362,
        2500, 2646, 2782, 2932, 3075, 3220, 3377
    };

    for (int t = 1; t <= 23; ++t) {
        // U_(17+t) = U15 U17^t in the selected semiconvergent chain.
        const long long credit = T_U15(D);
        const long long length = 485LL + 1054LL * t;

        if (credit != expected[t - 1]) return 10 + t;
        std::cout << "t=" << t
                  << " length=" << length
                  << " constructive_credit=" << credit << '\n';

        if (t < 23) D = T_U17(D);
    }

    if (expected[22] != 3377) return 40;
    std::cout << "final_length=24727\n";
    std::cout << "final_credit_lower_bound=3377\n";
    std::cout << "cache_U6=" << B6.cache.size() << '\n';
    std::cout << "cache_U7=" << B7.cache.size() << '\n';
    return 0;
}
