#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = __uint128_t;

static int contraction_budget(int d) {
    if (d <= 0) return -1;
    u128 p3 = 1;
    for (int i = 0; i < d; ++i) p3 *= 3;
    int E = -1;
    while ((u128(1) << (d + E + 1)) < p3) ++E;
    return E;
}

struct RState { u64 residue; std::uint8_t E; };

static bool reverse_forbidden(u64 mask, int d, const std::vector<u64>& p3) {
    u64 S = 0, p = 1;
    for (int i = 0; i < d; ++i) {
        if ((mask >> i) & 1ULL) S += p;
        p *= 3;
    }

    const int qmax = d + 2;
    const int Emax = contraction_budget(d);
    const u64 y = 9 * S + 8;
    std::vector<RState> st, tmp, next;
    st.reserve(256); tmp.reserve(2048); next.reserve(256);
    st.push_back({y,0});

    for (int q = 1; q <= qmax; ++q) {
        const u64 mod = p3[qmax-q];
        tmp.clear();
        for (const auto s : st) {
            const int c3 = int(s.residue % 3);
            if (c3 == 0) continue;
            const int parity = (c3 == 2) ? 0 : 1;
            for (int e = parity; e <= Emax - int(s.E); e += 2) {
                const int E = int(s.E) + e;
                const u128 numerator = (u128(1) << (e+1)) * s.residue - 1;
                u64 r = u64(numerator / 3);
                if (mod > 1) r %= mod; else r = 0;
                tmp.push_back({r, std::uint8_t(E)});
            }
        }
        if (tmp.empty()) return false;
        std::sort(tmp.begin(), tmp.end(), [](const RState& a, const RState& b) {
            return a.residue < b.residue ||
                   (a.residue == b.residue && a.E < b.E);
        });
        next.clear();
        for (const auto s : tmp)
            if (next.empty() || next.back().residue != s.residue) next.push_back(s);
        st.swap(next);
        if (q >= 3) {
            int Emin = 127;
            for (const auto s : st) Emin = std::min(Emin, int(s.E));
            if (Emin <= contraction_budget(q-2)) return true;
        }
    }
    return false;
}

static int barrier(int k) {
    u128 p3 = 1, p2 = u128(1) << k;
    int q = 0;
    while (p3 < p2) { p3 *= 3; ++q; }
    return q;
}

struct PState { u64 r, y, p3; int q; };

static PState extend_parity(PState s, int k, int b) {
    const int carry = b ^ int(s.y & 1ULL);
    const u64 endpoint = s.y + (carry ? s.p3 : 0);
    if (carry) s.r += u64(1) << k;
    if (b) {
        s.y = (3 * endpoint + 1) / 2;
        ++s.q;
        s.p3 *= 3;
    } else {
        s.y = endpoint / 2;
    }
    return s;
}

static void generate_binary_survivors(int k, PState s, std::vector<std::uint8_t>& alive) {
    constexpr int L = 26;
    if (k == L) {
        if ((s.r & 3ULL) != 3ULL) std::abort();
        alive[(s.r - 3) / 4] = 1;
        return;
    }
    for (int b = 0; b <= 1; ++b) {
        if (k < 2 && b != 1) continue; // core starts are 3 mod 4: universal OO
        PState t = extend_parity(s, k, b);
        if (t.q < barrier(k+1)) continue;
        generate_binary_survivors(k+1, t, alive);
    }
}

int main() {
    constexpr int D = 23;
    constexpr int L = 26;
    constexpr int R = L - 2;
    constexpr u64 LOW_COUNT = u64(1) << D;
    constexpr u64 M = u64(1) << R;
    constexpr u64 FULL = u64(1) << 44;

    std::vector<u64> p3(D+3,1);
    for (int i=1; i<int(p3.size()); ++i) p3[i] = p3[i-1] * 3ULL;

    std::vector<std::uint8_t> allowed(LOW_COUNT,0);
    unsigned long long killed = 0;
    #pragma omp parallel for reduction(+:killed) schedule(dynamic,4096)
    for (u64 mask=0; mask<LOW_COUNT; ++mask) {
        const bool bad = reverse_forbidden(mask,D,p3);
        allowed[mask] = bad ? 0 : 1;
        if (bad) ++killed;
    }
    if (killed != 299740ULL) return 2;

    std::vector<u64> pow3mod(45,1);
    for (int i=1; i<=44; ++i) pow3mod[i] = (3 * pow3mod[i-1]) & (M-1);

    std::vector<u64> dp(M,0), next(M,0);
    // Enumerate the allowed low-23 subset sums by Gray code.
    u64 cur = pow3mod[44], previous_gray = 0;
    for (u64 index=0; index<LOW_COUNT; ++index) {
        const u64 gray = index ^ (index >> 1);
        if (index) {
            const u64 diff = gray ^ previous_gray;
            const int bit = __builtin_ctzll(diff);
            if (gray & diff) cur = (cur + pow3mod[bit]) & (M-1);
            else             cur = (cur - pow3mod[bit]) & (M-1);
        }
        previous_gray = gray;
        if (allowed[gray]) ++dp[cur];
    }

    // Add the unrestricted high ternary digits a_23,...,a_43 by exact cyclic
    // subset-sum convolution.
    for (int i=23; i<44; ++i) {
        const u64 shift = pow3mod[i];
        #pragma omp parallel for schedule(static)
        for (u64 r=0; r<M; ++r)
            next[r] = dp[r] + dp[(r-shift) & (M-1)];
        dp.swap(next);
    }

    unsigned long long reverse_allowed_mass = 0;
    for (u64 c : dp) reverse_allowed_mass += c;
    const unsigned long long expected_allowed =
        (LOW_COUNT - killed) * (u64(1) << (44-D));
    if (reverse_allowed_mass != expected_allowed) return 3;

    std::vector<std::uint8_t> binary_alive(M,0);
    generate_binary_survivors(0,{0,0,1,0},binary_alive);
    u64 survivor_classes = 0;
    for (auto b : binary_alive) survivor_classes += b;
    if (survivor_classes != 1037374ULL) return 4;

    unsigned long long cross_mass = 0;
    for (u64 r=0; r<M; ++r)
        if (binary_alive[r]) cross_mass += dp[r];

    if (cross_mass != 1048897463045ULL) return 5;

    constexpr unsigned long long BINARY_ONLY_MASS = 1087765074138ULL;

    std::cout << "reverse_depth23_killed=" << killed << "/" << LOW_COUNT << "\n";
    std::cout << "reverse_allowed_mass=" << reverse_allowed_mass << "\n";
    std::cout << "binary_depth26_classes=" << survivor_classes << "\n";
    std::cout << "binary_only_mass=" << BINARY_ONLY_MASS << "\n";
    std::cout << "cross_mass=" << cross_mass << "\n";
    std::cout << std::setprecision(18);
    std::cout << "cross_fraction_of_full=" << (long double)cross_mass / FULL << "\n";
    std::cout << "binary_fraction_full=" << (long double)BINARY_ONLY_MASS / FULL << "\n";
    std::cout << "binary_fraction_conditioned_on_reverse="
              << (long double)cross_mass / reverse_allowed_mass << "\n";
    return 0;
}
