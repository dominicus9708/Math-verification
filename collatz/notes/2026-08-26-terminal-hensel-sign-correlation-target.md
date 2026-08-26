# First resonance: zero-target terminal Hensel lift and weighted sign-correlation target

Date: 2026-08-26

Status: **exact structural lemma + exact first-resonance arithmetic threshold.** The terminal-sign lemma is unconditional inside the repaired first-global-resonance binary branch. The final correlation bound identified below is a new target, not yet proved. This document does not prove the Collatz conjecture.

## 1. Terminal state

For the repaired first resonance

\[
(A,Q)=(114208327604,72057431991),
\]

let a terminal window contain the last \(m\) odd ordinals. Write its mechanical positions as

\[
B_t=b_{Q-m+1+t},\qquad
b_j=\lfloor (j-1)\log_2 3\rfloor,
\]

and displacement

\[
\delta_t=B_t-a_{Q-m+1+t}\ge0.
\]

The normalized terminal endpoint residue is

\[
Y_m(\delta)=
2^{-A}\sum_{t=0}^{m-1}3^{m-1-t}2^{B_t-\delta_t}.
\]

For an admissible endpoint \(y<3^{46}\), the terminal congruence is

\[
Y_m(\delta)\equiv y\pmod{3^m}.
\]

For \(m\ge46\), the higher ternary digits of the ordinary integer endpoint are zero. This turns every further left extension into a zero-target Hensel lift.

## 2. One-class Hensel lift lemma

Evaluate the old terminal sum one ternary digit deeper and define

\[
c_m
:=
\frac{Y_m(\delta)-y}{3^m}\pmod3.
\]

When one earlier odd ordinal is prepended, let its mechanical position be

\[
\widehat B_0=b_{Q-m}
\]

and its new displacement be \(d\ge0\). The old displacement vector shifts one coordinate to the right.

Modulo \(3^{m+1}\), the new endpoint condition is exactly

\[
\boxed{
c_m+2^{\widehat B_0-A-d}\equiv0\pmod3.
}
\]

Since every power of two modulo three is \(\pm1\), there are only three cases:

- \(c_m=0\): no lift exists for any \(d\);
- \(c_m=1\): exactly one parity class of \(d\) works;
- \(c_m=2\): exactly the opposite parity class works.

Thus a terminal Hensel state has **at most one displacement-parity child class** at the next ternary digit.

The ordering constraint is independent:

\[
\delta_1\le d+(\widehat B_1-\widehat B_0)-1.
\]

Therefore a support-preserving lift with \(d=0\) exists only when both the Hensel parity and this ordering inequality allow it. Otherwise every successful lift adds a new terminal defect.

This explains why the low-support terminal enumeration repeatedly collapses rather than branching arbitrarily.

## 3. Balanced-sign interpretation

Identify the nonzero residue classes modulo three with signs \(\{+1,-1\}\). The Hensel condition chooses a required sign

\[
\varepsilon_m\in\{+1,-1\}.
\]

The mechanical prepend has sign

\[
\sigma_m=(-1)^{\widehat B_0-A}.
\]

If

\[
\varepsilon_m\ne\sigma_m,
\]

then the new displacement must be odd and therefore positive. Hence a sign mismatch forces a new defect.

This gives a deterministic lower bound on the normalized correction defect. For odd ordinal \(j\), define

\[
c_j:=\frac{2^{b_j-1}}{3^j}.
\]

Any odd displacement \(d_j\ge1\) has normalized correction cost

\[
\frac{2^{b_j}-2^{b_j-d_j}}{3^j}\ge c_j.
\]

Therefore, over any terminal extension range,

\[
\boxed{
\frac{E}{3^Q}
\ge
\sum_j c_j\,\mathbf 1_{\{\varepsilon_j\ne\sigma_j\}}.
}
\]

Ordering can create additional even positive displacements, so the right-hand side is only a lower bound; this is favorable for exclusion.

## 4. Mechanical single-step mass

For the first-resonance Farey cell,

\[
b_j=\lfloor(j-1)\log_2 3\rfloor
\]

through the full relevant ordinal range. Hence

\[
c_j
=\frac16\,2^{-\{(j-1)\log_2 3\}}.
\]

The Farey permutation argument gives

