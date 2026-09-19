// MATH-234 exact post-r10 multi-source SAFE-horizon quotient audit.
//
// Input: frozen MATH-115 r=10 target AP rows a<TAB>b<TAB>m.
//
// Each input AP receives its own resolution budget
//   R0 = ceil(log2 m).
// Exact parity refinement consumes one budget bit per shortcut decision.
// We merge AP intervals ONLY when they carry the same remaining budget.
// This preserves MATH-197's per-lineage source-resolution meaning.
//
// When an output has budget 0 (or count 1), every represented ordinary value
// is an exact singleton in its original lineage.  Such outputs are moved to a
// terminal AP-union channel and are not propagated as multi-source SAFE state.
//
// No singleton-tail closure and no r=10 layer closure are claimed.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <tuple>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;

static const cpp_int LO = cpp_int(1) << 71;
static const int MAX_DEPTH = 40;

struct AP { cpp_int a,b; u64 m; int budget; };
struct PlainAP { cpp_int a,b; u64 m; };
struct Interval { cpp_int b,r,k0,k1; int budget; };

static cpp_int parse_big(const std::string& s) {
    cpp_int x=0;
    for(char c:s){ assert(c>='0'&&c<='9'); x*=10; x+=unsigned(c-'0'); }
    return x;
}

static int cres(u64 m) {
    if(m<=1) return 0;
    return 64 - __builtin_clzll(m-1);
}

static std::vector<AP> merge_multi(const std::vector<AP>& input) {
    std::vector<Interval> v;
    v.reserve(input.size());
    for (const auto& x: input) {
        assert(x.m>=2 && x.b>0 && (x.b&1)!=0 && x.budget>0);
        cpp_int r=x.a%x.b;
        cpp_int k0=(x.a-r)/x.b;
        cpp_int k1=k0+(x.m-1);
        v.push_back({x.b,r,k0,k1,x.budget});
    }
    std::sort(v.begin(),v.end(),[](const Interval&x,const Interval&y){
        if(x.budget!=y.budget)return x.budget<y.budget;
        if(x.b!=y.b)return x.b<y.b;
        if(x.r!=y.r)return x.r<y.r;
        if(x.k0!=y.k0)return x.k0<y.k0;
        return x.k1<y.k1;
    });
    std::vector<AP> out;
    for(std::size_t i=0;i<v.size();) {
        int budget=v[i].budget;
        cpp_int b=v[i].b,r=v[i].r,lo=v[i].k0,hi=v[i].k1;
        std::size_t j=i+1;
        while(j<v.size()&&v[j].budget==budget&&v[j].b==b&&v[j].r==r&&v[j].k0<=hi+1){
            if(v[j].k1>hi)hi=v[j].k1;
            ++j;
        }
        cpp_int width=hi-lo+1;
        assert(width<=std::numeric_limits<u64>::max());
        u64 m=width.convert_to<u64>();
        if(m>=2) out.push_back({r+b*lo,b,m,budget});
        // m==1 is already an exact singleton and is emitted by advance;
        // initial normalization handles it separately.
        i=j;
    }
    return out;
}

static std::vector<PlainAP> merge_plain(const std::vector<PlainAP>& input) {
    struct I { cpp_int b,r,k0,k1; };
    std::vector<I> v; v.reserve(input.size());
    for(const auto& x:input){
        assert(x.m>=1 && x.b>0 && (x.b&1)!=0);
        cpp_int r=x.a%x.b, k0=(x.a-r)/x.b, k1=k0+(x.m-1);
        v.push_back({x.b,r,k0,k1});
    }
    std::sort(v.begin(),v.end(),[](const I&x,const I&y){
        if(x.b!=y.b)return x.b<y.b;
        if(x.r!=y.r)return x.r<y.r;
        if(x.k0!=y.k0)return x.k0<y.k0;
        return x.k1<y.k1;
    });
    std::vector<PlainAP> out;
    for(std::size_t i=0;i<v.size();){
        cpp_int b=v[i].b,r=v[i].r,lo=v[i].k0,hi=v[i].k1;
        std::size_t j=i+1;
        while(j<v.size()&&v[j].b==b&&v[j].r==r&&v[j].k0<=hi+1){
            if(v[j].k1>hi)hi=v[j].k1;
            ++j;
        }
        cpp_int width=hi-lo+1;
        assert(width<=std::numeric_limits<u64>::max());
        out.push_back({r+b*lo,b,width.convert_to<u64>()});
        i=j;
    }
    return out;
}

template<class T>
static cpp_int mass(const std::vector<T>& s) {
    cpp_int z=0; for(const auto& x:s) z+=x.m; return z;
}

struct StepResult {
    std::vector<AP> multi;
    std::vector<PlainAP> terminal;
    cpp_int floor_closed_records=0;
};

