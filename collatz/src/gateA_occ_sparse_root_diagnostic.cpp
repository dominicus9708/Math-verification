#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

struct State {
    u64 R = 0;
    std::uint8_t q = 0;
};

static std::array<u64, 40> P3{};

inline u64 keyc(int q, u64 R) {
    return (u64(q) << 56) | (R % P3[q]);
}

int boundary(int k) {
    int q = 0;
    while (P3[q] < (1ULL << k)) ++q;
    return q;
}

void scan_all_endpoint_words(
    int pos,
    int k,
    int q,
    u64 R,
    int qmin,
    std::unordered_map<u64, u64>& maxima
) {
    if (q + (k - pos) < qmin) return;

    if (pos == k) {
        auto it = maxima.find(keyc(q, R));
        if (it != maxima.end() && R > it->second) it->second = R;
        return;
    }

    scan_all_endpoint_words(pos + 1, k, q, R, qmin, maxima);
    scan_all_endpoint_words(
        pos + 1,
        k,
        q + 1,
        3 * R + (1ULL << pos),
        qmin,
        maxima
    );
}

void run_case(int m) {
    int H = 0;
    int max_root_depth = 0;
    std::vector<std::pair<int, int>> sparse_blocks;

    if (m == 16) {
        H = 28;
        max_root_depth = 21;
        sparse_blocks = {{21, 27}};
    } else if (m == 18) {
        H = 32;
        max_root_depth = 24;
        sparse_blocks = {{21, 27}, {24, 29}};
    } else {
        std::cerr << "supported cases: m=16 or m=18\n";
        std::exit(2);
    }

    const u64 total = 1ULL << m;
    const int stride = H + 1;

    std::vector<State> states(total * stride);
    std::vector<std::uint8_t> coeff_alive(total * stride, 0);
    std::vector<std::uint8_t> root_alive(total * stride, 0);
    std::vector<u64> parity_bits(total, 0);

    auto at = [stride](u64 atom, int k) -> std::size_t {
        return std::size_t(atom) * stride + k;
    };

    for (u64 mask = 0; mask < total; ++mask) {
        u64 X = P3[m];
        for (int i = 0; i < m; ++i) {
            if ((mask >> i) & 1ULL) X += P3[i];
        }

        u128 n = u128(4) * X + 3;
        State s{};
        coeff_alive[at(mask, 0)] = 1;
        root_alive[at(mask, 0)] = 1;

        for (int k = 1; k <= H; ++k) {
            const int bit = int(n & 1);
            if (bit) {
                n = (3 * n + 1) / 2;
                s.R = 3 * s.R + (1ULL << (k - 1));
                ++s.q;
                parity_bits[mask] |= 1ULL << (k - 1);
            } else {
                n /= 2;
            }

            states[at(mask, k)] = s;
            coeff_alive[at(mask, k)] =
                coeff_alive[at(mask, k - 1)] &&
                P3[s.q] >= (1ULL << k);
        }
    }

    for (int k = 1; k <= max_root_depth; ++k) {
        std::unordered_map<u64, u64> maxima;
        maxima.reserve(total / 2);

        for (u64 atom = 0; atom < total; ++atom) {
            if (!coeff_alive[at(atom, k)]) continue;
            const State s = states[at(atom, k)];
            const u64 key = keyc(s.q, s.R);
            auto [it, inserted] = maxima.emplace(key, s.R);
            if (!inserted && s.R > it->second) it->second = s.R;
        }

        scan_all_endpoint_words(0, k, 0, 0, boundary(k), maxima);

        u64 alive_count = 0;
        for (u64 atom = 0; atom < total; ++atom) {
            if (!root_alive[at(atom, k - 1)] || !coeff_alive[at(atom, k)]) {
                root_alive[at(atom, k)] = 0;
                continue;
            }

            const State s = states[at(atom, k)];
            const auto it = maxima.find(keyc(s.q, s.R));
            root_alive[at(atom, k)] =
                it != maxima.end() && it->second == s.R;
            alive_count += root_alive[at(atom, k)];
        }

        if (k >= 10) {
            std::cout << "ROOT_DEPTH " << k
                      << " selector_atoms " << alive_count
                      << " queried_keys " << maxima.size()
                      << "\n";
        }
    }

    std::cout << std::setprecision(18);

    for (auto [a, c] : sparse_blocks) {
        const int L = c - a;
        const int rises = boundary(c) - boundary(a);
        long double in = 0;
        long double full = 0;
        long double valid = 0;
        u64 parents = 0;

        for (u64 atom = 0; atom < total; ++atom) {
            if (!root_alive[at(atom, a)]) continue;

            const State s = states[at(atom, a)];
            const int d = int(s.q) - boundary(a);
            const u64 word =
                (parity_bits[atom] >> a) & ((1ULL << L) - 1);
            const int ones = __builtin_popcountll(word);

            const long double omega = std::powl(1.5L, d);
            const long double g = std::powl(1.5L, ones - rises);

            in += omega;
            full += omega * g;
            if (coeff_alive[at(atom, c)]) valid += omega * g;
            ++parents;
        }

        const long double sigma =
            std::powl(1.25L, L) / std::powl(1.5L, rises);

        std::cout << "ROOT_SPARSE_BLOCK " << a << "->" << c
                  << " m " << m
                  << " parents " << parents
                  << " sigma " << sigma
                  << " full_selector_upper_ratio " << full / in
                  << " coefficient_valid_ratio " << valid / in
                  << " signed_phi " << (full / in) / sigma - 1
                  << "\n";
    }

    std::cout << "FINITE_ROOT_DIAGNOSTIC_ONLY\n";
}

int main(int argc, char** argv) {
    P3[0] = 1;
    for (int i = 1; i < (int)P3.size(); ++i) P3[i] = P3[i - 1] * 3ULL;

    const int m = argc > 1 ? std::atoi(argv[1]) : 16;
    run_case(m);
    return 0;
}
