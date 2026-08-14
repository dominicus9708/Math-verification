#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using u32 = uint32_t;

// Exact q-slice builder for the depth-28 Hensel retained residue set.
// Run once for each q=18,...,28 and union the emitted uint32 residue files.
// The q-slices are disjoint because one dyadic start residue determines one
// unique length-28 parity word and hence one final odd count.

struct W { u64 R; int q; };
struct Key {
    uint8_t s;
    u64 r;
    bool operator==(Key const& o) const { return s == o.s && r == o.r; }
};
struct KH {
    size_t operator()(Key const& k) const noexcept {
        u64 x = k.r ^ (u64(k.s) << 56);
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccdULL;
        x ^= x >> 33;
        return size_t(x);
    }
};

static constexpr int L = 28;
vector<u64> P3;
int target_q;

void generate_survivors(int pos, int q, u64 R, vector<W>& out) {
    if (q > target_q || q + (L - pos) < target_q) return;
    if (pos == L) {
        if (q == target_q) out.push_back({R, q});
        return;
    }

    if (P3[q] >= (1ULL << (pos + 1)))
        generate_survivors(pos + 1, q, R, out);

    const u64 R1 = 3 * R + (1ULL << pos);
    if (P3[q + 1] >= (1ULL << (pos + 1)))
        generate_survivors(pos + 1, q + 1, R1, out);
}

u64 correction(const vector<int>& p) {
    u64 R = 0;
    for (int x : p) R = 3 * R + (1ULL << x);
    return R;
}

void enumerate_later(int start, int need, vector<int>& p, int s,
                     unordered_map<Key, u64, KH>& maximum) {
    if (!need) {
        const u64 R = correction(p);
        auto it = maximum.find(Key{uint8_t(s), R % P3[s + 1]});
        if (it != maximum.end() && R > it->second) it->second = R;
        return;
    }
    for (int x = start; x <= L - need; ++x) {
        p.push_back(x);
        enumerate_later(x + 1, need - 1, p, s, maximum);
        p.pop_back();
    }
}

void enumerate_q(int start, int need, vector<int>& p,
                 unordered_map<u64, u64>& immediate) {
    if (!need) {
        const u64 R = correction(p);
        auto it = immediate.find(R % P3[target_q]);
        if (it != immediate.end() && R > it->second) it->second = R;
        return;
    }
    for (int x = start; x <= L - need; ++x) {
        p.push_back(x);
        enumerate_q(x + 1, need - 1, p, immediate);
        p.pop_back();
    }
}

u64 inverse_odd(u64 a) {
    u64 x = 1;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: depth28_hensel_retained_residue_qslice <q> <out.bin>\n";
        return 1;
    }
    target_q = stoi(argv[1]);
    if (target_q < 18 || target_q > 28) return 2;
    const string output = argv[2];

    P3.assign(L + 2, 1);
    for (int i = 1; i < int(P3.size()); ++i) P3[i] = 3 * P3[i - 1];

    vector<W> survivors;
    // common OO core: first two time-expanded parity bits are 11,
    // correction after those two odd steps is 5.
    generate_survivors(2, 2, 5, survivors);

    unordered_map<Key, u64, KH> partial;
    unordered_map<u64, u64> immediate;
    partial.reserve(survivors.size() * 8ULL + 100);
    immediate.reserve(survivors.size() * 2ULL + 100);

    for (auto const& w : survivors) {
        immediate.emplace(w.R % P3[target_q], 0);
        for (int s = 1; s < target_q; ++s) {
            const u64 base = w.R % P3[s];
            const u64 digit = (w.R / P3[s]) % 3;
            for (u64 a = 0; a < 3; ++a)
                if (a != digit)
                    partial.emplace(Key{uint8_t(s), base + a * P3[s]}, 0);
        }
    }

    for (int s = 1; s < target_q; ++s) {
        const int d = target_q - s;
        int pmin = d - 1;
        while (pmin < L && (1ULL << (pmin + 1)) <= P3[d]) ++pmin;

        for (int pd = pmin; pd <= L - 1 - s; ++pd) {
            const int first = pd - d + 1;
            if (first < 0) continue;
            vector<int> p;
            for (int x = first; x <= pd; ++x) p.push_back(x);
            enumerate_later(pd + 1, s, p, s, partial);
        }
    }

    vector<int> p;
    enumerate_q(0, target_q, p, immediate);

    const u64 mask = (1ULL << L) - 1;
    const u64 inv = inverse_odd(P3[target_q]) & mask;
    vector<u32> retained;
    retained.reserve(survivors.size());

    for (auto const& w : survivors) {
        bool kill = false;
        for (int s = 1; s < target_q && !kill; ++s) {
            const u64 base = w.R % P3[s];
            const u64 digit = (w.R / P3[s]) % 3;
            for (u64 a = 0; a < 3; ++a) {
                if (a == digit) continue;
                auto it = partial.find(Key{uint8_t(s), base + a * P3[s]});
                if (it != partial.end() && it->second > w.R) {
                    kill = true;
                    break;
                }
            }
        }
        auto it = immediate.find(w.R % P3[target_q]);
        if (it != immediate.end() && it->second > w.R) kill = true;

        if (!kill) retained.push_back(u32((-inv * w.R) & mask));
    }

    sort(retained.begin(), retained.end());
    retained.erase(unique(retained.begin(), retained.end()), retained.end());

    ofstream f(output, ios::binary);
    f.write(reinterpret_cast<const char*>(retained.data()), retained.size() * sizeof(u32));
    if (!f) return 3;

    cout << target_q << ' ' << survivors.size() << ' ' << retained.size() << '\n';
    return 0;
}
