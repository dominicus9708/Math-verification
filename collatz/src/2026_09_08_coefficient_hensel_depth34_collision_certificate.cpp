// MATH-037: first non-vacuous root-Hensel collision layer inside the
// coefficient-surviving candidate language.
//
// This certificate re-extracts the five q=22 collision classes at depth 34
// by intersecting the depth-33 q=22 even-child classes with the depth-33 q=21
// odd-child classes.  It also verifies that each collision has credit 4 and
// yields an ordinary-start translation by exactly four residue units modulo
// 2^34.
//
// Scope note: the previously completed full external-partition audit found
// zero coefficient-language Hensel collisions through depth 33 and exactly
// five total collision classes at depth 34.  This certificate isolates and
// reproduces all five of those classes in the minimal q=22 layer.

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;

struct Rec {
    u64 residue;
    u64 correction;
    u64 word;
};

static int qminv[34];
static u64 p3[40];

static void collect_q22(int k, int q, u64 C, u64 word, std::vector<Rec>& out) {
    if (q > 22 || q + (33 - k) < 22) return;
    if (k == 33) {
        if (q == 22) out.push_back({C % p3[22], C, word});
        return;
    }
    const int nk = k + 1;
    if (q >= qminv[nk])
        collect_q22(nk, q, C, word, out);
    if (q + 1 >= qminv[nk])
        collect_q22(nk, q + 1, 3 * C + (1ULL << k), word | (1ULL << k), out);
}

template<class F>
static void stream_q21(int k, int q, u64 C, u64 word, F&& fn) {
    if (q > 21 || q + (33 - k) < 21) return;
    if (k == 33) {
        if (q == 21) fn(C, word);
        return;
    }
    const int nk = k + 1;
    if (q >= qminv[nk])
        stream_q21(nk, q, C, word, fn);
    if (q + 1 >= qminv[nk])
        stream_q21(nk, q + 1, 3 * C + (1ULL << k), word | (1ULL << k), fn);
}

static u64 inverse_odd_mod_pow2(u64 a, int bits) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x & ((1ULL << bits) - 1);
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 40; ++i) p3[i] = p3[i - 1] * 3ULL;

    for (int k = 1; k <= 33; ++k) {
        int q = 0;
        u64 a = 1;
        const u64 target = 1ULL << k;
        while (a < target) { a *= 3ULL; ++q; }
        qminv[k] = q;
    }

    std::vector<Rec> even_q22;
    even_q22.reserve(27'000'000);
    collect_q22(0, 0, 0, 0, even_q22);
    assert(even_q22.size() == 26'521'599ULL);

    std::sort(even_q22.begin(), even_q22.end(), [](const Rec& a, const Rec& b) {
        return a.residue < b.residue;
    });

    // The depth-33 q=22 layer itself is injective.
    for (std::size_t i = 1; i < even_q22.size(); ++i)
        assert(even_q22[i - 1].residue != even_q22[i].residue);

    const u64 mod = p3[22];
    const u64 add = 1ULL << 33;
    std::vector<std::array<u64,5>> hits; // residue, Csmall, Clarge, smallword, largeword
    u64 q21_words = 0;

    stream_q21(0, 0, 0, 0, [&](u64 C, u64 word) {
        ++q21_words;
        const u64 Codd = 3 * C + add;
        const u64 residue = Codd % mod;
        auto it = std::lower_bound(even_q22.begin(), even_q22.end(), residue,
            [](const Rec& r, u64 x) { return r.residue < x; });
        if (it != even_q22.end() && it->residue == residue) {
            assert(Codd > it->correction);
            assert((Codd - it->correction) / mod == 4ULL);
            hits.push_back({residue, it->correction, Codd,
                            it->word, word | (1ULL << 33)});
        }
    });

    assert(q21_words == 13'472'296ULL);
    assert(hits.size() == 5ULL);

    std::sort(hits.begin(), hits.end(), [](auto const& a, auto const& b) {
        return a[0] < b[0];
    });

    const std::array<u64,5> expected_residues = {
        4'015'726'592ULL,
        4'559'922'176ULL,
        5'240'166'656ULL,
        8'585'544'704ULL,
        9'875'489'792ULL
    };
    for (int i = 0; i < 5; ++i) assert(hits[i][0] == expected_residues[i]);

    // Convert each correction to its canonical ordinary-start residue mod 2^34.
    // Larger correction corresponds to a start smaller by exactly 4.
    const u64 M = 1ULL << 34;
    const u64 inv3q = inverse_odd_mod_pow2(p3[22] & (M - 1), 34);
    std::vector<std::pair<u64,u64>> start_pairs;
    for (auto const& h : hits) {
        const u64 Nsmallcorr = ((M - (h[1] & (M - 1))) * inv3q) & (M - 1);
        const u64 Nlargecorr = ((M - (h[2] & (M - 1))) * inv3q) & (M - 1);
        assert((Nsmallcorr - Nlargecorr) & (M - 1));
        assert(((Nsmallcorr - Nlargecorr) & (M - 1)) == 4ULL);
        start_pairs.push_back({Nsmallcorr, Nlargecorr});
    }

    std::sort(start_pairs.begin(), start_pairs.end());
    const std::array<u64,5> loser_residues = {
        5'348'744'191ULL,
        7'435'082'751ULL,
        11'843'133'439ULL,
        15'231'450'879ULL,
        15'257'926'655ULL
    };
    for (int i = 0; i < 5; ++i) {
        assert(start_pairs[i].first == loser_residues[i]);
        assert(start_pairs[i].second + 4 == start_pairs[i].first);
    }

    std::cout << "PASS MATH-037\n";
    std::cout << "depth33 q22 words=" << even_q22.size()
              << " q21 words=" << q21_words << "\n";
    std::cout << "depth34 q22 collision classes=" << hits.size() << "\n";
    std::cout << "all credits=4\n";
    std::cout << "loser ordinary-start residues mod 2^34:";
    for (auto x : loser_residues) std::cout << ' ' << x;
    std::cout << "\nfirst universal cell: OPEN\nCollatz: OPEN\n";
}
