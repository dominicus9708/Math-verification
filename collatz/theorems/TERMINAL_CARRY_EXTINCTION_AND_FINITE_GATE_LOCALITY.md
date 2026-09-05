# Terminal carry extinction and finite-gate right-H locality

Status: **EXACT / CLOSED for terminal ternary residue locality**

## Setting

Use the exact backward exponential carry chart for a right-indexed sequence of one-event gates:

\[
z_i=3z_{i+1}-2^{A_i}+2^{B_i}.
\]

After `k` gates,

\[
z_0
=3^kz_k+
\sum_{i=0}^{k-1}3^i(2^{B_i}-2^{A_i})
\pmod{3^L}.
\]

The index `i=0` is the one-event nearest the observed/right terminal boundary in the current right-indexed chart; increasing `i` moves leftward/deeper into the right-H factor.

## Theorem 1 — terminal carry extinction

For every terminal precision `L>=1`, if

\[
k\ge L,
\]

then

\[
3^k z_k\equiv0\pmod{3^L}.
\]

Therefore

\[
\boxed{
z_0
\equiv
\sum_{i=0}^{L-1}3^i(2^{B_i}-2^{A_i})
\pmod{3^L}.
}
\]

All gates with index `i>=L`, and every carry/base state beyond the first `L` right-indexed gates, are invisible to the terminal residue modulo `3^L`.

## Theorem 2 — precision filtration

More generally, for every

\[
1\le\ell\le L,
\]

the residue

\[
z_0\pmod{3^\ell}
\]

depends only on the first `ell` right-indexed gate positions

\[
(B_0,\ldots,B_{\ell-1}).
\]

Indeed all terms with `i>=ell` contain a factor `3^ell`, and the surviving base-carry term is also divisible by `3^ell` after at least `ell` gates.

Hence the terminal residue has an exact nested filtration:

\[
(B_0)
\to z_0\bmod3,
\]

\[
(B_0,B_1)
\to z_0\bmod3^2,
\]

and in general

\[
(B_0,\ldots,B_{\ell-1})
\to z_0\bmod3^\ell.
\]

## Current checkpoint consequence

The synchronized checkpoint interface uses

\[
L=28.
\]

The current critical-cut right H block contains

\[
q_R=397{,}573{,}380
\]

one-events, far more than 28.

Therefore its complete 28-trit checkpoint observation is determined exactly by only the first 28 right-indexed one positions:

\[
\boxed{
z_H
\equiv
\sum_{i=0}^{27}3^i(2^{B_i}-2^{A_i})
\pmod{3^{28}}.
}
\]

No carry coordinate from the remaining

\[
397{,}573{,}352
\]

one-events can affect this 28-trit export.

The analogous exact localities are:

- 24-trit terminal predicate -> first 24 right-indexed one-events;
- 28-trit synchronized checkpoint predicate -> first 28 right-indexed one-events;
- 47-trit terminal predicate -> first 47 right-indexed one-events.

## Interaction with carry-base necessity

The earlier exponential-chart theorem correctly states that the successor carry/base cannot generally be discarded **while fewer than the queried number of gates have been absorbed**.

This theorem sharpens that scope:

- inside an unfinished `L`-gate terminal window, the active base carry remains observable and must be retained unless another theorem eliminates it;
- after `L` right-indexed gates, the unresolved deeper base is multiplied by `3^L` and becomes exactly invisible modulo `3^L`.

Thus there is no contradiction between base-carry necessity locally and terminal carry extinction after the full precision window.

## G2 consequence

For the synchronized checkpoint export, G2 no longer needs a state recursion across the entire `q_R=397,573,380`-one right-H factor.

The exact export problem is reduced to the finite ordered 28-gate domain

\[
0\le s_i\le D_i,
\qquad
s_{i+1}\le s_i,
\qquad
0\le i<28,
\]

with

\[
B_i=(q_R-i-1)+s_i.
\]

The remaining task is still nontrivial because this 28-dimensional ordered slack domain can contain many legal vectors and distinct exponential chart values. However, the huge deeper H grammar/carry tail is provably irrelevant to the 28-trit checkpoint export itself.

The preferred next state construction should therefore combine:

- this 28-gate terminal window;
- the high-precision prescribed-cylinder injectivity/singleton facts;
- max-slack feasibility only within its certified fixed-carry scope;
- one-dimensional `Pi3` quotients at fixed projective gates;
- the dyadic checkpoint-index/right-H isometry for the G2 -> G3 handoff.

## Scope restriction

This theorem proves **residue locality**, not formation completion.

It does not prove that an arbitrary 28-gate slack vector extends through the remaining right-H grammar.

It does not prove whole-path injectivity inside the 28-gate window.

It does not allow local carry-greedy selection.

It does not turn terminal residue agreement into full correction-language membership.

## DSD classification

### EXACT / CLOSED

- base carry extinction after `L` gates modulo `3^L`;
- `ell`-digit filtration by the first `ell` right-indexed gates;
- exact 24/28/47-gate locality for the current terminal predicates.

### OPEN

- compressed enumeration/quotient of the legal 28-gate ordered slack chart;
- proof that exported terminal states extend through every required formation predicate;
- synchronized source/checkpoint membership join.

## Certificate

- `../src/A0_s1_routeB_terminal_carry_extinction_certificate.py`

The certificate checks the symbolic divisibility identities and finite implementation examples; the theorem is the algebraic `3^L` extinction argument above.
