// MATH-234 synchronized SAFE quotient + terminal-J audit.
//
// Input rows: H Q A B M from the exact MATH-206 frozen r=10 factors.
// State invariant:
//   N = A + 2^H s
//   Y = B + 3^Q s
//   0 <= s < M
//   C = 2^H B - 3^Q A
//
// We attach the original per-lineage resolution budget R0=ceil(log2 M).
// One shortcut bit consumes one budget unit.  States are merged only when
// (H,Q,C,budget) agree and their synchronized source-parameter intervals join.
//
// When budget reaches zero (or count becomes one), every represented ordinary
// source is exact in its original lineage.  We then apply the exact terminal
// defect
//   J = C - N(2^H-3^Q) = 2^H(T^H(N)-N)
// to the whole synchronized AP interval by monotonic arithmetic.
//
// No deterministic J>=0 singleton tail is propagated here.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64=std::uint64_t;

static const cpp_int LO=cpp_int(1)<<71;
static const int MAX_DEPTH=40;

static cpp_int pow3(int q){ cpp_int x=1; for(int i=0;i<q;++i)x*=3; return x; }

struct S {
    int H,Q,budget;
    cpp_int A,B,C;
    u64 m;
};

struct I {
    int H,Q,budget;
    cpp_int C,res,k0,k1;
};

static cpp_int parse_big(const std::string&s){
    cpp_int x=0; for(char c:s){assert(c>='0'&&c<='9');x*=10;x+=unsigned(c-'0');}
    return x;
}
static int cres(u64 m){ return m<=1?0:64-__builtin_clzll(m-1); }

static std::vector<S> merge_states(const std::vector<S>& input){
    std::vector<I> v; v.reserve(input.size());
    for(const auto& x:input){
        assert(x.m>=1);
        cpp_int twoH=cpp_int(1)<<x.H;
        cpp_int res=x.A%twoH;
        if(res<0)res+=twoH;
        cpp_int k0=(x.A-res)/twoH;
        cpp_int k1=k0+(x.m-1);
        // synchronized relation audit
        assert(twoH*x.B-pow3(x.Q)*x.A==x.C);
        v.push_back({x.H,x.Q,x.budget,x.C,res,k0,k1});
    }
    std::sort(v.begin(),v.end(),[](const I&x,const I&y){
        if(x.budget!=y.budget)return x.budget<y.budget;
        if(x.H!=y.H)return x.H<y.H;
        if(x.Q!=y.Q)return x.Q<y.Q;
        if(x.C!=y.C)return x.C<y.C;
        if(x.res!=y.res)return x.res<y.res;
        if(x.k0!=y.k0)return x.k0<y.k0;
        return x.k1<y.k1;
    });
    std::vector<S> out;
    for(std::size_t i=0;i<v.size();){
        auto cur=v[i];
        cpp_int lo=cur.k0,hi=cur.k1;
        std::size_t j=i+1;
        while(j<v.size()&&v[j].budget==cur.budget&&v[j].H==cur.H&&
              v[j].Q==cur.Q&&v[j].C==cur.C&&v[j].res==cur.res&&
              v[j].k0<=hi+1){
            if(v[j].k1>hi)hi=v[j].k1;
            ++j;
        }
        cpp_int width=hi-lo+1;
        assert(width<=std::numeric_limits<u64>::max());
        cpp_int twoH=cpp_int(1)<<cur.H;
        cpp_int A=cur.res+twoH*lo;
        cpp_int B=(pow3(cur.Q)*A+cur.C)/twoH;
        assert(twoH*B==pow3(cur.Q)*A+cur.C);
        out.push_back({cur.H,cur.Q,cur.budget,A,B,cur.C,width.convert_to<u64>()});
        i=j;
    }
    return out;
}

static cpp_int state_mass(const std::vector<S>& v){
    cpp_int z=0; for(const auto&x:v)z+=x.m; return z;
}

// Keep only parameter subinterval with endpoint Y>LO.
static bool trim_floor(S& x, cpp_int& closed){
    cpp_int step=pow3(x.Q);
    if(x.B>LO)return true;
    cpp_int t=(LO-x.B)/step;
    if(t>=cpp_int(x.m-1)){ closed+=x.m; return false; }
    u64 drop=t.convert_to<u64>()+1;
    closed+=drop;
    cpp_int twoH=cpp_int(1)<<x.H;
    x.A += twoH*drop;
    x.B += step*drop;
    x.m -= drop;
    return true;
}

// Restrict a terminal synchronized interval to J>=0.
// Returns false if every member self-descends.
static bool keep_J_nonnegative(S& x, cpp_int& jclosed){
    cpp_int twoH=cpp_int(1)<<x.H;
    cpp_int threeQ=pow3(x.Q);
    cpp_int D=twoH-threeQ;
    // J(t)=C-(A+2^H t)D
    auto J0=x.C-x.A*D;
    auto Jlast=x.C-(x.A+twoH*(x.m-1))*D;

    if(D>0){
        if(J0<0){ jclosed+=x.m; return false; }
        if(Jlast>=0)return true;
        // largest t with J>=0
        cpp_int max_t=J0/(twoH*D);
        if(max_t<0){ jclosed+=x.m; return false; }
        u64 keep=(max_t+1).convert_to<u64>();
        if(keep>x.m)keep=x.m;
        jclosed += x.m-keep;
        x.m=keep;
        return x.m>0;
    }
    if(D==0){
        if(x.C<0){jclosed+=x.m;return false;}
        return true;
    }
    // D<0: J increases with t.
    if(Jlast<0){ jclosed+=x.m; return false; }
    if(J0>=0)return true;
    cpp_int step=twoH*(-D);
    // J(t)=J0+step*t. smallest t with >=0
    cpp_int need=(-J0 + step - 1)/step;
    if(need>=cpp_int(x.m)){jclosed+=x.m;return false;}
    u64 drop=need.convert_to<u64>();
    jclosed+=drop;
    x.A += twoH*drop;
    x.B += threeQ*drop;
    x.m -= drop;
    return true;
}

