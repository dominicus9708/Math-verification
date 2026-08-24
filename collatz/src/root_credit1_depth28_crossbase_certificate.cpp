// Exact finite certificate for the globally safe root credit-1 filter.
//
// A hypothetical minimal counterexample N is odd.  Hence N and N-1 have the
// same binary lift bits above bit 0.  If at some prefix depth k their actual
// Collatz prefixes have equal odd count and equal endpoint, then the two
// correction terms satisfy R(N-1)-R(N)=3^q, so the N-prefix has a root
// credit-1 sibling.  Since N-1<N, such a prefix is impossible for a minimal
// counterexample.
//
// This program exhausts the first 28 coefficient-surviving parity prefixes,
// reconstructs their canonical starts modulo 2^28, removes exactly those for
// which N and N-1 have already merged at equal odd count, and intersects the
// remaining residues with the m=44/m=45 ternary selector multiplicities.
//
// The result is a NEGATIVE CONTROL: the conditional credit-1 survival fraction
// on the ternary selector is essentially the same as in the ambient
// coefficient-surviving language.  No asymptotic independence claim is made.
//
// Build: g++ -O3 -std=c++17 root_credit1_depth28_crossbase_certificate.cpp -o cert

#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u32 = std::uint32_t;

static constexpr int L = 28;
static constexpr int KY = 26;
static constexpr u32 YM = 1u << KY;
static constexpr u32 YMASK = YM - 1;

std::vector<std::uint8_t> credit_alive;
u64 language_total = 0;
u64 credit_alive_total = 0;

u64 invodd(u64 a) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x;
}

u64 correction(u32 mask) {
    u64 R = 0;
    for (int i = 0; i < L; ++i)
        if ((mask >> i) & 1u) R = 3 * R + (1ULL << i);
    return R;
}

bool avoids_root_credit1(u32 N) {
    u64 x = N;
    u64 y = N - 1;
    int qx = 0;
    int qy = 0;

    for (int k = 0; k < L; ++k) {
        if (x & 1ULL) {
            x = (3 * x + 1) >> 1;
            ++qx;
        } else {
            x >>= 1;
        }

        if (y & 1ULL) {
            y = (3 * y + 1) >> 1;
            ++qy;
        } else {
            y >>= 1;
        }

        if (x == y && qx == qy) return false;
    }
    return true;
}

void emit(u32 mask, int q) {
    u64 R = correction(mask);
    u64 p3 = 1;
    for (int i = 0; i < q; ++i) p3 *= 3;

    const u32 N = static_cast<u32>(
        ((0ULL - R) * invodd(p3)) & ((1ULL << L) - 1));
    if ((N & 3u) != 3u) std::exit(2);

    ++language_total;
    if (!avoids_root_credit1(N)) return;

    const u32 z = (N - 3u) >> 2;
    if (credit_alive[z]) std::exit(3); // parity-vector bijection audit
    credit_alive[z] = 1;
    ++credit_alive_total;
}

void dfs(int k, int q, u32 mask) {
    if (k == L) {
        emit(mask, q);
        return;
    }

    for (int bit = 0; bit <= 1; ++bit) {
        const int q2 = q + bit;
        u64 p3 = 1;
        for (int j = 0; j < q2; ++j) p3 *= 3;
        if (p3 < (1ULL << (k + 1))) continue; // coefficient survival
        dfs(k + 1, q2, mask | (u32(bit) << k));
    }
}

std::vector<u32> selector_dp(int digits) {
    std::vector<u32> dp(YM), nd(YM);
    dp[0] = 1;
    u32 w = 1;
    for (int i = 0; i < digits; ++i) {
        if (i) w = static_cast<u32>((u64(w) * 3) & YMASK);
        for (u32 r = 0; r < YM; ++r)
            nd[r] = dp[r] + dp[(r + YM - w) & YMASK];
        dp.swap(nd);
    }
    return dp;
}

u64 count_block(const std::vector<u32>& dp, u64 C) {
    const u32 c = static_cast<u32>(C) & YMASK;
    u64 total = 0;
    for (u32 s = 0; s < YM; ++s)
        if (dp[s] && credit_alive[(c + s) & YMASK]) total += dp[s];
    return total;
}

int main() {
    credit_alive.assign(YM, 0);
    dfs(0, 0, 0);

    if (language_total != 3'524'586ULL) std::exit(4);
    if (credit_alive_total != 2'890'278ULL) std::exit(5);

    auto dp44 = selector_dp(44);
    auto dp33 = selector_dp(33);

    u64 p44 = 1;
    for (int i = 0; i < 44; ++i) p44 *= 3;

    const u64 m44_full = count_block(dp44, p44);
    const u64 m44_low33 = count_block(dp33, p44);
    const u64 m44_current = m44_full - m44_low33;
    const u64 m45_a = count_block(dp44, 3 * p44);
    const u64 m45_b = count_block(dp44, 4 * p44);
    const u64 m45_two = m45_a + m45_b;

    if (m44_full != 757'668'610'188ULL) std::exit(6);
    if (m44_low33 != 369'949'107ULL) std::exit(7);
    if (m44_current != 757'298'661'081ULL) std::exit(8);
    if (m45_a != 757'669'365'943ULL) std::exit(9);
    if (m45_b != 757'668'597'391ULL) std::exit(10);
    if (m45_two != 1'515'337'963'334ULL) std::exit(11);

    std::cout << "root credit-1 depth28 cross-base: PASS\n";
    std::cout << "coefficient_language " << language_total << '\n';
    std::cout << "credit1_alive_language " << credit_alive_total << '\n';
    std::cout << "m44_current_credit1_alive " << m44_current << '\n';
    std::cout << "m45_two_credit1_alive " << m45_two << '\n';
}
