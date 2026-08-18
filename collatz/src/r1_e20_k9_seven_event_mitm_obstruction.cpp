#include <algorithm>
#include <cstdint>
#include <iostream>
#include <functional>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using u128=unsigned __int128; using i128=__int128; using boost::multiprecision::cpp_int;
static constexpr int W=107,K=9; static u128 M=((u128)1<<W),MASK=M-1; static u128 A[8][W];
cpp_int invmod(cpp_int a,cpp_int m){cpp_int t=0,nt=1,r=m,nr=a;while(nr){cpp_int q=r/nr,x=t-q*nt;t=nt;nt=x;x=r-q*nr;r=nr;nr=x;}if(t<0)t+=m;return t;}
u128 from_cpp(const cpp_int&x){cpp_int mask=(cpp_int(1)<<64)-1;uint64_t lo=(uint64_t)(x&mask),hi=(uint64_t)((x>>64)&mask);return ((u128)hi<<64)|lo;}
void init_terms(){cpp_int mod=cpp_int(1)<<W,inv3=invmod(3,mod);for(int i=0;i<8;i++)for(int p=i;p<W;p++){cpp_int e=p-i,b=inv3,q=1;while(e){if((e&1)!=0)q=q*b%mod;b=b*b%mod;e>>=1;}A[i][p]=from_cpp(((cpp_int(1)<<p)*q)%mod);}}
std::pair<u128,u128> interval(){cpp_int N0("3939105844976711153619"),NMAX("5908625413101667397287"),num=1;for(int i=0;i<64;i++)num*=3;cpp_int den=cpp_int(1)<<73;return {from_cpp((num*(N0+1)+den-1)/den),from_cpp(num*(NMAX+512)/den)};}
bool formation(u128 target,int depth){std::vector<std::pair<int,i128>> st{{K,-(i128)target}};for(int d=0;d<depth;d++){std::vector<std::pair<int,i128>> nx;for(auto[a,c]:st)for(int a2=0;a2<=a;a2++){i128 z=c+(((i128)1)<<a)-(((i128)1)<<a2);if(z%3==0)nx.push_back({a2,2*(z/3)});}if(nx.empty())return false;std::sort(nx.begin(),nx.end(),[](auto&x,auto&y){return x.first<y.first||(x.first==y.first&&x.second<y.second);});nx.erase(std::unique(nx.begin(),nx.end()),nx.end());st.swap(nx);}return !st.empty();}
std::vector<uint64_t> targets(const std::vector<uint64_t>&c,uint64_t mod){std::vector<uint64_t>o;o.reserve(c.size());for(auto x:c)o.push_back(x?mod-x:0);std::sort(o.begin(),o.end());return o;}
struct Filters{uint64_t m15=0,m18=0,m21=0;std::vector<unsigned char>a15;std::vector<uint64_t>T18,T21;};
Filters make_filters(){std::vector<std::vector<uint64_t>>S(K+1,std::vector<uint64_t>{0});uint64_t mod=1;Filters f;for(int r=1;r<=21;r++){mod*=3;std::vector<std::vector<uint64_t>>N(K+1);for(int a=0;a<=K;a++){for(int a2=0;a2<=a;a2++){long long delta=(1LL<<a)-(1LL<<a2);for(uint64_t cp:S[a2]){uint64_t t=3*cp,half=(t&1)?(t+mod)/2:t/2;long long c=(long long)half-delta;c%=(long long)mod;if(c<0)c+=mod;N[a].push_back((uint64_t)c);}}std::sort(N[a].begin(),N[a].end());N[a].erase(std::unique(N[a].begin(),N[a].end()),N[a].end());}S.swap(N);if(r==15){f.m15=mod;auto T=targets(S[K],mod);f.a15.assign(mod,0);for(auto t:T)f.a15[t]=1;}if(r==18){f.m18=mod;f.T18=targets(S[K],mod);}if(r==21){f.m21=mod;f.T21=targets(S[K],mod);}}return f;}
struct NumEnum{int z,l;u128 lo,hi;std::vector<std::vector<u128>>L;std::function<void(u128)>cb;uint64_t count=0;NumEnum(int z_,u128 a,u128 b,std::function<void(u128)>c):z(z_),l(z_/2),lo(a),hi(b),L(W),cb(c){}
void lr(int d,int st,u128 s){if(d==l){int last=st-1;for(int m=last+1;m<W;m++)L[m].push_back(s);return;}int need=l-d;for(int p=st;p<=W-need;p++)lr(d+1,p+1,s+A[d][p]);}
void proc(u128 rs,int first){auto&v=L[first];u128 maxL=(u128)l*M-l;for(int q=1;q<=z;q++){i128 qlo=(i128)((u128)q*M-hi)-(i128)rs,qhi=(i128)((u128)q*M-lo)-(i128)rs;if(qhi<0||qlo>(i128)maxL)continue;u128 a=qlo<0?0:(u128)qlo,b=qhi>(i128)maxL?maxL:(u128)qhi;if(a>b)continue;auto it=std::lower_bound(v.begin(),v.end(),a),en=std::upper_bound(v.begin(),v.end(),b);for(;it!=en;++it){u128 s=*it+rs,r=s&MASK,U=r?M-r:0;if(U>=lo&&U<=hi){count++;cb(U);}}}}
void rr(int d,int st,u128 s,int first){if(d==z){proc(s,first);return;}int need=z-d;for(int p=st;p<=W-need;p++)rr(d+1,p+1,s+A[d][p],first<0?p:first);}
void run(){if(z==0){if((u128)0>=lo&&(u128)0<=hi){count++;cb(0);}return;}lr(0,0,0);for(auto&v:L)std::sort(v.begin(),v.end());rr(l,l,0,-1);}};
int main(){init_terms();auto F=make_filters();auto[lo,hi]=interval();uint64_t numeric=0,c15=0,c18=0,c21=0;std::vector<u128>surv21;for(int z=0;z<=7;z++){NumEnum en(z,lo,hi,[&](u128 U){numeric++;uint64_t t15=(uint64_t)((U<<K)%F.m15);if(!F.a15[t15])return;c15++;uint64_t t18=(uint64_t)((U<<K)%F.m18);if(!std::binary_search(F.T18.begin(),F.T18.end(),t18))return;c18++;uint64_t t21=(uint64_t)((U<<K)%F.m21);if(!std::binary_search(F.T21.begin(),F.T21.end(),t21))return;c21++;surv21.push_back(U);});en.run();}
std::cout<<"numeric="<<numeric<<" K15="<<c15<<" K18="<<c18<<" K21="<<c21<<"\n";std::vector<u128>cur=std::move(surv21);for(int d:{24,27,30,33,36}){std::vector<u128>nx;for(u128 U:cur)if(formation(U<<K,d))nx.push_back(U);std::cout<<"K"<<d<<"="<<nx.size()<<"\n";cur.swap(nx);}if(numeric!=123546096||c15!=5560638||c18!=871631||c21!=109482||!cur.empty())return 1;std::cout<<"R1 E20 k9: PASS\n";}
