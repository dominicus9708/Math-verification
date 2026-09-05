// Exact finite certificate for the first global resonance.
//
// It enumerates every length-72 coefficient-surviving parity prefix whose
// ordinal displacement count from the mechanical Beatty prefix is <= 8.
// For every corresponding ordinary start in
//
//     2^71 < N < (4/3) 2^71,
//
// it follows the exact Collatz shortcut orbit until the first coefficient
// crossing and checks that the endpoint is below N.  Consequently any
// first-resonance minimal-counterexample candidate must already have at least
// nine displaced odd ordinals in its first 72 parity positions.
//
// This is a finite certificate, not a proof of the Collatz conjecture.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

static constexpr int H = 72;
static constexpr int MAXR = 8;

static vector<int> bpos;
static u128 MASK, B;
static u128 inv3pow[80];
static unsigned long long patterns[9] = {};
static unsigned long long band_count[9] = {};
static unsigned long long bad_first_cross[9] = {};
static unsigned long long max_cross[9] = {};
static u128 max_cross_start[9] = {};

static string to_string_u128(u128 x) {
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
    // Newton iteration in Z_2; unsigned overflow keeps the low 128 bits,
    // which is more than enough for the low 72-bit inverse.
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x *= (u128)2 - a * x;
    return x & MASK;
}

static cpp_int to_cpp_int(u128 n) {
    cpp_int x = (unsigned long long)(n >> 64);
    x <<= 64;
    x += (unsigned long long)n;
    return x;
}

static pair<int, bool> first_coefficient_cross(u128 n128) {
    cpp_int n = to_cpp_int(n128);
    cpp_int x = n;
    cpp_int p3 = 1;
    cpp_int p2 = 1;

    // The certified scan below never reaches 400.  20,000 is only a hard
    // safety cap; hitting it is treated as certificate failure in main().
    for (int j = 1; j <= 20000; ++j) {
        bool odd = static_cast<bool>(x & 1);
        if (odd) {
            p3 *= 3;
            x = (3 * x + 1) / 2;
        } else {
            x /= 2;
        }
        p2 *= 2;
        if (p3 < p2) return {j, x >= n};
    }
    return {20001, true};
}

static void evaluate_prefix(const vector<int>& a, int cost) {
    // Correction modulo 2^72 for the chosen odd positions.
    u128 R = 0;
    for (int p : a) R = (3 * R + (((u128)1) << p)) & MASK;

    int q = (int)a.size();
    u128 residue = ((u128)0 - (R * inv3pow[q])) & MASK;
    patterns[cost]++;

    // Strict first-resonance band.
    if (!(residue > B && 3 * residue < 4 * B)) return;

    band_count[cost]++;
    auto [j, still_at_or_above_start] = first_coefficient_cross(residue);
    if (j > 20000) {
        cerr << "safety cap reached\n";
        exit(2);
    }
    if (still_at_or_above_start) bad_first_cross[cost]++;
    if ((unsigned long long)j > max_cross[cost]) {
        max_cross[cost] = j;
        max_cross_start[cost] = residue;
    }
}

static void enumerate_positions(int j, int prev, int cost, vector<int>& a) {
    const int bj = bpos[j];
    const int hi = min(bj, H - 1);

    for (int p = prev + 1; p <= hi; ++p) {
        int next_cost = cost + (p != bj);
        if (next_cost > MAXR) continue;

        a.push_back(p);

        // At depth 72, coefficient survival requires at least the 46
        // mechanical odd ordinals.  Stopping here represents the case where
        // all later odd positions are >=72.
        if (j + 1 >= 46) evaluate_prefix(a, next_cost);

        if (p < H - 1 && j + 1 < (int)bpos.size())
            enumerate_positions(j + 1, p, next_cost, a);

        a.pop_back();
    }
}

int main() {
    MASK = (((u128)1) << H) - 1;
    B = ((u128)1) << 71;

    // Generate the mechanical odd positions exactly from
    // k_i = ceil(i log_3 2), using only comparisons 3^k >= 2^i.
    cpp_int pow3 = 1;
    int q_prev = 0;
    for (int i = 1; i <= 130; ++i) {
        cpp_int pow2 = cpp_int(1);
        pow2 <<= i;
        int k = q_prev;
        while (pow3 < pow2) {
            pow3 *= 3;
            ++k;
        }
        if (k - q_prev) bpos.push_back(i - 1);
        q_prev = k;
    }

    // 3^{-q} mod 2^72.
    u128 p3 = 1;
    for (int q = 0; q < 80; ++q) {
        if (q) p3 = (p3 * 3) & MASK;
        inv3pow[q] = inverse_odd_mod_2_72(p3);
        assert((p3 * inv3pow[q] & MASK) == 1);
    }

    vector<int> a;
    enumerate_positions(0, -1, 0, a);

    const unsigned long long expected_patterns[9] = {
        1ULL, 26ULL, 351ULL, 3275ULL, 23725ULL,
        142153ULL, 732947ULL, 3341257ULL, 13733231ULL
    };
    const unsigned long long expected_band[9] = {
        0ULL, 7ULL, 40ULL, 541ULL, 3913ULL,
        23583ULL, 122732ULL, 557068ULL, 2290462ULL
    };
    const unsigned long long expected_max_cross[9] = {
        0ULL, 81ULL, 140ULL, 134ULL, 184ULL,
        265ULL, 278ULL, 308ULL, 379ULL
    };

    unsigned long long total_patterns = 0;
    unsigned long long total_band = 0;
    unsigned long long total_bad = 0;

    for (int r = 0; r <= MAXR; ++r) {
        assert(patterns[r] == expected_patterns[r]);
        assert(band_count[r] == expected_band[r]);
        assert(max_cross[r] == expected_max_cross[r]);
        assert(bad_first_cross[r] == 0);

        total_patterns += patterns[r];
        total_band += band_count[r];
        total_bad += bad_first_cross[r];

        cout << "r=" << r
             << " patterns=" << patterns[r]
             << " band=" << band_count[r]
             << " max_first_cross=" << max_cross[r];
        if (max_cross[r])
            cout << " max_start=" << to_string_u128(max_cross_start[r]);
        cout << "\n";
    }

    assert(total_patterns == 17'976'966ULL);
    assert(total_band == 2'998'346ULL);
    assert(total_bad == 0ULL);

    cout << "PASS first-resonance prefix-72 displacement<=8 exclusion\n";
    cout << "total_patterns=" << total_patterns << "\n";
    cout << "total_band_starts=" << total_band << "\n";
    cout << "latest_first_cross=379\n";
    cout << "conclusion: any first-resonance minimal candidate has >=9 displaced odd ordinals in the first 72 positions\n";
    return 0;
}
