#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>

using u128 = unsigned __int128;

static u128 parse128(const std::string& s) {
    u128 x = 0;
    for (char c : s) x = 10 * x + (c - '0');
    return x;
}

static std::string out128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static bool cantor21(u128 x) {
    for (int i = 0; i < 21; ++i) {
        const int d = int(x % 3);
        if (d == 2) return false;
        x /= 3;
    }
    return x == 0;
}

int main() {
    // Isolated resonance and terminal 48-core constants.
    const u128 M48 = parse128("79766443076872509863361"); // 3^48
    const u128 y_mech = parse128("40150856745180969070537");
    // Mechanical contribution of i=q-20 to the terminal 48 residue.
    const u128 term0 = parse128("59848982037546512930379");

    const std::uint64_t M19 = 1162261467ULL; // 3^19
    const std::uint64_t r19 = 738416854ULL; // fixed y mod 3^19
    const std::uint64_t Cq = 7908027021468ULL;

    // Exact-rational upstream certificate: ceil(beta*N_def,max).
    const std::uint64_t ZMAX = 167265511ULL;

    // With exactly one defect in the last 20 odd positions, if it is the
    // first terminal position it may be inherited from an earlier run.
    // Then y(z) = y_mech + term0(2^{-z}-1) mod 3^48.
    u128 base = (y_mech + M48 - term0) % M48;
    u128 varying = term0;

    std::uint64_t hits = 0;
    for (std::uint64_t z = 1; z <= ZMAX; ++z) {
        // Multiply by 2^{-1} modulo an odd modulus without wide multiply.
        if (varying & 1) varying = (varying + M48) >> 1;
        else varying >>= 1;

        u128 y = base + varying;
        if (y >= M48) y -= M48;

        if (std::uint64_t(y % M19) != r19) {
            std::cerr << "terminal residue invariant failed\n";
            return 2;
        }

        const u128 Y = (y - r19) / M19;
        if ((Y & 3) != 0) continue;
        const u128 q4 = Y >> 2;
        if (q4 < Cq) continue;
        const u128 shi = q4 - Cq;
        if (!cantor21(shi)) continue;

        ++hits;
        std::cout << z << '\t' << out128(y) << '\t' << out128(shi) << '\n';
    }

    std::cerr << "COUNT " << hits << '\n';
    return hits == 5 ? 0 : 3;
}
