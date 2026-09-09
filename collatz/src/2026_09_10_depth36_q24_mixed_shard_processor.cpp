#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using u64=uint64_t; static constexpr u64 TAG=1ULL<<63; static u64 MOD;
struct Item{u64 r,ctag;}; struct Stat{u64 n=0,classes=0,cand=0,surv=0,cand_collision_excess=0,dom=0,mincredit=UINT64_MAX,maxcredit=0;};
string fn(string const&d,int P,int s,int b){return d+"/m46_q24_p"+to_string(P)+"_s"+to_string(s)+"_b"+to_string(b)+".bin";}
Stat one(string const&d,int b){
 vector<Item> v; vector<pair<int,int>> shards={{2,0},{2,1},{2,2},{4,3},{4,7},{4,11},{4,15}};
 for(auto [P,s]:shards){string fna=fn(d,P,s,b);ifstream f(fna,ios::binary|ios::ate);if(!f)continue;auto sz=f.tellg();size_t n=(size_t)sz/8;f.seekg(0);vector<u64>x(n);f.read((char*)x.data(),sz);f.close();v.reserve(v.size()+n);for(u64 z:x){u64 c=z&~TAG;v.push_back({c%MOD,z});}std::remove(fna.c_str());}
 sort(v.begin(),v.end(),[](auto const&a,auto const&b){return a.r<b.r||(a.r==b.r&&(a.ctag&~TAG)<(b.ctag&~TAG));});
 Stat S;S.n=v.size();for(size_t i=0;i<v.size();){size_t j=i+1;while(j<v.size()&&v[j].r==v[i].r)++j;++S.classes;u64 mx=0,cm=0,cn=0;for(size_t t=i;t<j;t++){u64 c=v[t].ctag&~TAG;mx=max(mx,c);if(v[t].ctag&TAG){++cn;cm=max(cm,c);}}S.cand+=cn;if(cn>1)S.cand_collision_excess+=cn-1;if(cn){if(cm==mx)++S.surv;else{++S.dom;u64 cr=(mx-cm)/MOD;assert(cr);S.mincredit=min(S.mincredit,cr);S.maxcredit=max(S.maxcredit,cr);}}i=j;}return S;
}
int main(int argc,char**argv){if(argc!=5)return 2;string d=argv[1];int b0=stoi(argv[2]),b1=stoi(argv[3]),threads=stoi(argv[4]);omp_set_num_threads(threads);MOD=1;for(int i=0;i<24;i++)MOD*=3ULL;vector<Stat> st(b1-b0);
#pragma omp parallel for schedule(dynamic,1)
for(int b=b0;b<b1;b++)st[b-b0]=one(d,b);
for(int b=b0;b<b1;b++){auto&s=st[b-b0];cout<<b<<'\t'<<s.n<<'\t'<<s.classes<<'\t'<<s.cand<<'\t'<<s.surv<<'\t'<<s.cand_collision_excess<<'\t'<<s.dom<<'\t'<<(s.mincredit==UINT64_MAX?0:s.mincredit)<<'\t'<<s.maxcredit<<'\n';}
}
