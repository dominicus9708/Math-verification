# Height-normalized predecessor credit and the first-return phase cocycle

Date: 2026-08-19

Status: **exact algebraic globalization lemma for the predecessor-credit amplitude channel + exact finite 19-step source bounds**.  This removes exponential growth from one repair channel.  It does **not** yet bound the full mixed-place/Hensel syndrome multiplicity and therefore is not a proof of the Collatz conjecture.

## 1. Why scalar credit was the wrong coordinate

For a same-length, same-odd-count alternate word `u` against an actual word `w`, the ordinary integer predecessor-credit recursion is

\[
\boxed{
\delta_L
=
\frac{R_u-R_w+2^L\delta_R}{3^q}
}
\]

whenever the numerator is a positive multiple of \(3^q\).

The current depth-28 p=8 renewal calculation exposed a normalization issue.  Its number `290` is not an ordinary gate credit.  It is the common-suffix-normalized quantity

\[
\widehat\delta
=
\frac{\Delta_{\rm return}}{2^{18}}
=
\frac{\Delta_{\rm end}}{3^{11}}
=290.
\]

The exact coordinate correction is certified by

`collatz/src/m45_p8_projective_credit_alignment_certificate.py`.

The correct global normalization is obtained by carrying the relative coefficient height explicitly.

## 2. Height-normalized credit identity

Take one length-19 mechanical/Sturmian factor.  Let

