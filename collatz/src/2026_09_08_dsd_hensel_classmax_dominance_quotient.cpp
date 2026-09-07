// MATH-013: DSD exact class-max dominance quotient for root-Hensel computation.
//
// Scope:
//   * symbolic length-L parity words;
//   * correction C(w) defined by C <- 3C + 2^i on odd bit i;
//   * root-Hensel translation classes keyed by (q, C mod 3^q);
//   * safe computational dominance: retain only the largest quotient
//       h = floor(C / 3^q)
//     in each class.
//
// This quotient accelerates class-max computation.  It does NOT by itself
// exclude a Collatz candidate outside a separately valid positive-credit
// bound such as the MATH-012 gate k-q<=71 (or an actual start-specific bound).
//
// Default: exact quotient DP through L=24.
// Use --full26 for the larger L=26 state-count regression.
//
// Build:
//   g++ -O3 -std=c++17 2026_09_08_dsd_hensel_classmax_dominance_quotient.cpp -o m13

#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;

struct State {
    u64 key;  // q in high bits, ternary residue r in low bits; valid here for L<=26
    u32 h;    // maximum floor(C/3^q) retained in this class
};

static inline u64 pack_key(int q, u64 r) {
    return (u64(q) << 48) | r;
}
static inline int unpack_q(u64 key) { return int(key >> 48); }
static inline u64 unpack_r(u64 key) { return key & ((1ULL << 48) - 1); }

u64 p3(int q) {
    u64 x = 1;
    while (q--) x *= 3ULL;
    return x;
}

std::pair<int,u64> correction_from_word(const std::string& w) {
    int q = 0;
    u64 C = 0;
    for (int i = 0; i < int(w.size()); ++i) {
        if (w[i] == '1') {
            C = 3ULL * C + (1ULL << i);
            ++q;
        }
    }
    return {q,C};
}

struct Row {
    int L;
    u64 classes_including_zero;
    u64 cumulative_child_transitions;
};

std::vector<Row> quotient_dp(int maxL) {
    std::vector<u64> pow3(maxL + 2, 1);
    for (int i = 1; i <= maxL + 1; ++i) pow3[i] = pow3[i-1] * 3ULL;

    std::vector<State> dp{{pack_key(0,0),0}}, next;
    std::vector<Row> rows;
    rows.push_back({0,1,0});
    u64 transitions = 0;

    for (int k = 0; k < maxL; ++k) {
        next.clear();
        next.reserve(dp.size() * 2);

        for (auto const& s : dp) {
            const int q = unpack_q(s.key);
            const u64 r = unpack_r(s.key);

            // even child: C, q, r, h unchanged
            next.push_back(s);

            // odd child at new position k:
            // C' = 3C + 2^k
            //    = h*3^(q+1) + (3r+2^k).
            // Child class key depends only on (q,r,k), not on h, and
            // h' = h + carry.  Therefore larger h stays larger after this
            // transition: a dominated parent can never recover downstream.
            const int q1 = q + 1;
            const u64 t = 3ULL * r + (1ULL << k);
            const u64 mod = pow3[q1];
            const u64 r1 = t % mod;
            const u32 h1 = s.h + u32(t / mod);
            next.push_back({pack_key(q1,r1),h1});
            transitions += 2;
        }

        std::sort(next.begin(), next.end(), [](State const& a, State const& b) {
            return a.key < b.key;
        });

        // Exact dominance collapse: one maximum h per class key.
        std::size_t write = 0;
        for (std::size_t i = 0; i < next.size();) {
            std::size_t j = i + 1;
            u32 best_h = next[i].h;
            while (j < next.size() && next[j].key == next[i].key) {
                if (next[j].h > best_h) best_h = next[j].h;
                ++j;
            }
            next[write++] = {next[i].key,best_h};
            i = j;
        }
        next.resize(write);
        dp.swap(next);
        rows.push_back({k+1,u64(dp.size()),transitions});
    }
    return rows;
}

void verify_information_loss_witness() {
    const std::string w = "110110110101010110110101";
    const std::string u = "111111111101011000100100";
    auto [qw,Cw] = correction_from_word(w);
    auto [qu,Cu] = correction_from_word(u);
    assert(qw == 15 && qu == 15);
    assert(Cw == 74913815ULL);
    assert(Cu == 17518187ULL);
    const u64 mod = p3(qw);
    assert(mod == 14348907ULL);
    assert(Cw % mod == 3169280ULL);
    assert(Cu % mod == 3169280ULL);
    assert(Cw / mod == 5ULL);
    assert(Cu / mod == 1ULL);
    assert((Cw - Cu) / mod == 4ULL);
    // Same k=24, q=15, d=k-q=9 and same class residue, different credit score.
}

int main(int argc, char** argv) {
    int maxL = 24;
    if (argc > 1 && std::string(argv[1]) == "--full26") maxL = 26;

    verify_information_loss_witness();

    auto t0 = std::chrono::steady_clock::now();
    auto rows = quotient_dp(maxL);
    auto t1 = std::chrono::steady_clock::now();

    // Exact state-count regressions. Counts include the all-zero q=0 class;
    // subtract one when comparing with the 2^L-1 nonzero words.
    const u64 expected24 = 3213595ULL;
    assert(rows.at(24).classes_including_zero == expected24);
    assert(rows.at(24).cumulative_child_transitions == 7141552ULL);

    if (maxL >= 25) {
        assert(rows.at(25).classes_including_zero == 6116464ULL);
        assert(rows.at(25).cumulative_child_transitions == 13568742ULL);
    }
    if (maxL >= 26) {
        assert(rows.at(26).classes_including_zero == 11650326ULL);
        assert(rows.at(26).cumulative_child_transitions == 25801670ULL);
    }

    std::cout << "PASS\n";
    std::cout << "information-loss witness: (k,q,d)=(24,15,9), class residue=3169280, h=5 versus h=1\n";
    std::cout << "L nonzero_words nonzero_classmax_states state_ratio baseline_child_transitions quotient_child_transitions transition_ratio\n";

    for (int L : {24,25,26}) {
        if (L > maxL) continue;
        const u64 words = (1ULL << L) - 1ULL;
        const u64 classes = rows.at(L).classes_including_zero - 1ULL;
        const u64 baseline_transitions = 2ULL * ((1ULL << L) - 1ULL);
        const u64 quotient_transitions = rows.at(L).cumulative_child_transitions;
        std::cout << L << ' ' << words << ' ' << classes << ' '
                  << std::fixed << std::setprecision(9) << double(words)/double(classes) << ' '
                  << baseline_transitions << ' ' << quotient_transitions << ' '
                  << double(baseline_transitions)/double(quotient_transitions) << "\n";
    }

    const double seconds = std::chrono::duration<double>(t1-t0).count();
    std::cout << "quotient-DP wall seconds (environment-dependent diagnostic): " << seconds << "\n";
    std::cout << "DSD outcome: exact downstream-stable dominance quotient for root-Hensel class-max computation\n";
    std::cout << "scope warning: class-max dominance is candidate-excluding only when positive ordinary-start credit is separately legal\n";
    std::cout << "same (q,r) or same d is not the same full Collatz trajectory\n";
    std::cout << "Collatz remains OPEN\n";
}
