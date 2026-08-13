# Binary alternate-predecessor integerization sieve

Date: 2026-08-13

Status: **exact algebraic cylinder-elimination theorem + exact finite depth-20 diagnostic**.  This is a recursively-sufficient / minimal-counterexample filter on parity cylinders.  It does not prove the Collatz conjecture.

## 1. Same-length, same-odd-count alternate prefix

Use the accelerated map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Let `w` and `u` be two binary parity words of the same time length `L` and the same odd count `q`.  Write their affine maps as

\[
T_w^L(N)=\frac{3^qN+R_w}{2^L},
\qquad
T_u^L(X)=\frac{3^qX+R_u}{2^L}.
\]

Assume

\[
C:=R_u-R_w>0.
\]

Define the rational 2-adic alternate start

\[
\boxed{N^\sharp=N-\frac{C}{3^q}.}
\]

Then

\[
3^qN^\sharp+R_u=3^qN+R_w,
\]

hence

\[
\boxed{T_u^L(N^\sharp)=T_w^L(N).}
\]

Thus `u` from `N^sharp` and `w` from `N` merge at the same ordinary endpoint after `L` steps.

## 2. Exact denominator-clearing depth

Let

\[
s:=v_3(C),
\qquad
d:=q-s.
\]

First assume

\[
0<s<q.
\]

The reduced denominator of `N^sharp` is exactly

\[
3^d.
\]

Let `t_d` be the time immediately after the `d`-th odd symbol of the alternate word `u`.  Let `R_{u,d}` be the affine correction of the prefix `u[0:t_d]`, which has exactly `d` odd symbols.

At that time

\[
X_d
=
\frac{3^dN^\sharp+R_{u,d}}{2^{t_d}}
=
\frac{3^dN+R_{u,d}-C/3^s}{2^{t_d}}.
\]

Before the `d`-th odd symbol, the remaining factor `3^{d-q_t}` in the denominator is nontrivial; multiplication or division by powers of two cannot cancel it.  At the `d`-th odd symbol it is cleared exactly.  Because the parity word `u` is the canonical 2-adic word of `N^sharp`, the resulting rational is 2-adically integral; after the odd denominator has disappeared it is therefore an ordinary integer.

Hence the first ordinary-integer state on the alternate branch is

\[
\boxed{
m
=
\frac{3^dN+R_{u,d}-C/3^s}{2^{t_d}}.
}
\]

If `s>=q`, then `3^q | C` and the alternate start itself is already an ordinary integer:

\[
\boxed{N^\sharp=N-C/3^q.}
\]

This is the depth-zero special case.

## 3. Contracting integerization criterion

For `0<s<q`, subtract `N` from the exact integerization formula:

\[
m-N
=
\frac{
(3^d-2^{t_d})N
+R_{u,d}-C/3^s
}{2^{t_d}}.
\]

If

\[
\boxed{2^{t_d}>3^d,}
\]

the coefficient of `N` is strictly negative.  Therefore every start satisfying

\[
\boxed{
N>
\frac{R_{u,d}-C/3^s}{2^{t_d}-3^d}
}
\]

has

\[
\boxed{m<N.}
\]

If additionally `N^sharp>0`, every intermediate rational state on the alternate word is positive, so the integerized state satisfies `m>0`.  From `m` onward the remaining suffix of `u` is an ordinary Collatz trajectory and reaches the same endpoint as the original word `w`.

Consequently, above the displayed threshold, the entire parity cylinder `w` is recursively safe: it cannot be the prefix of a minimal positive counterexample.

The condition `s>=q` is even simpler.  If

\[
0<C/3^q<N,
\]
then `N^sharp` itself is a smaller positive integer that reaches the same endpoint, so the cylinder is excluded immediately.

## 4. Prefix-monotonicity

This elimination is stable under every common future suffix.

Let `v` be any suffix with `r` odd symbols.  Concatenation gives

\[
R_{uv}-R_{wv}=3^r(R_u-R_w)=3^rC.
\]

