#include <algorithm>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static constexpr u64 A = 114208327604ULL;
static constexpr u64 Q = 72057431991ULL;
static constexpr u64 P = A - Q;
static constexpr int K = 47;
static const u128 B = (u128)1 << 71;

static u64 gap_factor(u64 r, int L) {
    u64 bits = 0;
    for (int i = 0; i < L; ++i) {
        u128 a = (u128)r + (u128)(i + 1) * P;
        u128 b = (u128)r + (u128)i * P;
        int m = (u64)(a / Q) - (u64)(b / Q);
        if (m) bits |= (1ULL << i);
    }
    return bits;
}

static u64 parity_bits_from_gap(u64 gbits, int horizon) {
    u64 pb = 1ULL;  // the segment starts at an odd state
    int t = 0;
    for (int i = 0; i < horizon; ++i) {
        t += 1 + ((gbits >> i) & 1ULL);
        if (t >= horizon) break;
        pb |= (1ULL << t);
    }
    return pb;
}

static u64 inv_odd_mod2k(u64 a, int k) {
    // Newton inversion for an odd number modulo 2^64, then truncate.
    u64 x = 1;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x & ((1ULL << k) - 1);
}

static std::pair<u64, int> canonical_residue(u64 pb, int k) {
    const u64 mask = (1ULL << k) - 1;
    u64 R = 0;
    int q = 0;
    for (int i = 0; i < k; ++i) {
        if ((pb >> i) & 1ULL) {
            R = (3 * R + (1ULL << i)) & mask;
            ++q;
        }
    }
    u64 p3 = 1;
    for (int i = 0; i < q; ++i) p3 *= 3;
    p3 &= mask;
    u64 inv = inv_odd_mod2k(p3, k);
    u64 rho = (0ULL - R) * inv;
    rho &= mask;
    return {rho, q};
}

static inline bool reaches_below_B(u128 n, int& steps) {
    u128 x = n;
    for (int s = 0; s < 5000; ++s) {
        if (x < B) {
            steps = s;
            return true;
        }
        if ((x & 1) == 0) {
            x >>= 1;
        } else {
            // Guard the exact 128-bit arithmetic.  It is never approached by
            // the certified candidate set.
            if (x > ((~(u128)0) - 1) / 3) return false;
            x = (3 * x + 1) >> 1;
        }
    }
    return false;
}

int main() {
    // A length-K rational mechanical gap factor changes only when the phase
    // residue crosses one of the K+1 exact breakpoints -kP mod Q.
    std::vector<u64> breaks;
    for (int k = 0; k <= K; ++k)
        breaks.push_back((Q - (u64)(((u128)k * P) % Q)) % Q);
    std::sort(breaks.begin(), breaks.end());
    breaks.erase(std::unique(breaks.begin(), breaks.end()), breaks.end());

    std::set<u64> gap_factors;
    for (u64 b : breaks) {
        gap_factors.insert(gap_factor(b, K));
        gap_factors.insert(gap_factor((b + 1) % Q, K));
        gap_factors.insert(gap_factor((b + Q - 1) % Q, K));
    }
    assert(gap_factors.size() == 48);

    // Different gap factors can give the same K-time parity factor because the
    // last unused mechanical gap may lie beyond the time horizon.
    std::set<u64> parity_set;
    for (u64 f : gap_factors)
        parity_set.insert(parity_bits_from_gap(f, K));
    assert(parity_set.size() == 30);

    std::vector<u64> parity_factors(parity_set.begin(), parity_set.end());
    const u128 M = (u128)1 << K;

    unsigned long long candidates = 0;
    int global_max_steps = 0;
    std::atomic<bool> failed(false);

    // A d=0 odd state satisfies N<x<2N and the first-resonance start bound
    // N<(4/3)2^71, hence B<x<(8/3)B.  Enumerate every integer in that shell
    // having one of the 30 canonical K-bit factors.
#pragma omp parallel for schedule(dynamic) reduction(+:candidates) reduction(max:global_max_steps)
    for (int ii = 0; ii < (int)parity_factors.size(); ++ii) {
        auto [rho, q] = canonical_residue(parity_factors[ii], K);
        (void)q;
        const u128 r = rho;

        u128 tmin = 0;
        if (B >= r) tmin = (B - r) / M + 1;
        const u128 upper_num = 8 * B - 1;  // strict 3x<8B
        if (upper_num < 3 * r) continue;
        const u128 tmax128 = (upper_num - 3 * r) / (3 * M);

        const u64 lo = (u64)tmin;
        const u64 hi = (u64)tmax128;
        for (u64 t = lo; t <= hi; ++t) {
            const u128 x = r + (u128)t * M;
            if (!(B < x && 3 * x < 8 * B)) continue;
            ++candidates;

            int steps = 0;
            if (!reaches_below_B(x, steps)) {
                failed.store(true, std::memory_order_relaxed);
                break;
            }
            global_max_steps = std::max(global_max_steps, steps);
            if (t == hi) break;
        }
    }

    assert(!failed.load());
    assert(candidates == 838860804ULL);
    assert(global_max_steps == 461);

    // 30 mechanical gaps always span at least floor(30*A/Q)=47 time steps.
    // Hence 31 consecutive d=0 odd states determine one of the certified
    // length-47 parity factors, which is impossible on a counterexample orbit.
    assert((30ULL * A) / Q == 47ULL);

    // If a length-Q displacement sequence has no run of 31 zeros, then with r
    // positive positions its Q-r zeros occupy at most r+1 runs of length 30:
    // Q-r <= 30(r+1).  Thus r >= ceil((Q-30)/31).
    const u64 rmin = (Q - 30 + 30) / 31;
    assert(rmin == 2324433290ULL);

    std::cout << "PASS first-resonance base-shell factor-47 exclusion\n";
    std::cout << "gap_factors=" << gap_factors.size() << "\n";
    std::cout << "odd_start_parity_factors=" << parity_factors.size() << "\n";
    std::cout << "shell_candidates=" << candidates << "\n";
    std::cout << "max_accelerated_steps_to_below_2^71=" << global_max_steps << "\n";
    std::cout << "no_31_consecutive_d0_odd_states\n";
    std::cout << "displaced_ordinals_at_least=" << rmin << "\n";
    std::cout << "coarse_normalized_defect_gt=" << (long double)rmin / 12.0L << "\n";
}
