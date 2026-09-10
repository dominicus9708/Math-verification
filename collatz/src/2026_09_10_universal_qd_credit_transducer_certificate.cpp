// Universal (q,d) credit-transducer certificate for the one-sided root-Hensel branch.
//
// Algebraic reduction after MATH-051.
// This file shows that the fixed-d solvers are slices of one recurrence.
// It does not prove the Collatz conjecture.
//
// q = number of odd shortcut steps, d = number of even shortcut steps.
// For candidate even rank j with cumulative odd-gap G_j,
//
//   coefficient-valid  <=>  3^G_j > 2^(G_j+j+1).
//
// Hence the universal deadline is
//
//   ell_j = ceil((j+1) log_{3/2} 2),
//
// and its exact inverse capacity is
//
//   m(r) = floor(r log_2(3/2)),
//
// equivalently the greatest a with 3^r > 2^(r+a).
// A reverse gap state with a remaining candidate ranks is admissible iff a<=m(r).
//
// The older carry h and remaining candidate/competitor ranks a,b are replaced by
//
//   chi = h + 2^b - 2^a.
//
// If the current gap level is consumed leaving a',b', then exactly
//
//   chi' = (2 chi + 2^b' - 2^a') / 3,
//
// with integral divisibility required. Initial chi is 0; at r=0 the exact
// positive-translation condition is simply chi>0.
//
// Therefore can(r,a,b,chi) below is a UNIVERSAL viability recurrence: it contains
// no original fixed-d parameter. q supplies the initial gap horizon and d only
// supplies the initial state (a,b,chi)=(d,d,0).
//
// Audited implementation scope here: q<=41, d<=15, sufficient to regress the
// completed depth-41 MATH-051 calculation. The mathematical identities are not
// claimed to solve the arbitrary-d closure problem.

#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using i128 = __int128_t;

static i128 P2[80], P3[80];
static vector<int> CAP;
static constexpr int HB = 1 << 20;

static inline uint32_t enc(int b, int chi) {
    int v = chi + HB;
    if (v < 0 || v >= (1 << 21)) abort();
    return ((uint32_t)b << 21) | (uint32_t)v;
}
static inline void dec(uint32_t x, int& b, int& chi) {
    b = (int)(x >> 21);
    chi = (int)(x & ((1u << 21) - 1)) - HB;
}

struct MemoKey {
    uint8_t r, a, b;
    int32_t chi;
    bool operator==(MemoKey const& o) const noexcept {
        return r==o.r && a==o.a && b==o.b && chi==o.chi;
    }
};
struct MemoHash {
    size_t operator()(MemoKey const& x) const noexcept {
        uint64_t z=(uint32_t)x.chi;
        z^=(uint64_t)x.r<<32; z^=(uint64_t)x.a<<40; z^=(uint64_t)x.b<<48;
        z^=z>>33; z*=0xff51afd7ed558ccdULL; z^=z>>33;
        return (size_t)z;
    }
};
struct StateKey {
    uint8_t a;
    vector<uint32_t> frontier;
    bool operator==(StateKey const& o) const noexcept {
        return a==o.a && frontier==o.frontier;
    }
};
struct StateHash {
    size_t operator()(StateKey const& k) const noexcept {
        uint64_t h=0x9e3779b97f4a7c15ULL^k.a;
        for(uint32_t x:k.frontier){
            uint64_t z=x+0x9e3779b97f4a7c15ULL;
            z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
            z=(z^(z>>27))*0x94d049bb133111ebULL; z^=z>>31;
            h^=z+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);
        }
        return (size_t)h;
    }
};

struct UniversalSolver {
    unordered_map<MemoKey,uint8_t,MemoHash> memo;

    bool upper_possible(int r, int a, int b, int chi) const {
        if (a > CAP[r]) return false;
        i128 U = (i128)chi * P2[r] + (P2[b]-1) * (P3[r]-P2[r]);
        return U > 0;
    }

