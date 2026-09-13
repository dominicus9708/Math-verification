#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using u64=std::uint64_t;

static constexpr int DOLD=22, DNEW=23;
static constexpr u64 MOD=1ULL<<DNEW;
static constexpr u64 EXPECT_ROWS=605977ULL;
static constexpr u64 EXPECT_MASS=3419719061560ULL;
static constexpr u64 PRIOR_SAFE=3209065424947ULL;
static constexpr u64 PRIOR_TAIL=210653636613ULL;
static constexpr u64 EXPECT_EXTRA=3151665357ULL;
static const cpp_int LO=cpp_int(1)<<71;
static cpp_int p2[24],p3[24];

static cpp_int lim(int d,int q){
  cpp_int cmax=0;
  if(q) cmax=p2[d-q]*(p3[q]-p2[q]);
  return (p2[d]*LO-cmax)/p3[q];
}
static cpp_int parse_big(const std::string&s){
  cpp_int x=0;
  for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=c-'0';}
  return x;
}

int main(int argc,char**argv){
  if(argc<2){std::cerr<<"usage: math130 shard.tsv...\n";return 2;}
  p2[0]=p3[0]=1;
  for(int i=1;i<=23;i++){p2[i]=p2[i-1]*2;p3[i]=p3[i-1]*3;}

  // For each source residue mod 2^23, compute the best old MATH-129
  // threshold from depths 1..22 and the new depth-23 threshold.
  // A residue contributes to the increment exactly for source maxima N with
  // old_limit < N <= new_limit.  This makes the new set disjoint from MATH-129.
  std::vector<cpp_int> starts,ends;
  starts.reserve(MOD/8); ends.reserve(MOD/8);
  u64 improving_residues=0;
  for(u64 r=0;r<MOD;r++){
    u64 x=r; int q=0;
    cpp_int old=-(cpp_int(1)<<200), nw=0;
    for(int d=1;d<=DNEW;d++){
      if(x&1ULL){q++;x=(3*x+1)/2;} else x/=2;
      cpp_int L=lim(d,q);
      if(d<=DOLD){if(L>old)old=L;} else nw=L;
    }
    if(nw>old){starts.push_back(old);ends.push_back(nw);improving_residues++;}
  }
  std::sort(starts.begin(),starts.end());
  std::sort(ends.begin(),ends.end());
  assert(starts.size()==ends.size());

  auto count_new=[&](const cpp_int&N)->u64{
    // intervals are (old_limit,new_limit]; active at N iff old<N<=new.
    auto a=std::lower_bound(starts.begin(),starts.end(),N)-starts.begin();
    auto b=std::lower_bound(ends.begin(),ends.end(),N)-ends.begin();
    assert(a>=b);
    return (u64)(a-b);
  };

  u64 rows=0,total_mass=0,cycle_mass=0,extra=0;
  u64 rows_with_cycles=0,rows_with_gain=0,max_cnew=0;
  for(int fi=1;fi<argc;fi++){
    std::ifstream in(argv[fi]);assert(in);
    std::string as,bs;u64 m;
    while(in>>as>>bs>>m){
      cpp_int a=parse_big(as),b=parse_big(bs),N=a+b*(m-1);
      rows++;total_mass+=m;
      u64 cycles=m/MOD;
      if(!cycles)continue;
      rows_with_cycles++;
      cycle_mass+=cycles*MOD;
      u64 c=count_new(N);
      if(c){
        rows_with_gain++;
        max_cnew=std::max(max_cnew,c);
        extra+=cycles*c;
      }
    }
  }

  assert(rows==EXPECT_ROWS);
  assert(total_mass==EXPECT_MASS);
  assert(extra==EXPECT_EXTRA);
  assert(extra<=PRIOR_TAIL);

  std::cout<<"metric\tvalue\n";
  std::cout<<"prepared_split_pieces\t"<<rows<<"\n";
  std::cout<<"total_occurrence_mass\t"<<total_mass<<"\n";
  std::cout<<"d23_modulus\t"<<MOD<<"\n";
  std::cout<<"d23_residues_with_stronger_threshold\t"<<improving_residues<<"\n";
  std::cout<<"rows_with_complete_d23_cycles\t"<<rows_with_cycles<<"\n";
  std::cout<<"complete_cycle_mass_examined\t"<<cycle_mass<<"\n";
  std::cout<<"rows_with_positive_d23_increment\t"<<rows_with_gain<<"\n";
  std::cout<<"max_new_safe_residues_per_complete_cycle\t"<<max_cnew<<"\n";
  std::cout<<"d23_disjoint_complete_cycle_extra_safe_mass\t"<<extra<<"\n";
  std::cout<<"prior_math129_safe_mass\t"<<PRIOR_SAFE<<"\n";
  std::cout<<"prior_math129_tail_mass\t"<<PRIOR_TAIL<<"\n";
  std::cout<<"conservative_safe_mass_after_d23_increment\t"<<(PRIOR_SAFE+extra)<<"\n";
  std::cout<<"conservative_tail_after_d23_increment\t"<<(PRIOR_TAIL-extra)<<"\n";
  std::cerr<<"PASS MATH-130 disjoint d23 complete-cycle increment\n";
  std::cerr<<"NO r=11 CLOSURE CLAIM\n";
}
