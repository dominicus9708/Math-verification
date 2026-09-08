// MATH-038: sparse Hensel-event audit for the minimal q layer at depth 35.
//
// At depth 34 MATH-037 found five q=22 collision classes.  Since the
// coefficient floor at depth 35 is q_min(35)=23, only their odd children can
// remain in the coefficient-surviving language.  This certificate computes
// the genuinely new q=23 even/odd cross-branch intersections and verifies that
// they are disjoint from those five inherited collision classes.
//
// Scope warning: this certificate audits the q=23 layer at depth 35. It does
// not assert that no additional collisions occur at q>23.

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>

using u64 = std::uint64_t;
static int qminv[35];
static u64 p3[40];

static void collect_target(int k, int q, u64 C, int target, std::vector<u64>& out) {
    if (q > target || q + (34 - k) < target) return;
    if (k == 34) {
        if (q == target) out.push_back(C % p3[q]);
        return;
    }
    const int nk = k + 1;
    if (q >= qminv[nk]) collect_target(nk, q, C, target, out);
    if (q + 1 >= qminv[nk])
        collect_target(nk, q + 1, 3 * C + (1ULL << k), target, out);
}

template<class F>
static void stream_target(int k, int q, u64 C, int target, F&& fn) {
    if (q > target || q + (34 - k) < target) return;
    if (k == 34) {
        if (q == target) fn(C);
        return;
    }
    const int nk = k + 1;
    if (q >= qminv[nk]) stream_target(nk, q, C, target, fn);
    if (q + 1 >= qminv[nk])
        stream_target(nk, q + 1, 3 * C + (1ULL << k), target, fn);
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 40; ++i) p3[i] = p3[i - 1] * 3ULL;
    for (int k = 1; k <= 34; ++k) {
        int q = 0;
        u64 a = 1, target = 1ULL << k;
        while (a < target) { a *= 3ULL; ++q; }
        qminv[k] = q;
    }
    assert(qminv[35 - 1] == 22); // q_min(34)=22
    // q_min(35)=23 is used for the child-selection interpretation below.

    std::vector<u64> even_q23;
    even_q23.reserve(49'000'000);
    collect_target(0, 0, 0, 23, even_q23);
    assert(even_q23.size() == 47'993'022ULL);
    std::sort(even_q23.begin(), even_q23.end());
    for (std::size_t i = 1; i < even_q23.size(); ++i)
        assert(even_q23[i - 1] != even_q23[i]);

    const u64 mod23 = p3[23];
    const u64 add = 1ULL << 34;
    std::vector<u64> cross_targets;
    u64 q22_words = 0;

    const std::unordered_set<u64> duplicated_q22_parent_classes = {
        4'015'726'592ULL,
        4'559'922'176ULL,
        5'240'166'656ULL,
        8'585'544'704ULL,
        9'875'489'792ULL
    };
    u64 duplicated_parent_cross_hits = 0;

    stream_target(0, 0, 0, 22, [&](u64 C) {
        ++q22_words;
        const u64 parent_r = C % p3[22];
        const u64 child_r = (3 * C + add) % mod23;
        if (std::binary_search(even_q23.begin(), even_q23.end(), child_r)) {
            cross_targets.push_back(child_r);
            if (duplicated_q22_parent_classes.count(parent_r))
                ++duplicated_parent_cross_hits;
        }
    });

    assert(q22_words == 39'993'895ULL);
    assert(cross_targets.size() == 15ULL);
    assert(duplicated_parent_cross_hits == 0ULL);

    std::sort(cross_targets.begin(), cross_targets.end());
    auto ue = std::unique(cross_targets.begin(), cross_targets.end());
    assert(std::distance(cross_targets.begin(), ue) == 15);

    const std::array<u64,15> expected_cross = {
        2'406'940'672ULL,
        3'935'764'480ULL,
        5'762'080'768ULL,
        6'124'822'528ULL,
        7'394'667'520ULL,
        7'576'066'048ULL,
        7'757'409'280ULL,
        7'984'212'736ULL,
        9'435'400'960ULL,
        9'798'142'720ULL,
        16'342'147'072ULL,
        17'974'733'824ULL,
        20'015'467'264ULL,
        30'051'601'408ULL,
        33'921'436'672ULL
    };
    for (int i = 0; i < 15; ++i) assert(cross_targets[i] == expected_cross[i]);

    // Odd-child images of the five depth-34 q=22 collision classes.
    std::vector<u64> inherited;
    for (u64 r : duplicated_q22_parent_classes)
        inherited.push_back((3 * r + add) % mod23);
    std::sort(inherited.begin(), inherited.end());
    assert(inherited.size() == 5ULL);
    for (u64 r : inherited)
        assert(!std::binary_search(cross_targets.begin(), cross_targets.end(), r));

    std::cout << "PASS MATH-038\n";
    std::cout << "depth34 q23 parent classes=" << even_q23.size() << "\n";
    std::cout << "depth34 q22 words=" << q22_words << "\n";
    std::cout << "new depth35 q23 cross classes=" << cross_targets.size() << "\n";
    std::cout << "inherited depth35 q23 collision classes=" << inherited.size() << "\n";
    std::cout << "overlap=0\n";
    std::cout << "scope: q=23 layer only; q>23 not closed by this certificate\n";
    std::cout << "first universal cell: OPEN\nCollatz: OPEN\n";
}
