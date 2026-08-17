#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif

// Exact E=13 depth-27 -> depth-73 formation certificate.
//
// Input: the 2^27-bit retained-residue bitset produced by
//   depth27_hensel_retained_residue_builder.cpp
// which contains exactly 1,061,510 exact Hensel-hard dyadic prefixes.
//
// For a selected surviving first-defect channel p, retain only prefixes with
// at most eight even events in the first 27 steps.  An unresolved E=13 path
// must have exactly nine even events by step 73, because the <=8 first-73
// layers were previously closed.  Each retained depth-27 prefix is therefore
// extended only by the required number of suffix-even positions.
//
// Since every current start is <2^73, a complete length-73 parity word has one
// exact ordinary start, not an infinite lift class.  The certificate computes
// that start modulo 2^73, tests the current m=44 ternary core, and follows only
// the resulting tiny set of ordinary starts until first descent or step 1539.
//
// This is not enumeration of the 97,082,021,465 raw nine-zero words.  It is a
// refinement of the already-certified depth-27 formation/Hensel classes.

using u64 = std::uint64_t;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

constexpr int L0 = 27;
constexpr int L = 73;
constexpr std::uint32_t NMECH27 = 29'252'603;

struct Prefix {
    std::uint32_t residue;
    int even_count;
    u128 correction;
};

struct Expected {
    int p;
    int only_k; // -1 means all k<=8
    std::uint64_t prefixes;
    std::uint64_t classes;
    std::uint64_t numeric;
    std::uint64_t core;
    int max_first_descent;
};

