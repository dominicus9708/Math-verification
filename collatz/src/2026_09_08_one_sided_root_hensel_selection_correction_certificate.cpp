// MATH-040: one-sided root-Hensel selection correction.
//
// A minimal-counterexample candidate prefix must satisfy the frozen
// published-floor coefficient gate, but its Hensel competitor is an arbitrary
// parity word of the same length and odd count in the same correction class.
// This certificate audits that asymmetric selection through depth 26.
//
// It also implements an exact targeted reverse-Hensel class oracle: for a
// queried class (k,q,r=C mod 3^q), enumerate only the odd-position tuples in
// that class instead of materializing every arbitrary Hensel class.
//
// Scope: FINITE EXACT.  Collatz remains OPEN.

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using u64 = uint64_t;

static const int QMIN[] = {
    0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,16,16,17
};

struct Candidate { u64 C; uint8_t q; };

struct ReverseHenselOracle {
    int k;
    const vector<u64>& p3;
    const vector<u64>& p2;

    u64 rec(int j, int maxp, u64 r) const {
        if (j == 0) return r == 0 ? 0 : UINT64_MAX;
        u64 best = UINT64_MAX;
        const u64 mod_prev = p3[j-1];
        for (int p = j-1; p < maxp; ++p) {
            if ((r % 3) != (p2[p] % 3)) continue;
            __int128 diff = (__int128)r - (__int128)p2[p];
            assert(diff % 3 == 0);
            __int128 z = diff / 3;
            long long m = (long long)mod_prev;
            long long rprev = m ? (long long)(z % m) : 0;
            if (rprev < 0) rprev += m;
            u64 prev = rec(j-1, p, (u64)rprev);
            if (prev == UINT64_MAX) continue;
            u64 C = 3 * prev + p2[p];
            if (best == UINT64_MAX || C > best) best = C;
        }
        return best;
    }

    u64 best(int q, u64 r) const { return rec(q, k, r); }
};

u64 start_residue(u64 C, int q, int k) {
    u64 p = 1;
    for (int i=0;i<q;++i) p *= 3;
    u64 inv = 1;
    for (int i=0;i<6;++i) inv *= 2 - p * inv;
    const u64 mask = (1ULL << k) - 1;
    return ((0ULL - C) * inv) & mask;
}

int main() {
    constexpr int K = 26;
    vector<u64> p3(K+2,1), p2(K+2,1);
    for (int i=1;i<=K+1;++i) { p3[i]=p3[i-1]*3ULL; p2[i]=p2[i-1]*2ULL; }

    const u64 exp_cand[K+1] = {
        0,1,1,2,3,4,8,13,19,38,64,128,226,367,734,1295,2114,4228,
        7495,14990,27328,46611,93222,168807,286581,573162,1037374
    };
    const u64 exp_dom[K+1] = {
        0,0,0,0,0,0,1,2,3,7,12,25,44,70,141,246,394,789,
        1391,2796,5084,8592,17253,31150,52425,105267,189881
    };
    const u64 exp_maxcredit[K+1] = {
        0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,3,6,7,7,7,7,7,15,15
    };

    vector<Candidate> cand{{0,0}}, next;
    int first_k = 0; u64 first_C=0, first_best=0, first_N=0;

    cout << "k candidates one_sided_dominated max_credit\n";
    for (int k=1;k<=K;++k) {
        next.clear(); next.reserve(cand.size()*2);
        for (auto const& s : cand) {
            if (s.q >= QMIN[k]) next.push_back(s);
            Candidate odd{3*s.C + p2[k-1], uint8_t(s.q+1)};
            if (odd.q >= QMIN[k]) next.push_back(odd);
        }
        cand.swap(next);
        assert(cand.size() == exp_cand[k]);

        ReverseHenselOracle oracle{k,p3,p2};
        u64 dominated=0, maxcredit=0;
        for (auto const& s : cand) {
            const u64 mod = p3[s.q];
            const u64 r = s.C % mod;
            const u64 best = oracle.best(s.q,r);
            assert(best != UINT64_MAX && best >= s.C);
            assert((best - s.C) % mod == 0);
            const u64 credit = (best - s.C) / mod;
            if (credit) {
                ++dominated;
                maxcredit = max(maxcredit, credit);
                if (!first_k) {
                    first_k=k; first_C=s.C; first_best=best;
                    first_N=start_residue(s.C,s.q,k);
                }
            }
        }
        assert(dominated == exp_dom[k]);
        assert(maxcredit == exp_maxcredit[k]);
        cout << k << ' ' << cand.size() << ' ' << dominated << ' ' << maxcredit << '\n';
    }

    assert(first_k == 6);
    assert(first_C == 65);
    assert(first_best == 146);
    assert(first_best-first_C == 81);
    assert(first_N == 15);
    assert(start_residue(first_best,4,6) == 14);

    cout << "FIRST one-sided pruning: k=6 q=4 C=65 bestC=146 credit=1\n";
    cout << "candidate residue N mod64=15; competitor residue=14\n";
    cout << "MATH-037 is the first TWO-SIDED coefficient-language collision, not the first Hensel pruning.\n";
    cout << "Collatz remains OPEN\n";
}
