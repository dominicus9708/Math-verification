#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

// Exact depth-28 renewal diagnostic for the unresolved m=45 first-defect hard
// language.  Input q18.bin,...,q28.bin are the exact retained canonical N
// residues produced by depth28_hensel_retained_residue_qslice.cpp.
//
// For a first defect at a mechanical zero p, define the relative height as the
// cumulative actual-minus-mechanical odd count from p onward.  If it returns to
// zero immediately at p+1, the local 01 mechanical pair has been replaced by
// 10.  For a fixed suffix this changes the canonical start residue by
//
//   d_p = 2^p * 3^(-(q_before(p)+1)) mod 2^28.
//
// The verifier proves exact translated-set renewal identities for the retained
// depth-28 hard language:
//
// * p=2, immediate return at 3: after subtracting d_2, each class classified
//   by its next first defect is EXACTLY the corresponding later first-defect
//   retained hard set (including the no-further-defect class);
// * p=5, immediate return at 6: the same exact renewal identity holds;
// * p=10, immediate return at 11: the same identity holds for later defects;
// * p=8 is explicitly recorded as the exceptional transition: its immediate
//   return / next-p=10 class has 14443 retained residues, whereas the ordinary
//   p=10 hard set has 11763, so Hensel retention is not conjugate there.
//
// This is a structural compression of the finite hard language, not a transfer
// theorem for the m=45 ternary selector mass and not a proof of Collatz.

using u32=std::uint32_t;
using u64=std::uint64_t;

namespace {

constexpr int L=28;
constexpr u32 MOD=1U<<L;
constexpr u32 MASK=MOD-1;
const std::string H19="1101101101011011010";

std::string mechanical(){
    std::string s;
    while(static_cast<int>(s.size())<L)s+=H19;
    s.resize(L);
    return s;
}

std::vector<u32> load_all(const std::string& dir){
    std::vector<u32> out;
    for(int q=18;q<=28;++q){
        const std::string path=dir+"/q"+std::to_string(q)+".bin";
        std::ifstream f(path,std::ios::binary|std::ios::ate);
        if(!f){std::cerr<<"cannot open "<<path<<"\n";std::exit(1);}
        const std::streamsize bytes=f.tellg();f.seekg(0);
        if(bytes%4)std::exit(2);
        const std::size_t old=out.size();
        out.resize(old+static_cast<std::size_t>(bytes/4));
        f.read(reinterpret_cast<char*>(out.data()+old),bytes);
        if(!f)std::exit(3);
    }
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    return out;
}

std::vector<int> parity(u32 r){
    u64 x=r;
    std::vector<int>b(L);
    for(int i=0;i<L;++i){
        b[i]=static_cast<int>(x&1ULL);
        x=b[i]?(3*x+1)/2:x/2;
    }
    return b;
}

int first_defect(const std::vector<int>&b,const std::string&m){
    for(int i=0;i<L;++i)if(b[i]!=(m[i]-'0'))return i;
    return 99;
}

int first_return(const std::vector<int>&b,const std::string&m,int p){
    int h=0;
    for(int i=p;i<L;++i){
        h+=b[i]-(m[i]-'0');
        if(i>p&&h==0)return i;
    }
    return 99;
}

int next_defect(const std::vector<int>&b,const std::string&m,int after){
    for(int i=after+1;i<L;++i)if(b[i]!=(m[i]-'0'))return i;
    return 99;
}

u32 inv_odd(u32 a){
    u32 x=1;
    for(int i=0;i<6;++i)x*=2-a*x;
    return x&MASK;
}

u32 pow3(int n){u32 x=1;for(int i=0;i<n;++i)x=(u64(x)*3U)&MASK;return x;}

u32 swap_translation(int p,const std::string&m){
    int q0=0;
    for(int i=0;i<p;++i)q0+=m[i]=='1';
    const u32 inv=inv_odd(pow3(q0+1));
    return static_cast<u32>((u64(1U<<p)*inv)&MASK);
}

} // namespace

int main(int argc,char**argv){
    const std::string dir=argc>=2?argv[1]:".";
    const auto m=mechanical();
    const auto all=load_all(dir);

    std::map<int,std::set<u32>> first_sets;
    std::map<int,std::map<int,std::set<u32>>> immediate;
    std::map<int,std::map<int,u64>> return_counts;

    for(const u32 r:all){
        const auto b=parity(r);
        const int p=first_defect(b,m);
        first_sets[p].insert(r);
        if(p==99)continue;
        const int ret=first_return(b,m,p);
        ++return_counts[p][ret];
        if(ret==p+1){
            const int nd=next_defect(b,m,ret);
            immediate[p][nd].insert(r);
        }
    }

    if(first_sets[2].size()!=1'623'807ULL)return 4;
    if(first_sets[5].size()!=286'895ULL)return 5;
    if(first_sets[8].size()!=51'825ULL)return 6;
    if(first_sets[10].size()!=11'763ULL)return 7;

    const std::map<int,u64> expected_p2_returns{
        {3,353'165},{4,353'153},{7,66'268},{9,28'890},{11,13'410},
        {12,37'525},{14,13'783},{15,39'177},{17,17'510},{19,9'659},
        {20,30'790},{22,16'722},{23,43'745},{25,30'079},{26,65'607},
        {99,504'324}
    };
    if(return_counts[2]!=expected_p2_returns)return 8;

    const std::array<int,3> exact_ps{2,5,10};
    for(const int p:exact_ps){
        const u32 d=swap_translation(p,m);
        for(const auto&[nd,S]:immediate[p]){
            std::set<u32> mapped;
            for(const u32 r:S)mapped.insert((r-d)&MASK);
            if(mapped!=first_sets[nd])return 9;
        }
        std::cout<<"p="<<p<<" immediate-return translation="<<d
                 <<" exact renewal conjugacy PASS\n";
    }

    // p=8 is the exceptional Hensel state transition.
    if(immediate[8][10].size()!=14'443ULL)return 10;
    if(first_sets[10].size()!=11'763ULL)return 11;
    const u32 d8=swap_translation(8,m);
    std::set<u32> mapped8;
    for(const u32 r:immediate[8][10])mapped8.insert((r-d8)&MASK);
    if(mapped8==first_sets[10])return 12;

    std::cout<<"p=2 immediate-return size="<<return_counts[2][3]<<"\n";
    std::cout<<"p=8 exceptional immediate-return-next10="
             <<immediate[8][10].size()<<" vs ordinary p10="
             <<first_sets[10].size()<<"\n";
    std::cout<<"m45 depth28 first-return renewal diagnostic: PASS\n";
    return 0;
}
