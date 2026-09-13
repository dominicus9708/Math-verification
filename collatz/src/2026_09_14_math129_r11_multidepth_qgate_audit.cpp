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
static constexpr int D=22; static constexpr u64 MOD=1ULL<<D, MASK=MOD-1; static constexpr int BS=512; static constexpr int NB=MOD/BS;
static constexpr u64 EXPECT_ROWS=605977, EXPECT_MASS=3419719061560ULL;
static constexpr u64 EXPECT_SAFE=3209065424947ULL, EXPECT_TAIL=210653636613ULL;
static const cpp_int LO=cpp_int(1)<<71;
struct Row{cpp_int a,b,N;u64 m,amod,bmod;u64 adapt;};
static cpp_int P2[35], P3[35]; static u64 C[35][35], SW[35][35];
static cpp_int parse_big(const std::string&s){cpp_int x=0;for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=(c-'0');}return x;}
static u64 mod_u64(const cpp_int&x){return (x%MOD).convert_to<u64>();}
static u64 inv22(u64 a){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x&MASK;}
static cpp_int lim(int d,int q){cpp_int cmax=0;if(q)cmax=P2[d-q]*(P3[q]-P2[q]);return ((P2[d]*LO-cmax)/P3[q]);}
static int qsafe(int d,const cpp_int&N){int best=-1;for(int q=0;q<=d;q++){if(N<=lim(d,q))best=q;else break;}return best;}
int main(int argc,char**argv){if(argc!=2){std::cerr<<"usage: math129 source.tsv\n";return 2;}
 P2[0]=1;P3[0]=1;for(int q=1;q<=34;q++){P2[q]=P2[q-1]*2;P3[q]=P3[q-1]*3;}for(int d=0;d<=34;d++){C[d][0]=C[d][d]=1;for(int q=1;q<d;q++)C[d][q]=C[d-1][q-1]+C[d-1][q];u64 s=0;for(int q=0;q<=d;q++){s+=C[d][q];SW[d][q]=s;}}
 std::vector<cpp_int> vals;for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)vals.push_back(lim(d,q));std::sort(vals.begin(),vals.end());vals.erase(std::unique(vals.begin(),vals.end()),vals.end());
 int rank[23][23];for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)rank[d][q]=std::lower_bound(vals.begin(),vals.end(),lim(d,q))-vals.begin();int K=vals.size();
 std::vector<uint16_t> baseRank(MOD);std::vector<u64> global(K,0);for(u64 r=0;r<MOD;r++){u64 x=r;int q=0,best=-1;for(int d=1;d<=D;d++){if(x&1){q++;x=(3*x+1)/2;}else x/=2;best=std::max(best,rank[d][q]);}baseRank[r]=best;global[best]++;}
 for(int i=K-2;i>=0;i--)global[i]+=global[i+1];
 std::ifstream in(argv[1]);assert(in);std::vector<Row>rows;rows.reserve(EXPECT_ROWS);std::map<u64,std::vector<size_t>>groups;std::string as,bs;u64 m,total=0;
 while(in>>as>>bs>>m){cpp_int a=parse_big(as),b=parse_big(bs),N=a+b*(m-1);u64 adapt=0;for(int d=1;d<=34;d++){int q=qsafe(d,N);if(q<0)continue;u64 blocks=m>>d;if(!blocks)continue;adapt=std::max(adapt,blocks*SW[d][q]);}size_t idx=rows.size();rows.push_back({a,b,N,m,mod_u64(a),mod_u64(b),adapt});groups[rows.back().bmod].push_back(idx);total+=m;}
 assert(rows.size()==EXPECT_ROWS&&total==EXPECT_MASS);
 u64 multi=0,hybrid=0;u64 multiWin=0,adaptWin=0,tie=0;
 for(auto&kv:groups){u64 b=kv.first,inv=inv22(b);std::vector<uint16_t> seq(MOD);for(u64 k=0;k<MOD;k++)seq[k]=baseRank[(b*k)&MASK];
   std::vector<uint32_t> suf((size_t)NB*(K+1));
   for(int bl=0;bl<NB;bl++){auto* row=&suf[(size_t)bl*(K+1)];for(int j=0;j<BS;j++)row[seq[(u64)bl*BS+j]]++;for(int c=K-2;c>=0;c--)row[c]+=row[c+1];}
   auto countRange=[&](u64 l,u64 len,int thr)->u64{if(len==0||thr>=K)return 0;u64 r=l+len;auto linear=[&](u64 L,u64 R)->u64{u64 z=0;while(L<R && (L%BS)){z+=seq[L]>=thr;L++;}while(R>L && (R%BS)){--R;z+=seq[R]>=thr;}while(L<R){int bl=L/BS;z+=suf[(size_t)bl*(K+1)+thr];L+=BS;}return z;};if(r<=MOD)return linear(l,r);return linear(l,MOD)+linear(0,r-MOD);};
   for(size_t idx:kv.second){auto&r=rows[idx];int thr=std::lower_bound(vals.begin(),vals.end(),r.N)-vals.begin();u64 cycles=r.m/MOD,rem=r.m%MOD,shift=(r.amod*inv)&MASK;u64 exact=0;if(thr<K)exact=cycles*global[thr]+countRange(shift,rem,thr);multi+=exact;u64 h=std::max(exact,r.adapt);hybrid+=h;if(exact>r.adapt)multiWin++;else if(r.adapt>exact)adaptWin++;else tie++;assert(h<=r.m);}
 }
 std::cout<<"threshold_levels\t"<<K<<"\n"<<"rows\t"<<rows.size()<<"\n"<<"total_mass\t"<<total<<"\n"<<"multidepth_d1_22_exact_safe_mass\t"<<multi<<"\n"<<"multidepth_d1_22_tail_mass\t"<<(total-multi)<<"\n"<<"hybrid_with_adaptive_d1_34_safe_mass\t"<<hybrid<<"\n"<<"hybrid_tail_mass\t"<<(total-hybrid)<<"\n"<<"multidepth_wins_pieces\t"<<multiWin<<"\n"<<"adaptive_wins_pieces\t"<<adaptWin<<"\n"<<"ties_pieces\t"<<tie<<"\n";
 assert(multi==EXPECT_SAFE);assert(total-multi==EXPECT_TAIL);assert(hybrid==EXPECT_SAFE);
 std::cerr<<"PASS MATH-129 exact multi-depth q-gate audit\nNO r=11 CLOSURE CLAIM\n";
}
