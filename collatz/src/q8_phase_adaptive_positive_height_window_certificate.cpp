#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using ull=unsigned long long;
using i64=long long;
using boost::multiprecision::cpp_int;

// Exact finite certificate for the m=44 R1 local language.
//
// This extends the earlier phase-adaptive q<=8 two-place backtrace filter from
// zero-defect endpoints h=0 to every endpoint with h<=3.  The exact minimality
// inequality is applied in the form
//
//   2^(K+h) * sup(2^theta) * (3 V0 + H) < 3^(q+1) V0,
//
// which guarantees that the positive q-odd-step inverse ancestor is < N for
// every m=44 candidate N>=V0 represented by the full Sturmian phase cylinder.
//
// No later-block L7 maximality assumption is used here.  This is a valid
// repeated root-minimality filter.  It is still a finite m=44 resonance
// certificate, not a proof of the Collatz conjecture.

static i64 p3i(int q){i64 x=1;while(q--)x*=3;return x;}
static i64 invm(i64 a,i64 m){i64 b=m,u=1,v=0;while(b){i64 t=a/b;a-=t*b;swap(a,b);u-=t*v;swap(u,v);}u%=m;if(u<0)u+=m;return u;}
static i64 endpoint(const vector<int>&a,int q){i64 M=p3i(q),y=0;for(int v:a){i64 pw=1;for(int t=0;t<v;t++)pw=pw*2%M;y=((3*y+1)%M)*invm(pw,M)%M;}return y;}
static void comps(int q,int pos,int rem,vector<int>&a,vector<int>&dmin){
    if(pos==q){if(rem==0){int r=(int)endpoint(a,q);dmin[r]=min(dmin[r],accumulate(a.begin(),a.end(),0));}return;}
    for(int x=1;x<=rem-(q-pos-1);x++){a[pos]=x;comps(q,pos+1,rem-x,a,dmin);}
}

// alpha=log_2(3/2).  For nonzero integer n it is irrational, so
// floor(-n alpha)=-floor(n alpha)-1.  For n>0,
// floor(n alpha)=floor(log_2 3^n)-n, evaluated exactly from bit length.
static long long floor_alpha(int n){
    if(n==0)return 0;
    if(n>0){cpp_int p=1;for(int i=0;i<n;i++)p*=3;return (long long)boost::multiprecision::msb(p)-n;}
    return -floor_alpha(-n)-1;
}

// The length-m critical Sturmian factor on the cylinder whose upper
// breakpoint is b_u={-u alpha}.  u=0 denotes the final interval ending at 1.
static vector<int> factor_upper(int u,int m){
    vector<long long> F(m+1);
    if(u==0){F[0]=0;for(int i=1;i<=m;i++)F[i]=1+floor_alpha(i);}
    else for(int i=0;i<=m;i++){int d=i-u;F[i]=(d==0)?-1:floor_alpha(d);}
    vector<int> r(m);for(int i=0;i<m;i++)r[i]=1+(int)(F[i+1]-F[i]);return r;
}

// Exact rational supremum of 2^{theta_s} over the factor cylinder.
static pair<cpp_int,cpp_int> phase_sup(int u,int s){
    if(u!=0 && s==u)return {cpp_int(2),cpp_int(1)};
    int n=s-u;
    if(n>0){long long f=floor_alpha(n);cpp_int num=1;for(int i=0;i<n;i++)num*=3;cpp_int den=cpp_int(1)<<(n+f);return {num,den};}
    int k=-n;long long f=floor_alpha(k);cpp_int num=cpp_int(1)<<(k+f+1);cpp_int den=1;for(int i=0;i<k;i++)den*=3;return {num,den};
}

struct Key{uint32_t res;uint16_t h,j;bool operator==(Key const&o)const{return res==o.res&&h==o.h&&j==o.j;}};
struct Hsh{size_t operator()(Key const&k)const{return ((size_t)k.res*11995408973635179863ULL)^((size_t)k.h<<8)^k.j;}};

