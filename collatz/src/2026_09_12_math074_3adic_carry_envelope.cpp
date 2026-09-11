// MATH-074: depth-41 3-adic carry-envelope regression.
//
// This is the MATH-051 fixed-d solver with one exact canonicalization:
// at rem=r, for equal competitor rank count nb and equal h modulo 3^r,
// retain only the largest carry h.  The companion note proves that the
// discarded state has exactly the same future divisibility pattern under
// matched lower-gap choices and finishes with smaller translation credit.
// Collatz and the first universal Farey cell remain OPEN.

#include <bits/stdc++.h>
using namespace std; using u64=uint64_t; using i128=__int128_t;
static i128 P3[64],P2[64];
static inline int blocksum(int n,int l){return l?(((1<<l)-1)<<(n-l)):0;}
struct Key{uint8_t na; vector<uint32_t>S; bool operator==(Key const&o)const noexcept{return na==o.na&&S==o.S;}};
struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=0x9e3779b97f4a7c15ULL^k.na; for(uint32_t x:k.S){uint64_t z=x+0x9e3779b97f4a7c15ULL;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;z^=z>>31;h^=z+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return(size_t)h;}};
static constexpr int HB=1<<20;
static inline uint32_t enc(int nb,int h){int v=h+HB;if(v<0||v>=(1<<21))abort();return((uint32_t)nb<<21)|(uint32_t)v;}
static inline void dec(uint32_t x,int&nb,int&h){nb=(int)(x>>21);h=(int)(x&((1u<<21)-1))-HB;}
struct Solver{
 int d; vector<int>L; unordered_map<uint64_t,uint8_t>memo; u64 env_in=0,env_out=0,env_removed=0; size_t maxS=0;
 Solver(int D):d(D){L.resize(d);for(int j=0;j<d;++j){int G=0;while(P3[G]<=P2[G+j+1])++G;L[j]=G;}memo.reserve(1<<20);} 
 inline bool upper(int rem,int na,int nb,int h)const{if(na&&L[na-1]>rem)return false;i128 lhs=(i128)(h-((1<<na)-1))*P2[rem]+(i128)((1<<nb)-1)*P3[rem];return lhs>0;}
 uint64_t mkey(int rem,int na,int nb,int h)const{uint64_t v=(uint32_t)(h+HB);return v|((uint64_t)nb<<21)|((uint64_t)na<<26)|((uint64_t)rem<<31);} 
 bool can(int rem,int na,int nb,int h){if(!upper(rem,na,nb,h))return false;if(rem==0){if(na){for(int j=0;j<na;++j)if(L[j]>0)return false;}return (long long)((1<<nb)-1)-((1<<na)-1)+h>0;} auto key=mkey(rem,na,nb,h);auto it=memo.find(key);if(it!=memo.end())return it->second;bool ok=false;for(int la=0;la<=na&&!ok;++la){bool valid=true;for(int j=na-la;j<na;++j)if(rem<L[j]){valid=false;break;}if(!valid)continue;int na2=na-la;if(na2&&L[na2-1]>rem-1)continue;int aa=blocksum(na,la);for(int lb=0;lb<=nb;++lb){int bb=blocksum(nb,lb),z=h+bb-aa;if(z%3)continue;int h2=2*(z/3);if(can(rem-1,na2,nb-lb,h2)){ok=true;break;}}}memo.emplace(key,(uint8_t)ok);return ok;}
 vector<uint32_t> envelope(vector<uint32_t> v,int rem){env_in+=v.size(); if(v.empty())return v; long long mod=1;for(int i=0;i<rem;++i)mod*=3; struct X{int nb,h; long long r;};vector<X>x;x.reserve(v.size());for(auto p:v){int nb,h;dec(p,nb,h);long long r=h%mod;if(r<0)r+=mod;x.push_back({nb,h,r});}sort(x.begin(),x.end(),[](auto&a,auto&b){if(a.nb!=b.nb)return a.nb<b.nb;if(a.r!=b.r)return a.r<b.r;return a.h>b.h;});vector<uint32_t>o;o.reserve(x.size());for(size_t i=0;i<x.size();){o.push_back(enc(x[i].nb,x[i].h));size_t j=i+1;while(j<x.size()&&x[j].nb==x[i].nb&&x[j].r==x[i].r)++j;i=j;}env_out+=o.size();env_removed+=v.size()-o.size();maxS=max(maxS,o.size());return o;}
 vector<uint32_t> trans(vector<uint32_t>const&S,int na,int la,int rem){int aa=blocksum(na,la),na2=na-la;vector<uint32_t>o;o.reserve(S.size()*2+8);for(auto p:S){int nb,h;dec(p,nb,h);for(int lb=0;lb<=nb;++lb){int bb=blocksum(nb,lb),z=h+bb-aa;if(z%3)continue;int h2=2*(z/3),nb2=nb-lb;if(can(rem,na2,nb2,h2))o.push_back(enc(nb2,h2));}}return envelope(move(o),rem);} 
 tuple<u64,size_t,size_t> run(int k,bool verb){int M=k-d;if(d==0)return{0,1,1};unordered_map<Key,u64,KH>dp,nd;dp.reserve(1024);dp.emplace(Key{(uint8_t)d,{enc(d,0)}},1);size_t peak=1;for(int r=M;r>=1;--r){nd.clear();nd.max_load_factor(.85f);nd.reserve(min<size_t>(max<size_t>(1024,dp.size()*2),16000000));for(auto const&kv:dp){int na=kv.first.na;auto const&S=kv.first.S;u64 cnt=kv.second;for(int la=0;la<=na;++la){bool valid=true;for(int j=na-la;j<na;++j)if(r<L[j]){valid=false;break;}if(!valid)continue;int na2=na-la;if(na2&&L[na2-1]>r-1)continue;auto S2=trans(S,na,la,r-1);if(S2.empty())continue;Key nx{(uint8_t)na2,move(S2)};auto it=nd.find(nx);if(it==nd.end())nd.emplace(move(nx),cnt);else it->second+=cnt;}}dp.swap(nd);peak=max(peak,dp.size());if(verb)cerr<<"r "<<r<<" states "<<dp.size()<<" memo "<<memo.size()<<" removed "<<env_removed<<" maxS "<<maxS<<"\n";}u64 D=0;for(auto const&kv:dp){if(kv.first.na)continue;bool f=false;for(auto p:kv.first.S){int nb,h;dec(p,nb,h);if(((1<<nb)-1)+h>0){f=true;break;}}if(f)D+=kv.second;}return{D,peak,maxS};}
};
int main(){P3[0]=P2[0]=1;for(int i=1;i<64;++i){P3[i]=P3[i-1]*3;P2[i]=P2[i-1]*2;}struct E{int d;u64 D;size_t peak,maxS;};vector<E> exp={{12,361499293ULL,3227,23},{13,586723760ULL,9835,33},{14,703863494ULL,28455,44},{15,355002462ULL,44095,68}};for(auto e:exp){Solver s(e.d);auto t=chrono::steady_clock::now();auto[D,peak,maxS]=s.run(41,false);double sec=chrono::duration<double>(chrono::steady_clock::now()-t).count();assert(D==e.D);assert(peak==e.peak);assert(maxS==e.maxS);cout<<"PASS d="<<e.d<<" D="<<D<<" peak="<<peak<<" maxS="<<maxS<<" env_removed="<<s.env_removed<<" memo="<<s.memo.size()<<" sec="<<sec<<"\n";}cout<<"PASS MATH-074 depth-41 3-adic carry envelope regression\n";}
