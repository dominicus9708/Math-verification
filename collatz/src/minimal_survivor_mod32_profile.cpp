#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using boost::multiprecision::cpp_int;

// Exact branch profile for the minimal-survivor function
//   mu(K) = min { n >= 1 : tau_c(n) > K }
// of the accelerated Collatz map.
//
// Any survivor beyond depth 5 must have
//   n mod 32 in {7,15,27,31}.
// For one chosen residue a from this set, this program computes the
// branch-restricted function
//   mu_a(K) = min { n == a (mod 32) : tau_c(n) > K }
// for all depths up to the requested K in a single Dijkstra-style traversal.
// The first node popped at each depth has the smallest canonical residue at
// that depth because child residues are r or r+2^k and hence never decrease.

struct Node {
    int k = 0;
    int q = 0;
    cpp_int r = 0;
    cpp_int y = 0;
};

struct ByResidue {
    bool operator()(Node const& a, Node const& b) const {
        if (a.r != b.r) return a.r > b.r;
        if (a.k != b.k) return a.k < b.k;
        return a.q < b.q;
    }
};

static cpp_int Tacc(cpp_int x) {
    if ((x & 1) != 0) return cpp_int((3 * x + 1) / 2);
    return cpp_int(x / 2);
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "usage: minimal_survivor_mod32_profile K residue\n";
        return 1;
    }

    const int K = std::stoi(argv[1]);
    const unsigned long long residue = std::stoull(argv[2]);
    const int allowed[4] = {7,15,27,31};
    bool ok_residue = false;
    for (int a : allowed) if (residue == static_cast<unsigned long long>(a)) ok_residue = true;
    if (!ok_residue || K < 5) {
        std::cerr << "residue must be one of 7,15,27,31 and K >= 5\n";
        return 2;
    }

    std::vector<cpp_int> pow2(K + 2), pow3(K + 2);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= K + 1; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    cpp_int y = residue;
    int q = 0;
    for (int i = 0; i < 5; ++i) {
        if ((y & 1) != 0) ++q;
        y = Tacc(y);
    }

    std::priority_queue<Node, std::vector<Node>, ByResidue> pq;
    pq.push(Node{5, q, cpp_int(residue), y});

    std::vector<bool> seen(K + 1, false);
    cpp_int last = -1;
    std::cout << "K,mu_branch,q,endpoint\n";

    while (!pq.empty()) {
        Node n = pq.top();
        pq.pop();

        if (!seen[n.k]) {
            seen[n.k] = true;
            if (n.r != last) {
                std::cout << n.k << ',' << n.r << ',' << n.q << ',' << n.y << '\n';
                last = n.r;
            }
            if (n.k == K) return 0;
        }

        for (int b = 0; b <= 1; ++b) {
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
            if (pow3[t.q] >= pow2[t.k]) pq.push(std::move(t));
        }
    }

    return 3;
}
