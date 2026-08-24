// Exact L=77 all-height zero-mixed/L7 same-integer obstruction for the
// current m=44 ternary selector core.
//
// Define Z~_77 by all length-77 parity words satisfying:
//   * coefficient survival at every prefix:
//       q_j >= b(j),  b(j)=min{q : 3^q >= 2^j};
//   * every aligned full 7-bit block is L7 residue-maximal;
//   * every Beatty plateau pair is globally unmixed (00 or 11).
//
// IMPORTANT: no terminal equality q_77=b(77) is imposed.  Thus open positive-
// height excursions at depth 77 are included.
//
// The m=44 selector core is
//   C_44={4(3^44 + sum_{i=0}^{43} a_i 3^i)+3 : a_i in {0,1}}.
// Every C_44 integer is <2^73, while this verifier reconstructs the canonical
// start modulo 2^77; hence any same-integer hit must occur literally below 2^73.
//
// Exact regression values:
//   |Z~_77|                         = 1,615,699,347
//   |{N in Z~_77 : N < 2^73}|      =   100,986,373
//   |Z~_77 intersect C_44|         =             0
//
// Therefore the globally zero-mixed branch of this m=44 selector core is
// excluded already by its first 77 parity bits under survival+L7 constraints.
// This is a finite exact obstruction inside the current proof reduction; it is
// not by itself an asymptotic transversality theorem or a proof of Collatz.

