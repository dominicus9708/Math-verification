// MATH-035: exact finite bootstrap on 0 <= r <= 2e9 using the audited
// cut-10 bounded residue lifting + MATH-031 cyclic 22-step prefilter +
// MATH-033 base-independent 22-step critical-prefix rolling gate.
//
// This certificate records the independently executed finite result from the
// current DSD-native calculation line.  The conclusion is only an internal
// adjacent-block same-endpoint coupling exclusion in the audited
// universal-spine/coefficient-survival scope.  Collatz remains OPEN.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u128 = unsigned __int128;
using u64 = uint64_t;
using boost::multiprecision::cpp_int;

struct S { uint32_t r; u128 y; uint8_t q, k; };
struct T11 { uint8_t s; uint64_t c; array<uint8_t,12> pref; };
struct D22 { uint8_t jcrit, scrit, stotal; };

static const u64 RMAX = 2'000'000'000ULL;
static const int M11 = 1 << 11;
static const int M22 = 1 << 22;
static const int MASK22 = M22 - 1;
static const int KEND = 1029;

int qpub[KEND + 23];
u128 p3[64];
cpp_int A, B, pA[23], pB[23], p2i[23];

int compare_score(int j1, int s1, int j2, int s2) {
    const int dj = j1 - j2;
    const int ds = s1 - s2;
    if (dj == 0) return ds < 0 ? 1 : (ds > 0 ? -1 : 0);
    if (ds == 0) return dj > 0 ? 1 : -1;
    if (dj > 0 && ds < 0) return 1;
    if (dj < 0 && ds > 0) return -1;
    if (dj > 0) {
        const cpp_int lhs = p2i[dj] * pB[ds];
        const cpp_int &rhs = pA[ds];
        assert(lhs != rhs);
        return lhs > rhs ? 1 : -1;
    }
    const cpp_int lhs = p2i[-dj] * pB[-ds];
    const cpp_int &rhs = pA[-ds];
    assert(lhs != rhs);
    return lhs > rhs ? -1 : 1;
}

uint32_t inverse_odd(uint32_t a) {
    uint32_t x = a;
    for (int i = 0; i < 5; ++i) x *= 2 - a * x;
    return x;
}

bool step11(u128 &n, int &q, const T11 *d11) {
    const int u = int(n & (M11 - 1));
    const auto de = d11[u];
    const u128 UMAX = ~u128(0);
    if (n > (UMAX - de.c) / p3[de.s]) return false;
    n = (p3[de.s] * n + de.c) >> 11;
    q += de.s;
    return true;
}

