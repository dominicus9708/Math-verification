#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <utility>
#include <vector>

// Unconditional whole-prefix Hensel/endpoint maximality certificate at L=28.
//
// For a length-L parity word w with q odd steps and correction R_w,
//
//   T^L(N) = (3^q N + R_w)/2^L.
//
// If another length-L word u has the same q and
//
//   R_u = R_w + 3^q d,   d>0,
//
// then M=N-d reaches exactly the same L-step endpoint.  Hence a minimal
// counterexample N>d cannot use w.  This is a root-level predecessor and does
// NOT rely on repeating a local block argument later in the orbit.
//
// The certificate proves for every coefficient-surviving L=28 word:
//   * 3,524,586 coefficient survivors total;
//   * 2,882,872 are maximum-correction representatives of their complete
//     same-(q,R mod 3^q) class;
//   * 641,714 are deleted by the root predecessor theorem;
//   * the largest required predecessor credit is only d=29;
//   * every selector-compatible mixed-q (q -> q+s) predecessor cylinder,
//     1<=s<=28-q, occurs on a word already deleted by same-q maximality.
//
// Thus mixed-q whole-prefix pruning adds zero new L=28 words after the safe
// same-q root filter.  This is a finite exact theorem, not a Collatz proof.

using u64 = std::uint64_t;
using i64 = std::int64_t;

namespace {

constexpr int L = 28;
std::array<u64,30> P3{};

struct Word { u64 R; int q; };

void generate_survivors(int pos,int q,u64 R,std::vector<Word>& out) {
    if (pos==L) { out.push_back({R,q}); return; }
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

u64 selector_residue(int prefix,int s) {
    u64 S=0,p=1;
    for (int i=0;i<s;++i) {
        if ((prefix>>i)&1) S+=p;
        p*=3;
    }
    return (4*S+3)%P3[s];
}

} // namespace

int main() {
    P3[0]=1;
    for (int i=1;i<int(P3.size());++i) P3[i]=3*P3[i-1];

    std::vector<Word> survivors;
    survivors.reserve(3'524'586);
    generate_survivors(0,0,0,survivors);
    assert(survivors.size()==3'524'586);

    std::array<std::vector<std::size_t>,29> byq;
    for (std::size_t i=0;i<survivors.size();++i)
        byq[survivors[i].q].push_back(i);

    constexpr std::array<u64,11> EXPECT_TOTAL{
        663535,1236935,898798,464889,185684,57923,13953,2520,322,26,1
    };
    constexpr std::array<u64,11> EXPECT_KEEP{
        535688,1003902,736512,385729,156461,49738,12246,2270,299,26,1
    };
    constexpr std::array<u64,11> EXPECT_MAX_D{
        29,15,7,7,3,1,1,1,1,0,0
    };

    std::vector<unsigned char> maximal(survivors.size(),1);
    u64 kept=0,rejected=0,global_max_d=0;

    for (int q=18;q<=28;++q) {
        auto a=all_q(q);
        std::vector<std::pair<u64,u64>> keyed;
        keyed.reserve(a.size());
        for (u64 R:a) keyed.push_back({R%P3[q],R});
        std::sort(keyed.begin(),keyed.end());

        u64 kq=0,maxdq=0;
        for (std::size_t wi:byq[q]) {
            const u64 Rw=survivors[wi].R;
            const u64 key=Rw%P3[q];
            auto lo=std::lower_bound(keyed.begin(),keyed.end(),
                                     std::pair<u64,u64>{key,0});
            auto hi=std::upper_bound(keyed.begin(),keyed.end(),
                                     std::pair<u64,u64>{key,std::numeric_limits<u64>::max()});
            assert(lo!=hi);
            const u64 mx=(hi-1)->second;
            if (Rw==mx) {
                ++kept; ++kq;
            } else {
                maximal[wi]=0;
                ++rejected;
                assert(mx>Rw && (mx-Rw)%P3[q]==0);
                const u64 d=(mx-Rw)/P3[q];
                maxdq=std::max(maxdq,d);
                global_max_d=std::max(global_max_d,d);
            }
        }
        const std::size_t j=std::size_t(q-18);
        assert(byq[q].size()==EXPECT_TOTAL[j]);
        assert(kq==EXPECT_KEEP[j]);
        assert(maxdq==EXPECT_MAX_D[j]);
    }

    assert(kept==2'882'872);
    assert(rejected==641'714);
    assert(global_max_d==29);

    // Exact mixed-q audit.  A q+s alternate u with
    // R_u-R_w = 3^q d gives M=(N-d)/3^s.  It is an integer root predecessor
    // exactly on the selector cylinder N == d (mod 3^s).  At m=45 and s<=10,
    // N mod 3^s runs over 4*sum a_i 3^i + 3 with a_i in {0,1}.
    // Verify that every such selector-compatible mixed-q cylinder belongs to
    // a word already rejected above.
    u64 compatible_words=0,compatible_pairs=0;
    std::vector<unsigned char> seen(survivors.size(),0);

    for (int q=18;q<=27;++q) {
        for (int s=1;s<=28-q;++s) {
            auto alt=all_q(q+s);
            std::vector<std::pair<u64,u64>> keyed;
            keyed.reserve(alt.size());
            for (u64 R:alt) keyed.push_back({R%P3[q],R});
            std::sort(keyed.begin(),keyed.end());

            std::unordered_map<u64,int> allowed;
            allowed.reserve((std::size_t(1)<<s)*2);
            for (int pref=0;pref<(1<<s);++pref)
                allowed.emplace(selector_residue(pref,s),pref);

            for (std::size_t wi:byq[q]) {
                const u64 Rw=survivors[wi].R;
                const u64 key=Rw%P3[q];
                auto lo=std::lower_bound(keyed.begin(),keyed.end(),
                                         std::pair<u64,u64>{key,0});
                auto hi=std::upper_bound(keyed.begin(),keyed.end(),
                                         std::pair<u64,u64>{key,std::numeric_limits<u64>::max()});
                for (auto it=lo;it!=hi;++it) {
                    const i64 diff=i64(it->second)-i64(Rw);
                    assert(diff%i64(P3[q])==0);
                    i64 d=diff/i64(P3[q]);
                    i64 r=d%i64(P3[s]);
                    if (r<0) r+=i64(P3[s]);
                    if (!allowed.count(u64(r))) continue;
                    ++compatible_pairs;
                    if (!seen[wi]) { seen[wi]=1; ++compatible_words; }
                    assert(!maximal[wi]);
                }
            }
        }
    }

    assert(compatible_words==14'855);
    assert(compatible_pairs==21'226);

    std::cout << "coefficient survivors=" << survivors.size() << "\n";
    std::cout << "whole-prefix same-q maxima=" << kept << "\n";
    std::cout << "whole-prefix deletions=" << rejected << "\n";
    std::cout << "maximum root predecessor credit=" << global_max_d << "\n";
    std::cout << "selector-compatible mixed-q words=" << compatible_words << "\n";
    std::cout << "selector-compatible mixed-q pairs=" << compatible_pairs << "\n";
    std::cout << "incremental mixed-q words after same-q maximality=0\n";
    std::cout << "depth28 whole-prefix endpoint maximality: PASS\n";
}