static const Expected expected[] = {
    {16,-1,      128ULL,       355'971ULL,        74'554ULL,  0ULL,   0},
    {13,-1,      713ULL,     4'729'858ULL,       986'501ULL,  0ULL,   0},
    {10,-1,    4'033ULL,    56'440'574ULL,    11'770'312ULL,  0ULL,   0},
    { 8,-1,   18'399ULL,   560'447'762ULL,   116'867'675ULL,  6ULL, 395},
    { 5,-1,  103'939ULL, 5'710'084'052ULL, 1'190'716'483ULL, 42ULL, 349},
    { 2, 8,  287'473ULL,    13'223'758ULL,     2'756'951ULL,  1ULL, 195},
    { 2, 7,  183'049ULL,   189'455'715ULL,    39'515'274ULL,  3ULL, 213},
    { 2, 6,   86'283ULL, 1'309'775'940ULL,   273'138'246ULL, 10ULL, 273},
    { 2, 5,   31'019ULL, 5'061'835'515ULL, 1'055'543'943ULL, 46ULL, 302},
};

u128 parse_u128(const std::string& s) {
    u128 x = 0;
    for (char c : s) x = 10*x + static_cast<unsigned>(c-'0');
    return x;
}

std::string to_string_u128(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(static_cast<char>('0' + x%10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

u128 inverse_odd_mod_2pow(u128 a, int bits) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x *= 2 - a*x;
    return x & ((u128(1)<<bits)-1);
}

bool in_current_m44_core(u128 n, u128 lo, u128 hi) {
    if (n < lo || n > hi || n%4 != 3) return false;
    u128 y = (n-3)/4;
    for (int i = 0; i < 44; ++i) {
        const u128 d = y%3;
        if (d > 1) return false;
        y /= 3;
    }
    return y == 1;
}

std::pair<int,int> first_descent_or_1539(u128 n) {
    cpp_int start = 0;
    for (char c : to_string_u128(n)) start = 10*start + (c-'0');
    cpp_int x = start;
    int evens = 0;

    for (int t = 1; t <= 1539; ++t) {
        const bool odd = static_cast<bool>(x & 1);
        if (!odd) ++evens;
        if (odd) x = (3*x+1)/2;
        else x /= 2;
        if (x < start) return {t, evens};
    }
    return {0, evens};
}

const Expected* find_expected(int p, int only_k) {
    for (const auto& e : expected) {
        if (e.p == p && e.only_k == only_k) return &e;
    }
    return nullptr;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "usage: certificate allow27.bin first_defect_p [only_k|-1]\n";
        return 2;
    }

    const std::string bitset_path = argv[1];
    const int target_p = std::atoi(argv[2]);
    const int only_k = argc > 3 ? std::atoi(argv[3]) : -1;

    const Expected* ex = find_expected(target_p, only_k);
    if (!ex) {
        std::cerr << "no frozen checkpoint for this (p,k) mode\n";
        return 3;
    }

    const u128 N0 = parse_u128("3939105844976711153619");
    const u128 NMAX = parse_u128("5908625413101667397287");

    std::ifstream f(bitset_path, std::ios::binary);
    if (!f) return 4;
    std::vector<u64> retained((1u<<27)/64);
    f.read(reinterpret_cast<char*>(retained.data()), retained.size()*sizeof(u64));
    if (!f) return 5;

    const u128 modulus = u128(1)<<73;
    const u128 mask73 = modulus-1;
    const std::uint32_t mask27 = (1u<<27)-1;

    u128 p3_64 = 1;
    for (int i = 0; i < 64; ++i) p3_64 = (3*p3_64)&mask73;
    const u128 inv3_64 = inverse_odd_mod_2pow(p3_64, 73);

    std::array<u128,73> p2{};
    for (int i = 0; i < 73; ++i) p2[i] = u128(1)<<i;

    std::vector<Prefix> prefixes;
    std::array<std::uint64_t,10> k_hist{};

    for (std::size_t w = 0; w < retained.size(); ++w) {
        u64 word = retained[w];
        while (word) {
            const int bit = __builtin_ctzll(word);
            const std::uint32_t r = static_cast<std::uint32_t>(w*64 + bit);
            word &= word-1;

            const std::uint32_t diff = (r-NMECH27)&mask27;
            const int p = diff ? __builtin_ctz(diff) : 27;
            if (p != target_p) continue;

            std::uint64_t x = r;
            int k = 0;
            u128 R = 0;
            for (int t = 0; t < 27; ++t) {
                const int parity = static_cast<int>(x&1);
                if (!parity) ++k;
                else R = (3*R + p2[t])&mask73;
                x = parity ? (3*x+1)/2 : x/2;
            }

            if (k < static_cast<int>(k_hist.size())) ++k_hist[k];
            if (k <= 8 && (only_k < 0 || k == only_k)) {
                prefixes.push_back({r,k,R});
            }
        }
    }

    std::uint64_t total_classes = 0;
    std::uint64_t numeric_classes = 0;
    std::vector<u128> core_starts;

#ifdef _OPENMP
#pragma omp parallel
#endif
    {
        std::uint64_t local_classes = 0;
        std::uint64_t local_numeric = 0;
        std::vector<u128> local_core;

#ifdef _OPENMP
#pragma omp for schedule(dynamic,1)
#endif
        for (long long ii = 0; ii < static_cast<long long>(prefixes.size()); ++ii) {
            const Prefix P = prefixes[static_cast<std::size_t>(ii)];
            const int need_zeros = 9-P.even_count;

            std::function<void(int,int,u128)> extend = [&](int pos, int left, u128 R) {
                if (46-pos < left) return;
                if (pos == 46) {
                    if (left != 0) return;
                    ++local_classes;

                    const u128 n = (modulus - ((inv3_64*R)&mask73))&mask73;
                    if (n < N0 || n > NMAX) return;
                    ++local_numeric;
                    if (in_current_m44_core(n, N0, NMAX)) local_core.push_back(n);
                    return;
                }

                const int global_pos = 27+pos;

                // Choose an even symbol at this suffix position.
                if (left > 0) extend(pos+1, left-1, R);

                // Choose an odd symbol.
                if (46-pos-1 >= left) {
                    extend(pos+1, left, (3*R+p2[global_pos])&mask73);
                }
            };

            extend(0, need_zeros, P.correction);
        }

#ifdef _OPENMP
#pragma omp critical
#endif
        {
            total_classes += local_classes;
            numeric_classes += local_numeric;
            core_starts.insert(core_starts.end(), local_core.begin(), local_core.end());
        }
    }

    std::sort(core_starts.begin(), core_starts.end());
    core_starts.erase(std::unique(core_starts.begin(), core_starts.end()), core_starts.end());

    int unresolved_e13 = 0;
    int max_first_descent = 0;

    for (u128 n : core_starts) {
        const auto [first_descent, evens] = first_descent_or_1539(n);
        std::cout << to_string_u128(n)
                  << " first_descent=" << first_descent
                  << " evens_at_stop_or_1539=" << evens << "\n";

        if (first_descent) max_first_descent = std::max(max_first_descent, first_descent);
        else if (evens == 13) ++unresolved_e13;
    }

    assert(prefixes.size() == ex->prefixes);
    assert(total_classes == ex->classes);
    assert(numeric_classes == ex->numeric);
    assert(core_starts.size() == ex->core);
    assert(max_first_descent == ex->max_first_descent);
    assert(unresolved_e13 == 0);

    std::cout << "E13 depth27-to73 formation certificate: PASS\n";
    std::cout << "p=" << target_p << " only_k=" << only_k
              << " prefixes=" << prefixes.size()
              << " classes=" << total_classes
              << " numeric=" << numeric_classes
              << " core=" << core_starts.size()
              << " unresolved_E13=0"
              << " max_first_descent=" << max_first_descent << "\n";

    std::cout << "depth27 k histogram:";
    for (int k = 0; k < static_cast<int>(k_hist.size()); ++k) {
        if (k_hist[k]) std::cout << " k" << k << "=" << k_hist[k];
    }
    std::cout << "\n";

    return 0;
}
