#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

// Exact unrestricted length-19 correction/Hensel-class certificate.
//
// For a binary word w of length 19 with q odd symbols, let R(w) be its affine
// correction. In a fixed full-Hensel class R mod 3^q, if R_u>R_w then
//
//     Delta=(R_u-R_w)/3^q
//
// is a positive ordinary *local* predecessor credit: starting u at x-Delta
// and w at x gives exactly the same 19-step endpoint.
//
// This verifier enumerates the COMPLETE 2^19 binary cube (no survival filter),
// so every mechanical-factor/height constrained fibre is a subset. It proves
// the universal local bound
//
//     Delta <= 87381.
//
// IMPORTANT CORRECTION (2026-08-20): for a later block of a hypothetical
// minimal counterexample N, its block start x=T^s(N) is generally only known
// to satisfy x>=N. Therefore x-Delta<x does NOT by itself imply x-Delta<N.
// Local minimality excludes the block immediately only when
//
//     Delta > x-N,
//
// or when a separate prefix-pullback theorem produces an integer smaller
// original start. Thus this file certifies the finite local constant, class
// counts, and merge identity; it does not certify unconditional repeated
// residue-maximality along every later block.
//
// See:
// collatz/notes/2026-08-20-stage3c-pullback-correction-and-safe-stage4.md

using u32 = std::uint32_t;
using u64 = std::uint64_t;

struct Span {
    u64 lo = ~u64(0);
    u64 hi = 0;
    unsigned count = 0;
    void add(u64 x) {
        lo = std::min(lo,x);
        hi = std::max(hi,x);
        ++count;
    }
};

int main() {
    constexpr int L=19;
    std::array<u64,20> p3{};
    p3[0]=1;
    for(int i=1;i<20;++i) p3[i]=3*p3[i-1];

    std::array<std::unordered_map<u64,Span>,20> cls;
    std::array<unsigned,20> word_count{};

    for(u32 mask=0; mask<(1u<<L); ++mask) {
        int q=0;
        u64 R=0;
        for(int i=0;i<L;++i) {
            if((mask>>i)&1u) {
                R=3*R+(u64(1)<<i);
                ++q;
            }
        }
        ++word_count[q];
        cls[q][R%p3[q]].add(R);
    }

    const std::array<unsigned,20> expected_classes{{
        1,2,6,18,54,162,486,1458,4352,11692,
        23557,31072,27469,17527,8411,3048,817,154,19,1
    }};

    u64 global_max_credit=0;
    int max_q=-1;
    unsigned total_classes=0;

    for(int q=0;q<=19;++q) {
        if(cls[q].size()!=expected_classes[q]) return 1;
        total_classes += unsigned(cls[q].size());
        u64 qmax=0;
        for(const auto& [r,sp]:cls[q]) {
            if(sp.count<2) continue;
            const u64 d=(sp.hi-sp.lo)/p3[q];
            qmax=std::max(qmax,d);
        }
        if(qmax>global_max_credit) {
            global_max_credit=qmax;
            max_q=q;
        }
        std::cout << "q " << q
                  << " words " << word_count[q]
                  << " classes " << cls[q].size()
                  << " max_credit " << qmax << "\n";
    }

    if(total_classes!=130'306U) return 2;
    if(global_max_credit!=87'381ULL) return 3;

    std::cout << "total_full_hensel_classes " << total_classes << "\n";
    std::cout << "global_local_credit_max " << global_max_credit
              << " at_q " << max_q << "\n";
    std::cout << "H19 unrestricted local-credit certificate: PASS\n";
    return 0;
}
