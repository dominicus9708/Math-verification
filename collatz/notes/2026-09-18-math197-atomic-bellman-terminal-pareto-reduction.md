# MATH-197 — atomic Bellman localization and terminal Pareto reduction

Date: 2026-09-18

Status: `EXACT STRUCTURAL LEMMA / ONE-STEP SAFE-OR-SINGLETON / TERMINAL INTEGER-DEFECT REDUCTION / FIRST-CELL OPEN`

## 1. Purpose

MATH-186 proves a macro-scale safe-or-singleton dichotomy for zero-cost prefixes followed by multi-paid clusters.

MATH-188--193 then reduce the synchronized product state to a common correction/source lineage and isolate the remaining singleton overshoot danger in exact dyadic residue/carry coordinates.

This note pushes the safe-or-singleton statement down to the **single parity-step level** and identifies an exact integer terminal defect coordinate. It also gives a rigorous Pareto dominance relation for singleton terminal states.

No paid layer, first universal Farey cell, or Collatz theorem is closed here.

## 2. Synchronized source interval

Use the MATH-190 common-origin state. At a given prefix, let the current ordinary-source parameter range be a consecutive integer interval

\[
s\in[L_s,U_s],
\qquad
M:=U_s-L_s+1\ge1,
\]

with resolution height

\[
\boxed{R:=\lceil\log_2 M\rceil},
\qquad R(1)=0.
\]

The current exact prefix has depth/count/correction coordinates

\[
(k,q,C).
\]

For a requested next parity bit \(b\), exact compatibility fixes one parity class of \(s\),

\[
s\equiv\eta\pmod2.
\]

After writing \(s=\eta+2t\), the surviving \(t\)-values again form one consecutive integer interval.

## 3. One parity bit consumes one unresolved source bit

