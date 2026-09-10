// MATH-056 exact min-plus first-cell value-frontier certificate.
//
// Scope
// -----
// For length-72 coefficient-valid parity prefixes, minimize the exact first-72
// slack penalty among ordinary starts in the current first-cell window
//
//     2^71 < N < 1364*2^61
//
// whose same ordinary integer remains coefficient-valid through depth K.
//
// If q,d are the odd/even counts before an odd step at position k and
// u=m(q)-d with m(q)=floor(q log_2(3/2)), then
//
//   p(q,u) = (1-2^-u) Omega_q / 3,
//   Omega_q = 2^(q+m(q))/3^q.
//
// With common denominator 3^72 the odd-step cost is the exact integer
//
//   w_72(k,q,u) = (2^u-1) 2^k 3^(71-q).
//
// All edge costs are nonnegative. Therefore a priority queue ordered by the
// accumulated exact integer cost is an exact Dijkstra/min-plus search: the first
// terminal prefix satisfying the address and same-integer coefficient conditions
// is the global minimum. No floating-point comparison is used for the search.
//
// Audited targets in the accompanying ledger: K=195,265,300.
// Finite exact computation only. Collatz conjecture remains OPEN.

#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using u128 = unsigned __int128;
using u256 = boost::multiprecision::uint256_t;
using boost::multiprecision::cpp_int;

static u128 P2[128], P3[128];
static u256 P3_256[128];

static int mfun(int q) {
    int d = 0;
    while (P3[q] > P2[q + d + 1]) ++d;
    return d;
}

static string dec128(u128 x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    reverse(s.begin(), s.end());
    return s;
}

static u128 inv_odd_mod2_128(u128 a) {
    // Newton iteration for an odd inverse modulo 2^128.
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x *= 2 - a * x;
    return x;
}

struct Node {
    u256 cost;
    u128 C;
    u128 mask;
    uint8_t pos, q, d;
};
struct GreaterCost {
    bool operator()(Node const& a, Node const& b) const {
        return a.cost > b.cost;
    }
};

static bool coefficient_survives_same_integer(u128 N, int K) {
    cpp_int n = (uint64_t)(N >> 64);
    n <<= 64;
    n += (uint64_t)N;
    cpp_int p3 = 1, p2 = 1;
    int q = 0;
    for (int pos = 0; pos < K; ++pos) {
        if ((n & 1) != 0) {
            n = (3 * n + 1) / 2;
            ++q;
            p3 *= 3;
        } else {
            n /= 2;
        }
        p2 <<= 1;
        if (p3 <= p2) return false;
    }
    return true;
}

struct Answer {
    u256 cost;
    u128 N;
    u128 mask;
    size_t pops;
};

static Answer solve(int K) {
    priority_queue<Node, vector<Node>, GreaterCost> pq;
    pq.push({0, 0, 0, 0, 0, 0});

    const u128 MODMASK = ((u128)1 << 72) - 1;
    const u128 LO = (u128)1 << 71;
    const u128 HI = (u128)1364 << 61;
    size_t pops = 0;

    while (!pq.empty()) {
        Node s = pq.top();
        pq.pop();
        ++pops;

        if (s.pos == 72) {
            u128 a = P3[s.q] & MODMASK;
            u128 inv = inv_odd_mod2_128(a) & MODMASK;
            u128 N = ((u128)(0 - s.C) * inv) & MODMASK;
            if (!(LO < N && N < HI)) continue;
            if (coefficient_survives_same_integer(N, K))
                return {s.cost, N, s.mask, pops};
            continue;
        }

        int pos = s.pos, q = s.q, d = s.d;
        int u = mfun(q) - d;

        // Odd child.
        if (d <= mfun(q + 1)) {
            u256 w = 0;
            if (u > 0)
                w = ((u256(1) << u) - 1)
                  * (u256(1) << pos)
                  * P3_256[71 - q];
            pq.push({s.cost + w,
                     3 * s.C + ((u128)1 << pos),
                     s.mask | ((u128)1 << pos),
                     (uint8_t)(pos + 1),
                     (uint8_t)(q + 1),
                     (uint8_t)d});
        }

        // Even child.
        if (d + 1 <= mfun(q))
            pq.push({s.cost, s.C, s.mask,
                     (uint8_t)(pos + 1), (uint8_t)q, (uint8_t)(d + 1)});
    }

    throw runtime_error("no admissible terminal state");
}

int main(int argc, char** argv) {
    P2[0] = P3[0] = 1;
    P3_256[0] = 1;
    for (int i = 1; i < 128; ++i) {
        P2[i] = P2[i - 1] * 2;
        P3[i] = P3[i - 1] * 3;
        P3_256[i] = P3_256[i - 1] * 3;
    }

    int K = argc > 1 ? stoi(argv[1]) : 195;
    if (K < 72) {
        cerr << "K must be >=72\n";
        return 2;
    }

    auto ans = solve(K);
    cout << "K " << K
         << " cost_over_3pow72 " << ans.cost
         << " N " << dec128(ans.N)
         << " address " << (unsigned long long)(ans.N >> 61)
         << " pops " << ans.pops << '\n';

    int q = 0, d = 0;
    cout << "positive_slack_events";
    for (int pos = 0; pos < 72; ++pos) {
        int u = mfun(q) - d;
        bool odd = ((ans.mask >> pos) & 1) != 0;
        if (odd) {
            if (u > 0) cout << ' ' << pos << ':' << q << ':' << u;
            ++q;
        } else {
            ++d;
        }
    }
    cout << '\n';
}
