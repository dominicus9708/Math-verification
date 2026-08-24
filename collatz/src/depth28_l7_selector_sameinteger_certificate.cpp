// Exact finite same-integer cross-base certificate at depth 28 after imposing
// aligned L7 locally residue-maximal representatives in all four 7-bit blocks.
//
// IMPORTANT SCOPE: L7 maximality at later blocks is a local language condition;
// this file does not claim root-global later-block exclusion.  Its role is to
// measure exact same-integer selector concentration on that finite language.
//
// Memory: about 0.9 GiB.  Build: g++ -O3 -std=c++17 this_file.cpp -o cert
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using u64=std::uint64_t; using u32=std::uint32_t;
static const std::string H19="1101101101011011010";
static constexpr int L=28,KY=26;
static constexpr u32 YM=1u<<KY,YMASK=YM-1;
struct W7{u32 mask;int q;u64 R;};
std::vector<W7> allowed7;
std::string mech;
std::vector<std::int8_t> height_map,first_map;
u64 language[16][32]{};

u64 invodd(u64 a){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x;}
u64 correction(u32 mask,int len=28,int off=0){u64 R=0;for(int i=0;i<len;i++)if(mask>>i&1u)R=3*R+(1ULL<<(off+i));return R;}

void build_allowed7(){
    std::array<std::map<u64,std::pair<u64,u32>>,8> cls;
    for(u32 mask=0;mask<128;mask++){
        u64 R=0,p3=1;int q=0;
        for(int i=0;i<7;i++)if(mask>>i&1u){R=3*R+(1ULL<<i);q++;}
        for(int i=0;i<q;i++)p3*=3;
        u64 r=R%p3;auto it=cls[q].find(r);
        if(it==cls[q].end()||R>it->second.first)cls[q][r]={R,mask};
    }
    const int expected[8]={1,2,6,15,21,16,7,1};
    for(int q=0;q<=7;q++)if((int)cls[q].size()!=expected[q])std::exit(10);
    for(int q=0;q<=7;q++)for(auto &kv:cls[q])allowed7.push_back({kv.second.second,q,kv.second.first});
    if(allowed7.size()!=69)std::exit(11);
}

void emit(u32 mask,int q,int h,int fp){
    u64 R=correction(mask),p3=1;for(int i=0;i<q;i++)p3*=3;
    u64 inv=invodd(p3)&((1ULL<<28)-1);
    u32 N=(u32)((0ULL-R)*inv)&((1u<<28)-1);
    if((N&3u)!=3u)std::exit(2);
    u32 y=(N-3u)>>2;
    if(height_map[y]!=-1)std::exit(3); // parity-vector injectivity
    height_map[y]=(std::int8_t)h;
    first_map[y]=(std::int8_t)(fp<0?31:fp);
    language[h][first_map[y]]++;
}

void dfs_block(int bidx,int h,int q,u32 mask,int fp){
    if(bidx==4){emit(mask,q,h,fp);return;}
    int off=7*bidx;
    for(const auto&w:allowed7){
        int hh=h,fp2=fp;bool ok=true;
        for(int j=0;j<7;j++){
            int bit=(w.mask>>j)&1u,m=mech[off+j]-'0';
            if(fp2<0&&bit!=m)fp2=off+j;
            hh+=bit-m;if(hh<0){ok=false;break;}
        }
        if(ok)dfs_block(bidx+1,hh,q+w.q,mask|(w.mask<<off),fp2);
    }
}