Let \(M'\) be the child multiplicity.

A parity class contains at most half of a consecutive interval, rounded upward:

\[
\boxed{M'\le\left\lceil\frac M2\right\rceil.}
\]

If \(M\ge2\), then \(R\ge1\) and

\[
2^{R-1}<M\le2^R.
\]

Hence

\[
M'\le 2^{R-1},
\]

so every nonempty child obeys

\[
\boxed{R'\le R-1.}
\]

Thus in a synchronized exact source lineage every legal parity decision strictly lowers unresolved dyadic source resolution until the singleton regime is reached.

This is an atomic version of the MATH-074/MATH-186 resolution-consumption mechanism.

## 4. Atomic Bellman safe-or-singleton theorem

Inside the coefficient-valid region \(u\ge0\), MATH-187 gives the one-step penalty increment

\[
p_b
=
\frac b3(\Omega-\rho).
\]

Since

\[
\frac{\Omega}{\rho}=2^u,
\]

we have

\[
\boxed{p_b=\frac{b\rho}{3}(2^u-1)\ge0.}
\]

At \(u=0\) this is exactly zero; at a positive-slack paid odd step it is strictly positive.

Let \(\lambda>0\), and in particular later take the MATH-060 target

\[
\lambda=\frac{19}{503}.
\]

Use the resolution potential

\[
H_R=-\lambda R.
\]

For one shortcut step, the reduced-cost increment is

\[
\Delta\mathcal B
=
p_b-\lambda+H_{R'}-H_R
=
p_b-\lambda+\lambda(R-R').
\]

If \(M\ge2\), then \(R-R'\ge1\). Therefore

\[
\boxed{
\Delta\mathcal B\ge p_b\ge0.
}
\]

Consequently,

\[
\boxed{
\Delta\mathcal B<0
\Longrightarrow
R=0.
}
\]

So **every possible one-step Bellman deficit is already in the singleton regime**.

This statement is independent of the paid count \(r\). The paid count remains relevant to legal macro structure and accumulated positive surplus, but it is not needed to exclude negative reduced cost while source multiplicity exceeds one.

## 5. Exact integer terminal defect

MATH-190 gives

\[
S=\frac{C}{3^q},
\qquad
\rho=\frac{2^k}{3^q}.
\]

At a \(\rho>1\) self-comparison, the MATH-183 master defect is

\[
\mathfrak D(N)
=
S-N(\rho-1).
\]

Define

\[
\Delta_{k,q}:=2^k-3^q.
\]

Then

\[
\boxed{
\mathfrak D(N)
=
\frac{C-N\Delta_{k,q}}{3^q}.
}
\]

Therefore the sign of the terminal defect is exactly the sign of the integer

\[
\boxed{
J(k,q,C;N)
:=
C-N(2^k-3^q).
}
\]

The affine prefix identity

\[
2^kT^k(N)=3^qN+C
\]

gives the stronger interpretation

\[
\boxed{
J
=
2^k\bigl(T^k(N)-N\bigr).
}
\]

Thus

\[
\boxed{
J<0
\iff
T^k(N)<N,
}
\]

with no floating-point or phase approximation.

## 6. Exact one-step recurrence for the integer defect

MATH-190 gives

\[
C'=3^bC+b2^k,
\qquad
k'=k+1,
\qquad
q'=q+b.
\]

For fixed ordinary source \(N\), the defect coordinate obeys

\[
\boxed{
J'=
\begin{cases}
J-2^kN,&b=0,\\[3pt]
3J+2^k(N+1),&b=1.
\end{cases}
}
\]

This is algebraically exact.

It should not be mistaken for a monotone invariant: odd steps can increase \(J\). Its role is to remove all analytic ambiguity from terminal descent and to provide a deterministic singleton-tail coordinate.

## 7. Bellman penalty and terminal defect use the same correction coordinate

MATH-053/MATH-060 give

\[
S=S_\partial(q)-\mathcal P.
\]

Since \(S=C/3^q\),

\[
\boxed{
\mathcal P
=
S_\partial(q)-\frac{C}{3^q}.
}
\]

At fixed \((k,q)\), larger \(C\)

- lowers the accumulated penalty \(\mathcal P\), hence is worse for the Bellman lower bound;
- raises \(J=C-N\Delta_{k,q}\), hence is worse for terminal non-descent.

This produces an exact Pareto order.

## 8. Terminal Pareto dominance lemma

Assume \(\Delta_{k,q}>0\), i.e. \(\rho>1\).

Take two singleton states at the same \((k,q)\),

\[
(N_1,C_1),
\qquad
(N_2,C_2).
\]

If

\[
\boxed{
N_1\le N_2,
\qquad
C_1\ge C_2,
}
\]

then

\[
J_1-J_2
=
(C_1-C_2)
+
\Delta_{k,q}(N_2-N_1)
\ge0,
\]

so

\[
\boxed{J_1\ge J_2.}
\]

Also

\[
\mathcal P_1-\mathcal P_2
=
-\frac{C_1-C_2}{3^q}
\le0,
\]

so

\[
\boxed{\mathcal P_1\le\mathcal P_2.}
\]

Hence state 1 is simultaneously at least as dangerous for

1. insufficient paid-penalty accumulation, and
2. failure of terminal descent.

Therefore, within a fixed \((k,q)\) terminal comparison, any state dominated in the partial order

\[
N\text{ smaller},\quad C\text{ larger}
\]

may be removed from a Pareto safety search once its dominating state is retained.

This is a global Pareto statement; it does **not** assume or imply a unique local sink, so it does not revive the failed August unique-sink route.

## 9. Relation to MATH-192/193 singleton residue state

MATH-192 replaces an overshoot singleton source lookup by the exact residue \(r_L\), while MATH-193 factors danger into

\[
r_R\le r_{\rm bad},
\qquad
\nu_2(C_R)\ge z.
\]

Once a compatible singleton is identified, its ordinary source is exact. The present integer defect gives its terminal risk without any further analytic state:

\[
J=C-N(2^k-3^q).
\]

Thus the remaining singleton theorem may be organized as

1. **compatibility:** MATH-193 low/high residue/carry corridor;
2. **Hensel legality:** MATH-190/191 prefix predicate / forward viability;
3. **terminal descent:** the integer sign test \(J<0\);
4. **Pareto pruning:** retain only undominated \((N,C)\) states at fixed \((k,q)\).

## 10. Consequence for the r=1..21, depth=2..41 executor

The synchronized executor need not carry separate analytic Pareto coordinates \((S,\Sigma,\rho,\Omega,\mathcal P,\mathfrak D)\).

For proof logic, they are derived from

\[
\boxed{(k,q,C)}
\]

plus the exact source interval / singleton source.

While \(R\ge1\), atomic resolution consumption makes every legal one-step Bellman transfer safe.

At \(R=0\), the terminal risk is represented exactly by \(J\), and comparable singleton states admit the Pareto dominance rule above.

Therefore the difficult product-state region is localized to

\[
\boxed{
R=0
\quad+\quad
\text{Hensel-legal}
\quad+\quad
\text{MATH-193 compatible}
\quad+\quad
J\ge0.
}
\]

This is strictly smaller than the previous state-space description, but its global emptiness is not yet proved.

## 11. Claim boundary

Established:

- one parity decision reduces source resolution by at least one bit whenever \(M\ge2\);
- every coefficient-valid one-step Bellman deficit is therefore singleton-localized;
- exact integer terminal defect \(J=C-N(2^k-3^q)\);
- exact identity \(J=2^k(T^k(N)-N)\);
- exact one-step recurrence for \(J\);
- exact terminal Pareto dominance at fixed \((k,q)\);
- further reduction of the product proof state.

Not established:

- emptiness of all Hensel-legal MATH-193 singleton danger states;
- arbitrary-depth boundedness of the singleton Pareto frontier;
- closure of the first universal Farey cell;
- the Collatz conjecture.