\[
\sum_{j=1}^{Q}c_j
>
\frac{Q}{12\ln2}.
\]

Discarding the final 46 terms loses at most \(46/6\), so for the long zero-target extension range

\[
\boxed{
C_{\rm pre}
:=\sum_{j=1}^{Q-46}c_j
>
\frac{Q}{12\ln2}-\frac{46}{6}.
}
\]

The companion exact-rational certificate gives the numerical lower bound

\[
C_{\rm pre}>8,663,074,975.05\ldots.
\]

## 5. The 50-percent threshold

The already-certified first-resonance defect budget is

\[
\boxed{E/3^Q<4,314,000,000.}
\]

But

\[
\boxed{
\frac12 C_{\rm pre}
>4,331,537,487.52\ldots
>4,314,000,000.
}
\]

The margin is more than

\[
\boxed{17,500,000.}
\]

Therefore the first resonance is impossible as soon as one proves the weighted mismatch inequality

\[
\boxed{
\sum_{j=1}^{Q-46}
c_j\,\mathbf1_{\{\varepsilon_j\ne\sigma_j\}}
\ge\frac12 C_{\rm pre}.
}
\]

Equivalently, define the weighted sign correlation

\[
\mathcal C
:=
\sum_{j=1}^{Q-46}c_j\varepsilon_j\sigma_j.
\]

Since

\[
M=\frac{C_{\rm pre}-\mathcal C}{2},
\]

a surviving candidate would require

\[
\boxed{
\mathcal C
>
C_{\rm pre}-2(4,314,000,000)
>35,000,000.
}
\]

Thus the actual unresolved analytic target is much smaller than a multi-billion support-count theorem:

> **Terminal weighted sign-correlation theorem.** Rule out a positive weighted Hensel/mechanical sign bias larger than about \(0.4049\%\) of the total single-step mass.

A nonpositive correlation bound would be far stronger than necessary; even an explicit \(0.4\%\)-scale correlation estimate would close the repaired first resonance.

## 6. Relation to the existing low-support ladder

The finite terminal ladder

\[
D_{\rm tail}(66)\ge11
\]

and the computed exact \(m=66\) support-11 split are finite manifestations of the same Hensel sign process. The surviving support-11 state

\[
\operatorname{supp}(\delta)
=(2,12,13,22,23,24,48,49,50,51,55)
\]

with

\[
(\delta_{24},\delta_{49})=(2,2)
\]

has endpoint

\[
y=2620472197936414017727.
\]

At the \(m=66\to67\) lift the required parity is even, so a mechanical prepend survives. At the \(m=67\to68\) lift the required parity is odd, so support 11 cannot persist; an explicit support-12 lift uses new displacement one.

The separate exhaustive support-11 split remains the finite computational input for claiming that no other support-11 state survives this stage. The one-class Hensel lemma itself does not depend on that enumeration.

## 7. DSD audit interpretation

This is a genuine reduction of descriptors rather than a new assumption.

The previous terminal picture tracked

\[
\text{support positions},\quad
\text{displacement sizes},\quad
\text{endpoint residue},\quad
\text{correction cost}
\]

as partially separate objects.

The zero-target Hensel chain shows that their next-step interaction is organized by one ternary carry class:

\[
\boxed{
\text{Hensel carry}
\to
\text{required sign/parity}
\to
\text{mechanical mismatch}
\to
\text{forced defect cost}.
}
\]

DSD is used here as proof-chain bookkeeping. Every displayed implication above is an ordinary modular-arithmetic statement and can be verified without accepting DSD as an axiom system.

## 8. Next proof target

Do not continue raising the terminal support lower bound one unit at a time as the main route.

The higher-leverage target is now the weighted correlation

\[
\mathcal C
=
\sum c_j\varepsilon_j\sigma_j.
\]

The natural next tasks are:

1. write the Hensel signs as the carry sequence of the nested dyadic-resolution tower;
2. write \(\sigma_j\) as the parity coding of the first-resonance Beatty/Sturmian mechanical word;
3. seek cancellation of their weighted correlation, using the exact Farey permutation already available at this resonance;
4. retain the terminal low-support ladder as a finite calibration and regression suite, not as the asymptotic engine.

Companion certificate:

`collatz/src/first_resonance_terminal_hensel_sign_threshold_certificate.py`.
