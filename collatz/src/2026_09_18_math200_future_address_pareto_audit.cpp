// MATH-200 finite future-address audit for the MATH-199 terminal Pareto records.
//
// This recomputes the coefficient-valid terminal Pareto records for K=28,29,30
// and measures the MATH-096 singleton key X mod 2^73.
//
// Finite regression only. Collatz remains open.
//
// Build:
//   g++ -O3 -std=c++20 file.cpp -o cert
//
#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

struct Point { u64 off; u128 C; };

static u64 inv64(u64 a, int bits) {
    u64 x = 1;
    for (int i=0;i<6;i++) x *= 2-a*x;
    if (bits < 64) x &= ((1ULL<<bits)-1);
    return x;
}

static u128 inv128(u128 a, int bits) {
    u128 mask = ((u128)1<<bits)-1;
    u128 x = 1;
    for (int i=0;i<8;i++) x = (x*(2-a*x)) & mask;
    return x;
}

int main() {
    const u128 MASK73 = ((u128)1<<73)-1;

    for (int K : {28,29,30}) {
        const u64 MOD = 1ULL<<K;
        const u64 MASK = MOD-1;

        vector<u64> p3m(K+1,1), invm(K+1,1);
        for (int q=1;q<=K;q++) p3m[q]=(p3m[q-1]*3ULL)&MASK;
        for (int q=0;q<=K;q++) invm[q]=inv64(p3m[q],K);

        vector<vector<Point>> groups(K+1);

        function<void(int,int,u128,u128)> dfs =
        [&](int k,int q,u128 C,u128 p3) {
            if (k==K) {
                u64 a = (u64)(0ULL - (((u64)C)&MASK)*invm[q]) & MASK;
                groups[q].push_back({a ? a : MOD, C});
                return;
            }

            int kp=k+1;
            u128 p2=(u128)1<<kp;

            if (p2<=p3) dfs(kp,q,C,p3);

            u128 p3o=p3*3;
            if (p2<=p3o)
                dfs(kp,q+1,3*C+((u128)1<<k),p3o);
        };

        dfs(0,0,0,1);

        unsigned long long total_records=0, classes73=0;
        vector<set<u128>> xclasses(K+1);

        for (int q=0;q<=K;q++) {
            auto &v=groups[q];
            if (v.empty()) continue;

            sort(v.begin(),v.end(),[](const Point&a,const Point&b){
                if (a.off!=b.off) return a.off<b.off;
                return a.C>b.C;
            });

            vector<Point> rec;
            bool have=false;
            u128 maxC=0;

            for (auto &p:v) {
                if (!have || p.C>maxC) {
                    have=true;
                    maxC=p.C;
                    rec.push_back(p);
                }
            }

            total_records += rec.size();

            u128 p3=1;
            for (int i=0;i<q;i++) p3*=3;
            u128 G=inv128(p3 & MASK73,73);

            for (auto &p:rec) {
                u128 N=((u128)1<<71)+p.off;
                u128 Y=(p3*N+p.C)>>K;
                u128 X=(G*(Y&MASK73))&MASK73;
                xclasses[q].insert(X);
            }

            classes73 += xclasses[q].size();
        }

        cout << "K " << K
             << " pareto " << total_records
             << " classes73 " << classes73 << "\n";

        assert(total_records==classes73);

        int min_unique=0;
        for (int bits=1;bits<=73;bits++) {
            u128 mask=((u128)1<<bits)-1;
            bool unique=true;
            for (int q=0;q<=K;q++) if (!xclasses[q].empty()) {
                set<u128> s;
                for (auto X:xclasses[q]) s.insert(X&mask);
                if (s.size()!=xclasses[q].size()) {
                    unique=false;
                    break;
                }
            }
            if (unique) {
                min_unique=bits;
                break;
            }
        }

        cout << "minimum_unique_bits " << min_unique << "\n";

        if (K==28) { assert(total_records==120); assert(min_unique==13); }
        if (K==29) { assert(total_records==122); assert(min_unique==12); }
        if (K==30) { assert(total_records==141); assert(min_unique==11); }
    }

    cout << "PASS MATH-200 future-address overpartition audit\n";
}
