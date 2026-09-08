// MATH-042: exact q-partitioned one-sided Hensel audit at depth 32.
// Input: live31_packed.bin from the companion checkpoint generator.
// Usage: ./m42 <q>, q=21..32.  Output is checked against the canonical table.
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std; using u64=uint64_t;
struct State{u64 C;uint8_t q;};
struct Solver{int k;vector<u64>p3,p2;Solver(int K):k(K),p3(K+1,1),p2(K+1,1){for(int i=1;i<=K;++i){p3[i]=p3[i-1]*3ULL;p2[i]=p2[i-1]*2ULL;}}u64 rec(int j,int maxp,u64 r)const{if(j==0)return r==0?0:UINT64_MAX;u64 best=UINT64_MAX,mod=p3[j-1];for(int p=j-1;p<maxp;++p){if(r%3!=p2[p]%3)continue;__int128 d=(__int128)r-p2[p];if(d%3)continue;__int128 z=d/3;long long m=(long long)mod,rp=m?(long long)(z%m):0;if(rp<0)rp+=m;u64 prev=rec(j-1,p,(u64)rp);if(prev==UINT64_MAX)continue;u64 C=3*prev+p2[p];if(best==UINT64_MAX||C>best)best=C;}return best;}u64 best(int q,u64 r)const{return rec(q,k,r);}};
int main(int argc,char**argv){if(argc!=2)return 2;int q=stoi(argv[1]);if(q<21||q>32)return 3;const u64 EP[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10933870,10656854,6935755,3428066,1360848,438178,113563,23221,3620,406,30,1};const u64 ES[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10924522,10653576,6934804,3427766,1360759,438144,113563,23221,3620,405,30,1};ifstream f("live31_packed.bin",ios::binary);u64 n;f.read((char*)&n,8);assert(n==19347686ULL);vector<State>live(n);for(u64 i=0;i<n;++i){f.read((char*)&live[i].C,8);live[i].q=(uint8_t)f.get();}vector<State>cand;cand.reserve((size_t)EP[q]);u64 bit=1ULL<<31;for(auto const&s:live){if(s.q==q)cand.push_back(s);if((int)s.q+1==q)cand.push_back(State{3*s.C+bit,(uint8_t)q});}assert(cand.size()==EP[q]);Solver sol(32);u64 mod=sol.p3[q];vector<u64>best(cand.size());
#pragma omp parallel for schedule(dynamic,128)
for(long long i=0;i<(long long)cand.size();++i)best[(size_t)i]=sol.best(q,cand[(size_t)i].C%mod);u64 survive=0,minc=UINT64_MAX,maxc=0;for(size_t i=0;i<cand.size();++i){assert(best[i]>=cand[i].C);if(best[i]==cand[i].C)++survive;else{u64 d=(best[i]-cand[i].C)/mod;assert(d>0);if(d<minc)minc=d;if(d>maxc)maxc=d;}}assert(survive==ES[q]);cout<<q<<' '<<cand.size()<<' '<<survive<<' '<<(cand.size()-survive)<<' '<<(minc==UINT64_MAX?0:minc)<<' '<<maxc<<'\n';}
