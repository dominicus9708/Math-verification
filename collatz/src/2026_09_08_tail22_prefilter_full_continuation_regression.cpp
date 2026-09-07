// MATH-032: full-continuation regression for the MATH-031 22-step cyclic-window
// prefilter on the finite RMAX=1e9 domain.
//
// The first two 11-step address windows (depth 61->83) are replaced by one
// exact 22-step cyclic-window prefilter.  Only depth-83 survivors are
// instantiated as exact endpoints, then the audited 11-step rolling operator
// resumes from base depth 83.  The final finite outputs are regressed against
// MATH-028.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u128 = unsigned __int128;
using u64 = uint64_t;
using boost::multiprecision::cpp_int;

struct S { uint32_t r; u128 y; uint8_t q, k; };
struct T11 { uint8_t s; uint64_t c; array<uint8_t,12> pref; };

static const u64 RMAX = 1'000'000'000ULL;
static const int M11 = 1 << 11;
static const int M22 = 1 << 22;
static const int MASK22 = M22 - 1;
static const int KEND = 1029;
int qminv[KEND + 1];
u128 pow3v[700];

uint32_t inv_odd(uint32_t a) {
    uint32_t x = a;
    for (int i = 0; i < 5; ++i) x *= 2 - a * x;
    return x;
}

