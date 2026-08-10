#include <algorithm>
#include <climits>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

// Integrated exact audit for the DSD-style Collatz state/dynamics formulation.
// Accelerated map:
//   T(n)=n/2       (n even)
//   T(n)=(3n+1)/2  (n odd)
//
// At depth k a coefficient-surviving canonical state is represented by
//   (r, y, q),
// with v=2^k, u=3^q and correction numerator R defined by
//   v*y = u*r + R.
//
// A requested next parity p in {0,1} fixes the canonical lift bit
//   c = p XOR (y mod 2),
// then
//   r'       = r + c*v,
//   y_tilde  = y + c*u,
//   y'       = (3^p*y_tilde + p)/2,
//   q'       = q+p,
//   R'       = 3^p R + p*v.
//
// The code verifies this exact closure before applying the coefficient-survival
// admissibility filter 3^q >= 2^k. It also checks the block lift identity
//   T^k(r + 2^k) = y + 3^q
// on deterministic samples.
//
// For equal-depth endpoint collisions it stores the ACTUAL lifted predecessor
// y_tilde. A pair is a true first merge iff the common current endpoint y is
// equal but the two actual predecessors differ. For Delta q = 1 it audits
//   G = r_L - 3 r_H = (R_H-R_L)/3^q,
// and records whether the bad merge region G<0 is reachable.

struct State {
    u64 y = 0;
    u64 r = 0;
    u64 pre = 0;   // actual lifted predecessor immediately before last branch
    std::uint8_t q = 0;
    std::uint8_t p = 0; // last parity branch
};

static bool fits_u64(u128 x) {
    return x <= static_cast<u128>(UINT64_MAX);
}

static u128 direct_accelerated(u128 x, int k) {
    for (int i = 0; i < k; ++i) {
        if (x & 1) x = (3*x + 1) >> 1;
        else x >>= 1;
    }
    return x;
}

