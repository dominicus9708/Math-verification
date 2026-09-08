// MATH-036 companion: exact small-depth internal-boundary scan for k<=60.
// Enumerates every internal boundary b=1025..1363 and every positive start
// displacement d satisfying the MATH-021 necessary bound d < k/3, written as
// left offset l>=1 and right offset r>=0 with l+r=d.  Both starts must satisfy
// the coefficient-survival prefix gate through depth k.  No joint surviving
// pair exists in this range.

#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std;
using boost::multiprecision::cpp_int;

static const int qpub[62]={0,1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,14,14,15,16,16,17,18,18,19,19,20,21,21,22,23,23,24,24,25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,35,35,36,36,37,38,38,39};

bool survive(cpp_int n,int k,int &q,cpp_int &E){
    q=0;
    for(int j=1;j<=k;++j){
        const bool odd=bit_test(n,0);
        if(odd){n=(3*n+1)/2;++q;}else n/=2;
        if(q<qpub[j]) return false;
    }
    E=n;
    return true;
}

int main(){
    const cpp_int W=cpp_int(1)<<61;
    long long checked=0,joint_survive=0,collisions=0;
    for(int k=1;k<=60;++k){
        const int D=(k-1)/3;
        for(int b=1025;b<=1363;++b){
            const cpp_int B=cpp_int(b)*W;
            for(int d=1;d<=D;++d){
                for(int l=1;l<=d;++l){
                    const int r=d-l;
                    int qL,qR; cpp_int EL,ER;
                    ++checked;
                    if(!survive(B-l,k,qL,EL) || !survive(B+r,k,qR,ER)) continue;
                    ++joint_survive;
                    if(qL==qR && EL==ER) ++collisions;
                }
            }
        }
    }
    assert(checked==1'352'610LL);
    assert(joint_survive==0);
    assert(collisions==0);
    cout<<"PASS checked="<<checked
        <<" joint_survive="<<joint_survive
        <<" collisions="<<collisions<<"\n";
    cout<<"COLLATZ STATUS=OPEN\n";
}
