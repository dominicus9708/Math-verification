# Repeated backtrace local-minimality filter inside the `m=44` R1 core

Date: 2026-08-12

Status: **exact local back-tracing exclusion + transition-conditioned window strengthening at the current upper-CF resonance**. The classical external input is the back-tracing-vector fact that a fixed finite inverse exponent pattern is admissible on one residue class modulo a power of three. The project-specific result couples these classes repeatedly to zero-defect orbit states and raises the `m=44` defect floor from `16.3832%` to `18.5090%`. This does not prove Collatz and does not yet close the `m=44` block.

## 1. Current finite core

Use the isolated upper-CF first-crossing resonance

\[
A=217,976,794,617,
\qquad
H=137,528,045,312.
\]

The strategic remaining finite block is

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

with

\[
V_0:=4\cdot3^{44}+2<N\le N_1:=6\cdot3^{44}+1.
\]

Numerically,

\[
V_0=3,939,083,608,734,444,931,526,
\]

so in particular

\[
\boxed{N>\frac{8H}{3}.}
\]

Let the odd-only orbit be

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad v_i=v_2(3x_i+1),
\]

and keep the exact skew coordinate

\[
h_i=\lfloor i\log_2 3\rfloor-a_i^{\rm cum}\ge0.
\]

At a zero-defect odd event, `h_i=0`, the existing renewal-state formula gives

\[
x_i=(N+c_i)2^{\{i\log_2 3\}},
\qquad c_i<\frac H3,
\]

hence

\[
\boxed{x_i<2\left(N+\frac H3\right).}
\]

## 2. General local back-tracing lemma

Take any finite odd-to-odd exponent code

\[
\mathbf a=(a_1,\ldots,a_q),
\qquad a_j\ge1,
\]

with total binary exponent

\[
K=\sum_{j=1}^q a_j.
\]

Its affine map has the form

\[
F_{\mathbf a}(m)
=\frac{3^q m+R_{\mathbf a}}{2^K},
\qquad R_{\mathbf a}>0.
\]

The endpoint residue is

\[
\rho(\mathbf a)
\equiv R_{\mathbf a}2^{-K}\pmod{3^q}.
\]

Thus every positive integer endpoint `y` with

\[
y\equiv\rho(\mathbf a)\pmod{3^q}
\]

has the corresponding integer ancestor

\[
\boxed{
m=\frac{2^K y-R_{\mathbf a}}{3^q}.}
\]

Because `R_a>0`,

\[
\boxed{m<\frac{2^K}{3^q}y.}
\]

This is the standard finite back-tracing-vector / unique `3^q` congruence principle.

For the present zero-defect states, if

\[
\frac{2^K}{3^q}\le\frac49,
\]

then

\[
m
<\frac49\,2\left(N+\frac H3\right)
=\frac89N+\frac{8H}{27}
<N,
\]

where the last inequality uses `N>8H/3`.

Therefore:

\[
\boxed{
\text{a zero-defect orbit state cannot lie in any back-tracing residue class with }2^K/3^q\le4/9.
}
\]

Otherwise a smaller positive integer merges with the hypothetical minimal-counterexample orbit.

## 3. Exact short forbidden residue classes

### Two inverse odd steps

The code

\[
(1,1)
\]

has

\[
K=2,
\qquad
\frac{2^K}{3^2}=\frac49.
\]

Its composition is

\[
F_{(1,1)}(m)=\frac{9m+5}{4}.
\]

Hence the endpoint condition is

\[
\boxed{y\equiv8\pmod9.}
\]

Every zero-defect state in this class is impossible.

### Three inverse odd steps

The code `(1,1,1)` has endpoint residue

\[
26\pmod{27},
\]

but this is already contained in `8 mod 9`, so it adds no new class.

### Four inverse odd steps

The codes with total exponent `K<=5` are

\[
(1,1,1,1),
(2,1,1,1),
(1,2,1,1),
(1,1,2,1),
(1,1,1,2).
\]

Their endpoint residues modulo `81` are respectively

\[
80,\ 26,\ 71,\ 20,\ 40.
\]

The first three lie in `8 mod 9`. Therefore the genuinely new short classes are

\[
\boxed{20\pmod{81}}
\]

and

\[
\boxed{40\pmod{81}.}
\]

The complete `q<=4` local minimality rule is therefore

\[
\boxed{
h_i=0
\Longrightarrow
x_i\not\equiv8\pmod9,
\quad
x_i\not\equiv20,40\pmod{81}.}
\]

## 4. Why this is a true local rule

For an odd-to-odd valuation block

\[
v_{i-q},\ldots,v_{i-1},
\]

the endpoint modulo `3^q` is independent of the state before the block because the earlier-state coefficient carries a factor `3^q`.

Equivalently, if

\[
z_{t+1}\equiv(3z_t+1)2^{-v_t}\pmod{3^q},
\]

then after `q` transitions the residue depends only on the last `q` valuations.

Thus the forbidden classes above are not root-only ternary cylinders. They can be checked at **every zero-defect endpoint along the orbit** using only a finite suffix of the valuation word.

