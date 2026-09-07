// MATH-033: base-independent critical-prefix descriptor for the exact
// 22-step coefficient-survival predicate at the frozen published floor.
//
// For a 22-step parity residue u, let s_j(u) be the number of odd shortcut
// steps through prefix j.  With c0=(3*2^71+1)/2^71 and
// beta=log(2)/log(c0), choose the unique j* maximizing beta*j-s_j.
// Then for every base depth K,
//
//   max_j (q_pub(K+j)-s_j) = q_pub(K+j*)-s_{j*},
//
// because q_pub(t)=ceil(beta*t) and s_{j*}-s_j is an integer.  The code
// computes j* without floating point by exact power comparisons and regresses
// the resulting threshold on all 2^22 residues at six separated base depths.
//
// This is a local exact descriptor theorem, not a Collatz proof.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std;
using boost::multiprecision::cpp_int;

static const int W = 22;
static const int MOD = 1 << W;
static const int KMAX = 1029 + W;

cpp_int A, B, pA[W + 1], pB[W + 1], p2[W + 1];
int qpub[KMAX + 1];

// Exact comparison of beta*j1-s1 and beta*j2-s2.
// For positive dj=j1-j2 and ds=s1-s2,
// beta*dj > ds iff 2^dj * B^ds > A^ds.
int compare_score(int j1, int s1, int j2, int s2) {
    const int dj = j1 - j2;
    const int ds = s1 - s2;

    if (dj == 0) return ds < 0 ? 1 : (ds > 0 ? -1 : 0);
    if (ds == 0) return dj > 0 ? 1 : -1;
    if (dj > 0 && ds < 0) return 1;
    if (dj < 0 && ds > 0) return -1;

    if (dj > 0) { // then ds>0
        const cpp_int lhs = p2[dj] * pB[ds];
        const cpp_int &rhs = pA[ds];
        // Equality would force the odd integer A^ds to be a power of two
        // times B^ds, impossible for ds>0.
        assert(lhs != rhs);
        return lhs > rhs ? 1 : -1;
    }

    // dj<0 and ds<0: compare the positive differences and reverse the sign.
    const cpp_int lhs = p2[-dj] * pB[-ds];
    const cpp_int &rhs = pA[-ds];
    assert(lhs != rhs);
    return lhs > rhs ? -1 : 1;
}

int main() {
    B = cpp_int(1) << 71;
    A = 3 * B + 1;

    pA[0] = pB[0] = p2[0] = 1;
    for (int i = 1; i <= W; ++i) {
        pA[i] = pA[i - 1] * A;
        pB[i] = pB[i - 1] * B;
        p2[i] = p2[i - 1] * 2;
    }

    // Frozen published-floor threshold q_pub(k): minimal q with
    // ((3*2^71+1)/2^71)^q > 2^k.
    cpp_int two = 1, ap = 1, bp = 1;
    int q = 0;
    for (int k = 1; k <= KMAX; ++k) {
        two *= 2;
        while (!(ap > two * bp)) {
            ap *= A;
            bp *= B;
            ++q;
        }
        qpub[k] = q;
    }

    const array<int, 6> bases = {0, 61, 83, 127, 545, 1007};
    array<unsigned long long, W + 1> critical_hist{};
    unsigned long long checked = 0;

    for (int u = 0; u < MOD; ++u) {
        uint64_t n = u;
        int s = 0;
        int jcrit = 1;
        int scrit = 0;
        array<uint8_t, W + 1> prefix_odds{};

        for (int j = 1; j <= W; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) {
                n = (3 * n + 1) / 2;
                ++s;
            } else {
                n /= 2;
            }
            prefix_odds[j] = uint8_t(s);

            if (j == 1 || compare_score(j, s, jcrit, scrit) > 0) {
                jcrit = j;
                scrit = s;
            }
        }

        ++critical_hist[jcrit];

        // Finite regression of the algebraic theorem at widely separated
        // bases, including the first prefilter and later rolling bases.
        for (int K : bases) {
            int explicit_h = INT_MIN;
            for (int j = 1; j <= W; ++j)
                explicit_h = max(explicit_h,
                                 qpub[K + j] - int(prefix_odds[j]));

            const int critical_h = qpub[K + jcrit] - scrit;
            assert(explicit_h == critical_h);
            ++checked;
        }
    }

    assert(checked == uint64_t(MOD) * bases.size());
    unsigned long long histogram_sum = 0;
    for (int j = 1; j <= W; ++j) histogram_sum += critical_hist[j];
    assert(histogram_sum == MOD);

    cout << "PASS\n";
    cout << "residues=" << MOD
         << " bases_regressed=" << bases.size()
         << " threshold_equalities=" << checked << "\n";
    cout << "critical-prefix histogram:";
    for (int j = 1; j <= W; ++j)
        if (critical_hist[j]) cout << " " << j << ":" << critical_hist[j];
    cout << "\nCOLLATZ STATUS=OPEN\n";
}
