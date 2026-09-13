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
using u64=std::uint64_t; using u128=unsigned __int128; using u32=std::uint32_t;
static constexpr u64 EXPECT_ROWS=605977, EXPECT_MASS=3419719061560ULL;
static u128 parse128(const std::string&s){u128 x=0;for(char c:s)x=x*10+(c-'0');return x;}
static u128 p3(int q){u128 x=1;while(q--)x*=3;return x;}
static u128 limv(int d,int q){u128 lo=((u128)1)<<71;u128 c=q?(((u128)1)<<(d-q))*(p3(q)-(((u128)1)<<q)):0;return (((((u128)1)<<d)*lo)-c)/p3(q);}
static u64 invmask(u64 a,u64 mask){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x&mask;}
struct Row{u128 N;u64 m,bmod,shift;int t;u64 ps=0,pe=0;};
struct Event{u64 pos;size_t row;bool start;};
struct G{u64 b,remmass;std::vector<size_t> ids;};
int main(int argc,char**argv){
 if(argc!=4){std::cerr<<"usage: math134 prepared.tsv batch_size skip_classes\n";return 2;}
 const int D=27;int TOP=std::stoi(argv[2]),SKIP=std::stoi(argv[3]);
 u64 MOD=1ULL<<D,MASK=MOD-1,PMOD=MOD>>1,PMASK=PMOD-1;
 std::vector<u128>vals;for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)vals.push_back(limv(d,q));
 std::sort(vals.begin(),vals.end());vals.erase(std::unique(vals.begin(),vals.end()),vals.end());int K=vals.size();
 std::vector<std::vector<int>>rank(D+1,std::vector<int>(D+1));
 for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)rank[d][q]=std::lower_bound(vals.begin(),vals.end(),limv(d,q))-vals.begin();
 std::vector<uint8_t>qp(2);qp[1]=1;std::vector<uint16_t>bp(2);bp[0]=rank[1][0];bp[1]=rank[1][1];
 for(int d=2;d<D;d++){u64 pm=1ULL<<(d-1),mask=pm-1;std::vector<uint8_t>qn(pm<<1);std::vector<uint16_t>bn(pm<<1);for(u64 s=0;s<pm;s++){u64 e=s<<1,o=e|1;qn[e]=qp[s];qn[o]=1+qp[(3*s+2)&mask];bn[e]=std::max<int>(bp[e&mask],rank[d][qn[e]]);bn[o]=std::max<int>(bp[o&mask],rank[d][qn[o]]);}qp.swap(qn);bp.swap(bn);}
 std::vector<u32>trans(MOD,0xffffffffu);std::vector<long long>gd(K+1);
 for(u64 s=0;s<PMOD;s++){u64 e=s<<1,o=e|1;int pe=bp[e&PMASK],ne=rank[D][qp[s]];if(ne>pe){trans[e]=((u32)pe<<16)|ne;gd[pe+1]++;gd[ne+1]--;}int qo=1+qp[(3*s+2)&PMASK],po=bp[o&PMASK],no=rank[D][qo];if(no>po){trans[o]=((u32)po<<16)|no;gd[po+1]++;gd[no+1]--;}}
 qp.clear();bp.clear();std::vector<u64>global(K+1);long long ac=0;for(int t=0;t<=K;t++){ac+=gd[t];global[t]=ac;}
 std::ifstream in(argv[1]);assert(in);std::vector<Row>rows;rows.reserve(EXPECT_ROWS);std::map<u64,std::vector<size_t>>gm;std::string as,bs;u64 m,total=0;
 while(in>>as>>bs>>m){u128 a=parse128(as),b=parse128(bs),N=a+b*(m-1);u64 bm=(u64)(b&MASK),shift=((u64)(a&MASK)*invmask(bm,MASK))&MASK;int t=std::lower_bound(vals.begin(),vals.end(),N)-vals.begin();size_t i=rows.size();rows.push_back({N,m,bm,shift,t});gm[bm].push_back(i);total+=m;}
 assert(rows.size()==EXPECT_ROWS&&total==EXPECT_MASS);
 std::vector<G>groups;for(auto &kv:gm){u64 rm=0;for(auto i:kv.second)rm+=rows[i].m&MASK;groups.push_back({kv.first,rm,std::move(kv.second)});}std::sort(groups.begin(),groups.end(),[](auto&a,auto&b){return a.remmass>b.remmass;});
 if(SKIP>(int)groups.size())SKIP=groups.size();if(SKIP+TOP>(int)groups.size())TOP=groups.size()-SKIP;groups.erase(groups.begin(),groups.begin()+SKIP);groups.resize(TOP);
 #pragma omp parallel for schedule(dynamic)
 for(int gi=0;gi<TOP;gi++){
  auto &gr=groups[gi];u64 b=gr.b;auto&ids=gr.ids;std::vector<int>tl;
  for(size_t i:ids)if((rows[i].m&MASK)&&rows[i].t<K)tl.push_back(rows[i].t);
  std::sort(tl.begin(),tl.end());tl.erase(std::unique(tl.begin(),tl.end()),tl.end());std::vector<int>up(K+1);for(int r=0;r<=K;r++)up[r]=std::upper_bound(tl.begin(),tl.end(),r)-tl.begin();std::unordered_map<int,int>tp;for(int j=0;j<(int)tl.size();j++)tp[tl[j]]=j;
  std::vector<Event>ev;ev.reserve(ids.size()*2);for(size_t i:ids){auto&r=rows[i];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;ev.push_back({r.shift,i,true});ev.push_back({(r.shift+rem)&MASK,i,false});}std::sort(ev.begin(),ev.end(),[](auto&a,auto&b){return a.pos<b.pos;});
  std::vector<long long>diff(tl.size()+1);size_t ei=0;u64 src=0;std::vector<u64>cur(tl.size());
  for(u64 pos=0;pos<=MOD;pos++){if(ei<ev.size()&&ev[ei].pos==pos){long long z=0;for(size_t j=0;j<tl.size();j++){z+=diff[j];cur[j]=z;}while(ei<ev.size()&&ev[ei].pos==pos){auto&e=ev[ei++];int j=tp[rows[e.row].t];if(e.start)rows[e.row].ps=cur[j];else rows[e.row].pe=cur[j];}}if(pos==MOD)break;u32 v=trans[src];if(v!=0xffffffffu){int p=v>>16,n=v&0xffffu,l=up[p],h=up[n];if(l<h){diff[l]++;diff[h]--;}}src=(src+b)&MASK;}
  u64 safe=0;for(size_t i:ids){auto&r=rows[i];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;safe+=(r.shift+rem<=MOD)?(r.pe-r.ps):((global[r.t]-r.ps)+r.pe);}
  #pragma omp critical
  {std::cout<<b<<"\t"<<gr.remmass<<"\t"<<safe<<"\n";}
 }
}
