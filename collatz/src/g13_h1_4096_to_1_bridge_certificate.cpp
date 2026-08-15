#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

using boost::multiprecision::cpp_int;

namespace {

constexpr int BLOCK = 19;
constexpr int G13_L = 20026;
constexpr int G13_Q = 12635;
constexpr int OFFSET = 1539;
constexpr int MOD19 = 1 << 19;
constexpr int BEAM = 50;
constexpr long long LEFT_CREDIT = 4096;

struct Rec {
    int residue;
    std::uint64_t correction;
    int mask;
};

struct Node {
    int H;
    long long credit;
    int parent;
    int q;
    int wmask;
    int umask;
};

std::uint64_t local_correction(int mask) {
    std::uint64_t R = 0;
    for (int p = 0; p < BLOCK; ++p) {
        if ((mask >> p) & 1) R = 3 * R + (std::uint64_t{1} << p);
    }
    return R;
}

int local_min_relative_height(int mask, const std::string& ref) {
    int a = 0;
    int b = 0;
    int M = 100;
    for (int i = 0; i < BLOCK; ++i) {
        a += (mask >> i) & 1;
        b += (ref[static_cast<std::size_t>(i)] == '1');
        M = std::min(M, a - b);
    }
    return M;
}

std::vector<int> exact_ceil_alpha_table(int max_t) {
    // ceil(t log_3 2) = least q with 3^q >= 2^t.
    // Equality occurs only at t=0, so all positive comparisons are strict.
    std::vector<int> out(static_cast<std::size_t>(max_t + 1), 0);
    cpp_int p2 = 1;
    cpp_int p3 = 1;
    int q = 0;
    for (int t = 1; t <= max_t; ++t) {
        p2 <<= 1;
        while (p3 < p2) {
            p3 *= 3;
            ++q;
        }
        out[static_cast<std::size_t>(t)] = q;
    }
    return out;
}

cpp_int inverse_mod_power_of_two(cpp_int a, const cpp_int& modulus) {
    // Extended Euclid; a is odd and modulus is a power of two.
    cpp_int t = 0;
    cpp_int newt = 1;
    cpp_int r = modulus;
    cpp_int newr = a % modulus;
    while (newr != 0) {
        const cpp_int q = r / newr;
        cpp_int tmp = t - q * newt;
        t = newt;
        newt = tmp;
        tmp = r - q * newr;
        r = newr;
        newr = tmp;
    }
    assert(r == 1);
    t %= modulus;
    if (t < 0) t += modulus;
    return t;
}

cpp_int mod_positive(cpp_int x, const cpp_int& m) {
    x %= m;
    if (x < 0) x += m;
    return x;
}

}  // namespace

