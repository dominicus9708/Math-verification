#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// Exact same-integer cross-base transversality certificate for the four
// unresolved m=45 first-defect channels p in {2,5,8,10} at binary depth 28.
//
// Inputs q18.bin,...,q28.bin are the exact retained canonical N residues made
// by depth28_hensel_retained_residue_qslice.cpp.  For each first-defect p this
// verifier:
//   * selects the p-compatible retained dyadic residues;
//   * intersects them with each m=45 ternary affine block by cyclic NTT;
//   * independently counts the raw ternary p-cylinder mass;
//   * compares the aggregate actual hard overlap with the exact overlap that
//     a uniform distribution on the p-compatible dyadic lifts would give.
//
// Result: after aggregating all four unresolved first-defect channels, BOTH
// m=45 affine blocks have actual hard mass strictly BELOW the uniform-dyadic
// prediction.  Thus this finite depth-28 cross-base overlap has no positive
// aggregate transversality/repair bias.
//
// This is a finite transversality certificate for this particular combined
// coefficient-survival + Hensel filter.  It is not yet a recursive
// globalization theorem and is not a proof of the Collatz conjecture.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr u32 MOD_NTT = 2'013'265'921U; // 15*2^27+1
constexpr u32 ROOT = 31U;
constexpr u32 YMOD = 1U << 26;          // N=4Y+3, N modulo 2^28
constexpr u32 YMASK = YMOD - 1;
constexpr u32 MECH_N28 = 163'470'331U;
constexpr std::array<int,4> PS{2,5,8,10};

constexpr std::array<u64,4> ALLOWED{
    1'623'807ULL, 286'895ULL, 51'825ULL, 11'763ULL
};
constexpr std::array<std::array<u64,2>,4> RAW{{
    {{8'796'093'022'208ULL, 8'796'093'022'208ULL}},
    {{1'099'511'627'776ULL, 1'099'511'103'504ULL}},
    {{137'438'953'481ULL, 137'438'887'938ULL}},
    {{34'359'739'317ULL, 34'359'721'961ULL}}
}};
constexpr std::array<std::array<u64,2>,4> HARD{{
    {{425'671'273'258ULL, 425'671'208'248ULL}},
    {{75'207'726'976ULL, 75'207'677'298ULL}},
    {{13'585'605'225ULL, 13'585'629'098ULL}},
    {{3'083'595'585ULL, 3'083'550'671ULL}}
}};

// q=18,...,28 hard-residue counts inside each p-cylinder.
constexpr std::array<std::array<u64,11>,4> QCOUNTS{{
    {{160476,555355,469660,268994,117238,39527,10257,1998,276,25,1}},
    {{29731,101508,83655,45905,18783,5770,1310,210,22,1,0}},
    {{5666,19034,15217,7930,2992,813,153,19,1,0,0}},
    {{1397,4572,3467,1647,542,120,17,1,0,0,0}}
}};

u32 modpow(u32 a, u64 e) {
    u64 r = 1, b = a;
    while (e) {
        if (e & 1) r = r * b % MOD_NTT;
        b = b * b % MOD_NTT;
        e >>= 1;
    }
    return static_cast<u32>(r);
}

void ntt(std::vector<u32>& a, bool inverse) {
    const std::size_t n = a.size();
    for (std::size_t i=1,j=0;i<n;++i) {
        std::size_t bit=n>>1;
        for (; j&bit; bit>>=1) j^=bit;
        j^=bit;
        if (i<j) std::swap(a[i],a[j]);
    }
    for (std::size_t len=2;len<=n;len<<=1) {
        u32 wlen=modpow(ROOT,(MOD_NTT-1)/len);
        if (inverse) wlen=modpow(wlen,MOD_NTT-2);
        const std::size_t half=len>>1;
        for (std::size_t i=0;i<n;i+=len) {
            u64 w=1;
            for (std::size_t j=0;j<half;++j) {
                const u32 u=a[i+j];
                const u32 v=static_cast<u32>(w*a[i+j+half]%MOD_NTT);
                u32 s=u+v; if (s>=MOD_NTT) s-=MOD_NTT;
                a[i+j]=s;
                a[i+j+half]=(u>=v)?(u-v):(u+MOD_NTT-v);
                w=w*wlen%MOD_NTT;
            }
        }
    }
    if (inverse) {
        const u32 invn=modpow(static_cast<u32>(n),MOD_NTT-2);
        for (u32& x:a) x=static_cast<u32>(u64(x)*invn%MOD_NTT);
    }
}

u32 pow3mod(int e,u32 mask) {
    u32 x=1;
    for (int i=0;i<e;++i) x=static_cast<u32>(u64(x)*3U)&mask;
    return x;
}

std::vector<u32> subset_sums_mod(int begin,int end,u32 mask) {
    std::vector<u32> out(1,0);
    out.reserve(std::size_t{1}<<(end-begin));
    u32 w=pow3mod(begin,mask);
    for (int i=begin;i<end;++i) {
        const std::size_t old=out.size();
        out.resize(2*old);
        for (std::size_t j=0;j<old;++j) out[old+j]=(out[j]+w)&mask;
        w=static_cast<u32>(u64(w)*3U)&mask;
    }
    return out;
}

