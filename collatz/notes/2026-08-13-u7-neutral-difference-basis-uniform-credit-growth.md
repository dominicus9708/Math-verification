# U7 neutral difference-basis and uniform predecessor-credit growth

Date: 2026-08-13

Status: **exact finite difference-basis certificate + uniform successor-growth lemma**.  This concerns the correction-collision transducer inside the Euclidean macroblock hierarchy.  It gives an existence theorem for a growing credit successor; it does not prove that a hypothetical Collatz candidate must select that successor, and it is not a proof of Collatz.

## 1. Neutral U7 block

Use the deterministic Euclidean return word

\[
\boxed{
U_7=011011011010110110101101101.
}
\]

It has

\[
L=27,
\qquad Q=17.
\]

Let \(\mathcal N_7\) be the actual orientations with relative survival state

\[
(\Sigma,M)=(0,0).
\]

Every such orientation therefore has exactly `Q=17` odd symbols and can replace another neutral orientation without changing the incoming or outgoing Beatty slack or the set of allowed future continuations.

For an orientation `w`, let `R(w)` be its exact Collatz correction and define the neutral correction-residue set

\[
\boxed{
S_7=\{R(w)\bmod3^{17}:w\in\mathcal N_7\}.
}
\]

## 2. Exact finite counts

The verifier obtains

\[
\boxed{|\mathcal N_7|=1,741,350}
\]

and

\[
\boxed{|S_7|=1,478,620}.
\]

The exact correction extrema are

\[
R_{\min}=129,009,091,
\]

\[
R_{\max}=1,096,880,542,
\]

so the correction width is

\[
\boxed{
W_7=R_{\max}-R_{\min}=967,871,451.
}
\]

## 3. Deterministic 90,000-element difference basis

Order every element `r in S7` by the deterministic key

\[
(\operatorname{splitmix64}(r),r)
\]

and let \(B_7\subset S_7\) be the first exactly 90,000 residues in this order.

The exact OpenMP verifier marks every cyclic difference

\[
a-b\pmod{3^{17}},
\qquad a,b\in B_7.
\]

It certifies

\[
\boxed{
B_7-B_7
=\mathbb Z/3^{17}\mathbb Z.
}
\]

Since \(B_7\subset S_7\), this proves a fortiori

\[
\boxed{
S_7-S_7
=\mathbb Z/3^{17}\mathbb Z.
}
\]

This is a finite certificate, not a probabilistic coverage estimate: all

\[
3^{17}=129,140,163
\]

residues are explicitly marked.

## 4. Neutral credit transducer

Suppose a suffix collision currently carries an integer quotient/credit state \(D\).  Prepending two neutral `U7` orientations `w_h,w_l` gives

\[
\boxed{
D'
=
\frac{R(w_h)-R(w_l)+2^{27}D}{3^{17}}
}
\]

whenever the numerator is divisible by \(3^{17}\).

Because \(S_7-S_7\) is the whole residue group, for **every integer \(D\)** there is at least one neutral pair satisfying the required congruence

\[
R(w_h)-R(w_l)
\equiv-2^{27}D
\pmod{3^{17}}.
\]

Hence:

\[
\boxed{
\text{the neutral }U_7\text{ transducer has at least one successor for every }D\in\mathbb Z.
}
\]

This is an exact totality statement.

## 5. Uniform interval bound on every successor

For any neutral pair,

\[
-W_7
\le R(w_h)-R(w_l)\le W_7.
\]

Therefore every valid successor satisfies

\[
\boxed{
\frac{2^{27}D-W_7}{3^{17}}
\le D'
\le
\frac{2^{27}D+W_7}{3^{17}}.
}
\]

In approximate orientation only,

\[
\frac{2^{27}}{3^{17}}
\approx1.039318,
\qquad
\frac{W_7}{3^{17}}
\approx7.49474.
\]

The proof comparisons below use integers only.

## 6. Sharp integer threshold for guaranteed available growth

A sufficient condition that the lower endpoint of the successor interval exceed \(D\) is

\[
(2^{27}-3^{17})D>W_7.
\]

Now

\[
2^{27}-3^{17}=5,077,565.
\]

Exact multiplication gives

\[
5,077,565\cdot190
=964,737,350
<W_7,
\]

while

\[
5,077,565\cdot191
=969,814,915
>W_7.
\]

Consequently

\[
\boxed{
D\ge191
\Longrightarrow
\exists\text{ a neutral }U_7\text{ successor }D'>D.
}
\]

In fact, because the entire interval bound lies above \(D\) once the inequality holds, **every valid neutral U7 successor** is larger than \(D\) for \(D\ge191\).

This last strengthening uses both totality and the correction-width bound: totality guarantees that at least one valid successor exists, while the width inequality forces every possible valid successor above the incoming state.

## 7. Interpretation

This is the first uniform growth lemma in the Euclidean predecessor-credit program.

Earlier results showed only individual growing witnesses

\[
1,2,3,5,11,19,35,47,\ldots
\]

at selected macroblock scales.  The present result says something qualitatively different:

> once a collision quotient has reached 191, **no neutral U7 block can keep it from increasing**, and a successor always exists.

The theorem is still an existence/transport statement on the alternate-orientation fibre.  It does not yet show that every actual critical R2 orientation belongs to a positive-credit fibre, nor does it bound the density of such fibres.  A coverage theorem remains necessary before this can eliminate the aperiodic R2 branch.

## 8. Verification

`collatz/src/u7_neutral_difference_basis_growth_certificate.cpp` verifies with exact integer arithmetic:

1. the neutral word count `1,741,350`;
2. the unique residue count `1,478,620`;
3. the exact correction extrema and width;
4. the deterministic 90,000-element basis;
5. full coverage of all `129,140,163` cyclic differences;
6. the exact threshold inequalities at `D=190` and `D=191`.

The difference calculation is parallelized only for speed; the marked bitset and all final checks are exact.
