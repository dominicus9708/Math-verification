# Overlapping-window defect-density theorem and complete exclusion of the m=46 layer

Date: 2026-08-12

Status: **exact overlapping-window counting theorem for the current first unresolved upper-CF resonance + complete exclusion of the recursive-core `m=46` layer**. A factor-length refinement is independently checked with Wolfram. This does not prove Collatz.

## 1. Current resonance and defect coordinates

Work at the first upper continued-fraction first-crossing resonance not already covered by the published `2^71` convergence verification:

\[
A=217,976,794,617,
\qquad
H=137,528,045,312.
\]

Let

\[
\gamma:=\log_2 3,
\qquad
\kappa_q:=\lfloor q\gamma\rfloor,
\]

and let

\[
h_q:=\kappa_q-a_q\ge0
\qquad(0\le q<H)
\]

be the exact signed-skew / Christoffel-displacement coordinate at odd-event index `q`.

Define

\[
\boxed{r_*:=\#\{q:0\le q<H,\ h_q>0\}.}
\]

The exact coordinate-collapse theorem identifies `h_q` with the draft branch's cumulative mechanical-cap defect `z_q`.

The fully rational next-resonance certificate gives

\[
N<36,797,925,187,243,805,015,225<2^{75}.
\]

At every zero-defect odd event,

\[
h_q=0,
\]

we have

\[
x_q=(N+c_q)2^{\{q\gamma\}},
\qquad c_q<\frac H3,
\]

and therefore

\[
\boxed{
x_q<X:=2\left(N+\frac H3\right)<2^{76}.}
\]

This uniform state bound is the arithmetic input for the window count.

## 2. Critical valuation factors

Put

\[
r_q:=\kappa_{q+1}-\kappa_q\in\{1,2\}.
\]

The binary word `r_q-1` is a Sturmian/mechanical word, so the critical valuation language has factor complexity

\[
\boxed{p(m)=m+1.}
\]

Thus there are exactly `m+1` critical valuation factors of odd-event length `m`.

For an actual skew path,

\[
\boxed{v_q=r_q+h_q-h_{q+1}.}
\]

Hence, once a critical factor `(r_q,...,r_{q+m-1})` and the skew vector

\[
(h_q,h_{q+1},...,h_{q+m})
\]

are fixed, the exact local parity word is fixed.

## 3. Zero-endpoint windows

Fix an odd-event window length `m` and consider starts

\[
0\le q\le H-m-1.
\]

There are

\[
\boxed{W:=H-m}
\]

such windows, each using odd events `q,...,q+m` as endpoints with `m` transitions.

Call a window **zero-endpoint** if

\[
h_q=h_{q+m}=0.
\]

A positive defect can spoil at most one start endpoint and at most one end endpoint, so the number `E` of zero-endpoint windows satisfies

\[
\boxed{E\ge W-2r_*.}
\]

For a zero-endpoint window define its internal defect count

\[
j(q):=\#\{i:q<i<q+m,\ h_i>0\}.
\]

Each global positive-defect index belongs to the interior of at most `m-1` windows. Therefore

\[
\boxed{
\sum_{\text{zero-endpoint }q}j(q)
\le(m-1)r_*.
}
\]

This is the global incidence budget.

## 4. Counting skew patterns with j internal defects

Take a zero-endpoint window with exactly `j` positive internal skew coordinates.

The support can be chosen in at most

\[
\binom{m-1}{j}
\]

ways.

Because

\[
h_{i+1}\le h_i+(r_i-1)
\le h_i+1
\]

and the window begins at height zero, every positive internal height is at most the total number `j` of positive internal positions. Hence each positive height lies in

\[
\{1,2,...,j\}.
\]

A safe overcount of height assignments is therefore

\[
j^j.
\]

For `j=0` there is one zero assignment.

Multiplying by the `m+1` possible critical valuation factors, the number of candidate local parity words with exactly `j` internal defects is bounded by

\[
\boxed{
P_j(m)
\le
(m+1)
\binom{m-1}{j}j^j
\qquad(j\ge1),
}
\]

and

\[
\boxed{P_0(m)\le m+1.}
\]

Invalid height assignments or duplicate parity words are included in this count, so it is a rigorous upper bound.

## 5. Parity-cylinder multiplicity

For zero endpoints,

\[
a_{q+m}-a_q
=\kappa_{q+m}-\kappa_q.
\]

Thus the total time-expanded parity length `D` of the local word is exactly the critical parity span.

For `m=47`,

\[
\lfloor47\gamma\rfloor=74,
\]

so every zero-endpoint local word has

\[
\boxed{D\ge74.}
\]

By the parity-vector/residue bijection, one exact length-`D` parity word fixes the starting state to one residue class modulo

\[
2^D.
\]

Every zero-endpoint start is a zero-defect state and therefore satisfies

\[
0<x_q<2^{76}.
\]

Since `D>=74`, one residue class modulo `2^D` has at most

\[
\boxed{4}
\]

positive representatives below `2^76`.

Consequently the number `C_j` of zero-endpoint `m=47` windows with exactly `j` internal defects obeys

\[
\boxed{
C_0\le192,
}
\]

and for `j>=1`,

\[
\boxed{
C_j
\le
192\binom{46}{j}j^j.
}
\]

The first capacities are

\[
\boxed{
(C_0,C_1,C_2,C_3,C_4,C_5)
=
(192,
8,832,
794,880,
78,693,120,
8,020,869,120,
822,452,400,000)
}
\]

as safe upper bounds.

## 6. Capacity-minimization principle

Suppose there are `E` zero-endpoint windows. To minimize the total number of internal defect incidences among them subject to the capacities `C_j`, fill the smallest defect levels first:

1. use at most `C_0` windows of cost zero;
2. then at most `C_1` windows of cost one;
3. then `C_2` windows of cost two;
4. and so on.

Let

\[
\Phi_m(E)
\]

be this exact greedy minimum incidence cost. Because the costs `j` are increasing, the greedy fill is optimal.

Every candidate must satisfy simultaneously

\[
E\ge H-m-2r_*
\]

and

\[
\Phi_m(E)\le(m-1)r_*.
\]

Therefore a necessary condition is

\[
\boxed{
\Phi_m(H-m-2r_*)
\le(m-1)r_*.
}
\]

This is a purely finite integer inequality.

## 7. Exact m=47 lower defect count

For

\[
m=47,
\]

binary search / exact integer evaluation of the preceding capacity inequality gives the first admissible integer

\[
\boxed{
r_*=12,133,206,251.}
\]

At this value,

\[
H-m-2r_*
=113,261,632,763,
\]

and the exact greedy incidence minimum is

\[
\Phi_{47}=558,127,487,527,
\]

while

\[
46r_*=558,127,487,546.
\]

At `r_*-1` the inequality fails. Thus every candidate at the current resonance obeys the rigorous universal lower bound

\[
\boxed{
r_*\ge12,133,206,251.}
\]

Equivalently,

\[
\boxed{
\frac{r_*}{H}>0.0882235.
}
\]

So at least about `8.82%` of all odd-event coordinates must depart from the critical mechanical cap.

An independent Wolfram exact-integer implementation reproduced the threshold and the two incidence integers above.

## 8. Factor-length refinement: m=46

The preceding theorem deliberately used only the uniform parity-length lower bound. One can sharpen it by separating critical factors according to their exact parity length.

For `m=46`, the 47 critical valuation factors split as

\[
\boxed{
5\text{ factors with }D=72,
\qquad
42\text{ factors with }D=73.
}
\]

This split is obtained from the finite Sturmian length-46 factor partition; an independent 100-digit Wolfram enumeration collected exactly 47 distinct factors and returned the count map

\[
72\mapsto5,
\qquad73\mapsto42.
\]

Under the same state bound `x_q<2^76`, a `D=72` word has at most 16 positive representatives and a `D=73` word at most 8. Therefore the effective factor-multiplicity coefficient is

\[
\boxed{5\cdot16+42\cdot8=416.}
\]

The refined capacities are

\[
\boxed{
C_0\le416,
\qquad
C_j\le416\binom{45}{j}j^j.
}
\]

The same exact incidence minimization yields

\[
\boxed{
r_*\ge12,208,164,939.}
\]

or

\[
\boxed{
\frac{r_*}{H}>0.0887685.
}
\]

The `m=47` result is the simpler theorem; the `m=46` split is a certified finite sharpening.

## 9. Immediate exclusion of every m=46 ternary prefix

The independently audited run-average defect theorem gives

\[
\Delta S\ge\frac5{48}r_*.
\]

The rational ternary-prefix run budgets at the current resonance give the following upper bounds in the recursive `m=46` block:

\[
\begin{array}{c|r}
0000&11,613,503,138\\
0001&11,193,963,847\\
0010&10,354,885,265\\
0011&9,935,345,974\\
0100&7,837,649,519\\
0101&7,418,110,227\\
0110&6,579,031,645\\
0111&6,159,492,354\\
1000&285,942,279
\end{array}
\]

Already the simpler universal bound gives

\[
12,133,206,251
>
11,613,503,138.
\]

Therefore no high-four branch survives:

\[
\boxed{
\text{the entire recursive-core }m=46\text{ layer is impossible.}
}
\]

The previous separate `1000` exclusion is subsumed by this theorem.

## 10. Defect-improved global start ceiling

The factor-length-refined bound gives

\[
r_*\ge12,208,164,939.
\]

Hence the run-average theorem gives the real normalized correction loss

\[
\boxed{
\eta=\frac13\mathfrak D_H
\ge\frac5{48}r_*
=1,271,683,847.8125.
}

The exact first-crossing endpoint identity and Denjoy--Koksma bound give

\[
N
\le
\frac{
H/(6\ln2)+1/3-\eta-4P
}{P-1},
\qquad
P=\frac{2^A}{3^H}.
\]

At the current resonance,

\[
P-1
\approx8.98654870862\times10^{-13},
\]

so the refined universal ceiling becomes approximately

\[
\boxed{
N<3.53826836145\times10^{22}.
}

This lies below the minimum of the `m=46` layer,

\[
4\cdot3^{46}+3
=35,451,752,478,610,004,383,719,
\]

providing an independent magnitude-level confirmation that `m=46` has disappeared.

## 11. What remains

The current R1 recursive core is now reduced to the three lower 44-trit affine blocks:

\[
\boxed{
C_j\in
\{3^{44},\ 3^{45},\ 3^{45}+3^{44}\}
}
\]

in

\[
N=4\left(C_j+\sum_{i=0}^{43}a_i3^i\right)+3.
\]

These lower blocks have much more Archimedean correction budget, so defect-count density alone is not expected to remove them.

The next obstruction must use the ordinary-integer cross-base consistency more directly: the strengthened dyadic defect address, late-lift causality, and the ternary recursive-core endpoint structure.

## 12. Methodological consequence

This theorem shows that sparse-defect control is stronger when windows are overlapped globally rather than treated as disjoint runs.

The essential mechanism is

\[
\boxed{
\text{few global defects}
\Rightarrow
\text{many low-defect overlapping windows}
\Rightarrow
\text{too many repetitions of a small-complexity mechanical local language}
\Rightarrow
\text{parity-cylinder capacity contradiction}.
}

No statistical independence, random parity assumption, or density-zero argument is used.
