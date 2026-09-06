// Streaming exact audit for root-11, no-00 target words.
//
// Instead of storing every full-Hensel class, first store only target keys
//   (q, C mod 3^q)
// for root-11/no-00 words, then stream all 2^L binary words and update only
// those target classes.  This reduces memory from O(2^L) class storage to the
// Fibonacci-sized target set.
//
// Exact run status recorded on 2026-09-06:
//   L=27: all target words class-maximal.
//   L=28: all target words class-maximal.
//   L=29: NOT CERTIFIED (the interactive run timed out before completion).
//
// This is FINITE ONLY and is not a proof of the general class-max conjecture.
//
// Build:
//   g++ -O3 -std=c++17 no00_root_hensel_target_stream_certificate.cpp -o audit
// Run:
//   ./audit 28

#include <bits/stdc++.h>
using namespace std;
using u64 = unsigned long long;

struct Key {
    u64 r;
    unsigned q;
    bool operator==(Key const& o) const { return r == o.r && q == o.q; }
};
struct Hash {
    size_t operator()(Key const& k) const {
        return hash<u64>{}(k.r ^ (u64(k.q) * 0x9e3779b97f4a7c15ULL));
    }
};
struct Value {
    u64 targetC;
    u64 maxC;
    u64 targetMask;
    u64 maxMask;
};

int L;
u64 p3[50];
unordered_map<Key,Value,Hash> targets;

void generate_targets(int i, int prev, u64 C, unsigned q, u64 mask) {
    if (i == L) {
        Key k{C % p3[q], q};
        auto it = targets.find(k);
        if (it == targets.end()) {
            targets.emplace(k, Value{C,C,mask,mask});
        } else if (C > it->second.targetC) {
            // Multiple target words in one class would already be interesting;
            // retain the larger target for the max test.
            it->second.targetC = C;
            it->second.targetMask = mask;
            if (C > it->second.maxC) {
                it->second.maxC = C;
                it->second.maxMask = mask;
            }
        }
        return;
    }

    if (i < 2) {
        // Force the COV-1 root parity head 11.
        generate_targets(i + 1, 1, 3 * C + (1ULL << i), q + 1,
                         mask | (1ULL << i));
        return;
    }

    // Append 1.
    generate_targets(i + 1, 1, 3 * C + (1ULL << i), q + 1,
                     mask | (1ULL << i));

    // Append 0 only when it does not create 00.
    if (prev) generate_targets(i + 1, 0, C, q, mask);
}

void scan_all_words(int i, u64 C, unsigned q, u64 mask) {
    if (i == L) {
        if (!q) return;
        Key k{C % p3[q], q};
        auto it = targets.find(k);
        if (it != targets.end() && C > it->second.maxC) {
            it->second.maxC = C;
            it->second.maxMask = mask;
        }
        return;
    }

    scan_all_words(i + 1, C, q, mask);
    scan_all_words(i + 1, 3 * C + (1ULL << i), q + 1,
                   mask | (1ULL << i));
}

string word(u64 mask) {
    string s;
    for (int i = 0; i < L; ++i)
        s.push_back(((mask >> i) & 1ULL) ? '1' : '0');
    return s;
}

int main(int argc, char** argv) {
    L = argc > 1 ? atoi(argv[1]) : 28;
    if (L < 2 || L > 35) return 2;

    p3[0] = 1;
    for (int i = 1; i < 50; ++i) p3[i] = 3 * p3[i - 1];

    targets.reserve(1000000);
    generate_targets(0, 1, 0, 0, 0);
    scan_all_words(0, 0, 0, 0);

    for (auto const& kv : targets) {
        auto const& v = kv.second;
        if (v.maxC > v.targetC) {
            cout << "NONMAX\n";
            cout << "L=" << L << " q=" << kv.first.q << "\n";
            cout << "target=" << word(v.targetMask) << " C=" << v.targetC << "\n";
            cout << "competitor=" << word(v.maxMask) << " C=" << v.maxC << "\n";
            cout << "credit=" << (v.maxC - v.targetC) / p3[kv.first.q] << "\n";
            return 1;
        }
    }

    cout << "PASS L=" << L
         << " target_classes=" << targets.size()
         << " all_root11_no00_targets_class_maximal\n";
    cout << "FINITE ONLY\n";
    return 0;
}
