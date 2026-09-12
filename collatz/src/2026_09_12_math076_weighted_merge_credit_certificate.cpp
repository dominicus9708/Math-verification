// MATH-076 — exact weighted correction/address merge-credit audit through depth 32.
//
// For two depth-k coefficient-surviving states with q_H=q_L+d, define
//   Gamma_d = 3^d S_H - S_L = (C_H-C_L)/3^q_L,
//   A_d     = r_L - 3^d r_H.
// The exact endpoint residual identity is
//   Gamma_d - A_d = (2^k/3^q_L)(y_H-y_L).
// Hence a common endpoint satisfies Gamma_d=A_d.
//
// This certificate re-enumerates the exact coefficient-surviving tree through
// depth 32, identifies true first merges using distinct actual predecessors,
// and records A_d (=Gamma_d at a merge) for every observed d.
// Finite exact computation only. Collatz remains OPEN.

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using u64=uint64_t; using i128=__int128_t;
struct __attribute__((packed)) State { u64 y,r,pre; uint8_t q,p; };
static std::string s128(i128 x){if(x==0)return"0";bool n=x<0;if(n)x=-x;std::string s;while(x){s.push_back('0'+x%10);x/=10;}if(n)s.push_back('-');std::reverse(s.begin(),s.end());return s;}
struct Agg {u64 n=0,pos=0,zero=0,neg=0; i128 mn=0,mx=0; bool init=false; std::map<long long,u64> hist;};
int main(){
 const int K=32; u64 p2[K+2],p3[K+2]; p2[0]=p3[0]=1;
 for(int i=1;i<K+2;i++){p2[i]=2*p2[i-1];p3[i]=3*p3[i-1];}
 std::vector<State> cur{{0,0,0,0,0}}; std::map<int,Agg> total; u64 total_pairs=0;
 for(int k=0;k<K;k++){
  const u64 v=p2[k]; std::vector<State> next; next.reserve((size_t)(cur.size()*1.9));
  for(auto const&s:cur){ const u64 u=p3[s.q]; for(int p=0;p<2;p++){
   const int c=p^(s.y&1ULL); const u64 r=s.r+(c?v:0); const u64 pre=s.y+(c?u:0);
   const u64 y=p?(3*pre+1)/2:pre/2; const int q=s.q+p;
   if(p3[q]>=p2[k+1]) next.push_back({y,r,pre,(uint8_t)q,(uint8_t)p});
  }}
  cur.swap(next);
  std::sort(cur.begin(),cur.end(),[](auto const&a,auto const&b){if(a.y!=b.y)return a.y<b.y;if(a.q!=b.q)return a.q<b.q;if(a.r!=b.r)return a.r<b.r;if(a.pre!=b.pre)return a.pre<b.pre;return a.p<b.p;});
  std::map<int,Agg> here; u64 pairs=0;
  for(size_t a=0;a<cur.size();){ size_t e=a+1; while(e<cur.size()&&cur[e].y==cur[a].y)e++;
   for(size_t i=a;i<e;i++)for(size_t j=i+1;j<e;j++){
    if(cur[i].pre==cur[j].pre)continue; ++pairs;
    auto const*lo=&cur[i]; auto const*hi=&cur[j]; if(lo->q>hi->q)std::swap(lo,hi);
    const int d=hi->q-lo->q; if(d==0)continue;
    i128 pw=1; for(int z=0;z<d;z++)pw*=3;
    const i128 g=(i128)lo->r-pw*(i128)hi->r;
    for(Agg* ap:{&here[d],&total[d]}){ap->n++;if(g>0)ap->pos++;else if(g<0)ap->neg++;else ap->zero++;if(!ap->init){ap->mn=ap->mx=g;ap->init=true;}else{if(g<ap->mn)ap->mn=g;if(g>ap->mx)ap->mx=g;}if(g>=-1000000&&g<=1000000)ap->hist[(long long)g]++;}
   }
   a=e;
  }
  total_pairs+=pairs;
  std::cout<<"depth "<<(k+1)<<" states "<<cur.size()<<" true_pairs "<<pairs;
  for(auto const&kv:here)std::cout<<" dq"<<kv.first<<"="<<kv.second.n<<"/neg"<<kv.second.neg;
  std::cout<<'\n';
 }
 std::cout<<"TOTAL_PAIRS "<<total_pairs<<'\n';
 for(auto const&kv:total){auto const&a=kv.second;std::cout<<"TOTAL dq "<<kv.first<<" n "<<a.n<<" pos "<<a.pos<<" zero "<<a.zero<<" neg "<<a.neg<<" min "<<s128(a.mn)<<" max "<<s128(a.mx)<<"\nHIST";for(auto const&h:a.hist)std::cout<<' '<<h.first<<':'<<h.second;std::cout<<'\n';}
}
