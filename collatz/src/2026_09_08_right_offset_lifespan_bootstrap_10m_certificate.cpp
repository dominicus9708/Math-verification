// MATH-022: finite bootstrap of the MATH-021 linear collision halo.
//
// Compile:
//   g++ -O3 -std=c++17 -fopenmp \
//     2026_09_08_right_offset_lifespan_bootstrap_10m_certificate.cpp -o cert
// Run:
//   OMP_NUM_THREADS=8 ./cert
//
// The result is finite/exact within the stated internal-boundary candidate scope.
// It is not a Collatz proof.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#ifdef _OPENMP
#include <omp.h>
#endif

using namespace std;
using boost::multiprecision::cpp_int;

struct R61 {
    int r;
    cpp_int y;
    int q;
};

int main() {
    const int RMAX = 10'000'000;
    const int KCAP = 512;
    const int B0 = 1025;
    const int B1 = 1363;

    // Exact coefficient thresholds.  qmin[k] is the simpler 3^q >= 2^k
    // threshold; qpub[k] is the strict published-floor threshold
    // (3+2^-71)^q > 2^k.  They are checked equal through KCAP.
    vector<int> qmin(KCAP + 1), qpub(KCAP + 1);
    cpp_int two = 1, p3 = 1;
    int q3 = 0;

    cpp_int B = 1;
    for (int i = 0; i < 71; ++i) B *= 2;
    const cpp_int A = 3 * B + 1;
    cpp_int ap = 1, bp = 1;
    int qp = 0;

    for (int k = 1; k <= KCAP; ++k) {
        two *= 2;
        while (p3 < two) {
            p3 *= 3;
            ++q3;
        }
        qmin[k] = q3;

        while (!(ap > two * bp)) {
            ap *= A;
            bp *= B;
            ++qp;
        }
        qpub[k] = qp;
        assert(qpub[k] == qmin[k]);
    }

    vector<cpp_int> pow3(62);
    pow3[0] = 1;
    for (int i = 1; i <= 61; ++i) pow3[i] = pow3[i - 1] * 3;

    // Stage 1: exhaustive depth-61 right-offset filter on [0,RMAX].
    vector<R61> survivors;
    survivors.reserve(20'000);

    for (int r = 0; r <= RMAX; ++r) {
        cpp_int n = r;
        int q = 0;
        bool ok = true;

        for (int k = 1; k <= 61; ++k) {
            const bool odd = (n & 1) != 0;
            if (odd) {
                n = (3 * n + 1) / 2;
                ++q;
            } else {
                n /= 2;
            }

            if (q < qmin[k]) {
                ok = false;
                break;
            }
        }

        if (ok) survivors.push_back({r, n, q});
    }

    assert(!survivors.empty());
    assert(survivors.size() == 17'745);
    assert(survivors.front().r == 703);
    assert(survivors.back().r == 9'999'823);

    // Stage 2: continue every surviving lower-61 state through every one of
    // the 339 internal boundaries.  For N=b*2^61+r,
    // T^61(N)=T^61(r)+b*3^q, so we continue from that exact endpoint.
    //
    // MATH-021 says offset r first enters the collision-complete linear halo
    // at depth 3r+1.  Since the first possible entry is 2110, proving all
    // these states die before KCAP=512 is already enough to prove that none
    // reaches its halo-entry depth.
    atomic<int> unresolved{0};
    atomic<int> halo_entry_violation{0};
    atomic<int> max_lifespan{0};

    #pragma omp parallel for schedule(dynamic, 1)
    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        const auto &s = survivors[i];
        const long long entry_depth = 3LL * s.r + 1;
        int local_max = 61;

        for (int b = B0; b <= B1; ++b) {
            cpp_int n = s.y + cpp_int(b) * pow3[s.q];
            int q = s.q;
            int life = 61;

            for (int k = 62; k <= KCAP; ++k) {
                const bool odd = (n & 1) != 0;
                if (odd) {
                    n = (3 * n + 1) / 2;
                    ++q;
                } else {
                    n /= 2;
                }

                if (q < qmin[k]) {
                    life = k - 1;
                    break;
                }
                life = k;
            }

            local_max = max(local_max, life);
            if (life >= entry_depth) halo_entry_violation.fetch_add(1);
            if (life == KCAP) unresolved.fetch_add(1);
        }

        int old = max_lifespan.load();
        while (local_max > old &&
               !max_lifespan.compare_exchange_weak(old, local_max)) {}
    }

    assert(unresolved.load() == 0);
    assert(halo_entry_violation.load() == 0);
    assert(max_lifespan.load() == 429);

    // Deterministic regression for the unique first max-lifespan witness in
    // lexicographic (r,b) scan order.
    int witness_r = -1, witness_b = -1, exact_max = -1;
    for (const auto &s : survivors) {
        for (int b = B0; b <= B1; ++b) {
            cpp_int n = s.y + cpp_int(b) * pow3[s.q];
            int q = s.q;
            int life = 61;

            for (int k = 62; k <= 430; ++k) {
                const bool odd = (n & 1) != 0;
                if (odd) {
                    n = (3 * n + 1) / 2;
                    ++q;
                } else {
                    n /= 2;
                }
                if (q < qmin[k]) {
                    life = k - 1;
                    break;
                }
                life = k;
            }

            if (life > exact_max) {
                exact_max = life;
                witness_r = s.r;
                witness_b = b;
            }
        }
    }

    assert(exact_max == 429);
    assert(witness_r == 276'199);
    assert(witness_b == 1177);

    const long long exclusion_depth = 3LL * RMAX + 3;
    assert(exclusion_depth == 30'000'003);

    cout << "PASS\n";
    cout << "RMAX=" << RMAX << "\n";
    cout << "published-floor q_min == 3^q threshold for depths 1.."
         << KCAP << "\n";
    cout << "depth61 surviving right offsets in [0,RMAX]="
         << survivors.size() << "\n";
    cout << "first survivor=" << survivors.front().r
         << " last survivor=" << survivors.back().r << "\n";
    cout << "max candidate lifespan=" << exact_max
         << " at r=" << witness_r
         << " boundary=" << witness_b << "\n";
    cout << "states surviving through depth512=0\n";
    cout << "states reaching their halo-entry depth 3r+1=0\n";
    cout << "internal adjacent-block endpoint collision excluded through depth="
         << exclusion_depth << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
