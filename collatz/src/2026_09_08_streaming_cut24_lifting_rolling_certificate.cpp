// MATH-029: exact streaming reordering of the MATH-028 combined engine.
//
// Instead of retaining the full breadth-first lift frontier up to its depth-30
// peak, build only the exact depth-24 frontier.  Each frontier state is then
// expanded by a local DFS to depth 61; every surviving leaf is consumed
// immediately by the exact address lift + MATH-025 rolling continuation.
//
// This changes enumeration order only.  No mathematical state is merged.
// The certificate reproduces the complete MATH-028 finite outputs at RMAX=1e9.

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
    uint8_t k;
};

struct Tail11 {
    uint8_t s;
    uint64_t correction;
    array<uint8_t,12> prefix_odds;
};

int main() {
    const uint32_t RMAX = 1'000'000'000u;
    const int CUT = 24;
    const int KEND = 1029;
    const int W = 11, MOD = 1 << W;
    const int B0 = 1025, B1 = 1363;

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
        while (!(ap > two*bp)) { ap *= A; bp *= B; ++qp; }
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
        desc[u] = {uint8_t(s),c,pref};
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

    // Phase A: exact breadth-first frontier only through CUT=24.
    vector<State> frontier{{0,0,0,0}};
    unsigned long long frontier_attempts = 0;

    for (int k = 0; k < CUT; ++k) {
        vector<State> next;
        next.reserve(frontier.size()*2);
        const uint64_t add = 1ULL << k;

        for (const auto &st : frontier) {
            for (int e = 0; e <= 1; ++e) {
                if (e && uint64_t(st.r) + add > RMAX) continue;
                ++frontier_attempts;

                const u128 z = st.y + (e ? pow3[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qpub[k+1]) continue;

                const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                const uint32_t r2 = st.r +
                    (e ? static_cast<uint32_t>(add) : 0u);
                next.push_back({r2,y2,uint8_t(q2),uint8_t(k+1)});
            }
        }
        frontier.swap(next);
    }

    assert(frontier.size() == 286'581);
    assert(frontier_attempts == 735'398ULL);

    // Phase B: each frontier state is expanded by local DFS.  Depth-61 leaves
    // are immediately consumed by all 339 address labels and rolling windows.
    atomic<unsigned long long> tail_attempts{0};
    atomic<unsigned long long> leaves{0};
    atomic<uint32_t> min_r{UINT32_MAX}, max_r{0};
    atomic<size_t> max_local_stack{0};
    atomic<long long> survive_to_end{0}, overflow{0};
    atomic<int> deepest_failed_base{61};
    atomic<unsigned long long> max_witness{~0ULL};

    #pragma omp parallel for schedule(dynamic,1)
    for (int fi = 0; fi < static_cast<int>(frontier.size()); ++fi) {
        vector<State> stack;
        stack.reserve(128);
        stack.push_back(frontier[fi]);
        size_t local_stack_max = 1;

        while (!stack.empty()) {
            const State st = stack.back();
            stack.pop_back();
            const int k = st.k;

            if (k == 61) {
                leaves.fetch_add(1);

                auto lo = min_r.load();
                while (st.r < lo && !min_r.compare_exchange_weak(lo,st.r)) {}
                auto hi = max_r.load();
                while (st.r > hi && !max_r.compare_exchange_weak(hi,st.r)) {}

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
                continue;
            }

            const uint64_t add = 1ULL << k;
            // Push high then low so the local DFS visits low first.
            for (int e = 1; e >= 0; --e) {
                if (e && uint64_t(st.r) + add > RMAX) continue;
                tail_attempts.fetch_add(1);

                const u128 z = st.y + (e ? pow3[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qpub[k+1]) continue;

                const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                const uint32_t r2 = st.r +
                    (e ? static_cast<uint32_t>(add) : 0u);
                stack.push_back({r2,y2,uint8_t(q2),uint8_t(k+1)});
            }
            local_stack_max = max(local_stack_max, stack.size());
        }

        auto old = max_local_stack.load();
        while (local_stack_max > old &&
               !max_local_stack.compare_exchange_weak(old,local_stack_max)) {}
    }

    assert(tail_attempts.load() == 186'328'593ULL);
    assert(frontier_attempts + tail_attempts.load() == 187'063'991ULL);
    assert(leaves.load() == 1'796'718ULL);
    assert(min_r.load() == 703);
    assert(max_r.load() == 999'999'207);
    assert(max_local_stack.load() == 7);
    assert(overflow.load() == 0);
    assert(survive_to_end.load() == 0);
    assert(deepest_failed_base.load() == 545);
    assert((max_witness.load() >> 16) == 378'620'799ULL);
    assert((max_witness.load() & 0xffffULL) == 1183ULL);

    // MATH-028 breadth-first peak was 11,894,128 live prefix states.
    // The streaming algorithm stores the 286,581-state cut frontier plus only
    // a small DFS stack per worker.  With 16 workers and the audited max stack
    // of 7, this is 286,693 algorithmic prefix states versus 11,894,128.
    const unsigned long long live16 = frontier.size() + 16ULL*max_local_stack.load();
    assert(live16 == 286'693ULL);

    cout << "PASS\n";
    cout << "cut frontier=" << frontier.size()
         << " frontier attempts=" << frontier_attempts << "\n";
    cout << "tail attempts=" << tail_attempts.load()
         << " total attempts=" << frontier_attempts + tail_attempts.load() << "\n";
    cout << "depth61 leaves=" << leaves.load()
         << " first=" << min_r.load()
         << " last=" << max_r.load() << "\n";
    cout << "max local DFS stack=" << max_local_stack.load() << "\n";
    cout << "16-worker algorithmic live-prefix states=" << live16 << "\n";
    cout << "MATH-028 breadth-first peak states=11894128\n";
    cout << "deepest failing base=" << deepest_failed_base.load()
         << " witness r=" << (max_witness.load() >> 16)
         << " b=" << (max_witness.load() & 0xffffULL) << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
