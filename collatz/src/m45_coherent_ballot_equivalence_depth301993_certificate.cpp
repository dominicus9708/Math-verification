#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

// Exact coherent no-descent => coefficient-survival certificate for the
// current m=45 recursively sufficient layer, through H=301,993.
//
// Accelerated Collatz map:
//   T(n)=n/2            for even n,
//   T(n)=(3n+1)/2       for odd n.
//
// For a length-H parity prefix with q odd symbols,
//   2^H T^H(N) = 3^q N + R_H.
//
// Current m=45 roots satisfy
//   N >= NMIN = 4*3^45+3
// and N == 3 (mod 4), hence the first two parity symbols are forced 11.
//
// Put b_H=min{q:3^q>=2^H}.  Inductively, if no coherent subcritical
// no-descent state has appeared earlier, the unique minimum-q surviving prefix
// is the mechanical Beatty boundary q=b_H.  A FIRST subcritical state can be
// born only at a rise b_H=b_(H-1)+1 by taking the even child of the previous
// mechanical boundary prefix.  Its correction is unchanged, so it survives
// only if
//
//   R_(H-1) >= N (2^H - 3^(b_H-1)).
//
// It suffices to test N=NMIN.  This program checks the strict opposite
// inequality at every rise H<=301,993 using exact cpp_int arithmetic.
//
// Therefore every current m=45 orbit which has not descended below its start
// through H<=301,993 must satisfy the coefficient-survival inequality at every
// prefix through H.
//
// This is a finite theorem for m=45, not a proof of the Collatz conjecture.

using boost::multiprecision::cpp_int;

int main() {
    constexpr int HMAX = 301'993;

    cpp_int NMIN = 4;
    for (int i=0;i<45;++i) NMIN *= 3;
    NMIN += 3;

    int q = 0;
    cpp_int p3 = 1;  // 3^q on the mechanical boundary
    cpp_int p2 = 1;  // 2^H
    cpp_int R = 0;   // correction of the mechanical boundary prefix

    long long rise_count = 0;

    for (int H=1; H<=HMAX; ++H) {
        p2 <<= 1;

        bool rise = false;
        if (p3 < p2) {
            p3 *= 3;
            ++q;
            rise = true;
        }

        if (rise && H>=3) {
            ++rise_count;

            const cpp_int previous_p3 = p3 / 3; // 3^(b_H-1)
            const cpp_int D = p2 - previous_p3;
            if (!(D > 0)) return 1;

            // Exact exclusion of the unique possible first coherent
            // subcritical even offshoot.
            if (!(R < NMIN * D)) {
                std::cerr << "coherent subcritical birth at H=" << H
                          << " previous_q=" << (q-1) << "\n";
                return 2;
            }
        }

        // Follow the unique minimum-q coefficient-surviving boundary child.
        if (rise) {
            R = 3*R + (cpp_int(1) << (H-1));
        }
        // Plateau child is even, so R is unchanged.
    }

    if (rise_count != 190'535) return 3;
    if (q != 190'537) return 4;

    std::cout << "m45 coherent ballot equivalence: PASS\n";
    std::cout << "certified through H=" << HMAX << "\n";
    std::cout << "Beatty rises checked=" << rise_count << "\n";
    std::cout << "terminal boundary odd count=" << q << "\n";
    std::cout << "H=195,q=123 endpoint-only exception cannot occur coherently\n";
    return 0;
}
