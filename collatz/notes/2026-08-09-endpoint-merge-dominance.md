# Endpoint-merge status and finite-horizon correction — 2026-08-09

Status: **FAILED ROUTE (global endpoint dominance) + DERIVED LEMMA (finite-horizon cylinder dominance)**

This note corrects an earlier claim that same-depth states with a common endpoint could be globally quotient-ed by a simple `(r,q)` Pareto rule.

## 1. Exact state

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

use the canonical prefix state

\[
S=(k,q;r,y),
\qquad y=T^k(r),
\qquad 0\le r<2^k,
\]

where `q` is the number of odd parity entries in the first `k` steps.
For a requested next parity bit `b`, the unique canonical lift is

\[
r'=r+c2^k,
\qquad
c=b\oplus (y\bmod2),
\]

and before the next Collatz step the lifted endpoint is

\[
\widetilde y=y+c3^q.
\]

Thus the future canonical lift depends not only on the current endpoint parity but also on the multiplier `3^q` whenever `c=1`.

## 2. Retraction of the earlier global endpoint-dominance lemma

The earlier claim was:

> At a common depth and common endpoint `y`, if `r_1<=r_2` and `q_1>=q_2`, then state 1 dominates state 2 for every future continuation when computing the minimal-survivor function.

This is **false** for future canonical descendants.
The equality of endpoints only guarantees the same immediate lift bit.  After a lift with `c=1`, the two lifted endpoints differ by `3^{q_1}-3^{q_2}`, so later carry bits can diverge.

### Exact counterexample

At depth

\[
k=10
\]

there are coefficient-surviving states

\[
S_1=(10,8;127,820),
\qquad
S_2=(10,7;383,820).
\]

They satisfy

\[
127<383,
\qquad 8>7,
\qquad y_1=y_2=820.
\]

Nevertheless, over five additional coefficient-surviving steps, exhaustive exact enumeration gives

\[
\min r_{15}(S_1)=2175
\]

attained with suffix `01101`, while

\[
\min r_{15}(S_2)=1407
\]

attained with suffix `11111`.
Therefore

\[
\boxed{2175>1407},
\]

so the supposedly dominated state produces the smaller depth-15 descendant.

This counterexample was obtained by an arbitrary-precision integer search and independently reproduced in Wolfram Language.

Consequently, the previous same-endpoint quotient counts remain useful as a **collision diagnostic**, but their Pareto deletion rule is not an exact global pruning theorem.

## 3. Safe replacement: finite-horizon cylinder dominance

Fix a target depth

\[
K=k+m.
\]

Consider two coefficient-surviving states at depth `k` with the same odd count `q`:

\[
S_i=(k,q;r_i,y_i).
\]

Assume

\[
\boxed{y_1\equiv y_2\pmod{2^m}}
\]

and

\[
\boxed{r_1\le r_2}.
\]

Then state 1 dominates state 2 **for this fixed remaining horizon `m`**.

### Proof

Take any common requested future parity suffix

\[
b_0,b_1,\ldots,b_{m-1}.
\]

At the first future step, `y_1` and `y_2` have the same parity, hence the same lift bit

\[
c_0=b_0\oplus(y_i\bmod2).
\]

Because the odd counts are equal, both states add the same quantity `c_0 3^q` before the next map step.  Their lifted endpoint difference is still divisible by `2^m`.
After division by two, with an optional multiplication by three on the odd branch, the new endpoint difference is divisible by `2^{m-1}`.
The new odd counts also remain equal.

Inductively, the two states have identical lift bits

\[
c_0,c_1,\ldots,c_{m-1}
\]

for the whole common suffix.  Therefore the canonical-start increment is identical:

\[
\Delta r
=
\sum_{j=0}^{m-1}c_j2^{k+j}.
\]

Hence

\[
r_1+\Delta r\le r_2+\Delta r.
\]

