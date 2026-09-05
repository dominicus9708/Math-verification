# Exact target-displacement decomposition of the S10 defect numerator

Status: **EXACT / CLOSED decomposition; future additive defect remains OPEN**

## Purpose

The active A0 `s=1` Route-B physical gate carries the exact integer prefix-defect numerator

\[
N=C_T(q)-C_W(q),
\]

where `C_T(q)` is the correction of the first `q` target one-positions and `C_W(q)` is the correction of the realized pure-ballot prefix.

This note identifies `N` exactly with the ordered-one displacement defect.  Its main proof-level consequence is negative but important:

> Any lower bound that only re-expresses displacement already realized in the current prefix is already contained in `N` and must not be added again as an independent future defect.

A genuinely stronger `P_min` gate must instead certify displacement that is **forced in the unresolved future suffix**.

---

## 1. Ordered one positions

Let a realized prefix contain exactly `q` one-events at zero-based positions

\[
a_0<a_1<\cdots<a_{q-1}.
\]

Let the corresponding target one-positions be

\[
t_0<t_1<\cdots<t_{q-1}.
\]

In the active pure-ballot sector,

\[
\boxed{a_j\le t_j}\qquad(0\le j<q).
\]

Define the nonnegative displacement

\[
\boxed{s_j:=t_j-a_j\ge0.}
\]

---

## 2. Correction expansion

For any parity word with ordered one-positions `a_j`, the affine correction is

\[
\boxed{
C_W(q)=\sum_{j=0}^{q-1}3^{q-1-j}2^{a_j}.
}
\]

The target correction is

\[
\boxed{
C_T(q)=\sum_{j=0}^{q-1}3^{q-1-j}2^{t_j}.
}
\]

Therefore

\[
\begin{aligned}
N
&=C_T(q)-C_W(q)\\
&=\sum_{j=0}^{q-1}3^{q-1-j}\left(2^{t_j}-2^{a_j}\right)\\
&=\sum_{j=0}^{q-1}3^{q-1-j}2^{a_j}\left(2^{s_j}-1\right).
\end{aligned}
\]

Hence

\[
\boxed{
N=
\sum_{j=0}^{q-1}
3^{q-1-j}2^{a_j}(2^{s_j}-1).
}
\]

Every summand is nonnegative in the pure-ballot domain.

This is the integer, unnormalized counterpart of the already-used monotone prefix-defect representation.

---

## 3. Exact zero criterion

Because every summand above is nonnegative,

\[
\boxed{N=0\iff s_j=0\text{ for every }j<q.}
\]

Equivalently,

\[
\boxed{N=0\iff a_j=t_j\text{ for all already realized one-events}.}
\]

Thus a positive current defect means that at least one target one-event has already been displaced strictly left.

---

## 4. Earliest displaced-rank valuation decoder

Assume `N>0` and let

\[
j_*=\min\{j:s_j>0\}.
\]

Since the actual one-positions are strictly increasing, `a_{j_*}` is the smallest `a_j` among all displaced ranks.

For every displaced rank,

\[
3^{q-1-j}(2^{s_j}-1)
\]

is odd.  Therefore the corresponding summand has exact 2-adic valuation

\[
v_2\!\left(3^{q-1-j}2^{a_j}(2^{s_j}-1)\right)=a_j.
\]

All later displaced summands have strictly larger valuation because their `a_j` are strictly larger.  Hence the lowest nonzero dyadic bit cannot cancel.

Therefore

\[
\boxed{v_2(N)=a_{j_*}.}
\]

So the exact current defect numerator already decodes the position of the earliest displaced realized one-event.

This is a property of the integer correction defect itself, not an extra state coordinate.

---

## 5. Compatibility with the recursive S10 update

Suppose the current prefix has `q` one-events and defect `N`.  Append the next one at actual position `a_q`, whose target position is `t_q`.

The correction recurrence gives

\[
C_W(q+1)=3C_W(q)+2^{a_q},
\]

\[
C_T(q+1)=3C_T(q)+2^{t_q}.
\]

Consequently

\[
\boxed{
N'=3N+2^{t_q}-2^{a_q}.
}
\]

This is exactly the update used by the current eight-jump `P_min` certificate.

Thus the recursively carried scalar `N` and the complete ordered-displacement sum are mathematically identical descriptions of the already-realized prefix defect.

---

## 6. Relation to historical displacement / phase defect bounds

The repository already contains exact or lower-bound defect statements expressed through ordered-one displacement, Beatty/mechanical phase slack, first-crossing skew, and specialized branch geometry.

Whenever such a theorem is applied to the **same already-realized target prefix** and its hypotheses are satisfied, its defect contribution is a lower bound on, or a decomposition of, the same quantity represented here by `N` (up to the theorem's documented normalization).

Therefore such a bound cannot be used as

\[
N_{\rm strengthened}=N+N_{\rm historical\ prefix\ bound}.
\]

That would double-count already-realized displacement.

The correct uses are instead:

1. replace `N` by a cheaper certified lower bound if exact `N` is unavailable;
2. use the theorem to infer structural information from `N`;
3. or prove that unresolved future constraints force at least one **new** displacement not yet represented in `N`.

In the active source-preserving S10 state, exact `N` is already available in the `P_min` reconstruction, so item 3 is the only route that can strictly strengthen that gate.

---

## 7. Required form of a genuine future defect floor

Let the unresolved suffix eventually contain target ranks

\[
q,q+1,\ldots,q+r-1.
\]

A new theorem must force, from the current exact source/control state and unresolved Route-B constraints, a positive lower bound on the future contribution after the appropriate powers of 3 are accounted for.

For example, if a future rank `j>=q` is provably forced to satisfy

\[
a_j\le t_j-d,
\qquad d\ge1,
\]

then its eventual correction defect contributes a strictly positive atom

\[
3^{Q-1-j}2^{a_j}(2^d-1)
\]

at the final odd count `Q`.

But the powers of `3`, the final rank, and compatibility with all intermediate source-cylinder refinements must be handled exactly.  One must not simply add a present-normalized lower bound to `N` without transporting it through the correction recurrence.

Thus the open target is a **future-forced displacement theorem with exact transport**, not another prefix-defect estimate.

---

## 8. DSD classification

### EXACT / CLOSED

- ordered-one expansion of `C_W` and `C_T`;
- target-displacement decomposition of `N`;
- `N=0` iff all realized displacements vanish;
- `v_2(N)` decodes the earliest displaced actual one-position when `N>0`;
- equivalence with the recursive update `N'=3N+2^t-2^a`.

### NON-INDEPENDENT

Historical bounds that quantify only displacement already realized in the current target prefix are not additive to exact current `N`.

### OPEN

- any strictly positive defect forced by the unresolved future;
- exact transport of such a future floor into the current physical `P` score;
- a source-universal theorem valid on arbitrary active 14-root Route-B cylinders.

## Proof-level consequence

The high-value C4 search is narrowed from

\[
\text{``find another defect lower bound''}
\]

to

\[
\boxed{
\text{``force a new future target displacement from the current exact source state.''}
}
\]

Anything weaker risks re-counting `N` rather than strengthening it.
