#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif

using i64 = long long;
using boost::multiprecision::cpp_int;

constexpr int Q = 1526;
constexpr int T = 1539;
constexpr int E = 13;

struct State {
    short a, b, ea, eb;
    i64 c;

    bool operator<(const State& o) const {
        if (a != o.a) return a < o.a;
        if (b != o.b) return b < o.b;
        if (ea != o.ea) return ea < o.ea;
        if (eb != o.eb) return eb < o.eb;
        return c < o.c;
    }

    bool operator==(const State& o) const {
        return a == o.a && b == o.b && ea == o.ea && eb == o.eb && c == o.c;
    }
};

// Exact terminal-inverse-limit survivors from the positive G13 transition
// parent-credit envelope 1..6859.  The cutoff-free terminal automaton reduces
// that whole range to these 403 labels before the two-ended run test below.
static const int candidates[] = {
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,75,76,77,78,79,81,83,84,85,86,87,88,90,91,92,93,94,95,96,97,99,101,102,103,104,105,106,108,111,112,113,114,115,116,117,118,119,121,122,123,124,126,128,129,130,131,132,135,137,138,139,141,142,144,145,146,147,148,151,152,153,155,156,157,159,160,162,166,168,170,171,172,173,174,175,176,177,178,182,183,186,189,191,192,193,194,195,197,198,202,203,204,205,207,209,212,213,216,219,220,221,222,227,228,229,230,231,232,234,237,238,239,240,243,249,250,252,254,255,256,257,258,259,261,263,264,267,268,273,274,276,279,283,284,288,290,291,292,295,297,303,306,307,310,318,319,320,324,328,330,333,335,338,342,344,345,348,349,351,355,357,360,364,365,367,372,374,375,378,381,384,385,387,388,391,394,396,401,402,409,411,414,426,432,435,436,438,445,446,459,465,472,477,480,486,492,495,499,507,513,516,517,522,526,540,544,546,558,561,567,576,578,581,582,583,587,591,594,603,607,621,633,639,648,654,657,662,668,669,689,708,720,729,738,774,783,789,810,816,819,837,864,867,871,873,891,895,924,972,981,993,1002,1003,1039,1062,1080,1094,1107,1154,1161,1175,1215,1224,1296,1312,1336,1366,1384,1386,1458,1503,1593,1620,1640,1641,1690,1731,1732,1750,1822,1836,1849,1944,1958,1968,1984,2004,2049,2065,2076,2077,2079,2083,2187,2257,2309,2430,2460,2461,2535,2551,2597,2598,2625,2733,2754,2916,2937,2952,2976,3006,3113,3114,3281,3382,3645,3690,3897,4131,4374,4428,4464,4509,4669,4671,4677,5072,5073,5535,6226,6561,6642,6696
};
constexpr int NC = sizeof(candidates) / sizeof(candidates[0]);

// e_j = Q-p_j+j.  These are necessary exponent-coordinate bounds for actual
// current-R1 and alternate ordinary E=13 pre-gate paths below current NMAX.
std::array<int,E> amin{1454,1341,1163,882,437,0,0,0,0,0,0,0,0};
std::array<int,E> bmin = amin;
std::array<int,E> amax{1524,1524,1524,1524,1524,1524,1524,1524,1468,1371,1219,979,600};
std::array<int,E> bmax{1526,1526,1526,1526,1526,1526,1526,1526,1468,1371,1219,979,600};

using Opts = std::array<std::vector<int>,14>;
std::vector<Opts> OA, OB;
std::array<int,T> MG;

Opts make_opts(int t, const std::array<int,E>& mn, const std::array<int,E>& mx) {
    Opts out;
    for (int r = 0; r <= 13; ++r) {
        for (int r2 = 0; r2 <= r; ++r2) {
            bool ok = true;
            for (int j = r2; j < r && ok; ++j) {
                if (!(mn[j] <= t && t <= mx[j])) ok = false;
            }
            for (int j = 0; j < r2 && ok; ++j) {
                if (mx[j] <= t) ok = false;
            }
            if (ok) out[r].push_back(r2);
        }
    }
    return out;
}

// If rank j has exponent current_e, then p_j=Q+j-current_e.  If next_e is the
// exponent of the already-assigned next event, current_e-next_e is exactly the
// intervening odd-run length.  For rank 12, next_e<0 denotes the final suffix.
bool gap_ok(int rank, int current_e, int next_e) {
    const int p = Q + rank - current_e;
    if (p < 0 || p >= T) return false;
    const int gap = (rank == 12 && next_e < 0) ? current_e : (current_e - next_e);
    return gap >= 0 && gap <= MG[p];
}

