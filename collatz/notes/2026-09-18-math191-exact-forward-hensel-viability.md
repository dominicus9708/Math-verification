# MATH-191 — exact forward Hensel viability recursion

Date: 2026-09-18

Status: `EXACT FINITE WITNESS RECURSION / FORWARD PRODUCT READY IN AUDITED RANGE / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-189 gives the exact forward Hensel difference recurrence

\[
W_r=3W_{r-1}+2^r(B_r-A_r),
\]

and MATH-190 gives a safe optimistic upper-bound prune.

This note completes the logical bridge by defining an exact finite forward viability recursion for a fixed candidate gap-block sequence and a fixed terminal `(Q,D)`.

The recursion asks only whether at least one competitor block sequence exists that ends in the same fixed-d Hensel class with positive translation credit.

No new depth or Collatz closure is claimed.

## 2. Candidate data

Let the candidate terminal parity word have

\[
Q=\text{odd count},
\qquad
D=\text{even count},
\]

and online gap blocks

\[
a_0,a_1,\ldots,a_Q,
\qquad
\sum_{r=0}^{Q}a_r=D.
\]

Let

\[
p_A(r)=\sum_{t<r}a_t
\]

and

\[
A_r=2^{p_A(r)}(2^{a_r}-1).
\]

The candidate block sequence is fixed by the actual MATH-188 parity path.

## 3. Forward competitor state

At the start of gap level `r`, use state

\[
\boxed{(p_B,W)}
\]

where

- `p_B` is the number of competitor even ranks already assigned to levels `<r`;
- `W` is the MATH-189 forward scaled signature difference after level `r-1`.

Initial state:

\[
\boxed{(p_B,W)=(0,0).}
\]

At level `r`, choose a competitor block length

\[
0\le b_r\le D-p_B.
\]

Its rank-power block is

\[
B_r=2^{p_B}(2^{b_r}-1).
\]

Then

\[
\boxed{
(p_B,W)
\longmapsto
\left(
 p_B+b_r,
 3W+2^r(B_r-A_r)
\right).
}
\]

Duplicate states are merged exactly.

## 4. Exact recursion

Define

\[
\operatorname{CanFwd}(r,p_B,W)
\]

to mean:

> there exists a choice of competitor blocks `b_r,...,b_Q` whose total competitor even count is exactly `D` and whose final forward credit lies in `3^Q Z_{>0}`.

Terminal condition after all levels have been processed:

\[
\boxed{
\operatorname{CanFwd}(Q+1,p_B,W)
\iff
p_B=D,
\quad
W>0,
\quad
3^Q\mid W.
}
\]

Recursive condition for `0<=r<=Q`:

\[
\boxed{
\operatorname{CanFwd}(r,p_B,W)
\iff
\bigvee_{b=0}^{D-p_B}
\operatorname{CanFwd}
\left(
 r+1,
 p_B+b,
 3W+2^r\bigl(B_r(b)-A_r\bigr)
\right).
}
\]

This is finite because

\[
0\le r\le Q+1,
\qquad
0\le p_B\le D,
\]

and the audited complete depth-41 coefficient-valid frontier of MATH-051 has

\[
D\le15.
\]

Memoization by `(r,p_B,W)` is exact.

## 5. Safe prefilters

Before recursion, a state may be removed if any exact necessary condition fails.

### Rank-count feasibility

If the remaining number of levels cannot accommodate the required competitor ranks under an imposed additional constraint, delete the state. In the unrestricted block-count representation, only

\[
p_B\le D
\]

is needed.

### MATH-190 optimistic bound

For any nonterminal level, if

\[
U_{r\to Q,D}\le0,
\]

then no continuation can finish with positive `W_Q`, so the state is false without further recursion.

### Exact terminal divisibility

At `r=Q+1`, require

\[
W\equiv0\pmod{3^Q}.
\]

This is not replaced by an approximate residue test.

## 6. Equivalence to direct Hensel comparison

For any complete competitor block sequence, MATH-189 proves

\[
W_Q=3^Q(\Sigma_B-\Sigma_A).
\]

Therefore the recursion returns true iff there exists a competitor satisfying

\[
\Sigma_B-\Sigma_A\in\mathbb Z_{>0}.
\]

This is exactly the fixed-d positive Hensel translation condition used by MATH-051.

Hence

\[
\boxed{
\operatorname{CanFwd}(A)=\text{true}
\iff
A\text{ is terminally Hensel-dominated in its exact fixed-d class.}
}
\]

within the same candidate/competitor scope.

## 7. Product-transducer interpretation

The MATH-188 chronological state need not retain the complete parity word.

It needs only

- the current unfinished candidate block `a_cur`;
- the forward competitor frontier / memo state induced by already completed gap levels;
- the existing MATH-188 analytic and same-integer address coordinates.

Thus the synchronized proof-facing state can be refined to

\[
\boxed{
\mathscr U^{++}
=(k,q,\Sigma,c,\mathcal P,A,B,M;
 a_{\rm cur},\mathcal V),
}
\]

where `V` is the finite set of non-pruned `(p_B,W)` competitor witness states for completed gap levels.

Two candidate histories with the same complete future-relevant tuple may be merged; histories are not distinguished merely because their raw parity words differ.

## 8. Regression role

The companion certificate checks all parity words through a small exhaustive depth and compares

1. direct pairwise `Sigma_B-Sigma_A` Hensel domination;
2. `CanFwd` recursion.

They agree exactly in the tested finite range.

This validates the coordinate conversion and recursion implementation. It does not extend MATH-051 beyond its separately audited depth-41 scope.

## 9. Remaining theorem target

The Hensel channel is no longer a conceptual blocker to the joint `r=1..21`, depth `2..41` recurrence.

The remaining hard proof obligation is still the same one isolated by MATH-186:

\[
\boxed{
\text{singleton overshoot / terminal same-integer closure}
}
\]

plus engineering the forward witness frontier so that the exact product executor remains tractable throughout the full audited range.

The correct next audit is therefore not another source enumeration. It is:

1. measure/derive frontier-state compression under exact merging and MATH-190 pruning;
2. attach the singleton terminal theorem;
3. regress all already-audited MATH-051 and paid-layer results against the product recurrence.

## 10. Claim boundary

Established:

- exact finite `CanFwd` recursion;
- exact terminal equivalence to positive fixed-d Hensel class domination;
- compatibility of the Hensel witness state with the chronological MATH-188 recurrence;
- a finite product-state formulation in the complete audited depth-41 `D<=15` range.

Not established:

- full-range product executor resource bounds;
- new depth-42 Hensel results;
- singleton overshoot closure;
- any new paid-layer closure;
- first-cell emptiness;
- the Collatz conjecture.
