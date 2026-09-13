#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using u64=std::uint64_t; using u128=unsigned __int128;
static constexpr u64 EXPECT_ROWS=605977, EXPECT_MASS=3419719061560ULL;
static u128 parse128(const std::string&s){u128 x=0;for(char c:s){x=x*10+(c-'0');}return x;}
static u128 p3(int q){u128 x=1;while(q--)x*=3;return x;}
static u128 limv(int d,int q){u128 lo=((u128)1)<<71;u128 c=q?(((u128)1)<<(d-q))*(p3(q)-(((u128)1)<<q)):0;return (((((u128)1)<<d)*lo)-c)/p3(q);}
static u64 invmask(u64 a,u64 mask){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x&mask;}
struct Row{u128 N;u64 m,bmod,shift;int t;u64 ps=0,pe=0;};
struct Event{u64 pos;size_t row;bool start;};
int main(int argc,char**argv){
 if(argc!=3){std::cerr<<"usage: math133 D prepared.tsv\n";return 2;}
 int D=std::stoi(argv[1]);assert(D>=23&&D<=28);u64 MOD=1ULL<<D,MASK=MOD-1,PMOD=MOD>>1,PMASK=PMOD-1;
 std::vector<u128> vals;for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)vals.push_back(limv(d,q));
 std::sort(vals.begin(),vals.end());vals.erase(std::unique(vals.begin(),vals.end()),vals.end());int K=vals.size();
 std::vector<std::vector<int>> rank(D+1,std::vector<int>(D+1));
 for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)rank[d][q]=std::lower_bound(vals.begin(),vals.end(),limv(d,q))-vals.begin();

 // Exact O(2^D) parity-count recursion. For n=2s the remaining parity word
 // is that of s. For n=2s+1 the first odd step maps to 3s+2.
 std::vector<uint8_t> qprev(2);qprev[0]=0;qprev[1]=1;
 std::vector<uint16_t> bprev(2);bprev[0]=rank[1][0];bprev[1]=rank[1][1];
 for(int d=2;d<D;d++){
   u64 pm=1ULL<<(d-1),mask=pm-1;std::vector<uint8_t> qnew(pm<<1);std::vector<uint16_t> bnew(pm<<1);
   for(u64 s=0;s<pm;s++){
     u64 e=s<<1,o=e|1;
     qnew[e]=qprev[s];
     qnew[o]=1+qprev[(3*s+2)&mask];
     bnew[e]=std::max<int>(bprev[e&mask],rank[d][qnew[e]]);
     bnew[o]=std::max<int>(bprev[o&mask],rank[d][qnew[o]]);
   }
   qprev.swap(qnew);bprev.swap(bnew);
 }
 assert(qprev.size()==PMOD&&bprev.size()==PMOD);
 std::vector<uint8_t> qcur(MOD);
 for(u64 s=0;s<PMOD;s++){u64 e=s<<1,o=e|1;qcur[e]=qprev[s];qcur[o]=1+qprev[(3*s+2)&PMASK];}

 const uint16_t BAD=65535;
 std::vector<uint16_t> pr(MOD,BAD),nr(MOD,BAD);std::vector<long long> gd(K+1);
 for(u64 r=0;r<MOD;r++){
   int p=bprev[r&PMASK],n=rank[D][qcur[r]];
   if(n>p){pr[r]=p;nr[r]=n;gd[p+1]++;gd[n+1]--;}
 }
 qcur.clear();qcur.shrink_to_fit();qprev.clear();qprev.shrink_to_fit();bprev.clear();bprev.shrink_to_fit();
 std::vector<u64> global(K+1);long long ac=0;for(int t=0;t<=K;t++){ac+=gd[t];global[t]=ac;}

 std::ifstream in(argv[2]);assert(in);std::vector<Row> rows;rows.reserve(EXPECT_ROWS);std::map<u64,std::vector<size_t>> gm;
 std::string as,bs;u64 m,total=0;
 while(in>>as>>bs>>m){
   u128 a=parse128(as),b=parse128(bs),N=a+b*(m-1);u64 bm=(u64)(b&MASK),shift=((u64)(a&MASK)*invmask(bm,MASK))&MASK;
   int t=std::lower_bound(vals.begin(),vals.end(),N)-vals.begin();size_t i=rows.size();rows.push_back({N,m,bm,shift,t});gm[bm].push_back(i);total+=m;
 }
 assert(rows.size()==EXPECT_ROWS&&total==EXPECT_MASS);
 std::vector<std::pair<u64,std::vector<size_t>>> groups;for(auto&x:gm)groups.push_back(std::move(x));
 u64 complete=0,remsafe=0;
 #pragma omp parallel for schedule(dynamic) reduction(+:complete,remsafe)
 for(long long gi=0;gi<(long long)groups.size();gi++){
   u64 b=groups[gi].first;auto&ids=groups[gi].second;std::vector<int> tl;
   for(size_t i:ids)if((rows[i].m&MASK)&&rows[i].t<K)tl.push_back(rows[i].t);
   std::sort(tl.begin(),tl.end());tl.erase(std::unique(tl.begin(),tl.end()),tl.end());
   std::vector<int> up(K+1);for(int r=0;r<=K;r++)up[r]=std::upper_bound(tl.begin(),tl.end(),r)-tl.begin();
   std::unordered_map<int,int> tp;for(int j=0;j<(int)tl.size();j++)tp[tl[j]]=j;
   std::vector<Event> ev;ev.reserve(ids.size()*2);
   for(size_t i:ids){auto&r=rows[i];u64 blocks=r.m>>D;if(r.t<K)complete+=blocks*global[r.t];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;ev.push_back({r.shift,i,true});ev.push_back({(r.shift+rem)&MASK,i,false});}
   std::sort(ev.begin(),ev.end(),[](auto&a,auto&b){return a.pos<b.pos;});
   std::vector<long long> diff(tl.size()+1);size_t ei=0;u64 src=0;std::vector<u64> cur(tl.size());
   for(u64 pos=0;pos<=MOD;pos++){
     if(ei<ev.size()&&ev[ei].pos==pos){
       long long z=0;for(size_t j=0;j<tl.size();j++){z+=diff[j];cur[j]=z;}
       while(ei<ev.size()&&ev[ei].pos==pos){auto&e=ev[ei++];int j=tp[rows[e.row].t];if(e.start)rows[e.row].ps=cur[j];else rows[e.row].pe=cur[j];}
     }
     if(pos==MOD)break;
     uint16_t p=pr[src];if(p!=BAD){uint16_t n=nr[src];int l=up[p],h=up[n];if(l<h){diff[l]++;diff[h]--;}}
     src=(src+b)&MASK;
   }
   for(size_t i:ids){auto&r=rows[i];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;u64 c=(r.shift+rem<=MOD)?(r.pe-r.ps):((global[r.t]-r.ps)+r.pe);remsafe+=c;}
 }
 static std::map<int,u64> expect={{23,3151665357ULL},{24,17456818136ULL},{25,15350900431ULL},{26,5512456558ULL},{27,13125146222ULL},{28,5153825838ULL}};
 assert(complete==expect[D]);
 std::cout<<"depth\t"<<D<<"\nthreshold_levels\t"<<K<<"\ncomplete_increment\t"<<complete<<"\nremainder_increment\t"<<remsafe<<"\nexact_increment\t"<<(complete+remsafe)<<"\n";
 std::cerr<<"PASS optimized exact remainder D="<<D<<"\n";
}
