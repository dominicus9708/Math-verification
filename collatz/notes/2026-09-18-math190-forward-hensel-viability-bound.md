# MATH-190 — forward Hensel viability upper bound

Date: 2026-09-18

Status: `EXACT SAFE PRUNING LEMMA / FORWARD WITNESS COMPRESSION / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-189 rewrites the fixed-d Hensel comparison in forward coordinates

\[
W_r=3W_{r-1}+2^r(B_r-A_r).
\]

The raw competitor frontier is exact but can retain witness states that can never finish with positive Hensel credit.

This note derives a safe necessary upper bound analogous in role to the MATH-051 `upper_possible()` test, but written in the chronological coordinates of MATH-189.

## 2. Current partial state and terminal target

Assume gap levels `0,...,r` have been completed.

Let

- `p_A` be the number of candidate even ranks already assigned;
- `p_B` be the number of competitor even ranks already assigned;
- `W=W_r` be the forward scaled signature difference;
- `(Q,D)` be a fixed terminal target, where `Q` is the final odd count and `D` the final even count.

Necessarily

\[
Q\ge r,
\qquad
D\ge p_A,
\qquad
D\ge p_B.
\]

Define remaining rank counts

\[
n_A=D-p_A,
\qquad
n_B=D-p_B.
\]

The remaining rank-power sums are fixed independently of how the remaining ranks are distributed among future gap levels:

\[
\boxed{
C_A=2^{p_A}(2^{n_A}-1),
}
\]

\[
\boxed{
C_B=2^{p_B}(2^{n_B}-1).
}
\]

## 3. Terminal expansion

Iterating the MATH-189 recurrence gives

\[
\boxed{
W_Q
=3^{Q-r}W_r
+\sum_{t=r+1}^{Q}2^t3^{Q-t}(B_t-A_t).
}
\]

The weight

\[
w_t:=2^t3^{Q-t}
=3^Q\left(\frac23\right)^t
\]

strictly decreases with `t`.

Therefore, among all possible future block placements with the same remaining rank-power totals:

- competitor contribution is maximized by placing all remaining competitor rank power at the earliest future level `r+1`;
- candidate subtraction is minimized in magnitude by placing all remaining candidate rank power at the latest level `Q`.

Hence every completion satisfies

\[
\boxed{
W_Q\le U_{r\to Q,D},
}
\]

where

\[
\boxed{
U_{r\to Q,D}
:=
3^{Q-r}W
+2^{r+1}3^{Q-r-1}C_B
-2^Q C_A.
}
\]

For `r=Q`, there is no future level and viability is decided directly from the terminal state rather than this future-placement bound.

## 4. Safe pruning rule

If

\[
\boxed{
U_{r\to Q,D}\le0,
}
\]

then no completion to the fixed terminal target `(Q,D)` can have

\[
W_Q>0.
\]

Therefore it certainly cannot satisfy the positive exact Hensel witness condition

\[
W_Q\in3^Q\mathbb Z_{>0}.
\]

Thus

\[
\boxed{
U_{r\to Q,D}\le0
\Longrightarrow
\text{the forward competitor state is impossible for terminal }(Q,D).
}
\]

This deletion is exact. It is not a heuristic score or probability cutoff.

## 5. Multi-terminal range `k<=41`

The joint executor observes many terminal depths. A witness state may be removed globally from the requested finite range only if it is impossible for every legal future terminal target.

Let `T` be the set of requested coefficient-valid terminal pairs `(Q,D)` satisfying

\[
Q+D\le41
\]

and the applicable coefficient/Hensel scope.

Define

\[
\boxed{
U_*:=\max_{(Q,D)\in T\text{ compatible}}U_{r\to Q,D}.
}
\]

If

\[
\boxed{U_*\le0,}
\]

then the witness state cannot dominate at any requested future terminal and may be deleted from the joint frontier.

A practical executor may keep terminal-specific viability masks instead of taking only the scalar maximum. That is stronger and still finite.

## 6. Relation to MATH-051

MATH-051 uses a reverse carry coordinate and an optimistic future bound before its exact recursive `can()` viability test.

MATH-190 is the forward-coordinate analogue:

- both put competitor ranks in the most favorable future positions;
- both put candidate ranks in the least damaging positions;
- both delete a state only when even that optimistic completion cannot produce positive credit.

The formulas need not look identical because their carry scalings and processing directions differ.

They must not be counted as independent Hensel filters; they are two representations of the same witness feasibility question.

## 7. Next exact strengthening

The upper bound ignores the terminal divisibility condition

\[
3^Q\mid W_Q
\]

and ignores exact candidate coefficient deadlines.

Therefore it is deliberately conservative.

The next strengthening is a memoized forward viability predicate

\[
\operatorname{CanFwd}(r,p_A,p_B,W;Q,D)
\]

that explores only competitor block lengths while taking the candidate block sequence from the actual MATH-188 path and checks both

1. exact terminal rank count `p_B=D`;
2. exact terminal condition `W_Q in 3^Q Z_{>0}`.

The MATH-190 bound is a safe prefilter for that recursion.

## 8. Claim boundary

Established:

- exact terminal expansion of the forward `W` recurrence;
- a monotone-weight optimistic upper bound on all future completions;
- safe deletion rule `U<=0` for a fixed terminal target;
- safe all-terminal deletion by checking the complete requested finite target set.

Not established:

- equivalence of raw frontier sizes to the optimized MATH-051 state counts;
- a completed forward `CanFwd` memoization proof/certificate;
- any new Hensel depth or paid-layer closure;
- singleton terminal closure;
- first-cell emptiness;
- the Collatz conjecture.
