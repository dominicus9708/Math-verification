// MATH-108 executable gate B: region-independent exact AP-union engine.
//
// This is the MATH-071 exact AP propagation core with the five hard-coded
// r=14 multiplicity regions removed from the ingestion layer.
//
// Input rows:
//   target0<TAB>odd_step<TAB>count
//
// Arguments:
//   expected_cylinders expected_occurrences [source_chunk]
//
// Every source record is assigned to exactly one initial chunk.  If an exact
// state exceeds STATE_CAP, the ORIGINAL source-record list is bisected and
// both halves are audited.  If one source AP alone is too large, its parameter
// interval is bisected exactly.  These are set identities, not pruning.
//
// This executable is a representation/regression gate.  A successful r=14
// regression is required before any r=13 run may be promoted to a closure
// claim.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;

static const cpp_int LO = cpp_int(1) << 71;
static const std::size_t STATE_CAP = 1'000'000;
static const int MAX_DEPTH = 1000;

struct AP { cpp_int a, b; u64 m; };
struct Interval { cpp_int b, r, k0, k1; };
struct State { std::vector<AP> ap; std::vector<cpp_int> singletons; };
struct TooBig {};

struct Stats {
    u64 source_parts = 0;
    u64 closure_leaves = 0;
    u64 resource_splits = 0;
    int max_depth = 0;
    std::size_t max_state = 0;
};

static cpp_int parse_big(const std::string& s) {
    cpp_int x = 0;
    for (char c : s) {
        if (c < '0' || c > '9') throw std::runtime_error("non-decimal integer");
        x *= 10;
        x += unsigned(c - '0');
    }
    return x;
}

static u64 parse_u64(const char* s) {
    std::string t(s);
    cpp_int x = parse_big(t);
    if (x < 0 || x > std::numeric_limits<u64>::max())
        throw std::runtime_error("u64 argument overflow");
    return x.convert_to<u64>();
}

static void uniq(std::vector<cpp_int>& v) {
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
}

static std::vector<AP> merge_multi(const std::vector<AP>& input) {
    if (input.size() > STATE_CAP) throw TooBig{};
    std::vector<Interval> v;
    v.reserve(input.size());
    for (const auto& x : input) {
        assert(x.m >= 2 && x.b > 0 && (x.b & 1) != 0);
        cpp_int r = x.a % x.b;
        cpp_int k0 = (x.a - r) / x.b;
        cpp_int k1 = k0 + (x.m - 1);
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
        cpp_int b = v[i].b, r = v[i].r, lo = v[i].k0, hi = v[i].k1;
        std::size_t j = i + 1;
        while (j < v.size() && v[j].b == b && v[j].r == r &&
               v[j].k0 <= hi + 1) {
            if (v[j].k1 > hi) hi = v[j].k1;
            ++j;
        }
        cpp_int width = hi - lo + 1;
        assert(width <= std::numeric_limits<u64>::max());
        out.push_back({r + b * lo, b, width.convert_to<u64>()});
        i = j;
    }
    return out;
}

static State normalize(const std::vector<AP>& raw) {
    State s;
    std::vector<AP> multi;
    multi.reserve(raw.size());
    for (const auto& x : raw) {
        if (x.m == 1) s.singletons.push_back(x.a);
        else multi.push_back(x);
    }
    uniq(s.singletons);
    s.ap = merge_multi(multi);
    if (s.ap.size() + s.singletons.size() > STATE_CAP) throw TooBig{};
    return s;
}

