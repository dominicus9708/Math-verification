# First global resonance: exact exclusion of prefix-72 displacement count at most 8

Date: 2026-08-26

Status: **exact finite theorem** inside the repaired global binary branch.  It uses the first-resonance start band already proved from the published \(2^{71}\) verification input and the exact coefficient-survival/formation identities.  It does not use the disputed ternary selector, repeated L7/L14 pullback, or a probabilistic assumption.  It does not prove the Collatz conjecture.

## 1. First-resonance setting

The sharp constant-wall/Farey analysis isolates the first possible coefficient crossing of a hypothetical minimal counterexample at

\[
(A_0,q_0)
=(114208327604,72057431991).
\]

Every candidate in this cell satisfies

\[
\boxed{2^{71}<N<\frac43\,2^{71}<2^{72}.}
\]

Hence its first 72 parity symbols determine the ordinary integer \(N\) exactly, not merely modulo a power of two.

Because the full word has its first coefficient crossing only at \(A_0\), its first 72 symbols are coefficient-surviving and therefore dominate the mechanical Beatty prefix in cumulative odd count.

## 2. Prefix-72 ordinal displacement count

Let

\[
0\le a_1<a_2<\cdots
\]

be the actual odd positions and

\[
0\le b_1<b_2<\cdots
\]

the odd positions of the global first-crossing mechanical word.

Coefficient survival gives

\[
a_j\le b_j.
\]

At depth 72 the mechanical prefix contains exactly 46 odd symbols.

Define

\[
\boxed{
D_{72}
:=
\#\{j:a_j<72\text{ and }a_j\ne b_j\}.
}
\]

Odd ordinals beyond the mechanical first 46 can also enter the first 72 positions; each such ordinal automatically contributes to \(D_{72}\) because its mechanical position is at least 72.

Thus \(D_{72}\) measures how many ordinal channels have already departed from the mechanical formation before the ordinary start address is completely exposed.

## 3. Exhaustive exact enumeration

The companion C++ certificate enumerates every strictly increasing position vector satisfying

\[
a_j\le b_j,
\qquad
D_{72}\le8,
\]

with at least the 46 odd positions required by coefficient survival at depth 72.

For every such vector it computes exactly:

1. the correction residue modulo \(2^{72}\);
2. the unique canonical start \(N\in[0,2^{72})\);
3. whether \(N\) lies in the strict first-resonance band
   \[
   2^{71}<N<\frac43\,2^{71};
   \]
4. if it does, the actual shortcut Collatz orbit of that exact natural number until its **actual first coefficient crossing**;
5. whether the crossing endpoint remains at or above \(N\).

No floating point arithmetic and no random sampling are used.

The exact counts by displacement number are

\[
\begin{array}{c|r|r|r}
D_{72}&\text{prefixes}&\text{starts in band}&\text{latest first crossing}\\\hline
0&1&0&-\\
1&26&7&81\\
2&351&40&140\\
3&3275&541&134\\
4&23725&3913&184\\
5&142153&23583&265\\
6&732947&122732&278\\
7&3341257&557068&308\\
8&13733231&2290462&379
\end{array}
\]

Aggregating,

\[
\boxed{17,976,966}
\]

coefficient-surviving prefix patterns are checked, of which

\[
\boxed{2,998,346}
\]

produce an ordinary start in the first-resonance band.

For **every one** of those 2,998,346 starts, its actual first coefficient crossing has endpoint strictly below the start.

The deepest observed first crossing in the complete certified family is only

\[
\boxed{379}.
\]

## 4. Exact consequence

A hypothetical minimal counterexample in the first global resonance cell cannot belong to any of the enumerated prefix classes.

Therefore

\[
\boxed{
D_{72}\ge9.
}
\]

This is now a proof-level finite condition, not a heuristic observation.

Combined with the exact correction-defect theorem,

\[
\frac{E}{3^{q_0}}
>
\frac16\sum_j(1-2^{-s_j}),
\]

one obtains the immediate but numerically weak corollary

\[
\boxed{
\frac{E}{3^{q_0}}>\frac34.
}
\]

The main value of \(D_{72}\ge9\) is structural rather than this constant: a first-resonance candidate cannot be a one- or few-defect perturbation of the mechanical address during the complete ordinary-address exposure.

## 5. DSD logical-chain role

The result gives the first exact finite bridge among all three synchronized descriptors:

\[
\boxed{
\text{bounded formation address}
\to
D_{72}\ge9
\to
\text{nontrivial Beatty excursion/transport}
\to
\text{positive correction defect}.
}
\]

The next theorem should not merely increase the number 8 by brute force.  The desired structural extension is a recurrence or transfer inequality of the form

\[
D_K\text{ small}
\Longrightarrow
\text{coefficient crossing occurs by }F(K,D_K),
\]

or conversely

\[
\text{coefficient survival to a very large depth}
\Longrightarrow
D_K\ge \Phi(K)
\]

for bounded ordinary formation floors.

Such a theorem would convert the finite prefix certificate into a scalable address--defect incompatibility statement.

Certificate:

`collatz/src/global_first_resonance_prefix72_displacement8_certificate.cpp`.
