# First global resonance: a global budget on displaced odd ordinals

Date: 2026-08-26

Status: **exact arithmetic/combinatorial theorem inside the repaired global binary first-resonance branch.** It does not use the disputed ternary selector or the invalid repeated-local pullback. It does not prove Collatz.

## 1. Setup

At the first possible global coefficient crossing,

\[
(A,Q)=(114208327604,72057431991),
\]

let

\[
0\le a_1<\cdots<a_Q<A
\]

be the odd positions of a candidate first-crossing word and

\[
0\le b_1<\cdots<b_Q<A
\]

the positions of the mechanical first-crossing word.

The first-crossing prefix order gives

\[
\boxed{a_j\le b_j}\qquad(1\le j\le Q).
\]

Put

\[
s_j=b_j-a_j\ge0,
\]

and define the displaced-ordinal count

\[
\boxed{r_*:=\#\{j:s_j>0\}.}
\]

The exact normalized correction defect is

\[
\boxed{
\frac{E}{3^Q}
=
\sum_{j=1}^{Q}
\frac{2^{b_j}}{3^j}(1-2^{-s_j}).
}
\]

Therefore every displaced ordinal pays at least

\[
\boxed{c_j:=\frac{2^{b_j-1}}{3^j}.}
\]

## 2. Rational mechanical positions from the first-resonance Farey cell

The first-resonance slope has the lower Farey neighbour

\[
\frac{103768467013}{65470613321}
<
\gamma:=\log_2 3
<
\frac{114208327604}{72057431991},
\]

with determinant

\[
114208327604\cdot65470613321
-
103768467013\cdot72057431991
=1.
\]

Hence no rational strictly between these two fractions has denominator below their denominator sum. In particular, for every

\[
0\le n<Q,
\]

one has

\[
\boxed{
\lfloor n\gamma\rfloor
=
\left\lfloor\frac{nA}{Q}\right\rfloor.
}
\]

Thus

\[
b_{n+1}=\left\lfloor\frac{nA}{Q}\right\rfloor.
\]

Because \(\gcd(A,Q)=1\), the residues

\[
r_n:=nA\bmod Q
\]

form a permutation of

\[
0,1,\ldots,Q-1.
\]

Writing

\[
P:=\frac{2^A}{3^Q}>1,
\]

we obtain

\[
\begin{aligned}
c_{n+1}
&=\frac{2^{\lfloor nA/Q\rfloor-1}}{3^{n+1}}\\
&=\frac16 P^{n/Q}2^{-r_n/Q}\\
&\ge\boxed{\frac16\,2^{-r_n/Q}}.
\end{aligned}
\]

So the individual minimum displacement costs are bounded from below by one exact permutation of a monotone dyadic profile.

## 3. Cheapest possible set of R displaced ordinals

Even if we ignore all ordering constraints among the displacements, the cheapest possible choice of \(R\) indices must take the \(R\) largest residues \(r_n\).

Consequently

\[
\sum_{s_j>0}c_j
\ge
\frac16
\sum_{m=Q-R}^{Q-1}2^{-m/Q}.
\]

Since \(2^{-x}\) is decreasing,

\[
\sum_{m=Q-R}^{Q-1}2^{-m/Q}
\ge
Q\int_{1-R/Q}^{1}2^{-x}\,dx.
\]

Therefore

\[
\boxed{
\frac{E}{3^Q}
\ge
\frac{Q}{12\ln2}
\left(2^{R/Q}-1\right)
}
\]

whenever \(r_*\ge R\).

This estimate is deliberately optimistic for the candidate: it allows the displaced indices to be selected independently even though the ordinal ordering constraints can only increase the true minimum cost.

## 4. Whole first-resonance defect budget

For a genuine first-resonance candidate,

\[
N>2^{71},
\qquad
T^A(N)=N+g,
\qquad
g\ge4,
\]

and the mechanical normalized correction obeys

\[
S_{\rm mech}
\le
\frac{Q}{6\ln2}+\frac13.
\]

Since

\[
\frac{E}{3^Q}
=S_{\rm mech}-(P-1)N-Pg,
\]

we obtain

\[
\frac{E}{3^Q}
<
\frac{Q}{6\ln2}+\frac13
-(P-1)2^{71}-4P.
\]

The exact-rational companion certificate uses positive atanh-series bounds for \(\ln2\) and \(\ln3\), together with

\[
P-1>\ln P=A\ln2-Q\ln3,
\]

to certify the simple strict bound

\[
\boxed{
\frac{E}{3^Q}<4,314,000,000.
}
\]

## 5. Global displaced-ordinal exclusion

Take

\[
R=42,010,000,000.
\]

Using the first six positive terms of the exponential series in the integral lower bound gives, entirely with rational arithmetic,

\[
\boxed{
\frac{Q}{12\ln2}
(2^{R/Q}-1)
>4,314,000,000.
}
\]

This exceeds the complete available defect budget.

Hence

\[
\boxed{r_*<42,010,000,000.}
\]

Since \(r_*\) is integral,

\[
\boxed{r_*\le42,009,999,999.}
\]

Therefore at least

\[
Q-r_*
\ge
\boxed{30,047,431,992}
\]

odd ordinals occur at **exactly their mechanical positions**.

This is the first global quantitative restriction on the whole 114-billion-step middle bridge obtained from the same defect variable that controls the near-return gap.

## 6. Height consequence

Let

\[
h_i=q_i-k_i\ge0
\]

be the Beatty excursion height at a prefix time \(i\).

If \(h_i=h\), then at least \(h\) odd ordinals have already occurred earlier than their mechanical positions. Therefore

\[
\boxed{h_i\le r_*}
\]

for every prefix.

Consequently every first-resonance candidate satisfies the global excursion-height bound

\[
\boxed{
h_i<42,010,000,000
\qquad(0\le i<A).
}
\]

The middle bridge may still be long, but it can no longer carry arbitrary Beatty height or arbitrary ordinal transport.

## 7. DSD proof-chain role

The important point is not the decimal constant itself. The DSD-style alignment has turned three previously separate objects into one budgeted state:

\[
\boxed{
\text{Beatty excursion}
\leftrightarrow
\text{ordinal displacement}
\longrightarrow
\text{correction defect}
\longrightarrow
\text{near-return budget}.
}
\]

The global middle bridge is therefore constrained by a finite resource: displaced ordinals cannot exceed about 58.3% of the total first-resonance odd events, and at least about 41.7% must remain mechanically aligned.

## 8. Next target

The natural next step is no longer to increase the finite \(D_{72}\) brute-force cutoff indefinitely. It is to exploit the continued-fraction / Christoffel block recursion of the first-resonance mechanical word and ask:

> Can a primitive renewal word alter at most \(42.01\) billion of the \(72.06\) billion mechanical odd ordinals, satisfy the early 72-bit natural-address condition, and still realize the late near-return endpoint condition?

A useful proof would compress this question recursively over standard/semistandard Christoffel blocks rather than over individual parity steps.

Certificate:

`collatz/src/global_first_resonance_displacement_budget_certificate.py`.
