#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using boost::multiprecision::cpp_int;

// Exact best-first solver for the generalized coefficient-survivor profile
//
//   mu_{s,h}(J) = min { x>=1 : q_j(x) >= b_{s+j}-b_s-h for all 1<=j<=J },
//
// where b_k is the least q with 3^q >= 2^k.
//
// s is the mechanical phase offset and h is an already accumulated odd-count
// surplus.  The ordinary minimal-survivor function is mu_{0,0}(J).
//
// This is the natural state produced by the exact five-step decomposition:
// after a block with q odd steps,
//
//   h' = h + q - (b_{s+5}-b_s).
//
// Child canonical representatives are r or r+2^k, so residue cost never
// decreases and Dijkstra/best-first order is exact.

struct Node {
    int k = 0;
    int q = 0;
    cpp_int r = 1;  // least positive representative of the current cylinder
    cpp_int y = 1;  // endpoint obtained from r after k steps
};

struct ByResidue {
    bool operator()(Node const& a, Node const& b) const {
        if (a.r != b.r) return a.r > b.r;
        if (a.k != b.k) return a.k < b.k;
        return a.q < b.q;
    }
};

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "usage: phase_height_minimal_survivor s h J\n";
        return 1;
    }

    const int s = std::stoi(argv[1]);
    const int h = std::stoi(argv[2]);
    const int J = std::stoi(argv[3]);
    if (s < 0 || h < 0 || J < 0) return 2;

    const int M = s + J + 2;
    std::vector<cpp_int> p2(M + 1), p3(M + 1);
    p2[0] = p3[0] = 1;
    for (int i = 1; i <= M; ++i) {
        p2[i] = 2 * p2[i - 1];
        p3[i] = 3 * p3[i - 1];
    }

    std::vector<int> barrier(M + 1, 0);
    cpp_int cur3 = 1;
    int b = 0;
    for (int j = 1; j <= M; ++j) {
        while (cur3 < p2[j]) {
            cur3 *= 3;
            ++b;
        }
        barrier[j] = b;
    }

    std::priority_queue<Node, std::vector<Node>, ByResidue> pq;
    pq.push(Node{});

    std::vector<char> seen(J + 1, 0);
    std::vector<cpp_int> mu(J + 1);
    cpp_int last = -1;

    std::cout << "J,mu_phase_height\n";

    while (!pq.empty()) {
        Node n = pq.top();
        pq.pop();

        if (!seen[n.k]) {
            seen[n.k] = 1;
            mu[n.k] = n.r;
            if (n.r != last) {
                std::cout << n.k << ',' << n.r << '\n';
                last = n.r;
            }
            if (n.k == J) return 0;
        }

        if (n.k == J) continue;

        for (int bit = 0; bit <= 1; ++bit) {
            const int carry = bit ^ static_cast<int>((n.y & 1) != 0);
            Node t = n;
            if (carry) {
                t.r += p2[n.k];
                t.y += p3[n.q];
            }

            ++t.k;
            if (bit == 0) {
                t.y >>= 1;
            } else {
                t.y = (3 * t.y + 1) >> 1;
                ++t.q;
            }

            const int required = barrier[s + t.k] - barrier[s] - h;
            if (t.q >= required) pq.push(std::move(t));
        }
    }

    return 3;
}
