// MATH-042 — exact depth-32 one-sided root-Hensel class-max audit.
//
// Candidate side: coefficient-surviving parity words.
// Competitor side: arbitrary parity words with the same (q, C mod 3^q) class.
//
// MATH-013 downstream dominance implies that a non-maximal prefix cannot
// recover under a common suffix. Therefore, within the audited credit-safe
// range, current-depth unrestricted class-max filtering is equivalent to
// imposing one-sided root-Hensel maximality at every earlier prefix.
//
// Exact result certified here:
//   coefficient-surviving depth-32 words = 41,347,483
//   one-sided Hensel-max survivors       = 33,880,411
//   cumulative Hensel-removed            =  7,467,072
//   newly removed from the depth-31 nested prefilter = 14,001
//
// Build: g++ -O3 -std=c++17 <file> -o m42
// Collatz and the first universal Farey cell remain OPEN.

#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;

static const int QMIN[33] = {
    0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,
    16,16,17,18,18,19,19,20,21
};

static inline u64 mix64(u64 x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

struct FlatMax {
    vector<u64> key, val;
    size_t mask;

    explicit FlatMax(size_t n) {
        size_t cap = 1;
        while (cap < n * 2) cap <<= 1;
        key.assign(cap, UINT64_MAX);
        val.assign(cap, 0);
        mask = cap - 1;
    }

    size_t slot(u64 k) const {
        size_t i = (size_t)mix64(k) & mask;
        while (true) {
            u64 x = key[i];
            if (x == UINT64_MAX || x == k) return i;
            i = (i + 1) & mask;
        }
    }

    void add_key(u64 k) {
        size_t i = slot(k);
        if (key[i] == UINT64_MAX) key[i] = k;
    }

    void update(u64 k, u64 C) {
        size_t i = slot(k);
        if (key[i] == k && C > val[i]) val[i] = C;
    }

    u64 get(u64 k) const {
        size_t i = slot(k);
        return key[i] == k ? val[i] : UINT64_MAX;
    }
};

vector<vector<u64>> candidate(33);

void generate_coefficient_words(int i, int q, u64 C, const u64 p2[33]) {
    if (i == 32) {
        candidate[q].push_back(C);
        return;
    }
    int k = i + 1;
    if (q >= QMIN[k])
        generate_coefficient_words(i + 1, q, C, p2);

    int q1 = q + 1;
    if (q1 >= QMIN[k])
        generate_coefficient_words(i + 1, q1, 3 * C + p2[i], p2);
}

u64 correction_from_zero_mask(uint32_t zmask, const u64 p2[33], const u64 p3[33]) {
    u64 C = 0;
    int start = 0;
    uint32_t z = zmask;
    while (z) {
        int pos = __builtin_ctz(z);
        int run = pos - start;
        if (run)
            C = p3[run] * C + p2[start] * (p3[run] - p2[run]);
        start = pos + 1;
        z &= z - 1;
    }
    int run = 32 - start;
    if (run)
        C = p3[run] * C + p2[start] * (p3[run] - p2[run]);
    return C;
}

template <class F>
void enumerate_zero_masks(int d, F f) {
    if (d == 0) {
        f(0u);
        return;
    }
    u64 comb = (1ULL << d) - 1ULL;
    const u64 limit = 1ULL << 32;
    while (comb < limit) {
        f((uint32_t)comb);
        u64 x = comb & (~comb + 1);
        u64 y = comb + x;
        u64 next = (((comb & ~y) / x) >> 1) | y;
        if (next >= limit) break;
        comb = next;
    }
}

int main() {
    u64 p2[33], p3[33];
    p2[0] = p3[0] = 1;
    for (int i = 1; i <= 32; ++i) {
        p2[i] = p2[i - 1] * 2ULL;
        p3[i] = p3[i - 1] * 3ULL;
    }

    generate_coefficient_words(0, 0, 0, p2);

    const u64 expected_coeff[33] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        13472296ULL,13049303ULL,8422120ULL,4118103ULL,1613495ULL,
        511496ULL,130169ULL,26070ULL,3968ULL,432ULL,30ULL,1ULL
    };

    const u64 expected_survive[33] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        10924522ULL,10653576ULL,6934804ULL,3427766ULL,1360759ULL,
        438144ULL,113563ULL,23221ULL,3620ULL,405ULL,30ULL,1ULL
    };

    u64 coefficient_total = 0;
    for (int q = 21; q <= 32; ++q) {
        assert(candidate[q].size() == expected_coeff[q]);
        coefficient_total += candidate[q].size();
    }
    assert(coefficient_total == 41347483ULL);

    u64 survive_total = 0;
    u64 arbitrary_total = 0;

    for (int q = 32; q >= 21; --q) {
        auto &v = candidate[q];
        const u64 mod = p3[q];
        FlatMax H(v.size());
        for (u64 C : v) H.add_key(C % mod);

        const int d = 32 - q;
        u64 arbitrary_count = 0;
        enumerate_zero_masks(d, [&](uint32_t zmask) {
            u64 C = correction_from_zero_mask(zmask, p2, p3);
            H.update(C % mod, C);
            ++arbitrary_count;
        });

        u64 survive = 0;
        for (u64 C : v) {
            u64 best = H.get(C % mod);
            assert(best != UINT64_MAX && best >= C);
            if (best == C) ++survive;
        }
        assert(survive == expected_survive[q]);
        survive_total += survive;
        arbitrary_total += arbitrary_count;
    }

    assert(survive_total == 33880411ULL);
    assert(coefficient_total - survive_total == 7467072ULL);
    assert(arbitrary_total == 236618693ULL);

    // From MATH-041, 19,347,686 depth-31 nested survivors generate exactly
    // 33,894,412 coefficient-admissible depth-32 children before the new
    // depth-32 Hensel comparison.
    const u64 nested_prefilter = 33894412ULL;
    assert(nested_prefilter - survive_total == 14001ULL);

    cout << "depth32 coefficient = 41347483\n";
    cout << "depth32 one-sided Hensel-max survivors = 33880411\n";
    cout << "depth32 cumulative Hensel-removed = 7467072\n";
    cout << "depth32 newly pruned = 14001\n";
    cout << "arbitrary competitor words examined = 236618693\n";
    cout << "FINITE EXACT; first cell and Collatz remain OPEN.\n";
}
