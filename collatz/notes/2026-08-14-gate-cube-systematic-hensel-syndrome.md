# Systematic Hensel syndrome of the gate-wide orientation cube

Date: 2026-08-14

Status: **exact code decomposition + exact finite no-full-lift certificate for the first-return gate cubes**. This note refines the gate-wide Hensel cube by separating independently selectable low ternary digits from the dependent high syndrome. It also audits all integer predecessor credits `1 <= delta <= 397` arising in the previously identified length-19 credit SCC. The result applies to the explicit cube section only, not to the full same-state gate fibre, and does not prove Collatz.

## 1. Generic cube parameters

Use an explicit same-state gate cube of the form

\[
\boxed{1^F(01/10)^J0.}
\]

Every vertex has actual odd count

\[
\boxed{q=F+J.}
\]

For a difference vector

\[
\epsilon=(\epsilon_0,\ldots,\epsilon_{J-1})
\in\{-1,0,1\}^J,
\]

the exact correction difference is

\[
D(\epsilon)
=
\sum_{j=0}^{J-1}
\epsilon_j3^{J-1-j}2^{F+2j}.
\]

Factor out the common dyadic unit:

\[
\boxed{
Z(\epsilon)
:=2^{-F}D(\epsilon)
=
\sum_{j=0}^{J-1}
\epsilon_j3^{J-1-j}4^j.
}
\]

## 2. Low Hensel digits are systematic coordinates

Modulo `3^J`, the map

\[
\epsilon\mapsto Z(\epsilon)\pmod{3^J}
\]

is a bijection from `{-1,0,1}^J` to `Z/3^J Z`.

Therefore every low-Hensel target

\[
t\pmod{3^J}
\]

selects a **unique** cube vector

\[
\boxed{\epsilon(t).}
\]

The vector can be recovered digit by digit from the lowest ternary place: at each stage the coefficient `4^j` is a unit modulo three, so one uniquely chooses `epsilon_j in {-1,0,1}` to cancel the current residue, subtracts that coordinate, and divides by three.

Thus the first `J` ternary digits are the independent or **systematic** coordinates of the cube.

## 3. High Hensel syndrome

The full correction congruence lives modulo

\[
3^q=3^{F+J}.
\]

After the unique vector `epsilon(t)` has been fixed by the low `J` digits, its remaining high ternary digits are no longer adjustable.

Write

\[
Z(\epsilon(t))
=t+3^J S(t)
\pmod{3^{F+J}},
\]

with

\[
\boxed{S(t)\in\mathbb Z/3^F\mathbb Z.}
\]

Then

\[
\boxed{
S:\mathbb Z/3^J\mathbb Z
\longrightarrow
\mathbb Z/3^F\mathbb Z
}
\]

is the **high-Hensel syndrome map** of the explicit cube.

The correct interpretation is therefore

\[
\boxed{
\text{low }J\text{ Hensel trits freely pivot}
\quad\Longrightarrow\quad
\text{high }F\text{ trits are a deterministic syndrome.}
}
\]

The high digits are not frozen or unaffected by the low choices; they are dependent functions of those choices.

## 4. Flexible and syndrome budgets

For the first-return gates the exact dimensions are

\[
\boxed{
\begin{array}{c|r|r|r}
\text{gate/fibre}&q&J&F=q-J\\\hline
G_{81}\text{ neutral}&971&567&404\\
G_{81}\text{ one-slack}&970&568&402\\
G_{82}\text{ neutral}&983&574&409\\
G_{82}\text{ one-slack}&982&575&407
\end{array}
}
\]

At a critical Euclidean scale, `L/q -> log_2 3`. Since the gate-wide cube has

\[
J=L-q-1
\]

up to the finite endpoint convention, asymptotically

\[
\boxed{
\frac{J}{q}
\longrightarrow
\log_2\frac32
=0.5849625007\ldots
}
\]

and

\[
\boxed{
\frac{F}{q}
\longrightarrow
1-\log_2\frac32
=2-\log_2 3
=0.4150374993\ldots.
}
\]

Thus roughly 58.5% of the Hensel coordinates in this explicit section are independent pivots and roughly 41.5% are dependent syndrome coordinates.

This is another appearance of the same complementary critical ratio already present in the synchronized Beatty/Hensel clock.

## 5. Integer-credit target

Suppose the right suffix already supplies an ordinary integer predecessor credit

\[
\delta>0.
\]

Prepending the cube block produces a full integer predecessor only if the left correction difference satisfies

\[
\boxed{
D(\epsilon)+2^L\delta
\equiv0\pmod{3^q}.
}
\]

After dividing by `2^F`, this becomes

\[
\boxed{
Z(\epsilon)
\equiv
-2^{L-F}\delta
\pmod{3^q}.
}
\]