int main(int argc, char** argv) {
    const int K = (argc >= 2 ? std::stoi(argv[1]) : 28);
    const std::size_t block_samples =
        (argc >= 3 ? static_cast<std::size_t>(std::stoull(argv[2])) : 1024);

    // Flat exact enumeration becomes memory-intensive above the low 30s.
    if (K < 1 || K > 39) {
        std::cerr << "K must satisfy 1 <= K <= 39\n";
        return 1;
    }

    std::vector<u64> pow2(K + 2), pow3(K + 2);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K + 1; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::vector<State> current{{0,0,0,0,0}};

    std::map<int,u64> dq_hist;
    std::map<long long,u64> g_hist;
    std::map<long long,u64> g_type_a;
    std::map<long long,u64> g_type_b;

    u64 cumulative_survivor_transitions = 0;
    u64 cumulative_transition_checks = 0;
    u64 cumulative_true_merges = 0;
    u64 cumulative_dq1 = 0;
    u64 cumulative_bad_g = 0;
    u64 cumulative_block_samples = 0;

    std::cout
        << "k,survivors,closure_fail,transition_checked,transition_fail,"
           "block_samples,block_fail,endpoint_classes,collision_classes,max_endpoint_class,"
           "true_merge_pairs,dq0_pairs,dq1_pairs,"
           "bad_G,typeA,typeB,G2,G6,G10,G_other_pos,dq_gt1,max_dq\n";

    for (int k = 0; k < K; ++k) {
        const u64 v = pow2[k];
        std::vector<State> next;
        next.reserve(current.size() * 2);

        u64 closure_fail = 0;
        u64 transition_checked = 0;
        u64 transition_fail = 0;

        for (const State& s : current) {
            const u64 u = pow3[s.q];
            const u128 lhs_parent = static_cast<u128>(v) * s.y;
            const u128 ur = static_cast<u128>(u) * s.r;
            if (lhs_parent < ur) {
                ++closure_fail;
                continue;
            }
            const u128 R = lhs_parent - ur;

            for (int p = 0; p <= 1; ++p) {
                ++transition_checked;
                const int c = p ^ static_cast<int>(s.y & 1ULL);

                const u128 r2x = static_cast<u128>(s.r) + (c ? v : 0);
                const u128 prex = static_cast<u128>(s.y) + (c ? u : 0);
                const u128 y2x = p ? (3*prex + 1)/2 : prex/2;
                const int q2 = static_cast<int>(s.q) + p;
                const u128 R2 = p ? 3*R + v : R;

                if (!fits_u64(r2x) || !fits_u64(prex) || !fits_u64(y2x)) {
                    std::cerr << "uint64 state overflow at depth " << (k+1) << '\n';
                    return 2;
                }

                const u64 r2 = static_cast<u64>(r2x);
                const u64 pre = static_cast<u64>(prex);
                const u64 y2 = static_cast<u64>(y2x);

                const u128 lhs = static_cast<u128>(pow2[k+1]) * y2;
                const u128 rhs = static_cast<u128>(pow3[q2]) * r2 + R2;
                if (lhs != rhs) {
                    ++transition_fail;
                    continue;
                }

                // Coefficient-survival admissibility at the new depth.
                if (pow3[q2] >= pow2[k+1]) {
                    next.push_back(State{y2,r2,pre,
                                         static_cast<std::uint8_t>(q2),
                                         static_cast<std::uint8_t>(p)});
                }
            }
        }

        current.swap(next);
        cumulative_survivor_transitions += current.size();
        cumulative_transition_checks += transition_checked;

        std::sort(current.begin(), current.end(), [](const State& a, const State& b) {
            if (a.y != b.y) return a.y < b.y;
            if (a.q != b.q) return a.q < b.q;
            if (a.r != b.r) return a.r < b.r;
            if (a.pre != b.pre) return a.pre < b.pre;
            return a.p < b.p;
        });

        // Deterministic block-lift cross-check on the first states after sorting.
        const std::size_t nsamp = std::min(block_samples, current.size());
        u64 block_fail = 0;
        for (std::size_t i = 0; i < nsamp; ++i) {
            const State& s = current[i];
            const u128 lifted_start = static_cast<u128>(s.r) + pow2[k+1];
            const u128 got = direct_accelerated(lifted_start, k+1);
            const u128 want = static_cast<u128>(s.y) + pow3[s.q];
            if (got != want) ++block_fail;
        }
        cumulative_block_samples += nsamp;

        u64 endpoint_classes=0, collision_classes=0, max_endpoint_class=0;
        u64 true_pairs=0, dq0=0, dq1=0, bad_g=0;
        u64 type_a=0, type_b=0, G2=0, G6=0, G10=0, Gother=0, dq_gt1=0;
        int max_dq=0;

        for (std::size_t s = 0; s < current.size();) {
            std::size_t e = s + 1;
            while (e < current.size() && current[e].y == current[s].y) ++e;

            ++endpoint_classes;
            const u64 class_size = static_cast<u64>(e-s);
            if (class_size > 1) ++collision_classes;
            max_endpoint_class = std::max(max_endpoint_class, class_size);

            for (std::size_t i = s; i < e; ++i) {
                for (std::size_t j = i + 1; j < e; ++j) {
                    // Same actual predecessor means the pair was already merged.
                    if (current[i].pre == current[j].pre) continue;
                    ++true_pairs;

                    const int d = std::abs(static_cast<int>(current[i].q) -
                                           static_cast<int>(current[j].q));
                    ++dq_hist[d];
                    max_dq = std::max(max_dq, d);
                    if (d == 0) { ++dq0; continue; }
                    if (d > 1) { ++dq_gt1; continue; }

                    ++dq1;
                    const State* lo = &current[i];
                    const State* hi = &current[j];
                    if (lo->q > hi->q) std::swap(lo, hi);

                    const i128 G = static_cast<i128>(lo->r) -
                                   static_cast<i128>(3) * hi->r;
                    if (G >= LLONG_MIN && G <= LLONG_MAX) {
                        ++g_hist[static_cast<long long>(G)];
                    }

                    if (G < 0) ++bad_g;
                    else if (G == 2) ++G2;
                    else if (G == 6) ++G6;
                    else if (G == 10) ++G10;
                    else ++Gother;

                    const int pH = hi->p;
                    const int pL = lo->p;
                    const int dprev =
                        (static_cast<int>(hi->q) - pH) -
                        (static_cast<int>(lo->q) - pL);

                    if (pH == 1 && pL == 0 && dprev == 0) {
                        ++type_a;
                        if (G >= LLONG_MIN && G <= LLONG_MAX)
                            ++g_type_a[static_cast<long long>(G)];
                    } else if (pH == 0 && pL == 1 && dprev == 2) {
                        ++type_b;
                        if (G >= LLONG_MIN && G <= LLONG_MAX)
                            ++g_type_b[static_cast<long long>(G)];
                    } else {
                        std::cerr << "Delta-q=1 last-step classification failure at depth "
                                  << (k+1) << '\n';
                        return 3;
                    }
                }
            }
            s = e;
        }

        cumulative_true_merges += true_pairs;
        cumulative_dq1 += dq1;
        cumulative_bad_g += bad_g;

        std::cout << (k+1) << ',' << current.size() << ',' << closure_fail << ','
                  << transition_checked << ',' << transition_fail << ','
                  << nsamp << ',' << block_fail << ',' << endpoint_classes << ','
                  << collision_classes << ',' << max_endpoint_class << ',' << true_pairs << ','
                  << dq0 << ',' << dq1 << ',' << bad_g << ',' << type_a << ','
                  << type_b << ',' << G2 << ',' << G6 << ',' << G10 << ','
                  << Gother << ',' << dq_gt1 << ',' << max_dq << '\n';
    }

    std::cerr << "SUMMARY survivor_transitions=" << cumulative_survivor_transitions
              << " transition_checks=" << cumulative_transition_checks
              << " block_samples=" << cumulative_block_samples
              << " true_merges=" << cumulative_true_merges
              << " dq1=" << cumulative_dq1
              << " bad_G=" << cumulative_bad_g << '\n';

    std::cerr << "DQ_HIST";
    for (const auto& kv : dq_hist) std::cerr << " d" << kv.first << '=' << kv.second;
    std::cerr << '\n';

    std::cerr << "G_HIST";
    for (const auto& kv : g_hist) std::cerr << " G" << kv.first << '=' << kv.second;
    std::cerr << '\n';

    std::cerr << "TYPE_A_G_HIST";
    for (const auto& kv : g_type_a) std::cerr << " G" << kv.first << '=' << kv.second;
    std::cerr << '\n';

    std::cerr << "TYPE_B_G_HIST";
    for (const auto& kv : g_type_b) std::cerr << " G" << kv.first << '=' << kv.second;
    std::cerr << '\n';

    return 0;
}
