#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

// Exact pointwise / nested mass-transport certificate for the m=45 ternary
// selector distribution through binary depth 28.
//
// Write N=4Y+3 with
//   Y = 3^45 + b 3^44 + sum_{i=0}^{43} a_i 3^i,
// b in {0,1}, a_i in {0,1}.  The free selector sum is computed modulo 2^26.
//
// Main conclusions.
//
// (1) Complete free-selector multiplicities modulo 2^26 lie in
//
//       260110 <= c(r) <= 264167.
//
// (2) At EVERY binary parent in the full selector-mass tree through depth 26,
//     the two child masses obey
//
//       |c0-c1|/(c0+c1) < 1/160.
//
//     The worst parent ratio is exactly 3226/523920 at the final 25->26 split.
//     Hence arbitrary nested binary hard filtering inside this window cannot
//     repair more than 1/160 of a one-child balanced exclusion at any parent.
//
// (3) Conditioning on any of the unresolved first-defect cylinders
//     p in {2,5,8,10} and either m=45 affine block, every individual depth-28
//     lift has density relative to the uniform lift measure strictly below
//
//       129/128.
//
//     Therefore for EVERY subset H of such a cylinder,
//
//       mu(H) < (129/128) nu(H).
//
//     This is hard-set independent.  Since 129^80 < 2*128^80,
//
//       log2( mu(H)/nu(H) ) < 1/80 bit
//
//     whenever the ratio is defined.
//
// Exactness of the NTT convolution is certified before transformation: each
// 22-selector half histogram has maximum multiplicity 4, so every full cyclic
// convolution coefficient is at most 4*2^22=16,777,216, well below the NTT
// prime 2,013,265,921.
//
// This is a finite first-window transversality theorem.  It does not by itself
// control new information appearing beyond binary depth 28 and is not a proof
// of the Collatz conjecture.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

namespace {

constexpr u32 MOD=2'013'265'921U;
constexpr u32 ROOT=31U;
constexpr u32 N=1U<<26;
constexpr u32 MASK=N-1;
constexpr u32 MECH_N28=163'470'331U;
constexpr std::array<int,4> PS{2,5,8,10};

constexpr std::array<std::array<u64,2>,4> RAW{{
    {{8'796'093'022'208ULL,8'796'093'022'208ULL}},
    {{1'099'511'627'776ULL,1'099'511'103'504ULL}},
    {{137'438'953'481ULL,137'438'887'938ULL}},
    {{34'359'739'317ULL,34'359'721'961ULL}}
}};

u32 modpow(u32 a,u64 e){
    u64 r=1,b=a;
    while(e){if(e&1)r=r*b%MOD;b=b*b%MOD;e>>=1;}
    return static_cast<u32>(r);
}

void ntt(std::vector<u32>&a,bool inv){
    const std::size_t n=a.size();
    for(std::size_t i=1,j=0;i<n;++i){
        std::size_t bit=n>>1;
        for(;j&bit;bit>>=1)j^=bit;
        j^=bit;
        if(i<j)std::swap(a[i],a[j]);
    }
    for(std::size_t len=2;len<=n;len<<=1){
        u32 wl=modpow(ROOT,(MOD-1)/len);
        if(inv)wl=modpow(wl,MOD-2);
        const std::size_t half=len>>1;
        for(std::size_t i=0;i<n;i+=len){
            u64 w=1;
            for(std::size_t j=0;j<half;++j){
                const u32 u=a[i+j];
                const u32 v=static_cast<u32>(w*a[i+j+half]%MOD);
                u32 s=u+v;if(s>=MOD)s-=MOD;
                a[i+j]=s;
                a[i+j+half]=(u>=v)?(u-v):(u+MOD-v);
                w=w*wl%MOD;
            }
        }
    }
    if(inv){
        const u32 ni=modpow(static_cast<u32>(n),MOD-2);
        for(u32&x:a)x=static_cast<u32>(u64(x)*ni%MOD);
    }
}

u32 pow3mod(int e){
    u32 x=1;
    for(int i=0;i<e;++i)x=static_cast<u32>(u64(x)*3U)&MASK;
    return x;
}

std::vector<u32> half_hist(int lo,int hi){
    std::vector<u32>h(N,0);
    std::vector<u32>s(std::size_t{1}<<(hi-lo),0);
    u32 w=pow3mod(lo);
    std::size_t cur=1;
    for(int i=lo;i<hi;++i){
        for(std::size_t j=0;j<cur;++j)s[cur+j]=(s[j]+w)&MASK;
        cur*=2;
        w=static_cast<u32>(u64(w)*3U)&MASK;
    }
    for(const u32 x:s)++h[x];
    return h;
}

} // namespace

