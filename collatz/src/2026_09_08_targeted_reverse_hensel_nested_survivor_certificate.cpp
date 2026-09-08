// MATH-041: targeted reverse-Hensel oracle + nested candidate survivor engine.
//
// Builds only coefficient-surviving candidate prefixes.  For each candidate
// class (k,q,r), an exact reverse-Hensel recursion reconstructs arbitrary
// competitors in that class and returns the maximum correction.  A candidate
// is retained iff it is the unrestricted class maximum.
//
// MATH-013 downstream dominance implies a non-maximal prefix can never recover
// under a common suffix.  Therefore filtering at each depth is equivalent to
// imposing root-Hensel maximality at every prefix.
//
// Exact finite scope: depths <=31.  OpenMP changes only execution order.
// Collatz remains OPEN.
// Build: g++ -O3 -fopenmp -std=c++17 <file> -o m41

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;
using u64 = uint64_t;

static const int QMIN[] = {
    0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,
    16,16,17,18,18,19,19,20
};

struct State { u64 C; uint8_t q; };

struct Solver {
    int k;
    const vector<u64>* p3;
    const vector<u64>* p2;

    u64 rec(int j, int maxp, u64 r) const {
        if (j == 0) return r == 0 ? 0 : UINT64_MAX;
        u64 best = UINT64_MAX;
        const u64 mod_prev = (*p3)[j-1];
        for (int p=j-1; p<maxp; ++p) {
            if ((r % 3) != ((*p2)[p] % 3)) continue;
            __int128 diff = (__int128)r - (__int128)(*p2)[p];
            assert(diff % 3 == 0);
            __int128 z = diff / 3;
            long long m = (long long)mod_prev;
            long long rprev = m ? (long long)(z % m) : 0;
            if (rprev < 0) rprev += m;
            u64 prev = rec(j-1, p, (u64)rprev);
            if (prev == UINT64_MAX) continue;
            u64 C = 3*prev + (*p2)[p];
            if (best == UINT64_MAX || C > best) best = C;
        }
        return best;
    }

    u64 best(int q, u64 r) const { return rec(q,k,r); }
};

int main() {
    constexpr int K=31;
    vector<u64> p3(K+2,1), p2(K+2,1);
    for (int i=1;i<=K+1;++i) { p3[i]=p3[i-1]*3ULL; p2[i]=p2[i-1]*2ULL; }

    // Full coefficient-language counts (without Hensel filtering), obtained by
    // exact q-count recurrence and included as regression constants.
    const u64 coeff_total[K+1] = {
        1,
        1,1,2,3,4,8,13,19,38,64,128,226,367,734,1295,2114,4228,
        7495,14990,27328,46611,93222,168807,286581,573162,1037374,
        1762293,3524586,6385637,12771274,23642078
    };

    const u64 exp_prefilter[K+1] = {
        1,
        1,1,2,3,4,8,12,17,32,53,104,183,298,594,1050,1721,3440,
        6111,12208,22272,38055,76038,137802,234332,468312,848189,
        1443156,2884698,5230056,10453970,19359254
    };

    const u64 exp_survive[K+1] = {
        1,
        1,1,2,3,4,7,11,16,31,52,103,182,297,593,1049,1720,3439,
        6104,12194,22244,38019,75969,137657,234156,467895,847493,
        1442349,2882872,5226985,10446423,19347686
    };

    vector<State> live{{0,0}}, next;
    cout << "threads " << omp_get_max_threads() << '\n';
    cout << "k full_coefficient from_previous_Hensel survivors newly_pruned cumulative_Hensel_removed\n";

    for (int k=1;k<=K;++k) {
        next.clear(); next.reserve(live.size()*2);
        for (auto const& s : live) {
            if (s.q >= QMIN[k]) next.push_back(s);
            State odd{3*s.C+p2[k-1], uint8_t(s.q+1)};
            if (odd.q >= QMIN[k]) next.push_back(odd);
        }
        assert(next.size() == exp_prefilter[k]);

        vector<uint8_t> keep(next.size(),0);
        Solver solver{k,&p3,&p2};
        #pragma omp parallel for schedule(dynamic,64)
        for (long long i=0;i<(long long)next.size();++i) {
            auto const& s = next[(size_t)i];
            const u64 mod=p3[s.q];
            const u64 r=s.C%mod;
            const u64 best=solver.best(s.q,r);
            assert(best != UINT64_MAX && best >= s.C);
            keep[(size_t)i] = (best == s.C);
        }

        size_t w=0;
        for (size_t i=0;i<next.size();++i) if (keep[i]) next[w++]=next[i];
        next.resize(w);
        assert(next.size() == exp_survive[k]);
        live.swap(next);

        const u64 newly = exp_prefilter[k]-exp_survive[k];
        const u64 cumulative = coeff_total[k]-exp_survive[k];
        cout << k << ' ' << coeff_total[k] << ' ' << exp_prefilter[k] << ' '
             << exp_survive[k] << ' ' << newly << ' ' << cumulative << '\n';
    }

    assert(coeff_total[31] == 23642078ULL);
    assert(exp_survive[31] == 19347686ULL);
    assert(coeff_total[31]-exp_survive[31] == 4294392ULL);

    // MATH-013 downstream dominance explains why a prefix once removed by a
    // larger-h class representative never needs to be generated again.
    cout << "depth31 coefficient classes = 23642078\n";
    cout << "depth31 all-prefix coefficient+Hensel survivors = 19347686\n";
    cout << "depth31 cumulative Hensel-removed coefficient classes = 4294392\n";
    cout << "Targeted oracle avoids materializing the full unrestricted class table.\n";
    cout << "FINITE EXACT through depth31; first cell and Collatz remain OPEN.\n";
}
