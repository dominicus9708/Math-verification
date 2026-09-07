// MATH-023: finite aliasing audit for (q61, T^61(r) mod 2^m)
// as a descriptor of max candidate lifespan over the 339 internal boundaries.
//
// Depends on the same finite domain and coefficient gate audited in MATH-022.
// This is a finite output-metric diagnostic, not a full-state quotient theorem.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#ifdef _OPENMP
#include <omp.h>
#endif

using namespace std;
using boost::multiprecision::cpp_int;

struct R61 { int r; cpp_int y; int q; };
struct Stats { long long classes, conflict_classes, conflict_states; int max_values; };

int main() {
    const int RMAX = 10'000'000;
    const int KCAP = 512;

    vector<int> qmin(KCAP + 1);
    cpp_int p3 = 1, two = 1;
    int q = 0;
    for (int k = 1; k <= KCAP; ++k) {
        two *= 2;
        while (p3 < two) { p3 *= 3; ++q; }
        qmin[k] = q;
    }

    vector<cpp_int> pow3(62);
    pow3[0] = 1;
    for (int i = 1; i <= 61; ++i) pow3[i] = pow3[i - 1] * 3;

    vector<R61> survivors;
    survivors.reserve(20'000);
    for (int r = 0; r <= RMAX; ++r) {
        cpp_int n = r;
        int qq = 0;
        bool ok = true;
        for (int k = 1; k <= 61; ++k) {
            const bool odd = (n & 1) != 0;
            if (odd) { n = (3 * n + 1) / 2; ++qq; }
            else n /= 2;
            if (qq < qmin[k]) { ok = false; break; }
        }
        if (ok) survivors.push_back({r, n, qq});
    }
    assert(survivors.size() == 17'745);

    vector<int> life(survivors.size(), 61);
    #pragma omp parallel for schedule(dynamic, 1)
    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        const auto &s = survivors[i];
        int best = 61;
        for (int b = 1025; b <= 1363; ++b) {
            cpp_int n = s.y + cpp_int(b) * pow3[s.q];
            int qq = s.q;
            int L = 61;
            for (int k = 62; k <= KCAP; ++k) {
                const bool odd = (n & 1) != 0;
                if (odd) { n = (3 * n + 1) / 2; ++qq; }
                else n /= 2;
                if (qq < qmin[k]) { L = k - 1; break; }
                L = k;
            }
            best = max(best, L);
        }
        life[i] = best;
    }

    auto audit_m = [&](int m) {
        const uint64_t mask = (uint64_t(1) << m) - 1;
        struct V { int count = 0; set<int> values; };
        unordered_map<uint64_t, V> mp;
        mp.reserve(survivors.size() * 2);
        for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
            const uint64_t phase = static_cast<uint64_t>(survivors[i].y & mask);
            const uint64_t key = (uint64_t(survivors[i].q) << 32) | phase;
            auto &v = mp[key];
            ++v.count;
            v.values.insert(life[i]);
        }
        long long conflict_classes = 0, conflict_states = 0;
        int max_values = 0;
        for (const auto &kv : mp) {
            const auto &v = kv.second;
            max_values = max(max_values, static_cast<int>(v.values.size()));
            if (v.values.size() > 1) {
                ++conflict_classes;
                conflict_states += v.count;
            }
        }
        return Stats{static_cast<long long>(mp.size()), conflict_classes,
                     conflict_states, max_values};
    };

    const map<int, Stats> expected = {
        {11, {8910, 4818, 13605, 8}},
        {20, {17702, 41, 82, 2}},
        {24, {17742, 2, 4, 2}},
        {25, {17743, 1, 2, 2}},
        {26, {17744, 0, 0, 1}},
    };

    for (const auto &[m, ex] : expected) {
        const Stats got = audit_m(m);
        assert(got.classes == ex.classes);
        assert(got.conflict_classes == ex.conflict_classes);
        assert(got.conflict_states == ex.conflict_states);
        assert(got.max_values == ex.max_values);
        cout << "m=" << m
             << " classes=" << got.classes
             << " conflict_classes=" << got.conflict_classes
             << " conflict_states=" << got.conflict_states
             << " max_lifespans_per_class=" << got.max_values << "\n";
    }

    auto find_index = [&](int r) {
        for (int i = 0; i < static_cast<int>(survivors.size()); ++i)
            if (survivors[i].r == r) return i;
        return -1;
    };

    // Exact m=25 ambiguity witness.
    int i1 = find_index(702'631);
    int i2 = find_index(7'066'623);
    assert(i1 >= 0 && i2 >= 0);
    const uint64_t mask25 = (uint64_t(1) << 25) - 1;
    assert(survivors[i1].q == 41 && survivors[i2].q == 41);
    assert(static_cast<uint64_t>(survivors[i1].y & mask25) == 11'114'030);
    assert(static_cast<uint64_t>(survivors[i2].y & mask25) == 11'114'030);
    assert(life[i1] == 210);
    assert(life[i2] == 177);

    // At m=26 the finite lifespan metric has no ambiguity, but there is only
    // one actual merge among 17,745 states, so the compression is negligible.
    int j1 = find_index(311'291);
    int j2 = find_index(311'295);
    assert(j1 >= 0 && j2 >= 0);
    const uint64_t mask26 = (uint64_t(1) << 26) - 1;
    assert(survivors[j1].q == 40 && survivors[j2].q == 40);
    assert(static_cast<uint64_t>(survivors[j1].y & mask26) == 1'641'329);
    assert(static_cast<uint64_t>(survivors[j2].y & mask26) == 1'641'329);
    assert(life[j1] == 171 && life[j2] == 171);

    cout << "m25 witness: q=41 phase=11114030 r=702631 L=210 vs r=7066623 L=177\n";
    cout << "m26 only finite-metric merge witness: q=40 phase=1641329 r=311291/311295 L=171\n";
    cout << "VERDICT: SATURATED / NO MATERIAL COMPRESSION\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
