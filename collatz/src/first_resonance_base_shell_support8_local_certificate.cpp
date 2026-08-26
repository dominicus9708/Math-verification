#include <algorithm>
#include <array>
#include <atomic>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <omp.h>
#include <unordered_set>
#include <vector>

using u128 = unsigned __int128;
static constexpr uint64_t A=114208327604ULL,Q=72057431991ULL,P=A-Q;
static constexpr int GAPLEN=48, ODDS=49;

struct H { size_t operator()(u128 x) const noexcept {
    uint64_t lo=(uint64_t)x, hi=(uint64_t)(x>>64);
    return std::hash<uint64_t>{}(lo^(hi*0x9e3779b97f4a7c15ULL));
}};

static u128 invodd(u128 a,int bits){
    u128 x=1; for(int i=0;i<8;++i)x=x*(2-a*x);
    return x&((((u128)1)<<bits)-1);
}

static std::vector<std::array<int,GAPLEN>> factors(){
    std::vector<uint64_t> bp;
    for(int j=0;j<=GAPLEN;++j){uint64_t r=(u128(j)*P)%Q;bp.push_back(r?Q-r:0);}
    std::sort(bp.begin(),bp.end());bp.erase(std::unique(bp.begin(),bp.end()),bp.end());
    std::vector<std::array<int,GAPLEN>> out;
    for(uint64_t r:bp){
        std::array<int,GAPLEN> g{}; uint64_t rr=r;
        for(int j=0;j<GAPLEN;++j){int b=rr>=Q-P;g[j]=1+b;rr=b?rr+P-Q:rr+P;}
        if(std::find(out.begin(),out.end(),g)==out.end())out.push_back(g);
    }
    assert(out.size()==49); return out;
}

int main(){
    auto fs=factors();
    const u128 B=((u128)1)<<71, U=8*B/3, MAX=~(u128)0, MASK73=(((u128)1)<<73)-1;
    u128 inv3=invodd(3,73), ip[50]; ip[0]=1;
    for(int q=1;q<50;++q)ip[q]=(ip[q-1]*inv3)&MASK73;

    unsigned long long raw_total=0, phase_candidate_total=0;
    std::atomic<bool> bad(false); int global_worst=-1;

    #pragma omp parallel for schedule(dynamic,1) reduction(+:raw_total,phase_candidate_total)
    for(int pi=0;pi<49;++pi){
        const auto& g=fs[pi];
        std::unordered_set<u128,H> cand; cand.reserve(10'000'000);
        std::array<int,ODDS> d{}; uint64_t raw=0;

        auto dfs=[&](auto&& self,int i,int supp,int pos,u128 R,int q)->void{
            if(i==ODDS){
                if(supp!=8)return; ++raw;
                int bits=std::min(73,pos+1); assert(bits>=72);
                u128 mod=((u128)1)<<bits, mask=mod-1;
                u128 r=(mod-(R&mask))&mask;
                r=(r*(ip[q]&mask))&mask;
                for(u128 n=r;n<U;n+=mod)if(n>B)cand.insert(n);
                return;
            }
            int maxd=d[i-1]+g[i-1]-1;
            for(int nd=0;nd<=maxd;++nd){
                int ns=supp+(nd>0); if(ns>8)continue;
                int npos=pos+g[i-1]+d[i-1]-nd;
                u128 nR=R; int nq=q;
                if(npos<73){nR=(3*nR+(((u128)1)<<npos))&MASK73;++nq;}
                d[i]=nd; self(self,i+1,ns,npos,nR,nq);
            }
        };
        dfs(dfs,1,0,0,1,1);
        raw_total+=raw; phase_candidate_total+=cand.size();

        int local_worst=-1;
        for(u128 n:cand){
            u128 x=n; int st=0;
            while(x>=B&&st<=2000){
                if(x&1){if(x>(MAX-1)/3){bad.store(true);break;}x=(3*x+1)>>1;}
                else x>>=1; ++st;
            }
            if(!(x<B)){bad.store(true);break;}
            local_worst=std::max(local_worst,st);
        }
        #pragma omp critical
        global_worst=std::max(global_worst,local_worst);
    }

    assert(!bad.load());
    assert(raw_total==1'137'416'850ULL);
    assert(phase_candidate_total==443'720'724ULL);
    assert(global_worst==465);

    std::cout<<"PASS first-resonance exact support-8 local exclusion\n";
    std::cout<<"raw_support8_paths="<<raw_total<<"\n";
    std::cout<<"phase_candidate_total="<<phase_candidate_total<<"\n";
    std::cout<<"worst_steps_to_below_2^71="<<global_worst<<"\n";
}
