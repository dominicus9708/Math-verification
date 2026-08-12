# Ternary local-window universality inside long-surviving representative sets

Date: 2026-08-12

Status: **exact finite diagnostic limitation certificate**. Long-surviving `A_26` representatives still realise every short ternary selector word at every position. Thus the present survivor condition is not explained by a bounded local forbidden-word grammar on the ternary selectors. The result is finite and does not rule out all possible asymptotic local-language theorems.

## 1. Representative family

Use

\[
A_{26}=\left\{4\left(3^{44}+\sum_{i=0}^{25}a_i3^i\right)+3:\ a_i\in\{0,1\}\right\}.
\]

For a representative `N`, let

\[
\tau_<(N):=\min\{k\ge1:T^k(N)<N\}
\]

for the accelerated Collatz map

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

The exact integer verifier examines all `2^26` selector vectors and records only the masks satisfying `tau_>(N)>B` for several diagnostic cutoffs.

## 2. Exact survivor counts

The certified counts are

\[
\boxed{
\begin{array}{c|r}
B&\#\{N\in A_{26}:\tau_<(N)>B\}\\\hline
100&64,411\\
150&6,864\\
200&803\\
250&123
\end{array}}
\]

These are finite exact counts using integer arithmetic only.

## 3. Local ternary-window test

The selector mask is the ternary `0/1` word

\[
(a_0,a_1,\ldots,a_{25}).
\]

For every surviving mask, every consecutive window

\[
(a_j,\ldots,a_{j+k-1})
\]

is recorded. For a given `(B,k)`, call the survivor family **positionwise k-universal** if, at every position `j`, all `2^k` binary/ternary-selector words occur among the survivors.

The exact certificate gives:

\[
\boxed{
\begin{array}{c|c}
B&\text{positionwise universal through window length}\\\hline
100&11\\
150&9\\
200&6\\
250&4
\end{array}}
\]

Thus, for example, among the 64,411 representatives surviving beyond 100 steps, every one of the `2^11=2048` possible length-11 ternary selector patterns occurs at **every** one of the 16 possible length-11 positions.

Likewise the 6,864 representatives surviving beyond 150 steps still realise all `2^9=512` length-9 patterns at every possible position.

## 4. Consequence for the local-subshift route

A proof mechanism based on a fixed finite list of short forbidden ternary words would need some local pattern to disappear from every sufficiently dangerous representative.

The present exact data show that this does not happen at surprisingly high stopping-depth thresholds and nontrivial window lengths.

In particular, at `B=100` there is no forbidden selector word of length at most 11 at **any** position, and at `B=150` there is no forbidden selector word of length at most 9 at any position.

Therefore the current dangerous set is not naturally described by a small ordinary subshift of finite type on the ternary selectors.

This is consistent with the cross-place formulation: the dynamical condition depends on the global weighted sum

\[
\sum_i a_i3^i\pmod{2^L},
\]

so selector bits that look completely unrestricted in short local windows can still satisfy a strong global dyadic congruence.

## 5. What this does and does not rule out

It does **not** prove that no local-language theorem exists asymptotically. A forbidden word could emerge only at much larger stopping depth or with window length growing with the selector depth.

What it does justify is a strategy choice:

\[
\boxed{
\text{do not replace the cross-base address by a fixed short ternary grammar.}
}
\]

The next proof object should remain the global binary/ternary compatibility count

\[
C_{d,L}(R)
\]

and its exact cross-spectrum, rather than a bounded ternary forbidden-word list.

## 6. Reproducibility

Exact verifier:

`collatz/src/m44_low26_survivor_window_universality.cpp`

Expected output:

- `B=100`: 64,411 survivors, universal through length 11;
- `B=150`: 6,864 survivors, universal through length 9;
- `B=200`: 803 survivors, universal through length 6;
- `B=250`: 123 survivors, universal through length 4.
