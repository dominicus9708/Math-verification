# Targeted reverse-code forbidden-prefix tree in the R1 `p=16` hard sector

Date: 2026-08-14

Status: **exact finite cross-place reverse-code certificate through reverse depth 14 + proof-strategy correction**.  This refines the three low-19 dyadic hard residues left in the current `p=16` first-defect channel.  It does not close that channel and does not prove Collatz.

## 1. Hard dyadic sector

After the depth-27 Hensel sieve, the `p=16` first-defect channel collapses modulo `2^19` to exactly

\[
\boxed{r\in\{89,083,\ 220,155,\ 351,227\}.}
\]

For each fixed `r`, combine forward affine prefixes through

\[
2\le B\le18
\]

with positive odd-to-odd reverse codes.

## 2. Reverse-code representation

A reverse exponent code

\[
(a_1,\ldots,a_q),
\qquad a_i\ge1,
\]

has total binary exponent

\[
K=\sum_i a_i
\]

and correction recurrence

\[
C_0=0,
\qquad
\boxed{C_{j+1}=2^{a_{j+1}}C_j+3^j.}
\]

The endpoint residue required by that code is uniquely

\[
\boxed{
z\equiv C_q2^{-K}\pmod{3^q}.}
\]

The code is retained only when every intermediate inverse odd step is integral and admissible.  For fixed `(q,z,K)`, only the largest `C` is needed because it gives the smallest ancestor.

This representation is much smaller than building a separate reverse frontier for all `3^Q` endpoint residues.  In the present hard sector the class-uniform smaller-ancestor slope inequality bounds the useful total exponents by

\[
\boxed{
K_{\max}(q)=
1,3,4,6,7,9,10,12,14,15,17,18,20,22
}
\]

for `q=1,...,14` respectively.  The total valid code table through `q=14` contains only hundreds of thousands of states.

## 3. Exact survivor progression

For every low-ternary selector mask of depth `Q`, compute

\[
N\pmod{3^Q}
\]

and test every forward depth `B<=18` against all indexed reverse codes of depth at most `Q`.

The three dyadic hard residues have **identical survivor sets** at every audited `Q`:

\[
\boxed{
\begin{array}{c|r|r|c}
Q&\text{surviving masks}&\text{excluded masks}&\text{excluded fraction}\\\hline
6&64&0&0\\
8&256&0&0\\
10&984&40&0.0390625\\
11&1960&88&0.04296875\\
12&3896&200&0.048828125\\
13&7776&416&0.05078125\\
14&15440&944&0.0576171875
\end{array}
}
\]

Thus the low-ternary reverse obstruction grows with depth while remaining synchronized across all three dyadic members of the `p=16` hard sector.

## 4. Prefix-minimal forbidden cylinders

Represent a low-selector cylinder by `(k,b)`, meaning

\[
a_0+2a_1+\cdots+2^{k-1}a_{k-1}=b
\]

in binary-mask notation, with all higher selector bits free.

### Through `Q=10`

The exact prefix-minimal cylinders are

\[
\boxed{
(6,14),\quad
(7,6),\quad
(7,8),\quad
(7,35).
}
\]

Their descendant mass in the low-10 cube is

\[
16+8+8+8=40.
\]

This is equivalent to the earlier five low-seven mask description, because the `k=6` cylinder `14` contains both low-seven masks `14` and `78`.

### Through `Q=11`

Two new minimal cylinders appear:

\[
\boxed{(9,148),\quad(9,461).}
\]

Together with the inherited cylinders they remove exactly `88` low-11 masks.

### Through `Q=12`

Three further low-nine cylinders appear:

\[
\boxed{(9,135),\quad(9,254),\quad(9,494).}
\]

The nine inherited/minimal cylinders remove exactly `200` low-12 masks.

### Through `Q=13`

Four new low-eleven cylinders appear:

\[
\boxed{
(11,1143),\quad
(11,1869),\quad
(11,1940),\quad
(11,1961).
}
\]

The complete minimal tree removes `416` low-13 masks.

### Through `Q=14`

The minimal tree has 38 cylinders and removes exactly `944` low-14 masks.  Besides the inherited nodes, new nodes occur at lengths 11 and 12.  The exact list is stored and checked by the companion verifier rather than repeated here.

## 5. Representative exact witnesses

The minimal cylinders have explicit smaller-ancestor reverse codes.  Examples include

\[
\begin{array}{c|c|c|c|l}
(k,b)&B&q_r&K&(a_1,\ldots,a_{q_r})\\\hline
(6,14)&4&9&13&(3,1,1,2,1,2,1,1,1)\\
(7,6)&4&10&15&(3,1,1,2,1,2,2,1,1,1)\\
(7,8)&3&9&14&(2,3,2,1,1,1,2,1,1)\\
(7,35)&3&9&14&(2,1,4,1,2,1,1,1,1)\\
(9,148)&3&11&17&(2,3,2,1,2,1,2,1,1,1,1)\\
(9,461)&3&11&17&(2,1,4,2,1,2,1,1,1,1,1)\\
(9,135)&4&12&18&(3,1,3,2,1,1,1,2,1,1,1,1)
\end{array}
\]

Every witness is checked by exact affine inequality over the full current start interval, including positivity of the reverse ancestor.

## 6. Important correction: pure reverse plateau does not transfer to cross-place birth

For the common-`OO` **pure reverse contraction** analysis, the multiplicative budget

\[
\lfloor q\log_2(3/2)\rfloor
\]

implies that a budget plateau cannot create a new prefix-minimal reverse contraction cylinder.

It is tempting to apply the same conclusion to the present forward+reverse cross-place sieve.  That is invalid.

At `q=13`, the pure multiplicative extra-even budget is unchanged relative to the preceding relevant scale, yet the exact cross-place audit produces four new low-eleven cylinders.

The reason is that the class comparison is not purely multiplicative.  With forward data `(q_f,R_f,B)` and reverse data `(q_r,K,C)`,

\[
\boxed{
2^K(3^{q_f}N+R_f)
-
2^B C
-
2^B3^{q_r}N
<0.
}
\]

The additive terms `2^K R_f` and `2^B C` can make a deeper reverse code class-uniformly smaller even when the simple multiplicative budget has not increased.

Therefore:

\[
\boxed{
\text{Beatty plateau no-birth}
\text{ is a theorem for the aligned pure-reverse model,}
}
\]

but **not** for the forward+reverse cross-place composite.

This distinction prevents an invalid transfer of a true local theorem to the stronger mixed-place sieve.

## 7. Proof-program consequence

The `p=16` branch contains a genuine nested low-ternary forbidden-prefix tree rather than a one-shot percentage filter.  Its key features are

1. exact synchronization across the three hard dyadic residues;
2. persistent inherited cylinders;
3. new cylinder births at growing reverse depth;
4. a compact reverse-code representation requiring only the reachable exponent codes rather than all endpoint residues.

The current finite data do not prove that the forbidden tree eventually covers all ternary prefixes.  The survival fraction through `Q=14` is still about 94.24%.

The useful next target is a **growth/automaton theorem for the surviving low-ternary prefix tree conditioned on the three hard dyadic residues**, or a higher-scale condition that combines this tree with the early-defect dyadic address and the Euclidean gate syndrome.