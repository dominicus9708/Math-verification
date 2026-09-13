#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using u64=std::uint64_t;
struct Row{cpp_int a,b; u64 m; u64 amod,bmod; int qs;};
static constexpr int D=22;
static constexpr u64 MOD=1ULL<<D;
static constexpr u64 MASK=MOD-1;
static constexpr u64 EXPECT_ROWS=605977;
static constexpr u64 EXPECT_MASS=3419719061560ULL;
static constexpr u64 EXPECT_SAFE=2904383883175ULL;
static constexpr u64 EXPECT_TAIL=515335178385ULL;
static const cpp_int LO=cpp_int(1)<<71;

static cpp_int parse_big(const std::string&s){cpp_int x=0;for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=(c-'0');}return x;}
static u64 mod_u64(const cpp_int&x,u64 mod){return (x % mod).convert_to<u64>();}
static u64 inv_odd_pow2(u64 a){assert(a&1); u64 x=a; for(int i=0;i<6;i++) x*=2-a*x; return x & MASK;}
static int qsafe(const cpp_int&N){
    int best=-1;
    for(int q=0;q<=D;q++){
        cpp_int cmax=0;
        if(q) cmax=(cpp_int(1)<<(D-q))*(pow(cpp_int(3),q)-(cpp_int(1)<<q));
        cpp_int lhs=pow(cpp_int(3),q)*N+cmax;
        cpp_int rhs=(cpp_int(1)<<D)*LO;
        if(lhs<=rhs) best=q; else break;
    }
    return best;
}
static int odd_count(u64 n){int q=0; u64 x=n; for(int i=0;i<D;i++){if(x&1){q++; x=(3*x+1)/2;}else x/=2;} return q;}
static u64 cyclic_count(const std::vector<uint32_t>&pref,u64 shift,u64 len){
    if(len==0) return 0; u64 end=shift+len; if(end<=MOD) return pref[end]-pref[shift];
    return (pref[MOD]-pref[shift])+pref[end-MOD];
}
int main(int argc,char**argv){
    if(argc!=2){std::cerr<<"usage: math127 source.tsv\n";return 2;}
    std::ifstream in(argv[1]); assert(in);
    std::vector<Row> rows; rows.reserve(EXPECT_ROWS); u64 total=0; std::map<u64,std::vector<size_t>> groups; std::map<int,u64> qhist;
    std::string as,bs;u64 m; cpp_int maxN=0;
    while(in>>as>>bs>>m){
        cpp_int a=parse_big(as),b=parse_big(bs); assert(b>0 && (b&1)!=0 && m>0);
        cpp_int N=a+b*(m-1); int qs=qsafe(N); assert(qs==12||qs==13); qhist[qs]++;
        size_t idx=rows.size(); rows.push_back({a,b,m,mod_u64(a,MOD),mod_u64(b,MOD),qs}); groups[rows.back().bmod].push_back(idx);
        total+=m; if(N>maxN)maxN=N;
    }
    assert(rows.size()==EXPECT_ROWS); assert(total==EXPECT_MASS); assert(groups.size()==32);
    std::vector<uint8_t> qval(MOD); for(u64 r=0;r<MOD;r++) qval[r]=odd_count(r);
    u64 safe=0;
    for(auto &kv:groups){
        u64 bmod=kv.first, inv=inv_odd_pow2(bmod);
        std::vector<uint32_t> p12(MOD+1),p13(MOD+1);
        for(u64 k=0;k<MOD;k++){
            int q=qval[(bmod*k)&MASK];
            p12[k+1]=p12[k]+(q<=12); p13[k+1]=p13[k]+(q<=13);
        }
        assert(p12[MOD]==3096514); assert(p13[MOD]==3593934);
        for(size_t idx:kv.second){auto&r=rows[idx]; u64 cycles=r.m/MOD, rem=r.m%MOD; u64 shift=(r.amod*inv)&MASK;
            const auto &p=(r.qs==12?p12:p13); u64 sc=cycles*(u64)p[MOD]+cyclic_count(p,shift,rem); safe+=sc;
        }
    }
    std::cout<<"rows\t"<<rows.size()<<"\n";
    std::cout<<"total_mass\t"<<total<<"\n";
    std::cout<<"distinct_b_mod_2pow22\t"<<groups.size()<<"\n";
    std::cout<<"q_safe_12_pieces\t"<<qhist[12]<<"\n";
    std::cout<<"q_safe_13_pieces\t"<<qhist[13]<<"\n";
    std::cout<<"exact_d22_safe_mass\t"<<safe<<"\n";
    std::cout<<"exact_d22_tail_mass\t"<<(total-safe)<<"\n";
    std::cout<<"max_N\t"<<maxN<<"\n";
    assert(safe==EXPECT_SAFE); assert(total-safe==EXPECT_TAIL);
    std::cerr<<"PASS MATH-127 exact d22 remainder-aware q-gate audit\nNO r=11 CLOSURE CLAIM\n";
}
