#include <boost/multiprecision/cpp_int.hpp>

#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <tuple>
#include <vector>

using boost::multiprecision::cpp_int;

// Exact diagnostic for the Collatz proof program.
//
// It computes, simultaneously for every 1 <= h <= H,
//
//   mu_L7(h) = min rho_h(w),
//
// over parity prefixes w which satisfy
//
//   (1) coefficient survival 3^{q_j} >= 2^j at every j <= h, and
//   (2) every completed aligned seven-step block is the maximum-correction
//       representative of its full-Hensel residue class.
//
// This is a finite exact calculation, not an asymptotic proof.
//
// Every parity prefix has one canonical starting residue r mod 2^k.  On
// extension its child residue is r or r+2^k, so r is nondecreasing along every
// branch.  Therefore, in a global priority queue ordered by r, the first node
// popped at a given depth k has the exact minimum canonical residue at that
// depth.  The parent of every as-yet-uncreated node must be popped first and
// has no larger residue, so an uncreated smaller depth-k node cannot be hidden
// behind a larger queue key.

static std::array<bool, 128> build_l7_allowed() {
    struct Key {
        int q;
        long long rem;
        bool operator<(Key const& o) const {
            return std::tie(q, rem) < std::tie(o.q, o.rem);
        }
    };

    long long pow3[8];
    pow3[0] = 1;
    for (int i = 1; i <= 7; ++i) pow3[i] = 3 * pow3[i - 1];

    std::map<Key, long long> max_correction;
    std::array<std::pair<int, long long>, 128> qr{};

    for (int mask = 0; mask < 128; ++mask) {
        int q = 0;
        long long R = 0;
        for (int i = 0; i < 7; ++i) {
            if ((mask >> i) & 1) {
                R = 3 * R + (1LL << i);
                ++q;
            }
        }

        qr[mask] = {q, R};
        Key key{q, R % pow3[q]};
        auto it = max_correction.find(key);
        if (it == max_correction.end() || R > it->second)
            max_correction[key] = R;
    }

    std::array<bool, 128> allowed{};
    int total = 0;
    int by_q[8] = {};

    for (int mask = 0; mask < 128; ++mask) {
        const auto [q, R] = qr[mask];
        Key key{q, R % pow3[q]};
        allowed[mask] = (R == max_correction[key]);
        if (allowed[mask]) {
            ++total;
            ++by_q[q];
        }
    }

    // Independent regression against the exact L7 theorem.
    const int expected[8] = {1, 2, 6, 15, 21, 16, 7, 1};
    if (total != 69) throw std::runtime_error("L7 total-count regression");
    for (int q = 0; q <= 7; ++q)
        if (by_q[q] != expected[q])
            throw std::runtime_error("L7 q-count regression");

    std::cerr << "L7_allowed=69 counts=1,2,6,15,21,16,7,1\n";
    return allowed;
}

struct Node {
    int k = 0;
    int q = 0;
    cpp_int r = 0;  // canonical start mod 2^k
    cpp_int y = 0;  // T^k(r)
    unsigned char block = 0;
    int block_len = 0;
};

struct ByResidue {
    bool operator()(Node const& a, Node const& b) const {
        if (a.r != b.r) return a.r > b.r;
        // For equal canonical residue, advance the deeper deterministic prefix
        // first; this affects performance only, not correctness.
        if (a.k != b.k) return a.k < b.k;
        return a.q < b.q;
    }
};

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: l7_minimal_formation_floor_bestfirst H [max_popped]\n";
        return 1;
    }

    const int H = std::stoi(argv[1]);
    const std::uint64_t max_popped =
        (argc >= 3 ? std::stoull(argv[2]) : 100000000ULL);
    if (H < 1) return 2;

    const auto allowed = build_l7_allowed();

    std::vector<cpp_int> pow2(H + 2), pow3(H + 2);
    pow2[0] = pow3[0] = 1;
    for (int i = 1; i <= H + 1; ++i) {
        pow2[i] = 2 * pow2[i - 1];
        pow3[i] = 3 * pow3[i - 1];
    }

    std::priority_queue<Node, std::vector<Node>, ByResidue> pq;
    pq.push(Node{});

    std::vector<char> seen(H + 1, 0);
    int found_depths = 0;
    std::uint64_t popped = 0;
    std::uint64_t pushed = 1;

    while (!pq.empty() && found_depths < H) {
        Node n = pq.top();
        pq.pop();

        if (++popped > max_popped) {
            std::cerr << "limit,popped=" << popped
                      << ",queued=" << pq.size() << '\n';
            return 3;
        }

        if (n.k > 0 && !seen[n.k]) {
            seen[n.k] = 1;
            ++found_depths;
            std::cout << n.k << ',' << n.r << ',' << n.q << ',' << n.y << '\n';
        }

        if (n.k == H) continue;

        for (int b = 0; b <= 1; ++b) {
            // The two lifts r and r+2^k have time-k endpoints differing by
            // 3^q, hence opposite parity.  carry is the new binary digit of
            // the canonical start which selects desired next parity b.
            const int carry = b ^ static_cast<int>((n.y & 1) != 0);

            Node t = n;
            if (carry) {
                t.r += pow2[n.k];
                t.y += pow3[n.q];
            }

            t.block |= static_cast<unsigned char>(b << t.block_len);
            ++t.block_len;
            ++t.k;

            if (b == 0) {
                t.y >>= 1;
            } else {
                t.y = (3 * t.y + 1) >> 1;
                ++t.q;
            }

            if (pow3[t.q] < pow2[t.k]) continue;

            // Impose the exact L7 rule as soon as an aligned block closes.
            // An unfinished terminal block is left unconstrained, exactly as
            // in a finite horizon with only completed aligned L7 blocks.
            if (t.block_len == 7) {
                if (!allowed[t.block]) continue;
                t.block = 0;
                t.block_len = 0;
            }

            pq.push(std::move(t));
            ++pushed;
        }
    }

    std::cerr << "popped=" << popped
              << ",pushed=" << pushed
              << ",found_depths=" << found_depths
              << ",queued=" << pq.size() << '\n';

    return (found_depths == H ? 0 : 4);
}
