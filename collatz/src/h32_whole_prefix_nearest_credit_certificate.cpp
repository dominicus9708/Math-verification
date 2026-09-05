#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>

// Exact H=32 whole-prefix nearest-credit certificate.
//
// For each coefficient-surviving length-32 word w with q odd steps and
// correction R_w, define its nearest larger correction in the same complete
// Hensel class by
//
//   d_near(w)=min{(R'-R_w)/3^q : R'>R_w, R'==R_w (mod 3^q)}.
//
// Only existence of one such larger correction is needed for the root
// predecessor M=N-d_near.  There is no need to move all the way to the class
// maximum.  This certificate computes d_near exactly for every terminal
// coefficient-surviving q=21,...,32 layer.
//
// The q=21 layer contains 13,472,296 coefficient survivors and 129,024,480
// unrestricted q-words.  A flat residue table stores only the coefficient
// survivor target in each complete Hensel residue and one pass over a 16+16
// meet-in-the-middle enumeration finds the nearest larger correction.
//
// Exact result:
//   (G_32,q)_{q=21}^{32} = (34,25,12,6,6,1,1,1,1,1,0,0),
// hence G_32=34.
//
// This is a finite exact certificate, not an asymptotic theorem and not a
// proof of the Collatz conjecture.

using u8 = std::uint8_t;
using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {
constexpr int H=32;
std::array<u64,40> P3{};
int Q=0;

struct Flat {
    std::size_t cap,mask,n=0;
    std::vector<u64> key,target_lo,best;
    std::vector<u8> target_hi;

    explicit Flat(std::size_t c)
        : cap(c), mask(c-1), key(c,UINT64_MAX), target_lo(c),
          best(c,UINT64_MAX), target_hi(c) {}

    static inline u64 mix(u64 x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x^(x>>30))*0xbf58476d1ce4e5b9ULL;
        x = (x^(x>>27))*0x94d049bb133111ebULL;
        return x^(x>>31);
    }

    std::size_t slot(u64 k) const {
        std::size_t i=std::size_t(mix(k))&mask;
        for (;;) {
            const u64 z=key[i];
            if (z==k || z==UINT64_MAX) return i;
            i=(i+1)&mask;
        }
    }

    void insert(u64 k,u128 r) {
        const std::size_t i=slot(k);
        assert(key[i]==UINT64_MAX); // target residues are injective here
        key[i]=k;
        target_lo[i]=u64(r);
        target_hi[i]=u8(r>>64);
        ++n;
    }

    void update(u64 k,u128 r) {
        std::size_t i=std::size_t(mix(k))&mask;
        for (;;) {
            const u64 z=key[i];
            if (z==UINT64_MAX) return;
            if (z==k) {
                const u128 target=(u128(target_hi[i])<<64)|target_lo[i];
                if (r>target) {
                    const u128 diff=r-target;
                    const u64 d=u64(diff/P3[Q]);
                    assert(u128(d)*P3[Q]==diff);
                    best[i]=std::min(best[i],d);
                }
                return;
            }
            i=(i+1)&mask;
        }
    }
};

u64 survivor_count=0;
void generate_survivors(int pos,int q,u128 R,Flat& table) {
    if (q>Q || q+(H-pos)<Q) return;
    if (pos==H) {
        if (q==Q) {
            table.insert(u64(R%P3[Q]),R);
            ++survivor_count;
        }
        return;
    }
    if (u128(P3[q]) >= (u128(1)<<(pos+1)))
        generate_survivors(pos+1,q,R,table);
    if (u128(P3[q+1]) >= (u128(1)<<(pos+1)))
        generate_survivors(pos+1,q+1,3*R+(u128(1)<<pos),table);
}

std::array<std::vector<u64>,17> half_corrections(int offset) {
    std::array<std::vector<u64>,17> out;
    for (unsigned mask=0; mask<(1u<<16); ++mask) {
        int q=0;
        u64 R=0;
        for (int j=0;j<16;++j) if ((mask>>j)&1u) {
            const int pos=offset+j;
            R=3*R+(u64(1)<<pos);
            ++q;
        }
        out[q].push_back(R);
    }
    return out;
}

struct Result { u64 survivors,all_words,nonmax,max_near,d1; };

Result run_layer(int q,u64 expected_survivors) {
    Q=q;
    survivor_count=0;
    std::size_t cap=1;
    while (long double(cap)*0.80L < long double(expected_survivors)) cap<<=1;
    Flat table(cap);
    generate_survivors(0,0,0,table);
    assert(survivor_count==expected_survivors);

    static const auto low=half_corrections(0);
    static const auto high=half_corrections(16);
    const u64 mod=P3[Q];
    u64 scanned=0;

    for (int a=std::max(0,Q-16); a<=std::min(16,Q); ++a) {
        const int b=Q-a;
        if (b<0 || b>16) continue;
        const u64 pb=P3[b];
        for (const u64 x:low[a]) {
            const u64 xr=x%mod;
            for (const u64 y:high[b]) {
                const u64 residue=u64((u128(pb)*xr+(y%mod))%mod);
                const u128 full=u128(pb)*x+y;
                table.update(residue,full);
                ++scanned;
            }
        }
    }

    u64 nonmax=0,max_near=0,d1=0;
    for (std::size_t i=0;i<table.cap;++i) {
        if (table.key[i]==UINT64_MAX || table.best[i]==UINT64_MAX) continue;
        ++nonmax;
        max_near=std::max(max_near,table.best[i]);
        if (table.best[i]==1) ++d1;
    }
    return {survivor_count,scanned,nonmax,max_near,d1};
}
} // namespace

int main() {
    P3[0]=1;
    for (int i=1;i<int(P3.size());++i) P3[i]=3*P3[i-1];

    constexpr std::array<u64,12> SURV{
        13'472'296,13'049'303,8'422'120,4'118'103,1'613'495,511'496,
        130'169,26'070,3'968,432,30,1
    };
    constexpr std::array<u64,12> ALL{
        129'024'480,64'512'240,28'048'800,10'518'300,3'365'856,906'192,
        201'376,35'960,4'960,496,32,1
    };
    constexpr std::array<u64,12> NONMAX{
        2'547'774,2'395'727,1'487'316,690'337,252'736,73'352,
        16'606,2'849,348,27,0,0
    };
    constexpr std::array<u64,12> G{
        34,25,12,6,6,1,1,1,1,1,0,0
    };
    constexpr std::array<u64,12> D1{
        2'488'626,2'363'145,1'476'261,688'002,252'458,73'352,
        16'606,2'849,348,27,0,0
    };

    u64 global=0;
    for (int q=21;q<=32;++q) {
        const std::size_t j=std::size_t(q-21);
        const Result r=run_layer(q,SURV[j]);
        assert(r.all_words==ALL[j]);
        assert(r.nonmax==NONMAX[j]);
        assert(r.max_near==G[j]);
        assert(r.d1==D1[j]);
        global=std::max(global,r.max_near);
        std::cout << "q=" << q
                  << " survivors=" << r.survivors
                  << " all_words=" << r.all_words
                  << " nonmax=" << r.nonmax
                  << " G=" << r.max_near
                  << " d1=" << r.d1 << '\n';
    }
    assert(global==34);
    std::cout << "G_32=34\n";
    std::cout << "H32 whole-prefix nearest-credit certificate: PASS\n";
}
