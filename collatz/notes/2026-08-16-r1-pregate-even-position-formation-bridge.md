# R1 pre-G13 even-position formation bridge

Date: 2026-08-16

Status: **exact affine formation/composition theorem + candidate-specific natural-G13 attachment exclusion**. This note replaces a large sparse parity-word layer by a short root interval attached to each G13 entrance. It does **not** close the complete `E=13` G13-natural section and does not prove Collatz.

## 1. Motivation

The current exact R1 entrance theorem gives

\[
e_{1539}\ge 13,\qquad
x_{1539}<2^{952}.
\]

The next blind finite route would treat `E=13` by enumerating first-73 parity words with at most nine zeros. The raw nine-zero layer has

\[
\binom{73}{9}=97,082,021,465
\]

words.

That is the wrong proof object for the intended proposition/set/formation architecture. The correct object is the **ordered set of even-event positions**, composed into one exact affine correction.

## 2. The \(U=x+1\) formation law

For the accelerated Collatz map, put

\[
U=x+1.
\]

Then one step is

\[
U\mapsto \frac{3U}{2}
\]

on an odd state, and

\[
U\mapsto \frac{U+1}{2}
\]

on an even state.

Consider `T` accelerated steps and suppose exactly `E` of them are even events, at positions

\[
0\le p_0<p_1<\cdots<p_{E-1}<T.
\]

Let

\[
q=T-E.
\]

Before the `j`-th even event there are exactly

\[
p_j-j
\]

odd events. Therefore direct affine composition gives

\[
2^T U_T
=
3^q U_0
+
\sum_{j=0}^{E-1}
2^{p_j}3^{q-(p_j-j)}.
\]

After division by \(3^q\),

\[
\boxed{
\frac{2^T U_T}{3^q}
=
U_0+
\sum_{j=0}^{E-1}
3^j\left(\frac23\right)^{p_j}.
}
\]

Define the formation correction

\[
\boxed{
\varepsilon_E(p_0,\ldots,p_{E-1})
:=
\sum_{j=0}^{E-1}
3^j\left(\frac23\right)^{p_j}.
}
\]

The full time-expanded parity word is no longer the primary object. All pre-gate additive information is compressed into the ordered event-position set.

## 3. Current-core prefix bound

Every current `m=44` start obeys

\[
N\equiv3\pmod4.
\]

Write \(N=4k+3\). Its first accelerated step is odd, and

\[
T(N)=\frac{3N+1}{2}=6k+5,
\]

which is also odd.

Hence the first two accelerated parity symbols are always

\[
11.
\]

Therefore the ordered even-event positions satisfy

\[
\boxed{p_j\ge j+2.}
\]

Since \(0<2/3<1\),

\[
\varepsilon_E
\le
\sum_{j=0}^{E-1}
3^j\left(\frac23\right)^{j+2}
=
\frac49\sum_{j=0}^{E-1}2^j.
\]

Thus

\[
\boxed{
0<\varepsilon_E
\le
\frac49(2^E-1).
}
\]

This bound is sharp at the level of the prefix constraint: equality is attained by the event positions

\[
p_j=j+2.
\]

## 4. Fixed G13 entrance gives a short root interval

Now specialize to the current pre-gate length

\[
T=1539
\]

and write

\[
X=x_{1539}.
\]

For a fixed total even count `E`, define

\[
Y_E(X)
:=
\frac{2^{1539}(X+1)}{3^{1539-E}}.
\]

The formation identity gives

\[
N+1
=
Y_E(X)-\varepsilon_E.
\]

Hence every compatible ordinary root lies in

\[
\boxed{
Y_E(X)-1-\frac49(2^E-1)
\le N
<
Y_E(X)-1.
}
\]

The width depends only on `E`, not on 1539-bit parity-word enumeration.

### \(E=13\)

\[
\varepsilon_{13}
\le
\frac{32764}{9}
=
3640+\frac49.
\]

Therefore a fixed G13 entrance \(X\) has at most

\[
\boxed{3641}
\]

ordinary integer roots compatible with `E=13`.

This replaces the raw first-73 nine-zero search scale

\[
97,082,021,465
\]

by a root interval of at most 3641 integers **per actual G13 entrance state**.

Because every current-core root is \(3\bmod4\), even this short interval contains at most 911 congruence-compatible integers before the ternary-digit test.

### \(E=14\)

Likewise

\[
\varepsilon_{14}
\le
\frac{21844}{3}
=
7281+\frac13,
\]

so there are at most

\[
\boxed{7282}
\]

