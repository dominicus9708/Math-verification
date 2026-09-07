// MATH-027: exact bounded residue-lifting generator for depth-61
// coefficient-surviving right offsets.
//
// It reproduces the scalar stage-1 survivor vector without scanning every
// start independently through its prefix.  The exact lift relation is
//
//   if T^k(x)=y with q odd steps and x<2^k, then
//   T^k(x + e*2^k) = y + e*3^q,  e in {0,1}.
//
// Each binary lift is filtered immediately by the depth-(k+1) coefficient
// threshold, and branches exceeding RMAX are never created.
//
// The certificate compares the COMPLETE final vectors (r,T^61(r),q61)
// against an independent scalar scan for RMAX=1e8 and 2e8.
// Finite/exact within this validation scope.  Collatz remains open.

#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u128 = unsigned __int128;

struct State {
    uint32_t x;
    u128 y;
    uint8_t q;
};

static bool same_state(const State &a, const State &b) {
    return a.x == b.x && a.y == b.y && a.q == b.q;
}

struct LiftResult {
    vector<State> states;
    unsigned long long branch_attempts = 0;
    size_t peak_states = 0;
    int peak_depth = 0;
};

int main() {
    int qmin[62]{};
    u128 p3[62];
    p3[0] = 1;

    u128 three = 1, two = 1;
    int q = 0;
    for (int k = 1; k <= 61; ++k) {
        p3[k] = p3[k-1] * 3;
        two *= 2;
        while (three < two) { three *= 3; ++q; }
        qmin[k] = q;
    }

    auto scalar = [&](uint32_t RMAX,
                      unsigned long long &step_count) {
        const int nt = omp_get_max_threads();
        vector<vector<State>> local(nt);
        unsigned long long steps = 0;

        #pragma omp parallel reduction(+:steps)
        {
            const int tid = omp_get_thread_num();

            #pragma omp for schedule(static)
            for (uint64_t rr = 0; rr <= uint64_t(RMAX); ++rr) {
                u128 n = rr;
                int qq = 0;
                bool ok = true;

                for (int k = 1; k <= 61; ++k) {
                    ++steps;
                    const bool odd = (n & 1) != 0;
                    if (odd) { n = (3*n + 1)/2; ++qq; }
                    else n /= 2;

                    if (qq < qmin[k]) { ok = false; break; }
                }

                if (ok)
                    local[tid].push_back({uint32_t(rr), n, uint8_t(qq)});
            }
        }

        vector<State> out;
        for (auto &v : local)
            out.insert(out.end(),
                       make_move_iterator(v.begin()),
                       make_move_iterator(v.end()));

        sort(out.begin(), out.end(),
             [](const State &a, const State &b){ return a.x < b.x; });
        step_count = steps;
        return out;
    };

    auto lift = [&](uint32_t RMAX) {
        LiftResult R;
        vector<State> v{{0,0,0}};
        R.peak_states = 1;

        for (int k = 0; k < 61; ++k) {
            vector<State> nv;
            nv.reserve(v.size()*2);
            const uint64_t add = 1ULL << k;

            for (const auto &st : v) {
                // e=0 always remains inside the current finite bound.
                for (int e = 0; e <= 1; ++e) {
                    if (e && uint64_t(st.x) + add > RMAX) continue;
                    ++R.branch_attempts;

                    // Exact lift at depth k.
                    const u128 z = st.y + (e ? p3[st.q] : 0);
                    const int odd = int(z & 1);
                    const int q2 = int(st.q) + odd;
                    if (q2 < qmin[k+1]) continue;

                    const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                    const uint32_t x2 = st.x +
                        (e ? static_cast<uint32_t>(add) : 0u);

                    nv.push_back({x2,y2,uint8_t(q2)});
                }
            }

            v.swap(nv);
            if (v.size() > R.peak_states) {
                R.peak_states = v.size();
                R.peak_depth = k+1;
            }
        }

        sort(v.begin(), v.end(),
             [](const State &a, const State &b){ return a.x < b.x; });
        R.states = move(v);
        return R;
    };

    for (uint32_t RMAX : {100'000'000u, 200'000'000u}) {
        unsigned long long scalar_steps = 0;
        const auto S = scalar(RMAX, scalar_steps);
        const auto L = lift(RMAX);

        assert(S.size() == L.states.size());
        for (size_t i = 0; i < S.size(); ++i)
            assert(same_state(S[i], L.states[i]));

        if (RMAX == 100'000'000u) {
            assert(S.size() == 179'754);
            assert(S.front().x == 703);
            assert(S.back().x == 99'999'855);
            assert(scalar_steps == 345'676'746ULL);
            assert(L.branch_attempts == 23'802'595ULL);
            assert(L.peak_states == 1'312'797);
            assert(L.peak_depth == 27);
        } else {
            assert(S.size() == 358'907);
            assert(S.front().x == 703);
            assert(S.back().x == 199'999'983);
            assert(scalar_steps == 691'370'987ULL);
            assert(L.branch_attempts == 44'150'751ULL);
            assert(L.peak_states == 2'625'819);
            assert(L.peak_depth == 28);
        }

        cout << "RMAX=" << RMAX
             << " survivors=" << S.size()
             << " scalar_steps=" << scalar_steps
             << " lift_branch_attempts=" << L.branch_attempts
             << " peak_states=" << L.peak_states
             << " peak_depth=" << L.peak_depth
             << " exact_vector_match=YES\n";
    }

    cout << "VERDICT=CONFIRMED / EXACT BOUNDED GENERATOR / STAGE1 ACCELERATION\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