int main(){
    auto A=half_hist(0,22);
    auto B=half_hist(22,44);
    const u32 maxA=*std::max_element(A.begin(),A.end());
    const u32 maxB=*std::max_element(B.begin(),B.end());
    if(maxA!=4U||maxB!=4U)return 1;
    if(u64(4)*(1ULL<<22)>=MOD)return 2;

    ntt(A,false);ntt(B,false);
    for(u32 i=0;i<N;++i)A[i]=static_cast<u32>(u64(A[i])*B[i]%MOD);
    B.clear();B.shrink_to_fit();
    ntt(A,true);

    u64 total=0;
    u32 mn=UINT32_MAX,mx=0;
    for(const u32 c:A){total+=c;mn=std::min(mn,c);mx=std::max(mx,c);}
    if(total!=(1ULL<<44))return 3;
    if(mn!=260'110U||mx!=264'167U)return 4;

    // Nested local child-imbalance audit.  cur is the exact selector mass at
    // the current Y-modulus depth.  Folding by the high bit gives the parent
    // masses at the next shallower depth.
    std::vector<u64>cur(A.begin(),A.end());
    u64 global_num=0,global_den=1;
    int global_depth=-1;
    for(int d=25;d>=0;--d){
        const std::size_t M=std::size_t{1}<<d;
        std::vector<u64>next(M,0);
        u64 best_num=0,best_den=1;
        for(std::size_t r=0;r<M;++r){
            const u64 c0=cur[r],c1=cur[r+M];
            const u64 den=c0+c1;
            const u64 num=(c0>=c1)?(c0-c1):(c1-c0);
            if(u128(num)*best_den>u128(best_num)*den){
                best_num=num;best_den=den;
            }
            next[r]=den;
        }
        if(u128(best_num)*160>=best_den)return 5;
        if(u128(best_num)*global_den>u128(global_num)*best_den){
            global_num=best_num;global_den=best_den;global_depth=d;
        }
        cur.swap(next);
    }
    if(global_depth!=25||global_num!=3'226ULL||global_den!=523'920ULL)return 6;

    // Pointwise conditional Radon-Nikodym bound for all unresolved p-cylinders.
    const u32 c45=pow3mod(45),c44=pow3mod(44);
    for(std::size_t ip=0;ip<PS.size();++ip){
        const int p=PS[ip];
        const int r=p-1;
        const u32 lowmask=(1U<<r)-1;
        const u32 nmask=(1U<<(p+1))-1;
        const u32 targetN=((MECH_N28&nmask)+(1U<<p))&nmask;
        const u32 targetY=((targetN-3U)>>2)&lowmask;
        const u64 Mp=1ULL<<(26-r);

        for(int b=0;b<2;++b){
            const u32 base=(c45+(b?c44:0U))&MASK;
            u128 raw=0;
            u64 local_max=0;
            for(u64 z=0;z<Mp;++z){
                const u32 y=targetY|(u32(z)<<r);
                const u32 s=(y-base)&MASK;
                raw+=A[s];
                local_max=std::max<u64>(local_max,A[s]);
            }
            if(raw!=RAW[ip][b])return 7;

            // For every point z:
            //   (mu(z)/nu(z)) = c(z)*Mp/raw.
            // Prove the worst point is below 129/128 directly.
            if(u128(local_max)*Mp*128>=u128(129)*raw)return 8;

            std::cout<<"p="<<p<<" block="<<b
                     <<" pointwise_density_ratio<129/128 PASS\n";
        }
    }

    cpp_int p129=1,p128=1;
    for(int i=0;i<80;++i){p129*=129;p128*=128;}
    if(!(p129<2*p128))return 9;

    std::cout<<"global selector multiplicity range="<<mn<<".."<<mx<<"\n";
    std::cout<<"worst nested child imbalance="<<global_num<<"/"<<global_den
             <<" at parent depth "<<global_depth<<"\n";
    std::cout<<"all nested child imbalances < 1/160\n";
    std::cout<<"all p-cylinder pointwise density ratios < 129/128\n";
    std::cout<<"hard-set-independent one-window repair budget < 1/80 bit\n";
    std::cout<<"m45 depth28 local mass transport: PASS\n";
    return 0;
}