The total odd count becomes `q+r`, so the rational displacement is unchanged:

\[
\boxed{
\frac{R_{uv}-R_{wv}}{3^{q+r}}
=
\frac{C}{3^q}.
}
\]

The denominator-clearing event already occurred inside `u`, before the common suffix begins.  Therefore any extension of an excluded cylinder remains excluded.

Thus the forbidden set is a genuine prefix-closed union of infinite binary cylinders rather than a collection of isolated finite computations.

## 5. Relation to the earlier reverse-preimage sieve

The common-`OO` ternary reverse sieve searched for a smaller integer that merges with a candidate orbit at a common descendant.  The present theorem is the parity-prefix dual of the same principle:

1. choose an alternate parity prefix with the same affine coefficient `3^q/2^L`;
2. use the correction congruence `v_3(R_u-R_w)>0` to make the rational alternate predecessor become ordinary before the merge endpoint;
3. require that the denominator-clearing prefix be contracting strongly enough that the new integer lies below the original start.

The 3-adic valuation is therefore not merely a residue label.  It is exactly the number of odd multiplications removed from the denominator before an ordinary smaller predecessor can appear.

## 6. Exact finite diagnostic in the current large-start regime

For the current `m=44` minimal-counterexample search use the already certified lower start

\[
\boxed{
N_{\min}=4(3^{44}+3^{32})+3.
}
\]

The verifier considers every binary parity word of length `L` that

1. begins with the mandatory `OO` prefix;
2. satisfies the coefficient-survival barrier at every prefix:
   \[
   3^{q_t}\ge2^t;
   \]
3. is tested against every same-length word with the same total odd count as a possible alternate prefix.

All arithmetic is exact.  A cylinder is removed only when the integerization inequality is certified for every `N>=N_min` in that cylinder.

The resulting counts are

\[
\boxed{
\begin{array}{c|r|r|r}
L&\text{coefficient-surviving}&\text{removed}&\text{retained}\\\hline
3&2&0&2\\
4&3&0&3\\
5&4&0&4\\
6&8&1&7\\
7&13&2&11\\
8&19&3&16\\
9&38&11&27\\
10&64&18&46\\
11&128&48&80\\
12&226&82&144\\
13&367&125&242\\
14&734&298&436\\
15&1295&493&802\\
16&2114&751&1363\\
17&4228&1729&2499\\
18&7495&2895&4600\\
19&14990&6527&8463\\
20&27328&11458&15870
\end{array}
}
\]

At depth 20 the exact removed fraction is

\[
\boxed{
\frac{11458}{27328}
=0.419276932084\ldots
}
\]

or about

\[
\boxed{41.9277\%.}
\]

Because of prefix-monotonicity, these are cylinder eliminations, not a sample of individual integer trajectories.

## 7. Interpretation

This finite percentage should not be extrapolated as an asymptotic proof.  The important structural gain is the new exact interface

\[
\boxed{
\text{binary correction difference}
\xrightarrow{v_3}
\text{denominator-clearing time}
\xrightarrow{2^{t_d}>3^d}
\text{smaller ordinary predecessor}.
}
\]

It joins the binary parity-prefix language, the 3-adic correction channel, and minimal-counterexample recursion in one theorem.

The result also explains why shallow 2-adic and 3-adic density filters looked almost independent: the useful interaction is not their marginal densities.  It is the valuation of the **difference of two corrections with the same coefficient**.

## 8. Next target

The next useful question is not to push the flat depth from 20 to a much larger number.  The Euclidean macroblock state-multiplicity construction should be augmented by a correction-congruence coordinate:

\[
\boxed{
(\Sigma,M,\;R\bmod3^j,\;\text{multiplicity}).
}
\]

Equal survival states can then be tested for alternate-predecessor collisions at increasing 3-adic depths without enumerating all internal parity words.

A multiscale theorem showing that a positive fraction of the critical survivor language acquires an integerizing correction collision at each Euclidean scale would convert the finite cylinder sieve into a genuine hierarchical contraction mechanism.
