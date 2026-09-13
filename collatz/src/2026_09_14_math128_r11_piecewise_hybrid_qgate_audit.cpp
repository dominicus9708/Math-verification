#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int; using u64=std::uint64_t;
struct Row{cpp_int a,b,N;u64 m,amod,bmod;int qs22;u64 adaptive=0,exact22=0;int bestd=0;};
static constexpr int D22=22; static constexpr u64 MOD=1ULL<<D22, MASK=MOD-1;
static constexpr u64 EXPECT_ROWS=605977, EXPECT_MASS=3419719061560ULL;
static constexpr u64 EXPECT_ADAPT=2971304357696ULL;
static constexpr u64 EXPECT_D22=2904383883175ULL;
static constexpr u64 EXPECT_COMBINED=2987225373882ULL;
static constexpr u64 EXPECT_TAIL=432493687678ULL;
static const cpp_int LO=cpp_int(1)<<71;
static cpp_int p3[35]; static u64 combv[35][35], safeWords[35][35];
static cpp_int parse_big(const std::string&s){cpp_int x=0;for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=(c-'0');}return x;}
static u64 mod_u64(const cpp_int&x,u64 mod){return (x%mod).convert_to<u64>();}
static u64 inv22(u64 a){assert(a&1);u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x&MASK;}
static int qsafe(int d,const cpp_int&N){int best=-1;for(int q=0;q<=d;q++){cpp_int cmax=0;if(q)cmax=(cpp_int(1)<<(d-q))*(p3[q]-(cpp_int(1)<<q));cpp_int lhs=p3[q]*N+cmax, rhs=(cpp_int(1)<<d)*LO;if(lhs<=rhs)best=q;else break;}return best;}
static int odd_count22(u64 n){int q=0;u64 x=n;for(int i=0;i<D22;i++){if(x&1){q++;x=(3*x+1)/2;}else x/=2;}return q;}
static u64 cyc(const std::vector<uint32_t>&p,u64 s,u64 len){if(!len)return 0;u64 e=s+len;if(e<=MOD)return p[e]-p[s];return p[MOD]-p[s]+p[e-MOD];}
int main(int argc,char**argv){if(argc!=2){std::cerr<<"usage: math128 source.tsv\n";return 2;}
 p3[0]=1;for(int q=1;q<=34;q++)p3[q]=p3[q-1]*3;
 for(int d=0;d<=34;d++){combv[d][0]=combv[d][d]=1;for(int q=1;q<d;q++)combv[d][q]=combv[d-1][q-1]+combv[d-1][q];u64 s=0;for(int q=0;q<=d;q++){s+=combv[d][q];safeWords[d][q]=s;}}
 std::ifstream in(argv[1]);assert(in);std::vector<Row>rows;rows.reserve(EXPECT_ROWS);std::map<u64,std::vector<size_t>>groups;u64 total=0;std::string as,bs;u64 m;
 while(in>>as>>bs>>m){cpp_int a=parse_big(as),b=parse_big(bs),N=a+b*(m-1);int q22=qsafe(22,N);assert(q22==12||q22==13);Row r{a,b,N,m,mod_u64(a,MOD),mod_u64(b,MOD),q22};
   for(int d=1;d<=34;d++){int q=qsafe(d,N);if(q<0)continue;u64 blocks = d>=64?0:(m>>d); if(!blocks)continue;u64 credit=blocks*safeWords[d][q]; if(credit>r.adaptive){r.adaptive=credit;r.bestd=d;}}
   size_t idx=rows.size();rows.push_back(std::move(r));groups[rows.back().bmod].push_back(idx);total+=m;}
 assert(rows.size()==EXPECT_ROWS&&total==EXPECT_MASS&&groups.size()==32);
 std::vector<uint8_t>qv(MOD);for(u64 r=0;r<MOD;r++)qv[r]=odd_count22(r);
 for(auto&kv:groups){u64 bmod=kv.first,inv=inv22(bmod);std::vector<uint32_t>p12(MOD+1),p13(MOD+1);for(u64 k=0;k<MOD;k++){int q=qv[(bmod*k)&MASK];p12[k+1]=p12[k]+(q<=12);p13[k+1]=p13[k]+(q<=13);}for(size_t idx:kv.second){auto&r=rows[idx];auto&p=(r.qs22==12?p12:p13);u64 cycN=r.m/MOD,rem=r.m%MOD,shift=(r.amod*inv)&MASK;r.exact22=cycN*(u64)p[MOD]+cyc(p,shift,rem);}}
 u64 adapt=0,d22=0,combined=0,adaptWin=0,d22Win=0,tie=0;std::map<int,u64>bestdhist;
 for(auto&r:rows){adapt+=r.adaptive;d22+=r.exact22;u64 c=std::max(r.adaptive,r.exact22);combined+=c;if(r.adaptive>r.exact22)adaptWin++;else if(r.exact22>r.adaptive)d22Win++;else tie++;bestdhist[r.bestd]++;assert(c<=r.m);}
 std::cout<<"rows\t"<<rows.size()<<"\n"<<"total_mass\t"<<total<<"\n"<<"adaptive_complete_block_safe_mass\t"<<adapt<<"\n"<<"exact_d22_safe_mass\t"<<d22<<"\n"<<"combined_piecewise_max_safe_mass\t"<<combined<<"\n"<<"combined_tail_mass\t"<<(total-combined)<<"\n"<<"adaptive_wins_pieces\t"<<adaptWin<<"\n"<<"d22_wins_pieces\t"<<d22Win<<"\n"<<"ties_pieces\t"<<tie<<"\n";
 std::cout<<"best_depth_hist";for(auto &kv:bestdhist)std::cout<<"\t"<<kv.first<<":"<<kv.second;std::cout<<"\n";
 assert(adapt==EXPECT_ADAPT);assert(d22==EXPECT_D22);assert(combined==EXPECT_COMBINED);assert(total-combined==EXPECT_TAIL);
 std::cerr<<"PASS MATH-128 r11 piecewise hybrid q-gate audit\nNO r=11 CLOSURE CLAIM\n";
}
