#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <omp.h>
using u32=std::uint32_t; using u64=std::uint64_t; using u128=unsigned __int128;
static std::string s128(u128 x){if(!x)return"0";std::string s;while(x){s.push_back(char('0'+unsigned(x%10)));x/=10;}std::reverse(s.begin(),s.end());return s;}
struct Entry{u32 r12;u64 exact;};
static int first_descent(u128 N,u128&below,u128&peak,bool&ov){u128 x=N;peak=N;ov=false;const u128 MX=~u128(0);for(int k=1;k<=5000;++k){if(x&1){if(x>(MX-1)/3){ov=true;below=x;return-1;}x=(3*x+1)/2;}else x/=2;if(x>peak)peak=x;if(x<N){below=x;return k;}}below=x;return-1;}
int main(int argc,char**argv){
 constexpr int DL=22,DH=22,P=13,B=14; constexpr u32 M12=1u<<(B-2),MASK12=M12-1; constexpr u32 NMECH24=12475387u; constexpr u64 MASK25=(1ULL<<25)-1;
 const u32 nmech=NMECH24&((1u<<B)-1), targetN=nmech^(1u<<P), targetY=(targetN-3u)/4u;
 int which=argc>1?std::atoi(argv[1]):0; int chunk=argc>2?std::atoi(argv[2]):0; const std::string allow_path=argc>3?argv[3]:"allow27.bin"; if(which<0||which>1||chunk<0||chunk>=8)return 9;
 std::vector<u64> allow(1ULL<<21); std::ifstream f(allow_path,std::ios::binary); f.read((char*)allow.data(),allow.size()*sizeof(u64)); if(!f){std::cerr<<"allow read fail\n";return 1;}
 std::array<u128,46>P3{};P3[0]=1;for(int i=1;i<46;++i)P3[i]=P3[i-1]*3;
 std::vector<u64> lows(1,0);for(int i=0;i<DL;++i){size_t n=lows.size();lows.resize(2*n);u64 w=(u64)P3[i];for(size_t j=0;j<n;++j)lows[n+j]=lows[j]+w;}
 std::vector<Entry> low;low.reserve(lows.size());for(u64 x:lows)low.push_back({u32(x&MASK12),x});std::sort(low.begin(),low.end(),[](auto&a,auto&b){if(a.r12!=b.r12)return a.r12<b.r12;return a.exact<b.exact;});
 std::vector<u32> start(M12+1);size_t pos=0;for(u32 r=0;r<M12;++r){start[r]=u32(pos);while(pos<low.size()&&low[pos].r12==r)++pos;}start[M12]=u32(pos);
 std::vector<u128> high(1,0);for(int i=DL;i<DL+DH;++i){size_t n=high.size();high.resize(2*n);u128 w=P3[i];for(size_t j=0;j<n;++j)high[n+j]=high[j]+w;}
 struct Case{const char*name;u128 C;u64 raw_total;}; Case cs=which==0?Case{"C45",P3[45],4294972331ULL}:Case{"C45plusC44",P3[45]+P3[44],4294962588ULL};
 constexpr u64 RAW[2][8]={{536869484ULL,536872021ULL,536873251ULL,536871508ULL,536873738ULL,536869211ULL,536868448ULL,536874670ULL},{536869280ULL,536869477ULL,536871264ULL,536871980ULL,536869924ULL,536872139ULL,536870037ULL,536868487ULL}};
 constexpr u64 HARD[2][8]={{77007814ULL,77007283ULL,77004313ULL,77007010ULL,77003459ULL,77002987ULL,77003352ULL,76995421ULL},{77005127ULL,77004916ULL,77007698ULL,77006159ULL,77018221ULL,77004283ULL,77008997ULL,77003843ULL}};
 constexpr int TAU[2][8]={{471,474,465,482,424,489,446,438},{474,546,462,430,452,441,498,460}};
 u64 rawsum=0,hardsum=0;for(int c=0;c<8;++c){rawsum+=RAW[which][c];hardsum+=HARD[which][c];}if(rawsum!=cs.raw_total)return 10;
 const long long HN=(long long)high.size(),HLO=HN*chunk/8,HHI=HN*(chunk+1)/8;
 u64 raw=0,hard=0,fail=0,ovc=0;int gmax=0;u128 worst=0,wbelow=0,gpeak=0;const u32 c12=u32(cs.C&MASK12);const u64 c25=u64(cs.C&MASK25);
 #pragma omp parallel
 {u64 lr=0,lh=0,lf=0,lo=0;int lm=0;u128 lw=0,lb=0,lp=0;
  #pragma omp for schedule(static)
  for(long long hh=HLO;hh<HHI;++hh){u128 hs=high[(size_t)hh];u32 hr12=u32(hs&MASK12);u32 need=(targetY-c12-hr12)&MASK12;u64 base25=(c25+u64(hs&MASK25))&MASK25;for(u32 j=start[need];j<start[need+1];++j){++lr;u64 y25=(base25+(low[j].exact&MASK25))&MASK25;u32 r27=u32((y25<<2)|3ULL);if(((allow[r27>>6]>>(r27&63))&1ULL)==0)continue;++lh;u128 N=4*(cs.C+hs+(u128)low[j].exact)+3,below=0,peak=0;bool ov=false;int tau=first_descent(N,below,peak,ov);if(ov)++lo;if(tau<0)++lf;if(tau>lm){lm=tau;lw=N;lb=below;}if(peak>lp)lp=peak;}}
  #pragma omp critical
  {raw+=lr;hard+=lh;fail+=lf;ovc+=lo;if(lm>gmax){gmax=lm;worst=lw;wbelow=lb;}if(lp>gpeak)gpeak=lp;}
 }
 std::cout<<"case="<<cs.name<<" chunk="<<chunk<<" raw="<<raw<<" hard="<<hard<<" failures="<<fail<<" overflows="<<ovc<<" max_tau="<<gmax<<" worst_N="<<s128(worst)<<" below="<<s128(wbelow)<<" max_peak="<<s128(gpeak)<<" total_hard="<<hardsum<<"\n";
 if(raw!=RAW[which][chunk]||hard!=HARD[which][chunk]||gmax!=TAU[which][chunk]||fail||ovc)return 2;
 return 0;
}
