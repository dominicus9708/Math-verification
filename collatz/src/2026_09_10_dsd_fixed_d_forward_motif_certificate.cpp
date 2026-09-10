// DSD fixed-even-budget forward/motif certificate.
// Scope: finite exact checks used after MATH-050, not a Collatz proof.
//
// For a length-K parity word, D is the number of even bits and q=K-D.
// This certificate enumerates exact fixed-D words, computes terminal Hensel
// class maxima keyed by C mod 3^q, reconstructs the nested prefilter from
// depth K-1 survivors, and reports the newly pruned words.
//
// Intended audited range here: K=32..41, D=2..7.  Full corrections are guarded
// with unsigned __int128 before conversion to u64.
#include <bits/stdc++.h>
using namespace std; using u64=uint64_t; using u128=__uint128_t;
struct W{u64 mask,C;bool valid;};
static u64 p2[64],p3[64];
vector<W> enumerate_words(int K,int D){
    vector<W>v;u64 n=1;for(int i=1;i<=D;i++)n=n*(K-D+i)/i;v.reserve((size_t)n);
    function<void(int,int,u64,u64,int,bool)> rec=[&](int p,int ev,u64 mask,u64 C,int q,bool valid){
        if(p==K){if(ev==D)v.push_back({mask,C,valid});return;}
        int rem=K-p;if(ev>D||ev+rem<D)return;
        if(ev+(rem-1)>=D){u128 x=(u128)3*C+p2[p];if(x>numeric_limits<u64>::max())abort();int q1=q+1;rec(p+1,ev,mask,(u64)x,q1,valid&&(p3[q1]>p2[p+1]));}
        if(ev<D)rec(p+1,ev+1,mask|(1ULL<<p),C,q,valid&&(p3[q]>p2[p+1]));
    };
    rec(0,0,0,0,0,true);return v;
}
vector<W> terminal_survivors(int K,int D){
    auto v=enumerate_words(K,D);int q=K-D;u64 mod=p3[q];unordered_map<u64,u64>mx;mx.reserve(v.size()*2+1);
    for(auto const&w:v){u64 r=w.C%mod;auto it=mx.find(r);if(it==mx.end()||w.C>it->second)mx[r]=w.C;}
    vector<W>s;for(auto const&w:v)if(w.valid&&mx[w.C%mod]==w.C)s.push_back(w);return s;
}
vector<u64> newly_pruned_masks(int K,int D){
    auto cur=enumerate_words(K,D);int q=K-D;u64 mod=p3[q];unordered_map<u64,u64>mx;mx.reserve(cur.size()*2+1);unordered_map<u64,u64>Cby;Cby.reserve(cur.size()*2+1);
    for(auto const&w:cur){Cby[w.mask]=w.C;u64 r=w.C%mod;auto it=mx.find(r);if(it==mx.end()||w.C>it->second)mx[r]=w.C;}
    auto odd_parent=terminal_survivors(K-1,D);auto even_parent=terminal_survivors(K-1,D-1);vector<u64>rem;
    for(auto const&w:odd_parent){u64 C=Cby[w.mask];if(mx[C%mod]!=C)rem.push_back(w.mask);}
    for(auto const&w:even_parent){u64 m=w.mask|(1ULL<<(K-1));u64 C=Cby[m];if(mx[C%mod]!=C)rem.push_back(m);}
    sort(rem.begin(),rem.end());return rem;
}
set<u64> d6_motif_masks(int K){
    set<u64>s;for(int n=10;n<=K-6;n++){
        int A[]={n-2,n,n+1,n+2,n+3,K-2};u64 a=0;for(int p:A)a|=1ULL<<p;s.insert(a);
        int B[]={n-3,n,n+1,n+2,n+3,K-2};u64 b=0;for(int p:B)b|=1ULL<<p;s.insert(b);
    }return s;
}
int main(){
    p2[0]=p3[0]=1;for(int i=1;i<64;i++){p2[i]=p2[i-1]*2ULL;if(i<=40)p3[i]=p3[i-1]*3ULL;}
    auto expect=[&](int K,int D)->long long{if(D==2)return 1;if(D>=3&&D<=5)return 0;if(D==6)return 2LL*K-30;if(D==7)return 6LL*K-103;return -1;};
    for(int K=32;K<=41;K++)for(int D=2;D<=7;D++){
        auto r=newly_pruned_masks(K,D);long long e=expect(K,D);if((long long)r.size()!=e){cerr<<"count mismatch K="<<K<<" D="<<D<<" got="<<r.size()<<" expected="<<e<<"\n";return 1;}
        if(D==6){auto m=d6_motif_masks(K);set<u64>a(r.begin(),r.end());if(a!=m){cerr<<"d6 motif mismatch K="<<K<<"\n";return 2;}}
        cout<<K<<' '<<D<<' '<<r.size()<<" PASS\n";
    }
    // d=2 explicit terminal witness family: candidate even positions {K-2,K-1}.
    // The unrestricted competitor with evens {0,K-2} has
    // C_comp-C_cand = 3^(K-2), hence credit 1 in q=K-2.
    // d=6 extracted terminal witness families, for n=10..K-6:
    // A={n-2,n,n+1,n+2,n+3,K-2}, A'={0,1,n-2,n,K-2,K-1};
    // B={n-3,n,n+1,n+2,n+3,K-2}, B'={0,1,n-3,n+1,K-2,K-1}.
    // Direct block algebra gives C(A')-C(A)=C(B')-C(B)=3^(K-5)
    // =3*3^(K-6), so each pair is one exact q=K-6 Hensel class with credit 3.
    cout<<"FINITE EXACT CHECKS PASS; general uniqueness beyond audited K-range remains open.\n";
}
