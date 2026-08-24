#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>

using boost::multiprecision::cpp_int;
using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {
constexpr int B = 8;
constexpr int HMAX = 256;
bool ALLOW[9][256]{};
int QMIN[HMAX + 1]{};

void build_blocks() {
    std::array<u64, 9> p3{};
    p3[0] = 1;
    for (int i = 1; i <= B; ++i) p3[i] = 3 * p3[i - 1];

    struct Entry { u64 R = 0; u32 mask = 0; bool set = false; };
    for (int q = 0; q <= B; ++q) {
        std::unordered_map<u64, Entry> maxima;
        for (u32 mask = 0; mask < (1u << B); ++mask) {
            int qq = 0;
            u64 R = 0;
            for (int i = 0; i < B; ++i) {
                if ((mask >> i) & 1u) {
                    R = 3 * R + (u64(1) << i);
                    ++qq;
                }
            }
            if (qq != q) continue;
            auto &e = maxima[R % p3[q]];
            if (!e.set || R > e.R) e = Entry{R, mask, true};
        }
        for (const auto &kv : maxima) ALLOW[q][kv.second.mask] = true;
    }

    const std::array<int, 9> expected{{1, 2, 6, 17, 34, 36, 22, 8, 1}};
    for (int q = 0; q <= B; ++q) {
        int count = 0;
        for (int mask = 0; mask < (1 << B); ++mask) count += ALLOW[q][mask];
        if (count != expected[q]) std::exit(2);
    }

    cpp_int p2 = 1, p3exact = 1;
    int q = 0;
    for (int k = 1; k <= HMAX; ++k) {
        p2 <<= 1;
        while (p3exact < p2) {
            p3exact *= 3;
            ++q;
        }
        QMIN[k] = q;
    }
}

// Returns the number of fully valid accelerated steps before the first failure,
// capped at HMAX. A block-maximality failure at step k+1 returns k.
int survival_depth(u128 x) {
    int q = 0;
    u32 block_mask = 0;
    int block_q = 0, block_offset = 0;

    for (int k = 0; k < HMAX; ++k) {
        const int bit = int(x & 1);
        block_mask |= u32(bit) << block_offset;
        block_q += bit;
        ++block_offset;

        if (bit) {
            x = (3 * x + 1) >> 1;
            ++q;
        } else {
            x >>= 1;
        }

        if (q < QMIN[k + 1]) return k;

        if (block_offset == B) {
            if (!ALLOW[block_q][block_mask]) return k;
            block_mask = 0;
            block_q = 0;
            block_offset = 0;
        }
    }
    return HMAX;
}

struct Result {
    u64 h128 = 0;
    u64 h160 = 0;
    u64 h192 = 0;
    int max_depth = 0;
};

Result scan(int m) {
    std::vector<u64> p3(m + 1, 1);
    for (int i = 1; i <= m; ++i) p3[i] = 3 * p3[i - 1];

    const int low_bits = m / 2;
    const int high_bits = m - low_bits;
    const u64 nlow = u64(1) << low_bits;
    const u64 nhigh = u64(1) << high_bits;
    std::vector<u64> low_sum(nlow), high_sum(nhigh);

    for (u64 mask = 1; mask < nlow; ++mask) {
        const u64 bit = mask & (~mask + 1);
        const int i = __builtin_ctzll(bit);
        low_sum[mask] = low_sum[mask ^ bit] + p3[i];
    }
    for (u64 mask = 1; mask < nhigh; ++mask) {
        const u64 bit = mask & (~mask + 1);
        const int i = __builtin_ctzll(bit);
        high_sum[mask] = high_sum[mask ^ bit] + p3[low_bits + i];
    }

    const u64 total = u64(1) << m;
    u64 c128 = 0, c160 = 0, c192 = 0;
    int max_depth = 0;

    #pragma omp parallel
    {
        u64 l128 = 0, l160 = 0, l192 = 0;
        int lmax = 0;

        #pragma omp for schedule(static)
        for (long long mm = 0; mm < static_cast<long long>(total); ++mm) {
            const u64 mask = static_cast<u64>(mm);
            const u64 s = low_sum[mask & (nlow - 1)] + high_sum[mask >> low_bits];
            const u128 N = u128(4) * (u128(p3[m]) + s) + 3;
            const int d = survival_depth(N);
            if (d >= 128) ++l128;
            if (d >= 160) ++l160;
            if (d >= 192) ++l192;
            if (d > lmax) lmax = d;
        }

        #pragma omp atomic
        c128 += l128;
        #pragma omp atomic
        c160 += l160;
        #pragma omp atomic
        c192 += l192;
        #pragma omp critical
        { if (lmax > max_depth) max_depth = lmax; }
    }

    return Result{c128, c160, c192, max_depth};
}

struct Expected {
    int m;
    u64 h128;
    u64 h160;
    u64 h192;
    int max_depth;
};

constexpr std::array<Expected, 5> EXPECTED{{
    {23,  2, 0, 0, 135},
    {24,  2, 0, 0, 151},
    {25, 11, 0, 0, 143},
    {26, 23, 2, 0, 175},
    {27, 26, 1, 0, 167},
}};
} // namespace

int main() {
    build_blocks();
    for (const auto &e : EXPECTED) {
        const Result r = scan(e.m);
        if (r.h128 != e.h128 || r.h160 != e.h160 ||
            r.h192 != e.h192 || r.max_depth != e.max_depth) return 3;
        std::cout << "m=" << e.m
                  << " H128=" << r.h128
                  << " H160=" << r.h160
                  << " H192=" << r.h192
                  << " max_valid_depth=" << r.max_depth << "\n";
    }
    std::cout << "L8 small-core m23-m27 extension certificate: PASS\n";
    return 0;
}
