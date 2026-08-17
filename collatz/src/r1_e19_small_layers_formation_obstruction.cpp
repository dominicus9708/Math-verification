#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using u128 = unsigned __int128;
using i128 = __int128;
using boost::multiprecision::cpp_int;

static constexpr int W = 104;
static u128 M = (u128)1 << W;
static u128 MASK = M - 1;
static u128 A[7][W];

cpp_int invmod(cpp_int a, cpp_int m) {
    cpp_int t=0, nt=1, r=m, nr=a;
    while (nr != 0) {
        cpp_int q=r/nr;
        cpp_int x=t-q*nt; t=nt; nt=x;
        x=r-q*nr; r=nr; nr=x;
    }
    if (t < 0) t += m;
    return t;
}

u128 from_cpp(const cpp_int& x) {
    cpp_int mask=(cpp_int(1)<<64)-1;
    uint64_t lo=(uint64_t)(x & mask);
    uint64_t hi=(uint64_t)((x>>64) & mask);
    return ((u128)hi<<64)|lo;
}

void init_terms() {
    cpp_int mod=cpp_int(1)<<W;
    cpp_int inv3=invmod(3,mod);
    for (int i=0;i<=6;i++) {
        for (int p=i;p<W;p++) {
            cpp_int e=p-i, b=inv3, q=1;
            while (e != 0) {
                if ((e & 1) != 0) q=q*b%mod;
                b=b*b%mod;
                e >>= 1;
            }
            A[i][p]=from_cpp(((cpp_int(1)<<p)*q)%mod);
        }
    }
}

std::pair<u128,u128> U73_interval(int k) {
    cpp_int N0("3939105844976711153619");
    cpp_int NMAX("5908625413101667397287");
    cpp_int num=1;
    for (int i=0;i<73-k;i++) num*=3;
    cpp_int den=cpp_int(1)<<73;
    cpp_int lo_num=num*(N0+1);
    cpp_int hi_num=num*(NMAX+1+((cpp_int(1)<<k)-1));
    return {from_cpp((lo_num+den-1)/den),from_cpp(hi_num/den)};
}

bool formation_survives(u128 target, int ranks, int K) {
    std::vector<std::pair<int,i128>> st{{ranks,-(i128)target}};
    for (int d=0;d<K;d++) {
        std::vector<std::pair<int,i128>> nx;
        for (auto [a,c]:st) {
            for (int a2=0;a2<=a;a2++) {
                i128 z=c+(((i128)1)<<a)-(((i128)1)<<a2);
                if (z%3==0) nx.push_back({a2,2*(z/3)});
            }
        }
        if (nx.empty()) return false;
        std::sort(nx.begin(),nx.end(),[](auto&x,auto&y){
            return x.first<y.first || (x.first==y.first && x.second<y.second);
        });
        nx.erase(std::unique(nx.begin(),nx.end()),nx.end());
        st.swap(nx);
    }
    return !st.empty();
}

struct Acc { uint64_t raw=0, numeric=0; std::vector<u128> U; };

void enumerate_z(int z,int start,int depth,u128 sum,u128 lo,u128 hi,Acc& acc) {
    if (depth==z) {
        acc.raw++;
        u128 r=sum & MASK;
        u128 U=r ? M-r : 0;
        if (U>=lo && U<=hi) { acc.numeric++; acc.U.push_back(U); }
        return;
    }
    int need=z-depth;
    for (int p=start;p<=W-need;p++)
        enumerate_z(z,p+1,depth+1,sum+A[depth][p],lo,hi,acc);
}

int main() {
    init_terms();
    struct Spec { int k,m,zeroK; uint64_t raw,numeric; };
    const Spec specs[] = {
        {15,0,12,1,0},
        {14,1,12,105,0},
        {13,2,15,5461,2},
        {12,3,27,187565,219},
        {11,4,30,4785691,18688},
        {10,5,33,96748211,1137712},
        // k=9 is split: z<=5 is direct here; z=6 is handled by MITM.
        {9,5,33,96748211,3417527},
    };

    for (const auto& s:specs) {
        auto [lo,hi]=U73_interval(s.k);
        Acc acc;
        for (int z=0;z<=s.m;z++) enumerate_z(z,0,0,0,lo,hi,acc);
        assert(acc.raw==s.raw);
        assert(acc.numeric==s.numeric);
        uint64_t survivors=0;
        for (u128 U:acc.U)
            survivors += formation_survives(U<<s.k,s.k,s.zeroK);
        assert(survivors==0);
        std::cout << "k=" << s.k << " raw=" << acc.raw
                  << " numeric=" << acc.numeric
                  << " zero_by_K=" << s.zeroK << "\n";
    }
    std::cout << "R1 E19 direct small/sublayers: PASS\n";
}
