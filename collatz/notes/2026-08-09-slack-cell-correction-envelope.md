# Exact correction envelope inside a coefficient-surviving E/O cell

Date: 2026-08-09

Status: **DERIVED LEMMA + EXHAUSTIVE SMALL CROSS-CHECK**

This note sharpens the affine correction bound inside a fixed E/O count cell by imposing the full coefficient-survival prefix constraint.

## 1. Setup

Let a length-`h` accelerated parity word contain `q` odd steps and `e=h-q` even steps. Assume it survives coefficient contraction through depth `h`:

\[
3^{q_j}\ge2^j
\qquad(1\le j\le h).
\]

Let its zero-based odd positions be

\[
0\le d_0<d_1<\cdots<d_{q-1}<h.
\]

The affine iterate is

\[
T^h(n)=\frac{3^q n+R}{2^h},
\]

with

\[
\boxed{
R(d)=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
}
\]

## 2. Prefix-survival bound on every odd position

Immediately before the `(i+1)`-st odd step, the prefix length is `d_i` and only `i` odd steps have already occurred. Coefficient survival up to that point requires

\[
3^i\ge2^{d_i}.
\]

Therefore

\[
\boxed{
d_i\le\lfloor i\log_2 3\rfloor.}
\]

This bound is independent of the final cell length `h`.

There is also a purely combinatorial room constraint. After position `d_i`, the remaining `q-i-1` odd steps must fit into the last `h-d_i-1` positions, so

\[
\boxed{
d_i\le h-q+i.}
\]

Hence every coefficient-surviving word in the fixed `(h,q)` cell satisfies

\[
\boxed{
d_i\le d_i^*(h,q)
:=\min\!\left(
\lfloor i\log_2 3\rfloor,
\ h-q+i
\right).}
\]

## 3. The coordinatewise maximum vector is feasible

The two integer sequences

\[
A_i=\lfloor i\log_2 3\rfloor,
\qquad
C_i=h-q+i
\]

both increase by at least one at every step. Therefore

\[
\min(A_{i+1},C_{i+1})
\ge
\min(A_i,C_i)+1.
\]

Thus

\[
d_0^*<d_1^*<\cdots<d_{q-1}^*.
\]

The vector `d*` satisfies both the survival-position bound and the room bound. Since the cell itself is coefficient-surviving at its endpoint,

\[
3^q\ge2^h,
\]

the possible trailing even segment after the last odd step is also safe. Hence `d*` is an admissible parity word in the cell.

## 4. Exact correction maximum

Every coefficient of `2^{d_i}` in `R(d)` is positive. Therefore `R` is strictly increasing in every coordinate `d_i` while the remaining positions are fixed.

Since every admissible vector obeys

\[
d_i\le d_i^*,
\]

the feasible vector `d*` simultaneously maximizes all coordinates. Hence

\[
\boxed{
R_{\max}^{\rm surv}(h,q)
=
\sum_{i=0}^{q-1}
2^{\min(\lfloor i\log_2 3\rfloor,\,h-q+i)}
3^{q-1-i}.
}
\]

The maximizer is unique at the level of the odd-position vector.

The minimum remains the all-odd-first word

\[
d_i=i,
\]

which is admissible whenever the final cell is coefficient-surviving. Thus

\[
\boxed{
R_{\min}^{\rm surv}(h,q)=3^q-2^q.
}
\]

Therefore the full prefix-constrained cell envelope is

\[
\boxed{
3^q-2^q
\le R\le
R_{\max}^{\rm surv}(h,q).
}
\]

This is sharper than the order-unconstrained fixed-count maximum

\[
2^{h-q}(3^q-2^q),
\]

because the latter allows late odd positions that violate earlier coefficient survival.

## 5. Structure of the maximizing path

The maximum position formula has two regimes:

\[
d_i^*=\lfloor i\log_2 3\rfloor
\]

when the coefficient barrier is active, and

\[
d_i^*=h-q+i
\]

when the finite-length room constraint is active.

Thus the extremal word is naturally interpreted as

1. a mechanical-boundary prefix that delays each required odd step as far as coefficient survival permits;
2. followed, when the cell has excess odd slack, by a packed odd tail forced by the requirement to fit all `q` odd steps into length `h`.

This gives a precise cell-level version of the E/O-plane plus slack picture.

## 6. Small exhaustive Wolfram check

All coefficient-surviving `(h,q)` cells with `1<=h<=10` were exhaustively enumerated in Wolfram. For every nonempty cell:

- the vector `d*(h,q)` was present in the admissible set;
- its exact `R` equaled the enumerated maximum.

Selected rows are:

| h | q | surviving words | exact max R |
|---:|---:|---:|---:|
| 4 | 3 | 2 | 23 |
| 5 | 4 | 3 | 85 |
| 6 | 5 | 4 | 287 |
| 7 | 5 | 7 | 319 |
| 8 | 6 | 12 | 1085 |
| 9 | 7 | 18 | 3511 |
| 10 | 7 | 30 | 3767 |
| 10 | 8 | 25 | 11045 |
| 10 | 9 | 8 | 27407 |

The exhaustive computation is a cross-check; the formula follows from the coordinatewise proof above.

## 7. Endpoint magnitude envelope

For a canonical start `r`, the depth-`h` endpoint satisfies

\[
2^h y=3^q r+R.
\]

Using the exact cell envelope gives

\[
\boxed{
y
\le
\frac{3^q r+R_{\max}^{\rm surv}(h,q)}{2^h}.}
\]

A coarser but simple universal bound follows from

\[
2^{d_i}\le3^i.
\]

Each correction summand is then at most `3^(q-1)`, hence

\[
\boxed{R\le q3^{q-1}.}
\]

If

\[
q=a_h+s,
\qquad a_h=\lceil h\log_3 2\rceil,
\]

then

\[
1\le\frac{3^{a_h}}{2^h}<3,
\]

so

\[
\frac{3^q}{2^h}<3^{s+1}.
\]

For a candidate start `r<=U`, this yields

\[
\boxed{
y<3^{s+1}U+q3^s
=3^s(3U+q).}
\]

Thus low-slack candidate states have a deterministic endpoint-magnitude bound polynomial in `(U,h)` whenever `s=O(log h)`.

This does not give a deterministic global slack bound, but it can reduce the endpoint-residue search range in any branch where a slack bound has already been certified.

## 8. Use in the proof program

The fixed E/O cell can now carry three rigorously separated pieces of information:

\[
(h,q)
\quad\text{coefficient plane},
\]

\[
s=q-a_h
\quad\text{slack},
\]

\[
R\in
[3^q-2^q,\ R_{\max}^{\rm surv}(h,q)]
\quad\text{order-sensitive affine fiber}.
\]

This is a safe static-aggregation envelope: all parity words in the cell are retained, but their correction channel is bounded by an exact extremal word rather than by the much looser unconstrained permutation envelope.

The next useful question is whether the endpoint bound can be combined with the prefix first-hit lower bounds to certify additional cross-cell pruning for small candidate thresholds.