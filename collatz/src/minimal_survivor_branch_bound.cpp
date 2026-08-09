#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using boost::multiprecision::cpp_int;

// Memory-light exact solver for
//   mu(K)=min{n>=1: tau_c(n)>K}.
//
// It explores the coefficient-survivor parity tree depth first, always taking
// the smaller canonical-residue child first.  Because child residues are r or
// r+2^k, canonical residue is nondecreasing along every branch.  Once a leaf
// with residue best is found, every node with r>=best can be discarded with no
// loss of correctness.

struct State {
    int k = 0;
    int q = 0;
    cpp_int r = 0;
    cpp_int y = 0;
};

static int K;
static std::vector<cpp_int> pow2v, pow3v;
static std::vector<int> min_q;
static cpp_int best;
static State best_state;
static std::uint64_t nodes = 0, prunes = 0, leaves = 0;
static std::uint64_t max_nodes = 1000000000ULL;

static void dfs(State const& n) {
    if (++nodes > max_nodes) throw 1;
    if (n.r >= best) {
        ++prunes;
        return;
    }

    if (n.k == K) {
        best = n.r;
        best_state = n;
        ++leaves;
        return;
    }

    State child[2];
    int count = 0;
    for (int b = 0; b <= 1; ++b) {
        const int carry = b ^ static_cast<int>((n.y & 1) != 0);
        State t{n.k + 1, n.q, n.r, n.y};

        if (carry) {
            t.r += pow2v[n.k];
            t.y += pow3v[n.q];
        }

        if (b == 0) {
            t.y >>= 1;
        } else {
            t.y = (3 * t.y + 1) >> 1;
            ++t.q;
        }

        if (t.q >= min_q[t.k] && t.r < best)
            child[count++] = std::move(t);
    }

    if (count == 2 && child[1].r < child[0].r)
        std::swap(child[0], child[1]);

    for (int i = 0; i < count; ++i)
        dfs(child[i]);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: minimal_survivor_branch_bound K [max_nodes]\n";
        return 1;
    }
    K = std::stoi(argv[1]);
    if (argc >= 3) max_nodes = std::stoull(argv[2]);
    if (K < 1) return 2;

    pow2v.resize(K + 2);
    pow3v.resize(K + 2);
    min_q.resize(K + 2);
    pow2v[0] = pow3v[0] = 1;
    min_q[0] = 0;

    for (int j = 1; j <= K + 1; ++j) {
        pow2v[j] = 2 * pow2v[j - 1];
        pow3v[j] = 3 * pow3v[j - 1];
        int a = min_q[j - 1];
        while (pow3v[a] < pow2v[j]) ++a;
        min_q[j] = a;
    }

    // 2^K is a harmless initial upper bound on canonical depth-K residues.
    best = pow2v[K];

    try {
        dfs(State{});
    } catch (...) {
        std::cout << "limit,nodes=" << nodes << ",best_so_far=" << best << '\n';
        return 3;
    }

    std::cout << "K=" << K
              << ",mu=" << best
              << ",q=" << best_state.q
              << ",endpoint=" << best_state.y
              << ",nodes=" << nodes
              << ",prunes=" << prunes
              << ",improving_leaves=" << leaves << '\n';
    return 0;
}
