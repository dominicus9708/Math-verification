#include <bits/stdc++.h>
using namespace std;
using u32 = uint32_t;
using u64 = uint64_t;

// Exact cyclic-correlation certificate for the R1 gap44 + depth27 Hensel merge.
//
// Input file allow27.bin is produced by
//   collatz/src/depth27_hensel_retained_residue_builder.cpp
// and contains the exact depth-27 retained dyadic residue bitset.
//
// After dividing residues N == 3 (mod 4) by the affine coordinate
//   x = (N-3)/4 mod 2^25,
// we correlate the low-21 ternary selector multiset
//   C21 = sum_{i=0}^{20} a_i 3^i
// against the retained indicator for every cyclic shift in Z/2^25 Z.
//
// The NTT modulus 2013265921 = 15*2^27+1 supports length 2^25.
// Every true correlation count is <= 2^21 < MOD, so one modulus is exact.

static constexpr u32 MOD = 2013265921u;
static constexpr u32 G = 31u;

u32 modpow(u32 a, u64 e) {
    u64 r = 1, b = a;
    while (e) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return static_cast<u32>(r);
}

void ntt(vector<u32>& a, bool inverse) {
    const size_t n = a.size();
    for (size_t i = 1, j = 0; i < n; ++i) {
        size_t bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (size_t len = 2; len <= n; len <<= 1) {
        u32 wlen = modpow(G, (MOD - 1) / len);
        if (inverse) wlen = modpow(wlen, MOD - 2);
        const size_t half = len >> 1;
        for (size_t i = 0; i < n; i += len) {
            u64 w = 1;
            for (size_t j = 0; j < half; ++j) {
                const u32 u = a[i + j];
                const u32 v = static_cast<u32>(w * a[i + j + half] % MOD);
                u32 s = u + v;
                if (s >= MOD) s -= MOD;
                a[i + j] = s;
                a[i + j + half] = (u >= v) ? (u - v) : (u + MOD - v);
                w = w * wlen % MOD;
            }
        }
    }

    if (inverse) {
        const u32 inv_n = modpow(static_cast<u32>(n), MOD - 2);
        for (u32& x : a) x = static_cast<u32>(static_cast<u64>(x) * inv_n % MOD);
    }
}

int main(int argc, char** argv) {
    const string path = (argc > 1) ? argv[1] : "allow27.bin";
    constexpr u32 N = 1u << 25;
    constexpr u32 MASK = N - 1;

    static_assert((MOD - 1) % N == 0);
    const u32 rootN = modpow(G, (MOD - 1) / N);
    if (modpow(rootN, N) != 1 || modpow(rootN, N / 2) == 1) {
        cerr << "NTT root-order assertion failed\n";
        return 2;
    }

    vector<u32> low_rev(N, 0), allow(N, 0);

    vector<u32> sums(1, 0);
    sums.reserve(1u << 21);
    u32 weight = 1;
    for (int i = 0; i < 21; ++i) {
        const size_t old = sums.size();
        sums.resize(2 * old);
        for (size_t j = 0; j < old; ++j)
            sums[old + j] = (sums[j] + weight) & MASK;
        weight = static_cast<u32>(static_cast<u64>(weight) * 3u & MASK);
    }
    if (sums.size() != (1u << 21)) return 3;

    u64 low_total = 0;
    for (u32 x : sums) {
        ++low_rev[(-x) & MASK];
        ++low_total;
    }
    if (low_total != (1u << 21)) return 4;

    ifstream f(path, ios::binary);
    vector<u64> bits((1u << 27) / 64);
    f.read(reinterpret_cast<char*>(bits.data()), bits.size() * sizeof(u64));
    if (!f) {
        cerr << "cannot read " << path << '\n';
        return 5;
    }

    u64 allow_count = 0;
    for (u32 x = 0; x < N; ++x) {
        const u32 r = (x << 2) | 3u;
        if ((bits[r >> 6] >> (r & 63)) & 1ULL) {
            allow[x] = 1;
            ++allow_count;
        }
    }
    if (allow_count != 1'061'510ULL) {
        cerr << "allow count mismatch: " << allow_count << '\n';
        return 6;
    }

    ntt(low_rev, false);
    ntt(allow, false);
    for (u32 i = 0; i < N; ++i)
        low_rev[i] = static_cast<u32>(static_cast<u64>(low_rev[i]) * allow[i] % MOD);
    ntt(low_rev, true);

    u32 minimum = numeric_limits<u32>::max();
    u32 maximum = 0;
    u32 argmax = 0;
    u64 total = 0;
    for (u32 h = 0; h < N; ++h) {
        const u32 v = low_rev[h];
        if (v >= MOD || v > (1u << 21)) return 7;
        minimum = min(minimum, v);
        if (v > maximum) {
            maximum = v;
            argmax = h;
        }
        total += v;
    }

    if (minimum != 65'248u || maximum != 67'470u || argmax != 23'374'573u)
        return 8;

    const u64 expected_total = (1ULL << 21) * 1'061'510ULL;
    if (total != expected_total) return 9;

    // If a gap interval of length < 3^21 meets two low-21 copies, their
    // high-prefix starts must differ by exactly 3^21.  Therefore the reduced
    // dyadic shifts differ by delta = 3^21 mod 2^25.  Compute the exact
    // maximum of the sum of the two complete-copy correlations.  This safely
    // dominates the actual tail+head intersection.
    u32 delta = 1;
    for (int i = 0; i < 21; ++i)
        delta = static_cast<u32>(static_cast<u64>(delta) * 3u & MASK);

    u32 pair_max = 0;
    u32 pair_argmax = 0;
    for (u32 h = 0; h < N; ++h) {
        const u32 v = low_rev[h] + low_rev[(h + delta) & MASK];
        if (v > pair_max) {
            pair_max = v;
            pair_argmax = h;
        }
    }

    if (delta != 24'924'851u || pair_max != 134'265u || pair_argmax != 26'369'234u)
        return 10;

    cout << "R1 gap44/depth27 correlation certificate: PASS\n";
    cout << "low_selector_count " << (1u << 21) << '\n';
    cout << "depth27_retained_count " << allow_count << '\n';
    cout << "correlation_min " << minimum << '\n';
    cout << "correlation_max " << maximum << '\n';
    cout << "argmax " << argmax << '\n';
    cout << "adjacent_copy_shift " << delta << '\n';
    cout << "two_copy_uniform_bound " << pair_max << '\n';
    cout << "two_copy_argmax " << pair_argmax << '\n';
    return 0;
}
