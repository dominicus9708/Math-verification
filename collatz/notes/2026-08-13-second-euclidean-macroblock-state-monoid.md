# Second Euclidean macroblock and the survival-state multiplicity monoid

Date: 2026-08-13

Status: **exact finite-state renormalization theorem at the first two Euclidean levels**. It identifies the correct state carried by a larger Christoffel/Sturmian macroblock and exhibits a new three-way orientation fiber at the second level. This is a structural reduction, not a proof of Collatz.

## 1. Relative-height state of a block

Fix a deterministic mechanical bit block `u`. For an actual bit block `v` of the same time length, let

\[
x_i=v_i-u_i\in\{-1,0,1\}.
\]

Define the total relative-height change

\[
\boxed{
\Sigma(v|u):=\sum_i x_i
}
\]

and the internal minimum prefix displacement

\[
\boxed{
M(v|u):=
\min\left(0,x_0,x_0+x_1,\ldots,\sum_i x_i\right).
}
\]

If the incoming Beatty slack is `h>=0`, the actual block is coefficient-surviving throughout the block iff

\[
\boxed{h+M(v|u)\ge0.}
\]

Its outgoing slack is

\[
\boxed{h+\Sigma(v|u).}
\]

Thus all internal parity details relevant to survival and continuation collapse to the pair

\[
\boxed{(\Sigma,M).}
\]

plus the number of actual subwords realizing that pair.

## 2. Exact concatenation law

Let blocks `U,V` carry states

\[
(\Sigma_U,M_U),
\qquad
(\Sigma_V,M_V).
\]

For their concatenation,

\[
\boxed{
\Sigma_{UV}=\Sigma_U+\Sigma_V,
}
\]

and the minimum either occurs inside `U` or inside `V` after the total displacement of `U`:

\[
\boxed{
M_{UV}
=
\min(M_U,\Sigma_U+M_V).
}
\]

Therefore

\[
\boxed{
(\Sigma_U,M_U)\star(\Sigma_V,M_V)
=
(\Sigma_U+\Sigma_V,
\min(M_U,\Sigma_U+M_V)).
}
\]

This operation is associative because it is induced by ordinary concatenation. Multiplicities of equal states add. Hence Christoffel return words may be renormalized in the finite state-multiplicity semiring

\[
\boxed{(\Sigma,M,\text{multiplicity}).}
\]

## 3. First Euclidean block states

The first renormalization has

\[
A=01,
\qquad
B=1.
\]

For `A`, direct enumeration gives

\[
\begin{array}{c|c|c}
\text{actual}&(\Sigma,M)&\text{multiplicity contribution}\\
\hline
00&(-1,-1)&1\\
01&(0,0)&1\\
10&(0,0)&1\\
11&(1,0)&1
\end{array}
\]

so the state distribution is

\[
\boxed{
A:\quad
(-1,-1):1,
\quad
(0,0):2,
\quad
(1,0):1.
}
\]

The multiplicity-two neutral state is exactly the deterministic plateau-pair `01/10` cube coordinate.

For `B=1`,

\[
\boxed{
B:\quad
(-1,-1):1,
\quad
(0,0):1.
}
\]

## 4. Second Euclidean deterministic macroblock

The deterministic `A/B` word has slope

\[
\gamma=\log_2(3/2)>1/2.
\]

Its `B` symbols are isolated. Pair each `B` with the following `A`. The basic second-level composite is therefore

\[
\boxed{BA.}
\]

In original time bits the mechanical macroblock is

\[
\boxed{BA=1\,01=101.}
\]

It contains three time positions and two mechanical ones.

## 5. Exact state multiplicities of BA

Enumerating all eight actual three-bit patterns and applying the state law gives

\[
\boxed{
\begin{array}{c|c|c}
(\Sigma,M)&\text{multiplicity}&\text{actual patterns}\\
\hline
(-2,-2)&1&000\\
(-1,-1)&3&001,010,100\\
(0,-1)&1&011\\
(0,0)&2&101,110\\
(1,0)&1&111
\end{array}
}
\]

The total multiplicity is

\[
1+3+1+2+1=8,
\]

as required.

## 6. New three-way orientation fiber

The state

\[
\boxed{(-1,-1)}
\]

has multiplicity three:

\[
\boxed{001,\quad010,\quad100.}
\]

If the incoming slack satisfies

\[
\boxed{h\ge1,}
\]

all three patterns are admissible because `h+M>=0`, all end at the same outgoing slack

\[
h-1,
\]

and therefore admit **exactly the same set of suffix continuations**.

Thus the second Euclidean level contains a genuine three-way local orientation fiber, not merely the inherited two-way `01/10` swap.

The three patterns place one actual one in each of the three possible positions of the macroblock. Their canonical start residues are distinct, so this fiber carries a ternary-valued local address coordinate.

## 7. Existing neutral two-way fiber inside BA

The state

\[
(0,0)
\]

has multiplicity two:

\[
101,\quad110.
\]

This is the inherited neutral orientation of the `A=01` subblock with the leading `B` bit fixed to one.

Hence the second level contains simultaneously

- the inherited two-way neutral coordinate;
- a new three-way downward coordinate activated at positive incoming slack.

## 8. Why the state pair is the correct renormalization object

A larger macroblock cannot in general be summarized by total one count alone: a block may dip below the incoming height and later recover.

The pair

\[
(\Sigma,M)
\]

is minimal and sufficient:

- `M` decides admissibility from the incoming slack;
- `Sigma` determines the outgoing slack;
- multiplicity counts how many parity realizations have identical future behavior.

Therefore continued-fraction/Sturmian renormalization can proceed without retaining all `2^n` internal words.

## 9. General recursive construction

For any two deterministic macroblocks with finite state-multiplicity tables, the table of their concatenation is obtained by the associative product

\[
(\Sigma_1,M_1)\star(\Sigma_2,M_2)
=
(\Sigma_1+\Sigma_2,
\min(M_1,\Sigma_1+M_2)),
\]

followed by aggregation of equal states.

Hence the standard continued-fraction recursion for the mechanical/Sturmian return words can be mirrored by an exact recursion of state-multiplicity tables.

This gives a practical route to the third, fourth, ... Euclidean levels while the number of retained states grows polynomially in block length rather than as the number of internal parity words.

## 10. Proof-program consequence

The first plateau cube extracted only one family of Boolean orientations. The second level proves that higher Euclidean scales produce new multiplicity fibers when slack is available.

The new target is to measure, along the continued-fraction hierarchy, how much of the survivor-language entropy is carried by these equal-state multiplicities.

If a sufficiently large fraction is captured, the deep canonical-address condition can be analyzed as a hierarchy of local orientation coordinates rather than as one flat `2^L` residue problem.
