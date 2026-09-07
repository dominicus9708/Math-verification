// MATH-017: DSD lift-bit constrained halo generator + depth-78 endpoint audit.
//
// Build:
//   g++ -O3 -std=c++17 -fopenmp 2026_09_08_dsd_liftbit_halo_generator_depth78_certificate.cpp -o audit
//   OMP_NUM_THREADS=4 ./audit
//
// FINITE ONLY.  This certificate does not prove the Collatz conjecture.

#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

static int MINQ[79];
static u128 P3[79];

static int min_q_survival(int k) {
    u128 p3 = 1;
    u128 p2 = ((u128)1) << k;
    int q = 0;
    while (p3 < p2) { p3 *= 3; ++q; }
    return q;
}

struct State61 {
    u64 low;
    u128 endpoint;
    uint8_t q;
};

struct Key {
    u128 endpoint;
    uint8_t q;
};

struct KeyHash {
    size_t operator()(Key const& a) const noexcept {
        u64 lo = (u64)a.endpoint;
        u64 hi = (u64)(a.endpoint >> 64);
        return lo ^ (hi * 0x9e3779b97f4a7c15ULL)
                  ^ ((u64)a.q * 0xbf58476d1ce4e5b9ULL);
    }
};

struct KeyEq {
    bool operator()(Key const& a, Key const& b) const noexcept {
        return a.q == b.q && a.endpoint == b.endpoint;
    }
};

// Generate exactly the lower-61 residues inside a 2^m-1 boundary halo that
// survive the universal-spine coefficient condition through depth 61.
//
// At depth k, adding binary lift bit e changes the current k-step endpoint by
// e*3^q.  Therefore, with current endpoint y and odd count q,
//     z = y + e*3^q,
//     next parity b = z mod 2,
//     y' = T(z), q' = q+b.
//
// For the right halo, bits e_m..e_60 are fixed to 0.
// For the left halo residue x=2^61-l, bits e_m..e_60 are fixed to 1.
static vector<State61> generate_halo_states(int m, bool left) {
    vector<State61> cur, next;
    cur.push_back({0, 0, 0});

    for (int k = 0; k < 61; ++k) {
        next.clear();
        next.reserve(k < m ? cur.size() * 2 : cur.size());

        for (auto const& s : cur) {
            int e0 = (k < m ? 0 : (left ? 1 : 0));
            int e1 = (k < m ? 1 : e0);

            for (int e = e0; e <= e1; ++e) {
                u128 z = s.endpoint + (e ? P3[s.q] : 0);
                int b = (int)(z & 1);
                int q2 = s.q + b;
                if (q2 < MINQ[k + 1]) continue;

                u128 y2 = b ? ((3 * z + 1) >> 1) : (z >> 1);
                u64 low2 = s.low;
                if (k < m && e) low2 |= (1ULL << k);
                next.push_back({low2, y2, (uint8_t)q2});
            }
        }
        cur.swap(next);
    }

    const u64 mask = (1ULL << m) - 1;
    vector<State61> out;
    out.reserve(cur.size());

    for (auto const& s : cur) {
        // Right range: 0 <= r < 2^m-1, so exclude r=2^m-1.
        if (!left && s.low == mask) continue;

        // Left range: x=2^61-l with 1<=l<=2^m-1.  The low-m word is
        // 2^m-l and is therefore nonzero.
        if (left && s.low == 0) continue;
        out.push_back(s);
    }
    return out;
}

static inline bool propagate_tail_17(
    u128 endpoint61,
    int q61,
    int address,
    u128& endpoint78,
    uint8_t& q78
) {
    u128 x = endpoint61 + (u128)address * P3[q61];
    int q = q61;

    for (int j = 1; j <= 17; ++j) {
        int b = (int)(x & 1);
        q += b;
        if (q < MINQ[61 + j]) return false;
        x = b ? ((3 * x + 1) >> 1) : (x >> 1);
    }

    endpoint78 = x;
    q78 = (uint8_t)q;
    return true;
}

int main() {
    for (int k = 1; k <= 78; ++k) MINQ[k] = min_q_survival(k);
    P3[0] = 1;
    for (int i = 1; i <= 78; ++i) P3[i] = P3[i - 1] * 3;

    assert(MINQ[78] == 50);

    // At depth78, same-endpoint candidate displacement is bounded by
    // d < 2^(78-q), and coefficient survival gives q>=50.
    const int m = 28;
    const u64 D = (1ULL << m) - 1;
    assert(D == 268'435'455ULL);

    auto right = generate_halo_states(m, false);
    auto left  = generate_halo_states(m, true);

    assert(right.size() == 481570);
    assert(left.size() == 481645);

    unordered_set<Key, KeyHash, KeyEq> right_endpoints;

    unsigned long long total_right78 = 0;
    unsigned long long total_left78 = 0;
    unsigned long long hits = 0;
    int boundaries_with_collision = 0;

    #pragma omp parallel for schedule(dynamic,1) reduction(+:total_right78,total_left78,hits,boundaries_with_collision)
    for (int b = 1025; b <= 1363; ++b) {
        unordered_set<Key, KeyHash, KeyEq> local_right;
        local_right.reserve(700000);

        unsigned long long rcount = 0;
        unsigned long long lcount = 0;
        unsigned long long local_hits = 0;
        bool any = false;

        for (auto const& s : right) {
            u128 y78;
            uint8_t q78;
            if (!propagate_tail_17(s.endpoint, s.q, b, y78, q78)) continue;
            ++rcount;
            local_right.insert(Key{y78, q78});
        }

        for (auto const& s : left) {
            u128 y78;
            uint8_t q78;
            if (!propagate_tail_17(s.endpoint, s.q, b - 1, y78, q78)) continue;
            ++lcount;
            if (local_right.find(Key{y78, q78}) != local_right.end()) {
                ++local_hits;
                any = true;
            }
        }

        total_right78 += rcount;
        total_left78 += lcount;
        hits += local_hits;
        if (any) ++boundaries_with_collision;
    }

    assert(total_right78 == 64'370'400ULL);
    assert(total_left78 == 64'259'236ULL);
    assert(hits == 0);
    assert(boundaries_with_collision == 0);

    cout << "PASS\n";
    cout << "qmin(78)=50\n";
    cout << "complete depth-78 halo D=2^28-1=" << D << "\n";
    cout << "generated right lower-61 states=" << right.size() << "\n";
    cout << "generated left lower-61 states=" << left.size() << "\n";
    cout << "depth-78 surviving right evaluations=" << total_right78 << "\n";
    cout << "depth-78 surviving left evaluations=" << total_left78 << "\n";
    cout << "339 internal boundaries scanned\n";
    cout << "cross-boundary endpoint collisions through depth78=0\n";
    cout << "FINITE ONLY / NO COLLATZ CLOSURE CLAIM\n";
}
