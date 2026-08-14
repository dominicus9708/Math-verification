#include <bits/stdc++.h>
using namespace std;
using u32 = uint32_t;
using u64 = uint64_t;

// Exact depth-28 counterpart of the gap44/Hensel cyclic-correlation theorem.
//
// Inputs are q-slice uint32 residue files produced by
//   depth28_hensel_retained_residue_qslice.cpp
// for q=18,...,28, named q18.bin,...,q28.bin in the supplied directory.
//
// The union contains exactly 1,976,972 depth-28 retained residues modulo 2^28.
// After reducing (N-3)/4, correlation lives on Z/2^26 Z.

static constexpr u32 MOD = 2013265921u; // 15*2^27+1
static constexpr u32 G = 31u;

u32 modpow(u32 a, u64 e) {
    u64 r = 1, b = a;
    while (e) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return u32(r);
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
                const u32 v = u32(w * a[i + j + half] % MOD);
                u32 s = u + v;
                if (s >= MOD) s -= MOD;
                a[i + j] = s;
                a[i + j + half] = (u >= v) ? (u - v) : (u + MOD - v);
                w = w * wlen % MOD;
            }
        }
    }
    if (inverse) {
        const u32 inv_n = modpow(u32(n), MOD - 2);
        for (u32& x : a) x = u32(u64(x) * inv_n % MOD);
    }
}

int main(int argc, char** argv) {
    const string dir = (argc > 1) ? argv[1] : ".";
    constexpr u32 N = 1u << 26;
    constexpr u32 MASK = N - 1;

    static_assert((MOD - 1) % N == 0);
    const u32 rootN = modpow(G, (MOD - 1) / N);
    if (modpow(rootN, N) != 1 || modpow(rootN, N / 2) == 1) return 2;

    vector<u32> low_rev(N, 0), allow(N, 0);

    // Low C21 multiplicity modulo 2^26, reversed for correlation.
    vector<u32> sums(1, 0);
    sums.reserve(1u << 21);
    u32 weight = 1;
    for (int i = 0; i < 21; ++i) {
        const size_t old = sums.size();
        sums.resize(2 * old);
        for (size_t j = 0; j < old; ++j)
            sums[old + j] = (sums[j] + weight) & MASK;
        weight = u32(u64(weight) * 3u & MASK);
    }
    for (u32 x : sums) ++low_rev[(-x) & MASK];

    // Union disjoint q-slices and reduce r == 3 mod 4 to (r-3)/4 mod 2^26.
    u64 allow_count = 0;
    for (int q = 18; q <= 28; ++q) {
        const string path = dir + "/q" + to_string(q) + ".bin";
        ifstream f(path, ios::binary);
        if (!f) {
            cerr << "cannot read " << path << '\n';
            return 3;
        }
        vector<u32> residues((istreambuf_iterator<char>(f)), {});
        // The iterator constructor above is byte-oriented and unsuitable for u32.
        // Re-open with an explicit byte count.
        f.close();
        ifstream g(path, ios::binary | ios::ate);
        const streamsize bytes = g.tellg();
        if (bytes < 0 || bytes % 4) return 4;
        g.seekg(0);
        vector<u32> rr(size_t(bytes / 4));
        g.read(reinterpret_cast<char*>(rr.data()), bytes);
        if (!g) return 5;

        for (u32 r : rr) {
            if ((r & 3u) != 3u) return 6;
            const u32 x = (r - 3u) >> 2;
            if (allow[x]) return 7; // q-slices must be disjoint
            allow[x] = 1;
            ++allow_count;
        }
    }

    if (allow_count != 1'976'972ULL) {
        cerr << "allow count mismatch " << allow_count << '\n';
        return 8;
    }

    ntt(low_rev, false);
    ntt(allow, false);
    for (u32 i = 0; i < N; ++i)
        low_rev[i] = u32(u64(low_rev[i]) * allow[i] % MOD);
    ntt(low_rev, true);

    u32 minimum = numeric_limits<u32>::max();
    u32 maximum = 0, argmax = 0;
    u64 total = 0;
    for (u32 h = 0; h < N; ++h) {
        const u32 v = low_rev[h];
        if (v > (1u << 21)) return 9;
        minimum = min(minimum, v);
        if (v > maximum) { maximum = v; argmax = h; }
        total += v;
    }

    const u64 expected_total = (1ULL << 21) * 1'976'972ULL;
    if (total != expected_total) return 10;
    if (minimum != 60'645u || maximum != 62'985u || argmax != 23'528'858u)
        return 11;

    u32 delta = 1;
    for (int i = 0; i < 21; ++i) delta = u32(u64(delta) * 3u & MASK);

    u32 pair_max = 0, pair_argmax = 0;
    for (u32 h = 0; h < N; ++h) {
        const u32 v = low_rev[h] + low_rev[(h + delta) & MASK];
        if (v > pair_max) { pair_max = v; pair_argmax = h; }
    }

    if (delta != 58'479'283u || pair_max != 125'165u || pair_argmax != 34'750'766u)
        return 12;

    cout << "R1 gap44/depth28 correlation certificate: PASS\n";
    cout << "depth28_retained_count " << allow_count << '\n';
    cout << "correlation_min " << minimum << '\n';
    cout << "correlation_max " << maximum << '\n';
    cout << "argmax " << argmax << '\n';
    cout << "adjacent_copy_shift " << delta << '\n';
    cout << "two_copy_uniform_bound " << pair_max << '\n';
    cout << "two_copy_argmax " << pair_argmax << '\n';
    return 0;
}
