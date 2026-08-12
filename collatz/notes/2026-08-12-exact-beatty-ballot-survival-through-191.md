# Exact Beatty-ballot survival language through depth 191 above the m=44 floor

Date: 2026-08-12

Status: **exact finite-range structural theorem** for the time-expanded accelerated Collatz map above the current recursively verified floor. It identifies the first-descent survivor language through depth 191 with a Beatty/ballot language. It does not prove Collatz and the exact equivalence fails as a uniform consequence at depth 192 because the additive term can become large enough in principle.

## 1. Setup

Use

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For a parity prefix of length `j`, let `q_j` be the number of odd steps. Then

\[
\boxed{T^j(N)=\frac{3^{q_j}N+R_j}{2^j}}
\]

with integer correction numerator `R_j>0` once at least one odd step occurs.

All recursively sufficient m=44 representatives satisfy

\[
\boxed{N\equiv3\pmod4,}
\]

so their first two time-expanded parity symbols are forced to be

\[
\boxed{OO.}
\]

Let

\[
\alpha:=\log_3 2.
\]

## 2. Maximum additive correction at fixed (j,q)

Fix `j>=2` and `q>=2`, with the first two odd steps fixed.

The correction recurrence is

\[
R_{k+1}=\begin{cases}
R_k,&\text{even step},\\
3R_k+2^k,&\text{odd step}.
\end{cases}
\]

Consider two adjacent optional symbols `OE` at positions `k,k+1`. Swapping them to `EO` preserves the total odd count but changes the local correction contribution from `2^k` to `2^(k+1)` after the same preceding value. Hence

\[
\boxed{R(EO)>R(OE).}
\]

Repeated adjacent swaps therefore move every optional odd symbol as far right as possible in the correction-maximizing word.

Thus, after the forced `OO`, the remaining `q-2` odd steps occur in the last `q-2` positions.

Put

\[
m=q-2.
\]

After the forced first two odds one has `R_2=5`. The exact maximum correction is therefore

\[
\boxed{
R_{\max}(j,q)
=5\,3^m
+2^{j-m}(3^m-2^m),
\qquad m=q-2.
}
\]

This is an exact combinatorial maximum over all parity words of length `j` with `q` odd symbols and forced initial `OO`.

## 3. Subcritical coefficient condition

If

\[
q<\lceil j\alpha\rceil,
\]

then

\[
3^q<2^j.
\]

For such a prefix to avoid descending below its own start, one would need

\[
\frac{3^qN+R_j}{2^j}\ge N,
\]

hence

\[
\boxed{
N\le\frac{R_j}{2^j-3^q}
\le
\frac{R_{\max}(j,q)}{2^j-3^q}.
}
\]

Define the worst subcritical threshold

\[
\boxed{
M_j:=
\max_{2\le q<\lceil j\alpha\rceil}
\frac{R_{\max}(j,q)}{2^j-3^q}.
}
\]

## 4. Exact comparison with the current floor

The current recursively extended floor is

\[
\boxed{V_0=4\cdot3^{44}+2.}
\]

Exact integer comparison gives

\[
\boxed{M_j<V_0\qquad(2\le j\le191).}
\]

At the last safe depth,

\[
M_{191}\approx1.4057041605760133\times10^{21},
\]

while

\[
V_0\approx3.9390836087344449\times10^{21}.
\]

At depth 192 the uniform comparison first fails:

\[
M_{192}\approx6.384847853633542\times10^{21}>V_0.
\]

This does **not** exhibit a Collatz survivor or counterexample at depth 192; it only means the simple worst-case additive bound no longer forces every subcritical parity prefix to descend for every `N>=V_0`.

## 5. Exact survivor-language theorem through 191

For every

\[
N\ge V_0,
\qquad N\equiv3\pmod4,
\]

and every

\[
1\le j\le191,
\]

one has the equivalence

\[
\boxed{
T^i(N)\ge N\ \text{for every }1\le i\le j
\iff
q_i\ge\lceil i\log_3 2\rceil\ \text{for every }1\le i\le j.
}
\]

### Proof

If

\[
q_i\ge\lceil i\log_3 2\rceil,
\]

then

\[
3^{q_i}\ge2^i,
\]

and since `R_i>0`,

\[
T^i(N)>N.
\]

Conversely, if for some `i<=191`

\[
q_i<\lceil i\log_3 2\rceil,
\]

then Section 4 gives

\[
N>\frac{R_i}{2^i-3^{q_i}},
\]

so

\[
T^i(N)<N.
\]

Hence the first-descent survivor language through depth 191 is exactly the prefix-ballot language above the irrational Beatty boundary

\[
\boxed{q_i\ge\lceil i\log_3 2\rceil.}
\]

## 6. Exact language counts

Because `N=3 mod4` forces the first two odd symbols, the number `C_B` of survivor parity words of length `B` is obtained by a tiny dynamic program over the current odd count rather than by enumerating `2^B` words.

Representative values are

\[
\begin{array}{c|r|c}
B&C_B&C_B/2^{B-2}\\\hline
28&3,524,586&5.2520424127578735\times10^{-2}\\
50&3,734,259,929,440&1.3266756331518081\times10^{-2}\\
100&302,560,669,500,543,257,546,172,187&9.547131345058957\times10^{-4}\\
150&36,669,896,893,826,317,415,292,528,305,119,465,918,904&1.027709404085364\times10^{-4}\\
191&14,603,890,878,430,725,479,972,220,655,907,544,270,840,991,721,772,560&1.8612272343591195\times10^{-5}
\end{array}
\]

Thus by depth 191 only about

\[
\boxed{1.8612\times10^{-5}}
\]

of all parity cylinders compatible with the forced initial `OO` satisfy the exact no-descent condition.

## 7. Explanation of the observed Beatty plateaus

Let

\[
k_B=\lceil B\log_3 2\rceil.
\]

When `k_B=k_(B-1)`, extending a surviving ballot prefix by one additional parity bit does not introduce a new odd-count threshold at the final level. In the exact finite counts this produces the observed dyadic plateaus, for example

\[
p_{18}=p_{19},\quad
p_{21}=p_{22},\quad
p_{24}=p_{25},\quad
p_{27}=p_{28}.
\]

Hence the class-survivor staircase is controlled by the Beatty sequence of `log_3 2`, not by an irregular computational accident.

## 8. Strategic consequence

This theorem removes the need to enumerate dyadic survivor residues individually through depth 191. The dangerous binary language is described exactly by one prefix inequality:

\[
\boxed{q_i\ge\lceil i\log_3 2\rceil.}
\]

The unresolved cross-base problem is now sharper:

> How many ternary Cantor-core representatives can realize a binary parity prefix lying in this exact Beatty-ballot language as the binary resolution grows?

A pure binary entropy count is insufficient by itself; the terminal step still requires the ternary address and/or the `3`-adic predecessor channel. But the binary channel is now a theorem-level symbolic language rather than a finite residue table.
