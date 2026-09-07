// MATH-025: exact rolling 11-step tail operator.
//
// Generalizes the MATH-011 61+11 descriptor from one fixed base depth to an
// arbitrary base depth K.  For n mod 2^11 = u, the next 11 shortcut parities
// are fixed by u.  The operator stores their odd-count prefix, total odd count
// s(u), and exact affine correction c(u).
//
// This certificate audits K=0..1024 against the frozen 2^71 coefficient floor.
// It is a local exact continuation operator, not a Collatz proof.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std;
using boost::multiprecision::cpp_int;

struct Desc {
    int s;
    long long c;
    array<int,12> pref;
};

int main() {
    const int W = 11;
    const int MOD = 1 << W;
    const int KMAX = 1024;

    long long p3[12];
    p3[0] = 1;
    for (int i = 1; i <= W; ++i) p3[i] = p3[i-1] * 3;

    vector<Desc> D(MOD);

    // Residue-local parity/affine descriptors.
    for (int u = 0; u < MOD; ++u) {
        long long n = u;
        int s = 0;
        array<int,12> pref{};
        pref[0] = 0;

        for (int j = 1; j <= W; ++j) {
            const bool odd = (n & 1LL) != 0;
            if (odd) { n = (3*n + 1) / 2; ++s; }
            else n /= 2;
            pref[j] = s;
        }

        // 2^11*T^11(u) = 3^s*u + c.
        const long long c = (long long)MOD * n - p3[s] * (long long)u;
        assert(c >= 0);
        D[u] = {s,c,pref};

        // Exact transition regression for arbitrary lifts n=u+2^11*t.
        const vector<cpp_int> lifts = {
            0, 1, 2, 17, cpp_int(123456789), (cpp_int(1) << 80) + 12345
        };

        for (const cpp_int &t : lifts) {
            cpp_int x = cpp_int(u) + cpp_int(MOD) * t;
            cpp_int z = x;
            int ss = 0;

            for (int j = 1; j <= W; ++j) {
                const bool odd = (z & 1) != 0;
                if (odd) { z = (3*z + 1) / 2; ++ss; }
                else z /= 2;
            }

            const cpp_int affine = (cpp_int(p3[s]) * x + c) / MOD;
            assert(ss == s);
            assert(z == affine);
        }
    }

    // Exact threshold arrays. qpub is the frozen published-floor predicate
    // (3+2^-71)^q > 2^k. qmin is the simple 3^q >= 2^k threshold.
    vector<int> qmin(KMAX + W + 1), qpub(KMAX + W + 1);
    cpp_int threep = 1, two = 1;
    int qs = 0;

    const cpp_int B = cpp_int(1) << 71;
    const cpp_int A = 3*B + 1;
    cpp_int ap = 1, bp = 1;
    int qp = 0;

    for (int k = 1; k <= KMAX + W; ++k) {
        two *= 2;
        while (threep < two) { threep *= 3; ++qs; }
        qmin[k] = qs;

        while (!(ap > two * bp)) {
            ap *= A;
            bp *= B;
            ++qp;
        }
        qpub[k] = qp;
        assert(qpub[k] == qmin[k]);
    }

    // For arbitrary base depth K and residue u, define
    // H_K(u)=max_j(qpub[K+j]-s_j(u)).
    // Then q0 >= H_K(u) is exactly equivalent to passing every one of the
    // next 11 coefficient thresholds.
    long long checks = 0;

    for (int K = 0; K <= KMAX; ++K) {
        for (int u = 0; u < MOD; ++u) {
            int H = INT_MIN;
            for (int j = 1; j <= W; ++j)
                H = max(H, qpub[K+j] - D[u].pref[j]);

            for (int q0 : {max(0,H-1), max(0,H), max(0,H+1)}) {
                bool direct = true;
                int q = q0;

                for (int j = 1; j <= W; ++j) {
                    q += D[u].pref[j] - D[u].pref[j-1];
                    if (q < qpub[K+j]) { direct = false; break; }
                }

                const bool descriptor = q0 >= H;
                assert(direct == descriptor);
                ++checks;
            }
        }
    }

    assert(checks == 6'297'600);

    cout << "PASS\n";
    cout << "residues=2048 window=11 K=0..1024\n";
    cout << "threshold boundary checks=" << checks << "\n";
    cout << "transition lifts tested per residue=6\n";
    cout << "survive iff q>=H_K(u)\n";
    cout << "q'=q+s(u)\n";
    cout << "n'=(3^s n+c(u))/2^11\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
