// Exact certificate for the m=44 Q=7/B=20 cross-place sieve intersected
// with nested root-Hensel full maximality through H=24.
//
// Main structural audit:
// for a reverse code
//
//   m = (2^K (3^qf N + Rf) - C 2^B) / (2^B 3^qr),
//
// the sign of m-N is controlled by
//
//   A = 2^K 3^qf - 2^B 3^qr
//
// once the start scale dominates every possible finite correction.  With
// Q=7, B<=20, K<=36 and the m=44 core,
//
//   Nmin > 2^Kmax 3^Bmax
//   Nmin > 2^(Kmax+Bmax-1) 3^Q.
//
// Hence A<0 is always a smaller positive ancestor, A>0 never is, and A=0
// reduces exactly to C>Rf.  Unique factorization makes A=0 equivalent to
// K=B and qr=qf.  The program first reproduces the complete published
// Q=7/B=20 counts using this scale-separated rule, then intersects the same
// survivor predicate with the exact H=24 nested root-fullmax language.
//
// Build:
//   g++ -O3 -std=c++17 m44_q7_b20_rootfullmax_h24_scale_rule_certificate.cpp -o cert

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;
using i128 = __int128_t;
using u128 = __uint128_t;

static constexpr int H = 24;
static constexpr int ZBITS = H - 2;
static constexpr u32 ZM = 1u << ZBITS;
static constexpr u32 ZMASK = ZM - 1;
static constexpr int Q = 7;
static constexpr int BMAX = 20;
static constexpr int KMAX = 36;
static constexpr int LOWZBITS = BMAX - 1;
static constexpr u32 LOWZMASK = (1u << LOWZBITS) - 1;
static constexpr int MOD3 = 2187;

struct State { u64 R; std::uint8_t q; };
struct Rev { std::uint8_t qr, K; u64 C; };

u64 p3[50];

