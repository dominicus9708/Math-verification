# MATH-076 — combined slack/resolution Bellman potential before singleton handoff

Date: 2026-09-12

Status: `EXACT PRE-SINGLETON DEBT BOUND / FIRST-CELL OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note combines MATH-073 and MATH-075 only while the exact source cylinder still contains more than one ordinary source anchor.

## 1. Combined potential

Use

\[
\lambda=\frac{19}{503},
\qquad
\boxed{H_{uR}=-\lambda(u+R)},
\]

where

\[
R=\lceil\log_2 M\rceil
\]

is the exact same-integer source-resolution height of MATH-073.

For every nonempty child while the parent has `R>0`, exact dyadic refinement gives

\[
\Delta_R:=R-R'\ge1.
\]

For one shortcut edge the reduced cost is

\[
\boxed{
g=p-\lambda+H_{uR}'-H_{uR}
=p-\lambda+\lambda(u-u')+\lambda\Delta_R.
}
\]

## 2. Local classification for R>0

### Even edge

Coefficient validity requires `u>=1` and

\[
u'=u-1.
\]

Hence

\[
g=-\lambda+\lambda+\lambda\Delta_R
=\boxed{\lambda\Delta_R\ge\lambda}.
\]

### Odd edge, positive slack

For `u>=1` MATH-075 already gives strict positive margin even without the resolution term. Therefore every positive-slack odd edge remains strictly positive under the combined potential.

More explicitly:

- if `epsilon=0`,
  \[
  g=p-\lambda+\lambda\Delta_R\ge p>0;
  \]
- if `epsilon=1`,
  \[
  g=p-2\lambda+\lambda\Delta_R
  \ge p-\lambda
  >\frac1{12}-\frac{19}{503}
  =\frac{275}{6036}>0.
  \]

### Odd edge at u=0, epsilon=0

Here `p=0` and `u'=0`, so

\[
g=-\lambda+\lambda\Delta_R\ge0.
\]

### Odd edge at u=0, epsilon=1

Here `p=0` and `u'=1`, so

\[
\boxed{g=\lambda(\Delta_R-2).}
\]

Thus this edge is negative if and only if

\[
\boxed{\Delta_R=1},
\]

in which case

\[
\boxed{g=-\lambda}.
\]

Hence, while `R>0`, there is exactly one negative local state type:

\[
oxed{u=0,\ \varepsilon=1,\ R-R'=1.}
\]

## 3. Pairing of every nonterminal negative edge

A negative edge necessarily changes

\[
u:0\to1.
\]

Before another negative edge can occur, the path must return to `u=0`. Because odd steps never decrease `u`, this requires at least one coefficient-valid even edge.

While `R>0`, every such even edge has

\[
g\ge\lambda.
\]

Therefore each negative `-lambda` edge is compensated by the first later even edge required before another negative edge can occur.

Positive-slack odd edges between them contribute strictly positive reduced cost and cannot worsen the balance.

Thus all negative edges except possibly the final edge before the source becomes singleton can be paired injectively with later nonnegative/surplus edges.

## 4. Pre-singleton cumulative debt theorem

Let a coefficient-valid path segment begin at any state with `R>0` and end at the first state with `R=0`.

From the pairing argument,

\[
\boxed{
\sum_e g_e\ge-\lambda.
}
\]

The only possible unpaired debt is one final boundary `u=0, epsilon=1` edge that itself performs the singleton handoff.

This bound is independent of the number of shortcut steps before singleton resolution.

## 5. Translation back to raw penalty cost

Write the raw adjusted cost as

\[
J=\sum_e(p_e-\lambda).
\]

Since

\[
\sum_e g_e
=J+H_{uR}(\text{end})-H_{uR}(\text{start}),
\]

and the first-cell source calculation has

\[
R_0\le73,
\qquad
u_0=0,
\]

we have

\[
H_{\rm start}\ge-73\lambda.
\]

At singleton handoff `R=0` and `u>=0`, so a conservative endpoint estimate gives

\[
\boxed{J\ge-74\lambda.}
\]

The sharper value depends on the handoff slack. If the final unpaired negative edge is exactly the singleton edge then `u=1`, improving the endpoint accounting; `-74 lambda` is retained only as a uniform simple bound.

## 6. Relation to the MATH-060 allowance

MATH-060 needs globally

\[
\mathcal P_K\ge\lambda(K-89),
\]

or equivalently an adjusted-cost loss no worse than `89 lambda`.

MATH-076 shows that the entire unresolved multi-source prefix through singleton resolution costs at most

\[
74\lambda
\]

under a conservative translation.

Therefore the numerical additive budget not yet consumed is

\[
\boxed{89-74=15}
\]

step-equivalents.

This is not yet a first-cell proof: the post-singleton deterministic continuation still requires a uniform argument whose adjusted debt fits the remaining allowance or is closed by another exact contradiction.

## 7. DSD interpretation

MATH-075 localized negative unit weight to free odd edges on the coefficient boundary.
MATH-073 showed that every exact parity refinement consumes dyadic source resolution before singleton.
MATH-076 combines them:

\[
\boxed{
\text{boundary debt before singleton}
\text{ cannot accumulate linearly with path length.}
}
\]

It is uniformly bounded by one reduced slope unit, because every repeatable debt event forces a slack excursion whose return even edge pays the debt while resolution remains active.

This is a structural replacement for enumerating paid-count layers in the pre-singleton part of the final Bellman argument.

## 8. Claim boundary

Established:

- exact local classification under `H_{uR}` for `R>0`;
- unique negative local type `u=0, epsilon=1, Delta_R=1`;
- exact pairing of repeatable negative edges with required later even edges;
- cumulative pre-singleton reduced debt at least `-lambda`;
- conservative raw adjusted-cost bound `>=-74 lambda` using `R_0<=73`.

Not established:

- a post-singleton bound of `15 lambda`;
- first-cell emptiness;
- standalone closure of `r=2,...,13`;
- the Collatz conjecture.

## 9. Next target

After `R=0` the start is one ordinary integer and its future is deterministic, but the collection of possible singleton starts is still too large to enumerate directly.

The next task is therefore to combine:

1. MATH-061 exact macro-cylinder composition;
2. MATH-052/MATH-074 Hensel comparison quotient;
3. the coefficient-boundary free-odd language;

so that the post-singleton continuation can be certified symbolically rather than by scanning ordinary integers.

## Reproducibility

`collatz/src/2026_09_12_math076_combined_slack_resolution_bellman.py`