The coefficient barrier at every future prefix depends only on the depth and the accumulated odd count, which are the same for the two states under the common suffix.  Thus a suffix is coefficient-admissible for one state iff it is admissible for the other.
This proves the finite-horizon dominance.

## 4. Slightly stronger cross-q form

The same induction works for two states with `q_1>=q_2` if, in addition to endpoint congruence,

\[
\boxed{3^{q_1}\equiv3^{q_2}\pmod{2^m}}.
\]

Then every common suffix generates the same lift bits through horizon `m`, while state 1 has at least as many accumulated odd steps at every future depth.  Thus, if also `r_1<=r_2`, state 1 dominates state 2 for target depth `K=k+m`.

For `m>=3`, the multiplicative order of `3 mod 2^m` is `2^{m-2}`, so the power congruence is equivalent to

\[
q_1\equiv q_2\pmod{2^{m-2}}.
\]

This cross-q extension is mainly useful near the terminal end of a fixed-horizon computation, where `m` is small.

## 5. Exact target-specific quotient

For the simpler same-q version, at depth `k` in a computation targeted at `K`, it is safe to group states by

\[
\boxed{
\left(q,\ y\bmod2^{K-k}\right)
}
\]

and retain only the smallest canonical start `r` in each group.

This quotient is **target dependent**.  As `k` increases, the required endpoint modulus shrinks by one bit per step.
It is not a global quotient valid for all future horizons at once.

The stronger cross-q form groups by

\[
\boxed{
\left(y\bmod2^m,\ 3^q\bmod2^m\right)
}
\]

and keeps the `(r,q)` Pareto frontier: a state can be removed when another state in the same signature has no larger `r` and no smaller `q`.

## 6. Min-plus interpretation

The canonical start at depth `K` is

\[
r_K=\sum_{j=0}^{K-1}c_j2^j.
\]

Thus the exact minimal-survivor search is a min-plus shortest-path problem with edge cost

\[
c_j2^j.
\]

For a remaining horizon `m`, the finite carry state can be written as

\[
\eta=y\bmod2^m,
\qquad
g=3^q\bmod2^m.
\]

For requested parity `b`, let

\[
c=b\oplus(\eta\bmod2).
\]

After one step the modulus drops to `2^{m-1}` and

\[
\eta'=
\begin{cases}
(\eta+cg)/2,&b=0,\\[2mm]
(3(\eta+cg)+1)/2,&b=1,
\end{cases}
\pmod{2^{m-1}},
\]

while

\[
g'=
\begin{cases}
g,&b=0,\\3g,&b=1,
\end{cases}
\pmod{2^{m-1}}.
\]

This gives a rigorous finite-horizon block transfer / min-plus matrix formulation of the E/O-channel model.

## 7. Independent checks

Two independent exact checks were performed:

1. Python arbitrary-precision enumeration found the depth-10 / horizon-5 counterexample above and exhaustively tested the finite-horizon signature on small depths;
2. Wolfram Language independently reproduced
   `2175` versus `1407` for the counterexample and found no failure of the finite-horizon signature in its small-depth exhaustive test.

The finite computations support the algebraic proof but are not used in place of it.

## 8. Relation to known 2-adic structure

The fact that a length-`m` future parity block is controlled by a residue modulo `2^m` is consistent with the classical parity-vector / 2-adic conjugacy theory of Terras and Bernstein--Lagarias.  The contribution of this note is not a new parity-vector theorem; it is the explicit **min-plus dominance rule** for the current canonical-residue search state.

## 9. Consequence for the proof program

The exact state hierarchy is now

\[
\boxed{
(k,q)
\longrightarrow
s
\longrightarrow
(\eta,g)
\longrightarrow
r,
}
\]

with `s` derived from `(k,q)` and `eta,g` containing only the low-bit carry information required by the chosen remaining horizon.

Safe future work may contract the full endpoint `y` to this finite-horizon signature.  It may not contract merely by endpoint equality, slack, or the smallest residue in a slack layer.
