# Christoffel square-prefix barrier and eventual finiteness

Date: 2026-08-11

Status: **exact formation barrier + effective asymptotic exclusion of the primitive exact-Christoffel supercritical renewal branch**. The external inputs are the classical standard-Sturmian/Christoffel continued-fraction recursion, the Fernández–Ibáñez Christoffel extremal bound, and an explicit Matveev/Baker lower bound for the nonzero linear form `A log 2 - H log 3`. The result reduces this exact equality branch to a finite initial audit; no numerical cutoff is instantiated here.

## 1. Notation

Put

\[
\gamma:=\log_2 3,
\qquad
\beta:=\gamma^{-1}.
\]

Let `H_n/A_n` be the convergents of `beta`, and let `W_n` denote the ceiling/minimum-rotation Christoffel representative with length `A_n` and `H_n` ones.

In the convention used here, the standard-word recursion is

\[
\boxed{
W_n=
\begin{cases}
W_{n-1}^{a_n}W_{n-2},&n\text{ even},\\[1mm]
W_{n-2}W_{n-1}^{a_n},&n\text{ odd},
\end{cases}
}
\]

where `a_n` is the corresponding continued-fraction partial quotient.

The even indices are the upper approximants in `A/H`, hence the aggregate-supercritical Christoffel words:

\[
\boxed{
\frac{A_n}{H_n}>\gamma.
}
\]

## 2. Long square prefix in every non-base supercritical standard word

Let `n` be even and beyond the base cases.

If

\[
a_n\ge2,
\]

then the recursion gives immediately

\[
\boxed{W_n\text{ begins with }W_{n-1}^2.}
\]

If

\[
a_n=1,
\]

then

\[
W_n=W_{n-1}W_{n-2}.
\]

Since `n-1` is odd,

\[
W_{n-1}=W_{n-3}W_{n-2}^{a_{n-1}},
\]

and since `n-2` is even,

\[
W_{n-2}=W_{n-3}^{a_{n-2}}W_{n-4},
\]

so `W_{n-2}` begins with `W_{n-3}`. Hence

\[
\boxed{W_n\text{ begins with }W_{n-3}^2.}
\]

Therefore every sufficiently indexed aggregate-supercritical standard Christoffel word has a prefix

\[
\boxed{u^2}
\]

where `u` is a prior convergent standard word at index distance at most `3`.

For even `n`, the selected `u` lies on the opposite side of the critical slope, so its affine coefficient is greater than `1` but tends to `1`.

## 3. Square-prefix formation barrier

Let a finite exact parity word `u` have accelerated length `L`, odd count `K`, and exact endpoint-odd formation residue

\[
\rho_u\in\{1,3,5,\ldots,2^{L+1}-1\}.
\]

Let its affine map be

\[
G(x)=ax+b,
\qquad
 a=\frac{3^K}{2^L},
\qquad b>0.
\]

Assume

\[
\boxed{1<a<\frac32,}
\]

and

\[
\boxed{0<b<2^L.}
\]

Suppose the least residue representative `rho_u` also realizes the doubled word `u^2`. Then after one copy of `u`, the state must lie in the same exact endpoint-odd formation class modulo `2^{L+1}`:

\[
G(\rho_u)-\rho_u\equiv0\pmod{2^{L+1}}.
\]

But

\[
G(\rho_u)-\rho_u=(a-1)\rho_u+b>0.
\]

For the convergent words used below we have the sharper bound `a<sqrt(2)`, so

\[
\begin{aligned}
0<G(\rho_u)-\rho_u
&<(\sqrt2-1)2^{L+1}+2^L\\
&<2^{L+1}.
\end{aligned}
\]

There is no positive nonzero multiple of `2^{L+1}` in this interval. Hence the least representative cannot realize `u^2`, unless the gap is exactly zero, which would be an exact positive periodic return.

In the aperiodic branch the periodic alternative is excluded. Therefore

\[
\boxed{
\rho(u^2)>2^{L+1}.
}
\]

### Why the two coefficient bounds hold for convergent words

For a convergent `L/K` of `gamma=log_2 3`,

\[
\left|\gamma-\frac LK\right|<\frac1{K^2}.
\]

Thus for `K>=2`,

\[
|K\gamma-L|<\frac1K\le\frac12.
\]

On the lower-`L/K` side,

\[
1<a=2^{K\gamma-L}<\sqrt2<\frac32.
\]

For the additive term, moving odd steps to later positions maximizes the positive correction, giving

