#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <limits>
#include <omp.h>
using u64=uint64_t; using u32=uint32_t; using u128=__uint128_t;
static constexpr int H=24, ZBITS=22, ZM=1<<22, ZMASK=ZM-1, BMAX=20, KMAX=36, LOWZBITS=19, LOWZMASK=(1u<<19)-1;
struct State{u64 R; uint8_t q;};
struct Fwd{u64 R; uint8_t q; bool odd;};
struct E{u64 C=0; uint8_t q=0,K=0; bool valid=false;};
u64 p3[50];
inline bool coeffok(int k,int q){return p3[q]>=(1ULL<<k);} 
inline u64 ckey(int q,u64 R){return (u64(q)<<56)|(R%p3[q]);}
void scanall(int pos,int k,int q,u64 R,int qmin,std::unordered_map<u64,u64>& cm){
 if(q+(k-pos)<qmin)return; if(pos==k){auto it=cm.find(ckey(q,R)); if(it!=cm.end()&&R>it->second)it->second=R; return;}
 scanall(pos+1,k,q,R,qmin,cm); scanall(pos+1,k,q+1,3*R+(1ULL<<pos),qmin,cm);
}
u64 invodd(u64 a){u64 x=a; for(int i=0;i<6;++i)x*=2-a*x; return x;}
std::vector<u32> rootH24(){
 const u64 exp[25]={0,1,1,2,3,4,7,11,16,31,52,103,182,297,593,1049,1720,3439,6104,12194,22244,38019,75969,137657,234156};
 std::vector<State> coef{{0,0}}, nest{{0,0}};
 for(int k=1;k<=H;++k){
  std::vector<State> nc; nc.reserve(coef.size()*2);
  for(auto s:coef){if(coeffok(k,s.q))nc.push_back(s);int q=s.q+1;u64 R=3*s.R+(1ULL<<(k-1));if(coeffok(k,q))nc.push_back({R,(uint8_t)q});} coef.swap(nc);
  std::unordered_map<u64,u64> cm; cm.reserve(coef.size()*2); for(auto s:coef){auto [it,ins]=cm.emplace(ckey(s.q,s.R),s.R); if(!ins&&s.R>it->second)it->second=s.R;}
  int qmin=0;while(!coeffok(k,qmin))++qmin;scanall(0,k,0,0,qmin,cm);
  std::vector<State> nn;nn.reserve(nest.size()*2);for(auto s:nest){
   if(coeffok(k,s.q)){auto it=cm.find(ckey(s.q,s.R));if(it!=cm.end()&&it->second==s.R)nn.push_back(s);} int q=s.q+1;u64 R=3*s.R+(1ULL<<(k-1));if(coeffok(k,q)){auto it=cm.find(ckey(q,R));if(it!=cm.end()&&it->second==R)nn.push_back({R,(uint8_t)q});}
  } nest.swap(nn); if(nest.size()!=exp[k]){std::cerr<<"root regression fail "<<k<<" "<<nest.size()<<"\n";exit(2);} }
 std::vector<u32> z;z.reserve(nest.size());std::vector<uint8_t> seen(ZM);for(auto s:nest){u32 N=(u32)(((0ULL-s.R)*invodd(p3[s.q]))&((1ULL<<H)-1));if((N&3)!=3)exit(3);u32 a=(N-3)>>2;if(seen[a])exit(4);seen[a]=1;z.push_back(a);}std::sort(z.begin(),z.end());return z;
}
Fwd forward(u32 r,int B){u64 n=r,R=0;int q=0;for(int k=0;k<B;++k){if(n&1){R=3*R+(1ULL<<k);++q;n=(3*n+1)>>1;}else n>>=1;}return{R,(uint8_t)q,bool(n&1)};}
bool ratio_better(const E&a,const E&b){if(!a.valid)return false;if(!b.valid)return true;u64 L=p3[a.q]*(1ULL<<b.K), R=p3[b.q]*(1ULL<<a.K);if(L!=R)return L>R;return a.C>b.C;}
std::vector<std::vector<E>> buildReverseDP(int Qmax){
 std::vector<std::vector<E>> keep(Qmax+1); int prevM=1; std::vector<E> prev(prevM*(KMAX+1));
 for(int d=1;d<=Qmax;++d){int M=prevM*3;std::vector<E> cur((size_t)M*(KMAX+1));
  for(int z=0;z<M;++z){int r3=z%3;if(r3==0)continue;int a0=(r3==1)?2:1;
   for(int bud=1;bud<=KMAX;++bud){E best;
    for(int a=a0;a<=bud;a+=2){u64 num=(1ULL<<a)*(u64)z-1;if(num%3)exit(5);int zp=prevM>1?int((num/3)%prevM):0;E cand;E suf=prev[(size_t)zp*(KMAX+1)+(bud-a)];bool useSuf=false;if(suf.valid){u64 sr=p3[suf.q], sp=1ULL<<suf.K;if(sr>sp)useSuf=true;}
     cand.valid=true;if(useSuf){cand.q=suf.q+1;cand.K=suf.K+a;cand.C=(1ULL<<suf.K)+3*suf.C;}else{cand.q=1;cand.K=a;cand.C=1;}
     if(cand.K>bud)exit(6); if(ratio_better(cand,best))best=cand;
    }
    cur[(size_t)z*(KMAX+1)+bud]=best;
   }
  }
  keep[d]=cur; prev.swap(cur); prevM=M; std::cerr<<"reverseDP depth "<<d<<" M "<<M<<"\n";
 }
 return keep;
}
long long egcd(long long a,long long b,long long&x,long long&y){if(!b){x=1;y=0;return a;}long long x1,y1;long long g=egcd(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
int invmod(int a,int m){long long x,y;egcd(a,m,x,y);x%=m;if(x<0)x+=m;return(int)x;}
struct Calc{u64 total=0;std::vector<u64> bymask;};
Calc calcQ(int Q,const std::vector<E>& rev,const std::vector<u32>& rootz,const std::vector<std::array<Fwd,BMAX+1>>& paths){
 int MOD=(int)p3[Q]; std::vector<int> inv2(BMAX+1);int tw=1;for(int B=1;B<=BMAX;++B){tw=(long long)tw*2%MOD;inv2[B]=invmod(tw,MOD);} 
 std::vector<u64> dp(ZM),nd(ZM);dp[0]=1;u32 w=1;for(int i=0;i<44;++i){if(i==0)w=1;else w=(u32)((u64)w*3&ZMASK);if(i<Q)continue;for(u32 r=0;r<ZM;++r)nd[r]=dp[r]+dp[(r+ZM-w)&ZMASK];dp.swap(nd);}u64 s=0;for(auto v:dp)s+=v;if(s!=(1ULL<<(44-Q))){std::cerr<<"dp sum fail\n";exit(7);} 
 int NM=1<<Q;std::vector<u32> low(NM);std::vector<int> n3(NM);for(int mask=0;mask<NM;++mask){u64 sh=0,pw=1;long long t=3%MOD;for(int i=0;i<Q;++i){if(mask&(1<<i)){sh+=pw;t=(t+4*(pw%MOD))%MOD;}pw*=3;}low[mask]=(u32)(sh&ZMASK);n3[mask]=(int)t;}
 u32 fixed=1;for(int i=0;i<44;++i)fixed=(u32)((u64)fixed*3&ZMASK);
 Calc out;out.bymask.assign(NM,0);
 #pragma omp parallel for schedule(dynamic,1)
 for(int lm=0;lm<NM;++lm){u32 base=(fixed+low[lm])&ZMASK;int nm=n3[lm];u64 cnt=0;
  for(size_t j=0;j<rootz.size();++j){u32 hr=(rootz[j]+ZM-base)&ZMASK;u64 mult=dp[hr];if(!mult)continue;bool alive=true;
   for(int B=2;B<=BMAX;++B){const Fwd& f=paths[j][B];if(!f.odd)continue;int z3=(int)(((p3[f.q]%MOD)*(u64)nm+(f.R%MOD))%MOD);z3=(long long)z3*inv2[B]%MOD;const E&e=rev[(size_t)z3*(KMAX+1)+KMAX];if(!e.valid)continue;u64 L=p3[e.q]*(1ULL<<B), R=p3[f.q]*(1ULL<<e.K);if(L>R||(L==R&&e.C>f.R)){alive=false;break;}}
   if(alive)cnt+=mult;
  }
  out.bymask[lm]=cnt;
 }
 for(u64 v:out.bymask)out.total+=v;return out;
}
void trans(const Calc&a,const Calc&b,int Q){long double mi=1e100L,ma=-1;int mim=-1,mam=-1;u64 minnum=0,minden=1,maxnum=0,maxden=1;int equal=0,expand=0,zero=0;for(int p=0;p<(1<<Q);++p){u64 den=a.bymask[p],num=b.bymask[p]+b.bymask[p+(1<<Q)];if(!den){if(num)++expand;continue;}long double r=(long double)num/den;if(r<mi){mi=r;mim=p;minnum=num;minden=den;}if(r>ma){ma=r;mam=p;maxnum=num;maxden=den;}if(num==den)++equal;if(num>den)++expand;if(!num)++zero;}std::cout<<std::setprecision(18)<<"Q"<<Q<<"->Q"<<Q+1<<" global "<<(long double)b.total/a.total<<" min "<<mi<<" p "<<mim<<" "<<minnum<<"/"<<minden<<" max "<<ma<<" p "<<mam<<" "<<maxnum<<"/"<<maxden<<" equal "<<equal<<" expand "<<expand<<" zero "<<zero<<"\n";}

int main(){p3[0]=1;for(int i=1;i<50;++i)p3[i]=p3[i-1]*3ULL;omp_set_num_threads(5);auto rz=rootH24();std::cerr<<"rootz "<<rz.size()<<"\n";std::vector<std::array<Fwd,BMAX+1>> paths(rz.size());for(size_t j=0;j<rz.size();++j){u32 r21=(4u*(rz[j]&LOWZMASK)+3u)&((1u<<21)-1);for(int B=2;B<=BMAX;++B)paths[j][B]=forward(r21&((1u<<(B+1))-1),B);}auto all=buildReverseDP(10);Calc q7=calcQ(7,all[7],rz,paths);std::cout<<"Q7 "<<q7.total<<"\n";Calc q8=calcQ(8,all[8],rz,paths);std::cout<<"Q8 "<<q8.total<<"\n";Calc q9=calcQ(9,all[9],rz,paths);std::cout<<"Q9 "<<q9.total<<"\n";Calc q10=calcQ(10,all[10],rz,paths);std::cout<<"Q10 "<<q10.total<<"\n"; if(q7.total!=784787338151ULL||q8.total!=776902007561ULL||q9.total!=758110858098ULL||q10.total!=752548965765ULL){std::cerr<<"total regression failure\n";return 11;}trans(q7,q8,7);trans(q8,q9,8);trans(q9,q10,9);std::cout<<std::setprecision(18)<<"Q10_fraction "<<(long double)q10.total/(long double)(1ULL<<44)<<"\n";return 0;}
