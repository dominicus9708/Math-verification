import cmath
import math
from plateau_pair_cube_check import b, boundary_words, residue

def plateau_starts(L):
    return [j for j in range(L-1) if b(j+1) == b(j)]

def mixed_data(w, P):
    pref=[0]
    for x in w:
        pref.append(pref[-1]+x)
    return [(j,pref[j]+1) for j in P if w[j]+w[j+1]==1]

def direct_fourier(W,k):
    L=len(W[0]); mod=1<<(L+1); z=0j
    for w in W:
        r=residue(w+(1,))
        z += cmath.exp(-2j*math.pi*k*r/mod)
    return abs(z)/len(W)

def cube_bound(W,P,k):
    L=len(W[0]); total=0.0; cache={}
    for w in W:
        prod=1.0
        for j,ell in mixed_data(w,P):
            key=(j,ell,k)
            if key not in cache:
                e=L+1-j; mod=1<<e; a=pow(3,-ell,mod)
                cache[key]=abs(math.cos(math.pi*((k*a)%mod)/mod))
            prod*=cache[key]
        total+=prod
    return total/len(W)

def check(L=20):
    W=boundary_words(L); P=plateau_starts(L); S=set(W)
    assert all(P[i+1]-P[i]>=2 for i in range(len(P)-1))
    mod=1<<(L+1)
    for w in W:
        pref=[0]
        for x in w: pref.append(pref[-1]+x)
        ww=list(w)
        for j in P:
            if w[j]+w[j+1]!=1: continue
            sw=list(w); sw[j],sw[j+1]=sw[j+1],sw[j]; sw=tuple(sw)
            assert sw in S
            ell=pref[j]+1
            old=j if w[j] else j+1; new=j if sw[j] else j+1
            expected=(-((1<<new)-(1<<old))*pow(3,-ell,mod))%mod
            assert (residue(sw+(1,))-residue(w+(1,)))%mod==expected
            ww[j],ww[j+1]=ww[j+1],ww[j]
        assert tuple(ww) in S
    for k in (1,3,5,7,15,31):
        d=direct_fourier(W,k); c=cube_bound(W,P,k)
        assert d <= c + 1e-10
        print(k,d,c)
    print('beatty plateau-pair cube audit: PASS')

if __name__=='__main__':
    check()
