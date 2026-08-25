#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <omp.h>
using u64=uint64_t; using u32=uint32_t; using i128=__int128_t;
static constexpr int H=25, MINB=10, ZMAX=1<<(H-2), ZMASK=ZMAX-1, SCALE=16;
struct State{u64 R; uint8_t q;};
u64 p3[64];
inline bool coeffok(int k,int q){return p3[q]>=(1ULL<<k);} 
inline u64 keyc(int q,u64 R){return (u64(q)<<56)|(R%p3[q]);}
void scanall(int pos,int k,int q,u64 R,int qmin,std::unordered_map<u64,u64>&cm){
    if(q+(k-pos)<qmin)return;
    if(pos==k){auto it=cm.find(keyc(q,R)); if(it!=cm.end()&&R>it->second)it->second=R; return;}
    scanall(pos+1,k,q,R,qmin,cm);
    scanall(pos+1,k,q+1,3*R+(1ULL<<pos),qmin,cm);
}
u64 invodd(u64 a){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x;}
int boundary(int k){int q=0;while(p3[q]<(1ULL<<k))q++;return q;}
long double told(i128 x){return (long double)x;}

int main(){
    p3[0]=1;for(int i=1;i<64;i++)p3[i]=p3[i-1]*3;
    omp_set_num_threads(8);

    // Exact selector multiplicity for
    // x = 3^44 + sum_{i=0}^{43} a_i 3^i modulo 2^23.
    std::vector<u64> dp(ZMAX), nd(ZMAX);
    u32 fixed=(u32)(p3[44]&ZMASK); dp[fixed]=1;
    u32 w=1;
    for(int i=0;i<44;i++){
        if(i) w=(u64)w*3 & ZMASK;
        #pragma omp parallel for schedule(static)
        for(int r=0;r<ZMAX;r++) nd[r]=dp[r]+dp[(r+ZMAX-w)&ZMASK];
        dp.swap(nd);
    }
    u64 dpsum=0;for(auto x:dp)dpsum+=x;
    if(dpsum!=(1ULL<<44)){std::cerr<<"selector sum fail\n";return 2;}

    // Fold the exact depth-25 multiplicity table to all shallower depths.
    std::array<std::vector<u64>,H+1> cnt;
    cnt[H]=std::move(dp); nd.clear();nd.shrink_to_fit();
    for(int k=H-1;k>=MINB;k--){
        int M=1<<(k-2);cnt[k].resize(M);
        auto &up=cnt[k+1];auto &cur=cnt[k];
        #pragma omp parallel for schedule(static)
        for(int r=0;r<M;r++)cur[r]=up[r]+up[r+M];
    }

    // Pointwise selector distortion is small enough that
    // (cmax/cmin)*(3125/3456) < 1 at every audited depth.
    std::array<u64,H+1> selMin{}, selMax{};
    for(int k=MINB;k<=H;k++){
        auto mm=std::minmax_element(cnt[k].begin(),cnt[k].end());
        selMin[k]=*mm.first; selMax[k]=*mm.second;
        if(i128(selMax[k])*3125 >= i128(selMin[k])*3456){
            std::cerr<<"selector distortion too large at depth "<<k<<"\n"; return 5;
        }
    }
    if(selMin[25]!=2092917ULL || selMax[25]!=2102038ULL) return 6;

    const u64 ex[26]={0,1,1,2,3,4,7,11,16,31,52,103,182,297,593,1049,1720,3439,6104,12194,22244,38019,75969,137657,234156,467895};
    std::vector<State> co{{0,0}}, ne{{0,0}};
    std::array<u64,H+1> coMass{}, neMass{};
    std::array<i128,H+1> coW{}, neW{};
    std::array<int,H+1> coDmax{}, neDmax{};

    auto measure=[&](int k,const std::vector<State>&v,u64 &mass,i128 &ws,int &dmax){
        mass=0;ws=0;dmax=0;int Mmask=(1<<(k-2))-1;int b=boundary(k);
        for(auto s:v){
            u64 mask=(1ULL<<k)-1;
            u64 Nres=((0ULL-s.R)*invodd(p3[s.q]))&mask;
            if((Nres&3)!=3)continue;
            u32 z=(u32)((Nres-3)>>2)&Mmask;
            u64 mult=cnt[k][z]; if(!mult)continue;
            int d=int(s.q)-b;
            if(d<0){std::cerr<<"negative d\n";std::exit(3);}
            dmax=std::max(dmax,d);
            mass+=mult;
            // Common denominator 2^SCALE for W(d)=(3/2)^d.
            i128 factor=i128(p3[d]) << (SCALE-d);
            ws += i128(mult)*factor;
        }
    };

    for(int k=1;k<=H;k++){
        std::vector<State> nc;nc.reserve(co.size()*2);
        for(auto s:co){
            if(coeffok(k,s.q))nc.push_back(s);
            int q=s.q+1;u64 R=3*s.R+(1ULL<<(k-1));
            if(coeffok(k,q))nc.push_back({R,(uint8_t)q});
        }
        co.swap(nc);

        // Root-fullmax/Hensel-maximality filter.
        std::unordered_map<u64,u64> cm;cm.reserve(co.size()*2);
        for(auto s:co){auto[it,ins]=cm.emplace(keyc(s.q,s.R),s.R);if(!ins&&s.R>it->second)it->second=s.R;}
        int qmin=0;while(!coeffok(k,qmin))qmin++;
        scanall(0,k,0,0,qmin,cm);
        std::vector<State> nn;nn.reserve(ne.size()*2);
        for(auto s:ne){
            if(coeffok(k,s.q)){auto it=cm.find(keyc(s.q,s.R));if(it!=cm.end()&&it->second==s.R)nn.push_back(s);}
            int q=s.q+1;u64 R=3*s.R+(1ULL<<(k-1));
            if(coeffok(k,q)){auto it=cm.find(keyc(q,R));if(it!=cm.end()&&it->second==R)nn.push_back({R,(uint8_t)q});}
        }
        ne.swap(nn);
        if(ne.size()!=ex[k]){std::cerr<<"root count fail "<<k<<" got "<<ne.size()<<" exp "<<ex[k]<<"\n";return 4;}

        if(k>=MINB){
            measure(k,co,coMass[k],coW[k],coDmax[k]);
            measure(k,ne,neMass[k],neW[k],neDmax[k]);
            std::cout<<"DEPTH "<<k<<" b "<<boundary(k)<<" coeff_words "<<co.size()<<" root_words "<<ne.size()
                     <<" coeff_mass "<<coMass[k]<<" root_mass "<<neMass[k]
                     <<" coeff_dmax "<<coDmax[k]<<" root_dmax "<<neDmax[k]<<"\n";
        }
    }

    std::cout<<std::setprecision(18);
    for(int k=MINB;k<=H;k++)
        std::cout<<"SELECTOR_MIX depth "<<k<<" min "<<selMin[k]<<" max "<<selMax[k]
                 <<" maxmin "<<(long double)selMax[k]/selMin[k]
                 <<" sigma_dist "<<((long double)selMax[k]/selMin[k])*((long double)3125/3456)<<"\n";

    std::vector<int> plats;
    for(int n=MINB;n<H;n++)if(boundary(n+1)==boundary(n))plats.push_back(n);
    std::cout<<"PLATEAUS";for(int p:plats)std::cout<<" "<<p;std::cout<<"\n";

    long double worstCo=0,worstNe=0;int wc=-1,wn=-1;bool allCoSigma=true,allNeSigma=true;
    for(size_t i=0;i+2<plats.size();i++){
        int a=plats[i], c=plats[i+2]; if(c>H)continue; int L=c-a;
        long double rc=told(coW[c])/told(coW[a]);
        long double rn=told(neW[c])/told(neW[a]);
        bool cs = coW[c]*3456 < coW[a]*3125;
        bool ns = neW[c]*3456 < neW[a]*3125;
        allCoSigma &= cs; allNeSigma &= ns;
        if(rc>worstCo){worstCo=rc;wc=a;}if(rn>worstNe){worstNe=rn;wn=a;}
        std::cout<<"MACRO2 "<<a<<"->"<<c<<" L "<<L
                 <<" coeff_ratio "<<rc<<" root_ratio "<<rn
                 <<" coeff_lt_sigma "<<cs<<" root_lt_sigma "<<ns
                 <<" coeff_mass_ratio "<<(long double)coMass[c]/coMass[a]
                 <<" root_mass_ratio "<<(long double)neMass[c]/neMass[a]<<"\n";
    }

    std::cout<<"WORST coeff "<<worstCo<<" start "<<wc<<" root "<<worstNe<<" start "<<wn<<"\n";
    std::cout<<"ALL_LT_SIGMA coeff "<<allCoSigma<<" root "<<allNeSigma
             <<" sigma "<<(long double)3125/3456<<"\n";
    std::cout<<"PASS\n";
}
