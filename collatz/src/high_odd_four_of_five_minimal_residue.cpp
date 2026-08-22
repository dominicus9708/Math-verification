#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using boost::multiprecision::cpp_int;

// Exact best-first diagnostic for the sublanguage in which every aligned
// five-step block contains at least four odd steps.
//
// The canonical residue r is monotone under parity-cylinder refinement, so the
// first popped node at each depth has the least positive canonical start among
// all prefixes satisfying the block constraint.
//
// This finite certificate does not prove that the profile diverges and does not
// prove the Collatz conjecture.

struct Node {
    int k = 0;
    int q = 0;
    int block_q = 0;
    cpp_int r = 1;
    cpp_int y = 1;
};

struct ByResidue {
    bool operator()(Node const& a, Node const& b) const {
        if (a.r != b.r) return a.r > b.r;
        if (a.k != b.k) return a.k < b.k;
        return a.q < b.q;
    }
};

std::map<int, cpp_int> profile(int K) {
    std::vector<cpp_int> p2(K + 1), p3(K + 1);
    p2[0] = p3[0] = 1;
    for (int i = 1; i <= K; ++i) {
        p2[i] = 2 * p2[i - 1];
        p3[i] = 3 * p3[i - 1];
    }

    std::priority_queue<Node, std::vector<Node>, ByResidue> pq;
    pq.push(Node{});

    std::vector<char> seen(K + 1, 0);
    std::map<int, cpp_int> out;

    while (!pq.empty()) {
        Node n = pq.top();
        pq.pop();

        if (!seen[n.k]) {
            seen[n.k] = 1;
            if (n.k > 0 && n.k % 5 == 0) out[n.k] = n.r;
            if (n.k == K) break;
        }

        if (n.k == K) continue;

        for (int bit = 0; bit <= 1; ++bit) {
            Node t = n;
            const int carry = bit ^ static_cast<int>((n.y & 1) != 0);
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
                ++t.block_q;
            }

            const int pos = t.k % 5;
            if (pos == 0) {
                if (t.block_q < 4) continue;
                t.block_q = 0;
            } else {
                const int remaining = 5 - pos;
                if (t.block_q + remaining < 4) continue;
            }

            pq.push(std::move(t));
        }
    }

    return out;
}

int main(int argc, char** argv) {
    const int K = argc >= 2 ? std::stoi(argv[1]) : 75;
    if (K <= 0 || K % 5 != 0) {
        std::cerr << "usage: high_odd_four_of_five_minimal_residue [K multiple of 5]\n";
        return 1;
    }

    const auto got = profile(K);
    for (const auto& [k, value] : got) {
        std::cout << k << ',' << value << '\n';
    }

    if (K == 75) {
        const std::map<int, cpp_int> expected{
            {5, 7},
            {10, 27},
            {15, 111},
            {20, 111},
            {25, 4591},
            {30, 4591},
            {35, 4591},
            {40, 1509545},
            {45, 6574831},
            {50, 8555497},
            {55, 60533863},
            {60, 180121343},
            {65, cpp_int("3994690279")},
            {70, cpp_int("34406735401")},
            {75, cpp_int("129821427871")},
        };

        if (got != expected) {
            std::cerr << "four-of-five profile selfcheck mismatch\n";
            return 2;
        }
        std::cout << "high-density 4-of-5 block minimal-residue selfcheck: PASS\n";
    }

    return 0;
}
