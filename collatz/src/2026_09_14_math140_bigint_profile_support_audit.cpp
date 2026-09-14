// MATH-140 support certificate: arbitrary-precision q-gate profile-support audit.
// Used to verify that fixed-width unsigned __int128 threshold arithmetic becomes
// invalid once D+71 reaches 128, i.e. from D=57 onward.
#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using boost::multiprecision::cpp_int;
using u64=std::uint64_t;
static cpp_int parse_big(const std::string&s){cpp_int x=0;for(char c:s){x*=10;x+=c-'0';}return x;}
static cpp_int p3(int q){cpp_int x=1;while(q--)x*=3;return x;}
static cpp_int limv(int d,int q){cpp_int B=cpp_int(1)<<71;cpp_int p=p3(q);cpp_int c=q?(cpp_int(1)<<(d-q))*(p-(cpp_int(1)<<q)):0;return (((cpp_int(1)<<d)*B)-c)/p;}
static int qsafe(int d,const cpp_int&N,const std::vector<std::vector<cpp_int>>&L){int lo=0,hi=d+1;while(lo<hi){int m=(lo+hi)/2;if(N<=L[d][m])lo=m+1;else hi=m;}return lo-1;}
int main(int argc,char**argv){if(argc!=4){std::cerr<<"usage: start_depth end_depth prepared.tsv\n";return 2;}int A=std::stoi(argv[1]),Z=std::stoi(argv[2]);std::ifstream in(argv[3]);std::string as,bs;u64 m;std::vector<cpp_int> Ns;while(in>>as>>bs>>m){cpp_int a=parse_big(as),b=parse_big(bs);Ns.push_back(a+b*(m-1));}std::sort(Ns.begin(),Ns.end());
for(int D=A;D<=Z;D++){std::vector<std::vector<cpp_int>>L(D+1);for(int d=1;d<=D;d++){L[d].resize(d+1);for(int q=0;q<=d;q++)L[d][q]=limv(d,q);}std::vector<cpp_int>bounds;std::vector<int>prev;for(size_t i=0;i<Ns.size();i++){std::vector<int>cur(D);for(int d=1;d<=D;d++)cur[d-1]=qsafe(d,Ns[i],L);if(i==0||cur!=prev){if(i)bounds.push_back(Ns[i-1]);prev.swap(cur);}}bounds.push_back(Ns.back());int NP=bounds.size();std::vector<std::vector<int>>H(D+1,std::vector<int>(D+1,-1));for(int d=1;d<=D;d++)for(int q=0;q<=d;q++)H[d][q]=(int)(std::upper_bound(bounds.begin(),bounds.end(),L[d][q])-bounds.begin())-1;std::map<std::pair<int,int>,cpp_int>st;st[{0,-1}]=1;for(int d=1;d<D;d++){std::map<std::pair<int,int>,cpp_int>ns;for(auto&kv:st){auto[q,b]=kv.first;cpp_int c=kv.second;for(int e=0;e<2;e++){int qq=q+e,bb=std::max(b,H[d][qq]);if(H[D][qq]<=bb)continue;ns[{qq,bb}]+=c;}}st.swap(ns);}std::map<std::pair<int,int>,cpp_int>pats;cpp_int support=0;for(auto&kv:st){auto[q,b]=kv.first;cpp_int c=kv.second;for(int e=0;e<2;e++){int nh=H[D][q+e];if(nh>b){support+=c;pats[{b,nh}]+=c;}}}std::cout<<D<<'\t'<<NP<<'\t'<<pats.size()<<'\t'<<support<<'\t'<<st.size()<<'\n';}
}
