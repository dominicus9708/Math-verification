// Exact finite closure of the high first-defect dyadic shells for A0 s=1.
//
// Upstream SAFE inputs:
//   * every survivor has d_75 >= 8;
//   * v2(X-X_th) is one of the 24 certified first-defect positions;
//   * each first-defect shell has its own SAFE X upper bound obtained from its
//     minimum irreversible first-75 correction defect.
//
// This scanner exhausts every ordinary X in the ten shells
//
//   f in {40,43,46,48,51,54,56,59,62,65}
//
// below the corresponding shell-specific X bound.  It runs the ACTUAL
// accelerated Collatz orbit, checks the exact pure-ballot threshold at every
// prefix, enforces d_75>=8 at depth 75, and scans through depth 1000.
//
// Every candidate fails.  The latest first failure is prefix 454.  Hence no
// A0 s=1 survivor can have first-defect valuation f>=40 among the certified
// shell list; the remaining first-defect set ends at f=37.
//
// This is a finite necessary-condition closure, not a Collatz proof.
// Recommended build: g++ -O3 -fopenmp -std=c++17 <file> -o cert

#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>

using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

namespace {

constexpr int MAX_SCAN = 1000;

struct Shell {
    int f;
    const char* xmax;
    unsigned long long expected_total;
    unsigned long long expected_pass75;
    int expected_latest;
};

constexpr std::array<Shell, 10> SHELLS = {{
    {40, "3234977022306380720329", 397355407ULL, 18494738ULL, 454},
    {43, "3234977022306538979478",  49669426ULL,  3162894ULL, 433},
    {46, "3234977022306619447778",   6208679ULL,   549048ULL, 382},
    {48, "3234977022306244314981",   1552170ULL,   116594ULL, 316},
    {51, "3234977022306411040669",    194021ULL,    19521ULL, 284},
    {54, "3234977022306495813858",     24253ULL,     3171ULL, 224},
    {56, "3234977022306100612227",      6064ULL,      596ULL, 197},
    {59, "3234977022306276257396",       758ULL,       68ULL, 127},
    {62, "3234977022306365565777",        94ULL,        6ULL, 129},
    {65, "3234977022306134263496",        12ULL,        0ULL,  75},
}};

u128 parse_u128(const char* s) {
    u128 x = 0;
    for (; *s; ++s) {
        assert('0' <= *s && *s <= '9');
        x = 10 * x + static_cast<unsigned>(*s - '0');
    }
    return x;
}

}  // namespace

int main() {
    std::array<int, MAX_SCAN + 1> req{};
    std::array<int, 75> threshold{};

    cpp_int p2 = 1;
    cpp_int p3 = 1;
    int k = 0;
    for (int n = 1; n <= MAX_SCAN; ++n) {
        p2 *= 2;
        while (p3 <= p2) {
            p3 *= 3;
            ++k;
        }
        req[n] = k;
        if (n <= 75) threshold[n - 1] = req[n] - req[n - 1];
    }
    assert(req[75] == 48);

    const u128 X_TH = parse_u128("4697939311072332635131");
    const u128 X_MIN = (u128(1) << 71) + 1;
    const u128 UMAX = ~u128(0);

    unsigned long long grand_total = 0;
    unsigned long long grand_pass75 = 0;
    unsigned long long grand_survivors = 0;
    int grand_latest = 0;

    for (const Shell& shell : SHELLS) {
        const int f = shell.f;
        const u128 hi = parse_u128(shell.xmax);
        const u128 modulus = u128(1) << (f + 1);
        const u128 mask = modulus - 1;
        const u128 residue = (X_TH + (u128(1) << f)) & mask;
        const u128 low_residue = X_MIN & mask;
        const u128 offset = (residue + modulus - low_residue) & mask;
        const u128 first = X_MIN + offset;
        assert(first <= hi);

        const u128 count128 = (hi - first) / modulus + 1;
        const unsigned long long count = static_cast<unsigned long long>(count128);
        assert(u128(count) == count128);
        assert(count == shell.expected_total);

        unsigned long long pass75 = 0;
        unsigned long long survivors = 0;
        int latest = 0;
        unsigned long long overflows = 0;

#pragma omp parallel for reduction(+:pass75,survivors,overflows) reduction(max:latest) schedule(static)
        for (unsigned long long i = 0; i < count; ++i) {
            const u128 X = first + modulus * u128(i);
            u128 x = X;
            int q = 0;
            int d75 = 0;
            bool passed75 = false;
            bool alive = true;
            int failure = 0;

            for (int n = 1; n <= MAX_SCAN; ++n) {
                const int bit = static_cast<int>(x & 1);
                q += bit;
                if (n <= 75) d75 += (bit != threshold[n - 1]);

                if (q < req[n]) {
                    alive = false;
                    failure = n;
                    break;
                }

                if (n == 75) {
                    if (d75 < 8) {
                        alive = false;
                        failure = 75;
                        break;
                    }
                    passed75 = true;
                }

                if (bit) {
                    if (x > (UMAX - 1) / 3) {
                        ++overflows;
                        alive = false;
                        failure = MAX_SCAN + 1;
                        break;
                    }
                    x = (3 * x + 1) / 2;
                } else {
                    x /= 2;
                }
            }

            if (passed75) ++pass75;
            if (alive) {
                ++survivors;
            } else if (failure <= MAX_SCAN) {
                latest = std::max(latest, failure);
            }
        }

        assert(overflows == 0);
        assert(pass75 == shell.expected_pass75);
        assert(survivors == 0);
        assert(latest == shell.expected_latest);

        grand_total += count;
        grand_pass75 += pass75;
        grand_survivors += survivors;
        grand_latest = std::max(grand_latest, latest);

        std::cout << "f " << f
                  << " total " << count
                  << " pass75 " << pass75
                  << " survivors " << survivors
                  << " latest " << latest << '\n';
    }

    assert(grand_total == 455010884ULL);
    assert(grand_pass75 == 22346636ULL);
    assert(grand_survivors == 0);
    assert(grand_latest == 454);

    std::cout << "PASS A0 s=1 first-defect f>=40 shell closure certificate\n";
    std::cout << "total_scanned " << grand_total << '\n';
    std::cout << "passed_first75_d_ge_8 " << grand_pass75 << '\n';
    std::cout << "survivors_to_1000 0\n";
    std::cout << "latest_ballot_failure " << grand_latest << '\n';
    std::cout << "remaining_first_defect_max 37\n";
    std::cout << "status SAFE finite shell closure; full membership remains OPEN\n";
}
