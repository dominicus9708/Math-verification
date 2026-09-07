// MATH-034: apply the base-independent MATH-033 22-step critical-prefix gate
// to the full finite RMAX=1e9 address continuation.
//
// The MATH-031 22-step cyclic prefilter is used through depth 83.  Thereafter
// each 22-bit residue supplies one exact base-independent threshold via its
// MATH-033 critical prefix.  Endpoint arithmetic is intentionally executed as
// two already-audited 11-step exact affine updates to avoid fixed-width
// overflow from forming one large 22-step numerator.
//
// The final finite outputs are regressed against MATH-028/032.  This is a
// computational acceleration result, not a Collatz proof.

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

static const u64 RMAX = 1'000'000'000ULL;
static const int M11 = 1 << 11;
static const int M22 = 1 << 22;
static const int MASK22 = M22 - 1;
static const int KEND = 1029;

int qpub[KEND + 23];
u128 p3[700];
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
        pA[i] = pA[i - 1] * A;
        pB[i] = pB[i - 1] * B;
        p2i[i] = p2i[i - 1] * 2;
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
    for (int i = 1; i < 700; ++i) p3[i] = p3[i - 1] * 3;

    T11 d11[M11];
    for (int u = 0; u < M11; ++u) {
        uint64_t n = u;
        int s = 0;
        array<uint8_t,12> pref{};
        for (int j = 1; j <= 11; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) {
                n = (3 * n + 1) / 2;
                ++s;
            } else {
                n /= 2;
            }
            pref[j] = uint8_t(s);
        }
        const uint64_t c = uint64_t(M11) * n
                         - uint64_t(p3[s]) * uint64_t(u);
        d11[u] = {uint8_t(s), c, pref};
    }

    vector<D22> descriptor(M22);
    vector<uint8_t> H61(M22);

    for (int u = 0; u < M22; ++u) {
        uint64_t n = u;
        int s = 0;
        int jcrit = 1;
        int scrit = 0;
        array<uint8_t,23> pref{};

        for (int j = 1; j <= 22; ++j) {
            const bool odd = (n & 1ULL) != 0;
            if (odd) {
                n = (3 * n + 1) / 2;
                ++s;
            } else {
                n /= 2;
            }
            pref[j] = uint8_t(s);
            if (j == 1 || compare_score(j, s, jcrit, scrit) > 0) {
                jcrit = j;
                scrit = s;
            }
        }

        descriptor[u] = {uint8_t(jcrit), uint8_t(scrit), uint8_t(s)};

        // Finite regressions of the MATH-033 formula at the prefilter base and
        // the first 22-step rolling base.
        for (int K : {61, 83}) {
            int explicit_h = INT_MIN;
            for (int j = 1; j <= 22; ++j)
                explicit_h = max(explicit_h, qpub[K + j] - int(pref[j]));
            assert(explicit_h == qpub[K + jcrit] - scrit);
        }
        H61[u] = uint8_t(qpub[61 + jcrit] - scrit);
    }

    // MATH-031 cyclic prefilter for the first 22 address-continuation steps.
    const int Q0 = 39, Q1 = 52, NQ = Q1 - Q0 + 1;
    const int WORDS = M22 / 64;
    vector<vector<uint64_t>> bits(NQ, vector<uint64_t>(WORDS));
    uint32_t mult[NQ], inv[NQ];

    for (int qq = Q0; qq <= Q1; ++qq) {
        const int qi = qq - Q0;
        mult[qi] = uint32_t(p3[qq] & MASK22);
        inv[qi] = inverse_odd(mult[qi]) & MASK22;
        for (int t = 0; t < M22; ++t) {
            const uint32_t u = uint32_t(uint64_t(mult[qi]) * t) & MASK22;
            if (H61[u] <= qq)
                bits[qi][t >> 6] |= 1ULL << (t & 63);
        }
    }

    // Exact cut-10 bounded lifting through depth 61.
    vector<S> frontier{{0,0,0,0}};
    for (int k = 0; k < 10; ++k) {
        vector<S> next;
        next.reserve(frontier.size() * 2);
        const u64 add = 1ULL << k;
        for (const auto st : frontier) {
            for (int e = 0; e <= 1; ++e) {
                if (e && u64(st.r) + add > RMAX) continue;
                const u128 z = st.y + (e ? p3[st.q] : 0);
                const int odd = int(z & 1);
                const int q2 = int(st.q) + odd;
                if (q2 < qpub[k + 1]) continue;
                const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
                const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                next.push_back({r2, y2, uint8_t(q2), uint8_t(k + 1)});
            }
        }
        frontier.swap(next);
    }
    assert(frontier.size() == 64);

    unsigned long long total_leaves = 0;
    unsigned long long total_instantiated83 = 0;
    unsigned long long total_blocks22 = 0;
    long long survive_to_end = 0;
    long long overflow = 0;
    int deepest_failed_base = 0;
    unsigned long long first_witness = ~0ULL;

    #pragma omp parallel
    {
        unsigned long long leaves = 0, inst = 0, blocks = 0;
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
                        const u128 z = st.y + (e ? p3[st.q] : 0);
                        const int odd = int(z & 1);
                        const int q2 = int(st.q) + odd;
                        if (q2 < qpub[st.k + 1]) continue;
                        const u128 y2 = odd ? (3 * z + 1) / 2 : z / 2;
                        const uint32_t r2 = st.r + (e ? uint32_t(add) : 0u);
                        stack.push_back({r2, y2, uint8_t(q2), uint8_t(st.k + 1)});
                    }
                    continue;
                }

                ++leaves;
                const int qq = st.q;
                const int qi = qq - Q0;
                assert(qi >= 0 && qi < NQ);

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
                        assert(H61[u] <= qq);
                        ++inst;

                        u128 n = st.y + u128(b) * p3[qq];
                        int qn = qq;

                        // Depth 61->83 endpoint transition.  Sequential 11-step
                        // updates avoid the one-shot 22-step numerator overflow.
                        bool bad = !step11(n, qn, d11) || !step11(n, qn, d11);
                        if (bad) {
                            ++ovc;
                            word &= word - 1;
                            continue;
                        }
                        assert(qn == qq + descriptor[u].stotal);

                        int K = 83;
                        for (; K + 22 <= KEND; K += 22) {
                            ++blocks;
                            const uint32_t ur = uint32_t(n & MASK22);
                            const auto de = descriptor[ur];
                            const int need = qpub[K + de.jcrit] - de.scrit;
                            if (qn < need) break;

                            if (!step11(n, qn, d11) || !step11(n, qn, d11)) {
                                bad = true;
                                ++ovc;
                                break;
                            }
                        }

                        if (!bad) {
                            deep = max(deep, K);
                            if (K == 545) {
                                const unsigned long long packed =
                                    (static_cast<unsigned long long>(st.r) << 16)
                                    | static_cast<unsigned long long>(b);
                                witness = min(witness, packed);
                            }
                            if (K + 22 > KEND) ++send;
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
            total_instantiated83 += inst;
            total_blocks22 += blocks;
            survive_to_end += send;
            overflow += ovc;
            deepest_failed_base = max(deepest_failed_base, deep);
            first_witness = min(first_witness, witness);
        }
    }

    assert(total_leaves == 1'796'718ULL);
    assert(total_instantiated83 == 189'767'400ULL);
    assert(total_blocks22 == 294'223'428ULL);
    assert(survive_to_end == 0);
    assert(overflow == 0);
    assert(deepest_failed_base == 545);
    assert((first_witness >> 16) == 378'620'799ULL);
    assert((first_witness & 0xffffULL) == 1183ULL);

    cout << "PASS\n";
    cout << "depth61 leaves=" << total_leaves
         << " depth83 instantiations=" << total_instantiated83 << "\n";
    cout << "base83+ 22-step threshold gates=" << total_blocks22 << "\n";
    cout << "survive=" << survive_to_end
         << " overflow=" << overflow
         << " deepest failing base=" << deepest_failed_base << "\n";
    cout << "witness r=" << (first_witness >> 16)
         << " b=" << (first_witness & 0xffffULL) << "\n";
    cout << "COLLATZ STATUS=OPEN\n";
}
