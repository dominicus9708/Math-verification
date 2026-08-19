#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Exact finite macroblock certificate for the 20 length-19 Sturmian factor
// types occurring in the current Euclidean quotient.
//
// For an incoming relative height H>=0, retain every binary orientation w whose
// cumulative actual-minus-mechanical odd count never drops below -H.  For fixed
// actual odd count q let R(w) be the accelerated affine correction.
//
// The verifier proves two uniform bounds.
//
// (A) Arbitrary same-q correction-source bound:
//
//     |R(u)-R(w)| / 3^(q+H) < 8.
//
// This is the local source term which appears after normalizing predecessor
// credit by 3^H.
//
// (B) Full-Hensel ordinary-credit bound.  If
//
//     R(u) == R(w) (mod 3^q),
//
// so Delta=(R(u)-R(w))/3^q is an ordinary integer predecessor credit, then
//
//     |Delta| < 7*3^H.
//
// The checks are exhaustive for H=0,...,12.  Every length-19 mechanical factor
// has at most 12 ones, hence every binary word has relative-prefix deficit at
// most 12.  For H>=12 the admissible word family is already the complete
// 2^19 cube; increasing H cannot increase either correction span while the
// displayed denominators/bounds only increase.  Therefore the bounds hold for
// all H>=0.
//
// The 20 factor types themselves are independently certified by the existing
// G81 conjugacy / Sturmian-factor theorem in the repository.  This file checks
// the arithmetic bounds on exactly that complete factor list.
//
// This is a reusable macroblock theorem, not a proof of Collatz.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

struct Rec {
    std::uint8_t required_height{};
    std::uint8_t q{};
    u64 R{};
};

struct Key {
    std::uint8_t q{};
    u64 residue{};
    bool operator==(const Key& o) const {
        return q == o.q && residue == o.residue;
    }
};

struct KeyHash {
    std::size_t operator()(const Key& k) const noexcept {
        u64 x = k.residue ^ (u64(k.q) * 0x9e3779b97f4a7c15ULL);
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccdULL;
        x ^= x >> 33;
        return std::size_t(x);
    }
};

struct Span {
    u64 lo = ~u64(0);
    u64 hi = 0;
    unsigned count = 0;
    void add(u64 x) {
        lo = std::min(lo, x);
        hi = std::max(hi, x);
        ++count;
    }
};

const std::array<std::string, 20> FACTORS{{
    "1101101101011011010",
    "1101101011011011010",
    "1101101011011010110",
    "1101011011011010110",
    "1101011011010110110",
    "1011011011010110110",
    "1011011010110110110",
    "1011011010110110101",
    "1011010110110110101",
    "1011010110110101101",
    "1010110110110101101",
    "1010110110101101101",
    "0110110110101101101",
    "0110110101101101101",
    "0110110101101101011",
    "0110101101101101011",
    "0110101101101011011",
    "0101101101101011011",
    "0101101101011011011",
    "0101101101011011010",
}};

std::string u128s(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + unsigned(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

} // namespace

int main() {
    constexpr int L = 19;
    std::array<u64, 40> p3{};
    p3[0] = 1;
    for (int i = 1; i < int(p3.size()); ++i) p3[i] = 3 * p3[i - 1];

    // Length-19 Sturmian factors here have 12 ones except the unique 11-one
    // factor at the wrap end of the 20-type list.
    for (int f = 0; f < 19; ++f)
        if (std::count(FACTORS[f].begin(), FACTORS[f].end(), '1') != 12) return 1;
    if (std::count(FACTORS[19].begin(), FACTORS[19].end(), '1') != 11) return 2;

    u128 best_source_num = 0, best_source_den = 1;
    int best_source_factor = -1, best_source_H = -1, best_source_q = -1;

    u128 best_credit_num = 0, best_credit_den = 1;
    int best_credit_factor = -1, best_credit_H = -1;

    for (int fi = 0; fi < int(FACTORS.size()); ++fi) {
        const std::string& mech = FACTORS[fi];
        std::vector<Rec> recs;
        recs.reserve(1u << L);
        int maximum_required_height = 0;

        for (u32 mask = 0; mask < (1u << L); ++mask) {
            int rel = 0, min_rel = 0, q = 0;
            u64 R = 0;
            for (int i = 0; i < L; ++i) {
                const int b = int((mask >> i) & 1u);
                const int m = mech[std::size_t(i)] - '0';
                rel += b - m;
                min_rel = std::min(min_rel, rel);
                if (b) {
                    R = 3 * R + (u64(1) << i);
                    ++q;
                }
            }
            const int req = std::max(0, -min_rel);
            maximum_required_height = std::max(maximum_required_height, req);
            recs.push_back({std::uint8_t(req), std::uint8_t(q), R});
        }
        if (maximum_required_height > 12) return 3;

        for (int H = 0; H <= 12; ++H) {
            // First: unrestricted same-q correction spans.
            std::array<Span, 20> raw{};
            for (const Rec& r : recs)
                if (r.required_height <= H)
                    raw[r.q].add(r.R);

            for (int q = 0; q <= 19; ++q) {
                if (raw[q].count < 2) continue;
                const u64 span = raw[q].hi - raw[q].lo;
                const u64 den = p3[q + H];

                // Exact source theorem: span / 3^(q+H) < 8.
                if (u128(span) >= u128(8) * den) return 4;

                if (u128(span) * best_source_den > best_source_num * den) {
                    best_source_num = span;
                    best_source_den = den;
                    best_source_factor = fi;
                    best_source_H = H;
                    best_source_q = q;
                }
            }

            // Second: full-Hensel correction classes R mod 3^q.
            std::unordered_map<Key, Span, KeyHash> classes;
            classes.reserve(recs.size() * 2);
            for (const Rec& r : recs) {
                if (r.required_height > H) continue;
                const u64 mod = p3[r.q];
                classes[Key{r.q, r.R % mod}].add(r.R);
            }

            u64 max_credit = 0;
            for (const auto& [key, sp] : classes) {
                if (sp.count < 2) continue;
                const u64 delta = (sp.hi - sp.lo) / p3[key.q];
                max_credit = std::max(max_credit, delta);
            }

            // Exact ordinary-credit theorem: Delta < 7*3^H.
            if (u128(max_credit) >= u128(7) * p3[H]) return 5;

            if (u128(max_credit) * best_credit_den > best_credit_num * p3[H]) {
                best_credit_num = max_credit;
                best_credit_den = p3[H];
                best_credit_factor = fi;
                best_credit_H = H;
            }
        }
    }

    // Regression values for the exact worst cases found by the exhaustive scan.
    if (best_source_num != 3'909'437 || best_source_den != 531'441) return 6;
    if (best_source_factor != 18 || best_source_H != 0 || best_source_q != 12) return 7;

    if (best_credit_num != 55 || best_credit_den != 9) return 8;
    if (best_credit_factor != 18 || best_credit_H != 2) return 9;

    std::cout << "H19 all-factor height/credit/source certificate: PASS\n";
    std::cout << "worst_source " << u128s(best_source_num) << "/"
              << u128s(best_source_den) << " < 8"
              << " factor " << best_source_factor
              << " H " << best_source_H
              << " q " << best_source_q << "\n";
    std::cout << "worst_full_hensel_credit_ratio " << u128s(best_credit_num)
              << "/" << u128s(best_credit_den) << " < 7"
              << " factor " << best_credit_factor
              << " H " << best_credit_H << "\n";
    std::cout << "all_H_ge_0_extension: PASS\n";
    return 0;
}
