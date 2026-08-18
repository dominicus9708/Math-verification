#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

using u64=uint64_t;
static constexpr int K=9;

std::vector<u64> targets(const std::vector<u64>& c,u64 mod){
    std::vector<u64> out; out.reserve(c.size());
    for(u64 x:c) out.push_back(x?mod-x:0);
    std::sort(out.begin(),out.end());
    return out;
}

int main(){
    std::vector<std::vector<u64>> S(K+1,std::vector<u64>{0});
    u64 mod=1;
    for(int depth=1;depth<=21;depth++){
        mod*=3;
        std::vector<std::vector<u64>> N(K+1);
        for(int a=0;a<=K;a++){
            for(int a2=0;a2<=a;a2++){
                long long delta=(1LL<<a)-(1LL<<a2);
                for(u64 cp:S[a2]){
                    u64 t=3*cp;
                    u64 half=(t&1)?(t+mod)/2:t/2;
                    long long c=(long long)half-delta;
                    c%=(long long)mod; if(c<0)c+=mod;
                    N[a].push_back((u64)c);
                }
            }
            std::sort(N[a].begin(),N[a].end());
            N[a].erase(std::unique(N[a].begin(),N[a].end()),N[a].end());
        }
        S.swap(N);

        if(depth==15 || depth==18){
            auto T=targets(S[K],mod);
            std::vector<u64> bits((mod+63)/64);
            for(u64 x:T) bits[x>>6]|=1ULL<<(x&63);
            const char* fn=depth==15?"k9_15.bits":"k9_18.bits";
            std::ofstream f(fn,std::ios::binary);
            u64 n=bits.size();
            f.write((char*)&mod,8); f.write((char*)&n,8);
            f.write((char*)bits.data(),bits.size()*8);
            std::cout<<fn<<" targets="<<T.size()<<"\n";
        }
        if(depth==21){
            auto T=targets(S[K],mod);
            std::ofstream f("k9_21.vec",std::ios::binary);
            u64 n=T.size();
            f.write((char*)&mod,8); f.write((char*)&n,8);
            f.write((char*)T.data(),T.size()*8);
            std::cout<<"k9_21.vec targets="<<T.size()<<"\n";
        }
    }
}
