// MATH-028: combined exact bounded residue lifting + rolling 11-step
// continuation for the right-offset domain 0 <= r <= 1,000,000,000.
//
// Stage 1 uses MATH-027 exact bounded binary lifting to depth 61.
// Stage 2 uses MATH-025 exact 11-step rolling continuation through all 339
// internal right-side address labels.
// MATH-021 converts the finite offset domain into an internal same-endpoint
// collision-exclusion depth.
//
// Build:
//   g++ -O3 -std=c++17 -fopenmp \
//     2026_09_08_combined_lifting_rolling_bootstrap_1b_certificate.cpp -o cert
// Run:
//   OMP_NUM_THREADS=16 ./cert
//
// Finite/exact within the stated mechanism.  This is not a Collatz proof.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u128 = unsigned __int128;
using boost::multiprecision::cpp_int;

struct State {
    uint32_t r;
    u128 y;
    uint8_t q;
};

struct Tail11 {
    uint8_t s;
    uint64_t correction;
    array<uint8_t,12> prefix_odds;
};

int main() {
    const uint32_t RMAX = 1'000'000'000u;
    const int KEND = 1029;
    const int W = 11, MOD = 1 << W;
    const int B0 = 1025, B1 = 1363;

    // Thresholds are constructed with arbitrary-precision integers.
    // qpub is the frozen theorem-facing floor (3+2^-71)^q > 2^k;
    // qmin is least q with 3^q >= 2^k. They must agree throughout the
    // finite continuation range used by this certificate.
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

    u128 pow3[62];
    pow3[0] = 1;
    for (int i = 1; i < 62; ++i) pow3[i] = pow3[i-1]*3;

    Tail11 desc[MOD];
    for (int u = 0; u < MOD; ++u) {
        uint64_t n = u;
        int s = 0;
        array<uint8_t,12> pref{};

        for (int j = 1; j <= W; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3*n + 1)/2; ++s; }
            else n /= 2;
            pref[j] = uint8_t(s);
        }

        const uint64_t c = uint64_t(MOD)*n
                         - uint64_t(pow3[s])*uint64_t(u);
        desc[u] = {uint8_t(s), c, pref};
    }

    vector<array<int16_t,MOD>> H(KEND + 1);
    for (int K = 61; K + W <= KEND; K += W) {
        for (int u = 0; u < MOD; ++u) {
            int h = INT_MIN;
            for (int j = 1; j <= W; ++j)
                h = max(h, qpub[K+j] - int(desc[u].prefix_odds[j]));
            H[K][u] = int16_t(h);
        }
    }

    // Stage 1: MATH-027 exact bounded residue lifting.
    vector<State> states{{0,0,0}};
    unsigned long long branch_attempts = 0;
    size_t peak_states = 1;
    int peak_depth = 0;

    for (int k = 0; k < 61; ++k) {
        vector<State> next;
        next.reserve(states.size()*2);
        const uint64_t add = 1ULL << k;

        for (const auto &st : states) {
            for (int e = 0; e <= 1; ++e) {
                if (e && uint64_t(st.r) + add > RMAX) continue;
                ++branch_attempts;

                // Exact binary lift:
                // T^k(x+e2^k)=T^k(x)+e3^q.
                const u128 z = st.y + (e ? pow3[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qpub[k+1]) continue;

                const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                const uint32_t r2 = st.r +
                    (e ? static_cast<uint32_t>(add) : 0u);
                next.push_back({r2,y2,uint8_t(q2)});
            }
        }

        states.swap(next);
        if (states.size() > peak_states) {
            peak_states = states.size();
            peak_depth = k+1;
        }
    }

    sort(states.begin(), states.end(),
         [](const State &a, const State &b){ return a.r < b.r; });

    assert(states.size() == 1'796'718);
    assert(states.front().r == 703);
    assert(states.back().r == 999'999'207);
    assert(branch_attempts == 187'063'991ULL);
    assert(peak_states == 11'894'128);
    assert(peak_depth == 30);

    // Stage 2: MATH-025 exact rolling continuation over all 339 internal
    // right-side address labels.
    atomic<long long> survive_to_end{0};
    atomic<long long> overflow{0};
    atomic<int> deepest_failed_base{61};
    atomic<unsigned long long> max_witness{~0ULL};

    #pragma omp parallel for schedule(dynamic,4)
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        const auto st = states[i];

        for (int b = B0; b <= B1; ++b) {
            u128 n = st.y + u128(b)*pow3[st.q];
            int q = st.q;
            int K = 61;
            bool ov = false;

            for (; K + W <= KEND; K += W) {
                const int u = int(n & (MOD-1));
                if (q < H[K][u]) break;

                const auto de = desc[u];
                q += de.s;

                const u128 UMAX = ~u128(0);
                if (n > (UMAX - de.correction)/pow3[de.s]) {
                    ov = true;
                    overflow.fetch_add(1);
                    break;
                }
                n = (pow3[de.s]*n + de.correction) >> W;
            }

            if (!ov) {
                int old = deepest_failed_base.load();
                while (K > old &&
                       !deepest_failed_base.compare_exchange_weak(old,K)) {}

                if (K == 545) {
                    const unsigned long long packed =
                        (static_cast<unsigned long long>(st.r) << 16)
                        | static_cast<unsigned long long>(b);
                    auto cur = max_witness.load();
                    while (packed < cur &&
                           !max_witness.compare_exchange_weak(cur,packed)) {}
                }

                if (K + W > KEND)
                    survive_to_end.fetch_add(1);
            }
        }
    }

    assert(overflow.load() == 0);
    assert(survive_to_end.load() == 0);
    assert(deepest_failed_base.load() == 545);
    assert((max_witness.load() >> 16) == 378'620'799ULL);
    assert((max_witness.load() & 0xffffULL) == 1183ULL);

    // MATH-021: collision at depth k requires
    // r <= floor((k-1)/3). Therefore all possible relevant right offsets
    // through 3*RMAX+3 lie inside this finite domain.
    const long long exclusion_depth = 3LL*RMAX + 3;
    assert(exclusion_depth == 3'000'000'003LL);

    cout << "PASS\n";
    cout << "RMAX=" << RMAX << "\n";
    cout << "depth61 survivors=" << states.size()
         << " first=" << states.front().r
         << " last=" << states.back().r << "\n";
    cout << "lift branch attempts=" << branch_attempts
         << " peak states=" << peak_states
         << " at depth=" << peak_depth << "\n";
    cout << "states surviving all rolling windows through depth "
         << KEND << "=" << survive_to_end.load() << "\n";
    cout << "deepest failing-window base=" << deepest_failed_base.load()
         << " witness r=" << (max_witness.load() >> 16)
         << " b=" << (max_witness.load() & 0xffffULL) << "\n";
    cout << "internal adjacent-block same-endpoint coupling excluded through depth="
         << exclusion_depth << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
