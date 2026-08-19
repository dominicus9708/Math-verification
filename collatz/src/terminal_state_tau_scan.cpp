#include <algorithm>
#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <vector>
using u64=std::uint64_t; using u128=unsigned __int128; using boost::multiprecision::cpp_int;
static std::string u128str(u128 x){if(!x)return"0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}std::reverse(s.begin(),s.end());return s;}
struct B16{u64 A,R;uint16_t mask;uint8_t q;std::array<uint8_t,17> pref;};
struct State{u64 S;uint32_t dcap;}; struct Low{u64 d,s;};
static u128 parse128(const std::string&s){u128 x=0;for(char c:s)x=x*10+(c-'0');return x;}
int main(int argc,char**argv){if(argc<8){std::cerr<<"statefile R18 carry code threads maxk C_START\n";return 1;}std::string sf=argv[1];u64 R18=std::stoull(argv[2]),carry=std::stoull(argv[3]);int want=std::stoi(argv[4]),NT=std::stoi(argv[5]),MAXK=std::stoi(argv[6]);u128 CSTART=parse128(argv[7]);
const u64 M18=387420489ULL,DNEAR=29785654ULL;
std::vector<int>a(MAXK+17);cpp_int p2=1,p3=1;int qq=0;for(int k=1;k<(int)a.size();k++){p2*=2;while(p3<p2){p3*=3;qq++;}a[k]=qq;}
std::vector<B16> tab(65536);for(u64 r=0;r<65536;r++){B16 b{};b.A=1;b.R=0;b.pref[0]=0;u64 n=r;for(int j=0;j<16;j++){bool odd=n&1;b.mask|=(uint16_t(odd)<<j);if(odd){b.A*=3;b.R=3*b.R+(1ULL<<j);b.q++;n=(3*n+1)/2;}else n/=2;b.pref[j+1]=b.q;}tab[r]=b;}
int NB=(MAXK+15)/16;std::vector<uint16_t> threshold((size_t)NB*65536);for(int bi=0;bi<NB;bi++){int k0=16*bi;for(int r=0;r<65536;r++){int th=-10000;for(int j=1;j<=16 && k0+j<(int)a.size();j++)th=std::max(th,a[k0+j]-(int)tab[r].pref[j]);threshold[(size_t)bi*65536+r]=(uint16_t)std::max(0,th);}}
std::vector<Low> lows;std::vector<u64> vals{0};u64 p=1;for(int i=0;i<18;i++){size_t n=vals.size();for(size_t j=0;j<n;j++)vals.push_back(vals[j]+p);p*=3;}for(u64 s:vals){u64 xr=(4*s+3)%M18,d=(R18+M18-xr)%M18,c=(4*s+3+d-R18)/M18;if(d<=DNEAR&&c==carry)lows.push_back({d,s});}std::sort(lows.begin(),lows.end(),[](auto&a,auto&b){return a.d<b.d;});
std::vector<State> states;{std::ifstream f(sf);u64 S;uint32_t dc;while(f>>S>>dc){u64 h=S/M18,x=h,code=0,m=1;for(int j=0;j<4;j++){code+=(x%3)*m;m*=2;x/=3;}if((int)code==want)states.push_back({S,dc});}}
std::cerr<<"states="<<states.size()<<" lows="<<lows.size()<<" code="<<want<<"\n";
struct Res{unsigned long long count=0,surv=0,overflow=0;int maxt=0;u128 maxx=0;};std::vector<Res> res(NT);std::vector<std::thread> ths;
for(int tid=0;tid<NT;tid++)ths.emplace_back([&,tid]{size_t lo=states.size()*tid/NT,hi=states.size()*(tid+1)/NT;auto &rr=res[tid];for(size_t si=lo;si<hi;si++){auto st=states[si];auto ed=std::upper_bound(lows.begin(),lows.end(),st.dcap,[](u64 v,const Low&x){return v<x.d;});for(auto it=lows.begin();it!=ed;++it){u128 x=4*(CSTART+(u128)M18*st.S+it->s)+3;u128 x0=x;rr.count++;int k=0,q=0;bool done=false,ov=false;while(k<MAXK){u64 r=(u64)x&65535ULL;auto &b=tab[r];int bi=k/16;if(q < threshold[(size_t)bi*65536+r]){for(int j=1;j<=16 && k+j<=MAXK;j++){if(q+(int)b.pref[j]<a[k+j]){int tc=k+j;if(tc>rr.maxt){rr.maxt=tc;rr.maxx=x0;}done=true;break;}}if(done)break;}u128 maxv=~(u128)0;if(x>(maxv-b.R)/b.A){ov=true;break;}x=(b.A*x+b.R)>>16;q+=b.q;k+=16;}if(ov){rr.overflow++;continue;}if(!done)rr.surv++;}}});
for(auto&t:ths)t.join();Res R;for(auto&r:res){R.count+=r.count;R.surv+=r.surv;R.overflow+=r.overflow;if(r.maxt>R.maxt){R.maxt=r.maxt;R.maxx=r.maxx;}}
std::cout<<"count="<<R.count<<" max_tau="<<R.maxt<<" max_x="<<u128str(R.maxx)<<" survivors="<<R.surv<<" overflow="<<R.overflow<<"\n";
}
