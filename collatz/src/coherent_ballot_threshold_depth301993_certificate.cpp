#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

// Sharp integer threshold for the coherent Beatty-boundary argument through
// H=301,993, under the forced initial parity 11 (equivalently N == 3 mod 4).
//
// Define b_H=min{q:3^q>=2^H}.  If no coherent subcritical no-descent prefix
// has appeared earlier, the unique minimum-q prefix follows the mechanical
// boundary.  At a rise b_H=b_(H-1)+1, the only possible first subcritical
// state is its even offshoot and survives only if
//
//   R_(H-1) >= N (2^H - 3^(b_H-1)).
//
// This verifier proves that the smallest integer N0 for which every such rise
// offshoot is excluded through H=301,993 is
//
//   N0 = 5,205,340,380.
//
// N0 passes all rise inequalities, while N0-1 fails at H=125,743.
// Thus every N == 3 (mod 4) with N>=N0 satisfies
//
//   no descent through H <=301,993
//      => coefficient survival at every prefix through H.
//
// This is a finite auxiliary theorem, not a proof of Collatz.

using boost::multiprecision::cpp_int;

namespace {
constexpr int HMAX = 301'993;
constexpr unsigned long long N0 = 5'205'340'380ULL;

bool check(unsigned long long N, int& failH, int& failQ) {
    int q=0;
    cpp_int p3=1, p2=1, R=0;

    for (int H=1; H<=HMAX; ++H) {
        p2 <<= 1;
        bool rise=false;
        if (p3 < p2) {
            p3 *= 3;
            ++q;
            rise=true;
        }

        if (rise && H>=3) {
            const cpp_int D = p2 - p3/3;
            if (!(R < cpp_int(N)*D)) {
                failH=H;
                failQ=q-1;
                return false;
            }
        }

        if (rise) R = 3*R + (cpp_int(1) << (H-1));
    }
    failH=0;
    failQ=0;
    return true;
}
}

int main() {
    int h=0,q=0;
    if (!check(N0,h,q)) return 1;

    int hm=0,qm=0;
    if (check(N0-1,hm,qm)) return 2;
    if (hm != 125'743) return 3;
    if (qm != 79'335) return 4;

    // All current recursively sufficient layers m>=20 lie above N0.
    cpp_int m20min=4;
    for(int i=0;i<20;++i) m20min*=3;
    m20min+=3;
    if (!(m20min > N0)) return 5;

    cpp_int m19min=4;
    for(int i=0;i<19;++i) m19min*=3;
    m19min+=3;
    if (!(m19min < N0)) return 6;

    std::cout << "coherent ballot threshold depth301993: PASS\n";
    std::cout << "sharp_integer_threshold=" << N0 << "\n";
    std::cout << "threshold_minus_one_first_failure_H=" << hm
              << " q=" << qm << "\n";
    std::cout << "recursively sufficient layers m>=20 are covered\n";
    return 0;
}
