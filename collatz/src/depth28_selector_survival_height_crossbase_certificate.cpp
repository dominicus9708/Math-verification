// Exact same-integer cross-base certificate at the first 28 time bits of the
// current R1 mechanical phase.
//
// It exhausts the entire coefficient-surviving parity language relative to
// the exact first-28 mechanical word, reconstructs each canonical start residue
// modulo 2^28, and intersects those residues with exact cyclic subset-sum
// multiplicities of the recursively-sufficient ternary selector blocks.
//
// This is finite evidence / a finite class theorem only.  No independence or
// repeated-window claim is made.
//
// Memory: about 1 GiB with the implementation below.
// Build: g++ -O3 -std=c++17 depth28_selector_survival_height_crossbase_certificate.cpp -o cert

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
static constexpr int L=28, KY=26;
static constexpr u32 YM=1u<<KY, YMASK=YM-1;
std::string mech;
std::vector<std::int8_t> height_map, first_map;
u64 language[16][32]{};

u64 invodd(u64 a){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x;}
u64 correction(u32 mask){u64 R=0;for(int i=0;i<L;i++)if(mask>>i&1u)R=3*R+(1ULL<<i);return R;}

void emit(u32 mask,int q,int h,int fp){
    u64 R=correction(mask),p3=1; for(int i=0;i<q;i++)p3*=3;
    u64 inv=invodd(p3)&((1ULL<<28)-1);
    u32 N=(u32)((0ULL-R)*inv)&((1u<<28)-1);
    if((N&3u)!=3u) std::exit(2);
    u32 y=(N-3u)>>2;
    if(height_map[y]!=-1) std::exit(3); // parity-vector bijection audit
    height_map[y]=(std::int8_t)h;
    first_map[y]=(std::int8_t)(fp<0?31:fp);
    language[h][first_map[y]]++;
}

void dfs(int i,int h,int q,u32 mask,int fp){
    if(i==L){emit(mask,q,h,fp);return;}
    int m=mech[i]-'0';
    for(int bit=0;bit<=1;bit++){
        int h2=h+bit-m; if(h2<0) continue;
        int fp2=fp; if(fp2<0 && bit!=m) fp2=i;
        dfs(i+1,h2,q+bit,mask|(u32(bit)<<i),fp2);
    }
}

std::vector<u32> selector_dp(int bits){
    std::vector<u32> dp(YM),nd(YM); dp[0]=1; u32 w=1;
    for(int i=0;i<bits;i++){
        if(i)w=(u64(w)*3)&YMASK;
        for(u32 r=0;r<YM;r++) nd[r]=dp[r]+dp[(r+YM-w)&YMASK];
        dp.swap(nd);
    }
    return dp;
}

using Mat=std::array<std::array<u64,32>,16>;
Mat count_block(const std::vector<u32>&dp,u64 C){
    Mat out{}; u32 c=C&YMASK;
    for(u32 s=0;s<YM;s++) if(dp[s]){
        u32 y=(c+s)&YMASK; int h=height_map[y];
        if(h>=0) out[h][first_map[y]]+=dp[s];
    }
    return out;
}

u64 total_mat(const Mat&A,const Mat*B=nullptr){
    u64 z=0; for(int h=0;h<16;h++)for(int p=0;p<32;p++)z+=A[h][p]-(B?(*B)[h][p]:0); return z;
}

int main(){
    mech=(H19+H19).substr(0,L);
    height_map.assign(YM,-1); first_map.assign(YM,-1);
    dfs(0,0,0,0,-1);

    const u64 expected_lang[11]={663535,1236935,898798,464889,185684,57923,13953,2520,322,26,1};
    u64 lang_total=0;
    for(int h=0;h<=10;h++){
        u64 z=0;for(int p=0;p<32;p++)z+=language[h][p];
        if(z!=expected_lang[h]) std::exit(4); lang_total+=z;
    }
    if(lang_total!=3524586) std::exit(5);

    auto dp44=selector_dp(44), dp33=selector_dp(33);
    u64 p44=1;for(int i=0;i<44;i++)p44*=3;
    auto full44=count_block(dp44,p44);
    auto low33=count_block(dp33,p44);
    auto a45=count_block(dp44,3*p44);
    auto b45=count_block(dp44,4*p44);
    Mat m45{};
    for(int h=0;h<16;h++)for(int p=0;p<32;p++)m45[h][p]=a45[h][p]+b45[h][p];

    u64 surv44=total_mat(full44,&low33), surv45=total_mat(m45);
    if(surv44!=923497419313ULL) std::exit(6);
    if(surv45!=1847897870486ULL) std::exit(7);

    if(full44[0][2]-low33[0][2]!=141896844483ULL) std::exit(8);
    if(full44[0][5]-low33[0][5]!=25749886299ULL) std::exit(9);
    if(full44[0][8]-low33[0][8]!=4797005339ULL) std::exit(10);
    if(full44[0][10]-low33[0][10]!=1139258856ULL) std::exit(11);
    if(full44[0][13]-low33[0][13]!=216683050ULL) std::exit(12);
    if(full44[0][16]-low33[0][16]!=42708985ULL) std::exit(13);

    if(m45[0][2]!=283932835442ULL) std::exit(14);
    if(m45[0][5]!=51525023749ULL) std::exit(15);
    if(m45[0][8]!=9598623667ULL) std::exit(16);
    if(m45[0][10]!=2279581725ULL) std::exit(17);

    const std::set<int> U44={2,5,8,10,13,16}, U45={2,5,8,10};
    u64 unresolved44=0,unresolved45=0,neutral44=0,neutral45=0;
    for(int h=0;h<16;h++){
        for(int p:U44) unresolved44+=full44[h][p]-low33[h][p];
        for(int p:U45) unresolved45+=m45[h][p];
    }
    for(int p:U44) neutral44+=full44[0][p]-low33[0][p];
    for(int p:U45) neutral45+=m45[0][p];

    if(unresolved44!=923446059910ULL) std::exit(18);
    if(unresolved45!=1845541690295ULL) std::exit(19);
    if(neutral44!=173842387012ULL) std::exit(20);
    if(neutral45!=347336064583ULL) std::exit(21);

    std::cout<<"depth28 selector/survival/height cross-base: PASS\n";
    std::cout<<"language_total "<<lang_total<<"\n";
    for(int h=0;h<=10;h++){u64 z=0;for(int p=0;p<32;p++)z+=language[h][p];std::cout<<"language_h"<<h<<" "<<z<<"\n";}
    std::cout<<"m44_current_survival "<<surv44<<"\n";
    std::cout<<"m45_two_block_survival "<<surv45<<"\n";
    std::cout<<"m44_unresolved_p_survival "<<unresolved44<<"\n";
    std::cout<<"m45_unresolved_p_survival "<<unresolved45<<"\n";
    std::cout<<"m44_neutral_unresolved_p "<<neutral44<<"\n";
    std::cout<<"m45_neutral_unresolved_p "<<neutral45<<"\n";
}