ordinary integer roots for a fixed entrance.

## 5. High-prefix factorization for \(E=13\)

The current entrance bound is

\[
X<2^{952}.
\]

For `E=13`, write

\[
X+1=h2^{879}+\ell,
\qquad
0\le\ell<2^{879}.
\]

Then

\[
Y_{13}(X)
=
\frac{2^{1539}(X+1)}{3^{1526}}
=
\lambda h+\eta,
\]

where

\[
\boxed{
\lambda=\frac{2^{2418}}{3^{1526}},
}
\]

and

\[
0\le\eta<\lambda.
\]

Exact integer comparison gives

\[
2^{2418}<3^{1526},
\]

hence

\[
\boxed{\lambda<1.}
\]

Therefore all lower 879 bits of the G13 entrance move the normalized pre-gate root coordinate by **less than one**.

Equivalently, once the top prefix

\[
h=\left\lfloor\frac{X+1}{2^{879}}\right\rfloor
\]

is fixed, every possible `E=13` current root is confined to an interval of width

\[
\frac{32764}{9}+\lambda
<
3642.
\]

Thus the exact product-state target can be split into

\[
\boxed{
\text{G13 high 73-bit entrance prefix}
\times
\text{low natural-lift state}
\times
\text{current ternary core}.
}
\]

The lower 879 entrance bits contribute only a sub-unit carry to the root coordinate.

## 6. Re-exclusion of the known finite-natural sample

The previously found ordinary finite-natural G13 sample is

\[
\begin{aligned}
X_0={}&9311066934133191055179217771751644756458780835642375520644606697570370834878851085876330120952372828601875854086643506229770877868471756436379730259097164274868063513702695410370082518062231340901656195848133042167901156081765468572447679246085622583924868464925000059470402523777450879.
\end{aligned}
\]

For `E=13`, the exact root interval is

\[
[1469359527463825158996,\,
1469359527463825162635],
\]

which lies entirely below the current R1 numerical interval. Therefore `E=13` is impossible for this entrance immediately.

For `E=14`, the exact root interval is

\[
\boxed{
[4408078582391475480628,\,
4408078582391475487909].
}
\]

It contains exactly

\[
\boxed{7282}
\]

ordinary integers.

Testing only the defining `m=44` ternary formation condition inside this tiny interval gives

\[
\boxed{0}
\]

current-core members.

Hence the known natural G13 candidate is excluded from the current R1 core without constructing its 1539-step reverse parity tree:

\[
\boxed{
X_0\not\leftarrow F_{44}^{\rm current}
\quad\text{for }E=14.
}
\]

This independently reproduces the earlier candidate-specific reverse-tree exclusion by a stronger set-level attachment test.

## 7. Structural interpretation

The new bridge changes the proof object from

\[
\text{one parity word}
\]

to

\[
\text{one event-position formation class}.
\]

The chain is now

\[
\boxed{
\text{even-event set}
\Longrightarrow
\varepsilon_E\text{ interval}
\Longrightarrow
\text{short ordinary-root set}
\Longrightarrow
\text{ternary-core subtraction}.
}
\]

For the next unresolved layer the intended global target is therefore

\[
\boxed{
\mathcal G_{\rm nat}^{(952)}
\cap
\mathcal P_{E=13}
\cap
F_{44}^{\rm current}
=
\varnothing,
}
\]

but \(\mathcal P_{E=13}\) should now be represented by the short root windows above, not by the \(97\) billion first-73 words.

## 8. Next exact target

The next implementation should make the G13 natural transducer expose the high prefix

\[
h=\left\lfloor(X+1)/2^{879}\right\rfloor
\]

while retaining only the low state needed for the same-word/credit relation.

For each reachable high-prefix state, attach the interval

\[
\left[
\lambda h-1-\frac{32764}{9},
\,
\lambda(h+1)-1
\right)
\]

to the current `m=44` ternary core.

A prefix state can be deleted as a whole whenever this interval has no current-core member.

This is a direct formation-composition subtraction rule: an entire family of G13 states is removed by one set-intersection proposition, with no enumeration of the corresponding 1539-step parity histories.

## Reproducibility

Exact certificate:

`collatz/src/r1_pregate_even_position_formation_bridge_certificate.py`

Related prior certificates:

- `collatz/src/r1_g13_entry_952bit_bound_certificate.py`
- `collatz/src/g13_natural_cut_reverse_sameword_certificate.cpp`
- `collatz/src/g13_h1_4096_to_1_bridge_certificate.cpp`
