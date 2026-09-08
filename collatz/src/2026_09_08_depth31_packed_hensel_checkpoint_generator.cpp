// Packed depth-31 checkpoint generator used by MATH-042.
// Record format after the leading u64 count: repeated little-endian u64 C + u8 q.
// Exact finite scope only. Collatz remains OPEN.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std; using u64=uint64_t;
static const int QMIN[]={0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,16,16,17,18,18,19,19,20};
struct State{u64 C; uint8_t q;};
struct Solver{int k;const vector<u64>*p3,*p2;u64 rec(int j,int maxp,u64 r)const{if(j==0)return r==0?0:UINT64_MAX;u64 best=UINT64_MAX,mod=(*p3)[j-1];for(int p=j-1;p<maxp;++p){if(r%3!=(*p2)[p]%3)continue;__int128 d=(__int128)r-(*p2)[p];assert(d%3==0);__int128 z=d/3;long long m=(long long)mod,rp=m?(long long)(z%m):0;if(rp<0)rp+=m;u64 prev=rec(j-1,p,(u64)rp);if(prev==UINT64_MAX)continue;u64 C=3*prev+(*p2)[p];if(best==UINT64_MAX||C>best)best=C;}return best;}u64 best(int q,u64 r)const{return rec(q,k,r);}};
int main(){constexpr int K=31;vector<u64>p3(K+2,1),p2(K+2,1);for(int i=1;i<=K+1;++i){p3[i]=p3[i-1]*3ULL;p2[i]=p2[i-1]*2ULL;}vector<State>live{{0,0}},next;for(int k=1;k<=K;++k){next.clear();next.reserve(live.size()*2);for(auto const&s:live){if(s.q>=QMIN[k])next.push_back(s);State o{3*s.C+p2[k-1],uint8_t(s.q+1)};if(o.q>=QMIN[k])next.push_back(o);}vector<uint8_t>keep(next.size());Solver sol{k,&p3,&p2};
#pragma omp parallel for schedule(dynamic,128)
for(long long i=0;i<(long long)next.size();++i){auto const&s=next[(size_t)i];keep[(size_t)i]=(sol.best(s.q,s.C%p3[s.q])==s.C);}size_t w=0;for(size_t i=0;i<next.size();++i)if(keep[i])next[w++]=next[i];next.resize(w);live.swap(next);}assert(live.size()==19347686ULL);ofstream f("live31_packed.bin",ios::binary);u64 n=live.size();f.write((char*)&n,8);for(auto const&s:live){f.write((char*)&s.C,8);f.put((char)s.q);}cout<<"states "<<n<<"\n";cout<<"expected_sha256 f4d39cf0fd464b99f78d01aa3a38fc20ab5f3664c3c02e69478ccaccedd8a79d\n";}
