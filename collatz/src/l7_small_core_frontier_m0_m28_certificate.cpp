// Exact finite certificate for the recursively sufficient Collatz Cantor core
// intersected with coefficient survival and aligned L7 full-Hensel
// residue-maximality.  This is finite evidence only, not an asymptotic proof.
//
// Build example:
//   g++ -O3 -march=native -fopenmp -std=c++17 \
//       l7_small_core_frontier_m0_m28_certificate.cpp -o l7_core
// Run example:
//   ./l7_core 0 28
//
// Each layer m enumerates exactly the 2^m integers
//   N = 4(3^m + sum_{i=0}^{m-1} a_i 3^i) + 3,  a_i in {0,1}.
// max= is the exact largest hard-prefix depth found up to HMAX=224.

#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using u32=std::uint32_t; using u64=std::uint64_t; using u128=unsigned __int128; using boost::multiprecision::cpp_int;
namespace{constexpr int B=7,HMAX=224; bool ALLOW[8][128]{}; int QMIN[HMAX+1]{};
void build(){std::array<u64,8>p3{};p3[0]=1;for(int i=1;i<=B;i++)p3[i]=3*p3[i-1];struct E{u64 R=0;u32 mask=0;bool set=false;};for(int q=0;q<=B;q++){std::unordered_map<u64,E>mx;for(u32 mask=0;mask<(1u<<B);mask++){int qq=0;u64 R=0;for(int i=0;i<B;i++)if(mask>>i&1u){R=3*R+(u64(1)<<i);qq++;}if(qq!=q)continue;auto&e=mx[R%p3[q]];if(!e.set||R>e.R)e=E{R,mask,true};}for(auto const&kv:mx)ALLOW[q][kv.second.mask]=true;}int ex[8]={1,2,6,15,21,16,7,1};for(int q=0;q<=B;q++){int c=0;for(int m=0;m<(1<<B);m++)c+=ALLOW[q][m];if(c!=ex[q])std::exit(2);}cpp_int p2=1,p3e=1;int q=0;for(int k=1;k<=HMAX;k++){p2<<=1;while(p3e<p2){p3e*=3;q++;}QMIN[k]=q;}}
int depth(u128 x){int q=0;u32 bm=0;int bq=0,bo=0;for(int k=0;k<HMAX;k++){int bit=int(x&1);bm|=u32(bit)<<bo;bq+=bit;bo++;if(bit){x=(3*x+1)>>1;q++;}else x>>=1;if(q<QMIN[k+1])return k;if(bo==B){if(!ALLOW[bq][bm])return k;bm=0;bq=0;bo=0;}}return HMAX;}
std::string s128(u128 x){if(!x)return"0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}std::reverse(s.begin(),s.end());return s;}
struct R{u64 c64=0,c96=0,c128=0,c144=0,c160=0,c192=0,c196=0;int maxd=0;u128 min64=~u128(0),min96=~u128(0),min128=~u128(0),min144=~u128(0),min160=~u128(0),min192=~u128(0),min196=~u128(0);};
R scan(int m){std::vector<u64>p3(m+1,1);for(int i=1;i<=m;i++)p3[i]=3*p3[i-1];int lo=m/2,hi=m-lo;u64 nl=u64(1)<<lo,nh=u64(1)<<hi;std::vector<u64>ls(nl),hs(nh);for(u64 mask=1;mask<nl;mask++){u64 bit=mask&(~mask+1);int i=__builtin_ctzll(bit);ls[mask]=ls[mask^bit]+p3[i];}for(u64 mask=1;mask<nh;mask++){u64 bit=mask&(~mask+1);int i=__builtin_ctzll(bit);hs[mask]=hs[mask^bit]+p3[lo+i];}u64 total=u64(1)<<m;R out;
#pragma omp parallel
{R z;
#pragma omp for schedule(static)
for(long long mm=0;mm<(long long)total;mm++){u64 mask=mm;u64 s=ls[mask&(nl-1)]+hs[mask>>lo];u128 N=u128(4)*(u128(p3[m])+s)+3;int d=depth(N);z.maxd=std::max(z.maxd,d);auto add=[&](int H,u64&c,u128&mn){if(d>=H){c++;if(N<mn)mn=N;}};add(64,z.c64,z.min64);add(96,z.c96,z.min96);add(128,z.c128,z.min128);add(144,z.c144,z.min144);add(160,z.c160,z.min160);add(192,z.c192,z.min192);add(196,z.c196,z.min196);}
#pragma omp critical
{out.c64+=z.c64;out.c96+=z.c96;out.c128+=z.c128;out.c144+=z.c144;out.c160+=z.c160;out.c192+=z.c192;out.c196+=z.c196;out.maxd=std::max(out.maxd,z.maxd);out.min64=std::min(out.min64,z.min64);out.min96=std::min(out.min96,z.min96);out.min128=std::min(out.min128,z.min128);out.min144=std::min(out.min144,z.min144);out.min160=std::min(out.min160,z.min160);out.min192=std::min(out.min192,z.min192);out.min196=std::min(out.min196,z.min196);}}
return out;}
void pv(const char*n,u64 c,u128 mn){std::cout<<' '<<n<<'='<<c;if(c)std::cout<<" min"<<n<<'='<<s128(mn);} }
int main(int argc,char**argv){build();int a=argc>1?std::stoi(argv[1]):0,b=argc>2?std::stoi(argv[2]):24;for(int m=a;m<=b;m++){auto r=scan(m);std::cout<<"m="<<m<<" max="<<r.maxd;pv("64",r.c64,r.min64);pv("96",r.c96,r.min96);pv("128",r.c128,r.min128);pv("144",r.c144,r.min144);pv("160",r.c160,r.min160);pv("192",r.c192,r.min192);pv("196",r.c196,r.min196);std::cout<<'\n';}}
