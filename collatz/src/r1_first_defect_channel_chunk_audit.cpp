#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {

constexpr int DEPTH = 27;
constexpr int SPLIT = 22;
constexpr int CHUNK_BITS = 18;
constexpr u64 MOD25 = 1ULL << 25;
constexpr u64 MASK25 = MOD25 - 1;

std::string to_string128(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(static_cast<char>('0' + static_cast<int>(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

u128 pow3e(int e) {
    u128 x = 1;
    while (e-- > 0) x *= 3;
    return x;
}

u64 invodd(u64 a) {
    u64 x = 1;
    for (int i = 0; i < 7; ++i) x *= 2 - a * x;
    return x;
}

struct LowEntry {
    u32 r25{};
    u64 exact{};
    bool operator<(const LowEntry& o) const {
        if (r25 != o.r25) return r25 < o.r25;
        return exact < o.exact;
    }
};

std::vector<u64> load_allow27(const std::string& path) {
    std::ifstream f(path, std::ios::binary);
    if (!f) throw std::runtime_error("cannot open allow27 bitset");
    std::vector<u64> bits((1ULL << DEPTH) / 64);
    f.read(reinterpret_cast<char*>(bits.data()), bits.size() * sizeof(u64));
    if (!f) throw std::runtime_error("short allow27 bitset");
    return bits;
}

bool allowed(const std::vector<u64>& bits, u32 r) {
    return ((bits[r >> 6] >> (r & 63)) & 1ULL) != 0;
}

u64 mechanical_residue_73() {
    const std::string H19 = "1101101101011011010";
    const std::string w = (H19 + H19 + H19 + H19).substr(0, 73);
    const u64 mask = (1ULL << 63) - 1; // only for the low-64 intermediate below

    // Use u128 for the exact 73-bit modulus.
    const u128 M = u128{1} << 73;
    const u128 MASK = M - 1;
    u128 R = 0;
    int q = 0;
    for (int i = 0; i < 73; ++i) {
        if (w[static_cast<std::size_t>(i)] == '1') {
            R = (3 * R + (u128{1} << i)) & MASK;
            ++q;
        }
    }

    u128 a = 1;
    for (int i = 0; i < q; ++i) a = (3 * a) & MASK;
    u128 x = 1;
    for (int i = 0; i < 8; ++i) x = x * (2 - a * x);
    const u128 n = ((u128{0} - R) * x) & MASK;
    (void)mask;
    return static_cast<u64>(n & ((u128{1} << 63) - 1));
}

// The current mechanical residue is below 2^73 but above 2^63, so for the
// first-mismatch test at p<=21 only its low 27 bits are needed.
u32 mechanical_residue_27() {
    const std::string H19 = "1101101101011011010";
    const std::string w = (H19 + H19 + H19 + H19).substr(0, 27);
    const u64 M = 1ULL << 27;
    const u64 MASK = M - 1;
    u64 R = 0;
    int q = 0;
    for (int i = 0; i < 27; ++i) {
        if (w[static_cast<std::size_t>(i)] == '1') {
            R = (3 * R + (1ULL << i)) & MASK;
            ++q;
        }
    }
    u64 a = 1;
    for (int i = 0; i < q; ++i) a = (3 * a) & MASK;
    return static_cast<u32>((u64(0) - R) * invodd(a) & MASK);
}

int first_descent(u128 N, int limit, u128& below, u128& peak) {
    u128 x = N;
    peak = N;
    for (int step = 1; step <= limit; ++step) {
        if (x & 1) x = (3 * x + 1) / 2;
        else x /= 2;
        if (x > peak) peak = x;
        if (x < N) {
            below = x;
            return step;
        }
    }
    below = x;
    return -1;
}

} // namespace

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "usage: r1_first_defect_channel_chunk_audit allow27.bin p chunk\n";
        return 2;
    }
    const std::string allow_path = argv[1];
    const int p = std::atoi(argv[2]);
    const int chunk = std::atoi(argv[3]);
    if (p < 2 || p >= 27 || chunk < 0 || chunk >= 16) return 3;

    const auto allow_bits = load_allow27(allow_path);
    const u32 mech27 = mechanical_residue_27();
    const u32 mod27mask = (1U << 27) - 1;

    // Gather every depth-27 Hensel-retained residue whose first parity mismatch
    // from the mechanical R1 prefix is exactly at bit p.
    std::vector<u32> targetsN;
    const u32 maskp1 = (1U << (p + 1)) - 1;
    const u32 want = 1U << p;
    for (u32 r = 3; r < (1U << 27); r += 4) {
        if (!allowed(allow_bits, r)) continue;
        const u32 d = (r - mech27) & maskp1;
        if (d == want) targetsN.push_back(r);
    }

    const u64 base_y25 = static_cast<u64>(pow3e(44)) & MASK25;
    std::vector<u32> targetsS;
    targetsS.reserve(targetsN.size());
    for (u32 r : targetsN) {
        const u32 y = (r - 3U) >> 2;
        targetsS.push_back(static_cast<u32>((u64(y) - base_y25) & MASK25));
    }

    // Low 22 selectors: exact sum is still below 2^64.
    std::vector<u64> low_r(1, 0), low_exact(1, 0);
    for (int i = 0; i < 22; ++i) {
        const u64 w = static_cast<u64>(pow3e(i));
        const std::size_t n = low_r.size();
        low_r.resize(2 * n);
        low_exact.resize(2 * n);
        for (std::size_t j = 0; j < n; ++j) {
            low_r[n + j] = (low_r[j] + w) & MASK25;
            low_exact[n + j] = low_exact[j] + w;
        }
    }

    std::vector<LowEntry> low;
    low.reserve(low_r.size());
    for (std::size_t i = 0; i < low_r.size(); ++i)
        low.push_back({static_cast<u32>(low_r[i]), low_exact[i]});
    std::sort(low.begin(), low.end());

    // High 22 selectors.  Index bits are selectors a_22,...,a_43.
    std::vector<u64> high_r(1, 0);
    std::vector<u128> high_exact(1, 0);
    for (int i = 22; i < 44; ++i) {
        const u128 we = pow3e(i);
        const u64 wr = static_cast<u64>(we) & MASK25;
        const std::size_t n = high_r.size();
        high_r.resize(2 * n);
        high_exact.resize(2 * n);
        for (std::size_t j = 0; j < n; ++j) {
            high_r[n + j] = (high_r[j] + wr) & MASK25;
            high_exact[n + j] = high_exact[j] + we;
        }
    }

    // Current unresolved core is N>V_33.  In the m=44 Cantor layer that is
    // equivalent to at least one of a_33,...,a_43 being one, i.e. high mask >=2^11.
    const std::size_t CH = 1ULL << CHUNK_BITS;
    std::size_t begin = std::max<std::size_t>(1ULL << 11, std::size_t(chunk) * CH);
    std::size_t end = std::min<std::size_t>(high_r.size(), std::size_t(chunk + 1) * CH);

    const u128 baseN = 4 * pow3e(44) + 3;
    unsigned long long pairs = 0;
    unsigned long long failures = 0;
    int max_tau = 0;
    u128 worstN = 0, worstBelow = 0, maxPeak = 0;

    for (std::size_t hm = begin; hm < end; ++hm) {
        const u32 hr = static_cast<u32>(high_r[hm]);
        for (u32 target : targetsS) {
            const u32 complement = static_cast<u32>((u64(target) - hr) & MASK25);
            const LowEntry lo_key{complement, 0};
            const LowEntry hi_key{complement, ~u64(0)};
            auto lo_it = std::lower_bound(low.begin(), low.end(), lo_key);
            auto hi_it = std::upper_bound(low.begin(), low.end(), hi_key);

            for (auto it = lo_it; it != hi_it; ++it) {
                ++pairs;
                const u128 N = baseN + 4 * (u128(it->exact) + high_exact[hm]);
                u128 below = 0, peak = 0;
                const int tau = first_descent(N, 20000, below, peak);
                if (tau < 0) {
                    ++failures;
                    if (failures <= 4)
                        std::cerr << "FAIL " << to_string128(N) << "\n";
                } else if (tau > max_tau) {
                    max_tau = tau;
                    worstN = N;
                    worstBelow = below;
                }
                if (peak > maxPeak) maxPeak = peak;
            }
        }
    }

    std::cout << "p " << p
              << " chunk " << chunk
              << " retained_prefixes " << targetsN.size()
              << " pairs " << pairs
              << " failures " << failures
              << " max_tau " << max_tau
              << " worst_N " << to_string128(worstN)
              << " below " << to_string128(worstBelow)
              << " max_peak " << to_string128(maxPeak)
              << "\n";

    return failures ? 4 : 0;
}
