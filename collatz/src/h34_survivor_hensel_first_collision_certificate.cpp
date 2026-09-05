#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

// Exact first raw coefficient-survivor Hensel-collision certificate.
//
// The coefficient-surviving Hensel code
//
//   w -> (q, R(w) mod 3^q)
//
// is collision-free through H=33.  At H=34, q=22 is the first tested layer
// with collisions.  This verifier enumerates exactly the coefficient-surviving
// H=34,q=22 words, sorts their complete Hensel residues, and proves:
//
//   survivors = 39,993,895,
//   exactly five residue classes contain two survivors,
//   every collision difference is R'-R = 4*3^22,
//   hence every corresponding root credit is d=4.
//
// This is a finite exact diagnostic supporting the general linear-credit lemma
// d<q/3 for surviving siblings.  It is not a proof of Collatz.

using u64 = std::uint64_t;
using u128 = unsigned __int128;

namespace {
constexpr int H=34;
constexpr int Q=22;
u64 P3[40]{};

struct Rec {
    u64 residue;
    u64 correction;
};

std::vector<Rec> records;

void generate(int pos,int q,u128 R) {
    if (q>Q || q+(H-pos)<Q) return;
    if (pos==H) {
        if (q==Q) {
            assert(R<=u128(UINT64_MAX));
            records.push_back({u64(R%P3[Q]),u64(R)});
        }
        return;
    }

    if (u128(P3[q]) >= (u128(1)<<(pos+1)))
        generate(pos+1,q,R);

    if (u128(P3[q+1]) >= (u128(1)<<(pos+1)))
        generate(pos+1,q+1,3*R+(u128(1)<<pos));
}
}

int main() {
    P3[0]=1;
    for (int i=1;i<40;++i) P3[i]=3*P3[i-1];

    records.reserve(40'000'000);
    generate(0,0,0);
    assert(records.size()==39'993'895ULL);

    std::sort(records.begin(),records.end(),[](const Rec& a,const Rec& b){
        return a.residue<b.residue ||
               (a.residue==b.residue && a.correction<b.correction);
    });

    u64 collision_pairs=0;
    u64 collision_classes=0;
    bool in_collision_class=false;

    for (std::size_t i=1;i<records.size();++i) {
        if (records[i].residue!=records[i-1].residue) {
            in_collision_class=false;
            continue;
        }

        ++collision_pairs;
        if (!in_collision_class) {
            ++collision_classes;
            in_collision_class=true;
        }

        const u64 diff=records[i].correction-records[i-1].correction;
        assert(diff%P3[Q]==0);
        const u64 d=diff/P3[Q];
        assert(d==4);
    }

    assert(collision_pairs==5);
    assert(collision_classes==5);

    std::cout << "H34 q22 survivors=" << records.size() << '\n';
    std::cout << "collision_classes=5 collision_pairs=5\n";
    std::cout << "all survivor-Hensel collision credits d=4\n";
    std::cout << "H34 survivor Hensel first collision: PASS\n";
}
