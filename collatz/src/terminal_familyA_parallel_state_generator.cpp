#include <algorithm>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <thread>
#include <vector>
using u64=std::uint64_t; using u32=std::uint32_t; using u128=unsigned __int128; using i128=__int128;
static inline u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static long long egcd(long long a,long long b,long long&x,long long&y){if(!b){x=1;y=0;return a;}long long x1,y1;auto g=egcd(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
static u64 invmod(u64 a,u64 m){long long x,y;if(egcd((long long)a,(long long)m,x,y)!=1)std::exit(2);x%=(long long)m;if(x<0)x+=m;return (u64)x;}
struct DL30{static constexpr u64 M16=43046721ULL,O16=28697814ULL,H=4782969ULL,M30=205891132094649ULL,O30=137260754729766ULL;std::vector<std::int32_t>log16;std::vector<u64>invpow;u64 cinv;DL30():log16(M16,-1),invpow(O16){u64 v=1;for(u64 e=0;e<O16;e++){log16[v]=(int)e;v=2*v%M16;}u64 inv2=(M30+1)/2;v=1;for(u64 e=0;e<O16;e++){invpow[e]=v;v=mulmod(v,inv2,M30);}u64 B=powmod(2,O16,M30);cinv=invmod(((B-1)/M16)%H,H);}inline u64 log(u64 u)const{int e0=log16[u%M16];if(e0<0)std::exit(4);u64 R=mulmod(u,invpow[e0],M30);if(R%M16!=1)std::exit(5);return (u64)e0+O16*mulmod((R-1)/M16,cinv,H);}};
struct Target{u64 l,s; bool operator<(Target const&o)const{return l<o.l||(l==o.l&&s<o.s);}};
struct Stats{unsigned long long rh=0,raw=0,budget=0;u64 maxper=0;};
int main(int argc,char**argv){if(argc<7){std::cerr<<"K R18 carry ZCAP threads outfile\n";return 1;}u64 K=std::stoull(argv[1]),R18=std::stoull(argv[2]),carry=std::stoull(argv[3]),ZCAP=std::stoull(argv[4]);int NT=std::stoi(argv[5]);std::string out=argv[6];
DL30 dl; const u64 G=120123938613220ULL,invG=invmod(G,DL30::M30);std::vector<u64>cv{0};u64 p=1;for(int i=0;i<21;i++){size_t n=cv.size();for(size_t j=0;j<n;j++)cv.push_back(cv[j]+p);p*=3;}
std::vector<Target> targets;targets.reserve(1<<21);for(u64 c:cv){for(u64 s0=0;s0<2;s0++){u64 S=s0+3*c;u64 T=(5+mulmod(invG,(4*S+K)%DL30::M30,DL30::M30))%DL30::M30;if(T%3)targets.push_back({dl.log(T),S});}}std::sort(targets.begin(),targets.end());std::cerr<<"target size="<<targets.size()<<"\n";
const u64 M18=387420489ULL,DNEAR=29785654ULL,CQ18=23724081064404ULL;std::vector<u64>low{0};p=1;for(int i=0;i<18;i++){size_t n=low.size();for(size_t j=0;j<n;j++)low.push_back(low[j]+p);p*=3;}
std::vector<u64>dvals;for(u64 s:low){u64 xr=(4*s+3)%M18,d=(R18+M18-xr)%M18,c=(4*s+3+d-R18)/M18;if(d<=DNEAR&&c==carry)dvals.push_back(d);}std::sort(dvals.begin(),dvals.end());std::cerr<<"targets="<<targets.size()<<" dvals="<<dvals.size()<<" dmin="<<dvals.front()<<"\n";
const u128 DEN=(u128)117*1000000000000000000ULL;const u64 U=33068504827ULL,LAM=898654ULL;const u128 DLAM=117,DCOST=1000000000000ULL;
std::vector<std::vector<u32>> local(NT,std::vector<u32>(targets.size(),0));std::vector<Stats> sts(NT);std::vector<std::thread> th;
for(int tid=0;tid<NT;tid++)th.emplace_back([&,tid]{u64 lo=(u128)ZCAP*tid/NT,hi=(u128)ZCAP*(tid+1)/NT;u64 inv2=(DL30::M30+1)/2;u64 inv2r=powmod(inv2,lo,DL30::M30);auto &md=local[tid];auto &st=sts[tid];auto consume=[&](u64 L,u64 H,u64 a,u64 r)->u64{if(L>H)return 0;auto it=std::lower_bound(targets.begin(),targets.end(),Target{L,0});auto ed=std::upper_bound(targets.begin(),targets.end(),Target{H,std::numeric_limits<u64>::max()});u64 n=0;for(;it!=ed;++it){u64 w=(a+DL30::O30-it->l)%DL30::O30;if(!(w>=1&&w<=ZCAP-r))continue;++n;u64 z=w+r;u128 Y=(u128)4*CQ18+(u128)4*it->s+carry;u128 y=(u128)R18+(u128)M18*Y;i128 costnum=(i128)240449*((i128)117+(i128)200*((i128)z-3))-(i128)92*39*1000000;u128 pc=costnum>0?(u128)costnum:0;u128 base=(u128)U*DEN,lt=(u128)LAM*y*DLAM,ct=pc*DCOST;if(base<lt||base-lt<ct)continue;u64 dcap=(u64)((base-lt-ct)/DEN);if(dcap>DNEAR)dcap=DNEAR;if(dcap<dvals.front())continue;st.budget++;size_t idx=(size_t)(it-targets.begin());if(dcap>md[idx])md[idx]=(u32)dcap;}return n;};
for(u64 r=lo;r<hi;r++){u64 A=(2+mulmod(3,inv2r,DL30::M30))%DL30::M30,a=dl.log(A),W=ZCAP-r,n=0;if(a>=W)n+=consume(a-W,a-1,a,r);else{if(a)n+=consume(0,a-1,a,r);n+=consume(DL30::O30-(W-a),DL30::O30-1,a,r);}if(n){st.rh++;st.raw+=n;st.maxper=std::max(st.maxper,n);}if(inv2r&1)inv2r=(inv2r+DL30::M30)>>1;else inv2r>>=1;}});
for(auto&t:th)t.join();std::vector<u32> md(targets.size(),0);Stats S;for(int t=0;t<NT;t++){S.rh+=sts[t].rh;S.raw+=sts[t].raw;S.budget+=sts[t].budget;S.maxper=std::max(S.maxper,sts[t].maxper);for(size_t i=0;i<md.size();i++)if(local[t][i]>md[i])md[i]=local[t][i];local[t].clear();local[t].shrink_to_fit();}
unsigned long long states=0,starts=0;unsigned long long pcnt[16]={0},pstarts[16]={0};std::ofstream f(out);for(size_t i=0;i<md.size();i++)if(md[i]){states++;u64 cnt=std::upper_bound(dvals.begin(),dvals.end(),md[i])-dvals.begin();starts+=cnt;u64 Sval=targets[i].s;u64 high4=Sval/387420489ULL;u64 x=high4,code=0,mul=1;for(int j=0;j<4;j++){code+=(x%3)*mul;mul*=2;x/=3;}pcnt[code]++;pstarts[code]+=cnt;f<<targets[i].s<<" "<<md[i]<<"\n";}
std::cout<<"r_hits="<<S.rh<<" raw="<<S.raw<<" maxper="<<S.maxper<<" budget="<<S.budget<<" states="<<states<<" starts="<<starts<<"\n";for(int c=0;c<16;c++)if(pcnt[c])std::cout<<c<<" "<<pcnt[c]<<" "<<pstarts[c]<<"\n";
}
