// MATH-056 targeted cross-channel Hensel candidate certificate.
//
// Purpose
// -------
// If a candidate prefix was exact class-max at depth k-1, a competitor ending
// in the same last parity channel cannot become newly dominant after appending
// the common last step: downstream dominance order is preserved. Therefore a
// first Hensel failure at depth k can only arise from the opposite last-parity
// channel.
//
// In fixed-d gap coordinates, if the candidate last bit is odd then an opposite
// competitor ending even must place at least one highest-rank even at G=q. If
// the candidate last bit is even then an opposite competitor ending odd must
// place no even rank at G=q.
//
// The search below uses the exact bounded-carry recurrence and a safe optimistic
// upper bound to decide whether any opposite-channel competitor has positive
// exact Hensel credit.
//
// Canonical finite checks for this source:
//   N=2614662758027828756219  -> first cross-channel failure at depth 56.
//   N=2444527107741509901307  -> no cross-channel failure through depth 90.
//
// The earlier scratch claim of a depth-140 pass is intentionally not canonical:
// while preparing this certificate an unsafe large-exponent implementation of
// the pruning upper bound was identified. Only the overflow-safe checks above
// are retained.
//
// Finite exact computation only. Collatz conjecture remains OPEN.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

static vector<cpp_int> P3BIG;

static inline long long blocksum(int n, int l) {
    if (!l) return 0;
    if (n >= 62) throw runtime_error("audited rank exceeds signed-64 packing");
    return (((1LL << l) - 1) << (n - l));
}

struct Solver {
    int k, d, q;
    vector<int> candidate_blocks;
    unordered_map<string, char> memo;

    Solver(vector<int> const& evens, int K)
        : k(K), d((int)evens.size()), q(K - d), candidate_blocks(q + 1, 0) {
        if (d >= 62) throw runtime_error("audited d must be <62");
        for (int j = 0; j < d; ++j) {
            int G = evens[j] - j;
            if (G < 0 || G > q) throw runtime_error("bad gap coordinate");
            candidate_blocks[G]++;
        }
    }

    bool upper_possible(int rem, int na, int nb, long long h) const {
        // Safe optimistic bound: put all remaining competitor ranks at gap 0
        // and all remaining candidate ranks at the largest remaining gap.
        cpp_int lhs = cpp_int(h - ((1LL << na) - 1));
        lhs <<= rem;
        lhs += cpp_int((1LL << nb) - 1) * P3BIG[rem];
        return lhs > 0;
    }

    string key(int rem, int na, int nb, long long h) const {
        return to_string(rem) + "," + to_string(na) + "," +
               to_string(nb) + "," + to_string(h);
    }

    bool can(int rem, int na, int nb, long long h) {
        if (!upper_possible(rem, na, nb, h)) return false;

        if (rem == 0) {
            long long aa = blocksum(na, candidate_blocks[0]);
            int na2 = na - candidate_blocks[0];
            if (na2 != 0) throw runtime_error("candidate ranks left at terminal");
            long long credit = ((1LL << nb) - 1) - aa + h;
            return credit > 0;
        }

        string K = key(rem, na, nb, h);
        auto it = memo.find(K);
        if (it != memo.end()) return it->second;

        int la = candidate_blocks[rem];
        long long aa = blocksum(na, la);
        int na2 = na - la;
        bool ok = false;

        for (int lb = 0; lb <= nb && !ok; ++lb) {
            long long bb = blocksum(nb, lb);
            long long z = h + bb - aa;
            if (z % 3) continue;
            long long h2 = 2 * (z / 3);
            if (can(rem - 1, na2, nb - lb, h2)) ok = true;
        }

        memo.emplace(K, (char)ok);
        return ok;
    }

    bool cross_channel_dominated(bool candidate_last_odd) {
        int r = q, na = d, nb = d;
        int la = candidate_blocks[r];
        long long aa = blocksum(na, la);
        int na2 = na - la;

        for (int lb = 0; lb <= nb; ++lb) {
            if (candidate_last_odd) {
                if (lb < 1) continue; // competitor must end even
            } else {
                if (lb != 0) continue; // competitor must end odd
            }
            long long bb = blocksum(nb, lb);
            long long z = bb - aa;
            if (z % 3) continue;
            long long h2 = 2 * (z / 3);
            if (can(r - 1, na2, nb - lb, h2)) return true;
        }
        return false;
    }
};

static void parity_prefix(cpp_int N, int K, vector<int>& bits) {
    cpp_int n = N;
    bits.clear();
    bits.reserve(K);
    for (int p = 0; p < K; ++p) {
        if ((n & 1) != 0) {
            bits.push_back(1);
            n = (3 * n + 1) / 2;
        } else {
            bits.push_back(0);
            n /= 2;
        }
    }
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: cert N K\n";
        return 2;
    }

    cpp_int N(argv[1]);
    int K = stoi(argv[2]);
    P3BIG.assign(K + 1, 1);
    for (int i = 1; i <= K; ++i) P3BIG[i] = P3BIG[i - 1] * 3;

    vector<int> bits;
    parity_prefix(N, K, bits);
    vector<int> evens;

    for (int k = 1; k <= K; ++k) {
        if (bits[k - 1] == 0) evens.push_back(k - 1);
        Solver solver(evens, k);
        if (solver.cross_channel_dominated(bits[k - 1] == 1)) {
            cout << "FAIL " << k << " memo " << solver.memo.size() << '\n';
            return 0;
        }
    }

    cout << "PASS_TO " << K << '\n';
}
