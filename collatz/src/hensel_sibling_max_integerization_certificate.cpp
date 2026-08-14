#include <bits/stdc++.h>
using namespace std;

using u32 = uint32_t;
using u64 = uint64_t;

struct WordInfo {
    u32 mask{};
    int q{};
    u64 R{};
    vector<int> odd_times;
};

struct Key {
    uint8_t q{};
    uint8_t s{};
    u64 residue{};
    bool operator==(const Key& o) const {
        return q == o.q && s == o.s && residue == o.residue;
    }
};

struct KeyHash {
    size_t operator()(const Key& k) const noexcept {
        u64 x = k.residue ^ (u64(k.q) << 57) ^ (u64(k.s) << 51);
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccdULL;
        x ^= x >> 33;
        return static_cast<size_t>(x);
    }
};

static WordInfo make_info(u32 mask, int L) {
    WordInfo w;
    w.mask = mask;
    for (int i = 0; i < L; ++i) {
        if ((mask >> i) & 1U) {
            w.R = 3ULL * w.R + (1ULL << i);
            ++w.q;
            w.odd_times.push_back(i + 1);
        }
    }
    return w;
}

struct Result {
    u64 surviving{};
    u64 removed{};
};

static Result run_depth(int L) {
    if (L > 25) throw runtime_error("reference certificate is audited through L=25");

    const u32 total = 1U << L;
    vector<u64> pow3(L + 2, 1);
    for (int i = 1; i < static_cast<int>(pow3.size()); ++i)
        pow3[i] = 3ULL * pow3[i - 1];

    vector<WordInfo> survivors;

    for (u32 mask = 0; mask < total; ++mask) {
        int q = 0;
        u64 R = 0;
        vector<int> odd;
        bool ok = ((mask & 3U) == 3U);  // common OO core

        for (int i = 0; i < L; ++i) {
            if ((mask >> i) & 1U) {
                R = 3ULL * R + (1ULL << i);
                ++q;
                odd.push_back(i + 1);
            }
            if (pow3[q] < (1ULL << (i + 1))) ok = false;
        }

        if (ok) survivors.push_back({mask, q, R, std::move(odd)});
    }

    // Only maxima for residues actually queried by coefficient survivors
    // are stored.  s=q is a sentinel for the immediate integer-start case.
    unordered_map<Key, u64, KeyHash> maximum;
    maximum.reserve(survivors.size() * 8ULL);

    for (const auto& w : survivors) {
        const int q = w.q;
        const u64 R = w.R;

        maximum.emplace(Key{uint8_t(q), uint8_t(q), R % pow3[q]}, 0);

        for (int s = 1; s < q; ++s) {
            const u64 base = R % pow3[s];
            const u64 digit = (R / pow3[s]) % 3ULL;
            for (u64 a = 0; a < 3; ++a) {
                if (a == digit) continue;
                maximum.emplace(
                    Key{uint8_t(q), uint8_t(s), base + a * pow3[s]}, 0);
            }
        }
    }

    // One pass through alternate words.  This validates the sibling-max
    // theorem directly; a later implementation can replace this final flat
    // pass by the canonical tail-max / max-plus recurrence.
    for (u32 mask = 0; mask < total; ++mask) {
        WordInfo u = make_info(mask, L);
        const int q = u.q;
        if (q == 0) continue;

        auto immediate = maximum.find(
            Key{uint8_t(q), uint8_t(q), u.R % pow3[q]});
        if (immediate != maximum.end() && u.R > immediate->second)
            immediate->second = u.R;

        for (int s = 1; s < q; ++s) {
            const int d = q - s;
            const int td = u.odd_times[d - 1];
            if ((1ULL << td) <= pow3[d]) continue;

            auto it = maximum.find(
                Key{uint8_t(q), uint8_t(s), u.R % pow3[s + 1]});
            if (it != maximum.end() && u.R > it->second)
                it->second = u.R;
        }
    }

    u64 removed = 0;

    for (const auto& w : survivors) {
        bool kill = false;
        const int q = w.q;
        const u64 R = w.R;

        auto immediate = maximum.find(
            Key{uint8_t(q), uint8_t(q), R % pow3[q]});
        if (immediate != maximum.end() && immediate->second > R)
            kill = true;

        for (int s = 1; s < q && !kill; ++s) {
            const u64 base = R % pow3[s];
            const u64 digit = (R / pow3[s]) % 3ULL;

            for (u64 a = 0; a < 3; ++a) {
                if (a == digit) continue;
                auto it = maximum.find(
                    Key{uint8_t(q), uint8_t(s), base + a * pow3[s]});
                if (it != maximum.end() && it->second > R) {
                    kill = true;
                    break;
                }
            }
        }

        if (kill) ++removed;
    }

    return {static_cast<u64>(survivors.size()), removed};
}

int main() {
    const map<int, Result> expected = {
        {20, {27328, 11458}},
        {21, {46611, 18464}},
        {22, {93222, 41046}},
        {23, {168807, 70829}},
        {24, {286581, 113713}},
        {25, {573162, 251141}},
    };

    cout << "L surviving removed retained removed_fraction\n";
    for (const auto& [L, exp] : expected) {
        Result got = run_depth(L);
        if (got.surviving != exp.surviving || got.removed != exp.removed) {
            cerr << "certificate mismatch at L=" << L << '\n';
            return 1;
        }
        cout << L << ' '
             << got.surviving << ' '
             << got.removed << ' '
             << got.surviving - got.removed << ' '
             << setprecision(15)
             << static_cast<long double>(got.removed) /
                    static_cast<long double>(got.surviving)
             << '\n';
    }
    return 0;
}
