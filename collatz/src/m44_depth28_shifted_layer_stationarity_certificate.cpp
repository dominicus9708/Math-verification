// Exact depth-28 same-integer survival profile on each remaining shifted m=44 selector layer.
//
// The current m=44 core after the certified A_33 prefix block is the disjoint union
// over d=33,...,43 of
//   {4(3^44 + 3^d + sum_{i<d} a_i 3^i)+3 : a_i in {0,1}}.
//
// This certificate reuses the exact first-28 mechanical-relative coefficient-survival
// language and exact cyclic ternary subset-sum multiplicities modulo 2^26.  It reports
// the full survival fraction, the previously unresolved first-defect fraction, and the
// unresolved neutral-return fraction on every shifted layer.  The aggregate is asserted
// against the earlier whole-current-core certificate.
//
// Build: g++ -O3 -std=c++17 m44_depth28_shifted_layer_stationarity_certificate.cpp -o cert

#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using u64=std::uint64_t; using u32=std::uint32_t;
static const std::string H19="1101101101011011010";
static constexpr int L=28, KY=26;
static constexpr u32 YM=1u<<KY, YMASK=YM-1;
std::string mech;
std::vector<std::int8_t> height_map, first_map;

u64 invodd(u64 a){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x;}
u64 correction(u32 mask){u64 R=0;for(int i=0;i<L;i++)if(mask>>i&1u)R=3*R+(1ULL<<i);return R;}

void emit(u32 mask,int q,int h,int fp){
    u64 R=correction(mask),p3=1;for(int i=0;i<q;i++)p3*=3;
    u64 inv=invodd(p3)&((1ULL<<28)-1);
    u32 N=(u32)((0ULL-R)*inv)&((1u<<28)-1);
    if((N&3u)!=3u)std::exit(2);
    u32 y=(N-3u)>>2;
    if(height_map[y]!=-1)std::exit(3);
    height_map[y]=(std::int8_t)h;
    first_map[y]=(std::int8_t)(fp<0?31:fp);
}

void dfs(int i,int h,int q,u32 mask,int fp){
    if(i==L){emit(mask,q,h,fp);return;}
    int m=mech[i]-'0';
    for(int bit=0;bit<=1;bit++){
        int h2=h+bit-m;if(h2<0)continue;
        int fp2=fp;if(fp2<0&&bit!=m)fp2=i;
        dfs(i+1,h2,q+bit,mask|(u32(bit)<<i),fp2);
    }
}

void dp_step(std::vector<u32>&dp,std::vector<u32>&nd,u32 w){
    for(u32 r=0;r<YM;r++)nd[r]=dp[r]+dp[(r+YM-w)&YMASK];
    dp.swap(nd);
}

struct Counts{u64 survival=0,unresolved=0,neutral=0;};

Counts count_layer(const std::vector<u32>&dp,u64 C){
    static const std::set<int> U={2,5,8,10,13,16};
    Counts out;u32 c=C&YMASK;
    for(u32 s=0;s<YM;s++){
        u32 mult=dp[s];if(!mult)continue;
        u32 y=(c+s)&YMASK;
        int h=height_map[y];if(h<0)continue;
        int p=first_map[y];
        out.survival+=mult;
        if(U.count(p)){
            out.unresolved+=mult;
            if(h==0)out.neutral+=mult;
        }
    }
    return out;
}

int main(){
    mech=(H19+H19).substr(0,L);
    height_map.assign(YM,-1);first_map.assign(YM,-1);
    dfs(0,0,0,0,-1);

    std::vector<u32>dp(YM),nd(YM);dp[0]=1;u32 w=1;
    // Build the 33-free-digit selector convolution.
    for(int i=0;i<33;i++){
        if(i)w=(u64(w)*3)&YMASK;
        dp_step(dp,nd,w);
    }

    u64 p44=1;for(int i=0;i<44;i++)p44*=3ULL;
    u64 pd=1;for(int i=0;i<33;i++)pd*=3ULL;
    u64 sumS=0,sumU=0,sumN=0;

    std::cout<<std::setprecision(15);
    for(int d=33;d<=43;d++){
        if(d>33)pd*=3ULL;
        Counts c=count_layer(dp,p44+pd);
        u64 size=1ULL<<d;
        std::cout<<"d "<<d
                 <<" size "<<size
                 <<" survival "<<c.survival
                 <<" frac "<<(long double)c.survival/size
                 <<" unresolved "<<c.unresolved
                 <<" ufrac "<<(long double)c.unresolved/size
                 <<" neutral "<<c.neutral
                 <<" nfrac "<<(long double)c.neutral/size<<"\n";
        sumS+=c.survival;sumU+=c.unresolved;sumN+=c.neutral;
        if(d<43){w=(u64(w)*3)&YMASK;dp_step(dp,nd,w);}
    }

    if(sumS!=923497419313ULL)std::exit(4);
    if(sumU!=923446059910ULL)std::exit(5);
    if(sumN!=173842387012ULL)std::exit(6);

    std::cout<<"sum survival "<<sumS
             <<" unresolved "<<sumU
             <<" neutral "<<sumN<<"\n";
}
