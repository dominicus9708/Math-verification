# `m=44` bootstrap priority and branch-specific window defect floor

Date: 2026-08-12

Status: **exact branch-specific local-language bound + recursive-sufficiency bootstrap reduction**. It shows why the single `m=44` ternary block is the strategically dominant remaining finite core. This does not prove convergence of that block.

## 1. Global verified floor and the next Cantor block

Let

\[
V_0:=4\cdot3^{44}+2.
\]

Barina's published verification through `2^71`, combined with Ansari's recursively sufficient intersection sieve, proves the Collatz conjecture for every positive integer up to `V_0`.

Ansari's intersection is

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

The first members of `F` above `V_0` are exactly the `m=44` block

\[
\boxed{
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
}
\]

Its minimum is

\[
4\cdot3^{44}+3=V_0+1,
\]

and its maximum is

\[
\boxed{
N_1
=4\left(3^{44}+\frac{3^{44}-1}{2}\right)+3
=6\cdot3^{44}+1
=2\cdot3^{45}+1.
}
\]

Thus

\[
\boxed{F\cap(V_0,N_1]=\text{exactly the }m=44\text{ block}.}
\]

## 2. Why closing only m=44 would bootstrap the global floor

Ansari's recursive-sufficiency theorem says that, once every integer through `V_0` is known to converge, it is enough to prove convergence only for `F cap (V_0,N_1]` in order to extend the verified interval through `N_1`.

Therefore a proof that every `m=44` block member converges would imply

\[
\boxed{[1,N_1]\text{ is verified}.}
\]

But `N_1` has the special form required by Ansari's Proposition 3.2:

\[
N_1=2\cdot3^{45}+1.
\]

That proposition then doubles the interval automatically:

\[
\boxed{
[1,2N_1]
=[1,4\cdot3^{45}+2]
\text{ is verified}.}
\]

The next elements of `F` above this new floor are exactly the two `m=45` blocks.

Hence the three residual blocks are not strategically symmetric. The correct first target is the single `m=44` block; closing it produces a global verification jump before the `m=45` analysis begins.

## 3. Current first-crossing resonance

At the presently isolated upper-CF resonance

\[
A=217,976,794,617,
\qquad
H=137,528,045,312,
\]

define

\[
\gamma=\log_2 3,
\qquad
\kappa_q=\lfloor q\gamma\rfloor,
\qquad
h_q=\kappa_q-a_q\ge0.
\]

Let

\[
r_*:=\#\{q:0\le q<H:\ h_q>0\}.
\]

For every zero-defect odd event,

\[
x_q=(N+c_q)2^{\{q\gamma\}},
\qquad c_q<\frac H3,
\]

and therefore for the whole `m=44` block

\[
x_q<2\left(N_1+\frac H3\right).
\]

Exact integer arithmetic gives

\[
\boxed{
2\left(N_1+\frac H3\right)<2^{74}.
}
\]

Equivalently,

\[
3\,2^{74}-(6N_1+2H)
=21,216,645,315,550,682,090,006>0.
\]

## 4. Length-47 transition-conditioned windows

Take zero-endpoint odd-event windows of length

\[
\boxed{m=47.}
\]

The critical Sturmian valuation language has exactly `48` length-47 factors. Their time-expanded parity lengths split as

\[
\boxed{
25\text{ factors with }D=74,
\qquad
23\text{ factors with }D=75.
}
\]

Because every zero-defect start is strictly below `2^74`, each exact local parity word has at most one ordinary realization in the admissible state interval.

For each critical factor, count exactly the skew paths

\[
h_0=h_{47}=0,
\qquad
h_{i+1}\le h_i+r_i-1,
\qquad
h_i\ge0,
\]

by the number `j` of positive internal skew coordinates.

Summing over all 48 factors gives the first exact local capacities

\[
\boxed{
\begin{array}{c|r}
j&C_j\\\hline
0&48\\
1&1,291\\
2&17,981\\
3&172,710\\
4&1,285,571\\
5&7,901,554\\
6&41,730,678\\
7&194,599,968\\
8&817,211,454\\
9&3,136,858,278\\
10&11,134,285,529\\
11&36,885,993,640
\end{array}
}
\]

## 5. Global incidence threshold

There are `H-47` window positions. At most `2r_*` have a positive defect at one of their endpoints, so the number `E` of zero-endpoint windows obeys

\[
E\ge H-47-2r_*.
\]

Every global positive defect belongs to the interior of at most `46` such windows, hence

\[
\sum j(q)\le46r_*.
\]

Let `Phi_47(E)` be the greedy minimum incidence cost obtained by filling the capacities `C_0,C_1,...` in increasing `j` order. Necessarily

\[
\boxed{
\Phi_{47}(H-47-2r_*)\le46r_*.
}
\]

Exact integer evaluation gives the least admissible value

\[
\boxed{
r_*=22,531,597,565.}
\]

At this threshold,

\[
H-47-2r_*=92,464,850,135,
\]

\[
\Phi_{47}=1,036,453,487,941,
\]

and

\[
46r_*=1,036,453,487,990.
\]

At `r_*-1`, the minimum incidence cost is

\[
1,036,453,487,965
>
1,036,453,487,944
=46(r_*-1),
\]

so the previous integer is impossible.

Therefore every `m=44` candidate at this resonance satisfies

\[
\boxed{
r_*\ge22,531,597,565,}
\]

or

\[
\boxed{
\frac{r_*}{H}>0.1638327478.
}
\]

Thus more than `16.38%` of odd-event coordinates must depart from the mechanical cap.

## 6. Why this does not yet close m=44

The audited run-average correction theorem gives

\[
\eta\ge\frac5{48}r_*.
\]

The present defect floor therefore forces

\[
\eta\ge2,347,041,413.020833\ldots
\]

But the low end of the `m=44` block still has substantially more available Archimedean correction budget than this. Hence defect-density pressure alone does not eliminate the block.

The branch-specific strengthening is useful as a constraint, but not as the terminal mechanism.

## 7. Correct next mechanism

The `m=44` block should now be attacked with a minimal-counterexample sieve rather than another refinement of the same first-crossing density estimate.

Two compatible ingredients are available:

1. the ternary recursively sufficient Cantor core `F`;
2. independent reverse contracting-ancestor cylinders, which certify additional members of `F` as recursive by constructing a smaller positive Collatz ancestor.

Because closing the `m=44` block bootstraps the global verified floor to `4*3^45+2`, every global recursive subcylinder removed from this one block has leverage beyond the current single first-crossing resonance.

## External input

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025), especially Theorem 2.1, Corollary 2.1, Lemma 3.2, Proposition 3.2, and Remark 3.1.
