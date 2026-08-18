#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

// Exact hard-set-independent transversality certificate for the four remaining
// m=45 first-defect cylinders p in {2,5,8,10} at binary depth 28.
//
// Let
//   N = 4(3^45 + b 3^44 + sum_{i=0}^{43} a_i 3^i) + 3,
// with b in {0,1} and a_i in {0,1}. Conditioning on first defect p fixes
// N modulo 2^(p+1), equivalently Y=(N-3)/4 modulo 2^(p-1). The remaining
// depth-28 dyadic lift coordinate has size M_p=2^(27-p).
//
// The complete 44-selector subset-sum distribution modulo 2^26 is obtained by
// cyclic NTT convolution of two exact 22-selector histograms. Each half
// histogram has maximum multiplicity exactly 4, so every full convolution
// coefficient is at most 4*2^22=16,777,216, strictly below the NTT prime.
// Thus the inverse-NTT coefficients are certified ordinary integers rather
// than merely residues modulo the NTT prime.
//
// For each (p,b), the exact total-variation distance between the conditional
// selector distribution mu_{p,b} and the uniform distribution nu_p satisfies
//
//     TV(mu_{p,b},nu_p) < 1/1600.
//
// The p-compatible depth-28 coefficient+Hensel hard fractions certified in the
// companion q-sliced calculation satisfy u_p=A_p/M_p >= 3/64. Therefore for
// ANY hard subset H of the p-cylinder with uniform fraction at least 3/64,
//
//     mu_{p,b}(H)/nu_p(H)
//       <= 1 + TV/u_p
//       < 1 + (1/1600)/(3/64)
//       = 76/75.
//
// Since 76^50 < 2*75^50, log_2(76/75) < 1/50 bit. Hence one depth-28
// cross-base hard-set correlation can repair less than 0.02 bit in every
// remaining m=45 first-defect cylinder, independently of the hard-set geometry.
//
// This is a finite one-window theorem. It does NOT justify repeating the same
// bound after arbitrary later conditioning, and it is not a proof of Collatz.

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

