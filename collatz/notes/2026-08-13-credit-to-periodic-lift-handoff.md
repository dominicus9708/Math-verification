# Predecessor-credit / periodic-lift handoff at a Euclidean macroblock

Date: 2026-08-13

Status: **exact valuation dichotomy + finite type-17 handoff certificate**. This connects failure of an integer predecessor collision to the rational high-lift channel. It does not prove Collatz.

## 1. Cross-block correction difference

Let a left macroblock `U` have length `L_U` and odd count `q_U`. Let a right macroblock already contain two orientations whose correction difference is

\[
D_V=3^{q_V}\delta,
\]

so `delta` is an integer predecessor credit on the right.

For two left orientations with correction difference `D_U`, the full concatenation difference is

\[
\boxed{
D
=3^{q_V}
\left(D_U+2^{L_U}\delta\right).
}
\]

Put

\[
X:=D_U+2^{L_U}\delta.
\]

## 2. Valuation dichotomy

Let

\[
s=v_3(X).
\]

If

\[
s\ge q_U,
\]

then

\[
3^{q_U+q_V}\mid D
\]

and the full alternate predecessor shift is the ordinary integer

\[
\boxed{
\Delta=\frac{X}{3^{q_U}}.
}
\]

This is the integer-credit channel.

If instead

\[
s<q_U,
\]

write

\[
X=3^s a,
\qquad 3\nmid a.
\]

Then the normalized full predecessor displacement is the reduced rational

\[
\boxed{
\frac{D}{3^{q_U+q_V}}
=\frac{a}{3^{q_U-s}}.
}
\]

Thus failure of full integerization does not erase the arithmetic information: it produces an exact odd 3-power denominator.

## 3. High-lift consequence

For reduced denominator

\[
3^d,
\qquad d=q_U-s>0,
\]

the high-resolution dyadic residue of the rational displacement follows the deterministic inverse-two orbit modulo `3^d`.

Its period is

\[
\boxed{
\operatorname{ord}_{3^d}(2)
=2\cdot3^{d-1}.
}
\]

Across one complete period the newly exposed high binary digits contain exactly half zeros and half ones.

Therefore every cross-block state has the exact alternative:

\[
\boxed{
\text{integer predecessor credit}
\quad\text{or}\quad
\text{periodic nonzero late-lift obligation}.
}
\]

The two channels are selected by the 3-adic valuation of the same correction numerator `X`.

## 4. Finite reachable-context diagnostic

Starting from the certified length-92 context with incoming credit

\[
\delta=30,
\]

a finite backward context calculation in 19-bit Sturmian factors shows:

- the first 100 predecessor blocks have 25 possible phase branches;
- every branch reaches the same integer credit
  \[
  \boxed{148};
  \]
- the growth occurs through long plateaus and phase-wrap jumps, not monotone block-by-block increase.

Extending to 500 predecessor blocks gives 118 phase branches. Every branch loses the full integer-credit congruence at the same local state:

\[
\boxed{
\text{factor type }17
=1101101011011010110,
\qquad
\delta=148.
}
\]

The first failure occurs at predecessor-block index `121` or `122` depending on phase.

This is a finite diagnostic of the factor-context model; it is not yet a rigorous infinite substitution theorem.

## 5. Exact type-17 valuation handoff

The type-17 factor has

\[
L_U=19,
\qquad
q_U=12.
\]

Its neutral survival fibre contains `3387` orientations.

For incoming credit

\[
\delta=148,
\]

there is no pair satisfying the full congruence modulo

\[
3^{12}.
\]

However there are pairs satisfying it modulo

\[
3^{11}.
\]

The maximum possible 3-adic valuation of

\[
D_U+2^{19}\cdot148
\]

is therefore exactly

\[
\boxed{s=11.}
\]

One extremal positive numerator is

\[
\boxed{
D_U+2^{19}\cdot148
=77,944,680
=440\cdot3^{11}.
}
\]

Since `q_U=12`, the reduced alternate-predecessor displacement is

\[
\boxed{\frac{440}{3}.}
\]

Thus the failed integer-credit channel hands off to the smallest possible nontrivial 3-adic denominator:

\[
\boxed{d=1.}
\]

## 6. Period-two late-lift obligation

For denominator `3`,

\[
\operatorname{ord}_3(2)=2.
\]

Hence after the finite numerator-dependent low-bit transient, the high-resolution binary displacement has a period-two tail with one `1` in every two positions.

This is the strongest simple periodic-lift obligation available from an odd 3-power denominator: the high-lift density is exactly `1/2` with the shortest nontrivial period.

## 7. Proof-program consequence

A scalar predecessor-credit potential alone is not monotone: it can plateau and can cease to integerize.

The correct multichannel state should instead retain at least

\[
\boxed{
(\Delta_{\rm int},\ d_{3},\ \text{return-word type/phase})
}
\]

where

- `Delta_int` records the best ordinary predecessor credit when `d_3=0`;
- `d_3=q_U-v_3(X)` records the residual rational denominator exponent when full integerization fails;
- the return-word type determines the next correction-difference options.

The next target is a lexicographic/well-founded progress theorem:

> along every critical-return context, either an integer predecessor credit eventually exceeds the available orbit headroom, or the residual denominator channel forces a late canonical lift incompatible with the eventually-zero binary expansion of an ordinary start.

The type-17 `148 -> 440/3` handoff is the first explicit finite instance where the two channels meet at exactly the same obstruction point.