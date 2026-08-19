#include <algorithm>
#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Exact finite calibration of repeated same-integer overlap for the stronger
// L=8 residue-maximal language.  This is diagnostic evidence for the remaining
// globalization bridge, not an asymptotic proof.
//
// Candidate family:
//   N = 4(3^m + sum_{i=0}^{m-1} a_i 3^i)+3, a_i in {0,1}.
//
// Language condition through H (H multiple of 8):
//   * coefficient survival at every accelerated step;
//   * every aligned 8-step parity block is the maximum-correction member of
//     its full-Hensel class.
//
// The program certifies selected m=20,21,22 survivor counts.  All candidate
// and language counts are exact integers.

using boost::multiprecision::cpp_int;
using u32=std::uint32_t;
using u64=std::uint64_t;
static constexpr int B=8;

std::array<std::unordered_set<u32>,9> ALLOW;
struct BlockInfo { int q=0; std::array<int,9> pref{}; };
std::vector<BlockInfo> BLOCKS;

void build_blocks(){
    std::array<u64,9> p3{}; p3[0]=1;
    for(int i=1;i<=8;++i) p3[i]=3*p3[i-1];
    struct E{u64 R=0;u32 mask=0;bool set=false;};
    std::array<std::unordered_map<u64,E>,9> mp;
    for(u32 mask=0;mask<(1u<<8);++mask){
        int q=0;u64 R=0;
        for(int i=0;i<8;++i) if((mask>>i)&1u){R=3*R+(u64(1)<<i);++q;}
        auto &e=mp[q][R%p3[q]];
        if(!e.set||R>e.R)e={R,mask,true};
    }
    for(int q=0;q<=8;++q){
        for(const auto &kv:mp[q]){
            const u32 mask=kv.second.mask;
            ALLOW[q].insert(mask);
            BlockInfo z; z.q=q; int c=0; z.pref[0]=0;
            for(int i=0;i<8;++i){c+=(mask>>i)&1u;z.pref[i+1]=c;}
            BLOCKS.push_back(z);
        }
    }
    const std::array<std::size_t,9> expect{{1,2,6,17,34,36,22,8,1}};
    for(int q=0;q<=8;++q) if(ALLOW[q].size()!=expect[q]) std::exit(2);
}

int qmin_exact(int k){
    cpp_int p3=1, p2=cpp_int(1)<<k; int q=0;
    while(p3<p2){p3*=3;++q;}
    return q;
}

cpp_int language_count(int H){
    std::vector<int> qmin(H+1);
    for(int j=1;j<=H;++j) qmin[j]=qmin_exact(j);
    std::unordered_map<int,cpp_int> dp,nd;
    dp[0]=1;
    for(int b=0;b<H/B;++b){
        nd.clear(); const int off=b*B;
        for(const auto &st:dp){
            for(const auto &z:BLOCKS){
                bool ok=true;
                for(int t=1;t<=B;++t)
                    if(st.first+z.pref[t]<qmin[off+t]){ok=false;break;}
                if(ok) nd[st.first+z.q]+=st.second;
            }
        }
        dp.swap(nd);
    }
    cpp_int s=0; for(const auto &x:dp)s+=x.second; return s;
}

bool survives(u64 N,int H){
    u64 x=N; int q=0; u32 bm=0; int bq=0,boff=0;
    cpp_int p3=1,p2=1;
    for(int k=0;k<H;++k){
        const int b=int(x&1u);
        bm|=u32(b)<<boff; bq+=b; ++boff;
        if(b){x=(3*x+1)>>1;++q;p3*=3;} else x>>=1;
        p2*=2;
        if(p3<p2) return false;
        if(boff==B){
            if(!ALLOW[bq].count(bm)) return false;
            bm=0;bq=0;boff=0;
        }
    }
    return true;
}

u64 candidate_survivors(int m,int H){
    std::vector<u64> p3(m+1,1);
    for(int i=1;i<=m;++i)p3[i]=3*p3[i-1];
    const u64 total=u64(1)<<m;
    u64 out=0;
    for(u64 mask=0;mask<total;++mask){
        u64 s=0;
        for(int i=0;i<m;++i) if((mask>>i)&1u) s+=p3[i];
        const u64 N=4*(p3[m]+s)+3;
        if(survives(N,H))++out;
    }
    return out;
}

struct Check{int m,H;u64 survivors;};
const std::array<Check,12> CHECKS{{
    {20,32,9981},{20,64,251},{20,96,9},{20,128,1},
    {21,32,20200},{21,64,474},{21,96,10},{21,128,0},
    {22,32,40359},{22,64,1022},{22,96,28},{22,128,0},
}};

int main(){
    build_blocks();
    std::unordered_map<int,cpp_int> lc;
    for(const auto &e:CHECKS){
        if(!lc.count(e.H)) lc[e.H]=language_count(e.H);
        const u64 s=candidate_survivors(e.m,e.H);
        if(s!=e.survivors) return 3;
        std::cout<<"m="<<e.m<<" H="<<e.H
                 <<" survivors="<<s
                 <<" language="<<lc[e.H]<<"\n";
    }

    // Both coefficient survival and the Cantor core force the common initial
    // canonical cylinder N==3 (mod 4): the first two parity bits are 11.
    // Hence the raw overlap factor has an unavoidable constant factor 4.
    // Removing it does not change any exponential rate.
    std::cout<<"common_forced_mod4_factor 4\n";
    std::cout<<"normalized_overlap Xi_circ = Xi/4\n";
    std::cout<<"L8 small-core multiwindow overlap certificate: PASS\n";
    return 0;
}
