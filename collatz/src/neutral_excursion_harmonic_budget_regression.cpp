// Finite regression for the neutral-excursion harmonic-budget lemma.
//
// Against the exact first-28 mechanical reference, enumerate every binary word
// whose relative odd-count height never goes below zero.  Whenever a positive
// excursion ends and the next actual odd position is visible inside the finite
// window, verify the algebraic lower bound
//
//     lambda_i = 2^{A_i}/3^i > 1/3.
//
// The theorem is algebraic and not dependent on this finite calculation.
// Build: g++ -O3 -std=c++17 neutral_excursion_harmonic_budget_regression.cpp -o cert

#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
using u64=std::uint64_t; using u32=std::uint32_t;
static const std::string H19="1101101101011011010";
static constexpr int L=28;
std::string mech;
u64 words=0,returns_checked=0,words_with_return=0;
long double min_lambda=10;
int min_p=-1,min_i=-1,min_a=-1;

void audit_word(u32 mask){
    int h=0,refq=0; bool any=false;
    for(int p=0;p<L;p++){
        int m=mech[p]-'0',b=(mask>>p)&1u;
        if(m)++refq;
        int prev=h; h+=b-m;
        if(prev>0&&h==0){
            if(!(m==1&&b==0))std::exit(10);
            int a=-1;
            for(int t=p+1;t<L;t++)if((mask>>t)&1u){a=t;break;}
            if(a>=0){
                int i=refq;
                u64 p3=1;for(int z=0;z<i;z++)p3*=3ULL;
                if(3ULL*(1ULL<<a)<=p3)std::exit(11);
                long double lam=(long double)(1ULL<<a)/(long double)p3;
                if(lam<min_lambda){min_lambda=lam;min_p=p;min_i=i;min_a=a;}
                ++returns_checked;any=true;
            }
        }
    }
    if(any)++words_with_return;
}

void dfs(int i,int h,u32 mask){
    if(i==L){++words;audit_word(mask);return;}
    int m=mech[i]-'0';
    for(int b=0;b<=1;b++){
        int h2=h+b-m;if(h2<0)continue;
        dfs(i+1,h2,mask|(u32(b)<<i));
    }
}

int main(){
    mech=(H19+H19).substr(0,L);
    dfs(0,0,0);
    if(words!=3524586ULL)std::exit(12);
    if(returns_checked!=6441884ULL)std::exit(13);
    if(words_with_return!=2683483ULL)std::exit(14);
    std::cout.precision(18);
    std::cout<<"neutral-excursion harmonic regression: PASS\n";
    std::cout<<"words "<<words<<"\n";
    std::cout<<"returns_checked "<<returns_checked<<"\n";
    std::cout<<"words_with_return "<<words_with_return<<"\n";
    std::cout<<"min_lambda "<<min_lambda
             <<" end_p "<<min_p
             <<" odd_index "<<min_i
             <<" next_odd_pos "<<min_a<<"\n";
}
