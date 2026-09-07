// MATH-030: exact cut-depth Pareto audit for the RMAX=1e9 streaming
// bounded-lift tree used by MATH-028/029.
//
// Goal: find the smallest cut that gives enough 16-worker task granularity
// without introducing a single-subtree work bottleneck, while preserving the
// exact bounded-lift tree.  This is a scheduling/memory result only.

#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;

struct S { uint32_t r; u128 y; uint8_t q, k; };
struct Stat {
    unsigned long long attempts = 0;
    unsigned long long leaves = 0;
    size_t max_stack = 0;
};

static const uint64_t RMAX = 1'000'000'000ULL;
int qminv[62];
u128 pow3v[62];

vector<S> expand_one(const vector<S>& f, int k, vector<int>* parent = nullptr) {
    vector<S> n;
    n.reserve(f.size() * 2);
    const uint64_t add = 1ULL << k;
    for (int i = 0; i < static_cast<int>(f.size()); ++i) {
        const auto st = f[i];
        for (int e = 0; e <= 1; ++e) {
            if (e && uint64_t(st.r) + add > RMAX) continue;
            const u128 z = st.y + (e ? pow3v[st.q] : 0);
            const int odd = int(z & 1);
            const int q2 = int(st.q) + odd;
            if (q2 < qminv[k + 1]) continue;
            const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
            const uint32_t r2 = st.r + (e ? static_cast<uint32_t>(add) : 0u);
            n.push_back({r2, y2, uint8_t(q2), uint8_t(k + 1)});
            if (parent) parent->push_back(i);
        }
    }
    return n;
}

Stat subtree_stat(S root) {
    vector<S> stack{root};
    Stat out;
    out.max_stack = 1;

    while (!stack.empty()) {
        const S st = stack.back();
        stack.pop_back();
        if (st.k == 61) {
            ++out.leaves;
            continue;
        }

        const uint64_t add = 1ULL << st.k;
        for (int e = 0; e <= 1; ++e) {
            if (e && uint64_t(st.r) + add > RMAX) continue;
            ++out.attempts;
            const u128 z = st.y + (e ? pow3v[st.q] : 0);
            const int odd = int(z & 1);
            const int q2 = int(st.q) + odd;
            if (q2 < qminv[st.k + 1]) continue;
            const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
            const uint32_t r2 = st.r + (e ? static_cast<uint32_t>(add) : 0u);
            stack.push_back({r2, y2, uint8_t(q2), uint8_t(st.k + 1)});
            out.max_stack = max(out.max_stack, stack.size());
        }
    }
    return out;
}

int main() {
    pow3v[0] = 1;
    for (int i = 1; i < 62; ++i) pow3v[i] = pow3v[i - 1] * 3;

    u128 two = 1, three = 1;
    int q = 0;
    for (int k = 1; k <= 61; ++k) {
        two *= 2;
        while (three < two) { three *= 3; ++q; }
        qminv[k] = q;
    }

    vector<S> f{{0, 0, 0, 0}};
    vector<size_t> count(11);
    count[0] = 1;
    unsigned long long prefix_attempts = 0;

    for (int k = 0; k < 8; ++k) {
        const uint64_t add = 1ULL << k;
        vector<S> n;
        n.reserve(f.size() * 2);
        for (const auto st : f) {
            for (int e = 0; e <= 1; ++e) {
                if (e && uint64_t(st.r) + add > RMAX) continue;
                ++prefix_attempts;
                const u128 z = st.y + (e ? pow3v[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qminv[k + 1]) continue;
                const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
                const uint32_t r2 = st.r + (e ? static_cast<uint32_t>(add) : 0u);
                n.push_back({r2, y2, uint8_t(q2), uint8_t(k + 1)});
            }
        }
        f.swap(n);
        count[k + 1] = f.size();
    }

    assert(f.size() == 19);
    assert(prefix_attempts == 66ULL);

    vector<int> parent9;
    auto f9 = expand_one(f, 8, &parent9);
    prefix_attempts += 38;
    count[9] = f9.size();
    assert(f9.size() == 38);
    assert(prefix_attempts == 104ULL);

    vector<int> parent10;
    auto f10 = expand_one(f9, 9, &parent10);
    prefix_attempts += 76;
    count[10] = f10.size();
    assert(f10.size() == 64);
    assert(prefix_attempts == 180ULL);

    vector<Stat> s10(f10.size());
    unsigned long long tail10 = 0, leaves = 0, max10 = 0;
    size_t max_stack10 = 0;
    for (int i = 0; i < static_cast<int>(f10.size()); ++i) {
        s10[i] = subtree_stat(f10[i]);
        tail10 += s10[i].attempts;
        leaves += s10[i].leaves;
        max10 = max(max10, s10[i].attempts);
        max_stack10 = max(max_stack10, s10[i].max_stack);
    }

    assert(tail10 == 187'063'811ULL);
    assert(leaves == 1'796'718ULL);
    assert(max10 == 10'943'447ULL);
    assert(max_stack10 == 20);

    // Aggregate cut-10 subtrees into their cut-9 parents, including the
    // attempted step-10 branches themselves.
    vector<unsigned long long> work9(f9.size(), 0);
    for (int i = 0; i < static_cast<int>(f10.size()); ++i)
        work9[parent10[i]] += s10[i].attempts;
    for (int i = 0; i < static_cast<int>(f9.size()); ++i) {
        const uint64_t add = 1ULL << 9;
        for (int e = 0; e <= 1; ++e)
            if (!(e && uint64_t(f9[i].r) + add > RMAX)) ++work9[i];
    }
    const auto max9 = *max_element(work9.begin(), work9.end());
    assert(max9 == 17'725'864ULL);

    // Aggregate again to cut 8.
    vector<unsigned long long> work8(f.size(), 0);
    for (int i = 0; i < static_cast<int>(f9.size()); ++i)
        work8[parent9[i]] += work9[i];
    for (int i = 0; i < static_cast<int>(f.size()); ++i) {
        const uint64_t add = 1ULL << 8;
        for (int e = 0; e <= 1; ++e)
            if (!(e && uint64_t(f[i].r) + add > RMAX)) ++work8[i];
    }
    const auto max8 = *max_element(work8.begin(), work8.end());
    assert(max8 == 27'928'598ULL);

    const long double ideal16 = static_cast<long double>(tail10) / 16.0L;
    assert(static_cast<long double>(max8) > ideal16);
    assert(static_cast<long double>(max9) > ideal16);
    assert(static_cast<long double>(max10) < ideal16);

    // Cuts 0..7 do not even expose 16 tasks.
    for (int k = 0; k <= 7; ++k) assert(count[k] < 16);

    // Thus cut 10 is the first audited cut that both supplies >=16 tasks and
    // has no individual tail subtree larger than the ideal total-tail/16 load.
    const unsigned long long live16 = 64ULL + 16ULL * max_stack10;
    assert(live16 == 384ULL);

    assert(prefix_attempts + tail10 == 187'063'991ULL);

    cout << "PASS\n";
    cout << "cut8 tasks=19 max_subtree=" << max8 << "\n";
    cout << "cut9 tasks=38 max_subtree=" << max9 << "\n";
    cout << "cut10 tasks=64 max_subtree=" << max10 << "\n";
    cout << "ideal tail work per 16=" << static_cast<unsigned long long>(ideal16)
         << " + fraction\n";
    cout << "cut10 max_stack=" << max_stack10 << " live16=" << live16 << "\n";
    cout << "total branch attempts=" << prefix_attempts + tail10
         << " leaves=" << leaves << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
