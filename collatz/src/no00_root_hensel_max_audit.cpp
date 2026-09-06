// Exact finite audit for root-11, no-00 parity words.
//
// Findings certified here:
//   * every root-11/no-00 word is a singleton full-Hensel class through L=23;
//   * singleton status first fails at L=24;
//   * the first displayed collision is
//       w = 110110110101010110110101, q=15,
//       C(w)=74913815,
//       u = 111111111101011000100100,
//       C(u)=17518187,
//       C(w)-C(u)=4*3^15;
//   * despite singleton failure, every root-11/no-00 word remains the maximum
//     correction representative of its full-Hensel class through L=26.
//
// The L<=26 maximality statement is FINITE ONLY.  Do not extrapolate it.
// Build: g++ -O3 -std=c++17 no00_root_hensel_max_audit.cpp -o audit

#include <bits/stdc++.h>
using namespace std;
using u64 = unsigned long long;

struct Key {
    u64 r;
    unsigned q;
    bool operator==(Key const& o) const { return r == o.r && q == o.q; }
};
struct KeyHash {
    size_t operator()(Key const& k) const {
        return std::hash<u64>{}(k.r ^ (u64(k.q) * 0x9e3779b97f4a7c15ULL));
    }
};

u64 p3(unsigned q) {
    u64 x = 1;
    while (q--) x *= 3;
    return x;
}

pair<unsigned,u64> correction(uint32_t mask, int L) {
    unsigned q = 0;
    u64 C = 0;
    for (int i = 0; i < L; ++i) {
        if ((mask >> i) & 1u) {
            C = 3 * C + (1ULL << i);
            ++q;
        }
    }
    return {q, C};
}

bool no00(uint32_t mask, int L) {
    for (int i = 0; i + 1 < L; ++i)
        if (((mask >> i) & 3u) == 0u) return false;
    return true;
}

string word(uint32_t mask, int L) {
    string s;
    for (int i = 0; i < L; ++i) s.push_back(((mask >> i) & 1u) ? '1' : '0');
    return s;
}

void audit_length(int L, bool require_singleton) {
    const uint32_t LIM = 1u << L;
    unordered_map<Key, pair<u64,uint32_t>, KeyHash> best; // max C, multiplicity capped at 2
    best.reserve(LIM / 2);

    for (uint32_t m = 0; m < LIM; ++m) {
        auto [q,C] = correction(m,L);
        if (!q) continue;
        Key k{C % p3(q), q};
        auto it = best.find(k);
        if (it == best.end()) best.emplace(k, make_pair(C,1u));
        else {
            if (C > it->second.first) it->second.first = C;
            if (it->second.second < 2) ++it->second.second;
        }
    }

    size_t targets = 0;
    for (uint32_t m = 0; m < LIM; ++m) {
        if ((m & 3u) != 3u || !no00(m,L)) continue;
        ++targets;
        auto [q,C] = correction(m,L);
        Key k{C % p3(q), q};
        auto const& entry = best.at(k);
        if (C != entry.first) {
            cerr << "NONMAX at L=" << L << " word=" << word(m,L) << "\n";
            exit(2);
        }
        if (require_singleton && entry.second != 1u) {
            cerr << "UNEXPECTED collision before L=24\n";
            exit(3);
        }
    }
    cout << "L=" << L << " root11_no00=" << targets
         << " max=PASS" << (require_singleton ? " singleton=PASS" : "") << "\n";
}

int main(int argc, char** argv) {
    // Cheap exact regression of the singleton range.
    for (int L = 2; L <= 23; ++L) audit_length(L, true);

    // First collision at L=24.
    const int L = 24;
    const uint32_t wmask = 11381467u;
    auto [q,Cw] = correction(wmask,L);
    if (word(wmask,L) != "110110110101010110110101" || q != 15 || Cw != 74913815ULL)
        return 4;

    const string uword = "111111111101011000100100";
    uint32_t umask = 0;
    for (int i = 0; i < L; ++i) if (uword[i] == '1') umask |= (1u << i);
    auto [qu,Cu] = correction(umask,L);
    if (qu != q || Cu != 17518187ULL) return 5;
    if ((Cw - Cu) != 4ULL * p3(q)) return 6;
    if (Cw % p3(q) != Cu % p3(q)) return 7;
    if (!no00(wmask,L) || (wmask & 3u) != 3u) return 8;

    cout << "L=24 first displayed singleton failure verified\n";

    // Full class-max audits.  L=26 may use substantial memory; pass --full26.
    audit_length(24, false);
    audit_length(25, false);
    if (argc > 1 && string(argv[1]) == "--full26") audit_length(26, false);

    cout << "SAFE: singleton conjecture REJECTED at L=24.\n";
    cout << "FINITE ONLY: root11/no00 class-max verified through L=25 by default; L=26 with --full26.\n";
}
