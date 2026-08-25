# First-crossing excursion area equals ordinal transport

Date: 2026-08-26

Status: **general exact combinatorial identity for the first-coefficient-crossing language.** It is independent of the disputed ternary selector and of repeated local pullback arguments. It does not prove Collatz.

## 1. Setup

Let a length-\(A\) first-coefficient-crossing word contain \(Q\) odd positions

\[
0\le a_1<\cdots<a_Q<A.
\]

Let the mechanical/Beatty boundary word at the same \((A,Q)\) have odd positions

\[
0\le b_1<\cdots<b_Q<A.
\]

For a first crossing, prefix dominance gives

\[
\boxed{a_j\le b_j}\qquad(1\le j\le Q).
\]

Define the ordinal displacement

\[
\boxed{s_j:=b_j-a_j\ge0.}
\]

Let \(q_i\) and \(k_i\) be the actual and mechanical numbers of odd events among positions \(0,\ldots,i-1\), and put

\[
\boxed{h_i:=q_i-k_i\ge0.}
\]

The quantity \(h_i\) is the vertical Beatty excursion height of the actual prefix above the coefficient-survival boundary.

## 2. Exact area/transport identity

Count the incidence pairs \((i,j)\) for which the \(j\)-th odd event has already occurred by time \(i\).

For the actual word,

\[
\sum_{i=1}^{A}q_i
=
\sum_{j=1}^{Q}(A-a_j).
\]

For the mechanical word,

\[
\sum_{i=1}^{A}k_i
=
\sum_{j=1}^{Q}(A-b_j).
\]

Subtracting gives

\[
\boxed{
\sum_{i=1}^{A}h_i
=
\sum_{j=1}^{Q}(b_j-a_j)
=
\sum_{j=1}^{Q}s_j.
}
\]

At the completed crossing the two words have the same total odd count, so \(h_A=0\). Hence equivalently

\[
\boxed{
\sum_{i=1}^{A-1}h_i
=
\sum_{j=1}^{Q}s_j.
}
\]

Thus the area of the Beatty excursion and the total leftward transport distance of the odd ordinals are not merely correlated descriptors: they are exactly the same integer.

## 3. One-sided Lipschitz constraint on the displacement path

For the first-resonance/mechanical word the consecutive mechanical odd positions satisfy

\[
b_{j+1}-b_j\in\{1,2\}.
\]

Every actual parity word has

\[
a_{j+1}-a_j\ge1.
\]

Therefore

\[
\begin{aligned}
s_{j+1}-s_j
&=(b_{j+1}-b_j)-(a_{j+1}-a_j)\\
&\le1.
\end{aligned}
\]

So

\[
\boxed{s_{j+1}\le s_j+1.}
\]

A displacement spike cannot be created instantaneously; reaching height \(S\) requires a staircase of prior transport.

For a hypothetical minimal counterexample, \(N\equiv3\pmod4\) forces the initial shortcut parity symbols `11`, which coincide with the mechanical prefix. Hence at the first global resonance

\[
\boxed{s_1=s_2=0.}
\]

If

\[
S:=\max_j s_j,
\]

then the rise constraint implies that before a first occurrence of \(S\), the sequence must contain values at least

\[
1,2,\ldots,S.
\]

Consequently

\[
\boxed{
\sum_{j=1}^{Q}s_j
\ge
\frac{S(S+1)}2.
}
\]

Combining with the area identity,

\[
\boxed{
\max_j s_j
\le
\left\lfloor
\frac{\sqrt{1+8\sum_i h_i}-1}{2}
\right\rfloor.
}
\]

## 4. Relation to the correction defect

The exact normalized correction defect is

\[
\frac{E}{3^Q}
=
\sum_{j=1}^{Q}
\frac{2^{b_j}}{3^j}(1-2^{-s_j}).
\]

This gives a second projection of the same displacement path.

However, one must not infer a linear upper bound on the excursion area from the correction budget alone: the factor

\[
1-2^{-s}
\]

saturates as \(s\to\infty\). Therefore the global defect budget primarily controls the **number** and weighted placement of nonzero displacements, while the area identity controls their **transport distance**.

A further structural theorem is needed to prevent a small number of very large displacement excursions.

This limitation is important for the DSD audit: count, height, area, and defect are distinct descriptors even though they are coupled by exact identities.

## 5. DSD interpretation

The useful logical chain is now

\[
\boxed{
\text{coefficient-survival height }h_i
\longleftrightarrow
\text{ordinal transport }s_j
\longrightarrow
\text{real correction defect }E
\longrightarrow
\text{near-return budget}.
}
\]

The first arrow is an exact area identity rather than a heuristic analogy. This makes the middle survivor bridge accessible from either the prefix-height representation or the odd-ordinal displacement representation without changing the underlying state.

## 6. Next target

The remaining missing inequality can be stated cleanly:

> prove that a first-resonance path satisfying the two finite address boundaries and the tiny return-gap condition cannot concentrate its required transport into a sparse set of very large displacement spikes.

One possible route is to use the late \(3\)-adic endpoint exposure to constrain the terminal displacement vector; another is to derive a renewal/continued-fraction regularity condition that converts the current weighted defect budget into an area bound.

Regression certificate:

`collatz/src/first_crossing_excursion_area_identity_certificate.py`.
