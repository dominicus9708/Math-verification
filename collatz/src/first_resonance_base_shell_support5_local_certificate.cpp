#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

static constexpr uint64_t A = 114208327604ULL;
static constexpr uint64_t Q = 72057431991ULL;
static constexpr uint64_t P = A - Q;
static constexpr int GAPLEN = 48;
static constexpr int ODDS = 49;
static constexpr int K = 73;
static constexpr int MAXSUP = 5;

struct Mask73 { uint64_t lo; uint16_t hi; bool operator==(const Mask73& o) const { return lo==o.lo && hi==o.hi; } };
struct MaskHash { size_t operator()(const Mask73& m) const noexcept { return std::hash<uint64_t>{}(m.lo ^ (uint64_t(m.hi)*0x9e3779b97f4a7c15ULL)); } };

static inline Mask73 setbit(Mask73 m,int i){ if(i<64)m.lo|=1ULL<<i; else m.hi|=uint16_t(1U<<(i-64)); return m; }
static inline bool getbit(Mask73 m,int i){ return i<64 ? ((m.lo>>i)&1ULL) : ((m.hi>>(i-64))&1U); }
static inline u128 mask73(){ return (((u128)1)<<73)-1; }

static std::string u128s(u128 x){ if(!x)return "0"; std::string s; while(x){s.push_back(char('0'+x%10));x/=10;} std::reverse(s.begin(),s.end()); return s; }
static u128 inv_odd_pow2(u128 a){ u128 x=1; for(int i=0;i<8;++i)x=x*(2-a*x); return x&mask73(); }

static std::vector<std::array<int,GAPLEN>> gap_factors(){
    std::vector<uint64_t> bp;
    for(int j=0;j<=GAPLEN;++j){
        uint64_t rem=uint64_t(((u128)j*P)%Q);
        bp.push_back(rem?Q-rem:0);
    }
    std::sort(bp.begin(),bp.end()); bp.erase(std::unique(bp.begin(),bp.end()),bp.end());
    assert(bp.size()==49);
    std::vector<std::array<int,GAPLEN>> out;
    for(uint64_t r:bp){
        std::array<int,GAPLEN> g{}; uint64_t rr=r;
        for(int j=0;j<GAPLEN;++j){
            int bit=(rr>=Q-P)?1:0; g[j]=1+bit; rr=bit?rr+P-Q:rr+P;
        }
        bool dup=false; for(const auto& x:out) if(x==g){dup=true;break;}
        if(!dup) out.push_back(g);
    }
    assert(out.size()==49); return out;
}

int main(){
    const auto factors=gap_factors();
    std::unordered_set<Mask73,MaskHash> masks; masks.reserve(8500000);
    uint64_t raw=0; std::array<int,ODDS> d{};
    for(const auto& g:factors){
        d.fill(0);
        auto dfs=[&](auto&& self,int i,int supp)->void{
            if(i==ODDS){
                ++raw; int pos=0; Mask73 m{1,0};
                for(int j=1;j<ODDS;++j){ pos+=g[j-1]+d[j-1]-d[j]; if(pos<K)m=setbit(m,pos); }
                assert(pos>=72); masks.insert(m); return;
            }
            int maxd=d[i-1]+g[i-1]-1;
            for(int x=0;x<=maxd;++x){ int ns=supp+(x>0); if(ns>MAXSUP)continue; d[i]=x; self(self,i+1,ns); }
        };
        dfs(dfs,1,0);
    }
    assert(raw==11642760ULL);
    assert(masks.size()==7607777ULL);

    const u128 MOD=((u128)1)<<73, MM=MOD-1, B=((u128)1)<<71;
    u128 inv3=inv_odd_pow2(3), inv3pow[74]; inv3pow[0]=1;
    for(int q=1;q<74;++q)inv3pow[q]=(inv3pow[q-1]*inv3)&MM;

    std::vector<u128> cands; cands.reserve(3200000);
    for(const auto&m:masks){
        u128 R=0; int q=0;
        for(int i=0;i<K;++i) if(getbit(m,i)){ R=(3*R+(((u128)1)<<i))&MM; ++q; }
        u128 r=((MOD-R)&MM); r=(r*inv3pow[q])&MM;
        if(r>B && 3*r<8*B)cands.push_back(r);
    }
    assert(cands.size()==3170816ULL);

    cpp_int BB=cpp_int(1); BB<<=71;
    int worst=-1; u128 arg=0;
    for(u128 n:cands){
        cpp_int x=uint64_t(n>>64); x<<=64; x+=uint64_t(n);
        int s=0;
        while(x>=BB && s<=1000){ if((x&1)!=0)x=(3*x+1)>>1; else x>>=1; ++s; }
        assert(x<BB);
        if(s>worst){worst=s;arg=n;}
    }
    assert(worst==367);
    assert(uint64_t(arg>>64)==145ULL);
    assert(uint64_t(arg)==15079730633704974203ULL);

    std::cout<<"PASS first-resonance base-shell support<=5 local exclusion\n";
    std::cout<<"gap_factors="<<factors.size()<<"\n";
    std::cout<<"raw_paths="<<raw<<"\n";
    std::cout<<"unique_parity_words="<<masks.size()<<"\n";
    std::cout<<"canonical_shell_candidates="<<cands.size()<<"\n";
    std::cout<<"worst_steps_to_below_2^71="<<worst<<"\n";
    std::cout<<"worst_start="<<u128s(arg)<<"\n";
}