int death_depth(int d) {
    // The relation carry is scaled so that the initial 3-adic equation is
    // c=2^13 d after removing the common unit 2^Q.
    std::vector<State> st{{13,13,-1,-1,(i64(1)<<13)*d}}, nx;

    for (int t = 0; t < Q; ++t) {
        nx.clear();
        nx.reserve(st.size()*4 + 64);

        for (const auto& s : st) {
            for (int a2 : OA[t][s.a]) {
                if (a2 < s.a && !gap_ok(s.a-1, t, s.ea)) continue;
                const i64 A = (i64(1)<<s.a) - (i64(1)<<a2);
                const short ea2 = a2 < s.a ? short(t) : s.ea;

                for (int b2 : OB[t][s.b]) {
                    if (b2 < s.b && !gap_ok(s.b-1, t, s.eb)) continue;
                    const i64 B = (i64(1)<<s.b) - (i64(1)<<b2);
                    const i64 z = s.c + B - A;
                    if (z % 3 == 0) {
                        nx.push_back({
                            short(a2), short(b2), ea2,
                            short(b2 < s.b ? t : s.eb),
                            2*(z/3)
                        });
                    }
                }
            }
        }

        std::sort(nx.begin(), nx.end());
        nx.erase(std::unique(nx.begin(), nx.end()), nx.end());
        st.swap(nx);
        if (st.empty()) return t+1;
    }

    // At K=Q, actual ranks cannot remain because the actual current-core start
    // begins with parity 11, hence its first two relevant exponents are <=1524.
    // Alternate remaining prefix ranks may have e=Q; assign them together and
    // check the final left-end run constraint.
    for (const auto& s : st) {
        if (s.a != 0) continue;
        bool ok = true;
        if (s.b > 0) {
            for (int j = 0; j < s.b; ++j) {
                if (!(bmin[j] <= Q && Q <= bmax[j])) ok = false;
            }
            if (ok) {
                const int rank = s.b-1;
                if (!gap_ok(rank, Q, s.eb)) ok = false;
            }
        }
        if (ok) return 0;
    }
    return Q;
}

int main(int argc, char** argv) {
    const int shard = argc > 1 ? std::atoi(argv[1]) : 0;
    const int shards = argc > 2 ? std::atoi(argv[2]) : 5;
    if (shards <= 0 || shard < 0 || shard >= shards) {
        std::cerr << "usage: certificate [shard_index] [shard_count]\n";
        return 2;
    }

    assert(NC == 403);
    OA.resize(Q);
    OB.resize(Q);
    for (int t = 0; t < Q; ++t) {
        OA[t] = make_opts(t, amin, amax);
        OB[t] = make_opts(t, bmin, bmax);
    }

    // Universal exact growth envelope.  In U=x+1 coordinates an odd step
    // multiplies U by 3/2, while an even step (U+1)/2 <= U for U>=1.  Hence
    //
    // U_{p+1} <= (NMAX+1)*(3/2)^(p+1).
    //
    // MG[p] is its exact floor log2, computed without floating point.
    cpp_int N("5908625413101667397287");
    cpp_int num = N + 1;
    for (int p = 0; p < T; ++p) {
        num *= 3;
        MG[p] = int(boost::multiprecision::msb(num)) - (p+1);
    }
    assert(MG[0] == 72 && MG[192] == 185 && MG[1538] == 972);

    std::vector<int> indices;
    for (int i = shard; i < NC; i += shards) indices.push_back(i);
    std::vector<int> deaths(indices.size());

#ifdef _OPENMP
#pragma omp parallel for schedule(dynamic,1)
#endif
    for (long long z = 0; z < static_cast<long long>(indices.size()); ++z) {
        deaths[static_cast<std::size_t>(z)] = death_depth(candidates[indices[static_cast<std::size_t>(z)]]);
    }

    std::map<int,int> hist;
    const int tested = static_cast<int>(indices.size());
    int survive = 0;
    for (std::size_t z = 0; z < indices.size(); ++z) {
        const int death = deaths[z];
        if (death == 0) {
            ++survive;
            std::cout << "SURVIVE " << candidates[indices[z]] << "\n";
        } else {
            ++hist[death];
        }
    }
    assert(survive == 0);

    // Independent all-403 execution established the following exact five-shard
    // checkpoints.  They make accidental under/over-pruning reproducibly visible.
    if (shards == 5) {
        static const int expected_tested[5] = {81,81,81,80,80};
        static const int expected_1372[5] = {1,0,1,1,1};
        static const int expected_1525[5] = {80,81,80,79,79};
        assert(tested == expected_tested[shard]);
        assert(hist[1372] == expected_1372[shard]);
        assert(hist[1525] == expected_1525[shard]);
        int other = 0;
        for (auto [k,v] : hist) if (k != 1372 && k != 1525) other += v;
        assert(other == 0);
    }

    std::cout << "E13 transition-parent pullback shard: PASS\n";
    std::cout << "shard=" << shard << "/" << shards
              << " tested=" << tested << " survivors=0\n";
    for (auto [k,v] : hist) if (v) {
        std::cout << "death_depth " << k << " count " << v << "\n";
    }
    return 0;
}
