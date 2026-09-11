// MATH-069 stage B: exact hybrid AP/ordinary-set union engine for r=16.
//
// Input (stdin): target0<TAB>odd_step<TAB>count, produced by
// 2026_09_11_math069_r16_leaf_export.py.
//
// The engine audits the three multiplicity bands separately.  Non-singleton
// arithmetic progressions are unioned exactly on identical (b,a mod b) grids.
// Singleton states are stored only by their ordinary integer value, so exact
// trajectory merges are deduplicated without carrying obsolete AP lineage.
//
// unsigned __int128 is used only with explicit overflow guards; any operation
// that could exceed its exact range aborts the certificate.
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <vector>

using u128 = __uint128_t;
using u64 = std::uint64_t;

static constexpr u128 UMAX = ~u128(0);
static const u128 LO = u128(1) << 71;

static u128 parse128(const std::string& s) {
    u128 x = 0;
    for (char c : s) {
        assert(std::isdigit(static_cast<unsigned char>(c)));
        unsigned d = unsigned(c - '0');
        assert(x <= (UMAX - d) / 10);
        x = x * 10 + d;
    }
    return x;
}

static std::string str128(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + unsigned(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static u128 add_checked(u128 a, u128 b) {
    assert(a <= UMAX - b);
    return a + b;
}

static u128 mul_checked(u128 a, u128 b) {
    if (a == 0 || b == 0) return 0;
    assert(a <= UMAX / b);
    return a * b;
}

struct AP {
    u128 a;
    u128 b;
    u64 m;
};

struct Interval {
    u128 b, r, k0, k1;
};

static std::vector<AP> merge_multi(const std::vector<AP>& input) {
    std::vector<Interval> v;
    v.reserve(input.size());
    for (const auto& x : input) {
        assert(x.m >= 2 && x.b > 0);
        u128 r = x.a % x.b;
        u128 k0 = (x.a - r) / x.b;
        u128 k1 = add_checked(k0, u128(x.m - 1));
        v.push_back({x.b, r, k0, k1});
    }

    std::sort(v.begin(), v.end(), [](const Interval& x, const Interval& y) {
        if (x.b != y.b) return x.b < y.b;
        if (x.r != y.r) return x.r < y.r;
        if (x.k0 != y.k0) return x.k0 < y.k0;
        return x.k1 < y.k1;
    });

    std::vector<AP> out;
    out.reserve(v.size());
    for (std::size_t i = 0; i < v.size();) {
        u128 b = v[i].b, r = v[i].r, lo = v[i].k0, hi = v[i].k1;
        std::size_t j = i + 1;
        while (j < v.size() && v[j].b == b && v[j].r == r &&
               v[j].k0 <= add_checked(hi, 1)) {
            if (v[j].k1 > hi) hi = v[j].k1;
            ++j;
        }
        u128 width = hi - lo + 1;
        assert(width <= std::numeric_limits<u64>::max());
        u128 a = add_checked(r, mul_checked(b, lo));
        out.push_back({a, b, u64(width)});
        i = j;
    }
    return out;
}

static void uniq(std::vector<u128>& v) {
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
}

struct BandState {
    std::vector<AP> ap;
    std::vector<u128> singletons;
};

static BandState normalize(std::vector<AP> raw) {
    BandState s;
    std::vector<AP> multi;
    multi.reserve(raw.size());
    for (auto x : raw) {
        if (x.m == 1) s.singletons.push_back(x.a);
        else multi.push_back(x);
    }
    uniq(s.singletons);
    s.ap = merge_multi(multi);
    return s;
}

static BandState advance(const BandState& s) {
    std::vector<u128> next_singletons;
    next_singletons.reserve(s.singletons.size() + s.ap.size());
    std::vector<AP> next_ap;
    next_ap.reserve(s.ap.size() * 2);

    for (u128 n : s.singletons) {
        if (n <= LO) continue;
        u128 z;
        if ((n & 1) == 0) {
            z = n / 2;
        } else {
            z = add_checked(mul_checked(3, n), 1) / 2;
        }
        if (z > LO) next_singletons.push_back(z);
    }

    for (auto x : s.ap) {
        assert(x.m >= 2 && (x.b & 1));
        if (x.a <= LO) {
            u128 t = (LO - x.a) / x.b;
            if (t >= u128(x.m - 1)) continue;
            u64 drop = u64(t + 1);
            x.a = add_checked(x.a, mul_checked(x.b, drop));
            x.m -= drop;
        }

        for (u64 rho = 0; rho <= 1; ++rho) {
            if (rho >= x.m) continue;
            u64 count = (x.m - 1 - rho) / 2 + 1;
            u128 base = add_checked(x.a, mul_checked(x.b, rho));
            u128 a1, b1;
            if ((base & 1) == 0) {
                a1 = base / 2;
                b1 = x.b;
            } else {
                a1 = add_checked(mul_checked(3, base), 1) / 2;
                b1 = mul_checked(3, x.b);
            }
            if (count == 1) {
                if (a1 > LO) next_singletons.push_back(a1);
            } else {
                next_ap.push_back({a1, b1, count});
            }
        }
    }

    uniq(next_singletons);
    BandState out;
    out.singletons = std::move(next_singletons);
    out.ap = merge_multi(next_ap);
    return out;
}

static u128 represented_occurrences(const BandState& s) {
    u128 n = s.singletons.size();
    for (const auto& x : s.ap) n += x.m;
    return n;
}

struct ExpectedBand {
    u64 raw_cylinders;
    u128 raw_occurrences;
    u64 initial_ap;
    u64 initial_singletons;
    u128 initial_occurrences;
    int reach_depth;
    u128 last_above;
    u128 first_below;
};

static void audit_band(std::vector<AP> raw, const ExpectedBand& e,
                       const char* name) {
    assert(raw.size() == e.raw_cylinders);
    u128 raw_occ = 0;
    for (const auto& x : raw) raw_occ += x.m;
    assert(raw_occ == e.raw_occurrences);

    BandState s = normalize(std::move(raw));
    assert(s.ap.size() == e.initial_ap);
    assert(s.singletons.size() == e.initial_singletons);
    assert(represented_occurrences(s) == e.initial_occurrences);

    u128 last_singleton = 0;
    for (int depth = 0; depth <= e.reach_depth; ++depth) {
        if (depth == e.reach_depth - 1) {
            assert(s.ap.empty());
            assert(s.singletons.size() == 1);
            last_singleton = s.singletons[0];
            assert(last_singleton == e.last_above);
            assert(last_singleton > LO);
        }
        if (depth == e.reach_depth) {
            assert(s.ap.empty() && s.singletons.empty());
            break;
        }
        s = advance(s);
    }

    u128 mapped = ((e.last_above & 1) == 0)
        ? e.last_above / 2
        : add_checked(mul_checked(3, e.last_above), 1) / 2;
    assert(mapped == e.first_below);
    assert(mapped <= LO);

    std::cerr << "closed " << name
              << " raw_cylinders=" << e.raw_cylinders
              << " raw_occurrences=" << str128(e.raw_occurrences)
              << " initial_union_occurrences=" << str128(e.initial_occurrences)
              << " max_reach_depth=" << e.reach_depth << "\n";
}

int main() {
    std::vector<AP> small, medium, large;
    std::string a_s, b_s;
    u64 m;
    while (std::cin >> a_s >> b_s >> m) {
        AP x{parse128(a_s), parse128(b_s), m};
        if (m <= 64) small.push_back(x);
        else if (m <= 1023) medium.push_back(x);
        else large.push_back(x);
    }

    audit_band(
        std::move(small),
        {2'238'071, u128(12'763'331), 898'392, 612'619,
         u128(10'471'444), 326,
         parse128("4078779061073975415814"),
         parse128("2039389530536987707907")},
        "m<=64");

    audit_band(
        std::move(medium),
        {154'255, u128(39'692'496), 136'542, 0,
         u128(35'768'873), 314,
         parse128("2844034437459965374174"),
         parse128("1422017218729982687087")},
        "65<=m<=1023");

    audit_band(
        std::move(large),
        {24'803, u128(160'551'069), 23'103, 0,
         u128(155'249'446), 347,
         parse128("2401457543131136922308"),
         parse128("1200728771565568461154")},
        "m>=1024");

    std::cerr << "PASS MATH-069: complete r=16 layer closed; r>=16 closed\n";
    return 0;
}
