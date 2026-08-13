#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

using boost::multiprecision::cpp_int;

namespace {

constexpr int MAX_L = 20;

struct Info {
    std::uint32_t mask{};
    int L{};
    int q{};
    std::uint64_t correction{};
    std::vector<int> odd_times;
    std::vector<std::uint64_t> correction_after_odd;
    bool coefficient_surviving{};
};

cpp_int pow3_big(int e) {
    cpp_int x = 1;
    while (e-- > 0) x *= 3;
    return x;
}

std::uint64_t pow3_u64(int e) {
    std::uint64_t x = 1;
    while (e-- > 0) x *= 3ULL;
    return x;
}

int v3(std::uint64_t x) {
    int s = 0;
    while (x != 0 && x % 3ULL == 0) {
        x /= 3ULL;
        ++s;
    }
    return s;
}

Info make_info(std::uint32_t mask, int L) {
    Info out;
    out.mask = mask;
    out.L = L;
    out.coefficient_surviving = true;

    std::uint64_t R = 0;
    int q = 0;

    for (int i = 0; i < L; ++i) {
        const int bit = static_cast<int>((mask >> i) & 1U);
        if (bit) {
            R = 3ULL * R + (1ULL << i);
            ++q;
            out.odd_times.push_back(i + 1);
            out.correction_after_odd.push_back(R);
        }

        // Exact coefficient-survival test at time t=i+1:
        // 3^q >= 2^t.
        if (pow3_u64(q) < (1ULL << (i + 1))) {
            out.coefficient_surviving = false;
        }
    }

    out.q = q;
    out.correction = R;
    return out;
}

bool removed_by_some_alternate(
    const Info& w,
    const std::vector<Info>& references,
    const cpp_int& Nmin) {

    const int q = w.q;
    const cpp_int p3q = pow3_big(q);

    for (const Info& u : references) {
        if (u.correction <= w.correction) continue;

        const std::uint64_t C = u.correction - w.correction;
        const int s = v3(C);
        if (s == 0) continue;

        // If 3^q divides C, the alternate start is already an integer:
        // N^# = N - C/3^q.
        if (s >= q) {
            const cpp_int delta = cpp_int(C) / p3q;
            if (delta > 0 && delta < Nmin) return true;
            continue;
        }

        const int d = q - s;
        const int td = u.odd_times.at(static_cast<std::size_t>(d - 1));
        const cpp_int p3d = pow3_big(d);
        const cpp_int p2t = cpp_int(1) << td;

        // The integerization prefix must be contracting.
        if (p2t <= p3d) continue;

        std::uint64_t C0 = C;
        for (int j = 0; j < s; ++j) C0 /= 3ULL;

        const cpp_int Rprefix =
            u.correction_after_odd.at(static_cast<std::size_t>(d - 1));

        // m-N = [(3^d-2^td)N + Rprefix - C/3^s]/2^td.
        // Since the N coefficient is negative, checking N=Nmin certifies
        // every N>=Nmin in the cylinder.
        const cpp_int diff_numerator =
            (p3d - p2t) * Nmin + Rprefix - cpp_int(C0);

        // Also ensure N^#>0 throughout the large-start regime.
        const bool alternate_positive = cpp_int(C) < Nmin * p3q;

        if (alternate_positive && diff_numerator < 0) return true;
    }

    return false;
}

}  // namespace

int main() {
    static_assert(MAX_L <= 20,
                  "This compact certificate stores finite corrections in uint64_t.");

    const cpp_int Nmin = 4 * (pow3_big(44) + pow3_big(32)) + 3;

    std::cout << "Nmin = " << Nmin << "\n";
    std::cout << "L surviving removed retained removed_fraction\n";

    for (int L = 3; L <= MAX_L; ++L) {
        const std::uint32_t total = 1U << L;
        std::vector<std::vector<Info>> by_q(static_cast<std::size_t>(L + 1));
        std::vector<Info> survivors;

        for (std::uint32_t mask = 0; mask < total; ++mask) {
            Info info = make_info(mask, L);
            by_q.at(static_cast<std::size_t>(info.q)).push_back(info);

            // Minimal-counterexample core begins OO in accelerated parity.
            if (info.coefficient_surviving && (mask & 3U) == 3U) {
                survivors.push_back(info);
            }
        }

        std::uint64_t removed = 0;
        for (const Info& w : survivors) {
            if (removed_by_some_alternate(
                    w,
                    by_q.at(static_cast<std::size_t>(w.q)),
                    Nmin)) {
                ++removed;
            }
        }

        const std::uint64_t retained =
            static_cast<std::uint64_t>(survivors.size()) - removed;
        const long double fraction =
            survivors.empty()
                ? 0.0L
                : static_cast<long double>(removed) /
                      static_cast<long double>(survivors.size());

        std::cout << L << ' '
                  << survivors.size() << ' '
                  << removed << ' '
                  << retained << ' '
                  << std::setprecision(15) << fraction << '\n';
    }

    return 0;
}
