# Bounded-displacement source reachability and cumulative future defect

Status: **EXACT finite-horizon theorem / jump-8 `c<=2` execution certified separately**

## 1. Displaced future ranks

At a current source state with odd count `q`, let the next target one-positions be

\[
t_q,t_{q+1},\ldots.
\]

For a future one-event `k`, write its actual position as

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0.
\]

A rank is **displaced** when

\[
d_k>0.
\]

Let

\[
D_r=\#\{0\le k<r:d_k>0\}
\]

be the number of displaced ranks among the first `r` future one-events.

---

## 2. Exact source-sensitive reachability set

For an exact affine source interval, define

\[
\mathcal R_{r,c}(s)
\]

as the set of nonempty exact source descendants after `r` future one-events whose path has

\[
D_r\le c.
\]

A child at actual one-position `u=t_q-d` is obtained by the usual exact valuation residue intersection.  The displacement budget updates by

\[
c_{used}'=c_{used}+\mathbf 1_{d>0}.
\]

Therefore the recursion for `R_{r,c}` is exact and source-preserving.  Distinct source payloads are not merged.

For a proof of emptiness it is safe to relax later predicates such as first-75 Hamming completion: if the larger source+pure-ballot reachability set is already empty, every stricter descendant class is also empty.

---

## 3. Mechanical target atom lower bound

Let `t_{r-1}` be the target position of the global rank-`r` one-event.  Since this position is a target `1`,

\[
Q(t_{r-1})=r-1,
\qquad
Q(t_{r-1}+1)=r.
\]

By the definition

\[
Q(n)=\min\{q:3^q>2^n\},
\]

the second equality implies

\[
3^{r-1}\le2^{t_{r-1}+1}.
\]

Equality between a positive power of `3` and a positive power of `2` is impossible here, hence

\[
\frac{2^{t_{r-1}}}{3^r}>\frac16.
\]

If the rank is displaced by at least one position,

\[
\epsilon_r
=\frac{2^{t_{r-1}}-2^{a_{r-1}}}{3^r}
=\frac{2^{t_{r-1}}}{3^r}(1-2^{-d})
>\frac1{12}.
\]

Thus every path satisfies

\[
\boxed{
\eta_{future}(r) > \frac{D_r}{12}.
}
\]

This is a normalized additive bound, so no later power-of-three transport is required.

---

## 4. Ballot-death-or-defect principle

If

\[
\mathcal R_{r,c}(s)=\varnothing,
\]

then every member of the parent source family either

1. loses the required pure-ballot condition before `r` future one-events, or
2. survives to the horizon with at least `c+1` displaced ranks.

Consequently every surviving horizon-`r` continuation has

\[
\boxed{
\eta_{future} > \frac{c+1}{12}.
}
\]

This lower bound can be composed with any active predicate that is monotone in the normalized defect.

---

## 5. Directed physical source-tail rejection

For the existing directed physical gate

\[
M_{lo}\eta+\Delta_{lo}X>B,
\]

suppose `R_{r,c}` is empty for every active parent.  Then every original source value either dies by the relaxed ballot gate or, if it survives, has future defect greater than `(c+1)/12`.

Therefore every source value satisfying

\[
\boxed{
M_{lo}\left(\eta_{current}+\frac{c+1}{12}\right)
+\Delta_{lo}X>B
}
\]

is closed immediately without expanding its horizon-`r` descendants.

This is a true source-value rejection, unlike a mere predicate-availability partition.

---

## 6. DSD classification

### EXACT / CLOSED

- displaced-rank definition;
- exact source reachability recursion;
- relaxed-class emptiness implication;
- per-displacement normalized defect `>1/12`;
- ballot-death-or-defect composition;
- monotone physical source-tail cut.

### Finite execution

A fixed `(r,c)` emptiness statement on the current jump-8 source forest is a finite exact result, not a universal Collatz theorem.

### Forbidden extrapolation

Observed horizons for `c=0,1,2` must not be extrapolated into an asymptotic displacement density without a separate theorem.

## Dependencies

- `AFFINE_VALUATION_CYLINDER_JUMP.md`
- `TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`
- `FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`
- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`