std::string s128(i128 x) {
    if (x == 0) return "0";
    bool neg = x < 0;
    u128 y = neg ? u128(-x) : u128(x);
    std::string s;
    while (y) {
        s.push_back(char('0' + y % 10));
        y /= 10;
    }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

inline bool coefficient_ok(int k, int q) {
    return p3[q] >= (1ULL << k);
}

inline u64 class_key(int q, u64 R) {
    return (u64(q) << 56) | (R % p3[q]);
}

void scan_all_words(int pos, int k, int q, u64 R, int qmin,
                    std::unordered_map<u64, u64>& class_max) {
    if (q + (k - pos) < qmin) return;
    if (pos == k) {
        auto it = class_max.find(class_key(q, R));
        if (it != class_max.end() && R > it->second) it->second = R;
        return;
    }
    scan_all_words(pos + 1, k, q, R, qmin, class_max);
    scan_all_words(pos + 1, k, q + 1, 3 * R + (1ULL << pos), qmin, class_max);
}

u64 invodd(u64 a) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

std::vector<u32> build_rootfullmax_h24() {
    const u64 expected[25] = {
        0,
        1, 1, 2, 3, 4, 7, 11, 16, 31, 52, 103, 182, 297, 593, 1049,
        1720, 3439, 6104, 12194, 22244, 38019, 75969, 137657, 234156
    };

    std::vector<State> coefficient{{0, 0}}, nested{{0, 0}};

    for (int k = 1; k <= H; ++k) {
        std::vector<State> nc;
        nc.reserve(coefficient.size() * 2);
        for (auto s : coefficient) {
            if (coefficient_ok(k, s.q)) nc.push_back(s);
            int q1 = s.q + 1;
            u64 R1 = 3 * s.R + (1ULL << (k - 1));
            if (coefficient_ok(k, q1)) nc.push_back({R1, (std::uint8_t)q1});
        }
        coefficient.swap(nc);

        std::unordered_map<u64, u64> cm;
        cm.reserve(coefficient.size() * 2);
        for (auto s : coefficient) {
            u64 key = class_key(s.q, s.R);
            auto [it, ins] = cm.emplace(key, s.R);
            if (!ins && s.R > it->second) it->second = s.R;
        }

        int qmin = 0;
        while (!coefficient_ok(k, qmin)) ++qmin;
        scan_all_words(0, k, 0, 0, qmin, cm);

        std::vector<State> nn;
        nn.reserve(nested.size() * 2);
        for (auto s : nested) {
            if (coefficient_ok(k, s.q)) {
                auto it = cm.find(class_key(s.q, s.R));
                if (it != cm.end() && it->second == s.R) nn.push_back(s);
            }

            int q1 = s.q + 1;
            u64 R1 = 3 * s.R + (1ULL << (k - 1));
            if (coefficient_ok(k, q1)) {
                auto it = cm.find(class_key(q1, R1));
                if (it != cm.end() && it->second == R1)
                    nn.push_back({R1, (std::uint8_t)q1});
            }
        }

        nested.swap(nn);
        if (nested.size() != expected[k]) std::exit(10 + k);
    }

    std::vector<u32> zs;
    zs.reserve(nested.size());
    std::vector<std::uint8_t> seen(ZM, 0);

    for (auto s : nested) {
        u32 N = (u32)(((0ULL - s.R) * invodd(p3[s.q])) & ((1ULL << H) - 1));
        if ((N & 3u) != 3u) std::exit(50);
        u32 z = (N - 3u) >> 2;
        if (seen[z]) std::exit(51);
        seen[z] = 1;
        zs.push_back(z);
    }

    std::sort(zs.begin(), zs.end());
    return zs;
}

std::vector<Rev> reverse_frontier(int z) {
    struct Node { int residue, K; u64 C; };
    std::vector<Node> states{{z, 0, 0}};
    std::vector<Rev> out;

    for (int d = 0; d < Q; ++d) {
        int mod_next = 1;
        for (int j = 0; j < Q - d - 1; ++j) mod_next *= 3;

        std::unordered_map<u64, u64> best;
        best.reserve(states.size() * 8 + 8);

        for (auto st : states) {
            int r3 = st.residue % 3;
            if (r3 == 0) continue;
            int a0 = (r3 == 1) ? 2 : 1;

            for (int a = a0; a <= KMAX - st.K; a += 2) {
                int K2 = st.K + a;
                u64 numerator = (1ULL << a) * (u64)st.residue - 1;
                if (numerator % 3) std::exit(60);

                u64 C2 = (1ULL << a) * st.C + p3[d];
                u64 residue64 = numerator / 3;
                int residue = mod_next > 1 ? int(residue64 % (u64)mod_next) : 0;

                u64 key = (u64(residue) << 8) | u64(K2);
                auto it = best.find(key);
                if (it == best.end() || C2 > it->second) best[key] = C2;
            }
        }

        states.clear();
        states.reserve(best.size());
        std::array<u64, KMAX + 1> byK{};

        for (auto& kv : best) {
            int residue = int(kv.first >> 8);
            int K = int(kv.first & 255);
            states.push_back({residue, K, kv.second});
            byK[K] = std::max(byK[K], kv.second);
        }

        int qr = d + 1;
        for (int K = 0; K <= KMAX; ++K)
            if (byK[K]) out.push_back({(std::uint8_t)qr, (std::uint8_t)K, byK[K]});
    }

    return out;
}

struct RevSummary {
    bool strict_contract = false;
    u64 tie_maxC = 0;
};

std::vector<RevSummary> build_reverse_summaries(
    const std::vector<std::vector<Rev>>& fronts) {
    size_t SZ = (BMAX + 1) * (BMAX + 1) * MOD3;
    std::vector<RevSummary> s(SZ);
    auto idx = [](int B, int q, int z) {
        return (size_t(B) * (BMAX + 1) + q) * MOD3 + z;
    };

    for (int B = 2; B <= BMAX; ++B) {
        for (int qf = 0; qf <= B; ++qf) {
            for (int z = 0; z < MOD3; ++z) {
                auto& o = s[idx(B, qf, z)];
                for (const auto& r : fronts[z]) {
                    i128 lhs = (i128(1) << r.K) * i128(p3[qf]);
                    i128 rhs = (i128(1) << B) * i128(p3[r.qr]);
                    if (lhs < rhs) {
                        o.strict_contract = true;
                        break;
                    }
                    if (lhs == rhs) o.tie_maxC = std::max(o.tie_maxC, r.C);
                }
            }
        }
    }

    return s;
}

struct Fwd { u64 R; std::uint8_t q; bool odd; };

Fwd forward(u32 r, int B) {
    u64 n = r, R = 0;
    int q = 0;
    for (int k = 0; k < B; ++k) {
        if (n & 1ULL) {
            R = 3 * R + (1ULL << k);
            ++q;
            n = (3 * n + 1) >> 1;
        } else {
            n >>= 1;
        }
    }
    return {R, (std::uint8_t)q, bool(n & 1ULL)};
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 30; ++i) p3[i] = p3[i - 1] * 3ULL;

    i128 P44 = 1;
    for (int i = 0; i < 44; ++i) P44 *= 3;
    const i128 NMIN = i128(4) * P44 + 3;
    const i128 NMAX = i128(6) * P44 + 1;

    const i128 BRF = (i128(1) << KMAX) * i128(p3[BMAX]);
    const i128 BRC = (i128(1) << (KMAX + BMAX - 1)) * i128(p3[Q]);
    if (!(NMIN > BRF && NMIN > BRC)) return 2;

    std::cout << "NMIN " << s128(NMIN) << '\n';
    std::cout << "scale_bound_forward_correction " << s128(BRF) << '\n';
    std::cout << "scale_bound_reverse_correction " << s128(BRC) << '\n';

    auto rootz = build_rootfullmax_h24();
    std::cout << "root_h24_residues " << rootz.size() << '\n';

    std::vector<std::vector<Rev>> fronts(MOD3);
    u64 front_entries = 0;
    for (int z = 0; z < MOD3; ++z) {
        fronts[z] = reverse_frontier(z);
        front_entries += fronts[z].size();
    }
    std::cout << "reverse_frontier_entries " << front_entries << '\n';

    auto rs = build_reverse_summaries(fronts);
    auto ridx = [](int B, int q, int z) {
        return (size_t(B) * (BMAX + 1) + q) * MOD3 + z;
    };

    std::array<int, BMAX + 1> inv2{};
    auto modpow = [](int a, int e) {
        long long r = 1, b = a;
        while (e) {
            if (e & 1) r = r * b % MOD3;
            b = b * b % MOD3;
            e >>= 1;
        }
        return int(r);
    };

    int two = 1;
    for (int B = 1; B <= BMAX; ++B) {
        two = (two * 2) % MOD3;
        inv2[B] = modpow(two, 1457);
    }

    struct Path { std::array<Fwd, BMAX + 1> f; };
    std::vector<Path> paths(rootz.size());
    for (size_t j = 0; j < rootz.size(); ++j) {
        u32 r21 = (4u * (rootz[j] & LOWZMASK) + 3u) & ((1u << (BMAX + 1)) - 1);
        for (int B = 2; B <= BMAX; ++B)
            paths[j].f[B] = forward(r21 & ((1u << (B + 1)) - 1), B);
    }

    // Distribution of high selectors a_7,...,a_43 in z=(N-3)/4 modulo 2^22.
    std::vector<u64> dp(ZM), nd(ZM);
    dp[0] = 1;
    u32 w = 1;
    for (int i = 0; i < 44; ++i) {
        if (i == 0) w = 1;
        else w = (u32)((u64)w * 3u & ZMASK);
        if (i < Q) continue;
        for (u32 r = 0; r < ZM; ++r)
            nd[r] = dp[r] + dp[(r + ZM - w) & ZMASK];
        dp.swap(nd);
    }

    u64 dpsum = 0;
    for (u64 c : dp) dpsum += c;
    if (dpsum != (1ULL << (44 - Q))) return 3;

    std::array<u32, 1 << Q> lowshift{};
    std::array<int, 1 << Q> n3{};
    for (int mask = 0; mask < (1 << Q); ++mask) {
        u64 s = 0, pw = 1;
        int t = 3 % MOD3;
        for (int i = 0; i < Q; ++i) {
            if (mask & (1 << i)) {
                s += pw;
                t = (t + 4 * int(pw % MOD3)) % MOD3;
            }
            pw *= 3;
        }
        lowshift[mask] = (u32)(s & ZMASK);
        n3[mask] = t;
    }

    u32 fixed = 1;
    for (int i = 0; i < 44; ++i) fixed = (u32)((u64)fixed * 3u & ZMASK);

    // Full Q=7/B=20 regression using the scale-separated reverse criterion.
    const u32 M19 = 1u << 19, MASK19 = M19 - 1;
    std::vector<u64> dp19(M19), nd19(M19);
    dp19[0] = 1;
    u32 w19 = 1;
    for (int i = 0; i < 44; ++i) {
        if (i == 0) w19 = 1;
        else w19 = (u32)((u64)w19 * 3u & MASK19);
        if (i < Q) continue;
        for (u32 r = 0; r < M19; ++r)
            nd19[r] = dp19[r] + dp19[(r + M19 - w19) & MASK19];
        dp19.swap(nd19);
    }

    u32 fixed19 = 1;
    for (int i = 0; i < 44; ++i)
        fixed19 = (u32)((u64)fixed19 * 3u & MASK19);

    u64 vf = 0, vr = 0, vs = 0;
    std::array<u64, 1 << Q> cross_surv_by_mask{};

    for (int lm = 0; lm < (1 << Q); ++lm) {
        u32 base19 = (fixed19 + (lowshift[lm] & MASK19)) & MASK19;
        for (u32 z19 = 0; z19 < M19; ++z19) {
            u64 mult = dp19[(z19 + M19 - base19) & MASK19];
            if (!mult) continue;

            u64 n = (4ULL * z19 + 3ULL) & ((1ULL << 21) - 1);
            u64 R = 0;
            int q = 0;
            bool done = false;

            for (int k = 0; k < BMAX; ++k) {
                if (n & 1ULL) {
                    R = 3 * R + (1ULL << k);
                    ++q;
                    n = (3 * n + 1) >> 1;
                } else {
                    n >>= 1;
                }

                int B = k + 1;
                if (B < 2) continue;

                i128 slope = i128(p3[q]) - i128(1ULL << B);
                i128 testN = slope > 0 ? NMAX : NMIN;
                if (slope * testN + i128(R) < 0) {
                    vf += mult;
                    done = true;
                    break;
                }

                if (!(n & 1ULL)) continue;
                int z3 = int(((p3[q] % MOD3) * (u64)n3[lm] + (R % MOD3)) % MOD3);
                z3 = int((long long)z3 * inv2[B] % MOD3);
                const auto& sm = rs[ridx(B, q, z3)];

                if (sm.strict_contract || sm.tie_maxC > R) {
                    vr += mult;
                    done = true;
                    break;
                }
            }

            if (!done) {
                vs += mult;
                cross_surv_by_mask[lm] += mult;
            }
        }
    }

    std::cout << "scale_rule_regression_all_q7b20 " << vf << ' ' << vr << ' ' << vs << '\n';
    if (vf != 14'245'065'266'398ULL ||
        vr != 2'191'707'946'271ULL ||
        vs != 1'155'412'831'747ULL) return 9;

    u64 cross_min = ~0ULL, cross_max = 0;
    int cross_min_m = -1, cross_max_m = -1;
    for (int lm = 0; lm < (1 << Q); ++lm) {
        if (cross_surv_by_mask[lm] < cross_min) {
            cross_min = cross_surv_by_mask[lm];
            cross_min_m = lm;
        }
        if (cross_surv_by_mask[lm] > cross_max) {
            cross_max = cross_surv_by_mask[lm];
            cross_max_m = lm;
        }
    }
    std::cout << "cross_mask_survivor_min " << cross_min << " mask " << cross_min_m << '\n';
    std::cout << "cross_mask_survivor_max " << cross_max << " mask " << cross_max_m << '\n';

    u64 root_selector_count = 0, intersection = 0;
    u64 reverse_killed_inside_root = 0;
    std::array<u64, 1 << Q> inter_by_mask{};
    std::array<u64, BMAX + 1> firstkill{};

    for (int lm = 0; lm < (1 << Q); ++lm) {
        u32 base = (fixed + lowshift[lm]) & ZMASK;
        int nmod = n3[lm];

        for (size_t j = 0; j < rootz.size(); ++j) {
            u32 z = rootz[j];
            u32 hr = (z + ZM - base) & ZMASK;
            u64 mult = dp[hr];
            if (!mult) continue;

            root_selector_count += mult;
            bool alive = true;

            for (int B = 2; B <= BMAX; ++B) {
                const Fwd& f = paths[j].f[B];
                if (p3[f.q] < (1ULL << B)) return 4;
                if (!f.odd) continue;

                int z3 = int(((p3[f.q] % MOD3) * (u64)nmod + (f.R % MOD3)) % MOD3);
                z3 = int((long long)z3 * inv2[B] % MOD3);
                const auto& sm = rs[ridx(B, f.q, z3)];

                if (sm.strict_contract || sm.tie_maxC > f.R) {
                    alive = false;
                    reverse_killed_inside_root += mult;
                    firstkill[B] += mult;
                    break;
                }
            }

            if (alive) {
                intersection += mult;
                inter_by_mask[lm] += mult;
            }
        }
    }

    if (root_selector_count != intersection + reverse_killed_inside_root) return 5;
    if (root_selector_count != 982'121'237'012ULL) return 6;
    if (reverse_killed_inside_root != 197'333'898'861ULL) return 7;
    if (intersection != 784'787'338'151ULL) return 8;

    u64 inter_min = ~0ULL, inter_max = 0;
    int inter_min_m = -1, inter_max_m = -1;
    for (int lm = 0; lm < (1 << Q); ++lm) {
        if (inter_by_mask[lm] < inter_min) {
            inter_min = inter_by_mask[lm];
            inter_min_m = lm;
        }
        if (inter_by_mask[lm] > inter_max) {
            inter_max = inter_by_mask[lm];
            inter_max_m = lm;
        }
    }

    std::cout << "combined_mask_survivor_min " << inter_min << " mask " << inter_min_m << '\n';
    std::cout << "combined_mask_survivor_max " << inter_max << " mask " << inter_max_m << '\n';
    std::cout << "root_h24_selector_survivors " << root_selector_count << '\n';
    std::cout << "cross_reverse_killed_inside_root " << reverse_killed_inside_root << '\n';
    std::cout << "q7_b20_and_root_h24_survivors " << intersection << '\n';

    std::cout << "first_reverse_kill_by_B";
    for (int B = 2; B <= BMAX; ++B)
        if (firstkill[B]) std::cout << ' ' << B << ':' << firstkill[B];
    std::cout << '\n';

    const long double TOTAL = (long double)(1ULL << 44);
    const long double CROSS = 1'155'412'831'747.0L;
    std::cout << std::setprecision(15);
    std::cout << "ambient_root_h24_fraction "
              << (long double)root_selector_count / TOTAL << '\n';
    std::cout << "root_h24_conditional_cross_survival "
              << (long double)intersection / root_selector_count << '\n';
    std::cout << "ambient_cross_q7b20_survival " << CROSS / TOTAL << '\n';
    std::cout << "root_h24_fraction_inside_cross "
              << (long double)intersection / CROSS << '\n';
    std::cout << "combined_survival_fraction "
              << (long double)intersection / TOTAL << '\n';
    std::cout << "combined_excluded_fraction "
              << 1.0L - (long double)intersection / TOTAL << '\n';
    std::cout << "cross_survivor_reduction_by_root_h24 "
              << (CROSS - (long double)intersection) / CROSS << '\n';
}
