# MATH-213 — carry-valuation regeneration budget

Date: 2026-09-19

Status: \`EXACT POTENTIAL IDENTITY / CANCELLATION REGENERATION ISOLATED / r=10 OPEN\`

## 1. Purpose

MATH-204 shows that a dangerous singleton overshoot consumes low dyadic discrepancy bits.
MATH-205 gives the ordinary carry recurrence.
MATH-212 gives a growing lower bound on the total number of overshoot bits required by consecutive r=10 danger.

The missing issue is that a shift-add transition can regenerate low-zero bits by exact cancellation.

This note isolates that regeneration as one explicit additive budget.

## 2. Nonzero carry recurrence

Write one exact carry transition as

\[
\boxed{
d_{i+1}
=
\frac{3^{Q_i}d_i+c_i}{2^{z_{i+1}}},
}
\]

where

\[
c_i:=B_i-A_{i+1}.
\]

Assume in this section that

\[
d_i\ne0,\qquad d_{i+1}\ne0.
\]

Define

\[
v_i:=\nu_2(d_i)
\]

and

\[
w_i
:=
\nu_2(3^{Q_i}d_i+c_i).
\]

Exact compatibility gives

\[
w_i\ge z_{i+1}
\]

and division by \(2^{z_{i+1}}\) gives

\[
\boxed{
v_{i+1}=w_i-z_{i+1}.
}
\]

Hence

\[
\boxed{
z_{i+1}=w_i-v_{i+1}.
}
\]

## 3. Regeneration gain

Define the valuation-regeneration gain

\[
\boxed{
g_i:=w_i-v_i.
}
\]

Then

\[
\boxed{
z_{i+1}
=
v_i-v_{i+1}+g_i.
}
\]

Summing \(m\) consecutive nonzero-carry transitions gives the exact telescope

\[
\boxed{
\sum_{i=0}^{m-1}z_{i+1}
=
v_0-v_m
+
\sum_{i=0}^{m-1}g_i.
}
\]

Therefore all overshoot bits come from exactly two sources:

1. previously stored carry valuation;
2. newly regenerated valuation from addition cancellation.

No third source of dyadic compatibility exists.

## 4. When can positive regeneration occur?

Let

\[
s_i:=\nu_2(c_i)
\]

when \(c_i\ne0\).

Because \(3^{Q_i}\) is odd,

\[
\nu_2(3^{Q_i}d_i)=v_i.
\]

If

\[
s_i\ne v_i,
\]

the standard valuation law gives

\[
w_i=\min(s_i,v_i).
\]

Hence

\[
\boxed{
s_i\ne v_i
\Longrightarrow
g_i\le0.
}
\]

So **positive regeneration is possible only at an exact valuation match**

\[
\boxed{s_i=v_i.}
\]

Write then

\[
d_i=2^{v_i}u_i,
\qquad
c_i=2^{v_i}a_i,
\]

with \(u_i,a_i\) odd.

The gain is exactly

\[
\boxed{
g_i
=
\nu_2(3^{Q_i}u_i+a_i).
}
\]

Thus a positive gain of at least \(g\) bits requires the odd-part congruence

\[
\boxed{
3^{Q_i}u_i
\equiv
-a_i
\pmod{2^g}.
}
\]

This is a finite carry-residue condition.

## 5. Zero constant

If

\[
c_i=0,
\]

then

\[
w_i=v_i
\]

and therefore

\[
\boxed{g_i=0.}
\]

So an exact endpoint-to-source equality does not regenerate valuation in the nonzero carry itself; it only transports and consumes the valuation already present.

The separate zero-carry case \(d_i=0\) remains the MATH-204/206 reset branch and is not encoded by finite \(v_i\).

## 6. Combine with MATH-212

For \(m\) consecutive dangerous r=10 transfers, MATH-212 gives

\[
\sum_{i=1}^{m}z_i
\ge
Z_{\min}^{(10)}(m).
\]

Combining with the valuation telescope,

\[
v_0-v_m+\sum_{i=0}^{m-1}g_i
\ge
Z_{\min}^{(10)}(m).
\]

Therefore

\[
\boxed{
\sum_{i=0}^{m-1}g_i
\ge
Z_{\min}^{(10)}(m)-v_0+v_m.
}
\]

In particular,

\[
\boxed{
\sum_i g_i
\ge
Z_{\min}^{(10)}(m)-v_0.
}
\]

So once the initial stored valuation has been spent, every further dangerous r=10 chain must repeatedly create exact odd-part cancellations.

Examples:

\[
m=2:\quad
\sum g_i\ge27-v_0+v_2,
\]

\[
m=3:\quad
\sum g_i\ge42-v_0+v_3,
\]

\[
m=5:\quad
\sum g_i\ge72-v_0+v_5.
\]

## 7. Final quotient target

The r=10 hard core is therefore no longer an unrestricted integer carry.

For each transition it is enough to retain:

1. current carry valuation \(v_i\);
2. when \(v_i=\nu_2(c_i)\), the odd carry residue needed by
   \[
   3^{Q_i}u_i\equiv-a_i\pmod{2^g};
   \]
3. MATH-207/212 phase credit;
4. MATH-210 Hensel/Pareto extremality.

A transition with mismatched valuations has \(g_i\le0\) and cannot replenish the cumulative bit budget.

Thus the final structural closure problem is:

> prove that the reachable r=10 factor language cannot supply the positive regeneration budget demanded by MATH-212.

This is strictly smaller than enumerating ordinary source APs or depth ranges.

## 8. Claim boundary

Established:

- exact valuation telescope;
- exact regeneration gain;
- positive regeneration only at matched factor/carry valuation;
- exact odd-part congruence governing every positive gain;
- exact combination with MATH-212 cumulative r=10 thresholds.

Not established:

- a uniform upper bound on cumulative regeneration gain for every legal r=10 factor path;
- emptiness of the resulting carry quotient;
- r=10 closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
