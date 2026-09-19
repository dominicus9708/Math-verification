// MATH-234 exact post-r10 multi-source SAFE-horizon quotient audit.
//
// Input: frozen MATH-115 r=10 target AP rows
//   a<TAB>b<TAB>m
// representing a+b*k, 0<=k<m.
//
// This is the unchanged MATH-108 parity split/merge geometry, except that
// singleton children are emitted from the symbolic state instead of being
// propagated further.  MATH-197 proves every step while multiplicity >=2 is
// resolution-Bellman-safe, so this program measures exactly the finite
// multi-source SAFE prefix before singleton handoff.
//
// No singleton-tail closure and no r=10 layer closure are claimed.\n// Workflow trigger revision: exact quotient-state measurement.
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

struct AP { cpp_int a,b; u64 m; };
struct Interval { cpp_int b,r,k0,k1; };

static cpp_int parse_big(const std::string& s) {
    cpp_int x=0;
    for(char c:s){ assert(c>='0'&&c<='9'); x*=10; x+=unsigned(c-'0'); }
    return x;
}

static std::vector<AP> merge_multi(const std::vector<AP>& input) {
    std::vector<Interval> v;
    v.reserve(input.size());
    for (const auto& x: input) {
        assert(x.m>=2 && x.b>0 && (x.b&1)!=0);
        cpp_int r=x.a%x.b;
        cpp_int k0=(x.a-r)/x.b;
        cpp_int k1=k0+(x.m-1);
        v.push_back({x.b,r,k0,k1});
    }
    std::sort(v.begin(),v.end(),[](const Interval&x,const Interval&y){
        if(x.b!=y.b)return x.b<y.b;
        if(x.r!=y.r)return x.r<y.r;
        if(x.k0!=y.k0)return x.k0<y.k0;
        return x.k1<y.k1;
    });
    std::vector<AP> out;
    for(std::size_t i=0;i<v.size();) {
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

static cpp_int union_mass(const std::vector<AP>& s) {
    cpp_int z=0;
    for(const auto& x:s) z+=x.m;
    return z;
}

struct StepResult {
    std::vector<AP> multi;
    cpp_int singleton_records = 0; // exact emitted records before cross-parent dedup
    cpp_int closed_floor_records = 0;
};

static StepResult advance(const std::vector<AP>& state) {
    std::vector<AP> raw;
    raw.reserve(state.size()*2);
    StepResult ans;

    for (auto x: state) {
        assert(x.m>=2 && (x.b&1)!=0);

        // Remove the initial AP segment already at/below the frozen floor.
        if (x.a<=LO) {
            cpp_int t=(LO-x.a)/x.b;
            if(t>=cpp_int(x.m-1)) {
                ans.closed_floor_records += x.m;
                continue;
            }
            u64 drop=t.convert_to<u64>()+1;
            ans.closed_floor_records += drop;
            x.a += x.b*drop;
            x.m -= drop;
        }

        for(u64 rho=0;rho<=1;++rho) {
            if(rho>=x.m)continue;
            u64 count=(x.m-1-rho)/2+1;
            cpp_int base=x.a+x.b*rho;
            cpp_int a1,b1;
            if((base&1)==0){ a1=base/2; b1=x.b; }
            else { a1=(3*base+1)/2; b1=3*x.b; }

            if(count==1) {
                if(a1>LO) ans.singleton_records += 1;
                else ans.closed_floor_records += 1;
            } else {
                raw.push_back({std::move(a1),std::move(b1),count});
            }
        }
    }
    ans.multi=merge_multi(raw);
    return ans;
}

int main() {
    std::vector<AP> raw;
    std::string as,bs;
    u64 m;
    u64 rows=0;
    cpp_int occurrence_mass=0;
    while(std::cin>>as>>bs>>m) {
        AP x{parse_big(as),parse_big(bs),m};
        assert(x.b>0 && (x.b&1)!=0 && x.m>0);
        ++rows; occurrence_mass+=m;
        if(m>=2) raw.push_back(std::move(x));
        // input singleton rows are already terminal handoffs and are not part
        // of the multi-source SAFE state.
    }
    assert(rows==278725);
    assert(occurrence_mass==cpp_int("27557263803397"));

    auto state=merge_multi(raw);
    std::cerr<<"depth=0"
             <<" multi_ap="<<state.size()
             <<" union_multi_mass="<<union_mass(state)
             <<"\n";

    cpp_int emitted_singletons=0;
    cpp_int floor_closed=0;
    int last_nonempty=0;

    for(int depth=1;depth<=MAX_DEPTH;++depth) {
        StepResult x=advance(state);
        emitted_singletons += x.singleton_records;
        floor_closed += x.closed_floor_records;
        state=std::move(x.multi);
        if(!state.empty()) last_nonempty=depth;

        std::cerr<<"depth="<<depth
                 <<" multi_ap="<<state.size()
                 <<" union_multi_mass="<<union_mass(state)
                 <<" emitted_singleton_records_step="<<x.singleton_records
                 <<" emitted_singleton_records_total="<<emitted_singletons
                 <<" floor_closed_records_total="<<floor_closed
                 <<"\n";
        if(state.empty()) break;
    }

    // MATH-225: no r=10 output family has initial R>40.  Therefore every
    // exact member still represented after 40 parity decisions would
    // contradict source-resolution exhaustion.
    assert(state.empty());

    std::cerr<<"PASS MATH-234 post-r10 multi-source SAFE horizon"
             <<" last_nonempty_depth="<<last_nonempty
             <<" emitted_singleton_records="<<emitted_singletons
             <<" floor_closed_records="<<floor_closed
             <<"\n";
    std::cerr<<"NO SINGLETON-TAIL CLOSURE CLAIM\n";
    std::cerr<<"NO r10 LAYER CLOSURE CLAIM\n";
    return 0;
}
