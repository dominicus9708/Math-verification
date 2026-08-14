#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using u128 = unsigned __int128;

namespace {

constexpr int L = 73;
const std::string H19 = "1101101101011011010";

std::string mech;
std::array<int, L + 1> barrier{};
u128 mask73{};
u128 V33{};
u128 Nmax{};
std::array<u128, L + 1> inv3q{};

std::string print_u128(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(static_cast<char>('0' + static_cast<int>(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

u128 pow3(int n) {
    u128 x = 1;
    while (n-- > 0) x *= 3;
    return x;
}

u128 inverse_odd_mod_2_73(u128 a) {
    // Newton iteration in the 2-adics. Unsigned overflow is reduction mod 2^128;
    // masking at the end leaves the exact inverse modulo 2^73.
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    return x & mask73;
}

bool in_current_m44_cantor_core(u128 N) {
    if ((N & 3) != 3) return false;
    if (N <= V33 || N > Nmax) return false;

    u128 y = (N - 3) / 4;
    for (int i = 0; i < 44; ++i) {
        const unsigned digit = static_cast<unsigned>(y % 3);
        if (digit > 1) return false;
        y /= 3;
    }
    if (static_cast<unsigned>(y % 3) != 1) return false;
    y /= 3;
    return y == 0;
}

struct Result {
    std::uint64_t leaves = 0;
    std::vector<std::pair<int, u128>> matches;
};

void dfs(int i, int q, int hamming, int K, u128 R, Result& out) {
    if (hamming > K) return;

    if (i == L) {
        ++out.leaves;
        const u128 N = ((u128{0} - R) * inv3q[static_cast<std::size_t>(q)]) & mask73;
        if (in_current_m44_cantor_core(N)) {
            out.matches.push_back({hamming, N});
        }
        return;
    }

    const int m = mech[static_cast<std::size_t>(i)] - '0';
    for (int choice = 0; choice < 2; ++choice) {
        const int bit = (choice == 0 ? m : 1 - m);
        const int q2 = q + bit;
        if (q2 < barrier[static_cast<std::size_t>(i + 1)]) continue;

        u128 R2 = R;
        if (bit) {
            R2 = (3 * R2 + (u128{1} << i)) & mask73;
        }
        dfs(i + 1,
            q2,
            hamming + (bit != m),
            K,
            R2,
            out);
    }
}

std::pair<int, u128> first_descent(u128 n, int limit = 100000) {
    u128 x = n;
    for (int step = 1; step <= limit; ++step) {
        if (x & 1) x = (3 * x + 1) / 2;
        else x /= 2;
        if (x < n) return {step, x};
    }
    return {-1, x};
}

}  // namespace

int main(int argc, char** argv) {
    const int K = (argc > 1 ? std::atoi(argv[1]) : 7);
    if (K < 0 || K > 9) {
        std::cerr << "This compact verifier is intended for K=0,...,9.\n";
        return 2;
    }

    mech = (H19 + H19 + H19 + H19).substr(0, L);
    int count = 0;
    for (int i = 0; i < L; ++i) {
        count += (mech[static_cast<std::size_t>(i)] == '1');
        barrier[static_cast<std::size_t>(i + 1)] = count;
    }

    mask73 = (u128{1} << 73) - 1;
    u128 p3mod = 1;
    for (int q = 0; q <= L; ++q) {
        inv3q[static_cast<std::size_t>(q)] = inverse_odd_mod_2_73(p3mod);
        p3mod = (3 * p3mod) & mask73;
    }

    V33 = 4 * (pow3(44) + pow3(33)) + 2;
    Nmax = 6 * pow3(44) + 1;

    Result result;
    dfs(0, 0, 0, K, 0, result);

    std::sort(result.matches.begin(), result.matches.end(),
              [](const auto& a, const auto& b) {
                  if (a.first != b.first) return a.first < b.first;
                  return a.second < b.second;
              });
    result.matches.erase(
        std::unique(result.matches.begin(), result.matches.end(),
                    [](const auto& a, const auto& b) {
                        return a.first == b.first && a.second == b.second;
                    }),
        result.matches.end());

    std::cout << "K=" << K
              << " ballot_leaves=" << result.leaves
              << " cantor_matches=" << result.matches.size() << "\n";

    int max_descent = 0;
    for (const auto& [h, N] : result.matches) {
        const auto [depth, below] = first_descent(N);
        std::cout << "h=" << h
                  << " N=" << print_u128(N)
                  << " first_descent=" << depth
                  << " below=" << print_u128(below) << "\n";
        if (depth < 0) {
            std::cerr << "No first descent within safety limit.\n";
            return 3;
        }
        max_descent = std::max(max_descent, depth);
    }

    std::cout << "max_first_descent=" << max_descent << "\n";

    // Reference counts used in the accompanying note.
    if (K == 4 && result.leaves != 235873ULL) return 4;
    if (K == 6 && result.leaves != 25000400ULL) return 5;
    if (K == 7 && (result.leaves != 176477240ULL || result.matches.size() != 1)) return 6;
    if (K == 8 && (result.leaves != 1425446750ULL || result.matches.size() != 11)) return 7;
    // K=9 is large and was independently partitioned in the original audit.
    // The expected totals are 7,900,490,816 ballot leaves and 57 Cantor matches.

    return 0;
}
