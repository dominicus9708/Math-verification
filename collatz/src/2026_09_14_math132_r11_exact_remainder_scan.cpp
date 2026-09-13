#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using u64=std::uint64_t; using u128=unsigned __int128;
static constexpr u64 EXPECT_ROWS=605977, EXPECT_MASS=3419719061560ULL;
static u128 parse128(const std::string&s){u128 x=0;for(char c:s){assert(c>='0'&&c<='9');x=x*10+(c-'0');}return x;}
static u128 p3(int q){u128 x=1;while(q--)x*=3;return x;}
static u128 limv(int d,int q){u128 lo=((u128)1)<<71;u128 c=0;if(q)c=(((u128)1)<<(d-q))*(p3(q)-(((u128)1)<<q));return (((((u128)1)<<d)*lo)-c)/p3(q);}
static u64 invmask(u64 a,u64 mask){u64 x=a;for(int i=0;i<6;i++)x*=2-a*x;return x&mask;}
struct Row{u128 a,b,N;u64 m,bmod,shift;int t;u64 ps=0,pe=0;};
struct Event{u64 pos;size_t row;bool start;};
int main(int argc,char**argv){
 if(argc!=3){std::cerr<<"usage: math132 D prepared.tsv\n";return 2;}int D=std::stoi(argv[1]);assert(D>=23&&D<=26);u64 MOD=1ULL<<D,MASK=MOD-1,PMOD=1ULL<<(D-1),PMASK=PMOD-1;
 std::vector<u128> vals;for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)vals.push_back(limv(d,q));std::sort(vals.begin(),vals.end());vals.erase(std::unique(vals.begin(),vals.end()),vals.end());int K=vals.size();
 std::vector<std::vector<int>> rank(D+1,std::vector<int>(D+1));for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)rank[d][q]=std::lower_bound(vals.begin(),vals.end(),limv(d,q))-vals.begin();
 std::vector<uint16_t> best(PMOD);for(u64 r=0;r<PMOD;r++){u64 x=r;int q=0,b=-1;for(int d=1;d<D;d++){if(x&1){q++;x=(3*x+1)/2;}else x>>=1;b=std::max(b,rank[d][q]);}best[r]=b;}
 const uint16_t BAD=65535;std::vector<uint16_t> pr(MOD,BAD),nr(MOD,BAD);std::vector<long long> gd(K+1);for(u64 r=0;r<MOD;r++){u64 x=r;int q=0;for(int d=1;d<=D;d++){if(x&1){q++;x=(3*x+1)/2;}else x>>=1;}int p=best[r&PMASK],n=rank[D][q];if(n>p){pr[r]=p;nr[r]=n;gd[p+1]++;gd[n+1]--;}}
 std::vector<u64> global(K+1);long long acc=0;for(int t=0;t<=K;t++){acc+=gd[t];global[t]=acc;}
 std::ifstream in(argv[2]);assert(in);std::vector<Row> rows;rows.reserve(EXPECT_ROWS);std::map<u64,std::vector<size_t>> groups;std::string as,bs;u64 m,total=0;while(in>>as>>bs>>m){u128 a=parse128(as),b=parse128(bs),N=a+b*(m-1);u64 bm=(u64)(b&MASK);int t=std::lower_bound(vals.begin(),vals.end(),N)-vals.begin();u64 shift=((u64)(a&MASK)*invmask(bm,MASK))&MASK;size_t i=rows.size();rows.push_back({a,b,N,m,bm,shift,t});groups[bm].push_back(i);total+=m;}assert(rows.size()==EXPECT_ROWS&&total==EXPECT_MASS);
 u64 complete=0,remsafe=0;for(auto &kv:groups){u64 b=kv.first;auto &ids=kv.second;std::vector<int> tlist;for(size_t i:ids)if((rows[i].m&MASK)&&rows[i].t<K)tlist.push_back(rows[i].t);std::sort(tlist.begin(),tlist.end());tlist.erase(std::unique(tlist.begin(),tlist.end()),tlist.end());std::unordered_map<int,int> tpos;for(int j=0;j<(int)tlist.size();j++)tpos[tlist[j]]=j;std::vector<Event> ev;ev.reserve(ids.size()*2);for(size_t i:ids){auto&r=rows[i];u64 blocks=r.m>>D;if(r.t<K)complete+=blocks*global[r.t];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;ev.push_back({r.shift,i,true});ev.push_back({(r.shift+rem)&MASK,i,false});}std::sort(ev.begin(),ev.end(),[](auto&a,auto&b){return a.pos<b.pos;});std::vector<long long> diff(tlist.size()+1);size_t ei=0;u64 src=0;for(u64 pos=0;pos<=MOD;pos++){if(ei<ev.size()&&ev[ei].pos==pos){std::vector<u64> cur(tlist.size());long long z=0;for(size_t j=0;j<tlist.size();j++){z+=diff[j];cur[j]=z;}while(ei<ev.size()&&ev[ei].pos==pos){auto&e=ev[ei++];int j=tpos[rows[e.row].t];if(e.start)rows[e.row].ps=cur[j];else rows[e.row].pe=cur[j];}}if(pos==MOD)break;uint16_t p=pr[src];if(p!=BAD){uint16_t n=nr[src];auto l=std::upper_bound(tlist.begin(),tlist.end(),(int)p)-tlist.begin();auto h=std::upper_bound(tlist.begin(),tlist.end(),(int)n)-tlist.begin();if(l<h){diff[l]++;diff[h]--;}}src=(src+b)&MASK;}for(size_t i:ids){auto&r=rows[i];u64 rem=r.m&MASK;if(!rem||r.t>=K)continue;u64 c=(r.shift+rem<=MOD)?(r.pe-r.ps):((global[r.t]-r.ps)+r.pe);remsafe+=c;}}
 static std::map<int,u64> expect={{23,3151665357ULL},{24,17456818136ULL},{25,15350900431ULL},{26,5512456558ULL}};assert(complete==expect[D]);std::cout<<"depth\t"<<D<<"\nthreshold_levels\t"<<K<<"\nrows\t"<<rows.size()<<"\ntotal_mass\t"<<total<<"\ncomplete_increment\t"<<complete<<"\nremainder_increment\t"<<remsafe<<"\nexact_increment\t"<<(complete+remsafe)<<"\n";std::cerr<<"PASS MATH-132 exact remainder audit D="<<D<<"\n";
}
