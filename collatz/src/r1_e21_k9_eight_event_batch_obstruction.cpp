#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <utility>
#include <boost/multiprecision/cpp_int.hpp>
using u128=unsigned __int128; using i128=__int128; using boost::multiprecision::cpp_int; using u64=uint64_t;
static constexpr int W=109,K=9; static constexpr u64 M15=14348907ULL,M18=387420489ULL,M21=10460353203ULL; static u128 M=((u128)1<<W),MASK=M-1,A[8][W];
cpp_int invmod(cpp_int a,cpp_int m){cpp_int t=0,nt=1,r=m,nr=a;while(nr){cpp_int q=r/nr,x=t-q*nt;t=nt;nt=x;x=r-q*nr;r=nr;nr=x;}if(t<0)t+=m;return t;}
u128 from_cpp(const cpp_int&x){cpp_int mask=(cpp_int(1)<<64)-1;u64 lo=(u64)(x&mask),hi=(u64)((x>>64)&mask);return ((u128)hi<<64)|lo;}
void init_terms(){cpp_int mod=cpp_int(1)<<W,inv3=invmod(3,mod);for(int i=0;i<8;i++)for(int p=i;p<W;p++){cpp_int e=p-i,b=inv3,q=1;while(e){if((e&1)!=0)q=q*b%mod;b=b*b%mod;e>>=1;}A[i][p]=from_cpp(((cpp_int(1)<<p)*q)%mod);}}
std::pair<u128,u128> interval(){cpp_int N0("3939105844976711153619"),NMAX("5908625413101667397287"),num=1;for(int i=0;i<64;i++)num*=3;cpp_int den=cpp_int(1)<<73;return{from_cpp((num*(N0+1)+den-1)/den),from_cpp(num*(NMAX+512)/den)};}
bool formation(u128 target,int depth){std::vector<std::pair<int,i128>>st{{K,-(i128)target}};for(int d=0;d<depth;d++){std::vector<std::pair<int,i128>>nx;for(auto[a,c]:st)for(int a2=0;a2<=a;a2++){i128 z=c+(((i128)1)<<a)-(((i128)1)<<a2);if(z%3==0)nx.push_back({a2,2*(z/3)});}if(nx.empty())return false;std::sort(nx.begin(),nx.end(),[](auto&x,auto&y){return x.first<y.first||(x.first==y.first&&x.second<y.second);});nx.erase(std::unique(nx.begin(),nx.end()),nx.end());st.swap(nx);}return !st.empty();}
struct Bits{u64 mod;std::vector<u64>b;bool has(u64 x)const{return (b[x>>6]>>(x&63))&1ULL;}};
Bits loadbits(const char*fn){std::ifstream f(fn,std::ios::binary);Bits x;u64 n;f.read((char*)&x.mod,8);f.read((char*)&n,8);x.b.resize(n);f.read((char*)x.b.data(),n*8);return x;}
std::pair<u64,std::vector<u64>> loadvec(const char*fn){std::ifstream f(fn,std::ios::binary);u64 m,n;f.read((char*)&m,8);f.read((char*)&n,8);std::vector<u64>v(n);f.read((char*)v.data(),n*8);return{m,std::move(v)};}
inline u64 tm15(u128 U){return (u64)(((U%M15)*512)%M15);} inline u64 tm18(u128 U){return (u64)(((U%M18)*512)%M18);} inline u64 tm21(u128 U){return (u64)(((U%M21)*512)%M21);}
int main(int argc,char**argv){if(argc!=3){std::cerr<<"usage: cert START_P4 END_P4\n";return 2;}int S=std::stoi(argv[1]),E=std::stoi(argv[2]);init_terms();auto B15=loadbits("k9_15.bits"),B18=loadbits("k9_18.bits");auto [m21,T21]=loadvec("k9_21.vec");auto[lo,hi]=interval();std::vector<u128>left;left.reserve(6000000);
for(int p0=0;p0<S;p0++)for(int p1=p0+1;p1<S;p1++)for(int p2=p1+1;p2<S;p2++)for(int p3=p2+1;p3<S;p3++)left.push_back(A[0][p0]+A[1][p1]+A[2][p2]+A[3][p3]);std::sort(left.begin(),left.end());
u64 numeric=0,c15=0,c18=0,c21=0;std::vector<u128>surv;u128 maxL=4*M-4;
for(int p4=S;p4<=E;p4++){
 if(p4>S){int p3=p4-1;std::vector<u128>add;add.reserve((u64)p3*(p3-1)*(p3-2)/6);for(int p0=0;p0<p3;p0++)for(int p1=p0+1;p1<p3;p1++)for(int p2=p1+1;p2<p3;p2++)add.push_back(A[0][p0]+A[1][p1]+A[2][p2]+A[3][p3]);std::sort(add.begin(),add.end());std::vector<u128>mer;mer.reserve(left.size()+add.size());std::merge(left.begin(),left.end(),add.begin(),add.end(),std::back_inserter(mer));left.swap(mer);}
 for(int p5=p4+1;p5<W;p5++)for(int p6=p5+1;p6<W;p6++)for(int p7=p6+1;p7<W;p7++){u128 rs=A[4][p4]+A[5][p5]+A[6][p6]+A[7][p7];for(int q=1;q<=8;q++){i128 qlo=(i128)((u128)q*M-hi)-(i128)rs,qhi=(i128)((u128)q*M-lo)-(i128)rs;if(qhi<0||qlo>(i128)maxL)continue;u128 a=qlo<0?0:(u128)qlo,b=qhi>(i128)maxL?maxL:(u128)qhi;if(a>b)continue;auto it=std::lower_bound(left.begin(),left.end(),a),en=std::upper_bound(left.begin(),left.end(),b);for(;it!=en;++it){u128 s=*it+rs,r=s&MASK,U=r?M-r:0;if(U<lo||U>hi)continue;numeric++;if(!B15.has(tm15(U)))continue;c15++;if(!B18.has(tm18(U)))continue;c18++;if(!std::binary_search(T21.begin(),T21.end(),tm21(U)))continue;c21++;surv.push_back(U);}}}
}
std::cout<<"BATCH "<<S<<" "<<E<<" numeric="<<numeric<<" K15="<<c15<<" K18="<<c18<<" K21="<<c21;std::vector<u128>cur=std::move(surv);for(int d:{24,27,30,33,36,39}){std::vector<u128>nx;for(u128 U:cur)if(formation(U<<K,d))nx.push_back(U);std::cout<<" K"<<d<<"="<<nx.size();cur.swap(nx);if(cur.empty())break;}std::cout<<"\n";
}
