// MATH-099 stage B: compact 2-adic carry verifier for one-paid macro depth 14.
// Input tables are emitted by the MATH-099 stage-A exporter.
// Root shards are independent; cross-root duplicates are intentionally not merged.
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_int/misc.hpp>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using boost::multiprecision::uint256_t; using std::uint64_t;
struct Edge{int h,q;uint256_t A,Be;};struct Tr{int ei,cpid;};struct Root{int H,pid;uint256_t M,x,g;};struct State{int H,pid;uint256_t M,x,g;};
static inline uint64_t limb(const uint256_t&x,int k){return static_cast<uint64_t>(x>>(64*k));}
static inline bool less_state(const State&a,const State&b){if(a.H!=b.H)return a.H<b.H;if(a.pid!=b.pid)return a.pid<b.pid;for(int k=1;k>=0;--k){auto x=limb(a.M,k),y=limb(b.M,k);if(x!=y)return x<y;}for(int k=2;k>=0;--k){auto x=limb(a.x,k),y=limb(b.x,k);if(x!=y)return x<y;}for(int k=2;k>=0;--k){auto x=limb(a.g,k),y=limb(b.g,k);if(x!=y)return x<y;}return false;}
static inline bool eq_state(const State&a,const State&b){return a.H==b.H&&a.pid==b.pid&&a.M==b.M&&a.x==b.x&&a.g==b.g;}
static inline int ceil_log2(const uint256_t&m){if(m<=1)return 0;return boost::multiprecision::msb(m-1)+1;}static inline uint256_t maskbits(int b){return b>=256?~uint256_t(0):(uint256_t(1)<<b)-1;}
struct Key{int q,b;bool operator==(Key const&o)const{return q==o.q&&b==o.b;}};struct KH{size_t operator()(Key const&k)const{return(size_t(k.q)<<16)^size_t(k.b);}};std::unordered_map<Key,uint256_t,KH>IC;
uint256_t inv3base(int bits){uint256_t inv=1;int k=1;while(k<bits){int nk=std::min(bits,2*k);auto m=maskbits(nk);inv=(inv*(uint256_t(2)-uint256_t(3)*inv))&m;k=nk;}return inv&maskbits(bits);}uint256_t pows(uint256_t a,int e,int bits){auto m=maskbits(bits);uint256_t r=1;a&=m;while(e){if(e&1)r=(r*a)&m;a=(a*a)&m;e>>=1;}return r;}uint256_t inv3pow(int q,int bits){Key k{q,bits};auto it=IC.find(k);if(it!=IC.end())return it->second;auto v=pows(inv3base(bits),q,bits);IC.emplace(k,v);return v;}
std::vector<std::string>split(const std::string&s){std::vector<std::string>v;std::stringstream z(s);std::string x;while(std::getline(z,x,'\t'))v.push_back(x);return v;}
int main(int argc,char**argv){int start=0,stop=1000000;if(argc>1)start=std::stoi(argv[1]);if(argc>2)stop=std::stoi(argv[2]);std::vector<Edge>E;{std::ifstream f("t14_edges.tsv");std::string s;while(std::getline(f,s)){auto p=split(s);int id=std::stoi(p[0]);if((int)E.size()<=id)E.resize(id+1);E[id]={std::stoi(p[1]),std::stoi(p[2]),uint256_t(p[3]),uint256_t(p[4])};}}static std::vector<Tr>T[14][72][200];{std::ifstream f("t14_trans.tsv");std::string s;while(std::getline(f,s)){auto p=split(s);T[std::stoi(p[0])][std::stoi(p[1])][std::stoi(p[2])].push_back({std::stoi(p[3]),std::stoi(p[5])});}}static std::vector<int>TERM[72][200];{std::ifstream f("t14_term.tsv");std::string s;while(std::getline(f,s)){auto p=split(s);TERM[std::stoi(p[0])][std::stoi(p[1])].push_back(std::stoi(p[2]));}}std::vector<Root>roots;{std::ifstream f("t14_roots.tsv");std::string s;while(std::getline(f,s)){auto p=split(s);roots.push_back({std::stoi(p[1]),std::stoi(p[5]),uint256_t(p[2]),uint256_t(p[3]),uint256_t(p[4])});}}stop=std::min(stop,(int)roots.size());
unsigned long long TT=0,CC=0,PP=0;size_t PK=0;uint256_t GG=0;bool HG=false;for(int ri=start;ri<stop;++ri){std::vector<State>cur{{roots[ri].H,roots[ri].pid,roots[ri].M,roots[ri].x,roots[ri].g}},nxt;size_t peak=1;for(int d=1;d<13&&!cur.empty();++d){nxt.clear();for(auto const&s:cur){int R=ceil_log2(s.M),P=73+R;auto mP=maskbits(P);for(auto const&t:T[d][s.H][s.pid]){auto const&e=E[t.ei];auto eta=(s.g*e.A)&mP;auto r=(eta-s.x)&maskbits(e.h);if(r>=s.M)continue;auto Mp=(s.M-1-r)/(uint256_t(1)<<e.h)+1;if(Mp<=1)continue;int Rp=ceil_log2(Mp);if(Rp>R-e.h)return 2;auto delta=(s.x+r-eta)&mP;if((delta&maskbits(e.h))!=0)return 3;int Pav=P-e.h;auto mA=maskbits(Pav);auto high=(delta>>e.h)&mA;auto gq=(s.g*inv3pow(e.q,Pav))&mA;auto xq=(high+gq*e.Be)&mA;int Pp=73+Rp;auto mp=maskbits(Pp);nxt.push_back({s.H+e.h,t.cpid,Mp,xq&mp,gq&mp});}}std::sort(nxt.begin(),nxt.end(),less_state);nxt.erase(std::unique(nxt.begin(),nxt.end(),eq_state),nxt.end());cur.swap(nxt);peak=std::max(peak,cur.size());}
unsigned long long tries=0,ok=0;uint256_t mg=0;bool hg=false;for(auto const&s:cur){int R=ceil_log2(s.M),P=73+R;auto mP=maskbits(P);for(int ei:TERM[s.H][s.pid]){auto const&e=E[ei];if(e.h-R<42)continue;++tries;auto eta=(s.g*e.A)&mP;auto r=(eta-s.x)&maskbits(e.h);if(r<s.M)++ok;else{auto gap=r-s.M;if(!hg||gap<mg){mg=gap;hg=true;}}}}TT+=tries;CC+=ok;PP+=cur.size();PK=std::max(PK,peak);if(hg&&(!HG||mg<GG)){GG=mg;HG=true;}std::cout<<"root\t"<<ri<<"\ttries\t"<<tries<<"\tcompatible\t"<<ok<<"\tparents\t"<<cur.size()<<"\tpeak\t"<<peak<<"\tmin_gap\t"<<(hg?mg:uint256_t(0))<<"\n";}
std::cout<<"TOTAL\ttries\t"<<TT<<"\tcompatible\t"<<CC<<"\tparents\t"<<PP<<"\tpeak\t"<<PK<<"\tmin_gap\t"<<(HG?GG:uint256_t(0))<<"\n";return CC==0?0:4;}
