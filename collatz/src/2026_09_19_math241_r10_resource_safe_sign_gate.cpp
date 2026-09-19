// MATH-241 resource-safe exact coefficient-sign gate for the post-J r=10 set.
//
// Same mathematics as MATH-240:
//   endpoint <= 2^71 => closed by frozen-floor induction;
//   H<=183 and 3^Q<2^H => closed by MATH-239;
//   H<=183 and coefficient contraction => MATH-239 sign closure;
//   after H=183, continue exact AP dynamics without sign pruning.
//
// Difference: execution is recursively split if the exact union state exceeds
// STATE_CAP.  Splitting is only along the original affine parameter interval
// B+3^Q s, 0<=s<M, hence is an exact set identity and not mathematical pruning.
//
// Input rows: H Q A B M (MATH-235 post-J exporter).
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64=std::uint64_t;

static const cpp_int LO=cpp_int(1)<<71;
static const int SIGN_DEPTH_MAX=183;
static const int MAX_ROUNDS=1000;
static const std::size_t STATE_CAP=750000;

struct Src { int H,Q; cpp_int B; u64 m; };
struct AP  { int H,Q; cpp_int a; u64 m; };
struct I   { int H,Q; cpp_int r,k0,k1; };
struct TooBig {};

static cpp_int parse_big(const std::string&s){
    cpp_int x=0;
    for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=unsigned(c-'0');}
    return x;
}
static cpp_int pow3(int q){cpp_int x=1;for(int i=0;i<q;++i)x*=3;return x;}

static std::vector<AP> merge_state(const std::vector<AP>& input){
    if(input.size()>STATE_CAP) throw TooBig{};
    std::vector<I> v; v.reserve(input.size());
    for(const auto&x:input){
        assert(x.m>=1);
        cpp_int b=pow3(x.Q);
        cpp_int r=x.a%b;if(r<0)r+=b;
        cpp_int k0=(x.a-r)/b,k1=k0+(x.m-1);
        v.push_back({x.H,x.Q,r,k0,k1});
    }
    std::sort(v.begin(),v.end(),[](const I&x,const I&y){
        if(x.H!=y.H)return x.H<y.H;
        if(x.Q!=y.Q)return x.Q<y.Q;
        if(x.r!=y.r)return x.r<y.r;
        if(x.k0!=y.k0)return x.k0<y.k0;
        return x.k1<y.k1;
    });
    std::vector<AP> out;
    out.reserve(v.size());
    for(std::size_t i=0;i<v.size();){
        auto cur=v[i];
        cpp_int lo=cur.k0,hi=cur.k1;
        std::size_t j=i+1;
        while(j<v.size()&&v[j].H==cur.H&&v[j].Q==cur.Q&&
              v[j].r==cur.r&&v[j].k0<=hi+1){
            if(v[j].k1>hi)hi=v[j].k1;
            ++j;
        }
        cpp_int width=hi-lo+1;
        assert(width<=std::numeric_limits<u64>::max());
        cpp_int b=pow3(cur.Q);
        out.push_back({cur.H,cur.Q,cur.r+b*lo,width.convert_to<u64>()});
        if(out.size()>STATE_CAP) throw TooBig{};
        i=j;
    }
    return out;
}

struct Step {
    std::vector<AP> next;
};

static Step advance(const std::vector<AP>&state){
    if(state.size()>STATE_CAP) throw TooBig{};
    std::vector<AP> raw;
    raw.reserve(std::min<std::size_t>(STATE_CAP,state.size()*2));
    Step ans;

    for(auto x:state){
        cpp_int b=pow3(x.Q);

        if(x.a<=LO){
            cpp_int t=(LO-x.a)/b;
            if(t>=cpp_int(x.m-1)) continue;
            u64 drop=t.convert_to<u64>()+1;
            x.a+=b*drop; x.m-=drop;
        }

        for(u64 rho=0;rho<=1;++rho){
            if(rho>=x.m)continue;
            u64 cnt=(x.m-1-rho)/2+1;
            cpp_int base=x.a+b*rho;
            int bit=(base&1)!=0;
            int H1=x.H+1,Q1=x.Q+bit;
            cpp_int a1;
            if(bit) a1=(3*base+1)/2;
            else a1=base/2;
            cpp_int b1=pow3(Q1);

            if(a1<=LO){
                cpp_int t=(LO-a1)/b1;
                if(t>=cpp_int(cnt-1)) continue;
                u64 drop=t.convert_to<u64>()+1;
                a1+=b1*drop; cnt-=drop;
            }

            cpp_int two=cpp_int(1)<<H1;
            assert(b1!=two);
            if(H1<=SIGN_DEPTH_MAX && b1<two) continue;

            // Beyond depth 183 we simply stop using MATH-239 sign pruning.
            // Exact AP propagation and frozen-floor closure remain valid at
            // arbitrary depth.
            raw.push_back({H1,Q1,a1,cnt});

            if(raw.size()>2*STATE_CAP) throw TooBig{};
        }
    }
    ans.next=merge_state(raw);
    return ans;
}

