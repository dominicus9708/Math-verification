// MATH-199 exact finite terminal Pareto-frontier audit.
//
// Enumerates coefficient-valid parity words at a fixed depth K<=30,
// reconstructs the exact correction C and canonical source residue,
// and counts terminal Pareto records under the MATH-197 order.
//
// This is finite computational evidence only. It is NOT a future-complete
// transfer frontier and does not prove a Collatz theorem.
//
// Build:
//   g++ -O3 -std=c++20 file.cpp -o cert
// Usage:
//   ./cert K
//
#include <bits/stdc++.h>
using namespace std;

using u64 = uint64_t;
using u128 = __uint128_t;

struct Point {
    u64 offset;
    u128 C;
};

static string u128_to_string(u128 x) {
    if (!x) return "0";
    string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

static u64 inv_odd_mod_pow2(u64 a, int K) {
    u64 x = 1;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    x &= ((1ULL << K) - 1);
    return x;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: cert K\n";
        return 2;
    }

    const int K = stoi(argv[1]);
    if (K < 1 || K > 30) {
        cerr << "audited implementation scope: 1<=K<=30\n";
        return 3;
    }

    const u64 MOD = 1ULL << K;
    const u64 MASK = MOD - 1;

    vector<u64> p3mod(K + 1, 1), inv(K + 1, 1);
    for (int q = 1; q <= K; ++q)
        p3mod[q] = (p3mod[q - 1] * 3ULL) & MASK;
    for (int q = 0; q <= K; ++q)
        inv[q] = inv_odd_mod_pow2(p3mod[q], K);

    vector<vector<Point>> groups(K + 1);

    function<void(int,int,u128,u128)> dfs =
        [&](int k, int q, u128 C, u128 p3) {
            if (k == K) {
                u64 cmod = (u64)C & MASK;
                u64 a = (u64)(0ULL - cmod * inv[q]) & MASK;

                // B0=2^71 is divisible by 2^K for K<=30.
                // The least N>B0 in residue class a is B0+a for a>0,
                // and B0+2^K for a=0.
                u64 offset = a ? a : MOD;
                groups[q].push_back({offset, C});
                return;
            }

            const int k2 = k + 1;
            const u128 p2 = (u128)1 << k2;

            // even branch
            if (p2 <= p3)
                dfs(k2, q, C, p3);

            // odd branch
            const u128 p3odd = p3 * 3;
            if (p2 <= p3odd)
                dfs(k2, q + 1, 3 * C + ((u128)1 << k), p3odd);
        };

    dfs(0, 0, 0, 1);

    u64 total_words = 0;
    u64 total_frontier = 0;

    for (int q = 0; q <= K; ++q) {
        auto& v = groups[q];
        if (v.empty()) continue;

        total_words += v.size();

        sort(v.begin(), v.end(), [](const Point& a, const Point& b) {
            if (a.offset != b.offset) return a.offset < b.offset;
            return a.C > b.C;
        });

        bool have = false;
        u128 maxC = 0;
        u64 frontier = 0;

        vector<Point> records;

        for (const auto& p : v) {
            if (!have || p.C > maxC) {
                have = true;
                maxC = p.C;
                ++frontier;
                records.push_back(p);
            }
        }

        total_frontier += frontier;

        cout << "K " << K
             << " q " << q
             << " words " << v.size()
             << " pareto " << frontier
             << "\n";

        if (K == 30 && q == 20) {
            for (const auto& p : records) {
                cout << "REC offset " << p.offset
                     << " C " << u128_to_string(p.C)
                     << "\n";
            }
        }
    }

    cout << "TOTAL words " << total_words
         << " pareto " << total_frontier
         << "\n";

    if (K == 28) {
        assert(total_words == 3'524'586ULL);
        assert(total_frontier == 120ULL);
    }
    if (K == 29) {
        assert(total_words == 6'385'637ULL);
        assert(total_frontier == 122ULL);
    }
    if (K == 30) {
        assert(total_words == 12'771'274ULL);
        assert(total_frontier == 141ULL);
    }

    cout << "PASS MATH-199 finite terminal Pareto audit\n";
    return 0;
}
