// Depth-35 partial exact one-sided root-Hensel continuation, high-q tail q>=28.
// Restores the MATH-044 nested candidate rule and uses the MATH-013 downstream-stable
// class-max quotient on the arbitrary competitor side. Scope d=k-q<=7 is exact for
// every terminal q>=28 state at k=35 because d never decreases under either child.
// Depth-34 q=27..34 is regression-checked against the MATH-044 ledger.
// Finite partial certificate only; Collatz remains OPEN.
#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;

struct State { u64 C; uint8_t q; };

static inline void upd(unordered_map<u64,u64>& mp, u64 r, u64 C){
    auto it = mp.find(r);
    if(it==mp.end()) mp.emplace(r,C);
    else if(C > it->second) it->second=C;
}

int main(){
    constexpr int KMAX=35, DMAX=7;
    u64 p2[KMAX+1], p3[KMAX+1];
    p2[0]=1; p3[0]=1;
    for(int i=1;i<=KMAX;i++){p2[i]=p2[i-1]*2ULL; p3[i]=p3[i-1]*3ULL;}
    int qmin[KMAX+1]{};
    for(int k=1;k<=KMAX;k++){
        int q=0; while(p3[q] <= p2[k]) ++q; qmin[k]=q;
    }

    vector<unordered_map<u64,u64>> arb(KMAX+1), narb(KMAX+1);
    arb[0].reserve(1); arb[0][0]=0;
    vector<State> live{{0,0}}, pre, next;

    const u64 known34[35] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        32432663ULL,39138196ULL,27942054ULL,15148621ULL,6586664ULL,
        2350378ULL,688417ULL,163625ULL,30866ULL,4459ULL,464ULL,32ULL,1ULL
    };

    cout << "k\tqmin\tpre_tail\tsurv_tail\tarb_classes_tail\n";
    for(int k=1;k<=KMAX;k++){
        for(auto &m:narb) m.clear();
        // Exact arbitrary class maxima for all length-k words with d=k-q<=7.
        for(int q=0;q<=k-1;q++) if(!arb[q].empty()){
            int dprev=(k-1)-q;
            // even child: d increases by 1
            if(dprev+1<=DMAX){
                auto &dst=narb[q];
                if(dst.empty()) dst.reserve(arb[q].size()*2+1);
                for(auto const &kv:arb[q]) upd(dst, kv.first, kv.second);
            }
            // odd child: d unchanged
            if(dprev<=DMAX){
                auto &dst=narb[q+1];
                if(dst.empty()) dst.reserve(arb[q].size()*2+1);
                u64 mod=p3[q+1], bit=p2[k-1];
                for(auto const &kv:arb[q]){
                    u64 C=3*kv.second + bit;
                    u64 r=C%mod;
                    upd(dst,r,C);
                }
            }
        }
        arb.swap(narb);

        pre.clear(); pre.reserve(live.size()*2);
        u64 bit=p2[k-1];
        for(auto const&s:live){
            int dprev=(k-1)-(int)s.q;
            // even candidate
            if(dprev+1<=DMAX && (int)s.q>=qmin[k]) pre.push_back(s);
            // odd candidate
            int qo=(int)s.q+1;
            if(dprev<=DMAX && qo>=qmin[k]) pre.push_back(State{3*s.C+bit,(uint8_t)qo});
        }
        next.clear(); next.reserve(pre.size());
        vector<u64> preq(k+1), survq(k+1), arbq(k+1);
        for(int q=max(0,k-DMAX);q<=k;q++) arbq[q]=arb[q].size();
        for(auto const&s:pre){
            ++preq[s.q];
            u64 r=s.C%p3[s.q];
            auto it=arb[s.q].find(r);
            if(it==arb[s.q].end()) { cerr<<"missing arb class\n"; return 4; }
            if(it->second==s.C){next.push_back(s); ++survq[s.q];}
        }
        live.swap(next);
        u64 at=0; for(int q=max(0,k-DMAX);q<=k;q++) at+=arbq[q];
        cout<<k<<'\t'<<qmin[k]<<'\t'<<pre.size()<<'\t'<<live.size()<<'\t'<<at<<"\n";

        if(k==34){
            cout << "DEPTH34_Q\nq\tprefilter\tsurvivors\tknown_survivors\tstatus\n";
            for(int q=27;q<=34;q++){
                cout<<q<<'\t'<<preq[q]<<'\t'<<survq[q]<<'\t'<<known34[q]<<'\t'<<(survq[q]==known34[q]?"OK":"MISMATCH")<<"\n";
            }
        }
        if(k==35){
            const u64 expected_pre[36] = {
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                3038795ULL,852042ULL,194491ULL,35325ULL,4923ULL,496ULL,33ULL,1ULL
            };
            const u64 expected_surv[36] = {
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                3038688ULL,852002ULL,194491ULL,35325ULL,4923ULL,495ULL,33ULL,1ULL
            };
            for(int q=28;q<=35;q++){
                assert(preq[q]==expected_pre[q]);
                assert(survq[q]==expected_surv[q]);
            }
            cout << "DEPTH35_Q\nq\tprefilter\tarbitrary_classes\tsurvivors\tnewly_pruned\n";
            for(int q=28;q<=35;q++){
                cout<<q<<'\t'<<preq[q]<<'\t'<<arbq[q]<<'\t'<<survq[q]<<'\t'<<(preq[q]-survq[q])<<"\n";
            }
        }
    }
}
