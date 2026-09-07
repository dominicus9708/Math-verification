// MATH-024: exact finite right-offset lifespan/dominance audit on 0 <= r <= 1e8.
//
// Scope:
//   N = b*2^61 + r, 1025 <= b <= 1363,
//   coefficient-survival gate through the stated depth,
//   internal adjacent-block same-endpoint collision route from MATH-021.
//
// Build:
//   g++ -O3 -std=c++17 -fopenmp \
//     2026_09_08_right_offset_lifespan_dominance_100m_certificate.cpp -o cert
// Run:
//   OMP_NUM_THREADS=16 ./cert
//
// Finite/exact only. This is not a proof of the Collatz conjecture.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using boost::multiprecision::cpp_int;

struct S { int r; cpp_int y; int q; };

int main() {
    const int RMAX = 100'000'000;
    const int KCAP = 700;
    const int B0 = 1025, B1 = 1363;

    // qmin[k]: least q with 3^q >= 2^k.
    // qpub[k]: strict frozen-floor coefficient threshold
    //           (3 + 2^-71)^q > 2^k.
    // They are required to agree on the whole continuation range used here.
    vector<int> qmin(KCAP + 1), qpub(KCAP + 1);
    cpp_int p3 = 1, two = 1;
    int qq = 0;
    const cpp_int B = cpp_int(1) << 71;
    const cpp_int A = 3 * B + 1;
    cpp_int ap = 1, bp = 1;
    int qp = 0;

    for (int k = 1; k <= KCAP; ++k) {
        two *= 2;
        while (p3 < two) { p3 *= 3; ++qq; }
        qmin[k] = qq;

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

    // Stage 1: exhaustive depth-61 filter of every nonnegative right offset
    // in the finite domain. The first 61 parity steps depend only on r.
    vector<S> survivors;
    survivors.reserve(200'000);

    const int nt = omp_get_max_threads();
    vector<vector<S>> local(nt);

    #pragma omp parallel
    {
        const int tid = omp_get_thread_num();
        local[tid].reserve(25'000);

        #pragma omp for schedule(static)
        for (int r = 0; r <= RMAX; ++r) {
            unsigned long long n = static_cast<unsigned long long>(r);
            int q = 0;
            bool ok = true;

            for (int k = 1; k <= 61; ++k) {
                const bool odd = (n & 1ULL) != 0;
                if (odd) {
                    const __uint128_t z = (__uint128_t)3 * n + 1;
                    n = static_cast<unsigned long long>(z / 2);
                    ++q;
                } else {
                    n /= 2;
                }
                if (q < qmin[k]) { ok = false; break; }
            }

            if (ok) local[tid].push_back({r, cpp_int(n), q});
        }
    }

    for (auto &v : local)
        survivors.insert(survivors.end(),
                         make_move_iterator(v.begin()),
                         make_move_iterator(v.end()));

    sort(survivors.begin(), survivors.end(),
         [](const S &a, const S &b) { return a.r < b.r; });

    // Stage 2: continue every surviving lower-61 state through all 339
    // internal right-side block labels.
    // Exact affine lift:
    //   T^61(b*2^61+r) = T^61(r) + b*3^q.
    vector<int> maxlife(survivors.size(), 61);
    vector<int> argb(survivors.size(), -1);

    #pragma omp parallel for schedule(dynamic, 8)
    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        const auto &s = survivors[i];
        int best = 61, best_b = -1;

        for (int b = B0; b <= B1; ++b) {
            cpp_int n = s.y + cpp_int(b) * pow3[s.q];
            int q = s.q;
            int L = 61;

            for (int k = 62; k <= KCAP; ++k) {
                const bool odd = (n & 1) != 0;
                if (odd) { n = (3 * n + 1) / 2; ++q; }
                else n /= 2;

                if (q < qmin[k]) { L = k - 1; break; }
                L = k;
            }

            if (L > best) { best = L; best_b = b; }
        }

        maxlife[i] = best;
        argb[i] = best_b;
    }

    int global_max = 0, witness_r = -1, witness_b = -1;
    int unresolved = 0, halo_entry_violation = 0;
    vector<int> rmin(KCAP + 1, INT_MAX);

    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        if (maxlife[i] > global_max) {
            global_max = maxlife[i];
            witness_r = survivors[i].r;
            witness_b = argb[i];
        }
        if (maxlife[i] >= KCAP) ++unresolved;
        if ((long long)maxlife[i] >= 3LL * survivors[i].r + 1)
            ++halo_entry_violation;

        for (int k = 61; k <= maxlife[i] && k <= KCAP; ++k)
            rmin[k] = min(rmin[k], survivors[i].r);
    }

    assert(survivors.size() == 179'754);
    assert(survivors.front().r == 703);
    assert(survivors.back().r == 99'999'855);
    assert(global_max == 504);
    assert(witness_r == 31'595'291);
    assert(witness_b == 1218);
    assert(unresolved == 0);
    assert(halo_entry_violation == 0);

    // Running-max/Pareto dominance frontier.
    // If record i is (r_i,L_i), every later survivor until the next record
    // has r >= r_i and lifespan <= L_i. Therefore L_i < 3 r_i + 1
    // certifies the whole record interval against halo entry.
    vector<array<int,4>> records;
    int running = -1;
    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        if (maxlife[i] > running) {
            running = maxlife[i];
            records.push_back({survivors[i].r, maxlife[i], argb[i], survivors[i].q});
        }
    }

    const vector<array<int,4>> expected = {
        {703,161,1147,42},
        {1055,182,1055,42},
        {1407,194,1264,41},
        {1583,199,1087,42},
        {6383,226,1243,42},
        {17023,245,1263,42},
        {18599,305,1229,41},
        {106239,345,1328,41},
        {276199,429,1177,42},
        {11991359,439,1144,43},
        {27454695,440,1152,45},
        {29660287,462,1306,42},
        {31595291,504,1218,42}
    };
    assert(records == expected);

    for (const auto &a : records)
        assert(a[1] < 3LL * a[0] + 1);

    // MATH-021 collision-complete halo: at depth k, right offset must satisfy
    // r <= floor((k-1)/3). Therefore all k <= 3*RMAX+3 are covered by the
    // finite offset domain audited here.
    const long long exclusion_depth = 3LL * RMAX + 3;
    assert(exclusion_depth == 300'000'003LL);

    int first_rmin_le_halo = -1;
    for (int k = 61; k <= KCAP; ++k) {
        if (rmin[k] != INT_MAX && rmin[k] <= (k - 1) / 3) {
            first_rmin_le_halo = k;
            break;
        }
    }
    assert(first_rmin_le_halo == -1);

    cout << "PASS\n";
    cout << "RMAX=" << RMAX << "\n";
    cout << "published-floor q_min == 3^q threshold for depths 1.." << KCAP << "\n";
    cout << "depth61 survivors=" << survivors.size() << " first="
         << survivors.front().r << " last=" << survivors.back().r << "\n";
    cout << "global max lifespan=" << global_max << " at r=" << witness_r
         << " boundary=" << witness_b << "\n";
    cout << "halo-entry violations=" << halo_entry_violation << "\n";
    cout << "dominance records=" << records.size() << "\n";
    for (const auto &a : records)
        cout << a[0] << " " << a[1] << " " << a[2] << " " << a[3] << "\n";
    cout << "internal adjacent-block endpoint collision excluded through depth="
         << exclusion_depth << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