static StepResult advance(const std::vector<AP>& state) {
    std::vector<AP> raw_multi;
    std::vector<PlainAP> raw_terminal;
    raw_multi.reserve(state.size()*2);
    raw_terminal.reserve(state.size());
    StepResult ans;

    for(auto x:state) {
        assert(x.m>=2 && x.budget>0 && (x.b&1)!=0);

        if(x.a<=LO) {
            cpp_int t=(LO-x.a)/x.b;
            if(t>=cpp_int(x.m-1)) {
                ans.floor_closed_records += x.m;
                continue;
            }
            u64 drop=t.convert_to<u64>()+1;
            ans.floor_closed_records += drop;
            x.a += x.b*drop;
            x.m -= drop;
            if(x.m==1) {
                raw_terminal.push_back({x.a,x.b,1});
                continue;
            }
        }

        for(u64 rho=0;rho<=1;++rho) {
            if(rho>=x.m)continue;
            u64 count=(x.m-1-rho)/2+1;
            cpp_int base=x.a+x.b*rho;
            cpp_int a1,b1;
            if((base&1)==0){ a1=base/2; b1=x.b; }
            else { a1=(3*base+1)/2; b1=3*x.b; }

            if(a1<=LO && count==1) {
                ans.floor_closed_records += 1;
                continue;
            }

            int bnext=x.budget-1;
            if(count==1 || bnext==0) {
                if(a1>LO) raw_terminal.push_back({a1,b1,count});
                else {
                    // For count>1, later AP members may exceed LO; trim first.
                    cpp_int t=(LO-a1)/b1;
                    if(t>=cpp_int(count-1)) ans.floor_closed_records += count;
                    else {
                        u64 drop=t.convert_to<u64>()+1;
                        ans.floor_closed_records += drop;
                        raw_terminal.push_back({a1+b1*drop,b1,count-drop});
                    }
                }
            } else {
                raw_multi.push_back({a1,b1,count,bnext});
            }
        }
    }

    ans.multi=merge_multi(raw_multi);
    ans.terminal=merge_plain(raw_terminal);
    return ans;
}

int main() {
    std::vector<AP> raw_multi;
    std::vector<PlainAP> initial_terminal;
    std::string as,bs; u64 m;
    u64 rows=0; cpp_int occurrence_mass=0;
    int max_budget=0;

    while(std::cin>>as>>bs>>m) {
        cpp_int a=parse_big(as), b=parse_big(bs);
        assert(b>0 && (b&1)!=0 && m>0);
        ++rows; occurrence_mass+=m;
        int R=cres(m); max_budget=std::max(max_budget,R);
        if(R==0) initial_terminal.push_back({a,b,1});
        else raw_multi.push_back({a,b,m,R});
    }
    assert(rows==278725);
    assert(occurrence_mass==cpp_int("27557263803397"));
    assert(max_budget<=40);

    auto state=merge_multi(raw_multi);
    auto term0=merge_plain(initial_terminal);

    std::cerr<<"depth=0"
             <<" multi_ap="<<state.size()
             <<" multi_union_mass="<<mass(state)
             <<" terminal_ap="<<term0.size()
             <<" terminal_union_mass="<<mass(term0)
             <<" max_budget="<<max_budget
             <<"\n";

    cpp_int terminal_union_mass_sum=mass(term0);
    cpp_int floor_closed=0;
    int last_nonempty=0;
    std::size_t max_multi_ap=state.size();

    for(int depth=1;depth<=MAX_DEPTH;++depth) {
        StepResult x=advance(state);
        terminal_union_mass_sum += mass(x.terminal);
        floor_closed += x.floor_closed_records;
        state=std::move(x.multi);
        max_multi_ap=std::max(max_multi_ap,state.size());
        if(!state.empty()) last_nonempty=depth;

        int mb=0; for(const auto& a:state) mb=std::max(mb,a.budget);

        std::cerr<<"depth="<<depth
                 <<" multi_ap="<<state.size()
                 <<" multi_union_mass="<<mass(state)
                 <<" terminal_ap_step="<<x.terminal.size()
                 <<" terminal_union_mass_step="<<mass(x.terminal)
                 <<" terminal_union_mass_sum="<<terminal_union_mass_sum
                 <<" floor_closed_records_total="<<floor_closed
                 <<" max_budget_remaining="<<mb
                 <<"\n";
        if(state.empty()) break;
    }

    assert(state.empty());

    std::cerr<<"PASS MATH-234 post-r10 budget-preserving multi-source SAFE horizon"
             <<" last_nonempty_depth="<<last_nonempty
             <<" max_multi_ap="<<max_multi_ap
             <<" terminal_union_mass_sum="<<terminal_union_mass_sum
             <<" floor_closed_records="<<floor_closed
             <<"\n";
    std::cerr<<"NO SINGLETON-TAIL CLOSURE CLAIM\n";
    std::cerr<<"NO r10 LAYER CLOSURE CLAIM\n";
    return 0;
}
