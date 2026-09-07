// MATH-026: finite right-offset bootstrap using the exact MATH-025
// rolling 11-step operator.
//
// Scope:
//   0 <= r <= 200,000,000
//   N = b*2^61 + r, 1025 <= b <= 1363
//   coefficient-survival gate only
//   internal adjacent-block same-endpoint collision route from MATH-021
//
// Build:
//   g++ -O3 -std=c++17 -fopenmp \
//     2026_09_08_right_offset_rolling_bootstrap_200m_certificate.cpp -o cert
// Run:
//   OMP_NUM_THREADS=16 ./cert
//
// Expected output is embedded as assertions below.
// Finite/exact within scope. This is not a Collatz proof.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

struct Survivor {
    int r;
    u128 y;
    uint8_t q;
};

struct Tail11 {
    uint8_t s;
    uint64_t correction;
    array<uint8_t,12> prefix_odds;
};

int main() {
    const int RMAX = 200'000'000;
    const int KEND = 1029; // 61 + 88*11
    const int B0 = 1025, B1 = 1363;
    const int W = 11, MOD = 1 << W;

    // Exact coefficient thresholds. qpub implements the frozen theorem-facing
    // floor (3+2^-71)^q > 2^k; qmin is least q with 3^q >= 2^k.
    vector<int> qmin(KEND + 1), qpub(KEND + 1);
    cpp_int three = 1, two = 1;
    int qs = 0;
    const cpp_int B = cpp_int(1) << 71;
    const cpp_int A = 3*B + 1;
    cpp_int ap = 1, bp = 1;
    int qp = 0;

    for (int k = 1; k <= KEND; ++k) {
        two *= 2;
        while (three < two) { three *= 3; ++qs; }
        qmin[k] = qs;

        while (!(ap > two*bp)) {
            ap *= A;
            bp *= B;
            ++qp;
        }
        qpub[k] = qp;
        assert(qpub[k] == qmin[k]);
    }

    u128 pow3[80];
    pow3[0] = 1;
    for (int i = 1; i < 80; ++i) pow3[i] = pow3[i-1] * 3;

    // Exact 11-step residue descriptors.
    Tail11 desc[MOD];
    for (int u = 0; u < MOD; ++u) {
        uint64_t n = u;
        int s = 0;
        array<uint8_t,12> pref{};

        for (int j = 1; j <= W; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3*n + 1)/2; ++s; }
            else n /= 2;
            pref[j] = static_cast<uint8_t>(s);
        }

        const uint64_t c = uint64_t(MOD)*n
                         - uint64_t(pow3[s])*uint64_t(u);
        desc[u] = {static_cast<uint8_t>(s), c, pref};
    }

    // H[K][u] is needed only at rolling bases K=61 mod 11.
    vector<array<int16_t,MOD>> H(KEND + 1);
    for (int K = 61; K + W <= KEND; K += W) {
        for (int u = 0; u < MOD; ++u) {
            int h = INT_MIN;
            for (int j = 1; j <= W; ++j)
                h = max(h, qpub[K+j] - int(desc[u].prefix_odds[j]));
            H[K][u] = static_cast<int16_t>(h);
        }
    }

    // Stage 1: exact scalar filter through depth 61 for every right offset in
    // the finite domain.  The first 61 shortcut parities depend only on r.
    vector<Survivor> survivors;
    survivors.reserve(400'000);

    const int nt = omp_get_max_threads();
    vector<vector<Survivor>> local(nt);

    #pragma omp parallel
    {
        const int tid = omp_get_thread_num();
        local[tid].reserve(30'000);

        #pragma omp for schedule(static)
        for (int r = 0; r <= RMAX; ++r) {
            u128 n = static_cast<uint64_t>(r);
            int q = 0;
            bool ok = true;

            for (int k = 1; k <= 61; ++k) {
                const bool odd = (n & 1) != 0;
                if (odd) { n = (3*n + 1)/2; ++q; }
                else n /= 2;

                if (q < qmin[k]) { ok = false; break; }
            }

            if (ok)
                local[tid].push_back({r,n,static_cast<uint8_t>(q)});
        }
    }

    for (auto &v : local)
        survivors.insert(survivors.end(),
                         make_move_iterator(v.begin()),
                         make_move_iterator(v.end()));

    sort(survivors.begin(), survivors.end(),
         [](const Survivor &a, const Survivor &b){ return a.r < b.r; });

    // Stage 2: all 339 internal right-side labels, now advanced by the exact
    // MATH-025 11-step rolling operator rather than by scalar steps.
    atomic<long long> survive_to_end{0};
    atomic<int> deepest_failed_base{61};

    #pragma omp parallel for schedule(dynamic,8)
    for (int i = 0; i < static_cast<int>(survivors.size()); ++i) {
        const auto &s = survivors[i];

        for (int b = B0; b <= B1; ++b) {
            // Exact address lift from MATH-006/MATH-025 lineage.
            u128 n = s.y + u128(b)*pow3[s.q];
            int q = s.q;
            int K = 61;

            for (; K + W <= KEND; K += W) {
                const int u = int(n & (MOD-1));
                if (q < H[K][u]) break;

                const auto de = desc[u];
                q += de.s;

                // All states in this finite audit remain in u128.  Guard the
                // exact multiply-add before shifting by 11.
                const u128 UMAX = ~u128(0);
                assert(n <= (UMAX - de.correction)/pow3[de.s]);
                n = (pow3[de.s]*n + de.correction) >> W;
            }

            int old = deepest_failed_base.load();
            while (K > old &&
                   !deepest_failed_base.compare_exchange_weak(old,K)) {}

            if (K + W > KEND)
                survive_to_end.fetch_add(1);
        }
    }

    assert(survivors.size() == 358'907);
    assert(survivors.front().r == 703);
    assert(survivors.back().r == 199'999'983);
    assert(survive_to_end.load() == 0);
    assert(deepest_failed_base.load() == 501);

    // MATH-021: collision at depth k requires
    // r <= floor((k-1)/3).  Therefore the finite offset domain 0..RMAX covers
    // all possible right offsets through depth 3*RMAX+3.
    const long long exclusion_depth = 3LL*RMAX + 3;
    assert(exclusion_depth == 600'000'003LL);

    cout << "PASS\n";
    cout << "RMAX=" << RMAX << "\n";
    cout << "depth61 survivors=" << survivors.size()
         << " first=" << survivors.front().r
         << " last=" << survivors.back().r << "\n";
    cout << "states surviving all rolling windows through depth "
         << KEND << "=" << survive_to_end.load() << "\n";
    cout << "deepest failed rolling-window base depth="
         << deepest_failed_base.load() << "\n";
    cout << "internal adjacent-block same-endpoint coupling excluded through depth="
         << exclusion_depth << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
