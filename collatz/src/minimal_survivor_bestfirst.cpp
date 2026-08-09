#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using boost::multiprecision::cpp_int;

// Exact minimal-survivor solver for the accelerated Collatz map
//   T(n)=n/2       (n even)
//   T(n)=(3n+1)/2  (n odd).
//
// Define tau_c(n) as the first k>=1 for which 3^{q_k}<2^k, where q_k is
// the number of odd entries among n,T(n),...,T^{k-1}(n).  This program finds
//
//   mu(K) = min { n>=1 : tau_c(n) > K }.
//
// A parity prefix of length k has a unique canonical starting residue r mod
// 2^k.  Each child residue is either r or r+2^k, hence every descendant has
// canonical residue >= r.  Consequently the first depth-K node removed from
// a priority queue ordered by r is exactly the minimum depth-K survivor.
// No probabilistic, dominance, or finite-lookahead assumption is used.

struct Node {
    int k = 0;
    int q = 0;
    cpp_int r = 0;  // canonical residue modulo 2^k
    cpp_int y = 0;  // T^k(r)
};

struct ByResidue {
    bool operator()(Node const& a, Node const& b) const {
        if (a.r != b.r) return a.r > b.r;  // min-heap
        // For equal residue, follow its deterministic continuation first.
        if (a.k != b.k) return a.k < b.k;
        return a.q < b.q;
    }
};

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: minimal_survivor_bestfirst K [max_popped]\n";
        return 1;
    }

    const int K = std::stoi(argv[1]);
    const std::uint64_t max_popped =
        (argc >= 3 ? std::stoull(argv[2]) : 100000000ULL);
    if (K < 1) {
        std::cerr << "K must be positive\n";
        return 2;
    }

    std::vector<cpp_int> pow2(K + 2), pow3(K + 2);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K + 1; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::priority_queue<Node, std::vector<Node>, ByResidue> pq;
    pq.push(Node{});

    std::uint64_t popped = 0, pushed = 1;
    while (!pq.empty()) {
        Node n = pq.top();
        pq.pop();
        ++popped;

        if (popped > max_popped) {
            std::cout << "limit,popped=" << popped
                      << ",queued=" << pq.size() << '\n';
            return 3;
        }

        if (n.k == K) {
            std::cout << "K=" << K
                      << ",mu=" << n.r
                      << ",q=" << n.q
                      << ",endpoint=" << n.y
                      << ",popped=" << popped
                      << ",queued=" << pq.size()
                      << ",pushed=" << pushed << '\n';
            return 0;
        }

        for (int b = 0; b <= 1; ++b) {
            // The two lifts r and r+2^k have time-k endpoints differing by
            // 3^q, hence opposite parity.  carry selects the unique lift whose
            // next parity bit is b.
            const int carry = b ^ static_cast<int>((n.y & 1) != 0);

            Node t = n;
            if (carry) {
                t.r += pow2[n.k];
                t.y += pow3[n.q];
            }

            ++t.k;
            if (b == 0) {
                t.y >>= 1;
            } else {
                t.y = (3 * t.y + 1) >> 1;
                ++t.q;
            }

            // Keep only prefixes that have not yet undergone coefficient
            // contraction.
            if (pow3[t.q] >= pow2[t.k]) {
                pq.push(std::move(t));
                ++pushed;
            }
        }
    }

    std::cout << "no survivor at depth " << K << '\n';
    return 4;
}
