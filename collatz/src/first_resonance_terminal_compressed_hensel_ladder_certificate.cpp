#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;

static const long long A = 114208327604LL;
static const long long Q = 72057431991LL;

u128 addmod(u128 a,u128 b,u128 m){u128 s=a+b; if(s>=m)s-=m; return s;}
u128 mulmod(u128 a,u128 b,u128 m){u128 r=0; while(b){if(b&1)r=addmod(r,a,m); b>>=1; if(b)a=addmod(a,a,m);} return r;}
u128 powmod(u128 a,unsigned long long e,u128 m){u128 r=1%m; while(e){if(e&1)r=mulmod(r,a,m); e>>=1; if(e)a=mulmod(a,a,m);} return r;}
u128 pow3i(int n){u128 r=1; while(n--)r*=3; return r;}
string dec(u128 x){if(!x)return "0"; string s; while(x){s.push_back(char('0'+x%10));x/=10;} reverse(s.begin(),s.end());return s;}
long long mech(long long j){return (long long)(((__int128)(j-1)*A)/Q);}

const u128 LOW=((u128)1<<71);
const u128 UPPER_TIMES_3=4*LOW+3*((u128)1<<33);
bool admissible(u128 y){return LOW<y && 3*y<UPPER_TIMES_3 && (y&3)==3;}

struct Hit {int L; vector<pair<int,int>> later; u128 y; int initial_mod3;};
struct Solver {
 int m,k,L; u128 M,q,ym; vector<long long>B; vector<int>gap; vector<u128>base; vector<array<u128,16>> C;
 unsigned long long seq=0; vector<Hit> hits; int init_u=0;
 Solver(int mm,int kk,int LL):m(mm),k(kk),L(LL){
  M=pow3i(m); q=pow3i(m-L); B.resize(m); gap.assign(m,0); base.resize(m); C.resize(m);
  for(int t=0;t<m;t++)B[t]=mech(Q-m+1+t);
  for(int t=1;t<m;t++){gap[t]=(int)(B[t]-B[t-1]); assert(gap[t]==1||gap[t]==2);}
  u128 inv2=(M+1)/2, invA=powmod(inv2,A,M); vector<u128> p3(m); p3[0]=1; for(int i=1;i<m;i++)p3[i]=3*p3[i-1];
  ym=0;
  for(int t=0;t<m;t++){base[t]=mulmod(mulmod(invA,p3[m-1-t],M),powmod(2,B[t],M),M); ym=addmod(ym,base[t],M);}
  for(int t=0;t<m;t++){C[t].fill(0); u128 ip=1; for(int d=1;d<16;d++){ip=mulmod(ip,inv2,M); C[t][d]=mulmod(base[t],ip-1,M);}}
  if(L){u128 u=(base[L-1]/q)%3; assert(u==1||u==2); init_u=(int)u;}
 }
 void terminal_test(u128 later,const vector<pair<int,int>>&pat){
  seq++; u128 z=addmod(ym,later,M);
  if(!L){if(admissible(z))hits.push_back({L,pat,z,0}); return;}
  assert(UPPER_TIMES_3/3<q);
  u128 y=z%q; if(!admissible(y))return;
  u128 high=z/q, modL=pow3i(L), h=(high?modL-high:0);
  int r=(int)(h%3);
  if(r==0||r==init_u)hits.push_back({L,pat,y,r});
 }
 void rec(int t,int left,int prev,u128 sum,vector<pair<int,int>>&pat){
  if(left<0||left>m-t)return;
  if(t==m){if(!left)terminal_test(sum,pat);return;}
  rec(t+1,left,0,sum,pat);
  if(!left)return;
  if(!prev){if(t>0&&gap[t]==2){pat.push_back({t,1});rec(t+1,left-1,1,addmod(sum,C[t][1],M),pat);pat.pop_back();}}
  else {int md=prev+gap[t]-1; assert(md<16); for(int d=1;d<=md;d++){pat.push_back({t,d});rec(t+1,left-1,d,addmod(sum,C[t][d],M),pat);pat.pop_back();}}
 }
 void run(){vector<pair<int,int>> p; if(L==m){if(k==L)terminal_test(0,p);return;} rec(L+1,k-L,0,0,p);}
};

