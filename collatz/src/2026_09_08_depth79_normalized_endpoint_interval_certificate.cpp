// MATH-019: exact depth-79 internal-boundary normalized-endpoint interval audit.
//
// Build:
//   g++ -O3 -std=c++17 2026_09_08_depth79_normalized_endpoint_interval_certificate.cpp -o audit
//
// The calculation covers all 339 internal 2^61 boundaries and the complete
// depth-79 displacement halo D=2^29-1, using the DSD lift-bit halo generator
// and the MATH-018 G18 tail descriptor.
//
// No complete Collatz proof is claimed.

#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;

struct State { u128 y; uint8_t q; uint32_t low; };
struct Desc { uint8_t H, s; uint64_t correction; uint32_t t; };

static int qminv[80];
static u128 p3[80];

string dec128(u128 x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    reverse(s.begin(), s.end());
    return s;
}

uint64_t shortcut_u64(uint64_t n) {
    return (n & 1) ? (3*n + 1)/2 : n/2;
}

vector<State> generate_side(bool left, int m) {
    vector<State> v;
    v.reserve(5000000);
    v.push_back({0,0,0});

    for (int k=0;k<61;k++) {
        vector<State> nv;
        nv.reserve(k<m ? v.size()*2 : v.size());
        for (auto st: v) {
            int lo = (k<m) ? 0 : (left ? 1 : 0);
            int hi = (k<m) ? 1 : lo;
            for (int e=lo;e<=hi;e++) {
                u128 z = st.y + (e ? p3[st.q] : 0);
                int b = e ^ int(st.y & 1);
                int q2 = st.q + b;
                if (q2 < qminv[k+1]) continue;
                u128 y2 = b ? (3*z+1)/2 : z/2;
                uint32_t low = st.low;
                if (k<m && e) low |= (1u<<k);
                nv.push_back({y2, uint8_t(q2), low});
                if (k>=m) break;
            }
        }
        v.swap(nv);
    }

    const uint32_t maxlow = (1u<<m)-1;
    if (left) {
        // left offset ell ranges 1..D, so x mod 2^m cannot be zero
        v.erase(remove_if(v.begin(), v.end(), [](const State&s){return s.low==0;}), v.end());
    } else {
        // right offset r ranges 0..D-1 because ell>=1 and ell+r<=D
        v.erase(remove_if(v.begin(), v.end(), [&](const State&s){return s.low==maxlow;}), v.end());
    }
    return v;
}

struct CellRange {
    bool seen=false;
    u128 mn=0, mx=0;
    State mn_state{}, mx_state{};
    uint32_t mn_r=0, mx_r=0;
    Desc mn_desc{}, mx_desc{};
};

