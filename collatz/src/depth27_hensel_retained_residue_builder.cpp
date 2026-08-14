#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;using u32=uint32_t;
struct W{u64 R;int q;u32 mask;};
struct Key{uint8_t s;u64 r;bool operator==(Key const&o)const{return s==o.s&&r==o.r;}};
struct KH{size_t operator()(Key const&k)const noexcept{u64 x=k.r^(u64(k.s)<<56);x^=x>>33;x*=0xff51afd7ed558ccdULL;x^=x>>33;return x;}};
vector<u64>P3;
void gs(int pos,int L,int q,u64 R,u32 mask,map<int,vector<W>>&g){if(pos==L){g[q].push_back({R,q,mask});return;}if(P3[q]>=(1ULL<<(pos+1)))gs(pos+1,L,q,R,mask,g);u64 R1=3*R+(1ULL<<pos);if(P3[q+1]>=(1ULL<<(pos+1)))gs(pos+1,L,q+1,R1,mask|(1U<<pos),g);}
u64 corr(const vector<int>&p){u64 R=0;for(int x:p)R=3*R+(1ULL<<x);return R;}
void enum_later(int st,int need,int L,vector<int>&p,int s,unordered_map<Key,u64,KH>&mx){if(!need){u64 R=corr(p);auto it=mx.find(Key{uint8_t(s),R%P3[s+1]});if(it!=mx.end()&&R>it->second)it->second=R;return;}for(int x=st;x<=L-need;x++){p.push_back(x);enum_later(x+1,need-1,L,p,s,mx);p.pop_back();}}
void enum_q(int st,int need,int L,vector<int>&p,int q,unordered_map<u64,u64>&imm){if(!need){u64 R=corr(p),r=R%P3[q];auto it=imm.find(r);if(it!=imm.end()&&R>it->second)it->second=R;return;}for(int x=st;x<=L-need;x++){p.push_back(x);enum_q(x+1,need-1,L,p,q,imm);p.pop_back();}}
u64 invodd(u64 a){u64 x=1;for(int i=0;i<6;i++)x*=2-a*x;return x;}
int main(int argc,char**argv){const int L=27;const u64 MOD=1ULL<<L,MASK=MOD-1;const string out=argc>1?argv[1]:"allow27.bin";P3.assign(L+2,1);for(int i=1;i<(int)P3.size();i++)P3[i]=3*P3[i-1];map<int,vector<W>>groups;gs(2,L,2,5,3,groups);vector<u32>residues;residues.reserve(1100000);
for(auto&[q,S]:groups){unordered_map<Key,u64,KH>partial;partial.reserve(S.size()*8);unordered_map<u64,u64>imm;imm.reserve(S.size()*2);for(auto&w:S){imm.emplace(w.R%P3[q],0);for(int s=1;s<q;s++){u64 base=w.R%P3[s],digit=(w.R/P3[s])%3;for(u64 a=0;a<3;a++)if(a!=digit)partial.emplace(Key{uint8_t(s),base+a*P3[s]},0);}}
for(int s=1;s<q;s++){int d=q-s,pmin=d-1;while(pmin<L&&(1ULL<<(pmin+1))<=P3[d])pmin++;for(int pd=pmin;pd<=L-1-s;pd++){vector<int>p;int first=pd-d+1;if(first<0)continue;for(int x=first;x<=pd;x++)p.push_back(x);enum_later(pd+1,s,L,p,s,partial);}}
vector<int>p;enum_q(0,q,L,p,q,imm);
for(auto&w:S){bool kill=false;for(int s=1;s<q&&!kill;s++){u64 base=w.R%P3[s],digit=(w.R/P3[s])%3;for(u64 a=0;a<3;a++)if(a!=digit){auto it=partial.find(Key{uint8_t(s),base+a*P3[s]});if(it!=partial.end()&&it->second>w.R){kill=true;break;}}}auto it=imm.find(w.R%P3[q]);if(it!=imm.end()&&it->second>w.R)kill=true;if(!kill){u64 inv=invodd(P3[q])&MASK;u64 r=(-inv*w.R)&MASK;residues.push_back(u32(r));}}}
sort(residues.begin(),residues.end());residues.erase(unique(residues.begin(),residues.end()),residues.end());if(residues.size()!=1061510ULL){cerr<<"retained residue mismatch: "<<residues.size()<<"\n";return 2;}vector<u64>bits(MOD/64,0);for(u32 r:residues)bits[r>>6]|=1ULL<<(r&63);ofstream f(out,ios::binary);f.write(reinterpret_cast<const char*>(bits.data()),bits.size()*sizeof(u64));if(!f)return 3;cout<<"retained_residues "<<residues.size()<<" bitset_bytes "<<bits.size()*sizeof(u64)<<" output "<<out<<"\n";return 0;}
