// MATH-070 stage B: exact multiplicity-band AP-union closure engine for r=15.
//
// Input (stdin): target0<TAB>odd_step<TAB>count, produced by
// 2026_09_11_math070_r15_leaf_export.py.
//
// The raw negative-candidate cylinders are partitioned by their INITIAL
// multiplicity. Each band is then audited independently. This is logically
// safe: proving descent for every member of every disjoint cylinder band proves
// descent for their union; cross-band deduplication is not required.
//
// Within one band the current ordinary-target set is represented exactly as:
//   * non-singleton arithmetic progressions, unioned only on identical
//     (step, residue mod step) grids with overlapping/adjacent parameter ranges;
//   * singleton ordinary integers, deduplicated by value.
//
// One shortcut step performs exact floor trimming, parity splitting, affine
// image propagation, same-grid interval union, and singleton deduplication.
// No density or probabilistic inference is used.
//
// unsigned __int128 arithmetic is guarded against overflow.
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
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

static void uniq(std::vector<u128>& v) {
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
}

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
        out.push_back({add_checked(r, mul_checked(b, lo)), b, u64(width)});
        i = j;
    }
    return out;
}

struct State {
    std::vector<AP> ap;
    std::vector<u128> singletons;
};

static State normalize(std::vector<AP> raw) {
    State s;
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

static State advance(const State& s) {
    std::vector<u128> next_singletons;
    next_singletons.reserve(s.singletons.size() + s.ap.size());
    std::vector<AP> next_ap;
    next_ap.reserve(s.ap.size() * 2);

    for (u128 n : s.singletons) {
        if (n <= LO) continue;
        u128 z = ((n & 1) == 0)
            ? n / 2
            : add_checked(mul_checked(3, n), 1) / 2;
        if (z > LO) next_singletons.push_back(z);
    }

    for (auto x : s.ap) {
        assert(x.m >= 2 && (x.b & 1));

        // b>0, so values <=LO form an initial parameter interval.
        if (x.a <= LO) {
            u128 t = (LO - x.a) / x.b;
            if (t >= u128(x.m - 1)) continue;
            u64 drop = u64(t + 1);
            x.a = add_checked(x.a, mul_checked(x.b, drop));
            x.m -= drop;
        }

        // Since b is odd, k parity fixes value parity.
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
    State out;
    out.singletons = std::move(next_singletons);
    out.ap = merge_multi(next_ap);
    return out;
}

static u128 represented_occurrences(const State& s) {
    u128 n = s.singletons.size();
    for (const auto& x : s.ap) n += x.m;
    return n;
}

struct ExpectedBand {
    u64 lo, hi;
    u64 raw_cylinders;
    u128 raw_occurrences;
    u64 initial_ap;
    u64 initial_singletons;
    u128 initial_occurrences;
    int closure_sweep_bound;
};

static const std::vector<ExpectedBand> EXPECTED = {
    {1,3,1610075,u128(2385287),388307,564293,u128(1579340),251},
    {4,7,195529,u128(951393),174228,0,u128(856061),274},
    {8,11,261635,u128(2286562),202707,0,u128(1797291),252},
    {12,15,111601,u128(1578082),98954,0,u128(1410291),282},
    {16,23,32544,u128(743502),25830,0,u128(597225),218},
    {24,31,154683,u128(4094694),121209,0,u128(3260663),270},
    {32,47,87913,u128(3726570),78339,0,u128(3345438),325},
    {48,63,0,u128(0),0,0,u128(0),0},
    {64,95,149070,u128(11547278),118961,0,u128(9346190),305},
    {96,127,23922,u128(2912706),21490,0,u128(2630082),325},
    {128,191,24992,u128(3329867),22320,0,u128(3002765),296},
    {192,255,76383,u128(17347622),63491,0,u128(14594541),291},
    {256,383,27427,u128(8684307),23736,0,u128(7666847),325},
    {384,511,14260,u128(5703980),12995,0,u128(5239368),306},
    {512,767,53583,u128(36249397),45250,0,u128(30945743),394},
    {768,1023,6676,u128(5236775),5584,0,u128(4434673),270},
    {1024,1535,17891,u128(20885004),16365,0,u128(19243766),344},
    {1536,2047,14866,u128(28615626),13153,0,u128(25507477),376},
    {2048,3071,17829,u128(39624574),15132,0,u128(34081764),318},
    {3072,4095,8403,u128(29496139),7851,0,u128(27713043),373},
    {4096,6143,8646,u128(49603126),7810,0,u128(45078617),329},
    {6144,8191,7895,u128(52594388),7000,0,u128(47099133),393},
    {8192,12287,5430,u128(57257240),5147,0,u128(54518972),373},
    {12288,16383,0,u128(0),0,0,u128(0),0},
    {16384,24575,8963,u128(169713284),8145,0,u128(155291953),393},
    {24576,32767,1515,u128(47152465),1441,0,u128(45000947),341},
    {32768,65535,3619,u128(194915650),3440,0,u128(185550916),373},
    {65536,131071,757,u128(71540502),740,0,u128(70064130),400},
    {131072,262143,1700,u128(286466944),1630,0,u128(275513033),443},
    {262144,524287,548,u128(224156149),543,0,u128(222277646),372},
    {524288,1048575,136,u128(89476178),134,0,u128(88432433),332},
    {1048576,4194303,157,u128(259265611),156,0,u128(257910207),438},
    {4194304,16777215,21,u128(108239377),21,0,u128(108239377),389},
};

static void audit_band(std::vector<AP> raw, const ExpectedBand& e) {
    assert(raw.size() == e.raw_cylinders);
    u128 raw_occ = 0;
    for (const auto& x : raw) raw_occ += x.m;
    assert(raw_occ == e.raw_occurrences);

    if (raw.empty()) {
        assert(e.initial_ap == 0 && e.initial_singletons == 0 &&
               e.initial_occurrences == 0 && e.closure_sweep_bound == 0);
        return;
    }

    State s = normalize(std::move(raw));
    assert(s.ap.size() == e.initial_ap);
    assert(s.singletons.size() == e.initial_singletons);
    assert(represented_occurrences(s) == e.initial_occurrences);

    int closed_at = -1;
    for (int depth = 1; depth <= e.closure_sweep_bound; ++depth) {
        s = advance(s);
        if (s.ap.empty() && s.singletons.empty()) {
            closed_at = depth;
            break;
        }
    }
    assert(closed_at == e.closure_sweep_bound);

    std::cerr << "closed [" << e.lo << "," << e.hi << "]"
              << " raw_cylinders=" << e.raw_cylinders
              << " raw_occurrences=" << str128(e.raw_occurrences)
              << " initial_union_occurrences=" << str128(e.initial_occurrences)
              << " sweep_bound=" << closed_at << "\n";
}

int main() {
    std::vector<std::vector<AP>> buckets(EXPECTED.size());
    std::string a_s, b_s;
    u64 m;
    u64 total_cylinders = 0;
    u128 total_occurrences = 0;

    while (std::cin >> a_s >> b_s >> m) {
        AP x{parse128(a_s), parse128(b_s), m};
        bool placed = false;
        for (std::size_t i = 0; i < EXPECTED.size(); ++i) {
            if (EXPECTED[i].lo <= m && m <= EXPECTED[i].hi) {
                buckets[i].push_back(x);
                placed = true;
                break;
            }
        }
        assert(placed);
        ++total_cylinders;
        total_occurrences += m;
    }

    assert(total_cylinders == 2'928'669);
    assert(total_occurrences == u128(1'835'780'279));

    // The bands are contiguous and disjoint from m=1 through 2^24-1.
    assert(EXPECTED.front().lo == 1);
    for (std::size_t i = 1; i < EXPECTED.size(); ++i)
        assert(EXPECTED[i - 1].hi + 1 == EXPECTED[i].lo);
    assert(EXPECTED.back().hi == 16'777'215);

    int global_bound = 0;
    for (std::size_t i = 0; i < EXPECTED.size(); ++i) {
        audit_band(std::move(buckets[i]), EXPECTED[i]);
        global_bound = std::max(global_bound, EXPECTED[i].closure_sweep_bound);
    }

    assert(global_bound == 443);
    std::cerr << "PASS MATH-070: complete r=15 layer closed; r>=15 closed; "
              << "certified sweep bound <=443\n";
    return 0;
}
