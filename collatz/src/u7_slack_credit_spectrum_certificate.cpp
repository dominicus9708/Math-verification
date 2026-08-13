#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

struct Aggregate {
    std::uint64_t lo = std::numeric_limits<std::uint64_t>::max();
    std::uint64_t hi = 0;
    std::uint64_t count = 0;
};

static std::uint64_t pow3(int n) {
    std::uint64_t x = 1;
    while (n--) x *= 3ULL;
    return x;
}

struct Expected {
    int h;
    int q;
    std::uint64_t fibre;
    std::uint64_t classes;
    std::uint64_t covered;
    std::uint64_t max_credit;
};

int main() {
    const std::string mechanical = "011011011010110110101101101";
    const int L = 27;
    const int Q = 17;

    const Expected expected[] = {
        {1,16, 4'717'204ULL, 2'994'059ULL, 1'723'145ULL, 19ULL},
        {2,15, 8'592'795ULL, 3'388'771ULL, 5'204'024ULL, 59ULL},
        {3,14,12'032'438ULL, 2'260'388ULL, 9'772'050ULL,167ULL},
        {4,13,13'716'208ULL, 1'001'830ULL,12'714'378ULL,481ULL},
        {5,12,13'050'437ULL,   353'924ULL,12'696'513ULL,1'377ULL},
        {6,11,10'490'228ULL,   118'098ULL,10'372'130ULL,4'011ULL},
        {7,10, 7'156'370ULL,    39'366ULL, 7'117'004ULL,11'027ULL},
        {8, 9, 4'142'481ULL,    13'122ULL, 4'129'359ULL,29'025ULL},
        {9, 8, 2'026'638ULL,     4'374ULL, 2'022'264ULL,78'886ULL},
        {10,7,   831'657ULL,     1'458ULL,   830'199ULL,203'915ULL},
        {11,6,   282'891ULL,       486ULL,   282'405ULL,546'214ULL},
        {12,5,    78'386ULL,       162ULL,    78'224ULL,1'376'523ULL},
        {13,4,    17'248ULL,        54ULL,    17'194ULL,3'080'998ULL},
        {14,3,     2'900ULL,        18ULL,     2'882ULL,7'145'845ULL},
        {15,2,       350ULL,         6ULL,       344ULL,13'048'945ULL},
        {16,1,        27ULL,         2ULL,        25ULL,22'369'621ULL},
    };

    for (const auto& ex : expected) {
        const int htarget = ex.h;
        const int q = ex.q;
        const std::uint64_t modulus = pow3(q);

        std::unordered_map<std::uint64_t, Aggregate> classes;
        classes.reserve(static_cast<std::size_t>(ex.classes * 1.3) + 64);
        std::uint64_t fibre = 0;

        std::uint32_t comb = (1U << q) - 1U;
        const std::uint32_t limit = 1U << L;

        while (comb < limit) {
            int height = 0;
            int minimum = 0;
            bool admissible = true;

            for (int i = 0; i < L; ++i) {
                const int actual = static_cast<int>((comb >> i) & 1U);
                const int reference = mechanical[static_cast<std::size_t>(i)] - '0';
                height += actual - reference;
                minimum = std::min(minimum, height);
                if (minimum < -htarget) {
                    admissible = false;
                    break;
                }
            }

            if (admissible && height == -htarget && minimum == -htarget) {
                std::uint64_t R = 0;
                for (int i = 0; i < L; ++i) {
                    if ((comb >> i) & 1U) R = 3ULL * R + (1ULL << i);
                }
                auto& a = classes[R % modulus];
                a.lo = std::min(a.lo, R);
                a.hi = std::max(a.hi, R);
                ++a.count;
                ++fibre;
            }

            const std::uint32_t x = comb & (~comb + 1U);
            const std::uint32_t y = comb + x;
            if (y == 0 || y >= limit) break;
            comb = (((comb & ~y) / x) >> 1U) | y;
        }

        std::uint64_t covered = 0;
        std::uint64_t max_credit = 0;
        for (const auto& [residue, a] : classes) {
            (void)residue;
            if (a.count > 1) {
                covered += a.count - 1;
                max_credit = std::max(max_credit, (a.hi - a.lo) / modulus);
            }
        }

        if (fibre != ex.fibre) return 10 + ex.h;
        if (classes.size() != ex.classes) return 40 + ex.h;
        if (covered != ex.covered) return 70 + ex.h;
        if (max_credit != ex.max_credit) return 100 + ex.h;

        // Every nonempty correction residue is a 3-adic unit.
        for (const auto& [residue, a] : classes) {
            (void)a;
            if (q > 0 && residue % 3ULL == 0ULL) return 140 + ex.h;
        }

        if (ex.h >= 6) {
            const std::uint64_t phi = 2ULL * pow3(q - 1);
            if (classes.size() != phi) return 180 + ex.h;
        }

        std::cout << "h=" << ex.h
                  << " q=" << q
                  << " fibre=" << fibre
                  << " classes=" << classes.size()
                  << " covered=" << covered
                  << " max_credit=" << max_credit << '\n';
    }

    return 0;
}
