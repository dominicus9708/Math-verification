#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;
using u64 = unsigned long long;

static const long long A = 114208327604LL;
static const long long Q = 72057431991LL;

u128 addmod(u128 a, u128 b, u128 m) { u128 s=a+b; if (s>=m) s-=m; return s; }
u128 mulmod(u128 a, u128 b, u128 m) { u128 r=0; while (b) { if (b&1) r=addmod(r,a,m); b>>=1; if (b) a=addmod(a,a,m); } return r; }
u128 powmod(u128 a, unsigned long long e, u128 m) { u128 r=1%m; while(e){ if(e&1)r=mulmod(r,a,m); e>>=1; if(e)a=mulmod(a,a,m);} return r; }
u128 pow3i(int n) { u128 r=1; while(n--) r*=3; return r; }
long long mech(long long j) { return (long long)(((__int128)(j-1)*A)/Q); }
string dec(u128 x) { if(!x) return "0"; string s; while(x){ s.push_back(char('0'+x%10)); x/=10; } reverse(s.begin(),s.end()); return s; }
u128 parse128(const string &s) { u128 x=0; for(char c:s) x=x*10+(c-'0'); return x; }

const u128 LOW = (u128(1)<<71);
const u128 UPPER_TIMES_3 = 4*LOW + 3*(u128(1)<<33);
bool admissible(u128 y) { return LOW<y && 3*y<UPPER_TIMES_3 && (y&3)==3; }

struct Pair46 { u128 lo; u64 hi; };
struct PrefixDesc { int L, boundary; u64 initial_h; vector<pair<int,int>> later; };