struct Stats {
    u64 audit_leaves=0;
    u64 resource_splits=0;
    u64 source_interval_splits=0;
    std::size_t max_state=0;
    int max_rounds=0;
    u64 depth_limit_leaves=0;
};

static cpp_int mass(const std::vector<AP>&v){
    cpp_int z=0;for(const auto&x:v)z+=x.m;return z;
}

static void audit(std::vector<Src> raw, Stats& stats){
    try{
        std::vector<AP> init; init.reserve(raw.size());
        for(const auto&s:raw) init.push_back({s.H,s.Q,s.B,s.m});
        auto state=merge_state(init);
        stats.max_state=std::max(stats.max_state,state.size());

        int rounds=0;
        while(!state.empty()){
            Step z=advance(state);
            ++rounds;
            stats.max_state=std::max(stats.max_state,z.next.size());
            state=std::move(z.next);
            if(rounds>=MAX_ROUNDS && !state.empty()){
                ++stats.depth_limit_leaves;
                return;
            }
        }
        stats.max_rounds=std::max(stats.max_rounds,rounds);
        ++stats.audit_leaves;
        return;
    } catch(const TooBig&){
        ++stats.resource_splits;
        if(raw.size()>1){
            std::size_t mid=raw.size()/2;
            std::vector<Src> left(raw.begin(),raw.begin()+mid);
            std::vector<Src> right(raw.begin()+mid,raw.end());
            audit(std::move(left),stats);
            audit(std::move(right),stats);
            return;
        }

        Src x=raw.front();
        assert(x.m>1);
        u64 m1=x.m/2,m2=x.m-m1;
        Src y{x.H,x.Q,x.B+pow3(x.Q)*m1,m2};
        x.m=m1;
        ++stats.source_interval_splits;
        audit(std::vector<Src>{x},stats);
        audit(std::vector<Src>{y},stats);
    }
}

int main(){
    std::vector<Src> raw;
    std::string Hs,Qs,As,Bs,Ms;
    u64 rows=0; cpp_int input_mass=0;

    while(std::cin>>Hs>>Qs>>As>>Bs>>Ms){
        int H=std::stoi(Hs),Q=std::stoi(Qs);
        cpp_int A=parse_big(As),B=parse_big(Bs);
        u64 M=std::stoull(Ms);
        (void)A;
        assert(pow3(Q)>(cpp_int(1)<<H));
        raw.push_back({H,Q,B,M});
        ++rows; input_mass+=M;
    }

    assert(rows>0);
    Stats stats;
    audit(std::move(raw),stats);

    std::cerr<<"MATH-241_SUMMARY"
             <<" input_rows="<<rows
             <<" input_mass="<<input_mass
             <<" audit_leaves="<<stats.audit_leaves
             <<" resource_splits="<<stats.resource_splits
             <<" source_interval_splits="<<stats.source_interval_splits
             <<" max_state="<<stats.max_state
             <<" max_rounds="<<stats.max_rounds
             <<" depth_limit_leaves="<<stats.depth_limit_leaves
             <<"\n";

    if(stats.depth_limit_leaves==0){
        std::cerr<<"PASS MATH-241 resource-safe exact closure: every state reaches floor/sign closure\n";
        return 0;
    }
    std::cerr<<"MATH-241 OPEN: at least one exact resource leaf survives 1000 additional shortcut rounds\n";
    return 3;
}
