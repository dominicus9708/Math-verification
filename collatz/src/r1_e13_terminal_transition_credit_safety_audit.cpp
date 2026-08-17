#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>

// Safety audit for the cutoff-free E=13 terminal inverse-limit automaton.
//
// The terminal automaton temporarily omits the first five even-event ranks
// j=0..4.  Their earliest possible ternary visibility in the physical E=13
// problem is K=438 (rank 4), with the others entering still later.
//
// Therefore a credit removed by the terminal automaton is safely removed from
// the physical problem only if its finite terminal obstruction occurs before
// K=438.  This file computes, for every positive transition-parent credit
// d=1..6859, the maximum number of legal terminal digit transitions possible
// before a rejected state dies.  Accepted inverse-limit states are marked -1.
//
// Exact result:
//
//   accepted credits = 403
//   rejected credits = 6456
//   maximum finite rejection depth = 36
//
// Hence every terminally rejected transition-parent credit is already dead by
// K<=36, far before the first omitted early rank can enter at K=438.

using i64 = long long;

struct Key {
    std::uint8_t a;
    std::uint8_t b;
    i64 c;

    bool operator==(const Key& o) const {
        return a == o.a && b == o.b && c == o.c;
    }
};

struct Hash {
    std::size_t operator()(const Key& k) const noexcept {
        std::uint64_t x = static_cast<std::uint64_t>(k.c)
            ^ (static_cast<std::uint64_t>(k.a) << 56)
            ^ (static_cast<std::uint64_t>(k.b) << 60);
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccdULL;
        x ^= x >> 33;
        x *= 0xc4ceb9fe1a85ec53ULL;
        x ^= x >> 33;
        return static_cast<std::size_t>(x);
    }
};

std::unordered_map<Key,int,Hash> memo;

static i64 block_sum(int after, int before) {
    // Terminal coefficient ranks are 5,...,12.
    return (i64(1) << (5 + before)) - (i64(1) << (5 + after));
}

// Return -1 for an infinite accepted branch.  Otherwise return the maximum
// number of additional legal ternary digit transitions before every branch
// dies.  The recursion is well-founded: a no-assignment transition strictly
// decreases |c|, while every assignment decreases a+b.
int finite_height(int a, int b, i64 c) {
    if (c == 0) return -1;

    const Key key{
        static_cast<std::uint8_t>(a),
        static_cast<std::uint8_t>(b),
        c
    };
    if (const auto it = memo.find(key); it != memo.end()) return it->second;

    int best = 0;

    if (c % 3 == 0) {
        const i64 next = 2 * (c / 3);
        const int h = finite_height(a, b, next);
        if (h < 0) {
            memo.emplace(key, -1);
            return -1;
        }
        best = std::max(best, 1 + h);
    }

    for (int a2 = 0; a2 <= a; ++a2) {
        const i64 A = block_sum(a2, a);
        for (int b2 = 0; b2 <= b; ++b2) {
            if (a2 == a && b2 == b) continue;
            const i64 B = block_sum(b2, b);
            const i64 z = c + B - A;
            if (z % 3 != 0) continue;

            const int h = finite_height(a2, b2, 2 * (z / 3));
            if (h < 0) {
                memo.emplace(key, -1);
                return -1;
            }
            best = std::max(best, 1 + h);
        }
    }

    memo.emplace(key, best);
    return best;
}

int main() {
    constexpr int MAX_CREDIT = 6859;
    constexpr int FIRST_EARLY_VISIBILITY = 438;

    memo.reserve(6'000'000);

    int accepted = 0;
    int rejected = 0;
    int max_rejection_depth = 0;
    int extremal_credit = 0;
    std::map<int,int> histogram;

    for (int d = 1; d <= MAX_CREDIT; ++d) {
        const int h = finite_height(8, 8, (i64(1) << 13) * d);
        if (h < 0) {
            ++accepted;
        } else {
            ++rejected;
            ++histogram[h];
            if (h > max_rejection_depth) {
                max_rejection_depth = h;
                extremal_credit = d;
            }
        }
    }

    if (accepted != 403) return 10;
    if (rejected != 6456) return 11;
    if (max_rejection_depth != 36) return 12;
    if (!(max_rejection_depth < FIRST_EARLY_VISIBILITY)) return 13;

    std::cout << "E13 terminal transition-credit safety audit: PASS\n";
    std::cout << "accepted=" << accepted
              << " rejected=" << rejected << "\n";
    std::cout << "max_finite_rejection_depth=" << max_rejection_depth
              << " extremal_credit=" << extremal_credit << "\n";
    std::cout << "first_omitted_early_rank_visibility="
              << FIRST_EARLY_VISIBILITY << "\n";
    std::cout << "terminal pruning is physically safe through the full 1..6859 envelope\n";
    return 0;
}
