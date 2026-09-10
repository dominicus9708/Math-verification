// MATH-051 fixed-d exact finite-state dominated-word counter.
//
// Purpose
// -------
// Replace large fixed-depth parity-word enumeration by the exact fixed-d
// signature / bounded-carry automaton derived after MATH-050.
//
// For a length-k word with d even positions e_j and q=k-d,
//
//   Sigma_d(E) = sum_j 3^j (2/3)^e_j
//              = sum_j 2^j (2/3)^G_j,  G_j=e_j-j.
//
// Two fixed-(k,d) words are in the same exact Hensel class iff their Sigma
// difference is an integer. A positive integer difference is exactly the
// Hensel translation credit. Grouping equal G levels gives the carry rule
//
//   h_{r-1} = 2(h_r + Delta a_r)/3,
//
// with divisibility by 3 required at every level.
//
// This program counts D(k,d): coefficient-valid words that are terminally
// dominated in their exact Hensel class. Candidate histories with identical
// future competitor/carry subsets are merged.
//
// Exact viability pruning
// -----------------------
// A primitive competitor state (rem,na,nb,h) is discarded only when no
// completion of the remaining gap levels can possibly end with positive exact
// credit. `can()` computes this existential property recursively and memoizes
// it. `upper_possible()` is only a necessary upper bound used before that
// exact recursion; it never discards a potentially positive completion.
//
// The primitive new-loss count is recovered by downstream-stable dominance:
//
//   R(k,d) = D(k,d) - D(k-1,d) - D(k-1,d-1).
//
// Audited scope for MATH-051: k<=41, d<=15. Finite exact computation only.
// Collatz conjecture remains OPEN.
//
// Build:
//   g++ -O3 -std=c++20 -march=native file.cpp -o cert
// Usage:
//   ./cert K D [verbose]

#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using i128 = __int128_t;

static i128 P3[64], P2[64];

static inline int blocksum(int n, int l) {
    return l ? (((1 << l) - 1) << (n - l)) : 0;
}

struct Key {
    uint8_t na;
    vector<uint32_t> S;
    bool operator==(Key const& o) const noexcept {
        return na == o.na && S == o.S;
    }
};

struct KeyHash {
    size_t operator()(Key const& k) const noexcept {
        uint64_t h = 0x9e3779b97f4a7c15ULL ^ k.na;
        for (uint32_t x : k.S) {
            uint64_t z = x + 0x9e3779b97f4a7c15ULL;
            z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
            z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
            z ^= z >> 31;
            h ^= z + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
        }
        return (size_t)h;
    }
};

// For d<=15 the audited carry bound is far below this packing range.
static constexpr int HB = 1 << 20;

static inline uint32_t enc(int nb, int h) {
    int v = h + HB;
    if (v < 0 || v >= (1 << 21)) abort();
    return ((uint32_t)nb << 21) | (uint32_t)v;
}

static inline void dec(uint32_t x, int& nb, int& h) {
    nb = (int)(x >> 21);
    h = (int)(x & ((1u << 21) - 1)) - HB;
}

struct Solver {
    int d;
    vector<int> L;
    unordered_map<uint64_t, uint8_t> memo;

    explicit Solver(int D) : d(D) {
        // Rank-j candidate even at gap G is coefficient-valid exactly when
        // 3^G > 2^(G+j+1). L[j] is the least allowed G.
        L.resize(d);
        for (int j = 0; j < d; ++j) {
            int G = 0;
            while (P3[G] <= P2[G + j + 1]) ++G;
            L[j] = G;
        }
        memo.reserve(1 << 20);
    }

    // Necessary upper bound for existence of any positive completion.
    // Put all remaining competitor ranks at gap 0 (largest contribution) and
    // all remaining candidate ranks at gap rem (smallest contribution).
    inline bool upper_possible(int rem, int na, int nb, int h) const {
        if (na && L[na - 1] > rem) return false;
        i128 lhs = (i128)(h - ((1 << na) - 1)) * P2[rem]
                 + (i128)((1 << nb) - 1) * P3[rem];
        return lhs > 0;
    }

    uint64_t memo_key(int rem, int na, int nb, int h) const {
        uint64_t v = (uint32_t)(h + HB);
        return v
             | ((uint64_t)nb << 21)
             | ((uint64_t)na << 26)
             | ((uint64_t)rem << 31);
    }

