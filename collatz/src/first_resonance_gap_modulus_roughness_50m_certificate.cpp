#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

static constexpr uint64_t A = 114208327604ULL;
static constexpr uint64_t Q = 72057431991ULL;
static constexpr int LIMIT = 50000000;

static uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m) {
    return (uint64_t)((__uint128_t)a * b % m);
}

static uint64_t powmod(uint64_t a, uint64_t e, uint64_t m) {
    uint64_t r = 1 % m;
    while (e) {
        if (e & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        e >>= 1;
    }
    return r;
}

int main() {
    std::vector<bool> is_prime(LIMIT + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; (int64_t)p * p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        for (int64_t q = (int64_t)p * p; q <= LIMIT; q += p)
            is_prime[(size_t)q] = false;
    }

    uint64_t prime_count = 0;
    uint64_t divisors = 0;
    for (int p = 2; p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        ++prime_count;
        // p divides Z=2^A-3^Q iff the two modular powers agree.
        if (powmod(2, A, p) == powmod(3, Q, p)) {
            ++divisors;
            std::cout << "unexpected_divisor=" << p << "\n";
        }
    }

    assert(prime_count == 3001134ULL);
    assert(divisors == 0ULL);

    std::cout << "PASS first-resonance gap-modulus roughness below 50,000,000\n";
    std::cout << "primes_checked=" << prime_count << "\n";
    std::cout << "prime_divisors_found=" << divisors << "\n";
    return 0;
}
