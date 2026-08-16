#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <string>
#include <vector>

using boost::multiprecision::cpp_int;

constexpr int PRE_GATE_STEPS = 1539;
const cpp_int N0("3939105844976711153619");
const cpp_int NMAX("5908625413101667397287");

// Exact natural G13 sample found after enforcing x_G13 < 2^954.
// Its G13 relation reaches endpoint credit 1 at block 51, but this certificate
// proves that this ordinary G13 start has no 1539-step R1 preimage even in the
// numeric interval [N0,NMAX], before the ternary Cantor restriction is applied.
const cpp_int X0(
"9311066934133191055179217771751644756458780835642375520644606697570370834878851085876330120952372828601875854086643506229770877868471756436379730259097164274868063513702695410370082518062231340901656195848133042167901156081765468572447679246085622583924868464925000059470402523777450879");

std::vector<cpp_int> p2, p3;
int target_evens = 0;
unsigned long long nodes = 0, numeric_leaves = 0, core_leaves = 0;

bool in_current_m44_core(cpp_int N) {
    if (N < N0 || N > NMAX) return false;
    if ((N & 3) != 3) return false;
    cpp_int y = (N - 3) / 4;
    for (int i = 0; i < 44; ++i) {
        unsigned d = static_cast<unsigned>((y % 3).convert_to<unsigned>());
        if (d > 1) return false;
        y /= 3;
    }
    return y == 1;
}

bool root_interval_possible(const cpp_int& x, int E) {
    const int r = PRE_GATE_STEPS;
    const int k = E;
    const int m = r - k;
    if (m < 0) return false;

    // Reverse maps corresponding to forward steps:
    //   forward-even predecessor: E(x)=2x,
    //   forward-odd predecessor:  O(x)=(2x-1)/3, if x == 2 mod 3.
    // Among all orders with k E maps and m O maps, exact endpoint envelopes are
    //
    // min = E^k O^m(x) = [2^k 3^m + 2^r(x-1)] / 3^m,
    // max = O^m E^k(x) = [3^m + 2^m(2^k x-1)] / 3^m.
    const cpp_int minnum = p2[k] * p3[m] + p2[r] * (x - 1);
    const cpp_int maxnum = p3[m] + p2[m] * (p2[k] * x - 1);
    return minnum <= p3[m] * NMAX && maxnum >= p3[m] * N0;
}

void dfs(int r, int eused, const cpp_int& x) {
    ++nodes;
    const int k = target_evens - eused;
    if (k < 0 || k > r) return;
    const int m = r - k;

    const cpp_int minnum = p2[k] * p3[m] + p2[r] * (x - 1);
    if (minnum > p3[m] * NMAX) return;
    const cpp_int maxnum = p3[m] + p2[m] * (p2[k] * x - 1);
    if (maxnum < p3[m] * N0) return;

    if (r == 0) {
        if (x >= N0 && x <= NMAX) {
            ++numeric_leaves;
            if (in_current_m44_core(x)) ++core_leaves;
        }
        return;
    }

    if (k > 0) dfs(r - 1, eused + 1, 2 * x);
    if ((x % 3) == 2) dfs(r - 1, eused, (2 * x - 1) / 3);
}

int main() {
    p2.resize(PRE_GATE_STEPS + 1);
    p3.resize(PRE_GATE_STEPS + 1);
    p2[0] = p3[0] = 1;
    for (int i = 1; i <= PRE_GATE_STEPS; ++i) {
        p2[i] = 2 * p2[i - 1];
        p3[i] = 3 * p3[i - 1];
    }

    std::vector<int> possible_E;
    for (int E = 0; E <= 30; ++E)
        if (root_interval_possible(X0, E)) possible_E.push_back(E);

    if (possible_E != std::vector<int>{14}) {
        std::cerr << "Unexpected root-even envelope.\n";
        return 2;
    }

    target_evens = 14;
    dfs(PRE_GATE_STEPS, 0, X0);

    std::cout << "possible_total_evens=14\n";
    std::cout << "reverse_nodes=" << nodes << "\n";
    std::cout << "numeric_window_leaves=" << numeric_leaves << "\n";
    std::cout << "m44_core_leaves=" << core_leaves << "\n";

    if (nodes != 3131ULL) return 3;
    if (numeric_leaves != 0 || core_leaves != 0) return 4;
    std::cout << "candidate_specific_same_word_elimination: PASS\n";
    return 0;
}
