# First-resonance phase-renewal bridge to the next convergent

Date: 2026-08-27

Status: **SAFE LEMMA + exact continued-fraction certificate.**  This advances the repaired first-resonance branch.  It does not prove the Collatz conjecture.

## 1. Current repaired first-resonance state

Let

\[
\alpha=\log_3 2,
\qquad
b(n)=\lceil \alpha n\rceil.
\]

For the repaired first global resonance, write

\[
(A_0,Q_0)
=(114208327604,72057431991),
\]

and assume a hypothetical minimal counterexample satisfies

\[
y=T^{A_0}(N)=N+g,
\qquad
0<g<2^{33}.
\]

The endpoint near-survival theorem already proved on this branch gives

\[
3^{q_k(y)}\ge 2^k
\qquad (1\le k<A_0),
\]

hence

\[
q_k(y)\ge b(k)
\qquad (1\le k<A_0).
\]

The remaining question is what this second coefficient-survivor block implies for the original trajectory after time \(A_0\).

## 2. First-resonance phase defect

Define

\[
\varepsilon_0:=\alpha A_0-Q_0>0.
\]

The exact rational logarithm certificate gives

\[
\varepsilon_0
=5.016228338798793\ldots\times 10^{-12}.
\]

Thus

\[
\alpha A_0=Q_0+\varepsilon_0.
\]

For any later offset \(k\),

\[
b(A_0+k)
=Q_0+\left\lceil \alpha k+\varepsilon_0\right\rceil.
\]

So the issue is exactly when the small phase shift \(\varepsilon_0\) changes the ceiling of \(\alpha k\).

## 3. The first opposite-sided return

The continued fraction of \(\alpha\) contains the consecutive convergents

\[
\frac{6586818670}{10439860591}
<\alpha<
\frac{65470613321}{103768467013}.
\]

Put

\[
(K_1,P_1)
=(103768467013,65470613321),
\]

and

\[
\eta_1:=P_1-\alpha K_1>0.
\]

The exact interval certificate proves

\[
0<\eta_1
<\varepsilon_0
<\alpha\cdot10439860591-6586818670,
\]

numerically

\[
4.198237424141115\times10^{-12}
<
5.016228338798793\times10^{-12}
<
9.214465762939909\times10^{-12}.
\]

By the standard best-approximation-of-the-second-kind theorem for continued fractions, for every

\[
1\le k<K_1
\]

we have

\[
\|k\alpha\|
\ge
\|10439860591\,\alpha\|
>arepsilon_0.
\]

In particular the distance from \(\alpha k\) to its next integer is larger than \(\varepsilon_0\).  Therefore

\[
\boxed{
 b(A_0+k)=Q_0+b(k)
 \qquad(1\le k<K_1).
}
\]

At \(k=K_1\), however,

\[
P_1-\alpha K_1=\eta_1<\varepsilon_0,
\]

so the ceiling changes by one:

\[
\boxed{
 b(A_0+K_1)=Q_0+b(K_1)+1.
}
\]

Since \(b(K_1)=P_1\), this is

\[
b(A_0+K_1)=Q_0+P_1+1.
\]

## 4. Exact identification with the next lower convergent

The two resonance vectors add exactly:

\[
A_2=A_0+K_1
=217976794617,
\]

\[
Q_2=Q_0+P_1
=137528045312.
\]

The pair

\[
(Q_2,A_2)
=(137528045312,217976794617)
\]

is the next lower continued-fraction convergent already isolated elsewhere in the project.

Moreover

\[
\alpha A_2-Q_2
=arepsilon_0-\eta_1
=8.17990914657678\ldots\times10^{-13}>0,
\]

hence

\[
\boxed{b(A_2)=Q_2+1.}
\]

Thus the next lower resonance is not a separate numerical accident: it is the exact cancellation of the first lower phase defect by the intervening upper-convergent phase defect.

## 5. Transfer to the actual Collatz trajectory

Because

\[
y=T^{A_0}(N),
\]

odd-event counts concatenate:

\[
q_{A_0+k}(N)
=Q_0+q_k(y).
\]

The endpoint theorem gives

\[
q_k(y)\ge b(k)
\qquad(1\le k<A_0).
\]

Since \(K_1<A_0\), for every \(1\le k<K_1\),

\[
q_{A_0+k}(N)
\ge Q_0+b(k)
=b(A_0+k).
\]

Therefore

\[
\boxed{
3^{q_{A_0+k}(N)}\ge2^{A_0+k}
\qquad(1\le k<K_1).
}
\]

So after the first coefficient-subcritical event at \(A_0\), **no second coefficient-subcritical prefix can occur before \(A_2\)**.

At the endpoint \(k=K_1\), only two cases remain:

### Case I: surplus recovery

If

\[
q_{K_1}(y)\ge P_1+1,
\]

then

\[
q_{A_2}(N)
\ge Q_0+P_1+1
=b(A_2),
\]

so the original trajectory is coefficient-surviving at \(A_2\) as well.

### Case II: exact second resonance

If

\[
q_{K_1}(y)=P_1,
\]

then

\[
q_{A_2}(N)=Q_2=b(A_2)-1,
\]

so the original trajectory hits exactly the next lower resonance

\[
\boxed{
(A_2,Q_2)
=(217976794617,137528045312).
}
\]

There is no third possibility.

## 6. DSD interpretation

The first resonance is therefore a genuine renewal interface:

\[
\boxed{
\text{first lower resonance}
\;\xrightarrow{\text{endpoint survivor block}}\;
\text{phase-translated coefficient language}
\;\xrightarrow{K_1}\;
\begin{cases}
\text{surplus recovery},\\
\text{next lower resonance}.
\end{cases}
}
\]

The important point is that the huge interval between the two resonances does not require direct enumeration.  Its exclusion follows from the continued-fraction phase geometry plus the already-proved endpoint coefficient survival.

This converts the repaired binary target into a sharper branch split:

1. prove that the endpoint block gains at least one extra odd event by depth \(K_1\); or
2. if it has exactly \(P_1\) odd events, reuse the existing second-resonance machinery at \((A_2,Q_2)\), now with a logically valid bridge from the repaired first resonance.

## 7. Audit discipline

- The endpoint coefficient-survival input is taken only from the repaired first-resonance theorem already recorded on this branch.
- The phase-renewal identity is analytic and horizon-independent once the stated convergents are fixed.
- The companion script uses exact rational intervals for \(\ln2\) and \(\ln3\).
- The only external mathematical ingredient is the classical best-approximation property of continued-fraction convergents.
- No finite scan is promoted to an all-Collatz statement.

Companion certificate:

`collatz/src/first_resonance_phase_renewal_bridge_certificate.py`