int main(){
    constexpr int Q=8,M=6561,L=47,JMAX=18,HF=3;
    const ull H=137528045312ULL;
    cpp_int V0=4;for(int i=0;i<44;i++)V0*=3;V0+=2;

    // Minimum K needed for each admissible endpoint residue at reverse depth q.
    // A forbidden inequality implies 2^K<3^q, hence K<2q; larger K cannot help.
    vector<vector<int>> dmin(Q+1);
    for(int q=1;q<=Q;q++){
        int mod=p3i(q);dmin[q].assign(mod,999);vector<int>a(q);
        for(int K=q;K<2*q;K++)comps(q,0,K,a,dmin[q]);
    }

    vector<vector<int>> fac(48);set<vector<int>> uniq;
    for(int u=0;u<48;u++){fac[u]=factor_upper(u,L);uniq.insert(fac[u]);}
    if(uniq.size()!=48)return 2;

    vector<int> modq(Q+1);for(int q=1;q<=Q;q++)modq[q]=p3i(q);
    const size_t SZ=(size_t)48*48*(HF+1)*M;
    vector<unsigned char> forbidden(SZ,0);
    auto ix=[&](int u,int s,int h,int res){return ((((size_t)u*48+s)*(HF+1)+h)*M+res);};

    for(int u=0;u<48;u++)for(int s=1;s<=47;s++){
        auto [pn,pd]=phase_sup(u,s);
        for(int h=0;h<=HF;h++)for(int res=0;res<M;res++){
            bool bad=false;
            for(int q=1;q<=min(Q,s);q++){
                int K=dmin[q][res%modq[q]];if(K==999)continue;
                cpp_int lhs=cpp_int(1)<<(K+h);lhs*=pn;lhs*=(3*V0+H);
                cpp_int rhs=1;for(int z=0;z<q+1;z++)rhs*=3;rhs*=V0;rhs*=pd;
                if(lhs<rhs){bad=true;break;}
            }
            forbidden[ix(u,s,h,res)]=bad;
        }
    }

    vector<i64>inv2p(128);inv2p[0]=1;i64 inv2=invm(2,M);for(int i=1;i<128;i++)inv2p[i]=inv2p[i-1]*inv2%M;
    vector<ull>C(JMAX+1);

#pragma omp parallel for schedule(dynamic)
    for(int u=0;u<48;u++){
        const auto&r=fac[u];vector<ull>LC(JMAX+1);
        unordered_map<Key,ull,Hsh>st,nx;st.reserve(70000);st[{0,0,0}]=1;
        for(int i=0;i<L;i++){
            nx.clear();nx.reserve(st.size()*2+100);
            for(auto &kv:st){auto k=kv.first;ull cnt=kv.second;int maxh=k.h+r[i]-1;
                for(int hp=0;hp<=maxh;hp++){
                    int v=r[i]+k.h-hp;if(v<1)continue;
                    int j=k.j+((i+1<L&&hp>0)?1:0);if(j>JMAX)continue;
                    uint32_t res=(uint32_t)(((3LL*k.res+1)%M)*inv2p[v]%M);
                    if(hp<=HF&&forbidden[ix(u,i+1,hp,res)])continue;
                    Key key{res,(uint16_t)hp,(uint16_t)j};auto &z=nx[key];
                    if(ULLONG_MAX-z<cnt)z=ULLONG_MAX;else z+=cnt;
                }
            }
            st.swap(nx);
        }
        for(auto &kv:st)if(kv.first.h==0&&kv.first.j<=JMAX){auto &z=LC[kv.first.j];if(ULLONG_MAX-z<kv.second)z=ULLONG_MAX;else z+=kv.second;}
#pragma omp critical
        {for(int j=0;j<=JMAX;j++){auto &z=C[j];ull a=LC[j];if(ULLONG_MAX-z<a)z=ULLONG_MAX;else z+=a;}}
    }

    const vector<ull> expected={
        48ULL,917ULL,8670ULL,54571ULL,261464ULL,1039208ULL,3648409ULL,
        11816396ULL,36190638ULL,106028242ULL,298905312ULL,814856327ULL,
        2157844802ULL,5569902294ULL,14050583911ULL,34717893182ULL,
        84199143072ULL,200713077167ULL,470710868104ULL};
    if(C!=expected)return 3;

    auto phi=[&](ull E)->__uint128_t{
        ull rem=E;__uint128_t cost=0;
        for(int j=0;j<=JMAX;j++){ull take=min(rem,C[j]);cost+=(__uint128_t)j*take;rem-=take;if(!rem)return cost;}
        return ~(__uint128_t)0;
    };
    auto ok=[&](ull rr){ull E=(2*rr>=H-L)?0:(H-L-2*rr);return phi(E)<=(__uint128_t)46*rr;};
    ull lo=0,hi=H;while(lo<hi){ull md=lo+(hi-lo)/2;if(ok(md))hi=md;else lo=md+1;}
    const ull threshold=26990139680ULL;
    if(lo!=threshold||ok(threshold-1)||!ok(threshold))return 4;

    ull Eprev=H-L-2*(threshold-1),Eat=H-L-2*threshold;
    __uint128_t Pprev=phi(Eprev),Pat=phi(Eat);
    if(Pprev!=(__uint128_t)1241546425277ULL)return 5;
    if(Pat!=(__uint128_t)1241546425245ULL)return 6;
    if((__uint128_t)46*(threshold-1)!=(__uint128_t)1241546425234ULL)return 7;
    if((__uint128_t)46*threshold!=(__uint128_t)1241546425280ULL)return 8;

    for(int j=0;j<=JMAX;j++)cout<<j<<" "<<C[j]<<"\n";
    cout<<"threshold "<<threshold<<"\n";
    cout<<setprecision(18)<<"defect_ratio_gt "<<(long double)threshold/H<<"\n";
    cout<<"previous_gap +43\nthreshold_gap -35\n";
    cout<<"q8 phase-adaptive positive-height certificate: PASS\n";
}