This is the key difference from the earlier one-time reverse-ancestor sieve.

## 5. Coupling to the skew transition language

On a primitive upper-CF first-crossing segment,

\[
v_i=r_i+h_i-h_{i+1},
\]

where

\[
r_i=\lfloor(i+1)\log_2 3\rfloor-\lfloor i\log_2 3\rfloor\in\{1,2\}
\]

and

\[
h_{i+1}\le h_i+r_i-1.
\]

Therefore the local minimality rule can be inserted directly into the existing transition-conditioned skew DP.

Use the `m=44` branch-specific length-47 zero-endpoint windows. The critical valuation language has exactly `48` factors.

The DP state is enlarged only from

\[
(h,j)
\]

to

\[
\boxed{(h,j,z)},
\qquad z\in\mathbb Z/81\mathbb Z,
\]

with update

\[
z'=(3z+1)2^{-v}\pmod{81}.
\]

Whenever the new endpoint has `h'=0`, reject the path if

\[
z'\equiv8\pmod9
\]

or

\[
z'\equiv20,40\pmod{81}.
\]

No individual integer start is enumerated.

## 6. Exact filtered local capacities

Let `C_j` be the number of surviving `(critical factor, skew path)` local types with exactly `j` positive internal skew coordinates.

The first filtered capacities are

\[
\boxed{
\begin{array}{c|r}
j&C_j\\\hline
0&48\\
1&925\\
2&8,845\\
3&57,810\\
4&300,894\\
5&1,358,317\\
6&5,546,570\\
7&20,903,417\\
8&73,672,624\\
9&245,352,790\\
10&778,021,771\\
11&2,362,496,663\\
12&6,900,828,158\\
13&19,461,781,802\\
14&53,150,715,786\\
15&140,914,112,831
\end{array}
}
\]

For comparison, before imposing the repeated `3`-adic minimality rule the corresponding capacities began

\[
48,\ 1,291,\ 17,981,\ 172,710,\ 1,285,571,\ldots
\]

and in particular the `j=10` capacity was

\[
11,134,285,529.
\]

The local minimality filter lowers it to

\[
778,021,771.
\]

## 7. Global overlapping-window incidence bound

There are

\[
H-47
\]

length-47 window positions.

If

\[
r_*=\#\{i:0\le i<H,\ h_i>0\},
\]

then at least

\[
E=H-47-2r_*
\]

windows have zero endpoints, and their total internal defect incidence is at most

\[
46r_*.
\]

Let `Phi(E)` be the greedy minimum incidence cost obtained by filling the filtered capacities `C_0,C_1,...` in increasing `j` order.

Every candidate must satisfy

\[
\boxed{
\Phi(H-47-2r_*)\le46r_*.
}
\]

Exact integer evaluation gives the least admissible value

\[
\boxed{
r_*=25,455,014,904.}
\]

At `r_*-1`,

\[
\Phi=1,170,930,685,561
>
1,170,930,685,538
=46(r_*-1),
\]

while at the threshold

\[
\Phi=1,170,930,685,531
<
1,170,930,685,584
=46r_*.
\]

Therefore every `m=44` candidate at the current resonance obeys

\[
\boxed{
r_*\ge25,455,014,904,}
\]

or

\[
\boxed{
\frac{r_*}{H}>0.1850896291.
}
\]

Thus more than `18.50%` of all odd-event coordinates must depart from the critical mechanical cap.

This strictly strengthens the previous branch-specific floor

\[
16.38327478\%.
\]

## 8. Structural interpretation

The useful new object is not the numerical `18.50%` itself but the repeated compatibility chain

\[
\boxed{
\text{short contracting back-tracing code}
\to
3\text{-adic endpoint class}
\to
\text{local valuation suffix}
\to
\text{forbidden zero-defect factor}
\to
\text{global overlapping-window capacity loss}.}
\]

This is a true local-language constraint and therefore can legitimately be iterated along the entire hypothetical orbit.

It also supplies the desired conceptual bridge between the previously separate `3`-adic predecessor channel and the Sturmian/skew defect channel.

## 9. Scope and next target

This stronger defect floor still does **not** close the `m=44` block by the real correction budget alone. The available correction allowance at the low end of the block remains too large.

The next exact extension is to add longer contracting back-tracing classes. Through inverse odd-depth six, the first genuinely new classes beyond the `q<=4` rule occur modulo `3^6=729` at

\[
\boxed{91,137,319,479,661\pmod{729}.}
\]

A higher-resolution local automaton can insert these classes as additional repeated forbidden factors.

More importantly, the same construction can be applied after a short forward descendant, producing a repeated forward/backward merge filter rather than a root-only reverse sieve.

## External background

The standard back-tracing-vector framework and the fact that a fixed finite feasible inverse vector is admissible on a unique residue class modulo `3^q` are classical; see the back-tracing discussion in Monks, Monks, Monks & Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Discrete Mathematics 313 (2013), arXiv:1204.3904, especially their discussion of Wirsching's feasible vectors. The project-specific contribution here is the repeated coupling of these classes to the zero-defect local language and the resulting exact incidence bound.
