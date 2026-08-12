# q-sensitive affine correction bound and Christoffel first-crossing maximizer

Date: 2026-08-12

Status: **exact affine/combinatorial theorem**. The additive Collatz correction has a sharp upper bound at fixed time length and odd count. Under the prefix coefficient-survival constraint, the correction at a first coefficient crossing is maximized uniquely by the delayed mechanical/Christoffel boundary word. This recovers the continued-fraction resonance mechanism from a direct prefix-extremal argument. This does not prove Collatz.

## 1. Affine correction at fixed odd positions

For a length-`k` parity word with `q` odd steps at zero-based positions

\[
0\le j_1<j_2<\cdots<j_q\le k-1,
\]

the accelerated Collatz iterate has the exact form

\[
T^k(n)=\frac{3^q n+R}{2^k},
\]

with

\[
\boxed{
R=\sum_{t=1}^q2^{j_t}3^{q-t}.
}
\]

## 2. Sharp fixed-(k,q) bound

For fixed `k,q`, every summand is strictly increasing in its position `j_t`. Hence the correction is maximized by placing all `q` odd steps as late as the ordering permits:

\[
j_t=k-q+t-1.
\]

Therefore

\[
\boxed{
R\le R_{\max}(k,q)
:=2^{k-q}(3^q-2^q).
}
\]

Equality holds for the parity word

\[
0^{k-q}1^q.
\]

This refines the all-word bound `R<=3^k-2^k` by retaining the actual odd count.

## 3. Uniform additive-free consequence

If

\[
3^q<2^k,
\]

then actual descent below the start is equivalent to

\[
R<(2^k-3^q)n.
\]

The fixed-(k,q) bound gives the sufficient condition

\[
\boxed{
n>
\frac{2^{k-q}(3^q-2^q)}{2^k-3^q}.
}
\]

The right side is strictly increasing in `q` throughout the coefficient-contracting range, because it can be written

\[
\frac{(3/2)^q-1}{1-3^q/2^k}.
\]

Thus the worst contracting odd count is

\[
q=\lfloor k\log_3 2\rfloor.
\]

For the current `m=44` lower start

\[
N_0=4\cdot3^{44}+3,
\]

exact integer arithmetic proves the inequality for every `1<=k<=191`.

At the last successful point,

\[
(k,q)=(191,120),
\]

and

\[
N_0(2^{191}-3^{120})-R_{\max}(191,120)
\]

is the positive integer

\[
1041369856146482344824851097374905325771796552034884751798218495857498300854169.
\]

At

\[
(k,q)=(192,121),
\]

the same unrestricted fixed-`q` envelope becomes too large, with difference

\[
-9238904709670659611822865732323116353266848722183741892777246534052770873930037.
\]

Hence the unrestricted `q`-sensitive theorem alone extends the earlier additive-free window from 44 to exactly 191 steps before this particular universal envelope ceases to certify it.

An independent Wolfram integer evaluation reproduces both signs and verifies all `k<=191`.

## 4. Prefix coefficient barrier

Now impose the actual condition relevant to a **first** coefficient crossing.

Put

\[
\beta:=\log_3 2=1/\log_2 3,
\qquad
a_j:=\lceil j\beta\rceil.
\]

If the multiplicative coefficient survives through all prefixes before time `k`, then

\[
q_j\ge a_j
\qquad(1\le j<k).
\]

A first crossing at time `k` is possible only when the Beatty boundary rises:

\[
a_k=a_{k-1}+1,
\]

and then necessarily

\[
\boxed{
q_k=q_{k-1}=a_k-1.
}
\]

The last step is even.

Write

\[
H:=a_k-1.
\]

The first-crossing time is then

\[
\boxed{
k=\lceil H\log_2 3\rceil.}
\]

## 5. Latest admissible odd positions

Let `j_t` be the zero-based position of the `t`-th odd step, `1<=t<=H`.

To satisfy

\[
q_n\ge\lceil n\beta\rceil
\]

at every prefix, the `t`-th odd step must have appeared no later than the first time the boundary reaches height `t`.

That time is

\[
\lfloor(t-1)/\beta\rfloor+1,
\]

so

\[
\boxed{
j_t\le\lfloor(t-1)\log_2 3\rfloor.}
\]

Since the correction is increasing in each `j_t`, the largest prefix-admissible correction occurs when equality holds for every `t`.

Thus the unique delayed maximizer has odd positions

\[
\boxed{
j_t^{\rm chr}=\lfloor(t-1)\log_2 3\rfloor.}
\]

This is exactly the lower mechanical/Christoffel placement underlying the existing R1 reference word.

## 6. Christoffel correction maximum

Therefore every prefix-surviving first-crossing word with odd count `H` satisfies

\[
\boxed{
R\le R_{\rm chr}(H)
:=\sum_{t=1}^{H}
2^{\lfloor(t-1)\log_2 3\rfloor}3^{H-t}.
}
\]

After normalization by `3^H`,

\[
\boxed{
\frac{R_{\rm chr}(H)}{3^H}
=\frac13\sum_{r=0}^{H-1}2^{-\{r\log_2 3\}}.
}
\]

Because fractional parts are unchanged by subtracting the integer `r`, this is the same reference correction already denoted

\[
\boxed{c_{\rm chr}.}
\]

Thus the Christoffel correction is not merely a convenient comparison word: it is the exact maximum additive support available to **any** coefficient-surviving first-crossing prefix with the same `(A,H)`.

## 7. Direct resonance criterion

At a first crossing put

\[
A=\lceil H\log_2 3\rceil,
\qquad
Z=2^A-3^H>0.
\]

Then

\[
T^A(N)-N=\frac{R-ZN}{2^A}.
\]

Since `R<=R_chr`, every possible first-crossing word descends below `N` whenever

\[
R_{\rm chr}\le ZN.
\]

Consequently a paradoxical/non-descending first crossing requires

\[
\boxed{
N<\frac{R_{\rm chr}}{Z}
=\frac{c_{\rm chr}}{2^A/3^H-1}.
}
\]

This is precisely why only unusually small linear forms

\[
A\log2-H\log3
\]

can support a large starting value: ordinary first-crossing times are killed automatically by the maximal Christoffel correction bound, while continued-fraction resonances remain.

## 8. Relation to the current R1 program

The existing Worley--Dujella isolation and Denjoy--Koksma machinery may now be read as the arithmetic continuation of this extremal theorem:

1. prefix survival forces the Christoffel envelope;
2. the envelope yields the start bound `N<c_chr/(P-1)`;
3. a large `N` forces `P-1` to be exceptionally small;
4. continued fractions isolate the exceptional resonances;
5. defect/address/minimality arguments then attack those isolated resonances.

Thus the small-time additive-free phenomenon and the enormous current CF resonance are two scales of one and the same extremal structure.