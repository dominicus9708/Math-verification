#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

// Targeted exact extension of the whole-prefix endpoint audit.
//
// Instead of computing whole-prefix maximality for every coefficient survivor,
// this verifier first identifies only endpoint collision groups and then
// computes the complete same-(q,R mod 3^q) correction maximum for the residue
// classes appearing inside those groups.  This is sufficient to test whether
// any endpoint can contain two whole-prefix maximal coefficient survivors.
//
// Exact audited results:
//   H=30: 12,771,274 coefficient survivors; 758,572 endpoint collision groups;
//         zero groups with >=2 whole-prefix maxima.
//   H=31: 23,642,078 coefficient survivors; 1,401,286 endpoint collision groups;
//         zero groups with >=2 whole-prefix maxima.
//
// In every collision group having exactly one maximal survivor, that survivor
// is the largest-q member of the group.  This is finite evidence for the
// stronger endpoint-injectivity conjecture; the general O(H) endpoint-fibre
// theorem is proved algebraically in the companion note and does not depend on
// this finite observation.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

struct Word {
    u64 endpoint;
    u64 R;
    std::uint8_t q;
};

int H;
std::vector<u64> P3;
std::vector<Word> words;

void generate_survivors(int pos,int q,u64 R) {
    if (pos==H) {
        const u64 mod=u64(1)<<H;
        const u64 mask=mod-1;
        const u64 a=P3[q];
        u64 inv=1;
        for (int i=0;i<6;++i) inv*=2-a*inv;
        inv&=mask;
        const u64 r=(-inv*R)&mask;
        const u128 num=u128(a)*r+R;
        const u64 y=static_cast<u64>(num>>H);
        words.push_back({y,R,static_cast<std::uint8_t>(q)});
        return;
    }
    if (P3[q] >= (u64(1)<<(pos+1)))
        generate_survivors(pos+1,q,R);
    if (P3[q+1] >= (u64(1)<<(pos+1)))
        generate_survivors(pos+1,q+1,3*R+(u64(1)<<pos));
}

struct TargetSet {
    std::unordered_map<u64,u64> maximum;
};

std::vector<TargetSet> targets;

void enumerate_all_q(int pos,int need,int q,u64 R) {
    if (!need) {
        const u64 key=R%P3[q];
        auto it=targets[q].maximum.find(key);
        if (it!=targets[q].maximum.end() && R>it->second)
            it->second=R;
        return;
    }
    if (H-pos<need) return;
    enumerate_all_q(pos+1,need,q,R);
    enumerate_all_q(pos+1,need-1,q,3*R+(u64(1)<<pos));
}

struct Expected {
    u64 survivors;
    u64 collision_groups;
    u64 collision_members;
    u64 max_group;
    u64 maximal_collision_members;
    u64 zero_groups;
    u64 one_groups;
};

Expected expected_for(int h) {
    if (h==30) return {
        12'771'274ULL,
        758'572ULL,
        1'523'006ULL,
        4ULL,
        746'893ULL,
        11'679ULL,
        746'893ULL
    };
    if (h==31) return {
        23'642'078ULL,
        1'401'286ULL,
        2'813'598ULL,
        4ULL,
        1'379'303ULL,
        21'983ULL,
        1'379'303ULL
    };
    std::abort();
}

int main(int argc,char**argv) {
    H=(argc>=2 ? std::stoi(argv[1]) : 30);
    if (H!=30 && H!=31) return 2;
    const auto expected=expected_for(H);

    P3.assign(H+2,1);
    for (int i=1;i<int(P3.size());++i) P3[i]=3*P3[i-1];

    words.reserve(static_cast<std::size_t>(expected.survivors));
    generate_survivors(0,0,0);
    assert(words.size()==expected.survivors);

    std::sort(words.begin(),words.end(),[](const Word&a,const Word&b){
        if (a.endpoint!=b.endpoint) return a.endpoint<b.endpoint;
        return a.q<b.q;
    });

    targets.resize(H+1);
    u64 collision_groups=0,collision_members=0,max_group=0;

    for (std::size_t i=0;i<words.size();) {
        std::size_t j=i+1;
        while (j<words.size() && words[j].endpoint==words[i].endpoint) ++j;
        if (j-i>1) {
            ++collision_groups;
            collision_members+=j-i;
            max_group=std::max<u64>(max_group,j-i);
            for (std::size_t k=i;k<j;++k) {
                const int q=words[k].q;
                const u64 key=words[k].R%P3[q];
                auto& m=targets[q].maximum;
                auto it=m.find(key);
                if (it==m.end()) m.emplace(key,words[k].R);
                else if (words[k].R>it->second) it->second=words[k].R;
            }
        }
        i=j;
    }

    assert(collision_groups==expected.collision_groups);
    assert(collision_members==expected.collision_members);
    assert(max_group==expected.max_group);

    for (int q=0;q<=H;++q)
        if (!targets[q].maximum.empty())
            enumerate_all_q(0,q,q,0);

    u64 bad_groups=0;
    u64 maximal_collision_members=0;
    u64 zero_groups=0;
    u64 one_groups=0;
    u64 one_is_maxq=0;

    for (std::size_t i=0;i<words.size();) {
        std::size_t j=i+1;
        while (j<words.size() && words[j].endpoint==words[i].endpoint) ++j;
        if (j-i>1) {
            int count=0;
            int maxq=-1;
            int survivor_q=-1;
            for (std::size_t k=i;k<j;++k) {
                maxq=std::max(maxq,int(words[k].q));
                const int q=words[k].q;
                const u64 key=words[k].R%P3[q];
                if (words[k].R==targets[q].maximum[key]) {
                    ++count;
                    survivor_q=q;
                }
            }
            maximal_collision_members+=count;
            if (count==0) ++zero_groups;
            else if (count==1) {
                ++one_groups;
                if (survivor_q==maxq) ++one_is_maxq;
            } else {
                ++bad_groups;
            }
        }
        i=j;
    }

    assert(maximal_collision_members==expected.maximal_collision_members);
    assert(zero_groups==expected.zero_groups);
    assert(one_groups==expected.one_groups);
    assert(one_is_maxq==one_groups);
    assert(bad_groups==0);

    std::cout << "H=" << H
              << " survivors=" << words.size()
              << " collision_groups=" << collision_groups
              << " collision_members=" << collision_members
              << " max_group=" << max_group
              << " zero_max_groups=" << zero_groups
              << " one_max_groups=" << one_groups
              << " bad_groups=" << bad_groups << '\n';
    std::cout << "whole-prefix targeted endpoint extension: PASS\n";
}
