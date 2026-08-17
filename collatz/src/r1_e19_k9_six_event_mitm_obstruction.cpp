#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using u128 = unsigned __int128;
using i128 = __int128;
using boost::multiprecision::cpp_int;

static constexpr int W = 104;
static constexpr int K = 9;
static u128 M = (u128)1 << W;
static u128 MASK = M - 1;
static u128 A[6][W];

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
    for (int i=0;i<6;i++) {
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

std::pair<u128,u128> U73_interval() {
    cpp_int N0("3939105844976711153619");
    cpp_int NMAX("5908625413101667397287");
    cpp_int num=1;
    for (int i=0;i<64;i++) num*=3;
    cpp_int den=cpp_int(1)<<73;
    cpp_int lo_num=num*(N0+1);
    cpp_int hi_num=num*(NMAX+512);
    return {from_cpp((lo_num+den-1)/den),from_cpp(hi_num/den)};
}

std::vector<uint64_t> target_residues(const std::vector<uint64_t>& carries,
                                      uint64_t mod) {
    std::vector<uint64_t> out;
    out.reserve(carries.size());
    for (uint64_t c:carries) out.push_back(c ? mod-c : 0);
    std::sort(out.begin(),out.end());
    return out;
}

bool formation_survives(u128 target, int depth) {
    std::vector<std::pair<int,i128>> st{{K,-(i128)target}};
    for (int d=0;d<depth;d++) {
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

int main() {
    init_terms();
    auto [lo,hi]=U73_interval();

    // Finite ternary-formation target sets at K=15,18,21.
    std::vector<std::vector<uint64_t>> S(K+1,std::vector<uint64_t>{0});
    uint64_t mod=1,m15=0,m18=0,m21=0;
    std::vector<uint64_t> T15,T18,T21;
    for (int r=1;r<=21;r++) {
        mod*=3;
        std::vector<std::vector<uint64_t>> N(K+1);
        for (int a=0;a<=K;a++) {
            size_t cap=0;
            for (int a2=0;a2<=a;a2++) cap+=S[a2].size();
            N[a].reserve(cap);
            for (int a2=0;a2<=a;a2++) {
                long long delta=(1LL<<a)-(1LL<<a2);
                for (uint64_t cp:S[a2]) {
                    uint64_t t=3*cp;
                    uint64_t half=(t&1) ? (t+mod)/2 : t/2;
                    long long c=(long long)half-delta;
                    c%=(long long)mod;
                    if (c<0) c+=(long long)mod;
                    N[a].push_back((uint64_t)c);
                }
            }
            std::sort(N[a].begin(),N[a].end());
            N[a].erase(std::unique(N[a].begin(),N[a].end()),N[a].end());
        }
        S.swap(N);
        if (r==15) { m15=mod; T15=target_residues(S[K],mod); }
        if (r==18) { m18=mod; T18=target_residues(S[K],mod); }
        if (r==21) { m21=mod; T21=target_residues(S[K],mod); }
    }
    assert(T15.size()==646146);
    assert(T18.size()==2735501);
    assert(T21.size()==9229199);

    std::vector<unsigned char> allow15(m15,0);
    for (uint64_t t:T15) allow15[t]=1;

    // For six window-even events p0<...<p5,
    // U == -sum_i 2^pi 3^{-(pi-i)} (mod 2^104).
    // Split ranks 0..2 and 3..5.  L[m] contains all left triples with p2<m,
    // so the order condition p2<p3 is enforced before pairing.
    std::vector<std::vector<u128>> L(W);
    for (int p0=0;p0<W;p0++)
        for (int p1=p0+1;p1<W;p1++)
            for (int p2=p1+1;p2<W;p2++) {
                u128 s=A[0][p0]+A[1][p1]+A[2][p2];
                for (int m=p2+1;m<W;m++) L[m].push_back(s);
            }
    for (auto& v:L) std::sort(v.begin(),v.end());

    uint64_t numeric=0,c15=0,c18=0,c21=0;
    std::vector<u128> survivors21;
    u128 maxL=3*M-3;

    for (int p3=3;p3<W;p3++) {
        const auto& left=L[p3];
        for (int p4=p3+1;p4<W;p4++)
            for (int p5=p4+1;p5<W;p5++) {
                u128 rs=A[3][p3]+A[4][p4]+A[5][p5];
                for (int j=0;j<6;j++) {
                    i128 qlo=(i128)((u128)(j+1)*M-hi)-(i128)rs;
                    i128 qhi=(i128)((u128)(j+1)*M-lo)-(i128)rs;
                    if (qhi<0 || qlo>(i128)maxL) continue;
                    u128 a=qlo<0 ? 0 : (u128)qlo;
                    u128 b=qhi>(i128)maxL ? maxL : (u128)qhi;
                    if (a>b) continue;
                    auto it=std::lower_bound(left.begin(),left.end(),a);
                    auto en=std::upper_bound(left.begin(),left.end(),b);
                    for (;it!=en;++it) {
                        u128 s=*it+rs;
                        u128 r=s&MASK;
                        u128 U=r ? M-r : 0;
                        if (U<lo || U>hi) continue;
                        numeric++;
                        uint64_t t15=(uint64_t)((U<<K)%m15);
                        if (!allow15[t15]) continue;
                        c15++;
                        uint64_t t18=(uint64_t)((U<<K)%m18);
                        if (!std::binary_search(T18.begin(),T18.end(),t18)) continue;
                        c18++;
                        uint64_t t21=(uint64_t)((U<<K)%m21);
                        if (!std::binary_search(T21.begin(),T21.end(),t21)) continue;
                        c21++;
                        survivors21.push_back(U);
                    }
                }
            }
    }

    assert(numeric==53574256);
    assert(c15==2413569);
    assert(c18==378769);
    assert(c21==47519);

    const std::pair<int,uint64_t> checkpoints[] = {
        {24,5225},{27,473},{30,54},{33,6},{36,0}
    };
    std::vector<u128> cur=std::move(survivors21);
    for (auto [depth,expected]:checkpoints) {
        std::vector<u128> next;
        for (u128 U:cur)
            if (formation_survives(U<<K,depth)) next.push_back(U);
        assert(next.size()==expected);
        cur.swap(next);
    }

    std::cout << "R1 E19 k=9 six-event MITM obstruction: PASS\n";
    std::cout << "raw C(104,6)=1517381580\n";
    std::cout << "numeric=53574256 K15=2413569 K18=378769 K21=47519\n";
    std::cout << "K24=5225 K27=473 K30=54 K33=6 K36=0\n";
}