int main() {
    p3[0]=1;
    for(int i=1;i<80;i++) p3[i]=p3[i-1]*3;
    for(int k=1;k<80;k++) {
        int q=0; u128 p=1, target=((u128)1)<<k;
        while(p<target){p*=3; ++q;}
        qminv[k]=q;
    }

    constexpr int L=18;
    constexpr int M=1<<18;
    constexpr int MASK=M-1;
    constexpr int m=29;
    constexpr int D=(1<<29)-1;
    static_assert(D==536870911);
    assert(qminv[79]==50);
    assert(79-qminv[79]==29);

    vector<Desc> G(M);
    for(int r=0;r<M;r++) {
        uint64_t n=r;
        int s=0, H=-100;
        for(int j=1;j<=L;j++) {
            int b=n&1;
            s+=b;
            H=max(H,qminv[61+j]-s);
            n=shortcut_u64(n);
        }
        u128 corr=(u128)M*n-p3[s]*(u128)r;
        assert(corr <= numeric_limits<uint64_t>::max());
        G[r]={uint8_t(H),uint8_t(s),uint64_t(corr),uint32_t(n)};
    }

    auto right=generate_side(false,m);
    auto left =generate_side(true,m);
    assert(right.size()==964227);
    assert(left.size()==963422);

    static CellRange R[339][80], Lft[339][80];

    auto fill = [&](const vector<State>& states, bool is_left, CellRange out[339][80]) {
        const int a0=is_left ? 1024 : 1025;
        for(auto st: states) {
            u128 yp[19];
            for(int s=0;s<=18;s++) yp[s]=st.y*p3[s];
            int q=st.q;
            uint32_t step=(uint32_t)(p3[q]&MASK);
            uint32_t r=((uint32_t)(st.y&MASK)+(uint64_t)a0*step)&MASK;
            for(int j=0;j<339;j++) {
                Desc de=G[r];
                if(q>=de.H) {
                    int Q=q+de.s;
                    // Z = 2^18 E - a*3^Q = 3^s*y + C_tail(r)
                    u128 Z=yp[de.s]+de.correction;
                    auto &c=out[j][Q];
                    if(!c.seen) {
                        c.seen=true; c.mn=c.mx=Z;
                        c.mn_state=c.mx_state=st;
                        c.mn_r=c.mx_r=r;
                        c.mn_desc=c.mx_desc=de;
                    } else {
                        if(Z<c.mn){c.mn=Z;c.mn_state=st;c.mn_r=r;c.mn_desc=de;}
                        if(Z>c.mx){c.mx=Z;c.mx_state=st;c.mx_r=r;c.mx_desc=de;}
                    }
                }
                r=(r+step)&MASK;
            }
        }
    };

    fill(right,false,R);
    fill(left,true,Lft);

    long long common_cells=0;
    map<int,int> overlap_q_hist;
    u128 global_gap=~(u128)0;
    int gap_boundary=-1, gap_Q=-1;
    CellRange *gapL=nullptr, *gapR=nullptr;

    for(int j=0;j<339;j++) {
        int common_q=0;
        for(int Q=0;Q<80;Q++) if(Lft[j][Q].seen && R[j][Q].seen) {
            ++common_cells; ++common_q;
            auto &A=Lft[j][Q];
            auto &B=R[j][Q];
            // For left block label a and right label a+1,
            // endpoint equality with common Q is equivalent to
            //     Z_L = Z_R + 3^Q.
            u128 shifted_min=B.mn+p3[Q];
            u128 shifted_max=B.mx+p3[Q];
            // Exact observed ordering: every left endpoint lies below every
            // right endpoint in every common-(boundary,Q) cell.
            assert(A.mx < shifted_min);
            u128 gap=shifted_min-A.mx;
            if(gap<global_gap){global_gap=gap;gap_boundary=1025+j;gap_Q=Q;gapL=&A;gapR=&B;}
            (void)shifted_max;
        }
        overlap_q_hist[common_q]++;
    }

    assert(common_cells==5100);
    assert(overlap_q_hist[14]==43);
    assert(overlap_q_hist[15]==240);
    assert(overlap_q_hist[16]==54);
    assert(overlap_q_hist[17]==2);
    assert(gap_boundary==1241);
    assert(gap_Q==50);
    assert(global_gap==(u128)219414528);
    assert(global_gap % M == 0);
    assert(global_gap/M==837);

    // Extremal witness data for the smallest same-Q endpoint gap.
    assert(gapL && gapR);
    assert(gapL->mx_state.q==41);
    assert(gapL->mx_state.low==(1u<<29)-5); // left offset ell=5
    assert(gapL->mx_r==55268);
    assert(gapL->mx_desc.s==9);
    assert(gapR->mn_state.q==42);
    assert(gapR->mn_state.low==703);       // right offset r=703
    assert(gapR->mn_r==199268);
    assert(gapR->mn_desc.s==8);

    // Direct ordinary-integer regression of the extremal pair.
    u128 boundary=(u128)1241*((u128)1<<61);
    u128 NL=boundary-5;
    u128 NR=boundary+703;
    auto direct79=[&](u128 n){
        int q=0;
        for(int k=1;k<=79;k++) {
            int b=n&1; q+=b;
            assert(q>=qminv[k]);
            n=b?(3*n+1)/2:n/2;
        }
        return pair<u128,int>{n,q};
    };
    auto [EL,QL]=direct79(NL);
    auto [ER,QR]=direct79(NR);
    assert(QL==50 && QR==50);
    assert(ER>EL && ER-EL==837);

    cout << "PASS\n";
    cout << "right local states = " << right.size() << "\n";
    cout << "left local states = " << left.size() << "\n";
    cout << "common (boundary,Q) cells = " << common_cells << "\n";
    cout << "common-Q-count histogram: 14->43 15->240 16->54 17->2\n";
    cout << "all 5100 cells satisfy max(E_left) < min(E_right)\n";
    cout << "minimum same-Q endpoint separation = 837\n";
    cout << "witness boundary=1241 Q=50 left_offset=5 right_offset=703\n";
    cout << "NO INTERNAL CROSS-BOUNDARY ENDPOINT COLLISION AT DEPTH 79\n";
    cout << "NO COMPLETE COLLATZ PROOF CLAIM\n";
}
