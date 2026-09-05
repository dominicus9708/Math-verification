#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

// Exact whole-prefix nearest-credit certificate for H=23,...,27.
//
// For a coefficient-surviving H-bit word w with q odd steps and correction R,
// define
//
//   d_near(w)=min{(R'-R)/3^q : R'>R, R'==R (mod 3^q)},
//
// where R' ranges over all length-H q-odd words (the alternate word need not
// itself satisfy coefficient survival).  G_H is the maximum finite d_near over
// coefficient survivors.
//
// This fills the exact gap between the earlier small-H sweep and the later
// H=28+ certificates:
//
//   G_23=6, G_24=6, G_25=12, G_26=12, G_27=12.
//
// Together with the already certified values this exposes a staircase rather
// than step-by-step growth of nearest root credit.  This is a finite exact
// certificate, not an asymptotic theorem and not a proof of Collatz.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {
int H,Q;
std::vector<u64> P3;

void generate_survivors(int pos,int q,u64 R,std::vector<u64>& out) {
    if (q>Q || q+(H-pos)<Q) return;
    if (pos==H) {
        if (q==Q) out.push_back(R);
        return;
    }
    if (u128(P3[q]) >= (u128(1)<<(pos+1)))
        generate_survivors(pos+1,q,R,out);
    if (u128(P3[q+1]) >= (u128(1)<<(pos+1)))
        generate_survivors(pos+1,q+1,3*R+(u64(1)<<pos),out);
}

void generate_all(int pos,int q,u64 R,
                  std::unordered_map<u64,std::vector<u64>>& cls) {
    if (q>Q || q+(H-pos)<Q) return;
    if (pos==H) {
        if (q==Q) cls[R%P3[Q]].push_back(R);
        return;
    }
    generate_all(pos+1,q,R,cls);
    generate_all(pos+1,q+1,3*R+(u64(1)<<pos),cls);
}

u64 run_layer(int h,int q) {
    H=h; Q=q;
    P3.assign(H+2,1);
    for (int i=1;i<int(P3.size());++i) P3[i]=3*P3[i-1];

    std::vector<u64> survivors;
    generate_survivors(0,0,0,survivors);
    if (survivors.empty()) return 0;

    std::unordered_map<u64,std::vector<u64>> cls;
    cls.reserve(survivors.size()*2+100);
    generate_all(0,0,0,cls);
    for (auto& kv:cls) std::sort(kv.second.begin(),kv.second.end());

    u64 g=0;
    for (u64 R:survivors) {
        auto& v=cls[R%P3[Q]];
        auto it=std::upper_bound(v.begin(),v.end(),R);
        if (it!=v.end()) {
            const u64 d=(*it-R)/P3[Q];
            assert(d>0);
            g=std::max(g,d);
        }
    }
    return g;
}

int qmin(int h) {
    u128 p3=1, p2=u128(1)<<h;
    int q=0;
    while (p3<p2) { p3*=3; ++q; }
    return q;
}
}

int main() {
    const u64 EXPECT[5]={6,6,12,12,12};
    for (int h=23;h<=27;++h) {
        u64 global=0;
        const int qm=qmin(h);
        for (int q=qm;q<=h;++q)
            global=std::max(global,run_layer(h,q));
        assert(global==EXPECT[h-23]);
        std::cout << "H=" << h << " G_H=" << global << '\n';
    }
    std::cout << "whole-prefix nearest credit H23-H27: PASS\n";
}
