#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

using u64 = std::uint64_t;
static constexpr int MEXP = 22;
static constexpr std::uint32_t MOD = 1u << MEXP;
static constexpr std::uint32_t MASK = MOD - 1;

struct Stats { u64 mn, mx, sum; };

Stats selector_dp_stats(int Q) {
    std::vector<u64> dp(MOD), nd(MOD);
    dp[0] = 1;
    std::uint32_t w = 1;
    for (int i = 0; i < 44; ++i) {
        if (i) w = (u64(w) * 3u) & MASK;
        if (i < Q) continue;
        for (std::uint32_t r = 0; r < MOD; ++r)
            nd[r] = dp[r] + dp[(r + MOD - w) & MASK];
        dp.swap(nd);
    }
    Stats s{std::numeric_limits<u64>::max(), 0, 0};
    for (u64 x : dp) {
        s.mn = std::min(s.mn, x);
        s.mx = std::max(s.mx, x);
        s.sum += x;
    }
    return s;
}

struct Transition { int Q, B0, B1; u64 T0, T1; long double observed_worst; };

int main() {
    const Stats full = selector_dp_stats(0);
    if (full.mn != 4'188'525ULL || full.mx != 4'199'983ULL ||
        full.sum != (1ULL << 44)) return 2;

    std::array<Stats, 10> st{};
    st[7] = selector_dp_stats(7);
    st[8] = selector_dp_stats(8);
    st[9] = selector_dp_stats(9);

    if (st[7].mn != 32'039ULL || st[7].mx != 33'523ULL || st[7].sum != (1ULL << 37)) return 3;
    if (st[8].mn != 15'871ULL || st[8].mx != 16'878ULL || st[8].sum != (1ULL << 36)) return 4;
    if (st[9].mn != 7'826ULL || st[9].mx != 8'584ULL || st[9].sum != (1ULL << 35)) return 5;

    const Transition tr[] = {
        {7,18,20,808'636'281'975ULL,784'787'338'151ULL,0.970512230760285933L},
        {7,20,22,784'787'338'151ULL,758'790'964'225ULL,0.966880742700459664L},
        {8,18,20,801'761'825'945ULL,776'902'007'561ULL,0.969002126690579002L},
        {8,20,22,776'902'007'561ULL,750'528'152'486ULL,0.966062004983500975L},
        {9,18,20,783'213'881'122ULL,758'110'858'098ULL,0.969164685593047698L},
        {9,20,22,758'110'858'098ULL,731'875'202'312ULL,0.966216078008374639L},
    };

    std::cout << std::setprecision(18);
    std::cout << "full_dp min " << full.mn << " max " << full.mx
              << " ratio " << (long double)full.mn/full.mx << '\n';

    long double worst_derived = 0;
    for (const auto &x : tr) {
        const Stats h = st[x.Q];
        const long double kappa =
            ((long double)h.mn / h.mx) * ((long double)full.mn / full.mx);
        const long double eta = (long double)(x.T0 - x.T1) / x.T0;
        const long double derived_upper = 1.0L - kappa * eta;
        if (!(x.observed_worst <= derived_upper + 1e-18L)) return 10 + x.Q;
        if (!(derived_upper < 0.972L)) return 20 + x.Q;
        worst_derived = std::max(worst_derived, derived_upper);
        std::cout << "Q" << x.Q << " B" << x.B0 << "->" << x.B1
                  << " high_minmax " << h.mn << '/' << h.mx
                  << " kappa " << kappa
                  << " eta " << eta
                  << " derived_survivor_upper " << derived_upper
                  << " observed_worst " << x.observed_worst << '\n';
    }

    std::cout << "uniform_derived_upper " << worst_derived << '\n';
    std::cout << "certificate PASS\n";
    return 0;
}