std::vector<u32> selector_dp(int bits){
    std::vector<u32>dp(YM),nd(YM);dp[0]=1;u32 w=1;
    for(int i=0;i<bits;i++){
        if(i)w=(u64(w)*3)&YMASK;
        for(u32 r=0;r<YM;r++)nd[r]=dp[r]+dp[(r+YM-w)&YMASK];
        dp.swap(nd);
    }
    return dp;
}
using Mat=std::array<std::array<u64,32>,16>;
Mat count_block(const std::vector<u32>&dp,u64 C){
    Mat out{};u32 c=C&YMASK;
    for(u32 s=0;s<YM;s++)if(dp[s]){
        u32 y=(c+s)&YMASK;int h=height_map[y];
        if(h>=0)out[h][first_map[y]]+=dp[s];
    }
    return out;
}
u64 sumall(const Mat&A,const Mat*B=nullptr){u64 z=0;for(int h=0;h<16;h++)for(int p=0;p<32;p++)z+=A[h][p]-(B?(*B)[h][p]:0);return z;}

int main(){
    build_allowed7();mech=(H19+H19).substr(0,L);
    height_map.assign(YM,-1);first_map.assign(YM,-1);
    dfs_block(0,0,0,0,-1);

    const u64 expected_h[11]={116041,289509,277962,185001,93151,35745,10307,2153,305,26,1};
    u64 lang=0;for(int h=0;h<=10;h++){u64 z=0;for(int p=0;p<32;p++)z+=language[h][p];if(z!=expected_h[h])std::exit(4);lang+=z;}
    if(lang!=1010201ULL)std::exit(5);

    auto dp44=selector_dp(44),dp33=selector_dp(33);u64 p44=1;for(int i=0;i<44;i++)p44*=3;
    auto full44=count_block(dp44,p44),low33=count_block(dp33,p44);
    auto a45=count_block(dp44,3*p44),b45=count_block(dp44,4*p44);Mat m45{};
    for(int h=0;h<16;h++)for(int p=0;p<32;p++)m45[h][p]=a45[h][p]+b45[h][p];

    const std::set<int>U44={2,5,8,10,13,16},U45={2,5,8,10};
    u64 s44=sumall(full44,&low33),s45=sumall(m45),u44=0,u45=0,n44=0,n45=0;
    for(int h=0;h<16;h++){
        for(int p:U44)u44+=full44[h][p]-low33[h][p];
        for(int p:U45)u45+=m45[h][p];
    }
    for(int p:U44)n44+=full44[0][p]-low33[0][p];
    for(int p:U45)n45+=m45[0][p];

    if(s44!=264688110351ULL||s45!=529636500458ULL)std::exit(6);
    if(u44!=264650899763ULL||u45!=528441621623ULL)std::exit(7);
    if(n44!=30396266923ULL||n45!=60645599888ULL)std::exit(8);

    const u64 pop44=(1ULL<<44)-(1ULL<<33),pop45=(1ULL<<45);
    // Xi = (selector intersection / selector population) /
    //      (language size / 2^26), since all starts are 3 mod 4.
    __uint128_t x44n=(__uint128_t)s44*(1ULL<<26),x44d=(__uint128_t)pop44*lang;
    __uint128_t x45n=(__uint128_t)s45*(1ULL<<26),x45d=(__uint128_t)pop45*lang;
    if(!(x44n<x44d))std::exit(9);
    // m45 is only 4.504e-7 above 1; certify Xi<1+2^-20 exactly.
    if(!((x45n-x45d)*(1ULL<<20)<x45d))std::exit(12);

    __uint128_t n44n=(__uint128_t)n44*(1ULL<<26),n44d=(__uint128_t)pop44*116041ULL;
    __uint128_t n45n=(__uint128_t)n45*(1ULL<<26),n45d=(__uint128_t)pop45*116041ULL;
    if(!(n44n<n44d&&n45n<n45d))std::exit(13);

    std::cout<<"depth28 L7 selector same-integer certificate: PASS\n";
    std::cout<<"language_total "<<lang<<" neutral "<<116041<<"\n";
    std::cout<<"m44_all "<<s44<<" unresolved "<<u44<<" neutral_unresolved "<<n44<<"\n";
    std::cout<<"m45_all "<<s45<<" unresolved "<<u45<<" neutral_unresolved "<<n45<<"\n";
    std::cout<<"m44_Xi_lt_1 1\n";
    std::cout<<"m45_Xi_lt_1_plus_2^-20 1\n";
}