int main() {
    // Exact threshold sequence plus frozen published-floor equality.
    cpp_int two = 1, three = 1;
    int qs = 0;
    const cpp_int B = cpp_int(1) << 71;
    const cpp_int A = 3 * B + 1;
    cpp_int ap = 1, bp = 1;
    int qp = 0;

    for (int k = 1; k <= KEND; ++k) {
        two *= 2;
        while (three < two) { three *= 3; ++qs; }
        qminv[k] = qs;
        while (!(ap > two * bp)) { ap *= A; bp *= B; ++qp; }
        assert(qp == qs);
    }

    pow3v[0] = 1;
    for (int i = 1; i < 700; ++i) pow3v[i] = pow3v[i - 1] * 3;

    // Audited 11-step local descriptors.
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

    int H61[M11];
    for (int u = 0; u < M11; ++u) {
        int h = -100;
        for (int j = 1; j <= 11; ++j)
            h = max(h, qminv[61 + j] - int(d11[u].pref[j]));
        H61[u] = h;
    }

    // Exact count of states surviving only the first 11-step address window.
    static uint16_t count11[53][M11];
    for (int qq = 39; qq <= 52; ++qq) {
        const uint32_t m = uint32_t(pow3v[qq] & (M11 - 1));
        for (int phase = 0; phase < M11; ++phase) {
            int c = 0;
            for (int b = 1025; b <= 1363; ++b) {
                const int u = (phase + uint64_t(b) * m) & (M11 - 1);
                if (H61[u] <= qq) ++c;
            }
            count11[qq][phase] = uint16_t(c);
        }
    }

    // Rolling 11-step thresholds from base 83 onward.
    vector<array<int16_t,M11>> H(KEND + 1);
    for (int K = 83; K + 11 <= KEND; K += 11) {
        for (int u = 0; u < M11; ++u) {
            int h = -100;
            for (int j = 1; j <= 11; ++j)
                h = max(h, qminv[K + j] - int(d11[u].pref[j]));
            H[K][u] = int16_t(h);
        }
    }

    // Exact 22-step local descriptor.
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
    }

    // Bitsets in transformed t-coordinate: g_q(t)=1[H22(3^q t)<=q].
    static const int Q0 = 39, Q1 = 52, NQ = Q1 - Q0 + 1;
    static const int WORDS = M22 / 64;
    vector<vector<uint64_t>> bits(NQ, vector<uint64_t>(WORDS));
    uint32_t mult[NQ], inv[NQ];

    for (int qq = Q0; qq <= Q1; ++qq) {
        const int qi = qq - Q0;
        mult[qi] = uint32_t(pow3v[qq] & MASK22);
        inv[qi] = inv_odd(mult[qi]) & MASK22;
        for (int t = 0; t < M22; ++t) {
            const uint32_t u = uint32_t(uint64_t(mult[qi]) * t) & MASK22;
            if (H22[u] <= qq)
                bits[qi][t >> 6] |= 1ULL << (t & 63);
        }
    }

    // Exact cut-10 bounded-lift frontier through depth 61.
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

    unsigned long long total_leaves = 0;
    unsigned long long total_after11 = 0;
    unsigned long long total_instantiated83 = 0;
    unsigned long long total_windows83plus = 0;
    long long survive_to_end = 0;
    long long overflow = 0;
    int deepest_failed_base = 0;
    unsigned long long first_witness = ~0ULL;

    #pragma omp parallel
    {
        unsigned long long leaves = 0, after11 = 0, inst = 0, wins = 0;
        long long send = 0, ovc = 0;
        int deep = 0;
        unsigned long long witness = ~0ULL;

        #pragma omp for schedule(dynamic,1)
        for (int fi = 0; fi < static_cast<int>(frontier.size()); ++fi) {
            vector<S> stack{frontier[fi]};
            while (!stack.empty()) {
                const auto st = stack.back();
                stack.pop_back();

                if (st.k < 61) {
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
                    continue;
                }

                ++leaves;
                const int qq = st.q;
                assert(qq >= Q0 && qq <= Q1);
                after11 += count11[qq][int(st.y & (M11 - 1))];

                const int qi = qq - Q0;
                const uint32_t phase22 = uint32_t(st.y & MASK22);
                const uint32_t z0 = uint32_t(uint64_t(inv[qi]) * phase22) & MASK22;
                const uint32_t start = (z0 + 1025u) & MASK22;

                int remain = 339, offset = 0;
                uint32_t pos = start;
                while (remain) {
                    const int wi = pos >> 6;
                    const int bitoff = pos & 63;
                    int take = min(remain, 64 - bitoff);
                    if (pos + take > M22) take = M22 - pos;

                    uint64_t word = bits[qi][wi] >> bitoff;
                    if (take < 64) word &= (1ULL << take) - 1;

                    while (word) {
                        const int bit = __builtin_ctzll(word);
                        const int delta = offset + bit;
                        const int b = 1025 + delta;
                        const uint32_t t = (start + delta) & MASK22;
                        const uint32_t u = uint32_t(uint64_t(mult[qi]) * t) & MASK22;
                        assert(H22[u] <= qq);
                        ++inst;

                        const u128 n61 = st.y + u128(b) * pow3v[qq];
                        assert(uint32_t(n61 & MASK22) == u);
                        int q83 = qq + S22[u];
                        u128 n83 = (pow3v[S22[u]] * n61 + C22[u]) >> 22;

                        int K = 83;
                        bool bad_overflow = false;
                        for (; K + 11 <= KEND; K += 11) {
                            ++wins;
                            const int ur = int(n83 & (M11 - 1));
                            if (q83 < H[K][ur]) break;

                            const auto de = d11[ur];
                            q83 += de.s;
                            const u128 UMAX = ~u128(0);
                            if (n83 > (UMAX - de.c) / pow3v[de.s]) {
                                bad_overflow = true;
                                ++ovc;
                                break;
                            }
                            n83 = (pow3v[de.s] * n83 + de.c) >> 11;
                        }

                        if (!bad_overflow) {
                            deep = max(deep, K);
                            if (K == 545) {
                                const unsigned long long packed =
                                    (static_cast<unsigned long long>(st.r) << 16)
                                    | static_cast<unsigned long long>(b);
                                witness = min(witness, packed);
                            }
                            if (K + 11 > KEND) ++send;
                        }

                        word &= word - 1;
                    }

                    remain -= take;
                    offset += take;
                    pos = (pos + take) & MASK22;
                }
            }
        }

        #pragma omp critical
        {
            total_leaves += leaves;
            total_after11 += after11;
            total_instantiated83 += inst;
            total_windows83plus += wins;
            survive_to_end += send;
            overflow += ovc;
            deepest_failed_base = max(deepest_failed_base, deep);
            first_witness = min(first_witness, witness);
        }
    }

    assert(total_leaves == 1'796'718ULL);
    assert(total_after11 == 333'913'383ULL);
    assert(total_instantiated83 == 189'767'400ULL);
    assert(total_windows83plus == 467'202'551ULL);
    assert(survive_to_end == 0);
    assert(overflow == 0);
    assert(deepest_failed_base == 545);
    assert((first_witness >> 16) == 378'620'799ULL);
    assert((first_witness & 0xffffULL) == 1183ULL);

    const unsigned long long raw = total_leaves * 339ULL;
    assert(raw == 609'087'402ULL);

    // Legacy 11-step rolling would test every raw address at K=61, every
    // first-window survivor at K=72, and then the identical K>=83 windows.
    const unsigned long long legacy_window_checks =
        raw + total_after11 + total_windows83plus;
    assert(legacy_window_checks == 1'410'203'336ULL);

    const unsigned long long skipped_first_two = raw + total_after11;
    assert(skipped_first_two == 943'000'785ULL);

    cout << "PASS\n";
    cout << "depth61 leaves=" << total_leaves << "\n";
    cout << "after first 11-step window=" << total_after11 << "\n";
    cout << "depth83 exact endpoint instantiations=" << total_instantiated83 << "\n";
    cout << "post83 rolling-window checks=" << total_windows83plus << "\n";
    cout << "legacy total address-window checks=" << legacy_window_checks << "\n";
    cout << "per-address checks replaced in first two windows=" << skipped_first_two << "\n";
    cout << "deepest failing base=" << deepest_failed_base
         << " witness r=" << (first_witness >> 16)
         << " b=" << (first_witness & 0xffffULL) << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
