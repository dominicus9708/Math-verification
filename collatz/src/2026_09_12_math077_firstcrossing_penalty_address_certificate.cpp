// MATH-077 — first-crossing mechanical penalty vs dyadic address audit.
// Exact finite regression through depth 26.
//
// For each first coefficient-crossing depth j, all candidates have the same q.
// Let m be the unique candidate with maximal correction C (the mechanical
// envelope), and define Delta r = r_w-r_m. Then
//
//   2^j (y_m-y_w) = (C_m-C_w) - 3^q Delta r.
//
// Equivalently, with S=C/3^q, rho=2^j/3^q and
// P=S_m-S_w,
//
//   rho (y_m-y_w) = P - Delta r.
//
// The certificate verifies the mechanical maximum, this exact residual, and
// the observed endpoint/address ordering through depth 26.
// Collatz remains OPEN.

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using u64=uint64_t; using u128=__uint128_t;
struct State {u64 y,r; uint8_t q;};
static std::string u128s(u128 x){if(x==0)return"0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}std::reverse(s.begin(),s.end());return s;}
int main(){
 const int K=26;u64 p2[K+2],p3[K+2];p2[0]=p3[0]=1;for(int i=1;i<K+2;i++){p2[i]=2*p2[i-1];p3[i]=3*p3[i-1];}
 std::vector<State> cur{{0,0,0}};u64 total_cross=0,total_resfail=0,total_envfail=0,total_nontrivial_equal=0,total_order_fail=0;
 for(int k=0;k<K;k++){
  int j=k+1;u64 v=p2[k];std::vector<State> next;next.reserve(cur.size()*2);
  struct Cross{u64 y,r;uint8_t q;u128 corr;};std::vector<Cross> cross;
  for(auto const&s:cur){u64 u=p3[s.q];for(int p=0;p<2;p++){
   int c=p^(s.y&1ULL);u64 r=s.r+(c?v:0);u64 pre=s.y+(c?u:0);u64 y=p?(3*pre+1)/2:pre/2;int q=s.q+p;
   u128 corr=(u128)p2[j]*y-(u128)p3[q]*r;
   if(p3[q]>=p2[j])next.push_back({y,r,(uint8_t)q});else cross.push_back({y,r,(uint8_t)q,corr});
  }}
  if(!cross.empty()){
   total_cross+=cross.size();auto it=std::max_element(cross.begin(),cross.end(),[](auto const&a,auto const&b){return a.corr<b.corr;});
   u128 Cm=it->corr;u64 rm=it->r,ym=it->y;int qm=it->q;u64 max_count=0;for(auto const&x:cross)if(x.corr==Cm)max_count++;
   u64 below=0,equal=0,above=0,negdr=0,zerodr=0,posdr=0;u128 maxCdef=0;long long mindr=0,maxdr=0;bool init=false;
   for(auto const&w:cross){if(w.q!=qm)return 2;if(w.corr>Cm)total_envfail++;u128 cd=Cm-w.corr;if(cd>maxCdef)maxCdef=cd;long long dr=(long long)w.r-(long long)rm;
    if(!init){mindr=maxdr=dr;init=true;}else{mindr=std::min(mindr,dr);maxdr=std::max(maxdr,dr);}if(dr>0)posdr++;else if(dr<0)negdr++;else zerodr++;
    __int128 lhs=(__int128)p2[j]*((__int128)ym-(__int128)w.y);__int128 rhs=(__int128)cd-(__int128)p3[qm]*dr;if(lhs!=rhs)total_resfail++;
    int sy=(w.y>ym)-(w.y<ym);int sr=(dr>0)-(dr<0);if(sy!=sr)total_order_fail++;
    if(w.y<ym)below++;else if(w.y>ym)above++;else{equal++;if(w.r!=rm)total_nontrivial_equal++;}
   }
   std::cout<<"depth "<<j<<" crossing "<<cross.size()<<" q "<<qm<<" mech_max_unique "<<max_count<<" endpoint_below "<<below<<" equal "<<equal<<" above "<<above<<" dr_neg "<<negdr<<" dr_zero "<<zerodr<<" dr_pos "<<posdr<<" dr_range "<<mindr<<':'<<maxdr<<" max_Cdef "<<u128s(maxCdef)<<'\n';
  }
  cur.swap(next);
 }
 std::cout<<"TOTAL crossing "<<total_cross<<" envelope_fail "<<total_envfail<<" residual_fail "<<total_resfail<<" order_fail "<<total_order_fail<<" nontrivial_equal_endpoint "<<total_nontrivial_equal<<'\n';
}