#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
#ifdef _OPENMP
#include <omp.h>
#endif
using u128=unsigned __int128; using u64=std::uint64_t; using u32=std::uint32_t;
constexpr int L=77,B=7,NB=11,QMAX=77;
int BA[L+1]; bool PL[L];
int barrslow(int j){u128 p3=1,p2=((u128)1)<<j;int q=0;while(p3<p2){p3*=3;++q;}return q;}
struct Tr{u32 mask; unsigned char q,prev;};
std::array<std::vector<u32>,8> AL;
std::vector<Tr> T[NB][QMAX+1][2][2];
u64 SUF[NB+1][QMAX+1][2][2]{};
void init(){
 for(int j=0;j<=L;++j)BA[j]=barrslow(j);
 for(int j=0;j<L-1;++j)PL[j]=(BA[j+1]==BA[j]);
 std::array<u64,8> p3{};p3[0]=1;for(int i=1;i<=7;++i)p3[i]=3*p3[i-1];
 std::array<std::unordered_map<u64,std::pair<u64,u32>>,8> best;
 for(u32 mask=0;mask<128;++mask){int q=0;u64 R=0;for(int i=0;i<7;++i)if((mask>>i)&1u){R=3*R+(1ull<<i);++q;}u64 key=R%p3[q];auto it=best[q].find(key);if(it==best[q].end()||R>it->second.first)best[q][key]={R,mask};}
 const std::array<int,8> ex{1,2,6,15,21,16,7,1};
 for(int q=0;q<=7;++q){for(auto &kv:best[q])AL[q].push_back(kv.second.second);std::sort(AL[q].begin(),AL[q].end());if((int)AL[q].size()!=ex[q])std::exit(2);}
 for(int bl=0;bl<NB;++bl){int off=bl*B;for(int q0=0;q0<=QMAX;++q0)for(int pr=0;pr<2;++pr)for(int hp=0;hp<2;++hp){auto &v=T[bl][q0][pr][hp];for(int bq=0;bq<=7;++bq)for(u32 mask:AL[bq]){int q=q0,p=pr,h=hp;bool ok=true;for(int k=0;k<B;++k){int pos=off+k,bit=(mask>>k)&1u;if(h && pos>=1 && PL[pos-1] && bit!=p){ok=false;break;}q+=bit;if(q>QMAX||q<BA[pos+1]){ok=false;break;}p=bit;h=1;}if(ok)v.push_back({mask,(unsigned char)q,(unsigned char)p});}}}
 for(int q=0;q<=QMAX;++q)for(int p=0;p<2;++p)for(int h=0;h<2;++h)SUF[NB][q][p][h]=1;
 for(int bl=NB-1;bl>=0;--bl)for(int q=0;q<=QMAX;++q)for(int p=0;p<2;++p)for(int h=0;h<2;++h){u64 s=0;for(auto &tr:T[bl][q][p][h])s+=SUF[bl+1][tr.q][tr.prev][1];SUF[bl][q][p][h]=s;}
}
struct St{int q=0,prev=0;bool hp=false;u128 r=0,y=0,p3=1;};
inline St apply(const St&s,u32 mask,int bl){St t=s;int off=bl*B;for(int k=0;k<B;++k){int pos=off+k,bit=(mask>>k)&1u;int carry=bit ^ int(t.y&1);if(carry){t.r+=((u128)1)<<pos;t.y+=t.p3;}if(bit){t.y=(3*t.y+1)/2;t.p3*=3;}else t.y/=2;t.q+=bit;t.prev=bit;t.hp=true;}return t;}
std::string dec(u128 x){if(!x)return"0";std::string s;while(x){s.push_back(char('0'+x%10));x/=10;}std::reverse(s.begin(),s.end());return s;}
u128 pow3(int n){u128 x=1;while(n--)x*=3;return x;} u128 P344;
inline bool cantor(u128 N){if((N&3)!=3)return false;u128 Y=(N-3)/4;if(Y<P344)return false;u128 t=Y-P344;for(int i=0;i<44;++i){unsigned d=(unsigned)(t%3);if(d>1)return false;t/=3;}return t==0;}
struct Task{St s;int block;};
std::vector<Task> tasks;
void make_tasks(int bl,const St&s,int cut){if(bl==cut){tasks.push_back({s,bl});return;}for(auto &tr:T[bl][s.q][s.prev][s.hp]){if(!SUF[bl+1][tr.q][tr.prev][1])continue;St t=apply(s,tr.mask,bl);make_tasks(bl+1,t,cut);}}
struct Cnt{u64 leaves=0,below=0,hits=0;};
void walk(int bl,const St&s,Cnt&c,std::vector<u128>&hv){if(bl==NB){++c.leaves;if(s.r<(((u128)1)<<73)){++c.below;if(cantor(s.r)){++c.hits;if(hv.size()<20)hv.push_back(s.r);}}return;}for(auto &tr:T[bl][s.q][s.prev][s.hp]){if(!SUF[bl+1][tr.q][tr.prev][1])continue;St t=apply(s,tr.mask,bl);walk(bl+1,t,c,hv);}}
int main(){
 init();P344=pow3(44);const u128 max_core=4*(P344+(P344-1)/2)+3;
 if(!(max_core < (((u128)1)<<73))) return 3;
 std::cout<<"boundary="<<SUF[0][0][0][0]<<" b77="<<BA[77]<<std::endl;
 if(SUF[0][0][0][0]!=1615699347ull) return 4;
 St s;make_tasks(0,s,7);std::cout<<"tasks_after49="<<tasks.size()<<std::endl;u64 leaves=0,below=0,hits=0;std::vector<u128> allhits;
 #pragma omp parallel
 {Cnt c;std::vector<u128> hv;
  #pragma omp for schedule(dynamic,64)
  for(long long i=0;i<(long long)tasks.size();++i)walk(tasks[i].block,tasks[i].s,c,hv);
  #pragma omp atomic
  leaves+=c.leaves;
  #pragma omp atomic
  below+=c.below;
  #pragma omp atomic
  hits+=c.hits;
  if(!hv.empty()){
   #pragma omp critical
   allhits.insert(allhits.end(),hv.begin(),hv.end());
  }
 }
 std::cout<<"enumerated="<<leaves<<" below2^73="<<below<<" cantor_hits="<<hits<<std::endl;
 for(auto x:allhits) std::cout<<"hit "<<dec(x)<<std::endl;
 if(leaves!=1615699347ull) return 5;
 if(below!=100986373ull) return 6;
 if(hits!=0ull) return 7;
 return 0;
}
