// MATH-031: exact 22-step tail descriptor + cyclic-window address prefilter
// on the finite RMAX=1e9 MATH-028 domain.
//
// The 22-step descriptor is exhaustively checked on all 2^22 residues against
// the composition of two audited 11-step blocks.  The address aggregation then
// uses the inverse of 3^q modulo 2^22 so b=1025..1363 becomes a contiguous
// cyclic window.  This is a computational prefilter; it is not a Collatz proof.

#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;
using u64 = uint64_t;

struct S { uint32_t r; u128 y; uint8_t q, k; };
struct T11 { uint8_t s; uint64_t c; array<uint8_t,12> pref; };

static const u64 RMAX = 1'000'000'000ULL;
static const int W = 11;
static const int M11 = 1 << 11;
static const int M22 = 1 << 22;
int qminv[84];
u128 pow3v[84];

uint32_t inv_odd(uint32_t a) {
    uint32_t x = a;
    for (int i = 0; i < 5; ++i) x *= 2 - a * x;
    return x;
}

int main() {
    pow3v[0] = 1;
    for (int i = 1; i < 84; ++i) pow3v[i] = pow3v[i - 1] * 3;

    u128 two = 1, three = 1;
    int q = 0;
    for (int k = 1; k <= 83; ++k) {
        two *= 2;
        while (three < two) { three *= 3; ++q; }
        qminv[k] = q;
    }

    T11 d11[M11];
    for (int u = 0; u < M11; ++u) {
        uint64_t n = u;
        int s = 0;
        array<uint8_t,12> pref{};
        for (int j = 1; j <= 11; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3 * n + 1) / 2; ++s; }
            else n /= 2;
            pref[j] = uint8_t(s);
        }
        const uint64_t c = uint64_t(M11) * n
                         - uint64_t(pow3v[s]) * uint64_t(u);
        d11[u] = {uint8_t(s), c, pref};
    }

    int H61[M11], H72[M11];
    for (int u = 0; u < M11; ++u) {
        int h1 = -100, h2 = -100;
        for (int j = 1; j <= 11; ++j) {
            h1 = max(h1, qminv[61 + j] - int(d11[u].pref[j]));
            h2 = max(h2, qminv[72 + j] - int(d11[u].pref[j]));
        }
        H61[u] = h1;
        H72[u] = h2;
    }

    vector<uint8_t> H22(M22), S22(M22);
    vector<uint64_t> C22(M22);

    for (int u = 0; u < M22; ++u) {
        uint64_t n = u;
        int s = 0, h = -100;
        for (int j = 1; j <= 22; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3 * n + 1) / 2; ++s; }
            else n /= 2;
            h = max(h, qminv[61 + j] - s);
        }

        const u128 c = u128(M22) * n - pow3v[s] * uint64_t(u);
        assert(c <= numeric_limits<uint64_t>::max());
        H22[u] = uint8_t(h);
        S22[u] = uint8_t(s);
        C22[u] = uint64_t(c);

        // Exhaustive composition check against two 11-step blocks.
        const int u0 = u & (M11 - 1);
        const auto a = d11[u0];
        const uint64_t n11 = uint64_t((pow3v[a.s] * u128(u) + a.c) >> 11);
        const int u1 = n11 & (M11 - 1);
        const auto b = d11[u1];

        const int hc = max(H61[u0], H72[u1] - int(a.s));
        const int sc = int(a.s) + int(b.s);
        const u128 cc = pow3v[b.s] * u128(a.c) + (u128(b.c) << 11);

        assert(hc == h);
        assert(sc == s);
        assert(cc == c);
    }

    // Rebuild the exact MATH-028 depth-61 right-offset survivor set using the
    // audited cut-10 streaming tree.
    vector<S> frontier{{0,0,0,0}};
    for (int k = 0; k < 10; ++k) {
        vector<S> next;
        next.reserve(frontier.size() * 2);
        const u64 add = 1ULL << k;
        for (const auto st : frontier) {
            for (int e = 0; e <= 1; ++e) {
                if (e && u64(st.r) + add > RMAX) continue;
                const u128 z = st.y + (e ? pow3v[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qminv[k + 1]) continue;
                const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
                const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                next.push_back({r2, y2, uint8_t(q2), uint8_t(k + 1)});
            }
        }
        frontier.swap(next);
    }
    assert(frontier.size() == 64);

    struct Leaf { uint32_t phase22; uint8_t q; };
    vector<Leaf> leaves;
    leaves.reserve(1'800'000);

    for (const auto root : frontier) {
        vector<S> stack{root};
        while (!stack.empty()) {
            const auto st = stack.back();
            stack.pop_back();
            if (st.k == 61) {
                leaves.push_back({uint32_t(st.y & (M22 - 1)), st.q});
                continue;
            }

            const u64 add = 1ULL << st.k;
            for (int e = 1; e >= 0; --e) {
                if (e && u64(st.r) + add > RMAX) continue;
                const u128 z = st.y + (e ? pow3v[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qminv[st.k + 1]) continue;
                const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
                const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                stack.push_back({r2, y2, uint8_t(q2), uint8_t(st.k + 1)});
            }
        }
    }
    assert(leaves.size() == 1'796'718);

    const map<int, unsigned long long> expected = {
        {39, 5'764'074ULL},
        {40, 26'716'059ULL},
        {41, 43'543'702ULL},
        {42, 44'809'331ULL},
        {43, 33'473'148ULL},
        {44, 19'717'995ULL},
        {45, 9'632'832ULL},
        {46, 3'977'507ULL},
        {47, 1'467'235ULL},
        {48, 483'539ULL},
        {49, 130'113ULL},
        {50, 38'983ULL},
        {51, 11'187ULL},
        {52, 1'695ULL},
    };

    vector<uint32_t> prefix(2 * M22 + 1);
    unsigned long long total = 0;

    // For m=3^q mod 2^22 and z=m^{-1}y, the address residues are
    // m(z+b), b=1025..1363.  Hence the survival indicator becomes a length-339
    // cyclic contiguous window in the transformed coordinate.
    for (const auto [qq, ex] : expected) {
        const uint32_t m = uint32_t(pow3v[qq] & (M22 - 1));
        const uint32_t inv = inv_odd(m) & (M22 - 1);

        prefix[0] = 0;
        for (int i = 0; i < 2 * M22; ++i) {
            const uint32_t t = uint32_t(i) & (M22 - 1);
            const uint32_t u = uint32_t(uint64_t(m) * t) & (M22 - 1);
            prefix[i + 1] = prefix[i] + (H22[u] <= qq ? 1u : 0u);
        }

        unsigned long long sum = 0;
        for (const auto leaf : leaves) {
            if (leaf.q != qq) continue;
            const uint32_t z = uint32_t(uint64_t(inv) * leaf.phase22) & (M22 - 1);
            const uint32_t start = (z + 1025u) & (M22 - 1);
            sum += prefix[start + 339] - prefix[start];
        }

        assert(sum == ex);
        total += sum;
    }

    const unsigned long long raw = leaves.size() * 339ULL;
    assert(raw == 609'087'402ULL);
    assert(total == 189'767'400ULL);

    cout << "PASS\n";
    cout << "all 2^22 descriptors equal composition of two audited 11-step blocks\n";
    cout << "depth61 leaves=" << leaves.size()
         << " raw_address_states=" << raw
         << " depth83_survivors=" << total << "\n";
    cout << "raw/survivor factor=" << double(raw) / double(total) << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
