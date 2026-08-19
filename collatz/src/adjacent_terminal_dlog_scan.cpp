#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;
using i128 = __int128;

static inline u64 mulmod(u64 a, u64 b, u64 m) {
    return (u128)a * b % m;
}

static u64 powmod(u64 a, u64 e, u64 m) {
    u64 r = 1;
    while (e) {
        if (e & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        e >>= 1;
    }
    return r;
}

static long long egcd(long long a, long long b, long long& x, long long& y) {
    if (!b) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    const auto g = egcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return g;
}

static u64 invmod(u64 a, u64 m) {
    long long x, y;
    if (egcd((long long)a, (long long)m, x, y) != 1) std::exit(2);
    x %= (long long)m;
    if (x < 0) x += m;
    return (u64)x;
}

// Exact base-two discrete logarithm modulo 3^30.
// Low exponent: full table modulo 3^16.
// High 14 ternary exponent digits: one linear lift, since (3^16)^2=0 mod 3^30.
struct DL30 {
    static constexpr u64 M16 = 43046721ULL;          // 3^16
    static constexpr u64 O16 = 28697814ULL;          // 2*3^15
    static constexpr u64 H   = 4782969ULL;           // 3^14
    static constexpr u64 M30 = 205891132094649ULL;   // 3^30
    static constexpr u64 O30 = 137260754729766ULL;   // 2*3^29

    std::vector<std::int32_t> log16;
    std::vector<u64> invpow;
    u64 c_inv;

    DL30() : log16(M16, -1), invpow(O16) {
        u64 v = 1;
        for (u64 e = 0; e < O16; ++e) {
            log16[v] = (std::int32_t)e;
            v = 2 * v % M16;
        }

        const u64 inv2 = (M30 + 1) / 2;
        v = 1;
        for (u64 e = 0; e < O16; ++e) {
            invpow[e] = v;
            v = mulmod(v, inv2, M30);
        }

        const u64 B = powmod(2, O16, M30);
        if ((B - 1) % M16) std::exit(3);
        c_inv = invmod(((B - 1) / M16) % H, H);
    }

    u64 log(u64 u) const {
        const int e0 = log16[u % M16];
        if (e0 < 0) std::exit(4);
        const u64 R = mulmod(u, invpow[e0], M30);
        if (R % M16 != 1) std::exit(5);
        return (u64)e0 + O16 * mulmod((R - 1) / M16, c_inv, H);
    }
};

struct Target {
    u64 l;
    u64 s;
    bool operator<(const Target& o) const { return l < o.l; }
};

int main() {
    DL30 dl;

    const u64 G = 120123938613220ULL;
    const u64 K = 197151077055918ULL;
    const u64 invG = invmod(G, DL30::M30);

    // T(S)=5+G^{-1}(4S+K).  The target is a unit exactly when the
    // lowest upper-22 Cantor digit is zero, so write S=3*C_21.
    std::vector<u64> cvals{0};
    u64 p = 1;
    for (int i = 0; i < 21; ++i) {
        const std::size_t n = cvals.size();
        for (std::size_t j = 0; j < n; ++j) cvals.push_back(cvals[j] + p);
        p *= 3;
    }

    std::vector<Target> targets;
    targets.reserve(cvals.size());
    for (u64 c : cvals) {
        const u64 S = 3 * c;
        const u64 rhs = (4 * S + K) % DL30::M30;
        const u64 T = (5 + mulmod(invG, rhs, DL30::M30)) % DL30::M30;
        if (T % 3 == 0) std::exit(6);
        targets.push_back({dl.log(T), S});
    }
    std::sort(targets.begin(), targets.end());

    // Exact lower-18 near-return differences.
    std::vector<u64> low18{0};
    p = 1;
    for (int i = 0; i < 18; ++i) {
        const std::size_t n = low18.size();
        for (std::size_t j = 0; j < n; ++j) low18.push_back(low18[j] + p);
        p *= 3;
    }

    const u64 M18 = 387420489ULL;  // 3^18
    const u64 R18 = 350996365ULL;
    const u64 DNEAR = 29785654ULL;
    std::vector<u64> dvals;
    for (u64 s : low18) {
        const u64 xr = (4 * s + 3) % M18;
        const u64 d = (R18 + M18 - xr) % M18;
        if (d <= DNEAR) dvals.push_back(d);
    }
    std::sort(dvals.begin(), dvals.end());
    if (dvals.size() != 13824 || dvals.front() != 20971503ULL) std::exit(7);

    // Corrected DK/Ostrowski inherited-amplitude ceiling.
    const u64 ZCAP = 21128727ULL;
    std::vector<u64> max_dcap(targets.size(), 0);

    u64 inv2pow_r = 1;
    unsigned long long r_with_hits = 0;
    unsigned long long raw_pairs = 0;
    unsigned long long max_per_r = 0;
    unsigned long long budget_pairs = 0;
    u64 min_z = UINT64_MAX;
    u64 min_w = 0;
    u64 min_r = 0;
    u64 min_budget_z = UINT64_MAX;
    u64 min_budget_w = 0;
    u64 min_budget_r = 0;

    // Safe rational simplifications of the exact upstream certificates:
    // U_S < 33068504827,
    // Lambda_- > 898654/10^18,
    // 1/(6 ln 2) > 240449/10^6.
    // Relevant Ostrowski digit-sum error <= 92/3.
    const u128 DEN = (u128)117 * 1000000000000000000ULL;
    const u64 U = 33068504827ULL;
    const u64 LAM = 898654ULL;
    const u128 DLAM = 117;
    const u128 DCOST = 1000000000000ULL;

    auto consume = [&](u64 lo, u64 hi, u64 a, u64 r) -> u64 {
        if (lo > hi) return 0;
        auto it = std::lower_bound(targets.begin(), targets.end(), Target{lo, 0});
        auto ed = std::upper_bound(targets.begin(), targets.end(), Target{hi, UINT64_MAX});
        u64 n = 0;

        for (; it != ed; ++it) {
            const u64 w = (a + DL30::O30 - it->l) % DL30::O30;
            if (!(w >= 1 && w <= ZCAP - r)) continue;
            ++n;

            const u64 z = w + r;
            if (z < min_z) {
                min_z = z;
                min_w = w;
                min_r = r;
            }

            const u64 CQ18 = 23724081064404ULL;
            const u128 Y = (u128)4 * CQ18 + (u128)4 * it->s + 1;
            const u128 y = (u128)R18 + (u128)M18 * Y;

            // Safe lower cost:
            // 240449/1e6 * (1 + 200/117*(z-3)) - 92/3.
            // Its numerator over 117e6 is the signed integer below.
            const i128 cost_num =
                (i128)240449 * ((i128)117 + (i128)200 * ((i128)z - 3))
                - (i128)92 * 39 * 1000000;
            const u128 positive_cost_num = cost_num > 0 ? (u128)cost_num : 0;

            const u128 base = (u128)U * DEN;
            const u128 lambda_term = (u128)LAM * y * DLAM;
            const u128 cost_term = positive_cost_num * DCOST;
            if (base < lambda_term || base - lambda_term < cost_term) continue;

            const u128 rem = base - lambda_term - cost_term;
            u64 dcap = (u64)(rem / DEN);
            if (dcap > DNEAR) dcap = DNEAR;
            if (dcap < dvals.front()) continue;

            ++budget_pairs;
            if (z < min_budget_z) {
                min_budget_z = z;
                min_budget_w = w;
                min_budget_r = r;
            }

            const std::size_t idx = (std::size_t)(it - targets.begin());
            if (dcap > max_dcap[idx]) max_dcap[idx] = dcap;
        }
        return n;
    };

    for (u64 r = 0; r < ZCAP; ++r) {
        const u64 A = (2 + mulmod(3, inv2pow_r, DL30::M30)) % DL30::M30;
        const u64 a = dl.log(A);
        const u64 W = ZCAP - r;
        u64 n = 0;

        if (a >= W) {
            n += consume(a - W, a - 1, a, r);
        } else {
            if (a) n += consume(0, a - 1, a, r);
            n += consume(DL30::O30 - (W - a), DL30::O30 - 1, a, r);
        }

        if (n) {
            ++r_with_hits;
            raw_pairs += n;
            max_per_r = std::max<unsigned long long>(max_per_r, n);
        }

        if (inv2pow_r & 1) inv2pow_r = (inv2pow_r + DL30::M30) >> 1;
        else inv2pow_r >>= 1;
    }

    unsigned long long upper_states = 0;
    unsigned long long ordinary_start_superset = 0;
    for (u64 dcap : max_dcap) {
        if (!dcap) continue;
        ++upper_states;
        ordinary_start_superset += (unsigned long long)
            (std::upper_bound(dvals.begin(), dvals.end(), dcap) - dvals.begin());
    }

    std::cout
        << "r_with_hits=" << r_with_hits
        << " raw_pairs=" << raw_pairs
        << " max_per_r=" << max_per_r
        << " budget_pairs=" << budget_pairs
        << " upper_states=" << upper_states
        << " ordinary_start_superset=" << ordinary_start_superset
        << " min_z=" << min_z
        << " min_w=" << min_w
        << " min_r=" << min_r
        << " min_budget_z=" << min_budget_z
        << " min_budget_w=" << min_budget_w
        << " min_budget_r=" << min_budget_r
        << '\n';

    if (targets.size() != 2097152ULL) return 10;
    if (r_with_hits != 3071912ULL) return 11;
    if (raw_pairs != 3411199ULL) return 12;
    if (max_per_r != 6ULL) return 13;
    if (budget_pairs != 730578ULL) return 14;
    if (upper_states != 443009ULL) return 15;
    if (ordinary_start_superset != 2525428246ULL) return 16;
    if (min_z != 3232ULL || min_w != 994ULL || min_r != 2238ULL) return 17;
    if (min_budget_z != 3232ULL || min_budget_w != 994ULL || min_budget_r != 2238ULL) return 18;

    return 0;
}