namespace {

constexpr u32 MOD = 2'013'265'921U; // 15*2^27+1
constexpr u32 ROOT = 31U;
constexpr int L = 26;
constexpr u32 N = 1U << L;
constexpr u32 MASK = N - 1;
constexpr u32 MECH_N28 = 163'470'331U;
constexpr std::array<int,4> PS{2,5,8,10};
constexpr std::array<u64,4> HARD_CARD{
    1'623'807ULL, 286'895ULL, 51'825ULL, 11'763ULL
};

struct Expected {
    int p;
    int block;
    u64 raw;
    u64 min_count;
    u64 max_count;
    u64 tv_num;
};

const std::array<Expected,8> EXPECTED{{
    {2,0,8'796'093'022'208ULL,260'113ULL,264'163ULL,352'117'077'839'970'304ULL},
    {2,1,8'796'093'022'208ULL,260'110ULL,264'167ULL,352'101'617'299'881'984ULL},
    {5,0,1'099'511'627'776ULL,260'183ULL,264'082ULL,5'502'289'305'403'392ULL},
    {5,1,1'099'511'103'504ULL,260'206ULL,264'151ULL,5'501'887'494'144'160ULL},
    {8,0,137'438'953'481ULL,260'260ULL,263'912ULL,85'957'936'677'836ULL},
    {8,1,137'438'887'938ULL,260'354ULL,263'954ULL,86'055'322'907'416ULL},
    {10,0,34'359'739'317ULL,260'308ULL,263'764ULL,5'369'573'154'106ULL},
    {10,1,34'359'721'961ULL,260'367ULL,263'965ULL,5'366'750'776'560ULL},
}};

u32 modpow(u32 a,u64 e) {
    u64 r=1,b=a;
    while(e){ if(e&1) r=r*b%MOD; b=b*b%MOD; e>>=1; }
    return static_cast<u32>(r);
}

void ntt(std::vector<u32>& a,bool inverse) {
    const std::size_t n=a.size();
    for(std::size_t i=1,j=0;i<n;++i){
        std::size_t bit=n>>1;
        for(;j&bit;bit>>=1) j^=bit;
        j^=bit;
        if(i<j) std::swap(a[i],a[j]);
    }
    for(std::size_t len=2;len<=n;len<<=1){
        u32 wlen=modpow(ROOT,(MOD-1)/len);
        if(inverse) wlen=modpow(wlen,MOD-2);
        const std::size_t half=len>>1;
        for(std::size_t i=0;i<n;i+=len){
            u64 w=1;
            for(std::size_t j=0;j<half;++j){
                const u32 u=a[i+j];
                const u32 v=static_cast<u32>(w*a[i+j+half]%MOD);
                u32 s=u+v; if(s>=MOD) s-=MOD;
                a[i+j]=s;
                a[i+j+half]=(u>=v)?(u-v):(u+MOD-v);
                w=w*wlen%MOD;
            }
        }
    }
    if(inverse){
        const u32 invn=modpow(static_cast<u32>(n),MOD-2);
        for(u32& x:a) x=static_cast<u32>(u64(x)*invn%MOD);
    }
}

u32 pow3mod(int e) {
    u32 x=1;
    for(int i=0;i<e;++i) x=static_cast<u32>(u64(x)*3U)&MASK;
    return x;
}

std::vector<u32> half_histogram(int lo,int hi) {
    std::vector<u32> h(N,0);
    const std::size_t count=std::size_t{1}<<(hi-lo);
    std::vector<u32> sums(count,0);
    u32 w=pow3mod(lo);
    std::size_t cur=1;
    for(int i=lo;i<hi;++i){
        for(std::size_t j=0;j<cur;++j) sums[cur+j]=(sums[j]+w)&MASK;
        cur*=2;
        w=static_cast<u32>(u64(w)*3U)&MASK;
    }
    for(const u32 x:sums) ++h[x];
    return h;
}

u32 histogram_max(const std::vector<u32>& h) {
    return *std::max_element(h.begin(),h.end());
}

std::string s128(u128 x) {
    if(!x) return "0";
    std::string s;
    while(x){ s.push_back(char('0'+unsigned(x%10))); x/=10; }
    std::reverse(s.begin(),s.end());
    return s;
}

} // namespace

int main() {
    auto A=half_histogram(0,22);
    auto B=half_histogram(22,44);

    const u32 maxA=histogram_max(A);
    const u32 maxB=histogram_max(B);
    if(maxA!=4U || maxB!=4U) return 1;
    const u64 exact_coefficient_upper=
        std::min<u64>(u64(maxA)*(1ULL<<22),u64(maxB)*(1ULL<<22));
    if(exact_coefficient_upper>=MOD) return 2;

    ntt(A,false);
    ntt(B,false);
    for(u32 i=0;i<N;++i) A[i]=static_cast<u32>(u64(A[i])*B[i]%MOD);
    B.clear(); B.shrink_to_fit();
    ntt(A,true);

    u64 total=0;
    u32 global_min=UINT32_MAX, global_max=0;
    for(const u32 c:A){
        total+=c;
        global_min=std::min(global_min,c);
        global_max=std::max(global_max,c);
    }
    if(total!=(1ULL<<44)) return 3;
    if(global_min!=260'110U || global_max!=264'167U) return 4;
    if(global_max>exact_coefficient_upper) return 5;

    const u32 c45=pow3mod(45);
    const u32 c44=pow3mod(44);

    std::size_t ei=0;
    for(std::size_t ip=0;ip<PS.size();++ip){
        const int p=PS[ip];
        const u32 r=p-1;
        const u32 lowmask=(1U<<r)-1;
        const u32 nlowmask=(1U<<(p+1))-1;
        const u32 targetN=((MECH_N28&nlowmask)+(1U<<p))&nlowmask;
        const u32 targetY=((targetN-3U)>>2)&lowmask;
        const u64 Mp=1ULL<<(26-r); // 2^(27-p)

        // Uniform hard fraction u_p=A_p/M_p is at least 3/64 exactly.
        if(u128(HARD_CARD[ip])*64 < u128(3)*Mp) return 6;

        for(int block=0;block<2;++block,++ei){
            const Expected& e=EXPECTED[ei];
            if(e.p!=p || e.block!=block) return 7;
            const u32 base=(c45+(block?c44:0U))&MASK;

            u128 raw=0;
            u64 minc=UINT64_MAX,maxc=0;
            for(u64 z=0;z<Mp;++z){
                const u32 y=targetY | (u32(z)<<r);
                const u32 s=(y-base)&MASK;
                const u64 c=A[s];
                raw+=c;
                minc=std::min(minc,c);
                maxc=std::max(maxc,c);
            }

            u128 l1num=0;
            for(u64 z=0;z<Mp;++z){
                const u32 y=targetY | (u32(z)<<r);
                const u32 s=(y-base)&MASK;
                const u128 scaled=u128(A[s])*Mp;
                l1num += (scaled>=raw)?(scaled-raw):(raw-scaled);
            }
            const u128 tvden=u128(2)*raw*Mp;

            if(raw!=e.raw || minc!=e.min_count || maxc!=e.max_count) return 8;
            if(l1num!=u128(e.tv_num)) return 9;

            // TV = l1num/tvden < 1/1600.
            if(u128(1600)*l1num>=tvden) return 10;

            std::cout<<"p="<<p<<" block="<<block
                     <<" raw="<<s128(raw)
                     <<" min="<<minc<<" max="<<maxc
                     <<" TV<1/1600 PASS\n";
        }
    }

    // Exact repair-bit consequence: Xi<76/75 and log2(Xi)<1/50.
    cpp_int p76=1,p75=1;
    for(int i=0;i<50;++i){ p76*=76; p75*=75; }
    if(!(p76<2*p75)) return 11;

    std::cout<<"half-histogram max multiplicities="<<maxA<<","<<maxB<<"\n";
    std::cout<<"full-coefficient certified upper="<<exact_coefficient_upper<<"\n";
    std::cout<<"uniform hard-set relative overlap Xi < 76/75\n";
    std::cout<<"one-window repair budget log2(Xi) < 1/50 bit\n";
    std::cout<<"m45 depth28 hard-set-independent transversality: PASS\n";
    return 0;
}
