#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using u64=uint64_t; static constexpr int K=36; static constexpr u64 TAG=1ULL<<63;
struct Tail{array<uint8_t,12> p{};u64 tailC=0;bool valid=false;uint8_t first=0;};
struct Slot{u64 key=0,mx=0,cm=0;}; struct Stat{u64 n=0,classes=0,cand=0,candclasses=0,surv=0,dom=0,minc=UINT64_MAX,maxc=0;};
static int Q,BT,E,B; static u64 MOD,PB,p2v[40],p3v[40],choosev[40][40]; static int qminv[40],boundv[40];
static vector<vector<Tail>> buckets; static vector<vector<u64>> early;
static inline u64 mix(u64 x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
void early_rec(int f,int pos,int left,int rank,u64 C,bool valid,vector<u64>&out){if(left==0){out.push_back(C|(valid?TAG:0));return;}for(int p=pos;p<=f-left;p++)early_rec(f,p+1,left-1,rank+1,3*C+p2v[p],valid&&(p<=boundv[rank]),out);}
void tails_rec(int pos,int left,int idx,array<uint8_t,12>&a){if(left==0){int f=a[0];if(f<E)return;u64 tc=0;bool v=true;for(int i=0;i<BT;i++){tc=3*tc+p2v[a[i]];v=v&&(a[i]<=boundv[E+i+1]);}Tail t;t.p=a;t.tailC=tc;t.valid=v;t.first=f;buckets[(int)(tc%(u64)B)].push_back(t);return;}for(int p=pos;p<=K-left;p++){a[idx]=p;tails_rec(p+1,left-1,idx+1,a);}}
Stat one(int b,u64 expected){
 size_t cap=16; long double need=(long double)expected*1.15L+16;while((long double)cap<need)cap<<=1;vector<Slot> h(cap);size_t mask=cap-1;Stat S;S.n=expected;
 for(auto const&t:buckets[b]){auto const&es=early[t.first];for(u64 z:es){u64 ce=z&~TAG;u64 X=PB*ce+t.tailC;bool cand=(z&TAG)&&t.valid;if(cand)++S.cand;u64 r=X%MOD,k=r+1;size_t i=(size_t)mix(r)&mask;while(h[i].key&&h[i].key!=k)i=(i+1)&mask;if(!h[i].key){h[i].key=k;h[i].mx=X;++S.classes;}else if(X>h[i].mx)h[i].mx=X;if(cand&&X>h[i].cm)h[i].cm=X;}}
 for(auto const&s:h)if(s.key&&s.cm){++S.candclasses;if(s.cm==s.mx)++S.surv;else{++S.dom;u64 d=(s.mx-s.cm)/MOD;assert(d);S.minc=min(S.minc,d);S.maxc=max(S.maxc,d);}}
 return S;
}
int main(int argc,char**argv){if(argc<3)return 2;Q=stoi(argv[1]);BT=stoi(argv[2]);int threads=argc>3?stoi(argv[3]):5;if(BT<1||BT>12||Q<=BT||Q>30)return 3;E=Q-BT;B=1;for(int i=0;i<BT;i++)B*=3;
 p2v[0]=p3v[0]=1;for(int i=1;i<40;i++){p2v[i]=p2v[i-1]*2ULL;p3v[i]=p3v[i-1]*3ULL;}MOD=p3v[Q];PB=p3v[BT];for(int k=1;k<=K;k++){int z=0;while(p3v[z]<=p2v[k])++z;qminv[k]=z;}for(int j=1;j<40;j++){boundv[j]=K;for(int k=1;k<=K;k++)if(qminv[k]>=j){boundv[j]=k-1;break;}}
 memset(choosev,0,sizeof(choosev));for(int n=0;n<40;n++){choosev[n][0]=choosev[n][n]=1;for(int k=1;k<n;k++)choosev[n][k]=choosev[n-1][k-1]+choosev[n-1][k];}
 early.resize(K);u64 earlyN=0;for(int f=E;f<=K-BT;f++){auto&o=early[f];o.reserve((size_t)choosev[f][E]);early_rec(f,0,E,1,0,true,o);assert(o.size()==choosev[f][E]);earlyN+=o.size();}
 buckets.assign(B,{});array<uint8_t,12>a{};tails_rec(E,BT,0,a);u64 tailN=0,expected=0,maxbucket=0;vector<u64>bn(B);for(int b=0;b<B;b++){tailN+=buckets[b].size();for(auto&t:buckets[b])bn[b]+=early[t.first].size();expected+=bn[b];maxbucket=max(maxbucket,bn[b]);}
 cerr<<"Q "<<Q<<" BT "<<BT<<" E "<<E<<" B "<<B<<" early_states "<<earlyN<<" tails "<<tailN<<" expected "<<expected<<" maxbucket "<<maxbucket<<" nonempty "<<count_if(bn.begin(),bn.end(),[](u64 x){return x>0;})<<"\n";
 vector<int>ids;for(int b=0;b<B;b++)if(bn[b])ids.push_back(b);sort(ids.begin(),ids.end(),[&](int a,int b){return bn[a]>bn[b];});vector<Stat>st(B);omp_set_num_threads(threads);
 #pragma omp parallel for schedule(dynamic,1)
 for(long long ii=0;ii<(long long)ids.size();ii++){int b=ids[(size_t)ii];st[b]=one(b,bn[b]);}
 Stat T;for(int b:ids){auto&s=st[b];T.n+=s.n;T.classes+=s.classes;T.cand+=s.cand;T.candclasses+=s.candclasses;T.surv+=s.surv;T.dom+=s.dom;if(s.minc!=UINT64_MAX)T.minc=min(T.minc,s.minc);T.maxc=max(T.maxc,s.maxc);}
 cout<<"Q "<<Q<<" BT "<<BT<<" arbitrary_words "<<T.n<<" classes "<<T.classes<<" coefficient_words "<<T.cand<<" candidate_classes "<<T.candclasses<<" candidate_collision_excess "<<(T.cand-T.candclasses)<<" survivors "<<T.surv<<" dominated_classes "<<T.dom<<" mincredit "<<(T.minc==UINT64_MAX?0:T.minc)<<" maxcredit "<<T.maxc<<"\n";
}