    // Exact existential viability of a primitive competitor state.
    bool can(int rem, int na, int nb, int h) {
        if (!upper_possible(rem, na, nb, h)) return false;

        if (rem == 0) {
            if (na) {
                for (int j = 0; j < na; ++j)
                    if (L[j] > 0) return false;
            }
            long long credit = (long long)((1 << nb) - 1)
                             - ((1 << na) - 1) + h;
            return credit > 0;
        }

        uint64_t key = memo_key(rem, na, nb, h);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;

        bool ok = false;
        for (int la = 0; la <= na && !ok; ++la) {
            bool valid = true;
            for (int j = na - la; j < na; ++j) {
                if (rem < L[j]) { valid = false; break; }
            }
            if (!valid) continue;

            int na2 = na - la;
            if (na2 && L[na2 - 1] > rem - 1) continue;

            int aa = blocksum(na, la);
            for (int lb = 0; lb <= nb; ++lb) {
                int bb = blocksum(nb, lb);
                int z = h + bb - aa;
                if (z % 3) continue;
                int h2 = 2 * (z / 3);
                if (can(rem - 1, na2, nb - lb, h2)) {
                    ok = true;
                    break;
                }
            }
        }

        memo.emplace(key, (uint8_t)ok);
        return ok;
    }

    vector<uint32_t> transition(vector<uint32_t> const& S,
                                int na, int la, int rem) {
        int aa = blocksum(na, la);
        int na2 = na - la;
        vector<uint32_t> out;
        out.reserve(S.size() * 2 + 8);

        for (uint32_t packed : S) {
            int nb, h;
            dec(packed, nb, h);
            for (int lb = 0; lb <= nb; ++lb) {
                int bb = blocksum(nb, lb);
                int z = h + bb - aa;
                if (z % 3) continue;
                int h2 = 2 * (z / 3);
                int nb2 = nb - lb;
                if (can(rem, na2, nb2, h2))
                    out.push_back(enc(nb2, h2));
            }
        }

        sort(out.begin(), out.end());
        out.erase(unique(out.begin(), out.end()), out.end());
        if (out.capacity() > out.size() * 2 + 16) {
            vector<uint32_t> compact(out.begin(), out.end());
            return compact;
        }
        return out;
    }

    pair<u64, size_t> run(int k, bool verbose) {
        int M = k - d;
        if (d == 0) return {0, 1};

        unordered_map<Key, u64, KeyHash> dp, nd;
        dp.reserve(1024);
        dp.emplace(Key{(uint8_t)d, {enc(d, 0)}}, 1);
        size_t peak = 1;

        for (int r = M; r >= 1; --r) {
            nd.clear();
            nd.max_load_factor(0.85f);
            nd.reserve(min<size_t>(max<size_t>(1024, dp.size() * 2),
                                   16000000));

            for (auto const& kv : dp) {
                int na = kv.first.na;
                auto const& S = kv.first.S;
                u64 count = kv.second;

                for (int la = 0; la <= na; ++la) {
                    bool valid = true;
                    for (int j = na - la; j < na; ++j) {
                        if (r < L[j]) { valid = false; break; }
                    }
                    if (!valid) continue;

                    int na2 = na - la;
                    if (na2 && L[na2 - 1] > r - 1) continue;

                    auto S2 = transition(S, na, la, r - 1);
                    if (S2.empty()) continue;

                    Key next{(uint8_t)na2, move(S2)};
                    auto it = nd.find(next);
                    if (it == nd.end()) nd.emplace(move(next), count);
                    else it->second += count;
                }
            }

            dp.swap(nd);
            peak = max(peak, dp.size());

            if (verbose) {
                u64 candidate_count = 0, entries = 0;
                for (auto const& x : dp) {
                    candidate_count += x.second;
                    entries += x.first.S.size();
                }
                cerr << "r " << r
                     << " states " << dp.size()
                     << " cand " << candidate_count
                     << " avgS " << (dp.empty() ? 0.0 :
                                      (double)entries / dp.size())
                     << " memo " << memo.size()
                     << " peak " << peak << '\n';
            }
        }

        u64 dominated = 0;
        for (auto const& kv : dp) {
            if (kv.first.na != 0) continue;
            bool found = false;
            for (uint32_t packed : kv.first.S) {
                int nb, h;
                dec(packed, nb, h);
                if (((1 << nb) - 1) + h > 0) {
                    found = true;
                    break;
                }
            }
            if (found) dominated += kv.second;
        }
        return {dominated, peak};
    }
};

int main(int argc, char** argv) {
    P3[0] = P2[0] = 1;
    for (int i = 1; i < 64; ++i) {
        P3[i] = P3[i - 1] * 3;
        P2[i] = P2[i - 1] * 2;
    }

    if (argc < 3) {
        cerr << "usage: cert K D [verbose]\n";
        return 2;
    }

    int k = stoi(argv[1]);
    int d = stoi(argv[2]);
    if (k < 0 || d < 0 || d > k || k > 41 || d > 15) {
        cerr << "audited scope: 0<=D<=15, D<=K<=41\n";
        return 3;
    }

    Solver solver(d);
    auto t0 = chrono::steady_clock::now();
    auto [D, peak] = solver.run(k, argc > 3);
    double sec = chrono::duration<double>(chrono::steady_clock::now()-t0).count();

    cout << "RESULT k " << k
         << " d " << d
         << " q " << (k-d)
         << " D " << D
         << " peak_subset " << peak
         << " viability_memo " << solver.memo.size()
         << " sec " << sec << '\n';
}
