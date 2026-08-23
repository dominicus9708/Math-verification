#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

// Exact dynamic program for complete whole-prefix Hensel correction classes.
//
// For a length-H parity word with q odd bits, let R be its correction in
//
//   T^H(N) = (3^q N + R)/2^H.
//
// Define S[H,q] as the set of residues R mod 3^q realized by all length-H
// q-odd words.  Appending one bit gives the exact set recurrence
//
//   S[H+1,q] = S[H,q]
//                union { 3 r + 2^H (mod 3^q) : r in S[H,q-1] }.
//
// A minimal counterexample whose whole H-prefix is non-maximal inside its
// (q,R mod 3^q) class has a smaller root predecessor merging at time H.
// Hence the number of possible whole-prefix maximal representatives is at
// most sum_q |S[H,q]|.  If coefficient survival is imposed at the terminal
// horizon, q >= ceil(H log_3 2), so only the corresponding upper tail is
// relevant.
//
// This certificate computes the class sets exactly through H=28.  It is a
// finite-growth diagnostic, not an asymptotic entropy theorem and not a proof
// of Collatz.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

std::vector<u64> odd_image(const std::vector<u64>& src,u64 add,u64 mod) {
    std::vector<u64> out;
    out.reserve(src.size());
    for (u64 r:src)
        out.push_back(static_cast<u64>((u128(3)*r+add)%mod));
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    return out;
}

std::vector<u64> merge_unique(const std::vector<u64>& a,
                              const std::vector<u64>& b) {
    std::vector<u64> out;
    out.reserve(a.size()+b.size());
    std::size_t i=0,j=0;
    while (i<a.size() || j<b.size()) {
        u64 x;
        if (j==b.size() || (i<a.size() && a[i]<b[j])) x=a[i++];
        else if (i==a.size() || b[j]<a[i]) x=b[j++];
        else { x=a[i]; ++i; ++j; }
        if (out.empty() || out.back()!=x) out.push_back(x);
    }
    return out;
}

int qmin_terminal(int H,const std::vector<u64>& p3) {
    const u64 p2=u64(1)<<H;
    int q=0;
    while (p3[q]<p2) ++q;
    return q;
}

} // namespace

int main() {
    constexpr int HMAX=28;
    std::vector<u64> p3(HMAX+2,1);
    for (int q=1;q<int(p3.size());++q) {
        const u128 z=u128(3)*p3[q-1];
        assert(z<=std::numeric_limits<u64>::max());
        p3[q]=static_cast<u64>(z);
    }

    constexpr std::array<u64,29> EXPECT_TOTAL{
        1,2,4,7,12,21,38,69,127,235,438,819,1535,2883,5425,
        10218,19275,36403,68835,130306,246912,468345,889180,
        1689686,3213595,6116464,11650326,22207183,42356936
    };

    std::vector<std::vector<u64>> S(HMAX+2);
    S[0]={0};

    std::cout << "H,total_classes,qmin,terminal_high_classes,high_exclusion_rate\n";
    std::cout << "0,1,0,1,0\n";

    for (int H=0;H<HMAX;++H) {
        std::vector<std::vector<u64>> T(HMAX+2);
        const u64 add=u64(1)<<H;
        for (int q=0;q<=H+1;++q) {
            if (q==0) {
                T[q]=S[q];
                continue;
            }
            const auto odd=odd_image(S[q-1],add,p3[q]);
            T[q]=merge_unique(S[q],odd);
        }
        S.swap(T);

        u64 total=0;
        for (int q=0;q<=H+1;++q) total+=S[q].size();
        assert(total==EXPECT_TOTAL[H+1]);

        const int qmin=qmin_terminal(H+1,p3);
        u64 high=0;
        for (int q=qmin;q<=H+1;++q) high+=S[q].size();

        const long double exclusion=
            1.0L-std::log2(static_cast<long double>(high))/(H+1);
        std::cout << (H+1) << ',' << total << ',' << qmin << ',' << high
                  << ',' << std::setprecision(12) << exclusion << '\n';
    }

    // Reproduce the previously audited H=19 class vector exactly.
    // (The current S is H=28, so independently regenerate to H=19.)
    std::vector<std::vector<u64>> A(HMAX+2);
    A[0]={0};
    for (int H=0;H<19;++H) {
        std::vector<std::vector<u64>> B(HMAX+2);
        const u64 add=u64(1)<<H;
        for (int q=0;q<=H+1;++q) {
            if (q==0) B[q]=A[q];
            else B[q]=merge_unique(A[q],odd_image(A[q-1],add,p3[q]));
        }
        A.swap(B);
    }
    constexpr std::array<u64,20> H19{
        1,2,6,18,54,162,486,1458,4352,11692,23557,31072,27469,
        17527,8411,3048,817,154,19,1
    };
    for (int q=0;q<=19;++q) assert(A[q].size()==H19[q]);

    const int qmin28=qmin_terminal(28,p3);
    assert(qmin28==18);
    u64 high28=0;
    for (int q=qmin28;q<=28;++q) high28+=S[q].size();
    assert(high28==14'387'029);

    std::cout << "H28 total classes=42356936\n";
    std::cout << "H28 terminal coefficient-threshold classes=14387029\n";
    std::cout << "H28 terminal high-q exclusion rate approximately 0.150776237048\n";
    std::cout << "whole-prefix Hensel class growth: PASS\n";
}