int main() {
    // ------------------------------------------------------------------
    // 1. Exact R1 mechanical phase and the internal G13 segment.
    // ------------------------------------------------------------------
    const auto ceil_alpha = exact_ceil_alpha_table(OFFSET + G13_L);
    std::string W;
    W.reserve(G13_L);
    for (int i = 0; i < G13_L; ++i) {
        const int bit =
            ceil_alpha[static_cast<std::size_t>(OFFSET + i + 1)] -
            ceil_alpha[static_cast<std::size_t>(OFFSET + i)];
        assert(bit == 0 || bit == 1);
        W.push_back(static_cast<char>('0' + bit));
    }
    assert(static_cast<int>(std::count(W.begin(), W.end(), '1')) == G13_Q);

    std::vector<std::string> blocks;
    for (int b = 0; b < G13_L / BLOCK; ++b) {
        blocks.push_back(W.substr(static_cast<std::size_t>(BLOCK * b), BLOCK));
    }
    assert(blocks.size() == 1054);

    std::vector<int> type0_positions;
    for (int b = 0; b < static_cast<int>(blocks.size()); ++b) {
        if (std::count(blocks[b].begin(), blocks[b].end(), '1') == 11) {
            type0_positions.push_back(b);
        }
    }
    const std::vector<int> expected_type0{
        0,81,162,243,324,405,486,567,648,729,810,891,972
    };
    assert(type0_positions == expected_type0);

    // ------------------------------------------------------------------
    // 2. Fixed-q local correction tables and survival fibres for H=0,1.
    // ------------------------------------------------------------------
    std::vector<std::vector<Rec>> byq(20);
    std::vector<std::vector<int>> residue_index(20, std::vector<int>(MOD19, -1));

    for (int mask = 0; mask < MOD19; ++mask) {
        const int q = __builtin_popcount(static_cast<unsigned>(mask));
        if (q < 8 || q > 15) continue;
        const std::uint64_t R = local_correction(mask);
        const int residue = static_cast<int>(R & (MOD19 - 1));
        assert(residue_index[q][residue] == -1);  // fixed-q injectivity
        residue_index[q][residue] = static_cast<int>(byq[q].size());
        byq[q].push_back({residue, R, mask});
    }

    std::map<std::string, int> ref_id;
    std::vector<std::string> refs;
    for (const auto& r : blocks) {
        if (!ref_id.count(r)) {
            const int id = static_cast<int>(refs.size());
            ref_id[r] = id;
            refs.push_back(r);
        }
    }
    assert(refs.size() == 20);

    using IndexList = std::vector<int>;
    std::vector<std::vector<std::vector<IndexList>>> admissible(
        refs.size(), std::vector<std::vector<IndexList>>(2, std::vector<IndexList>(20)));
    std::vector<std::vector<std::vector<std::vector<char>>>> allowed(
        refs.size(),
        std::vector<std::vector<std::vector<char>>>(2, std::vector<std::vector<char>>(20)));

    for (int ri = 0; ri < static_cast<int>(refs.size()); ++ri) {
        for (int H = 0; H <= 1; ++H) {
            for (int q = 8; q <= 15; ++q) {
                allowed[ri][H][q].assign(byq[q].size(), 0);
                for (int j = 0; j < static_cast<int>(byq[q].size()); ++j) {
                    if (local_min_relative_height(byq[q][j].mask, refs[ri]) >= -H) {
                        admissible[ri][H][q].push_back(j);
                        allowed[ri][H][q][j] = 1;
                    }
                }
            }
        }
    }

    std::array<std::uint64_t, 20> p3{};
    p3[0] = 1;
    for (int q = 1; q < 20; ++q) p3[q] = 3 * p3[q - 1];

    // ------------------------------------------------------------------
    // 3. Construct one exact 4096 -> 1 witness.
    //
    // The beam is only a witness finder.  Once found, the path is verified
    // independently below, so no nonexistence statement depends on pruning.
    // ------------------------------------------------------------------
    std::vector<std::vector<Node>> layers;
    layers.push_back({{0, LEFT_CREDIT, -1, -1, -1, -1}});

    for (int bi = 0; bi < static_cast<int>(blocks.size()); ++bi) {
        const auto& prev = layers.back();
        const std::string& ref = blocks[bi];
        const int ri = ref_id[ref];
        const int qref = static_cast<int>(std::count(ref.begin(), ref.end(), '1'));

        std::map<std::pair<int,long long>, Node> next_by_state;

        for (int pi = 0; pi < static_cast<int>(prev.size()); ++pi) {
            const Node s = prev[pi];
            for (int q = 8; q <= 15; ++q) {
                const int H2 = s.H + q - qref;
                if (H2 < 0 || H2 > 1) continue;

                const std::uint64_t shift = static_cast<std::uint64_t>(
                    (static_cast<unsigned __int128>(p3[q] % MOD19) *
                     static_cast<std::uint64_t>(s.credit % MOD19)) % MOD19);
                const __int128 A = static_cast<__int128>(p3[q]) * s.credit;

                for (const int wi : admissible[ri][s.H][q]) {
                    const Rec& w = byq[q][wi];
                    const int wanted = (w.residue + static_cast<int>(shift)) & (MOD19 - 1);
                    const int ui = residue_index[q][wanted];
                    if (ui < 0 || !allowed[ri][s.H][q][ui]) continue;
                    const Rec& u = byq[q][ui];

                    const __int128 numerator = A -
                        (static_cast<__int128>(u.correction) - w.correction);
                    assert(numerator % MOD19 == 0);
                    const long long right = static_cast<long long>(numerator / MOD19);
                    if (right <= 0) continue;

                    const std::pair<int,long long> key{H2, right};
                    if (!next_by_state.count(key)) {
                        next_by_state[key] = {H2, right, pi, q, w.mask, u.mask};
                    }
                }
            }
        }

        std::vector<Node> next;
        for (int H = 0; H <= 1; ++H) {
            std::vector<Node> bucket;
            for (const auto& kv : next_by_state) {
                if (kv.second.H == H) bucket.push_back(kv.second);
            }
            std::sort(bucket.begin(), bucket.end(),
                      [](const Node& a, const Node& b) { return a.credit < b.credit; });
            if (static_cast<int>(bucket.size()) > BEAM) bucket.resize(BEAM);
            next.insert(next.end(), bucket.begin(), bucket.end());
        }
        assert(!next.empty());
        layers.push_back(std::move(next));
    }

    int pick = -1;
    for (int i = 0; i < static_cast<int>(layers.back().size()); ++i) {
        if (layers.back()[i].H == 0 && layers.back()[i].credit == 1) {
            pick = i;
            break;
        }
    }
    assert(pick >= 0);

    std::vector<Node> witness(blocks.size());
    for (int b = static_cast<int>(blocks.size()); b >= 1; --b) {
        witness[static_cast<std::size_t>(b - 1)] = layers[b][pick];
        pick = layers[b][pick].parent;
    }

    // ------------------------------------------------------------------
    // 4. Independent local/global verification of the constructed path.
    // ------------------------------------------------------------------
    int H = 0;
    long long credit = LEFT_CREDIT;
    int total_q = 0;
    int global_height_w = 0;
    int global_height_u = 0;
    int global_min_w = 0;
    int global_min_u = 0;

    cpp_int Rw = 0;
    cpp_int Ru = 0;

    for (int b = 0; b < static_cast<int>(blocks.size()); ++b) {
        const Node& n = witness[static_cast<std::size_t>(b)];
        const std::string& ref = blocks[b];
        const int qref = static_cast<int>(std::count(ref.begin(), ref.end(), '1'));

        assert(__builtin_popcount(static_cast<unsigned>(n.wmask)) == n.q);
        assert(__builtin_popcount(static_cast<unsigned>(n.umask)) == n.q);
        assert(local_min_relative_height(n.wmask, ref) >= -H);
        assert(local_min_relative_height(n.umask, ref) >= -H);

        const int H2 = H + n.q - qref;
        assert(H2 == n.H && H2 >= 0 && H2 <= 1);

        const std::uint64_t rw = local_correction(n.wmask);
        const std::uint64_t ru = local_correction(n.umask);
        const __int128 num = static_cast<__int128>(p3[n.q]) * credit -
            (static_cast<__int128>(ru) - rw);
        assert(num % MOD19 == 0);
        const long long next_credit = static_cast<long long>(num / MOD19);
        assert(next_credit == n.credit && next_credit > 0);

        const int shift = BLOCK * b;
        Rw = boost::multiprecision::pow(cpp_int(3), n.q) * Rw + (cpp_int(1) << shift) * rw;
        Ru = boost::multiprecision::pow(cpp_int(3), n.q) * Ru + (cpp_int(1) << shift) * ru;
        total_q += n.q;

        for (int i = 0; i < BLOCK; ++i) {
            const int mech_bit = ref[static_cast<std::size_t>(i)] - '0';
            global_height_w += ((n.wmask >> i) & 1) - mech_bit;
            global_height_u += ((n.umask >> i) & 1) - mech_bit;
            global_min_w = std::min(global_min_w, global_height_w);
            global_min_u = std::min(global_min_u, global_height_u);
        }

        H = H2;
        credit = next_credit;
    }

    assert(total_q == G13_Q);
    assert(H == 0 && credit == 1);
    assert(global_height_w == 0 && global_height_u == 0);
    assert(global_min_w >= 0 && global_min_u >= 0);

    const cpp_int lhs = boost::multiprecision::pow(cpp_int(3), G13_Q) * LEFT_CREDIT -
        (Ru - Rw);
    const cpp_int rhs = cpp_int(1) << G13_L;
    assert(lhs == rhs);

    // ------------------------------------------------------------------
    // 5. Canonical G13 start representative and finite-natural obstruction.
    // ------------------------------------------------------------------
    const cpp_int modulus = cpp_int(1) << G13_L;
    const cpp_int a = boost::multiprecision::powm(cpp_int(3), G13_Q, modulus);
    const cpp_int inv = inverse_mod_power_of_two(a, modulus);

    const cpp_int rho_w = mod_positive(-inv * Rw, modulus);
    const cpp_int rho_u = mod_positive(-inv * Ru, modulus);
    assert(mod_positive(rho_u - rho_w, modulus) == modulus - LEFT_CREDIT);

    const unsigned bitlen_w = static_cast<unsigned>(boost::multiprecision::msb(rho_w) + 1);
    const unsigned bitlen_u = static_cast<unsigned>(boost::multiprecision::msb(rho_u) + 1);
    assert(bitlen_w == 20024);
    assert(bitlen_u == 20024);

    // Current R1 starts obey N < 2^73.  Since T(x) <= 2x for positive x,
    // the ordinary state at time 1539 is < 2^(1539+73)=2^1612.
    const cpp_int gate_start_ceiling = cpp_int(1) << 1612;
    assert(rho_w >= gate_start_ceiling);
    assert(rho_u >= gate_start_ceiling);

    std::cout << "G13 H<=1 4096->1 witness: PASS\n";
    std::cout << "offset=" << OFFSET << " L=" << G13_L << " q=" << total_q << "\n";
    std::cout << "global_min_heights=" << global_min_w << "," << global_min_u << "\n";
    std::cout << "canonical_bitlengths=" << bitlen_w << "," << bitlen_u << "\n";
    std::cout << "R1_gate_start_required_bitlength<=1612: witness FAILS finite-natural condition\n";

    return 0;
}