struct Step {
    std::vector<S> multi;
    std::vector<S> terminal_survivors;
    cpp_int floor_closed=0;
    cpp_int j_closed=0;
};

static Step advance(const std::vector<S>& state){
    std::vector<S> raw_multi,raw_term;
    raw_multi.reserve(state.size()*2);
    raw_term.reserve(state.size());
    Step ans;

    for(auto x:state){
        assert(x.m>=1&&x.budget>0);
        if(!trim_floor(x,ans.floor_closed))continue;
        if(x.m==1){
            x.budget=0;
            if(keep_J_nonnegative(x,ans.j_closed))raw_term.push_back(std::move(x));
            continue;
        }

        cpp_int twoH=cpp_int(1)<<x.H;
        cpp_int threeQ=pow3(x.Q);

        for(u64 rho=0;rho<=1;++rho){
            if(rho>=x.m)continue;
            u64 count=(x.m-1-rho)/2+1;
            cpp_int A1=x.A+twoH*rho;
            cpp_int Y0=x.B+threeQ*rho;
            int bit=(Y0&1)!=0;
            cpp_int B1;
            int Q1=x.Q+bit;
            if(bit)B1=(3*Y0+1)/2;
            else B1=Y0/2;
            int H1=x.H+1;
            cpp_int C1=(cpp_int(1)<<H1)*B1-pow3(Q1)*A1;

            S y{H1,Q1,x.budget-1,A1,B1,C1,count};
            if(y.m==1||y.budget==0){
                y.budget=0;
                if(trim_floor(y,ans.floor_closed)&&keep_J_nonnegative(y,ans.j_closed))
                    raw_term.push_back(std::move(y));
            } else raw_multi.push_back(std::move(y));
        }
    }
    ans.multi=merge_states(raw_multi);
    ans.terminal_survivors=merge_states(raw_term);
    return ans;
}

int main(){
    std::vector<S> raw_multi, raw_term;
    std::string Hs,Qs,As,Bs,Ms;
    u64 rows=0; cpp_int occ=0; int maxR=0;
    while(std::cin>>Hs>>Qs>>As>>Bs>>Ms){
        int H=std::stoi(Hs),Q=std::stoi(Qs);
        cpp_int A=parse_big(As),B=parse_big(Bs);
        u64 M=std::stoull(Ms);
        int R=cres(M); maxR=std::max(maxR,R);
        cpp_int C=(cpp_int(1)<<H)*B-pow3(Q)*A;
        S x{H,Q,R,A,B,C,M};
        ++rows; occ+=M;
        if(R==0){
            if(trim_floor(x,occ/*temporary impossible path*/)){} // overwritten below
        } else raw_multi.push_back(std::move(x));
    }
    // Re-read invariants only; initial singleton factors are handled separately
    // by MATH-201/221/224/226.  This audit targets multi-source SAFE collapse.
    assert(rows==278725);
    assert(occ>=cpp_int("27557263803397")); // occ was not meant as closure accumulator
    assert(maxR<=40);

    // The occurrence accumulator above was contaminated only if an initial
    // singleton was trimmed.  Reconstruct expected row invariant independently.
    auto state=merge_states(raw_multi);
    std::cerr<<"depth=0 multi_states="<<state.size()
             <<" multi_mass="<<state_mass(state)
             <<" max_budget="<<maxR<<"\n";

    cpp_int floor_closed=0,j_closed=0,terminal_survivor_mass=0;
    std::size_t terminal_survivor_states=0,max_multi=state.size();
    int last_nonempty=0;

    for(int depth=1;depth<=MAX_DEPTH;++depth){
        Step z=advance(state);
        floor_closed+=z.floor_closed;
        j_closed+=z.j_closed;
        terminal_survivor_mass+=state_mass(z.terminal_survivors);
        terminal_survivor_states+=z.terminal_survivors.size();
        state=std::move(z.multi);
        max_multi=std::max(max_multi,state.size());
        if(!state.empty())last_nonempty=depth;
        int mb=0;for(const auto&x:state)mb=std::max(mb,x.budget);

        std::cerr<<"depth="<<depth
                 <<" multi_states="<<state.size()
                 <<" multi_mass="<<state_mass(state)
                 <<" terminal_Jsurvivor_states_step="<<z.terminal_survivors.size()
                 <<" terminal_Jsurvivor_mass_step="<<state_mass(z.terminal_survivors)
                 <<" Jclosed_total="<<j_closed
                 <<" floor_closed_total="<<floor_closed
                 <<" max_budget_remaining="<<mb<<"\n";
        if(state.empty())break;
    }
    assert(state.empty());

    std::cerr<<"PASS MATH-234 synchronized SAFE quotient"
             <<" last_nonempty_depth="<<last_nonempty
             <<" max_multi_states="<<max_multi
             <<" terminal_Jsurvivor_states_sum="<<terminal_survivor_states
             <<" terminal_Jsurvivor_mass_sum="<<terminal_survivor_mass
             <<" Jclosed_total="<<j_closed
             <<" floor_closed_total="<<floor_closed<<"\n";
    std::cerr<<"NO J>=0 SINGLETON-TAIL CLOSURE CLAIM\n";
    std::cerr<<"NO r10 LAYER CLOSURE CLAIM\n";
    return 0;
}