u64 raw_count(int p,bool high44) {
    const u32 M=1U<<(p-1), mask=M-1;
    const u32 lowmask=(1U<<(p+1))-1;
    const u32 targetN=((MECH_N28&lowmask)+(1U<<p))&lowmask;
    const u32 targetY=((targetN-3U)>>2)&mask;

    std::vector<u64> dp(M,0), next;
    u32 base=pow3mod(45,mask);
    if (high44) base=(base+pow3mod(44,mask))&mask;
    dp[base]=1;
    u32 w=1;
    for (int i=0;i<44;++i) {
        next=dp;
        for (u32 r=0;r<M;++r) next[(r+w)&mask]+=dp[r];
        dp.swap(next);
        w=static_cast<u32>(u64(w)*3U)&mask;
    }
    return dp[targetY];
}

std::string s128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) { s.push_back(char('0'+unsigned(x%10))); x/=10; }
    std::reverse(s.begin(),s.end());
    return s;
}

} // namespace

int main(int argc,char** argv) {
    const std::string dir=(argc>=2?argv[1]:".");

    // Load all q-slices once.
    std::array<std::vector<u32>,11> qres;
    for (int q=18;q<=28;++q) {
        const std::string path=dir+"/q"+std::to_string(q)+".bin";
        std::ifstream f(path,std::ios::binary|std::ios::ate);
        if (!f) { std::cerr<<"cannot open "<<path<<"\n"; return 1; }
        const std::streamsize bytes=f.tellg(); f.seekg(0);
        if (bytes%4) return 2;
        auto& v=qres[static_cast<std::size_t>(q-18)];
        v.resize(static_cast<std::size_t>(bytes/4));
        f.read(reinterpret_cast<char*>(v.data()),bytes);
        if (!f) return 3;
    }

    // Transform the low-21 ternary selector multiplicity polynomial once.
    std::vector<u32> lowfft(YMOD,0);
    const auto low=subset_sums_mod(0,21,YMASK);
    for (const u32 x:low) ++lowfft[(-x)&YMASK];
    ntt(lowfft,false);

    const auto high=subset_sums_mod(21,44,YMASK);
    const u32 p45=pow3mod(45,YMASK), p44=pow3mod(44,YMASK);

    std::array<std::array<u64,2>,4> hard{};

    for (std::size_t ip=0;ip<PS.size();++ip) {
        const int p=PS[ip];
        const u32 lowmask=(1U<<(p+1))-1;
        const u32 delta=1U<<p;
        std::vector<u32> work(YMOD,0);
        u64 count=0;

        for (int q=18;q<=28;++q) {
            u64 cq=0;
            for (const u32 x:qres[static_cast<std::size_t>(q-18)]) {
                if (((x-MECH_N28)&lowmask)!=delta) continue;
                assert((x&3U)==3U);
                const u32 y=(x-3U)>>2;
                if (work[y]) return 4;
                work[y]=1;
                ++cq; ++count;
            }
            if (cq!=QCOUNTS[ip][static_cast<std::size_t>(q-18)]) return 5;
        }
        if (count!=ALLOWED[ip]) return 6;

        ntt(work,false);
        for (u32 i=0;i<YMOD;++i)
            work[i]=static_cast<u32>(u64(work[i])*lowfft[i]%MOD_NTT);
        ntt(work,true);

        for (const u32 h:high) {
            const u32 s0=(h+p45)&YMASK;
            const u32 s1=(s0+p44)&YMASK;
            hard[ip][0]+=work[s0];
            hard[ip][1]+=work[s1];
        }

        for (int b=0;b<2;++b) {
            const u64 raw=raw_count(p,b);
            if (raw!=RAW[ip][b]) return 7;
            if (hard[ip][b]!=HARD[ip][b]) return 8;
            std::cout<<"p="<<p<<" block="<<b
                     <<" allowed="<<count
                     <<" raw="<<raw
                     <<" hard="<<hard[ip][b]<<"\n";
        }
    }

    // Exact aggregate transversality comparison.
    // For first defect p, fixing bits 0..p leaves 2^(27-p) dyadic lifts at
    // depth 28.  Uniform-dyadic expected hard mass is therefore
    //   raw_p * ALLOWED_p / 2^(27-p).
    // Put all four terms over the common denominator 2^25:
    //   expected_num = sum raw_p * ALLOWED_p * 2^(p-2).
    // Compare against actual_hard * 2^25 using u128 exactly.
    constexpr u128 DEN=u128(1)<<25;
    const u128 EXPECTED_DIFF[2]={
        u128(2'577'049'406'784ULL),
        u128(5'658'413'153'024ULL)
    };

    for (int b=0;b<2;++b) {
        u128 expected_num=0;
        u128 actual=0;
        u64 raw_total=0;
        for (std::size_t ip=0;ip<PS.size();++ip) {
            const int p=PS[ip];
            expected_num += u128(RAW[ip][b])*ALLOWED[ip]*(u128(1)<<(p-2));
            actual += hard[ip][b];
            raw_total += RAW[ip][b];
        }
        const u128 actual_num=actual*DEN;
        if (!(actual_num<expected_num)) return 9;
        const u128 diff=expected_num-actual_num;
        if (diff!=EXPECTED_DIFF[b]) return 10;

        std::cout<<"aggregate block="<<b
                 <<" raw_total="<<raw_total
                 <<" actual_hard="<<s128(actual)
                 <<" uniform_minus_actual_scaled_2^25="<<s128(diff)
                 <<" aggregate_antibias=PASS\n";
    }

    std::cout<<"m45 remaining depth28 aggregate transversality: PASS\n";
    return 0;
}
