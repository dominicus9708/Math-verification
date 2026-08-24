// Exact refinement of the m=44, L=77 globally-zero-mixed obstruction.
//
// This certificate enumerates the same survival + aligned-L7 + zero-mixed
// language as m44_l77_allheight_zero_mixed_l7_selector_obstruction_certificate.cpp,
// but prunes any canonical lift with a nonzero bit at positions >=73 and then
// audits the ternary selector coordinate
//
//   t=(N-3)/4-3^44.
//
// Exact results:
//   N<2^73                                      : 100,986,373
//   additionally in the convex hull of C_44    :  21,054,225
//   pass ternary digits 0..29 in {0,1}          :          99
//   pass ternary digits 0..34 in {0,1}          :          14
//   pass ternary digits 0..39 in {0,1}          :           3
//   pass ternary digits 0..41 in {0,1}          :           1
//   pass ternary digits 0..42 in {0,1}          :           0
//
// Hence t mod 3^43 already excludes the entire zero-mixed branch.  An
// independent diagnostic identifies the unique candidate surviving through
// ternary digit 41 as N*=5009655000888502825071; its digit_42(t*)=2,
// digit_43(t*)=0, while digits 0..41 are all 0/1.
//
// This is a finite exact certificate inside the present m=44 reduction.  It is
// not an asymptotic theorem and not a proof of the Collatz conjecture.

#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#ifdef _OPENMP
#include <omp.h>
#endif

using u128 = unsigned __int128;
using u64 = std::uint64_t;
using u32 = std::uint32_t;

constexpr int L=77, B=7, NB=11, QMAX=77;
int BA[L+1];
bool PL[L];

int barrier(int j){
    u128 p3=1, p2=((u128)1)<<j;
    int q=0;
    while(p3<p2){p3*=3; ++q;}
    return q;
}

struct Tr { u32 mask; std::uint8_t q, p; };
std::array<std::vector<u32>,8> AL;
std::vector<Tr> T[NB][QMAX+1][2][2];
u64 SUF[NB+1][QMAX+1][2][2]{};

void init(){
    for(int j=0;j<=L;++j) BA[j]=barrier(j);
    for(int j=0;j<L-1;++j) PL[j]=(BA[j+1]==BA[j]);

    std::array<u64,8> p3{};
    p3[0]=1;
    for(int i=1;i<=7;++i) p3[i]=3*p3[i-1];

    std::array<std::unordered_map<u64,std::pair<u64,u32>>,8> best;
    for(u32 mask=0; mask<128; ++mask){
        int q=0; u64 R=0;
        for(int i=0;i<7;++i) if((mask>>i)&1u){R=3*R+(1ull<<i); ++q;}
        u64 key=R%p3[q];
        auto it=best[q].find(key);
        if(it==best[q].end() || R>it->second.first) best[q][key]={R,mask};
    }
    const std::array<int,8> expected{1,2,6,15,21,16,7,1};
    for(int q=0;q<=7;++q){
        for(auto &kv:best[q]) AL[q].push_back(kv.second.second);
        std::sort(AL[q].begin(),AL[q].end());
        if((int)AL[q].size()!=expected[q]) std::exit(2);
    }

    for(int bl=0; bl<NB; ++bl){
        const int off=7*bl;
        for(int q0=0;q0<=QMAX;++q0) for(int pr=0;pr<2;++pr) for(int hp=0;hp<2;++hp){
            auto &v=T[bl][q0][pr][hp];
            for(int bq=0;bq<=7;++bq) for(u32 mask:AL[bq]){
                int q=q0,p=pr,h=hp;
                bool ok=true;
                for(int k=0;k<7;++k){
                    int pos=off+k, bit=(mask>>k)&1u;
                    if(h && pos>=1 && PL[pos-1] && bit!=p){ok=false; break;}
                    q += bit;
                    if(q<BA[pos+1]){ok=false; break;}
                    p=bit; h=1;
                }
                if(ok) v.push_back({mask,(std::uint8_t)q,(std::uint8_t)p});
            }
        }
    }

    for(int q=0;q<=QMAX;++q) for(int p=0;p<2;++p) for(int h=0;h<2;++h)
        SUF[NB][q][p][h]=1;
    for(int bl=NB-1; bl>=0; --bl)
        for(int q=0;q<=QMAX;++q) for(int p=0;p<2;++p) for(int h=0;h<2;++h){
            u64 s=0;
            for(auto &tr:T[bl][q][p][h]) s += SUF[bl+1][tr.q][tr.p][1];
            SUF[bl][q][p][h]=s;
        }
}

