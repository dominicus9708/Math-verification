// MATH-020 helper: exact normalized endpoint range generator for depth 80 or 81.
//
// Usage:
//   g++ -O3 -std=c++17 2026_09_08_depth80_81_normalized_range_generator.cpp -o gen
//   ./gen 80 right > right80.txt
//   ./gen 80 left  > left80.txt
//   ./gen 81 right > right81.txt
//   ./gen 81 left  > left81.txt
//
// Feed those files to 2026_09_08_depth80_81_normalized_range_postaudit.py.

#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;

struct State { u128 y; uint8_t q; uint32_t low; };
struct Desc { uint8_t H, s; uint64_t correction; };
static int qminv[90];
static u128 p3[90];

string dec128(u128 x){
    if(!x) return "0";
    string s;
    while(x){s.push_back(char('0'+x%10));x/=10;}
    reverse(s.begin(),s.end());
    return s;
}

int main(int argc,char**argv){
    if(argc!=3){cerr<<"usage: gen DEPTH(80|81) SIDE(right|left)\n";return 2;}
    int K=stoi(argv[1]);
    bool left=string(argv[2])=="left";
    if(K!=80 && K!=81) return 3;

    p3[0]=1;
    for(int i=1;i<90;i++) p3[i]=p3[i-1]*3;
    for(int k=1;k<90;k++){
        int q=0;u128 p=1,target=((u128)1)<<k;
        while(p<target){p*=3;++q;}
        qminv[k]=q;
    }

    const int tail=K-61;
    const int M=1<<tail;
    const int MASK=M-1;
    const int m=29;
    assert(K-qminv[K]==29);

    vector<Desc> G(M);
    for(int r=0;r<M;r++){
        uint64_t n=r;
        int s=0,H=-100;
        for(int j=1;j<=tail;j++){
            int b=n&1;
            s+=b;
            H=max(H,qminv[61+j]-s);
            n=b?(3*n+1)/2:n/2;
        }
        u128 c=(u128)M*n-p3[s]*(u128)r;
        assert(c<=numeric_limits<uint64_t>::max());
        G[r]={uint8_t(H),uint8_t(s),uint64_t(c)};
    }

    vector<State> v;
    v.reserve(5000000);
    v.push_back({0,0,0});
    for(int k=0;k<61;k++){
        vector<State> nv;
        nv.reserve(k<m?v.size()*2:v.size());
        for(auto st:v){
            int lo=k<m?0:(left?1:0);
            int hi=k<m?1:lo;
            for(int e=lo;e<=hi;e++){
                u128 z=st.y+(e?p3[st.q]:0);
                int b=e^int(st.y&1);
                int q2=st.q+b;
                if(q2<qminv[k+1]) continue;
                u128 y2=b?(3*z+1)/2:z/2;
                uint32_t low=st.low;
                if(k<m&&e) low|=1u<<k;
                nv.push_back({y2,uint8_t(q2),low});
                if(k>=m) break;
            }
        }
        v.swap(nv);
    }

    const uint32_t D=(1u<<29)-1;
    if(left){
        v.erase(remove_if(v.begin(),v.end(),[](const State&s){return s.low==0;}),v.end());
        assert(v.size()==963422);
    }else{
        v.erase(remove_if(v.begin(),v.end(),[&](const State&s){return s.low==D;}),v.end());
        assert(v.size()==964227);
    }

    static u128 mn[339][90],mx[339][90];
    static bool seen[339][90];
    const int a0=left?1024:1025;

    for(auto st:v){
        u128 yp[30];
        for(int s=0;s<=tail;s++) yp[s]=st.y*p3[s];
        int q=st.q;
        uint32_t step=(uint32_t)(p3[q]&MASK);
        uint32_t r=((uint32_t)(st.y&MASK)+(uint64_t)a0*step)&MASK;
        for(int j=0;j<339;j++){
            Desc de=G[r];
            if(q>=de.H){
                int Q=q+de.s;
                u128 Z=yp[de.s]+de.correction;
                if(!seen[j][Q]){seen[j][Q]=true;mn[j][Q]=mx[j][Q]=Z;}
                else{if(Z<mn[j][Q])mn[j][Q]=Z;if(Z>mx[j][Q])mx[j][Q]=Z;}
            }
            r=(r+step)&MASK;
        }
    }

    for(int j=0;j<339;j++) for(int Q=0;Q<90;Q++) if(seen[j][Q])
        cout<<(1025+j)<<" "<<Q<<" "<<dec128(mn[j][Q])<<" "<<dec128(mx[j][Q])<<"\n";
}