For the gate-wide cube

\[
L-F=2J+1,
\]

so the normalized target is simply

\[
\boxed{
T_\delta
:=[-2^{2J+1}\delta]_{3^q}.
}
\]

Its low part

\[
t_\delta:=T_\delta\pmod{3^J}
\]

selects one unique cube vector `epsilon(t_delta)`. Full integerization is then equivalent to the **single syndrome equality**

\[
\boxed{
S(t_\delta)
=
\frac{T_\delta-t_\delta}{3^J}
\pmod{3^F}.
}
\]

Thus the `3^q` search has collapsed to one deterministic balanced-Hensel lift followed by one high-syndrome comparison.

## 6. Exact finite audit for the recurrent credit range

The earlier length-19 all-credit analysis found a bounded recurrent integer-credit channel with

\[
\boxed{7\le\delta\le397,}
\]

and no credit outside the interval `[1,397]` is needed to cover that finite SCC.

For a stronger finite test, audit **every**

\[
\boxed{1\le\delta\le397}
\]

against each of the four first-return explicit cubes.

All arithmetic is exact arbitrary-precision integer arithmetic. For each `delta`:

1. compute `T_delta mod 3^q`;
2. recover the unique balanced vector matching `T_delta mod 3^J`;
3. evaluate its exact normalized correction `Z`;
4. compute
   \[
   v_3(Z-T_\delta)-J;
   \]
   to count how many additional high-syndrome trits match;
5. accept only if the valuation reaches the full exponent `q`.

The exact results are

\[
\boxed{
\begin{array}{c|r|l|r}
\text{gate/fibre}&\text{full lifts}&\text{extra high-trit match distribution}&\max\\\hline
G_{81}\text{ neutral}&0&
0:254,\ 1:97,\ 2:32,\ 3:9,\ 4:3,\ 5:2&5\\
G_{81}\text{ one-slack}&0&
0:266,\ 1:89,\ 2:30,\ 3:8,\ 4:4&4\\
G_{82}\text{ neutral}&0&
0:259,\ 1:90,\ 2:35,\ 3:8,\ 4:3,\ 6:2&6\\
G_{82}\text{ one-slack}&0&
0:263,\ 1:95,\ 2:25,\ 3:10,\ 5:3,\ 6:1&6
\end{array}
}
\]

The maximizers are:

- `G_81` neutral: `delta=103,142` match five high syndrome trits;
- `G_81` one-slack: `delta=103,142,174,357` match four;
- `G_82` neutral: `delta=68,134` match six;
- `G_82` one-slack: `delta=51` matches six.

Hence, in the whole finite credit interval,

\[
\boxed{
\text{no nonzero credit fully lifts inside any of the four explicit first-return cubes.}
}
\]

More strongly, after the freely adjustable low `J` trits are matched, every tested credit fails within at most the next six high-syndrome trits.

## 7. Interpretation

This result should **not** be read as saying that the full gate fibre has no integer predecessor relation in this credit range. The explicit cube is only one state-preserving section of that fibre.

What has been proved is narrower and structurally useful:

1. the large low-Hensel freedom of the explicit cube is systematic rather than independent of the high digits;
2. the high-syndrome coordinates reject the entire previously observed finite credit interval almost immediately;
3. therefore the recurrent small-credit channel seen at length 19 cannot be propagated through a first-return gate **using this explicit gate-wide cube section**.

The remaining full-fibre problem is exactly a kernel/image problem:

\[
\boxed{
\mathcal K_t
=
\{\Delta\rho:
\text{same gate state},\
\Delta R\equiv0\pmod{3^J}
\}.
}
\]

Other gate orientations may lie in the same low-Hensel fibre and change the high syndrome or dyadic image.

## 8. Connection to the early R1 first-defect sector

The current isolated R1 branch has already been reduced to first Christoffel defect ranks

\[
\boxed{3,5,7,8,10,12.}
\]

These are extremely early odd events. In the gate correction sum, early odd events occupy the **high-Hensel end** of the triangular ordering, whereas the gate-wide pair cube supplies its independent pivots from the late odd events and controls the low-Hensel end.

Thus the two newest reductions target complementary ends of the same correction sum:

\[
\boxed{
\text{early first defect}
\longleftrightarrow
\text{high Hensel syndrome},
}
\]

\[
\boxed{
\text{late pair cube}
\longleftrightarrow
\text{low Hensel pivots}.
}
\]

This explains why the next theorem should not seek still more low-order Hensel freedom. That freedom is already enormous. The useful target is to propagate the six early-defect channels into the **high syndrome** and test whether any full same-state Hensel fibre can simultaneously satisfy the ordinary dyadic zero-lift condition.
