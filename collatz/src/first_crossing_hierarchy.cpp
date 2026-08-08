#include <bits/stdc++.h>
using namespace std;
using u128 = __uint128_t;
using i128 = __int128_t;

// Exact-integer verifier for the accelerated Collatz map
// T(n)=n/2 (even), (3n+1)/2 (odd).
//
// For a fixed first coefficient-stopping length J, enumerate exactly the
// admissible parity words satisfying
//   3^{q_k} >= 2^k for k<J,
//   3^{q_J} <  2^J.
// For every prefix subtree compare:
//   argmin canonical starting residue r
//   argmin descent margin z=r-T^J(r).
// Equality for every subtree is a COMPUTATIONAL CHECK of the current
// Hierarchical Extremal Principle candidate, not a proof for all J.

static string str128(i128 x) {
    if (x == 0) return "0";
    bool neg = x < 0;
    u128 y = neg ? (u128)(-x) : (u128)x;
    string s;
    while (y) { s.push_back(char('0' + y % 10)); y /= 10; }
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

struct State {
    u128 r = 0;   // canonical residue modulo 2^k
    u128 y = 0;   // T^k(r)
    int q = 0;    // number of odd entries in the prefix
    uint64_t bits = 0;
};

struct Result {
    bool any = false;
    State min_r{}, min_z{};
    uint64_t leaves = 0;
    bool hierarchy_ok = true;
    int first_bad_depth = -1;
};

static int J;
static vector<u128> pow2v, pow3v;

static i128 z(const State& s) {
    return (i128)s.r - (i128)s.y;
}

static State extend_state(const State& s, int k, int b) {
    // Two lifts r and r+2^k have endpoints differing by 3^q, hence opposite
    // parity. Choose the unique lift whose time-k parity is b.
    int carry = b ^ int(s.y & 1);
    State t = s;
    t.r = s.r + (carry ? pow2v[k] : 0);
    u128 endpoint = s.y + (carry ? pow3v[s.q] : 0);
    if (b == 0) {
        t.y = endpoint / 2;
    } else {
        t.y = (3 * endpoint + 1) / 2;
        ++t.q;
        t.bits |= (uint64_t(1) << k);
    }
    return t;
}

static Result dfs(State s, int k) {
    if (k == J) {
        Result out;
        out.any = true;
        out.min_r = out.min_z = s;
        out.leaves = 1;
        return out;
    }

    Result out;
    for (int b = 0; b <= 1; ++b) {
        State t = extend_state(s, k, b);
        int kk = k + 1;
        bool admissible = (kk < J)
            ? (pow3v[t.q] >= pow2v[kk])
            : (pow3v[t.q] <  pow2v[kk]);
        if (!admissible) continue;

        Result child = dfs(t, kk);
        if (!child.any) continue;

        if (!out.any) {
            out = child;
        } else {
            out.leaves += child.leaves;
            if (child.min_r.r < out.min_r.r) out.min_r = child.min_r;
            if (z(child.min_z) < z(out.min_z)) out.min_z = child.min_z;
            if (out.hierarchy_ok && !child.hierarchy_ok) {
                out.hierarchy_ok = false;
                out.first_bad_depth = child.first_bad_depth;
            }
        }
    }

    if (out.any && out.hierarchy_ok && out.min_r.bits != out.min_z.bits) {
        out.hierarchy_ok = false;
        out.first_bad_depth = k;
    }
    return out;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: first_crossing_hierarchy J\n";
        return 1;
    }
    J = stoi(argv[1]);
    if (J < 1 || J > 62) {
        cerr << "J must be in [1,62] for this bit-mask implementation\n";
        return 2;
    }

    pow2v.assign(J + 1, 1);
    pow3v.assign(J + 1, 1);
    for (int i = 1; i <= J; ++i) {
        pow2v[i] = pow2v[i-1] * 2;
        pow3v[i] = pow3v[i-1] * 3;
    }

    Result r = dfs(State{}, 0);
    cout << "J=" << J
         << " leaves=" << r.leaves
         << " hierarchy_ok=" << r.hierarchy_ok << "\n";
    if (r.any) {
        cout << "min_r=" << str128((i128)r.min_r.r)
             << " endpoint=" << str128((i128)r.min_r.y)
             << " z=" << str128(z(r.min_r)) << "\n";
        cout << "min_z_r=" << str128((i128)r.min_z.r)
             << " endpoint=" << str128((i128)r.min_z.y)
             << " z=" << str128(z(r.min_z)) << "\n";
    }
    if (!r.hierarchy_ok)
        cout << "first_bad_prefix_depth=" << r.first_bad_depth << "\n";
}
