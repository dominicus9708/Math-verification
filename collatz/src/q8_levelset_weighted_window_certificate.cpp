// Exact q<=8 phase-adaptive weighted overlapping-window certificate.
//
// Define N_{>=s}=#{i:h_i>=s}.  The audited run-average lemma gives
//   eta >= (5/24) sum_{s>=1} 2^{-s} N_{>=s}.
// Truncating at s<=6 and multiplying by 64 defines the integer weight
//   W6 = 32 N1 + 16 N2 + 8 N3 + 4 N4 + 2 N5 + N6,
// so eta >= 5 W6 / 1536.
//
// The local DP preserves this same six-level weight inside every length-47
// zero-endpoint window while applying the valid root-globalized q<=8
// phase-adaptive backtrace exclusions at h<=3.  Global incidence gives
//   Phi(H-47-2 floor(W6/32)) <= 46 W6.
// The first W6 satisfying this necessary condition is certified below.
//
// No later-block L7 maximality assumption is used.  This is a finite
// first-crossing certificate for the current m=44 resonance, not a proof
// of the Collatz conjecture.

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
 constexpr int Q=8,M=6561,L=47,WMAX=576,HF=3; const ull H=137528045312ULL;
 cpp_int V0=4;for(int i=0;i<44;i++)V0*=3;V0+=2;
 vector<vector<int>>dmin(Q+1);for(int q=1;q<=Q;q++){int mod=p3i(q);dmin[q].assign(mod,999);vector<int>a(q);for(int K=q;K<2*q;K++)comps(q,0,K,a,dmin[q]);}
 vector<vector<int>>fac(48);set<vector<int>>uniq;for(int u=0;u<48;u++){fac[u]=factor_upper(u,L);uniq.insert(fac[u]);}if(uniq.size()!=48)return 2;
 vector<int>modq(Q+1);for(int q=1;q<=Q;q++)modq[q]=p3i(q);
 const size_t SZ=(size_t)48*48*(HF+1)*M;vector<unsigned char>forbidden(SZ);auto ix=[&](int u,int s,int h,int res){return ((((size_t)u*48+s)*(HF+1)+h)*M+res);};
 for(int u=0;u<48;u++)for(int s=1;s<=47;s++){auto[pn,pd]=phase_sup(u,s);for(int h=0;h<=HF;h++)for(int res=0;res<M;res++){bool bad=false;for(int q=1;q<=min(Q,s);q++){int K=dmin[q][res%modq[q]];if(K==999)continue;cpp_int lhs=cpp_int(1)<<(K+h);lhs*=pn;lhs*=(3*V0+H);cpp_int rhs=1;for(int z=0;z<q+1;z++)rhs*=3;rhs*=V0;rhs*=pd;if(lhs<rhs){bad=true;break;}}forbidden[ix(u,s,h,res)]=bad;}}
 vector<i64>inv2p(128);inv2p[0]=1;i64 inv2=invm(2,M);for(int i=1;i<128;i++)inv2p[i]=inv2p[i-1]*inv2%M;
 vector<ull>C(WMAX+1);
 #pragma omp parallel for schedule(dynamic)
 for(int u=0;u<48;u++){
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
 auto ok=[&](ull W){ull rmax=W/32;ull E=(2*rmax>=H-L)?0:(H-L-2*rmax);return phi(E)<=(__uint128_t)46*W;};
 ull lo=0,hi=32*H;while(lo<hi){ull md=lo+(hi-lo)/2;if(ok(md))hi=md;else lo=md+1;}
 const ull TH=917388026368ULL;
 if(lo!=TH || ok(TH-1) || !ok(TH)) return 3;
 if(C[0]!=48ULL || C[32]!=917ULL || C[64]!=8669ULL || C[80]!=1ULL ||
    C[96]!=54509ULL || C[112]!=61ULL || C[128]!=258366ULL ||
    C[256]!=23657288ULL || C[384]!=529247117ULL ||
    C[512]!=7391705817ULL || C[575]!=129ULL || C[576]!=25486655704ULL) return 4;
 ull cum575=0; for(int w=0;w<=575;w++) cum575+=C[w];
 if(cum575!=76218244353ULL) return 5;
 ull Eprev=H-L-2*((TH-1)/32), Eat=H-L-2*(TH/32);
 auto Pprev=phi(Eprev), Pat=phi(Eat);
 auto Bprev=(__uint128_t)46*(TH-1), Bat=(__uint128_t)46*TH;
 if(Eprev!=80191293619ULL || Eat!=80191293617ULL) return 6;
 if(Pprev!=(__uint128_t)42199849213041ULL || Bprev!=(__uint128_t)42199849212882ULL) return 7;
 if(Pat!=(__uint128_t)42199849211889ULL || Bat!=(__uint128_t)42199849212928ULL) return 8;
 if(Eat-cum575!=3973049264ULL || Eat-cum575>C[576]) return 9;
 cout<<"threshold "<<TH<<"\n";
 cout<<"previous_E "<<Eprev<<" phi "<<u128(Pprev)<<" budget "<<u128(Bprev)<<" gap +159\n";
 cout<<"threshold_E "<<Eat<<" phi "<<u128(Pat)<<" budget "<<u128(Bat)<<" gap -1039\n";
 cout<<"cum_weight_le_575 "<<cum575<<"\n";
 cout<<"weight576_needed "<<(Eat-cum575)<<" of "<<C[576]<<"\n";
 cout<<setprecision(18)<<"eta/H_ge "<<(5.0L*(long double)TH)/(1536.0L*H)<<"\n";
 cout<<setprecision(18)<<"D/H_ge "<<(15.0L*(long double)TH)/(1536.0L*H)<<"\n";
 cout<<"q8 level-set weighted window certificate: PASS\n";
}