    bool can(int r, int a, int b, int chi) {
        if (!upper_possible(r,a,b,chi)) return false;
        if (r==0) return a==0 && chi>0;

        MemoKey key{(uint8_t)r,(uint8_t)a,(uint8_t)b,(int32_t)chi};
        auto it=memo.find(key);
        if(it!=memo.end()) return it->second;

        bool ok=false;
        int max_a2=min(a,CAP[r-1]);
        for(int a2=0;a2<=max_a2 && !ok;++a2){
            for(int b2=0;b2<=b;++b2){
                int num=2*chi+(1<<b2)-(1<<a2);
                if(num%3) continue;
                int chi2=num/3;
                if(can(r-1,a2,b2,chi2)){ok=true;break;}
            }
        }
        memo.emplace(key,(uint8_t)ok);
        return ok;
    }

    vector<uint32_t> transition(vector<uint32_t> const& F, int rnew, int a2) {
        vector<uint32_t> out;
        out.reserve(F.size()*2+8);
        for(uint32_t p:F){
            int b,chi; dec(p,b,chi);
            for(int b2=0;b2<=b;++b2){
                int num=2*chi+(1<<b2)-(1<<a2);
                if(num%3) continue;
                int chi2=num/3;
                if(can(rnew,a2,b2,chi2)) out.push_back(enc(b2,chi2));
            }
        }
        sort(out.begin(),out.end());
        out.erase(unique(out.begin(),out.end()),out.end());
        return out;
    }

    pair<u64,size_t> dominated(int q, int d) {
        if(d>CAP[q]) return {0,1};
        unordered_map<StateKey,u64,StateHash> dp, next;
        dp.emplace(StateKey{(uint8_t)d,{enc(d,0)}},1);
        size_t peak=1;

        for(int r=q;r>=1;--r){
            next.clear(); next.reserve(max<size_t>(1024,dp.size()*2));
            for(auto const& kv:dp){
                int a=kv.first.a;
                for(int a2=0;a2<=min(a,CAP[r-1]);++a2){
                    auto F2=transition(kv.first.frontier,r-1,a2);
                    if(F2.empty()) continue;
                    StateKey key{(uint8_t)a2,move(F2)};
                    next[key]+=kv.second;
                }
            }
            dp.swap(next); peak=max(peak,dp.size());
        }

        u64 D=0;
        for(auto const& kv:dp){
            if(kv.first.a!=0) continue;
            bool dominated=false;
            for(uint32_t p:kv.first.frontier){
                int b,chi; dec(p,b,chi);
                if(chi>0){dominated=true;break;}
            }
            if(dominated) D+=kv.second;
        }
        return {D,peak};
    }
};

static int deadline_by_integer_test(int j) {
    int G=0;
    while(P3[G] <= P2[G+j+1]) ++G;
    return G;
}

int main() {
    P2[0]=P3[0]=1;
    for(int i=1;i<80;++i){P2[i]=P2[i-1]*2; P3[i]=P3[i-1]*3;}

    CAP.assign(42,0);
    for(int r=0;r<=41;++r){
        int a=0;
        while(a<20 && P3[r] > P2[r+a+1]) ++a;
        CAP[r]=a;
    }

    for(int r=0;r<=41;++r){
        for(int a=0;a<=15;++a){
            bool lhs = (a==0) || (deadline_by_integer_test(a-1)<=r);
            bool rhs = a<=CAP[r];
            if(lhs!=rhs){cerr<<"capacity/deadline mismatch\n"; return 2;}
        }
    }

    struct Case {int q,d; u64 expected;};
    vector<Case> tests={
        {30,10,54028926ULL},
        {29,11,124678824ULL},
        {29,12,361499293ULL},
        {28,13,586723760ULL},
        {27,14,703863494ULL},
        {26,15,355002462ULL}
    };

    for(auto t:tests){
        UniversalSolver s;
        auto [got,peak]=s.dominated(t.q,t.d);
        cout<<"q="<<t.q<<" d="<<t.d<<" D="<<got
            <<" expected="<<t.expected<<" peak="<<peak
            <<" memo="<<s.memo.size()<<"\n";
        if(got!=t.expected) return 3;
    }
    cout<<"PASS universal (q,d) credit-transducer regression against MATH-051\n";
    return 0;
}