\[
0<b\le\left(\frac32\right)^K-1.
\]

Since the convergent lengths satisfy `L/K` near `gamma>log_2(3/2)`, for all relevant non-base words

\[
\boxed{b<2^L.}
\]

## 4. Formation floor of a supercritical Christoffel word

Let `W_n` be a non-base supercritical Christoffel word, and let `u^2` be the square prefix from Section 2. If `L` is the length of `u`, then exact prefix formation gives

\[
\boxed{
\rho(W_n)\ge\rho(u^2)>2^{L+1}.
}
\]

Thus the integer formation floor grows at least exponentially in the length of a prior convergent word.

## 5. Polynomial upper bound on the rational Christoffel shadow

Let the current supercritical word have length `A=A_n`, odd count `H=H_n`, and rational shadow minimum `C_n`.

The Fernández–Ibáñez extremal inequality gives

\[
\boxed{
C_n\le\frac1{2^{A/H}-3}.
}
\]

Put

\[
\varepsilon:=\frac AH-\gamma>0.
\]

For the fixed algebraic numbers `2` and `3`, an explicit Matveev/Baker lower bound for the nonzero linear form

\[
A\log2-H\log3
\]

implies effective constants `c>0` and `mu>0` such that

\[
\boxed{
\varepsilon\ge cH^{-\mu}.
}
\]

Since

\[
2^\varepsilon-1\ge(\ln2)\varepsilon,
\]

we obtain

\[
\boxed{
C_n\le C_0 H^\mu
}
\]

for an effective constant `C_0`.

Thus the rational shadow minimum grows at most polynomially in the current convergent denominator.

## 6. Nearby convergent denominators are polynomially related

For consecutive convergents,

\[
\left|\gamma-\frac{A_k}{H_k}\right|
<\frac1{H_kH_{k+1}}.
\]

Combining this with the same effective lower bound

\[
\left|\gamma-\frac{A_k}{H_k}\right|
\ge cH_k^{-\mu}
\]

gives

\[
\boxed{
H_{k+1}<c^{-1}H_k^{\mu-1}.
}
\]

The square-prefix word `u` lies at index distance at most `3` from `W_n`; iterating the preceding polynomial relation a fixed number of times shows that the current `H_n` is bounded by a fixed polynomial in the odd count of `u`.

Since the length `L` of `u` is comparable to its odd count, `C_n` is therefore polynomially bounded in `L`.

## 7. Exponential formation floor beats polynomial shadow

Section 4 gives

\[
\rho(W_n)>2^{L+1},
\]

while Sections 5--6 give

\[
C_n\le P(L)
\]

for an effective fixed polynomial `P`.

Hence there exists an effective index `n_0` such that for every supercritical Christoffel convergent word with `n>=n_0`,

\[
\boxed{
\rho(W_n)>C_n.
}
\]

But a floor-increasing aggregate-supercritical renewal start must lie strictly below its positive rational shadow minimum:

\[
N<C_n.
\]

Therefore no such integer renewal start exists for `n>=n_0`.

We conclude

\[
\boxed{
\text{primitive exact-Christoffel supercritical renewal words are possible only for finitely many initial convergents.}
}
\]

The cutoff is effective in principle because Matveev's bound is explicit, although it may be extremely large and is not instantiated in this note.

## 8. Complete role of the exact-Christoffel branch

The earlier renewal power-free theorem already excludes every nonprimitive Christoffel equality word, including nontrivial continued-fraction multiple layers.

The present theorem excludes all sufficiently large primitive Christoffel convergent words.

Therefore the exact Christoffel equality sector is reduced from an infinite hard core to a finite initial audit:

\[
\boxed{
\text{exact Christoffel equality branch}
=\text{finite effective residue-window audit}.
}
\]

This does **not** eliminate the full continued-fraction-resonant sector. Primitive non-Christoffel words with the same aggregate exponent ratio remain and must be controlled by their strict Christoffel correction defect.

## 9. Next target

The remaining economical supercritical problem is a near-Christoffel defect problem.

For a word `w` with the same `(A,H)` as the Christoffel extremizer, define

\[
\mathcal E(w):=C_{\min}^{\rm chr}-C_{\min}(w)>0.
\]

The next target is to combine an explicit lower bound for `mathcal E(w)` in terms of the number/location of required transpositions with the renewal shadow condition `C>N'` and the exact gap channel. The desired conclusion is that a sufficiently large renewal floor forces `mathcal E(w)=0`, sending the word back into the now-finite exact-Christoffel branch.
