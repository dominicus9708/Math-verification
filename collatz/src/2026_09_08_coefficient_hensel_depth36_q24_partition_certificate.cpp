// MATH-039: full q=24 Hensel collision layer at depth 36 using external
// residue partitioning.
//
// Child q=24 states at depth 36 come from:
//   source 0: even children of depth-35 q=24 parents;
//   source 1: odd  children of depth-35 q=23 parents.
//
// Records are partitioned by low residue bits so no monolithic 170M-record
// sort is needed.  Inside each bucket, key=(residue<<1)|source is sorted and
// grouped by residue.  This directly counts inherited and genuinely new
// collision classes in the complete q=24 child layer.

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using u64 = std::uint64_t;
using boost::multiprecision::cpp_int;
static const int NB = 128;
static int qminv[36];
static u64 p3[40];
static FILE* files[NB];

static void emit(u64 residue, int source) {
    const u64 key = (residue << 1) | u64(source);
    std::fwrite(&key, sizeof(key), 1, files[residue & (NB - 1)]);
}

static void generate(int k, int q, u64 C) {
    // Only depth-35 q=23 or q=24 parents can feed child q=24.
    if (q > 24 || q + (35 - k) < 23) return;
    if (k == 35) {
        if (q == 24) emit(C % p3[24], 0);
        if (q == 23) emit((3 * C + (1ULL << 35)) % p3[24], 1);
        return;
    }
    const int nk = k + 1;
    if (q >= qminv[nk]) generate(nk, q, C);
    if (q + 1 >= qminv[nk])
        generate(nk, q + 1, 3 * C + (1ULL << k));
}

int main() {
    p3[0] = 1;
    for (int i = 1; i < 40; ++i) p3[i] = p3[i - 1] * 3ULL;

    // Frozen published-floor coefficient thresholds.
    const cpp_int B = cpp_int(1) << 71;
    const cpp_int A = 3 * B + 1;
    cpp_int ap = 1, bp = 1, two = 1;
    int qp = 0;
    for (int k = 1; k <= 35; ++k) {
        two *= 2;
        while (!(ap > two * bp)) { ap *= A; bp *= B; ++qp; }
        qminv[k] = qp;
    }
    assert(qminv[35] == 23);

    const std::string dir = "math039_d36_q24_partitions";
    std::filesystem::create_directories(dir);
    std::vector<std::vector<char>> buffers(NB, std::vector<char>(1 << 20));
    for (int i = 0; i < NB; ++i) {
        const std::string path = dir + "/b" + std::to_string(i) + ".bin";
        files[i] = std::fopen(path.c_str(), "wb");
        assert(files[i]);
        std::setvbuf(files[i], buffers[i].data(), _IOFBF, buffers[i].size());
    }

    generate(0, 0, 0);
    for (int i = 0; i < NB; ++i) std::fclose(files[i]);

    u64 records = 0, classes = 0, collision_classes = 0;
    u64 even_even = 0, odd_odd = 0, even_odd = 0;
    u64 excess_words = 0;
    int max_multiplicity = 0;

    for (int b = 0; b < NB; ++b) {
        const std::string path = dir + "/b" + std::to_string(b) + ".bin";
        std::ifstream in(path, std::ios::binary | std::ios::ate);
        const std::size_t bytes = std::size_t(in.tellg());
        in.seekg(0);
        std::vector<u64> v(bytes / sizeof(u64));
        in.read(reinterpret_cast<char*>(v.data()), bytes);
        in.close();
        records += v.size();
        std::sort(v.begin(), v.end());

        for (std::size_t i = 0; i < v.size();) {
            const u64 residue = v[i] >> 1;
            std::size_t j = i;
            int c0 = 0, c1 = 0;
            while (j < v.size() && (v[j] >> 1) == residue) {
                if (v[j] & 1ULL) ++c1; else ++c0;
                ++j;
            }
            const int m = c0 + c1;
            ++classes;
            max_multiplicity = std::max(max_multiplicity, m);
            if (m > 1) {
                ++collision_classes;
                excess_words += u64(m - 1);
                if (c0 == 2 && c1 == 0) ++even_even;
                else if (c0 == 0 && c1 == 2) ++odd_odd;
                else if (c0 == 1 && c1 == 1) ++even_odd;
                else assert(false && "unexpected multiplicity/source pattern");
            }
            i = j;
        }
        std::filesystem::remove(path);
    }
    std::filesystem::remove(dir);

    assert(records == 169'991'585ULL);
    assert(classes == 169'991'555ULL);
    assert(collision_classes == 30ULL);
    assert(excess_words == 30ULL);
    assert(max_multiplicity == 2);
    assert(even_even == 0ULL);
    assert(odd_odd == 20ULL);
    assert(even_odd == 10ULL);

    std::cout << "PASS MATH-039\n";
    std::cout << "records=" << records << " classes=" << classes << "\n";
    std::cout << "collision classes=" << collision_classes
              << " multiplicity max=" << max_multiplicity << "\n";
    std::cout << "inherited from q24-even parents=" << even_even << "\n";
    std::cout << "inherited from q23-odd parents=" << odd_odd << "\n";
    std::cout << "new even/odd cross classes=" << even_odd << "\n";
    std::cout << "first universal cell: OPEN\nCollatz: OPEN\n";
}
