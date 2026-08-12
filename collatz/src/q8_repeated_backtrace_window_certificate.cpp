#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using ull=unsigned long long; using i64=long long; using u128=__uint128_t; using boost::multiprecision::cpp_int;
i64 p3(int q){i64 x=1;while(q--)x*=3;return x;}i64 invm(i64 a,i64 m){i64 b=m,u=1,v=0;while(b){i64 t=a/b;a-=t*b;swap(a,b);u-=t*v;swap(u,v);}u%=m;if(u<0)u+=m;return u;}
i64 endpoint(const vector<int>&a,int q){i64 M=p3(q),y=0;for(int v:a){i64 pw=1;for(int t=0;t<v;t++)pw=pw*2%M;y=((3*y+1)%M)*invm(pw,M)%M;}return y;}
void comps(int q,int pos,int rem,vector<int>&a,unordered_set<i64>&bad){if(pos==q){if(rem==0)bad.insert(endpoint(a,q));return;}for(int x=1;x<=rem-(q-pos-1);x++){a[pos]=x;comps(q,pos+1,rem-x,a,bad);}}
vector<vector<int>> crit(int m){set<vector<int>>fs; cpp_int p=1; vector<int> kap; kap.push_back(0); vector<int> rr; for(int n=0;fs.size()<(size_t)m+1 && n<10000;n++){p*=3; int k=boost::multiprecision::msb(p); kap.push_back(k); rr.push_back(k-kap[kap.size()-2]); if((int)rr.size()>=m){vector<int> f(rr.end()-m,rr.end());fs.insert(f);}}return {fs.begin(),fs.end()};}
struct Key{uint32_t res;uint16_t h,j;bool operator==(Key const&o)const{return res==o.res&&h==o.h&&j==o.j;}};struct Hsh{size_t operator()(Key const&k)const{return ((size_t)k.res*11995408973635179863ULL)^((size_t)k.h<<8)^k.j;}};
int main(){const int Q=8,m=47,JMAX=18,HMAX=0; const unsigned long long H=137528045312ULL; cpp_int V=4; for(int i=0;i<44;i++)V*=3; V+=2;
 vector<vector<unordered_set<i64>>> bad(HMAX+1, vector<unordered_set<i64>>(Q+1));
 for(int h=0;h<=HMAX;h++)for(int q=1;q<=Q;q++){int Kmax=-1; for(int K=q;K<=3*q;K++){cpp_int lhs=cpp_int(1)<<(K+h+1); lhs*= (3*V + H); cpp_int rhs=1; for(int i=0;i<q+1;i++)rhs*=3; rhs*=V; if(lhs<rhs)Kmax=K;} if(Kmax>=q){vector<int>a(q);for(int K=q;K<=Kmax;K++)comps(q,0,K,a,bad[h][q]);} cerr<<"h"<<h<<" q"<<q<<" Kmax "<<Kmax<<" bad "<<bad[h][q].size()<<"\n";}
 i64 M=p3(Q); vector<i64> mods(Q+1);for(int q=1;q<=Q;q++)mods[q]=p3(q);vector<i64>inv2p(128);inv2p[0]=1;i64 inv2=invm(2,M);for(int i=1;i<128;i++)inv2p[i]=inv2p[i-1]*inv2%M;
 auto forb=[&](uint32_t res,int t,int h){if(h>HMAX)return false;for(int q=1;q<=min(Q,t);q++)if(!bad[h][q].empty()&&bad[h][q].count(res%mods[q]))return true;return false;};
 auto fs=crit(m);cerr<<"factors "<<fs.size()<<"\n";vector<ull>C(JMAX+1);for(auto&r:fs){unordered_map<Key,ull,Hsh>st,nx;st.reserve(50000);st[{0,0,0}]=1;for(int i=0;i<m;i++){nx.clear();nx.reserve(st.size()*2+100);for(auto &kv:st){auto k=kv.first;ull cnt=kv.second;int maxh=k.h+r[i]-1;for(int hp=0;hp<=maxh;hp++){int v=r[i]+k.h-hp;if(v<1)continue;int j=k.j+((i+1<m&&hp>0)?1:0);if(j>JMAX)continue;uint32_t res=(uint32_t)(((3LL*k.res+1)%M)*inv2p[v]%M);if(forb(res,i+1,hp))continue;auto key=Key{res,(uint16_t)hp,(uint16_t)j};auto &z=nx[key]; if(ULLONG_MAX-z<cnt)z=ULLONG_MAX;else z+=cnt;}}st.swap(nx);}for(auto &kv:st)if(kv.first.h==0&&kv.first.j<=JMAX){auto &z=C[kv.first.j];if(ULLONG_MAX-z<kv.second)z=ULLONG_MAX;else z+=kv.second;}}
 for(int j=0;j<=JMAX;j++)if(C[j])cout<<j<<" "<<C[j]<<"\n";
 auto phi=[&](unsigned long long E)->__uint128_t{unsigned long long rem=E; __uint128_t cost=0; for(int j=0;j<=JMAX;j++){unsigned long long take=min(rem,C[j]); cost+=(__uint128_t)j*take; rem-=take; if(!rem)return cost;} return ~(__uint128_t)0;};
 auto ok=[&](unsigned long long rr){unsigned long long E=(2*rr>=H-m)?0:(H-m-2*rr); return phi(E)<=(__uint128_t)46*rr;}; unsigned long long lo=0,hi=H; while(lo<hi){auto md=lo+(hi-lo)/2;if(ok(md))hi=md;else lo=md+1;} cerr<<"threshold "<<lo<<"\n"; if(lo!=26381334316ULL) return 2; if(ok(lo-1)||!ok(lo)) return 3;
}
