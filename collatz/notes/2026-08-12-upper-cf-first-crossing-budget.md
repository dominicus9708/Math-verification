# Upper-CF first-crossing correction and formation budget

Date: 2026-08-12

Status: **exact theorem for the primitive upper-convergent renewal branch**. The only external input needed for the asymptotic polynomial corollary is an explicit lower bound for the nonzero linear form `A log 2 - H log 3` (e.g. Matveev).

## 1. Setup

Let a renewal-compatible aggregate-supercritical word have accelerated length `A`, odd count `H`, and

\[
P:=\frac{2^A}{3^H}>1.
\]

Assume `(A,H)` is a primitive upper continued-fraction approximant to `log_2 3` and that the renewal suffix conditions force the full word to be the first coefficient crossing:

\[
2^{A_p}<3^{H_p}
\]

for every proper prefix, while

\[
2^A>3^H.
\]

Let the odd positions be

\[
1=i_1<i_2<\cdots<i_H\le A.
\]

Write the aggregate affine map as

\[
T^A(n)=\frac{3^Hn+R}{2^A},
\]

and define the normalized correction

\[
\boxed{r:=\frac{R}{3^H}.}
\]

For a renewal floor `N` with next floor `N'=N+g`, the endpoint equation is

\[
N+r=P(N+g).
\]

## 2. First-crossing correction bound

The exact correction expansion is

\[
\boxed{
r=\sum_{k=1}^{H}\frac{2^{i_k-1}}{3^k}.}
\]

For `k>=2`, immediately before the `k`th odd bit the proper prefix has length `i_k-1` and contains `k-1` odd bits. First coefficient crossing therefore gives

\[
2^{i_k-1}<3^{k-1}.
\]

Hence

\[
\frac{2^{i_k-1}}{3^k}<\frac13.
\]

For `k=1`, `i_1=1`, so the first term equals `1/3`. Since at least one later term is strict,

\[
\boxed{r<\frac H3.}
\]

This is independent of Christoffel extremality.

## 3. Exact floor-gap budget

From

\[
N+r=P(N+g)
\]

we obtain

\[
\boxed{r=(P-1)N+Pg.}
\]

Combining with `r<H/3`,

\[
\boxed{(P-1)N+Pg<\frac H3.}
\]

Therefore

\[
\boxed{N<\frac{H}{3(P-1)},}
\]

and

\[
\boxed{0<g<\frac{H}{3P}.}
\]

Since every renewal floor is `3 mod 4`,

\[
\boxed{g\in4\mathbb Z_{>0}.}
\]

Thus a necessary condition for this branch is

\[
\boxed{4\le g<\frac{H}{3P}.}
\]

## 4. Exact gap residue modulo `2Z` and `4Z`

Let

\[
Z:=2^A-3^H>0.
\]

Endpoint oddness fixes one exact starting residue class

\[
N\equiv\rho_w\pmod{2^{A+1}}.
\]

For the least representative `rho_w`, define

\[
\boxed{\Gamma_w:=\frac{R-Z\rho_w}{2^A}.}
\]

The numerator is divisible by `2^A` by exact formation.

Any other exact realization has

\[
N=\rho_w+k2^{A+1},
\]

and hence

\[
g=\frac{R-ZN}{2^A}
=\Gamma_w-2kZ.
\]

Therefore

\[
\boxed{g\equiv\Gamma_w\pmod{2Z}.}
\]

Because genuine renewal floors are both `3 mod 4`, we also require

\[
\boxed{g\equiv0\pmod4.}
\]

Since `Z` is odd, the pair of congruences determines one exact class modulo

\[
\boxed{4Z.}
\]

Thus a fixed primitive upper-CF renewal word has candidate gaps in one arithmetic progression modulo `4Z`, intersected with the short interval

\[
\boxed{0<g<\frac{H}{3P}.}
\]

For every sufficiently large such word, `4Z>H/(3P)`, so at most one positive gap candidate remains.

## 5. Polynomial ceiling on the ordinary starting integer

The exact bound

\[
N<\frac{H}{3(P-1)}
\]

becomes polynomial in `H` once one uses a standard explicit lower bound for

\[
A\log2-H\log3\ne0.
\]

Indeed, a Matveev/Baker-type estimate gives effective constants `c>0` and `mu>0` such that

\[
|A\log2-H\log3|\ge cH^{-\mu}.
\]

On the upper side this implies an effective polynomial lower bound for `P-1`, and hence

\[
\boxed{N\le C H^{\mu+1}}
\]

for an effective constant `C`.

Since

\[
2^{A+1}
\]

grows exponentially in `H`, for all sufficiently large upper convergents

\[
\boxed{N<2^{A+1}.}
\]

Therefore any surviving ordinary integer is necessarily the least positive exact formation representative:

\[
\boxed{N=\rho_w.}
\]

Hence the residual branch must satisfy the **polynomial formation-floor ceiling**

\[
\boxed{\rho_w<\frac{H}{3(P-1)}.}
\]

This converts the primitive upper-CF renewal problem into a sharp atomic statement: an exact parity word of exponential modulus `2^{A+1}` must have a least positive representative lying inside an explicit polynomial interval.

## 6. Defect finite-lift consequence

Let `R_chr` be the Christoffel correction numerator at the same `(A,H)` and

\[
E:=R_{chr}-R(w)>0
\]

for a non-Christoffel residual word.

The tri-place formation identity gives

\[
\rho_w-\rho_{chr}
\equiv E(3^H)^{-1}
\pmod{2^{A+1}}.
\]

Equivalently,

\[
\boxed{E\equiv3^H(\rho_w-\rho_{chr})\pmod{2^{A+1}}.}
\]

The real correction budget gives `R(w)/3^H< H/3`; the Christoffel correction is also `O(H)` after normalization. Thus

\[
0<E<O(H3^H).
\]

Because

\[
2^{A+1}=2P3^H,
\]

`E` can occupy only `O(H)` lifts of its fixed residue modulo `2^{A+1}`.

Therefore, once the small ordinary start `rho_w` is fixed, the nonzero Christoffel defect is no longer an unrestricted integer: it belongs to a finite linear-size lift family.

## 7. Current role

This theorem does not exclude the primitive upper-CF branch. It does three things that are useful for the next step:

1. replaces the Christoffel-only real ceiling by a universal first-crossing ceiling for **all** primitive upper-CF renewal words;
2. shows that the next renewal gap lies in one class modulo `4Z` but inside an interval of length `O(H)`;
3. shows that the ordinary integer start is eventually the least dyadic formation representative and is polynomially bounded in `H`.

The remaining infinite problem is therefore an atomic residue problem:

\[
\boxed{
\text{Can a first-crossing upper-CF word have }
\rho_w=\operatorname{poly}(H)
\text{ while its exact modulus is }2^{A+1}\asymp3^H?
}
\]

The tri-place Christoffel defect coordinate and the exact `4Z` gap class are the two additional arithmetic constraints available for attacking this question.
