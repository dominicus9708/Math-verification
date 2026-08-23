#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <utility>
#include <vector>

// Exact horizon sweep for the unconditional whole-prefix maximality filter.
//
// Through H=28 this verifies simultaneously:
//   1. the exact coefficient-survivor count;
//   2. the number whose complete (q,R mod 3^q) class correction is maximal;
//   3. the maximal root predecessor credit needed to delete a non-maximal word;
//   4. injectivity of the endpoint map on the remaining maximal survivors.
//
// The observed whole-prefix pruning saturates near 0.29 total bit rather than
// producing a visible positive per-step entropy rate.  On the other hand, the
// endpoint map is collision-free on the maximal coefficient-survivor set for
// every tested H=3,...,28.
//
// This is an exact finite certificate and theorem-candidate diagnostic, not a
// proof of an all-H endpoint-injectivity theorem and not a proof of Collatz.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

int L;
std::vector<u64> P3;

struct Word {
    u64 R;
    u64 start;
    u64 endpoint;
    int q;
    bool maximal;
};

u64 inverse_odd(u64 a) {
    u64 x=1;
    for (int i=0;i<6;++i) x*=2-a*x;
    return x;
}

void generate_survivors(int pos,int q,u64 R,std::vector<Word>& out) {
    if (pos==L) {
        const u64 mask=(u64(1)<<L)-1;
        const u64 inv=inverse_odd(P3[q])&mask;
        const u64 r=(-inv*R)&mask;
        const u128 num=u128(P3[q])*r+R;
        assert((num&mask)==0);
        const u64 y=static_cast<u64>(num>>L);
        out.push_back({R,r,y,q,true});
        return;
    }
    if (P3[q] >= (u64(1)<<(pos+1)))
        generate_survivors(pos+1,q,R,out);
    if (P3[q+1] >= (u64(1)<<(pos+1)))
        generate_survivors(pos+1,q+1,3*R+(u64(1)<<pos),out);
}

void generate_q(int pos,int need,u64 R,std::vector<u64>& out) {
    if (!need) { out.push_back(R); return; }
    if (L-pos<need) return;
    generate_q(pos+1,need,R,out);
    generate_q(pos+1,need-1,3*R+(u64(1)<<pos),out);
}

std::vector<u64> all_q(int q) {
    std::vector<u64> out;
    generate_q(0,q,0,out);
    return out;
}

} // namespace

int main() {
    constexpr std::array<u64,26> EXPECT_COEFF{
        2,3,4,8,13,19,38,64,128,226,367,734,1295,2114,4228,7495,
        14990,27328,46611,93222,168807,286581,573162,1037374,1762293,3524586
    };
    constexpr std::array<u64,26> EXPECT_MAXIMAL{
        2,3,4,7,11,16,31,52,103,182,297,593,1049,1720,3439,6104,
        12194,22244,38019,75969,137657,234156,467895,847493,1442349,2882872
    };
    constexpr std::array<u64,26> EXPECT_MAX_D{
        0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,3,6,7,7,7,7,7,15,15,15,29
    };

    std::cout << "H,coefficient,maximal,retention,max_credit,unique_endpoints\n";

    for (L=3;L<=28;++L) {
        P3.assign(L+2,1);
        for (int i=1;i<int(P3.size());++i) P3[i]=3*P3[i-1];

        std::vector<Word> words;
        generate_survivors(0,0,0,words);
        std::vector<std::vector<std::size_t>> byq(L+1);
        for (std::size_t i=0;i<words.size();++i)
            byq[words[i].q].push_back(i);

        u64 kept=0,maxd=0;
        for (int q=0;q<=L;++q) {
            if (byq[q].empty()) continue;
            auto all=all_q(q);
            std::vector<std::pair<u64,u64>> keyed;
            keyed.reserve(all.size());
            for (u64 R:all) keyed.push_back({R%P3[q],R});
            std::sort(keyed.begin(),keyed.end());

            for (std::size_t wi:byq[q]) {
                auto& w=words[wi];
                const u64 key=w.R%P3[q];
                auto hi=std::upper_bound(keyed.begin(),keyed.end(),
                                         std::pair<u64,u64>{key,std::numeric_limits<u64>::max()});
                const u64 mx=(hi-1)->second;
                w.maximal=(w.R==mx);
                if (w.maximal) ++kept;
                else {
                    assert(mx>w.R && (mx-w.R)%P3[q]==0);
                    maxd=std::max(maxd,(mx-w.R)/P3[q]);
                }
            }
        }

        std::unordered_map<u64,u32> endpoints;
        endpoints.reserve(std::size_t(kept)*2+1);
        for (const auto& w:words) if (w.maximal) ++endpoints[w.endpoint];
        u64 collision_groups=0;
        for (const auto& kv:endpoints) if (kv.second>1) ++collision_groups;

        const std::size_t j=std::size_t(L-3);
        assert(words.size()==EXPECT_COEFF[j]);
        assert(kept==EXPECT_MAXIMAL[j]);
        assert(maxd==EXPECT_MAX_D[j]);
        assert(endpoints.size()==kept);
        assert(collision_groups==0);

        std::cout << L << ',' << words.size() << ',' << kept << ','
                  << double(kept)/double(words.size()) << ',' << maxd << ','
                  << endpoints.size() << '\n';
    }

    std::cout << "whole-prefix maximality horizon sweep: PASS\n";
}