int main() {
    B = cpp_int(1) << 71;
    A = 3 * B + 1;
    pA[0] = pB[0] = p2i[0] = 1;
    for (int i = 1; i <= 22; ++i) {
        pA[i] = pA[i-1] * A;
        pB[i] = pB[i-1] * B;
        p2i[i] = p2i[i-1] * 2;
    }

    cpp_int two = 1, ap = 1, bp = 1;
    int qp = 0;
    for (int k = 1; k <= KEND + 22; ++k) {
        two *= 2;
        while (!(ap > two * bp)) {
            ap *= A;
            bp *= B;
            ++qp;
        }
        qpub[k] = qp;
    }

    p3[0] = 1;
    for (int i = 1; i < 64; ++i) p3[i] = p3[i-1] * 3;

    T11 d11[M11];
    for (int u = 0; u < M11; ++u) {
        uint64_t n = u;
        int s = 0;
        array<uint8_t,12> pref{};
        for (int j = 1; j <= 11; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3*n + 1)/2; ++s; }
            else n /= 2;
            pref[j] = uint8_t(s);
        }
        const uint64_t c = uint64_t(M11)*n - uint64_t(p3[s])*uint64_t(u);
        d11[u] = {uint8_t(s), c, pref};
    }

    vector<D22> descriptor(M22);
    vector<uint8_t> H61(M22);
    for (int u = 0; u < M22; ++u) {
        uint64_t n = u;
        int s = 0, jcrit = 1, scrit = 0;
        array<uint8_t,23> pref{};
        for (int j = 1; j <= 22; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) { n = (3*n + 1)/2; ++s; }
            else n /= 2;
            pref[j] = uint8_t(s);
            if (j == 1 || compare_score(j,s,jcrit,scrit) > 0) {
                jcrit = j;
                scrit = s;
            }
        }
        descriptor[u] = {uint8_t(jcrit), uint8_t(scrit), uint8_t(s)};
        int explicit_h = INT_MIN;
        for (int j = 1; j <= 22; ++j)
            explicit_h = max(explicit_h, qpub[61+j] - int(pref[j]));
        assert(explicit_h == qpub[61+jcrit] - scrit);
        H61[u] = uint8_t(explicit_h);
    }

    const int Q0 = 39, Q1 = 53, NQ = Q1 - Q0 + 1;
    const int WORDS = M22 / 64;
    vector<vector<uint64_t>> bits(NQ, vector<uint64_t>(WORDS));
    uint32_t mult[NQ], inv[NQ];
    for (int qq = Q0; qq <= Q1; ++qq) {
        const int qi = qq - Q0;
        mult[qi] = uint32_t(p3[qq] & MASK22);
        inv[qi] = inverse_odd(mult[qi]) & MASK22;
        for (int t = 0; t < M22; ++t) {
            const uint32_t u = uint32_t(uint64_t(mult[qi]) * t) & MASK22;
            if (H61[u] <= qq) bits[qi][t >> 6] |= 1ULL << (t & 63);
        }
    }

    vector<S> frontier{{0,0,0,0}};
    for (int k = 0; k < 10; ++k) {
        vector<S> next;
        const u64 add = 1ULL << k;
        for (const auto st : frontier) {
            for (int e = 0; e <= 1; ++e) {
                if (e && u64(st.r) + add > RMAX) continue;
                const u128 z = st.y + (e ? p3[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qpub[k+1]) continue;
                const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                next.push_back({r2,y2,uint8_t(q2),uint8_t(k+1)});
            }
        }
        frontier.swap(next);
    }
    assert(frontier.size() == 64);

    unsigned long long leaves = 0, inst83 = 0, gates22 = 0;
    long long survive = 0, overflow = 0;
    int deepest = 0;
    unsigned long long witness = ~0ULL;
    uint32_t min_r = UINT32_MAX, max_r = 0;
    array<unsigned long long,64> qhist{};

    #pragma omp parallel
    {
        unsigned long long l=0, i83=0, g22=0;
        long long sv=0, ov=0;
        int dp=0;
        unsigned long long wit=~0ULL;
        uint32_t lrmin=UINT32_MAX, lrmax=0;
        array<unsigned long long,64> lh{};

        #pragma omp for schedule(dynamic,1)
        for (int fi = 0; fi < (int)frontier.size(); ++fi) {
            vector<S> stack{frontier[fi]};
            while (!stack.empty()) {
                const S st = stack.back();
                stack.pop_back();
                if (st.k < 61) {
                    const u64 add = 1ULL << st.k;
                    for (int e = 1; e >= 0; --e) {
                        if (e && u64(st.r) + add > RMAX) continue;
                        const u128 z = st.y + (e ? p3[st.q] : 0);
                        const int odd = int(z & 1);
                        const int q2 = int(st.q) + odd;
                        if (q2 < qpub[st.k+1]) continue;
                        const u128 y2 = odd ? (3*z + 1)/2 : z/2;
                        const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                        stack.push_back({r2,y2,uint8_t(q2),uint8_t(st.k+1)});
                    }
                    continue;
                }

                ++l;
                ++lh[st.q];
                lrmin = min(lrmin, st.r);
                lrmax = max(lrmax, st.r);
                const int qq = st.q;
                assert(qq >= Q0 && qq <= Q1);
                const int qi = qq - Q0;
                const uint32_t phase22 = uint32_t(st.y & MASK22);
                const uint32_t z0 = uint32_t(uint64_t(inv[qi]) * phase22) & MASK22;
                const uint32_t start = (z0 + 1025u) & MASK22;

                int remain=339, offset=0;
                uint32_t pos=start;
                while (remain) {
                    const int wi = pos >> 6;
                    const int bitoff = pos & 63;
                    int take = min(remain, 64-bitoff);
                    if (pos + take > M22) take = M22-pos;
                    uint64_t word = bits[qi][wi] >> bitoff;
                    if (take < 64) word &= (1ULL << take)-1;

                    while (word) {
                        const int bit = __builtin_ctzll(word);
                        const int delta = offset + bit;
                        const int b = 1025 + delta;
                        const uint32_t t = (start + delta) & MASK22;
                        const uint32_t u = uint32_t(uint64_t(mult[qi]) * t) & MASK22;
                        ++i83;

                        u128 n = st.y + u128(b)*p3[qq];
                        int qn = qq;
                        bool bad = !step11(n,qn,d11) || !step11(n,qn,d11);
                        if (bad) { ++ov; word &= word-1; continue; }
                        assert(qn == qq + descriptor[u].stotal);

                        int K=83;
                        for (; K+22 <= KEND; K += 22) {
                            ++g22;
                            const uint32_t ur = uint32_t(n & MASK22);
                            const auto de = descriptor[ur];
                            const int need = qpub[K + de.jcrit] - de.scrit;
                            if (qn < need) break;
                            if (!step11(n,qn,d11) || !step11(n,qn,d11)) {
                                bad=true; ++ov; break;
                            }
                        }
                        if (!bad) {
                            dp=max(dp,K);
                            if (K==545) {
                                const unsigned long long packed =
                                    (static_cast<unsigned long long>(st.r)<<16) |
                                    static_cast<unsigned long long>(b);
                                wit=min(wit,packed);
                            }
                            if (K+22 > KEND) ++sv;
                        }
                        word &= word-1;
                    }
                    remain -= take;
                    offset += take;
                    pos = (pos + take) & MASK22;
                }
            }
        }

        #pragma omp critical
        {
            leaves += l; inst83 += i83; gates22 += g22;
            survive += sv; overflow += ov; deepest=max(deepest,dp);
            witness=min(witness,wit); min_r=min(min_r,lrmin); max_r=max(max_r,lrmax);
            for (int q=0;q<64;++q) qhist[q]+=lh[q];
        }
    }

    assert(leaves == 3'592'089ULL);
    assert(min_r == 703u);
    assert(max_r == 1'999'999'935u);
    const unsigned long long expected[] = {
        771761ULL,987601ULL,794250ULL,514554ULL,285599ULL,
        140125ULL,61616ULL,24051ULL,8723ULL,2770ULL,745ULL,
        231ULL,54ULL,8ULL,1ULL
    };
    for (int q=39;q<=53;++q) assert(qhist[q] == expected[q-39]);
    assert(inst83 == 379'544'924ULL);
    assert(gates22 == 588'381'926ULL);
    assert(survive == 0);
    assert(overflow == 0);
    assert(deepest == 545);
    assert((witness >> 16) == 378'620'799ULL);
    assert((witness & 0xffffULL) == 1183ULL);

    cout << "PASS MATH-035\n";
    cout << "RMAX=" << RMAX << " depth61 leaves=" << leaves
         << " first=" << min_r << " last=" << max_r << "\n";
    cout << "depth83 instantiations=" << inst83
         << " base83+ tail22 gates=" << gates22 << "\n";
    cout << "survive=" << survive << " overflow=" << overflow
         << " deepest failing base=" << deepest << "\n";
    cout << "witness r=" << (witness >> 16)
         << " b=" << (witness & 0xffffULL) << "\n";
    cout << "finite internal coupling frontier=6000000003\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