static State advance(const State& s) {
    if (s.ap.size() + s.singletons.size() > STATE_CAP) throw TooBig{};
    std::vector<cpp_int> next_singletons;
    std::vector<AP> next_ap;
    next_singletons.reserve(std::min(STATE_CAP, s.singletons.size() + s.ap.size()));
    next_ap.reserve(std::min(STATE_CAP, s.ap.size() * 2));

    for (cpp_int n : s.singletons) {
        if (n <= LO) continue;
        cpp_int z;
        if ((n & 1) == 0) z = n / 2;
        else z = (3 * n + 1) / 2;
        if (z > LO) next_singletons.push_back(std::move(z));
        if (next_singletons.size() + next_ap.size() > STATE_CAP) throw TooBig{};
    }

    for (auto x : s.ap) {
        assert(x.m >= 2 && (x.b & 1) != 0);

        if (x.a <= LO) {
            cpp_int t = (LO - x.a) / x.b;
            if (t >= cpp_int(x.m - 1)) continue;
            u64 drop = t.convert_to<u64>() + 1;
            x.a += x.b * drop;
            x.m -= drop;
        }

        for (u64 rho = 0; rho <= 1; ++rho) {
            if (rho >= x.m) continue;
            u64 count = (x.m - 1 - rho) / 2 + 1;
            cpp_int base = x.a + x.b * rho;
            cpp_int a1, b1;
            if ((base & 1) == 0) {
                a1 = base / 2;
                b1 = x.b;
            } else {
                a1 = (3 * base + 1) / 2;
                b1 = 3 * x.b;
            }
            if (count == 1) {
                if (a1 > LO) next_singletons.push_back(std::move(a1));
            } else {
                next_ap.push_back({std::move(a1), std::move(b1), count});
            }
            if (next_singletons.size() + next_ap.size() > STATE_CAP) throw TooBig{};
        }
    }

    uniq(next_singletons);
    State out;
    out.singletons = std::move(next_singletons);
    out.ap = merge_multi(next_ap);
    if (out.ap.size() + out.singletons.size() > STATE_CAP) throw TooBig{};
    return out;
}

static void audit(std::vector<AP> raw, Stats& stats) {
    try {
        State s = normalize(raw);
        stats.max_state = std::max(stats.max_state, s.ap.size() + s.singletons.size());
        for (int depth = 1; depth <= MAX_DEPTH; ++depth) {
            s = advance(s);
            stats.max_state = std::max(stats.max_state, s.ap.size() + s.singletons.size());
            if (s.ap.empty() && s.singletons.empty()) {
                ++stats.closure_leaves;
                stats.source_parts += raw.size();
                stats.max_depth = std::max(stats.max_depth, depth);
                return;
            }
        }
        throw std::runtime_error("depth limit exceeded");
    } catch (const TooBig&) {
        ++stats.resource_splits;
        if (raw.size() > 1) {
            std::size_t mid = raw.size() / 2;
            std::vector<AP> left(raw.begin(), raw.begin() + mid);
            std::vector<AP> right(raw.begin() + mid, raw.end());
            audit(std::move(left), stats);
            audit(std::move(right), stats);
            return;
        }

        AP x = raw.front();
        assert(x.m > 1);
        u64 m1 = x.m / 2;
        u64 m2 = x.m - m1;
        AP y{x.a + x.b * m1, x.b, m2};
        x.m = m1;
        audit(std::vector<AP>{x}, stats);
        audit(std::vector<AP>{y}, stats);
    }
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        std::cerr << "usage: engine expected_cylinders expected_occurrences [source_chunk]\n";
        return 2;
    }

    const u64 expected_cylinders = parse_u64(argv[1]);
    const u64 expected_occurrences = parse_u64(argv[2]);
    const std::size_t source_chunk = argc == 4 ? std::stoull(argv[3]) : 20'000;
    if (source_chunk == 0) throw std::runtime_error("source_chunk must be positive");

    u64 total_cylinders = 0;
    u64 total_occurrences = 0;
    std::vector<AP> chunk;
    chunk.reserve(source_chunk);
    Stats stats;

    std::string a_s, b_s;
    u64 m;
    while (std::cin >> a_s >> b_s >> m) {
        AP x{parse_big(a_s), parse_big(b_s), m};
        assert(x.b > 0 && (x.b & 1) != 0 && x.m > 0);
        ++total_cylinders;
        if (std::numeric_limits<u64>::max() - total_occurrences < m)
            throw std::runtime_error("occurrence total overflow");
        total_occurrences += m;
        chunk.push_back(std::move(x));
        if (chunk.size() == source_chunk) {
            audit(std::move(chunk), stats);
            chunk.clear();
            chunk.reserve(source_chunk);
        }
    }
    if (!chunk.empty()) audit(std::move(chunk), stats);

    assert(total_cylinders == expected_cylinders);
    assert(total_occurrences == expected_occurrences);
    assert(stats.source_parts == total_cylinders);

    std::cerr << "PASS generalized exact AP-union audit"
              << " cylinders=" << total_cylinders
              << " occurrences=" << total_occurrences
              << " closure_leaves=" << stats.closure_leaves
              << " resource_splits=" << stats.resource_splits
              << " max_depth=" << stats.max_depth
              << " max_state=" << stats.max_state
              << " source_chunk=" << source_chunk
              << "\n";
    return 0;
}
