// Exact finite certificate for first-resonance prefix displacement <= 10.
//
// For every length-72 coefficient-surviving parity prefix whose ordinal
// displacement count from the mechanical Beatty prefix is at most 10, compute
// the unique canonical start modulo 2^72.  If it lies in the strict global
// first-resonance band
//
//     2^71 < N < (4/3) 2^71,
//
// follow that exact natural-number orbit to its actual first coefficient
// crossing.  Every such endpoint is below N.  Therefore a hypothetical
// first-resonance minimal counterexample must have D_72 >= 11.
//
// No floating point arithmetic is used.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

static constexpr int H = 72;
static constexpr int MAXR = 10;
static constexpr int CROSS_CAP = 5000;

static vector<int> mechanical_positions;
static vector<int> coefficient_threshold;
static u128 MASK, B;
static u128 inv3pow[90];

static unsigned long long patterns[MAXR + 1] = {};
static unsigned long long band_count[MAXR + 1] = {};
static unsigned long long paradox_at_first_cross[MAXR + 1] = {};
static unsigned long long max_first_cross[MAXR + 1] = {};
static u128 max_cross_start[MAXR + 1] = {};

static string u128_string(u128 x) {
    if (!x) return "0";
    string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

static u128 inverse_odd_mod_2_72(u128 a) {
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x *= (u128)2 - a * x;
    return x & MASK;
}

static pair<int, bool> first_coefficient_cross(u128 n) {
    u128 x = n;
    int q = 0;
    const u128 overflow_limit = (~(u128)0 - 1) / 3;

    for (int j = 1; j <= CROSS_CAP; ++j) {
        if (x & 1) {
            ++q;
            if (x > overflow_limit) {
                cerr << "128-bit orbit overflow before first crossing\n";
                exit(2);
            }
            x = (3 * x + 1) >> 1;
        } else {
            x >>= 1;
        }

        // coefficient_threshold[j] = ceil(j log_3 2), precomputed by exact
        // comparisons of integer powers.  Thus q<threshold is exactly
        // 3^q<2^j.
        if (q < coefficient_threshold[j]) return {j, x >= n};
    }

    cerr << "first-crossing safety cap reached\n";
    exit(3);
}

static void evaluate_prefix(const vector<int>& positions, int displacement_count) {
    u128 R = 0;
    for (int p : positions)
        R = (3 * R + (((u128)1) << p)) & MASK;

    int q = (int)positions.size();
    u128 N = ((u128)0 - R * inv3pow[q]) & MASK;

    patterns[displacement_count]++;
    if (!(N > B && 3 * N < 4 * B)) return;

    band_count[displacement_count]++;
    auto [j, endpoint_not_below_start] = first_coefficient_cross(N);

    if (endpoint_not_below_start)
        paradox_at_first_cross[displacement_count]++;

    if ((unsigned long long)j > max_first_cross[displacement_count]) {
        max_first_cross[displacement_count] = j;
        max_cross_start[displacement_count] = N;
    }
}

static void enumerate_positions(int ordinal, int previous_position,
                                int displacement_count,
                                vector<int>& positions) {
    const int bj = mechanical_positions[ordinal];
    const int max_position = min(bj, H - 1);

    for (int p = previous_position + 1; p <= max_position; ++p) {
        const int next_displacement = displacement_count + (p != bj);
        if (next_displacement > MAXR) continue;

        positions.push_back(p);

        // The mechanical prefix has 46 odds through depth 72.  Prefix
        // coefficient survival forces at least those 46 ordinals; stopping
        // after any later ordinal represents the case that the next odd
        // position is >=72.
        if (ordinal + 1 >= 46)
            evaluate_prefix(positions, next_displacement);

        if (p < H - 1 && ordinal + 1 < (int)mechanical_positions.size())
            enumerate_positions(ordinal + 1, p, next_displacement, positions);

        positions.pop_back();
    }
}

int main() {
    MASK = (((u128)1) << H) - 1;
    B = ((u128)1) << 71;

    // Exact Beatty thresholds and enough mechanical odd positions.
    coefficient_threshold.assign(CROSS_CAP + 1, 0);
    cpp_int pow3 = 1;
    cpp_int pow2 = 1;
    int k = 0;
    int previous_k = 0;

    for (int j = 1; j <= CROSS_CAP; ++j) {
        pow2 <<= 1;
        while (pow3 < pow2) {
            pow3 *= 3;
            ++k;
        }
        coefficient_threshold[j] = k;

        if (j <= 140 && k > previous_k)
            mechanical_positions.push_back(j - 1);
        previous_k = k;
    }

    assert(coefficient_threshold[72] == 46);
    assert(mechanical_positions[45] == 71);
    assert(mechanical_positions[46] == 72);

    u128 p3 = 1;
    for (int q = 0; q < 90; ++q) {
        if (q) p3 = (3 * p3) & MASK;
        inv3pow[q] = inverse_odd_mod_2_72(p3);
        assert(((p3 * inv3pow[q]) & MASK) == 1);
    }

    vector<int> positions;
    enumerate_positions(0, -1, 0, positions);

    const unsigned long long expected_patterns[MAXR + 1] = {
        1ULL, 26ULL, 351ULL, 3275ULL, 23725ULL,
        142153ULL, 732947ULL, 3341257ULL, 13733231ULL,
        51650827ULL, 179812491ULL
    };

    const unsigned long long expected_band[MAXR + 1] = {
        0ULL, 7ULL, 40ULL, 541ULL, 3913ULL,
        23583ULL, 122732ULL, 557068ULL, 2290462ULL,
        8608590ULL, 29964365ULL
    };

    const unsigned long long expected_max_cross[MAXR + 1] = {
        0ULL, 81ULL, 140ULL, 134ULL, 184ULL,
        265ULL, 278ULL, 308ULL, 379ULL, 357ULL, 471ULL
    };

    unsigned long long total_patterns = 0;
    unsigned long long total_band = 0;
    unsigned long long total_paradox = 0;

    for (int r = 0; r <= MAXR; ++r) {
        assert(patterns[r] == expected_patterns[r]);
        assert(band_count[r] == expected_band[r]);
        assert(max_first_cross[r] == expected_max_cross[r]);
        assert(paradox_at_first_cross[r] == 0);

        total_patterns += patterns[r];
        total_band += band_count[r];
        total_paradox += paradox_at_first_cross[r];

        cout << "D72=" << r
             << " patterns=" << patterns[r]
             << " band=" << band_count[r]
             << " first-cross-paradox=" << paradox_at_first_cross[r]
             << " max-first-cross=" << max_first_cross[r];
        if (max_first_cross[r])
            cout << " start=" << u128_string(max_cross_start[r]);
        cout << "\n";
    }

    assert(total_patterns == 249440284ULL);
    assert(total_band == 41571301ULL);
    assert(total_paradox == 0ULL);

    cout << "PASS first-resonance D72<=10 exclusion\n";
    cout << "total_prefixes=" << total_patterns << "\n";
    cout << "total_band_starts=" << total_band << "\n";
    cout << "latest_actual_first_cross=471\n";
    cout << "therefore any first-resonance minimal candidate has D72>=11\n";
    return 0;
}
