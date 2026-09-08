// MATH-043 — per-q exact depth-33 one-sided root-Hensel audit.
//
// Candidate side: coefficient-surviving depth-33 words in one selected q-layer.
// Competitor side: arbitrary depth-33 words in the same Hensel class.
//
// Run once for each q=21..33 and combine with the companion post-audit.
// q=21 is the heaviest layer; OpenMP partitions arbitrary zero-position
// combinations by the smallest zero position. Hash keys are immutable after
// construction and only the stored maximum correction is atomically updated.
//
// Build: g++ -O3 -fopenmp -std=c++17 <file> -o m43
// Example: OMP_NUM_THREADS=5 ./m43 21
// Collatz and the first universal Farey cell remain OPEN.

#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u64 = uint64_t;

static const int K = 33;
static const int QMIN[34] = {
    0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,
    16,16,17,18,18,19,19,20,21,21
};

static const u64 EXP_CAND[34] = {
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    13472296ULL,26521599ULL,21471423ULL,12540223ULL,5731598ULL,
    2124991ULL,641665ULL,156239ULL,30038ULL,4400ULL,462ULL,31ULL,1ULL
};

static const u64 EXP_SURV[34] = {
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    10907449ULL,21566825ULL,17584670ULL,10361536ULL,4788202ULL,
    1798808ULL,551671ULL,136784ULL,26841ULL,4025ULL,434ULL,31ULL,1ULL
};

static const u64 EXP_ARB[34] = {
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    354817320ULL,193536720ULL,92561040ULL,38567100ULL,13884156ULL,
    4272048ULL,1107568ULL,237336ULL,40920ULL,5456ULL,528ULL,33ULL,1ULL
};

static inline u64 mix64(u64 x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

struct FlatMax {
    vector<u64> key, val;
    size_t mask;

    explicit FlatMax(size_t n) {
        size_t cap = 1;
        while (cap < n * 2) cap <<= 1;
        key.assign(cap, UINT64_MAX);
        val.assign(cap, 0);
        mask = cap - 1;
    }

    size_t slot(u64 k) const {
        size_t i = (size_t)mix64(k) & mask;
        while (true) {
            u64 x = key[i];
            if (x == UINT64_MAX || x == k) return i;
            i = (i + 1) & mask;
        }
    }

    void add_key(u64 k) {
        size_t i = slot(k);
        if (key[i] == UINT64_MAX) key[i] = k;
    }

    size_t find_index(u64 k) const {
        size_t i = slot(k);
        return key[i] == k ? i : SIZE_MAX;
    }

    void atomic_update_index(size_t i, u64 C) {
        u64 old = __atomic_load_n(&val[i], __ATOMIC_RELAXED);
        while (old < C &&
               !__atomic_compare_exchange_n(&val[i], &old, C, true,
                                             __ATOMIC_RELAXED, __ATOMIC_RELAXED)) {}
    }

    u64 get(u64 k) const {
        size_t i = slot(k);
        return key[i] == k ? val[i] : UINT64_MAX;
    }
};

vector<u64> candidate;
int target_q;
u64 p2[34], p3[34];

void generate_target(int i, int q, u64 C) {
    int remaining = K - i;
    if (q > target_q || q + remaining < target_q) return;
    if (i == K) {
        if (q == target_q) candidate.push_back(C);
        return;
    }

    int k = i + 1;
    if (q >= QMIN[k])
        generate_target(i + 1, q, C);
    if (q + 1 >= QMIN[k])
        generate_target(i + 1, q + 1, 3 * C + p2[i]);
}

inline u64 correction_from_zero_mask(u64 zmask) {
    u64 C = 0;
    int start = 0;
    u64 z = zmask;
    while (z) {
        int pos = __builtin_ctzll(z);
        int run = pos - start;
        if (run)
            C = p3[run] * C + p2[start] * (p3[run] - p2[run]);
        start = pos + 1;
        z &= z - 1;
    }
    int run = K - start;
    if (run)
        C = p3[run] * C + p2[start] * (p3[run] - p2[run]);
    return C;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        cerr << "usage: certificate q\n";
        return 1;
    }
    target_q = stoi(argv[1]);
    if (target_q < 21 || target_q > 33) return 2;

    p2[0] = p3[0] = 1;
    for (int i = 1; i <= K; ++i) {
        p2[i] = p2[i - 1] * 2ULL;
        p3[i] = p3[i - 1] * 3ULL;
    }

    generate_target(0, 0, 0);
    assert(candidate.size() == EXP_CAND[target_q]);

    const u64 mod = p3[target_q];
    FlatMax H(candidate.size());
    for (u64 C : candidate) H.add_key(C % mod);

    const int d = K - target_q;
    unsigned long long arbitrary_count = 0, target_hits = 0;

    if (d == 0) {
        u64 C = correction_from_zero_mask(0);
        size_t idx = H.find_index(C % mod);
        if (idx != SIZE_MAX) {
            H.atomic_update_index(idx, C);
            ++target_hits;
        }
        arbitrary_count = 1;
    } else {
        const int max_p0 = K - d;

        #pragma omp parallel for schedule(dynamic,1) reduction(+:arbitrary_count,target_hits)
        for (int p0 = 0; p0 <= max_p0; ++p0) {
            int n = K - 1 - p0;
            int need = d - 1;

            if (need == 0) {
                u64 zmask = 1ULL << p0;
                u64 C = correction_from_zero_mask(zmask);
                size_t idx = H.find_index(C % mod);
                if (idx != SIZE_MAX) {
                    H.atomic_update_index(idx, C);
                    ++target_hits;
                }
                ++arbitrary_count;
                continue;
            }

            if (n < need) continue;
            u64 comb = (1ULL << need) - 1ULL;
            const u64 limit = 1ULL << n;

            while (comb < limit) {
                u64 zmask = (1ULL << p0) | (comb << (p0 + 1));
                u64 C = correction_from_zero_mask(zmask);
                size_t idx = H.find_index(C % mod);
                if (idx != SIZE_MAX) {
                    H.atomic_update_index(idx, C);
                    ++target_hits;
                }
                ++arbitrary_count;

                u64 x = comb & (~comb + 1);
                u64 y = comb + x;
                u64 next = (((comb & ~y) / x) >> 1) | y;
                if (next >= limit) break;
                comb = next;
            }
        }
    }

    assert(arbitrary_count == EXP_ARB[target_q]);

    u64 survive = 0;
    for (u64 C : candidate) {
        u64 best = H.get(C % mod);
        assert(best != UINT64_MAX && best >= C);
        if (best == C) ++survive;
    }

    assert(survive == EXP_SURV[target_q]);

    cout << "q=" << target_q
         << " candidates=" << candidate.size()
         << " arbitrary=" << arbitrary_count
         << " target_hits=" << target_hits
         << " survive=" << survive
         << " pruned=" << (candidate.size() - survive) << "\n";
    cout << "FINITE EXACT q-layer; first cell and Collatz remain OPEN.\n";
}
