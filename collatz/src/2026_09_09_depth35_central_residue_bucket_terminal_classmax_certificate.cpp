// MATH-045 central-layer exact certificate for depth-35 one-sided root-Hensel.
//
// Fixed depth K=35.  Terminal exact class-max is sufficient for all-prefix
// root-Hensel maximality by the downstream-stable dominance lemma, while the
// coefficient threshold is still checked at every prefix.
//
// The unrestricted competitor language is partitioned by exact residue bucket.
// A Hensel class (q, C mod 3^q) belongs to exactly one bucket, so bucket sums are
// mathematically identical to a monolithic exact class-max computation.
//
// Generation mode:
//   ./m45 gen Q P MASK B DIR
// where P leading parity bits are fixed by MASK (bit=1 means odd), B is the
// number of residue buckets, and output records are 8-byte (C | candidate_tag).
// Use every MASK in [0,2^P) to obtain a disjoint complete shard decomposition.
//
// Processing mode:
//   ./m45 process Q P B B0 B1 DIR
// which merges every prefix shard for buckets [B0,B1), reconstructs r=C mod 3^q,
// sorts exact classes, and prints per-bucket exact counts.
//
// Finite exact scope only.  Collatz remains OPEN.
#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using u64=uint64_t; using u128=__uint128_t;
static constexpr int K=35; static constexpr u64 TAG=1ULL<<63;
static u64 p2v[40],p3v[40],MOD; static int qminv[40],Q,D,P,B;
static vector<ofstream> outs; static u64 total_words,coeff_words;
static vector<u64> bucket_count;
inline int bucket_of(u64 r){return (int)(((u128)r*(u64)B)/MOD);}
void gen_rec(int p,int ev,u64 C,bool valid){
    if(p==K){
        if(ev!=D)return;
        bool cand=valid; if(cand)++coeff_words;
        u64 r=C%MOD; int b=bucket_of(r); u64 x=C|(cand?TAG:0);
        outs[b].write((char*)&x,8); ++bucket_count[b]; ++total_words; return;
    }
    int rem=K-p; if(ev>D||ev+rem<D)return;
    // odd bit: q increases, C -> 3C+2^p
    if(ev+(rem-1)>=D){int qnext=(p-ev)+1;gen_rec(p+1,ev,3*C+p2v[p],valid&&qnext>=qminv[p+1]);}
    // even bit: q unchanged, C unchanged
    if(ev<D){int qnext=p-ev;gen_rec(p+1,ev+1,C,valid&&qnext>=qminv[p+1]);}
}
struct Item{u64 r,ctag;};
struct Stat{u64 n=0,classes=0,cand=0,surv=0,cand_collision_excess=0,dom=0,mincredit=UINT64_MAX,maxcredit=0;};
string file_name(string const&dir,int mask,int b){return dir+"/m45_q"+to_string(Q)+"_p"+to_string(P)+"_s"+to_string(mask)+"_b"+to_string(b)+".bin";}
Stat process_bucket(string const&dir,int b){
    vector<Item> v; int shards=1<<P;
    for(int s=0;s<shards;s++){
        string fn=file_name(dir,s,b); ifstream f(fn,ios::binary|ios::ate); if(!f)continue;
        auto sz=f.tellg(); size_t n=(size_t)sz/8; f.seekg(0); vector<u64>x(n); f.read((char*)x.data(),sz); f.close();
        v.reserve(v.size()+n); for(u64 z:x){u64 c=z&~TAG;v.push_back({c%MOD,z});}
    }
    sort(v.begin(),v.end(),[](Item const&a,Item const&b){return a.r<b.r||(a.r==b.r&&(a.ctag&~TAG)<(b.ctag&~TAG));});
    Stat S; S.n=v.size();
    for(size_t i=0;i<v.size();){
        size_t j=i+1;while(j<v.size()&&v[j].r==v[i].r)++j;++S.classes;
        u64 mx=0,cm=0,cn=0;for(size_t t=i;t<j;t++){u64 c=v[t].ctag&~TAG;mx=max(mx,c);if(v[t].ctag&TAG){++cn;cm=max(cm,c);}}
        S.cand+=cn;if(cn>1)S.cand_collision_excess+=cn-1;
        if(cn){if(cm==mx)++S.surv;else{++S.dom;u64 cr=(mx-cm)/MOD;assert(cr>0);S.mincredit=min(S.mincredit,cr);S.maxcredit=max(S.maxcredit,cr);}}
        i=j;
    }
    return S;
}
void init(int q){Q=q;D=K-Q;p2v[0]=p3v[0]=1;for(int i=1;i<40;i++){p2v[i]=p2v[i-1]*2ULL;p3v[i]=p3v[i-1]*3ULL;}MOD=p3v[Q];for(int k=1;k<=K;k++){int z=0;while(p3v[z]<=p2v[k])++z;qminv[k]=z;}}
int main(int argc,char**argv){
    if(argc<2)return 2;string mode=argv[1];
    if(mode=="gen"){
        if(argc!=7)return 3;int mask;string dir;init(stoi(argv[2]));P=stoi(argv[3]);mask=stoi(argv[4]);B=stoi(argv[5]);dir=argv[6];
        if(Q<23||Q>25||P<0||P>8||mask<0||mask>=(1<<P)||B<=0)return 4;
        outs.resize(B);bucket_count.assign(B,0);for(int b=0;b<B;b++)outs[b].open(file_name(dir,mask,b),ios::binary|ios::trunc);
        int ev=0;u64 C=0;bool valid=true;for(int p=0;p<P;p++){bool odd=(mask>>p)&1;if(odd){int qnext=(p-ev)+1;C=3*C+p2v[p];valid=valid&&qnext>=qminv[p+1];}else{int qnext=p-ev;++ev;valid=valid&&qnext>=qminv[p+1];}}
        gen_rec(P,ev,C,valid);for(auto&o:outs)o.close();
        cout<<"Q "<<Q<<" P "<<P<<" MASK "<<mask<<" B "<<B<<" arbitrary_words "<<total_words<<" coefficient_words "<<coeff_words<<"\n";
        return 0;
    }
    if(mode=="process"){
        if(argc!=8)return 5;string dir;int b0,b1;init(stoi(argv[2]));P=stoi(argv[3]);B=stoi(argv[4]);b0=stoi(argv[5]);b1=stoi(argv[6]);dir=argv[7];
        if(Q<23||Q>25||P<0||P>8||B<=0||b0<0||b1>B||b0>=b1)return 6;
        vector<Stat> st(b1-b0);
        #pragma omp parallel for schedule(dynamic,1)
        for(int b=b0;b<b1;b++)st[b-b0]=process_bucket(dir,b);
        for(int b=b0;b<b1;b++){auto const&s=st[b-b0];cout<<b<<'\t'<<s.n<<'\t'<<s.classes<<'\t'<<s.cand<<'\t'<<s.surv<<'\t'<<s.cand_collision_excess<<'\t'<<s.dom<<'\t'<<(s.mincredit==UINT64_MAX?0:s.mincredit)<<'\t'<<s.maxcredit<<'\n';}
        return 0;
    }
    return 7;
}