- \(Q\in\{11,12\}\) be its mechanical odd count;
- \(q\) be the actual odd count of the chosen orientation;
- \(H\ge0\) be the incoming relative height;
- \(H'\ge0\) be the outgoing relative height.

By definition,

\[
\boxed{
H'=H+q-Q.
}
\]

Apply the ordinary credit recursion with \(L=19\):

\[
\delta_L
=
\frac{R_u-R_w+2^{19}\delta_R}{3^q}.
\]

Define

\[
\boxed{
\chi_L:=\frac{\delta_L}{3^H},
\qquad
\chi_R:=\frac{\delta_R}{3^{H'}}.
}
\]

Since \(q+H=Q+H'\), substitution gives the exact identity

\[
\boxed{
\chi_L
=
\frac{R_u-R_w}{3^{q+H}}
+
\frac{2^{19}}{3^Q}\chi_R.
}
\]

This is the first useful cancellation: the actual odd count \(q\) and the height change disappear completely from the homogeneous multiplier.

## 3. Exact all-factor local source theorem

The complete length-19 Euclidean quotient has exactly twenty Sturmian factor types.  The exhaustive integer certificate

`collatz/src/h19_allfactor_height_credit_source_certificate.cpp`

checks every binary orientation against every one of these twenty factors.

For all incoming heights \(H\ge0\), all factor types, and all same-\(q\) surviving pairs,

\[
\boxed{
\frac{|R_u-R_w|}{3^{q+H}}<8.
}
\]

The exact worst finite case is

\[
\frac{3,909,437}{531,441}
\approx7.35629543<8.
\]

The same verifier also proves that every locally created full-Hensel ordinary credit satisfies

\[
\boxed{
|\Delta|<7\,3^H.
}
\]

The exact worst normalized case is

\[
\frac{|\Delta|}{3^H}
=\frac{55}{9}
\approx6.11111<7.
\]

The exhaustive scan is needed only for \(0\le H\le12\).  Every length-19 mechanical factor has at most twelve odd symbols, so at \(H\ge12\) the survival constraint already admits the entire binary cube.  Increasing \(H\) cannot enlarge the correction spans while the displayed normalization denominators grow.

Thus the two inequalities hold for every \(H\ge0\).

## 4. Bounded source over a first-return gate

Write one 19-step normalized transition as

\[
\chi_i=s_i+a_i\chi_{i+1},
\qquad
|s_i|<8,
\qquad
 a_i=\frac{2^{19}}{3^{Q_i}}.
\]

For any mechanical/Sturmian prefix of length \(t\), its odd count differs from \(t\log_3 2\) by less than one.  Consequently every partial homogeneous product inside a gate satisfies

\[
\boxed{
\prod_{i<j}a_i<3.
}
\]

A first-return gate contains at most 82 length-19 blocks.  Therefore its accumulated normalized source obeys the safe uniform bound

\[
\boxed{
|S_{\rm gate}|<8\cdot3\cdot82=1968.
}
\]

No statistical independence is used here.

## 5. Exact G81/G82 phase coboundary

Put

\[
\alpha:=\log_3 2,
\qquad
\varepsilon:=12-19\alpha,
\qquad
\delta:=1-81\varepsilon.
\]

The exact first-return theorem partitions the phase interval \([0,\varepsilon)\) into

\[
I_{81}=[0,\varepsilon-\delta),
\qquad
I_{82}=[\varepsilon-\delta,\varepsilon).
\]

The two gate vectors are

\[
G_{81}:(L,q)=(1539,971),
\qquad
G_{82}:(L,q)=(1558,983).
\]

Their normalized homogeneous multipliers are

\[
\frac{2^{1539}}{3^{971}}
=3^{1539\alpha-971}
=3^\delta,
\]

and

\[
\frac{2^{1558}}{3^{983}}
=3^{1558\alpha-983}
=3^{\delta-\varepsilon}.
\]

The first-return phase map is

\[
x'=
\begin{cases}
x+\delta,&x\in I_{81},\\
x+\delta-\varepsilon,&x\in I_{82}.
\end{cases}
\]

Hence in both cases

\[
\boxed{
A_{\rm gate}=3^{x'-x}.
}
\]

Thus the slight expansion of G81 and the contraction of G82 are not independent effects whose average must be estimated.  They are one exact phase coboundary.

## 6. Phase-adjusted credit potential

Define

\[
\boxed{
\Psi:=3^x\chi
=3^x\frac{\delta_{\rm credit}}{3^H}.
}
\]

At gate level,

\[
\chi_L=S_{\rm gate}+3^{x'-x}\chi_R.
\]

Multiplying by \(3^x\) gives

\[
\boxed{
\Psi_L
=
\Psi_R+3^xS_{\rm gate}.
}
\]

The homogeneous coefficient has disappeared exactly.

Because

\[
0\le x<\varepsilon<1,
\]

we have \(3^x<3\).  Therefore

\[
\boxed{
|\Psi_L-\Psi_R|<3\cdot1968=5904.
}
\]

Iterating through \(n\) first-return gates gives

\[
\boxed{
|\Psi_0-\Psi_n|<5904n.
}
\]

In the common predecessor construction with terminal relation \(\delta_n=0\),

\[
\boxed{
|\Psi_0|<5904n.
}
\]

At a renewal boundary \(H=0\), ordinary credit therefore has only linear amplitude in the number of first-return gates:

\[
\boxed{
|\delta_{\rm renewal}|=O(n).
}
\]

Equivalently the **excess credit exponent** satisfies

\[
\boxed{
\log_3(1+|\delta|)-H
=O(\log n).
}
\]

Thus predecessor credit cannot create an independent positive exponential repair rate above the height channel.

## 7. Meaning for the globalization program

The static-aggregation globalization criterion requires any surviving global branch to repay a linear formation-exclusion budget.  Before the present normalization, predecessor credit looked capable of carrying a separate exponentially growing repair resource.

This lemma removes that possibility:

\[
\boxed{
\text{height-normalized credit repair has zero exponential growth rate.}
}
\]

The remaining repair channels are now more sharply separated:

1. **height itself** — paid by defect/correction loss or long-excursion cost;
2. **mixed-place/Hensel syndrome multiplicity** — still requires a growth bound;
3. **cross-base selector concentration** — the current m=45 depth-28 theorem bounds one fresh window very strongly, but repeated conditioned windows still require a renormalization theorem.

The depth-28 renewal computation additionally compresses the finite Hensel exception graph to three named states \(E_{10},E_{18},E_{21}\), with only 873 open-excursion representatives at the right boundary.  The exact graph is certified separately by

`collatz/src/m45_depth28_renewal_syndrome_graph_certificate.cpp`.

## 8. What remains for a full extinction theorem

The credit channel is no longer the main asymptotic obstruction.  A sufficient next theorem is now:

> **Renewal-conditioned mixed-place growth theorem.**  After quotienting by relative height and the phase-adjusted credit \(\Psi\), the number/correlation mass of distinct Hensel-syndrome continuation states grows subexponentially in the number of first-return gates.

If this gives a repair budget \(B_n=o(n)\), then the previously proved positive formation-exclusion rate dominates and the integer-mass extinction criterion applies.

The present note proves the credit-amplitude part of that statement, not the remaining syndrome/correlation part.
