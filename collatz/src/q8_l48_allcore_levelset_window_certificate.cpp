// Exact length-48 all-core q<=8 weighted overlapping-window certificate.
//
// Six-level weight:
//   W6 = 32 N_{>=1}+16 N_{>=2}+8 N_{>=3}+4 N_{>=4}+2 N_{>=5}+N_{>=6},
// with eta >= 5 W6 / 1536 from the audited level-set run-average theorem.
//
// For all three remaining 44-trit affine blocks, N<=18*3^44+1 and every
// zero-defect state is <2^75.  A length-48 zero-endpoint critical factor has
// time-expanded parity length at least 76, so each exact local parity word has
// at most one positive representative in the state range.  This removes the
// multiplicity-two loss present at length 47.
//
// Root-globalized phase-adaptive q<=8 backtrace exclusions are applied only
// when their exact headroom inequality proves an alternate ancestor below N.
// No later-block L7 maximality is used.  Finite current-resonance certificate;
// not a proof of Collatz.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using ull=unsigned long long; using i64=long long; using boost::multiprecision::cpp_int;
static i64 p3i(int q){i64 x=1;while(q--)x*=3;return x;}
static i64 invm(i64 a,i64 m){i64 b=m,u=1,v=0;while(b){i64 t=a/b;a-=t*b;swap(a,b);u-=t*v;swap(u,v);}u%=m;if(u<0)u+=m;return u;}
static i64 endpoint(const vector<int>&a,int q){i64 M=p3i(q),y=0;for(int v:a){i64 pw=1;for(int t=0;t<v;t++)pw=pw*2%M;y=((3*y+1)%M)*invm(pw,M)%M;}return y;}
static void comps(int q,int pos,int rem,vector<int>&a,vector<int>&dmin){if(pos==q){if(rem==0){int r=(int)endpoint(a,q);dmin[r]=min(dmin[r],accumulate(a.begin(),a.end(),0));}return;}for(int x=1;x<=rem-(q-pos-1);x++){a[pos]=x;comps(q,pos+1,rem-x,a,dmin);}}
static long long floor_alpha(int n){if(n==0)return 0;if(n>0){cpp_int p=1;for(int i=0;i<n;i++)p*=3;return (long long)boost::multiprecision::msb(p)-n;}return -floor_alpha(-n)-1;}
static vector<int> factor_upper(int u,int m){vector<long long>F(m+1);if(u==0){F[0]=0;for(int i=1;i<=m;i++)F[i]=1+floor_alpha(i);}else for(int i=0;i<=m;i++){int d=i-u;F[i]=(d==0)?-1:floor_alpha(d);}vector<int>r(m);for(int i=0;i<m;i++)r[i]=1+(int)(F[i+1]-F[i]);return r;}
static pair<cpp_int,cpp_int> phase_sup(int u,int s){if(u!=0&&s==u)return {cpp_int(2),cpp_int(1)};int n=s-u;if(n>0){long long f=floor_alpha(n);cpp_int num=1;for(int i=0;i<n;i++)num*=3;cpp_int den=cpp_int(1)<<(n+f);return {num,den};}int k=-n;long long f=floor_alpha(k);cpp_int num=cpp_int(1)<<(k+f+1);cpp_int den=1;for(int i=0;i<k;i++)den*=3;return {num,den};}
static int wt(int h){return (h>=1?32:0)+(h>=2?16:0)+(h>=3?8:0)+(h>=4?4:0)+(h>=5?2:0)+(h>=6?1:0);}
struct Key{uint32_t res;uint16_t h,w;bool operator==(Key const&o)const{return res==o.res&&h==o.h&&w==o.w;}};
struct Hsh{size_t operator()(Key const&k)const{return ((size_t)k.res*11995408973635179863ULL)^((size_t)k.h<<16)^k.w;}};
static string u128(__uint128_t x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
int main(){
 constexpr int Q=8,M=6561,L=48,NF=49,WMAX=560,HF=3; const ull H=137528045312ULL;
 cpp_int p44=1;for(int i=0;i<44;i++)p44*=3;
 cpp_int V0=4*p44+2;
 cpp_int NMAX=18*p44+1, two74=cpp_int(1)<<74;
 // All remaining core: 2(NMAX+H/3)<2^75, checked without division.
 cpp_int state_lhs=3*NMAX+H, state_rhs=3*two74; if(state_lhs>=state_rhs)return 10;
 vector<vector<int>>dmin(Q+1);for(int q=1;q<=Q;q++){int mod=p3i(q);dmin[q].assign(mod,999);vector<int>a(q);for(int K=q;K<2*q;K++)comps(q,0,K,a,dmin[q]);}
 vector<vector<int>>fac(NF);set<vector<int>>uniq;int minD=999;
 for(int u=0;u<NF;u++){fac[u]=factor_upper(u,L);uniq.insert(fac[u]);minD=min(minD,accumulate(fac[u].begin(),fac[u].end(),0));}
 if(uniq.size()!=NF||minD<76)return 2;
 vector<int>modq(Q+1);for(int q=1;q<=Q;q++)modq[q]=p3i(q);
 const size_t SZ=(size_t)NF*NF*(HF+1)*M;vector<unsigned char>forbidden(SZ);auto ix=[&](int u,int s,int h,int res){return ((((size_t)u*NF+s)*(HF+1)+h)*M+res);};
 for(int u=0;u<NF;u++)for(int s=1;s<=L;s++){auto[pn,pd]=phase_sup(u,s);for(int h=0;h<=HF;h++)for(int res=0;res<M;res++){bool bad=false;for(int q=1;q<=min(Q,s);q++){int K=dmin[q][res%modq[q]];if(K==999)continue;cpp_int lhs=cpp_int(1)<<(K+h);lhs*=pn;lhs*=(3*V0+H);cpp_int rhs=1;for(int z=0;z<q+1;z++)rhs*=3;rhs*=V0;rhs*=pd;if(lhs<rhs){bad=true;break;}}forbidden[ix(u,s,h,res)]=bad;}}
 vector<i64>inv2p(128);inv2p[0]=1;i64 inv2=invm(2,M);for(int i=1;i<128;i++)inv2p[i]=inv2p[i-1]*inv2%M;
 vector<ull>C(WMAX+1);
 #pragma omp parallel for schedule(dynamic)
 for(int u=0;u<NF;u++){
   const auto&r=fac[u];vector<ull>LC(WMAX+1);unordered_map<Key,ull,Hsh>st,nx;st.reserve(100000);st[{0,0,0}]=1;
   for(int i=0;i<L;i++){
     nx.clear();nx.reserve(st.size()*2+100);
     for(auto &kv:st){auto k=kv.first;ull cnt=kv.second;int maxh=k.h+r[i]-1;for(int hp=0;hp<=maxh;hp++){int v=r[i]+k.h-hp;if(v<1)continue;int w=k.w+((i+1<L)?wt(hp):0);if(w>WMAX)continue;uint32_t res=(uint32_t)(((3LL*k.res+1)%M)*inv2p[v]%M);if(hp<=HF&&forbidden[ix(u,i+1,hp,res)])continue;Key key{res,(uint16_t)hp,(uint16_t)w};auto &z=nx[key];if(ULLONG_MAX-z<cnt)z=ULLONG_MAX;else z+=cnt;}}
     st.swap(nx);
   }
   for(auto &kv:st)if(kv.first.h==0&&kv.first.w<=WMAX){auto &z=LC[kv.first.w];if(ULLONG_MAX-z<kv.second)z=ULLONG_MAX;else z+=kv.second;}
   #pragma omp critical
   {for(int w=0;w<=WMAX;w++){auto &z=C[w];ull a=LC[w];if(ULLONG_MAX-z<a)z=ULLONG_MAX;else z+=a;}}
 }
 auto phi=[&](ull E)->__uint128_t{ull rem=E;__uint128_t cost=0;for(int w=0;w<=WMAX;w++){ull take=min(rem,C[w]);cost+=(__uint128_t)w*take;rem-=take;if(!rem)return cost;}return ~(__uint128_t)0;};
 auto ok=[&](ull W){ull rmax=W/32;ull E=(2*rmax>=H-L)?0:(H-L-2*rmax);return phi(E)<=(__uint128_t)(L-1)*W;};
 ull lo=0,hi=32*H;while(lo<hi){ull md=lo+(hi-lo)/2;if(ok(md))hi=md;else lo=md+1;}
 const ull TH=894734262659ULL;
 if(lo!=TH||ok(TH-1)||!ok(TH))return 3;
 ull Ep=H-L-2*((TH-1)/32), E=H-L-2*(TH/32);
 auto Pp=phi(Ep), P=phi(E); auto Bp=(__uint128_t)(L-1)*(TH-1), B=(__uint128_t)(L-1)*TH;
 if(Ep!=81607153848ULL||E!=81607153848ULL)return 4;
 if(Pp!=(__uint128_t)42052510344966ULL||P!=(__uint128_t)42052510344966ULL)return 5;
 if(Bp!=(__uint128_t)42052510344926ULL||B!=(__uint128_t)42052510344973ULL)return 6;
 ull cum559=0;for(int w=0;w<=559;w++)cum559+=C[w];
 if(cum559!=71393756708ULL||C[560]!=24711535104ULL)return 7;
 if(E-cum559!=10213397140ULL||E-cum559>C[560])return 8;
 cout<<"threshold "<<TH<<"\n";
 cout<<"previous gap +40; threshold gap -7\n";
 cout<<"weight560_needed "<<(E-cum559)<<" of "<<C[560]<<"\n";
 cout<<setprecision(18)<<"eta/H_ge "<<(5.0L*(long double)TH)/(1536.0L*H)<<"\n";
 cout<<"minD "<<minD<<" factors "<<uniq.size()<<"\n";
 cout<<"q8 L48 all-core level-set certificate: PASS\n";
}