struct St { int q=0,p=0; bool hp=false; u128 r=0,y=0,p3=1; };

bool apply(const St&s, const Tr&tr, int bl, St&t){
    t=s;
    const int off=7*bl;
    for(int k=0;k<7;++k){
        const int pos=off+k, bit=(tr.mask>>k)&1u;
        const int carry=bit ^ int(t.y&1);
        if(carry){
            if(pos>=73) return false;
            t.r += ((u128)1)<<pos;
            t.y += t.p3;
        }
        if(bit){t.y=(3*t.y+1)/2; t.p3*=3;}
        else t.y/=2;
        t.q += bit; t.p=bit; t.hp=true;
    }
    return true;
}

u128 pow3(int n){u128 x=1; while(n--) x*=3; return x;}
u128 P44, MAXC;

struct Task { St s; int bl; };
std::vector<Task> tasks;
void make_tasks(int bl,const St&s,int cut){
    if(bl==cut){tasks.push_back({s,bl}); return;}
    for(auto &tr:T[bl][s.q][s.p][s.hp]) if(SUF[bl+1][tr.q][tr.p][1]){
        St t; if(apply(s,tr,bl,t)) make_tasks(bl+1,t,cut);
    }
}

struct Count {
    u64 low=0, hull=0, cantor=0;
    std::array<u64,45> bad{};
    u64 finalNear=0;
};

void inspect_leaf(const St&s, Count&c){
    ++c.low;
    if((s.r&3)!=3) return;
    const u128 Y=(s.r-3)/4;
    if(Y<P44) return;
    u128 t=Y-P44;
    if(t>MAXC) return;
    ++c.hull;

    u128 z=t;
    for(int i=0;i<44;++i){
        const unsigned d=(unsigned)(z%3);
        if(d>1){
            ++c.bad[i];
            if(i==42) ++c.finalNear;
            return;
        }
        z/=3;
    }
    if(z==0) ++c.cantor;
}

void walk(int bl,const St&s,Count&c){
    if(bl==NB){inspect_leaf(s,c); return;}
    for(auto &tr:T[bl][s.q][s.p][s.hp]) if(SUF[bl+1][tr.q][tr.p][1]){
        St t; if(apply(s,tr,bl,t)) walk(bl+1,t,c);
    }
}

int main(){
    init();
    P44=pow3(44);
    MAXC=(P44-1)/2;
    if(SUF[0][0][0][0]!=1615699347ull) return 3;

    St s;
    make_tasks(0,s,7);
    if(tasks.size()!=450466ull) return 4;

    Count total;
#pragma omp parallel
    {
        Count local;
#pragma omp for schedule(dynamic,32)
        for(long long i=0;i<(long long)tasks.size();++i)
            walk(tasks[i].bl,tasks[i].s,local);
#pragma omp critical
        {
            total.low += local.low;
            total.hull += local.hull;
            total.cantor += local.cantor;
            total.finalNear += local.finalNear;
            for(int i=0;i<45;++i) total.bad[i] += local.bad[i];
        }
    }

    if(total.low!=100986373ull) return 5;
    if(total.hull!=21054225ull) return 6;
    if(total.cantor!=0ull) return 7;

    u64 rem=total.hull;
    std::array<u64,43> after{};
    for(int i=0;i<=42;++i){rem-=total.bad[i]; after[i]=rem;}

    if(after[29]!=99ull) return 8;
    if(after[34]!=14ull) return 9;
    if(after[39]!=3ull) return 10;
    if(after[41]!=1ull) return 11;
    if(after[42]!=0ull) return 12;
    if(total.bad[42]!=1ull || total.finalNear!=1ull) return 13;

    std::cout << "zero_mixed_total=" << SUF[0][0][0][0] << "\n";
    std::cout << "below_2^73=" << total.low << "\n";
    std::cout << "core_convex_hull=" << total.hull << "\n";
    std::cout << "after_digit29=" << after[29] << "\n";
    std::cout << "after_digit34=" << after[34] << "\n";
    std::cout << "after_digit39=" << after[39] << "\n";
    std::cout << "after_digit41=" << after[41] << "\n";
    std::cout << "after_digit42=" << after[42] << "\n";
    std::cout << "digit42_near_misses=" << total.bad[42] << "\n";
    return 0;
}