int main() {
    const int m=65, split=19, K=10;
    const u128 M=pow3i(65), R=pow3i(46);
    const u64 P=(u64)pow3i(19);
    const u128 Y=parse128("2556679481397564529951");

    vector<long long> B(m);
    vector<int> gap(m,0);
    for(int t=0;t<m;t++) B[t]=mech(Q-m+1+t);
    for(int t=1;t<m;t++) { gap[t]=(int)(B[t]-B[t-1]); assert(gap[t]==1||gap[t]==2); }
    assert(split==m-46);

    u128 inv2=(M+1)/2, invA=powmod(inv2,A,M);
    vector<u128> p3(m); p3[0]=1; for(int i=1;i<m;i++) p3[i]=3*p3[i-1];
    vector<u128> base(m); u128 y_mech=0;
    for(int t=0;t<m;t++) {
        base[t]=mulmod(mulmod(invA,p3[m-1-t],M),powmod(2,B[t],M),M);
        y_mech=addmod(y_mech,base[t],M);
    }
    vector<array<u128,24>> C(m);
    for(int t=0;t<m;t++) {
        C[t].fill(0); u128 ip=1;
        for(int d=1;d<24;d++) { ip=mulmod(ip,inv2,M); C[t][d]=mulmod(base[t],ip-1,M); }
    }

    // Exact prefix high-state sets: first 19 coordinates, normalized by 3^46.
    // Initial positive runs are compressed using the primitive-root image.
    array<array<unordered_set<u64>,9>,9> S;
    for(int p=0;p<=8;p++) for(int L=0;L<=p;L++) {
        function<void(int,int,int,u64)> rec = [&](int t,int left,int prev,u64 h) {
            if(left<0 || left>split-t) return;
            if(t==split) {
                if(left) return;
                int boundary=prev; assert(boundary<=8);
                if(L==0) { S[p][boundary].insert(h); return; }
                u128 q=pow3i(m-L);
                u64 unit=(u64)((base[L-1]/q)%3); assert(unit==1||unit==2);
                u64 scale=(u64)pow3i(19-L), modL=(u64)pow3i(L);
                for(u64 x=0;x<modL;x++) if(x%3==0 || x%3==unit) {
                    u64 v=(h+(u128)scale*x%P)%P;
                    S[p][boundary].insert(v);
                }
                return;
            }
            rec(t+1,left,0,h);
            if(!left) return;
            if(prev==0) {
                if(t>0 && gap[t]==2) {
                    assert(C[t][1]%R==0);
                    rec(t+1,left-1,1,(h+(u64)(C[t][1]/R))%P);
                }
            } else {
                int md=prev+gap[t]-1; assert(md<24);
                for(int d=1;d<=md;d++) {
                    assert(C[t][d]%R==0);
                    rec(t+1,left-1,d,(h+(u64)(C[t][d]/R))%P);
                }
            }
        };
        rec(L+1,p-L,0,0);
    }
    const size_t PREFIX_DISTINCT[9]={1,13,90,444,1762,6006,18297,51023,132317};
    for(int p=0;p<=8;p++) {
        size_t n=0; for(int d=0;d<=p;d++) n+=S[p][d].size();
        assert(n==PREFIX_DISTINCT[p]);
    }

    array<array<unordered_set<u64>,10>,9> U;
    for(int p=0;p<=8;p++) for(int req=0;req<=p;req++)
        for(int bd=req;bd<=p;bd++) U[p][req].insert(S[p][bd].begin(),S[p][bd].end());

    Pair46 y0{y_mech%R,(u64)(y_mech/R)};
    vector<array<Pair46,24>> CP(m);
    for(int t=split;t<m;t++) for(int d=1;d<24;d++)
        CP[t][d]={C[t][d]%R,(u64)(C[t][d]/R)};
    auto addpair = [&](Pair46 a, Pair46 c) {
        u128 lo=a.lo+c.lo; u64 carry=0;
        if(lo>=R){lo-=R;carry=1;}
        u64 hi=a.hi+c.hi+carry; if(hi>=P) hi%=P;
        return Pair46{lo,hi};
    };

    const unsigned long long EXPECT_LEAVES[9]={
        234334166ULL,88391047ULL,28849080ULL,8060208ULL,1900479ULL,
        370946ULL,58342ULL,7106ULL,629ULL
    };
    unsigned long long total_leaves=0,total_join_hits=0;
    u64 unique_need=0; int unique_req=-1;

    for(int p=0;p<=8;p++) {
        int s=K-p;
        unsigned long long leaves=0,hits=0;
        function<void(int,int,int,int,Pair46)> rec = [&](int t,int left,int prev,int req,Pair46 cur) {
            if(left<0 || left>m-t) return;
            if(t==m) {
                if(left) return;
                leaves++;
                if(!admissible(cur.lo)) return;
                u64 need=cur.hi ? P-cur.hi : 0;
                if(U[p][req].find(need)!=U[p][req].end()) {
                    hits++;
                    if(p==3) { unique_need=need; unique_req=req; assert(cur.lo==Y); }
                }
                return;
            }
            rec(t+1,left,0,req,cur);
            if(!left) return;
            if(t==split) {
                int md=p+gap[t]-1;
                for(int d=1;d<=md;d++) {
                    int rq=max(0,d-gap[t]+1);
                    rec(t+1,left-1,d,rq,addpair(cur,CP[t][d]));
                }
            } else if(prev==0) {
                if(gap[t]==2) rec(t+1,left-1,1,req,addpair(cur,CP[t][1]));
            } else {
                int md=prev+gap[t]-1; assert(md<24);
                for(int d=1;d<=md;d++) rec(t+1,left-1,d,req,addpair(cur,CP[t][d]));
            }
        };
        rec(split,s,0,0,y0);
        assert(leaves==EXPECT_LEAVES[p]);
        assert(hits==(p==3 ? 1ULL : 0ULL));
        total_leaves+=leaves; total_join_hits+=hits;
    }
    assert(total_leaves==361972003ULL);
    assert(total_join_hits==1ULL);
    assert(unique_need==193090230ULL && unique_req==0);

    vector<PrefixDesc> prefix_matches;
    const int p=3; const u64 TARGET=unique_need;
    for(int L=0;L<=p;L++) {
        vector<pair<int,int>> path;
        function<void(int,int,int,u64)> rec = [&](int t,int left,int prev,u64 h) {
            if(left<0 || left>split-t) return;
            if(t==split) {
                if(left) return;
                if(L==0) { if(h==TARGET) prefix_matches.push_back({L,prev,0,path}); return; }
                u128 q=pow3i(m-L); u64 unit=(u64)((base[L-1]/q)%3);
                u64 scale=(u64)pow3i(19-L), modL=(u64)pow3i(L);
                for(u64 x=0;x<modL;x++) if(x%3==0 || x%3==unit) {
                    if((h+(u128)scale*x%P)%P==TARGET) prefix_matches.push_back({L,prev,x,path});
                }
                return;
            }
            rec(t+1,left,0,h); if(!left) return;
            if(prev==0) {
                if(t>0 && gap[t]==2) { path.push_back({t,1}); rec(t+1,left-1,1,(h+(u64)(C[t][1]/R))%P); path.pop_back(); }
            } else {
                int md=prev+gap[t]-1;
                for(int d=1;d<=md;d++) { path.push_back({t,d}); rec(t+1,left-1,d,(h+(u64)(C[t][d]/R))%P); path.pop_back(); }
            }
        };
        rec(L+1,p-L,0,0);
    }
    assert(prefix_matches.size()==1);
    assert(prefix_matches[0].L==2 && prefix_matches[0].boundary==0 && prefix_matches[0].initial_h==7);
    { vector<pair<int,int>> expected={{7,1}}; assert(prefix_matches[0].later==expected); }

    vector<vector<pair<int,int>>> suffix_matches;
    vector<int> suffix_req;
    vector<pair<int,int>> path;
    function<void(int,int,int,int,Pair46)> recs = [&](int t,int left,int prev,int req,Pair46 cur) {
        if(left<0 || left>m-t) return;
        if(t==m) {
            if(left) return;
            u64 need=cur.hi ? P-cur.hi : 0;
            if(cur.lo==Y && need==TARGET) { suffix_matches.push_back(path); suffix_req.push_back(req); }
            return;
        }
        recs(t+1,left,0,req,cur); if(!left) return;
        if(t==split) {
            int md=p+gap[t]-1;
            for(int d=1;d<=md;d++) { path.push_back({t,d}); recs(t+1,left-1,d,max(0,d-gap[t]+1),addpair(cur,CP[t][d])); path.pop_back(); }
        } else if(prev==0) {
            if(gap[t]==2) { path.push_back({t,1}); recs(t+1,left-1,1,req,addpair(cur,CP[t][1])); path.pop_back(); }
        } else {
            int md=prev+gap[t]-1;
            for(int d=1;d<=md;d++) { path.push_back({t,d}); recs(t+1,left-1,d,req,addpair(cur,CP[t][d])); path.pop_back(); }
        }
    };
    recs(split,7,0,0,y0);
    assert(suffix_matches.size()==1 && suffix_req[0]==0);
    { vector<pair<int,int>> expected={{26,1},{28,1},{35,1},{52,1},{54,1},{57,1},{62,1}}; assert(suffix_matches[0]==expected); }

    vector<pair<int,int>> initial_classes;
    u128 q2=pow3i(63);
    for(int r0=0;r0<2;r0++) for(int r1=0;r1<6;r1++) {
        int d1=r1?r1:6;
        int d0=r0?r0:2;
        while(d1>d0+gap[1]-1) d0+=2;
        u128 c=addmod(C[0][d0],C[1][d1],M);
        assert(c%q2==0);
        if((u64)((c/q2)%9)==7) initial_classes.push_back({r0,r1});
    }
    sort(initial_classes.begin(),initial_classes.end());
    { vector<pair<int,int>> expected={{0,3},{1,1}}; assert(initial_classes==expected); }

    // D_tail(65)>=10 is imported from the previous certified ladder.
    // A support-10 state at m=66 must prepend a mechanical zero and therefore
    // restrict to one of the two m=65 equality classes above.
    vector<long long> B66(66); for(int t=0;t<66;t++) B66[t]=mech(Q-65+t);
    int new_gap=B66[1]-B66[0];
    assert(new_gap==1);
    // With new delta_0=0, ordering requires delta_1 <= new_gap-1 = 0,
    // while both equality classes have the shifted old t=0 coordinate positive.
    assert(new_gap-1==0);

    assert(Q-66>72);

    cout << "PASS first-resonance support-10 split certificate\n";
    cout << "m65 support10 split leaves=" << total_leaves << " joined_hits=1\n";
    cout << "unique compressed support=(0,1,7,26,28,35,52,54,57,62)\n";
    cout << "initial residue classes=(0 mod2,3 mod6),(1 mod2,1 mod6)\n";
    cout << "endpoint=" << dec(Y) << "\n";
    cout << "m66 new leading mechanical gap=1, so support10 cannot lift\n";
    cout << "D_tail(66)>=11\n";
    cout << "with D_72>=11: r_*>=22\n";
    cout << "coarse normalized correction: E/3^Q > 22/12 = 11/6\n";
}
