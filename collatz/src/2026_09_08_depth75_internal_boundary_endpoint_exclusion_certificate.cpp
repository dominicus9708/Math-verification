// MATH-016: exact internal-boundary endpoint exclusion through depth 75.
//
// Build:
//   g++ -O3 -std=c++17 2026_09_08_depth75_internal_boundary_endpoint_exclusion_certificate.cpp -o audit
//
// FINITE ONLY.  No Collatz closure claim.

#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

static int MINQ[76];

static int min_q_survival(int k) {
    u128 p3 = 1;
    u128 p2 = ((u128)1) << k;
    int q = 0;
    while (p3 < p2) { p3 *= 3; ++q; }
    return q;
}

struct State61 {
    u64 offset;
    u128 endpoint;
    uint8_t q;
};

struct Key {
    u128 endpoint;
    uint8_t q;
};

struct KeyHash {
    size_t operator()(Key const& x) const noexcept {
        u64 lo = (u64)x.endpoint;
        u64 hi = (u64)(x.endpoint >> 64);
        return lo ^ (hi * 0x9e3779b97f4a7c15ULL)
                  ^ ((u64)x.q * 0xbf58476d1ce4e5b9ULL);
    }
};

struct KeyEq {
    bool operator()(Key const& a, Key const& b) const noexcept {
        return a.q == b.q && a.endpoint == b.endpoint;
    }
};

static bool universal_spine_61(u64 n, u128& endpoint, uint8_t& qout) {
    u128 x = n;
    int q = 0;
    for (int k = 1; k <= 61; ++k) {
        int b = (int)(x & 1);
        q += b;
        if (q < MINQ[k]) return false;
        x = b ? ((3 * x + 1) >> 1) : (x >> 1);
    }
    endpoint = x;
    qout = (uint8_t)q;
    return true;
}

static bool lifted_tail_14(
    u128 base_endpoint,
    int q61,
    int address,
    const u128* p3,
    u128& endpoint75,
    uint8_t& q75
) {
    u128 x = base_endpoint + (u128)address * p3[q61];
    int q = q61;
    for (int j = 1; j <= 14; ++j) {
        int b = (int)(x & 1);
        q += b;
        if (q < MINQ[61 + j]) return false;
        x = b ? ((3 * x + 1) >> 1) : (x >> 1);
    }
    endpoint75 = x;
    q75 = (uint8_t)q;
    return true;
}

int main() {
    for (int k = 1; k <= 75; ++k) MINQ[k] = min_q_survival(k);
    assert(MINQ[61] == 39);
    assert(MINQ[75] == 48);

    u128 p3[76];
    p3[0] = 1;
    for (int i = 1; i <= 75; ++i) p3[i] = p3[i - 1] * 3;

    const u64 W = 1ULL << 61;

    // MATH-004 gives equal q for same-endpoint candidate states.  At depth75,
    // coefficient survival gives q>=48, hence an integer same-endpoint start
    // displacement satisfies d < 2^(75-q) <= 2^27 and therefore
    // d <= 2^27-1.
    const u64 D = (1ULL << 27) - 1;
    assert(D == 134'217'727ULL);

    vector<State61> left, right;
    left.reserve(250000);
    right.reserve(250000);

    for (u64 r = 0; r < D; ++r) {
        u128 y; uint8_t q;
        if (universal_spine_61(r, y, q)) right.push_back({r, y, q});
    }
    for (u64 l = 1; l <= D; ++l) {
        u128 y; uint8_t q;
        if (universal_spine_61(W - l, y, q)) left.push_back({l, y, q});
    }

    assert(right.size() == 241066);
    assert(left.size() == 240441);

    unordered_set<Key, KeyHash, KeyEq> right_endpoints;
    right_endpoints.reserve(500000);

    u64 total_right75 = 0;
    u64 total_left75 = 0;
    u64 boundaries_with_collision = 0;
    u64 left_collision_hits = 0;

    // 339 internal boundaries between the 340 current top-address blocks.
    for (int b = 1025; b <= 1363; ++b) {
        right_endpoints.clear();

        for (auto const& s : right) {
            u128 y75; uint8_t q75;
            if (!lifted_tail_14(s.endpoint, s.q, b, p3, y75, q75)) continue;
            ++total_right75;
            right_endpoints.insert(Key{y75, q75});
        }

        bool any = false;
        for (auto const& s : left) {
            u128 y75; uint8_t q75;
            if (!lifted_tail_14(s.endpoint, s.q, b - 1, p3, y75, q75)) continue;
            ++total_left75;
            if (right_endpoints.find(Key{y75, q75}) != right_endpoints.end()) {
                any = true;
                ++left_collision_hits;
            }
        }
        if (any) ++boundaries_with_collision;
    }

    assert(total_right75 == 37'619'431ULL);
    assert(total_left75 == 37'318'039ULL);
    assert(boundaries_with_collision == 0);
    assert(left_collision_hits == 0);

    cout << "PASS\n";
    cout << "qmin(75)=48\n";
    cout << "complete depth-75 displacement halo D=2^27-1=" << D << "\n";
    cout << "lower-61 right survivors in halo=" << right.size() << "\n";
    cout << "lower-61 left survivors in halo=" << left.size() << "\n";
    cout << "339 internal boundaries scanned exactly\n";
    cout << "depth-75 surviving right evaluations=" << total_right75 << "\n";
    cout << "depth-75 surviving left evaluations=" << total_left75 << "\n";
    cout << "cross-boundary endpoint collisions through depth75=0\n";
    cout << "FINITE ONLY / NO COLLATZ CLOSURE CLAIM\n";
}
