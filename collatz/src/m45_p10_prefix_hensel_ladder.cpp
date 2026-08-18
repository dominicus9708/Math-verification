#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

// Prefix-specific Hensel integerization verifier for the unresolved m=45
// first-defect p=10 channel.
//
// The fixed first eleven time-expanded parity bits are
//
//   11011011011
//
// i.e. the current mechanical prefix with the p=10 zero flipped to one.
// Their odd count is 8 and their exact correction is 12325.
//
// Unlike the global depth-L q-slice builders, this verifier generates only
// coefficient-surviving words extending that fixed prefix.  The alternate
// predecessor search remains unrestricted, so the Hensel kill test is exact
// for every generated p=10 word.
//
// Usage:
//   m45_p10_prefix_hensel_ladder L q
//
// Certified reference rows are included for L=28,...,32.  Nonemptiness is a
// diagnostic only: this file does not close p=10 and does not prove Collatz.

using u64 = std::uint64_t;

namespace {

struct Word { u64 R; int q; };
struct Key {
    std::uint8_t s;
    u64 r;
    bool operator==(const Key& o) const { return s == o.s && r == o.r; }
};
struct KeyHash {
    std::size_t operator()(const Key& k) const noexcept {
        u64 x = k.r ^ (u64(k.s) << 56);
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccdULL;
        x ^= x >> 33;
        return static_cast<std::size_t>(x);
    }
};

constexpr int PREFIX_LEN = 11;
constexpr int PREFIX_Q = 8;
constexpr u64 PREFIX_R = 12'325ULL;

int L = 0;
int target_q = 0;
std::vector<u64> p3;

void generate(int pos, int q, u64 R, std::vector<Word>& out) {
    if (q > target_q || q + (L - pos) < target_q) return;
    if (pos == L) {
        if (q == target_q) out.push_back({R, q});
        return;
    }

    if (p3[q] >= (u64(1) << (pos + 1)))
        generate(pos + 1, q, R, out);

    const u64 R1 = 3 * R + (u64(1) << pos);
    if (p3[q + 1] >= (u64(1) << (pos + 1)))
        generate(pos + 1, q + 1, R1, out);
}

u64 correction(const std::vector<int>& positions) {
    u64 R = 0;
    for (const int x : positions) R = 3 * R + (u64(1) << x);
    return R;
}

void enumerate_later(int start, int need, std::vector<int>& positions, int s,
                     std::unordered_map<Key, u64, KeyHash>& maximum) {
    if (!need) {
        const u64 R = correction(positions);
        auto it = maximum.find(Key{std::uint8_t(s), R % p3[s + 1]});
        if (it != maximum.end() && R > it->second) it->second = R;
        return;
    }
    for (int x = start; x <= L - need; ++x) {
        positions.push_back(x);
        enumerate_later(x + 1, need - 1, positions, s, maximum);
        positions.pop_back();
    }
}

void enumerate_full_q(int start, int need, std::vector<int>& positions,
                      std::unordered_map<u64, u64>& immediate) {
    if (!need) {
        const u64 R = correction(positions);
        auto it = immediate.find(R % p3[target_q]);
        if (it != immediate.end() && R > it->second) it->second = R;
        return;
    }
    for (int x = start; x <= L - need; ++x) {
        positions.push_back(x);
        enumerate_full_q(x + 1, need - 1, positions, immediate);
        positions.pop_back();
    }
}

std::pair<u64,u64> expected(int l, int q) {
    // (coefficient survivors, Hensel retained)
    static const std::unordered_map<int,std::unordered_map<int,std::pair<u64,u64>>> e = {
        {28, {{18,{4348,1397}}, {19,{7775,4572}}, {20,{5068,3467}},
              {21,{2180,1647}}, {22,{658,542}}, {23,{135,120}},
              {24,{17,17}}, {25,{1,1}}}},
        {29, {{19,{12123,5647}}, {20,{12843,7989}}, {21,{7248,5108}},
              {22,{2838,2186}}, {23,{793,661}}, {24,{152,136}},
              {25,{18,18}}, {26,{1,1}}}},
        {30, {{19,{12123,2685}}, {20,{24966,13357}}, {21,{20091,13045}},
              {22,{10086,7288}}, {23,{3631,2844}}, {24,{945,796}},
              {25,{170,153}}, {26,{19,19}}, {27,{1,1}}}},
        {31, {{20,{37089,14323}}, {21,{45057,26114}}, {22,{30177,20279}},
              {23,{13717,10126}}, {24,{4576,3637}}, {25,{1115,948}},
              {26,{189,171}}, {27,{20,20}}, {28,{1,1}}}},
        {32, {{21,{82146,38905}}, {22,{75234,46095}}, {23,{43894,30349}},
              {24,{18293,13757}}, {25,{5691,4582}}, {26,{1304,1118}},
              {27,{209,190}}, {28,{21,21}}, {29,{1,1}}}}
    };
    const auto il = e.find(l);
    if (il == e.end()) return {0,0};
    const auto iq = il->second.find(q);
    if (iq == il->second.end()) return {0,0};
    return iq->second;
}

} // namespace

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: m45_p10_prefix_hensel_ladder L q\n";
        return 1;
    }
    L = std::stoi(argv[1]);
    target_q = std::stoi(argv[2]);
    if (L < 28 || L > 40 || target_q < PREFIX_Q || target_q > L) return 2;

    p3.assign(L + 3, 1);
    for (int i = 1; i < static_cast<int>(p3.size()); ++i) p3[i] = 3 * p3[i - 1];

    std::vector<Word> survivors;
    generate(PREFIX_LEN, PREFIX_Q, PREFIX_R, survivors);

    std::unordered_map<Key, u64, KeyHash> partial;
    std::unordered_map<u64, u64> immediate;
    partial.reserve(survivors.size() * 8ULL + 100);
    immediate.reserve(survivors.size() * 2ULL + 100);

    for (const Word& w : survivors) {
        immediate.emplace(w.R % p3[target_q], 0);
        for (int s = 1; s < target_q; ++s) {
            const u64 base = w.R % p3[s];
            const u64 digit = (w.R / p3[s]) % 3;
            for (u64 a = 0; a < 3; ++a)
                if (a != digit)
                    partial.emplace(Key{std::uint8_t(s), base + a * p3[s]}, 0);
        }
    }

    // Search all possible alternate corrections that can hit one of the
    // target residue keys.  The alternate family is NOT restricted to p=10.
    for (int s = 1; s < target_q; ++s) {
        const int d = target_q - s;
        int pmin = d - 1;
        while (pmin < L && (u64(1) << (pmin + 1)) <= p3[d]) ++pmin;

        for (int pd = pmin; pd <= L - 1 - s; ++pd) {
            const int first = pd - d + 1;
            if (first < 0) continue;
            std::vector<int> positions;
            for (int x = first; x <= pd; ++x) positions.push_back(x);
            enumerate_later(pd + 1, s, positions, s, partial);
        }
    }

    std::vector<int> positions;
    enumerate_full_q(0, target_q, positions, immediate);

    u64 retained = 0;
    for (const Word& w : survivors) {
        bool kill = false;
        for (int s = 1; s < target_q && !kill; ++s) {
            const u64 base = w.R % p3[s];
            const u64 digit = (w.R / p3[s]) % 3;
            for (u64 a = 0; a < 3; ++a) {
                if (a == digit) continue;
                const auto it = partial.find(Key{std::uint8_t(s), base + a * p3[s]});
                if (it != partial.end() && it->second > w.R) {
                    kill = true;
                    break;
                }
            }
        }
        const auto it = immediate.find(w.R % p3[target_q]);
        if (it != immediate.end() && it->second > w.R) kill = true;
        if (!kill) ++retained;
    }

    const auto want = expected(L, target_q);
    if (want.first) {
        if (survivors.size() != want.first || retained != want.second) return 3;
    }

    std::cout << "m45 p10 prefix Hensel: PASS\n";
    std::cout << "L=" << L << " q=" << target_q
              << " coefficient_survivors=" << survivors.size()
              << " retained=" << retained << "\n";
    return 0;
}