u128 endpoint_global(int m,const map<long long,int>&D){
 u128 M=pow3i(m), invA=powmod((M+1)/2,A,M), s=0;
 for(int t=0;t<m;t++){long long j=Q-m+1+t; int d=0; auto it=D.find(j); if(it!=D.end())d=it->second; long long a=mech(j)-d; u128 term=mulmod(pow3i(m-1-t),powmod(2,a,M),M); s=addmod(s,term,M);}
 return mulmod(invA,s,M);
}

pair<unsigned long long,vector<Hit>> layer(int m,int k){unsigned long long n=0; vector<Hit> H; for(int L=0;L<=k;L++){Solver S(m,k,L);S.run();n+=S.seq;H.insert(H.end(),S.hits.begin(),S.hits.end());} return {n,H};}

int main(){
 for(int L=1;L<=9;L++){
  u128 mod=pow3i(L); unsigned long long period=2; for(int i=1;i<L;i++)period*=3;
  vector<char> seen((size_t)mod,0); u128 inv2=(mod+1)/2, x=1;
  for(unsigned long long d=1;d<=period;d++){x=mulmod(x,inv2,mod); seen[(size_t)((x+mod-1)%mod)]=1;}
  size_t c=0; int missing=-1; for(size_t h=0;h<(size_t)mod;h++)if(seen[h])c++;
  assert(c==2*(size_t)(mod/3));
  for(int r=0;r<3;r++){bool any=false;for(size_t h=r;h<(size_t)mod;h+=3)if(seen[h]){any=true;break;} if(!any)missing=r;}
  assert(missing>=0);
 }

 auto [n58,h58]=layer(58,6); assert(n58==3188310ULL); assert(h58.size()==1); assert(h58[0].L==1);
 vector<pair<int,int>> p58={{2,1},{17,1},{18,1},{47,1},{57,1}}; assert(h58[0].later==p58);
 u128 Y4=(u128)2704820911452840622ULL*1000+43; assert(h58[0].y==Y4);
 map<long long,int>D58; for(int t:vector<int>{0,2,17,18,47,57})D58[Q-57+t]=1;
 assert(endpoint_global(58,D58)==Y4); assert(endpoint_global(59,D58)==Y4); assert(endpoint_global(60,D58)!=Y4);

 auto [n60k7,h60k7]=layer(60,7); assert(n60k7==25581232ULL); assert(h60k7.empty());

 auto [n64k8,h64k8]=layer(64,8); assert(n64k8==203183093ULL); assert(h64k8.empty());

 auto [n64k9,h64k9]=layer(64,9); assert(n64k9==1023618344ULL); assert(h64k9.size()==1); assert(h64k9[0].L==1);
 vector<pair<int,int>> p64={{6,1},{25,1},{27,1},{34,1},{51,1},{53,1},{56,1},{61,1}}; assert(h64k9[0].later==p64);
 u128 Y9=(u128)2556679481397564529ULL*1000+951; assert(h64k9[0].y==Y9);
 map<long long,int>D64; for(int t:vector<int>{0,6,25,27,34,51,53,56,61})D64[Q-63+t]=1;
 assert(endpoint_global(64,D64)==Y9); assert(!admissible(endpoint_global(65,D64)));

 assert(Q-65>72);
 cout<<"PASS first-resonance compressed terminal Hensel ladder\n";
 cout<<"m58 k6 compressed classes="<<n58<<" hits="<<h58.size()<<"\n";
 cout<<"m60 k7 compressed classes="<<n60k7<<" hits=0\n";
 cout<<"D_tail(60)>=8\n";
 cout<<"m64 k8 compressed classes="<<n64k8<<" hits=0\n";
 cout<<"D_tail(64)>=9\n";
 cout<<"m64 k9 compressed classes="<<n64k9<<" hits=1 endpoint="<<dec(Y9)<<"\n";
 cout<<"unique k9 equality does not lift to m65\n";
 cout<<"D_tail(65)>=10\n";
 cout<<"with D_72>=11: r_*>=21\n";
 cout<<"coarse normalized correction: E/3^Q > 21/12 = 7/4\n";
}
