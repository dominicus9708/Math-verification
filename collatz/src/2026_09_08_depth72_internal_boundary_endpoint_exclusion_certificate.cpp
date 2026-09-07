// MATH-015: exact internal-boundary endpoint exclusion through depth 72.
//
// Build:
//   g++ -O3 -std=c++17 2026_09_08_depth72_internal_boundary_endpoint_exclusion_certificate.cpp -o audit
//
// This is a finite exact certificate for the current first-cell 61+11 window.
// It does NOT prove the Collatz conjecture and does not extrapolate beyond depth 72.

#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

static int MINQ[73];

static int min_q_survival(int k) {
    u128 p3 = 1;
    u128 p2 = ((u128)1) << k;
    int q = 0;
    while (p3 < p2) {
        p3 *= 3;
        ++q;
    }
    return q;
}

struct State61 {
    u64 offset;
    u128 endpoint;
    uint8_t q;
};

struct U128Hash {
    size_t operator()(u128 x) const noexcept {
        u64 lo = (u64)x;
        u64 hi = (u64)(x >> 64);
        return lo ^ (hi * 0x9e3779b97f4a7c15ULL);
    }
};

static bool universal_spine_61(u64 n, u128 &endpoint, uint8_t &qout) {
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

static bool lifted_tail_11(
    u128 base_endpoint,
    int q61,
    int address,
    const u128 *p3,
    u128 &endpoint72,
    uint8_t &q72
) {
    // For N = address*2^61 + x,
    // T^61(N) = T^61(x) + address*3^q61.
    u128 x = base_endpoint + (u128)address * p3[q61];
    int q = q61;
    for (int j = 1; j <= 11; ++j) {
        int b = (int)(x & 1);
        q += b;
        if (q < MINQ[61 + j]) return false;
        x = b ? ((3 * x + 1) >> 1) : (x >> 1);
    }
    endpoint72 = x;
    q72 = (uint8_t)q;
    return true;
}

int main() {
    for (int k = 1; k <= 72; ++k) MINQ[k] = min_q_survival(k);
    assert(MINQ[61] == 39);
    assert(MINQ[72] == 46);

    u128 p3[73];
    p3[0] = 1;
    for (int i = 1; i <= 72; ++i) p3[i] = p3[i - 1] * 3;

    const u64 W = 1ULL << 61;

    // If two candidate prefixes of length k have the same endpoint, MATH-004
    // supplies the same q.  Their positive ordinary-start displacement d is a
    // same-q correction credit.  Since
    //   d < 2^(k-q) * (1-(2/3)^q) < 2^(k-q),
    // coefficient survival at k=72 (q>=46) implies d <= 2^26-1.
    const u64 D = (1ULL << 26) - 1;
    assert(D == 67'108'863ULL);

    // Around boundary B=b*2^61:
    //   left  N = B-l = (b-1)*2^61 + (2^61-l), 1<=l<=D
    //   right N = B+r = b*2^61 + r,               0<=r<D
    // First 61 parity bits therefore depend only on the local lower residues.
    vector<State61> left, right;
    left.reserve(130000);
    right.reserve(130000);

    for (u64 r = 0; r < D; ++r) {
        u128 y;
        uint8_t q;
        if (universal_spine_61(r, y, q)) right.push_back({r, y, q});
    }
    for (u64 l = 1; l <= D; ++l) {
        u128 y;
        uint8_t q;
        if (universal_spine_61(W - l, y, q)) left.push_back({l, y, q});
    }

    assert(right.size() == 120566);
    assert(left.size() == 120071);

    // Internal boundaries between the 340 blocks are b=1025..1363.
    // An endpoint equality at any earlier depth <=72 would persist to depth72,
    // so it is enough to test exact depth-72 endpoint equality after enforcing
    // universal-spine survival through every intermediate prefix.
    unordered_set<u128, U128Hash> right_endpoints;
    right_endpoints.reserve(250000);

    u64 total_right72 = 0;
    u64 total_left72 = 0;
    u64 boundaries_with_collision = 0;
    u64 left_collision_hits = 0;

    for (int b = 1025; b <= 1363; ++b) {
        right_endpoints.clear();

        for (auto const &s : right) {
            u128 y72;
            uint8_t q72;
            if (!lifted_tail_11(s.endpoint, s.q, b, p3, y72, q72)) continue;
            ++total_right72;
            right_endpoints.insert(y72);
        }

        bool any = false;
        for (auto const &s : left) {
            u128 y72;
            uint8_t q72;
            if (!lifted_tail_11(s.endpoint, s.q, b - 1, p3, y72, q72)) continue;
            ++total_left72;
            if (right_endpoints.find(y72) != right_endpoints.end()) {
                any = true;
                ++left_collision_hits;
            }
        }
        if (any) ++boundaries_with_collision;
    }

    assert(total_right72 == 22'527'308ULL);
    assert(total_left72 == 22'306'426ULL);
    assert(boundaries_with_collision == 0);
    assert(left_collision_hits == 0);

    cout << "PASS\n";
    cout << "qmin(61)=39; qmin(72)=46\n";
    cout << "complete depth-72 displacement halo D=2^26-1=" << D << "\n";
    cout << "lower-61 right survivors in halo=" << right.size() << "\n";
    cout << "lower-61 left survivors in halo=" << left.size() << "\n";
    cout << "339 internal boundaries scanned exactly\n";
    cout << "depth-72 surviving right evaluations=" << total_right72 << "\n";
    cout << "depth-72 surviving left evaluations=" << total_left72 << "\n";
    cout << "cross-boundary endpoint collisions through depth72=0\n";
    cout << "FINITE ONLY / NO COLLATZ CLOSURE CLAIM\n";
}
