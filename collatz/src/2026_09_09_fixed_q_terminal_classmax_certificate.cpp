// Fixed-q terminal class-max certificate for one-sided root-Hensel survivor counts.
// Key reduction: if a prefix is dominated in its exact (q, C mod 3^q) class,
// appending the same suffix preserves the class relation and strict C ordering.
// Therefore a terminal class-max word automatically has class-max at every prefix.
// Coefficient admissibility is still checked at every prefix. Finite exact scope only.
#include <bits/stdc++.h>
using namespace std; using u64=uint64_t;
struct Item{u64 r, ctag;};
static int K,Q,D; static u64 MOD; static u64 p2v[40],p3v[40]; static int qminv[40];
static vector<Item> items;
static u64 coeff_count=0;
static constexpr u64 TAG=1ULL<<63;
void gen(int p,int ev,u64 C,bool valid){
    if(p==K){
        if(ev!=D) return;
        u64 q=K-D;
        bool v=valid && ((int)q==Q);
        if(v) ++coeff_count;
        items.push_back({C%MOD, C | (v?TAG:0)});
        return;
    }
    int remain=K-p;
    if(ev>D || ev+remain<D) return;
    if(ev+(remain-1)>=D){
        int qnext=(p-ev)+1;
        bool v2=valid && qnext>=qminv[p+1];
        gen(p+1,ev,3*C+p2v[p],v2);
    }
    if(ev<D){
        int qnext=p-ev;
        bool v2=valid && qnext>=qminv[p+1];
        gen(p+1,ev+1,C,v2);
    }
}
int main(int argc,char**argv){
    if(argc!=3){cerr<<"usage K Q\n";return 2;} K=stoi(argv[1]);Q=stoi(argv[2]);D=K-Q;
    if(K>35||Q<0||Q>K||D>12)return 3;
    p2v[0]=p3v[0]=1; for(int i=1;i<40;i++){p2v[i]=p2v[i-1]*2ULL;p3v[i]=p3v[i-1]*3ULL;}
    for(int k=1;k<=K;k++){int q=0;while(p3v[q]<=p2v[k])++q;qminv[k]=q;}
    MOD=p3v[Q];
    unsigned long long n=1; for(int i=1;i<=D;i++) n=n*(K-D+i)/i;
    items.reserve(n);
    gen(0,0,0,true);
    if(items.size()!=n){cerr<<"count mismatch "<<items.size()<<" "<<n<<"\n";return 4;}
    sort(items.begin(),items.end(),[](Item const&a,Item const&b){return a.r<b.r;});
    u64 classes=0,surv=0,cand_collisions=0,mincredit=UINT64_MAX,maxcredit=0;
    for(size_t i=0;i<items.size();){
        size_t j=i+1;while(j<items.size()&&items[j].r==items[i].r)++j;++classes;
        u64 mx=0; for(size_t t=i;t<j;t++) mx=max(mx,items[t].ctag&~TAG);
        int cand_in_class=0; u64 candmax=0;
        for(size_t t=i;t<j;t++) if(items[t].ctag&TAG){++cand_in_class;candmax=max(candmax,items[t].ctag&~TAG);}
        if(cand_in_class>1) cand_collisions += (u64)cand_in_class-1;
        if(cand_in_class){
            if(candmax==mx) ++surv;
            if(mx>candmax){u64 d=(mx-candmax)/MOD; if(d){mincredit=min(mincredit,d);maxcredit=max(maxcredit,d);}}
        }
        i=j;
    }
    cout<<"K "<<K<<" Q "<<Q<<" D "<<D<<"\n";
    cout<<"arbitrary_words "<<items.size()<<"\n";
    cout<<"coefficient_language_candidates "<<coeff_count<<"\n";
    cout<<"arbitrary_classes "<<classes<<"\n";
    cout<<"terminal_classmax_coefficient_survivors "<<surv<<"\n";
    cout<<"coefficient_candidate_collisions_excess "<<cand_collisions<<"\n";
    cout<<"dominated_candidate_class_credit_range "<<(mincredit==UINT64_MAX?0:mincredit)<<" "<<maxcredit<<"\n";
}
