#include <algorithm>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

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

static std::int64_t egcd(std::int64_t a, std::int64_t b,
                         std::int64_t& x, std::int64_t& y) {
    if (!b) { x = 1; y = 0; return a; }
    std::int64_t x1, y1;
    auto g = egcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return g;
}

static u64 invmod(u64 a, u64 m) {
    std::int64_t x, y;
    if (egcd((std::int64_t)a, (std::int64_t)m, x, y) != 1) {
        std::cerr << "inverse failure\n";
        std::exit(2);
    }
    x %= (std::int64_t)m;
    if (x < 0) x += m;
    return (u64)x;
}

// Fast exact discrete logarithm base 2 modulo 3^30.
// First tabulate logs modulo 3^16.  If e0 is the low exponent modulo
// 2*3^15, then after division by 2^e0 the residual is 1 mod 3^16.
// Because (3^16)^2 is 0 mod 3^30, the remaining 14 ternary exponent
// digits lift linearly in one step.
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
            v = (2 * v) % M16;
        }

        const u64 inv2 = (M30 + 1) / 2;
        v = 1;
        for (u64 e = 0; e < O16; ++e) {
            invpow[e] = v;
            v = mulmod(v, inv2, M30);
        }

        const u64 B = powmod(2, O16, M30);
        if ((B - 1) % M16) std::exit(3);
        const u64 c = ((B - 1) / M16) % H;
        c_inv = invmod(c, H);
    }

    inline u64 log(u64 u) const {
        const std::int32_t ee = log16[u % M16];
        if (ee < 0) std::exit(4);
        const u64 e0 = (u64)ee;
        const u64 R = mulmod(u, invpow[e0], M30);
        if (R % M16 != 1) std::exit(5);
        const u64 t = mulmod((R - 1) / M16, c_inv, H);
        return e0 + O16 * t;
    }
};

struct Target {
    u64 l;
    u64 s;
    bool operator<(const Target& o) const { return l < o.l; }
};

int main() {
    DL30 dl;

    // Independent internal check of the discrete-log lift.
    std::mt19937_64 rng(1234567);
    for (int i = 0; i < 1000; ++i) {
        const u64 e = rng() % DL30::O30;
        const u64 u = powmod(2, e, DL30::M30);
        if (dl.log(u) != e) {
            std::cerr << "discrete-log check failed\n";
            return 6;
        }
    }

    const u64 G = 120123938613220ULL;
    const u64 K = 197151077055918ULL;
    const u64 invG = invmod(G, DL30::M30);

    // T(S)=5+G^{-1}(4S+K).  T is a unit exactly when the lowest
    // ternary Cantor digit is zero, so generate S=3*C_21.
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
        if (T % 3 == 0) return 7;
        targets.push_back({dl.log(T), S});
    }
    std::sort(targets.begin(), targets.end());

    // Exact lower-18 near-return d-values.
    std::vector<u64> low18{0};
    p = 1;
    for (int i = 0; i < 18; ++i) {
        const std::size_t n = low18.size();
        for (std::size_t j = 0; j < n; ++j) low18.push_back(low18[j] + p);
        p *= 3;
    }
    const u64 M18 = 387420489ULL;
    const u64 r18 = 350996365ULL;
    const u64 Dnear = 29785654ULL;
    std::vector<u64> dvals;
    for (u64 sl : low18) {
        const u64 xr = (4 * sl + 3) % M18;
        const u64 d = (r18 + M18 - xr) % M18;
        if (d <= Dnear) dvals.push_back(d);
    }
    std::sort(dvals.begin(), dvals.end());
    if (dvals.size() != 13824 || dvals.front() != 20971503ULL) return 8;

    // Universal amplitude ceiling from the run-level correction bound.
    const u64 ZCAP = 24750138ULL;
    const u64 inv2 = (DL30::M30 + 1) / 2;
    u64 u = 1; // 2^{-r}

    unsigned long long r_with_hits = 0;
    unsigned long long total_pairs = 0;
    unsigned long long max_per_r = 0;
    unsigned long long budget_pairs = 0;
    unsigned long long start_superset = 0;

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
            const u64 Cq18 = 23724081064404ULL;
            const u128 Y = (u128)4 * Cq18 + (u128)4 * it->s + 1;
            const u128 y = (u128)r18 + (u128)M18 * Y;

            // Rigorous safe filter using the convenient rational bounds
            // U_S < 33068504827 and Lambda_- > 89865134/10^20,
            // together with Delta S > 125/351*(z-2).
            const u128 SCALE = (u128)10000000000ULL * 10000000000ULL;
            const u128 lhs = (u128)125 * SCALE * (z >= 2 ? z - 2 : 0);
            const u128 rhs0 = (u128)351 * SCALE * (33068504827ULL - 20971503ULL);
            const u128 rhs1 = (u128)351 * 89865134ULL * y;
            if (rhs0 < rhs1 || lhs > rhs0 - rhs1) continue;

            ++budget_pairs;
            const u128 rem = rhs0 - rhs1 - lhs;
            const u128 den = (u128)351 * SCALE;
            const u64 dcap = 20971503ULL + (u64)(rem / den);
            start_superset += (unsigned long long)
                (std::upper_bound(dvals.begin(), dvals.end(), dcap) - dvals.begin());
        }
        return n;
    };

    for (u64 r = 0; r < ZCAP; ++r) {
        const u64 A = (2 + mulmod(3, u, DL30::M30)) % DL30::M30;
        const u64 a = dl.log(A);
        const u64 W = ZCAP - r;
        u64 n = 0;

        if (a >= W) {
            n += consume(a - W, a - 1, a, r);
        } else {
            if (a > 0) n += consume(0, a - 1, a, r);
            n += consume(DL30::O30 - (W - a), DL30::O30 - 1, a, r);
        }

        if (n) {
            ++r_with_hits;
            total_pairs += n;
            if (n > max_per_r) max_per_r = n;
        }

        if (u & 1) u = (u + DL30::M30) >> 1;
        else u >>= 1;
    }

    std::cout
        << "r_with_hits=" << r_with_hits
        << " total_pairs=" << total_pairs
        << " max_per_r=" << max_per_r
        << " budget_pairs=" << budget_pairs
        << " start_superset=" << start_superset
        << '\n';

    if (targets.size() != 2097152ULL) return 9;
    if (r_with_hits != 4142478ULL) return 10;
    if (total_pairs != 4680313ULL) return 11;
    if (max_per_r != 7ULL) return 12;
    if (budget_pairs != 1004770ULL) return 13;
    if (start_superset != 5156118135ULL) return 14;
    return 0;
}
